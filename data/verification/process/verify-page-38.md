# Verification process log — verify-page-38


## [2026-09-04T18:46:47.580Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 38 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-38.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-38.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-38.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 38` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T18:46:49.375Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:46:51.441Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:46:51.458Z] TOOL RESULT

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
62	- **Scanned references without OCR text** (Borhan-e Qate' vols 3-5 = BQT pages ~1208-2475,
63	  Farahvashi's Iranvij = IRN, and any entry whose table record has a `scans` list): do NOT
64	  OCR whole books. Fetch only the cited page:
65	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
66	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
67	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
68	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
69	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
70	  surrounding lines you relied on) verbatim to the companion file
71	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
72	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
73	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
74	  note the correct pdf page in your ref_check note.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch.
76	- Do this for at least ONE cited reference per node (the most authoritative available:
77	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
78	  BQT/MON for Persian). If none of a node's references is accessible, say so.
79	
80	Add to every node a `ref_check` array:
81	
82	```json
83	"ref_check": [
84	  {"ref": "KLN:164", "status": "supports", "note": "Klein s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
85	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
86	]
87	```
88	
89	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
90	word but a different/looser derivation) · `contradicts` (the reference says something else)
91	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
92	not accessible online). Quote the key phrase of the reference in `note` when you can.
93	
94	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
95	
96	
97	## Process documentation (required)
98	
99	The owner wants to be able to audit every step later. Therefore:
100	
101	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
102	  curl), run
103	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
104	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
105	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
106	  one Bash command to save time.)
107	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` include
108	  the exact phrase(s) you found (with the grep pattern or page you used, e.g.
109	  "KLN.txt p.164 (ff-page 178): 'cherub … prob. rel. to Akkad. karābu'"), so the finding can
110	  be re-run.
111	- Your full transcript (every tool call and result) is exported automatically by the
112	  coordinator; nothing else needed for that.
113	
114	
115	## Use EVERY relevant book on disk (required)
116	
117	Checking only the reference Nourai cites is not enough. For every node, also consult the
118	other books in the local library that could speak to that claim, and record what each says.
119	The list of which books cover which kind of node, with file paths, is
120	`/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md`
121	(also `data/verification/sources/SOURCE_MATRIX.md`). Minimum per node:
122	
123	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
124	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
125	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
126	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
127	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
128	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY, once its text exists);
129	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
130	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
131	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
132	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
133	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
134	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
135	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
136	
137	Grep each file for the headword (several spellings; Latin transliteration for the Western
138	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
139	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
140	node (separate from `ref_check`, which is only for the references Nourai himself cites):
141	
142	```json
143	"consulted": [
144	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
145	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
146	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
147	]
148	```
149	
150	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
151	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
152	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
153	entries from different books whenever the matrix lists two or more books for its language.
154	
155	## Sources to use (in roughly this order)
156	
157	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
158	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
159	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
160	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
161	  Use URL-encoded Persian/Arabic script for those pages.
162	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
163	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
164	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
165	  appendix; the online appendix is the updated edition of the same list.
166	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
167	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
168	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
169	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
170	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
171	  if needed for a hard case.
172	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
173	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
174	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
175	
176	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
177	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
178	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
179	which are where errors are likelier.
180	
181	## Output — write ONE file per page
182	
183	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
184	
185	```json
186	{
187	  "pdf_page": 126,
188	  "book_page": 96,
189	  "verified_by": "claude-fable-5-1",
190	  "verified_on": "2026-09-04",
191	  "entries": [
192	    {
193	      "entry": 0,
194	      "root": "Dheigh, Dhigha",
195	      "verdict": "confirmed",
196	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
197	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
198	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
199	      "nodes": [
200	        {
201	          "id": 6,
202	          "lang": "Avestan",
203	          "words": "pairi-daeza",
204	          "verdict": "confirmed",
205	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
206	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
207	        },
208	        {
209	          "id": 9,
210	          "lang": "Greek",
211	          "words": "paradeisos",
212	          "verdict": "confirmed",
213	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
214	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
215	        }
216	      ]
217	    }
218	  ]
219	}
220	```
221	
222	Rules:
223	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
224	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
225	- `words` = the transliterations of the node joined by "; " (copy from the chart).
226	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
227	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
228	- Keep `note` on the entry for root-level comments and for anything cross-cutting
229	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
230	- If a node lists several words, cover each word; if they differ in verdict, use the worst
231	  verdict for the node and explain per word in `derivation`.
232	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
233	  from root Mad"), evaluate it: say which side modern scholarship takes.
234	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted` (array).
235	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
236	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
237	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
238	  Do not paste the JSON back into your reply.
239	
```


## [2026-09-04T18:46:51.637Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-38.txt"
}
```


### [2026-09-04T18:46:51.660Z] TOOL RESULT

```
1	=== PDF page 38 (book page 8) ===
2	--- entry 0 ---
3	ROOT [Avestan] Ahu : defect, fault  (refs BQT:72)
4	#1 (parent #0) [Pahlavi] refs=BQT:72 | ahŭk 2 : fault
5	  #2 (parent #1) [Persian] refs=BRT:345 | âhŭ 2 «آهو۲» : defect | NOTE: FAF:38 claims this word is from AV "a-hu: not good".
6	#3 (parent #0) [Avestan] refs=BQT:72; FAF:36; KNT:167 | âhita : dirty, faulty ; an-âhita : not dirty, clean, innocent, spotless ☞Ne 1
7	  #4 (parent #3) [Persian] refs=FAF:36 | Ânâhîta «آناهیتا» : "innocent, clean", a female name ; Nâhîd «ناهید» : "innocent, clean", a female name, a bright star
8	--- entry 1 ---
9	ROOT [Indo-European] Ai : to give  (refs POK:10)
10	#1 (parent #0) [Avestan] refs=POK:10 | aěta : share
11	#2 (parent #0) [Greek] refs=AHD | dia-ithan : to decide on one's life
12	  #3 (parent #2) [English] refs=None | diet
13	
```


## [2026-09-04T18:46:56.223Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-38.json; echo \"=== MATRIX ===\"; cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:46:56.267Z] TOOL RESULT

```
{
  "pdf_page": 38,
  "book_page": 8,
  "entries": [
    {
      "root": {
        "name": "Ahu",
        "lang": "Avestan",
        "refs": "BQT:72",
        "gloss": "defect, fault"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:72",
          "words": [
            {"translit": "ahŭk 2", "gloss": "fault", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BRT:345",
          "words": [
            {"translit": "âhŭ 2", "gloss": "defect", "script": "آهو۲"}
          ],
          "note": "FAF:38 claims this word is from AV \"a-hu: not good\".",
          "quote": {"text": "زگیتی بی آهو نیابی کسی - اگر چند دارد هنر ها بسی", "poet": "Vîs-o-Râmîn"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:72; FAF:36; KNT:167",
          "words": [
            {"translit": "âhita", "gloss": "dirty, faulty", "script": null},
            {"translit": "an-âhita", "gloss": "not dirty, clean, innocent, spotless", "script": null, "see": ["Ne 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "FAF:36",
          "words": [
            {"translit": "Ânâhîta", "gloss": "\"innocent, clean\", a female name", "script": "آناهیتا"},
            {"translit": "Nâhîd", "gloss": "\"innocent, clean\", a female name, a bright star", "script": "ناهید"}
          ],
          "note": null,
          "quote": {"text": "از آن ترس کو هوش و زور آفرید - درخشنده ناهید و هور آفرید", "poet": "Ferdowsî"}
        }
      ]
    },
    {
      "root": {
        "name": "Ai",
        "lang": "Indo-European",
        "refs": "POK:10",
        "gloss": "to give"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:10",
          "words": [
            {"translit": "aěta", "gloss": "share", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "dia-ithan", "gloss": "to decide on one's life", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "diet", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **RCH** — J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt`
- **NAT** — C. Berlitz, Native Tongues, New York 1982
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt`
- **PEI** — M. Pei, The Families of Words, New York 1962
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt`

## Turkic / Mongolian

- **TTS** — H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt`
- **VIE** — M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt`
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf`

## Sanskrit / Hindustani

- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt`
- **GPL** — J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt`
- **AID** — G. C. Whitworth, An Anglo-Indian Dictionary, London 1885
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt`
```


## [2026-09-04T18:47:02.699Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['BQT','BRT','FAF','KNT','POK','AHD','MON','HRN','HUB','PHD','NYB','KLN','WLD','IEC','SYN','SKT','ARY','CHEUNG','FSD','WEB']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; echo \"=== FAF bib ===\"; grep -n -i -A3 'FAF' /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt | head -40; echo \"=== ls verification ===\"; ls /home/sfmqrb/git/rishe/data/verification/ | head -30"
}
```


### [2026-09-04T18:47:04.538Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
=== FAF bib ===
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
4-===== page_16
5- Page 16 
6- TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
--
9: TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
10-===== page_18
11- Page 18 
12- TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
=== ls verification ===
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-35.json
page-36.json
process
sources
```


## [2026-09-04T18:47:08.464Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -80 data/verification/page-36.json; echo \"=== verify_check ===\"; sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-04T18:47:08.515Z] TOOL RESULT

```
{
  "pdf_page": 36,
  "book_page": 6,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "Agaru",
      "verdict": "confirmed",
      "modern_form": "Akkadian agāru 'to hire' (stative agir), with agru / agarru 'hired man, hireling' and igru 'wages'",
      "note": "The root box is right: Akkadian agāru 'to hire' is a well-attested verb (CAD A/1 s.v. agāru; Zimmern, Akkadische Fremdwörter, 2nd ed. 1917, p.47). The Semitic left branch of this chart (Akk. > Aram./Syr. > Arab. ʾajara > Persian ejāre/ojrat/ajr) is solidly supported by Nourai's own references and is still the standard account. The Greek right branch is the weak point: Zimmern (1917), Jeffery (1938) and Klein (1966) do connect Greek ἄγγαρος (and through it ἄγγελος) with Akkadian agru 'hireling', but current scholarship (Beekes, EDG 2010; Tavernier, Iranica in the Achaemenid Period 2007, followed by Wiktionary) instead derives ἄγγαρος from Old Persian *angara- 'missive' < Aramaic *ʾiggartā < Akkadian egirtu 'inscribed tablet, letter' — a different Akkadian etymon. Watkins (AHD appendix) simply says 'unknown Oriental source'. One transliteration point: the chart's Arabic verb is printed in the JSON as 'a`jara'; the verb is أَجَرَ ʾajara, root ʾ-j-r with hamza, not ʿayn (Zimmern writes ʾagara, Klein 'Arab. ajara'). Since the chart elsewhere uses the backtick for ʿayn (Mo`ayyerî), this is most likely a hamza/ʿayn confusion introduced somewhere between the print and the JSON.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82",
        "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82",
        "https://www.etymonline.com/word/angel"
      ],
      "ref_check": [
        {"ref": "KLN", "status": "supports", "note": "KLN_1966.txt \\f-leaf 51 (≈ printed p.74-78), s.v. angel: 'of Persian, ult. of Sem. origin. Cp. Akkad, agarru, \"hireling, hired laborer\", fr. agaru, to hire, which is rel. to Aram. agar, eggār, \"he hired\", (whence Arab. ajara, of s.m.)'. Klein is exactly Nourai's root box."}
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Syriac",
          "words": "",
          "verdict": "confirmed",
          "derivation": "Empty pass-through node standing for the Aramaic/Syriac stage. Akkadian agāru 'to hire' was taken over into Imperial Aramaic as ʾgr (ʾăgar 'he hired'), Syriac ܐܓܪ ʾegar 'to hire', with the nouns ܐܓܝܪܐ ʾăgīrā 'hireling, hired labourer' and ܐܓܪܐ ʾagrā 'wage, reward'. The Aramaic forms keep the Akkadian consonant skeleton unchanged (ʾ-g-r); the word is far commoner in Syriac than in Jewish Aramaic, which is why Jeffery makes Syriac specifically the donor to Arabic. Placing Syriac between Akkadian and both Arabic and Greek is therefore right for the Arabic branch and at least defensible for the Greek one.",
          "sources": ["https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1"],
          "ref_check": [
            {"ref": "KLN", "status": "supports", "note": "KLN_1966.txt leaf 51 s.v. angel: 'fr. agaru, to hire, which is rel. to Aram. agar, eggār, \"he hired\", (whence Arab. ajara, of s.m.)' — Klein's Aramaic is Nourai's Syriac node."}
          ],
          "consulted": [
            {"src": "FVQ", "where": "p.49 (FVQ_pages.txt leaf 66)", "stance": "supports", "note": "'From this come on the one hand the Aram. אגר : Syr. ܐܓܝܪܐ a hireling, and thence the denominative verbs אגר and ܐܓܪ, to hire, with corresponding nouns … It would have been from the Aram. that the word passed into Arabic … as the word is of much wider use in Syriac than in Jewish Aramaic, we are probably right in considering it as a borrowing from Syriac.'"},
            {"src": "AKD", "where": "p.47 (AKD.txt leaf 56)", "stance": "supports", "note": "'akk. agru, agir, agarru Mietsklave, agāru mieten : > wohl aram. ʾegar mieten, ʾăgīrā Lohnarbeiter (> arab. ʾagara)'."},
            {"src": "AFA", "where": "grep 'agara|aggara|agir' in AFA.txt", "stance": "silent", "note": "Fraenkel's Aramäische Fremdwörter has no entry for this root in the OCR text."}
          ]
        },
        {
          "id": 2,
          "lang": "Arabic",
          "words": "a`jara",
          "verdict": "confirmed",
          "derivation": "Arabic أَجَرَ ʾajara 'he hired, he gave wages, he rewarded' (root ʾ-j-r), with the verbal noun أَجْر ʾajr 'wage, reward' and أُجْرَة ʾujra 'hire, rent'. Aramaic/Syriac ʾ-g-r was taken into Arabic in the pre-Islamic period; Aramaic g regularly answers Arabic j (ǧ), so ʾăgar → ʾajara with no other change. Jeffery notes that the Muslim lexicographers took the root for pure Arabic but that the verb أجر 'to receive hire' is obviously denominative from the noun أجر, which betrays the loan. NOTE on the data: the JSON transliteration 'a`jara' has a backtick where a hamza belongs — the verb is ʾajara (ʾ-j-r), not *ʿajara (ʿ-j-r); the chart uses the same backtick for ʿayn elsewhere on the page, so this is very likely a hamza/ʿayn confusion in the transcription rather than Nourai's claim.",
          "sources": ["https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1"],
          "ref_check": [
            {"ref": "AKD:47", "status": "supports", "note": "AKD.txt \\f-leaf 56 = printed p.47: 'akk. agru, agir, agarru Mietsklave, agāru mieten : > wohl aram. ʾegar mieten, ʾăgīrā Lohnarbeiter (> arab. ʾagara); > wahrsch. auch ἄγγαρος urspr. wohl Mietling und dann erst Postknecht.' Zimmern's page is exactly the arrow Nourai draws, and Zimmern too writes the Arabic with the aleph/hamza, not ʿayn."},
            {"ref": "FVQ:49", "status": "supports", "note": "FVQ_pages.txt leaf 66 = printed p.49 (heading 'FOREIGN VOCABULARY OF THE QUR'AN 49'), s.v. أجر 'reward, wages': 'Zimmern, Akkad. Fremdw. 47, has pointed out that the ultimate origin of the root in this sense is the Akk. agru, agarru, hired servant … It would have been from the Aram. that the word passed into Arabic, probably at a very early period … we are probably right in considering it as a borrowing from Syriac.'"}
          ],
          "consulted": [
            {"src": "KLN", "where": "KLN_1966.txt leaf 51, s.v. angel", "stance": "supports", "note": "'Aram. agar, eggār, \"he hired\", (whence Arab. ajara, of s.m.)'."},
            {"src": "RCH", "where": "RCH.txt leaf 122", "stance": "supports", "note": "Richardson lists 'A أجرة ujrat, Reward, recompense, hire, rent, wages' — marked A(rabic), the word and sense the chart gives."},
            {"src": "PLA", "where": "grep in PLA_pages.txt (Asbaghi, Persische Lehnwörter im Arabischen)", "stance": "silent", "note": "Asbaghi does not list أجر — consistent with the word being an Aramaic, not a Persian, loan in Arabic."}
          ]
        },
        {
          "id": 3,
          "lang": "Persian",
          "words": "ejâreh «اجاره»; ojrat «اجرت»; ajr «اجر»",
          "verdict": "confirmed",
          "derivation": "All three are ordinary Arabic loans in New Persian, taken over after the Islamic conquest from the Arabic root ʾ-j-r: إِجَارَة ʾijāra (form-IV verbal noun) → Persian ejāre/ejārat اجاره 'lease, rent'; أُجْرَة ʾujra → Persian ojrat اجرت 'wage, fee' (Persian keeps the Arabic tāʾ marbūṭa as -at in the older pronunciation); أَجْر ʾajr → Persian ajr اجر 'reward, recompense', the sense Ḥāfeẓ uses in the couplet quoted on the chart ('اجر صبری است …'). The native Middle/New Persian word for the same notion is mizd/muzd (MP mizd 'reward, hire, pay', MacKenzie PHD), so these are lexical replacements, not inherited forms. The route Akkadian → Aramaic/Syriac → Arabic → Persian is therefore correct as drawn.",
          "sources": ["https://en.wiktionary.org/wiki/%D8%A3%D8%AC%D8%B1"],
          "ref_check": [
            {"ref": "MON", "status": "partial", "note": "The 6-vol page is not cited by number so the exact page could not be located, but Mo'in's text (2-vol Adena abridgement, MON_part1.txt) tags all three as Arabic: 'اجاره: [- اجارت، ع. اجارة] (مص‌ع.) … به مزد گرفتن' and 'اجرت: [ع. اجرة] (ا.) مزد، مزدکار، دستمزد … کرایه'. Mo'in confirms the words and their Arabic origin, i.e. the last arrow of the chain."}
          ],
          "consulted": [
            {"src": "MON", "where": "MON_part1.txt s.vv. اجاره، اجرت (2-vol abridgement, no page numbers)", "stance": "supports", "note": "'اجاره: [- اجارت. ع. اجارة]' and 'اجرت: [ع. اجرة] (ا.) مزد، مزدکار، دستمزد' — Mo'in's [ع.] tag = Arabic."},
            {"src": "RCH", "where": "RCH.txt leaf 122 s.v. ujrat", "stance": "supports", "note": "'A أجرة ujrat, Reward, recompense, hire, rent, wages' in a Persian-Arabic-English dictionary, marked Arabic."},
            {"src": "PHD", "where": "PHD_mackenzie.txt leaf 77 s.v. mizd", "stance": "partial", "note": "'mizd [m(y)zd | N muzd] reward, hire, pay. -war [-wbl | N -ur] hireling' — the inherited Iranian word; MacKenzie has no ʾgr-type word, confirming that ajr/ojrat/ejāre are post-conquest Arabic imports."},
            {"src": "HRN", "where": "grep 'ajr|ijar|uǧrat' in HRN.txt", "stance": "silent", "note": "Horn's Grundriss covers only inherited Iranian vocabulary and has no entry — expected for an Arabic loan."}
          ]
        },
        {
          "id": 4,
          "lang": "Greek",
          "words": "angelos; eu-angelos; evangelion",
          "verdict": "disputed",
          "derivation": "The Greek words are of course real: ἄγγελος 'messenger' (Mycenaean a-ke-ro, so attested by the 13th c. BCE), εὐάγγελος 'bringing good news', εὐαγγέλιον originally 'reward given to the bearer of good news', then in the Koine 'good news, gospel'. What is disputed is the arrow. Nourai follows Zimmern (1917), Jeffery (1938) and Klein (1966), who derive Greek ἄγγαρος 'Persian mounted courier' from Akkadian agru/agarru 'hireling' (Klein's semantic ladder 'hireling → hired messenger → messenger'), and then treat ἄγγελος as a doublet of ἄγγαρος; Nourai's gloss 'hired messenger' for angelos is that reconstruction, not an attested Greek sense. Modern scholarship prefers a different Akkadian source: Beekes (EDG 2010) and Tavernier (Iranica in the Achaemenid Period, 2007) derive ἄγγαρος from Old Persian *angara- 'missive, letter' < Aramaic *ʾiggartā / *ʾengartā < Akkadian egirtu 'inscribed tablet, letter', and expressly say it is NOT from agru 'hired man'. Klein himself hedges by citing both etyma (agarru 'hireling' AND Heb. iggereth / Aram. iggartā 'letter') in one breath. Watkins (AHD IE-roots appendix) declines to choose: '[angelos. Messenger. Greek noun, akin to Greek angaros, mounted courier, both from an unknown Oriental source.]'; Skeat says only 'from O. Persian'. So: a Near-Eastern loan — yes, essentially undisputed; from the 'hire' root agāru — a minority, now largely superseded, view. There is also a structural problem with the chart: it hangs Greek off the Syriac node, whereas every version of the Semitic hypothesis routes the word through Persian/Median (ἄγγαρος is a Persian institution — the royal post described by Herodotus 8.98).",
          "sources": [
            "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B5%CE%BB%CE%BF%CF%82",
            "https://en.wiktionary.org/wiki/%E1%BC%84%CE%B3%CE%B3%CE%B1%CF%81%CE%BF%CF%82",
=== verify_check ===
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
VER = os.environ.get("VERIFY_DIR") or os.path.join(ROOT, "data", "verification")


def page_no(path):
    return int(os.path.basename(path).split("-")[1].split(".")[0])


def main(argv):
    only = set(int(a) for a in argv[1:])
    missing_pages, problems = [], []
    tally = collections.Counter()
    root_tally = collections.Counter()
    ref_tally = collections.Counter()
    con_tally = collections.Counter()
    con_books = collections.Counter()
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
                for c in vn.get("consulted") or []:
                    con_tally[c.get("stance")] += 1
                    con_books[c.get("src")] += 1
    print(f"nodes verified: {nodes_done}/{nodes_total}")
    print("node verdicts:", dict(tally))
    print("root verdicts:", dict(root_tally))
    print("ref checks:", dict(ref_tally))
    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
    if missing_pages:
        print(f"pages without verification ({len(missing_pages)}):", " ".join(map(str, missing_pages)))
    for p in problems:
        print("PROBLEM:", p)
    if "--flagged" in os.environ.get("VERIFY_OPTS", "") or os.environ.get("FLAGGED"):
        for f in flagged:
            print("FLAG:", *f[:4], "|", f[4][:200])
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```


## [2026-09-04T18:47:46.107Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['BQT','BRT','KNT','POK','AHD','MON','ARY']:\n    print('###',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-04T18:47:47.611Z] TOOL RESULT

```
### BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt"
 ],
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
 "covers_etymology": true,
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
 "scans": [
  {
   "volume": "3",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
   "first_printed": 1208,
   "last_printed": 1925,
   "pdf_offset": -1205,
   "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json",
   "lang": "fas",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
   "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"
  },
  {
   "volume": "4",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
   "first_printed": 1920,
   "last_printed": 2475,
   "pdf_offset": -1917,
   "lang": "fas",
   "offset_note": "printed = pdf+1917, checked at pdf 150 and 500",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"
  },
  {
   "volume": "5",
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf",
   "first_printed": 1,
   "last_printed": 290,
   "pdf_offset": 5,
   "lang": "fas",
   "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt",
   "requires_volume": true
  }
 ],
 "cites": "page number, continuous across the five volumes of Mo'in's edition (1342/1963 = Amir Kabir 1362 reprint); Mo'in's etymological footnotes are the cited material"
}
### BRT
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
### KNT
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
### POK
{
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
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
### AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
### MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
### ARY
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"
}
```


## [2026-09-04T18:47:53.622Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full ai- ===\"; grep -n -i -B2 -A30 'lemma: ai-' POK_full.txt | head -80\necho \"=== POK_01 p10 (leaf 18) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==19' POK_01.txt | head -60"
}
```


### [2026-09-04T18:47:55.201Z] TOOL RESULT

```
=== POK_full ai- ===
2582-Page(s): 9 
2583-
2584:Root / lemma: ai-6'^-, Ad^- nasalized /-n-6^-{*av/-6^-) 
2585-
2586-English meaning: to burn 
2587-
2588-Note: 
2589-
2590-Common lllyrian -gh->-dh- 
2591-
2592-Material: Old Indie inddhe^ inflamed, is aroused ' (pass, idhyate, Perf. Tdhe, part. Perf. 
2593-
2594-Pass iddha-h), indhana-m^ lighting '. 
2595-
2596-Gr. aiGw " lights, burns ' (aiGopsvoc;), aiGwv, al9oi|j " igneous, sparkling ', i9aiv£a9ai 
2597-0£Pfjaiv£o9ai Hes., hylleisch aiSwaaa aiGouoa " to light up, kindle '; changing by ablaut 
2598-KaK-ien(; Hes. 'ravenously' (W. Schuize KZ. 29, 269 = Kl. Schr. 329). common gr.- lllyrian 
2599-ks- > -ss- 
2600-
2601-Maybe alb. (*5ujaaa) ndez^ to light up, kindle '. 
2602-
2603-
2604-
2605-o-Grade:gr. al9o(; m. "fire' (ai96(; "burntly') = Old Indie edha-hxw. "Firewood' = Old 
2606-English ad. Old High German Middle High German eitvc\. " glow, pyre ': zero grade 
2607-probably Norwegian Swedish id^ leuciscus idus ' (a bright carp kind), of Modern High 
2608-German dial, alter leuciscus cephalus' as the " shining '; besides u- stem *ai6!"u- in gall. 
2609-VN Aedui, Old Irish aed^f\re\ also as MN; Latin aedes^ a dwelling of the gods, a 
2610-sanctuary, a temple ', ursprijngl. " the domestic stove ', also aedis= maked. ab\c, saxapa 
2611-Hes. 
2612-
2613-From the verbal adjective in -/o- derived probably Latin aestas, - af/s 'yNarm season, 
2614-summer' (from *aisto-tat-, Indo Germanic *afd!"-to-)\ aestus, - Js(from *aiA^-tu-) "heat, 
--
2844-Page(s): 1 5 
2845-
2846:Root/ lemma: ai-2{*avi-2) 
2847-
2848-English meaning: to drive, to overwhelm, harm 
2849-
2850-
2851-
2852-Material: present *{a)i-neu-mr. Old Indie inoti, fnvati, Imper. inuhf, participle -inita- 
2853-{upenita-^ pushed, cut into '), " penetrate into something, master', Avestan inaoiti. Inf. 
2854-aenarjhe^ violate, hurt ', a /n /ta {irom *an-initaby haplology) " not violated, not painedly ' 
2855-(from Old Indie enas- n. ' Crime, sin, misfortune ' = Avestan aenah-' act of violence, crime 
2856-', in addition m. ' evildoer'?), Avestan />7/5y-'rape, injury; torture ', Old Indie ina- 'strong; m. 
2857-master ', maybe also Tti-h\. 'plague, need'; gr. aiv6(; 'tremendous'; 
2858-
2859-maybe here-//?- in Gothic /^//'-//7a 'guilt, reproach'. Old High German firindn^s\v\\ Old 
2860-Icelandic firnu. PI. 'the extraordinary' (cf Weisweiler IF. 41, 29 f.), if original meaning ' act 
2861-of violence '. 
2862-
2863-References: WP. I 1, Feist 139/140. 
2864-Page(s): 1 
2865-
2866:Root / lemma: ai-3, {*hei-, heiua) 
2867-
2868-English meaning: to give 
2869-
2870-Note: 
2871-
2872-Root/ lemma: ap-1 {exact ap-) : ep-: to take, grab, reach, *give' > Root/ lemma: ep/-: 
2873-
2874-'comrade' > Root/ lemma: a/-3: 'to give'. 
2875-
2876-Material: Gr. {*avinumai) a'lvupai 'take, pack, touch', only present and imperfect tense. 
2877-
2878-Venetic MN {*avi-mos) Aimos, lllyrian MN {*ave-ta/) Aetor. 
2879-
2880-Latin {*ave-mulus) ae-mulus^ emulous, rivalling; in bad sense, jealous. M. orf. as 
2881-subst., a rival, esp. in love ', probably as ' reaches for something ' (Frisk Eranos 41 , 53). 
2882-
2883-Tocharian B {*avi) a'h, A e-, infinitive B {*avi-tsi) aitsi, A ess/'give'; Hittite pa-a-T he 
2884-gives ', 3. PI. p{-ia)-an-ziW\\h proverb /?e- 'there'. 
2885-
2886-Note: 
2887-
2888-common Hittite p/77e- : Slavic p/7jo- : Albanian p/7ia- > pe- prefix. 
2889-
=== POK_01 p10 (leaf 18) ===
(j,9-ar  Y.lrjQova^ai.  ^eaßtoi  Ues.]  atcrtog  , gutes  Geschick verheißend,  günstig',  aXai^og  ,vom  Schicksal  bestimmt,  gebührend',  ccvcaai- fxöü)  ,an wenden,  gebrauchen,  verzehren',  af(7i;^raw  , spreche  Recht,  herrsche'; dicciTdo)  (vielleicht  dissimiliert  aus  *diaLTida))  ,bin  Schiedsrichter,  leite; teile  das    Leben   ein  =  führe    eine   gewisse   Lebensart;    schreibe   ein   ge-
11
visses  Maß  im  Essen  und  Trinken  vor',  daher  ö'iaira  ,Schiedsricliteramt' und    Lebensweise,   Lebenseinteilung-',  e^acvog  , ausgewählt,  auserlesen'.
Osk.  Gen.  aeteis  ,partis',  aittiüm  ,portionum'.
Aus  dem  Gr.  hierher  wohl  auch  akiog  , haftbar,  schuldig'  (das  t  nach ahecü),  woraus  späteres  ahla  , Schuld,  Ursache';  auch  ahico,  ahi^cü  , for- dere' als  , seinen  Anteil  verlangen';   ablaut.  ohog  m.  , Schicksal'.
Air.  äes  n.,  cymr.  oes  f.  , Alter,  Zeitalter'  aus  "^ait-to-,  air.  des  m.  , Leute' aus   *ait-tu-,    cymr.  oed  m.  , Alter'  aus  *aito-,
WP.  I  2,  Hirt  Idg.  Gr.  II,  82 f.  Schwjzer  Gr.  Gr.  1  421^,  696^,  7051;
4.  äi-  , brennen,  leuchten'.
S.  unter  ai-dh-,  uier-,  aios-,  aisk-,  ai-tro-.
Das  aus  ag"s.  äfov  , scharf,  heftig',  ahd.  eibar,  eivar  ,acerbus,  amarus, horridus'  erschlossene  *aibhro-  ist  nicht  sicher  anzuschließen.
Vielleicht  aber  hierher  gr.  iaLvco  , er  wärme'  aus  *i{i)-aniö]  s.  unter  1.  eis- ,sich  heftig   bewegen'.
5.  ai-  :  oi-  , bedeutsame  Rede'  (?).
Gr.  mvrjixi,  alveu  ^lobe^,  airoq  m.,  aiWi  f.  .bedeutsame  Rede,  Lob';  al- viaaoiiai  ,rede  in  Rätseln',  aXviy^ia  n.  , dunkle  Rede'  (aber  dv-aivoiiai  »ver- neine' scheint  -lo-Ableiteng  der  Negation  ccv-)]  ablaut.  mir.  öeth  m.  ,Eid' (acymr.  anutonou  PL,  gl.  ,periuria',  ncymr.  anndon  , Meineid')  =  got. aips  m.,  aisl.  eidr,  ags.  öjb,  as.  ^d,  ahd.  eid  m.  ,Eid'  (wohl  kelt.  Lw.).
WP.  I  2,  103,  Osthoff  BP>.  24,  208 f.
aid-  , schwellen'  s.  oid-.
ai'dh,  i-dh-,  nas.  i-n-dh-  , brennen,  leuchten'.
Ai.  inddhe  , entzündet,  entflammt'  (Pass.  idhydte,  Per  f.  idJiB^  Part.  Perf. Pass.  iddhd-h),  indhana-m  ^das  Anzünden'.
Gr.  aid-oj  , zünde  an,  brenne'  (al&ö(j,8vog),  ai'd^wv,  alOoip  , feurig,  fun- kelnd', id-alvEGdai'  d-sof^cdveGd-at  Hes.,  hylleisch  aldwaaa'  al'O-ovaa  , Loggia'; ablautend  xax-i&ijg  Hes.  ^ausgehungert*^  (W.  Schulze  KZ.  29,  269  =  Kl. Sehr.  329).
o-St.:  gr.  ald-og  m.  , Brand'  (ald-ög  ,verbrannt')  =  ai.  idha-h  m.  , Brenn- holz' =  ags.  ädj  ahd.  mhd.  elt  m.  ,Glut,  Scheiterhaufen':  schwundstufig wohl  norw.  schwed.  id.  .leuciscus  idus'  (eine  helle  Karpfenart),  vgl.  nhd. dial.  aitel  , leuciscus  cephalus'  als  ,der  Glänzende';  dane
```


## [2026-09-04T18:47:59.787Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==18' POK_01.txt | tail -40"
}
```


### [2026-09-04T18:48:01.447Z] TOOL RESULT

```
)  ;agnas^  aus  Kreuzung  von  '^'hedlno-  =  lat.  haedlnus  und  *abnino- =  lat.  agninus  erklärt  werden  könnte;  Avürde  allerdings  das  umbr.  b  auf unaspirierte  Media  hinweisen.  Aber  vielleicht  ist  gy^h  im  Osk.-Umbr.  zu  b geworden.
Lat.  avillus  ;Lämmchen'^  wegen  der  Suffixbildung  nicht  zu  ovis,  son- dern aus  "^ag'-ihnelos.
WP.  I  39;  WH.  I.  23.
10
1.  ai  Ausruf.
Ai.  e  Ausruf  des  Sichbesinnens^  der  Anrede^  des  Mitleids; ai.  ai  dasselbe;  ayi  Interjektion  beim  Vokativ; av.  äi  Interjektion  des  Anrufs  vor  dem  Vokativ;
gT.  al,  ai,  aial  Ausruf  der  Verwunderung^  des  Staunens  oder  Schmerzes (davon  aidloj  ;,seufze;  beklage^;  aiayi-ta  ^Seufzen^); lit.  at  und  di  ^ach!  wehe!^  und  vor  Vokativen. WP.  I  1,  WH.  I  396,  Benveniste  Origines  130  f.  S.  auch  *aik-.
2.  ai-  ^worauf  eindringen,  treiben,  überwältigen,  kränken^.
Präs.  *(a)i-neu-mi :  Sil.  inötl,  invati,  Imper.  inuM,  Partiz.  -in'ita-  (lipenita- ,eingedrückt,  eingeschnürt^),  ,auf  etwas  eindringen,  bewältigen^,  av.  inaoiti, Inf.  aenaidhe  ,vergewaltigen,  kränken^,  ainita  (aus  *an-inita  durch  Haplo- logie)  ,nicht  vergewaltigt,  nicht  gekränkt^  (ob  dazu  ai.  enas-  n.  ,Frevel, Sünde,  Unglück^  =  av.  aenah-  ,Gewalttat,  Frevel^,  ra.  ,Übeltäter^?),  av. intay-  ,Vergewaltigung,  Kränkung;  Qual^,  ai.  ind-  ,stark;  m.  Gebieter^, vielleicht  auch  Ui-h  f.  ,Flage,  Not^;  gr.  alvög  ,schrecklich^;
vielleicht  hierher  -in-  in  got.  fair-ina  ,Schuld,  Vorwurfe,  ahd.  firinön ,sündigen^,  aisl.  firn  n.  PI.  , Außerordentliches^  (vgl.  Weisweiler  IF.  41, 29  f.),  falls  ursprüngliche  Bedeutung  (wie  im  Heliand)  ,Gewalttat^
WP.  I  1,  Feist  139/140.
j.  ai-  ^geben,  zuteilen^,  über  mediales  ,sich  geben  lassen^  dann  auch  ,nehmen^
Gr.  aXw^iai  ,nehmen,  packen,  fassen^,  nur  Präsens  und  Imperfekt.
Ven.  MN  Aimos,  illyr.  MN  Aetor.
Lat.  ae-mulus  ,nach-,  wetteifernd^,  wohl  als  ,der  nach  etwas  greift^ (Frisk  Eranos  41,  53).
Toch.  B  ai-,  A  e-,  Infinitiv  B  aitsi,  A  essi  , geben';  hett.  pa-a-i  ,er  gibt', 3.  PI.  p{(-{ayan-zi  mit  Präverb  pe  ,hin'.
Pedersen  Groupement  20,  Hittitisch  115,  Tocharisch  227;  Frisk  Indo- germ.  10  f.
Hierher  gehört  zweifellos:
ai-ti-,  ai-tO'  :  oi-to-  , Anteil'.
Av.aeta-  ,der  gebührende  Teil'  (,Strafe';  Dual  , Schuld  und  Strafe').
Gr.  alaa  (*ahia)  , Anteil,  Schicksal',  hom.  tW,  besser  l'aaa  ,der  gebüh- rende Anteil',  iW«
```


## [2026-09-04T18:48:10.808Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD ai- ===\"; grep -n -A12 '^ai-1' AHD_watkins1985.txt | head -40; echo \"---alt\"; grep -n -i 'diaita\\|DIET' AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T18:48:10.882Z] TOOL RESULT

```
=== AHD ai- ===
268:ai-1, To give, allot. 1. Suffixed form “ai-t-yd in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-td- in Greek diaitan, to decide, lead one’s life: DIET!. [Pok. 3. ai- 10.]
269-ai-2, An utterance. Suffixed form *ai-no- in Greek ainos, tale: ENIGMA. [Pok. 5. ai- 11.]
270-aidh-. To burn. 1. Suffixed form *aidh-sto- in: a. Ger- manic *aistaz in Old English dsé, kiln: oast; b. Latin aestas (stem aestat- for earlier *aestotat-), heat, summer: AESTIVAL. 2. Suffixed form *aidh-lo- perhaps in Ger- manic *ail- in Old English dl, fire: ANNEAL. 3. Suffixed form *aidh-i- in Latin aedés, aedis, building, house (<
271-“hearth”): AEDILE; EDIFICE, (EDIFY), MAZAEDIUM. 4. Suffixed form *aidh-stu- in Latin aestus, heat, swell, surge, tide: ESTUARY. 5. Suffixed form *aidh-er- in Greek aithér, air: AETHER, ETHER. [Pok. ai-dh- 11.]
272-aig-. Goat. Greek aigis, goatskin (shield of Athena): AEGIS. [Pok. 3. aig- 13.] .
273-ais-. To wish, desire. Suffixed form *ais-sk- in Germanic *aiskOn in Old English dscian, dcsian, to ask, seek: ASK. [Pok. 1. ais- 16.]
274-aiw-. Vital force, life, long life, eternity; also “endowed with the acme of vital force, young.” 1. Extended form in Germanic *aiwi in: a. Old English a, ever: No}; b. Ger- manic *aiwi + *wihti, “ever a thing, anything” (*wihii-, thing; see wekti-), in Old English Gwiht, duht, anything, “ever a creature”: AUGHT!; c. Old English &fre (second element obscure), ever: EVER; EVERY, NEVER; d. Old Norse ei, ever: AYE?; NAY. 2. Suffixed form *ai-wo- in: a. Latin aevum, age, eternity: COEVAL, LONGEVITY, ME- DIEVAL, PRIMEVAL; b. suffixed form *aiwo-tdt- in Latin aetds (stem aetdt-), age: AGE; COETANEOUS; C. suffixed form *aiwo-terno- in Latin aeternus, eternal: ETERNAL; SEMPITERNAL. 3. Suffixed form *aiw-en- in Greek aidn, age, vital force: EON. See also *yuwwen- under yeu-. [Pok. aiu- 17.]
275-ak-. Sharp. 1. Suffixed form *ak-yd- in: a. Germanic *akjo in Old English ecg, sharp side: EDGE; b. Germanic *akjan in Old Norse eggja, to incite, goad: EGG?. 2. Suf- fixed form *ak-u- in: a. Germanic *ahuz in Old English éar, zr, zhher, spike, ear of grain: EAR?; ACROSPIRE; b. Latin acus, needle: ACICULA, (ACUITY), ACUMEN, ACUTE, AGLET, EGLANTINE. 3. Suffixed form *ak-men, stone, sharp stone used as a tool, with metathetic variant *ka-men, with variants: a. *ka-mer- in Germanic *hama- raz in Old English hamor, hammer: HAMMER; b. *ke- men- (probable variant) in Germanic *himin-, in dissimi- lated form *hibin-, “the stony vault of heaven,” in Old English heofon, hefn, heaven: HEAVEN. 4. Suffixed form *ak-ond- in Germanic *agan6d in Old Norse dgn, chaff: awn. 5. Suffixed lengthened form *dk-ri- in Latin dcer, sharp, bitter: ACERATE, ACRID, ACRIMONY, EAGER}; CAR- VACROL, VINEGAR. 6. Suffixed form *ak-ri-bhwo- in Latin acerbus, bitter, sharp, tart: ACERB; EXACERBATE. 7. Suffixed (stative) form *ak-é- in Latin acére, to be sharp: ACID. 8. Suffixed form *ak-éto- in Latin acétum, vinegar: ACETABULUM, (ACETIC), ACETUM; ESTER. 9. Greek akantha (second element of Mediterranean origin), thorn, thorny plant: ACANTHO-, ACANTHUS; COELACANTH, PYRACANTHA, TRAGACANTH. 10. Suffixed form *ak-md- in Greek akmé, point: ACME, ACNE. 11. Suffixed form *ak-ro- in Greek akros, topmost: ACRO-; (ACROBAT), ACROMION. 12. Variant suffixed form *ok-su- in Greek oxus, sharp, sour: AMPHIOXUS, OXALIS, OXYGEN, OXYURIASIS, PAROXYSM. [Pok. 2. ak- 18, 3. kem- 556.]
276-aks-. Axis. 1. Suffixed form *aks-lo- in Old Norse éxull, axle: AXLE. 2. Suffixed form *aks-i- in: a. Latin axis, axle, pivot: axis; b. Latin diminutive axilla, armpit (< “axis point of the arm and shoulder”): AXILLA. 3. Suf- fixed form *aks-ld- in Latin dla (< *axla), wing, upper arm (see axilla in 2. b. for semantic transition): AISLE, ALA, ALAR, ALARY, ALATE, ALULA; ALIFORM. 4, Suffixed form *aks-on- in Greek ax6n, axis: AKON; MONAXON. [In Pok. ag- 4.]
277-akwa-. Water. 1. Germanic *agwjd becoming *auj6, “thing on the water,” in Old English ig, ieg, island, and
278-al-'
279-igland, iegland (land, land; see lendh-2), island: ISLAND. 2. Latin aqua, water: AQUA, AQUARELLE, AQUARIUM, AQUATIC, AQUI-, EWER, GOUACHE; SEWER!. [Pok. akva 23.
280-al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
---alt
171:Indo-European had a verb “‘to cook” (pekv-, also having the notion “to ripen’’) and an adjective “raw” (om-). Another op- eration is denoted by peis-', “to crush.” Meat (méms-) was an established item of diet, and some sort of sauce or broth is indi- cated by the term yeue- (*yii-s-, JUICE, from Latin). Other household activities included spinning ((s)né-'), weaving, (webh-) and sewing (syd-). The verb wes-* (WEAR) is ancient and everywhere attested. The Indo- European garment was probably belted: y6és-, “to gird.”
268:ai-1, To give, allot. 1. Suffixed form “ai-t-yd in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-td- in Greek diaitan, to decide, lead one’s life: DIET!. [Pok. 3. ai- 10.]
360:[dan-. Low ground. Germanic root. Suffixed form *dan- Jam in: a. Old English denn, lair of a wild beast: DEN; b. possibly Old English Dene (genitive plural Dena), the Danes, and Old Norse Danr, Dane: DANE, DANISH; DANELAW. [In Pok. 2. dhen- 249.]] dap-. To apportion (in exchange). Suffixed form *dap-no- in Latin damnum, damage entailing liability (for repara- tion), harm: DAMAGE, DAMN; CONDEMN, DAMNIFY, IN- DEMNIFY, (INDEMNITY). [In Pok. dd- 175.] de-. Demonstrative stem, base of prepositions and ad- verbs. 1. Germanic *t6 in Old English #6, to: TO, TOO. 2. Perhaps Latin dé, dé-, from: DE-. 3. Latin déterior, worse: DETERIORATE. 4, Latin débilis, weak (see bel-). [Pok. de-, do- 181.] dé-. To bind. Contracted from *deo-. Greek dein, to bind: DESMID; ANADEM, ASYNDETON, DIADEM, PLASMODESMA, (SYNDESMOSIS), SYNDETIC. [Pok. dé- 183.] deigh-. Insect. Possibly in Germanic *tik-6, tikk-6 in Middle English teke, tick: TIck?. [Pok. deigh- 187.] deik-. To show, pronounce solemnly; also in derivatives referring to the directing of words or objects. I. Variant *deig-. 1. O-grade form doig- in: a. Germanic *taikjan, to show, in Old English t&can, to show, instruct: TEACH; b. Germanic *taiknam in (i) Old English tacen, tacn, sign, mark: TOKEN (ii) Old English tdcnian, to signify: BETO- KEN (iti) Gothic taikns, sign: TETCHY (iv) Old French tache, teche, mark, stain: TACHISM. 2. Latin digitus, finger (< “pointer,” “indicator”): picitT. II. Basic form *deik-. 1. O-grade form *doik- possibly in Germanic *taihw6 in Old English ta, tahe, toe: TOE. 2. Basic form *deik- in Latin dicere, to say, tell: DICTATE, DICTION, DICTUM, DITTO, DITTY; ADDICT, BENEDICTION, CONDI- TION, CONTRADICT, EDICT, FATIDIC, (INDICT), INDITE, INTERDICT, JURIDICAL, JURISDICTION, MALEDICT, PRE- DICT, VALEDICTION, VERDICT, VERIDICAL. 3. Zero-grade form *dik-d- in Latin dicdre, to proclaim: ABDICATE, DEDICATE, PREACH, PREDICATE. 4. Agential suffix *-dik- in: a. Latin index, indicator, forefinger (in-, toward; see en): INDEX, INDICATE; b. Latin jiidex (< *yewes-dik-), judge, “one who shows or pronounces the law” (jis, law; see yewes-): JUDGE, JUDICIAL; PREJUDICE; Cc. Latin vindex (first element obscure), claimant, avenger: (VEN- DETTA), VINDICATE; (AVENGE), REVENGE. 5. Greek deik- nunai, to show: DEICTIC; APODICTIC, PARADIGM, POLICY?. 6. Zero-grade form *dik- in Greek dikein, to throw (< “to direct an object”): DIsK. 7. Form *dikd in Greek diké, justice, right, court case: DICAST; EURYDICE, SYNDIC, THEODICY. [Pok. deik- 188.] deiw-. To shine (and in many derivatives, “sky, heaven, god”). I. Noun *deiwos, god. 1. Germanic *Tiwaz in: a. Old English Tiw (genitive Tiwes), god of war and sky: Tiu, (TuEspay); b. Old Norse Tyr, sky god: Tyr. 2. Latin deus, god: DEISM, DEITY, JOSS; ADIEU, DEICIDE, DEIFIC. 3. Latin divus, divine, god: DIVA, DIVINE!, (DI- VINE?). 4. Latin dives, rich (< “fortunate, blessed, di- vine”): Dives. 5. Suffixed zero-grade form *diw-yo-, heavenly, in Latin Didna, moon goddess: DIANA. 6. San- skrit devah, god, and deva-, divine: DEVI; DEODAR, DEVANAGARI. II. Variant *dyeu-, Jove, the name of the god of the bright sky, head of the Indo-European pan- theon. 1. Latin Jovis, Jupiter (> Italian Giove): JovE, JOVIAL. 2. Derivative *jou-il- in Latin Jiilius, “descended from Jupiter” (name of a Roman gens): JULY. 3. Voca- tive compound *dyeu-poter- (*pater-, father; see peater-), “O father Jove,” in Latin Juppiter, Jiipiter, head of the Roman pantheon: JuprTerR. 4. Greek Zeus, Zeus: ZEUS; (Dioscuri). III. Variant *dyé- (< *dyea-) in Latin diés, day (> Late Latin diurnum, day): DIAL, DIARY, DIET?, DISMAL, DIURNAL; ADJOURN, CIRCADIAN, (JOURNAL), (JOURNEY), MERIDIAN, QUOTIDIAN, (POSTMERIDIAN), SOJOURN. IV. Variant *deis- in Greek délos (< *deyalos), clear: PSYCHEDELIC. [Pok. 1. dei- 183.] dek-'. To take, accept. 1. Suffixed (stative) form *dek-é- in Latin decére, to be fitting (< “to be acceptable”):
1425:DIESIS yé- DIET!  ai-1
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
```


## [2026-09-04T18:48:21.229Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls; ls data | head; ls tools | head -40; find . -maxdepth 3 -iname '*.pdf' | head"
}
```


### [2026-09-04T18:48:21.291Z] TOOL RESULT

```
CONTRIBUTING.md
data
docs
EtymologicalDictionary-persian-english.epub
EtymologicalDictionary-persian-english.pdf
README.fa.md
README.md
site
tools
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T18:48:25.449Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; (pdftoppm -f 38 -l 38 -r 170 -png EtymologicalDictionary-persian-english.pdf $S/p38 && ls -la $S/p38*) 2>&1 | tail -5"
}
```


### [2026-09-04T18:48:27.394Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 41973 Sep  4 14:48 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p38-038.png
```


## [2026-09-04T18:48:29.170Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p38-038.png"
}
```


### [2026-09-04T18:48:29.196Z] TOOL RESULT

```

```


## [2026-09-04T18:48:47.450Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT grep ahita ===\"; grep -n -i 'ahita\\|āhita\\|ähita\\|anähita\\|anahita' BRT.txt | head -30\necho \"=== BRT grep ahu (Not) ===\"; grep -n -i 'āhū\\|ähü\\|ahü' BRT.txt | head -20"
}
```


### [2026-09-04T18:48:47.520Z] TOOL RESULT

```
=== BRT grep ahita ===
4458:•  j.  an-ähita-,  p.  *an-ähita-'*  Adj.  (fem. 'tä-)  'woran  kein  Fleck,  kein  Makel  ist, haftet,  makellos':  mihnm  .  .  yim  yazata haemö . .  't^m  'Is  "tili  parü  bartsm^n  °tayst pars  zaohräyat  'talibyS  farS  vayzibyS  Yt. JO.88;  —  tiilrtm  .  .  dßrät  vyavantsm bämtbyS  raoxsnibyi}  'iaäbyJ'^X.S.z;  —  'ta F. 5.  o)  bes.  von  der  Ar>dvT  (sd.): anduya  äpS  'tayh  Ny.  4,0,  Vr.  7.5;  Yt. /.  2i;  ^  sonst  mit  sQra-  Adj,  verb.;  ap?in andvJm  sürqm  Hqm  Y.  Ö5.  i  usw.'';  — aridvt  süra  °ta  Y.ö'5.4  USW.";  —  arpdvl Sure  'te  (VS.)  YL5.18  usw.'\  A)  als weibliche  Gottheit*',  Avamfi*:  D  «*«/'a*- masdä  "atfh'C  (=  anahiti')  Uta  mitriß mäm  pätuv  Am.  4;  Am.  j'.
5476:•  j.  aradvi-  f.  Name  eines  mythischen Flusses *>:  -dvT  nqtna  apa  V.  7.  16;  — bqsnubyS  {^A^  °duya  V.z.aa;  —  °dt^ä lipo  anähilayä  Ny.  *  o,  Vr.  7,5,  YLr.  21; —  sonst  mit  sBrä-  und  anähita-  verbunden; ap3m  'dvTm  sürqm  anähitqm  Y.  65. 1;  — yat .  .  aoi  frazgaraiti  "dvX  süra  anähita Y.  65.4.  A)  meist  als  weibliche  Got^ heit  gedacht*':  upaJacat  'dvJ  sBra  anähita
7573:•  j.  ähita-  Adj.  'befieckt,  verunreinigt': yim    anlan    vastrgm  /rajasät  yim  atttar^
12489:•  j.  daevÖ.kaHita-  Adj.  'von  den  Dasva bewirkt,  veranlasst":  paitiMtSe  *take  i^ai- Saahö  YLy.137.
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
18697:srz.)  wer.."  Y.44.4;  3"*'; — is  urva'iä (sd.)  tpUamai  saraiuHräi  nä  mazdä  Y. 5/.  11;  —  kS  möi  paiSiii  ks  tnS  na  "i^rStä vistd . .  azää  {iA.)  Y.30.  i;  —  ataf  ahmäi .  .  üiä  (Sp.  134  o.)  ankaitl  .  .  yi . .  vandayaita  (sd.)  Y.50.3;  —  a^ yS  rna nä  trtanxlaiti  attyida  (sA)  ttvS  . .  Y.5/. 10;  —  at  yasßm  rtö'it  nä  is^mnS  äyst. (Sp.  150  Q.)  .  .  hs5  .  .  \.46.6;  —  yi  1/ ahmai  ?r?:ux'jä  {%A^  nä  däitl  '^.44.  19; —  aat  yd  na  hli  fräyazaite ..ahmäi .,  Yt 'JSi;  'S,  152;  —  Mä  tfm  urvaijm  .  . fräyavayöis  .  .  aom  nar>m  daitlm  y5  nä . .  frayatät  (sd.)  Yt  /.  24 ;  —  y3  . .  kv5 nä  */rasrBiäyäi  (sA.)  ifTf^Tvö  \ . 4ß.  i y, — /ivö  ma  n  a  sravä  tnörmdat  (sd.)  yS  ,  . Y._^2. 10;  —  a/  hv5  var^Aius  vahyä  (sd.) nä  aibJ.jamyät  yS  ..  Y.^^j.  3;  —  hvS  tat na  ahmai  dasdi(^^.  715  u.)  Y.5/.  19;  — hicä  nä  ßüma  nHaaharatü  hs  aiwyä- xsayatü  Y.5Ä4;  —  yezica  ma  hau  nä ava  snaHita  (sd.)  .  .  aJnavät  P.  2/j  — nai'a  paicaaa  *hau  *«J'^  .  .  isaäa  .  . apasütHt  (sd.)  P.  23;  —  aisS  nä  yS yaoidä'hryS  V.  g.  39,  40,  42,  ip.  31,  Vd. *?,  10,  V.  5.  41,  4.  49  (wo  naröy-,  — h'at  hS  nä  atthuyäite  (sd.)  cvat  hö na  alayäti  hat  ahmäi  naire  miidam aahatyl  .  .  A.4.^i.;  6',  V.Ä81,  p.  39', 44,  Y.Ö2. 1,  Yl/o.  i37£3;  —  yesi^  hö nä  paitiMncSit  yS  nöi}  apivatäite  damaya sva, "wenn einer.,,  der.."  V.^. 47;  —  taEca narSg3rpo5Ji3r3lasca{iA.)..'^.j.7^;  24;  — yasia  mi  aS^m  narpm  .  .paili  utiärayat sva.  "und  wer  ihn  .  ."  V.iS.  10; — paiti- tjm  ahe  nari yavaiea  ..  V.^.ai;  —  ndtt zT  ahmt  paiti  nairi  .  .  rSna  (sd.)  .  .  V. 7.  5»;  —  anätartta  a^byS  nprtbyö  . . yöi  .  .  Yt  13.  30;  —  hauca  *anayä  narä (GD.)  vohu  man3  jäg)r)bustare  arfhat yS ..  V.  4. 48.  B)  Ohne  Attribut  steht 'ein  Mann'  im  Sinn  von  'einer,  Jemand'; insbesondere  hat  der  NS.  na  in  der  Stellung der  Enklitika  häufig  die  Bedeutung  unsres 'raa.ii'-.yB  nar»m  anduIa{zA.)  sna'iajainti V.4.  »6;  18,  ai ;  —  äfs  nanm  jainti  vä V.5.  8;  8f.3;  — yB  *naire"^  aoxte  Jrä im  «Ä  (sd.)  "wer  zu  einem  sagt :  . ."  F. 4A;  —  na  tat  (Sp.  630U.)  paraJri^yeiti V.  5.  i;  a,  5;  —  mit  der  Negation  'nie- mand': nüit  spsJ>3ntS  .  .  nasui  nar?m nsil  *ästarayäti  V.  5.  3,  a)  NS.  na  in
26761:avatghtm  (sd.)  Y.jrf-4;  ^T.  vciwcndel    Ny.       „  ^  AKri-i;  vgl.  »neh  «e»..  mhd.  j^^  'steif. J.  10;  — _y5  ^ijH   ahmäi  västravaitim  stsi       itatüich';  Bthl,  IF.  ii.  ijS. »tTj-J/fSp.  i38so.)  Y.50.2;— ^^"/(f  WT'«Ä/  ,  j    stiptay-  £  Name  eines  Insekts,  das *ustä  *j/»"    "denen  wir  beide  wünschen,   auf    Hunden    sclimaroUt':     duye    navaüi dass    es    ihnen    nach    Wunsch    gehe"    ^.  galwqm  pairi.yaoidaihtta   -tibyasca    ans- 4ß-i6;    —    a/    "i-^J    »tStighi    *J>aourvm  iritib}asca    -.yamiraHbyasca    vUpaäbyasca mazää  *ya^m  (sd)  stSi  Y.31.8;  —  nSil  pairi  aHitaäbyS  ySi  gahwam  pairiiavaiti spmiqm    dSTist  (Sp.  690  a)    ahmäi    stü  "zweimal  neunzig  Hunde  soll  er  von  St. armaitlm   \.4g.2-,  —   Ayat  ..  Bist  (Sp.   reinigen   und  von  An.  und  Vy.   und  von 430  m.)  ..  ahmäi  slH  dqn  ^JA  K/<7yfii/7|  ^11  den  bösesten  (Insekten),  die  auf  Hunden \.4S.io;  —    data  xratius  hixi-3  rai^ltit   schmarotzen"  V. 74.17. (sd.)  stöi  mahyä  räifng  .  .  iähil  ¥.50.6;!      Eig.  Bed.   und   Et.?    —    Pa,:    ddrptkrak, —  tum  tiB  äiraom  *tafftasU'>  "du,  O  A>.,  I      halb  {jap)  twtsskr. sollst  unser  Z.   sein"   Vr.j.7.        a)  im  •  j.   stivant*  in.  EN.   eines  Gläubigen: jAw,    mit    der   Negation,    in    altnbuüveja  /r3dat.vawhfus  •talö  aiaotiS  Yt  IJ.  121. Gebrauch  'der  nicht  existireQ  kann,  den      Ablcit.  mos  'siay-i    Bed.7 es  nicht  geben  kann' ^:  nöil  ma^S  gal^yj   •    j.    siai',    sli'i',    nur   KompA.:    sva. Sil  agjä  (sd.)  sunaiaoiti  gaosaiwe  "es  gibt ;  "stüra-.
28577:—  aridvT  sära  anähita  . ,  hä  Al  mathim nyäsaia  Yt  5-  I37;  65,  Y.  ß'j.  5«,  V.  18. i6,5.48^(?);  — ■   haraifi  bars:   ha  hama
29087:•  j.  *'ha'Ja  Adj.  'immer,  stets':  andv'i sUra  anähita  *A'  *tao'hrS.baräi  andrai yazjmtiili  jailyantai  dd^ris  äyaftfm  ". .  die immer  Glück  gewährt  dem,  der  . ."  Yt.
=== BRT grep ahu (Not) ===
2103:(H)GkASsmann  Wb.:  Wörterbuch  zum  RigVeda.    Leipzig  l!J73. GrBd.  (GBd.  und  GrB.):  Grosses  Bundahün.     Zitirt  nach  den  Mitteilungen  Darmesteteks  (ZA.)
2460:—  afyö  räläbyö  saoirälyö  .  .  yasatrm  io.T^i.;—gunäö ..aitihli gumiay3i{fiA.)\. yazamaiäeY.16. 1 ;  —  shü^  at  paitl  adähü  ^.j,z',~~vät»m  ..atihä  viltay^ /rinnta\i.2. ..büiricä  k>r»hia  xrapaitl (sd.)  ..  Ayat..  g;  —  zugleichauf ein  Relativiim  als  dessen "bei  diesen  Heimzablungea  jetzt  . ."  Y,  1  Korrelat  vorausweisend :  flt^aw^(7»i..(7S'^m 40.1''.  a)  mit  einem  aläMteradea  amanAam  ..ya£/am  tß  ..  irixb/n(sd.)..  V. oder  ergänzenden  Relativ:  ai^/a  at»hsus\^2.'j.  aa)  Der  Begriff  ist  zwar  zuvor yB  astvatS  yasca   asti  manahyö  Y.  57.25;  nicht  ausdrucklich  genannt,  hat  aber  dem
3169:flim  das  AUeischlechteste  und  stinkendste lu  Teil  werden  .  ."  ^.40;  —  mit  Inf.: y>  't)m  *vainariAe  (sd.)  aogidä  gqmcä  .  . hianiä  V.?-'.  10.  a)  bes.  van  an/iav- (sd.);  Aaia  -tat  auhaot  Y.7J.15; — okAus 'lö  V.jo,  4;  —  äi'a  't)m  aüa  ähüm  ä V-53S;  FrW.j.a;  —  -täi  auuhe'^.i,. 61.  A)    in    religiös- moralischem  Sinn:
3188:*J  Gemeint  ist  die  Zerstörung  des  Thebens  und alles  was  daiil  dient:  die  äaimichc  Gegen- achöpRing  [fiailyäta-)  in  dem  «Äunschen  gaya-. Vgl-  Bd.  I.  [ ;  iuadahiimk  i  ehrmazii  u  palyätak i  süräk  mrniii,  was  wesentlich  das  selbe  besagt wie  g'  ajy'.  Ohne  pa'ilyära-  wären  alle  aiiiri- sehen  Wesen  unsterblich.  S.  noch  Bd.  i.  6: kar  S  Hl  amiar  dahün  i  Shrmatd  tanärakömaH,!  u akanätakSmand  ei  en  an  i  andar  har  2än  meniik patmäii  ('Verlrag'}  däii/iid.  —  Pü.  beiiehl  die Stelle  auf  die  Schiffung  und  Tötung  des  Gaya Maritan.
3415:•  j.  a-i9ya}ah-,  a-iS'yeJah- '>  Adj.  'un- gefährdet, der  Gefahr  entrückt,  dem  keine. Gefahr  droht':  nari  yS  i^yajanhal  haca. a»kaol  'jarghim  avi  ahüm  frqfrä  V.  7 5a;     ig.  31;    —    •Janhtm    vacqm    Yt  2
3447:7.  b)  beim  Imp.:  dJidt  at  ruras  .  . aimil.ra/mauis {s^)  Y.40.S;  —  äAü  at paiti  adähü  .  .  mazdqmcä  büiricä  ksnniä ..  Äru/nt^f  (sd.)  Y.40.1.  U)  sonst  (?)=>: ifm  atm  *apl  ae'i-rapaitim  upayat  N,/2 —  ailahmi  paiti  at^  as^ante  YL  i(). 46.  Wertlos:  Vd.<¥,"^/J.  S.  noch  atca, atcit,  at  va,  at  zT.  [P.  27:  lies  aoaoy^ ainaL]
4073:•  j.  a-friÖyant-  Adj.  'nicht  verfaulend, verwesend':  yat  kirmavqn  frahm  ahüm azar}Smi3m  amarihntim  -yantim  apu- yantsm  Yt  79.  11;  —  *°yS  Vyt  45'', F.jh".
4110:•  j.  aDuhi-  f.:  s.  unter  ahü-.
4148:vergänghchc.di.  materielle  Dasein,  Leben': kaaa  ns  iaa  .  .  agatJ  i^yejauhatat  haca °f»haot  ai'kyejanhsm  ahüm  a  V.  7p.  3 1 ; 7.52;  —  hai:a  apajäsö  .  .  i'iyejatuthata^ haca  'fihaot  atiryejanhutäitn  avi  °hü?n H.  2, 16.  2)  mit  a)  manahya-  Adj.  oder manauhs  GS.,  b)  datbitya-  Adj.,  c)  parS.- asna-  Adj.,  d)  ai>y0ah-  oder  ai'hyejakvant-
4170:•  '].,  g.   'aohü-  m.:  S.  unter  ahü-,
4385:•  j.  an-ahü-  Adj.  'der  keinen  Aha  (sd.) hat';  ahmaofanqm  .  ,  °ahunqm  aratunqm Yt.  /^.  I  o  5 ; — *anaKruA3i?)  ">  arafvS  acisifm duzanhavS  "das  Schlimmste  der  Hölle  ist fiir  den,  der  keinen  A.  und  R.  hat"  P.  14.
4393:•  g.  anäi§  ä  adv.-aitige  Verb,  'dadurch, damit,  auf  diese  Weise,  deshalb,  also', zurückweisend:   "näis  ä  manoAtm   ahüm
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
4764:•  j.  a-maräant-*'  Adj.  (fem.  °santT-)  nicht sterbend;  unsterblich':  yat  kirsnavqn  .  . ahüm  .  .  'hnhm  Yt  ig.  ii;  —  yaj  k)T}- naot .  .  *'/an/a  (AD.)  fasu  vlra  Y.p.4;  — bun  ga?SsA  *°sanlii  yä  a^ahe  Vt  /p.  1 2 ;  —
4828:mit  frS^''^  i)  'hervorgehen,  -Ireten': aiiihe  haxayB  fräyente  astva(.»r>take  Yt. ■'5-9SJ  — yü'ia  .,  hvanxsaet^m  tarasca harqtn..fraca  iii/i  aiwica  vazaite  ava^a  . . Yt  /0.118.  2)  'vorwärts,  weiter  gehen': fräyantö  tarö  pilüm  ..yim  cinvats  Vyt. 42.  a)  &oiysX  mA  ß-a^a: /rain /raysiii^ irUtim  uzbaröti  äpö  V.6.2T,  — /ra/a  fra- yaniu  n  maoö  (sA)  Y. /O.  14,  ig;  19;  — /rasa  /raya  (aSIA.)!'  vahisDm  a  ahüm binjayanti  (sd.)  ie  ..  V,  7.52;  —  vgl.  Inf. Jrayäi.  3)  'einhergehen'  iyio? paiti  mit Akk.):  yat  ÖS  paiii  ml  asava  frayaf^  .  . aismssastö  .  .  V.J.  i ;  —  äat  liama  yh paiti  frayat^^  tä paiii, .Yi.  lOjiJ).  4)  'be- gehen', mit  Akk.,  a)  einen  Weg:  kaf  tä pa>ä  (sd.)  Jrayqn^  pasvqm  vil  staorqm va  narqm  vä  Y.S.iy,  ii^23,  3.  15;  — likrava  paoirlm  aHa  pa%ä/rayanlu{s\.3Xl Sing.)  V.  Ä19.  b)  eine  Tat:  (aili  tä ^ao^aa  varsta  , .  fralta^''^  apati(a{&i.) anuzvars/a  . .  V.i^.i.
4841:Beziehung  ist  aus  dem  Zusammenhang  zu  J*«^^'*''  ixivainit  yavaica  yavaäslaica erschliesscn:  yastat  mtzdim  kamna (%A.)\"^^^^  können  sie  nun  und  nunmennehr nsii  däitty}  U  aimii  »niuxiä  (sd.)  «T'pwfe'rt  werden"  V.^.14;  —  yezi  an>hat ditiay.44.iQ,—g3r?zfi  m  a  U  m-ams  »mamU . .  yavamüe  ya  (NSf.)  V.7.75. (sd.)  aAuräY.4'i.  2 i  — na  Tm  vTtpa  a>ri  V.««W>'"-PFP.iumV.^^M.._Pü.:  <y.^=i/i^. tl  mazdänAj.dBm  (sd.)  ^.45.1.  a)vor-l»j.  ay ata- Adj.  (fem.  "AI-)  -  ?  —■.gaatoam ausweisend,  auf  ein  Nomen:  tWii  ts  im  .."^rayam  *iaazdri  iary^ri/a puirä/a  (^.) x/nau/ val/ys (sd.)  ,.  zard^usir^m  Y.^t.'paemainiia  °läca  V.i^.4g. Ii;  — yasta  .  .  tarS.mqsta  yöi  Im  tari.A  P"-  '»■''/'';  ^og  "  "Iso  mm  V.  ay-  (a-ya/a-'.). mainyanta  ..  saofyants  Y.4^.11;  ^0.9  •  j,  a-yapta-  n.:  s.  unter  äyapta-. (ahüm),  45.3  (mahrim);  —  yS  I  (ADm.)  1     KorapA.
5049:deshalb  . .  weil  , .':  -'ha  saoiyqs  yaha vXspim  ahüm  . .  sävayat  Yt  /J.129;  129, 142;"  —  zaya  "^a  staxrS  (sd.)  yal  . . FrW.  5.  2.  3)  zurückweisend,  a)  modal
5833:35.36,41,50.  i4-ii',i2-is,  /5.i7,23, 44,46,50,  j6'.i,5,i4,  /p.27,  c)  atfliav- (sd,,  auch  fdSt):  ahvi  'vaiascä  hyatci maiiatiks  äyapts  (sd.)  Y.  28. 2;  —  paid. . ahyä  arahSus  °vatö  manatthascä  hatk:ySng *•!  Sil/  (sd.)  Y.  4j.  3 ;  —  uvaHbya  nS  aAubya nipayä  . .  ahe'a  anhSus  yS  'vatB yash  asti manahyo  Y.  57,  25;  —  mäca  .  ,  'vatahe^^ anhHis  didnsvg  Pisa  (sd.)  manahim  paiti.- ralxMa  '2.40;  *4o'^;  —  ka>a  .  .  apa- jasg .  .  °vatal  haca  arahaot  manahim  avi ahüm  H.  2. 16;  —  vTspB  anhus  "va  \.s. I  usw.j>;  —  visp>m  ahUm  °rani3m .  .jumta iristfmca  Yt,  13.  9;  *Vd.  <V'*;  usw.3>;  — hascit  atihsus  'vats  F.  -'tf;  *N.  63'^;  usw.J*;
6130:•  j.  *asa-  n.  Name'*  des  mit  asnn  voha vahUttm  astX  beginnenden  Gebets  Y.  27. 14*':  yö  °s3m  staoiti  (sd.)  . .  hö  mam  slaoiti yim  ahunm  mazdqm  H.  i.  3;  7;  —  stäomi a^3m  n3isml  äagvs\t.24.y,  Y. //.  19  und /2. 1 ;  —  sardiiustrahe  .  .  yd  paoiryö  .  . Staat  'Lm  naist  daivS  Yt.  13. 89;  —  yal  nä . .  %ris  "s^n  ufajtuyät  V.  18. 43 ;  —  "hmca *!0  pasca  hü  fräsmSJaitim  (näml  stuyät od.dgl.)  N.  6"^;  imd  so  Öfters.  a)  auch  mit a)  vanhav-'h  aiwi^r^lmahi  's>m  voAa  Vr. J7. 1.  ß)  vaAista-'^:  ahun^mca  vairitn  .  . °s?m(a  vahUtim . .yeAhl.tiätqmca\.6i.\\i3. 8,'Hyuf.S;—jainii  mqm  ahuna  vairya  ..lapa- yäti  mqm  'la  vakUta  Yt/7. 20;  —  6ayqm 'iahe  vahistake  yazatnatde  'sähe  vahÜtahe yasamaide  frasraeimmca  .  .  Y.  20.  5;  — zara^uitrS  ys  paoiryö  .  .  staota  °sfm  ya^
6292:—  yastttm  hapta»h3itim  'lavarum  Y.41. 8,Yr.l6.o,  21.0; — yasnaheca  hapta»hä- tais  .  .  vir)%rayne  'faene  (statt  GS.)  Vr. 75.2;  I,  5;  —  ahBtrim  frasn>m  'i'ava- mm  .  .  ahüiflm  tkalsim  -savansm  Y.  yi. 1 2.        II)  'dem  das  (höchste)  Anrecht  zu-
```


## [2026-09-04T18:48:54.820Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'ähita-  Adj.' in l or 'an-ähita-' in l:\n        print('LEAF',i, repr(l[:200]))\nEOF"
}
```


### [2026-09-04T18:48:56.555Z] TOOL RESULT

```
LEAF 104 "ya'ia  kava  syJ- FarsänS  Az._j,\n1)  Var.  anähisüri^wamnt.\n•  j.  an-ä'zar^ta-  Adj.  (fem.  °ta-)  'nicht enilmt':  ytzi  sl  bavaitUi  °ta  xsnütä  ainilä al/nsia  .  .  fravasayi  Yt/^.63;  30,  "
LEAF 219 "i- iaslaii,  (lu  Y.  6S)\\  apar  an  i  amäk  yaxiSn iiiSliü,  erl.:  fföS  däi-e;  s.  noch  No.  8.  — »  S  '4^-  —  '>  Doch  s.  No.  3.  —  J)  NA.  'inli (aber  •fnti  tu  Vt.  //.  1 1).  —  "
```


## [2026-09-04T18:49:04.796Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in range(214,226):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', leaves[i])\n    print('LEAF',i,'nums',nums[:6],'|', leaves[i][:120].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T18:49:06.814Z] TOOL RESULT

```
LEAF 214 nums ['337'] |  z)  sonst:  °leis  .mazdascü  ühuräi^hs  asicn  "maifi  Y.  j/. kasctt  asa  AuzSntus{?.d.)  Y.  4^.  5 ;  —  Aahil  \ 
LEAF 215 nums ['339', '340'] | �  präklanah, •  j.  ärmaitiä.hak-  Adj.  'der  Arm.  an- h^gend,  ergeben':  mmS  . .  asis.hiig>t 'kägit  (NSn.)  Y.5^
LEAF 216 nums ['342'] | (sd.)  carärii  kacä  xlmat  *'-slai(im ''  xhna- kam  hyatiä  . .  "mein  Ziel  .  . :  das  Sich- anschliessen an  euc
LEAF 217 nums ['344'] | anter  'had-. •  j.  ä-snatar-,  ä-snäftr-  m.  Bezeich- nung des  fUnften  mit  der  Waschung  und Filterung  des  Haom
LEAF 218 nums ['345', '346'] | bigen:  'Iahe karsnayanahe  asaonB  Yt/J,  108.  I Vgl.  'äzäla:  —  Wie  das  entsprechende  np. äzäd  wohl  Kuriname; 
LEAF 219 nums [] | i- iaslaii,  (lu  Y.  6S)\  apar  an  i  amäk  yaxiSn iiiSliü,  erl.:  fföS  däi-e;  s.  noch  No.  8.  — »  S  '4^-  — 
LEAF 220 nums [] |  vgl. äsiiriya-  Adj.  —  PQ.:  j^atäi.  —  ■)  D.i.  '»70, S  26*.  3ä- •  j.  'ähüirya-  (Adj.  'vom  Machthaber, Fürs
LEAF 221 nums [] |  verscheuchen,  weil  sie  des guten  Sinns  ermangeln,  sie  deren  Tun  Übel ist"  Y.^4-9- Zum  V.  'vaed:  —  ai,  iv
LEAF 222 nums ['351'] | anam  .  . dby  Google 351 *ar»dvaya ■»«zav- 35« ,  denen  . "wäca  kiniwäca  "M.   ist  aller  J/aaÄi- i  würdig  erkan
LEAF 223 nums ['353'] | aiiti  ",  ,   zu   den  geraden   Wegen   zu dby  Google 353 "arazav- Asa  hin,  bei  denen  MAA.  wohnt"  Y.jj. 5.  a)
LEAF 224 nums ['355'] | .  arazvan-  Adj.  'gerade  gerichtet'  sva, 'die  Richtung  einhaltend,  nicht  abirrend, ohne  Fehl':  ta  ns  data  l
LEAF 225 nums ['357'] | asivä (sd.)  (isla  Y.j/.s", Pü.:  Tüsl  ml,  Sü.:  salyena  ladauruh.^  ■)  Vgl. •  j.  araz-UxÄa-  Adj.:  s.  unter  a
```


## [2026-09-04T18:49:12.310Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nfor i in (218,219,220):\n    print('======== LEAF',i)\n    print(leaves[i])\nEOF"
}
```


### [2026-09-04T18:49:14.427Z] TOOL RESULT

```
======== LEAF 218
bigen:  'Iahe karsnayanahe  asaonB  Yt/J,  108.  I
Vgl.  'äzäla:  —  Wie  das  entsprechende  np. äzäd  wohl  Kuriname;   vgl.  Justi  NB.  53  äff.
j.,  ß.  ä«  V.  31.  18,  N.  6/:  lies  ä  :<;  s.  ä No.  18.
j.  ä%iiqlh'aili!  F.  je:  lies  äzanliv'.
•  j.,  g.  ä-zutay-  f.''  'Fett,  Schmalz':  raoy- nyqtn  i'aranhim  "suitlmca  urvaranqm  Yt. /2.3.  a)  überhaupt  sva.  'feste  Ndirung' gegenüber  der  flüssigen,  im  Gegensatz  zu ' xsi'td-  'Milch' :  pars  xsvisät  (sd.)  -zaitUca  "  1 girii mal  V.  13. z8;  — xhioaica  'sBlayaEca  ■> ^.68.2;  —  t!m  'iSdiis'''  ahurB  mq%r)m tasal  .  .  mazdä  gavei  xhildimcil  *ki'B.- umiaHbys  spmt3  säsnayä  "das  Wort  vom Fett  hat  AhM. ..  für  das  Rind  geschaffen und  die  Milch  für  die  Nahrung  begehren- den durch  sein  Gebot,  der  heilige"  Y. 29.71'.  a)  Du.  in  Verbindung  mit  xhild- Du.:  xsviöa  'zütH  yazamaide  .  .  ilzSis  .  . hamsistri  \.i6.8.  2)  'Üppigkeit,  strotzende Kraft  und  Fülle':  vaKuAlm  'zBülm*^  . . frasasttm  .  .   *p3r»ndlm  yazamaidl  Y.jS.
a.  a)  bes.  neben  Isä-  (sd.):  aj  Äv5 mazda  tzäcä  "zBitisca  yS  . .  *särjs/a  (sd.) "der,  o  M.,  -  Glück  und  Fülle  (wird  ihm), wer.."  ¥.415.5*';  —  P^ra  ..  ahmst  haca Oianhatca . .  axstat . .  iiäca  'sUitUla .  .frada- %>inca  var3da>:?mca  vaxsaifmca..V.g.^3.
KompA.  —  Zum  ai.  V.JaM/i.  —  ai.  ähuiay-  {.
*Gegensland  der  Opferspende'.    —   Pü. :  lar-
pih,  Sü.  (lu  Y.  Tfi):  ?ot/B*,  (iu  Y.  4^)-.  ma- hallatnatvam;  s.  noch  No.  1  ff.  —  ')  Fb.:  s. isvid-  No.  I.  —  ')  Pü.;  atazüniilh,  Sü. ;  ma- hattamaWam;  s.  No.  4,  —  »  Dh.  es  ist  alles göttliches  Oebot,  dass  das  Kind  mil  seinem t'elt  (Fleisch)  und  seiner  Milch  dem  Menschen zur  Nahrung  dienen  solle,  äzülöii  mq%rjm weist  darauf  als  auf  etwas  Bekanntes  hin. Pü. :  an  i  laaaünJkih  pa  mäusr  öhtmazd  *ö  *di täiitir  . .,  erl. :  an  mizä'i)  i  hac  mänsr  fdiläi  d ei  dahcnd;  s.  da*u  No.  5.  Vgl.  iSt.  Bthl. AF.  3.  53,  Gani  anders  JuSTl  PiJ.  SS.jg.— 4)  Pü.:  (iwzilitiMfA);  Sü.:  r^-ddÜA;  s.  No.  a. — i)  Der  Sali  ist  anakoluth;  Pü.erL:  hii  m/:d7i dakrnd;  s.  No.  3.  —  *J  l'üErt.  bezieht  die Stelle  also  auf  die  letzten  Dinge;  s.  No.  7.  ~ n  S.  No.  6.     Hier  richtig.
•  j.  äzuitLdä-  Adj.  '(Fett  sva.)  Üppig- keit, strotzende  Kraft  und  Fülle  schenkend': mi^rfiH  .  .  yff  °dä  yü  vai;wC.dii  Yt.  w.  65.
j,  ahmäi  äsySnim  Y. /3.  l;  lies  a' ä  zyänim (sd.).
•  g.  Eiav-  DO.  'Streben,  Eifer',  spez.  in Glaubetissachen :  yavat  'his*zrazdUtS  banöi haxtaya  (sd.)  "sofern  der  gläubigste  Eifer (euch)  in  Fleisch  und  Blut  (sitzt)"  Y.55.7.
Aus  ar.  *äilkaii-,  lum  V.  äs-;  Bthl.  "iF,  j. 215.  —  Pü.  (nach  DST.):  ka  e  iiii.tkt)  rau:^/ pa  bau  i  haxi  i  ian  i  "wenn  der  Igel  geht in  den  Grund  der  Schamteilfc  einer  Frau";  s. dazu  DsT.  ZA.  /.  347,  3.  195.  Die  PLiF.rl.  ist mit  ebenso  an  verständlich  wie  diese  selbst, Ton  der  nur  so  viel  deutlich  ist,  dass  sie  die Strophe  aufUniucht  vonWeibern  bezieht. — 0  SP.  hat:  amtainik.  V^l.  West  zu  Dk. g.  17.  S,  der  auch  anf  Av,  yo,  3  vervreisl.
•  g.  äidyäi  Inf.  'hin  zu  gelangen  zu  — ,  zu erlangen':  yqm..iiy<im  (sd.)  dtilü  ..mazd.'i ahurö  asahyä  ä'  gtnzdlm  ".  .  zum  Besitz des  A/a  zu  gelangen"  Y.5/.17.
Zum  (?J-Aor.  des)  V.  qi-  mil  a.  —  Pu,:  /yi pilixiäkih  i  öhitnazd  u  äii  i  ahrätlh  arziii .:;iräl.  erl.  kalakbänükik  "durch  die  Herrschaft des  V.  und  des  A.  soll  Me  den  Preis  empfangen (die  Hausherrinschaft)".
•  j.  'äh-  V.  'sitzen':  Praes.  i  ah-,  21 ,7/sha-''>.        Inf.  iiste.
Nur  Med."*  i)  'sitzen':  iisfe  F.  7;  — *Äist?mnö  vcl  anhand  va  "stehend  oder sitzend"  N.J7;  — frataire  gätvs  st^ha- nqm  fratarSJairt  (sd.)  gati'd  niiäoaysis H.  2. 14;  —  yaihe  .  .  vispähu  paiti  ban- zähu  . .  spasff  auhäire  (3PPM  )'>  mvirahe Yt.  io. 45 ;  —  a2sqm  vatitn»ha  ..  gatui paiti  *ar»h^nte*  <'  "ihre  Frauen  sitzen  auf dem  Lager  Yt/7. 10.  a)  'da  sitzen': aisqm  kaininS  Stfhinle''^  qymfipaiois(ad.).. YLiy.ii.        z)  mit  a)  Mj.  oder  b)  Absol.
dby  Google
345
'ih-
'ahüirya-
346
'in  einem  (dadurch  bezeichneten)  Tun  oder Verhalten  dauernd  beharren'*':  a)  ysi  ,  . nasks.frasauhS  (sd.)  auh^nle  'W.g.z2;  — tasät  ya  kaitiinS  ätakaire  (3PPM.)"  dan- y^m  ayrvd  "die  als  Mädchen  lang  unver- heiratet geblieben  sind"  Y.*j.  23''.  b)  s. Inf.  Undeutlich:  dr^fya  paiti  zharahe
ahuräi  masdäi  .  .  ätakanö  V./p.ii".
mit  uPa  'beachten,  (Bitte)  erfüllen'; surunuyä  nS  yasmm  . .  xsnuyä  ns  yasn>m .  .  upa  nS  yasrum  ahlsä  (2SOM-)  "hör auf  unser  Gebet  . .;  lass  dir  unser  Gebet gefaUen,  erfüll  unser  Gebet"  Y.ö'Äg;  Yt. /o.jz  (wo  ahiia^.
aL  äsli',  mp.  ähislani^,  s.  No.  S).  —  FB.:  n
======== LEAF 219
i- iaslaii,  (lu  Y.  6S)\  apar  an  i  amäk  yaxiSn iiiSliü,  erl.:  fföS  däi-e;  s.  noch  No.  8.  — »  S  '4^-  —  '>  Doch  s.  No.  3.  —  J)  NA.  'inli (aber  •fnti  tu  Vt.  //.  1 1).  —  «)  Theni.  —  5)  Vgl. Dbr.  AiS.  391  und  unter  'iad-  mit  tit,  itiaex ■fl*-  I  5,  —  6)  5  i2ii.  _  7)  Vgl.  noch  ifl*- No.  3.  —  8)  PQ. ;  ßa  draj  i  tbSr  Su  Shrmazd  . . äAii/  (in  Aw.-Buchst)  ifiiJ.
•  j,  Ih-  V.  'empfangen'.  Praes.  5  isäA- äiaurunS  hs  rätanqm   raoxsni.xsRüUni
isiiihoila'''  aikaurunö  hs  räianqm pouru.- xsttOtim  isanhaita"''  "Gaben  des  Priesters würde  er  als  glänzende  Eelohnung  em- pfangen . ."  Yt/fj-SJ.
Et?  —  ')  iF.  S  J"b.  —  ')  Them.
•  j.,  g.  ^äh-,  g.  S»äh-"  n,  'Mund':  tal  nS maiuia  , .  vaocil  hisvä  (sd.)  'hwahyä  üfthö y-J'-3>  —  ahurä  . .  frS  ntä  sTsä  *vao- catihg .  .%WiJ  JjäuAä'i  Y.2S.11;  —  ä/jia (IS.)  F.jd.         [P.2S:  lies  «^wÄa.l
Vgl.  iahan-.  —  al  dj-  n.  (nur  äid  IS.  und äidi  CS.)a).  —    Pü,:    dahäti.    —    ■)  zSchr.  s.
S  36S.  6.  —  'i  Wie  im  Aw.
•  g.  ä.höi^i  Inf.  'zu  unterdrücken':  aiyS (nämL  mq'^ränS)  *grShms  a.h'  nl  käva- yascU  xratüsnl  dadat  *var»cäkiclt  fraidiva "auf  dessen  (des  Propheten)  Unterdrückung richten  Gr.  und  die  Kavay  ihre  Absichten und  Kräfte  schon  lange"  Y.J2.14.
Zum  V,  ha{j)-,  Gdn.  KZ.  3/.  236,  BTHt.  AF.
2.  107,  —  Pü,;  Ä  le  pa  grahmak  maslh  (Sil.: mahath-am),    daher   DsT.  ZA.  i.  241:    "celui qni  vend  le  pouvoir  pour  l'nrgent". äki  aniilrilim  N.  lo:  lies  ä  ht  anisriam.
•  j.  ähita-  Adj.  'befieckt,  verunreinigt': yim    anlan    vastrgm  /rajasät  yim  atttar^
"tim  räntm  frajasat  (sd.)  V.  t6. 1 6. KompE.  —  PPfP.,  idg.  ».[»«äv  (oder  'ila-  m einer  Basis  'ai'Y'i-  —  Vgl.  TD.-f.3hok,  np.  äkö 'Sünde'.  — Pü.:  fehlt;  vgl.  lu  anäh'.  —  ')  S. ! zn  anäkita-  No.  3.
I  •  j.  Shitay-  f  'Befleckung,  Veninreinigung, j  Makel':  p>r>tte  'lim  ya  äili  ätrfni  apftn zqm  gqm  urvarä  V.  //.  9 ;  —  nSit  aotS  välH I  nsit  ganmS  rWit  axtü  . .  nöit  'tti  dafvB.- data  Yt  10. 50;  —  nasyäti . .  akmal  haca I  nmäiiät  'ti!  Y.  ro.  7 ;  —  csat . .  a^a  druxs \y:l    nasuf  axiUa  *pavitiea  °tiia  /räsnaoili V.  5. 2  7 ;  —  paiiiitätSe  ayaiyh  püifyä  'fya (GS.)  ya  artrS  matnyui/rakfrmtai  V.  20. 3. Vgl.  ähila-  imd  anähila-  No.  3.  —   Pü. ;   ähö- kenün,    erl.   (lU  V.  j):    aiSrih,    (lu    V.  //): awzärif);  (lu  V.  20):  Shokemiär  (Adj.!). g.  dhiiäyä:  s.  hä{yy. ].  ähilä  P.  26:  lies  äxUi. j.  Shu  N.  4S:  lies  ä  Aü;  s.  ä  No.  6.
•  p.  *äNitiyära-''  m,  Name  einer  Land- schaft in  Armenien:  */-«*  tiämä"  dahyäuS arminaiy  Bh.  2, 11.
<)  Sonst  oMtiy*  gelesen.  So  wie  oben  klingt mir  der  Name  wahrscheinlicher.  Eü.  ist  nicht entscheidend.
•  j.  ätiQray-  Adj.  (auch  fem.)  'aÄ«Hsch, mit  Ah.  in  Beziehung  stehend,  von  ihm stammend,  ihm  zugetan':  °hüiril framS.. "Aüiris  tiaiiö  "die  an  Ah.  gerichtete  Frage .  .  die  von  AA.  erteilte  Belehrung"  Y.  j". 24;  6o.y,  —  'Aßiri/n  fraSn3m  . .  'hüirlm ikal^tm  Vr.  2.  ii,  Y.  71.  12;  h.  3.  12;  — "hurSisfralnahe  'huröis Ikai^ahe^z.!.^;  — vßfanqmca  allqm  zardkuStnm  . .  °häirim *susruma  tkagsptn  ".  .  den  ^^«nschen Lehrer"  sva.  "den  Lehrer  des  aA.  Glaubens" Yt.f^.  148;  —  dainqm  mazdayasnlm  . .  yä 'hüirilX.  12. 9,  iV.  7 ;  —  imqm  daenqm  yqm 'AsirTm    zarakuitrim  Yt.^'.S9;  V.2.1,  2;
—  airihä  dainayi  yat  'hurdil  Y.60.2; *Yty.99";  —  dähyumahe  "hurSÜ  Yx.t. 9;  —  upa  imal  nmätum  yat  'hüiii  Y. 10. i\  —  uiti  *asH.ga/yS  'AüirisYt  /j.  2S.
Ableit.  aus  <aAura-[mitf^Jä/iii);\e[.'äAi7irj-a- und  vor  %  /pj,  —  ai.  asui-ay-  m.  EN,  —  I'ii. : {all)  i  ehi-mazd.  —  ■)  NA.  oh;  Wo.  Ji°,  beide ohne  Varianten  angäbe,
•  j,  'ähüirya-  Adj.  'aAurisch,  mit  AA.  in Beziehung  stehend,  von  AA.  stammend,  zu AA.  gehörig':  tf«  aj  ya  (IS.)  nUmJm mazda.vara  (sd.)    .  .  yasamatde  Y.^".  3;
—  von  VtStäspa:  vTstalpaAe  .  .  °yehe  Yt '3-99>  ^^'ö;  —  sonst , von  Göttern:  atn^- iiinqm  sp?ntanqm  .  .  'yaiiqm  Y.  26.3;  — sraosaAe  asyehe  .  .  "yehe  .  .  yasataAe  V, _j.  20 ;  4. 23,  V.  18. 1 4,  S.  1. 1 7-  A)  Plur. ntr.  'die  öÄwHschen  Räume,  die  Räume,
dby  Google
347  ^huirya-  —
da  Ah.  wohnf:  äk&im  (sd.)  •«'>  (AP.); .  .  jas>ntam  Y.  60. 1 1.
Ableit.  (mit  Vj-dii/ai)  aus'DAHra-;  ■<ij^.  äkuray-
und  vor  S  '95'  —  Vgl.  ^äküirya:  —  ai. 
======== LEAF 220
 vgl.
äsiiriya-  Adj.  —  PQ.:  j^atäi.  —  ■)  D.i.  '»70,
S  26*.  3ä-
•  j.  'ähüirya-  (Adj.  'vom  Machthaber, Fürsten  abstammend' als)  m. 'Fürstensohn'; ahura^hs  .  .  'yänks  "die  Fürsten  .  .  die Fürstensöhne"  Yl.  74.39.
AbleiL    (mit    Vrddhih)    aus    ^abura-,    -    Vgl. tä/iüirya-.   —  Npfi. :  unklar.
•  j.  ahvah-  :  ai>hus-  Adj.,  PPfA.:  s.  '^ah-. Vgl.  akvah'.
s.  S  1
11  hindav-  No.  1 ;  doch  vgl.
3,   %.
•  ].,  g.  >',  g.  5",  nur  KompA.:  s.  unter  '(t°.
g.  '  V._29.  6i  s.  .n..
•  g.  Saädü-  f.:  s.  unter  üi)£-.
•  j.  39änQ  Praev.:  s.  unter  anu.
•  g.  39ävä  AD.  Pron.  i.  Pers.  'uns  beide'; kost!  voha  manav/ia  p  I  dayat  (sd.)  °vü maritalibyS  Y.sq.j.         S.  zu  vayam.
D.  i.  ä!;l,  s.  iSchr.  S  26S.  6.  —  ai.  vgl,  ,h'd/i. AD.  —  Pü.:  -/fl*J«>).  —  '}  Wie  für  JjJwÄi (e.  3äA-)  und  »Jwr/.  Für  Fü.  war  also  Pi  der Träger  der  Cedeutung.
g.  iiSuhi  V.  i8.   11:  S.  'ik;
g.  ittäiUä:  s.  »«lu-.
•  g.  Jtiitay-  f.:  s.  unter  /«/ay-.
•  g.  äma'vant- Adj,  (fem.  "iia/Vr-):  s.  unter amavanl:
•  j.  spastinis  varamis  sispimnö  f»9mnÖ paoiris  iiöiyti'^  Yt. /^.ö?.  Vom  verstUm- j meltes  PPM.  in  der  Bedeutung  'veran- ' lassend',  NSm.  ,
•  j.  a-varazika-"  Adj.  (fem.  °zikii-)  'nicht wirkend,  faul':  druxi  ojfä^re  'ke  (VSf.) ' V.  /*.3o.  I
Zum  V.  ivifj;..  —  Pü.:  avirzü«,  etl.:  '"'^  i frärSii  ni  Titr~J.  —  ■)  Oder  auch  'zaka- ;  s. Wh.  Gr."  S  ^'^'S'J'  c-
•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
Fa.;  az'srülSr.    —    i)  Statt  'üi-h'  für  «ij
j.  *9-vito.xra'8iy-'*:  °of-  Adj.  'des  Ein- sicht untüchtig  ist':  *janyöii  .  .  mairyaya ''iayd'>  (GSf.)  Y.mis- *v'i-iaxra.  (%  268.  57)  Adj. ;  iBed.  und  El,  s. /axma-.i)  —  Pü.:  fehlt;  Sü.i  paribbraflabiid- dhik.  —  I)  So  K  5  b,  J  a;  KA.  'j:arA'.  — a)  S  sfiiK  11  b.  —  3)  Oder  darf  man  an  mp. laxr,  np.  lalx  'bitter'  denken?
•  j.  a-viSvah-,  g.  a-vidvah-  Adj.  i)iAw. mit  Akk.  'etwas  nicht  kennend,  womit unbekannt':  yam  asava  .  ,  alayqm  (sd.) vai'ia  tarn  ärrä  'ovä  Vr.22.2.  z)  gAw. absoL  'nichtwissend'  sva.  'nicht  im  Besitz des  wahren  Wissens,  in  die  rechte  Lehre  . nicht  eingeweiht':  mi^akvaia  vä  ^»ns.vam (sd.)  vs  vidva  vä  'dvh  va  ". .  ein  wissen- der oder  auch  ein  nichtwissender"  Y.^JJ. 12;  —  vTdvä  vJduil  mraolB  mä  'dva  *aipj.- dsbävayai  (sd.)  Y._j7. 17.
Pü. .  anäkäs ;  zu  Y.  _J/.  1 2  erl. :  ziitäk  mcniii.
•  j.  a-vindan-  Adj.  'nichts  erlangend, bekommend':  späns  ydi  hisimie  ai^arO upa  !^'ar>ttt>m  *tarS  spasUnS  *dättS  "die Hunde,  die  ohne  Essen  beim  Essenden stehen,  von  der  Seite  drauf  hinspähend, aber  nichts  abbekommend"  V.  y,28.
«was  Schlechtes'.
•  j.  »-vis-  Adj.  'der  kein  Hauswesen  hat'; vUäne  akm^i  (näml.  pourum  framraomi) ya%a  'säi''>  "dem  der  ein  Hauswesen  hat, (spreche  ich  einen  höheren  Wert  zu)  als dem,  derkeines  hat"V.4.47.  \?visaiusi'a N.  s6:  lies  pvistaist'a.]
Pü,:  az-s.  —  ">  Them.
•  j.  s-vissmna-  Adj.  'sich  weigernd'  (etwas zu  tun):  *vTsaiU  (sÄ)  anyB  "usyö  (sd.)  nsil ainyS  'nS  *astryeiH  P-57.
PPM,  lum  V.  vaes:  —  Pü.:  afa/IriiriTA.
•  j.  *»-vista-'*  Adj.  'nicht  erhalten,  em- pfangen'; nur  LP.  'so  dass  man  nichts (dafür)  erhält'  sva.  'ohne  En^elt':  _^iwr.7- TayS  ava  däirayim  dim  vaeniil*°tash'a^'> vindatum  nSil  *afayiJ  *vistarh'a  "wenn  er nur  eine  solche  (so  geringe)  Besoldung dafür  bewilligt,  dass  man  ihn  für  einen, der  olme  Entgelt  (Unterricht)  erhält,  an- sieht, nicht  eine  solche,  dass  es  gegen Entgelt  (zu  geschehen  scheint)"  Ü.iO.
Pü-:  /«/  <ti  i  sräyil  an  i  däsi   {ia)  äH  i  mizd
tindisii   däiiel  iv  yut  hac  aiizd  *man  fäU  mä
i      aad  ia   p.iliak    häl   ta    dAnft  kam   h.if   mizd
I      last.    —    Es   handelt  sich  um  die  Frage,   ob
Uiflitized  byVj 00^ IC
«vistay-
•  g.  5-vistay-  f.  'Nichtteilhafltgsein':  yot .  .  ilrmaiirni  .  .  b?nxAam  (sd.)  .  .  duLfyag- ianä  avazatai  varghSuS'tt  mana»hS"6S.t die  ■  ■  Arm. , .
```


## [2026-09-04T18:49:48.697Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT anahita ===\"; grep -n -i 'anahita\\|Anāhita\\|anahit' KNT.txt | head -20\necho; echo \"=== KNT leaf 182 (p.167) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==183' KNT.txt | head -50"
}
```


### [2026-09-04T18:49:50.373Z] TOOL RESULT

```
=== KNT anahita ===
539:and its forms, and in its ethnic Ау = Hi?- duya; and once in anh? = Anahita A'Sd 3f. Occasionally there are writings with Ауе for -hiy- in words which are normally written ћу: such are:
4987:Andhita- sb. ‘Anahita, Anaitis’, a goddess: Elam. a-na-hi-ud-da, Akk. a-na-ah-t-tu-’, Gk. ’Avairs; Av. andhitd-. Cpd. of neg. an- + pte. pass. dhita- ‘spotted, defiled’, of uncertain connec- tions (§67.J, §118.V, §242.1): ‘The Spotless’. The OP writings, being late, fail to show length of б in either position. Anahita (827, $52.11) nsf. A’Sd 3f; Anah*ta, A’Sa 4 (as gen., §313.11), 4f; A?Ha 5° (as gen.), б.

=== KNT leaf 182 (p.167) ===
he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Persian noblemen who co- operated with Darius in slaying Gaumata the false Smerdis, are given in Behistan §68 and in Herodotus 3.70; there is agreement in the names of the first five:
Behistan Herodotus Vi"dafarnd son of Vayaspdra —— Intaphernes {Дата son of 8uxra Otanes son of
Pharnaspes
Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
Herodotus, it will be seen, differs from the Behistan account in the name of the father of
Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
The Behistan inscription mentions Vidarna again in §25, as defeating one of Phraortes’ armies in Media; Vi"dafarna in $50, as defeating the rebels at Babylon; Gaubaruva in $71, as crushing the last revolt of the Elamites.
IV. Tug Persian CALENDAR AND Benistan I-IV
In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
calendar, and in the other calendars, was by no means certain. Now, however, with evidence from additional Akkadian and Elamite tablets which have no Old Persian version, Arno Poebel has suc-
ceeded in reconstructing the lists of months, as
follows:!
! AJSLL 55.139-42. The Persian calendar has been the subject of many studies, but Poebel’s studies have sup- planted them all: ALSLL 55.130-65, 285-314, 56.121-45. Cf. also Hinz, ZDMG 96.326-31;
TEXTSIWITH NOTES AND TRANSLATION
Old Persian Elamite Akkadian Equivalent
1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
The narrative of the revolts, however, is not given in temporal sequence in Columns Т-Ш, but rather in а geographical order conditioned by the order in which the rebellious provinces are named in $22: Persia, Elam, Media, Assyria, Egypt, Parthia, Margiana, Sattagydia, Seythia. If we should reduce the story to a more easily intelligible pattern, it would be аз follows:
After Cambyses, son of Cyrus the Great, secretly slew his full-brother Smerdis and went on the expedition to conquer Egypt, uprisings against his rule took place in Persia and in Media and elsewhere (810). Notably a Magian named Gaumata led the revolt, claiming to be Smerdis, whose death was known to but few; he started his revolt on XII 14 of 528/2, and received the adherence of the entire Empire, becoming King on IV 9 of 522/1? Cambyses died by his own hand, either intentionally or accidentally, in Egypt soon after hearing of Gaumata’s revolt, (§11).
Three months later Darius and his associates killed Gaumata and his ehief followers at Sikayau- vati in Media, on VII 10 of 522/1. Thereby Darius
2 The months will be indicated by Roman numerals.
161
became King, but at the very outset his rule was contested by Agina in Elam, and by Nidintu-Bel (claiming to be Nebuchadrezzar son of Nabonidus) in Babylon, who were recognized as King each in his locality. But Аспа did not last long; Darius, after organizing the gove
```


## [2026-09-04T18:49:55.389Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\ndata=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\ntgt=None\nfor i,l in enumerate(leaves):\n    if 'Andhita- sb.' in l or 'Anahita, Anaitis' in l:\n        tgt=i; print('LEAF',i)\n        nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', l)\n        print('page nums on leaf:',nums)\n        print(l[:1500])\nEOF"
}
```


### [2026-09-04T18:49:57.664Z] TOOL RESULT

```
LEAF 189
page nums on leaf: ['167', '168']
n., asn.); AÁuramazdü, АМ; ava (nsn.); avdkaram, avükaramca-; ucdram; uld, uta-; tya (nsn., asn.); dahydus; duvarayd; nat-; pati-; pasdva; уава; haw, hau-: Asl 12; DB 1.25 bis, 55, 87, 94; 2.24, 34, 40, 45, 54, 60, 68, 75, 79, 86, 90, 96; 3.6, 11, 17, 37, 441, 61, G6f, 87; 4.39, 46, 60, 64; DPd 28°; DPh 8, 10; DNa 50 (m° omitted, $52.VI), 52#, 544; DNb 13, 28, 28f, 31, 32f, 33, 48, 51, 52; DSe 51°, 52°; DSE 10, 19°, 20°, 58; Ds} 4°, 6°; DSk 5; DSI 4f; DSm 3°; D8s 7°; DSt 9°; DH 6, 8; Хра 15, 18f, 191; XPb 24, 29, 30; XPe 13 bis; ХРа 18f, 19; ХР 32, 38, 41, 45f, 47; XPg 14; XPh 32, 45, 58,
167
60; Хе 5° bis; XV 261°, 27°; A!Pa 23°, 24°: A’Sdb 4 (-may de, $52. VT); А?Не 20 bis.
-ma gsm. for -maty ($198.11); apan*yáka-ma А?За 3; [n"yà |kama for n*yàkam-ma (5130) A’Sa 4. Not kamna-ma DB 2.19, as taken by Tolman.
-ma absm. enel. (Av. maf, Skt. mat, pIE *med, $193.IV; orthotone pIE *méd in oLt. méd, elLt. mē); only in hacd-ma DB 1.19, 23; 2.6, 12°, 16, 98; 3.27, 78, 81; 4.92; DPe 9; DNa 20; DSe 19°; XPh 18. Not duviliya-ma DB 3.24 (with Bthl.); not apara-ma DB 4.37, 68, 87 (with Bthl.), nor DSt 10°.
vayam npm. (Av. vaém, Skt. vaydm, рї Е *uei + pAr. -am, cf. Gt. wei-s; §193.V) DB 1.7, 10°; DBa 10, 17.
amazam gpm. (Ау. ahmakem, Skt. asmákam; $118.11, §193.VI) DB 1.8, 28, 45, 49, 61, 69, 71; DBa 12.
Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. o
```


## [2026-09-04T18:50:05.684Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nprint('nleaves',len(leaves))\nfor i in range(275,292):\n    l=leaves[i]\n    print('==== LEAF',i, 'len',len(l))\n    print(l[:900])\nEOF"
}
```


### [2026-09-04T18:50:07.822Z] TOOL RESULT

```
nleaves 777
==== LEAF 275 len 2300
که هکلم سوراخ کردن نمل اسب و استر ومانند
آن از سل بیفند .
آواد - بسکون زای‌قطه دار.عمروف
است کد مدا و ندا و بانگه بلند باشد - وبمعنی
شهره شدن و سم کشتن عم آمده است .
آو اد گشتن بممنی شهره شدن
و مشهور کردیدن باشد .
]واه ۷ - بنتح زای هوز . بمعنی
شهرت باشد - و گفتار و حرف زدن بلند را نیز
گوشد - و چند نقمه‌هی‌هست ازموسیقی کهآ نرا
شش آوازه کویند و آن : سلمك و شهناز ومابه
و نوروز و کردانیا و کوشت باشد .
]و اذه گشتن - بسنیم آوازکفتن
است که بممنی شهرت گرفتن ر سمر گردیدن
ا وخ « بفتح ثاك و سکون خای قطه
دار. بمعنی آواخ است که آه واضوس - وفشمت
آو بروزن واو . آب را کوبند چه
در فارسی واو ببا و برعکس تبدیل می‌باید ۷ .
و « با تاك بالف کشیده . مخفف
آواز باشد لهذا هزار دستان را هزار آوا تسیز
گومشد .
] و اخه بسکون خای‌نقطه دار » بمعنی
آوخ قت که ماو بای نی فقوت نی مق اف
وضمت و اصیب را نیز گوبند .
آواد » بر وزن ناچار . مخذف آواره
است که از خان و مان دور افتاده باشد - وبمعنی
آزار و مشم هم آمده است - و حسب و ح
==== LEAF 276 len 1080
عمتی هم هست معنی بیاور - و بمنی صاحب و
خداوند نز گفته‌اند وقت ی که بالفظی م کب شود
همچو جنکه‌آور و دلاور و زورآور و مانند
آن - ویمشی کربه و زشت و بد قیافه هم بنظر
آمده است ۱ - و مخی‌ژشت و بدرا نیز گویند.
| ور چ4 - بنتح‌جیم» بمعنی‌آوارجه ۴
است که دفتر حسابهای پراگنده (۱) باشد .
آودذده بر وزن ناورد ۰ عمروف ات
که تقیض برد باشد ۴ - وبمعنی جنگ و یبکار
و کلوزار هم هت و بعربی«هیجا» خوانند .
ای بیع( ۹
آوردیلن ۴ - بننی حبله کردن
وجنگه اوری نمودن باشد .
]ود فك - ختح را رسکون نون ودال,
(6۷ ها :۷ج با که
کته
اند - و بیعنی مکی و فرب و حیله هم بنظر
آمده ات ۵
آوده- تح رایع و سکون ها ۰
اودی ح بر وزن باوری . صاحب
یقین و تحفق را" گونند . چه اور دمعتی تحقیق
و شین است ۹ ۰
| و شن س بکسر شین‌قطه داروسکون
نون » کاكوتي را کوبند ۷ و آن کیاهیست
که بعربی«سمتربری» خوانند ۵ .
آون *- بروزن اون ؛ مخخفآونگت
است که آویشنه و آویزان شده باشد .
او ند - بروزن ایند . رسمانی را
گوبند که خوشه های انگور از آن باویزند
کامروز همچو
==== LEAF 277 len 1247
9
و لنگی و جامه و غیره بر زبرآن اندازند - و
حجت و دلیل و برهاترا بیز کویند ۱ -و بمعنی
سابر ظروف و اوانی باشد همچو کاسه و کوزمو
امثال آن وبعربی «وعا» گوبند ۴ - و تخت‌وهسند
راهم گفته اند ۴ - و بمعنی شطرنج باشد و آن
بازیی است مشپور - و بمعنی اول و نضت هم
هست و باین معنی بکسر ثالث هم گفته اند .
و فدی ه بروزن رامندی , ظرف یکه
شواب درآن کنند .
و فگه ۴ - بسکون تون وکاف فارسی »
بمعتی رسمانی باشد که رخت بر آن انداژنه
و خوشه ای انگور نیز از آن آویزند- و حر
چیز آوشته را نیز گویتد.
آو نگان ۲ بروزن افرمان, آوشتن
و اوشته شده و آووان را گونتد..
٩‏ چنین کنت با پهلوان زال زر
رکه : آبه .
نامه» .
]وه - بنتح اك وطهور حا؛ بمعی ۰
ووای‌وافوس باشد ۵ وباخقای‌ها» نلم شهرست
ترديك بساوه ۱ - و کوره و داش خشت پزیرا
هم کفته اند - و بر آورتده صدا و ندا ماشك ب
و زنجیره را نیز گوبند که نقاشان و دوزندکان
ا وج 2۲ باجم. بروزن و معنی آویز
است که از آویختن‌باشد ۸ - چه در فارسی جیم
ابجد بزای هوز و برعکس تبدبل می‌بابد 4 .9
]ویر
==== LEAF 278 len 2199
آویزه وروت
آوفزه « بر وزن پاکیزه , کوشوارء
راگوند
. ٩و‏ لژ ۵ ح بازای فارسی ۰ بمعنی خاص و
خالص و پالك و پاکیزه ۱ - و شراب انگوری "
ناشد .
]و یه - ختح شین قطه دار , بسنی
او آوشن ات که کا کوتی ۴ باشد ۴ .
۵ -یسکون ها. کلمه است که‌بوقت
افوی و حسرت و مصیبت کوشد 6 .
] هد - بروزن ناعار » بمعنی خورش د
چیزی خوردن بأشد» چنانکه‌ناهار چیزی‌دخوردن»
و چون خورش باعث فوت است بنا بر آن آشی
راکه برکاغة و جامه مالند فا سب تقوت آن
کردد آهار کویند ۱ -ویمعنی فولاد جوهر دار
هم آمده است ۷ ,
]هدفه - بکس زای نفطه دار و
سکون تحتالی و فتح دال ۰ بعمنی کشیده باشد
خواء فد کشیده و خواء شمشیر کشبده و خواه
تنکه اسب و امثال آن ۸ - و عمارنهای طولانی
را نیز گویند .
- و
۰ آویش ۲-
باشین قطمدار بر وزن
پاشیدن . ک کونی را
گونند؟ وآن کیاهی‌است
که بعربی «سمتربری»
خوانند و در "کیلان
8 که نوت
وبینی_آریختن و بی
کئیدن نبغ از غلاف
۱ - مر کب از: پیشوند ۲ ۲+-ویژه » رکه : پیژه . فارسی نیز آوش »"
آبشن ۰ آوشن . آفشن ۰ آرشم 4102 2۵12618 < ابت
==== LEAF 279 len 1480
اه
۲ هنیا به (۱) - با بای ابجد و نون
و بای حطی وبای بيكك قطةٌ تحتانی بر وزن ۷ -
ات ادن بعتی جاااهوی امه که زوا از
گویند و مربی «تاب» خوانشد .
7 42 - بر وزن نافثه » بععنی آازیده
است که مطلن کشیده باشد اعم از قد کشیده و
شمشیر کنیده و امثال آن ٩‏ - و هارتهای
| هتخت ۲ - بکر ثالث و سکون خای
خن و ای افرشت » یمنی ب رکشید و بر آورد .
]خن ۴ » بروزن دانستن . بمعنی
" کشیدن باشد ۰طلقا اعم از هد کشیدن و شمشبر
از غلاف کشدن - و دست از چیزی کشیدن
و امتال انها ۴ .
باشد مطلقا ؟ .
]هر اهی * - با رای فرشت بر وزن
(۱) چب . چش : آحبیا ۱
رهنمای بیکیهاست .
آ هرمن * - بتتح رای قرئت و میم
بروزن لاف زدن» سمعنی و امن است کمرهنمای
بدیها باشد و بسکون رای فرشت حم کفته اند
که‌بروزنوا کردن باشه۷ . وبسن یکوینهآهرمن
شیطان است چنانکه (۲) بزدان فرشته است و
بضی گویند بزدان دم خداتمای کته آهرمن
نم‌شیطان و این اصح است : وتوبة مسگوشد
که خلی تمه علمت او ارنگی و بهع رسای
شر وفتنه و فاد اوست .
] هرن * - بر وزن باد زن » بععنی
آهرمن 
==== LEAF 280 len 2123
ودال ابجد ,کی را گویند که دروغ وید 6
هودم را فریپ دهد ۷ .
آ هی ؟ س بفتح اك و سکون نون »
ممروفست.- وشمشیر و تیغ را نیز آهن گویند .
بمعنی ب رکشیدن باشد مطلفا - و اهر بکشیدن‌هم
را یز گون که فاعل نوشیدن وکشیدن وانداختن
باشد ۴ - وبمعنی عزم واراده - ونضت وابدا-
و انداژهم آمده است .
از مرد سخت جان و سخلی کش نی محنت
کش باشد . ۱
] هنجد ؟ - بنتح جیم و سکون دال
۲ - آدرخش صاعقه » بدی 7
اه
ایجد , یشی یکشد - و ینداژد .
آهنچه - بتج جم ۰ پپناکش
جولاهگانرا گوبند , و آن چوبی است که طول
آن موافق عرش جامه ایست که می بافند و بر
هردو سرآن آهنی صب کرده اند » و آنرا هد
وقت بافند کی بردو کناوجامه بند کنند - وبعنی
گوند رسمانی باشد که جولاهگان در آخرکار
پندند و در سقف خانه بند کنند » و باجیم فارسی
هم کفته اند .
ا هی چخت - بض جیم و سکون 8
تای فرشت . آهنی باشد که زمین را بدان‌شیار
گت .
آ هنحیدن * - بر وزن واگردیدن,
بعمنی توشیدن- و کشیدن باشد. ویمعنی انداختن
هم آمده است ۷ .
آهمندآن دروشگو ظریب . « لت نامه » .
ایا 251
==== LEAF 281 len 1424
: آهنخای - باخای هطه دار بر ون
پا برجلی ء کنابه از اسب سرشخ یر زور باشد .
آ هن .دبا - بن رای فرشت » سنگی
کویند چون آب سیر و لعاب دهان ناشتا وخون
کوسفند ماده را بر آن بمالند جابه اش برطرف
شود .
هر گ ‌ بفتح‌رای‌بی نقطه دسکون
کاف فارسی . کنایه از اسب صاحب فوت ویرزود
باشد .
هن سرد کوفتن یکس نون
کنایه از کاری و اراده ای که تتیجه سداشته باشد
و بفعل تباید -
"هی ۱
ساز و آواز باشد ۴ -. و آوازی که در اول
اراده - و توجه - و عزم ‏ و شتاب و تعجیل
را یز گویند - و بمعتی خسید گی طاق ابوان و
امثال آن باشد که باسطلاح بنابان لنکه گونند
سوکنار صفحه وحوض وامثال آن راهم کفته‌انس_
و بمعنی طرز و روش - و قاعده وقانون هم‌آمده "
است - و صفت مردمان وجانوران را نیز کوینه
و ماضی کشیدن باشد بعنی کشید ۴ - و طوبلمو
گفته اید وحرهی «ازح» خوانند وق سقلپوسکان
آ هن گاو- باکاف فارسی بالف کنیده
و بواو زده » بمعنی آهن جفت است , و آن
آهنی باشد که بدان زمین را شبا رکنند . #
آ هفگیدن - مسدر آهنکه است که
بمعنی کشبدن بود مطلفاء خواء
==== LEAF 282 len 1250
آهو پای
عب را نیز گفته اند "۱ خواه با مردم باشد و
خواء با چیزهای دبگر-
و یمعتی رم باشد که از
رمیدن است چه آحوبی
رمیدگی را کوبند - و
بمعنی قرباد و آواز بلئد . . ۳
عم آمنه است - و تام
مرضی و عأی حم صست احو
که آیزا جربی ضیق‌النفی خوانند - و بطریق
استماره چشم را نیز آهو مبگویند - و شاهد
و ممثوق را عم کنته ان .
]هو بای » با بای‌فارسی بالف کشده
و خالةٌ شش پپلو را گویند -
19
آهوردی با واو مجهول بی وزن
لاهوری » یمعنی‌خردل باشد ؛ و آن داروبی است
یار تند و نیز ؟ . 8 ۱
] هون بر وزن قارون » رخنه و قب
را کونند ۴
سم
"هون پر « بفئح بای ایجد بر وزن "
عالمتاب است .
آهوی لقن س بسن یآهوی‌خاورست
که کنابه از خورشید جهان آرا باشد .
" آهوی دی - کنابه از آفتاب
است - و صراحی طلا را نیز گفته‌اند .
هوی‌سیهین « ساتی سفید پوست را
گویند و آن صاحب حنئی است که در عجلس
بمردم شراب میدحد .
آهوی شیر اقکن - چن-طلوب
و تیش و مت ی
صست .
آهوی فاك. 0 از خورشید
است
از با اصافی کردن باشد .
۱ آهو یی - بکسر بای اول و سکون
بای ثأنی »
==== LEAF 283 len 1186
(۱) بىمنیآهو باش د که عربان«غزال» کوبند ۱ .
]هیافه » بکر تالك مروزن نازبانه »
استضوان بای دماغ را کویند و آنرا بیبی
وس وس نب ی 9
باشد لیکن" آباک سار واه است وبیی
«حناك» عیگوف .
آهیخت ۴ ت بر وزن آوبثت ؛
نی يکنی و برآورد 2 پاشدبا
ری ده
آهیختی ی ده
پر کشیدن و بر آوردن باشه مطلفا ۶..
آهیخته ۲
بر آورده و بر کشیده باشد .
و استفهام باشد - وگاء بجهت امتفار و استخبار
ت لغتی‌است درآ هو 0 نه هزواری .
بصول خواهد پیوست بانه ۰4 - و کاهی درمقام
ی » بر وزن آواز » نام غلام سلطان
محمود غزلوی بود - و بعضی کویند نام یکی از
امرای سلطان اپراهیم بن‌سعود بن محمودغز نوی
است ۵ .
[بشتنه ۷ - بای فردت شت و نون بروزن
دارشکنه , جاسوس را گویند - و بععنی‌چاپلوی
هم آمده است
ا یشم ۷ + بکر ثاكث و سکون شین
که پرتو ماه باشد -
و فتج نون » بمعتی آیشتنه است که جاسوی -
و چاپلوی باشد .
| یشه ۱ - بروزن عابشه ء بممنیآمشنه
است که جاسوس ۸ و چاپلوی باشد٩‏ .
و تای فرشت » پممنی حاجتی باشد که از خالق
؟ ‏ ره : آهیختن . ۴ ساژه‌صدر
متخ کردن
==== LEAF 284 len 2151
اسکنف‌دی؟ - آینه‌ای‌بود ازعنرهای ارسطو
" که ابجهت آگاهی از حال فرنگه بر سر منارٌ
اسکندربه که در حدود فرنگه برکنار دربا بنا
کرد اسکندریود اصب کرده بودند. شبی‌پاسبانان
غافل شدند و فردگیان فرصت یافته آنرا درآب
اساختند و اسکتدربه را برهم ژدند » و عاقبت
. ارسطو آترا از آب‌بیرون آورد- و کنابه از قتاب
ح‌ حست .۰
آینه آسمان و آئیتة آسمان -
ونخلوق خواهند؟ .
آلن « تح الث بر وزن و حمنی آهن
آ دنه و ]دنه
که صورت چزها در آن‌نمابان
کردد و کاهی از فولاد یز
سازید , آینة دستی
7 بنة اسکنددی و 7ینف
«لت‌نامه». .۰ ۴ - پپلوی2162021 «منای »۷4٩‏ وعق20۵0» بارنیآدینگ ۹۷۵8" رد :
0۸6 18 ابر صمنطا:2 200 عبمم عازن ۲ اک ۸بع‌دنجدهع۲۲ ۱۷/۰8
(۰ 0,79 ۸ ,۷۵
در بلوچی 2060 , حاعهتع۵0 ,حعط20 ,2202 « جیلبرتسن +4۲ » مشثق از
ربشة له (پارسی باستان 9 بیین . پارسی دبدن) , یمنی آلتی که خود را در آن بسیننه « از
افادات ذغاهی استاد حنينك » :
فرستاد از آن آهن تیره رنگ یکی آینه کرده دوشن ز ژنگه.
فردوسی < لفت نامه >.
۴ - در نظم وش پارسی «1ب
==== LEAF 285 len 1071
.کنایه از آ غاب عالمتاب باشد .
] بنه اق و ز و آیینه افر ود -
صیقل گر و روش نکر را کوبند » و آن شخصی
باشد که چیزها را جلا دهد و صقل کند . 3
آینة چرخ و آینة چرخ -
بععتی آبنهٌ آسمان ابت که کنابه از خورشد
جهان آرا باشد .
آینة چینی و آئینه چینی -
آبنه است که ازتال‌سازند وآنرا بعربی«سجنجل»
اف بت ۱
آینةخاودی و آیینة خاودی-
آبنه دار و]بینه داد ۰ سرراش
و حجام را گویند ۴
آبنه ددای و آئنه زدای -
بمعنی آیینه افروز است که صیقل کر و ردشن
هو
تاعروس‌وحجز ی
آییژ + ۵ صفیر
آینة شش جهت و آیینة ششی
هت « آشاره بر دل سرور کاینات است
صلوات اف علیه - و کنابه از اسحاب کهف
باشد - ورجال الغیب راهم کنته اند ومشاهدات
راز گونند . ۱
آبنه فرور و آیینه فرود -
بیعتیآبینه زدای است که صیقل کر وروش نکر
باشد .
آینة گر دان و آبينةً "ار دان-
باضافت فو ی ان صمت: ام
9 با زای و
شرار؛ آش راگوند ۴ .
۳ رو و
و زشت و آرایش
س پر وزن پایین » بمعنی زیب
است ۷ و رسم و عادت و طرز
۴ نیز, آنکه آیته دریش دارد
۴ - ئز بویمادران ؛ ائث» آیدو ایدهم

==== LEAF 286 len 1536
آ لین جمشید - یکس نون . فلحن
دیم است از سی‌لحن باربد - و نام نوایی هم‌هست
از موسیقی .
وروش‌زا یز گویند - ونامدهی است یت ار
مومیایی . ۳ ۱
آ لین پرستی - بتح بای فارسی .
کنابه از خدمت کردن با مایت فروتنی باشد .
بیان دوم
در همزه با بای ابجد مشتمل برشصت و دو لغت و کنایت
زد و پلزن )۱( ۳9 عربی دز درست است - و در عربی سربار زدن و قبول
همین ممثی دارد . نکردن باشه ٩‏ . ۱
ی یب ) پاش من اول بروزن قماش » مجمعی
«باست که‌عرب«سم» گوند ۴ , چنانکه گویند "دا گویندکه از هرجنس مردم در آنجا باشند .
نو میگویم» بمنی با نو مبگوم - بسنی | . پاش ینم اول و قح آخر » بسنی
)۱( چك : ژند و باژند .
۱- مشهورترین آبین‌ها (تشکیلات) ۰ آبین اکبری است ِ- | کبریادشاه هندوستان
که وزبر او ابرالفّل در مجلد سوم « اکبنامة » خود آترا شرح داده است . < دائرة المعارف
اسلام : آین >. ۴ محیح آبن است . رك : آبن
۴ - آشوری بابلی ابو ۵01 , عبری اب 80 , آرامی ابا 202, لفات جنوب الجزبره
وحبشه آب 80 « ولفنون ۲۸۳ »؛ حزواری لا20 « دهارله ۱۷۹ », (20
==== LEAF 287 len 2406
و امد تجرید نوفتر
آای‌افت را با واو جمداز اف که « اوپاشه » باشد ابحد تحرید () نوشتن -
بومن حعنی نز کفته اند ۷ * . ۱ کنابه از توثك خواهش و آرز و کردن و ازخودی ‏
هام »یر وزن سلام . بسینی ولم است | و مزاحمت اضی بر آمدن واژماسوی اف مجرد
. که قرض باشد . ۶ گردیدن بلشه .
۱ - فرحنکه نوسان اين بت را از فطمدای ازسمدی شاهدآوردمانه :
در ساحب دیوان ابلخان نالم که در اباشة او جوریست برمسکین .
این شاهد برای ممنی ولفظ فوق رسا لیست وچنین میشمابد که این کلمه درقطعةٌ مزبوره
غیراز اباشة عرب وبمعنی سیرت و دوش وآیین وامثال آست « لت مه ٩‏ .
۵ اباقا - ترکی , اباغه . ابافا بمعنی برادر مهتر با کهتر پدر « جفتابی صا *.
8 اچث - اسطلاحاً حروف حجای عربی را که بترئیب الف , ب» ت . ث مرتب
شده و به ی ختم میگردد » ابتث فامند » درمقابل ابجد . دسثه بندی حروف بترتٍ ابجد با
قدینتر از ابتث است . چه آن در خط فنیفی د عبری وسربالی و آرامی و تبطی نیز موجود است.
رور عرب بسد ها ترئیب اسلی الفبا را جهم زدند و نرتيب دبگری اختبارکردند ک
==== LEAF 288 len 2166
ابحل ی
)بحل « بنتح اول و ضم حای بی نفطه و«شتکار» نیز گفته‌اند » لقری را نافع است .
و سکون ثانی و لام » نام یادشاه جایلسا باشد » و
آن شهپرست در مقابل جابلفا وهردو درعالم مثال
اند ؛ و بعضی جایرسا گفته اند که بجای لام .
رای قرشت باشد .
) بحاد - باخای نقطه داربر وزن‌اهواز.
تلم ولانتی است ازتر کستان مشهوریظلم:. گویند
مردم آنجا یشتر ترساو آتش پرستند و درآنجا
دبرست سار تسم ۱ .
ایحوسا ۴ - باسین بی نقطه بر وزن
محمودا . بزبان سربانی دوائی است که ب رکه
آن ساه برخی مابل باشد و آنرا« اپوخلما »
آیدا۵ - با دار ابجد بر وزن بد تام
بمعتی چم است که در مقابل جوهر باشد ۴ .
ابف‌آن - بر وزن افغان , بمعنی دودمان
و خاندان باشد - و بمعنی سزاوار و حستحق حم
آمده است ؛ و در موّبد الفضلاء با ذال نقطه دار
نوشته اند * .
ایدرم * ه بکس اول بروزن اسپرم .
نام کتلب شاکمونی ۷ و او باعتفاد کف ند
پیغمس صاحب کتاب است » و معنی این لفت
باعتفاد او اول و آخر کتابها باشد .
اير - یسکون ثانی بروزن صبر » حص‌ون
البلدان) ۸۵25 و ۸۵216 « ل
==== LEAF 289 len 2495
- ۷ - ایکا کبا
و سکون الث و ها و رای قرشت ؛ نام اصلی
نیشابور است و ممدن فیروزه آلجاست ٩‏ .
ابر قباك ع من فان . نام ولایتی است
از توابم اره جان ۱ که میان اهواز و فاری
واقم است و آباد کرد قباد شهربار است ؛ و با
زای قطه دار هم کفته اند ۲ . #
ا پر کاد - باکاف‌بروزن‌اتکبار » بمعنی
متحیر و حیران و س رکردان باند ۸ .
ایکا کیا هیفتح اول وانی‌و کسرکاف
دوم تحتانی بال فکشیده , ننیده و تارعنکبوت را
کویند. اکر بر جراحت نهند خون را باز دارد
انت و بمربی «سحاب» گود ٩‏ - و بمعنی هرد
(۱) هم آمده است که دره‌قابل زن‌باشد, و بفنح
ثانی‌بلفت زند ویازید (۲)لت تناسل را گوید ۳
- و «بر » را نیز گفته الد که بمرمی « علی »
خوانند ۴ و بمعنی بر و آغوش هم هت  .‏
آ برش ع بنتح اول و تال ۰ بر وزن
مهوش ؛رنگه سرخ و سفید در هم امیخته را
گوبند . - و اسبی که نقطه های مخالف رنگه
او پر او باشد ۴  .‏
] پر ش خور شیف کنابه‌ازآسمانت.
ابر شهر - فتح اول و انی و رابع
(۱) چك : مردم ! )۱( چك : ژند و باژند ..
۱ - انسکرت 2080۴4 (با 200068 مر
==== LEAF 290 len 2199
و نگذارد که جراحت ورم کند . وااگر بلس رکه
بردمل. وخيارك نهند ب رکرداند ۱ » وابرک کیاپ "
یز بنض آمده است که در آخرش بای ابجد
باشد . ٩‏
ابر که ین کاف » نم شهزیست از
عراق عجم . و چون‌آن شهر بر زمیتی که درته
آن کوه است واقم شده باين نام موسوم ماختند
ومعوب آن ابر قوه است ۴ حرایین زمان بتعریب
ار هر گنه - بکر ثاك و خم میم »
بمعنی ابی‌کپن است که اسفنج الب باشد ۴ .
ابر نجن - بفتح جیم‌بروزن ب رکندن»
حلقه ای باشد از طلا و نقره و امثال آن که
زان در دست و بای (۱) کنند ۴ و آنه در(۷)
دست کنند دست ابر نج و آنراکه در (۲) بای
کنند پای ابرنجن خوانند .
اتتهار دارد . ابر ن<سن - بر وزن فروردین ؛ بمعنی
اب رگن - بکس تاك و انوم ابر‌تجن است . وان حلقه‌ای باشد از طلا و نقره
که در (۲) دست و پای کنند ۴ .
ایرو ددن - کتابه از دا دادن
واشاره کردن باشد ۵ .
ها و سکون نون . چیزی است مانند مد کرم
خورده » چون بی آب گذارند اب را بخود کشد
واسفنج الیسر حمانت ۴ .
۱ - دلیل توایری است یوشای حق بیستی است همچون ابرکا کبا
لطيفي پنقل
==== LEAF 291 len 2402
اول و فتح ثانی حوبرء را کویند و آن پرنده
ایست که بمربی « حباری » گوبند ۴ و کی
«تفدری» خوانند و بکسر اول ميو# نوری و و
باوه باشد ۴ .
ا یر هام » باها بروزن شفق فلم . بمعنی
طسمت باشد؛ گویند فرشته ات که تدی سکننده
عالم است - و تام ییفمبری هم هست ۵ .
ار هه - بنتح اول و ثالث و رابع » تام
پرنده ایست بمیار حقیر ۷ - و نام سر کروء(4)
اصحاب فیل هم هست . کوبند وفتیکه بخراب
کردن که معظمه می آمد ؛ در راه بجپنم
واصل شد و هو که قبر اورا می بیند بی اختیار
ارو د فك - ینی اداره کند -
ورشادهد - _,
اپرو فراخی ‏ کنابه از خوشدلی
و خوش منشی و کشاده روبی و اژه دوی -
وهمت و سضاوت باشد (۱) .
ابرو لقن -با نون و تای فرشت » بی
ون پهلو شکن . بزبان زند و باژند (۲) بمعنی
مردن باخد که در مقابل زستن است ِ.
ابر وی دالزد س کنابه از ماه نو
باتد که بعربی هلال گویند .
ابر ه « بفتح اول و سکون انی » دوی
کلاه وروی قبا و امثال آن بائد ۴ -و بضم
۹ وارش ۵ بپهلوی ( مردن ) ۷6۲01010180 است « براهامیان ٩٩‏ *.
۴ - لرماند پیکی‌سف رگث‌دیبا
```


## [2026-09-04T18:50:16.859Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/ref_page.py BQT:72 --image 2>&1 | tail -40"
}
```


### [2026-09-04T18:50:18.622Z] TOOL RESULT

```
no scan of BQT covers printed page 72 (see 'scans' in refs_online.json)
```


## [2026-09-04T18:50:27.264Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'ahuk\\|āhūk\\|ähük\\|ahūk\\|hūk\\|ähuk' BQT_v1.txt BQT_v1_pages.txt BQT_alt_v1.txt BQT_dli_part1.txt 2>/dev/null | head -20; echo \"---- avestan ahu grep\"; grep -n -i 'anahita\\|anāhitā\\|anahit' BQT_v1_pages.txt | head"
}
```


### [2026-09-04T18:50:27.344Z] TOOL RESULT

```
---- avestan ahu grep
```


## [2026-09-04T18:50:36.026Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; for n in 282; do curl -s -L -o bqt_$n.jpg \"https://iiif.archive.org/iiif/borhan-ghate-v1%24$n/full/1200,/0/default.jpg\"; file bqt_$n.jpg; done"
}
```


### [2026-09-04T18:50:43.158Z] TOOL RESULT

```
bqt_282.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 1200x1698, components 3
```


## [2026-09-04T18:50:45.017Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt_282.jpg"
}
```


### [2026-09-04T18:50:45.070Z] TOOL RESULT

```

```


## [2026-09-04T18:51:08.217Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ahog ===\"; grep -n -i 'āhōg\\|ahog\\|ahok\\|ʾhwk' PHD_mackenzie.txt PHD.txt | head -10\necho \"=== NYB ahok ===\"; grep -n -i 'āhōk\\|ahok\\|āhōg' NYB_vol2_glossary.txt | head -10\necho \"=== HRN ahu ===\"; grep -n -i 'āhū\\|ahu.*Fehler\\|Gebrechen' HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i 'āhū\\|ähü\\|anahita' HUB.txt | head -20"
}
```


### [2026-09-04T18:51:08.347Z] TOOL RESULT

```
=== PHD ahog ===
PHD_mackenzie.txt:6768:hare sahog, xargos.                      held griftiir.
PHD_mackenzie.txt:7857:undefiled anahog, analiid; v. immacu-    unwilling akiimagomand.
PHD_mackenzie.txt:9051:si                            ..1.tl    sahOg                       ,~~
PHD_mackenzie.txt:12199:anagih                   ..", ~ ~      anahog
PHD_mackenzie.txt:12386:ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
=== NYB ahok ===
=== HRN ahu ===
=== HUB ===
4826:Shk. 228, arm. Anahit, zd. anahita-,
```


## [2026-09-04T18:51:15.111Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ahog ctx ===\"; grep -n -i -B3 -A3 '^ahog\\|ahog,\\| ahog ' PHD_mackenzie.txt | head -40\necho; echo \"=== PHD anahid ===\"; grep -n -i 'anahid\\|anahit\\|nahid' PHD_mackenzie.txt | head -20\necho; echo \"=== PHD.txt variant ===\"; grep -n -i 'ahog\\|anahid' PHD.txt | head -20"
}
```


### [2026-09-04T18:51:15.187Z] TOOL RESULT

```
=== PHD ahog ctx ===
6765-  husnud, sad, xunak.                    heel pasnag.
6766-hard saxt, staft, skeft.                 height baliiy.
6767-hardness, hardship skeftih.              heir namburdiir; enoken.
6768:hare sahog, xargos.                      held griftiir.
6769-harm (n.) ak, anagih, azarm, bes,        hell dusox, dwarisn.
6770-  besisn, wizend, zyan.                  hellish dusoxig.
6771-ll~                    ENGLISH-PAHLAVI INDEX
--
7854-unconscious abeos.                       untilled awarzid.
7855-unconsciousness abeosih.                 untruth ariist.
7856-uncultivated anabadan.                   unwanted anabediin.
7857:undefiled anahog, analiid; v. immacu-    unwilling akiimagomand.
7858-  late.                                  u1l'lcitting anagah.
7859-under azer, er.                          unworthyanarzanig.
7860-undershirt sabig, taskanag.              up abar, uI.
--
12383-aMgen-                        -,.,-'~         axczidan                 \\~~
12384-aMgenidan                  \\te,)" ,~
12385-                                              iihidih                   -"-'~
12386:ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
12387-axwarr                             \\"'0'     axwan
12388-                                                                             \""' t"U'
12389-axwarrsaHir                ~~~                axwarih                   ~~

=== PHD anahid ===
1052:anahid ['n'hyt ' I N ntihid] immaculate; a goddess; astr. Venus.
5388:winAhidan. winAh- [wn)s-ytn I M wyn)h-] spoil, damage, destroy.
6304:creation afurisn. brehenisn. (bun-)        damage (v.) winahidan, zinenidan;
6361:defecate ridan.                               wanidan, wirnustan, winahidan,
7633: sorrow andag, andoh, bes, pim,         spoil wimustan, winahidan.
7899: Venus Anahid.                           wall dewar.
10115:winJisk                             winahidan
10198:winahidan         \\~II                wiftag                \~~Q.YI
12198:anagiih                 ~ ~,.-.        Anahid                   \l'6'Vt"

=== PHD.txt variant ===
2378:immaculate anahid, awinast.
```


## [2026-09-04T18:51:20.746Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1040,1060p' PHD_mackenzie.txt; echo \"-----\"; grep -n -i \"ah[oö]g\\b\\|ahog \\[\" PHD_mackenzie.txt | head; echo \"--- search 'hwk'\"; grep -n \"hwk\" PHD_mackenzie.txt | head"
}
```


### [2026-09-04T18:51:20.812Z] TOOL RESULT

```
an-IdDI! ['n)twk'] incapable.
an-afseniAn ['n)psynfn l ] indestructible.
inaftan, anib- ['n)pen', )n)p- I M )n)pt, Cn'm-)] avert, reject, frustrate.
 -iAn: avoidance, warding off.
anag ['n)k' I M )n)g] evil.
 -ih : evil, harm.
an-agah ['n)k)s I N ntigah] unaware, unwitting.
anilg-kardilr ['n)k' krt'l], -kuniAn [-kwnsn ' ] evil-doer, maleficent.
anagr ['ngl] infinite.
 -an [-'n' I M 'nyr)n] Infinite Light; cal. 30th day.
anaf!\r-rOsn(ih)                       9                           anerib
 .....,-rOsn(ih) [-lwIn', -lwInyh] Infinite Light.
anahid ['n'hyt ' I N ntihid] immaculate; a goddess; astr. Venus.
an-ahOf!\ ['n'hwk ' ] undefiled.
an-aUld ['n'lwt l] undefiled.
a-nam~istif!\ ['n'mcftyk l ] unspecified.
an-Imurzid ['n'mwlcyt l I M 'n'mwrzCyd] merciless.
an-amurzisn ['n'mwlcfn'] mercilessness.
anlr ['n'll N .....,] pomegranate.
anarf!\el ['n'lgyll N ntirgel] coconut.
an-arzlnif!\ ['n'lc'nyk l ] undeserving, unworthy.
-----
6768:hare sahog, xargos.                      held griftiir.
7857:undefiled anahog, analiid; v. immacu-    unwilling akiimagomand.
9051:si                            ..1.tl    sahOg                       ,~~
12199:anagih                   ..", ~ ~      anahog
12386:ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
--- search 'hwk'
558:add    hiig [HZWLYA < A ~zyr'; hwk' 1M hwg, N xugj pig.
559:add    hiikar(ag) Ihwkl(k') I N xiikaraj porcupine. (not hedgehog)
948:                ihOg ehwk l I M Uhwg, N aha] fault, blemish.
960: Ahila [TYBA < A Iby'; 'hwk' I M (')'hwg, N tihu] gazelle.
1053:an-ahOf!\ ['n'hwk ' ] undefiled.
2433:gahug [g)hwk ] bier.
4474:sah6~ [shwk l ] hare.
4992: -tiho~ [tyhwk l I N tihu] small grey partridge.
5563:x6g [hwk I N xwk, xoy] nature, character, disposition.
5580:xiig [HZWL Y A < A lJ,zyr); hwk l IN . . . . ] pig.
```


## [2026-09-04T18:51:28.948Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN Gazelle/Fehler ===\"; grep -n -i 'gazelle\\|Fehler,\\|Gebrechen' HRN.txt | head -20\necho; echo \"=== HUB ctx 4826 ===\"; sed -n '4810,4840p' HUB.txt\necho; echo \"=== NYB ===\"; grep -n -i 'ahok\\|āhōk\\|ahog\\|anahit' NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-04T18:51:29.024Z] TOOL RESULT

```
=== HRN Gazelle/Fehler ===
974:59. ähu 'Gazelle*.
975:phlv. ahük 'Gazelle'.

=== HUB ctx 4826 ===
m(i)zd und muzd Gl. and Ind. 213 und 217, afgh. LW. mazd
oder muzd Vages, hire' = zd. mizda-^ ap. ^mizda-, gr.
fjLi6&6g] supuS, supus neben sipiS u. s. w. 'Laus == zd. spis;
tabus (Muwaffaq) = tabiS 'fervor, aestus' (Horn, Grund-
riss p. 83, Anm. 1); nu (neben ni) in numUdan zeigen*,
nuvistan schreiben (= nivistan) , nuvdxtun (= navOxtan)
schmeicheln', nuhuftan ( - nihuftan) *bedecken, verbergen'
von zd. ap. ni-, vgl. ap. nipistam geschrieben', nipiStanaiy- 138 -
'schreiben'; praef. gu- — zd. ap. vi- in gur^xtan, guzldan
u. 8. w.
Ueber den Wechsel von t und u in der Partikel hi =
hu je nach dem folgenden Vokale siehe Trumpp, Accent
und Aussprache des Persischen p. 243 {bi-nmn *setze dich*,
bi^rau gehe*, aber bu-kun *thue* etc.), Sal. Shuk. Gram,
p. 14.
Aus iwird?: Naked (Noldeke, Tab. 4) = paz.-4«atotf
Shk. 228, arm. Anahit, zd. anahita-,
Ueber Ir aus iry = ^y siehe § 8, c.
§ 20. Ap. I (= idg. %) bleibt im Np. als I, vgl. s%r
'Milch'= skr. HVra- ; dldan *sehen', ap. didiy d. i. *didiy, skr.
dl glanzen ^) (ipt. didlhi und dTdihi)^ u. s. w.
Fiir t erscheint e in ^ir5 *Hals*, girebdn *Kragen*, skr.
grTva- 'Nacken*.
Kapitel 4: ap. u nnd u.
§ 21. Ap. u (= idg. u) bleibt im Np. als u, vgl. u
(u) und* = ap. uta; ustur (sutur) 'Kameel* = zd. mtra-;
xmk 'trocken = ap. uSka-, zd. huika-, skr. guska-; xusur
*Schwiegervater = zd. x^asura- ; Xusrav = zd. husravah-
(arm. Xosrov, gr. XoOpo^g).
§ 22. Anlaut. w vor einfachen Konsonanten in mittel-
persisch zwei- oder mehrsilbigen WSrtern wurde zu a und

=== NYB ===
419:Anähit ['Phyt'] a female deity; the planet Venus 511. — Av. (125) Anahita.
869:azat [c”t'; inser. ?z't-] 1. noble, noble- man, nobility, designation of the large class of lower Sass. nobility (v. Christen- sen, Sass. 111-113): pl. cas. rect. ~ 26*; pl eas. obl. —-än HajA:6. B:6 [’z’tn]. 169. — 2. set free from servitude, manu- mitted (of a slave), sg. cas. obl. ~-éh, v. s. v. daštan. — 1. Av. (343) ā-zāta- ‘high- born, noble’ (v.s. v. zātan), properly ‘agnate’ and therefore in the line of succession and entitled to a share in the inheritance and privileges of the clan; Arm. lw. azat; hence also Paz. àz(!)ad, Skr. v. ddhya ‘rich’ (SGV). — 2. < d- + Av. (1688) zäy- ‘to let out (water from a basin)’, cf ava-zdy- ‘to chase away’; MPrthPrs ?zd ‘free’, in this sense also Arm. lw. azat and Paz. āž(!)ād, Skr. v. svatantra ‘independent’ NP āzād; borrowed in OAram in the expression ?2't SBQ ‘to release’ (Pap. Kraeling). The earlier investigations of these two ws., which were as a rule regarded as one etymologically (by Bthl; Bailey, BSOS VI, 1930-1932, 70. 953-955; Gershevitch, JRAS 1954, 126; Benveniste, JA 242, 1954, 298-299), are now superseded by the short but masterly analysis given by Anahit Périkhanian in REA, N.S. V, 1968, 9-16, establishing, with the aid of abundant Arm. material, two hom- onyms of widely different origin and use.
4015:Anahit Pērikhanian, to whose paper in REA, N.S.V, 1968, 9—30. reference is made here once and for all.
```


## [2026-09-04T18:51:40.357Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 59 ===\"; sed -n '968,985p' HRN.txt\necho; echo \"=== MON آهو ===\"; grep -n -o 'آهو[^ ]\\{0,40\\}' MON_part1.txt | head -20\necho; echo \"=== MON ناهید ===\"; grep -n -o 'ناهید[^ ]\\{0,60\\}' MON_part1.txt MON_part2.txt | head -10\necho; echo \"=== ARY latin index ahu/anahita ===\"; grep -n -i 'AHU\\|ANAHIT\\|NAHID' incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-04T18:51:42.338Z] TOOL RESULT

```
=== HRN 59 ===
gleichen np. ferhe/teiiy ferhi/ten^ ferdhi/Un (phlv. fra-
hä/Jan 'erziehen etc., frasäxtan, AV., sind nur fraJtä/tun
zu lesen), die ebenso wie berhe/ten^ berki/teu 'ziehen,
herausziehen* und 'erziehen bedeuten sollen; vergl.
ferheng, ferhenj 'Wissen etc.' (phlv. /raAaw^, Nöldeke,
Kärn. 38; arm. LW. hrahang), ferhenjukn 'erziehen.
59. ähu 'Gazelle*.
phlv. ahük 'Gazelle'.
kurd. ask; afy, ösai; bei. äak (19), LW. aü (15); ya/.
LW. ahü.
60. äyem 'ich komme*, äyende.
ap. *el + l^«y- ; päz. ü^d, aend {üyad, äyand),
kurd. e/w, ei, et etc. (Justi, Gramm. S. 235, Houtum-
Schindler, S. 103); bei. äyag^ n. ay (21); wa/. ni-ytt
(3 Sg.).
61. äytn 'Sitte, Schmuck*, äJTw-); aöme^ adme 'Freitag*.
phlv. ädlnak, ay\i\nak 'Sitte, Gewohnheit'.
Wohl zu ö + i^dai- (ai. {^dhai-) wie die folgende

=== MON آهو ===
5449:آهومند]
5550:آهوان»
5551:آهوها.
5553:آهو:
5557:آهوان»چون
5557:آهو.
5559:آهوپا]
5560:آهو
5563:آهو
5564:آهو
5566:آهوجه:
5567:آهو
5567:آهو.
5569:آهودل:
5573:آهومند.
5574:آهون:
5579:آهون‌بر:
5599:آهو
6488:آهوه
8165:آهو

=== MON ناهید ===
MON_part1.txt:215:ناهید
MON_part1.txt:16001:ناهیدن.
MON_part1.txt:26869:ناهید.
MON_part1.txt:32687:ناهیده»
MON_part1.txt:32689:ناهیدن:
MON_part1.txt:37457:ناهیدن»
MON_part1.txt:70247:ناهید.
MON_part1.txt:72508:ناهید
MON_part2.txt:80581:ناهید)
MON_part2.txt:81488:ناهید)»

=== ARY latin index ahu/anahita ===
2777:éss AHU-, AHURA, —(AVESTAN) gl)
2975:BOG (OLD ENGLISH) oy pnts! BAHUH, BAHUS
3134:BRUG (DUTCH) gala BRUR, BAHU — (SANSKRIT) ca Si
3910:VESELS LATVIAN) (35) 393 VAHU
7490:‘TRE :(OLD SCANDINAVIAN) oS Sahu!
8266:DEIDEMON, DEIMOS, DEILOS DUSHAHU <(OLD PERSIAN) inl .go\
9625:AMINDAROY: (POISON) 269 ‘ZHAHR, ZHAHUR (ARMENIAN) ¢s,!
10942:FOUNDEN :(OLD ENGHISH) oS lSsi JUHOTI, AHUTIS
14288:NAGEL (DUTCH) gale KAKUN, NAHUN, —(BALUCHI) x
```


## [2026-09-04T18:51:48.683Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 5545-5580 ===\"; sed -n '5545,5580p' MON_part1.txt\necho; echo \"=== MON nahid 26860-26875 ===\"; sed -n '26862,26875p' MON_part1.txt\necho; echo \"=== MON nahid 70240-70255 ===\"; sed -n '70240,70252p' MON_part1.txt"
}
```


### [2026-09-04T18:51:48.802Z] TOOL RESULT

```
=== MON 5545-5580 ===
تهی‌شاخان» جزو راستة نشخوارکنندگان که 
اقسام مختلف دارد و توا دوتة سار 
سریع و چابک و دارای دست و پای بلند و 


چشمان زا است؛ غرال» ظبی؛ ج. آهوان» 
آهوها. 

آهو: 1 (.) عیب» نقص. بسماری» مر ض. 
(ص.) بد» ناسند. 

افته انسه: (0-)200۷-202 (ق.) مانند 
آهوان»چون آهو. 

اهوپای: .5 [- آهوپا] (ص‌مر.) (معم.) 
بنا با خانه آهو پای. خانه شش پهلوء خانه 
ضلمی. 

اهسوتک: 2.1 (ص‌مر.) مانند آهو در 
دوندن» آهو دو. 

آهوجه: .2 (ص مر .) آنکه جهشی چون 
آهو دارد» جهنده مانند آهو. 

آهودل: 5-44 (ص‌مر.) ترسنده: شتردل؛ 
گاو دل» بزدل. 

اهومند: 20 (ص‌مر.) مر بض» سمار» 
آهمند. معیوب» اقص» مختل» آهومند. 
آهون: 0 (.) رخنه و راه و مجرایی که 
زیر زمین حفر کنند» نقب» سمج) اهون. 
اهوناک: .2 (ص‌مر.) معیوب؛ دارای 
۱ 

آهون‌بر: 3.۴ [- آهن‌بر ۹ آهن‌بره] (افا. 
ص‌مر.) نقب‌زن» نقاب. 

=== MON nahid 26860-26875 ===
درخت بید. نوعی از پیکان تیر شبیه به برگث 
نك . 


بید خحت: ۱۵-0۷ [- بذخت - بغ‌دخت» 


۳ (امر .) ستارة زهر ه» ناهید. 
بید خشت: ]نا (امر.) و کی که 


سدر فرهنکگ فاررسی و 3 ۳۰ 



=== MON nahid 70240-70255 ===
زاور: :222 (- زور] (.) زور» قوت» نیرو. 
زاور: :22:۳ (.) وان سواری و بارکش» 
راحله. 

زاور؛ ۶ (.) (بز.) علتی است که آن را 
آب سیاه گویند. 

زاور: 22۷2۴ (۰) زهره» ناهید. 

زاولانه: (م-)22۷182 [- زولانه] (.) بندی 
آهنین که بر گردن و دست و پای ستوران یا 
زندانیان بندند؛ بخاو» بخو.
```


## [2026-09-04T18:51:58.338Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON nahid headword ===\"; sed -n '72500,72515p' MON_part1.txt; sed -n '210,220p' MON_part1.txt\necho; echo \"=== ARY pages آهو ===\"; grep -n -o 'آهو[^ ]\\{0,50\\}' incoming/ARY/ARY_pages.txt | head -15\necho; echo \"=== ARY pages ناهید ===\"; grep -n -o 'ناهید[^ ]\\{0,50\\}' incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T18:52:00.331Z] TOOL RESULT

```
=== MON nahid headword ===
زهره‌بناگوش: 5 - 2 [ع. . ف.] 
(ص‌مر.) آنکه بناگوشش ش مانند زهره 
درخشان است (معشوق). 

۳ داشتن: 7.0 (مصل.) دل و 
جرأت داشتن» شهامت داشتن. 

زهره‌رخ: 2-۲ [ع. ف.] (ص‌مر.) دارای 
چهره‌ای مانند زهره؛ ناهید رخسار» زهره 


زهسره‌طبع: "7-20 [ع.) (ص‌مر.) آنکه 
طبیعت زهره دارد؛ کسی که به عيش و 
عشرت و مجالس بزم و موسیقی علاقمند 
است. خوش‌منش. 


تصنیف و تألیف : 

الف ‏ تألیف : 

۱ - ستاره ناهید یا داستان خرداد و امرداد (نثر و نظم) چاپخانة شرکت طبع 
کتاب تهران ۰.۱۳۱۱ 


۲ حافظ شیرین سخن. جلد اول بنگاه پروین. تهران ۱۹ ۱۳. 


=== ARY pages آهو ===
8747:آهورامزدا"
13275:آهوش
15575:آهوش"

=== ARY pages ناهید ===
15953:ناهید
```


## [2026-09-04T18:52:06.422Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\np='incoming/ARY/ARY_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\nfor n in (15953,13275,15575):\n    # find nearest preceding [pdf page N]\n    pg=None\n    for i in range(n-1,0,-1):\n        m=re.search(r'\\[pdf page (\\d+)\\]', lines[i])\n        if m: pg=m.group(1); break\n    print('line',n,'pdf page',pg)\n    print('\\n'.join(lines[max(0,n-8):n+8]))\n    print('-----')\nEOF"
}
```


### [2026-09-04T18:52:08.056Z] TOOL RESULT

```
line 15953 pdf page 537
1 ۸020 انگلیسی (نل82/01./5): رادید ۸ نا
آرمنی (4۸6۵۷۸4۸): ۰ 1180 0۸887811 دانمارکی (1820ل0۸): ار برد 68 ان ۱
بونانی 0725880): اد اند سوئدی (81750157): 1۸
لاتین (710مل): 10 نروژی (/40ا0 ۸/08۲8 اد رد 8 8 ند
فرانسه (۳72(/674) 02 هملدی (7ل070): از اد
اسپانیایی (5۳۸۸75): دشن لهستانی (52لا۳0): اسان در
ایتالیایی (1فلرقه7): 11 روسی (لها55نا#): ان بان زار
رومانی (۸04اانهلاناهید ‏ 1088887865 چکه (280(7): 3
پرتغالی (۳070010885): 012 بلفاری (استقم‌ماناق: ۰ ۸0۷۳۸8۹۳۲
گرنیک (0077710): ۸۳ اسلواکی 5]01۸0): اناد اند ره
ایسندی کهن (8(7010۸71۸2 صا0): آلبانی (4۵//۵۸۷: 038 2762/0۸01
87
[pdf page 538]
نا اک اک وم
۰
بیغ / ۵۳۹ ۱
-----
line 13275 pdf page 446
انگلیسی کهن (9لقلا80 ۰:02 8۸8۳ ۶008900 .
انگلیسی (577ل62/01): 2۸ 0 (5۸3) :8470/77
دانمارکی (0۸/824): 02 6 (56 ۴ 0) ,251 َ
سوئدی (5750/57): ۵5۸ 2 (38ه5) داد اه
نروژی (/(40775014: 08۵ برهان قاطع : ۱۸۵۵
یادداشت:
۱ بازگشت به: هوش
۲- در اوستایی "گوش" و آهوش " هم چم بوده‌اند.
اس ارستایی (4۲297۵۷): ۰۸057۸۸ نروژی (/۷077501۸)(محلی) 05
پهلوی رن ۰ ممتعته هلندی (/0076): 1
کردی (57/صناه): 7 مقااقنآم
بلوچی (31ل/اءل8۸): 01۸ پسگشت‌ها شک تن
ونانی 0882/0): عقانا» ۶0۵08
نورس کهن (۸۵788 010): 085 8 (۲0232) :۸4402/215
سوئدی (57:015[7): 8 ,2718۸ برهان قاطع : ۱۸۵۹
[pdf page 447]
-----
line 15575 pdf page 524
بونانی 0670): ایا( موز (۸1130 ,123 (۱83,08)
لاتین (71۸مل): ای ان ۸
گوتیک (00774/6): ۷۸5 46 +7
انگلیسی کهن (#اقلا2/0 ۰:۵۵ ۷۷8۴۰ برهان قاطع + اریریرا اه فا
ینوانی (//(نا7آا): ۷۸5 لغت‌نامه دهخدا: ۱۳۶۲
لعرنی (لتی) (714(۷بل): نت انا
بادداشت:
در پهلوی این واژه هم به چم "یاد" و "حافظه" و آهوش" بوده و هم به چم "نیرومند"» آقهرمان".
اوستایی (/48974): . 2 اقا پرتغالی (ظ۳07701788): دید
پهلری (41مائل۸): گالی (ن3لالا0۸): 1۸
ات 4 بل :۷۷۳2۸0 برتونی (8870): میا
ِ ً سانسکریت ( 0 1 آلبانی ‏ (1۸/۷ 8/۸7 ام): 0 ,۷100
۸۵5۵۲ ,۷85 ,۷15
: آرمثی (۸0/8142): میدن ۱ پسگشت‌ها ارت درد
۱ بونانی 088870): رن را
لانین (7100 )+ ۸5 9 (0185۸) ما05
-----
```


## [2026-09-04T18:52:21.974Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN diet ===\"; grep -n -i 'diaita\\|diaitan\\|dianta' KLN_1966.txt KLN_1971.txt | head -10\necho \"=== SKT diet ===\"; grep -n -i -A4 'diet\\b' SKT.txt | head -20\necho \"=== IEC ai- ===\"; grep -n -i 'aitsi\\|aisa\\|aetd\\|aēta' IEC.txt | head -10\necho \"=== SYN share ===\"; grep -n -i 'diaita' SYN.txt | head -5\necho \"=== WLD band3 ===\"; grep -n -i 'diaita' WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-04T18:52:22.108Z] TOOL RESULT

```
=== KLN diet ===
=== SKT diet ===
119:II  u  in  WiUinms'  Diet. ;
120-in  FcrraU  uid  Kepi* :
121-as  In  the  Tftiichnitr  Dutch Otd  Dui^  wunli  arc  (roro llcxtiam     (165S),     or
122-I  iLJiglwi;   as  ta  Webster  s
123-Enfrltkb  (English  from
--
145:Diet.,  1851. Low  L, — Low  Latin ;  as  in  the  Lexicon
146-Mannale  (abridged  from  Ducangc)
147-by  Maipne  d'AmU,  1866. M.  E. — AltUdie  English;   see  under  E,
148-above. M.  II.G.—Middle  High  Gennan ;  see
149-under  G,  above. Norw. — Norwej^ian ;  as  in  Aasen's  NonJc
--
153:and  Pcrs.  Diet ;  or  in  Palmer's  I'crs.
154-Uict^  1 8; 6. Port. — Portu;;iie5e  ;  as  in  Vieyra,  1857. Prov.^Provcnfal :  as    in    Ravnouani'«
155-Lexique  Kouian,  and  iJai  tsca\  Chro-
156-tomatbie  Proven^ale. Rnss. — Ku>sian;  as  in  KcifTsDict.,  187^. St:and. — Scandinavian;  nvd  as  a  general
157-term  for  Icelandic,  Swedish.  Uani&h,
--
159:Diet.,  or  in  Widtyrcti. Swed.  dial.  —  Suedish   dialects;   as  in
160-Kieti  C'S07). Tcul.  —  Teutonic  ;   a   peneral   term   fof
=== IEC ai- ===
317:aità, is, iə “share, part, lot. WP I, 2 & I, 7 Av. aeta; Gk. aisa (ambig.); Osc. aet-, aitt- (i-stem); OHG cf. eidum (OFris. athom, OE apum, G Eidam, 'son-in-law', lit. *partici- pant' according to Kluge 17)
1471:bhoisos, à (fearful; fear, horror. Cf. WP II, 125 & 186 Olr. cf. báes, Ir. baois, baos ‘folly, rage; lust (fr. *bhoist-); MHG ber, OS bêr, OE bār, Ger. Beier ‘boar’; OCS R bésü, bës ‘demon’; Li. baisüs ‘horrible’; baisas “horror, demon’, baisà ‘terror’
4793:ghoisos, ios, is ‘fiery, vigorous, intense; vigour, spirit, fire. Cf. ghoist-, ghoit-, and WP I, 527 Skt. hesáh ‘swift, strong’; hesas, n. ‘vigour’; Mir. gáes, Ir. gaos, gaois (wisdom, skill'. Mod. also “spirit, dash’, fr. *ghoist-, q.v.); ON geis ‘spirit, dash"; OE gar Ø), id.; Go. cf. us-gáisnan ‘horrify’; e-gde in geisnan "be horrorstruck'; Li. gaisas “flash, blaze’; Latv. gaišs “bright; light; gaiss “air? Cf. Li. (variant) gaisras *blaze; dash?
9998:loisos (loisós, óm) (1) ‘loam, clay? ON Je, m. leir; n., id.; leira, f. tmudflat'; Sw. ler, n., lera, f. ‘clay’; OPr. laiso (for *laisa clay”); Li. cf. laistai, mpl. ‘stucco’
11028:moiks- (o-gde form of type miks-, q.v.). WP II, 245 Skt. meksayami, tr. ‘stir; Gk. cf. aor. (e-gde) é-meixa ‘I mixed; MHG meisch, adj. 'in- fused; meisch, sm., G Meische, f. ‘mash’; Ger. cf. meischen, v. Cinfuse': E dial. to mash, id.); OCS měšọ, mésiti & mésati, v. ‘mix’; Li. mai&aü, ýti, id.; Late maisu, it, id.; (e-gde in) Li. miefiü, ti, v. id. and in OCz. mí&&ti, id.; (z-gde in) Ir. meascaim, W mysgu, id. and in OS mehs, n. ‘dung’. Grade uncertain in Arm. mec, gs meçi, meciv, i-st. trot, mould’; mesim, v. ‘grow mouldy’. A variant of type *moiK- occurs in OE mah ‘wanton, shame- less, but see moigh-. Extn. in Li. maisalas, m. “medley”
12038:oisa, io 'shaft-pole'. Cf. oios (2) Skt. ísa, f. id.; Av. isa, f. id.; LW in Finn. aisa, id.
13309:peik- (pik) and next Skt. pé$ah, m. 'ornament'; Av. paešō, m. id. (and ‘shape’); Ober cf. paisiya, f. ‘writing’; Oss. fes, s. (Tuck?. See note on poigh- "mark: Tokh. A cf. paik-, v. ‘write’; Gk. cf. poikilós ‘variegated’; Lat. picus, m. pica, f. (magpie; woodpecker’. Lit. ‘variegated or ‘pied’ bird"); Umb. peico, m., peica, f. as Lat., beside peica, adj. f. ‘brindled’; OS féh, MHG vech, gs: véhes, adj. ‘motley’; G cf. Feb, s. (“sable- skin’, lit. *mottled"); Go. cf. filu-fáihs, adj. *many-coloured'; Li. paiSas, paiSà, m. f. and -0s, fpl. ‘smudge, charcoal mark, blot’; cf. also piesà 'smut'; paisüs ‘smutty’. (OE fina, wm. *woodpecker' seems to represent a type *peiKno-)
20237:uidolos, uidulos “evident, perceptible, per- ceptive, clever'. Cf. ueid-, cpds. Skt. vidurah “clever”; Ir. (?) eol, gs: iuil, s. ‘knowledge’; OE cf. fore-witol *foreknowing'; EME wittol, sm. ‘cuckold, complaisant hus- band’; ON cf. á-vitall, -vitull, m. ‘hint’; Li. cf. pa-vidalas, m. ‘form, figure, appearance’
=== SYN share ===
=== WLD band3 ===
```


## [2026-09-04T18:52:31.037Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN diet entries ===\"; grep -n -i 'diet' KLN_1966.txt | head -20\necho; echo \"=== SKT DIET body ===\"; grep -n -i 'DIET (1)\\|Diet, a way\\|Diet,\\ba\\|mode of living\\|way of living' SKT.txt | head -10\necho; echo \"=== WLD Bd1 ai geben ===\"; grep -n -i 'geben, zuteilen\\|zuteilen' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T18:52:31.128Z] TOOL RESULT

```
=== KLN diet entries ===
577:diet.
8324:comedian,  n.  —  F.  comedien,  fr.  comedie ,  ‘com- medy’.  See  comedy  and  -an. comedienne,  n.  —  F.  comedienne,  ‘an  actress  in comedy’,  fem.  of  comedien.  See  prec.  word, comedietta,  n.,  a  short  comedy.  —  It.  (now commedietta),  dimin.  of  comedia  (now  comme- dia),  ‘comedy’,  fr.  L.  edmoedia.  See  comedy, comedo,  n.,  blackhead  ( med .)  —  L.  comedo,  ‘a glutton’,  rel.  to  comedere,  ‘to  eat  entirely  up’, fr.  com-  and  edere,  ‘to  eat’.  See  edible  and  cp. comestible.
8988:contradictory,  adj.  —  Late  L.  contradietorius , ‘containing  a  contradiction  or  objection’,  fr.  L. contradictus,  pp.  of  contradicere.  See  contradict and  adj.  suff.  -ory.
9474:coverture,  n.,  the  status  of  a  married  woman  (law). —  OF.  (F.  couverture),  fr.  covert,  pp.  of  covrir. See  prec.  word  and  -ure. covet,  tr.  and  intr.  v.  —  Fr.  OF.  coveitier,  fr.  VL. *cupidietdre,  fr.  *cupidietas,  altered  fr.  L.  cupi- ditds,  ‘desire’,  fr.  cupere,  ‘to  desire’ ;  see  Cupid. OF.  coveitier  soon  became  conveitier  (F.  con- voiter)  on  analogy  of  the  numerous  words  be¬ ginning  with  con-.
10680:All  these  words  come  fr.  *deyew(o)-,  ‘shining’, which  derives  fr.  I.-E.  base  *dei-,  *deyd-,  *di-, dya-,  ‘to  shine’,  whence  also  OI.  di-de-ti,  ‘shines, diva,  ‘by  day’,  di-vasah ,  ‘heaven;  day’.  Arm.  tiv, ‘day’,  Gk.  Searo, ‘seemed’,  SrjXo?,  Homeric  SeeXo^ (for  *Slt-eXoc),  ‘visible,  clear’,  L.  dies,  OIr.  die, W.  dyw,' day',  OIr.  in-diu,  W.  /ic-rfa'yH', ‘today’. Cp. Adelia,  adelo-,  adieu,  adjourn,  Bhumi  Devi,  daiva, deiform,  deify,  deodand,  deodar,  devadasi,  Dewali, dial,  Diana,  diary,  dies  non,  diet,  ‘assembly’,  Dios- ma,  Dis,  dismal,  diurnal,  diutumal,  diva,  Dives,  di¬ vine,  Dorothea,  Dyaus,  eudiometer,  joss,  journey, Jove,  jovial,  Jupiter,  Lent,  meridian,  prie-dieu, quotidien,  sojourn,  Tuesday,  Zenobia,  Zeus, deject,  tr.  v.,  to  cast  down.  —  L.  dejectus,  pp.  of dejicere,  ‘to  throw  down,  drive  off,  lower,  let down;  to  humble’,  fr.  de-  and  jacere  (pp.  jac- tus),  ‘to  throw’.  See  jet,  ‘to  spirt  forth’,  and  cp. words  there  referred  to.  For  the  change  of  Latin d  (in  jactus)  to  e  (in  de-j&ctus )  see  accent  and  cp. words  there  referred  to.
11361:dies  non,  a  day  on  which  no  legal  business  is carried  on.  —  L.  dies  non  ( juridicus ),  lit.  ‘a  not juridical  day’.  L.  dies,  ‘day’,  derives  fr.  I.-E. base  *dei-,  *deya-,  *di-,  *dya-,  ‘to  shine’.  See deity  and  cp.  dial,  diary,  diet,  ‘assembly’,  diur¬ nal,  diuturnal,  journal,  and  the  second  element in  hodiernal,  meridian,  Midi,  quotidian.  For  L. non,  ‘not’,  see  non-.
11362:diet,  n.,  a  parliamentary  assembly.  —  ML.  dicta, ‘an  appointed  day’  (whence  also  F.  diete,  ‘par¬ liamentary  assembly),  fr.  L.  dies,  ‘day’  (see  dies non):  prop,  a  loan  translation  of  G.  Tag,  ‘day’, in  the  sense  of  ‘parliamentary  assembly’.  For sense  development  cp.  landtag  and  words  there referred  to.
11363:diet,  n.,  fare,  food.  —  ME.  diete,  fr.  OF.  diete (F.  diete),  fr.  L.  diaeta,  ‘mode  of  living’,  fr.  Gk. Slaixa,  ‘the  office  of  an  arbiter;  mode  of  living; dwelling,  abode’,  back  formation  fr.  SLaixav, ‘to  maintain,  support’,  which  is  formed  fr.  81- (form  of  Sia  before  a  vowel’)  and  aloa  (for ♦atria),  ‘share,  lot,  destiny’.  See  dia-  and  etio-. Derivatives:  diet,  tr.  v.,  to  prescribe  a  diet,  diet¬ ary,  adj.,  diet-er,  n.
11364:dietetic,  also  dietetical,  adj.,  pertaining  to  diet.  — —  Gk.  8iaiT7]Tix49,  ‘of,  or  pertaining  to,  diet’, fr.  Siaixa.  See  prec.  word  and  -ic.
11365:Derivatives:  dietetical-ly,  adv.,  dietet-ics,  n. dietician,  dietitian,  n.,  an  expert  in  dietetics.  — Formed  fr.  diet,  ‘fare,  food’,  on  analogy  of phys-ician.
11478:dinus,  n.,  vertigo  (med.)  —  Medical  L.,  fr.  Gk. STvo?,  ‘a  whirling,  rotation,  vertigo’,  which  is rel.  to  SfvT),  ‘a  whirling’,  STveio,  Sivsuto,  ‘I  make whirl  or  spin  round’,  StvEupoi,  ‘a  whirling round’,  Sispai,  ‘I  hasten  away’,  and  prob.  cogn. with  OI.  diyati,  ‘flies,  hovers’,  Lett,  diet,  ‘to dance’,  OIr.  dian,  ‘swift,  rapid’.  Cp.  dinic  and the  second  element  in  scotodinia. diocesan,  adj.,  pertaining  to  a  diocese.  —  F.  dio- cesain,  fr.  diocese.  See  next  word  and  -an. Derivative:  diocesan,  n.
13744:‘I  take’,  e^outo?,  ‘picked,  choice’,  al'cuo?,  ‘auspi¬ cious,  opportune’,  and  cogn.  with  Avestic  aeta-, ‘share,  lot,  due’,  Oscan  aeteis  (gen.),  ‘of  some¬ body’s  part’,Toch.  B  ai-,  ‘to  give’  (lit.  ‘to  allot’). Cp.  diet,  ‘fare’.
20673:kieserite,  n.,  a  hydrous  magnesium  sulfate  (mi¬ neral.)  —  G.  Kieserit,  named  after  Dietrich  G. Kieser,  president  of  the  Academy  of  Jena  (died in  1862).  For  the  ending  -it,  which  goes  back  to Gk.  see  subst.  suff.  -ite.
21102:landtag,  n.,  the  legislative  assembly  in  German states.  —  G.,  lit.  ‘day  of  the  country’.  See  land and  day.  For  sense  development  cp.  diet,  ‘par¬
22585:maieutic,  adj.,  serving  to  elicit  ideas  (said  of  the Socratic  method  of  teaching). — Gk.  p.aieimx6(;, ‘pertaining  to  midwifery,  obstetric’,  fr.  pateoe- a-SIai,  ‘to  act  as  midwife’,  fr.  pafa,  ‘mother, nurse,  midwife’,  fr.  pa  (voc.),  ‘mother ,  from infants’  babbling  *md-,  whence  also  Dor.  Gk. parqp,  Gk.  pr)rqp,  ‘mother’,  and— with  redu¬ plication — papp7],  ‘mother’.  See  mother, ‘female  parent’,  and  cp.  mamma,  'mother’, maigre,  adj.,  containing  neither  flesh  nor  its  juices (said  of  articles  of  diet).  —  F.,  ‘meager  .  See meager.
23706:—  F.  See  next  word  and  -age. metayer,  n.,  one  who  cultivates  the  land  for  a share  (usually  a  half)  of  the  yield.  —  F.,  fr. MF.,  fr.  OF.  meteer,  fr.  ML.  medietarius,  fr.  L. medietas,  ‘middle,  place  in  the  middle,  half  ,  fr. medius,  ‘middle’.  See  media,  ‘voiced  stop  con¬ sonant’,  and  cp.  moiety.
24071:mitten,  n.,  a  kind  of  glove.  —  The  word  lit.  means ‘divided  in  the  middle’,  fr.  ME.  meteyn,  fr.  OF. mitaine,  fr.  VL.  *medietana,  ‘divided  in  the middle;  half-glove’,  fr.  L.  medius,  ‘middle’.  See media,  ‘voiced  stop  consonant’,  and  cp.  prec. word.
24167:moidore,  n.,  a  Portuguese  gold  coin.  —  Corrup¬ tion  of  Port,  moeda  de  ouro,  lit.  ‘money  of  gold’, fr.  moeda,  ‘money’  (fr.  L.  moneta,  ‘mint, money'),  the  prep,  de,  ‘from,  of’  (fr.  L.  de,  ‘from, away  from’)  and  ouro,  ‘gold’  (fr.  L.  aurum ).  See mint,  ‘place  for  coining  money’,  de-  and  aureate, moiety,  n.,  a  half.  —  ME.  moite,  fr.  MF.  moiti (F.  moitie),  fr.  OF.  meitiet,  fr.  L.  medietatem, acc.  of  medietas,  ‘the  middle,  a  half’,  fr.  medius, ‘middle’.  See  media,  ‘voiced  stop  consonant’, and  subst.  suff.  -ty.
27911:pellagra,  n.,  a  chronic  disease  caused  by  a  defi¬ ciency  of  nicotine  acid  in  the  diet.  —  It.,  a  hy¬ brid  coined  fr.  L.  pellis,  ‘skin’,  and  Gk.  dtypa, ‘a  catching,  seizure’.  See  fell,  ‘hide’,  and  chiragra. Derivatives :  pellagr-ic,  pellagr-ous,  adjs. pellet,  n.,  a  small  ball.  —  ME.  pelote,  pelet,  fr. OF .  (=  F.) pelote,  ‘ball’,  fr.  VL.  *pihtta,  dimin. of  L.  pila,  ‘ball’  (hence  lit.  meaning  ‘ball  of  hair’), which  is  rel.  to  pilus,  ‘hair’.  See  pile,  ‘hair’,  and cp.  pelota.
32152:regimen,  n.,  1)  system  of  diet;  2)  government (gramm.)  —  L.,  ‘rule,  guidance,  government’, fr.  regere.  See  regent,  adj.,  and  cp.  prec.  word and  realm.

=== SKT DIET body ===

=== WLD Bd1 ai geben ===
5069:2. ar- oder er- „zuteilen; (med. ) an sich bringen“. 
6498:zuteilen, doch ist ev- noch nicht gekliirt (EinfluB der Praep. iv ist doch 
6791:tJber die nicht als r-Bildungen unserer Wz. zuzuteilenden anord. ar 
8104:sicher zu *nem- „zuteilen : nehmen“) steht jetiit, jenit das nicht je- aus e- 
8868:Ai. Wb. 13, Brugmann IF. 37, 240 f.; nicht zu *ar- .,zuteilen‘‘); 
14478:austrocknen“ kaum unserer Wz. zuzuteilen ist, s. Kluge 8 s. v. Fick III 4 
14566:pnvinati „kehrt sich woran, verehrt. huldigt“ zuteilen will ; wenn mit Recht. 
15619:„Ding, Sache“). will Prusik aaO. unserer Wz. zuteilen. da auch slav. reeb 
17583:serp- „Sichel“) zuzuteilen ist. 
18485:,,drehen, winden" zuteilen mochte) und Persson Beitr. 509 Anm. 1 . An
```


## [2026-09-04T18:52:43.935Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i 'aivvpai\\|αἴνυμαι\\|ai-mulus\\|aemulus\\|Anteil.*Schicksal\\|aeteis' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo ---; sed -n '/^\\s*3\\. ai-/,+20p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -30"
}
```


### [2026-09-04T18:52:45.796Z] TOOL RESULT

```
322:0. aeteis ..partis', a ittlihn ..portionum"; 
10773:Binz aaO., Yf. LEWb. 2 u. aemulus ), und die lett. Anwendung auf faules 
---
3. ai- ..brennen, leuchten" (s. bes. Prellwitz BB. 23, 65 ff.). 

ai-s- : lit. diskus , woneben schwundstufig alit. isJcits . deutlich“, dazu wohl 
abg. jasno adv. .clare", russ. jdsnyj ..licht, klar 1 usw. [das kaum nach 
Uhlenbeck Ai. Wb. 236 als *aildno- mit ai. yagas n. .Anselien, Wiirde, 
Herrlichkeit, Ehre, Ruhm" unter einer Basis aiek- zu vereinigen ist, sondern 
*ai-s-k-no- mit ausgedrangtem k ist, Pedersen IF. 5, 43, Berneker 276 
— der als weniger wahrscheinliche Herleitung die aus aiclh-s-no- erwagt]. 

Dasselbe ai-s-k- in russ. dial, jaska, dem. jdsocka . klarer Stern", poln. 
jaskry, jashawy ..blendend, funkelnd", wr. jaskorka . Fiinkchen", klr. jas- 
kryty sa ..funkeln", is-k- in abg. usw. iskra ..Funke" (Berneker 433 m. 
Lit., KZ. 31, 15). 



3 


Yielleicht auch in awn. eishra ,.vor hitziger, leidenscliaftlicher Erregruno- 
wiiten", nisi, t'sira auch von brennendem Schmerz, und im spatlat. (aus
```


## [2026-09-04T18:52:49.236Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '300,340p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T18:52:49.293Z] TOOL RESULT

```
liber aho g auch Prellwitz 38 — die Form dmjvtjvavio Horn, spricht gegen 
alten Diphthong; es ist also gegen Osthoff [BB. 24, 199 ff.] vielmehr mit 
Stolz [Wiener Stud. 25, 133 ff.] als /o-Ableitung der Negation av- zu be- 
trachten) bleibt fern. 

tiber dt. Eid usw. s. u. ei- . gehen". 

S. auch *ai-to~, ai-ti- „Anteil“. — - Fick 1 3 4 113. 

ai-to-, ai-ti- .Anteil", vermutlich nach Fick I 4 345 zu ai- ..packen" (..das, 
was jeder an sich rafft ). 

Gr. aioa (*ahm) . Anteil, Schieksal", horn, toy, besser I'ooy ,.der gebiik- 
rende Anteil ', I'ooaodai ‘ y.hjoovodac. Aeothoi Hes. ; ai’oiog . gutes Geschick 
verheifiend, giinstig cuoiiiog ..yom Schieksal bestimmt, gebiihrend ', avcu- 
at,u6co ,.amvenden, gebrauchen, verzehren" (s. dazu Boisacq 59, Fraenkel 
KZ. 42, 236), aiovf.iva.co . spreche Recht, herrsche" ; dtaadco (vielleieht dis- 
similiert aus *dtaindco) . bin Sehiedsrichter, leite ; teile das Leben ein = 
fiihre eine gewisse Lebensart; schreibe ein gewisses MaB im Essen und 
Trinkenvor ', daher diaira . Schiedsrichteramt ■ und . Lebensweise, Lebens- 
einteilung ’. Lit. bei Boisacq 184. 

0. aeteis ..partis', a ittlihn ..portionum"; 

av. atta- ,.der gebiihrende TeiL (..Strafe"; dual . Schuld und Strafe ) 
(Bezzenberger BB. 4, 322; Fick; Bartholomae IF. 12, 139, Airan. Wb. 1 1 f.). 

Aus dem Griech. hierher wohl auch airiog . schuldig“ (. Teilnehmer an 
einem Diebstahl ?), woraus spiiteres ahia ..Ursache"; auch ahsco, ahiCco 
..fordere" als . seinen Anteil verlangen". 

Anmerkung: Uber gr. ohog ..Los, Geschick' s. *ej r ,gehn“, zu welcher 
Wz. neuerdings (s. Brugmann IF. 37, 241 f.) auch lat. fitor, alat. oitier, 
osk. liittiuf ..NutznieBung ' gestellt wird (wofiir unter Berufung auf dv- 
aioifiom . gebrauche, wende an" Zugehorigkeit zu ai-to- ervvogen worden 
war; vgl. Bezzenberger, Osthoff BB. 24, 209 und die Lit. bei Walde LWb. 2 
s. v. utor). Hierher aber air. dis, ties . Alter ", cymr. oes und oed ds., s. u. aiu-. 

3. ai- ..brennen, leuchten" (s. bes. Prellwitz BB. 23, 65 ff.). 

ai-s- : lit. diskus , woneben schwundstufig alit. isJcits . deutlich“, dazu wohl
```


## [2026-09-04T18:52:56.422Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-04T18:52:56.430Z] TOOL RESULT

```


```


## [2026-09-04T18:53:00.476Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88",
 "prompt": "Give the full Persian etymology sections for آهو: both the 'gazelle' sense and the 'fault, defect, blemish' sense. Quote the Middle Persian, Avestan and Proto-Iranian forms and any cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


### [2026-09-04T18:53:07.308Z] TOOL RESULT

```
# Persian Etymology for آهو

Based on the Wiktionary content provided, here are the two Persian etymology sections:

## Etymology 1: Gazelle/Deer Sense

The entry states that آهو derives "From Middle Persian [Term?] (/⁠āhūg⁠/), ultimately from Proto-Indo-European *h₂eḱus ("sharp, swift")." The source lists cognates with Northern Kurdish *ask* and Baluchi *آسک* (ásk).

The references cited are:
- Steingass (1892): *A Comprehensive Persian–English dictionary*
- Dehkhoda (1931–): *Dehkhoda Dictionary*
- MacKenzie (1971): *A concise Pahlavi dictionary*
- Horn (1893): *Grundriss der neupersischen Etymologie*

## Etymology 2: Defect/Imperfection Sense

The Wiktionary article notes: "(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

This second sense is documented only through a 10th-century citation from Ferdowsi's *Shahnameh*, where "آهو گرفت" means "have grown faulty," but no formal etymological derivation, Middle Persian ancestors, Avestan forms, or Proto-Iranian reconstructions are provided in the source material.
```


## [2026-09-04T18:53:12.801Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%87%DB%8C%D8%AF",
 "prompt": "Give the Persian etymology of ناهید (Nāhid): the Middle Persian and Avestan forms, the meaning ('Venus', 'Anahita'), and any cited sources."
}
```


## [2026-09-04T18:53:13.580Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/diet",
 "prompt": "Quote the full etymology of 'diet' (both senses), especially the chain from Greek diaita / diaitan and the PIE root *ai- 'to give, allot'."
}
```


### [2026-09-04T18:53:17.860Z] TOOL RESULT

```
# Persian Etymology of ناهید (Nāhid)

## Middle Persian Form
According to the Wiktionary entry, the term derives from "Middle Persian _ʾnʾhyt'_ (anāhīd)," with the earlier Persian form being _اَنَاهِید_ (anāhīd).

## Meaning
The term has multiple related meanings:
1. **Anahita** - a figure from Iranian mythology
2. **Venus** - the planet in astronomy
3. A female given name

## Sources
The entry does not cite specific Avestan sources. It notes cognates in Northern Kurdish (_Nehîda_, _Nehî_) and Central Kurdish (_ناهیە_, _ناهێ_), suggesting the term's broader linguistic heritage across related languages, though primary etymological sources are not explicitly referenced in this Wiktionary article.
```


### [2026-09-04T18:53:22.202Z] TOOL RESULT

```
# Etymology of "Diet"

## First Sense (Food/Regimen)

The noun meaning "regular food" derives from Old French *diete*, Medieval Latin *dieta*, and ultimately Greek *diaita* meaning "way of life, regimen, dwelling." According to the source, this Greek term traces back through *diaitasthai* "lead one's life" and *diaitan* "separate, select" (food and drink).

The etymological chain continues: *diaitan* is described as "apparently a frequentative of *\*diainysthai* 'take apart,'" which combines *dia* "apart" plus *ainysthai* "take." The source attributes this final element to "PIE root *\*ai-* (1) 'to give, allot.'"

By the late 14th century, the word acquired the sense of "customary way of eating" and "food regulated by a physician." The adjective meaning "slimming, having reduced calories" emerged by 1963 in American English.

## Second Sense (Assembly)

The noun denoting "assembly of delegates" originated in the mid-15th century from Medieval Latin *dieta*, though this sense associates with Latin *dies* "day" rather than the food sense, despite sharing a Greek root in *diaita*.
```


## [2026-09-04T18:53:31.617Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/anahid",
 "prompt": "What does the article say about the etymology and meaning of the name Anāhitā / Anāhīd / Nāhīd — the Avestan form anāhitā- 'immaculate/undefiled', the element āhita-, the Middle Persian Anāhīd, New Persian Nāhīd, and the identification with the planet Venus?"
}
```


## [2026-09-04T18:53:31.698Z] TOOL CALL #41: WebSearch

```json
{
 "query": "Avestan āhita- \"defiled\" etymology anāhitā \"immaculate\" Bartholomae Middle Persian āhōg New Persian āhū fault"
}
```


### [2026-09-04T18:53:33.474Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T18:53:36.706Z] TOOL RESULT

```
Web search results for query: "Avestan āhita- "defiled" etymology anāhitā "immaculate" Bartholomae Middle Persian āhōg New Persian āhū fault"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T18:53:43.086Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Anahita",
 "prompt": "Give the etymology of Anahita: the Avestan form 𐬀𐬥𐬁𐬵𐬌𐬙𐬀 (anāhita) and its analysis (an- privative + āhita- 'defiled/soiled'), the Old Persian and Middle Persian forms, and the Greek Anaitis."
}
```


## [2026-09-04T18:53:45.471Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CE%B1%CE%B9%CF%84%CE%B1",
 "prompt": "Give the Ancient Greek etymology of δίαιτα and of διαιτάω / διαιτᾶν: the analysis into δια- + the root of αἴνυμαι / αἶσα, the PIE root cited, and any note that the etymology is uncertain (e.g. Beekes)."
}
```


### [2026-09-04T18:53:49.821Z] TOOL RESULT

```
# Etymology of Anahita

Based on the Wiktionary entry provided, here's what's documented about Anahita's etymology:

## Available Information

The page states the word comes "From Old Persian _𐎠𐎴𐏃𐎡𐎫_ (a-n-h-i-t /⁠anahita⁠/)."

The entry also lists related forms across languages:
- **Middle Persian**: ʾnʾhyt' (anāhīd)
- **Modern Persian**: آناهیتا (ânâhitâ) or ناهید (nâhid)
- **Armenian**: Անահիտ (Anahit)
- **Ancient Greek**: Ἀναῖτις (Anaï̂tis)

## Limitations

Unfortunately, the Wiktionary source does **not** provide the detailed etymological analysis you're requesting. The page explicitly notes: "(This etymology is missing or incomplete. Please add to it...)" 

The component breakdown (an- as privative prefix + āhita- meaning 'defiled/soiled') and the Avestan form you mention are not included in this particular document. To find that linguistic analysis, you would need to consult more specialized etymological resources or academic sources on Indo-Iranian languages.
```


### [2026-09-04T18:53:51.156Z] TOOL RESULT

```
# Ancient Greek Etymology of δίαιτα

## Etymology of δίαιτα

According to the Wiktionary entry, δίαιτα is a "Nominal formation from _δῐαιτᾰ́ω_ (dĭaitắō, 'to treat, handle')." The entry traces this to the PIE root *dwís.

## Etymology of διαιτάω

The page indicates that διαιτάω is the verbal form from which the noun derives, but it does not provide a detailed breakdown into component morphemes like δια- plus a root related to αἴνυμαι or αἶσα.

## Uncertainty Note

Robert S. P. Beekes's *Etymological Dictionary of Greek* (2010) is cited as the reference source. However, the entry does not explicitly flag the etymology as uncertain, suggesting Beekes may offer a relatively confident analysis, though consulting his work directly would clarify any reservations he expresses about this derivation.
```


## [2026-09-04T18:53:58.692Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%B1%CE%B9%CF%84%CE%AC%CF%89",
 "prompt": "Give the full etymology section of διαιτάω (diaitaō): its morphological analysis, any connection to αἶσα / αἴνυμαι, the PIE root given, and whether the etymology is called uncertain. Also give the meanings/glosses listed."
}
```


### [2026-09-04T18:54:06.353Z] TOOL RESULT

```
# Etymology of διαιτάω (diaitaō)

## Morphological Analysis

The word is composed of two elements: either **δῐᾰ-** (dĭă-, "through") per Bailly, or **δῐ-** (dĭ-, "twice, double") per Beekes, plus **\*αἰτᾰ́ω** (\*aitắō), described as a frequentative of **αἴνῠμαι** (aínŭmai, "to take").

## PIE Root

The entry indicates the Proto-Indo-European root **\*dwís** as relevant to this word's formation.

## Connection to Related Words

The etymology notes a comparison to **αἰτέω** (aitéō, "to ask for"), linking the verb to a semantic field involving taking and requesting.

## Uncertainty Status

The etymology is **not explicitly marked as uncertain**, though the presentation of alternative analyses (Bailly vs. Beekes) suggests scholarly debate about the precise prefix interpretation.

## Glosses and Meanings

The verb carries four primary meanings:

1. To treat (handle, deal with, or behave towards in a specific way)
2. To lead one's life; to live (mediopassive voice)
3. To arbitrate; to regulate
4. To reconcile
```


## [2026-09-04T18:54:20.921Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\ndata=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=data.split('\\f')\nl=leaves[104]\ni=l.find('an-ähita-')\nprint(l[max(0,i-200):i+2500])\nEOF"
}
```


### [2026-09-04T18:54:22.992Z] TOOL RESULT

```
  (fem.  °ta-)  'nicht enilmt':  ytzi  sl  bavaitUi  °ta  xsnütä  ainilä al/nsia  .  .  fravasayi  Yt/^.63;  30,  34.
np.  vgl.  Ssird  'gekränkt'. g.  anäsc  Y.  44-  14=  s.  unter  ä  niie.
•  j.  an-ähita-,  p.  *an-ähita-'*  Adj.  (fem. 'tä-)  'woran  kein  Fleck,  kein  Makel  ist, haftet,  makellos':  mihnm  .  .  yim  yazata haemö . .  't^m  'Is  "tili  parü  bartsm^n  °tayst pars  zaohräyat  'talibyS  farS  vayzibyS  Yt. JO.88;  —  tiilrtm  .  .  dßrät  vyavantsm bämtbyS  raoxsnibyi}  'iaäbyJ'^X.S.z;  —  'ta F. 5.  o)  bes.  von  der  Ar>dvT  (sd.): anduya  äpS  'tayh  Ny.  4,0,  Vr.  7.5;  Yt. /.  2i;  ^  sonst  mit  sQra-  Adj,  verb.;  ap?in andvJm  sürqm  Hqm  Y.  Ö5.  i  usw.'';  — aridvt  süra  °ta  Y.ö'5.4  USW.";  —  arpdvl Sure  'te  (VS.)  YL5.18  usw.'\  A)  als weibliche  Gottheit*',  Avamfi*:  D  «*«/'a*- masdä  "atfh'C  (=  anahiti')  Uta  mitriß mäm  pätuv  Am.  4;  Am.  j'.
*)  S.  dam  unter  andtii-  und  Cumont,  Pauly- Wis50w»  RE.»  I.  2030.
Pü,  (m  F.  5):  anä/wirnil,  (sonst):  annddtn, Npü.;  fSa.  —  ■>  In  mangelhafter  Rechtschrei- bung, s.  unter  A.  —  ')  Slveri.  unter  atidvi-. —  i>  Das  ein  ir.  *a'iäAtlis  vorauszusetzen scheint. j.  '"anSi/hä  P.  141  s.  unter  anaAü',
•  ],  an-azah-  Adj.  'der  keiner  Bedrängung ausgesetzt  ist,  keine  Not  kennt";  mi^r^m . ,  yet'ihe  mag'i^anpm  .  .  °zS  Yt-jo.44.
•  j.  ajnika-  m.  i)  'Antlitz' 1  tanüm  .  . yeühe  'ks  bräzaiti  yaia  ..  Yt. /o.  143; F.jd,  2)  'Stirn-,  Vorderseite":  aspahe ..  yim  ttpairi  'tum  sanat  amS  Yt.  14. 9.  a)  bes.  des  Heeres,  'Front'  (nur Komp.).
KompE.  —  ai.  äHTia-  n.,  kuid.  atii,  np.  vgl. fS-äm.  —  lEt.  s.  JScHMtDT  Plur.  390.  —  Pü, : äaii  (so!  Päi.  A^,  für  an  dk  r«  änii).
•  j.  ainita-  Adj.  (fem.  'tä-)  'nicht  ver- gewaltigt, gekränkt':  x/aüiA  °iä  aibtfta  .. Jravasayö  Yt/j.  51;  34,  63,
Durch  Haplol.  (S  306)  aus  *aH-imta-,  PPfP. zum  V.  atit:  —  Vgl.  ainitay:
•  j.  ainitay-  1)  f.  'Nichtvergewaltigen, -kränken'  sva.  "milde  Behandlung,  Milde': '■tsit  F,  7;  —  'Isis  F.  7;  —  hada  . .  'ticä Y.  5Ä'.  4.  a)  Adj,  'nicht  kränkend' ;  'tis ai^  *vaxs  P.  26.
Durch  Haplol.  (Sjoff)  aiis*d«-ini('>>;  s.  unter intay.—  Vgl.  ainila:  —  Pü.  (in  l):  akimh^\ (102):  akin.  —  ')  Anders  Leumahn  EtWb.  34, —  »}  Für  aimlöii  hat  Pü. :  dak  n  aa,  erl. :  ax^äsla- kih  mit  Npü.  gaili  'Beiller';  s.  dazu  Haug ZPGl.  59,  PPGl,  an.
•  j.  ain-iJJat  Adv.  'nicht  hier':  {6atca üitiihatca  ioatca  Y.57. 33. -""^
Vgl. 'unter  1%  —  Pü.:  anflar.
•  j.  "ainidkitn '>  nazS"  t:i.66:  -?-, Pü.:   vetiU  mSyiin  'Atemausgang'').  —   i)  T hat
```


## [2026-09-04T18:54:36.945Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88' \\\n 'https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%87%DB%8C%D8%AF' \\\n 'https://en.wiktionary.org/wiki/Anahita' \\\n 'https://www.etymonline.com/word/diet' \\\n 'https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CE%B1%CE%B9%CF%84%CE%B1' \\\n 'https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%B1%CE%B9%CF%84%CE%AC%CF%89' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 38 (book p.8): roots Ahu and Ai — Persian ahu/nahid, Greek diaita, English diet' 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T18:54:40.572Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/844b9204c5629849.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/16b22d85686859b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cffbe374515ee25b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f231cbb5475c634d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa1b0bc8341659d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b3ebb78d9ac530e.txt
```


## [2026-09-04T18:54:59.139Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null; mkdir -p data/verification/sources/refs/ocr/BQT; cat > data/verification/sources/refs/ocr/BQT/72.vision.txt <<'EOF'\n# Borhan-e Qate', ed. Mo'in, printed page 72 (vol. 1)\n# read by Claude from the archive.org leaf image\n# https://iiif.archive.org/iiif/borhan-ghate-v1%24282/full/1200,/0/default.jpg\n# (item borhan-ghate-v1, leaf n282; running head \"-۷۲-\" confirms printed p.72)\n# read 2026-09-04 for data/verification/page-38.json (root \"Ahu\")\n\n--- main column, entry آهو (continuation from p.71) ---\nعیب را نیز گفته اند ۱ خواه با مردم باشد و خواه با چیزهای دیگر - و بمعنی رم باشد که از\nرمیدن است چه آهوبی رمیدگی را گویند - و بمعنی فریاد و آواز بلند هم آمده است - و نام\nمرضی و علتی هم هست که آنرا بعربی ضیق‌النفس خوانند - و بطریق استعاره چشم را نیز\nآهو میگویند - و شاهد و معشوق را هم گفته اند .\n\n--- footnote 1 (Mo'in's etymological note, foot of p.72) ---\n۱ - مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین،\nپلید و ناپاک، پهلوی âhôk (عیب) «مناس ۲۶۵». خاقانی در بیت ذیل به هر دو معنی آهو که\nغزال و عیب باشد اشاره کند:\nیعنی آن جانور که زاید مشک        نامش آهو و او همه هنر است.  «یشت ۱ ص۱۶۵»\n\n--- footnote 5 (same page) ---\n۵ - آهومند - مرکب از: آهو بمعنی عیب + مند پسوند اتصاف؛ بمعنی مریض - معیوب -\nمغزآهومند، مختل، مخبط\nEOF\necho written; wc -l data/verification/sources/refs/ocr/BQT/72.vision.txt"
}
```


### [2026-09-04T18:54:59.229Z] TOOL RESULT

```
ARY
BQT
IRN
PLA
written
21 data/verification/sources/refs/ocr/BQT/72.vision.txt
```


## [2026-09-04T18:55:09.738Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT aeta ===\"; grep -n 'aeta-\\|aetä\\|gebührende  Teil\\|gebührende Teil' BRT.txt | head -10\necho; echo \"=== SKT diet ===\"; grep -n -i 'diaita\\|Diet, a prescribed\\|Diet, food\\|Diet (1)' SKT.txt | head -10\necho; echo \"=== FSD vol1 diet ===\"; grep -n -i 'diaita' FSD_vol1.txt FSD_vol2.txt WEB_vol1.txt | head -10"
}
```


### [2026-09-04T18:55:09.846Z] TOOL RESULT

```
=== BRT aeta ===
2502:II  'a-  No.  —  ^aeta-  Et  I  i  a.  ii
2527:•  j,  "acta-  m.  'das  gebührende  Teil',  sva.!.,    'tat    :^ar3nS   YL/<>.45— 51;  Y./p.ii,
2530:17  ^aeta-  II 2  z  b  —  aetavant-  18
2540:das  die  fehlenden  NSm.  und  f.  zu  ^aeta-
2549:1 5  3aeta-  H  I  3  b  —  %cta-  II  2  2  a.  16
2558:17  Jaeta-  U  2  a  b  —  aetavant-  i8
3496:•  j.  apa-kava- 1 )  Adj,  'der  hinten,  auf  dem Rücken  einen  Höcker  hat':  mit  ml  aeta- yiisäl  zao^rayä  /mnharintu  frakavö  nttl 'vB  Yt  5.  93.  2)  m.  Name  fUr  solches Gebrechen:  mä  (a%ra)  'vö  2.  29.
4489:•  j.  an-upaeta-  Adj.  'noch  nicht  zu  be- gatten, noch  nicht  reif  fiir  — '  (Gen.),  von Mädchen:  ydi  kainina  °ta^'>  masyänqm "Mädchen,  die  noch  nicht  reif  sind  für Männer"  Yt.Z/.sS;  S4.  J5-39-
6152:•  j.  a-Saeta-  Adj.  'der  Icein  Geld  hab arm':  saHavatö  ahmot  (nämL  pourum  fra- mraomi)  yä^a  °täi  "dem  vennöglichen (spreche  ich  einen  höheren  Wert  zu)  als dem  armen"  V.  4.47.
8900:•  j.  kaeta-  m.  —  ?  — ,  wohl  Bezeichnung feindlicher  Wesen:  tistrim  ,  .  yim  pailis' mar.mte  .  .  masy,l'a  parö  darAi'qttS  (sd.) "/n.vj  pars  druzinlö  ".  .  und  die  A".,  die zuvor  böslich  gehandelt  haben"  YL>V.  5.

=== SKT diet ===

=== FSD vol1 diet ===
```


## [2026-09-04T18:55:16.367Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i 'diaeta\\|di.eta' SKT.txt FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -10\necho \"--- SKT around DIE ---\"; grep -n -i '^DIET\\|DIET, ' SKT.txt | head"
}
```


### [2026-09-04T18:55:16.458Z] TOOL RESULT

```
FSD_vol1.txt:93084:nourishing  diet.  3.  [Archaic.]  Allowance  of  food;  ra- tion. 4f.  Allowance  for  expenses;  daily  pay,  as  of  a legislator.  [   <   F.  diete,  <   L.  diseta,  <   Gr.  diaila,  man- ner of  living,  diet.]  dl'etcf.
--- SKT around DIE ---
145:Diet.,  1851. Low  L, — Low  Latin ;  as  in  the  Lexicon
159:Diet.,  or  in  Widtyrcti. Swed.  dial.  —  Suedish   dialects;   as  in
1130:audit.  (L.)  Perhaps  from  L.  audiim, a  hearing:  but  in  Webster's  Diet,  it  is  uid to  have  arisen  from  the  use  of  the  3rd  pent sing.  pres.  audit,  he  hears.  — L.  audin,  to hear :  whence  also  attdi-tor.
5020:dietart,  to  dklate,  pre-
5047:Diet  (i\  regimen.  fF.-L.-Gk.)  M.  E. «//>/^.  —  O.  F.  (//>/^  Hnily  fnre.  —  I>nw  L. dieta,  diaia,  a  ration  of  food.*-Gk.  fljoira, mA.!c  of  life,  diet.
5048:Diet  {i\  %xx  n&scrnbly.  (F. -L.-GkO O.K.  diet,  *a  dietc,  parliament/  Cot.— Lx>w  L.  diatn^  a  public  assembly:  also  a mtion  of  food,  diet.  — Gk.  Sjaim,  a  mode  of life,  diet:  sec  Diet  (l)-  ^  The  pcaili.ir  use of  the  word  was  due  to  a  pcpnlnr  et>  mglogy which  connected  dtata  with  diet,  a  day we  even  find  diata  used  to  mean  '«  day's journey;'  Ducange.
7996:—  O.  F.  grri/ii  (Moisy.  Diet,  of  Nor- inau  patois') ;  also  grit'/  ^Gmlcfroy).  — Low  L.  (raiicuium,  L.  tratiiuia,  dimin. of  cratiSt  a  hurdle.  Dor.  Hence  M.  £. Xridi'n,  a  gridfile,  afterwards  turned  into griJiron,  by  confu&ioa  with  M.  E  irt  — \i.  iron*
14261:E lunge,  dive;'  Cot.  Formctl  from  a  Low ,.  piumbicart  •,  not  found,  but  verified  by Picard /iifrt^w/r,  to  plunge:  *ee  Diet,  «.  v. piombaf^.  A  frequentative  form  from  L. plumbum^  lead  ;  cf.  Ital.  piambare,  to throw,  hurl,  fall  heavily  like  lead,  from piombo^  lead.
16640:Scimet&r,  Cimet&r.  (F.  pr  Ital.  - Ters.  ?)  F.  cim^Urt^,  *%  scj'mitar;'  Cot. Cf.  Ital.  fd'mifarm,  '»  simitar,'  Florio, Prob.  from  Pcrs.  sAimskfr,  sAamsklr,  "a cimeter.'  Rich.  Diet,  p.  009.  Lit.  lion's claw.  —  rers  jAam,  nail,  claw;  iM/r,  lion.
20233:Troy-weight.  (F.  a/iJ  E.)  Orig.  a wcii^'ht  used  at  the  fair  of  Troyes,  a  town in  Frnuce,  S.  E.  of  Paiis.  See  Arnold's Chronicle,  ed.  181 1,  pp.  108,  191 ;  Haydn, Diet,  of  Dates,  &c.
```


## [2026-09-04T18:56:34.836Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:59:20.094Z] TOOL CALL #50: Bash

```json
{
 "command": "cat > data/verification/page-38.json <<'JSONEOF'\n{\n  \"pdf_page\": 38,\n  \"book_page\": 8,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ahu\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"the Avestan family is āhita- 'defiled, soiled' / āhiti- f. 'defilement, blemish' (Bartholomae, AiW cols. 345-348); an independent Avestan noun *ahu- 'defect' is not attested\",\n      \"note\": \"Everything on this chart except the root box itself checks out. The root box comes straight from Nourai's single reference: Mo'in's etymological footnote at Borhan-e Qate' p.72 says the word is 'مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین، پلید و ناپاک، پهلوی âhôk (عیب)' — i.e. Mo'in himself posits an Avestan ahu 'defect, fault' beside the adjective āhita-. But no such headword exists in Bartholomae's Altiranisches Wörterbuch: AiW has ahu-/aŋhu- 'lord' and 'existence, life' (a completely different word, whence Ahura), and for the 'blemish' family only āhita- Adj. 'befleckt, verunreinigt' and āhiti- f. 'Befleckung, Verunreinigung, Makel'. Two further points about the root box: (a) the vowel is long — the whole family has ā- (āhita-, MP āhōg, NP āhū), so the printed 'Ahu' is at best a shortened citation form; (b) Bartholomae, at the very column Nourai cites for the Persian node, derives MP āhōk / NP āhū from āhita- directly, so the chart's two branches are one branch in the standard treatment. The Avestan words, the Pahlavi word, the Persian words and their glosses are all correct as printed, so the entry is sound in substance; only the reconstructed apex is unverifiable. Node #2's chart NOTE (FAF:38 deriving āhū from AV 'a-hu: not good') is rejected by every source consulted — see that node.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"BQT:72\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in, printed p.72 (archive.org borhan-ghate-v1 leaf n282, running head '-۷۲-'; read from the leaf image, saved to data/verification/sources/refs/ocr/BQT/72.vision.txt). Footnote 1 to the entry آهو: 'مشتق از کلمهٔ اوستایی ahu بمعنی عیب و نقص و صفت اوستایی âhita یعنی چرکین، پلید و ناپاک، پهلوی âhôk (عیب)'. This is verbatim Nourai's root box, his Pahlavi node and his āhita node — Mo'in is the whole source of the entry. The OCR text BQT_v1_pages.txt leaf 282 has the main column ('عیب را نیز گفته اند … خواه با مردم باشد و خواه با چیزهای دیگر') but drops the footnotes, hence the image reading.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"ahŭk 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian āhōg, spelled ʾhwk' in Book Pahlavi and ʾhwg in Manichaean script, 'fault, blemish' — MacKenzie, CPD p.5: \\\"āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish\\\". The Manichaean spelling with -g shows the suffix -ōg (< Old Iranian *-uka-) with the stop already voiced; the same suffix gives the homonym āhūg [ʾhwk' | M (ʾ)ʾhwg, N āhū] 'gazelle' (CPD p.5), which is why Nourai and Mo'in both number these words 1 and 2. The negated form is attested in Pahlavi too: an-āhōg [ʾnʾhwk'] 'undefiled' (CPD p.9), i.e. the exact Middle Persian counterpart of Avestan an-āhita-, which ties this node to node #3. Two remarks on the printed form: the book writes 'ahŭk' without marking the long ā- of āhōg, and it uses the older Pahlavi transcription with -k for what MacKenzie reads -g; neither is an error in the JSON (checked against the page image), just Nourai's 1960s-style transcription following Mo'in's 'âhôk'.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88\"],\n          \"ref_check\": [\n            {\"ref\": \"BQT:72\", \"status\": \"supports\", \"note\": \"Mo'in's footnote 1 on printed p.72 names the Pahlavi form explicitly: 'پهلوی âhôk (عیب)' = Pahlavi āhōk 'defect' — exactly this node (see the saved vision reading data/verification/sources/refs/ocr/BQT/72.vision.txt).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 948 = CPD p.5 s.v. āhōg\", \"stance\": \"supports\", \"note\": \"\\\"āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish\\\"; and line 960 \\\"āhūg [ʾhwk' | M (ʾ)ʾhwg, N āhū] gazelle\\\" — the two homonyms Nourai numbers, with the New Persian outcome āhū given for both.\"},\n            {\"src\": \"NYB\", \"where\": \"grep 'ahok|āhōk|ahog' in NYB_vol2_glossary.txt\", \"stance\": \"silent\", \"note\": \"Nyberg's Manual of Pahlavi glossary has no āhōk entry (it covers only the texts printed in Part I); it does have 'Anāhit [ʾnʾhyt'] a female deity; the planet Venus 511. — Av. (125) Anāhita' (line 419), which belongs to node #4.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt no. 59, p.1-2 (grep 'Gazelle')\", \"stance\": \"partial\", \"note\": \"Horn's Grundriss no. 59 is 'āhu \\\"Gazelle\\\". phlv. āhūk \\\"Gazelle\\\"' — he registers only the animal homonym and its Pahlavi ancestor, and says nothing about āhū 'fault'. Confirms the Pahlavi -ūk/-ōk word type but is silent on this particular sense.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âhŭ 2 «آهو۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian آهو āhū (2) 'defect, fault, blemish' is the regular continuation of Middle Persian āhōg: the New Persian reflex of the MP suffix -ōg/-ūg loses the final stop and the vowel falls together as -ū (āhōg > āhū, exactly as āhūg 'gazelle' > āhū 'gazelle', which is why the two are homophones and are numbered in the Persian dictionaries). MacKenzie prints the New Persian outcome in the entry itself ('N āhū'). The word is old New Persian, current in the 10th-11th c. (Ferdowsī آهو گرفت 'became faulty'; the chart's shāhed from Faḵr al-Dīn Gorgānī's Vīs o Rāmīn, 'ز گیتی بی آهو نیابی کسی – اگر چند دارد هنرها بسی', is of the same period), and it still lives in آهومند 'faulty, defective, sick'. Mo'in's own dictionary glosses it 'آهو: (اِ.) عیب، نقص. بیماری، مرض. (ص.) بد، ناپسند' — the chart's 'defect' exactly. On the chart's NOTE (FAF:38 derives the word from Avestan 'a-hu: not good'): the privative a-/an- and the adjective hu- 'good' are both real Old Iranian morphemes, but no compound *a-hu- is attested, and the derivation cannot explain either the long ā- or the -k/-g suffix of MP āhōg, which is the form New Persian actually continues; Bartholomae, MacKenzie and Mo'in all attach āhū instead to Avestan āhita- 'defiled'. Nourai is right to record FAF's claim only as a dissenting note.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%87%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BRT:345\", \"status\": \"supports\", \"note\": \"Bartholomae, AiW: the āhita- entry stands in the column block headed '345 āh- … āhūirya- 346' (archive.org altiranischeswr00bartgoog, form-feed leaf 219 of BRT.txt; the next running head on that leaf is '347 āhūirya-'). Text: '• j. āhita- Adj. \\\"befleckt, verunreinigt\\\" … KompE. — PPfP. … — Vgl. [Pü.] āhōk, np. āhū \\\"Sünde\\\".' Bartholomae therefore states in so many words that New Persian āhū 'sin, fault' and Pahlavi āhōk belong to Avestan āhita- — which is precisely the arrow Nourai draws (his cited column 345 is right, or at most one column early).\"},\n            {\"ref\": \"FAF:38\", \"status\": \"not_checked\", \"note\": \"Daneshgar, Farhang-e A'lam-e Fārsi (1370/1991) — refs_online.json records no digitised copy on any accessible platform, so the wording of the claim quoted in the chart's NOTE could not be verified at source; only its content was evaluated (see derivation).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol Adena abridgement) s.v. آهو\", \"stance\": \"supports\", \"note\": \"'آهو: (اِ.) عیب، نقص. بیماری، مرض. (ص.) بد، ناپسند' and 'آهومند: (ص‌مر.) مریض، بیمار … معیوب، ناقص، مختل' — Mo'in's lexicon gives exactly the chart's gloss 'defect' for the second آهو.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' printed p.72 (leaf image, vision reading saved)\", \"stance\": \"supports\", \"note\": \"Main column: 'عیب را نیز گفته اند … خواه با مردم باشد و خواه با چیزهای دیگر' — Borhan lists 'fault' among the senses of آهو; footnote 1 (Mo'in) gives the Avestan/Pahlavi etymology and quotes Khāqāni playing on the two senses ('غزال و عیب').\"},\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 948\", \"stance\": \"supports\", \"note\": \"MacKenzie writes the New Persian outcome into the Middle Persian entry: 'āhōg … N āhū, fault, blemish'.\"},\n            {\"src\": \"HRN\", \"where\": \"HRN.txt no. 59\", \"stance\": \"silent\", \"note\": \"Horn treats only āhū 'Gazelle' (phlv. āhūk 'Gazelle'), with Kurdish ask, Baluchi āsk; he has no entry for āhū 'fault', so the Grundriss neither supports nor contradicts.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/آهو\", \"stance\": \"partial\", \"note\": \"Etymology 1 (gazelle) is derived from MP āhūg, ultimately PIE *h₂eḱus 'sharp, swift' (Kurd. ask, Bal. āsk), citing MacKenzie and Horn; Etymology 2, the 'defect, imperfection' sense, is explicitly marked '(This etymology is missing or incomplete)' and is illustrated only by a Ferdowsī citation 'آهو گرفت'. So Wiktionary confirms the existence and sense of the word and the split into two homonyms, but offers no etymology to compare.\"},\n            {\"src\": \"ARY\", \"where\": \"grep 'آهو' in incoming/ARY/ARY_pages.txt (3 hits, all آهورامزدا / آهوش)\", \"stance\": \"silent\", \"note\": \"Aryanpur's Persian IE-roots dictionary has no usable آهو entry in the OCR.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"âhita; an-âhita\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both words are Younger Avestan and are glossed on the chart exactly as the standard dictionaries gloss them. Bartholomae, AiW: 'j. āhita- Adj. \\\"befleckt, verunreinigt\\\"' (attested Vd. 16.16, of the garment a menstruating woman has touched), a past participle in -ta-, and 'j. an-āhita-, p. *an-āhita- Adj. (fem. -tā-) \\\"woran kein Fleck, kein Makel ist, haftet, makellos\\\"', used above all as the third epithet of the river goddess Arədvī Sūrā Anāhitā (Yt. 5, Yasna 65.1 apəm arədvīm sūrām anāhitām) and also of the priestly barəsman and zaohra in Yt. 10.88. Morphologically an-āhita- is the privative an- (PIE *n̥-) + āhita-, i.e. 'the unstained one'; that analysis is Kent's too ('Cpd. of neg. an- + pte. pass. āhita- \\\"spotted, defiled\\\"… \\\"The Spotless\\\"'), though Kent adds that āhita- itself is 'of uncertain connections' and Bartholomae only calls it a participle without settling its base. So the two Avestan words and their meanings are certain; what is not demonstrable is the chart's arrow from a root box 'Ahu' (see the entry note).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"KNT:167\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.167 (KNT.txt form-feed leaf 189, which carries the printed page numbers 167/168): 'Anāhita- sb. \\\"Anahita, Anaitis\\\", a goddess: Elam. a-na-hi-ud-da, Akk. a-na-ah-i-tu-ʾ, Gk. Ἀναῖτις; Av. anāhitā-. Cpd. of neg. an- + pte. pass. āhita- \\\"spotted, defiled\\\", of uncertain connections (§67.I, §118.V, §242.I): \\\"The Spotless\\\".' Nourai's page number and his analysis both hold.\"},\n            {\"ref\": \"BQT:72\", \"status\": \"supports\", \"note\": \"Mo'in's footnote: 'و صفت اوستایی âhita یعنی چرکین، پلید و ناپاک' = 'and the Avestan adjective āhita, i.e. filthy, foul and unclean' — the chart's gloss 'dirty, faulty'.\"},\n            {\"ref\": \"FAF:36\", \"status\": \"not_checked\", \"note\": \"Daneshgar, Farhang-e A'lam-e Fārsi — no accessible copy (refs_online.json: 'none online').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt leaf 219 (cols. ~345-348) s.v. āhita-, āhitay-; leaf 104 (col. ~125) s.v. an-āhita-\", \"stance\": \"supports\", \"note\": \"'j. āhita- Adj. \\\"befleckt, verunreinigt\\\"' with the derived noun 'j. āhitay- f. \\\"Befleckung, Verunreinigung, Makel\\\"' (Pahlavi gloss āhōkēnūn / āhōkōmand); and 'j. an-āhita-, p. *an-āhita- Adj. \\\"woran kein Fleck, kein Makel ist, haftet, makellos\\\"… A) als weibliche Gottheit, Anāhitā'.\"},\n            {\"src\": \"KNT\", \"where\": \"KNT.txt leaf 189 = p.167\", \"stance\": \"supports\", \"note\": \"See ref_check: an- + āhita- 'spotted, defiled' = 'The Spotless'; Kent also flags §67.I etc. for the writing of the Old Persian form.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 419\", \"stance\": \"supports\", \"note\": \"'Anāhit [ʾnʾhyt'] a female deity; the planet Venus 511. — Av. (125) Anāhita' — Nyberg refers the Middle Persian name back to Avestan anāhita- (his '(125)' is Bartholomae's AiW column).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"Ânâhîta «آناهیتا»; Nâhîd «ناهید»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two Persian reflexes of Avestan anāhitā-, by two different routes. (1) Nāhīd is the inherited one: Av. (Arədvī Sūrā) Anāhitā → Old Persian Anāhita (first in the inscriptions of Artaxerxes II, A²Sa 3-4, A²Ha 5-6, beside Elamite a-na-hi-ud-da, Akkadian a-na-ah-i-tu-ʾ and Greek Ἀναῖτις) → Middle Persian Anāhīd, written ʾnʾhyt', 'immaculate; a goddess; astr. Venus' (MacKenzie, CPD p.9; Nyberg II 419) → New Persian Nāhīd by loss of the unstressed initial a- (aphaeresis), the change Hübschmann documents in Persische Studien §19 ('Nāhēd (Nöldeke, Tab. 4) = paz. Anāhit, Shk. 228, arm. Anahit, zd. anāhita-'; the Armenian loan Anahit preserves the a-). The astral sense on the chart ('a bright star') is the ancient identification of Anāhitā with the planet Venus, already Middle Persian (MacKenzie: 'astr. Venus'), which is why Mo'in's dictionary glosses زهره/بیدخت as ناهید. Ferdowsī's line quoted on the chart ('درخشنده ناهید و هور آفرید') is the planet, not the goddess. (2) Ānāhitā آناهیتا, by contrast, is not an inherited form — New Persian would not preserve -itā; it is a modern learned re-borrowing of the Avestan nominative Anāhitā, taken over as a girl's name in the 20th-century revival of pre-Islamic names (and Nourai's own gloss, '\\\"innocent, clean\\\", a female name', is the Avestan meaning, not a Persian one). Both are correctly attached to node #3.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A7%D9%87%DB%8C%D8%AF\",\n            \"https://en.wiktionary.org/wiki/Anahita\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FAF:36\", \"status\": \"not_checked\", \"note\": \"Daneshgar, Farhang-e A'lam-e Fārsi (1370/1991), Nourai's only reference for this node, is not digitised anywhere reachable (refs_online.json: kind 'none', 'RE-SEARCH 2026-09: nothing digitised on any permitted platform'). The claim was checked instead against Kent, Bartholomae, MacKenzie, Nyberg and Hübschmann, all of which support it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt line 1052 = CPD p.9\", \"stance\": \"supports\", \"note\": \"\\\"anāhīd ['nʾhyt' | N nāhīd] immaculate; a goddess; astr. Venus\\\" — MacKenzie gives the Middle Persian → New Persian step and both of the chart's glosses ('innocent, clean' and 'a bright star') in one line; also 'an-āhōg [ʾnʾhwk'] undefiled' on the next line, the native doublet.\"},\n            {\"src\": \"HUB\", \"where\": \"HUB.txt line ~4826 (Persische Studien §19, p.137-138)\", \"stance\": \"supports\", \"note\": \"'Aus i wird ē: Nāhēd (Nöldeke, Tab. 4) = paz. Anāhit, Shk. 228, arm. Anahit, zd. anāhita-' — Hübschmann's chain Avestan anāhita- > Pazand/MP Anāhit > NP Nāhēd/Nāhīd, with the Armenian loan as witness.\"},\n            {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt line 419\", \"stance\": \"supports\", \"note\": \"'Anāhit [ʾnʾhyt'] a female deity; the planet Venus 511. — Av. (125) Anāhita'.\"},\n            {\"src\": \"KNT\", \"where\": \"KNT.txt leaf 189 = p.167 s.v. Anāhita-\", \"stance\": \"supports\", \"note\": \"Gives the Old Persian link in the chain (Artaxerxes II's inscriptions) with the Elamite, Akkadian and Greek transcriptions.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt s.vv. بیدخت، زاور، زهره‌رخ (2-vol abridgement; the a'lam volumes are not online)\", \"stance\": \"partial\", \"note\": \"Mo'in's abridged lexicon has no headword ناهید (proper names are in vols 5-6, which are not digitised) but uses it as the gloss of the Venus words: 'بیدخت … (امر.) ستارهٔ زهره، ناهید' and 'زاور … (اِ.) زهره، ناهید' — confirming the 'bright star' sense of the chart.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ناهید and /Anahita\", \"stance\": \"supports\", \"note\": \"ناهید 'from Middle Persian ʾnʾhyt' (anāhīd)', senses 'Anahita; the planet Venus; a female given name', with Kurdish Nehîda; the Anahita page gives Old Persian 𐎠𐎴𐏃𐎡𐎫 and lists MP ʾnʾhyt' (anāhīd), NP آناهیتا / ناهید, Armenian Անահիտ, Greek Ἀναῖτις (its etymology section is otherwise flagged incomplete).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ai\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂ey- 'to give, allot' (Pokorny 3. ai- 'geben, zuteilen', p.10; Watkins ai-1 'to give, allot'), with the derived stems *ai-ti-, *ai-to- / *oi-to- 'share'\",\n      \"note\": \"A short, entirely orthodox chart: root, both branches and the English word are what Pokorny and Watkins print, and Nourai's page number POK:10 is exact. Two things to note. (a) The reconstruction is written today with an initial laryngeal, *h₂ey- (the Hittite pa-i 'he gives' and Tocharian B ai- that Pokorny already cites are the key witnesses), so 'Ai' is the 1959 shape of the root, not an error. (b) The Greek word as printed, 'dia-ithan', is misspelled in the book itself — I rendered pdf page 38 from the repository's own PDF and the box really reads 'dia-ithan : to decide on one's life'; the JSON transcription is faithful. Watkins's text, which is plainly Nourai's source ('Suffixed form *ai-tā- in Greek diaitan, to decide, lead one's life: DIET¹'), spells it diaitan (διαιτᾶν). The chart also has one empty box, drawn to the right of the aēta node with an arrow into it but no text — an unfilled box in the print, not a lost node.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/diet\",\n        \"https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CE%B1%CE%B9%CF%84%CE%B1\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:10\", \"status\": \"supports\", \"note\": \"Pokorny, IEW I p.10 (POK_01.txt form-feed leaf 17, the leaf carrying the printed '10'): '3. ai- \\\"geben, zuteilen\\\", über mediales \\\"sich geben lassen\\\" dann auch \\\"nehmen\\\"', with Gr. αἴνυμαι, Lat. aemulus, Toch. B ai- / A e- 'geben', Hitt. pa-a-i 'er gibt'; and immediately after, 'Hierher gehört zweifellos: ai-ti-, ai-to- : oi-to- \\\"Anteil\\\"'. Root name, gloss and page are all right.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aěta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan aēta- m. 'the due share, the portion that is owed' — from the root *h₂ey- 'give, allot' by the o-/e-grade *ai-to- noun suffix that Pokorny sets up under the root ('ai-ti-, ai-to- : oi-to- \\\"Anteil\\\"'), the same formation as Greek αἶσα (< *ait-i̯a) 'share, lot' and Oscan aeteis gen. 'partis', aittíúm 'portionum'. Bartholomae (AiW cols. 17-18) prints 'j. ²aēta- m. \\\"das gebührende Teil\\\"'; in practice the Avestan word is used of what is owed as requital, hence Pokorny's parenthesis '(\\\"Strafe\\\"; Dual \\\"Schuld und Strafe\\\")' — 'share' as on the chart is the etymological, not the usual textual, sense, and Nourai's one-word gloss follows Pokorny's Anteil. The word is Younger Avestan (Yt. 10.45-51, Y. 19.11).\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:10\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 17 (printed p.10), under 'ai-ti-, ai-to- : oi-to- \\\"Anteil\\\"': 'Av. aēta- \\\"der gebührende Teil\\\" (\\\"Strafe\\\"; Dual \\\"Schuld und Strafe\\\")'. Exactly this node, on exactly the page cited.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt cols. 17-18 (line 2527) s.v. ²aēta-\", \"stance\": \"supports\", \"note\": \"'• j. ²aēta- m. \\\"das gebührende Teil\\\"' with the Yašt/Yasna references — the Avestan word and Nourai's gloss.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 2-3 (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt lines 306-322), s.v. ai-to-, ai-ti- 'Anteil'\", \"stance\": \"supports\", \"note\": \"'av. aēta- \\\"der gebührende Teil\\\" (\\\"Strafe\\\"; dual \\\"Schuld und Strafe\\\") (Bezzenberger BB. 4, 322; Fick; Bartholomae IF. 12, 139, Airan. Wb. 11 f.)', beside Gk. αἶσα and Osc. aeteis 'partis'.\"},\n            {\"src\": \"IEC\", \"where\": \"IEC.txt line 317\", \"stance\": \"supports\", \"note\": \"Mann, IE Comparative Dictionary: 'aitā, is, iə \\\"share, part, lot\\\". WP I, 2 & I, 7  Av. aeta; Gk. aisa (ambig.); Osc. aet-, aitt- (i-stem)…'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 13744 (s.v. etio-/aetiology)\", \"stance\": \"supports\", \"note\": \"Klein cites 'Avestic aēta-, \\\"share, lot, due\\\", Oscan aeteis (gen.), \\\"of somebody's part\\\", Toch. B ai-, \\\"to give\\\" (lit. \\\"to allot\\\")' as cognates of Gk. αἶσα, and cross-refers 'Cp. diet, \\\"fare\\\"' — i.e. Klein joins this node and node #2 under one root, as the chart does.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"dia-ithan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The etymology drawn here is standard; the Greek form as printed is not. What is meant is διαιτᾶν, the infinitive of διαιτάω 'to arbitrate, to regulate, to order one's way of life' — Watkins, whose appendix Nourai cites, writes 'Suffixed form *ai-tā- in Greek diaitan, to decide, lead one's life: DIET¹', word for word Nourai's gloss 'to decide on one's life'. There is no θ in the word (it is δι-/δια- + *αἰτάω, a frequentative of αἴνυμαι 'to take'), so 'dia-ithan' is a misprint; I checked the page image of the book itself, and the error is Nourai's, not the JSON transcription's. From the verb comes the deverbal noun δίαιτα 'the office of an arbiter; way of living, regimen', which is the word that actually travels on to Latin and English (node #3). Pokorny gives the same analysis on the cited page ('διαιτάω (vielleicht dissimiliert aus *διαιτιάω) \\\"bin Schiedsrichter, leite; teile das Leben ein = führe eine gewisse Lebensart; schreibe ein gewisses Maß im Essen und Trinken vor\\\", daher δίαιτα'). A minor divergence in current scholarship: Beekes (EDG 2010, followed by Wiktionary) takes the first element as δι- 'twice' rather than δια- 'through/apart', while Bailly and the older tradition (and Etymonline, 'from dia- \\\"apart\\\" + ainysthai \\\"take\\\"') keep δια-; nobody disputes the connection with the *ai- root, so the arrow itself stands.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%B4%CE%B9%CE%B1%CE%B9%CF%84%CE%AC%CF%89\",\n            \"https://en.wiktionary.org/wiki/%CE%B4%CE%AF%CE%B1%CE%B9%CF%84%CE%B1\",\n            \"https://www.etymonline.com/word/diet\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 268: 'ai-1, To give, allot. 1. Suffixed form *ai-t-yā in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-tā- in Greek diaitan, to decide, lead one's life: DIET¹. [Pok. 3. ai- 10.]' — Nourai's node is a transcription of this sentence (including the gloss), with the h wrongly inserted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 18 (printed p.11), continuation of 3. ai-\", \"stance\": \"supports\", \"note\": \"'διαιτάω (vielleicht dissimiliert aus *διαιτιάω) \\\"bin Schiedsrichter, leite; teile das Leben ein = führe eine gewisse Lebensart…\\\", daher δίαιτα \\\"Schiedsrichteramt\\\" und \\\"Lebensweise, Lebenseinteilung\\\"' — the verb, spelled correctly, under the very root Nourai cites.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 2 (WLD_Bd1 djvu line ~312)\", \"stance\": \"supports\", \"note\": \"Same text in the older Walde-Pokorny: 'διαιτάω (vielleicht dissimiliert aus *διαιτιάω) \\\"bin Schiedsrichter, leite; teile das Leben ein…\\\", daher δίαιτα \\\"Schiedsrichteramt\\\" und \\\"Lebensweise, Lebenseinteilung\\\"'.\"},\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 11363, s.v. diet 'fare, food'\", \"stance\": \"supports\", \"note\": \"'Gk. δίαιτα, \\\"the office of an arbiter; mode of living; dwelling, abode\\\", back formation fr. διαιτᾶν, \\\"to maintain, support\\\", which is formed fr. δι- (form of διά before a vowel) and αἶσα (for *αἰτια), \\\"share, lot, destiny\\\"' — Klein spells the infinitive διαιτᾶν, i.e. Nourai's 'dia-ithan' minus the h.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/διαιτάω\", \"stance\": \"partial\", \"note\": \"Analyses it as δῐᾰ- (Bailly) or δῐ- (Beekes) + *αἰτᾰ́ω, a frequentative of αἴνῠμαι 'to take', comparing αἰτέω; senses given include 'to lead one's life; to live' and 'to arbitrate; to regulate' — the chart's 'to decide on one's life'. The prefix is the only point at issue.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"English\",\n          \"words\": \"diet\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek δίαιτα 'way of living, regimen' was borrowed into Latin as diaeta 'prescribed way of life, regimen', which in the medical Latin of the Middle Ages became dieta; Old French diete (13th c.) 'food, fare, regimen' gave Middle English diete (c. 1300), whence modern diet, in the specialised sense 'customary or prescribed food' from the late 14th c. and 'reduced-calorie regimen' only from the 20th (attributive 'diet' of foods, US, by 1963). The homonym diet 'legislative assembly' is a different word — Medieval Latin dieta 'appointed day' from Latin dies 'day' — and Klein, Skeat and Etymonline all keep the two apart; since the chart gives no gloss, only the food word belongs under this root, and that is the one Watkins tags DIET¹.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/diet\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); the chain was checked against Klein, Skeat, Funk & Wagnalls and Etymonline instead — see consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 11363 (and 11362 for the homonym)\", \"stance\": \"supports\", \"note\": \"'diet, n., fare, food. — ME. diete, fr. OF. diete (F. diète), fr. L. diaeta, \\\"mode of living\\\", fr. Gk. δίαιτα…'; and separately 'diet, n., a parliamentary assembly. — ML. dieta, \\\"an appointed day\\\"… fr. L. dies, \\\"day\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"SKT.txt line 5047 (and 5048)\", \"stance\": \"supports\", \"note\": \"'Diet (1), regimen. (F. — L. — Gk.) M.E. diete. — O.F. diete… — Low L. dieta, diaeta, a ration of food. — Gk. δίαιτα, mode of life, diet.' Skeat's Diet (2) 'an assembly' is derived from Low L. diaeta/dies with the note that the use 'was due to a popular etymology which connected diaeta with dies, a day'.\"},\n            {\"src\": \"FSD\", \"where\": \"FSD_vol1.txt line 93084, s.v. diet\", \"stance\": \"supports\", \"note\": \"Funk & Wagnalls: '[< F. diète, < L. diaeta, < Gr. diaita, manner of living, diet.]'.\"},\n            {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/diet\", \"stance\": \"supports\", \"note\": \"'from Old French diete, Medieval Latin dieta, from Greek diaita \\\"way of life, regimen, dwelling\\\", related to diaitasthai \\\"lead one's life\\\", from diaitan… from PIE root *ai- (1) \\\"to give, allot\\\"' — the whole chart in one line, root included.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool data/verification/page-38.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T18:59:22.165Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T18:59:28.055Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -la data/verification/page-38.json; python3 tools/verify_check.py 38"
}
```


### [2026-09-04T18:59:29.772Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 29055 Sep  4 14:59 data/verification/page-38.json
nodes verified: 7/7
node verdicts: {'confirmed': 6, 'plausible': 1}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'supports': 6, 'not_checked': 4}
books consulted: {'supports': 23, 'silent': 3, 'partial': 4} | by book: {'PHD': 3, 'NYB': 3, 'Wiktionary': 3, 'KLN': 3, 'HRN': 2, 'MON': 2, 'BRT': 2, 'KNT': 2, 'WLD': 2, 'BQT': 1, 'ARY': 1, 'HUB': 1, 'IEC': 1, 'POK': 1, 'SKT': 1, 'FSD': 1, 'Etymonline': 1}
```


## [2026-09-04T18:59:45.013Z] AGENT

Done. `data/verification/page-38.json` written; `python3 tools/verify_check.py 38` reports 7/7 nodes, no PROBLEM lines.

**Page 38 (book p.8) — 2 entries, 7 nodes**
- Node verdicts: 6 confirmed, 1 plausible. Root verdicts: 1 confirmed (Ai), 1 plausible (Ahu).
- Ref checks: 6 supports, 4 not_checked (all FAF = Daneshgar, *Farhang-e A'lam-e Fārsi*, not digitised anywhere). Books consulted: 30 entries across BQT, BRT, KNT, PHD, NYB, HRN, HUB, MON, ARY, POK, WLD, IEC, KLN, SKT, FSD + Wiktionary/Etymonline (all web pages archived via `fetch_source.py`).

Flagged items:
- **ROOT "Ahu" (Avestan, 'defect, fault') — plausible.** Nourai's only source, Mo'in's footnote at Borhan-e Qate' p.72, does assert an Avestan *ahu* 'عیب و نقص', but no such headword exists in Bartholomae's AiW (which has only āhita- 'befleckt' / āhiti- 'Makel'; ahu-/aŋhu- is the unrelated 'lord, life'). The vowel should also be long (ā-). Everything hanging off it is correct.
- **#2 Greek "dia-ithan" (entry Ai) — plausible.** The form is a misprint for διαιτᾶν (*diaitan*); I rendered pdf page 38 from the repo PDF and the book itself prints "dia-ithan", so the JSON is faithful — not a transcription error. The etymology is verbatim Watkins (`ai-1 … Greek diaitan, to decide, lead one's life: DIET¹`).

Notable positive findings: Bartholomae at the very column Nourai cites (BRT:345) writes "Vgl. … āhōk, np. āhū 'Sünde'" under āhita-, and MacKenzie CPD p.5 has "āhōg [ʾhwk' | M ʾhwg, N āhū] fault, blemish" beside the homonym āhūg 'gazelle' — so Nourai's "2" numbering is exactly right. Kent p.167 confirms an- + āhita- = "The Spotless". The FAF:38 alternative (āhū < AV *a-hu 'not good') is unsupported by every source consulted. I also saved a vision reading of the un-OCRed BQT p.72 footnote to `data/verification/sources/refs/ocr/BQT/72.vision.txt`.
