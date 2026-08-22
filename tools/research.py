#!/usr/bin/env python3
"""Compute the analyses shown in the site's Research tab.

Reads the extracted page JSONs (and, if present, the semantic-field
annotations in data/research/domains.json) and writes
data/research/research.json, which tools/build_site.py injects into the site.

Every number shown on the Research page is produced here; the methodology
notes on the page describe exactly what this script does.

Usage: research.py [extracted-dir]
"""
import json, math, random, re, sys, unicodedata, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "research"

IRANIAN = {"persian","avestan","pahlavi","old persian","middle persian","sogdian","kurdish",
           "ossetic","parthian","indo-scythian","indo-schythian","old iranian","iranian",
           "baluchi","tajik","khotanese","scythian"}
SEMITIC = {"semitic","arabic","hebrew","akkadian","aramaic","syriac","phoenician","assyrian",
           "babylonian","ethiopian","egyptian","sumerian","arab"}
TURKIC = {"turkish","turkic","altaic","mongolian","tatar","uighur","chagatai","ottoman turkish"}
EURO = {"french","old french","latin","medieval latin","late latin","middle latin","vulgar latin",
        "greek","middle greek","english","old english","middle english","italian","spanish",
        "portuguese","russian","german","germanic","dutch","norman french","anglo-french",
        "provençal","provencal","new latin","modern latin"}

def famof(lang):
    if not lang: return "other"
    for p in str(lang).lower().split("/"):
        p = p.strip()
        if p in IRANIAN: return "iranian"
        if p in SEMITIC: return "semitic"
        if p in TURKIC: return "turkic"
        if p in EURO or p in {"indo-european","sanskrit","armenian","hittite","celtic","irish",
                              "welsh","hindustani","hindi","urdu","bengali","lithuanian","polish",
                              "czech","slavic","old slavic","old russian","church slavonic",
                              "prakrit","pali","frankish","old high german","middle high german",
                              "middle low german","middle german","middle dutch","old norse",
                              "norwegian","swedish","danish","gothic","tokharian","romanian"}:
            return "ie"
    return "other"

def is_modern_persian(lang):
    l = (lang or "").lower()
    return "persian" in l and "old" not in l and "middle" not in l

def is_modern_english(lang):
    l = (lang or "").lower()
    return bool(re.search(r"\benglish\b", l)) and "old" not in l and "middle" not in l

# ---------- transliteration folding ----------
VOWEL_FOLD = {"â":"a","ā":"a","à":"a","á":"a","ŭ":"u","û":"u","ū":"u","ù":"u",
              "î":"i","ī":"i","ì":"i","í":"i","ê":"e","ě":"e","è":"e","é":"e",
              "ô":"o","ō":"o","ò":"o","ó":"o"}
def fold(s, keep_special=True):
    """Fold a transliteration: collapse vowel diacritics, lowercase,
    keep the consonant distinctions č š ž ğ x q ` that carry sound-change signal."""
    s = unicodedata.normalize("NFC", str(s)).lower().strip()
    out = []
    for ch in s:
        if ch in VOWEL_FOLD: out.append(VOWEL_FOLD[ch])
        elif ch.isalpha() or (keep_special and ch in "`'ʼ’"): out.append(ch)
    return "".join(out)

def fold_plain(s):
    """Aggressive fold for similarity scoring: strip ALL diacritics, letters only."""
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if c.isascii() and c.isalpha())

def norm_key(s):
    """Normalization for identifying roots: keeps digits (Per 1 != Per 3)."""
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if c.isascii() and c.isalnum())

def lev(a, b):
    if not a or not b: return max(len(a), len(b))
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]

def sim(a, b):
    if not a and not b: return 0.0
    return 1.0 - lev(a, b) / max(len(a), len(b), 1)

def align(a, b):
    """Needleman-Wunsch alignment (match 0, mismatch 1, gap 1); return substitution pairs."""
    n, m = len(a), len(b)
    D = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): D[i][0] = i
    for j in range(m+1): D[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = min(D[i-1][j-1] + (a[i-1] != b[j-1]), D[i-1][j] + 1, D[i][j-1] + 1)
    subs = []
    i, j = n, m
    while i > 0 and j > 0:
        if D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]: subs.append((a[i-1], b[j-1]))
            i, j = i-1, j-1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return subs

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    e = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return (p, max(0.0, (c-e)/d), min(1.0, (c+e)/d))

# ---------- load ----------
def load(dirs):
    pages = {}
    for d in dirs:
        for f in sorted(Path(d).glob("page-*.json")):
            try: pg = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError: continue
            pages[pg["pdf_page"]] = pg
    entries = []
    for k in sorted(pages):
        for e in pages[k].get("entries", []):
            r = e.get("root", {})
            if r.get("name") and not r.get("redirect"):
                entries.append(e)
    return entries

def group_entries(entries):
    """Group chart entries by root (same normalization as the site)."""
    groups = collections.OrderedDict()
    for e in entries:
        key = (norm_key(e["root"]["name"]), norm_key(e["root"].get("lang") or ""))
        groups.setdefault(key, {"root": e["root"], "entries": []})["entries"].append(e)
    return list(groups.values())

def chain_langs(node, byid):
    """Languages of a node's ancestor chain, nearest first."""
    out, p, guard = [], node.get("parent", 0), 0
    while p and p in byid and guard < 80:
        out.append(byid[p].get("lang") or ""); p = byid[p].get("parent", 0); guard += 1
    return out

def route_of(node, byid, root_fam):
    """Borrowing route of a modern-Persian node (same rules as the Flows view)."""
    parts = [x.strip().lower() for l in chain_langs(node, byid) for x in l.split("/")]
    if any(x in SEMITIC for x in parts): return "arabic"
    if any(x in EURO for x in parts): return "euro"
    if any(x in TURKIC for x in parts) or root_fam == "turkic": return "turkic"
    if root_fam == "semitic": return "arabic"
    return "direct"

# ---------- analyses ----------
def persian_words(groups):
    """Every modern-Persian word with its route, root, gloss."""
    out = []
    for g in groups:
        fam = famof(g["root"].get("lang"))
        for e in g["entries"]:
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                if not is_modern_persian(n.get("lang")): continue
                r = route_of(n, byid, fam)
                for w in (n.get("words") or []):
                    out.append({"t": w.get("translit") or "", "s": w.get("script") or "",
                                "g": w.get("gloss") or "", "route": r, "fam": fam,
                                "root": g["root"]["name"]})
    return out

def domain_analysis(pwords):
    """Borrowing share per WOLD semantic field, using double-annotated glosses."""
    dom_file = OUT / "domains.json"
    if not dom_file.exists(): return None
    dom = json.loads(dom_file.read_text(encoding="utf-8"))
    lab, agree_n, both_n = dom["labels"], dom["n_agree"], dom["n_both"]
    per_field = collections.Counter(); borrowed = collections.Counter()
    used = skipped = 0
    for w in pwords:
        f = lab.get(w["g"])           # only glosses where both passes agreed
        if not f: skipped += 1; continue
        used += 1
        per_field[f] += 1
        if w["route"] != "direct": borrowed[f] += 1
    fields = []
    for f, n in per_field.most_common():
        if n < 15: continue           # too small for a stable share
        p, lo, hi = wilson(borrowed[f], n)
        fields.append({"code": f, "n": n, "b": borrowed[f],
                       "share": round(p, 3), "lo": round(lo, 3), "hi": round(hi, 3)})
    fields.sort(key=lambda x: -x["share"])
    overall_b = sum(borrowed.values()); overall_n = sum(per_field.values())
    op, olo, ohi = wilson(overall_b, overall_n)
    return {"fields": fields, "used": used, "skipped": skipped,
            "agreement": round(agree_n / max(1, both_n), 3),
            "overall": {"share": round(op, 3), "lo": round(olo, 3), "hi": round(ohi, 3)}}

def doublet_analysis(groups):
    """Inherited vs Arabic-mediated shapes of the same root: aligned sound substitutions."""
    pairs = []
    for g in groups:
        fam = famof(g["root"].get("lang"))
        byroute = collections.defaultdict(list)
        for e in g["entries"]:
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                if not is_modern_persian(n.get("lang")): continue
                r = route_of(n, byid, fam)
                for w in (n.get("words") or []):
                    if w.get("translit"):
                        for piece in re.split(r"[,;]", w["translit"]):
                            piece = piece.strip()
                            if len(fold(piece)) >= 3:
                                byroute[r].append({"t": piece, "s": w.get("script") or "",
                                                   "g": w.get("gloss") or ""})
        if "direct" not in byroute or "arabic" not in byroute: continue
        # match each Arabic-mediated shape to its most similar inherited sibling
        for wb in byroute["arabic"]:
            fb = fold(wb["t"])
            best, bs = None, 0.0
            for wd in byroute["direct"]:
                s = sim(fold(wd["t"]), fb)
                if s > bs: best, bs = wd, s
            if best and bs >= 0.5 and fold(best["t"]) != fb:
                pairs.append({"root": g["root"]["name"], "sim": round(bs, 2),
                              "inh": best, "bor": wb})
    # aggregate aligned substitutions
    rules = collections.Counter(); rule_ex = collections.defaultdict(list)
    for p in pairs:
        for a, b in align(fold(p["inh"]["t"]), fold(p["bor"]["t"])):
            rules[(a, b)] += 1
            if len(rule_ex[(a, b)]) < 3:
                rule_ex[(a, b)].append([p["inh"]["t"], p["bor"]["t"], p["inh"]["s"], p["bor"]["s"]])
    VOW = set("aeiou")
    top = [{"a": a, "b": b, "n": n, "vowel": a in VOW and b in VOW, "ex": rule_ex[(a, b)]}
           for (a, b), n in rules.most_common(40) if n >= 2]
    ex_pairs = sorted(pairs, key=lambda p: -p["sim"])
    seen, show = set(), []
    for p in ex_pairs:
        if p["root"] in seen: continue
        seen.add(p["root"])
        show.append({"root": p["root"], "inh": p["inh"]["t"], "inh_s": p["inh"]["s"],
                     "bor": p["bor"]["t"], "bor_s": p["bor"]["s"], "g": p["inh"]["g"] or p["bor"]["g"]})
        if len(show) >= 16: break
    return {"n_pairs": len(pairs), "n_roots": len({p["root"] for p in pairs}),
            "rules": top, "examples": show}

def build_graphs(groups):
    """Root-level ☞ graph and word-level derivation(+☞) graph."""
    idx = {}
    for i, g in enumerate(groups):
        full = norm_key(g["root"]["name"])
        idx.setdefault(full, i)
        for part in g["root"]["name"].split(","):
            idx.setdefault(norm_key(part), i)
    redirects = {}
    def find_root(name):
        n = norm_key(name)
        for _ in range(3):
            if n in idx: return idx[n]
            if n in redirects: n = redirects[n]; continue
            break
        for k in idx:
            if k.startswith(n) or n.startswith(k): return idx[k]
        return -1
    redges = set()                       # root graph (☞)
    wadj = collections.defaultdict(set)  # word graph: derivation + ☞
    def wedge(a, b): wadj[a].add(b); wadj[b].add(a)
    word_v = []
    for gi, g in enumerate(groups):
        rv = ("r", gi)
        for ei, e in enumerate(g["entries"]):
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                nv = ("n", gi, ei, n["id"])
                p = n.get("parent", 0)
                wedge(nv, ("n", gi, ei, p) if p and p in byid else rv)
                if n.get("words"): word_v.append((nv, n))
                for w in (n.get("words") or []):
                    for s in (w.get("see") or []):
                        t = find_root(s)
                        if t >= 0 and t != gi:
                            redges.add((min(gi, t), max(gi, t)))
                            wedge(nv, ("r", t))
    return redges, wadj, word_v, find_root

def network_analysis(groups, redges):
    n = len(groups)
    adj = collections.defaultdict(set)
    for a, b in redges: adj[a].add(b); adj[b].add(a)
    degs = [len(adj[i]) for i in range(n)]
    # components
    seen, comps = set(), []
    for s in range(n):
        if s in seen: continue
        q, comp = [s], {s}; seen.add(s)
        while q:
            v = q.pop()
            for u in adj[v]:
                if u not in seen: seen.add(u); comp.add(u); q.append(u)
        comps.append(comp)
    giant = max(comps, key=len)
    # clustering coefficient (average, over nodes with deg>=2)
    cc, cn = 0.0, 0
    for v in range(n):
        nb = list(adj[v])
        if len(nb) < 2: continue
        links = sum(1 for i in range(len(nb)) for j in range(i+1, len(nb)) if nb[j] in adj[nb[i]])
        cc += 2*links/(len(nb)*(len(nb)-1)); cn += 1
    # categorical assortativity by origin family (Newman r)
    fams = [famof(g["root"].get("lang")) for g in groups]
    cats = sorted(set(fams))
    m = len(redges)
    e = collections.Counter(); a_i = collections.Counter(); b_i = collections.Counter()
    for x, y in redges:
        e[(fams[x], fams[y])] += 1; e[(fams[y], fams[x])] += 1
        a_i[fams[x]] += 1; a_i[fams[y]] += 1
    tr = sum(e[(c, c)] for c in cats) / (2*m)
    sq = sum((a_i[c]/(2*m))**2 for c in cats)
    assort = (tr - sq) / (1 - sq) if sq < 1 else 0.0
    # family-pair edge counts
    fpairs = collections.Counter()
    for x, y in redges:
        fpairs[tuple(sorted((fams[x], fams[y])))] += 1
    # betweenness (Brandes) on giant component -> top bridges
    bt = collections.Counter()
    gnodes = list(giant)
    for s in gnodes:
        S, P, sigma, dist = [], collections.defaultdict(list), collections.Counter(), {}
        sigma[s] = 1; dist[s] = 0; Q = collections.deque([s])
        while Q:
            v = Q.popleft(); S.append(v)
            for w in adj[v]:
                if w not in dist: dist[w] = dist[v]+1; Q.append(w)
                if dist[w] == dist[v]+1: sigma[w] += sigma[v]; P[w].append(v)
        delta = collections.Counter()
        for w in reversed(S):
            for v in P[w]: delta[v] += sigma[v]/sigma[w]*(1+delta[w])
            if w != s: bt[w] += delta[w]
    hubs = sorted(range(n), key=lambda i: -degs[i])[:8]
    bridges = [i for i, _ in bt.most_common(8)]
    # cross-family bridges: high-betweenness roots whose edges span >=2 families
    deghist = collections.Counter(degs)
    return {
        "nodes": n, "edges": len(redges),
        "density": round(2*len(redges)/(n*(n-1)), 5),
        "components": len(comps), "giant": len(giant),
        "isolates": sum(1 for d in degs if d == 0),
        "avg_deg": round(sum(degs)/n, 2), "max_deg": max(degs),
        "clustering": round(cc/max(1, cn), 3),
        "assortativity": round(assort, 3),
        "fam_pairs": [{"a": k[0], "b": k[1], "n": v} for k, v in fpairs.most_common()],
        "deg_hist": [{"d": d, "n": deghist[d]} for d in sorted(deghist)],
        "hubs": [{"root": groups[i]["root"]["name"], "fam": famof(groups[i]["root"].get("lang")),
                  "deg": degs[i]} for i in hubs],
        "bridges": [{"root": groups[i]["root"]["name"], "fam": famof(groups[i]["root"].get("lang")),
                     "bt": round(bt[i], 0), "deg": degs[i]} for i in bridges],
    }

def sixdeg_analysis(wadj, word_v, seed=42):
    rng = random.Random(seed)
    verts = list(wadj)
    vset = [v for v, _ in word_v]
    # giant component of the word graph
    seen = set(); comps = []
    for s in verts:
        if s in seen: continue
        q, comp = [s], {s}; seen.add(s)
        while q:
            v = q.pop()
            for u in wadj[v]:
                if u not in seen: seen.add(u); comp.add(u); q.append(u)
        comps.append(comp)
    giant = max(comps, key=len)
    in_g = [v for v in vset if v in giant]
    # sampled BFS distances between word-bearing nodes in the giant component
    sources = rng.sample(in_g, min(400, len(in_g)))
    hist = collections.Counter(); total = 0; far = (0, None, None)
    for s in sources:
        dist = {s: 0}; Q = collections.deque([s])
        while Q:
            v = Q.popleft()
            for u in wadj[v]:
                if u not in dist: dist[u] = dist[v]+1; Q.append(u)
        for t in rng.sample(in_g, min(120, len(in_g))):
            if t == s or t not in dist: continue
            hist[dist[t]] += 1; total += 1
            if dist[t] > far[0]: far = (dist[t], s, t)
    cum, median = 0, None
    for d in sorted(hist):
        cum += hist[d]
        if median is None and cum >= total/2: median = d
    frac_conn = len(giant & set(vset)) / max(1, len(vset))
    return {"giant_frac": round(frac_conn, 3), "n_words_nodes": len(vset),
            "median": median, "sampled_pairs": total,
            "hist": [{"d": d, "n": hist[d]} for d in sorted(hist) if d <= 30],
            "diameter_lb": far[0]}

def simcog_analysis(groups, redges, seed=42):
    """Can surface string similarity recover the book's relatedness judgments?"""
    rng = random.Random(seed)
    # ☞ closeness between root charts (for excluding near-related "negatives")
    radj = collections.defaultdict(set)
    for a, b in redges: radj[a].add(b); radj[b].add(a)
    def roots_near(a, b):
        if a == b: return True
        if b in radj[a]: return True
        return any(b in radj[x] for x in radj[a])
    per, eng = [], []
    for gi, g in enumerate(groups):
        fam = famof(g["root"].get("lang"))
        for e in g["entries"]:
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                if is_modern_persian(n.get("lang")):
                    tgt, route = per, route_of(n, byid, fam)
                elif is_modern_english(n.get("lang")):
                    tgt, route = eng, None
                else: continue
                for w in (n.get("words") or []):
                    if not w.get("translit"): continue
                    for piece in re.split(r"[,;]", w["translit"]):
                        piece = piece.strip()
                        f = fold_plain(piece)
                        if len(f) >= 3:
                            tgt.append({"gi": gi, "t": piece, "f": f, "g": w.get("gloss") or "",
                                        "s": w.get("script") or "", "root": g["root"]["name"],
                                        "route": route, "fam": fam})
    by_gi = collections.defaultdict(lambda: ([], []))
    for w in per: by_gi[w["gi"]][0].append(w)
    for w in eng: by_gi[w["gi"]][1].append(w)
    pos = []
    for gi, (ps, es) in by_gi.items():
        for p in ps:
            for q in es:
                pos.append((sim(p["f"], q["f"]), p, q))
    rng.shuffle(pos); pos = pos[:6000]
    neg = []
    while len(neg) < len(pos):
        p, q = rng.choice(per), rng.choice(eng)
        if p["gi"] != q["gi"]: neg.append((sim(p["f"], q["f"]), p, q))
    # AUC via rank statistic
    allv = [(s, 1) for s, _, _ in pos] + [(s, 0) for s, _, _ in neg]
    allv.sort(key=lambda x: x[0])
    ranks, i = {}, 0
    rsum = 0.0
    while i < len(allv):
        j = i
        while j < len(allv) and allv[j][0] == allv[i][0]: j += 1
        avg = (i + j + 1) / 2  # 1-based average rank
        for k in range(i, j):
            if allv[k][1] == 1: rsum += avg
        i = j
    n1, n0 = len(pos), len(neg)
    auc = (rsum - n1*(n1+1)/2) / (n1*n0)
    # hidden cognates: related pairs with lowest similarity.
    # Persian side restricted to INHERITED words (route=direct, no compounds,
    # not proper nouns) so the examples are deep cognacy, not obscured loans.
    def propern(w): return w["t"][:1].isupper()
    seen, hidden = set(), []
    for s, p, q in sorted(pos, key=lambda x: (x[0], -len(x[1]["f"]) - len(x[2]["f"]))):
        if p["root"] in seen: continue
        if p["route"] != "direct" or propern(p) or propern(q): continue
        if len(p["f"]) < 4 or len(q["f"]) < 4 or not p["s"]: continue
        if "-" in p["t"] or " " in p["t"] or "-" in q["t"] or " " in q["t"]: continue
        seen.add(p["root"])
        hidden.append({"per": p["t"], "per_s": p["s"], "eng": q["t"], "root": p["root"],
                       "sim": round(s, 2), "g": q["g"] or p["g"]})
        if len(hidden) >= 12: break
    # false friends: SYSTEMATIC search — Persian/English pairs whose folded forms
    # are identical or one edit apart but whose root charts are unrelated.
    # Guards against artifacts: the Persian word must NOT itself be a European
    # loan (else it is the same word charted twice, not a false friend), proper
    # nouns are excluded, and the two roots must not be within 2 ☞ hops.
    eng_by_len = collections.defaultdict(list)
    for q in eng: eng_by_len[len(q["f"])].append(q)
    seenf, ff = set(), []
    for p in per:
        L = len(p["f"])
        if L < 3 or p["route"] == "euro" or propern(p): continue
        for dL in (0, 1, -1):
            for q in eng_by_len.get(L + dL, []):
                if p["gi"] == q["gi"] or propern(q): continue
                s = sim(p["f"], q["f"])
                if s < (1.0 if L <= 4 else 0.8): continue
                if roots_near(p["gi"], q["gi"]): continue
                key = (p["f"], q["f"])
                if key in seenf: continue
                seenf.add(key)
                ff.append({"per": p["t"], "per_s": p["s"], "eng": q["t"], "sim": round(s, 2),
                           "per_root": p["root"], "eng_root": q["root"], "pg": p["g"], "qg": q["g"]})
    ff.sort(key=lambda x: (-x["sim"], -len(x["per"])))
    n_ff = len(ff)
    ff = ff[:12]
    hb = collections.Counter(); hbn = collections.Counter()
    for s, _, _ in pos: hb[min(9, int(s*10))] += 1
    for s, _, _ in neg: hbn[min(9, int(s*10))] += 1
    return {"auc": round(auc, 3), "n_pos": n1, "n_neg": n0, "n_false_friends": n_ff,
            "pos_hist": [hb[i] for i in range(10)], "neg_hist": [hbn[i] for i in range(10)],
            "hidden": hidden, "false_friends": ff}

POETS = {  # normalized name -> (display en, display fa, floruit-era label, approx midpoint year)
    "ferdowsi": ("Ferdowsî", "فردوسی", "c. 940–1020", 980),
    "hafez": ("Hâfez", "حافظ", "c. 1315–1390", 1350),
    "molavi": ("Molavî (Rumi)", "مولوی", "1207–1273", 1240),
    "sadi": ("Sa‘dî", "سعدی", "c. 1210–1292", 1250),
    "rudaki": ("Rŭdakî", "رودکی", "c. 858–941", 900),
    "farrokhi": ("Farrokhî", "فرخی سیستانی", "d. 1037", 1020),
    "nezami": ("Nezâmî", "نظامی", "1141–1209", 1175),
    "asadi": ("Asadî Tŭsî", "اسدی توسی", "d. c. 1073", 1060),
    "naserkhosrow": ("Nâser-Khosrow", "ناصرخسرو", "1004–1088", 1045),
    "visoramin": ("Vîs o Râmîn (Gorgânî)", "ویس و رامین (گرگانی)", "c. 1050", 1050),
}
def poet_key(p):
    k = fold_plain(p)
    k = k.replace("-", "").replace(" ", "")
    for cand in POETS:
        if k.startswith(cand) or cand.startswith(k): return cand
    return None

def poetry_analysis(groups):
    per_poet = collections.defaultdict(lambda: {"n": 0, "arabic": 0, "euro": 0, "turkic": 0})
    for g in groups:
        fam = famof(g["root"].get("lang"))
        for e in g["entries"]:
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                q = n.get("quote")
                if not (q and q.get("text") and q.get("poet")): continue
                if not is_modern_persian(n.get("lang")): continue
                k = poet_key(q["poet"])
                if not k: continue
                r = route_of(n, byid, fam)
                st = per_poet[k]; st["n"] += 1
                if r in st: st[r] += 1
    rows = []
    for k, st in per_poet.items():
        if st["n"] < 10: continue
        nb = st["arabic"] + st["euro"] + st["turkic"]
        p, lo, hi = wilson(nb, st["n"])
        en, fa, era, year = POETS[k]
        rows.append({"key": k, "en": en, "fa": fa, "era": era, "year": year,
                     "n": st["n"], "borrowed": nb, "arabic": st["arabic"],
                     "share": round(p, 3), "lo": round(lo, 3), "hi": round(hi, 3)})
    rows.sort(key=lambda r: r["year"])
    return rows

def roundtrip_analysis(groups):
    trips = []
    for g in groups:
        for e in g["entries"]:
            byid = {n["id"]: n for n in e.get("nodes", [])}
            for n in e.get("nodes", []):
                if not is_modern_persian(n.get("lang")): continue
                chain = chain_langs(n, byid)
                lc = [c.lower() for c in chain]
                if not any(is_modern_persian(c) for c in chain): continue
                mids = []
                started = False
                for c in chain:  # nearest ancestor first; walk up to the earlier Persian stage
                    if is_modern_persian(c): started = True; break
                    mids.append(c)
                if not (started and mids): continue
                w = next((w for w in (n.get("words") or []) if w.get("translit")), None)
                if not w: continue
                trips.append({"root": g["root"]["name"], "word": w["translit"],
                              "script": w.get("script") or "", "g": w.get("gloss") or "",
                              "via": " → ".join(reversed(mids))})
    uniq = {}
    for tr in trips:
        uniq.setdefault((tr["root"], tr["word"]), tr)
    trips = list(uniq.values())
    seen, out = set(), []
    for tr in sorted(trips, key=lambda x: -len(x["via"])):
        key = fold_plain(tr["word"])
        if key in seen: continue
        seen.add(key); out.append(tr)
    return {"n": len(trips), "n_words": len(seen), "examples": out[:14]}

def main(argv):
    dirs = argv or [ROOT / "data" / "extracted" / "batch"]
    entries = load(dirs)
    groups = group_entries(entries)
    pw = persian_words(groups)
    routes = collections.Counter(w["route"] for w in pw)
    redges, wadj, word_v, _ = build_graphs(groups)
    res = {
        "n_roots": len(groups),
        "n_persian_words": len(pw),
        "routes": dict(routes),
        "domains": domain_analysis(pw),
        "doublets": doublet_analysis(groups),
        "network": network_analysis(groups, redges),
        "sixdeg": sixdeg_analysis(wadj, word_v),
        "simcog": simcog_analysis(groups, redges),
        "poets": poetry_analysis(groups),
        "roundtrips": roundtrip_analysis(groups),
    }
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / "research.json"
    out.write_text(json.dumps(res, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{out}: {out.stat().st_size/1024:.0f} KB")
    return res

if __name__ == "__main__":
    main(sys.argv[1:])
