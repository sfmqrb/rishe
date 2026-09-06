# Verification process log — verify-page-178


## [2026-09-05T20:51:53.209Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 178 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-178.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-178.json. Write /home/sfmqrb/git/rishe/data/verification/page-178.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 178` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:51:54.982Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:51:55.563Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:51:55.575Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe/data/verification/agent/charts/page-<pdf>.txt`.
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
38	   - `transcription_suspect` — the form in the JSON is not what the sources know (a misread
39	     letter, an impossible form, a wrong Persian script). See "Transcription flags" below:
40	     you must check the printed page and say whether the book or the extraction is at fault.
41	4. Record sources as URLs (Wiktionary page, Etymonline page, AHD appendix entry, archive.org
42	   page of Klein/Horn/Bartholomae, etc.). Also note when Nourai's own cited reference
43	   (KLN, POK, AHD, BQT, MON, HRN, HUB…) is itself the modern standard for that claim.
44	
45	## Checking Nourai's OWN cited references (required)
46	
47	Every node carries `refs=` — Nourai's citations, e.g. `KLN:164; FVQ:75` (abbreviation:page;
48	`MON5:528` = MON vol. 5 p. 528). The author claims each arrow is supported by those pages.
49	You must check them:
50	
51	- The bibliography key (abbreviation → book), where each reference can be read, page
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe/tools/ref_page.py BQT:918 --image`
64	  It renders that one page to PNG, OCRs it (Persian OCR is rough), caches both under
65	  `data/verification/sources/refs/ocr/`, and prints the text plus the PNG path. If the OCR
66	  is unreadable, Read the PNG (you can read Persian print directly), and then SAVE what you
67	  read: write the entry/entries you used (headword, Mo'in's etymological footnote, and any
68	  surrounding lines you relied on) verbatim to the companion file
69	  `data/verification/sources/refs/ocr/<ABBR>/<page>.vision.txt` (the tool prints the exact
70	  paths). The tool prefers that file next time, so nobody pays for reading the image again.
71	  If the printed page number on the image is off, re-run with `--pdf-page <n>` adjusted, and
72	  note the correct pdf page in your ref_check note. Borhan vol. 5 (the addenda, own
73	  pagination 1–290) is reached only as `BQT5:<page>`; Borhan vols 1–2 exist as OCR text
74	  files (`BQT_v1_pages.txt`, `BQT_v2_pages.txt`), vols 3–5 as `BQT_v3/4/5_pages.txt` too.
75	- If `kind` is `website`, use the `lookup_hint` URL pattern with WebFetch (e.g. Mo'in via
76	  vajehyab.com / abadis.ir).
77	- Do this for at least ONE cited reference per node (the most authoritative available:
78	  POK/AHD/KLN for IE roots, HRN/HUB/BRT/KNT/PHD for Iranian, KLN/FVQ/AFM/PLA for Semitic,
79	  BQT/MON for Persian). If none of a node's references is accessible, say so.
80	
81	Add to every node a `ref_check` array:
82	
83	```json
84	"ref_check": [
85	  {"ref": "KLN:164", "status": "supports", "note": "Klein p.164 s.v. 'cherub': Heb. kerūbh, prob. rel. to Akkad. karābu 'to bless', metathesis of b-r-k — exactly Nourai's claim."},
86	  {"ref": "FVQ:75", "status": "not_checked", "note": "no online copy"}
87	]
88	```
89	
90	`status` ∈ `supports` (the page says what the arrow says) · `partial` (the reference has the
91	word but a different/looser derivation) · `contradicts` (the reference says something else)
92	· `not_found` (checked the text, could not find the entry/page) · `not_checked` (reference
93	not accessible online). Quote the key phrase of the reference in `note` when you can, with
94	the file/leaf/page where you found it.
95	
96	Also add to each entry a root-level `ref_check` for the root's own refs (e.g. `POK:244`).
97	
98	## Use EVERY relevant book on disk (required)
99	
100	Checking only the reference Nourai cites is not enough. For every node, also consult the
101	other books in the local library that could speak to that claim, and record what each says.
102	The list of which books cover which kind of node, with file paths, is
103	`/home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
104	
105	- an Indo-European node or root box: Pokorny (POK) AND Walde-Pokorny (WLD) AND Watkins/AHD,
106	  plus Mann (IEC) or Buck (SYN) when the word is a common noun;
107	- an Avestan / Old Persian node: Bartholomae (BRT) or Kent (KNT);
108	- a Pahlavi / Middle Persian node: MacKenzie (PHD) and Nyberg (NYB);
109	- a New Persian node: Horn (HRN), Hübschmann (HUB), Cheung (CHEUNG, for verbs), Borhan-e
110	  Qate' with Mo'in's footnotes (BQT), Mo'in (MON), and Aryanpur (ARY);
111	- a Sogdian node: Gharib (SOD); a Khotanese one: Bailey (ISS_alt_DKS);
112	- an Arabic node or a Persian/Arabic loan in either direction: Klein (KLN), Jeffery (FVQ),
113	  Addi Shir (AFM), Asbaghi (PLA), Fraenkel (AFA), Lokotsch (LKT); for French/Spanish
114	  Arabisms Pihan (PHN), Devic (DEV), Lammens (LAM), Dozy (DOZ);
115	- an English / Romance node: Klein (KLN), Skeat (SKT), Funk & Wagnalls (FSD), Webster (WEB);
116	  Anglo-Indian words: Hobson-Jobson (HJB), Whitworth (AID);
117	- a Turkic node: Vámbéry (TTS), Lokotsch (LKT).
118	
119	Grep each file for the headword (several spellings; Latin transliteration for the Western
120	books, Persian script for BQT/MON/ARY, Pahlavi transliteration for PHD/NYB). A grep that
121	finds nothing is also a result ("silent"). Record everything in a `consulted` array on the
122	node (separate from `ref_check`, which is only for the references Nourai himself cites):
123	
124	```json
125	"consulted": [
126	  {"src": "HRN", "where": "no. 3, p. 1", "stance": "contradicts", "note": "Horn separates āb 'Glanz' from āb 'water' and derives āftāb from the former"},
127	  {"src": "PHD", "where": "p. 5 s.v. ābād", "stance": "supports", "note": "'ābād [ʾpʾt] populous, thriving' — no water element"},
128	  {"src": "WLD", "where": "Bd. I p. 46", "stance": "silent", "note": "root ap- listed, no Persian compound"}
129	]
130	```
131	
132	`stance` ∈ supports / contradicts / partial / silent. Quote the key phrase. Books consulted
133	via the web (vajehyab for Mo'in, AHD online) go here too, with the URL archived via
134	fetch_source.py and listed in `sources`. Every node must have at least two `consulted`
135	entries from different books whenever the matrix lists two or more books for its language.
136	
137	## Transcription flags: say WHERE the error is (required)
138	
139	For every node you mark `transcription_suspect`, look at the printed page itself — render it
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
141	(or open `site/pages/<pdf page>.jpg`) and Read the image — and add to the node:
142	
143	```json
144	"error_in": "book",            // "book" = the printed book has the odd form (author's misprint); the extraction is faithful
145	                               // "extraction" = the book prints the correct form; the JSON misread it
146	                               // "unknown" = could not decide from the image
147	"book_prints": "borrāgō",      // what the printed page actually shows
148	"correct_form": "borrāgō"      // the form that should stand (per the sources)
149	```
150	
151	Usually the extraction is faithful and the problem is in the book itself; say so plainly in
152	`derivation` too ("the book prints X; this is Nourai's misprint for Y"). Only when the JSON
153	differs from the page is it an extraction error (report those separately in your summary — the
154	owner fixes the data). Copy the page PNG you relied on to
155	`data/verification/sources/refs/ocr/BOOK/<pdf page>.png` so the check can be audited.
156	
157	## Persian explanation (required): `derivation_fa` on every node, `note_fa` on every root
158	
159	Write the derivation a second time IN PERSIAN, for a Persian reader — not a translation of the
160	English sentence. Think about how a Persian etymologist (حسن‌دوست، ابوالقاسمی، معین در حواشی
161	برهان قاطع) would explain it to an educated Persian reader:
162	
163	- Use the established Persian terminology: هندواروپایی آغازین، ایرانی باستان، اوستایی، پارسی
164	  باستان، فارسی میانه (پهلوی)، پارتی، سغدی، فارسی نو/دری؛ وام‌واژه، وام‌گیری، دگرگونی آوایی،
165	  قلب (metathesis)، ابدال، همگونی، پیشوند، پسوند، ریشه، ستاک، تحول معنایی، معرّب، ریشه‌شناسی
166	  عامیانه (folk etymology)، هم‌ریشه (cognate)، دوگانه (doublet).
167	- Give the Persian word first in Persian script, then the older forms in Latin transliteration
168	  as Persian philology does (e.g. «آب» از فارسی میانهٔ āb / āp، از ایرانی باستان *āp-، هم‌ریشه با
169	  سنسکریت āp-). Persian-script forms for Arabic words; Greek/Latin words in Latin letters.
170	- Explain the sound changes in the way a Persian reader expects (e.g. «پ ایرانی باستان در میان
171	  دو واکه در فارسی میانه به ب نرم شده»؛ «ای کشیدهٔ فارسی میانه در فارسی نو به ی بدل شده»).
172	- Say clearly, in Persian, what the verdict means for the reader: ادعای نورایی درست است / با
173	  احتیاط پذیرفتنی است / پژوهش امروزی آن را رد می‌کند و به جای آن … می‌گوید / خطای چاپی کتاب /
174	  خطای خوانش اسکن.
175	- Keep it 2–5 sentences, formal but readable (نه ترجمهٔ لفظ‌به‌لفظ، نه ماشینی). Numbers in
176	  Persian digits are fine. Mention the key sources by their Persian-usable names (پوکورنی،
177	  بارتولومه، هرن، هوبشمان، مکنزی، نیبرگ، چونگ، معین، برهان قاطع، ویکی‌واژه).
178	
179	Field names: `derivation_fa` (node) and `note_fa` (root entry). Both required.
180	
181	## Process documentation (required)
182	
183	The owner wants to be able to audit every step later. Therefore:
184	
185	- **Every web page you rely on must be archived**: after you read a page (WebFetch or
186	  curl), run
187	  `python3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
188	  This stores the page as text under `data/verification/sources/web/` and indexes it. Only
189	  URLs that were archived this way may appear in a `sources` array. (Batch several calls in
190	  one Bash command to save time.)
191	- **Every lookup in a local reference text must be quoted**: in `ref_check[].note` and
192	  `consulted[].note` include the exact phrase(s) you found (with the grep pattern or page you
193	  used), so the finding can be re-run.
194	- Your full transcript (every tool call and result) is exported automatically by the
195	  coordinator; nothing else needed for that.
196	
197	## Sources to use (in roughly this order)
198	
199	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
200	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
201	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
202	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
203	  Use URL-encoded Persian/Arabic script for those pages.
204	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
205	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
206	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
207	  appendix; the online appendix is the updated edition of the same list (local: Watkins 1985).
208	- **Pokorny** — local OCR (POK_01/02/03, POK_full) or indo-european.info / starlingdb.org;
209	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
210	- **Klein**, **Horn**, **Hübschmann**, **MacKenzie**, **Bartholomae**, **Kent**, **Nyberg**,
211	  **Mann**, **Buck**, **Walde-Pokorny**, **Jeffery**, **Addi Shir**, **Asbaghi**, **Lokotsch**,
212	  **Gharib**, **Cheung**, **Aryanpur** … are all on disk (see SOURCE_MATRIX.md).
213	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
214	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
215	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
216	
217	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
218	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
219	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
220	which are where errors are likelier.
221	
222	## Output — write ONE file per page
223	
224	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	```json
227	{
228	  "pdf_page": 126,
229	  "book_page": 96,
230	  "verified_by": "claude-opus-5",
231	  "verified_on": "2026-09-05",
232	  "entries": [
233	    {
234	      "entry": 0,
235	      "root": "Dheigh, Dhigha",
236	      "verdict": "confirmed",
237	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
238	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
239	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
240	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
241	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
242	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
243	      "nodes": [
244	        {
245	          "id": 6,
246	          "lang": "Avestan",
247	          "words": "pairi-daeza",
248	          "verdict": "confirmed",
249	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
250	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
251	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
252	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
253	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
254	        }
255	      ]
256	    }
257	  ]
258	}
259	```
260	
261	Rules:
262	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
263	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
264	- `words` = the transliterations of the node joined by "; " (copy from the chart).
265	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
266	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
267	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
268	- If a node lists several words, cover each word; if they differ in verdict, use the worst
269	  verdict for the node and explain per word in `derivation`.
270	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
271	  scholarship takes.
272	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
273	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
274	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
275	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
276	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
277	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
278	  any extraction errors (JSON differs from the printed page) the owner must fix.
279	  Do not paste the JSON back into your reply.
280	
```


## [2026-09-05T20:51:55.719Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-178.txt"
}
```


### [2026-09-05T20:51:55.733Z] TOOL RESULT

```
1	=== PDF page 178 (book page 148) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Geu 3, Gyeu, Gieu : to chew  (refs POK:400)
4	#1 (parent #0) [Old Persian] refs=POK:400 | jutan : to chew
5	  #2 (parent #1) [Persian] refs=KLN:275 | javîdan «جویدن» : to chew | extra: جاویدن ، جاییدن
6	#3 (parent #0) [Germanic] refs=AHD | kewwan : to chew
7	  #4 (parent #3) [English] refs=KLN:274 | chew
8	--- entry 1 ---
9	ROOT Geua -> redirect to Geu 2
10	--- entry 2 ---
11	ROOT Geulo -> redirect to Dhogh
12	--- entry 3 ---
13	ROOT [Indo-European] Geus : to love, favor, choose  (refs POK:399)
14	#1 (parent #0) [Avestan / Old Persian] refs=POK:399; KNT:189 | zaošô : to agree ; zuštô : favorite ; dauštar : friend
15	  #2 (parent #1) [Persian] refs=HRN:130; BQT:897 | dŭst «دوست» : friend
16	#3 (parent #0) [Germanic] refs=AHD | kiusan : to choose
17	  #4 (parent #3) [English] refs=None | choose, choice
18	#5 (parent #0) [Latin] refs=AHD:377 | gustus : taste ; dis-goust : dislike
19	  #6 (parent #5) [English] refs=None | disgust
20	--- entry 4 ---
21	ROOT [Indo-European] Ghaido : goat  (refs POK:409; CEL5:7)
22	#1 (parent #0) [Persian] refs=CEL5:7; MON:1712 | zâq «زاق» : young of any animal ; zâq-dân «زاقدان» : womb ☞Dhĕ 2
23	#2 (parent #0) [Armenian] refs=CEL5:7; MON:1712 | jag : young beast
24	  #3 (parent #2) [Germanic] refs=AHD:1517 | gât : goat
25	    #4 (parent #3) [English] refs=AHD | goat
26	--- entry 5 ---
27	ROOT Ghaise -> redirect to Ghei 2
28	
```


## [2026-09-05T20:51:59.573Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-178.json && echo \"=== TOOLS ===\" && ls tools/ && echo \"=== SOURCES ===\" && ls data/verification/sources/",
 "description": "Read page JSON and list source dirs"
}
```


### [2026-09-05T20:51:59.613Z] TOOL RESULT

```
{
  "pdf_page": 178,
  "book_page": 148,
  "entries": [
    {
      "root": {
        "name": "Geu 3, Gyeu, Gieu",
        "lang": "Indo-European",
        "refs": "POK:400",
        "gloss": "to chew"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:400",
          "words": [
            {"translit": "jutan", "gloss": "to chew", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:275",
          "words": [
            {"translit": "javîdan", "gloss": "to chew", "script": "جویدن"}
          ],
          "script_extra": "جاویدن ، جاییدن",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kewwan", "gloss": "to chew", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:274",
          "words": [
            {"translit": "chew", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Geua", "redirect": "Geu 2"},
      "nodes": []
    },
    {
      "root": {"name": "Geulo", "redirect": "Dhogh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Geus",
        "lang": "Indo-European",
        "refs": "POK:399",
        "gloss": "to love, favor, choose"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:399; KNT:189",
          "words": [
            {"translit": "zaošô", "gloss": "to agree", "script": null},
            {"translit": "zuštô", "gloss": "favorite", "script": null},
            {"translit": "dauštar", "gloss": "friend", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:130; BQT:897",
          "words": [
            {"translit": "dŭst", "gloss": "friend", "script": "دوست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "kiusan", "gloss": "to choose", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "choose, choice", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:377",
          "words": [
            {"translit": "gustus", "gloss": "taste", "script": null},
            {"translit": "dis-goust", "gloss": "dislike", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "disgust", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ghaido",
        "lang": "Indo-European",
        "refs": "POK:409; CEL5:7",
        "gloss": "goat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "CEL5:7; MON:1712",
          "words": [
            {"translit": "zâq", "gloss": "young of any animal", "script": "زاق"},
            {"translit": "zâq-dân", "gloss": "womb", "script": "زاقدان", "see": ["Dhĕ 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Armenian",
          "refs": "CEL5:7; MON:1712",
          "words": [
            {"translit": "jag", "gloss": "young beast", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Germanic",
          "refs": "AHD:1517",
          "words": [
            {"translit": "gât", "gloss": "goat", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "goat", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Ghaise", "redirect": "Ghei 2"},
      "nodes": []
    }
  ]
}
=== TOOLS ===
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
=== SOURCES ===
MISSING_REFERENCES.md
refs
refs_online.json
SOURCE_MATRIX.md
web
```


## [2026-09-05T20:52:00.280Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:52:00.320Z] TOOL RESULT

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


## [2026-09-05T20:52:26.557Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','KNT','HRN','BQT','MON','CEL','WLD','IEC','SYN','BRT','PHD','NYB','HUB','CHEUNG','ARY','SKT','LEW','LAT','FSD','WEB','SIN']:\n    v=d.get(k)\n    print('---',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-05T20:52:27.663Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"=== sample ===\" && python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'));print(json.dumps(d,ensure_ascii=False,indent=1)[:3000])\"",
 "description": "Check existing verification file format"
}
```


### [2026-09-05T20:52:28.541Z] TOOL RESULT

```
--- POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
--- KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
--- AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
--- KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
--- HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
--- BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
--- MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
--- CEL {"title": "S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 vols., Milton MA 1997", "edition_found": null, "kind": "catalog", "url": "HathiTrust mdp.39015021572337 etc. (8-vol 1986- ed., search-only) ; Open Library records", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": null, "notes": "RE-SEARCH 2026-09: catalogue only; the 1997 Sverge Haus printing is not digitised anywhere found. HathiTrust full-text search (search-only volumes) can confirm whether a word occurs, via a browser."}
--- WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
--- IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
--- SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
--- BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
--- PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
--- NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
--- HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
--- CHEUNG MISSING
--- ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
--- SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
--- LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
--- LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
--- FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
--- WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
--- SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sectio
```


### [2026-09-05T20:52:30.693Z] TOOL RESULT

```
agent
page-100.json
page-101.json
page-102.json
page-103.json
page-104.json
page-105.json
page-106.json
page-107.json
page-108.json
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
page-117.json
page-118.json
page-119.json
page-120.json
page-121.json
page-123.json
page-124.json
page-125.json
page-126.json
page-127.json
page-128.json
page-129.json
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
=== sample ===
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix
```


## [2026-09-05T20:52:37.652Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 407 408 409; do echo \"=== POK_01 leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -80; done",
 "description": "Print Pokorny leaves near p.399-400"
}
```


## [2026-09-05T20:52:39.220Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gieu-\\|g^ieu\\|kauen\\|ĝeus-\\|geus-\\|ghaido\\|ĝhaido\" POK_01.txt | head -40",
 "description": "Grep Pokorny for roots"
}
```


### [2026-09-05T20:52:39.422Z] TOOL RESULT

```
=== POK_01 leaf 407 ===
=== POK_01 leaf 408 ===
=== POK_01 leaf 409 ===
```


### [2026-09-05T20:52:39.469Z] TOOL RESULT

```
1883:fest^^  haou7'va-  ^kauend^)  aus  *bharati  durch  Einfluß   von   ai.  cdrvati  ,zer. kaut^  umgestaltet.
2803:mit  ^Suffix  germ.  Heida-  ,*aufgespannte  Zeltstange'  (:  gr.  deXtog)  in ftiiord.  tiald  , Vorhang,  Decke,  Teppich,  Zelt',  ags.  teld  n.  ,Zelt',  ahd.  nhd. teli  eio'entlich  ,ausgespannte  Decke';  dazu  ahd.  zelto,  nhd.  Zelten,  Zelt- kuchen] oder  besser  als  ,geschrotet'  (s.  oben  devöaXig)  zu  toch.  B  tselt-, Uält-  ,kauen';
2816:toch.  A  täloj  B  talläwo  ^unglücklich',  Van  Windekens  Lexique  136 eher  B  tsalt-,  tsält-  ,kauen',  Pedersen  Toch.  Sprachg.  18  f.
```


## [2026-09-05T20:52:43.019Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt POK_full.txt; do echo \"=== $f ===\"; wc -c $f; awk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\", NR}' $f; done",
 "description": "Check Pokorny file sizes"
}
```


## [2026-09-05T20:52:44.222Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"gieu\\|ĝeus\\|ghaido\\|haedus\\|gaits\" POK_full.txt | head -40",
 "description": "Grep POK_full"
}
```


### [2026-09-05T20:52:44.611Z] TOOL RESULT

```
=== POK_01.txt ===
981836 POK_01.txt
leaves: 363
=== POK_02.txt ===
1137861 POK_02.txt
leaves: 433
=== POK_03.txt ===
1170809 POK_03.txt
leaves: 429
=== POK_full.txt ===
3971883 POK_full.txt
leaves: 1
```


### [2026-09-05T20:52:44.659Z] TOOL RESULT

```
32248:Root / lemma: ghaido- or ghaido- 
32252:Material: Latin haedus, -/"m. " a young goat, a kid ' from *^/7a/ofc»s (dialect (h)edus, faedus, 
32271:kizzi(n), chizziu. (Germanic *kittTna) " caressing alteration ' are from ghaido-, is a 
43631:equivalent from Indo Germanic ghaido- {above S. 409). 
71508:Old Irish sa/g/m^go a thing after, search, seek' (zur3. PI. segaits. Pedersen KG. II 606
```


## [2026-09-05T20:52:49.011Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '32235,32290p' POK_full.txt",
 "description": "Read ghaido entry in POK_full"
}
```


### [2026-09-05T20:52:49.056Z] TOOL RESULT

```
Lithuanian gabana, gabanat ' armful, armload (hay)'; besides gabenu, gabentT take 
away ', Prater, dial, at-gebau " has brought ' (compare Latin capio: cepi), gabus ' gifted, 
talented ', gebu, gebeti^ to be able, be used to, be accustomed to '; with a gobus ' greedy 
', gobisvn. "greed, lust', dial, gudbti^ snatch ', etc.; 

Slavic (originally iterative) *gabajQ, *gabat/"\r\ poln. gabac' assail, gripe ', wruss. habac' 
take, gripe ', etc.; Old Church Slavic ^c»i6>//7c» "fullness, wealth', gobbZb'ncW are Germanic 
loanword About the expressive character of cb- in russ. chabitb "grab quickly ', chopftb " 
grasp, catch' etc. s. Machek Slavia 16, 178, 208 ff. 

References: WP. I 344 f., WH. I 158 ff., 630 f., Trautmann 74, Feist 175 f., 214. 
Page(s): 407-409 

Root / lemma: ghaido- or ghaido- 

Meaning: goat 

Material: Latin haedus, -/"m. " a young goat, a kid ' from *^/7a/ofc»s (dialect (h)edus, faedus, 

fedusX 

Maybe abbreviated alb. {*gheida) dhija " a goat' common alb. gh- > d- ; -d- > -j-%. 

Gothic ga/tsan6 Old High German ge/zt, Old Icelandic ge/tt, Old Swedish get, f.. Old 
English gati., Old Saxon geti. (consonant stem) "goaf, originally used for both genders. 

From *gba/do- 6emed *gba/d/'nos: Latin haedmus^ of a kid ', Old English gseten. Old 
High German geizTn " of or pertaining to goats ', Gothic gaiteinu. " kid ', Old High German 
geizTn n. " he-goat; billy goat '. 

Old High German ziga, wherefore Old English ticcena'r\6 Old High German zicchTn\N\Vr\ 
hypocoristic consonant stretch, is not " through causing taboo Lautumstellung' from Indo 
Germanic *^/7Adhds originated, rather as Auslautsdublette to gr. 5i^a ai^. AaK(jov£(; (Hes.) < 
*digia, Armenian tik^hose (from goatskin)' to stellen. 

Daft alb. q/th'k\6', Middle Irish c//"sheep'. Old Norse /r/id'"Tierjunges', Old High German 
kizzi(n), chizziu. (Germanic *kittTna) " caressing alteration ' are from ghaido-, is a 



unnecessary assumption. Rather the named words are directly an enticing (or frightening) 
shout, call, as kitz, gitz, hitz, hetzusi. is attested to have evolved from most different 
languages and dialects. 

References: WP. I 527 f., WH. I 632, 868. 
Page(s): 409-410 

Root / lemma: ghais- 

Meaning: to stick to 

Material: Latin haereo, -ere, haesT, haesum ' to hang or hold fast, to hang, stick, cleave, 

cling, adhere, be fixed, sit fast, remain close to any thing or in any manner; to hold fast, 

remain attached or fixed, to keep firm, adhere; to hold fast, remain attached or fixed, to
```


## [2026-09-05T20:52:49.486Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 399\\|Page(s): 400\\|Page(s): 409\" POK_full.txt | head -20",
 "description": "Find page markers in POK_full"
}
```


### [2026-09-05T20:52:49.537Z] TOOL RESULT

```
31720:Page(s): 399 
32153:Page(s): 409 
32280:Page(s): 409-410 
34195:Page(s): 400 
34228:Page(s): 400-401 
35741:Page(s): 399-400 
35768:Page(s): 399 
36098:Page(s): 409
```


## [2026-09-05T20:52:55.674Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### around 35690-35800\"; sed -n '35690,35800p' POK_full.txt",
 "description": "Read POK page 399-400 entries"
}
```


### [2026-09-05T20:52:55.750Z] TOOL RESULT

```
### around 35690-35800

pleasure', yiosa-/?' contentedness, approval, sufficiency ', Avestan zaos-. Old pers. daus- 

"where one finds flavor ', Avestan zaoso' pleasure ', zusto^ liked, beloved, fancied, 

desirable, worth having, welcome, wanted '; khotan-sak. ysusde' he appraises, 

appreciates ', ysua, ysuyan {ys = z) "treat, delight '; 

gr. ysuoMQi ' feel, enjoy the taste of; experience, have enjoyment of, enjoy the company 
of ' (therefrom ysuu) " allow to taste '); 

alb. deshal loved', present do, dua{*geus-n-, Jokl IF. 37, 101 f.); 

Also alb. Geg me dashte' to love '. 

/7-present Latin deguno, -e/ie 'taste' {*gus-nd)\ 

Old Irish asa-gu{*gus-s-t} 'he wishes ' {ad-gusi, asa-gussi^he wishes ', s. to form 
Pedersen II 549), do-goa{*gus-a-t) 'he chooses ', verbal noun togu^ choose ', preterit 
doroigu^ elegit ' {*to-ro-gi-geus-t), Pokorny IF. 35, 177 ff., etc. (see Pedersen aaO.); 

Gothic kiusan^ assay, try, test, check ', Old Norse kjosa^ choose, wish' (also ' affect 
through sorcery ', Old High German Old Saxon kiosan' taste, assay, try, choose ', Modern 
High German kiesen, Kaus.-lter. Gothic kausjan^ assay, try, taste ' (= Old Indie idsayate); 
compare Old English wael-ceasig^ choosing corpses ' (of raven). 



noun actionis of /"/-/Old Indicy^s//-/?' Liebeserweisung, favour ', Gothic ga-kusts\. ' 
examination ', Old Frisian kest. Old English cystm. ' object of a choice, exquisiteness, 
excellence ' (but gr. ysuoK; previously single-linguistic formation from ysuoijai): of tu-: Latin 
gustus, -us ' a tasting of food, a partaking slightly or eating a little of any thing, a light dish 



at the beginning of a Roman meal, an antepast, whet, relish, taste, flavor', Celtic *gustu-' 
choice ' in names Irish Oengus, Fergus, acymr. Ungust, Gurgustan6 in Old Irish guss' 
skillfulness, power', Gothic kustus' examination ', Old High German Old Saxon kustm. " 
examination, appraisal, choice, excellence ', Old Norse kostr, -ar^ choice, capriciousness, 
(good) quality '; derivative of participle "ig^S'/ds/ Latin gusto, -^Ae "taste, eat, drink; relish, 
enjoy ' = Old High German Old Saxon /ros/d/7 'taste, try, assay, test ', Old English costian^ 
try, assay, test, plague'. Old Norse kosta, -ada " assay, try, exert oneself, strive '; previous 
noun actionis is *kur/z\n Old English cyrem. " choice, judgement'. Old High German kur/1. 
ds. (Modern High German Kur-iurst "prince elector, elector, electoral prince, one of the 
princes of the Holy Roman Empire entitled to elect the emperor', Will-ZTJA "capriciousness, 
despotism, arbitrariness'), with intersection in neuter Old Norse k0r' choice ', Old English 
ge-cor' verdict ', derived Old High German koron' taste, sip; have some experience of; 
enjoy, try'. 

References: WP. I 568 f., WH. I 628 f.. Feist 312 f. 
Page(s): 399-400 

Root / lemma: geu- geua- (besides geus^ 

Meaning: to advance; to hurry 

Material: Old \v\6\cjunati^ drive, hurry, set in motion, stir into action as if by fanning; 

arouse, instigate 'Javate^ hurries ',yzy/^-/7 "hurrying', y^- "quick, ias\.\jut/^ quickness, 

encouragement ',yai///7 "hurrying', yai/a-/7 "hurrying, quick, iast' , jav/stha-h 'the fastest', m. 

"haste, hurry, quickness ',Javas-' quickness \Javana-h' driving, animating, inciting '; 

Avestan zavah-r\. " power, strength ', zavar- n. "(physical) power, strength ' (esp. of the 
feet and the horse), npers. zor' power ', Baluchi zJ/ "quick, fast', Avestan zevTstya " the 
hastiest, most fastest, the most conducive ', uzutay-' hurrying out, foaming '; 

besides auf Indo Germanic ^'et/a-weisend: Avestan yai/a" hurry '; npers. zJo' "quick, 
fast' could belong to Aryan gox z, 

perhaps to Old Norse /rey/'a "drive, ride, push, throw, ride'; 

Serbo-Croatian zuriti se " hurry ', from Trautmann 80 to guriti se " brew ' placed, perhaps 
in spite of unclear aniaut here. 

References: WP. I 555. 
Page(s): 399 



Root / lemma: gei- : gT- 

Meaning: to sprout 

Material: Armenian c//, ciui, ceV stem, stalk', s/7-c/^/ "sprout, germ, sprout'; 

Gothic keinan, ^s-/re/>75/7 "germinate', us-kijans^ germinated, sprouted '; Old High 
German c/7/77a/7 "germinate, split, open'. Old English clhan^break, crack, be open'; Old 
High German chTmoxu., asachs. /r/777c»"germ, sprout'; Old English cTd, Old Saxon kTdm. 
"germ, sprout, young shoot ', Old High German frumakTdi^ first shoot '; Old Saxon kio. Old 
English ceon, cTun^ gills ' (probably *kijan-). 

Here probably with a previous form the bursting bud, sprout in general meaning "break, 
crack, sich split' Old High German kTI, Modern High German Keil, Middle Low German kTI, 
Norwegian kTlem. "wedge' (or this meaning of the sharpness deriving form of the plant 
bud? formally from *kT-dla-, compare *kT-Ma-\n:) Old High German k/de/, Modern High 
German Dialectal ke/de/m. "wedge'; Old Icelandic A/7/m. " narrow sea bay ' ("*cleft, 
fissure'), changing through ablaut Norwegian keilai. "small gully, canal'. Middle Low 
German kelrc\. "narrow Meerbucht '; with /Old English cinui. " cleft, col, gap', Danish 
Dialectal kin "col, gap'; perhaps Old Middle High German chiT\eeW, Middle High German 
/r//m. " onion, bulb of the leek ', Modern High German Kielm. ds. (compare Bavarian 
ausk/e/enirom acorn, onion , " germinating the peel, breakthrough skin '); 

Latvian ze/ju, z/et' flourish, bloom, appear, come into view ', next to which with d- 
extension (probably originally o'-present) Lithuanian zyd{z/Ju zydef/"b\oor(\, blossom', 
prazystu, -zydau, -zysti^ blossom ', z/ec/as "bloom, blossom, ring', Latvian ziedu {ziezu), 
z/ec/e/ "bloom, blossom'. 

References: WP. I 544.
```


## [2026-09-05T20:52:56.371Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### 34130-34240\"; sed -n '34130,34240p' POK_full.txt; echo \"### 31680-31725\"; sed -n '31680,31725p' POK_full.txt",
 "description": "Read POK page 400 entries"
}
```


### [2026-09-05T20:52:56.443Z] TOOL RESULT

```
### 34130-34240
With dental extension: Old English grsedxw. "grass'. Middle High German graz, -zzes' 
young branches of coniferous wood ' from ghre-t-, ghre-t-; 

probab\Y to ghre-: ghrd-\ ghre-^ project, protrude, e.g. from plants shoots, plants 
prickles, beard hair ' and its light basic root gher- ds. (see there would be to be covered by 
Latin herba ' vegetation; a green plant; a blade or stalk, esp. of corn or grass ' to the latter, 
if from *gberz-d^a 'bar\eY' with suffixal of the same kind to *gher-6!"a. 

Berneker 355 considers doubtingly for Old Church Slavic grozdh "grape', grozrrb ds. a 
cognate of *ghras-6!^o-, -nu- as base; the meaning would be justified at most through russ. 
granka^ bundle ' : Bulgarian Serbo-Croatian grana'tw\g, branch'. 

References: WP. I 645 f., WH. I 616 f., 639 f. 
Page(s): 454 

Root / lemma: ghroud- 



Meaning: a protruding body part 

Note: only Celtic and Germanic 

Material: Old Irish gruad{u. es-stem) "cheek", cymr. gruddds., corn, ^mo' 'maxilla'; 

Old English greadam. 'bosom'. 

References: WP. I 658. 
Page(s): 462 

Root / lemma: g(Oeu-, g(Oeu- 

Meaning: to chew 

Material: Npers. yai/zo'a/? "chew', afgh. zova/, zoya/ds., "bite, gnaw ' (Iran. *jyav-)\ 

Armenian kveni^ larch, any of a number of cone-bearing trees which yield a heavy solid 
wood '; 

Old Icelandic tyggja, -i/a"chew' (for *kyggja af^er tgg/a'c\r\e\N'), Swedish tugga, Old 
English ceowan, nengl. c/7ei4/ [common lllyrian-alb. kh- > t-, gh- > d-s]\ 

Middle Low German keuwen. Old High German kiuwan. Middle High German kuwen 
"chew' {*kewian)\ Old High German kewa. Middle High German kiuwei. " jaw, mandible, 
lower jaw bone '; derived: Old English ceace. Old Frisian ziakei. {*keukdn) and Old Frisian 
kese^ molar tooth ', Middle Low German kuse, mnl. kuze, changing through ablaut mnl. 
kiezeds.; 

Balto-Slavic *ziauid^ chew ' in: 

Lithuanian ziaunost PI. " jaws ', Latvian zaunast PI. " jaws, maxilla, gill'; 

r.-Church Slavic zuju {* zjou-) and zbvg, zbvati{ *zjbv-). Old Czech ziji, zvati, russ. zuju, 
zevatb "chew'; in addition (from Balto-Slavic *zjauna) Bulgarian zunai. "lip' and Serbo- 
Croatian zva/on. " pharynxes, throat, gorge ', zva/et PI. " set of teeth in the bridle '; russ. 
zvakatb "chew', zi/a/r" larch resin as a tooth cleaning material '; 

Tocharian AB sw-a-fs/"eat' (Pedersen Tocharian Sprachg. 43); 

compare further g^Tu- "resin'. 

References: WP. I 642, WH. I 601, Trautmann 372, Liden Ann. Acad. Sclent. Fennicae 27, 

119. 

Page(s): 400 



Root / lemma: glag-ox glak- 

Meaning: milk 

Grammatical information: Norn, glaktn. 

Note: only gr. and Latin 

Material: Gr. yaAa, yaAaKTOt; n. "milk"; originally probably *YAaKT, Gen. *YAaKT6(; (compare 

yAaKTO-cpayoc;), out of it *yAaK, *yAaKT6(; (hence yAaK(I)VT£(; psaroi yaAoKTOc; Hes. and 

yAoKKOv yaAa9r|v6v Hes., probably a Kinderwort with hypocoristic gemination as |jikk6(;), 

further *yAa, with vocal development in monosyllabic word (probably in the child's mouth, 

whence also die initial stress:) yaAa, whereupon also yaAaKTO(; instead of *yAaKT6(;. The 

form hom. ykdyoc, (nspiyAaync;, later yAayaw), on the other hand dissimilated Cretan 

KAayoc;, goes back perhaps to Nom. *yAay < *yAaK. 

Latin lac, lactisu., with dissimilation reduction of aniaut. Gutturals from *glact= gr. yaAa; 
old- and late Latin /-stem lacte, compare PI. lactesi. " milk of the male fish '; derived 
delicus ( *de-lac-os) " put away from the breast, weaned; the weaned mother's milk '? 

About altchin. lac{*glac)iroxr\ Indo Germanic *galakts. Karlgren DLZ. 1926, 1960 f. 

References: WP. I 659, WH. I 337 f., 741 f. 
Page(s): 400-401 

Root / lemma: gleg- 

Meaning: soft, tender 

Material: Nasalized in Old Icelandic klokkr^ soft, pliable, flexible, sentimental ' (from 

*klinkuaz). Old Icelandic klekkva^ become soft, show faintheartedness or grief, groan, 

moan', Swedish /r/5c/ra "frighten' {*klinkwan). Old Danish kliunka6s., Danish klynke^ 

whimper ', compare in addition the causative Old Norse klokkva' soW. make', Swedish dial. 
### 31680-31725
gr. Eysipu) " awake ' (whether £- Adv. *e?compare eor din Avestan a-garayeiti ar\6 
above S. 280; different SchwyzerGr. Gr. I 6483), Aor. sypsTO, sypEaGai, Perf. s-ypn-yopa 
(for E-yn-yopa - compare Old Indicya-^a/a- with dem p from sypsaOai; Med. (late) s-yn- 
ysp-pai; of Perf. proceed from sypnyopTi " on guard ', sypnyopaic;); sypnaau) "watch' to 
*ypr|-T- (compare Avestan fra-srato^by awakening '); barely from *£ypriaKi(ji) (Schwyzer Gr. 
Gr. I 7082); 

alb. Tosc ngre {irorr\ which ngr^, Geg ngrei^\\i\. up, arouse, erect, awake, stretch a gun 
'{*n-gra-n-id), participle n-grite{*-grht-)\ 

presumably Old Norse karskr, /re/'s/r/'" fresh, agile, lively'. Middle Low German karsch 
"fresh, alert, awake, smart', Alemannian charzsch. 

References: WP. I 598 f., WH. I 429 f. 
Page(s): 390 



Root / lemma: g(e)u-lo- 

Meaning: glowing coals 

Note: 

Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 

Material: With Asuffix: 

Irish guar coa\' (< *geulo- or * goulo); 

Old Icelandic kolu. " charcoal ', Old English colm. "coal', engl. coal. Old Frisian kolei.. 
Old High German kolom., also kolu.. Middle High German kolu., kol(e)xx\., kolei., Swiss 
c/7c»//e "gleam'. 

In addition with /"-suffix (or previously reshaped from *^^/c»- after Armenian hur^f\re'): 

Armenian Ara/r "fire, glowing coals' (< *guro-, *gura-), krak-aran^ siove, hearth, fireplace, 
glowing frying pan '. 

References: WP. I 563. other possibilities by W. Schuize Kl. Schr. 479. 
Page(s): 399 

Root / lemma: ge(i)- : gd(i)- : 57- 

Meaning: to sing, to cry
```


## [2026-09-05T20:53:16.381Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35670,35695p' POK_full.txt; echo \"=== ghaido header ===\"; sed -n '32100,32160p' POK_full.txt",
 "description": "Get geus- header and check p.409 entry"
}
```


### [2026-09-05T20:53:16.444Z] TOOL RESULT

```
English ciern, engl. churn 6s.). 



Maybe alb. {*kjern) thjerre^ lentil ' not from Armenian sisern' chickpea ' 

*graros {*gr-r6s) " pulverized, ground into fine particles; crushed ' is continual probably in 
Latin glarea {* grareja) ' gravel '; o'-present 'ig/'d-o'd perhaps in Gothic ^5/r/io/d/7 ' crunch '. 

References: WP. I 599 f., WH. I 605 f., 618 f., Trautmann 371 f., Schwyzer Gr. Gr. I 514, 
574, 682 under Anm. 5. 
Page(s): 390-391 

Root / lemma: geus- 

Meaning: to taste; to enjoy [' savor, enjoy, taste ', in the Germanic and Celtic 'choose', in 

Indo Iran, and Alban. 'love'] 

Material: Old \nd'\c Josat/, Jusate ' tastes, enjoys, loves 'Josayate^^here one finds 

pleasure', yiosa-/?' contentedness, approval, sufficiency ', Avestan zaos-. Old pers. daus- 

"where one finds flavor ', Avestan zaoso' pleasure ', zusto^ liked, beloved, fancied, 

desirable, worth having, welcome, wanted '; khotan-sak. ysusde' he appraises, 
=== ghaido header ===

gr. Yur|<; " the crooked piece of wood in a plow ', aporpov auToyuov " Pflug, an dem 
ilCrummholz und Scharbaum noch aus einem Stuck bestanden ' (s-suffix doubtful), 



wherefore Yur|<; " piece of wood as field measure ' {*\/u[a]diq-, but also *YuFac;- possible); 
gr. YuTov " limb, the feet, womb, hands, the hand, (so prob. as device on signet); the whole 
body '; 

maybe alb. 5//" womb' 

gr. MHTpoc; yuTa "lap", yuiow " lame ', from which yuioq " lame ' (Grdf. *yua-iov; or yuF-iov? 
ders. doubt by yuaAov, see above), yavaoq 'crooked, bent outwards, writhed humped 
(from legs)', yauaoojjai " to be bent ' (but ^avaabaq i])Z{jbf\q Hes. perhaps Gaelic, to Old 
Irish gau'We, falsity'?) can a have preserved after other Adj. in -ooqior ' stooped, writhed, 
crooked, humped ', yet au is also difficult, because an ablaut *geu- : gdu-'\n spite of the 
frequent grade *gu- stands not certainly; unclear hom. apcpiyuoq " with a limb at each end, 
double-pointed, or bending both ways, elastic', epithet of spear, and aiJcpiyunsK; ' he that 
halts in both feet, the lame one ', epithet of Hephaistos; 

maybe also alb. genje/l'\e' 

Middle Low German nnd. kuse' stump, club, mace, joint; grinder, molar tooth ', 
Norwegian dial, kus' hump, hunchback '; Swedish /ri/s5 'pudenda'; Old Norse kjossi. " 
pouch ', kjossm. 'bay, cavity', faro, kjosi. 'craw ', Swedish kjusa^ valley gulch ', kjus 
'point, edge of a poke ' , Norwegian kysa {*keusidn-) and k0ysa ( *kausidn-) ' crest, bonnet, 
cowl '. 

References: WP. I 555 ff., WH. I 112 f., 311, 629, 852, Trautmann 80, 100 f. 
Page(s): 393-398 

Root / lemma: ghsb^(o)lo-, -la 
Meaning: bifurcation 

Material: Old Irish Middle Irish gabur\oxV.Qd bough, fork; fork point the thighs, vulva', cymr. 
gafr fork; thigh fork, vulva', abret. Plur. gablau^ fork ', nbret. gavl, gaor bifurcation ' (with 
/^umlaut from ato eacymr. gebeF a mattock, pickaxe ', cymr. gefail\-l-s\.Q'C(\\ 'pliers', bret. 
gevelm., acorn. geuel-hoern<^\. A pair of snuffers), (gall-)Latin gabalus^ cross, gallows '; 
the brit. forms prove a Celtic *gablo-\ the medial 5 in gabalus\s probably Latin; v. Wartburg 
separates gallorom. gabalus 'spear, javelin' (older '*fork'), places that in *gab-lakkos 
'spear, javelin' (cymr. gaflachds), from gabulum' gallows ', but ^in Old Irish gabul 
( *gh^'^lo-) is only epenthesis; 



Old High German gaba/alorW, Middle Low German gaffel(e)i., Old English gafol, 
geafeli. ds.; Old Icelandic gaflak. Old English gafeluc^ light spear, lance' derive from an 
Old Irish *gablacfr, 

here probably the PN lllyrian Gabuleo, Venetic Tpi-yapoAoi. 

References: WP. I 533 f., WH. I 575, Krahe WiJrzb. Jahrbucher 1, 215. 
Page(s): 409 

Root / lemma: ghsb^- 
Meaning: to grab, take 
Note: 

Root/ lemma: ghsb"^-'. 'to grab, take' derived from the extended labials: gelet{h)-, glet{h)- 
(: gl9t{h)-) and glet{h)- {\glt{h)-) of Root/ lemma: gel-1\ "to curl; round' [see above].
```


## [2026-09-05T20:53:18.619Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD jud/jaw ===\"; grep -n \"ǰūdan\\|judan\\|ywtn\\|to chew\\|jāyīdan\\|jāwīdan\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD dost ===\"; grep -n \"dōst\\|dost \" PHD.txt | head -20",
 "description": "Grep MacKenzie for chew and friend"
}
```


### [2026-09-05T20:53:18.678Z] TOOL RESULT

```
=== PHD jud/jaw ===
PHD.txt:414:jawédan [LOLMN < А l-Imn; ywyt?n' | (P y'wyd?n, M Pyn), N ~] eternally, always. ~ag [-k! | (P -g), N ~a] eternal, perpetual. jawén [S£yn! | № jawin] made of barley. jeh [yh, yyh = Av. jahi-] the Whore, female arch-demon. fiw [суш!, yyw! = Av. fiwya-] (consecrated) milk. *jomā [ywm’y] together with; both. jorda [ywilt’y, 2k | (P yw?rd?w), J *jwrd?r] corn, grain. jo(y) [ywd, ywb! | N ~] stream, channel. Jóy-, -išn, v. Jadan. jud [ywdt' | M jwd] separate, different; anti-. ~ az [N juz] except, apart from. judàg [ywd? h! | N juda] separate, different. ~ih: separation, difference. Jūdan, jóy- [ywtn!, ywd- | M jwwdn, (jw-), (N jawruan)] chew; devour (daevic). „išn: eating (daevic). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk!] schismatic, heretic. ~th: heresy. Juy [усе | N ~] yoke. Jumbāģīh [ywmb’kyh] motion. jumbénidan, jumbén- [ywmbyn-yin'] (cause to) move. jumbidan, jumb- [ywmb-yin' | N ~] move. ~išn: motion, movement. jumbihistan, jumbīh- [ywmbyh-stn'] be moved. juttar [ywdtl | M jwtr] different, otherwise. --īh: opposite, reverse. Juwān [ywb?n! | (P ywn), N jawàn] young; a youth. ~th: youth. juxt [ywht! | (P ywxt), N juft!] pair, couple.
PHD_mackenzie.txt:3086:Jiidan, Joy- [ywtn l, ywd- I M jwwdn, (jw-), (N JaWJu'an)] chew; devour
PHD_mackenzie.txt:6168:caste pesag.                            chew judan.
PHD_mackenzie.txt:10588:drayii                      ~         judan                         \\~tt
=== PHD dost ===
```


## [2026-09-05T20:53:30.390Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD dost ===\"; grep -n \"dost\\b\\|d6st\\|dost,\" PHD.txt | head -10\necho \"=== PHD friend ===\"; grep -n \"friend\" PHD.txt | head -10\necho \"=== NYB dost ===\"; grep -n \"dōst\\|dwst\\|friend\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Pahlavi dicts for dost"
}
```


### [2026-09-05T20:53:30.473Z] TOOL RESULT

```
=== PHD dost ===
=== PHD friend ===
14:For his good counsel on what to include in the dictionary I am most grateful to my friend Dr. P. Gignoux of Paris, for without him many common words would have slipped through my net. Most of the labour of compiling the English index, which will surely be appreciated, was undertaken by my wife. The debt I owe to the teaching of the late Professor W. B. Henning, in connection with Pahlavi and all things Iranian, cannot be expressed in words.
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
2044:friend ayür, dëst, ērmān,
2045:friendliness ayarómandih.
2046:friendly ayàrómand, mihrbān.
2047:friendship ayürih, dēstih, ērmānīh, mihr.
=== NYB dost ===
805:avinn-biiteh [~-bwtyh or -YHWWN-tyh] abstr. of the preceding w.: waste, loss 420-21; the state of one defeated 638. — As to formation cf MPrs hy’rbwdyh ‘friend- ship’ (A-H II).
1026:^ mtws ZY kysr... = i Amtös i kēsar ~ kart ‘which Amtos, the son of the brother of Kaisar' built. However, his reading Amtés is quite arbitrary, and he gives no reason for it; it is certainly not Greek, and no such Iranian name is imaginable. His attempt to situate the man so named in the history of the Roman emperors is pure fancy (Cat. 82). — [Would it be too daring to read the name [^mtws] Amittös and to regard it as a somewhat inaccurate rendering of Amyntas, the well known king of the highland of Asia Minor who died in the year 25 A.D.? He was established as king by Antonius in the year 36 B.C., but went over to Octavia- nus in the year,31 B.C. and became a close friend of the emperor: He had po- litical interests in Cilicia too (Strabo 671). It seems however doubtful whether he also extended his power to upper Meso- potamia. |
1318:döst [dwst'] 1. adj. kind, friendly 832°, 10413; dear, beloved, comp. ~-tar 2218, 41°. — 2. subst. friend 3215, 621°, 6325; pl. cas. obl. —-än '701.2.22, — < *dauštā, nom. sg. of OP daustar-; MPrs dwst (S); Paz. NP döst; SW forms from Av. (1656) zaoš- ‘to enjoy’; cf došaram.
1319:dēstēh friendship 51. 5527. 7028,
1800:*hamāxakēh [hm’hkyh} comradeship, companionship 5718, 6114-23, — Abstr. of *hamāzak (no Paz. reading known to me) which renders Av. (1744) haxay- ‘friend, companion’, FrO XXIV. I derive *hamā- xak from *hama-haxa-ka-. MPrth Pm- zwnd ‘unanimous’ (S, List 83, Sogd. 54) may go back to *hama-haxa-vant- (and thus be separated from MPrs h’mwx in the same sense, v. BBB and List 83).
1836:*ham-hàl [hmh?l] companion, fellow 70?3; pl. cas. obl. ~-dn 68°. — No Paz. reading known to me; Paz. substitutes for it ham-ayčir (ayär ‘friend’), Skr. v. sarve sahäyinah. I derive it from *hama-harda-, SW form of *hama-harza-, v. the next w.; NP hamal ‘companion, friend’ (Šn.). An- other reading and etymology by Bthl, MirM I, 5.28 sqq., whom I followed in HP.
2556:mihr [mtr'] 1. n. pr. the Aryan god Mitra, Av. Midra: ~u Srēš u Rasn 1215; ~ u Zurvān i akanārak u menčyč datistan 77-12, ~ zg"'"atài névak, Dahman Afrin 9213, ~ yazét u x"aršet 961! ; atur burzen ~ the third of the three imperial fires 11%. 2°, symbolizing the class of the cattle- breeders and farmers 2° (cf Av. [1430] Midrē yö vouru.gaoyaotiš); — existing in all animal beings 965-%; — Dadv pat ~ the name of the 15th day of the month 9715-16, — 2. the sun 78. 317. 7913-18, — 3. abstr. friendship, loyalty: — u došaram i apāk čišan 87°; ~ + amāh 98; ~ i čvak 6 dit 119; vehän ... ~ däst u dosteh varzit 5526-27, — Av. (1183 sqq.) midra-.
2884:pahlom [p’hlwm, inser. p'lswmy], pāšom [p’swm] 1. noble, elevated, exalted, fore- most: Sühpuhr ... martan ~ foremost among man 15!? = P2:5 (p’lswmy). — 2. sublime, blessed, paradisiae, of Garod- màn and the heavenly world 3115. 325 [p'šwm]. 8916; of those bringing about the fraškart 105%. 1067! [p’swm]; ~ dēstēh i 6 yazdčin blessed friendship with the gods 5511; of ahläyeh 598; sup. ~-tom apazär i crat the most sublime power of Wisdom 89?" (~-tar Mx 151), — Not to be combined with fratom (g. v.) From *pardama-, orig. ‘Parthian’, an adj. derived from Par0a(va)- (Gr IIdp0ot) in the same way as Av. (710) dahyuma- from dahyu- and (1661) zantuma- from zantu-, cf also (1566) the name of the people Sairima-. In Achaemenian time there are proper names such as (in Bab. cuneiform) Par-ta- a- ma, Pa-ar-ta-am-mu (Holma, NKt 35 n. 1, after Tallqvist) Hence in the Bible, with the Hebr. pl. ending, partemim ‘the nobles’ at the Babylonian and Per- sian (historically: the Parthian) court: Esth. 13. 6%. Dan. 13. Parthians constitu- ting the highest social class in Parthian-
4037:vat-došaramčh [wtdwš'Imyh] the quality of having bad affection, coldheartedness, unfriendliness 849. — Skr. v. nikrsta- vällabhya.
4382:xučš [NPŠH; hwyš] 1. refl. pron. self, valid for all persons, a) referring to the agent = the logical subj.: -š ~ hécak hac cäh ul hixt he himself hauled up 1519; b) as an obj.: ~ hac ranj äsän kartan to relieve oneself of trouble 1313-14; c) after a prep.: vinäskäreh andar ~ bē guft 3474; (šmāh) ~ rād 45°; d) as a refi. poss. pron.: 4 ~, passim, e.g. hac avatdi i avēš 51"; ruvün i ~ rädY F:2; hac har i ~ F:3; or ~ alone, or kan i ~, both placed before their subst.: pat ~ casm 80%; hac ~ xünak ŠPrs: 10; api-š ~ GfrinY kart" and he praised himself Pl: 10-11; hàn i ~ xvatāt 5%; also fravahr ēt i ~ 88%; har kas õi i dit ētūn döst bavet cigon i ~ everyone will be as friendly to the other as to himself 10412-15; e) as an attr.: ~ Zartuxšt 5228; — emphatic form ~-tan or (659. 928) tan 4 ~ (v. tan): ~-tan u asvārān ranjak mā dārēt 8? ; —-tan o marg
5938:dwst: dost
```


## [2026-09-05T20:53:31.743Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN chew ===\"; grep -n \"chew\" KLN_1966.txt | head -20\necho \"=== KLN 1971 chew ===\"; grep -n \"^chew\\|chew, \" KLN_1971.txt | head -20",
 "description": "Grep Klein for chew"
}
```


### [2026-09-05T20:53:31.804Z] TOOL RESULT

```
=== KLN chew ===
7158:champ,  tr.  and  intr.  v.,  to  chew'  noisily.  -  -Of  imi¬ tative  origin.  Cp.  jam,  ‘to  press  tightly’. Derivatives:  champ,  n.,  champ-er,  n. champac,  champak,  n.,  an  East-Indian  tree.  — Malay  tshampdka,  fr.  OI.  campakah,  which  is prob.  an  Austric  loan  word, champagne,  n.  —  F.,  abbreviation  of  vin  de  Cham¬ pagne,  ‘wine  made  in  the  province  of  Cham¬ pagne’,  a  name  derived  fr.  Late  L.  campania, ‘plain,  open  country’.  See  campaign  and  cp. champaign.
7286:chaw,  tr.  v.  —  A  variant  of  chew, chawbuck,  n.  and  tr.  v.  ( obsol .)  —  Anglicized form  of  chabouk  (q.v.)
7376:chew,  tr.  and  intr.  v.  —  ME.  chewen,  fr.  OE.  ceo-
7379:wan,  rel.  to  MLG.  keuwen,  Du.  kauwen,  OHG. kiuwan,  MHG.  kiuwen,  MG.  kiiwen,  ‘to  chew’ (whence  G.  kauen,  ‘to  chew’;  but  cp.  G.  wieder- kauen,  ‘to  chew  the  cud’,  fr.  MHG.  kiuwen)  and to  ON.  tyggva  (dissimilated  fr.  *kyggva),  and cogn.  with  OSlav.  zivp,  zivati,  ‘to  chew’,  Lith. zidunos  (pi.),  Lett,  zaunas  (pi.),  ‘jaw;  gill’,  Pers. javidan,  ‘to  chew’,  Toch.  swa,  ‘to  eat’.  L.  gingiva, ‘gum’,  is  not  cognate  with  the  above  words.  Cp. chaw.
7380:Derivatives:  chew,  n.,  chew-er,  n.,  chew-y,  adv. cheyney,  n.,  a  woolen  fabric.  —  Lit.  ‘china  ware’. The  word  represents  the  former  pronunciation of  China.
9463:pounded’,  which  is  rel.  to  Heb.  kiskes,  of  s.m. These  verbs  are  prop.  Pilpel  forms  of  Arab. kassa,  resp.  Heb.  kdsds,  ‘he  chewed’.  Cp.  Ak¬ kad.  kasasu,  ‘to  cut  small’,  Aram.-Syr.  kiss‘thd, Akkad,  kissatu,  ‘fodder’, cousin,  n.  —  F.  cousin,  rel.  to  OProveng.  cozin; fr.  L.  consobrinus,  ‘cousin-german’,  orig.  de¬ noting  only  ‘the  child  of  a  mother’s  sister’,  fr. con-  and  sobrinus,  ‘a  cousin  by  the  mother’s side',  contraction  of  sordrinus,  from  soror,  ‘sis¬ ter’  (hence  prop,  meaning  ‘sister’s  child’),  which is  cogn.  with  Goth,  swistar,  OE.  sweostor,  ‘sis¬ ter’.  See  sister  and  cp.  cozen.
9869:Cucurbitaceae,  n.  pi.,  a  family  of  vines  (bot.)  — Formed  fr.  Cucurbita  with  suff.  -aceae. cucurbitaceous,adj.  —  See  prec.  word  and  -aceous. cud,  n.  —  ME.,  fr.  OE.  cwidu,  cudu,  ‘mastic,  cud’, rel.  to  ME.  code,  ‘pitch’,  ON.  kvada,  ‘resin’, OHG.  quit i,  kuti ,  ‘glue’  (whence  MHG.  kiite, kiit,  G.  Kill,  ‘putty’),  and  cogn.  with  OI.  jatu-, lac,  gum’,  and  with  L.  bitumen  (an  Osco- Umbrian  dial,  word;  the  genuine  Latin  form would  have  been  *vetumen,  fr.  *gwetumen), ‘mineral  pitch’.  All  these  words  are  derivatives of  I.-E.  *gwet-,  *geut-,*gut-,  dental  enlargements of  base  *geu-,  ‘to  bend,  curve,  arch’.  See  cove, ‘a  small  bay’,  and  cp.  quid  for  chewing.  Cp.  also bitumen,  bowel,  guttural, cudbear,  n.,  a  dye  made  from  lichens.  —  Coined from  the  name  of  Cuthbert  Gordon  (in  1766) who  patented  this  dye.
13618:escheat,  n.,  the  reverting  of  the  land  to  the  king or  another  lord  of  the  fee.  —  ME.  eschete,  fr. OF.  escheoite,  prop.  fem.  pp.  of  escheoir  (F. echoir),  fr.  VL.  *excadere,  ‘to  fall  out’,  fr.  1st ex  and  *cadere,  corresponding  to  L.  cadere,  ‘to fall’.  See  cadence  and  cp.  cheat,  decay. Derivative:  escheat,  intr.  and  tr.  v. eschew,  tr.  v.,  to  shun,  avoid.  —  ME.  eschewen, eschuen,  fr.  OF.  eschiuver,  eschiver,  eschever, ‘to  shun’,  fr.  Frankish  *skiuhan,  which  is  rel. to  OHG.  sciuhen,  ‘to  avoid,  escape’,  MHG. schiuhen,  G.  scheuen,  ‘to  fear,  shun,  shrink  from’, MHG.  schiech,  G.  scheu,  ‘shy,  timid’.  It.  schivare, ‘to  avoid,  shun,  protect  from’  (whence  F.  esquiver, ‘to  avoid,  dodge’),  derives  fr.  It.  schivo,  ‘shy, bashful’,  which  is  a  loan  word  fr.  WTeut.  *skiu, ‘shy’.  See  shy  and  cp.  skew,  which  is  a  doublet of  eschew.
13619:Derivatives:  eschew-al,  n.,  eschew-er,  n. Eschscholtzia,  n.,  a  genus  of  herbs  of  the  Pa- paveraceae.  —  ModL.,  named  after  the  German botanist  Johann  Friedrich  von  Eschscholtz (1793-1831).  For  the  ending  see  suff.  -ia. esclandre,  n.,  a  scandal,  scandalous  scene.  —  F., fr.  OF.  escandle,  fr.  earlier  escandele,  fr.  L.  scan- dalum.  See  scandal  and  cp.  slander, esclavage,  n.,  necklace.  —  F.,  fit.  ‘slavery’,  fr.
14800:fitch,  n.  —  A  dial.  var.  of  vetch, fitch,  n.,  a  fitchew  or  its  fur.  —  MDu. /me,  visse, vische,  prob.  related  to  vies,  ‘stinking’,  and  to E.  fizz  (q.v.)  Cp.  fitchew.
14801:fitche,  adj.,  pointed  at  its  lower  end  (her.)  —  F. fiche,  ‘fixed’,  pp.  of  ficher.  See  fish,  ‘counter’, fitchet,  n.,  a  fitchew  or  its  fur.  —  Formed  with dimin.  suff.  -et  fr.  fitch,  ‘fitchew’, fitchew,  n.,  the  polecat  or  its  fur.  —  ME.,  fr. Picard  ficheux,  corresponding  to  OF.  fichau,  fr. MDu.  fisse,  visse.  See  fitch,  ‘fitchew’, fitful,  adj.,  irregular.  —  Coined  by  Shakespeare
14811:fizz,  intr.  v„  to  hiss.  —  Of  imitative  origin.  Cp. ON.  fisa,  ‘to  break  wind’,  Dan.  fise,  ‘to  foist, fizzle',  G.  fisten,  ‘to  break  wind’,  and  E.  fitch, ‘fitchew’.
14898:Derivatives:  flesh,  tr.  v.,  flesh-er,  n . ,  fleshings, n.  pi.,  fleshly  (q.v.),  flesh-ment,  n.,  flesh-y,  adj. fleshly,  adj.  —  ME.  fleschlich,  fr.  OE.  fliesclic, fr.  flssc,  ‘flesh’.  See  flesh  and  adj.  suff.  -ly. Derivative:  fleshli-ness,  n. fletcb,  tr.  v.,  to  provide  (an  arrow)  with  a  feather; to  feather.  —  Back  formation  fr.  fletcher. fletcher,  n.,  one  who  makes  arrows.  —  OF. flechier,  fr.  fleche  (F.  fUche),  ‘arrow’.  See  fliche. Fletcherism,  n.,  the  practice  of  chewing  one’s food  thoroughly.  —  So  called  after  the  Amer¬ ican  nutritionist  Horace  Fletcher  (1849-1919), who  advocated  this  practice.  For  the  ending  see suff.  -ism.
16163:uncertain  origin;  possibly  meaning  lit.  ‘some¬ thing  round’,  and  cogn.  with  Gk.  -(o'fpJkoq, ‘round’,  y°YYP°S>  ‘tubercular  growth  on  trees; sea  eel,  conger’,  lit.  ‘something  round’;  not cogn.  with  E.  chew.  Cp.  conger, gingival,  adj.,  pertaining  to  the  gums.  — Formed with  adj.  suff.  -al  fr.  L.  gingiva,  ‘gum’.  See prec.  word.
17175:Hanukkah,  also  Chanukkah,  n.,  the  Feast  of Dedication  ( Jewish  religion).  —  Heb.  hanukkdh, ‘dedication’,  consecration’,  fr.  franakh,  ‘he  dedi¬ cated,  consecrated,  trained  up’,  which  is  de¬ nominated  fr,  hekh  (for  *hink),  ‘palate’,  and orig.  meant  ‘to  rub  the  palate  of  a  child  with chewed  dates’.  Cp.  Arab,  hanak,  ‘palate’ (whence  hannaka,  ‘he  rubbed  the  palate  of  a child’,  hanaka,  ‘he  taught,  instructed’),  which is  rel.  to  Heb.  hekh  (see  above).  Heb.  hantkh, ‘trained,  experienced',  Mishnaic  Heb.  hinnekh, ‘he  dedicated,  inaugurated;  he  accustomed’  (in ModHeb.  ‘he  brought  up,  educated’),  hin- ndkh,  “inauguration ;  accustoming’  (in  ModHeb. ‘education’),  are  derivatives  of  hanakh.  Cp. Enoch.
22765:Derivative :  mandatori-ly,  adj. mandible,  n.,  the  jaw,  esp.  the  lower  jaw.  —  MF. mandible  (F.  mandibule),  fr.  L.  mandibula,  ‘jaw’, fr.  mandere,  ‘to  chew’,  which  is  prob.  cogn.  with Gk.  fxd&uiat,  ‘jaws’,  (xaatfcopioa  (for  *p.a&tao- ‘I  chew,  bite',  ^aax^fo,  ‘I  chew’,  \i.i.azA, ‘jaws,  mouth’  (lit.  ‘that  with  which  one  chews  or eats’),  Goth,  munps,  OE.  mud,  ‘mouth’.  See mouth  and  cp.  mandibular,  manducate,  mange, manger.
22775:Late  L.  manducare.  See  next  word, manducate,  tr.  v.,  to  chew  (rare).  —  Fr.  Late  L. manducdtus,  pp.  of  manducare,  ‘to  chew’,  fr.  L.
22777:mandere,  ‘to  chew’.  See  mandible,  and  verbal suff.  -ate.
22789:care,  ‘to  chew,  to  eat’,  fr.  L.  mandere,  ‘to  chew’ (in  Late  L.  also  ‘to  eat’).  See  mandible  and  cp. words  there  referred  to.  Cp.  also  blancmange. Derivatives;  mang-y,  adj.,  mang-i-ly,  adv.,  mang- i-ness,  n.
23069:masseter,  n.,  either  of  a  pair  of  muscles  used  in mastication  (anat.)  —  Medical  L.,  fr.  Gk. p.aoniT7jp,  incorrectly  spelled  also  p.aa<T7)TT)p, ‘chewer’,  fr.  (j.aaao|xoa  (for  •p.aflttxop.ai.),  ‘I chew,  bite’,  which  is  rel,  to  (zaflutai,  ‘jaw’, (xan-ritCew,  ‘to  chew’,  (zaaTiyav,  ‘to  gnash  the teeth',  ux<myr;,  ‘mastic’,  lit,  ‘chewing  gum’. See  masticate  and  cp.  mastic.  In  its  anatomical sense  as  name  of  a  muscle  of  the  lower  jaw,  lit. ‘the  chewing  muscle’,  the  word  was  first  used  by Hippocrates.  See  Joseph  Hyrtl,  Onomatologia Anatomica,  p.  314.
=== KLN 1971 chew ===
44530:chaw, tr. v. — A variant of chew, 
45028:chew, tr. and intr. v. — ME. chewen , fr. OE. ceo- 
85326:eschew, tr. v., to shun, avoid. — ME. eschewen, 
93447:E. fizz (q.v.) Cp. fitchew, 
93452:fitchew, n., the polecat or its fur. — ME., fr. 
109469:chewed dates’. Cp. Arab, bdnak, ‘palate* 
144158:fxai), ‘I chew, bite’, fxafrra^w, ‘I chew’, p.acrra£, 
144311:cdre, ‘to chew, to eat’, fr. L. mandere , ‘to chew’ 
146165:chew, bite’, which is rel, to (id&oiai, ‘jaw’, 
146296:chew*, y. 0 LCT 0 Li , ‘jaws, mouth’ (lit. ‘that with 
146298:chewed’), [iaaaopt.ai (for *pafHaop.at), l I 
146299:chew, bite’, and prob. cogn. with L. mandere, 
155934:*(ialHaop,a!.), ‘I chew, bite’, ^acnrdt£o>, ‘I chew’, 
155936:chews’), L. mandere, ‘to chew’, Ir. meadal , 
157304:*p.a$£ao|xoa ) , ‘I chew, bite’, fr. I.-E. base 
265606:chew’, which comes fr. L. vissio, Cp. also bison,
```


## [2026-09-05T20:53:47.212Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT dauštar ===\"; grep -n \"dauštar\\|daustar\\|dauSta\" KNT.txt | head -10\necho \"=== HRN dost ===\"; grep -n \"dôst\\|dost\\b\" HRN.txt | head -20\necho \"=== HRN javidan ===\"; grep -n \"jâvîdan\\|javîdan\\|javidan\\|jâvîden\" HRN.txt HUB.txt | head -20",
 "description": "Grep Kent and Horn"
}
```


### [2026-09-05T20:53:47.281Z] TOOL RESULT

```
=== KNT dauštar ===
2661:B. As direct object of a verbal noun: DB 4.55f Auramazdé (uvüm dauSta biyà ‘may Ahuramazda be a friend unto thee’.
5508:dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
=== HRN dost ===
5244:(116); bei. dost (95).
=== HRN javidan ===
HUB.txt:8165:javidan *kauen\ afgh. zOvql, ksl. zwati (Wrzl. iran. jyu^
HUB.txt:10510:javidan 49.
```


## [2026-09-05T20:53:48.843Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG jau/gaw chew ===\"; grep -n \"chew\" CHEUNG.txt | head -20\necho \"=== CHEUNG zauš ===\"; grep -n \"zauš\\|\\*jau\\|dauš\" CHEUNG.txt | head -20",
 "description": "Grep Cheung"
}
```


### [2026-09-05T20:53:48.904Z] TOOL RESULT

```
=== CHEUNG jau/gaw chew ===
557:second millennium BCE (p. 306). Iranian verbs, such as *baru” ‘to chew, swallow’ 
2014:*Баги? (*barHu ?) ‘to chew, swallow’ 
2016:*AVESTAN: YAv. as.baouruua- '(place) where there is a lot to chew he to eat]’ (Yt 
2017:5.130, Yt 17.7), YAv. baoiriia- ‘chewable [of food]’ (Y 3.3) 
2032:*SANSKRIT: bharv ‘to chew, devour, eat’ (RV) = EWAia II: 252 
3697:0 On *&iaH’/eiH < (?) PIE *Ki-, cf. *jiauH ‘to chew’ < PIE *gieuH-, see Rasmussen 
4759:*NWIR: ? Bal. dajit/daj- ‘to bite, sting’. 0 With -j- from j30-/jä- ‘to chew’, s. *jiauH ? 
7955:*NWIR: Gz. Zara/Zar-, Tr. Zarta/Zar- ‘to chew’, NP Zard ‘gluttony’ (LW) || (+ *aua-) ? 
7956:Bal. ugarit/ugar- ‘to chew the cud, swallow, devour, devastate, misspend’. © The 
7959:tion with Si. ugaranu ‘to chew the cud’ seems quite likely, as observed by Shah- 
8557:*gnaió ? ‘to gnaw, chew’ 
8559:*AVESTAN: (+ *abi-) Y Av. aißi.ynixta- (ppp.) ‘gnawed, chewed on’ (V) 
12321:*IE COGNATES: Gr. ёрёрёо ‘I rob, deprive’, Lat. mordeö ‘I bite, chew’, ? OE 
13529:compares the Chor. forms to Skt. bhas ‘to chew’, is less likely. = Samadi: 228 
15160:*fiauH ‘to chew’ 
15162:*MIDDLE PERSIAN: MMP jw- ‘to chew’, BMP ywd- /joy-/ ‘to chew; devour (daevic)’ 
15166:*PARTHIAN: J ’w- ‘to chew (?)” = DMMPP: 197b 
15178:Jawin/jaw-, Zaz. jawitiS//awen-, (LW) Siv. gav-/Zavi, Tal. jüye ‘to chew’, Abz. 
15181:*NEIR: Pash. Zowul, Zoyol/Zoy- ‘to chew’, (LW ?) Yghn. Zav-/Zafta ‘to eat (liquid 
15184:masticate, munch, to fight together [of dogs, etc.]’, ? Ishk. Saw-/Sawod ‘to chew’ (S- 
=== CHEUNG zauš ===
8123:112 *gau (*jau) 
11828:from *jaua-a(n)za-ka-, on which see Tafazzoli ("do vazah-i parti az diraxt-i аѕшӣ" [= 
14471:*jau2 215 
14512:*jau ‘to (re)bind, hold’ 
14531:*jau? ‘to separate" 
14553:keep away, off, chase away’ is secondarily derived from that of *jau ‘to (re)bind, 
14556:Fehlen eines glaubhaften idg. Etymons für iir. *jau ‘trennen’ [...] "e silentio" auf 
14572:*jaué ‘to learn, teach’ 
14591:*jauj 217 
14594:© The evidence for a root *jaué is confined to East Ir. The initial *7- of Ir. *jauc is 
14609:*jauj ‘to harness, yoke, employ’ 
14654:218 *jaup ? 
14672:*jaup ? ‘to change’ 
14684:similar Skt. connection is semantically implausible (*raup?). The root *jaup may be 
16617:*jaus ‘to be agitated, passionate; love’, which is unknown in Ir. and, in addition, 
17877:similar to *jaué ‘to teach, learn’: таиё may have been abstracted from *ham-Hauc 
21034:‘change, Wandel (Mir. Man. III: 875) see *jaup^. > Ghilain: 65 f. | DMMPP: 297b 
23977:may be explained differently, v. *raup, *jaup?. 
27104:has acquired a secondary *j- (*jauc), not to mention the fact that the expected Av. 
30541:*zauš ‘to take pleasure, rejoice in’
```


## [2026-09-05T20:53:57.446Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG jiauH ===\"; sed -n '15155,15200p' CHEUNG.txt\necho \"=== CHEUNG zaus ===\"; sed -n '30535,30590p' CHEUNG.txt",
 "description": "Read Cheung entries"
}
```


### [2026-09-05T20:53:57.533Z] TOOL RESULT

```
=== CHEUNG jiauH ===


226 *jiauH 


*fiauH ‘to chew’ 

*MIDDLE PERSIAN: MMP jw- ‘to chew’, BMP ywd- /joy-/ ‘to chew; devour (daevic)’ 
с DMMPP: 199 

Pres.: IND. 3р1. MMP jwynd, BMP ywdynd /joyend/; Partic.: perf. pass. MMP jwwd, BMP ywt /jud/ 
*PARTHIAN: J ’w- ‘to chew (?)” = DMMPP: 197b 

Pres.: IND. 35р. j’wyd 

*KHOTANESE: (+ *ham-) LKh. hamjvame = SGS: 138 f. 

*SOGDIAN: BSogd. zyB, MSogd. jB’ ‘to bite’, CSogd. (zb'qy) *Zyb’mnty ‘the biting 
(of their tongues)’. © Sogd. -B- (CSogd. -b-) is perhaps due to the influence of zB’k 
(CSogd. zb'q) ‘tongue, language’. 

Impf.: IND. 35р. BSogd. ZyB’’; Pass.: pret. IND. 1sg. MSogd. jB’ty "ktym ‘I have been bitten’ (BBB: 43) 
*NWIR: NP javidan/jav-, Bal. ja0-//a-, Kurd. (Kurm.) jun, jutin/ju-, (Sor.) jun/ju-, 
Jawin/jaw-, Zaz. jawitiS//awen-, (LW) Siv. gav-/Zavi, Tal. jüye ‘to chew’, Abz. 
Jovida/jov- ‘to gnaw’ 

*NEIR: Pash. Zowul, Zoyol/Zoy- ‘to chew’, (LW ?) Yghn. Zav-/Zafta ‘to eat (liquid 
food), drink, slurp’ (why -v-/-f- ?), Rosh. yiyaw-/yiyud, Bart. yiyaw-/yiyud, Khf. 
yiyaw-/yiyud, Orosh. yiyaw-/yiyud ‘to gnaw, nibble’, Sariq. Z(i)yew-/Zyod ‘to 
masticate, munch, to fight together [of dogs, etc.]’, ? Ishk. Saw-/Sawod ‘to chew’ (S- 
< ?), ? Yi. Zaf-/Zaft- ‘to chew, masticate; to light a fire’ (why -f ?) 

*MISC: Orm. zay-ék ‘to chew, mastigate’ = zay-/zayók 

© On the development of initial *gi- > Ir. *ji- see Rasmussen 1989: 114, no. 5. This 
development suggested by Rasmussen may also account for the doublet roots *JiaH 
~ *zaiH ‘to perish; to destroy’ and *&iaH’/&iH ~ *saiH/siH ‘to freeze’, but both cases 
have no clear IE etymology. 

«PIE *gieuH- ‘to chew, bite” => LIV: 168 | Pok.: 400 

*IE COGNATES: Toch. su- ‘to eat; consume, devour’, OCS Zuju, Russ. Zuju ‘I chew’, 


OHG kewa, OE céowan, Engl. to chew, Lith. (f. pl.) Ziáunos ‘jaws’, etc. 

=== CHEUNG zaus ===


*IE COGNATES: OCS zsvati, Slov. zváti, Toch. B kwa- ‘to call out to, invite’ 
*REFERENCES: Werba 1997: 332; Adams 1999: 235; NEVP: 103 


*zauš ‘to take pleasure, rejoice in’ 
*AVESTAN: YAv. zus- ‘to take pleasure, rejoice in’ || (+ *a-) ‘to be joyful about 


something’ — Liste: 69 
MED.; Pres. athem. red.: IND. 3sg. YAv. äzüzuste (P 43); Partic.: perf. pass. YAv. zusta- (F 620, F 764, 
VdPZ 17.8) 


*OLD PERSIAN: dausta (Nsg.) ‘friend’ <d-u-8-t-a> (DB 4.56, DB 4.69, DB 4.74, etc.) 
*MIDDLE PERSIAN: BMP dws- /doš-/ ‘to love, like, choose ?’, MMP dwst, BMP dwst 
/dost/ ‘loving; friend’ = DMMPP: 145b 

Pres.: IND. 3р1. BMP dwsynd /dosend/; Pass.: pret. IND. 3sg. BMP dwsyt /dösid/; Inf.: BMP dwsytn 
/dösidan/ 

*PARTHIAN: zws ‘love’ = DMMPP: 386a 

*KHOTANESE: ОКЪ. ysus- (ysv-) ‘to value; approve’ = SGS: 113 

*NWIR: NP dost ‘friend’ (also dost dastan ‘to love’), 

*NEIR: Pash. 20Ха (Ё) ‘a kind of syrup’, zwag ‘bitterness, distress; gall’ (< *a-zausa-) 
*SANSKRIT: jos ‘to like, be pleased, to enjoy’ (RV+) = EWAia I: 599 

© This root has an impeccable IE etymology. 

«PIE *geus- ‘to taste, like, choose, be pleased’ — LIV: 166 | Pok.: 399 f. 

*IE COGNATES: Gr. yevouat, Lat. gusto ‘I taste’, gustus ‘taste, enjoyment’, Olrish 


do-goa (3sg.) ‘chooses’, Goth. ga-kiusan ‘to test’, NHG kosten ‘to taste’ 
*REFERENCES: EVP: 103; DKS: 354b; Werba 1997: 187; NEVP: 104 


*zgad ‘to go on, gallop, mount’ 
*AVESTAN: YAv. zgaó(/0)- ‘to go on horseback, gallop’ || (+ *fra-) ‘to go forth’ 


c» Liste: 69 
Pres. them.: IND. med. 3sg. YAv. zgaóaite (V 9.46), Y Av. frazgaóaite (Yt 5.97), INJ. 35р. ? YAv. zga0at 
(F 20), med. 35р. Y Av. frazgaóata (Yt 19.56, Yt 19.82) 


*MIDDLE PERSIAN: ? BMP yh- /jah-/ *to jump; arise, happen, occur' (see below) 
Pres.: IND. 3sg. BMP yhyt /jahed/; Partic.: perf. pass. BMP yst /jast/ 


*KHOTANESE: (+ *aua-) LKh. va’ysged- ‘to dismount’ || (+ *fra-) OKh. haysgas-
```


## [2026-09-05T20:53:58.592Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT page near dauštar ===\"; awk 'BEGIN{RS=\"\\f\"} /dauStar- sb/{print NR}' KNT.txt\necho \"--- context ---\"; sed -n '5500,5512p' KNT.txt",
 "description": "Find Kent leaf for daustar"
}
```


### [2026-09-05T20:54:00.524Z] TOOL RESULT

```
=== KNT page near dauštar ===
213
--- context ---
-
УА $ " Aic hts КҮЧ - EUR EE EE ГЕНЕ ЗЕ, m aad ACCENT add Va, rA a Ra SENS un at Mom o "heat aai Тэ мә GIO Ate a ec ala ie
Rec tae ais 5g AAA, лса mia (n n m VRAT, ЁК te o rre ns"
- eS i.i Nai ie "e Loren чйр ло
LEXICON
daéva-, Skt. devd- ‘deity’, Lt. divos, deus, pIE *deiyo- (876.1IT, $114, 5148.11). See also data- dána-. ата npm. XPh 36, 38, 39.
dat»adàna- sb. ‘sanctuary of false divinities’ (8147.1, $160.Ib): daiwa- + dána- (in derogatory sense, ‘den’, ace. to Hz. AMI 8.75, ApI 181). dawadénam asm. XPh 37f (written -d'av*m? in second copy, cf. $51, Lg. 13.293).
daug- vb., see hadugà-.
dauStar- sb. ‘friend’: NPers. dost, Skt. jostdr- ‘loving’; agent-noun ($154.IT) to root daus-, Av. zaos- ‘enjoy’, Skt. jus-, Lt. gustat ‘tastes’, NEng. choose, pIE *ĝeus- (S88). daustà nsm. (§124.5, 6186.1) DB 4.56, 69, 74; DNb 7,8, 12; DS} 4.
dacara-, see tacara-.
dáta- sb. ‘law’: Av. dáta-, NPers. dat; nt. ptc. to *dd- (8122, §242.1I). See also Vahyazdata-. dātam nsn. DNa 21; DSe 20°, 37; XPh 18f. dala isn. (less probably absn., §172) DB 1.23; XPh 49, 52. [d]ātā npn. DNb 58.
datasa, KT's reading, with first and third characters uncertain, DB 4.71f; read шаш, q.v.
Détuvahya- sb. (§164.V) ‘Datuvahya’, father of Megabyzus ($168.10): Elam. da-ad-du-man-za, АКК. 2a--tu--a; cf. Iz. AMI 1.84n. Dät[u]- vahyahyü gsm. DB 4.85.
```


## [2026-09-05T20:54:10.790Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 210 211 212 213 214; do echo \"--- leaf $i first/last lines ---\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -4; echo \"....\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | tail -3; done",
 "description": "Check Kent leaf page numbers"
}
```


## [2026-09-05T20:54:11.852Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB javidan ctx ===\"; sed -n '8155,8175p' HUB.txt\necho \"=== HRN around 5244 ===\"; sed -n '5235,5250p' HRN.txt",
 "description": "Read Hübschmann javidan and Horn dost"
}
```


### [2026-09-05T20:54:12.537Z] TOOL RESULT

```
--- leaf 210 first/last lines ---
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
....
(1) Rel. ‘who, which’: tyam asm. DB 3.60, 70. lyaiy npm. DB 1.9, 15; 4.50, 61, 63, 80; 5.22; DBa 15; DPe. 13, 131; DPhc5; DNa 28, 41; DSe 28°,
LEXICON
281°; DSf 47f, 49, 51°, 52, 54°, DH 4; XPh 24. tyat-saiy (6186) DB 1.57; 2.77; 3.48, 51, 74, 90, 91. tya as npm. ($52
--- leaf 211 first/last lines ---
1) XPh 23.
tyam asi. DB 4.70f; DPd 7. tya as asf. (856.V) AmH 5; AsH 13°. tyà npf. DB 1.13, 18; 2.6; 4.33; DPe 9, 14f; DSf 45. tyaiy as npf. (§258.1V) = XPh 31. рё apf. DPe 7; DNa 17, 40; DSe 16. . tyaišām gpf. DSm 6°; XPh 15.
tya nsn. (M0) DB 1.27, 61, 67; 2.91; 3.10, 20, 58, 76; 4.1f, 42, 49°, 53; DNa 48; DNb 2, 11, 29, 54, 56; DSe 31, 43; DSf 36; DS} 5^; D8n 2^; DZe 9, 10; XPa 19; XPb 23; ХРЇ 26, 37, 46; XPg 4; XPh 42; XV 19; AjPa 26. tya-sém DB 1.19; DNa 20; DSe 19°; XPh 17. tya-maiy DNb 48; DSe 52°; DSf 19°; DSs 7^; XPa 19f; XPb 24, 30; XPe 13 bis; XPd 19; XPf 38, 47; X8e 5°; XV 27°; A!Pa 24°; A?He 20. tya-taiy DNb 58. tya-patiy XPa 15. (ya asn. DB 1.44, 72; 4.3, 40, 59, 75, 79; 5.2; DPh 4; DNb 22, 24; DSa 4; DSf 20f, 22°; рө) 2°, 4; DSI 3; DH 3; XPa 14, 15; XPf 41; XPh 43, 49, 52; A’Sa 5^; А4 3; А?На 7. [tya]- ат DNa 36f. tya-maiy DPh 8; DH 6. tya-patiy XPf 40f. {уала isn. DSf 42. {уй npn. in tyã- maiy DNb 13. tyä apn. DB 1.64; DNb 46, 49. tyā-diš DB 1.65.
(2) Def. art., ‘the’: ат asm. DB 1.50, 54, 57, . T8, 89, 95; 2.21, 25f, 35, 41, 46, 55, 61, 69, 87, 97^; 3.7, 18, 38, 46, 625, 67f; 481; DSe 39. tyam- iim DB 5.12".
....
Gataguiya- adj. ‘Sattagydian’: adj. to preced- ing (5144.11, $167). G@ataguiya nsm. А?Р 11; for -guoiybi, unless -gudaya is to be read (854.T, $167), ef. Gk. Zarrayidat, in which case the etymology given under @atagu- must be revised.
да"4- vb. ‘seem’: Av. sand-, Skt. chand- (887, $215). @adaydlary subj. mid. ($222.II) DB 4.49; DSa 5; 08) 6 (for text, see under frasa-; cf. 554.1). ðadaya inj. ($224, 5228.11, §237) DNa 58; рМ 53.
додада,
--- leaf 212 first/last lines ---
 word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
See also wlanwaniya-.  Ganwaniya.nsm. DNb 42.
188
....
Idà- vb. ‘give’: Av. Skt. dà-, Gk. бош, Lt. dai ‘gives’, dónum ‘gift’, pIE *dó- (862, 576.11). dadátus іту. (§209, $237.II) DPd 28; DNa 55; XPh 60.
*dà- vb. ‘put, make, create’: Av. dá-, Skt.
dhà-, Gk. ri
--- leaf 213 first/last lines ---
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
....
*dar- vb. ‘be angry’, see daríana-.
daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.19
--- leaf 214 first/last lines ---
5-6).
Dérayava'u- sb. ‘Darius’ (I, son of Hystaspes, king 522-486 ».c.; IT, son of Artaxerxes I, king 426-04 в.с.): Elam da-ri-a-ma-u-ts, Akk. da-ri- ja-mus, Gk. Дарєюѕ (by haplology for *Aapetaios; Keiper, Acta Sem. Phil. Erlangen, 1.253). From pAr. *dháragat-, pic. to root in OP dar- (§162, §240), + pAr. *yasu asn. ‘the good’ (5158.1), see OP vau-: ‘He who holds firm the good’ (Hz. Arch. Hist. Iran 40, ApI 255, 267, takes as hypocoris- tie of *ddraya-vahu-manah- ‘Holder of Good Thought’; this is rejected by Nyberg, Rel. 361).
Dérayavaus nsm. (8118.IV, 5124.2) DB 1.1, 4, 6,9, 11, 13, 171, 201, 24, 27, 35, 44, 48, 61, 71, 73, 81, 83, 90; 2.1, 5, 8, 11, 13f, 18, 29, 37, 42f, 49, 57, 64, 70, 78, 91, 92; 3.1, 9, 10f, 19f, 21, 29, 40, 49, 53, 54, 64, 69, 75, 76, 83; 4.1, 2f, 31, 33, 36, 40, 43, 45, 50, 58, 57, 59, 611, 67, 69f, 72, 76; 80, 86, 88; 5.1, 14, 18, 20, 30, 34^; DBa 1, 41,9, 14; DPa 1;
190 OLD PERSIAN
....
dasta- sb. ‘hand’: Av. zasta-, N Pers. 0051, Skt. hdsta-, pIE *ghosto- (§88, $116, $145). See also dastakarta-. даѕіауа ism. DR 4.35. dastaibiya idm. (§189) DNb 41.
dastakarta- adj. ‘handmade’: dasta- + pte. .
karta- (5160.10), to kar- ‘make’. [dasta|kartam (restored after the Elam., Wb. ZDMG 91.85,
```


### [2026-09-05T20:54:12.603Z] TOOL RESULT

```
=== HUB javidan ctx ===
diiS' *iibel, bose* H. 565 = ap. dus-, zd. duz- und dm-^
phi. dm- Gl. and Ind. 276 flg., paz. dus- Shk. 242, arm.
dz^ neben fs- (also phi. "^diiz- neben dws-); arm. nzdeh
*Fremdling (5. Jhd.) = ap. '*mzdahyu' = zd. *nisdanhu-
'der ausserhalb des Landes ist'.^ 229 ~
§ 120. Ap. i (= idg. g^^ g^h) im Aniaut = np. j,
z und 2:
a) = np. j im N. pr. Jamasp, jamasp = phi. famdsp,
arm. jamasp (PerserkSnig, Sebeos p. 19) = zd. jamaspa-^
aber gd. dBjamaspa-, syr. Zdmasp, gr. Zafidanjjg Tab. 142;
javidan *kauen\ afgh. zOvql, ksl. zwati (Wrzl. iran. jyu^
oben p. 49 — 50 und § il); jtva *Quecksilber = ziva^ siehe
unter c).
b) ^=np. z: zadan 'schlagen' = zd. ap. jan, skr. han\
zan *Weib* = gd. j^ni- 'Weib'; zih *Bogeusehne' =^ zd. skr.
jycL-; zistan 'leben', zd. skr. jiv\ zahr (oben p. 71), arm.
zahr 'Gift' = zd. *fal^ra-; zdv 'Spalt' H. 649, oben p. 68
und 70.
Die Dialekte ^) haben hier j, i, wahrend sie fiir z ==
iran. z {g^^ 9^h): z setzen , siehe das Material bei Horn
p. 143—151. Daher zud H. 673 mit z in den Dialekten
=== HRN around 5244 ===
phlv. döst, döstth, vergl. dös(i)s)t, döäak; ai. vergl.
josa-.
bei. vergl. zar-ßs geldliebend' (181).
np. döst ist allgemein entlehnt ; vergl. bei. (65).
np. döstdär ist eine sekundäre Missbildung.
583. {i)dös 'die letzte, vergangene Nacht'.
aw. daosatara- 'abendlich, westlich'; phlv. dös,
dösastar, vergl. s(i)dös (geschrieben s(i)t") ') ; ai. dösä-,
kurd. duc; afy. LW. dös; oss. disson 'gestern Abend'
(116); bei. dost (95).
Bartholomae, BB. XV, 209 möchte auch in
aw. daozanhahe, duzanha-, daozavat u. a. m. die ur-
sprüngliche Bedeutung 'finster, nächtlich' finden.
584. (^)dös 'Schulter .
aw. daösa- 'Schulter (ZPGL); phlv. dös; ai. dos-,
dösdn- 'Vorderarm, Arm'.
```


## [2026-09-05T20:54:21.856Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5215,5245p' HRN.txt\necho \"=== leaf containing it ===\"; awk 'BEGIN{RS=\"\\f\"} /582\\./{print NR\": \"substr($0,1,60)}' HRN.txt | head -5",
 "description": "Horn entry for dost"
}
```


## [2026-09-05T20:54:22.687Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN javidan/jav ===\"; grep -n \"jav\\b\\|jäv\\|jāv\\|kauen\" HRN.txt | head -20",
 "description": "Horn chew"
}
```


### [2026-09-05T20:54:23.677Z] TOOL RESULT

```
öud, sar. düt.
580. dür 'fern'.
ap. dura- 'fern'; aw. dura''; phlv. dür\ ai. dum-,
kurd. dür; af/. liri; bei. d/lr, dJr (89); wa;^. JJr,
yidg. lüro,
581. dö»eyi 'Hölle*.
aw. (anMtis) daozaMahe, vergl. duzah" 'Hölle';
phlv. dömx (päz. diiza/, dorn/), dö^a/ (PPGl.) —
dusähü darf man das Pchlevivvort nicht losen; denn
*J Wa/. dayOWj sar. diiyoic *Molke*.
Hör II, Qrundriss d. neup. Etymologie. 9- 130 —
erstens könnte dusähü nicht 'böse Welt*, sondern nur
*selilechtweltig' bedeuten, und zweitens findet phlv.
dösa/ seine einfache Erklärung darin, dass im Mittel-
persischen altes duZ'y aus- nur als dn§-, nie als duz-
erscheint.
afy. LW. döyax bezw. dözax\ kurd. duze*, bei. dözak,
döze, n. döza/, dözc (66); arm. LW. dzo/ß.
582. döst 'Freund', dösfär, dösii,
ap. daustar- 'Freund'; aw. vergl. zaosa- 'Wunsch';
phlv. döst, döstth, vergl. dös(i)s)t, döäak; ai. vergl.
josa-.
bei. vergl. zar-ßs geldliebend' (181).
np. döst ist allgemein entlehnt ; vergl. bei. (65).
np. döstdär ist eine sekundäre Missbildung.
583. {i)dös 'die letzte, vergangene Nacht'.
aw. daosatara- 'abendlich, westlich'; phlv. dös,
dösastar, vergl. s(i)dös (geschrieben s(i)t") ') ; ai. dösä-,
kurd. duc; afy. LW. dös; oss. disson 'gestern Abend'
(116); bei. dost (95).
Bartholomae, BB. XV, 209 möchte auch in
=== leaf containing it ===
63: - 41 —
Gehört hierher vielleicht auch np. evän 'Vorhalle
152: - 130 —
erstens könnte dusähü nicht 'böse Welt*, sonde
332: dez 568 u. Anm-, 594.
```


### [2026-09-05T20:54:23.725Z] TOOL RESULT

```
=== HRN javidan/jav ===
3890:415. Jävf^den 'kauen, zäviden,
3892:phlv. vergl. jütan 'kauen, verzehren' (West: jaldanö),
3894:kurd. /Miw, jün 'kauen'; afy. Sövul, zöyal; he], jfayag,
3897:jävJden aus ar. gzhau-, altir. yiaw-, einer w-Bildung
3978:SiW.yava- *6etreide'; phlv. jav bezw. yav; ai. yäva-.
3980:(147); bei. /ö, jav, n. jau 'Gei-ste' (179); si/n. yavoj,
3983:niäz. javän.
3987:LW. kurd. juvän; afy. javän; bei. javan (111).
5941:aw. \/jav- 'eilen*, Java, javarö (?, Geldner, BB.
5943:zöt); ai. i^jav-, jdvate *eilen*.
12610:jävBd 414.
12611:jävedän 414.
12612:jäviden 4 1 5.
17680:l^Jav-, jävate 878.
18517:m. javän 429.
19820:jävän 429.
22981:nslov. gorjav 895.
```


## [2026-09-05T20:54:34.021Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3885,3905p' HRN.txt\necho \"=== leaf/page for 415 ===\"; awk 'BEGIN{RS=\"\\f\"} /415\\. Jävf/{print NR}' HRN.txt\nfor i in 114 115 116; do echo \"--leaf $i head--\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | grep -o -- \"- *[0-9]\\+ *—\" | head -3; done",
 "description": "Read Horn 415 and page"
}
```


### [2026-09-05T20:54:36.491Z] TOOL RESULT

```
KZ. 27, 101 unter (Berücksichtigung von Geldner,
BB. 15, 261).
414. Jäved^) *ewig', javMan.
aw. yava^tat- 'Ewigkeit*, yave *für ewig ; phlv. yä-
vetan (PPGl.), arm. LW. yav^t^ yavitean, yavitenakan.
415. Jävf^den 'kauen, zäviden,
g. jovadmün,
phlv. vergl. jütan 'kauen, verzehren' (West: jaldanö),
jüyend (vd. 17 (9))^).
kurd. /Miw, jün 'kauen'; afy. Sövul, zöyal; he], jfayag,
n. jäy (176).
Bartholomae meint (briefl. Mitteilung), dass np.
jävJden aus ar. gzhau-, altir. yiaw-, einer w-Bildung
zu i^yhas-, stammen könne (vergl. sravati — sarati
u. a. m. bei Per Persson, Wurzelerweiterung).
Dann müsste die Grundbedeutung Verzehren* sein.
') Nicht *Gefä88*, wie ich ZDMG. 43, 48 übersetzt habe.
*) Reimt auf umed (Vis und Rämln, Seite 85 Vers 3 v. u.).
») Fr. Müll er 's Lesung .^ar^rmw (WZKM. 5, 380J ist unmöglich.— 94 -
416. Jäh 'Würde, Stellung.
ap. ^ya&a-, vergl. ai. yä^a- f Gang)*.
=== leaf/page for 415 ===
115
--leaf 114 head--
--leaf 115 head--
--leaf 116 head--
```


## [2026-09-05T20:54:42.704Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /chew,  tr\\.  and  intr\\.  v\\./{print \"leaf(1based)=\"NR}' KLN_1966.txt\necho \"---\"; sed -n '7370,7382p' KLN_1966.txt | cut -c1-200",
 "description": "Find Klein leaf for chew"
}
```


## [2026-09-05T20:54:44.537Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print('---'); print(d['KLN'].get('lookup_hint'))\nprint('=== MON ==='); print(json.dumps(d['MON'],ensure_ascii=False)[:2000])\nprint('=== BQT ==='); print(json.dumps(d['BQT'],ensure_ascii=False)[:2500])\n\"",
 "description": "Get KLN/MON/BQT offsets"
}
```


### [2026-09-05T20:54:44.595Z] TOOL RESULT

```
leaf(1based)=156
---
chevet,  n.,  the  apsidal  east  end  of  the  choir  of a  church  ( archil .)  —  F.,  ‘pillow,  apse’,  fr.  OF. chevetz,  fr.  L.  capitium,  ‘covering  for  the  head’, fr.  caput,  ge
chevin,  n.,  the  chub.  —  Cp.  F.  chevanne;  of  un¬ known  origin.
cheviot,  n.,  cloth  made  from  wool  of  sheep  of Cheviot  Hills.  —  Named  from  the  Cheviot  Hills, the  range  forming  the  borderland  between  Eng¬ land  and  Scotland.
chevron,  n.,  t)  a  beam,  rafter;  2)  a  shaped mark  (her.)  —  F.,  ‘rafter,  joist,  chevron’,  fr. VL.  *capridnem,  acc.  of  *eaprid,  fr.  L.  caper, gen.  capri,  ‘goat’.  See  c
chevrotain,  n.,  a  very  small  ruminant  mammal, (Tragulus  kanchil)-,  the  mouse  deer.  —  F.,  di¬ min.  of  OF.  chevrot,  itself  a  dimin.  formed  fr. chievre  (F.  chevre),  ‘she-goat
chevy,  also  chivy,  n.,  a)  a  hunting  cry;  b)  a  hunt, chase;  tr.  and  intr.  v.,  to  hunt,  chase.  — Shortened  from  Chevy  chase,  from  the  1 6th cent,  ballad  of  Chew  Chase,  a  
chew,  tr.  and  intr.  v.  —  ME.  chewen,  fr.  OE.  ceo-
i
i
wan,  rel.  to  MLG.  keuwen,  Du.  kauwen,  OHG. kiuwan,  MHG.  kiuwen,  MG.  kiiwen,  ‘to  chew’ (whence  G.  kauen,  ‘to  chew’;  but  cp.  G.  wieder- kauen,  ‘to  chew  the  cud’,  fr
Derivatives:  chew,  n.,  chew-er,  n.,  chew-y,  adv. cheyney,  n.,  a  woolen  fabric.  —  Lit.  ‘china  ware’. The  word  represents  the  former  pronunciation of  China.
Chian,  adj.,  pertaining  to  the  island  Chios.  — Formed  with  suff.  -an  fr.  L.  Chius,  fr.  Gk.  XCog, name  of  an  island  off  the  coast  of  Asia  Minor. Chian,  also  chian,  n.  —
chiasma,  n.,  a  crossing  or  decussation  ( anat .)  — ModL.,  fr.  Gk.  xta.csy.01,  ‘two  things  placed  cross¬ wise’,  which  is  rel.  to  xfaopuk,  ‘a  placing  cross¬ wise’.  See
```


### [2026-09-05T20:54:46.691Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
=== MON ===
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"], "page_offset": null, "covers_etymology": true, "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6
=== BQT ===
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/git/rishe/data/verification/sour
```


## [2026-09-05T20:55:03.082Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 154 155 156 157; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -nE \"^[^a-zA-Z]*[0-9]{3}[^a-zA-Z0-9]*$|CHE|chee\" | head -6; done",
 "description": "Look for page numbers in Klein leaves"
}
```


### [2026-09-05T20:55:04.611Z] TOOL RESULT

```
=== leaf 154 ===
26:270
27:271
=== leaf 155 ===
13:Derivatives:  checkmate,  n.  and  tr.  v. cheeky,  adj.,  divided  into  squares  of  alternate tincture.  —  Formed  fr.  check,  n.,  ‘a  sudden stop’,  with  adj.  suff.  -y.
14:Cheddar  cheese,  Cheddar,  also  Cheddar,  n.  — Named  fr.  Cheddar,  Somerset,  England,  where it  was  originally  made.
16:272
19:cheek,  n.  —  ME.  cheke,  fr.  ceace,  ‘jaw,  cheek’, rel.  to  MLG.  kake,  Du.  kaak,  ‘jaw,  cheek’;  of uncertain  origin.
20:Derivatives:  cheek,  tr.  v.,  cheek-y,  adj.,  cheek- i-ly,  adv.,  cheek-i-ness,  n.
21:cheenar,  n.  —  A  variant  spelling  of  chinar.
=== leaf 156 ===
19:Cheshire  cheese.  —  So  called  because  it  is  made chiefly  in  the  county  of  Cheshire  in  England.
23:chessel,  n.,  cheese  vat.  —  Compounded  of  cheese and  well,  n.
26:275
=== leaf 157 ===
22:276
23:277
31:Goth,  kinnus,  ‘cheek’,  and  cogn.  withOI.  hanuh, ‘chin’,  Avestic  zanu-  (in  compounds),  ‘chin’, Toch.  A  sanwem ,  ‘both  jaws’.  Arm.  cnaw't, ‘jawbone,  cheek’,  Gk.  ylvus,  ‘the  lower  jaw, cheek,  chin’,  ysveiov,  ‘chin’,  L.  gena,  ‘cheek’, Lith.  zandas,  ‘jawbone’,  Lett,  zuods,  ‘chin’,W„ Bret.,  MCo.  gen,  ‘jawbone,  chin’,  OIr.  gin,  giun, ‘mouth’.  Cp.  gena,  genial,  ‘pertaining  to  the chin’,  genio-,  genyo-,  gnathic.
32:Derivatives:  chin,  tr.  v.,  chinn-ed,  chinn-y,  adjs. China,  n.  —  Fr.  Chin  or  Hsin,  name  of  the  First Dynasty  of  China  (255-206  B.C.E.).  This  word lit.  means  ‘man’.  Cp.  cheyney,  chine,  sinology. Cp.  also  serge,  Seric,  silk, china,  n.  —  Short  for  orig.  chinaware,  i.e.  ‘ware from  China’.  See  prec.  word, chinar,  also  cheenar,  n.,  the  Oriental  plane  tree ( platanus  Orientalis).  —  Pers.  chinar. chinch,  n.,  the  bedbug.  —  Sp.  chinche,  fr.  L.  ci- micem,  acc.  of  cimex,  ‘bedbug’.  See  cimex. chinchilla,  n.,  a  small  S.  American  rodent.  — Sp.,  a  hybrid  coined  from  a  S.  American  native name  and  the  Spanish  dimin.  suff,  -ilia. chin-chin,  n.,  polite  salutation;  ceremonious  talk.
```


## [2026-09-05T20:55:17.110Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 dust ===\"; grep -n \"دوست\" BQT_v2_pages.txt | head -5 | cut -c1-300\necho \"=== leaf for دوست ===\"; awk 'BEGIN{RS=\"\\f\"} /دوست/{print NR}' BQT_v2_pages.txt | head -20\necho \"=== MON zaq ===\"; grep -n \"زاق\" MON_part1.txt MON_part2.txt | head -10 | cut -c1-400",
 "description": "Grep BQT and MON"
}
```


### [2026-09-05T20:55:18.827Z] TOOL RESULT

```
=== BQT v2 dust ===
772:          ‫زبرا که جان زنده بدوست ‪ -‬ک‬                                               ‫معشوق ومطلوب باشد ‪.‬‬
947:‫ونام کلی حم هت وآن در هندوستان‬      ‫باشف ‪-۴‬‬       ‫و بیار‬       ‫دده‬
1096:                              ‫بعنی پنشیند ‪.‬‬                ‫قومی باشندفرومابه وصحرا شین درهندوستان‪.‬‬
2464:‫ماوراء‌النهر مردم بازاری و کم اصل و جلف‬              ‫کار ‪٩‬‏‬   ‫سلاحی استت که آنرا در هندوستان‬
2676:                   ‫وبعربی سعتر خوانند گ‬             ‫ومهمان دوست می باشند وشمشیر را درآن شهر‬
=== leaf for دوست ===
18
21
23
45
49
51
57
61
64
71
110
123
125
130
131
132
142
145
149
157
=== MON zaq ===
MON_part2.txt:763:غدد بزاقی و غدد مترشحهةٌ عرق. این گونه 
MON_part2.txt:779:اشکی واقعند. غده‌های بزاقی: (پز.) 
MON_part2.txt:782:مترشحه مخاط دهان مجموهاً بزاق دهان را 
MON_part2.txt:783:می‌سازند. غده‌های بزاقی عبار تند از سه زوج 
MON_part2.txt:794:جزو غده‌های بزاقی می‌باشند و ترشح آنها 
MON_part2.txt:8088:غدد بزاقی زیر زبانی و تحت فکی وجود 
MON_part2.txt:8537:کنندهة ترشحات بزاق و تسکین دهندة 
MON_part2.txt:34866:گلیز: «اهع [لزاق| (۰) آبی لز ج که ار دهان 
MON_part2.txt:48032:ارزاق. 
MON_part2.txt:73486:وسیلة ار تزاق بودن (نبودن).
```


## [2026-09-05T20:55:25.829Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"\\[pdf page [0-9]*\\]\" BQT_v2_pages.txt | head -3; echo \"...\"; grep -c \"pdf page\" BQT_v2_pages.txt\necho \"=== search for printed 897 ===\"; grep -n \"۸۹۷\\|897\" BQT_v2_pages.txt | head -10",
 "description": "Inspect BQT v2 page tags"
}
```


### [2026-09-05T20:55:25.900Z] TOOL RESULT

```
...
0
=== search for printed 897 ===
15166:      ‫بقیه در صفحةٌ ‪۸۹۷‬‬
23934:   ‫‪١۹‬ے‏ در فهرست ولف هل از فرهنك شاهنامةٌ عبدا لقادر نمرة ‪ ۵۸۹۷۲‬همین معتی آهده‪.‬‬
39369:  ‫‪ ۷‬ب‪-‬ونالی ‪ 5۵05100۹‬بدعنی استاد » زبردست ‪.‬کیکه دارمور‬                     ‫ابا ‪. ۸۹۷-۵۹۲‬‬
40727:  ‫=وی ‪ .065 - ۷۲110۳7‬اوستا ‪( 811897321 60625‬بشت‬
```


## [2026-09-05T20:55:26.238Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30",
 "description": "ref_page help"
}
```


### [2026-09-05T20:55:27.988Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
```


## [2026-09-05T20:55:34.745Z] TOOL CALL #34: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null && ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -30",
 "description": "Check OCR cache"
}
```


### [2026-09-05T20:55:34.789Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1462.png
1462.txt
1471.png
1471.txt
```


## [2026-09-05T20:55:35.206Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15150,15180p' BQT_v2_pages.txt | cut -c1-200",
 "description": "Context around page 897 note"
}
```


### [2026-09-05T20:55:35.266Z] TOOL RESULT

```
  ‫‪ - ۱‬از ‪ :‬خوهله(خوهلکه) ی‬                                     ‫‪۲‬‬   ‫خوهلی* لغت فری ‪ ۹۳‬و‬                  ‫¬‬    ‫خوهل�

      ‫(اب دهان) «واژه‌نامه‪ ۹۱۳‬ار کت ‪ 2‬خبو‪,‬خدو‪.‬و رکف ‪ 0‬جح‬                                  ‫‪10‬‬       ‫‪ ۹۳ ۷‬
                                            ‫و هوشمان اس ‪:‬‬                    ‫خور (ھ‪.‬م‪ (.‬ورك‪ :‬امشق ‪۲‬‬                     ‫=‬    ‫�

  ‫فریدون است پنداری‌بز بردرع وخوی اندره‬                                          ‫سباوش است پنداری‌میان شپرو کوی‌اندر‬
      ‫دقیقی طوسی ‪« .‬لغت فری ‪۱۲۵‬‬
  ‫‏‪( - ٩‬عر) «خوی ‪ ۰‬زمین پت ميان دکووه است » وخوی نرم از زمین است ‪« ».‬شرح‬
      ‫‪ - °‬بهلوی ‪ . ) 12۷1 ( 12۷2‬اوستا ‪ . :21062۷-‬هندی باستان ‪20۵۷5‬‬                                                               ‫قاموس؛
      ‫‪,‬ردی ‪161 ۰ ×۵‬‬
                  ‫(عرق) «اسفا‪۲ :۱‬ص‪,»۸۳‬بلوچی ‪ 1۵21‬ایا ‪ , ۳۲۰‬وخی أنظ «ایضاً ‪ 5۹۲6‬ک‬
  ‫‪.‬‬    ‫رك‪ :‬خوه ورك ‪ :‬لفت قرس ‪۵ ۴۲‬‬                        ‫(عرق) ‪ ۱‬استی ‪dex‬‏ ‪ ۰‬سربکلی ‪hdiax‬‏ «اسشق

          ‫سنگدلی خوی تست ومهرمرا خوی ‪.‬‬                                               ‫‪- ۱‬خوی تو باخوی‌من بنیز نسازد‬
  ‫‪.>۵0‬‬    ‫‪۹‬‬        ‫‪«۰‬لفت فری‬   ‫خسروی‬

      ‫بقیه در صفحةٌ ‪۸۹۷‬‬
  ‫‪۷ 6‬‬                                                                                                           ‫خوی درد‬

 ‫‪-‬‬        ‫هم هت‬    ‫باشد ‪ - ۴‬و نمعتی خود وخوشتن‬                     ‫خوی درد « بکراولرالی‌وسکون‬
‫وقلبه را نگیوزبند وآن چویی اس (‪ )۲‬که کاو‬                       ‫بیلقطة‬       ‫ودال‬   ‫ابجد مفتوح‌برا‬   ‫ودال‬  


‫آهن رایدان محکم سازند وزمین را شیارکنند ›‬                       ‫أن چنان باشد که‬           ‫و‬   ‫‪۰‬‬   ‫است‬   ‫زد�

 ‫‪ ۳‬بعضی کاوآهن را گفته‌اند ‪ - ۴‬و نمعتی خوت‬                     ‫اطراف انگت بخته شود و چرك کند و گاهی‬
‫وبن دکه‬ ‫ونيك‌هم آهده است ‪ - ۴‬و وجودرا نگیز‬
  ‫نقیض عدم است ‪ -‬ونوعی ازبافتة کتان باشد ‪#‬‬                                                                  ‫گوند ‪. ۱‬‬
 ‫خو بشتی د ار (‪ = )۳‬شخصی راگوند‬                                    ‫خوبه = بائالك مجهول ‪:‬روزن هرسه‪,‬‬
 ‫که پیوسته خود را او دا دارد و فراغت دوست‬
                                                                                       ‫مباحثه ومنافشه رگاوند‬
```


## [2026-09-05T20:55:50.201Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== daust ===\"; grep -n \"aust\\|dost\\|dōst\\|3057\\|zao\" BQT_v2_pages.txt | head -20 | cut -c1-250\necho \"=== headword dust entry ===\"; grep -n \"دوست ‪\\|‫دوست\\|دوستی\" BQT_v2_pages.txt | head -10 | cut -c1-250",
 "description": "Search BQT v2 for dost etymology"
}
```


### [2026-09-05T20:55:50.281Z] TOOL RESULT

```
=== daust ===
=== headword dust entry ===
772:          ‫زبرا که جان زنده بدوست ‪ -‬ک‬                                               ‫معشوق ومطلوب باشد ‪.‬‬
8187:                                                                                    ‫دوست دارد ‪.‬‬
8968:             ‫راکش منوب بدوست ‪.‬‬
11926:‫خز یه ‪ = ۲‬پروزن ندیده » شخصی را‬                          ‫دربای گیلان‌منسوب بدوست ‪ ۴‬ونام میارزی هم‬
13279:                                                                ‫دوست ودوستی باشد‪ .‬ک‬
14485:‫جمبح امباب زراعت کردن و برزیگری را مهيا‬                 ‫خور وافم‌میشود متعلق بدوست ‪-‬ونام روزبازدهم‬
14725:                    ‫برکف آنرا بخورلد يمر ند‪.‬‬                            ‫‪:‬دوست ‪ -‬ونام شپری هم هت ‪۴‬‬
17474:  ‫در پارسی «وشتی » بمعنی زیبایی است « دوستی‪ .‬نام‌نامه‬
17540:                                                     ‫کنند و دوستی لمایند ‪« ».‬کلتان ‪. ۱۶۱2‬‬
21141: ‫دوستکانی ‏‪ - ٩‬بر وزن ومعتن‬
```


## [2026-09-05T20:55:56.169Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:897 --image 2>&1 | tail -40",
 "description": "Fetch BQT page 897"
}
```


### [2026-09-05T20:55:57.740Z] TOOL RESULT

```
no scan of BQT covers printed page 897 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:56:00.749Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\n\"",
 "description": "Check BQT scans coverage"
}
```


### [2026-09-05T20:56:02.364Z] TOOL RESULT

```
[
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
]
```


## [2026-09-05T20:56:14.153Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nprint(\"n leaves\",len(leaves))\n# find leaf containing 'بقیه در صفح' 897\nfor i,l in enumerate(leaves):\n    if 'بقیه در صفح' in l and '۸۹۷' in l:\n        print(\"leaf idx (0-based)\",i)\n# print persian digit standalone tokens for a few leaves\ndef pnums(l):\n    return re.findall(r'[۰-۹]{3,4}', l)\nfor i in range(0,len(leaves),1):\n    pass\nEOF",
 "description": "Calibrate BQT v2 leaves"
}
```


### [2026-09-05T20:56:15.874Z] TOOL RESULT

```
n leaves 684
leaf idx (0-based) 257
```


## [2026-09-05T20:56:29.581Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\n# find leaves whose text contains 'دوستکان' or many 'دوست'\nfor i,l in enumerate(leaves):\n    c=l.count('دوست')\n    if c>=3:\n        print(i,c, re.sub(r'\\s+',' ',l)[:150])\nEOF",
 "description": "Find BQT leaf with dost entries"
}
```


### [2026-09-05T20:57:41.391Z] TOOL RESULT

```
357 24  ‫دوس‬ ‫و‬ ‫عزیز دارندش م آمدہ است ‪ ۷‬وياله بز رکه‬ ‫را یکی‬ ‫چبانند با خود‬ ‫باجیزی‬ ‫چیز که ر‬ ‫کزون ‪. ۸‬‬ ‫را ی‬ ‫وابندند ‪۰‬‬ ‫دوستکانی ‏‪ - ٩‬ب
```


## [2026-09-05T20:57:54.490Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nfor i in (356,357,358):\n    print(\"=\"*20,\"leaf\",i)\n    print(leaves[i][:2600])\nEOF",
 "description": "Print BQT leaves 356-358"
}
```


### [2026-09-05T20:57:56.173Z] TOOL RESULT

```
==================== leaf 356
‫پاسس‬                                                                                                   ‫ذو روژی‬

‫‪ ۱‬دور نه ‪ = ۱‬و دوژله ‪.‬ضم اول و واو‬                          ‫دو دودی = با زای قطه‌دار بتحتالی‬
‫مجهول وفتح زای هوزوزای فارسی ونون » لش‬                                  ‫تتندرستی را گویند ‪.‬‬
                                                                                          ‫کشیده » وصح‬
                  ‫گرواند ‪.‬‬
                         ‫زنبور ویشه وامثال آ‬                ‫دوده ‪ ۱۰‬طامول بر وزن شوره ‪.‬‬
‫دور = بم اول و واو مجیول وفتح‬                                                     ‫مرطبان کوچك را کوبند ‪-‬‬
‫زای فارمی گ‪.‬یاهی باشد که ثمرآن گرهیاست‬                                           ‫و فتح اول دابره و پیمانة(‪)۱‬‬
‫خاردار ببزرگی فندق» ومغزی‌درمیان دارد وچون‬                                       ‫شراب ‪ -‬وبمعنی زلف‌هم آمده‬
‫بجامه بچید جدا نشود ؛ وبسضی گوبند لاكاست‬                                                                 ‫است ‪.‬‬
‫وآن صمع مانندی باشد که بدان‌کارد و شمشیر‬                                         ‫دودای ‪ -‬با زای‬
‫ومانندآن را بدسته چسبانند (‪ » )۲‬وبحذف های‬                                        ‫نقطه دار بروزں ومعنی دورای‬
                                 ‫ات‬     ‫هوزهم ای‬                 ‫دوره‬           ‫وربی‬
                                                                                   ‫است که نای حطر بان‌باشد ع‬
‫دور دنه ‪ ۰ ۷‬با زای فارسی وتحتانی‌بر‬
                                    ‫‪. _ ۵‬‬
                                                            ‫مز مار خوانند ‪ - ۳‬وبا ثانی‌مجهول دو ژاننده را‬
‫وزن بوزینه‪ ,‬بمعنی‌دوزنه است که یش جانوران‬                                                           ‫کویتت ‪۴‬‬
                                     ‫گز نده باشد ‪۰‬‬
                                                             ‫دودخ؟ = معروف است و آن نقیض‬
‫دوسانید ‪ ۰ ۵‬بساین بی‌قطه بروزن‬                               ‫اجنس است‬        ‫ونابه ازصدبت‬
                                                                                        ‫باشد © ‪ -‬ک‬         ‫بپشت‬
                    ‫جوشانید » بعنی چپانید(‪. )۳‬‬              ‫ترد ارباب معرفت ‪ -‬وبزم رشك وحد است فزد‬
                                                             ‫عشاق ‪ -‬وسختی ودرشتی وکلفت ورنج ‪ -‬و محل‬
‫جوشایدن » بمعنی چبایدن بائد اعم ازآنکه‬                                                     ‫عذاب کفار باشد ‪٩‬‏ ‪.‬‬

  ‫(‪)۳‬چك‪ :‬چسانید‪.‬‬          ‫(‪ )۲‬چك ‪ :‬چپانند؛ خم‪ : ۳‬بجپانند ‪.‬‬                      ‫(‪ )۱‬خم‪ : ۳‬دايرة پیمانه ‪.‬‬

  ‫*المدسد» وامرادوری» ودرتر کی «رو
==================== leaf 357
  ‫دوس‬                                                                                              ‫و‬

‫عزیز دارندش م آمدہ است ‪ ۷‬وياله بز رکه‬                  ‫را یکی‬          ‫چبانند با خود‬    ‫باجیزی‬
                                                                                             ‫چیز که ر‬
                              ‫کزون ‪. ۸‬‬
                                     ‫را ی‬                                                        ‫وابندند ‪۰‬‬

 ‫دوستکانی ‏‪ - ٩‬بر وزن ومعتن‬
                                                        ‫دوست = بروزن پوست؛» بمعتی محب‬
‫و بیاد‬     ‫واق‬
             ‫شب‬‫صردن‬
                  ‫م خو‬
                     ‫دوستکامی باشدکه می‬                ‫رنگه ‪ - ۱‬و یمعتی « دوعدداست »‬
                                                                                     ‫وبکدل وبك‬
‫دوستان اوستپب‪-‬الة پرشرابی را نیز گوبند که‬                                                          ‫باشد ‪.‬‬
 ‫کسی درئوبت خودبدیگری تکلف کند و‪-‬بمعنی‬                  ‫دوست لین = بابای‌ابجد بروزن پوست‬
                                     ‫سار وياله‬
                                                     ‫چين ‪ ۰‬نام روز بیت و دویم است از ماحهای ‪.‬‬
         ‫‪Ni‬‏‬                    ‫بزرکه‌هم آمدء‬
‫‪۳‬‬‫‪۲ ۳‬‬                       ‫‪/‬‬         ‫است ‪۱ 3.‬‬
                                                                                                   ‫ملک ‪.‬‬
                                                       ‫نقیض دشمن کاماست ›‬     ‫دوستگا م‬
                                                        ‫پمعنی اینکه‌کارهایش برحسب مطلوب وبمراددل‬
                                                        ‫دوستان باشد ‪ -‬وبمعنی شراب خوری با دوستان‬
                                                                                  ‫و بیاد ابشان هم هست ‪.‬‬
                                                       ‫دوست کامی ‪ ۰ ۲‬یش دشمن کامی‬
                                                       ‫است‪ - ۴‬وشراب خوردن با دوستان وبیاد ایشان‬
                                                                                                 ‫اشد ‪. ۵‬‬

                                                       ‫با نون بروزن و معنی‬             ‫دوستکان‬
                                ‫‪ ۰‬داءا(تملب‬    ‫روف‬     ‫دوستکام است که می‌خوردن با دوستان ویرباد‬
                                 ‫را قیده دهد ‪.‬‬         ‫ابشان‌باشد‪ .‬وبمعنی‌ممشوقه وباراکه ازجان ودل‬

  ‫‪ - ۱‬پهلوی ‪ « 1501‬مناس ‪« » ۲۷۲‬اسشق ‪ . › ۲۸۵‬از ‪212‬ا‪5‬لا‪ .21‬از پارسی با‪-‬تان‬
   ‫‪« ۲21511210‬بارتولمه ‪6۷٩‬‏ نردبکه ‪۸‬ه“ «اسشق ‪ ۲۸۵‬ورك‪ :‬هوبشمان 
==================== leaf 358
     ‫—~‪—~AAA‬‬                                                                                                               ‫دوسرألی‬

 ‫ژولیده» بمعنی چبیده(‪)٤‬‏ وخودرا چسبایده(ه)‬                      ‫دو سرالی ‪ = 1‬بفتح اول بر وزن لن‬
                                   ‫باشد ‪.‬‬                              ‫ده وسطبر وبزر که باشد‪.‬‬
                                                                                            ‫کعننی‬
                                                                                                ‫ترالی » بم‬
     ‫نش ‪ ۰‬بمکعنتیف‬
                 ‫دوش م بر وگزو‬                                   ‫دو سر د هلیز ‪ -‬کنابه از عناصرارعه‬

‫و امر‬           ‫باشد ا ‪ -‬وش گذشته را نز گونند ‪۷‬‬                        ‫‪-‬ای خمه را نگیوزبند ‪.‬‬
                                                                                           ‫حو‬‫اوست‬
                   ‫از دوشیدن هم هت نی بدوش ‪.‬‬                    ‫«ابه‌ازهفت کوکب‬
                                                                              ‫دو سر قندیل کن‬
                                                                ‫است ‪ -‬وهرستار روشن را نز گفته اندو کنابه‬

‫که انرا مسد‌وشند همجو گوسفند وگاو و امثال‬
                                                                                                         ‫‪.‬‬     ‫از فلك هم هت‬

         ‫تهه‬
           ‫اهشهرچ‬
                ‫دت ک‬
                   ‫آن ‪ -‬وکنابه ازشخصی اس‬                        ‫دو سر ی = بفتح اول بروزن کوثری '‬
                           ‫باشد ازو بتدریج بگیرند ‪.‬‬             ‫بمعنی‌دوسرالی است که‌بزر کههوسطبرو گنده‌باشد‪.‬‬
                                                                ‫دوسنك ‪ ۴‬ب باانی جهول بر وزن‬
‫داشته باشد وآنرا بگرردن مجرمانو کناهکاران‬                              ‫موبند » بعنی بچسبند(‪ )۱‬وملاصق شوند ‪.‬‬
     ‫‪.‬‬     ‫گذارند ‪ -‬ولوعی از پنکان دوشاخ هم هت‬                  ‫دو سنكه ‪ = ۴‬بروزن دوزنده * بمعنی‬
                                                                ‫چبنده (‪ )۲‬باشد ‪ -‬و زمین لغزنده ‪ -‬وگل‬
‫ان کنابه‌ازشادی کردن‬            ‫بر‬    ‫دوش‬
                                                                ‫چسبنده(‪ )۲‬را نگیوزنند ؛ ویکسرثالث هبمنظر‬
                                                   ‫باشد ‪.‬‬
                                                                                                                      ‫آمده است ‪.‬‬
 ‫دوشنه ‏‪ - ٩‬م اول و ثانی مجهول‬
                                                                ‫دو سین = بر وزن بوسیدن » بمعنی‬
‫وفتح ثالث و نون » ظرفی باشد که درآن شیر‬
```


## [2026-09-05T20:58:16.999Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nl=leaves[357]\ni=l.find('پهلوی')\nprint(l[i-200:i+1400])\nEOF",
 "description": "Read Mo'in footnote on dost"
}
```


## [2026-09-05T20:58:18.259Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins gyeu ===\"; grep -n \"gyeu\\|g(i)eu\\|geus-\\|ghaid\" AHD_watkins1985.txt | head -20\necho \"=== AHD goat ===\"; grep -n \"^goat\\|goat\\.\" AHD_watkins1985.txt | head -10",
 "description": "Grep Watkins AHD"
}
```


### [2026-09-05T20:58:18.806Z] TOOL RESULT

```
           ‫‪ ۰‬داءا(تملب‬    ‫روف‬     ‫دوستکام است که می‌خوردن با دوستان ویرباد‬
                                 ‫را قیده دهد ‪.‬‬         ‫ابشان‌باشد‪ .‬وبمعنی‌ممشوقه وباراکه ازجان ودل‬

  ‫‪ - ۱‬پهلوی ‪ « 1501‬مناس ‪« » ۲۷۲‬اسشق ‪ . › ۲۸۵‬از ‪212‬ا‪5‬لا‪ .21‬از پارسی با‪-‬تان‬
   ‫‪« ۲21511210‬بارتولمه ‪6۷٩‬‏ نردبکه ‪۸‬ه“ «اسشق ‪ ۲۸۵‬ورك‪ :‬هوبشمان ‪۳۸‬ه‪ .‬اورامانی ‪900‬‬
   ‫> ‪ .‬کیلکی ‪tsud‬‏ » فریزندی ویبرای ونطنزی ‪sûd‬‏ «‪۱ .‬ص ‪-.۹۸۲۰‬نکری‬                       ‫اورامانی ‪۲۲۱‬‬       ‫ك‬
                                                            ‫هب مرخه‌بی ‪ .۵« 651‬ص ‪: ۸۸۱‬‬                    ‫‪4‬‬
            ‫که دل هر دو در صرف آوست ‪.‬‬                        ‫دوست‬
                                                                ‫از خدا دان خلاف دشمن و‬
   ‫«کلتان ‪. ۷:۰‬‬
                                 ‫ی‬     ‫کم‬     ‫‪ E‬از ‪ :‬دوست‬    ‫‪۳‬‏‬           ‫رك ‪ :‬دوستکان ‪.‬‬     ‫‪۳‬‬
    ‫(مصدری )‪ .‬رك ‪ :‬دوسنکالی ‪9‬‬
  ‫ومطا‪.‬اق دلخواه دوستان ‪« :‬وملطان مسمود رضی لمعنه صمادت ودومتکامی مامد تا‬                    ‫‪۴‬‬

   ‫=وستکاں ‪ .‬رك‪ :‬دوستکام‪٠ ‎‬‬
                          ‫‪ ١‬د‬            ‫ورك‪ :‬دوستگانی ‪۰‬‬          ‫‪8‬ے‬         ‫‪۹۰‬‬   ‫بشبورقان؛ «تاریخ هقی‬


          ‫دوستگانرا برشك‌مژه بر کرد زخواب‪‎‬‬                  ‫عاشق ازغربت بازآمده باچشم پرآب‬            ‫‪۷‬‬
         ‫ازیس پرده برون آمد با روی چوماه‪. ‎‬‬             ‫دوستگان دست پآرورد وبدرید نقاب‬
   ‫یرهچونم« ‪‎‬یلاغماد ‪. ٩۱۵۶‬‬
   ‫‪ - ۸‬امروز ظرف چینی بزرگی که در مجالس عزاو مساجد شربت کنند و بقول عوام‬
        ‫‪ 1001-0501‬کوبند وممرب آن دسنکان «ممجم الا
```


### [2026-09-05T20:58:18.880Z] TOOL RESULT

```
=== AHD watkins gyeu ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
501:geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, cedsan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE. 2. Zero-grade *gus- in Germanic *kuz-, becoming *kur- in Old Norse Valkyrja, “chooser of the slain,” Valkyrie (valr, the slain; see wele-2). 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST?), GUSTO; DISGUST, RAGOUT; b. Latin gustdre, to taste: DEGUST. [Pok. geus- 399.]
505:ghaido-. A goat. Germanic *gaitaz in Old English gat, goat: GoaT. [Pok. ghaido- 409.]
557:gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(iJeu- 400.]
1142:HELMINTH; ANTHELMINTIC, PLATYHELMINTH. [Pok. 7. uel- 1140.] wel-‘, To tear, pull. 1. Suffixed form *wel-do- in Latin vellere, to tear, pull: AVULSE, CONVULSE, DIVULSION, EVULSION, REVULSION, SVELTE. 2. Suffixed form *wel-no- in Latin vullis, shaggy hair, wool: VELOURS, VELVET, VILLUS [Pok. 8. wel- 1144.] wele-'. Wool. Probably related to wel-‘. 1. Suffixed extended zero-grade form “*wi-nd- in: a. Germanic *wullé in Old English wul(l), wool: woot; b. Italic *wland in Latin lana (> French laine), wool, and its derivative laénig6, down: LANATE; DELAINE, LANIFER- OUS, LANOLIN, LANUGO; ¢. Celtic *wland in Welsh gwlan, wool (> Middle English flannel, woolen cloth): FLANNEL. 2. Possible suffixed o-grade form *wol(o)-no- in Greek oulos, wooly, curly: ULoTRICHOUs. [Pok. 4. uel- 1139.] wela-2. To strike, wound. 1. Suffixed o-grade form *wol()-o- in Germanic *walaz in Old Norse valr, the slain in battle in: a. Old Norse Valhdéll, Valhalla: VAL- HALLA; b. Old Norse Valkyrja, “chooser of the slain,” name of one of the twelve war goddesses (-kyrja, chooser; see geus-): VALKYRIE. 2. Suffixed basic form *welo-nes- in Latin vudnus (stem vulner-), a wound: VULNERABLE. [In Pok. 8. wel- 1144.] welg-. Wet. Germanic *welk- in: a. Old English wolc(e)n, cloud, sky: WELKIN; b. Middle English welken, to wilt: wILT!. [Pok. 2. welk-, uelg-, 1145.] welt-. Woods; wild. 1. Suffixed form *wolt-u- in Germanic *walthuz in: a. Old English weald, wald, a forest: WEALD, WOLD!; b. Old Norse vdllr, field: VOLE!. 2. Ger- manic *walthdn- in Middle English welde, a plant yield- ing a yellow dye, weld: WELD2. 3. Germanic *wilthigaz in: a. Old English wilde, wild: wip; b. Old English wildéor, wilddéor, wild beast (déor, animal; see dheu-'): WILDERNESS; C. Dutch wild, wild: WILDEBEEST. [In Pok. 4. uel- 1139.] weme-. To vomit. 1. Germanic *wam- in Old Norse vamla, qualm, and Danish vamle, to become sick, prob- ably akin to the Scandinavian source of Middle English wam(ejlen, to feel nausea, stagger: WAMBLE. 2. Latin vomere, to vomit: NUX VOMICA, VOMIT. 3. Greek emein, to vomit: EMESIS, EMETIC. [Pok. wem- 1146.] wen-', To desire, strive for. 1. Suffixed form *wen-w- in Germanic *winn(w)an, to seek to gain, in Old English winnan, to win: WIN}. 2. Suffixed zero-grade form *wn-ydé in Germanic *wunjé in Old English wynn, wen, pleasure, joy: WEN2, WINSOME. 3. Suffixed (stative) zero-grade form *wn-é-, to be contented, in Germanic *wunén in Old English wunian, to become accustomed to, dwell: won!, (wont). 4. Suffixed (causative) o-grade form *won-eyo- in Germanic *wanjan in Old English wenian, to accustom, train, wean: WEAN}. 5. Germanic *wéniz, hope, with denominative *wénjan, to hope, in Old English wénan, to expect, imagine, think: WEEN. 6. Suffixed zero-grade form *wn-sko- in Germanic *wunsk- in Old English wyscan, to desire, wish: WISH. 7. O-grade *won- perhaps in Germanic *wani- in: a. Old Norse Vanir, the Vanir: VANIR; b. Old Norse vana- in Vanadis, name of the goddess Freya: VANADIUM 8. Suf- fixed form *wen-es- in: a. Latin venus, love (> venerari, to worship): VENERATE, VENEREAL, VENERY!, VENUS; b. suffixed form *wen-es-no- in Latin venénum, love potion, poison: VENOM. 9. Suffixed form *wen-eto-, “be- loved,” possibly in Germanic *Weneda-, a Slavic people, in Old High German Winida, the Wends: WEND. 10, Suffixed form “wen-yd@ in Latin venia, favor, forgive- ness: VENIAL. 11. Lengthened-grade form *wén-d- in Latin véndri, to hunt: VENATIC, VENERY2, VENISON. 12. Suffixed basic form *wen-o- in Sanskrit vanam, forest: WANDEROO. 13. Possibly zero-grade suffixed form *wn-ig- in Sanskrit vanik, vdnijah, merchant (? < “seek- ing to gain”): BANIAN. [Pok. 1. ven- 1146.] wen-2. To beat, wound. 1. Suffixed zero-grade form
1349:CHEST kista CHEVRON kapro- CHEW gyeu- CHIAROSCURO kele-2, (s)keu- CHICKEN ku-
1356:CHIRO- ghesor- CHIRURGEON ghesor- CHISEL kaa-id- CHITTERLINGS ku- CHLOASMA ghel-2 CHLORITE! ghel-2 CHLORO- ghel-2 CHOANA gheu- CHOANOCYTE gheu- CHOICE geus- CHOIR gher-1
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
2160:RABBET battuere RABBLE? reu-2 RABID rebh-1 RABIES rebh-1 RACE? ers-1 RACES wrad- RACHIS wragh- RACK! reg-1 RACK3 wreg- RACLETTE réd- RADDLE! reidh- RADICAL wrad- RADICLE wrad- RADIOSONDE swem- RADISH wrad- RADIX wrad- RADULA réd- RAFT! rép-2 RAFTER rép-2 RAG! reu-2 RAGA reg-3 RAGE rebh-1 RAGOUT geus- RAID reidh- RAIL! reg-1 RAIN reg-2 RAINBOW reg-2 RAISE risan RAJ reg-1 RAJAH_ reg-! RAKE! reg-1 RALLENTANDO lento- RALLY leig-1 RAMBUNCTIOUS reudh-1 RAMEKIN reugh-men- RAMIFY wrad- RAMOSE wrad- RAMP2  skerbh- RAMPART pere-1 RAMPION rap- RAMSON krem- RAMUS wrad- RANCH sker-3 RANGE sker-3 RANI reg-1 RANK!  sker-3 RANK? reg-1 RANKLE derk- RANSACK sag- RANSOM em- RAPACIOUS rep- RAPE! rep- RAPE? rap- RAPHE wer-3 RAPHIDE wer-3 RAPID rep- RAPPORT per-2 RAPPROCHEMENT per! RAPT rep- RARE! era-2
=== AHD goat ===
348:bhugo-. Male animal of various kinds; stag, ram, he-goat. 1. Germanic *bukkaz (possibly borrowed from the Celtic form in 2. below) in: a. Old English buc, bucca, stag, he-goat: BUCK}; b. Middle Dutch boc, bok, buck: BLEs- BOK, BONTEBOK, SPRINGBOK, STEENBOK; C. Old High German boc, buck: GEMSBOK. 2. Celtic *bukkos, he-goat, in Old French boc, buck: BUTCHER. [Pok. bhiigo-s 174.]
400:digh-. She-goat. Germanic *tigon (with expressive conso- nantism) in Old Norse iik, bitch: TYKE. [Pok. digh- 222.]
505:ghaido-. A goat. Germanic *gaitaz in Old English gat, goat: GoaT. [Pok. ghaido- 409.]
```


## [2026-09-05T20:58:35.683Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\necho \"=== WLD Bd1 kauen javidan ===\"; grep -n \"javīdan\\|javidan\\|jāvīdan\\|kauen'\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== WLD Bd1 ghaido ===\"; grep -n \"ghaido\\|haedus\\|gaits\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== WLD Bd1 geus ===\"; grep -n \"zaoša\\|zusta\\|daustar\\|geus-\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T20:58:35.759Z] TOOL RESULT

```
=== WLD Bd1 kauen javidan ===
=== WLD Bd1 ghaido ===
33131:ghait-a, -es ghaido-, ghaiclo- 
33164:gliaido- oder ghaido* „Ziegenbock, Ziege“. 
33166:Lat. haedus „Bockchen, junger Ziegenbock“ (dazu die, dialektischen und 
33169:got. gaits und ahd. geiz fi , aisl. geit f„ aschw. get , gcet f., ags. gat f., 
33172:Yon ghaido- abgeleitet *ghaideinos : lat. haedinus „von jungen B6eken“. 
33194:kip „Tierjunges“, ahd. hi: si ds. „kosende Umgestaltung“ von ghaido- sind. 
34228:gang mit . . ." , allenfalls auch lat. ha edits , dt. Geiss (s. ghaidos) anreihto (siehe 
51373:aus *$ita (: *ghaidos ,.haedus“) umgestellt, s. Liden aaO. u. o. S. 527. Kaum 
=== WLD Bd1 geus ===
4936:„gedeiht, gelingt, macht gelingen, bringt zustande“, Desid. Irtsati , ardlmka- 
4941:ai. radJnidti, rddhyati „macht (passend) zurecht, bringt zustande; gerat, 
4943:zustande, befriedigt* 1 , radha-h ni., rfidhah n. „Segen, Gelingen, Wohltat, 
5002:ordnen, zurechtlegen, zustandebringen, entrichten, zahlen 1 , mhd. reiten „zu- 
5780:rdhdti, >;dhyati „gedeiht, gelingt, maeht gelingen, bringt zustande“, av. 
11280:vom Feldbau), zustandebringen ; Ertrag der Arbeit, Reichtum-'; die 
11979:zustand habend“ oder „steif wie ein Stein“) ist verfehlt, ware auch lat. *osti-. 
14676:„ist tatig. wirkt, bringt zustande. richtet aus“. lat. vi-r-es (s. o.) (lat. virgo 
14926:Sippe von bewegm zustandegekommen sein. 
20857:fiber aisl. heyja ,,zustandebringen“, ags. lwgan „verrichten“, Fick III 4 66, 
29289:lehnung an kosten , Wz. geus- ?) aisl. boss, ags. coss, ahd. kus „KuB“, aisl. 
30731:dehnung durcb Kreuzung von *kork- und *krok- zustande gekommen zu sein 
35781:geus- ,, kosten, geniefien, schmecken 44 , im Germ, und Kelt, auch iiber , mit 
35786:Geschmack woran finden 4 ', av. suoiia- „Gefallen 4 ', zusta „beliebt, erwiinscht 44 , 
53474:eine (yielleicht unter Beihilfe der Worte fur „Pflock, Zapfen“ zustande
```


## [2026-09-05T20:58:39.929Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\necho \"=== ghaido block ===\"; sed -n '33160,33200p' WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== geus block ===\"; sed -n '35778,35830p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read WLD ghaido and geus"
}
```


### [2026-09-05T20:58:39.998Z] TOOL RESULT

```
=== ghaido block ===

Liden IF. 19, 318 f. und Charpentier KZ. 40, 272 f., beide mit Kritik 
abweichender Versuche. 

gliaido- oder ghaido* „Ziegenbock, Ziege“. 

Lat. haedus „Bockchen, junger Ziegenbock“ (dazu die, dialektischen und 
vulgaren Formen hedus, edus, faedns, f edits s. Ernout El. dial. lat. 154f.); 

got. gaits und ahd. geiz fi , aisl. geit f„ aschw. get , gcet f., ags. gat f., 
as. get f. (konsonant. Stamme) „Ziege“. 

Yon ghaido- abgeleitet *ghaideinos : lat. haedinus „von jungen B6eken“. 
ags. gcet'U, ahd. geizin „caprinus“, got. gaitein n. „Bocklein“, ahd. geizin 
n. „Bock“. (Zur Bildung vgl. sivein und Kluge, Nom. Stammb. § 57, 5S a .) 

Ob die Ziege als „die springende“' (Prellwitz s. v. yaha ) zu ai. jihlte 
„springt auf, setzt sich in Bewegung, lauft“, hdyah „RoB“, arm. ji ds.. aksl. 
zajecb „Hase“ (Zupitza Gutt. 200) oder naeh FickI 4 433 zu lit. zaidziu 
„ich spiele“ gehort, ist fraglich. Ygl. Yerf. LEWb.' 2 359 (die Yerwandt- 
schaft des lit. und ind. Wortes ebenfalls zweifelhaft). Abzulehnen mit 
Liden IF. 19, 319 fF., Charpentier KZ. 40, 472 die Zusammenstellung mit 
gr. yang, s. u. ghaitd-. 

Ahd. ziga, wozu ags. ticccn und ahd. siclil mit hypokoristischer Konso- 
nantendehnung (s. Kretschmer Glotta 14, 321, ist nicht mit Kluge in alteren 
Auflagen der E. Wb. (spater ist die Kombination aufgegeben), Ipsen 
IF. 41, 143, Hirt idg. Gr. I 85 und 187 , ; durch tabuierende Lautumstellnng“ 
aus idg. gidlids entstanden, vielmehr als Auslautsdublette zu gr. di'Qa • at$. 
Ady.covsg (Hes.) < *<ligi/i, arm. tik „Sehlauch a zu stellen. (Liden Arm. 
Stud. 10ft', Meillet MSL. 15. 356 = Bezzenberger BB. 27. 165. Fick KZ. 
42, 14S.) 

DaB alb. kid „Bockchen £ , mir. cit ,,Schaf - ‘ (Marstrander, ZfcPh. 7, 4(>3), an 
kip „Tierjunges“, ahd. hi: si ds. „kosende Umgestaltung“ von ghaido- sind. 



528 


=== geus block ===
fernzuhaltenden vermischt sind), Berneker aaO , Trautmann aaO., Persson 
Beitr. 105 A (der die Parallelitiit von *kcu-, *geu- und *gheubh- hervorhebt). 

geus- ,, kosten, geniefien, schmecken 44 , im Germ, und Kelt, auch iiber , mit 
dem Geschmack priifen 44 zu ,,wahlen“ entwickelt. 

Ai. julati, jusdte ..kostet, genieBt, liebt", jrktyatc ..findet woran Yer- 
gniigen 4- , jijsa-h ,.Zufriedenheit, Billigung, Geniige 44 , av. zoos-, ap. daits- 
Geschmack woran finden 4 ', av. suoiia- „Gefallen 4 ', zusta „beliebt, erwiinscht 44 , 
gr. ycvopat ,.koste, genieBe 4 ; davon yevco .,lasse kosten 44 ) ; got. Jciuscin 
.,priifen, erproben 4 ’, anord. kjiisa „wahlen, wiinschcir (auch „durch Zauberei 
beeinflussen 4- , s. Falk-Torp u. kyse), ahd. as. kiosan „ schmecken, priifen, 
wiihlen -4 , nhd. kicscn, kiiren , Kaus.-Iter. got. kails j an „priifen, kosten, 
schmecken 4 (= ai. jusdyatcr, air. asa-gu „er wiinsche 4- {ad-gusi, asa-gussi 
,,er wiinscht' 4 . s. zur Form Pedersen II 549), do-goa „er wiihlt' 4 , inf. toga 
,,wahlen, Wahl 44 , praet. dordign „elegit 4 (zur Bildung dieser Praet.-Form 
zuletzt Pokorny IF. 35, 177 ff. ; usw. fs. Pedersen aaO. ; alb. don ,.ich 
liebte 4 ', Praes. dun (zu den Formen zuletzt Jokl IF. 37, 101 f.) : w-Praes. 
lat. deguno, -ire ,, kosten 4 ' ( *gus-nf> ). 

Komen actionis auf it- und to-: ai .justi-h ..Liebeserweisung, Gunst' 4 , got. 
ga-kvsts , Priifung 4 . afr. kest, ags cyst m. ..Gegenstand einer Wahl, Yorziiglich- 



gheus-, ghous- - geg(h)-, gog(h)- 569 


keit" (aber gr. yevai g erst einzelsprachliche Bildung von yevo/aai aus); lat. 
gustus , -ils ,,das Kosten, Geniefien", kelt. *gustu- ,,Wahl £ ' in den Xamen 
ir. Oengus, iergus , acymr. Ungust , Gurgust (z. B. Pick II 4 115; aber iiber 
cymr. usw. deivis „Wahl‘ ! s. Pedersen KG. I 210, Lw. aus lat. divtso ) und 
in air. gus „Tiichtigkeit, Kraft", got. kustiis „Priifung £i , abd. as. kust m. 
„Priifung, Schatzung, Wabl, Vortrefflichkeit, Art und Weise", anord. kostr, 
-ar ,,Wahl, Willkiir, (gute) Eigenschaft"; Ableitung vom Ptc. *gus-tos : 
lat. gusto, -are „kosten, genie8en“ = ahd. as. koston „kosten, versuchen“, 
ags. costian .vcrsuchen, plagen“, anord. host a, -acta „priifen, sich anstrengen, 
erstreben". 

Ygl. noch anord. k0r n. ,,Wahl“, ags. gecor n. ,.Entscheidung“ ( *guso 
abl. m. ai. josa-h , av. mosa-\ davon abd. bikoran ,,schmecken, priifen, 
wahlen“ i, ags. eyre m. „Wahl £c , ahd. kuri f. ds. (*guri - ; nhd. Kur-furst , 
Willkur). 

7a. B. CurtiuB* 177. — Xicht hierher ahd. kUski, nhd. keusch ..rein, keusch“ 
als „auserlesen“ (Sommer IP. 31, 372; bes. vermisse ich Stiitzen fiir pas- 
sive Yerwendung des germ. Suffixes -ska-). — Unannehmbar koppelt Fay 
Journ. of engl. and germ. Phil. XII Hr. 3 yens- mit g>eu- .,kauen“ und 
andern Wzln. zusammen. 

gheus- : ghous- „tonen, horen“. 

Ai. ghoiati „ertont, verkiindet laut, hort“ (diese Bedeutung am imp.
```


## [2026-09-05T20:58:40.977Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"g\\^ieu\\|gieu\\|kauen\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep WLD for chew root"
}
```


### [2026-09-05T20:58:41.032Z] TOOL RESULT

```
2966:rucchen, ags. edrocinn „wiederkauen“, ags. cdcerr „Wiederkehr'‘, s. weitere 
18614:856’; altn. lltn, ags. u'Utnn ..sehen, sckauen"; schwundstufig got. n'lits 
21551:„essen, kauen“ (Hiibschmann ZDMG. 38, 423, Horn Np. Et. 104, Uhlen- 
23329:skauivdn , ahd. scouwon „sckauen“; aisl. si yqn „sehend, scharfsichtig" (*skuv- 
24467:schwerfallig kauen 41 , serb. kbtnsam , -afi „kauen, nagen, fressen 41 , kuni „Wein- 
32676:qHeru- „kauen; zermalmen, mahlen (Mehl und daraus bereitetes)“. 
35825:Journ. of engl. and germ. Phil. XII Hr. 3 yens- mit g>eu- .,kauen“ und 
40415:gieu, gieu- — ghuer 
40418:gieu- und gieu- „kauen“. 
40420:Npers. Javldan „kauen“, afgh. zovgl, zoyal „kauen, beiBen, nagen“ (Hiibsch- 
40426:Aisl. tyggva „kauen verspeisen“ (Dach Pedersen KZ. 32, 255 mit Dissi- 
40428:IF. 1, 513f.), nscbw. kugg „Zahn am Rade“, ags. ceowan „beifien, kauen“, 
40429:ahd. kiuuan „kauen, beiBen, verzehren", ags. clan „Kiemen“, and. keho, kio, 
40436:„kauen“; bulg. zuna „Lippe, Lefze“; bulg, zrdlo , skr. zv'ilo „Rachen, Eng- 
40442:Nicht von yevoyai lassen sich die von Fick aaO. zu *gieu- gestellte 
42243:(Ycreinigung mit *gieti- ..kauen". *gcns- ..kosten 1 ";- 
47169:tnei- „scharf kauen, schlagen"?? 
47223:251. Weiterer Yergleich mit *‘ud- (? ? 1 ; ,scharf kauen ‘ bei Wood Mod.
```


## [2026-09-05T20:58:51.380Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '40415,40450p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read WLD gieu block"
}
```


### [2026-09-05T20:58:51.425Z] TOOL RESULT

```
gieu, gieu- — ghuer 


gieu- und gieu- „kauen“. 

Npers. Javldan „kauen“, afgh. zovgl, zoyal „kauen, beiBen, nagen“ (Hiibsch- 
mann, Pers. Studien 49 f.): arm. kiv „Mastix, Baumharz“ (eigtl. „Kauharz“), 
kveni „pieea, pinus, larix“ (Liden Arm. Stud. 68). 

Lat. gingiva „Zahnfleisch“ (nicht zu *gong- „Geschwulst“, s. d.). 

Aisl. tyggva „kauen verspeisen“ (Dach Pedersen KZ. 32, 255 mit Dissi- 
milation des durch i palatalisierten k vor gg ; etwas anders Streitberg 
IF. 1, 513f.), nscbw. kugg „Zahn am Rade“, ags. ceowan „beifien, kauen“, 
ahd. kiuuan „kauen, beiBen, verzehren", ags. clan „Kiemen“, and. keho, kio, 
abd. kio, kiuua , mbd. kimve ds., und die Ableitungen mnl. coon „Kiefer. 
Ivinnbacken (< *kaund ), afr. ziake f. „Kinnbacken“ und afr. kese „Backen- 
zahn“, mnd. kiise, mnl. kuze, ablautend mnl. kiese ds. 

Lit. ziaunos „Kiefer“, lett. zaiinas (Plur.) „Kiefer, Kinnladen, Fischkiemen“ ; 
aksl. zuju (zbvq), zwati , russ. zuju, zevdtb, acech. ziji, zvati, poln. zuje, zuc , 
„kauen“; bulg. zuna „Lippe, Lefze“; bulg, zrdlo , skr. zv'ilo „Rachen, Eng- 
pafi“, si. zvald, bulg. zvdle, skr. zvale „Gebi6 am Pferdezaum“. 

Ygl. Fick I 4 406, III 4 44, Falk-Torp 1307, 1570, Zupitza G. 1 45 f., 
Trautmann Bsl. Wb. 372. 

Nicht von yevoyai lassen sich die von Fick aaO. zu *gieu- gestellte 
Hesychglossen: £evoaodai • yevoao&ai, devaaadai ' yevoaodai trennen, siehe 
G. Meyer Gr. Gr. 3 268 a 3. 

gliuen- „tonen“, Erweiterung von yhau- s. Persson Wzerw. 71, Beitr. 191. 

Arm. jain i-St. „Stimme“ (mit i-Epenthese ; s. Meillet Msl. 9, 54, Pedersen 
KZ. 36, 338, 38, 198, 39, 406; dagegen Hubschmann Arm. Gr. I 469); alb. 
ze „Stimme“, geg. zq ( <*ghuono - s. Pedersen KZ. 36, 338, Brugmann
```


## [2026-09-05T20:58:54.029Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC gieu ===\"; grep -n \"gjeu\\|gieu\\|geus-\\|ghaido\" IEC.txt | head -20\necho \"=== SYN chew/goat/friend ===\"; grep -n \"javidan\\|jāvīdan\\|Pers. dōst\\|Pers. dost\\|ghaido\" SYN.txt | head -20",
 "description": "Grep Mann and Buck"
}
```


### [2026-09-05T20:58:54.132Z] TOOL RESULT

```
=== IEC gieu ===
3978:geuuð, ið, see gieuuð, ið
3979:geu-, see gieuuo, ið
4015:gieuð, ið (gleuu-, giau-) ‘chew’. WP I, 642. Cf. geus-
5666:OBr. cf. gen ‘corner’ beside gennec ‘gulf’; Go. (with unexplained doubling) kinnus: MHG kin, kinne; OHG kinni; OE cinn; ON kinn, pl. kinnr, id. (Variants in Du. koon ‘cheek’ see $&eun-; extn. Gk. gn-áthos; OE cenep ‘moustache’, lit. *chin-nap'; OFris. kanep, id.; ON kanpr, kampr uncertain in view of Arm. cam, see gomb-. For Lat. gin-giva ‘gum of teeth’, see ĝen- above, and gieua below. Iso- phonic: Mir gin, oun, ap. ginu ‘gullet, mouth’. Skt. hanuh “jaw? has an unexplained initial. Cf. J. Puhvel on Gösta Liebert in *Lan- guage’ 35.4.646-7 :e80, dhugter, Krd-)
5686:$euà, $ieua (Gu) ‘chap, jowl, jaw; gill of fish’. Cf. $eunos, gieuuo Lat. gin-giva (“gum of teeth’; for gin- see ĝe- nus above); MHG kiuwe, kéwe, kouwe ‘jaw, cheek’; NGer. Kiewe ‘gill’; cf. MHG kiuwel
=== SYN chew/goat/friend ===
33714:OPers. daustar- (NPers. dost) : Av. zus-, Skt. jus- ‘take pleasure in, enjoy’, Av. zaoga- ‘pleasure’, Grk. yeboua ‘taste, enjoy’, etc. (15.31). Barth. 674 f.
```


## [2026-09-05T20:59:04.205Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN context ===\"; sed -n '33700,33720p' SYN.txt\necho \"=== SYN chew ===\"; grep -n \"19.51\\|‘chew’\\|4.58\" SYN.txt | head -10\necho \"=== SYN goat ===\"; grep -n \"Goth. gaits\\|gaits\" SYN.txt | head -10",
 "description": "Buck context"
}
```


### [2026-09-05T20:59:04.293Z] TOOL RESULT

```
=== SYN context ===
W. cyfaill, old cyfaillt = Ir. com-alta ‘foster-brother’, orig. pres. pple. of *com-alim, cpd. of alim ‘nourish, rear’. Pedersen 2.35.
Br. mignon, fr. Fr. mignon ‘darling, pet’ (REW 5581.2). Henry 203.
4. Goth. frijonds, OE fréond, etc., general East and West Gmc., but ON frendi ‘relative’, orig. pres. pples. of Goth. frijon, OE fréon, etc. ‘love’ (16.27). Feist 168. Weigand-H. 1.583.
ON vinr, Dan. ven, Sw. vén, OF wine, OS, OHG wint, MHG win(e) : Ir. fine ‘clan’, Skt. van- ‘desire, love, wish, acquire’, etc. Walde-P. 1.259. Falk- Torp 1366.
5. Lith. draugas (also ‘companion’), Lett. draugs = ChSl. drugit (also ‘com- panion’, pron. andadj. ‘other’), Russ. drug (SCr. drug, Boh. drug ‘companion’, SCr. drug, etc. ‘other’) : Goth. driugan ‘do military service’, ga-drauhts ‘soldier’, ON drott, OE dryht, OHG iruht ‘multitude, people, army’, etc. Whatever the root and primary sense in this group, ‘friend’ comes fr. ‘companion’. Miihl.-Endz. 1.492. Berneker 230 f.
Lith. biéiulis (pop. word for ‘bosom- friend’), lit. ‘bee-keeper’, deriv. of bité ‘bee’. The bee-keepers of a neighbor- hood are bound together in close friend-
ship and form a kind of ‘bee-fraternity’. Cf. Zemaités Ragtai 1.231 ff., and Tauta ir Zodis 4.459.
6. ChSl. drugz, Russ. drug, cf. Lith. draugas (above).
ChSl. (late) prijatelji, etc., general modern Slavic, fr. prijati ‘favor, be well- disposed to’ : Goth. frijon ‘love’, frijonds ‘friend’, etc., and esp. OHG friudil, ON fridill lover’. Walde-P. 2.87. Meillet, Etudes 312 f.
7. Skt. sakhi-, sakha-, Av. hazi-, both also ‘companion’, etym. dub. (: Skt. sac- ‘follow’, but kh?; cpd. of sa- ‘with’?). Walde-P. 2.476. Uhlenbeck 324. Er- nout-M 949.
Skt. suwhrd-, lit. ‘having a good heart’, epd. of su- ‘good’ and Ard- ‘heart’.
Skt. mitra- (Vedic ‘friend, compan- ion’, later mostly ‘Mitra’) = Av. mi6ra- ‘agreement, compact’, Mi@ra-, OPers. Mitra-, etym. dub., perh. : Skt. mith- ‘exchange’, mithuna ‘a pair’, etc. Walde- P. 2.241. Uhlenbeck 223.
Av. urvafa-, etym. dub., perh. : var- ‘choose’. Barth 1537.
Av. frya-, as adj. ‘dear’ (16.28).
OPers. daustar- (NPers. dost) : Av. zus-, Skt. jus- ‘take pleasure in, enjoy’, Av. zaoga- ‘pleasure’, Grk. yeboua ‘taste, enjoy’, etc. (15.31). Barth. 674 f.
19.52 ENEMY
Grk. — &x8pbs, rodeos Goth. fijands Lith. prieSas
NG ExOpés, Todeutos ON = fjdndi, avinr Lett. denaidnieks
tnimicus, hostis Dan. fiende, uven ChSl. vragii, neprijateljt
es nimico Sw. fiende SCr.  neprijatelj, du’manin , ennemt OE Séond, gefa Boh.  nepitel
Sp. enem2go ME enemi, fend, fo Pol. nieprzyjaciel
=== SYN chew ===
4626:‘yearling bullock’, manza ‘heifer’, etc., generally regarded as of Illyr. origin. REW 5289. Densusianu 29. G. Meyer, Alb. Etym. Wtb. 270. Otherwise, as fr. *mandius, deriv. of mandere ‘chew’, Puscariu 1092.
5771:be teeth, on ‘fork’, tour OS ’ t of the Jaw in jaw Pol ‘angle�� to tha Bee ae m verbs for ‘chew’ Or wae he modern Polish) seems to have dasa slang term forthe: ‘chauter starte - Several are obscure in their d ection. i a ait words for ew, aHal ‘chin’. Orig. sense Jaw and ultimate connection with ae word for ‘knee’, 1B *genu- (neut.), Gri. yoru, Lat. geni, etc. (4.36), through some com- mon notion like ‘angle’, is probable. Walde-P. 1.587. Ernout-M. 414. -H, 1.589 f. on ‘jaw’ (so always in Hom.) and ‘cheek’, -yéverov ‘chin’ (and ‘beard’) ; Lat. gena ‘cheek’ (mostly in pl.; stem genu- in genutni dentés ‘back teeth’); W. gen ‘jaw, chin’ (Ir. gin, W. geneu, Br. genou ‘mouth’); Goth. kinnus, ON kinn, Dan., Sw. kind ‘cheek’, OE cin, OHG kinni, etc. (all WGmce. words) ‘chin’ (but in early period traces of use for ‘jaw’, as OHG chinne ‘jaws’ Notker, Ps. 31.9, OHG chinnibacho ‘jaw’, OE cinban ‘jaw- bone’); Skt. hanu- ‘jaw’ (h for 7 second- ary), Av. zanu- ‘jaw’ or ‘chin’ (in epd., Barth, 1689) , NPers. zanaz ‘chin’; Toch. Ber oa (dual, SSS, 3, ftn.). Gre ae ae extension *Gon(e)dh-, Ba ease pn ; zandas ‘jaw’, al Mihl.-Endz, 4.759) edi pail # Ok rn al yom vor) istot, =i + Boisacq 862. GROpeRT se ce nr HdBos,. vers NG Hacé\)\a, of frequency.
5783:Fr. mdchoire, fr. mdcher ‘chew’.
5801:ME tow, towe, iawe, NE jaw, etym. disputed. Now taken by many as fr. *chowe : OF céowan ‘chew’, like MHG kiuwe ‘jaw’ fr. the same root (OHG chiwa, like OE cian ‘gills’). But the old deriv. fr. a form of Fr. jowe ‘cheek’ is less difficult, despite the objection made in NED. For OFr. ioe, iowe must have been pronounced with [owe], not [a], and the phonetic history would be paral- lel to that of ME powe, pawe, NE paw, fr. OF r. poe, poue = Prov. pauta. The transition fr. ‘cheek’ to ‘jaw’ may have started in ‘cheek bone’ = ‘jawbone’, which is in fact the sense in the earliest ME quotation (iow in Wyclif, see NED).
5807:use only since 19th cent., cf. NED s.v.), fr. the root in OE céowan, OHG kiwwan ‘chew’ (: ChSl. Ztvatz ‘chew’), not (as
5933:5. Goth. munps, OE mip, OHG mund, ete., general Gmc., prob. : Lat. mentum ‘chin’, etc. (4.209), rather than : Lat. mandere ‘chew’, as preferred in Walde-P. 2.270, Falk-Torp 738. Feist 368. Ernout-M. 608.
6857:4.58 BITE (vb.)
8331:Lat. manditcare ‘chew’ (beside older mandere), used collog. for ‘eat? and freq. in this sense from Varro on (esp. Petronius, Peregrinatio, Itala, etc.). Hence Olt. manicare, Fr. manger (> It.
8347:Skt. khad- ‘chew’, colloq. for ‘eat’ and in MIndic mostly displacing ad-. Wack- ernagel-Debrunner, KZ 67.158.
17110:Koraes, “Araxra 4.58 Cc iny s . Cf. Fr. plonger,
=== SYN goat ===
4470:‘gray’, etc. Walde-P. 1.602f. TFalk- | ssdéi ‘suck’. 3.36 3.37 3.38 GOAT HE-GOAT KID (Generic or feminine) Grk. al (xlpatpa) Tp&yos épidos NG ylét, fem. yida  rpa&yos, rpayl karolxe Lat. capra hircus, caper haedus It. capra becco, capro capretto Fr. chevre, bique bouc chevreau, biquet Sp. cabra, chiva cabrén cabrito Rum. capré lap caprioard Ibe, gabor boce menn(dn) Nir. gabhar boc mionnan W. gafr bweh myn Br. gaor bouc’h gaorig Goth. gaits Sante pueceis | ON get hafr (bukkr) kid | Dan. ged buk kid Sw. get bock kid OE gat bucca, hafor ticcen, hécen ME pote bucke kide NE goat he-goat kid Du. geit bok geitje OHG  geiz, ziga boc zicki(n), kizzt(n) - MHG geiz, zige bock 2ickelin NHG ziege, geiss bock zicklein Lith. oka ozys ozelis, ozkutis Lett. kaza Gzis kazlens ChSl. koza koztlit koztle SCr. koza jarac Jare, kozlié Boh. koza kozel kizle Pol. koza koziot koéle Russ. koza kozel kozlenok Skt. _aja-; fem. aja- aja-, chaga- “a Av. i tlcts biza-
4484:3. Ir. gabor, NIr. gabhar, W. gafr, Br. gaor, gavr, perh. with unexplained init. variation : Lat. caper, etc. So Thurney- sen, Gram. 189, Z. celt. Ph. 13.108 ff. Otherwise Walde-P. 1.533, 547. es Goth. gaits, ON geit, OE gat, etc., a general Gme. word: Lat. haedus kid ; perh. Lith. Zaidziu, Zaisti ‘play’ as =H Jump, gambol’. Walde-P. 1.527.
4517:2. Lat. haedus: Goth. gaits, ete, (3.36).
28040:5, Lith. Zaisti, perh. as orig. ‘jump’ : Iat. haedus ‘young goat’, Goth. gaits, ete, ‘goat’, ChSI. zaject ‘hare’, and Skt. jikile ‘bounds up, leaps up, runs off’.
```


## [2026-09-05T20:59:04.751Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zaosa ===\"; grep -n \"zaoša\\|zaosa\\|zušta\\|zusta\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:59:04.826Z] TOOL RESULT

```
=== BRT zaosa ===
3746:•  j.apu*rya-n.  "Niederkunft,  Puerperium': yal  .  .  allaoa  aisa  nsirika  tdöa  'rTin nijasst  uzustana  "wenn  .  .  dort  die  Frau dann  niederkommt  mit  einem  leblosen Kind"  V.5.4S;  Vd./.?.
3769:das  Narkotikum  banha-  hervorgerufenen) , Betäubungszustand,  durch  Narkotika  nicht ' zu  betäuben':  ax^aßiS  aAi  "tihö  tSm  y5 ahurs  V.ig.20.  I
5976:j.  a-zaosa-  m.  'Nichtwille,  NichUbsicht'; yezi  zaela  yezi  -/a  (IS.)  "sei  es  absicht- lich, sei  es  unabsichtlich"  Y. ;.  21.
8120:•  j,  ujra.zaosa-  Adj.  (fem.  '!•!-)  'starken sva.  unbeugsamen  Willens  gegenüber  — ' (Dat.) :  /ravasayö . .  °/.f  tbtsyanbyS  Vt  7J.  3 1  .■
9493:•  j.,  g.,  p.  käma-  m.  'Verlangen,  Wunsch': haväi  °maua  zaosai'a\t.i^.2y,  —  aeiby:! p^r^na  äpansis  (sd.)  "m^m  Y.  2(V.  10;  — arii;ä  vsizdyäi  (sd.)  °mahy3  ^.43. 13.  a)  mit  Akk.  des  Verlangten": /^..-/y- xat  (sd.)  "///?..  dBtVm  ". .  im  Verlangen !  ^'^'''5,^ nach  der  Botschaft"  V.J.M3.  b)  mit'  "?  -' Akk.  des  Verlangenden^':  II  ya>3  mäm 'ina*  ä/ta*  "wie  es  mein  Verlangen  war" D.tf.4;Bh.4  4.
12653:•  g.  daidyäi  Inf.  'zu  geben,  zu  gewähren': tat  vS  fiS  hazaosauhs  (sd.)  VTSpaahB  d' savB  Y.  57.  20.  \in}ncä  daidyäi  Y.JJ. 5:  s,  unter  ma/id-.]
14732:u  fasimärTk  'Anütge  und  Verieidig'^rg"  und  i^-o«/-''  sbes.  s)  Tcr��nken,  beleidigen", vicir  II  ditawarik  "Entscheid  und  Urteil';  (lu  mit  Akk.:  ratavS  vJspe  masista  ,  .  yai  vS i  t):  dätmoar;  {t^  3):  dSlinaarih,  etL;  "icir.^ ^^f/j/gg^^  _  „gfig„^g  ^  .j,acargAa  . .  syaeÜFfta .SQ. :  ayäyai.    Zu  F.  S  wird  gesagt,  liaiii  be- 1  ,        azaosa  V  7  3  a  ■  2 1  ■  —  ahuräne
15551:I):  fei,  (lu  II):  api  hac,  (lu  III):  apc;  s.  noch No.  2  ff.,  6,  8  ff.  —  0  Hds.  pari.  —  »)  D.  i. TOT  oder  nach  der  Rezitation  der  Gs%ä%\  Pü.: pas  -  tu  fralum    kär   ape   kuntt  pas   apasläk gffujet-aiävp/i—ku  afaitik  (Rest  weggelassen). —  3)  Pü.:  ausgelassen.  —  4)  Unsicher.     Pü.: apar.     -    S>  Vgl.  Bipi  II  I   i  (Sp.  83  ">■)■  - 6)    PD.  :    apar  pa  barsm.    —     ?)   S.  dam  Dbr, VglS.  /.   71 1.  —  »'  PS-:  i'  onrfflr  an  apar.  — 9)  Pü. !  *ia/.  —  10)  Pü. :  undeutlich.  —  "»  Pii, : apF,  —  ")  Wörtlich :  "non  profuse  sine  semine', eine  Vermischung  der  beiden  sinngemäss  rich- tigen  Ausdrücke   */rai>har>iäl  pairi  xl'    und tt/raa/iamäl  paiti  xs',    vgl.  anädntxlay-  No. I.     Pü.:    fehlt.    —     '.0  Pü.:    hat.  —   M)  Wo NA.  unrichtig  abteilt ;    s.  Vt,  3,  la  —  >5)  Wo die  Hds.  das  2.  Mal/aiV/  bieten;  s.  Yt.  j.  14. •  j.   *pairi.aoxtay- ",    pairyaoxtay-    f. i)    'Aussprache,    Vortrag':  yezi  araitrim (sd.)  *'ta'^  pairi Jta  Ü.32.         2)  'Zuruf, Befehl':    dansa    nä    'tala    (LS.  als  IS.) uzustanä    *adir»yäte  .  .  frasumaitls  (sd.)
16706:Betäubungszustandes 3'  (nur  Komp,).  i'"-»^s-    ^
18969:•  j.,  g.  'namah-  n.  'Verehrung,  Ehrerbie- 1 tung,  Huldigung,  Ehrfurcht{sbezeigung)':  | parinavö  .  .  m^vyaAe  .  .  patmrva  hl  °mö  '■ baraiti  paourva  sfartnä  "wer  eine  Feder  \ des  . .  Vogels  hat,  der  gewinnt  sich  zuert Huldigung  .  ."  Yt.  14.  36;  —  sonst  nur  in ' Beziehung  auf  Gottheiten  gebraucht:  haomö .  .  yakmäi  kvan  .  .  dural  'mS  l/ao6ayeiü  1 Yt.  jo.  90;  —  namistaAyä  {sd.)  °maaAä'^ fiii  .  .  paitJ.jamyä  Y.jß.s;  ~~  tat  vS  11}  \ hazaosanks(f.d.)  . .  daiäySi  savH  ahm  vohü\ manatihä  .  .  yaz:>mniN/iS {sA.)  °mai^h3''*\ Y.j/.  20;  —  at  töi  myazdtm  ..  'maahä^ .  .  däm3  (sd.)  y.^^.  3;  —  tsm  ttS  staotais 'maahS  ^a.vlvanlö  (sd.)  Y.  45-  8 ;  —  'maaka  ' aoara  data  ajasani  upara  data  Yt.JO.  118; 118;  —  mi%rim  . .  pairi.jasäi  vantaca 'maahaca  Yt/o.  6;  —  kn  nS  (näml.yVa- Tialls)  stavät  .  .  asa.näsa  "maaha  Yt.  /J. 50; —  'maAT  fySntä  *akura.mazdä  'mahi (LS.  als  Inf)  usSmahi  'mat»ki  (DS,  als Inf.)  vTsilmaidJ  "wir  haben  Freude  an  deiner Verehrung,  o  AAM.,  wir  wünschen  (dich) zu  verehren,  wir  sind  bereit  (dich)  zu  ver- ehren" ^.58.  3JI;  —  mit  Dat  des  Gottes, dem  die  Huldigung  gilt:  'matgkä  a/ni  . . avat  ituyl'^.  12.  3;  —  a/  3  %waAmai  äkre rtltqm  (sd.)  'manAS  .  .  Y.  4j.  9.  a)  bes. NS.  in  elliptischen  Sätzen«;  der  Name  der Gottheit  folgt  im  a)  Vok,:  °m^  urvaireV. ig.  18;  YLi.  21;  —  'num^l  kttvatm  y^arms Yt  /.  2 1 ;  18.  7.  b)  Dat  oder  Gen. :  'mB ahuräi  mazdai  °mS  anDsaHbyH  sp^ntaeibyS *mS^  .  .  'ms  gsul  'mS  gayehe  'mS  lara- "kusirahe ..frava^e  'mstn^'^  vJspayh  afaonS stBis  Y.  68.  22;  g.3,  16,  JO.  13, 17',  2o',Yt /.2iJ,7.iS,  JO.91, V./5.25';  — gave  am^m gave  'm?mi*  Vt/i^.  61,  c)  Vok.  hinter dem  enkl.  Dat-Gen.  des  Fron.  2.  Person: n;mas>  ti  aAura  mazda  .  .  'mB  vS  amf^ä spinta  Ny.  /.  1 ;  j.  4,  Y.58. 7,  V.  21. 1*;  — •mS  vS  gaha  alaonilY.  28.0,  43.  o,  47.0, ^i.o,  SS-o-  d)  Lok.:  'mir  airyene  vai- JaAi  Ytl.21.  OhneWert:  'ttU!  tistrim
21963:—  tat  v!  nS  hazaosaaks  {sd.)  .  .  daidysi sav5  Y.51,  20;  —  tum  v!  asä  tnShmaidi *Aus^axäim  (sd.)  Y.^ff.  13; — tä  vS  urväts margntü  ..  Y.31.1; — katvS  xia^/ym  ks T/ti/(s±)  Y.34.  5;  —  yaHra  v!  aßmänX (sd.)  ssnghsni  Y.46.1T,  —  däitü  .  ,  ya vJ  mq%ra  srmJm  arädä  (sd.)  Y.  2S.  7;  — yöi  vS  yBiktma  (sd.)  dattmi  ststam  Y. 2Ä9;  rit  Ji.  g;  J7. 3;  —  ys  vS  staotais (sd.)  masdä  frJrüli  Y.4g.is;  —  Ayat  vS lUa  (sd.)  vahUtiM  Y.  49.1a;  —  dSi/t  mffi ya  vS  abifra  (sd.)  Y.^.  13;  —  sin:  ya v5  . .  *namam  dadat  . ,  täil . .  Y.3S.  4;
27735:•  j-,  g.  zav-,  zbä-'*  V.  'rufen'.  Praes. 2  sava-,  5  sBm>;  ^  zaosav,  5  +  7  zao- tftv-'>,  24  tiaya';S' AOT.  x  zävii'-.  —  PPfP. 'tbata-;  PFP.  'saoya-.
```


## [2026-09-05T20:59:14.083Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T20:59:14.089Z] TOOL RESULT

```


```


## [2026-09-05T20:59:18.174Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%88%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full etymology of Persian جویدن (javidan) 'to chew': Middle Persian form, Proto-Iranian and PIE reconstruction, cognates, and any alternative forms like جاویدن/جاییدن."
}
```


## [2026-09-05T20:59:19.831Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B3%D8%AA",
 "prompt": "Give the full Persian etymology of دوست 'friend': Middle Persian, Old Persian, Proto-Iranian, PIE root, and cognates cited."
}
```


### [2026-09-05T20:59:25.164Z] TOOL RESULT

```
# Etymology of Persian جویدن (javidan)

**Middle Persian Origin:**
The word derives from Middle Persian jūdan (/⁠jūdan⁠/), continuing an ancient lineage.

**Proto-Indo-European Root:**
It traces back to the PIE reconstruction *ǵyewh₁-, which encompasses the concept of mastication and gnawing across multiple language families.

**Cognate Languages:**
The document lists several related words: English "chew," Pashto ژول (žovạl, "to gnaw"), Baluchi جایگ (jáyag), Northern Kurdish cûtin, and Northern Luri ژایێ (jayı).

**Alternative Forms:**
An alternate spelling جاویدن (jâvidan) exists within Persian itself.

**Semantic Field:**
The verb fundamentally means "to chew" or "to gnaw," with خاییدن (xāyīdan/xâyidan) listed as a synonym, demonstrating consistent usage across Persian dialects.

This etymological trajectory illustrates how ancient Indo-European vocabulary for mastication persists across geographically dispersed modern languages.
```


### [2026-09-05T20:59:26.600Z] TOOL RESULT

```
# Persian Etymology of دوست (Friend)

**Full etymological chain:**

The word traces back through Middle Persian "dwst'" (/dōst/) from Old Persian "𐎭𐎢𐏁𐎫𐎠" (d-u-š-t-a /dauštā/), ultimately deriving from Proto-Iranian "*jawštā́" and Proto-Indo-Iranian "*ȷ́awštā́", which stem from the Proto-Indo-European root "*ǵéws-tōr ~ *ǵus-tr-és" (itself from "*ǵews-").

**Cognates across languages:**

The Wiktionary entry documents numerous descendant terms borrowing from Persian across the region, including Turkish "dost," Urdu "دوست," Uyghur "دوست," and Azerbaijani "dost," among many others listed in the Persian descendants section.

This word represents an ancient Indo-European concept of friendship that spread throughout the Islamic world and Central Asia via Persian transmission.
```


## [2026-09-05T20:59:31.433Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%B1%D5%A1%D5%A3",
 "prompt": "Give the etymology of Armenian ձագ (jag) 'young of an animal, nestling': what origin is proposed, which PIE root if any, and any connection to *gʰaydos 'goat' or to Persian زاق."
}
```


## [2026-09-05T20:59:32.618Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/goat",
 "prompt": "Give the full etymology of English 'goat': Old English gat, Proto-Germanic form, PIE root, Latin haedus, and any Armenian connection."
}
```


### [2026-09-05T20:59:38.505Z] TOOL RESULT

```
# Etymology of Armenian ձագ (jag)

According to the Wiktionary entry, the origin of this word is debated:

**Proposed Origins:**

The word is "usually compared to Albanian _zog_ ('bird; nestling'), Persian _زاق_ (zâq, 'the young of anything'), Sogdian _zāk_ ('child') and Classical Syriac _zāggā_."

**PIE vs. Borrowing:**

Two hypotheses are presented:
1. Inheritance from a "Proto-Indo-European root of the unusual shape _*ǵʰāgʰ-_"
2. Borrowing from Aramaic _zāḡā_ ("young cock or hen"), which would account for the Eastern Armenian _j-_ sound

**Regarding your specific questions:**

- **No mention of *gʰaydos ('goat')**: The entry does not connect this word to the PIE term for goat.
- **Persian connection**: The Persian cognate _زاق_ (zâq) is acknowledged, though the Wiktionary editors note that "the _զ-_ (z-) would be expected in case of an Iranian borrowing," suggesting the Aramaic borrowing hypothesis may be more likely.

The entry concludes that the Aramaic borrowing theory is "more likely" than PIE inheritance.
```


### [2026-09-05T20:59:39.292Z] TOOL RESULT

```
# Etymology of English 'Goat'

**Old English Origin:**
The word derives from Old English *gat*, meaning "she-goat."

**Proto-Germanic Form:**
It comes from Proto-Germanic *\*gaito*, which also produced cognates in Old Saxon *get*, Old Norse *geit*, Danish *gjed*, Dutch *geit*, and German *Geiß*.

**Indo-European Root:**
The ultimate source is PIE *\*ghaid-o-*, meaning "young goat," which also generated words for "to play" across various languages.

**Latin Connection:**
Latin *hædus* ("kid" or young goat) shares this same Indo-European ancestry, demonstrating the widespread distribution of this root.

**Armenian Link:**
While the provided content doesn't explicitly mention an Armenian connection to *goat* specifically, it does note that PIE *\*aig-* ("goat," found in the etymology of *aegis*) has cognates including "Lithuanian ožys" and "Sanskrit ajah"—showing how this root family spread across Indo-European languages, though Armenian isn't mentioned in this particular entry.
```


## [2026-09-05T20:59:52.804Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82/",
 "prompt": "What do Dehkhoda and Farhang-e Mo'in say about the Persian word زاق? Give the definitions verbatim, especially any meaning 'the young of any animal' and any etymological bracket tag. Also anything about زاقدان."
}
```


## [2026-09-05T20:59:54.629Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD zak ===\"; grep -n \"z’k\\|zāk\\|zak \\|child\" SOD.txt | head -20",
 "description": "Grep Gharib Sogdian for zāk"
}
```


### [2026-09-05T20:59:54.682Z] TOOL RESULT

```
=== SOD zak ===
8368:being,  child 
10120:creature,  being,  child(w/z*c/i  has  been  born  or 
10330:child,  existence,  life 
10336:childhood 
20034:uzak   =*wjk-k 
23326:child,  son 
24405:Po6eze,  PiSezak   =»p5>yz- 
26333:child 
27700:Pize,  pizak  ? 
29417:cuzak   ©Yaghn.  cuja%  Khwar.  twzk 
39193:small  girl,  child 
39638:krazak  ?  ©<Skt.  kasaya 
39747:korn/zak  ?  (krz'kh)  ©Skt.  vidisah 
40982:child 
44672:mozak   (mwj'q)  ©pi.  -/   =>mwz*k\  mwc'k' 
44956:mozak   ^mwj'k,  mwc^1 
66097:child,  small,  little 
66130:childhood 
66138:child,  little,  light 
68547:childless
```


### [2026-09-05T20:59:57.678Z] TOOL RESULT

```
# Definitions of زاق

**Dehkhoda Dictionary:**
States that زاق means "بچه هر چیز را گویند" (the young of any animal), marked with etymological bracket (اِ). It also notes a reference to زاقدان, along with related terms زاق و زیق.

**Farhang-e Mo'in:**
Provides the concise definition: "(اِ. ) بچة هر چیز" (the young of any animal), using the same etymological marker (اِ).

Both sources agree on the primary meaning regarding offspring, and both include the etymological bracket notation indicating this is a Persian (not Arabic) term.
```


## [2026-09-05T21:00:08.787Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/disgust",
 "prompt": "Full etymology of 'disgust': French desgouster / Middle French desgoust, Latin gustus, PIE root. Quote the chain."
}
```


## [2026-09-05T21:00:09.945Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82%D8%AF%D8%A7%D9%86/",
 "prompt": "What do Dehkhoda and Farhang-e Mo'in say about زاقدان? Give the definitions verbatim, especially any meaning 'womb' (زهدان/رحم)."
}
```


### [2026-09-05T21:00:13.846Z] TOOL RESULT

```
# Etymology of "Disgust"

The word "disgust" traces back through multiple linguistic layers:

**French origins:** The term comes from French *desgoust* (Modern French *dégoût*), meaning "strong dislike, repugnance," which is literally "distaste."

**Latin foundation:** The French *gouster* derives from Latin *gustare*, meaning "to taste."

**Indo-European root:** This ultimately connects to the PIE root *\*geus-*, which means "to taste; to choose."

The word entered English around the 1590s with the sense of "repugnance excited by something offensive or loathsome," initially retaining its literal meaning of "distaste" before evolving to describe emotional revulsion more broadly.
```


### [2026-09-05T21:00:16.040Z] TOOL RESULT

```
# Definitions of زاقدان

**Dehkhoda Dictionary:**
"بچه دان و زهدان را گویند" (refers to baby dan and zehdan). It also notes: "قرارگاه نطفه در شکم که آن را زهدان نیز گویند و بتازیش رحم خوانند" (the site of conception in the belly, also called zehdan, and its renewal is called womb).

**Farhang-e Mo'in:**
"بچه دان ، زهدان" (baby dan, zehdan)

Both sources identify زاقدان as relating to reproductive anatomy, with Dehkhoda explicitly connecting it to the womb (رحم).
```


## [2026-09-05T21:00:25.012Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5%CA%B0h%E2%82%81eydos",
 "prompt": "Is there a PIE reconstruction page for 'goat' (*gʰaidos / *ǵʰaydos)? Give its meaning, descendants (Latin haedus, Proto-Germanic *gaits, Albanian), and any Armenian or Iranian descendant."
}
```


### [2026-09-05T21:00:26.787Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T21:00:27.560Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5ews-",
 "prompt": "Give the PIE root *ǵews-: meaning, derived terms, and descendants — especially Proto-Indo-Iranian *ȷ́awš-, Avestan zaoša-, Old Persian dauštā, Proto-Germanic *keusaną, Latin gustus, Greek geuomai."
}
```


### [2026-09-05T21:00:34.508Z] TOOL RESULT

```
# Proto-Indo-European Root *ǵews-

## Meaning
The root *ǵews- means **"to taste, try"** according to the Wiktionary reconstruction.

## Key Derived Terms

The root generated numerous morphological variants, including:
- Thematic present: *ǵéws-e-ti
- Reduplicated forms: *ǵu-ǵéws-ti ~ *ǵú-ǵus-nti
- Nominal derivatives: *ǵéws-ti-s ~ *ǵus-téy-s

## Major Descendants

**Proto-Indo-Iranian:** *ȷ́awš- family, yielding:
- Avestan zušta (tasted)
- Sanskrit juṣṭá (enjoyed)

**Proto-Germanic:** *keusaną (to try, choose), leading to English "choose"

**Proto-Celtic:** *guseti (to choose)

**Proto-Hellenic:** Ancient Greek geustós (tasteable)

**Proto-Anatolian:** Hittite kukušzi (to taste)

The root demonstrates the typical Indo-European pattern of ablaut variation and productive derivational suffixation across language families.
```


## [2026-09-05T21:00:39.778Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gaits",
 "prompt": "Give the etymology of Proto-Germanic *gaits 'goat': PIE source, cognates (Latin haedus, Albanian), descendants (Gothic gaits, Old English gāt, Old High German geiz). Any Armenian mention?"
}
```


## [2026-09-05T21:00:41.617Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kewwan%C4%85",
 "prompt": "Give the etymology of Proto-Germanic *kewwaną 'to chew': PIE root, cognates including Persian javidan, descendants (Old English cēowan, OHG kiuwan)."
}
```


### [2026-09-05T21:00:46.698Z] TOOL RESULT

```
# Etymology of Proto-Germanic *gaits

Based on the Wiktionary entry, here's what we know about the word's origins:

## Etymology Summary

The article states that *gaits "cannot be traced back to Proto-Indo-European." Instead, according to Bjørn's research, it may derive "from the same source as Proto-Semitic *gady-, Proto-Berber *e-ɣăyd, and Proto-Nakh *gaaʒaᶰ."

The entry also notes a cognate relationship with Proto-Italic *haidos, suggesting a non-Indo-European origin story for this word.

## Key Descendants Mentioned

- **Gothic:** gaits
- **Old English:** gāt
- **Old High German:** geiȥ

The article documents extensive Romance language borrowings (Spanish, Catalan, Galician, Portuguese gaita) seemingly from Gothic.

## Missing Information

The document contains **no mention of Latin haedus, Albanian cognates, or Armenian**. While you asked specifically about these languages, they don't appear in this Wiktionary reconstruction entry. The focus remains on Germanic and non-Indo-European language families instead.
```


### [2026-09-05T21:00:47.540Z] TOOL RESULT

```
# Etymology of Proto-Germanic *kewwaną

**PIE Root:** The term derives from Proto-Indo-European *ǵyewh₁-, meaning "to chew."

**Cognates:** Related words appear across Indo-European languages:
- Tocharian B: śuwaṃ ("to eat")
- Polish: żuć ("to chew")
- Persian: javidan
- Pashto: žovạl ("to bite, gnaw")

**Descendants:** The verb spread throughout Germanic languages:
- **Old English:** ċēowan → Modern English "chew"
- **Old High German:** kiuwan → Modern German "kauen"
- **Old Norse:** tyggva/tyggja → Swedish "tugga," Danish "tygge"
- **Old Frisian & Old Saxon:** kiāwa/kiuwan → West Frisian and Low German variants
- **Old Dutch:** kiuwan → Modern Dutch "kauwen"

The word reflects a strong class 2 verb pattern and remained productive across Germanic branches, with some descendants becoming weak verbs in later stages.
```


## [2026-09-05T21:00:59.685Z] TOOL CALL #64: Bash

```json
{
 "command": "pdftoppm -f 178 -l 178 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg178 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 178"
}
```


## [2026-09-05T21:01:00.233Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chew",
 "prompt": "Full etymology of 'chew': Old English ceowan, Proto-Germanic *keuwan, PIE root, and cognates including Persian javidan."
}
```


### [2026-09-05T21:01:01.823Z] TOOL RESULT

```
total 23816
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:01 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T21:01:09.452Z] TOOL RESULT

```
# Etymology of "Chew"

The word "chew" traces back to Old English **_ceowan_**, derived from West Germanic **_*keuwwan_**. This likely stems from the Proto-Indo-European root **_*gyeu-_**, meaning "to chew."

## Key Historical Points

**Verb origins:** The term has cognates across multiple language families, including Old Church Slavonic _živo_, Lithuanian _žiaunos_ (jaws), and Persian _javidan_. Germanic relatives include Middle Low German _keuwen_, Dutch _kauwen_, and German _kauen_.

**Figurative development:** The meaning "to think over" emerged in the late 14th century. The phrase "chew the rag" ("discuss some matter") originated as British army slang around 1885, while "chew (someone) out" developed as military slang during World War II (1948).

**Noun form:** As a standalone noun from around 1200, it initially meant "an act of chewing." By 1725, it referred to "wad of tobacco chewed at one time," and by 1906 it described a type of chewy candy.

## Related Terms

**Chewing-gum** (1843) was originally "hardened secretions of the spruce tree." The adjective **chewable** emerged in 1827, combining the verb with the suffix "-able."
```


## [2026-09-05T21:01:12.855Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg178.png"
}
```


### [2026-09-05T21:01:13.279Z] TOOL RESULT

```

```


## [2026-09-05T21:01:13.274Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:01:33.164Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 178 -l 178 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg178_hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg178_hi.png'); print(im.size)\nw,h=im.size\n# crop left part of the Ghaido entry: y from ~0.47*h to 0.62*h, x 0.15-0.55\nim.crop((int(0.17*w),int(0.485*h),int(0.60*w),int(0.63*h))).save('ghaido_left.png')\nim.crop((int(0.17*w),int(0.29*h),int(0.60*w),int(0.47*h))).save('geus_left.png')\n\"",
 "description": "Crop chart regions"
}
```


### [2026-09-05T21:01:36.247Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T21:01:38.582Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ghaido_left.png"
}
```


### [2026-09-05T21:01:38.595Z] TOOL RESULT

```

```


## [2026-09-05T21:01:49.602Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg178_hi.png'); w,h=im.size\nim.crop((int(0.18*w),int(0.555*h),int(0.45*w),int(0.635*h))).save('ghaido_low.png')\n\"",
 "description": "Crop lower Ghaido region"
}
```


### [2026-09-05T21:01:51.913Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:01:54.506Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ghaido_low.png"
}
```


### [2026-09-05T21:01:54.516Z] TOOL RESULT

```

```


## [2026-09-05T21:01:58.801Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg178_hi.png'); w,h=im.size\nim.crop((int(0.18*w),int(0.53*h),int(0.45*w),int(0.63*h))).resize((int(0.27*w),int(0.10*h))).save('g2.png')\nim.crop((int(0.18*w),int(0.585*h),int(0.45*w),int(0.625*h))).save('g3.png')\n\"",
 "description": "Crop Germanic row"
}
```


### [2026-09-05T21:02:00.540Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:02:02.847Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g3.png"
}
```


### [2026-09-05T21:02:02.857Z] TOOL RESULT

```

```


## [2026-09-05T21:02:07.427Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg178_hi.png'); w,h=im.size\nim.crop((int(0.18*w),int(0.60*h),int(0.45*w),int(0.68*h))).save('g4.png')\n\"",
 "description": "Crop Germanic row lower"
}
```


### [2026-09-05T21:02:09.522Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:02:12.134Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g4.png"
}
```


### [2026-09-05T21:02:12.150Z] TOOL RESULT

```

```


## [2026-09-05T21:02:50.715Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN choose\"; grep -n \"^choose,\\|^choice,\" KLN_1966.txt | head; sed -n \"$(grep -n '^choose,' KLN_1966.txt | head -1 | cut -d: -f1),+3p\" KLN_1966.txt | cut -c1-900\necho \"### KLN disgust\"; sed -n \"$(grep -n '^disgust,' KLN_1966.txt | head -1 | cut -d: -f1),+2p\" KLN_1966.txt | cut -c1-700\necho \"### KLN goat\"; sed -n \"$(grep -n '^goat,' KLN_1966.txt | head -1 | cut -d: -f1),+2p\" KLN_1966.txt | cut -c1-900\necho \"### KLN gust\"; grep -n \"^gust,\\|^gusto,\" KLN_1966.txt | head",
 "description": "Klein entries for choose/disgust/goat"
}
```


### [2026-09-05T21:02:52.908Z] TOOL RESULT

```
### KLN choose
7518:choose,  tr.  and  intr.  v.  —  ME.  cheosen,  chesen, chusen,  fr.  OE  ceosan ,  rel.  to  OS.,  OHG.  kiosan, ON.  kjosa,  OFris.  kiasa,  Du.  kiezen,  MHG.,  G. kiesen,  Goth,  kiusan,  ‘to  choose’,  and  to  Goth. kausjan,  'to  prove,  test’,  fr.  I.-E.  base  *geus-, *gus-,  ‘to  taste,  enjoy  by  tasting',  whence  also Gk.  yeuectFxi,  ‘to  taste’,  L.  gustdre,  ‘to  taste, enjoy’,  OI .  jdsati,juydte,  ‘enjoys’,  Avestic zaosh-, ‘to  find  delicious’,  OIr.  gu-,  go-,  ‘to  choose’.  Cp. OE.  coslian,  OS.,  OHG.  kosron,  ON.  kosta, MHG.,  G.  kosten ,  ‘to  test,  try,  taste’,  which  are all  related  to  OE.  ceosan,  etc.  F.  choisir,  ‘to choose’,  OProveng.  causir,  ‘to  look  at’,  OSlav. kusili ,  to  taste,  try’,  are  Goth,  loan  words.  Cp. choice.  Cp.  also  gust,  ‘relish’,  disgust,  and  the second  element  in  Fergus  and  in  valkyrie.
choose,  tr.  and  intr.  v.  —  ME.  cheosen,  chesen, chusen,  fr.  OE  ceosan ,  rel.  to  OS.,  OHG.  kiosan, ON.  kjosa,  OFris.  kiasa,  Du.  kiezen,  MHG.,  G. kiesen,  Goth,  kiusan,  ‘to  choose’,  and  to  Goth. kausjan,  'to  prove,  test’,  fr.  I.-E.  base  *geus-, *gus-,  ‘to  taste,  enjoy  by  tasting',  whence  also Gk.  yeuectFxi,  ‘to  taste’,  L.  gustdre,  ‘to  taste, enjoy’,  OI .  jdsati,juydte,  ‘enjoys’,  Avestic zaosh-, ‘to  find  delicious’,  OIr.  gu-,  go-,  ‘to  choose’.  Cp. OE.  coslian,  OS.,  OHG.  kosron,  ON.  kosta, MHG.,  G.  kosten ,  ‘to  test,  try,  taste’,  which  are all  related  to  OE.  ceosan,  etc.  F.  choisir,  ‘to choose’,  OProveng.  causir,  ‘to  look  at’,  OSlav. kusili ,  to  taste,  try’,  are  Goth,  loan  words.  Cp. choice.  Cp.  also  gust,  ‘relish’,  disgust,  and  the second  
Derivatives:  choos-er,  n.,  choos-ing,  adj.,  choos¬ ing-!}',  adv.
chop,  tr.  and  intr.  v.,  to  cut.  —  ME.  choppen,  ‘to cut  up’,  in  gradational  relationship  to  ME.  chap- pen,  ‘to  cut’.  See  chap,  ‘to  chop’,  and  cp.  chip. Derivatives:  chop ,  n.,  chopp-er,  n.,  chopp-ing, adj.,  chopp-y,  adj.
chop,n.,  t)jaw;  2)  entrance  ofa  valley  or  channel.
### KLN disgust
sed: -e expression #1, char 1: unknown command: `,'
### KLN goat
sed: -e expression #1, char 1: unknown command: `,'
### KLN gust
16893:gust,  n.,  a  sudden  blast  of  wind.  —  ON.  gustr, ‘gust,  blast’,  formed  with  suff.  -t  from  gus-, weak  grade  of  gjosa,  ‘to  gush’.  See  geyser. Derivatives:  gustful  (q.v.),  gust-y,  adj.,  gusti-ly, adv.,  gust-i-ness,  n.
16894:gust,  n.,  relish.  —  L.  gustus,  ‘tasting,  taste’.  See choose  and  cp.  gout,  gustation,  gusto,  degust, disgust,  ageustia,  ragout.
16900:gusto,  n.,  taste;  keen  relish.  —  It.,  fr.  L.  gustus, ‘tasting,  taste’.  See  gust,  ‘taste’, gut,  n.,  the  alimentary  canal;  the  intestines.  — ME.  gut,  gutte,  fr.  OE.  guttas  (pi.),  ‘entrails’, rel.  to  MDu.  gote,  Du.  goot,  G.  Gosse,  ‘gutter, drain’,  ME.  gote,  ‘channel,  stream’,  and  in  grad¬ ational  relationship  to  OE.  geotan,  ‘to  pour’. See  found,  ‘to  cast’,  and  cp.  words  there  referred to.  Cp.  also  guttle.
```


## [2026-09-05T21:02:53.577Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SKT chew/goat/choose\"; grep -n \"^CHEW\\|^GOAT\\|^CHOOSE\\|chew (1)\\|goat (E.)\" SKT.txt | head\ngrep -n \"ceowan\\|kiusan\\|gát, a goat\\|haedus\" SKT.txt | head -10\necho \"### LEW gustus\"; grep -n \"gustus\\|gusto,\" LEW_1910.txt | head -5\necho \"### LAT gustus\"; grep -n \"gustus\" LAT.txt | head -5",
 "description": "Skeat and Latin dictionaries"
}
```


### [2026-09-05T21:02:53.658Z] TOOL RESULT

```
### SKT chew/goat/choose
### LEW gustus
### LAT gustus
810:Dioscoride les formes abalbus, abangustus qui dquivalent 4 des comparatifs,
3772:angiportus, -us a.(et angiportum n.): = uicus angustus, ruelle,
3774:a ango qui a disparu au profit de angustus ; le second est le mot portus
3798:angustus: etroit,serre; peut-etre d'un thfeme en -s-, cf. onus/onus tus ;
3799:robustus, augustus, uetus/uetustus? D'ou angustia, employe surtout au
```


## [2026-09-05T21:03:37.226Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN disgust\"; grep -n \"^disgust\" KLN_1966.txt | head -3 | cut -c1-800\necho \"### KLN goat\"; grep -n \"^goat\" KLN_1966.txt | head -3 | cut -c1-900\necho \"### SKT chew\"; grep -n -i \"^chew\\|Chew\\.\" SKT.txt | head -5 | cut -c1-500\necho \"### SKT goat\"; grep -n -i \"^goat\\|Goat,\" SKT.txt | head -5 | cut -c1-500\necho \"### LAT gust\"; grep -n \"gust[oau]\" LAT.txt | head -8 | cut -c1-300",
 "description": "More dictionary lookups"
}
```


### [2026-09-05T21:03:37.342Z] TOOL RESULT

```
### KLN disgust
### KLN goat
16373:goatee,  n.,  a  man’s  beard  resembling  a  goat’s beard.  —  Formed  from  prec.  word  with  suff.  -ee. Derivative:  goate-ed,  adj. gob,  n.,  a  mouthful  of  saliva;  a  lump  of  slimy substance.  —  OF.  gobe,  ‘a  mouthful,  a  lump’ [whence  F.  gobe,  gobbe,  ‘fattening  ball  (for poultry);  poisoned  ball  (for  a  dog)’],  of  Celtic origin;  cp.  Ir.  gob,  ‘mouth’,  Gael,  gob,  ‘beak’. Cp.  gobbet,  gobble,  ‘to  eat  greedily’,  goblet, gob,  n.,  a  sailor  in  the  navy  (slang).  —  Perh.  lit.
17852:goat ;  of  a  rank  smell.  —  L.  hircinus,  ‘pertaining to  a  he-goat’,  fr.  hircus,  ‘he-goat’,  which  is  prob. rel.  to  hirsutus,  ‘shaggy,  prickly,  bristly’.  See hirsute  and  adj.  suff.  -ine  and  cp.  hearse, hire,  n.  —  ME.,  fr.  OE.  hyr,  ‘hire,  wages,  usury, interest’,  rel.  to  OS.  hura,  huria,  Dan.  hyre, Swed.  hyra,  ‘hire,  wages’,  OFris.  here,  MLG., MDu.  hure,  Du.  hour,  G.  Heuer,  ‘hire,  wages, rent,  lease’.  The  ulterior  etymol.  of  these  words is  unknown.
### SKT chew
3372:Chew,   Chaw.    ^E)      M.  E A.S.  f^rwjw.  lochcw.eaL  +  Du. G,  kaucn  ;  Rtiss.  Jafaf9,     Der. a  jaw;  now  spclt/dtv.
9446:FonBcxlyciow;  see  Chew.
10867:maxUl&r,  maxiUary.  belonging  to the  jawbone.  (L.)  L.  wHUciiiaris,  adj., from  maxiJ/a,  jaw-bone.  •L.  mtacerart,  to chew.
11026:Mandible,  a  jaw.  (L.)  L.  mandihila^ jaw.  — L.  mandtre,  to  chew.
11027:man^p  scab  or  itch  in  dogs.  (F.»L.) Made  out  of  ndj.  mangy ^  an  oUleT  word.— F.  mangr,  ealm,  fed  on :  pp.  of  manger,  to trat.  —  L.  manduiare,  to  eat.  —  L.  matuiucHi, a  glutton.  — L.  mandtre,  to  chew.
### SKT goat
2384:broiling  men  and  animals.  The  word  AMtfOJt is  said  to  be  Caribbean,  and  to  mean  'a place  where  meat  is  smoke-dried.* Buck  ( I ),  a  male  deer,  goat.  (£.)  M.  £. bukke.  A.  S.  btuca,  a  he-goat.  +  Dn.  bok, Icel.  buJbir,  Swed.  boci,  a  he-goat;  Dan. Ouk,  a  he-goat,  ram,  buck;  G.  bcKi,  W. dwch,  Gael,  doc,  Irish  boc.  Also  Skt.  buJkJka, a  goat.
2946:Capatan.  (F.  — Span.— L.?)  )e.ci\btstan. ^Span.  (c^strantf,  <abrcstante,  an  cnijinc to  raise  weights.  £tym.  uncertain:  but Min&heu'B  Span.  Diet.  0^^3)  ba&  cabtt- itanti  as  the  form,  and  Monlaa's  £tym. Span.  Diet.  (i88i)  has  cabria,  a  crane, and  suggests  Span,  cobra  estantt,  a  fixed (permanent)  goat;  since  the  Span.  eain-A meana  (i)  goat,  (i)  a  machine  for  throw- ing large  clones.  Here  Sp.  ca^^a^L.  i-fl//tf» a  she-goat ;  sec  Oaper
15070:Pulley.  (F.  -  L.)  M.E  /•/iW  ( poiivi,  riming  with  dhv?),  Ch. ; poltyn*^  Prompt.  Parv.  The  latter  foi from  Y.p<mlain,  *  a  fole,  a  colt,  also  the wherewith  wine  is  let  clown  into  a  kI [cellar],  a  pulley-ro{)e;'  Cot  — Low  L./ /anus,  A  colt.  m,l^  pH//us,  A  yoang  anii see  pullet,  s.v.  Pool  (a).  SoalsoE./ii( an^twers  to  mod.  F.  pouJif.  p.  Tbc  inl fcrcnoc  of  sense  causes  no  diffioilty ;  thu ppu^rt,  a  filly,  also  means  a  beam, 
23908:Cheverll.  kid  leather.     (F.-L.)    OF. chevrtl  (mod.    F.   chfvreau)^  a leather.      Dimin.  of  O.F.  ^hevre^  F, a  goat,  kid,  — L.  capram^  ace  of  c she-goal.
### LAT gust
810:Dioscoride les formes abalbus, abangustus qui dquivalent 4 des comparatifs,
3772:angiportus, -us a.(et angiportum n.): = uicus angustus, ruelle,
3774:a ango qui a disparu au profit de angustus ; le second est le mot portus
3798:angustus: etroit,serre; peut-etre d'un thfeme en -s-, cf. onus/onus tus ;
3799:robustus, augustus, uetus/uetustus? D'ou angustia, employe surtout au
3802:ei cruciatus. De la: angusto,-as, et angustio, -as (b.latin) angustio-
3804:angustus figure comme premier terme de compos 4 dans angusticlduus,
3821:angustus (avec ses derives); cf.v.h.a .angust "angoisse". Le thfeme en
```


## [2026-09-05T21:03:45.206Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16370,16374p' KLN_1966.txt | cut -c1-1200\necho \"### disgust\"; grep -n \"disgust,  tr\\|disgust,  n\" KLN_1966.txt | head -3\ngrep -n \"desgouster\\|desgout\\|dis-  and  L\\.  gustare\" KLN_1966.txt | head -5 | cut -c1-600",
 "description": "Klein goat and disgust"
}
```


### [2026-09-05T21:03:45.291Z] TOOL RESULT

```
All  these  words  are  traceable  to  I.-E.  base  *ghei-, ‘to  drive  on,  push  on’.  Cp.  gore,  ‘a  triangular piece  of  land’,  and  words  there  referred  to. Derivative:  goad,  tr.  v.
goaf,  n.,  the  open  space  from  which  the  coal  has been  extracted  (dial.  E.)  —  ME.  golf,  ‘heap  of sheaves  placed  in  a  barn’,  fr.  ON.  golf,  ‘floor,, apartment,  division’.
goal,  n.  —  ME.  gol,  ‘limit,  boundary’,  prob.  fr. OE.  *gal,  ‘hindrance’,  whence  gxlan,  ‘to  hin¬ der’;  see  gill,  ‘ravine’.  For  sense  development cp.  L.  meta,  ‘end,  boundary;  goal’, goat,  n.  —  ME.  goot,  gote,  fr.  OE.  gat,  rel.  to  OS. get,  ON., Norw.  geit,  Swed.  get,  Dan .gjed,  MDu. gheet,  Du.  geit,  OHG.,  MHG.  gets,  G.  Geifi, Goth,  gaits,  ‘goat’,  fr.  I.-E.  base  *ghaido-,  ‘kid, goat’,  whence  also  L.  haedus,  ‘kid,  young  goat’. Derivatives:  goatee  (q.v.),  goat-ish,  adj.,  goat- ish-ly,  adv.,  goat-ish-ness,  n.,  goat-ling,  n., goat-ly,  adj.
goatee,  n.,  a  man’s  beard  resembling  a  goat’s beard.  —  Formed  from  prec.  word  with  suff.  -ee. Derivative:  goate-ed,  adj. gob,  n.,  a  mouthful  of  saliva;  a  lump  of  slimy substance.  —  OF.  gobe,  ‘a  mouthful,  a  lump’ [whence  F.  gobe,  gobbe,  ‘fattening  ball  (for poultry);  poisoned  ball  (for  a  dog)’],  of  Celtic origin;  cp.  Ir.  gob,  ‘mouth’,  Gael,  gob,  ‘beak’. Cp.  gobbet,  gobble,  ‘to  eat  greedily’,  goblet, gob,  n.,  a  sailor  in  the  navy  (slang).  —  Perh.  lit.
‘a  lump’,  and  orig.  identical  with  prec.  word, gobang,  also  goban,  n.,  a  Japanese  game  resem¬ bling  checker.  —  Japan,  goban,  corruption  of Chinese  k'i-p'an ,  ‘checkerboard’, gobbet,  n.,  a  piece  of  flesh;  a  lump  of  food  (ar¬ chaic  or  rare).  —  ME.  gobet,  ff.  OF.  gobet, dimin.  of  gobe,  ‘a  mouthful,  a  lump’.  See  gob,  ‘a mouthful’,  and  dimin.  suff.  -et  and  cp.  goblet, gobble,  tr.  and  intr.  v.,  to  eat  greedily.  —  Formed with  freq.  suff.  -le  fr.  F.  gober,  ‘to  gulp  down, swallow’,  fr.  OF.  gobe,  ‘a  mouthful,  a  lump’. See  gob,  ‘a  mouthful’.
### disgust
11689:Derivatives:  disguise,  n.,  disguis-ed,  adj.,  dis- guis-ed-Iy,  adv.,  disguis-ed-ness,  n.,  disguis-er,  n. disgust,  tr.  v.  —  Earlier  F.  desgouster  (F.  de- gouter),  ‘to  disgust’,  fr.  des-  (fr.  L.  dis-)  and gouster  (F.  gouter),  ‘to  taste’,  fr.  L.  gustare,  of s.m.  See  gust,  ‘relish’,  and  cp.  degust. Derivatives:  disgust-ed,  adj.,  disgust-ed-ly,  adv., disgust-ed-ness,  n.,  disgust-er,  n.,  disgust-ing, adj.,  disgust-ing-ly,  adv.,  disgust- ing-ness,  n. disgust,  n.  —  Earlier  F.  desgoust  (F.  degout),  fr. desgouster.  See  disgust,  v.
11689:Derivatives:  disguise,  n.,  disguis-ed,  adj.,  dis- guis-ed-Iy,  adv.,  disguis-ed-ness,  n.,  disguis-er,  n. disgust,  tr.  v.  —  Earlier  F.  desgouster  (F.  de- gouter),  ‘to  disgust’,  fr.  des-  (fr.  L.  dis-)  and gouster  (F.  gouter),  ‘to  taste’,  fr.  L.  gustare,  of s.m.  See  gust,  ‘relish’,  and  cp.  degust. Derivatives:  disgust-ed,  adj.,  disgust-ed-ly,  adv., disgust-ed-ness,  n.,  disgust-er,  n.,  disgust-ing, adj.,  disgust-ing-ly,  adv.,  disgust- ing-ness,  n. disgust,  n.  —  Earlier  F.  desgoust  (F.  degout),  fr. desgouster.  See  di
```


## [2026-09-05T21:03:55.178Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\necho \"### ARY latin index\"; grep -n -i \"javidan\\|jav-\\|geus\\|gieu\\|ghaido\\|dost\" ARY_latin_index_pages.txt | head -20\necho \"### ARY persian\"; grep -n \"جویدن\\|دوست\\b\\|زاق\" ARY_pages.txt | head -10 | cut -c1-200",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T21:03:55.241Z] TOOL RESULT

```
### ARY latin index
5993:MALLORY & ADAMS: TUSSKJOS DOST :(OLD HIGH GERMAN) 5 gist
8285:CHOOSE ENGLISH) .,SSil DOST, DAUSHTA, DOSHIDAN
### ARY persian
36:امیدوارم که این کتاب دوست‌داران زبان پارسی و زبانشناسی را خوش آید.
75:خانواده‌ی بزرگك از هندوستان و فلات ایران تا باختر اروپا و بریتانیای کبیر گسترش دارند. برخی
102:ساسکریت در هندوستان و (بسه طور نادرتر) برای اشاره به زبانهای اییرانی و هندی
114:سرزمین کم‌کم از یک سو به فلات ایران و شمال هندوستان و از سوی دیگر به آسیای صغیر و از آنجا
167:صغیر و فلات ایران و هندوستان را زیر مهمیز خود درآوردند.
245:سارماتی * سغدی * خوازمی + فارسی > پشتو + زبانهای هندوستان شمالی. جهت این موج‌های
356:در جنوب هندوستان نیز زبانهای غیر هند و اروپایی (مثلاً «دراویدی» 2۸۷101۸7 و
357:«مونداء ۸]۲7870۸) هنوز رایج‌اند. قراین نشان می‌دهند که در شمال هندوستان هم زبانهای غیر هند و
426:تسلط انگلستان بر هندوستان و یافت نوشتارهای کهن هندی
427:در سده‌ی هیجدهم میلادی انگلستان هندوستان را تصرف کرد. یکی از پیامدهای تماس
```


## [2026-09-05T21:03:57.362Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\n# find occurrences of 'zaos' variants\nfor m in re.finditer(r'zao[sš][a-zA-Z]*', t):\n    s=max(0,m.start()-120); print(repr(t[s:m.start()+200])); print('---')\nEOF",
 "description": "Bartholomae zaosa occurrences"
}
```


### [2026-09-05T21:03:59.146Z] TOOL RESULT

```
'P.22;  —  kthrpa \'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail\'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di\'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya\'ia  .  . P.25(?).  a)  substantivisch  \'Wntum\',  mit Gen.  part:  yat  mS  \'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;'
---
'  i  öi  tanättuhtiikänlh  300  [st  a/itr ianisnik  apar  iaiiiin  asf  ailr.  —  S)  Stveri. unter  iipizaita-.\nj.  a-zaosa-  m.  \'Nichtwille,  NichUbsicht\'; yezi  zaela  yezi  -/a  (IS.)  "sei  es  absicht- lich, sei  es  unabsichtlich"  Y. ;.  21.\nPü. :  adSsiinU.\n•  j.,  g.  a-srustay-  f.  \'Ungehorsam\';  vairtTi '
---
'S  viäqnt  (sd.)  Y.  ja. 6;  —  at  räiam  (sd.)  zarakustrB..  daäaitf .  .matdsi.  .°/3i\\.J J.  14;  —  ahurS..°sä hazaosS  tnasda  Y.sg.j;  —  .  yim  \'üt  vahiitS hasaoltm    ahur^m  yäsä   (sd.)  .  .  Y..  28.  8 ;\n—  kadä  vatds  yezT  <ahyä  xlayaüa  (sd.) masda  °sa  (Vok.)  ".  .  o  M.  und  Asa" Y.4<?,g;  '
---
"B  Y.45.\n7;  benutzt  G.j.6,  Vr./Äa,  V.28-,  —  taca .  .  'säum  Mi  (sd.)  yä  xl  ctia  vahisiä hanar»  '^wahtnst  zaosät  dr)gvä  haxiaitl (sd.)  Y.47.S;  —  tat^  %wahmt  *J  dam (sd.)  nipanhe  manS  voha  urunasüä  'säunqm ..  at..  dr?g7-atif  aiäi/ :ifarfhai/ (sd.) paiil urvqnö  paityeintl  Y.4t}.io{.;  zT, "
---
'sa\'ia  ahi  (sd,)  änJ"  Ti.G.a,.  B)  im  Aw.:  y.i^a Xfayamna  ..*d3ilim  Yt  ly.  15;  —  narim  ..  ka\'^aia  K  3s  zaosS  mana  yal  akuraheYt. yl  anhat  . ,  mq\'^rfm  pgr^sS  Y.Cf.t;  Yyt.  \'9.82;  —  vJdylti^d^  saosy u ya\'i:a  hn  asis S0(});  —  h^.\'d\' ioa  y:i:i7i\'7  (sd.)  *asta  Y.   awA«/ V.4Ä9;    —    f'
---
"kad»möi  minas  'rä  Y.  46. , 14; — gätamcä  'räi..t3raohm(^A^  mazdäi ^ Y. 2&5;  —  töi  rwr<7/(sd.)  rädmil  -rahyä- zaosl  mazdä  ^.33.2;   —    yai'ä  xsnaol)H\\\n■ahura-  Noten  292\n(sd.)  'nm  :  .  mazdqm  ^.30.  5;  46.  i;  — y3  vi  staotäis  (sd.)  mazdä  /rlnäi  °rä  Y. 4-9-  12;  34.Zt  45.8;  —  mazdä  .  "
---
'yS  zaotil  asä  "zö/  (AP.) hvd  *mainySuf  H  vakHiilt  kayit  (sd.)  Y. SS\'^\'i  —  \'"^  äng^\'ote  *mar»daili  damä *\'zaos\'^  Aai%Tm  "so  macht  sich  das  Ich des  Z>/-»^enossen  den  gewissen  Lohn  des rechten  Wegs  zu  nichte"  \\.$i.i:i^.\nKompA.;  Ableit.  (s.  auch  är/a/a-).  —  Vgl. *fr>2af\'  EN.  —  ai.  //'
---
") ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]\nai.  iigräiä/i.n-  Adj.  (von  Jndi»  ua.).\n•  j,  ujra.zaosa-  Adj.  (fem.  '!•!-)  'starken sva.  unbeugsamen  Willens  gegenüber  — ' (Dat.) :  /ravasayö . .  °/.f  tbtsyanbyS  Vt  7J.  3 1  .■\n■  j.,  g.  '«  enkl.  Part,  der  Hervorhebung,\nnur  in  f"
---
'als  Indefini- tum,  a)  mit  vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer\':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  \'nicht irgendwie\':  *\'mä\',a  ^'
---
' vorausg.  ja^a  und  folg.  ca  "wie, in  welcher  Weise  auch  immer\':  hvqm  anu usiim  zaos?mca  yaiia  "iiaca  hs  zaosö  "nach seinem  Willen  und  Gefallen,  wie  immer sein  Gefallen  war"  V.2. 11;  Yt/fj.82,  N. _J7.  b)  mit  Neg.  und  folg.  cina  \'nicht irgendwie\':  *\'mä\',a  ^\'i^aäna  paitt.Jime  (.sä.) V'
---
' sollen sie    als  Busse   auf  sich   nehmen"  YL 10.\n•  j.,  g.,  p.  käma-  m.  \'Verlangen,  Wunsch\': haväi  °maua  zaosai\'a\\t.i^.2y,  —  aeiby:! p^r^na  äpansis  (sd.)  "m^m  Y.  2(V.  10;  — arii;ä  vsizdyäi  (sd.)  °mahy3  ^.43. 13.  a)  mit  Akk.  des  Verlangten": /^..-/y- xat  (sd.)  "///?..  dBtVm  ". .  im '
---
'.  Haomakt) \'piin  vaxlayats  V. /O-3;  —  vupimca  \'ß (als  AS.)^\'  ahurahe  mazdä  yazamaide  Y. 77.4;  — yat  dim  mazaos  (sd.)  °/J  türahe V.  13.  39;  —  pueril  zayante  tanuAshrpa \'pa  Yyt.i;  —  biDX\'jqm  tnöi  firasaostrd ..dalddiit  "pJm  (AS.)\'y.5/.  17;  —  upa.- iaht  ar?dvi .  .  kainlnB  \'pa  srtraya '
---
">l  Ob  für  diiy  (S  368.  9)?     Vgl.  liüayatil:\n•  g.  daidyäi  Inf.  'zu  geben,  zu  gewähren': tat  vS  fiS  hazaosauhs  (sd.)  VTSpaahB  d' savB  Y.  57.  20.  \\in}ncä  daidyäi  Y.JJ. 5:  s,  unter  ma/id-.]\nZum  V,  da-.  —  Pü,:  daiiin.\n•  j.  daSvah-  :  dadus-,  da'^us-  Adj.  'der geschaffen   hat,   Sc"
---
"  dSjtt.arita^byS  Y.  ^3.  6 ;  —  lä  varmyanqm^a  'vätqm  Y.  27.  i ;  Yt,  5.  2  2, 'gvatö  *mandaitg  dalnl  *fr>zaos  {sd.)  i0.i)i,  118,  13.78,  137;  —  pairi  main- haihTm  Y-ßi-  13;  4Q.  4;  —  naidä  dahySus  yaoyät  dnijat  ^varmyayäalca  *°vB.i^yJi''^ yni    säslärö    (sd.)     'gvanlB    \\.  4O.  1"
---
'/gg^^  _  „gfig„^g  ^  .j,acargAa  . .  syaeÜFfta .SQ. :  ayäyai.    Zu  F.  S  wird  gesagt,  liaiii  be- 1  ,        azaosa  V  7  3  a  ■  2 1  ■  —  ahuräne\ndeule  meist  ^J/oj/J»,  aber  au  eh  dälavmt.  —  \' \'  "^f  ■"*  " \'  ^f?\'^  ,  *  ■  \'l"  \' \'  ^  ^ \'  "\'"Tratte . . »  irfoÄa- (und  ebenso  "/*nAV,  sd.) '
---
"mS  l/ao6ayeiü  1 Yt.  jo.  90;  —  namistaAyä  {sd.)  °maaAä'^ fiii  .  .  paitJ.jamyä  Y.jß.s;  ~~  tat  vS  11}  \\ hazaosanks(f.d.)  . .  daiäySi  savH  ahm  vohü\\ manatihä  .  .  yaz:>mniN/iS {sA.)  °mai^h3''*\\ Y.j/.  20;  —  at  töi  myazdtm  ..  'maahä^ .  .  däm3  (sd.)  y.^^.  3;  —  tsm  ttS  staotais 'maahS  "
---
"mi  anhvB  ,  .  ^rii^} vahisla  .  .  vUata  (sd.)  P-^p;  -—  inja  ml uruisyat?m  ..ya%a  ia%aca  /y(Sp.  6500.) äs  zaosB  mono  Ytig.83;  —  i/an-stait/ra ml  vXspS  arshul . .  p»sSJanuI  V.  5. 4;  — yavS  ml  malyO  :^arat  V.j.ao;  — yataisa ml  hlm..  an>dvTm\\t5.i;  —  hacanuha  ml ana   ap^rmayäka  'S.  g.  "
---
" tasi^syw\\.i  auch  immer':  tnja  mS  urvisyai?m  .. all  i^Aä  (sd.)  Y.  44.  18.  c)  im  jAw.;!f  ia'ia'a  ..  äs  zaosö  maua  Yt.  ;p.  8a; zu  i);  y  vali  (sd.)  .  .  *dfia  aahS  asOTa  V.  2.  1 1 ;  —  y  ka^aca  dakmS  staofa Y.7J.16;  —  a'ha  JamySt  y'  ä/rTnämi ' yesnya  haurva  ^aoätti  ,  .  a%a  r"
---
"  '%ä  anaif n,/  ^räsdüm  Y.5S.$;¥.43i;  —  avavatam  'vyämrvlta  ..  zura'^idtrö  Y.IS.6;  —  yü sraya  y  dthayatam  zaosö  {akoA.  asti)  Vt  anu  aesqm{sA.)  bar?sma  *frast?nnie  y  . . i/.  11;  —  kihrpa  avaimta  ^sraya  (sd.)  y  jilmäsps  */rast}rmaSa  N.  Äp;  Yt  13.  41; dämqn  sralsttiis  {jii.'aA.  hmti"
---
'dv5.hr3han3m  (sd.)  vayta- n»m  upa.janyatY .^.\\\\.  4)  dasVerbum i^aA\')  ist  weggelassen:  spanim  nida%?m y  dim  mazaos  (sd.)  ksArpB  tarahe  V.  13. 39.  V)    einen   Inhaltssatz    einleitend\n\'dass\';    a)  im  gAw.;    es  folgen  modale\ndby  Google\n1*59  "yatVB   -\nFormen:  tai  möi  daidr  ahura  hy  mazää'
---
'  w? Uta  Äyaniä  .  .  räitr  (sd.)  Y.40.4;  —  ai vS  yaojä  ..  aurvatH   Y.jo.  7;  11,  53.  T,\n—  tat  v!  nS  hazaosaaks  {sd.)  .  .  daidysi sav5  Y.51,  20;  —  tum  v!  asä  tnShmaidi *Aus^axäim  (sd.)  Y.^ff.  13; — tä  vS  urväts margntü  ..  Y.31.1; — katvS  xia^/ym  ks T/ti/(s±)  Y.34.  5;  —  yaHra  v!'
---
"—  gae%A  °pä  . .  *'yll  vohu  '^rao^ta fsA)  manatihä  \\.  34.  y,  —  -pä.stBi'-'' Aujüayö  (sd.) . .  %waAmt  his  zaosi  ^sbaxsS.- hva  Y.  33. 10;  —  tä  casmJng  (sd.)  . .  aibl vamahl 'ps  {AVu.)  'V.ji.  13; $4-  10,57.5. 4^.  I ;  —  °pä  aySrS  * darigd.jyatSis  (sd.) Y.4.J.  a;  ^4.2;  —  bOmTmlS  'pScä "
---
"Sii  (sd.)  Y. 43.y,  —  Jr-a' (Sp.  185  o.)  zJ  kudanks vTspais  mazda  xsmavasa  'vS  Y.J4-3;  —\n—  tat  vS  TiS  hazaosätahs  (sd.)  vlspSnhs daidyli  -vS  Y.  5/,  20;  —  xsa%r>tn  .  . xsmakim  ,,  vahmai  (Sp.  1403  m.)  däidl ■vat»hs  Y.57. 2;  —  auch  Plur.;  yaiSm ■■?vütyär)hs  (sd.)  T^S  xia%r3miä  'vat"
---
"^ä.adhr>m     Bomi.buhnm    tüi.- dqsur?m  vXrS.dra(mat»hftn  gathanqm  bar»- \\a  .  .   iparum    nida%tm  ya{   dtm mazaos' (sd.)   kakrpü  tlirahe  V./;.39;   — sBnahe*>  afvahe  *asta.bifmn{^d.)  V./J.  44; \\pan3m  tairittm  cd^ru.casm>m  spaOfin zairi.gaehm  ä^ritXm  t(äa  altä  pa%ä  vTVä- iayantu  aiwi.nitHsd.)c"
---
'mäJima-.  —  KpQ. : Hlib  ba  yäri  rasandalar.\n•  j-,  g.  zav-,  zbä-\'*  V.  \'rufen\'.  Praes. 2  sava-,  5  sBm>;  ^  zaosav,  5  +  7  zao- tftv-\'>,  24  tiaya\';S\' AOT.  x  zävii\'-.  —  PPfP. \'tbata-;  PFP.  \'saoya-.\n1)  \'Jemanden,  etwas  (Akk.)  lufen,  an- rufen, aufrufen\':  t!ng  sbayä  vanhiu^ uxhäis manankö  "'
---
'i  4;—  im  Neben- satz :  täcä  sp»nt3  mainyü  . .  aiävnZ  Isi^ (Sp.  430  o.)  yä  zi  Mä  vahista  Aanar? %waAmai  zaosäi  dr?gvä  baxsaitl  (sd.)  Y. 47.  S;zT.  verwendet  Y.J2.I.  B)imjAw.: JvB  %J  . ,  mairyS  drrä  .  .  ap>m  Jainti  .  . tiöil  ava%a  m>r>t5  "so  lang  er  lebt,  trifft er  allerdings . .'
---
```


## [2026-09-05T21:04:14.240Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '8270,8300p' ARY_latin_index_pages.txt | cut -c1-300\necho \"=== pdf page tag nearby ===\"; awk 'NR<=8300 && /\\[pdf page [0-9]+\\]/{p=$0} END{}' ARY_latin_index_pages.txt\ngrep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<8300' | tail -3\necho \"### CHEW in ARY index\"; grep -n -i \"CHEW\\|GOAT\" ARY_latin_index_pages.txt | head -10",
 "description": "Aryanpur index lookup"
}
```


### [2026-09-05T21:04:16.102Z] TOOL RESULT

```
POKORNY: 227-228 DOzZAK, DOZE, DnqAx *
MACKENZIE: (HELL) 117 HAPGHANI) (924) glait
-AMINDAROV: (HELL) 235 DOGHAX, DOZAX
Aw igbb oly SANSKRIT) 2 Sit
DVESTI, DVESAS
Aentlaab
Bye Sia 6 ghey WS tans tly gpl hel a=}
[pdf page 287]
tts Ges eee? | YAA
Colge” (& QVANHD  Costetes’ a" 9) DOSH 5s cal eh 3 os! hays
KIASA, ZIASA HAVESTAN) pins
(OLD HIGH GERMAN) oS galt ‘ZAOSH, ZAOSHO, ZUSHTO
KIOSAN (OLD PERSIAN) skool 534,
KIESEN (GERMAN) glT DAUSHTAR, DAUSH-
CBOSAN (OLD ENGLISH) pS 535i! (PAHLAVI) 5 3h,
CHOOSE ENGLISH) .,SSil DOST, DAUSHTA, DOSHIDAN
KIEZEN (DUTCH) ada posT (AFGHANI) (4) lil
s(LITHUANIAN) ale :(KHOTANESE) >
ASAGD, DOGOA, TOGU YSUSDE, YSUA, YSUYAN
-GUSSIM © (OLD IRISH) 45 54),,) (SANSKRIT) cy She
DESHA - ALBANIAN) gt JOSATI, JOSATE, JOSAH, JOSTIS
: GEGEIN GREEK) lin
‘REFERENCES both DEGUNO, GUSTUS — (LATIN) «3
POKORNY SS*C*~C~S~S~S~«S cour FRENCH) il
BARNHART: (CHOOSE) 168 GusTO SPANISH) gly!
DELAMARRE: (GOUT) 88 GusTO HITALIAN) pts}
MACKENZIE: KAUSJAN, KIUSAN :(GOTHIC) S
(LIKE) 121, (FRIEND) 115, (LOVE) 122} (OLD SCANDINAVIAN) pS 5h!
ONIONS: (CHOOSE) 172 KJOSA
Ay buoy KIOSAN (OLD SAXON) of pS
. OLD FRISIAN) oS S23
=== pdf page tag nearby ===
8215:[pdf page 285]
8248:[pdf page 286]
8277:[pdf page 287]
### CHEW in ARY index
164:WY) Spt 9 BE SE ceed Adee 93% Bh y2 9 chew Gb y2 Jad Glogs JL
570:pgs goat ott dye! jhsy ng bad gil jb pbefly Saison BLUSE 3I So
1642:LIT ADT: 2eS5 F0USS oyS sd gh OS- SV Us: stig OD- cy Soihe tlany ply goat ji 3
2291:FEMALE GOAT eed 50 y pt gun ge
3635:‘MACKENZIE: (Goat) 116 OLD HIGH GERMAN) pS galt
3639:AMINDAROY: (GOAT) 231 BUCCA
6219:CHEW HENGLISH) goulSs AFGHAN) (54) gilts!
6233:ONIONS: (CHEW) 168 REFERENCES otha
6234:SKEAT: (CHEW) 106 “Poxoryy = SOSO*~*~S~«S
6235:AMINDAROV: (CHEW) 199 BARNHART: (CHEW) 164
```


## [2026-09-05T21:04:25.971Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\necho \"#### CHEW block\"; sed -n '6200,6245p' ARY_latin_index_pages.txt | cut -c1-250\necho \"--- page tag\"; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<6245' | tail -2\necho; echo \"#### GOAT block\"; sed -n '3615,3650p' ARY_latin_index_pages.txt | cut -c1-250\necho \"--- page tag\"; grep -n \"\\[pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<3650' | tail -2",
 "description": "Read Aryanpur chew and goat blocks"
}
```


### [2026-09-05T21:04:27.720Z] TOOL RESULT

```
#### CHEW block
Olsle aye | VE
JAST (SWEDISH) 54 yo YESHA- 4AFGHANI) (3-4) git
GIST (DUTCH) gocha YAS :(TOKHARIAN A) A 6 ,\55
ws yh AGAULISH) IF Yis (TOKHARIAN B) B s,s
we » 8 * YAS-, YESATI (SANSKRIT) cy Suit
| REFERENCES Denthey yAsaTI, YOSH, YUSHAN
POKORNY, —~SS*~*~*~S~S*~*« EO, ZEIN GREEK) ghiy
BARNHART: ~ (vEAST) 1252 {OLD SCANDINAVIAN) pS Suche!
DELAMARRE: JosTR
(BOUILLIR, BOUILLONNER) 261 JOSTR (OLD NORSE) aS e335
BUCK: 676 JESAN:(OLD HIGH GERMAN) pS gas
ONIONS: (YEAST) 1019 GAREN, GISCHT — (GERMAN) ,glT
SKEAT: (YEAST) 728 GIEST — (OLD ENGLISH) oS 3S!
Foe : ieboby YEAST ENGLISH) gutS3h
> leetloal
: wpb ni ay} SUN; 029) glisal a He GHOL) F293 oll
KIUWAN JUDAN, JOYITAN — :(PAHLAVI) 5 4
KAUEN GERMAN) gilt JUTIN, JON, JOIN (KURDISH) 52,5
CBOWAN (OLD ENGLISH) pS pK! ‘ZHIYAG (BALUCHI) gs
CHEW HENGLISH) goulSs AFGHAN) (54) gilts!
KAUWEN (DUTCH) «sicla ZHOVAL, ZHOYAL
(OLD CHURCH SLAVIC) pS g3%=i + ZWATSI :(TOKHARIAN A) A ($55
ZHIVATI, ZHUJU ZWATSI, SWA.:(TOKHARIAN B) B 3 \%5
ZHUCIA POLISH) long) KIV, KVENI ARMENIAN) gs,
ZHIVAT, ZHUJU (RUSSIAN) ys) GINGIVA LATIN) 53
7AUI CZECH) Soy (OLD SCANDINAVIAN) 4S $-th-5\
ZHONA (BULGARIAN) «5 )\ih, TYGGVA
ZHUVAT (SLOVAK) 5 shal TYGGVA OLD NORSE) oS 393
‘ZHIAUNOS (LITHUANIAN) gl 3 ZIAKE, KESE:(OLD FRISIAN) oS 623
‘ZHAUNAS (LATVIAN) (3) 5.93 (OLD HIGH GERMAN) 7S galt
a
[pdf page 216]
|
ONIONS: (CHEW) 168 REFERENCES otha
SKEAT: (CHEW) 106 “Poxoryy = SOSO*~*~S~«S
AMINDAROV: (CHEW) 199 BARNHART: (CHEW) 164
opr igbG oly DELAMARRE: (MACHER) 256
MACKENZIE: (CHEW) 106
leatloah
AD SY Oj 22 05s onl ee
a Folia AS SAA 2319 oth ee
PRYD AGAULISH) Jf CHARA AVESTAN) posi
PRED XABRETON) 3.2 KARTA- (OLD PERSIAN) jl gj
CHAR, CHARAK, — (PAHLAVI) S shy
‘REFERENCES ethey CHARAG, CHARAGGARIH |
POKORNY, = SSS*S*~*~*~«SOS CHARE NRURDISH) 526
--- page tag
6199:[pdf page 215]
6231:[pdf page 216]

#### GOAT block
SKEAT: (BORE) 68, (BHER) 752. «POKORNY; = SSs=S~S~S~«w
AMINDAROV: * . 208 BARNHART: (BORE) 107-108
Se Nee , . iu day MACKENZIE: (CUT) 109
. BUCK: (CUT) 556, (BORE) 592
leatlaal
02S gob} Maj ee 2 Sale 9 JU) gal om
a gph 602 S Gla Fogg) GUL; 22 05s cal om
op hin O45 22 3a nl ow
BOCK (SWEDISH) 5 yo BUZA AAVESTAN) gl) —
BUK NORWEGIAN) 5533 Buc PAHLAVI) 5345,
BOK (DUTCH) g4che BIZIN KURDISH) 53,5
BOCC HOLD IRISH) 5543 p! WEZA AFGHAN] (3-4) g3\
BWCH WELSH) 59 BUC, BUZ ARMENIAN) 5,
BOC AGABLIC) SIE BUCCA LATIN) 3
BOUCH HBRETON) 6p Bouc HPRENCH) sili
BECCO (SPANISH) g\ ile!
REFERENCES Ucathany (OLD SCANDINAVIAN) i655 hes!
POKORNY: 114 BUKKR
BARNHART: (BUCK) 122 BUKKR (OLD NORSE) pS es5
DELAMARRE: 132 BOCK HOLD SAXON) pS gi pS
‘MACKENZIE: (Goat) 116 OLD HIGH GERMAN) pS galt
BUCK: 164-166 BOC, BUKKA
ONIONS: (BUCK) 122-123 BOCK GERMAN) glST
SKEAT: (BUCK) 77 BUC, HOLD ENGLISH) pS 51531
AMINDAROY: (GOAT) 231 BUCCA
MALLORY & ADAMS: BHUGOS BUCK ENGLISH) 153)
rvi-rvr road Olay BUK DANISH) 5 jila
[pdf page 128]
ee
| ; ,
4 | Sy nee, ws
oO vo
|
WACAN, (OLD ENGLISH) oS lS} VAZRA AVESTAN) glee!
WECCAN VAZRAKA, :(OLD PERSIAN) oles p+,
WAKE ENGLISH) SS} VAZARKA
--- page tag
3612:[pdf page 127]
3642:[pdf page 128]
```


## [2026-09-05T21:04:43.888Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D9%88%DB%8C%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B3%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D5%B1%D5%A1%D5%A3' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%C7%B5ews-' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/gaits' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/kewwan%C4%85' \\\n 'https://www.etymonline.com/word/goat' \\\n 'https://www.etymonline.com/word/chew' \\\n 'https://www.etymonline.com/word/disgust' \\\n 'https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82/' \\\n 'https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82%D8%AF%D8%A7%D9%86/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 178 (book 148): roots Geu 3/Gyeu (chew), Geus (dost/choose/disgust), Ghaido (goat/zaq/jag)' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T21:04:51.631Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cc8ab56b95544de7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/539e975dfded6456.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b0377d6a0a2fd9da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5b2cdae806e05a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0fff70bd7669475a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/466ba0f00b454c73.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d19a71a0992bd653.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7e2dd41255b7b9ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e2b9ccc8380d955.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/52873b75152be610.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9d6858c8cfcc040c.txt
```


## [2026-09-05T21:04:56.317Z] TOOL CALL #84: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg178.png data/verification/sources/refs/ocr/BOOK/178.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -5 && sed -n '1,60p' tools/verify_check.py",
 "description": "Copy page PNG and read verify_check"
}
```


### [2026-09-05T21:04:56.421Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
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
```


## [2026-09-05T21:04:58.530Z] TOOL CALL #85: Bash

```json
{
 "command": "sed -n '60,140p' tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-05T21:04:58.574Z] TOOL RESULT

```
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


## [2026-09-05T21:06:05.860Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,pat,off in [('PHD.txt','dōst [dwst\\'',21),('PHD.txt','Jūdan, jōy-',21),('NYB_vol2_glossary.txt','döst [dwst\\'',8),('HUB.txt','javidan *kauen',10),('SKT.txt','Chew,   Chaw',20),('KLN_1966.txt','goat,  n.  —  ME.  goot',12)]:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    leaves=t.split('\\f')\n    for i,l in enumerate(leaves):\n        if pat in l:\n            print(f, pat[:20], '-> leaf(0based)', i, 'printed ~', i-off if off!=12 else (i-12)*2)\n            break\n    else:\n        print(f, pat[:20], 'NOT FOUND')\nEOF",
 "description": "Compute printed pages for local refs"
}
```


### [2026-09-05T21:06:07.756Z] TOOL RESULT

```
PHD.txt dōst [dwst' NOT FOUND
PHD.txt Jūdan, jōy- NOT FOUND
NYB_vol2_glossary.txt döst [dwst' -> leaf(0based) 76 printed ~ 68
HUB.txt javidan *kauen -> leaf(0based) 239 printed ~ 229
SKT.txt Chew,   Chaw -> leaf(0based) 99 printed ~ 79
KLN_1966.txt goat,  n.  —  ME.  g -> leaf(0based) 360 printed ~ 696
```


## [2026-09-05T21:06:21.630Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor pat in ['dwst','ywtn','chew judan']:\n    for i,l in enumerate(leaves):\n        if pat in l:\n            print(pat,'-> leaf',i,'printed',i-21)\n            break\n    else: print(pat,'not found')\nprint('total leaves',len(leaves))\nEOF",
 "description": "PHD leaf lookup"
}
```


### [2026-09-05T21:06:23.433Z] TOOL RESULT

```
dwst -> leaf 48 printed 27
ywtn -> leaf 71 printed 50
chew judan not found
total leaves 259
```


## [2026-09-05T21:06:33.385Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\ndef find(pat):\n    for i,l in enumerate(leaves):\n        if pat in l:\n            nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', l)\n            return i,nums\n    return None,None\nfor pat in ['choose,  tr.  and  intr.  v.','gust,  n.,  relish','disgust,  tr.  v.','goat,  n.  —  ME.  goot','chew,  tr.  and  intr.  v.']:\n    print(pat[:22], find(pat))\nEOF",
 "description": "Klein page numbers"
}
```


### [2026-09-05T21:06:35.089Z] TOOL RESULT

```
choose,  tr.  and  int (159, ['282', '283'])
gust,  n.,  relish (371, ['688', '689'])
disgust,  tr.  v. (251, [])
goat,  n.  —  ME.  goo (360, ['666', '667'])
chew,  tr.  and  intr. (155, ['275'])
```


## [2026-09-05T21:07:31.192Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:15:06.360Z] TOOL CALL #89: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk178.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 178,\n \"book_page\": 148,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Geu 3, Gyeu, Gieu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵyewh₁- (Pokorny gi̯eu-, gi̯eu̯-) 'to chew'\",\n   \"note\": \"Pokorny IEW 400 heads the entry 'g(i̯)eu-, g(i̯)eu̯- „kauen“' and the very first witness he prints is the Iranian one: 'Npers. javīdan „kauen“, afgh. zōvəl, zoyal ds. „beißen, nagen“ (Iran. *jyav-)'. Walde-Pokorny I 642 has the same lemma with the same opening line. Watkins/AHD: 'gyeu-. Also geu-. To chew. Germanic *kewwan in Old English cēowan, to chew: CHEW. [Pok. g(i)eu- 400.]' Root name, language label and gloss are therefore all correct, and the whole chart (Iranian verb + Germanic verb) is Pokorny's own entry in miniature. The one defect is the language label of node 1: 'jutan' is not Old Persian but the Book-Pahlavi spelling ywtn' of Middle Persian jūdan, which Nourai took over from Horn §415 ('phlv. vergl. jūtan').\",\n   \"note_fa\": \"ریشهٔ نمودار همان ریشهٔ هندواروپایی آغازین *ǵyewh₁- «جویدن» است که پوکورنی در صفحهٔ ۴۰۰ به صورت g(i̯)eu- «kauen» آورده و نخستین گواهی که برای آن می‌آورد خودِ «جویدن» فارسی است: «npers. javīdan، افغانی (پشتو) žōvəl». والده‑پوکورنی (جلد ۱، ص ۶۴۲) و واتکینز در پیوستِ AHD نیز همین ریشه و همین معنا را دارند. پس نام ریشه، برچسب زبان و معنای آن هر سه درست است و ادعای نورایی در حدِ جعبهٔ ریشه پذیرفتنی است. تنها لغزش نمودار در برچسب زبانِ گرهٔ نخست است: jutan صورتِ پارسی باستان نیست، بلکه املای پهلوی کتابی ywtn' برای فارسی میانهٔ jūdan است که نورایی آن را از هرن (بند ۴۱۵: «phlv. jūtan») گرفته است.\",\n   \"sources\": [\n     W + \"Reconstruction:Proto-Germanic/kewwan%C4%85\",\n     \"https://www.etymonline.com/word/chew\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:400\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (grep -n 'Root / lemma: g(i)eu' → line 34195 region), IEW p.400: 'Root / lemma: g(i̯)eu-, g(i̯)eu̯- | Meaning: to chew | Material: Npers. javīdan „chew“, afgh. zovəl, zoyal ds., „bite, gnaw“ (Iran. *jyav-); Armenian kveni …; Old Icelandic tyggja … Old English ceowan, nengl. chew … Page(s): 400'. Exactly the root box as drawn.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 642 (WLD_Bd1 djvu line 40418)\", \"stance\": \"supports\",\n     \"note\": \"'gi̯eu- und gi̯eu̯- „kauen“. Npers. javīdan „kauen“, afgh. zovəl, zoyal „kauen, beißen, nagen“ (Hübschmann, Pers. Studien 49 f.) … ags. ceowan „beißen, kauen“, ahd. kiuwan …' — the source Pokorny 400 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 557)\", \"stance\": \"supports\",\n     \"note\": \"'gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(i)eu- 400.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. ǵieuō (IEC.txt line 4015)\", \"stance\": \"supports\",\n     \"note\": \"'ǵieuō, iō (gleuu-, giau-) „chew“. WP I, 642. Cf. ǵeus-' — Mann sets up the same verbal root and cross-refers it to ǵeus-, the root of Nourai's next chart.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *jiauH (CHEUNG.txt line 15160 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'*jiauH „to chew“ … «PIE *ǵieuH- „to chew, bite“ ⇒ LIV: 168 | Pok.: 400» … IE COGNATES: Toch. śu-, OCS žuju, OHG kewa, OE cēowan, Engl. to chew, Lith. žiáunos „jaws“.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"jutan\", \"verdict\": \"plausible\",\n     \"derivation\": \"The word is real but the language label is wrong: Old Persian has no attested verb 'to chew', and 'jutan' is the Book-Pahlavi (Middle Persian) form. MacKenzie, Concise Pahlavi Dictionary p.50: 'jūdan, jōy- [ywtn', ywd- | M jwwdn, (jw-), (N jāwīdan)] chew; devour (daevic)'; the heterographic-looking spelling ywtn' with -t- is what produced Nourai's 'jutan', by way of Horn, Grundriss §415 (p.93), which prints 'phlv. vergl. jūtan „kauen, verzehren“ (West: jaūdanō), jūyend (Vd. 17)'. Horn is Nourai's ultimate source here and Horn labels it phlv. = Pahlavi. The descent itself is sound and regular: PIE *ǵyewh₁- > Proto-Iranian *jiauH- (initial *ǵi̯- > Ir. *ǰ-, Rasmussen 1989: 114) > Manichaean MP jw-, Book MP ywd- /jōy-/, infinitive jūdan. Aryanpur's Persian IE-roots dictionary (printed p.216 f.) likewise files JUDAN, JOYITAN under '(PAHLAVI)'. Verdict: the derivation root → this verb is correct, the label 'Old Persian' is not.\",\n     \"derivation_fa\": \"این صورت واقعی است اما برچسب زبانش نادرست: در پارسی باستان هیچ فعلی به معنای «جویدن» بازمانده نیست و jutan در حقیقت صورت فارسی میانه (پهلوی) است. مکنزی در فرهنگ کوچک پهلوی (ص ۵۰) می‌آورد: jūdan, jōy- [ywtn', ywd-] «جویدن؛ (در کاربرد دیوی) بلعیدن»، و همان املای پهلوی کتابیِ ywtn' با «ت» است که به دستِ هرن (بند ۴۱۵) به شکل «phlv. jūtan» درآمده و نورایی آن را از هرن گرفته و به اشتباه «پارسی باستان» برچسب زده است. سیر تحول خودش بی‌عیب است: هندواروپایی *ǵyewh₁- ← ایرانی آغازین *jiauH- (که در آن *ǵi̯- آغازین به ǰ ایرانی بدل شده) ← فارسی میانهٔ jūdan / ستاک حال jōy-. آریان‌پور نیز (ص ۲۱۶) JUDAN را زیر «پهلوی» آورده است. حکم: پیوند ریشه به این فعل درست است، ولی برچسب «پارسی باستان» خطای کتاب است.\",\n     \"sources\": [W + \"%D8%AC%D9%88%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:400\", \"status\": \"partial\",\n       \"note\": \"IEW p.400 does list the Iranian branch, but as 'Npers. javīdan' plus 'afgh. zovəl, zoyal (Iran. *jyav-)' — it gives no Old Persian and no Pahlavi form at all, so the page supports the root→Iranian link but not the label 'Old Persian jutan'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 50 s.v. jūdan (PHD.txt leaf 71)\", \"stance\": \"partial\",\n       \"note\": \"'Jūdan, jōy- [ywtn', ywd- | M jwwdn, (jw-), (N jāwīdan)] chew; devour (daevic). ~išn: eating (daevic).' — MacKenzie has the word, as Middle Persian, not Old Persian.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 415, p. 93 (HRN.txt leaf 115)\", \"stance\": \"partial\",\n       \"note\": \"'415. jāvīden „kauen“, zāvīden, g. jovadmūn, phlv. vergl. jūtan „kauen, verzehren“ (West: jaūdanō), jūyend (Vd. 17 (9))' — the printed source of Nourai's 'jutan', explicitly labelled phlv. (Pahlavi).\"},\n      {\"src\": \"KNT\", \"where\": \"Lexicon, d-/j- entries pp. 189-192\", \"stance\": \"silent\",\n       \"note\": \"Kent's Old Persian lexicon (grep 'chew', 'jav', 'jut' in KNT.txt) has no verb for 'chew' — confirming that no Old Persian form of this verb is attested.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *jiauH (CHEUNG.txt line 15162)\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: MMP jw- „to chew“, BMP ywd- /jōy-/ „to chew; devour (daevic)“ = DMMPP: 199 … Partic. perf. pass. MMP jwwd, BMP ywt /jūd/' — the Middle Persian participle is literally spelled ywt.\"},\n      {\"src\": \"ARY\", \"where\": \"printed p. 216 f. (ARY_latin_index_pages.txt line 6219, pdf page 215-216)\", \"stance\": \"partial\",\n       \"note\": \"Aryanpur's cognate list under CHEW gives 'JUDAN, JOYITAN :(PAHLAVI)', 'ZHOVAL, ZHOYAL (AFGHAN)', 'KIV, KVENI (ARMENIAN)', 'CEOWAN (OLD ENGLISH) → CHEW (ENGLISH)' — same chain, again with the verb assigned to Pahlavi.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"javîdan «جویدن»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP جویدن javīdan 'to chew' continues MP jūdan directly. The Middle Persian present stem jōy-/jaw- was re-characterised in New Persian with the productive infinitive suffix -īdan, giving jav-īdan beside older jāv-īdan; MacKenzie already registers 'N jāwīdan' as the New Persian outcome of MP jūdan. Klein, s.v. chew (pp. 274-275, the pages Nourai cites), lists 'Pers. javidan, „to chew“' among the cognates of OE cēowan, and Pokorny 400 / Walde-Pokorny I 642 both open the root with 'Npers. javīdan'. The two extra spellings in the box are genuine variants and not misprints: جاویدن jāvīdan is the older infinitive with unshortened ā (Horn's headword is jāvīden), and جاییدن jāyīdan preserves the -y- stem also seen in Baluchi jāyag, Kurdish jūn/jūtin, Pashto žōwəl (Cheung s.v. *jiauH). Chain: PIE *ǵyewh₁- > PIr. *jiauH- > MP jūdan/jōy- > NP jāvīdan ~ javīdan.\",\n     \"derivation_fa\": \"«جویدن» فارسی نو دنبالهٔ مستقیم فارسی میانهٔ jūdan است: ستاک حالِ فارسی میانه jōy-/jaw- در فارسی نو با پسوند مصدرسازِ پرکاربردِ ‑یدن بازساخته شده و jav-īdan را کنار صورت کهن‌ترِ jāv-īdan پدید آورده است؛ مکنزی خود «N jāwīdan» را بازماندهٔ jūdan می‌داند. کلاین در مدخل chew (ص ۲۷۴–۲۷۵، همان صفحه‌ای که نورایی ارجاع داده) «Pers. javidan» را در شمار هم‌ریشه‌های ceowan انگلیسی کهن آورده، و پوکورنی (ص ۴۰۰) و والده‑پوکورنی (۱: ۶۴۲) هر دو مدخل ریشه را با «npers. javīdan» می‌گشایند. دو صورتِ افزودهٔ جعبه هم واقعی‌اند و خطای چاپی نیستند: «جاویدن» مصدر کهن‌تر با «آ»ی کشیده است (سرمدخلِ هرن نیز jāvīden است) و «جاییدن» ستاکِ ‑ی‑ را نگاه داشته که در بلوچی jāyag، کردی jūn/jūtin و پشتوی žōwəl نیز دیده می‌شود (چونگ، مدخل *jiauH). زنجیره: *ǵyewh₁- ← *jiauH- ← jūdan ← جویدن. ادعای نورایی درست است.\",\n     \"sources\": [\n       W + \"%D8%AC%D9%88%DB%8C%D8%AF%D9%86\",\n       W + \"Reconstruction:Proto-Germanic/kewwan%C4%85\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:275\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 155-156 (page markers '272' … '275' on the leaves), s.v. chew: 'ME. chewen, fr. OE. ceowan, rel. to MLG. keuwen, Du. kauwen, OHG. kiuwan … and cogn. with OSlav. živǫ, živati, „to chew“, Lith. žiaunos …, Pers. javidan, „to chew“, Toch. swa, „to eat“.' The entry straddles pp. 274-275, so Nourai's KLN:275 for javīdan and KLN:274 for chew are both right.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 415, p. 93 (HRN.txt leaf 115)\", \"stance\": \"supports\",\n       \"note\": \"'415. jāvīden „kauen“, zāvīden … kurd. jūn „kauen“; afγ. žōvul, zōyal; bel. jāyag, n. jāy (176). Bartholomae meint …, dass np. jāvīden aus ar. gžhau-, altir. jiaw-, einer u̯-Bildung … stammen könne.' Horn's headword is the ā-form, exactly Nourai's variant جاویدن.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §120 (p. 229), referring back to pp. 49-50 (HUB.txt line 8165)\", \"stance\": \"supports\",\n       \"note\": \"'javidan „kauen“, afgh. žōvəl, ksl. živati (Wrzl. iran. jyu, oben p. 49-50 und § 11)' — listed among the words showing ap. j (= idg. *ǵ, *ǵʰ) > np. j.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *jiauH, NWIR section (CHEUNG.txt line 15178)\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP javīdan/jav-, Bal. jaθ-/ja-, Kurd. (Kurm.) jūn, jūtin/jū-, (Sor.) jūn/jū-, jawīn/jaw-, Zaz. jawitiš/jawen-, … Tal. jūye „to chew“.'\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in / Dehkhoda s.v. جویدن (vajehyab, abadis)\", \"stance\": \"silent\",\n       \"note\": \"the local 2-vol abridgement (MON_part1/2) has no separate جویدن headword with an etymological tag; nothing that contradicts the chart.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"kewwan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *kewwaną 'to chew' is the regular Germanic reflex of PIE *ǵyewh₁-: the PIE palatal *ǵ appears in the centum branches simply as *g, which Grimm's Law shifts to Germanic *k-, while the root-final laryngeal plus the *-w- of the root gives the geminate -ww- of this strong class-2 verb. Watkins/AHD prints Nourai's form verbatim: 'gyeu-. Also geu-. To chew. Germanic *kewwan in Old English cēowan, to chew: CHEW.' Descendants: OE cēowan, OHG kiuwan (> G. kauen), MHG kiuwen, MLG keuwen, Du. kauwen, and ON tyggva/tyggja, whose t- is a dissimilation of the palatalised *k before -ggw-. The chart's arrow root → Germanic is exactly the handbook one.\",\n     \"derivation_fa\": \"*kewwaną ژرمنیِ آغازین «جویدن» بازتاب قاعده‌مندِ *ǵyewh₁- هندواروپایی است: کامیِ *ǵ در شاخه‌های کنتوم به g ساده بدل می‌شود و قانون گریم آن را به k ژرمنی می‌رساند، و حنجریِ پایانِ ریشه به‌همراه *‑w‑ همان ‑ww‑ مشدّدِ این فعل قویِ ردهٔ دوم را می‌سازد. واتکینز در پیوستِ AHD دقیقاً همین صورت را چاپ کرده است: «Germanic *kewwan in Old English cēowan: CHEW». بازماندگان: ceowan انگلیسی کهن، kiuwan آلمانی علیای کهن (← kauen آلمانی)، keuwen ساکسون سفلای میانه، kauwen هلندی و tyggva نُرسی کهن که «ت» آغازینش از ناهمگونیِ k کامی‌شده پیش از ‑ggw‑ پدید آمده. پیکانِ ریشه ← ژرمنی همان چیزی است که در فرهنگ‌های مرجع می‌آید؛ ادعای نورایی درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Germanic/kewwan%C4%85\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 557: 'gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(i)eu- 400.]' — Nourai's Germanic form and gloss come straight from this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 642 (WLD_Bd1 djvu line 40426 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'Aisl. tyggva „kauen, verspeisen“ (nach Pedersen KZ. 32, 255 mit Dissimilation des durch i palatalisierten k vor gg) … ags. ceowan „beißen, kauen“, ahd. kiuwan „kauen, beißen, verzehren“ …'\"},\n      {\"src\": \"KLN\", \"where\": \"p. 274 f. s.v. chew (KLN_1966.txt leaf 155-156)\", \"stance\": \"supports\",\n       \"note\": \"'rel. to MLG. keuwen, Du. kauwen, OHG. kiuwan, MHG. kiuwen, MG. küwen, „to chew“ (whence G. kauen)'.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 400 (POK_full.txt s.v. g(i̯)eu-)\", \"stance\": \"supports\",\n       \"note\": \"'Middle Low German keuwen, Old High German kiuwan, Middle High German kuwen „chew“ (*kewian)'.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"chew\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE cēowan > ME chewen > NE chew; the ModE ch- is the regular palatalisation of Old English initial c- before a front vowel, and the -w- of the stem survives in the spelling. Klein pp. 274-275: 'chew, tr. and intr. v. — ME. chewen, fr. OE. cēowan …'. Etymonline gives the same chain (OE ceowan < West Germanic *keuwwan < PIE *gyeu- 'to chew') and, like Klein, lists Persian javidan among the cognates — so the whole left-to-right chart, Persian and English hanging off one PIE root, is the standard account. Uncontroversial.\",\n     \"derivation_fa\": \"chew انگلیسی از ceowan انگلیسی کهن ← chewen انگلیسی میانه می‌آید؛ «چ» امروزی همان کام‌شدگیِ قاعده‌مندِ c آغازینِ انگلیسی کهن پیش از واکهٔ پیشین است و ‑w‑ ستاک در املا مانده است. کلاین (ص ۲۷۴–۲۷۵): «chew — ME. chewen, fr. OE. ceowan». اتیمانلاین نیز همین زنجیره را می‌دهد (ceowan ← ژرمنی باختری *keuwwan ← هندواروپایی *gyeu-) و مانند کلاین «javidan» فارسی را در شمار هم‌ریشه‌ها می‌آورد؛ بنابراین کلِ نمودار، یعنی قرار گرفتنِ «جویدن» و chew زیر یک ریشه، همان روایتِ پذیرفتهٔ امروزی است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/chew\", W + \"Reconstruction:Proto-Germanic/kewwan%C4%85\"],\n     \"ref_check\": [\n      {\"ref\": \"KLN:274\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 155-156 (printed page markers 272 … 275 in the OCR of those leaves), s.v. chew: 'ME. chewen, fr. OE. ceowan …'; the entry begins on p. 274 and runs onto p. 275.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., s.v. 'Chew, Chaw' (SKT.txt line 3372)\", \"stance\": \"supports\",\n       \"note\": \"'Chew, Chaw. (E.) M.E. chewen. A.S. cēowan, to chew. + Du. kauwen, G. kauen; Russ. jevate. Der. [chaw >] jaw; now spelt jaw.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 1349)\", \"stance\": \"supports\",\n       \"note\": \"'CHEW gyeu-' in the index of English words to IE roots.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Geus\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *ǵews- 'to taste, enjoy'; in Germanic and Celtic 'to choose', in Indo-Iranian and Albanian 'to love'\",\n   \"note\": \"Pokorny IEW 399-400: 'ĝeus- „kosten, genießen, schmecken“, im Germ. und Kelt. auch über „mit dem Geschmack prüfen“ zu „wählen“ entwickelt, in Indo-Iran. und Alban. „lieben“'. Nourai's gloss 'to love, favor, choose' renders the Indo-Iranian and Germanic ends of that range but drops the base sense 'to taste', which is what actually holds the Latin box (gustus) together with the rest; that is a compression, not an error. Everything else on the chart is textbook: Kent's Old Persian lexicon s.v. dauštar- (p.189, the page Nourai cites) itself strings together 'NPers. dōst, Skt. joṣṭar-; agent-noun to root dauš-, Av. zaoš- „enjoy“, Skt. juṣ-, Lat. gustat „tastes“, NEng. choose, pIE *ǵeus-' — i.e. Nourai's four branches in one sentence. The only label slip is 'dis-goust' in the Latin box, which is Middle French desgoust, not Latin.\",\n   \"note_fa\": \"پوکورنی (ص ۳۹۹–۴۰۰) ریشه را چنین می‌آورد: ĝeus- «چشیدن، لذت بردن، مزه کردن»، که در ژرمنی و سلتی از راهِ «با چشیدن آزمودن» به معنای «برگزیدن» رسیده و در هندوایرانی و آلبانیایی به «دوست داشتن». معنایی که نورایی داده («دوست داشتن، پسندیدن، برگزیدن») دو سرِ این طیف را می‌گیرد ولی معنای پایه یعنی «چشیدن» را می‌اندازد؛ این فشرده‌سازی است نه خطا، هرچند پیوندِ جعبهٔ لاتینی (gustus) با بقیه را کم‌رنگ می‌کند. باقیِ نمودار کاملاً استاندارد است: کنت در واژه‌نامهٔ پارسی باستان، در همان صفحهٔ ۱۸۹ که نورایی ارجاع داده، خودش می‌نویسد «dauštar- „friend“: NPers. dōst … Av. zaoš- „enjoy“ … Lat. gustat „tastes“, NEng. choose, pIE *ǵeus-» — یعنی هر چهار شاخهٔ نورایی در یک جمله. تنها لغزش، «dis-goust» است که در جعبهٔ «لاتین» نشسته حال آنکه صورتِ فرانسهٔ میانه (desgoust) است.\",\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/%C7%B5ews-\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 35741 region: 'Root / lemma: ǵeus- | Meaning: to taste; to enjoy [„savor, enjoy, taste“, in the Germanic and Celtic „choose“, in Indo Iran. and Alban. „love“] | Material: … Avestan zaoš-, Old pers. dauš- … Gothic kiusan … Latin gustus … Page(s): 399-400.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 568 f. (WLD_Bd1 djvu line 35781)\", \"stance\": \"supports\",\n     \"note\": \"'ǵeus- „kosten, genießen, schmecken“, im Germ. und Kelt. auch über „mit dem Geschmack prüfen“ zu „wählen“ entwickelt. Ai. juṣati, juṣáte … av. zaoš-, ap. dauš- „Geschmack woran finden“, av. zaoša- „Gefallen“, zušta- „beliebt, erwünscht“ …'\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 501)\", \"stance\": \"supports\",\n     \"note\": \"'geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan … CHOOSE. b. Gothic *kausjan … CHOICE. … 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: GUST², GUSTO; DISGUST, RAGOUT. [Pok. ĝeus- 399.]' — all four of Nourai's branches except the Iranian one.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 19.51 'friend' (SYN.txt line 33714)\", \"stance\": \"supports\",\n     \"note\": \"'OPers. daustar- (NPers. dost) : Av. zuš-, Skt. juṣ- „take pleasure in, enjoy“, Av. zaoša- „pleasure“, Grk. γεύομαι „taste, enjoy“, etc. (15.31). Barth. 674 f.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *zauš (CHEUNG.txt line 30541)\", \"stance\": \"supports\",\n     \"note\": \"'*zauš „to take pleasure, rejoice in“ … © This root has an impeccable IE etymology. «PIE *ǵeus- „to taste, like, choose, be pleased“ — LIV: 166 | Pok.: 399 f.»'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"zaošô; zuštô; dauštar\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three forms are real, though the box mixes an Avestan pair with an Old Persian noun (as its double label allows). Av. zaoša- m. is 'pleasure, liking, will' (Bartholomae AiW: a-zaoša- 'Nichtwille, Nichtabsicht' Y.7.21; uγra.zaoša- 'of strong, unbending will' Yt.13.31; 'nach seinem Willen und Gefallen' V.2.11) — so Nourai's gloss 'to agree' is loose: the word is a noun 'pleasure/will', not a verb. Av. zušta- 'liked, beloved, welcome' is the past participle of the same zaoš-. OP dauštar- 'friend' is attested only in the nom. sg. dauštā (DB 4.56, 69, 74; DNb 7, 8, 12; DSj 4). The two initials are the two regular Iranian reflexes of the PIE palatal *ǵ: PIE *ǵ > PIIr. *ȷ́ > Proto-Iranian *dz, which Avestan simplifies to z- but Old Persian resolves to d- — the same split as Av. zasta- : OP dasta- 'hand' and Av. zaranya- : OP daraniya- 'gold'. dauštar- itself is the agent noun *ǵews-tōr- 'one who takes pleasure (in someone)' > 'friend'.\",\n     \"derivation_fa\": \"هر سه صورت واقعی‌اند، هرچند جعبه یک جفت اوستایی را با یک نامِ پارسی باستان کنار هم نشانده (که برچسب دوگانه‌اش همین را اجازه می‌دهد). zaoša- اوستایی «خشنودی، کام، خواست» است — بارتولمه a-zaoša- «ناخواست، بی‌قصدی» و uγra.zaoša- «سخت‌اراده» را می‌آورد و در وندیداد ۲٫۱۱ «به خواست و کامِ خویش» — پس معنایی که نورایی داده («to agree») سست است: این واژه اسم است نه فعل. zušta- صفت مفعولیِ همان ستاکِ zaoš- است به معنای «پسندیده، دوست‌داشته». dauštar- «دوست» تنها در فاعلیِ مفرد dauštā در سنگ‌نبشته‌های بیستون و نقش رستم آمده است. دو آغازِ z و d دو بازتابِ قاعده‌مندِ کامیِ *ǵ هندواروپایی‌اند: *ǵ ← هندوایرانیِ *ȷ́ ← ایرانیِ آغازینِ *dz، که در اوستایی به z ساده و در پارسی باستان به d بدل می‌شود؛ درست همان جفتِ zasta- اوستایی در برابر dasta- پارسی باستان («دست») و zaranya- در برابر daraniya- («زر»). خودِ dauštar- اسم فاعلِ *ǵews-tōr- است: «آنکه از کسی خشنود می‌شود» ← «دوست». ادعای نورایی درست است، جز معنای سستِ zaošô.\",\n     \"sources\": [W + \"%D8%AF%D9%88%D8%B3%D8%AA\", W + \"Reconstruction:Proto-Indo-European/%C7%B5ews-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:399\", \"status\": \"supports\",\n       \"note\": \"IEW 399 f. (POK_full.txt line 35695): 'Avestan zaoš-, Old pers. dauš- „where one finds flavor“, Avestan zaoša- „pleasure“, zušta- „liked, beloved, fancied, desirable, welcome“' — all three of Nourai's words on the cited page.\"},\n      {\"ref\": \"KNT:189\", \"status\": \"supports\",\n       \"note\": \"KNT.txt leaf 213 (leaf 212 ends '188', leaf 214 shows '190 OLD PERSIAN', so leaf 213 = printed p.189): 'dauštar- sb. „friend“: NPers. dōst, Skt. joṣṭar- „loving“; agent-noun (§154.II) to root dauš-, Av. zaoš- „enjoy“, Skt. juṣ-, Lt. gustat „tastes“, NEng. choose, pIE *ǵeus- (§88). daustā nsm. DB 4.56, 69, 74; DNb 7, 8, 12; DSj 4.' Exactly the arrow drawn.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW s.vv. a-zaoša-, uγra.zaoša-, zaoša- (BRT.txt lines 5976, 8120; cf. Buck's citation 'Barth. 674 f.')\", \"stance\": \"partial\",\n       \"note\": \"'j. a-zaoša- m. „Nichtwille, Nichtabsicht“: yezi zaoša yezi ažaoša „sei es absichtlich, sei es unabsichtlich“ Y.7.21'; 'j. uγra.zaoša- Adj. „starken sva. unbeugsamen Willens gegenüber —“ Yt.13.31'; 'hvąm anu ušim zaošəmca yaθa hē zaošō „nach seinem Willen und Gefallen, wie immer sein Gefallen war“ V.2.11'. Bartholomae's zaoša- is 'Wille, Gefallen', which is why Nourai's gloss 'to agree' is only approximate.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 19.51 (SYN.txt line 33714)\", \"stance\": \"supports\",\n       \"note\": \"'OPers. daustar- (NPers. dost) : Av. zuš-, Skt. juṣ- …, Av. zaoša- „pleasure“, Grk. γεύομαι „taste, enjoy“ … Barth. 674 f.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *zauš (CHEUNG.txt line 30545 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*AVESTAN: YAv. zuš- „to take pleasure, rejoice in“ … Partic. perf. pass. YAv. zušta- (F 620, F 764, VdPZ 17.8); *OLD PERSIAN: dauštā (Nsg.) „friend“ <d-u-š-t-a> (DB 4.56, DB 4.69, DB 4.74).'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 568 (WLD_Bd1 djvu line 35786)\", \"stance\": \"supports\",\n       \"note\": \"'av. zaoš-, ap. dauš- „Geschmack woran finden“, av. zaoša- „Gefallen“, zušta- „beliebt, erwünscht“'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"dŭst «دوست»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP دوست dōst 'friend' < MP dōst [dwst'] < OP dauštā, nom. sg. of dauštar-. Nyberg's Pahlavi glossary (Part II, p.68) states the whole chain: 'dōst [dwst'] … 2. subst. friend … < *dauštā, nom. sg. of OP dauštar-; MPrs dwst (S); Paz. NP dōst; SW forms from Av. (1656) zaoš- „to enjoy“'; MacKenzie p.27: 'dōst [dwst' | = M, N ~] friend. ~īh: friendship, love.' Phonetically: the Old Persian diphthong au is monophthongised to ō in Middle Persian, the cluster -št- is simplified to -st-, and the nominative ending is lost; New Persian keeps dōst unchanged and writes it دوست with the historical wāw (later pronounced dūst). The initial d- rather than z- shows that the word is a genuine south-western (Persid) inheritance, not a borrowing from a Median or Avestan dialect. Horn's no. 582, on the very page Nourai cites, gives 'ap. daustar- „Freund“; aw. vergl. zaoša- „Wunsch“; phlv. dōst, dōstīh'.\",\n     \"derivation_fa\": \"«دوست» فارسی نو از فارسی میانهٔ dōst (املای پهلوی dwst') می‌آید و آن از dauštā، فاعلیِ مفردِ dauštar- پارسی باستان. نیبرگ در واژه‌نامهٔ پهلوی (بخش دوم، ص ۶۸) همهٔ زنجیره را می‌آورد: «dōst … از *dauštā، فاعلیِ مفردِ dauštar- پارسی باستان؛ صورت‌های جنوب‌غربی از ستاکِ اوستاییِ zaoš- „خشنود شدن“»؛ مکنزی نیز (ص ۲۷): «dōst [dwst'] دوست؛ dōstīh دوستی». از نظر آوایی: مصوّت مرکّبِ au در پارسی باستان در فارسی میانه به ō تک‌آوا شده، خوشهٔ ‑št‑ به ‑st‑ ساده شده و پایانهٔ فاعلی افتاده است؛ فارسی نو همان dōst را نگاه داشته و آن را با «واو» تاریخی می‌نویسد (تلفظ متأخرِ dūst). حضورِ «د» به‌جای «ز» در آغاز نشان می‌دهد که واژه میراثِ اصیلِ گویشِ جنوب‌غربی (پارسی) است نه وام از مادی یا اوستایی. هرن در بند ۵۸۲، در همان صفحهٔ ۱۳۰ که نورایی ارجاع داده، می‌نویسد: «ap. daustar- „Freund“؛ aw. zaoša- „Wunsch“؛ phlv. dōst, dōstīh». ادعای نورایی درست است.\",\n     \"sources\": [W + \"%D8%AF%D9%88%D8%B3%D8%AA\"],\n     \"ref_check\": [\n      {\"ref\": \"HRN:130\", \"status\": \"supports\",\n       \"note\": \"HRN.txt leaf 152 opens with the running page number '- 130 -' and carries entry 582: 'dōst „Freund“, dōstār, dōstī. ap. daustar- „Freund“; aw. vergl. zaoša- „Wunsch“; phlv. dōst, dōstīh, vergl. dōs(i)st, dōšak; ai. vergl. joṣa-. … np. dōst ist allgemein entlehnt.' Exactly the arrow drawn.\"},\n      {\"ref\": \"BQT:897\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 357 (= printed 897 on the vol-2 offset printed = leaf + 540, which puts leaf 0 at ~p.540 and the last leaf at ~p.1223, matching the recorded range for vol 2) carries the headword 'دوست = بروزن پوست، بمعنی محب و بکدل و بک رنگ' with Mo'in's footnote 1: 'پهلوی dōst … از *dauštar، از پارسی باستان dauštar-، «بارتولمه ۶۹۰…»، «اسشق ۲۸۵»، ورک: هوبشمان'. Mo'in's note is precisely Nourai's derivation.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 27 s.v. dōst (PHD.txt leaf 48)\", \"stance\": \"supports\",\n       \"note\": \"'dōst [dwst' | = M, N ~] friend. ~īh: friendship, love.' — the Middle Persian link of the chain, with the Manichaean and New Persian forms identical.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (Glossary) p. 68 s.v. dōst (NYB_vol2_glossary.txt line 1318)\", \"stance\": \"supports\",\n       \"note\": \"'dōst [dwst'] 1. adj. kind, friendly …; 2. subst. friend … — < *dauštā, nom. sg. of OP daustar-; MPrs dwst (S); Paz. NP dōst; SW forms from Av. (1656) zaoš- „to enjoy“; cf. dōšaram.'\"},\n      {\"src\": \"CHEUNG\", \"where\": \"s.v. *zauš, MP and NWIR sections (CHEUNG.txt line 30549 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'*MIDDLE PERSIAN: BMP dwš- /dōš-/ „to love, like, choose ?“, MMP dwst, BMP dwst /dōst/ „loving; friend“ … *NWIR: NP dōst „friend“ (also dōst dāštan „to love“).'\"},\n      {\"src\": \"ARY\", \"where\": \"printed p. ~288 (ARY_latin_index_pages.txt line 8285, pdf page 287)\", \"stance\": \"supports\",\n       \"note\": \"Aryanpur's cognate table gives 'ZAOSH, ZAOSHO, ZUSHTO :(AVESTAN)', 'DAUSHTAR, DAUSH- :(OLD PERSIAN)', 'DOST :(PAHLAVI)', 'DOST, DAUSHTA, DOSHIDAN', beside Gothic KAUSJAN/KIUSAN, OE CEOSAN → CHOOSE and Latin DEGUNO, GUSTUS — an independent modern Persian source reproducing Nourai's whole chart.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"kiusan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gothic kiusan / Proto-Germanic *keusaną 'to test, choose' is the regular Germanic reflex of PIE *ǵews-: centum *g- > Grimm *k-, e-grade *ǵews- > *keus-. The semantic step is the one Pokorny describes for Germanic and Celtic, 'to judge by tasting' > 'to choose'. Watkins/AHD: 'geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, ceosan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE.' The causative-iterative Goth. kausjan 'to test, taste' (= Skt. joṣayate) shows the o-grade of the same root, and the zero-grade *gus- gives Goth. kustus, OHG kust 'test, choice'. Nourai's spelling kiusan is the Gothic form rather than a reconstructed Proto-Germanic one, but that is the shape Pokorny and Walde-Pokorny print too.\",\n     \"derivation_fa\": \"kiusan گوتی (ژرمنی آغازین *keusaną) «آزمودن، برگزیدن» بازتاب قاعده‌مندِ *ǵews- هندواروپایی است: *ǵ کامی در شاخهٔ کنتوم به g و سپس با قانون گریم به k بدل می‌شود و درجهٔ e‑دارِ *ǵews- به *keus- می‌رسد. تحول معنایی همان است که پوکورنی برای ژرمنی و سلتی توصیف می‌کند: «با چشیدن سنجیدن» ← «برگزیدن». واتکینز: «geus-. To taste, choose. Germanic *keusan in Old English cēosan: CHOOSE؛ Gothic *kausjan: CHOICE». صورتِ سببیِ گوتیِ kausjan «آزمودن، چشیدن» درجهٔ o‑دارِ همین ریشه است و درجهٔ صفر *gus- به kustus گوتی و kust آلمانی علیای کهن «آزمون، گزینش» می‌رسد. آنچه نورایی نوشته صورت گوتی است نه بازسازیِ ژرمنی آغازین، اما پوکورنی و والده‑پوکورنی هم همین را چاپ کرده‌اند. ادعا درست است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/%C7%B5ews-\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 501: 'geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, cedsan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 399 f. (POK_full.txt line 35712)\", \"stance\": \"supports\",\n       \"note\": \"'Gothic kiusan „assay, try, test, check“, Old Norse kjósa „choose, wish“, Old High German Old Saxon kiosan „taste, assay, try, choose“, MHG kiesen, Kaus.-Iter. Gothic kausjan „assay, try, taste“ (= Old Indic joṣayate).'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 568 (WLD_Bd1 djvu line 35789)\", \"stance\": \"supports\",\n       \"note\": \"'got. kiusan „prüfen, erproben“, anord. kjósa „wählen, wünschen“, ahd. as. kiosan „schmecken, prüfen, wählen“, nhd. kiesen, küren.'\"},\n      {\"src\": \"KLN\", \"where\": \"p. 282 f. s.v. choose (KLN_1966.txt leaf 159, page markers 282/283)\", \"stance\": \"supports\",\n       \"note\": \"'rel. to OS., OHG. kiosan, ON. kjósa, OFris. kiasa, Du. kiezen, MHG., G. kiesen, Goth. kiusan, „to choose“ … fr. I.-E. base *geus-, *gus-, „to taste, enjoy by tasting“ … Avestic zaosh-, „to find delicious“.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"choose, choice\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Two different routes, both from the same Germanic root, which is why Nourai boxes them together. CHOOSE is inherited: OE cēosan > ME chesen/chusen > NE choose, with regular palatalisation of initial c- to ch- and levelling of the Verner alternation (OE past pl. curon, ptc. coren, whence the -s- of the modern verb was generalised). CHOICE is borrowed: Old French chois (noun to choisir 'to choose'), which is itself a Frankish/Gothic loan into Gallo-Romance from Germanic *kausjan; it entered Middle English in the 13th century as chois and was later re-spelled choice. Klein pp.282-283 s.v. choose: 'F. choisir, „to choose“, OProvenç. causir, „to look at“, OSlav. kusiti, „to taste, try“, are Goth. loan words. Cp. choice.' Watkins likewise files CHOOSE under Germanic *keusan and CHOICE under Gothic *kausjan. The node carries no citation of its own in the book, but the chain is uncontroversial.\",\n     \"derivation_fa\": \"دو راهِ متفاوت از یک ریشهٔ ژرمنی، و به همین سبب نورایی هر دو را در یک جعبه گذاشته است. choose میراثی است: cēosan انگلیسی کهن ← chesen/chusen انگلیسی میانه ← choose، با کام‌شدگیِ قاعده‌مندِ c آغازین به ch و یکدست‌شدنِ تناوبِ ورنر (گذشتهٔ جمعِ curon و صفت مفعولیِ coren، که سرانجام «س» بر همه چیره شد). اما choice وام‌واژه است: از chois فرانسهٔ کهن (اسم از choisir «برگزیدن») که خودش وامی است از ژرمنی (*kausjan گوتی) در گالو‑رومی، و در سدهٔ سیزدهم به انگلیسی میانه به شکل chois رسیده و بعدها choice نوشته شده است. کلاین (ص ۲۸۲–۲۸۳): «F. choisir، OProvenç. causir، OSlav. kusiti وام‌واژه‌های گوتی‌اند. رک: choice». واتکینز نیز choose را زیر *keusan و choice را زیر *kausjan گوتی می‌آورد. این گره در کتاب ارجاعی ندارد، ولی زنجیره‌اش بی‌مناقشه است.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/%C7%B5ews-\"],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\",\n       \"note\": \"the node carries no reference in the book (refs=None); checked against Klein p.282 f. and Watkins instead, both recorded under 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"pp. 282-283 s.v. choose (KLN_1966.txt leaf 159)\", \"stance\": \"supports\",\n       \"note\": \"'choose, tr. and intr. v. — ME. cheosen, chesen, chusen, fr. OE. ceosan … Goth. kiusan, „to choose“ … fr. I.-E. base *geus-, *gus-, „to taste, enjoy by tasting“ … Cp. choice. Cp. also gust, „relish“, disgust.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 1357)\", \"stance\": \"supports\",\n       \"note\": \"'CHOICE geus- … CHOOSE geus-'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Latin\", \"words\": \"gustus; dis-goust\", \"verdict\": \"plausible\",\n     \"derivation\": \"The first word is right, the second is misfiled. Latin gustus, -ūs m. 'a tasting, taste, relish' is the suffixed zero-grade *ǵus-tu- of the root (Watkins: 'Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: GUST², GUSTO; DISGUST, RAGOUT; b. Latin gustāre, to taste: DEGUST'), with the denominative verb gustāre built on the participle *ǵus-to-. But 'dis-goust' is not a Latin word: it is the Middle French noun desgoust (modern dégoût), formed in French from des- (< Latin dis-) plus goust 'taste' (< Latin gustus), beside the verb desgouster (< Vulgar Latin *disgustāre from gustāre). Klein s.v. disgust: 'Earlier F. desgouster (F. dégoûter), „to disgust“, fr. des- (fr. L. dis-) and gouster (F. goûter), „to taste“, fr. L. gustāre'; and the noun 'Earlier F. desgoust (F. dégoût), fr. desgouster'. So the box should read Latin gustus / gustāre with a separate French desgoust node under it; as drawn, a French form wears a Latin label. Everything else in the box is correct, hence 'plausible' rather than 'disputed'.\",\n     \"derivation_fa\": \"واژهٔ نخست درست است و دومی سرِ جای خود نیست. gustus لاتینی «چشیدن، مزه، ذائقه» همان درجهٔ صفرِ پسونددارِ *ǵus-tu- است (واتکینز: «*gus-tu- در لاتینِ gustus: GUST, GUSTO, DISGUST, RAGOUT؛ و gustāre: DEGUST»)، و فعلِ اسم‌بنیادِ gustāre بر صفت مفعولیِ *ǵus-to- ساخته شده است. اما «dis-goust» واژه‌ای لاتینی نیست: صورتِ فرانسهٔ میانهٔ desgoust (فرانسهٔ امروز dégoût) است که در خودِ فرانسه از des- (بازماندهٔ dis- لاتینی) و goust «مزه» (از gustus) ساخته شده، در کنار فعلِ desgouster (از *disgustāre لاتینیِ عامیانه). کلاین در مدخل disgust: «Earlier F. desgouster … fr. des- (fr. L. dis-) and gouster … fr. L. gustāre» و برای اسم: «Earlier F. desgoust (F. dégoût), fr. desgouster». پس درست آن بود که جعبه gustus/gustāre لاتینی را داشته باشد و desgoust فرانسوی گرهی جداگانه زیر آن باشد؛ چنان‌که هست، صورتی فرانسوی برچسبِ «لاتین» خورده است. چون باقیِ جعبه درست است، حکم «با احتیاط پذیرفتنی» است نه رد.\",\n     \"sources\": [\"https://www.etymonline.com/word/disgust\", W + \"Reconstruction:Proto-Indo-European/%C7%B5ews-\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:377\", \"status\": \"not_checked\",\n       \"note\": \"AHD:377 is a page of the main New College Edition dictionary (the alphabetical d- section, where 'disgust' falls), not of the IE appendix; no copy of that edition is available here (archive.org copies are lending-only). The claim it is meant to support is however exactly what Watkins' appendix says at geus-: 'Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: GUST², GUSTO; DISGUST, RAGOUT' — recorded under 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 501)\", \"stance\": \"partial\",\n       \"note\": \"'3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST²), GUSTO; DISGUST, RAGOUT; b. Latin gustāre, to taste: DEGUST.' Confirms gustus and the route to DISGUST, but routes it through Latin gustāre + French, never through a Latin *disgustus.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. disgust (KLN_1966.txt leaf 251) and s.v. gust 'relish' (leaf 371, pp. 688-689)\", \"stance\": \"contradicts\",\n       \"note\": \"'disgust, tr. v. — Earlier F. desgouster (F. dégoûter), „to disgust“, fr. des- (fr. L. dis-) and gouster (F. goûter), „to taste“, fr. L. gustāre'; 'disgust, n. — Earlier F. desgoust (F. dégoût), fr. desgouster'; 'gust, n., relish. — L. gustus, „tasting, taste“. See choose.' Klein makes desgoust French, not Latin.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 399 f. (POK_full.txt line 35720)\", \"stance\": \"supports\",\n       \"note\": \"'of tu-: Latin gustus, -ūs „a tasting of food … taste, flavor“ … derivative of participle *ǵus-tos: Latin gustō, -āre „taste, eat, drink“.' — Latin gustus yes; no *disgustus anywhere.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (LAT.txt, grep 'gust')\", \"stance\": \"silent\",\n       \"note\": \"the local OCR of Ernout-Meillet returns only angustus/augustus; the g- fascicle is not in this scan, so no independent Latin-dictionary check was possible.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"English\", \"words\": \"disgust\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English disgust (verb and noun, both from the 1590s) is borrowed from earlier French: the verb from desgouster 'to put off the taste of, to displease', the noun from desgoust 'strong dislike, distaste' (modern dégoût), themselves built in French on goust/goûter < Latin gustus/gustāre 'taste'. The English sense 'repugnance excited by something offensive' develops out of the literal 'distaste' during the 17th century. Etymonline gives exactly this chain and traces it to PIE *geus- 'to taste; to choose'; Klein the same. The arrow from the (Latin) box is therefore right in substance — English disgust does go back to Latin gustus — but it passes through French, which the chart does not show.\",\n     \"derivation_fa\": \"disgust انگلیسی (فعل و اسم، هر دو از دههٔ ۱۵۹۰) وامی است از فرانسه: فعل از desgouster «بی‌ذوق کردن، ناخوش آمدن» و اسم از desgoust «بیزاری، بدمزگی» (فرانسهٔ امروز dégoût)، که خودشان در فرانسه بر goust/goûter (از gustus/gustāre لاتینی) ساخته شده‌اند. معنای امروزیِ «نفرت از چیزِ زننده» در سدهٔ هفدهم از همان «بدمزگی» تحول یافته است. اتیمانلاین همین زنجیره را می‌دهد و آن را به ریشهٔ *geus- «چشیدن، برگزیدن» می‌رساند؛ کلاین نیز همین. پس پیکانِ این گره در اصل درست است — disgust انگلیسی سرانجام به gustus لاتینی می‌رسد — اما راهش از فرانسه می‌گذرد و نمودار این حلقه را نشان نداده است.\",\n     \"sources\": [\"https://www.etymonline.com/word/disgust\"],\n     \"ref_check\": [\n      {\"ref\": \"none\", \"status\": \"not_checked\",\n       \"note\": \"the node carries no reference in the book (refs=None); checked against Klein s.v. disgust and Etymonline, recorded under 'consulted'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. disgust (KLN_1966.txt leaf 251)\", \"stance\": \"supports\",\n       \"note\": \"'disgust, tr. v. — Earlier F. desgouster (F. dégoûter) … fr. des- (fr. L. dis-) and gouster (F. goûter), „to taste“, fr. L. gustāre, of s.m. See gust, „relish“, and cp. degust.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 1418)\", \"stance\": \"supports\",\n       \"note\": \"'DISGUST geus-'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Ghaido\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gʰaidos (Pokorny ghaido- / ĝhaido-) 'goat, he-goat'\",\n   \"note\": \"The root box itself is right: Pokorny IEW 409-410 'ghaido- or ĝhaido- | Meaning: goat | Material: Latin haedus „a young goat, a kid“ …; Gothic gaits and Old High German geiz, Old Icelandic geit, Old English gāt, Old Saxon gēt „goat“ …'; Walde-Pokorny I 527 f. the same; Watkins 'ghaido-. A goat. Germanic *gaitaz in Old English gāt, goat: GOAT. [Pok. ghaido- 409.]'. What is not right is the shape of the tree hung under it. Pokorny, Walde-Pokorny, Watkins and Klein all know only two branches, Italic (haedus) and Germanic (*gaits); none of them lists an Armenian or an Iranian descendant, and Nourai's Persian and Armenian boxes rest solely on Gupta's CEL 5:7, a work that is not digitised anywhere and cannot be checked. Persian zāq and Armenian ձագ jag are real words with a real connection to each other, but they belong to a different (and probably non-Indo-European) group — Sogdian zāk 'child', Albanian zog 'nestling', Aramaic zāḡā — and cannot come from *gʰaidos on any regular sound law, since a stem in -d- cannot yield Persian -q or Armenian -g. Wiktionary's current entry on *gaits goes further and, following Bjørn, doubts a PIE origin for the Germanic word altogether, comparing Proto-Semitic *gady- and Proto-Berber *e-ɣăyd; that is a minority view and does not touch Nourai's root box, which faithfully reproduces his source.\",\n   \"note_fa\": \"خودِ جعبهٔ ریشه درست است: پوکورنی (ص ۴۰۹–۴۱۰) ریشهٔ ghaido- / ĝhaido- «بز» را با گواهانِ haedus لاتینی «بزغاله» و gaits گوتی، geiz آلمانی علیای کهن، gāt انگلیسی کهن می‌آورد؛ والده‑پوکورنی (۱: ۵۲۷) و واتکینز («ghaido-. A goat. Germanic *gaitaz in Old English gāt: GOAT») نیز همین. آنچه درست نیست، شکلِ درختی است که زیر این ریشه کشیده شده. پوکورنی، والده‑پوکورنی، واتکینز و کلاین تنها دو شاخه می‌شناسند: ایتالیایی (haedus) و ژرمنی (*gaits)؛ هیچ‌کدام بازماندهٔ ارمنی یا ایرانی نمی‌آورند، و جعبه‌های «فارسی» و «ارمنی»ِ نورایی تنها بر CEL 5:7 (گوپتا) تکیه دارند که هیچ نسخهٔ دیجیتالی از آن در دسترس نیست. «زاق» فارسی و ձագ (jag) ارمنی واژه‌هایی واقعی‌اند و با هم پیوند دارند، اما به گروهِ دیگری تعلق دارند — zāk سغدی «کودک»، zog آلبانیایی «جوجه»، zāḡā آرامی — و با هیچ قانونِ آواییِ منظمی از *gʰaidos برنمی‌آیند، چون ستاکی با ‑d‑ نه «ق» فارسی می‌دهد نه ‑g ارمنی. ویکی‌واژه امروز حتی پا را فراتر می‌گذارد و به پیروی از بیورن در هندواروپایی‌بودنِ خودِ واژهٔ ژرمنی هم تردید می‌کند و آن را با *gady- سامی آغازین و *e-ɣăyd بربری می‌سنجد؛ این دیدگاهی اقلیتی است و به جعبهٔ ریشهٔ نورایی، که وفادارانه مأخذش را بازمی‌گوید، آسیبی نمی‌زند.\",\n   \"sources\": [\n     \"https://www.etymonline.com/word/goat\",\n     W + \"Reconstruction:Proto-Germanic/gaits\",\n     W + \"%D5%B1%D5%A1%D5%A3\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:409\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 32248 ff.: 'Root / lemma: ghaido- or ĝhaido- | Meaning: goat | Material: Latin haedus, -ī m. „a young goat, a kid“ … Gothic gaits and Old High German geiz, Old Icelandic geit, Old Swedish get, Old English gāt, Old Saxon gēt (consonant stem) „goat“ … References: WP. I 527 f., WH. I 632, 868. Page(s): 409-410.' The root name, language label and gloss are exactly as Nourai prints them; the page has no Armenian and no Iranian material.\"},\n    {\"ref\": \"CEL5:7\", \"status\": \"not_checked\",\n     \"note\": \"S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, vol. 5 p.7 — refs_online.json records it as 'catalogue only; the 1997 Sverge Haus printing is not digitised anywhere found' (HathiTrust copies are search-only). This is the only authority Nourai gives for the Persian and Armenian branches, so those two arrows rest on an unverifiable source.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 527 f. (WLD_Bd1 djvu line 33164)\", \"stance\": \"supports\",\n     \"note\": \"'ghaido- oder ĝhaido- „Ziegenbock, Ziege“. Lat. haedus „Böckchen, junger Ziegenbock“ …; got. gaits und ahd. geiz f., aisl. geit f., aschw. get f., ags. gāt f., as. gēt f. (konsonant. Stämme) „Ziege“. Von ghaido- abgeleitet *ghaideinos: lat. haedinus …' — two branches only, Italic and Germanic.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 505) and p. 166 of the introduction\", \"stance\": \"supports\",\n     \"note\": \"'ghaido-. A goat. Germanic *gaitaz in Old English gāt, goat: GOAT. [Pok. ghaido- 409.]'; and in the essay on IE culture: 'the names for all the familiar domesticated animals … aig- and ghaido-, „goat“'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 3.36 GOAT (SYN.txt lines 4470, 4484)\", \"stance\": \"supports\",\n     \"note\": \"'Goth. gaits, ON geit, OE gāt, etc., a general Gmc. word: Lat. haedus „kid“; perh. Lith. žaidžiu, žaisti „play“ as orig. „jump, gambol“. Walde-P. 1.527.' Buck's Avestan/Sanskrit column under 'goat' has aja-/buza-, not anything from this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Persian\", \"words\": \"zâq «زاق»; zâq-dân «زاقدان»\", \"verdict\": \"disputed\",\n     \"derivation\": \"Both Persian words are real and the glosses are right — Mo'in s.v. زاق '(اِ.) بچهٔ هر چیز' and Dehkhoda 'بچه هر چیز را گویند'; زاقدان 'بچه‌دان، زهدان', Dehkhoda 'قرارگاه نطفه در شکم که آن را زهدان نیز گویند و به تازی رحم خوانند', so 'womb' is exact, and the compound is transparently zāq 'young' + the container suffix -dān (< Iranian *-dāna-, root dā- 'to place', PIE *dʰeh₁-, which is why Nourai cross-refers to his root Dhē 2). What is wrong is the parentage. زاق cannot descend from *gʰaidos: a PIE stem in *-d- gives Iranian -d-, never -q, and PIE *gʰ- gives Iranian g- (a palatal *ǵʰ- would give z- but then the -d- remains). The word belongs instead to a well-known but etymologically unsettled cluster — Armenian ձագ jag 'young of an animal, nestling', Sogdian zāk 'child', Albanian zog 'bird, nestling', Classical Syriac zāggā — for which Wiktionary (following Ačaṙyan and Olsen) offers either a PIE root 'of the unusual shape *ǵʰāgʰ-' or, judged 'more likely', a borrowing from Aramaic zāḡā 'young cock or hen'. Neither option is *gʰaidos 'goat'. Nourai's only authority is Gupta CEL 5:7, which cannot be consulted.\",\n     \"derivation_fa\": \"هر دو واژهٔ فارسی واقعی‌اند و معناهایی که نورایی داده درست است: معین ذیل «زاق» می‌آورد «(اِ.) بچهٔ هر چیز» و دهخدا «بچهٔ هر چیز را گویند»؛ و «زاقدان» را معین «بچه‌دان، زهدان» و دهخدا «قرارگاه نطفه در شکم که آن را زهدان نیز گویند و به تازی رحم خوانند» — پس معنای «womb» دقیق است و ترکیب هم روشن است: زاق «بچه» + پسوندِ ظرفِ ‑دان (از ایرانیِ *‑dāna-، از ستاکِ dā- «نهادن»، هندواروپاییِ *dʰeh₁-، و از همین رو نورایی به ریشهٔ Dhē 2 ارجاع می‌دهد). آنچه نادرست است نسبِ واژه است. «زاق» نمی‌تواند از *gʰaidos بیاید: ستاکی با *‑d‑ هندواروپایی در ایرانی ‑d‑ می‌دهد نه «ق»، و *gʰ‑ آغازین در ایرانی g می‌شود (اگر *ǵʰ‑ کامی باشد z می‌دهد، اما آنگاه ‑d‑ سرِ جایش می‌ماند). این واژه در حقیقت به خوشه‌ای شناخته اما ریشه‌شناسی‌نشده تعلق دارد: ձագ (jag) ارمنی «بچهٔ جانور، جوجه»، zāk سغدی «کودک»، zog آلبانیایی «جوجه»، zāggā سریانی؛ ویکی‌واژه (به پیروی از آچاریان و اولسن) یا ریشه‌ای هندواروپایی با ساختِ نامعمولِ *ǵʰāgʰ- پیشنهاد می‌کند یا — که آن را «محتمل‌تر» می‌داند — وام‌گیری از zāḡā آرامی «جوجه‌خروس». هیچ‌یک *gʰaidos «بز» نیست. تنها مأخذ نورایی CEL 5:7 گوپتاست که در دسترس نیست. پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [W + \"%D5%B1%D5%A1%D5%A3\", \"https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82/\", \"https://abadis.ir/fatofa/%D8%B2%D8%A7%D9%82%D8%AF%D8%A7%D9%86/\"],\n     \"ref_check\": [\n      {\"ref\": \"CEL5:7\", \"status\": \"not_checked\",\n       \"note\": \"Gupta's Comparative Etymologic Lexicon is catalogue-only (refs_online.json: 'the 1997 Sverge Haus printing is not digitised anywhere found'); HathiTrust holds only search-only volumes. Nourai's single authority for this arrow therefore cannot be examined.\"},\n      {\"ref\": \"MON:1712\", \"status\": \"supports\",\n       \"note\": \"Mo'in's Farhang-e Farsi s.v. زاق, read via abadis.ir/fatofa/زاق (the 6-vol pagination cannot be checked online, but the entry exists and reads exactly as Nourai glosses it): '(اِ.) بچهٔ هر چیز'; and s.v. زاقدان: 'بچه‌دان، زهدان'. Mo'in gives no origin tag at all — no [په.], no [ع.] — so he supports the word and the gloss but says nothing about the etymology Nourai draws.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. زاق and زاقدان (abadis.ir)\", \"stance\": \"partial\",\n       \"note\": \"'(اِ.) بچة هر چیز' / 'بچه دان ، زهدان' — the words and glosses are confirmed, the etymology is not addressed.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 2 (BQT_v2_pages.txt, grep 'زاق')\", \"stance\": \"silent\",\n       \"note\": \"no usable زاق entry surfaced in the OCR of the volume; Mo'in's etymological footnotes therefore give nothing for or against.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 409 f. (POK_full.txt line 32248 ff.)\", \"stance\": \"contradicts\",\n       \"note\": \"the whole ghaido- entry lists only Latin haedus, Albanian dhi(a) and the Germanic words; there is no Iranian reflex, and Pokorny even devotes a paragraph to rejecting further additions to the root.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss (HRN.txt, grep 'zāq', 'zaq')\", \"stance\": \"silent\",\n       \"note\": \"Horn has no entry for زاق, i.e. he does not treat it as an inherited Iranian word.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Armenian\", \"words\": \"jag\", \"verdict\": \"disputed\",\n     \"derivation\": \"Armenian ձագ (jag) 'young of an animal, nestling, chick' is a real and common word, and Nourai's gloss 'young beast' is fair. Its connection to Persian زاق is also real — Wiktionary's entry says the word is 'usually compared to Albanian zog („bird; nestling“), Persian زاق (zâq, „the young of anything“), Sogdian zāk („child“) and Classical Syriac zāggā'. But that is a comparison within an obscure regional cluster, not a descent from *gʰaidos. The two hypotheses actually on offer are (a) inheritance from a PIE root 'of the unusual shape *ǵʰāgʰ-' — which would give Armenian j- and a velar in the coda, as required, but has no other IE support — and (b) borrowing from Aramaic zāḡā 'young cock or hen', which Wiktionary judges 'more likely' and which also explains why the Iranian form has z- where an Iranian loan into Armenian would have given զ- (z-) rather than ձ- (j-). Neither hypothesis involves 'goat'. Formally, *gʰaidos would give Armenian *j-ayd- or *g-ayd-, never jag: the dental of the root has no way to become -g. Pokorny, Walde-Pokorny, Watkins, Klein and Buck list no Armenian reflex of ghaido- at all; Walde-Pokorny mentions Armenian only in the neighbouring discussion of tik 'skin bag'.\",\n     \"derivation_fa\": \"ձագ (jag) ارمنی «بچهٔ جانور، جوجه» واژه‌ای واقعی و پرکاربرد است و معنایی که نورایی داده («young beast») بجاست. پیوندش با «زاق» فارسی هم واقعی است؛ ویکی‌واژه می‌نویسد این واژه «معمولاً با zog آلبانیایی „پرنده، جوجه“، زاقِ فارسی „بچهٔ هر چیز“، zāk سغدی „کودک“ و zāggā سریانی سنجیده می‌شود». اما این سنجشی است درونِ خوشه‌ای مبهم و منطقه‌ای، نه فرودآمدن از *gʰaidos. دو فرضیهٔ موجود اینهاست: نخست، میراث از ریشه‌ای هندواروپایی با ساختِ نامعمولِ *ǵʰāgʰ- که j ارمنی و انسدادیِ نرم‌کامیِ پایانی را توضیح می‌دهد ولی گواهِ هندواروپاییِ دیگری ندارد؛ دوم، وام‌گیری از zāḡā آرامی «جوجه‌خروس» که ویکی‌واژه آن را «محتمل‌تر» می‌داند و توضیح می‌دهد چرا اگر واژه وامِ ایرانی می‌بود باید در ارمنی զ (z) می‌داشت نه ձ (j). هیچ‌کدام به «بز» ربطی ندارد. از نظر صوری نیز *gʰaidos در ارمنی *jayd- یا *gayd- می‌داد نه jag؛ دندانیِ ریشه به هیچ راهی g نمی‌شود. پوکورنی، والده‑پوکورنی، واتکینز، کلاین و باک هیچ بازماندهٔ ارمنی برای ghaido- نمی‌آورند. پژوهش امروزی این پیکان را رد می‌کند.\",\n     \"sources\": [W + \"%D5%B1%D5%A1%D5%A3\"],\n     \"ref_check\": [\n      {\"ref\": \"CEL5:7\", \"status\": \"not_checked\",\n       \"note\": \"Gupta, CEL vol. 5 p.7 — not digitised (refs_online.json 'catalog' entry, HathiTrust search-only), so Nourai's authority for the Armenian branch cannot be examined.\"},\n      {\"ref\": \"MON:1712\", \"status\": \"not_found\",\n       \"note\": \"Mo'in's dictionary is cited here for an Armenian headword; the Farhang-e Farsi entry at زاق (read via abadis.ir) carries no Armenian comparison and no origin tag, so the citation does not support the Armenian box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 409 f. (POK_full.txt line 32248 ff.)\", \"stance\": \"contradicts\",\n       \"note\": \"no Armenian appears under ghaido-; the only Armenian word mentioned in the article is tik 'hose (from goatskin)', and it is expressly attached to a different comparison (gr. δίζα).\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 527 f. (WLD_Bd1 djvu line 33186)\", \"stance\": \"contradicts\",\n       \"note\": \"'… vielmehr als Auslautsdublette zu gr. δίζα · αἶξ. Λάκωνες (Hes.) < *digi̯a, arm. tik „Schlauch“ zu stellen' — the one Armenian item in the entry, and it is not jag.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.36-3.38 (SYN.txt line 4470)\", \"stance\": \"silent\",\n       \"note\": \"Buck's table for GOAT / HE-GOAT / KID has no Armenian column entry connected to this root.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Germanic\", \"words\": \"gât\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The word and the arrow as PRINTED are correct: on the page the Germanic box hangs directly off the root box, at the same indentation and off the same vertical rule as the Armenian box, i.e. it is a sibling of Armenian jag, not its child. (The extracted JSON gives node 3 parent = 2, which the printed chart does not; see error_in below.) Germanic *gaits / OE gāt 'she-goat' is the regular reflex of PIE *gʰaidos: PIE *gʰ > Germanic *g by Grimm's Law, and the *-d- of the stem > Germanic *-t-, giving the consonant-stem feminine attested as Gothic gaits, OHG geiz, ON geit, OSw. get, OE gāt, OS gēt. Latin haedus is the Italic match (PIE *gʰ > Latin h-). Watkins, at the page Nourai cites for this box: 'ghaido-. A goat. Germanic *gaitaz in Old English gāt, goat: GOAT.' Klein p.666 f. s.v. goat: 'fr. I.-E. base *ghaido-, „kid, goat“, whence also L. haedus.' No source routes the Germanic word through Armenian, so had the book really drawn that arrow it would have been wrong; it does not.\",\n     \"derivation_fa\": \"خودِ واژه و پیکانی که در کتاب چاپ شده درست است: در صفحهٔ چاپی، جعبهٔ «ژرمنی» مستقیماً از جعبهٔ ریشه آویخته و با همان تورفتگی و از همان خطِ عمودیِ جعبهٔ «ارمنی» بیرون آمده، یعنی هم‌ردیفِ jag ارمنی است نه فرزندِ آن. (دادهٔ استخراج‌شده برای این گره parent = 2 گذاشته که در صفحهٔ چاپی چنین نیست؛ رک: error_in.) *gaits ژرمنی و gāt انگلیسی کهن «بز ماده» بازتابِ قاعده‌مندِ *gʰaidos است: *gʰ هندواروپایی با قانون گریم به g ژرمنی و *‑d‑ ستاک به ‑t‑ بدل می‌شود و ستاکِ صامتیِ مؤنث را می‌دهد که در گوتیِ gaits، آلمانی علیای کهنِ geiz، نُرسیِ geit، انگلیسی کهنِ gāt و ساکسون کهنِ gēt بازمانده است؛ haedus لاتینی همتای ایتالیایی آن است (*gʰ ← h لاتینی). واتکینز در همان صفحه‌ای که نورایی برای این جعبه ارجاع داده: «ghaido-. A goat. Germanic *gaitaz in Old English gāt: GOAT». کلاین (ص ۶۶۶): «fr. I.-E. base *ghaido-, „kid, goat“, whence also L. haedus». هیچ مأخذی واژهٔ ژرمنی را از راه ارمنی نمی‌آورد؛ اگر کتاب چنین پیکانی کشیده بود نادرست می‌بود، ولی نکشیده است. خطای خوانشِ اسکن.\",\n     \"error_in\": \"extraction\",\n     \"book_prints\": \"the Germanic box hangs directly from the root box, at the same indent level as the Armenian box (both branch off the same vertical rule, arrowheads aligned); it is a sibling of Armenian jag, not its child\",\n     \"correct_form\": \"node 3 (Germanic gât) should have parent 0, not parent 2\",\n     \"sources\": [\"https://www.etymonline.com/word/goat\", W + \"Reconstruction:Proto-Germanic/gaits\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1517\", \"status\": \"supports\",\n       \"note\": \"the IE appendix of the AHD New College Edition occupies pp. 1505-1550 and ghaido- falls in the gh- run around p. 1517; the corresponding text in the standalone Watkins 1985 (AHD_watkins1985.txt line 505) reads 'ghaido-. A goat. Germanic *gaitaz in Old English gāt, goat: GOAT. [Pok. ghaido- 409.]' — Nourai's Germanic form, gloss and parentage (root → Germanic, not Armenian → Germanic) all from this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 527 (WLD_Bd1 djvu line 33169)\", \"stance\": \"supports\",\n       \"note\": \"'got. gaits und ahd. geiz f., aisl. geit f., aschw. get, gēt f., ags. gāt f., as. gēt f. (konsonant. Stämme) „Ziege“' directly under the lemma ghaido-.\"},\n      {\"src\": \"KLN\", \"where\": \"pp. 666-667 s.v. goat (KLN_1966.txt leaf 360)\", \"stance\": \"supports\",\n       \"note\": \"'goat, n. — ME. goot, gote, fr. OE. gāt, rel. to OS. gēt, ON., Norw. geit, Swed. get, Dan. gjed, MDu. gheet, Du. geit, OHG., MHG. geiz, G. Geiß, Goth. gaits, „goat“, fr. I.-E. base *ghaido-, „kid, goat“, whence also L. haedus, „kid, young goat“.'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.36 (SYN.txt line 4484)\", \"stance\": \"supports\",\n       \"note\": \"'Goth. gaits, ON geit, OE gāt, etc., a general Gmc. word: Lat. haedus „kid“ … Walde-P. 1.527.'\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"goat\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE gāt (fem., 'she-goat') > ME goot, gote > NE goat, with the regular Middle English lengthening/rounding of OE ā to ō and the modern spelling oa. In Old English gāt was specifically the female and bucca the male; the word became generic in Middle English. Etymonline: 'Old English gat „she-goat“, from Proto-Germanic *gaito …, from PIE *ghaid-o- „young goat“ … Latin haedus „kid“'. Klein and Watkins agree, and Watkins' English index prints 'GOAT ghaido-'. The Germanic → English arrow is uncontroversial.\",\n     \"derivation_fa\": \"goat انگلیسی از gāt انگلیسی کهن (مؤنث: «بز ماده») می‌آید: gāt ← goot/gote انگلیسی میانه ← goat، با کشش و گردشدگیِ قاعده‌مندِ ā انگلیسی کهن به ō در انگلیسی میانه و املای امروزیِ oa. در انگلیسی کهن gāt ویژهٔ ماده بود و نر را bucca می‌گفتند؛ در انگلیسی میانه واژه عام شد. اتیمانلاین: «Old English gat „she-goat“، از ژرمنی آغازینِ *gaito، از هندواروپاییِ *ghaid-o- „بزغاله“ … haedus لاتینی». کلاین و واتکینز نیز همین را می‌گویند و در نمایهٔ واژه‌های انگلیسیِ واتکینز آمده «GOAT ghaido-». پیکانِ ژرمنی ← انگلیسی بی‌مناقشه است و ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/goat\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 505 'ghaido-. A goat. Germanic *gaitaz in Old English gāt, goat: GOAT'; and the English index at line 1565: 'GOAT ghaido-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"pp. 666-667 s.v. goat (KLN_1966.txt leaf 360)\", \"stance\": \"supports\",\n       \"note\": \"'goat, n. — ME. goot, gote, fr. OE. gāt …'\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 3.36 GOAT (SYN.txt line 4470)\", \"stance\": \"supports\",\n       \"note\": \"Buck's table gives the English column 'OE gāt / ME gote / NE goat' in the same row as Goth. gaits and ON geit.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-178.json','w',encoding='utf-8') as f:\n    json.dump(data, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk178.py",
 "description": "Write verification JSON for page 178"
}
```


### [2026-09-05T21:15:09.991Z] TOOL RESULT

```
written
```


## [2026-09-05T21:15:10.603Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
