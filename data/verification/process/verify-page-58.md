# Verification process log — verify-page-58


## [2026-09-04T22:40:39.515Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 58 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-58.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-58.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-58.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 58` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T22:40:41.229Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-04T22:40:43.367Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T22:40:43.380Z] TOOL RESULT

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


## [2026-09-04T22:40:43.729Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-58.txt"
}
```


### [2026-09-04T22:40:43.746Z] TOOL RESULT

```
1	=== PDF page 58 (book page 28) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ap 2 : to take, receive, reach, attain  (refs POK:50)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:50; SNS:14; FFD:82 | ap 1, af, ab : to receive ; apayeiti : received ; abi-âp, abi-âf : to detain
5	  #2 (parent #1) [Pahlavi] refs=BQT:2254; SNS:14 | apâm, avâm : loan, something received. | NOTE: HRN:31 does not agree with this derivation
6	    #3 (parent #2) [Persian] refs=SNS:14; BQT:2254; AEF:173 | vâm «وام» : loan ; avâm «اوام» : loan | extra: فام ۲، آوام
7	  #4 (parent #1) [Pahlavi] refs=FFD:82 | ayâf, ayâb : to find
8	    #5 (parent #4) [Persian] refs=BQT:2419; FFD:82 | yâftan «یافتن» : to find ; yâbîdan «یابیدن» : to find | extra: یافت، یاب
9	#6 (parent #0) [Latin] refs=POK:50; AHD; KLN:22,24,96 | apere : to bind, attach, reach ; aptus : fit, suited ; ad-apt-are : to fit, adapt ; ad-eptus : reached ; apex : something, reached, apex ; co-apere : bond together, couple
10	  #7 (parent #6) [English] refs=AHD; KLN:96 | apt, aptitude ; adapt, adept, inept ; apex, attitude ; couple
11	--- entry 1 ---
12	ROOT Apâ -> redirect to Apo
13	--- entry 2 ---
14	ROOT [Avestan] Apânk : turned backwards, north  (refs SYN:873)
15	#1 (parent #0) [Pahlavi] refs=SYN:870; BQT:99; FSF:58 | apâxtar : north, north star ; axtar : star
16	  #2 (parent #1) [Persian] refs=BQT:99; FSF:58 | bâxtar «باختر» : north ; axtar «اختر» : star, fate | extra: اخترشناس | NOTE: IEC:260 links "axtar" to "setareh: star". See root "Ster 2"
17	  #3 (parent #1) [Pahlavi] refs=MON5:275; BQT:297 | bâxtri, bâxr, balx : a city north of the ancient Iran
18	    #4 (parent #3) [Persian] refs=MON5:247 | balx «بلخ» : an ancient city in Iran famous for its rose-red ruby gems | extra: بلخش، بدخشان
19	      #5 (parent #4) [Arabic] refs=AHD:101 | balaxš : ruby
20	        #6 (parent #5) [Old French] refs=AHD:101 | balais : ruby
21	          #7 (parent #6) [English] refs=AHD:101 | balas : a rose-red gem
22	#8 (parent #0) [Sogdian] refs=SOD:39 | anxar, `ngr : star | NOTE: This may be a cognate rather than a derivative of the Avestan "apânk"
23	
```


## [2026-09-04T22:40:47.551Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-58.json",
 "description": "Read source JSON page 58"
}
```


### [2026-09-04T22:40:47.590Z] TOOL RESULT

```
{
  "pdf_page": 58,
  "book_page": 28,
  "entries": [
    {
      "root": {
        "name": "Ap 2",
        "lang": "Indo-European",
        "refs": "POK:50",
        "gloss": "to take, receive, reach, attain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:50; SNS:14; FFD:82",
          "words": [
            {"translit": "ap 1, af, ab", "gloss": "to receive", "script": null},
            {"translit": "apayeiti", "gloss": "received", "script": null},
            {"translit": "abi-âp, abi-âf", "gloss": "to detain", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:2254; SNS:14",
          "words": [
            {"translit": "apâm, avâm", "gloss": "loan, something received.", "script": null}
          ],
          "note": "HRN:31 does not agree with this derivation",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:14; BQT:2254; AEF:173",
          "words": [
            {"translit": "vâm", "gloss": "loan", "script": "وام"},
            {"translit": "avâm", "gloss": "loan", "script": "اوام"}
          ],
          "script_extra": "فام ۲، آوام",
          "note": null,
          "quote": {
            "text": "درم خواست فام از پی شهریار - برو انجمن شد بسی مایه دار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:82",
          "words": [
            {"translit": "ayâf, ayâb", "gloss": "to find", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:2419; FFD:82",
          "words": [
            {"translit": "yâftan", "gloss": "to find", "script": "یافتن"},
            {"translit": "yâbîdan", "gloss": "to find", "script": "یابیدن"}
          ],
          "script_extra": "یافت، یاب",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:50; AHD; KLN:22,24,96",
          "words": [
            {"translit": "apere", "gloss": "to bind, attach, reach", "script": null},
            {"translit": "aptus", "gloss": "fit, suited", "script": null},
            {"translit": "ad-apt-are", "gloss": "to fit, adapt", "script": null},
            {"translit": "ad-eptus", "gloss": "reached", "script": null},
            {"translit": "apex", "gloss": "something, reached, apex", "script": null},
            {"translit": "co-apere", "gloss": "bond together, couple", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD; KLN:96",
          "words": [
            {"translit": "apt, aptitude", "gloss": null, "script": null},
            {"translit": "adapt, adept, inept", "gloss": null, "script": null},
            {"translit": "apex, attitude", "gloss": null, "script": null},
            {"translit": "couple", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Apâ",
        "redirect": "Apo"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Apânk",
        "lang": "Avestan",
        "refs": "SYN:873",
        "gloss": "turned backwards, north"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "SYN:870; BQT:99; FSF:58",
          "words": [
            {"translit": "apâxtar", "gloss": "north, north star", "script": null},
            {"translit": "axtar", "gloss": "star", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:99; FSF:58",
          "words": [
            {"translit": "bâxtar", "gloss": "north", "script": "باختر"},
            {"translit": "axtar", "gloss": "star, fate", "script": "اختر"}
          ],
          "script_extra": "اخترشناس",
          "note": "IEC:260 links \"axtar\" to \"setareh: star\". See root \"Ster 2\"",
          "quote": {
            "text": "نبینم همی اختر خویش بد - ندانم چرا برسرم بد رسد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON5:275; BQT:297",
          "words": [
            {"translit": "bâxtri, bâxr, balx", "gloss": "a city north of the ancient Iran", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON5:247",
          "words": [
            {"translit": "balx", "gloss": "an ancient city in Iran famous for its rose-red ruby gems", "script": "بلخ"}
          ],
          "script_extra": "بلخش، بدخشان",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Arabic",
          "refs": "AHD:101",
          "words": [
            {"translit": "balaxš", "gloss": "ruby", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Old French",
          "refs": "AHD:101",
          "words": [
            {"translit": "balais", "gloss": "ruby", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:101",
          "words": [
            {"translit": "balas", "gloss": "a rose-red gem", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:39",
          "words": [
            {"translit": "anxar, `ngr", "gloss": "star", "script": null}
          ],
          "note": "This may be a cognate rather than a derivative of the Avestan \"apânk\"",
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-04T22:40:48.551Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T22:40:48.588Z] TOOL RESULT

```
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


## [2026-09-04T22:40:56.616Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nfor k in ['POK','SNS','FFD','BQT','AEF','HRN','AHD','KLN','SYN','FSF','MON','SOD','IEC','HUB','BRT','PHD','NYB','CHEUNG','WLD','LKT','DEV','PHN','AFM','PLA']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-04T22:40:58.539Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

CHEUNG null

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
```


## [2026-09-04T22:41:03.570Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo ---- && sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-04T22:41:03.626Z] TOOL RESULT

```
page-101.json
page-126.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
page-42.json
page-43.json
page-44.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
page-50.json
page-51.json
page-52.json
page-53.json
page-54.json
page-55.json
process
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
```


## [2026-09-04T22:41:04.713Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==58 || NR==59' POK_01.txt | head -120",
 "description": "Print Pokorny page 50 area"
}
```


### [2026-09-04T22:41:06.916Z] TOOL RESULT

```
  ,begegne'.
Lat.  ante  (aus  *a?i^i,  vgl.  antistö,  sowie  anflcus,  antiquus)  Präp.  m.  Akk. riUmilich  ,gegenüber,  vor',  zeitlich  ,vor',  auch  Präverb  (z.  B.  antecedo), antid-eä, -liäc  ,YOvhQv' ,  antid-lre  ,vorangehen'  {-d  nach_prö<^);  dazu  anterior früherer',  antärium  bellum  , Krieg  vor  der  Stadt',  antlcas  ,der  vordere' (c  nach  posticus  ,hinter'),  antiquus  ,alt'  (der  Ausgang  und  die  Verengerung auf  die  zeitliche  Bed.  nach  novus]  idg.  *anti -\- *olm-  ,aussehend'),  antes, -mm  ,Reihen  (von  Soldaten,  Weinstöcken  u.  dgl.)',  ursprünglich  etwa ,Fronten'  (über  antae  s.  aber  unter  "^andtä  ,Türpfosten').
Hitt.  ha-an-ti  (hanti)  ,vorne,  besonders'.
anta  ,gegenüber  hin'  (Richtung);  zum  -a  s.  Sclnvyzer  Gr.  Gr.  I  622 f.
Got.  and  Präp.  m.  Akk.  ,auf— hin,  über— hin,  entlang'.  Mit  davon  ab- weichender Bed.  das  Nominal-  und  Verbalpräfix  germ.  anda-,  and-  ,ent- gegen,  gegenüber'  und  —  indem  ein  Dagegenhandeln  in  ein  Trennen  aus- läuft —  in  Verben  perfektivierend  gewöhnlich  ,von— weg' :  got.  anda-,  and- (z.  B.  andniman  ,eutgegennehmen',  andanüms  ,annehmlich,  angenehm', andbindan  ,losbinden,  entbinden'),  anord.  as.  ags.  and-,  ahd.  ant-,  int-, mhd.  nhd.  ant-,  ent-  (z.  B.  Antlitz,  Antwort,  entbinden).
Komp.  anord.  endr,  enn  ,früher,  vormals,  wieder,  nach'  (endr  =  got. andiz-uh  ,entweder'),  ags.  end  ,vorher'  (^andis),  ahd.  enti  ,früher,  voi-mals' (germ.  "^andiaz),  mhd.  e^it,  end  Konj.  ,ehe,  vor'  (z.  B.  Falk-Torp  192,  1455).
Lit.  ant,  älter  anta  m.  Gen.  ,nach— hin,  auf.
über  gr.  ävTcc  s.  oben.
nti
Eine  schwächere  Ablautform  ("^nt-)  zeigt  got.  und  m.  Dat.  ,dyTi,  für, um',  unpa-  (*nto-)  in  unpa-piiuJian  ,entfliehen',  ags.  od-  (*unp-)  in  oägangan ,entgehen',  üdgenge  ,fliüchtig'  =  anord.  unningi,  undingi  (*unp-,  *und- gangia-)  ,entwichener  Sklave'  (Brugmann  Grdr.  II-  2,  803),
4
50
Andere  Bed.  zeigt  got.  und  m.  Akk.  ^bis*^,  ahd.  unt  in  unt-az  jhW  undj unzi  (=  untzi)  ,\i\s',  as.  und  ,Vis^,  unti,  unt  {und  -J-  te  ,zvi^),  unto  {und  -f-  tö)^ engl,  unto  ,7m,  bis^,  anord.  unz  {und  es)  ,bis  daß^^  ags.  (mit  grammatischeruj Wechsel)  o^  ^hin  zu^  bis^^^,  osk.  ant  m.  Akk.  ^bis  zu^  (ebenfalls  aus  *nid s.  Walde  Kelten  und  Italiker  54;  wegen  der  zu  germ.  und  genau  stimmenden] Bed.  nicht  =  lat.  ante  zu  setzen,  z.  B.  v.  Planta  II  443),  lit.  int  ,nacVl (eher  Kontamination  von  in  und  ant).  Daß  diese  Formen  eine  Erweiterung] der  Präp.  *en,  *n  ,in^  darstellen  (Schwyzer  Gr.  Gr.  I  629  f.,  wo  auch] über  gr.  dial.  svts)^  ist  möglich,  wie  denn  lit.  int  mit  f  ,nach^  in  der  An- wendung sich  deckt.  Doch  könnte  dies  eine  nachträgliche  Gebrauchsan- gleichu
ng infolge  der  Lautähnlichkeit  sein  und  idg.  *nt{-i^  -a?)  ,bis^  als ^gegenüber  hin,  auf  die  entgegengesetzte  Seite  hinüber^  zu  anti  gehören;  auch die  Worte  für  ,Ende^  (s.  u.)  sind  ursprüngl.  das  auf  der  gegenüberliegen- den Seite  winkende  Ziel,  und  mit  as.  unt  ist  auch  ant  {and  -\-  te)  Präp.  m. Akk.  ,usque  ad^  bedeutungsgleich,  was,  selbst  wenn  nur  junge  Kreuzung  von unt  mit  and-  vorläge,   doch   die  Begriffsverwandtschaft   beider  beleuchtet.
antios  , gegenüber,  vor  einem  liegend'^  (vom  Adverb  anti  gebildet): *antiö-  (gerra.  *andja-)  in  got.  andeis^  anord.  endir,  as.  endi,  ags.  ende m.,   ahd.    anti,   entl   m.    und   n.,   nhd.   Ende]   auch   gr.  ävTtog  ,gegenüber^ {d3iZ\i ivavzlov  ds.,  ivavvlog  ,gegenüber  befindlich;  Gegner^)  geht  wahrschein- lich (vgl.  Schwyzer  Gr.  Gr.  I  379)  auf  *ävTiög  zurück.
Dagegen  ist  von  *anto-  (s.  oben)  abgeleitet  dntio-  in  anord.  enni  n., ahd.  andi,  endi  n.  ,Stirn^  =  lat.  antiae  ,capilli  demissi  in  frontem^»
Ein  ganz  verschiedenes  Wort  ist  nhd.  und^  ahd.  unii^  anti,  enti  u.  dgl., as.  endi,  ags.  engl,  and  ,und^,  anord.  en{n)  ,und,  aber^,  das  mit  ai.  dtlm ,darauf,  dann,  desgleichen^,  av.  a&n  ,ebenso^,  osk.  ant  m.  Akk.  ,usque  ad^, lit.  int  m.  Akk.  ,nach'^  (aber  s.  oben),  toch.  B  entwe  ,also^  zu  *en,  iq.  ,in^ gehört.
WP.  I.  65  ff.,  WH.  I  53  f.,  Feist  46,  Schwyzer  Gr.  Gr.  I  619,  621, 629  f.,  632  f.,  722,  726,  II  (B  V  2  b  d  3).
antro-m  ,Höhle,  Luftlochs
Arm.   ayr,  Gen.  PL   ayric  ,Höhle^,  gr.  ävzgov  ds. Vielleicht  zu  an{9)-  ,atmen^,  als  ursprüngl.  ,Luftloch^ WP.  I  561,  Schwyzer  Mel.  Boisacq  II  234 1,   KZ.  68,  222,    Gr.  Gr.  I 532,  Pisani  KZ.  68,  161  f.
I.  ap-  (richtiger  dp-)  :  ep-  ,fassen,  nehmen,  erreichend
Ai.  äpnötierreicht,  erlangt',  jünger  äptd-h  ,geschickt,  geeignet,  vertraut'; av.  apayeiti  ,erreicht',  3.  PL  äpdnte  aus  *äpuantai;
51
arm.  itnim  ^besitze^  (*öp-n-?)^  dnd-unim  ^erlange"^;
o-r.  ärtto)  ^anfassen^  anheften^,  anbinden^  anzünden^^  tlmEa^ca  ;berühren% cicpn  Berührung^  Haften  usw/  wird  trotz  dem  Spiritus  hierherzustellen sein.  Kretschmer  Gl.  1,  352  nimmt  Beeinflussung  durch  ertoj  an;  hom. dwcict)  (äq)dü))  ^berühre^  betaste^^  ion.  acpäaoo)  ds.^  hom.  dcrtaq)ia'/.(x),  }jrca(pov (mit  äol.  o:  ärtocpeiv'  ärcazfiaai  Hes.)  ^betrügen;,  täuschen^^  dTrocpcbXiog trüo-erisch^;,  '/.airjcprjg  ^niedergeschlagen^  (eigentl.  ^untergekriegt^).  Pedersen KZ.  39^  428  stellt  mit  gr.  Utito)  arm.  a//  ^die  hohle  Hand^  (o-St.^  doch Lok.  y-(^p'^  3-^3  -i-St.,  also  wohl  ätler  neutr.  -o-i-St.)  zusammen,  welches Wort  dem  gr.  äxpog  ;,Gelenk^  entsprechen  soll;  wegen  des  p*  (=  idg.  pA) jedoch  unsicher  (vgl.  Meillet  BSL.  36^  HO);
lat.  apiscor  ^fasse,  erreiche^^  adipzscor  ^erlange^;,  coe.'pi  ,habe  angefangen^; später  coepl.  Der
```


## [2026-09-04T22:41:16.796Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==60' POK_01.txt | head -60",
 "description": "Print Pokorny leaf 60"
}
```


### [2026-09-04T22:41:18.881Z] TOOL RESULT

```
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
```


## [2026-09-04T22:41:28.317Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -m5 \"To take, reach\" AHD_watkins1985.txt; echo \"=== ap-1 context\"; grep -n -i -A12 \"^ *ap-1\" AHD_watkins1985.txt | head -60",
 "description": "Grep AHD for ap-1"
}
```


### [2026-09-04T22:41:28.378Z] TOOL RESULT

```
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
=== ap-1 context
```


## [2026-09-04T22:41:29.609Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"apex\\b\" AHD_watkins1985.txt | head -20; echo ===; grep -n -i \"attitude\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for apex/attitude"
}
```


### [2026-09-04T22:41:29.657Z] TOOL RESULT

```
Exit code 1
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
1252:AORTA wer-2 APERIENT wer-5 APERITIF wer-5 APERTURE wer-5 APEX ap-! APHELION sawel- APHONIA bha-2 APLANATIC pele-2 APLOMB plumbum APNEA pneu-
(eval):1: == not found
```


## [2026-09-04T22:41:39.351Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online.json'))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FSF'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SOD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['SYN'],ensure_ascii=False,indent=1))\n\"",
 "description": "Print offsets for key refs"
}
```


### [2026-09-04T22:41:45.270Z] TOOL RESULT

```
{
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
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
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
{
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
```


## [2026-09-04T22:41:51.638Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in '^apt,' '^aptitude,' '^adapt,' '^adept,' '^inept,' '^apex,' '^attitude,' '^couple,' '^copula,'; do echo \"### $w\"; grep -n -m1 -A6 \"$w\" KLN_1966.txt; done",
 "description": "Grep Klein for apt family"
}
```


## [2026-09-04T22:41:52.665Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==897 || NR==898' SYN.txt | head -80",
 "description": "Buck p.873 area"
}
```


### [2026-09-04T22:41:55.376Z] TOOL RESULT

```
### ^apt,
3252:apt,  adj.,  fit.  —  L.  aptus,  ‘fitted,  suited’,  prop.  pp. of  obsol.  apere,  ‘to  fasten’,  rel.  to  aptsci,  to reach  after,  attain’,  and  cogn.  with  OI.  apnoti, ‘he  reaches,  attains’,  Hitt,  epmi,  ‘I  seize  .  Cp.
3253-adapt,  adept,  apex,  aptitude,  attitude,  inept, lariat,  reata.
3254-Derivatives:  apt-ly,  adv.,  apt-ness,  n.
3255-Aptenodytes,  n„  a  genus  of  pinguins  ( ornithol .)  — ModL.,  lit.  ‘wingless  diver’,  fr.  Gk.  ajrnjv, ‘wingless’,  and  Su-nr,?,  ‘diver’.  The  first  element is  formed  fr.  d-  (see  priv.  pref.  a-)  and  a  collat¬ eral  form  of  itttivos,  ‘flying,  winged  ,  fr.  *pta-, zero  degree  of  I.-E.  base  *pet-,  ‘to  fly’;  see ptero-.The  second  element  derives  fr.  Gk.  Soelv, ‘to  dive’ ;  see  adytum  and  cp.  words  there  referred
3256-apterous,  adj.,  without  wings  (zool.)  —  Gk.  &n- xepoq,  ‘wingless’,  fr.  &-  (see  priv.  pref.  a-)  and mrep6v,  ‘wing’.  See  ptero-,  and  cp.  next  word. For  E.  -ous,  as  equivalent  to  Gk.  -os,  see  -ous- apteryx,  n.,  the  kiwi.  —  Lit.  ‘without  wings  ,  fr. priv.  pref.  a-  and  ir-cepu^,  ‘wing’,  which  is  rel. to  Trxepov,  ‘wing’.  See  ptero-  and  cp.  prec.  word, aptitude,  n„  fitness.  -  F„  fr.  Lute  L.  aptitudd, ‘fitness’,  fr.  L.  aptus.  See  apt  and  -tude  and  cp. attitude,  which  is  a  doublet  of  aptitude. aptote,  n.,  an  indeclinable  noun.  L.  aptotum, fr  Gk.  Stttwtov,  neut.  of  dirtoiTo <;,  ‘having  no cases,  indeclinable’,  fr.  i-  (see  priv.  pref.  a-)  and imo-rd?,  ‘fallen’,  verbal  adj.  of  nftrretv,  to fall’,  which  stands  for  *nf-7rreiv,  fr.  pt-,  zero degree  of  I.-E.  base  *pet-,  ‘to  fly,  to  fall .  See
3257-feather  and  cp.  symptom  and  words  there  re¬ ferred  to.
3258-Derivative:  aptot-ic,  adj. apyretic,  adj.,  without  fever  (med.)  —  Formed with  suff.  -ic  fr.  Gk.  dbruperoi;,  ‘without  fever’, fr.  4-  (see  priv.  pref.  a-)  and  mipETo?,  ‘fever, feverish  heat',  fr.  mip,  ‘fire’.  See  pyretic  and  cp. apyrexia.
### ^aptitude,
### ^adapt,
1576:adapt,  tr.  v.  —  F.  adapter ,  fr.  L.  adaptare,  ‘to  fit, adjust,  adapt’,  fr.  ad-  and  aptare,  ‘to  fit’,  fr. aptus,  ‘fit’.  See  apt  and  cp.  adept.
1577-Derivatives:  adapt-able,  adj.,  adapt-abil-ity,  n., adaptation  (q.v.),  adapt-ed ,  adj.,  adapt-ed-ness, n.,  adapt-er,  adapt-or,  n.
1578-adaptation,  n.  —  F.,  fr.  ML.  adaptationem,  acc. of  adaptatio,  fr.  L.  adaptatus,  pp.  of  adaptdre. See  adapt  and  -ation.
1579-Derivatives:  adaptation-al,  adj.,  adaptation-al¬ ly,  adv.
1580-Adar,  n.,  name  of  the  twelfth  Jewish  month.  — Heb.  Adhir,  fr.  Akkad.  Addaru,  Adaru,  lit.  ‘the dark  or  clouded  month’,  fr.  Akkad,  adaru.  ‘to be  dark’;  see  Frd.  Delitzsch,  Prolegomena, p.  138.  According  to  Haupt  in  ZDMG.,  64,  705, Addaru  is  rel.  to  Akkad,  iddar,  ‘threshing  floor’, and  prop,  means  ‘month  of  the  threshing  floor’. Cp.  Veadar.
1581-adati,  n.,  a  kind  of  fine  cloth  exported  from  Ben¬ gal.  —  Prob.  fr.  Hind,  adha,  ‘half’,  and  lit. meaning  ‘of  half  width’.  See  Yule-Bumell, Hobson-Jobson,  p.4.
1582-add,  tr.  and  intr.  v.  —  L.  addere,  ‘to  put  to,  lay on,  give  in  addition  to,  add’,  fr.  ad-  and  -dere, fr.  dare,  ‘to  give’.  See  date,  ‘point  of  time’,  and cp.  addendum,  additament,  addition. Derivatives:  add-ed,  adj.,  adder  (q.v.),  add- ible,  adj.
### ^adept,
1616:adept,  adj.,  skilled,  proficient;  n.,  an  expert.  — L.  adeptus,  ‘reached,  attained',  pp.  of  adipisci.
1617-adequacy
1618-administer
1619-24
1620-‘to  arrive  at,  reach,  attain’,  fr.  ad-  and  apisci (pp.  aptus),  ‘to  reach,  come  up  with’,  which  is rel.  to  OL.  *apid ,  apere,  ‘to  bind,  attach’,  pp. aptus,  ‘attached  to’.  See  apt  and  cp.  adapt.  For the  change  of  Latin  d  (in  aptus )  to  e  (in  ad- eptus )  see  accent  and  cp.  words  there  referred  to. Derivative:  adept-ness,  n. adequacy,  n.  —  Formed  fr.  next  word  with stiff,  -cy.
1621-adequate,  adj.  —  L.  adaequatus ,  pp.  of  adaequare, ‘to  make  equal  to’,  fr.  ad-  and  aequare,  ‘to  make equal’,  fr.  aequus,  ‘equal’.  See  equal  and  adj. suff.  -ate.
1622-Derivatives:  adequate-ly,  adv.,  adequate-ness,  n. adermia,  n.,  absence  of  the  skin  ( med .)  —  Medical L.,  formed  fr.  priv.  pref.  a-,  Gk.  86pp.a,  ‘skin’ (see  derma),  and  suff.  -ia. adevism,  n.,  the  denial  of  gods.  —  A  hybrid  coin¬ ed  by  Max  Muller  on  analogy  of  atheism,  fr. priv.  pref.  a-,  OI.  devah,  ‘god’,  and  -ism,  a  suff. of  Greek  origin.  See  deity, adharma,  n.,  unrighteousness  (Hinduism).  —  OI. a-dharmah,  formed  fr.  priv.  pref.  a-  and  dhdrmah, ‘law,  right,  justice’.  See  an-  and  dharma. adhere,  v.  —  F.  adherer ,  fr.  L.  adhaerere,  ‘to  stick to,  cling  to’,  fr.  ad-  and  haerere,  ‘to  stick,  cling’. See  hesitate  and  cp.  adhesion.  Cp.  also  cohere, inhere.
### ^inept,
### ^apex,
### ^attitude,
### ^couple,
### ^copula,
9141:copula,  n.  —  I  .  copula,  ‘that  which  binds  to¬ gether,  band,  bond’,  which  stands  for  *co- apula,  and  is  formed  fr.  co-  and  a  dimin.  from the  stem  of  apio,  apere,  ‘to  join,  fasten’.  See
9142-apt  and  cp.  couple.
9143-copulate,  intr.  v.  —  L.  copulatus,  pp.  of  copulare, ‘to  bind  together,  copulate’,  fr.  copulare.  See copula  and  verbal  suff.  -ate.
9144-Derivatives:  copulation ,  copulative  (qq.v.),  co- pulat-ory,  adj.
9145-copulation,  n.  —  F.,  fr.  L.  copulationem,  acc. of  copulatio,  ‘a  binding  together’,  fr.  copulatus, pp.  of  copulare.  See  prec.  word  and  -ion. copulative,  adj.  —  F.  copulatif  ( fem.  copulative), fr.  L.  copulativus,  fr.  copulatus,  pp.  of  copulare. See  copulate  and  -ive.
9146-Derivatives :  copulative,  n.,  copulative-Iy,  adv. copy,  n.  —  ME.  copie, fr.  MF.  ( =  F.)  copie.  ‘abun¬ dance;  copy’,  fr.  L.  copia,  ‘plenty,  abundance’; see  copious.  For  sense  development  see  next  word, copy,  tr.  and  intr.  v.  —  F.  copier,  fr.  ML.  copiare, ‘to  transcribe’,  orig.  ‘to  write  in  plenty’  (fr.
9147-L.  copia,  ‘plenty,  abundance’),  whence  arose  the particular  meaning  ‘to  write  the  original  text many  times’.  See  prec.  word, copyist,  n.  —  A  hybrid  coined  fr.  copy  and  -ist, a  suff.  of  Greek  origin.
```


### [2026-09-04T22:41:57.606Z] TOOL RESULT

```
. less restricted than in England), fr. a Lat. type *ez- pensivus, fr. expendere ‘spend’, but asso- ciated with expense (11.72). NEDs.v.
5. Lith. brangus, etym.? (: Du. pronk ‘ostentation, show’?). Uhlenbeck 205. Franck-v. W. 524.
Lett. ddrgs, either cognate with, or borrowed from, the Slavic (below). Miihl.-Endz. 1.448.
6. ChSl. dragi, etc., general Slavic (in the modern languages also ‘dear, be- loved’), etym. dub. Berneker 213.
SCr. skup, also ‘stingy’, Bulg. skapit ‘dear, expensive, stingy’, in the other Slavic languages only ‘stingy’, Russ. skupoj, Boh. skoupy, Pol. skapy (11.54).
7. Skt. mahargha-, epd. of maha- ‘large, great’ and argha- ‘price’ (11.87).
Skt. bahumilya-, cpd. of bahu- ‘much, many’ and milya- ‘price’ (11.87).
11.89 CHEAP
Gtk, ebreAs, etwvos Goth. Lith.  pigus NG ormpbs ON udyrr Lett.  éts te Dan. _ billig GhBU teste i; hae mercato (vile) Sw. billig SCr.  jeftin & @) bon marché OE —undéor Boh. lacing Tum ‘ain ME good chepe, undere Pol. tani in nm NE cheap Russ. deSevyj Met sor Du. goedkoop, billajk Skt. —_alpakrita- ¥. aa See untiuri Av. sOstess
eo mare hoa, untiure, wolveil(e)
. “ mat NHG billig, wohlfeil
me of t cant a St fae.
ormed he words for cheap’ are | (and quite the opposite in NHG billig,
in accordance with its origin).
1. Grk. ebredjs, cpd. of ed- ‘well’ and rédos ‘tax, toll, duty’ (11.68), hence ‘easy to pay for’, opp. to woAvredns ‘dear’.
Grk. etwvos, epd. of ed- and aves ‘price’ (11.87).
NG pop. ¢ryvés, lit. eb@nvés, through ‘abundant’ fr. post-class. el@qvés ‘thriv- ing, flourishing’, beside class. Grk. ei@- via “prosperity, plenty’, evOnvéw, eibevin
. Gurukul Kangri Collection, Haridwar
EI OO
Digitized by Arya Samaj Foundation Chennai and eGangotri
828 SELECTED INDO-EUROPEAN SYNONYMS
‘thrive’, etc., prob. : Skt. ghana- ‘com- pact, firm’, Lith. gana ‘enough’, etc. (13.18).
2. Lat. vilis (>It. vile, sometimes ‘cheap’ but mostly ‘mean, vile’), etym. dub. Walde-P. 1.214, 312. Ernout- M. 1108.
It. a buon mercato, Fr. (a) bon marché, lit. ‘at good trade’, with mercato, marché ‘trade (= sale, purchase), market’ (11.85).
Sp. barato, fr. baratar ‘buy a thing at less than its value’ : It. barattare ‘ex- change’, OFr. barate ‘strife, trade, de- ceit’, etc., a widespread group, including NE barrat (obs.) and barter, but of uncertain orig. REW 9438 a (giving as source ON baraita ‘strife’ but this rather fr. OFr.). Gamillscheg 78. NED s.v. barrat. Diez 41.
Rum. ieftin, fr. Byz., NG ev6nvds (é¢rnvés), above, 1. Tiktin 592.
3. Ir. word for ‘cheap’?
NIr. saor, orig. ‘free’ (19.44). The sense ‘cheap’ is prob. acquired by con- trast with daor ‘enslaved, captive’ and ‘dear, expensive’ (11.88). The sense ‘free’ lent itself readily to ‘cheap’ (cf. W. rhad).
W. rhad, orig. ‘gratuitous, free’ = sb. rhad ‘grace, gift’ (fr. adv. and predicate noun constructions as yn rhad ‘gratis’) : Ir. rath ‘grace, reward, success, result’, etym. dub. Stokes 225. Pedersen 1.144. Thurneysen, Gram. 131.
Br. mare’had-mat, lit. ‘good market’, semantic borrowing fr. Fr. bon marché.
4. ON adyrr, OF undéor, ME undere, OHG untiuri, MAG untiure, neg. cpds. of ON 
djyrr, etc., ‘dear, expensive’ (11.88).
ME good chepe, NE cheap (shortened fr. good cheap), Du. goedkoop, lit. ‘good
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
bargain, trade, or market’, with OR ceap, ME chepe, Du. koop ‘trade (= sale or purchase), market, bargain, etc.’ : Or céapian, etc., ‘trade’ (11.88). NED BY cheap sb. Cf. the It. and Fr. locutio: above, 2.
NHG billig, MLG billtk (> Dan. Sw. billig), orig. ‘fair, just’, like OHG billtch, MHG billich, fr. *bili- in OF bile- wit ‘simple, innocent’, MHG un-bil(e). de ‘injustice, monstrosity’, etc. : Ip. bil ‘good’, Grk. ¢idos ‘dear, worthy’, Development of sense ‘cheap’ fr, phrases like billiger preis, orig. ‘fair price’. Walde-P. 2.185. Falk-Torp 74. Weigand-H. 1.239. Paul, Deutsches Wtb. 82.
NHG wohlfeil, MHG wolveil(e) or two words wol veil(e), lit. ‘easy to buy’, epd. of wohl, MHG wol ‘well’ and feil, MHG veil(e) ‘te be sold, for sale’. Weigand-H. 2.1281.
5. Lith. pigus, beside pingu, pigli ‘become cheap’, etym.?
Lett. Jéts, also ‘easy, light’ : Lith. létas, lénas, Lett. léns ‘slow, lazy, gentle’, ChSl. léni% ‘lazy’, Lat. lénis ‘soft’, etc. Walde-P. 2.395. Miihl.-Endz. 2.460, 463.
6. SCr. jeftin, fr. Byz., NG «d6nvos (éprnvés), above, 1. Berneker 455.
Boh. lacing, in earlier use ‘easy’ : Pol. tatwy, tacny ‘easy’ (9.96).
Pol. tani, etym.? Briickner 565.
Russ. degevyj, fr. adv. degevo ‘cheaply’, etym. dub., perh. (as ‘right, suitable, fitting’ > ‘moderate, cheap’, cf. NHG billig, etc., above) : SCr. u-desiti ‘set right, make right’, ChSI. desiti ‘find’, etc. Or loanword? Berneker 188.
7. Skt. alpakrita-, lit. ‘bought for little’, epd. of alpa- ‘little, small’ and krita- fr. kri- ‘buy’ (11.81).
n,
Digitized by Arya Samaj Foundation Chennai and eGangotri
LATIONS: PLACE, FORM, SIZE
ForM, SHAPE
SIzE
Grow
MEasune (vb.) LarGE, Bie (GREAT) SMALL, LITTLE Lone
TALL
SHORT
Wipe, Broap NARROW
Turck! (in Dimension) Tuicx? (in Density) Tun! (in Dimension) Tun? (in Density) DEEP
SHALLOW
Fiat
Hottow (= Concave) STRAIGHT
CROOKED
Hoox
CoRNER
Cross
SquanRkE (sb.) Rowunp (adj.) CircLE
SPHERE
Linz (sb.)
Hoe
EquaL
Like, SmmmLar CHANGE (vb.)
Sien (sb.)
CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
CC-0. In Public Domain. Gurukul Kangri C
```


## [2026-09-04T22:42:06.969Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\nfor target in [3252,1576,1616,9141]:\n    # count formfeeds before that line\n    pre='\\n'.join(lines[:target])\n    print(target, 'leaf', pre.count('\\f'))\nEOF",
 "description": "Compute Klein leaf numbers"
}
```


## [2026-09-04T22:42:08.129Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"12\\.4[5-8]\" SYN.txt | head -20; echo \"=== NORTH\"; grep -n \"NORTH$\\|12.47\" SYN.txt | head",
 "description": "Find Buck NORTH section"
}
```


### [2026-09-04T22:42:09.329Z] TOOL RESULT

```
3252 leaf 62
1576 leaf 23
1616 leaf 24
9141 leaf 195
```


### [2026-09-04T22:42:17.112Z] TOOL RESULT

```
9311:loanword fr, ON . m Meyer, RC 12.461, Se SAIS Ue
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
22241:870 12.45 HAST 12.46 WEST Grk. — dvarody, éws éoxépa, dvopal, dbots NG évarody Shots Lat. _oriéns occidéns, occdsus It. est, levante ovest, ponente Fr. est ouest Sp. este oeste, poniente Rum. est, rdsdrit vest, apus Ir. airther iarthar Nir. oirthear tarthar W. dwyrain gorllewin Br. reler, savheol kuzheol, kornaoueg Goth. urruns saggqs ON austr vesir Dan. gst vest Sw. Oster vdster OE éast west ME est west NE east west Du. oosten westen OHG dstan westan MHG  dsten west(en) NHG  osten westen Lith. rytai vakarat Lett. austrums, rili rielums, vakari ChSl.  vitstokiz zapadit SCr.  istok zapad Boh.  vgchod zdpad Pol. wschéd zachéd Russ. vostok zapad Skt.  purvd-(dig-), pratici-(dig-), praci-(di¢-) paccima-(di¢-) Av. upaosanhva-, daosatara- (adj.)
22248:re 12.47 NORTH 12.48 SOUTH of Bopéas, Boppas véros, peonuBpla 3Y Boptas, Boppas véros, peonuBpla sk septentrid meridiés, auster : nord sud, mezzogiorno, mezzod ef nord sud, midi 'p0 norte sur, mediodia sto nord sud ltiascert descert , tuaisceart deisceart gogledd deheu, de mt hanternoz kreistetz i mW nordr sudr ‘be nord syd din nord, norr séder norp stip | north south wo north south for noorden zuiden nord, nordan sundan up nort, norden stiden, sunden aul norden stiden 10 Siauré, Ziemiai pieltis | ztemel't dienvidus séverit jugit At sjever jug (* sever, piilnoc jih ; péinoc poludnie ea sever jug 12. ultara-(di¢-), daksind-(dic-) ate udici(dig-) § apdaztara- (adj.) paurva-, rapi0witara- iit (adjs.) ; Ch with ‘midnight’ as opposite of ‘midday’ Uy = ‘south’. lar Notable is the spread of the English for words, first as nautical terms, to the ) Romance languages. a The attested Goth. words for ‘east’ ave and ‘west’ (Mt. 8.11; those for ‘north’ | and ‘south’ are not quotable) are not ‘rs general Gme. terms, but literal transla- on tions of the Grk. Cf. G. S. Lane, Phil. Quarterly 12.323 f. fr, But it may be noted that Luther used i the Gme. terms only for the winds, otherwise those for ‘morning’, ‘evening’, M etc., and that these or others had almost . replaced the old terms fora while. Paul, a Deutsches Wtb. 379. §
22274:8. Skt. pirva-(dig-) fr. adj. purva- ‘in front, former, eastern’ = Av. paorva- in front, former’, but ‘southern’ (see 12.48). OPers. paruva- ‘eastern’ (Barth. 871) is to be deleted. The correct read- ing is paradraya ‘beyond the sea’. Cf. Cameron, J. Near East. Stud. 2.307 fs
22276:12.46. Words for ‘west’ are derived from those for the ‘setting, going down’ (of the sun), or ‘evening’ or ‘behind’ (as opposed to ‘in front’ = ‘east’, cf. 12.45).
22308:12.47. Words for ‘north’ are from the name of a north wind, a northern con- stellation, ‘midnight’, ‘winter’, ‘upper region’, and from ‘left’, or under a south- ern orientation ‘behind’.
22338:Lat. auster ‘south wind’, also ‘south’, prob. orig. ‘east wind’ : ON austr, etc., feast’ (12.45), with shift through ‘south- east’ explained by the diagonal position of the axis of Italy. Walde-H. 1.87. Ernout-M. 94 (with some doubt).
22340:3. Ir. descert, NIr. deisceart, epd. of dess ‘right, southern’ (12.41), with cert as in téascert ‘north’ (12.47).
25407:1, IE *wespero- and *wekero-, parallel forms with first part prob. *wes- and tye Skt. avas, ava ‘down’ and OE west, ete, ‘west’ (12.46). Walde-P. 1.15, 311, Falk-Torp 1371 f.
=== NORTH
22248:re 12.47 NORTH 12.48 SOUTH of Bopéas, Boppas véros, peonuBpla 3Y Boptas, Boppas véros, peonuBpla sk septentrid meridiés, auster : nord sud, mezzogiorno, mezzod ef nord sud, midi 'p0 norte sur, mediodia sto nord sud ltiascert descert , tuaisceart deisceart gogledd deheu, de mt hanternoz kreistetz i mW nordr sudr ‘be nord syd din nord, norr séder norp stip | north south wo north south for noorden zuiden nord, nordan sundan up nort, norden stiden, sunden aul norden stiden 10 Siauré, Ziemiai pieltis | ztemel't dienvidus séverit jugit At sjever jug (* sever, piilnoc jih ; péinoc poludnie ea sever jug 12. ultara-(di¢-), daksind-(dic-) ate udici(dig-) § apdaztara- (adj.) paurva-, rapi0witara- iit (adjs.) ; Ch with ‘midnight’ as opposite of ‘midday’ Uy = ‘south’. lar Notable is the spread of the English for words, first as nautical terms, to the ) Romance languages. a The attested Goth. words for ‘east’ ave and ‘west’ (Mt. 8.11; those for ‘north’ | and ‘south’ are not quotable) are not ‘rs general Gme. terms, but literal transla- on tions of the Grk. Cf. G. S. Lane, Phil. Quarterly 12.323 f. fr, But it may be noted that Luther used i the Gme. terms only for the winds, otherwise those for ‘morning’, ‘evening’, M etc., and that these or others had almost . replaced the old terms fora while. Paul, a Deutsches Wtb. 379. §
22308:12.47. Words for ‘north’ are from the name of a north wind, a northern con- stellation, ‘midnight’, ‘winter’, ‘upper region’, and from ‘left’, or under a south- ern orientation ‘behind’.
22340:3. Ir. descert, NIr. deisceart, epd. of dess ‘right, southern’ (12.41), with cert as in téascert ‘north’ (12.47).
```


## [2026-09-04T22:42:33.514Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22300,22345p' SYN.txt",
 "description": "Buck 12.47 north discussion"
}
```


### [2026-09-04T22:42:33.564Z] TOOL RESULT

```
6. ChSI. zapadz, SCr., Russ. zapad, Boh. zépad, fr. za- ‘behind’, and pada, pasti ‘fall’ (with reference to the disap- pearance of the sun behind the horizon).
SELECTED INDO-EUROPEAN SYNONYMS
Pol. zachéd fr. zachodzié go down (of sun)’.
7. Skt. pratict-(dig-), fr. ‘turned toward, facing, (‘west’ from ‘behind’),
Skt.  pagcimd-(dig-), lit, ‘hinder. (most), last’, fr. pagca- ‘behind, aftey’ and ‘in the west’.
Av. daogatara-, daogastara-, adj. (-3- fr. usastara- ‘eastern’), fr. *daogq- ‘eve. ning, west’ = Skt. dosa- ‘evening, dark- ness’ (prob. : dicis, etc., above, 1), Barth. 674. Walde-P. 1.777 f.
‘Zo behing,
Ir. pratyaric- behind, western’
12.47. Words for ‘north’ are from the name of a north wind, a northern con- stellation, ‘midnight’, ‘winter’, ‘upper region’, and from ‘left’, or under a south- ern orientation ‘behind’.
1. Grk. Bopéas, Att. Boppas, NG pop. Boptas (Bopias, two syll.), orig. ‘north wind’ (personified), source uncertain, perh. a northern loanword related to Slay. burja ‘storm’. Walde-P. 1.682.
2. Lat. septentrid, orig. pl. septeniri- Ones ‘the seven plow-oxen’ (trid ‘plow- ox’), name of a constellation in the north (the great or little bear). Ernout-M. 925 f.
Fr. nord (>It. Rum. nord, Sp. norte), fr. OF norp. REW 5957.
3. Ir. tuascert, NIr. tuaisceart, cpd. of *tias : tiath ‘left’ (12.42) and cert (as in des-cert ‘south’) ‘part, region’, perh. orig. ��quarter’ : Lat. quartus, ete. Loth, RC 43.160 ff. Pedersen, Don. Nat. Schrij- nen 423 ff.
W. gogledd, cf. Ir. fochla ‘the North’ (as a section of Ireland), epd. W. 90>) Tr. fo- ‘sub-’ and last member : W. cledd, Tr. clé ‘left’ (12.42). Pedersen 1.68.
Br. hanternoz, ‘midnight’ (lit. ‘half- night’, fr. hanter ‘half’, 13.24) and ‘north’, as opposed to kreisteiz ‘noon and ‘south’.
4, ON nordr, OF norp (adv.), ete
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
ee
gpAT
‘ t faces eft? to north’ as one gpft, 8 te Walde-P. 2.333 f. Falk-
orp ie ChSI. sévert, etc., the b. iso ‘nort wind’, beside Lith. stter 5 th wind’: Lat. caurus est wind’, Goth. skura windis
selind’ OHG scur ‘storm’, etc. yi
fena, Lett. 21ea ‘winter’. g, ChSl. seve Bob. mulnoc, snd ‘north’, cpds noc night’.
7, Skt. uttard-(dic-), fr. uttara- ‘up- per, higher’ also ‘left, northern’, deriv. ofud- ‘up, out’.
Skt, udici-(dic-), fr. udafic- ‘upward, northward’, fr. ud- ‘up, out’.
Ay, apazlara-, apdxasra-, deriv. of opink- ‘turned backwards’, adv. ‘back’, in accordance with the southern orien- lation in the Avesta. Barth. 79 f., 82.
Pol. péinoc ‘midnight’ of pil, pol ‘half’ and
1248, Words for ‘south’ are often
the same as those for ‘midday, noon’.
be Sources are ‘(rainy) south wind’,
“nny region’(?), and ‘right’, or with a rent orientation ‘in front’.
1, Grk..
as Bios Properly ‘south wind’, tiny’ ae * vortos, vorepds ‘damp, ee moisture, rain’, etc., prob. ye Ob in Grk. vdeo ‘flow’, Lat. nare
‘wim’, th ete, Walde-P. 2.692f. Boisacq
Gtk, u gg Sd oie. ‘mi « Lat, mersars thy! (1445) oe es also and orig. ‘mid- Hpusges Tt Similarly in the Romance midi, § ; as mezzogiorno, mezzodi, Fr. tay, ediodia, all lit, ‘noon, ance
TAL RELATIONS:
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 873
Lat. auster ‘south wind’, also ‘south’, prob. orig. ‘east wind’ : ON austr, etc., feast’ (12.45), with shift through ‘south- east’ explained by the diagonal position of the axis of Italy. Walde-H. 1.87. Ernout-M. 94 (with some doubt).
Fr. sud (> It., Rum. sud), Sp. sud, sur, fr. OE sap (below, 4). REW 8424.
3. Ir. descert, NIr. deisceart, epd. of dess ‘right, southern’ (12.41), with cert as in téascert ‘north’ (12.47).
Ir. téias, NIr. thuas, adv. ‘above’ and ‘in the South’, that is, t-was, fr. was ‘above’ : Grk. ty ‘on high’. Pedersen, Don. Nat. Schrijnen 424.
W. deheu, de, lit. ‘right (hand, side)’, as adj. ‘right, southern’ (12.41).
Br. kreisteiz, also and orig. ‘midday’ (14.45).
4. ON sudr, OE sip, etc., general Gme. (the MHG and NHG form with- out -n- fr. LG), Gme. *sunpa-, orig. perh. ‘toward the sun, the sunny region’ : Goth. sunnd, etc., ‘sun’, like the words for ‘east? fr. ‘dawn’. Walde-P. 2.447. Falk-Torp 1224 f.
5. Lith. pietas (pl.) also and orig. ‘midday meal, midday’ (14.46).
```


## [2026-09-04T22:42:33.897Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3240,3252p' KLN_1966.txt | cut -c1-200",
 "description": "Klein page marker near apt"
}
```


### [2026-09-04T22:42:33.950Z] TOOL RESULT

```
appurtenant,  adj.,  appertaining.  —  Mb.,  tr.  M. apurtenant,  fr.  OF.  apartenant,  pres.  part,  of apartenir.  See  prec.  word  and  -ant. apricate,  intr.  v„  to  bask  in  the  sun;  tr
April,  n.  —  L.  ( mensis )  Aprilis,  lit.  ‘the  month  of Aphrodite’,  fr.  Gk.  ’A<ppw,  a  short  form  of ’  AippoSfrr).  See  Aphrodite.  Cp.  L.  mensis  Maius, ‘the  month  of  
Derivative:  April-ine,  adj.
a  priori,  1)  from  cause  to  effect;  2)  deductively; 3)  not  derived  from  experience  (phdos.)  —  L. a  priori,  ‘from  what  comes  first’,  fr.  a,  ‘from’ (see  a-,  ‘from’)
See  prior,  prius.  .
apron,  n.  —  ME.  napron  (through  misdi vision  of a  napron  into  an  apron),  fr.  OF.  naperon,  dimin. of  nape,  nappe  (F.  nappe),  dissimilated  fr.  mappa, ‘tablecloth,  napkin’.  
apropos,  adv.,  opportunely.  —  F.  d  propos,  ^  to the  purpose’  (  =  L.  ad  proposition),  fr.  a,  to (see  a),  and  propos  (fr.  L.  propositum),  purpose  .
See  purpose  and  cp.  malapropos,  malapropism. Apsaras,  n.,  one  of  the  nymphs  of  India’s  heaven (Hindu  mythol.)  —  OI.  Apsardh,  lit.  ‘moving  in the  waters’,  compounded  of  
serum.  .  ,
apse,  n.,  r)  a  semicircular  extension  at  the  end  ot a  church;  2)  apsis.  —  L.  apsis.  See  apsis, apsidal,  adj.  —  Formed  with  adj.  suff.  -al  fr.  L. apsis,  gen.  apsidis.  S
‘arch,  vault’,  fr.  Gk.  &[>(?,  Ion.  ‘a  fastening, felloe  of  a  wheel’  (whence  (rivals,  ‘contact, point  or  line  of  junction’),  from  the  stem  of fircxeiv,  ‘to  fasten, 
‘to  touch,  handle,  feel’,  a(j.;j.cc,  'knot,  noose  ;  of uncertain  etymology.  Cp.  -aphia,  aphtha,  hap- teron,  haptic,  hapto-  and  the  second  element  m Anaphe,  chirapsia,  paraphi
apt,  adj.,  fit.  —  L.  aptus,  ‘fitted,  suited’,  prop.  pp. of  obsol.  apere,  ‘to  fasten’,  rel.  to  aptsci,  to reach  after,  attain’,  and  cogn.  with  OI.  apnoti, ‘he  rea
```


## [2026-09-04T22:43:25.410Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD abām/ayāb/axtar/abāxtar/Baxl\"; grep -n -i \"abām\\|ayāb\\|ayāft\\|axtar\\|abāxtar\\|Baxl\" PHD.txt | head -40",
 "description": "MacKenzie lookups"
}
```


### [2026-09-04T22:43:25.461Z] TOOL RESULT

```
=== PHD abām/ayāb/axtar/abāxtar/Baxl
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
718:acquire ayāftan, handóxtan, wind- ādan, xwāstan.
721:acquisitive ayābag.
878:astrology axtar(a)marih, kundāgīh.
886:attain abar rasidan 6, ayāftan.
898:axtar(ājmār,  staró$màr
1357:constellation axtar.
1505:debt abām.
2653:loan abām.
2936:north abāxtar.
2961:obtain ayāftan, windādan.
2993:оғ ayāb.
3142:planet abaxtar; the haftün.
3277:providence bayābaxt.
3801:star axtar, star, stārag.
4380:zodiac dwazdahan; sign of the ~ axtar.
```


## [2026-09-04T22:43:26.212Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n -i \"abām\\|ayāb\\|ayāft\\|axtar\\|abāxtar\\|baxl\" NYB_vol2_glossary.txt | head -40",
 "description": "Nyberg lookups"
}
```


### [2026-09-04T22:43:26.260Z] TOOL RESULT

```
=== NYB
504:apam [’p’m] debt 70%. — < Olr *apamna- ‘that which a p. (the lender) has to obtain (from the borrower), middle pt. of Av. (70 sqq.) ap- (v. ayāftan); as to the form, cf garämik. Paz. dwam; NP vam, āvām.
552:apaxš [’phs] changing one's mind, repent- ing 8311. — Paz. awäx$, but in SGV awaxša- dar and awaxši. Perhaps Paz. awāxš = apāxš represents the original form: < "apa-axši ‘having his eye (look) turned back’; as to "axši- cf s. v. bītaxš. apaxtar [’p’htl] 1. planet 1151; han i 7 ~ 7718-19.22, 7915-16 (cas. rect.); 62 7 ~-dn 7720; Gišan ~-dn 7919-20 (pl. cas. obl. as subj.); —-àn 1152. — 2. the north 12012, — Av. (79) apäztara- ‘northern’; MPrs ’b’zir; Paz. awāxtar; NP bāxtar ‘the west’ or ‘the east’.
824:axtar [htl] constellation, one of the signs of the Zodiac, pl. cas. obl. ~-dn: Jagr ~ the constellation Leo 511; har ~-é [~+1] 872; hàn i 12 ~ 77"; čišan 12 ~ TTL, 7913; 72 ~-dn 894; disan —-dn 79; ēišān 12 —-ān 19%, 8724; 12 katak à ~-dn 8122-28,  MPrthPrs ?xtr; Paz. NP axtar; v. also dväzdah.
825:axtar-mär [—-m?l] *Zodiac-calculator" = horoscopist, astrologer, pl. cas. obl. —-än 55.9.25, — V. s. v. ošmurtan.
829:a-x"ansandéh [hwnsndyh] discontent, displeasure: ~ kartan to cause offence 83". — Paz. axtarsandi; v. x"ansand.
838:ayāft [y*pt'] gain, benefaction 94, from ayaftan ayäp-, to reach, to attain 4618-22, 809.25, 888, 1053-12, — Ps. pt. ?y'pty; MPrs pt. ’y’pt, pres. ’y’b- (Verbum 176); Paz. ayäftan ayäw- (Mx, SGV); NP yäftan yàb-. Av. (70sq.) ap-; dp- < à- + ap-; ay- probably < abi-, cf Av. (71) avi-ap-. — The pres. st. ayäp in com- pounds: hamäk- ~, dur- ~, v. these ws. ayärtitan [’d’ltytn'] to torment 612-19, — MPrs pt. (not pres.!) ’y’rdyd; ’yrdysn (A-H I, II); Verbum 188.
954:Baxl [b’hl] Balkh 1132. — Av. Bāxtrī-, Bäxöt-; NP Balz.
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
1420:dvaristan [dwb'lstn'], dvaritan [dwb'lytn'] to run, to rush, of enemies and demoniac beings 2518 ete. passim; — andar ~. to rush, to come dashing (6 into the presence of) 7526; to make an onslaught, of Ahri- man and the demons at the beginning of the world 933.13, 9519, 10318; to make an assault upon (6) 1142; — apāc ~ to run back 1024; apar ~ to coil upwards (up a tree) 4012; — bē ~ to dash off 422, 10211.14.20; — frāc ~ to rush forth 25%; to spring forth (hac from) 9674. 9819. — Av. (765) dvar- ; Paz. duärestan, dvärestan. dvarišn [dwb'lin'] the act of running; as pred.: has to run, or is running 6811-12, dvārišnēh det. v. n. = the preceding w.: višāt- ~ the act of running about with loose, open clothes 69%, v. višat. dväzdah [dw’cdh; figure] twelve; han 4 12 axtar, 12 axtarān etc., v. axtar; dväz- dahān [dw’cdh’n'] the Zodiac 57. [12-n!] Ti: i dvàzdahom [dwb’cdhwm; 12-wm] the twelfth 8216, 844, E
2632:nàmik [n’myk] renowned, comp. ~-tar 227, 916, 178. 4727; Baxl 1 ~ 1132; v. also fräc-nämik.
2804:oi [LH], 6 [L] dem. and det. pron. this; also the pers. pron. of the 3d p.: he, she, it; when used adjectively placed before its headw.: 0? mart this man; det. 0% ke 6671; õi veh ke 223- mänäk(k)äi (g.v.) 6 či cigon ke ... 4182; 6% is the normal form, 0 is rare: 6 ydtuk 5412-18; 6 màn this palace (subj.) 5822-26, 6114.23; 6 kē he who 90? (e 5715 is prev. to mat l. 16); — gen. his, her, its: % õi placed after, or hän + oi placed before its headw.: han i õi mat 39%; — forms the def. rel. attr. (v. s. v. 2): O õi 4 tē pusar 5174; õi i äxtar sardār 2618 (but 2616 6 õi āzvar sardār); õi i dus-äkäh u vat-xàm mart 91U, etc.; changes an adj. into a subst.: õi i druvand the wicked man 7417; — pl. ētšān ['LH-š*n'] they, them, these, both cas. rect. and cas. obl., independant or adj.; ūtšān amäh hem kē we are those who, we belong to those beings that 5728-24; connected with a pl. in the cas. rect.: ūtšān hom these haoma- stalks 41!9 (subj.). 417? (dir. obj.); bē örsän gav dos milk these cows 42°; disan druž ... bē 6 došax" oftend 10228-24; to. gether with the cas. obl. pl.: pač paitiyära- keh + ... ētšān 12 axtarān 719; the con- struction is, however, unstable: ó?$ün-ic 12 aztarän (subj.) ... ravénd 8724-5; har nēvakēh 4 (obj.) ölsän axtarān (subj.) barščnd, oifün apäztarän haciš apparēnd
3396:sardar [srd?l] the chief, leader, command- er, manager, the obj. of the leadership etc. being always placed before (if a pl., in the cas. obl. —-än): axtarmärän — the chief of the astrologers, the chief astrol- oger 5°. 73-6; artestäran ~ the commander of the warriors, the general 16° eto.; äxtar ~ the stable-master 2616-18; — pl. cas. obl. ~-dn: asp ~-dn u pah ~-an the managers of horses and the managers of cattle 4418; andar ~-dn 7112; — Ar- davän ~ A. the sovereign 1*; pit u mat u ~ 6674; hacis-mas pat ~ u ~ pat auatčii dar! 685-9; Vazurg-mihr apar čišan ~ kart V. was made general over them 1212-3, — MPrs err (s’Pr BBB); Arm. lw. satar; NP salar.
3416:saxtan [s'htn'] sác- to form, to prepare, to arrange, to build, to make: asp zén ~ to saddle the horse 2514-15, 269, 2811; x'"ari$n ~ to prepare.a meal 4216, 53*; hanbürak ~ to build a storehouse 973-6.10 [sht' for s?ht'!]:!!. — Caus. of sac- (q.v.); Av. (1552) säcaya- ‘to teach’; MPrth odn s’c- ‘to prepare, to form’ (A-H III); Paz. NP sdztan sāz-; v. also passdat. saxtaréh [s’ht’lyh] industriousness, sed- ulousness 70?5. — What the Skr. v. means by the translation $isyäpanä and West by ‘flattery’ is not clear to me.
3418:saxtan [shwn'; MRY?] word, speech, passim; ~ haciš pursēnd they ask him 742.6-7, 765-6, — Av. (1569) saxtar- ‘device, plot’; MPrthPrs sewn; Paz. saxun; NP SAXUN, suxun, SULAN.
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
3988:vartišn [wltšn'] the act of turning: 1. han i avdom ~ the last turn, of the end of the world and the fraškart (q. v.) 4619; ~ 4 axtarün u gartišn 4 spahr the revolu- tion of the fixed stars and the rotation of the sphere 1205-5; ~ u gartišn + muhrak the moving and transposing of the draughtsmen 12015, — 2. pred.: turned, became 41??, — V. vastan.
5058:Bäxtri: Baxl
5839:"xir: axtar
6448:axtar: ~
7026:aužand: apa-cand āvar: ēvar āvār: ēvār āvār(ah): ēvarz āvāz: ēvāc (a)vizah: apécak āxur: axtar az: hac azadi: azateh äzärdan, äzär-: läzär- äzarm: azarm azmudan (äzmäy-): ozmutan aždaha: Azi-dahak ažgahan: ašgihanēh
```


## [2026-09-04T22:43:46.570Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apāxtara\\|ap'axtara\\|apaxtara\\|apāxaδra\\|apāŋh\\|apąnk\\|apāṅk\" BRT.txt | head -20; echo \"=== leaf for p.79 (col?)\"; grep -n \"Bāxδī\\|Baxdi\\|Bāxtri\" BRT.txt | head -10",
 "description": "Bartholomae grep"
}
```


### [2026-09-04T22:43:46.624Z] TOOL RESULT

```
18490:•  j.  naema-  1)  Adj.  'halb':  '«am  bay^m Vd.  2;  —  'nam  ySr»  "ein  halbes  Jahr (lang)"  N.45i*44'^;  —  'mmi  yJn.drä/ä "eine halbe  Jahreslänge  (hmdurch)"  V. j.gö, ti.44i  42;  —  paourwn  va  'm^m  yän apar?m  va  "das  erste  Halbjahr  oder  das zweite"  N.  44)  —  pimrumca  'me  asne (bz.  xia/ne)  aparvmca  "die  eiste  Hälfte  des Tags  (bz.  der  Nacht)  und  die  zweite"  V. 4. 45*>.  3)  m.  a)  'Hälfte,  latus  alterum': ya(  vS  'mim  yat  va  'hri^wi  .  .  V,  if ,  32, 16.  2,  Y.  Jp.  7;  V.Äioi;  — aWsr  'mat.. uparät  *mat  y.i4.T,  6'.  8,  N.5_j,  P.  23;  — haoyat  hol  +*mS/3' . .  dalinat  hat  *'mai^ N.  75;  —  '^fraoirilarai  'mat  N.fi?;  — *aevahmat  'mat  N.  7p;  —  paurvat  va 'mat  aparät  va  ^.Jj;  —  antarä^  (sd.) 'm^  V.5.43»,  51,  6.2,  3,  7.77,  8.^1,  42, 104,5.15,  16,  N.öo,  6p',  *7jT,  54,  104^; II';  —  *va  *'ma  N.pp*';  —  vaHbya 'maltiya  "von  beiden  Seiten"  V./_y.3 1—37 PüZ.*;  —  apaxtarat  haca  *mat  V.ig.i, H.2.25,  FrW,/o.43";  V.j^.s,  H.2.7,  A. 4.6.  b)  'Seite'  überhaupt:  vlspe  'mq (AP.)  F.jg;  —  vlspa^työ  'maübys  Yl /0.41;  —  ahmst  'mäi ..yahmäi  'tnanqm YtJO.  19;  y.  3,  V.Ä80;  —  usastaratibyö haca  'maiiiys  V./p.5;  1,  H.2.  35,  V.7.  2, *i6,  FrW.JO.42.
=== leaf for p.79 (col?)
```


## [2026-09-04T22:43:47.579Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apayeiti\\|apayeinti\" BRT.txt | head -10; echo \"===\"; grep -n \"aiwyāp\\|avi-ap\\|aiβy-āp\\|aiwi-āp\" BRT.txt | head",
 "description": "Bartholomae ap- forms"
}
```


### [2026-09-04T22:43:47.634Z] TOOL RESULT

```
3478:a/ayeinti  ya  *ace  paskät  vyänli  (sd.)  nsit *aoe  paskii  äfinU  "welche  all  die  ein- holen, denen  sie  .  .,  nicht  werden  sie (selber)  von  hinten  her  eingeholt"  Y.57. 39;  —  kam  «J  arsa  gavai^Tm  apayst pasiä/(sd.)  vaz^mnH  Yt. /0.86; — h5  alvS .  .  iiva.vasma  {sd.)  apayeiti  YL  14.10;  — aval  "apayaie  nama  ahmi  yat  uva  dama apayemi  ..  Yt.  J5.43.  a)  ohne  Obj. 'nachkommen'  (i^umüch):  ma  apaima paourvavaysii  {sd.)   Vr.  22.2'*.  2)  'ge-
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
8068:•  j.  iSva.vasman-  n.  'Pfeilflug':  hö  aci'v . .  °sma  apayeiti  .  .  yatcit  vazaite  hvashm "er  alleinholt  denPfeilflug  ein..;  auch  wenn er  guigeschossen  dahinfliegt"  Yt,  14.  20.
9093:•  j.  ustana'vant- Adj.  (fem.  -Taiii')  'leben- dig, lebend':  uzuitani  .  .  "vaitls  (APf.) vupa  frasumaitls  (sd.)  P.ji?;  —  hs  aet-ö 'valqm  ih-a.vaima  (sd.)  apayeiti  "er  allein unter  allen  lebenden  (Geschöpfen) . ."  Yt.
19036:asrusts  (sd.)  pairyaoyzä  Y.  43-^  s;  —  ayä'n'  Asvanane  n'^  ..  V.  5.  58;  —  Ab n°  ins  vliyätä  dafaäcinii  (Sp.  595  o.)  Y.  aevS  .  .  apayeiti  hasHt  (Sp.  592  u,)  vä 30.6;  —  mit  Ellipse  von  asti:  avalsam  ^(■akuA.  apayeiti)  n°  vä  Yt.  14.20*^; — mit ff  vlduy!  (sd.)^'  yä  ..Y.  2g.  3.  c)   im  Ellipse  von  äi^Aa  'war':  «•  aSra  frakavS
19196:•  j.  oi-vanda-  m,  'Fessel,  Fesselimg, Gefangennahme':  haomsm  yim  tüvisaiH (sd.)  'dät  apayeiti  \dusmainyagt,  sd.]  p>Sana kaca  ".  .  entgeht  man  der  Fessel  [des Feindes]  in  der  Schlacht"  Yt/^-s?.
21521:gehen', mit  Abi.;  kaomsm  yim  nivUatH riivandäi  {sd.)  apayeiti  Yt.  1^,57,
22180:haom>m  yim  mvizatti^  nivandäi  (sd.) apayeiti  "wenn  man  einen  ^Hfmustengel ansteckt,  entgeht  man  .  ."  Yt  1^.57.
23434:'jagen,  jagend  verfolgen' :^ff^a8a'a»i_j'^»t apu%ram  Janaiti  vIt  vayäti  va  xraosyäti vä  patdayeiti  (sd.)  vä  V.  75. 5 ;  —  ysi  vlsps U  apayeinti  yq  *aoe  paskät  vyeinii  ". ,  denen sie  von  hinten  her  verfolgend  nachjagen" ¥.57.29;  —  y&  *ava  ^xbayats  avaähe vyqsca  vyanasca  apatse  (sd.)  zbayeitt vyqs  apagaße  vyänS  "welche  beide  um Hilfe  rufen  der  Verfolger  und  der  Ver- folgte .  ."  Vt  i^.  3S;  —  aval  vayul .  . yat  xtia  dqma  vayemi  Yt/J.  43''.  1
25266:'schädigen,  Schaden  schaffen',  mit  Akk. : yatBt  tanBm  apayeiti  (näml.  arltis)  alcit  dim lUlil  rälayente  "auch  wenn  er  (der  Pfeil)  den Leib  erreicht,  so  schaffen  sie  ihm  (damit) doch  keinen  Schaden"  Yt  10.  a  1 .  a)  ins-
===
```


## [2026-09-04T22:43:58.434Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== CHEUNG HAP/ĀP\"; grep -n -i \"yāftan\\|ayāftan\\|\\*Hap\\|ĀP\\b\" CHEUNG.txt | head -30",
 "description": "Cheung lookups"
}
```


### [2026-09-04T22:43:58.482Z] TOOL RESULT

```
== CHEUNG HAP/ĀP
9205:*hap ‘to keep, observe’ 
11118:*Hap/f 161 
11178:*Hap/f ‘to reach, attain’ 
11183:162 *Hap/f 
12618:Perhaps, *Hrab/f is rather a blend of similar roots of motion (notably *Hap/f and 
44165:čāp-/čāpā, 33 
55109:*bauH (s.v.), *Hap/f (s.v), 
55112:*Hap/f (.v.), *Har' (s.v.), 
55311:*Hap/f, *Hnas, *tac? 
55348:*Hap/f (s.v.), suaH (s.v.), 
55498:*Hap/f (s.v.), suaH (s.v.), 
56940:*dar', *hap 
57249:*бар, *čait/9, *hap, *har! 
57517:*Hap/f, *Har', *Hnas, *iat,
```


## [2026-09-04T22:43:59.269Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==52' HRN.txt | head -60",
 "description": "Horn page 31"
}
```


### [2026-09-04T22:44:01.148Z] TOOL RESULT

```
— 80 -
125. enguM Tinger, Zehe'; vergl. etigustetl 'Ring'^
engusfioäne Tingerhut* *).
Kä§. ungüss^) (neben engüst, mgüs etc.); mäz. nngus.
aw. angusta- 'Zehe'; phlv. angust^)\ skr. angtistha-
*Daunien, grosse Zehe*.
kurd. LW. engust; oss. d. at'ndje^ ünguljä Tinger
(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
augar, §iyn. angast, sar. ingä/t, sangl. ingit.
Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
vergl. skr. atlgün-, angüli- Tinger, Zehe'.
126. efiffist 'Kohle'.
Vergl. skr. angärä- 'Kohle'.
127. engeiten antreiben', Praes. engez-em,
phlv. angfytan antreiben', angejet (AV.), vergl.
ham]vB/t (Geiger, Yätk. Zar., Anni. 52); skr. vgl.
samvignu' 'aufgeregt'.
vergl. oss. d. ve^^nn^ t. viyin erschüttern, bewegen'
(80), bei. gejag n. ge^cig 'schwingen, schleudern,
schlagen' (113).
128. enose 'glücklich, heil!', vergl. hös, nöse, nösin,^)
aw. anaosa- unsterblich'; phlv. anöäak unvergäng-
lich', arm. LW. antcsak, anois,
oss. ämisoriy änusi 'unvergänglich' (119); nicht bei.
anJmy 'Schicksal' (2) (Hübschmann, ZDMG. 44, 555).
129. ö er, jener, Plur. ösän (dialektisch, Lumsden, Per-
sische Grammatik, II, 76 Anm.; vergl. gel. üsüfi,
ühan),
ap. aw. ava- jener'; päz. ö.
Vergl, kurd. ätr, atve jener, er'.
130. o- (Praefix), u-,
aw. ava 'herab, von weg'; phlv. ö; ai. dva.
131. ewam, awam 'Schuld', loam,
phlv. äpäm (PPGL).
bei. LW. warn (288).
^) Aw. *angu8tapäna' (vergl. aw. ranapäna-)'^ oss. d. LW.
ängurstevän.
*) Der Wechsel von st und st ist häufig.
'') Vergl. Fr. Müller, WZKM. 5, 264.
```


## [2026-09-04T22:44:10.179Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==53' HRN.txt | head -70",
 "description": "Horn printed page 31"
}
```


### [2026-09-04T22:44:12.400Z] TOOL RESULT

```
— 31 —
Darmesteter's Erklärung (Et. ir. I, 75) aus
*apama' d. i. apa 4- ama- = lat. abemptum ist aus zwei
Gründen unmöglich: erstens weil die Grundbedeutung
von emö nicht ^kaufen*, sondern nehmen* ist (vergl.
lit. imü, ifriti nehmen', air. ein 'nehmen*, ksl. imq,
jpM 'nehmen'); zweitens weil lat. emö auch zu got.
tnman gehört, also seine Urform *^rwö lautet.
132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
(Jer. 51, 44).
ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
V. u.); Thron*.
ap. *avaranga- oder wohl besser '^abiranga- (vergl.
skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
134. euJzen (geschrieben evzen) 'tödtend*, in ser]ewzen
(Sahn. I, 100 Vers 714, 450 Vers 288), hezber\ewzen
(Sahn. I, 356 Vers 659).
aw. aiwi + l/^aw- 'tödten' ; phlv. afzatan (PPGL),
päz. awazadan.
Np. evzendlden der Wörterbücher ist nur eine gram-
matische gelehrte Bildung ; über die Emendation ewzen
vergl. Salemann-Shukovski, Neup. Grammatik, § 7
(dieselbe verbietet die Ableitung von ava-),
135. östUm, ustam 'treu, ergeben' (Vis und Rämin, Seite 78
Vers 12 1).
ap. ^avastaman- 'zuverlässig*, vergl. skr. ava-r
i/^sthä' 'bleiben, verharren*, avasthita- (von Personen)
'standhaft, zuverlässig*; phlv. östam bezw. tistäm
'Helfer (Men., vergl. awastäm, West ib.).
136. öi 'er, jener, vei,
ap. ava' + hya-; päz. öi.
*j Hier scheint es aber ^schwach* zu bedeuten.
```


## [2026-09-04T22:44:23.897Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11178,11200p' CHEUNG.txt",
 "description": "Cheung *Hap entry"
}
```


### [2026-09-04T22:44:23.940Z] TOOL RESULT

```
*Hap/f ‘to reach, attain’ 
*AVESTAN: ap- ‘to reach, attain’ || (+ *abi-) ‘to obtain, find’ || (+ *pati-) ‘to reach to’ 
|| (+ *pari-) ‘to reach, attain’ — Liste: 11 


162 *Hap/f 


Pres. aja-: IND. 15р. YAv. apaiiemi (Yt 5.42, Yt 15.43), 35р. YAv. apaiieiti (Yt 10.21, Yt 14.20, Yt 
14.57, Yt 17.19), 3pl. YAv. apaiieinti (Y 57.29, Yt 10.20), INJ. 3sg. Y Av. paiti.apaiiat (Yt 8.38), IMPV. 
2sg. YAv. auui арапа (Yt 16.2); Aor. them.: ОРТ. 1р1. OAv. apaema (Y 41.2); Perf.: IND. 3sg. ҮАУ. 
ара; Partic.: pres. YAv. apaiiant- (Y 9.31), perf. med. OAv. apana- (Y 33.5); Inf.: pass. YAv. afiieióiiai 
(Y 71.13); Pass.: pres. 3pl. YAv. afonte (Y 57.29); Caus.: pres. SUBJ. 3sg. YAv. apaiiat (Yt 10.86). 0 
According to Sims-Williams 1989: 257 Y Av. apaiiant- rather derives from *4-pa- ‘to observe’. 

*MIDDLE PERSIAN: (+ *abi-) MMP ’y’b- ‘to obtain, acquire, attain; to achieve 
success’, BMP ’y’p- /ayab-/ ‘to attain’ > DMMPP: 80a 

Pres.: SUBJ. 1р1. MMP ’y’b’m; Partic.: perf. pass. MMP ’y’pt, BMP ’y’pt /ayafi/; Inf.: BMP ’y’ptn 
/ayaftan/ 

*PARTHIAN: (+ *pari-) pry’b- ‘to attain, reach; to overtake, come upon’. ç On Pth. 
’b’myh, BMP ’p’m /abam/, NP avam ‘debt’ see *Hmai’. = Ghilain: 60 | DMMPP:
```


## [2026-09-04T22:44:25.539Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SOD anxar\"; grep -n \"ngr\\|nxr\\|anxar\" SOD_pages.txt | head -20; echo \"== SOD star gloss\"; grep -n -i \"^\\s*[0-9]\\+ .*star\" SOD_pages.txt | head -20",
 "description": "Gharib Sogdian lookups"
}
```


### [2026-09-04T22:44:25.633Z] TOOL RESULT

```
== SOD anxar
2530:einer Soghdischen Ubersetzung des Padmacintamani-                    of Leningrad (Frag, LenX This was followed by two
2533:                                                                     "The Sogdian Fragments of Leningrad II", Bulletin of
2536:                                                                     288; "The Sogdian Fragments of Leningrad III,
2567:Leningrad (St. Petersburg) in Russia were published
2579:                                                                     55. It docs not cover Buddhist Fragments of Leningrad
2587:Wiliiams,     "The    Sogdian    Fragment   of   Leningrad",             this study until now.
2629:                                                              61. See, for instance, G. Widengren, Mani und der
2707:date.73 F.W.K. Muller was again the first to study the             Sogdian manuscript in Tajikestan reached Leningrad
2806:                                                                    International Congress of Orientalists, 2, 196ft pp.
3652:    Petersbrug (Leningrad).                                       Dokumenty s Gory Mug, /. Moscow, 1962.
5160:    (to)bc lit up, 0o)bccomc angry
5165:    lit up, angry
5176:    angrier                                                         C2, 23V10n p61
5435: 582 »pyz'krtyh B                             .Lfu,jr                 (o)Pz-anxare ©pi. -*
5711:      first                                                                   (to)gct angry
6610:     anxaste ©pp.     ^'nxstyy                       "C ->■*"        anxar ©<*ana-har ? ©pi. -/ =^'nxr
6627:    anyaw ©<*ham-gama                                           1012 'ngr'nd-     M                           u-^<Cp^bA
6629:                                                                     angrand Ongrnd-) ^nkr'nt-
6638: 'ngrnd-                                                                                                                  40
6641:       anxar-kase      ©pl-t(h)
== SOD star gloss
5842:724 >Ysy>5 S                                 jzU-wjsf             (o)xsankistar
7778: 1393 >pw zn'kh B                               jbU t^h JjJj               opistarick (pystycyk)
7784:1394 'pxyyr- =* pcyyr-                                                      opistar(u)        ©comp. adj. =*pystrw
8637: 1685 »stVk B, M                                   >>-                    1697 'starch B                                     ^«aU
12304:      2995 pyk Syn>k B           (j*> J' £j^)j^ <*V <-^                                   Pek-star (byqstr) =»Pystr         (>^j^)-^"*>j^
12703: 3147 c'nw B                                    jt,^                   castar ©<*c}Jsrr <cySrstr **c}8x
23008:6709 pcwz-' M, B, S (jy y--^ j->)o>jj^j <O^TolS:**                pacxo5-yonestar
23875:7018 pr'ynk1    B, M            jjj «z>jy+ j/ 0.r.«..jf)flj>? < jj,         paristarn   ©impf. =»*prstrn-, prJstr-
27845:8369 pys(>)y =* pys>k                                              pistarecik
29588:8950 sr8S M                                               JU        mustard seed
31705:9691 trzmnw      S =» trzmnw                                     tawandistar ©comp. adj.
32583:9996 wy'rs- B, S               JojUj i&J'd jT <oju^ Ojj*           famine, starvation
```


## [2026-09-04T22:44:38.767Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6595,6660p' SOD_pages.txt",
 "description": "Gharib entry context anxar"
}
```


### [2026-09-04T22:44:38.807Z] TOOL RESULT

```
        1983, 46                                                      0o)picrcc, (ro)prick
                                                                      SCE 100, 48p45; AVS 114
 993 'ny's B                             ju^IjmX*.
     anxas ^ny's, }x}s                                          1006 'ngm'n C                                    ^'j****
     struggle, dispute                                               angman ^'ncmn, ^jmn, 'njmnyq
     GMS 659; TSP 13ii7; Vim. 139, BSTBL; Bcnv.                      assembly, crowd
                                        o*£t60.2
       Notcsiii 222; Notesiv 199; Sogdica.  }-                       BSTi 236

 994 >nY)st- B                                                  1007 'ngm'ny' C                                ^jA^'j^
     anxast ©<*ham-xasta         ©pt. st. -^nY^-, }nxst               angmanya    ^'nkm'nCy)
                                                                      in face, openly
     (ro)picrcc, (to)prick
     SCE 169; AVS 114                                                 GMS 1037; STi 74.2; Bcnv. Notcsiii 203
 995 »nY*stk B                                                  1008 'nyr B                     Jk^i^fji^
     anxaste ©pp.     ^'nxstyy                       "C ->■*"        anxar ©<*ana-har ? ©pi. -/ =^'nxr
                                                                     star
     pierced
     SCE 169                                                          VJ 25, IT; TSP 3.148, 150; Andreas. SPAW
 996 »nY's- B, S                                                        1910, 310
                                     jj^tf ^ ^JV^
     anxas Ony'nz-) =»nxs-, pY'rs- 'nys-                        1009 'nyr^mnyy       M =$ 'nyr'mn'y
     (fo)withdraw, (ro)retirc
     BSTBL, Dhu. 210; Frag. Len. Ill V5                         1010 'nYr'm- B           Q;>bflJo ij^J'j^^ O^jo^v
                                                                     anyram ©impf. mYr^m
 997 >nY'st- B                           J^^s <tf*J%                 0o)slander
     anxast ©pt. st. ^nyz-, toyst-, vxst-                            SCE 243
     (to)risc                                                   1011 'nyr'nui'v     B                      exjfr^y o j^~*#
     VJ 1133; BSTBL, Dhy. 253; AVS 80, 132                           anyramne       Onyr'ninyy)     ©pres. part,
998 'ny'tch S *± 'nytch                                              slanderer
999 >nY>w B                                                          SCE 145; GMS 892; Sogdica. p52
                                                  i^v i<-^bii
    anyaw ©<*ham-gama                                           1012 'ngr'nd-     M                           u-^<Cp^bA
    haste, effort
                                                                     angrand Ongrnd-) ^nkr'nt-
      VJ 129; TSP 13.15; GMS 351A                                    0o)cut in pieces
1000 'ny'wnc =» mywnc                                                GMS 48, 245; BBB 500; Hen. Magi. 143.19 n 2
1001 >nY'wy-    B =» myw'y-1                                    1013 'nyr'n rwc S               (0>':tyJ^)ftUf,.j- JJJ
1002 'nfyz- B                                                        anayran-roc, Anaghran    (nyrn* rwc)
                                    O^Uo^xL                          Anagran, thirtieth day of the month
     anxez Onyyz-) ©inf. -»y ^nyz-, }nxyj-f }xyz-,                   MDiii BUR
       'nx^z-
     GcOrai;tse                                                 1014 toyrks'y     B                         ^Uiojlx- <^>^i
 'ngrnd-                                                                                                                  40

                                                                        anyat-mazen      Cytmzyn)
       anxar-kase      ©pl-t(h)
       astrologer                                                       completely armoured
                                                                        GMS 335 n 1
       VJ21.81, 13\ 27, 58
                                                                  1026 >nyttc     M => >nytch
 1015 }ngrnd- =* 'ngr'nd-
 1016 >nyrs-     S                                                1027 >nyty' B                     (u>>>^- jj)>1^*<*a
                                           OJLta^^ loX^lai — *
      anxars     (nyrs-) ^nys-                                         anyate Onytyy) ®<*ham-gata-ka\ Parth.
                                                                         angadag\ A v. hsngata-, Oss. dnYdd; Khwar.
      (/o)overtake
      MDii B-17 R7 pl20.7                                                  }ngdi OP hagmata =*}Yty\ 'nyt'k
                                                                        all, entire
 1017 >nyrwzn     B                                                     BSTBL; GMS 335, 1273; Frag. Len. 50, 6; MSP;
                                        ^^C^'C-3^15^
      anxar-wazan       ©Parth, axtar-wazan ©pi. -'/                      Gersh. TPS 1979 125; BBB b47, -yyh
        =>}nxrwzn, 'xrwzn                                         1028 >nyty: B                                Jji^j^
      zodiac, constellation                                             anyate, anyati ? <§><*ham-gati\ <*ham-gata;
      TSP 3.151; BSTBL, Dhy. 168, 238; Hen. Texts.                        *hama-gata     =*}yty:
        727
```


## [2026-09-04T22:44:39.648Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*Hmai\" CHEUNG.txt | head",
 "description": "Cheung Hmai index"
}
```


### [2026-09-04T22:44:39.694Z] TOOL RESULT

```
11200:’b’myh, BMP ’p’m /abam/, NP avam ‘debt’ see *Hmai’. = Ghilain: 60 | DMMPP: 
12120:*Hmai2 177 
12131:*Hmai ‘to fix(ate), build, fashion 
12180:178 *Hmaijl ? 
12206:*Hmaij! ? ‘to exchange’ 
12216:*Hmaif? ? ‘to pour, flow, rain’ 
12224:© According to Mayrhofer, EWAia, Le IE *Hsmeié - ‘to urinate’ (> Ir. *Hmaiz) 
12244:*Hmaiz ‘to urinate’ 
55869:*Hmai', *skamb (s.v.), *suaH 
55984:*gart (s.v.), *Hmai’, *harH
```


## [2026-09-04T22:44:52.775Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12180,12245p' CHEUNG.txt",
 "description": "Cheung Hmai1 entry"
}
```


### [2026-09-04T22:44:52.825Z] TOOL RESULT

```
178 *Hmaijl ? 


*MIDDLE PERSIAN: (+ *apa- BMP ’p’m /abam/ ‘debt’. 0 The etymology and 
reconstruction given by Nyberg 1974: 22a (notably for the Pahlavi form), from 
partic. med. *(&-)apamna-, is less convincing. 

*PARTHIAN: (+ *apa-) ’b’myh ‘loan’ = DMMPP: 8 

*SOGDIAN: (+ *apa-) BSogd. p’myt’y, BSogd. p’mytk, BSogd. p’m’ytk ‘loan’ 
*BACTRIAN: (+ *apa-) Bapddtyo ‘loan’ = S-W, Bact.: 185a 

*NWIR: (+ *ä-apa-) NP avam ‘debt’ 

*SANSKRIT: may ‘to exchange, change’ || (+ *apa) apamitya- (AV +), apamitya- (n.) 
‘something borrowed, debt’ (Kath. +) > EWAia П: 314 

«PIE *Hamei- ‘to (ex)change’ = LIV: 426 | Pok.: 710 

*IE COGNATES: Toch. B mäsk-, Latv. miju (mit) ‘I exchange’, Lith. mainas ‘change’, 
OCS ména ‘change’, OHG mein ‘deceptive’, (with enlarged root-element) Gr. 
Aneißo ‘to (ex)change’ 

*REFERENCES: Werba 1997: 216 f.; Adams 1999: 459 


*Hmaij! ? ‘to exchange’ 

*BACTRIAN: uty- ‘to exchange’ = S-W, Bact.: 204a 

© The evidence for this root in Iranian is limited to Bactrian. 

«PIE *H,meig”- ‘to exchange, change for’ = LIV: 279 | Pok.: 713 
*IE COGNATES: Gr. &petBo ‘I (ex)change’ 


*Hmaif? ? ‘to pour, flow, rain’ 

*CHORESMIAN: (+ *pati-) pemyz- ‘to flow abundantly’, pcmyzy- ‘to let (it) rain’ 
c» Samadi: 142 

*NWIR: Bal. missit/miss- (inch.) ‘to wet, soak, drench, moisten’, Awrom. mitáy/mij- 
‘to pour out (abundantly) = EWAia П: 381, s.v. meh ‘harnen’ 

© According to Mayrhofer, EWAia, Le IE *Hsmeié - ‘to urinate’ (> Ir. *Hmaiz) 
shows mutual influence with IE *Hameig'"- ‘to pour, flow’ (in the ‘cloud, nebula’ 
formations) in the separate IE languages. This is a rather tenuous approach, on 
which see Cheung, F's Klingenschmitt. There is no clear evidence that in Skt. a sepa- 
rate root *MEH ‘to pour, flow’ has existed: the formation Skt. ni-méghamana- from 
which this root has been abstracted may be interpreted differently: cf. *maij” ‘to 
move’. The Iranian forms might reflect the denominative usage of the well-attested 
PIE ‘cloud’ form: *H;mig"- ‘cloud’ ? Alternatively, the forms might point to the 
existence of an old PIE verbal root *Hsmeig"- ‘to pour out, nebulize’ (?), cf. Ger- 
shevitch 1974: 89 ff. No further support in IE for such a root can be cited though. 
«PIE *H3mig - ‘cloud’ => LIV: — | Pok.: 712 

*IE COGNATES: Gr. оріҳАт (Ё) ‘nebula’, etc. 

*REFERENCES: MacKenzie 1966: 102; Shahbakhsh: s.v. miss- 


*Hmard 179 


*Hmaiz ‘to urinate’
```


## [2026-09-04T22:45:10.476Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v4 pdf 337 (printed 2254)\"; awk 'BEGIN{RS=\"\\f\"} /pdf page 33[5-9]\\]/' incoming/BQT/BQT_v4_pages_faseng.txt | head -60",
 "description": "BQT p.2254 vām"
}
```


### [2026-09-04T22:45:17.703Z] TOOL RESULT

```
=== BQT v4 pdf 337 (printed 2254)
awk: cannot open "incoming/BQT/BQT_v4_pages_faseng.txt" (No such file or directory)
```


## [2026-09-04T22:45:20.345Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls; echo; grep -c \"\" BQT_v4_pages.txt",
 "description": "List BQT incoming"
}
```


### [2026-09-04T22:45:20.392Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf

22553
```


## [2026-09-04T22:45:23.516Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"pdf page 33[0-9]\\]\" BQT_v4_pages.txt | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /pdf page 337\\]/' BQT_v4_pages.txt | head -60",
 "description": "BQT v4 page 337"
}
```


### [2026-09-04T22:45:26.323Z] TOOL RESULT

```
13279:[pdf page 330]
13323:[pdf page 331]
13359:[pdf page 332]
13406:[pdf page 333]
13451:[pdf page 334]
13496:[pdf page 335]
13544:[pdf page 336]
13604:[pdf page 337]
13648:[pdf page 338]
13685:[pdf page 339]
---
[pdf page 337]
بالیس <<
محراها از دور بآب میماند ‎٩‏ - و بمعتی زاری | کوبتد۹٩‏ » ومعتی دویم راکه رنگه ولون وشبه
کردن ومبالقه نمودن درکارها نیز آمده‌است؟ - | ومانند باشد بدون ترکیب استممال نکرده‌اند +
ویکسر لام و تلهور هاء درعربی حیران و بیخود وامران۷ - بکرئالكبروزدحاضران,
وس رکعته ازافراط هشق ومحبت را کوبند - گیاهیت که از ملك چین آورند ومامیران هم
والیس؟ - با ناك پتخالی کشید. | کوینش . سفیدی باغن وسفیدی چشم را زابل
وی ماضد زد ۱ ۵ کی است که ایس کند .
وجل در بوده (۱) ۰ ۰
رس
مربخ است واو درآسمان پنجم می‌باشد - در وجود آدمی مر ثب‌است چه این بمنز
9 - بر وزن لام , بممنی قرض ودین | قرضی است آدمیرا اززمین +
است۴ - ورنگه ولون 8 - وشبه ومانند را نیز و امق - بروزن‌عاشق, لام‌عاشق عذراست
() چش : بود - :
- ازشوق روت جاب خود میکنم نگاه چون تشنه کزعطش بسوی واله میرود.
سیف اسفرنگه « جهانگیری ».
۴ - آورد سبك طعام در پیش حلوا وکلیجه از عدد بیش
چندانکه درو نمود واله زان سفره نخورد يك نواله.
نظامی کنجوی « فرهنگه نظام ».

۴ - فالیی (ر3 : تاریخ الحکماء. قنطی. چاپ ليبسك سص ۲۹۱؛ الفهرست ابن‌الندیم
چاپ مسرس ۳۷۹ ). مصحف والنی , ۷21685 ۷۵۸115 هنجم پونانی ازمردم انطاکیه ( قرن
دوم میلادی ) ر4: تقی‌زاده. گاه شماری ۳۱۹ و۳۱۷ ؛ نالینو . علم‌الفلك. طبم‌روم ۱۹۱۱م. ص
۳ ه ۲۱۹9۱۹۵ : ۰

فلاطون و والیی وفرفوربوی که روح‌القدس کردشان دستبوی.

نظامی کنجوی. اقباز نامه چاپ ارمغان ۰۱۲۰
نظامی در زمان او اشتباه کرده‌است. رك : حکمای سبمه. بقلم نگارنده . مجلةٌ فروغ علم۱: ۱ص
۱۳-۲ ؛ بلیتای بقلم نگارنده . مجلةٌ داش ۱: ی 464 جح ۵۵ ۰

۶ صفم (م.) #افام < بام < پام * اوام . پپلوی 8022 ( قرض » دین ) » ایرانی
-802028: ( چیزی که دربافت شود ) ۰ از -88 و -8788 - از 280 تس : 8272016

و 08224 « یب ر که س ۱۳ ۰4 در اوراق مانوی بپعلوی 2ل(0180* ( عاریت » قرض )
ظرسی » ارام ( 80 .0 ....:۳679188 ۸114416 0۲ افنا ۸ ,17162528 )

هزار بوسه فروست برلب تو مرا تووام دار منی خیز و وام من‌بگزار!

* فرخی سیستالی . دیوان سس ۱۹۵ *.

عفم (ه.م.) ۳ اوام ۶ پام ۳ بام . رك : ص لو ازدیباچهٌ مولف .

عم (م.) ۷ -ظ . مصحف «مامیران» .
```


## [2026-09-04T22:45:41.305Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'BEGIN{RS=\"\\f\"} /pdf page 502\\]/' BQT_v4_pages.txt | head -60",
 "description": "BQT p.2419 yāftan"
}
```


### [2026-09-04T22:45:43.163Z] TOOL RESULT

```
[pdf page 502]
ساددنها باه
تحتانی لون» بممنی‌باسمون است که کل باسمن یاه - بروزن‌بافته, قبض‌الوسولوحبت. .
باشد . و اصل خط راکوبند .
اه < بروزدکت : پستی رد ورن ۱ هافر س بقع بات پروزنسان بازکن
وقاعده وقالون باشد۱ - وبمعنی خواهش وآرزو | ورقاس را .کوبند؛ وبکسر ثالك هم آمده است.
هم آمده است؟ وبعربی‌تمنی کوبند ‏ باقه؟۴ « بنتح ثالك بروزن نافه. کمشده
یاشق « بنم شین‌قطه دار پروزن فاشق, | و باپدید کشته را میگوبنده - و اسشنان هرزه
بام درختی است.* وبیهوده وسرد رگم وپربشان و هذیان و فحش را

۹ باسا (مغولی) ر4: باسا : ۱

کان آسیران را بجز دوری نبود دبدن فرعون دستوری لبود

گر فتادندی بره در پیش او بهر آن باسه بخفتندی برو

باسه این‌ید که لهبیندهیج اسیر درگه و بیگه لقای آن امیر.

مولوی بلخی رومی «مثنوی. چاپ لیکلسن دفتر سوم ص۹۶۸.

۴ - هوبشمان گوید: 1288 ۳ پهلوی #28821 ازاوستا وپارسی باستان- 8858 ۰
هوبشمان وجه اشتقاق هرن «اسشق ۱۱۲۳ را قبول ندارد. رله: هوبشمان ۰۱۱۲۳

۴ - «بافن, بازیگر را نامند» «جهانگیری» . مرا گوید : «وبمشی رقاس نیز گفته اند
وظاهواً میدل *یاور» است . درین صورت تصحیف دراین معنی است که «باریگر» برای مهمله را
«بازیگر» بزای معجمه خواندء اند.» جهانگیری ازسروری واو ازموید نقل کرده» پی‌سحیف از
جهانگیری لیست «فرهنگه نطام».۰ ۰ ۴ ۳ یاوه (ء.م.) «یافه, وخله وژاژ ولك حمه پیهوده
بوده ولی ز کوبند خله کردم وباقه کردم و کم کردم وهرز هکردم.» «لفت قرس ص4۹۳ +

8 -گو بافه‌شو قلاده زرین آسمان لور کف خجتهٌ او زیور تو باد.

شمس طبسی «رشیدی» «فرهنکه نظام» .

۵ یافتی - بفتح چهارم, از : یاف ( ۳ باب) تن (پوند مسدری) پهلوی 741128 ۰
0 . فی : اگفْلاة . استی 02[78100 ۰ 210ر[2 ( رسیدن ) «اسشق ۰۹۱۱۲۶
هوبشمان کوید: فارسی: پابم. یافتن ۳ پلزد 2[41088, ازريشة 20لا با ططاقل. استی 28۶18
از 12018 مشتق است؟ "هوبشمان ۱۱۲۶؛ پیداکردن, بدست آوردن. کب کردن .
بقیه از حاشيهٌ صفحهٌ قبل
را مخصوص سوسن‌سفید داسته‌اند... وجمهوراطیا تعریف باسمین‌نموده‌اند که درخت اومانند درخت
مورد واملی, برکش نرمتر ویهن‌تر و بنطبری بر که مورد لیست . درخت قسم مفید او ضیف
وگلش مفید و با شایبهٌ مرخی وبسیار خوشبوی وازوقت شکفتن لرکس تا اول عقرب کل میدهد
ودر بلاد حاره همیشه » ودرخت نوع زرد او عظیم و چتری ومانند درخت موز است » وتزد بسنی
قم زره ار مسمي پزایق اسی...» «تحقهٌ حکیم مژمن».
```


## [2026-09-04T22:45:56.149Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 300<i<330 and ('اختر' in p or 'باختر' in p):\n        print('LEAF',i, 'printed~',i-210)\n        print(p[:2500])\n        print('======')\nEOF",
 "description": "BQT vol1 axtar"
}
```


### [2026-09-04T22:45:58.929Z] TOOL RESULT

```
LEAF 301 printed~ 91
« ری الافی » خوانند ؛ و بجای بای بجد بای
اخت - حم اول وسکون ثالی وفوقانی»
بممنی مثل‌ومانند و قرین ولظیی باشدب وددعریی
خواهر را گویند » و بی بممنی اول نیزعریی
میدانتد ۴ .
اختر ۴ ه بر وزن افر » رابت وعلمرا
گویشد - و بمعنی بخت و طالع هم هست -
و ک وکب و ستاره را یز کوبند - و بعمتی‌فال
و شگون هم آمده است - و نلم فرشته ابست
مو کل کر زمین (۱)- و عم یکی از متازل قمر
کنابه از کوکب عطارد است - و کو کب‌مشتری
را نیز کویند .
اختر ستان - بکس رای م للم کتایی
است در علم هیأت و نجوم .
اختر شهر ه منج و نسوم دان را
اخترکاوبان
اخشر شهر ذن «کنابه از شب بیداری
باشد .
اختر شناس - بسنی‌اختر شمراست
که منجم و جوم دان باشد (۳) . *
اخمر او ان - با کاف و واو پروزن
ار شاهان , مخفف اختر کاوبان است ت که نام
علم افربدون (4) باشد . د آن از کاوة آهنگی
بود ویادشاهان عجم بعدازشکت ضحاك آنرا بر
خود شگون کرفته بودند ».و آن چرمی بود که
کاو؛ آهنگر بوقت کار کردن بر میان خود
طلمات بغایت عاهر» شکل صد در صدی برآن
هش کرده بود + وبستی کوبندشکلی ازسوختگی
های آش در آن چم بهم وسیده بود که این
خاصیت داشت » نی درهر جرد که آن‌همراه
ی شد و آنرا مرفم کرده بودند
ودر زمان حرت رسالت یناه صلرات ال علیموآ له
(ه) بدست سلمانان اقاد وآنرا باره پاره کردند
و بر مسلمانان فسمت لمودند ۴ ,
اختر کاویان -
بروزنرهی غاز بان.
کوند . حىان اختر کاواست که علم فربدون باشد ۴ .
)۱( خم ۳ : که مو کل کر؛ زمین است )۱( خم ۳ : - است .
(۳ خم ۳ : را گوبند . (4) خم ۳ : فربدون . (ه) چك : صلمم .
۰ ولی صحیح‌اخیون است
/ - هر دو عری است
۲ ( ساره) « اونوالا ۳۳۰ >
۴ - هلوی 9186 ؛ منلی ۲۹۸ : ۲ *  ,‏
درفش کاوبانی برما واسح ات ۰
در روی لته سد
======
LEAF 302 printed~ 92
وخواهر زاده را گونند .
اخروش « با رای فرخت بر وزن خر
اخ‌تفی - جنم ثالث وفا :۰ اج و لف را
گوبند که آب دهن را جمم کردن و انداختن
باشد . کوش » خروش و غوغا و شور را کویند .
اخته - بر وزن تخته » بمعنی خابه اخریان - بر وزن پرنبان » غماش
بیرون کشید» باشد . ومتاع و اسباب و کالای بر گزیده را گویند .
ی آستان اخر اط » بکسر اول و الت وسکون
درخانه را گویشد . انی و تحتالی و طای حطی » کندنای صحرابی
را کویند . فولنج بگشابد و بول براند . بعربی
۳ ق . م واقم‌شد ودر این جنک بود که اسکندر داربوش آخرین پادشاه هخامنشی را شکست
داد . درطرف چپ انن تختمسنکه صورت اسکنفو را کشده‌اند که درمیان سیاه خو یش سوارابستاده
است . درطرف راست روبروی اسکندر ؛ داربوش روی گردونهٌ جنگی ابسناده است و اودرمیاناعکر
ابرانی‌است که ازهجوم لشکراسکندر درشرف فرارهستند. درعقب داربوش‌سواری بیرق دردست دارد.
متأمقانه همین قست خانسکاری شکتی واردامده است که بدانواسطه درست مشگه‌یرق هویدا
نیست ولی‌باوجود این‌فسمت بالابی خودییرق ونوك نیزه‌ای که بیرق بدان وصل‌است وهمچنین‌قسمنی
از ریفه‌هابی که برای زینت برق آویشته بودند بضویی نمابان است انسا .که شهر ممیتی در
تال ۷۹ م زبرمقذوفات کوه وژوه خراب وینهان کشت بس باست ظاهراً این تخته مگیهخاتمکاری
مدتی قبل از ايين تاریخ باس رتیت ناید روقا کان مود که تاریخ نمام شدن این تخته منگه
یبا مرن با زمان تولد حضرت عیسی باشد .
شکل دیگری هم که تقرباً ازهمان عسرباقی مانده شباهت تامی با تصوبر درفش مذ کور
دارد . این‌شکل عبارت است ۱ و ی
که درمملکت اصلی هخامنشبان یمنی فارس نفوزی پیدا کرده وتا زمان اشکانان‌حکمرانی میکردند
وجندان نفوذ واستقلال بافته بودند که سکه بنام خود میژدند . لفب این سلمله قراتا کارا بوده .
روی سکه ققط سریادشاه را نشان مبدهد » در پشت سکه آتشکده ای که بادشاهان در مقابل او
ایستاده نماز میگزارند منقوش است . درعفب آنشکده شکلی دیده میشود که ازهرحبث هم‌شبیه به
بیرق ابران درخاتمکاری پمینی‌است وهم شباهت تام بدرفشس کاودانی که فردوسی(درشاهتسامه) وصف
کرده است دارد و همچنین آن اختری که فربدون با جواهر زینت داده و برروی چرم یار بیرق
نصب کرده بوده است بطور وضوح نمادان است . از توافق این سه ماخذ ( خاتمکاری پمینی » سکه
های سلسلهٌ مزبور , شاهنامه) برمبآید که درفش‌مزیور عبارت بوده از مکقطعه چرم پار؛ مریم ی که
بربالای يك نیزه نصب شده ونوگ نیز ازیشت ت آن ازطرف بالا بدا بوده وبرروی چرم که هزین به
حربر و کوهر بوده شکل ستارهای بوده م رکب ازچهاریرء ودر مرکزآن دابر کوچکی و همچنین
در فوق آن یز دایر# کوچکی که قربب بیقین هماست که فردوسی از آن باختر کاوبانی تعبیر
میکند. واز طرف فحتانی‌چرم چهاررشه برنگهای مختلف سرخ و زرد و بنفقش آویخته بوده و نوك
این ریشه‌ها مزین بجواهر بوده است « له کاوه » صفعهُ ۳ و 4 ۶ کاوه و درفش کاوبانی » بقلم
استاد اسکارمان > .
اختر شناسی - عمل اخترشناس . تنجیم « لفت‌نامه > .
======
LEAF 303 printed~ 93
«کراث الک رکم » خوانند .
اخسمه - بفتح اول وسکون انی و شم
سین بی نقطه و فتح عیم » بوژه را گویند و آن
شرابی‌باشد که از آرد ارزن وجو و امتال آن‌سازند.
آحسی » بروزن مخفی . نام فصبه‌است
از ماوراء النهر در ناحيهٌ فرغانه ء از بهترین آن
بارد است ۱
2 ‌
کاف» بمعنی اخی است که تام قصبه ای باشد از
ماوراء الثهر۱ ۰
فاق واسش اقسه لیات ی
باشد از ماوراعالنهر در نهایت خویی و مولد اثبر
الدین است . واوشاعری‌بوده مشهور ومعروی؟ ۰
اش تم اول و سکون ثانی وشین
قرشت » قیمت وابها و ارزش چیزی باشد .
وتقیض ومخالف باشد - و هربث از ءاصر اربعه
را نیز گفته اند .
| خشیلك « باکاف بروزن و معنی‌اختیج
است که ضد و مخالف - و هرك از عناصیباشد؛
و مجموع را اخشیگان کوند .
اخگر با کاف فارسی بر وزن اختر .
پر آعی رخشنده را گویند و بعربی جمره
خوانند - و کنابه ازمادء عشق و عاشقی هم هست.
اخگل - بغتح اول و خن کاف فارسی -
و سکون ثانی و لام » داسَهٌ کنشدم و جو را
گوند » یعنی خهای سر تیز که برسر خوشهةٌ
کندم و جو مباشد .
(4) چك : اسنا و دساتیر .
4-۱ : اخسکت .
اخگوز نه - بنتح زای فارسی و نون »
اخک ولگ - بروزن وه .دای
اخلکندو - بنتح اول و لام و کاف
وسکون انی و نون ودال اببمد مضموم بواو زده»
بازیچه ای باشد اطفال را ؛ و.آنْ چنادت که
چیزی بسازنه مدور و مبان خالی از می با از
آن سنگریزه ریزند ودسته‌ای یر آن نصب سار ند
۴ بدست اطفال دهند . چون آنرا بجنبا تندصدامی
ازآن برآمد » بدان ای ؛ واخککندو
بفتح دوکاف هم بنظر آمده است
اخلور - با لام بر وزن مور »
خرنوب بطی‌باشد» وآن میوماست سرخ بسیاهی
مایل بشکل کرده کوسفند وآنرا بشیرازی کورز
(۲) گونند وآن یو کبر باشد» با س رکه پرورده
کنند و خورند ۰
| خهساه - با سین بی‌قطه بروژن‌حخیصه:
و آرد ارزن سازند .
اخنوخ" - با نون بر وزن مطبوخ »
نام آدرس پیغمبر علیه السلام (۳) است » و جضم
اول عم .گفتد اند - و بسنی کویند تلم لوح‌پیشمبی
است .
احواستی - با واو معدوله بر وزن
بشوامنی » بمعنی غیر ارادی باشد چه خواستی
بمعثی ارادی است بزبان استاد دساتیر (4) 9 .
۳ چك : عم .
رجوع بلخت نامه شود .
۴ - ۲۲6۵06۲ _ ۳۳۵6۷ . خنوخ .
======
```


## [2026-09-04T22:46:10.395Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'باختر' in p:\n        print('LEAF',i,'printed~',i-215, p.count('باختر'))\nEOF",
 "description": "find bāxtar leaves"
}
```


### [2026-09-04T22:46:12.624Z] TOOL RESULT

```
LEAF 164 printed~ -51 1
LEAF 302 printed~ 87 1
LEAF 424 printed~ 209 2
```


## [2026-09-04T22:46:16.391Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[424]\nimport re\nprint(p[:3000])\nEOF",
 "description": "BQT leaf 424 bāxtar"
}
```


### [2026-09-04T22:46:18.981Z] TOOL RESULT

```
ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
است که مصفر باجه باشده و باجه مخفف بادجه
و پادجه بمعنی باد گیر و باد گیر جایی و دوزنی
را کویند که باد از آنآمدو شد نماید واله‌اعلم .
۱ باجه پفتح جیم بروزن راجه ؛ دربچه
و دوژنه (۱) بزر که را گوشد ۱ . ۱
باحور با حای حملی بروزن کافور »
بخاربر| گوین که درهوای کرم از زمین‌برخیزد-
در عربی بمعنی بیاری وسختی کرما باشد ۴ .
پاحو اه با زبادنی الف ؛ لفظی است
بونانی بمعنی روز کار آزموده » و ایام آن هفت
روز است و مضی گویند هشت روز ؛ اشدای آن
دا 0
و۳۵ امس
بود » وصنی گوبند معنی این لفظ شدت وزیادتی
از بحران بمعنی حکم » یعنی ازین روز هاحکم
کنند بر احوال ماههای خزان و زمستان » وروز
او آن دلیل‌نشرین‌الاول (۲) و روز دوما ندلیل
شرین‌ال خر (۳) تا باخر, هرچه در آن روز ها
وافع شود از کرما و سرما و باران و میغ درآن
ماهبا نیز چنان بود ۰ وجمعی گویند روز اول‌آن
دلیل ماهی اننخ. که ]فتاب در مرج اسد باشت
و روز دوم درستبله و همچنین تا بحوت که‌هشتم
ای برحکم مذ کور ازباد و باران وامثال آن ۳ .
بخ « باخای نقطمدار بروزن شاخ »بمعنی
راه باشد که عربان طریق گویند .
ماه وشدت گرماست «قطرالمحط».
«قطرالمحیط» .۰ ۴ - دراوستا 202764872 :ا 2020001020072 «معنی‌شمال آمده وآنجا جایگاه
اهر یمن و دیوان و مکان درزخ دانسته شده « خرده اوستا ۸۷ ح ۲ » . در پپلوی نبز کق2021
آمده بدین همنی و نیز بمعنی سیاره « منای ۷۹۹ : ۲ * در زبان فارسی اکثر بسعنی هفرب
آمده در پرابر خاور ؛ ولیگاه نیز بمکس, باختر بمعنی مشرق و خاور بمعنی هغرب استعمال شدم:
چو قهر آورد سوی خاورکریغ هم از باختر برزند بازتیغ . عنصری باخی.
بقیه ازصفحة ۲۰۳
٩‏ - درفرکی بمعتی قوی , مخت هجفتابی ۱6۵*- باتو پسر جوجی خان پسس چنگیزخان که در
قوربلتای سال 14۲ ۶ بهمراه یکیو که ومنگو مأمور تسخیرهمالك دوس و چرکس وبلغار کردید
و او بادشاه دشت قبچاق بود وبعدها وی منگو را بمقام خانی بررگزید . رك : فهرست تاربخ مفول
بقلم آ قای اقبال وداثرةالمعارف اسلام. ‏ ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی
از ریشه 08 پارسی‌بامتان مشتق است «مزدیسنا ۵4-۲۵۳ » وآن از ريشة 2 اوستایی بمعنی
بخش کردن وقسمت کردن‌است . ٩‏ - باح وبا وباز وواج و واژ باین‌معنی ازريشة اوستابی ۷۵6
( گفتن)» سان‌کریت ۷۵6 ۰ درپهلوی [۷2 با ۷۵8 ۰ درلاتینی ۷۵۴ , درفرانه ۷۵۷۴ » در
انگلیسی ۷۵۱6۶ . باژ بممنی کلمه و سخن و گفتار است . کليةٌ دعا های مختصر راکه زرتشتیان
آهته بزبان میرانند باژ گویند :
پرستندة آذر زردهشت. همی‌رفت باباژ و برسم بمشت . فردوسی‌طوسی «مزدیسنا۲۵۳ببمد»
اجثاق _ ترکی, دومردراکه دو خواهررا درازدواج دارند نبت‌بهم باجناق گویند .
«جنتایی 4۱40
```


## [2026-09-04T22:46:38.608Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(295,325):\n    m=re.findall(r'صفح[هة]?ٌ?\\s*[۰-۹\\d]+', pages[i])\n    print(i, m[:4], pages[i][:60].replace('\\n',' '))\nEOF",
 "description": "calibrate BQT vol1 pages"
}
```


### [2026-09-04T22:46:40.683Z] TOOL RESULT

```
295 [] کت آیرویز نحتانی مجهول و واو » بسعنی آبی باشد و آن ا ییون « 
296 [] بچهُ با رسیده را گویند که از شکم ۱ و حبوان دمگر بیفتد . اپرن
297 ['صفحهٌ ۸٩'] ی سس اعشی وسکون ثانی و جیم . میواست که آنرا خاوسی «تریج» اگو
298 [] «سیخول» نیز کوبند . ۶ آقوت » با تای قرشت بر وز نکبود . بلغت‌
299 [] بگبترا جمیم جانوران موذی بگریزند - و شرارژ آتش را نیز کفته‌ا
300 [] ست و 4 سب #احر یض « بکر اول و دای بی نقطه و سکون ثانی وتحتان
301 [] « ری الافی » خوانند ؛ و بجای بای بجد بای اخت - حم اول وسکون 
302 [] وخواهر زاده را گونند . اخروش « با رای فرخت بر وزن خر اخ‌تفی 
303 [] «کراث الک رکم » خوانند . اخسمه - بفتح اول وسکون انی و شم سین
304 [] اخی» بر وزن مفی ؛ کاری و چیزی‌را کوبندکه قابل تین باشد - وصا
305 [] و تشنگی را فرو نشاند - و بفتح اول ‏ و کسرثالث در غربی اهر بد
306 [] -9-- درودگری باشد . ومضفقف اکر هم هست که‌آن کلمةٌ حرط است - 
307 ['صفحهٌ ٩۸'] ی "ار پیاسیوس - با تحتانی و سین بی نقطه و تحتالی دبکر بروزن 
308 ['صفحهٌ ٩۷'] ارجالون کثتاس را در جنگه کشته بود و لهراسب پدر کتتاس راکه تر
309 ['صفحةٌ ۷۰۰'] خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است وتا کردة او
310 ['صفحه ٩٩'] اردشیران " قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسان این همن 
311 [] آردسهشت او س باکاف‌فارسی بروزن‌پهلوان, بمعئی اردجان است و ها
312 ['صفحه ۱۶۱'] بخشایش » بمعنی خیر و خیرات و چیزی در راه خدا بمردم دادن باشد
313 [] مه موم ما ی > ج با کل فا درل مخرفا اردو
314 [] آردو ت برابر نا سس ۳ص اس ای دیس ۳۳ سذ الفبای ار دو ۳ کیت لا 
315 [] شراب است - و حبایی را نیز کوبند که بردوی شراب بهم رسد - و کو
316 [] لرسانیفون ارسانقون » با اك بالف کشیده و نون تحتانی رسیده و ف
317 [] وا ۱ ارغاب جمیم گزندکان بگرایزند و آرا ازطاعاسیا وار طمسا دز
318 [] ارغامونی ار غامو نی پامیم بر وزن افلاطونی؛ بلغت بونانی تباتی
319 ['صفحةٌ ۱۰۸'] سس سا مشهور که افلاطون وضع (۱) کرده است ؛» و ی گونند .ارغنون
320 ['صفحهٌ ۱۰۷'] ار که واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛ و باین مع
321 [] سب ۱۰۵ تت ضحاك می فرمود بکشند و مغز سرایشالرا بجهت مارالی که
322 [] ارمند زلایتی‌است از کوهستان آنربابجان و مولدشیرین مشهور آبجا
323 [] از یا وجیم. , بمعنی آرنج است ت که بندگاه ساعد وبازو باشد وبح
324 ['صفحهٌ ۱٩۱۱'] ارء جان اره‌جان با ثاتی‌هشدد و جیم بروزن پهلوان » نام شهری ا
```


## [2026-09-04T22:47:08.256Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[301][-1200:])\nEOF",
 "description": "tail of BQT axtar page"
}
```


### [2026-09-04T22:47:10.297Z] TOOL RESULT

```
- و بعمتی‌فال
و شگون هم آمده است - و نلم فرشته ابست
مو کل کر زمین (۱)- و عم یکی از متازل قمر
کنابه از کوکب عطارد است - و کو کب‌مشتری
را نیز کویند .
اختر ستان - بکس رای م للم کتایی
است در علم هیأت و نجوم .
اختر شهر ه منج و نسوم دان را
اخترکاوبان
اخشر شهر ذن «کنابه از شب بیداری
باشد .
اختر شناس - بسنی‌اختر شمراست
که منجم و جوم دان باشد (۳) . *
اخمر او ان - با کاف و واو پروزن
ار شاهان , مخفف اختر کاوبان است ت که نام
علم افربدون (4) باشد . د آن از کاوة آهنگی
بود ویادشاهان عجم بعدازشکت ضحاك آنرا بر
خود شگون کرفته بودند ».و آن چرمی بود که
کاو؛ آهنگر بوقت کار کردن بر میان خود
طلمات بغایت عاهر» شکل صد در صدی برآن
هش کرده بود + وبستی کوبندشکلی ازسوختگی
های آش در آن چم بهم وسیده بود که این
خاصیت داشت » نی درهر جرد که آن‌همراه
ی شد و آنرا مرفم کرده بودند
ودر زمان حرت رسالت یناه صلرات ال علیموآ له
(ه) بدست سلمانان اقاد وآنرا باره پاره کردند
و بر مسلمانان فسمت لمودند ۴ ,
اختر کاویان -
بروزنرهی غاز بان.
کوند . حىان اختر کاواست که علم فربدون باشد ۴ .
)۱( خم ۳ : که مو کل کر؛ زمین است )۱( خم ۳ : - است .
(۳ خم ۳ : را گوبند . (4) خم ۳ : فربدون . (ه) چك : صلمم .
۰ ولی صحیح‌اخیون است
/ - هر دو عری است
۲ ( ساره) « اونوالا ۳۳۰ >
۴ - هلوی 9186 ؛ منلی ۲۹۸ : ۲ *  ,‏
درفش کاوبانی برما واسح ات ۰
در روی لته سد
```


## [2026-09-04T22:47:30.621Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 500<i<560 and ('بلخش' in p or ('بلخ' in p and 'بدخشان' in p)):\n        print('LEAF',i)\n        print(p[:2600])\n        print('=====')\nEOF",
 "description": "BQT balkh entry"
}
```


### [2026-09-04T22:47:32.814Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T22:47:36.938Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nhits=[i for i,p in enumerate(pages) if 'بلخش' in p]\nprint('balaxsh leaves',hits)\nhits2=[i for i,p in enumerate(pages) if 'بدخشان' in p]\nprint('badaxshan leaves',hits2[:20])\nEOF",
 "description": "locate balakhsh in BQT v1"
}
```


### [2026-09-04T22:47:38.945Z] TOOL RESULT

```
balaxsh leaves [463, 660]
badaxshan leaves [32, 113, 324, 387, 462, 463, 747]
```


## [2026-09-04T22:47:42.415Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (462,463):\n    print('LEAF',i)\n    print(pages[i][:3000])\n    print('=====')\nEOF",
 "description": "BQT badakhshan/balakhsh page"
}
```


### [2026-09-04T22:47:44.075Z] TOOL RESULT

```
LEAF 462
بقتح اول و سکون تانی » نقیض
خوپ و نيكك باشد ٩‏ - وله ور کوی نیم سوخنه
راکوبندکه بجهت آتشگیره مه.ا کرده ماشتشب
و چم اول مخفف بود باشد - و بمعتی آن"
0 7711
با چضاق آش برآن زد - و بمشی صاحب
و خداوند عم آمده است ؟ - و خادم وخدمتکار
را نز کفتداید ۴ .
بف‌اختر - یفتحم همزه و تای قرشت
و سکون خای تقطمدار و رای بی‌نقطه ۰ بدطالع
و بدبخت و شوم راگوند .
۱ بداسقان - بختح اولو ثانی‌بالف کنیده
و سکون سن بی‌شطه و ال تقو یدود
زده » بیونانی حشیشی است کرم و خشك و آنرا
جرب ی کف‌ال خوانند ۴ .
)۱( چك : خشم" لود ۰
آواز ؛ دس بدسرشت و بدذات باشد .
بداق » بکس اودبروزن عراق .پاچة
قنبان و ازار و شلوار باشد .
بدا لگ ه پنتح‌اول بروزن‌هلاك. بداندیش
وخثمآ لوده (۱) را ود .
بد ید لش ٩‏ - با با و دال ابجد بی وزن
بلبلك , مرغ سلیمانرا کون دکه هدهد باشد .
ند سل تن مشکل ید را گوشد ۰
بد بور با بای فارسی بروزن‌مرموز »
برامون دهانرا گونند ازطرف برون ٩‏ .
بد خش - بفتح اول و انی و سکون‌خا
وشن حردو نقطهدار مخفف بدخشان اسمت ورجون
لمل از آنجا آرند لعل را نیز بدخش گویند»
و بدخشانی و بدخشی را هم بدخش کوباد ۷
بد حشای ۸ ‌‌ بروزن نمکدان +ولاشی
کیلکی و طنزی 984 . فریزندی و برنی 980 « ۵ . ۱ ص ۰۲۹۲ , شهمیرزادی 224 «2 .
۲ م۰۱۹۲ . ۴ و آن پسوندیست که باخر اسم ملحق شود » در اوستا ثافةم با نا
یمعتی مولی و صاحب در پهلوی 036 «اونوالا ۱۱۹ ۰ درفارسی بد (اصللا بقتح باء ک امروز بضم
تلفظ کتند) چون + سهیید » حویف » گهید بارید » هرید امزدسنا ٩۳۹64‏ . ۴ - بد (بم
اول) در کتب اسلامی بسنی بودا موصی آین بودایی‌هند ویمنی بت ویمعتی‌بتخانه آمده است .ره:
داگرتالمعارف انلام . ۰ ۴ - بدسفان » بدشنان, ۷۷ 600۷۵۱۷۷1۵5 «اشتتگاس»رأ: بدسفان.
و ۲- 4 ( پسوند پدید آورندة اسم از صوت ) ؛ در کیلکی
. این مرغ حرلغلب زبانها بآوازش نامیده میشود «ارمفان سال ۱۷ ش ۷ «کاف» بقلم
کسروی». . ۷ فش مت دز تقو ۲ - رك هو ۸ ما رکوارت
۵/۵( (279ع , 2۲8081221۲) گوید که بدخشان بمعنی «بلاد بذخش 00250هو
شه درسفحهٌ ۱:۳
=====
LEAF 463
- ۷۳
است مابن هندوستان و خراسان ۰ کوبند معدن
لءل و طلا در آنجا هست و گوسفند آنجا را از
غابت. بزر کی و قوت سوارشوند و باهای‌تر دك
تردد نمایشد » وبسنی کویندکان لمل آنجانیست
و چون از مدن بدانجا آدرند و فررشند بدان
شبب سوب مبدخشان شده است.
بدخش مذاب ه کنابه از امن
بدخشانو شراب لعل باشد .
بفدل « با دال ابجد بی وژن محفل »
ترسنده و و تاه را گوشد 4
ارام - با رای قرشت برزئن ام
بمعنی همیشه و مدام - و بمعنی خوش و خرم
و آراسته _وخرام - ومجلسدلکتا وجایآسایش
عموماً و اسب و استر سر کش راخصوماً ۲ .
پف‌درآن - بروزن‌کران , سبزه ورستنی
بود مانند ترب» وآن بفایت گنده و بدبوی باشد
و آراکندکیا نیز کوبند - و بدراننده را هم
کفتهاند - و بععنی دیگر ظاهر است که ران بد
باثد - و بکر اول و تشدید ثالث؛ معنی‌اینکار
را تمام کن و باره گردان ۴ .
۱ - باين معانی» رك: پدرام.
شونده » مشکل رام شوندم) .
فرح ی»*
پر ره س بکس اول و سکون تانی‌وشم
ثاات و فتح زای‌تقطمدار , طملمی وا گوند کمزله
کرده باشند و در رومالی بته بجابی برند , وبه
فتح ثالث نیز باینسمنی آمده است - و بقتح اول
و ثانی و رابع» بسمتی حصه و بهرمباشد ۴ .
در 48 - با قاف بروزن دغدغه » رهیر
و رهنمای را کوبند ۵ ۰ ك‌
درو ۵ « بر وزن بهبود » بمعتی سالم
و سلاحت بأشف وه بمعنی‌وداع هم‌اآهنه است 5
وبمعنی ترك هم هت که از وا کذاشتن و دست
پرداشتن از چیزی باشد ۷ .
ید ر ۵ بروزن‌صنره ,خر بطهاییر! گوشد
ازجامه و با کلیم با تیماج که طولان از خی
و در موبدالفضلا بهمین وزن آورده بمعنی‌درختی
که بار و میوه ندارد .
پد‌دی - ب‌وزن‌ابری ۰ بمعتی بدرمباشد
که خربطه زد و بول است .
بد ز هر مه بروزن خرزعره .کابه از
بشدل و ترسنده و واهمه‌یاك باشد .
۴ - رك: بدورم
9 - بدرقه » مأخون از نازی » رهب و رهنمل. پاسبان ونگهبان - پشت و پناء - می کب - مایمع
نب م گرم ی که پس ازشرب مسهل جپت اعانت وازدیاد عمل‌آن تدرجاً وشد - معتمد - و شکیبا
و صابر دنانمآلاطباء» » مبذرق » در عربی بمعنی دلیل و دیدبان است .
9 ماء کنعانی هن اهستف مصرآن توشد وفت آتست که بدرود کنیزندان وا. تحانط شیرازییه»
۲ - رك: پدرود - .
۵ بدر 8 محبت ‏ ورقمراسلة دوستانه «نلظم‌الاطباه».
بقه از مشحهً؟ ۷4"
با بلخش 0212:0510 است و آن نوعی است از باقوت که کویند جز دربدخشان » در ساحل نهر
ککجدت»0 بات نشود.» اماکاملایحتملاست که کلم باخش 021850( که‌کت فان کنعلعط
و انگلیسی کقاق(] از آن مأخوذ است) در آغاز نام ناحیت هورد بحث بوده و بسدها بلملی که حر
آن ناحت بافت شود اطلاق شده باشد . «بارتولد . دائرتالمعارف اسلام : بدخشان».
=====
```


## [2026-09-04T22:47:57.989Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(505,535):\n    seg=pages[i]\n    if 'بلخ' in seg:\n        print('LEAF',i,'printed~',i-224)\n        # print lines containing بلخ\n        for ln in seg.split('\\n'):\n            if 'بلخ' in ln: print('   ',ln[:160])\nEOF",
 "description": "find Balkh entry BQT"
}
```


### [2026-09-04T22:48:00.062Z] TOOL RESULT

```
LEAF 507 printed~ 283
    را گویند و بعریق جبلخوانند , ز بجای حرف
LEAF 517 printed~ 293
    بلخ هت بفتح آول وسکون ثانی وخای
LEAF 518 printed~ 294
    بلخور بشم اول بروژن پر زور ۰ هر
    پلغار ممروف است ۰ ناسررخسرو بلخ یکوید *
LEAF 519 printed~ 295
    بلخفتن ۱ ست که بمعنی جمم کردن و اندوختن
LEAF 530 printed~ 306
    زیرا که چنین‌دوات بدار درآعد.مولوی‌بلخی.
```


## [2026-09-04T22:48:03.289Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[517][:2200]); print('---TAIL---'); print(pages[517][-1400:])\nEOF",
 "description": "BQT Balkh page"
}
```


### [2026-09-04T22:48:05.407Z] TOOL RESULT

```
9ج
تاری ٩‏ , وآترا چون سبز باشد ولیم و جدال
خوانند ۰ و چون درغلاف باشدطلم کویند ؛رسنم
اول م‌ بنظی ففح است ۰
بلخ هت بفتح آول وسکون ثانی وخای
نتطهدار ۰ نام شهری است‌هشهور از خراسانوآن
از شهر های قدیم است همجو استخر فاریوآن
را فبةالاسلام خوانند ولفبآن بامی است. گویند
برامکه از آنجا بودمائد و مقتوح العنوه هت
و کدوبی را نیز گویند که شراب دران کنند .
بلحج با جیم فارسی بر وزن اعرج ؛
زاج سیاء را گویند که قلا باشد , و بفتح اول
و نانی هم بنظر آمده است
"لاتم - پروزن شلف ی
و دو رسمان فان یگذرانشد ‏ و شاطران
و شانان بدان سنکه اندازند . ۴
تلد ه ه با دال ابجد و حای هوزوح رکت
بلس ۹ ۷7۷
در فرهنگگ جپانگیری نام غله‌امت که از آن
هربسه بزند و دز آشها نز کنند و بعر یی عذص
خوانتد ۰ ودرسحاح‌الادوبه بمعتی تین ایض آمده
است که انجیرسفید باشد» و بلسن با زبادتی‌نون
بلسان.؟ بروزن سرطان » نام درختی
است مشهور درمصر . گوبند بمد. از طاوع‌شمری
نثتری که از آهن ساخته باشند بر ب رکث آن
بلعك
درخت فرو برند روغن از آن‌روان شود؛ با ینبه
جمم کنند» و بسنی کویند
شیشها در بر هرب رک یکه
نشتر زده اند بیاویز ند .
امتحان وی چنان ات 6
قطره‌ای برشیر کاو چکانند
بلسان بعد از لمحه‌ای مانتد دلمةٌ
پثیر سته شود » و بر آب چکانند و برهم زنتد
آب ماند هر نقنه گرد , و آنرا بعربی
دهن‌البلسان خوانند ؛ و موضعی که درخت بلان
آ»جاست باغ فرعون بوده است وا نرا عین‌الشمس
خواند؛و کوبند ازممجزء عیسی علیه‌السللام است؛
و تخم آنرا حب‌البلسان کوبند. گرم و خشك
است‌در دویم. کوفت رعشهرا نافع‌است» وبیدانجیر
نیز گفته‌اند .
بلساك . بکر اول و انی و سکون
ثالت و کاف » سیخ آهنی باشد که یکی آنرا
پپن کرده باشند برای نان از تنور جدا کردن -
و سیخ کباب را نیز گوبند - و پفتح اول و انی
پرستوك‌باشد وآنر! بمربی‌خطاف گونند ۵ ونم
اول و نانی چوبی باشد با سی خگنده‌ای که بدان
بربان در تنور آویز ند .
بلسی - نم اول و ثالك و سکون تا
ونون » غله‌ایرا وین دکه‌بعربی عدس‌خوانند ٩‏
پلشاث « ینم اول و ثالی و سکون شبن
قرشت و کاف ؛ بمعنی آخر بلسك است که‌چوی
با سیخ کنده ای باشد که بدان بریان در تنور
آوی ند ۰
‌- هلر ی 13۳ 1 4 0 آرهنی
۲س ۵۳
نیز بلس‌درخثی
- بونانی 021521000 <
(عطروطیب) «نفس؛ .
‌ بلدر چیی - رگ : ور
وه مش :
---TAIL---
 با دال ابجد و حای هوزوح رکت
بلس ۹ ۷7۷
در فرهنگگ جپانگیری نام غله‌امت که از آن
هربسه بزند و دز آشها نز کنند و بعر یی عذص
خوانتد ۰ ودرسحاح‌الادوبه بمعتی تین ایض آمده
است که انجیرسفید باشد» و بلسن با زبادتی‌نون
بلسان.؟ بروزن سرطان » نام درختی
است مشهور درمصر . گوبند بمد. از طاوع‌شمری
نثتری که از آهن ساخته باشند بر ب رکث آن
بلعك
درخت فرو برند روغن از آن‌روان شود؛ با ینبه
جمم کنند» و بسنی کویند
شیشها در بر هرب رک یکه
نشتر زده اند بیاویز ند .
امتحان وی چنان ات 6
قطره‌ای برشیر کاو چکانند
بلسان بعد از لمحه‌ای مانتد دلمةٌ
پثیر سته شود » و بر آب چکانند و برهم زنتد
آب ماند هر نقنه گرد , و آنرا بعربی
دهن‌البلسان خوانند ؛ و موضعی که درخت بلان
آ»جاست باغ فرعون بوده است وا نرا عین‌الشمس
خواند؛و کوبند ازممجزء عیسی علیه‌السللام است؛
و تخم آنرا حب‌البلسان کوبند. گرم و خشك
است‌در دویم. کوفت رعشهرا نافع‌است» وبیدانجیر
نیز گفته‌اند .
بلساك . بکر اول و انی و سکون
ثالت و کاف » سیخ آهنی باشد که یکی آنرا
پپن کرده باشند برای نان از تنور جدا کردن -
و سیخ کباب را نیز گوبند - و پفتح اول و انی
پرستوك‌باشد وآنر! بمربی‌خطاف گونند ۵ ونم
اول و نانی چوبی باشد با سی خگنده‌ای که بدان
بربان در تنور آویز ند .
بلسی - نم اول و ثالك و سکون تا
ونون » غله‌ایرا وین دکه‌بعربی عدس‌خوانند ٩‏
پلشاث « ینم اول و ثالی و سکون شبن
قرشت و کاف ؛ بمعنی آخر بلسك است که‌چوی
با سیخ کنده ای باشد که بدان بریان در تنور
آوی ند ۰
‌- هلر ی 13۳ 1 4 0 آرهنی
۲س ۵۳
نیز بلس‌درخثی
- بونانی 021521000 <
(عطروطیب) «نفس؛ .
‌ بلدر چیی - رگ : ور
وه مش :
```


## [2026-09-04T22:48:15.827Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'باختر' in p and i<120:\n        print('LEAF',i)\n        print(p[:1800]); print('====')\nEOF",
 "description": "Noushin bāxtar"
}
```


### [2026-09-04T22:48:17.661Z] TOOL RESULT

```
485
LEAF 73
                                          ‫‪۷.‬‬                                         ‫بابزن‬


 ‫([شمال ]»‪( .‬مارکوارت‪ .‬ایرانشهر‬   ‫‪۲‬‬            ‫(باب در این بیت پدر گیو است و گیو پدر‬
                        ‫‪(AF FV‬‬     ‫‏‪۷‬‬                                       ‫بیژن است)‬
     ‫در تاریخ سیستان نیز چنین آمده است‪:‬‬                                             ‫‪ .‬بایزن‬
‫«هر چه حد شمالست باختر گویند و هر‬                                           ‫سیخ کباب‪:‬‬

 ‫چه حد جنوبست نیمروز گویند و میانه‬                       ‫بسزد نیزه بر بند درع و زره‬
 ‫اندر بدو قسمت شود هر چه حد‬                     ‫زره را ن‌ماند ايچ بند وگره‬
 ‫مشرقست خراسان گویند هور چه حد‬                            ‫ز زینش جداکرد و برداشتش‬
                     ‫مغربست ایرانشهر»‬            ‫گراشتش‬
                                                      ‫چو بر بابزن مرغ» ب‬
 ‫سخنوران پیشین گاه باختر را به معنی‬            ‫‏)‪(VAT-114-1‬‬
  ‫ور رابه‌معنی مغرب آورده‌اند‪:‬‬ ‫او‬‫خرق‬
                                   ‫مش‬                  ‫از اسدی ( گرشاسب‌نامه ‪:)۷۱۲-۷۱‬‬
 ‫رودکی خراسان را به معنی مشرق‬                                 ‫بر آن آهنی نیزة یل فکنن‬
‫[چنانکه در زبان پهلوی نیز چنین است] و‬           ‫زد آگنور چون مرغ بر بابزن‬
     ‫خاور را بهمعنی مغرب بکار می‌برد‪.‬‬              ‫از فخر گرگانی (ویس و رامین ‪:)۴۶-۲۸‬‬
                 ‫(نفیسی بیت ‪:)۹۲۸-۰۲۸‬‬                       ‫سنان نیزهگفتی بابزن بود‬
      ‫مهر دیدم بامدادان چون بتافت‬              ‫بروبر مرغگرد تیغزن بود‬
 ‫اخزراسان سوی خاور می‌شتافت‬                                                         ‫بابک‬
      ‫نیم روزان بر سر ما برگذشت‬                ‫مرکب از باب [‪:‬پدر] ‪+‬ک [‪:‬نشانه تصغیر ]‪:‬‬
‫چون به حاور شد زمانادید گشت‬                                                      ‫پدرک‪:‬‬

 ‫تک ن رای نه
====
LEAF 74
‫ب(ایداد) افراه‬                                      ‫‪۷‬‬

                     ‫از فخر گرگانی (‪:)۸۷-۱۲‬‬             ‫و‬      ‫(‪۴-۸۶۱-۴۳۸‬‬         ‫شاهامه‬        ‫از‬
                 ‫تو این پیوند نو را باد می‌دار‬                                        ‫‪:)۵-۵۸۲-۲۳۸‬‬
‫همیدون دل از آن پیوند بردار‬                                      ‫چو خورشید تابان ز گنبد بگشت‬
                   ‫ی‪۴‬ہت ‪:)۷‬‬
                          ‫از حافظ (غزل ‪۲‬‬                    ‫ز بالا همی سوی خاور گذشت‬
  ‫مقاتونی شد‬
           ‫للتیعش‬
                ‫حافظ اسزدو‬                                    ‫شب تیره با لشکر افراسیاب‬
‫یعنی‌از وصل تواش نیست بجز بادبه دست‬                     ‫گذر کرد از آموی و بگذاشت آب‬
     ‫‪-۲‬آه (بهبادسرد‪ .‬سردباد نگاه کنید)‪:‬‬                          ‫سپیده چو از باختر بسردمید‬
       ‫چگوشتاسب امد بدان شارستان‬                         ‫طلایه سپه را به هامون ندید‪.‬‬
‫همی جست جای یکی کارستان‬                                 ‫از اسدی ( شگارسب‌نامه ‪٩۵ ۷۰۳-۷۵‬‏ و‬
       ‫گررد روم‬
              ‫همی گشت یک هفته ب‬                                                          ‫‪:)4-۹۵‬‬

 ‫همی کار جست اندر آباد بوم‬                                       ‫از آنجایگه رفت خرم روان‬
       ‫چو چیزی که بودش بخورد و بداد‬                     ‫به پیش آمدش ژرف رودی روان‬
‫همی رفت ناشاد و دل پر زباد‬                                    ‫چو خور برکشیدی به خاور فرود‬
‫)‪(۶-۷1-10‬‬                                               ‫سوی باختر رفتی آن ژرف رود‬
                                           ‫بادات‬                 ‫چو از باختر باز بسرتافتی‬
‫آرزومندی و‬           ‫ف‬
                     ‫ل‪+‬‬‫اشد]‬
                          ‫مرکب از باد [‪ :‬با‬              ‫سوی خساور آن آب بشتافتی‬
         ‫دعا ‪+‬ت ضمیر مفعولی‪ :‬باشد ترا‪:‬‬                         ‫چ
====
LEAF 99
                                                                                   ‫برع‬


      ‫‪ ...‬چو برزد سر از برج خرچنگ ماه‬             ‫بدان بسرترین نام یزدان پاک‬
‫(‪)۴-۵۸۲-۸۶۱۱‬‬                                ‫برهخشنده خورشید و برتیره خاک‬
                     ‫گواه چنگ خرچنگ‪:‬‬        ‫)‪(1-۶4-4۷‬‬
  ‫چو برزد سر ازچنگ خرچنگ هور‬               ‫دتررجمه تفیسر طبری ص ‪۱۱‬و ‪۷۹‬با‬
‫جهان شدپراز جنگ و آهنگ و شور‬                 ‫یمن» آمدهاست‪.‬‬ ‫رنا‬
                                                             ‫تن»‬
                                                               ‫گمهی‬
                                                                  ‫رنام‬
                                                                     ‫زت «‬
                                                                        ‫بارا‬
                                                                           ‫عب‬
‫(‪)۵-۹۷۲-۲۲۷‬‬                                                  ‫وکون درم)‬
                                                                     ‫برج (باپیش اول س‬
                                ‫برج خوشه‬   ‫شکل یاچند گوش که بر‬        ‫ودانه‬
                                                                          ‫باناسیبتلن‬
                  ‫به واژة چرخ نگاهکنید‪:‬‬                              ‫دیوار دژ سازند‪:‬‬
               ‫نوشه بی‬   ‫دتوی؛‬
                             ‫بگدورگف‬                 ‫به دیوار عراده بر پای کرد‬
‫چو ناهید در برح خوشه بدٍی‬                   ‫به برج اندرون رزم را جای کرد‬
‫(پرویز ‪)۸۳۹۲‬‬                                 ‫)‪(0-441-۷1‬‬
                                ‫برج شیر‬
                                                                                ‫برجای‬
                ‫به واژة چرخ نگاه کنید‪:‬‬
                             
====
```


## [2026-09-04T22:48:28.931Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls; awk 'BEGIN{RS=\"\\f\"} /pdf page 8[6-8]\\]/' FFD_pages_faseng.txt 2>/dev/null | head -80 || awk 'BEGIN{RS=\"\\f\"} NR>=86 && NR<=88' FFD_pages.txt | head -80",
 "description": "FFD page 82"
}
```


### [2026-09-04T22:48:31.108Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
```


## [2026-09-04T22:48:34.472Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"pdf page 8[5-9]\\]\" FFD_pages.txt | head; echo ---; awk 'BEGIN{RS=\"\\f\"} /pdf page 87\\]/' FFD_pages.txt | head -70",
 "description": "FFD printed p.82"
}
```


### [2026-09-04T22:48:36.681Z] TOOL RESULT

```
2155:[pdf page 85]
2181:[pdf page 86]
2212:[pdf page 87]
2223:[pdf page 88]
2242:[pdf page 89]
---
[pdf page 87]
فعلهای فارسی دری
یافتن
یافت < فارسی میانه 27311 < ایرانی باستان ۵1-3۳4۵*. برای 12 > آراست. 21
: پیشوند فعلی است. ريشةٌ 22 به معنی «به دس تآوردن» است.
یاب < فارسی میانه 2730 < ایرانی باستان ۵01-30-8*. برای 2 -> آرای.
بشترد
پشت + فارسی میانه 181 < ایرانی باستان 9۵3-12*. برای 12 -» آراست. 7صورت
اصلی 28 است. * پیش از ۲ به 5 بدل شده است. ريشهٌ 727 به معنی «ستودن» است,
«یشتن» از واژه‌های «زند و پازند» است. مادةٌ مضارع آن در فارسی میانه 22 است»
از ایرانی باستان 922-8. برای 2 + آرای,
```


## [2026-09-04T22:48:45.901Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apam\\|apām\\|ap'am\\|'p'm\" SNS.txt | head -20; echo \"--- pages file\"; grep -n \"apam\\|ayaf\\|ayāf\" SNS_pages.txt | head -20",
 "description": "SNS lookup"
}
```


### [2026-09-04T22:48:45.964Z] TOOL RESULT

```
3136:{GNPE. '•&&) ULiVb. 80-81) *apat9ma, apama : L_ 
--- pages file
1843:                                                                                                {GNPE.    '•&&) ULiVb. 80-81) *apat9ma, apama                                                                 :   L_
16544:ahen   I   vidaxtag 34/21   asantar 30/9                           ayaft 84/1                abaz kun 223/23
```


## [2026-09-04T22:48:51.062Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1820,1870p' SNS_pages.txt; echo \"=== leaf?\"; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:1843])\nprint('leaf',pre.count('\\f'))\nEOF",
 "description": "SNS context"
}
```


### [2026-09-04T22:48:53.179Z] TOOL RESULT

```
                                                                                                 \t*
     _vv-if-ia/vY ^ .Tv-rr-u/i<>«*                           it/a^ -a/r^.ii, is.)                           r/i   f* [J^J^oy -.«*) .^ (jtijil ^:                      aburnay: JS, «>
                                                           -a/To^ -T«>/ir^ -ro-T^-T^
16   •   (*&&•) awlr-tar             :   ^ -j^w «j3j(o :ab§rtar:                         ^^o*              l.^.fl-Ao/T <*(*-**)*!» <**, I* :aburnayIg:^J>
                                                                                                                                                          lC,
                                                                                                                                                          .


                                                      •   A/To»5 .r«/ir**' -n-ivu ^
                                                                                                                                                                     IT/IT «5    1/6^           IA
                                                                                                                                •A/Y ^     .iH,«jl3     ;jj   :   aburnay Ig:^^!^
                          it/H*S -t^-'j'^'j^abSrahlh:                                            -\
                                                                                         -*u-o
                                                                                                           -rr/YT^        t9W»:<&         u^   .^b..^ tooiT             :   afrin:     Kie^
         mOzag +tf, ab§         -*i**b «j^oj->* -*i>\*                       :ab§mOzag: 4«.
                                                                                                                                               ^^^J^^'^'^l :ab§- say
                                                                                                           (Pere.       Stud.   33)   aw:        V *apaiy:^ apa+ id              :   U
     TY                                            iBMvUtelMjlj                                                                                 .L^^-^L^L.jij                                                           Y*



                                                                                                                                   .    (.U^i^-       .
                                                                                                                                                          >f   <   (•Jjl   :   abdum/dfdurn:                        ^v^
                                                                                                {GNPE.    '•&&) ULiVb. 80-81) *apat9ma, apama                                                                 :   L_

      .   jyjjA^ipT.j^j^T :5tal                     I   Ohrmazd:              ^k^   -            awadum             ^   (Mir. Man. 11,44) bdwm: .^li 9-10)
       o—ljj-Ji* j «xl «.ij.-i J j*/* j-* <d*sT , jjT        L-jl 3 uiiJjj^t^c/l^jljJ                               •Y/A^ -An/Y^ ,/y-> ei/; f oil ^jU/jj**^


6                    VT-VT/16'* -1V/VT **          (^vlUu' -V^'Tc                       **-*    ji^^» :^Sj) «bS vinah                      +rf*           ab§ .•b^ :abevinah:                                 ^^mv               a

       -o-Ji* xxj&j*          'fWir3* :3tas I vahram: -S^-^um- -u^y**
                                                                                                          .ft/UiS .^Ab^- :abSvinah!h:                                                         -o-o-»»*o'


     u^ T 63 /- .cJ^jljjaT :3tas I vazist:
             ,
                 l                                                      v?-kjj^' w^*»aj'         :^ Utr. Man.                II,           44)            ->gr        zjsL<j\ agar:>*                        HT:         y*>*

                                                                                                                    .>T6-rA-n-U/T^ .(**>&*) agar
                                                                                                     •Y/&^ -H/T** -YA/Y^ ./1j-j*ijSI :agar-iz: <.*>"                                                                            ) s


                                                                    •   Y*/ir^    (o^y^                                                                                                                   T7VT**


                                                                                                     JjlJ-.-j^i) s +Jri agar.ljjIjSKoijJI :agar-s: J°>2>
                                                                                                                                                                                                                    '



=== leaf?
leaf 29
```


## [2026-09-04T22:49:09.493Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(26,34):\n    p=pages[i]\n    for m in re.finditer(r'\\b(a[pwbv][aā]m\\w*|ap[- ]|ayaf\\w*|ayab\\w*)', p):\n        print(i, repr(p[max(0,m.start()-90):m.end()+90].replace('\\n',' ')))\nEOF",
 "description": "SNS search apam"
}
```


### [2026-09-04T22:49:11.437Z] TOOL RESULT

```
29 "                                                  {GNPE.    '•&&) ULiVb. 80-81) *apat9ma, apama                                                                 :   L_        .   jyjjA^i"
```


## [2026-09-04T22:49:19.323Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb && sed -n '1,60p' tools/ref_page.py",
 "description": "inspect ref_page.py"
}
```


### [2026-09-04T22:49:21.500Z] TOOL RESULT

```
Exit code 2
sed: can't read tools/ref_page.py: No such file or directory
```


## [2026-09-04T22:49:23.747Z] TOOL CALL #51: Bash

```json
{
 "command": "ls tools/ | head -40",
 "description": "list tools"
}
```


### [2026-09-04T22:49:23.786Z] TOOL RESULT

```
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
```


## [2026-09-04T22:49:32.204Z] TOOL CALL #52: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T22:49:32.211Z] TOOL RESULT

```


```


## [2026-09-04T22:49:37.497Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ep-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derived terms/descendants (Latin, Avestan, Sanskrit, Hittite). Quote the gloss exactly."
}
```


## [2026-09-04T22:49:38.458Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%A7%D9%85",
 "prompt": "Persian وام: give the full etymology section verbatim — Middle Persian form, Proto-Iranian reconstruction, any cited scholars (Cheung, Hasandust, MacKenzie), and the meaning."
}
```


### [2026-09-04T22:49:43.804Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁ep-

**Reconstructed Root:** *h₁ep-

**Meaning:** "to grab, snatch, get"

## Derived Terms and Descendants:

**Latin:**
- apiō (from *h₁p-i-)
- apīscor ("to seize, get, obtain")
- coēpī (from reduplicated perfect *h₁e-h₁óp-e)

**Hittite:**
- 𒂊𒅁𒍣 (e-ep-zi, "seizes")
- 𒉺𒀀𒄿 (pa-a-i, "gives, hands over, pays")

**Sanskrit:**
- आप् (āp) - direct descendant
- आप (ā́pa) - from reduplicated perfect
- आपयति (āpayati) - causative form

**Avestan:**
- āpa (from reduplicated perfect)
- apaiieiti (causative form)
```


### [2026-09-04T22:49:44.624Z] TOOL RESULT

```
# Etymology of Persian وام (wām)

Based on the Wiktionary entry, here is the complete etymology section:

The word وام derives from an earlier form آوام (āwām/âvâm), which was inherited from Middle Persian. The Middle Persian form is cited as **ʾpʾm** (abām), meaning "loan, debt." A related Parthian form ʾbʾmyh is also noted for comparison.

The entry references **D. N. MacKenzie's** *A Concise Pahlavi Dictionary* (1971) as the scholarly source for this etymology. However, the Wiktionary article does not include a Proto-Iranian reconstruction. The Middle Persian form itself requires Book Pahlavi script notation, which the entry flags as incomplete ("Book Pahlavi needed").
```


## [2026-09-04T22:49:49.744Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D9%81%D8%AA%D9%86",
 "prompt": "Persian یافتن: give the etymology verbatim — Middle Persian form, Proto-Iranian root, PIE root, cited sources."
}
```


## [2026-09-04T22:49:51.637Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%B1",
 "prompt": "Persian اختر (axtar): give the etymology verbatim — Middle Persian form, any Proto-Iranian reconstruction, cited sources (Hasandust, MacKenzie, Nyberg), and the meanings."
}
```


### [2026-09-04T22:49:55.828Z] TOOL RESULT

```
# Etymology of Persian یافتن (yāftan)

**Middle Persian form:** The entry notes "[script needed]" for the Middle Persian form 'y'ptn' (/⁠ayāftan⁠/)

**Proto-Iranian root:** Composed of two elements:
- Prefix: *Habí
- Root: *Hap- ("to reach, attain")

**Proto-Indo-European root:** *h₁ep- ("to take, seize, grab")

**Etymology chain:** The prefix derives from Proto-Indo-Iranian *Habʰí ("to, against, for"), while the root traces back to the PIE *h₁ep- element meaning "to take, seize, grab."

**Source cited:** Cheung, Johnny (2007), *Etymological Dictionary of the Iranian Verb* (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, pages 161-3
```


### [2026-09-04T22:49:57.906Z] TOOL RESULT

```
# Etymology of Persian اختر (axtar)

**Middle Persian Form:**
The word derives from Middle Persian 𐭠𐭧𐭲𐭫 (ʾhtl /⁠axtar⁠/).

**Origin:**
According to the source, this Middle Persian term represents "an ancient backformation from 𐭠𐭯𐭠𐭧𐭲𐭫 (ʾpʾhtl /⁠abāxtar⁠/, 'planet')." The backformation occurred "due to a mistaken folk etymology that the first element ab- was a negative suffix, since Zoroastrianism considers the planets to be nefarious 'un-stars' due to their astronomically odd behavior."

**Cited Source:**
Eilers, W. (30 December 2012), "AXTAR," in *Encyclopædia Iranica*, volume III/2, page 123.

**Proto-Iranian Reconstruction:**
The document does not provide an explicit Proto-Iranian reconstruction for this word.

**Meaning:**
In Persian, اختر (axtar) denotes a "star" in astronomical contexts or literary usage, and figuratively means "fortune" or "luck."
```


## [2026-09-04T22:50:03.740Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/axtar-mid",
 "prompt": "Quote what this article says about axtar 'star', its relation to abāxtar 'planet/north', and the Avestan background."
}
```


## [2026-09-04T22:50:04.799Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AE%D8%AA%D8%B1",
 "prompt": "Persian باختر: give the etymology verbatim — Middle Persian abāxtar, Avestan apāxtara-, meanings (north/west), cited sources."
}
```


### [2026-09-04T22:50:06.139Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T22:50:11.464Z] TOOL RESULT

```
# Etymology of Persian باختر (Bāxtar)

**Middle Persian Origin:**
"Inherited from Middle Persian (ʾp̄ʾhtl /⁠abāxtar⁠/, 'north')" according to the Wiktionary entry.

**Avestan Derivation:**
The term traces to Avestan *apāxtara*, meaning "north; direction of the daevas, direction of Ahriman, direction of Hell."

**Proto-Language Ancestry:**
This derives from Old Iranian *\*apāxtara* ("retrograde, backward-turning"), ultimately rooted in Proto-Indo-European *\*h₂epo-tm̥mo-*, stemming from the preposition *\*apa* ("behind").

**Modern Meaning Shift:**
Interestingly, while the historical sense denoted "north," in contemporary Persian باختر primarily means "the west," with the northern meaning marked as obsolete. The Urdu cognate preserves both directional meanings plus geographical references to Khorasan and Bactria.
```


## [2026-09-04T22:50:23.051Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/balas",
 "prompt": "Give the full etymology of \"balas\" (balas ruby) verbatim: Old French, Medieval Latin, Arabic, Persian forms and the place name."
}
```


## [2026-09-04T22:50:24.347Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/apt",
 "prompt": "Give the full etymology of \"apt\" verbatim, including the Latin apere/aptus and the PIE root; also list related entries mentioned (adapt, adept, inept, apex, attitude, couple) if shown."
}
```


### [2026-09-04T22:50:28.444Z] TOOL RESULT

```
I appreciate your request, but the webpage content provided doesn't include detailed etymology information for "balas" or "balas ruby." The page shows only the Etymonline website's header, navigation, footer, and general structural elements—it doesn't contain the actual dictionary entry you're asking about.

To find the full etymology of "balas" including the Old French, Medieval Latin, Arabic, Persian forms and place name origins, you would need to:

1. Visit etymonline.com directly
2. Search for "balas" in their dictionary
3. View the complete entry with all etymological details

If you can provide the actual dictionary entry content from Etymonline, I'd be happy to extract and format the etymology according to your specifications.
```


### [2026-09-04T22:50:31.807Z] TOOL RESULT

```
# Etymology of "Apt"

## Full Etymology

The word "apt" originates from mid-14c. English, derived from Old French *ate* ("fitting, suitable, appropriate") or directly from Latin *aptus* ("fit, suited, proper, appropriate"). The Latin term represents "the adjectival use of past participle of *\*apere* 'to attach, join, tie to.'"

This reconstructed Latin root traces back to the PIE root *\*ap-* (1), meaning "to grasp, take, reach," which also produced Sanskrit *apnoti* ("he reaches"), Latin *apisci* ("to reach after, attain"), and Hittite *epmi* ("I seize").

## Related Entries Listed

The page references these etymologically connected words:

- **Adapt** – from Latin *adaptare* ("adjust, fit to")
- **Adept** – from Latin *adeptus* ("having reached or attained")
- **Apex** – plausibly related to *apere* ("to fasten, fix")
- **Inept** – implicitly related through the *apt* root
- **Aptitude, Aptly, Aptness** – derivative forms

Note: The page does not mention "attitude" or "couple" in connection with "apt."
```


## [2026-09-04T22:50:36.677Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/balas",
 "prompt": "English \"balas\" (balas ruby): give the etymology verbatim — Middle English, Old French balais, Medieval Latin, Arabic balaxš, Persian Badaxšān/Balaxš."
}
```


## [2026-09-04T22:50:37.394Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/couple",
 "prompt": "Give the full etymology of \"couple\" verbatim: Old French cople, Latin copula, and the *co-apere analysis. Also, if the page mentions \"attitude\", give that too."
}
```


### [2026-09-04T22:50:43.450Z] TOOL RESULT

```
# Etymology of "Couple"

Based on the page content, here is the etymological chain:

**Noun Form (late 13c.):**
"from Old French _cople_ 'married couple, lovers' (12c., Modern French _couple_), from Latin _copula_ 'tie, connection,' from PIE _\*ko-ap-_, from _\*ko(m)-_ 'together' + _\*ap-_ 'to take, reach.'"

**Verb Form (c. 1200):**
"from Old French _copler_ 'to couple, join together,' from _cople_" with meanings evolving from linking/connecting to marriage and sexual relations.

**Note on "attitude":**
The page does not mention "attitude" anywhere in its content.
```


### [2026-09-04T22:50:43.466Z] TOOL RESULT

```
# Etymology of "Balas"

The word "balas" has a fascinating etymological journey through multiple languages:

**English Origin Path:**
The English term derives from "Old English _bales_, _balais_" → "Old French _balais_" → "Arabic _بَلَخْش_ (balaḵš)" → "Persian _بلخش_ (balaxš)," which connects to "Persian _بدخشان_ (badaxšân, '[Badakhshan](https://en.wikipedia.org/wiki/Badakhshan)')," the geographical region where these gemstones originate.

**Meaning:**
In English, "balas" refers to "a type of rose-coloured [spinel](/wiki/spinel 'spinel') once thought to be a form of [ruby](/wiki/ruby 'ruby')." The term is now primarily used as an attributive descriptor, particularly in the phrase "balas ruby."

**Cross-Linguistic Notes:**
Interestingly, the word appears across numerous languages with different meanings. In Malayo-Polynesian languages (Indonesian, Tagalog, Cebuano, Kapampangan), it typically means "sand" or "granulated sugar," deriving from Proto-Malayo-Polynesian *badas ("grit, coarse sand, gravel").
```


## [2026-09-04T22:50:58.436Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -c \"بلخ\" $f; grep -o -n \"باختر[^ ]*\" $f | head -5; done",
 "description": "grep Moin for Balkh/bakhtar"
}
```


## [2026-09-04T22:50:59.328Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/attitude",
 "prompt": "Give the full etymology of \"attitude\" verbatim: French, Italian attitudine, Late Latin aptitudinem, Latin aptus."
}
```


### [2026-09-04T22:51:00.291Z] TOOL RESULT

```
### MON_part1.txt
13
19730:باختر
19732:باختر
19736:باختر
55018:باختر.
### MON_part2.txt
10
1066:باختری؛
6906:باختر.
57635:باختر.
61540:باختر؛
```


### [2026-09-04T22:51:04.593Z] TOOL RESULT

```
# Etymology of "Attitude"

The word "attitude" traces back through several languages. It entered English in the 1660s "via French _attitude_ (17c.), from Italian _attitudine_" meaning "disposition, posture." The Italian term derived from "Late Latin _aptitudinem_" which came from Latin _aptus_, meaning "joined, fitted."

This Latin root _aptus_ is shared with the word "aptitude," making them doublets—words with a common origin that diverged through different pathways.
```


## [2026-09-04T22:51:07.635Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19725,19745p' MON_part1.txt",
 "description": "Moin bakhtar entry"
}
```


### [2026-09-04T22:51:07.686Z] TOOL RESULT

```
نوزدهم تموز است. 

باحورا: 2:55 (ع.] (.) شدت حرارت در 
یت 

باختر : ۰22۴ (.) در اوستا اپاختره. به معنی 
شمال آمده و جایگاه اهریمن و دیوان و 
دوزح دانسته شده» در بهلوی نیز اباختر 
بدین معنی و نیز به معنی سیاره امده. در 
زبان فارسی اکثر به معنی مغرب استعمال 
می‌شود. در برابر خاور. ولی گاه نیز به 
عکس» باختر به معنی مشرق و خاور به معنی 
مغرب امده. 

باختن: 25-0 [- ب‌آزیدن] (مصل. م.) 
(باخت. بازد» خواهد باخت» بباز» بازند» 
باخته) زیان کردن در قمار» باختن چیزی به 
گرو؛ مق. بردن (در قمار). تلف کردن تمام یا 
حصه‌ای از مال خود. بازی کردن» مشغول 
شدن» سرگرم شدن. گوی» نرده شطر نج 
باختن. ورزیدن: عشق باختن (به عنی عشق
```


## [2026-09-04T22:51:14.821Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^اختر\\|اختر:\" MON_part1.txt | head -5; echo ---; grep -n \"بلخ\" MON_part1.txt | head -8; echo \"--- part2\"; grep -n \"بلخ\" MON_part2.txt | head -8",
 "description": "Moin axtar and Balkh"
}
```


### [2026-09-04T22:51:14.906Z] TOOL RESULT

```
8287:اختر: ۲ (.) ستار ه» جرم فلکی» کوکب؛ 
8297:اختر کاوبان‌اختر کاویان: درنش کاویانی. 
8310:اختراع: "3 ([ع.] (سص م.) آفریدن» 
8317:اختراعات. 
8319:اختربین: 227-0 (افا. ص‌مر.) منجم. 
---
15964:(ابلخانان مخول ئ قاجار به) 
19355:دادن امور دیوانی سفر از (ابلخانان» 
19364:ابلخانان. 
20550:مالیات (ابلخانان مغول). 
21031:درخشند ه. لب شهر بلخ. 
24505:تقسیم عنایم بوده است (ابلخانان مغول و 
26725:و مالبات (ابلخانان مغول). 
43620:مالیات بر مال و سرمایه (ابلخانان) رسومات 
--- part2
10873:ابلخانان مغول بود (ایلخانان). 
11145:حبوانات (ابلخانان). 
13922:(ابلخانان)؛ ج. ۰ (به سیاق ) عربی) قلانات. 
73814:از سلطان نبابت می‌کرد. در دوره ابلخانان 
79238:(ابلخانان)؛ نماری. 
81311:مالیات با عوارض (ابلخانان). 
89540:و مرج حکمفرما باشد نظیر دیوان بلخ 
93468:بستی (ابلخانان تا دورد آق‌قه بو نلو). اسب
```


## [2026-09-04T22:51:20.608Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8285,8300p' MON_part1.txt",
 "description": "Moin axtar"
}
```


### [2026-09-04T22:51:20.655Z] TOOL RESULT

```
اختتامات. 

اختر: ۲ (.) ستار ه» جرم فلکی» کوکب؛ 
نجم. ستارةٌ بخت و اقبال» ستار؛ٌ مسلط بر 
زایجه (بنابه عقيدة پیشینیان). اختر بد: طا 
بد» بخت بد. اختر دانش: (کن.) الف: 
مشتری. ب: عطار د. اختر دنساله‌دار؛ ستارة 
دنباله‌دار. نوعی ستاره که دم گونه‌ای دارد و 
عرت آن را دوذنب خواند. اختر ش بکرد: 
ماه. اختر نیکك: بخت نیکك. اختر سعد فال 
نیکك. نیکک‌بختی» نیک‌روزی, اقبال» حسن 
طالع. درفش» علم» رایت لوا اختر کاوان: 
اختر کاوبان‌اختر کاویان: درنش کاویانی. 
(گیا.) سردستة گیاهان تيرةٌ اختریان است و 
جزو تک لیه‌ای‌ها می‌باشد و دارای ساقه‌های 
زیرزمینی و برگک‌های هن دراز است.
```


## [2026-09-04T22:51:21.738Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Bactria",
 "prompt": "Give the etymology of Bactria verbatim: Old Persian Bāxtriš, Avestan Bāxδī, Middle Persian Baxl, New Persian Balx, and any proposed Proto-Iranian source."
}
```


### [2026-09-04T22:51:26.797Z] TOOL RESULT

```
# Etymology of Bactria

Based on the Wiktionary article provided, here is the etymological information given:

The term derives from "Latin _Bactria_, from Ancient Greek _Βακτρίᾱ_ (Baktríā), from Old Persian _𐎲𐎠𐎧𐎫𐎼𐎡𐏁_ (b-a-x-t-r-i-š /⁠bâxtriš⁠/)."

**Note:** The source document does not include information about Avestan Bāxδī, Middle Persian Baxl, New Persian Balx, or Proto-Iranian sources. The article only traces the etymology back to Old Persian *bâxtriš*, with comparisons to modern Persian and Hindi cognates but without the additional linguistic stages you requested.
```


## [2026-09-04T22:51:36.841Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN balas\"; grep -n -m3 -A5 \"^balas\" KLN_1966.txt; echo \"== SKT\"; grep -n -m2 -A3 \"balas\" SKT.txt; echo \"== LKT\"; grep -n -i -m5 \"balais\\|balaḫš\\|balachsch\\|Badachschan\" LKT.txt; echo \"== DEV\"; grep -n -i -m5 \"balais\" DEV.txt; echo \"== PHN\"; grep -n -i -m5 \"balais\" PHN.txt",
 "description": "balas in western dictionaries"
}
```


### [2026-09-04T22:51:36.931Z] TOOL RESULT

```
== KLN balas
4308:balas,  n.,  a  variety  of  spinel  ruby.  —  F.  balais, fr.  Arab,  balakhsh,  fr.  Balakhshdn,  fr.  Pers. Badhakhshin,  name  of  a  region  in  Central  Asia (near  Samarkand),  where  this  variety  of  spinel ruby  is  found.
4309-balatron,  n.,  jester,  buffoon.  —  L.  balatro,  gen. -onis,  of  Etruscan  origin;  not  related  to  L. blaterd,  ‘babbler’.
4310-balaustine,  n.,  the  pomegranate  tree.  —  Formed with  suff.  -ine  fr.  Gk.  pocXaucmov,  ‘flower  of the  wild  pomegranate’,  a  word  of  Sem.  origin. Cp.  Aram,  balatz,  said  of  the  blossoming  of  the pomegranate  tree.  For  the  correspondence  of Greek  st  to  Semitic  s,  tz,  cp.  Gk.  e-rupa^,  fr. Heb.  tzdri  (see  sty  rax).  Cp.  baluster, balbriggan,  n.,  a  cotton  fabric  used  for  hosiery.  — Prop,  ‘fabric  made  in  Balbriggan  (in  Ireland)’, balbuties,  n.,  stammering  (med.)  —  Medical  L., fr.  L.  balbutire,  ‘to  stammer’,  fr.  balbus,  ‘stam¬ merer’,  from  the  I.-E.  imitative  base  *bal-,  ‘to stutter’.  See  booby  and  cp.  words  there  re¬ ferred  to.
4311-balcony,  n.  —  It.  balcone,  formed  with  the  aug¬ mentative  suff.  -one  fr.  balco,  ‘scaffold’,  which is  borrowed  fr.  OHG.  balcho,  ‘beam’  (whence MHG.  balke,  G.  Balken,  ‘beam’).  See  balk, ‘beam’.
4312-bald,  adj.  —  ME.  balled,  orig.  ‘white’,  fr.  I.-E. base  *bhel-,  ‘to  shine’,  whence  also  OI.  bhalam, ‘brightness;  forehead’,  Gk.  <paX6?,  ‘white’.
4313-142
== SKT
== LKT
563:N.  pr.  Name  des  nordöstlichen  Teiles des  lieutigeii  Afgänistän.  Von  hier  be- zot,'  man  in  früheren  Zeiten  Edelsteine [MP  12ü/lt241.  Über  das  ar.  balaM  er- ^ab  sich  als  Bezeichnunjj;  iür  eine  Rubin- art ndat.  bahiscius,  it.  halascio,  halasso, sp.  halaju,  balaja,  pg.  balais,  bedache, kat.  balaix,  frz.  prov.  balais;  dtsch. Ballasrubin.  [Devic  DEt  57.  DE  S!33. ML  891.
6346:balais  151
7974:badana  316 badanal  21 badea  319 badejo  1 badiana  162 bafari  \11 bagaxa  171 öa;ii<  1975 6«;»«/  1975 bailadera  1530 balache  151 balais  151 balcäo  197 baldequino  170 ia^rf/o  271
8515:balais  151
== DEV
726:Balais  (Rubis).  Esp.  balax,  balaxo,  balaja;  portug. halax,  ital.  balascio,  bas  lat.  balascius.  De  l'arabe  iJ^sÀsi balakltch,  venant  du  persan  (jLi^j^^Xj  badakhchân ,  nom  du pays  d'où  l'on  tire  ces  gemmes.  ^^  C'est  dans  les  montagnes de  Badakschian  que  se  trouve  la  mine  de  rubis  que  les Orientaux  appellent  badakhschiani  ou  balakhschiani ,  et  que nous  nommons  rubis  balays.  •;?  (D'Herbelot^.)  ç^Pour  ce qui  est  du  rubis.  .  .  ,  on  l'appelle  aussi  balacchani^  pierre de  Balacchariy  qui  est  le  Pégu^,  d'où  je  juge  cju'est  venu le  nom  de  balais  qu'on  donne  aux  rubis  couleur  de  rose.  ?? (Chardin*.)  Marco  Polo  appelle  ce  même  ipays Balasian  et les  rubis  balaxi  ou  balasci.
2942:Balacchan ,  voy.  Balais.
2943:Balais  (Bnbis).
2944:Balaja,  esp.  voy.  Balais.
2945:Balascio,  ital.  voy.  Balais.
== PHN
2100:BALAIS, adj. m. (p.)
2106:balais, en persan ^L&^«Xj JoJ [/aV badakhchân j. — Les Italiens
10271:Balais, adj. m. (p.) 55DES MOTS EXPLIQUÉS. 379
```


## [2026-09-04T22:51:59.229Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LAT apio/aptus\"; grep -n -m4 -B2 -A8 \"apiscor\" LAT.txt | head -50; echo \"== LEW\"; grep -n -m3 -A6 \"apiscor\" LEW_1910.txt | head -30",
 "description": "Latin etymological dicts for apere"
}
```


### [2026-09-04T22:51:59.283Z] TOOL RESULT

```
== LAT apio/aptus
4366-dejA dans Plaute, usitn surtout au pl., ineptiae "sottises" et ineptio,
4367--is.
4368:Apio a un inchoatif apiscor, -eris, aptus sum (pour la derivation,
4369-cf. facio, pro-ficiscor) dont il existe un doublet actif apisco chez
4370-les archaiques, cf. J.-B:Hofmann, De uerbis... deponentibus, pp.12,32,
4371-40; apiscitur est passif chez Pl., Trin.367: "s'attacher A", d'ou "at-
4372-teindre, obtenir".
4373-Apiscor, rare, quoique classique (Cic., T.L.), a fourni les composes
4374-adipiscor, d'ou adeptio (cic.); indipiscor (et indipisco; aussi inde-
4375-pisci, P.F.94,18) redipiscor (Pl., Trin.1022) . Indipiscor a conserve
4376-la forme ancienne du pr^verbe ind(u) (cf. indaudire ) de end(o) , sans
--
4389-apparait surtout au parfait et a 1'aoriste; oeci explique 1'importance
4390-de coepi en latino Le pr6sent skr. dpnSti "il atteint" est d6ja dans
4391:1 1 Atharvaveda; il est secondaire, comme apio et apiscor le sont en
4392-latin. Le hittite epmi "je prends" (3® sgo epzi, etc.) indique un ancien
4393-present athematique que donnait a supposer lat. apio. Pour hitt. e repr 4 -
4394-sentant e, cf, es- = gr. tict- , skr. 5 s-. L'adjectif skr. aptah n'est pas
4395-ancien; il ne se superpose pas a aptus » Le sanskrit a gen6ralis6 le
4396-representant de 1 1 e conservi dans lat. co-epi ou d*un ancien o que sup-
4397-pose arm . unim "je tiens, j , ai", de *op-ne- , et la latin a tendu a gene-
4398-raLiser le degr6 zero a attest6 par lat .aptus.
4399-apis, -is (g6n.pl. a pum ou apium, cf. Neue-Wagener, Forra? I 359 , ce
--
40274-adhuc nos dicimus nanciscitur et nactus, i.e. adeptus. Le simple a
40275-4t4 remplac4 par 1'inchoatif nanciscor,-eri^, nactus (nanctus) sum,
40276:nancisci (cf. apiscor/apis, paciscor/paco ): rencontrer, trouver, ob-
40277-tenir; contracter (ane maladie). Ni compos4s, ni d4riv4s. - Ancien
40278-(XII Tables) et classique, mais rare a l'4poque imperiale, ou l'on
40279-ne troave que quelques exemples de nactus. Da reste le verbe, dtant
40280-donne son sens, ne s'emploie guere qu’au perfectam, de meme qu'en
40281-grec la racine n'a fourni que des thbmes d'aoriste et de parfait:
40282-Tiveyxov, evqvoxa* Conservi en logoudorien, M.L.5816 *nanciscSre.
40283-nanciscor, nactus appartient k ane racine indo~europ4enne dont
40284-les formes sont aberrantes. L'adjectif en —to— lat. nactus ne peat
== LEW
```


## [2026-09-04T22:52:00.207Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==145 || NR==146' IEC.txt | grep -n -i \"axtar\\|star\\|ster\" | head -20",
 "description": "Mann IEC p.260"
}
```


### [2026-09-04T22:52:02.149Z] TOOL RESULT

```
27:elntà, os, is ‘tree; timber’. Cf. WP I, 152 & 437. Variant: lenta, is Hitt. alanc(a) (a kind of wood); Gk. láte ‘pine’; Alb. lândë, lëndë “tree, timber, mate- rial, substance’; Br. lann juniper’; ON lind “lime-tree? beside lundr ‘copse, tree’; Pol. cf. tet ‘stick’; Cz. la? (“lath”, infl. by G Latte); Li. lentà “board”; Latv. ? lieta “thing, matter’. O-gde in G Lande ‘stake, pale’; Ge-länder ‘banister’; MHG lander, f. ‘palings’; Swiss Lande ‘shaft of cart
```


## [2026-09-04T22:52:10.969Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"axtar\" IEC.txt | head -10; echo \"== ster\"; grep -n -m5 \"stēr\\|ster- .star\\|'star'\" IEC.txt | head -20",
 "description": "Mann axtar"
}
```


### [2026-09-04T22:52:11.025Z] TOOL RESULT

```
3841:oster- (osteren-, ster-) ‘star’. WP II, 635. (A Semitic LW according to E. Schrader. Cf. Akkad. istar, Can. Syr. Astarte, AStoroth, a goddess of fertility. Cf. also Basque izar ‘star and Kabyle ithri, id.) Skt. cf. str-bhih ‘by the stars; Romani Cheren ‘star’; Av. stare, acc. stárom beside axtaro, id., Per. sitare, axtar; Tokh. eren, B on, sCirin, beside cCirye; Hitt. asteras, sittar; Gk. astér, gs. asté- ros beside ástron; (LW in Lat. astrum); Lat.
== ster
```


## [2026-09-04T22:52:29.122Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1126\\.\" HRN.txt | head -5; echo ---; grep -n \"jäften\\|yäften\\|jäft\\|jaften\" HRN.txt | head -10",
 "description": "Horn yaftan"
}
```


### [2026-09-04T22:52:29.175Z] TOOL RESULT

```
14034:yex 1126.
14035:y «?/€<? 1126.
14379:afxa- 1126.
17460:;/«// 1126.
19673:)ftx 1126.
---
1398:Die augenscheinlich sekundäre Bildung enjäften
1399:'beendigen* (vergl. ferjaften) findet sich nur in der
9703:1124. yäften 'erlangen, erreichen, erfinden*, Praes. yah-em,
10437:82. frajäftan Vollenden* (AV., in späten Kolophonen).
10458:mutung in den unorganischen phlv. frajäftati, jüd.-
```


## [2026-09-04T22:52:30.295Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ln in [('IEC.txt',3841),('SYN.txt',22248),('SYN.txt',22308)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    print(f,ln,'leaf',('\\n'.join(lines[:ln])).count('\\f'))\nEOF",
 "description": "compute leaves"
}
```


### [2026-09-04T22:52:32.412Z] TOOL RESULT

```
IEC.txt 3841 leaf 156
SYN.txt 22248 leaf 941
SYN.txt 22308 leaf 943
```


## [2026-09-04T22:52:42.254Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9700,9720p' HRN.txt",
 "description": "Horn 1124 yaften"
}
```


### [2026-09-04T22:52:42.300Z] TOOL RESULT

```
1123. yase (eyase) *Wunsch, Begierde'^).
aw. *ayäs((k(i' 'Wunsch, Begehren', vergl. d -| yäs-,
yäsanuha 'wünschen, verlangen*.
1124. yäften 'erlangen, erreichen, erfinden*, Praes. yah-em,
..-\*^'' ••i:5n^ (Jer. 2, 24).
aw. vergl. ayapta- 'Belohnung; phlv. äyäftan
(Yasna, Spiegel, Trad. Lit. 439), yaftan (Bund.),
vergl. äyaft,
oss. d. ba]yafun, t. ba]yafin einholen, erreichen'
(145).
») 'Dar steht daneben in hösdär (Sahn. I, 234 Vers 1882). Das
Suffix -yär ist generell jünger als -r/är, doch erscheint dieses letztere
auch häufig in neuen Bildungen.
2) Vergl. Seite 128 Note 6.
*) Der bei Vullers s. v. mitgeteilte Vers Fürbehä Jäml's ist
nach dem FR als Beleg bedenklich, da eine andere Lesart yäse'l
Xünrä laute und yäse — türk. yaso^ yesäq sei (Vullers 1, yäsp).— 252 —
\l2i>'^^ f/än *liimmlische Offenbarung, Gesicht' (mystischer
t. t., den ich nicht zu belegen vermag).
ap. f/ana- *6abe, Gnadengabe' ^) ; aw. yäna; phlv.
yün (Hörn).
```


## [2026-09-04T22:52:43.682Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"yäften\\|jäften\\|ayäftan\" HUB.txt | head -10; echo \"== HUB awam\"; grep -n -i \"awam\\|āpām\\|apām\" HUB.txt | head -10",
 "description": "Hübschmann lookups"
}
```


### [2026-09-04T22:52:43.738Z] TOOL RESULT

```
== HUB awam
2137:*drawam spater nach der Analogic von Verben wie MnU-
```


## [2026-09-04T22:52:51.295Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=balas",
 "prompt": "Give the American Heritage Dictionary entry for \"balas\" including its full etymology (Middle English, Old French, Arabic, Persian)."
}
```


### [2026-09-04T22:52:56.955Z] TOOL RESULT

```
# American Heritage Dictionary Entry: Balas

**Definition:** A semiprecious gemstone, this term refers to "a rose-red to orange spinel used as a semiprecious gem, once confused with the ruby."

**Etymology:** The word's linguistic journey traces back through multiple languages and regions:

- **Middle English** origin from Old French *balais* and Old Spanish *balax*
- Connected to **Medieval Latin** *balascus*
- Derived from **Arabic** *balaḫš*
- Ultimately from **Persian** *Badakhshān*, referring to a region in northeast Afghanistan

This etymological path illustrates how trade routes and cultural exchange shaped English vocabulary, with the word traveling westward from the Persian region known for producing these valuable stones.
```


## [2026-09-04T22:53:09.200Z] TOOL CALL #78: Bash

```json
{
 "command": "ls data/ && ls data/extracted | head",
 "description": "inspect data dir"
}
```


### [2026-09-04T22:53:09.237Z] TOOL RESULT

```
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
batch
NEXT_CHUNK
RETRY.txt
test
```


## [2026-09-04T22:53:13.276Z] TOOL CALL #79: Bash

```json
{
 "command": "ls -la | head -25; find . -maxdepth 2 -iname \"*.pdf\" 2>/dev/null | head",
 "description": "look for source pdf"
}
```


### [2026-09-04T22:53:13.330Z] TOOL RESULT

```
total 24660
drwxrwxr-x  8 sfmqrb sfmqrb     4096 Sep  4 13:41 .
drwxrwxr-x 20 sfmqrb sfmqrb     4096 Sep  4 14:35 ..
-rw-rw-r--  1 sfmqrb sfmqrb     2209 Aug 22 01:02 CONTRIBUTING.md
drwxrwxr-x  6 sfmqrb sfmqrb     4096 Sep  4 10:26 data
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 15:38 docs
-rw-rw-r--  1 sfmqrb sfmqrb  1201179 Aug 22 01:02 EtymologicalDictionary-persian-english.epub
-rw-rw-r--  1 sfmqrb sfmqrb 23984297 Aug 22 01:02 EtymologicalDictionary-persian-english.pdf
drwxrwxr-x  9 sfmqrb sfmqrb     4096 Sep  4 16:10 .git
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 01:02 .github
-rw-rw-r--  1 sfmqrb sfmqrb      263 Sep  4 13:41 .gitignore
-rw-rw-r--  1 sfmqrb sfmqrb    12133 Aug 22 15:41 README.fa.md
-rw-rw-r--  1 sfmqrb sfmqrb     8014 Aug 22 15:39 README.md
drwxrwxr-x  3 sfmqrb sfmqrb     4096 Aug 22 18:35 site
drwxrwxr-x  4 sfmqrb sfmqrb     4096 Sep  4 14:35 tools
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T22:53:16.145Z] TOOL CALL #80: Bash

```json
{
 "command": "(pdftotext -f 58 -l 58 -layout EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -80) || echo \"no pdftotext\"",
 "description": "extract page 58 text from source pdf"
}
```


### [2026-09-04T22:53:18.080Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T22:53:20.770Z] TOOL CALL #81: Bash

```json
{
 "command": "which pdftotext pdftoppm; python3 -c \"import fitz; print('fitz ok')\" 2>&1 | head -2",
 "description": "check pdf tools"
}
```


### [2026-09-04T22:53:22.802Z] TOOL RESULT

```
/usr/bin/pdftotext
/usr/bin/pdftoppm
Traceback (most recent call last):
  File "<string>", line 1, in <module>
```


## [2026-09-04T22:53:28.105Z] TOOL CALL #82: Bash

```json
{
 "command": "D=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 58 -l 58 -r 200 -png EtymologicalDictionary-persian-english.pdf $D/p58 && ls -la $D/p58*",
 "description": "render pdf page 58"
}
```


### [2026-09-04T22:53:30.467Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 86276 Sep  4 18:53 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p58-058.png
```


## [2026-09-04T22:53:32.700Z] TOOL CALL #83: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p58-058.png"
}
```


### [2026-09-04T22:53:33.052Z] TOOL RESULT

```

```


## [2026-09-04T22:53:33.049Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-04T22:53:48.121Z] TOOL CALL #84: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81ep-\" \\\n \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%AE%D8%AA%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AE%D8%AA%D8%B1\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 58 (book 28), roots Ap 2 / Apank: PIE *h1ep-, Persian vam, yaftan, axtar, baxtar\" 2>&1 | tail -2; done",
 "description": "archive wiktionary sources"
}
```


### [2026-09-04T22:53:53.492Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8326ebe71be8013c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/914a1f1cf9627b50.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/194836e34cca842e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9981fb5b8c7d95f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c927414f3feb6470.txt
```


## [2026-09-04T22:53:58.865Z] TOOL CALL #85: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/balas\" \\\n \"https://www.etymonline.com/word/apt\" \\\n \"https://www.etymonline.com/word/couple\" \\\n \"https://www.etymonline.com/word/attitude\" \\\n \"https://www.ahdictionary.com/word/search.html?q=balas\" \\\n \"https://en.wiktionary.org/wiki/Bactria\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 58 (book 28), roots Ap 2 / Apank: balas/balais/balaxs, Latin apere family, Bactria/Balkh\" 2>&1 | tail -2; done",
 "description": "archive remaining sources"
}
```


### [2026-09-04T22:54:04.649Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/80c99d44d1c7fa7c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d3d5df48bfd3a36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01c1eea1b34c0703.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81cd99626f365c5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c9e7fced37cd1c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c286ea20aafb8f30.txt
```


## [2026-09-04T22:54:12.506Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 ../web/1d3d5df48bfd3a36.txt; echo; echo \"=== WLD Bd1\"; grep -n -m3 -A12 \"apiscor\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -40",
 "description": "check archives and Walde-Pokorny"
}
```


### [2026-09-04T22:54:14.795Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/apt
FETCHED: 2026-09-04T22:54:02Z
STATUS: 200
TITLE: Apt - Etymology, Origin & Meaning

Apt - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of apt 

 apt (adj.) 

 mid-14c.,
=== WLD Bd1
3127:Lat. apiscor „fasse, erreiche“, adipiscor „erlange“, coepi „habe ange- 
3128-fangen“. Wegen des genau zusammenstimmenden ai. aptah und lat. aptus 
3129-„angefiigt, verbunden, angepaBt, passend“ steht der Zusammenhang mit 
3130-lat. *apio, *apere „comprehendere vinculo, verbinden, umbinden“ (imper. 
3131-ape „probibe, compesce“ Vanieek 15, Thes), copula ( co-apula ) „Band“ 
3132-ammentum (aus *ap-mentom Vanieek 15) ,,'Wurfriemen, Riemenschleife, 
3133-Riemen zum Binden“ (vgl. Yf. LEWb. 2 35) fest. Yielleicht ist von einer 
3134-gemeinsamen Grundbedeutung „fassen, zusammenfassen" auszugehen. 
3135-
3136-Auch lat. apud „bei :! wird am besten hierher zu stellen sein. Die Grund- 
3137-bedeutung ware „in naher Verbindung“ (vgl. juxta). Man hat von ppa. 
3138-neutr. *apuod (aus *apuot „erreicht habend“) auszugehen. Die Nebenform 
3139-apor, apur (mars. -lat. apur finetri) weist auf ursprgl. -d. Ygl. Georges, 
--
33467:haltnis aptus : apiscor). 
33468-
33469-Anm. : Abweichend verbinden Legerlotz KZ. 8, 416, Lagererantz KZ. 
33470-35, 287 f. und Nord. Stud. 450f. gut als '*ghatos mit gr. yaoiog' aya&os, 
33471-yogoTog lies., lakon. yuiog (pyaxiog) ,,gut“ und alb. zot „tiichtig“. Andrer- 
33472-seits hat man oft (vgl. bes. Johansson BB. 13, 115 f.) mit gut das gr. aya- 
33473-&og. bei Hesych dxaftog. zusammengebracht, wobei der Anlaut am ehesten 
33474-das a- copulativum („ganz gut“?), und y statt x durch volketymologische 
33475-Anlehnung entstanden ware ; doch hat dyadog noch als etymologisch dunkel 
33476-zu gelten, s. Boisacq s. v., wo Lit. (wozu Brugmann IF. 19, 389). 
33477-
33478-Ganz fragwiirdig wird von Fick 4 III, 123 auch ahd. gadum n. — „mit 
33479-Unterbleiben der Yerschiebung vor m“ — umschlossener Raum, Haus,
```


## [2026-09-04T22:54:22.478Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3112,3128p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD root header"
}
```


### [2026-09-04T22:54:22.533Z] TOOL RESULT

```
1. ap- „erreichen“. 

Ai. apnoti „erreicht, erlangt“, dpta-h „geschickt, geeignet, vertraut“ (d 
durch Kontraktion der Praposition <1- mit dp- ? Keller KZ. 39, 157); av. 
apayeiti „erreicht“. 

Gr. ajtzco „anheften, anbinden, anziinden“, dcprj „Beriihrung, Haften usw.“ 
wird trotz dem Spiritus hierherzustellen sein. Kretschmer Gl. 7, 352 nimmt 
Beeinflussung durch ejico an. Brugmanns Yerbindung mit skr. yabhati „fu- 
tuit“ hat nichts fiir sich (vgl. Kretschmer aaO. u. s. v. iabh-). Pedersen KZ. 
39, 428 stellt mit gr. dmm arm. ap „die hohle Rand“ (o-Stamm, doch lok. 
y-api als -i-Stamm, also wohl alter ntr. -os-Stamm) zusammen, welches 
Wort dem gr. dipog „Gelenk“ entsprechen soil. Das bleibt unsicher. 

Lat. apiscor „fasse, erreiche“, adipiscor „erlange“, coepi „habe ange- 
fangen“. Wegen des genau zusammenstimmenden ai. aptah und lat. aptus
```


## [2026-09-04T22:55:55.916Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT baxtri\"; grep -n -i -m4 \"Baxtri\\|Bāxtri\" KNT.txt | head; echo \"== AFM balakhsh\"; grep -n -m4 \"بلخش\\|بدخشان\" AFM.txt | head; echo \"== PLA\"; grep -n -i -m4 \"balaḫš\\|balahs\\|Badaḫšān\\|balaxš\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head; echo \"== TAD\"; grep -n -m3 \"بلخش\" TAD.txt | head",
 "description": "Kent Bactria and Arabic balakhsh sources"
}
```


### [2026-09-04T22:55:56.021Z] TOOL RESULT

```
== KNT baxtri
2134:АЫ. Sg.: Harawatiyà, Baxtriya, Uvdrazmiyd.
2135:Loc. Sg.: Harawatiyd, Baxtriya, йрй, bümiyā.
3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
3705:21 nā : kartam : Baxtriya — :08tiy : Dárayavaus : xSaya
== AFM balakhsh
1093:(اللقار )وهر ات ف بلخشان ٠‏ والعجم يقولون له بدخشان (شفاء الغليل) ٠‏ 
6670:بدخشان ܟ 
== PLA
== TAD
```


## [2026-09-04T22:56:02.471Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1090,1096p' AFM.txt; echo \"--- leaf\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'بلخشان' in p: print('leaf',i)\nEOF",
 "description": "Addi Shir balakhshan"
}
```


### [2026-09-04T22:56:04.402Z] TOOL RESULT

```
+ الآ ܨܣ 1 ا من 3 اى العالى ٠وقالوا‏ 4 إلتدك ‹ | بلَتَدَح 

(اللقار )وهر ات ف بلخشان ٠‏ والعجم يقولون له بدخشان (شفاء الغليل) ٠‏ 
ام ندخشان ويقال ها 6 5 بالفارسمة قاسم ولاه ببن خوراسان وهندستان فيها 
معادن الذهس والآأ حجار اتكرعة (البرهان القاطع ) 

--- leaf
leaf 27
```


## [2026-09-04T22:56:11.946Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor tgt in (3252,4308):\n    print(tgt,'leaf',('\\n'.join(lines[:tgt])).count('\\f'))\n# find nearest standalone page numbers around leaf of 3252\nimport re\npages=t.split('\\f')\nfor i in (60,61,62,63):\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', pages[i])\n    print('leaf',i,'nums',nums[:5])\nEOF",
 "description": "Klein page markers"
}
```


### [2026-09-04T22:56:14.218Z] TOOL RESULT

```
3252 leaf 62
4308 leaf 86
leaf 60 nums ['92', '93']
leaf 61 nums []
leaf 62 nums ['96']
leaf 63 nums []
```


## [2026-09-04T23:01:31.103Z] TOOL CALL #91: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-58.json",
 "content": "{\n  \"pdf_page\": 58,\n  \"book_page\": 28,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ap 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁ep- 'to take, seize, reach' (Pokorny '1. ap- (richtiger əp-) : ep- \\\"fassen, nehmen, erreichen\\\"', IEW 50-51; Watkins/AHD ap-¹ 'To take, reach'; LIV *h₁ep-)\",\n      \"note\": \"Root, language label and gloss are all correct: Pokorny's entry begins at the foot of p.50 (exactly Nourai's POK:50) and runs onto p.51, with Av. apayeiti, Skt. āpnóti, Lat. apiscor/apere/aptus/apex/cōpula and Hitt. epmi — i.e. precisely the two branches Nourai draws. The only correction is that the modern reconstruction has an initial laryngeal (*h₁ep-), which is why Hittite has e-ep-zi and Latin co-ēpī shows e-vocalism. Nourai's numbering 'Ap 2' distinguishes this root from 'Ap 1' = *h₂ep- 'water' (Pokorny 2. āp- p.51), which is the right distinction. The weak point of the page is not the root but the Iranian branch: Cheung 2007 removes MP abām 'loan' from this root altogether (see node 2).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁ep-\",\n        \"https://www.etymonline.com/word/apt\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:50\", \"status\": \"supports\", \"note\": \"POK_01.txt ff-page 59-60 (printed 50-51, the entry straddles the page break): '1. ap- (richtiger əp-) : ep- \\\"fassen, nehmen, erreichen\\\". Ai. āpnóti \\\"erreicht, erlangt\\\" ... av. apayeiti \\\"erreicht\\\" ... lat. apiscor \\\"fasse, erreiche\\\", adipiscor \\\"erlange\\\", coepi ... Zusammenhang mit lat. *apiō, *apere \\\"comprehendere vinculo\\\" ... aptus \\\"verknüpft\\\", cōpula (co-apula) \\\"Band\\\" ... lat. apex, -icis \\\"Spitze\\\" ... gehört vielleicht zu *apiō ... hitt. e-ip-mi \\\"nehme\\\". WP. I 45 f.' — the cited page is exactly Nourai's root and his Latin node.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ap 1, af, ab : to receive ; apayeiti : received ; abi-âp, abi-âf : to detain\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Avestan ap- 'to reach, attain' (present stem apaiia-, 3sg. apaiieiti Yt 10.21, 14.20, 17.19; 1sg. apaiiemi Yt 5.42, 15.43; perf. āpa; OAv. 1pl. opt. apaema Y 41.2) is the regular Iranian continuant of PIE *h₁ep-: *h₁p-eie- > Ir. *apaya-, with intervocalic *p preserved in Avestan. Nourai's 'af, ab' are not Avestan or Old Persian forms at all but retrojections of the later Iranian outcomes, where Old Iranian *p in postvocalic position lenites through *β to Middle/New Persian f (before a consonant / word-finally) and b/w (before a vowel): hence MP ayāft ~ ayāb-, NP yāft ~ yāb-. Old Persian has no attested reflex of this root (Kent's lexicon has none), so the label 'Avestan / Old Persian' overstates the evidence. The compound is Av. aiβi-/avi-ap- (Nyberg: 'ay- probably < abi-, cf Av. avi-ap-'; Cheung: '(+ *abi-) to obtain, find'), and its meaning is 'to obtain, reach, find' — NOT 'to detain'. The scan of p.28 does print 'to detain', so this is Nourai's own slip (probably for 'to obtain'), not a transcription error in the JSON.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁ep-\",\n            \"https://en.wiktionary.org/wiki/یافتن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:50\", \"status\": \"supports\", \"note\": \"POK_01.txt ff-page 59 (printed 50): 'Ai. āpnóti \\\"erreicht, erlangt\\\" ... av. apayeiti \\\"erreicht\\\", 3. Pl. apənte aus *āpuantai' — the Avestan form and gloss are exactly as charted.\"},\n            {\"ref\": \"SNS:14\", \"status\": \"not_found\", \"note\": \"SNS_pages.txt: the Šāyast nē Šāyast glossary OCR is very poor. The a-/ab- stretch of the glossary is ff-leaf 29 (≈ printed p.14) and there I can read 'abdum/afdum ... (HuIVb. 80-81) *apatəma, apama' and abartar/abē-mōzag/aburnāy/afrīn/agar, but no legible ap-/apām entry. grep for 'apam|ayaf|ayab|awam' across ff-leaves 26-33 returns only that *apatəma line.\"},\n            {\"ref\": \"FFD:82\", \"status\": \"supports\", \"note\": \"FFD_pages.txt [pdf page 87] = printed p.82, s.v. یافتن: 'یافت < فارسی میانه ayāft < ایرانی باستان *abi-āp-ta-… ای پیشوند فعلی است. ریشهٔ āp به معنی «به دست آوردن» است.' — Abolghasemi's root is āp 'to obtain', with abi- as the preverb, i.e. Nourai's 'abi-âp' but glossed 'to obtain', not 'to detain'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"s.v. ap-, col. ~74 (BRT.txt lines 3478-3479)\", \"stance\": \"supports\", \"note\": \"Bartholomae gives the paradigm apayeiti with senses '1) einholen, nachkommen 2) gelangen zu —, teilhaftig werden 3) treffen (vom Geschoss) 4) (einem Gebot) nachkommen', citing Yt 10.21, Yt 14.20, Y 41.2 — the root and the form apayeiti are exactly as charted.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 161-162 s.v. *Hap/f\", \"stance\": \"supports\", \"note\": \"'*Hap/f \\\"to reach, attain\\\" — *AVESTAN: ap- \\\"to reach, attain\\\" || (+ *abi-) \\\"to obtain, find\\\" || (+ *pati-) \\\"to reach to\\\" || (+ *pari-) \\\"to reach, attain\\\"'; forms listed: YAv. apaiiemi, apaiieiti, apaiieinti, OAv. apaema, perf. āpa. Confirms the root and gives 'to obtain, find' for the abi- compound.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 45 (WLD_Bd1 djvu lines 3112-3140)\", \"stance\": \"supports\", \"note\": \"'1. ap- \\\"erreichen\\\". Ai. āpnóti \\\"erreicht, erlangt\\\" ... av. apayeiti \\\"erreicht\\\". Lat. apiscor \\\"fasse, erreiche\\\", adipiscor \\\"erlange\\\", coepi ...' — Walde-Pokorny I 45 f. is the source Pokorny 50 refers to.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. ap-¹\", \"stance\": \"supports\", \"note\": \"'ap-¹. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex ... 4. Prefixed form *co-ap- ... cōpula ... [Pok. 1. ap- 50.]'\"},\n            {\"src\": \"KNT\", \"where\": \"Old Persian lexicon\", \"stance\": \"silent\", \"note\": \"Kent has no Old Persian verb ap-/āp- 'to reach'; the only Bāx-/ap- material in the lexicon is Bāxtriš and the preposition apa-. So the 'Old Persian' half of the language label is unsupported.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"apâm, avâm : loan, something received.\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Book Pahlavi ʾpʾm /abām/ 'loan, debt' is well attested (MacKenzie p.4; Nyberg II 22; Parthian ʾbʾmyh 'loan'). Nourai, following Nyberg and Mo'in, analyses it as Old Iranian *(ā-)apamna-, a middle participle of ap- 'to reach, obtain' — literally 'that which the lender has to obtain back', hence his gloss 'something received'. Cheung's Etymological Dictionary of the Iranian Verb (2007) rejects this: he files abām under the root *Hmai¹ 'to (ex)change' (< PIE *h₂mei-, Pok. 710, LIV 426) as a *apa- compound, comparing Sanskrit apa-mitya- 'something borrowed, debt' (Kāṭhaka+) from may- 'to exchange', Parth. ʾbʾmyh, Sogd. pʾmytʾy/pʾmytk 'loan' and Bactrian βαμδοιγο 'loan', and states in as many words that 'the etymology and reconstruction given by Nyberg 1974: 22a … from partic. med. *(ā-)apamna-, is less convincing'. The Sanskrit parallel apamitya- is decisive for Cheung because it gives a perfect semantic and morphological match ('borrowing' = 'exchanging away'), whereas *apamna- would be a unique formation. The modern standard therefore prefers a different origin, so the arrow root→apām is disputed; note that the two etymologies share the preverb *apa- and differ only in the verbal root (*Hap 'reach' vs *Hmai 'exchange').\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/وام\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2254\", \"status\": \"supports\", \"note\": \"BQT vol.4 [pdf page 337] = printed p.2254, Mo'in's footnote 6 to وام: 'وام (م.) < فام < بام < اوام. پهلوی apām (قرض، دین)، ایرانی *āpamna- (چیزی که دریافت شود). از āp- … نیبرگ …؛ در اوراق مانوی به‌پهلوی *ʾpʾm (عاریت، قرض)' — i.e. exactly Nourai's 'apām, avām: loan, something received' with the Old Iranian *āpamna- 'that which is received' analysis.\"},\n            {\"ref\": \"SNS:14\", \"status\": \"not_found\", \"note\": \"Same as node 1: SNS_pages.txt ff-leaf 29 (≈p.14) is the ab-/af-/ag- stretch of Tavoosi's glossary but the OCR yields no apām/awām entry; only 'abdum/afdum … *apatəma, apama' is legible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 4 s.v. abām\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'abām [ʾpʾm | P ʾbʾmyh, N (a)wām] loan, debt.' — form, meaning and the Parthian/New Persian correspondences are as charted, though MacKenzie gives no etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II (Glossary) p. 22a s.v. apam\", \"stance\": \"supports\", \"note\": \"'apam [ʾpʾm] debt 70⁵. — < OIr *apamna- \\\"that which a p. (the lender) has to obtain (from the borrower)\\\", middle pt. of Av. ap- (v. ayāftan); as to the form, cf. garāmīk. Paz. āwām; NP vām, āvām.' — this is Nourai's derivation verbatim, and is evidently his (and Mo'in's) source.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 162 (s.v. *Hap/f) and 177-178 (s.v. *Hmai¹)\", \"stance\": \"contradicts\", \"note\": \"Under *Hap/f: 'ç On Pth. ʾbʾmyh, BMP ʾpʾm /abām/, NP avam \\\"debt\\\" see *Hmai¹.' Under *Hmai¹: '(+ *apa-) BMP ʾpʾm /abam/ \\\"debt\\\". ⊙ The etymology and reconstruction given by Nyberg 1974: 22a … from partic. med. *(ā-)apamna-, is less convincing. … *SANSKRIT: may \\\"to exchange, change\\\" || (+ *apa) apamitya- … \\\"something borrowed, debt\\\". «PIE *Hamei- \\\"to (ex)change\\\" = LIV: 426 | Pok.: 710'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 131, pp. 30-31\", \"stance\": \"partial\", \"note\": \"Horn: 'ewām, awām \\\"Schuld\\\", wām. phlv. āpām (PPGL). bel. LW. wām.' Then on p.31: 'Darmesteter's Erklärung (Ét. ir. I, 75) aus *apama- d. i. apa + ama- = lat. abemptum ist aus zwei Gründen unmöglich…'. So Horn gives the Pahlavi antecedent but no positive etymology; what he rejects on p.31 is Darmesteter's apa+em- analysis, not Nourai's ap- analysis. Nourai's note 'HRN:31 does not agree with this derivation' is therefore only half right — Horn is silent about, not opposed to, the ap- route.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien, searched for awām/āpām\", \"stance\": \"silent\", \"note\": \"grep -i 'awam|āpām|apām' in HUB.txt returns nothing relevant (only *drawam); Hübschmann does not treat this word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"vâm «وام» : loan ; avâm «اوام» : loan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Middle Persian→New Persian step is beyond doubt: MP ʾpʾm /abām/ > early NP اوام/آوام awām, āvām (the regular treatment of postvocalic MP -b- as -w-), whence by aphaeresis of the unstressed initial a- the standard form وام wām, already the normal word in the 10th-11th c. (Farrokhi Sistāni: هزار بوسه فروشم بر لب تو مرا / تو وام‌دار منی خیز و وام من بگزار; Ferdowsi, quoted by Nourai: درم خواست فام از پی شهریار). The by-form فام fām listed by Nourai as 'فام ۲' is recorded by Borhān and by Mo'in's footnote in the chain وام < فام < بام < اوام, a spelling variant with f- for the older w-/b-. Mo'in glosses avām and vām identically as 'قرض، دین'. Only the ultimate parentage of MP abām (node 2) is disputed; this edge is not.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/وام\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SNS:14\", \"status\": \"not_found\", \"note\": \"As for nodes 1-2: the Šāyast nē Šāyast glossary (SNS_pages.txt ff-leaf 29 ≈ p.14) yields no readable apām/wām entry in this OCR.\"},\n            {\"ref\": \"BQT:2254\", \"status\": \"supports\", \"note\": \"BQT vol.4 [pdf page 337] = printed p.2254 s.v. وام, Mo'in's footnote: 'وام (م.) < فام < بام < اوام. پهلوی apām (قرض، دین)، ایرانی *āpamna- (چیزی که دریافت شود)' followed by the Farrokhi verse 'تو وام‌دار منی خیز و وام من بگزار'. Both charted words (وام, اوام) and both glosses are there.\"},\n            {\"ref\": \"AEF:173\", \"status\": \"not_checked\", \"note\": \"Khaleqi-Motlaq's Asās-e Ešteqāq-e Fārsi (the Persian translation/expansion of Horn) is not online and not in the local library (refs_online.json: kind 'catalog', no copy found).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 4 s.v. abām\", \"stance\": \"supports\", \"note\": \"'abām [ʾpʾm | P ʾbʾmyh, N (a)wām] loan, debt' — MacKenzie himself gives the New Persian outcome as (a)wām, i.e. both وام and اوام.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II p. 22a\", \"stance\": \"supports\", \"note\": \"'Paz. āwām; NP vām, āvām' — the three-way set Pazand āwām / NP vām / NP āvām matches the chart's وام, اوام and the extra آوام.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 177 s.v. *Hmai¹\", \"stance\": \"partial\", \"note\": \"'*NWIR: (+ *ā-apa-) NP avam \\\"debt\\\"' — Cheung has the same NP form and the same MP antecedent, but assigns the whole family to *Hmai¹, not to *Hap.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 131 p. 30\", \"stance\": \"supports\", \"note\": \"'ewām, awām \\\"Schuld\\\", wām. phlv. āpām' — Horn lists exactly the New Persian forms of this node under the Pahlavi antecedent.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"ayâf, ayâb : to find\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Book Pahlavi ʾyʾp-tn' /ayāftan/, present stem ʾyʾb- /ayāb-/ 'to obtain, acquire, attain' continues Old Iranian *abi-āp- (preverb *abi- 'to, upon' + the root *(H)āp- of node 1). *abi- regularly loses its -b- before a vowel in Middle Persian and contracts to ay- (Nyberg: 'ay- probably < abi-, cf. Av. avi-ap-'); the root vowel is lengthened in the compound (ā-p-). The two stems Nourai lists are the standard Middle Persian stem pair: past ayāft (< *āpta-, with *pt > ft) beside present ayāb- (< *āpa-, with intervocalic *p > β > b). Manichaean MP has the same ʾyʾb-/ʾyʾpt, and Parthian shows the parallel pari-compound pryʾb-.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/یافتن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FFD:82\", \"status\": \"supports\", \"note\": \"FFD_pages.txt [pdf page 87] = printed p.82: 'یافتن — یافت < فارسی میانه ayāft < ایرانی باستان *abi-āp-ta-… ریشهٔ āp به معنی «به دست آوردن» است. یاب < فارسی میانه ayāb < ایرانی باستان *abi-āpa-' — both Pahlavi stems ayāft/ayāb, exactly as charted, and the root āp.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 17 s.v. ayāftan\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'ayāftan, ayāb- [ʾyʾp-tn' | M ʾyʾpt, ʾyʾb-, N yāftan, yāb-] obtain, acquire, attain'; also 'āyaft [ʾdypt' | M ʾypt, N āyift] boon, favour, gift'.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II p. ~34 s.v. ayāft\", \"stance\": \"supports\", \"note\": \"'ayāft [yʾpt'] gain, benefaction, from ayāftan ayāb-, to reach, to attain … NP yāftan yāb-. Av. ap-; āp- < ā- + ap-; ay- probably < abi-, cf Av. avi-ap-.' — this is the explicit statement that the Pahlavi verb is the abi- compound of Av. ap-.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"p. 162 s.v. *Hap/f\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: (+ *abi-) MMP ʾyʾb- \\\"to obtain, acquire, attain; to achieve success\\\", BMP ʾyʾp- /ayāb-/ \\\"to attain\\\"'; Inf. BMP ʾyʾptn /ayāftan/. Cheung keeps this verb (unlike abām) under *Hap.\"},\n            {\"src\": \"BRT\", \"where\": \"s.v. ap- and ayapta-\", \"stance\": \"partial\", \"note\": \"Bartholomae has the simple verb ap- (apayeiti) and the noun ayapta- 'Belohnung, Wunschgewährung'; the prefixed avi-ap- to which Nyberg points is his AiW col. 71. Our BRT.txt OCR of that column is too corrupt to quote verbatim.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"yâftan «یافتن» : to find ; yâbîdan «یابیدن» : to find\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP یافتن yāftan / یاب- yāb- is MP ayāftan / ayāb- with loss of the unstressed initial a- (the same aphaeresis as in awām > wām, node 3); the older ayāftan survives in Pahlavi Psalter and Manichaean spellings and in the noun آیفت āyift. The stem alternation yāft ~ yāb reflects *-pt- > -ft- versus intervocalic *-p- > -b-. یابیدن yābīdan is a late, secondary infinitive built inside New Persian on the present stem yāb- with the productive -īdan suffix (the same pattern as دانستن/دانیدن), not an independent inheritance — Nourai's box does not distinguish the two, which is a small imprecision but not an error of derivation. Semantically 'attain, obtain' > 'find' is already complete in Middle Persian.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/یافتن\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2419\", \"status\": \"supports\", \"note\": \"BQT vol.4 [pdf page 502] = printed p.2419, Mo'in's footnote 5: 'یافتن — بفتح چهارم، از: یاف (مادهٔ ماضی) + تن (پسوند مصدری). پهلوی ayāftan … اوستایی āp-, ap- (رسیدن) «اشتقاق ۱۱۲۶». هوبشمان گوید: فارسی یابم، یافتن = پهلوی ayāftan، از ریشهٔ āp …؛ پیدا کردن، بدست آوردن، کسب کردن.' — the Pahlavi antecedent and the Avestan root as charted.\"},\n            {\"ref\": \"FFD:82\", \"status\": \"supports\", \"note\": \"FFD_pages.txt [pdf page 87] = printed p.82 s.v. یافتن, as quoted at node 4: NP یافتن < MP ayāft, present یاب < MP ayāb.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 1124, p. 251\", \"stance\": \"supports\", \"note\": \"Horn: 'yāften \\\"erlangen, erreichen, erfinden\\\", Praes. yāb-em … aw. vergl. ayapta- \\\"Belohnung\\\"; phlv. āyāftan …, yāftan (Bund.), vergl. āyaft; oss. d. ba]yafun, t. ba]yafin \\\"einholen, erreichen\\\"'. Horn already has the Pahlavi ayāftan and the Avestan connection; he does not list yābīdan.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 17 s.v. ayāftan\", \"stance\": \"supports\", \"note\": \"MacKenzie explicitly equates the Pahlavi verb with 'N yāftan, yāb-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"pp. 161-163 s.v. *Hap/f\", \"stance\": \"supports\", \"note\": \"Cheung 2007 is the source Wiktionary cites for NP یافتن < MP ayāftan < *Habi- + *Hap- 'to reach, attain' < PIE *h₁ep-.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep for 'yäften|jäften|ayäftan' in HUB.txt returns nothing; Hübschmann's discussion (cited second-hand by Mo'in as 'هوبشمان ۱۱۲۶') is not recoverable from this OCR.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Latin\",\n          \"words\": \"apere : to bind, attach, reach ; aptus : fit, suited ; ad-apt-are : to fit, adapt ; ad-eptus : reached ; apex : something, reached, apex ; co-apere : bond together, couple\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin has the root in two guises: an obsolete *apiō, apere 'to fasten, bind, attach' (surviving in the imperative gloss ape 'prohibē, compescē' and in the participle aptus 'joined, fitted, suited'), and the inchoative apīscor, aptus sum 'to reach, get hold of', with the prefixed compound adipīscor, ad-eptus 'to attain, reach' (ad- + apīscor, with the regular weakening of medial a to e in an open syllable: ad+aptus > adeptus). From the participle aptus is built the denominative aptāre 'to fit', whence ad-aptāre 'to adjust, fit to'. Latin apex, apicis 'point, tip; the rod-like ornament on a priest's cap' is assigned to this root by Pokorny only with 'vielleicht' ('< something reached'), which is why Watkins prints it as sense 3 but Ernout-Meillet leave it doubtful. 'co-apere' is a reconstruction, not an attested Latin verb: what is attested is cōpula < *co-apula, a diminutive noun formed from the stem of apiō with co(m)- 'together'; Nourai's box would be more accurate as *co-ap- / cōpula.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/apt\",\n            \"https://www.etymonline.com/word/couple\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:50\", \"status\": \"supports\", \"note\": \"POK_01.txt ff-page 59-60 (printed 50-51): 'lat. apiscor \\\"fasse, erreiche\\\", adipiscor \\\"erlange\\\", coepi … Zusammenhang mit lat. *apiō, *apere \\\"comprehendere vinculo, verbinden, umbinden\\\" (imper. ape \\\"prohibe, compesce\\\"), aptus \\\"verknüpft, ausgestattet mit\\\", cōpula (co-apula) \\\"Band\\\" steht wohl fest … lat. apex, -icis \\\"Spitze\\\" … gehört vielleicht zu *apiō'. Every Latin word in Nourai's box is on the cited page.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ap-¹: '1. Latin apere, to attach, join, tie to … 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< \\\"something reached\\\"): APEX. 4. Prefixed form *co-ap- (co-, together; see kom) in Latin cōpula, bond, tie, link'. Watkins' gloss for apex, '< something reached', is literally Nourai's gloss.\"},\n            {\"ref\": \"KLN:22,24,96\", \"status\": \"supports\", \"note\": \"All three pages check out in KLN_1966.txt. p.22-23 (ff-leaf 23): 'adapt, tr. v. — F. adapter, fr. L. adaptare, \\\"to fit, adjust, adapt\\\", fr. ad- and aptare, \\\"to fit\\\", fr. aptus, \\\"fit\\\". See apt and cp. adept.' p.24 (ff-leaf 24, running head '24'): 'adept, adj. … L. adeptus, \\\"reached, attained\\\", pp. of adipisci … fr. ad- and apisci (pp. aptus) … which is rel. to OL. *apiō, apere, \\\"to bind, attach\\\", pp. aptus … For the change of Latin a (in aptus) to e (in adeptus) see accent.' p.96 (ff-leaf 62, which carries the printed page number 96): 'apt, adj., fit. — L. aptus, \\\"fitted, suited\\\", prop. pp. of obsol. apere, \\\"to fasten\\\", rel. to apisci, \\\"to reach after, attain\\\", and cogn. with OI. āpnoti … Hitt. epmi, \\\"I seize\\\". Cp. adapt, adept, apex, aptitude, attitude, inept, lariat, reata.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. apiō/apiscor (LAT.txt lines 4366-4398)\", \"stance\": \"supports\", \"note\": \"'Apiō a un inchoatif apiscor, -eris, aptus sum … Apiscor … a fourni les composés adipiscor, d'où adeptio … Le présent skr. āpnóti \\\"il atteint\\\" est déjà dans l'Atharvaveda … Le hittite epmi \\\"je prends\\\" … indique un ancien présent athématique que donnait à supposer lat. apio.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. I p. 45 f.\", \"stance\": \"supports\", \"note\": \"'Lat. apiscor \\\"fasse, erreiche\\\", adipiscor \\\"erlange\\\", coepi … Zusammenhang mit lat. *apio, *apere \\\"comprehendere vinculo\\\" … copula (co-apula) \\\"Band\\\", ammentum (aus *ap-mentom) … Vielleicht ist von einer gemeinsamen Grundbedeutung \\\"fassen, zusammenfassen\\\" auszugehen.'\"},\n            {\"src\": \"LEW\", \"where\": \"Walde LEW (1910) s.v. apiscor\", \"stance\": \"silent\", \"note\": \"grep -n 'apiscor' in LEW_1910.txt returns no hit; the a- fascicle is missing or unreadable in this OCR, so Walde's Latin dictionary could not be used directly (Ernout-Meillet was used instead).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"apt, aptitude ; adapt, adept, inept ; apex, attitude ; couple\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All eight words descend from the Latin material of node 6, mostly through French: apt (mid-14c.) from OFr. ate or directly from L. aptus; aptitude from Fr. aptitude < Late Latin aptitūdō; attitude (1660s) via Fr. attitude < It. attitudine < the same Late Latin aptitūdinem, so a doublet of aptitude (the -pt- > -tt- assimilation happened in Italian); adapt from Fr. adapter < L. adaptāre; adept from L. adeptus (the past participle of adipīscor, taken over as a noun/adjective in 17th-c. alchemical Latin adeptus 'one who has attained'); inept from L. ineptus (in- + aptus, with the same a > e weakening); apex directly from L. apex; couple (late 13c.) from OFr. cople < L. cōpula < *co-ap- 'to take together'.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/apt\",\n            \"https://www.etymonline.com/word/attitude\",\n            \"https://www.etymonline.com/word/couple\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. ap-¹ lists as English derivatives: 'APT, (APTITUDE), ATTITUDE; (INEPT) … ADEPT … APEX … COPULA, COPULATE, COUPLE'. Watkins' list and Nourai's box are the same set (Nourai adds ADAPT, which AHD subsumes under aptāre).\"},\n            {\"ref\": \"KLN:96\", \"status\": \"supports\", \"note\": \"KLN_1966.txt ff-leaf 62 (printed page 96) s.v. apt: 'Cp. adapt, adept, apex, aptitude, attitude, inept, lariat, reata.' The neighbouring entry 'aptitude, n., fitness. — F., fr. Late L. aptitūdō \\\"fitness\\\", fr. L. aptus. See apt and -tude and cp. attitude, which is a doublet of aptitude' is on the same leaf. For couple, Klein s.v. copula (KLN_1966.txt line 9141): 'copula, n. — L. copula, \\\"that which binds together, band, bond\\\", which stands for *co-apula, and is formed fr. co- and a dimin. from the stem of apio, apere, \\\"to join, fasten\\\". See apt and cp. couple.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 22, 24, 96 and s.v. copula\", \"stance\": \"supports\", \"note\": \"See the ref_check quotes; Klein covers every word of the box and derives them all from L. aptus/apere.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"grep for 'apt'/'balas' in SKT.txt returns no usable entry in this OCR (the file appears to be partial); no independent statement recoverable.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins appendix s.v. ap-¹\", \"stance\": \"supports\", \"note\": \"Same list as in ref_check — Nourai's English node is a transcription of Watkins' derivative list.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Apânk\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Avestan apāṅk- / apąnc- 'turned backwards, facing away' (= *apa 'away, behind' + *anč-/ak- 'to bend, be directed'; cf. Skt. apā́ñc- 'turned away, backward'); the sense 'north' belongs only to the derivative apāxtara-\",\n      \"verdict_note\": null,\n      \"note\": \"The root box is real but its gloss telescopes two stages. Avestan apāṅk- itself means 'turned backwards / directed away' (Buck: 'apāṅk- \\\"turned backwards\\\", adv. \\\"back\\\"'); 'north' is the meaning of the derived adjective apāxtara-/apāxaδra- 'northern', and it means 'north' only because of the Avesta's southern orientation, in which the north is 'the region behind you' and the abode of the daēvas and of hell. Language label 'Avestan' and the reference SYN:873 are both exact. The chart's real problems are further down: (a) the Balkh branch (nodes 3-4) attaches the city name Bactria/Balx to apāxtar, which no Iranist accepts; (b) the ruby chain (nodes 4-7) goes through Badaxšān, not Balx, as Mo'in's own footnote in Borhān says; (c) the Sogdian node is a cognate of axtar, not a derivative of apāṅk-, which Nourai's own note concedes. On the note at node 2, IEC:260: Mann does link Persian axtar with the 'star' root (see there), but Mann's supporting form 'Av. axtarō' is not an attested Avestan word, and the current view (Eilers, EIr III/2 p.123 s.v. AXTAR) is a backformation from abāxtar 'planet' — i.e. modern scholarship sides with Nourai's arrow, not with Mann.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/باختر\",\n        \"https://en.wiktionary.org/wiki/اختر\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"SYN:873\", \"status\": \"supports\", \"note\": \"SYN.txt ff-leaf 943, printed page 873 (the running head 'PLACE, FORM, SIZE 873' is on the same leaf), §12.47 NORTH: 'Av. apāxtara-, apāxaδra-, deriv. of apāṅk- \\\"turned backwards\\\", adv. \\\"back\\\", in accordance with the southern orientation in the Avesta. Barth. 79 f., 82.' Buck's page is exactly Nourai's root box, gloss included.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"apâxtar : north, north star ; axtar : star\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Middle Persian ʾpʾhtl /abāxtar/ continues Av. apāxtara- unchanged except for the regular lenition of intervocalic *p to β/b: *apāxtara- > abāxtar. In Pahlavi it is in fact two lemmas: ¹abāxtar 'planet' (the planets are the 'backward-moving' bodies, because of their retrograde motion, and in Zoroastrian cosmology they are demonic) and ²abāxtar 'the north'. Nourai's gloss 'north, north star' is therefore half right: the second sense is 'planet(s)', not 'north star' — MacKenzie: '¹abāxtar [ʾpʾhtl | M ʾbʾxtr] planet. ²abāxtar [ʾpʾhtl | (N bāxtar \\\"west\\\")] north'. The step abāxtar > axtar 'star, constellation, sign of the zodiac' that Nourai draws is a specific and defensible hypothesis, not a self-evident sound change: Eilers (EIr s.v. AXTAR, followed by Wiktionary) explains axtar as an old backformation from abāxtar 'planet', the initial ab- having been reanalysed as the privative prefix a(b)- — 'un-stars' — because Zoroastrianism treats the planets as maleficent non-stars. Both MacKenzie and Nyberg list axtar as an independent lemma without an etymology, so the arrow is a hypothesis they neither state nor contradict.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/اختر\",\n            \"https://en.wiktionary.org/wiki/باختر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SYN:870\", \"status\": \"partial\", \"note\": \"SYN.txt: printed p.870 (ff-leaf ~940) carries the §12.45 EAST / §12.46 WEST word-table; the §12.47 NORTH / §12.48 SOUTH table, which lists 'Av. apāxtara- (adj.)' as the Avestan word for 'north', is on the very next leaf (p.871), and the derivational statement is on p.873. So the citation is one to three pages short but the material is Buck's.\"},\n            {\"ref\": \"BQT:99\", \"status\": \"supports\", \"note\": \"BQT vol.1 ff-leaf 301 (printed p. ≈93-99 by the drifting leaf offset; the entry اختر with اخترستان/اخترشناس/اختر کاویان) — Mo'in's footnotes to that entry read '۳ (ستاره) «اونوالا ۳۳۰»' and '۴ پهلوی axtar؛ مینوی …', i.e. Pahlavi axtar 'star', citing Unvala's King Husrav glossary p.330. That is exactly Nourai's Pahlavi 'axtar: star'; Borhān gives no derivation of axtar from apāxtar.\"},\n            {\"ref\": \"FSF:58\", \"status\": \"supports\", \"note\": \"FSF_pages.txt ff-leaf 73-74 (≈ printed pp.57-58) s.v. باختر: quotes Marquart's Ērānšahr for '[شمال]' and Tārīkh-e Sīstān: 'هر چه حد شمال است باختر گویند و هر چه حد جنوب است نیمروز گویند … هر چه حد مشرق است خراسان گویند …', then notes that early poets sometimes use باختر for مشرق and خاور for مغرب. Noushin thus confirms the 'north' value that Nourai assigns.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 4 s.vv. ¹abāxtar, ²abāxtar; p. 16 s.v. axtar\", \"stance\": \"partial\", \"note\": \"'¹abāxtar [ʾpʾhtl | M ʾbʾxtr] planet. ²abāxtar [ʾpʾhtl | (N bāxtar \\\"west\\\")] north.' and separately 'axtar [ʾhtl | M ʾxtr, N ~] star, constellation, sign of the zodiac.' MacKenzie confirms both words but keeps them apart and glosses the second abāxtar 'planet', not 'north star'.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II p. 20 s.v. apaxtar; p. 33 s.v. axtar\", \"stance\": \"partial\", \"note\": \"'apaxtar [ʾpʾhtl] 1. planet … 2. the north. — Av. apāxtara- \\\"northern\\\"; MPrs ʾbʾxtr; Paz. awāxtar; NP bāxtar \\\"the west\\\" or \\\"the east\\\".' and 'axtar [ʾhtl] constellation, one of the signs of the Zodiac … MPrth/Prs ʾxtr; Paz. NP axtar.' Nyberg confirms apāxtara- > abāxtar but gives axtar no etymology and does not link the two.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 79 f., 82 (as cited by Buck)\", \"stance\": \"partial\", \"note\": \"BRT.txt's OCR of the apāxtara- column is unusable, but the word is quoted in the citation apparatus of other entries, e.g. 'apaxtarat haca ⁺mat V.19.1, H.2.25, FrW.10.43' under naēma- 'side, half' — i.e. Avestan apāxtara- 'northern side' is attested in the Vidēvdād, as Bartholomae 79 f. states.\"},\n            {\"src\": \"IEC\", \"where\": \"Mann, s.v. oster- (osteren-, ster-) 'star' (IEC.txt ff-leaf 156)\", \"stance\": \"contradicts\", \"note\": \"'oster- (osteren-, ster-) \\\"star\\\". WP II, 635 … Av. stārō, acc. stārəm beside axtarō, id.; Per. sitāre, axtar' — Mann files Persian axtar under the PIE 'star' root, i.e. exactly the alternative Nourai flags at node 2. Mann's 'Av. axtarō' is however not an attested Avestan word, and no other authority repeats it.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"bâxtar «باختر» : north ; axtar «اختر» : star, fate\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP باختر bāxtar is MP abāxtar with the usual New Persian aphaeresis of the unstressed initial a- (compare abām > wām at entry 0 node 3; here ab- > b-). The semantic history is the problem: in the Avesta and in Pahlavi the word means 'north', and Ferdowsi and the Tārīkh-e Sīstān still use it that way ('هر چه حد شمال است باختر گویند'), but in New Persian generally — and in the modern standard language exclusively — باختر means 'west', paired against خاور 'east'; a few early poets even reverse the pair and use باختر for 'east'. Mo'in states this explicitly. Nourai's gloss 'north' is therefore the correct oldest sense but not the ordinary Persian one, which is why MacKenzie and Nyberg gloss the New Persian reflex 'west' / 'the west or the east'. NP اختر axtar 'star, constellation; horoscope, fortune' is MP axtar unchanged; the 'fate/fortune' sense is a natural astrological extension already visible in the Pahlavi compound axtar-mār 'astrologer' and in Ferdowsi's line quoted in the chart ('نبینم همی اختر خویش بد'), and it survives in the derivative اخترشناس axtar-šenās 'astronomer/astrologer' that Nourai lists.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/باختر\",\n            \"https://en.wiktionary.org/wiki/اختر\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:99\", \"status\": \"partial\", \"note\": \"The اختر half is confirmed at BQT vol.1 ff-leaf 301 (see node 1): 'اختر … رایت و علم را گویند، و بمعنی بخت و طالع هم هست، و کوکب و ستاره را نیز گویند، و بمعنی فال و شگون هم آمده است' — precisely Nourai's 'star, fate'. The باختر half is NOT on that page: in this scan باختر stands at ff-leaf 424 (≈ printed p.204), where Mo'in's footnote reads 'در اوستا apāxtara- بمعنی شمال آمده و آنجا جایگاه اهریمن و دیوان و مکان دوزخ دانسته شده «خرده اوستا ۸۷»؛ در پهلوی نیز abāxtar آمده بدین معنی و نیز بمعنی سیاره؛ در زبان فارسی اکثر بمعنی مغرب آمده در برابر خاور، ولی گاه نیز بعکس …'.\"},\n            {\"ref\": \"FSF:58\", \"status\": \"supports\", \"note\": \"FSF_pages.txt ff-leaf 73-74 s.v. باختر, quoted at node 1: Noushin's Shāhnāme glossary explicitly glosses باختر 'شمال' with Marquart and the Tārīkh-e Sīstān, which is Nourai's gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. باختر (MON_part1.txt line 19730)\", \"stance\": \"partial\", \"note\": \"'باختر: در اوستا اپاختره به معنی شمال آمده و جایگاه اهریمن و دیوان و دوزخ دانسته شده، در پهلوی نیز اباختر بدین معنی و نیز به معنی سیاره آمده. در زبان فارسی اکثر به معنی مغرب استعمال می‌شود، در برابر خاور؛ ولی گاه نیز به عکس، باختر به معنی مشرق و خاور به معنی مغرب آمده.' Supports the Avestan→Pahlavi→Persian chain; warns that the ordinary Persian sense is 'west'. Mo'in's اختر entry (line 8287) gives only glosses ('ستاره، جرم فلکی، کوکب؛ ستارهٔ بخت و اقبال … درفش، علم، رایت'), no etymology.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II p. 20 s.v. apaxtar\", \"stance\": \"partial\", \"note\": \"'NP bāxtar \\\"the west\\\" or \\\"the east\\\"' — Nyberg records the New Persian meanings as west/east, not north.\"},\n            {\"src\": \"PHD\", \"where\": \"p. 4 s.v. ²abāxtar\", \"stance\": \"partial\", \"note\": \"MacKenzie's bracket '(N bāxtar \\\"west\\\")' gives the same warning about the New Persian value.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. oster-/ster- 'star'\", \"stance\": \"contradicts\", \"note\": \"Mann's linkage of Persian axtar with sitāre and the *ster- root (the dispute recorded in Nourai's own NOTE) — see node 1. Modern scholarship (Eilers, EIr III/2 123; Wiktionary s.v. اختر) rejects it in favour of the backformation from abāxtar, i.e. it sides with Nourai's chart against Mann.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"bâxtri, bâxr, balx : a city north of the ancient Iran\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The city and province name is genuinely old — Old Persian Bāxtriš (Bisotun I.16, in the list of satrapies), Avestan Bāxδī-/Bāxtrī-, Greek Βακτρία/Βάκτρα, Middle Persian Baxl [bʾhl], New Persian Balx — but it has nothing to do with apāxtar 'north'. Its own etymology is unsettled (it is not a transparent Iranian formation); the -xtr- of Bāxtriš and the -xtar of abāxtar look alike only by accident, since abāxtar is *apa- plus a comparative-type suffix, while Bāxtriš has no *apa- and no -tara-. The Middle Persian development *Bāxδī > Baxl (with -δ-/-r- > -l-) then NP Balx is entirely different from abāxtar > bāxtar. Nourai's middle form 'bâxr' is not an attested word: the Pahlavi form is Baxl (Nyberg, glossary p.72 s.v. Baxl), and 'bâxr' is almost certainly a slip for bâxl. Verdict: the node's words are (with that correction) real, but the edge apāxtar → Bāxtrī/Balx is rejected.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Bactria\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:275\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang vol. 5 (اعلام, proper names) is not in the local library and not online: the two local Mo'in files (MON_part1/part2, the 2-volume Adena edition) are the lexicon volumes only and contain no بلخ article; vajehyab/abadis expose only the lexicon volumes.\"},\n            {\"ref\": \"BQT:297\", \"status\": \"partial\", \"note\": \"BQT vol.1 ff-leaf 517 (≈ printed pp.293-297) does carry the headword بلخ: 'بلخ — بفتح اول و سکون ثانی و خای نقطه‌دار، نام شهری است مشهور از خراسان و آن از شهرهای قدیم است همچو استخر فارس، و آن را قبةالاسلام خوانند و لقب آن بامی است؛ گویند برامکه از آنجا بوده‌اند …'. So the page reference is right, but Borhān/Mo'in give the city no etymology at all, and certainly not a derivation from apāxtar.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"NYB\", \"where\": \"vol. II p. 72 s.v. Baxl\", \"stance\": \"contradicts\", \"note\": \"'Baxl [bʾhl] Balkh 113². — Av. Bāxtrī-, Bāxδī-; NP Balx.' Nyberg derives Balkh from the Avestan country name Bāxδī-/Bāxtrī-, not from apāxtara-, and his Pahlavi form is Baxl (not Nourai's 'bâxr'). The cross-reference list in the same volume has 'Bāxtri: Baxl'.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, DB I.16 and lexicon\", \"stance\": \"contradicts\", \"note\": \"Kent's text of Bisotun I.16 reads '… Parθava : Zraka : Haraiva : Uvārazmiy : Bāxtriš : Suguda : Gadāra …' and the paradigm sections give Abl./Loc. sg. Bāxtriyā. Old Persian already has Bāxtri- in the 6th c. BCE, with no trace of an *apa- preverb.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. Bāxδī-\", \"stance\": \"silent\", \"note\": \"The Bāxδī- column is not recoverable from BRT.txt's OCR; no direct quotation possible.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"balx «بلخ» : an ancient city in Iran famous for its rose-red ruby gems\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP بلخ Balx < MP Baxl < Av. Bāxδī-/OP Bāxtriš is a sound chain, but the second half of the gloss is wrong and it is what carries the rest of the chart: the rose-red spinel of the medieval gem trade is the stone of بدخشان Badaxšān, the district on the upper Oxus in what is now north-eastern Afghanistan, not of Balkh. The gem name is بلخش balaxš ~ بلخشان balaxšān, a variant of بدخشان (Nourai lists both in his script extras). Mo'in himself, in the footnote to بدخش in the very dictionary Nourai cites, quotes Barthold (EI s.v. Badaxšān) and Marquart (Ērānšahr 279) to exactly this effect and says that balaxš was probably first the name of the district and only later of the stone found there. The similarity of Balx and balaxš is coincidental (and encouraged the medieval confusion), so the arrow Balx → Arabic balaxš is rejected.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/balas\",\n            \"https://www.ahdictionary.com/word/search.html?q=balas\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON5:247\", \"status\": \"not_checked\", \"note\": \"As at node 3: Mo'in's vol. 5 (اعلام) is not available locally or online; the local Mo'in lexicon files have no بلخ article.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol.1 ff-leaves 462-463 (≈ printed pp.240-241) s.v. بدخش / بدخشان\", \"stance\": \"contradicts\", \"note\": \"Mo'in's footnote 8: 'مارکوارت (Ērānšahr) گوید که بدخشان بمعنی «بلاد بذخش balaxš» است و آن نوعی است از یاقوت که گویند جز در بدخشان … یافت نشود. اما کاملاً محتمل است که کلمهٔ بلخش balaxš (که کلمهٔ فرانسه balais و انگلیسی balas از آن مأخوذ است) در آغاز نام ناحیت مورد بحث بوده و بعدها به لعلی که در آن ناحیت یافت شود اطلاق شده باشد. «بارتولد، دائرةالمعارف اسلام: بدخشان»'. Mo'in states the whole chain balaxš > balais > balas and roots it in Badaxšān, not Balx.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 142 s.v. balas\", \"stance\": \"contradicts\", \"note\": \"'balas, n., a variety of spinel ruby. — F. balais, fr. Arab. balakhsh, fr. Balakhshān, fr. Pers. Badhakhshān, name of a region in Central Asia (near Samarkand), where this variety of spinel ruby is found.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 151 (Badaḫšān)\", \"stance\": \"contradicts\", \"note\": \"Lokotsch: 'N. pr. Name des nordöstlichen Teiles des heutigen Afġānistān. Von hier bezog man in früheren Zeiten Edelsteine … Über das ar. balaḫš ergab sich als Bezeichnung für eine Rubinart mlat. balascius, it. balascio, balasso, sp. balaju, balaja, pg. balais, kat. balaix, frz. prov. balais; dtsch. Ballasrubin. [Devic DE 233. ML 891.]'\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, ff-leaf 27 s.v. بدخشان\", \"stance\": \"partial\", \"note\": \"'(اللقار) وهو … في بلخشان، والعجم يقولون له بدخشان (شفاء الغليل) … بدخشان … بلاد بين خراسان وهندستان فيها معادن الذهب والأحجار الكريمة (البرهان القاطع)' — the Arabic tradition itself equates بلخشان with بدخشان and locates the gem mines there; Balkh is not mentioned.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Arabic\",\n          \"words\": \"balaxš : ruby\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic بَلَخْش balaḵš 'balas ruby, rose-red spinel' is real and is indeed the form from which the European words were taken, so the node itself is right and its position between the Persian and the Old French node is right. What is wrong is its parent: Arabic balaḵš is a borrowing of Persian بلخش balaxš, a shortened/dissimilated variant of بدخشان Badaxšān (the gem-bearing district), not of بلخ Balx. Arabic geographers write both بلخشان and بدخشان for the same place (Addi Shir, quoting Šifāʾ al-ġalīl: 'والعجم يقولون له بدخشان'), which shows the two are the same name; the stone was then named for its provenance, the standard pattern for medieval gem names. Since Arabic balaḵš is not a native Semitic root formation but a place-name loan, the label 'Arabic' is best read as 'Arabic transmission of a Persian toponym'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/balas\",\n            \"https://www.ahdictionary.com/word/search.html?q=balas\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:101\", \"status\": \"partial\", \"note\": \"Checked in the online American Heritage Dictionary (the local AHD file holds only the Watkins IE appendix). AHD s.v. balas: 'A rose-red to orange spinel used as a semiprecious gem, once confused with the ruby. [Middle English, from Old French balais and Old Spanish balax, from Medieval Latin balascus, from Arabic balaḫš, from Persian Badakhshān, a region in northeast Afghanistan.]' The Arabic form and the route are exactly as charted; the Persian source given by AHD is Badakhshān, not Balx, so the reference supports the node but contradicts its parent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 142 s.v. balas\", \"stance\": \"partial\", \"note\": \"'F. balais, fr. Arab. balakhsh, fr. Balakhshān, fr. Pers. Badhakhshān' — Klein has the Arabic word but inserts Balaxšān and Badaxšān above it.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, s.v. Balais (Rubis)\", \"stance\": \"partial\", \"note\": \"'Balais (Rubis). Esp. balax, balaxo, balaja; portug. balax, ital. balascio, bas lat. balascius. De l'arabe بلخش balakhch, venant du persan بدخشان badakhchân, nom du pays d'où l'on tire ces gemmes. … Marco Polo appelle ce même pays Balasian et les rubis balaxi ou balasci.'\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir ff-leaf 27\", \"stance\": \"supports\", \"note\": \"Attests بلخشان alongside بدخشان in the Arabic lexicographical tradition (see node 4), i.e. an Arabic balaḵš- form of the toponym.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep for balaḫš/balahs/Badaḫšān in PLA_asbaghi_1988_ia_djvu.txt returns nothing; Asbaghi does not list this word.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Old French\",\n          \"words\": \"balais : ruby\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old French balais (also rubis balais), 13th c., is the Arabic balaḵš adapted to French phonology: the Arabic cluster -ḵš is simplified and the word is refashioned with the productive adjectival ending -ais (as in the parallel Medieval Latin balascius, Italian balascio/balasso, Spanish balax/balaja, Catalan balaix, Portuguese balais). It reached the West through the Levantine gem trade — Marco Polo already calls the country Balasian and the stones balaxi/balasci. In French the word is an adjective qualifying rubis, exactly as in English 'balas ruby'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/balas\",\n            \"https://www.ahdictionary.com/word/search.html?q=balas\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:101\", \"status\": \"supports\", \"note\": \"AHD s.v. balas: '[Middle English, from Old French balais and Old Spanish balax, from Medieval Latin balascus, from Arabic balaḫš …]' — the Arabic→Old French step is precisely Nourai's arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHN\", \"where\": \"Pihan, s.v. BALAIS, adj. m. (p.)\", \"stance\": \"supports\", \"note\": \"Pihan lists BALAIS among the French words of Persian origin and gives 'balais, en persan بدخشان badakhchân'.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, s.v. Balais (Rubis)\", \"stance\": \"supports\", \"note\": \"'De l'arabe بلخش balakhch, venant du persan بدخشان badakhchân, nom du pays d'où l'on tire ces gemmes' — Arabic to French, as charted.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 151\", \"stance\": \"supports\", \"note\": \"'Über das ar. balaḫš ergab sich als Bezeichnung für eine Rubinart … frz. prov. balais; dtsch. Ballasrubin.'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 142 s.v. balas\", \"stance\": \"supports\", \"note\": \"'F. balais, fr. Arab. balakhsh'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"balas : a rose-red gem\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle English balais/bales, borrowed from Old French balais (with support from Old Spanish balax and Medieval Latin balascus), gives modern English balas, now used almost only attributively in 'balas ruby'. The referent is a rose-red to orange spinel, distinguished from true ruby only after the 18th century — which is why the older English texts treat it as a kind of ruby, exactly Nourai's gloss 'a rose-red gem'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/balas\",\n            \"https://www.ahdictionary.com/word/search.html?q=balas\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:101\", \"status\": \"supports\", \"note\": \"AHD s.v. balas: 'A rose-red to orange spinel used as a semiprecious gem, once confused with the ruby. [Middle English, from Old French balais …]' — gloss and immediate parent as charted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 142 s.v. balas\", \"stance\": \"supports\", \"note\": \"'balas, n., a variety of spinel ruby. — F. balais …'\"},\n            {\"src\": \"AHD\", \"where\": \"online dictionary s.v. balas\", \"stance\": \"supports\", \"note\": \"See ref_check; the online AHD is the current edition of the dictionary whose 1975 New College page 101 Nourai cites.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\", \"note\": \"No 'balas' entry recoverable from SKT.txt (grep returns nothing).\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Sogdian\",\n          \"words\": \"anxar, `ngr : star\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Sogdian ʾnγr /anɣar/ 'star' is correctly cited (Gharib no. 1008, Buddhist Sogdian, attested in the Vessantara Jātaka and in the Paris Sogdian texts), and the compounds confirm the meaning: no. 1014 ʾnγrksʾy anɣar-kase 'astrologer' and no. 1017 ʾnγrwzn anɣar-wazan 'zodiac, constellation', which Gharib himself equates with Parthian axtar-wazan. That equation is the point: Sogdian anɣar corresponds to Middle Persian/Parthian axtar, so it belongs with node 1's axtar, not directly under Avestan apāṅk-, and Nourai's own note ('This may be a cognate rather than a derivative') concedes as much. Gharib offers only a tentative *ana-har with a question mark; a derivation from *apāṅk-/*apāxtara- would not yield Sogdian ʾnγr (there is no trace of the *p and no *-tar- suffix). So: the word and gloss are right, the drawn edge is not a derivation but at best a cognate relation.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:39\", \"status\": \"supports\", \"note\": \"SOD_pages.txt, entry '1008 ʾnγr B — anxar ⊙<*ana-har ? ⊙pl. -t =ʾnxr — star. VJ 25, 17; TSP 3.148, 150; Andreas, SPAW 1910, 310'. The leaf carrying entries 993-1014 has the printed page number 40 in its footer, so entry 1008 sits on printed p.39/40 — Nourai's SOD:39 is right (as a page, not an entry number). Neighbours: '1014 ʾnγrksʾy … anxar-kase, astrologer' and '1017 ʾnγrwzn … anxar-wazan ⊙Parth. axtar-wazan … zodiac, constellation'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 1008, 1014, 1017 (printed pp. 39-40)\", \"stance\": \"partial\", \"note\": \"Confirms the form and the gloss 'star', but proposes '<*ana-har ?' — not a derivation from apāṅk- — and equates the compound anxar-wazan with Parthian axtar-wazan.\"},\n            {\"src\": \"NYB\", \"where\": \"vol. II s.vv. apaxtar, axtar\", \"stance\": \"partial\", \"note\": \"Nyberg keeps Middle Persian axtar and apaxtar apart; the Sogdian word matches the former, so it cannot be a direct derivative of the Avestan apāṅk- root box.\"},\n            {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Khotanese dictionary\", \"stance\": \"silent\", \"note\": \"No Khotanese cognate of anɣar found; nothing bearing on this node.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-04T23:01:31.132Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-58.json (file state is current in your context — no need to Read it back)
```


## [2026-09-04T23:01:36.274Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-58.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 58",
 "description": "validate and run verify_check"
}
```


### [2026-09-04T23:01:38.957Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 18, 'not_found': 3, 'not_checked': 3, 'partial': 4}
books consulted: {'supports': 26, 'silent': 9, 'contradicts': 8, 'partial': 14} | by book: {'NYB': 7, 'PHD': 6, 'CHEUNG': 5, 'KLN': 5, 'BRT': 4, 'AHD': 3, 'HRN': 3, 'WLD': 2, 'KNT': 2, 'HUB': 2, 'SKT': 2, 'IEC': 2, 'LKT': 2, 'AFM': 2, 'DEV': 2, 'LAT': 1, 'LEW': 1, 'MON': 1, 'BQT': 1, 'PLA': 1, 'PHN': 1, 'SOD': 1, 'ISS_alt_DKS': 1}
```


## [2026-09-04T23:01:44.851Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-58.json'\nd=json.load(open(p))\nd['entries'][1].pop('verdict_note',None)\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=2)\nEOF\npython3 tools/verify_archive_sources.py 2>&1 | tail -20",
 "description": "tidy json and check archived sources"
}
```


### [2026-09-04T23:01:50.656Z] TOOL RESULT

```
465 cited URLs, 26 not yet archived
archived 26, failed 0
```


## [2026-09-04T23:01:55.516Z] TOOL CALL #94: Bash

```json
{
 "command": "python3 tools/verify_check.py 58 && python3 -m json.tool data/verification/page-58.json >/dev/null && echo \"JSON OK\"; git status --short",
 "description": "final check"
}
```


### [2026-09-04T23:01:58.433Z] TOOL RESULT

```
nodes verified: 15/15
node verdicts: {'plausible': 5, 'disputed': 3, 'confirmed': 7}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 18, 'not_found': 3, 'not_checked': 3, 'partial': 4}
books consulted: {'supports': 26, 'silent': 9, 'contradicts': 8, 'partial': 14} | by book: {'NYB': 7, 'PHD': 6, 'CHEUNG': 5, 'KLN': 5, 'BRT': 4, 'AHD': 3, 'HRN': 3, 'WLD': 2, 'KNT': 2, 'HUB': 2, 'SKT': 2, 'IEC': 2, 'LKT': 2, 'AFM': 2, 'DEV': 2, 'LAT': 1, 'LEW': 1, 'MON': 1, 'BQT': 1, 'PLA': 1, 'PHN': 1, 'SOD': 1, 'ISS_alt_DKS': 1}
JSON OK
 M data/verification/page-31.json
 M data/verification/page-41.json
 M data/verification/sources/web/index.jsonl
?? data/verification/page-57.json
?? data/verification/page-58.json
?? data/verification/sources/web/5278f9daaa5c815e.txt
?? data/verification/sources/web/6231bec4e9852e14.txt
?? data/verification/sources/web/839e73f53001405e.txt
?? data/verification/sources/web/8b2dbd2897dcdca6.txt
?? data/verification/sources/web/8b75eadffac56d40.txt
?? data/verification/sources/web/9c67fcb024e6c3fd.txt
?? data/verification/sources/web/9d8f72780bec0a2e.txt
?? data/verification/sources/web/adae17388b0f3fec.txt
?? data/verification/sources/web/b5cfaf64341d0817.txt
```


## [2026-09-04T23:02:21.397Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-58.json` written; `verify_check.py 58` reports 15/15 nodes, no PROBLEM lines.

**PDF page 58 (book p. 28) — 2 charts (entry 1 is the `Apâ → Apo` redirect, skipped)**

- Root verdicts: confirmed 1 (`Ap 2`), plausible 1 (`Apânk`)
- Node verdicts: confirmed 7, plausible 5, disputed 3
- Ref checks: supports 18, partial 4, not_found 3, not_checked 3 · Books consulted: 23 titles (supports 26, partial 14, contradicts 8, silent 9)

Disputed / problem items:

- **Ap 2 › #2 Pahlavi `apâm, avâm` "loan"** — Cheung 2007 (pp. 162, 177f) removes MP *abām* from *Hap "reach" and files it under *Hmai¹ "to exchange" (*apa-mai-, cf. Skt. *apa-mitya-* "debt", Sogd. *pʾmytʾy*, Bactr. βαμδοιγο), calling Nyberg's *(ā-)apamna- "less convincing". Nourai follows Nyberg/Mo'in (BQT:2254 quotes *āpamna-* verbatim).
- **Apânk › #3 Pahlavi `bâxtri, bâxr, balx`** — Bactria/Balkh is OP *Bāxtriš* (Kent, DB I.16), Av. *Bāxδī-*, MP *Baxl* (Nyberg 954), unrelated to *apāxtar* "north"; also `bâxr` is unattested and is almost certainly a slip for *bâxl*.
- **Apânk › #4 Persian `balx`** — the balas ruby comes from **Badaxšān**, not Balkh: Mo'in's own footnote in Borhān s.v. بدخش (≈p.240, citing Barthold/Marquart) states *balaxš* > Fr. *balais* > Eng. *balas* and roots it in Badaxšān; Klein 142, AHD, Devic, Pihan, Lokotsch 151 agree.

Other notable findings: Nourai's `abi-âp : to detain` is his own misprint for "to obtain" (verified on the rendered PDF page — the JSON transcription is faithful, so no `transcription_suspect`); his note "HRN:31 does not agree" is only half right (Horn p.31 rejects *Darmesteter's* apa+em- analysis, not the ap- route); and his chart's NOTE about IEC:260 checks out — Mann does link *axtar* to *ster-*, but modern scholarship (Eilers, EIr III/2 123, via Wiktionary) instead backforms *axtar* from *abāxtar* "planet", i.e. it sides with Nourai. NP *bāxtar* "north" is the classical sense only; MacKenzie, Nyberg and Mo'in all note the ordinary Persian value is "west".
