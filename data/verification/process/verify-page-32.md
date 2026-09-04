# Verification process log — verify-page-32


## [2026-09-04T15:06:26.777Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 32 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-32.json. The reference table /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json is now complete (local OCR texts live under /home/sfmqrb/git/rishe/data/verification/sources/refs/, paginated with form-feeds; each entry gives page offsets and lookup hints). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py as required) and the local reference texts for Nourai's own citations (quote what you find). Write /home/sfmqrb/git/rishe/data/verification/page-32.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 32` to confirm complete coverage (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T15:06:29.678Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T15:06:29.708Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which
5	this repository (`/home/sfmqrb/git/rishe`) turned into JSON
6	(`data/extracted/batch/page-<pdf>.json`). Compact text renderings of the charts
7	are in `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-<pdf>.txt`.
8	
9	Each chart is a tree: a ROOT box, then nodes `#id (parent #p) [Language] refs=… | word «script» : gloss`.
10	An arrow parent→child in the book means "child derives from parent". `parent #0` = derives from the root.
11	Redirect entries (`ROOT X -> redirect to Y`) need no verification: skip them (do not include them).
12	
13	## Your job, per chart (entry)
14	
15	1. Verify the ROOT itself: is the reconstructed root real, is the language label right,
16	   is the gloss right? (e.g. PIE *dʰeyǵʰ- "knead, form" — Pokorny 244.)
17	2. Verify EVERY node (every derivation edge parent→child, and every word in the node):
18	   - Is the word real, in that language, with that meaning?
19	   - Does it really descend from (or was borrowed from) the parent as drawn?
20	   - Give the **derivation explanation**: how, phonetically and historically, the child form
21	     arises from the parent form. Be concrete: name the sound changes (e.g. "Av. pairi-daēza-
22	     → MP *pardēz; Greek borrowed it in the 5th c. BCE as paradeisos (Xenophon), Greek
23	     -ei- rendering Iranian -ē-; Latin paradīsus; Old French paradis; Middle English
24	     paradis > paradise"), the route of borrowing (which people/era/text), and the
25	     semantic shift ("walled enclosure" → "royal park" → "Garden of Eden" via the Septuagint).
26	     For Persian words descend through Old Iranian → Middle Persian → New Persian and name
27	     the intermediate forms when sources give them (e.g. OP didā- / Av. daēza- → MP diz →
28	     NP dež/dez). For Arabic loans note the Arabic stem, and for Arabic-mediated round-trips
29	     (Persian → Arabic → Persian) say so.
30	3. Give a verdict per node and per root:
31	   - `confirmed` — independent modern sources agree with the chart (same root, same route).
32	   - `plausible` — sources give a compatible but not identical picture, or the derivation
33	     is accepted by some scholars but not all; explain the difference.
34	   - `disputed` — modern scholarship (Wiktionary with citations, Etymonline, AHD, Cheung,
35	     Hasandust, Beekes, de Vaan, Kroonen, MacKenzie…) prefers a DIFFERENT origin, or the
36	     word is unrelated. Explain what the modern view is.
37	   - `unverified` — you could not find any independent source either way (say what you tried).
38	   - `transcription_suspect` — the JSON data looks like a transcription error from the scan
39	     (a misread letter, an impossible form, a wrong Persian script); say what you think the
40	     book actually printed and why.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	
46	## Checking Nourai's OWN cited references (required)
47	
48	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
49	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
50	You must check them:
51	
52	- The bibliography key (abbreviation → book) is in
53	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt`.
54	- Where each reference can be read online is in
55	  `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json`
56	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`).
57	- If `local_file` is set, the OCR text of that book is on disk: grep it for the headword
58	  (try several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and,
59	  if `page_offset` is given, locate the cited page (pages are separated by form-feeds; use
60	  `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one page). Read the entry and judge whether
61	  it actually says what Nourai's arrow says.
62	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
63	- Do this for at least ONE cited reference per node (the most authoritative available:
64	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
65	  BQT/MON for Persian). If none of a node's references is accessible, say so.
66	
67	Add to every node a `ref_check` array:
68	
69	```json
70	"ref_check": [
71	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
72	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
73	]
74	```
75	
76	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
77	word but a different/looser derivation) · `contradicts` (the reference says something else)
78	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
79	not accessible online). Quote the key phrase of the reference in `note` when you can.
80	
81	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
82	
83	
84	## Process documentation (required)
85	
86	The owner wants to be able to audit every step later. Therefore:
87	
88	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
89	  curl), run
90	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
91	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
92	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
93	  one Bash command to save time.)
94	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
95	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
96	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
97	  be re-run.
98	- Your full transcript (every tool call and result) is exported automatically by the
99	  coordinator; nothing else needed for that.
100	
101	## Sources to use (in roughly this order)
102	
103	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
104	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
105	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
106	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
107	  Use URL-encoded Persian/Arabic script for those pages.
108	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
109	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
110	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
111	  appendix; the online appendix is the updated edition of the same list.
112	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
113	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
114	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
115	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
116	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
117	  if needed for a hard case.
118	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
119	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
120	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
121	
122	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
123	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
124	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
125	which are where errors are likelier.
126	
127	## Output — write ONE file per page
128	
129	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
130	
131	```json
132	{
133	  "pdf_page": 126,
134	  "book_page": 96,
135	  "verified_by": "claude-fable-5-1",
136	  "verified_on": "2026-09-04",
137	  "entries": [
138	    {
139	      "entry": 0,
140	      "root": "Dheigh, Dhigha",
141	      "verdict": "confirmed",
142	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
143	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
144	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
145	      "nodes": [
146	        {
147	          "id": 6,
148	          "lang": "Avestan",
149	          "words": "pairi-daeza",
150	          "verdict": "confirmed",
151	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
152	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
153	        },
154	        {
155	          "id": 9,
156	          "lang": "Greek",
157	          "words": "paradeisos",
158	          "verdict": "confirmed",
159	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
160	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
161	        }
162	      ]
163	    }
164	  ]
165	}
166	```
167	
168	Rules:
169	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
170	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
171	- `words` = the transliterations of the node joined by "; " (copy from the chart).
172	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
173	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
174	- Keep `note` on the entry for root-level comments and for anything cross-cutting
175	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
176	- If a node lists several words, cover each word; if they differ in verdict, use the worst
177	  verdict for the node and explain per word in `derivation`.
178	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
179	  from root Mad"), evaluate it: say which side modern scholarship takes.
180	- Every node has `ref_check` (array, may contain a single `not_checked` item).
181	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
182	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
183	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
184	  Do not paste the JSON back into your reply.
185	
```


## [2026-09-04T15:06:35.643Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt; echo ----; cat /home/sfmqrb/git/rishe/data/extracted/batch/page-32.json; echo ----; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'));print(list(d.keys()))\"; echo ----; cat /home/sfmqrb/git/rishe/tools/verify_check.py | head -80; ls /home/sfmqrb/git/rishe/data/verification/ | head; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/",
 "description": "Read chart, JSON, refs list, checker"
}
```


### [2026-09-04T15:06:38.281Z] TOOL RESULT

```
=== PDF page 32 (book page 2) ===
--- entry 0 ---
ROOT [Indo-European] Ab 1, Ap 1 : water  (refs POK:1)  PART 2
#1 (parent #0) [Avestan / Pahlavi] refs=KLN:2 | âp : water
  #2 (parent #1) [Persian] refs=HRN:1; AEF:2 | âb «آب ۲» : glitter (as on water surface) ; âberŭ «آبرو» : "facial shine", good reputation ; âftâb «آفتاب» : "glitter shine", sun
    #3 (parent #2) [Arabic] refs=AFM:7; FVF:11 | âb-bahâ : "glittering shine", elegance ; abboha : magnificence, elegance
      #4 (parent #3) [Persian] refs=MON:131 | obbohat «أبهت» : elegance
----
{
  "pdf_page": 32,
  "book_page": 2,
  "entries": [
    {
      "root": {
        "name": "Ab 1, Ap 1",
        "lang": "Indo-European",
        "refs": "POK:1",
        "gloss": "water"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Pahlavi",
          "refs": "KLN:2",
          "words": [
            {"translit": "âp", "gloss": "water", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:1; AEF:2",
          "words": [
            {"translit": "âb", "gloss": "glitter (as on water surface)", "script": "آب ۲"},
            {"translit": "âberŭ", "gloss": "\"facial shine\", good reputation", "script": "آبرو"},
            {"translit": "âftâb", "gloss": "\"glitter shine\", sun", "script": "آفتاب"}
          ],
          "note": null,
          "quote": {
            "text": "چو آمد به برج حمل آفتاب - جهان گشت با فرّ و آیین و آب",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "AFM:7; FVF:11",
          "words": [
            {"translit": "âb-bahâ", "gloss": "\"glittering shine\", elegance", "script": null},
            {"translit": "abboha", "gloss": "magnificence, elegance", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:131",
          "words": [
            {"translit": "obbohat", "gloss": "elegance", "script": "أبهت"}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
----
['BQT', 'MON', 'SOD', 'SNS', 'FFD', 'FVA', 'AEF', 'VOP', 'FSF', 'TAD', 'FVQ', 'VDQ', 'FVF', 'ETM', 'TZF', 'SAP', 'IRN', 'AFM', 'FRS', 'ZMA', 'FAF', 'ARK', 'AMD', 'DZA', 'KAS', 'DMO', 'SBK', 'VGH', 'VIE', 'AKM', 'ZFS', 'SOR', 'FNI', 'VSF', 'FVS', 'FIB', 'IRT', 'SNB', 'KFL', 'NFI', 'MMF', 'MZF', 'ARM', 'ARB', 'AHD', 'POK', 'KLN', 'HRN', 'IEC', 'KNT', 'SYN', 'WLD', 'ISS', 'OEW', 'HUB', 'BRT', 'FSD', 'SKT', 'PRT', 'NYB', 'HJB', 'PHN', 'LKT', 'WEB', 'SIN', 'AHM', 'CEL', 'GPL', 'MAG', 'DEV', 'DRM', 'ZAW', 'SLW', 'BLY', 'KGW', 'SHP', 'AID', 'OXF', 'MPP', 'DVS', 'SPG', 'ARP', 'PHD', 'TYL', 'LAM', 'UNV', 'LAT', 'NAT', 'TTS', 'DOZ', 'AVG', 'LEW', 'SDQ', 'ROE', 'AFA', 'FWE', 'MFL', 'TLM', 'BST', 'HID', 'AIN', 'ZAP', 'AWH', 'PEI', 'EAV', 'SOG', 'LST', 'PLA', 'AKD', 'RCH']
----
#!/usr/bin/env python3
"""Check data/verification/*.json against data/extracted/batch/*.json.

Reports pages with no verification file, entries/nodes missing from the
verification, invalid verdicts, and a verdict tally.  Exit code 1 if any
verification file is malformed or incomplete.
"""
import glob, json, os, sys, collections

VERDICTS = {"confirmed", "plausible", "disputed", "unverified", "transcription_suspect"}
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "extracted", "batch")
VER = os.path.join(ROOT, "data", "verification")


def page_no(path):
    return int(os.path.basename(path).split("-")[1].split(".")[0])


def main(argv):
    only = set(int(a) for a in argv[1:])
    missing_pages, problems = [], []
    tally = collections.Counter()
    root_tally = collections.Counter()
    ref_tally = collections.Counter()
    nodes_total = nodes_done = 0
    flagged = []
    for src in sorted(glob.glob(os.path.join(SRC, "page-*.json")), key=page_no):
        pg = page_no(src)
        if only and pg not in only:
            continue
        d = json.load(open(src))
        vpath = os.path.join(VER, f"page-{pg}.json")
        entries = [(i, e) for i, e in enumerate(d["entries"]) if not e["root"].get("redirect")]
        need = sum(len(e["nodes"]) for _, e in entries)
        nodes_total += need
        if not os.path.exists(vpath):
            if need:
                missing_pages.append(pg)
            continue
        try:
            v = json.load(open(vpath))
        except Exception as ex:
            problems.append(f"page {pg}: invalid JSON ({ex})")
            continue
        ventries = {ve.get("entry"): ve for ve in v.get("entries", [])}
        for i, e in entries:
            ve = ventries.get(i)
            if ve is None:
                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
                continue
            rv = ve.get("verdict")
            if rv not in VERDICTS:
                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
            else:
                root_tally[rv] += 1
                if rv in ("disputed", "transcription_suspect"):
                    flagged.append((pg, e["root"]["name"], "ROOT", rv, ve.get("note", "")))
            vnodes = {vn.get("id"): vn for vn in ve.get("nodes", [])}
            for n in e["nodes"]:
                vn = vnodes.get(n["id"])
                if vn is None:
                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
                    continue
                nv = vn.get("verdict")
                if nv not in VERDICTS:
                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
                    continue
                nodes_done += 1
                tally[nv] += 1
                if not vn.get("derivation"):
                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
                if nv in ("disputed", "transcription_suspect"):
                    flagged.append((pg, e["root"]["name"], f"#{n['id']} {vn.get('words','')}", nv, vn.get("derivation", "")))
                for rc in vn.get("ref_check") or []:
                    ref_tally[rc.get("status")] += 1
    print(f"nodes verified: {nodes_done}/{nodes_total}")
    print("node verdicts:", dict(tally))
    print("root verdicts:", dict(root_tally))
    print("ref checks:", dict(ref_tally))
page-101.json
page-126.json
page-311.json
page-31.json
page-345.json
process
sources
AFA.txt
AFM_pages.txt
AFM.txt
AHD_watkins1985.txt
AHM.txt
AID.txt
AIN.txt
AKD.txt
ARB_abdulraheem.txt
ARB_mo3rb.txt
ARP.txt
AVG.txt
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
BRT.txt
BST.txt
CHEUNG.txt
DEV.txt
DOZ.txt
DRM.txt
EAV_studies.txt
FRS_pages.txt
FRS.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
FSF_pages.txt
FSF.txt
FVQ_pages.txt
FVQ.txt
GPL.txt
HENNING_selected_papers.txt
HID.txt
HJB.txt
HRN.txt
HUB.txt
IEC.txt
ISS_alt_DKS.txt
KFL.txt
KLN_1966.txt
KLN_1971.txt
KNT.txt
LAM.txt
LAT.txt
LEW_1910.txt
LKT.txt
LST.txt
MON_part1.txt
MON_part2.txt
MPP.txt
NAT_2005.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
```


## [2026-09-04T15:06:46.225Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','KLN','HRN','AEF','AFM','FVF','MON']: print(k, json.dumps(d[k],ensure_ascii=False,indent=1))\"; echo ----; grep -n -E '^(POK|KLN|HRN|AEF|AFM|FVF|MON)' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt; echo ----; python3 -c \"\nimport json;d=json.load(open('data/verification/page-31.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\"; echo ----; cat tools/fetch_source.py | head -60; ls data/verification/sources/web | head; ls data/verification/sources/web | wc -l",
 "description": "Inspect refs metadata, page-31 example, fetch tool"
}
```


### [2026-09-04T15:06:48.154Z] TOOL RESULT

```
POK {
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ]
}
KLN {
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ]
}
HRN {
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed."
}
AEF {
 "title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence",
 "kind": "none",
 "url": null,
 "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "none online; proxy via HRN/HUB."
}
AFM {
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled."
}
FVF {
 "title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968",
 "kind": "website",
 "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)",
 "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.",
 "local_file": null,
 "page_offset": null,
 "covers_etymology": true,
 "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."
}
MON {
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view."
}
----
----
{
 "pdf_page": 31,
 "book_page": 1,
 "verified_by": "claude-fable-5-1",
 "verified_on": "2026-09-04",
 "entries": [
  {
   "entry": 0,
   "root": "Ab 1, Ap 1",
   "verdict": "confirmed",
   "modern_form": "PIE *h₂ep- 'water, body of water; river' (Pokorny 2. ap- 51, with the by-form ab- 1); Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš",
   "note": "Pokorny IEW p.1 has 'ab- Wasser, Fluß' (Lat. amnis, OIr. ab, Welsh afon) and refers to '2. ap- Wasser, Fluß' on p.51 (Skt. ap-, Av. āfš/āpəm, Hitt. ḫap(a)-, Toch. āp); Nourai's double heading 'Ab 1, Ap 1' merely combines the two Pokorny lemmas, which modern scholarship (Wiktionary after Wodtko-Irslinger-Schneider NIL, Rastorgueva-Edelman ESIJa I 312) treats as variants of one root *h₂ep-/*h₂eb-. AHD/Watkins: 'ap-2 Water, river. Iranian ap- in Persian ab, water: JULEP [Pok. 2. ap- 51]'. Root, language label and gloss are correct. Weak points on this page are the four sub-derivations in node 2 (āftāb, ābādān, āxwarr are NOT from āb 'water' in modern etymology), the whole ābnīk > al-anbīq > alembic branch (nodes 5-6; every modern source derives anbīq from Greek ámbix, as Nourai's own NOTE half-admits), and the 'Sanskrit' label on Punjab (node 15), which is a Persian coinage.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂ep-",
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
    "https://en.wiktionary.org/wiki/آب"
   ],
   "ref_check": [
    {
     "ref": "POK:1",
     "status": "supports",
     "note": "POK_01.txt line 19 (IEW p.1): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß und abō(n) Affe'. The Iranian forms are under 2. ap- p.51 (English edition POK_full.txt: 'Root ap-2 (*hap-2) water, river ... Old Indic ap- f. water ... Avestan Nom. Sg. āfš, Akk. Sg. āpəm'). Pokorny is still the standard reference for this root."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Pahlavi",
     "words": "âp",
     "verdict": "confirmed",
     "derivation": "Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm, cf. the month-name Ābān 'of the waters'), Old Persian ap- (loc. sg. apiyā in DSf) both continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-, pl. āpaḥ; Hitt. ḫap(a)- 'river'; Lat. amnis < *abnis). In Middle Persian the word is āp/āb (Book Pahlavi ʾp, Manichaean ʾb; MacKenzie 'ab ... water'), the intervocalic/final -p- lenited to -b (spirant β) in the Sasanian period. The label 'Avestan / Pahlavi' correctly collapses the Old-Iranian and Middle-Persian stages.",
     "sources": [
      "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš",
      "https://en.wiktionary.org/wiki/آب"
     ],
     "ref_check": [
      {
       "ref": "KLN:2",
       "status": "supports",
       "note": "KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'"
      }
     ]
    },
    {
     "id": 2,
     "lang": "Pahlavi",
     "words": "âp-tab; zâ-âp; ô-pât-ân; av-xur",
     "verdict": "disputed",
     "derivation": "Only one of the four compounds really contains āp 'water'. (a) âp-tab = MP āftāb 'sunshine, sun' (Pahlavi ʾptʾb; NP āftāb): modern etymology (Cheung 2007 s.v. tap; Wiktionary) derives it from Proto-Iranian *abi-tāpah 'shining upon', i.e. the preverb abi- (> MP af-/āf-) + tāp- 'to shine, be hot'; Horn (Grundriss no. 3) likewise separated an āb 'Glanz' (cf. Skt. ābhā-) from āb 'water'. Nourai's gloss 'a (hot) glittering object' shows he is forcing āb 'water/lustre' into the compound; the water-root is not involved. (b) zâ-âp = MP zahābag (MacKenzie: 'zahabag [zhʾpk, NP zahāb] spring, source') = *zah 'spring, depth' + āb + suffix -ag; this one is genuinely āb 'water' and gives NP zahāb/zāb. (c) ô-pât-ân = ābādān: as a common noun MP ābādān 'thriving, populous' is ā-pāta- 'protected, cultivated' (root pā- 'protect', Nourai's own ☞Pa) + -ān, with no water element; as the city name, medieval Arabic ʿAbbādān (Balādhurī: founded by ʿAbbād of Tamīm; Ptolemy/Marcian Apphadana/Apphana) was officially respelled Ābādān in 1935, and the 'āb + pā(d) coast-guard station' reading is a modern proposal by B. Farahvashi (= Nourai's IRN), not a demonstrated etymology. (d) av-xur = MP āxwarr 'manger, stable' (Pahlavi ʾhwl; NP āxor/āxur, Arm. axoṙ): MacKenzie and Wiktionary derive it from ā- + xwar- 'eat' (Proto-Iranian *hwar-), literally 'eating-place'; the first element is the preverb ā-, not āb 'water', so the 'drinking' sense is a folk etymology.",
     "sources": [
      "https://en.wiktionary.org/wiki/آفتاب",
      "https://en.wiktionary.org/wiki/آخور",
      "https://en.wiktionary.org/wiki/آبادان",
      "https://en.wikipedia.org/wiki/Abadan,_Iran",
      "https://en.wiktionary.org/wiki/زه"
     ],
     "ref_check": [
      {
       "ref": "BQT:1,49",
       "status": "not_found",
       "note": "BQT_v1_pages.txt: the آب entries are at OCR lines ~5860-5875 ('آب ... که یکی ازجملهٔ چهار عنصر باشد') and آفتاب at line 8232 ('آفتاب ... بروزن ماهتاب'), but the Persian OCR of Mo'in's etymological footnotes on these pages is too garbled to read the Pahlavi forms; could not confirm what p.49 says."
      },
      {
       "ref": "IRN:119",
       "status": "not_checked",
       "note": "Farahvashi, Iranvij — no online copy; but Wikipedia (Abadan, Iran) reports exactly this etymology as 'B. Farahvashi proposed derivation from Persian ab (water) + pā (guard, watch), i.e. coastguard station', so the reference presumably says what the arrow says; it is a hypothesis not adopted by Iranica."
      },
      {
       "ref": "AEF:10",
       "status": "not_checked",
       "note": "Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi — no online copy."
      },
      {
       "ref": "PHD",
       "status": "contradicts",
       "note": "MacKenzie (PHD_mackenzie.txt line 658 'ab [MYA ..
----
#!/usr/bin/env python3
"""Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
"""
import sys, os, json, hashlib, re, html, time, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "data", "verification", "sources", "web")
INDEX = os.path.join(WEB, "index.jsonl")
UA = "rishe-verification/1.0 (+https://github.com/sfmqrb/rishe; etymology source archiving)"


def html_to_text(s):
    s = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h[1-6]>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n\n", s)
    return s.strip()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    note = ""
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
        args = [a for a in args if a != note]
    if not args:
        print(__doc__); return 2
    url = args[0]
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    # IRI -> URI: percent-encode non-ASCII path/query characters so urllib accepts them
    parts = urllib.parse.urlsplit(url)
    fetch_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc.encode("idna").decode(),
                                         urllib.parse.quote(parts.path, safe="/%:@!$&'()*+,;="),
                                         urllib.parse.quote(parts.query, safe="=&%:/?+"), parts.fragment))
    os.makedirs(WEB, exist_ok=True)
    path = os.path.join(WEB, h + ".txt")
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
        print(path); return 0
    status, title, text = 0, "", ""
    try:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": UA, "Accept-Language": "en"})
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
01a350f2398643fc.txt
03ddfbfafbdac423.txt
0420221ac764ad13.txt
0422a99755c9a7d1.txt
08eae3a92d63770a.txt
08f115c397a2436b.txt
08fbd766b4885f4f.txt
0933fa581bc4c83b.txt
0aa3b2561ab3e643.txt
0d1f88f9f8f7845f.txt
142
```


## [2026-09-04T15:06:57.285Z] TOOL CALL #4: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T15:06:57.303Z] TOOL RESULT

```


```


## [2026-09-04T15:07:02.340Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN leaf 22 (p.1) ==\"; awk 'BEGIN{RS=\"\\f\"} NR==23' HRN.txt | head -80; echo \"== HRN grep Glanz ==\"; grep -n -i 'Glanz' HRN.txt | head -20; echo \"== KLN abdest ==\"; grep -n -i 'ābhā\\|abhā' KLN_1966.txt | head; echo \"== POK_full ap-2 / lemma ab ==\"; grep -n 'lemma: ab\\b\\|lemma: ab-' POK_full.txt | head",
 "description": "Look up Horn p.1 and related local refs"
}
```


### [2026-09-04T15:07:04.212Z] TOOL RESULT

```
== HRN leaf 22 (p.1) ==
Ä.
1. ä. 1) Praefix, z. B. in ämeden^ ardi/is.
ap. aw. phlv. ä; ai. d,
2) Praeposition , z. B. in her ä her, gird ä gird,
aw. ai. ä,
/2^' ab, ätv *Wasser ; vergl. slm]ab (*Quecksilber, wortl.
'Silberwasser' d. i. flüssiges Silber), i^'^i^M Jer. 41, 8
(Etymologie Nüldeke's bei de Goeje, Bibliotheea geo-
— • mm
graphorum arabicorum, IV, 240), DN*:?!*! Is. 2, 9, 2^'ii^^^
Is. 36, 12, 2X^^D Jer. 31, 12 u. a. m.
ap. öp- 'Wasser ^); aw. äp-; phlv. fJp (päz. äw); ai. äp-,
kurd. äw; afy. öba (fem.); bei. ap, n. äf (12); wa;^.
ywpÄ:, ydpak, minj. ydoya; yidg. t/ow?;\
3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
äb[mendy Röd]äbe, Suhr]ab^ Mihr\äb^ Ardä VTr\af, af[täb,
phlv. üb] skr. äbha- *Glanz'-).
afy. bei. LW. ab, abrü; kurd. LW. äwrü.
*) So lautet das Thema nach Bartholomae BB. 14, 244.
*) Im Arabischen bedeutet mäun auch zugleich ^Wasser' und
*Glanz', worauf mich Herr Dr. Schwally aufmerksam macht. Etwa
in Anlehnung an das Persische? Die Zusammenstellung von np. ab
und skr. abhä- ist keineswegs sicher; von der Bedeutung ^glitzernder)
Wasserspieger könnte man sehr leicht zu 'Glanz* kommen.
U o r n , GrundrisB d. neup. Etyiuolog-io. 1
== HRN grep Glanz ==
464:3. ä& *Glanz , (Sahn. I S. 14 Vers 7), vergl. ab[rö, ah[tah,
466:phlv. üb] skr. äbha- *Glanz'-).
470:*Glanz', worauf mich Herr Dr. Schwally aufmerksam macht. Etwa
473:Wasserspieger könnte man sehr leicht zu 'Glanz* kommen.
2880:296. pertew 'Glanz*.
4978:soll auch *Blitz, Glanz' bedeuten, vergl. direßän,
5458:610. ru%8 {rexs) 'Glanz, Licht', ru/^Tden [rexsiden).
5594:'Glanz, Licht*; arm. lois Xicht' (H. No. 125).
7055:808. /<9ri* 'Glanz, Majestät*, ferre^ yurve % vergl. /eveme
9326:aw. *tmrecah- in asvaredah-, varei^afihvanf- 'glanz-
9329:235 Note 35); ai. vdrcas- 'Glanz.
10949:170. rar 'Glanz, Licht\ selten (AW.-Komm., Bund. 24, 25),
10951:aw. ray- 'Glanz, Licht'; ai. räy-,
== KLN abdest ==
== POK_full ap-2 / lemma ab ==
1541:lemma: ab-\ (water, river) : Root/ lemma: {en^^-2): ndd^-, errt'"-, /pb^-: (wet, damp; 
1551:Root / lemma: ab^- {*b2^^-) 
1583:Root / lemma: ab6(n){*h2abd-)\ " ape, *water demon ' derived from Root/ lemma: ab^- 
1609:Root / lemma: ab- 
1615:Root/ lemma: ab-: ' water, river ' derived from Root/ lemma: abofnj {* h2abd-): " ape, 
1617:*water demon ' < Root/ lemma: ab'^-(*/7i'abh-): " quick, abrupt ' < Root/ lemma: ab'^ro- 
3919:Root / lemma: ab'^i- 
3925:Root/ lemma: ab^i-: barley' derived from a truncated Root/ lemma: ereg*'(h)o-, 
3967:Root/ lemma: ab'^o-{*heb'^o-)\ "white' derived from Root/ lemma: el-1, ol-, J-\ red, brown 
5913:The Root/ lemma: apelo-: "strength' seems related to Root/ lemma: ab^ro-: "strong,
```


## [2026-09-04T15:07:12.590Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AFM grep ابهة/أبهة ==\"; grep -n 'ابهة\\|أبهة\\|الأبهة\\|الابهة\\|أبّهة' AFM.txt AFM_pages.txt | head -20; echo \"== AFM_pages leaf 15/16 head ==\"; for n in 14 15 16; do echo \"--leaf $n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' AFM_pages.txt | head -40; done; echo \"== MON ابهت ==\"; grep -n 'ابهت\\|ابّهت\\|اُبّهت\\|أبهت' MON_part1.txt | head -10",
 "description": "Grep Addi Shir and Mo'in for ubbaha/obbohat"
}
```


### [2026-09-04T15:07:14.830Z] TOOL RESULT

```
== AFM grep ابهة/أبهة ==
== AFM_pages leaf 15/16 head ==
--leaf 14--
ܠ @ ܛ اكه
الشمس ٠‏ وهرمس 0 - - الغليل )
0 ( | ܕ ) ݁ܡ ܐܬܝܐ او هما 0 2 ܣ 2 اع وهو 116122
1 يني
( ܠܬ 3( فارسي ء#ض وهو ܐܙܚ الخارصيني
اله ناردق ي مخض وهو الغزال
(الأوج) 210 :0 ܕܦ( ععنى ٠‏ 105( 5100 القاطع 0 هده 34 هندنة
١‏ الأوَاز) ضرب من الأنام : تعر يبب 56391 واصل معناه ` ويطلق على
:8 من الننهات الست ت الموجودة في 0 ولجموعها 5 شّش واه وهي هذه :
لباك وشهناز وما نه و 1497 ننه ܝ
8 العطّة والفرصة فارسئتها ܨ ومعناها الرجاء والطلى ٠‏ والظاهر
9 اللفظة 3 ܚܝ ومعئاها الطان
319 )0 ܐܐ 3 ونين ܐܝܢ اصمل اتسكلمة ;11
6 ,¿06 زهو نوع 6 ن الذئاب 8 بالفرنسة ܐ¥16]@§¢ ܝ
» (الأوكة) الغضب والشر ومن المحتمل ان تكون معربة :® وهو من
انواع البوم الكبير الوصوف بالشّامة
(الإيوان) الصئة العظيمة كلا زج ومنه ^ إبوان كسرى 32 ܐܨ ومئة
رق ايوان ٠‏ والظاهر ان اصل اتكلمة ارائى ` ܐܘܢܐ ܬܗ ܀ ن ܐܘܙ اي
2 د وأوى لمك يه ܕܘܥ سكن ٠‏ و بقر انه 0 7 ® 0
يكون اليونالى ماخوذًا من ܐܘܢܐ
+ ( ܐܐ ) ريف 00 وهما بمعنى ٠‏ وقالوا فيه ܵܩ 00 اي عاد
( ~ ܝܢ ܐ العادة واصل 0100 2050 المسيرة بين فرقة عظييسة اعجمى
ܩܨ ܘ الولّدون (شفاء الغليل ) ومنة )0 آيين :
9 < = ܨܝ - يطول وله وردة وورقة ء 9 وو كل.. ܐ‎ ١
29 ` رهو٠ البري زهره 1 ܢ 06 49 9( الكل‎
ܐܨܘ ٠قال في البرهان 7 2 1 ن بالهاء والقاف على وزن ܢ اسم الخردل‎
الذي يقال 4 بالعر مة جرجيرا. وهو 0 : ܝ 33 30 اضفر وورقة‎ 01
--leaf 15--
اصغر من ورق الفجل وهو حاذ الى الغابة ويستى ` 9 والقسم الاخر عدي
.| ܢ ورقه ܐ لبن قليل الحدة وزهره احمر٠‏ ٠اذا‏ سقيت سحرة ان ܐܝܒܨ عاء 25
.79 ܐܟܝ ܬ ܦܐ ܐ كثيرا »
ار 1 وان عا
باب الب
( 715 ) الفلا ل فارسي 0 ܐ له ܢܡܒ
س سر
ܟ <
( الما .© والمابوش ) معرب ابوج واصل ܐ 3 مغطي الرجل ܕ( نا نوس
بالتركية والكرد %
£ الم ونم ) تعر يب بابونه او يابونلك وهي حشيشة ذات زهر كتير النفع‎ ١
التحليل . ومنها السر ܨ ܒܒܘܝܐ‎
( المج .1 1 ܨ ܕ( | ܐܰܝ
( لبأ ) = لا اتاد 0
00 ب كيرة ة النفع في الأمرا ض السوذاوءة ܨܦ الأترجية
والتر ان رهي ܨ 09 11 ظات وهو ضرب من 1 ومن بوله 5 ܪ
2 اوغل 51
( 5 4 0 ܝ( تنفع من لدغ العقرب ܣ
09 فارساتها 0 البرهان 3130
2 من لدغ العقرب يقال له بالعر 032 ومفرح القلب > 0 بيك
ܡܠ 100 » وقمل انه اسم رنحان جبلي ورقه - ورق الريحان ورائحته
تضارع رانحة الاترجج »
( الباوزكر والبأزهر) حجر ينسّب اليه قوى غريبة في مقاومة السموم وهر
ܐ
ب لاف
--leaf 16--
ܒܝ ܝ( ك6
1 و الاتكليزي 6--020310|[
)ܕ نان والناذحان » قال 3 حيط المحيط: « الباذضيجان معرب باذتكان
بالفارسية ومعناه بيض اللان: نبات يعرف عند العامة بالمتتجان والبيدنحان ».قا-'
ان باد بالفارسيّة اسم جن كان موكلا على امر التزو يج . ونك (تجعة تكان )اهو
:2 6 معنى 5 ` 3 5 والصحيح ان 1 )
ܝ ܒܪܓܝܬܐ ب لسر ܨܬ وى ارم ܨ 8 ' ÷ ܐܚܐ 20 ابن
6 0 ܚ «واسمة الفرنني يقرب أكثر من ܝ الاصلي
شقال آل 1116 31161 ويقول الاسا” ماندون 86161286123 وهو باطلحان 6ܗܨ29 وباحأن
013
ܣ ,)ܪܕܕ والباداورد ܙ !)ܪܕܕ ) ܝܐܝ مثآث الساق مستدير الأعلى
09 3 4 زهر احمر لا 7 اوراقة على 7 باد 1 35( غنه لي
الببهان القاطع انه نوع من الشوك له زهر احمر وأبيض ܐܕܨ 301 له بالتركة
2 حافر ܓ :¢ وبوغه يك وقارنه باعر وسّيطان اريفسى ܨ 5 ܥ( ® 1 2
المماركة والشوكة البيضاء ܢ هذا الات بالا دورد لأن الريح تلعس به وهو
730 أي ريم وآور اي يذهب ب
( المأرّة) تعريب بره ومعناها القطعة - بأره 06 ܦ ± ܒܒ
5 الدارجة
095 20 9 ` ©
1( - ` ܥ وهو في اصله الفارسي
اسباب التجمّل 3 3 5 5 على الفرامين والرخصة
بالدخول على الماوك وهو مركب من بار اي حمل ورخصة ومن نامه اي رسالة
0 ( البأدنج ) عق بأدنج وهو الحوز المددي.
# ܐ ضرت من الصقور وهو :اسشد > ارح شكيرا وأضتها خلا
ܨ ܬܨ 80 ܠ للصند .27 باز ܫ طوغان
(البازّار) فارسي مخض وهو السوق ومنة الكردي بأحار
( المأزركان) ܨ ¢ ܐܨ 0207 السرق
== MON ابهت ==
6560:ابسهت: ۳۹ ال ابهت) [ع.] 
19777:منشی. نسیم. شکوه؛ ابهت» اهمست. تندی» 
25667:به مشابهت. ضح.- لازم الااضافه است. 
26989:بی‌ریب.: (ابهتطارودآا اف. ۳۵ (ص مر.) 
77878:حمله» هجوم. قهر» غلبه. ابهت» وقار. 
83494:گیاهی است از تیرةٌ پنیرکیان و مشابهتش با 
84131:شبه: "3202 [ع.] (امص.) مشابهت؛ مانندی. 
84157:پوشیدگی امری. مشابهت. (.) شکث» تردید. 
86306:دو روی آن با یکدیگر مشابهت ندارد. بخية
```


## [2026-09-04T15:07:23.523Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'ابه\\|أبه\\|آبه\\|أبه' AFM_pages.txt | head -20; echo ==; grep -n 'بها' AFM_pages.txt | head -20; echo \"== leaf list start of alif ==\"; for n in 8 9 10 11; do echo \"--leaf $n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' AFM_pages.txt | head -30; done; echo \"== MON 6555-6565 ==\"; sed -n '6555,6566p' MON_part1.txt",
 "description": "Locate ubbaha in Addi Shir and Mo'in entry context"
}
```


### [2026-09-04T15:07:25.199Z] TOOL RESULT

```
Exit code 1
150:( الوبريز والاإبريزي » من 4 الخمالص قال عنة فرتكل في كتابه في
787:( 6 ) 07 ܣ 3 2 بوزيدان وتركتة تلكى خابهسى
1525:(الدانة) ܐ ل دهي دابه بالفارسة
2251:ܥܬ قا ل ܚܨܢ به لذهابه على وجه ܚ 1
2810:`( الذي يروج .امرأة زابه 650 أرمات عله لله 01د 02
2837:(الطارق ) 3 بظرفٍ يطبخٍ به معرب تابه وهي 1 $
3447:( المُمْتِيج ) خبط غليظ ± الذمي فوق ثيابه دون الزّار معرب عن كدت .
3774:ܨܐܘ واضبطرابه عند السباق٠وقيل‏ هو من الوَدْن لان الل رون فيه «بحبط
4363:تابه ܙ |
4934:سه بد ابه
5115:كابه وم
5631:ܪܐ( خابهسى ܀ܘܙܐ
(eval):1: = not found
```


## [2026-09-04T15:07:28.821Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n 'بها' AFM_pages.txt | head -20; echo \"== leaf list start of alif ==\"; for n in 8 9 10 11; do echo \"--leaf $n--\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' AFM_pages.txt | head -30; done; echo \"== MON 6555-6565 ==\"; sed -n '6555,6566p' MON_part1.txt",
 "description": "Locate ubbaha in Addi Shir and Mo'in entry context"
}
```


### [2026-09-04T15:07:30.377Z] TOOL RESULT

```
380:الببهان القاطع انه نوع من الشوك له زهر احمر وأبيض ܐܕܨ 301 له بالتركة
457:* 3 الإبريج ) 45 بها 5 السّمن منها < ابيز
609:» (البتم ) التّخمة والسّامة قيل اليثم لبها خاصة دقيل هو مخصوص بالدسم
684:الببهان القاطع 116 بذم | الناء دواء يقال له فى .شيراز * بل شيدين 110 1
732:5 البطل والمهاوان * من بها اي من ومن دار اي ذو
734:* «البهار) العرار ويقال له عين البقر وهار !ܐܡ وهو يندت ايام الر بع وردهل الوزق 19 .27 79 ٠واصل‏ معنى بهار بالفارسمة موسم الربيع وأطلق
1091:“د (الجَلّخ ) 7930 بها السكين ܕܧܕܩܐ تعريب 5 آلة 123 ݂ܟ
1140:لبعض بنوع خني ٠‏ وتقول بالعريّة : سمعت من جانبها تجنشا
1298:قال ف الببهان القاطع :« ܥܰܚܰܐܚܺ محجن مثاّث ܒܝ شوكة من حديد 0
1333:( ارربيل ) الممقاء او العجوز المتهدمة مركّة من ثر وهي اداة بها يوصف
1354:بها بوصف الى ء ء بالغخلاظة ومن سم اي حافر
1357:' .قات والأرجم 9 اللفظة ® وهي بها خرطال ايضاً 007 ܟܢܫ
1565:(الدر بين والدّرَابرُون ) قواغ مصفوفة تمل من خشب او حديد تحاط بها
1593:* ¦ 34 والدرونج ) قطع من اصول 39 ذات عقر صغيرة يتداوى بها
1610:الغاب في الشطرنج ٠‏ فارسيّتها دست أخذتمهسا العرب وتصرفت بها ١‏ وقد اجتمع أكثر
2121:دالا ارس جود اسم 13 أتتداوى بها ٠‏ واشت لغة فيه
2134:+ (التسخة) 09 ?3 ِ )= :0 سبيخ وهو ܬܟ ٠‏ ٠وقالوا‏ فبها:
2409:جادها 5 ومن وبرها ثاب يلبسونبها في الايام المارة فلا يوثر يم 9705 1
2576:يلبيب ومن هناك تناولة الفرس ( حيط المحيط ) ‹ قال في الإبهان القاطع : « ܚܡ ܙܝ
2592:» ((6 ܘ ) لعبة بها يكسع الواحد ܐ من خافه فيصرعة تعريب سينك
== leaf list start of alif ==
--leaf 8--
حت آي ܝ
3 وهو ذو لسان 003 فبه ܨ )1 . ܣ(¿ فارسي مسرن >1 ٠وقال‏ ܝ
سفاء ܣ 6 تكون في السرج وغيذه ج أباذيم ويقال أبزين. .
وهو من ¥ بمنى ܢ عض فليس معرب لك :إبزيم ܐ £ حديدة في طرف اللزام
< :ܐ ويقال له ܐܢܐ زرفن وزرفين فين»٠قات‏ ان صعة هذا 3 ܚܨ على كإنه
0( معراقك اما عن 05 وهو المعماز او عن الفارسي ابزن وعر 1
من حديد اومن ܡ مصاوع ء! < ܝܝ على قدرقامة الانساناو 26
منها عليه غطاء ع مثقوب يضع شه الاطاء المريضُ و2 ,ܕܝ ن راسة من !ܝܢ 273
بصب 3 1:39 ܨ بالأدوية ܐ ` ابزن بالفارسة على
ܐܬܕܩ الصغير ايضا ومنهُ عرب (|% بزن ) وهو حوض يتس فيه ويعرف بالمغطس
وقد سحل من ܝ واهل ܦ يقولون بازاناً الحوض الذي 5 العين عند
الصفاء ٠‏ لانة شبه حوض ١‏ شنفاء » الغليل )
+ ( )¥ ]5 ) الطاعة ‏ تتول جات |( من الناس ْ 07 5371
الأخلاط والرعاع 0 البوش ) الماعة المختالطة 199 ܗ )0 0
اختلطوا فضِجُوا و( 6 القوم ¬ ٠‏ كل ذلك ماخوذ من أبأش ` ® دهي
جماغة مره "كل يشكال الناس ٠.‏ وقالوا فيها 06 01 ,01 ) النثتيء اي جمعة
9)
*< ܐ( مق السحاب تعريب ابْر ويرادفة الأرمني ودس 6: بأوت
والكردي 5 0 راو تور والروسي 064310
+ لي العظمة والبهجة معرب أب بآ 16031
ܕ | ܟ بالارامية ܦܐܢܐ ܦܐܐ ° ® بهي وبالفرنسية 18811
ܨ (( 56( الحارض الضعيف من القوم و عو لجل 955
ܐܝܟ المعاول والظاهر ان الفاسي ماخوذ من اليونالي :ܘܡܐ
( إلا جور اليا عور والا جور والا جر 0 وال جرون) قري ١‏ "لوز دعو
تراب يحكم عجلة وتقريصة 2 2 5 'وقالوا فيه أ جر الطين ٠‏ وييرادفة بالارمشة
سدمارس وقال )ܡܢܐ (ص 09110 اصل اللفظة ارا ى ܐܓܪܐ وهو موحود :
اللغة 32 القدعة ٠واما‏ العُرميد فهو @ 7
--leaf 9--
لكر له
| 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢
والايطا ليائي - 0 3430 بالسر ± الدارجة 36
والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153
( إلا درون ) المثلفٍ والارى والوطن وهر إما معرب 50 80350 ,<
ماخوذ عن اليونائي ا ثاريه وهر القسم من ܝܗ الختص باارجال ܢ܆ܐ ܐܢܝܕܪܘܢܐ
11:20 ® ܕ[ 0 والقليد فاخوذان عن بسجده»: وعن 0 اي المخدع
وسبه مخدع
( الاذرريون ). زهر اضفر في 71005 5957 الذذ كو راصل 11 ]ا
شمه الثار. وآذر يون اغة فيه ± ` 096( حيجكى ( زهر القمر )
وقره كز ( العين السوداء )
3( الأرجان ) ,شر 4033( :3( 600390550901017 ا
ارجن وهو الفستق البري وقيل الاوز المر واسمة 6 9 اي لوز الل
( الترهان القاطع )
590 معرب )6.35 وهو سّحر له ورد 0 به 0
ويطلق 9 على 0 حمر والشاب الخمر والصبغ الأخر ٠وقيل‏ 0 عوده اذا احصارق
تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1
اللفظة سنسكر ܝܬ 10 ܐܦܬ نه من 5282 اي احمر ومن 724 وهى اداة
النسة ( القاموس العبرالي الكلداني تأليف جسنيوسء ضن : + ) (4) :
الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1
مسدنّا من حسابات الديوان
+ ( الأرش ) ما 'يدفع بين السلامة والعيب في السلعة معرب رز وهو القيمة
5" (الأرْضي 039 ننات معروف ٠‏ .نا الصيغة غر يبة ٠‏ فلوو كان الاسم عربيا
لقمل الشوك الأرضي فهو عا 17 م 4 الفرني 56 ܐ( ܢܘܟ به
-210231طن) ]@ 1:31111123آط ع1 1231111216 1.2101 :115 1 موه ©
11121... 1125122 1847.
--leaf 10--
اليو نبا ܒ
(الأرغس) ' ور اشر أصل سح < ܨ 2 أرغش وفسره 5
القاطع 1ل شعرة اللا رياس (المسماة في الترمّة قادين طأوزلنى ) يدخل في
0 02 العيون ٠‏ 9 ܐܐܬ 0 اتلد 0 ® !¢ § (631032)
0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي
ܠ ومن 01
0 191 نت 00 0 كر ٠‏ والسريالي ماخوذ من الفارسي
2 وهو بعناه ويطاق ايضاً على سقف المت 8 قرن .0 به اليونالي 00
اي البيت والانكليزي 11146 ܐܨ 2
( الأزادرغت) تعر يبب 033 اي ور 50 “قال في البرهان القاط لع هي 3
مادة أزاد:< آزاد شجر يقال له 37 بكاين »> 3 بازادرغت » 380
أزاددرخت ما ܣܨ ܝ : *آزاددرخت * سجر يقال له في بلاد جرجان « زهر زمين > ( سم"
الأرض) ܢܢ فارس _يستى « طاق وطءك » 5 له ` ® ܐܢ̈ܕܐ وشجرة 3
ܝܬ للك واختلف كثيرًا في ماهيّة هذا الشجر. وقد قن اراي اكه مر ون
سجر الشييخ عاص لاد الفرس ورقة ܠܝܬ ورق الدذا لى مسموم قاتل اللموانات.
فقيل ان شجر «طاق » هو .الشجر المسى 96 «سكبيك اغاجى © ويعد شير ]
للنار وناره ܗܣ ويقال له ` ® غضا » ٠‏ وكتاب الفرائد 2 الطموع في
بيردت ܝ بالافرنسية ° 11125
2 307 تعر يب راس وهما < ٠‏ ومئة 0
ܐܙܒܐ
( لأسا بذة) ܝ ܨܝ 5 وهو ܣ > 3 حصان ومن ناد
أي حارس ٠‏ و باد تطلق ايضا على اعيان الملد وعمد نه
( الاوسينداج والاوسفيداج ) بياض.الرضاص 3 تعريب سيد نلك وممناء”
الانك الابيض ٠‏ ومنه 4 الارسي 6« | دي سياف
* :ܠܘ الذي يلف عليه الغزل ܐܟ 24008
اصن
--leaf 11--
ܗܕ ¢ ܙܝ
(الأستاذ) ܐܬܢ )ܪ الصناعة ورنسها ܠܚ 31 ܣܣ 4 سا <
والكركثة
( )ܠ ܚܡܕ الديياج الغليظ وقيل ديباج يعمّل بالذهب او ثاب + ܨ صفاق
ܨܝ عن استَبْر واصل ܢܓ الغليظ ^ الارامي ات دم
سر الأصاص او الرصاص 3:31 الردي نعر بب 8 ويرادفهة
ܝ 5 01 و0 : اي النحاس فاخوذ 9 ܥܨ 501 (فرتكلٌ
ضص: : ܐܘ ܙ ) والأبار من الاراءى ` ܐܒܪܐ
ܟ ܐ ©) 20 !ܥ ܀ ܨܣ 90 سر نبج وهو صبغ
ادر مصنوع من حريق الا نك والقلى وهو مركب من سسرخ 3 ® ومن 9¬=
0 نات تعلفة الدوات ܨܝ 1 ٠والفقصفصة‏ لغة ܦ ٠‏ .وقد
استعارتة السر ܬ ايضاً وهر فيها ܐܣܦܣܬܐ
* ( 9 والسقّند) الخردل الابيض وقيل 95 الابيض ٠والاول‏ ܟܝ
7 ܙ 5 الشطر ”` 9 الخردل وسفيك
الايض
ܐ `
الرصاص والانك تعريب اسفيداب واصل معناه الماء الابيض ومنة السسربالي
ܐܣܦ ܕܒܩܥܐ ش
( الأسكرجة والسم جة » إناء صغير مساه امقرنك اللزا :10
الغايل) .قا ܝܝ وفارسيتة 1 ١‏
0 ١الأسرّة)‏ القدوة «اخوذة 0 اسأً ومعئاها القاعدة والقانون وهي من ܪܕܐ
النشسه ايضاً . وقالت فيها 393 به اي اقتدى ٠‏ واما الآمي بعنى الطبيب فهو
و 5.5 1ل يك »هيع (فرنكل ض : \ \ ¥)
( |( > 9 نندت طويل الشوك ترعاه الإرئل ® من اند اي جسل ومن
غاز اي شوك
د 3 © < جدًا . يجتمل ان يكون ماخودًا 0"
المشرو بة لبلا
== MON 6555-6565 ==
تاریکی. (ا) انگشت ستبر و کو تاه دست يا با 
از جانب انسی» انگشت نر انگشت بزرگد» 
شست؛ چ. باهم اباهیم (غم.) ابهام پا: 
کت سس 

ابسهت: ۳۹ ال ابهت) [ع.] 
(اسص.) بزرگی» بزرگواری» شکوه 
عظمت. بهجت. شادمانی» تکس نخوت. 
ابهر : 9 [ع.] (۱.) (جان.) رگی‌است در 
بشت» رگ بشت که به دل بیوسته است؛ 
رگ جان» آورتی, ام‌الشرائین.
```


## [2026-09-04T15:07:54.355Z] TOOL CALL #9: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آب",
 "prompt": "Give the full Persian section: all etymology sections (Etymology 1, 2 ...), the senses listed (especially any 'lustre, glitter, splendour, honour' sense), the Middle Persian / Old Persian / Proto-Iranian forms cited, and any references (Cheung, Hasandust, Horn, MacKenzie, Nourai). Quote verbatim where possible."
}
```


### [2026-09-04T15:08:02.169Z] TOOL RESULT

```
# Persian Section from Wiktionary: آب

## Etymology 1

**Source forms:**
- Middle Persian: ʾp̄ (āb)
- Old Persian: 𐎠𐎱𐎡𐎹𐎠 (ap-)
- Proto-Iranian: *Hā́fš
- Proto-Indo-Iranian: *Hā́ps
- Proto-Indo-European: *h₂ep- ("water, body of water")

## Etymology 2

Borrowed from Arabic آب (ʔāb), from Classical Syriac ܐܒ (ʾāḇ).

## Senses (Etymology 1)

1. "water"
2. "liquid"
3. "juice" (synonym: آب میوه)
4. "river" (synonym: رود)
5. "honour, reputation, standing"

## References Cited

The page lists: Rastorgujeva, V. S. and Edelʹman, D. I. (2000), *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages], volume 1, Moscow: Vostochnaya Literatura, page 312

**Note:** The specific scholars you mentioned (Cheung, Hasandust, Horn, MacKenzie, Nourai) do not appear in the provided text's reference section for the Persian entry.
```


## [2026-09-04T15:08:06.611Z] TOOL CALL #10: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آبرو",
 "prompt": "Give the Persian entry verbatim: etymology (components, literal meaning, any Middle Persian or older forms, references), senses, and any notes on the 'water of the face' idiom. Also list any descendants (Urdu, Turkish, Hindi)."
}
```


### [2026-09-04T15:08:13.204Z] TOOL RESULT

```
# Persian Entry: آبرو

## Etymology
The term is "a shortened form of آبروی (âb-e-ruy), compound of آب (âb) +‎ روی (ruy)." The literal meaning translates to "water of the face." It shares cognates with Northern Kurdish *avrû* and Central Kurdish *ئاوڕوو* (awrrû).

## Senses
The noun has four meanings:
1. Face
2. Honour
3. Reputation
4. Standing

## Descendants
Notable descendants include:

**South Asian languages:**
- Urdu: آبرو (ābrū)
- Hindi: आबरू (ābrū)
- Bengali: আব্রু (abru)
- Punjabi: ਆਬਰੂ (ābarū)

**Turkic languages:**
- Ottoman Turkish: آبرو / آبروی (âb-ı rû(y))
- Turkmen: abraý
- Uyghur: ئابروي (abroy)
- Azerbaijani: abır

**Other:**
- Armenian: աբուռ (abuṙ) (via Kurdish)
```


## [2026-09-04T15:08:16.955Z] TOOL CALL #11: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/آفتاب",
 "prompt": "Give the Persian entry verbatim: etymology (Middle Persian form, Proto-Iranian reconstruction, components, any discussion of āb 'water/glitter' vs abi- preverb, references such as Cheung, Hasandust, MacKenzie, Nourai), senses and descendants."
}
```


## [2026-09-04T15:08:19.243Z] TOOL CALL #12: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/أبهة",
 "prompt": "Give the Arabic entry verbatim: root, etymology (any mention of Persian origin, Addi Shir, or the root ʾ-b-h / b-h-w), vocalization (ʔubbaha), senses, derived terms (تأبه), and descendants (Persian ابهت, Ottoman Turkish, Urdu). If the page doesn't exist say so."
}
```


## [2026-09-04T15:08:21.492Z] TOOL CALL #13: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/ابهت",
 "prompt": "Give the Persian entry verbatim: etymology (borrowed from Arabic? which form, with vocalization), pronunciation (obbohat / ubbahat), senses. Also any Urdu or other sections. If the page doesn't exist say so."
}
```


## [2026-09-04T15:08:22.933Z] TOOL CALL #14: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/आभा",
 "prompt": "Give the Sanskrit entry verbatim: etymology (root भा bhā- 'to shine' with prefix ā-, PIE *bʰeh₂-), senses (splendour, light, lustre), and any cognates or descendants."
}
```


### [2026-09-04T15:08:24.056Z] TOOL RESULT

```
# Arabic Entry: أبهة

**Root:** ء ب ه (ʔ b h)

**Vocalization:** أُبَّهَة (ʔubbaha)

**Part of Speech:** Feminine noun

**Definition:** The entry defines this term as meaning "greatness, majesty, grandeur"

**Grammatical Information:** The page indicates this is "a singular triptote in -a" and provides a complete declension table showing nominative, accusative, and genitive forms in indefinite, definite, and construct states.

**Notable Limitation:** The Wiktionary page does not include sections on etymology, Persian origin, derived terms (such as تأبه), or descendants in Persian, Ottoman Turkish, or Urdu. The entry focuses solely on the Arabic noun's definition, pronunciation, and grammatical declension.
```


## [2026-09-04T15:08:24.588Z] TOOL CALL #15: WebSearch

```json
{
 "query": "أبهة اشتقاق أصل الكلمة \"أُبَّهة\" لسان العرب \"الأُبَّهَة\" العظمة والكبرياء معرب"
}
```


### [2026-09-04T15:08:24.977Z] TOOL RESULT

```
# Persian Entry for آفتاب

## Etymology

The word derives from Middle Persian *𐭠𐭯𐭲𐭠𐭡* (ʾptʾb, "sunshine"), with a comparative form *𐮀𐮎𐮃𐮀𐮁* (ʾpdʾb). Its ultimate origin traces to Proto-Iranian *\*abi-tāpáh*. The term is analyzable as a compound: *[آف](/w/index.php?title=%D8%A2%D9%81&action=edit&redlink=1 "آف (page does not exist)")* (âf) plus *[تاب](/wiki/%D8%AA%D8%A7%D8%A8#Persian "تاب")* (tâb).

## Senses

1. **Sunlight, sunshine**: The primary meaning, with a coordinate term being *[مهتاب](/wiki/%D9%85%D9%87%D8%AA%D8%A7%D8%A8#Persian "مهتاب")* (mahtâb, "moonlight").

2. **Sun**: An alternative sense, synonymous with *[خورشید](/wiki/%D8%AE%D9%88%D8%B1%D8%B4%DB%8C%D8%AF#Persian "خورشید")* (xoršid), with *[ماه](/wiki/%D9%85%D8%A7%D9%87#Persian "ماه")* (mâh, "moon") as a coordinate term.

## Descendants

The word generated numerous descendant terms across multiple languages, including Azerbaijani, Bengali, Chagatai (with Uyghur and Uzbek offshoots), Gujarati, Classical Malay varieties, Hindustani languages, Ottoman Turkish, Punjabi, Turkmen, and Yaghnobi.

## References

Cheung, Johnny's etymological work provides the Proto-Iranian reconstruction cited in the entry.
```


### [2026-09-04T15:08:26.976Z] TOOL RESULT

```
# Persian Entry: ابهت

**Etymology:** Borrowed from Arabic _أُبَّهَة_ (ʔubbaha)

**Pronunciation:** Multiple regional variants including:
- Classical: /ʔub.ba.ˈhat/ or /ʔub.bu.ˈhat/
- Iranian formal: [ʔo.boɦ.hǽt̪ʰ]
- Dari formal: [ʔʊ.bo̞ɦ.hát̪]

**Sense:** The word denotes "magnificence, grandeur, imposing presence." The entry includes an example sentence showing usage in describing a person's dignified appearance.

**Other sections:** No Urdu section appears on this page. The entry notes alternate Tajik spelling (**уббаҳат**) and provides reference materials from Persian dictionaries.
```


### [2026-09-04T15:08:31.681Z] TOOL RESULT

```
# Sanskrit Entry: आभा (ābhā)

**Etymology:** The Sanskrit term combines the prefix आ- (ā-) with the root भा (bhā, "to shine"), forming a compound meaning "appearance" or "radiance."

**Senses:**
1. Appearance
2. Splendour, glamour

**Grammatical Notes:** Feminine ā-stem noun with complete declension across singular, dual, and plural forms in all cases (nominative, accusative, instrumental, dative, ablative, genitive, locative, vocative).

**Cognates/Related Forms:** The root भा (bhā) meaning "to shine" is the generative element. Hindi borrowed this Sanskrit term as आभा (ābhā), maintaining the same meaning of "lustre, brilliance, shine."
```


### [2026-09-04T15:08:42.287Z] TOOL RESULT

```
Web search results for query: "أبهة اشتقاق أصل الكلمة "أُبَّهة" لسان العرب "الأُبَّهَة" العظمة والكبرياء معرب"

Links: [{"title":"الكبرياء In English - Translation and Meaning in English Arabic Dictionary of All terms Page 1","url":"https://www.almaany.com/en/dict/ar-en/%D8%A7%D9%84%D9%83%D8%A8%D8%B1%D9%8A%D8%A7%D8%A1/"},{"title":"المعاني - الآيات والسور التى وردت فيها كلمة الكبرياء ومشتقاتها في القرآن الكريم.","url":"https://www.almaany.com/quran-b/%D8%A7%D9%84%D9%83%D8%A8%D8%B1%D9%8A%D8%A7%D8%A1/"},{"title":"تعريف و شرح و معنى الكبرياء بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D8%A7%D9%84%D9%83%D8%A8%D8%B1%D9%8A%D8%A7%D8%A1/"},{"title":"تعريف و شرح و معنى كبرياء بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D9%83%D8%A8%D8%B1%D9%8A%D8%A7%D8%A1/"},{"title":"معنى عظمة بالعربي — التعريف والشرح والمرادفات في معاجم اللغة العربية | قاموس عرب ديكت","url":"https://www.arabdict.com/en/%D8%B9%D8%B1%D8%A8%D9%8A-%D8%B9%D8%B1%D8%A8%D9%8A/%D8%B9%D8%B8%D9%85%D8%A9"},{"title":"الكبرياء ردائي والعظمة إزاري","url":"https://www.islamweb.net/ar/article/40088/%D8%A7%D9%84%D9%83%D8%A8%D8%B1%D9%8A%D8%A7%D8%A1-%D8%B1%D8%AF%D8%A7%D8%A6%D9%8A-%D9%88%D8%A7%D9%84%D8%B9%D8%B8%D9%85%D8%A9-%D8%A5%D8%B2%D8%A7%D8%B1%D9%8A"}]

Now let me search more specifically for the word "أُبَّهة" (ubbah):

Links: [{"title":"معنى أُبَّهَة, فخامة وعظَمة - معجم الرياض","url":"https://dictionary.ksaa.gov.sa/result/%D8%A3%D9%8F%D8%A8%D9%91%D9%8E%D9%87%D9%8E%D8%A9"},{"title":"لسان العرب : بجد- - ويكي مصدر","url":"https://ar.wikisource.org/wiki/%D9%84%D8%B3%D8%A7%D9%86_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8_:_%D8%A8%D8%AC%D8%AF-"},{"title":"تعريف و شرح و معنى أبهة بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D8%A3%D8%A8%D9%87%D8%A9/"},{"title":"معنى أبهت بالعربي — التعريف والشرح والمرادفات في معاجم اللغة العربية | قاموس عرب ديكت","url":"https://www.arabdict.com/en/%D8%B9%D8%B1%D8%A8%D9%8A-%D8%B9%D8%B1%D8%A8%D9%8A/%D8%A3%D8%A8%D9%87%D8%AA"},{"title":"إسلام ويب - لسان العرب - حرف الألف - أبه- الجزء رقم1","url":"https://www.islamweb.net/ar/library/content/122/22/%D8%A3%D8%A8%D9%87"},{"title":"معنى الأبهة بالعربي — التعريف والشرح والمرادفات في معاجم ...","url":"https://www.arabdict.com/en/%D8%B9%D8%B1%D8%A8%D9%8A-%D8%B9%D8%B1%D8%A8%D9%8A/%D8%A7%D9%84%D8%A3%D8%A8%D9%87%D8%A9"},{"title":"معنى الابيه في معجم عربي عربي - معاجم","url":"https://maajim.com/dictionary/%D8%A7%D9%84%D8%A7%D8%A8%D9%8A%D9%87"},{"title":"قاموس معاجم: معنى و شرح الابهة في معجم عربي عربي أو قاموس عربي عربي وأفضل قواميس اللغة العربية","url":"https://www.maajim.com/dictionary/%D8%A7%D9%84%D8%A7%D8%A8%D9%87%D8%A9"},{"title":"ما معنى أُبَّهَةٌ في معجم اللغة العربية القاموس - البيت العربي - البيت العربي","url":"https://www.arabehome.com/mojam/q/%D9%85%D8%A7-%D9%85%D8%B9%D9%86%D9%89-%D8%A3%D8%A8%D9%87%D8%A9-%D9%81%D9%8A-%D9%85%D8%B9%D8%AC%D9%85-%D8%A7%D9%84%D9%84%D8%BA%D8%A9-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-%D8%A7%D9%84%D9%82%D8%A7%D9%85%D9%88%D8%B3"},{"title":"معنى و ترجمة كلمة أبهة في القاموس, تعريف وشرح بالعربي","url":"https://www.alburaq.net/meaning/%D8%A3%D8%A8%D9%87%D8%A9"}]

Now let me search for information about whether أُبَّهة is borrowed/معرب:

Links: [{"title":"لفظ معرب - ويكيبيديا","url":"https://ar.wikipedia.org/wiki/%D9%84%D9%81%D8%B8_%D9%85%D8%B9%D8%B1%D8%A8"},{"title":"معربات فارسية - ويكيبيديا","url":"https://ar.wikipedia.org/wiki/%D9%85%D8%B9%D8%B1%D8%A8%D8%A7%D8%AA_%D9%81%D8%A7%D8%B1%D8%B3%D9%8A%D8%A9"},{"title":"كلمة (لغة) عربية أم معربة؟","url":"https://www.alukah.net/literature_language/0/111261/%D9%83%D9%84%D9%85%D8%A9-%D9%84%D8%BA%D8%A9-%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-%D8%A3%D9%85-%D9%85%D8%B9%D8%B1%D8%A8%D8%A9%D8%9F/"},{"title":"الألفاظ المعربة في كتاب (ديوان الأدب) للفارابي - ديوان العرب","url":"https://www.diwanalarab.com/%D8%A7%D9%84%D8%A3%D9%84%D9%81%D8%A7%D8%B8-%D8%A7%D9%84%D9%85%D8%B9%D8%B1%D8%A8%D8%A9-%D9%81%D9%8A.html"},{"title":"تعريف و شرح و معنى معرب بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D9%85%D8%B9%D8%B1%D8%A8/"},{"title":"تعريف و شرح و معنى أبهة بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D8%A3%D8%A8%D9%87%D8%A9/"},{"title":"تعريف و شرح و معنى عرب بالعربي في معاجم اللغة العربية معجم المعاني الجامع، المعجم الوسيط ،اللغة العربية المعاصر ،الرائد ،لسان العرب ،القاموس المحيط - معجم عربي عربي صفحة 1","url":"https://www.almaany.com/ar/dict/ar-ar/%D8%B9%D8%B1%D8%A8/"},{"title":"عرب (اشتقاق) - ويكيبيديا","url":"https://ar.wikipedia.org/wiki/%D8%B9%D8%B1%D8%A8_(%D8%A7%D8%B4%D8%AA%D9%82%D8%A7%D9%82)"},{"title":"تحقيق كلمة \"العرب\" – معناها ومشتقاتها ومصداقها","url":"https://muhammadencyclopedia.com/article/tahqiq-kalimat-al-arab"}]

Based on the search results, I have found comprehensive information about the word "أُبَّهة" (ubbah/abbah). Let me provide you with the information:

## معنى كلمة أُبَّهة

أُبَّهَة تعني: العَظَمَةُ، والبَهْجَةُ، والكِبْرُ، والنَّخْوَةُ. وبشكل أدق، الأُبَّهة هي العظَمَةُ والرُّواء.

الكلمة تدل على عظمة وكِبْر، فخامة، زهو وغِنًى، رواء ومنظر حسن.

## من لسان العرب

في المعاجس العربية المرجعية، يتكرر تعريف الكلمة بنفس المعاني المذكورة أعلاه، حيث يرجع معناها إلى العظمة والكبرياء والهيبة والبهجة.

## بخصوص كونها معرب أم عربية الأصل

للأسف، نتائج البحث لم تقدم معلومات مباشرة وواضحة حول ما إذا كانت كلمة "أُبَّهة" معربة من لغة أخرى أو عربية الأصل، أو حول تفاصيل اشتقاقها اللغوي الدقيقة. المعاجم المتاحة اكتفت بتقديم المعنى دون تحديد صريح لأصل الكلمة.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T15:08:53.004Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://www.islamweb.net/ar/library/content/122/22/أبه",
 "prompt": "Quote verbatim the Lisan al-Arab entry for the root أبه: the verb أَبَهَ / أَبِهَ and its meanings, الأُبَّهَة (meanings: العظمة, الكبر, البهجة, النخوة), تأبّه, and any statement about the word's origin or any poetic shawahid. Give the Arabic text."
}
```


## [2026-09-04T15:08:56.012Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://www.almaany.com/ar/dict/ar-ar/أبهة/",
 "prompt": "Quote verbatim the definitions given for أُبَّهَة in the dictionaries listed (المعجم الوسيط, الرائد, لسان العرب, القاموس المحيط, اللغة العربية المعاصر), including the verb forms أبَهَ / تأبَّهَ and their meanings, and any note on origin."
}
```


## [2026-09-04T15:08:57.549Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://ar.wikipedia.org/wiki/معربات_فارسية",
 "prompt": "Does the list include أبهة / الأبهة / أُبّهة? If so quote the line with its stated Persian origin. Also quote any lines for آب-derived words (e.g. أبريق, انبيق)."
}
```


### [2026-09-04T15:08:58.283Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T15:09:00.274Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=ابهت&d=moein",
 "prompt": "Quote verbatim the Mo'in (فرهنگ معین) entry for ابهت, including the origin tag ([ع.] etc.) and the definitions. Also quote the Dehkhoda entry if shown."
}
```


## [2026-09-04T15:09:00.728Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/ابهت/",
 "prompt": "Quote verbatim the sections for فرهنگ معین and لغت‌نامه دهخدا for ابهت, including origin tags and any statement about the Arabic form أبهة."
}
```


### [2026-09-04T15:09:01.620Z] TOOL RESULT

```
# Lisan al-Arab Entry for أبه

## Verbal Forms and Meanings

**أَبَهَ / أَبِهَ لَهُ يَأْبَهُ أَبْهًا**: "to notice, pay attention" (فطن)

Some lexicographers noted: "أَبِهَ لِلشَّيْءِ أَبَهًا" means to forget something, then become aware of it again.

**أَبَّهَ الرَّجُلَ**: "to make someone aware" (فطّنه)

**أَبَّهَهُ**: "to alert/wake him" (نبّهه)

## الأُبَّهَة (Magnificence)

The noun الأُبَّهَة (with damma and geminated ba') means "greatness and majesty" (العظمة والبهاء).

A man described as "ذُو أُبَّهَةٍ" possesses "dignity and grandeur."

## تأبّه (Behavior)

"تَأَبَّهَ فُلَانٌ عَلَى فُلَانٍ" means to act proudly and elevate one's status above another.

The text includes a poetic witness (شاهد) attributed to Ruwbah: "وَطَامِحٍ مِنْ نَخْوَةِ التَّأَبُّهِ" (and one aspiring from the arrogance of pride).
```


### [2026-09-04T15:09:04.737Z] TOOL RESULT

```
# Mo'in Dictionary Entry for ابهت

According to the Mo'in (فرهنگ انتشارات معین) dictionary shown on this page:

**Origin and Form:** "(اُ بُ هَّ) \[ ع . \] (اِمص .)"

**Definitions:** The entry provides two main senses:
1. "بزرگی ، بزرگواری ، عظمت" (grandeur, magnificence, majesty)
2. "تکبر، نخوت" (arrogance, haughtiness)

No Dehkhoda entry is displayed on this particular search results page. The page does show related entries from Mo'in for جذبه (attraction/impressiveness) and سطوت (might/dignity), both of which reference ابهت as a related concept.
```


### [2026-09-04T15:09:05.118Z] TOOL RESULT

```
# Response

Based on my review of the Wikipedia article on Persian-origin Arabic words (معربات فارسية), I cannot find "أبهة" or "الأبهة" listed in the provided content.

Regarding آب-derived words, the article does mention:

**"الجاموس، معرب گاوميش، (گاو: بقرة، وميش: نعجة)"** - This references گاو (cow), which contains the آب root concept in Persian animal terminology.

Additionally: **"جلاب معرب گلاب (برای مثال از عائشة نقل است «كان إذا اغتسل من الجنابة دعا بشيء كالجلاب»)"** - This discusses جلاب from گلاب (literally "flower water").

The article does not specifically list أبريق or انبيق with their Persian etymologies in the sections provided.
```


### [2026-09-04T15:09:08.719Z] TOOL RESULT

```
# لغت‌نامه دهخدا

"ابهت. [ اُب ْ ب َ هََ ] ( ع اِ )بزرگی. ( وطواط ). بزرگواری. ( دستوراللغة ). شکوه."

The entry indicates this is an Arabic-origin term (marked as ع اِ) with meanings including grandeur, nobility, and splendor in Persian contexts.

# فرهنگ معین

"(اُ بُ هَّ ) [ ع . ] (اِمص . ) ۱ - بزرگی ، بزرگواری ، عظمت . ۲ - تکبر، نخوت ."

This dictionary also marks the term as Arabic in origin (ع) and provides dual definitions: firstly as greatness and magnificence, and secondly as arrogance or pride.
```


## [2026-09-04T15:09:35.833Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'ftāb\\|abi-tāp\\|abi-tap' CHEUNG.txt | head -10; echo ==; grep -n -i 'ābrū\\|abrū\\|āb-rū' CHEUNG.txt HUB.txt HRN.txt | head; echo == HUB; grep -n -i 'Glanz' HUB.txt | head -5; echo == PHD; grep -n -i \"^ab \\|āb \\|āfr\\|abrōy\\|ābrōy\" PHD_mackenzie.txt | head -5; grep -n -i 'aftab\\|āftāb' PHD_mackenzie.txt | head -3; echo == KLN p2; grep -n 'abdest' KLN_1966.txt | head -3",
 "description": "Grep Cheung, Hübschmann, MacKenzie for āftāb/ābrū"
}
```


### [2026-09-04T15:09:35.910Z] TOOL RESULT

```
Exit code 1
(eval):1: = not found
```


## [2026-09-04T15:09:40.113Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'ftāb\\|abi-tāp\\|abi-tap' CHEUNG.txt | head -10; echo \"--\"; grep -n -i 'ābrū\\|abrū\\|āb-rū' CHEUNG.txt HUB.txt HRN.txt | head; echo \"-- HUB\"; grep -n -i 'Glanz' HUB.txt | head -5; echo \"-- PHD\"; grep -n -i 'aftab\\|āftāb\\|abrōy' PHD_mackenzie.txt | head -5; echo \"-- KLN p2\"; grep -n 'abdest' KLN_1966.txt | head -3",
 "description": "Grep Cheung, Hübschmann, MacKenzie for āftāb/ābrū"
}
```


### [2026-09-04T15:09:40.264Z] TOOL RESULT

```
--
-- HUB
548:svar glanzen*. Auch ist es mit dieser Wurzel irn Zend
551:x'^ared^a- (bei Justi = Glanz) nicht 'Glanz' bedeuten.
760:Geldner nie sublimis*, sondern glanzend, strahlend,
762:und ist ~ phi. hamik glanzend' Gl. and Ind. p. 76,
4830:dl glanzen ^) (ipt. didlhi und dTdihi)^ u. s. w.
-- PHD
-- KLN p2
1142:Abderite,  n„  i)  an  inhabitant  of  Abdera;  2)  a fool.  —  L.  Abderita ,  fr.  Gk.  ’A(38r)ptnr]!;,  ‘in¬ habitant  of  Abdera’,  fr.”A[38if]pa  (pi.),  ‘Abdera’, a  town  proverbial  for  the  stupidity  of  its  in¬ habitants.  For  sense  development  cp.  Gotha¬ mite.  For  the  ending  see  subst.  suff.  -ite. abdest,  n.,  the  Mohammedan  rite  of  washing  the hands  before  prayer.  —  Pers.  dbddst,  lit.  ‘water for  the  hand’,  fr.  ab,  ‘water’,  and  dost,  ‘hand’. Pers.  ab,  ‘water’,  is  rel.  to  Avestic  dp-,  OI.  dpah (fern,  pi.),  ‘water’;  sec  amnic  and  cp.  the  first element  in  abkari  and  the  second  element  in doab  and  in  julep.  Pers.  dost,  ‘hand’,  is  rel.  to Avestic  zasta,  ‘hand’,  fr.  I.-E.  base  *ghosto -, whence  also  OI.  hastah,  ‘hand’.  See  hasta  and cp.  hath.
1174:Derivatives:  abjure-ment ,  n.,  abjur-er,  n. abkari,  n.,  the  sale  of  intoxicating  drinks;  the excise  duty  on  such  sale  (India).  — -  Pers.  abkari, ‘business  of  distilling’,  fr.  abkar,  ‘a  distiller’,  fr. ab,  ‘water’,  and  kar,  ‘doer,  maker’.  For  the  first element  see  abdestThe  second  element  is  related to  Avestic  kar-,  ‘to  make’,  klrlnaoiti,  OI.  karoti, kyndti,  ‘makes’,  fr.  I.-E.  base  *q'cer-,  ‘to  make, form’.  See  corpus  and  cp.  the  second  element  in Sanskrit  and  words  there  referred  to. ablactate,  tr.  v.,  to  wean.  —  L.  ablactdtus,  pp.  of ablactare,  ‘to  wean’,  fr.  ab-  and  lactare.  See lactate.
2502:the  first  element  in  abdest,  abkari,  Apsaras  and the  second  element  in  doab  and  in  Messapian. For  the  ending  of  amnic  see  suff.  -ic. amnion,  n.,  the  membrane  enclosing  the  embryos of  mammals,  birds  and  reptiles.  —  Gk.  dpvlov,
```


## [2026-09-04T15:09:52.422Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in 'https://en.wiktionary.org/wiki/آب' 'https://en.wiktionary.org/wiki/آبرو' 'https://en.wiktionary.org/wiki/آفتاب' 'https://en.wiktionary.org/wiki/أبهة' 'https://en.wiktionary.org/wiki/ابهت' 'https://en.wiktionary.org/wiki/आभा' 'https://www.islamweb.net/ar/library/content/122/22/أبه' 'https://vajehyab.com/?q=ابهت&d=moein' 'https://abadis.ir/fatofa/ابهت/' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš'; do python3 tools/fetch_source.py \"$u\" --note \"page 32, root Ab 1/Ap 1 part 2: ab 'lustre', abru, aftab, Arabic ubbaha, Persian obbohat\"; done; tail -12 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d['status'], d['bytes'], d['url'])\"",
 "description": "Archive all web sources used"
}
```


### [2026-09-04T15:09:57.721Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fa72848139f07717.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d8c962be9136432.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/948d2d1ce1d3354a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/514384b1671bf57f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3853e1d9ad1762d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ef4108a56b972c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d32abb2d5442c7b8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e13732539da950c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a69427d54598b2d9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86bc6ee14218203c.txt
200 2723 https://vajehyab.com/?q=زهاب
200 7422 https://en.wiktionary.org/wiki/زه
200 18357 https://en.wiktionary.org/wiki/پنجاب
200 2185 https://vajehyab.com/?q=آبریز
200 48466 https://en.wikipedia.org/wiki/Abadan,_Iran
200 4147 https://en.wiktionary.org/wiki/آبرو
200 2640 https://en.wiktionary.org/wiki/أبهة
200 3581 https://en.wiktionary.org/wiki/ابهت
200 5713 https://en.wiktionary.org/wiki/आभा
200 9141 https://www.islamweb.net/ar/library/content/122/22/أبه
200 838 https://vajehyab.com/?q=ابهت&d=moein
200 5471 https://abadis.ir/fatofa/ابهت/
```


## [2026-09-04T15:10:01.950Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -c 'ابهت' data/verification/sources/web/e13732539da950c0.txt data/verification/sources/web/a69427d54598b2d9.txt; grep -o 'اُ بُ هَّ[^.]*' data/verification/sources/web/a69427d54598b2d9.txt | head -2",
 "description": "Confirm archived Mo'in pages contain the entry"
}
```


### [2026-09-04T15:10:02.013Z] TOOL RESULT

```
data/verification/sources/web/e13732539da950c0.txt:6
data/verification/sources/web/a69427d54598b2d9.txt:16
```


## [2026-09-04T15:11:09.600Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat > data/verification/page-32.json <<'EOF'\n{\n  \"pdf_page\": 32,\n  \"book_page\": 2,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 1, Ap 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂ep- 'water, body of water; river' (Pokorny 2. ap- p.51, by-form ab- p.1) > Proto-Indo-Iranian *Hā́ps > Proto-Iranian *Hā́fš (Av. āfš/āp-, OP ap-, MP āb)\",\n      \"note\": \"Part 2 of the chart begun on pdf p.31. The root is real and correctly glossed (Pokorny IEW p.1 'ab- Wasser, Fluß' cross-referring to '2. ap- Wasser, Fluß' p.51; AHD ap-2 'water, river ... Persian ab'). What this part of the chart adds is a semantic branch 'water' -> 'lustre, glitter' (NP āb 2, ābrū, āftāb) -> Arabic ubbaha -> Persian obbohat. The first step (āb 'lustre' from the glitter of a water-surface, ābrū 'water of the face') is accepted; āftāb is not from āb but from Proto-Iranian *abi-tāpah (Cheung 2007); and the Arabic link is Addi Shir's (AFM p.7) isolated proposal that ubbaha is an Arabization of Persian āb + bahā — a claim no modern Arabic or Persian etymological source accepts (Lisān al-ʿArab, Wiktionary and Mo'in treat ubbaha as native Arabic from the root ʔ-b-h 'notice; be haughty'). So the chain is sound down to ābrū and breaks at node 3; node 4 (Persian obbohat < Arabic ubbaha) is a real Arabic loan but has nothing to do with the water root.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš\",\n        \"https://en.wiktionary.org/wiki/آب\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1\",\n          \"status\": \"supports\",\n          \"note\": \"POK_01.txt (IEW p.1, leaf 9): 'ab- Wasser, Fluß. Lat. amnis ... air. ab ... cymr. afon ... Vgl. auch 2. ap- Wasser, Fluß'; the Iranian forms stand under 2. ap- p.51 (POK_full.txt 'Root ap-2 (*hap-2) water, river ... Avestan Nom. Sg. āfš, Akk. Sg. āpəm'). Same finding as for pdf p.31; Pokorny is still the standard reference.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Pahlavi\",\n          \"words\": \"âp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan āp- f. 'water' (nom. sg. āfš, acc. āpəm, gen. pl. apąm) and Old Persian ap- (loc. apiyā, DSf) continue Proto-Iranian *Hā́fš < PIIr. *Hā́ps < PIE *h₂ep- (Skt. āp-/āpaḥ, Hitt. ḫapa- 'river', Lat. amnis < *abnis). Middle Persian āb (Book Pahlavi ʾp̄, Manichaean ʾb; Pāzand āw) shows the Sasanian-era lenition of post-vocalic -p- to -b/-β; the label 'Avestan / Pahlavi' collapses the Old- and Middle-Iranian stages. Identical to node 1 of the Part-1 chart on pdf p.31.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hā́fš\",\n            \"https://en.wiktionary.org/wiki/آب\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:2\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 1142 (p.2, s.v. abdest): 'Pers. āb, water, is rel. to Avestic āp-, OI. āpaḥ (fem. pl.), water; see amnic and cp. the first element in abkari and the second element in doab and in julep.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âb; âberŭ; âftâb\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) āb 2 'lustre, glitter, brilliance' (as of a blade, a gem, a water-surface; hence 'honour'): Horn (Grundriss no. 3) listed it as a separate lemma 'āb Glanz' comparing Skt. ābhā- 'splendour' (ā- + bhā- 'shine'), but in his own footnote judged that comparison 'keineswegs sicher' and observed that from 'glittering water-surface' one very easily reaches 'Glanz'; Wiktionary today simply lists 'honour, reputation, standing' as a sense of āb 'water' (Etymology 1, PIE *h₂ep-), with no separate ābhā-etymology. So the arrow āp 'water' -> āb 'lustre' is the majority view (a semantic extension, no sound change involved): CONFIRMED. (b) ābrū 'honour, reputation', shortened from āb-e rūy 'water (= lustre) of the face', Kurdish avrû, loaned into Urdu/Hindi ābrū, Ottoman âb-ı rû, Azerbaijani abır, Armenian abuṙ; Horn already cited ab[rō under the same lemma: CONFIRMED. (c) āftāb 'sunshine, sun' < MP āftāb (Pahlavi ʾptʾb, Manichaean ʾpdʾb) < Proto-Iranian *abi-tāpah 'shining upon' = preverb abi- (> MP āf-/af-) + tāp- 'to shine, be hot' (Cheung 2007 s.v. tap; Wiktionary). The first element is the preverb, not āb 'water/lustre'; Nourai's gloss 'glitter shine' follows Horn's older grouping (Horn no. 3 lists af[tāb under āb 'Glanz'), which modern Iranian etymology has abandoned: DISPUTED. Worst verdict for the node is therefore 'disputed' (for āftāb only); the Ferdowsi quotation illustrates āb 'lustre/splendour' correctly (jahān gašt bā farr o āyīn o āb).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/آب\",\n            \"https://en.wiktionary.org/wiki/آبرو\",\n            \"https://en.wiktionary.org/wiki/آفتاب\",\n            \"https://en.wiktionary.org/wiki/आभा\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:1\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt leaf 22 (Horn p.1, entry no. 3, OCR lines 464-473): '3. āb Glanz (Šahn. I S. 14 Vers 7), vergl. āb]rō, āb]tāb, āb]mend, Rōd]ābe, Suhr]āb, Mihr]āb, Ardā Vīr]āf, āf[tāb, phlv. āb; skr. ābhā- Glanz' with footnote 2: 'Die Zusammenstellung von np. āb und skr. ābhā- ist keineswegs sicher; von der Bedeutung (glitzernder) Wasserspiegel könnte man sehr leicht zu Glanz kommen' — i.e. Horn lists exactly Nourai's three words (āb 'Glanz', ābrū, āftāb) and himself suggests the 'water' origin Nourai draws; but Horn's inclusion of āftāb is superseded by Cheung's *abi-tāpah.\"\n            },\n            {\n              \"ref\": \"AEF:2\",\n              \"status\": \"not_checked\",\n              \"note\": \"Khaleqi Motlaq, Asās-e Eshteqāq-e Fārsi — no online copy; it is the Persian translation of Horn, so its p.2 presumably reproduces Horn no. 3 quoted above.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"âb-bahâ; abboha\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic أُبَّهَة ubbaha 'grandeur, majesty, pomp' (also 'haughtiness': taʾabbaha ʿalā 'to behave proudly towards', Ruʾba: wa-ṭāmiḥin min naxwati t-taʾabbuhi) is real, but 'âb-bahâ' is not an Arabic word: it is the etymon Addi Shir (AFM p.7) proposed — 'al-ubbaha: al-ʿaẓama wa-l-bahja, muʿarrab āb bahā', i.e. Persian āb 'lustre' + bahā 'splendour'. That proposal is isolated and implausible: (i) Persian bahā 'splendour' is itself the Arabic loanword bahāʾ (root b-h-w), so the alleged Persian compound would be half Arabic; (ii) Lisān al-ʿArab treats ubbaha under the native root ʔ-b-h together with the verb abaha/abiha 'to notice, become aware' and taʾabbaha 'be proud', and the fuʿʿala shape (cf. سُكَّرة, أُبَّهة) is a regular Arabic nominal pattern; (iii) Wiktionary files أبهة under root ء ب ه with no foreign origin, and the Arabic Wikipedia list of Persian loanwords (muʿarrabāt fārisiyya) does not include it. Modern Arabic lexicography therefore gives no Persian etymology for ubbaha; Nourai's arrow rests solely on Addi Shir.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/أبهة\",\n            \"https://www.islamweb.net/ar/library/content/122/22/أبه\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AFM:7\",\n              \"status\": \"supports\",\n              \"note\": \"AFM_pages.txt leaf 8 (0-based ff-page; ≈ printed p.7, among the ab- headwords الأبزن, الأوباش, الأبر), OCR: '(الأبّهة) العظمة والبهجة معرب أب بآ [= آب بها] ... بالارامية ... بهي وبالفرنسية ...' — Addi Shir does say ubbaha 'grandeur, splendour' is an Arabization of āb + bahā, which is exactly Nourai's arrow; but this is Shir's own conjecture, not accepted elsewhere.\"\n            },\n            {\n              \"ref\": \"FVF:11\",\n              \"status\": \"not_checked\",\n              \"note\": \"Emam Shushtari, Farhang-e vāžehā-ye fārsi dar zabān-e ʿarabi — only on noorlib/ketabnak behind a JS viewer/login; not readable here.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"obbohat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian ابهت obbohat (classical ubbahat, Dari ubbohat, Tajik уббаҳат) 'grandeur, majesty, imposing presence; haughtiness' is a straightforward Arabic loan of ubbaha: the Arabic tāʾ marbūṭa of أُبَّهَة is taken over as -t (as in ḥikmat, raḥmat), and Iranian Persian lowers the short vowels u > o, hence obbohat; the chart's script «أبهت» with hamza is an Arabic-style spelling of what Persian normally writes ابهت. Dehkhoda (citing Vaṭvāṭ and Dastūr al-luġa) and Mo'in both tag it [ع.] 'Arabic'. The edge Arabic -> Persian is correct; only the further link back to āb 'water' (node 3) fails, so obbohat is not an Arabic-mediated round-trip of a Persian word.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/ابهت\",\n            \"https://abadis.ir/fatofa/ابهت/\",\n            \"https://vajehyab.com/?q=ابهت&d=moein\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:131\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in s.v. ابهت (vajehyab/abadis online text): '(اُ بُ هَّ) [ع.] (اِمص.) ۱- بزرگی، بزرگواری، عظمت. ۲- تکبر، نخوت.' — Arabic loan, gloss 'grandeur'; the 2-vol. abridgement (MON_part1.txt line 6560) reads the same: 'ابهت ... [ع.] (اِمص.) بزرگی، بزرگواری، شکوه، عظمت، بهجت، شادمانی، تکبر، نخوت'. Page 131 of the 6-vol. edition cannot be mapped online, but the entry supports the Arabic origin Nourai draws (it says nothing about āb + bahā).\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nEOF\npython3 -m json.tool data/verification/page-32.json >/dev/null && echo JSON_OK; python3 tools/verify_check.py 32",
 "description": "Write page-32 verification JSON and run checker"
}
```


### [2026-09-04T15:11:11.912Z] TOOL RESULT

```
JSON_OK
nodes verified: 4/4
node verdicts: {'confirmed': 2, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 4, 'not_checked': 2}
```


## [2026-09-04T15:11:22.624Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-32.json`; `verify_check.py 32` reports full coverage (4/4 nodes, no PROBLEM lines).

**Page 32 (book p. 2) — root Ab 1/Ap 1, Part 2**
- Root: confirmed (Pokorny p.1 ab- / p.51 2. ap-; PIE *h₂ep- > PIr. *Hā́fš).
- Node verdicts: confirmed 2 (#1 Av./Pahl. āp; #4 Persian obbohat < Arabic ubbaha), disputed 2 (#2, #3).
- Ref checks: 4 supports (POK:1, KLN:2, HRN:1, AFM:7, MON:131 — quoted from local OCR/online), 2 not_checked (AEF:2, FVF:11 — not online).

Disputed items:
- **Ab 1/Ap 1, #2 âftâb**: not from āb 'lustre'; Cheung/Wiktionary derive MP āftāb from Proto-Iranian *abi-tāpah (preverb abi- + tāp- 'shine'). āb 'lustre' and ābrū 'water of the face' are fine (Horn no. 3 p.1 actually lists all three words and himself suggests the 'glittering water-surface' origin).
- **Ab 1/Ap 1, #3 Arabic âb-bahâ / abboha**: 'āb-bahā' is only Addi Shir's (AFM p.7) conjectured etymon of ubbaha; Lisān al-ʿArab, Wiktionary and Mo'in treat أُبَّهة as native Arabic (root ʔ-b-h: abaha 'notice', taʾabbaha 'be proud'), and Persian bahā is itself an Arabic loan, so the chain to the water root breaks here. Node #4 (obbohat) is a genuine Arabic loan but not a round-trip Persian word.

All 10 web pages used were archived with `tools/fetch_source.py` (Wiktionary آب / آبرو / آفتاب / أبهة / ابهت / आभा / Hā́fš, Lisān al-ʿArab via islamweb, Mo'in via vajehyab and abadis).
