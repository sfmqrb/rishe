# Verification process log — verify-page-443


## [2026-09-14T01:55:51.186Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 443 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-443.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-443.json. Write /home/sfmqrb/git/rishe/data/verification/page-443.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 443` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:52.148Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-14T01:55:52.971Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:52.986Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:55:53.532Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-443.txt"
}
```


### [2026-09-14T01:55:53.553Z] TOOL RESULT

```
1	=== PDF page 443 (book page 413) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sem 2, Sam : summer  (refs POK:905)
4	#1 (parent #0) [Avestan] refs=POK:905; KLN:1541 | ham 2, hama 2 : summer
5	  #2 (parent #1) [Persian] refs=HRN:280 | hamîn «همین» : summer (obsolete)
6	#3 (parent #0) [Sanskrit] refs=KLN:1541 | samâ : half-year
7	#4 (parent #0) [Germanic] refs=POK:905; AHD | sumaraz : summer
8	  #5 (parent #4) [English] refs=AHD | summer
9	--- entry 1 ---
10	ROOT [Greek] Sěma, A-sěma : Sěma: marked, stamped (coin); A-sěma: unmarked, unstamped (silver)  (refs KNT:209; MON:1982)
11	#1 (parent #0) [Pahlavi] refs=KNT:209 | asěm, sîm : silver ; sîměn : made of or shining like silver, white
12	  #2 (parent #1) [Persian] refs=BQT:1212; KNT:209; MON:1982 | sîm 2 «سیم ۲» : silver ; sîm 3 «سیم ۳» : electric wire (originally made of silver) ; sîm 4 «سیم ۴ ( سیماب )» : mercury (due to its white shiny color) | extra: سیم کشی ، سیم پیچ ، بی سیم
13	#3 (parent #0) [Old Persian] refs=KNT:209 | siyaman : made of silver
14	--- entry 2 ---
15	ROOT [Indo-European] Sen 1, Seno : old  (refs POK:907)
16	#1 (parent #0) [Avestan] refs=POK:907 | hana, hanâ : old
17	  #2 (parent #1) [Persian] refs=HRN:280 | hân «هان» : old (obsolete)
18	#3 (parent #0) [Latin] refs=POK:907; AHD | senex : old ; senior : old, old man
19	  #4 (parent #3) [French] refs=AHD | monsieur : sir ; seinat : an assembly of old wise men ; senateur : a member of the senate
20	    #5 (parent #4) [Persian] refs=MON:1925,4125 | mosyo «مُسیو» : sir ; senâ «سنا» : senate ; senâtor «سناتور» : senator
21	    #6 (parent #4) [English] refs=AHD | sir, senior, senile, senate, senator
22	#7 (parent #0) [Sanskrit] refs=POK:907 | sana : old
23	
```


## [2026-09-14T01:55:54.892Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-14T01:55:56.182Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-443.json",
 "description": "Read source JSON for page 443"
}
```


### [2026-09-14T01:55:56.226Z] TOOL RESULT

```
{
  "pdf_page": 443,
  "book_page": 413,
  "entries": [
    {
      "root": {
        "name": "Sem 2, Sam",
        "lang": "Indo-European",
        "refs": "POK:905",
        "gloss": "summer"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:905; KLN:1541",
          "words": [
            {"translit": "ham 2, hama 2", "gloss": "summer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:280",
          "words": [
            {"translit": "hamîn", "gloss": "summer (obsolete)", "script": "همین"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "KLN:1541",
          "words": [
            {"translit": "samâ", "gloss": "half-year", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "POK:905; AHD",
          "words": [
            {"translit": "sumaraz", "gloss": "summer", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "summer", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sěma, A-sěma",
        "lang": "Greek",
        "refs": "KNT:209; MON:1982",
        "gloss": "Sěma: marked, stamped (coin); A-sěma: unmarked, unstamped (silver)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "KNT:209",
          "words": [
            {"translit": "asěm, sîm", "gloss": "silver", "script": null},
            {"translit": "sîměn", "gloss": "made of or shining like silver, white", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1212; KNT:209; MON:1982",
          "words": [
            {"translit": "sîm 2", "gloss": "silver", "script": "سیم ۲"},
            {"translit": "sîm 3", "gloss": "electric wire (originally made of silver)", "script": "سیم ۳"},
            {"translit": "sîm 4", "gloss": "mercury (due to its white shiny color)", "script": "سیم ۴ ( سیماب )"}
          ],
          "script_extra": "سیم کشی ، سیم پیچ ، بی سیم",
          "note": null,
          "quote": {
            "text": "سیم و زر دنیا پرستان را منافق میکند - پشت و رو باشد یکی آیینهٔ بی سیم را",
            "poet": "Tâher Vahîd"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:209",
          "words": [
            {"translit": "siyaman", "gloss": "made of silver", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sen 1, Seno",
        "lang": "Indo-European",
        "refs": "POK:907",
        "gloss": "old"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:907",
          "words": [
            {"translit": "hana, hanâ", "gloss": "old", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:280",
          "words": [
            {"translit": "hân", "gloss": "old (obsolete)", "script": "هان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:907; AHD",
          "words": [
            {"translit": "senex", "gloss": "old", "script": null},
            {"translit": "senior", "gloss": "old, old man", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "monsieur", "gloss": "sir", "script": null},
            {"translit": "seinat", "gloss": "an assembly of old wise men", "script": null},
            {"translit": "senateur", "gloss": "a member of the senate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1925,4125",
          "words": [
            {"translit": "mosyo", "gloss": "sir", "script": "مُسیو"},
            {"translit": "senâ", "gloss": "senate", "script": "سنا"},
            {"translit": "senâtor", "gloss": "senator", "script": "سناتور"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "sir, senior, senile, senate, senator", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:907",
          "words": [
            {"translit": "sana", "gloss": "old", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:55:58.545Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','AHD','HRN','KNT','BQT','MON','WLD','IEC','SYN','BRT','PHD','NYB','HUB','ARY','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online.json for relevant keys"
}
```


### [2026-09-14T01:55:59.794Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-14T01:56:11.558Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,120p' SOURCE_MATRIX.md; echo ===; ls refs/ | head -60",
 "description": "Read source matrix and list refs"
}
```


### [2026-09-14T01:56:11.630Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-14T01:56:12.562Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls; echo ===; head -60 page-385.json",
 "description": "List verification dir and sample prior file"
}
```


### [2026-09-14T01:56:12.641Z] TOOL RESULT

```
Exit code 1
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
page-150.json
page-151.json
page-152.json
page-153.json
page-154.json
page-155.json
page-156.json
page-157.json
page-158.json
page-159.json
page-160.json
page-161.json
page-162.json
page-163.json
page-164.json
page-165.json
page-166.json
page-167.json
page-168.json
page-169.json
page-170.json
page-171.json
page-172.json
page-173.json
page-174.json
page-175.json
page-176.json
page-177.json
page-178.json
page-179.json
page-180.json
page-181.json
page-182.json
page-183.json
page-184.json
page-185.json
page-186.json
page-187.json
page-188.json
page-189.json
page-190.json
page-191.json
page-192.json
page-193.json
page-194.json
page-195.json
page-196.json
page-197.json
page-198.json
page-199.json
page-200.json
page-201.json
page-202.json
page-203.json
page-204.json
page-205.json
page-206.json
page-207.json
page-208.json
page-209.json
page-210.json
page-211.json
page-212.json
page-213.json
page-214.json
page-215.json
page-216.json
page-217.json
page-218.json
page-219.json
page-220.json
page-221.json
page-222.json
page-223.json
page-224.json
page-225.json
page-226.json
page-227.json
page-228.json
page-229.json
page-230.json
page-231.json
page-232.json
page-233.json
page-234.json
page-235.json
page-236.json
page-237.json
page-238.json
page-239.json
page-240.json
page-241.json
page-242.json
page-243.json
page-244.json
page-245.json
page-246.json
page-247.json
page-248.json
page-249.json
page-250.json
page-251.json
page-252.json
page-253.json
page-254.json
page-255.json
page-256.json
page-257.json
page-258.json
page-259.json
page-260.json
page-261.json
page-262.json
page-263.json
page-264.json
page-265.json
page-266.json
page-267.json
page-268.json
page-269.json
page-270.json
page-271.json
page-272.json
page-273.json
page-274.json
page-275.json
page-276.json
page-277.json
page-278.json
page-279.json
page-280.json
page-281.json
page-282.json
page-283.json
page-284.json
page-285.json
page-286.json
page-287.json
page-288.json
page-289.json
page-290.json
page-291.json
page-292.json
page-293.json
page-294.json
page-295.json
page-296.json
page-297.json
page-298.json
page-299.json
page-300.json
page-301.json
page-302.json
page-303.json
page-304.json
page-305.json
page-306.json
page-307.json
page-308.json
page-309.json
page-310.json
page-311.json
page-312.json
page-313.json
page-314.json
page-315.json
page-316.json
page-317.json
page-318.json
page-319.json
page-31.json
page-320.json
page-321.json
page-322.json
page-323.json
page-324.json
page-325.json
page-326.json
page-327.json
page-328.json
page-329.json
page-32.json
page-330.json
page-331.json
page-332.json
page-333.json
page-334.json
page-335.json
page-336.json
page-337.json
page-338.json
page-339.json
page-33.json
page-340.json
page-341.json
page-342.json
page-343.json
page-344.json
page-345.json
page-346.json
page-347.json
page-348.json
page-349.json
page-34.json
page-350.json
page-351.json
page-352.json
page-353.json
page-354.json
page-355.json
page-356.json
page-357.json
page-358.json
page-359.json
page-35.json
page-360.json
page-361.json
page-362.json
page-363.json
page-364.json
page-365.json
page-366.json
page-367.json
page-368.json
page-369.json
page-36.json
page-370.json
page-371.json
page-372.json
page-373.json
page-374.json
page-375.json
page-376.json
page-377.json
page-378.json
page-379.json
page-37.json
page-380.json
page-381.json
page-382.json
page-383.json
page-384.json
page-385.json
page-386.json
page-387.json
page-388.json
page-389.json
page-38.json
page-390.json
page-391.json
page-392.json
page-393.json
page-394.json
page-395.json
page-396.json
page-397.json
page-398.json
page-399.json
page-39.json
page-400.json
page-401.json
page-402.json
page-403.json
page-404.json
page-405.json
page-406.json
page-407.json
page-408.json
page-409.json
page-40.json
page-410.json
page-411.json
page-412.json
page-413.json
page-414.json
page-415.json
page-416.json
page-417.json
page-418.json
page-419.json
page-41.json
page-420.json
page-421.json
page-422.json
page-423.json
page-424.json
page-425.json
page-426.json
page-427.json
page-428.json
page-429.json
page-42.json
page-430.json
page-431.json
page-432.json
page-433.json
page-434.json
page-435.json
page-436.json
page-437.json
page-438.json
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
page-56.json
page-57.json
page-58.json
page-59.json
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
page-76.json
page-77.json
page-78.json
page-79.json
page-80.json
page-81.json
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
page-97.json
page-98.json
page-99.json
process
sources
(eval):1: == not found
```


## [2026-09-14T01:56:14.466Z] AGENT

Now let me look up the local reference texts.


## [2026-09-14T01:56:17.704Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,io\nfor f in ['POK_full.txt']:\n    try:\n        t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e:\n        print(f,e); continue\n    print(f, len(t))\n    # find sem-3 summer\n    for m in re.finditer(r'sem-?\\s*3', t):\n        print('---', t[max(0,m.start()-200):m.start()+600].replace('\\n',' | ')[:900])\n        break\nEOF",
 "description": "Grep Pokorny for sem-3"
}
```


## [2026-09-14T01:56:18.715Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ===; grep -n \"905\" POK_full.txt | head -5",
 "description": "List ref files"
}
```


### [2026-09-14T01:56:19.139Z] TOOL RESULT

```
POK_full.txt 3967710
---  | Page(s): 778  |  | Root / lemma: om- {*houm-)  |  | Meaning: raw, bitter, *sweet  |  | Note: reduced grade oin-  |  | Root/ lemma: om-{*hamef}\ "raw, bitter, *sweet' : Root/ lemma: sem-1\ "to pour' : Root/  |  | lemma: sem-3\ "summer'. Old Indie amia-, ambla-^sour, sorrel, Oxalis acetosella ' : gall.  |  | samor{ios] "summer months', samolus^ sour, sorrel, Oxalis acetosella '.  |  | Material: Old Indie amIa-, ambia- "sour, sorrel, Oxalis acetosella ' (= maked. appo-,  |  | Germanic *ampra-), zero grade amra-m. " Mango tree ', ama- "raw, unripe ' (= gr. u)|j6(;),  |  | amad- " eating raw flesh '; skyth. VN ApaSoKOi from Iran. *amad-aka- " raw meat eater ';  |  | Note:  |  | Phonetically the closest cognate to Old Indie amIa-, ambIa- "sour' is alb. Geg amIa, Tose  |  | emb(e)la "sweet' common alb. shift m > mb. Clearly the cognate of Old
```


### [2026-09-14T01:56:19.199Z] TOOL RESULT

```
Exit code 1
AFA.txt
AFM_alt.txt
AFM_pages.txt
AFM.pdf
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
incoming
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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
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
(eval):1: == not found
```


## [2026-09-14T01:56:24.634Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=Page\\(s\\):)', t)\nfor b in blocks:\n    m=re.match(r'Page\\(s\\):\\s*(\\d+)', b)\n    if m and m.group(1) in ('905','906','907'):\n        head=b[:1800].replace('\\n',' | ')\n        print('=====', m.group(1), head[:1800])\n        print()\nEOF",
 "description": "Extract Pokorny pages 905-907 entries"
}
```


### [2026-09-14T01:56:25.899Z] TOOL RESULT

```
===== 905 Page(s): 905  |  | Root /lemma: send'^ro-, -a  |  | Meaning: clot, melted metal, etc..  |  | Note: only Germanic and Slavic  |  | Material: Old Icelandic sindru. "Metallschlacke' and "Hammerschlag' (in addition sindra^  |  | spark, produce sparks '), Old English sinderds.. Old High German sinterds.. Modern High  |  | German Sinter, Kalksinter (\v\ addition s//7/e/'/7"durchsickern, curdle, coagulate, harden ');  |  | vermutlichverwandt is Norwegian dial, s/nk/a ^ s\c\r\ with an Ice crust beziehen' as *sind-kla;  |  |  |  | Serb. -Church Slavic sedry krbvbnyje, russ. -Church Slavic sjadry krovnyja ^ coagulated  | Blutmassen', Serbo-Croatian seo'/'a'Ka Iks inter', Czech sao'/'a'Gips' (from *sen6'^ra).  | References: WP. II 497, Trautmann 256.  | 

===== 906 Page(s): 906  |  | Root / lemma: seng^h-  |  | Meaning: to sing  |  | Material: Prakr. samghai^say, instruct'; gr. opcpn "voice, Prophezeiung' {*song'^ha),  |  | navo|j(paTo(; "epithet of Zeus'; mcymr. defhjong/' dei\ne'; Note: common lllyrian g"'- > b-.  |  | Gothic 5/ig^M/5/7"sing, vorlesen, rezitieren'. Old Icelandic syngua. Old English Old High  | German Old Saxon singan, singen, Gothic saggws^ song, Musik, Vorlesung', Old  | Icelandic sgngr'{ religious) song'. Old English sang, song, Old High German Old Saxon  | sang. Sang " chant, song '.  |  | References: WP. II 496, Bloch BSL 31 , 62, Vendryes RC 48, 476; after W. WiJst (briefl.)  | belongs prakr. samgha/to Rens-, above S. 566.  | 

===== 906 Page(s): 906-907  |  | Root / lemma: seng"-  |  | Meaning: to fall, sink  |  | Note:  |  | From Root / lemma: sek-1 : to flow out, dry out (of water) derived Root / lemma: seng"- : to  |  | fall, sink  |  | Material: Armenian ankan/mlaW, retreat, take ab'; gr. eacpOri "sank' {aamq);  |  | Germanic *sinkwan\v\: Gothic sigqan. Old Icelandic S0kkva, Old English sincan. Old  | Saxon Old High German sinkan sinken, Intens. Danish-Norwegian sakka, Dutch zakken.  | Modern High German sacken^ sink '; Adj. *sinhti- in Old English s/77/e "sumpfig'. Middle  | High German sTht(e), Modern High German seichV shallow, having little depth ',  | Alemannian sTcht^vevj humid, wet' (from Wiesen).  |  | References: WP. II 495 f.  | 

===== 906 Page(s): 906  |  | Root /lemma: seni-, senu- {Sgni-), sp-ter-  | Meaning: for oneself; separate  |  |  |  | Material: Old Indie sanu-tar' abseWs from, welt weg', sanutara- (?), sanutya-^ furtive,  | unvermerkt' ("*beiseite'), Avestan /7a/7a/'a"abseits, without'; gr. arep (Ionian) 'abseits,  | without' ( *snter)\  |  | Old Saxon 5^/70'//' "without' (= arsp). Old High German suntar^ separate ' and "but,  | against it'. Modern High German sondern {d'\ese meaning from 'besides, without'). Old  | English 5^/7o''c»/''for sich, particularly, specially, especially, particular: in particular,  | peculiarly, separately, extra, notably ', Old Norse sundr^ divided ', Gothic sundrolor sich,  | abseits, particularly, specially, especially, particular: in particular, peculiarly, separately,  | extra, notably ', Adj. Middle High German sunder, besunder. Modern High German  | besonder,  |  | Latin 5//7e 'without' (probably neutr. *seni, standing next to Irish sa/afrom *Seni-)\  |  | Old Irish sain M]. 'different, particularly, specially, especially, particular: in particular,  | peculiarly, separately, extra, notably ' ( *Seni-s), cymr. o-han-, a-han- 'from', gwa-han  | 'apart, separated, different', acymr. /75/7'alium'; cymr. hanes' narration ' = Middle Irish  | sanas^ mystery, Lispein' ( *sani-sta)\ corn, hanys' secret '; Tocharian A sne, B sna/  | {*sana/) 'without';  |  | The meaning ' separate, for sich' allows connection with dem Reflexivstamm *se-,  | *s(e)ue-\.o, compare with aniaut su-: Old Church Slavic 5i/e/7e 'besides, without' and Latin  | sed, se preposition 'sine, without', prefix 'without, beiseite'.  |  | References: WP. II 494 f., WH. II 542 f., H. Lewis EC. 1, 322.  | 

===== 907 Page(s): 907  |  | Root / lemma: senk-  |  | Meaning: to burn, dry  |  | Note: only Germanic and Slavic  |  | Material: Old English sengan. Middle Low German Middle High German se/7^e/7 'singe'  |  | {*sangjan^ burn make'); Low German sangeren^\v\ the Haut prickein' (actually 'burn'), old  |  | Dutch se/7^e/ 'spark'. Middle High German senge^ dryness, aridity ', sinc{-g-) 'das  |  | Sengen', sungen, s^/7/re/7'anbrennen', sungein, sunkeln^ rustle ', Norwegian dial, sengra,  |  | se/7^/5'brenzlich smell', Swedish dial, sjang/a ^ s\nge' , isl. sang{u)r, n. sangt^s\nges,  |  | burns, angebrannt';  |  | Old Church S\av\c pre-sgc/t/, /spc///"dry', 5(?c//o 'oven', russ. /zsjak/yj^ dry'.  |  |  |  | References: WP. II 495.  | 

===== 907 Page(s): 907  |  | Root / lemma: sen(o)- {*heno)  |  | Meaning: old, *old moon  |  | Material: Old Indie sana-, Avestan hana- 'old', Old Indie s5/7a/r^-"ehemalig, old' (: Latin  |  | senex, Franeonian Sinigus, gall. Seneca), 55/75/7 "vor alters', sana, sanat, sanata Irom  |  | alters her, from jeher, stets', sanatana-^ eternal, immortal, perennial '; Armenian hanapaz^  |  | always ', h/n'o\d'; gr. £vo(; "old, of previous years', 5i-£vo(; " biennial ', £vr| Koi vsa ' the day  |  | before the new moon and the first one of the beginning month ';  |  | again gr. £vo(; 'old' in eontrast to "anew', only in standing phrases of fruit and employees of  |  | the last year, also from the last day of the last month or moon eireulation whieh initiates at  |  | the same time the new eireulation (sinee Hes.); in the last-named formation usually £vr| Kai  |  | v£a (se. a£Ar|vr|; Attie sinee Solon).  |  | Maybe alb. hana'{*o\6) moon' : gr. £voi; "old moon' : otkaq n. " brillianee', a£Ar|vr|, Aeolie  |  | a£Aavva "moon' (*a£Aaava), oeKa\/z\y " shine '; henee a£A-rivr| " the full-moon ' see Root/  |  | lemma: suel-2\ "to smoulder, burn'.  |  | Latin senex. Gen. senis, Kompar. sen/or^o\d, aged'; seneo, -ere'o\6, weak sein',  | senesco, -ere "a Item, dwindle away, deerease ', senium^ senility, zehrende  | GemiJtsstimmung', senatus, -us {Oscau Gen. senateis) "Senaf, senectus ' age' , senecio  | ds.; Old Irish se/7"old', aeymr. eorn. bret. hen^o\6 man, aged', eompounds Old Irish s/n/'u,  | eymr. hyn; Irish sen-math{a)ir{= Lithuanian sen-mote) "grandmother'; gall. Seno-gnatus ,  | Seneca, Gothie sineigs^ an old man ', S//7/5/5 "oldest'. Old Franeonian sini-skalkus^\he  | oldest Hausdiener', Old leelandie S//75" grass of the previous year'; Lithuanian 5^/755 "old',  | sen/'s' graybeard ', sen/a

===== 907 Page(s): 907-908  |  | Root / lemma: sent-  |  | Meaning: to take a direetion, go; to feel  |  | Material: A. in geistigen sense: Latin sentio, -Tre, -si, -sum' feel, pereeive ', sensus, -us'  |  | emotion, sense, mind, Gesinnung; opinion', sententia {*sentientia) "opinion ete.'; Old High  |  | German sin, -nnes'sense, mind' {*sent-no-), sinnan' strive, lust, erave'. Modern High  |  | German sinnen; (under the influenee of eommon Celtie -ns-, -nt- > -nn-), Lithuanian sinteti  |  | "think'; Old Chureh Slavie s^stb "smart'.  |  |  |  | Maybe zero grade alb. {*sentid, entio) ndjej'ieey [typical alb. mutation se- > e-]  |  | B. in eigentlichen sense: Avestan hant- (present hT-sasaX Fut. ni-sqsyS) " reach, reach  | let'; Armenian a/7/5c'way, gait ', ant'anam^QO, travel, journey, hurry ';  |  | Old Irish set'\Nay', cymr. hyntds., Middle Breton nbret. hent6s. (= Germanic *s/nPa-),  | abret. Gl. c/o-guo-h/nt/7/at ^\nceduus', acorn. cam-h/ns/cG\. 'iniustus' (ca/77- "crooked'), eun-  | hinsic(j\. 'Justus' {eun- " justified, legitimate '); therefrom Old Irish set/g'\N\ie, woman'  | ("Weggenossin', ^Fem. eines Adj. *setach)\ cymr. carrynt {to carr' cart ') 'way, journey',  | epynt{to eb-, *eRuo-) " horse-way', dyffrynt^vaWeY (to o'm//^ 'water'); from *se/7//c»-.'mcymr.  | hennydd^ fellow ', bret. /75/7/ez'Nachbar', corn, hynsads.;  |  | Gothic s/nf^sm. 'Mai', Old Icelandic s/nnn. 'Mai', s/'nn/n. ' gait, journey' (and as  | descendant of *gas/nf^ja- a\so ' cortege, UnterstiJtzung'), Old English s/dm. 'Fahrt,  | journey, way, Mai', Old Saxon 5/15'way, direction'. Old High German s/nd' gait, way,  | journey, Fahrt'; Goth\c ga-s/nPa ' travelling companion ', Old Icelandic s/nn/6s., (under the  | influence of common Celtic -ns-, -nt- > -nn-). Old English gesTt^, Old Saxon gisTd, Old Hig

===== 906 Page(s): 906  |  | Root / lemma: septrp {*seR''m-)  |  | Meaning: seven  |  | Note:  |  | Root/ lemma: septrp {* seR"!!-) : seven derived from a mutated Root/ lemma: sueRs, seRs,  |  | kseRs, RsueRs, ueRs{. uRs) : six; common gr.-celt. k"'>p, g"'> b.  |  | Material: Old Indie sapta, Avestan hapta, Armenian evt'n, gr. snra, Latin septem. Old Irish  |  | secht n-, cymr. etc. saith, Gothic Old High German sibun. Old English seofon. Old Norse  |  | s/a^(-/7 preserved after one besides *s/5i//7 stehenden sibunr, /-loss in ordinals sep[t]m-tos  |  | dissimilatory erfolgt; whether septunihe Lex. sal. still gesprochenes seftunox Latinisierung  |  | eines echten *sifun is, stands dahin), Lithuanian septyni. Old Church Slavic sedmb (after  |  | dem ordinals), alb. shtate {* ^e]ptm-ti-\ abstract number formation as Old Indie saptatf-,  |  | Avestan haptaiti-10. Old Icelandic s/ai//7o'" number from 7'); Tocharian A spat, B suk{t);  |  | Hittite s/pfa.  |  | Note:  |  | Gr. ep5opa5iK6^ "belonging to the week' : alb. yai/e "week' common alb. -b- > -v-.  |  | Alb. shtata "seven' from {*£{e]ptm-tf-) is not possible. Anatolian languages show a pattern  |  | similar to alb. So Lycian aitata {* oRtd(u)ta) "eight' : alb. /e/a "eight'; Lycian nuntata'n\ne' :  |  | alb. nanda'n\ne'. Therefore alb. sMata ' seven' derived from a truncated *sa{pjtata' seven'  |  | later Old Indie saptathah, Avestan hapta&a-. Old Saxon sivotho. Old English seofoda,  |  | Lithuanian septintas, also Old Indie saptatf-, Avestan haptaiti-lQ; in alb. -ta, -teare  |  | attribute endings that were solidified in Anatolian and Indie cognates. The attribute suffix -  |  | ta'\s used in the alb. genitive and adjectives.  |  |  |  | ordinals: sept(e)mos\n Old Indie saptama-, npers. haftum, gr. £p5opo(;, dial. £p5£M0(; (die 

===== 905 Page(s): 905-906  |  | Root/ lemma: se[i]6y-. slby-ax\6 : ss6!^-  | Meaning: to strive for a goal  |  | Material: Old Indie s^o/7a//"kommtzum Ziel, bringtzum Ziel, in order', causative sadhayati,  | 5^077^/- "straight, proficient', -sadh-{2. composition part) = jav. -had- "steering', hadroya-i.  | "desire nachErreichung of Zieles' (from *hadra- rw., Indo Germanic *sedh-/-c»-"Erreichung of  | Zieles'); zero grade Old Indie s/icy^Aa- "erfolgreich', s/o'/7y5//"kommtzum Ziel', participle  | siddha-, Perf. s/sSdha- etc.; Avestan as/75 "erfolgreich' {*a-z6'^-na-y, ablaut neologism is  | sadh-\x\ Old Indie sadh-not/ and sadh/'s- ^p\ace, purpose ';  |  | gr.ieu(; ( *sJci^us) "straight (auf ein Ziel gerichtet). Adv. geradeaus', i0u(;, -uo(; "attack,  | undertaking', iOuu) "dringe vor',10uv(jo "make straight'; siOap "immediately, right away',  | £U0uq (from *£i0U(;) "straight'.  |  | References: WP. II 450, SchwyzerGr. Gr. 1, 350.  |
```


## [2026-09-14T01:56:31.748Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'(?=Page\\(s\\):)', t)\nfor b in blocks:\n    if re.search(r'Root\\s*/\\s*lemma:\\s*sem-\\s*3', b) or ('summer' in b[:200] and 'sem' in b[:200]):\n        print('=====', b[:1600].replace('\\n',' | '))\n        print()\nEOF",
 "description": "Find Pokorny sem-3 summer entry"
}
```


### [2026-09-14T01:56:32.980Z] TOOL RESULT

```
===== Page(s): 778  |  | Root / lemma: om- {*houm-)  |  | Meaning: raw, bitter, *sweet  |  | Note: reduced grade oin-  |  | Root/ lemma: om-{*hamef}\ "raw, bitter, *sweet' : Root/ lemma: sem-1\ "to pour' : Root/  |  | lemma: sem-3\ "summer'. Old Indie amia-, ambla-^sour, sorrel, Oxalis acetosella ' : gall.  |  | samor{ios] "summer months', samolus^ sour, sorrel, Oxalis acetosella '.  |  | Material: Old Indie amIa-, ambia- "sour, sorrel, Oxalis acetosella ' (= maked. appo-,  |  | Germanic *ampra-), zero grade amra-m. " Mango tree ', ama- "raw, unripe ' (= gr. u)|j6(;),  |  | amad- " eating raw flesh '; skyth. VN ApaSoKOi from Iran. *amad-aka- " raw meat eater ';  |  | Note:  |  | Phonetically the closest cognate to Old Indie amIa-, ambIa- "sour' is alb. Geg amIa, Tose  |  | emb(e)la "sweet' common alb. shift m > mb. Clearly the cognate of Old Indie amIa- "sour'  |  | derived from alb. Geg a/77a "mother', t'amle^ sour milk (of the mother), breast milk '.  |  |  |  | Armenian zero grade /7^/77Yaw, cruel, savage';  |  | maked. appo- " astringent ', apapu opiyavov Hes.;  |  | gr. u)|j6c; 'raw, cruel, savage', u)[jr|aTn(; " eating raw meat ' etc. (= Old Indie amad-Wxih  | already Indo Germanic contraction from dmo-an6 ed-'eat');  |  | alb. tam/e'{sour) milk', ambele, emb/e' sweet', temb/e' bile ' (article /-);  |  | Latin amarus' bitter'; Old Irish 0/77 >aw', cymr. of 6s., in addition Old Irish umfaje'  | copper, ore' = cymr. efydd^ copper, bronze ' ( *omiJo^\  |  | Germanic *a/77/7/'a- (from *ambra-< *am-ro-) in Dutch a/TT/Oe/"' sharp, bitter, unripe ', Old  | Icelandic apr{*ampraR) 'sharp', Subst. Old English ampre. Old High German ampfaro\  | (Sauer)ampfer '; doubtful 

===== Page(s): 902-905  |  | Root / lemma: sem-3  | Meaning: summer  |  | Grammatical information: (Gen. Sefn-os)  | Note:  |  | Root/ lemma: sem-3: "summer' has certainly derived from Root/ lemma: ghei-2. ghi-,  | ghei-men-, *gheimn-\ "winter; snow' [common satem IE ghe- > se-]. It seems that the  | Hittite-lllyrian name for winter became the Sanskrit name for summer. This discovery  | seems crucial to determine the homeland of Indo Europeans.  |  | Material: Old Indie samai. "Halbjahr, season, year' (= Armenian am), a/-sa-mah'\h'\s year'  | (probably from a Lok. *5/- 55/775/ reshaped, see above S. 286); Avestan ham- "summer';  | Armenian a/77 "year' (= Old Indie sama), a/77a/77 "summer' {*Semerom); Old Irish sam  | {*semo-) and samrad {*Semo-rdto-, above S. 866), cymr. corn, haf, bret. /7a/7K" summer';  | cymr. /7a/oo'"Sommerhaus', bret. havreg^ fallow ', Middle Irish samadm. "Ampfer'; gall.  | samor{ios] "Sommermonaf, samolus' sorrel, Oxalis acetosella ', 5a/775/'a"Ulmensamen';  | remain far off the ibero-rom. a kind offish s5/77ai/C5(Hubschmid. Rom. Phil. 8, 12 f.); Old  | High German sumar. Old English sumorm.. Old Icelandic sumarn. "summer'; as " one-  | year-old animal' Old Icelandic s/mu//'{ one-year-old) ox', s/m/, s/m/rds., Norwegian s/m/a  | "Renntierkuh' (Indo Germanic sem-), Swedish 50/775/ " Ren ntierkalb'.  | References: WP. II 492 f.  |
```


## [2026-09-14T01:56:41.846Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN summer ===\" && grep -n -i \"summer, from ME\\|sumer, fr\\. OE\\|^summer\" KLN_1966.txt | head -20\necho \"=== KLN 1971 summer ===\"; grep -n \"sumor\" KLN_1966.txt | head -20",
 "description": "Grep Klein for summer"
}
```


### [2026-09-14T01:56:41.969Z] TOOL RESULT

```
=== KLN summer ===
37436:summer,  n.,  a  season.  —  ME.  sumer,  somer,  fr.
37438:summer,  n.,  a  large  beam.  —  ME.  somere,  sumer, fr.  MF.  (=  F.)  sommier,  ‘pack  animal,  beam, rafter’,  fr.  OF.  sumer,  fr.  Late  L.  sagmarius, ‘pack  animal’,  fr.  sagma,  ‘packsaddle’,  fr.  Gk. CTdcy(za,  of  s.m.,  which  is  rel.  to  aar-rco  (for *aobqco),  ‘I  pack,  stuff’.  Cp.  OHG.,  MHG. soum,  G.  Saum,  OE.  seam,  ‘burden,  load  of  a beast  of  burden’.  Cp.  also  seam,  ‘measure’, sumpter.
37439:summer  herring.  —  Translation  of  Du.  zomerha- ring,  of  s.m.
37440:summersault,  n.  —  A  var.  spelling  of  somersault, summit,  n.  —  ME.  somette,  fr.  MF.  somete,  fr.
=== KLN 1971 summer ===
23861:OE.  midsumor.  See  mid,  adj.,  and  summer, midwife,  n.  —  ME.  midwif,  fr.  OE.  mid,  with , and  wif,  ‘wife,  woman’.  The  first  element  is  rel. to  Goth,  mip,  ON.  med,  ‘with’,  and  cogn.  with Gk.  pcxi,  ‘between,  among,  with,  after’;  see meta-.  For  the  second  element  see  wife. Derivatives:  midwife,  tr.  v.,  midwifery  (q.v.) midwifery,  n.  —  A  hybrid  formed  fr.  midwife and  -ery,  a  suff.  of  Romance  origin, mien,  n.,  manner,  demeanor,  appearance.  F. mine,  ‘look,  appearance,  mien’,  borrowed  fr. Bret,  min,  ‘beak,  muzzle,  nose’;  prob.  influ¬ enced  in  meaning  by  the  verb  de-mean. miff,  n.,  a  trifling  quarrel;  tr.  v.,  to  put  or  be  out of  humor.  —  Orig.  exclamation  of  disgust.  Cp. G.  muffen,  ‘to  sulk’.
37437:OE.  sumor,  rel.  to  OS.,  ON.,  Norw.,  OHG. sumar,  Dan.  sommer,  Swed.  sommar,  OFris. sumur,  MDu.  somer,  Du.  zomer,  MHG.  sumer, G.  Sommer,  and  cogn.  with  OI.  sama,  ‘season, half-year,  year’,  Avestic  hama,  ‘summer’,  Arm. am,  ‘year’,  amarn,  ‘summer’,  OIr.  sam,  samrad, OW.  ham,  W.  hdf  ‘summer’.  All  these  words  are traceable  to  I.-E.  base  *sem-,  *sam-,  ‘summer; season’.  Cp.  the  second  element  in  gossamer. Derivatives:  summer,  intr.  and  tr.  v.,  and  adj., summer-ing,  n.,  summer-less,  adj.
```


## [2026-09-14T01:56:43.373Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN hamin ===\"; grep -n -i \"hamīn\\|hamin\\|hâmîn\\|hämin\" HRN.txt | head -20\necho \"=== HRN page 280 area ===\"; grep -n \"280\" HRN.txt | head -10",
 "description": "Grep Horn for hamin"
}
```


### [2026-09-14T01:56:43.455Z] TOOL RESULT

```
=== HRN hamin ===
10601:^haminaka^?),
=== HRN page 280 area ===
2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
2757:päda-; arm. otn (H. No. 280).
3026:fästäg 'hinterer, nachher, zuletzt, am Ende' (280) ; bei.
3217:Zcrile 2 (nach Darme steter, Et. ir. I, 280).
3460:(vd. 5 (57)), tacet (vd. 8 (287) flf.), tazad (vd. 8 (280),
5004:drütik courtoous' (West II, 280).
6664:ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
7549:Vergl. Rückert, ZDMG. 8, 280.
10592:Bund.).- 280 -
13271:pänsed 280.
```


## [2026-09-14T01:56:47.857Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10575,10650p' HRN.txt",
 "description": "Print Horn page 280 region"
}
```


### [2026-09-14T01:56:47.909Z] TOOL RESULT

```
102. yursltan 'hungern' (vd. 9 (182) Gl.).
Derartige Verba sind nicht wenige verloren ge-
gangen, die nicht besonders aufgeführt sind, wie
kam(i)8tan, man(i)stan 'bleiben* etc.
H.
103. häj vor dem Imperativ.
Vergl. Nöldeke, Tabarl-Übersetzung, 385 Note 2.
104. hax 'Fußsohle (vd. 8 (219) (221), 9 (107) GL).
aw. ha/a- 'Fußsohle*.
Da der Kommentator keine Glosse macht, so ist
phlv. ha/ vielleicht noch verstanden worden; doch
steht das Wort an der letzterwähnten Stelle in
Awestabuchstaben.
Dasselbe gilt für lia/t 'Schenkel' (vd. 8 (184), Zend-
buchstaben; 9 (82) ff.), aw. haxti-, ai. sdkthi-^ sakthdn
'Schenkel', oss. t. ayd 'Lende' (7).
105. hamestär Gegner, Widersacher, hamestärih (Men.,
Bund.).- 280 -
ap. vergl. hamiiViya- aufrührerisch' ; aw. Jtamaesttir-
Teind\
106. heimln 'Sommer, hänümk 'sommerlich*, häufig.
aw. harn- ') Sommer, hqmln- 'sommerlich' ; ai. samö-
'Halbjahr, Jahreszeit, Wetter, Jahr; arm. am 'Jahr
(H. No. 10), amarw 'Sommer (H. No. 12); ahd. an. sumar
'Sommer .
kurd. havin (H.-Sch.); sar. menj 'Sommer (aus
^haminaka^?),
107. hamkÖH 'synonym* (wörtl. 'zusammenstossend'), vd. 1
(4) u. ö.
Die Erklärung stammt von Fr. Müller, WZKM.
III, 171.
Composita mit harn- könnten eine ganze Reihe als
verloren gegangenes Sprachgut hier aufgezählt werden.
108. hän 1) alt' (vd. 15 (42) mit Awesta-, sonst mit
PehlevTbuchstaben).
aw. hanä" 'alt*; ai. sdna-; arm. hin (H. No. 168).
2) 'anderer* (päz. han),
ap. aniya- 'anderer; aw. ant/a-; ai. anyd-,
oss. d. t. inne, innä anderer' (140).
109. harvisp, oft verschrieben in harvtst 'all, jeder, sehr
häufig, vergl. haroistm,
ap. haruva- + vtspa-; aw. haurva- + vlspa-; ai.
sdrva- -|- vhjva-.
110. häsr 'Wegmass' (Bund.).
aw. hCL^ra-,
111. häva/nd'^o\Q\\, ähnlich*, päz. havand (P.-Vend., Men.).
aw. cwant' 'solch*.
112. häv(i)8t 'Schüler* (aw. a^&rya- übersetzend u. ö.).
aw. hävista- (y. 68, 12; ZPGl.).
113. hejak 'Eimer* (Kärn. 65 Note 3), vergl. he/tan, ib.
np. he:^ wird als PehlevTwort bezeichnet 2).
^) Zu aw. hama vergl. J. Schmidt, Pluraibildungen 209 folg.;
Bartholomae, Arische Forsch. II, 111, 112. Indog. Forsch. 1, 189, 190.
2) Nichts Neues bei Fr. Müller, WZKM. 5, 257.— 281 -
lU. hen *Heer, Schaar ; arm. LW. hm TrsiQdtf'jfjmv^
ATjotrjgiov^ TfeigaTr,!^.
ap. hainä' 'Heerschaar ; aw. ha^nä-; ai. senä'. Im
Iranischen bekanntlich nur von Dämonen gebraucht.
115. hiyiV 'Unreinheit* (AW.-Komni., AV., Bund.), päz. hlhar,
hihir,
aw. hiyra- 'Unreinheit'.
Vorwiegend ritueller t. t. In Pärsenschriften be-
gegnet np. ÄTr, hl (Spiegel, ür. d. P., 201).
116. hol *link'.
aw. havya- 'link'; ai. suDi/d-; arm. aheuk *link' (un-
sicher, H. No. 5).
117. höH 'Morgenröte' (Aw.-Komm.j; vergl. hömstur öst-
lich*, hösbäm ^Tagesanbruch* (Men.).
aw. usah' 'Morgenröte'; ai. ums-.
118. hU' 'gut-'; sehr häufig in Zusammensetzungen (z. B
in hu[ramak, hii/t, hu\tu/s, hu\xtm etc.
ap. u-, UV-; aw. hu-; ai. su-; arm. h- (H. No. 15;3).
Im Neupersischen bisweilen in der Form /ti- erhalten;
vergl. auch np. huMr (oben No. 1098**'") und huweidä
V
'deutlich, klar* (Sahn. I, 282 Vers 15), das wohl zu
```


## [2026-09-14T01:57:07.172Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Pehlevi\\|Anhang\\|ANHANG\" HRN.txt | sed -n '1,40p'; echo \"=== around 9000 ===\"; grep -n -- \"- 2[56][0-9] -\" HRN.txt | head -20",
 "description": "Find Horn appendix section header"
}
```


### [2026-09-14T01:57:07.242Z] TOOL RESULT

```
122:solchen aus dem Pehlevi oder aus modern - iranischen
654:aw. *a (oder nach dem Pehlevi wohl ava) + uz +
660:*) Im Pehlevi auch schon in der kaum hierher gehörenden Be-
1178:*J NatürUch könnte man die Pehleviforraen auch steulk, -sten
1444:') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).- 28 -
2117:zu bürden gestellt; die Pehleviform lautet vartak (Geiger, Yätk.
2529:Eine über das Pehlevi hinausgehende iranische Form
2698:Pehlevi aufgegeben worden; np. pärav alte Frau' ist
4596:*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
4670:Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
7120:scheint im Pehlevi noch /ra-, nicht schon far- gesprochen zu sein.
10049:aw. ahi' *böse* (im Pehlevi aufgegeben), "^akadaeua-
10404:aw. duzgainti') u. v. a. m. Im Pehlevi erscheint nur
=== around 9000 ===
9973:den) es auch der Bedeutung nach nicht passt. Die- 259 -
10062:nicht für richtig.- 265 -
```


## [2026-09-14T01:57:09.451Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10062,10110p' HRN.txt",
 "description": "Print Horn p.265 region to find appendix header"
}
```


### [2026-09-14T01:57:09.507Z] TOOL RESULT

```
nicht für richtig.- 265 -
12. anaiv nicht arisch; boshaft, feindlich*, anainh (Men.).
aw. miairya-,
np. ener schlechter Charakter ist unbelegt (die laut-
gesetzliche Form müsste nEr lauten), die Riväyets
haben arier als ^ungehorsam'.
13. anäklh 'Unheil etc.'
Das sehr häufige Wort ist aufgegeben; das seltene
anäk (AV.) hat sich dagegen im np. näk erhalten
(s. oben No. 1020*»»»).
14. andarvnl Atmosphäre, Luftraum .
aw. *aütarevat/u-; ai. *antarc(lyU',
Im Neupersischen soll endervä {endenväl 'Bedürfniss*
vergl. unter bayisten, oben No. 179) 1) aufgehängt,
hangend; nieder (den Kopf nach unten)' bedeuten.
FJ citiert hierfür als angebliche Belege die beiden
folgenden Verse (Kamal):
^i kl ez her ser-). mö-yl tu etil endercäst (sie)
yeJc sPr-l mö-yt türCL her dö jäidn nem-l bdhdst
Kemäl Ismail.
ger bemihr-i tu myerdäned ztmüne ^) rayträi
göyM ez yem röz-ü seb jCLy-l vey endervüyi vdi
Hekim Qaträn.
2) erstaunt, bestürzt* (mit Vers aus Enverr).
15. angöSttak *Art und Weise' (Men., Bund., ZPGl.).
Die Lesung ist unsicher; West liest neuerdings
(mir völlig unwahrscheinlich) 'angiim-altak und über-
setzt counterpart, similitude* (Bund.). Jedenfalls kann
auch West' 8 erste Erklärung aus angösUan ^umarmen'
nicht beibehalten werden ; np. engösTden existirt nicht.
16. änUan 'herzubringen*.
aw. *Ä + V^iiay-; ai. cL -i [/^yiay- 'herbeigeleiten,
-führen, -bringen, -holen\ Vergl. phlv. nitan.
17. antarmäh 'Neumond'.
aw. aütaremaofiha" 'Neumond'.
') Corrigirt aus zi zemätie^ aber die beiden Zeilen sind wohl nicht
ganz in Ordnung.— 266 —
18. aniifnal ^Kleinvieh*.
aw. anumaya- 'Kleinvieh'. Wohl nur Transcription
des Awestawortes.
19. apavTk 'später, anderer, übrig; der Rest' (päz. aware),
ap. aparam nachher ; aw. apara-, ai. äpara- 'hinterer,
späterer.
20. apastän Vertrauen , sehr häufig auf Gemmen ; arm.
LW. apastan,
skr. upasthäna- 'das Aufwarten, Verehren'.
20***** ajnsfnan nicht sehend, blindlings', nur vd. 13 (145),
aber wegen des Suffixes vielleicht nicht nur um-
schreibend.
```


## [2026-09-14T01:57:14.683Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9973,10062p' HRN.txt | head -70",
 "description": "Print Horn appendix start"
}
```


### [2026-09-14T01:57:14.739Z] TOOL RESULT

```
den) es auch der Bedeutung nach nicht passt. Die- 259 -
hellen Saiten waren wohl oben' auf dem Instrument
angebracht.
682. Np. zlre ist nacli Weber a. eben a. 0. indisches
Lehnwort.
707. Vergl. kauk.-bergjüd. süpiil,
735. Lies simld (Keim auf röd. Sahn. I, 229 Vers 1780;
auch die indische Aussprache lautet suröden),
748. Lies .so, söt (im Reim Sahn. I, 111 Anm. 29, Calc,
257 Vers 129).
753. Zu aw. mirt/a- vergl. bereits Hübschmann, Casus-
lehre S. 196 Anm.
796. Lies aw. ^/modraka-, "^/saüda-,
819. Lies ar. *prasth-fd' statt ^prasth-td-,
847. Der Präsensstamm kün- mit dem Infinitiv kerde findet
sich in der Bedeutung coire' im kauk.-bergjüdischen
(vergl. phlv. kär kartan etc. Hörn, BB. XVII, 265),
dagegen sonst immer der Inf. kurde, kürde, vergl. de-
kürde 'hinlegen', po kurde (pak kerden), fuknrde^
hukurde {ßrö kerden).
909. girift * Verbrechen'.
aw. ägerepta-; phlv. ägraft, päz. agereft.
Salem ann, Shams i Fachrii Ispahänensis lexicon
persicum S. 172 g.
Die np. Lexicographen erklären das Wort als ein
'Verbrechen, bei dem man auf frischer That er-
griffen wird'.
17'VERLORENES SPRACHGÜT.A, A').
1. a-, a//-, un-, nicht-' (« privativumj. Sehr häulig, z. B.
asnr endlos*, a/^ar(i)sn *das Nichtessen , aguftar 'nicht
sprechend' u. v. m.
ap. a- in Anämaka' Monatsname (?) ; aw. a-, an- ;
ai. a-, an-; arm. aw- (H. No. 20).
oss. d. t. «-, ä- (1).
Das Neupersische hat a-, an- aufgegeben (Fälle wie
näb, oben No. 1015, und nägäh, oben No. 1021, sind ver-
einzelt) und ersetzt dieses Praefix durch vorgesetztes
nä' (oben No. 1014) , z. B. phlv. anspä$ 'undankbar
gegenüber np. näsipüs, oder durch be- (247).
2. afd 'trefflich; Wunder (AV., Men.), päz. awd,
np. tifde 'wunderbar , efdlden 'staunen, bewundern* sind
nicht belegt. Ist phlv. afd nur eine Umschreibung von
aw. abda- (vergl. abdötema-, Epitheton der Savanhaväc
und Erenavaö) und die np. Worte wiederum nur falsch
aus dem PehlevT transcribirt ? Der BQ und durch
diesen der PS enthalten eine Menge niemals im Neu-
persischen vorhanden gewesener PehlevT- und Päzend-
worte.
3. äfräH 'Mitteilung, Belehrung (Men.).
aw. ^afrasa-, vergl. paitifrasa', phlv. patfräs (oben
No. 154).
*) Die einzelnen Worte sind in diesem Abschnitt nach unserem
Alphabet angeordnet.- 264 —
4. afsTultan Vernichten; abnehmen', awsiuitan, afstn-
(i)sn.
Scheint ein Causativuni mit der gewöhnlichen phlv.
Endung -imtan (np. dagegen -ämdeN) zu sein. Bar-
tholomae denkt dagegen nach briefl. Mitteilung an
Zusammenhang mit aw. hisidyät etc. (vergl. oben
No. 922).
5. agräl, agre Vortrefflich' (AW.-Komm., Bund.).
aw. ayrya' Vorzüglich ; ai. agriyd",
6. ahöklnltan Verunreinigen, beschmutzen', ähökinttär
(aw. ähitl', vd. 20, 14), ahökm{i)sn (aw. ähiti-) ^).
Nur ähö (Reim: Vis und Rämin, S. 48, Vers 2),
phlv. äliök, ist im Neupersischen erhalten.
7. ahlav *fromm, gottesfürchtig (Nöldeke, ZDMü. 31,
557).
ap. arta- (in Comp.); aw. areta, asa-; ai. ^td-,
8. ahü 1) *Herr'.
```


## [2026-09-14T01:57:28.030Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"asem\\|a-sem\\|siyaman\\|silver\" KNT.txt | head -40",
 "description": "Grep Kent for silver/asem"
}
```


### [2026-09-14T01:57:28.083Z] TOOL RESULT

```
581:ardata- ‘silver’, Av. srezata-; Yezdi ali ‘silver’, from earlier ard-, is not necessarily evidence for OP, since Yezdi is a Kurdish dialect; Skt. rajatd- also has a different initial.
1170:pIE *rjnto-, OP ardala- ‘silver’, Av. orozata-, Lt. argentum, c£. Skt. rajaldn.
1798:$45. NOUN AND ADJECTIVE STEMS WITH SUF- prx. -ta- found in OP are mostly participles ($242), superlatives (8190.1), and ordinal numerals (8204). The remaining examples are aruvasta-, a neuter abstract seemingly formed upon an adjec- tive *aryani- (see Lex. s.v.); XSaérita-, а hypo- corstie to a compound personal name; ardata- ‘silver’, perhaps an -a- extension of a participle in -ni-, cf. Lat. arg-ent-um; dasta- ‘hand’, which can- not be related to any simpler extant root; and three feminine abstracts arsid-, hanalü-, avaslá-, the last two of which are dubious and the third is taken as having acquired concrete meaning.
3316:DPh = Darius, PEnsEPOUIS н: Trilingual, on two gold and two silver plates; now in Teheran. OP 10 lines, Elam. 7, Akk. 8; same text as DH. New York Times, Feb. 9, 1986, 2d news section, page 8; Univ. of Chicago Mag. 284.235, Feb. 1936; Hz. ApI 18-9 No. 6 and Plate 6 (1938).
3356:DH = Darius, HAMADAN: Trilingual, in dupli- cate on a gold and a silver plate; now in Teheran. OP 8 lines, Elam. 7 lines, АКК. 8 lines. The two copies vary slightly in the line-division; our text follows the gold plate. The text is repeated in DPh. JMUnwalla, Jame Jamshed, Sept. 30, 1926; Hz. DLZ 47.2105-8 (Oct. 16, 1926); SSmith, JRAS 1926.433-6; CDBuck, Lg. 3.1-5 (1927); LHGray, JRAS 1927.97-101; JMUn- walla, JCOI 10.1-3 (1927); Wb. 2А 37291-4 (1927); ESchwentner, ZH 6.171-3 (1928); Hz. Memoirs of the Archaeological Survey of India
3381:XH = Xerxes, HaMADAN: OP only, in one line, on a fragment of a silver pitcher. Hz. AMI 2.115-6 (1930); Brd. WZKM 39.83 (1932); Hz. ApI 43 No. 19 (1938); Sen, OPI 161 (1941).
3385:A'I = Artaxerxes I, iNCERTO Loco: OP only, in one line, identical inscription on four silver dishes. Hz. AMI 7.1-8 and 4 Plates (1935); Schaeder, SbPAW 1935.489-96; Hz. AMI 8.6-17, 46-51 (1937); Ву. JAs. 228.233-4 (1936); Kent, JAOS 56.215 (1986), 58.327 (1988); Hz. Ар] 46 No. 23 (1938); Sen, OPT 178 (1941).
4296:{81. 40-5. The silver and the ebony were brought from Egypt. The ornamentation with which the wall was adorned, that from Ionia was brought. The ivory whieh was wrought here, was brought from Ethiopia and from Sind and from Arachosia.
4677:TRANSLATION OF АЧ: Artaxerxes the Great King, King of Kings, King of Countries, son of Xerxes the King, of Xerxes (who was) son of Darius the King; in whose royal house this silver saucer was made.
5068:ardata- sb. ‘silver’: Av. arazata-, Skt. rajatá-, cf. Gk. &pyvpos, Lt. argentum. (S30, §88, $145); Yezdi ait ‘silver’ has Iran. ar-, not r- (Ву. BSLP 30.1.60, Origines 12). See also ardastdna-. arda- tam nsn. DSf 40.
5069:ardastāna- sb. ‘window-frame, window cor- nice’: arda- ‘light’ as in OP ardata- ‘silver’, Skt. rajatd- ‘white’, rjrá- ‘red’, Gk. àpyós ‘shining’ + stāna- ‘place’ (831, §160.Ib; Foy, KZ 35.48; hardly as with Bthl. AiW 193, or Hz. Ар! 74-6); ‘light- place’. ardasténa nsm. DPc.
5171:ula-maiy (§135) DSe 51°; DSf 58; DSj 6°; DSt 9°; XPa 15, 18f; XPd 18f; XPf 41, 45f; XPg 14; XPh 58 (space for w left blank; Lg. 13.303); XSc 5^; A'Pa 23°; Аа 4. uta-Sem (8135) XPh 34, (In restorations there is almost always un- certainty between utà- and uld-.)
```


## [2026-09-14T01:57:29.574Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"asēm\\|asem\\|'sym\\|sym \" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt 2>/dev/null | head -30",
 "description": "Grep MacKenzie/Nyberg for asem"
}
```


### [2026-09-14T01:57:29.753Z] TOOL RESULT

```
PHD.txt:545:pas-dānišnīh [4HLd’nsnyh] anti-knowledge. pasēmāl [psym’l, v. hamemal] defendant, accused. ~ih: (legal) defence. pasen [psyn! | N pasin] final, last. pasox [p’shw' | № ~] = passox. passand [psnd | N pasand] pleasure, liking. passandidan, passand- [psnd-ytn' | M psynd-, N pasandidan] like, approve. ~išn: liking, approval. ~isnig : likeable. passáxt [ps’ht'] test. passaxtan, passàz- [ps’hin', ps’c- | M ps?xt, ps’c-] fashion, prepare; insert; test. ~išn: preparation, constitution. passazag [psck! | M pscg] suitable, fitting. ~ih: suitability. passox [pshw! | M pswx, № pāsux) answer. past [pst' | N ~] low; astr. dejection. pašēmān [pšm?n! | = M, N ~] penitent, repentant. ~ih: penitence, repentance. pašm [psm | N ~] wool. ~ёп [-yn! | N ~in] woollen. pašn [psn'] bond, agreement. pāšnag [p’snk! | N ~a] heel. pāšom [p(”)$zvm) excellent. passing [pšng | N pišing] drop, exudation. paššinjag [pfnck! | N pišanja] drop. paššinjīdan, paššinj- [psnc-ytn' | N pišanjīdan) sprinkle. ~išn: sprinkling. pa&t(ag) [pšt(k)! | J pst] pact, bond, agreement. *pattān [pt’n'] noise, resonance. ~6mand [отта] resonant. pattāyistan [pi?dstn'] = pattüdan. pattüdan, pattày- [ptwtn', ptd- | P ptwdn, M pt’y-] stay, remain, last, endure. pattüg [ptwk'] enduring, patient, persevering. ^АҺһ: endurance, patience, perseverance. paxSag [phšk! | N pasa] mosquito, gnat. 1рау [pdy | N ~] foot; footstep, track. ~ 1: after. *pay [pdy | M pyy, N ~] sinew, tendon. pay [LGLE < А rglh; p'dy | M p'y, N —] foot, leg; foot (12 in.). 1,2 páy-, у, bL? pādan. payādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn. payag [p'd(y)k! | N paya] base, station. paydag [pyt?k! | M pyd'g, N payda] visible, obvious, revealed.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:1534:defence  pahréz, pasēmālīh.
PHD.txt:1536:defendant pasēmāl.
PHD.txt:4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
NYB_vol2_glossary.txt:668:asēmēn
NYB_vol2_glossary.txt:682:asēm [sym] silver 118%. — Borrowed from Gr &onuov; MPrs ’sym (A-H II); NP sim.
NYB_vol2_glossary.txt:3254:rasitan [lsytn'; YHMTWN-tn', ~-ytn'] ras-, pres. Ist p. sg. rasam [YHMTWN-m 2917], lst p. pl. rasēm [YHMTWN-ym 62. 197] ete., subju. 3d p. sg. rasät [YHM- TWN-t' 412]; pt. = pret. 3d p. sg. rasit [YHMTWN-t', YHMTWN-yt' (coin- ciding in spelling with pres. 3d p.sg. and 2nd pl. in -é)]: to arrive, to attain; to reach, to come (0, be 6, 6 peš 4 at, to); to fall to one's lot (6); passim; — andar rasit came to the place 31%; be 6 han i asar rošneh ... apar rasét he ascends up to the Endless Light 73?’ sq.; rasét apar 6 haft- kišvar damik will extend all over the sevenfold earth 51°; apar — to fall upon, to come upon, to assault 197. 726-7; — 6 ham ~ to come together, to meet 431’. 5017, 6122-25; — ruvän + ahlavàn pat buxtan
NYB_vol2_glossary.txt:5811:’sym: asem
NYB_vol2_glossary.txt:7322:pašīmān, pišmān, pižmān, pašīmāni, pišmānī: pasēmānēh
NYB_vol2_glossary.txt:7393:sim: asem
PHD_mackenzie.txt:1216:asem ['sym I = M, N sim] silver.
PHD_mackenzie.txt:4082: pasemal [psym)l, v. hamemal] defendant, accused.
PHD_mackenzie.txt:4103:paseman [psym'n l I = M, N .......] penitent, repentant.
PHD_mackenzie.txt:4540:sem [sym I N -] = asem.
PHD_mackenzie.txt:5908:accused pasemal.                          aged pir.
PHD_mackenzie.txt:6363:   pasemiilih.                              destroyed anast, miidag, tabiih, wany;
PHD_mackenzie.txt:6365:defendant pasemiil.                        destroyer, destructive kastar, zadiir.
PHD_mackenzie.txt:7232:pain bes, dard, pim.                   penitence petitigih, pasemanih.
PHD_mackenzie.txt:7233:painless adard.                        penitent petitig, paseman.
PHD_mackenzie.txt:7442:repentance abaxsih, pasemanih.           reward mizd, padiisn, diisar.
PHD_mackenzie.txt:7443:repentant abaxs, paseman.                rhinoceros karg.
PHD_mackenzie.txt:7582:silver (a)sem; (a.) asemen.                   slope, v. acclivity, declivity.
PHD_mackenzie.txt:8596:paseminih         -"'"U t""6\)U Q)      pardag                      \~~Q)
PHD_mackenzie.txt:8597:paseman                 \~Q)            pambagcn                 \~cU
PHD_mackenzie.txt:8606:passinJisn         ,~ ' \ t"'U CU       pasemal
PHD_mackenzie.txt:8608:pasm                       ~V           pasemalih             ~v
PHD_mackenzie.txt:11574:asemen               ,~           amarg                   ~
```


## [2026-09-14T01:57:46.853Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"siyam\\|siyām\\|sim-\\|Gk\\. .sem\\|asēm\" KNT.txt | head -20; echo \"=== page markers ===\"; grep -n \"^\\s*20[5-9]\\s*$\\|\\[pdf page\" KNT.txt | head -20; echo \"=== struct ===\"; awk 'BEGIN{RS=\"\\f\"} {print NR\": \"substr($0,1,60)}' KNT.txt | sed -n '1,10p'",
 "description": "Grep Kent for siyam and page structure"
}
```


### [2026-09-14T01:57:47.981Z] TOOL RESULT

```
844:АЧ hya (пега. for gsm.) imam (asm. for nsm. iyam) bdtugara siyamam (asm. for nsm. -ma).
994:§72. Tue PIE Long DiPHTHONGS appear in OP as @ and du, corresponding to the short diphthongs ai and au; they are easily identified by their writings, except when they are initial, in which position they are ambiguous with the short diphthongs. There are the following oc- currences: waipasiyam ‘his own’, ef. watpasiyahyd with
1107:OP hasiyam ‘true’, Skt. satyám.
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
2047:Nt. Nom. Sg. zsacam, dusiyaram, ardatam, darant- yam, aruvastam, dàtam, Sakatam, kartam, visam, kamnam; aec. xsagam, stánam, daraniyam, aru- vastam, kartam, visam, uvdipasiyam, uvaspam, probably casam.
3495:47 : Madam : uta : атуда : dahy&va : hauv : àyasatà : uvaipasiyam : акша : hau
3838:44 yafiya : Auramazd&ha : ragam s eartaiyaly : уаба : ima : hasiyam : пау : duru
5204: wüipasiya-, same as preceding, with vriddhi in initial syllable (§126; MB Gr. §298); but wai- may be an error for uvai-, or wai- for wäi- (§53). uvdipasiyam asn. DB 1.47.
=== page markers ===
5857:206
=== struct ===
1: Google
This book is provided in digital form with the permis
2: ien
=
vw
es cos
ut T
s$
[4 ^s Ж $^ Ido" PH
4
```


## [2026-09-14T01:57:53.025Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"siyamam\\|bātugara\\|batugara\\|b&tugara\\|bdtugara\" KNT.txt | head; echo \"=== lexicon s ===\"; grep -n \"^siyamam\\|siyamam \" KNT.txt | head",
 "description": "Grep Kent for siyamam"
}
```


### [2026-09-14T01:57:53.290Z] TOOL RESULT

```
844:АЧ hya (пега. for gsm.) imam (asm. for nsm. iyam) bdtugara siyamam (asm. for nsm. -ma).
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
4675:АЛ = ARTAXERXES I, INCERTO LOCO. Artaxfaci : XS : vazraka : XS : XSyinam P E DHyünàm : XéayarSahya : XShyà : puça : XSayarsahya : Dàrayavausahy& : XShyà : риса : Haxamanisiya : hya : imam : batugara : slyamam : vidiya : karta
5365:gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
5723:batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
=== lexicon s ===
844:АЧ hya (пега. for gsm.) imam (asm. for nsm. iyam) bdtugara siyamam (asm. for nsm. -ma).
```


## [2026-09-14T01:58:00.116Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5850,5890p' KNT.txt",
 "description": "Print Kent lexicon around page 206"
}
```


### [2026-09-14T01:58:00.170Z] TOOL RESULT

```
ra”ga- sb. ‘speed, haste’: Av. rang- "leicht, flink werden’ (Bthl. AiW 1511), Skt. rdhale ‘has- tens, speeds’, rahas- nt. ‘speed, quickness’ (for fur- ther connections, see Uhlenbeck, Wrtb. d. altind. Sprache 241). ragam asn. (or asm.?) as adv. (§143.1, $191.IIT) DB 4.44, perhaps with develop- ment to ‘eagerly’ or ‘confidently’.
Raga- sb. ‘Rhages’, a district in Media: Elam. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-14T01:58:07.912Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5890 && NR<=5960' KNT.txt | grep -n \"siy\\|^2[01][0-9]$\\|sim\" ; echo \"--- page markers ---\"; awk 'NR>=5840 && NR<=6000 {if ($0 ~ /^[0-9]{3}$/) print NR+5839\": \"$0}' KNT.txt; echo \"--- find 209 ---\"; grep -n \"^209$\\|^208$\\|^210$\" KNT.txt",
 "description": "Locate Kent page 209"
}
```


### [2026-09-14T01:58:09.039Z] TOOL RESULT

```
--- page markers ---
11696: 206
--- find 209 ---
```


## [2026-09-14T01:58:12.206Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5890 && NR<=5990' KNT.txt | grep -n -i \"siyam\\|silver\\|^ *2[01][0-9]\" ; echo \"====\"; sed -n '5890,5905p' KNT.txt | cut -c1-200",
 "description": "Search Kent s-section"
}
```


### [2026-09-14T01:58:13.327Z] TOOL RESULT

```
====
```


## [2026-09-14T01:58:15.772Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l KNT.txt && sed -n '5885,5889p' KNT.txt | cut -c1-300",
 "description": "Check Kent file end"
}
```


### [2026-09-14T01:58:15.828Z] TOOL RESULT

```
5868 KNT.txt
```


## [2026-09-14T01:58:20.566Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json; d=json.load(open('refs_online.json')); print(json.dumps(d['KNT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\"; echo ===; sed -n '5860,5868p' refs/KNT.txt | cut -c1-400",
 "description": "Check KNT/BQT/MON ref metadata"
}
```


### [2026-09-14T01:58:21.677Z] TOOL RESULT

```
Exit code 1
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
 "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF

... [2075 characters truncated] ...

g, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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
(eval):5: == not found
```


## [2026-09-14T01:58:25.638Z] TOOL CALL #26: Bash

```json
{
 "command": "timeout 180 python3 tools/ref_page.py KNT:209 2>&1 | head -60",
 "description": "Fetch Kent page 209"
}
```


### [2026-09-14T01:58:26.733Z] TOOL RESULT

```
no scan of KNT covers printed page 209 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:58:33.733Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && timeout 120 curl -sL \"https://archive.org/metadata/oldpers\" -o meta-443-knt.json && python3 -c \"\nimport json;d=json.load(open('meta-443-knt.json'))\nprint(d.get('server'),d.get('dir'))\nfor f in d['files']:\n    if f['name'].endswith(('djvu.txt','_djvu.xml','.pdf')): print(f['name'], f.get('size'))\n\"",
 "description": "Get archive.org metadata for Kent"
}
```


### [2026-09-14T01:58:35.615Z] TOOL RESULT

```
ia800101.us.archive.org /20/items/oldpers
oldpers.pdf 16183299
oldpers_djvu.txt 944060
oldpers_djvu.xml 12640802
```


## [2026-09-14T01:58:38.552Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && timeout 180 curl -sL \"https://ia800101.us.archive.org/20/items/oldpers/oldpers_djvu.txt\" -o knt443.txt && wc -c knt443.txt && grep -n -i \"siyamam\" knt443.txt | head",
 "description": "Download Kent djvu text and grep siyamam"
}
```


### [2026-09-14T01:58:40.854Z] TOOL RESULT

```
944060 knt443.txt
4030:iyam) bdtugara siyamam (asm. for nsm. -ma). 
6373:dubious siyamam. 3 
29160:siyamam adj., asm. for nsm., ‘made of silver’,
```


## [2026-09-14T01:58:43.044Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && sed -n '29140,29200p' knt443.txt",
 "description": "Print Kent siyamam entry"
}
```


### [2026-09-14T01:58:43.125Z] TOOL RESULT

```
si"kabru- sh. ‘carnelian’: Elam. $7-/n-qa-ab-ru- 
iš, Akk. gi-in-ga-4--ru-ü (§6, §75.V, §116, §153.1; 
JAOS 54.57-8). For meaning, ef. Bleichsteiner, 
WZKM 37.101-3; Konig, Burgbau 62-3; Kent, 
JAOS 53.18, 54.37-8; ‘cinnabar’, Hz. AMI 3.64.5, 
ApI 303-5; ‘serpentine’, Gray, AJP 53.68-9. st- 
kabrus nsm. DSf 87. 


Sikaya^wali- sb. ‘Sikayauvati’, a fortress in 
Media: Elam. ši-tk-ki-ú-ma-ti-iš, АКК. sik-kam- 
u-ba-at-ti-’, Possibly *sika-yas-vati-, fem. adj. de- 
rived from ikä- (q.v.; also §9.1, 587, $152.II, 
$156.11, $157); therefore ‘Fort Rubble’ from a 
wall of broken stones and mortar. Cf. Hz. AMI 
3.55-6. | Sika|yaluvati$ nsf. DB 1.58. 


siyamam adj., asm. for nsm., ‘made of silver’, 
АЧ; characters clear, but word dubious ($55.11, 
§56.V, $116, 5149.1). Apparently for NPers. stm 
‘silver’, from Phl. asém, borrowed from Gk. &enuov 
'(unstamped) silver’, NGk. атш ‘silver’; but this 
seems anachronistic. Hz. ApI 296-9 (also AMI 
7.2-3, 8.10-7) normalizes saiymam: against au- 
thenticity of the inscription, cf. Schaeder, SbPAw 
1935.489-96. 


Sugda- Suguda- sb. Sogdiana’, a province of 
the Persian Empire: Elam. $u-ug-da, Akk. su-ug- 
du, Gk. Eoyóuiv (822, $103.IV, §116, $128). Sugda 
nsm. XPh 21. Suguda (8128) DB 1.16; DNa 23; 
DSe 22°; DSm 9°. Sug"da (822) DPe 16. Sug- 
dam asm. DPh 6; DH 5. Sugudá absm. DSf 38. 


skauét- adj. ‘poor, weak, lowly’: Turfan Phl. - 


Soh; cf. §6, §116, $152.I, $190.IV, JAOS 56.219- 
20, 58.324; Ву. JAs. 223.244-5; Hz. Арі 305-10. 
Initial s is clear in photographs of DNb. skawh8 
nsm. DNb 8f. skaufim asm. DSe 39f; miswritten 
fkaurim DB 4.65.  skaufai$ gsm. DNb 10. 


Sku^za- sb. ‘Skunkha’, a Scythian rebel: 
Elam. ?ikun-qa. (9100; 58111; $110). Skuza 
nsm. DB 5. 27; DBk 1f. 


Lr 


210 


Skudra- adj. 'Skudrian'; mase. as sb.,
```


## [2026-09-14T01:59:02.065Z] AGENT

Kent p.209 found. Now let me check the Persian sources for sīm.


## [2026-09-14T01:59:04.662Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor leaf in (671,672,673):\n    p=pages[leaf]\n    print('==== leaf',leaf,'printed~',leaf+540)\n    print(p[:1500])\nEOF",
 "description": "Print BQT vol2 leaves around printed p.1212"
}
```


### [2026-09-14T01:59:05.840Z] TOOL RESULT

```
leaves 684
==== leaf 671 printed~ 1211
  ‫سی لحن‬                                                                                    ‫‪ ۷۵۷‬اس‬

 ‫کوبند درکوه و صحرا کهآب سیل آارا کنده‬               ‫و مشنك (‪ )۱‬باشد ‏ و زردی غله زار را لیز‬
‫ورخنها در آن افکنده باشد و رآنخنها را یز‬                                                         ‫گوبند ‪.‬‬
                          ‫سیلاب کند خوالند ‪.‬‬
                                                      ‫ون لام‪.‬‬
                                                            ‫سكکو‬
                                                               ‫ا‬                ‫ح‬
                                                                                ‫‪-۱‬‬‫فت‬
                                                                                   ‫بگل‬
                                                                                     ‫سی‬
 ‫سیالان = بکر اوژرثانی مجهول‌بروزن‬                     ‫است که علت و زردی دوی‬              ‫کك‬  ‫سنییآخر‬‫بمع‬
‫یلان » شیره را کوبند که از خرمای رسیده‬                                                    ‫عله زار باشد ‪.‬‬
‫بکد ‪ - ۴‬و لوعی از دوشاب هم هت ‪ -‬و در‬

 ‫عربی‌نام شخصی بوده ‪ -‬وبختح اول نام ولابتی‌است‬          ‫‪ -‬بكر اول وثالث بورزن‬             ‫سیکی ‏‬     ‫‪۱‬‬
 ‫از آنجا آورند ‪7‬‬    ‫مشهور ® که دارچنی خوب‬              ‫د کی »شبیلرغتازی‌بمعتی شراب ویدالهةٌ شراب‬
‫و بعربی جاری شدن ورو'ن کردیدن آپ وشراب‬                 ‫رآمده است چنانکه بادهکه شراب‬
                                                                  
==== leaf 672 printed~ 1212
  ‫سوه اس‬                                                                                                ‫سيلك‬
‫‏‪ ٤4‬مك مالی » ‪ -6۲‬مهر بانیو برامھر گکائی‬           ‫بود و از برای خسروپرویز می‌تواخت ‪ ۰ ۱‬و دام‬
  ‫اافوسی»‪ -۷۲ .‬فوبهاری »‬       ‫همگفته‌اند ‪- ۰‬‬            ‫آنها بترییب حروف ابجد بدین تفصیل ‪:‬‬
‫‪ -۸‬لوشین باده » و بادة نوشین هبنمظر آمده‬           ‫جپان هم‬         ‫و ابرا آرایش‬      ‫آراش خورشد‬            ‫‪-۱‬‬

‫است ‪٩۲ ۰‬‏ ‪ -‬نریموز » ‪۳‬ل‪۰‬خ‪-‬جیر گالی »‬                ‫اورنگی »‬       ‫‪۳‬‬   ‫‪ -۲‬آهین جمشید ‪,‬‬              ‫کگفته اند ‪.‬‬

 ‫وشیخ نظامی درخسروشیرین ن کراینها کرده‌است‬          ‫*‪-‬حقه‬         ‫قتدیی‪.‬‬
                                                                       ‫اتخ‬
                                                                         ‫‪ ۰‬هطد‬                 ‫رین‬
                                                                                                 ‫یاغ‬
                                                                                                   ‫‪۸‬ش‪ -‬ب‬
 ‫و سه نام از اننها را کهآ بین‌جمشید وراحروح(‪)۱‬‬
                                                    ‫‪-‬مش جان‬
                                                          ‫را‬‫اح روح (‪۸ ۰ )۱‬‬
                                                                         ‫ر‪-‬‬‫کاوی ‪٠‬‏ ‪۷‬‬
 ‫و وبهاری باشد نیاورده‪ .‬اما چپارنام دبگر که‬         ‫آوارا رامش جخهوانانحدمه‌اند ‪٩- ۰‬‏ سبزدر‬
 ‫سناوزروزوغنچة کبك‌دری وفرخ روز و کیضروی‬

==== leaf 673 printed~ 1213
                                                                                         ‫—‬   ‫=‪0۱ 4-‬‬
 ‫سای‬



‫ه را گویند ‪ ۱‬اسزبان و آحوان | هم حت درم دارکه آارا ماهی هشمی‌ممیگویند‬
                                                                    ‫رهمو‬
                                                                       ‫کل‬
                                                      ‫ووسفندان وکاوان و امثالآنا ‪ -‬وبز بان هندی‬
                                                                                              ‫گ‬
                                                     ‫بافنة ریسمالی باثد شبیه بمامل وبیشتر درولابت‬
                                           ‫سیم‬       ‫دکن شود وآنرا یله با شین نقطه دار یز‬
                                                                                             ‫کویند ‪.‬‬
                                                     ‫سیلی = بروزن فیلی‪ .‬آست که‌انگشتان‬

‫بناقشطینمدار © ‪ -‬و بسی گویند نراومدخانه‬              ‫دست را راست کنند و بهم بچسبانند وتبغ‌وار بر‬
‫ابیت که آن ماهی در آن رود خاله مبباشد ‪-‬‬              ‫گردن مجرمان گوناحکاران وبی ادءان زنشد؟ >‬
  ‫و بمهنی رمز وایما واثاره ‪ ۷‬هم آمده‌است ‪. ۷‬‬          ‫و اینکطیانجه سرصالیسگویند غاطاست ‪. ۴‬‬
‫یو»ه را‬
      ‫جتاب‬
         ‫سیماب *‏ بروزن پی‌‬                                                   ‫سیم ب‬
                                                     ‫=فتح اول و الی بورزن بقم »‬
‫گوبند ومعرب آن زیبق باشد و جزواعظم! کسیو‬              ‫چوبهایی است که ب
```


## [2026-09-14T01:59:16.227Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in (673,674):\n    print('==== leaf',leaf)\n    print(pages[leaf])\nEOF",
 "description": "Print full BQT leaves 673-674"
}
```


### [2026-09-14T01:59:17.336Z] TOOL RESULT

```
==== leaf 673
                                                                                         ‫—‬   ‫=‪0۱ 4-‬‬
 ‫سای‬



‫ه را گویند ‪ ۱‬اسزبان و آحوان | هم حت درم دارکه آارا ماهی هشمی‌ممیگویند‬
                                                                    ‫رهمو‬
                                                                       ‫کل‬
                                                      ‫ووسفندان وکاوان و امثالآنا ‪ -‬وبز بان هندی‬
                                                                                              ‫گ‬
                                                     ‫بافنة ریسمالی باثد شبیه بمامل وبیشتر درولابت‬
                                           ‫سیم‬       ‫دکن شود وآنرا یله با شین نقطه دار یز‬
                                                                                             ‫کویند ‪.‬‬
                                                     ‫سیلی = بروزن فیلی‪ .‬آست که‌انگشتان‬

‫بناقشطینمدار © ‪ -‬و بسی گویند نراومدخانه‬              ‫دست را راست کنند و بهم بچسبانند وتبغ‌وار بر‬
‫ابیت که آن ماهی در آن رود خاله مبباشد ‪-‬‬              ‫گردن مجرمان گوناحکاران وبی ادءان زنشد؟ >‬
  ‫و بمهنی رمز وایما واثاره ‪ ۷‬هم آمده‌است ‪. ۷‬‬          ‫و اینکطیانجه سرصالیسگویند غاطاست ‪. ۴‬‬
‫یو»ه را‬
      ‫جتاب‬
         ‫سیماب *‏ بروزن پی‌‬                                                   ‫سیم ب‬
                                                     ‫=فتح اول و الی بورزن بقم »‬
‫گوبند ومعرب آن زیبق باشد و جزواعظم! کسیو‬              ‫چوبهایی است که برزسگران بر دوطرف چوبی‬
‫است‌بلکه روح |کسیروروح جمیع اجاداست ‪٩‬‏‬               ‫که بر گردن گاوزراعت گذارند بندند ‪ -‬وبکر‬
      ‫‪.‬‬   ‫و بمعنی خیره وبی‌حیا هم‌آمده است‬   ‫‪-‬‬       ‫اول بروزن جیم » نقره راکوبند ‪ - ۴‬ونام‌ماهیی‬

                           ‫‏‪ - ٩‬قس‪ :‬فیله‪ :‬بباغ اندرکنون مردم لبرد مجلس ازمجلس‬
           ‫براغ ادر کنون آهو برد سیله اسزیله ‪.‬‬

  ‫‪ ۴‬ولف «سیلی» رادرشاهنامهبممنی(ضربت با کف‌دستبازک)رفته (فهرستشاحنامةولف)‪:‬‬
             ‫بیلی و مشتش همی کوفتند‬             ‫همه کمتران زو برآشوفتند‬
               ‫از آن لیمةٌ روز تالبم شب‪.‬‬                ‫و نکشاد لب‬      ‫همه خوردسیلی‬

  ‫‪ - ۴‬درزیان کنولی بمعنی طیااحه استعمال‌شود‪.‬‬                 ‫«شاهنامة بخ ج ‪۹‬ص ‪۵۲۸۲٩‬‏ ‪.‬‬
 ‫‪ = ۴‬اوستا۔ ‪ , 2۳15‬قس_‪116is 4۲‬‏ (مشت*‪ )۰۰۲۱ ۱‬؛ هندی باستان ‪4¢ 4¥‬‬
 ‫(تیربوخ) » ارمنی ]"‪5‬ع‪( 101۵‬چوب بوغ کاودر) » پپلوی ‪( 0153‬هره) «اسشق ‪ ›4۷‬ورك ‪:‬‬
  ‫حوبشمان ‪ , 8۱۲۷‬درفارسی ‪ 4‬از اول‌کلمة (بهلوی)حذف شده «دهازله ‪ ۸۸۱‬اما«سمین؟ دریپلوی‬
   ‫آمد|رك‪ :‬سیم ] » اورامالی "‪( 1115‬رشتة شره) «‪ .۵‬اورامان ‪۹۲۱٩‬‏ برخی از مسفقان معاصراصل‬
  ‫و‪۰‬ص‪٠۹‬‏ ‪۱‬ببعد‪ .‬تقی‌زاده) وآنرا‬
                              ‫شمار ‪۱ ۹‬‬
                                     ‫و‪۲‬‬‫ص ‪۲‬‬           ‫ار‬
                                                      ‫شلم‪4‬‬
                                                         ‫«سیم» را بوئالی دانند (محلة داد کا ا‬
                                  ‫کمبر‌از‪ 2 :‬علامت نفی و ‪:( 2015‬شانه‌نهاده » عگلاذمت‬
  ‫اشته) (رك‪ :‬فرهنگه بونانی ‪-‬انگلیسی‬
  ‫لیدل واسکات) جمماً بمنی ( قر ) نامسکوله (از افادات شفاهی استاد بنونیست) ورك ‪ :‬ااجماهر‬
  ‫® = ‪ smarbA arb am‬ازماهیان استخواندار«دربای خزر‪.‬یریمالی‬                         ‫بیرولی ص ‪۲٤۲‬‏ ‪.‬‬
  ‫‪- ۷‬وایز رشته‌های باريك فلزی را «سی»‬         ‫‪ ۱‬رك ‪ :‬حیمیار ‪.‬‬                       ‫‪۸‬‏ ‪. ۲۵۱ ,‬‬
  ‫گوبند‪ .‬مفتول» واین‌معنی درزمان‌مولف معمول‌بوده ‪ .‬رك‪:‬سیم کش‪ .‬ورك‪ :‬ح‪ .۸‬سیم یک راول وم‬
  ‫‪- ۸‬از‪ :‬سیم‪ +‬آب؛ وسیم‌خودبمعنی جیوه مده ‪:‬‬                       ‫م‪.‬‬  ‫وه»‪.‬‬‫سی« س‬
                                                                             ‫‪:‬برا‬
                                                                                ‫كیبی‬
                                                                                   ‫ردارت‬
                                                                                       ‫دوم‌مشند» عد‬
       ‫يشت و رو باشد مکی آبینةبی‌سیم را‪.‬‬                     ‫سیم وزر دلیایرستان رامنافق میکند‬
  ‫‪۳‬‬   ‫‪١‬ص‏ ‪۲4‬‬      ‫«فرهنگك اظام» ورك ‪ :‬ما‬         ‫طاهروحید‪.‬‬


            ‫همجو سیماب برکف مفلوج‪. ‎‬‬                         ‫‪ - ٩‬شب بيدار ویندودید؛ من‬
  ‫یجافآ ‪ ,‬تفل« ‪‎‬یرف ‪. ۰۲۷‬‬

==== leaf 674
    ‫ه‬
    ‫ا ‪۱۷‬‬
       ‫مه‬                                                                                               ‫سیماب آتشین‬
‫سیما هنگ = با ها بروزن مینارنگه»‬                              ‫شبي|ن = بکس بای ابجد ‪.‬‬
                                                                                   ‫تها‬
                                                                                     ‫سی‬
‫رستنیی باشد دوایی و آلرا بعربی قثاه البری‬
‫خوالند ممتی خبار صحرایی وقثاء الحمار همان‬
                                                                                          ‫حم میکوبند بحذف نون ‪.‬‬
                                                              ‫سیماب آ تشين سربفتح‌سین سعفص‬
                                                              ‫و سکون رای قرشت (‪.)۱‬بمعنی سیماب آتدین‬
 ‫سیم بر= بفتح بای ابجد (‪ )۲‬سوکون‬                                       ‫ازخورشد عالمآر| باشد‪.‬‬                    ‫نابه‬
                                                                                                                   ‫که‬‫است ک‬
‫رای فرشت (‪.)۳‬اشاره‌ببدن سفید است‪- ۳‬ویزبان‬
‫گیلانی در سرای خود راگونند ودرجای‌دیگر‬
                                                              ‫سیهاب پا ‪ -‬بابای فارس‌بالف کشیده‪:‬‬
‫مود ‪۴‬ے و کنانه ازجوان‬         ‫مهمان‌خانه نوشته شده‬
                                                              ‫کتابه از مردم گربزیا باشد همجو غلام و طفلی‬
                                                                                             ‫که از مکتب بگریزد ‪:‬‬


‫سیمیر اسو اره (‪)4‬سبفتم همزه‌وسکرن‬                              ‫سیماب دگروش ‪ -‬کنابه اکزی‬
                                                             ‫او کرباشد وچیزی شنود ‪ -‬و نا‬                            ‫وهش‬
                                                                                                                      ‫کت ک‬
                                                                                                                         ‫اس‬
‫سین بی نقطه (ه) و واو بااف کشید» و برای‬
‫نکران عرب را‬
           ‫فرشت زده )‪(٩‬‏ » بزنان گیلان و‬                                               ‫وری را نکیوزند‪.‬‬
                                                                                                     ‫شنوایی ک‬
‫وم‌خوارباشند‬       ‫گونند که هر درخانهٌ بادشاهان مر‬            ‫کنابه از غردد باشد‬                  ‫سیماب دل‬
                        ‫دافته باشنف ‪۳‬‬   ‫واسب وسلاح‬            ‫‪-‬مده‬
                                                                 ‫یمنی قحبهدل " چهغربمعنی قحبههم آ‬
‫=نابه از جوان شدن‬
                ‫سیم بر شدان ک‬                                                    ‫است ‪ -‬و مردم بی‌جگر ب‬
                                                             ‫وی‌دل وترسنده ولرزنده‬




‫سیهتاخ ‪ « ۷‬بفواقانی بالف کشیدء‬                                ‫سمات شدن = کنابه ازسقرار شدن‬
‫باشد‬   ‫خل‬      ‫و بخای لفطه دار زده (‪ » )۷‬بمعنی‬                                   ‫و گربختن ونایدید گردیدن باشد‪.‬‬
 ‫وآن منم سابل است بوجهی از وجوه بواجود‬                        ‫سیماذه ‪ = ۱‬بذاال نقطه دار بر وزن‬
                                     ‫واستطاعت‪.‬‬      ‫قدرت‬      ‫شیرازه » لوعی از سنگه باشد که بجهت صیقل‬
                                                                    ‫کاربها بکار آید ‪ -‬وسنباده را کنفزته‌اند ‪.‬‬
‫کشیده ویغای نقطه‌دارزده » چیزی ازخدای(‪)۸‬‬                         ‫> نغال‬
                                                              ‫مامی‬           ‫سیمالك ‪ -‬بر وزن ببیاك‬
                                      ‫خواستن باشد ‪.‬‬                                                         ‫‪۰‬‬       ‫ات‪۳‬‬   ‫موده‬




       ‫را‪.‬‬    ‫وسکون‬     ‫‏)‪ (e‬حك‪:‬‬                                                 ‫(‪ )۱‬چك‪ :‬وسکون را ‪.‬‬
               ‫‪۰‬‬   ‫وبرا رده‬   ‫(‪)+‬‬            ‫(‪ )e‬جك‪ 0" :‬بی لطه‪۰ ‎‬‬                 ‫‏(‪ )٤‬چش ‪ :‬ار (!)‬
                                            ‫(‪ )۸‬چش ‪ :‬خدایتمالی ‪.‬‬                  ‫‪5‬‬   ‫و بضا زده‬   ‫جك‪:‬‬       ‫)‪۲‬‬




                                              ‫‪٠‬‏‬   ‫و رك‪ :‬صیماژه‬    ‫«مضانه»‬   ‫ر‬    ‫«سمباده؟‬       ‫مصحف‬   ‫‪-‬‬       ‫‪۱‬‬


  ‫ما کف ‪۰‬‬     ‫وس‬    ‫ودستار سىزك‬     ‫دممصر‬   ‫دهی‬            ‫بمستحقان ندهی هرآ نجه داری وباژ‬                      ‫‪۳‬‬

       ‫‪۰‬‬     ‫ا‪.‬ت‬    ‫‪ - ۳‬مراد دأرندة بدن مد‬                        ‫عنصری بلخی‪« .‬لغت فرس ‪4۵۲٩‬‏ ‪.‬‬
                                    ‫اسوار‬
                                                 ‫اکنون در گیلکی معمول نیت ‪۰‬‬
                                            ‫ر کث‪ :‬سمبر‬
                                                                                                                ‫‪۴‬‬
                    ‫»زبرساخته های فرقة آنرکیوان ‪.‬‬
                                                ‫‪ 1‬ظ ا‬                                 ‫مین‬    ‫‪:‬‬    ‫رک‬            ‫‪۵‬‬



                                                       ‫‪ - ۷‬از دساتیر ‪« .‬فرهنگه دساتبر ‪٩ ۸۵۲‬‏ ‪.‬‬
```


## [2026-09-14T01:59:46.229Z] AGENT

Now let me render the printed page and fetch web sources.


## [2026-09-14T01:59:49.390Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 443 -l 443 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg443 && ls -la pg443.png",
 "description": "Render PDF page 443"
}
```


### [2026-09-14T01:59:51.556Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77924 Sep 13 21:59 pg443.png
```


## [2026-09-14T01:59:52.375Z] TOOL CALL #33: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sem-\" \"https://en.wiktionary.org/wiki/summer\" \"https://www.etymonline.com/word/summer\" \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sen-\" \"https://www.etymonline.com/word/senate\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 443 verification\" 2>&1 | tail -2; done",
 "description": "Archive web sources for page 443"
}
```


### [2026-09-14T01:59:57.931Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/00537653f130356c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4fdb50b6ca2c2148.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/86361ce6b3cc6827.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b726e506f213ce7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f058fa075f4731f1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/43e013b4e13e384c.txt
```


## [2026-09-14T01:59:59.756Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg443.png"
}
```


### [2026-09-14T02:00:00.540Z] TOOL RESULT

```

```


## [2026-09-14T02:00:00.538Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:00:32.879Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT hana ===\"; grep -n \"hana-\\|hanō\\|hana‑\" BRT.txt | head -10\necho \"=== BRT hama summer ===\"; grep -n \"ham-\\b\\|hama- \" BRT.txt | head -10\necho \"=== BRT Sommer ===\"; grep -n \"Sommer\" BRT.txt | head -20",
 "description": "Grep Bartholomae for hana/hama"
}
```


### [2026-09-14T02:00:32.975Z] TOOL RESULT

```
=== BRT hana ===
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
6340:Etwa;  'die  St&tze,  den  Pfeiler  des  Aia  bi\- dend';  ai.  ilambhana-  n.;  vgl.  PDs.  tatiibam 'ramme  Pßhie  ein'  (S  S3.  3)?
7380:•  p.  ä-vahana-  n.  'Wohnplatz,  Flecken': •t  nüm^  'tiam  armaniyaiy  Bh.2.7.
7381:Znm  V.  '^■ah-.  —  ai.  'vasana-  n.  'Wohnen' (vgl.  ävaiathä-  n. 'Wobnplati');  vgl.  arm.  1,W. aoan  'Flecken'  (aas  mp.  *äv3n  aus  ap.  "ävä- hana-,  GltPb,  /  b.  96).
7786:•  j.  aohana-  Adj,  (fem.  °ml-),  PPM.:  s.  'ä/i-,
8377:Vgl.  darjfö.upa!lay.  mit  S  SOg.  —  Vgl.  ai. upa4lhana-n.  'Hinzutreten' (usw.);  inp.  apaslaii, arm.  LW.  apaslan  'Vertrauen'.  —  Wegen  Pü. s.  tn  ufailäA'  mit  Ko.
9870:BJ.  goflhana-  Adj.,  gasthäna-  n.;  mp.  (Pü.j ^slän.  —  I)  So  Jpi,  Mfa;  NA.  hat  ^avö.ü'. —  ä)  zSt.  s.  HHr5.slSna.  No.   l.
18167:•  \.  frshana-  Adj.  (fem.  °»a-)  'fördernd, mehrend'.
22481:•  j.  vaehana-  n.  'Kleidung,  Gewand': kammtK  (sd.)  vaste  'n>m  \.4.4g; —  aom asmatum  .  .  yim  mazda  vaste  (sd.)  'tum st3hrpaisat9h?m  Yl  13.  y,  —  'lumca  Vd.  ig.
24222:•  j.  vivashana-  patron.  Adj.  'von  Vlvah- vanl  stammend,  dessen  Nachkomme': yimahe  'nahe  Yt/J.  i?oj  —  yima  srXra •na  V.  2. 3,  9,  22.
=== BRT hama summer ===
7206:•  j.  ax'afnya-  Adj.  (fem.  yä-)  'schlaflos, immer  wach':  nairyam  ham-ianitlm  . . °yqm  \.(>J.$.
9981:nSmSni  aeSam  drujinqm  .  .  paiti.janaiti*'' Yt.4. 7.  3)  Med.  a)  II  'sich  wehren gegen  --,  bekämpfen',  mit  Akk.:  pärst^ martiy^  ^duraiyapiy  kacä  pitrsil^  hama- ram  (sd.)  patiyajatä  (3SPrM.)"  D.  ti. 4.  b)  'sich  wehren  um  — ,  kämpfen um  — ',  mit  kala  und  Abt.:  ya'ia  nä taxmö  . .  kus.kqm.bfr?tal  kam  laität  (sd.) . .  paiti.ynita  (3SOM.)  Yt.  13. 67.
11238:Zum  V.  'iar:  —  Pü.:  kattäraii.  —  0  So  nach Pü.;  das  Wort  könnte  aus  einem  Komp.  los- geschält sein;  vgl.  zu  'aril:     Unsicher. ■  p.  £artanaiy  Inf.  'zu  machen',  nur  mit hamaranam  'praellum  facere':  hauv  kära^ aliyavJ' . .  hamaranam  c°  . .  avada  hama- ranam akunavc^ . .  avdhäsäm  hamaranam kartam  Bh.j.9;  6,  7,  10,  J.  19,  2.7-12*. Zum  V.  >to-.     Vgl.    (gegenüber   WZKM.  g. 166}  IF.  4-  128,  KZ.  35.  61.
11863:Med.  adam  Aamaiax/aiy  yatä  vfiam tyam  amaxam  *ga^avä  avästayam)Sa..i.\ä,\ —  adam  hamataxlaiy  .  .  y<^3  gaumät^ .  .  viiam  tyäm  amaxam  naiy  paräbar<^ Bh.  /.  14;  —  *adakXy  imaiy  marliyiJ  *hama- taxsd'm  anusiyä  manä  *v^da'/amä  .  . Bh.  4.  18.  a)  mit  Gen.  (statt  Dat) 'für  — ':  marliyt^  hyJ"  hamataxsatJ  manä viüyj  avam  ''ubaratam  aöirraw»  Bh.4.13.
14250:•  p,  9-akatay-  C  '(zeitliches)  Vorüber-, Zuendegehen',  nur  LS.  *lä  in  Verbindung mit  dem  Verbum  ^ah-  (Sp.  »71  o^:  gar- mapadahya  mähyä  g  raucabii'^  'tä  akt^ avah/l  xsa%''am  agarbayata  "im  Monat  des G.  gingen  neun  Tage  zu  Ende '',  da  . ." Bh./.  11;  II,  13,  18,  19,  2.6-10,  12, J' 3-  6,  7t  9.  ro.  '4;  —  garmapadahya mahya  1  rauc^  °ta  akc^  ava^aiäm  hama- ranam  kartam  "im  Monat  des  G.  ging ein  Tag  zu  Ende^',  da  . ."  Bh.  g.  i.
15065:•  p.  patiS,  j.  paiti$'>  i)  Praen.  mit  Akk. 'in  der  Richtung  gegen  — ,  nach  —  hin, gegen  — 'r  II  avadä  ,  .  nad^tabairJ' . .  *äis (Sp.  148  u.)  hadä  kärä  p'  mäm  hama- ranam  carlanaiy  ".  .  brach  N.  mit  seinem Heer  gegen  mich  auf,  um  (mir)  eine  Schlacht zu  liefern"  Bh.M9;  2.7-12^,^.6,  7,  10; —  ayme  p'  gars  nmm>m  "auf  dem  Gang nach  dem  GA'/«."  Ytj.  4(?); — yö  aisqm
15663:•  p.  *parga-'>  m.  Name  eines  Bergs  in Fersien:  'ga*  näm(^  kaufet  avadä  hama- ranam  akunavif  Bh,^.  7.
16650:•  j.  bayö.baxta-  Adj.  'von  den  Göttern bestimmt,  gefügt':  'ttm  paiti  yaomm  Yt ^'.35;  _  =wVyLi'5(?).  a)  -fc«  ASn. als  Adv.  'auf  (besondere)  Fügung  der Götter'";  nairyqm  ham-varaitlm  ..yä  dim (sd.)  jasaiti  'ttmcit  ". .  die  sich,  und  zwar auf  besondere  Fügung  der  Götter,  bei  ihnen (den  Männern)  einstellt"  Vr.  7. 3.
18738:I055     naiiyam-ham-värativant-
20321:•  p.  *inärgaya-''  Adj.  'aus  Mai^iane stammend;  Margianer":  dadarsi! .,  hama- ranam  akunaus  hadä  yatdis  Bh.  3.  ^.
=== BRT Sommer ===
3494:*)  Der  austrocknenden  Sommerhitze;  vgl.  Yt. S.  2iff,,  Bd.  7.  8ff.,  2S.  39,  Dd.  gj.  II  (,  wo der  Name  volksetymotogiscji  als  „the  destructioti of  water"  —  äfi  ös  —  gedeutet  wird).
3797:•  j.  aiwLgäma-  m.  r)  'Winter';  fra  hama (stL)  iocinte  aHa  'me  V.j.io;  —  hama.. °me  "während  des  Sommers  . .  im  Winter" F.  2jb;  V.5.4a,  75.45,  "-^.46,  47,  4^'\ $0,  j/,  103'.  3)  sva,  'Jahr':  hasannm •manqm  Yt().  lo;  ig.2^,  V.  2.41.
7899:yeie  dus:^arm3:  nSit  imat  .  .  mihr/f  vat- naili  Ytio.105;  —  aeü/a  (sd.)  ti  sävan .  .  framrava  .  .  °5«  tl  zävan  .  .  fra- ifiraomi {sd.)  YLJj.r-ig;  —  "äil  mainya matnanäitl  Y.  j_y.  4;  4';  —  °äa  ät  yaza- maide  ahurtm  Y.jj.i;  39-1;  —  ät  '%ä yazamaidi  .  .  Y.  jtj?.3;  —  °äa  f  hai^ya (sd.)  nard  d^ä  jjnayö  Y.5^.6;  ■ —  Aaca ..pairi.sa^äiti  °äa  *aiwi.game  Hat  hama.. "sie  dauert  von  . .  bis  ,  .;  so  im  Winter; aber   im   Sommer  .  ."   N. 4Ö;  47,  ^SO^"^;
11897:auf  diese  Weise',  zurückweisend;  a)  avavat kavaim  ^armd  ya%a  yat  .  .  us./ravayBit (sd.)  . .  f  asti  kavalm  ifarmS  %rä^nm  . . Yt.  ig.  6Bi  b)  als  Korrelat  von  iya^ 'wie':  s?rao^  ita  astü  .  .  hyaf  paour- vXm  f  ust3mfm(sd.)cyt  Y.  56.  i,  Vr.  g. 7.  c)  bei  elliptischer  Ausdrucksweise im  Sinn  von  'das  (Gesagte)  gilt  ,  .':  Aaea hä  vaxiat  [.  .]  mailyai  xsape  palrisacäiti t°  Aatna  t°  *ami.gäme  ".  .  das  gilt  im Winter,  das  im  Sommer"  N.ji;  48',  103Q); —  tat^giiniakva  %rigamlm  f  lkaesaAe{sA.) f  *vtkayehe  f  arüaAe  f  arikavanS  F. 2jb.  7)  wie  unser  schwach  toniges  (zeit- liches und  räumliches)  'da'  zur  Belebung einer  Schilderung  (usw.):  na  t°  para.- irihyeiti  avi  jqfnavS  raonqm  a  f  mirTy^m .tisvazaitcupa  tarn  kiArptm  fratauAaraiü \..3t°  msnyim  utvazaite  ,  .  avi  bar^i- navs  gairinam  . .  nä  f  frasusaUi  .  .  upa
14636:narS  asavanö  "Drei  Mahlzeiten  (am Tag)  erhält  das  Feuer  ..  im  Sommer,  zwei im  Winter.  Ebenso  die  gläubigen  Männer."
15103:*)  Ursprünglich  Erntefest  ist  es  spater  dem Andenken  an  die  Schaffung  der  Erde  geweiht Der  lelite  (75.)  Tag  fallt  auf  den  30.  des  6, Monats,  75  Tage  nach  dem  Maüjiöisam-FesX,  d.  i. ursprünglich  75  Tage  nach  der  Sommersonn- wende,  also  auf  den  3.  September.  Heutzutage auf  Mitle  Mail.  S.  im  Übrigen  unter  yäiiya- und  maiiyöiSam-.
17869:AbleiL  ans  */riu>urvaeiira-  n.  "Eiotrieb',  Komp.  -■ */ra+*iirvafJtta;  lUm  V,  urvaFs-  (vgl.  Yt.  lO. 86>  —  Pü.;  i  pa/rSt  vall  hamlmh  äy?t  "der Icoramt,  «enns  mit  dem  Sommer  abwärts  ceht", Sü. :  adhakparivarlilaatifakälägätiH-,  vgl.  DsT. ZA.  7.  39-  —  ')  Bed.  nach  Roth  ZDMG.  J^. 704;  vgL  Ggr.  OK.  3^1.
19646:Eig.  'Mittjahr*;  ir.  *madjiäria-,  haplol.  aus *niaäiai-iär^a  entstanden  (falsch  J  306,  3) Der  Nume  läist  schliesien,  dass  in  ältester Zeit  das  Jahr  mit  dem  Sommersolsliz  begann; s.  Roth  ZDMG.  34-  711,  Gor.  OK.  324.
19662:*)  Ursprünglich  Sommersannwendfest  ist  es später  dem  Andenken  an  die  Schaffung  des Wassers  geweiht. Der  leuteTag(iS. des 4.Monats) ist  der  105.  Tag  des  Jabrs;  mit  ihm  schliesst die  erste  Hälfte  der  auf  310  Tage  (7  Monate) gerechneten  warmen  Zeit;  »gl.  V,  /.  3  Gl.,  Bd. 35.  7.  Heutzutage  ffillt  er  auf  Anfang  Janaar. War  er  in  alter  Zeit  der  Sommersonnwendtag (30.  Jani),  so  begann  das  alte  Jahr  am  g.  Man. So  Roth.  West  und  Dst.  dagegen  setzen  den Jahresanfang  auf  den  Tag  nach  der  Frlihlings-
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
25870:mit  ä  dnwS. :  hapta  h»nti  hqminö  manha panca  tayana  aikan  (3PPrA.)''  "es  gibt (sonst)  sieben  Sommermonate,  (wenn)  die fünf  Wintermonate  vorbei  sind"  V.  1. 3 PüZ.
26089:•  j.  sar9ta-  Adj.  "katt':  dva  (näml.  manhs) hqmina  iaica  h^nti  'ia  äps  'ta  z»mS  'ta urvarayä  "(es  sind  dort)  nur  zwei  Sommer- monate und  auch  die  sind  (zu)  kalt  für . ."
26097:Ablcit.  —  ooss.  sätd  'Sommer',  ap.sjl  'Jahr';
29390:•  j. 'ham-,  °/a»i-m. 'Sommer':  *ä«^'äa'J .  .  äfari  .  .  'ma  (IS.)  ^ii/i^wS  aiwi.gäme F.  25  b;  V.5.4a,  i5.4S,  Ä  74  PüZ.  {?),  N. 46,  *4j'-\  48,  50,  5/,  */0j'>;  —  yat  vä 'ma  . .  yat  vä  . .  zalna  V.16.12;  — •uia  al  zayem  Y.  16.10;  —  /■wca (GS.)  aiwi^gaUm  V.5.6.  a)  Plur. 'Sommerzeit';  /rä  •>Hfl(NP,)3)  sacinte  a'ha aitui^äme  "die  Sommerzeit  ist  vorbei;  tm Winter  also  . ."  V.5. 10.
29411:j.  hama'S-a  Adv.;  1)  modal" 'gleicher- weise, ebenso;  gleich ra'ässig';  h'  yaha paracit  "ebenso  wie  zuvor"  Ytj.  65,  V. "  [,"43,  8.2Z,  ff.  48;  —  ^a^hasca  .  .  äps (näml.  apayiars)  h'  ava.baraiti  hqmimmca zayammca  "und  dieses  Wassers  (Abfluss) strömt  gleichmässig  herab  zur  Winters-  und Sommerszeit"  Y.  6^.  5;  —  avi  dis  alm  .  . h'  baraiti  isavS  "an  sie  verteilt  er  gleich- mässig seine  Pfeile"  Yt  10.  loi,  2)  tem- poral'* 'gleichzeitig":  h'  .,  vsiynä  jasänti h'  .  .  h'  .  .  "gleichzeitig    damit  .  ■"    Yt
```


## [2026-09-14T02:00:40.175Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"'alt'\\|\\\"alt'\" BRT.txt | grep -n -i \"hana\\|hanō\\|hano\" | head -10; echo \"---\"; grep -n \"hana-  Adj\\|hana- Adj\\|j\\.  hana\\|p\\.  hana\" BRT.txt | head -10; echo \"--- search sana/senex ---\"; grep -n \"senex\" BRT.txt | head -5",
 "description": "Grep Bartholomae for hana 'old'"
}
```


### [2026-09-14T02:00:40.274Z] TOOL RESULT

```
---
7786:•  j.  aohana-  Adj,  (fem.  °ml-),  PPM.:  s.  'ä/i-,
9870:BJ.  goflhana-  Adj.,  gasthäna-  n.;  mp.  (Pü.j ^slän.  —  I)  So  Jpi,  Mfa;  NA.  hat  ^avö.ü'. —  ä)  zSt.  s.  HHr5.slSna.  No.   l.
18167:•  \.  frshana-  Adj.  (fem.  °»a-)  'fördernd, mehrend'.
29101:•  j.  haSa.aiwyashana-  Adj.  'mit  dem Gürlelband'*  versehen,  umbunden':  imat bansma  h^a.zaöir>m  'tum  asaya  fra- stantpm  Y.  2.  i ;  77, 13.
29325:•  j.  hana-  Adj.  (fem.  °na-)  'greis,  alt': yat  haiiB  vä  zaururB  v3  pairistä.xhtdrS vä  bavät  V,_j.  ig.  a)  fem.  °nä-  als SubsL  'Alte  (in  verächtlichem  Sinn),  Vettel' : 'nqm  aitalsqm^)  *jijisat3uha  (Sp.  503  o.) p?r>sat3uha  V.  15.  13;  14;—  a?Ä  -na  fra- baraiti  baakitn  vä  .  ,  V./J.14;  —  *Aa- variti  (sd.) . .  V7r>zyan  näca  kainica  'nsca V./5. 14.          [N.  5:' lies  ana\
29327:•  j.  hanayamna-  Adj.,  PPM.:  s.  ''han-,
--- search sana/senex ---
16741:•  j-,  g.,  p.  bav-  V.  'werden'.  Fraes.  1  \hm  V.  7.  52  PiiZ.;  —  iJ»«*'  gag'^ia  ''amar- bu;  bv-'\  2  bava-,  3  bva-'\  17  (Fat.)  ] säntis  Yt  ig.  12;  —  iä  srva  ..  bun^  .. büiya-,  22  bJ-'^,  [25  'vlli/\'>,  27  buya-(^)i']  dagvattam  karstayasia  . .  "die  Nägel  wer- Perf.  I  bväv*',  2  babv'^;  J-Aor.  i  bUs-*''.  \  den  zu  Messern  der  Z>.  und  . ."  V.  ly.  10; —  PPfP.  bsta-]  Inf.  buy^,  'bata,  bOzdyäi.  —  vXsp^m  a  ahmat  yat  kan5  .  .  bavaj I)  'werden  sva,  ins  Dasein  treten,  ent- ,  "usque  eo  donec  senex  . .  fuerit"  Y.j.ig; stehen;  erfolgen,  geschehen':  vupim  a/a-'j,  32,  5.38,  5.31,  Y.  65.  9,  FrW.4.3;  — vamm  hsntiinca  bavanlimcai'^  bßsyan-'  itala  dai/iAävS  AuyäiiyS  baväitti  Yt  S.  36; titnca  ",  .  der  (jetzt)  da  ist  und  (jetzt)  FrW.^.jj — yat  baväni /rya  fri^a  paiti.- ins  Dasein  tritt  und  künftig  ins  Dasein  irdn/tf  (s.5)  Yt./J.sö;  —  siviÜS  bavski ya'ka treten  wird"  Y.2/.4,  Vr,/Ä2;  — vispam  ,mazdi  Az.2.  2-7"^  Vyt4*;  —  *ya%a*ra aSaetüS  sttm  haitimca  bavaintJmca^''  bäs-  ,buyäl  (statt  Plur.)  Aväyaonänhs  pantätüS yeintxmia  Y.  rp,  9;  —  vTspayS  afaonö  Yl/ö.  3;  —  yesnyS  ahi  .  .  yesnyö  buyi stuii Aai'ätyaica  bavqi%yäi^a^  bB^yqi%-\Y.62.i;  —  Uta  buyä  afrazaintis  Y.ii.i; yäi^a  Y,52,i;  68.22;  —  ala  Aau  apa-\  —  ta  tiS  buyqn  kumiid^Y.^^.2;  —  «ä«i ylärB  bvat'''  "da  entstand  jener  Abfluss" ,  e?  buyarps  masänä  Ny. _j-ii;  —  alsiJca Yt  ig.  56;  —  yat  kvan  uzuxsyäti  bvat'>  ■  ^wä  Smavantasca  buyamä  "wirksam  möch- zqm  , .  yacsdäi^rjm  "wenn  die  Sonne  auf-  i  ten  wir  durch  dich  werden  und  mächtig" geht,   erfolgt  eine  Purifizirung  der  Erde"  |y.  47. 4;   —   buyama  ahurahe  . .  frya  ..
```


## [2026-09-14T02:00:47.049Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 00537653f130356c 4fdb50b6ca2c2148 b726e506f213ce7d; do echo \"======== $f\"; head -c 2500 $f.txt; echo; done",
 "description": "Read archived PIE sem- and summer pages"
}
```


### [2026-09-14T02:00:48.173Z] TOOL RESULT

```
======== 00537653f130356c
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sem-
FETCHED: 2026-09-14T01:59:54Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/sem- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/sem- - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.2 
 References 

 1.3 
 Further reading 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ sem- 

 Add languages 

 Reconstruction 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *sem- [ 1 ] 

 one , whole ; same 

 together 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *sem- (141 c, 0 e) 

 *sḗm ( “ one ” ) 

 *sēm-i ( “ half ” ) 

 *sm̥- ( compounding stem ) 

 *sem-ǵʰo- 
 Proto-Albanian: *semdza 
 Albanian: gjithë 

 Proto-Italic: *senɣeloi 
 Latin: singulī 

 *som- [ 2 ] [ 3 ] 
 Proto-Balto-Slavic: *sam- ( see there for further descendants )

 Proto-Germanic: *sam- 
 Old Norse: sam- ( see there for further descendants )

 Proto-Indo-Iranian: *sam- ( see there for further descendants )

 *ḱóm -som- ? 
 > ? Proto-Hellenic: *ksún ( see there for further descendants )

 *som-H-ós ( “ same ” ) 

 *sm̥mo- ( “ some, any ” , enclitic ) [ 1 ] [ 4 ] or *sm̥Ho- [ 5 ] [ 6 ] 
 Proto-Armenian: 
 ⇒ Old Armenian: ամէն ( amēn ) ( see there for further descendants )

 Proto-Germanic: *sumaz ( “ some, 
======== 4fdb50b6ca2c2148
URL: https://en.wiktionary.org/wiki/summer
FETCHED: 2026-09-14T01:59:54Z
STATUS: 200
TITLE: summer - Wiktionary, the free dictionary

summer - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 English 

 Toggle English subsection 

 1.1 
 Pronunciation 

 1.2 
 Etymology 1 

 1.2.1 
 Alternative forms 

 1.2.2 
 Noun 

 1.2.2.1 
 Usage notes 

 1.2.2.2 
 Antonyms 

 1.2.2.3 
 Coordinate terms 

 1.2.2.4 
 Derived terms 

 1.2.2.5 
 Translations 

 1.2.3 
 Verb 

 1.2.3.1 
 Derived terms 

 1.2.3.2 
 Translations 

 1.2.4 
 See also 

 1.3 
 Etymology 2 

 1.3.1 
 Noun 

 1.3.1.1 
 Derived terms 

 1.3.1.2 
 Translations 

 1.4 
 Etymology 3 

 1.4.1 
 Noun 

 1.4.1.1 
 Derived terms 

 1.4.1.2 
 See also 

 1.5 
 References 

 2 
 Alemannic German 

 Toggle Alemannic German subsection 

 2.1 
 Alternative forms 

 2.2 
 Etymology 

 2.3 
 Noun 

 2.4 
 See also 

 2.5 
 References 

 3 
 Bavarian 

 Toggle Bavarian subsection 

 3.1 
 Alternative forms 

 3.2 
 Noun 

 3.3 
 References 

 4 
 Mòcheno 

 Toggle Mòcheno subsection 

 4.1 
 Etymology 

 4.2 
 Noun 

 4.3 
 See also 

 4.4 
 References 

 5 
 Norwegian Bokmål 

 Toggle Norwegian Bokmål subsection 

 5.1 
 Noun 

 5.2 
 Verb 

 6 
 Old French 

 Toggle Old French subsection 

 6.1 
 Alternative forms 

 6.2 
 Etymology 

 6.3 
 Noun 

 6.3.1 
 Descendants 

 6.4 
 References 

 Toggle the table of contents 

 summer 

 77 languages 

 العربية 
 Asturianu 
 Azərbaycanca 
 বাংলা 
 Brezhoneg 
 Català 
 Čeština 
 Cymraeg 
 Dansk 
 Deutsch 
 Zazaki 
 Ελληνικά 
 Esperanto 
 Español 
 Eesti 
 Euskara 
 فارسی 
 Suomi 
 Français 
 Galego 
 Gaelg 
 हिन्दी 
 Hrvatski 
 Magyar 
 Հայերեն 
 Bahasa Indonesia 
 Interlingue 
 Ido 
 Íslenska 
 Italiano 
 日本語 
 ქართული 
 Қазақша 
 ភាសាខ្មែរ 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Кыргызча 
 Latina 
 Limburgs 
 Lombard 
 ລາວ 
 Lietuvių 
 Latviešu 
 Malagasy 
 Māori 
 Македонски 
 മലയാളം 
 Монгол 
 မြန်မာဘာသာ 
 Nederla
======== b726e506f213ce7d
URL: https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85
FETCHED: 2026-09-14T01:59:56Z
STATUS: 200
TITLE: سیم - Wiktionary, the free dictionary

سیم - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Mazanderani 

 Toggle Mazanderani subsection 

 1.1 
 Pronunciation 

 1.2 
 Noun 

 1.2.1 
 Synonyms 

 2 
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection 

 2.1 
 Etymology 

 2.2 
 Noun 

 2.2.1 
 Derived terms 

 2.2.2 
 Descendants 

 2.3 
 Further reading 

 3 
 Persian 

 Toggle Persian subsection 

 3.1 
 Etymology 1 

 3.1.1 
 Pronunciation 

 3.1.2 
 Noun 

 3.1.2.1 
 Derived terms 

 3.1.2.2 
 Descendants 

 3.1.3 
 References 

 3.2 
 Etymology 2 

 3.2.1 
 Noun 

 3.3 
 Etymology 3 

 3.3.1 
 Pronunciation 

 3.3.2 
 Adjective 

 3.4 
 Etymology 4 

 3.4.1 
 Pronunciation 

 3.4.2 
 Noun 

 Toggle the table of contents 

 سیم 

 12 languages 

 Беларуская 
 فارسی 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Polski 
 Русский 
 سرائیکی 
 Тоҷикӣ 
 Türkçe 
 中文 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Mazanderani
 [ edit ] 

 Pronunciation
 [ edit ] 

 This entry needs pronunciation information. If you are familiar with the IPA then please add some!

 Noun
 [ edit ] 

 سیم ( sim ) 

 mold 

 Synonyms
 [ edit ] 

 پلسک ( plesk ) 

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Classical Persian سیم ( sīm ) .

 Noun
 [ edit ] 

 سیم • ( sim ) 

 silver , a lustrous , white , metallic element
 Synonyms: فضه ( fidda, fizza ) , كومش ( gümüş ) 

 money and coins made of silver 
 Synonyms: درم ( direm ) , فضه ( fidda, fizza ) 

 silverlike thread , lace or meta
```


## [2026-09-14T02:00:53.861Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('b726e506f213ce7d.txt',encoding='utf-8').read()\ni=t.find('Persian\\n [ edit ]')\nif i<0: i=t.find('Etymology 1')\nprint(t[i:i+3000])\nEOF",
 "description": "Read Wiktionary Persian sim etymology"
}
```


### [2026-09-14T02:00:55.023Z] TOOL RESULT

```
Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Middle Persian [script needed] ( (ʾ)sym /⁠(a)sēm⁠/ , “ silver ” ) , from Old Persian 𐎿𐎡𐎹𐎶𐎶 ( s-i-y-m-m /⁠siyamam⁠/ ) , from Ancient Greek ἄσημον ( ásēmon , “ silverware ” ) , neuter form of ἄσημος ( ásēmos , “ pure, unmarked ” ) . Akin to Parthian hsym ( hasēm , “ silver ” ) , Bactrian σιμινο ( simino , “ made of silver, silverware ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈsiːm/ 

 ( Dari, formal ) IPA ( key ) : [siːm] 

 ( Dari, formal ) IPA ( key ) : [siːm] 
 ( Kabuli ) IPA ( key ) : [siːm] 

 ( Hazaragi ) IPA ( key ) : [sim] 

 ( Iran, formal ) IPA ( key ) : [siːm] 

 ( Tajik, formal ) IPA ( key ) : [sim] 

 Rhymes: -iːm 

 Readings

 Classical reading ? 

 sīm

 Dari reading ? 

 sīm

 Iranian reading ? 

 sim

 Tajik reading ? 

 sim

 Noun
 [ edit ] 

 سیم • ( sīm / sim ) ( plural سیم‌ها ( sīm-hā / sim-hâ ) , Tajik spelling сим ) 

 wire 
 سیم تلفن ― sim -e telefon ― telephone wire 
 سیم خاردار ― sim -e xârdâr ― barbed wire 

 string ; cord 
 سیم ویولن ― sim -e viyolon ― violin string 

 ( original sense , now poetic ) silver 
 Synonym: نقره ( nuqra  / noġre ) 
 c. 1850 , Mirzā Ḥabib-Allāh Širāzi Qāʾāni , وله ایضاً فی مدحه : نرگسک آن طشت سیم باز به سر برنهاد
 بر سر سیمینه طشت طاسک زر برنهاد nargesak ân tašt-e sim bâz be sar barnehâd
bar sar-e simine tasht tâsak-e zar barnehâd The little narcissus has again put that silver basin on its head
Upon the silvery head, the basin has put a little golden bowl 

 ( now poetic ) wealth ; money 

 Derived terms
 [ edit ] 

 بی‌سیم ( bē-sīm  / bi-sim ) 
 سیم خاردار ( sīm-i xārdār  / sim-e xârdâr ) 
 سیم ظرفشویی ( sīm-i zarfšōyī  / sim-e zarfšuyi ) 
 سیم و زر ( sīm u zar  / sim o zar ) 
 سیم کشیدن ( sīm kašīdan  / sim kešidan ) 
 سیمین ( sīmīn  / simin ) 
 سیمینه ( sīmīna  / simine ) 
 سیم‌پیچ ( sīm-pēč  / sim-pič ) 
 سیم‌کشی ( sīm-kašī  / sim-keši ) 
 ماهی سیم ( māhī-yi sīm  / mâhi-ye sim ) 

 Descendants
 [ edit ] 

 → Azerbaijani: sim 

 → Chagatai: سیم ( sym /⁠sīm⁠/ ) 
 Uyghur: سىم ( sim ) 

 Uzbek: sim ( “ wire ” ) , siym ( “ silver ” ) 

 → Gujarati: સીમ ( sīm ) 

 → Kazakh: сым ( sım ) 

 → Kyrgyz: сым ( sım ) , зым ( zım ) 

 → Turkmen: sim 

 References
 [ edit ] 

 Philip Huyse (23 February 2012), “Greek Loanwords in Middle Iranian Languages”, in Encyclopaedia Iranica ‎ [5] 

 Etymology 2
 [ edit ] 

 Short for ماهی سیم ( mâhi-ye sim ) , literally “silver fish”, but its old form was شیم ( šim ) .

 Noun
 [ edit ] 

 سیم • ( sīm / sim ) ( plural سیم‌ها ( sīm-hā / sim-hâ ) , Tajik spelling сим ) 

 bream 

 Etymology 3
 [ edit ] 

 From سی ( sī  / si , “ thirty ” ) + ـم ( -um  / om , “ -th , -eth ( ordinal number suffix)) ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /si.ˈjum/ 

 ( Dari, formal ) IPA ( key ) : [si.jʊm] 

 ( Dari, formal ) IPA ( key ) : [si.jʊm] 
 ( Kabuli ) IPA ( key ) : [si.jʊm] 

 ( Hazaragi ) IPA ( key ) : [su.jum] 

 ( Iran, formal ) IPA ( key ) : [si.jom] 

 ( Tajik, fo
```


## [2026-09-14T02:01:05.749Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD sem summer ===\"; grep -n -i \"sem-2\\|sem-3\\|Summer\\. \" AHD_watkins1985.txt | head -10; echo \"--- sumaraz/sumar ---\"; grep -n \"sumar\\b\\|Germanic \\*sumar\\|sumor\" AHD_watkins1985.txt | head -10; echo \"=== AHD sen old ===\"; grep -n -i \"^sen-\\|sen-\\. Old\\|senex\" AHD_watkins1985.txt | head -10",
 "description": "Grep Watkins AHD for sem/sen"
}
```


### [2026-09-14T02:01:05.857Z] TOOL RESULT

```
=== AHD sem summer ===
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
--- sumaraz/sumar ---
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
=== AHD sen old ===
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
```


## [2026-09-14T02:01:14.732Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN summer ===\"; grep -n -i \"SUMMER\" SYN.txt | head -8; echo \"=== SYN old ===\"; grep -n \"14.15 OLD\\|OLD$\" SYN.txt | head -8; echo \"=== IEC semos/sumaraz ===\"; grep -n \"sem-, sem\\|semos\\|sumaraz\\|senos\\|senex\" IEC.txt | head -10",
 "description": "Grep Buck and Mann"
}
```


### [2026-09-14T02:01:15.896Z] TOOL RESULT

```
=== SYN summer ===
9477:: od here in the cur- pruit’ i NE fruit as a generic pet Stree fruit’, covering apples, pame for This notion is commonly, a always, the result of unre i fea fruit, product’ in the wides tion gdov, Dor. waov, uiente tat, a oth used for ‘apple and other malum, f pre-Greek orig. See 5.72. fruits, prob: M4 ts fruit season’ srtopa late summer, ru ? pie ‘fruit? (cf. LS s.v.), epd. of ae ém-bey ‘behind, after’ and vat. *H(e)a00 : Goth. asans ‘harvest- time, summer’, ChSl. jesent, etc. ‘au- umn’ (14.67). Schulze, Quaest. Ep. 474f, Walde-P. 1.161f. Boisacq 709 (but Dor. érépa very dub.). Hence, through adj. dawprxds. NG (6)awprxd. NG ¢poiro, the usual word, fr. It. rulto. : 2. Lat. pomum, orig. dub., loanword? Osthoff, IF 5.317 ff. Ernout-M. 786 f. Hence Rum. poamd ‘fruit’ (also ‘apple’, dial. ‘grape’), pom ‘fruit tree’, It. pomo fruit, fruit tree’, and other Romance words for ‘fruit’ or ‘apple’. REW 6645. Lat. frictus ‘product, fruit’ in widest sense, fr. frut ‘enjoy’ : Goth. brikjan, OE brican ‘use’, etc. Walde-P. 2.208. Emout-M, 893 f. Walde-H. 1.552. oe os special though not exclusive fla Te ae fruit’, It. frutto, coll. rg eit (> ME ful, NE ret), » Coll. fruta, Rum, fruct, W.
10788:But the objection to the old deriv. fr. MLat. aestivalia, lit. ‘belonging to the summer’ (fr. Lat. aestivus, fr. aestus ‘summer’), but actually described as ‘high boots’, is invalid. Cf. esp. Kret- schmer, Wortgeogr. 487 f.
12739:2. Grk. depltw, fr. Géoos ‘summer’ and hence also ‘harvest’ (8.41).
12875:Grk, Gé ¢ harvest? ‘Pos summer’ and also ‘crop,
12895:Goth. asans (= Oepiopds, once Bépos ‘summer’), OHG aran, MHG erne, NHG ernte, all orig. with reference to the ‘harvest-season’: OE earnian, OHG arnen ‘earn’, arndn ‘reap’, ChSI. jesent ‘autumn’. Walde-P. 1.161. Feist 58 f.
24331:SUMMER
25292:tainly those of the large inherited | léto ‘year, summer’ (14.73). Walde-P. ze denoted the -bright ‘day’ vs. | 2.427. Pedersen 1.133. Thurneysen, ie Kit and only secondarily (like ‘sum- | Gram..35, 180. Pokorny KZ 50.43 if ne ss ‘winters’ for ‘years’) the com- (taking lae as of different orig., but cf. wehensive 94-hour ‘day’ (for which | Vendryes, RC 42.234 f.). Dan., Sw. have distinctive forms). 4. Goth. dags, ON dagr, OE deg, 1. Derivs. of IE *dei- ‘shine’, rare in | OHG fag, etc. general Gmc. (also derivs. verbal forms (Skt. 3sg. imperf. adzdet, Goth. fidur-dogs ‘of four days’, OE dégor etc.), but widespread in words for ‘sky, | ‘day’, ON degr ‘12-hour period, day or heaven’ as Skt. nom. sg. dydus and the | night’, Dan. dégn, Sw. dygn (the last two personified Grk. Zebs, Lat. Iupiter, Iovis; denoting the 24-hour day), etym. dub., ‘god’ as Skt. deva-, Lat. deus, etc.; and | but perh. (despite phonetic difficulties ‘ay’. Walde-P. 1.772 ff. Ernout-M. | with the gutturals) : Lith. dagas ‘(sum- 268 ff. Walde-H. 1.350. Here as ‘day’. | mer-) heat’, OPruss. dagis ‘summer’, Skt. a) IE *dyeu-, *diw-, etc. nidagha- ‘heat, summer’, fr. the root Lat, digs (> It. di, OF r. di, Sp. dia, | *dheg*h- in Skt. dah-, Lith. degti, etc., Rum. zi); Ir, dia, die, W. dydd, Br. | ‘burn’, and also (with init. doublets, as deiz; Skt, diva- (in dive dive ‘day by day’, | Skt. agru-, Lith. asara : Grk. daxpu otherwise divasa-); Arm. tiw. Lat. deriv. | Goth. tagr ‘tear’, etc.), Skt. ahan-, Ay. adj. diurnus ‘of the day’, late sb. diur- | azan ‘day’. Walde-P. 1.849 f. Walde- mm > Fr. jour, Prov., Cat. jorn; It. | H. 1.467. Falk-Torp 183, 176. Feist ee vs. di perh. due to lit. influence | 113. ea or Fr. REW 2632, 2700.| 5- Skt. gat Caisse ae il ae 3.71f., 105f. Bonfante, | instr. sg. ahna, etc.), Av. se . Sg. “74 59.877 ff. (with refs.). asni, etc.), see above, 4, with reis. b) With nasal suffix. Av. ayan- (nom. sg. ayara, gen. 8g. aes Lett. diena; ChSl. dint, ete., | war ete., neut r/n stem. like Skt eral Slavies Skt. di in epds.): | 2a" above), prob. : Grk. fier ‘in the Me ed (eap. in epds.); ning’, Goth. air, ON ar, etc., ‘early’, » tre-denus ‘triduum’, Goth. sin- he eee z
25736:7. ChSI. léto (= eros, évaurés, xXpbvos, katpés, Gospels, Supr.; also Bépos Pg, Sin.), modern Slavic ‘summer’, rarely also ‘year’ : Sw. dial. lading ‘spring’, Ir. laithe ‘day’. Walde-P. 2.427. Ber- neker 713 f.
=== SYN old ===
15391:610 SELECTED INDO-EUROPEAN SYNONYMS 9.64 GOLD
24433:14.15 OLD
27293:COLD
=== IEC semos/sumaraz ===
15144:. and cpds. Cf. séko (1) & cpds.) Lat. cf. foeni-seca, mf. ‘mower, cutter’; -sicia, f. ‘mowing, cutting’, pro-siciae, prae-siciae, fpl. *meat-cuts in sacrifice’; cf. also foenisex gs: -sicis, m. ‘mower’; (LW in) OHG séhh, n., G Sech *plowshare'; (long-gde. in) OCZ. s&Ci, f. ‘slaughter’; R séca, f. id.; cf. Cz. seno-sec, f. and senoseky, fpl. ‘mowing’
15196:senát- “age”. See senos Skt. cf. sanátà, adv. “of old’; sanat, ab. s. of sanah, see senos; sanat, m. ‘a brahma’ (proper name?); Ober hanata, f. “age, lapse of time’; Lat. senátus, gs: -üs, m. ‘senate’. Cf. OW hen- eint *old age' fr. *senonti-
15198:seneió (sen(e)sKo) ‘grow old Cf. senos Lat. seneo, ere beside senesco, Gre, v. "be old; grow old'; Li. senéju, éti, beside sénstu, sénti, id.
15213:senos "old: senis, ios “elderly; old man’. WP Ii, 494 Skt. sánab, id.; Av. hand, m. old man’; Arm. hin, gs: hno ‘old’; Gk. hénos "last year's old’; Lat. cf. senex, gs: senis, m. old man’; Olr. sen, Ir. sean, adj. "old: m. “old man’; cf. seine, sine, f. “old age’; Gaul. seno-, cpds.; W, OBr. Br. Cor. hen old: Go. cf. sin-eigs, adj. “old, aged”; sin-ista ‘oldes’; Burgundian (in LLat.) sinistus “elder, elderly priest; OS cf. sin- hrwun *man-and-wife'; sin-weldi ‘forest’; sin- lif (“eternal life’. Hybridism w. type sem- ‘one’, q. v.; Li. sénas, adj. "old: sénis, gs: -io, m. "old man’; Latv. sens, adj. "old
```


## [2026-09-14T02:01:16.026Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB sim ===\"; grep -n \"sīm\\|sim 'Silber'\\|Silber\" HUB.txt | head -20",
 "description": "Grep Hübschmann for sim/Silber"
}
```


### [2026-09-14T02:01:16.085Z] TOOL RESULT

```
=== HUB sim ===
4215:'Silber =^ phi. asTm, gr. aatjiioQ (Noldeke, Pers. Stud. II,
```


## [2026-09-14T02:01:22.713Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4205,4225p' HUB.txt; echo \"=== BUCK summer 24331 ===\"; sed -n '24331,24345p' SYN.txt | cut -c1-1800; echo \"=== BUCK old 24433 ===\"; sed -n '24433,24445p' SYN.txt | cut -c1-1500",
 "description": "Print Hübschmann sim and Buck sections"
}
```


### [2026-09-14T02:01:22.866Z] TOOL RESULT

```
vitae', twsdara, n^sgiya antidotum*, paz. anos 'antidote' Shk.
230, phi. anos Gl. and Ind. 59, vgl. phi. anorak *unsterb-
lich*, arm. anvsak unverganglich' ; dazu N. pr. Nosirevan
(bei Firdusi metri causa) = Nosirvdn (Muwaffaq
p. 4, Z. 7), alter Anosarvan (Noldeke, Tab. 136), paz.
anosruan, phi. anosakruvdn, arm. Anuseruan Xosrov (Sebeos
26, 30) = *Chosru Nushirvan*; N. pr. Noszad, alter Anosa-
zad, phi. anosakzat NOldeke, BB. 4, 52, Tab. 263, 467;
nosddir^) (bei Vullers ndsddur) =^ syr. anosddur, arm. ami-
sadr (nur bei CaxCax und im kleinen Wb.) 'Salmiak*; sltn
'Silber =^ phi. asTm, gr. aatjiioQ (Noldeke, Pers. Stud. II,
45); sdgird *Schuler = paz. asdgard Min. Gl. 17, arm.
asakert; vSrdn Viist', paz. avTrdn Min. Gl. 21, phi. aperdn;
vdrun ^) perversus, miser ^= paz. awdrun 'irregular, wicked*
Min. Gl. 26, phi. apdrfin Gl. and Ind. 9; zPr unten = paz.
azer Shk. 236 (aus z = «^^), paz. az = ap. hacd und paz.
er in ertan u. s. w. = zd. adardt); Murddd *der funfte
Monat' == paz. ^amerddd" Min. Gl. 7, parsT amiirddd
ZDMG. 36, 60, phi. amurd{d)t, zd. ameretdt-, ameretatdt-;
Naked, alter Anahed (Noldeke, Tab. 4) = paz. andhu)
Shk. 228, phi. andhit, arm. Anahit, np. anahata (fiir "^aftd-
=== BUCK summer 24331 ===
SUMMER
AUTUMN
SEASON Lith. laikas (Sésas) Lett. laiks ChSl. vréme, East, godt SCr. _vrijeme (doba) Boh.  éas (doba) Pol. czas (doba) Russ. vremja Skt. kala- Av. zrvan-
zit, (h)wila, stunta
zit, stunde, wile zeit (weile)
953
several : . (nati jane ont i
;. ylike ‘on’ yore Of the notions classified under “Spatial Relations” or Quantity and Num-
tis direction ee enor’ » ‘first’, ‘last’, are applied equally to time, ‘8: Lett. algs ‘long’ only of time, NE brief ‘short’ mostly of time.
or in some cases specialized in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
a Saree ©
Digitized by Arya Samaj Foundation Chennai and eGangotri
954 SELECTED INDO-EUROPEAN SYNONYMS
Some of the words for ‘time’ are from roots for ‘stretch’ or ‘measure’, with es- tablished temporal, rather than spatial, application. Others are of diverse and partly obscure orig.
=== BUCK old 24433 ===
14.15 OLD
Grk. adatés, dpxatos, Goth. fairneis, alpeis, Lith.  senas
yépwv sineigs Lett. veces NG madtés, apxatos ON forn, gamall ChSl.  vettichit, slarit Lat. velus, senex Dan. gammel : SCr. star It. vecchio Sw. gammal Boh. _ stary Fr. vieux (ancien) OE eald, gamol Pol. stary Sp. viejo ME old Russ.  staryj Rum. vechiu, batrin NE old (ancient) Skt. jirna-, sana-, vrddha- Tr. sen Du. oud Av. hana- NIr. _ aosta, crionna, sean- OHG | allt, firni W. hen MHG allt, virne Br. koz, hen- NHG alt
Most of the words for ‘old’ are used alike for ‘old’ vs. ‘new’ and ‘old’ vs. ‘young’, and this is to be understood in the following, except as otherwise noted. But a few are used wholly or chiefly in the latter sense, esp. of old persons; and this was the orig. application of many of the others, as indicated by their etym.
1. TB *sen-. Walde-P. 2.494. Er- nout-M. 922 f.
Lat. senex (of living things, mostly persons); Ir. sen, NIr. sean, W. hen (Br. hen- as prefix, as often Ir. sen- and most- ly NI. sean-); Goth. sineigs, super. sin- ista (only of persons, ‘rpecBirns, mpeoBbre- pos’); Lith. senas, Skt. (Ved.) sana- (opp. to nava- and yuvan-), sanaya-, Av.
hana- (quotable only for old persons); Arm. hin; cf. Grk. é&os ‘of last year’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
évn kal véa (Sc. jyépa) ‘the old and new day’ = ‘last day of the month’, ON sina ‘dry standing grass from the previous year’.
2. Ii *wetus- (*wetos-?), prob. : Grk.
réros ‘year’, etc. (14.73), as orig. ‘full —
of years’ or even ‘one year old’ (which would be ‘old’ vs. ‘new’ for wine, grains, fruits, etc.). Walde-P. 1.251. Ernout-M. 1100 (with doubt).
Lat. vetus, vetustus, dim. vetulus (> VLat. veclus > It. vecchio, Fr. vieux, Sp. viejo, Rum. vechiu), Lat. veterdnus ‘veter- an’ (> vetraénus > Rum. bdirin); OLith. velugas, Lett. vecs; ChSl. vetticht in the Gospels ‘ranarés’.
```


## [2026-09-14T02:01:33.300Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4215 && /^—? *[0-9]{1,3} *—?$|- [0-9]{1,3} -/ {ln=NR; l=$0} END{}' HUB.txt; grep -n -- \"- 1[0-9][0-9] -\\|— 1[0-9][0-9] —\" HUB.txt | awk -F: '$1<4260 && $1>4000' | tail -5; echo \"=== buck summer section ===\"; grep -n \"14.6[5-9]\\|SUMMER$\" SYN.txt | head",
 "description": "Find Hübschmann page and Buck summer section"
}
```


### [2026-09-14T02:01:34.452Z] TOOL RESULT

```
4034:8*-- 116 -
4074:konsonantische Stumme audi nacli dem Abfall der Endsilben den [Inter-- 117 -
4114:schen verwerthet worden sind.— 118 —
4152:*) Ueher die heutige Aussprache vgl. Sal. Shuk. p. 10 flg.- 119 -
=== buck summer section ===
5663:e’ (as Mt. 6.16, Mk. 14.65,
9477:: od here in the cur- pruit’ i NE fruit as a generic pet Stree fruit’, covering apples, pame for This notion is commonly, a always, the result of unre i fea fruit, product’ in the wides tion gdov, Dor. waov, uiente tat, a oth used for ‘apple and other malum, f pre-Greek orig. See 5.72. fruits, prob: M4 ts fruit season’ srtopa late summer, ru ? pie ‘fruit? (cf. LS s.v.), epd. of ae ém-bey ‘behind, after’ and vat. *H(e)a00 : Goth. asans ‘harvest- time, summer’, ChSl. jesent, etc. ‘au- umn’ (14.67). Schulze, Quaest. Ep. 474f, Walde-P. 1.161f. Boisacq 709 (but Dor. érépa very dub.). Hence, through adj. dawprxds. NG (6)awprxd. NG ¢poiro, the usual word, fr. It. rulto. : 2. Lat. pomum, orig. dub., loanword? Osthoff, IF 5.317 ff. Ernout-M. 786 f. Hence Rum. poamd ‘fruit’ (also ‘apple’, dial. ‘grape’), pom ‘fruit tree’, It. pomo fruit, fruit tree’, and other Romance words for ‘fruit’ or ‘apple’. REW 6645. Lat. frictus ‘product, fruit’ in widest sense, fr. frut ‘enjoy’ : Goth. brikjan, OE brican ‘use’, etc. Walde-P. 2.208. Emout-M, 893 f. Walde-H. 1.552. oe os special though not exclusive fla Te ae fruit’, It. frutto, coll. rg eit (> ME ful, NE ret), » Coll. fruta, Rum, fruct, W.
12891:(14.67).
12904:W. cynhaeaf ‘harvest-time, autumn’ (14.67), now sometimes ‘harvest’. 3
24305:14.53 14.61 14.62 14.63 14.64 14.65 14.66 14.67 14.68 14.71 14.72 14.78 14.74 14.75 14.76 14.77 14.78
24331:SUMMER
25630:14.65 WEDNESDAy
25641:TIME 1007 14.66 14.67 14.68 THURSDAY FRIDAY SATURDAY gapparov mopcanely oaBBarov Gr “co Acés tutpa "Agpodlrns jyutpa. Kpévov : wapacKkeun ‘ xo rT dies Veneris praia Iat. oe ‘nla feria a feria sabbatum easy venerdi 1 ele vendredi aan pr 4 viernes fi 1eves Lerne sdbado z ‘oui vinert simbdta HL quinta feira sexta Seira sabado Po dardain din diden satharn It dardaoin aoine satharn aM dydd iaw dydd gwener dydd sadwrn hr diziow digwener disadorn Goth “Se paraskaiwe, fruma sabbaté sabbato dags ON orsdagr Srjadagr laugardagr, pvattdagr Nicel. fimtudagur Séstudagur laugardagur Dan. forsdag fredag Igrdag Sy,  torsdag fredag lordag 0E  punresdeeg Srigedeg seter(n)dag ME thursday friday saterday NE thursday friday saturday Du.  dondersdag vrijdag zalerdag OHG donarestag Sriatag sambaztag, sunniinadband MHG donerstac, pfinztac vri(e)tac sameztac, sunnabent NHG donnerstag freitag samstag, sonnabend Lith. Ketvirtadienis (Getvergas) penktadienis (pétnycia) SeStadienis (subata) Lett. celurdiena piektdiena sestdiena a telurlttieis peliiki, pelinica sobota, sabota a ‘hey petak subota Pol, She Pe patek sobota Russ as e piqtek sobota : 9 pjatnica subbota
```


## [2026-09-14T02:01:42.064Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hama-\\|Av. ham\\|sama- ‘half\\|sam4-\\|OE sumor\\|sumor\" SYN.txt | head -10",
 "description": "Grep Buck for summer words"
}
```


### [2026-09-14T02:01:42.129Z] TOOL RESULT

```
21461:3. Ir. sdéim, NIr. sdémh, sdimhe, also NIr., Gael. samhach ‘quiet, calm, pleas- ant’, with sb. Ir. sém, NIr. samh ‘quiet, rest’, perh. through notion of ‘even- ness’ : Skt. sama-, Av. hama-, hdama- ‘equal, same’, OF som ‘agreement’, etc. Walde-P. 2.492. Stokes 290.
23224:Brickner 113. fault’) : chid- ‘cut, split? (9.22, 9.97), ’ 12.91 EQUAL Grk. tos Goth. bna, samaleiks Lith. lygus NG toos ON (g)likr Lett. lidz (adv.), lidzeng Lat.  aequus, aequalis, par Dan. lige ChSl.  ravinii It. uguale, pari Sw. lika SCr.  jednak, ravan, Fr. égal OE gelic Boh. _ stejny, rouni Sp. igual ME’ -ilike, egall Pol. réwny Rum. egal NE equal, alike Russ. ravnyj Ir. 4(n)no(n)n Du. gelijk Skt. sama-, tulya- NIr.  tonann OHG gilth, ebanlih, sama- Av. hama- W. cyfartal lih Br. ingal, par MHG gelich NHG gleich
23257:7. Skt. sama- (also ‘level, flat’), Av. hama- = Grk. éyés, Goth. sama, etc. ‘same’. Walde-P. 2.490.
23902:célne, cét- NE jirst Skt. . prathama-
23907:mest; Lith. pirmas, Lett. pirmais; ChSI. priv, etc., general Slavic (cf. Skt. pur- va- ‘former’); Skt. prathama-, Av. fratama-.
25750:1013 14.76 14.77 SUMMER AUTUMN Oépos POtvérwpov xadoxalpt P0tvorwpo aestas aulumnus estate aulunno été automne verano, estio otono vara toamnd sam, samrad fog(a)mar samhradh foghmhar haf hydref (cynhaeaf) haziv diskar-amzer, dilost-hanv asans Re sumar haust sommer efteraar (h¢st) sommar hést sumor herfest sumer hervest, autum(p)ne summer autumn, fall zomer herfst sumar herbist sumer herb(e)st sommer herbst vasara ruduo vasara rudens Zetva, léto jesent ljeto jesen. leto podzim, jesen lato jester leto osen’ grisma-, nidagha- ¢arad- ham-
25788:Ir. sam, W. haf, Br. ham, Ir. samrad, NIr. samhradh (sam-r-ad Pedersen 2.53, but -rad :rdithe ‘season’, Loth, RC 43, 143 f.); ON sumar, OE sumor, etc., general Gmc., except Goth.; Av. ham- (Skt. samda- ‘season, year’ rarely also ‘summer’, cf. Macdonell-Keith 2.429 f.);
27059:7. Skt. sama- ‘even, smooth, level’ : Av. hama- ‘like, same’, Grk. duds ‘the same, common’, duadds ‘even, level’, etc. Walde-P. 2.489.
33762:Av. hamaraéa-, lit. ‘meeting’, fr. ham- ‘together’ and ar- ‘reach, come to’. Cf. OPers. hamarana- ‘battle’. Barth. 1776
34415:Skt. rana-, Av. rana-, and epds. Skt. samara-, samarana-, Av. hamarana-, OPers. hamarana- : Skt. r- ‘rise, move’, Grk. dpvipe ‘stir up, rouse’, etc. Walde- P. 1.136.
```


## [2026-09-14T02:01:52.287Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nfor vol in ('BQT_v4_pages.txt',):\n    t=open(vol,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    for i,p in enumerate(pages):\n        for w in ('هامین','هامون','هان '):\n            if w in p:\n                m=re.search(r'\\[pdf page (\\d+)\\]',p)\n                print(vol, 'idx',i, m.group(1) if m else '?', w)\n                break\nEOF",
 "description": "Search BQT vol4 for هامین"
}
```


## [2026-09-14T02:01:53.395Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"سیم\\b\\|هامین\" ARY_pages.txt | head -20",
 "description": "Grep Aryanpur for sim/hamin"
}
```


### [2026-09-14T02:01:53.435Z] TOOL RESULT

```
BQT_v4_pages.txt idx 2 3 هان 
BQT_v4_pages.txt idx 3 4 هان 
BQT_v4_pages.txt idx 4 5 هان 
BQT_v4_pages.txt idx 6 7 هان 
BQT_v4_pages.txt idx 7 8 هان 
BQT_v4_pages.txt idx 8 9 هان 
BQT_v4_pages.txt idx 9 10 هان 
BQT_v4_pages.txt idx 10 11 هان 
BQT_v4_pages.txt idx 15 16 هان 
BQT_v4_pages.txt idx 16 17 هان 
BQT_v4_pages.txt idx 17 18 هان 
BQT_v4_pages.txt idx 18 19 هان 
BQT_v4_pages.txt idx 19 20 هان 
BQT_v4_pages.txt idx 20 21 هان 
BQT_v4_pages.txt idx 21 22 هان 
BQT_v4_pages.txt idx 23 24 هامون
BQT_v4_pages.txt idx 24 25 هان 
BQT_v4_pages.txt idx 25 26 هان 
BQT_v4_pages.txt idx 26 27 هان 
BQT_v4_pages.txt idx 27 28 هان 
BQT_v4_pages.txt idx 28 29 هان 
BQT_v4_pages.txt idx 30 31 هامون
BQT_v4_pages.txt idx 32 33 هان 
BQT_v4_pages.txt idx 34 35 هان 
BQT_v4_pages.txt idx 36 37 هان 
BQT_v4_pages.txt idx 39 40 هان 
BQT_v4_pages.txt idx 40 41 هان 
BQT_v4_pages.txt idx 45 46 هان 
BQT_v4_pages.txt idx 46 47 هان 
BQT_v4_pages.txt idx 48 49 هان 
BQT_v4_pages.txt idx 52 53 هان 
BQT_v4_pages.txt idx 53 54 هان 
BQT_v4_pages.txt idx 54 55 هان 
BQT_v4_pages.txt idx 57 58 هان 
BQT_v4_pages.txt idx 60 61 هان 
BQT_v4_pages.txt idx 61 62 هان 
BQT_v4_pages.txt idx 62 63 هان 
BQT_v4_pages.txt idx 63 64 هان 
BQT_v4_pages.txt idx 65 66 هان 
BQT_v4_pages.txt idx 67 68 هان 
BQT_v4_pages.txt idx 68 69 هان 
BQT_v4_pages.txt idx 69 70 هان 
BQT_v4_pages.txt idx 70 71 هان 
BQT_v4_pages.txt idx 71 72 هان 
BQT_v4_pages.txt idx 72 73 هان 
BQT_v4_pages.txt idx 76 77 هان 
BQT_v4_pages.txt idx 77 78 هان 
BQT_v4_pages.txt idx 81 82 هان 
BQT_v4_pages.txt idx 82 83 هان 
BQT_v4_pages.txt idx 84 85 هان 
BQT_v4_pages.txt idx 85 86 هان 
BQT_v4_pages.txt idx 86 87 هان 
BQT_v4_pages.txt idx 90 91 هان 
BQT_v4_pages.txt idx 92 93 هان 
BQT_v4_pages.txt idx 96 97 هان 
BQT_v4_pages.txt idx 97 98 هان 
BQT_v4_pages.txt idx 100 101 هان 
BQT_v4_pages.txt idx 103 104 هان 
BQT_v4_pages.txt idx 108 109 هان 
BQT_v4_pages.txt idx 109 110 هان 
BQT_v4_pages.txt idx 112 113 هان 
BQT_v4_pages.txt idx 115 116 هان 
BQT_v4_pages.txt idx 116 117 هان 
BQT_v4_pages.txt idx 120 121 هان 
BQT_v4_pages.txt idx 126 127 هان 
BQT_v4_pages.txt idx 129 130 هان 
BQT_v4_pages.txt idx 130 131 هان 
BQT_v4_pages.txt idx 132 133 هان 
BQT_v4_pages.txt idx 133 134 هان 
BQT_v4_pages.txt idx 136 137 هان 
BQT_v4_pages.txt idx 140 141 هان 
BQT_v4_pages.txt idx 141 142 هان 
BQT_v4_pages.txt idx 145 146 هان 
BQT_v4_pages.txt idx 147 148 هان 
BQT_v4_pages.txt idx 148 149 هان 
BQT_v4_pages.txt idx 149 150 هان 
BQT_v4_pages.txt idx 152 153 هان 
BQT_v4_pages.txt idx 156 157 هان 
BQT_v4_pages.txt idx 157 158 هان 
BQT_v4_pages.txt idx 162 163 هان 
BQT_v4_pages.txt idx 163 164 هان 
BQT_v4_pages.txt idx 164 165 هان 
BQT_v4_pages.txt idx 165 166 هان 
BQT_v4_pages.txt idx 166 167 هان 
BQT_v4_pages.txt idx 167 168 هان 
BQT_v4_pages.txt idx 169 170 هان 
BQT_v4_pages.txt idx 172 173 هان 
BQT_v4_pages.txt idx 173 174 هان 
BQT_v4_pages.txt idx 174 175 هان 
BQT_v4_pages.txt idx 179 180 هان 
BQT_v4_pages.txt idx 181 182 هان 
BQT_v4_pages.txt idx 182 183 هان 
BQT_v4_pages.txt idx 183 184 هان 
BQT_v4_pages.txt idx 185 186 هان 
BQT_v4_pages.txt idx 188 189 هان 
BQT_v4_pages.txt idx 192 193 هان 
BQT_v4_pages.txt idx 198 199 هان 
BQT_v4_pages.txt idx 199 200 هان 
BQT_v4_pages.txt idx 200 201 هان 
BQT_v4_pages.txt idx 202 203 هان 
BQT_v4_pages.txt idx 204 205 هان 
BQT_v4_pages.txt idx 205 206 هان 
BQT_v4_pages.txt idx 206 207 هان 
BQT_v4_pages.txt idx 212 213 هان 
BQT_v4_pages.txt idx 214 215 هان 
BQT_v4_pages.txt idx 217 218 هان 
BQT_v4_pages.txt idx 218 219 هان 
BQT_v4_pages.txt idx 221 222 هان 
BQT_v4_pages.txt idx 224 225 هان 
BQT_v4_pages.txt idx 225 226 هان 
BQT_v4_pages.txt idx 228 229 هان 
BQT_v4_pages.txt idx 230 231 هان 
BQT_v4_pages.txt idx 232 233 هان 
BQT_v4_pages.txt idx 233 234 هان 
BQT_v4_pages.txt idx 236 237 هان 
BQT_v4_pages.txt idx 240 241 هان 
BQT_v4_pages.txt idx 241 242 هان 
BQT_v4_pages.txt idx 242 243 هان 
BQT_v4_pages.txt idx 244 245 هان 
BQT_v4_pages.txt idx 246 247 هان 
BQT_v4_pages.txt idx 247 248 هان 
BQT_v4_pages.txt idx 252 253 هان 
BQT_v4_pages.txt idx 253 254 هان 
BQT_v4_pages.txt idx 254 255 هان 
BQT_v4_pages.txt idx 256 257 هان 
BQT_v4_pages.txt idx 257 258 هان 
BQT_v4_pages.txt idx 258 259 هان 
BQT_v4_pages.txt idx 260 261 هان 
BQT_v4_pages.txt idx 261 262 هان 
BQT_v4_pages.txt idx 262 263 هان 
BQT_v4_pages.txt idx 267 268 هان 
BQT_v4_pages.txt idx 268 269 هان 
BQT_v4_pages.txt idx 272 273 هامون
BQT_v4_pages.txt idx 273 274 هامون
BQT_v4_pages.txt idx 274 275 هان 
BQT_v4_pages.txt idx 276 277 هان 
BQT_v4_pages.txt idx 278 279 هان 
BQT_v4_pages.txt idx 284 285 هان 
BQT_v4_pages.txt idx 286 287 هان 
BQT_v4_pages.txt idx 287 288 هان 
BQT_v4_pages.txt idx 288 289 هان 
BQT_v4_pages.txt idx 292 293 هان 
BQT_v4_pages.txt idx 293 294 هان 
BQT_v4_pages.txt idx 296 297 هامین
BQT_v4_pages.txt idx 298 299 هان 
BQT_v4_pages.txt idx 299 300 هان 
BQT_v4_pages.txt idx 300 301 هان 
BQT_v4_pages.txt idx 304 305 هان 
BQT_v4_pages.txt idx 306 307 هان 
BQT_v4_pages.txt idx 307 308 هان 
BQT_v4_pages.txt idx 308 309 هان 
BQT_v4_pages.txt idx 314 315 هان 
BQT_v4_pages.txt idx 315 316 هان 
BQT_v4_pages.txt idx 316 317 هان 
BQT_v4_pages.txt idx 317 318 هان 
BQT_v4_pages.txt idx 321 322 هان 
BQT_v4_pages.txt idx 323 324 هان 
BQT_v4_pages.txt idx 324 325 هان 
BQT_v4_pages.txt idx 327 328 هان 
BQT_v4_pages.txt idx 330 331 هان 
BQT_v4_pages.txt idx 332 333 هان 
BQT_v4_pages.txt idx 339 340 هان 
BQT_v4_pages.txt idx 340 341 هان 
BQT_v4_pages.txt idx 342 343 هان 
BQT_v4_pages.txt idx 344 345 هان 
BQT_v4_pages.txt idx 345 346 هان 
BQT_v4_pages.txt idx 346 347 هان 
BQT_v4_pages.txt idx 347 348 هان 
BQT_v4_pages.txt idx 348 349 هان 
BQT_v4_pages.txt idx 349 350 هامون
BQT_v4_pages.txt idx 350 351 هان 
BQT_v4_pages.txt idx 356 357 هان 
BQT_v4_pages.txt idx 359 360 هان 
BQT_v4_pages.txt idx 361 362 هان 
BQT_v4_pages.txt idx 364 365 هان 
BQT_v4_pages.txt idx 365 366 هان 
BQT_v4_pages.txt idx 367 368 هان 
BQT_v4_pages.txt idx 368 369 هان 
BQT_v4_pages.txt idx 370 371 هان 
BQT_v4_pages.txt idx 372 373 هان 
BQT_v4_pages.txt idx 374 375 هامون
BQT_v4_pages.txt idx 375 376 هان 
BQT_v4_pages.txt idx 379 380 هان 
BQT_v4_pages.txt idx 385 386 هان 
BQT_v4_pages.txt idx 388 389 هان 
BQT_v4_pages.txt idx 390 391 هان 
BQT_v4_pages.txt idx 393 394 هامون
BQT_v4_pages.txt idx 394 395 هان 
BQT_v4_pages.txt idx 395 396 هان 
BQT_v4_pages.txt idx 398 399 هان 
BQT_v4_pages.txt idx 402 403 هان 
BQT_v4_pages.txt idx 404 405 هان 
BQT_v4_pages.txt idx 406 407 هان 
BQT_v4_pages.txt idx 409 410 هان 
BQT_v4_pages.txt idx 410 411 هان 
BQT_v4_pages.txt idx 414 415 هان 
BQT_v4_pages.txt idx 417 418 هان 
BQT_v4_pages.txt idx 419 420 هان 
BQT_v4_pages.txt idx 420 421 هان 
BQT_v4_pages.txt idx 421 422 هان 
BQT_v4_pages.txt idx 428 429 هان 
BQT_v4_pages.txt idx 431 432 هان 
BQT_v4_pages.txt idx 432 433 هان 
BQT_v4_pages.txt idx 433 434 هان 
BQT_v4_pages.txt idx 435 436 هان 
BQT_v4_pages.txt idx 436 437 هان 
BQT_v4_pages.txt idx 438 439 هان 
BQT_v4_pages.txt idx 444 445 هان 
BQT_v4_pages.txt idx 445 446 هان 
BQT_v4_pages.txt idx 446 447 هان 
BQT_v4_pages.txt idx 447 448 هان 
BQT_v4_pages.txt idx 448 449 هان 
BQT_v4_pages.txt idx 451 452 هان 
BQT_v4_pages.txt idx 454 455 هان 
BQT_v4_pages.txt idx 456 457 هامین
BQT_v4_pages.txt idx 457 458 هان 
BQT_v4_pages.txt idx 459 460 هامون
BQT_v4_pages.txt idx 460 461 هان 
BQT_v4_pages.txt idx 464 465 هان 
BQT_v4_pages.txt idx 467 468 هان 
BQT_v4_pages.txt idx 469 470 هان 
BQT_v4_pages.txt idx 471 472 هان 
BQT_v4_pages.txt idx 475 476 هان 
BQT_v4_pages.txt idx 476 477 هان 
BQT_v4_pages.txt idx 477 478 هان 
BQT_v4_pages.txt idx 479 480 هان 
BQT_v4_pages.txt idx 481 482 هان 
BQT_v4_pages.txt idx 483 484 هان 
BQT_v4_pages.txt idx 484 485 هان 
BQT_v4_pages.txt idx 487 488 هان 
BQT_v4_pages.txt idx 488 489 هامون
BQT_v4_pages.txt idx 489 490 هان 
BQT_v4_pages.txt idx 491 492 هان 
BQT_v4_pages.txt idx 493 494 هان 
BQT_v4_pages.txt idx 494 495 هان 
BQT_v4_pages.txt idx 495 496 هان 
BQT_v4_pages.txt idx 497 498 هان 
BQT_v4_pages.txt idx 500 501 هان 
BQT_v4_pages.txt idx 505 506 هان 
BQT_v4_pages.txt idx 506 507 هان 
BQT_v4_pages.txt idx 508 509 هان 
BQT_v4_pages.txt idx 514 515 هان 
BQT_v4_pages.txt idx 517 518 هان 
BQT_v4_pages.txt idx 520 521 هان 
BQT_v4_pages.txt idx 522 523 هان 
BQT_v4_pages.txt idx 523 524 هان 
BQT_v4_pages.txt idx 526 527 هان 
BQT_v4_pages.txt idx 529 530 هان 
BQT_v4_pages.txt idx 530 531 هان 
BQT_v4_pages.txt idx 532 533 هان 
BQT_v4_pages.txt idx 533 534 هان 
BQT_v4_pages.txt idx 537 538 هان 
BQT_v4_pages.txt idx 540 541 هان 
BQT_v4_pages.txt idx 542 543 هان 
BQT_v4_pages.txt idx 543 544 هان 
BQT_v4_pages.txt idx 547 548 هان 
BQT_v4_pages.txt idx 548 549 هان
```


### [2026-09-14T02:01:53.490Z] TOOL RESULT

```
171:کش و واکنش یکی از دلایل عمده‌ی تقسیم زبان واحد هندو اروپایی ابندا به گویش‌ها و سپس به
880:ِ تقسیم پندی زبانهای هند و اروپایی از نظر مکان جغرافیانی
935:تصویر کلی فرهنگ و جامعهی هند و اروپایی حدود شش هزار سال پیش را به تقریب ترسیم کنند.
1176:اروپایی نخستین را ترسیم نمایند. در چند دهه‌ی اخیر نیز زبانشناسان توانسته‌اند از راه همسنجی
3814:۲ معنی این واژه در سانسکریت: بخشنده) خداء تقسیم کننده,
6867:سیم موم
10934:| سیم (به چم آبخشی از برغ)
```


## [2026-09-14T02:01:59.334Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (456,):\n    print('==== idx',i)\n    print(pages[i][:4000])\nEOF",
 "description": "Print BQT v4 page with هامین"
}
```


### [2026-09-14T02:02:00.466Z] TOOL RESULT

```
==== idx 456
[pdf page 457]
همیدون نس
سره خوانشد - و بمعتی کمر و میان هم بنظر همیز ؟ - باناك مجپول وزای قله‌دار
آمس است۱ . سپ بروزن عزبز» بلفت زد ویازند(۱) بممتی‌تابستان
همیدون ؟ - ۸ باشد وبمربی تموز میگویند ؛ وبچلی زای نقطه.
پادال ابجد بواو کنید. ‏ 4.3 | داز نون هم‌بنظرآمده است که همین بروزن‌زمین
و پنون زده . مخفف هم بت باشد » الل‌اعلم .
ابدون است پمنی‌همین دم ۳۳۳۷ هميشك جوان* - بنش‌شن‌تردت
وهمین‌زمان وهمین‌سامت؟۴ - همیان وسکون‌کاف وجیم مفتوح وواو بالف کشیدهوبئون
وهمچنین - وعمین‌جا وهم اکنون وهمین لفی؛ [ زده . بوتهٌ کیاهیست که بر کهای‌آن همیده سببز
چه ایدون بمعنی این زمان و این دم واینجا | وخرم‌ونازه‌میباشدوآدرابمربی حی‌العالم میگویند
واینچنین‌باشد - وبممنی همچنین - وبيك تاکاء | ودر دواها بکار پرند - و نام بل جزو از اجزای
هم بنظرآمده است . اکسیرهم هست .* ۱

() چك: ژد وپاژند - ۰

۱ -قس : (عر) همیان: «بقالله همیان, بمنی اوبز رکه سرین‌است» «منتهی‌الارب» .

۴ - از: هم (پیشوند اعتراك) + ایدون (۸.م.) ۴ - امیر عمید گفت : « نظامی
لیامد؟» ملك جبال گفت: «* آمد ! ابنك آنجا شسته است .» امیرعمید کفت: « من نه این‌نظامی
را می‌کوم » آن نظامی دیگر است » ومن این‌را خود شناسم.» همیدون آن پادشام را دیدم که
متفر گشت ودرحال روی سوی من کرد وکفت: «جز نو جابی‌نظامی‌هست؟» «نظامی عروضی. چهار
مقاله طبم دوم نگارنده ص۴۸4 .

۴ - مسحف‌هسین ۳ «هامین»11813318بممنی‌تابستان,دراوستا 108832(ساسکر یت 8882۵
بمعنی سال) وئیز دراوستا 138133182 بممنی تابستانی وئیز تابستان آهده « پورداود . خرده اوستا
۳ ابیرونی. آثارالباقیه ص۹۳ »ی ۳:هامین». 8 - از: هميغك (صورت‌پپلوی«همیشه)
+جوان << همیشه جوان, قس: عمیشه بپار. مغقف آن «هميشك» است ۳ 52706۲۷1۷۷۲72
(فولری آ1]. 4۷۵) < حی‌المالم ۳ 0۳01۵ «عقار ۱۹۲ف -

0 همیشه - بفتح اول وچهارم (درلهجهٌ مرکزی بکسر چهارم) » پپلوی 1381285121
«منای ۲۷۹ (ر4: هميعك [جوان] ): کردی ع ۵6891806 ( همیشه. دائماً ) « ژابا س۰4۵۱
سنگری ۰8271966 سرخه‌بی888215086. لاسگر ری ۰888219046 شهمیرزادی153ط8ظ
« ۲.4 ۱۹۹ کیلکی ۰۵۳1903 نهرانی۵8۳1886 و80873831806؛ دایم» همواره»مدام.

5 همیعه بهار - بفتح اول وچهارم و ششم. از: عمیعه ۳ بهار؛ مخفقف و معرب آن
«میش بهار» « دزی جس4۲:۹۲۹؛ همیشه بهار بستانی (۲8164118) ازدستهٌ آفتایی‌ها دارای
کلهای زرد وفندقه‌های‌خمیده‌است که جز درزمتان‌های‌سرد همیشه گل دارد. بر گهای‌آن محرك
است وییشتر برای زینت کاشته میشود - عمیشه بپار کوعی (4۸170102) ازدستةٌ آقتابیه! دارای
بر گهای کر4 داراست که کلها ورشةٌ آن قی‌آوراست « کل کلاب ۲۹۶
```


## [2026-09-14T02:02:26.316Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'هاون' in p or 'هامون' in p and i>380:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print('idx',i,m.group(1) if m else '?', p[:90].replace('\\n',' / '))\nEOF",
 "description": "Locate BQT v4 ها section"
}
```


### [2026-09-14T02:02:27.485Z] TOOL RESULT

```
idx 16 17 [pdf page 17] / مادر آب وآش -۱۹۳ / مادر آب و آتش - بکسر راق ‏ | خوانند . خوردن‌آن قوت باه دهد 
idx 39 40 [pdf page 40] / -۱۹۵۷- مامیار / پهلوی شهر ومملکت راکویند که عربان مدینه | ازکشته شدن آبرج معلو
idx 102 103 [pdf page 103] / همن‌زایده امه / شهر شیراز است . چه کوبند شیراز را عمرولیت مفن دایاده - شخسی ب
idx 123 124 [pdf page 124] / -4۱< مندیش / اش / و ی گوبند مندل شهریست در زمین هند که | مندبور اس ت که مفلوك و
idx 145 146 [pdf page 146] / نها مهراسفند. / هم والی کابل ات که رستم از دختر او تولد | بمعنی هاون باشد مطف
idx 292 293 [pdf page 293] / نویده ۱۰۳ / نویده" بروزن‌خمیده, بمعنی‌لرزیده | کوبند که‌از درخت‌رسته باشدوعر 
idx 296 297 [pdf page 297] / نهائه که ۷۱-۳ /  / نهاله 4۳ ۱ - بکر اول و قح کاف خانه پسازند - وخانه‌ای را نیز 
idx 297 298 [pdf page 298] / -۷۱۵- به رزاق : /  / دملوند باغد وآن از عراق مجم است ۱ - ولوح | پیچیدن و پیچ وت
idx 374 375 [pdf page 375] / وئانه ۹۳ / بل و بلکه هم هست که كلمهٌ ترقی باشد ‎٩‏ - | اسیرم راکوبند و بمربی 
idx 393 394 [pdf page 394] / ۹۳۱۱۳ هامرن /  / ات بعنی برخیز. هم‌آمده است . /  / هامی! * بنم‌ميم وسکون دون,مخفف ه
idx 394 395 [pdf page 395] / هأمی 2۳۱۳۳ / هامی!۱ * پروزن جامی » سرگشته و هانی؟ < بروزن‌کالی ۰" بزبان پپلوی
idx 395 396 [pdf page 396] / ۲۳۱۳۳ های های / معروف است ۱ - و کنایه از فرج زدان یمنی هایاهای ۱ - با ستای ر 
idx 459 460 [pdf page 460] / << هند / هنجام « بختح اول پروزن اندام؛مردم | کنند وبمربی غملول (۱) خوانند . / ب
idx 481 482 [pdf page 482] / ۳۹۹ اه / بقیه از حاشیةٌ صفحهٌ قبل / نوشابه‌را روی آتش میربشتند. الکلی که درآن‌و
idx 488 489 [pdf page 489] / هیر -۲4۹- / که درتمام عمر با زنان نزدیکی نکرده است . هیرون؟ بکسراول وضم ثالث‌
idx 495 496 [pdf page 496] / -4۱۴- بلو / فرخانلی نگاه داشتن باشد - وبمعنی بیداری هم بادندان* > بفتح ثالك و
idx 496 497 [pdf page 497] / بارا ۹۱۳ / کقباتد ۰.۱ بتقدیم بار براسفند بنظم آورده است ۴ . / یا)؟ « بر وزن خار
idx 504 505 [pdf page 505] / بانه << / کثف خواند ۱ - و بترکی طرف و جاب را | یابد است که از پافتن باشد چه د
```


## [2026-09-14T02:02:33.090Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (393,394):\n    print('======= idx',i)\n    print(pages[i][:4500])\nEOF",
 "description": "Print BQT v4 pages with هان"
}
```


### [2026-09-14T02:02:34.451Z] TOOL RESULT

```
======= idx 393
[pdf page 394]
۹۳۱۱۳ هامرن

ات بعنی برخیز. هم‌آمده است .

هامی! * بنم‌ميم وسکون دون,مخفف هامواره؟ بروز ن گاهواره, پمعنی
هامون است که زمین هموار ودشت سخت باشد | هامواراست که هموار و بيك طربق و برایر - و
که قبول باران نکند. همیشگی وپبوسته باشد۴ .

هام ار؟ - بواویروزن نامدارءپممتی هامون؟* » بروزن‌قارون » بمعنی‌دشت
برابر وبيك طربق وهموارباشدیمنی پستی‌وبلندی | وصحرا وزمین هموار وخالی از بلندی و پستی
قداشته باشد ویمعنی پیوسته وهموارموهمیشگی | باشد وبعربی قاع خواش۹ .

‎٩‏ اه هامون (هم.) .۲ < هبوار (م.) از: هام (* هم) ‏ واز ات هامواره
(و.م.): « وهردورآییا کند ازسبیکه‌هاه زر وسیم » وسرش‌بزعفران هاموار کرد ...» «مجمل‌التواریخ
والقضص س4۹۹* ور : اسآمقدمه مرربح . ۴ هاموار (ه.م.) * همواره (.م.) ور4:
هموار. ۴ - پربرویان کیتی هامواره شده بر پزمگاه او نظاره."

‏فغرالدین کر کانی «فرهنگه نظام».

‏* <هامن (۸.م.)هرن وجه اشتقاقی برای این‌کلمه نقل کرده«اسشق ۱۶۸۸ که‌هوبشمان
«اناً6۱۰۸۸آ را قطعی نمیداند. پهلوی7820880-8200878 ارط 120176718,601160طه۴)
( ۸5208.1.0.3 قی : طبری [8۳28ظ ( سحرا, زمین هموار) » مازدرانی کنوای
2۵ 22ص , #مقس36 عقصقط. ۵۳۸20ط تواژ امه ۸4۹ ۰

‏- همیشه تاکه بهاران وروز کاربهار فرولهد ز برکوه سر بهامون هین.

‏«فرخی سیستانی. دبوان ۰۲۹۹
بقیه از حاشیةٌ صفحهةٌ قبل
که «برخیز» . پی کسری بدین فال کرد وهآمرز راگفت : «نام توچنین است که برخیز » وممنی
ام دشمن توایدون است که بنشین . اکنون بای که برخیزی وظفر‌ترا بود.» وخود این فال راست
نيامد...» (ازسخة تاریخ بلعمی‌متعملق یکتابغان دهغد!) ور: لغت نامه : ذوقار . خمزة اسفهانی
نام او را « الهامرز بن‌آذ رکر » نوشته وموّلف مجمل‌التواریخ والقص لام پدر او را « او رکوفی»
آورده است > «مجمل‌التواریخ ص ۱۷۹ متن و حاشیه > جوالیقی درالمعرب ( ص ۳۵۲ ) کوید :
«الهامرز ۰ اسم بعض مرازبة کسری » وکان علی ميمنة جیشه یوم ذی قار وقال هالیء بن قبيصة :
متی بلقنا الپامرز نصف بیومه و تخذله اقیاله و مرازبه .>
ابن‌البلخی درفارسنامه (س۹-۱*۹) این‌جنگه وسر‌داری «هامرز» را بزمان کسری‌اپرویز
این‌هرمز لقل میکند . هدایت نیزدر انجمن‌آرا این‌داستان را بزمان(خسرو) پرویز بت میدحد.
بنظرمیرسد که «ها» درین دوکلمه پیشوند فعل‌باید (چنانکه دریض‌اوجه‌ها هنوز مستعمل است :
در دیه‌های‌ارا (سلطان]آباد) هاگیر ۳ بگیر, هاده * بده, هاگفت * بگفت «مکی نژاد»» گیلکی
هیر ۳ بگیر» هدم ۳ بده). ودلی» بجای «لیش» بمعنی بنشین باشد (قس: اراکی(سلطانآپادی)
هایش ۳ بنشین «مکی‌نژاد» ) » ولی مرز 138۳2 با 1308۳28 درپهلوی بمعنی مالیدن «لیب رکه
۷ ومعانی دیگرست (رك : مرزء مالیدن) که بابرخاستن تناسبی ندارد ؛ موّلف فرهنگه
نظام «هامرز» رامسحف «هابرز» (بایاه موحده) داند (برزیمعنی بلند [قی : البرز] ) ۰ وانی» در
«عانی» را بمعنی پایین گرفته کوید : «تفأل پرویز از اين باب بوده ومعنی نام سردار خودش بلند
وبالا بوده ومعنی نام سردار عرب در پهلوی پاییین وپست.»

======= idx 394
[pdf page 395]
هأمی 2۳۱۳۳
هامی!۱ * پروزن جامی » سرگشته و هانی؟ < بروزن‌کالی ۰" بزبان پپلوی
حیران مانده را کویند . آمر به‌نشستن باشد یمنی بنشین .
قامیان؟ - بروزن آسان . همیانرا هاوش؟ - بت واروسکون خین‌نط.
کوبند وآن کيسةٌ درازی باشد که زردرآن کنند | داره امت راکوبند مطلفاً یمنی‌امت «رپیغمی رکه
وب رگمربندند . باشد - وترجمة متعلق هم هست.
هان < بروزن‌کان,کلمةٌ تنبیه استبمنی هاوشت* ی واو وسکون شین و
درمحلآ گاهانیدن وتا کیددرکاری‌وامری‌بکاربرند | تای قرشت » بمعنی هاوش باشد که امت پیغمبر
خواء بطریق امرباشد وخواء بعنوان نهی, وخواء | است - و ترجمةٌ متعلق هم هست بلفت زدد و
بخوش طبمی وظرافت وخواء بتصدیق وجد۴ و | پازند (۱) ۰
امربشتاب کردن هم هست یمنی بشتاب‌وجلدبای. | اون ‎٩‏ - بفتح واو و سکون هون ,
سس سس ی

() چك : ژد و پاژد . :

۹ «هامی » سرگردان بود.» «لفت فری ص۳۵۲۹:

استه وفامی شدم ز درد جدایی " هامی ووامی شدم ز خستن مترب.

منجك (منجيك) «لفت فرس‌س6۳۱.

۲ <دهییان (وم.) امیان:

هامیان از سیم وزر پرداختن بهکه سنگه منجنیق انداختن .

سمدی شیرازی . ر4: مزدیتا ص۲4۵.
با زر چو باز کردد آزو بیم آن بود زایرش راکه بگلد از هامیان میان.
لامعی جرجانی «فرهنگه فظام».

۴ -قی : هبن ؛کردی 388 (كومك . وسیفه) » قن : فارسی : هبن (منت) « ژابا

ار هد نها
مان قی‌دلمبرت بین ازدیده نظرکن‌هان ! ایوان مدالن را آبینهٌ عبرت دان !

1 «خأقانی غشروانی . دبوان صس۳۹۲*.

۴ - رك : هامرز . ۴ -ر4 : هاوشت . * - پهلوی 8۸۷1681 مغ
(ررخانی‌زرتشتی) » موبد «یولکرص۹4 ؛ شاکرد . روحالی جوان ( زرتشتی ) که در مراسم دینی
بقربانی کننده » پاری کند «دهارله ص۷۵>. دراوستا 8۵۷18۷068 آمده که درفرهنگهای فارسی
خزولغات زند وپازند ضبط شده وبمعنی امت گرفته‌اند «پورداود . خرده اوستا سح

‎٩‏ اوستا 84۷۵02 (هاون) . پهلوی 88۰88 ۰ ارمنی ع » لهجدٌیپودبان
جبال قنتازع 36۷۵۵ . معرب هاون 8۷28 « اسشق ۹*۸۹ درتعریب هاون (بفتح واو)وهاوون
ی واو اول )آمده « اين‌دزید > ۸« تفس» ۰ جمع‌آن « اهوان »> است « دزی جص44 ۷ کردی
(هاون ) « ژابا س 4۵4 ۰ 38۷68 , 8۷60 ۶ ژابا س 4۳۹ ۲ ۵6۷6۴ « ژابا
س 40۹ کبلکی 88۷888 (هاون ) » در اراك (سلطانآباد) ۵8۷308 (هاون) «مکی‌نزاد».
اساسا هاون ( هاونه اوستایی) ظرفی‌است که زرتشتیان درآن «هوم» (ه.م.) را با دسته می کوین
ولیز اهاون در دین زرتعتی بمنوان زنگه (ناقوی) بکار میرفت - عموماً هاون و دستةٌ آنرا از هس
آمباخته‌اند « دارمستتر . زید اوستا جاص آ]] 1-227 > ؛ ورك : پوردآود . بشتها اس 2۹۹ 4 م +
همین . مزدیستا . ص ۲۳۳ .
```


## [2026-09-14T02:02:58.366Z] TOOL CALL #50: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sumaraz\" \"https://www.etymonline.com/word/sir\" \"https://www.etymonline.com/word/senior\" \"https://vajehyab.com/dehkhoda/%D9%87%D8%A7%D9%85%DB%8C%D9%86\" \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7%D8%AA%D9%88%D8%B1/\" \"https://abadis.ir/fatofa/%D9%85%D8%B3%DB%8C%D9%88/\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 443 verification\" 2>&1 | tail -1; done",
 "description": "Fetch more sources"
}
```


### [2026-09-14T02:03:04.715Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/dfceec5faced12dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ad3379f21a07676.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e9a1c086ac14d0e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dcb4f5f5454818f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ecdf168810dc2d19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e429423d54dcd649.txt
```


## [2026-09-14T02:03:08.233Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in dfceec5faced12dc 8ad3379f21a07676 dcb4f5f5454818f7; do echo \"=========== $f\"; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt',encoding='utf-8').read()\nfor kw in ('Etymology','هامین','From Proto-Germanic','sire'):\n    i=t.find(kw)\n    if i>0:\n        print('---',kw); print(t[i:i+1200]); break\nEOF\ndone",
 "description": "Read fetched pages"
}
```


### [2026-09-14T02:03:09.676Z] TOOL RESULT

```
=========== dfceec5faced12dc
--- Etymology
Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Inflection 

 1.3.2 
 Derived terms 

 1.3.3 
 Descendants 

 1.4 
 See also 

 1.5 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Germanic/ sumaraz 

 Add languages 

 Reconstruction 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Germanic
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Indo-European *sm̥-h₂-ór-o- , (cf. Old Armenian ամառն ( amaṙn , “ summer ” ) ), an oblique r -stem based on *s(e)m-eh₂- ( “ summer, year ” ) (cf. Tocharian A ṣme , ṣmāye , Sanskrit समा ( sámā , “ season, year ” ) , thematicized differently in Proto-Celtic *sam
=========== 8ad3379f21a07676
--- Etymology
Etymology, Origin & Meaning

Sir - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of sir 

 sir 

 title of honor of a knight or baronet (until 17c. also a title of priests), c. 1300, a variant of sire (q.v.) that was used originally only in unstressed position. It is not an acronym of anything . 

 It was generalized as a respectful form of address by mid-14c., and eventually extended to all equals or used without regard for rank. It has been used as a salutation at the beginning of letters from early 15c. As a noun, "person of rank or importance," from 14c.
 also from 17c. 

 Entries linking to sir 

 sire (n.) 

 c. 1200, a title placed before a name and denoting knighthood, from Old French sire "lord (appellation), sire, my lord," from Vulgar Latin *seior , from Latin senior "older, elder" (from PIE root *sen- "old"). Later sir (q.v.), an alteration of sire , was used for this.

 Wulcume sire Arður, wilcume lauerd.

 [Laʒamon's "Brut," c. 1200]

 Standing alone and meaning "your majesty" it i
=========== dcb4f5f5454818f7
--- هامین
هامین | لغت‌نامه دهخدا | واژه یاب

'
 />

 معنی هامین | لغت‌نامه دهخدا | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 هامین

 لغت‌نامه دهخدا
 هامین . (اِ) وزنی برابر بیست وپنج استار. (فرهنگ نظام ). رجوع به استار شود. ابن سینا در قانون نقل نموده که هامین پنج استار است و بیست درهم و چهار اوبولو . (از فرهنگ نظام ). وزنی معادل بیست وپنج استار و چهار اوبولو. (یادداشت به خط مؤلف ).

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-14T02:03:21.325Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in ecdf168810dc2d19 e429423d54dcd649; do echo \"==== $f\"; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt',encoding='utf-8').read()\ni=t.find('فرهنگ فارسی معین')\nif i<0: i=t.find('معین')\nprint(t[max(0,i-200):i+900])\nEOF\ndone",
 "description": "Read abadis senator/monsieur"
}
```


### [2026-09-14T02:03:22.491Z] TOOL RESULT

```
==== ecdf168810dc2d19
 : senator 

 دنبال کنید 

 لغت نامه دهخدا

 سناتور. [ س ِ ت ُ] ( فرانسوی ، اِ ) وکیل مجلس اعیان. وکیل مجلس سنا. 

 فرهنگ فارسی

 عضوسنا، نماینده درمجلس سنا
( اسم ) عضو سنا وکیل مجلس اعیان . 

 فرهنگ معین

 (س ) [ فر. ] (اِ. ) عضو مجلس سنا، نماینده مجلس اعیان . 

 فرهنگ عمید

 عضو مجلس سنا. 

 مترادف ها

 holdover (اسم) 
 تمدید، سناتور

 فارسی به عربی

 عضو مجلس الشیوخ 

 پیشنهاد کاربران

 منبع. عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی

 سناتور ؛ زندگی دهنده یا شخص ایجاد کننده ی شرایط زندگی. 
حالا این مفهوم چطور در دل این کلمه وجود دارد در متن تحلیلی زیر تبیین شده است؛
لا تَأْخُذُهُ سِنَةٌ وَ لا نَوْمٌ ؛ در اینجا برای کلمه ی سنتهٌ از کلمه ی أخذ استفاده شده که از یک زاویه احتمالاً منظور قرآن از کلمه ی سنتهٌ زنده شدن و زندگی باشد. یعنی از کسی زنده نشده و زندگی أخذ نمی کند. نه تنها از کسی زندگی أخذ نمی کند بلکه سناتور و زندگی بخش است. 
 ... [مشاهده متن کامل] 
 و از یک زاویه دیگر احتمالا منظور قرآن أخذ سن و سال بوده باشد به طوری که یکی از چهارده بُعد کلمه انسان همین مفهوم سن و سال در این کلمه است یعنی خدا مثل انسان و مخلوقات دچار پیر سنی نمی شود که هر دو برداشت هم برای وجود خدا قابل پ
==== e429423d54dcd649
تداول عامه ، خطاب به اقلیت مسیحی ارامنه و یا آشوریها گفته میشود ونیز در خطاب به فرنگیان و فرنگی مآبان مستعمل است. 

 فرهنگ فارسی

 ( اسم ) آقا ( در خطاب بفرنگیان یافرنگی مابان مستعمل است ) . 

 فرهنگ معین

 (مُ یُ ) [ فر. ] (اِ. ) آقا (در خطاب به فرنگیان گفته می شود. ) 

 دانشنامه عمومی

 مَسیو ( به فرانسوی: Massieux; تلفظ فرانسوی:  ​ ) یک کمون در بخش ان در شرق فرانسه است. 
مسیو ۳ کیلومتر مربع مساحت دارد و ۴۸۳ متر بالاتر از سطح دریا واقع شده است. 
 wiki: مسیو 

 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف 

 مترادف ها

 monsieur (اسم) 
 ارباب، آقا، مسیو
 signor (اسم) 
 آقا، شخص محترم، مسیو

 پیشنهاد کاربران

 منبع. عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی

 + عکس و لینک 

 دیکشنری آبادیس

 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کن
```


## [2026-09-14T02:03:31.992Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('43e013b4e13e384c.txt',encoding='utf-8').read()\ni=t.find('Origin and history of senate')\nprint(t[i:i+1800])\nEOF",
 "description": "Read etymonline senate"
}
```


### [2026-09-14T02:03:33.109Z] TOOL RESULT

```
Origin and history of senate 

 senate (n.) 

 c. 1200, "the legal and administrative body of ancient Rome," from Old French senat or Latin senatus "highest council of the state in ancient Rome," literally "council of elders," from senex (genitive senis ) "old man, old" (from PIE root *sen- "old").

 It is attested from late 14c. in reference to governing bodies of free cities in Europe (Italy); of national governing bodies from 1550s (typically the upper or less-numerous branch of the legislature). The specific sense of "upper house of the U.S. legislature" is recorded from 1775.
 also from c. 1200 

 Entries linking to senate 

 *sen- 

 Proto-Indo-European root meaning "old."

 It might form all or part of: monseigneur ; seignior ; senate ; senescent ; seneschal ; senicide ; senile ; senility ; senior ; seniority ; senor ; senora ; senorita ; shanachie ; Shannon ; signor ; sir ; sire ; surly .

 It might also be the source of: Sanskrit sanah "old;" Avestan hana- "old," Old Persian hanata- "old age, lapse of time;" Armenian hin "old;" Greek enos "old, of last year;" Latin senilis "of old age," senex "old, old man;" Lithuanian senas "old," senis "an old man;" Gothic sineigs "old" (used only of persons), sinistra "elder, senior;" Old Norse sina "dry standing grass from the previous year;" Old Irish sen , Old Welsh hen "old."

 -ate (1) 

 word-forming element used in forming nouns from Latin words ending in -atus , -atum (such as estate , primate , senate ). Those that came to English via French often arrived with -at , but an -e was added after c. 1400 to indicate the long vowel. The suffix also can mark adjectives formed from Latin past participles in -atus , -ata (such as desolate , moderate , separate ); again, they often were adopted in Middle English as -at , with
```


## [2026-09-14T02:03:35.339Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CE%B7%CE%BC%CE%BF%CF%82\" \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7/\" \"https://www.iranicaonline.org/articles/greek-loanwords-in-middle-iranian-languages\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 443 verification\" 2>&1 | tail -1; done",
 "description": "Fetch Greek asemos and Persian sena"
}
```


### [2026-09-14T02:03:43.532Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4ac8a6d5d7ff579b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb8537025c1da307.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee9c07c19c06c1d1.txt
```


## [2026-09-14T02:03:47.258Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('4ac8a6d5d7ff579b.txt',encoding='utf-8').read()\ni=t.find('Ancient Greek')\nprint(t[i:i+1500])\nEOF\necho \"===== sena =====\"\ncd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('fb8537025c1da307.txt',encoding='utf-8').read()\ni=t.find('فرهنگ معین')\nprint(t[max(0,i-900):i+500])\nEOF",
 "description": "Read Greek asemos and Persian sena entries"
}
```


### [2026-09-14T02:03:48.377Z] TOOL RESULT

```
Ancient Greek 

 Toggle Ancient Greek subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Adjective 

 1.4.1 
 Declension 

 1.4.2 
 Quotations 

 1.4.3 
 Derived terms 

 1.5 
 Further reading 

 Toggle the table of contents 

 ἄσημος 

 5 languages 

 Ελληνικά 
 Français 
 Latviešu 
 Malagasy 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Ancient Greek
 [ edit ] 

 Alternative forms
 [ edit ] 

 ἄσᾱμος ( ásāmos ) — Doric 

 Etymology
 [ edit ] 

 From ἀ- ( a- ) +‎ σῆμα ( sêma ) +‎ -ος ( -os ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /á.sɛː.mos/ → /ˈa.si.mos/ → /ˈa.si.mos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /á.sɛː.mos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈa.se̝.mos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈa.si.mos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈa.si.mos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈa.si.mos/ 

 Adjective
 [ edit ] 

 ἄσημος • ( ásēmos )  m or f ( neuter ἄσημον ) ; second declension 

 without mark or sign 

 uncoined ( of a precious metal ) 

 giving no sign, unintelligible 

 leaving no 
===== sena =====
یباً بدون انحنا و برگچه هایش در قاعده کمی نامتقارن است. سنای هندوستانی. ( از فرهنگ فارسی معین ).
 سنا. [ س ِ ] ( فرانسوی ، اِ ) مجلس سالخوردگان که اعضای آن سران روحانی و غیرروحانی ملت اند. ( ایران باستان ). مجلسی که اعضای آن از بزرگان و اعیان کشور برگزیده شوند. مجلس اعیان.
- سنای پانصدنفری ؛ سنای پانصدنفری مجلسی بود که کلیس تنس در سال 510 ق.م. از تریبوس های ده گانه آتن در آن شهر تأسیس کرد. عده اعضای سناتا آن زمان چهار نفر بود. کلیس تنس به طرفداری طبقات پست مقرر داشت که هر یک از تریبوس های ده گانه پنجاه نفر عضو انتخاب کند و بدین طریق عده اعضای سنا را به پانصد نفر رسانید. ( تاریخ تمدن قدیم ایران ). 

 فرهنگ فارسی

 مجلس اعیان، مجلس شیوخ، سالخوردگان رجال معروف
( اسم ) مجلسی که اعضای آن از بزرگان و اعیان کشور بر گزیده شوند مجلس اعیان . توضیح تعداد نمایندگان مجلس سنا در ایران ۶٠ تن بود که ۳٠ تن منتخب ملت و ۳٠ تن منتخب شاه که ( ۱۵ تن از تهران و ۱۵ تن از شهرستانها )
روشنی کمتر از ضیا و نور 

 فرهنگ معین

 (سَ ) [ ع . ] (اِ. ) گیاهی است از تیرة پروانه واران (سبزی آساها ) که دارای چند گونه است . برگ هایش متناوب و مرکب بدون برگچة انتهایی است . گل هایش زرد رنگ و میوه اش نیامک و محتوی چند دانه است . میوه و برگ مختلف سنا دوای تلخ مسهلی است که به صورت دم کرده یا پو
 (س ) [ فر. ] (اِ. ) مجلسی که اعضای آن از بزرگان و اعیان کشور برگزیده شوند. 

 فرهنگ عمید

 مجلسی که در کنار مجلس شورا در برخی از کشورها، به امر قانون گذاری می پردازد.
۱. ضیا، روشنایی، روشنی، فروغ.
۲. رفعت، بلندی.
گیاهی گرمسیری ب
```


## [2026-09-14T02:04:00.112Z] TOOL CALL #56: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85/\" --note \"page 443, Mo'in entry for سیم\" 2>&1 | tail -1",
 "description": "Fetch Mo'in entry for sim"
}
```


### [2026-09-14T02:04:03.173Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f6630de30854ea4e.txt
```


## [2026-09-14T02:04:03.345Z] TOOL CALL #57: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg443.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/443.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/443.png",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-14T02:04:03.424Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77924 Sep 13 22:04 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/443.png
```


## [2026-09-14T02:04:06.121Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('f6630de30854ea4e.txt',encoding='utf-8').read()\ni=t.find('فرهنگ معین')\nprint(t[i:i+900])\nEOF",
 "description": "Read Mo'in sim entry"
}
```


### [2026-09-14T02:04:07.153Z] TOOL RESULT

```
فرهنگ معین

 [ په . ] (اِ. )۱ - نقره . ۲ - پول ، وجه . ۳ - فلزی قیمتی که در معادن به طور خالص یا به صورت ترکیب با فلزات دیگر (انتیمون ، سرب ) یافت می شود و چون آن را با مس ترکیب کنند محکم تر می گردد و در صنعت کاربرد زیاد دارد. ۴ - مفتول ، رشتة باریک فلزی . ۵ - یک یا 
 (اِ. ) چرک ، خونابه .
 (اِ. ) چوب هایی که برزگران بر دو طرف چوبی که بر گردن گاو زراعی گذارند، بندند، یوغ . 

 فرهنگ عمید

 = شیم šim
چرک و خونابه که در زخم و جراحت جمع شود.
* سیم کشیدن: (مصدر لازم ) [عامیانه]
۱. (برق ) یک یا چند رشتۀ باریک و بلند ساخته شده از فلزی با رسانایی بالا که برای انتقال برق یا سیگنال های الکتریکی به کار می رود: سیم برق، سیم تلفن.
۲. (شیمی ) = نقره
۳. (موسیقی ) رشتۀ نازک فلزی که روی بعضی آلات موسیقی، مانند تار و سه تار، می کشند و با زخمه زدن یا کشیدن ابزار موسیقیایی بر آن، مرتعش شده و تولید صدا می کند.
* سیم کشیدن: (مصدر لازم ) کشیدن و امتداد دادن سیم برق، تلفن، یا تلگراف از جایی به جای دیگر و وصل کر
```


## [2026-09-14T02:04:54.448Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD band3 sem/sen ===\"; grep -n \"sem-\\|sen(o)\\|seno-\" WLD_band3.txt | head -10\necho \"=== IEC summer ===\"; grep -n \"semos\\|sema \\|sm̥ero\\|'summer'\" IEC.txt | head -10\necho \"=== LAT senex ===\"; grep -n \"senex\" LAT.txt LEW_1910.txt | head -6\necho \"=== SKT senate/sir/summer ===\"; grep -n \"^Senate\\|^Sir\\|Summer, \\|senate, \" SKT.txt | head -10\necho \"=== KLN senate/sir ===\"; grep -n \"senate,  n\\|^sir,  n\\|sire,  n\" KLN_1966.txt | head -6",
 "description": "Additional consulted sources"
}
```


### [2026-09-14T02:04:54.582Z] TOOL RESULT

```
=== WLD band3 sem/sen ===
3103:(junger) = merjo- 231%. 2. sem- ASS*, | “oy 440%, Mantel wy- 48*, | mittenin, hinein 2. me- 290" | nachatellen 1. de- 808. Marder 13. %er- 287. mittiherer medhio- SH1* | nachesnchen 3. reu- 350".
=== IEC summer ===
=== LAT senex ===
LAT.txt:122:senex, niidus, et, naturellement, les pronoms personnels,
LAT.txt:266:senex, suSuis et leuis se d£noncent comme indo^-europ^ens
LAT.txt:4210:anus, -us f.: vieille femae; joint k senex, oppos6 k puer. Sert
LAT.txt:6447:e.g. dans TerHaut.38, neque semper seruos currens, iratus senex,\
LAT.txt:9409:pel. casnar "senex", et v.h.a .hasan "brillant, joli"j' *-ko- dans lat.
LAT.txt:21373:"feaae", coapagne du "aari": Ov., M.8,704, senex ( Philemon) et femina
=== SKT senate/sir/summer ===
10797:Sirloin,  surioin.  (F. - L.)  M.E. snr^ hyn\  XV  cent.  —  O.  F.  surhngt  U4th cent.),  the  surluiu. * F.  jMr,  upon,  above; iongty  loin  (above).  %  TTie  story  abont taming  the  tain  into  sir-ioim  by  knighting it  is  mere  trash.
16854:Senate,  a  council  of  clden.  (F. «  L.)  F. seita/.  —  h.sena/um,  ace.  ol  renafus,  cooQcil of  elder*.  ^  L.  sen  ex,  old,  sen-ium,  old age.  Cf.  O.  Gk.  tvot,  old,  Goth.  linii^, \V.  Men,  O.  :^kt.  snna.  old.
17320:Sir,  Sire ;  see  Sdnata.
17321:Siren.  (L,-Gk  )    Lri/w.-Glc. a  nymph  who  enticed  sea*mm  lo tion  by  her  ma^ic  song ;  allied  to pit« ;  see  Syringe.
17322:Sirloin,  for  Surloin  ;  see  Lumbar.
17324:Sirocco ;  see  Baraeen.
17325:Sirrah;  see  Senate.
17332:Sirup ;  see  Sherbet.
=== KLN senate/sir ===
11038:desire,  n.  —  OF.  desir  (F.  desir),  fr.  desirer.  See
23655:Messidor,  n.,  name  of  the  10th  month  of  the French  revolutionary  calendar  (lasting  fr.  June 19th  to  July  18th).  —  F.,  a  hybrid  coined  by Fabre  d'Lglantine  in  1793  fr.  L.  messis,  ‘har¬ vest’  [fr.  mess-(um),  pp.  stem  of  metere,  ‘to  reap, mow,  crop’],  and  Gk.  8u>pov,  ‘gift’.  For  the  first element  see  mow,  ‘to  cut  (grass)’,  for  the  second see  donation  and  cp.  the  second  element  in Fructidor,  Thermldor. messieurs,  n.,  pi.  of  monsieur, messire,  n.,  a  French  title  of  honor  and  form  of address.  —  OF.,  nom.,  lit.  ‘my  lord’.  See  mon¬ sieur,  seigneur,  sire.
34543:senate,  n.  —  ME.  senat,  fr.  OF.  senat  (F.  senat), fr.  L.  sendtus,  ‘senate’,  lit.  ‘the  council  of  the elders’,  fr.  senex,  gen.  senis,  ‘old’.  See  senile  and subst.  suff.  -ate.
35333:sir,  n.  —  Reduced  form  of  sire,  orig.  used  only  in unstressed  position.
35336:sirdar,  n.,  military  commander  in  India,  Afgha¬ nistan  and  Pakistan.  —  Hind,  sirdar,  fr.  Pers., contraction  of  silali-ddr.  See  silladar. sire,  n.  —  ME.,  fr.  OF.  sire,  fr.  mseior,  vulgar form  of  L.  senior,  ‘older’,  compar.  of  senex.  See senior  and  cp.  sir.  Cp.  also  seignior,  senhor, senor,  sieur,  signore.
39854:transire,  n.,  a  customs  document  describing  the cargo  of  a  ship  for  the  sake  of  clearing  it.  —  L. transire,  ‘to  go  across’.  See  transient  and  cp. transit.
```


## [2026-09-14T02:05:01.872Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^senile,  adj\\|senile,  adj\\|^senior,  adj\\|senior,  adj\\|monsieur,  n\\|senator,  n\" KLN_1966.txt | head -8",
 "description": "Klein senile/senior/monsieur"
}
```


### [2026-09-14T02:05:02.258Z] TOOL RESULT

```
24341:Monroe  doctrine,  the  doctrine  laid  down  by President  Monroe  of  the  United  States  in  his message  to  Congress,  Dec.  2,  1823. monseigneur,  n.,  a  French  title  of  honor.  —  F., lit.  ‘my  lord’,  fr.  mon,  ‘my’,  and  seigneur,  ‘lord’, F.  mon  derives  fr.  L.  meum,  acc.  of  metis,  ‘my, mine’,  which  is  rel.  to  me,  ‘me’,  mihi,  ‘to  me’ ;  see meum,  me.  F.  seigneur  comes  fr.  L.  seniorem,  acc. of  senior,  ‘older’;  see  seigneur  and  cp.  next word.  Cp.  also  monsignor, monsieur,  n.,  the  French  equivalent  of  English Mr.  —  F.,  lit.  ‘my  lord’,  compounded  of  mon, ‘my’,  and  sieur,  ‘lord’,  a  shortened  form  of seigneur.  See  prec.  word  and  cp.  messire. monsignor,  n.,  a  title  conferred  on  some  prelates.
34544:senator,  n.  —  ME.  senatour,  fr.  OF.  senatour  (F. senateur),  fr.  L.  senatorem,  acc.  of  senator,  fr. senex,  gen.  senis,  ‘old’.  See  senile  and  agential suff.  -or  and  cp.  prec.  word, senatorial,  adj.  —  Formed  with  adj.  suff.  -al  fr. L.  senatorius,  ‘pertaining  to  a  senator’,  fr.  sena¬ tor,  gen.  -oris.  See  prec.  word.
34556:senile,  adj.  —  L.  senilis,  ‘pertaining  to  old  people, senile’,  formed  with  suff.  -ile  fr.  senex,  gen.  senis, ‘old’,  which  is  cogn.  with  OI.  sdnah,  ‘old’.
34559:senior,  adj.  —  L.,  ‘older’,  compar.  of  senex,  gen. senis,  ‘old’.  See  senile  and  cp.  seigneur,  seignior, senhor,  seiior,  sieur,  signor,  sir,  sire,  messire, monseigneur,  monsieur,  monsignor.  Cp.  also surly.
```


## [2026-09-14T02:05:08.117Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Inspect verify_check.py"
}
```


### [2026-09-14T02:05:08.169Z] TOOL RESULT

```
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


## [2026-09-14T02:05:09.634Z] AGENT

Now let me write the verification file.


## [2026-09-14T02:11:53.387Z] TOOL CALL #62: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-443.json",
 "content": "{\n  \"pdf_page\": 443,\n  \"book_page\": 413,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sem 2, Sam\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sem- / *semh₂- 'summer' (gen. *sem-os); Watkins *sem-² / *semə-\",\n      \"note\": \"Pokorny's third homonym sem- 'Sommer' (IEW 905, gen. sem-os) is exactly Nourai's root box; Watkins in AHD lists it as sem-² 'Summer' with the explicit cross-reference '[Pok. 3. sem- 905]'. The variant 'Sam' in the head is the ā-grade seen in Old Irish sam, Welsh haf and in the Indo-Iranian *sama-. The current reconstruction writes the laryngeal: *semh₂- / oblique *sm̥-h₂-ór-o-, but the root, the language label ('Indo-European') and the gloss 'summer' are all correct. Note that this root is entirely distinct from the much better-known *sem- 'one, same' (Pokorny 902, Watkins sem-¹), with which it must not be confused.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sem- / *semh₂- به معنی «تابستان» (حالت غیرفاعلی *sem-os) در فرهنگ پوکورنی زیر مدخل sem-3 در همان صفحهٔ ۹۰۵ آمده است و واتکینز نیز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage آن را با ارجاع صریح به «پوکورنی ۹۰۵» آورده. گونهٔ «Sam» همان ستاک با آی کشیده است که در ایرلندی کهن sam و ولزی haf دیده می‌شود. بازسازی امروزی حنجره‌ای را نیز می‌نویسد (*semh₂-)، ولی برچسب زبانی و معنای «تابستان» درست است. باید توجه داشت که این ریشه با ریشهٔ پرکاربردتر *sem- «یک، همان» (پوکورنی ۹۰۲) یکی نیست. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sumaraz\",\n        \"https://en.wiktionary.org/wiki/summer\",\n        \"https://www.etymonline.com/word/summer\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:905\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt, block 'Page(s): 902-905': 'Root / lemma: sem-3 | Meaning: summer | Grammatical information: (Gen. sem-os) ... Old Indic samā f. \\\"Halbjahr, season, year\\\" (= Armenian am) ... Avestan ham- \\\"summer\\\" ... Old High German sumar, Old English sumor m., Old Icelandic sumar n. \\\"summer\\\". References: WP. II 492 f.' The whole chart is this one Pokorny entry; the printed IEW page for it is 905, as Nourai cites.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sem-²\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 916: 'sem-2, Also semə-. Summer. Suffixed zero-grade form *sm̥ə-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMER¹. [Pok. 3. sem- 905.]'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 14.76 'Summer'\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt line 25788: 'Ir. sam, W. haf, Br. hañv, Ir. samrad, NIr. samhradh ...; ON sumar, OE sumor, etc., general Gmc., except Goth.; Av. ham- (Skt. samā- \\\"season, year\\\" rarely also \\\"summer\\\")'\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny II 492 f. (cited by Pokorny; only the Register Bd. III is on disk)\",\n          \"stance\": \"silent\",\n          \"note\": \"grep 'sem-' in WLD_band3.txt returns only the index line '2. sem- 488*' with no summer entry; Bd. II, where WP. II 492 f. stands, is not among the local files.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. — not found\",\n          \"stance\": \"silent\",\n          \"note\": \"grep 'semos', 'sema ', \\\"'summer'\\\" in IEC.txt returns nothing; Mann has senos 'old' (see entry 2) but no separate summer lemma was located.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"ham 2, hama 2\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan ham- (stem hama-) m. 'summer' is the regular Iranian outcome of PIE *sem-: PIE initial *s- becomes Indo-Iranian *s- and then, by the Iranian s > h shift, Av. h- (compare Av. hapta 'seven' : Skt. sapta). Bartholomae's Altiranisches Wörterbuch lemmatises it 'j. ʰham-, °ham- m. \\\"Sommer\\\"' with citations from Vendidad 5.4, 15.45-51, Nirangistan 46-51 and the Frahang, and the derived adjective hąmina- 'summer-' ('hapta hənti hąminō månha' = 'there are seven summer months', Vd. 1.3 Pahlavi gloss). The contrast pair is aiwi.gāma- 'winter', with which ham- is repeatedly juxtaposed. Nourai's double citation 'ham 2, hama 2' distinguishes this from the homonymous Av. hama- 'same, equal' (< *sem- 'one'), which is correct practice.\",\n          \"derivation_fa\": \"اوستایی ham- (ستاک hama-) به معنی «تابستان» بازماندهٔ منظم *sem- هندواروپایی در ایرانی باستان است؛ «س» آغازین هندواروپایی در ایرانی به «ه» بدل می‌شود (مانند اوستایی hapta در برابر سنسکریت sapta). بارتولومه در فرهنگ ایرانی باستان این واژه را با شاهدهایی از وندیداد و نیرنگستان آورده و صفت مشتق hąmina- «تابستانی» را نیز ثبت کرده است. نورایی به‌درستی آن را با شمارهٔ ۲ از هم‌آوای دیگر hama- «همانند، برابر» (از ریشهٔ *sem- «یک») جدا کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/summer\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:905\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt, sem-3 material: 'Avestan ham- \\\"summer\\\"' stands between Old Indic samā and Armenian am.\"\n            },\n            {\n              \"ref\": \"KLN:1541\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 37437 (s.v. summer): '... cogn. with OI. sama, \\\"season, half-year, year\\\", Avestic hama, \\\"summer\\\", Arm. am, \\\"year\\\", amarn, \\\"summer\\\" ... All these words are traceable to I.-E. base *sem-, *sam-, \\\"summer; season\\\".' Klein's page for 'summer' in the 1966/67 two-volume set is 1541, as cited.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch, s.v. ham-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt line 29390: '• j. ʰham-, °ham- m. \\\"Sommer\\\": ... hama .. aiwi.gāme F. 25 b; V.5.4a, 15.45 ... a) Plur. \\\"Sommerzeit\\\"'; cf. line 25870 'hapta hənti hąminō månha panca tayana' = 'es gibt (sonst) sieben Sommermonate'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 14.76\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. ham-' listed among the IE words for 'summer' (SYN.txt line 25788).\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hamîn «همین»\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"hamîn «همین»\",\n          \"correct_form\": \"hāmīn «هامین»\",\n          \"derivation\": \"The derivation itself is right: Av. hąmina- / ham- 'summer' > Middle Persian hāmīn 'summer' (with the adjective hāmīnīg 'summery'), continued in the learned New Persian word هامین hāmīn 'summer'. But the FORM printed on p. 413 is wrong. Horn, the reference Nourai cites, prints it with a long ā: Grundriss p. 280, no. 106 'hāmīn \\\"Sommer\\\", hāmīnīk \\\"sommerlich\\\", häufig. aw. ham- \\\"Sommer\\\", hąmīn- \\\"sommerlich\\\"; ai. samā- \\\"Halbjahr, Jahreszeit, Wetter, Jahr\\\"; arm. am \\\"Jahr\\\", amaṙn \\\"Sommer\\\"; ahd. an. sumar \\\"Sommer\\\". kurd. havin'. Mo'in makes the point explicitly in his footnote to Borhan-e Qate' (p. 1212 ff. of vol. 4, s.v. همیز/همین): the Borhan headword is 'مصحف «هامین» hāmīn بمعنی تابستان' — a scribal corruption of hāmīn — and he cites Biruni's Āthār al-bāqiya p. 93 for هامین. Nourai has copied the corrupted Borhan spelling, which in Persian is the homograph of the everyday word همین hamin 'this very (same)'. The extraction is faithful to the printed page (the page image shows 'hamîn : summer (obsolete)' with همین). Two further caveats: Horn lists the word in his appendix 'Verlorenes Sprachgut', i.e. among Pahlavi words that did NOT survive into New Persian, and Dehkhoda's only هامین entry is a unit of weight (25 staters, from Farhang-e Nezām); the 'summer' sense is an archaic/Zoroastrian-tradition word, so Nourai's gloss '(obsolete)' is fair.\",\n          \"derivation_fa\": \"ریشه‌شناسی درست است: اوستایی hąmina-/ham- «تابستان» در فارسی میانه hāmīn (و صفت hāmīnīg «تابستانی») شده و در فارسی نو به‌صورت «هامین» بازمانده است. اما صورتی که کتاب چاپ کرده نادرست است: هرن در همان صفحهٔ ۲۸۰ که نورایی به آن ارجاع می‌دهد، شمارهٔ ۱۰۶، واژه را با الف کشیده «hāmīn» آورده است. معین نیز در حاشیهٔ برهان قاطع تصریح می‌کند که ضبط «همین/همیز» برهان «مصحّفِ هامین hāmīn بمعنی تابستان» است و به آثارالباقیهٔ بیرونی ص ۹۳ استناد می‌کند. نورایی همان ضبط مصحّف برهان را نقل کرده که در فارسی هم‌نگاشت واژهٔ رایج «همین» است. خطای چاپی (یا خطای خود مؤلف) کتاب است، نه خطای خوانش اسکن؛ تصویر صفحه همان «hamîn / همین» را نشان می‌دهد. افزون بر این، هرن این واژه را در بخش «سرمایهٔ زبانی از دست‌رفته» یعنی واژه‌های پهلوی‌ای که به فارسی نو نرسیده‌اند آورده، و دهخدا ذیل «هامین» تنها معنی واحد وزن را ثبت کرده است؛ پس قید «منسوخ» نورایی بجاست.\",\n          \"sources\": [\n            \"https://vajehyab.com/dehkhoda/%D9%87%D8%A7%D9%85%DB%8C%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:280\",\n              \"status\": \"partial\",\n              \"note\": \"HRN.txt lines 10593-10600 (page header '- 280 -' immediately precedes): '106. hāmīn \\\"Sommer\\\", hāmīnīk \\\"sommerlich\\\", häufig. aw. ham- \\\"Sommer\\\", hąmīn- \\\"sommerlich\\\"; ai. samā- ...; ahd. an. sumar \\\"Sommer\\\".' Horn has the word and the derivation but prints hāmīn, not hamīn, and files it under 'VERLORENES SPRACHGUT' (Horn's appendix of Pahlavi words lost in New Persian, beginning p. 263), so he labels it Pahlavi rather than New Persian.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 4, printed p. 2374 (BQT_v4_pages.txt, pdf page 457), Mo'in's footnote 4 to همیز/همین\",\n              \"stance\": \"partial\",\n              \"note\": \"'مصحف «هامین» hāmīn بمعنی تابستان، در اوستا hama (سانسکریت samā بمعنی سال) و نیز در اوستا hāminya بمعنی تابستانی و نیز تابستان آمده. پورداود، خرده اوستا ...؛ ابیرونی، آثارالباقیه ص ۹۳ «هامین»'. Mo'in confirms the etymology but flags the spelling Nourai used as a corruption.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Manual of Pahlavi II (glossary), s.v. hāmīn — not found\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'hāmīn', 'hamin' in NYB_vol2_glossary.txt returns no hit; Nyberg's glossary covers only the texts of Part I.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-hā, s.v. هامین — not found\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'هامین' in incoming/ARY/ARY_pages.txt returns nothing.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"samâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit samā́ f. is the Indic member of the same paradigm: PIE *semh₂- with the ā-stem, giving Indo-Iranian *samā, whence Skt. samā́ and (with s > h) Av. hama-. Pokorny glosses it 'Halbjahr, season, year' and Klein 'season, half-year, year'; Nourai's 'half-year' is one of these attested senses. Buck (14.76) notes that samā- means 'season, year' and only rarely 'summer' — the Indic branch generalised the term from the warm half of the year to the whole year, so the Vedic idiom a-sa-mā 'this year'. The same semantic widening produced Armenian am 'year' beside amaṙn 'summer'.\",\n          \"derivation_fa\": \"سنسکریت samā́ (مؤنث) عضو هندی همین خانواده است: *semh₂- هندواروپایی با ستاک ā، در هندوایرانی *samā، که در سنسکریت samā́ و در اوستایی (با تبدیل س به ه) hama- بازتاب یافته است. پوکورنی آن را «نیم‌سال، فصل، سال» و کلاین «فصل، نیم‌سال، سال» معنی کرده‌اند؛ ضبط «نیم‌سال» نورایی یکی از همین معانی است. باک یادآور می‌شود که در هندی معنی «سال» غالب شده و معنی «تابستان» کمیاب است — همان تحول معنایی که در ارمنی am «سال» در کنار amaṙn «تابستان» دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sumaraz\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1541\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 37437 (s.v. summer, p. 1541): 'cogn. with OI. sama, \\\"season, half-year, year\\\"'. Klein's 'half-year' is precisely Nourai's gloss.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 905 s.v. sem-3\",\n              \"stance\": \"supports\",\n              \"note\": \"'Material: Old Indic samā f. \\\"Halbjahr, season, year\\\" (= Armenian am), a-sa-mah \\\"this year\\\"' (POK_full.txt).\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 14.76\",\n              \"stance\": \"partial\",\n              \"note\": \"'Skt. samā- \\\"season, year\\\" rarely also \\\"summer\\\", cf. Macdonell-Keith 2.429 f.' — Buck stresses 'year/season' rather than 'half-year'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"sumaraz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *sumaraz m. 'summer' is derived from the same root by an r-stem suffix. Watkins reconstructs a 'suffixed zero-grade form *sm̥ə-aro-' (in modern notation *sm̥-h₂-ór-o-, an oblique r-stem, the same formation as Old Armenian amaṙn 'summer'), which gives Gmc. *sumaraz with the regular development of the syllabic *m̥ to Gmc. -um-. Descendants: OHG sumar, OS/OFris. sumur, MDu. somer, ON sumar, OE sumor; Gothic, which lost the word, has asans instead.\",\n          \"derivation_fa\": \"ژرمنی آغازین *sumaraz «تابستان» با پسوند ستاکِ r از همین ریشه ساخته شده است. واتکینز آن را از صورت صفرپایهٔ پسونددار *sm̥ə-aro- (در نگارش امروزی *sm̥-h₂-ór-o-) می‌گیرد، همان ساختی که در ارمنی کهن amaṙn «تابستان» نیز دیده می‌شود؛ «م» هجایی هندواروپایی در ژرمنی به‌طور منظم به um بدل شده است. بازماندگان: آلمانی علیای باستان sumar، نورس باستان sumar، انگلیسی باستان sumor. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/sumaraz\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:905\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt sem-3: 'Old High German sumar, Old English sumor m., Old Icelandic sumar n. \\\"summer\\\"'.\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 916: 'Suffixed zero-grade form *sm̥ə-aro- in Germanic *sumaraz in Old English sumor'. The starred Germanic form is literally Watkins'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 1541 s.v. summer\",\n              \"stance\": \"supports\",\n              \"note\": \"'OE. sumor, rel. to OS., ON., Norw., OHG. sumar, Dan. sommer, Swed. sommar, OFris. sumur, MDu. somer, Du. zomer, MHG. sumer, G. Sommer'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 14.76\",\n              \"stance\": \"supports\",\n              \"note\": \"'ON sumar, OE sumor, etc., general Gmc., except Goth.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"summer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English sumor m. > Middle English sumer, somer > Modern English summer; the -or of the OE i-stem oblique was levelled to -er, and the geminate spelling -mm- is a Middle English orthographic marker of the preceding short vowel. The word is the direct inherited continuation of Gmc. *sumaraz — not a borrowing — and the one ancient English survivor of this root; the only other trace is the second element of gossamer ('goose-summer').\",\n          \"derivation_fa\": \"انگلیسی باستان sumor به انگلیسی میانه sumer/somer و سپس انگلیسی نو summer رسیده است؛ دو «م» در املا نشانهٔ کوتاهی واکهٔ پیشین در انگلیسی میانه است. این واژه بازماندهٔ مستقیم و ارثی *sumaraz ژرمنی است و وام‌واژه نیست؛ تنها نشان دیگر این ریشه در انگلیسی، جزء دوم gossamer است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/summer\",\n            \"https://en.wiktionary.org/wiki/summer\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'in Old English sumor, summer: SUMMER¹'; and the index line 2325 'SUMMER! sem-2'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"p. 1541 s.v. summer\",\n              \"stance\": \"supports\",\n              \"note\": \"'summer, n., a season. — ME. sumer, somer, fr. OE. sumor ... Cp. the second element in gossamer.'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etym. Dict. — checked, no separate entry quoted\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'Summer, ' in SKT.txt returned no headword line (the OCR of that page is defective); Klein and Watkins cover the chain.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Sěma, A-sěma\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Ancient Greek σῆμα (sêma) 'sign, mark, token'; ἄσημος (ásēmos) 'without mark, uncoined', neuter ἄσημον (ásēmon) '(unstamped) bullion, silverware'\",\n      \"note\": \"The root box is not an Indo-European root but a pair of Greek words, and the account is right in substance though loose in the glosses. σῆμα is a NOUN 'sign, mark, token' (Nourai's 'marked, stamped (coin)' is a paraphrase — he is following Mo'in, who glosses σῆμα in his Borhan footnote as «نشانه‌نهاده، علامت‌داشته»). ἄσημος is the adjective ἀ- (privative) + σῆμα + -ος, 'without mark or sign, uncoined (of a precious metal)', and the technical term that travelled east is the neuter ἄσημον (ἀργύριον) 'unstamped silver, bullion', already Attic (Liddell-Scott s.v.). The etymology of σῆμα itself is disputed in modern scholarship (often compared with Skt. dhyā́man, i.e. PIE *dʰyeh₂-mn̥, which Beekes regards as uncertain), but that lies outside the chart. The chart's single blank Old-Persian daughter box (to the right of 'siyaman' on the printed page) carries no text and is not in the extraction; nothing is lost.\",\n      \"note_fa\": \"جعبهٔ ریشه در اینجا یک ریشهٔ هندواروپایی نیست، بلکه دو واژهٔ یونانی است و مضمون آن درست، ولی معنی‌هایش تقریبی است. σῆμα اسم است به معنی «نشانه، علامت» (ترجمهٔ نورایی «سکه‌خورده، ضرب‌شده» برگرفته از حاشیهٔ معین بر برهان قاطع است که آن را «نشانه‌نهاده، علامت‌داشته» معنی کرده). ἄσημος صفت است از ἀ- نفی + σῆμα، یعنی «بی‌نشان، ضرب‌ناشده»، و اصطلاحی که به شرق راه یافت صورت خنثای ἄσημον (ἀργύριον) «نقرهٔ سکه‌ناخورده» بود که در یونانی آتیک کاربرد داشت. ریشهٔ خودِ σῆμα نزد پژوهشگران امروزی مورد اختلاف است. روی‌هم‌رفته ادعای نورایی با احتیاط پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%E1%BC%84%CF%83%CE%B7%CE%BC%CE%BF%CF%82\",\n        \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KNT:209\",\n          \"status\": \"supports\",\n          \"note\": \"Kent, Old Persian, Lexicon p. 209 s.v. siyamam (archive.org 'oldpers' djvu text, the block immediately before the running number 210): 'siyamam adj., asm. for nsm., \\\"made of silver\\\", A¹I; characters clear, but word dubious ... Apparently for NPers. sīm \\\"silver\\\", from Phl. asēm, borrowed from Gk. ἄσημον \\\"(unstamped) silver\\\", NGk. ἀσήμι \\\"silver\\\"; but this seems anachronistic.' Kent names the Greek word and the whole chain.\"\n        },\n        {\n          \"ref\": \"MON:1982\",\n          \"status\": \"not_checked\",\n          \"note\": \"The six-volume Amir Kabir Farhang-e Farsi is not online (refs_online.json note); vajehyab/abadis give Mo'in's entry text without page numbers. Mo'in's online entry tags سیم only as [په.] (Pahlavi) and does not repeat the Greek step, so the page could not be verified.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"BQT\",\n          \"where\": \"vol. 2, printed p. 1212 (BQT_v2_pages.txt leaf 673), Mo'in's footnote 6 to سیم\",\n          \"stance\": \"supports\",\n          \"note\": \"'برخی از محققان معاصر اصل «سیم» را یونانی دانند (مجلهٔ دادگستری ... تقی‌زاده) و آن را مرکب از: ἀ علامت نفی و σῆμα (:نشانه نهاده، علامت داشته) (رک: فرهنگ یونانی-انگلیسی لیدل و اسکات) جمعاً بمعنی (زر) نامسکوکه (از افادات شفاهی استاد بنونیست)'. This is Nourai's root box almost word for word, on the very page he cites.\"\n        },\n        {\n          \"src\": \"NYB\",\n          \"where\": \"Manual of Pahlavi II, glossary s.v. asēm\",\n          \"stance\": \"supports\",\n          \"note\": \"NYB_vol2_glossary.txt line 682: 'asēm [sym] silver 118⁸. — Borrowed from Gr ἄσημον; MPrs ʾsym (A-H II); NP sim.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"asěm, sîm; sîměn\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ἄσημον '(unstamped) silver' was taken into Middle Persian in the Parthian/Sasanian period as asēm, written ʾsym; the Greek accusative/neuter -on was dropped and the long ē of Greek η was rendered by MP ē. MacKenzie's Concise Pahlavi Dictionary gives 'asēm [ʾsym | = M, N sīm] silver' and separately 'sēm [sym | N ~] = asēm', i.e. the aphaeretic variant already existed in Book Pahlavi; the English-Pahlavi index has 'silver (a)sēm; (a.) asēmēn'. Nyberg's glossary (Bundahišn 118⁸) says outright 'Borrowed from Gr. ἄσημον; MPrs ʾsym; NP sīm'. Parthian has hasēm and Bactrian σιμινο 'made of silver'. ONE CAVEAT on the second word: the Pahlavi adjective is asēmēn (so MacKenzie and Nyberg, who lists asēmēn); the form sīmēn with ī is the New Persian adjective سیمین, not the Pahlavi one, so Nourai has put a New Persian word in the Pahlavi box.\",\n          \"derivation_fa\": \"یونانی ἄσημον «نقرهٔ سکه‌ناخورده» در دورهٔ اشکانی/ساسانی به فارسی میانه راه یافت و به‌صورت asēm (نوشتاری ʾsym) درآمد؛ پایانهٔ خنثای یونانی -on افتاد و «ای» بلند یونانی (η) با ē فارسی میانه نمایانده شد. مکنزی در فرهنگ کوچک پهلوی هر دو صورت asēm و sēm را ثبت کرده است، یعنی حذف «اَ»ی آغازین از همان پهلوی کتابی آغاز شده بود؛ نیبرگ نیز تصریح می‌کند که وام‌واژه‌ای است از یونانی. در پارتی hasēm و در بلخی σιμινο «سیمین» دیده می‌شود. یک نکته: صفتِ پهلوی asēmēn است (مکنزی و نیبرگ)، و «سیمین» صورت فارسی نو است؛ بنابراین نورایی واژه‌ای فارسی نو را در جعبهٔ پهلوی نشانده است. در مجموع ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:209\",\n              \"status\": \"supports\",\n              \"note\": \"Kent p. 209 s.v. siyamam: 'Apparently for NPers. sīm \\\"silver\\\", from Phl. asēm, borrowed from Gk. ἄσημον \\\"(unstamped) silver\\\"'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971, s.vv. asēm, sēm, and English-Pahlavi index 'silver'\",\n              \"stance\": \"supports\",\n              \"note\": \"PHD_mackenzie.txt line 1216 'asem [ʾsym | = M, N sim] silver'; line 4540 'sem [sym | N -] = asem'; line 7582 'silver (a)sem; (a.) asemen.' The adjective is asēmēn, not sīmēn.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Manual of Pahlavi II, glossary\",\n              \"stance\": \"supports\",\n              \"note\": \"NYB_vol2_glossary.txt line 682 'asēm [sym] silver 118⁸. — Borrowed from Gr ἄσημον; MPrs ʾsym (A-H II); NP sim.'; line 668 also lists 'asēmēn'; the index lines 5811 and 7393 map 'ʾsym: asem' and 'sim: asem'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sîm 2 «سیم ۲»; sîm 3 «سیم ۳»; sîm 4 «سیم ۴ ( سیماب )»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سیم sīm continues Middle Persian (a)sēm by loss of the unstressed initial a- (aphaeresis) and the regular MP ē > NP ī: asēm > sēm > sīm. Hübschmann lists it among exactly this class of New Persian words in Persische Studien (p. 119 f.): 'sīm \\\"Silber\\\" = phl. asīm, gr. ἄσημος (Nöldeke, Pers. Stud. II, 45)'. The three senses of the chart are all documented on the Borhan page Nourai cites: sīm 2 'silver' is the original sense (Borhan: «نقره را گویند»; Mo'in's Farhang tags سیم '[په.] ۱- نقره ۲- پول'); sīm 3 'wire' is Mo'in's footnote 7 on the same page — «و نیز رشته‌های باریک فلزی را «سیم» گویند، مفتول، و این معنی در زمان مؤلف معمول بوده» — a metonymy from silver thread to any drawn metal filament, now the dominant modern sense (سیم برق, سیم‌کشی, بی‌سیم, سیم‌پیچ, exactly the compounds in the chart's extra line); sīm 4 'mercury' is Mo'in's footnote 8 to سیماب — «از: سیم + آب؛ و سیم خود بمعنی جیوه آمده» — i.e. quicksilver as 'silver-water', named for its white shine. The Ṭāher Vahīd couplet in the box is the one printed on Borhan p. 1212.\",\n          \"derivation_fa\": \"«سیم» فارسی نو دنبالهٔ (a)sēm فارسی میانه است با حذف «اَ»ی آغازینِ بی‌تکیه و تبدیل منظم ēِ فارسی میانه به ī در فارسی نو: asēm > sēm > sīm. هوبشمان در «پژوهش‌های فارسی» (ص ۱۱۹ به بعد) آن را در همین دستهٔ واژه‌های افتاده‌آغاز آورده است. هر سه معنی جدول در همان صفحهٔ برهان که نورایی ارجاع داده مستند است: «سیم ۲» نقره (معین: «[په.] ۱- نقره ۲- پول»)؛ «سیم ۳» مفتول و رشتهٔ باریک فلزی، که در حاشیهٔ ۷ معین آمده و امروز معنی غالب است (سیم برق، سیم‌کشی، بی‌سیم، سیم‌پیچ — همان ترکیب‌هایی که در جدول آمده)، و از راه مجاز از «رشتهٔ نقره» به هر رشتهٔ فلزی گسترش یافته است؛ «سیم ۴» جیوه، که حاشیهٔ ۸ معین ذیل «سیماب» آن را توضیح می‌دهد: «از: سیم + آب؛ و سیم خود بمعنی جیوه آمده». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\",\n            \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1212\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt leaf 673 (printed 1212) carries the headword سیم, the Ṭāher Vahīd couplet Nourai quotes — «سیم و زر دنیا پرستان را منافق میکند / پشت و رو باشد مگر آیینهٔ بی‌سیم را. طاهر وحید» — and Mo'in's footnotes 6 (Greek origin), 7 (سیم = مفتول) and 8 (سیماب = سیم + آب).\"\n            },\n            {\n              \"ref\": \"KNT:209\",\n              \"status\": \"supports\",\n              \"note\": \"Kent p. 209: 'Apparently for NPers. sīm \\\"silver\\\", from Phl. asēm'.\"\n            },\n            {\n              \"ref\": \"MON:1982\",\n              \"status\": \"not_checked\",\n              \"note\": \"6-volume Mo'in not available; the online Mo'in text (abadis) reads '[په.] (اِ.) ۱- نقره. ۲- پول، وجه ... ۴- مفتول، رشتهٔ باریک فلزی', which matches senses 2 and 3 but is not page-verifiable.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Persische Studien, printed p. 119 f. (HUB.txt line 4215, after the '- 119 -' page mark)\",\n              \"stance\": \"supports\",\n              \"note\": \"'sīm \\\"Silber\\\" = phl. asīm, gr. ἄσημος (Nöldeke, Pers. Stud. II, 45)' — in Hübschmann's list of NP words that lost an initial vowel, beside sāgird = paz. asāgard and vērān = paz. avīrān.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in online (abadis.ir/fatofa/سیم)\",\n              \"stance\": \"partial\",\n              \"note\": \"'[ په . ] (اِ. ) ۱ - نقره . ۲ - پول ، وجه ... ۴ - مفتول ، رشتة باریک فلزی' — Mo'in tags the word Pahlavi and gives senses 2 and 3, but the online text omits the Greek step.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-hā — no etymological entry found\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'سیم' in incoming/ARY/ARY_pages.txt hits only unrelated strings (تقسیم, ترسیم) and 'سیم موم' at line 6867; no headword سیم.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old Persian\",\n          \"words\": \"siyaman\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"siyaman\",\n          \"correct_form\": \"siyamam\",\n          \"derivation\": \"The form is misprinted. Kent's lexicon (p. 209, the page Nourai cites) reads 'siyamam adj., asm. for nsm., \\\"made of silver\\\"' — with final -m, the accusative-singular ending of the a-stem, used for the nominative in the text A¹I ('hya imam bātugara siyamam vidiya karta' = 'in whose royal house this silver saucer was made'). Nourai's 'siyaman' with -n is not a possible Old Persian form here, and the page image confirms the book itself prints 'siyaman', so the extraction is faithful and the error is the author's. Substance: Kent supports the derivation Nourai draws (Greek ἄσημον > the Iranian word) but attaches two heavy warnings on the same page — 'characters clear, but word dubious', 'but this seems anachronistic', and 'against authenticity of the inscription, cf. Schaeder, SbPAW 1935.489-96'. The A¹I silver dishes of Artaxerxes I are widely suspected of being modern forgeries, precisely because a Greek loanword for silver is out of place in an Achaemenid royal inscription; Herzfeld read the word as saiymam instead. Wiktionary, by contrast, accepts OP siyamam and even makes it the intermediary (Greek > OP siyamam > MP asēm). So the node's derivation is defensible but the word is not securely attested Old Persian.\",\n          \"derivation_fa\": \"صورت واژه در کتاب نادرست چاپ شده است. کنت در همان صفحهٔ ۲۰۹ که نورایی ارجاع می‌دهد «siyamam» را ثبت کرده — با «م» پایانی، یعنی پایانهٔ حالت مفعولیِ مفرد که در کتیبهٔ A¹I به‌جای فاعلی به کار رفته است («hya imam bātugara siyamam vidiya karta»: «که در کاخ او این جام سیمین ساخته شد»). «siyaman» با «ن» پایانی در فارسی باستان ممکن نیست، و تصویر صفحهٔ چاپی نشان می‌دهد خودِ کتاب همین را چاپ کرده است؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن. اما در محتوا: کنت همان‌جا دو هشدار جدی می‌دهد — «حروف روشن‌اند اما خود واژه مشکوک است» و «این امر زمان‌پریشانه می‌نماید» — و به مقالهٔ شدر (۱۹۳۵) در ردّ اصالت کتیبه ارجاع می‌دهد؛ بشقاب‌های سیمین منسوب به اردشیر یکم را بسیاری جعلی می‌دانند، چون وجود یک وام‌واژهٔ یونانی برای نقره در کتیبه‌ای هخامنشی بعید است. در مقابل، ویکی‌واژه siyamam را می‌پذیرد و آن را حلقهٔ واسط یونانی به فارسی میانه می‌شمارد. پس ریشه‌شناسی پذیرفتنی است ولی خود واژه سند استواری در فارسی باستان ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:209\",\n              \"status\": \"partial\",\n              \"note\": \"Kent, Old Persian, Lexicon p. 209: 'siyamam adj., asm. for nsm., \\\"made of silver\\\", A¹I; characters clear, but word dubious (§55.II, §56.V, §116, §149.I). Apparently for NPers. sīm \\\"silver\\\", from Phl. asēm, borrowed from Gk. ἄσημον \\\"(unstamped) silver\\\", NGk. ἀσήμι \\\"silver\\\"; but this seems anachronistic. Hz. ApI 296-9 ... normalizes saiymam: against authenticity of the inscription, cf. Schaeder, SbPAW 1935.489-96.' Supports the etymology, contradicts both the spelling and the confidence.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent §117 and the translation of A¹I\",\n              \"stance\": \"partial\",\n              \"note\": \"Kent §117 (KNT.txt line 1438) lists 'the 3 dubious siyamam' among the words with initial s; the translation of A¹I (line 4677) reads 'in whose royal house this silver saucer was made'. Kent's own page-209 warning about the dubious status is not reflected in Nourai's chart.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch — no entry\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'siyam' in BRT.txt returns nothing; Bartholomae (1904) predates the A¹I dishes (published by Herzfeld from 1935), so the word is necessarily absent.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie s.v. asēm\",\n              \"stance\": \"partial\",\n              \"note\": \"PHD_mackenzie.txt 'asem [ʾsym | = M, N sim] silver' gives the Middle Persian word with no Old Persian antecedent.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Sen 1, Seno\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sen- / *sen(o)- 'old'\",\n      \"note\": \"Pokorny 907 has exactly 'Root / lemma: sen(o)- (*heno) | Meaning: old, *old moon', with Old Indic sana-, Avestan hana- 'old', Latin senex/senior/senatus, Old Irish sen, Gothic sineigs, Lithuanian senas. Watkins gives 'sen-¹. Old ... [Pok. sen(o)- 907]'. Nourai's numbering 'Sen 1' correctly separates it from Pokorny's seni-/senu- 'apart, separated' (IEW 906-7, Watkins sen-²), the source of Latin sine and English sunder — a distinction the chart keeps. Root, language label and gloss are all right.\",\n      \"note_fa\": \"پوکورنی در صفحهٔ ۹۰۷ دقیقاً مدخل sen(o)- «کهن، پیر» را با شواهد سنسکریت sana-، اوستایی hana-، لاتین senex/senior/senatus، ایرلندی کهن sen، گوتیک sineigs و لیتوانیایی senas آورده است، و واتکینز نیز sen-1 «old» را با ارجاع به همان صفحه ثبت کرده. شمارهٔ «Sen 1» نورایی به‌درستی این ریشه را از seni-/senu- «جدا، سوا» (پوکورنی ۹۰۶–۹۰۷، خاستگاه sine لاتین و sunder انگلیسی) جدا می‌کند. ریشه، برچسب زبانی و معنی، هر سه درست است.\",\n      \"sources\": [\n        \"https://www.etymonline.com/word/senate\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sen-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:907\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt block 'Page(s): 907': 'Root / lemma: sen(o)- (*heno) | Meaning: old, *old moon | Material: Old Indic sana-, Avestan hana- \\\"old\\\" ... Latin senex, Gen. senis, Kompar. senior \\\"old, aged\\\" ... senatus, -us (Oscan Gen. senateis) \\\"Senat\\\" ... Lithuanian senas \\\"old\\\". References: WP. II 494 f.'\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sen-¹\",\n          \"stance\": \"supports\",\n          \"note\": \"AHD_watkins1985.txt line 916: 'sen-¹. Old. 1. Latin senex, old, an elder: SEIGNIOR, SENATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENOPIA, (SIGNORY), (SIR), SIRE, (SURLY). ... [Pok. sen(o)- 907.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. senos\",\n          \"stance\": \"supports\",\n          \"note\": \"IEC.txt line 15213: 'senos \\\"old\\\": senis, -ios \\\"elderly; old man\\\". WP II, 494. Skt. sánaḥ, id.; Av. hanō, m. \\\"old man\\\"; Arm. hin ...; Gk. hénos \\\"last year's, old\\\"; Lat. cf. senex ...; Olr. sen ...; Li. sénas.' Line 15196 adds 'senát- \\\"age\\\" ... Lat. senātus'.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 14.15 'Old'\",\n          \"stance\": \"supports\",\n          \"note\": \"SYN.txt line 24433 ff.: '1. IE *sen-. Walde-P. 2.494 ... Lat. senex ...; Lith. senas, Skt. (Ved.) sana- (opp. to nava- and yuvan-), sanaya-, Av. hana- (quotable only for old persons); Arm. hin.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"hana, hanâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan hana- 'old, aged' is the direct Iranian reflex of PIE *sen-o-, with the regular Iranian shift of initial *s- to h- (as in ham- 'summer' above). Bartholomae's entry reads 'j. hana- Adj. (fem. hanā-) \\\"greis, alt\\\"', with Vendidad 3.19 (hanō vā zaurvō vā 'be he aged or decrepit') and, in the feminine, the pejorative use 'Alte, Vettel' at Vd. 15.13-14. So Nourai's second form hanâ is not an independent lemma but the FEMININE of the same adjective; that is a minor imprecision, not an error. The Old Persian cognate is hanatā- 'old age' (Bh. 1.11 etc.).\",\n          \"derivation_fa\": \"اوستایی hana- «پیر، سالخورده» بازتاب مستقیم *sen-o- هندواروپایی در ایرانی است، با همان تبدیل منظم «س» آغازین به «ه». بارتولومه آن را چنین ثبت کرده است: «hana- صفت (مؤنث hanā-) پیر، کهنسال»، با شاهد وندیداد ۳٫۱۹ و کاربرد تحقیرآمیز مؤنث آن («پیرزن») در وندیداد ۱۵. پس صورت دوم نورایی، hanâ، مدخلی جداگانه نیست بلکه مؤنث همان صفت است؛ این بی‌دقتی کوچکی است، نه خطا. هم‌ریشهٔ فارسی باستان آن hanatā- «پیری» است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/senate\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:907\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt sen(o)-: 'Old Indic sana-, Avestan hana- \\\"old\\\"' is the opening line of the Material section.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch, s.v. hana-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt line 29325: '• j. hana- Adj. (fem. °nā-) \\\"greis, alt\\\": yat hanō vā zaururō vā pairistā.xšudrō vā bavāt V.3.19. a) fem. °nā- als Subst. \\\"Alte (in verächtlichem Sinn), Vettel\\\": V.15.13, 14.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 14.15\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. hana- (quotable only for old persons)' (SYN.txt line 24433 ff.).\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. senos\",\n              \"stance\": \"supports\",\n              \"note\": \"'Av. hanō, m. \\\"old man\\\"' (IEC.txt line 15213).\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hân «هان»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The etymology of the word is fine, but the language label is wrong and the Persian script is misleading. Horn's page 280, which Nourai cites, is in his appendix 'VERLORENES SPRACHGUT' (Grundriss, from p. 263) — a list of PAHLAVI words that did NOT survive into New Persian — and entry no. 108 reads 'hān 1) \\\"alt\\\" (vd. 15 (42) mit Awesta-, sonst mit Pehlevībuchstaben). aw. hanā- \\\"alt\\\"; ai. sána-; arm. hin.' Horn even notes that the word is written in Avestan characters at that Vendidad passage, i.e. it is barely more than a transcription of the Avestan adjective; and in the introduction to that very section he complains that 'der BQ und durch diesen der PS enthalten eine Menge niemals im Neupersischen vorhanden gewesener Pehlevī- und Pāzendworte'. There is no New Persian هان 'old': Borhan-e Qate' (vol. 4, printed p. 2312) has only «هان — بروزن کان، کلمهٔ تنبیه است، بمعنی در محل آگاهانیدن و تأکید در کاری و امری بکار برند» — the attention particle hān 'lo! beware!', a different word, with no 'old' sense at all; Dehkhoda and Mo'in agree. Modern scholarship therefore places hān 'old' in Middle Persian, not in Persian, and the chart's arrow Avestan > Persian should read Avestan > Pahlavi.\",\n          \"derivation_fa\": \"ریشه‌شناسی خودِ واژه ایرادی ندارد، ولی برچسب زبانی نادرست است. صفحهٔ ۲۸۰ هرن که نورایی به آن ارجاع داده در پیوستِ «سرمایهٔ زبانیِ از دست‌رفته» (از ص ۲۶۳) است، یعنی فهرست واژه‌های پهلوی‌ای که به فارسی نو نرسیده‌اند؛ مدخل ۱۰۸ چنین است: «hān ۱) پیر (وندیداد ۱۵٫۴۲، با حروف اوستایی)؛ اوستایی hanā-؛ سنسکریت sána-؛ ارمنی hin». هرن خود در آغاز همین بخش گله می‌کند که برهان قاطع و از راه آن فرهنگ‌های پس از آن، انبوهی واژهٔ پهلوی و پازند را که هرگز در فارسی نو نبوده‌اند ثبت کرده‌اند. در فارسی نو «هان» به معنی «پیر» وجود ندارد: برهان قاطع (ج ۴، ص ۲۳۱۲) تنها «هان: کلمهٔ تنبیه است، در محل آگاهانیدن و تأکید» را آورده است، و دهخدا و معین نیز همین. پس پژوهش امروزی این واژه را فارسی میانه می‌داند و پیکان نمودار باید «اوستایی ← پهلوی» باشد، نه «اوستایی ← فارسی».\",\n          \"sources\": [\"https://www.etymonline.com/word/senate\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:280\",\n              \"status\": \"partial\",\n              \"note\": \"HRN.txt lines 10607-10612: '108. hān 1) \\\"alt\\\" (vd. 15 (42) mit Awesta-, sonst mit Pehlevībuchstaben). aw. hanā \\\"alt\\\"; ai. sána-; arm. hin (H. No. 168). 2) \\\"anderer\\\" (pāz. han).' The page supports the etymology but labels the word Pahlavi and files it under words lost in New Persian (section header 'VERLORENES SPRACHGUT', HRN.txt line ~10047).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 4, printed p. 2312 (BQT_v4_pages.txt, pdf page 395), s.v. هان\",\n              \"stance\": \"contradicts\",\n              \"note\": \"«هان — بروزن کان، کلمهٔ تنبیه است بمعنی در محل آگاهانیدن و تأکید در کاری و امری بکار برند، خواه بطریق امر باشد و خواه بعنوان نهی ...» — no 'old' sense; the neighbouring entry «هانی: بزبان پهلوی امر به نشستن باشد یعنی بنشین» is likewise unrelated.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie 1971 — no entry hān 'old'\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'hān' in PHD.txt/PHD_mackenzie.txt gives only hān 'that' and unrelated forms; MacKenzie's word for 'old' is pīr (English-Pahlavi index line 5908 'aged pīr').\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in / Dehkhoda online\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Persian هان is uniformly an interjection of warning ('آگاه باش'); no dictionary of New Persian gives it the sense 'old'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Latin\",\n          \"words\": \"senex; senior\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin senex, gen. senis 'old, old man' continues the PIE root *sen- with a -k- extension (*sen-eks); senior is its regular comparative 'older', formed with the Latin comparative suffix -ior. From the same stem Latin built senēre 'to be old', senēscere 'to grow old', senium 'senility', senīlis 'senile', senectūs 'old age', and — the form that matters for the rest of the chart — senātus, -ūs 'council of the elders' (Oscan gen. senateis), with senātor. Pokorny prints exactly this list on p. 907, and Watkins gives senex as the sole Latin representative of sen-¹.\",\n          \"derivation_fa\": \"لاتین senex (حالت اضافه senis) «پیر، پیرمرد» دنبالهٔ ریشهٔ *sen- هندواروپایی با گسترشِ -k- است (*sen-eks)، و senior صفت تفضیلی منظم آن «پیرتر» با پسوند -ior لاتینی. از همین ستاک واژه‌های senēre «پیر بودن»، senēscere «پیر شدن»، senium، senīlis، senectūs و — که برای ادامهٔ نمودار مهم است — senātus «شورای پیران» (با صورت اوسکیِ senateis) و senātor ساخته شده‌اند. پوکورنی همین فهرست را در صفحهٔ ۹۰۷ آورده و واتکینز نیز senex را تنها نمایندهٔ لاتینی این ریشه می‌شمارد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/senate\", \"https://www.etymonline.com/word/senior\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:907\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt sen(o)-: 'Latin senex, Gen. senis, Kompar. senior \\\"old, aged\\\"; seneo, -ere \\\"old, weak sein\\\", senesco, -ere ..., senium ..., senatus, -us (Oscan Gen. senateis) \\\"Senat\\\", senectus \\\"age\\\", senecio ds.'\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt: 'sen-¹. Old. 1. Latin senex, old, an elder'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.vv. senile, senior\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt line 34556 'senile, adj. — L. senilis, \\\"pertaining to old people, senile\\\", formed with suff. -ile fr. senex, gen. senis, \\\"old\\\", which is cogn. with OI. sánaḥ, \\\"old\\\"'; line 34559 'senior, adj. — L., \\\"older\\\", compar. of senex'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.vv. senos, senát-, seneió\",\n              \"stance\": \"supports\",\n              \"note\": \"IEC.txt lines 15196-15213: 'senát- \\\"age\\\" ... Lat. senātus, gs: -ūs, m. \\\"senate\\\"'; 'seneió (sen(e)sko) \\\"grow old\\\" ... Lat. seneo, -ere beside senesco'; 'senos \\\"old\\\" ... Lat. cf. senex, gs: senis, m. \\\"old man\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"French\",\n          \"words\": \"monsieur; seinat; senateur\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"seinat\",\n          \"correct_form\": \"sénat\",\n          \"derivation\": \"Two of the three French words are misspelt on the printed page, and the page image shows the misspelling is the book's own, not the extraction's. (1) monsieur is right: it is literally 'my lord', mon 'my' (< L. meum) + sieur, a reduced form of seigneur (< L. seniōrem, acc. of senior) — so Klein s.v. monsieur; the same senior gives Old French sire > sir. (2) 'seinat' is a misprint for sénat 'senate', Old French senat borrowed from Latin senātus in the 13th century; there has never been a French form with -ei-. Nourai's gloss 'an assembly of old wise men' is the literal Latin sense 'council of elders', not a French dictionary definition. (3) 'senateur' lacks its accent: the French word is sénateur, Old French senatour, from Latin senātōrem. All three are learned borrowings of the Latin words rather than inherited developments — except monsieur, whose second element sieur/seigneur IS the inherited outcome of senior (with -ni- > -gn- palatalisation in seigneur).\",\n          \"derivation_fa\": \"از سه واژهٔ فرانسوی این جعبه، دو تا در صفحهٔ چاپی غلط ضبط شده‌اند و تصویر صفحه نشان می‌دهد غلط از خودِ کتاب است نه از خوانش اسکن. یکم، monsieur درست است: به‌معنای تحت‌اللفظی «سرور من»، از mon «من» (لاتین meum) و sieur، صورت کوتاه‌شدهٔ seigneur (از seniōrem لاتین)؛ همین senior در فرانسهٔ کهن sire و سپس sir انگلیسی را داده است. دوم، «seinat» غلط چاپی «sénat» است؛ فرانسهٔ کهن senat وام‌گرفته از senātus لاتین در سدهٔ سیزدهم، و هرگز صورتی با -ei- نداشته است؛ معنی‌ای که نورایی داده («انجمن پیران فرزانه») ترجمهٔ تحت‌اللفظی لاتینی است نه تعریف فرهنگ فرانسوی. سوم، «senateur» بدون علامت است و صورت درست sénateur (فرانسهٔ کهن senatour، از senātōrem لاتین) است. این‌ها همه وام‌واژه‌های عالمانه از لاتین‌اند، جز جزء دوم monsieur که بازماندهٔ ارثی senior است (با کامی‌شدن -ni- به -gn- در seigneur). خطای چاپی کتاب است.\",\n          \"sources\": [\"https://www.etymonline.com/word/sir\", \"https://www.etymonline.com/word/senate\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"AHD_watkins1985.txt s.v. sen-¹ lists the English descendants (SEIGNIOR, SENATE, SENIOR, SIR, SIRE) with their Latin source but gives no French forms, so it cannot confirm the spellings; Watkins does confirm that the French intermediaries go back to Latin senex/senior.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.vv. monsieur, monseigneur, sire, senate, senator\",\n              \"stance\": \"partial\",\n              \"note\": \"KLN_1966.txt line 24341: 'monsieur, n., the French equivalent of English Mr. — F., lit. \\\"my lord\\\", compounded of mon, \\\"my\\\", and sieur, \\\"lord\\\", a shortened form of seigneur' (and 'F. seigneur comes fr. L. seniorem, acc. of senior'); line 34543 'senate ... fr. OF. senat (F. sénat)'; line 34544 'senator ... fr. OF. senatour (F. senateur)'. Klein prints sénat/senateur — never 'seinat'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Senate\",\n              \"stance\": \"supports\",\n              \"note\": \"SKT.txt line 16854: 'Senate, a council of elders. (F. – L.) F. senat. — L. senatum, acc. of senatus, council of elders. — L. senex, old ... Cf. Gk. ἕνος, old, Goth. sineigs, W. hen, O. Skt. sana, old.' Skeat's gloss 'council of elders' is the source of Nourai's paraphrase.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"mosyo «مُسیو»; senâ «سنا»; senâtor «سناتور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three are modern French loans, taken into Persian in the Qajar and Pahlavi periods through the francophone administrative and diplomatic vocabulary. مسیو mosyo < French monsieur, used in Persian as a form of address to Europeans (Mo'in: '[فر.] (اِ.) آقا (در خطاب به فرنگیان گفته می‌شود)'; Dehkhoda notes its colloquial extension to Armenians and Assyrians). سنا senā < French sénat, the name of the upper chamber created by the 1906 constitution and actually convened 1949-1979 (Mo'in: '(س) [فر.] (اِ.) مجلسی که اعضای آن از بزرگان و اعیان کشور برگزیده شوند'; Dehkhoda: 'سنا. [س ِ] (فرانسوی، اِ) مجلس سالخوردگان'). سناتور senātor < French sénateur (Mo'in: '(س) [فر.] (اِ.) عضو مجلس سنا، نمایندهٔ مجلس اعیان'; Dehkhoda: 'سناتور. [س ِ ت ُ] (فرانسوی، اِ)'). The French -eur was regularly rendered in Persian by -or, as in دکتر/امپراتور-type loans. Note that senā 'senate' is a homograph of the much older Arabic loans سنا 'senna (the plant)' and سنا 'radiance', which Persian dictionaries list separately; Nourai's box is unambiguous because he glosses it 'senate'.\",\n          \"derivation_fa\": \"هر سه وام‌واژهٔ فرانسوی‌اند که در دورهٔ قاجار و پهلوی از راه واژگان اداری و دیپلماتیک فرانسوی‌زبان وارد فارسی شده‌اند. «مسیو» از monsieur فرانسوی که در فارسی خطاب به فرنگیان به کار می‌رفت (معین: «[فر.] آقا؛ در خطاب به فرنگیان»). «سنا» از sénat فرانسوی، نام مجلس اعیانی که در قانون اساسی مشروطه پیش‌بینی و از ۱۳۲۸ تا ۱۳۵۷ برپا بود (دهخدا: «سنا. (فرانسوی، اِ) مجلس سالخوردگان»). «سناتور» از sénateur فرانسوی (معین: «[فر.] عضو مجلس سنا، نمایندهٔ مجلس اعیان»). پایانهٔ -eur فرانسوی در فارسی به‌طور منظم -ور/-ور شده است. یادآوری: «سنا»ی مجلس هم‌نگاشتِ دو وام‌واژهٔ کهن‌ترِ عربی «سنا» (گیاه سنا) و «سنا» (روشنایی) است که فرهنگ‌ها جداگانه آورده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%85%D8%B3%DB%8C%D9%88/\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7/\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%86%D8%A7%D8%AA%D9%88%D8%B1/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1925,4125\",\n              \"status\": \"partial\",\n              \"note\": \"The 6-volume Farhang-e Farsi is not online, so the two page numbers could not be checked; but Mo'in's entry text (abadis.ir) tags each of the three words '[فر.]' = French, exactly as the chart's arrow requires: مسیو '(مُ یُ) [فر.] (اِ.) آقا (در خطاب به فرنگیان گفته می‌شود.)', سنا '(س) [فر.] (اِ.) مجلسی که اعضای آن از بزرگان و اعیان کشور برگزیده شوند.', سناتور '(س) [فر.] (اِ.) عضو مجلس سنا، نمایندهٔ مجلس اعیان.' The two page numbers are consistent with the six-volume pagination (1925 in the lexicon volume for س, 4125 in vol. 4 of foreign words for م).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in online (abadis.ir), s.vv. مسیو، سنا، سناتور\",\n              \"stance\": \"supports\",\n              \"note\": \"All three carry the origin tag [فر.] (French). Quoted in ref_check above.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e rishe-hā — no entries\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for سنا/سناتور/مسیو in incoming/ARY/ARY_pages.txt returns no headwords; Aryanpur covers inherited Indo-European vocabulary, not 20th-century French loans.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"sir, senior, senile, senate, senator\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The root is right for all five, but the single arrow from French is right for only three. sir: Old French sire (from Vulgar Latin *seior, a reduced form of Latin senior) gave Middle English sire, and sir is its unstressed variant, attested c. 1300 as a knight's title (Etymonline: 'a variant of sire ... It is not an acronym of anything'). senate: ME senat, from Old French senat (Klein), c. 1200 of the Roman body, from Latin senātus. senator: ME senatour, from Old French senatour, from Latin senātōrem. But senior is a direct Latin borrowing — Klein: 'senior, adj. — L., \\\"older\\\", compar. of senex' — entering English in the 15th century as a school/academic term and never passing through French; and senile is from Latin senīlis (Klein: 'senile, adj. — L. senilis'), 1660s, a learned coinage of the scientific register. So for those two the chart should have an arrow straight from the Latin box.\",\n          \"derivation_fa\": \"ریشه برای هر پنج واژه درست است، ولی پیکانِ یگانهٔ «از فرانسوی» تنها برای سه‌تای آن‌ها درست است. sir: فرانسهٔ کهن sire (از *seior در لاتین عامیانه، صورت کوتاه‌شدهٔ senior) به انگلیسی میانه sire رسید و sir گونهٔ بی‌تکیهٔ آن است که از حدود ۱۳۰۰ م. عنوان شوالیه بوده (اتیمآنلاین تصریح می‌کند که sir سرواژه نیست). senate: انگلیسی میانه senat از فرانسهٔ کهن senat، از senātus لاتین. senator: انگلیسی میانه senatour از فرانسهٔ کهن senatour. اما senior وام مستقیم از لاتین است — کلاین: «senior، از لاتین، صفت تفضیلی senex» — و در سدهٔ پانزدهم به انگلیسی راه یافته و از فرانسوی نگذشته است؛ senile نیز از senīlis لاتین (کلاین) در دههٔ ۱۶۶۰ ساخته شده است. پس برای این دو واژه باید پیکانی مستقیم از جعبهٔ لاتین کشیده می‌شد. ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sir\",\n            \"https://www.etymonline.com/word/senate\",\n            \"https://www.etymonline.com/word/senior\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt s.v. sen-¹ lists exactly SENATE, SENILE, SENIOR, (SIR), SIRE among the English words from Latin senex, confirming the root membership of all five (without specifying the French vs. direct-Latin route).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.vv. senate, senator, senile, senior, sir, sire\",\n              \"stance\": \"partial\",\n              \"note\": \"KLN_1966.txt 34543 'senate ... ME. senat, fr. OF. senat'; 34544 'senator ... ME. senatour, fr. OF. senatour'; 35333 'sir, n. — Reduced form of sire'; 35336 'sire, n. — ME., fr. OF. sire, fr. *seior, vulgar form of L. senior'; but 34556 'senile ... L. senilis' and 34559 'senior, adj. — L., \\\"older\\\"' — both straight from Latin, not from French.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.vv. Senate, Sir\",\n              \"stance\": \"supports\",\n              \"note\": \"SKT.txt line 16854 'Senate, a council of elders. (F. – L.) F. senat. — L. senatum'; line 17320 'Sir, Sire; see Senate' — Skeat too routes senate and sir through French.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls — not consulted for this node\",\n              \"stance\": \"silent\",\n              \"note\": \"Klein, Skeat and Etymonline already agree on the chain; no further English dictionary was needed.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"sana\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Vedic sána- 'old, of long standing' is the Indic reflex of PIE *sen-o-, preserving the *s- that Iranian turned into h- (Skt. sána- : Av. hana-). Pokorny lists it first among the Material for sen(o)-, alongside the derivatives sanaká- 'former, old' (which he equates directly with Latin senex), sánā 'of old', sanát/sanátā 'from of old, always' and sanátana- 'eternal, perennial'. Buck adds that the word is Vedic and stands opposed both to náva- 'new' and to yúvan- 'young'.\",\n          \"derivation_fa\": \"سنسکریت ودایی sána- «کهن، دیرینه» بازتاب هندی *sen-o- هندواروپایی است و «س» آغازین را نگه داشته، همان که در ایرانی به «ه» بدل شده است (sána- سنسکریت در برابر hana- اوستایی). پوکورنی آن را نخستین شاهد مدخل sen(o)- آورده و مشتقات sanaká- «پیشین، کهن» (که آن را مستقیماً با senex لاتین برابر می‌نهد)، sánā «از دیرباز»، sanát/sanátā و sanátana- «جاودان» را نیز ثبت کرده است. باک می‌افزاید که این واژه ودایی است و هم در برابر náva- «نو» و هم در برابر yúvan- «جوان» می‌نشیند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/senate\"],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:907\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt sen(o)-: 'Material: Old Indic sana-, Avestan hana- \\\"old\\\", Old Indic sanaká- \\\"ehemalig, old\\\" (: Latin senex, Franconian Sinigus, gall. Seneca), sánā \\\"vor alters\\\", sanā, sanát, sanátā \\\"from alters her, from jeher, stets\\\", sanátana- \\\"eternal, immortal, perennial\\\"'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 14.15\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. (Ved.) sana- (opp. to nava- and yuvan-), sanaya-' (SYN.txt line 24433 ff.).\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. senos\",\n              \"stance\": \"supports\",\n              \"note\": \"IEC.txt line 15213: 'senos \\\"old\\\" ... Skt. sánaḥ, id.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. senile\",\n              \"stance\": \"supports\",\n              \"note\": \"KLN_1966.txt line 34556: 'senex, gen. senis, \\\"old\\\", which is cogn. with OI. sánaḥ, \\\"old\\\".'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T02:11:53.429Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-443.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:11:55.893Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-443.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 443",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T02:11:57.257Z] TOOL RESULT

```
JSON OK
nodes verified: 15/15
node verdicts: {'confirmed': 10, 'transcription_suspect': 3, 'disputed': 1, 'plausible': 1}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 5, 'not_checked': 1}
books consulted: {'supports': 20, 'partial': 7, 'silent': 8, 'contradicts': 2} | by book: {'KLN': 6, 'SYN': 5, 'BRT': 3, 'ARY': 3, 'SKT': 3, 'PHD': 3, 'MON': 3, 'IEC': 3, 'BQT': 2, 'NYB': 2, 'POK': 1, 'HUB': 1, 'KNT': 1, 'FSD': 1}
```


## [2026-09-14T02:12:15.530Z] AGENT

Page 443 (book p. 413) verified — 3 entries, 15 nodes, `verify_check.py 443` shows 0 PROBLEM lines.

**Verdicts:** roots — confirmed 2, plausible 1. Nodes — confirmed 10, transcription_suspect 3, disputed 1, plausible 1. Ref checks: supports 14, partial 5, not_checked 1.

**Flagged items (all book errors, extraction is faithful — page image saved to `data/verification/sources/refs/ocr/BOOK/443.png`):**
- **Sem 2 / #2 `hamîn «همین»`** — transcription_suspect. Horn p. 280 no. 106 prints **hāmīn**; Mo'in's Borhan footnote (vol. 4, p. 2374) says the Borhan spelling همین/همیز is «مصحف هامین». Correct form: hāmīn «هامین». Nourai copied the corrupt Borhan spelling, which is a homograph of everyday همین.
- **Sěma / #3 `siyaman`** — transcription_suspect + substantive caveat. Kent p. 209 prints **siyamam** (acc.-sg. -m). Kent also calls the word "dubious", the Greek borrowing "anachronistic", and cites Schaeder against the authenticity of inscription A¹I; Wiktionary nonetheless accepts it.
- **Sen 1 / #4 French `seinat`** — transcription_suspect; misprint for **sénat** (and `senateur` for sénateur).
- **Sen 1 / #2 `hân «هان»`** — disputed. Horn p. 280 no. 108 lists hān 'alt' in his appendix *Verlorenes Sprachgut* = Pahlavi words lost in New Persian; Borhan vol. 4 p. 2312 gives NP هان only as the attention particle "beware!". Language label should be Pahlavi, not Persian.
- **Sen 1 / #6 English** — plausible: *sir, senate, senator* come via Old French, but *senior* and *senile* are direct Latin borrowings (Klein), so the single French arrow is partly wrong.

**Strongest confirmations:** Kent p. 209 s.v. *siyamam* states the whole chain (Gk. ἄσημον → Phl. asēm → NPers. sīm); Mo'in's footnote 6 on Borhan p. 1212 reproduces Nourai's root box almost verbatim (ἀ- + σῆμα = "unminted silver", credited to Benveniste orally and Taqizadeh); Nyberg and MacKenzie both label MP asēm a Greek loan. Watkins AHD gives *sem-²* "Summer → Gmc. \*sumaraz" citing Pok. 905, and *sen-¹* citing Pok. 907 — both exactly Nourai's citations.

**No extraction errors found** — the JSON matches the printed page in every case.

**One infrastructure note for the owner:** `data/verification/sources/refs/KNT.txt` is truncated at printed page ~207, so the Kent lexicon's s/š/z/h section (incl. p. 209) is missing; I pulled it from `https://ia800101.us.archive.org/20/items/oldpers/oldpers_djvu.txt`, which is complete. Re-downloading that file would help future pages citing KNT ≥ 208.
