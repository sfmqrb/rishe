# Verification process log — verify-page-537


## [2026-10-16T05:13:02.159Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 537 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-537.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-537.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-537.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 537` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.220Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.289Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.319Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-16T05:13:05.795Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-537.txt"
}
```


### [2026-10-16T05:13:05.828Z] TOOL RESULT

```
1	=== PDF page 537 (book page 507) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Weis : to rot, melt away, flow  (refs POK:1134)
4	#1 (parent #0) [Avestan] refs=POK:1134; KLN:1714 | vaeša : mold ; viš 1, viša : rotten food, poison
5	  #2 (parent #1) [Pahlavi] refs=BQT:338 | běš 2 : a poisonous plant | NOTE: See "Dwei" for an alternative root.
6	    #3 (parent #2) [Persian] refs=BQT:338 | bîš 2 «بیش ٢» : a poisonous plant
7	#4 (parent #0) [Latin] refs=AHD | virus : slime, poison ; viscum : slime
8	  #5 (parent #4) [French] refs=None | virus
9	    #6 (parent #5) [Persian] refs=MON:5070 | vîrŭs «ویروس» : virus
10	  #7 (parent #4) [English] refs=None | virus ; viscous
11	#8 (parent #0) [Germanic] refs=AHD | wisôn : slime ; wisolon : stinking animal, weasel ; wisand : a bison with musky smell
12	  #9 (parent #8) [English] refs=None | ooze 2 : mud, sediment ; weasel ; bison
13	--- entry 1 ---
14	ROOT [Indo-European] Wek : to wish, desire  (refs POK:1135; KNT:207)
15	#1 (parent #0) [Old Persian] refs=KNT:207; BST:234 | vas : to wish, desire ; vašna : will, desire ; vasiy : at will
16	  #2 (parent #1) [Pahlavi] refs=MON:537; KNT:207; BQT:276 | vas : enough ; vas-yâr : plenty
17	    #3 (parent #2) [Persian] refs=KNT:207; BQT:276; MON:537 | bas «بس (بسی)» : enough, sufficient ; basand «بسند (بسنده)» : sufficient ; besyâr «بسیار (بسیاری)» : plenty, many
18	#4 (parent #0) [Avestan] refs=POK:1135 | vasami, usâmahi : I wish ; an-usant : not willing, reluctant ☞Ne 1 ; vasah : desired ; vasnah : wish
19	#5 (parent #0) [Greek] refs=POK:1135 | exôn : willing ; a-exôn : not willing, reluctant
20	
```


## [2026-10-16T05:13:06.394Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-537.json"
}
```


### [2026-10-16T05:13:06.666Z] TOOL RESULT

```
1	{
2	  "pdf_page": 537,
3	  "book_page": 507,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Weis",
8	        "lang": "Indo-European",
9	        "refs": "POK:1134",
10	        "gloss": "to rot, melt away, flow"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1134; KLN:1714",
18	          "words": [
19	            {"translit": "vaeša", "gloss": "mold", "script": null},
20	            {"translit": "viš 1, viša", "gloss": "rotten food, poison", "script": null}
21	          ],
22	          "script_extra": null,
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Pahlavi",
30	          "refs": "BQT:338",
31	          "words": [
32	            {"translit": "běš 2", "gloss": "a poisonous plant", "script": null}
33	          ],
34	          "script_extra": null,
35	          "note": "See \"Dwei\" for an alternative root.",
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "Persian",
42	          "refs": "BQT:338",
43	          "words": [
44	            {"translit": "bîš 2", "gloss": "a poisonous plant", "script": "بیش ٢"}
45	          ],
46	          "script_extra": null,
47	          "note": null,
48	          "quote": null
49	        },
50	        {
51	          "id": 4,
52	          "parent": 0,
53	          "lang": "Latin",
54	          "refs": "AHD",
55	          "words": [
56	            {"translit": "virus", "gloss": "slime, poison", "script": null},
57	            {"translit": "viscum", "gloss": "slime", "script": null}
58	          ],
59	          "script_extra": null,
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 5,
65	          "parent": 4,
66	          "lang": "French",
67	          "refs": null,
68	          "words": [
69	            {"translit": "virus", "gloss": null, "script": null}
70	          ],
71	          "script_extra": null,
72	          "note": null,
73	          "quote": null
74	        },
75	        {
76	          "id": 6,
77	          "parent": 5,
78	          "lang": "Persian",
79	          "refs": "MON:5070",
80	          "words": [
81	            {"translit": "vîrŭs", "gloss": "virus", "script": "ویروس"}
82	          ],
83	          "script_extra": null,
84	          "note": null,
85	          "quote": null
86	        },
87	        {
88	          "id": 7,
89	          "parent": 4,
90	          "lang": "English",
91	          "refs": null,
92	          "words": [
93	            {"translit": "virus", "gloss": null, "script": null},
94	            {"translit": "viscous", "gloss": null, "script": null}
95	          ],
96	          "script_extra": null,
97	          "note": null,
98	          "quote": null
99	        },
100	        {
101	          "id": 8,
102	          "parent": 0,
103	          "lang": "Germanic",
104	          "refs": "AHD",
105	          "words": [
106	            {"translit": "wisôn", "gloss": "slime", "script": null},
107	            {"translit": "wisolon", "gloss": "stinking animal, weasel", "script": null},
108	            {"translit": "wisand", "gloss": "a bison with musky smell", "script": null}
109	          ],
110	          "script_extra": null,
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 9,
116	          "parent": 8,
117	          "lang": "English",
118	          "refs": null,
119	          "words": [
120	            {"translit": "ooze 2", "gloss": "mud, sediment", "script": null},
121	            {"translit": "weasel", "gloss": null, "script": null},
122	            {"translit": "bison", "gloss": null, "script": null}
123	          ],
124	          "script_extra": null,
125	          "note": null,
126	          "quote": null
127	        }
128	      ]
129	    },
130	    {
131	      "root": {
132	        "name": "Wek",
133	        "lang": "Indo-European",
134	        "refs": "POK:1135; KNT:207",
135	        "gloss": "to wish, desire"
136	      },
137	      "nodes": [
138	        {
139	          "id": 1,
140	          "parent": 0,
141	          "lang": "Old Persian",
142	          "refs": "KNT:207; BST:234",
143	          "words": [
144	            {"translit": "vas", "gloss": "to wish, desire", "script": null},
145	            {"translit": "vašna", "gloss": "will, desire", "script": null},
146	            {"translit": "vasiy", "gloss": "at will", "script": null}
147	          ],
148	          "script_extra": null,
149	          "note": null,
150	          "quote": null
151	        },
152	        {
153	          "id": 2,
154	          "parent": 1,
155	          "lang": "Pahlavi",
156	          "refs": "MON:537; KNT:207; BQT:276",
157	          "words": [
158	            {"translit": "vas", "gloss": "enough", "script": null},
159	            {"translit": "vas-yâr", "gloss": "plenty", "script": null}
160	          ],
161	          "script_extra": null,
162	          "note": null,
163	          "quote": null
164	        },
165	        {
166	          "id": 3,
167	          "parent": 2,
168	          "lang": "Persian",
169	          "refs": "KNT:207; BQT:276; MON:537",
170	          "words": [
171	            {"translit": "bas", "gloss": "enough, sufficient", "script": "بس (بسی)"},
172	            {"translit": "basand", "gloss": "sufficient", "script": "بسند (بسنده)"},
173	            {"translit": "besyâr", "gloss": "plenty, many", "script": "بسیار (بسیاری)"}
174	          ],
175	          "script_extra": null,
176	          "note": null,
177	          "quote": {
178	            "text": "به آورد با او بسنده نبود - بپیچید ازاو روی و برگاشت زود",
179	            "poet": "Ferdowsî"
180	          }
181	        },
182	        {
183	          "id": 4,
184	          "parent": 0,
185	          "lang": "Avestan",
186	          "refs": "POK:1135",
187	          "words": [
188	            {"translit": "vasami, usâmahi", "gloss": "I wish", "script": null},
189	            {"translit": "an-usant", "gloss": "not willing, reluctant", "script": null, "see": ["Ne 1"]},
190	            {"translit": "vasah", "gloss": "desired", "script": null},
191	            {"translit": "vasnah", "gloss": "wish", "script": null}
192	          ],
193	          "script_extra": null,
194	          "note": null,
195	          "quote": null
196	        },
197	        {
198	          "id": 5,
199	          "parent": 0,
200	          "lang": "Greek",
201	          "refs": "POK:1135",
202	          "words": [
203	            {"translit": "exôn", "gloss": "willing", "script": null},
204	            {"translit": "a-exôn", "gloss": "not willing, reluctant", "script": null}
205	          ],
206	          "script_extra": null,
207	          "note": null,
208	          "quote": null
209	        }
210	      ]
211	    }
212	  ]
213	}
214	
```


## [2026-10-16T05:13:13.550Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/.claude-work/projects/-home-sfmqrb-git-rishe-private/memory/checkout-setup.md; cat /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md | head -80; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ | head -100; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -80"
}
```


### [2026-10-16T05:13:13.853Z] TOOL RESULT

```
---
name: checkout-setup
description: "How the rishe-private checkout was wired up on 2026-10-14 (remotes, worktree, ref library, hook)"
metadata:
  node_type: memory
  type: project
  originSessionId: 7c41a241-7571-4c3b-8e91-929d2c62eed6
  modified: 2026-10-15T02:20:15.267Z
---

The repo now lives at /home/sfmqrb/git/rishe-private (it used to be /home/sfmqrb/git/rishe). On 2026-10-14 it was set up to match COORDINATOR.md:
- `origin` = public sfmqrb/rishe, `private` = sfmqrb/rishe-private. Working branch is `verified`.
- `../rishe-backup` is a worktree on `verified-with-sources`. The reference library (`sources/refs/`) was rsynced from there into the main tree, where it is gitignored.
- `.git/hooks/pre-push` blocks pushes of `sources/refs/` to any remote except `private`. The hook is not versioned.
- Subagent transcripts are at `~/.claude-work/projects/-home-sfmqrb-git-rishe-private/<session>/subagents/`.
- Known gaps: `refs/tessdata` (Persian OCR traineddata; the system only has eng), the `incoming/*_faseng.txt` files and the Bailey PDF were never in the backup.

**Why:** the docs and scripts assumed the old path and remote layout.
**How to apply:** if the checkout is re-cloned, redo these steps before launching verification agents.
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
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


## [2026-10-16T05:13:17.530Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 80,200p /home/sfmqrb/git/rishe-private/tools/verify_check.py; sed -n 80,200p /home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md"
}
```


## [2026-10-16T05:13:19.717Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json\nd=json.load(open('page-536.json')) if __import__('os').path.exists('page-536.json') else json.load(open('page-501.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\n\"; python3 -c \"\nimport json;r=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','MON','AHD','KNT','BST']: print(k, json.dumps(r.get(k),ensure_ascii=False)[:600])\n\""
}
```


### [2026-10-16T05:13:20.212Z] TOOL RESULT

```
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
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
```


### [2026-10-16T05:13:20.490Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Ten 1, Tengh, Temp",
 "verdict": "confirmed",
 "modern_form": "PIE *ten- 'to stretch' (Pokorny 1. ten- 1065-1066; LIV 626 f.), with the enlargements *tengʰ- 'to pull, draw' (Pokorny 1067; Cheung *θanǰ) and *temp- 'to stretch' (Pokorny 1064; Watkins temp-)",
 "note": "The root box is correct: Pokorny p.1064 has 'temp- to extend, stretch, span; Note: extension from *ten-', p.1067 'tengh- to extend, stretch, span; Aryan *thengh-, yet probably extension from ten-1', and pp.1065-1066 the base '1. ten-, tend- to extend, stretch'. Nourai's citation POK:1064,1067 covers the two enlargements; the base is on p.1065. Watkins (AHD) lists ten- and temp- with exactly Nourai's English outcomes (SITAR under ten-, TAFFETA and TAPESTRY under temp-). Problems lie in individual branches: (1) Av. tauruna- 'young' (#8) belongs to a different root, PIE *ter-/teru- 'tender, weak' (Pokorny 1070-1071, Mann teren-, Klein s.v. tender), so the tar/tarāneh/tūleh/tūrah branch does not belong under Ten; (2) Greek kithara (#14) is not from Persian tār/si-tār — it is a Pre-Greek word attested from Homer (kitharis), centuries before the Persian si-tār, although Klein (whom Nourai follows) writes 'Gk. kithara, fr. Pers. sihtār'; (3) English tape is a native Old English word (tæppe), not from the Persian/Greek carpet word; (4) Persian tābīdan 'twist' comes from the *temp- enlargement (Iranian *tāp-), not from Av. tan- as drawn; (5) hanjār 'path, norm' has no secure link to *θanǰ (Wiktionary: from Parthian anjār 'behaviour'; Mo'in compares Skt saṃcāra). The Avestan 'tathra' and 'thri-thatra' are not attested: the first is the reconstructed *tąθra- of Horn and Pokorny, the second appears to be Nourai's own back-projection of si-tār. The JSON matches the printed page (checked against the page image), including the inconsistent spellings tathra / thri-thatra and the reference 'KLN:572', which is a misprint in the book for KLN:1572 (tapestry). No extraction errors.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ten- «کشیدن، کش دادن» (پوکورنی ۱۰۶۵–۱۰۶۶) و دو گونهٔ گسترش‌یافتهٔ آن، *tengʰ- «کشیدن، بیرون کشیدن» (پوکورنی ۱۰۶۷) و *temp- «کش دادن» (پوکورنی ۱۰۶۴)، درست آمده است و واتکینز نیز همین سه را با sitar و taffeta و tapestry آورده است؛ پس سرریشهٔ نورایی درست است. ایراد در چند شاخه است: «تئوروونه» (tauruna) اوستایی به معنای «جوان» از ریشهٔ دیگری (*ter- / *teru- «نرم، نازک») است، نه از *ten-؛ «کیثارا»ی یونانی از «سه‌تار» فارسی نیست و پژوهش امروزی آن را واژه‌ای پیشایونانی می‌داند؛ tape انگلیسی واژه‌ای بومی است؛ «تابیدن» از ستاک ایرانی *tāp- (گونهٔ *temp-) است نه از tan- اوستایی؛ و پیوند «هنجار» با *θanǰ ثابت نیست. «tathra» و «thri-thatra» در اوستا گواهی نشده‌اند و بازسازی (یا ساختهٔ خود نورایی) است. خطای استخراج دیده نشد؛ «KLN:572» در خود کتاب چاپ شده و خطای چاپی به جای ۱۵۷۲ است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ten-",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-",
  "https://en.wiktionary.
{
 "id": 1,
 "lang": "Avestan",
 "words": "thang, â-thax, hanč; far-thang",
 "verdict": "plausible",
 "derivation": "Young Avestan θang- / θanj- 'to pull, draw (a chariot), draw (a sword), draw (a bow)' (Bartholomae col. 785-786; pres. θanjaya-, ppp. θaxta-; with fra- 'to drive forward', fraθanjayeiti Yt 17.2) is the regular Iranian reflex of PIE *tengʰ- (Iranian *θanǰ-, with the unexplained θ- discussed by Cheung). 'â-thax' corresponds to the ā-prefixed participle *ā-θaxta- underlying MP āhixt (not itself attested in Avestan), and 'far-thang' to fra-θanj-, which in Avestan means 'drive forward'; the sense 'educate' belongs to MP frahanj-/frahixtan and NP farhang. 'hanč' is not Avestan: it is the Old/Middle Persian development *θ > h (MP hanj-, Kent's OP ha(n)j- in frāhajam, which Kent however derives from a different verb 'hang'). The core claim (Av. θang- 'pull') is confirmed; the extra forms are reconstructed or belong to later Persian, hence 'plausible'.",
 "derivation_fa": "فعل اوستایی θang- / θanj- به معنای «کشیدن (گردونه، شمشیر، کمان)» در فرهنگ بارتولمه (ستون ۷۸۵–۷۸۶) گواهی شده و با پیشوند fra- به معنای «پیش راندن» است؛ چونگ آن را از ایرانی *θanǰ- و هندواروپایی *tengʰ- (گونهٔ گسترش‌یافتهٔ *ten-) می‌داند. ولی «â-thax» صورت بازسازی‌شدهٔ *ā-θaxta- است و «hanč» اوستایی نیست بلکه صورت پارسی/فارسی میانه (hanj-) است که در آن θ ایرانی به h بدل شده؛ معنای «آموزش» نیز از فارسی میانهٔ frahang است. اصل ادعای نورایی درست است، ولی برچسب «اوستایی» برای همهٔ صورت‌ها دقیق نیست؛ با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tengʰ-",
  "https://en.wiktionary.org/wiki/آهیختن"
 ],
 "ref_check": [
  {
   "ref": "BQT:2381",
   "status": "supports",
   "note": "ref_page.py BQT:2381 (vol.4 pdf p.464), s.v. هنگ, Mo'in quotes Pur-Davud: 'دراوستا فعل تهنگه (θang) بمعنی کشیدن بسیار بکار رفته وازین مصدر (ریشه) چندین واژه درفارسی بجا مانده؛ ازآنهاست: هنگ (= آهنگ)، هنجیدن، با پیشاوند ā آهنجیدن ... هختن (= هیختن)، با پیشاوند ā آهختن (= آهیختن)، با پیشاوند فر فرهختن، باپیشاوند بر برهیختن، باپیشاوند فرو فروهختن'."
  },
  {
   "ref": "BQT:2376",
   "status": "supports",
   "note": "BQT_v4_pages.txt [pdf page 459] = printed 2376, s.v. هنج fn.: 'ریشهٔ اوستایی θang (کشیدن) بارتولمه ۷۸۶. از همین ریشه است: آهنج (آهنجیدن)، آهیختن، فرهنگ'."
  },
  {
   "ref": "BQT:1481",
   "status": "partial",
   "note": "ref_page.py BQT:1481 (vol.3 pdf p.274) s.v. فرهنگ / فرهیختن: 'فرهیختن بروزن انگیختن، بمعنی ادب آموختن ... فرهختن درست مطابق است درمفهوم با educere و educare لاتینی بمعنی کشیدن ... در پهلوی frahixtan'. Confirms the 'pull' > 'educate' sense, but this page does not itself name Av. θang-."
  },
  {
   "ref": "SNS:7",
   "status": "partial",
   "note": "SNS_pages.txt index (OCR poor): 'ahanjišn 7/2', '-hanc 7/3' — p.7 of Tavoosi's glossary has MP āhanjišn 'drawing' (the Avestan-Pahlavi pair), consistent with Nourai; the page text itself is not legible in the OCR."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "c
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local fil
BST {"title": "P. Horn, 'Some Inscriptions on Sassanian Gems', in Avesta, Pahlavi and Ancient Persian Studies in honour of Dastur P. B. Sanjana, First Series, Bombay 1904, pp. 224-263", "edition_found": "1904", "kind": "archive_djvu", "url": "https://archive.org/details/avestapahlavianc00sanjuoft", "identifier": "avestapahlavianc00sanjuoft (also in.ernet.dli.2015.281259)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BST.txt", "page_offset": "leaf = printed + 16 (e.g. leaf 18 = p.2), so pp. 224-263 = leaves ~240-279. local file has \\f between leaves (0-based leaf i
```


## [2026-10-16T05:13:24.037Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;r=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','BQT','KNT','AHD','WLD','MON','BRT','PHD','NYB','HRN','HUB','SKT','IEC']: \n  v=r.get(k) or {}\n  print(k, '|', v.get('page_offset'), '|', v.get('lookup_hint','')[:500]); print()\n\""
}
```


### [2026-10-16T05:13:24.412Z] TOOL RESULT

```
POK | POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas

KLN | KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

BQT | vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag

KNT | leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

AHD | 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg

WLD | Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

MON | None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden

BRT | Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

PHD | leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB | Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

HRN | leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

HUB | leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.

SKT | leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.

IEC | TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
```


## [2026-10-16T05:13:28.569Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'lemma: (u̯eis|weis|u̯ek|wek)' POK_full.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==1134-762+1 || NR==1135-762+1 || NR==1134-766+1 ||NR==1135-766+1 {print \"=====LEAF\",NR-1; print}' POK_03.txt | grep -n -i -E 'u̯eis|weis|virus|vaēša|vīš|wisun|wisent|u̯ek|vasmi|ἑκών|usant|vasn|leaf' | head -60"
}
```


### [2026-10-16T05:13:28.923Z] TOOL RESULT

```
1:=====LEAF 368
3:arm.  egit  ,er  fand*  (=  ai.  dvidat,  gr.  efids),  gtanem  ,finde';  aus  dem Perf.  *uoida  umgebildet  gitem  ,ich  weiß'  (i  aus  oi\  dazu  gU,  gitak,  giiun ,wissend,  weise');  Nachwirkung  des  Nasalpräsens  (=  ai.  vindati,  iv,  finn-y s.  u.)  vielleicht  in  arm.  gint  ,  Gewinn',  wenn  aus  '^uind--^
7:lat.  visö,  -ere  ,besuchen'  (d.  i.  ,zu  sehen  wünschen'),  umbr.  revestu  ,revisito' ^ueid-s-ö)]  ähnlich  got.  gaweisön,  as.  ahd.  wtsön  , besuchen';
11:=====LEAF 369
13:got.  /raj^-ezVari  , rächen'  (,animadvertere'),  ahd.  ßrwlzzan  ,tadelnd  Yftr* •  werfen,  verweisen',  icizzan  ^bemerken,  achtgeben  auf,  as.  ags.  wXtan  Vor*  ^ werfen,  tadeln'  (davon  aisl.  viti  n.  ags.  wUe,  as.  wlti,  ahd.  nnzzi  n.  JStr^lk<v  | got.  in-weitan  ,die  Verehrung  erweisen';  mit  auffälliger  Bed.-Entw.'ifg-" gewltan  ^fortgehen,  sterben',  as.  giioltan  , gehen',  ahd.  (Hildebrandlied)  giwA ,er  ging',  (Tatian)  arawlzan  ,discedere*;  got.  fairweitjan  ,gespannt  hift» blicken  auf,  vielleicht  zur  Basis  auf  -e : -i-,  wie  sicher  die  g-Verben"*^!, ivitan,  -aida  ,auf  etwas  sehen,  beobachten',  aisl.  nur  Partiz.  vitadr  .bt» obachtet,  bestimmt',  ags.  (bejwitian  , betrachten,  bestimmen';  PräteritopriiMÄl got.  tvait^  witum  , weiß,  wir  wissen'  (Inf.  züz^an,  Partiz.  witands  Neubildanjäi aisl.  veit  vitum  (vita,  vissa)  , wissen',  auch  ,bemerken,  erforschen,  anzeigML gerichtet  sein  nach,  schauen  nach,  gehen  nach',  ags.  wät,  witon  (ivitan,  tciiii loiste),  ahd.  weiz,  tvizzumes  {icizzarij  wissa,  wessa)  ,wissen'  substantiviertü Partiz.  got.  weitwöps  , Zeuge'  (:  eiöiogy  Idvia  , Zeuge') ;  ^o-Partiz.  got.  unicill jungewiß',  ahd.  gküis{s),  as.  ags.  tuiss  ,gewiß'  (aisl.  vissa  , Gewißheit');  Kaoii^ aisl.  veita  ,gewähren,  leisten,  helfen ;  auch  Wasser  in  eine  Richtung  leitea*,^ ahd.  weizen  , zeigen,  beweisen';  zu  fLÖsXv  scheint  als  Injunktiv  ags.  vmi^ (mit  folgendem  Inf.)  aus  *iviton  ,laßt  uns'  (älter  ,laßt  uns  zusehen,  tendft- mus')  zu  gehören;
19:.^^ita  .weiser  Mann,  Ratgeber^  gewita  ,  Zeuge',  ahd.  ivizzo  , weiser  Mann^ glioizzo  , Zeuge'  postverbale  en-St. ;  aber  a.u\  fiadu  , Zeuge*  {*ueid-uöt-s) gekundärer  ?2-St.;
21:=====LEAF 372
33:=====LEAF 373
```


## [2026-10-16T05:13:31.517Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'Page\\(s\\): 113[3-6]' POK_full.txt | head; grep -n -i -E 'lemma: .{0,4}(eis|ek)-' POK_full.txt | head -20"
}
```


### [2026-10-16T05:13:32.352Z] TOOL RESULT

```
89987:Page(s): 1133-1134 
90086:Page(s): 1134-1135 
90177:Page(s): 1135-1136 
90262:Page(s): 1136-1137 
3187:Root/ lemma: aios-: 'metal (copper; iron)' derived from Root/ lemma: eis-1: 'to move 
22999:Germanic -s- > -r-] of Root / lemma: ueis-2\ "to turn, bend'. 
24633:Root / lemma: eis-1 
24639:Root/ lemma: aios-\ 'metal (copper; iron)' : Root/ lemma: eis-1 \ 'to move rapidly, 
27404:Root / lemma: erek-1 {erfejgh^ 
27414:Root / lemma: erek-1 {eije]gh^\ louse, tick, derived from a suffixed Root/ lemma: er-2, eri- 
32613:Root / lemma: gheis- and gheiz-d- 
34907:Root / lemma: geis- 
44575:Root / lemma: keis- 
48312:Root / lemma: krek-1 {-k-7) 
48341:Root / lemma: krek-2, kfk- 
48372:Root / lemma: krek-3 
48713:Root / lemma: krek-4 : krok- 
49019:Root / lemma: kueiek- or kelak-, kolak- 
56672:Root / lemma: lek-2\ lak- 
63092:Root/ lemma: nog''-, nog''od(h)o-, nog^-no-. naked > Root/ lemma: lek-2. lak-\ to tear, 
63527:lemma: dek-1\ "to take, *offer a sacrifice, observe a custom' [common lllyrian-Baltic d- > 
65150:Root / lemma: {peis-'H) : pis- 
65176:Root / lemma: peis-2, speis- 
70164:Root / lemma: rek-1
```


## [2026-10-16T05:13:35.100Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 90040,90200p POK_full.txt"
}
```


### [2026-10-16T05:13:35.504Z] TOOL RESULT

```
Page(s):1134 

Root / lemma: uek-ti- 
Meaning: thing 
Note: {uek'^-ti-1) 

Material: Gothic wafhtsi. "thing'. Old Icelandic vettr, vge(t)r, vitri. " living being, 
ijbermenschliches creature, thing'. Old English wihti. "thing, entity, demon'. Old Saxon 
wikt. Middle Low German tv/ic/?/ "entity, creature'. Old High German wiht^ living being, 
demon, thing'. Modern High German Wicht^ living creature, goblin, ugly mischievous sprite 
'; Gothic /7/-M/a/77/"nichts', Old English na-wiht {ev\i^\. naught, not) Old High German niwiht 
and neowiht^v\o{, nichts'; 

Old Church Slavic vestbi. " thing '; compare wruss. recb "thing': russ. recb " discourse, 
word'. 

References: WP. I 246, Vasmer 1, 196; 
See also: perhaps to uek'^- "speak'. 
Page(s):1136 

Root / lemma: uek-, ue-n-k- 
Meaning: to bend 



Material: Old Indie vancat/'geht. crooked or slant, skew', vacyate 'sch\N'\ng\. sich, flies', 
vakra- "gebogen, crooked', vank'u- "fliegend', vaiikri-i. " rib ', vaiika-, vankara- m. 
Tluftkrummung', va/iksana-m. " groin, flank', vaksana^beWy, groin, flank, riverbed '; 
Avestan -vasta- " writhed, crooked, humped '; common Old Indie -gh- > -ks- : Avestan -gh- 
> -xs- > -s- 
Armenian ^a/T^^r'crispus, flexus' {*unkuro)\ 

Latin convexus^ arched, writhed, crooked, humped ', 5^,6* i/ex^s "sch rag aufwarts 
fijhrend'; 

Middle Irish feccaid^bucVX sich', with the preposition for. 'wendet sich gegen, beginnt to' 
(with expressive -kk-)\ gall. FIN * Vocalus {Uaires Vocallinehae), germanisiert Vacalus, 
Va{c)ha//s ^VJaaV; Lithuanian FIN Vbke {* uokia); 

Indo Germanic uonko- in Old Indie vaiika-, Gothic i//>M/a/7s"untadelhaft', Old English 
14/0/7 'crooked, inverted ', Old Saxon wahn. " evil, wickedness ', Old Icelandic vai. 
( *uonkd) ' angle, mischief '. 

References: WP. I 246, WH. I 268 f.: after Kuiper, Nasalpras. 142 zur root t/a-(see above 
S. 1108), where besides dem present *ua-n-ek-mi e\v\ Konj. *u (9)-9n u-ko s\.av\&, 
consequently further zur root ua-, uag-, uak-, ueng(h)-, see there. 
Page(s): 1134-1135 

Root / lemma: ueR- 
Meaning: to wish 

Material: Old Indie vas-mi, vast/, us-masi, Avestan vasamT, usamahrwant, desire, will, 
wish', participle Old Indie usant-, f. ^sa/r willing', Avestan an-usant-, -i/5a///"'widerwillig, 
ohne es to want, desire, will', Avestan vasah- (Nom. vasa) 'wollend = after seinem Willen', 
vaso, i/asa 'after wish, beliebig' (Akk. Sg. of n. * vasah-), vaso-xsa^ra-^aiier QeiaWeu 
schaltend' etc.. Old Indie vasi-tva-v\. 'Willensfreiheit'; ap. vasna, Avestan i/as/75(lnstr. Sg.) 
'after dem Willen' (Armenian i/as/? 'because of loanword); 

gr. (previous participle) ekojv (Cretan Fskojv), SKOuaa 'freiwillig' (the Asper afters 'sich', 
as though 'from sich selbst heraus'), qekcjov, qkcjov 'wider Willen, ohne Vorsatz', f. Doric 
asKaaaa, compare Cretan ysKaGa SKOuaa Hes., Fskq in oucpsKa ouk apsaTux; Hes., i.e. ou 
Fekq, in £V£Ka, hom. sTvsKa 'because of (*£vF£Ka; £v is die preposition £v), hom. £Ka-£pYO(; 
'after Belieben wirkend', £Kr|-poAo(; 'after Belieben treffend' (metr. lengthening for *£Ka- 
(3oAo(;), out of it extended £KaTr|-p6Ao(;, -p£A£Tr|<;; Boeotian F/7£Ka-5a|JO(; (with versch. 



assimilation out of it thes. FsKsSapot;, Attic 'AKa5r||J0<;); £Kr|Ti, Doric skqti "after dem Willen, 
because of, (unclear)', asKa^opsvoc; 'not wollend, widerstrebend' (after avavKa^opEvoc;); 

Hittite uek- "wish, arrogate'. 

References: WP. I 244 f.. Frisk 473 f., 477, 479. 
Page(s):1135 

Root / lemma: ueic- {*huek"'-) 

Meaning: to speak 

Note: 

labialized old laryngeals {*hue-) 

Material: Old Indie vakti, vfvakti^ says, talks, speaks', Aor. avdcam{= sTnov, see below), 

participle ukta-, Kaus. vacayati, Avestan 1/5/r- "speak', uxta-. Old Indie vacas-v\. = Avestan 

vacah{= gr. luo(^) " discourse, word'. Old Indie Kac5/75-"redend, sagend', vac-, Nom. Sg. 

vak= Avestan vaxs{= Latin vox) "voice, discourse, word'. Old Indie vacala- " gabby, 

gossipy, loquacious, garrulous, blithering ', i/a/ry5/r7"Aussprueh, discourse '; vaktram 

"mouth'; 

Armenian gocem^cry, shout, shout to mir, lade ein, name' (?); 

Note: 

labialized old laryngeals {*hue-) 

common Armenian Celtic *hue- > gwo- > go-. 

gr. ETTOc;, el. Cypriot Fettoc; n. "word', Aor. slnov "sprach', Lesbian Fsinnv etc. (= Old 
Indie avocam, Indo Germanic *e-ue-uk"-om\N\\h Diss, from -FsF- to -Fei-), ona Akk. "voice' 
(also probably supuona as "den weithin schallenden'), oaaa f. "voice', svonn "shout, call, 
clamor '; 

Maybe alb. fem, them " say ' 

Latin vox, i/dc/s "voice', voco, -are'caW, shout, cry', Umbrian sub-ocau, -ocanu, -oco^ 
call, anbeten'; 

Old Irish foccu/'word' (= Old Indie i/5/r//'a/77 "mouth') < *uok"'-t/o-m = cymr. gwaethi 
"fight'; fua/mm'd\n, fuss, noise' {*uok"-smn); common lllyrian-celt. -k > -th. 

gall. Vepo-litanos^ breitgesichtig ', cymr. gweJblace'; 



Old High German giwahanen, -inen^ mention, commemorate ' {*gawahnjan, Denom. 
*uok"-no-, compare Old Indie vacana-; in addition tread in paradigm connection old 6- 
grade Pf.:) giwuog. Middle High German wuegen^ commemorate make, in Erinnerung 
bringen'. Old Icelandic i/a///'"Zeugnis' {*wahtaz, compare Old High German giwahtxr\. " 
mentioning, Ruhm'), i/a//a"bezeugen'; Old Icelandic omunt 'voice', nisi. dmur'soun6', 
Old English wdm{a)'d\n, fuss, noise' {*wdhm-)\ 

Old Prussian wackTtweT entice ', enwackemai^ we rufen an'; 
Note: 
The origin of labialized old laryngeals: 

Hittite huek-, huk- " adjure ', Tocharian A waki., B wek^yo\ce\ 

References: WP. I 245 f., WH. II 823 ff., Trautmann 339 f., Vasmer 1, 196, Bergin Eriu 12, 

136f. 

Page(s): 1135-1136 

Root / lemma: ue-2, ued!^- 

Meaning: " braid, plait, fold, roll up, twist, curl ' 

See also: see above S. 75 f. {au-). 

Page(s):1114 

Root / lemma: uelk-1 
Meaning: to drag 



Material: Avestan i/aAa/r-'ziehen, drag' only with Praverbien: aipivar9cainti^7\eher\ ein 
KleidungsstiJck dariJber an'; Lithuanian velku{vilkti). Old Church Slavic i//e/rp"pull, drag' = 
gr. a[F]oA^ (by Hom. for wA^ einzusetzen), Attic out of it reconverted with metathesis aAo^; 
u)Aa^ (hybridization from wA^ with auAa^) 'furrow', with Vokalvorschlag *a-F^- in auAa^ 
"furrow', *£-Fyk-a in lakon. euAoKa "plough'. 

References: WP. I 306, Trautmann 349 f.. Frisk 77; after Specht KZ. 66, 25 to suelk-, as 
se/A-- above S. 901. 
Page(s):1145
```


## [2026-10-16T05:13:40.693Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89960,90040p POK_full.txt"
}
```


### [2026-10-16T05:13:41.018Z] TOOL RESULT

```
Bewegung' here probably also Lithuanian viskiu, i//s/re//" quiver'; by East Frisian wisk 
"rasche Bewegung, Husch', Middle High German wischen^s\ch leicht and quick, fast 
dahinbewegen'. Modern High German enfm'schen kann secondary development from " 
fleeting about etwas wegwischen' vorliegen; 

Maybe alb. (^Vistula) vetulla' eyebrow'. 

besides Germanic p-Varianten on the one hand in ndd. wispeln^s\c\\ hin- and 
herbewegen', Swedish visp, visper^ changeable person', on the other hand in Norwegian 
K/spm. " tassel, tussock ', Swedish i//5/0 "verticil, whorl, group of parts (leaves, flowers, 
etc.) arranged in a circle from Ruten'. 

C. With 5«-extension: 



Latin v/rga'\h'\n twig, brancli, rod, rod' (from *y/z-ga), in addition v/rgd'g'\r\, virgin'; 

Maybe alb. vargu' row, line' 

Maybe alb. {*verga) varze^ girl' : Italian vergine : Spanish virgin : French vierge : Catalan 
verge : Latin virgo : Portuguese virgem : Sardinian Campidanesu birgini : Valencian verge 
: Breton gwerc'hez : Welsh gwyryf " virgin'. 

Lithuanian K/z^i/, i//zge// "tremble', iz/zg'd// "waver'. 

References: WP. I 242 f., WH. II 799, 802, Trautmann 345, 347, Vasmer 1, 195, 207, 243. 
Page(s): 1133-1134 

Root / lemma: ueis-3 

Meaning: to flow; poison 

Material: Old Indie i/esa//"zerflieftt', i//sa-n. " poison ', Adj. "giftig', vis- (Nom. vit) and vistha 

" excrement, ordure', also "tierischer Samen', visra- "muffig smelling '; Avestan vis-, visa-^ 

poison ', vaesah-^ mould, dank decay, Verwesung'; Armenian ges^ carrion '; 

gr.loc; " poison ' = Latin i//7-£/5 "tough Flijfligkeit, mucus, juice, sap, poison, sharpness' = 
Middle Irish /f" poison '; Latin venai. "vein' from *ueisna, cymr. gwyar^b\oo(y {*ueisaro)\ 
in addition Celtic FIN cymr. Gwy{*Ueisa), engl. Wear{abu{. *Uisuria), gall. Visera> French 
Vesere, Visuvia> French ia Vezouse etc.; Old Germanic FIN IV/sura^VMeser', Latin 
Visurgis 6s.: compare russ. FIN Veciira {to Soz), ablaut. V/ciiera {zur Kama); here the FIN 
i/Veic/isei {irom Old Prussian *Vfl<sia, older *VFsl<la, from Pre Baltic *l/?s//5 from *ueis-tla), 
Latin Vistuia {irom Germanic *WFstid\v\ Old English WFstiawudu, but Old English Wfsie 
from Slavic Visia); 

Note: 

the rhotacism n- > r-\r\ * ueisna, cymr. g\/i/yar'b\oo6' {*ueisaro) : Celtic FIN cymr. Gwy 
{*Ueisa), engl. Wear {abut. *Uisuria), gall. Visera> French Vesere: lllyrian llluria^ lllyria'. 

Old Icelandic veisai. "swamp, marsh'. Old English Old Frisian i/vase, engl. ooze "slime, 
mud'; perhaps Old High German weisunt, weisont, weisanf arteriae ' (the flowing); 
wherefore Old English wasend, engl. weasand' windpipe, gullet', further Old High German 
wisunt, -ant. Middle High German wisent. Old Icelandic visundr{* uis-onto) "Bisonochse' 
(from dem Germanic derives Latin bison, -ontisand gr. piacuv); in addition Old Prussian 
m's-samlbrs ^ Auerocbse' , Old Church Slavic zgJbrhds.; after dem smell, odor named, as 
also nisi, visia. Old High German wisuia. Old English weosule, wesle, engl. weasei 



'weasel' and litis 'polecat' (above S. 304), the Germanic *by/s(/)d "polecat' assumes; 
compare Vulgar Latin i//s5/o 'breaking wind, fart, fetidness '; Marstrander compares (Eriu 
5, 207) still nir. //'a/Trettchen' {*u/se/o-); 

Maybe alb. {*vikse) vithe^ buttock' common alb. -k > -th. 

perhaps moreover Indo Germanic £/7fcs-"Mistel and other leimliefernde tree ' in gr. \%6q, 
m. "Mistel, Vogelleim', Latin v/scum6s., Old High German wichsila. Middle High German 
wThser Weichsel^\xsc\\Q)\ russ. etc. visnja^ cherry' (out of it Latvian viksna. Old Prussian 
i47s/7ay/c»5"Kirschen') - Kirschgummi and Mistelbeere become as Vogelleim verwendet; 

Maybe alb. vishnja " cherry ' a Slavic loanword. 

after Specht (Indo Germanic Dekl. 206) in addition further Lithuanian i/z/rsi/^ "sedge' 
from *i//s-/r-Ka besides i//z^5 "grass'. Old Prussian wissene ^Porsc\\\ 

References: WP. I 234 f., WH. II 746, 800, 801 f., Vasmer 1, 208. 
Page(s):1134
```


## [2026-10-16T05:13:46.709Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(weis|wek|weik|weid)' AHD_watkins1985.txt | head; grep -n -i -E '^ *(weis-|wek-)' AHD_watkins1985.txt"
}
```


### [2026-10-16T05:13:47.052Z] TOOL RESULT

```
1136:weik-'
```


## [2026-10-16T05:13:49.322Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'VIRUS|WEASEL|OOZE|BISON|VISCOUS|weis|wek-' AHD_watkins1985.txt | head -30"
}
```


### [2026-10-16T05:13:49.632Z] TOOL RESULT

```
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1306:BISCUIT dwo-, pekw- BISHOP spek- BISHOPRIC reg-! BISON weis-
1983:00ZE2 weis-
2064:PARTERRE ters- PARTICIPATE kap- PARTRIDGE perd- PARTURIENT pere-1 PARURE pere-! PARVENU gWa-, pert PARVOVIRUS pau- Pas pete-
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
2455:VIRTUOSA wi-ro- VIRTUOSO Wi-ro- VIRUS weis-
2456:VISA weid- VISAGE weid- VISCID weis- VISCOUNT ei-1 vIscous weis- VISE wel-1 VISIGOTH weSs-pero- VISION weid- VISTA weid- VITAL gWei- VITAMIN gWei- VITELLUS wet-2 VITIATE wei-4 VITICULTURE wei-1 VITILIGO wel-4 VITTA wei-1 VITUPERATE wei-4 VIVA gWei- VIVACIOUS gWei- VIVERRINE wer-® VIVID g¥ei- VIVIFY dhé-1, gwel- VIVIPAROUS gWei- VIXEN puk-2 VOCABLE wekw- VOCAL wekw- VOCATION wekw- VOCIFERATE bher-1 VODKA wed-1 VOGUE wegh- VOICE wekw- VOID eu-2
```


## [2026-10-16T05:13:54.063Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in virus viscous viscid ooze weasel bison wisent; do echo \"== $w\"; grep -n -i -E \"^$w[,. ]\" KLN_1966.txt | head -5; done"
}
```


### [2026-10-16T05:13:54.396Z] TOOL RESULT

```
== virus
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== viscous
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== viscid
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== ooze
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== weasel
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== bison
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
== wisent
(eval):1: bad math expression: empty string
(eval):1: bad floating point constant
```


## [2026-10-16T05:13:56.430Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in virus viscous viscid ooze weasel bison wisent; do echo \"== $w\"; grep -n -i -E \"^${w}[,. ]\" KLN_1966.txt | head -5; done"
}
```


### [2026-10-16T05:13:57.133Z] TOOL RESULT

```
== virus
== viscous
== viscid
== ooze
26348:ooze,  n.,  1)  an  oozing;  2)  something  that  oozes; 3)  liquor  used  in  tanning  leather.  —  ME.  wose, wos,  fr.  OE.  wos,  ‘sap,  juice’,  rel.  to,  and  in-
== weasel
== bison
== wisent
```


## [2026-10-16T05:13:59.702Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"(^| )(virus|viscous|weasel|bison|wisent),\" KLN_1966.txt | head -20; sed -n 26345,26356p KLN_1966.txt"
}
```


### [2026-10-16T05:14:00.182Z] TOOL RESULT

```
5066:Derivative:  bishop,  tr.  and  intr.  v. bishopric,  n.  —  OE.  bisceoprice,  biscoprice,  com¬ pounded  of  bisceop,  biscop,  ‘bishop’,  and  rice ‘dominion’.  See  prec.  word  and  Reich, bismite,  n.,  bismuth  trioxide  (mineral.)  —  Coined fr.  next  word  and  subst.  suff.  -ite. bismuth,  n.,  name  of  a  metallic  element  (chem.)  — G.  Bismuth  (now  spelled  Wismut),  Latinized  by Georgius  Agricola  (in  1530)  into  bisemutum. The  origin  of  the  word  is  uncertain.  It  is  not connected  with  Arab,  ithmid,  ‘antimon’,  as  most lexicographers  would  have  it. bismuto-,  bismutho-,  combining  form  meaning ‘bismuth’.  —  See  prec.  word, bisnaga,  n.  a  kind  of  cactus.  —  Port,  bisnaga  (cp. Sp.  biznaga),  fr.  Arab,  bisndj,  secondary  form  of bastindj,  fr,  L .pastindca,  ‘parsnip’.  See  parsnip, bison,  n.,  wild  ox.  —  F.,  fr.  L.  bison,  fr.  OHG. wisunt  (MHG.,  G.  wisent),  which  is  rel.  to  OE. wesand,  ON.  visundr,  and  cogn.  with  OPruss. wis-sambrs,  ‘aurochs’,  and  with  L.  vissio, ‘stench’.  The  bison  is  named  after  the  peculiar odor  of  musk  emitted  by  it  during  the  rutting season.  See  weasel.
16333:glutinous,  adj.,  of  the  nature  of  glue,  sticky.  — L.  glutinosus,  ‘gluey,  viscous,  tenacious’,  fr. gluten,  gen.  gliitinis,  ‘glue’.  See  glue  and  -ous and  cp.  prec,  word.
20303:jiva,  n.,  life,  the  individual  soul,  vital  energy (Hinduism).  —  OI.  jivah,  ‘living,  alive’;  cogn. with  L.  virus,  OE.  cwicu,  ‘alive’,  Gk.  (lioc,  ‘life’. See  quick  and  cp.  words  there  referred  to.
24555:mucilage,  n.,  a  gelatinous  substance  found  in plants  (bot.)  —  F. ,  fr.  Late  L.  mucilago,  ‘a  moldy, musty  juice’,  fr.  L.  mucus.  See  mucus, mucilaginous,  adj.,  viscous,  sticky.  Formed with  suff.  -ous  fr.  Late  L.  mucilago,  gen.  -aginis. See  prec.  word.
34539:‘always’,  and  vivum,  neut.  of  virus,  ‘living’.  See semper-  and  vivacious.
oosphcrc,  n.,  an  unfertilized  egg  (hot.)  —  Com¬ pounded  of  oo-  and  Gk.  oyaipa,  ‘ball  globe’. See  sphere.
oospore,  n.,  a  fertilized  spore  (bot.)  —  Com¬ pounded  of  oo-  and  Gk.  axopa,  ‘a  sowing, seed'.  See  spore.
ootbeca,  n.,  a  case  containing  eggs  (zool.)  — ModL.  ootheca,  compounded  of  oo-  and  Gk. 8-fjx7),  ‘case’.  See  theca.
ooze,  n.,  1)  an  oozing;  2)  something  that  oozes; 3)  liquor  used  in  tanning  leather.  —  ME.  wose, wos,  fr.  OE.  wos,  ‘sap,  juice’,  rel.  to,  and  in-
ooze
opiate
fluenced  by,  OE.  wdse,  ‘soft  mud,  mire' ;  rel,  also to  OS.  waso,  ‘wet  ground,  mire',  ON.  veisa,  ‘pond of  stagnant  water’,  and  prob.  cogn.  with  OI. vifdm,  ‘poison’,  Gk.  to 5  (for  *Fta6;),  L.  virus (for  *visos),  ‘poison’.  See  virus.
Derivative:  ooze ,  intr.  v.,  to  flow  slowly,  drip, exude,  percolate;  tr.  v.,  to  emit  by  oozing, ooze,  n.,  soft  mud,  mire.  —  ME.  wose,  fr.  OE. wdse,  ‘soft  mud,  mire’,  rel.  to  OE.  wos,  ‘sap, juice’.  See  prec.  word.
oozy,  adj.,  gently  flowing.  —  Formed  with  adj. suff.  -y  fr.  ooze,  ‘an  oozing’.
Derivatives:  oozi-ly,  adv.,  oozi-ness,  n. oozy,  adj.,  muddy,  slimy.  —  ME.  wosie,  fr.  wore. See  ooze,  ‘soft  mud,  mire’,  and  adj.  suff.  -y. Derivatives:  oozi-ly,  adv.,  oozi-ness,  n. op-,  assimilated  form  of  ob-  before  p. opacity,  n.,  the  state  or  quality  of  being  opaque; something  opaque.  —  F.  opacite,  fr.  L.  opaci- tatem,  acc.  of  opacitas,  ‘shadiness’,  fr.  opacus. See  opaque  and  -ity.
opacous,  adj.,  opaque  {rare)  —  L.  opacus,  'shady, dark’.  See  opaque.  For  E.  -ous,  as  equivalent  to L.  -us,  see  -ous.
opah,  n.,  a  spotted,  brilliantly  colored  fish  of  the Atlantic  ( Lampris  gattatus)  —  W.  African  uba. opal,  n.,  a  gem  stone  of  iridescent  colors.  —  F. opale,  fr.  L.  opalus,  fr.  Gk.  inaXXiop,  fr.  OI. upalah  (masc.),  ‘stone,  gem’  [upald  (fern.),  ‘the upper  millstone’],  prob.  /-  form  of  uparah, ‘lower, later’,  which  is  compar.  of  upa,  ‘near,  under, up  to,  on’.  See  sub-.
```


## [2026-10-16T05:14:06.173Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{0,40}(virus|viscous|viscum|weasel),  ?(n|adj)\\..{0,600}\" KLN_1966.txt | head -8; awk 'BEGIN{RS=\"\\f\"} NR==1714/2+12+1 {print NR-1; print substr($0,1,300)}' KLN_1966.txt"
}
```


### [2026-10-16T05:14:10.671Z] TOOL RESULT

```
ugrep: error: error at position 119
m|weasel),  ?(n|adj)\.(?:[^\n\x80-\xbf][\x80-\xbf]*){0,600}
                              exceeds complexity limits___/


869
L.  transfor- matus,  pp.  of  transformdre.  See  prec.  word  and -ation.
Derivative:  transformation-al,  adj., transformative,  adj.  —  ML.  transformations,  fr. L.  transformatus,  pp.  of  transformdre.  See  trans¬ form  and  -ative.
transformism,  n.,  the  doctrine  of  the  transforma¬ t
```


## [2026-10-16T05:14:12.848Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"(virus|viscous|weasel|viscid),  (n|adj)\\.\" KLN_1966.txt | cut -c1-80; "
}
```


### [2026-10-16T05:14:13.541Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:14:17.016Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"virus|weasel|viscous\" KLN_1966.txt | cut -c1-120 | head -30"
}
```


### [2026-10-16T05:14:17.389Z] TOOL RESULT

```
2169:alfalfa,  n.,  lucerne.  —  Sp.,  fr.  Arab,  al-fasfasa  . (Cp.  the  collateral  Sp.  form  alfalfez,  which  rep
4973:bike,  n.  and  v.  —  Colloq.  abbreviation  of  bicycle, bikh,  bish,  n.,  aconite  poison  ( Anglo-Ind .)  — Hi
5066:Derivative:  bishop,  tr.  and  intr.  v. bishopric,  n.  —  OE.  bisceoprice,  biscoprice,  com¬ pounded  of  bisc
7415:Derivatives:  chime,  tr.  and  intr.  v.,  chim-er,  n. chime,  chimb,  n.,  rim  of  a  cask.  —  ME.  chimbe, fr
7861:ML.  clavicymbalum.  See  clavicembalo. Derivative:  clavecin-ist,  n. clavelization,  n.,  inoculation  with  shee
13569:ermine,  n.,  a  kind  of  weasel.  —  OF.  ermine  (F. hermine),  femin.  of  OF.  ermin,  hermin,  which prob.  
14433:‘the  pine  tree’,  nfcov,  ‘fat,  wealthy’,  map,  ‘fat, tallow’,  mixeXr),  ‘fat’,  Trtacra  (for  *irixia),  ‘p
14594:ferret,  n.,  a  small  animal  of  the  weasel  family.  — ME.  feret,  foret,  fr.  OF.  *fuiret,  *furet,  fr. 
15686:bot.)  —  L.,  ‘helmet’,  borrowed  fr.  Gk.  yaXsv], Att.  yaXrj,  ‘weasel,  polecat,  marten’.  The  phases of  
15687:1)  weasel;  2)  weasel’s  skin  or  hide;  3)  leather;
15708:Derivative:  galleri-ed,  adj. galley,  n.  —  ME.  galei,  galeie,  fr.  OF.  galie,  fr. ML.  galea,  fr.  Byzan
16268:L.  glires,  pi.  of  glis,  ‘dormouse’,  cogn.  with  OI. girih,  ‘mouse’,  Gk.  y aXit],  Att.  yocXrj,  ‘weasel
16333:glutinous,  adj.,  of  the  nature  of  glue,  sticky.  — L.  glutinosus,  ‘gluey,  viscous,  tenacious’,  fr. glu
16790:Derivatives:  grumble,  n.,  grumbl-er,  n.,  grumbl¬ ing,  adj.,  grumbl-ing-ly,  adv. grume,  n.,  a  clot  of  
18204:Huldah,  1)  fem.  PN.;  2)  in  the  Bible,  name  of  a prophetess.  —  Heb.  Hulddh,  lit.  ‘weasel’,  rel. to 
20303:jiva,  n.,  life,  the  individual  soul,  vital  energy (Hinduism).  —  OI.  jivah,  ‘living,  alive’;  cogn. wit
22079:loir,  n.,  a  species  of  dormouse.  —  F.,  fr.  VL.  gll- rem,  corresponding  to  L.  glirem,  acc.  of  glis
23004:marten,  n.,  a  kind  of  weasel.  —  ME.  martryn,  fr. MF.  martrine,  ‘marten  fur’,  fr.  OF.,  fem.  of mart
24555:mucilage,  n.,  a  gelatinous  substance  found  in plants  (bot.)  —  F. ,  fr.  Late  L.  mucilago,  ‘a  moldy, 
24763:Mustelidae,  n.,  pi.,  a  family  of  carnivorous  ani¬ mals  as  weasels,  badgers,  skunks.  —  ModL., formed  
24764:musteline,  adj.,  of,  or  pertaining  to,  the  family  of weasels.  —  Formed  with  suff.  -ine  fr.  L.  must
26351:fluenced  by,  OE.  wdse,  ‘soft  mud,  mire' ;  rel,  also to  OS.  waso,  ‘wet  ground,  mire',  ON.  veisa,  ‘p
28856:pine,  n.,  a  tree  of  the  genus  Pinus  (bot.)  —  ME., fr.  OE.  pin,  (in  ME.  fr.  F.  pin),  fr.  L.  pin
28946:pit-a-pat,  adv.,  palpitatingly;  n.,  the  sound  of something  going  pit-a-pat;  intr.  v.,  to  go  pit-a- pa
29381:pole,  n.,  either  of  the  extremities  of  the  axis  of  the sphere.  —  ME.,  fr.  OF.  pole  F.  pole),  fr.
31096:pus,  n.,  yellowish  matter  produced  by  an  infec¬ tion.  —  L.  pus,  ‘viscous  matter,  pus’,  rel.  to pute
31161:Derivative:  pylor-ic,  adj. pyo-,  before  a  vowel  py-,  combining  form  mean¬ ing  ‘pus’.  —  Gk.  Ttuo-,  TC
34539:‘always’,  and  vivum,  neut.  of  virus,  ‘living’.  See semper-  and  vivacious.
35239:simar,  n.,  a  loose  robe.  —  F.  si  mar  re,  fr.  It.  zi- marra,  dissimilated  fr.  Sp.  zamarra,  fr.  Ar
38188:tapu,  n.  —  A  var.  of  taboo, tar,  n.,  a  viscous  liquid.  —  ME.  terre,  fr.  OE. teoru,  teru,  rel.  to
```


## [2026-10-16T05:14:20.940Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; tail -c 400 KLN_1966.txt; echo; grep -n -E \"^(virus|viscous|weasel|viscid|viscum),? \" KLN_1971.txt | head; grep -n -E \"virus, n\\.|weasel, n\\.|viscous, adj\\.|viscid, adj\" KLN_1971.txt | cut -c1-100"
}
```


### [2026-10-16T05:14:21.248Z] TOOL RESULT

```
e  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
48371:virus (med.) — F. clavdisation, fr. claveUe , 
262734:virus, n., 1) venom; esp. of a snake; 2) an infec- 
262810:viscid, adj., sticky. — Late L. vise id us, fr. L. vis- 
262824:viscum and adj. suff. -ose. 
262845:viscous, adj., sticky. — Late L. viscosus. See vis- 
265597:weasel, n. — ME. wesel , wesele , fr. OE. wesle , rel. 
265848:viscum , ‘mistletoe; birdlime’. See Viscum and 
262734:virus, n., 1) venom; esp. of a snake; 2) an infec- 
262810:viscid, adj., sticky. — Late L. vise id us, fr. L. vis- 
262845:viscous, adj., sticky. — Late L. viscosus. See vis- 
265597:weasel, n. — ME. wesel , wesele , fr. OE. wesle , rel.
```


## [2026-10-16T05:14:23.883Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 262734,262760p KLN_1971.txt; echo ----; sed -n 262805,262850p KLN_1971.txt; echo ---; sed -n 265597,265612p KLN_1971.txt"
}
```


### [2026-10-16T05:14:24.262Z] TOOL RESULT

```
virus, n., 1) venom; esp. of a snake; 2) an infec- 
tive agent; 3) a harmful influence. — L. virus , 
‘poison’, for (see rho taci sm), fr. I.-E, base 

*weis-, ‘to melt away, rot’, whence also OI. 
vi$dm, ‘poison’, vifdh, ‘poisonous’, ve$ati , ‘melts 
away’, Avestic visk-, visha-, ‘poison’, vaeshah-, 
‘mold’, Gk. toe; (for *Fkj 6<;), ‘poison’, OIr. 
fi, ‘poison’, W. gwy, ‘fluid, water’, gwyar, 
‘blood’, possibly also L. viescere, ‘to fade, with- 
er’, Lith. vystu, ‘I wither’, ON. visna, OE. 
wisnian , weosnian, ‘to whither’. See wizen and cp. 
Viscum. Cp. also bikh. Cp. also ooze, n. 
vis, n., force. — L. vis, ‘strength, force, vigor’, fr. 
I.-E. base *wei~, ‘to be strong’, whence also OI. 
vayah, ‘vital force’, Gk. ‘strongly, 

violently’, fqnoc;, ‘strong’, prob. also L. violdre, 
‘to treat with violence’. Vis is prob. rel. to L. vir, 
‘man’. See virile and cp. vim, violate, virial, ultra 
vires, 

vis, viss, n.y a weight used in S. India and in 
Burma. — Tamil visai , ‘division’, from the base 
of OI. vihitah, ‘divided, distributed’, 
visa, n. — L. visa, fem. pp. of videre, ‘to see’. See 
vision and cp. vise. 
----
VISION 

visceri-, viscero-, combining form denoting the 
viscera. — See viscera. 

viscid, adj., sticky. — Late L. vise id us, fr. L. vis- 
cum, ‘mistletoe, birdlime’. See viscum and 1st 
-id. 

Derivatives: viscid-ity , n., viscid-ly, adv., viscid- 
ness, n. 

viscin, n., a sticky substance occurring in the 
berries of the mistletoe (chem.) — Formed with 
suff. -in fr. L. viscum , ‘mistletoe’. See Vis- 
cum. 

viscose, adj., viscous. — Late L. viscosus , ‘full of 
birdlime, sticky, viscous’, fr. L. viscum. See 
viscum and adj. suff. -ose. 

Derivative: viscose, n., a kind of cellulose used 
in making rayon. 

viscosity, n., stickiness. — ME. viscosite, fr. MF. 
(= F.) viscositi, fr. ML. viscositatem, acc. of 
viscositas, fr. L. viscosus. See prec. word and 

-ity. 

viscount, n. — ME. viscounte , fr. MF. viscomte, 
vicomte (F. vicomte), fr. OF., fr. ML. vicecomes, 
compounded of L. vice, ‘instead of’, and comes, 
‘a companion’. See vice, prep., and count, ‘title 
of nobility’ and cp. vidame. 
viscountcy, n. — Formed from prec. word with 
suff. -cy. 

viscountess, n. — Formed fr. viscount with 1st 
suff. -ess. Cp. F. vicomtesse. 
viscous, adj., sticky. — Late L. viscosus. See vis- 
cose and -ous. 

Derivatives: viscous-ly , adv., viscous-ness, n. 
Viscum, n., a genus of plants of the mistletoe fam- 
ily (bot.) — L. viscum , ‘mistletoe; birdlime’ 
---
weasel, n. — ME. wesel , wesele , fr. OE. wesle , rel. 
to ON. visla y Dan. vxsel , MDu. wesel, Du. 
wezel, OHG. wisula, MHG. wisele , G. Wiesel. 
These words are prob. diminutives formed fr. 
Teut. *His(j)£?-, ‘fitchew’, which is cogn. with L. 
vissio, ‘stench’. Accordingly weasel lit. means 
‘the malodorous animal’. L. visio and OE. 
wesle , etc., derive from the I.-E. imitative base 
*wis-, ‘to break wind’. Cp. OF. voisson , ‘fit- 
chew’, which comes fr. L. vissio, Cp. also bison, 
weather, n. — ME. weder , ‘storm’, fr. OE. weder y 
rel. to OS. wedar, ON. vedr, Swed. vdder , Dan. 
veir, OFris., MDu., Du, weder, OHG. wetar, 
MHG. we ter, G. Wetter , ‘storm, wind, weather’, 
and cogn. with OSlav. vitru , OPruss. wetro , 
‘wind’, Lith. vetra, ‘storm’, OSlav. vedro , ‘good
```


## [2026-10-16T05:14:29.978Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4973,4975p KLN_1966.txt | cut -c1-500; for n in 555 556 557 558 559 560 561; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1 {print \"=== LEAF\",n; print substr($0,1,200)}' BQT_v1_pages.txt; done"
}
```


### [2026-10-16T05:14:30.615Z] TOOL RESULT

```
bike,  n.  and  v.  —  Colloq.  abbreviation  of  bicycle, bikh,  bish,  n.,  aconite  poison  ( Anglo-Ind .)  — Hind.,  fr.  OI.  vifam,  ‘poison’,  which  is  cogn. with  Gk.  tot;  (for  *rino;),  L.  virus  (for  *  visos ), ‘poison’.  See  virus.
bilabial,  adj.,  formed  with  both  lips.  —  Lit.  ‘made with  both  lips’,  fr.  bi-  and  labial.
172
=== LEAF 555
- ۳۳ 7
یر دک بنتم رابع بر وزن نك بی »
بمعئی برژه انته ات صمفی‌باشف منتو, که‌بارزد
گوشش ٩‏ .
یرگ ؟ « بنتح اول و ثالث بر وزن
سنجق ؛ علم را گوشد - و یمعتی شقه جر مر
رنگین هم‌آعده است که برسر علم و نیزه و
=== LEAF 556
بیرونآحدن
بیرون آ هلان - سسروف است که
نفیض درون رفتن باشد- و کنابه از ترك اطاعت
وانقیاد هم هست.
یر ون‌سر | - بسکون نون » زری را
کون که درغر ضرابخانه سکه شده باشد .
لیر رن * بکسر اول و سکون ثانی
مجهول 
=== LEAF 557
پیمما --
لیستون ۱- نام کوهی است
مشپور که فرهاد بفرمودة شیرین آنرا
مبکند و کنابه ازآسمان هم هست؟ :.
۱ لیست و بات پیگر حور مالی
قلك‌البروح اک
یست و پا و شاق ".نی
قبت وت ی اسیت. که پیت بر رات
صورت باشد ا
=== LEAF 558
از "1 رن اه
لیشه » بر وزن ربشه جنگل و نستانرا
گونند و بعربی اجم خوانند؟ - وسازی هم‌هنت
از ني, که شبانان نوازند. و بسنی کوشد سازیست
شبه بچنگه » و بعضی دیگی گونند شبیه است
پرباب .
بیضه ] آشین «کنایدازآق
=== LEAF 559
۳۹۳6 سد
بیقاد ه بنتح اولبروزن نیزار , سرزنش
وطعنه باشد.
بیغاره بر وزن گهواره » بمعنی بیفار
ات که سرزش وطمنه باشد ٩‏ .
بیغال » بکر اول بر وزن فیفال »
بمعنی نیزه باشد که بعربی رمح خوانند .*#
بیگار ‌- با
=== LEAF 560
بنم ثانث مر وزث میگفت اه
ستارژ زهره را گوبند .
بیلقان ‏ بنتح اول و و
بر وزن نهروان ۰ شپرست از ولات اران مابین
شروان و آذربایجان؟ . ۱
پادشانعان - و قبالة خانه و باغ و امثال آنرا
کونند؟ - و تبربرا دز کن
=== LEAF 561
۳:۱
ماه است که بعربی شه ر گوبندا .
که مردمرا در حالت ماشفه دیده میشوده وآنرا
مربی ممایثه کوش
دریجهٌ خانه را گوند .
بیناساك .. بسکون سینو کاف, بمعنی
بیناس باشد که دربحهٌ خانه است ۰ رب بای فارسی
هم‌آحده
```


## [2026-10-16T05:14:35.460Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 557 558; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1 {print \"=== LEAF\",n; print}' BQT_v1_pages.txt; done | grep -n -E 'بیش|بیس|بش|زهر|aconit|vi|بیک' "
}
```


### [2026-10-16T05:14:36.471Z] TOOL RESULT

```
27:بر وزن شیفته ؛ بمعنی بیسر است که جانور
29:بشظرآهده است که عربان بقل عسگود .
50:لیشه » بر وزن ربشه جنگل و نستانرا
59:بیش بهاد -بتحبای
72:یش میباشد . کویند کوشت او تراق بش‌است
73:بمنی دقع ضور بیشءبکند واورا بعرمی‌فارةالبیش
85:۱ - پدین‌ممنی‌درپهلوی 065 «منای ۲۹٩‏ : ۲ *. در اوستا» ۷۷5/2 بمعنی‌زهر است .
86:در عفة حکیم مژمن آمده: «بیش: بهندی بش نامند» واوبیخی است مثبت او بلاد چین وکوهی .
87:که حلاهل نامند و لهذا زهر هلاعل عبارت ازوست » واوسرم نفوذتر ازسم افعیاست وقلیل اقسام
88:ار کمتر از دوساعت فانل است و در بلاد هند نیزاقام‌اومیباشد . » ۶ بشت ۲۷۵۱ ح* : معرب
89:آن نیز «یش» است «نفس » . - در اصطلاح احکام جوم بیش‌فارسی پممنی ترح وآفت عربی است.
```


## [2026-10-16T05:14:39.033Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==559 {print}' BQT_v1_pages.txt | sed -n 40,95p"
}
```


### [2026-10-16T05:14:40.061Z] TOOL RESULT

```
ار کمتر از دوساعت فانل است و در بلاد هند نیزاقام‌اومیباشد . » ۶ بشت ۲۷۵۱ ح* : معرب
آن نیز «یش» است «نفس » . - در اصطلاح احکام جوم بیش‌فارسی پممنی ترح وآفت عربی است.
< کاءشماری ص۳۳۷ ». ۴ اوستا ۷۵125198 (جنگل ) » سااسکرت ۷۳۴5۲18 (درخت)
«اسفا ۱: ۲ ص۸۸ ۰ پهلوی ۷151216 < بندهش 6۱۸۹ . سفدی ۷151021 «کوتبو ۱۱۸ » طبری
ما سرانی کنونی ۷1502 د« واژه نامه ۷۹۹ » اورامانی ۷۵58 « .اورامان ۱۲۷
۴ مصحف : بیفا. درعردی ببغاء بفتح‌اول‌وسکون دوم‌وفیز فتح اول ودوم‌مضفف رهم بفتح‌اول
ودوم مشدد». طوطی ست:
* یطار -بفتح اول, از بونانی ۳۳1۵/۳05] م رکب از1۳۳05 بممنی اسب و 180۳05
پزشك ( 134718 مداوا) ؛ جمماً بمعنی ستور پزخكو 1120184۳6 درفراضه بمعنی درمانکننده
اسپ‌از خمین ریده است «تفس». همرب‌آنهم بیطار وییطر بفتح و کسر اول (هردو) , رك : دائرة -
المعارف اسلام -
```


## [2026-10-16T05:14:51.065Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:338 --image 2>&1 | tail -80"
}
```


### [2026-10-16T05:14:52.408Z] TOOL RESULT

```
no scan of BQT covers printed page 338 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:14:58.609Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==559 {print}' BQT_v1_pages.txt | sed -n 1,40p"
}
```


### [2026-10-16T05:14:59.366Z] TOOL RESULT

```
از "1 رن اه
لیشه » بر وزن ربشه جنگل و نستانرا
گونند و بعربی اجم خوانند؟ - وسازی هم‌هنت
از ني, که شبانان نوازند. و بسنی کوشد سازیست
شبه بچنگه » و بعضی دیگی گونند شبیه است
پرباب .
بیضه ] آشین «کنایدازآقاب‌عالمتاب
و با انی معروف‌نلمبیخی است‌مهلك وکشنده ٩‏
شبیه بمله پروین ۰ کویند هر .
دو از یکجا روند .
بیش بهاد -بتحبای
ابجد و های پالف کشیده برای
فرشت زده » رستنیی باشد که
آنرا در کپلان حميشه جوان
خوانئد . ب رک آن از ب رکه
زتون بز رک تر است وپیوسته . . یش
صبز صباشد و حرگر خعك نمیشود و بر گه
نمی ربزد. ورنگرزان ب گآنرا بجپت رنگه‌سبز
کار برند » وآنرا بعربی حی‌العالم خوانشد,وبسنی
گویشد گیاهی است در حك شبیه باشنفن , آزا
حی‌العالم میگویند .
یش . هش - با میم بر وزن فیل
کوش » جانورست دانند موش و در زیر بوته
یش میباشد . کویند کوشت او تراق بش‌است
بمنی دقع ضور بیشءبکند واورا بعرمی‌فارةالبیش
خوانند .
یضهای ددلین و ینهای‌زری که
بیضجر خ کنابه از[ فتاب است.
بیضه دد آب » بینه‌ای تکههنوز
بچه درآن متکون شده باشد .
بیضه زد - ويضة زریی ۰ کنایه از
خورشمد عالم آراست 8
لیا" ه بفتح اول و سکون انی و غین
نخطه دار بالف کشیده ۰ نام مرغیست که از
هندوستان آورند و بعلوطی اشتهار دارد. وآنرا
طوطك یز کوبند .
۱ - پدین‌ممنی‌درپهلوی 065 «منای ۲۹٩‏ : ۲ *. در اوستا» ۷۷5/2 بمعنی‌زهر است .
در عفة حکیم مژمن آمده: «بیش: بهندی بش نامند» واوبیخی است مثبت او بلاد چین وکوهی .
که حلاهل نامند و لهذا زهر هلاعل عبارت ازوست » واوسرم نفوذتر ازسم افعیاست وقلیل اقسام
ار کمتر از دوساعت فانل است و در بلاد هند نیزاقام‌اومیباشد . » ۶ بشت ۲۷۵۱ ح* : معرب
```


## [2026-10-16T05:15:11.828Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^b[eē]š|^wiš|^wis|^was |^wasy|^wa[sš]n|^bas' PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-10-16T05:15:12.797Z] TOOL RESULT

```
PHD.txt:615:was [KBD < A kbyr; ws | = M, N bas] much, many, enough.
PHD.txt:628:wasyār [wsy(k)l | N bisyār] much, many.
PHD.txt:654:wistardan 92 wizürdan
PHD.txt:655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
PHD.txt:931:base bun, fragàn, payag.
PHD.txt:932:baseless abun.
PHD.txt:933:basil, royal — šāhesprahm; speckled ~ palangmušk.
PHD.txt:934:basin šādurwān; v. bowl.
PHD.txt:935:basis madayan, padisar.
PHD.txt:936:bastion frawar.
PHD.txt:3596:wisé kardan,
PHD.txt:3598:wisāndan,
PHD.txt:3742:bēšūmand, pimgén, zarigómand.
PHD.txt:4323:wisdom danagih, frazānagīh, xrad; innate ~ àsn-xrad.
PHD.txt:4324:wise dānāg, frazānag, xradēmand, zīrak.
PHD.txt:5130:wišomand nišāstan
PHD.txt:5131:wišād
PHD.txt:5135:wišād-dwārišnīh мехэухм ris ih, A T
PHD.txt:5136:wišādan nišēm nisémag nišēb nišēbīg wišūb- wišūbišnīg wišēbišn wišuftan wišūdan wišūdag wiškīdan wašag wiškin(n)- wiskof- wiškūfag wiškuftan wiškin(n)išn wiskar
PHD.txt:5213:wist
PHD.txt:5231:was wis
PHD.txt:5232:wasnid nixwiür- nixwārišn nahang, nihang wiyūz- wayūdagān wēn- (v. dīdan) жатап! wēnāgīh wēnāg winnār- winnārišn nēwardaxšīr winnārdan wēnāb wēnābdīg wēnābdāg niyūxš- niyoxsidan niyoxsián wénig
PHD.txt:5561:bas!
PHD_mackenzie.txt:1510:bastan. band- [ASLWN-tn < A -V 'sr; bstn',bnd- I M bstn, (bn-), P
PHD_mackenzie.txt:1515:bas [YHWWNII M b)f, N ,,-,] be! (imperative of biidan, q.v.)
PHD_mackenzie.txt:1516:baskuc [bfkwc] gryphon.
PHD_mackenzie.txt:1517:basn [bIni I = P] top, peak; stature; mane (v. bui).
PHD_mackenzie.txt:5229:was [KBD < A kbyr; ws I = 1'1, N bas] much, many, enough.
PHD_mackenzie.txt:5247:wasyar [wsy(k»ll N bisyiir] much, many.
PHD_mackenzie.txt:5412:wis [wys I = M] village.
```


## [2026-10-16T05:15:20.411Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,10}b[eē][sš][^a-z].{0,160}' PHD.txt | grep -v -E 'bēšag' | head -12; grep -n -E '^b[eē][sš]' PHD_mackenzie.txt | head"
}
```


### [2026-10-16T05:15:21.267Z] TOOL RESULT

```
32:t the scribes wrote r and / almost indis-
166:] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): des
256:ostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostil
256:= bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim
390:badig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hamb
414:c). jud-|-bēš [ywdt bys] harmless, antidote. ~-dadestan [-D YN A] disagreeable, opposing. ~-déw [-ŠD YA) anti-demonic. ---này [-> d] a fathom (6 ft.). jud-ristag [yzodt lystk
1582:ny; be — abesīhīdan,
2211:harmless abes, abéwizend, judbēš.
2232:heal bēšāz(ēn)-.
2233:ing (a.) bēšāz.
2234:ling (n.) bēšāz(ēn)išnīh.
2325:х; bear ~ bēš burdan.
1562:besaz(en)- [by.ez(yn)-, byfC)c6'n)- I M byez-] heal, cure.
1564:bes- burdar [byfbwlt)l] hostile.
1566:besomand [byewmnd] sorrowful.
6073:best pAhlom.                                bodily tanig.
6074:bestowal baxsisn.                           body kalbod, kirh, tan.
11195:bes, bis                       ~)             baxs-                       -..A\,)N \
11197:bes-                         -.AU-t\          baxt                           ,~\
11199:besomand               ., r6' t"'\)\V \       baxtan                         ,,~)
11203:besaz-           -~\                          pas[
11208:besazenisnih   AU~~,                          darhandarzbcdI   \¥'eu~",*~\
```


## [2026-10-16T05:15:23.936Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,300}ostility\\. bēš-, —i&n, v\\. bištan' PHD.txt | head -3; grep -n -o -E 'bištan.{0,120}' PHD.txt | head -3; sed -n 1555,1566p PHD_mackenzie.txt"
}
```


### [2026-10-16T05:15:25.108Z] TOOL RESULT

```
256:furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan
128:bištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add
256:bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-bu
256:bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [by
beliir [bylwll M bylwr, N biZiir] crystal.
beron [byZwn I M byrwn, N berun] outside.
                  '
bM [byf] pain, sorrow; hann, hostility.
  ...... burdan: bear hostility.
bM-, .....lin, v. blstan.
bMaz [byfC}z] healing, medicinal.
besaz(en)- [by.ez(yn)-, byfC)c6'n)- I M byez-] heal, cure.
  .....isnih: healing.
bes- burdar [byfbwlt)l] hostile.
bMidan [by/ytn'] = blitan.
besomand [byewmnd] sorrowful.
```


## [2026-10-16T05:15:34.674Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-16T05:15:34.683Z] TOOL RESULT

```

```


## [2026-10-16T05:15:41.570Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-16T05:15:42.075Z] TOOL RESULT

```
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
```


## [2026-10-16T05:15:44.911Z] AGENT

I'll archive and read pages via fetch_source.py, then grep the stored text.


## [2026-10-16T05:15:47.786Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weys-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wek-' 'https://en.wiktionary.org/wiki/بیش' 'https://en.wiktionary.org/wiki/بس' 'https://en.wiktionary.org/wiki/بسیار' 'https://en.wiktionary.org/wiki/بسنده' 'https://en.wiktionary.org/wiki/ویروس' 'https://en.wiktionary.org/wiki/virus' 'https://en.wiktionary.org/wiki/ἑκών' 'https://www.etymonline.com/word/virus' 'https://www.etymonline.com/word/viscous' 'https://www.etymonline.com/word/ooze' 'https://www.etymonline.com/word/weasel' 'https://www.etymonline.com/word/bison'; do python3 tools/fetch_source.py \"$u\" --note \"page 537, roots Weis/Wek: $u\" ; done"
}
```


### [2026-10-16T05:15:55.058Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2426a592cfe9e81.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/19d1100c927b4beb.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/23381f52fde6894b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae3aae3921fb02a0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0516546c72ef7690.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ed9e41affc0c10b6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/556265d31e2a2d0b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4ab82ab98c6be78f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e268f8ee9f4294a3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/767d94fad6b8f177.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ae71f83540a3d998.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3f2f256ea62698e3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f8570cd3996693e6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/789114fae702d56d.txt
```


## [2026-10-16T05:15:59.094Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -14 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'][:70],d['file'])\""
}
```


### [2026-10-16T05:15:59.741Z] TOOL RESULT

```
200 12858 https://en.wiktionary.org/wiki/بافتن data/verification/sources/web/a99d1a173da27456.txt
-1 39 https://www.etymonline.com/word/weasel data/verification/sources/web/f8570cd3996693e6.txt
-1 39 https://www.etymonline.com/word/bison data/verification/sources/web/789114fae702d56d.txt
200 13557 https://en.wiktionary.org/wiki/باران data/verification/sources/web/e6827b3b929efea0.txt
200 25319 https://en.wiktionary.org/wiki/wasp data/verification/sources/web/c6db3e67f7fc0a16.txt
200 23936 https://en.wiktionary.org/wiki/vespa data/verification/sources/web/b3fdeec23f646c0c.txt
-1 39 https://www.etymonline.com/word/vaseline data/verification/sources/web/b2cfd0452f5e51f4.txt
-1 39 https://www.etymonline.com/word/wobble data/verification/sources/web/ff98ccf6d6399bdb.txt
200 5603 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wódr data/verification/sources/web/3658df9147b80327.txt
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wŕ̥s data/verification/sources/web/fc16dc019ce898ea.txt
-1 39 https://en.wiktionary.org/wiki/وازلین data/verification/sources/web/c5a651edfcae6948.txt
-1 39 https://vajehyab.com/moein/وردیج data/verification/sources/web/a8fca35c986a1567.txt
200 562 https://vajehyab.com/moein/وازلین data/verification/sources/web/fdd510a3ba2312bd.txt
200 541 https://vajehyab.com/moein/پارگین data/verification/sources/web/55291544c6729363.txt
```


## [2026-10-16T05:16:03.859Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -F 'page 537' index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'][:80],d['file'])\"; for f in c2426a592cfe9e81 19d1100c927b4beb 23381f52fde6894b ae3aae3921fb02a0 0516546c72ef7690 ed9e41affc0c10b6 556265d31e2a2d0b 4ab82ab98c6be78f e268f8ee9f4294a3 767d94fad6b8f177 ae71f83540a3d998 3f2f256ea62698e3; do echo \"$f $(wc -c < $f.txt)\"; done"
}
```


### [2026-10-16T05:16:04.544Z] TOOL RESULT

```
200 6080 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weys- data/verification/sources/web/c2426a592cfe9e81.txt
-1 39 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wek- data/verification/sources/web/19d1100c927b4beb.txt
200 8978 https://en.wiktionary.org/wiki/بیش data/verification/sources/web/23381f52fde6894b.txt
200 27990 https://en.wiktionary.org/wiki/بس data/verification/sources/web/ae3aae3921fb02a0.txt
200 4618 https://en.wiktionary.org/wiki/بسیار data/verification/sources/web/0516546c72ef7690.txt
200 3393 https://en.wiktionary.org/wiki/بسنده data/verification/sources/web/ed9e41affc0c10b6.txt
200 3766 https://en.wiktionary.org/wiki/ویروس data/verification/sources/web/556265d31e2a2d0b.txt
200 68818 https://en.wiktionary.org/wiki/virus data/verification/sources/web/4ab82ab98c6be78f.txt
200 7725 https://en.wiktionary.org/wiki/ἑκών data/verification/sources/web/e268f8ee9f4294a3.txt
-1 39 https://www.etymonline.com/word/virus data/verification/sources/web/767d94fad6b8f177.txt
-1 39 https://www.etymonline.com/word/viscous data/verification/sources/web/ae71f83540a3d998.txt
-1 39 https://www.etymonline.com/word/ooze data/verification/sources/web/3f2f256ea62698e3.txt
-1 39 https://www.etymonline.com/word/weasel data/verification/sources/web/f8570cd3996693e6.txt
-1 39 https://www.etymonline.com/word/bison data/verification/sources/web/789114fae702d56d.txt
c2426a592cfe9e81 6615
19d1100c927b4beb 165
23381f52fde6894b 9690
ae3aae3921fb02a0 31864
0516546c72ef7690 5062
ed9e41affc0c10b6 3659
556265d31e2a2d0b 4018
4ab82ab98c6be78f 72603
e268f8ee9f4294a3 8829
767d94fad6b8f177 132
ae71f83540a3d998 134
3f2f256ea62698e3 131
```


## [2026-10-16T05:16:07.557Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n '/Etymology/,$p' c2426a592cfe9e81.txt | head -80; echo =====; sed -n '/Persian/,$p' 23381f52fde6894b.txt | head -60"
}
```


### [2026-10-16T05:16:08.178Z] TOOL RESULT

```
Exit code 1
 ↑ 5.0 5.1 Vladimir Orel ( 2003 ), “*waisō”, in A Handbook of Germanic Etymology ‎ [1] , Leiden, Boston: Brill , →ISBN , page 441 

 ^ Rix, Helmut , editor ( 2001 ), “ 2.*u̯ei̯s-¹ ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , page 672 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/weys-&oldid=93156581 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
 Proto-Indo-European ReRC-shaped roots 
 Proto-Indo-European homonymic roots 

 Hidden categories: Proto-Indo-European entries with more than one part of speech 
 Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 
 Avestan terms with redundant transliterations 

 This page was last edited on 30 September 2026, at 22:34.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ weys- 

 Add languages 

 Add topic(eval):1: ==== not found
```


## [2026-10-16T05:16:10.209Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -c 4500 c2426a592cfe9e81.txt; echo; echo =====; head -c 6000 23381f52fde6894b.txt"
}
```


### [2026-10-16T05:16:10.996Z] TOOL RESULT

```
Exit code 1
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weys-
FETCHED: 2026-10-16T05:15:48Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/weys- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/weys- - Wiktionary, the free dictionary 

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
 Root 

 1.2.1 
 Derived terms 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ weys- 

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

 *weys- [ 1 ] [ 2 ] [ 3 ] 

 to raise , increase 

 to produce , procreate 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *weys- (23 c, 0 e) 

 *wéys-ti ( athematic root present ) 
 Proto-Balto-Slavic: *wéištei 
 Latvian: viest ( “ to rear, raise, increase ” ) 

 Lithuanian: vei̇̃sti ( “ to breed, rear ” ) 

 *wéys-dʰh₁e-ti ( dʰh₁e-present ) [ 4 ] 
 Proto-Indo-Iranian: *wáyždʰHati 
 Proto-Iranian: *wáyždHati [ 4 ] 
 Avestan: 𐬬𐬋𐬌𐬲𐬛𐬀𐬝 ( vōiždat̰ , “ to raise ” ) 

 ⇒ *wéysdʰ-ti ~ *wisdʰ-én-ti ( athematic root present ) 
 Proto-Indo-Iranian: *wáyždᶻdʰi 
 Proto-Indo-Aryan: *wáyḍḍʰi 
 Sanskrit: वि॒ड्ढि ( viḍḍhí , “ to labour; to produce ” , 2sg.imp. ) 

 *wis-né-s-ti ~ *wis-n̥-s-én-ti ( nasal-infix ) [ 2 ] 
 Proto-Balto-Slavic: 
 Lithuanian: vi̇̀sti ( “ to multiply, breed ” ) 

 *wis-éh₁-ye-ti ( stative ) ?
 Proto-Italic: *wizēō ?
 > ? Latin: vireō ( “ to be green, verdant ” ) 

 *wí-weys-ti ( i-reduplicated athematic root present ) [ 3 ] 
 Proto-Indo-Iranian: *wíwayšti 
 Proto-Indo-Aryan: *wíwayṣṭi 
 Sanskrit: विवे॑ष्टि ( víveṣṭi , “ to labour; to produce ” ) 

 *woys-ó-s ( “ fruit, sprout ” ) 
 Proto-Albanian: *waiša 
 Albanian: vesh   m ( “ grape, wine grape ” ) 

 *wóys-eh₂ ( “ fruit, sprout ” ) 
 Proto-Balto-Slavic: *waišāˀ 
 Lithuanian: vai̇̃sius ( “ fruit ” ) 

 Old Prussian: wēisin ( “ fruit ” , acc.sg. ) 

 Proto-Slavic: *věxà ( “ straw bundle ” ) [ 5 ] 

 Proto-Germanic: *waisō ( “ sprout, stem ” ) [ 5 ] 
 Old English: wīse 

 Old Saxon: wisa 
 Middle Low German: wēse 
 Low German: Wees 

 ⇒ Old Saxon: wiska 
 Middle Low German: wische 
 Low German: Wisch 

 Old Dutch: 
 Middle Dutch: wēse ; wisch 

 Old High German: wīsa 
 Middle High German: wise 
 German: Wiese 

 Old Norse: vísir 
 Norwegian: veis 

 Root
 [ edit ] 

 *weys- [ 6 ] 

 to flow 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *weys- (flow) (17 c, 0 e) 

 *wisós 

 ? *weys- tleh₂ 
 → Proto-Slavic: *Visla 

 → Latin: Vistula 

 → Ancient Greek: Οὐιστούλα ( Ouistoúla ) 

 → ⇒ Old English: Wistlawudu 

 Unsorted formations 

 Proto-Celtic: *wēsarom 
 Welsh: gwyar 

 Proto-Germanic: *waisǭ 

 Proto-West Germanic: *waisund 

 Sanskrit: वेषति ( véṣati , “ to flow ” ) 

 Avestan: 𐬬𐬀𐬉𐬱𐬀𐬵 ( vaēšah , “ to decay ” ) 

 Tocharian B: wey- ( “ to steep ” ) 

 > ? Old Armenian: գէշ ( gēš ) 

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ 1. u̯eis- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 1133 

 ↑ 2.0 2.1 Rix, Helmut , e
(eval):1: ==== not found
```


## [2026-10-16T05:16:14.195Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 23381f52fde6894b 0516546c72ef7690 ed9e41affc0c10b6 556265d31e2a2d0b; do echo '-----' $f; sed -n '/From Wiktionary, the free dictionary/,/Retrieved from/p' $f.txt | grep -v '^\\s*$' | head -60; done"
}
```


### [2026-10-16T05:16:15.152Z] TOOL RESULT

```
----- 23381f52fde6894b
 From Wiktionary, the free dictionary
 See also: بيش 
 Brahui
 [ edit ] 
 Alternative forms
 [ edit ] 
 بھِیش ( bhīś ) 
 Etymology
 [ edit ] 
 Unknown. Compare Sanskrit वेसर ( vesara ) , वेशर ( veśara , “ mule ” ) .
 Noun
 [ edit ] 
 بِیش ( bīś ) 
 donkey 
 Derived terms
 [ edit ] 
 بِیشِی ( bīśī , “ donkey man ” ) 
 References
 [ edit ] 
 Bray, Denys ( 1934 ), “bīsh”, in The Brahui Language ‎ [1] , Calcutta, India: Superintendent Government Printing, Part II: The Brāhūī Problem; Part III: Etymological Vocabulary, page 75 
 Chagatai
 [ edit ] 
 Chagatai cardinal numbers 
  <  ۴ 
 ۵ 
 ۶  >  
     Cardinal  : بیش ( beş ) 
     Distributive  : بیشار ( byšʾr ) 
 Numeral
 [ edit ] 
 بیش • ( beş ) 
 five (5)
 Descendants
 [ edit ] 
 Ili Turki: besh 
 Uyghur: بەش ( besh ) 
 Uzbek: besh 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 From Middle Persian [script needed] ( wyš /⁠wēš⁠/ , “ more ” ) , probably borrowed from Avestan 𐬠𐬌𐬱 ( biš , “ twice ” ) , from 𐬛𐬀𐬌𐬠𐬌𐬙𐬌𐬌𐬀 ( da i bitiia ) . [ 1 ] [ 2 ] 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈbeːʃ/ 
 ( Dari, formal ) IPA ( key ) : [beːʃ] 
 ( Dari, formal ) IPA ( key ) : [beːʃ] 
 ( Kabuli ) IPA ( key ) : [beːʃ] 
 ( Hazaragi ) IPA ( key ) : [beːʃ] 
 ( Iran, formal ) IPA ( key ) : [biːʃ] 
 ( Tajik, formal ) IPA ( key ) : [beʃ] 
 Rhymes: -eːʃ 
 Readings
 Classical reading ? 
 bēš
 Dari reading ? 
 bēš
 Iranian reading ? 
 biš
 Tajik reading ? 
----- 0516546c72ef7690
 From Wiktionary, the free dictionary
 See also: تسيار 
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( wsy(k)ʾl /⁠wasyār⁠/ , “ much, many ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /bis.ˈjaːr/ 
 ( Dari, formal ) IPA ( key ) : [bɪs.jɑːɾ] 
 ( Dari, formal ) IPA ( key ) : [bɪs.jɑːɾ] 
 ( Kabuli ) IPA ( key ) : [bɪs.jɑːɾ] 
 ( Hazaragi ) IPA ( key ) : [bis.jɔːɾ] 
 ( Iran, formal ) IPA ( key ) : [bes.jɒːɹ] 
 ( Tajik, formal ) IPA ( key ) : [bis.jɔɾ] 
 Rhymes: -aːr 
 Readings
 Classical reading ? 
 bisyār
 Dari reading ? 
 bisyār
 Iranian reading ? 
 besyâr
 Tajik reading ? 
 bisyor
 Adjective
 [ edit ] 
 Dari
 بسیار 
 Iranian Persian
 خیلی 
 Tajik
 бисёр 
 بسیار • ( besyâr ) ( comparative بسیارتَر , superlative بسیارتَرین ) 
 many 
 Usage notes
 [ edit ] 
 The comparative and superlative forms بسیارتر ( besyâr-tar ) and بسیارترین ( besyâr-tarin ) are somewhat colloquial. More common alternatives are بیشتر ( bištar ) and بیشترین ( bištarin ) .
 Adverb
 [ edit ] 
 بسیار • ( besyâr ) 
 very 
 Synonym: خیلی ( xeyli ) 
 Related terms
 [ edit ] 
 بسیار خوب 
 بسیارخوب 
 References
 [ edit ] 
 MacKenzie, D. N. ( 1971 ), “wasyār”, in A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 88 
 Urdu
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian بسیار ( bisyâr , “ much, many, very ” ) , from Middle Persian [script needed] ( wsy(k)ʾl /⁠wasyār⁠/ , “ much, many ” ) .
 Pronunciation
 [ edit ] 
 ( Standard Urdu ) IPA ( key ) : /bɪs.jɑːɾ/ 
 Adjective
----- ed9e41affc0c10b6
 From Wiktionary, the free dictionary
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Persian بس ( bas ) 
 Proto-Indo-European *-onts der. 
 Middle Persian [script needed] ( -ntk' /⁠-andag⁠/ ) 
 Persian ـنده ( -ande/ande ) 
 Persian بسنده 
 From بس ( bas ) + ـنده ( -ande/ande ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ba.san.ˈda/ 
 ( Dari, formal ) IPA ( key ) : [bä.sän̪.d̪á] 
 ( Dari, formal ) IPA ( key ) : [bä.sän̪.d̪á] 
 ( Kabuli ) IPA ( key ) : [bä.sän̪.d̪á] 
 ( Hazaragi ) IPA ( key ) : [bä.sän̪.d̪á] 
 ( Iran, formal ) IPA ( key ) : [bæ.sæn̪.d̪é] 
 ( Tajik, formal ) IPA ( key ) : [bä.sän̪.d̪á] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 basanda
 Dari reading ? 
 basanda
 Iranian reading ? 
 basande
 Tajik reading ? 
 basanda
 Adjective
 [ edit ] 
 بسنده • ( basanda / basande ) ( Tajik spelling басанда ) 
 sufficient ; ( adverb ) enough 
 Derived terms
 [ edit ] 
 بسنده کردن ( basanda kardan  / basande kardan , “ to suffice, to make do with ” ) 
 Further reading
 [ edit ] 
 Hayyim, Sulayman ( 1934 ), “ بسنده ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=بسنده&oldid=92021657 "
----- 556265d31e2a2d0b
 From Wiktionary, the free dictionary
 Ottoman Turkish
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Italic *weizos 
 Latin vīrus lbor. 
 French virus bor. 
 Ottoman Turkish ویروس 
 Borrowed from French virus , a learned borrowing from Latin vīrus .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /viˈɾys/ 
 Noun
 [ edit ] 
 ویروس • ( virüs ) 
 ( pathology , microbiology , virology ) virus 
 Persian
 [ edit ] 
 Persian Wikipedia has an article on: ویروس 
 Wikipedia fa 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /wiː.ˈruːs/ 
 ( Dari, formal ) IPA ( key ) : [wiː.ɾúːs] 
 ( Dari, formal ) IPA ( key ) : [wiː.ɾúːs] 
 ( Kabuli ) IPA ( key ) : [wiː.ɾúːs] 
 ( Hazaragi ) IPA ( key ) : [wu.ɾús] 
 ( Iran, formal ) IPA ( key ) : [viː.ɹúːs] 
 ( Tajik, formal ) IPA ( key ) : [vi.ɾús] 
 Rhymes: -uːs 
 Readings
 Classical reading ? 
 wīrūs
 Dari reading ? 
 wīrūs
 Iranian reading ? 
 virus
 Tajik reading ? 
 virus
 Audio ( Iran ) : ( file ) 
 Noun
 [ edit ] 
 ویروس • ( virus ) 
 virus 
 virus (computing)
 Related terms
 [ edit ] 
 ویروسی ( virusi ) 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=ویروس&oldid=92999545 "
```


## [2026-10-16T05:16:17.891Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n '/^ Persian$/,/Retrieved from/p' 23381f52fde6894b.txt | grep -v '^\\s*$' | sed -n 40,90p; echo '-----'; sed -n '/^ Persian$/,/Retrieved from/p' ae3aae3921fb02a0.txt | grep -v '^\\s*$' | head -50"
}
```


### [2026-10-16T05:16:18.625Z] TOOL RESULT

```
 Etymology 2
 [ edit ] 
 From Middle Persian [script needed] ( byš /⁠bīš⁠/ , “ aconite ” ) , from Sanskrit विषा ( viṣā , “ Aconitum ferox ” ) , from विष ( viṣa , “ poison ” ) , whence English bikh .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈbiːʃ/ 
 ( Dari, formal ) IPA ( key ) : [biːʃ] 
 ( Dari, formal ) IPA ( key ) : [biːʃ] 
 ( Kabuli ) IPA ( key ) : [biːʃ] 
 ( Hazaragi ) IPA ( key ) : [biʃ] 
 ( Iran, formal ) IPA ( key ) : [biːʃ] 
 ( Tajik, formal ) IPA ( key ) : [biʃ] 
 Rhymes: -iːʃ 
 Readings
 Classical reading ? 
 bīš
 Dari reading ? 
 bīš
 Iranian reading ? 
 biš
 Tajik reading ? 
 biš
 Noun
 [ edit ] 
 بیش • ( bīš / biš ) ( Tajik spelling биш ) 
 aconite 
 Descendants
 [ edit ] 
 → Arabic: بِيش ( bīš ) 
 → Middle Armenian: բէշ ( bēš ) , բիշ ( biš ) , պէշ ( pēš ) , պիշ ( piš ) 
 Further reading
 [ edit ] 
 Ačaṙean, Hračʻeay ( 1971 ), “ բէշ ”, in Hayerēn armatakan baṙaran [ Armenian Etymological Dictionary ] (in Armenian), 2nd edition, a reprint of the original 1926–1935 seven-volume edition, volume I, Yerevan: University Press, pages 446–447 
 Laufer, Berthold ( 1919 ), Sino-Iranica: Chinese contributions to the history of civilization in ancient Iran, with special reference to the history of cultivated plants and products (Fieldiana, Anthropology; 15 ), volume 3, Chicago: University of Illinois Urbana-Champaign, page 582 
 MacKenzie, D. N. ( 1971 ), A concise Pahlavi dictionary , London, New York, Toronto: Oxford University Press, page 18 
 Palatecʻi, Gēorg Dpir ( 1829 ), “ պիյշ [ piyš ]”, in Baṙaran Parskerēn əst kargi haykakan aybubenicʻ [ Persian Dictionary in the Order of the Armenian Alphabet ] (in Armenian), Constantinople: Boghos Arabian Press, page 442b 
 Steingass, Francis Joseph ( 1892 ), “ بیش ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul, page 221 
 Torwali
 [ edit ] 
 Etymology
 [ edit ] 
 From Sanskrit वंशी ( vaṃśī , “ flute ” ) . Compare Hindi बाँसुरी ( bā̃surī ) .
 Noun
 [ edit ] 
 بیش ( bīš ) 
 flute 
 Urdu
 [ edit ] 
 Etymology
 [ edit ] 
 Borrowed from Classical Persian بیش ( bēš ) .
-----
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 From Middle Persian ws ( /⁠was⁠/ ) , from Proto-Iranian *was- ( “ to want, wish ” ) , from Proto-Indo-European *weḱ- ( “ to wish ” ) .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈbas/ 
 ( Dari, formal ) IPA ( key ) : [bäs] 
 ( Dari, formal ) IPA ( key ) : [bäs] 
 ( Kabuli ) IPA ( key ) : [bäs] 
 ( Hazaragi ) IPA ( key ) : [bäs] 
 ( Iran, formal ) IPA ( key ) : [bæs] 
 ( Tajik, formal ) IPA ( key ) : [bäs] 
 Rhymes: -as 
 Readings
 Classical reading ? 
 bas
 Dari reading ? 
 bas
 Iranian reading ? 
 bas
 Tajik reading ? 
 bas
 Adverb
 [ edit ] 
 بس • ( bas ) 
 enough , sufficiently 
 only 
 Determiner
 [ edit ] 
 بس • ( bas ) 
 many 
 Usage notes
 [ edit ] 
 Usually used in form of بسی ( basi ) .
 Derived terms
 [ edit ] 
 بسـ ( “ poly- ” ) 
 Interjection
 [ edit ] 
 بس • ( bas ) 
 enough 
 بسه! ― bas-e! ― Enough! 
 Descendants
 [ edit ] 
 → Azerbaijani: bəs 
 → Bengali: ব্যাস ( bês ) 
 → Gujarati: બસ ( bas ) 
 → Hindustani:
```


## [2026-10-16T05:16:22.036Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -o '.{0,120}aconit.{0,120}' PHD.txt PHD_mackenzie.txt | head; grep -n -i 'aconit' SIN.txt | head; grep -n -i -E 'b[iī]š|bish' SIN.txt | head"
}
```


### [2026-10-16T05:16:22.665Z] TOOL RESULT

```
1326:*  This  term  is  referred  (whether  correctly,  I  do  not  know)  to  Kcempferia pundurata  (Stuart,  Chinese  Materia  Medica,  p.  227).  Another  name  for  this plant  is  J|r  §£  jrj£  p'un-no  Su  (not  mou),  *buh-ha.  Now,  Ta  Mih  states  that  the Curcuma  growing  on  Hai-nan  is  ^  ^  j^E  P'un-no  Su,  while  that  growing  in  Kian-nan is  kian-hwan  (Curcuma  longa).  Kcempferia  belongs  to  the  same  order  as  Curcuma, — Scitamineae.  According  to  Ma  Ci  of  the  Sung,  this  plant  grows  in  Si-zuh  and  in all  districts  of  K  wan-nan;  it  is  poisonous,  and  the  people  of  the  West  first  test  it on  sheep :  if  these  refuse  to  eat  it,  it  is  discarded.  Chinese  p'un-no,  *buh-na,  looks  like a  transcription  of  Tibetan  bon-na,  which,  however,  applies  to  aconite.
1949:In  the  form  #  -?  fu-tse,  it  occurs  in  a  prescription  written  on  a wooden  tablet  of  the  Han  period,  found  in  Turkistan.7  Fu-tse  pft  -J"  is identified  with  Aconitum  fischeri,  cultivated  on  a  large  scale  in  Cah-min hien  in  the  prefecture  of  Lu-han,  Se-£'wan.8  It  is  not  known,  however, that  this  species  occurs  in  Persia.
1950:Yi  Tsih  calls  attention  to  the  fact  that  the  medicinal  herbs  of  India are  not  the  same  as  those  of  China,  and  enumerates  tubers  of  aconite together  with  fu-tse  among  the  best  drugs  of  China,  and  which  are  never found  in  India.9
3580:1  Such  an  example  I  have  given  in  T'&ung  Pao,  1915,  p.  319:  biS,  an  edible aconite,  does  not  occur  in  China,  as  stated  by  Damlrl,  but  in  India.  In  regard  to cubebs,  however,  Garcia  da  Orta  (C.  Markham,  Colloquies,  p.  169)  was  mis- taken in  denying  that  they  were  grown  in  China,  and  in  asserting  that  they  are called  kabab-£inl  only  because  they  are  brought  by  the  Chinese.  As  I  have shown  {ibid.,  pp.  282-288),  cubebs  were  cultivated  in  China  from  the  Sung  period onward.
4028:13(85).  bi$,  halakil,  aconite  (Aconitum).  Hindi  bis",  Skr.  visa  (Aconi- tum ferox),  from  visa,  "poison;"  Skr.  halahala,  a  species  of  aconite  and a  strong  poison  prepared  from  it.  Cf.  T'oung  Pao,  1915,  pp.  319-320, note.
4197:Aconite,  582.
4621:523,  553,  556. Jacobi,  569. al-Jafiki,  546. Jaguda,  aconite  of,  379;  black  salt  of,
5036:Europe  by,  294. Se-c'wan,  aconite  of,  379;  brassica  of,
5333:Aconitum  ferox  582
5334:Aconitum  fischeri  379
2347:teenth  century  positively  denies  the  occurrence  of  olives  in  China.1 Of  course,  this  Arabic  traveller  is  not  an  authority  on  Chinese  affairs: many  of  his  data  concerning  China  are  out  and  out  absurd.  He  may even  not  have  visited  China,  as  suggested  by  G.  Ferrand;  notwith- standing, he  may  be  right  in  this  particular  point.  Likewise  the  Arch- bishop of  Soltania,  who  wrote  about  1330,  states,  "There  groweth not  any  oil  olive  in  that  country."2
5061:Can  K'ien,  21 1;  viticulture  in,  221. Soleiman,  231,  232,  282,  407,  413,  553. Solinus,  486,  525. Soltania,  Archbishop  of,  419. Soubeiran,  J.  L.,  475. Soulie\  G.,  491,  520. Spain,  basil  brought  by  Arabs  to,  587;
```


## [2026-10-16T05:16:26.528Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==40 || NR==39 {print \"LEAF\",NR-1; print}' PHD_mackenzie.txt | grep -n -E '^b[iīeē]' | head -40"
}
```


### [2026-10-16T05:16:27.169Z] TOOL RESULT

```
12:biimig [b)myk ] brilliant, glorious.
27:biirag [b'lk I N -a] mount, horse.
31:biirestan [b'lst>n l ] patient, resigned.
33:biirig/k [b'lyk' 1 N barik (cf. tiirig)] thin, fine, subtle.
34:biir-Jiimag [b)ly)mk l I N -a] saddle-bag.
42:biistan [b)st)n I M b'yst'n, N ,,-,] always, often.
80:bedom [bytwm I M bydwm] furthermost.
81:beganag [byk)nk I N ......a] strange; stranger.
83:begar [byk)ll N .....] corvee, forced labour.
84:beh [byh I N bih] quince.
86:beliir [bylwll M bylwr, N biZiir] crystal.
87:beron [byZwn I M byrwn, N berun] outside.
93:besaz(en)- [by.ez(yn)-, byfC)c6'n)- I M byez-] heal, cure.
95:bes- burdar [byfbwlt)l] hostile.
97:besomand [byewmnd] sorrowful.
98:bewar [bywll M bywr, N,....,] myriad, ten thousand.
103:bim [bym I = M, N ,....,] fear, terror.
109:bis [byf IN .....] aconite.
```


## [2026-10-16T05:16:34.285Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo NYB; grep -n -E '^(b[iīeē][sš]|was|wasy|wiš|vas)' NYB_vol2_glossary.txt | head -20; echo HRN; grep -n -E '(^| )[0-9]+\\. *(bas|bisy|bīš|biš|basand)' HRN.txt | head; grep -n -E 'bisyār|basanda|basand' HRN.txt HUB.txt | head"
}
```


### [2026-10-16T05:16:35.091Z] TOOL RESULT

```
NYB
990:bēšāzišuēh det. v. n. of bēšāzišn healing: (yätuk) ~ gl. to biziskeh 44?. — Cf MPrs bys’zyn- ‘to heal? (A-H II)
991:beš-burtar [bys bwlt?l] grieved 681°, v. bes.
992:bēšēnītār [~-ynyt’l] causing pain, pain- ful, excruciating: ~ dart 43%.
993:bēšītan [byšytn'] to violate 73%. 831, 9824. — MPrs and Paz.
994:besömand [byš?"wmnd] grieved, afflicted 11%,
2147:vas-ic however much 46°-%, with apo- dosis introduced by adak-ic 81?2-4, by pas-ic 9112-318; (ka-š-ip 46° v. *kas); ka ne freftar hah: u man freftàr ... hah? while thou art not (otherwise) a deceiver, art thou (nevertheless) to deceive me? 3418-20. 798-9; 802-4, etc. — 4. conditional: if; real: ka-m han beton amävandeh
3557:besides, it
3990:vas
4001:vas [inscr. and Ps. KBYR, books KBD for KBYR; ws 7611] 1. adj. many, much, regularly placed before its subst.: ~ hir u zuästak 131; passim; ~ kas many a one 1514; ~ mat many a mother 22%; a non- personal subst. remains in sg. by analogy with the cardinals : ~ cig avd many wonder- ful things 319711; ~ säl many years 6%; ~
4004:vas
4007:vas-anākēh [ws’n’kyh] having, affording much harm 743.
4008:vasiha [KBYR-yh’] multifariously 10924.
4009:vasikär [wsyk'l 8615], vasiyär [wsy?l] numerous; much (= vas) 69. — NP bisydr; from vasty (v. vas), but the forms are not clear.
4010:vas-ö2 [KBYR "wc'] very powerful 962°, v. ož. — Renders Av. (240) aš.aojah-.
4011:vaspuhr [w’spwhl] belonging to the class of vispuhr (g.v.), i.e. the lawful heirs within the clan or family: [1. adj.: pus ~~ + šāhān farrax"tom (the son entitled to share the patrimony, foremost among the princes =) the crown prince, the heir to the throne SS 10.] — 2. subst. (royal) heir: ~ % Vistäspän the (foremost) heir of the Vistasp family 26”. 2719, of Frašāvart, the crown prince and co-regent (2217). — < *väispudri-, vrddhi derivative from *eispuÜra- (v. vispuhr), v. Bthl, WZKM 25, 1911, 251-254; in Babylonian cunei- form script 4-ma-su- (var. -as-) pe-it-ru-u = *wäspidri- < *wäspudri-, v. Eilers in Taqizadeh Vol., 1962, 55-63. The mean- ing and juridical purport of this term and its derivatives, as also of the basic w. vispuhr and its derivatives, have been
4018:vastarg [wstlg] clothes 41?-4-? [472° read vistarg]. — Av. (1385) vastra- ‘clothing’ ; inser. SM 1. 50 wstlg; Paz. vastarg, vastrg ; Mand. lw. bastirga.
4019:vastr [w’stl] pasture, (cattle) food 9411-14, — Borrowed from Av. (1414) västra-.
5426:vaströ.fSuyant-: vastri- yoš
6484:bes: !bes
6864:vaspuharga: vāspuhra- kān
HRN
```


## [2026-10-16T05:16:41.078Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4001,4006p NYB_vol2_glossary.txt | cut -c1-1500; grep -n -E 'bas |basī|bisyar|bisyār|bīš|bīsh' HRN.txt HUB.txt | head -20"
}
```


### [2026-10-16T05:16:41.621Z] TOOL RESULT

```
vas [inscr. and Ps. KBYR, books KBD for KBYR; ws 7611] 1. adj. many, much, regularly placed before its subst.: ~ hir u zuästak 131; passim; ~ kas many a one 1514; ~ mat many a mother 22%; a non- personal subst. remains in sg. by analogy with the cardinals : ~ cig avd many wonder- ful things 319711; ~ säl many years 6%; ~
[wlekrt’r] handicraftsman,
www .parsianjoman.org | ool wok
vas
frasang many parasangs 7%; ~ simén, ~ asp névak 1965; — with a personal subst.: —-än martöm (cas. obl.) 418, but also ~ frazänak martom (cas. obl.) 455; ~ āzātān u vazurgän (cas. obl.) 16°; ~-dn vazurg-spāsān (for cas. rect.) 1061; — less often placed after its subst. without or with the izGfat: névakéh ~ 351; anākēh ~ 95* (as against pat ~ andkéh 761); hesm i ~ 4815; gāvān + ~ 483-26; aspān i ~ 4013, — 2. as a pred.: numerous, great 41, 201? sq. 871; — in a compound: hesm ~ quick to anger 1074. — 3. subst. pl. cas. obl: 6 ~-dn to many people 3643 and passim. — 4. adv. very: ~ vazurg 8’; ~ pahréc 55°; — ka —-ic however much 463, 8122-23, 9112. — OP vasiy; MPrthPrs ws; Paz. vas; NP bas.
~ zarr,
HUB.txt:597:vabaSf pi. aubas ^GesindeF. — Auch Noldeke halt
HUB.txt:598:aubas fiir echt arabisch.
HUB.txt:983:vor. Daraus np. bis == bas h5chstens in Nr. 222: baskart
HUB.txt:4469:ap. ^vasi-ddra- zu bas Viel' = ap. vasiy (unter Mitwirkung
HUB.txt:4493:*VVelt'); bizisk Arzt' s. p. 128; bisyar Viel* ebenda.
HUB.txt:5458:= phi. varak^ skr. urana-; bas Viel* = paz. vas^ ap. vasiy;
HUB.txt:5459:bisyar Viel' =■ paz. vasydr Min. Gl. 210; banafsa 'Veilchen'
HUB.txt:7098:ap. *xsad^adara'\ bisyar Viel' = ap. *«?asi(T(!lra- ; -yod =
HUB.txt:9378:vra$, zd. baresa-, arm. bas 'Mahne* (13.— 14. Jhd.) und bars
HRN.txt:5566:aw. raopis (?) ; plilv. röpäs, röbas ; ai. löpa^d- (skr.
HRN.txt:5572:kurd. rüwi 'Fuchs'; oss. d. robas, t. rübas (215);
```


## [2026-10-16T05:16:46.457Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; pg(){ head -n $2 $1 | tr -cd '\\f' | wc -c; }; echo HUB5458 leaf $(pg HUB.txt 5458) ; echo HUB4469 leaf $(pg HUB.txt 4469); sed -n 4466,4471p HUB.txt; echo HRN; grep -n -E '\\b(bas|bisyār|bisyar|basanda)\\b' HRN.txt | head; grep -n -i -E 'vasiy|vašna|vas-' KNT_full.txt | head -20"
}
```


### [2026-10-16T05:16:47.024Z] TOOL RESULT

```
HUB5458 leaf 165
HUB4469 leaf 138
pieman (pazmdn^ puzmdn) *bereuend* aus paseman; hizisk
*Arzt*, arm. hzisk (aus^hizisk iuv ^bisizk), skr. bhisdj- 'Arzt'
(unter Mitwii^kung des i der ersten Silbe); hiayar Viel* =
ap. ^vasi-ddra- zu bas Viel' = ap. vasiy (unter Mitwirkung
des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
sassanid. Hormizd, arm. Ormizd^ ap. A(h)uramazdd; miyan
HRN
2037:np. ba^sis ist weithin entlehnt, schon arm. bas/is.
2282:kurd. eiiy. bei. LW. bas, bes.
1895:vasiy ‘at. will, greatly’, with s from Ё; but see 
5344:vasiy ‘at will, greatly’, with Med. s if loc. to a 
5597:pIE *uek- ‘wish’ + suffix -no-, OP vašna- ‘favor’! 
5636:vasaty rather than vasiy; see Lex. s.v. vasiy. 
7218:split of pAr. s into s and A (8115): stanam avas- 
7721:nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- 
8146:upon vat-: ar-uwant- in aruvas-ta-, sikaya "-want- in ` 
9800:k (vif- ‘house’, vas- ‘will’). 
9821:rüdiy, -padiy in ni-padiy, vasiy (but cf. Lex. s.v.) 
10034:Loc.: asnaty, dūraiy, vasiy, -katy; cf. conj. уату. 
10327:Sg. Nom. ava ava avas-ciy 
10329:Ace. отат ат ava avas-cry 
10395:avas-ciy, cis-cty. Abl. antyand developed like abl. 
12024:tion, as in DB 1.34f pasdva drauga dahyauvā vasiy 
12120:army which (was) in the palace’; XPa 13f vasiy 
12332:drauga dahyawd vasiy аата щй Parsaiy ша 
13025:DB 4.46f aniyašciy vasiy astiy karlam. 
13422:mary aniyascry vasiy astiy kartam ava ahydya 
13913:aniyaseiy vasiy astty kartam ‘much other (work) 
14597:DB 4.56 (and 4.75) utdtaiy taumā vasiy Муй ша
```


## [2026-10-16T05:16:49.687Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^ ?(vašna|vasiy|vas-)' KNT_full.txt | head; grep -n -E 'vasn|vašna' KNT_full.txt | head; sed -n 5590,5600p KNT_full.txt"
}
```


### [2026-10-16T05:16:50.310Z] TOOL RESULT

```
1895:vasiy ‘at. will, greatly’, with s from Ё; but see 
5344:vasiy ‘at will, greatly’, with Med. s if loc. to a 
28847:vasiy adv. ($191.TIT) ‘at will, greatly, utterly’; 
5597:pIE *uek- ‘wish’ + suffix -no-, OP vašna- ‘favor’! 
5619:{96.1 On Avestan -sn- [or expected -šn-, as in vasna 
7378:XPz 71, for vasnd + apiy. 
14451:seen in Аа 4 [vasnà : АМ: Analhtta |: ціа : 
14523:vam visam vasnd Auramazdahd akunavam I take aita as 
16591:11 уй :amahy — : бу : Dárayavaus : xSàyatiya : vasnd : Auramazd 
16603:18 yavaus : хёйуайуа : ima : dahydva : tyà : manā : patiyd@iSa : vasnà : Au 
16734:68 m : patiyübaram : vasnà : Auramazdáha : ima : adam : akunavam : adam : hamataxsaty : 
17115:3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 
17137:25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 

t nà-. 
pIE *jnu-lo-, OP zínula ‘satisfied’, Av. xínülo; 

medial -zšn- in the compound OP d-cSnautry 

‘he satisfies’. See Lex. s.vv. zínav-, urfnav-. 
pIE *uek- ‘wish’ + suffix -no-, OP vašna- ‘favor’! 

sec Lex. s.v. 
pil ghn in medial position is found in the $n of
```


## [2026-10-16T05:16:52.402Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28835,28860p KNT_full.txt; head -n 28847 KNT_full.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-10-16T05:16:52.989Z] TOOL RESULT

```
Gm. Werk, pIE *yerg-; in Artavardiya-. 


vardana- sb. ‘town’: Av. vorozona-, LAV. 
varazdna- ‘community’, Skt. wpjdna- ‘enclosed 
space’, pIE *urgeno- (830, 5147.1), to root *uerĝ-, 
Skt. yrj-, Gk. &pyo “Т enclose’ (discussion of etymol- 
ogy, with variant view, see Hall, Те. 12.297-9). 
vardanam nsn. DB 1.92; 2.9°, 22, 66, 95f; 3.5, 22, 
34, 51f; DSe 45f. 


vasiy adv. ($191.TIT) ‘at will, greatly, utterly’; 
as indecl. sb., ‘much’: Sas. РЫ. vas, NPers. bas; 
loc. of root-sb. vas- (§9.VI, §87, §142), to pIE 
root *yek-, GAv. vasomi ‘I wish’, Gk. (Cretan) 
реко» ‘willing’; unless properly vasaty (897), loc. 
of thematic stem vasa- (*yek-ske-, асе. to MB Gr. 
§114), from the present-tense stem of the same 
root. See also vaind. DB 1.34, 51, 89, 95; 2.26, 
36, 41, 46, 55, 61, 69, 98°; 3.7, 18, 39, 46, 63, 68; 
4.46, 56, 75; 5.25^; DNb 26f; DSe 31°, 43; XPa 
13; XPf 26, 37; XPg 3f; XV 19. 

vasddsaka, uncertain word in Se, probably а 
man's name (§168.VIT). 
0
```


## [2026-10-16T05:16:57.121Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^va[šs]n[aā]' KNT_full.txt; n=$(grep -n -E '^va[šs]n[aā] ' KNT_full.txt | head -1 | cut -d: -f1); sed -n \"$n,$((n+10))p\" KNT_full.txt"
}
```


### [2026-10-16T05:16:57.727Z] TOOL RESULT

```
Exit code 1
28863:vasna- sb. ‘will, favor’: Av. vasna-; deriv. 
sed: -e expression #1, char 1: unknown command: ','
```


## [2026-10-16T05:17:02.208Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28863,28870p KNT_full.txt; echo BST; grep -n -i -E 'vas|bas' BST.txt | sed -n 1,400p | awk -F: '{print}' | grep -i -E 'vas[iy]|vasn|bas\\b|vasyar|vasiy' | head"
}
```


### [2026-10-16T05:17:02.901Z] TOOL RESULT

```
vasna- sb. ‘will, favor’: Av. vasna-; deriv. 
(896, $147.T) of root vas- ‘wish’, see under vasiy 
(Mt. MSLP 17.8546; Hz. ApI 349.52; stem vaš- 
na- ace. to Bthl. AiW 1893 and MB Gr. $267, 
and not vasan- with Sen 5). vaina ism. AmH 7; 
AsH 10; DB 1.11, 18f, 18, 22, 26, 59f, 68, 70, 88, 
94°; 2.3°, 25, 35, 40, 45, 54, 60, 68, 86, 97; 3.6, 

BST
166:§ 1. The Iranian nation, so far asit reverenced Ahura Mazda as its God and Zarathushtra as His prophet, was once possessed of an extensive sacred literature similar to the Veda of the Indians—the Awesta (masc, or neut.). There has never been unanimity in Germany as to the gender of the name.! ‘The word comes to us from the Middle Persian which has no genders. The Pahlavi form is avistdk,? the Pazend avasid. Neriosangh reproducesit in Sanskrit by avisi@ as in avistavdk or avistdvdni, “ Awesta-speech.” The word can hardly be traced further back than the Sasanian era, Oppert is, however, of opinion that the word is already to be found in an inscription of the time of Darius in the form abastdm (Beh. IV, 64°), but the identification is at least doubtful. The word has been variously derived. The con- jecture of Professor Andreas, orally communicated, has most pro- bability on its side, namely, that Avistak or Avastak is to be traced back
238:Amesa Spenta (Haft Ameshaspends); 38, Yasht of the Asa Vahista (Ardabahisht); 4, of the Haurvatat (Khordad); 5, of the Ardvi Sara Andahita (Ardui sir band) ; 6, of the Dvaraasaéta (Khurshed) ; 7, of the Mdongha (Mah) ; 8, of the Tistrya (Tishtar, also called Tir); 9, of the Drvaspa (Drvasp, also called Gosh Yasht); 10, ofthe Mtthra (Mihir) ; 11 of the Sraoga (Srash Yasht, from the adhokht*); 11,a Srésh Yasht; 12, the Yasht of the Rasnu (Rashn) ; 13, of /ravasi (Fravardin) ; 14, «of Varethraghna (Bahiram); 15, of Varyin (generally cz called Ram Yasht); 16, of Razista Cista (generally called Din Yasht); 17, of Asi Vanguhi
434:The account given in the Dinkard is supplemented, it is true, by the less trustworthy accounts of the various Rivayets. They give in the case of all the Nasks not only the exact number of chapters, but, in the case of some, also the pre- and post-Alexandrine content. Thus it is said of the Nasks 7, 8, 9,10 and 11, which, before the invasion of Alexander, contained 50, 60, 60, 60, and 22 chapters, respectively,
705:_ Still fuller is the second account given in the fourth book of the Dinkard. King Vishtasp, after his campaign against Arjisp, had the scriptures of the Mazdayasna-religion collected. Dara, the son of Dara," gave orders that the whole of the Awesta, with its explanation, should be preserved in two copies, the one in the treasury, theother in the Archives. Valkhash (Vologeses), the son of Ashkan, organized the careful collection and transcription from original sources of the entire Awesta so far as it had descended pure to that time, all of it that had been preserved in Iran, handed down in writing or by oral tradition, in a fragmentary state since the invasion of Alexander. Ardashir, the son of Papak, invited Tansar to his court and had the ecattered original documents of the religion collected by him. He imparted canonical validity to his collection by proscribing as contrary to the religion all doctrines which did not proceed in this way direct from Tansar.? Ardashir’s son Shahpihr caused all the non-religious writings on astronomy, medicine, mathematics, and philosophy which were scattered in India, Greece and elsewhere to be collected and added tothe Awesta, and a correct copy of both writings to be deposited in the treasury. Under King Shahpihr, son of Atiharmazd, a tribunal was summoned to investigate the religious controversies in the land. Before this tribunal Adarpid submitted to the fire-ordeal (probably on behalf of the _Awesta as restored to its pureform by him). He fixed the numbering of the Nasks, and the king declared that from henceforth, now that the true religion stood visible before men’s eyes, he would no longer tolerate any false religion.
795:L. § 36. Danmesrerer’s Taeory.—The latest hypothesis’ of Dar- mesteter is much more radical than the view advanced above in § 33. According to him the entire body of the sacred writings, ifindeed the Achiimenian period possessed such, was lost after Alex- ander’s invasion of Persia and under Greek rule,* ‘he reformation . which began under King Vologeses I (§ 31) produced in reality an | entirely new book. As regards the subject-matter Darmesteter i distinguishes two strata, an ancient pre-Alexandrian and a modern post-Alexandrian stratum ; but not a single page of the old Awesta has been literally reproduced in the new.° The Gathas are a type of the second class, the law sections of the Vendidad proper are a type of the first. The Gathas were written in the. middle of the first century of our era, and, indeed, under the influence of Gnosticism.’ The idea of Vohu Mand, which plays the chief rdle in the Gathas, is probably borrowed from the School of Philo Judwus or employed in imitation of that School.®
1245:Guftash Jamasp ki: Hindtgan shahar buzurg hast, u sard hast u garm hast, u tar hast u khushk hast; dar u darakht hast; kih dasht sakht hast, kih niyaz hast, kih éshan zivishnash az barinj hast, u kih az shir-i g46 hast, kih az tokhmha khurand ; azshan, késh u dad u ravishn vas u hast pah nimah-i Atrmazd u hast pa nimah-i Ahriman jadiyash ashkara kunand; ukih mirand hast kih andar zamin nihan kunand, u hast 61 av afganand,u hast pah atash bi-sozand; u har kih nah ha-din 61 dizakh shavand. U Chinastan shaharha-i buzurg vasi zar, vas muskh, vas gohar, vas an-chish andar band kard Oi niz aman bar yak vinash estad band, u but paristand; kih mirand darvand hand.
1309:sal. Ashadvarin haftad u panj sal. Bahram Shavaran, khvanand Karmanshah, yazdah sal. Shakit Shadvaran® bist u yak salu panj mah. Varahrim Shakitan, kash Bahram-gor khvanand, bist u sih sil u dah mah. Shakit* Varahram panjdah sal u chahar mah. Piroz Shakitin bist u do sal. Lis® Pirdzin chahar sal. Kobad Pirdzin ava sal chihal dd. Jaimiasp Khamist chihal u haft sal u haft mah u haft réz. Atrmazd Khusrodan duviazdah sal. Khusrdb ‘Aiirmazdin, Avarvéz® shah si u haft sal. Kabad Khusrodb, kash Shirtyah khvanand, nuh sal. Ardashir, khiid vastar-i Kabadan, yak sal u panj mah. Shakit’ Shaharyar bist sal az an fraz na-panand, Oshin khid pah khid bah avasinand; pas pah dimand-i Tazigan avazirad varas az tukhmi héshm u pah andak ziir u zavar Iran shahar fraz girand si-sad u hasht@d u do sal u nuh mah u haft roz u chahar
1350:Barnabas Brisson® was the first to collect all records of antiquity relating to the Prophet. Thomas Hyde’ quotes the statements of Has- tern authors on Zoroaster. Adolf Rapp,® has again worked all these ancient records into a collection that is. well worth reading; andso is the collection of Arabic, Syriac, and other Kastern allusions to the prophet, edited, a few years ago, by R. Gottheil.®
1857:11 Ys. 34. 15 khshmaka khshathra ahiira ferashém vasna haithyén dao ahiim ‘ by
2020:‘The mere mention of the subject naturally brings at once before the mind the representation of the Lord God Ormazd on the Sassanian bas- reliefs, where the divinity is portrayed as mounted on a charger and presenting the crown to Ardashir. The figure is familiar to all Iranian students.! But this is not all. Inthe Chapter on the conversion of King Vishtaspa, in my ‘ Zoroaster’ (p. 65), I have given the traditional account of how three of the Amshaspands, or Archangels, came from heaven to the palace of the king as witnesses from Ormazd himself to
```


## [2026-10-16T05:17:06.117Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=249 && NR<=252 {print \"LEAF\",NR-1; print}' BST.txt | grep -n -i -E 'LEAF|vas|was|bas|wish|234' | head -20"
}
```


### [2026-10-16T05:17:06.671Z] TOOL RESULT

```
1:LEAF 248
4:This is a curious inscription. Firstly, because the common Pahlavi form for Mod. Pers. khuddi is khwatéi, modern khudéh occurs in Bukhéré and Tokharistén. Hormizd is again not especially the protector of chidren, the Frawashis, Mithra or Ardwistira Anéhita, and others give children according tothe Awesta. But I do not know how the curious words khwat(d)h and farsandén can be’ otherwise read and understood. Both seem to be dialectical (farsand instead of farzand as well as Arab. sausanjird, Mod. Pers. wig ‘needle’ and others). Or does farsand belong to the same stem as Mod. Pers, dimy ?
32:LEAF 249
46:2 adam pron. Ist pers. ‘1’ (Aw azem); acc, mam (Aw. mam), yathé mam kdma(h) @ha(h), {as my desire was,’ enclit. ma@tyamdm ‘that me not;’ gen. mané (Aw. mana, Mod. Pers. man), enclit. maty (Aw
47:LEAF 250
75:LEAF 251
76:�1 said,’ athaha(h) * he said,’ athaha(n) ‘they said.’ Passiv. pres. thahyd- mahy ‘we are called’ (with active ending), aorist. athahy ‘it was said’ (or perhaps athahya(h) imperf. with active ending). Inf. thastanaiy.
84:inally part. pret. from rt. mé@ and 4, 8 1, ah‘ to be,’ with genet. ‘be- long to’ (khshatram amdkham taum- dyG dha(h) ‘ the kingdom was ‘be- longing to our family’). Pres. ind, amty ‘I am’ (Aw. abmi, Mod. P. -am) ; ahy'* thou art’ (Aw. ahi) ; astiy ‘he is’ (Aw. asti, Mod. P. ast); amahy ‘ we are’ (Aw. mahi); ha(n)- tiy ‘they are’ (Aw. henti, Mod. P.and); con}. ahatiy * he may be’ (Aw. Gath, anhait?) ; imperf, indic, dham ‘ I was ’ (Skr. dsam) ; dha(h) ‘ he was’; dha(n) ‘ they were’ Skr. dsan) ; middle dha(n)td ‘ they were.’
85:* taumd-, sb, f. perhaps tau(h)md, Aw. taokhman, Mod. P, tukhm; ‘race, family,’ nom.sg. .-d: yded taumd ahutiy ‘as long as race (i.e, man- kind) is (i.¢., exists), wtdtaiy t. md biyd(h) ‘thou mayest not have posterity’; gen. -dyd (Aw. -aydo, Skr. -dy@); VIIL. mand t. ‘the eighth of my family,’ Ka(n)bu/ji- ya(h) amdkham t. * K, of our family,’ khshatram amakham t. dha(h) * the kingdom belonged to our family,’ amikham t, kasheiy ‘any one of oar f.,’ Khshathrita(h) (H)uvakhshatra- hyd t.* Kh. of H's f.’; abl. -dyd(A) (Aw, -aydt) : khshatram tya(h)- hacd amdkham tawndya(h)  pardbriam aha(h) ‘the kingdom that was taken away from our family.’ da
86:234 PAUL HORN,
```


## [2026-10-16T05:17:10.830Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=251 && NR<=253 {print \"LEAF\",NR-1; print}' BST.txt | grep -o -i -E '.{0,200}vas(iy|na|nd|n[aā]).{0,300}' | head -5"
}
```


### [2026-10-16T05:17:14.106Z] TOOL RESULT

```
ugrep: error: error at position 116
|a|\xc4[\x80\x81]))(?:[^\n\x80-\xbf][\x80-\xbf]*){0,300}
                           exceeds complexity limits___/
```


## [2026-10-16T05:17:17.641Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=250 && NR<=253 {print \"LEAF\",NR-1; print}' BST.txt | python3 -c \"\nimport sys,re\nt=sys.stdin.read()\nfor m in re.finditer(r'vas',t): print(repr(t[max(0,m.start()-200):m.start()+300]));print()\n\" | head -30"
}
```


### [2026-10-16T05:17:18.262Z] TOOL RESULT

```
'yd-nd (mand ddtd) ‘whatever my laws (were)’ with shortened @ as in avadashim, etc.\n2 paruvam adverb ~ ‘ before,’ paruvamciy ; Aw. pourva. —\n> duvitdtrnam adv. ‘of old,’ cp. Lat, diuturnus (W. Foy).\n* vashna-, sb. m, ‘ wish, grace ’; instr, sg. -4‘ by thegrace (of Ahura- mazda)’; Aw. vasna,\n5 khshtra-, sb. n, nom, acc, sg. ‘rule, kingdom’; Aw. khshathra, Mod. P. shahr ‘country’ (older), * city.’ khshatrapdvan-, sb, M,, nom. sg. -4 ‘satrap’; from khshatra and. rt. pd * protect,’ Mi\n \n° bar verb ‘b'

' paruvam adverb ~ ‘ before,’ paruvamciy ; Aw. pourva. —\n> duvitdtrnam adv. ‘of old,’ cp. Lat, diuturnus (W. Foy).\n* vashna-, sb. m, ‘ wish, grace ’; instr, sg. -4‘ by thegrace (of Ahura- mazda)’; Aw. vasna,\n5 khshtra-, sb. n, nom, acc, sg. ‘rule, kingdom’; Aw. khshathra, Mod. P. shahr ‘country’ (older), * city.’ khshatrapdvan-, sb, M,, nom. sg. -4 ‘satrap’; from khshatra and. rt. pd * protect,’ Mi\n \n° bar verb ‘bear, ¢éarty,’ Aw, tt. bar, Mod. P. baram; imperf. act. abaram avam (h)ubrtam ‘1 bore'
```


## [2026-10-16T05:17:38.732Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /vashna-, sb/ {print NR-1; print substr($0, length($0)-200)}' BST.txt | head; echo; echo BRT; grep -n -E \"vaēš|vaes|vīš|viš-|visa-|vasəmi|vasami|usant|vasah|vasnah\" BRT.txt | head -30"
}
```


### [2026-10-16T05:17:39.337Z] TOOL RESULT

```
252
a(n) : ima dahydva(h) tyand mand data ap-‘ these countries followed my laws,’ i.e., ‘they submitted to my laws’ (Bartholome reads a(h)apa- riydya(n) ‘they respected’ and compares Skr. saparydt:), perha

BRT
3294:mazd  ao'  /ramar?zaiti  *saste.mazö  a<i° antan  urvaitya  (sd.)  fradd^aiti  V.  4.3; 3f.*,  N.  7/,  Vd.  20;  —  caiwlrö  «6°  ahu- tum  vairim  fiasrsvayäit  V.i8.i,y,  —  us paili  an'  histaiti  . .  iistryd  . .  us  ao'  ÄtstJt satavaesö  Yt  1^.32;  23;  —  *uzdän»m  hl .  rto"    ktrinaot  V.  6.50;  /J.30.  2)    an-
3335:•  g.  a-dvaesah-  Adj.:  s.  unter  tf/^flS«^-.
3571:.  .  avat  "apayaU^'*  nama    ahmi  yat   «ra    0  dem  Ort  nach  'der  hintere':  'rat  h, dama'apayemi    "Einholer    heisse    ich   .  .,  urvaesnt  fratarjm    urfaes^m    Vyt.2^;  — weil  ich  .  .  einhole"  Yt./5.43.  1  °raya  (LS.)  paiH  *mastrr/nya  ..paourvya
4524:•  '}.  an-usant'  Adj.  (fem,  •saitt-)  'der (etwas)  nicht  (tun)  will,  widerwillig,  ohne CS  zu  wollen':  ndit  mam  vTspe  yazatat>hs •Sf/ttfm  fraerscinta  "nicht  mich  gegen meinenWillen.."Yt  i7. 19;  19;  —  v?r3zyjt usaitica  *°ja(//Vfl(NSf.)''"..  mag  sie  wollen oder  nicht"  N.  6\  —  virszylt  usaiti  (sd.) neu  *'saili'^  N.ö;  — yat  ■j^(NS.)  vi/yei- tii'aisA.)..  M.S.  a6.  a)  "jiJNSm.  alsAdv.J» 'widerwillig':  'sS..  avat  kvar»  ätäpaite{i^) •tJ  h-tu  ma  °s5  ave  stärB  V.9.41;  — frä ahmät  parö  vlspe  daiva  'SS  tarsta  mmanle Y.  57. 18.  o)  sva,  'mit  Gewalt':  vaim>m (sd.)  's5  pai'iy3ife^.4.i,^;  53.
4535:•  j.  an-uso  Adv.:  s.  anusant-,
5982:i)  'treiben,  wegtreiben,  wegschleppen' (Vieh   und  Gefangene   als   Kriegsbeute): jvU  gqm  *vani(rm  (sd.)  aznUe'W.  S-Zl ', —   ' ya  {gäu^  varÄa  (sd.)  azimna  (Pass.)  Yt.  . ;o.86;    —    kaoa    nS  fraourvaesayälti  . drujö  vaismmda  a z;/ mn a m  (APm.)  "wann wird  er  uns,   die  zur  Wohnung  der  Dr.  ,  j.^  g,  azan-  :  asn-'^  n.  'Tag',  im  Gegens. hinweggetriebenen  (Rinder)  . ."  Yt/o.86;,2ur  Nacht:  pat/i  'sai paiti  xsa/ne  Yt./.g,
7619:PPM,  lum  V.  vaes:  —  Pü.:  afa/IriiriTA.
7711:•  }.  »rszaurvaesa-  m.  Name  des  zweiten Abschnitts  der  ersten  Hälfte  der  Nacht*'; 'Sät  F.  27  b.
7957:1 1 ;  —  D  °mä  dahyävc^  tyil  kacärnJ'  hami- ' ^'^/^'J  abaia":  p^rsa^..'Bh.2.2;  1.6,  D.5.2, 6.3;  —  'm?m  Hwam  xstäm  yju>m  .  . jairiyemi  ..:  paurva  tiiyüm  . .  bütriyBimatoe Y.5.21.  a)  auf  eine  erläuternde  oder ergänzende  nominale  Beifügung,  a)  sut>- Stativisch;  dassmü  yat  ahmt  ,  .  i'a^rvdasS imat:  vIiivaestv3{sA.)  YtJ.8;  —  in  Kon- gruenz mit  dem  Praedikat:  'tnftn  'hwqm paoirlin  yiin?m  .  .  jatoyemi  .  .:  vahishm aküm  Y.5.19.  b) adjektivisch, bei rela- tivischem  Anschluss:  'mat  äama  yat  ahu- rahe  V.  ig.  14,  17,  34,  Vyt.  20;  —  avi °mqnt  tanUm  yqm  masylnqm  V.  20.  3, 5.  3)  auf  ein  Relativum  als  dessen Korrelat,  a)  adjektivisch :  'ine  vaca  framrva yöi  hmti  gä^ilkva  bisämrüta  V.  10.  2;  2;
8518:•  j.  'usant-  Adj.  (fem.  °saiti-),  PPA.:  s. vas-.
8520:•  j,  *usant-  Adj.  (fem.  °saiti-),  PPA.:  s. 'vah:
9068:75.44;  —  tJm  ahmakäis  azdibiscä  "tänäiscä  I  a)  °vaUi  häitis  (sd.)''  Y.^J  Überschr.;  — yazamaidg'^.^'.^;  —  nöit  astS  ttiS'it  'tänahl\  -vaitim  häitlm  {&A^^^ yazamaide  \ .  43. 17; Hnmata\.i2.y,  —  vi . .  wvaesayäl  astaca  a.4Ö;  —  'vatlyä  vü  . .  Aälsis  {sA.)'>  Aan- 'tänaca  (APn.)  P.2/;  —  Stars  handaiaiti\dsta'^.  102''.  b)  'Taitlm  g.l'^qm  (sd.)" ^asia  "tämm^a  V.5.9;— «(X^  asWa  nBit . .  .  yazamaide  V.46.2Q;  yi. 16,  Vr.  i'.  8, 'i-irumca  {HSn.)  nBit  inoaasea  *vT.ur7'lsyät  iX.o,  H.2.8;  —  'raitya  gu^aya  (sd.)" V,  it).  T,  —  vlspii  gafiäs.'a  tanvas'a  .Aandäiä  yazamaide  \.4b,xo;  A.  2.  i,  V. azd:>hls(a  'tänqsca  kglirpasca  tnnsista  dat>- ■  iff-^S,  Vr. /.6,  jS'.y,  *N. /02. oas^a  unMlTumt'a  fravasim:a  pairica  dadj- ,  "  !*■  ■■  V.  43-  —  "  D-  i-  Y.  43-^- mahl  .  .  V.  jy  1 ;  —  "/iPit  ynysi  'täna"  ■  •  j.  usta.x''araiiah-  m.  Name  eines  Bergs Nik.2.  \u<liina    \. 43.16:    s.  zu   Ufiä-'odeTGthiTgs'.a/imatha/trgamyti/rai'xsy-m
10164:-  gavaestryavarStaara-  510
10830:mag" Y._j/.  19;  —  vasaha  ahi  xsayamna (NSf.)  lanuye  ifarmanke  ^daitim  (sd.) YL/7.15.         I,  2  a)  'mit  Gen.  und  Infi
11693:•  j.  ^yä-'>,  p.  _;t)'J-»>  £  'Sehne';  a)  im Fleisch  (nur  Komp.).  b)  des  Bogens: yat..'yä{^.)  navi^yan  (sd.)  Yt/0.ii3i —  as(i  yS  gavasnahe  (sd.)  snäuya  -ya (NS.)  Yt70.  laS.
12698:Komp. :  JoiiikaD'  +  urv°,  statt  daiohuurv gescfar.;  %.  »u  tmaurvaesa-,  —  Pü.;  dek  vaitär, ed.:  otret  1  esletätak.  —  >)  Im  Gegensatz  zu fiairiJJ^cm-  (sd.).  Vgl.  Dk.  9.  6.  2,  utdaiihav- nnd  unter  haxteü.
13723:•  j.  dürae-urvaesa-"  i)  Adj.  'des  Wende fem  liegt',  vom  Weg:  °s)m  paili  pantqm Vt.i.35.  2)m. 'ferne  (Weges)wende':(7fl/ ti  narqm  fravaz>nti  'i»m  ",  .  zur  fernen Wegeswende"  Vt.  (J.  58.
15653:•  j.  paouru.{raourvaesa-  Adj.  (fem.  °sa-) 'mit  vielen  Ausläufern':  harqm  btrszaitim 'sam  Yt72.  23.
16279:•  j.  pouru.fraourvaesya-"  Adj.  (fem  °y3-) av^paouru/raourvaisa-:  haram  hnzaitim •syqm^''  Yt. /O.  50.
19421:—  a%a  ml  zae'kra  lyänte  ..  ti.6S;  — äaj  mg  tum  . .  Ausk>m  pflum  ra^aya  Yt 5.77;  V.2.4^,  Y.io,  iz;  —  aal  ml  afm paityaexta  Y.g.  2,  V.  2.  3;  —  nüit  tng  apam ährava . .  daiähava  äir3J{sd.)  Y.ff.  24;  — ma  ml  jamyäi  akäi  aSs  Y.  59. 31 ;  Yt.5. 92,93,  V. /().  6;  —  US  ml  pita  kaomäi dra&ns  frSrsnaot  Y,  //,  4 ;  V,  iÄ  i  g ;  —  upa ml  srayamtha  vasahe  Yt  iT-2\;  — pairi ml  tümHt  daya  . .  Y.ii.io;  Ytl.S,  12.1, F.  ^  d,  Vd.  20;  —  jasa  ml  avatthe  Y.  ■]2. 9 ;  Ny.  /.  1 8 ;  —  däyä  m  l  atarl. .  afä'hrsm Y.ö'2. 4;  GS.$';  —  dazäi  mi . .  yai  .. Ytp.  4;  V,  2.  3;  —  Aaema  \dazdi  ml  .  . Y.  iO.  9';  —  üaita  ml yaozdäilTm  V.  & roo;  —  dalva  ml.,  aostm  kqmp>nstnie V./p.3;  —  ulia  ml  .  .  VtÄag;  23;  — vaxhm  miasqsa/..  V./5.15;  Yt77.ao, Az.i,  Vyti; —  havatahum  ml  buyalaY. 7/,  11;  —  mo!u  ml  Java  avaoke  \nur3m ml  bara  upasiqm  Ytj.Ös.  zu  1  a): As  ba  ml  aetaäqm  arinam  paotryl  "V .  18. 34;  —  yasca  ml  .  .  imä  namSnTs  . .  Yt '■  16;  3-  9,  "i  P-  '»;  —  ^«"S'  »r  ml  nsit da&Ti  upasiqm  . .  Yty.  la;  —  mä  &' ml  änhqm  zao%ranqm  frattuharät . .  Yt 10.  \22\  17.54;  —  3  tu  ml  aOayä  zatf- ^rayä  frattAarSil  YL5.  91.  zu  3}: ydha  yaf  ml  sahayeht  H.a.  11;  —  avat äyaphm  dazdi  ml  Yt  5.  iS,  15.  5,  17.2$;
19822:maitiivasah-  1134
19904:•  j.  mainyav-asah-  Adj.:  s.  unter  matni- vasah:
21108:•  p.  ya'diy,  j.  ye8i'>,  yei8i'>  Konjn. I)  II  zeitlich 'zu  der  Zeit  als' ;  viyaxnakya\  3.-ai\i\\X, mähyn  14  raucabii  'kakaiä  äka'  y  uda- patatä  Bh./.  II.  II)  bedingend  'wenn, sofern';  i)  mit  (fiitur.)  Konj.,  a)  vor  dem Hauptsatz:  II  y  kürj'  pärsj'  patc^  aha- tty ..  siyätis  .  .  nirasstiy  .  ■  D.  5. 3;  — y  av(^a  *maniyähay  .  .  imam  pärsatn käram  pädiy  D.  5. 3;  —  y  imäm  dipim vainaAy  . .  uta  parikarähidil  J'urJ'mazda %uv3m  daufta  blyä^Bh. 4.  16;  17,10,11;! —  *(^(  sL.aSe  vacS  ustime  urvaese  gayehe /ramrai'3i{aS.)  pairt  te  tanava . .  urvamm . . Y.  7/.  ig;  —  im  Nachsatz  steht  «Sa:  °i%i zT  kvari  nUii  uzuxsyeiti  aha  datva  vTsph minnänta  "wenn  (einmal)  die  Sonne  nicht aufgehen  wird,  dann  werden  die  D.  alles zu  nichte  machen"  Yt  6.  3.  a)  ||  mit ^•^«/(^(sd.)  'wenn  etwa':  ^yadipatiy  *'ma- niyähay:  ciyJ'karam  (sd.)  .  .  patikaram dldiy  D.  6.  4.  b)  U  hinter  dem  Haupt- satz: martiy^  ky(^  draujaitJ'  ahatiy  avam *^u/iasata>n    pars3    y     avada    *mam-
21305:yavaesu-
22145:•  j.,g.vaes-V. 'sich  bereit  Stellen'.  Praes.  3
22151:vaes-  mit  paiti
22152:vaesma-
22162:•  '].  vaesa-  m.  'Knecht',  der  im  Herrenhof seine  feste,  dauernde  Wohnung  hat'*:  a%ra- varam..nman5.pailTm..nmanspaitTm  nairi- kqm..  'sJs/a  ^pairyaarSusca yaozda%d gSuI
22166:•  j.  vaesacpan-  Adj.  -  ?  -:  nBit  sat?m /ainti  viraja  nBil  halanl  jainti  'pa  (NS.) Yt.74.37.
22168:•  j.  vaesakay-  patr.  Adj.  'von  VaSsaka stammend,  dessen  Nachkomme':  tarn yasmia  aurra  hunavB  'iaya{li¥.)Yt^.S7; —  hunavB  'kaya  (als  AP.)  Ytj.  54.
```


## [2026-10-16T05:17:44.389Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E '.{0,80}(F.ulnis|Moder|.Gift.).{0,150}' BRT.txt | head -12; grep -n -o -E '•  j\\.  vas-.{0,300}' BRT.txt | head -4; grep -n -o -E '.{0,30}vasnah?-.{0,150}' BRT.txt | head -5"
}
```


### [2026-10-16T05:17:50.498Z] TOOL RESULT

```
ugrep: error: error at position 186
-\xbf]*))(?:[^\n\x80-\xbf][\x80-\xbf]*){0,150}
                 exceeds complexity limits___/


10173:•  j.gavasna-  m.  -?— :  asti  (Sp,  273  o.) yS  'nahe  mäuya  jya  Yt  10. 128  Gl.
15762:•  j.  *paurv5.vasna-'>  Adj.  'wobei  der Wille  vorausgeht  sva.  beabsichtigt,  vor- sätzhch':  yS  näirikayi  cthravaitya  .  .  °na ^adhna  tanUm  irihyäl  V.  l6.  1
23164:•  j-t  g-  vasna-  m.:  s.  unter  vasna-.
23281:•  p.  va§iia<,  j.,  g.  vasna-  m.  'Wille':  ys möi  . .  var^saiti . .  Ayal  'snn  f»rals.t»tn>m (sd.)  Y. 4^.19;  50,11,^4.15;  —  staola yesnya  ../raäm  (sd.)  'sna  akänt  d
```


## [2026-10-16T05:17:55.069Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BRT.txt').read()\npages=t.split('\\f')\ndef leaf(pos): return t.count('\\f',0,pos)\nfor pat in [r'•\\s+j\\.\\s+vis-', r'•\\s+j\\.\\s+visa-', r'vaesah-', r'•\\s+j\\.,?\\s*g?\\.?\\s*vas-\\s', r'Fäulnis',r'Moder']:\n    for m in list(re.finditer(pat,t))[:3]:\n        print(pat,'leaf',leaf(m.start()),repr(t[m.start():m.start()+250]));print()\nE"
}
```


### [2026-10-16T05:17:55.897Z] TOOL RESULT

```
vaesah- leaf 71 'vaesah-  Adj.:  s.  unter  tf/^flS«^-.\n•  g,  advan-,  j.  aSwan-  m.  \'Weg,  Pfad, Bahn\':  kasnU  i^ing  *str}mcä  dal  \'vanim\nI  "wer  bestimmte  den  Weg  der  Sonne  und\nder  Sterne?"  V.  44. 3;  —  tsm  °vän?m  .  .\nyj  "ha.k^rftä  ..  urvilx^a'

•\s+j\.,?\s*g?\.?\s*vas-\s leaf 759 '•  j.,  g.  vas-  V.  \'wollen\'.  Praes.  i  vas- US:  —  PPfP.  urta-.\n\'wollen,    wünschen\';    1)    mit    Akk.    als Ob].:  kal  vail  "was  willst  du?"  y.34.  la;\n—  *vlli\'im  nsrpi  asürahyS  *yS  *ma  vastmi *lsiljcfa\'^rlm  ", .  eines  uns'

Fäulnis leaf 481 'Fäulnis,  Venvesung": cvat  antar>  *n)r3ui  aSsa  druxl  y3  nasus axtica  \'ti^a  ahitica  fräsnaoiti  "wie  viel . , trifft  die  Drug  . .  mit  Krankheit,  Fäulnis und  Befleckung?"  V.5. 27,\nZum  V.  pav:  —  Vgl.  pülay;  zu  dem  sich *paviüiy'

Fäulnis leaf 481 'Fäulnis und  Befleckung?"  V.5. 27,\nZum  V.  pav:  —  Vgl.  pülay;  zu  dem  sich *paviüiy\'  verhalt  wie  im  Aind.  sämlay-  I.  zu sätäy-  i,  —  Pü.!  paiinjisn  \'Bespiengung\',  erl. : remanih.  —  i)  So  L  4,  K  1 ;  NA.  pivaf.\n•  j.  \'par- '

Fäulnis leaf 808 'Fäulnis\',\n•  j.  vyant-  Adj.,  PPA.:  s.  vä(.y)-.\n•  j-.  g-  vyam-  f.  i)  \'Zuwendung  des  Lohns beider  Verteilung,  Lohnverteilung\':  iiyayij/a (LP.)\'\' 7(7//ajflift\'^  (näml.  satavaäS)  srirJ Aiitaili  . .  huysiryä  avi  dai^hul  "wenn  er s'

Moder leaf 144 'Moder.<,»a-:..i°\'w<i^    "makyä  pttä    anySramnd\'  Bh./.z;\n—  Vgl.   \'arSan-.   —   ai.  fifoia-   Name   eines  \\  —  \'mar  Ao.  J.  2.\nGebirgs.  Komp.:  arsa-^ama-  \'die  Kraft  eines  Bären\')\n,     ,  \\   ,      X  \\  m  »...  besiliend\'.  —    '

Moder leaf 731 'Moder,  Verwesui^; Ort  der  Verwesung":  timS  ä\x0cca  \'!b  Sca aciH»m  aca  ahäm  3  V,_j.  35;  —  duivan- näis  \'SB  rastt  (sd.)  Y.5^.  9.\nVgL  ahd.  wesanen  \'faul  werden\',  nhd.  ver- wesen. —  Pü-  (zu  V.  _J)!  besömanä\'l,  erl.;  ax" i  da'
```


## [2026-10-16T05:18:01.829Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('BRT.txt').read()\ndef leaf(pos): return t.count('\\f',0,pos)\ni=t.find('Moder,  Verwesui^'); print(repr(t[i-500:i+400]))\ni=t.find(\"j.,  g.  vas-  V.  'wollen'\"); print(repr(t[i:i+1200]))\nfor pat in [r\"'Gift'\", r'vT?i-\\s', r\"viia-|visa-  n\"]:\n  for m in list(re.finditer(pat,t))[:4]: print(pat,leaf(m.start()),repr(t[m.start()-150:m.start()+200]))\nE"
}
```


### [2026-10-16T05:18:02.497Z] TOOL RESULT

```
'omnqm{%A.)  Yt  70.86.\nZum  V.  vaes-.  —  ai.  vgl.  vitman-  n.  >>.  — \'*  S  3\'M  n.  10.  —  >)  Zur  DÜTerenz  zwischen viüsma-  m.  nnd  ai.  -vliman-  n.  s.  ai.  dk^-mo\' neben  \'man-,  Mitta-  neben  \'man-  ui«.\ndb,Google\n1329  vaez-\n•  j.  vaez-  V.,  nur  mit  nT  \'an-,  einstecken\', Praes.  3  viza-.\nhaom>m  yim  mvizatti^  nivandäi  (sd.) apayeiti  "wenn  man  einen  ^Hfmustengel ansteckt,  entgeht  man  .  ."  Yt  1^.57.\nEt.?  —  t)  Faljch  S  363.  16.\n•  j-,  g.  vaeäah-  n.  \'Moder,  Verwesui^; Ort  der  Verwesung":  timS  ä\x0cca  \'!b  Sca aciH»m  aca  ahäm  3  V,_j.  35;  —  duivan- näis  \'SB  rastt  (sd.)  Y.5^.  9.\nVgL  ahd.  wesanen  \'faul  werden\',  nhd.  ver- wesen. —  Pü-  (zu  V.  _J)!  besömanä\'l,  erl.;  ax" i  darlömand,  (lu  Y.  Jj):  vesilH(?j\'),  erl.;  dort i  vBihilJ)*).  —  \')  Verwechslung  mit  dvtüi\'.  — »)  Mills  G.  361;  6es\';  s.  No.  i.\n•  j. '
'j.,  g.  vas-  V.  \'wollen\'.  Praes.  i  vas- US:  —  PPfP.  urta-.\n\'wollen,    wünschen\';    1)    mit    Akk.    als Ob].:  kal  vail  "was  willst  du?"  y.34.  la;\n—  *vlli\'im  nsrpi  asürahyS  *yS  *ma  vastmi *lsiljcfa\'^rlm  ", .  eines  unstarken  Mannes, während  mein  Wunsch  auf  einen  macht- vollen Gebieter  gerichtet  ist"Y.  2p.  9;  — Pass.:  aAmai yahmai  usta  kahmnictl  *vasS *xsayqs  mazää  däyäf  ahurB  ".  .  dem  was er  wünscht,  der  nach  Wunsch  schaltende MAk.  gewäJiren  möge"  "^-43- 1  \'*•  2)  mit Inf  als  Obj.:  täcll  mazda  vas?mT  attyäiä vTduyi  "das,  0  M.,  und  noch  andres  möchte ich  wissen"  Y..^.  3;  —  kahmäi  vtviäuyi (sd.)  vai\'l  Y.  43.  9;  —  AvS  nS  , .  vastX  , , carikinitrs  i^A)  srävayeiiAf  Y.2g.8;  — -fj  vä   *fräsrüidysi  (sd.)    vastt  Y.^.  14;\n—  tumahli^A.)  usJmaÄT  Y.3S.3;  —  yai vasi  . .  avä  JdaHa  taurvayS  (sd.)  . .  a^a  . . Vt  1. 10;  —  yeai  vasm  (Konj.) . .  »am  . .\n   _  138«\nhixtayaica  . .  V.  6.  6;  —  werllos:  narS hava  urva  (statt  Akk.)  .  .  mm  (Pract) fräyants  (statt  Inf.;  sd.)  . .  tarS  p?!üm  . . Vyt  4\'2.  3)    mit   Akk.    dessen   (dem\noder  von  dem  etwas  gewünscht'
'Gift' 266 ".?0.  —  Pü.:  fehlt;  Kyo.:  kF«ü.  ei\\.:  n.i kiMii  li.iti  ,/,ijl  kitnad.  —  ')  Man  setit  wegen np.  kiihijsl  'Koloquinle'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.\n•  p.  ka''büjiya-  m.  EN.  eines  persischen Königs;  Katnb"
'Gift' 806 '  grünliche  Gift  klafler- hoch  floss"  Y.o.  11;  Yt/p.40.\nKoropA   Vgl  vlia:  —  >)  So  K  j,  Pt  4  und\nFl  (wYt.  79.  40>\n•  j,  viäa-  n.  \'Gift\':  vTsa.aoca  Y.^^p.  1 1  Gl.\'\'; —  visaca  Y. 31.20  PüZ.\nKompA.,  E.j  Ableit.  —  Vgl.  ws-,  —  ai.  vi^ä-  n. ; vgl.  mp.  vti,  np.  6es  (wozu  Hbm.  PSL  270).  — ■)  S.  dazu  H.  3.  '
'Gift' 807 '!t«>f-  "  \'\'  Dem  Noroen  ist  überall\na\'.Si<  \'pake  N.4S.  ,     ,„5^^  Y.  sS.  7,  Yt.  5.  98,  v-  6\'.  Ai.  2.  j.\nAltes   Komp.:  ar.  V"-  \'Gift\'  +*j../a.  \'Safl\';        Vyt.  13,4s  der  Tiiel  .iopov  (sd.)  vorgeselrt.\nvgl.  an.  sa/f,  S  3\'>4  A.  I   No.  I.  -  arm.  L\\V. ,      dj^   Identifikation   dieses  K  mit    dem  Vate'
vT?i-\s 17 ' Die  eingeklammerten ZifTem  —  bei  Y,,  Vr.,  V.  —  geben  die  abweichende  Kapitel-  und  Paragraphen- zählung in  Spiegels  Ausgabe  der  Fahlavi-  und  SanskiitUbersetzung  aa\n3.\\.3.  aj.\n4  :  Y.  //.  17.\n5  :  Y.   //.  18.\n6  :  Y.   II.  19.\n7  :  V.     7.  33.\n8-12  :Y.  22.33-17.\n13  ■■  Y.  S-  35-\n14  :  Yt.  /.  O. 15 -V.  2/.li.'
vT?i-\s 140 "  —    Pü.:    transskr.    — ■>  Hd».  arad'.  —  a)  Hds.  'duia.\nj.  atidvai  N.  8^-.  lies  mdvaya.\nj.  aridiidjungö:  Lies  indvS.'.\n•  j.  aradvi-  f.  Name  eines  mythischen Flusses *>:  -dvT  nqtna  apa  V.  7.  16;  — bqsnubyS  {^A^  °duya  V.z.aa;  —  °dt^ä lipo  anähilayä  Ny.  *  o,  Vr.  7,5,  YLr.  21; —  sonst  mit  sBrä-  und  anä"
vT?i-\s 175 'nd  astak  pa  padrak;  der Re<:|  feUt.  —  ■>  Sicher  falsch  Haiig  ZPGl. 53,  DsT.  ZA.  3.   17.\n•  j.  "aätay-  m.  \'Pfeil\':  yat .  .  jyä  navi- >jqn  (sd.)  tiyrar?hs  "tayS  Yt  10.  113.\nEt?  —  Unsicher.\n•  j.  iaitay-  f.  ein  Längenmass ". KompA.,  E.  —  Vgl.  uiaitay.  —  Eig.  Bed.?  — ■>  Von  unbekannter,  jedenfalls  aber  ger'
vT?i-\s 225 '  oJm:  s.  aiva-  mit  No  1.\n•  j.  öiva\'  Adj.:  s.  unter  aH\'a-  (mit  No.  1).\ng.  Hyä  Y.  47.»:  s.  \'«.  II  2  1. j.  ^^m,  lii\'um:  s.  nrävi-  mit  No.  1.\n•  j.  äonhanna-  Adj.  \'zum  (Essen,) Trinken  dienend\' :  tasta  \'na  (NPn.) Trinkschalen"  V.7.73.\nKomp. :  ä+*j\'.jr3na- ;  %  2g8.  7.  —  mp.  Jj"."», np.  äj*aj-  {äxur)  \'Stal'
```


## [2026-10-16T05:18:13.666Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==807 {print substr($0,1,80)} NR==732{print substr($0,1,80)} NR==760{print substr($0,1,80)}' BRT.txt; awk 'BEGIN{RS=\"\\f\"} NR==281 || NR==280 {print \"LEAF\",NR-1;print}' HUB.txt | grep -n -i -E 'LEAF|b[eē]š|bes|vis|Gift' | head"
}
```


### [2026-10-16T05:18:14.228Z] TOOL RESULT

```
  überhaupt  keine  ; Versündigung"  P.  57;  —  hyat  vUJntä  j (sPPrM.)  ängva
  —  >)  Hda.  varalc3.
•  j,  varsni-haräta-  Adj.  '(admissuram habens,  d.  i
 geschickt' {?): dva  dim  nara  isSi'ie  vJzSislam  (sd.)  'rynlqm . .  ufajkam
1:LEAF 279
29:paitivad-, Im Ap. bestand also *dviikam (ace.
50:LEAF 280
55:'Aconitnm* = skr. visa- *Gift*, vis&- *em Aco-
57:ftltere Form (nicht vis oder v^.
89:p. 71, Nr. 678. Vgl. auch syr. NIHT Gift* und phi. zahrak
```


## [2026-10-16T05:18:20.187Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==281 {print}' HUB.txt | sed -n 1,12p; python3 - <<'E'\nt=open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt').read()\nimport re\nfor pat in [\"j,  viäa-  n.\",\"j-,  g.  vaeäah-\",\"j.,  g.  vas-  V.\"]:\n  i=t.find(pat); pg=t[:i].rfind('\\f'); seg=t[pg:i]\n  nums=re.findall(r'(?m)^\\s*(1[0-9]{3})\\s',seg)\n  print(pat, nums[-3:], re.findall(r'\\b1[0-9]{3}\\b',t[i-3000:i])[-5:])\nE"
}
```


### [2026-10-16T05:18:20.855Z] TOOL RESULT

```
— 270 —
p. 33, Nr. 251. Dazu (np. bed) audi deutsch Weide u. s. w.,
vorgerm. vtt- (Klug^e, Wb.)
p. 34. Geiger setzt Idg-. F. IV, Anz. 23 np. Im
'Aconitnm* = skr. visa- *Gift*, vis&- *em Aco-
nitnm*. Aber Phi. nnd Armen. geben b^ als
ftltere Form (nicht vis oder v^.
p. 38, Nr. 295. Vgl. WZKM. 8, 274.
p. 41, Nr. 314. Vgl. WZKM. 8, 272.
p. 44, Nr. 349. Bei Muwaffaq 3, Z. 3 v. u.; 4, Z. 12 paiSa
(mit dl).
p. 45, Nr. 349. Vgl. niand. LW. pugddma 'Botschaft*.
j,  viäa-  n. [] []
j-,  g.  vaeäah- ['1329'] ['1329']
j.,  g.  vas-  V. [] ['1381']
```


## [2026-10-16T05:18:27.028Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==56 || NR==55 {print \"LEAF\",NR-1;print}' HRN.txt | grep -n -i -E 'LEAF|Aconit|Gift|vi[sš]a|^ *2[5-9][0-9]\\.' | head"
}
```


### [2026-10-16T05:18:27.550Z] TOOL RESULT

```
1:LEAF 54
37:LEAF 55
```


## [2026-10-16T05:18:32.030Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Aconit|Eisenhut' HRN.txt | head; grep -n -E \"^ *(262|263|264)\\.\" HRN.txt | head"
}
```


### [2026-10-16T05:18:32.555Z] TOOL RESULT

```
2648:262. bever 'tausend'.
2651:263. beve Wittwe'.
2657:264. beyoj^beyök 'Braut*, :V2 (Jer. 16, 9).
```


## [2026-10-16T05:18:39.084Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2620,2650p HRN.txt"
}
```


### [2026-10-16T05:18:39.628Z] TOOL RESULT

```
vimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach
Darmesteter's Correctur, Et. ir. II, 138).
Die Etymologie ist gewiss falsch, da altes vi- im
Neupersischen consequent zu gu- wird, und selbst bei
Annahme eines Ausnahmefalles (z. B. biüer^ No. 218)
das i völlig unerklärt bliebe. Dass das erste Glied
np. be- *ohne' sei, könnte man nach sar. LW. bhnar
(d. i. bemar) vermuten; doch erhält man bei dieser
Ableitung keinen guten Sinn. Bartholomae schlägt
mir die Etymologie upai (s. No. 247) + mära-y also
*am Tode' vor, aber dafür spricht nicht das phlv. v
(oder auch w),
30. bin *sehend', hin-em^ binä^ bmis,
ap. vainähiy Conj. (Venn) du siehst'; aw. vaenämi
*ich sehe'; phlv. ven-am, ven(i)sn^ venäk^ venastan (päz.
vm-), vergl. üben (vd. 19 (43)).
af/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.
viti-am, sar. veln-am.
*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL— 60 —
261. Mm 'Nase.
Semn. vlm; mäz. v^it,
aw. va^nä' Nase' (Y. 9, 11 (35), Darmesteter, Et.
ir. I 57); phlv. venik (Bund., AV.), bEmk (AV.).
kurd. hen *Nase, Geruch' (H.-Sch.); bei. gin *Atem,
Leben (109) (?).
Fr. Müller (WZKM. 5, 260) stellt dazu phlv. mi,
(ZP61. 8, 3) 'Hauch* und nimmt als dessen Grundform
*vayana' an.
262. bever 'tausend'.
äw. ba^vare 'tausend'; phlv. bevar.
oss. d. beurä, t. birä Viel, sehr, lange (61).
```


## [2026-10-16T05:18:48.783Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in بیش ویروس بس بسیار بسنده; do python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 537, Mo'in s.v. $w (roots Weis/Wek)\"; done 2>&1; for u in 'https://abadis.ir/fatofa/بیش/' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weḱ-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wacati' 'https://en.wiktionary.org/wiki/viscum' 'https://en.wiktionary.org/wiki/bison' 'https://en.wiktionary.org/wiki/weasel' 'https://en.wiktionary.org/wiki/ooze' 'https://en.wiktionary.org/wiki/viscous'; do python3 tools/fetch_source.py \"$u\" --note \"page 537, roots Weis/Wek\"; done"
}
```


### [2026-10-16T05:18:56.049Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5ed95526867a6a2e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/87f9172524810508.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9b65a9c279801532.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8bcde23c48ba871b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dec804c6fccaec5f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b16475fc903ea3c7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e4a5279c0a77f7d6.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b3525b4385613431.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dcd7d636afd86fcc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/55a10c40b378798c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d2a75bbda23232cc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ac1a6b951184fd79.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5967bb2a98b47cee.txt
```


## [2026-10-16T05:19:07.017Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 5ed95526867a6a2e 87f9172524810508 9b65a9c279801532 8bcde23c48ba871b dec804c6fccaec5f b16475fc903ea3c7 e4a5279c0a77f7d6 b3525b4385613431 dcd7d636afd86fcc 55a10c40b378798c d2a75bbda23232cc ac1a6b951184fd79 5967bb2a98b47cee; do echo \"$f $(sed -n 3p $f.txt) $(wc -c <$f.txt)\"; done; for f in 5ed95526867a6a2e 87f9172524810508 9b65a9c279801532 8bcde23c48ba871b dec804c6fccaec5f; do echo '---'; tail -n +5 $f.txt | head -c 700; echo; done"
}
```


### [2026-10-16T05:19:07.564Z] TOOL RESULT

```
5ed95526867a6a2e STATUS: 200 1096
87f9172524810508 STATUS: 200 1203
9b65a9c279801532 STATUS: 200 1166
8bcde23c48ba871b STATUS: 200 1307
dec804c6fccaec5f STATUS: 200 1185
b16475fc903ea3c7 STATUS: 200 11336
e4a5279c0a77f7d6 STATUS: 200 4359
b3525b4385613431 STATUS: -1 161
dcd7d636afd86fcc STATUS: 200 4412
55a10c40b378798c STATUS: 200 17190
d2a75bbda23232cc STATUS: 200 20882
ac1a6b951184fd79 STATUS: 200 14278
5967bb2a98b47cee STATUS: 200 9369
---

معنی بیش | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بیش

 فرهنگ انتشارات معین
 [ په . ] (ق .) افزون ، زیاد.
 بیش در فرهنگ‌های دیگر
 معنی بیش در لغت‌نامه دهخدا 
 معنی بیش در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بیش در دیکشنری فارسی به عربی 
 معنی بیش در دیکشنری فارسی به انگلیسی 
 معنی بیش در گویش مازنی 
 معنی بیش در ف
---

معنی ویروس | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 ویروس

 فرهنگ انتشارات معین
 [ فر. ] (اِ.) موجود بسیار ریزی که باعث بروز بیماری می شود.
 ویروس در فرهنگ‌های دیگر
 معنی ویروس در لغت‌نامه دهخدا 
 معنی ویروس در فرهنگ فارسی عمید / قربان‌زاده 
 معنی ویروس در دیکشنری فارسی به عربی 
 معنی ویروس در دیکشنری فارسی به
---

معنی بس | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بس

 فرهنگ انتشارات معین
 (بَ) (ص .) 1 - کافی . 2 - بسیار.
 بس در فرهنگ‌های دیگر
 معنی بس در لغت‌نامه دهخدا 
 معنی بس در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بس در دیکشنری فارسی به عربی 
 معنی بس در دیکشنری فارسی به انگلیسی 
 معنی بس در گویش مازنی 
 معنی بس در فرهنگ متر
---

معنی بسیار | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بسیار

 فرهنگ انتشارات معین
 (بِ) [ په . ] (ص . ق .)زیاد، متعدد، فراوان ، دارای کمیت بزرگ نامعلوم .
 بسیار در فرهنگ‌های دیگر
 معنی بسیار در لغت‌نامه دهخدا 
 معنی بسیار در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بسیار در دیکشنری فارسی به عربی 
 معنی بسیار در دیکشنر�
---

معنی بسنده | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 بسنده

 فرهنگ انتشارات معین
 ( بَ سَ دِ) 1 - (ص .)کافی ، بس . 2 - شایسته .
 بسنده در فرهنگ‌های دیگر
 معنی بسنده در لغت‌نامه دهخدا 
 معنی بسنده در فرهنگ فارسی عمید / قربان‌زاده 
 معنی بسنده در دیکشنری فارسی به عربی 
 معنی بسنده در دیکشنری فارسی به انگلیسی 
 معنی بس�
```


## [2026-10-16T05:19:12.931Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E 'زهر|گیاه|اقونیطون|بیخ' b16475fc903ea3c7.txt | head -8; echo '---weḱ'; sed -n '/Root/,/References/p' e4a5279c0a77f7d6.txt | grep -v '^\\s*$' | head -60"
}
```


### [2026-10-16T05:19:13.439Z] TOOL RESULT

```
64: ( اسم ) ۱ - گیاهی است که در چین و هند روید. برگهای آن مانند کاهو و کاسنی است و بیخ آن سفت و سخت است و خوردن آن موجب هلاک گردد . ۲ - ترح آفت .
74:گیاهی بسیارسمّی با برگ هایی شبیه برگ کاهو یا کاسنی و ریشۀ غده ای سفت که اندرون آن سیاه است، هلاهل، اجل گیاه. 
86: نامی هندی ـ ایرانی چند گونه از جنس آکونتیوم از تیرۀ آلالگان و همچنین نام زهر حاصل از ریشۀ آن ها و یا ساقۀ زیرزمینی تُکمه ای آن ها (← آقونیطون). این واژه از bīš پهلوی (فارسی میانه) گرفته شده است. زیرا در بُنْدهش می خوانیم که وقتی پتیاره (= اهریمن) بر همه چیز آمیخت، به چند گیاه ازجمله بیش بیشتر آمیخت؛ درنتیجه این گیاه خیلی زهرآگین شد به طوری که اگر مردم و گوسفندان از آن بخورند می میرند. همین واژه به صورت wēš/v در پهلوی به معنای «زهر» آمده است که از واژۀ سانسکریت viš گرفته شده است. نام هندی الاصل دیگر این گیاه هَلاهِل یا هَلْهَل است. در عربی و فارسی به صورت قاتل الذئب، خانِق النَّمر، طَوارَه، گرگ مرگ و جَرْجَمَرج (معرب گرگ مرگ) آمده است. wikijoo: بیش 
---weḱ
 Root 
 1.1.1 
 Derived terms 
 1.2 
 References 
 Root
 [ edit ] 
 *weḱ- [ 1 ] [ 2 ] 
 to wish , to want 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *weḱ- (2 c, 0 e) 
 *wéḱ-ti ~ *uḱ-énti ( athematic root present ) 
 *wé-woḱ-ti ~ *wé-wḱ-n̥ti ( reduplicated present ) [ 1 ] 
 Proto-Anatolian: 
 Hittite: [script needed] ( ú-e-wa-ak-ki /⁠wewakki⁠/ ) (functioning as an intensive verb) [ 3 ] 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: ववक्षि ( vavákṣi , 2sg. ) ( possibly ) 
 *wéḱ- ont-s 
 Proto-Hellenic: 
 Ancient Greek: ἑκών ( hekṓn ) 
 Proto-Indo-Iranian: *ućánts 
 Proto-Indo-Aryan: *uśánts 
 Sanskrit: उशन्त् ( uśánt ) 
 Unsorted formations 
 Proto-Hellenic: 
 Ancient Greek: ἕκηλος ( hékēlos ) , εἰκῇ ( eikēî ) 
 Proto-Indo-Iranian: *wašnas 
 Proto-Iranian: *wašnah 
 Avestan: 𐬬𐬀𐬯𐬀𐬵 ( vasah ) , 𐬭𐬈-𐬎𐬎𐬀𐬯𐬥𐬀 ( re-uuasna , “ desire ” ) 
 Old Persian: 𐎺𐏁𐎴 ( v-š-n /⁠vašna⁠/ , “ will ” ) 
 → Old Armenian: վասն ( vasn ) 
 Proto-Hellenic: 
 Ancient Greek: ἕκητι ( hékēti ) 
 References
```


## [2026-10-16T05:19:18.821Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E 'From|ἀέκων|ἄκων' e268f8ee9f4294a3.txt | head -8; for f in dcd7d636afd86fcc 55a10c40b378798c d2a75bbda23232cc ac1a6b951184fd79 5967bb2a98b47cee; do echo \"--- $(sed -n 1p $f.txt)\"; grep -n -E '^ (From|Borrowed|Learned|Inherited)' $f.txt | head -4 | cut -c1-600; done"
}
```


### [2026-10-16T05:19:19.419Z] TOOL RESULT

```
145: From Wiktionary, the free dictionary
153: From Proto-Indo-European *weḱ- ( “ to choose; to want ” ) . According to Beekes, the term derives from a lost present verb *ϝέκμῐ ( *wékmĭ ) , itself perhaps from a present verb equivalent to Sanskrit वष्टि॑ ( váṣṭi , “ to will ” ) and Hittite [Term?] ( /⁠wekkmi⁠/ , “ to want; to desire ” ) . [ 1 ] The LIV suggests that the Hittite and Greek forms derive from a single Narten-type present *wḗḱ-ti whereas the Sanskrit form supposedly—according to the LIV—derives from an athematic root present *wéḱti . [ 2 ] 
179: 460 BCE – 430 BCE , Herodotus , Histories 2.65.5 : [ … ] τὸ δ’ ἄν τις τῶν θηρίων τούτων ἀποκτείνῃ, ἢν μὲν ἑκών , θάνατος ἡ ζημίη, ἢν δὲ ἀέκων, ἀποτίνει ζημίην τὴν ἂν οἱ ἱρέες τάξωνται. [ … ] tò d’ án tis tôn thēríōn toútōn apokteínēi, ḕn mèn hekṓn , thánatos hē zēmíē, ḕn dè aékōn, apotínei zēmíēn tḕn àn hoi hirées táxōntai. Translation by George Rawlinson When a man has killed one of the sacred animals, if he did it with malice prepense , he is punished with death; if unwittingly, he has to pay such a fine as the priests choose to impose. 
--- URL: https://en.wiktionary.org/wiki/viscum
148: From Wiktionary, the free dictionary
--- URL: https://en.wiktionary.org/wiki/bison
258: From Wiktionary, the free dictionary
274: From Middle English bysontes , bysountes   pl , from Middle French bison , from Latin bisōn, bisōnt- ( “ wild ox ” ) .
602: From English bison , from Middle English bisontes ( plural ) , from Old French bison , from Latin bisōn, bisōnt- ( “ wild ox ” ) , from Proto-Germanic *wisundaz ( “ wild ox, aurochs ” ) , from Proto-Indo-European *wisAn- ( “ aurochs, aurochs horn ” ) , from Proto-Indo-European *weys- ( “ to flow, melt ” ) .
713: From Middle French bison , from Latin bisōn, bisōnt- ( “ wild ox ” ) , from Proto-Germanic *wisundaz ( “ wild ox, aurochs ” ) .
--- URL: https://en.wiktionary.org/wiki/weasel
200: From Wiktionary, the free dictionary
224: From Middle English wesele , from Old English weosule , from Proto-West Germanic *wisulā , from Proto-Germanic *wisulǭ .
--- URL: https://en.wiktionary.org/wiki/ooze
184: From Wiktionary, the free dictionary
404: From Middle English wose , from Old English wāse ( “ mud, mire ” ) , from Proto-West Germanic *waisā , from Proto-Germanic *waisǭ (compare Dutch waas ( “ haze, mist; bloom ” ) , (obsolete) German Wasen ( “ turf, sod ” ) , Old Norse veisa ( “ slime, stagnant pool ” ) ), from Proto-Indo-European *weys- ( “ to flow ” ) (compare Sanskrit विष्यति ( viṣyati , “ flow, let loose ” ) ). Compare also Saterland Frisian öäzje ( “ to smear ” ) . More at virus .
--- URL: https://en.wiktionary.org/wiki/viscous
179: From Wiktionary, the free dictionary
352: Borrowed from Late Latin viscōsus , from Latin viscum .
```


## [2026-10-16T05:19:24.739Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E 'Etymology|Proto-|uncertain' dcd7d636afd86fcc.txt | head -8 | cut -c1-500; grep -n -E 'Proto-Italic|weys|Etymology' 4ab82ab98c6be78f.txt | head -10 | cut -c1-500"
}
```


### [2026-10-16T05:19:25.272Z] TOOL RESULT

```
65: Etymology 
160: Etymology
163: Perhaps from Proto-Indo-European *weyḱs- , possibly a European borrowing for a tree similar to the mistletoe. Compare also Ancient Greek ἰξός ( ixós , “ mistletoe, birdlime ” ) , Proto-Slavic *višьňa , Proto-Germanic *wīhsilō , and probably Italian visciola ( “ sour cherry ” ) , the last likely a Germanic borrowing. Traditionally associated with vīrus , although this is unlikely. Also compare Proto-Germanic *wiskaz ( “ bundle of hay or straw, wisp ” ) . More at virga .
274: Categories : Latin terms derived from Proto-Indo-European 
62: Etymology 
103: Etymology 
117: Etymology 
134: Etymology 
157: Etymology 
174: Etymology 
194: Etymology 
217: Etymology 
228: Etymology 
251: Etymology
```


## [2026-10-16T05:19:30.777Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E 'vīrus|Proto-Italic' 4ab82ab98c6be78f.txt | head -10 | cut -c1-600"
}
```


### [2026-10-16T05:19:31.314Z] TOOL RESULT

```
724: See also: -virus , Virus , virüs , vírus , vīrus , and vīruss 
747: Proto-Italic *weizos 
748: Latin vīrus bor. 
752: From Middle English virus , from Latin vīrus ( “ poison, slime, venom ” ) , via rhotacism from Proto-Italic *weizos , from Proto-Indo-European *wisós ( “ fluidity, slime, poison ” ) . First use in the computer context by David Gerrold in his 1972 book When HARLIE Was One .
1147: Latin: vīrus   n 
1149: Latvian: vīruss   m 
1419: From Latin vīrus .
1443: Ultimately from Latin vīrus .
1746: Learned borrowing from Latin vīrus .
1795: Borrowed from English virus , from Latin vīrus , from Proto-Italic *weizos , ultimately from Proto-Indo-European *wisós ( “ poison ” ) .
```


## [2026-10-16T05:19:40.985Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 243 244 253 254; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n {print \"=== LEAF(1based)\",n; print substr($0,1,150)}' WLD_Bd1_pages.txt; done; awk 'BEGIN{RS=\"\\f\"} NR>=242 && NR<=245' WLD_Bd1_pages.txt | grep -n -i -E 'Gift|virus|vaes|vis[aä]|Wiesel|wisunt|ooze|ixos|viscum' | head; awk 'BEGIN{RS=\"\\f\"} NR>=252 && NR<=255' WLD_Bd1_pages.txt | grep -n -i -E 'vasmi|wollen|vasn|usant|ἑκών|ekon' | head"
}
```


### [2026-10-16T05:19:41.929Z] TOOL RESULT

```
=== LEAF(1based) 243
                                                                         :




234                                                                    
=== LEAF(1based) 244
                                                                                                                                           ,




     
=== LEAF(1based) 253
                                                                                                                                                      
=== LEAF(1based) 254
      a                                                                                                              e                                
345:  „sehen‘- in aiioi-visam „habe wahrgenommen“, paitivlsdm       wurde gewahr                                  ,
181:nek- „wollen, wiinschen                                                           .
185:     Ai.    vitr-mi,                         ia-nidsi                    ,   av. rusaml,                   ushiuthi                            „wollen,              wiinscheir‘.              Ptc.         ai.
187:uni ut-, fem. ueatl „\\illig“, av. an-usant-, -usaitl „widerwillig, ohne es zu
188:wollen , av. vasali- (nom rasa „wollend = nach seinem Willen
205:freiheit     ap. vainCi  ; av. vasnd (i. sg.) ,.nach dem Willen  ,  (arm. vasn
271:wollend, widerstrebend“                          ( :       d-ftyta-      — thivud'Qto davtiaz-): diese Formen
```


## [2026-10-16T05:19:47.974Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR>=252 && NR<=255 {print \"=== LEAF\",NR}' WLD_Bd1_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} NR>=252 && NR<=255' WLD_Bd1_pages.txt | sed -n 178,190p | tr -s ' '; grep -n -E '^ *(ueis|u̯eis|neis|ueis-)' WLD_Bd1_pages.txt | head; python3 - <<'E'\nt=open('WLD_Bd1_pages.txt').read()\nimport re\nfor pat in ['Gift', 'Moder','zerflie']:\n  for m in list(re.finditer(pat,t))[:6]:\n    print(pat, t.count('\\f',0,m.start())+1, re.sub(r'\\s+',' ',t[m.start()-150:m.start()+150]))\nE"
}
```


### [2026-10-16T05:19:48.690Z] TOOL RESULT

```
=== LEAF 252
=== LEAF 253
=== LEAF 254
=== LEAF 255


 --
nek- „wollen, wiinschen .



 Ai. vitr-mi, ia-nidsi , av. rusaml, ushiuthi „wollen, wiinscheir‘. Ptc. ai.

uni ut-, fem. ueatl „\\illig“, av. an-usant-, -usaitl „widerwillig, ohne es zu
wollen , av. vasali- (nom rasa „wollend = nach seinem Willen
 --
 vasO.
Gift 128 n Apr. 345) „das Essen“, aksl. ohcch „Mahlzeit‘, (vielleicht auch jadb „Gift“, s. Berneker 271 f.); "edes- in lit. cde.sis „Speise“, eskq acc. „Appetit“, alt „FraB, Aas“ 
Gift 162 dazu, Gruppe die zahlreichen Formen Falk-Torp 1327, 1328. Ob ai. ala-, bei alaku „Gift“ hierher gehort (z. B. Falk-Torp aaO.) bleibt zweifelhaft. Gutturalerweiterung liegt vor in: ai.rjisd-h „klebrig, glatt, schliipfrig“ (?; n
Gift 171 sus obi. *(j)st n- mit dem nomi- nativischen (fi von ai. asrg-. sowie von sanies „verdorbenes Blut und andere Safte des Korpers, Wundjauche, Geifer, Gift“ als Verbindung desselben *(o)se n mit nominativischem i s. Yf. LEWb. 2 s. v.. Reichelt KZ. 46, 320 f. 
Gift 175 dro „Kern“ damit gleichsetzt; andere Deutungen von slav. ji-clro, jadro s. bei Berneker aaO., Mikkoll Ursl. Gr. 47), Yermutlich auch nhg.jadz ..Gift" (mit iibertragener Bed. „Zorn, sich giften". wenn lit. aidinti „reizen“ nach slov. jiuhti „argern
Gift 175 ur Entstehung von slav. jadz aus *oidos und gegen die von Berneker 271 als zweite Moglichkeit zugegebene Herkunft aus *edo- zu ed- ..essen". etwa wie Gift zu yeben) und ksl. isto, pi. istesa ,,Hode, Niere" aus schwundstufigem *id- s-fo-, woneben *oid-s-to- ( aisl. eista) vielleicht in aruss. jestesp
Gift 252  : (auch dem Gerucli) faulender. modriger Pflanzenteile (s. dazu unter *nei- ..welken"), unreinen Silften, Gift. Ai. ceiati „zerflieBt" fDhatup. vesantir nadkis Rgv. I 18 1, 6 „flieBende : Stro
Moder 162 ahrscnein- lich, doch wird ulcus „Geschwur“, gr. c/.y.o; „Wunde, Geschwiir“ kaum zu verbinden sein, wie auch die llerleitung von altn. [/Ida ,,Moderduft“ aus *nlhipon (Falk-Torp aaO., Fick III 4 559) unwahrscheinlich ist; vgl. *elkus „Geschwiir“. Lit. dlksna ,,Lache“ kann auf *ahj-snu zuriick
Moder 162 - diber die arm. Formen im Bes. vgl. Petersson aaO.j. Dazu altn. nldua „schimmeln“, wohl auch [/Ida „Moderduft“ (s. o.l, isl. uldinn (Bed. wie bei ul, ulen s. o.) , usw., ahd. oltar „Schmutzkrume“. tlber da
Moder 253  av. vis-, visa- „Gift“. vaesah- „Moder, Yerwesung (Bartholomae Airan. Wb. 1329 nnter Yergleich mit 44 ahd. ivesanni,
Moder 290 2 Boisacq s v.) und evgcbg, drehen", , -tTjxog ..Schimmel. Moder". wenn eigentlich ./Bedecker" (ware *e-foco- t-. 2 vgl. ai. arno-vrt: s. Brugmann II 2. 298;; ovgarog.
Moder 710  Yf. LEWb. 2 s. v. und *ser- „stromen". ta-, te-; fai-, tai-, tl-; [tau-], teu-, tu- „schmelzen, sich auflosen (fliefien), liinschwinden (Moder, Yerwesendes)“. ta- kann vorkonsonantisch Ent- wicklung aus ta[i\- oder td[u]- sein, aber auch umgekehrt deren Grund- 
Moder 710 bg. tslo „Boden“ usw.); abg. tbleti „modern, verwesen, falja „Yerwesung“, russ. tlja r Faulnis, Rost; Motte (vgl. unten lat. tinea), Blattlaus" (im Moder lebende oder modriges um sich an- haufende Tiere). Arm. *tlro-, -ri- in triH „Hist u , trem „knete Mehl, Teig“ („*mache weicb
zerflie 92 i ' und ai. arddgati „beruhigt u. dgl.“ angereiht dogvf3>]0£t, raga^ei wird, doch s. iiber letzteres *ard- „zerflie8en“), II 4 19, III 4 19 (wo kaum zutreffend fiir anord. erta eber Yerwandtschaft mit ai. drdati, rdati s. *ard- — „zerflieBen“, 
zerflie 92  iiber letzteres *ard- „zerflie8en“), II 4 19, III 4 19 (wo kaum zutreffend fiir anord. erta eber Yerwandtschaft mit ai. drdati, rdati s. *ard- — „zerflieBen“, — allenfalls auch mit k’gig, eo£&i£a> empfohlen wird), Boisacq 75 (bier wird Lidens U. U. A. 1894, 80 Anm.
zerflie 148 sicli argern, zanken“ eine Empfehlung erbalt). Erweiterung er-d- (rf-Praesens ?) : s. erd- „zerflieBen“, ai. ardati, rdati „flieBt usw.“, auch „beunruhigt“ mit dem Kaus. ardayati „macht ; flieBen; bedrangt, qualt, totet“ ware a
zerflie 237 , ursprgl. „feucht“, zu erwagen, ob nicht die Yorstellung der abgefallenen welken und verfaulenden Blatter zugrunde liegt und Be- ziehung zu *ueis- „zerflieSen, modrig werden“ besteht: ahnlich Falk-Torp u. vissen.. uei-, ueia x - 
zerflie 251 d rise „Iveim‘ ! und wohl aucli iris ..safdger Stengel", das kauni nach Falk-Torp u. risscu zu norw. reisa „Schlamm“ usw., \Yz. ueis- ,.zerflieBen“ geliort; mit Be- deutungskonvergenz beider Sippen im Nord. reehtiet Persson Beitr. 322 Anm. 1); ags. wise ,,Spro8, Stengel"; lit. veisiit,
zerflie 251 er verden die bait. Worte ,.sich ,. von Meringer DLZ. 1913, 405 f. unter der Gdbed. des ..mannlichen Samens" zu ueis- ..zerflielien" gestellt). S. Persson Beitr. 322 Anm. ! (Liden IF. IS. 497 hatte die germ. Worte zu ueis- „drehen
```


## [2026-10-16T05:19:55.982Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nimport re\nt=open('WLD_Bd1_pages.txt').read()\ni=t.find('vaesah- „Moder'); print(re.sub(r'\\s+',' ',t[i-900:i+1800]))\nE"
}
```


### [2026-10-16T05:19:56.597Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:20:01.698Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; python3 - <<'E'\nimport re\nt=open('WLD_Bd1_pages.txt').read()\ni=t.find('„Moder, Yerwesung'); \nif i<0: i=t.find('Moder, Yerwesung')\nprint(i, re.sub(r'\\s+',' ',t[i-900:i+1600]))\nE"
}
```


### [2026-10-16T05:20:02.294Z] TOOL RESULT

```
1162313  44 in Ath.-Yeda XII 1. 5 nach Meringer DLZ. 1915. 405 f.. der entsprechend Ario-vistus als „aus arischem Samen ent- 44 sprossen“ deutet). visrd- „muffig riechend ; av. vis-, visa- „Gift“. vaesah- „Moder, Yerwesung (Bartholomae Airan. Wb. 1329 nnter Yergleich mit 44 ahd. ivesanni, wo niber s. *vei- „welken“'. Gr. log „Gift“ = lat. virus „zahe Fliissigkeit. Schleim, Saft (auch Tiersamen: iibler Geruch), bes. Gift" = ir. fi (Corm.) ..Gift"; cymr awi/av „Blut‘ (s. Fick II 4 265. Pedersen KG. I . 4- 73); anord. veisa ,,palus putrida -1 , ags. lease „Schlamm (aber dr. Wiese, Scbade 1170, Wood IA. 11. 205 usw., eher zu *n<is- „sprieBen“, wie wohl 44 auch norw. veis „saftiger Stengel ); ags. wav, afries. war „Alge, Tang -4 nach Holthausen IF. 32, 337 hie
```


## [2026-10-16T05:20:12.152Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt').read(); print(t.count('\\f',0,1162313)+1, t.count('\\f',0,t.find('an-usant-, -usaitl'))+1)\"; grep -n -E '^(weis-|wek-|weys|weik)' IEC.txt | head; grep -n -i -E '^(poison|wish|weasel)' SYN.txt | head"
}
```


### [2026-10-16T05:20:12.812Z] TOOL RESULT

```
253 253
```


## [2026-10-16T05:20:21.781Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(u|w|ṷ|v)[a-z]{0,3}(is|ek)[a-z]{0,4}[ -]' IEC.txt | head -30; grep -n -i -E 'POISON|^ *[0-9]+\\.[0-9]+ +WISH' SYN.txt | head"
}
```


### [2026-10-16T05:20:22.337Z] TOOL RESULT

```
19590:ursis (ursis) *wickerwork, basket, withy’ Per. više (1) ‘ivy, woodbine’; Arm. uf, o-st. ‘vine-shoot’; uri, gs: -vo, ab. s. -eav, s. ‘willow’; Gk. hurrís, gs: -ídos, f. ‘basket’; Cz. vrš, f. *fish-basket, creel’; Pol. wiersza, f. id.; R vér3a, f. id. (Isophonic: Alb. urrë, f. 'sapwood")
19626:uadhis ‘pledge, surety’. WP I, 216 Lat. vas, gs: vadis, gp: vadum, mf. *bail, pled- ge’; Go. wadi, n. id.; OFris. wed, nd MHG wet, wete & wette, s & wn., id.; wette, adj. *paid-off; Ger. cf. wett sein ‘be quits’; Du. wedde, f. ‘salary’; Scots wad ‘bet, wager’; Icel. veð, n. ‘pledge’; Sw. cf. vädja, v. “appeal in court
19721:ualuis (ualdhuis?) “depression, lowland’ Lat. vallis & valles, f. “valley”; Ir. (?) faill, pl. -te, f. ‘cliff, precipice’; ON vollt, pl. vellir, m. low meadow’; uncertainly to MHG walt, gs: waldes, sm. ‘wood, forest’; OE weald, m. id.; Du. woud, n., Fris. wâld, n. id.
19887:ueis- “grow; growth, bud’. Cf. uois- (3), uis- (1). WP L 242 OE wise, s. ‘new shoot, bud'; ON vísir, pl. ‘shoots’; Li. veisiü, veísti, v. ‘produce’; cf.
19910:uek-, see uek- (2)
19912:ueks- “bend, turn” Mir feccaim, v. intr. ‘turn, bend; apply one- self; Ir. feacaim, tr. bend’; intr. ‘shrink’); Lat. cf. con-, in-vexus (lit. ‘turned up, — down"); MHG wéhsel, OHG & OS wéhsal, OFris. wixle, s. ‘change’. (Isophonic (?) in Gk. ixús, gs: -úos. f. ‘loins’: Alb. veshje, f. id.)
19916:uek- (1) (ueK-mi) ‘wish, beg, demand’. WP I, 244 Skt. vá$mi, v. id.; Av. vasomi, v. id.; cf. vaso, obl: vasáh-, n. ‘wil’ beside vasno, m. ‘wish’; Ober cf. vašna, f. “favour”; Hitt. wekmi “beg”; Gk. cf. hekón, act. pt. ‘willing’; a-ékon "un. willing’; a-éketi “against one's will
19918:ueks- ‘grow, thrive’. (ueks-?). Cf. aue-, eks-, uåks- and aueks-. Apparently a cpd. of pre- fixes. Cf. WP I, 23 and see next OPer. vaxi-, v. ‘grow’; Gk. aéxo, v. ‘make grow’; Li. vešiù, éti, v. “luxuriate, thrive’
19921:uek- — uel-
20065:uermis (uorm-, urm-) 'twisting creature, worm, insect’. WP I, 271 and next Skt. varmih, m. (a fish); cf. valmib, varmih and vamrih, f. ant: Lat. vermis, m. ‘worm’; Go. waürms, OHG wurm, OE worm, wurm Ar wyrm, m. id.; Li. varmas, m. “midge, horse- fly, winged ant’; cf. (alleged) Ukr. vermjanyj, adj. Cred lit. *worm-coloured' as Lat. ver- miculus, adj. & Cz. červený)
20157:uesis ‘existence, substance, matter’. Cf. ues- (2) Arm. go, gs: guji, ab. s: gujiv, s. ‘existence; goods’; Tokh. B wassi, wässi ‘material’; ON ver, n. ‘station’; veran, f. “existence, essence’; o-gde in MHG war, ware, sf. ‘wares, goods’, and com. W. Gmc.
20188:uestis (1) (uesnt-) “being, existence, abode’. Cf. ues- (2). WP I, 307 Skt. vastih, f. ‘sojourn, abode’ beside vasatíh, id. (see uesnt-); Tokh. wast, B ost, s. 'abode"; Olr. feiss, s. id.; W (?) gwest, pl. -i, -au, f. ‘visit’; Go. wists, f. ‘being, nature; OHG, MHG wist, i-st. f. ‘sojourn, lodging, home"; OE wist, f. as Go.; cf. hüs-wist, f. ‘home’; on-wist, f. ‘habitation’; ON vist, pl. -ir, f. ‘stay, abode’; Sw. cf. vistas, v. ‘reside’
20189:uestis (2) “feasting, food'. Same as (1) (?) Ir. feis, f. ‘feast’; feiste, f. accommodation, entertainment; W gwest, pl. -i, -au, f. (2) 'en-
20201:uestis (3) (uostis) “garment”. Cf. ues- (4) and next. WP I, 309 Skt. vastib, m. or f. lap of garment; Tokh A, B wastsi, wüstsi, s. ‘garment’; Lat. vestis, m. id.; Gk. dial. béston, bestion, n. id. beside Hesych. westía, id. and Gk. esthés, gs: -étos, f. id.; Arm. cf. z-gest, gs. ab. s. -u, s. id.; (o-gde in) Go. wasti, f. id.
20382:uis (1) “strength, youth'. Cf. guis, uis- (5) and uisàaió, eio. WP I, 229 (667) Gk. cf. í-phi, d. inst. pl. ‘by strength’; cf. also í-oulous, -onthos ‘youthful down": i-khór ‘lifeblood’; hi-drüo, v. ‘fix; an-ía ‘sorrow’; Lat. (acc.) vim, f. Å
20383:uis- (2) ‘colouring matter, dye’. WP I, 236. (Variant ui- ?) Gk. cf. i-sátis, gs: -satidos, f. (^woad', qua *uisntis ?); Lat. cf. vitrum, n. (2) ‘woad’; Ir. fis, f. ‘dye’; Go. cf. wiz-dils or -dila ‘weld, dyers weed'; (LLat. LW in waisda, f. id.; re- presenting an o-gde variant *uois-dha, as in G Waid, OE wad *woad"); E weld; Du. wouw, f. (LW in) Fr. gaude
20385:uis- (4) Av. viš-, v. ‘wet’; Hitt. wisis or wesis, s. *pas- ture’; W cf. gwaen, pl. gweunydd, f. ‘meadow’; Br. gæn, pl. -iu, f. (marsh”, fr. *uisin-); OHG wisa, f. ‘meadow’
20386:uis- (5) (uisis, os, uisuos, uisios, uisiuos) “all; totality’. WP I, 312. Cf. uis (1) Skt. cf. visvah, adj. Call each, every”, infl. by type vi$-); Av. cf. vispo, adj. "al": Medic vis-pa$, id.; Ober visa-, id.; Illyr. ves-, id.; Umb. sevum, acc. id., cpd. sev-akne ('every- year, annual’. Metath. for *ues-); OCS vísi, f: vísja, id. (and com. S1.); Li. visas, f: -à, id.; Latv. viss, id.
20388:uis — uisg-
20399:uis-dhlom, à (uisdhil-), extn. of type uis- (2), q. v. and cf. uis- (3) LLat. (LW fr. Gmc.) uuisdile-; Go. wizdila, f. *dyer's weed, weld: Du. cf. wouw (and LWs in Fr. gaude & Sp. gualda, with variant vocal- ism); EME welde, wolde 'yellow, dye, weld'. Uncertainly to OE widl, m. or n. “impurity”
20400:uisolos (1) (uislos) ‘poisonous, foul". Cf. uis- (3) and uisoros (1) Skt. (ambig.) visráh, adj. ‘musty’; Lat. cf. virul-entus ‘poisonous’. Cf. OE wode-wistle ‘hemlock’. (Isophonic: Mir fial ‘modest; W gwyl, id.)
20401:uisolos (2) (uislos, us) 'abundant, produc- tive’. Cf. uis (1) and ueis-, uois- WP I, 242 Ir. fial, adj. “generous, noble, clever’; Li. vis- lùs ‘fruitful’. (NB. Gk. hilaos, Arcadian Tl- ‘propitious; gay' is ambig. but digamma is not recorded. Cf. sila, is, above, in Sl. sila “strength? and prob. Lat. exilis, adj. “weak, and auxilium “aid”, if fr. *aug-siljiom)
20404:uisoros (2) ‘vigorous’. Cf. uisalos (2) and uis (1) Gk. dial. wiaros (epithet of órnis: “swift, dash- ing); W gwýr ‘vigorous, fresh, verdant’, Li. cf. vizgüs, adj. ‘active’
20405:uisg- (1) (uizg-) *haulm, stick, twig, bunch, faggot Lat. virga, f. ‘fod’; virgo, gs: -inis (“ virgin”, cf. Cz. hůl ‘roď’: holka, f. “girl); Ir. fiog, feog,
20408:uisg- (2); uisghnos; uisgheuor; uisghus, see supt: U W gwysg, adj. ‘headlong’; m. ‘trend, momen- tum’; MHG wischen, v. ‘dash’; Li. viskü, éti, v. ‘sway, tremble’; (variant in) Gk. íxalos, adj. ‘frisky, agile’. (Isophonic: Lat. viscus, gs: -eris, n. “vital organ’; viscera, pl.)
20414:uisg- — ultsis, os
5243:gg Cone, HEAD 4 PuysiclAN MepIcIne, Drue Poison (sb.
7128:Skt. vistha-, also vis- : visa-, Av. vis-, Grk. tés ‘poison’, Lat. virus ‘slime, se- men, poison, stench’, etc. Walde-P. 1.248 f.
7946:1. Grk. ¢dppaxoy (also ‘poison, en- chantment, etc.’), prob. : Lith. burti ‘practice sorcery’, Lett. burt ‘enchant’, root connection dub. Walde-P. 2.161.
7958:4. ON lyf esp. ‘herb with healing or magic power’, cpd. lekningarlyf, leknjs. lyf (: lekna ‘heal’), OE lybb also ‘oi- son’ = OHG luppi ‘poison, charm, sor- cery’, Goth. lubja- in lubja-leisei ‘gappa- keta, sorcery’: Ir. lub, NIr. luith ‘herb, plant’. Walde-P. 2.418. Falk. Torp 679.
7973:Kontamm, binim h wvords for ‘poison’, apart on an in- herited group, are in some cases the setae as those for ‘drug’ (4.88). movers or euphemistic expressions from ‘drink’ or tilt. Some are from wexbe meaning injure, pollute, consume or the like. Other sources are ‘love (potion)’, ‘(poi- son) of arrow’, ‘swelling’ (through ‘pus’), ‘(means of) death’. " 100) gy root connection dub. (possibly an IE specialization of ‘fluid’ to ‘poisonous fluid’, but evidence of an IE *weis- ‘flow’ meager). Walde-P. Ls f. Ernout-M. 1114. Grk. tés (poet.); Lat. virus (also any liquid, sperm’); Ir. fz; Skt. vzsa-, V. vis-, viga-, 2, Grk. ¢épyaxoy ‘drug’ (4.88) and Polson’, hence, fr. dim. form, NG ¢ap- Haxt ‘poison’, 3. Lat. venénum, earlier (ante-classi- cal) Potion, drug’, then (like Grk. gap- na Polson’ (> It. veleno, Sp. veneno, lites oe venin, OF r. velin, venim, (ito peer NE venom), prob. Wey ve Potion’) fr. *wenes-no- : Venus love’, Skt. van- ‘wish, desir. ae Emout-M. 1088: eee gain’, etc. pion on losigo, fr. Lat. toxicum vs and also ‘poison’ in
7977:4.89 POISON (sb.)
7979:Ce pappant wp Dan. gift ChSl. jadii, otrava N t penenums nee Sw. gift SCr. _ otrov (jed) Late peleno, t0sst OE ator, lybb_ Boh. je, otrova it poison, Peeotia, ME venim, potson, alter Pol. trucizna, jad Sp. penend, e NE poison (venom) Russ. jad, olrava
7988:Br. kontamm, back-formation fr. vb. kontammi ‘poison’ fr. Lat. contamindre ‘corrupt, pollute’. Henry 75.
7990:5. ON eitr, OE ator, attor, ME after, OHG eitar, MHG etter (NHG etter ‘pus’) : OHG ez ‘abscess, boil’, Grk. oldéw, Arm. attnum ‘swell’, prob. also ChSl. jadti, etc. ‘poison’ (below, 7). Walde-P. 1.166.. Falk-Torp 180.
7991:OE lybb ‘drug, poison’, OHG luppi ‘poison’, MHG lippe ‘astringent fluid, poisoning, sorcery’ : ON lyf ‘drug’, etc. (4.88).
```


## [2026-10-16T05:20:31.388Z] TOOL CALL #72: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe-private/site/pages/537.jpg 2>/dev/null; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 537 -l 537 -r 200 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg537 && echo ok"
}
```


### [2026-10-16T05:20:32.571Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   61k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/537.jpg
ok
```


## [2026-10-16T05:20:39.652Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg537.png"
}
```


### [2026-10-16T05:20:40.076Z] TOOL RESULT

```

```


## [2026-10-16T05:20:40.072Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-16T05:21:09.282Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 492 494 495 496 497 498 499 500; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1 {print \"=== LEAF\",n; print substr($0,1,90)}' BQT_v1_pages.txt; done"
}
```


### [2026-10-16T05:21:10.087Z] TOOL RESULT

```
=== LEAF 492
راد ب‌آمده
پز اد بر آهفه - زیی را گویند که
بسیار پیر شده باشد و سال بسیاری بر وگذشته
باشد 
=== LEAF 494
کنفه . کوبند که‌درخت‌پسته مکال میوه‌فزدار
بارآورد و یکسال بی‌مفز , وآنراکه بی‌مفز است
بزغن
=== LEAF 495
ی ۱۷
۵ » بفتح اول وثانی . بمحتی کناموخطا
باشد ٩‏ - و مردم نامراد ومسکین رانیز گوشد
و بمعنی
=== LEAF 496
بزمان ۲ بفتح اول بر وزن افنان .
غسگین و غمخوار و افرده رااگویند » ویضم‌اول
ح‌ آفقه ات
بر ه
=== LEAF 497
ایوان و مفه را گویند , و تک اول حم آهده
است .
بسك - بنتم اول و ثانی بالف کشیده
و بکاف زد» 
=== LEAF 498
بستان تم اول بروزن برهان » کلزار
و کلسان‌را کوشد , ومشفف بوستان هم‌هت كِ
و جابی‌را نیز کوی
=== LEAF 499
و افام رنگه برسوراج ها ذبکه ریزند؛ تانقشش
برآورد - و شخصی را نی زکویند که او را بحر
بته. ب
=== LEAF 500
و با بای عارسی نیز درست است -
بسقا یمن ۲ -بروزن پسندیدن»بمعنی
ساخته شدن و مهیا کشتن وآنلده
```


## [2026-10-16T05:21:12.668Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 496 497 498 499 500; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1 {print \"=== LEAF\",n; print}' BQT_v1_pages.txt | grep -n -E 'LEAF|^ ?بس|vas|was|بسنده|بسند|بسیار|kafi|کافی|اوستا|پهلوی'; done | head -50"
}
```


### [2026-10-16T05:21:13.361Z] TOOL RESULT

```
1:=== LEAF 496
8:بسربالی حربا خوانند .
38:و حسب باشد - و پمعثی بسیار ۷ - وبمئده هم
40:بسا - پر وزن رسا » بمعتی ای بس
42:بسارده ‌ بفتح اول و انی بالف کشیده
47:۲ - پهلوی ۷۵5 . پارسی
1:=== LEAF 497
4:بسك - بنتم اول و ثانی بالف کشیده
10:بسا ز لعج س بفتح اول ونون بروزنابارج»
14:بساو ند ۱ بروزن دمارند. فاف؛شر
17:بسباس ‏ بروزن کربای ۰ حرزه و بی
19:بسباسا؟ بن‌دوم بالف کشیده‌سربانی
27:بسیایه - با بای فارسی بروزن همابه »
35:بستن. است- وبمعنی سد - و بمعنی کوسوب‌عنی
38:بستاخ- بروزن و ممنی کستاخ است که
42:بستام « بکرار بروزن اسلام.جوهری
50:ستاق _ مکی اوز » اوستا. رل : اوستا و «مزدیسنا ۱۱۹ .
1:=== LEAF 498
2:بستان تم اول بروزن برهان » کلزار
11:بستان یر | -
13:بستان‌شی لن - نام توابی است از
15:بستاو لك » بفتح واو بروزن گل مانند؛
21:بستر ] هگ بر ارو سکون‌انی
29:بستر دن » بروزن حلبردن »نع وکردن
33:بستاث ح بضم اول بر وزن آردك » صمغ
37:بسع - بر وزن بدرو درطای تنم
41:بست‌و نك - کنابه از استعام وضط
1:=== LEAF 499
8:بستوه است که کهآ مده وملول باشدا - ونم
14:بستییاج" - بنتم اول و سکون ثانی
20:بس خواسته - کنابه از مطلوب
36:بسدك بفتح‌اول ونانی‌بروزن‌تگ رکه
43:بسر رشته‌دفتن -» کنابه از آمدن
44:بسرمخنی بودکه در ائنای گفتگو جملةٌ حعترضه
48:بسقده ۷ « بنتح اول و ثانی و سکون
1:=== LEAF 500
3:بسقا یمن ۲ -بروزن پسندیدن»بمعنی
7:بسفایج؟ « بفتح اول و بای‌حطی, لفظلی
9:بسك فتح اول و ثاني و سکون‌کاف»
20:بسله - بفتح اول و الث و سکون‌نانی»
22:بسصل « بکس اول و میم وسکون تافی
27:بستاسص" - با نون بروزن وسوای ۰ نم
34:لستك بت بر وزن سمل سزرآوار وکافی-
37:است که سزاوار و کافی - و تمام باشد 6
39:بسو 4 - بنم اول و انی و واو مجهول
42:بساو 6۵ - بکسرآول بروزن‌فزوده» بمعنی
48:9 مرا شفاعت این‌پنج‌تن بسنده بود
```


## [2026-10-16T05:21:15.342Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==497 {print}' BQT_v1_pages.txt | sed -n 30,60p; awk 'BEGIN{RS=\"\\f\"} NR==501 {print}' BQT_v1_pages.txt | sed -n 30,60p"
}
```


### [2026-10-16T05:21:15.922Z] TOOL RESULT

```
مجمود است بر خلاف حد ؛ چه حمود خواهد
که آن چیز او را باشد و آن شخص ححر وم
ما ؟ .
پس - بنم اول و سکون تابی » سیخی
باشد آهنی که بر آن کوش تکبا بکنند .وبعربی
سفود خوانند - و مخفف بوس هم هست کهعرب
قبله ۵ میگویند ٩‏ - و بفتح اول ترجه فقط
و حسب باشد - و پمعثی بسیار ۷ - وبمئده هم
آمده است ۸ - و امر بر قطع کردن هم حست
بسا - پر وزن رسا » بمعتی ای بس
را فا میگویند فد
بسارده ‌ بفتح اول و انی بالف کشیده
و سکون رای فرشت و فتح دال ابجد . زمینی
را گویند که بجهت چیزی کاشتن آب داده‌باشند . "
باره بفتح اول بی وزن هزاره »
۴ رك: پژهان. ٩‏ - منم اول و فتح سوم
۲ - پهلوی ۷۵5 . پارسی
لغات پارسی‌تو .
۵ ۸ . اس ۰۱۹۷ کیلکی شاقهت .
*۶- معرب‌آن‌ضا. شهری بفاری»
سنج ‌ بکسراول بروزن‌شکنج» خشکی
و داغی باشد که برروی واندام مردم افتد:» وآنرا
بمربی کلف خوانند - وامر برستج‌دن‌هم‌هست.
لستك بت بر وزن سمل سزرآوار وکافی-
و کفاف‌و کفایت‌را کوبند.و بمعنی‌تمام‌هم آهفه‌است.
لسیك ۵‏ بر وزن رونده » بمعنی پمند
است که سزاوار و کافی - و تمام باشد 6
باشفد .
بسو 4 - بنم اول و انی و واو مجهول
و فوفانی مفتوح » زلف راگوند ؛ و بکسر اول
ح‌ آهده است . ۶
بساو 6۵ - بکسرآول بروزن‌فزوده» بمعنی
دست‌زده ومالیده ولمس- ولامسه باشد ۷-وپعهتي
سوراخ کرده هم آمده است ۷ . * .
پایگ , رل : بس ‌یابه ۰
۴ - همرب‌بی
۴ - بتاي » نم استاد
9 مرا شفاعت این‌پنج‌تن بسنده بود
۱ - رك : بسودن ( حاشبه ) وپسودن .
( بر هان قابلع ۴«
```


## [2026-10-16T05:21:19.969Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E '^ *(BAS|BISYAR|BESYAR|BIŠ|BISH|VIRUS)\\b' ARY_latin_index_pages.txt | head; grep -n -i -E 'weis|wek|virus|basyar|besyar|bisyar' ARY_latin_index_pages.txt | head"
}
```


### [2026-10-16T05:21:20.494Z] TOOL RESULT

```
454:Trish ‘Weish Greek Latin Italian
1848:*KWEK., *KWOK-, *KWEKS (INDO-EUROPEAN) ,s2layy 9 4
4076:wopierta | tions abcd virus LATIN) os
4484:KWEKW, CUCHTAR COCERE AUTALIAN) gis!
7393:SCHWEISS, SCHWITZEN (KURDISH) 53,6
9960:BARNHART: (WHITE) 1233 WEISS GERMAN) galt
10979:j SHEST AARUSSIAN) guys HEKS, WEKS, HEX (GREEK) gly
14963:HWEK HITTITE) nen WAK (TOKHARIAN A) A 6555
14964:WEK :(TOKHARIAN B) B jis"
15224:FEN HOLD IRISH) 45 5-4) 2 WEKHTO, OCHEIN (GREEK) gli»
```


## [2026-10-16T05:21:22.355Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4070,4080p ARY_latin_index_pages.txt; grep -n -E 'ویروس|^بیش|بسیار' ARY_pages.txt | head"
}
```


### [2026-10-16T05:21:22.983Z] TOOL RESULT

```
BESH, WISH PAHLAVI) 5 Sy VISHA, VISH- HAVESTAN) gous!
[pdf page 143]
CSU Cos pe don | NE
‘REFERENCES they VISA, VIS- (SANSKRIT) 2 Sle
POKORNY = SSS*~*~*«wT Gs) ARMENIAN)
‘MACKENZIE: , * (POISON) 127 Tos (GREEK) gt y
wopierta | tions abcd virus LATIN) os
* | era igbidby Ww :(MIDDLE IRISH) ails .5-03 p\
aaa = ge Saad
fentlook
AY gel bd 23 cl ot
20:بسیاری از آنها غیر هند و اروپایی باشند. بهمین دلیل از آوردن اینگونه واژه‌ها خودداری کرده‌ام.
32:1 ٩-بسیاری‏ از ریشه‌یابی‌های موجود در این کتاب متکی به پژوهش‌های دانشمندان پیشین (به ویژه" ۱
91:موطلایی بسیار کمتر است.
123:نواحی زبان‌های اولیه این سّرزمین‌ها نبوده‌اند و توسط کوچگران به آنجا برده شده‌اند. ۳-بسیاری از
153:زندگی می‌کردند و بهمین دلیل زبان آنها پا فاقد گویش‌ها ی گوناگون بود و یاگویش‌های آن بهم بسیار
177:فرهنگی و زبانشناسی آنها را روشن می‌کند. بررسی کوچگری مردمان ترکك زبان مثال بسیار مفیدی
313:بیشتر روی همریشگی تاکید دارد نه هم چمی.
343:اروپائیان» بسیاری از بخش‌های اروپا و آسیا دارای بومیان اولیه بوده‌اند. در آبخست‌سانه‌ی (شبه
573:اروپایی پیشرفت بسیاری کرده است و دانشمندان ریشه مشترکك اکثر واژه‌های هند و آروپایی را (از
641:و ایرانی در زبان‌های مردم پین‌النهرین بسیار نادراند ولی پس از آن تاریخ شمار این واژه‌ها کم کم
```


## [2026-10-16T05:21:26.442Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 4055,4072p ARY_latin_index_pages.txt; grep -n -E 'WAS|VAS' ARY_latin_index_pages.txt | grep -i -E 'pahlavi|old persian|avestan' | head"
}
```


### [2026-10-16T05:21:26.947Z] TOOL RESULT

```
DVADSAT SLOVAK) S\ jlat DECAS, E{CHOSI (GREEK) ly
FICHE, HOLD IRISH) oS 54) p\ VIGNITI, VI-GINTI \ LATIN) ops
FICHET VINGT \PRENCH) sil
UCIENT WELSH) 1s) VEINTE (SPL Lil
VENTI HITALIAN) glial
REFERENCES beh DOUAZECI HRUMANIAN) ley ,
POKORNY: = SSSSSS«ST VINTE PORTUGUESE) gis 4
BARNHART: (TWENTY) 1178 TIGJUS, AGOTHIC) SE
DELAMARRE: (VINGT) 215 TWAITIGJUS
MACKENZIE: (TWENTY) 137) © (OLD SCANDINAVIAN) oS 5.
ONIONS: (TWENTY) 951 TUTTUGU
SKEAT: (TWENTY) 674 TWENTIG (OLD SAXON) oS gi y-Ste
AMINDAROY: (WENT) 302 TWINTICH (OLD FRISIAN) Ss.
TRAUPMAN: (TWENTY) 677 HOLD HIGH GERMAN), fg * ‘
re goo oly zueinzuc
BESH, WISH PAHLAVI) 5 Sy VISHA, VISH- HAVESTAN) gous!
[pdf page 143]
CSU Cos pe don | NE
1679:OLD HIGH GERMAN) 5 glsT VASTE, VASTRA-, :(AVESTAN) gus!
1681:WERIAN  :(OLD ENGLISH) gS godt WASTAR, (PAHLAVI) 5 34,
6152:AVAL, JAVAS (LITHUANIAN) ly} YAVA, YAVO AVESTAN) gles!
7117:r gst SUDYTT- (LITHUANIAN) gi 53 xWASTO HAVESTAN) glue
7118:XWASTAN PAHLAVI) 5 9h
10783:SAISPREZECE —-(RUMANIAN) gs, XSHVASH-DASA —{AVESTAN) gl!
10958:AXSAZ HOSSETIC) gue 3h XSHVASH HAVESTAN) glee 9)
11037:SIXTY ENGLISH) godSs| = XSHVASHTT AVESTAN) glory!
14984:oes CHEST a OWELSH) $3) VASTRQM, VASTRA-(AVESTAN) tus!
```


## [2026-10-16T05:21:31.263Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg537.png /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/537.png && echo ok"
}
```


### [2026-10-16T05:21:31.774Z] TOOL RESULT

```
ok
```


## [2026-10-16T05:24:22.889Z] TOOL CALL #81: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-537.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nU_WEYS = W + \"Reconstruction:Proto-Indo-European/weys-\"\nU_WEK = W + \"Reconstruction:Proto-Indo-European/weḱ-\"\nU_BISH = W + \"بیش\"\nU_BAS = W + \"بس\"\nU_BISYAR = W + \"بسیار\"\nU_BASANDA = W + \"بسنده\"\nU_VIRUS_FA = W + \"ویروس\"\nU_VIRUS = W + \"virus\"\nU_HEKON = W + \"ἑκών\"\nU_VISCUM = W + \"viscum\"\nU_BISON = W + \"bison\"\nU_WEASEL = W + \"weasel\"\nU_OOZE = W + \"ooze\"\nU_VISCOUS = W + \"viscous\"\nV = \"https://vajehyab.com/moein/\"\nU_MON_BISH, U_MON_VIRUS, U_MON_BAS, U_MON_BISYAR, U_MON_BASANDA = (V + w for w in [\"بیش\", \"ویروس\", \"بس\", \"بسیار\", \"بسنده\"])\nU_ABADIS_BISH = \"https://abadis.ir/fatofa/بیش/\"\n\nPOK_WEIS = {\"src\": \"POK\", \"where\": \"p. 1134 (POK_full.txt 'Root / lemma: ueis-3', Page(s):1134)\", \"stance\": \"supports\",\n            \"note\": \"'ueis-3 Meaning: to flow; poison ... Avestan viš-, viša- poison, vaēsah- mould, dank decay, Verwesung ... gr. ios = Latin vīrus ... Old English wāse, engl. ooze slime, mud ... Old High German wisunt ... (from dem Germanic derives Latin bison) ... engl. weasel ... perhaps moreover IE *uiks- Mistel ... Latin viscum'\"}\nWLD_WEIS = {\"src\": \"WLD\", \"where\": \"Bd. I (WLD_Bd1_pages.txt leaf 253; WP I 234 f.)\", \"stance\": \"supports\",\n            \"note\": \"'av. viš-, viša- „Gift“, vaēsah- „Moder, Verwesung“ (Bartholomae Airan. Wb. 1329 ...). Gr. ios „Gift“ = lat. virus „zähe Flüssigkeit, Schleim, Saft ... bes. Gift“ = ir. fí ... ags. wāse „Schlamm“'\"}\nAHD_WEIS = {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. weis- (AHD_watkins1985.txt l.1137-1140)\", \"stance\": \"partial\",\n            \"note\": \"'weis-. To flow. 1. Germanic *wisōn-, waisōn- in Old English wāse, mire, mud: OOZE2. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is ... *wis-o- in Latin vīrus ... 3. Extended zero-grade form *wisk- possibly in Latin viscum ... II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words for strong-smelling animals ... *wisulōn- ... WEASEL ... *wisand- ... BISON. [Pok. 3. weis- 1134.]'\"}\nSYN_POISON = {\"src\": \"SYN\", \"where\": \"§4.89 POISON (SYN.txt l.7128, 7973)\", \"stance\": \"partial\",\n              \"note\": \"Buck: 'Skt. viṣa-, Av. viš-, viša-, Grk. ios, Lat. vīrus ... root connection dub. (possibly an IE specialization of \\\"fluid\\\" to \\\"poisonous fluid\\\", but evidence of an IE *weis- \\\"flow\\\" meager). Walde-P. 1.248 f.'\"}\nIEC_WEIS = {\"src\": \"IEC\", \"where\": \"IEC.txt l.20400 s.v. uisolos (1)\", \"stance\": \"partial\",\n            \"note\": \"Mann: 'uisolos (1) poisonous, foul. Cf. uis- (3) ... Skt. visráh musty; Lat. cf. virul-entus' - Mann sets up a separate *uis- 'poison' base rather than one root 'flow'.\"}\n\nentries = []\n\n# ---------------- entry 0 : Weis ----------------\ne0_nodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vaeša; viš 1, viša\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Avestan vaēšah- n. 'mould, decay, putrefaction' (Bartholomae col. 1329, compared with OHG wesanēn 'to rot') is the full-grade s-stem *wóys-/wéys-es- of PIE *weys- 'to flow; rot', and Avestan viš- / viša- n. 'poison' (Bartholomae s.v. viša-, = Skt. viṣá-) continues the zero-grade *wis-ó-, the same formation as Latin vīrus and Greek ios. Nourai's gloss 'rotten food' for viš is loose (the attested sense is 'poison'), but forms, language and descent are correct.\",\n  \"derivation_fa\": \"واژه‌های اوستایی vaēšah- «کپک، پوسیدگی» و viš- / viša- «زهر» هر دو از ریشهٔ هندواروپایی آغازین *weys- «روان شدن، گندیدن» اند: نخستی با درجهٔ کامل و پسوند -ah-، دومی با درجهٔ صفر *wis-ó- که هم‌ریشهٔ سنسکریت viṣa «زهر»، یونانی ios و لاتین vīrus است. بارتولمه (ستون ۱۳۲۹) vaēšah- را «پوسیدگی، Moder» و viša- را «زهر» معنا کرده است. ادعای نورایی درست است؛ تنها معنای «خوراک گندیده» برای viš دقیق نیست.\",\n  \"sources\": [U_WEYS, U_VIRUS],\n  \"ref_check\": [\n   {\"ref\": \"POK:1134\", \"status\": \"supports\", \"note\": \"POK_full.txt 'ueis-3 ... Page(s):1134': 'Avestan viš-, viša- poison, vaēsah- mould, dank decay, Verwesung'.\"},\n   {\"ref\": \"KLN:1714\", \"status\": \"supports\", \"note\": \"Klein s.v. virus (1966 two-volume file is truncated before 'v', read in KLN_1971.txt l.262734): 'L. virus, poison ... fr. I.-E. base *weis-, to melt away, rot, whence also OI. viṣám, poison ... Avestic viš-, visha-, poison, vaēshah-, mold, Gk. ios'. Exactly Nourai's Avestan forms and the root gloss 'melt away, rot'.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1329 s.v. vaēšah-; s.v. viša- (BRT.txt leaves 731, 806)\", \"stance\": \"supports\", \"note\": \"'vaēšah- n. Moder, Verwesung; Ort der Verwesung ... Vgl. ahd. wesanēn faul werden'; 'viša- n. Gift ... ai. viṣá- n.; vgl. mp. viš, np. bēš (wozu Hbm. PSt 270)'.\"},\n   WLD_WEIS, POK_WEIS\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"běš 2\", \"verdict\": \"plausible\",\n  \"derivation\": \"MacKenzie lists two separate Pahlavi words: bīš [byš] 'aconite' (CPD p.18) and bēš 'pain, sorrow; harm, hostility'. The plant name is the one meant here; Pahlavi script does not distinguish ē and ī, so Nourai's reading bēš is an alternative reading, not a misprint. Its source is disputed. Wiktionary (citing MacKenzie, Laufer, Ačaṙean) and Laufer (Sino-Iranica 582: 'biš, halāhil, aconite. Hindi biš, Skr. viṣā (Aconitum ferox), from viṣa poison') derive it from an Indic word, i.e. a loan of the Himalayan aconite's name, not the inherited continuation of Av. viša- (that is MP wiš 'poison', MacKenzie p.92). Hübschmann (PSt 270) notes against Geiger's equation with Skt. viṣa- that 'Pahlavi and Armenian give bēš as the older form (not viš)'. Either way the word goes back to Indo-Iranian *wiša- < PIE *weys-, so the root is right but the arrow 'Avestan → Pahlavi' is not the accepted route. The chart's NOTE ('See Dwei') refers to the homonym MP bēš 'harm, hostility' < Av. ṭbaēšah- (PIE *dwey-). That is a different word from bīš 'aconite' and does not change the plant name's etymology.\",\n  \"derivation_fa\": \"در پهلوی دو واژهٔ جدا هست: bīš «گیاه بیش، آکونیت» (مکنزی، ص ۱۸) و bēš «درد، آزار، دشمنی». چون خط پهلوی میان ē و ī فرقی نمی‌گذارد، خوانش bēš نورایی خطای چاپی نیست. ولی بیشترِ پژوهشگران (لاوفر، ویکی‌واژه) bīš را وام‌واژه‌ای هندی از سنسکریت viṣā «آکونیت» می‌دانند، نه بازماندهٔ مستقیم viša- اوستایی؛ بازماندهٔ آن در پهلوی wiš «زهر» است. هوبشمان نیز یادآور می‌شود که صورت کهن‌تر در پهلوی و ارمنی bēš است نه viš. یادداشت نمودار («Dwei» را ببینید) به همنام دیگر، bēš «آزار» از اوستایی ṭbaēšah- (ریشهٔ *dwey-)، مربوط است. پس ریشهٔ نهایی (*weys-) درست است، ولی راهِ «اوستایی ← پهلوی» را باید با احتیاط پذیرفت.\",\n  \"sources\": [U_BISH, U_ABADIS_BISH],\n  \"ref_check\": [\n   {\"ref\": \"BQT:338\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt 0-based leaf 558 (printed p.338) s.v. بیش: 'بیخی است مهلک و کشنده'; Mo'in's footnote (OCR): '۱ - بدین معنی در پهلوی bēš ... در اوستا viša بمعنی زهر است. در تحفهٔ حکیم مؤمن آمده: «بیش: بهندی بش نامند» ... معرب آن نیز «بیش» است'. Mo'in gives the Pahlavi bēš and Av. viša exactly as Nourai does, but he also quotes the Hindi name biš, which supports the Indic-loan view.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 18 s.v. bīš; s.v. bēš; p. 92 s.v. wiš (PHD_mackenzie.txt leaf 39, l.1559; PHD.txt l.655)\", \"stance\": \"partial\", \"note\": \"'bīš [byš | N ~] aconite.' separate from 'bēš [byš] pain, sorrow; harm, hostility' and 'wiš [w(y)š | M wyš, N guš] poison, venom, bile'. MacKenzie shows the plant word but gives no derivation; the inherited reflex of viša- is wiš.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary pp. ~45 s.v. bēš-burtār, bēšēnītār, besōmand (NYB_vol2_glossary.txt l.991-994)\", \"stance\": \"silent\", \"note\": \"Only bēš 'pain, grief' derivatives ('bēšēnītār causing pain', 'besōmand grieved, afflicted'); no entry for the aconite word.\"},\n   {\"src\": \"HUB\", \"where\": \"p. 270 (HUB.txt leaf 280)\", \"stance\": \"partial\", \"note\": \"'p. 34. Geiger setzt ... np. bēš Aconitum = skr. viṣa- Gift, viṣā- ein Aconitum. Aber Pehl. und Armen. geben bēš als ältere Form (nicht viš oder vīš).'\"},\n   {\"src\": \"SIN\", \"where\": \"p. 582 (SIN.txt l.4028)\", \"stance\": \"contradicts\", \"note\": \"Laufer: '13(85). biš, halāhil, aconite (Aconitum). Hindi biš, Skr. viṣa (Aconitum ferox), from viṣa, \\\"poison\\\"' - i.e. an Indian loan, not an inherited Iranian word.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"bîš 2\", \"verdict\": \"plausible\",\n  \"derivation\": \"NP بیش bīš 'aconite, Aconitum ferox (a deadly poisonous root)' continues MP bīš (MacKenzie p.18 'N ~'). Arabic bīš and Middle Armenian bēš/biš are borrowed from Persian. As with node #2, the Persian word goes back to Indo-Iranian *wiša- 'poison' (PIE *weys-), but most likely through an Indic name: Skt viṣā 'Aconitum ferox', Hindi biš/bikh, which also gave Anglo-Indian bikh. It is not the regular inherited development of Av. viša-. Inherited OIr. *wiša- gives MP wiš, and Horn notes that old vi- 'consistently becomes gu-' in NP. So the root is right, but the route via Avestan is uncertain.\",\n  \"derivation_fa\": \"«بیش» در فارسی نو نام گیاهی بسیار زهرآگین (آکونیت، Aconitum ferox) است و از پهلوی bīš آمده است؛ «بیش» عربی و bēš ارمنی میانه از فارسی وام گرفته شده‌اند. لاوفر و ویکی‌واژه آن را وام‌واژه از سنسکریت viṣā «آکونیت» (هندی biš/bikh) می‌دانند. بازماندهٔ موروثیِ viša- اوستایی در پهلوی wiš است، و به گفتهٔ هرن، vi- کهن در فارسی نو به gu- بدل می‌شود، نه به bī-. ریشهٔ هندواروپایی *weys- درست است، ولی گذر مستقیم از اوستایی به فارسی را تنها با احتیاط می‌توان پذیرفت. در برهان قاطع، معین صورت پهلوی bēš و اوستایی viša را آورده و از تحفهٔ حکیم مؤمن نقل کرده که «بهندی بش نامند».\",\n  \"sources\": [U_BISH, U_MON_BISH, U_ABADIS_BISH],\n  \"ref_check\": [\n   {\"ref\": \"BQT:338\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt 0-based leaf 558 (p.338): headword بیش 'بیخی است مهلک و کشنده'. Footnote gives 'پهلوی bēš ... در اوستا viša بمعنی زهر است', plus Tuhfa: 'بیش: بهندی بش نامند ... که هلاهل نامند'. This is the source of Nourai's chain, and it also records the Indian name.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab Mo'in s.v. بیش\", \"stance\": \"silent\", \"note\": \"Online Mo'in shows only 'بیش [په.] (ق.) افزون، زیاد' (the homonym 'more'); the aconite entry is not shown online.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 142-143]\", \"stance\": \"supports\", \"note\": \"Aryanpur's entry for بیش lists 'BESH, WISH (PAHLAVI); VISHA, VISH- (AVESTAN); VISA, VIS- (SANSKRIT); ios (GREEK); virus (LATIN); fí (MIDDLE IRISH)' with refs 'POKORNY', 'MACKENZIE (POISON)'. It puts bīš under the same PIE root.\"},\n   {\"src\": \"HRN\", \"where\": \"p. ~39 (HRN.txt l.2622-2624, under no. 260 bīmār)\", \"stance\": \"partial\", \"note\": \"Horn has no bīš entry, but states 'altes vi- im Neupersischen consequent zu gu- wird'. That makes a direct inherited Av. viša- > NP bīš irregular.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. bikh (KLN_1966.txt l.4973)\", \"stance\": \"supports\", \"note\": \"'bikh, bish, n., aconite poison (Anglo-Ind.) - Hind., fr. OI. viṣam, poison, which is cogn. with Gk. ios, L. virus'. This gives the Indic name of the same plant.\"},\n   {\"src\": \"SIN\", \"where\": \"p. 582\", \"stance\": \"partial\", \"note\": \"'biš, halāhil, aconite. Hindi biš, Skr. viṣa (Aconitum ferox)': the Persian (and Arabic) name taken from India.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"virus; viscum\", \"verdict\": \"disputed\",\n  \"derivation\": \"virus: confirmed. Latin vīrus n. 'slimy liquid, poison' < Proto-Italic *weizos < PIE *wisós (rhotacism of intervocalic -s-), the exact match of Greek ios (< *wisos) and Skt viṣá-. AHD (Watkins) notes it may be 'an independent IE word' rather than a derivative of 'flow', but Pokorny, Klein, Walde-Pokorny and Wiktionary all put it under *weys-. viscum: disputed. Latin viscum means 'mistletoe; birdlime', not 'slime'. Pokorny lists it only as 'perhaps moreover IE *uiks- Mistel' (with Greek ixos, OHG wīhsila). Wiktionary: 'Perhaps from PIE *weyḱs- ... Traditionally associated with vīrus, although this is unlikely.' AHD has only 'possibly'. So the modern view keeps viscum apart from *weys-.\",\n  \"derivation_fa\": \"واژهٔ لاتین vīrus «مایع لزج، زهر» از ایتالیک آغازین *weizos و هندواروپایی *wisós است (s میان دو واکه در لاتین به r بدل شده) و هم‌ریشهٔ یونانی ios و سنسکریت viṣa است؛ این بخش درست است. اما viscum در لاتین به معنای «دارواش (گیاه انگلی) و چسب پرنده‌گیری» است، نه «لجن». پوکورنی آن را تنها با «شاید» زیر ریشهٔ جداگانه‌ای (*uiks- «دارواش»، هم‌ریشه با یونانی ixos) آورده است، و ویکی‌واژه پیوند آن با vīrus را «بعید» می‌داند. پس دربارهٔ viscum پژوهش امروزی نظر نورایی را نمی‌پذیرد.\",\n  \"sources\": [U_VIRUS, U_VISCUM, U_WEYS],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. weis-: 'Taken by many as a derivative of this root, but probably an independent Indo-European word, is ... *wis-o- in Latin vīrus ... Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS.' AHD lists both words, with reservations.\"}\n  ],\n  \"consulted\": [\n   POK_WEIS, WLD_WEIS,\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. uīrus / uiscum\", \"stance\": \"silent\", \"note\": \"Not checked in detail; Buck SYN cites 'Ernout-M. 1114' for virus with the same root doubt.\"},\n   SYN_POISON,\n   {\"src\": \"KLN\", \"where\": \"s.v. virus, viscid, Viscum (KLN_1971.txt l.262734, 262810, 262849)\", \"stance\": \"partial\", \"note\": \"virus 'fr. I.-E. base *weis-, to melt away, rot'; viscid 'fr. L. viscum, mistletoe, birdlime' and Viscum 'mistletoe; birdlime' - Klein does not derive viscum from *weis-.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"French\", \"words\": \"virus\", \"verdict\": \"confirmed\",\n  \"derivation\": \"French virus (16th c., medical 'venom, infectious matter') is a learned borrowing of Latin vīrus. In the late 19th century Pasteur's school used it for infectious agents, and that sense spread to the other European languages.\",\n  \"derivation_fa\": \"واژهٔ فرانسوی virus در سدهٔ شانزدهم به‌صورت وام‌واژهٔ علمی از لاتین vīrus گرفته شد و در سدهٔ نوزدهم، در پزشکی فرانسه (مکتب پاستور)، معنای «عامل بیماری‌زای واگیر» یافت. ادعای نورایی درست است.\",\n  \"sources\": [U_VIRUS, U_VIRUS_FA],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. virus (KLN_1971.txt l.262734)\", \"stance\": \"supports\", \"note\": \"'virus ... L. virus, poison' (French intermediary implied for the medical sense).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. VIRUS\", \"stance\": \"silent\", \"note\": \"Skeat's concise entry gives L. uīrus only.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Persian\", \"words\": \"vîrŭs\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP ویروس vīrus is a 20th-century borrowing of French virus. The spelling with و = v and the stress on the last syllable follow French. Mo'in tags it [فر.] 'French'; Wiktionary gives Ottoman ویروس (virüs) the same French origin.\",\n  \"derivation_fa\": \"«ویروس» در فارسی امروز وام‌واژه‌ای فرانسوی (virus) است که در سدهٔ بیستم همراه با دانش پزشکی نو به فارسی آمد؛ فرهنگ معین آن را با نشانهٔ [فر.] آورده است. ادعای نورایی درست است.\",\n  \"sources\": [U_VIRUS_FA, U_MON_VIRUS],\n  \"ref_check\": [{\"ref\": \"MON:5070\", \"status\": \"supports\", \"note\": \"Page not checkable online; vajehyab Mo'in s.v. ویروس: '[ فر. ] (اِ.) موجود بسیار ریزی که باعث بروز بیماری می شود' - French origin as drawn.\"}],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"vajehyab s.v. ویروس\", \"stance\": \"supports\", \"note\": \"'[فر.]' = French.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt [pdf page 143]\", \"stance\": \"silent\", \"note\": \"Aryanpur lists Latin virus only as a cognate of بیش; no entry for the loanword ویروس.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"virus; viscous\", \"verdict\": \"plausible\",\n  \"derivation\": \"English virus (late 14th c. 'venom', 1880s-90s 'infective agent') is taken directly from Latin vīrus, with the modern sense later reinforced from French. Confirmed. English viscous (c.1400) < Anglo-French viscous < Late Latin viscōsus 'sticky' < viscum 'birdlime'. The Latin → English edge is correct, but because viscum's attachment to *weys- is doubtful (node #4), viscous is only plausibly a member of this family.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی virus (سدهٔ چهاردهم به معنای «زهر» و از پایان سدهٔ نوزدهم به معنای «ویروس») مستقیم از لاتین vīrus آمده است و درست است. viscous «چسبناک» از لاتین متأخر viscōsus و آن از viscum «چسب پرنده‌گیری، دارواش» است. گذر از لاتین به انگلیسی درست است، ولی چون پیوند viscum با ریشهٔ *weys- مشکوک است، جای viscous در این خانواده تنها با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_VIRUS, U_VISCOUS],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. virus, viscous (KLN_1971.txt l.262734, 262845)\", \"stance\": \"partial\", \"note\": \"'virus ... L. virus, poison ... fr. I.-E. base *weis-'; 'viscous, adj., sticky. - Late L. viscosus. See viscose' (from viscum, no root given).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (l.2455-2456)\", \"stance\": \"partial\", \"note\": \"'VIRUS weis-', 'VISCID weis-', 'VISCOUS weis-' - listed under weis-, but in the entry viscum is only 'possibly' from *wisk-.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Germanic\", \"words\": \"wisôn; wisolon; wisand\", \"verdict\": \"plausible\",\n  \"derivation\": \"Proto-Germanic *wais-ō(n)- / *wis-ōn- 'slime, mud' (OE wāse 'mire', ON veisa 'stagnant pool', OS wāso) is accepted by Pokorny, Watkins and Wiktionary as a derivative of *weys- 'flow'. Confirmed. *wisulōn- 'weasel' (OE weosule, OHG wisula) and *wisund-/*wisand- 'bison, wisent' (OHG wisunt, ON vísundr) are attached to the root by Pokorny ('after the smell'), but Watkins says they are 'attributed by some to this root, but more likely of obscure origin', and Klein derives weasel from an imitative *wis- 'to break wind' (cf. L. vissio 'stench'). Nourai's starred forms are close to the reconstructions (*wisōn ~ *waisōn, *wisulōn, *wisand-). Overall: plausible.\",\n  \"derivation_fa\": \"صورت ژرمنی آغازین *waisō(n)- / *wisōn- «لجن، گل» (انگلیسی کهن wāse «گِل و لای»، نوردی کهن veisa «آب ایستادهٔ گندیده») را پوکورنی و واتکینز و ویکی‌واژه از ریشهٔ *weys- «روان شدن» می‌دانند و این درست است. اما *wisulōn- «راسو» و *wisand- «گاومیش اروپایی» را پوکورنی به سبب بوی تندشان به همین ریشه بسته است، در حالی که واتکینز آن‌ها را «احتمالاً با ریشهٔ ناروشن» می‌داند و کلاین «راسو» را از ریشهٔ آوانمای *wis- «باد در کردن» می‌شمارد. پس این گره با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_OOZE, U_WEASEL, U_BISON, U_WEYS],\n  \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. weis-: 'Germanic *wisōn-, waisōn- in Old English wāse, mire, mud: OOZE2 ... II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words for strong-smelling animals. 1. Germanic *wisulōn- ... WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, European bison (which emits a musky smell in the rutting season) ... BISON.' Nourai follows this entry, including the 'musky smell' gloss, but leaves out Watkins's reservation.\"}\n  ],\n  \"consulted\": [\n   POK_WEIS,\n   {\"src\": \"KLN\", \"where\": \"s.v. bison (KLN_1966.txt l.5066); s.v. weasel (KLN_1971.txt l.265597)\", \"stance\": \"partial\", \"note\": \"bison: 'fr. OHG. wisunt ... cogn. with OPruss. wis-sambrs, aurochs, and with L. vissio, stench. The bison is named after the peculiar odor of musk ...'; weasel: 'prob. diminutives formed fr. Teut. *wis(j)ō-, fitchew ... derive from the I.-E. imitative base *wis-, to break wind' - not *weis- 'flow'.\"},\n   WLD_WEIS,\n   {\"src\": \"SKT\", \"where\": \"s.v. OOZE / WEASEL\", \"stance\": \"silent\", \"note\": \"Skeat gives OE wāse / wesle without IE root.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"English\", \"words\": \"ooze 2; weasel; bison\", \"verdict\": \"plausible\",\n  \"derivation\": \"ooze 2 'soft mud, mire' < ME wose < OE wāse < PGmc *waisǭ: native, confirmed (Klein distinguishes it from ooze 1 'sap, juice' < OE wōs). weasel < ME wesele < OE weosule/wesle < PGmc *wisulǭ: native; its link to *weys- is doubtful (node #8). bison is not inherited in English. It came in through Latin bisōn (pl. bisontes, attested in Pliny and Martial), a borrowing from Germanic *wisund-, then French bison, ME bysontes (Wiktionary: 'from Latin bisōn, bisōnt-, from Proto-Germanic *wisundaz'). So the arrow from the Germanic box directly to English bison skips the Latin-French stage.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی ooze (به معنای دوم «گِل و لای») از انگلیسی میانه wose و انگلیسی کهن wāse و ژرمنی آغازین *waisǭ است و درست است. weasel «راسو» از انگلیسی کهن weosule است، ولی پیوندش با *weys- مشکوک است. bison واژهٔ موروثی انگلیسی نیست: لاتین bisōn آن را از ژرمنی *wisund- وام گرفت و این واژه از راه فرانسه به انگلیسی رسید. پس پیکان مستقیم از ژرمنی به انگلیسی، گذر از لاتین و فرانسه را نادیده گرفته است. در مجموع با احتیاط پذیرفتنی است.\",\n  \"sources\": [U_OOZE, U_WEASEL, U_BISON],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited by Nourai for this node.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. ooze (KLN_1966.txt l.26348-26352); s.v. bison (l.5066)\", \"stance\": \"supports\", \"note\": \"'ooze, n., soft mud, mire. - ME. wose, fr. OE. wāse, soft mud, mire'; 'bison, n., wild ox. - F., fr. L. bison, fr. OHG. wisunt' (via Latin and French, not direct).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index (l.1306, 1983)\", \"stance\": \"partial\", \"note\": \"'BISON weis-', 'OOZE2 weis-'; in the entry the animal words are 'more likely of obscure origin'.\"}\n  ]\n }\n]\n\nentries.append({\n \"entry\": 0,\n \"root\": \"Weis\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *weys- 'to flow; to melt away, rot' (Pokorny 3. u̯eis- 1134, 'to flow; poison'; Watkins weis- 'to flow'; LIV 2.*u̯ei̯s-), with *wisós 'poison'\",\n \"note\": \"The root box is correct: Pokorny p.1134 '3. u̯eis- to flow; poison' and Klein s.v. virus 'I.-E. base *weis-, to melt away, rot' give exactly Nourai's gloss. Buck (4.89) and Watkins add that the poison word *wisós (Skt viṣa, Av. viša, Gk ios, L. vīrus) may be a separate IE word, since evidence for 'flow' is meagre. Weaker branches: (1) Latin viscum 'mistletoe, birdlime' (not 'slime') probably belongs to *weyḱs-/*uiks- with Greek ixos, not to *weys- (Wiktionary, Pokorny 'perhaps'); (2) the Germanic weasel/bison words are only doubtfully connected (Watkins: 'more likely of obscure origin'; Klein: imitative *wis- 'break wind'); (3) English bison came via Latin and French, not directly from Germanic; (4) Persian bīš / Pahlavi bīš 'aconite' is most likely an Indic loan (Skt viṣā 'Aconitum ferox', Hindi biš; Laufer, Wiktionary) rather than an inherited descendant of Av. viša- (whose MP reflex is wiš). Nourai's reading bēš is a legitimate reading of Pahlavi byš (MacKenzie reads bīš). The chart's NOTE points to *dwey- for a homonym (MP bēš 'harm' < Av. ṭbaēšah-), which is a different word from the plant name. The JSON matches the printed page (checked against the page image); no extraction errors.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *weys- «روان شدن، گداختن، گندیدن» (پوکورنی ۱۱۳۴: «روان شدن؛ زهر») و معنای آن را نورایی درست آورده است، و کلاین نیز همین معنا را داده است. باک و واتکینز یادآور می‌شوند که واژهٔ «زهر» (*wisós: سنسکریت viṣa، اوستایی viša، یونانی ios، لاتین vīrus) شاید واژه‌ای مستقل باشد. ایراد در چند شاخه است: viscum لاتین («دارواش، چسب پرنده‌گیری») احتمالاً از ریشهٔ دیگری است؛ پیوند «راسو» و «گاومیش اروپایی» ژرمنی با این ریشه مشکوک است؛ bison انگلیسی از راه لاتین و فرانسه رسیده است؛ و «بیش» فارسی (پهلوی bīš، نام گیاه آکونیت) به احتمال زیاد وام‌واژه‌ای هندی از سنسکریت viṣā است، نه بازماندهٔ مستقیم viša- اوستایی، که بازمانده‌اش در پهلوی wiš است. یادداشت نمودار دربارهٔ ریشهٔ «Dwei» به همنام دیگر، bēš «آزار»، مربوط است. خطای استخراج دیده نشد.\",\n \"sources\": [U_WEYS, U_VIRUS, U_BISH],\n \"ref_check\": [{\"ref\": \"POK:1134\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: ueis-3 Meaning: to flow; poison ... References: WP. I 234 f. ... Page(s):1134'.\"}],\n \"consulted\": [WLD_WEIS, AHD_WEIS, SYN_POISON, IEC_WEIS],\n \"nodes\": e0_nodes\n})\n\n# ---------------- entry 1 : Wek ----------------\nKNT_VASIY = {\"ref\": \"KNT:207\", \"status\": \"supports\", \"note\": \"KNT_full.txt l.28847 (Lexicon p.207): 'vasiy adv. at will, greatly, utterly; as indecl. sb., much: Sas. Pahl. vas, NPers. bas; loc. of root-sb. vas- ... to pIE root *u̯ek̑-, GAv. vasəmi I wish, Gk. (Cretan) wekōn willing'; l.28863 'vašna- sb. will, favor: Av. vasna-; deriv. of root vas- wish'.\"}\nPOK_WEK = {\"src\": \"POK\", \"where\": \"p. 1135 (POK_full.txt 'Root / lemma: u̯ek̑-, Meaning: to wish', Page(s):1135)\", \"stance\": \"supports\", \"note\": \"'Old Indic vaś-mi, uś-masi, Avestan vasəmī, usəmahī ... participle ... Avestan an-usant- widerwillig ... Avestan vasah- (nom. vasō) wollend ... ap. vašna, Avestan vasnā (instr.) after dem Willen ... gr. hekōn (Cretan wekōn) freiwillig, aekōn wider Willen'.\"}\nWLD_WEK = {\"src\": \"WLD\", \"where\": \"Bd. I (WLD_Bd1_pages.txt leaf 253; WP I 244 f.)\", \"stance\": \"supports\", \"note\": \"'u̯ek̑- „wollen, wünschen“. Ai. vaś-mi ..., av. vasəmī, usəmahī ... av. an-usant-, -usaitī „widerwillig, ohne es zu wollen“, av. vasah- ... ap. vašnā; av. vasnā (i. sg.) „nach dem Willen“'.\"}\nIEC_WEK = {\"src\": \"IEC\", \"where\": \"IEC.txt l.19916 s.v. uek- (1)\", \"stance\": \"supports\", \"note\": \"'uek- (1) wish, beg, demand. WP I, 244. Skt. vaśmi; Av. vasəmi; vasō, obl. vasah-, n. will beside vasnō, m. wish; OPer. vašna, f. favour; Hitt. wekmi beg; Gk. hekōn willing; a-ekōn unwilling'.\"}\n\ne1_nodes = [\n {\n  \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"vas; vašna; vasiy\", \"verdict\": \"confirmed\",\n  \"derivation\": \"OP root vas- 'to wish' (attested only in derivatives), vašna- 'will, favour' (instrumental vašnā Auramazdāha 'by the favour of Ahuramazda', PIE *wéḱ-no-, with -šn- from *-ḱn-), and vasiy adv. 'at will, greatly, much' (locative of the root noun vas-) all come from PIE *weḱ- 'to wish', Iranian *wac-/*was- with PIE palatal *ḱ > Ir. s. Kent p.207 states the derivation explicitly, adding 'Sas. Pahl. vas, NPers. bas'.\",\n  \"derivation_fa\": \"در پارسی باستان، از ستاک vas- «خواستن» دو واژه به‌جا مانده است: vašna- «خواست، فضل» (در عبارت vašnā Auramazdāha «به خواست اهورامزدا») و قید vasiy «به دلخواه، بسیار». هر دو از ریشهٔ هندواروپایی آغازین *weḱ- «خواستن» اند؛ ḱ کامی هندواروپایی در ایرانی به s بدل شده است. کنت (ص ۲۰۷) همین را آورده و پهلوی vas و فارسی «بس» را از همین ریشه دانسته است. ادعای نورایی درست است.\",\n  \"sources\": [U_WEK],\n  \"ref_check\": [KNT_VASIY,\n   {\"ref\": \"BST:234\", \"status\": \"supports\", \"note\": \"BST.txt (Horn, 'Some Inscriptions...', OP glossary, 0-based leaf 252, around p.234-236): 'vashna-, sb. m, wish, grace; instr. sg. -ā by the grace (of Ahuramazda); Aw. vasna'.\"}],\n  \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1381 s.v. vas- V. 'wollen'; s.v. vašna-/vasna- (BRT.txt leaf 759)\", \"stance\": \"supports\", \"note\": \"'j., g. vas- V. wollen ... wollen, wünschen'; 'p. vašnā, j., g. vasna- m. Wille'.\"},\n   {\"src\": \"TLM\", \"where\": \"s.v. vašna-, vasiy\", \"stance\": \"silent\", \"note\": \"Not consulted in detail; Kent is the standard and is explicit.\"},\n   POK_WEK\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vas; vas-yâr\", \"verdict\": \"confirmed\",\n  \"derivation\": \"MP was [KBD; ws] 'much, many, enough' continues OP vasiy (Kent: 'Sas. Pahl. vas'). In MP the sense shifts from 'at will, as much as one wishes' to 'much; enough'. MP wasyār [wsy(k)ʾl] 'much, many' is built on the same base. Nyberg: 'vasīkār, vasiyār numerous ... NP bisyār; from vasiy, but the forms are not clear'. Hübschmann reconstructs OP *vasi-ādāra-, uncertain.\",\n  \"derivation_fa\": \"واژهٔ پهلوی was/vas «بسیار، فراوان، بس» بازماندهٔ قید پارسی باستان vasiy است و معنایش از «به دلخواه» به «بسیار، بسنده» گسترده شده است. wasyār «بسیار» نیز بر همین پایه ساخته شده است (مکنزی، ص ۸۸؛ نیبرگ). ادعای نورایی درست است.\",\n  \"sources\": [U_BAS, U_BISYAR],\n  \"ref_check\": [\n   KNT_VASIY,\n   {\"ref\": \"BQT:276\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt 0-based leaf 496 (≈ p.276) s.v. بس: 'بفتح اول ترجمهٔ فقط و حسب باشد - و بمعنی بسیار'; footnote '۲ - پهلوی vas'.\"},\n   {\"ref\": \"MON:537\", \"status\": \"not_checked\", \"note\": \"Mo'in's printed page not available; vajehyab s.v. بسیار shows '[په.]' (Pahlavi origin) without the Pahlavi form.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 88 s.v. was, wasyār (PHD.txt l.615, 628)\", \"stance\": \"supports\", \"note\": \"'was [KBD < A kbyr; ws | = M, N bas] much, many, enough.' 'wasyār [wsy(k)l | N bisyār] much, many.'\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. vas, vasikār/vasiyār (NYB_vol2_glossary.txt l.4001-4009)\", \"stance\": \"supports\", \"note\": \"'vas ... many, much ... adv. very ... — OP vasiy; MPrthPrs ws; Paz. vas; NP bas.' 'vasikār, vasiyār numerous; much (= vas). — NP bisyār; from vasiy (v. vas), but the forms are not clear.'\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"bas; basand; besyâr\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP بس bas 'enough; much' < MP was < OP vasiy. Initial w- > b- is the regular NP development (cf. MP wahār > bahār). بسی basī is bas + the indefinite/adverbial -ī. بسیار besyār/bisyār 'much, many' < MP wasyār. Initial wa- > bi- appears in Classical bisyār (Hübschmann: under the influence of the following y). بسند(ه) basand(a) 'sufficient' = bas + the participial suffix -and(a) (Wiktionary), in Shahnameh usage 'بسنده نبود' 'was not a match for'.\",\n  \"derivation_fa\": \"«بس» در فارسی نو از پهلوی was و پارسی باستان vasiy است؛ w آغازین پهلوی، چنان‌که در «بهار» از wahār، در فارسی به b بدل شده است. «بسی» همان «بس» با «ی» قیدی است. «بسیار» از پهلوی wasyār است و واکهٔ i در bisyār به گفتهٔ هوبشمان زیر تأثیر y پسین پدید آمده است. «بسنده» از «بس» و پسوند «-نده» ساخته شده است، چنان‌که در بیت فردوسی «به آورد با او بسنده نبود» آمده است. ادعای نورایی درست است.\",\n  \"sources\": [U_BAS, U_BISYAR, U_BASANDA, U_MON_BAS, U_MON_BISYAR, U_MON_BASANDA],\n  \"ref_check\": [\n   KNT_VASIY,\n   {\"ref\": \"BQT:276\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt 0-based leaf 496 (≈ p.276) s.v. بس, footnote 'پهلوی vas'; leaf 500 s.v. بسند/بسنده: 'سزاوار و کافی - و تمام باشد' with the verse 'مرا شفاعت این پنج تن بسنده بود'.\"},\n   {\"ref\": \"MON:537\", \"status\": \"partial\", \"note\": \"Printed page not accessible; vajehyab Mo'in: 'بس (بَ) (ص.) ۱- کافی ۲- بسیار'; 'بسیار (بِ) [په.] زیاد، متعدد، فراوان'; 'بسنده (بَ سَ دِ) ۱- کافی، بس'. The meanings and Pahlavi origin agree.\"}\n  ],\n  \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"pp. 128 and 155 (HUB.txt l.4466-4469, 5458-5459)\", \"stance\": \"supports\", \"note\": \"'bisyār viel = ap. *vasi-ādāra- zu bas viel = ap. vasiy (unter Mitwirkung des folgenden y)'; 'bas viel = paz. vas, ap. vasiy; bisyār viel = paz. vasyār'.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt (grep bas/bisyār)\", \"stance\": \"silent\", \"note\": \"No numbered entry for bas or bisyār found in Horn's Grundriss.\"},\n   {\"src\": \"MON\", \"where\": \"vajehyab s.v. بس، بسیار، بسنده\", \"stance\": \"supports\", \"note\": \"بسیار tagged '[په.]'; بس 'کافی، بسیار'; بسنده 'کافی، بس'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt (grep VAS/WAS)\", \"stance\": \"silent\", \"note\": \"No Aryanpur entry for بس / بسیار found in the Latin index.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 88\", \"stance\": \"supports\", \"note\": \"'was ... N bas'; 'wasyār ... N bisyār'.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Avestan\", \"words\": \"vasami, usâmahi; an-usant; vasah; vasnah\", \"verdict\": \"plausible\",\n  \"derivation\": \"Avestan vas- 'to wish': pres. 1sg. vasəmī, 1pl. usəmahī (zero grade *uḱ-), PIE *wéḱ-mi / *uḱ-més (= Skt váśmi / uśmási). an-usant- 'unwilling' = negative an- + present participle usant- (= Skt uśánt-). vasah- n. 'will' (nom. vasō 'at will', Pokorny 'wollend = nach seinem Willen'). All of these match Pokorny, Bartholomae and Walde-Pokorny. The last form, 'vasnah', is not attested as such: the Avestan noun is vasna- m. 'will' (instr. vasnā), Bartholomae's and Kent's stem. Nourai seems to have given it an s-stem ending by analogy with vasah-. The derivation is correct; that one form is slightly off.\",\n  \"derivation_fa\": \"فعل اوستایی vas- «خواستن» با صیغه‌های vasəmī «می‌خواهم» و usəmahī «می‌خواهیم» (درجهٔ صفر)، صفت an-usant- «ناخواهان» (an- نفی + وجه وصفی usant-) و اسم vasah- «خواست» در فرهنگ بارتولمه و نزد پوکورنی آمده و همه از *weḱ- هندواروپایی است. اما «vasnah» با این شکل گواهی نشده است؛ صورت درست اوستایی vasna- (مفعول‌به‌واسطه vasnā) است. ادعای نورایی درست است، فقط یکی از صورت‌ها اندکی نادرست است.\",\n  \"sources\": [U_WEK],\n  \"ref_check\": [{\"ref\": \"POK:1135\", \"status\": \"supports\", \"note\": \"POK_full.txt 'u̯ek̑- to wish ... Avestan vasəmī, usəmahī ... Avestan an-usant-, -usaitī widerwillig ... Avestan vasah- (Nom. vasō) wollend ... Avestan vasnā (Instr. Sg.) after dem Willen ... Page(s):1135'. Pokorny has vasnā (instr. of vasna-), not 'vasnah'.\"}],\n  \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 1381 s.v. vas-; s.v. an-usant- (BRT.txt l.4524); s.v. vasna- (l.23281)\", \"stance\": \"supports\", \"note\": \"'vas- V. wollen ... wollen, wünschen'; 'an-usant- Adj. (fem. -saitī-) der (etwas) nicht (tun) will, widerwillig'; 'p. vašnā, j., g. vasna- m. Wille' (stem vasna-, not vasnah-).\"},\n   WLD_WEK, IEC_WEK\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Greek\", \"words\": \"exôn; a-exôn\", \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"The Greek words are ἑκών (hekṓn, Cretan wekōn) 'willing' and ἀέκων (aékōn, Attic ἄκων) 'unwilling', an old participle of a lost verb *wék-mi < PIE *weḱ- (Beekes; Pokorny 1135; Kent cites Cretan wekōn under OP vasiy). The derivation is confirmed. But the book prints 'exôn' and 'a-exôn' with x for the kappa (ε-κ-ω-ν). The correct transliteration is ekôn / hekōn and a-ekôn / aekōn. This is Nourai's misprint, and the extraction is faithful.\",\n  \"derivation_fa\": \"واژهٔ یونانی ἑκών (hekōn، در گویش کرتی wekōn) «خواهان، به دلخواه» و ἀέκων (aekōn) «ناخواهان»، وجه وصفیِ فعلی از میان‌رفته از ریشهٔ *weḱ- اند (بیکس؛ پوکورنی ۱۱۳۵). ریشه‌شناسی نورایی درست است، ولی کتاب این دو را «exôn» و «a-exôn» چاپ کرده است، حال آنکه حرف یونانی کاپا (k) است و صورت درست ekôn و a-ekôn است. این خطای چاپی خود کتاب است، نه خطای استخراج.\",\n  \"sources\": [U_HEKON, U_WEK],\n  \"ref_check\": [{\"ref\": \"POK:1135\", \"status\": \"supports\", \"note\": \"POK_full.txt u̯ek̑-: 'gr. (previous participle) hekōn (Cretan wekōn), hekousa freiwillig ... aekōn, akōn wider Willen' - Pokorny prints ek-, confirming that 'exôn' is a misprint.\"}],\n  \"consulted\": [\n   WLD_WEK, IEC_WEK,\n   {\"src\": \"KNT\", \"where\": \"Lexicon p.207 s.v. vasiy\", \"stance\": \"supports\", \"note\": \"'Gk. (Cretan) wekōn willing'.\"}\n  ],\n  \"error_in\": \"book\",\n  \"book_prints\": \"exôn ; a-exôn\",\n  \"correct_form\": \"ekôn (hekṓn, ἑκών) ; a-ekôn (aékōn, ἀέκων)\"\n }\n]\n\nentries.append({\n \"entry\": 1,\n \"root\": \"Wek\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *weḱ- 'to wish, want' (Pokorny u̯ek̑- 1135; LIV *u̯ek̑-; Kent s.v. vasiy)\",\n \"note\": \"Root, label and gloss are correct: Pokorny p.1135 'u̯ek̑- to wish' (Skt vaśmi, Av. vasəmī/usəmahī, an-usant-, vasah-, OP vašna, Gk hekōn/aekōn, Hitt. wek-), and Kent p.207 (s.v. vasiy) ties OP vasiy to 'Sas. Pahl. vas, NPers. bas', which is exactly Nourai's Persian branch. MacKenzie (was, wasyār → N bas, bisyār), Nyberg and Hübschmann confirm the Middle and New Persian steps. Minor issues: Avestan 'vasnah' should be vasna- (instr. vasnā); Greek 'exôn / a-exôn' is the book's misprint for ekôn / a-ekôn (ἑκών, ἀέκων). The Avestan box points to an empty box in the printed chart. The JSON matches the printed page; no extraction errors.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *weḱ- «خواستن» (پوکورنی ۱۱۳۵) درست است. کنت (ص ۲۰۷) زیر واژهٔ پارسی باستان vasiy همین ریشه را آورده و پهلوی vas و فارسی «بس» را از آن دانسته است؛ مکنزی، نیبرگ و هوبشمان نیز گذر پهلوی was / wasyār به «بس» و «بسیار» را تأیید می‌کنند. پس ادعای نورایی درست است. دو ایراد کوچک هست: «vasnah» اوستایی باید vasna- باشد، و «exôn / a-exôn» یونانی خطای چاپی کتاب به جای ekôn / a-ekôn (ἑκών، ἀέκων) است. خطای استخراج دیده نشد.\",\n \"sources\": [U_WEK, U_BAS, U_HEKON],\n \"ref_check\": [\n  {\"ref\": \"POK:1135\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: u̯ek̑- Meaning: to wish ... References: WP. I 244 f., Frisk 473 f. ... Page(s):1135'.\"},\n  KNT_VASIY\n ],\n \"consulted\": [WLD_WEK, IEC_WEK,\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 (grep wek-)\", \"stance\": \"silent\", \"note\": \"The 1985 Watkins appendix has wekti- 'thing' and wekw- 'speak' but no wek- 'wish' (no English derivatives).\"}],\n \"nodes\": e1_nodes\n})\n\nout = {\"pdf_page\": 537, \"book_page\": 507, \"verified_by\": \"claude-opus-5\", \"verified_on\": \"2026-10-16\", \"entries\": entries}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-537.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\")\n"
}
```


### [2026-10-16T05:24:22.915Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-537.py (file state is current in your context — no need to Read it back)
```


## [2026-10-16T05:24:26.769Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(VIRUS|OOZE|WEASEL|BISON)' SKT.txt | head; for w in VIRUS OOZE WEASEL; do n=$(grep -n -E \"^$w\" SKT.txt | head -1 | cut -d: -f1); [ -n \"$n\" ] && sed -n \"${n},$((n+3))p\" SKT.txt; done"
}
```


### [2026-10-16T05:24:27.379Z] TOOL RESULT

```
Exit code 1
```


## [2026-10-16T05:24:29.385Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^\\W{0,3}(virus|ooze|weasel|bison)\\b' SKT.txt | head; grep -n -E 'Virus|Ooze|Weasel|Bison' SKT.txt | head"
}
```


### [2026-10-16T05:24:30.256Z] TOOL RESULT

```
1829:Bison,  n  quadnipcd.  (L.*Gk.«*Tcul.) L  btson  (,l*lmy>.-Latc  Gk.  &iav¥.  Not  a true  Gk.  word,  but  borro*red  from  Tea- tonic  ;  O  H,  («  wiiuHt,  (j.  witfiti,  i.biiODi A.  S.  iivjfftf,  a  will'  ox  ;   Icel   virunJr.
1829:Bison,  n  quadnipcd.  (L.*Gk.«*Tcul.) L  btson  (,l*lmy>.-Latc  Gk.  &iav¥.  Not  a true  Gk.  word,  but  borro*red  from  Tea- tonic  ;  O  H,  («  wiiuHt,  (j.  witfiti,  i.biiODi A.  S.  iivjfftf,  a  will'  ox  ;   Icel   virunJr.
```


## [2026-10-16T05:24:39.977Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'E'\np='build-537.py'; s=open(p).read()\nimport re\ndef cut(s, start):\n    i=s.index(start); j=s.index('}', i)+1\n    # remove trailing comma/newline handling\n    seg=s[i:j]\n    return s.replace(seg,'@@CUT@@')\ns=cut(s,'{\"src\": \"LAT\"'); s=s.replace('@@CUT@@,\\n   ','')\ns=cut(s,'{\"src\": \"TLM\"'); s=s.replace('@@CUT@@,\\n   ','')\nSKB='{\"src\": \"SKT\", \"where\": \"s.v. Bison (SKT.txt l.1829)\", \"stance\": \"supports\", \"note\": \"\\'Bison ... (L.-Gk.-Teut.) L. bison ... Not a true Gk. word, but borrowed from Teutonic; O.H.G. wisunt ... Icel. visundr\\' - English via Latin, ultimately Germanic.\"}'\ns=s.replace('{\"src\": \"SKT\", \"where\": \"s.v. VIRUS\", \"stance\": \"silent\", \"note\": \"Skeat\\'s concise entry gives L. uīrus only.\"}',\n '{\"src\": \"AHD\", \"where\": \"Watkins 1985 index (l.2455)\", \"stance\": \"supports\", \"note\": \"\\'VIRUS weis-\\' - English/French virus from Latin vīrus listed under weis-.\"}')\ns=s.replace('{\"src\": \"SKT\", \"where\": \"s.v. OOZE / WEASEL\", \"stance\": \"silent\", \"note\": \"Skeat gives OE wāse / wesle without IE root.\"}', SKB)\ns=s.replace('\"stance\": \"partial\", \"note\": \"\\'BISON weis-\\', \\'OOZE2 weis-\\'; in the entry the animal words are \\'more likely of obscure origin\\'.\"}',\n '\"stance\": \"partial\", \"note\": \"\\'BISON weis-\\', \\'OOZE2 weis-\\'; in the entry the animal words are \\'more likely of obscure origin\\'.\"},\\n   '+SKB)\nassert 'LAT\"' not in s and 'TLM' not in s and '\"SKT\", \"where\": \"s.v. OOZE' not in s\nopen(p,'w').write(s)\nE\npython3 build-537.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-537.json > /dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 537"
}
```


### [2026-10-16T05:24:40.812Z] TOOL RESULT

```
written
nodes verified: 14/14
node verdicts: {'confirmed': 6, 'plausible': 6, 'disputed': 1, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 12, 'partial': 4, 'not_checked': 4}
books consulted: {'supports': 28, 'partial': 10, 'silent': 5, 'contradicts': 1} | by book: {'KLN': 6, 'WLD': 5, 'POK': 4, 'BRT': 3, 'PHD': 3, 'MON': 3, 'ARY': 3, 'AHD': 3, 'NYB': 2, 'HUB': 2, 'SIN': 2, 'HRN': 2, 'SKT': 2, 'IEC': 2, 'SYN': 1, 'KNT': 1}
```


## [2026-10-16T05:24:48.043Z] TOOL CALL #85: SubagentHandback

```json
{
 "message": "I wrote /home/sfmqrb/git/rishe-private/data/verification/page-537.json. `verify_check.py 537` shows 14/14 nodes and 0 PROBLEM lines.\n\n**Verdicts on PDF page 537 (book page 507):**\n- Roots: 2 confirmed (Weis = PIE *weys-, Pokorny 1134; Wek = PIE *weḱ-, Pokorny 1135 and Kent 207).\n- Nodes: 6 confirmed, 6 plausible, 1 disputed, 1 transcription_suspect.\n\n**Disputed:**\n- Weis #4, Latin viscum: it means \"mistletoe, birdlime\", not \"slime\". Pokorny gives it only as \"perhaps\" under a separate root (*uiks-, with Greek ixos), and Wiktionary calls the link with vīrus \"unlikely\". Latin virus in the same node is confirmed.\n\n**Transcription suspect:**\n- Wek #5, Greek \"exôn / a-exôn\": the book prints x where the Greek has kappa. The correct forms are ekôn / a-ekôn (ἑκών, ἀέκων). This is the book's misprint, not an extraction error. The page image is saved at data/verification/sources/refs/ocr/BOOK/537.png.\n\n**Notable plausible items:**\n- Weis #2/#3, Pahlavi bēš / Persian bīš \"aconite\": the root is right, but the route via Avestan is doubtful.\n  - MacKenzie reads the Pahlavi word as bīš \"aconite\", so Nourai's bēš is another reading of the same spelling, not a misprint.\n  - Laufer and Wiktionary make it a loan from Sanskrit viṣā \"Aconitum ferox\"; the inherited Pahlavi descendant of Avestan viša- is wiš \"poison\".\n  - The chart's note pointing to \"Dwei\" concerns a homonym, Pahlavi bēš \"harm\" (from Avestan ṭbaēšah-), which is a different word.\n- Weis #8/#9: Watkins says the weasel and bison words are \"more likely of obscure origin\". English bison also came through Latin and French, not directly from Germanic.\n- Wek #4: Avestan \"vasnah\" should be vasna- (instrumental vasnā).\n\n**Extraction errors:** none. The JSON matches the printed page."
}
```


### [2026-10-16T05:24:48.630Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
