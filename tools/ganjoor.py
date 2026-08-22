#!/usr/bin/env python3
"""Corpus analyses against the Ganjoor corpus of Persian poetry.

Reads the official Ganjoor database dump (MySQL, from
https://github.com/ganjoor/ganjoor-db — data/dump.sql.gz), matches every
verse token against the dictionary's modern-Persian words with the same
conservative morphology the site's verse-linker uses, and computes:

  1. the poets' purism gradient over full divans (not Nourai's citations),
  2. first-attestation dates for borrowed words -> influx curves,
  3. token-frequency-weighted borrowing statistics.

Usage:
  ganjoor.py --import <dump.sql.gz> [ganjoor.db]   # one-time: MySQL dump -> SQLite
  ganjoor.py <ganjoor.db> [extracted-dir ...]      # writes data/research/ganjoor.json
"""
import collections, gzip, json, random, re, sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import research

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "research"

# ---------- Ganjoor poets: id in the official DB -> (en, fa, floruit year CE) ----------
# Floruit = rough midpoint of the poet's productive life. Excluded on purpose:
# Bâbâ Tâher (dialectal corpus), Abŭ-Sa'îd (apocryphal attribution),
# Hojvîrî & Nasrollâh Monshî (prose works), and small contemporary accounts.
GPOETS = {
    12: ("Rŭdakî", "رودکی", 900),
    45: ("Kasâ'î", "کسایی", 980),
    4: ("Ferdowsî", "فردوسی", 1000),
    15: ("Farrokhî", "فرخی سیستانی", 1020),
    14: ("Manŭchehrî", "منوچهری", 1030),
    38: ("Gorgânî", "فخرالدین اسعد گرگانی", 1050),
    13: ("Nâser-Khosrow", "ناصرخسرو", 1050),
    52: ("Asadî Tŭsî", "اسدی توسی", 1060),
    17: ("Mas'ŭd Sa'd", "مسعود سعد سلمان", 1090),
    3: ("Khayyâm", "خیام", 1090),
    10: ("Sanâ'î", "سنایی", 1110),
    54: ("Mahsatî", "مهستی گنجوی", 1120),
    37: ("Jabalî", "عبدالواسع جبلی", 1140),
    18: ("Anvarî", "انوری", 1160),
    16: ("Khâqânî", "خاقانی", 1160),
    6: ("Nezâmî", "نظامی", 1180),
    9: ("Attâr", "عطار", 1190),
    56: ("Bâbâ Afzal", "باباافضل کاشانی", 1190),
    5: ("Molavî (Rumi)", "مولوی", 1250),
    21: ("Erâqî", "عراقی", 1250),
    7: ("Sa'dî", "سعدی", 1255),
    34: ("Amîr Khosrow", "امیرخسرو دهلوی", 1290),
    31: ("Seyf Farghânî", "سیف فرغانی", 1300),
    19: ("Owhadî", "اوحدی", 1310),
    23: ("Shabestarî", "شیخ محمود شبستری", 1310),
    20: ("Khâjŭ", "خواجوی کرمانی", 1320),
    40: ("Salmân Sâvajî", "سلمان ساوجی", 1350),
    33: ("Obeyd Zâkânî", "عبید زاکانی", 1350),
    2: ("Hâfez", "حافظ", 1360),
    51: ("Shâh Ne'matollâh", "شاه نعمت‌الله ولی", 1390),
    24: ("Jâmî", "جامی", 1460),
    50: ("Helâlî", "هلالی جغتایی", 1510),
    29: ("Mohtasham", "محتشم کاشانی", 1550),
    11: ("Vahshî", "وحشی", 1560),
    46: ("Orfî", "عرفی", 1580),
    30: ("Sheykh Bahâ'î", "شیخ بهایی", 1590),
    47: ("Ârtîmânî", "رضی‌الدین آرتیمانی", 1600),
    22: ("Sâ'eb", "صائب تبریزی", 1640),
    39: ("Feyz Kâshânî", "فیض کاشانی", 1640),
    43: ("Bîdel", "بیدل دهلوی", 1690),
    25: ("Hâtef", "هاتف اصفهانی", 1760),
    32: ("Forŭghî Bastâmî", "فروغی بسطامی", 1830),
    44: ("Qâ'ânî", "قاآنی", 1830),
    602: ("Sabzevârî", "ملا هادی سبزواری", 1840),
    55: ("Sabŭhî", "شاطرعباس صبوحی", 1870),
    42: ("Eqbâl Lâhŭrî", "اقبال لاهوری", 1915),
    27: ("Bahâr", "ملک‌الشعرای بهار", 1920),
    8: ("Parvîn", "پروین اعتصامی", 1930),
    501: ("Nîmâ", "نیما یوشیج", 1935),
    41: ("Rahî Mo'ayyerî", "رهی معیری", 1945),
    35: ("Shahriyâr", "شهریار", 1950),
    504: ("Forŭgh", "فروغ فرخزاد", 1955),
    503: ("Sohrâb", "سهراب سپهری", 1960),
    502: ("Shâmlŭ", "احمد شاملو", 1965),
    506: ("Akhavân Sâles", "مهدی اخوان ثالث", 1965),
    505: ("Sîmîn Behbahânî", "سیمین بهبهانی", 1975),
}

# ---------- normalization + morphology (mirror of the site's linkFa fallback) ----------
FA_RUN = re.compile(r"[؀-ۿ‌ً-ٕ]+")

def norm_fa(s):
    s = re.sub(r"[ً-ْٰـ]", "", str(s))
    s = s.replace("ي", "ی").replace("ئ", "ی").replace("ك", "ک")
    s = re.sub(r"[أإآ]", "ا", s)
    return s.replace("ة", "ه")

ZWNJ = "‌"
FA_PREFIXES = ["نمی" + ZWNJ, "نمی", "همی" + ZWNJ, "همی", "می" + ZWNJ, "می"]
FA_SUF = ["هایی", "های", "ها", "ترین", "تر", "مان", "تان", "شان", "یم", "ید", "ند", "ان", "ست", "ه", "م", "ش"]
FA_BLOCK = {"ای", "همی", "نمی", "می", "بی", "ها", "وی", "ولی", "گویی", "بران", "مرا", "ترا", "چرا",
            "زیرا", "برای", "باری", "جایی", "رای", "نهند", "بدین", "بدانگه", "انگه", "برنده", "بنای",
            "جمله", "سوده", "بستان", "لاد", "نشاید", "نبینی", "بشوی", "بگوی", "گویم", "گوید", "شویم",
            "جویم", "تویی", "بمانند", "نیوش", "ایی", "بارد", "بامن", "باستان", "نامور", "نسرین",
            "بسیج", "بسام", "بتیم", "بسغر", "خوشه", "درهمه", "میرود", "میلایم", "دری"}
FA_ALIAS = {"چو": "چون"}

def ok_n(c):
    return c.endswith("دن") or c.endswith("تن")

def variants(k):
    """Fallback candidates for a token that has no exact dictionary match."""
    if k in FA_BLOCK:
        return []
    bases = [k]
    for p in FA_PREFIXES:
        if k.startswith(p) and len(k) - len(p) >= 3:
            bases.append(k[len(p):]); break
    if k[0] in "بن" and len(k) >= 4:
        bases.append(k[1:])
    for b in list(bases):
        if b.endswith(ZWNJ):
            bases.append(b[:-1])
    cand = []
    for b in bases:
        if len(b) >= 3 and ok_n(b + "ن"):
            cand.append(b + "ن")
        if b != k:
            cand.append(b)
        for s in FA_SUF:
            if b.endswith(s) and len(b) - len(s) >= 3:
                c = b[:-len(s)]
                if ok_n(c + "ن"):
                    cand.append(c + "ن")
                cand.append(c)
        if b.endswith("ی") and len(b) - 1 >= 2:
            c = b[:-1]
            if ok_n(c + "ن"):
                cand.append(c + "ن")
            cand.append(c)
    if k in FA_ALIAS:
        cand.append(FA_ALIAS[k])
    return cand

# ---------- dictionary lemma map ----------
# Corpus homographs whose only charted sense is the wrong one for running text:
# kon (imperative of kardan, not "kon fayakun"), ar (poetic agar, not the French
# unit), and xatâ ("error", not the Cathay place name).
STAT_DROP = {"خطا", "اند", "پی", "سری", "ار", "کن", "رز", "سودا", "ال", "انتن"}
STAT_REMAP = {"کن": "کردن", "ار": "اگر"}

def build_lexicon(dirs):
    """norm_fa(script token) -> lemma record. A script form that is itself a
    multi-word compound (pî jâmeh, šîš kabâb) is skipped — its fragments are
    not that word — except parenthesized single-word variants. Tokens whose
    charted homographs disagree on the route are dropped as ambiguous."""
    groups = research.group_entries(research.load(dirs))
    pwords = research.persian_words(groups)
    lex, routes = {}, collections.defaultdict(set)
    for w in pwords:
        if not w["s"]:
            continue
        for chunk in re.split(r"[()،,؛;·]", w["s"]):
            toks = FA_RUN.findall(chunk)
            if len(toks) != 1:
                continue
            k = norm_fa(toks[0])
            if len(k) <= 1:
                continue
            routes[k].add(w["route"])
            if k not in lex:
                lex[k] = {"t": w["t"], "g": w["g"], "route": w["route"], "root": w["root"]}
    ambiguous = {k for k, rs in routes.items() if len(rs) > 1}
    for k in ambiguous:
        del lex[k]
    for k in STAT_DROP:
        lex.pop(k, None)
    for k, target in STAT_REMAP.items():
        if target in lex:
            lex[k] = lex[target]
    return lex, ambiguous, pwords

def make_matcher(lex):
    cache = {}
    def match(k):
        if k in cache:
            return cache[k]
        r = lex.get(k)
        if r is None and k not in FA_BLOCK:
            for c in variants(k):
                if c in lex:
                    r = lex[c]; break
        cache[k] = r
        return r
    return match

# ---------- corpus walk ----------
def iter_poet_verses(db, poet_id):
    q = """SELECT v.text FROM verses v
           JOIN poems pm ON pm.id = v.poemId
           JOIN categories c ON c.id = pm.categoryId
           WHERE c.poetId = ? AND v.position >= 0"""
    for (text,) in db.execute(q, (poet_id,)):
        yield text or ""

def analyze(db_path, dirs):
    lex, ambiguous, pwords = build_lexicon(dirs)
    match = make_matcher(lex)
    db = sqlite3.connect(db_path)

    poet_rows = []
    lemma_tokens = collections.Counter()            # lemma key -> corpus token count
    lemma_first = {}                                # lemma key -> earliest attesting (year, poet_en)
    key_of = {}                                     # cache: token -> lemma key or None
    lemma_route = {k: v["route"] for k, v in lex.items()}

    for pid, (en, fa, year) in sorted(GPOETS.items(), key=lambda x: x[1][2]):
        tot = matched = 0
        by_route = collections.Counter()
        per_lemma = collections.Counter()
        for text in iter_poet_verses(db, pid):
            for tok in FA_RUN.findall(text):
                k = norm_fa(tok)
                if len(k) <= 1:
                    continue
                tot += 1
                if k in key_of:
                    lk = key_of[k]
                else:
                    rec = match(k)
                    lk = None
                    if rec is not None:
                        # resolve back to the lexicon key that matched
                        lk = k if k in lex else next((c for c in variants(k) if c in lex), None)
                    key_of[k] = lk
                if lk is None:
                    continue
                matched += 1
                by_route[lemma_route[lk]] += 1
                per_lemma[lk] += 1
        for lk, n in per_lemma.items():
            lemma_tokens[lk] += n
            if n >= 2 and (lk not in lemma_first or year < lemma_first[lk][0]):
                lemma_first[lk] = (year, en)
        # The gradient is measured over the poet's DISTINCT charted vocabulary
        # (types), the same yardstick as the book-citation analysis — not over
        # running tokens, which high-frequency inherited words would dominate.
        troutes = collections.Counter(lemma_route[lk] for lk in per_lemma)
        types = len(per_lemma)
        tnb = troutes["arabic"] + troutes["euro"] + troutes["turkic"]
        p, lo, hi = research.wilson(tnb, max(1, types))
        # rarefied share: a big divan reaches deeper into rare (more often
        # borrowed) vocabulary, so also sample every poet down to the same
        # number of running words for a size-controlled check.
        pop = [lk for lk, c in per_lemma.items() for _ in range(c)]
        n_r = min(1800, len(pop))
        rlem = set(random.Random(42).sample(pop, n_r))
        r_b = sum(1 for lk in rlem if lemma_route[lk] != "direct")
        poet_rows.append({
            "en": en, "fa": fa, "year": year,
            "tokens": tot, "matched": matched,
            "coverage": round(matched / max(1, tot), 3),
            "types": types, "borrowed": tnb,
            "arabic": troutes["arabic"], "euro": troutes["euro"], "turkic": troutes["turkic"],
            "share": round(p, 4), "lo": round(lo, 4), "hi": round(hi, 4),
            "rtypes": len(rlem), "rshare": round(r_b / max(1, len(rlem)), 4),
        })
        print(f"  {en:20s} {year}  tokens={tot:8d} types={types:6d} "
              f"borrowed={p:.1%}  rarefied={r_b/max(1,len(rlem)):.1%}", file=sys.stderr)

    # ---- 2. first attestations -> influx per half-century ----
    influx = collections.defaultdict(lambda: collections.Counter())
    for lk, (year, _) in lemma_first.items():
        b = (year // 50) * 50
        influx[b][lemma_route[lk]] += 1
    influx_rows = [{"y": b, "direct": influx[b]["direct"], "arabic": influx[b]["arabic"],
                    "euro": influx[b]["euro"], "turkic": influx[b]["turkic"]}
                   for b in range(900, 2000, 50)]
    # earliest attestations for the two datable waves, plus the modern European wave
    examples = {}
    for route in ("euro", "turkic"):
        rows = sorted(((y, poet, lk) for lk, (y, poet) in lemma_first.items()
                       if lemma_route[lk] == route and lemma_tokens[lk] >= 3),
                      key=lambda x: (x[0], -lemma_tokens[x[2]]))
        examples[route] = [{"w": lex[lk]["t"], "s": lk, "g": lex[lk]["g"],
                           "year": y, "poet": poet} for y, poet, lk in rows[:10]]
    modern = sorted(((y, -lemma_tokens[lk], poet, lk) for lk, (y, poet) in lemma_first.items()
                     if lemma_route[lk] == "euro" and y >= 1850 and lemma_tokens[lk] >= 2),
                    key=lambda x: (x[0], x[1]))
    examples["euro_modern"] = [{"w": lex[lk]["t"], "s": lk, "g": lex[lk]["g"],
                                "year": y, "poet": poet} for y, _, poet, lk in modern[:10]]

    # ---- 3. frequency weighting ----
    tok_total = sum(lemma_tokens.values())
    tok_borrowed = sum(n for lk, n in lemma_tokens.items() if lemma_route[lk] != "direct")
    tok_routes = collections.Counter()
    for lk, n in lemma_tokens.items():
        tok_routes[lemma_route[lk]] += n
    # dictionary-type baseline over the same lexicon
    typ_total = len(lex)
    typ_borrowed = sum(1 for v in lex.values() if v["route"] != "direct")
    # WOLD fields, token-weighted
    dom_file = OUT / "domains.json"
    fields_rows = []
    if dom_file.exists():
        lab = json.loads(dom_file.read_text(encoding="utf-8"))["labels"]
        f_tok = collections.Counter(); f_bor = collections.Counter()
        for lk, n in lemma_tokens.items():
            # 1–2-letter forms are heavily homographic in Persian; their gloss
            # (hence field) is unreliable even when the route is not.
            if len(lk) < 3:
                continue
            f = lab.get(lex[lk]["g"])
            if not f:
                continue
            f_tok[f] += n
            if lemma_route[lk] != "direct":
                f_bor[f] += n
        for f, n in f_tok.most_common():
            if n < 2000:
                continue
            fields_rows.append({"code": f, "n": n, "share": round(f_bor[f] / n, 4)})
        fields_rows.sort(key=lambda x: -x["share"])
    # most frequent words, per side
    def top_words(pred, n=12):
        rows = [(lemma_tokens[lk], lk) for lk in lemma_tokens if pred(lemma_route[lk])]
        rows.sort(reverse=True)
        return [{"w": lex[lk]["t"], "s": lk, "g": lex[lk]["g"], "n": c} for c, lk in rows[:n]]

    out = {
        "source": "ganjoor.net official database dump (github.com/ganjoor/ganjoor-db)",
        "n_poets": len(poet_rows),
        "corpus_tokens": sum(r["tokens"] for r in poet_rows),
        "matched_tokens": sum(r["matched"] for r in poet_rows),
        "lexicon_size": typ_total,
        "ambiguous_dropped": len(ambiguous),
        "poets": poet_rows,
        "influx": influx_rows,
        "influx_examples": examples,
        "weighted": {
            "token_total": tok_total, "token_borrowed": tok_borrowed,
            "token_share": round(tok_borrowed / max(1, tok_total), 4),
            "token_routes": {r: tok_routes[r] for r in ("direct", "arabic", "euro", "turkic")},
            "type_share": round(typ_borrowed / max(1, typ_total), 4),
            "fields": fields_rows,
            "top_inherited": top_words(lambda r: r == "direct"),
            "top_borrowed": top_words(lambda r: r != "direct"),
        },
    }
    return out, lemma_tokens, lex, key_of

def import_dump(dump_path, db_path):
    """Convert the official MySQL dump into the SQLite file this script reads."""
    def parse_tuples(vals):
        out, i, n = [], 0, len(vals)
        while i < n:
            if vals[i] == "(":
                row, cur, i = [], [], i + 1
                while i < n:
                    c = vals[i]
                    if c == "'":
                        buf, i = [], i + 1
                        while i < n:
                            if vals[i] == "\\":
                                e = vals[i + 1]
                                buf.append({"n": "\n", "t": "\t", "r": "\r", "0": "\0",
                                            "'": "'", '"': '"', "\\": "\\"}.get(e, e))
                                i += 2
                            elif vals[i] == "'":
                                if i + 1 < n and vals[i + 1] == "'":
                                    buf.append("'"); i += 2
                                else:
                                    i += 1; break
                            else:
                                buf.append(vals[i]); i += 1
                        row.append("".join(buf)); cur = []
                    elif c == ",":
                        if cur: row.append("".join(cur)); cur = []
                        i += 1
                    elif c == ")":
                        if cur: row.append("".join(cur))
                        out.append(row); i += 1
                        break
                    else:
                        cur.append(c); i += 1
            else:
                i += 1
        return out

    db = sqlite3.connect(db_path)
    db.executescript("""
    DROP TABLE IF EXISTS poets; DROP TABLE IF EXISTS categories;
    DROP TABLE IF EXISTS poems; DROP TABLE IF EXISTS verses;
    CREATE TABLE poets(id INT, name TEXT);
    CREATE TABLE categories(id INT, poetId INT, name TEXT, parentId INT);
    CREATE TABLE poems(id INT, categoryId INT, title TEXT);
    CREATE TABLE verses(poemId INT, vorder INT, position INT, text TEXT);
    """)
    iv = lambda x: None if x == "NULL" else int(x)
    with gzip.open(dump_path, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            m = re.match(r"INSERT INTO `(\w+)` VALUES (.*);\s*$", line, re.S)
            if not m:
                continue
            tbl, rows = m.group(1), parse_tuples(m.group(2))
            if tbl == "poets":
                db.executemany("INSERT INTO poets VALUES (?,?)", [(int(r[0]), r[1]) for r in rows])
            elif tbl == "categories":
                db.executemany("INSERT INTO categories VALUES (?,?,?,?)",
                               [(int(r[0]), iv(r[1]), r[2], iv(r[3])) for r in rows])
            elif tbl == "poems":
                db.executemany("INSERT INTO poems VALUES (?,?,?)",
                               [(int(r[0]), iv(r[1]), r[2]) for r in rows])
            elif tbl == "verses":
                db.executemany("INSERT INTO verses VALUES (?,?,?,?)",
                               [(iv(r[1]), iv(r[2]) or 0, iv(r[3]) if r[3] != "NULL" else 0, r[4])
                                for r in rows])
    db.execute("CREATE INDEX vi ON verses(poemId)")
    db.execute("CREATE INDEX pi ON poems(id)")
    db.commit()
    print(f"{db_path}: imported")

def main(argv):
    if not argv:
        print(__doc__); return
    if argv[0] == "--import":
        import_dump(argv[1], argv[2] if len(argv) > 2 else "ganjoor.db")
        return
    db_path = argv[0]
    dirs = argv[1:] or [ROOT / "data" / "extracted" / "batch"]
    out, lemma_tokens, lex, key_of = analyze(db_path, dirs)
    dest = OUT / "ganjoor.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{dest}: {out['n_poets']} poets, {out['corpus_tokens']} tokens, "
          f"{out['matched_tokens']} matched ({out['matched_tokens']/out['corpus_tokens']:.1%})")

if __name__ == "__main__":
    main(sys.argv[1:])
