# Verification process log — model-comparison/verify-opus-page-32


## [2026-09-04T18:06:58.752Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 32 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-32.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (all files listed in the source matrix exist there). ONE DEVIATION from the instructions: this is a model-comparison run, so write your output to /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-32.json instead of data/verification/, do NOT read or copy any existing file under /home/sfmqrb/git/rishe/data/verification/page-*.json, and check coverage with `VERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus python3 /home/sfmqrb/git/rishe/tools/verify_check.py 32` (the script now honours VERIFY_DIR). Everything else as instructed (modern web sources archived with tools/fetch_source.py, Nourai's citations checked in the local reference texts, every relevant book consulted per the source matrix). Reply with the short summary described in the instructions.


## [2026-09-04T18:06:59.993Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T18:07:01.861Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T18:07:01.875Z] TOOL RESULT

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


## [2026-09-04T18:07:02.605Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-32.txt"
}
```


### [2026-09-04T18:07:02.619Z] TOOL RESULT

```
1	=== PDF page 32 (book page 2) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ab 1, Ap 1 : water  (refs POK:1)  PART 2
4	#1 (parent #0) [Avestan / Pahlavi] refs=KLN:2 | âp : water
5	  #2 (parent #1) [Persian] refs=HRN:1; AEF:2 | âb «آب ۲» : glitter (as on water surface) ; âberŭ «آبرو» : "facial shine", good reputation ; âftâb «آفتاب» : "glitter shine", sun
6	    #3 (parent #2) [Arabic] refs=AFM:7; FVF:11 | âb-bahâ : "glittering shine", elegance ; abboha : magnificence, elegance
7	      #4 (parent #3) [Persian] refs=MON:131 | obbohat «أبهت» : elegance
8	
```


## [2026-09-04T18:07:03.875Z] AGENT

I'll read the supporting files.


## [2026-09-04T18:07:06.377Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-32.json && echo \"=== MATRIX ===\" && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md"
}
```


### [2026-09-04T18:07:06.448Z] TOOL RESULT

```
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


## [2026-09-04T18:07:10.202Z] AGENT

Small chart — root plus 4 nodes. Let me check the bibliography and refs index.


## [2026-09-04T18:07:12.397Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && grep -n -iE '^(AEF|FVF|FVQ|AFM|MON|HRN|KLN|POK)' bibliography_raw.txt | head -40; echo \"---\"; grep -n -iE 'AEF|FVF' bibliography_raw.txt | head -20"
}
```


### [2026-09-04T18:07:12.492Z] TOOL RESULT

```
---
3: TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
6: TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
12: TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll
```


## [2026-09-04T18:07:13.935Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','HRN','AEF','FVF','FVQ','AFM','MON','HUB','PHD','BRT','PLA','ARY','BQT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-04T18:07:15.607Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
```


## [2026-09-04T18:07:20.307Z] AGENT

Now let me look up Pokorny p.1 and Klein p.2.


## [2026-09-04T18:07:21.734Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor n in [8,9,10]:\n    print('=== leaf',n,'===')\n    print(d[n][:3000])\n\""
}
```


## [2026-09-04T18:07:22.442Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\n\" ; grep -n \"page 2\\]\" KLN_1966.txt | head"
}
```


### [2026-09-04T18:07:23.311Z] TOOL RESULT

```
leaves 364
=== leaf 8 ===
BUCH
ä  Ausruf  der  Empfindung,  oft  neugeschaffen.
Ai.  ä  Ausruf  der  Besinnung-;
gr.  ä  Ausruf  des  Unwillens,  Schmerzes,  Erstaunens;  Ic,  da  Ausruf  der Verwunderung  und  Klage;  dazu  ä^etv  ^ächzen*";
lat.  äj  äh  Ausruf  des  Schmerzes^  des  Unwillens;
lit.  äj  aä  Ausruf  der  Verwunderung^  des  Tadels  oder  Spottes^,  ä  Aus- ruf der  verwunderten  Frage  (lauter  Neuschöpfungen);
got.  ö  Ausruf  des  Unwillens^  der  Bewunderung;  ahd.  ö  Ausruf  des Schmerzes;  mhd.  ö  Ausruf  des  Schmerzes,,  der  Bewunderung^  auch  dem Vokativ  angehängt.
WP.  I  1,  WH.  I  1,  Loewe  KZ.  54,  143.
ab-  ^Wasser;,  Fluß^.
Lat.  amnis  i.,  später  m.  c(*abnis)]  air.  ab  (*a&ä)  Gen.  ahae  ^Fluß^,  da- neben abann,  cjmr.  afon,  orn.  bret.  auon,  gall.  brit.  FIN  Abona,  abge- leitet cymr.  afanc  \,Biber;  AVasserdämon,  Zwerg^,  mir.  abac  (^abankos ^Biber,  Zwerg^  Schweiz. -frz.  avan  ^Weide^  (*abanko-):   lett.  FIN  Äbava.
Die  westdeutschen  FIN  auf  -apa,  nhd.  -affa^  gehen  wohl  teils  auf  sonst verlorengegangenes  westgerm.  *ap-  (idg.  *a6-),  teils  auf  ven.-ill.  ap-  (idg. *ap-)  zurück.
Vgl.  auch  2.  up-  ^Wasser^  Fluß^  und  abö(n)  ,Affe^
WP.  I  46  f.,  WH.  I  40,  Feist  19  a,  579  a,  GIPatSR.  II  134.
äbel-,  Uböl-,  abel-  ,ApfeP.
Lat.  Abella  (osk.  Stadt  in  Campanien)  malifera  ,äpfeltragend'^,  nach  Verg. Aen.  7,  740,  dürfte  ihren  Namen  nach  der  Apfelzucht  erhalten  haben  und auf  die  Grundform  *ablo7iä  zurückweisen.  Der  Apfel  ist  nicht  etwa  erst nach  der  Stadt  benannt.
Im  Kelt.  sind  die  Bezeichnungen  für  ,Apfel^  (*ablu)  und  ,Apfelbaum'^ (*abal-n-)  auseinanderzuhalten.  Gall.  avallo  ,poma',  Aballö  (n-St.)  ON, frz.  AvalloTij  abrit.  ON  Aballäva,  gallo-rom.  *aballinca  , Alpenmistel  (Wart- burg); air.  ubuU  (*ablu)  n.  ,ApfeF,  ncymr.  afal/ VI.  afalau,  corn.  bret. aval   m.  ,Apfel^,   aber    mir.  aball  (^abalnä
=== leaf 9 ===
)  f.  , Apfelbaum^,    acymr.  aball^
mcymr.  avall  PL  euyill  (analogisch)  f.,  acymr.  aballen,  ncymr.  afallen _, Äpfelbaum*'  (mit  Singulativendung).
Die  gleichen  Ablautformen  im  Germanischen:
Krimg-ot.  apel  (got.  *apls?),  ahd.  apfid,  afful,  mhd.  apfel,  ags.  ceppel (engl,  apple),  an.  epli  n.  (apal-grär  ^apfelgrau^)  ;,Apfel^  Germ,  wohl *ap{a)la-,  *aplu-.  Ferner  an.  apaldr  ^Apfelbaum^,  ags.  apuldor,  ceppuldre, ahd.  aphoUra  (vgl.  nhd.  Affoltern  ON),  mhd.  apf alter  ^Apfelbaum^  {*apaldra-).
Das  Baltische  zeigt  deutliche  Spuren  der  im  Idg.  ganz  vereinzelten Z-Deklination  '^aböl,  G.  Sg.  *äbeles.  Dehnstufe  des  Suffixes  erscheint  noeist im  Worte  für  ^ApfeF:  ostlit.  obuolys,  lett.  dbuolis  (-uo-St.);  westlit.  öbuolas, lett.  äbuols  (o-St.)  aus  idg.  *a6ö^;  Normalstufe  meist  im  Worte  für  ^Apfel- baum^;  lit.  obelis  (fem.  i-St),  lett.  äbels  (i-St.)^  äbele  (e-St.)  aus  idg.  *äbel-] aber  apr.  tvoble  f.  {^äbl-)  ^Apfel*^;,  luobalne  (*äboln-)  f.  ^Apfelbaum^
Abg.  abhko,  jabhko,  poln.  jabiko,  slov.  jdbolko,  russ.  jdbloko  ^Apfel' (*abhko  aus  *äblu-)  usw.;  abg.  (j)ablanh,  sloven.  jdblan,  acech.  jablaiij jablon,  russ.  jdblom  ^»Apfelbaum^;  aus  idg.  ^äboln-  (die  Lautform  von  *ablo ;ApfeP  beeinflußt).
Obgleich  eine  einheitliche  Grundform  nicht  ansetzbar  ist,  wird  es  sich bei  den  lat.  kelt.  germ.  bsL  Formen  nur  um  Urverwandtschaft  und  kaum um  Entlehnung  handeln.  Beziehung  zu  lat.  ables  /Fanne^  usw.  sehr  un- siciier.
WP.  I  50,  WH.  I  3,  E.  Fraenkel  KZ.  63,  172  ff.,  Trautmann  2.
abh-  ,rasch,  heftig'^,  alter  r/n-St.
Gr.  äcpag  ,sogleich^  (altes  Abstraktum  ,Schnelliglceit'),  wozu  doch  wohl zunächst  Ixcpvu),  ^(pvcog  ,plötzlich^
Hierher  allenfalls  aksl.  aböje  ,sogleich,  alsbald^,  aber  unsicher  ai.  ahnäya ,alsbald,  sogleich^  (eher  zu  dhar,  dhan-  ,Tag^  S.  7).
WP.  1  52,  Lewy  IF.  54,  46,  Schwyzer  Gr.  Gr.  I  6245.
Dazu  o:ehört:
ahhro-  ,stark,  heftig'
Mir.  Präfix  abor-,  cymr.  a/r- ,sehr^;  got.  a6?'5  , stark,  heftig^,  SidiY.  abraba ,sehr^,  bi-abrjan  ,vor  Staunen  außer  sich  geraten^  aisl.  Präfix  afar-  ,sehr'; ill.  VN  "'u4ßQ0L,  thrak.  PN  '^ßqo-.
Hierher  vielleicht  got.  aba  (n-Stamm)  ,Gatte^
WP.  I  177,  Feist  1  b  f.,  579  a.,  W.  Schulze  KZ.  52,  311  =  Kl.  Sehr.  398.
abö(22)  ,Affe'  (kelt.  Neuschöpfung).
Das  durch  reisende  Kaufleute  eingeführte  Tier  kann  von  den  Kelten mit  dem  Namen  ihres  Wasserdämons  (s.  oben  ab-)  benannt  worden  sein. Hes.  äßQ�
=== leaf 10 ===
�vag'   KsItol  rovg  xsoKomd-rjnovg  ist  vielleicht  dßßdvag  (Akk.  PL)
zu  lesen  und  noch  vor  der  Lautverschiebung  ins  Germ,  gedrungen;  daher an.  api  m.  ^Affe^  Tor^^,    as.  apo^   ahd.  affo   m.,    affa,  affin  L,   ags.    apa  m. Aus    dem    Germ,    stammt    aruss.    opica    ^Affe^^    acech.    opice.     Vgl.    ab- ^Wasser^  und  Schrader  Reallex.^  Hoops  Reallex.  s.  v.  Affe. AVP.  I  51  f.
j.  ad'  ;Zu^  bei^  an^
Pliryg.  aö-daxET  ,Qr  macht^;  maked.  Hö-dai'  qv^ol  (Schwyzer  Gr.  Gr. I  69) ;  lat.  ad  /zu^  bei^  an^^  Präverb  und  Präp.  m.  Akk.^  auch  Gen.  des Bereiches^  atque,  ac  ^und  dazu^  und  auch^  und^  (*ad-que]  nicht  at  +  quey ebenso  umbr.  ap  ^ubi^  cum'^  zeitlich^  um  -I  erweitert  ape),  umbr.  aT^--  Prä- vcrb;  -af  Postposition  m.  Akk.^  osk.  adpud  ^quoad'^^  sonst  mit  s-Erw.  osk. az  ^ad^  Präp.  m.  Akk.;  air.  ad-  Präverb  (z.B.  ad-glädur  ^appellö^),  cymr. add-,  gall.  ad-  Präfix  (z.  B.  MN  Ad-iantii:  cymr.  addiant  , Sehnsucht^,  Ad- märiis:  air.  mar  ,groß');  cymr.  ä.  vor  Vokal  ag  ,mit'  (ad-\-ghe,  ai.  ha^ nicht  =  lat.  atque);  germ.  *at  Präverb  und  Präp.  meist  mit  ,Dativ^  =  Lok., seltener  ra.  Akk.  (got.  westgerm.  von  der  Zeit,  ags.  auch  vom  Orte),  aisl. auch  mit  Gen. :  got.  at  ,zu,  bei^,  aisl.  at  ,zu,  bei,  gegen,  nach',  ags.  cet^ as.  at,  ahd.  az  ,zu,  bei,  an'.
Schwundstufig:  ved.  t-sdrati  , schleicht,  schleicht  heran^,  ahd.  zagen  (:got. *-rt<7an  , fürchten'),  ahd.  z-ougen,  mhd.  zöngen,  as.  t-ögian  gegenüber  got.  at- angjan  ,vor  Augen  stellen,  zeigend
WP.  1  44  f.,  WH.  I  11  f.
Vielleicht  zum  Folgenden.
2.  ad'  , festsetzen,  ordnen',  ado-  ,Ziel'.
Umbr.  arsie  (*adto-)  ,sancte',  arsmor  (*admon)  ,ritus*,  arsmatiam  (*adma- tlo-)  ,ritualem',  armamu  ,ordinamini*,  Armune  Beiname  des  Jupiter,  zu  *ac?- , festsetzen,  ordnen';  air.  ad  n.  , Gesetz',  PI.  ada  , feierlicher  Brauch^,  daraus Adj.  ,gesetzHch',  adas  ,geziemend',  cymr.  addas  , passend',  eddyl  (*adilo-) , Pflicht,  Ziel';  wohl  auch  germ.  *tila-  ,passende  Gelegenheit'  in  got.  tu  n., ga-tiU  , passend',  ags.  til  ,passend,  nützlich'  als  n.  ,Güte,  Taughchkeit'  = ahd.  zil  ,Ziek,  Präp.  ags.  aisl.  iU  ,bis'. WH.  [  12,  Devoto  Mel.  Pedersen  224.
ades-,  ados'  n.  , Getreideart,  Spelt'.
r^at.  ador,  -(fi'ü  n.  ,eine  Art  Getreide,  Spelt',  vielleicht  zu  got.  atish (*ade8-lco-)  , Saatfeld',  wohl  m.  wie  ahd.  ezzisca  PI.  ,Saat',  mhd.  dial.  Esch, Schweiz,  dial.  Aesch,  , Feldflur  eines  Dorfes';  toch.  AB  äti  , Gräser'  (anders Pederse
```


### [2026-09-04T18:07:25.055Z] TOOL RESULT

```
leaves 903
```


## [2026-09-04T18:07:34.184Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('POK_01.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in [59,60]:\n    print('=== leaf',n,'(p.',n-8,') ===')\n    print(d[n][:2600])\n\""
}
```


### [2026-09-04T18:07:35.934Z] TOOL RESULT

```
=== leaf 59 (p. 51 ) ===
 Zusammenhang  mit  lat.  *a2nö,  *apere  ^comprehendere vinculO;  verbinden,  umbinden^  (imper.  ape  ,prohibe,  compesce'^),  aptus ^verknüpft,  ausgestattet  mit^,  cöpula  (co-apida)  ,Band*  steht  wohl  fest. Vielleicht  ist  von  einer  gemeinsamen  Grundbedeutung  ^fassen,  zusammen- fassen^ auszugehen.
Auch  lat.  apud  ,bei^  wird  am  besten  hierherzustellen  sein.  Die  Grund- bedeutung wäre  ,in  naher  Verbindung^  (vgl.  juxta).  Man  hat  vom  Part. Perf.  neutr.  *apiwd  (aus  *apuot  ^erreicht  habend^  auszugehen.  Die  Neben- form apor,  apur  (mars.-lat.  apur  finem)  weist  auf  ursprüngl.  -d]
lat.  apeXy  -icis  ,Spitze^,  bes.  ,stabartiger  Aufsatz  auf  der  Priestermütze*^; gehört  vielleicht  zu  *apw]  vgl.  auch  EM.  60;
toch.  A  oppäcgi  ^geschickt^  (Van  Windekens  Lexique  82);
hitt.  e-ip-mi  (epmi)  ,nehme^,  3.  PI.  ap-pa-an-zi  (^apanzi).
Über  ai.  äpi-h  ^Freund^,  gr.  }jn:iog  ^freundliche  s.  u.  epi-,
WP.  I  45  f.,  WH.  I  57  f.,  60,  847,  Pedersen  Hitt.  128,  Couvreur  ^  93.
2.  äp-  ,Wasser,  Fluß^
Ai.  up-  f.  ,Wassere,  z.  B.  PI.  Nom.  äpah^  Akk.  apdh,  Gen.  apäm,  av. Nom.  Sg.  äfs,  Akk.  Sg.  äpdm,  Instr.  Sg.  apa(-ca)j  ai.  dpavant-  ,wässerige, in  alter  Kontraktion  der  Red.-St.  mit  auf  -i,  -u  ausl.  Präfixen  (Kretschmer KZ.  31,  385,  Johansson  IF.  4,  137  f.)  pratlpd-  .gegen  den  Strom  gerichtet^, nipd-  ,tiefliegende,  anüpd-  ,am  Wasser  gelegen^,  dvipd-  ,Insel,  Sandbank im  Flusse^,  antarlpa-  ,Insek;  dieselbe  Kontraktion  mit  einem  auf  -o  en- digenden 1.  Glied  in  den  gr.  Flußnamen  ''IvwTtog,  l^acarvög  {:  höco,  ^Gig] Fick  BB.  22,  61,  62);  gr.  l^rcia  ,Peloponnese,  Meao-ania  ds.,  die  lokr. MeGO-(X7tL0Ly  die  ill.  MsaGafCLOi  (anders  Krabe  ZONF.  13,  20  f.)  und  Apuli Unteritaliens,  die  Flußnamen  ^Arciddiv  (Arkadien),  ''u4rtidav6g  (Thessalien), thrak.  ^'Ajtog  (Dacien),  ill.  ""^xpog,  Apsus,  apul.  ON  Sal-apia  (,Salzwasser'^);
hierher  als  Spuren  ven.-ill.  Einwanderung  im  Westen  ein  Teil  der  westd.
4*
52  •
apa-J^ umen^  wie  die  Erft  (^Arnapia),  und  alle  FIN  mit  -up-,  wie  nhd.  I C/ppia-Bach  (Tirol)^  frz.  Sinope  (Manche)^  brit.  Hafen  Rutupiae,  sizil. KaKVTtaQLg  (vgl.  lit.  Kakwpis),  vgl.  die  thrak.  YY^'^Yniog,  '^'Ynavig;  apr. ape  ;Fluß^,  apus  ^Quell^  Brunnen^,  lit.  üpe,  lett.  upe  ^Wasser^  {u  ist  vielleicht Red. -St.  von  idg.  o,  a,  Trautmann  Bsl.  Wb.  11;  o
=== leaf 60 (p. 52 ) ===
der  gehört  up-  eher  zu aksl.  vopa  ^See^?).  Hierher  Ach-{^aps-)  in  cymr.  FIN,  gall.  Axonal
Daneben  kelt.-lat.  ah-,  s.  u.  ah-.
Zur  Erklärung  der  6-Form  geht  Johansson  IF.  4^  137  f.  von  dem durch  ^Atzlööjv,  ^Amdavög  sowie  durch  ai.  dbda-h  m.  ^Wolke^  und  den  mit äpah  paradigmatisch  zusammengeschweißten  Instr.  Dat.  PI.  ai.  adhliih, adbhyah  vorausgesetzten  St.  *ap(9)d-  (vielleicht  ^Wasser  gebend'^  mit  zu dö-  ^geben''  gehörigem  2.  Gliede)  aus:  *ahd5(n),  Gen.  *abdnes,  woraus *abnes',  aus  den  obl.  Kasus  entsprang  lat.  amnisj  während  im  keltischen *abdö(n) :  *abnes  zu  *abä  (mir.  ab),  ^abonä  (daher  mir.  abann)  ausgeglichen wurde.
WP.  I  46  f.,  WH.  I  40,  846,  Krabe  Gl.  20,  188  ff.,  Pokornj  UriUyrier 110  ff.,  130  f.,  Krabe  Würzburg.  Jahrb.  1,  86  ff.
3.  ap-,  äp-  ,gebrechlich;  Schadend
Ai.  apvd  ,Krankheit,  Durchfall,  av.  (von  einem  -es-St.)  afia-  m.  ,Schaden, Unheil;  lit.  opus  ,schwach,  wund,  gebrechlich^  (Charpentier  KZ.  40,  442  f.), vermutlich  gr.  '^TTsöavög  ,gebrechlich,  schwach"  (Bezzenberger  BB.  1,  164; zum  Ausgang  s.  Risch  98;  anders  Schwyzer  Gr.  Gr.  I  530).
WP.  I  47,  Specht  Dekl.  345.
appa  ,Vater^;  Lallwort.
Vgl.  gr.  äTtTTcc,  dncpa,  ^ncpa,  ärccpvg  (Theokrit)  ,Papa';  toch.  B  appakke ,Vater^  (das  -{a)kke  von  ammakki  ,Mutter^). WP.  I  47.  Vgl.  auch  pap(p)a.
apelo-  ,Kraft^
Gr.  dv-a7teXdaag'  dvaQQcja&elg  Hes.,  ion.  E^nelrjg  ,kräftig^,  hom.  dXiyrjTreliT) ,Ohnmacht',  ion.  dvr^nslit}'  äad-sveia  Hes.,  elischer  MN  Tevrl-artlog (nach  Prellwitz  BB.  24,  214  ff.,  Kretschmer  Gl.  18,  205  hierher  'ArtBlluiv, "Aitolloiv,  mit  Vokalabstufung  thess.  "Anlow^  nach  Sommer  IF.  55, 1762  vielmehr  vorgriechisch)  ;_ill.  ym  Mag-aplinus,  Aplus,  Aplo,  Aplis,  -inis, FN  Aplo,  -onis-  gall.  VN  Di-ablintes  ,'die  Kraftlosen^  (aus  *-aplentes)', germ.  GN  Matroms  Aflims,  Afliabus  ,den  (Zauber)  Wirkenden^  aisl.  afi  n., ags.  afol,  abal  n.  ,Kraft^
WP.  I  176,  Feist  la,  Kretschmer  Gl.  24,  250.
53
ipero-  ;Ufer^
Gr.  iJTtsLQOQy  dor.  äTzsioog  L  ^Ufer;  Festland^;  ags.  ofer,  rand.  over^  mhd. (md..)  uover,  nhd.  Ufer]  aber  arra.  a'p^n  ^Ufer^  erfordert  idg.  j9Ä  und  bleibt
daher  fern.
Beziehung  zu  *«2^o  ^ab^^  ai.  dpara-  ^hinterer^  späterer^  als  Dehnstufen- bildun^''  wird  von  Specht  Dekl.  23  angenommen.
WP°  I  48.
apo'   {po,  ap-u,  pu)  ,ab,  weg^
Ai.  dpa  ^weg;  fort^  zurück^  als  adnominale  Präp.  m.  Abi.  ;,von— weg^^^ av.
```


## [2026-09-04T18:07:37.215Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','AFM','MON','HRN','FVQ']:\n    print(k, json.dumps(d[k].get('page_offset'), ensure_ascii=False))\n    print('  hint:', json.dumps(d[k].get('lookup_hint'), ensure_ascii=False)[:400])\n    print('  local:', json.dumps(d[k].get('local_file'), ensure_ascii=False))\n\""
}
```


### [2026-09-04T18:07:38.883Z] TOOL RESULT

```
KLN "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  hint: "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages."
  local: "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt"
AFM "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image"
  hint: "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير')."
  local: ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"]
MON null
  hint: "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/a
  local: ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"]
HRN "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
  hint: "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann."
  local: "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt"
FVQ "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)"
  hint: "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296)."
  local: ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"]
```


## [2026-09-04T18:07:48.637Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in [12,13,14]:\n    print('=== leaf',n,'===')\n    print(d[n][:2500])\n    print()\n\""
}
```


### [2026-09-04T18:07:50.519Z] TOOL RESULT

```
=== leaf 12 ===
an
Republics
Russ.
Russian
V.
verb
S.
South
var.
variant
S.Afr.
South  African
veter.
veterinary
S.Am.
South  American
VArab.
Vulgar  Arabic
XXV
VL.
Vulgar  Latin
vulg.
vulgar
Vulg.
Vulgate
W.
Welsh
W.African
West  African
WSem.
West  Semitic
WTeut.
West  Teutonic
Zech.
Zechariah
Zeph.
Zephaniah
zool.
zoology
Symbols  used  in  this  Dictionary
A
The  asterisk  (*)  indicates  a  hypothetical  form.
The  mark  called  macron  (-)  is  placed  over  a  vowel  to  show  that  it  is  long.
The  mark  called  breve  (  ')  is  placed  over  a  vowel  to  show  that  it  is  short.
In  this  dictionary  the  quantity  of  vowels  (esp.  in  Greek  and  Latin  words)  is  mdica  ed  °  ^ when  they  are  long.  The  brevity  of  vowels  is  indicated  only  in  some  special  cases  (e.g.  m  Latin "  to  ie  to  hang’,  in  contradistinction  to  pendtre,  ‘to  hang’  (see  pendan,).  Hence when  there  is  no  mark  over  a  vowel  it  is  to  be  assumed  that  it  is  short.
The  mark’  after  a  consonant  in  the  Slavonic  languages  indicates  Palata  “'
The  mark  -  after  a  syllable  or  a  group  of  syllables  (as  in  ant-,anti-)  indicates  that  this  syllable
or  group  of  syllables  is  a  prefix.
The  mark  -  before  a  syllable  or  a  group  of  syllables  (as  in  -ate,
syllable  or  group  of  syllables  is  a  suffix.
-atiori)  indicates  that  this
a,  indef.  article.  —  Form  of  an  before  a  consonant, a,  prep,  meaning  ‘of’,  as  in  a  clock  =  of  the dock.  —  ME.,  fr.  OE.  of,  ‘from,  off,  of’.  See  of. a,  prep,  meaning  ‘on*.  —  OE.  an,  on,  ‘on’.  See  on. a,  prep,  meaning  ‘to,  at,  in’.  —  F.,  fr.  L.  ad,  ‘to, toward’.  See  ad-  and  cp.  a-,  pref.  corresponding to  L.  ad-.  Cp.  also  a  la.
a-,  pref.  meaning  ‘of’,  as  in  akin.  —  ME.  a-, fr.  OE.  of.  See  a,  prep,  meaning  ‘of’, a-,  pref.  meaning  ‘on’;  used  to  form  adverbs from  nouns  as  in  abroad,  ashore.  —  Fr.  OE.  an, on.  See  a,  prep,  meaning  ‘on’, a-,  intensive  pref.  —  OE.  a-,  rel.  to  OS.,  OFris. ur-,  or-,  Du.  oor-,  OHG.,MHG.  ur-  (unstressed  : OHG.  ir-,  ar-,  MHG.,  G.  -er),  Goth.  us-.  The orig.  meaning  of  these  prefixes  was  ‘out,  away’. Cp.  the  pref.  in  oakum,  ordeal. a-,  pref.  meaning  ‘away  from,  from’  (occurring only  before  v),  as  in  avert.  —  L.  a-,  fr.  a,  short form  of  ab,  ‘away  from,  from’ ;  rel.  to  Oscan aa-,  Umbr.  aha-,  ‘away  from,  from’.  

=== leaf 13 ===
  L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  element in  bouillabaisse.
Derivatives :  abas-ed ,  adj.,  abas-ed-ly,  adv.,  abas- ed-ness,  n.,  abase- ment,  n. abash,  tr.  v.,to  confuse;  to  put  to  shame.  —  ME. abassen,  abaissen,  abashen,  fr.  OF.  esbahiss-, pres.  part,  stem  of  esbahir,  ‘to  astonish’,  com¬ pounded  of  pref.  es-  (fr.  L.  ex\  see  1st  ex-)  and a  derivative  of  OF.  baer  (F.  bayer ),  ‘to  gape’, the  change  of  conjugation  (-ir  for  -er)  being prob.  due  to  the  influence  of  the  OF.  adj.  batf.
abasia
abiogenesis
‘astonished’.  The  OF.  verb  baer  derives  fr.  VL. batare,  ‘to  gape,  yawn’.  See  bay,  ‘part  in  the wall’,  and  cp.  words  there  referred  to. Derivatives:  abash-less,  adj.,  abash-less-ly,  adv., abash-ment,  n.
abasia,  n.,  inability  to  walk  ( med .)  —  Medical  L., formed  fr.  priv.  pref.  a-  and  Gk.  Bam?,  ‘stepping, step;  base’,  from  the  stem  of  flaivsiv,  ‘to  go’. See  base,  n.,  and  -ia.
abate,  tr.  and  intr.  v.  —  ME.  abaten,  fr.  OF.  abatre, abattre  (F.  abattre),  ‘to  beat  down’,  fr.  VL.  *ab- balere  (whence  also  It.  abbattere,  Sp.  abatir ), fr.  ab-  and  batere  (L.  battuere),  ‘to  beat,  strike’. See  batter,  ‘to  beat,  strike’,  and  cp.  abatis,  abat¬ toir,  bate,  ‘to  reduce’.
Derivative:  abate-ment,  n. abatis,  n.,  a  defense  made  of  felled  trees  (m/7.)  — F.,  ‘things  thrown  down’,  fr.  abattre,  ‘to  beat down,  throw  down’.  See  prec.  word  and  cp. abattoir.
abattoir,  n.,  a  slaughterhouse.  —  F.,  fr.  abattre, ‘to  beat  down’.  See  abate.  The  subst.  suff.  -oir corresponds  to  L.  -orium,  whence  E.  -ory. abb,  n.,  the  yarn  for  the  woof.  —  OE.  aweb,  ab. See  a-,  ‘on’,  and  web.
abba,  n.,  title  of  honor.  —  L.,  fr.  Gk.  fr.
Aram,  abbd,  ‘the  father;  my  father’,  emphatic state  of  abh,  ‘father’.  See  abbot,  and  cp.  ab¬ bacy,  abbey.
abbacy,  n.,  the  office  or  jurisdiction  of  an  abbot. —  Eccles.  L.  abbatia,  fr.  abbas,  gen.  abbatis.  See abbot  and  cp.  abba,  abbey.  Cp.  also  badia. abbe,  n.,  a  title  given  in  France  to  a  priest.  —  F., fr.  Eccles.  L.  abbatem,  acc.  of  abbas.  Cp.  It. abbate,  Sp.  abad,  ‘abbot’,  which  also  derive  fr. Eccles.  L.  abbatem,  and  see  abbot, abbess,  n.  • —  ME.  abbesse,  fr.  OF.  ( =  F.)  abbesse, fr.  Eccles.  L.  abbatissa,  fern,  of  abbas,  gen.  -at

=== leaf 14 ===
nt,  efficient,  elicit,  exhibit,  Illicium,  inci¬ dent,  incipient,  inhibit,  inimical,  institute,  insipid, insipient,  irritate,  ‘to  make  null  and  void’,  navi¬ gate,  obstinate,  Occident,  occiput,  office,  partici¬ pate,  precipice,  prodigal,  proficient,  prohibit,  pros¬ titute,  receive,  recidivist,  resilient,  resipiscence, restitute,  reticent,  substitute,  superficies,  super¬ stition,  supplicate,  transilient. ability,  n.  —  ME.  abilite,  fr.  OF.  ablete,  habilite (F.  habilite),  fr.  L.  habffitatem,  acc.  of  habilitas, ‘aptitude,  ability’,  fr.  habilis,  ‘that  may  be  easily handled  or  managed,  suitable,  fit,  proper’.  See able  and  -ity.
-ability,  subst.  suff.  expressing  ability,  capacity, fitnrss.  —  L.  -abilitas,  forming  nouns  from  ad¬ jectives  ending  in  -abilis.  See  -able  and  -ity  and cp.  -ibility.
abh>-,  combining  form  meaning  ‘without  life’.  — Fr.  Gk.  Sffioi;,  ‘without  life’,  fr.  a-  (see  priv. pref.  a-)  and  (JIo?,  ‘life’.  See  bio-, abiogenesis,  n.  supposed  production  of  living  or¬ ganisms  from  unliving  matter;  spontaneous
abiogenetic
about
generation.  —  Coined  by  the  English  biologist Thomas  Henry  Huxley  (1825-95)  in  1870  fr. Gk.  ijiioc;,  ‘without  life’,  and  viveaiQ,  ‘origin, source’.  See  abio-  and  genesis  and  cp.  bio¬ genesis.
abiogenetic,  adj .,  pertaining  to  abiogenesis.  —  See prec.  word  and  genetic  and  cp.  biogenetic. Derivative:  abiogenetic-al-ly ,  adv. abiogenist,  n.,  one  who  believes  in  spontaneous generation.  —  See  abiogenesis  and  -ist. abiotrophy,  n.,  loss  of  vitality  (med.)  — -  Coined by  the  English  neurologist  Sir  William  Richard Gowers  (1845-1915)  fr.  Gk.  Spto?,  ‘without life’,  and  -rpocpta,  fr.  rpoqp r|,  ‘nourishment’. See  abio-  and  -trophy.
Derivative:  abiotroph-ic,  adj. abiturient,  n.,  one  who  is  preparing  for  the  final examination  of  a  high  school.  —  G.,  fr.  ModL. abituriens,  gen.  -ends,  pres.  part,  of  abiturlre, ‘to  wish  to  leave’,  a  desiderative  verb  formed  fr.
L.  abed,  abire  (neut.  pp.  abitum),  ‘to  go  away, leave’,  fr.  ab-  and  eo,  ire,  ‘to  go’.  See  itinerate and  cp.  Abeona.  For  the  Latin  desiderative  sutf. -urire  cp.  esurient,  micturition,  parturient,  vomi¬ turition.  For  the  ending  see  suff.  -ent. abject,  adj.,  1)  miserable;  2)  contemptible.  —  L. abjectus,  pp.  of  abicere  (less  correc
```


## [2026-09-04T18:08:06.268Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Avestic  *[āa]p\\b\\|Avestic  *ap-\\|Av\\.  *āp\\|Avestic  *āfš\\|apah\" KLN_1966.txt | head -20; echo \"=== julep/water ===\"; grep -n \"^julep\\|^Punjab\\|^Peshawar\\|^doab\" KLN_1966.txt | head"
}
```


### [2026-09-04T18:08:06.354Z] TOOL RESULT

```
2497:amnic,  adj.,  pertaining  to  a  river.  —  L.  amnicus, fr.  amnis,  ‘river’,  which  stands  for  *ab-nis  and is  cogn.  with  OIr.  abann,  ab,  W.  afon,  ‘river’,  fr. I.-E.  base  *ab-,  a  collateral  form  of  base  *ap-, ‘water,  river’,  whence  OI.  dpah,  apah,  Avestic af-sh,  ‘water’,  Gk.  ‘Atria,  a  name  of  the  Pelo¬ ponnesus  fso  called  because  surrounded  by water),  Mecraxtrla,  ‘Messapia’,  a  part  of  Magna Graecia  in  Lower  Italy  comprising  Apulia  and Calabria,  lit.  ‘the  country  between  two  waters', L.  Ap-ulia,  ‘Apulia’,  lit.  ‘region  abounding  in waters’,  Lith.  upe,  Lett,  upe,  ‘water’,  OPruss. ape,  ‘a  small  river’,  apus,  ‘spring,  fountain, well’,  and  prob.  also  Toch.  AB  ap-,  ‘river’.  Cp.
3247:See  purpose  and  cp.  malapropos,  malapropism. Apsaras,  n.,  one  of  the  nymphs  of  India’s  heaven (Hindu  mythol.)  —  OI.  Apsardh,  lit.  ‘moving  in the  waters’,  compounded  of  ap fr.  apah  (pl.)> ‘water’,  and  sarati,  ‘flows,  runs  fast’.  The  first element  derives  fr.  I.-E.  base  ap-,  ‘water,  river  ; see  amnic.  The  second  element  is  cogn.  with Gk.  6p6?  (for  *oop6 ?),  ‘whey’,  6P(xav,  ‘to  urge, stimulate’,  L.  serum,  ‘whey,  watery  fluid  ;  see
11940:do,  n.,  a  syllable  used  in  solmization  to  denote the  first  tone  of  the  diatonic  scale  (mus.). doab,  n.,  a  track  of  land  between  two  rivers  in India.  —  Pers.-Hind.  doab,  lit.  ‘two  waters’,  fr. do,  ‘two’,  and  db,  ‘water’.  The  first  element  is rel.  to  OI.  dvdu,  dvd,  Avestic  dva,  ‘two’;  see two.  The  second  element  is  rel.  to  OI.  ipah, apah,  Avestic  dp-,  ‘water’ ;  see  amnic. doat,  v.  —  See  dote.
27379:pard,  n.,  partner  (slang).  —  Abbreviated  fr. pardner,  a  slang  variant  of  partner, pardao,  n.,  a  former  Portuguese  gold  coin  of Western  India.  —  Port,  pardao,  ult.  fr.  OI. pratapah,  ‘splendor’,  which  is  formed  fr.  pref. pra-,  ‘before,  forward,  forth’,  and  tapati,  ‘makes warm,  heats’.  OI.  pra-  is  cogn.  with  Gk.  ttp<S, ‘before’ ;  see  pro-  and  cp.  Purana  and  the  first element  in  Prajapati,  Prakrit,  prakriti,  Pralaya.
=== julep/water ===
```


## [2026-09-04T18:08:28.312Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# find leaf containing amnic\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'amnic,  adj.' in l:\n        print('amnic leaf',i,'-> approx printed pages',(i-12)*2,(i-12)*2+1)\n        break\nEOF\necho \"=== HRN p.1 ===\"\npython3 -c \"\nd=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(d))\nprint(d[22][:3000])\n\""
}
```


### [2026-09-04T18:08:30.490Z] TOOL RESULT

```
amnic leaf 45 -> approx printed pages 66 67
=== HRN p.1 ===
412
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
```


## [2026-09-04T18:08:54.285Z] AGENT

Horn p.1 is directly on point. Now Addi Shir p.7 and the Arabic side.


## [2026-09-04T18:08:55.309Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nfor n in [13,14,15,16]:\n    print('=== leaf',n,'===')\n    print(d[n][:1800])\nEOF"
}
```


### [2026-09-04T18:08:57.159Z] TOOL RESULT

```
leaves 198
=== leaf 13 ===
83
0 الى 500 937 :ابن 55[ 37 39093 .1.3
ܐܨܦ القاطع : « اكت مكت بكسر الكافين ضرب من !ܐܝܢ بالسر ܬܒ وهو
اسود :ܠ جوذة الطيس ٠‏ يقال له ( 039 ححر الولادة ܝ الذسر وحجر
العا ٠١و‏ بالتركية « 1 طاثى وطوشتحل تظائق »© وتيختالاه افع لعسر الولادة
وتعلقة على ܐ( ينع تساقط الاكثر.» “قلت أو ܦܘ ܀ :111 لصبت سواانة يكل
ܨ إما ܠ 1 0
3 ܝܫ الشديدة من شدائد الدنيا تعريب آك وهما عمنى
0 ®+ ,|11 ,)7 5) العود 0 ) ܡܳܐ به . .قال الاصمعي ذهو فارسني
معرب ٠‏ قلت 9 13( الصبزء قال الاب 5 50 0507
قلت : والموثافى في ماخوذ من | ܕ لان 5 اصله من بلاد 0935 0
)ܒܨܢ 210 والفرني 0105 والاتكليزي” 5 موالايطاليالي 31 010
( الأماج» الغرض وهو في اصله الفارسي نبشان السهم الموضرع على كرمة من
ܨ ومنة اتكردي آما نج
* ( الاإمدان» | على وجه الارض تصحيف 1 دان ومعناه الغدير
+ (الأمد) يقال ما أمدك 35 5 7 امد ومعناها الزمنان
ܢ ' 1
0 والاميض) طعام ܣ من حلم عجل مجلده او مرق السكماج :7
1 ن الدهن معرب خأ ميز ܙܘ ايضا ܐܐܝܟ ܠܐܠ ܐ ܡܝܢ + يكن باللغة
الربانية
( )ܠ ܙܕ والأندَروَديّة ) اسم لنوع من السراويل مركب من اندّر اي داخل
ومن ور اي ذو
( !¥ ;ܨ ) 3091 فارسنتها آ نك وهو بالسريانّة ܐܢܟܐ و بالعبرانتة $
< 1101 وبالارمشة بسداهه ( القاموس العبرانى ~ ܢ جسشيوس
1( | 0 2 ܐܢܐ ܨ 8 وهر التصدير٠‏ والقصدير ܨܠ 8600 ?)×
ܬ 5 م الزهرة فارسي عر 5 الموأدون و بعضبهم يسميها ܠ ܝܫܝ
92 عطارد 00 الملشثترى و بعضهم لسميه ه الببجس ٠‏ ومرام الريخ ܝܚ
الو ܝܝ 4
ܠܘ
=== leaf 14 ===
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
=== leaf 15 ===
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
=== leaf 16 ===
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
```


## [2026-09-04T18:09:05.457Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 'أبهة' 'الأبهة' 'ابهة' 'الابهة' 'بها'; do echo \"--- $p ---\"; grep -n \"$p\" AFM_pages.txt | head -5; done; echo \"=== first leaves of alef ===\"; python3 -c \"\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in [8,9,10]:\n    print('=== leaf',n,'==='); print(d[n][:1200])\n\""
}
```


### [2026-09-04T18:09:07.501Z] TOOL RESULT

```
--- أبهة ---
--- الأبهة ---
--- ابهة ---
--- الابهة ---
--- بها ---
380:الببهان القاطع انه نوع من الشوك له زهر احمر وأبيض ܐܕܨ 301 له بالتركة
457:* 3 الإبريج ) 45 بها 5 السّمن منها < ابيز
609:» (البتم ) التّخمة والسّامة قيل اليثم لبها خاصة دقيل هو مخصوص بالدسم
684:الببهان القاطع 116 بذم | الناء دواء يقال له فى .شيراز * بل شيدين 110 1
732:5 البطل والمهاوان * من بها اي من ومن دار اي ذو
=== first leaves of alef ===
=== leaf 8 ===
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
( إلا جور اليا عور والا جور والا جر 0 وال جرون)
=== leaf 9 ===
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
-210231طن) ]@ 1:31111123آط ع1 1231111216 1.2101 :
=== leaf 10 ===
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
```


## [2026-09-04T18:09:19.252Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" AFM_pages.txt | head -3; echo \"---\"; grep -n \"العظمة والبهجة\" AFM_pages.txt; echo \"--- context ---\"; sed -n '250,270p' AFM_pages.txt"
}
```


### [2026-09-04T18:09:19.312Z] TOOL RESULT

```
---
182:+ لي العظمة والبهجة معرب أب بآ 16031
--- context ---
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
المشرو بة لبلا9 037 ` مط با كنا لاق
الذهب لانة يلحمة ٠‏ وبال له 28 « جادر اوشاغى »
١‏ الأسْتاقل ) ܣ .27 10 سش قاقل ويقال له بالتركة مبر ساجان
وجرخ فلك. ٠والششقاقل‏ ܕܐ‫ لعتان فيه
( £ ) ܨ݀ ܨܘ الابيض ܗ به السروح مغرب ادرنج ( اقرب
لموارد )
```


## [2026-09-04T18:09:23.335Z] TOOL CALL #16: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py AFM:7 --image 2>&1 | tail -40"
}
```


### [2026-09-04T18:09:25.290Z] TOOL RESULT

```
no scan of AFM covers printed page 7 (see 'scans' in refs_online.json)
```


## [2026-09-04T18:09:31.047Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor n in range(0,9):\n    print('=== leaf',n,'===')\n    print(d[n][:300].replace(chr(10),' | '))\n\""
}
```


### [2026-09-04T18:09:32.737Z] TOOL RESULT

```
=== leaf 0 ===

=== leaf 1 ===
8 | 0 | ܥܝ | ܶܡ 7 | ܫ ܢ 0 ܣܚ | .ܡܨ >  )‏ اعم ܨ | 3 ܛ 5 62 ܨ ܗ | ܡ 5 | 1 ` < 3[ | 1 , 3 5 ܢ | ل ܨ( : : | `( × 2 7 : ̄ܡ | ܝ 2 -. و | / ܪ ܇ ܐ ܢ | . ܥ يبد < ܲܗ | ܘܨ ܝ ܓ | بي بهم 0 1 1 | ܗܨ . ܢ 1 ` | ܙ ^ ܢܢ | 9 ܪ 1 .° 2 | 3 0 : | 1 : ܫ" | ܫ ܠ 1 ܨܢ 7 1 | " ܐ . ܢ | ܨ.܀ .ܝ 4 ܙ ܗܩ 1 | ل رار ܨ | هيه ܘ | ܫ @ < ܟ | 227 5 ܪܐ 8 | ` ܫ ܨ | ܡ ܨܝ بسح ܬ | : ܕ ܝܚ | ܝܢ ܗ | ܬ ܛܠ ܝܚ ص 1
=== leaf 2 ===
الالفاظ 9 ܐܘܝ ܐܬܗ بين | ܨ | 1 62 شرا | رس 03 سعرد اتكلرالى | 70 | ܒ | ܦ المطبعة الكاثوليكة للاباء السوعبين | في بيروت سنة ^ ܀ ܬܙ
=== leaf 3 ===

=== leaf 4 ===
- ܨ | | ان اللغة 5 مشحونة بالفاظ ± كثيرة .ولا ܫܕ من ذلك فان القشائل | السيطة في معيشتها وسياستها متى خالطت الامم الغريبة التمدنة ادخلت لا حالة | الفاظأ اعجسّة الى ܐܠܨܐ وهذا ما ܗ العرب فانم ل يزالوا مع مرور الازمان | خاضعين للبابليين والمصر ين والفرس «اليونان والروم ٠‏ وكانوا قمائل شتى 7 | يخالطون جميع ܐ < فان
=== leaf 5 ===
ل | وقد ܫܒܐ هذه ܠܐܝܐ الفارسة المعر بة 'منذ سئة 1407 15 101 ` | 0065 5 اللغة 393 550 063 غير الى 33130 | راجعت كتالي هذا وادغلت فنه كرات كثيرة كانت 5 99 100 | ممعت كرات اخرى عديدة غيرها ٠‏ واللي مقر بوعورة الطريق التى سلكت فيها وارجو | من علياء اللغة ان ينتقدوا علي 6 لحم للدمقاة ا" | ان العرب كثيرًا ما يتصرفون ت
=== leaf 6 ===
سد © سد | ܬܝܐ الاعجمية او © افعالا من الفاظها الغير 09 ب | مثلا من الفارسي | جنلدرة» 10 7 779 3 2 1 لحر 2 ز يردم » ܨ | ܢ 3 1 .48 ماخوذ م.* ن الفارسي ان ܨ كوس رن | "وشدن : ور ار ܒ ܝ ܪܫܡ الى غير ذلك | . وناهيك ܨ القاموس الفارسي الذى ܘܚܬ عليه فقي 0 هذا هو ܐܨ | « البرهان القاطع » لات حسين بن خلاف ܐܨܒ ٠‏ ܕܬ | ܝ ترحق
=== leaf 7 ===
أب الحمزة | ܟ ( الأباب) الماء الكل اب معرب آب وهو الما , ܕܬܕ 0 5 بالسنسكر ܝ ٠‏ | واو بالكردبة ܕ 211 © ® 13009 5 ن 3 516 ومعئاه ݀ܘ | (0 0003 الراغف في مغرد انه : 58 ولس من كلام العرب ٠‏ | قات وقع في شعر الفرزدق $ الثقات < ذهو | ¢ صحيح فصيح ( شفاء | الغليل ».قات وهو معرب اباد ومعئاه المعمور. وكان الفرس اذا اراد
=== leaf 8 ===
حت آي ܝ | 3 وهو ذو لسان 003 فبه ܨ )1 . ܣ(¿ فارسي مسرن >1 ٠وقال‏ ܝ | سفاء ܣ 6 تكون في السرج وغيذه ج أباذيم ويقال أبزين. . | وهو من ¥ بمنى ܢ عض فليس معرب لك :إبزيم ܐ £ حديدة في طرف اللزام | < :ܐ ويقال له ܐܢܐ زرفن وزرفين فين»٠قات‏ ان صعة هذا 3 ܚܨ على كإنه | 0( معراقك اما عن 05 وهو المعماز او عن الفارسي ابزن وعر
```


## [2026-09-04T18:09:42.035Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt; do echo \"### $f\"; grep -n \"ابهت\\|أبهت\\|ابهه\\|أبهة\" \"$f\" | head -8; done"
}
```


## [2026-09-04T18:09:42.562Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HUB abâ/âb\"; grep -n \"Glanz\" HUB.txt | head -20"
}
```


### [2026-09-04T18:09:44.108Z] TOOL RESULT

```
### MON_part1.txt
6560:ابسهت: ۳۹ ال ابهت) [ع.] 
19777:منشی. نسیم. شکوه؛ ابهت» اهمست. تندی» 
25667:به مشابهت. ضح.- لازم الااضافه است. 
26989:بی‌ریب.: (ابهتطارودآا اف. ۳۵ (ص مر.) 
77878:حمله» هجوم. قهر» غلبه. ابهت» وقار. 
78408:سفطه: (م)مابهه [ع. سقطة] (.) خطاء 
83494:گیاهی است از تیرةٌ پنیرکیان و مشابهتش با 
84131:شبه: "3202 [ع.] (امص.) مشابهت؛ مانندی. 
### MON_part2.txt
43527:ابهت و جلال مخصوصی به آن می‌دهد. 
46116:متشابهه. آیات متشابهات: آیه‌هایی از قرآن 
47941:محاز دارای علاقه مشابهت باشد آن را 
47983:مشابهت و قرينةٌ مانع از ارادهٌ معنی حقیقی 
48092:محانست: (عه)ابههمآهوه [ع. محانسه ] 
57079:مشابهت: (حط)نهطهط ۵۹8 [ع. مشابهه | 
57190:مفاعیلن» است و سبب همین مشابهت و 
57195:ی و (امص.) مشابهت. 
### incoming/MON/MON_2vol_Adena_v1_djvu.txt
6560:ابسهت: ۳۹ ال ابهت) [ع.] 
19777:منشی. نسیم. شکوه؛ ابهت» اهمست. تندی» 
25667:به مشابهت. ضح.- لازم الااضافه است. 
26989:بی‌ریب.: (ابهتطارودآا اف. ۳۵ (ص مر.) 
77878:حمله» هجوم. قهر» غلبه. ابهت» وقار. 
78408:سفطه: (م)مابهه [ع. سقطة] (.) خطاء 
83494:گیاهی است از تیرةٌ پنیرکیان و مشابهتش با 
84131:شبه: "3202 [ع.] (امص.) مشابهت؛ مانندی.
```


### [2026-09-04T18:09:44.148Z] TOOL RESULT

```
### HUB abâ/âb
551:x'^ared^a- (bei Justi = Glanz) nicht 'Glanz' bedeuten.
6123:glanzen' = ftiroxtan, furoy 'Glanz', phi. afrOxtan, zd. aiwi
6215:lava = Idba *Schmeichelei' H. 952 ; tdv = tdb 'Glanz, Hitze,
6401:Da ab *Glanz' == skr. abha- H. 3 unsicher ist, so ergiebt
6547:Dunkel ist das Verhaltniss von np. farr 'Glanz, Maje-
6630:'Glanz, Jifajestat' = ap. farnah-; Pharnerseh (Mos. Xor.),
6673:neben kafiar *Taube' (H. 842). Ueber partav *Glanz, Strahl
7748:avan-nuhabde-mna- ; xurrah 'Glanz' = zd. x^arenah-; Oxur
8333:= phi. tuxsak (oben p. 47) ; ruxs (raxs) 'Glanz*, vgl. zd.
8572:Tlucht' zu gurextan *fliehen', Wrzl. rik; furoy *Glanz* zu
9273:xurrah 'Glanz, Majestftt', zd. x^arenah- (oben p. 83), dazu arm.
9275:= zd. dusx^arenah-; farr, farrah *Glanz, Majestat' = ap.
9771:p. 128, § 6. a wird zu i auch in /arnAT *Glanz*, aL^./arnah-,
```


## [2026-09-04T18:09:49.841Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON ابهت context\"; sed -n '6555,6566p' MON_part1.txt; echo; echo \"### HUB 6390-6420\"; sed -n '6390,6412p' HUB.txt"
}
```


### [2026-09-04T18:09:49.905Z] TOOL RESULT

```
### MON ابهت context
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


### HUB 6390-6420
geschlagenem a: abrU 'Augenbraue* = skr. bhrU".
In den armenischen LW. erscheint stets anl. b = ap.
np. b, vgl. band *Kerker = np. band u. s. w.
b) Ap. b nach n ^= np. 6: xunb *Krug, zd. xumba-
u. s. w., siehe Kap. 28 (m = nb).
§ 75. Ap. b nach Vokalen, d. h. ap. w ist in einigen
Fallen im Np. zu 6, sonst aber zu v geworden:
a) = np. b in : abr * Wolke' = paz. awar Shk. 233, zd,
awra- ; sitabr stark'= zd. stawra-. Ueber asdb *Verwirrung'
u. s. w. (H. 32) vgl. oben p. 7 (phi. dsdp) und iiber (mar i)
s^ba *Viper (H. 800) oben p. 82 und unten p. 185 (phi. sBpak).
Da ab *Glanz' == skr. abha- H. 3 unsicher ist, so ergiebt
sich, dass ap. w nur vor r sicher zu np. b wird. Doch
vgl. np. girlb ein Getreidemass, arab. jarib, syr. NDn:i
(Tab. 242) = arm. griv = ap. ^grfwa-.
b) = np. V in : n^v Vacker , phi. nevak schon (— np.
nBk)j ap. naiwa-, geschrieben naiba- *sch5n ; girav, girau
Tfand', arm. grav Tfand', phi. grav (geschrieben grUbti),
ap.*grraM?a-, skr. grabh *ergreifen*; avardati, avurdan *bringen',
zd. a + bar ; xarvar 'Esels-last', sarvclr *Kopflast' aus *xa-
rawdra-, ^sarawdror', vgl. np. bar 'Last*, mit dem durch Neu-
komposition xarbar, sarbar gebildet wird ^) ; suvar 'Reiter
= ap. asawdra- (geschrieben asabara-) ; paivastan Ver-
```


## [2026-09-04T18:10:11.776Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### AHD watkins ap-\"; grep -n -A12 \"^ap-\\|^\\*ap-\\| ap-\\. Water\" AHD_watkins1985.txt | grep -n -i \"water\" | head; grep -n \"ap-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T18:10:11.834Z] TOOL RESULT

```
<persisted-output>
Output too large (44KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bmco9jb7e.txt

Preview (first 2KB):
### AHD watkins ap-
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
...
</persisted-output>
```


## [2026-09-04T18:10:13.271Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN water\"; grep -n \"1\\.31\\|āpaḥ\\|apah\" SYN.txt | head -20; echo \"### IEC ap\"; grep -n \"^ap- \\|^āp- \\|^apo-\" IEC.txt | head -20"
}
```


### [2026-09-04T18:10:13.352Z] TOOL RESULT

```
### SYN water
173:Similarly in regard to areal word distribution. No doubt, there are sey- eral significant instances of agreement in peripheral areas, e.g. in the Ro- mance field between Spanish-Portuguese and Rumanian, or in the Indo- European field between Italic, Celtic, and Indo-Iranian. Some of these are clearly inherited words, preserved in contrast to innovations spreading in the central area. But the exponents of “‘areal linguistics” (an expansion of the more factual “linguistic geography’) appear to me to overrate the valid- ity of their “norms” (“marginal, central, isolated’) and to indulge in rash inferences therefrom as to what constitutes an archaism and what an inno- vation. Thus for ‘fire’ (1.81) the group represented by Lat. ignis, etc. (Lat., Balto-Slavic, Skt.) is claimed as older than that of the more widespread group, Grk. rip, NE fire, etc. (Grk., Ose.-Umbr., Gme., Arm., Toch., Hitt.) because the former is in the marginal group. Both are inherited, doubtless with some original but lost difference of aspect. It is still more perverse to say that for ‘water’ (1.31) Lat. aqua (which has Germanic cognates in the Sense of running water, esp. ‘river’, and perhaps in some Tocharian and Hit- tite verbs, but only in Latin is the regular word for ���water’) is older than the group represented by Grk. viwp, NE water, etc. (Grk., Umbr., Ir., Gme., Balto-Slavic, Skt., Hitt.) with its typical archaic r/n type. Actually, in- stances of agreement in vocabulary (as in phonology and morphology) may be found between any two and almost any combination of the main Indo- European branches, and it is best to let the facts speak for themselves in each case.
1220:1.31 WATER
1269:now the common generic word (muir prevailing in the name of special seas, as the Irish Sea, etc.) etym. disputed the old comparison with Ir. ferg ‘anger’ and the dxeavds Ovepyotvos of Ptolemy is phonetically difficult. Stokes 273. ’ Ber- gin, Eriu 3.86. Pedersen 2.669 f. Walde- P. 1.289. Perh. best taken as fr. *foirsge : fairsiung ‘wide’ (12.61). So Thurney- sen, Z. celt. Ph. 11.312, Gram. 95.
1274:6. Lith. jira or pl. jarés, Lett. jura, OPruss. jurin (acc. sg.) : Skt. var-, vari- ‘water’, Av. var- ‘rain’, vazri- ‘Jake’, ON ver ‘sea’ (poet.), OF weer ‘sea’ (rare), ON @r ‘fine rain’, etc. (1.31). Walde-P. 1.268.
1296:jurés ‘sea’, ete. (1.31).
1343:3. Lat. unda : Grk. tdwp, Skt. udan-, etc. ‘water’ (1.31).
1380:Most of the words are derived from roots meaning ‘flow, run’. Some are cognate with words for ‘water’, perhaps originally ‘flowing water’ (cf. 1.31). Some are from verbs for ‘rush, plunge’, or ‘roar’, applied first to a rushing, roar- ing stream.
1391:3. From IE *ap (and ab-) ‘water’, Skt. pas, etc. (1.31). Walde-P. 1.46, Ernout-M. 45. Walde-H. 1.40.
1418:7. Goth. ahwa, ON a, OE éa, OHG aha : Lat. aqua ‘water’ (1.31).
1467:Lett. avuots ‘spring’ : Skt. avata- ‘well’, avata- ‘pit’, avani- ‘river, river bed’, perh. Grk. avavpos ‘mountain tor- rent’, Lat. Avernus, etc. Walde-P. 1.254. Mihl.-Endz. 1.233. Walde-H. 1.31f.
1517:4, ON widr ‘woods, wood’, Dan., Sw. ved ‘wood’ (mostly ‘firewood’), OF widu, wudu ‘woods, wood’, so ME wode, NE wood(s) OHG witu ‘wood’, Ir. fid ‘woods, tree, wood’ (NIv. fiodh esp. in epds. ‘wooded’ or ‘wooden’), W. gwydd ‘woods, trees’, Br. gwez ‘trees’ prob. : Lat. di- videre ‘separate’, Skt. vidhu- ‘solitary’, Lith. vidus ‘inside’, etc., with develop- ment of ‘woods’ through ‘borderland’ (as in ON mork, see foll.). Walde-P. 1.314. Falk-Torp 1357.
2003:Av. var- : Skt. vari- ‘water’, ON ar ‘fine rain’, etc. (1.31). Walde-P. 1.268 f.
3617:L Grk. pnrpud, Ton. Entpun (Hom. | tero- in Skt. vitaram ‘farther, more dis- +) ‘stepmother’, deriv. of pirnp with tant’, etc., from *wi- ‘apart’, and orig. suffix related to that of rarpus, uatpws, | pater vitricus ‘remoter father’. Walde-P. Lat. patruus, Skt. pitroya- ‘uncle’ (2.51). | 1.313. Hence Rum. vitreg (fr. lit. Latin, From this was formed masc. ynrpuds or prob. through Hung. official Latin, ef. matputos ‘stepfather’ (both late and | Tiktin S.v.), in tatd vitreg, and by exten rare), NG unr pubs. sion mamdé vitregd, fiu vitreg, fate vitrega.
4210:Fr. bélier, OF r. belin, deriv. of Gmc. word for ‘bell’, as in Du. belhamel, NE bellwether. REW 1022a. Wartburg 1.318.
4947:1. IE *wlkvo- and *luko-. Here be- Jong all the words listed except the Cel- tic and the ON vargr, Sw. varg. Lat. lupus is a Joanword fr. a rural dialect, like Lat. bds. Walde-P. 1.316 f. Ernout-M. 588. Walde-H. 1.836 i
4972:1, Grk. addrnt, NG &derod, Lat. vulpés (> It. volpe, Rum. vulpe), Br. louarn, Lith. lapé, Lett. lapsa : Skt. lopdga- ‘jackal’, Av. raopi- ‘a kind of dog’ (Barth. 1496), NPers. rabah ‘fox’. But phonetic relations complicated and obscure. Walde-P. 1.317.
5109:SCr. obad, Boh. ovdd ‘gadfly’, fr. *o}_ wado-, orig. ‘something that pesters, an- noys’ Boh. vaditi ‘harm, hinder, trouble’, Pol. wadzié ‘make quarrel, hin. der (= ChSl. vaditi ‘accuse’, 21.31), Briickner 387.
5824:(4.207). dim. of carro ‘cart’, and i first as slang, for Ae wsety ith reference to the lower [erent in eating. Le Riv. fil. esp. 11.316. Bee obraz ‘face’ and ‘cheek’, fr. ‘, (ChSl. obrazi ‘form, shape, plavie, ‘cheek’, etc. Tiktin image’, SCr. obraz ‘cheek , etc.
5999:feac (Dinneen), this perh. in orig. iden- tical with Ir. fec, NIr. feac ‘spade’ (though differing in decl. and gender), of which the etym. is dub. (Pedersen 1.159. Walde-P. 1.316). But cf. also Zupitza, KZ 36.208.
6134:‘mouse’ and ‘muscle’, etc. Walde-P. 1.312f. Ernout-M. 645 f.
### IEC ap
649:apo-teros ‘further, following’. WP I, 47. Cf. apo, -teros Skt. OPer. apataram; Arm. var, varo, i vajr, vajra- ‘down, below’; Gk. apóteros; Cor. ater, adar “out of, without’; Go. aftaro (:Gk. apo- . téro); OHG aftaro; ON aptr, eptir; OE efter
650:apo-tokos, à flow from, stream, derivation’. See apo, tek- Gk. (formally) apótokos “resulting from'; Arm. vtak, i, av ‘brook’; OCS potokü ‘stream’; Li. patakà 'flow, drip, leak; pl. small beer
```


## [2026-09-04T18:10:22.078Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SYN 1.31 block\"; sed -n '1220,1240p' SYN.txt | cut -c1-1600; echo; echo \"### AHD ap-2 entry\"; grep -n \"ap-2\\|ap-?\\|“water,”\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-04T18:10:22.145Z] TOOL RESULT

```
### SYN 1.31 block
1.31 WATER
Grk.  bdwp Goth. wats Lith. vanduo NG vepd ON vain Lett. adens Lat. aqua Dan. vand ChSl.  voda It. acqua Sw. vatten SCr.  voda Fr. eau OE weler Boh.  voda Sp. agua ME water Pol. _voda am apd aa water Russ. voda
usce u water Skt. jala-, Gp-, udan- put ae cee wazzar ; Abie ate :
B wfr HG ee lee
Br. dour NEG - carer ge ee
C-0. In Public Domain. Gurukul Kangri Collection, Haridwar
: e
| Digitized by Arya Samaj Foundation Chennai and eGangotri _ | \
oO
—_S ~~ Biotized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 35
The words for ‘water’, with few ex- belong to certain widespread nates, one of these reflect- ing what was clearly the general IE word for ‘water’, and three others also reflecting I words for ‘water’ , but per- haps in some more special application, such as ‘running water’ or ‘rain water’. Many words belonging to these groups appear in other lists, as under ‘sea’, “vave’, ‘river’, ‘rain’.
1. IE *wedor, *wodor, *uden-, a typi- cal r/n stem neuter, with gradation of the root syllable, fr. root *wed- in Skt. ud- ‘wet, flow’. Some forms with nasal in root syllable (intrusion from verb forms with nasal infix, or anticipation of n of stem). Walde-P. 1.252 ff. Er- nout-M. 1124.
Grk. téwp; Umbr. utur (Lat. unda ‘wave’); Ir. usce, NIr. uisce (Gael. wesge- beatha ‘water of life’ > NE whiskey); the Gme. group, Goth. waté, OF weter, etc.; Lith. vanduo, Lett. uidens, OPruss. wundan, unds; ChSl. voda, ete. general Slavic; Skt. wdan-; Hitt. watar, gen. we- tenas; Alb. wé.
2. IE *akva- or *akwa-. Walde-P. 1.34f. Ernout-M. 64. Walde-H. 1.60. Feist 18 f. Lat. aqua with its Romance derivatives. Elsewhere mostly of ‘run- ning water’ in words for ‘river’, as Goth. ahwa, OF éa, etc. (1.46). Here Hitt. eku-, aku-, Toch. yok- ‘drink’?
3. IK *a@p-. Walde-P. 1.46. Skt. dp-, ap- mostly pl. dpas, used esp. of the per-
ceptions, groups of cog
sonified ‘Waters’, Av. ap-, ap- the reg. word for ‘water’, also freq. personified, OPers. api-, NPers. ab ‘water’. Else- where only of ‘running water’ in words for ‘river’, as Lith. upé, Lat. amnis, Ir. abann, etc. (1.46).
4, IB *wer-. Walde-P. 1.268f. Skt. var-, vari, ‘water’ (of all kinds), Toch. A war, B war ‘water’. Elsewhere in words for ‘rain water, rain’, as Av. var-, ON ar (1.75), or for ‘sea’ or ‘lake’, as Av. vairi-, Lith. jurés, etc. (1.32, 1.33). Also Grk. obpov, Lat. wrina ‘urine’ (cf. NE make water).
5. Miscellaneous:
NG vepé fr. veapov (tdwp) ‘fresh water’, through vypdv (cf. Phrynichus vypdv dep ui) elrgs), with regular change of ir to er (Hatzidakis, Mec. 2.598).

### AHD ap-2 entry
83:the contraction of early Indo-European short vowels with a following 9. Already in Proto- Indo-European itself, two of the three laryn- geals had the property of coloring an adja- cent fundamental vowel e to a and o, respectively, before the contractions took place. Thus the root pa-, “to protect,” is contracted from older *paa-, with ‘“‘a- coloring”; the root d6-, “to give,” is con- tracted from older *doo-, with “o-coloring”; and the root dhé-', “to set, put,” is con- tracted from older *dheo-, without coloring. The fundamental vowel in each of these roots, as in most Indo-European roots, was originally e. In scholarly usage it is now customary to write the non-coloring laryn- geal as 9,, (or h,), thus *dheo,-; the a-coloring laryngeal as a, (or h,), thus *pas.-; and the o-coloring laryngeal as a; (or hz), thus *doo,-. This rather cumbersome notation has been simplified in this Dictionary, since the vowel before the schwa is sufficient to distinguish the three in the cases of contraction to a long vowel, and in other positions in most lan- guages other than Greek the three merge to one. No systematic notice has been taken in this Dictionary of word-initial laryngeals before vowels (amply attested in Hittite), since the root forms with initial vowel are readily convertible by the student. Thus ap-?, “water,” from *sap- (Hittite happ-, “water”; op-', “to work, produce in abun- dance,” from *sop- (Hittite happ-in-, “rich”’); ed-, “to eat,’ from 9ed- (Hittite ed-, “to eat”).
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
1707:JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
2044:PAMPER pap-2
2052:PAP? pap-2
2119:POPE papa POPLAR p(y)el- POPPLE? p(y)el- POPPYCOCK kakka-, pap-2 POPULACE populus POPULAR populus POPULATE populus PORCELAIN porko- PORCH per-2 PORCINE porko- PORCUPINE porko-, spei- PORE? per-2
```


## [2026-09-04T18:10:34.943Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### WLD Bd1 p.46 (ap- Wasser)\"; python3 -c \"\nd=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(d))\nimport re\nfor i,l in enumerate(d):\n    if 'Wasser' in l and re.search(r'\\bap-',l) and i<120:\n        print('leaf',i, l[:200].replace(chr(10),' | '))\n\""
}
```


## [2026-09-04T18:10:36.903Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT ap-\"; grep -n \"äp-\\|ap- .Wasser\\|Wasser'\" BRT.txt | head -15; echo; echo \"### KNT api\"; grep -n -i \"api-\\|apiya\" KNT.txt | head -10; echo; echo \"### PHD ab water\"; grep -n \"^āb\\|āb \\[\" PHD.txt | head -15"
}
```


### [2026-09-04T18:10:38.208Z] TOOL RESULT

```
### WLD Bd1 p.46 (ap- Wasser)
leaves 895
leaf 54 46                                           ap     ap- |  |  | 1.   ap- „erreichen“. |      Ai. apnoti „erreicht, erlangt“,         dpta-h „geschickt, geeignet, vertraut“ (d | durch Kontraktion der Praposition
leaf 55                                                ap-, ap-       — apo, po                                  47 |  | FluBnamen auf -npa, ahd. - affa wie ahd. Eril-affa „Erlaff“ (die also nicht |
```


### [2026-09-04T18:10:38.269Z] TOOL RESULT

```
### BRT ap-
3491:l-t  Z'  "t"  'Wasser';  s,  unter  ö>. '  i-  (j  g'.  P-)  spa  i)  Adv.  'weg,  getrennt von—'  (nur  Komp.) 'J.  2)  Praev.  (mit karit-,  gauä-,  gatn-,  bar-,  yam-,  itai'- usw.).  A)  bei  Ellipse  des  Verbums: aiwica  apanm  (sd.)  patica  apanm  (sd.) I  'paca  paourvatibya  nSit  dim  ava'i^a  iri- ^an  (sd.)  V.  r5.48 "';  —  daiuan  'pa  asaTan (sd.)  Yt7p.84(?).  tZu  apa  F.2d  und Vyt.44  s.  No.  i.J KompA.;  Ableit  —  S.  auch  apäaadpajcraifa-.
5154:•  j.  'avah-:  azeS-'^  n.  'Wasser':  macya  .. avS  urzmfi/ (sd.)  Yt.Ä40.
7268:327  äp-  I  A
7295:KompE.  —  Vgl.  äp-  (und  das  Verhältnis  von ai.  .■^pigi-  zu  sphig.).  —  »  D,  L.  Jpii+iim; falsch  BB.  14.  244.
7297:Komp. :  äp-\-*bjril;  also  für  *äb4',  eig. •Wasserträger';  s.  N. //  und  Pü.  —  Pü.: äi(art(Transskr,),  (lu  F.}:  äp  biinär.  —  ')  N.  fc erscheint  eine  andre  Bezeichnung  dafür; äänOBiäia-  (sd.).
8220:n.  'Wasser',    vgl.    gr.    Ziaip;   Bthl.   BB.  /j.
8229:Eig.  'Ottetberg',  AbleiL  aus  udra-,  oder  'der Bei^  am,  im  Wasser',  Ableit  aus  idg.  'udir- (s.  unter  udra^.
8260:•  j,  upa.äpam  Adv.  'auf  dem  Wasser':  | yayata  dunma  yayata  fra.apsm  nynpiin ' 'pfm  "der  Nebe!  wallt,  er  wallt  vor  dem ! Wasser,  dem  Wasser  entlang  abwärts,  auf dem  Wasser"  V.2/.3.
8261:ASn.  ans  *uf,i.äfa-  Adj.  'auf  dem  Wasser  be- findlich', Ableit.  la  upa+äp-,  —  S.  auch  upäpa-, —  pa. :  apar  an  vär-än  i  äp.
8415:Ableit.  zu  upa-iräp-.  —  S.  auch  upa-äpim.  — Pu,:  äpik;  Npü.  (zu  Yt.   I^:  bar  ab.
8465:•  j.  uniyäp-  Adj.  'des  Wasser  sich  weit- hin erstreckt':  zrayaahs  vourukasahe  .  . ja/rahe  'iipaAt''>  \t.8.^6.
8494:•  j,  urv-äp-  Adj.  'des  Wasser  sich  weit ausdehnt,  mit  weiter  Wasserfläche' '' :  ainö.- /aya>um  . .  yahmya  jafra  varayö  °apat>hd (NPm.)'>  hisl-itie\i.io.  14;  —  *pasne  varöis *äu^aitahe  jafrahe  'spahe'^  YL  V49.
11883:•  j.  tadLäp-  i)  'ßiessendes  Wasser":  yat alte  (sd.)  ysi  mazdayasna  ..  'apaya  (LS.)" nasaum  frajasqrt  V.<?,  26.  i)  Adj.  (auch fem.)  'mit  fiiessendem  Wasser':  vat^lm (sd.)  'apam  (A.SQ'i  V.  14.12.
11905:•  j.  tatäp-  Adj.  'fallende  Wasser  habend', sva.  'der  den  Regen  fallen  lässt':  sata- %ais5  .  .  'äpa  (NS.)">  zavarm.srats  'äfS (NS.)''  ux^at.urvarS  Yt.  7^,44;  43"';  — tnihrsm  .  .  frat.ap)m  zavanlS.srBt>m  •ap?m uxryat.urvar»n  Yt  10. 6 1  "*,
14858:ßUl',  ipaslm  'fallen',  np.  u/lad  'er  fälll',  u/tä- dan;  gr.  irirs/iai,  ixrifiT.y.  —  fä.:  falilan,  falc- ttllan.  —  I)  Nur  im  Inf.  iivafaileiS.  —  '1  Form des  absoluten  Anlauts  i  %  83.  l;  s.  taUäp-.  — J)  S  145,  151-  —  *)  Im  Gegensati  {-o.  frala- rai/e;  Pü.:  fehlt.  —  i)  Falsch  IF.  9.  356.  Es handelt  sich  um  das  'Nackt gehen',  s.  Sp.  iiSf.; Jahika   ist  ergäniende  Glosse.    Richtig  Dst.  I

### KNT api
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).

### PHD ab water
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
```


## [2026-09-04T18:10:45.820Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD ab\"; grep -o \"āb \\[[^]]*\\][^.]\\{0,60\\}\" PHD.txt | head -5; grep -o \"ābšār\\|ābgēnag\\|āb-\\|MYA\" PHD.txt | head -5; echo \"--- PHD_mackenzie\"; grep -n -o \".\\{0,120\\}āb \\[MYA.\\{0,120\\}\" PHD_mackenzie.txt | head -3; grep -n -o \".\\{0,80\\}water\\].\\{0,80\\}\" PHD_mackenzie.txt | head -3"
}
```


## [2026-09-04T18:10:47.343Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BRT col 327 region\"; sed -n '7265,7300p' BRT.txt | cut -c1-900"
}
```


### [2026-09-04T18:10:51.986Z] TOOL RESULT

```
### PHD ab
āb [?sy?5] (water-)mill
āb [уор | М ik, N уд] or
āb [pty | N ~] ritually clean; ceremonial ablution
āb [wyn’p | N binàb] vision
āb [hw’b | N ~] sleep
āb-
āb-
āb-
āb-
āb-
--- PHD_mackenzie
ugrep: error: error at position 87
0-\xbf][\x80-\xbf]*){0,120}
                           \___exceeds complexity limits


ugrep: error: error at position 83
xbf][\x80-\xbf]*){0,80}
                       \___exceeds complexity limits
```


### [2026-09-04T18:10:52.032Z] TOOL RESULT

```
### BRT col 327 region
13,  N.  Ö2;  —  äat  (s.  8)  yat  äpd  udiannte .  .  ä'  fralasinH  .  .  fravalayS  Yt  JJ.  65; V,  ^,40,  ^7.4;  —  yat  ('als')  mqm  Iura pazdayaiita  . .  ä°  azsm  tanüm  aguze  . . äat  (s.  3)  mamfraguzayanta  ..  Yt  i;.  553'; — yas)  Uli  mnärom  äktrirum  .  .  ü°  mam mairyd  äkasat  äat  (s.  2)  .  .  fräkirmaot V.  22.  if;    —    äat  (s.  8)  yat  mi>r)m   .  .
fradahqm   ..   il°   dim   daoam  ..  Yt/o-i;
dby  Google
327  äp-  I  A
Schritt  entfernt  ist,  auch  dem  Wasser opfern"  N.  6g.  A)  oft  neben  Feuer, Himmel,  Erde,  Rind,  FQanzen  (usw.):  ma x^ayamna  jasStt  ätnm  . .  äp>m  . .  tarn  . . gqm  ,  .  urvarqmY.g.^y,  42,  11. 1,  2,  5, 9,  10;  —  jia}  . .  vi'iürayat  asmamm  . . np)m  .  .  zqm  .  .  gqm  .  .  urvarqm  Yt  13. aS;  86,  Y.  ig.  8;  —  ahtaatca  apäalca^'> zimaatca  urvarayaatca  gaotca  Vr.  7. 4;- — para  asrntm  .  .  äp^m  ,  .  zqm  .  .  gqJt  ,  . urvarqm  .  .  atr?m  Y.  SQ.2;  —  fravaiayö ya  asmtm^m  viöäray^n  . .  lip»m  . .  zqm  . . gqm  Y.  2^.  1 ;  —  hs  ßptm  staoiti  .  .  zqm . .  gqm  . .  urvarä  . .  vtspa  vohü  H.  /.  3 ;
—  y^  Sl"*  f^^^  (sd.)  apasiil  urvaräscä  Y. 51.7;  /2.7,  _y7.i,  52.2;    —    imat  vü  äpS
/aioyetni  . .  stmS  . .  urvara  Y.  65.13;  i.i  6, 2.16,  77.9,  V1.1G.3,  Yt./^.28,  G.2.6,  V. 7.3,(7.3,  -'/.3;  — jvä  <lpim  faintt  . .  ätnm
frsvaydti  .  .  gqm  .  .  V.  5. 37;  —  sqm ahura'iiltqm  apim  mazdaailtqm  urvarqm aSaonJm   V.  it).  35;    —   apas^a    vawukil
yazftnnS  aiar^wtca  aÄurahe  mazdlt'R..2.i^;
—  nara  . .  yä  riasäum  . .  äpgm  ä  vä  atnm a  vä  .  .  frabariiiti  V.  7.  25;  —  yal fisit  äp5  takaii  stayat  (sd.)  nsit  urvarii uru^mahyö  .  .  fratactn  apö  srvÜth  uzuxs- yqma  urvarä  Yt  IJ.JS;  10,  14,  93';  — apS  ya/iii  urvarä  yaslä  FrW.  /.  2;  Y.  16. 9;  "^  apqmät  vaauhinqtn  urvaranqmca Vr.2/.i;  Ny.4,o,__  Yt./i.S3-SS;  —  ya vatiukil  ya  äpö  yäsal  urvarii  Vi.  21.1;  — kasnJ  d»r»tä  . .  apd  urvaräscä  Y.  44-  4 1 /.12,  2.12,  Äs,  YLÄ7,  23,  29,  y.79'. V.6'.46,  12.2,  /<V.63;  —  mit  .  .  ada  yä kaiiie  .  .  tarff  äax/t?m  pärayüt  (sd.)  tard ap?mca  urvarqmca  "nicht  soll  . .  heimlich (sich  verschaffen)  Wasser  und  Kraut"*' V./j.g;  \o;  ~  ye-A  atthal  iiß  antarät naimat  alte  pa'ha  ü/s  ahq/»  *fraoirisyeiti .  .  yezi  atihal  urvara  .  .  ätar/  a^ai/i *Jraoirisyeiti  V.
ä^rat  .  .  apat  .  .  bar}sm»n  V .  ^.  ii ;  16, /6".4,  77.4;  —  zqm  ahurd'Mtlqm  .  .  sp^m tacintqm .  .yavünqm  uru'imqin  V,  ig. 36;  — a'ia  fiaomya  (da  apa  (IS.)*'  »"^a  aiwyä- uhana  (näml.  ratufris)  N.  108.  a)  Du. in  Verbindung  mit  urvarä-  Du.;  yal  k?r)- naol  ..   atihaoiimne  äpa   urvaire  \.g.\;
ap-  Noten
328
Yt/().32; —  i7/«'*  urvaire yazamaide  G. 4.  s ;   vgl.   N.  2A'.  B)   mit  besonders
charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  y
heisst  der  10.  Monatstag:  apqm  vanu/il- riqm  mazdd'jätanqm  S./.io;  vgl2.io,  Y. ;6'.  4.  [Vt  7J.  I :   lies  apamca,  s.  apü-A
•)  AU  Ya^Ma.  Vgl  bes.  Y.'  6$  W^"  ^^'l Ny.  4  [i/än  «yJy/ia),  ferner  Y.  jS  (s.  lu maiitant-),  6S\  oben  I  c  Eine  eUlle  Schei- dung ist  unlnnlich.  S.  noch  I  C.  —  Über  die 17  Arien   von  Wusei,  die   von  der  Theologie
dby  Google
afritay-
330
geichieden    werden,    s.   unter   inaekanl-*)    and ^ätar-  1  d. KompE.;  Ableit    S.  auch  äpJ;  sowie /a/W/a-,
dvaipa-  und  ä/ani-,  äbitit-.  —  ai.  npa,  npah, apäm;  np.  ab.  —  l'ü.;  äp',  s.  noch  No.  6.  — 0  iFlex.  s.  S  387.  —  ')  Nach  der  (fem.) ä-DckL  —  J»  HdE,  äj'ai.  —  4)  Them.  —  s)  Zur Herbeilührung  der  Frühgeburt.  lüs  handelt sich  aliio  um  bestimmte  Wasser  und  Pftanien. —  o)  Pü, ;  /i/i'j/,  —  ;)  Vgl.  lU  maeianl-  Und ia  agittyä-,
•  g.  äpana-  n.  'Erreichen,  Erlangen'  (des Erstrebten):  aHbyS  pirml  'näi/  kämam "denen  erltillle  durch  Erreichen  (des  Er- strebten) ihr  Verlangen'"»  Y.  2<V.  lo.
Zam  V.  ap-.  —  ai.  'äpana-  n.  —  Pü,:  am  fa fsäa  p»rr  hati^äril  t'imak  "damit  füllt  meinen Wunsch  voll".  —  ')  D.  i.  dadurch,  dass  ihr  | sie  es  erreichen  lasst.
•  j,  hakat  daSva  "äparö  sente*''^  FrG.
■)  Die  beiden  Warter  haben  zusammen  eine 3.  Flur,  verdrängt;  etwa  *uparaßi3nit ,  lu '■raod:  I
•  j.  ä-paratay-  f.  'Ausgleich,  Sühne'  einer  I Übelthat,  usw.  durch  Leibesstrafe'*:  ka  hs asti  fi>a  (sd.)  iä  he  asti  °tis  ka^  he  asti yaeidainm  V.J.38;  39,  Ä107,  /.V-ÖS.
Zum  V.  '/.ir-,  —  Vgl.  p)t}%a:  —  Pü. :  puhr, erl. !  pa  aSir  u  sröiiaraiiim.  —  ')  Im  Gegens.
zu   h%ä;    sd.
•  p.  (,  j.)  äpi-  f.  'Wasser*:  aniyc^  'piyä (LS.)  ''ahyaia  (sd.)  '/isim'''  farabar(^  ". .ins Wasser  .  .,  das  Wasser  riss  ihn  fort"  Bh. 1. 19.
KompE.  —  Vgl.  äp-  (und  das  Verhältnis  von ai.  .■^pigi-  zu  sphig.).  —  »  D,  L.  Jpii+iim; falsch  BB.  14.  244.
•  j.  äbint-  m.  Bezeichnung  des  vierten Unterpriesters  (ratav),  der  das  beim Gottesdienst  nötige  Wasser  zu  bringen hat:  iiprn  'hns  (NS.)  äbarät  "der  Ab. soll  das  Wasser  herzutragen"  N.  77;  — 'Um  asiäya  Vr.^.i;  G.^.5,  F.j;^/ra- hr»>revä  'te  i'-i  V.5,57;  58;  —  -ts  (GS.) Vyt/j;  —  Du,  mit  sraosävars-.-  Du.: *'anaiwiarjtvs.gätu  (sd.)  aäa  'ta  (ND,) *sraoIävar?za  vlcarayat?m  N.  75.
Komp. :  äp-\-*bjril;  also  für  *äb4',  eig. •Wasserträger';  s.  N. //  und  Pü.  —  Pü.: äi(art(Transskr,),  (lu  F.}:  äp  biinär.  —  ')  N.  fc erscheint  eine  andre  Bezeichnung  dafür; äänOBiäia-  (sd.).
•  j.  ä-bar«tar-  m.  'Zuträger'  sva.  'Diener, Schaffner':  ai^qm  ?n%aüm  zarattim  *ni- bjrf^a  °ta  baraiti  "ihnen  bringtSilberund Gold  der  Schaffner  in  die  Kammer"  YL
p.  Siiiiäm  Bh.  4.  t3;  lies  abisläm  nach  IF.
8.  igz. j.  äbiis/ü  Y.  4J.  8:  lies  ä  b' ;    s,  S  No.  18.
```


## [2026-09-04T18:11:00.813Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KNT lexicon api\"; grep -n \"āpiyā\\|apiya\\|apiy\\b\" KNT.txt | tail -5; echo \"--- KNT 'water'\"; grep -n \"‘water’\\|'water'\" KNT.txt | head -8"
}
```


### [2026-09-04T18:11:00.866Z] TOOL RESULT

```
### KNT lexicon api
5005:pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
5006:apiy adv. ‘thereto, very’: Av. arpi, Skt. ápi, Gk. prep. &t ‘on’, pIE *epi (§44, §191.1). In OP, normally enclitic, but sometimes written sepa- rately; often with dūraiy ‘afar’ (5136): dürai-apty ‘far and wide’ DNa 12; düray-apiy DNa 46; dū- raiy apiy as two words, DSe 11, DZe 6, DE 19, ХРа 9, XPb 18f, ХРе 8, XPd 13, ХР? 13, XPh 10f, XE 18, XV 14, A!Pa 14^, A*He 17f. Prob- ably vafsna[pi]y X Pg 7f (Ву. BSLP 34.1.32-4) with crasis, rather than vadsnd-[cily or vasnà-[di]y (Lg.
5384:-ciy encl. particle, emphasizing or generaliz- ing, nsn. or asn. of с1-: Ау, -Git, Skt. eid, СК. т, Tat. quid, pIE *q*id (840, §84, $113, 5191.11, §201, 6998.11). In the following combinations: aciy (q.v.) ХРЇ 21. aniyaš-ciy nsn. DB 4.46; XPa 13; aniya&-c (452.1) XPh 41f; aniyai-ciy npm. XPf 29. avas-ccy nsn. DNb 55; asn. DNb 53f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
5554:-diy emphatic encl. particle: Av. zi, Skt. hi, Gk. encl. -xı in vai-xı ‘yes indeed’, of-xé ‘not at all’, pIE *ghi ($88, 5191.1). ufraštā-diy DB 4.69 (JAOS 35.351-2; not pron. apm., with Bv. BSLP 31.2.63-4, Gr. $845); hardly vasnd-[dily XPg 7f (despite Lg. 9.320; see under apiy); 7‘va-diy A’Sd 3 (JAOS 51.229).
5561:dūra- adj. ‘far (in time or space)’: Av. düra-, . NPers. dür, Skt. dürd- (5148.1). See also dürada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
--- KNT 'water'
1531:*ap- ‘water’ in inst. pl. abi$, *üp- in nom. dpi, loc. apryd.
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
2224:"$88. Tue Srems IN Stops, 1ч OP: these in- elude stems ending in £ (napdf- ‘prandson’), nf (*tunvant- ‘strong’), d (éard- ‘year’, pad- ‘foot, rād- ‘cause’), p (xSap- ‘night’, ap- ‘water’ cf. épi-) k (vif- ‘house’, vas- ‘will’).
5005:pi- sb. ‘water’: Av. áp-, NPers. db, Skt. pl. nom. dpas, acc. apás, pIE *йр-, with or without i-extension, which seems to have become 5 in OP ($422). āpišim (= apis-Sim; $41, $130) nsf. DB 1.95f. apiyálsf. DB 1.95. abis (Skt. adbhts, and dat.-abl. Skt. adbhyds, Av. aiwyó, both from *ap- bh-; §75.1V, $130, §188.V, JAOS 62.269-70; see also s.v. abi) ipf. DB 1.86.
5021:abi$ DB 1.86, probably not adv. ‘thereby’, abi- + adverbial -s, but ipf. of арі- ‘water’ (q.v.): not an error for äpiš nsf. ‘water’ as proposed by König, Кар 70-1.
```


## [2026-09-04T18:11:02.328Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD ab water\"; grep -n \"MYA\" PHD.txt PHD_mackenzie.txt | head -5; echo \"--- NYB glossary ap\"; grep -n \"^āp\\b\\|āp 'water'\\|ʾp̄ \" NYB_vol2_glossary.txt | head -10; grep -n \"water\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-04T18:11:02.396Z] TOOL RESULT

```
### PHD ab water
PHD_mackenzie.txt:658:ab [MYA < A my);)ft I M )b, N .....] water.                    'b S'u~ "r'"
PHD_mackenzie.txt:801:abgena~ ['PBynk l , MYAfJynk' IN abgina] crystal, glass.l~~J?~ r,.,,·
PHD_mackenzie.txt:5565:x6n [DMYA < Adm); hwn l I M xwn, N xun] blood.
--- NYB glossary ap
548:āpātān [’p’t’n']cultivated, inhabited 815, — Paz. äwäda; cf MPrth ’b’d (A-H III, BBB); Arm. lw. apat; NP äbäd and ābādān; < Olr *ā-pāta- ‘protected’, v. pätan (1).
172:MT’: MATA territory; small town, village MY”: MAYYA water
298:ahanj- Phnc-] pres., to draw up (water): imp. pl. ähanjet 14%, — MPrs pt, hat, pres. ?hynz-, Verbum 198; NP aähixtan ahanj-. Alternates in the same context with the simplex vb. hixtan hanj- (q.v.).
374:amah [LNH, Prth LN] pers. pron. Ist. p. pl. 1. cas. rect. we: —-ic... āyēm 913-14; to —-ic dāt hem we have been created by thee 397; ētšān (v.s.v. 04) ~ hem ke 5778; - an, ~ an: v. lan. — 2. cas. obl. us: a) dir. obj.: —-ic äkäh framāi kartan please let us know 11%; — martoman 11%; ~ (twice) proleptic obj. of zanišn 409-7; — b) virtual dat.: franāmišn ~ we must proceed 405; ~ ap i tē pat kar ne apāyet we have no need of your water 14?3; 191-2; — c) the agent of a pret. pass.: pas =: framāt HajB:11; HajA: 5.10 (Prth LN); ~ ētēn āšnūt ku 34, ete.; - d) i ~ our: dar i ~ 39, etc.; e) after a prep.: andar, apük, o ~. — Av. (295 sg.) gen. ahmākom, OP amāzam; MPrthPrs ’m’h; Paz. ema; NP ma. V. also -màn.
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
461:an-0šak [inser. 'nwšky; books 'nwšk'] immortal, a royal epithet: P2:5; 819, 10-16 passim. 783. 10515, 118%; ~-ruvan of immortal soul 108°. 1184. — Av. (114) an-aoša-, the neg. adj. of aoša(h), v. hos, from which the later Milr adj. a-hoš (q.v.) is derived. NP noš ‘the water of immor- tality; sweet; honey’; n. pr. Nosfrvàn < Anösak-ruvän.
473:ap [MY”; ’p' 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān Dp?n'] 1095. — Av. (325 sqq.) āp-, OP āpt-; MPrthPrs ’b; Paz. āw, àv; NP ab. - V. dp-cthrak, āp-sārān, āpīk.
503:apäk-puhr [LWTH pwhl] he who has a son 22%. - Cf the NP compounds with bà: bā-āb ‘having water’ and the like.
570:äp-eihrak [’p'-cyhlk'] containing the seed of the waters 87°; àp- u damik- u urvar- u gospand-cihrak containing the seed of the waters, the earth, the plants and the cattle 8711. — Av. (103 sq.) af$-cidra-; v. cihr and -cihrak.
589:apik [’pyk] belonging to water, aquatic 8219, 94%. — V. ap.
869:azat [c”t'; inser. ?z't-] 1. noble, noble- man, nobility, designation of the large class of lower Sass. nobility (v. Christen- sen, Sass. 111-113): pl. cas. rect. ~ 26*; pl eas. obl. —-än HajA:6. B:6 [’z’tn]. 169. — 2. set free from servitude, manu- mitted (of a slave), sg. cas. obl. ~-éh, v. s. v. daštan. — 1. Av. (343) ā-zāta- ‘high- born, noble’ (v.s. v. zātan), properly ‘agnate’ and therefore in the line of succession and entitled to a share in the inheritance and privileges of the clan; Arm. lw. azat; hence also Paz. àz(!)ad, Skr. v. ddhya ‘rich’ (SGV). — 2. < d- + Av. (1688) zäy- ‘to let out (water from a basin)’, cf ava-zdy- ‘to chase away’; MPrthPrs ?zd ‘free’, in this sense also Arm. lw. azat and Paz. āž(!)ād, Skr. v. svatantra ‘independent’ NP āzād; borrowed in OAram in the expression ?2't SBQ ‘to release’ (Pap. Kraeling). The earlier investigations of these two ws., which were as a rule regarded as one etymologically (by Bthl; Bailey, BSOS VI, 1930-1932, 70. 953-955; Gershevitch, JRAS 1954, 126; Benveniste, JA 242, 1954, 298-299), are now superseded by the short but masterly analysis given by Anahit Périkhanian in REA, N.S. V, 1968, 9-16, establishing, with the aid of abundant Arm. material, two hom- onyms of widely different origin and use.
```


## [2026-09-04T18:11:12.122Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON آبرو / آفتاب\"; grep -n \"^آبرو\\|آبرو:\\|آفتاب:\" MON_part1.txt | head -10; echo \"--- MON آب entries\"; grep -n \"^آب:\\|آب: \" MON_part1.txt | head -5; grep -n \"آب (\" MON_part1.txt | head -5"
}
```


### [2026-09-04T18:11:12.229Z] TOOL RESULT

```
### MON آبرو / آفتاب
920:آبرو داشتن. آب (کسی را) ریختن: بی‌عزت 
1388:آبروی او را ریختن. 
3758:آفتاب به آفتاب: رم 
3762:پنجةٌ آفتاب: بسیار زیبا. آفتاب به گل 
14234:آبرو» ارزش» قدره منزلت. اعتماد» اطمینان. 
32812:خورشد. رخسار» عارض. مثل پنجهٌ آفتاب: 
35727:عارف. بیمانه آفتاب: پیمانه‌ای که همجون 
40852:آبرومندانه. لوازم پذیرایی آبرومندانه. 
50635:آتشفشان: ( کد.) آفتاب. چشمة آفتاب: (کد.) 
54212:آفتاب: بدن خود را در معرض اشعة آفتاب 
--- MON آب entries
949:آب: ,1 )1( نام ماه پنجم 5 پاز دهم سالماه 
961:آب‌آب: 0 20-6 (امر.) آبی که هر موجود 
1792:پر آب: انار آب لمبو» آب لمیه انب لو 
1910:اپی: 70-1 (ص‌نسب. آب) منسوب به آب: 
21331:(فره.) گاز. بخار آب: گازی که از جوشیدن 
918:کرده. آب (چیزی» کسی) روشن بودن: 
920:آبرو داشتن. آب (کسی را) ریختن: بی‌عزت 
62835:در آب (دریاء اقیانوس). 
93022:استعمال می‌کر دند. (کد.) آب (دریا). (کذ.)
```


## [2026-09-04T18:11:13.556Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### BQT_v1 آبرو\"; grep -n \"آبرو\" BQT_v1_pages.txt | head -8; echo \"--- BQT آفتاب\"; grep -n \"آفتاب\" BQT_v1_pages.txt | head -5; echo \"### ARY آب\"; grep -n \"آفتاب\\|آبرو\" incoming/ARY/ARY_pages.txt | head -8"
}
```


### [2026-09-04T18:11:13.637Z] TOOL RESULT

```
### BQT_v1 آبرو
6257:و کنابه از شرمنده شدن - و رفتن :رت ءآبرو
6260:و آبرو -و رواج و رونق و طراوت دارد . *
6319:و بکسر ثاك » کنابه از رونق و رواج و آبرو
20070:و شتح اول تانش و طراوت رخار و آبروباشد .
--- BQT آفتاب
1205:«چون لغت عبری وسریانی وپهلوی تا بایام طلوع آفتاب دین عر ی
1422:سیوندی نیزاز نظار علم اصوات منفرد است ( 0۲] (خورء آفتاب) »
4164:آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
6084:بیمنی ابریق و آفتابه و مطهرء ومانند آن
6090:که‌آفتابه وابریق (۳) باشد .
### ARY آب
7172:چم اپن واژه در زبان لاتین: (هوا) صاف و آفتابی و خشکه.
```


## [2026-09-04T18:11:19.178Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '900,960p' MON_part1.txt; echo \"=== 3750,3775 ===\"; sed -n '3745,3775p' MON_part1.txt"
}
```


### [2026-09-04T18:11:19.248Z] TOOL RESULT

```
آب در جر نداشتن ۰ : مفلس بودن» سی چیز 
بودن. آ در جوی اسان ادن فولت 
رفته» با زگشتن اقبال از دست رفته. آب در 
جوی داشتن: داشتن دولت و اقال. رونق و 

تازگی و طراوت داشتن. آب در چشم 
نداشتن: بی حا بودن» شرم نداشتن. آب در 
دهان آمدن ( کسی را): آب اندر دهان 
امن [1 در دیده نداشتن شتن: شرم نداشتن» 
حباً نداشتن. آب در شکر داشتن: صعیف 
بودن؛ زار بودن. آب در چیزی کردن: دغلی 
کردن (در آن)» ناراستی بکار بردن (در 
وی). آب در هاون سودن ( کوبیدن» کوفتن): 
کار بیهوده کردن» مرتکب امری شدن که 
نتيجه نداشته باشد. آب را تيره کردن: آب 
را گل آلود کردن. میان دو یا چند تن نفاق 
انکندن» تضریب. آب رفته (روان) به جوی 
باز آمدن: با زگشتن سعادت و دولتی بشت 
کرده. آب (چیزی» کسی) روشن بودن: 
رواج داشتن» طراوت داشتن. عزرت داشتن» 
آبرو داشتن. آب (کسی را) ریختن: بی‌عزت 
کردن وی» خفیف ساختن او. آب زیر 
پوست ( کسی) افتادن: : (عم.) چاق شدن» فربه 
گر دیدن. متمول شدن. ترونمتل کو دیلن: 
آب سفت کردن: (عم.) کار بیهوده کردن. 
آب‌شان به یک جوی نمی‌رود: ۳9 

سازگار نیستند. آبی گرم کردن (با کسی): 
(عم.) جماع کردن (با وی): آمیزش کردن 
(با او). آبی گرم نشدن (از کسی): (عم.) 
بیهوده بودن توقع یاری (از او. از آب 
در آمدن: (عم.) نتیجه دادن» حاصل شدن: 
پرورش یافتن» ترست شدن. از آب کره 
گرفتن: از هر وسله استفاده‌ای (تتضویا 
مادی) بردن. خسیس بودن؛ لیم بودن. ..حق 
آب و گل داشتن تن: (عسم.) حق اقامت و 


آب فرهنگ فارسی معین ۳ 


سکونت داشتن. خود را به آب و آتش زدن: 
(عم.) به هر وسیلةٌ سخت و پر خطر متوسل 
شدن برای رسیدن به مقصود» خود را به 
مخاطره افکندن. آب‌ها از آسیا افتادن: سر و 
صداها خواییدن. تعیرات: آت نود» نانت 
نبوده ...ت چه بود؟: ذر مورد کسی گفته 
می‌شو د که هو ده به کاری اقدام کند و زیان 
بیند. وقتی که آب‌ها از آسیا افتاد. آسیا. 
آب: ,1 )1( نام ماه پنجم 5 پاز دهم سالماه 
خاص بهودی و سرانی. در اصطلاح 
سریانی رومی ماه آب با ماه ششم اغسطس 
سال ماه ترکان یعنی با ماه اوت یولیانی 
مطایق است. 

آباء: "2 ([ع. ف. آبا) ج. اب. بدران» 
اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
کنسه. آباء سبعه: هفت پدران. آباء علوی: 
پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
آناء کتسته. آباء کتسته: آباء کلیسا, 

=== 3750,3775 ===
بغل گرفتن» در بر کشیدن. 
اغول: اقبة [- آغل] (.) آغل زاغه. 
اغول: ۱ آغیل ] (.) ی به 
ی چشم از روی غضب؛ چشم آغول» 
ِ 
اناق: ۷ [ع.] (۱.) ج. افسق. افق‌هاء 
کرانه‌های آسمان» اطرات هامون. عالم؛ 
جهان. 
افت؛ ام [ع. آفهة) )۱( آنجه مابهٌ فساد و 
تباهی گردد» آشتشا بلاء » زیان: ج. آفات. 
افتاب: 220 [آفن - آب + تاب: جرم 
روشن گرمابخش] خورشید» شمس» مهر. 
نور خورشید» شعاع شمس؛ مق. ماهتاب. 
آفتاب به آفتاب: رم 
آفتاب سر دیوار: بری نزدیک به مرگگک. 
آفتاب لب بام: کسی که عمرش نزدیکث به 
اخر است. افتاب افتاب: اول روز. مثل 
پنجةٌ آفتاب: بسیار زیبا. آفتاب به گل 
اندودن: حقیقتی را با مجازی پوشیدن. 
زیبایی را با تقبیح پوشیده داشتن. 
افتاب پرست: ا25-.2 (افا.) آنکه 
آفتاب را نیایش کند. زردشتی» زرتشتی؛ 
گیر. مش رکه کافر. (جاد.) جانوری از راستة 
مارمولکان» از رده خز ندگان که زبان درازی 
برای شکار حشرات دارد و دمش بر خلاف 
مارمولکان دیگر کنده نمی‌شود و هر جای 
گیاه قرار گیرد» خود را به رنگ آن در 
می آورد: حریبا» حریایه» بوقلمون» خامالاون؛ 
حجل؛ اسدالارض» پژمره» خور؛ ماربلاس. 
(گیاء) گیاهی که تبره گاو زیان که در اراضی 
بایر روید و گل‌های کوچک و سفید و آبی
```


## [2026-09-04T18:11:28.325Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"آبرو\" MON_part1.txt | head -20; echo \"=== 1380,1400 ===\"; sed -n '1378,1400p' MON_part1.txt"
}
```


### [2026-09-04T18:11:28.402Z] TOOL RESULT

```
920:آبرو داشتن. آب (کسی را) ریختن: بی‌عزت 
1383:خوی» عرق. آبرو؛ اعتار» جاه. آب‌رخ 
1384:کسی را بردن: آبروی او را ریختن» عرض او 
1388:آبروی او را ریختن. 
1421:ناموس. آبروی کسی را ریختن: وی را 
1434:ابر وخواه: 20-0255 (- آبروخواهنده] 
1445:آیرو» با آیروه آبروداره عفیف» شر بف» 
14234:آبرو» ارزش» قدره منزلت. اعتماد» اطمینان. 
14856:شدن» بی‌آبرو گردیدن بدنام گشتن. 
14857:(امص.) بی آبروبی» بدنامی؟ ج. افتضاحات. 
22876:بر ومند: مها [< آبرومند] ((ص مر .) 
26603:آب. بسی‌رونق» بسی‌طروات. بی آبرو» 
27055:بی آبرو» بی‌عزّت: بیعرص. بی‌ناموس, 
27691:متمکن؛ ابت. معتیر» با اعشار» با آبرو. 
33724:(عم.) آبرو و اعتبار و ارزش ندارد. پهن با 
40852:آبرومندانه. لوازم پذیرایی آبرومندانه. 
43122:تلاقی: آبروا2] [ع.] (مص ع.) دیدار کردن 
54571:(مص‌جه.) وضع» اسلوب. اعتبار» آبرو؛ ج. 
67464:بی آبرو؛ بدنام» مفتضح. 
68325:آبروی وی. رگ با زگرفتن: (کن) کاهلی 
=== 1380,1400 ===

اير اهه: (0)هط-0 (امر.) راه آت؛ مجرای 
آب؛ نب راه . گذ رگاه سیل (فره.) سبلات. 

آب رخ: : 708 20-6 (امر .) آب‌رو آب‌روی» 
خوی» عرق. آبرو؛ اعتار» جاه. آب‌رخ 
کسی را بردن: آبروی او را ریختن» عرض او 
تیار وی انوم کسی وا ریک 


آبروی او را ریختن. 
اب رز؛ 30-672 (امر.) شراب باده» می. 


۳ رزان: 0 -20 (امر.) 
انگوری» آب رز. 


اثر فتاه ۲0« (امر.) (زم.) سنگی که به 
سیب جریان اب به مرور زمان ساییده و 
لغزان و مایل به گردی شده باشد. (زم.) مواد 
ته نشسته از اب رودخانه؛ ته‌نشست آب
```


## [2026-09-04T18:11:35.451Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1410,1450p' MON_part1.txt"
}
```


### [2026-09-04T18:11:35.494Z] TOOL RESULT

```
آب‌رنگ: 8 (امسر) (نق.) آب و 
رنگه اورنگ. (کد.) خنجر تیزه شمشیر 
ابدار. 

آب‌رو: --21 (امر.) عرق» خوی» آب 
رخ. اعستبار» قدرء» جاه» شرف عرض» 
ناموس» آب روی. 

ابر و: 20-7 (امر.) عرق» خوی» آب رج» 
اب روی. اعتبار» قدر» جاه» شرف عرض.» 
ناموس. آبروی کسی را ریختن: وی را 


مفتضح کردن, او را مفتضح نمودن. 


اب‌رو: (0-720۷)۲0۳ا5 زامر.) گذرگاه آب؛ 


عبر آب؛ محجرای است: تا ) کذز کاة 


لد 
ابر وخواه: 20-0255 (- آبروخواهنده] 


زوال اعتبار و ظرف خویش هراسد. شر بف. 


ابرودار: 20۲ [- ایرودارنده] (افا.) 
صاحب ایرو» خداوند ایرو» با اعتار» 
صاحب عزت با شرف. 

آسرومند: 20-۲14 (ص‌مر.) صاحب 
آیرو» با آیروه آبروداره عفیف» شر بف» 


ِِ فرهنگ فارسی معین
```


## [2026-09-04T18:11:42.510Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T18:11:42.518Z] TOOL RESULT

```


```


## [2026-09-04T18:11:46.181Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-",
 "prompt": "Give the reconstruction, gloss, descendants (esp. Proto-Indo-Iranian, Proto-Iranian, Avestan, Old Persian, Persian), and any note on the variant *ab- (Latin amnis, Old Irish ab) and Pokorny page references."
}
```


## [2026-09-04T18:11:48.516Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%AA%D8%A7%D8%A8",
 "prompt": "Give the full Persian etymology of آفتاب (āftāb): what it is derived from (Middle Persian form, components), and any cited references (Hasandust, MacKenzie, Horn)."
}
```


### [2026-09-04T18:11:52.885Z] TOOL RESULT

```
# Proto-Indo-European *h₂ep-

## Reconstruction and Glosses

The root **\*h₂ep-** has two distinct meanings:

1. **"water; body of water"** (nominal function only)
2. **"to join; attach; fasten; fit"** (verbal function)

## Key Descendants

**Proto-Indo-Iranian:**
- \*Hā́ps (water-related term)
- \*Hápsas (protruding body part)

**Proto-Iranian:**
- Ossetian: ӕфцӕг (æfcæg, "protruding part, neck")

**Avestan:**
- 𐬁𐬟𐬆𐬥𐬙𐬈 (āfənte)

## The *ab- Variant

The entry notes alternative reconstructions including **\*h₂eb-** and **\*h₂ebʰ-**. Latin *amnis* and Old Irish *ab* ("river") derive from this nominal root, reflecting the form \*h₂eph₃nés, which developed into various descendants including "river" terms across multiple language families.

## Pokorny Reference

The sources cite Wodtko, Irslinger, and Schneider's *Nomina im indogermanischen Lexikon* (2008), pages 311–317.
```


### [2026-09-04T18:11:54.635Z] TOOL RESULT

```
# Persian Etymology of آفتاب (āftāb)

Based on the Wiktionary content, here is the documented etymology:

**Middle Persian Origin:**
The word derives from Middle Persian 𐭠𐭯𐭲𐭠𐭡 (ʾptʾb /āftāb/, "sunshine"), with a comparative form 𐮀𐮎𐮃𐮀𐮁 (ʾpdʾb /ābdāb/).

**Proto-Iranian Root:**
The ultimate source is Proto-Iranian *abi-tāpáh, meaning the word is composed of two elements: "آف" (âf) + "تاب" (tâb).

**Cited Reference:**
The etymology cites a specific work: "Cheung, Johnny (2007), Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill."

The page does not reference Hasandust, MacKenzie, or Horn in the etymology section provided. The sole academic citation comes from Cheung's 2007 etymological dictionary focusing on the Iranian verb root *tap.
```


## [2026-09-04T18:12:01.665Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG tap\"; grep -n -i \"abi-tāp\\|abitāp\\|āftāb\\|aftab\" CHEUNG.txt | head -10; echo \"--- CHEUNG *tap entry\"; grep -n \"^\\*tap\\|\\*tap-\" CHEUNG.txt | head -5"
}
```


### [2026-09-04T18:12:01.728Z] TOOL RESULT

```
### CHEUNG tap
40733:aftab, 379 
--- CHEUNG *tap entry
3298:*tap ‘to seize, attach, stick, strike’ 
24669:*tap ‘to warm up, heat’ 
24686:*tap 379 
25332:*tap ‘to twist, wind’ 
25351:*tmp- (> Ir. *tap-), cf. LIV, ibid. Explaining the forms as a secondarily arisen
```


## [2026-09-04T18:12:03.201Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B1%D9%88",
 "prompt": "Give the full Persian etymology of آبرو (âbru) 'honour, reputation' — its components and literal meaning, and any Middle Persian form or cited references."
}
```


### [2026-09-04T18:12:08.587Z] TOOL RESULT

```
# Persian Etymology of آبرو (âbru)

Based on the Wiktionary entry, the Persian word آبرو derives from a compound structure:

**Components:** The word is "Shortened form of آبروی (âb-e-ruy), compound of آب (âb) +‎ روی (ruy)."

**Literal Meaning:** The compound breaks down as "âb" (water) + "ruy" (face/surface), literally meaning "water of the face" or "face-water."

**Etymology Note:** The entry identifies it as "Cognate with Northern Kurdish avrû and Central Kurdish ئاوڕوو (awrrû)," suggesting shared linguistic roots across related languages.

Unfortunately, the provided source does not include any cited Middle Persian forms or historical references beyond the etymology section itself. The entry focuses on the Modern Persian composition rather than tracing it through Middle Persian stages.
```


## [2026-09-04T18:12:10.903Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24660,24700p' CHEUNG.txt"
}
```


### [2026-09-04T18:12:10.954Z] TOOL RESULT

```
© The evidence for the corresponding Ir. root *tand of Skt. tand is confined to 
Parthian. 

«PIE *ten-d- ‘to tire’ = LIV: 627 f. | Pok.: (1066) 

*IE COGNATES: Lith. (dial.) tandus ‘lazy, sloppy’, Lat. tendo ‘I stretch’ 


*tap ‘to warm up, heat’ 

*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
be(come) hot’ — Liste: 24 

Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
YAv. täpaiieiti (Yt 6.1, Yt 7.4, Yt 17.20, etc.), ? YAv. "a.tapaiieiti (V 9.41); Partic.: perf. pass. YAv. 
ham.tapta- (V 4.46) 

*MIDDLE PERSIAN: MMP t’b- ‘to shine’ ?, BMP t’p- /tab-/ ‘to heat, burn (up); shine’. 
© No certain attestations in MMP, DMMPP: ibid. > DMMPP: 321a 

Pres.: IND. 3sg. BMP t’pyt /tabéd /, SUBJ. 35р. ? MMP t’b’d {rather Pth. 7}, OPT. 3sg. ? MMP ®t’byy, 
ІМРУ. 2sg. BMP t^p /tab/; Inf.: BMP t’ptn /taftan/; Partic.: perf. pass. BMP грі /tafi/; Pass.: pres. IND. 
35р. BMP t’pyhyt /tabihed/ 


*tap 379 


*PARTHIAN: t’b- ‘to shine, burn’ || (+ *abi-) *bd’b ‘sunshine’ || (+ *pati-) pt’b- ‘to 
burn into’ || (+ *ui-) wyt’b- ‘to shine’ (young formation) = Ghilain: 72 | DMMPP: 
321a f., 9, 360a 

Pres.: IND. 259. t’byh, 35р. t’byd, t'byd, 3р1. t'bynd, SUBJ. 3sg. t’b’h; Partic: perf. pass. П t^b'd, t’b’d || 
(+ *pati-) Pres.: IND. 3sg. pt'byd, IMPV. 2pl. pt’byd || (+ *ui-) Pres.: IND. 3sg. wyt'byd, SUBJ. 2sg. 
wyt’b’h; Partic.: perf. pass. II wyt’b’d 

*KHOTANESE: ttav- (ttau(s)-) ‘to be(come) hot’ || (+ *a) LKh. ауу- ‘to heat’ || (+ 
*nis-) nastau-/nistau-, (inch.) OKh. nastos- ‘to be consumed’ || (+ *pati-) 
pattav-/pattau- ‘to burn up; illuminate’ || (+ *ui-) LKh. byav- ‘to be hot’ || (+ *ham-) 
OKh. handau- ‘to become hot’, LKh. hamdev- (caus.) ‘to ripen’ = SGS: 38, 9, 67,
```


## [2026-09-04T18:12:23.598Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \".\\{0,140\\}ptbb\\|.\\{0,100\\}abtāb.\\{0,80\\}\\|.\\{0,100\\}āftāb.\\{0,80\\}\" PHD_mackenzie.txt PHD.txt NYB_vol2_glossary.txt | head -10; echo \"--- HRN aftab entry\"; grep -n \"aftab\\|af\\[tab\\|äftäb\" HRN.txt | head -10"
}
```


## [2026-09-04T18:12:24.697Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87%D8%A9",
 "prompt": "Give the Arabic etymology of أبهة (ubbaha) 'pomp, splendour, grandeur': what root it belongs to, and whether any Persian origin is mentioned."
}
```


### [2026-09-04T18:12:27.537Z] TOOL RESULT

```
ugrep: error: error at position 206
0-\xbf][\x80-\xbf]*){0,80}
                          \___exceeds complexity limits


--- HRN aftab entry
```


### [2026-09-04T18:12:30.926Z] TOOL RESULT

```
# Etymology of أبهة (ubbaha)

Based on the Wiktionary content provided:

**Root:** The word belongs to the Arabic root **ء ب ه** (ʔ b h), which contains 2 related terms.

**Meaning:** The noun means "greatness, majesty, grandeur."

**Persian Origin:** The page makes no mention of any Persian origin for this word. The entry focuses solely on its Arabic classification and grammatical properties as a feminine noun with a triptote singular form ending in -a.
```


## [2026-09-04T18:12:39.184Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt TAD_pages.txt ARB_mo3rb.txt ARB_abdulraheem.txt AFA.txt FVQ.txt; do echo \"### $f\"; grep -c . \"$f\" 2>/dev/null; grep -n \"ubbaha\\|أبهة\\|ubbahat\\|Ubbaha\\|ābbahā\\|āb-bahā\" \"$f\" 2>/dev/null | head -5; done"
}
```


### [2026-09-04T18:12:40.869Z] TOOL RESULT

```
### incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt
9956
### TAD_pages.txt
2291
### ARB_mo3rb.txt
18608
### ARB_abdulraheem.txt
7914
### AFA.txt
17458
### FVQ.txt
12883
```


## [2026-09-04T18:12:46.303Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- test arabic grep\"; grep -c \"الفارسية\" ARB_mo3rb.txt TAD_pages.txt 2>/dev/null; echo \"--- abha variants\"; grep -n \"ابهة\\|أبهة\\|الابهة\\|الأبهة\\|ابّهة\" ARB_mo3rb.txt TAD_pages.txt | head; echo \"--- PLA index a-\"; grep -n -i \"^abhara\\|abanüs\\|Abhar\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -5; echo \"--- PLA first entries\"; sed -n '1,40p' incoming/PLA/PLA_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-04T18:12:46.389Z] TOOL RESULT

```
--- test arabic grep
TAD_pages.txt:35
ARB_mo3rb.txt:160
--- abha variants
ARB_mo3rb.txt:13487:رفو لاسأة عي راطقل من الرجال : القصير الموق الخلق فقوطا غلى النشييه به ٠‏ والخزابهة 1 
--- PLA index a-
1396:>%1 - ’abhar: ein Ortsname in Qazwin und in Isfahan , 
1398:3%#1 - ”’abhari: Nisba v. abhar , 
--- PLA first entries
             Asya Asbaghi


Persische Lehnwörter im Arabischen




    OTTO HARRASSOWITZ   - WIESBADEN
          Asya Asbaghi
Persische Lehnwörter im Arabischen
               Asya Asbaghi


Persische Lehnwörter ım Arabischen




                    1988
```


## [2026-09-04T18:12:50.650Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1370,1420p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt"
}
```


### [2026-09-04T18:12:50.706Z] TOOL RESULT

```
u 
m äbSam: "Seidenraupenkokon" pers. 4 4. ve 


Sr- äbaqg: "Quecksilber" pers. 5 aus dem pers. dr abki "flüssig, wässerig" 
MP. „or apik . 


Sr - > ablag: "schwarz-weiß" pers. 6 aus dem pers. euı ablak "schwarz- 


weiß", wahrscheinlich mp. 9 o äblig "Blase" 7, 


Lug . 
EC»! - äblüg: "Kandis" aus dem pers. &+: abluf "weißer Kandis" 8 0d.0%7 
ablük "Staubzucker", mand. ablus 9 Ss. abdüf. 
BY - ”abuz: Pl. v. ;L bäz "Falke" s. bäz, 
.,. >= 10 < 
An - abü-zarßmihr: Name des Nuschiwans Großwesir pers. „_,, 


Bozorgmihr mp. Is Dıqı Vazurg-mihr il, 


3 - - 
>%1 - ’abhar: ein Ortsname in Qazwin und in Isfahan , 
E - 
3%#1 - ”’abhari: Nisba v. abhar , 


-..3 - - 
Qml- ’abirag: eine Abkürzung für Gr ’istabrag 12, 


1. LD. s. v., Steingaß s. v. 
2. Kiyä S. 6 

3. Nyberg Bd. II s. v. 

4. Steingaß s. v. 

5, LD. s. v., Steingaß s. v. 
6. ebda. 

7. Mackenzie Ss. v. 

8. Muhit s. v. 

9. Macuch S, v.
```


## [2026-09-04T18:13:12.378Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FSF آب\"; grep -n \"آب:\" FSF.txt | head -5; grep -n \"فر و آیین و آب\\|آیین و آب\" FSF.txt FRS.txt BQT_v1_pages.txt | head; echo; echo \"### BQT آب entry region\"; grep -n \"^آب \\|آب . بر وزن\\|بر وزن ماه\" BQT_v1_pages.txt | head -5; sed -n '6250,6330p' BQT_v1_pages.txt"
}
```


### [2026-09-04T18:13:12.481Z] TOOL RESULT

```
### FSF آب
FSF.txt:377:جهان گشت با فر و آیین و آب 

### BQT آب entry region
4882:آب اعد فر انسوی )
5869:آب ۲ تش د نگ - یکس شالت ؛
5871:آب ۲ تش دای با زای‌هوز. بنی
5872:آب آش رنگ است ک هکنابه از شراب لعلی -
5874:آب هم میگوند .
و استخر (۳) و امثال آنرا نیز کون که مردمان
و جانوران از آنجا آب خورند » و آنجاراپعریی
منپل و عطن خوانند - و ظرف آبخوربرا حم
کفته اد - و بمعنی توقف نمودن و مقام کردن
آپ شیب
هم هست ۴ .
آب شلن - بمعنی کداختن باشد -
و کنابه از شرمنده شدن - و رفتن :رت ءآبرو
و برطرف شدن رولق و رواج هم هت .
۲ پش دوشن است « نی عزت
و آبرو -و رواج و رونق و طراوت دارد . *
آب شناس - کنابه از حقیق‌هنلی-
و فاعده دان - وصاحب مهارت درعلوم باشد (4)-
و تخصی را لیز کویند که بر بالای تیر کشتی
برآمده ا صلاح و فاد دربا خبر دعدب وشخصی
که آب کاریز و چاه رامیشناسد بعنی میداندکه
کدام جای از زمین آب دارد وکدام جاندارد ؛
و آب شناسان جمم آب‌شنای است نی قاعه ‏
دانان .
آ بشنگ. ختح رابع بر وزن آبرنگه
بىعنی اول آپزن است و آن ظرفی باشد از می
و امثال آن بمقدار قامت آدمی که طبیبان مار
را در آن خوابانند و ادویهٌ جوشاننه در آن
بت سم
اب شنگر ی » بک ات .کنابه
۲۳۶۱
اب شیت بت یک رابع و سکون‌انی
و تحتالی وبای ابجد , راهگنر آب را گونن دکه
از بالا بزیر آورده باشند .
(4) خم ۳ : - باشد .
مقام کردن :
ببهرام داد ان زمان دخترش
۵ آبشی - رك : آوشن .
۴ - پمعنی منزل و مقام وموطن است ؛ نه
۳ ۰آب صفت بودن - کنابه از یار
بفم و فایده رسانیدن باشد - و بالقواضم بودن‌را
نیز گویند.
آب طبرستان - بکسر ثاك »
چشمه‌است روان در کوهی که اکر بانگه , برآن
ود ند و چون فربادکنند پنهان خودوچون
طلب نمایند روان گزدد ؛ و این حنال هر هر
سای از آن چشمه مکرد بفعل میآید .
چشمه‌ایت که مدت هفت سال بیوستهروان‌باشد
و هفت سال دیگر خشك نود .
شراب انگوری باشد .
۲ ب‌عشر ت - بکس الك و عبن می
شمه » بىمنی آب طربست که شراب انگوری
باشد
! شت س بفتح ثالث بر وزن وارفت »
حخفف آبافت است که بارچه گنده و سطبر
باشد ۷ .-
آب سر ۵۵ - بکس تاك , کنایه‌از
-شنشی ی وخنجر باشد و شیشه و پلور و آبگینه
را نیز کویند .
] ها هد بت تالث بر وزن اوك ۰ مکی
از نلبهای سیماب است و آنرا آب و آیق
سس ۰ ۷..--
و ابوالارواح و اصل و االاجاد و پرنده و ده
و تیر وناقة (۱) وجوهر وجیوه و حل‌النهب(۷)
وحی‌الماء و روح و روحانی و رجراج و زارق(۳)
و ژموم (4) و ژبوه و ستاره و سحاب و نور (۵)
و سیماپ و طبار و عبد و عطارد و عین الحیوان
و غبیط وغیان وفرار و گریزنده ولین ولجلاح(»)
9 را نیز خوان که طفلان
پر هیآ ورند و صم ثالث هرچیز پر آیوآبکی
وا میگویشد .
یکااه - بسکون ثالث بر وزن آیبار ,
پمعنی سقا باشد - و شراب‌خوار (۷) و شراب
فروش - و حکاك - و نگین‌ساز را نیز کویند(۸)-
و بکسر ثاك » کنابه از رونق و رواج و آبرو
بلشد : #
۲ یکاهه - بر وزن کارامه . نان‌خورشی
است ممروف که در صقلعان (4) ازماست وشیر
و نم سپند و خمیر خشكث شده و سر که سازند
و آنرا جربی مری خوانند .
۲ یکافه - با بلی فارسی بر وزن تابشانه, "
بجه آدمی با حیوان دیگر که نارسیده از شکم
مادر سفئد .
۲ بگاه - بر وزن خوابگاه . تهیگاه
ظي هست ۰
خم ۳ : اسطخر .
```


## [2026-09-04T18:13:19.717Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '365,392p' FSF.txt"
}
```


### [2026-09-04T18:13:19.761Z] TOOL RESULT

```
۳۶۵-۴): 
مکن کاری که من با تو نکردم 

مبر آبم که من آبت نبردم 
۲-اشک: 


فرو ريخت آب از دو دیده به درد... 
(۲۳۹۲-۲۲۶۵) 
۲ رای سوه 
چو آمد به‌برج حمل آفتاب ۱ 
جهان گشت با فر و آیین و آب 
(۷-۲۸-۱ 
حافظ (غنی» ۴۳۲): 
مخمور جام عشقم ساقی بده شرابی 
پر کن قدح که بی مِیٰ مجلس ندارد آبی 
۴-شادابی طراوت: ۱ 
دو جادوش پر خواب و پر آب روی 
پر از لاله رخسار و پر مشک موی 
(۴۴۴-۱۶۵-۱) 


اباد 


۵-عرق تن» خوی: 
دهن خشک و غرقه شده تن در اب
```


## [2026-09-04T18:13:25.087Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '350,372p' FSF.txt; echo \"--- pages file\"; grep -n \"جهان گشت با فر و آیین و آب\" FSF_pages.txt"
}
```


### [2026-09-04T18:13:25.156Z] TOOL RESULT

```
می‌فرستد و می‌گوید ] 
اگر آب دارد تو را میزبان 
بران شهر خرم دو هفته بمان 
(۱۸۰۱۲-۱۱۷-۳) 
(یعنی اگر میزبان عزت و احترام و 
آبروی تو رانگه دارد]. 
از ناصر خسرو (دبوان ۱-۴۵): 
زین سراب تشنه کش [جهان ] پرهیز کن 
تشنگان بسیار کشتست این سراب 


روی تازه‌ات زی سراب او مله 
تانریزد زان سراب از رویت آب 
از خر کت رگانی (ویس و رامین 


۳۶۵-۴): 
مکن کاری که من با تو نکردم 

مبر آبم که من آبت نبردم 
۲-اشک: 


--- pages file
```


## [2026-09-04T18:13:36.409Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY latin index AB\"; grep -n -i \"^AB\\b\\|AP (\\|water\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"--- ARY pages آب\"; grep -n \"آب (\\|آب:\\|ریشه.*آب\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-04T18:13:36.471Z] TOOL RESULT

```
### ARY latin index AB
187:Ab 8357 5 ASF SF 4 Sb yuthel
519:Ab shoal etbtth til 92 S pte 9 SUR L Wj eat 37 22 end GOL,
775:Ae Be Ves dhe 395 33 9) Zap (TACITUS) a. gealiy slo NF LT pa
782:AB eB ree SBE EVV 6) cle calS Ab J (53910 JV Dees
1164:AB SET JS ons ste 59 (Gps Sica Say esl ') 65 pis Dltatls Lg as
1358:AB, AP (PAHLAVI) 6 shy,
1361:MACKENZIE: (WATER) 139 APIA GREEK) gli
1362:BUCK: (WATER) 34-35 AMNIS LATIN) 3
4375:ab POKORNY 840-841 FOLEN GERMAN) ,glsT
6279:‘REFERENCES eho CHAP (AFGHANI)( 4) gsi!
--- ARY pages آب
```


## [2026-09-04T18:13:37.950Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%A8",
 "prompt": "For the Persian entry آب: give the full etymology (Middle Persian, Old Persian, Proto-Iranian, PIE root), the list of senses (including any 'lustre/sheen/gloss' or 'honour' sense), and derived terms like آبرو. Quote the etymology section."
}
```


### [2026-09-04T18:13:46.614Z] TOOL RESULT

```
# Persian Etymology and Senses for آب (āb)

## Full Etymology Chain

The Persian entry traces back through multiple language stages: "From Middle Persian _[ʾp̄](/wiki/%CA%BEp%CC%84#Middle_Persian "ʾp̄")_ (āb), from Old Persian _[𐎠𐎱𐎡𐎹𐎠](/wiki/%F0%90%8E%A0%F0%90%8E%B1%F0%90%8E%A1%F0%90%8E%B9%F0%90%8E%A0#Old_Persian "𐎠𐎱𐎡𐎹𐎠")_ (ap-), from Proto-Iranian _[\*Hā́fš](/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1 "Reconstruction:Proto-Iranian/Hā́fš")_" and ultimately "from Proto-Indo-European _[\*h₂ep-](/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep- "Reconstruction:Proto-Indo-European/h₂ep-")_ ("water, body of water")."

## Senses Listed

The word carries five distinct meanings: (1) water, (2) liquid, (3) juice, (4) river, and (5) honour/reputation/standing.

## Selected Derived Terms

Notable compounds include: آبرو (prestige/dignity), آبشار (waterfall), آب و هوا (climate), آب‌انبار (reservoir), and ضدآب (waterproof).
```


## [2026-09-04T18:13:53.409Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1340,1375p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== pdf page tags near ===\"; awk 'NR<=1375 && /pdf page/ {p=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt; grep -n \"pdf page\" incoming/ARY/ARY_latin_index_pages.txt | awk -F: '$1<1375' | tail -3"
}
```


### [2026-09-04T18:13:55.908Z] TOOL RESULT

```
Syl p gPAPF (GLUT yPUFF JS laos baa Sa 9 typ orb chao j)s-F
Lasgly gel UT Layla gant leas PAFEN sls yPUST (S,luls » BOUFFEE
Somme YET algal y ta Gat ply Called, a
oY choot G agen 9 plan cleesly lal y ole MEET lane LT Ad
feu! Slit| PENSARE .plJls| PENSAR elilel y PENSER (541) » PENSARE
JICOISA lit COSA Lill CHOSE spi} glaesTsb eer 8 valet
UT yy! y ain Gately Sleds ar 55 odly cpl LT alo glean alm y ell
Somer
Sep IE y lpr I Kay aly Sua godly eae y badly oul hat aly
lena seydin, tokfy tobels yey ge ay,dim
hagas
[pdf page 50]
Fe . ins
ats
|
[ware tees ty ar |
APE (OLD PRUSSIAN) AS 3. ‘AP, APAM AVESTAN) gles)
ABANN: HOLD IRISH) pS 5332) API, APUS (OLD PERSIAN) gal go,
AB, AP (PAHLAVI) 6 shy,
REFERENCES eh ‘AY, DjYRAV KURDISH) 3,5
POKORNY: . 51-52 Ae, APA (SANSKRIT) 2 Sie
MACKENZIE: (WATER) 139 APIA GREEK) gli
BUCK: (WATER) 34-35 AMNIS LATIN) 3
MALLORY 129 EAV APRENCH) si
1 igbG ob, UPE A(LITHUANIAN) gigs
ro sfaseos al cai UPE ALATVIAN) (3) is)
_ ATER ATARSH —(AVESTAN) gus)
‘REFERENCES breathy ATUR, ATAXSH (PAHLAVI) by
POKORNY, ar) AGIR (KURDISH) 52,5
DELAMARRE: (BEU) 179 ATHARVAN, — (SANSKRIT) © Site
MACKENZIE: (FIRE) 114 EDHOS, HUTASH u<o5
BUCK: n AIREM ARMENIAN) gs,\
AMINDAROV: (BIRE) 247 AITHOS GREEK) li
Ir-tF iebG oly ATER _— ALATINY a3 “a
FO-PF Mes eal cid EIT HOLD FRISIAN) (75 523
AITH OLD IRISH) S43 p
=== pdf page tags near ===
1305:[pdf page 48]
1333:[pdf page 49]
1351:[pdf page 50]
```


## [2026-09-04T18:14:07.181Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"AFTAB\\|AFTAB (\\|TAP, TAB\\|TAPAYEITI\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T18:14:07.229Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T18:14:08.653Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87#Arabic",
 "prompt": "Give the Arabic verb أبه (ʔabiha) — its meaning, its root, and any derived nouns including أبهة. Is any foreign (Persian) origin mentioned?"
}
```


### [2026-09-04T18:14:14.403Z] TOOL RESULT

```
# Arabic Verb أبه (ʔabaha/ʔabiha)

## Meaning
The verb means **"to pay attention," "to heed,"** or **"to take notice."**

## Root
The root is **ء ب ه** (ʔ b h), a three-letter Semitic root shared by two terms in the dictionary.

## Derived Forms
According to the conjugation table, derived nouns include:
- **Verbal noun**: أَبَه or أَبْه (ʔabah, ʔabh)
- **Active participle**: آبِه (ʔābih)
- **Passive participle**: مَأْبُوه (maʔbūh)

## Foreign Origin
**No mention of Persian origin appears** in the Wiktionary entry provided. The entry categorizes this as an Arabic form-I verb with standard Semitic root structure, but contains no etymological notes suggesting external linguistic origins.
```


## [2026-09-04T18:14:20.535Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D9%87%D8%AA",
 "prompt": "Is there a Persian entry for ابهت? Give its etymology (Arabic source word) and meaning."
}
```


## [2026-09-04T18:14:22.280Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1",
 "prompt": "Give the Proto-Iranian reconstruction *Hā́fš 'water', its descendants (Avestan, Old Persian, Middle Persian, Persian, Sogdian, Khotanese), and the PIE source."
}
```


### [2026-09-04T18:14:24.718Z] TOOL RESULT

```
# Persian Entry for ابهت

Yes, there is a Persian entry for **ابهت** (ubbahat/ubuhhat).

**Etymology:** The word was "Borrowed from Arabic _[أُبَّهَة](/wiki/%D8%A3%D8%A8%D9%87%D8%A9#Arabic "أبهة")_ (ʔubbaha)."

**Meaning:** The term denotes "magnificence, grandeur, imposing presence." The example provided illustrates this as referring to a commanding or dignified appearance that someone without a beard supposedly lacks.
```


### [2026-09-04T18:14:28.375Z] TOOL RESULT

```
# Proto-Iranian *Hā́fš 'Water'

**Proto-Iranian Term:** *Hā́fš (feminine noun meaning "water")

**Etymology Source:** The term derives from "Proto-Indo-Iranian *Hā́ps, from Proto-Indo-European *h₂ep-"

**Key Descendants:**

- **Avestan:** āfš (nom.sg. in Younger Avestan)
- **Old Persian:** āpī[š] (nom.sg.)
- **Middle Persian:** āp/āb (Pahlavi and Manichaean scripts)
- **Classical Persian:** آب (āb)
- **Sogdian:** āp (multiple script variants)
- **Khotanese:** Not explicitly listed as a descendant in this entry

**Additional Notable Reflexes:** The reconstruction shows widespread descendants across Iranian branches, including Kurdish (av), Pashto (āb), Baluchi (áp), and numerous other regional varieties, demonstrating the antiquity and stability of this water-related term throughout Iranian language evolution.
```


## [2026-09-04T18:14:30.070Z] AGENT

Now let me archive all the web sources I used.


## [2026-09-04T18:14:35.705Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%AA%D8%A7%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B1%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D9%87%D8%AA\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 32, root Ab1/Ap1 'water' (PART 2): nodes ap/ab, aftab, abru, Arabic ubbaha, Persian obbahat\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T18:14:38.842Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b60009fa4b7f1c12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a6ba4e0fea3b8f19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a4bcccc2e05357e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/481e10d7c983be67.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcd40df518ed1b47.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9271f40e20f0e45d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b6fb8fe67946706.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be3348e92a3dd02f.txt
```


## [2026-09-04T18:14:43.525Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### aftab\"; grep -n -i -A4 -B2 \"abi-tāp\\|Etymology\" 481e10d7c983be67.txt | head -40; echo; echo \"### ab honour\"; grep -n -i \"honour\\|reputation\\|standing\" a4bcccc2e05357e4.txt | head -6"
}
```


### [2026-09-04T18:14:43.590Z] TOOL RESULT

```
### aftab
63-
64- 1.2 
65: Etymology 
66-
67- 1.3 
68- Noun 
69-
--
83-
84- 2.2 
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
--
97-
98- 3.1 
99: Etymology 
100-
101- 3.2 
102- Noun 
103-
--
111-
112- 4.2 
113: Etymology 
114-
115- 4.3 
116- Pronunciation 
117-
--
134-
135- 5.1 
136: Etymology 
137-
138- 5.2 
139- Pronunciation 
140-
--

### ab honour
1940: honour , reputation , standing
```


## [2026-09-04T18:14:46.544Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"tāp\\|Cheung\\|ʾptʾb\\|abi-\\|Middle Persian\" 481e10d7c983be67.txt | head -20"
}
```


### [2026-09-04T18:14:46.595Z] TOOL RESULT

```
332: From Middle Persian 𐭠𐭯𐭲𐭠𐭡 ( ʾptʾb /⁠āftāb⁠/ , “ sunshine ” ) (compare 𐮀𐮎𐮃𐮀𐮁 ( ʾpdʾb /⁠ābdāb⁠/ ) ), from Proto-Iranian *abi-tāpáh [ 1 ] Equivalent to آف ( âf ) +‎ تاب ( tâb ) .
439: ^ Cheung, Johnny ( 2007 ), “ *tap ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN 
545: Persian terms inherited from Middle Persian 
546: Persian terms derived from Middle Persian 
586: Middle Persian terms with redundant transliterations
```


## [2026-09-04T18:15:30.661Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD aftab?\"; grep -c \"ptp\\|āftāb\\|abtāb\" PHD_mackenzie.txt; grep -n \"tāb-\\|tāftan\" PHD_mackenzie.txt | head -3; echo \"### KLN leaf 45 head\"; python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nt=d[45]\nprint(t[:200]); print('...'); \ni=t.find('amnic')\nprint(t[max(0,i-400):i+50])\n\""
}
```


### [2026-09-04T18:15:32.956Z] TOOL RESULT

```
### PHD aftab?
0
### KLN leaf 45 head
ddle’,  fr.  on  (see  a-,  ‘on’),  and  middan, dat.  sing.  masc.  of  midde,  adj.  See  mid  and  cp. amidst.
amide,  amid,  n.,  a  compound  obtained  by  re¬ placing  one  hydrogen  atom  in  a
...
,  fr.  I.-E.  base  *men-,  ‘to  think,  remember’. See  mind  and  cp.  next  word.  Cp.  also  anam¬ nesis,  paramnesia.  For  the  ending  see  suff.  -ia. amnesty,  n.,  general  pardon.  —  F.  amnestie,  fr. L.  amnestia,  fr.  Gk.  apvTjaTta,  ‘forgetfulness, fr.  a-  (see  priv.  pref.  a-)  and  ptvrjcmp,  ‘remem¬ brance’,  which  is  rel.  to  pivaopm,  ‘I  remember’. See  prec.  word.
amnic,  adj.,  pertaining  to  a  river.  —  L.  a
```


## [2026-09-04T18:15:36.948Z] AGENT

Now I'll write the verification file.


## [2026-09-04T18:18:29.365Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-32.json <<'JSONEOF'\n{\n  \"pdf_page\": 32,\n  \"book_page\": 2,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ab 1, Ap 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂ep- 'water, body of water' (Pokorny 2. ap-/āp- 'Wasser, Fluß', IEW 51-52; the collateral form ab- 'Wasser, Fluß' at IEW 1)\",\n      \"note\": \"The root is real and the gloss 'water' is right; 'Indo-European' is the correct language label. Nourai's double headword 'Ab 1, Ap 1' reproduces Pokorny's own двух-entry treatment: IEW p.1 has 'ab- \\\"Wasser, Fluß\\\"' (Lat. amnis < *abnis, OIr. ab/abann, W. afon), IEW pp.51-52 has '2. āp- \\\"Wasser, Fluß\\\"' (Skt. āpaḥ, Av. āfš/āpəm, OPers. āpi-, NPers. āb, Lith. upė, OPruss. ape), and Pokorny explicitly links them (p.52: 'Daneben kelt.-lat. ab-, s. u. ab-'). Modern reconstruction is a single *h₂ep-; Latin amnis and OIr. ab are now normally taken from an -n- stem *h₂ep-h₃on-/*h₂ep-n- of that same root rather than from an independent *ab-, so 'Ab' as a separate root is no longer maintained, but it is not a wrong word — only a superseded analysis. Nourai's own page reference POK:1 lands on the Celtic/Italic half; his whole Iranian chain sits on IEW 51-52, which he does not cite here. NOTE ON THE CHART AS A WHOLE: the Persian branch on this page is Paul Horn's 1893 analysis (āb 'Glanz' as the first element of āftāb, ābrū), and the Arabic branch is Addi Shir's 1908 claim that Arabic أبهة is Persian آب بها. Both were already doubted in the 19th c. (Hübschmann) and are rejected by current Iranian and Arabic lexicography (Cheung 2007; Asbaghi 1988).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82ep-\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:1\",\n          \"status\": \"partial\",\n          \"note\": \"POK_01.txt form-feed leaf 8 = printed p.1 (offset leaf = p+8): 'ab- \\\"Wasser, Fluß\\\". Lat. amnis f., später m. (*abnis); air. ab (*abā) Gen. abae \\\"Fluß\\\", daneben abann, cymr. afon … WP. I 46 f.' — the page confirms an IE root ab- 'water, river', so the root box and its gloss are supported. But this page contains NO Indo-Iranian material: Avestan/Old Persian/New Persian āp/āb are at POK pp.51-52 (leaf 59-60), '2. āp- \\\"Wasser, Fluß\\\": Ai. āp- f. \\\"Wasser\\\" … av. Nom. Sg. āfš, Akk. Sg. āpəm … Daneben kelt.-lat. ab-, s. u. ab-.' Nourai cites only the first page, hence 'partial'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Pahlavi\",\n          \"words\": \"âp\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *h₂ep- (Pokorny 2. āp-) → Proto-Indo-Iranian *Hā́ps → Proto-Iranian *Hā́fš, a root noun in -p-. In Avestan the nominative singular shows the regular Iranian devoicing of *-p-s to -fš (YAv. āfš), while the oblique stem keeps the labial: acc. sg. āpəm, gen. pl. apąm; the Waters are personified (Ābān Yašt, Y. 65 Āpąm Nəpāt). Old Persian has the i-extended stem āpi- (Bīsutūn 1.19 apiyā 'into the water', 1.95 āpiš). In Middle Persian the Avestan/OP form is continued as āp/āb, written ʾp̄ in Book Pahlavi (Aramaic ideogram MYA 'water'), ʾb in Manichaean, which is exactly what Nourai's node 'âp' represents; intervocalic and final Iranian -p- lenites to -b/-w in Middle and New Persian, giving NP āb (Pāzand āw). So one label covering Avestan and Pahlavi 'āp' is legitimate: the Pahlavi book-form is still written with the p-grapheme.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/H%C4%81%CC%81f%C5%A1\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:2\",\n              \"status\": \"not_found\",\n              \"note\": \"Klein 1966 vol. I p.2 (KLN_1966.txt form-feed leaf 13, the leaf that carries printed pp.2-3) runs 'abase … abash … abasia … abate … abatis … abattoir … abb … abba … abbacy … abbé … abbess'. There is nothing on Avestan or Pahlavi 'āp' there. Klein DOES support the claim, but at another page: s.v. amnic (KLN_1966.txt line 2497, leaf 45 ≈ printed p.67): 'L. amnicus, fr. amnis, \\\"river\\\", which stands for *ab-nis and is cogn. with OIr. abann, ab, W. afon, \\\"river\\\", fr. I.-E. base *ab-, a collateral form of base *ap-, \\\"water, river\\\", whence OI. āpah, apah, Avestic af-sh, \\\"water\\\" …'; and s.v. doab (line 11940): 'Pers.-Hind. doab, lit. \\\"two waters\\\" … db \\\"water\\\" … rel. to OI. āpah, apah, Avestic āp-, \\\"water\\\"; see amnic.' So the citation number 2 appears to be wrong (67 or 78 would be right); the substance is Klein's.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"cols. 325-330 s.v. āp-, and col. 330 s.v. āpi-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt (form-feed region printed '327 äp- I A'): 'āp- … n. \\\"Wasser\\\"' with the whole Yasna/Vidēvdād documentation, closing 'ai. āpa, āpaḥ, apām; np. āb. — Pü.: āp' — Bartholomae himself gives the Pahlavi (Pü. = Pahlavi version) form āp and NPers. āb. Immediately after: 'p. (j.) āpi- f. \\\"Wasser\\\": aniya⁰ ʾpiyā ahyata … Bh. 1.19' — the Old Persian form.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Lexicon s.v. āpi- (KNT.txt line 5005)\",\n              \"stance\": \"supports\",\n              \"note\": \"'āpi- sb. \\\"water\\\": Av. āp-, NPers. āb, Skt. pl. nom. āpaḥ, acc. apáḥ, pIE *āp-, with or without i-extension … āpišim nsf. DB 1.95f. āpiyā lsf. DB 1.95. abiš … ipf. DB 1.86.' Also §88: 'stems ending in … p (xšap- \\\"night\\\", ap- \\\"water\\\")'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"p. 4 s.v. āb\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD_mackenzie.txt line 658: 'āb [MYA < A myʾ; ʾp̄ | M ʾb, N ~] water.' MacKenzie's Pahlavi headword is āb, spelled ʾp̄, ideogram MYA — precisely the 'Pahlavi āp' of the node.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"vol. II Glossary s.v. āp\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt line 473: 'āp [MYʾ; ʾp̄ 607. 787. 862.6, 878-11] water 1416-26 and passim; pl. cas. obl. āpān … — Av. (325 sqq.) āp-, OP āpi-; MPrthPrs ʾb; Paz. āw, āv; NP āb.' Nyberg's chain Avestan → OP → MP → NP is Nourai's chain.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW pp. 51-52 (POK_01.txt leaves 59-60)\",\n              \"stance\": \"supports\",\n              \"note\": \"'2. āp- \\\"Wasser, Fluß\\\". Ai. āp- f. \\\"Wasser\\\", z. B. Pl. Nom. āpaḥ, Akk. apáḥ, Gen. apām, av. Nom. Sg. āfš, Akk. Sg. āpəm, Instr. Sg. apa(-ca) …'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins appendix s.v. ap-²\",\n              \"stance\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'ap-². Water, river. Iranian ap- in Persian āb, water: JULEP. [Pok. 2. ap- 51.]' — Watkins routes the Persian word through Iranian ap- exactly as the chart does, and cites Pokorny 51, not 1.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck §1.31 WATER, group 3\",\n              \"stance\": \"supports\",\n              \"note\": \"SYN.txt: '3. IE *āp-. Walde-P. 1.46. Skt. āp-, ap- mostly pl. āpas … Av. āp-, ap- the reg. word for \\\"water\\\", also freq. personified, OPers. āpi-, NPers. āb \\\"water\\\". Elsewhere only of \\\"running water\\\" in words for \\\"river\\\", as Lith. upė, Lat. amnis, Ir. abann, etc.' Buck also gathers ab- and ap- under one head at §1.36: 'From IE *ap (and ab-) \\\"water\\\", Skt. āpas, etc.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I p. 46-47 (WLD_Bd1_pages.txt leaves 54-55)\",\n              \"stance\": \"supports\",\n              \"note\": \"The leaf headed '46 … ap ap-' opens the ap-/āp- article that Pokorny p.51 abbreviates ('WP. I 46 f.' is the standard cross-reference given both at IEW 1 and at IEW 51); the following leaf continues 'ap-, āp- — apo …' with the Flußnamen auf -apa material.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, IE roots of Persian, pdf p. 50 (printed p. 51), entry آب\",\n              \"stance\": \"supports\",\n              \"note\": \"ARY_latin_index_pages.txt (after '[pdf page 50]') lists for آب: 'ĀP, APĄM (AVESTAN); ĀPI, APUS (OLD PERSIAN); AB, AP (PAHLAVI); ĀV, DJYRAV (KURDISH); ĀPAḤ, APA (SANSKRIT); APIA (GREEK); AMNIS (LATIN); ABANN (OLD IRISH); APE (OLD PRUSSIAN); UPĖ (LITHUANIAN/LATVIAN)' with 'REFERENCES: POKORNY 51-52; MACKENZIE (WATER) 139; BUCK (WATER) 34-35; MALLORY 129'. An independent modern Persian handbook thus puts the Pahlavi form AB/AP under the same root and, like AHD, cites Pokorny 51-52 rather than 1.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"âb «آب ۲»; âberŭ «آبرو»; âftâb «آفتاب»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) āb «آب ۲» 'glitter, lustre': the words are real and the sense is real — classical Persian āb means 'sheen, water (of a sword or a pearl), freshness, honour' beside 'water', and Wiktionary lists 'honour, reputation, standing' as sense 5 of āb itself, i.e. as a metaphorical extension of āb 'water' (the glint of a water surface, the 'water' of a blade), not as a separate lexeme. Horn set it up as a separate lemma no. 3 āb 'Glanz' compared with Skt. ābhā- 'Glanz', but in his own footnote conceded 'Die Zusammenstellung von np. āb und skr. ābhā- ist keineswegs sicher; von der Bedeutung \\\"(glitzernder) Wasserspiegel\\\" könnte man sehr leicht zu \\\"Glanz\\\" kommen' — which is Nourai's derivation. Hübschmann §75a repeats that the equation with ābhā- is 'unsicher'. So treating «آب ۲» as the water word used metaphorically is the better-supported view and Nourai's edge #1→#2 stands. (b) ābrū «آبرو» 'good repute': a transparent Persian compound āb + rū(y) 'face' (shortened from āb-i rūy), literally 'water of the face', paralleled by Kurdish avrû/awrrû. But the received Persian reading of the literal sense is 'the water/sweat of the face' — Mo'in glosses آب‌رخ and آب‌رو first as 'عرق، خوی' (sweat) and only then as 'اعتبار، قدر، جاه، شرف، عرض، ناموس' — not Nourai's 'facial shine'. Route: no Middle Persian *āb-rōy is attested; the compound is a New Persian formation, current from the earliest classical poetry. (c) āftāb «آفتاب» 'sun': this is where the chart is wrong. āftāb does not contain āb. It continues Middle Persian ʾptʾb /āftāb/ 'sunshine' (Parthian ʾbdʾb /ābdāb/ 'sunshine'), from Proto-Iranian *abi-tāpah = the preverb *abi- 'on, upon' (Av. aiwi-, OP abiy-) + the root *tap- 'to be hot, to shine' (Av. tāpaiieiti, BMP tʾp- 'to heat, burn, shine'). Iranian *-bit- gave MP -ft- regularly (*abi-tāpa- > āftāb, cf. the same preverb in āfrīn < *abi-θrai-, āfarīdan), so the first syllable is a prefix, not the noun āb; the parallel Parthian ābdāb with -d- shows the preverb, not 'water'. Nourai simply inherits Horn's 1893 grouping (Horn lists af-tāb among the compounds of his āb 'Glanz'), and Mo'in's dictionary repeats it ('آفتاب [آب + تاب: جرم روشن گرمابخش]'), but Cheung's Etymological Dictionary of the Iranian Verb (2007) s.v. *tap and the Manichaean dictionary evidence settle it against them.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D9%81%D8%AA%D8%A7%D8%A8\",\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D8%B1%D9%88\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:1\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p.1 (HRN.txt form-feed leaf 22, offset leaf = printed + 21) is exactly the page Nourai used. It has '2. āb, āw \\\"Wasser\\\" … ap. āp- \\\"Wasser\\\"; aw. āp-; phlv. āp (pāz. āw); ai. āp-, kurd. āw; afγ. ōba (fem.); bel. ap, n. āf' and then '3. āb \\\"Glanz\\\" (Šāhn. I S. 14 Vers 7), vergl. āb|rū, āb|tāb, āb|mend, Rōd|ābe, Suhr|āb, Mihr|āb, Ardā Vīr|āf, af|tāb, phlv. āb; skr. ābhā- \\\"Glanz\\\". afγ. bel. LW. āb, ābrū; kurd. LW. āwrū.' So Horn is the source both for the separate lemma āb 'Glanz' and for filing ābrū and āftāb under it — Nourai's node is a faithful copy. Horn's own footnote 2 on the same page, however, undercuts half of it: 'Die Zusammenstellung von np. āb und skr. ābhā- ist keineswegs sicher; von der Bedeutung \\\"(glitzernder) Wasserspiegel\\\" könnte man sehr leicht zu \\\"Glanz\\\" kommen.'\"\n            },\n            {\n              \"ref\": \"AEF:2\",\n              \"status\": \"not_checked\",\n              \"note\": \"AEF = Jalāl Khāleqi Motlaq, Asās-e Eštteqāq-e Fārsi vol. I (Bonyād-e Farhang-e Irān 1356/1977), which is the Persian rendering of Horn's Grundriss with Hübschmann's notes. refs_online.json records it as not online (no archive.org / noorlib copy; 2015 Mehrāfrūz reprint print-only) and there is no local text. Since it is Horn in Persian dress, its p.2 will be Horn's nos. 2-3, i.e. the same content already checked under HRN:1.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien §75a, p. 172 (HUB.txt line 6401)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Da āb \\\"Glanz\\\" == skr. ābhā- H. 3 unsicher ist, so ergiebt sich, dass ap. w nur vor r sicher zu np. b wird.' Hübschmann rejects Horn's Sanskrit comparison for āb 'Glanz' — which removes the only reason to keep it apart from āb 'water', and so indirectly supports Nourai's edge while contradicting the separate-lexeme framing.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Fārsi s.v. آفتاب and s.v. آب‌رو / آب‌رخ (MON_part1.txt lines 3757ff., 1383ff., 1414ff.)\",\n              \"stance\": \"partial\",\n              \"note\": \"آفتاب: '[آفتاب ← آب + تاب: جرم روشن گرمابخش] خورشید، شمس، مهر' — Mo'in analyses āftāb as āb + tāb 'the bright, heat-giving body', i.e. he supports Nourai on āftāb (and is, like Nourai, following Horn). But آب‌رو: 'عرق، خوی، آب رخ. اعتبار، قدر، جاه، شرف، عرض، ناموس' and آب‌رخ: 'آب‌رو، آب‌روی، خوی، عرق؛ آبرو، اعتبار، جاه' — the literal sense Mo'in gives is 'sweat of the face', not 'facial shine'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etymological Dictionary of the Iranian Verb, p. 379 s.v. *tap 'to warm up, heat'\",\n              \"stance\": \"contradicts\",\n              \"note\": \"CHEUNG.txt: under *tap, 'PARTHIAN: tʾb- \\\"to shine, burn\\\" || (+ *abi-) ʾbdʾb \\\"sunshine\\\" || (+ *pati-) ptʾb- … || (+ *ui-) wytʾb-'; 'MIDDLE PERSIAN: MMP tʾb- \\\"to shine\\\", BMP tʾp- /tāb-/ \\\"to heat, burn (up); shine\\\"'. The word for 'sunshine' is built with the preverb *abi-, not with āb 'water/glitter'; this is the entry Wiktionary cites for āftāb < Proto-Iranian *abi-tāpah.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ vol. 1, āb- compounds (BQT_v1_pages.txt lines ~6255-6320)\",\n              \"stance\": \"supports\",\n              \"note\": \"The Borhān repeatedly glosses āb metaphorically as lustre/standing: 'آب شدن … و کنایه از شرمنده شدن و رفتن آبرو و برطرف شدن رونق و رواج هم هست'; 'و بکسر ثاء، کنایه از رونق و رواج و آبرو باشد'. It documents the 'lustre / repute' sense of āb («آب ۲») that node #2 asserts, without positing a separate root.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Nushin, Vāžanāmak (Farhang-e Šāhnāme) s.v. آب (FSF.txt lines 350-392)\",\n              \"stance\": \"supports\",\n              \"note\": \"The entry āb has sense 1 'آبرو، عزت و احترام' ('اگر آب دارد تو را میزبان …' = 'if your host keeps your honour'), sense 2 'اشک', then a lustre sense illustrated by exactly the verse Nourai prints in the chart — 'چو آمد به برج حمل آفتاب / جهان گشت با فر و آیین و آب' (Šāhnāme I, 28, 7) — then sense 4 'شادابی، طراوت' and sense 5 'عرق تن، خوی'. This is the same verse Horn cites as 'Šāhn. I S. 14 Vers 7', so the chart's quotation is genuine and correctly attributed to Ferdowsī.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"A Concise Pahlavi Dictionary, ā- section\",\n              \"stance\": \"silent\",\n              \"note\": \"MacKenzie has āb 'water' (p.4) but no *āb 'lustre' and no āftāb; grep of PHD_mackenzie.txt for āftāb/abtāb returns nothing. The Middle Persian evidence for the compound therefore has to come from Manichaean/Parthian material (Cheung, DMMPP), which gives ʾptʾb/ʾbdʾb with the preverb.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, entry آب, pdf p. 50\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur's آب entry gives only the 'water' cognate set (Av. āp-, OP āpi-, Pahl. ab/ap, Skt. āpaḥ, Lat. amnis …) with Pokorny 51-52; he has no آب 'glitter' entry and does not list آفتاب or آبرو under it.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"âb-bahâ; abboha\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Arabic word itself is real: أُبَّهَة ubbaha 'pomp, splendour, grandeur, majesty' (Nourai's 'abboha'), a fuʿʿala-pattern noun. What is disputed is where it comes from. Nourai's second form 'âb-bahâ' is not an Arabic word at all but Addi Shir's proposed Persian etymon آب بها, i.e. āb 'lustre' + bahā 'splendour, worth' — so the node's language label 'Arabic' fits only the second word. Addi Shir (1908) claimed Arabic al-ubbaha was 'muʿarrab' (Arabicised) from that Persian phrase, and Nourai builds his chart on him. Modern Arabic lexicography assigns أُبَّهَة to the native triliteral root ء ب ه (ʔ-b-h), the root of the verb أَبِهَ 'to pay heed, take notice (of), be mindful', with the abstract 'self-regard, consequence' > 'grandeur' — no borrowing involved. Decisively, Asya Asbaghi's Persische Lehnwörter im Arabischen (1988), the standard modern inventory of Persian loans in Arabic, does not list it: her ʾab- entries run ābaq, ablaq, āblūǧ, ʾabūz, abū-zarǧmihr, ʾabhar, ʾabharī, ʾabīraǧ, with no ubbaha. Neither al-Jawālīqī's al-Muʿarrab nor al-ʿUnaysī's Tafsīr al-alfāẓ al-dakhīla contains it either. Phonologically the Persian source is also awkward: a two-word phrase āb bahā would not be expected to yield the geminated fuʿʿala shape ubbaha. The edge #2→#3 should be regarded as an Addi Shir folk-etymology.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87%D8%A9\",\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AFM:7\",\n              \"status\": \"supports\",\n              \"note\": \"Addi Shir does say it, on the second page of the hamza chapter. AFM_pages.txt line 182 (form-feed leaf 8; leaf 7 is the chapter opening باب الهمزة, so leaf 8 ≈ printed p.6-7, matching Nourai's citation): '( الأبهة ) العظمة والبهجة معرب آب بها' — 'al-ubbaha: greatness and splendour, Arabicised from āb bahā'. (The OCR of this line reads '+ لي العظمة والبهجة معرب أب بآ'; the surrounding entries are ابزيم/ابزن, أباش/البوش, ابر 'cloud' < Pers. abr.) The same chapter opens with '( الأباب ) الماء … معرب آب وهو الماء'. So the chart faithfully reports its source; the source is what is unreliable.\"\n            },\n            {\n              \"ref\": \"FVF:11\",\n              \"status\": \"not_checked\",\n              \"note\": \"FVF = S. M. A. Emām Shūshtarī, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi (Anjoman-e Āsār-e Melli 58, Tehran 1347/1968). refs_online.json marks it kind 'website' with no local text — readable only through the noorlib page-viewer (noorlib.ir/book/view/105056) or a login-walled ketabnak PDF; there is no fetchable page. Not checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical list, ʾab- entries\",\n              \"stance\": \"silent\",\n              \"note\": \"PLA_asbaghi_1988_ia_djvu.txt lines 1370-1400 run continuously 'ābšam … ābaq … ablaq … āblūǧ … ʾabūz … abū-zarǧmihr … ʾabhar: ein Ortsname in Qazwin und in Isfahan … ʾabharī: Nisba v. abhar … ʾabīraǧ'. أبهة is absent from the standard modern catalogue of Persian loanwords in Arabic — strong negative evidence against Addi Shir's claim.\"\n            },\n            {\n              \"src\": \"ARB\",\n              \"where\": \"al-Jawālīqī, al-Muʿarrab min al-kalām al-aʿjamī\",\n              \"stance\": \"silent\",\n              \"note\": \"grep of ARB_mo3rb.txt for أبهة / ابهة / الأبهة returns no entry (the file's Arabic indexes fine — 160 hits for الفارسية). The classical Arabic authority on Arabicised words does not treat ubbaha as foreign.\"\n            },\n            {\n              \"src\": \"TAD\",\n              \"where\": \"al-ʿUnaysī, Tafsīr al-alfāẓ al-dakhīla fī al-lugha al-ʿarabiyya\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for أبهة / ابهة in TAD_pages.txt (Arabic grep verified working on the same file).\"\n            },\n            {\n              \"src\": \"AFA\",\n              \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\",\n              \"stance\": \"silent\",\n              \"note\": \"No 'ubbaha' in AFA.txt; Fraenkel does not claim it as an Aramaic or Iranian import either.\"\n            },\n            {\n              \"src\": \"FVQ\",\n              \"where\": \"Jeffery, The Foreign Vocabulary of the Qurʾān\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry (the word is not Qurʾānic; grep of FVQ.txt returns nothing). Consulted because Nourai's parallel citation 'FVF' is easily confused with FVQ, and because the matrix lists FVQ for Arabic nodes.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, Comprehensive Etymological Dictionary\",\n              \"stance\": \"silent\",\n              \"note\": \"Klein has no English reflex of ubbaha and no entry bearing on it; his only relevant material is the *ap-/*ab- 'water' article s.v. amnic.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"obbohat «أبهت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian ابهت obbahat (more usually transcribed ubbahat/obbahat) 'grandeur, majesty, imposing presence' is a straightforward loan from Arabic أُبَّهَة ubbaha, taken over with the tāʾ marbūṭa realised as a full -t, which is the normal Persian treatment of Arabic feminines in -a when they are borrowed in the construct-like 'pausal-t' shape (cf. NP قدرت qodrat, رحمت raḥmat, نعمت neʿmat). The gemination of the -bb- is kept. So the edge #3→#4, Arabic → Persian, is real and is a genuine re-borrowing of an Arabic word into Persian. What is NOT established is that this is a round trip: it is only a round trip if node #3 is right that the Arabic word was itself Persian آب بها, and modern Arabic and loanword scholarship denies that (see node 3). Two small points on the chart's data: the script «أبهت» is given in Arabic orthography with hamza, whereas Persian normally writes ابهت; and Nourai's gloss 'elegance' is weak — Moʿin has 'بزرگی، بزرگواری، شکوه، عظمت' and Wiktionary 'magnificence, grandeur, imposing presence', i.e. 'grandeur/majesty' rather than 'elegance'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D9%87%D8%AA\",\n            \"https://en.wiktionary.org/wiki/%D8%A3%D8%A8%D9%87%D8%A9\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:131\",\n              \"status\": \"supports\",\n              \"note\": \"Moʿin has the entry and tags it Arabic. MON_part1.txt line 6560 (OCR 'ابسهت' for ابهت): 'ابهت: [ع.] (اِمص.) بزرگی، بزرگواری، شکوه، عظمت، بهجت، شادمانی، نخوت.' — '[Arabic] (abstract noun) greatness, nobility, splendour, magnificence, joy, haughtiness'. The neighbouring headwords are ابهام / ابهام پا (before) and ابهر (after), which is the right alphabetical slot for an early page of vol. I, consistent with p.131. Exact page verification is impossible: the OCR of Moʿin carries no page markers, and refs_online.json records that the online Moʿin text (vajehyab/abadis) cannot be mapped to print pages. Note that Moʿin marks the word simply '[ع.]' = Arabic; he does NOT say the Arabic came from Persian, so he supports the Arabic→Persian edge only, not the round trip.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhān-e Qāṭeʿ (Moʿin's ed.), vol. 1\",\n              \"stance\": \"silent\",\n              \"note\": \"No ابهت entry in BQT_v1_pages.txt; the Borhān is a dictionary of Persian words and normally omits transparent Arabic loans, so its silence is expected and carries no weight either way.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Fārsi, cross-check of the origin tag\",\n              \"stance\": \"supports\",\n              \"note\": \"Same entry as in ref_check: the bracketed tag is '[ع.]', Moʿin's marker for an Arabic loan, exactly matching the Arabic → Persian arrow of the chart.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry — Aryanpur covers only Indo-European inheritances of Persian, and an Arabic loan falls outside his scope; consulted as the independent modern cross-check the matrix prescribes for New Persian nodes.\"\n            },\n            {\n              \"src\": \"PLA\",\n              \"where\": \"Asbaghi 1988\",\n              \"stance\": \"silent\",\n              \"note\": \"Consulted because the node asserts a Persian → Arabic → Persian round trip; Asbaghi lists no ubbaha among Persian loans in Arabic, so the return leg has no attested outbound leg.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-32.json > /dev/null && echo \"VALID JSON\""
}
```


### [2026-09-04T18:18:33.133Z] TOOL RESULT

```
VALID JSON
```


## [2026-09-04T18:18:38.128Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus && python3 - <<'EOF'\nimport io\np='page-32.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace(\"Pokorny's own двух-entry treatment\",\"Pokorny's own two-entry treatment\")\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\ngrep -c \"двух\" page-32.json; python3 -m json.tool page-32.json >/dev/null && echo OK\nVERIFY_DIR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus python3 /home/sfmqrb/git/rishe/tools/verify_check.py 32"
}
```


### [2026-09-04T18:18:40.880Z] TOOL RESULT

```
0
OK
nodes verified: 4/4
node verdicts: {'confirmed': 2, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'not_found': 1, 'supports': 3, 'not_checked': 2}
books consulted: {'supports': 12, 'partial': 2, 'contradicts': 1, 'silent': 11} | by book: {'ARY': 3, 'PHD': 2, 'MON': 2, 'BQT': 2, 'PLA': 2, 'BRT': 1, 'KNT': 1, 'NYB': 1, 'POK': 1, 'AHD': 1, 'SYN': 1, 'WLD': 1, 'HUB': 1, 'CHEUNG': 1, 'FSF': 1, 'ARB': 1, 'TAD': 1, 'AFA': 1, 'FVQ': 1, 'KLN': 1}
```


## [2026-09-04T18:19:03.050Z] AGENT

Done. Output: `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/modelcmp/opus/page-32.json` (valid JSON; verify_check reports 4/4 nodes).

**PDF page 32 (book p.2) — 1 entry, root + 4 nodes**

- Root verdicts: confirmed 1
- Node verdicts: confirmed 2, disputed 2
- Nourai's ref checks: supports 3, not_found 1, not_checked 2 (+ root POK:1 = partial)
- Books consulted: 20 distinct (supports 12, partial 2, contradicts 1, silent 11)
- Web sources archived via fetch_source.py: 8 Wiktionary pages

Disputed items:
- **Root Ab1/Ap1 → node #2, âftâb «آفتاب»** — âftâb does not contain âb. It continues MP ʾptʾb /āftāb/ 'sunshine' (Parthian ʾbdʾb) from Proto-Iranian *abi-tāpah = preverb *abi- + *tap- 'shine, heat' (Cheung 2007 p.379, s.v. *tap, which lists Parthian "(+ *abi-) ʾbdʾb 'sunshine'"). Nourai follows Horn 1893 no.3 (and Mo'in repeats it: "آفتاب [آب + تاب]"), but *abi-t- > -ft- makes the first syllable a prefix.
- **Node #3, Arabic abboha / âb-bahâ** — Addi Shir (AFM p.7, verbatim: "( الأبهة ) العظمة والبهجة معرب آب بها") is Nourai's only real support. Modern lexicography puts أُبَّهَة under the native Arabic root ء ب ه (verb أَبِهَ 'to heed'); Asbaghi's *Persische Lehnwörter im Arabischen* (1988) does not list it, nor do al-Jawāliqī's al-Muʿarrab, al-ʿUnaysī, or Fraenkel. Also note "âb-bahâ" is Persian, not Arabic — the node's language label fits only "abboha".

Other findings worth flagging:
- **KLN:2 not_found** — Klein p.2 is "abase–abbess"; the *ab-/*ap- 'water' material is s.v. *amnic* (≈p.67) and *doab*, and does support node #1. The page number looks wrong.
- **POK:1 partial** — IEW p.1 has only the Celtic/Italic *ab-*; all of Nourai's Iranian material is at IEW 51–52 (which AHD, Buck and Aryanpur all cite instead).
- **Node #2 âberŭ** — compound âb + rū(y) is right, but Mo'in glosses آب‌رو/آب‌رخ first as 'عرق، خوی' (sweat of the face), not Nourai's "facial shine"; kept as part of the disputed node.
- **Node #4** confirmed as an Arabic→Persian loan (Mo'in tags ابهت "[ع.]"), but the round-trip framing depends on the disputed node #3; gloss "elegance" should be 'grandeur/majesty'.
- The Ferdowsi quote on node #2 is genuine and correctly attributed (found verbatim in Nushin's *Vāžanāmak* s.v. آب; = Horn's "Šāhn. I S.14 V.7").
