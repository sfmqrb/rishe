# Verification process log — verify-page-551


## [2026-10-17T00:00:15.617Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 551 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-551.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-551.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-551.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 551` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.689Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:18.482Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:18.542Z] TOOL RESULT

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
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:00:18.983Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-551.txt"
}
```


### [2026-10-17T00:00:19.055Z] TOOL RESULT

```
1	=== PDF page 551 (book page 521) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wes 3, Ew-es, Eu-es : to wear, put on  (refs POK:1172)
4	#1 (parent #0) [Avestan] refs=POK:1172; KNT:219 | vastra 1, vasta 1 : clothing ; vaste, vašaiti, aothra, vah, vahna, vanhna : cover
5	  #2 (parent #1) [Persian] refs=AEF:230 | bâm 2 «بام ۲ (بان ۲)» : shelter, house, roof ; bânŭ «بانو» : house lady | NOTE: HUB:25 does not agree with this derivation of "bânŭ".
6	#3 (parent #0) [Sanskrit] refs=POK:1172 | vasman, vasana : roof, cover
7	#4 (parent #0) [Old Persian] refs=HUB:32; AEF:305 | vahâna : cover
8	  #5 (parent #4) [Pahlavi] refs=HUB:32 | vahânak : hidden reason, excuse
9	    #6 (parent #5) [Persian] refs=AEF:305 | bahâneh «بهانه» : excuse
10	#7 (parent #0) [Avestan / Old Persian] refs=BRT:904; AEF:410; KLN:1223; KNT:196 | apa-vasta, pavasta, pastô : outer cover, skin, bark ☞Apo
11	  #8 (parent #7) [Pahlavi] refs=SNS:410; SNS:139 | pôst : skin, bark, cover
12	    #9 (parent #8) [Persian] refs=BQT:427; AEF:410; MON:830 | pŭst «پوست» : skin, hide | extra: پوسته، پوستین
13	  #10 (parent #7) [Sogdian] refs=SOD:331 | pwst : skin ; pwst`k : writing tablet
14	  #11 (parent #7) [Avestan] refs=BRT:904; AEF:410 | pastô-fratha : as wide as the skin gets ☞Per 1
15	#12 (parent #0) [Germanic] refs=AHD | wazjan : to wear
16	  #13 (parent #12) [English] refs=None | wear
17	#14 (parent #0) [Latin] refs=AHD | vestis : garment
18	  #15 (parent #14) [English] refs=AHD | vest, divest, invest
19	--- entry 1 ---
20	ROOT [Indo-European] Wes 4 : eat, feed  (refs POK:1171; WLD1:307)
21	#1 (parent #0) [Avestan] refs=POK:1171; WLD1:307 | vastra 2, vâstra 2 : food, feed, fodder, also a lining and cover
22	  #2 (parent #1) [Pahlavi] refs=SNS:260 | vâstr : farm, meadow ; vastriuš : farmer
23	    #3 (parent #2) [Persian] refs=SNS:260; MON:4946 | vâstar «واستر» : meadow, farm ; vâstriyŭš «واستریوش» : farmer | NOTE: The relationship of the Persian word "vâs:wheat" to these words is not clear
24	
```


## [2026-10-17T00:00:19.554Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-551.json"
}
```


### [2026-10-17T00:00:19.607Z] TOOL RESULT

```
1	{
2	  "pdf_page": 551,
3	  "book_page": 521,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wes 3, Ew-es, Eu-es",
8	        "lang": "Indo-European",
9	        "refs": "POK:1172",
10	        "gloss": "to wear, put on"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1172; KNT:219",
18	          "words": [
19	            {"translit": "vastra 1, vasta 1", "gloss": "clothing", "script": null},
20	            {"translit": "vaste, vašaiti, aothra, vah, vahna, vanhna", "gloss": "cover", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "AEF:230",
30	          "words": [
31	            {"translit": "bâm 2", "gloss": "shelter, house, roof", "script": "بام ۲ (بان ۲)"},
32	            {"translit": "bânŭ", "gloss": "house lady", "script": "بانو"}
33	          ],
34	          "note": "HUB:25 does not agree with this derivation of \"bânŭ\".",
35	          "quote": {
36	            "text": "سر فرو کن یک دمی از بان چرخ - تا زنم من چرخها بر سان چرخ",
37	            "poet": "Molavî"
38	          }
39	        },
40	        {
41	          "id": 3,
42	          "parent": 0,
43	          "lang": "Sanskrit",
44	          "refs": "POK:1172",
45	          "words": [
46	            {"translit": "vasman, vasana", "gloss": "roof, cover", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 4,
53	          "parent": 0,
54	          "lang": "Old Persian",
55	          "refs": "HUB:32; AEF:305",
56	          "words": [
57	            {"translit": "vahâna", "gloss": "cover", "script": null}
58	          ],
59	          "note": null,
60	          "quote": null
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Pahlavi",
66	          "refs": "HUB:32",
67	          "words": [
68	            {"translit": "vahânak", "gloss": "hidden reason, excuse", "script": null}
69	          ],
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 6,
75	          "parent": 5,
76	          "lang": "Persian",
77	          "refs": "AEF:305",
78	          "words": [
79	            {"translit": "bahâneh", "gloss": "excuse", "script": "بهانه"}
80	          ],
81	          "note": null,
82	          "quote": null
83	        },
84	        {
85	          "id": 7,
86	          "parent": 0,
87	          "lang": "Avestan / Old Persian",
88	          "refs": "BRT:904; AEF:410; KLN:1223; KNT:196",
89	          "words": [
90	            {"translit": "apa-vasta, pavasta, pastô", "gloss": "outer cover, skin, bark", "script": null, "see": ["Apo"]}
91	          ],
92	          "note": null,
93	          "quote": null
94	        },
95	        {
96	          "id": 8,
97	          "parent": 7,
98	          "lang": "Pahlavi",
99	          "refs": "SNS:410; SNS:139",
100	          "words": [
101	            {"translit": "pôst", "gloss": "skin, bark, cover", "script": null}
102	          ],
103	          "note": null,
104	          "quote": null
105	        },
106	        {
107	          "id": 9,
108	          "parent": 8,
109	          "lang": "Persian",
110	          "refs": "BQT:427; AEF:410; MON:830",
111	          "words": [
112	            {"translit": "pŭst", "gloss": "skin, hide", "script": "پوست"}
113	          ],
114	          "script_extra": "پوسته، پوستین",
115	          "note": null,
116	          "quote": {
117	            "text": "بگو آن سخن ها که سود اندروست - سخن گفته مغز است و ناگفته پوست",
118	            "poet": "Ferdowsî"
119	          }
120	        },
121	        {
122	          "id": 10,
123	          "parent": 7,
124	          "lang": "Sogdian",
125	          "refs": "SOD:331",
126	          "words": [
127	            {"translit": "pwst", "gloss": "skin", "script": null},
128	            {"translit": "pwst`k", "gloss": "writing tablet", "script": null}
129	          ],
130	          "note": null,
131	          "quote": null
132	        },
133	        {
134	          "id": 11,
135	          "parent": 7,
136	          "lang": "Avestan",
137	          "refs": "BRT:904; AEF:410",
138	          "words": [
139	            {"translit": "pastô-fratha", "gloss": "as wide as the skin gets", "script": null, "see": ["Per 1"]}
140	          ],
141	          "note": null,
142	          "quote": null
143	        },
144	        {
145	          "id": 12,
146	          "parent": 0,
147	          "lang": "Germanic",
148	          "refs": "AHD",
149	          "words": [
150	            {"translit": "wazjan", "gloss": "to wear", "script": null}
151	          ],
152	          "note": null,
153	          "quote": null
154	        },
155	        {
156	          "id": 13,
157	          "parent": 12,
158	          "lang": "English",
159	          "refs": null,
160	          "words": [
161	            {"translit": "wear", "gloss": null, "script": null}
162	          ],
163	          "note": null,
164	          "quote": null
165	        },
166	        {
167	          "id": 14,
168	          "parent": 0,
169	          "lang": "Latin",
170	          "refs": "AHD",
171	          "words": [
172	            {"translit": "vestis", "gloss": "garment", "script": null}
173	          ],
174	          "note": null,
175	          "quote": null
176	        },
177	        {
178	          "id": 15,
179	          "parent": 14,
180	          "lang": "English",
181	          "refs": "AHD",
182	          "words": [
183	            {"translit": "vest, divest, invest", "gloss": null, "script": null}
184	          ],
185	          "note": null,
186	          "quote": null
187	        }
188	      ]
189	    },
190	    {
191	      "root": {
192	        "name": "Wes 4",
193	        "lang": "Indo-European",
194	        "refs": "POK:1171; WLD1:307",
195	        "gloss": "eat, feed",
196	        "note": "Compare with \"Ed:to eat\"."
197	      },
198	      "nodes": [
199	        {
200	          "id": 1,
201	          "parent": 0,
202	          "lang": "Avestan",
203	          "refs": "POK:1171; WLD1:307",
204	          "words": [
205	            {"translit": "vastra 2, vâstra 2", "gloss": "food, feed, fodder, also a lining and cover", "script": null}
206	          ],
207	          "note": null,
208	          "quote": null
209	        },
210	        {
211	          "id": 2,
212	          "parent": 1,
213	          "lang": "Pahlavi",
214	          "refs": "SNS:260",
215	          "words": [
216	            {"translit": "vâstr", "gloss": "farm, meadow", "script": null},
217	            {"translit": "vastriuš", "gloss": "farmer", "script": null}
218	          ],
219	          "note": null,
220	          "quote": null
221	        },
222	        {
223	          "id": 3,
224	          "parent": 2,
225	          "lang": "Persian",
226	          "refs": "SNS:260; MON:4946",
227	          "words": [
228	            {"translit": "vâstar", "gloss": "meadow, farm", "script": "واستر"},
229	            {"translit": "vâstriyŭš", "gloss": "farmer", "script": "واستریوش"}
230	          ],
231	          "note": "The relationship of the Persian word \"vâs:wheat\" to these words is not clear",
232	          "quote": null
233	        }
234	      ]
235	    }
236	  ]
237	}
238	
```


## [2026-10-17T00:00:34.733Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -80; command ls data/verification/sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','KNT','BRT','HUB','AEF','SNS','BQT','MON','KLN','SOD','HRN','PHD','NYB','CHEUNG','ARY','IEC','SYN','SKT']:\n  v=d.get(k);print(k, json.dumps(v,ensure_ascii=False)[:400] if v else None)\n\""
}
```


### [2026-10-17T00:00:35.096Z] TOOL RESULT

```
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
KNT_full.txt
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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
CHEUNG None
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
```


## [2026-10-17T00:00:41.827Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-538.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000]); print(e.keys())\"; sed -n 1,80p tools/verify_check.py | head -120; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','WLD','HUB','HRN','BRT','KNT','SNS','SOD','BQT','MON','KLN','AHD','PHD','NYB','ARY']:\n  v=d[k];print(k,v.get('page_offset'),'|',v.get('lookup_hint','')[:300])\n\""
}
```


### [2026-10-17T00:00:42.285Z] TOOL RESULT

```
{"pdf_page": 538, "book_page": 508, "verified_by": "claude-opus-5.5", "verified_on": "2026-10-16"}
{
 "id": 1,
 "lang": "Avestan / Old Persian",
 "words": "vak, vačah, vaxš 1",
 "verdict": "confirmed",
 "derivation": "Avestan has the verb vac- / vaoc- 'to speak' (Indo-Iranian *wak-, *wač- < PIE *wekʷ-, with the labiovelar becoming k and then č before a front vowel), the neuter s-stem vacah- 'speech, word' (= Skt. vacas-, Gk. épos < *wekʷ-os) and the root noun vāč- 'voice, word', nominative vāxš (= Skt. vāk, Lat. vōx < *wōkʷs). Nourai's 'vak' is the root and 'vaxš' is that nominative (Bartholomae writes it vāxš with a long vowel). All three forms and the glosses are correct. The words are Avestan; Old Persian has no attested form of this root.",
 "derivation_fa": "در اوستایی فعل vac- / vaoc- «گفتن»، نام‌واژهٔ vacah- «سخن، گفتار» (برابر سنسکریت vacas- و یونانی épos) و نام‌واژهٔ vāč- «آواز، سخن» با حالت فاعلی vāxš (برابر سنسکریت vāk و لاتینی vōx) آمده است. kʷ هندواروپایی در هندوایرانی به k و پیش از واکهٔ پیشین به č بدل شده است. بارتولومه و پوکورنی و چونگ همین را می‌گویند و ادعای نورایی درست است. تنها این صورت‌ها اوستایی‌اند و در پارسی باستان گواهی ندارند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-",
  "https://en.wiktionary.org/wiki/آواز"
 ],
 "ref_check": [
  {
   "ref": "POK:1135",
   "status": "supports",
   "note": "POK_full.txt l.90122 'Avestan vac- speak ... Old Indic vacas- n. = Avestan vacah (= gr. épos) discourse, word ... vāk = Avestan vāxš (= Latin vox) voice, discourse, word'."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "col. 1333-1336 s.v. vāk-; col. 1340-1341 s.v. vacah-",
   "stance": "supports",
   "note": "BRT.txt l.22236 'vāk- (vāxš) m., f. 1) Stimme; 1) der Menschen (und Götter) Stimme ... 2) Rede, Wort ... Zum V. vak-'; l.22355 'vacah- n. 1) Sprechen, Rede, Wort ... im Gegensatz zu Denken und Handeln'."
  },
  {
   "src": "WLD",
   "where": "Bd. I 245",
   "stance": "supports",
   "note": "'ai. vacas- n. = av. vacah- „Rede, Wort“ ... ai. vāc-, n. sg. vāk = av. vāxš (= lat. vox) „Stimme, Rede, Wort“'."
  },
  {
   "src": "SYN",
   "where": "18.11 VOICE",
   "stance": "supports",
   "note": "'Skt. vāc-, Av. vāč- (nom. sg. Skt. vāk, Av. vāxš)'."
  },
  {
   "src": "CHEUNG",
   "where": "p. 402 s.v. *u̯ač",
   "stance": "supports",
   "note": "'AVESTAN: vaoc- (vāč-) to say' with forms vaocat, uxδa- etc."
  }
 ]
}
dict_keys(['entry', 'root', 'verdict', 'modern_form', 'note', 'note_fa', 'sources', 'ref_check', 'consulted', 'nodes'])
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
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
ARY printed page = pdf page + 1 | Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
```


## [2026-10-17T00:00:45.610Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'lemma: 1\\?\\.\\? \\?\\(wes\\|u̯es\\|eu-\\)' POK_full.txt | head -20; grep -n \"Page(s): 117[12]\" POK_full.txt | head"
}
```


### [2026-10-17T00:00:46.280Z] TOOL RESULT

```
28864:Root /lemma: eu-1, eua-\ ua- ua-{**hue-) 
28918:Root / lemma: eu-2 
28961:Root / lemma: eu-3, with present formants -et- : yet-, ut- 
28980:Root / lemma: eu-4 
92459:Page(s): 1171-1172 
92521:Page(s): 1172-1173
```


## [2026-10-17T00:00:48.325Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92420,92600p POK_full.txt"
}
```


### [2026-10-17T00:00:48.693Z] TOOL RESULT

```
Hittite {*hauhes^ ^es/- 'pasture', uesua-^qraze, abweiden; lead, regieren'; {*hauhes- 
)i/es/a/'a- 'herdsman, shepherd'. 

Maybe alb. ushq/mlood', ushqejleed'. 

References: WP. I 307 f., Vendryes RC. 35, 89 f., WH. II 769 

See also: probably to uesu- 'good'. 

Page(s):1171 

Root / lemma: ues-3 {* hyes-3) 
Meaning: wet 

Material: Gr. sapov Aournpa, n Trpoxouv Hes., alt-theraisch hsapa (meaning 
unacquainted); Umbrian i/es/z/ra/^'libato' (formation as Latin lectTca); 
Maybe alb. vese^ dew ' 

Old High German wasa/^ra\n', Old High German waso'\a\Nn, clod of earth, pit, pothole'. 
Modern High German l/Vasen lawn' , Old Saxon waso, Middle Low German wase^damp 
Erdgrund, slime, mud; clod of earth, lawn'; Middle Low German wasemm. 'Wasserdampf, 
haze, mist'; Old English wosn. ' dampness, juice, sap'; engl. ooze' dampness, slime, 
mud', as verb 'durchsickern, spring up, bubble'. Middle Low German wos'scum, froth. 



foam, decoction, extract acquired by boiling, juice, sap'. Old Danish Norwegian os' plant 
juice '; 

presumably Avestan varjhu-tat-t "blood', varjhu&wa-u. "Blutvergieflen, bloody fight', 
vohuna- m. 'blood' and Old Indie vasa, Kas5 "bacon, fat, lard ' (also i/asa inscribed, as 
vasa-m "flijssiges fat'); 

here with the meaning "male animal' (compare Latin verresetc: uer-, t/eA-s-'feuchten'): 
Old Indie ustra- m. 'Buffel, Kamel', ^s/5/'-'Pflugstier', Avestan ustrom. 'Kamel' (also in 
Zaral=>-ustrd)\ Old Indie ^5/5'Pflugstier'. 

References: WP. I 308, Trautmann 343, Mayrhofer 1 , 113 f.. Frisk 433. 
Page(s): 1171-1172 

Root / lemma: ues-4 {*hues-4) 

Meaning: to stick, pierce 

Material: Old Indie nivasita- 'ums Leben gebracht', n/rvasana-m^ das Ermorden, Toten', 

y0a/7Vas5ya//"sehneidetrings ab, from' ; Old Irish ;fe/7/75/o'"schindet' {*ues-na-ti)\ (common 

Celtic -ns-, -nt- > -nn-), alb. usht^ ear '; 

Lithuanian i/s/7/s 'thistle, hawthorn', Latvian usna, i/5/7a "thistle'; 

about Church Slavic vtdSB "louse' etc., see above S. 692 and Vasmer 1, 232 f. 
Maybe alb. vesh, PI. veshe^ ear'. 

Old High German c»/'/"cusp, peak, point, edge etc.'. Modern High German 0/t"place' (and 
"Schusterahle'), Old English ord^cus^, peak, beginning ', Old Icelandic oddr^cus^, peak'. 
Old Germanic Osd-ulfus= Old Saxon Old English 0/-o'-i//f (different above S. 237); 
[common Latin Germanic -s- > -/"-]. 

References: WP. I 308 f. 
Page(s):1172 

Root / lemma: ues-5 {* haues-5) 

Meaning: to dress, put on 

Material: Old Indie i/a5/e"kleidet sich, zieht an', Avestan vasteds. (compare the unthemat. 

gr. EGoai, -soTai), varjhaiti 6s.\ Old Indie vasana-, Avestan varjhana- n. " garment '; Old 

Indie vasman- n. "cover' (= z\\\a)\ vastra-, Avestan vastra- n. " clothing ' (: gr. FEGipa, 

Middle High German westeil); 

Armenian z-genum^'^uW myself an' {*ues-nu- = zvvv[}\), z-gest^ clothing ' (-/i/-stem); 



gr. Evvupi, Ionian sTvupi, Aor. zo{o)a\ " apparel ', Med. "sich kleiden', athemat. Perf. £l|jai 
(*F£a-[jai) 3. Sg. Eni-Earai (Herod.); zoBoq n. ' clothing ' (-dhes-stem), zaBr\q, -nroc; ds. 
(*F£a[TO-]TaT-c; with dem 9 from eoQoq); savoc; "weibliches garment ' (Old Indie vasana-m); 
Ionian Attic sipa, Doric Fripa, Lesbian Fsppa 'dress' (: Old Indie vas-man-); Hes. yHMCi 
ipaTiov, £u-, KQKO, 5ua-£ifju)v "good, schlecht gekleidet', with Vorstufe of Itazismuslpariov 
'dress, mantle'; Doric Fsarpa (ysaTpa aroAri Hes.), z(pzoip'\qi. "warmeres Wintergewand, 
Soldatenmantel'; 

alb. vesh'\ kleide an', i//s/7e/77"kleide myself an'; 

Latin vest/'s ' clothing ', vest/'o, -Tre " apparel ' (compare Yscrria svSugk; Hes.); 

Gothic wasjan. Old High German werian. Old Icelandic veria^ apparel ', Old English 
werian^6s., dress bear, carry'; Gothic wastii. 'dress'; Middle High German wester {see 
above) Taufkleid' (but Old High German early wastibarn, previously by Notker westerwat); 
Old Icelandic veslu. "dress' {*wesala-), ver^ coating, layer' {*waza-); 

Hittite uas-, ues-, Luvian uas(s)-^beV\e\6ev\, lure, tempt '; Tocharian B wastsi, wastsi 
"dress' (neologism); A wsal6s.\ 

References: WP. I 309, WH. II 775 f.. Frisk 521 f. 
Page(s): 1172-1173 

Root / lemma: ues-no- {* haues-no-) 

Meaning: price 

Material: By den einzelnen Sprachen sways e-and ovocalism: Old Indie vasna- m. " 

purchase price', n. "earnings', i/5S/7ay5//"feilscht'; Armenian gin^ purchase price'; gr. hom. 

(I)vo(; " purchase price', Lesbian ovva {*uosnS), Ionian Attic cJbvri " purchase', cbv£0|jai " buy 

', gort. u)vr|v " sell '; Latin venus{ov\\)j in Akk. venum, Dat. veno, later venui) "sale' {vendo, - 

dere' sell ' is *venom+ do, i/e/7eo "verkauft become' = *venom+ eo); marr. eituam 

vena//nam ^pecun\a{r\ venaliciam' (?) muft ein loanword from Latin sein, da s/7marr. not n 

ergeben wurde; Old Russian i/e/70 "dowry'; Hittite ussan/ya-' sell ' (compare above uas- 

"buy'). 

References: WP. I 31 1 f., WH. II 753 f., Vasmer 1, 182 f. 

See also: ues-8 

Page(s):1173 

Root / lemma: ues-7 {* haues-7) 
Meaning: to turn, wind 



Material: Old Indie veda- m. " hassock, clump of grass ' ( *uozdos); usnfhai. " nape ', 
usnTsa- m. "head fascia' {*us-nT-' gyration '); Swedish, Norwegian uase'Laubbundel', vasa 
"verwickein, maunder, drivel ', Old Icelandic i/55as/r"sich verwickein'. Middle Low German 
Middle English n/ase "bundle'. 
References: WP. I 309 f., Mayrhofer 1, 114. 
Page(s):1173 

Root / lemma: yes-8 {* haues-) 

Meaning: to buy, sell 

Material: Hittite uas-, uasija- "buy, acquire', ussaniia-^ sell ', uessia-^ purchase price'; 

perhaps Latin vTlis{*ues-li-) " cheap '. 

References: WP. I 312, WH. II 753 f., Szemerenyi Arch. Lingunder 6, 36 

See also: ues-no- 

Page(s):1173 

Root / lemma: ues-9 {* hayes-) 

Meaning: " gleam, shine ' 

See also: see above S. 86 f. [ayes-). 

Page(s):1173 

Root / lemma: yesperos {yekeros) {* hayekk"'ero) 

Meaning: evening 

Material: Gr. ia-nz^oc, m. "evening, vespertine ', sanspa f. "evening', ZQ-nt^xoo,, eonspivoq " 

vespertine '; Latin vesper, -er/s and -©/"/"evening, eventide ', vespera^ eventide ' (out of it 

Old Irish fescor, mcymr. gosper, gosber); probably to Modern High German West {above 

S. 73); against it Baltic- Slavic *uekera- m. "evening': Lithuanian i/a/raAas "evening' (PI. 

Ka/ra/'arWesten', vakarQ i/^5s"Westwind'), Latvian i/a/ra/'s "evening'. Old Church Slavic 

vecerb ds., wherefore Adv. Old Church Slavic vbcera " yesterday ' etc., basic meaning 

perhaps " darkness', to Lithuanian i//ra/7as "cloudy', i>/7/r/7a "shadow', Latin umbra {^ unksra)
```


## [2026-10-17T00:00:52.929Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 92340,92420p POK_full.txt"
}
```


### [2026-10-17T00:00:53.453Z] TOOL RESULT

```
References: WP. I 292, Meyer-LiJbke REW3 p. 9232, Vendryes RC. 46, 137 and above S. 

81. 

Page(s): 1 1 69 

Root / lemma: ues-1 {* hauhes-f) 

Meaning: to stay, live, spend the night 

Material: Old Indie i/asa// (participle secondary usita-) "verweilt, dwells, iibernachtet' (with 

a: 'sleeps with a Frau', with i/pa.' 'fastet') = Avestan varjhaiti^ dwells, verweilt'. Old Indie 

Kaus. K55ay5//"beherbergt'; vastu-, vasatf-xx\.i., vasa-m. 'abode, residence, 

Ubernachten', Old pers. a-vahanam^ residence, dot'. Old Indie lengthened grade vastu-n. 



'site, house', new vastu-n. " thing' {vastuka-xw. "a plant', actually "Hofunkraut'); vasa- 
vesmann. "Schlafzimmer'; 

Armenian goy"\s, existiert, is vorhanden', goy{f-stem) "being, being, blessing, property'; 

gr. azoa ep. Aor. (stets with vuktq connected) "zubringen', in addition present atoKOd, 
asGKOVTo; perhaps earia f. "stove, hearth, altar', figurative "house, family etc.', with 
secondary i Ionian iariri, Aeolic Boeotian lokr. Doric Arcadian iaria through Assimil. an das 
betonte i the second syllable, das Fehlen desF perhaps through influence of ToTriMi; 
derivative from 'Ves-//-"Bleiben, dwelling', also "zum Heim belonging'; with unexplained a- 
vocalism (F)aaTu n. "town, city' (aaT6(; " town dweller', aaTsToq "stadtisch'); 

Messapic vaste/{Dal); 

Latin l/es/a "goddess of hauslichen Hordes'; 

Middle Irish /o(a)/o'"nachtigt (also "with a wife, woman'), remains, verweilt, wakes in the 
night' {*uoseti), 3. Sg. preterit ffu{*ui-uds-t), 3. PI. feotar{*ui-uos-ont-j), verbal noun fess, 
feissi. " sleep, coitus, abode, residence', ablaut, fossm. "Bleiben, tranquility', /foss'to 
house', fossad't\g\r\t, firm, steadfast; dwelling, abode, residence'; cymr. ^M/as"Heimstatte', 
mcymr. gwest, AyM/es/"Ruheplatz', gwest, cywestach ^co\\.us\ ^M/es//"dwelling', dirwest 
{*dhro-ues-t-) and darwest{*to-are-ues-t-) " fast '; 

Gothic wisan{^. Sg. preterit was) "sein, abide, remain ', Old Icelandic i/es5 (later vera). 
Old English Old Saxon Old High German wesan {ev\ig\. preterit was). Old Frisian wesa 
"sein, abide, remain ', Modern High German war, gewesen, substantivierter Infin. "entity'; 
Gothic w/stst "entity'. Old Icelandic v/st. Old English Old High German iy/5/ "entity, abode, 
residence, Dasein'; Old Icelandic i/^/r" peaceful ' (or identical with dem 2. part from g/- 
vaerr, see above S. 1165; certainly here belongs /7e/'5d-i/^/r"berechtigt, in district, region, 
area to sein'); Old Saxon weron. Old High German n/e/'e'/? 'endure, wahren' (in addition Old 
High German wirig^ lasting, dauerhaft'. Modern High German lang-wierig) and Old Saxon 
waron. Middle Low German n/a/ie/? "endure'; perhaps Gothic nvis" calm (at sea) ', if actually 
" tranquility '); 

Tocharian A wsen/ie' lair', wast, B os/ "house', M/as5/r7c» "friend', PI. wasmoh, wsassam 
" dwells '; 

Hittite {*hueis-) huis-^ live, am Leben bleiben', {*hueisa-) /7^/sa-" mirror'. 



References: WP. I 306 f., WH. II 773, Frisk 25, 173 f., 576 f., VendryJs RC. 35, 89 f.. Loth 
RC. 38, 297, Ifor Williams BBCS. 2, 41 ff., R. A. Fowkes JC. stem 2, 1 f. 
Page(s): 1170-1171 



Root / lemma: ues-2 {* hauhes-2) 
Meaning: to feast 

Material: Old Indie anu vavase^has aufgezehrt', vastoh'vor dem ravenousness', Avestan 
vasfraTresse, muzzle', vastrsm loo6' , vas far- ^H\rte'; about Latin vescor^as meal eat, be 
nourished ' see above S. 73; Middle Irish fess, fe/sslood, eating' {*ues-ta). Old Irish fi'ach 
"raven' ( *uesakos), out of it borrowed cymr. gwyach "Steiftfuft' (ein bird); Old Irish ban- 
[f]ess^ wedding ' (Trauen-fesf), bret. /7a/7i/e5 'festival', cymr. ^n/es/ 'festival'; Gothic waila 
wisan 'to feast, delight ', frawisan 'consume', wizon 'indulge oneself, waila-wizns ' feast ', 
gawizneigs' s\c\\ mitfreuend'. Old English tvesa/? 'to feast' (only Beowulf 3115, Hs. 
weaxan); Old High German firwesan. Middle High German i/e/wese/7 'consume'; Old 
Icelandic vist. Old English Old High German wisti. 'dish, food'; in ablaut probably Old High 
German M/as/e/( French gateau) ' cake';
```


## [2026-10-17T00:01:19.022Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pasto\\|pastö\\|pastō' BRT.txt | head; grep -n -i 'pavast' KNT_full.txt BRT.txt | head; grep -n -i 'vahana\\|vahänam\\|a-vahanam\\|avahanam' KNT_full.txt | head; grep -n -i 'vastra\\|vaste' BRT.txt | head -30"
}
```


### [2026-10-17T00:01:19.441Z] TOOL RESULT

```
3300:•  j.  ad»  Adv,  'imten':  kasnS  dtntn.  zqnuä a'  nabihca  az'opastoi/ (sd.)  Y.44.4.
5095:•  g.  ava-pastöiä  In£  'hinabzufallen':  kasnä d>r»tä  samcü  ads  nabasSä  avap°  kl  aps urvarasca  "wer  wahrte  die  Erde  unten und  den  Luftraum,  dass  sie  nicht  hinab- iielen,  wer  Wasser  und  Pflanzen?"  Y.  44. 4'"
13648:f  «'«>"^£«''"^  ■-."'■■  "d^n  sollst  'k^(s^'^f,:^]^XA_2',-asim..'TL;^m du  einen  Pnester  oennen.  .  .  der  . ."  \ .  „^^^^^^  ^^j  y^  _  _  ^  ^„^'  ^^ iÄ6;  -  <7/^r^  (^)  .  .  m  d'a2-a>a  f„^^  sr»,«/i,7)  -y«»  <»>l«r<7^  »,«,/J  V. /«/,««  fsd.)  y.75.48;  -  yat  hanö  -  .,,^.,3.  _  ^^  ^^^  .nämL  maUh)  'g^ä bm-äl  aojjst^mca  d-  pascaaa  mazdayama  ^^^„„^^„3  s„naitis  Y.J3.4;  —  Pm.ru- tanast,mca    .  .  pastö.fra^a»,h^   (sd.)    h!    .^^^.  .^,^   ,^^^^    far^i^^^  Y.
27699:—  yB  hakat  astJica  ..  zimä^a'-^  kam.- rai%wayäti  (sd.)  Yt.  70. 72.  Daher  a)  oft im  Gegensatz  zu  a)  Himmel  und  Luft- raum: atitary  zqm  asmaiumca  Y.68.1^, Yt.<y.8,  io.95,  /J.13',  43,  44,  Y.Ol.i, H.7.16;  Yt  79.43;  —  vispqmca  zqm  .. vTspimca  asmamm  Y.  77,  9;  —  imqmla zqm  .  .  aomla  asmatam  "die  Erde  hier ..  der  Himmel  dort"  Yt7j.i53;  2,  77. 57,60; —  aiähäsia  ztmB  avai^htia  asnS Y.  7. 16;  —  kasna  djritä  zqmcä  ads  na- bäsiä  avapastöÜ {%A)  Y.44.  4;  —  s.  noch A.  ß)  den  Leuchten  des  Himmels: yetihe  växi  ,  ,  us  ava  raocä  asnaoiH  ava pairi  tmqm  sqm  jasaiti  Vt  70.85;  89, H.  7,  21;  —  ka^a  avatbyS  sitnbyB  aoi zqm  Yt5.85.  a)  Im  Gegensatz  lu Wasser  'Erde,  Land,  Festland':  aSavat apal  haca  nilbäraym  huskei^'A^  z?me''' nidaiiiyqn  V.(7. 29;  31;  —  zugleich  im Gegensatz  zu  Pflanzen:  zqm  akuraläiqm äptm  ,.  urvarqm  y.ig.$$;  5.33,  4a,  77. I,  a,  5,  9,  H,  7. 3;  —  Aa^a  apaj ..  z^mat •  ■  S^H  ,  .  urvarayät  V.  77.  10;  —  nava 3fs  .  .  tä  ..  urvarä  V.27.3;  —  ta^a fanti  sartta  äps  .  .  s»mB  . .  urvarayä V.  7. 3 ;  —  auch  Flur. :  imat  vS  äpS  Jaii- yemi  . .  z}mB  (VP.)  . .  urvarä  Y.  Ö3. 1  a;
7163:-daha, naham, атуйћа bagaha, dvahanam, Giira- 
8537:‘town’; dvahanam ‘village’; didà ‘fortress’; kaufa 
14348:‘fortress, stronghold’, vardanam ‘town’, dvahanam 
17145:33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 
20010:46 & : kartā : Abirádus : nàma : àvahanam : Ujaiy 
22911:dvahana-, and in the second parts of compounds 
24118:dvahana- sb. ‘village’ (5166): deriv. (8147.1) 
24120:‘being’. dvahanam DB 2.33; DSf 46. 
28911:vah- vb. ‘dwell’, see àvahana-. 
29029:IT, ТУ), ‘Conqueror, Winner’ (hardly *vivahana-, 
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
4358:•  j.  an-a'sp3r«nah-  n.  'Unvollständigkeit' : 'iiS  vastrake  N.pi.
4368:•  j,  an-^azdya-  Adj.  'nicht  fett,  mager*: nSit  pasusLO  (statt  IS.)  iazda  nsi/  irista (sd.)  {nOit)  °ya  ratufris  abanta  airista *asdya  .  .  N.  ^6;  —  ratufrii  *paysbis  . . ^azdyäisca  *'\\iuca'^^  .  .  pitus  .  .  *atdysii n5it*°yäis'K.  mskSmua  rTzuüa..  *asdyäif näit *'y3is'> N.5 7 ; — ratufris  carTmanqmca pasv.vastranqmca  .  .  *asdyanqm  nSit *'yanqm ''    (nämL   pasunqm)  ^     "r.    wird
5863:•  j.  a-sp3r9nah-  n.  i)  'Yollständigkeit' : °nS  vasirake  N.57,  '''pö'';  —  nSit  'tis vastrafieü.ijG.  2) 'Integrität':  katanm *a>:rava  aiaurumm  vä parayat gai'ijanqm va  -nS  avap  gai^anam  °nö  avffij  "Soll ein  Priester  auf  Priesterdienst  aus  (dem Haus)  gehen  oder  soll  er  für  die  Integrität seines  Hausstands  sorgen?  Er  soll  fiJr  , . sorgen,"  N.j'*.
6710:9)  Pu. :  vastrai  yal  /läl.  —  '")  Them.  So  (aia*) durchaus.  —  ")  D.  i.  '^aky,  Konj.;  ai.  äiasi.
7487:•  j.  'äste  Praen.  mit  Gen.  'mittelst,  mit' : yai  vä  ..  *aipi.?r3tS^3tus{sA.)  aeta'.a  aitahc (näml.  vastraAe)  ä'  stairi/ü  liar^ztsia hqm.vir?närtte  ".  .  dann  sollen  sie  damit ihr  Lager  und  ihr  Kissen  zudecken"  V.
8330:•  j.  ratu/ris  canmanqmca  pasu.vastra- nqmca  "upajaeäaätnÜä '* "  fraoiritarst n'almät  N-i«?'*.
9062:mit  lii,  niy  'eingraben,  verscharren':  yö iiars  .,  irtri'iusS  zumc  kshrpa  nikaiiiti  V. j.  40  PüZ.;  —  altafia  ..  aSta  vastra  fraca k3r3ntm  niia  kanaym  V.  7.  12;  —  yat aialta  zimS  nikante  (3SPM.)  späiias^a  .  . ttimskante  (sd.)  V.J.  36;  8;—  jarW  (sd,) .  .  zjme  nikante  (NDf.)  V.  7.  47;  j. ra.  a)  II  'vergraben'  sva.  'aus  der  Er- innerung verschwinden  machen,  in  Ver- gessenheit bringen':  uta  lyt/'  kunavahy ava''faiy  a''ura''mazdä  nika''tuv  "und  was du  tust,  das  soll  dir  AHM.  in  Vergessen- heit bringen"  Bh.  4.  1 7  ''.
9846:rfüssigen  Tieren  versehen,  be- byasca  haca  - maitibyasca  H. 'mit  Fleisch  vei  sehen,  Fleisch myatdim  .  .  'm^nfyrrt .  22  ■>;  —  4j  fiB  ..  paiti^anät vastravata  (sd.)  Yt  13. 50. i/-  EN.  i  femer  gaoman-  und  gae- aL  gimant'  Adj.  —  Pö.  (lu  l); d,   (lu  j):  göUSmand.   —    >)  Vgl.
10456:zu—'(A'k.k.):uzgpr3pipmaJ  siia>pm  apasa apa.:^anvaii:tiisi.)\t.s4-^6-  4)  'aus-, anbieten':  uzgprpptilt  paiti  draoriät{sdS) nava  uzgirpptaiN.^.zd.  5)  'wegtun, ausziehen'  (näml,  vastra"'>)\  u:g3iirvayJt vo/iu  mariB  "..soll  (die Kleider)  ausziehen" V.  Jp.  23.  6)  '(mit  den  Sinnen)  auffassen, wahrnehmen':  aal  Um  vatam  naiihaya *uzgrsmbayS"'>  saoayeiU  (sd.)  H.  2. 8, 36.        ugg}urvayal  Vd, /j.
11045:Aqscay.31.11;  32.11, !tJ.iS,45.'i;  —  ivaya ..dn-alai^a  asoonaita  Yt, /o.  2; — /.iuyan- taScä  västryäicä  Y.  2p,  6 ;  —  Aaväi  kämäica taosSua  YtJj,33;  —  yavas^a  yavaSätae'a Yt/j.So;  —  n>r»byasca  näiribyascä  Y.54. i;  —  niayal^a  upa.b»ntayal^a  N.  4S',  — tayäal^ä  Aazatghaicä  Y.  12.  2 ;  —  asnaatca xsafnaat^a  Yt  5, 1 5 ;  —  aiwtta^aca  spasi- 'ta^acaYtig.6;  —  %waAmaj  3'^riis^a mana»Aas/ä  Y.46.T, — glusca  vastraheca Yt/J.ioo; — apB  yat  snaliintylica  sras- äntySica  V, 6. 36  (s. dagegen  33 ;  Sp.564m.);
11708:jAw.'*:  i)  'darum,  deshalb':  nSil  tä  näi- rika  iasujera'huia  (sd.)  N.  40.  2) 'dann, alsdann':  ann  tä  vaiöTm  (sd.)  ayh  V.5. 5; kat  tä  vastra  kqmyäla  (sd.)  pasca yaoidaiti  frasnäiti  (sd.)  V.  5.  57 ;  58;  — '  1/  tä  Tiara  irisla  .  .  nasuf  upa.dvqsaiti V.  7. 1.  a)  vorausweisend  auf _j'J 'wenn':
11941:•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'  usw.  gebraucht  werden: ya  anrS  mainyui  frak?rfntat  avi  imqm 'nüm  yam  masyänqm  V.  20.3;  5;  s.  noch lu  aj  —  ks , .  a%r3  tafitus  äärayat  'naot haca  maiyehe  V.  20. 1 ;  —  yasca  .  .  dax- manam  avavantim  mazS  vXkänayat  yaha hl  'nui  anhal  V.  7. 5 1 ;  —  {yai)  *may'iain 'nUm**  aiwyästam  (sd.)  "irlris  .  .  N.  p5; *95^>  —  '*'"'  panna  (sd)  °nBm  aiwi.- si/ais  YX.  14. ^5 i  —  yaf  kl  'nus  hiskvi Aiynvi  (sd.)  pqsnu  bavai  V.5.31;  —  &«.- ayarpm..  'nüm  frasnayayania  Yt/0.  laz; 133;  —  US  'nüm  snayaita  us  *vasirä  V. J.  54;  —  "^ris  frasnaiti  •nunqm  . .  vastra- nam  V. /2.  a;  —  hakmt  aps  hvqm  'nüm pairi yaozdai^ita  V.  (),3i;  31",  ä  36,  37, 39,  Vd./5,  ig*,  20; —  Ja/  vlspam  kvam 'nüm  ayaozdata  k>r>naoiti  V,  ■¥.40;  — yal fU  zasta  nöie  frasnäta  aai  vJspam  hvqm 'nüm  ayaozdata  ik?n>»aoiti  Y.S.40; — yffi Aqm.nasüm  paitiäristfm  °nüm  yaozdai%yqn V.g.i;  —  iia  iristahe  'nüm  avaMsta  .. isaaa  (sd.)  ml  yaoldaitim  V,  Ä  100;   —
13354:•  j.  dädaray-  Adj.  'der  etwas  (Akk.)  be- sitzt': yai  asp>r?nB  vastrahe  . .  'rayS  (NP,) a  anaiwySsH  strmti  yezi  sat  nSit  asp?r}rw vastrahe  .  .  'rayS  nSit  ^anaiwyästt  "wenn  1 sie  ein  vollständiges  Kleid  . .  besitzen,  so versündigen  sie  sich,  wenn  sie  es  nicht! anziehen;  .  ."  N.  96".  1
15871:*pasu.vastra-
15876:•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
15878:•  j.  'pasu.vastra-  n.  "Viehstall';  az3m  . .
16580:mit    «pa    dn.:    vastrA  .  .  upa.baoiayqn
16685:'Biber':  bawraini  vastra  . . iqm  *caturS  elzanatqm{s6..) 3n  dreihundert  Bibern  . ."
16806:tarn  arstim  barai/iYt.  10.21.  5) '(davon- 1  nanbyB  .  .  V.  77.  4;  —  ydka  ..  am?r7xtim tragen  sva.)  gewinnen;  empfangen':  yänä  avaiaräni  ..  Uta  az?m  apaiaräni  ..  sk- (sd.)  baraiti  astavB  va  .  .  m^nyahe  Yt.  o^m'a  tars/amca  haca  maata  dämaiyS  Yt 14.3^.  a)  mit  refl.  Dat:  paourva  ?ü  g.^i-;  10*; — ya  haca  daevayasnai^yü . . fumS  baraiti  "zuerst  gewinnt  er  sich  .  ."  apa.bara{^S2ih.)'^^  aya  ratit/H/"w3sinajk Yt  14.36.  b)  mit  Abi.:  iahmät  .  .  1  den  D.  ..weggenommen  hat,  damit  wird Aar»hr?m  barUi  "von  wem . .  soll  sie  Pflege  man  r."  N.  ^4;  —  mt^ram  . .  yS  nar^m  apa empfangen?"  V. y,  17;  16.  6)  'halten,!  qxanhai  baraiti  ". ,  aus  der  Not  (fortträgt pflegen,  behandehi  ab -';  die  Bestimmung '  sva.)  befreit"  YtJo.az;  aaf.*.  b)  mit erfolgt  a)  durch  praed.  Akk,:  \avam'G^vi.:  yS  daii^hSus  . .  apa  v^n%rajtum **uiaratam  abaram  "den  hab  ich  gut  ge- .  iaz-fl///  Yt  70.27;  —  «/«*  aeiqm  bärvä halten  (behandelt)"  Bh.  /.  8,  4-  13;  — ^aojd  .  .  barahi  Yt/0,a3.  c)  mitDat: in  pass.  Wendung:  *driyümca  drJvJmca'kahmäi  xiäimm  .  .  paiti.da'häni  ..  koA- ara%wyS.b?r3te  (sd.)  barimne  (ADf.) "' !  mä/  xi^dinm  .  .  apaiaräni  Yt  10.  109— P.26.  b)  durch  ein  Absolutiv  (sd.)  zuliii.  d)  mit  enkl.  Gen.-Dat  desPron.: ^bar-.  ys  vohu.b3r»tqm  baraite  milir?m  Yt  \apa  hl  vastra  baraym  V.5. 49;  —  ku%a 13. 18;  —  yS  nS  hub?r3tqtn  barst  Yt  1$. '  te  aam  *apavaräni''''>  navaca  yaskS . .  V. 40;  —  yö  nä  his  kubfnta  *barat  Yt  22,6.  a)  'Jemanden  bringen  um  — ', y-  >8;  —  ya'ha  duibirmts  *barailt'**  (in  mit  dopp,  Akk.'**:  jvö  . .  drvä  .  .  nar^m pass.  Sinn)  Yt/0. 48;  —  ya^a  Aub^ntS  asavarum  hanhus  }fan'i:ahaa  .  .  apa.- *baraite"^  (in  pass.  Sinn,  näml.  mthrö)'  baraiti  "..bringt  (er)  den  Gläubigen  um Yt/0,  112.  7)    mit   AS.    vääirt    'die  j  die  Nutzniessung  . ."  V.5.  38.         2)  'ab-
16817:a)  '(Kleider)  herabziehen  sva,  von oben  her,  über  den  Kopf  her  anlegen'; yS  vastra  vastnm  *aiwyaithaysrii  *itzba- rmti  (sd.)  . .  uparat  ftaOnai  ava-bannti  . . N.pJ.  a)  'hinzu-,  herzubringen,  ver- schafien':  *yaoxHayS  ava-bantam  (statt Hur.)  F.  4  g;  —  cvat  gaonahe  (sd.)  ava.- barat  N.  65.  a)  mit  Angabe  des  wohin? oder  wem?,  a)  durch  avi  mit  Abi.:  ya^a ..amirjxtim  ava,baram  avi  mazdä  däma- iysYt.g.^;  9.  ß)durchGen.:  ya  vTspa- nqm  hairisinqm  .  .  rähwim  paima  ava.- baraiti  Y.  65.  2.  y)  «n^^-  Gen.-DaL  des Pron.:  ava  hl  gatam  baraym  afryeAe  (sd.) va  ..  V.  Ä  8;  —  Uta  hi  astunt  xratQm avaJiaraiti  vanma  (sd.)  Yt  //.  a;  V.  16. II.  3)  'etwas  anbringen  an—'  iupa mit  Akk.):  ava  hl  baraym  .  .  dsuru(sd.) Ufa  . .  manae^rfm  V.  13.  30.  4)  'etwas
16837:anlegen':  ys   vastra    z-aitr?m  *aiivyänha-        mit    parä      i)     'wegtragen,     -bringen,
17118:•  j.  bamaniva-  Adj.  'glanzvoll,  herrlich': !  iumhtiMi.  —  0  S»»,  j'ara-  iaäu.vchum:  — vastrasca  JbsA  'v.'i  "und  herrliche  fertige.  '>  So  T.  —  j'  Die  Eil.  daiu  in  F.  35b  ist Kleider"  Yti7.i4;  zitF-j.  nicht  kl«;  wohl.  ,«.  ^«-.ü«  ««ira.
17383:•  j.,  g.  buray-  Adj.  "reichlich;  völlig,  voll- kommen': 'uiri  gaos  'uiri  ^an^a  °u:ri vastra  'uiri  anyaHbyS  mazäayasnaübyöyyi. 4^ ;  —  masdä  dadat  ahurS  . .  'ärsis  ä  . . :^'apa^yai  (sd.) . .  Y.  ?7. 2 1.  a)  Akk.  mit 'kar-  'etwas  (Akk.)  völlig  machen  sva. (Erhofftes)  erfüllen  mit-'  (Instr.)":  mat- damüä  'airiiä  ksrt^ä  räitl  isi  xrapaitJ (sd.)  ahmat  hyat  aibl  hyat  mtzditn  . .  V. 40.J.  '        '
17949:•  j.  fra-snätay-  f.  'Abwaschung':  kat  tä vastra  hqmynta  {si!L)pasca  yaoidätti  'snäiti (IS.)  "..nachdem  sie  zum  Zweck  der  Puri- fikation  gewaschen  worden  sind"  V. 5. 57; 58;  —  ^ris  'snäiti  tanunqm  'hrif  'snättt vastranqm  V,  12.  2.  DS.  'snätse  als Inf.  sbes.
17963:srüvayS . .  apar?m  xraoidyehya  (sd.)  'irBiti Y.rj,  14;  —  ^ris  /rasnäiti  vastranqm  %ri/ •srüiti  ga%anqm  V.  12.  2.
19142:•  j.  ni-8ätay-  f.  i)  "Nieder-,  Ablegen': mal  vastranqm  'läitt  V.  6.  27.  2)  'Ver- bergen"': ya^a  nSit  *aiii  (sd.)  '^äitiifa *airisya  N.  6-y.
19676:—  tofniiu^  (sd.)  m'  aiana  m*  .  .  ays.- ayraHV.i4.9i  9,  14,  F.Bb,  /;;  —  mitDP. statt  IP.:  nar^m  .  .  m'  avaby3  daxltabys ya%a  a%rava  "einen  Maim  . ,  mit  jenen Merkmalen  wie  (sie)  ein  Priester  (hat)' V.  y.  aa;  —  tava  a%rS  . .  m'  vtsfiatibyB aündyS  Y.1.13;  2,12,17.11,22,26,  Ny. 5,6;  —  w  vTspäby!f../ravaMySY.23.3, 24.  5.  «)  von  einer  begleitenden  Hand- lung: m'  ao%ranqm/ramuxH  m'  vastranam niläi/i  upa.manajitn (sd.)  V.5.27.  b)  mit Abi.**:  draomSbyB yä  alimS , .  drävayat vüstaot  daevBJatät  ¥.57.25.  a)  mit Gen.  (statt  Abi.)'):  xfvis/!a  (sd.)  azüitisca ^uf  ftt' Y .i^.i^; — haTfuhar>ne*m'  hiwvS^ Y.  n.  4;  —  m'  *nizbayehe  Vd,  12.  [V. J4.15:  lies  mai^^
19886:urvaisi  jass  (Sp.  494  o.)  matda  xia%rä ahml  vohü  manatihs  Y.43.6;  —  azfm täis%wä  fraxhil (sd.)  avami mazda  spstUH 'inyü  vispanqm  dätänm  Y.44-Ti  —  ahmst '''inyJus  rSr^^dnfi (sd.)  dngvani5..spmtat Y.47.4;  —  mainyü  (Sp.  1125  m.)  yayä spanyi  (sd.) . .  mravai  ylm  angram  Y.  4^.  2 ; ■ayü  *mainivä(Sp.  ri25  o.)  varat3..aüm tyui  spStUstS  y!  xraozdtÜJng  asSnS  vaste (sd.)  Y.JO,  s;  —  :^l(hr3m  daidlta  %wil.. fpSni^ta  °inyB  matdä  ". .  per  tuum  sanctissi- mum    spiritum,    o  M."   Y.43.2;  jy.  ra,
20232:—  aj  vS  yaofa  zivlstyii^  (sd.)  aurvats  .  . 'da  a/a  ugryng  vohü  manarfha  Y.  50.  7 ; 33-  7,  8,  34-  5.  6i  4^- 1  a,  49-  '■  c)  in andrer  Verbindung:  tat  vS  nS  hazaelänhö (sd.) . .  daidyHi  tavS  ahm  vohü  mananka ..armaiHfyaamnänAsisA.) ..  'da  raßlnm (OgftÜ'i. 51.20.  a)iinjAw.:  vTsasttna ahmt  yat  ahmt  'da  nqma  Yt/.8'>;  — ahura  (Sp.  386  m.)  nqma  ahmt  'da  nqma ahmt  Yt  1.12'^;  —  sfviits  bavahi  ya%a 'äi  Az.2;  —  neij  xsnavaydH  ahur^m masdqm  . .  yB  *dqm  tarS  manyete  Yt  10. 139;  —  J"^"  ""^  avaahe  'da  Y.  72. 9. Ny.  J.  9;  YtJ.  3^;  —  asmamm,.ycm  'da vaste  vanhamm  Yt.  JJ.  3 ;  —  yau  tava •da  ktrmaot  taÜan  . .  Yt5.  90;  10.  92;  —
```


## [2026-10-17T00:01:26.353Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'past[oö]\\.fra\\|pastö-\\|Haut' BRT.txt | head -20; grep -n -i \"^ *904 *$\\|^ *903 *$\\|^ *905 *$\" BRT.txt | head"
}
```


### [2026-10-17T00:01:26.723Z] TOOL RESULT

```
2072:Alk.:  Hatnicat  i  Hitrav  i  JCaväiän.     Ausgabe;  %.  bei  Aam. (A)Baktiiei.uiy  Gab.:  Gujaitak  Abalitb  (Bibliothique  de  l'fcole  des  hautes  etudes.     69.  fasc).
2578:31;  3''.  35'*. "^-85;  —  tts  haca  nassvö  °vat  •  j.  aeJa-m.,  Plur.  'Kopfhaut';  '',a  ..*kay:i apat Aaca ni:iiiraj-fnV.6.$if?); — asH.masÖ  fi^nti  masyat»hd  'r,a  *ydi  *aparaya  paiti xraoidi'aAe  bis  'rate  lar^AaAe  "..h\s^3iXtto  *)tiastrfynaya..*kaya  kasya/i/t^  *yüi  *paou- mollisligni"  V.  jj.  30;  —  'val  apayaiia  H.  ruya  paiti  *mastrr/nya  "Kopfhaut.  — iog(X).  a)  mit  dem  Korrelat  _v(K'a«/- :  Welcher TeilderKopfhautistdergrössere? ^t/ (sd.)  °vat  htT^r»m  yaval  tacantn  F. '  Der  an  der  hiotera  Schädelwand.  Wel- 27a;  a;  ■ —  yavat-  hatca  hl  sastaiibya  eher  der  kleinere?  Der  an  der  vordem hangturvayqn  'vat  apat  haca  nizbärayfn  Schädelwand."  F.jc. \.ti.2t);  —  'imt  npö  yavat ,  .  J^.ioX;  — 'foiö  zaota  (iäm\.  ratu/rii)  yajat ß-ama- raiti  "mit  so  vielem  ist  der  Z.  r.,  als  .  -^  „  . n  (selber)  .ufsagt-  N.  2,1  2,,  23,  »>',  \  )■  if^  'a.«,y<,il„t  pa,U  afa  .  .  N. j'P.  Aa)  GS.  'vatö  als  .\dv.  'quantum  ^  j-  .  j^j^j^ sat  est,  in  hinreichendem  MassM?):  hura-  "  ^^.^  ^  ^  ^^^  ^^^^^ ysscti  (sd.)  a(.a  Tato  datdyat  A.j.4;  —  .   ^i%y^_^.^^,„„  -(.^5.  y^s  ka^i^yStarlum.
5660:Eig.  'Sichautrichten,  Geradesein' ;  lEt.  s.  arsla-.
6228:•  j.  aäava-x&ivaitya-  Adj.  'den,  die Gläubigen  zufrieden  stellend':  tum  haut txhi  vaauhi  raiti  °tysi  masyät  YtiS.^.
6747:iSi  ahautstö.tamö^h^äta-  —  'ahu-  282
9212:yaona    *car3nta'^    "(Leute)    die    dauernd'      mit  haut  'sich  ergehen':    i'^a    ml  tum angemessener  Beschäftigung  obliegen"  '^.\  hamJaraifuha     *antar>.arj',em     nmänahe
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
12088:_     _  .  T      .T      -•  I         ..1         ,  speziellen  Geener  von  Hautvaiäl  und  Amsritit
12319:Stammauslaut  und  Bed.  unsicher.  DsT.  ZA. 3.  92  'cd  terre';  Jh.  Reader  95:  "the  bancs are  to  be  placed  in  stane  osinarie»,  or  in terra-cott«  vases,  or  in  bags".  M«n  bat  ai. Itiai-  t.  'Haut,  Decke'  und  np.AflW  "Vorhang' verglichen.  —  PO.:  tuxittiUär  AOiä.
12376:*  p.  tya-  Pron.  rel.  (fem.  'yä-")  'welcher, wer,  der';  I)  als  eigentliches  Relativum; 1)  mit  einem  demonstrativen  Korrelat,  das i)  folgt,  uzw,  a)  aita-  (Sp.  13  u.):'  datam 'yJ'  mana  aitJ'  ^adariy  D.6'.3".  b)  ^ava- (Sp,  166  o.):  ya^säm  Aa/ama*  ahahyJ' . .  avi^  *akunavayi^t3  Eh.  7.  7 ;  D.  6.  3,  4; —  •_)'«*  kunavahy  avt^iaiy  .  .  Bh.  ^.  16, 17;  —  Uta  'yJ'maiy  p^'^e^  kartam  ava^- ay  . .  X. z.  i;  3.  $;  —  '>'«*  maiia  iariam idä  Uta  'yJ'maiy  apaiaram  iartam  av(^ visam  X.  2.  3;  —  'y^patiy  (sd.)  kartam vainataiy  naibam  (sd.)  ovo'  visam  .  .  X. 7.  3 ;  —  'yaiy  paruvä  xiaya%iya  yata  aAä" avaijilm  .  .  'Bh.4-  9;  —  xsa'S!''am  'yo'' . . parabartam  aAa*  ava*  .  ,  Eh.  7.  14;  — martiya  'yatsäty  Jraiamä  anusiya  akd'ia flufl/)'.- Bh, 2. 13.  a)  vorausgeht,  uzw. a)  ima-  (Sp.  371  ni.):  («a*  /v«*  adam akunavam ..  vasna  (^ur^mazdaki^  akuna- vam  Bh.-^i2;6,  2,  Am.4(?);  —  dahyavt/' ima  "yä  Aami^'iyä  abavd^  draugf^dU hamtk^iya  akunauf?,\i..4.a,; — imam  dipim ..'yam  adam  myapisam^.4-'^  <,.  b)  ^ava- (Sp.  165  m.,  167  m.)t  ^ava  dahyavJ"  'yä darayJ'vJ'us . .  adaraya*  'D.6.4;  —  ovaAya kärahya . .  yam  vahyazdatt^  fraisayt^  ßh. _^. II.  c)  sonstige:  iyam  dakyaus . .'yam manä  J'urJ'mazda  frabari^Yi.4.3\ — hauti karJ'  asiyavt^  'yam  vaAyazdatt^ /rai/ayJ' Bh.  J.9,  3)  eines  geht  voraus  und  eines folgt:  aiti/'  x^a%'am  'ya^  gaumatJ*  .  . adfna*  kt^hnfyam  atta^  x^dÜ'am  . .  Bh. 7,  la;  —  aita'  'ye^  kartam  avi/'  visam  .. D.  6. 5.  2)  ohne  demonstratives  Korre- lat; i)  das  Relativum  bezieht  sich  auf  ein
12944:'zu  Gesicht  bekommen,  erbUcken,  er- schauen': caräitii  .  .  yqm  it  yava  carSiti- aqm  hhrpa  sraiitqm  dädansa  ". ,  das  an Gestalt  schönste  von  den  Mädchen,  d^s ich  je  zu  Gesicht  bekommen  habe"  H. 2.10;  Y.5.  i;  —  ttla  kal  %ws  dansäni matuuca  vokü  vaidfmnS  "o  A.,  werde  ich dich  erschauen  und  den  VM.  als  ein wissender"  Y.  2Ä5";  —  a/a  vahisia  .. darjsäma  %W3  pairi  %WS  jamyama hanam  %wa  Aaxma  (sd.)  Y.  60.  la";  — kumqsdrä  (sd.)  asä  yecä  yä  raocübls  dan- jflöljSKM.)  urvasa^.30.\.-,  —  dar?sat'^ F.  i4;  —  darsstä.'.  a)  vom  visionären Erschauen:  hyaf  hufä  aipAsui  zaiiSi  dan- sjm  paourvim  "als  ich  dich  zuerst  er- schaute bei   der  Schaffung   des  Lebens"
13648:f  «'«>"^£«''"^  ■-."'■■  "d^n  sollst  'k^(s^'^f,:^]^XA_2',-asim..'TL;^m du  einen  Pnester  oennen.  .  .  der  . ."  \ .  „^^^^^^  ^^j  y^  _  _  ^  ^„^'  ^^ iÄ6;  -  <7/^r^  (^)  .  .  m  d'a2-a>a  f„^^  sr»,«/i,7)  -y«»  <»>l«r<7^  »,«,/J  V. /«/,««  fsd.)  y.75.48;  -  yat  hanö  -  .,,^.,3.  _  ^^  ^^^  .nämL  maUh)  'g^ä bm-äl  aojjst^mca  d-  pascaaa  mazdayama  ^^^„„^^„3  s„naitis  Y.J3.4;  —  Pm.ru- tanast,mca    .  .  pastö.fra^a»,h^   (sd.)    h!    .^^^.  .^,^   ,^^^^    far^i^^^  Y.
15999:Hautkrankheit):  tßil  t^ra  airyi  daifihävB
16333:•  j.  pj^sta-  m.  'Haut',  bes.  die  behaarte des  Menschen:  '/aha  F.jb.
16336:der  (behaarten)  Haut  sva.  soweit  die  (be- haarte) Haut  (des  Kopfes)  geht'":/"  hl iam^n^pm  vtnä^ayen  (sd.)  "sie  sollen  ihm den  Kopf  schinden,  soweit  das  Haar  geht" V.J.  zo;  —  yaäia  yal  Ag P'  kamsri^sm hiirpnuyäHSp.452  u.)  "als  ob  er  sich  (selber) den  Kopf  schindele,  soweit  das  Haar  gehl" V. /<?.  10.
19146:Vermutlich  verderbt  aus  niiätöMtiäi-  'wo(rin) Polster.Kissen  niedergelegt  sind'.  DsT.s  'hautet sur  leun  bases',  ZA.  3.  451  ist  unmöglich. ■  j.  ni-därant-  Adj.,  PPA.:  s.  ^dar-.
20384:•  j.  mar^STvant-  Adj.  'denkend  an  — ' (Lok.  oder  Akk.):  aimianqm  spmtanqm.. yagiqm  ainyS  ainyehe  urvärum  aitiii.vai- naiti  "wtnüm^  kumaiaüsu  .  .  fiüxtaäu  .  . hvarstaisa  'wmt»m  *garif  nmärum  ". .  deien einer  auf  des  andern  Seele  schaut,  die  an Humata  denkt . ,  an  das  Paradies  denkt" Yt/7.84">.
20617:ai.  vgl.  '»/■'diu-  Adj.;  s.  GtiN.  KZ.  2/.  249, Bthl.  AF.  2.130. —  Vgl.  kamiifatay-,  p.EN. 'AiiäTpr,l.  —  Pü. :  öhtmazdm  an  i  hatnäk  han- jamanikih  barim  asttj/ahiitia,  erl. :  kusän  haute- !ak  kanjaman  apar  tan  i  pasin  tuniiti.  — ')  NA.  getrennt;  s,  No.  2.  —  ")  ä  mSya'  (NA. ä.möya')  statt  ä  mya'  wie  in  hävdya  (S  268. 13);  s.  auch  ä  vdyn%rä  Y.  34.  10.  —  J)  W* hierin  die  Anspielung  auf  die  Bd.  30. 10  ge- 38-
22015:—  *ahnmMl  (sd.)  vidvä  Y.31.  19;  6, 34-  10;  ■ —  ärmaitTm  ..  bfnxoqm  (sd.) vidusB  Y.  34.  9;  —  at  vatdftnnäi^'' vaAii'tä  säsnanqm  (sd.)  "für  den  Wissen- den .."  Y.^-S.  3; —  asä  hat  ^wä  dansänj (sd.)  .  .  vaidpmnB^'  Y.  2S.  5;  —  AvSvt a/aom  vi^ufi  Ytlö.  15;  —  mä^raca spsnta  vidusa  Yt.  13. 146;  —  AyaJ  itü fryäi  valdamnB^'>  isvä  (sd.)  äaidlt  Y. 43-14; — :acf,l  (sd.)  fi-a  mimrGti../ra asava  vitva  mraotü  Y.3.  3$;  — J>ai/i  mi vl^va  mrüiZi  Yt  12.  i. sein':  aim  msi  ida  vistd  yS n3  agi'U  säsriii ,  mit  aiwi  i)  'wahrnehmen':  manhsm (sd)  güsatä  "der  ist  mir  hier  als  der  einzige  1  aiwi.vainsm  .  .  manhim  aiwi.vJsim  ^'  "auf bekannt,  der  .  ."  Y.  25. 8"';  —  ki  mSi  den  Mond  schaute  ich  hin,  den  Mond pasSui  ks  tns  na  %raia  vis ts ..azdä  {sd!)  habe  ich  (jetzt)  wahrgenommen"  Yt  7. zütä  Y. 50.  i'"';  —  hä  ii  anhsu!  vatfuhJ  3.  3)    Kaus.    'zusprechen,     zuweisen,
26062:•  j.  3sar-  f.,  Du.  'die  beiden  festen  Be- standteile des  menschlichen  und  tierischen Körpers,  d.  i.  Haut  (mit  Fleisch  usw.)  und
16308:903
```


## [2026-10-17T00:01:30.546Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16305,16340p BRT.txt | cut -c1-600"
}
```


### [2026-10-17T00:01:30.952Z] TOOL RESULT

```
•  j.  pouru.8päda-  Adj.  (fem.  'lä-)  i)  'der ein  zahlreiches,  grosses  Heer  besitzt*: xsa%r»m  .  .  'osm  Yt  10.  109.  2)  'ein grosses  Heer  bildend':  a/aunqm  ..frava- st^5  .  .  'U  Yt.  13.  37.
Vgl.  die  seltsame  Wiedergabe  des  Worts  Zs. 2J.  10.
dby  Google
903
pouruSa-
j.  foUTUS,  g.  faurüs  usw. :  s.  unter  parmi:
•  ).  pouruia-  (,  paourusa-)  Adj.  'grau, greis';  *°sö  asti  varsS  "greis  ist  das  Haar" V.  -.  57  Gl.
KompA.  —  ai.  farufä-  Adj.  'flecltig' ;  vgl. falitä-  Adj.  'grau' ;  op.  flr  'greis' ').  —  Pü. : pTr  asi  vars.  —  ')  NA.  fouruhi;  s.  Var.  und Pü.  ^  '1  In  np.  pir  l)  'canus'  und  z)  "pristi- nus'  sind  iwei  urspr.  geschiedene  Wörter  lu- sammengefallen.
•  j.  pourusaspa- '*  m.  EN.  des  Vaters Zara^ustras:  'ps ..yat  hi  tum  ussayaaha .  .  tara%ultra  nmänahe  'paheH.g.xy,  V. IQ.  4,  46,  F.4£;  —  puhnm  yai  'pahe  . . zarahustnm  Yl  5.  18;  V.  jp.  6;  —  mä OtaraySis  saraiustrake  {sXaXXVS.)  mä  'pake (statt  AS.)  mä  duyts.vqm  "erziime  nicht,  ■ oZ.,  den  F.,  nicht  die  Z»."  FrD.  ^;  — I pouru.aspB{sA.Y^ yä^a  'pahe  Vyt2  ";  hz.4.  \
Komp.:  f^HruSa--^(ufit-  (S  36S.  3),  eig.  'der graue  Rosse  besitzt',  Bfi.  p.  312;  vgl.  No.  2.
—  ')  Vyt.  a  steht  faoiir'.  —  >)  Ein  miss-  1 lungener  De utongsv ersuch  des  Namens.
•  j.  pouru^y-  m.  EN.  eines  Gläubigen:  j °tBis  kavSis'isÄ.)  osaonS  Yt.1j.114.
Eig.  Bed.  ?     Ot>  Komp.: /3rm-+itt/,y?  |
•  j.  pourus-x'^Sra-  Adj,  {fem,  'rä-)  'der  j viel  Behagen,  Glück,  Wonne  gewährt':, alis  'ra  Yt.  15.54;  —  kahmsi  istlm  °rqm\ azim  baxsäni  Yt/o.io8;  Y.6Ä11-
Vgl.  fauru.3?'ä%ra-  und  S  304  H.  45.  —  Pü. :  | pur  ü^äriA.  I
•  ).  pouru-hazaura-  Adj,  {fem.  'rä-)  'viele  I Tausende  betragend':  äat  fralüstnti  .  , fravasayS  paoirll  pouru.sata  ,  .  'ra  .  .  \ pouru.daevans  Ytij.6$i  —  a&a  un}ara\ balsazyä  uzbanm  paoirjl  pouru^ala  . .  °rä  I . .  pouru.baevanS  V.  20. 4.
Pü.:  pur  hazar.  1
•  j.  pouru.x''ar9nah-  Adj.  'der  viel  Herr- lichkeit, Glanz  besitzt,  hoheitsvoll';  °nat»Ad (NS.)''  asava  sarahusIrSY .ig.y, — 'nanha (VS.)"'  ahura  mazda  Vyt.  2.^'*;  —  yasata 'naiaha  (AP.)  yasata  pouru.bailaza  Ny.5. 6 ; —  yazata  'nanha  (VP.)  Ny.  J.  1 1 ;  — jc^arj»?  "««»^iffi  (ASm.  statt  n.)  Yt.iÄi.
Pü.  (lu  V.  I()):  Hai  pur  i^artih;  Npü.  (lu  Ny. 3) :  pur  ^irrah,  (lu  Ny.  S):  pur  nur.  —  ')  Them.
—  »)  Hier  paour'.
•  j.  pouru-x^äSra- Adj .  Aavi.pourus.:i^a^ra- ; i)  von  Gottheiten:  'r^m  {statt  NSm.)  bavähi
yaha  rämanS  ifästralie  Az.  7;  —  'ra  (statt NSm.)  nqma  ahmt  (näml.  AhM.)  Yt.  j. 14.  1)  von  Bergen:  vXspägarayS  aia.-
^^rä  'rä  Y.  2.  14;  —  vupaisqmca  gairi-
aia^'a^ranam    'ranqm  Y.7.14,  Vr.
•  j.  pourva-  Adj.:  s.  unter  paurva-. j.  pourvacqm  Y.  g.  35 :  lies  fovru.vacifni, j.  fourvB^aiä/B  V.  ig.  42 :  lies  fmin/ä  ^lä'.
•  j.  pint-  Adj.,  PPA.:  s.  'psiyy.
•  j,  pi^iian-  n.:  s.  unta  päman-.
•  j.  pasanav-  m.:  s,  untei  pq^nav-.
•  j.  pj^sta-  m.  'Haut',  bes.  die  behaarte des  Menschen:  '/aha  F.jb.
KompA.  —  Et.?  —  mp,  (Pü.),  np./äi/.   Aber woher  Ö?
•  }.  p^sto.fra^aDham  Adv.  'in  der  Breite
der  (behaarten)  Haut  sva.  soweit  die  (be- haarte) Haut  (des  Kopfes)  geht'":/"  hl iam^n^pm  vtnä^ayen  (sd.)  "sie  sollen  ihm den  Kopf  schinden,  soweit  das  Haar  geht" V.J.  zo;  —  yaäia  yal  Ag P'  kamsri^sm hiirpnuyäHSp.452  u.)  "als  ob  er  sich  (selber) den  Kopf  schindele,  soweit  das  Haar  gehl" V. /<?.  10.
ASn.  (them.)  aus  *'/ra%aA-  Adj,  —  Pü.  {lu  V. j  J):  pdst  pahnäk  äi  i  kamal  e  *kaimä,  erl- :  tu! I  sar  ape  e  brinind,  (in  V.  18):  pSst  pahnäk I  kamM  kart,  erl. :  kui  sar  iurrä  cslH.  —  »  Vgl I  lu  den  Stellen  H\ug  SBayrAW.  1S68.  2.  27, I  Gdn.  KZ.  ZV.  S47,  Stud.  /.  153,  Ggb,  ZDMG. I  34.  420,  FeMOller  WZKM.  ff.  i8i,  Dst.ZA. 2.  40,  143.     S.  noch  /rä.v>r>sa:
•  j.  pEfSnav-,  pasanav-''  m.,  n.  'Staub; jMüll':  'nus  gavg  °nuf  aspa  'nut  irrzafjm
saranim  'nus  narS  "zu  Staub  werden  die Rinder  .  ."  Aog,  S4;  —  ava  .  .  baraytn  .  ,
I  istyehe  vä  .  .  husks^manqm   v3  'nüm  V.
```


## [2026-10-17T00:01:37.000Z] TOOL CALL #12: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-17T00:01:37.010Z] TOOL RESULT

```

```


## [2026-10-17T00:01:49.672Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | head -50"
}
```


### [2026-10-17T00:01:49.959Z] TOOL RESULT

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


## [2026-10-17T00:01:57.089Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/پوست' 'https://en.wiktionary.org/wiki/بام' 'https://en.wiktionary.org/wiki/بانو' 'https://en.wiktionary.org/wiki/بهانه' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-' 'https://en.wiktionary.org/wiki/wear' 'https://en.wiktionary.org/wiki/vestis' 'https://www.etymonline.com/word/vest' 'https://www.etymonline.com/word/wear' 'https://www.etymonline.com/word/invest' 'https://www.etymonline.com/word/divest' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wazjaną' 'https://en.wiktionary.org/wiki/واستریوش' 'https://en.wiktionary.org/wiki/واستر' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram' 'https://en.wiktionary.org/wiki/vasman' 'https://en.wiktionary.org/wiki/वस्मन्' 'https://en.wiktionary.org/wiki/वसन'; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 551, roots Wes 3 / Wes 4' 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:02:04.992Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/پوست
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7e2e47bc80da4d0a.txt
== https://en.wiktionary.org/wiki/بام
/home/sfmqrb/git/rishe-private/data/verification/sources/web/17558bff3cd95133.txt
== https://en.wiktionary.org/wiki/بانو
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9cb41b658096e675.txt
== https://en.wiktionary.org/wiki/بهانه
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ef2bd461cdea148c.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c8f69f23d3ef8f2.txt
== https://en.wiktionary.org/wiki/wear
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2f3a05afbbf2b9ca.txt
== https://en.wiktionary.org/wiki/vestis
/home/sfmqrb/git/rishe-private/data/verification/sources/web/02c86fec33330f88.txt
== https://www.etymonline.com/word/vest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92af3b7363d62c94.txt
== https://www.etymonline.com/word/wear
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b7c7484bf808e010.txt
== https://www.etymonline.com/word/invest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3471461344210ed5.txt
== https://www.etymonline.com/word/divest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/20936d7ff7ffc2e4.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wazjaną
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ec8303f763882b05.txt
== https://en.wiktionary.org/wiki/واستریوش
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6572d0c89158b4a0.txt
== https://en.wiktionary.org/wiki/واستر
/home/sfmqrb/git/rishe-private/data/verification/sources/web/209b8b3af582ad4a.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2659c7064dbbd5f.txt
== https://en.wiktionary.org/wiki/vasman
/home/sfmqrb/git/rishe-private/data/verification/sources/web/57377905546001bd.txt
== https://en.wiktionary.org/wiki/वस्मन्
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e063104404fcb1d4.txt
== https://en.wiktionary.org/wiki/वसन
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b750b85d2923244a.txt
```


## [2026-10-17T00:02:09.113Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -18 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l);print(d['url'],d.get('status'),d.get('bytes'))\"; for f in 7e2e47bc80da4d0a 17558bff3cd95133 9cb41b658096e675 ef2bd461cdea148c; do echo \"=== $f\"; grep -n -i -A6 'Etymology' $f.txt | head -30; done"
}
```


### [2026-10-17T00:02:09.487Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Venezuela 200 39906
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wazjaną 200 4611
https://en.wiktionary.org/wiki/ونیز -1 39
https://en.wiktionary.org/wiki/واستریوش -1 39
https://en.wiktionary.org/wiki/برف 200 11963
https://en.wiktionary.org/wiki/واستر -1 39
https://en.wiktionary.org/wiki/vepres 200 4045
https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram -1 39
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wep- -1 39
https://www.etymonline.com/word/venery -1 39
https://en.wiktionary.org/wiki/vasman -1 39
https://www.etymonline.com/word/win -1 39
https://www.etymonline.com/word/wish -1 39
https://en.wiktionary.org/wiki/वस्मन् 200 6290
https://www.etymonline.com/word/venom -1 39
https://www.etymonline.com/word/Venice -1 39
https://www.etymonline.com/word/venereal -1 39
https://en.wiktionary.org/wiki/वसन 200 12038
=== 7e2e47bc80da4d0a
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
--
191: Etymology
192- [ edit ] 
193-
194- Inherited from Middle Persian pwst' ( pōst , “ skin, hide, shell ” ) , from Old Persian 𐎱𐎺𐎿𐎫𐎠 ( pavastā ) , ultimately from Proto-Indo-Iranian *pawástam ( “ covering, envelope ” ) .
195-See also Sanskrit पुस्तक ( pustaka ) .
196-
197- Pronunciation
--
288: Etymology
289- [ edit ] 
290-
291- Borrowed from Classical Persian پوسْت ( pōst , “ skin, hide, rind, shell, cover, poppy-head ” ) , from Old Persian 𐎱𐎠𐎺𐎿𐎫𐎠 ( p-a-v-s-t-a /⁠pavastā⁠/ ) , ultimately from Proto-Indo-Iranian *pawástam ( “ covering, envelope ” ) . Cognate to Gujarati પોસ ( pos ) . See also Sanskrit पुस्तक ( pustaka ) .
292-
293- Pronunciation
=== 17558bff3cd95133
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
96: Etymology 1 
97-
98- 3.2.1 
99- Alternative forms 
100-
101- 3.2.2 
102- Noun 
--
108: Etymology 2 
109-
110- 3.3.1 
111- Noun 
112-
113- 3.4 
114- References 
--
200: Etymology
201- [ edit ] 
202-
203- Possibly from Sanskrit वाम॑ ( vā́ma , “ left side ” ) .
204-
205- Pronunciation
=== 9cb41b658096e675
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Noun 
--
178: Etymology
179- [ edit ] 
180-
181- Inherited from Middle Persian [Book Pahlavi needed] ( bʾnwk' ) , [Manichaean needed] ( bʾnwg /⁠bānūg⁠/ ) , from Old Persian *bānūka- . [ 1 ] [ 2 ] Akin to Old Armenian բանուկան ( banukan ) , an Iranian borrowing.
182-
183: This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . 
184-Particularly: “Related to Ancient Greek δέσποινα ( déspoina , “ mistress, lady ” ) ? Proto-form might be something like Proto-Iranian *bāt-nūka- , with the "dems" part dropped off.”
185-
186- Pronunciation
187- [ edit ] 
188-
189- ( Classical Persian ) IPA ( key ) : /baː.ˈnuː/ , /baː.ˈnoː/ 
--
307: Etymology
=== ef2bd461cdea148c
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
154: Etymology
155- [ edit ] 
156-
157- Inherited from Middle Persian [Book Pahlavi needed] ( wh'nk' /⁠wihānag⁠/ ) , from Proto-Iranian [Term?] . Northern Luri: بڡنٮه ( bẉnə ) .
158-
159- Pronunciation
160- [ edit ]
```


## [2026-10-17T00:02:13.882Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n 'Etymology' -A8 17558bff3cd95133.txt | sed -n 1,80p | grep -v '^\\-*$' | head -60; python3 -c \"\nimport json\nfor l in open('index.jsonl'):\n  d=json.loads(l)\n  if 'page 551' in (d.get('note') or ''): print(d['url'],d['status'],d['bytes'],d['file'])\""
}
```


### [2026-10-17T00:02:14.563Z] TOOL RESULT

```
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.4 
96: Etymology 1 
97-
98- 3.2.1 
99- Alternative forms 
100-
101- 3.2.2 
102- Noun 
103-
104- 3.2.2.1 
108: Etymology 2 
109-
110- 3.3.1 
111- Noun 
112-
113- 3.4 
114- References 
115-
116- 3.5 
200: Etymology
201- [ edit ] 
202-
203- Possibly from Sanskrit वाम॑ ( vā́ma , “ left side ” ) .
204-
205- Pronunciation
206- [ edit ] 
207-
208- Tone class: H
311: Etymology 1
312- [ edit ] 
313-
314: Etymology tree
315-
316- Proto-Indo-European *wes- der. 
317- Middle Persian bʾn 
318- Persian بام 
319-
320- From Middle Persian [script needed] ( bʾn /⁠bān⁠/ , “ roof, rooftop ” ) , ultimately from Proto-Indo-European *wes- ( “ to clothe, wear, put on ” ) . Compare Avestan 𐬬𐬀𐬢𐬵𐬀𐬥𐬀 ( vaŋhana ) , 𐬬𐬀𐬢𐬵𐬁𐬥𐬀 ( vaŋhāna , “ cover ” ) .
321-
322- Alternative forms
349: Etymology 2
350- [ edit ] 
351-
352: Etymology tree
353-
354- Proto-Indo-European *bʰeh₂- 
355-
356- Proto-Indo-European *-mos 
357-
358- Proto-Indo-Iranian *bʰáHmas 
359- Middle Persian bʾm ( /⁠bām⁠/ ) 
360- Persian بام 
https://en.wiktionary.org/wiki/پوست 200 5721 data/verification/sources/web/7e2e47bc80da4d0a.txt
https://en.wiktionary.org/wiki/بام 200 7994 data/verification/sources/web/17558bff3cd95133.txt
https://en.wiktionary.org/wiki/بانو 200 7473 data/verification/sources/web/9cb41b658096e675.txt
https://en.wiktionary.org/wiki/بهانه 200 4467 data/verification/sources/web/ef2bd461cdea148c.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wes- 200 10802 data/verification/sources/web/4c8f69f23d3ef8f2.txt
https://en.wiktionary.org/wiki/wear 200 33309 data/verification/sources/web/2f3a05afbbf2b9ca.txt
https://en.wiktionary.org/wiki/vestis 200 6451 data/verification/sources/web/02c86fec33330f88.txt
https://www.etymonline.com/word/vest -1 39 data/verification/sources/web/92af3b7363d62c94.txt
https://www.etymonline.com/word/wear -1 39 data/verification/sources/web/b7c7484bf808e010.txt
https://www.etymonline.com/word/invest -1 39 data/verification/sources/web/3471461344210ed5.txt
https://www.etymonline.com/word/divest -1 39 data/verification/sources/web/20936d7ff7ffc2e4.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wazjaną 200 4611 data/verification/sources/web/ec8303f763882b05.txt
https://en.wiktionary.org/wiki/واستریوش -1 39 data/verification/sources/web/6572d0c89158b4a0.txt
https://en.wiktionary.org/wiki/واستر -1 39 data/verification/sources/web/209b8b3af582ad4a.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram -1 39 data/verification/sources/web/c2659c7064dbbd5f.txt
https://en.wiktionary.org/wiki/vasman -1 39 data/verification/sources/web/57377905546001bd.txt
https://en.wiktionary.org/wiki/वस्मन् 200 6290 data/verification/sources/web/e063104404fcb1d4.txt
https://en.wiktionary.org/wiki/वसन 200 12038 data/verification/sources/web/b750b85d2923244a.txt
```


## [2026-10-17T00:02:23.677Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/vest' 'https://en.wiktionary.org/wiki/invest' 'https://en.wiktionary.org/wiki/divest' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wes-' 'https://en.wiktionary.org/wiki/𐬬𐬀𐬯𐬙𐬭𐬀' 'https://en.wiktionary.org/wiki/𐬬𐬁𐬯𐬙𐬭𐬀' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wástram' 'https://en.wiktionary.org/wiki/𐬀𐬊𐬚𐬭𐬀' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃ewh₁-' 'https://en.wiktionary.org/wiki/پوستین' 'https://www.etymonline.com/word/vest' ; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note 'page 551, roots Wes 3 / Wes 4' 2>&1 | tail -1; done; cd data/verification/sources/web; grep -n -i 'iran\\|avest\\|persian\\|Old Persian' 4c8f69f23d3ef8f2.txt | head -30"
}
```


### [2026-10-17T00:02:28.563Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/vest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/dc200f7672fb6daf.txt
== https://en.wiktionary.org/wiki/invest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a271bea42073947d.txt
== https://en.wiktionary.org/wiki/divest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f6271edaad9e779c.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₂wes-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6076af4873cacb58.txt
== https://en.wiktionary.org/wiki/𐬬𐬀𐬯𐬙𐬭𐬀
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7c12f97fe457b8b1.txt
== https://en.wiktionary.org/wiki/𐬬𐬁𐬯𐬙𐬭𐬀
/home/sfmqrb/git/rishe-private/data/verification/sources/web/eb2f07d963592c7a.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wáHstram
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c2659c7064dbbd5f.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wástram
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f45a12f89d3bcc3d.txt
== https://en.wiktionary.org/wiki/𐬀𐬊𐬚𐬭𐬀
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0afa8bb3e480a8b4.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₃ewh₁-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f2422758fbb1a0ca.txt
== https://en.wiktionary.org/wiki/پوستین
/home/sfmqrb/git/rishe-private/data/verification/sources/web/da60e62b8bba85a6.txt
== https://www.etymonline.com/word/vest
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92af3b7363d62c94.txt
200: Proto-Indo-Iranian: *wásanam 
204: Proto-Iranian: *wáhanam 
205: Younger Avestan: 𐬬𐬀𐬢𐬵𐬀𐬥𐬀   n ( vaŋhana ) 
213: Proto-Indo-Iranian: *wásma 
226: Proto-Indo-Iranian: *wástram ( see there for further descendants )
249: Proto-Indo-Iranian: *was- 
253: Proto-Iranian: *wah- ( see there for further descendants )
299: Avestan: 𐬬𐬁𐬯𐬙𐬀𐬭 ( vāstar , “ herdsman ” ) [ 11 ] 
301: Avestan: 𐬬𐬁𐬯𐬙𐬭𐬀 ( vāstra , “ pasture ” ) 
334: Proto-Indo-Iranian: *wasás 
335: Proto-Iranian: *waháh 
338: Middle Persian: [Book Pahlavi needed] ( whʾk /⁠wahāg⁠/ ) 
339: Persian: بها ( bahâ ) 
347: ⇒ Proto-Iranian: *wahá-čāra- ( “ market ” ) ( with *kʷel- ( “ to walk ” ) ) 
358: Middle Persian: [Book Pahlavi needed] ( wʾčʾl /⁠wāzār⁠/ ) 
359: Persian: بازار ( bâzâr ) ( see there for further descendants )
386: ^ Beekes, Robert S. P. ( 1988 ), A Grammar of Gatha-Avestan ‎ [2] , volume 1, Leiden: Brill, →ISBN , page 80 
410: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-10-17T00:02:33.472Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 180,310p 4c8f69f23d3ef8f2.txt | grep -v '^\\s*$' | head -90; for f in 7c12f97fe457b8b1 eb2f07d963592c7a f45a12f89d3bcc3d 0afa8bb3e480a8b4 da60e62b8bba85a6 6076af4873cacb58 f2422758fbb1a0ca dc200f7672fb6daf a271bea42073947d f6271edaad9e779c 92af3b7363d62c94; do echo \"== $f $(head -c 0 $f.txt; wc -c < $f.txt)\"; done"
}
```


### [2026-10-17T00:02:33.800Z] TOOL RESULT

```
 *wos-éye-ti ( “ to dress ” , causative ) [ 4 ] 
 ? *wḗs-t ~ *wés-n̥t ( s-aorist ) [ 4 ] 
 Armenian:
 Old Armenian: զգեցաւ ( zgecʻaw , aorist of զգենում ( zgenum ) ) 
 Proto-Hellenic: 
 Ancient Greek: ἕσσα ( héssa , aorist of ἕννῡμῐ ( hénnūmĭ ) ) 
 Tocharian:
 Tocharian A: wässāte ( 3rd person singular preterite of wäs- ) 
 Tocharian B: wsānt ( 3rd person plural preterite of wäs- ) 
 *wés-mn̥o-s ( “ garment? ” ) ( or *wés-n̥no-s ) ? 
 Proto-Hellenic: *wéhanos 
 Ancient Greek: ἑᾰνός ( heănós , “ woman's robe ” ) , εἱᾰνός ( heiănós ) ( verse-initially ) , ἑᾱνός ( heānós ) ( later ) 
 Mycenaean Greek: 𐀸𐁀𐀜𐀂 ( we-a2-no-i /⁠wehanoiʰi⁠/ , dat.pl. ) 
 Proto-Indo-Iranian: *wásanam 
 Proto-Indo-Aryan: *wásanam 
 Sanskrit: वस॑न   n ( vásana ) 
 Proto-Iranian: *wáhanam 
 Younger Avestan: 𐬬𐬀𐬢𐬵𐬀𐬥𐬀   n ( vaŋhana ) 
 *wés-mn̥ ( “ garment ” ) 
 Proto-Hellenic: *wéhmə 
 Ancient Greek: εἷμα ( heîma ) , εἵματα ( heímata , “ clothes ” ) 
 Aeolic Greek: ἔμμα ( émma ) 
 Cretan Greek: ϝῆμα ( wêma ) 
 Proto-Indo-Iranian: *wásma 
 Proto-Indo-Aryan: *wásma 
 Sanskrit: वस्म॑न् ( vásman ) 
 *wés-ti-s ~ *us-téy-s ( “ act of dressing; clothing ” ) ( see there for further descendants )
 *wés-tro-m 
 Germanic:
 Middle High German: wester ( “ christening dress ” ) 
 Proto-Hellenic: *wéstrā 
 Doric Greek: ϝέστρᾱ ( wéstrā ) 
 Proto-Indo-Iranian: *wástram ( see there for further descendants )
 *wés-tu-s 
 Armenian:
 Old Armenian: զգեստ ( zgest , “ dress ” ) 
 Unsorted formations 
 Armenian:
 Old Armenian: առա-գաստ ( aṙa-gast , “ curtain ” ) (< *wés-t-eh₂- ) ( possibly ) 
 Hellenic:
 Ancient Greek: ἐσθής ( esthḗs , “ clothes ” ) 
 Tocharian:
 Tocharian B: wastsi ( “ clothers ” ) ( infinitive of wäs- ) 
 Descendants
 [ edit ] 
 Anatolian:
 Hittite: [script needed] ( waš- ) 
 Proto-Indo-Iranian: *was- 
 Proto-Indo-Aryan: *was- 
 Sanskrit: वस् ( vas ) 
 Proto-Iranian: *wah- ( see there for further descendants )
 Proto-Tocharian: *wäs- 
 Tocharian A: wäs- 
 Tocharian B: wäs- 
 Etymology 2
 [ edit ] 
 Root
 [ edit ] 
 *wes- ( imperfective ) [ 7 ] [ 8 ] [ 9 ] 
 to graze , consume , eat 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *wes- (graze) (5 c, 0 e) 
 *wḗs-ti ~ *wés-n̥ti ( Narten present ) 
 Proto-Anatolian: 
 > ? Hittite: 𒌑𒂊𒅆𒅀𒀜𒋫𒊑 ( ú-e-ši-ya-at-ta-ri , “ to pasture, graze ” ) [ 10 ] 
 > ? Proto-Germanic: *wesaną ( “ to consume, feast ” ) ( or from a thematic root presnet ) ( see there for further descendants )
 *wes-teh₂- 
 > ? Proto-Celtic: *westā ( “ food, feast ” ) ( see there for further descendants )
 *wes-ti- 
 Proto-Germanic: *wistiz ( “ provisions, food ” ) ( see there for further descendants )
 *wes-ri- 
 Tocharian A: wäsri ( “ pasture ” ) 
 *wēs ~ *wes-os ( “ pasture ” ) ?
 ⇒ Proto-Italic: *wēskōr ( “ to nourish oneself ” ) ( with a long vowel perhaps via the analogical influence of a root noun or Narten verb ) ( see there for further descendants )
 Unsorted formations 
 Hittite: wēsi- ( “ meadow ” ) 
 Hittite: wastara- ( “ herdsman ” ) 
 Avestan: 𐬬𐬁𐬯𐬙𐬀𐬭 ( vāstar , “ herdsman ” ) [ 11 ] 
 Avestan: 𐬬𐬁𐬯𐬙𐬭𐬀 ( vāstra , “ pasture ” ) 
 Proto-Germanic: *wisundz ( “ bison ” ) 
 Etymology 3
 [ edit ] 
 Root
 [ edit ] 
== 7c12f97fe457b8b1 2747
== eb2f07d963592c7a 150
== f45a12f89d3bcc3d 163
== 0afa8bb3e480a8b4 4975
== da60e62b8bba85a6 4206
== 6076af4873cacb58 6807
== f2422758fbb1a0ca 172
== dc200f7672fb6daf 32403
== a271bea42073947d 18542
== f6271edaad9e779c 7249
== 92af3b7363d62c94 131
```


## [2026-10-17T00:02:41.488Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 7c12f97fe457b8b1 0afa8bb3e480a8b4 da60e62b8bba85a6; do echo \"=== $f\"; grep -n -A4 '^ *Etymology$\\|^Etymology' $f.txt | grep -v '^\\S*-\\s*$\\|edit' | head -12; done; grep -n -i 'feast\\|graze\\|pasture\\|Avestan\\|Persian' 6076af4873cacb58.txt | head; grep -n -i 'From Middle English\\|Latin vest\\|investire\\|devest\\|Italian veste' dc200f7672fb6daf.txt a271bea42073947d.txt f6271edaad9e779c.txt | head -8"
}
```


### [2026-10-17T00:02:41.989Z] TOOL RESULT

```
=== 7c12f97fe457b8b1
134: Etymology
137- From Proto-Indo-Iranian *wástram , from Proto-Indo-European *wést-ro-m . Cognate with Sanskrit वस्त्र ( vástra ) .
=== 0afa8bb3e480a8b4
136: Etymology
139- From Proto-Indo-European *h₃ew- .
=== da60e62b8bba85a6
139: Etymology
142- From پوست ( pust , “ skin ” ) +‎ ـین ( -in ) , from Middle Persian 𐭯𐭥𐭮𐭲𐭩𐭭⁠ ( pwstyn' /⁠pōstēn⁠/ , “ made of leather ” ) .
f6271edaad9e779c.txt:179: Alteration of devest , from Middle French devester ( “ strip of possessions ” ) , from Old French desvestir , from des- ( “ dis- ” ) + vestir ( “ to clothe ” ) .
f6271edaad9e779c.txt:282: Italian: disinvestire 
a271bea42073947d.txt:214: Borrowed from Middle French investir or Medieval Latin investire , from Latin investio ( “ to clothe, cover ” ) , from in- ( “ in, on ” ) + vestio ( “ to clothe, dress ” ) , from vestis ( “ clothing ” ) ; see vest . The sense “to spend money etc.” probably via Italian investire , of the same root. [ 1 ] 
a271bea42073947d.txt:388: Italian: investire   (it) 
a271bea42073947d.txt:457: Italian: investire   (it) 
dc200f7672fb6daf.txt:467: Derived from French veste ( “ a vest, jacket ” ) , from Latin vestis ( “ a garment, gown, robe, vestment, clothing, vesture ” ) , from Proto-Indo-European *wéstis , from *wes- ( “ to be dressed ” ) ( English wear ). Cognate with Sanskrit वस्त्र ( vastra ) and Spanish vestir .
dc200f7672fb6daf.txt:993: Borrowed from French veste , from Italian veste , from Latin vestis .
dc200f7672fb6daf.txt:1354: Derived from Latin vestis , via French [Term?] and Italian [Term?] .
```


## [2026-10-17T00:02:49.562Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/551.jpg 2>/dev/null; pdftoppm -f 551 -l 551 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg551 && echo ok"
}
```


### [2026-10-17T00:02:50.757Z] TOOL RESULT

```
site/pages/551.jpg
ok
```


## [2026-10-17T00:02:55.974Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg551.png"
}
```


### [2026-10-17T00:02:56.445Z] TOOL RESULT

```

```


## [2026-10-17T00:02:56.442Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-17T00:03:04.107Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"'kleiden\\|'sich  kleiden\\|'Kleid'\\|  'Kleid\\|'anziehen\\|Gewand'\" BRT.txt | cut -c1-400 | head -20"
}
```


### [2026-10-17T00:03:04.676Z] TOOL RESULT

```
4308:*a-6däiay-,  zu  bdä-,  Weiterbildupg  der  in ahd.  vaisen  'sich  kleiden',  an./äi'  'Kleid'  ent- haltenen Basis;  Bthl.  IF.  9.  256.  —  Pü.: (ehit  —  >)  iSt.  und  zAusdr,  s,  'ananayäslay-
15100:PPfP.;  vgl. /romaj/ay-.  —  Vgl.  m.  muricHi ■er  lieht  aus',  pratimukia-  Adj.  *angeiogen'3>i mp.  patmöxtan  'anziehen',  np.  möza  'Schuh'. —  >)  Sm-  nach  i  neben  m-  hinter  a  {/ra- muxli)  nach  dem  Muster  von  Woltern  mit altem  sm-,  %  82.  4.  —  ')  So  Yt.  5  alle  guten Hds.;  NA.^ft'/Hi".  päiü  als  Praev.  an  Stelle von  paili  erklärt  sich  wie  päiri,  sd. 
19218:•  j.  nivizan-  Adj.  'anziehend,  reizend,  1 '^'''*  Yt/5. 45,  Geringe  Stelle. gefällig'  ■>:  Äa  hi  maiUm  nyazata  ya^aca  .  ,  j.  nisma-  m.  '(Hineingehen  in  den  Erd- hukfr)ptaßtänayai!aca  anh)rfz3nal^'Q:)  \^o^^^  sva.)  Tiefe':  paoirjm  upa  vmy>m "äe  schnürt  sich  ihre  Taille,  damit  '-^tz  ■  ni>:w>rnöil  .  .  dva  »rssu  -mähe''»  "das Brüste  schöngestaltet  und
22196:•  j.  vaoray  m.  'Rahm  (auf  der  Milch)'. KompE.  —  Statt  ♦mii'T-"  geschr.,  S  36S.  18.  — Zum  V.'var-;  red.  Bildung;  eig.  'Hülle,  Be- deckung''). —  ai.  vatn'dy-  m. 'Hülle,  Gewand' i). —  >)  Bthl.  IF,  9.  260.
22481:•  j.  vaehana-  n.  'Kleidung,  Gewand': kammtK  (sd.)  vaste  'n>m  \.4.4g; —  aom asmatum  .  .  yim  mazda  vaste  (sd.)  'tum st3hrpaisat9h?m  Yl  13.  y,  —  'lumca  Vd.  ig.
23152:•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhu
23159:Ableit  aus  'vattro;  eig.  Adj.  'Kleider  ent- haltend'. Unsicher.  —  Pü.:  vasir  dän.  — <)  AuffülL  Foim;  s.  zu  sfii-  No.
23299:"  }-t  g-  ^vah-  V,  'sich  kleiden  in  — '■ Praes.  i  vaA-,  2  vanha-,  —  Absol. vaKkätum.
23300:Mit  Akk.  'sich  kleiden  in  — ,  anziehen, sich  umtun;  anhaben';  Akt.  und  Med.: uai  vaslrä  vanAalu  V,_y.  19'';  ^^<Kcri7««( vastra  va»Aaia  (^S.)  andvl  YL5. 129"; —  spafta  vasträ  zanhaiti  tpaita  (sd.)  Yt 10.  126";  —  yS  vanhaiti  .  .  al^Js/a \frazus5  sanhasSa  .  .  N.92'*;p5;  —  *yffi .vanhinti  hntts^a  paiti-varahasca  ü.gi; I  —  kamn>m  (sd.)  vaste  vanhafum
```


## [2026-10-17T00:03:08.510Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=22400 && NR<=23320 && /^[0-9]{4}$/ {print NR\": \"$0}' BRT.txt; grep -n 'vastra-\\|ve.str\\|wäStar\\|västar\\|västra\\|vastrya\\|v.stry' BRT.txt | cut -c1-300 | head -20"
}
```


### [2026-10-17T00:03:08.969Z] TOOL RESULT

```
22417: 1345
22447: 1347
22450: 1348
22506: 1349
22509: 1350
22798: 1365
22883: 1369
22886: 1370
23018: 1377
23069: 1380
23114: 1384
23149: 1386
23169: 1387
23172: 1388
23213: 1390
23253: 1392
23273: 1393
23276: 1394
23308: 1396
183:Für  das  a^estiscbe  Material  liegen  die  Fundstellen  leider  gar  sehr  verstreut. Die  Hoffiiungen,  die  sich  an  das  von  der  Wiener  Akademie  unterstützte  Unter- nehroeo    knüpften,    haben   sich   als   tri^erische    erwiesen:    Geldners   'Awesta'    ist
3356:•  g.  a-drujyant-  Adj.  'trügeriscli,  arglistig, böslich  handelnd  (gegen  — )':  hanara  .  . vastryehyä  asnanhö  pas^ul  virlalcJ  "yants "ohne  Gewalttat  an  des  Bauern  Tieren und  Leuten,  der  (ihm)  doch  kein  Arg tut"  y.  j;.  15.
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  
3399:—  'rum  (GS.)  hö  rätanam  . .  isänAaaa (sd.)  Yl  ig.  53;  53';  F.  7^';  — paiH.ä3n?m ainim  baraiti  ..  diwiat  haca  'va  sauAaite V, /<y,  i;  2—4;  —  hial  n3  'va  a^aururum /ia:a  *gai>äöU  *parayat  "wie  weit  soll  ein , Priester  auf  Priesterdienst  aus  dem  Haus gehen?"  N
3400:—  tara'^ustrahe  . .  paoiryäi  'rune  .  .  ra- >ais'tai  .  .  västryäi  ßuyänte  YLij.  88; iij.%  {'runalca),  V.J.  57,  58,  y.  44-  45. J4,8';  —  västrye/ie  JSuyantö  .  .  ra>aSstä ..  •rutUf  (GS.)  raiüm  Y.i^.3  f.;  Vytj,/ö", Az.$; — 'runqsca*^  ra>aistisca  vastryqsca ..ßuyaniö
3451:8.  2)  eines  Satzteils,  voraus  geht   ^ä: //',röi  .  .  pai'iyatla  västryaEibyS  (sd.) sTattoavi  Y.5J.4.
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
4907:•  j.  aya^äna-  n.  Name  eines  landwirt- schaftlichen, anscheinend  beim  Pflügen notwendigen  Geräts:  yaiSatn  zayanqm vastryehe  ßiiyantS  .  .  'iJna  (NP.)  paiti.- dar>zäna  (sd.)  V.  i4- 10.
5184:•  j.  a-västra-  Adj.  'was  kein  Futter  hat, des  Futters  Wachstum  verhindert':  /laa'ö .  .  yat  'r)m  Y.ij.$i;  —  haicat)hs  'rahe V.  7.26;  Yt.  7^.130.
5186:•  g.  a-västrya-  Adj.  'der  kein  Bauer  ist': nöii  °yS . .  humsritöis  {sA^  baxitä  Y.J7.10.
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  mana
5971:mit  ä  dnwS,  4  a;  yezi  näil  paitiiaraiti *%rl  vs  äsäiti  ayar»jiräjö  (sd.)  vä  vastryä£ N.  69;  ^2,  43,  <V?,  log'''.
5973:mWpaiti  und  a  dnwS.  4a:  yezi  nsi^  *'irT 7>il  paiti  asaili  ayar).dr3jö  (sd.)  vä  västryät
6084:(als  Subj.)3>  ya  'sät  gSUs  taiä  (sd.)  mraet Y.4/i.g;'~  mq'ir^m  yim  haurvatatS  'iahyä amsntätaicä  (sd.)  Y.gi.d;  —  kä  "iswöi 'iä  (Vok.)  äka  (sd.)  arpdrfng  isyä  Y.48. 8;  —  daidl  'iä  (Volc)  tqm  ailm  vanhsui ayaptä  manaifhö  Y.  28. 7;  6;  —  yS  vi mazdii  ahurä  pair
6206:i)  'dem  heiligen  Recht  gemäss  handeln': asayata  (aP.)  vastryäüa  (sd.)  pu'^ra  fra- /ae/tra  \yi.  !!''>.        a)  mit  einer  Massbe- stimmung 'Werke  des  v4sa  (heiligen  Rechts) verrichten':  tauu.mats  (sd.)  asayäiti  yS .  . __  _  P.18.         a)  'sich  das  Recht,  den  rec
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a
6505:•  j.  as.dSnav-  Adj.  'mit  starken,  grossen  •  P-  aSna-  m.  'Marschiren',  mit  astty  'er (Samen-)Körnem':  us  apam  aoavS  .  .  befindet  sich  auf  dem  Marsch  nach  — ' jasänti  -nunqmca  yavanq'm  kasuJätm-  («^V  »"'*  Akk.):  *adaiiy  adam  ^naiy^^ natnca  västra'nam  "die  wäs
6509:.  ].  asa-*wo.zgatama-  Ad,,  'der  aUer-      ^Xr/:  d^n  ain^y-Ai.  ILm  =  j.  a>n^:  aL drängendste,  allereifrigste':  °mq  gavästrya-       äsmana).  —  jj  Vgl.  %rah-  No.  3. varlt>niq  narqm  asäunqm  Y.  13.  2.  '         j.  ainäat^a,  ainJ:  s.  unter  aiaa-.
6657:—  cDimS  . .  huxsa'iira  (sd.)  dagvä  aahari  der  kongruenten  Form  des  Adjektivs  er- Y.  44,20;  —  negirt:  västry3t  vä  . .  yl  scheint  das  Neutr.  im  Sing.;  A)llimAp.: vä  nSii  aahat  väslryl  Y.3i.<).  PPA.:  kär<^  ..hyt^  up3  mäm  äha'' haur  kamnam dr.'gvä  ..  duiazöbä  
6692:beschäftigen,  dem  Studium  von  -  (bes. der  heiligen  Texte)  obliegen":  cvat  n3 ''al'^ra.paitim  (sd.)  upJisal?  ylr).drajS; "i^riiarpmagm  xralüm  asavamm  aiwylnAät \.  i/j*';  —  y7i  däityJyaona  *car9fäa *gavästrya'a  varssnh  *V3r?zy3ntd xratüm'a aiovamm  aiioi^antö  ".  .  landwi
```


## [2026-10-17T00:03:12.009Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"j\\.  västra-\\|j\\.  västar-\\|västrya-  \\|j\\.  västrya\\|vä8tar\\|västryö\" BRT.txt | cut -c1-400 | head; "
}
```


### [2026-10-17T00:03:12.396Z] TOOL RESULT

```
5186:•  g.  a-västrya-  Adj.  'der  kein  Bauer  ist': nöii  °yS . .  humsritöis  {sA^  baxitä  Y.J7.10.
6509:.  ].  asa-*wo.zgatama-  Ad,,  'der  aUer-      ^Xr/:  d^n  ain^y-Ai.  ILm  =  j.  a>n^:  aL drängendste,  allereifrigste':  °mq  gavästrya-       äsmana).  —  jj  Vgl.  %rah-  No.  3. varlt>niq  narqm  asäunqm  Y.  13.  2.  '         j.  ainäat^a,  ainJ:  s.  unter  aiaa-.
7753:•  g.  araSva-  Adj.  i)  'recht  handelnd,  ge- recht': västryö  syaoianäis  °vs  hqs  huxratus namaakä  (sd.)  Y.5i'.  s;  —  ks  7'ä  vaiAsus manav/iö  aästä  magäi  'vd  "oder  wer  wird, rechthandelnd,  sich  auf  den  Bund  des  VM. bedacht  zeigen?"  Y,  57. 1 1 ;  —  yS  savaitl ädriiig  (sd.)  'ViwAöY.S^.^.  2)  "wahr, sicher':  ''i'j(APn.)  x/a^nl . .  asTstfs'{sd.)  Y. 44.g;~däidi*
10177:•  j.  gavästrya-  Adj.  'was  sich  auf  die Weide  des  Rinds  bezieht',  sva.  'landwirt- schaftlich, bäuerlich':  a(tät..°yit<a  vartiriä ^vinsjnti  "..  und  verrichten  landwirtschaft- liche Arbeiten"  N.  60;  —  *°yaca  '>  vanmii N.  53;  —  °ya  *var3s>iä  N.  iV,.
18391:'Vieh  auffüttern,  au&iehen,  Vieh  züchten"', nur  PPA.  ßuyant-  'ViehzUchter,  Freund der  Viehzucht*:  ySi  msimim  vandm  (sd.) . .  :^äü  hiiubls  /luyasü  aßuyanti  ". .  die Feinde  der  Viehzucht  unter  deren  Freun- den" 'Y.4f).ar''>;  —  nsil  »nzajySi  frajyaitis (sd.)  nsit  fsuyenlt  dngvasB  pairl  Y. 2p.  5.  a)  mit  västrya-  (sd.):  ai zl'kwa fsuyaniaila  vaslryäicä  %w
25082:•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y
```


## [2026-10-17T00:03:19.964Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for p in '^wāstar' '^wastar' '^wāstaryō' '^wihān' '^wihan' '^pōst' '^post' '^bān' '^ban ' '^bānūg' '^bām'; do echo \"## $p\"; grep -n -i \"$p\" PHD.txt | head -5; done; echo; for p in 'wāstar' 'vāstar' 'wāstr' 'vihān\\|wihān' 'pōst' 'bānūk\\|bānūg' 'bām ' 'vahān'; do echo \"## NYB $p\"; grep -n -i \"$p\" NYB_vol2_glossary.txt | head -5; done"
}
```


### [2026-10-17T00:03:20.520Z] TOOL RESULT

```
## ^wāstar
623:wāstar [w’st/] pasture, fodder.
625:wāstaryðš [w'stlywš = Av. wástryo.ffuyant-] husbandman. —-їһ: husbandry.
## ^wastar
621:wastar [wstl = Av. wastra-] clothing, garment.
624:wastarag [wstlg] = wastar.
5153:wastarag, wistarag nastaran wistardan Widadafs
## ^wāstaryō
## ^wihān
## ^wihan
## ^pōst
## ^post
3187:post-(horse) bayaspānīg.
3188:posterior nišēm.
## ^bān
## ^ban 
## ^bānūg
## ^bām
251:bāmbišn [MLK TTA < A тіке; РпЬй! | M Pnbyfu] queen. < dmana-
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.

## NYB wāstar
## NYB vāstar
## NYB wāstr
## NYB vihān\|wihān
## NYB pōst
## NYB bānūk\|bānūg
## NYB bām 
3865:uš-bām [?wSb’m] dawn, daybreak 72°. 10133. — Av. (415) us(ah)- ‘dawn’ + *bama- ‘light’, whence (954 sq.) bāmya- ‘luminous’ (v. bämik); MPrs ?’wsyb’m (A-H I), Paz. hösbäm.
## NYB vahān
```


## [2026-10-17T00:03:23.430Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wih[aā]n\\|whʾnk\\|why’n\\|pōst \\|pōst\\[\\|pöst\\|bān \\[\\|^bān' PHD.txt | head; grep -n -i 'vih[aā]n\\|v[ie]h[aā]nak\\|pōst\\|pöst\\|v[aā]st[ae]r\\|vāstry\\|bān\\b\\|bānūk' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-10-17T00:03:23.750Z] TOOL RESULT

```
212:anērān [?7°3?n'] non-Eran, the world beyond Eran. an-érang [?n’ylng] blameless. an-espās [’nsp’s] ungrateful. ~ih: ingratitude. 2 AY angubén [DW BS Y.A < A dbf ; ?ngpyn! | N angubin] honey. By? Wat), angür [AN BE < A ‘nb’; ?ngwl | N ~] grape. А AC k angust Pngwst! | (N angust)] finger, toe; unit of length (š in.). Va м ~arig [-lyk'] finger ring. „bān [-p’n'] finger-guard, -stall. anidan, ānay- [HY TYWN-tn! < А hyty, ^? th; ?nytn!] bring, lead. anig Payk! | (N pēšānī)] front, forehead. anī-z [AH RN(y)e, v. any | N niz] other also. anjir Pncyl | N ~] fig. anódag [nwtk! | M ?nwdg] strange, alien. ~ig [-yk'] foreign. ünóh, *ànóy [TME < A tmh | M ?nwh, ?wy] there. an-dst Pwwst'] infirm, unreliable. anos [nws] lit. immortal, i.e. the next life; elixir, antidote. — xwardan : risk death, fight to the death. anošag Pxwšk! | M ?nwsg, N ~a] immortal. «ii: immortality. ~-ruwan [-lwb’n'] the late, deceased. an-Ošmār [?7wsm’l] countless, innumerable. anó$-xwar [поў] mortal. *апбу, v. ānēh. anSahrig [nstr'yk'] slave. an-umméd P7wmyt! | J *nwmyd, N nauméd] hopeless, despairing. an-uspurrig [^r wspwlyk') imperfect. any [AH RN < A *hrn; (corruptly, 2К?у = *dn-i) | M ?n()] other. a-pattüg [ptwk!] impatient. a-paymān (?ptm?n!] immoderate. ~ih : immoderation. *apédag [ругА! | P?pyd(g)] lost, stray. ~dar [-d?/] custodian of stray animals. a-petitig žtytyk!] unrepentant, unconfessed. 7h : unrepentance. a-petyürag Pf(y)tyd'lk'] without misfortune, unassailed. a-pohisn Pwhšn'] incorruptible. appar [?5/ | М ’pr] robbery, theft. appar ['P?/] taken away, removed. ~ih : removal, loss, deprivation. apparag [25/6] robber. appurdan, appar- [YHNCLWN-tn' < A yhnslwn, V asi: >pl- | M эрит, *p(w)r-] steal. ~išn: stealing, theft. a-pursišnīg Ppwrsinyk'] irresponsible.
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
388:h- [HWE- < A d hwh; h- | M h-] be (defective verb). !had [HWEt! ! = Av. Gat] now, then; that is (= à). *hàd [/?t!] a section of the Yasna. hàdamaàns?r [/Ptkmnsl = Av. hača.mādra-| those scriptures dealing with ritual matters. ~ig [-yk'] concerned with the above. - hādēxt [W#twht! = Av. hadaoxta-] certain scriptural texts; a particular sacrifice. haft [лб | M Apt, N ~] seven. ~ad [7o | M hpt'd, N ~] seventy. ~ag [-À! | N hafta] week. —šn [-”x!] the seven planets. haftàr [h5tl | (N kaftār !)] hyena. haftdah [%tdh | N ~, hifdah] seventeen. Haftóring [kftw(k)lng = Av. haptóiringa-] astr. the Great Bear. hagriz [hkic | M hgryc, N hargiz] ever; (with a negative) never. halag [Alz'] foolish, imprudent. ~th: folly, madness. halām [Pm | N ~] potted meat. halilag [hlylk' | N ~a] myrobalan. ham [hm | = M, N ~] also; same; v. 6. —ih: association, union, harmony. hamābēr [hm’fyl | M 72m°byr] storehouse. hamāģ [hm’k' | M Pwg, N hama] all. ~-dén [-dyn'] a complete religious ceremony. hamagih [hmkyh | N —i] totality, universality. hamahl [4(*)4[] = hamāl. hamāl [ml | N ~] equal, peer; comrade, hambadig [hmbtyk'] opponent, adversary. hambah-, v. *hambastan. hambāh-, ~išn, v. hambástan. hambān [hmb’n' | N anbán(a)] skin bag. hamband [hmbnd] connected. ~ih: connection. hamband-, —išn, v. 'hambastan.
452:mānbān [m?np?n!] watch-dog.
491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
553:puštaģ [pwstk'] load (carried on the back). puštībān [pwštykp”n! | N ~] supporter, bodyguard. ~ЛЬ : support, protection.
570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
1645:giv [TWR”; g’w'] bull, cow, with the indef. art. —-č [TWR’-+1 458]: passim; ~ 4 ēvdāt (g. v.) 10418; öisän ~ these cows, dir. obj. 42%; pl. cas. obl. —-ān [TWR?--n'] gen. 482%. 4911, 861, 899. 905.6; gen. part.: dian ~-dn 2 425; —-din u gēspandān ... ēvakē vak 80?-3; dir. obj. 4825-26; instead of cas. rect. 495 (gl.); — ~ [TWR>] póstihà 107°, ~ [g’w'] pöstiyänihä ox-hides 110%, v. these ws. — Last element of proper names: Bér-~ Gafr-, Kartar-, Névak-, Purr-, Ramak-,
2559:*mih(a)rg [mytlg; Vd. 21? mtlg] cloud, the sphere of the clouds 21”. — Existing in the sphere called in Av. mäna-, v.s. v. mänenak. -g is to be explained in the same way as in andarg, vastarg, vistarg, vazurg: the suff. -ka- was added directly to the stem (cf arišk, husk) and -k- voiced by contact with the preceding -r-; -tl- is no doubt the archaistic spelling -0r- for Milr -hr.; original form consequently *miür-ka > mihrg and then perhaps with secondary vowel miharg, cf *vazrka- > vazurg ete. Possibly derived from M36ra-, cf Yt. 109! where he is praised as the giver of rain; not identical with MTL? (for Prth MTR’) varan, FrP 1.
3166:pöstiyän [pwsty’n'] leather, pl. ~-iha [-yh’] 1102, — Derived from post: NP pöstiyän ‘a kind of leather’.
3664:$upän [šp'n'] shepherd 1”; pl. cas. obl. ~-dn 10, — Av. (1029) fšu- ‘sheep’ = pasu-, v.S. v. püh, + pāna-, v. pānak; MPrth swb’n; NP šubān, sabän.
3681:*Tab [t?b] the name or the title of the king of Kabul 17°. — Cf Tābān, the capital of the country of Kabul, Yàqüt 3,454, v. Erangahr 299. Another possible reading would be Tai [t'd], Chinese t'a? ‘great’
4018:vastarg [wstlg] clothes 41?-4-? [472° read vistarg]. — Av. (1385) vastra- ‘clothing’ ; inser. SM 1. 50 wstlg; Paz. vastarg, vastrg ; Mand. lw. bastirga.
4211:vistarg [wstlg] bed coverlet 47%. — < OIr *vi-star-ka-, v. the next w. and cf vastarg; Ps. wstly, NP bistar ‘bed, mat- tress’; Talm. lw. bystrq?, Telegdi 235.
4326:x"arg [hwlg] consuming, of the fire: —-ē ātaxš 92°, with the same ending -é as in menöye, v. meno. — < *xvarka-, cf vastarg, vistarg, vitarg, vazurg, etc. Cf MPrth xwryndg or waryndg.
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
6865:vastarg: ~
7077:biyābān: ?viyäpän
7331:pīl-bān: pil-van
7341:puštbān, puštvān: puštē- pān
7455:šubān, Saban: šupan
```


## [2026-10-17T00:03:27.168Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wih[aā]nag\\|wihan\\|pōst\\b\\|pōst \\|bān \\[\\|\\bbān\\b.*roof\\|wāstar' PHD_mackenzie.txt | cut -c1-300 | head; grep -n -i 'wh’nk\\|wh.nk\\|pwst\\b\\|pwst’\\|b’n \\|b’n’' PHD.txt | cut -c1-300 | head"
}
```


### [2026-10-17T00:03:27.619Z] TOOL RESULT

```
5372:wihan(ag) [wh)n(k)', (b-) I M wh'ng, N bahana] cause, reason.
6174:cause (reason) Cim, wihan(ag); (case)      waccag, zadag, zahag.
10409:wayendag                 ,~    1'0""\              wihan, wiyan                   ,t""U' ,
10416:gir-t , kun-I               -\K)'\                 wihanag                      1 ~ t"'\)',
11273:                ""~~\                     wihanag                 \~~)
316:drón yaštan: consecrate the sacrificial bread. drēš [410] mark, branding; punishment. ~ag [-k!] *desolation. drēšīdan, dro$- [d/w$-ytn'] brand. drēūšom [dlwšwm] mark. droz-, v. druxtan. drózan [dlwen! | M, J drwzn] lying, liar. ^h: falsehood. drubušt [di(w)pwst'] fortress. ~ih: defence, fortific
551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~]
661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe
```


## [2026-10-17T00:03:32.160Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'bahän\\|bahan\\|bahāna\\|bänü\\|bānū\\|banü\\|\\bbäm\\b\\|\\bbām\\b\\|püst\\|pöst\\|pōst' HUB.txt | cut -c1-300 | head -20; echo ---; grep -n -i 'bahän\\|bahāna\\|bänü\\|bānū\\|\\bbäm\\b\\|\\bbām\\b\\|püst\\|pōst\\|pöst' HRN.txt | cut -c1-300 | head -20"
}
```


### [2026-10-17T00:03:32.710Z] TOOL RESULT

```
7623:skr. vasanta-; bahana 'Vorwand', skr. vasana- *Qewand';
---
126:(bei. No. 6), bartk, pöstden (bei. No. 308), terastden (bei.
1898:174. bäm 1) *Haus' s. bän (No. 175).
1903:afy. LW. bäm.
1907:worden. Dass np. bäm 'Haus' zu bämya- gehören
1911:175. {\)bän 'Haus; vergl. bänü (No. 178)2).
1948:1 vergl. säh]bänü 'Conyza' (AM. 162).
1949:g. bänü, banewün 'Königin',
1950:phlv. banük, Bänüki, N. pr. (Hörn, Mitteilungen,
3025:kurd. püstve, pfisl; af/. LW. pas; oss. d. fastäge, t.
3195:338. po8t 'Fell, Haut', pöstln,
3196:aw. pq8tö.[fra&ah' ; phlv. pöst, pöstln.
3197:LW. kurd. pöst ^ pTst 'Fell, Haut'; bei. pöst, pöst
3198:(213) ; afy. pöst ; wa/. p^i?^, sar. past,
```


## [2026-10-17T00:03:34.611Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1890,1960p HRN.txt; echo ----; sed -n 3190,3210p HRN.txt; echo ----; sed -n 7610,7630p HUB.txt"
}
```


### [2026-10-17T00:03:35.060Z] TOOL RESULT

```
') FR citirt als Beleg einen wortspielreichen Vers Senäl's
(Metr. Xeflf):
tä kl hhisesf /^äjS der bcUis
hälei ämed zt näz^ der hälis— 40 ~
aw. [/'vard', vareöayanuha 'wachse'; ai. l/'t?ardA-,
vdrdhati *wachsen\
np. välä gross* wird auch hierher gehören und nicht
als Dialektform zu bälä'^),
174. bäm 1) *Haus' s. bän (No. 175).
2) 'Morgen , bämdäd, bämdäddn *des Morgens' (z. B.
Vis und RamTn S. 41, Vers 6).
aw. mspö.]bäma' allbeleuchtend'; phlv. bämtk, bämdät;
ai. bhäma- 'Licht, Strahl*.
afy. LW. bäm.
Nach Geldner, Studien I, 77 bedeutet aw. bamya-
allerdings 'sublimis'; jedenfalls kann das Wort aber
nicht von der l^bhä- scheinen, leuchten getrennt
worden. Dass np. bäm 'Haus' zu bämya- gehören
sollte, ist mir aber sehr unwahrscheinlich; beim wird
secundär für bän stehen, wie sich auch sonst im
Auslaut ein Wechsel der Nasalen findet.
175. {\)bän 'Haus; vergl. bänü (No. 178)2).
phlv. bän 'Dach*.
kurd. bei. (27) LW. bän.
Jedenfalls nicht gleich jüd.-pers. JN^Z 'Zelt', wie
Geiger, Yätk. Zarlr. 50 will, denn JND selbst findet
sich dort, z, B. Is. 15, 3 3).
Nach FJ soll auch bälüden 'wachsen' bedeuten, wofür als Beweis
folgender Vers Mölevi Ma'nevl's angeführt wird (Metr. Remel):
In neseh peivest-i örä büM est
kez sehen sah än-l mih bälüd^ est
Die sprichwörtliche Redensart gurg-l bärändide *ein *Wolf, der nass
geworden ist* (vergl. Houtsma, Een paar perzisohe uitdrukkingen,
S. 11) will — beiläufig bemerkt — FR in bälän geändert wissen (also
*ein Wolf, der das Netz gesehen hat*); bUrän sei aus einem Miss-
verständniss entstanden.
*) FJ hat einen Vers Minöcihrl's als Beleg.
2) Vergl. gr. Sdjuag 'Hausfrau* neben ai. dam- (Schulze, KZ.
28, 281, dessen formale Erklärung von däfiag allerdings unrichtig ist,
vergl. Bartholomae, Berliner philolog. Wochenschrift, 1889, 386 und
Danielsson- Johansson, BB. 18, 11).
») Hörn, Ind. Forsch. II, 138, Nöldeke, ZDMG. 46, 140.- 41 —
Gehört hierher vielleicht auch np. evän 'Vorhalle*
aus a(Jlhi-\-bän, vergl. np. isiäden (No. 84), phlv.
evar (unter No. 16)?
176. {7)~hän *Herr*), -hütend, -schützend (Comp.)', -wan,
-wäne, z. B. päsbän^ suturwün, engust^wdtie,
aw. rand\pana' 'Beinschiene' ; phlv. ^pänak, -pün,
arm. LW. -paw; ai. pändr- ^schützend*.
177. bang *Ruf, Stimme', hanglden, DNl^jlZ 'Geschrei,
Klagen (Is. 14, 31 ; 15, 4, 5), nwXir:N2 (Is. 57, 13).
Kä§. hüng, vöng[vCLze (zweites Glied ist väj),
phlv. vdng, päz. vägined, vägmed jammert, klagt*,
Men. 2, 158, 165 (West, Pahlavi Texts^ 22 Note 2,
23 Note 1), arm. LW. vank, vang,
bei. gvänkj u, gvünJc *Ruf, Schall, Echo', gvänjag
'rufen (145, 146) ; kurd. LW. (?) bänk.
^78. bätm 'Herrin', wörtl. 'Hausherrin' (vergl. bän, No. 175) ;
1 vergl. säh]bänü 'Conyza' (AM. 162).
g. bänü, banewün 'Königin',
phlv. banük, Bänüki, N. pr. (Hörn, Mitteilungen,
Heft IV, S. 35, ZDMG. 44, 664 No. 92).
bei. bänuk, n. bänux (32).
178**'* bäver 'Glaube'.
Zu [/^var- 'glauben' mit upä (d. i. upa+ä)^),
179. baylsten müssen, nötig sein' (Imperson.), Praes.
^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
Kä§. apä (mit folgendem Futurum), vergl. ßmpeyd
etc. (S. 115).
\i
') Nie selbständig. Ghrest. Schahn. 10 ist hä an suwärän zu
----
aus Sa' dl und Gsedl.skr. (Sütr.) püjäyati 'Ehrfurcht bezeigen'; phlv.
pöfinak 'bereuend' ').
337. pü^e Pfote .
phlv. päcakf püzak 'Pfote'.
Zu pai, vergl. Hörn, BB. XVII, 258.
338. po8t 'Fell, Haut', pöstln,
aw. pq8tö.[fra&ah' ; phlv. pöst, pöstln.
LW. kurd. pöst ^ pTst 'Fell, Haut'; bei. pöst, pöst
(213) ; afy. pöst ; wa/. p^i?^, sar. past,
339. j>iifc, pwA: das Blasen (um Feuer anzufachen), Blase-
balg 2).
gr. (pvöa 'Blasen, Blasebalg, (pvonta *Blase'; arm.
puK 'Hauch', puUI^ Blasebalg , pKam 'sich aufblasen,
pcem 'hauchen' (nicht entlehnt nach Hübschmann
No. 285).
Die richtige neupersische Form muss buk sein.
Arm. p und gr. rp weisen auf indog. ph (vergl.
Bartholomae, BB. 10, 290), np. h auf indog. bh\
also indogermanische Doppelformen wie bei [/^veph-,
vebltr- u. ö.^).
340. puläd 'Stahl'.
----
hudi^ra-; hiStan 'IsLSsen* H. 1097; haft 'siehen H. 1098; ham
*zusammen, derselbe* H. 1102; hunar *Tugend' H. 1108 u.s.w.;
phi. A^ *feindliches Hear', arm. Aew, ap. Aaina-; Ifar^'Herat',
arm. Hrev = ap. Haraiva-; Humdi = phi. Humdk Yatk. i.
Zar. 62, 77, vgl. zd. huniaya- {humaya-); Hamadan = ap.
Hagmatdna- ') ; Hind = ap. Hindu- Indien ; Hindu Inder
= phi. Hinduk^ arm. Hndik-K Indien', Hnduk Inder Mos.
Kalank. I, 257, u. s. w.
b) im Inlaut: ddh *Sklave = skr. dasa-; mah Mond,
Monat* = ap. mdha-^ skr. mas-, mOsa- ; x^ahar *Schwester
= zd. x^'aiihar- ; aMaha Drache' = zd. am dahako ; bih gut,
besser = Siip.Vahyaz- (data^), arm. veh, skr. vasu-; bahd 'Werth,
skr. vasna- 'Kaufpreis ; bahor Triihling , ap. [&ura')vahara'?,
skr. vasanta-; bahana 'Vorwand', skr. vasana- *Qewand';
bahist, bihist 'Paradies* = zd. vahista-; dih *Dorf\ arm. deh,
ap. dahyth; phi. N(a)rs(e)hz = arm. Narseh, zd. nairydsatlha-.
XJeber pTh 'Fett* siehe p. 46.
Die arm. LehnwQrter haben hier gleichfalls iiber-
all k
§ 106. Anl. h vor u wurde im Np. zu x in': xusk
'trocken' = ap. {h)uska', zd. huska- ; Xusrav = arm. Xosrov
```


## [2026-10-17T00:03:39.803Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==36' HUB.txt | head -80; echo =====; awk 'BEGIN{RS=\"\\f\"} NR==43' HUB.txt | grep -n -i -B2 -A8 'bah\\|vah' | head -40; echo; awk -v RS='\\f' '/bahana .Vorwand/{print NR-1}' HUB.txt"
}
```


### [2026-10-17T00:03:40.908Z] TOOL RESULT

```
Exit code 1
- 25 -
Haus\ Ich halte daher auch Andreas' Etymologie:
ban 'Haus' = ap. vahana- (vgl. skr. vasana- 'Wohnen*,
arm. vanIS) nicht fiir richtig, zumal im Pehl. ban, aber
nirgends *v(ln hezeugt ist. Horn's Etymologie: evdn
(jetzt arabisiert divdn gesprochen Sal. Shuk. p. 7)
'Vorhalle' = adhi + ban hat nichts ftir sieh.
178. Ich bezweifle die Zugehorigkeit von bdnu *Herrin* zu
ban = bam *Dach, Haus*. — Die nordbal. Form lautet
banuK (Geiger, Lautl. p. 26).
178 bis jjp ipa^^ar 'Glaube, Vertrauen (afgh. LW. bavar
*belief, faith, confidence*, bavarl 'faithful, trustworthy')
gehort nicht zu upa + [/^var, sondern ist = paz. vawar
credibly, belief*, Shk. 272, phi. vawar (geschrieben
vapar)^) credible*, West, PT. II, 184, vawari-alto *is
believed*, ebenda 26, arm. vaver, vaver-akan glaub-
wiirdig, giiltig (WZKM 6, 79), an-vaver, an-vaver-akan
'unglaubwurdig, ungiltig, nichtig*. Vgl. zd. vaura- (aus
va-vr-a-) von var glauben' BB. 13, 80 und np. avari
glaubwiirdig oben unter Nr. 16.
179. Np. bdyad 'es steht an* konnte zu ayad *kommt' ge-
horen, also auf phi. "^upayat = ap. *upa -\- aitiy (skr.
upa + eti) zuriickgehen. Aus upO^ konnte nur ba
werden, wahrend sonst upa^ in Comp. vor Conson. zu
uWy aw werden musste. So kann auch t>ai (in andar-
vdi 'Bedurfnis*) formell = skr. upaya- fAnnaherung,
Mittel, Weg') gesetzt werden.
180. Vgl. afgh. bavr 'a leopard, a panther', kurd. bdvru-
beyOn Parderfell*, bavlubayan Telzkaputze* (?) Socin,
Samml. II, 286. Die Pehleviformen sind wohl wertlos,
vgl. phi. baprak (Phi. Min. p. 37, Z. 8) d. i. bawrak
'Biber' (Horn Nr. 181). So kommen wir uber np. habr,
*bawr 'Tiger nicht hinaus.
181. Dieses Wort ist auch arabisch: vaftr animal quadrupes
fele minus, pulveris colorem habens, cauda carens*.
Nach Noldeke ist vabr 'Klippdachs* „wohl echt
arabisch**.
*) Also falsoh ftir vavar, vgl. avar oben Nr. 53.
(eval):1: ==== not found
```


## [2026-10-17T00:03:43.861Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==43' HUB.txt | head -60; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"Vorwand\")) print NR-1}' HUB.txt"
}
```


### [2026-10-17T00:03:44.244Z] TOOL RESULT

```
- 32 -
*kusse' auf iran. *6awd-s-a»ii (vgl. Nr.240: toi'Geruch*
= zd. baoidi') zuriickfiihren. Np. mad 'Kuss' erinnert
an afgh. maca *Kuss'. — Arab, 'arus lautet im Persi-
schen *ards (N5ldeke).
236. Np. buSdsp Traum' u. s. w. (Noldeke, Pers. Stud.
II, 1, Anm. 4) ist Lehnwort aus dem Avesta (zd.
bUsyqsta, paz. bUsydsp) und entstellt.
242. Die Suffixe np. a, a, t, U, o =■- phi. afe, Oi, Fi, uk, dk,
die massenhaft vorkommen, sind eine Neuschopfung der
Arsacidenzeit, -) vielleicht auf Grund einiger weniger aus
dem Altpersischen iiberkommener Muster (wie banda
= phi. bandak = ap. bandaka- Diener neben band,
s. Nr. 219). Daher braucht haJia *Wert' = paz. vahd
Shk. 270 = phi. vahak nicht auf ein idg. ^vesdkO"'^
zuriickgefiihrt, sondern kann = ap.*e?aAa- gesetzt werden
(vgl. np. bCLzU 'Arm', arm. LW. bazuk, also arsacid. phi.
= *bdzuk == zd. bazU'y skr. bdhu- etc.). Ich stelle also
np. bah-a, phi. vah-dk zu skr. vas-na-, Im Uebrigen
hatte der Hinweis auf Solmsen, KZ. 29, 81 genugt.
243. Vgl. Nr. 501.
244. Np. bahdna Torwand' kann weder = skr. apidhdna-
fBedeckung, Hiille, Decke* — Darmesteter) noch =
skr. upadhdna- ^Deckel' etc. (vgl. upadhd- *Betrug' —
Horn, KZ. 32, 588) gesetzt werden, wie das Pehlevi
zeigt. Skr. vidhdna- 'Ordnung etc passt wegen der
Bedeutung gar nicht und soUte np. *bihan oder *guh(ln
lauten. Das Wort geht iiber paz. vahana = vahdn
*cause' Shk. 270 (vgl. avahdn without a cause' Shk.) =
phi. vahcLnak auf ap. ^vahdna- zuriick, das ich mit
Fr. M tiller zu skr. vasana- *Gewand' stelle. Der Be-
griflfsubergang : Kleid— Hiille — Vorwand macht doch
keine Schwierigkeit. Vgl. d. Ge-wand und Vor^wand^
d. Hiille und hehlen, lat. praetexo Verbramen, be-
manteln, als Vorwand nehmen', praetextus * Vorwand'
etc., WZKM. 5, 186.
^) Uebrigens nioht nur im Persischen sondern auch in den andern
iranischen Spraohen.
42
165
224
```


## [2026-10-17T00:03:49.651Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['MON']['lookup_hint']);print(d['ARY']['lookup_hint']);print(d['SOD'].get('lookup_hint'));print(d['SNS'])\" | cut -c1-900; command ls data/verification/sources/refs/incoming/ARY/"
}
```


### [2026-10-17T00:03:50.069Z] TOOL RESULT

```
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}
{'title': 'Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986', 'kind': 'archive_djvu', 'url': 'https://archive.org/details/VajnameShayest', 'lookup_hint': "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", 'local_file': ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt'], 'page_offset': '242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image', 'covers_etymology': True, 'notes': 'OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Ve
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
```


## [2026-10-17T00:03:53.058Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in 'بهانه' 'بام' 'بانو' 'پوست' 'واستر'; do echo \"## ARY $w\"; grep -n \"$w\" incoming/ARY/ARY_pages.txt | head -4 | cut -c1-200; done; for w in 'BAHANE\\|BAHĀNE\\|BAHANA' 'BAM\\b\\|BĀM' 'POST\\b\\|PUST\\b' 'VASTAR\\|VĀSTAR'; do echo \"## ARYlat $w\"; grep -n \"$w\" incoming/ARY/ARY_latin_index_pages.txt | head -4 | cut -c1-200; done"
}
```


### [2026-10-17T00:03:53.784Z] TOOL RESULT

```
## ARY بهانه
## ARY بام
13853:پهلری (اتمابامم: ,1۸3 زا
14254:: پهلوی (۲اتله: ۰ ۸1۸۵۲ ,1453۷157126 آلباتی (السابامشتم: 1120۷0 ,11030
## ARY بانو
## ARY پوست
107:پوست هستند ولی زبان مادری بیشتر آنها یک زبان هند و اروپایی (یعنی اسپانیایی) است. :
219:و پوست سفید تجسم می‌کنند (5663 ,01۸-1-07؟ فعلاً برای این پرسش‌ها پاسخ قاطعی در
331:1089 ۲57۸716) نشان می‌دهد که سفید پوست و «دراز سره (311۸31ه0011017028) از
925:منحصر به اقوام هند و اروپایی نیست. رزم آوران سرخپوست در آمریکا و سیاهپوستان در افریقا نیز
## ARY واستر
## ARYlat BAHANE\|BAHĀNE\|BAHANA
## ARYlat BAM\|BĀM
## ARYlat POST\|PUST
1341:Lasgly gel UT Layla gant leas PAFEN sls yPUST (S,luls » BOUFFEE
4779:BARNHART: (POST) 822 PAS AFGHAND (-4) g's!
4785:rer sabi aby POST-, POSTE ALATIN) 63
4854:BUCK: 211-212 POST ENGLISH) lS
## ARYlat VASTAR\|VĀSTAR
```


## [2026-10-17T00:03:56.042Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 1325,1350p ARY_latin_index_pages.txt | cut -c1-200; grep -n 'pdf page' ARY_latin_index_pages.txt | awk -F: '$1<1341' | tail -1"
}
```


### [2026-10-17T00:03:56.632Z] TOOL RESULT

```
NE alesse Lee dly op!
Sn) cod os can y9 Cyabd gt JB SeSLy ST tg eth et JU Sel Seal od CTP
ceil y SVADOS cp Sucle ghan5ly WT cgrni gilean ty (o4eT cK jl agin FA
a. cul Siig 1SeeSSSE glll SWEET
VS Solus y FLIEHEN (gLST y FLEE gaol Sit slanjly clad gos wo5ly-d
. isle Gl gla (POKORNY: 837 - “PLEUK gh)! 4 28 Ga ply 5!) FLYGTE
cab ee Sole y apt glands ar leglEl op yp for y2 Gls, il (lar By 23)
Fosla opey tet Veadly onl dle UT Sg bojly
[pdf page 49]
Obj phy! sata Glad, | Os
gula yNARWA of gla y NARROW (euolSil slaedy b ge sbs Sir ” Slyet
el 0 Gand 5g Waly ool ahysyl y a Gt erly dy auld Glas NAAR
gPIS (Sjlasls y PISSEN LAT y PISS cK glao§ly colt es wo5ly-t
go WT pablaal ys Ge Gea pl 9 9 25) ged gles PISS gj) 9 PISSEN ule
bean (ONOMATOPOIC) 1 sTeln pT stan So s2oge 1 y Ci
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
1333:[pdf page 49]
```


## [2026-10-17T00:04:03.180Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; if ($0 ~ /p[oōö]st/ ) print n}' BQT_v1_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; if ($0 ~ /bānūk|bānūg|banuk|bānōk/ ) print \"banu\",n}' BQT_v1_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; if ($0 ~ /vihānak|vahānak|wihānag|vahâna|vihān/ ) print \"bahane\",n}' BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:04:03.987Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:04:06.018Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 1500 BQT_v1_pages.txt; grep -c . BQT_v1_pages.txt; grep -n 'pdf page 64[0-9]\\]' BQT_v1_pages.txt | head"
}
```


### [2026-10-17T00:04:06.342Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م۸
و «ارس‌شبات
4
د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد *
کلیه حقوق‌تجد ید طبم کتاب برهان قاطع با تمحیحات وحواشی و
تملیقا ت وتصا ویرواقتباس‌وتلخیص وترجمه آن بنام‌جنابمالی
محفوظ ومخصوص خوا هد بودضمنا وزا رنفرهنگ فرصت رامفتنم شمرد ه
بد ینوسیله اززحمات شماد رانجام این‌خد مت مهم فرهنگی قد رد انی
میکند وموفقیت آن) ستا د محتر مراد را ینکونه خد مات خواستاراست»
هنگ
رن
یی سینشیر زوا عرسا رده ارسال ۱۳۱۷ ۰۳۳1« 9 لو امد ۰
/ ی و ۷ مر
دسج ناویح ( منیا مینست
با ل 32486
```


## [2026-10-17T00:04:08.787Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:427 --image 2>&1 | tail -60"
}
```


### [2026-10-17T00:04:09.286Z] TOOL RESULT

```
no scan of BQT covers printed page 427 (see 'scans' in refs_online.json)
```


## [2026-10-17T00:04:11.726Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 640 642 644 646 648 650; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n 'پوست' | head -3 | cut -c1-200; done"
}
```


### [2026-10-17T00:04:12.593Z] TOOL RESULT

```
== leaf 640
== leaf 642
== leaf 644
== leaf 646
== leaf 648
== leaf 650
```


## [2026-10-17T00:04:14.429Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {c=gsub(/پوست/,\"&\"); if (c>2) print NR-1, c}' BQT_v1_pages.txt | head -20"
}
```


### [2026-10-17T00:04:14.833Z] TOOL RESULT

```
653 5
```


## [2026-10-17T00:04:16.960Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==654' BQT_v1_pages.txt | grep -n -B2 -A3 'پوست\\|post\\|pōst\\|pust' | head -60"
}
```


### [2026-10-17T00:04:17.508Z] TOOL RESULT

```
26-است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
27-ومذمت باشد .
28:پوست باد کر دن -کنابه از طبار
29-نه دلی نمودن وراز گفتن باشد .
30:پوست یرای - با بای فارسی
31-حطی زده » چرم کر و دیاغ را کویند .
32-بوست دادن » کنابه از اظهار ته
33-دلی نمودن ومافی‌النمیر گفتن باشد .
--
35-از بی حیامی و بی شرمی‌نمودن باشد .
36-بوستگال ه باکاف فارسی بالف کشیده
37:وبلام زده ؛ پوست بی‌مویرا گوسد که درزبردنبة
38-کوسفتد مي باشد وآرا باندك دلبه جدا کرده
39-در سبراب بر ند» و دوست در کوسفند را ف ‏
40-کلته‌ادد که سر ککن از حودیای آنآ و بشتهات .
41-۱ بوستگا له بالام بر وزن بوست پاره,
42:بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
43-ودوست مقعد کوسفندباشد ۰
44-فوست کردن - کنابه از الیس
45-و محرم ساختن باشد - و غیبت نمودن و خبث
```


## [2026-10-17T00:04:19.554Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==654' BQT_v1_pages.txt | sed -n 1,27p; awk 'BEGIN{RS=\"\\f\"} NR==654' BQT_v1_pages.txt | grep -n '[a-zA-Z]\\{3,\\}' | head -20"
}
```


### [2026-10-17T00:04:20.270Z] TOOL RESULT

```
4 ۷۲۷-
ود یان - بکرثاك بر وزن‌حوربان»
۱ رای شهر کنوح۱ هم هست -
و زای هوز » پبرامونو کردا کرد دهان حیوانات
باشد - ومایین لب و بیتی را نیز گویندسوبم‌عنی
ساق درخت هم امده است.و نقار مرغاثرا نیز
کفته‌اند» و با زای فارسی م ۲۳
۰ ۳۹
پورش ۴ - با ابی مجهول بر وزن
سوزش » بمعتی عذر ومعذرت‌وعذرآوردن‌ومعذرت
خواستن باشد .
لودن » بر وزن سوزن » زمینی را
گویند. که بجهت زرات کردن پاك کرده
بشند .
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
```


## [2026-10-17T00:04:22.965Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==654' BQT_v1_pages.txt | tail -40"
}
```


### [2026-10-17T00:04:23.270Z] TOOL RESULT

```
ور ه ۳ بر وزن دوزه » بیرامون
و کردا کرد دهانرا گونند - و بمعتی ننةٌ درخت
هم‌آمده اس 8۵
ود ین ه بر وزن کوزیدن . عذر
آوردن وحعذرت خواستن باشدل" 3
وس » بر وزن طوس ۰ چرب زبانی
و قرب و فروتتی را گویند۷ .
دو یا نه بر وزن روزانه » قرب دادن
وفرونتی و بزبان خوش مردم را فربفئن .
لو ست هه ی وزن دوست » معروف
۱
است ۸ - و بمعنیغیبت هم آ مده‌استکهبد گوبی
ومذمت باشد .
پوست باد کر دن -کنابه از طبار
نه دلی نمودن وراز گفتن باشد .
پوست یرای - با بای فارسی
حطی زده » چرم کر و دیاغ را کویند .
بوست دادن » کنابه از اظهار ته
دلی نمودن ومافی‌النمیر گفتن باشد .
بوست سگ‌بر و کشدن- کناب
از بی حیامی و بی شرمی‌نمودن باشد .
بوستگال ه باکاف فارسی بالف کشیده
وبلام زده ؛ پوست بی‌مویرا گوسد که درزبردنبة
کوسفتد مي باشد وآرا باندك دلبه جدا کرده
در سبراب بر ند» و دوست در کوسفند را ف ‏
کلته‌ادد که سر ککن از حودیای آنآ و بشتهات .
۱ بوستگا له بالام بر وزن بوست پاره,
بهعنی پوستگال است که پوست زبردنبةٌ گوسفند
ودوست مقعد کوسفندباشد ۰
فوست کردن - کنابه از الیس
و محرم ساختن باشد - و غیبت نمودن و خبث
کردنرا گویند .
و ستین » لباسیاست‌مسرونه۹ .و کنابه
از غیبت ومذعت وعیب هم‌هست .
۴ کردی002, ۳6۵2, افغانی 0672 .
دروس ورامین) «اسشق ۳۳۹*.
۵ رك : بوز .
نت اسم مصدراز پوزیدن ( مسعمل
۷ - ره : پلوی .
و
```


## [2026-10-17T00:04:27.467Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; curl -sL -o bqt427-551.jpg 'https://archive.org/download/borhan-ghate-v1/page/n653_w1400.jpg'; file bqt427-551.jpg; command ls -la bqt427-551.jpg"
}
```


### [2026-10-17T00:04:29.796Z] TOOL RESULT

```
bqt427-551.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
-rw-r--r-- 1 sfmqrb sfmqrb 520643 Oct 16 20:04 bqt427-551.jpg
```


## [2026-10-17T00:04:32.622Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt427-551.jpg'); w,h=im.size; im.crop((0,int(h*0.72),w,h)).save('bqt427-551-foot.png'); im.crop((0,0,w,int(h*0.12))).resize((w//2,int(h*0.06))).save('bqt427-551-top.png')\""
}
```


### [2026-10-17T00:04:33.206Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-17T00:04:35.941Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; magick bqt427-551.jpg -crop 2479x1000+0+2500 -resize 60% bqt427-551-foot.png 2>&1 || convert bqt427-551.jpg -crop 2479x1000+0+2500 -resize 60% bqt427-551-foot.png; magick bqt427-551.jpg -crop 2479x300+0+0 -resize 40% bqt427-551-top.png; command ls *.png"
}
```


### [2026-10-17T00:04:37.138Z] TOOL RESULT

```
bqt427-551-foot.png
bqt427-551-top.png
bqt540-591.png
bqt540-593.png
bqt540-594.png
crop545a.png
pg539.png
pg540.png
pg545.png
pg550.png
pg551.png
pg552.png
pg554.png
pg558.png
```


## [2026-10-17T00:04:39.066Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt427-551-foot.png"
}
```


### [2026-10-17T00:04:39.111Z] TOOL RESULT

```

```


## [2026-10-17T00:04:45.174Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; mkdir -p ocr/BQT; cat > ocr/BQT/427.vision.txt <<'EOF'\n[Read from archive.org borhan-ghate-v1 leaf n653 (printed p. 427), footnotes; transcribed by vision, page 551 verification]\nپوست - بر وزن دوست، معروف است (۸) - و بمعنی غیبت هم آمده است که بدگویی و مذمت باشد.\nپوستین - لباسی است معروف (۹) ...\n۸ - پهلوی pôst «نیبرگ ۱۸۶»، «تاوادیا ۱۶۴ :۲»، اوستا pasta «بارتولمه ۹۰۴»، کردی pîst ، pôst ، افغانی pôst ، وخی pîst ، سریکلی past «اشتق ۳۳۸» ؛ جلد یعنی غشایی که بدن انسان و حیوانات را می پوشاند - پردهٔ بیرونی - قشر .\n۹ - پهلوی pôstîn «اشتق ۳۳۸»، pôstên «اونوالا ۵۶۶ ب»؛ لباسی‌جبه مانند از پوست بز و گوسپند.\nEOF\ngrep -n -i 'pwst' SOD_pages.txt | head; grep -n -i 'pwst' SOD.txt | head"
}
```


### [2026-10-17T00:04:45.643Z] TOOL RESULT

```
10816:2445 p'5tr B                                         jtif   2458 p'mpwst     M                              jiL^tA&A
10817:                                                                 Pambust ©MP bambist         ^^mpwst
13604:      judge                                                         TPS 1959, 10; 5}y pwsty, Frye 15, 16, 21 "slave
13606:3443 S'tnm'nn B, S                     ^^^r-^ojfc            3455 5>y pwsty S                            *S j*$(J>jJ)x~>
21070:6040 npwsty = n+pwsty =» n-, pwst'k                                    primordial
22240:6444 p'mpwst    M, S                       jL^ <<£u
22242:     pambust    ©pi. ~th ^P'mPwst
27413:        71.2, 85.5, 10                                        8228 pwst'k B, S       (oy> ^jlj jS)SZ* <<ub t^y ^j£
27414:8216 pwrny'nyCy)*        M =» pwrny}nyh                            poste (pwsty, pwst>y, pwstk) ©<OP pavasta-,
27415:8217 pwrs-        S => }prs-, prs-                                   Parth. pwstg\ Skt. pustaka ©ace. pwst())kw,
23884:2458  p'mpwst   M  jiL^tA&A 
23885:Pambust  ©MP  bambist   ^^mpwst 
30387:TPS  1959,  10;  5}y  pwsty,  Frye  15,  16,  21  "slave 
30390:3455  5>y  pwsty  S  *S  j*$(J>jJ)x~> 
48325:6040  npwsty  =  n+pwsty  =»  n-,  pwst'k 
51048:6444  p'mpwst   M,  S  jL^  <<£u 
51049:pambust   ©pi.  ~th  ^P'mPwst 
63292:Sogdica.  3424;  3sg.  pres.  pwst,  Hen.  Cosm. 
63329:8228  pwst'k   B,  S  (oy>  ^jlj  jS)SZ*  <<ub  t^y  ^j£ 
63330:poste   (pwsty,  pwst>y,  pwstk)  ©<OP  pavasta-,
```


## [2026-10-17T00:04:47.282Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63320,63340p SOD.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"8228 pwst\")) print NR-1}' SOD_pages.txt"
}
```


### [2026-10-17T00:04:47.846Z] TOOL RESULT

```
8227  pwskfty   M  jUb  icJd\s^A{J>  ijo\j&\  d^> 
pu-skafte   ©<*pw-skfs-,  Skamp-   =^skfty 
unobjecting 

GMS  369;  BBB  686;  Hen.  Tales.  467.53,  469  n  1; 
MSP  b  153 

8228  pwst'k   B,  S  (oy>  ^jlj  jS)SZ*  <<ub  t^y  ^j£ 
poste   (pwsty,  pwst>y,  pwstk)  ©<OP  pavasta-, 

Parth.  pwstg\  Skt.  pustaka   ©ace.  pwst())kw, 
pwstw;  abl.  pwst\  pL  pwst(>)yt,  pwstkt\  ob.  pi. 
pwstyty 
book,  Sutra,  document,  writing,  parchment 
GMS  604n  1;  SCE;  TSP;  BSTBL;  Frag.  Len.;  KG; 
MSP  c6;  STi;  STii;  C2;  MD;  Anc.  Lett.  2.47;  CII 
1990,  85;  pwst>kwt  SCE  193,  200;  Dhy.  395; 
pwstw,  C2,  104R9;  pwst\  C2,  77V12,  120  R30; 
pwst(>)yt,  TSP  2.339;  MDii;  C2,  55R28;  STi  53.1; 
398
```


## [2026-10-17T00:04:50.554Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==398' SOD_pages.txt | grep -n -i -B3 -A3 'skin\\|hide\\|pwst ' | head -30"
}
```


### [2026-10-17T00:04:51.095Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:04:53.003Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -B4 '^ *skin *$\\|  skin  \\|skin, hide\\|^skin' SOD.txt | grep -i -B4 'skin' | grep -i 'pws\\|pst\\|skin' | head -20"
}
```


### [2026-10-17T00:04:53.453Z] TOOL RESULT

```
5079:paper,  silk,  skin  and  wood.  Most  of  them  were  in  the 
29028:skin,  leather 
29035:skinworker 
63346-8230  pwst(h)  S  <*^  <f->^  *c~*-* 
63349:skin,  leather 
88273:coloured  skin     8502 
88470:cow's  skin     4075 
93721:skin     3254,3256,8230 
93723-(/c?)skin    525,  2847 
93725:skinworker    3255
```


## [2026-10-17T00:04:54.829Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63344,63356p SOD.txt"
}
```


### [2026-10-17T00:04:55.348Z] TOOL RESULT

```
8229  pwst*y  =*  pwst>k 

8230  pwst(h)  S  <*^  <f->^  *c~*-* 
post 

skin,  leather 

MDii  p210;  MDiii  pl27;  Frag.  Len.  61.3,  4 

8231  pwstk  =*  pwst>k 

8232  pwstkr}ynk   S  <j  J^f  >r  <ls*^ 
post-karene  ?
```


## [2026-10-17T00:04:57.676Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pavast\\|pavasta' KNT_full.txt KNT.txt | head; grep -n -i 'vastra\\|vah- vb\\|ä\\?vahana' KNT_full.txt | head"
}
```


### [2026-10-17T00:04:58.436Z] TOOL RESULT

```
7163:-daha, naham, атуйћа bagaha, dvahanam, Giira- 
8537:‘town’; dvahanam ‘village’; didà ‘fortress’; kaufa 
14348:‘fortress, stronghold’, vardanam ‘town’, dvahanam 
17145:33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 
20010:46 & : kartā : Abirádus : nàma : àvahanam : Ujaiy 
22911:dvahana-, and in the second parts of compounds 
24118:dvahana- sb. ‘village’ (5166): deriv. (8147.1) 
24120:‘being’. dvahanam DB 2.33; DSf 46. 
28911:vah- vb. ‘dwell’, see àvahana-. 
29029:IT, ТУ), ‘Conqueror, Winner’ (hardly *vivahana-,
```


## [2026-10-17T00:05:00.567Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'pavas\\|pav.st\\|parchment\\|clay tablet' KNT_full.txt | head; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"196\")>0 && index($0,\"LEXICON\")>0) print NR-1}' KNT_full.txt | head -3"
}
```


### [2026-10-17T00:05:00.891Z] TOOL RESULT

```
1601:by the parchment manuscripts of Auroman; and 
15649:broken clay tablets, in 5 lines; one copy in the 
15663:DSb = Darius, Susa в: Two clay tablets, one 
15713:broken baked clay tablet, with 58 lines: 27 on 
15985:3 limestone tablet simulating a clay tablet, found 
16411:Spur. b, c, d, e: Four baked clay tablets secured 
0
```


## [2026-10-17T00:05:03.423Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^pa[a-z]*-\\|^pā' KNT_full.txt | head -40; grep -n '^196$\\|^ *196 *$\\|LEXICON 196\\|196 OLD PERSIAN' KNT_full.txt | head"
}
```


### [2026-10-17T00:05:03.790Z] TOOL RESULT

```
1864:paru-zana- ‘having many men’, with z from j. 
2723:pada- might theoretically be grama- or garama- 
2877:parlara- ‘battle’, Av. posana-, Skt. prtana-. 
4815:parsd-miy, Skt. precha-mi, Lt. poscó. 
4942:pati-padam ‘on its base’, Skt. padd- ‘step’, Gk. 
5262:pasti- foot-soldier’, from *patsti- from *ped-t-. 
5487:pais-. 
6181:pan-tas. 
7215:pard-gmala ha"gmalà à-jamiyü. 
7256:pati-vd,, DB .1:207 aatpati-mé DNb 20; avā- 
7779:pati-kara- ‘made thereto’ = ‘sculptured figure’; 
8333:paru-zana- ‘having many men’; vispa-zana- ‘hav- 
9031:pari-ay- ‘respect’, is probably inst. rather than 
10040:para-draya (also as two words), pasdva (from 
10803:patiy-arsayaty ‘I ruled over’, ріс. zsayamna 
10847:pati-paya ^w. E 
11082:pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; 
11623:par-; ditam, cf. Av. zyà-; hita- in An-d-hitd, of un- 
12885:pati-vd (DB 1.20), with accusative in |pa]tiy 
23641:pati- + ay- ‘come to, come into the possession 
23651:pari- + ay- ‘go around before, respect’, with 
24130:pali- + avahya- ‘ask for help’: patiydvahyaty 
25278:pali- + z$ay- ‘have lordship over’: patiyarša- 
25592:pada- ‘step, station’ ($29, §31, $149.1, $161.Ib, 
25814:pali- + jan- ‘fight against’: patzyajatà imf. mid. 
26884:pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- 
27095:pati- + pã- mid. ‘protect one’s self against’, 
27123:pai- (§89, §144.V). See also Parsiyduvada-. 
27146:pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. 
27175:palikara-, Patigraband-, perhaps Pátisuvari- and 
27184:patikara- sb. ‘picture, (sculptured) likeness’: . 
27245:pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. 
27247:pasti-. 
27250:pada- sb. 'footing, step, station': Av. paóa- 
27261:pada-. püdaibiyà idm. ($189) DNb 41. 
27264:par- vb. ‘communicate’: Av. *par- ‘hindureh-, 
27313:parana- adj. ‘former’: deriv. ($147.11) of stem 
27325:pariyana-. 
27331:pariyana- sb. ‘superiority’: deriv. ($147.IT) of 
27338:paru- adj. ‘much, many’: Av. pouru-, Skt. 
27328:196 OLD PERSIAN
```


## [2026-10-17T00:05:05.399Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27328,27420p KNT_full.txt | grep -n -i -B2 -A6 'pav\\|pas' | head -40"
}
```


### [2026-10-17T00:05:05.878Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:05:07.239Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 27328,27470p KNT_full.txt | grep -v '^\\s*$' | head -90"
}
```


### [2026-10-17T00:05:07.526Z] TOOL RESULT

```
196 OLD PERSIAN 
pariyana- sb. ‘superiority’: deriv. ($147.IT) of 
pariy, in meaning seen in Ау. pairi ‘vorne, über 
... hin’, Skt. pári as prefix ‘much, excessively’, cf. 
Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, 
Sen 250). pariyanam nsn. DNb 52. 
paru- adj. ‘much, many’: Av. pouru-, Skt. 
purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). 
See also paruzana-. рати) nsm. ($114, $127, 
$140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 
4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; 
XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 
7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 
4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6, 7; 
Азра 6, 7. 
paruva- adj. ‘being before in time or place’ 
(§35.1[): Av. paurva-, Skt. pürva-, pIE *pruos 
(868, $150), ef. Gk. Ion. трохоѕ ‘early’. See also 
paruviyata, paruviyaüd. parwā npm. ‘former’ 
DB 4.51. parwam asn. as adv. ‘formerly’ DB 
1.9; DBa 15f; DSe 43°, 47; XPh 36, 39; paruvam- 
ciy DB 1.63, 67, 69. 
parwnyata, adv. with preceding hacd, ‘from 
long ago’: *paruviya- (ie. *parvya-, deriv. of 
paruva-), Av. paouruya-, Skt. pürvyd-, + adv. 
suffix -la^, Av. -£ó, Skt. -tas, Gk. -ros, Lt. -tus asin 
funditus, pIE *-los ($191.11). C£. also paruviyatà. 
DB 1.7, 8, 45; DBa 11, 12. 
[paruv|iyafà adv. ‘at first attempt’: *paruviya- 
(see paruviyala) + adv. suffix -0à, Av. -fa, Skt. 
-ihà ($191.ID). DSj 3 (conj. of Brandenstein, 
WZKM 39.49-51; ef. note ad loc.). 
paruzana- adj. ‘having many men, or many 
kinds of men’ (‘having men of all tongues’, Wb. 
ZfA 44.165, after the Akk.): paru- ‘many’ + 
zana- ‘man’ ($9.11, $88, $120, $161.ППа). paru- 
zanānām (5140.1) gpf. DE 15f; XE 15f; А!Ра 12°. 
poruvzandndm (523.1) XPb 15f; XPd 11. раги 
zandnam ($23.11, $44) XPa 8; XPe 7; XPf 11; 
XPh 9; XV 12. 
Parga- sb. ‘Parga’, a mountain in Persia: 
Elam. par-rak-qa, NPers. Purg ($30). Parga 
лет. DB 3.44. | 
partara- sb. ‘battle’ (as in Elam. and АКК. 
versions): extension of -r/n- stem (530, $148.I, 
6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- 
‘battle, army’, to root in Av. poral-onie ‘they 
fight’? (Bv. TPS 1945.69-4; not agency noun 
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. 
$277; not paratara- ‘foe’, with Wackernagel, KZ 
59.29-30, as compar. to [Skt.] pára- ‘distant’ = 
RV ‘enemy’). partaram asn. DNa 47. 
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also 
тазе, as sb. ‘Parthia’, a province of the Persian 
Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. 
IIapóià. Extension ($150) of stem seen with 
vriddhi in Pársa-, but with dialectal difference in 
the 0/s ($9. VT, 887). 
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. 
Par&avaibi$ ipm. DB 2.96. 
(2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92; 
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20. 
Par8avai ism. DB 2.94° 96°; 3.5, 10. 
parna-, see duildparanam, parana-. 
‘parsa- vb., see fraó-. 
?parsa- sb. ‘court’, only in Hz. ApI 278; for 
his pa[r|saiy lsm. DNb 22, see under patiy. 
Pársa- adj. ‘Persian’; also masc. as sb. 
‘Persia’, a province of the Persian Empire: Elam. 
par-sin, АКК. pa-ar-su, Gk. Перо, Пероќа (§9. VI, 
$87, §126, 5143.11). See also Paréava-. ` 
(1) ‘Persian’: Pársa nsm. DB 1.49; 2.18, 19, 49; 
3.18, 26, 31, 32, 56, 84; 4.16, 26, 83, 84 bis, 85 bis, 
86; 5.8°; DPe 22; DNa 18, 46; DN i; DSe 12; 
DZe 7; XPh 12; A?P 1. Pérsam asm. DB 2.81; 
8.2, 29f; DPe 21. Pàrsahyà gsm. DNa 13f, 43; 
DSe 13; XPh 12. Pérsé ism. DPe 8. 
(2) ‘Persia’: Pársa пзш. AsH 3 (for loc., §52.1); 
DB 1.14, 41; 2.7; DPd 6f; DSm 6°. Pársam asm. 
AsH 8f; DB 1.46; 3.33, 34; 49, 28; DZe 12. 
Pérsam-cé DB 1.66. Pürsá ism. XPa 14 (here 
‘Persepolis’, acc. to Cameron, by letter; $166, 
6166.1). Pürsà absm. РМа 18, 46f; DSe 17°; 
Юле 7f, 10; XPh 16. Parsa for lsm. AmH 2 
(856.V, §314b; wrongly Hz. AMI 4.132-4, 8.17- 
9, as instr. of extent); for пзш. AmH 5 ($53; not 
nsf. adj., as taken by Hz. AMI 820-1, 34). 
Pärsaiy lsm. DB 1.2, 34; 2.9; 3.23, 24, 28, 34, 52, 
58, 71; DBa 2. 
pasü prep. ‘after’, temporal with асе. and
```


## [2026-10-17T00:05:11.307Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'carma\\|čarma' KNT_full.txt | head"
}
```


### [2026-10-17T00:05:11.627Z] TOOL RESULT

```
20126:dara and from Carmania. 
25111:Karmüna- sb. ‘Carmania’, a district of South-
```


## [2026-10-17T00:05:16.663Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^posteen\\|^poshteen\\|pōst\\b\\|pōstīn\\|postin' KLN_1966.txt | head; for n in 621 622 623 624; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -3 | tr '\\n' ' '; echo \" <- leaf $n\"; done"
}
```


### [2026-10-17T00:05:17.153Z] TOOL RESULT

```
29763:posteen,  n.,  an  Afghan  leathern  pelisse  (Anglo- Indian).  —  Pers.  postin,  ‘of  leather’,  fr.  post, ‘hide,  leather’,  which  is  rel.  to  Pehlevi  post, Avestic  pqsto,  of  s.m.
fr.  OF.  pere  (F.  poire), fr.  VL.  piratum,  ‘made  of  pears’,  fr.  L.  pirum, ‘pear’.  See  pear. persalt,  n.  (chem.)  —  Formed  fr.  per-  and  salt, perse,  adj.,  grayish  blue.  —  ME.  pers,  fr.  OF. (=  F.)  pers  (fern,  perse),  ‘greenish  blue’,  fr. Late  L.  persus  (whence  also  It.  perso,  ‘dark red’,  OProven?.  pers,  ‘dark  blue’),  back  for¬ mation  fr.  L.  persicus,  ‘resembling  a  peach, peach-colored’,  fr.  Persicus,  ‘Persian’.  See  peach. Persea,  n.,  a  genus  of  trees  (bot.)  —  ModL.,  fr. L.  persea,  ‘a  tree  growing  in  Egypt  and  Persia’, fr.  Gk.  TtEpasa. persecute,  tr.  v.  —  MF.  (=  F.)  persecutor,  fr. persecutes,  ‘persecutor’,  fr.  OF.,  back  forma¬ tion  fr.  Eccles.  L.  persecutor,  fr.  L.  persecutus, pp.  of  persequi,  ‘to  pursue’,  lit.  ‘to  follow  perse- veringly,  follow  after’,  fr.  per-  and  sequi,  ‘to follow’.  See  sequel  and  cp.  words  there  referred to.  <- leaf 621
 adj.  —  MF.  (=  F.)  persuasif  (fem. persuasive ),  fr.  ML.  persuasivus,  fr.  L.  persuasus, pp.  of  persuadere.  See  persuade  and  -ive. Derivatives:  persuasive,  n.,  persuasive-ly,  adv., persuasive-ness,  n. persulfate,  persulphate,  n.  ( chem .)  —  Formed  fr. per-  and  sulfate.  <- leaf 622
r.  v.,  pett-ed,  adj., pett-er,  n.,  pett-ing,  n. pet,  n.,  peevishness.  —  Of  uncertain  origin;  per¬ haps  fr.  pet,  ‘fondled  animal’. Derivatives:  pett-ed,  adj.,  pett-ed-ly,  adv.,  petl- ed-ness,  n.,  pett-ish,  adj.  <- leaf 623
oun  formed  fr.  puier,  ‘to  prop,  support’, fr.  VL.  *podiare,  fr.  L.  podium,  ‘an  elevated place,  parapet,  balcony’,  fr.  Gk.  noStov,  ‘base, pedestal,  balcony’,  dimin.  of  nouc,  gen.  :ro86<;, ‘foot’.  See  foot  and  cp.  -pod,  podium,  puy.  Cp. also  appui,  apoggiatura. Derivatives:  pew,  tr.  v.,  pew-age,  n. pewee,  also  spelled  peewee,  n.,  1)  the  flycatcher; 2)  the  lapwing.  —  imitative  of  the  bird’s  cry. pewit,  peewit,  n.,  the  lapwing;  the  pewee.  —  Imi¬ tative.  See  prec.  word. pewter,  n.,  any  of  various  alloys  having  tin  as their  chief  constituent.  —  ME.  pewtyr,  pewtre, fr.  OF.  peltre,  peautre,  fr.  VL.  peltrum  (whence also  It.  peltro,  OProveng.,  Sp.  peltre ),  which  is of  uncertain  origin.  Cp.  spelter.  <- leaf 624
```


## [2026-10-17T00:05:20.121Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"posteen,  n.\")) print NR-1}' KLN_1966.txt; sed -n 29763,29766p KLN_1966.txt; grep -n -i '^vest,\\|^invest,\\|^divest,\\|^wear,' KLN_1966.txt | cut -c1-400"
}
```


### [2026-10-17T00:05:20.678Z] TOOL RESULT

```
652
posteen,  n.,  an  Afghan  leathern  pelisse  (Anglo- Indian).  —  Pers.  postin,  ‘of  leather’,  fr.  post, ‘hide,  leather’,  which  is  rel.  to  Pehlevi  post, Avestic  pqsto,  of  s.m.
poster,  n.,  bill,  placard.  —  Formed  fr.  post,  ‘pil¬ lar’,  with  suff.  -er.
poste  restante,  1)  a  direction  on  mail  asking  that it  be  held  at  the  post  office  until  called  for;  2)  a post-office  department  in  charge  of  such  mail.
—  F.,  ‘remaining  post’.  For  the  first  word  see 3rd  post.  F.  restante  is  fem.  of  restant,  pres.  part, of  rester,  ‘to  remain’ ;  see  rest,  ‘to  remain’.
```


## [2026-10-17T00:05:26.796Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^wear,\\|^vest,\\|^invest,\\|^divest,\\|wear,  tr' KLN_1966.txt | cut -c1-500 | head; grep -n '^wes-\\|^wes ' AHD_watkins1985.txt | head; grep -n -i '^wear\\b\\|^vest\\b' SKT.txt | head -4"
}
```


### [2026-10-17T00:05:27.134Z] TOOL RESULT

```
15216:Derivatives:  forsaken-ly,  adv.,  forsaken-ness,  n. forsook,  past  tense  of  forsake.  —  OE.  forsoc, past  tense  of  forsacan.  See  forsake, forsooth,  adv.  —  ME.  for  soth,  fr.  OE.  forsod, ‘for  a  truth’.  See  for  and  sooth, forspent,  adj.,  exhausted.  —  Pp.  of  obsol.  for¬ spend,  fr.  ME.  forspenden,  fr.  OE.  forspendan, ‘to  squander’.  See  for-  and  spend, forswear,  tr.  and  intr.  v.  —  ME.  forswerien,  fr. OE.  forswerian,  ‘to  renounce,  forswear;  
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
1157:wes-!
1159:wes-1. To buy. 1. Suffixed form *wes-no- in Latin vénum, sale: VENAL, VEND. 2. Suffixed o-grade form *wos-nd- in Greek dneisthai, to buy: DUOPSONY. [Pok. 8. wes- 1173.]
1160:wes-?. Wet. Germanic *wdés- in Old English wés, juice: 00ZE}. [Pok. 3. wes- 1171.]
1161:wes-3. To stay, dwell, pass the night, with derivatives meaning “to be.” 1.O-grade form *wos- in Germanic *was- in Old English wes, was: was. 2. Length- ened-grade form *wés- in Germanic *wéz- in Old English wére (subjunctive), w#ron (plural), were: WERE. 3. Ger- manic *wesan in Old Norse vesa, vera, to be: WASSAIL. 4. Suffixed form *wes-td- perhaps in Latin Vesta, house- hold goddess: Vesta. 5. Suffixed variant form *was-tu- possibly in Greek astu, town (< “place where one dwells”), whence Latin astus, skill, craft (practiced in a town): ASTUTE. [Pok. 1. wes- 1170.]
1162:wes-‘. To clothe. Extension of eu-'. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear, carry: WEAR}, 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY. 3. Suffixed form *wes-nu- in Greek hennunai, to clothe: HIMATION. [Pok. 5. wes- 1172.]
1163:wes-pero-. Evening, night. I. Reduced form “wes-. 1. Suffixed form *wes-to- in Germanic *west- in: a. Old English west, west: WEST; b. Old English westerne, western: WESTERN; C. Old English westra, more west- erly: WESTERLY. 2. Possibly Germanic *wis- in Late Latin Visigothi, “West Goths” (Gothi, the Goths): Vist- GorTu. II. Basic form *wespero-. 1. Latin vesper, evening: VESPER, VESPERTILIONID. 2. Greek hesperos, evening: HESPERIAN. [Pok. wesperos 1173.]
21258:WEAR.
21260:Wear  (i),  to  wear  clothes,  to  consume by  a*t  (E.)  M.  E.  wtrtn,  pt.  t.  wtrtd. A.  S.  Wtrian  (pt.  t.  werode).^\ct\.  verja, O.  H.  G.  werian,  to  wear ;  Goth,  warjan, to  clothe.  (^WAS,  to  clothe.)  ^All the  senses  of  wear  can  be  deduced  from the  senfcc  of  carrying  clothes  on  the  body; hence  it  means  to  consume  or  use  up  by wear,  to  dcsiroy,  efface.  The  pt.  t.  vfore  \% modem.  Not  allicfl  to  A.  S.  werian,  to defend,  which  is  a  difTerent  word. Wear  (a)  a  weir ;  see  weir,  under  Wary. Wear  (3),  to  veer  a  ship ;  the  same  as V«er,  q.  v.
```


## [2026-10-17T00:05:30.944Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==316 || NR==317 || NR==318' WLD_Bd1_pages.txt | grep -n -i -B2 -A6 'vastra\\|västra\\|Futter\\|Weide\\|kleid' | head -60"
}
```


### [2026-10-17T00:05:31.489Z] TOOL RESULT

```
82-
83- 2.    ues- „schmausen   ;   aufgeraumt sein‘‘.
84:      Ai. annvduase ..hat aufgezehrL,                vdstrh ,.vor   dem   Fresscn”. av. vastra
85:    ,.Fresse, Maul“ (vgl. Wolff, KZ. 40, 20. Zu av. vastra ..Futter", radar-
86-    „Hirte“ s. Bartholomae, Airan. Wb. 1413. Geldner KZ. 27, 216, 260). Lber
87-    lat. vvseor „als Speise genietien, sich nahren" vgl. *ed- und Yf. LEWb. 2
88-
89-        Walde, Etymologisches Worterbuch
90-                                      I.                            21
91-
--
196-                                                                                                 1
197-
198:5.   ues- „kleiden“ (Erw. von *eu- „anziehen“, s. d. m. Lit.                                     ).
199-
200-
201:     Ai. vciste „kleidet sich, zieht an“, av. vaste ds. (vgl. das unthemat. gr. eoaat,
202--karai), v'mhaiti ds. ; ai. vasana-, av. vcmhana- n.  ,,Gewand“; ai. vasman- n.
203:„Decke“ (= riua ) vastra-, av. vnstm- n. „Kleidung“ (: gr. feoxga, mhd. wester )
204-                                   ;
205-
206-
207-arm. z-genum „ziehe micli an“ (*ues-mt-                             —
208:                                            tvvvfii), s-gest „Kleidung“ (-Z«-St.
209-Hubschmann Arm. St. I 30, Arm. Gr. I 446); gr. 'dvvvfu. jon. ti'vv/u, aor.
210:'da{a)a „kleiden“, med. „sich kleiden“, unthemat. 2 sg. Horn, taaai, 3 sg.
211:Hdt. im-EOTcu; ’dados n. „Kleidung“ {-dhes- St., s. Brugmann II 2 1, 527),
212-eodgs -fjros ds. (*y Ea|ro-]r«T~? mit dem d von ’dados Schwyzer IF. 30,
213-         ,                                                                               ;
214-
215-
216-443, Kretschmer Gl. 6, 306’; eavos „weiblicbes Gewand                                    -
217-                                                                                             '   (iiber das in Bed.
--
219-(Hes.        yi)(xa' 1/j.a.Tiov,          yeu/uaxa   •
220-                                                         ijidna), ev-, xaxo-, Sva-ei/ucov ,.gut, scblecht
221:gekleidet", itazistisch   Boisacq 375 m. Lit.) i/aanov „Kleid, Mantel" dor.
222-                                           (s.                                                                       ;
223-
224-
225-j-saxga (yeaxga- axoh) Hes. s. o.), erpEoxotg „warmeres Wintergewand, Sol-
226-                                                 ;
227-
--
239-
240-eidos ifxaxiov Hes. nach Fick aaO. mit idg. o? im Nacliton?).
241:   Alb. ves „ich kleide an“, visem „kleide mich an“ (G. Meyer BB. S, 191,
242:Alb. Wb. 467); lat. vestis „Kleidung“, vestio, -ire „kleiden“ (vgl. yeaxla                                                 •
243-
244-
245-
246-
247:evdvaig Hes.) got. wasjan, ahd. werian, anord. veria „kleiden“, ags. werian
248-                      ;
249-
250-
251:„ds., Kleider tragen“; got. ivasti f. „Kleid“; mhd. wester (s. o.) „Taufkleid“;
252:anord. vest n. „Kleid“ ' *wesnla -), ver „Uberzug“ (*waza-).
253-   Schroder Abl. 49 f. will in ndl. jas „Uberrock“, mnd. jesse „\Vams,
254-Jacke“ und in ndl. jurlc, ostfries. jurk, jiirk, westf. jiirken „Kinderkittel“
```


## [2026-10-17T00:05:37.027Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'v[aā]str\\|vāstr\\|västr' NYB_vol2_glossary.txt | cut -c1-300 | head; grep -n -i 'vāstr\\|wāstr\\|vāstar\\|wāstar\\|bahān\\|wihān\\|bānūk\\|bānūg\\|pōst' SNS.txt SNS_pages.txt | cut -c1-200 | head -20"
}
```


## [2026-10-17T00:05:38.517Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'vastar\\|vastr\\|post\\b\\|pos[tf]' SNS_pages.txt | cut -c1-200 | head -20; grep -n -i 'vāstar\\|vāstry\\|bahān\\|bāmī\\|pōst\\|vastr' CHEUNG.txt | head -5"
}
```


### [2026-10-17T00:05:38.879Z] TOOL RESULT

```
4659:                                              xvastar: V#*y
5982:                                                                                                                                            *=*.* :pOst:   yiwjt,
7314:  .JUL: postpone, neglect. (<JW) spSzed:                                                                                                                          .^.L:s5yag: *-*-*OJ              
10293:                                                                                                                                           ^   «*lfflj>:vastr:       \«***»l             (
10299:                                                                                                                       T1/1T^ .(4tf/b.     1385) 2 vastra-           :   km
10303:                                                                                            wastryOsan             :      Jf^f Vastravaxsan:            «ou-«\***»i
10309:                                                                                                                        •JjJ-*«ui*f>Uj rvastryOs:          -*^ **«*•»•<
10310:                                                                                                          A*/Y*S -MiM,.          1416)vastrye5fsuya- :*.                            ,„
15772:                                                              vastrySs 260/9            vanand star 284/15
15900:pOst 138/20                ramisnlgtar 223/19                rasisnlh 234/9         rOd 229/12
15901:pOstSn 139/3               ram xvabar xv ad3y 223/9          rasn 227/5             rCkun!g/rOknIg(?) 231/
16307:dandSn fris post 339/19     deh/dih 242/10               dist 313/11                drustih 339/12
```


### [2026-10-17T00:05:38.889Z] TOOL RESULT

```
4013:vāstriyoš
4018:vastarg [wstlg] clothes 41?-4-? [472° read vistarg]. — Av. (1385) vastra- ‘clothing’ ; inser. SM 1. 50 wstlg; Paz. vastarg, vastrg ; Mand. lw. bastirga.
4019:vastr [w’stl] pasture, (cattle) food 9411-14, — Borrowed from Av. (1414) västra-.
4020:vüstriyo$ [w'stlywš] cattle-breeder, pl. cas. obl. —-än, the third class of the Sassanian society 2°. 814-14. — Borrowed from Av. (1028, 1416) vastryo.jšuyant-.
4022:västriyöseh
4025:västriyöseh coll. the class of cattle-
5424:varšni-: gušn vastra-: vastarg vastra-: vastr
5426:vaströ.fSuyant-: vastri- yoš
```


## [2026-10-17T00:05:42.857Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in واستریوش واستر بهانه بانو پوست بام; do u=\"https://vajehyab.com/moein/$w\"; echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 551, Mo'in entry $w\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:05:45.387Z] TOOL RESULT

```
== https://vajehyab.com/moein/واستریوش
/home/sfmqrb/git/rishe-private/data/verification/sources/web/338baf3a1379af91.txt
== https://vajehyab.com/moein/واستر
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b5b466f5285aacb8.txt
== https://vajehyab.com/moein/بهانه
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fee91080e3e4e7c4.txt
== https://vajehyab.com/moein/بانو
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e96974ebaabc4ebf.txt
== https://vajehyab.com/moein/پوست
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f17555598d7ab69a.txt
== https://vajehyab.com/moein/بام
/home/sfmqrb/git/rishe-private/data/verification/sources/web/51bf9b5fbd2d67f1.txt
```


## [2026-10-17T00:05:47.816Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 338baf3a1379af91 b5b466f5285aacb8 fee91080e3e4e7c4 e96974ebaabc4ebf f17555598d7ab69a 51bf9b5fbd2d67f1; do echo \"=== $f $(wc -c <$f.txt)\"; grep -n -i 'معین' -A3 $f.txt | grep -v '^\\S*-\\s*$' | head -8 | cut -c1-300; done"
}
```


### [2026-10-17T00:05:48.186Z] TOOL RESULT

```
=== 338baf3a1379af91 1022
4:TITLE: معنی واستریوش | فرهنگ انتشارات معین | واژه یاب
6:معنی واستریوش | فرهنگ انتشارات معین | واژه یاب 
8- 26 فرهنگ 
16: فرهنگ انتشارات معین
17- (تَ) [ په . ] (اِ.) کشاورز و آن یکی از طبقات چهارگانة عهد ساسانی به شمار می رفته . ج . واستریوشان .
18- واستریوش در فرهنگ‌های دیگر
19- معنی واستریوش در لغت‌نامه دهخدا 
=== b5b466f5285aacb8 132
=== fee91080e3e4e7c4 1403
4:TITLE: معنی بهانه | فرهنگ انتشارات معین | واژه یاب
6:معنی بهانه | فرهنگ انتشارات معین | واژه یاب 
8- 26 فرهنگ 
16: فرهنگ انتشارات معین
17- (بَ نِ) [ په . ] ( اِ.) 1 - عذر نابجا. 2 - بازخواست . 3 - سبب ، باعث .
18- بهانه در فرهنگ‌های دیگر
19- معنی بهانه در لغت‌نامه دهخدا 
=== e96974ebaabc4ebf 1075
4:TITLE: معنی بانو | فرهنگ انتشارات معین | واژه یاب
6:معنی بانو | فرهنگ انتشارات معین | واژه یاب 
8- 26 فرهنگ 
16: فرهنگ انتشارات معین
17- [ په . ] ( اِ.) خانم .
18- بانو در فرهنگ‌های دیگر
19- معنی بانو در لغت‌نامه دهخدا 
=== f17555598d7ab69a 1724
4:TITLE: معنی پوست | فرهنگ انتشارات معین | واژه یاب
6:معنی پوست | فرهنگ انتشارات معین | واژه یاب 
8- 26 فرهنگ 
16: فرهنگ انتشارات معین
17- (اِ.)1 - بیرونی ترین بخش بدن جانوران . 2 - پوشش بیرونی ساقه . 3 - پوشش تخم جانور و دانة گیاه . ؛ ~ کسی کنده شدن (کن .) متحمل عذاب شدید شدن .
18- پوست در فرهنگ‌های دیگر
19- معنی پوست در لغت‌نامه دهخدا 
=== 51bf9b5fbd2d67f1 1357
4:TITLE: معنی بام | فرهنگ انتشارات معین | واژه یاب
6:معنی بام | فرهنگ انتشارات معین | واژه یاب 
8- 26 فرهنگ 
16: فرهنگ انتشارات معین
17- ( اِ.) صبح ، پگاه .
18- بام در فرهنگ‌های دیگر
19- معنی بام در لغت‌نامه دهخدا
```


## [2026-10-17T00:05:57.752Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^21[89] \\|^OLD PERSIAN 21\\|^LEXICON 21\\| 219$' KNT_full.txt | head; grep -n -i \"vah- vb\\|vahana\\|vastra\" KNT_full.txt | head"
}
```


### [2026-10-17T00:05:58.154Z] TOOL RESULT

```
29617:LEXICON 213 
7163:-daha, naham, атуйћа bagaha, dvahanam, Giira- 
8537:‘town’; dvahanam ‘village’; didà ‘fortress’; kaufa 
14348:‘fortress, stronghold’, vardanam ‘town’, dvahanam 
17145:33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 
20010:46 & : kartā : Abirádus : nàma : àvahanam : Ujaiy 
22911:dvahana-, and in the second parts of compounds 
24118:dvahana- sb. ‘village’ (5166): deriv. (8147.1) 
24120:‘being’. dvahanam DB 2.33; DSf 46. 
28911:vah- vb. ‘dwell’, see àvahana-. 
29029:IT, ТУ), ‘Conqueror, Winner’ (hardly *vivahana-,
```


## [2026-10-17T00:06:03.517Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^wes[ō]*\\b\\|^wesō\\|^westis\\|^wes-' IEC.txt | head; grep -n -i 'vastra' IEC.txt SYN.txt | head -8 | cut -c1-250"
}
```


### [2026-10-17T00:06:03.862Z] TOOL RESULT

```
SYN.txt:4014:Av. vastrya-, deriv. of vastra- fodder’ and ‘pasture’ (cf. also vastar- ‘herds- man’), this prob. : Skt. vas- ‘consume’ (rare), OE wist, ‘food’, etc. (5.12). Walde-P. 1.306 ff. Connection with OHG weida (Barth. 1413) is to be re- jected 
SYN.txt:4021:Goth. winja ae ae Booxy ON hagi ; Lett. ganiba, ganikla Lat.  pascuum Dan. gresningsland, gres- ChSl. pazitt It. pascolo gang SCr.  paia — Fy. pature Sw. bete, betesmark Boh. pastuiské Sp. apacentedero OE l@swe Pol. pastwisko Rum. pédsu
SYN.txt:9836:Grk. — éoOis, etpara, tnaria Goth. wasljés Lith. drabuzis, drapanos NG potxa, évdtpara, dope ON kladi, biningr, fot rubat para Dan. klader Lett. drébes Lat. vestis, vestilus, vesti- Sw. klader, klidning ChSl.  odezZda, riza mentum OE cli
SYN.txt:9851:ment’, pl. ‘clothing’; Skt. vdsas-, vasana-, Ay, vanhana- (cf. Hom. éavés ‘robe, gar- ment’, fr, *¢écavos), Skt., Av. vastra-, all sg, ‘garment’, pl. ‘clothes’; Toch. A wsdl (6886, 471).
SYN.txt:9898:8. Skt. vasana-, Av. vavhana-, Skt., Ay. vastra-, above, 1.
SYN.txt:9980:vastra- ‘clothing’
SYN.txt:11605:tienda, pabellén NE tent Russ. palatka, Sater . cort, salrd Du. tent Skt. vastragrha-
SYN.txt:11638:7. Skt. vastragrha- (rare), lit. ‘cloth- house’, epd. of vastra- ‘cloth, dress’ and grha- ‘house’.
```


## [2026-10-17T00:06:05.709Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4008,4016p SYN.txt | cut -c1-600; sed -n 9845,9852p SYN.txt | cut -c1-500; grep -n -i 'farmer\\|husbandman\\|PASTURE' SYN.txt | head -5 | cut -c1-120"
}
```


### [2026-10-17T00:06:06.090Z] TOOL RESULT

```
Digitized by Arya Samaj Foundation Chennai and eGangotri
ANIMALS 147
ture’ fr. ‘hunting ground’ or ‘place for seeking fodder’ or both.
5. Lith. ganyti (a), refl. ganytis (b), Lett. ganit (a), refl. ganities (b), deriv. of Lith. genu, ginti, Lett. dztt ‘drive’ : ChSI. Zena, giinati, gong, goniti ‘drive’, Skt. han-, Grk. Oetvw ‘strike’, etc., Ii *gvhen-. Walde-P. 1.679 ff. Develop- ment from ‘strike’ to ‘drive’, then ‘drive cattle’, ‘tend cattle’. Cf. VLat. minare ‘drive cattle’ fr. mindrz ‘threaten’, and the specialization in NE drover.
6. ChSl. pasq, pasti (a), pres. pass. pple. pasomi ‘grazing’ (b): Lat. pds- cere, above, 2. SCr. pasti (a, b), Boh. pdsti (a), pdsti se (b) and similarly in the other Slavic languages.
7. Skt. car- ‘move about, wander’, also ‘graze’ (b, caus. a) : Grk. wé\w ‘be in motion’, Lat. colere ‘cultivate’, etc. IE *kvel-. Cf. NPers. éaridan ‘pasture’. Walde-P. 1.514 ff.
Av. vastrya-, deriv. of vastra- fodder’ and ‘pasture’ (cf. also vastar- ‘herds- man’), this prob. : Skt. vas- ‘consume’ (rare), OE wist, ‘food’, etc. (5.12). Walde-P. 1.306 ff. Connection with OHG weida (Barth. 1413) is to be re- jected on both formal and semantic grounds, since it takes no account of the history of weida (above, 4).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
} \ | i 1 a : ' |
rabds, SE: coll., pe : -rar-, with @ Ir. tin pan ike adjj-00s, 0, 443, Buck, Cl.Ph. . Enya, Cret. _ pAve. coll. ‘cloth-
mre ite a, id " plsewhere mids
' Ion. «fuarvor, sg. : Sioa pl. ‘clothes’, fr. elua; oe (> It. veste, etc.), hence v
b. vestire) vestitus, vestimen- lito, Sp. vestido; Fr. véte- ment’ or coll., pl. ‘clothes’) ; ‘sarment, clothing’, pl.
formerly
placed by oF after Fr. vélement) ; Goth. wasti ‘gar-
ment’, pl. ‘clothing’; Skt. vdsas-, vasana-, Ay, vanhana- (cf. Hom. éavés ‘robe, gar- ment’, fr, *¢écavos), Skt., Av. vastra-, all sg, ‘garment’, pl. ‘clothes’; Toch. A wsdl (6886, 471).
2. Grk. &dtua ‘garment’, NG id., also sg. coll. or pl. ‘clothes’, fr. éébw ‘clothe’ (6.11).
1499:Words for ‘woods’ are mostly from notions that were adventitiously asso- ciated, such as (wooded) ‘mountain’, (woo
1504:MLat. boscus (>It. bosco, Fr. bois, Sp. bosque) was used esp., like Lat. saltus, for ‘woodland pasture’ (cf. unusqu
1508:land in the forest’, etc.; cf. Du Cange s.V. agistare). It is now taken by many as a loanword fr. Gmc. (OHG busc, N
1524:Sw. vall ‘pasture’, etym. much disputed, but best taken as orig. ‘wildland’ : Goth. wilpeis, OE wilde ‘wild’. Walde
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (G
```


## [2026-10-17T00:06:28.675Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg551.png data/verification/sources/refs/ocr/BOOK/551.png; cp /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt427-551-foot.png data/verification/sources/refs/ocr/BQT/427.png; python3 tools/fetch_source.py 'https://archive.org/details/borhan-ghate-v1/page/n653' --note 'page 551, BQT p.427 s.v. پوست footnote 8' | tail -1"
}
```


### [2026-10-17T00:06:29.993Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/f24c0533f375d6e8.txt
```


## [2026-10-17T00:06:30.717Z] AGENT

Now I'll write the verification file.


## [2026-10-17T00:09:13.772Z] TOOL CALL #70: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-551.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE_WES = W + \"Reconstruction:Proto-Indo-European/wes-\"\nBOOKPNG = \"data/verification/sources/refs/ocr/BOOK/551.png\"\n\nPOK1172 = {\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt l.92477ff 'Root / lemma: ues-5 (*h2ues-5) Meaning: to dress, put on ... Old Indic vaste 'kleidet sich, zieht an', Avestan vaste ds. ..., vaŋhaiti ds. [OCR 'varjhaiti 6s.']; Old Indic vasana-, Avestan vaŋhana- n. 'garment'; Old Indic vasman- n. 'cover'; vastra-, Avestan vastra- n. 'clothing' ... Latin vestis ... Gothic wasjan, Old English werian' (Page(s): 1172-1173).\"}\nWLD309 = {\"src\": \"WLD\", \"where\": \"Bd. I p. 309 (WLD_Bd1_pages.txt leaf 318)\", \"stance\": \"supports\", \"note\": \"'5. ues- „kleiden“ (Erw. von *eu- „anziehen“) ... Ai. vaste „kleidet sich, zieht an“, av. vaste ds., vaŋhaiti ds.; ai. vasana-, av. vaŋhana- n. „Gewand“; ai. vasman- n. „Decke“; vastra-, av. vastra- n. „Kleidung“ ... lat. vestis ... got. wasjan, ahd. werian, ags. werian'.\"}\nAHD_WES4 = {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. wes-4 (AHD_watkins1985.txt l.1162)\", \"stance\": \"supports\", \"note\": \"'wes-4. To clothe. Extension of eu-1. 1. Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear ... 2. Suffixed form *wes-ti- in Latin vestis, garment: VEST; DEVEST, INVEST ... [Pok. 5. wes- 1172.]'\"}\nSYN_CLOTH = {\"src\": \"SYN\", \"where\": \"6.12 CLOTHING (SYN.txt l.9851)\", \"stance\": \"supports\", \"note\": \"'Skt. vásas-, vasana-, Av. vaŋhana- (cf. Hom. heanós), Skt., Av. vastra-, all sg. garment, pl. clothes'.\"}\nHRN175 = {\"src\": \"HRN\", \"where\": \"no. 174-175, 178 (p. 40-41)\", \"stance\": \"partial\", \"note\": \"'174. bām 1) Haus s. bān (No. 175) ... bām wird secundär für bān stehen'; '175. bān Haus; vergl. bānū (No. 178); phlv. bān Dach'; '178. bānū Herrin, wörtl. Hausherrin (vergl. bān)'. Horn links bām/bān and bānū but gives no Old Iranian source for bān.\"}\nHUB25 = {\"src\": \"HUB\", \"where\": \"p. 25, notes to Horn nos. 175, 178 (HUB.txt leaf 35)\", \"stance\": \"contradicts\", \"note\": \"'Ich halte daher auch Andreas' Etymologie: bān Haus = ap. vahana- (vgl. skr. vasana- Wohnen) nicht für richtig, zumal im Pehl. bān, aber nirgends *vān bezeugt ist ... 178. Ich bezweifle die Zugehörigkeit von bānū Herrin zu bān = bām Dach, Haus'.\"}\nHUB32 = {\"src\": \"HUB\", \"where\": \"p. 32, no. 244 (HUB.txt leaf 42)\", \"stance\": \"supports\", \"note\": \"'Np. bahāna Vorwand ... Das Wort geht über paz. vahāna = vahān cause Shk. 270 = phl. vahānak auf ap. *vahāna- zurück, das ich mit Fr. Müller zu skr. vasana- Gewand stelle. Der Begriffsübergang: Kleid—Hülle—Vorwand macht doch keine Schwierigkeit' (also §105: 'bahāna Vorwand, skr. vasana- Gewand').\"}\nPHD_WIHAN = {\"src\": \"PHD\", \"where\": \"s.v. wihān(ag) (PHD_mackenzie.txt l.5372)\", \"stance\": \"partial\", \"note\": \"'wihān(ag) [wh'n(k)' | M wh'ng, N bahāna] cause, reason.' MacKenzie reads the Pahlavi word with wi-, not vah-; he gives no etymology.\"}\nNYB_SILENT = {\"src\": \"NYB\", \"where\": \"Glossary (grep vihān/vahān/wihān)\", \"stance\": \"silent\", \"note\": \"no entry for vihānak/vahānak in the OCR of NYB vol. 2.\"}\nARY_SILENT = {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grep of the Persian headword and of the Latin transliteration found no entry (Persian OCR of ARY is poor); not located.\"}\nBRT_VAH = {\"src\": \"BRT\", \"where\": \"col. 1348-1349 s.v. vaŋhana-; col. 1386-1387 s.v. vastra-; col. 1394 s.v. vah-\", \"stance\": \"supports\", \"note\": \"BRT.txt l.22481 'vaŋhana- n. Kleidung, Gewand: kamərəδəm vaste vaŋhanəm'; l.23152 'vastra- n. Kleid, Gewand, Kleidungsstück'; l.23299 'vah- V. sich kleiden in — Praes. 1 vah-, 2 vaŋha- ... spaēta vastrā vaŋhaiti ... vaste'.\"}\nBRT_PASTA = {\"src\": \"BRT\", \"where\": \"col. 903-904 s.v. pəsta-, pəstō.fraθaŋhəm (BRT.txt l.16333-16340)\", \"stance\": \"partial\", \"note\": \"'pəsta- m. Haut, bes. die behaarte des Menschen ... Et.? — mp. (Pü.), np. pōst. Aber woher ō?'; 'pəstō.fraθaŋhəm Adv. in der Breite der (behaarten) Haut sva. soweit die (behaarte) Haut (des Kopfes) geht ... Pü. pōst pahnāk'. Bartholomae links NP pōst but leaves the etymology open.\"}\nHRN338 = {\"src\": \"HRN\", \"where\": \"no. 338 (p. 72)\", \"stance\": \"supports\", \"note\": \"'338. pōst Fell, Haut, pōstīn, aw. pəstō.fraθah-; phlv. pōst, pōstīn. LW. kurd. pōst, pīst; bal. pōst; afγ. pōst; wax. pīst, sar. past'.\"}\nKLN_POSTEEN = {\"src\": \"KLN\", \"where\": \"s.v. posteen (KLN_1966.txt l.29763, leaf 652)\", \"stance\": \"supports\", \"note\": \"'posteen ... Pers. postin, of leather, fr. post, hide, leather, which is rel. to Pehlevi post, Avestic pąsto, of s.m.'\"}\nSOD8228 = {\"src\": \"SOD\", \"where\": \"entries 8228, 8230 (SOD.txt l.63329-63349; leaf 398 ≈ p. 332)\", \"stance\": \"supports\", \"note\": \"'8228 pwst'k B, S poste (pwsty, pwst'y, pwstk) < OP pavasta-, Parth. pwstg, Skt. pustaka ... book, Sutra, document, writing, parchment'; '8230 pwst(h) S post skin, leather'.\"}\nBQT427_C = {\"src\": \"BQT\", \"where\": \"p. 427 s.v. پوست, Mo'in's note 8 (archive.org borhan-ghate-v1 leaf n653; saved in ocr/BQT/427.vision.txt)\", \"stance\": \"supports\", \"note\": \"'پهلوی pôst «نیبرگ ۱۸۶»، «تاوادیا ۱۶۴»، اوستا pasta «بارتولمه ۹۰۴»، کردی pîst، pôst، افغانی pôst ... «اشتق ۳۳۸»'; note 9: 'پهلوی pôstîn ... pôstên'.\"}\nNYB_POST = {\"src\": \"NYB\", \"where\": \"Glossary s.v. pōstiyān (NYB_vol2_glossary.txt l.3166)\", \"stance\": \"supports\", \"note\": \"'pōstiyān [pwsty'n'] leather ... Derived from pōst: NP pōstiyān a kind of leather'.\"}\nSNS_POST = {\"src\": \"SNS\", \"where\": \"index 'pōst 138/20, pōstēn 139/3' (SNS_pages.txt l.15900-15901)\", \"stance\": \"supports\", \"note\": \"Tavoosi's glossary lists pōst at p. 138 l. 20 and pōstēn at p. 139, i.e. Nourai's SNS:139.\"}\n\nentries = []\n\n# ---------------- entry 0 ----------------\ne0_nodes = [\n {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"vastra 1, vasta 1; vaste, vašaiti, aothra, vah, vahna, vanhna\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\", \"book_prints\": \"vašaiti\", \"correct_form\": \"vaŋhaiti\",\n  \"derivation\": \"Avestan has the verb root vah- 'to clothe oneself, wear', with a present stem vaŋha- (3sg. vaŋhaiti, < Proto-Iranian *wahati, *s > h, -ah- > -aŋh-) and the athematic middle vaste 'he clothes himself' (= Skt. vaste < PIE *wes-to). From it come vastra- n. 'garment' (< *wes-tro-m, = Skt. vastra-) and vaŋhana- n. 'clothing' (= Skt. vasana-). These are correct. The book prints 'vašaiti', which is not an Avestan form of this root; it is Nourai's misprint for vaŋhaiti (Pokorny and Bartholomae give vaŋhaiti). 'vahna, vanhna' are loose spellings of vaŋhana-, and 'vasta 1' is not attested as a noun (it is the bare stem of vaste). aoθra- 'shoe' comes from the base root *h3ewh1- / *eu- 'to put on' (Lat. induō, exuō). Watkins and Walde-Pokorny call *wes- an extension of that root, which is why Nourai heads the chart 'Wes 3, Ew-es, Eu-es'. Strictly, aoθra- is a cognate of *wes-, not a derivative of it. The printed page agrees with the JSON, so the error is the book's.\",\n  \"derivation_fa\": \"در اوستایی ریشهٔ vah- «پوشیدن، بر تن کردن» با ستاک vaŋha- (سوم‌شخص vaŋhaiti) و صورت میانهٔ vaste «می‌پوشد» آمده است. از همین ریشه vastra- «جامه» (برابر سنسکریت vastra-) و vaŋhana- «پوشاک» (برابر سنسکریت vasana-) ساخته شده‌اند. s هندوایرانی در ایرانی به h بدل شده است. صورت «vašaiti» که در کتاب چاپ شده خطای چاپی کتاب به جای vaŋhaiti است، و «vahna, vanhna» نگارش ساده‌شدهٔ vaŋhana- است. aoθra- «کفش» از ریشهٔ پایه‌ای *eu- «پوشیدن» است که wes- گسترش‌یافتهٔ آن به شمار می‌رود؛ پس این واژه هم‌ریشه است، نه برآمده از wes-. بارتولومه و پوکورنی اصل مطلب را تأیید می‌کنند.\",\n  \"sources\": [PIE_WES, W + \"𐬬𐬀𐬯𐬙𐬭𐬀\", W + \"𐬀𐬊𐬚𐬭𐬀\"],\n  \"ref_check\": [POK1172,\n    {\"ref\": \"KNT:219\", \"status\": \"not_found\", \"note\": \"Kent's lexicon (KNT_full.txt, 1950 ed.) ends c. p. 215 and has no p. 219 entry for this root; the only OP form is vah- vb. 'dwell' (l.28911 'vah- vb. dwell, see āvahana-'), a different root (*h2wes- 'dwell').\"}],\n  \"consulted\": [BRT_VAH, WLD309, SYN_CLOTH]},\n {\"id\": 2, \"lang\": \"Persian\", \"words\": \"bâm 2; bânŭ\", \"verdict\": \"plausible\",\n  \"derivation\": \"NP bām / bān 'roof, house' continues MP bān 'roof' (Horn: phlv. bān 'Dach'). Wiktionary derives it from PIE *wes- 'to clothe' via a 'covering' noun and compares Av. vaŋhana- 'cover'. The final -m of bām is a secondary variant of -n (Horn no. 174), and the word is distinct from bām 'dawn' (< *bʰeh2- 'shine'). The link to *wes- requires initial w- > b-, which is regular in Persian (cf. bahār, bahā). It is still a hypothesis: Hübschmann (p. 25) objects that MP has only bān and never *wān. The older proposal (Andreas) derived bān from OP *vahana- 'dwelling', i.e. *h2wes- 'to dwell', not 'to clothe'. For bānū 'lady' (MP bānūg), Horn's analysis 'mistress of the house' (bān + -ūg) is possible but unproven. Hübschmann doubts it, which is the dispute recorded in the chart's NOTE, and Wiktionary leaves the origin open (OP *bānūka-). So the bām/bān part is plausible and the bānū part is uncertain.\",\n  \"derivation_fa\": \"«بام/بان» به معنی «سقف، خانه» از فارسی میانهٔ bān «سقف» است و ویکی‌واژه آن را به ریشهٔ هندواروپایی *wes- «پوشاندن» می‌رساند و با اوستایی vaŋhana- «پوشش» می‌سنجد. w آغازی در فارسی به b بدل شده است، چنان‌که در «بهار» و «بها». م پایانی «بام» به گفتهٔ هرن جانشین ن است، و این واژه با «بام» به معنی «بامداد» یکی نیست. هوبشمان این ریشه‌شناسی را نمی‌پذیرد و پیوند «بانو» (پهلوی bānūg) با «بان» را نیز مشکوک می‌داند. پس ادعای نورایی برای «بام» با احتیاط پذیرفتنی است و برای «بانو» ثابت نشده است.\",\n  \"sources\": [W + \"بام\", W + \"بانو\", \"https://vajehyab.com/moein/بانو\", \"https://vajehyab.com/moein/بام\"],\n  \"ref_check\": [{\"ref\": \"AEF:230\", \"status\": \"not_checked\", \"note\": \"AEF (Khaleqi Motlaq's Persian translation of Horn) is not on disk. The corresponding Horn entries (nos. 174-175, 178) were read in HRN instead; see consulted.\"}],\n  \"consulted\": [HRN175, HUB25,\n    {\"src\": \"MON\", \"where\": \"vajehyab Mo'in s.v. بانو, بام\", \"stance\": \"partial\", \"note\": \"'بانو [په.] (اِ.) خانم'. Mo'in tags bānū as Pahlavi but gives no etymology; s.v. بام only the sense 'صبح، پگاه' is shown online.\"},\n    {\"src\": \"PHD\", \"where\": \"p. 15 s.v. bānūg (PHD.txt l.252)\", \"stance\": \"silent\", \"note\": \"'bānūg [b'nwk' | N bānū] lady' — no etymology given.\"},\n    ARY_SILENT]},\n {\"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"vasman, vasana\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Skt. vásman- n. 'covering' < *wés-mn̥ (= Gk. heîma 'garment') and vásana- n. 'garment, cover' < *wés-no- (= Av. vaŋhana-, Gk. heanós) are both nominal derivatives of the Vedic verb vas- 'to clothe' (vaste). Pokorny, Walde-Pokorny and Wiktionary all list them under *wes- 'to clothe'.\",\n  \"derivation_fa\": \"سنسکریت vásman- «پوشش» و vásana- «جامه، پوشش» از فعل vas- «پوشیدن» ساخته شده‌اند و برابر اوستایی vaŋhana- و یونانی heîma هستند. پوکورنی و ویکی‌واژه هر دو را زیر ریشهٔ *wes- «پوشیدن» آورده‌اند. ادعای نورایی درست است.\",\n  \"sources\": [PIE_WES, W + \"वस्मन्\", W + \"वसन\"],\n  \"ref_check\": [{\"ref\": \"POK:1172\", \"status\": \"supports\", \"note\": \"POK_full.txt l.92480 'Old Indic vasana-, Avestan vaŋhana- n. garment; Old Indic vasman- n. cover (= heîma)'.\"}],\n  \"consulted\": [WLD309, SYN_CLOTH]},\n {\"id\": 4, \"lang\": \"Old Persian\", \"words\": \"vahâna\", \"verdict\": \"plausible\",\n  \"derivation\": \"No OP *vahāna- 'cover' is attested. OP has only āvahana- 'village', from vah- 'to dwell' (a different root, *h2wes-). The form is Hübschmann's reconstruction (*vahāna-, starred, Persische Studien p. 32), set up to explain Pazand vahān and Pahlavi vahānak. He compared it with Skt. vasana- 'garment', so it would be a derivative of Iranian vah- 'to clothe' with the suffix -āna-. Nourai presents a hypothetical form as attested Old Persian.\",\n  \"derivation_fa\": \"واژهٔ vahāna- «پوشش» در کتیبه‌های پارسی باستان گواهی نشده است. در پارسی باستان تنها āvahana- «ده، آبادی» هست که از ریشهٔ دیگری، vah- «باشیدن»، آمده است. vahāna- صورتی بازسازی‌شده از هوبشمان است که آن را با سنسکریت vasana- «جامه» سنجیده است. پس صورت فرضی است و ادعای نورایی تنها با احتیاط پذیرفتنی است.\",\n  \"sources\": [W + \"بهانه\"],\n  \"ref_check\": [{\"ref\": \"HUB:32\", \"status\": \"supports\", \"note\": \"HUB p.32 no.244: 'auf ap. *vahāna- zurück, das ich mit Fr. Müller zu skr. vasana- Gewand stelle' (form starred, i.e. reconstructed).\"},\n    {\"ref\": \"AEF:305\", \"status\": \"not_checked\", \"note\": \"AEF not on disk.\"}],\n  \"consulted\": [{\"src\": \"KNT\", \"where\": \"Lexicon s.v. āvahana-, vah- (KNT_full.txt l.24118, 28911)\", \"stance\": \"contradicts\", \"note\": \"'āvahana- sb. village'; 'vah- vb. dwell, see āvahana-'. Kent has no vahāna- 'cover'; the only attested OP word of this shape belongs to 'dwell'.\"},\n    {\"src\": \"BRT\", \"where\": \"col. 1394 s.v. vah- 'sich kleiden'\", \"stance\": \"partial\", \"note\": \"BRT.txt l.23299 'vah- V. sich kleiden in —, Praes. 1 vah-, 2 vaŋha-'. The Avestan root exists, but there is no *vahāna- derivative.\"}]},\n {\"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"vahânak\", \"verdict\": \"plausible\",\n  \"derivation\": \"The Pahlavi word is written wh'n(k)' and Manichaean MP wh'ng. Older scholars read it vahān(ak) (Hübschmann, after Pazand vahāna 'cause'). MacKenzie reads it wihān(ag) 'cause, reason' and gives NP bahāna. With the wi- reading, a derivation from *wahāna- 'covering' is not straightforward. The word and its meaning ('cause, pretext') are correct. The reading and the ancestry Nourai gives follow Hübschmann and are not the current standard.\",\n  \"derivation_fa\": \"واژهٔ پهلوی با نگارش wh'n(k)' (مانوی wh'ng) به معنی «سبب، علت، بهانه» است. هوبشمان آن را vahānak می‌خواند. مکنزی آن را wihān(ag) خوانده است، و با این خوانش پیوند آن با *wahāna- «پوشش» آسان نیست. وجود واژه و معنای آن درست است، ولی خوانش و تبار آن جای بحث دارد.\",\n  \"sources\": [W + \"بهانه\"],\n  \"ref_check\": [{\"ref\": \"HUB:32\", \"status\": \"supports\", \"note\": \"HUB p.32: 'paz. vahāna = vahān cause Shk. 270 (vgl. avahān without a cause) = phl. vahānak'.\"}],\n  \"consulted\": [PHD_WIHAN, NYB_SILENT]},\n {\"id\": 6, \"lang\": \"Persian\", \"words\": \"bahâneh\", \"verdict\": \"plausible\",\n  \"derivation\": \"NP bahāna 'pretext, excuse' continues MP wh'n(k)' (wihānag / vahānak 'cause, reason'), with Iranian w- > NP b- and the -ag > -a(h) ending. Hübschmann (no. 244) derived it from OP *vahāna- 'covering' (cf. Skt. vasana- 'garment'). His semantic path is 'garment > cover > pretext', like German Gewand / Vorwand and Latin praetextus. He explicitly rejected Darmesteter's apidhāna- and Horn's upadhāna-. Wiktionary gives the MP source but leaves the Proto-Iranian form blank. MacKenzie's reading wihānag would point to a wi- prefixed formation instead. Nourai follows Hübschmann. The link is reasonable but not settled.\",\n  \"derivation_fa\": \"«بهانه» از فارسی میانهٔ wh'n(k)' (wihānag یا vahānak به معنی «سبب، علت») است. w آغازی در فارسی به b و پسوند ‎-ag به ‎-a(h) بدل شده است. هوبشمان آن را از پارسی باستان *vahāna- «پوشش» (سنجیدنی با سنسکریت vasana- «جامه») می‌داند و تحول معنایی «جامه ← پوشش ← بهانه» را با آلمانی Gewand/Vorwand و لاتینی praetextus می‌سنجد. ویکی‌واژه صورت ایرانی باستان را نامعلوم گذاشته، و خوانش مکنزی (wihānag) پیشوند wi- را نشان می‌دهد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W + \"بهانه\", \"https://vajehyab.com/moein/بهانه\"],\n  \"ref_check\": [{\"ref\": \"AEF:305\", \"status\": \"not_checked\", \"note\": \"AEF not on disk; Hübschmann's note, which AEF translates, was read directly (HUB p.32).\"}],\n  \"consulted\": [HUB32, PHD_WIHAN,\n    {\"src\": \"MON\", \"where\": \"vajehyab Mo'in s.v. بهانه\", \"stance\": \"partial\", \"note\": \"'بهانه (بَ نِ) [په.] (اِ.) ۱- عذر نابجا ۲- بازخواست ۳- سبب، باعث'. Mo'in confirms the Pahlavi origin, without a deeper etymology.\"},\n    {\"src\": \"HRN\", \"where\": \"grep bahāna\", \"stance\": \"silent\", \"note\": \"no Horn entry for bahāna found in HRN.txt (Hübschmann cites Horn's KZ 32 proposal upadhāna-, which he rejects).\"},\n    ARY_SILENT]},\n {\"id\": 7, \"lang\": \"Avestan / Old Persian\", \"words\": \"apa-vasta, pavasta, pastô\", \"verdict\": \"plausible\",\n  \"derivation\": \"OP pavastā- appears in the Bisotun inscription (DB IV 89, 'on clay tablets(?) and on parchment'). Wiktionary and Gharib take it from Proto-Indo-Iranian *pawástam 'covering, envelope' and make it the source of MP pōst and Sogdian pwst'k. The usual analysis is *pa- / *apa- + vasta- 'clothed, covered' (from vah- < *wes- 'to clothe'), so the derivation from this root is widely accepted. The Avestan word is pəsta- m. 'skin', stem form pəstō- in compounds, which Nourai writes 'pastô'. Bartholomae lists pəsta- but marks its etymology '?', and asks how MP/NP pōst can have ō if it is the same word. 'apa-vasta' is a reconstruction, not an attested form. Kent's 1950 lexicon does not include pavastā-.\",\n  \"derivation_fa\": \"پارسی باستان pavastā- در کتیبهٔ بیستون (ستون ۴، بند ۸۹) آمده و ویکی‌واژه و قریب آن را از هندوایرانی *pawástam «پوشش، پاکت» و آن را از پیشوند pa-/apa- و vasta- «پوشیده» (از ریشهٔ *wes- «پوشیدن») می‌دانند. اوستایی pəsta- «پوست» (در ترکیب pəstō-) است و بارتولومه ریشهٔ آن را نامعلوم می‌داند. «apa-vasta» صورتی بازسازی‌شده است، نه گواهی‌شده. ادعای نورایی پذیرفتنی است ولی همهٔ جزئیاتش ثابت نیست.\",\n  \"sources\": [W + \"پوست\"],\n  \"ref_check\": [{\"ref\": \"BRT:904\", \"status\": \"partial\", \"note\": \"BRT col. 903-904: 'pəsta- m. Haut ... Et.? — mp., np. pōst. Aber woher ō?' — the word and gloss match, but the derivation from apa-vasta- is not given.\"},\n    {\"ref\": \"KLN:1223\", \"status\": \"supports\", \"note\": \"KLN_1966 s.v. posteen (leaf 652): 'Pers. postin ... fr. post, hide, leather, which is rel. to Pehlevi post, Avestic pąsto'.\"},\n    {\"ref\": \"KNT:196\", \"status\": \"not_found\", \"note\": \"KNT_full.txt p.196 runs pariyana- ... Pārsa-; there is no pavastā- in the 1950 lexicon (the DB IV 89 reading was published later).\"},\n    {\"ref\": \"AEF:410\", \"status\": \"not_checked\", \"note\": \"AEF not on disk.\"}],\n  \"consulted\": [SOD8228, HRN338, BQT427_C]},\n {\"id\": 8, \"lang\": \"Pahlavi\", \"words\": \"pôst\", \"verdict\": \"confirmed\",\n  \"derivation\": \"MP pōst [pwst'] 'skin, hide, rind' (Manichaean pwst), with the derivatives pōstēn / pōstīn 'made of leather' and pōstiyān 'leather'. It is the regular continuation of Old Iranian *pawasta- (OP pavastā-): the sequence -awa- contracts to -ō- (as in *gawa- > gō-), which also answers Bartholomae's question 'woher ō?'.\",\n  \"derivation_fa\": \"پهلوی pōst «پوست، چرم» با مشتق‌های pōstēn و pōstiyān گواهی شده است. این واژه دنبالهٔ ایرانی باستان *pawasta- (پارسی باستان pavastā-) است که در آن ‎-awa- به ō فشرده شده است. نیبرگ، معین در حواشی برهان و هرن آن را تأیید می‌کنند و ادعای نورایی درست است.\",\n  \"sources\": [W + \"پوست\", W + \"پوستین\"],\n  \"ref_check\": [{\"ref\": \"SNS:139\", \"status\": \"supports\", \"note\": \"SNS index: 'pōst 138/20', 'pōstēn 139/3' (SNS_pages.txt l.15900-15901).\"},\n    {\"ref\": \"SNS:410\", \"status\": \"not_checked\", \"note\": \"SNS page 410 not located (242-leaf scan, page offset undetermined).\"}],\n  \"consulted\": [NYB_POST, BQT427_C,\n    {\"src\": \"PHD\", \"where\": \"grep pōst\", \"stance\": \"silent\", \"note\": \"the pōst line was not picked up by the OCR of PHD.txt/PHD_mackenzie.txt (the p- section is merged); not located.\"}]},\n {\"id\": 9, \"lang\": \"Persian\", \"words\": \"pŭst\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP pōst (Classical) > pūst (modern Iranian Persian, since majhul ō merged with ū) 'skin, hide, rind' is inherited from MP pōst. Derivatives are pōsta 'shell, crust' and pōstīn 'fur coat' (< MP pōstēn), which English borrowed via Anglo-Indian as posteen. The Kurdish, Pashto, Wakhi and Sarikoli cognates (pōst, pīst, past) are listed by Horn and Mo'in.\",\n  \"derivation_fa\": \"«پوست» (در فارسی دری pōst و در فارسی امروز ایران pust، با یکی شدن واو مجهول و معروف) از فارسی میانهٔ pōst آمده است. «پوسته» و «پوستین» (از پهلوی pōstēn) از آن ساخته شده‌اند و انگلیسی posteen از راه هندوستان از همین «پوستین» وام گرفته شده است. معین در حاشیهٔ برهان، هرن و کلاین این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  \"sources\": [W + \"پوست\", W + \"پوستین\", \"https://vajehyab.com/moein/پوست\", \"https://archive.org/details/borhan-ghate-v1/page/n653\"],\n  \"ref_check\": [{\"ref\": \"BQT:427\", \"status\": \"supports\", \"note\": \"BQT p.427 (leaf n653) note 8 s.v. پوست: 'پهلوی pôst ... اوستا pasta «بارتولمه ۹۰۴»، کردی pîst، pôst، افغانی pôst ...' — the same chain as Nourai's.\"},\n    {\"ref\": \"MON:830\", \"status\": \"partial\", \"note\": \"vajehyab Mo'in s.v. پوست gives the meanings only ('بیرونی‌ترین بخش بدن جانوران ...'); the print etymology is not online.\"},\n    {\"ref\": \"AEF:410\", \"status\": \"not_checked\", \"note\": \"AEF not on disk.\"}],\n  \"consulted\": [HRN338, KLN_POSTEEN, ARY_SILENT]},\n {\"id\": 10, \"lang\": \"Sogdian\", \"words\": \"pwst; pwst`k\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian pwst(h) /post/ 'skin, leather' (Gharib no. 8230) is the cognate of MP pōst. pwst'k /poste/ 'book, sutra, document, writing, parchment' (no. 8228; Parthian pwstg) is a -ka- derivative of the same word, glossed '< OP pavasta-'. The sense 'writing surface, book' arises from 'prepared skin, parchment' (cf. Skt. pustaka 'book', usually regarded as an Iranian loan). Nourai's 'writing tablet' is a fair short gloss.\",\n  \"derivation_fa\": \"سغدی pwst (post) «پوست، چرم» هم‌ریشهٔ پهلوی pōst است. pwst'k (poste) به معنی «کتاب، نوشته، پوست‌نوشته» (پارتی pwstg) با پسوند ‎-ka- از همان واژه ساخته شده است. قریب آن را از پارسی باستان pavasta- می‌داند. تحول معنایی «پوستِ آماده‌شده ← نوشته، کتاب» است؛ سنسکریت pustaka «کتاب» را هم وام‌واژه‌ای ایرانی می‌دانند. ادعای نورایی درست است.\",\n  \"sources\": [W + \"پوست\"],\n  \"ref_check\": [{\"ref\": \"SOD:331\", \"status\": \"supports\", \"note\": \"SOD leaf 398 (≈ p. 332): '8228 pwst'k ... < OP pavasta-, Parth. pwstg, Skt. pustaka ... book, Sutra, document, writing, parchment'; '8230 pwst(h) S post skin, leather'.\"}],\n  \"consulted\": [SOD8228, {\"src\": \"ISS_alt_DKS\", \"where\": \"not searched\", \"stance\": \"silent\", \"note\": \"Khotanese not relevant to this node; no Sogdian source besides Gharib in the matrix.\"}]},\n {\"id\": 11, \"lang\": \"Avestan\", \"words\": \"pastô-fratha\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Av. pəstō.fraθaŋhəm (adv., Vīdēvdād 3.20, 18.10) 'to the breadth of the (hairy) skin', i.e. 'as far as the scalp reaches' (flaying the head). It is a compound of pəsta- 'skin' (stem form pəstō-) and fraθah- 'breadth' (cf. Skt. prathas-, PIE *pleth2- 'flat, broad', Nourai's 'Per 1'). The Pahlavi translation renders it pōst pahnāk 'skin-breadth'. Nourai's gloss 'as wide as the skin gets' is correct.\",\n  \"derivation_fa\": \"اوستایی pəstō.fraθaŋhəm (قید، وندیداد ۳٫۲۰ و ۱۸٫۱۰) یعنی «به پهنای پوستِ مودار»، یعنی «تا جایی که پوست سر می‌رسد». این واژه از pəsta- «پوست» و fraθah- «پهنا» (هم‌ریشه با سنسکریت prathas-) ساخته شده است. گزارش پهلوی آن pōst pahnāk است. بارتولومه آن را دقیقاً همین‌گونه معنی کرده و ادعای نورایی درست است.\",\n  \"sources\": [W + \"پوست\"],\n  \"ref_check\": [{\"ref\": \"BRT:904\", \"status\": \"supports\", \"note\": \"BRT col. 904: 'pəstō.fraθaŋhəm Adv. in der Breite der (behaarten) Haut sva. soweit die (behaarte) Haut (des Kopfes) geht ... V.3.20 ... V.18.10 ... Pü. pōst pahnāk'.\"},\n    {\"ref\": \"AEF:410\", \"status\": \"not_checked\", \"note\": \"AEF not on disk.\"}],\n  \"consulted\": [HRN338, {\"src\": \"KNT\", \"where\": \"n/a\", \"stance\": \"silent\", \"note\": \"Avestan-only compound; not in Kent's OP lexicon.\"}]},\n {\"id\": 12, \"lang\": \"Germanic\", \"words\": \"wazjan\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *wazjaną 'to clothe, wear' is the causative-iterative *wos-éye- of *wes- 'to clothe', with *s > *z by Verner's law. Gothic wasjan, ON verja, OHG werien and OE werian go back to it.\",\n  \"derivation_fa\": \"پیش‌ژرمنی *wazjaną «پوشاندن، پوشیدن» صورت سببی ریشهٔ *wes- (*wos-éye-) است و s بنابر قانون ورنر به z بدل شده است. گوتی wasjan و انگلیسی کهن werian از آن آمده‌اند. واتکینز و پوکورنی این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  \"sources\": [W + \"Reconstruction:Proto-Germanic/wazjaną\", PIE_WES],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.1162: 'Suffixed o-grade form *wos-eyo- in Germanic *wazjan in Old English werian, to wear'.\"}],\n  \"consulted\": [POK1172 | {\"src\": \"POK\", \"where\": \"p. 1172 ues-5\", \"stance\": \"supports\"} if False else {\"src\": \"POK\", \"where\": \"p. 1172 ues-5\", \"stance\": \"supports\", \"note\": \"'Gothic wasjan, Old High German werian, Old Icelandic veria apparel, Old English werian'.\"}, WLD309]},\n {\"id\": 13, \"lang\": \"English\", \"words\": \"wear\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English wear < ME weren < OE werian 'to clothe, wear' < Proto-Germanic *wazjan. The senses 'use up, erode' develop from carrying clothes on the body until they wear out (Skeat). The strong past tense wore is a later, analogical form.\",\n  \"derivation_fa\": \"انگلیسی wear از انگلیسی میانه weren و انگلیسی کهن werian «پوشیدن» و آن از ژرمنی *wazjan است. معنای «فرسودن» از «پوشیدن جامه تا کهنه شدن» برآمده است. اسکیت و واتکینز این را تأیید می‌کنند و ادعای نورایی درست است.\",\n  \"sources\": [W + \"wear\"],\n  \"ref_check\": [{\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"node has no cited reference; AHD wes-4 (the root ref) covers it.\"}],\n  \"consulted\": [AHD_WES4, {\"src\": \"SKT\", \"where\": \"s.v. Wear (1) (SKT.txt l.21260)\", \"stance\": \"supports\", \"note\": \"'Wear (1), to wear clothes ... A.S. werian ... Goth. wasjan, to clothe. (√WAS, to clothe.)'\"}]},\n {\"id\": 14, \"lang\": \"Latin\", \"words\": \"vestis\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Latin vestis 'garment, clothing' < PIE *wes-ti- 'clothing', with the denominative verb vestīre 'to clothe'. It is cognate with Gothic wasti 'garment'.\",\n  \"derivation_fa\": \"لاتینی vestis «جامه» از هندواروپایی *wes-ti- «پوشاک» است و فعل vestīre «پوشاندن» از آن ساخته شده است. این واژه با گوتی wasti «جامه» هم‌ریشه است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"vestis\", PIE_WES],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD wes-4: 'Suffixed form *wes-ti- in Latin vestis, garment'.\"}],\n  \"consulted\": [WLD309, {\"src\": \"POK\", \"where\": \"p. 1172\", \"stance\": \"supports\", \"note\": \"'Latin vestis clothing, vestio, -ire apparel'.\"}, SYN_CLOTH]},\n {\"id\": 15, \"lang\": \"English\", \"words\": \"vest, divest, invest\", \"verdict\": \"confirmed\",\n  \"derivation\": \"vest (17th c.) comes from French veste < Italian veste < Latin vestis. invest comes from Middle French investir / Medieval Latin investīre 'to clothe (with an office)' (in- + vestīre). The financial sense comes via Italian investire. divest is an alteration of devest < Middle French devester < Old French desvestir 'to strip' (des- + vestir).\",\n  \"derivation_fa\": \"انگلیسی vest از فرانسوی veste و ایتالیایی veste و آن از لاتینی vestis است. invest از لاتینی investīre «پوشاندن (جامهٔ منصب)» آمده و معنای مالی‌اش از راه ایتالیایی investire است. divest دگرگون‌شدهٔ devest از فرانسوی کهن desvestir «برهنه کردن» است. ادعای نورایی درست است.\",\n  \"sources\": [W + \"vest\", W + \"invest\", W + \"divest\"],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD wes-4: 'Latin vestis, garment: VEST; DEVEST, INVEST, REVEST, TRAVESTY'.\"}],\n  \"consulted\": [AHD_WES4, {\"src\": \"KLN\", \"where\": \"s.v. vest/invest\", \"stance\": \"silent\", \"note\": \"headwords not isolable by grep in KLN_1966.txt OCR.\"}]},\n]\n\nentries.append({\n \"entry\": 0, \"root\": \"Wes 3, Ew-es, Eu-es\", \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *wes- (*h2wes-) 'to clothe, put on', an extension of *h3ew- / *eu- 'to put on'\",\n \"note\": \"Pokorny 1172-1173 '5. ues- to dress, put on'; Walde-Pokorny I 309 '5. ues- kleiden (Erw. von *eu- anziehen)'; Watkins/AHD wes-4 'To clothe. Extension of eu-1'. Root, label and gloss are correct, and the alternative heading 'Ew-es, Eu-es' reflects the standard view that *wes- extends *eu-. Iranian links: the vah-/vastra-/vaŋhana- group (node 1) and pōst (nodes 7-11) are sound. bām/bānū and bahāna (nodes 2, 4-6) rest on reconstructions by Andreas, Horn and Hübschmann that later scholars doubt, partly or wholly. One misprint: 'vašaiti' for vaŋhaiti (node 1).\",\n \"note_fa\": \"ریشهٔ هندواروپایی *wes- «پوشیدن، بر تن کردن» که گسترش‌یافتهٔ ریشهٔ *eu- «پوشیدن» است. پوکورنی (ص ۱۱۷۲)، والde-پوکورنی و واتکینز آن را با همین معنی آورده‌اند و ادعای نورایی دربارهٔ ریشه درست است. شاخهٔ اوستایی (vastra-، vaŋhana-) و شاخهٔ «پوست» استوارند. پیوند «بام/بانو» و «بهانه» با این ریشه بر بازسازی‌های هوبشمان و دیگران تکیه دارد و تنها با احتیاط پذیرفتنی است.\",\n \"sources\": [PIE_WES],\n \"ref_check\": [POK1172],\n \"consulted\": [WLD309, AHD_WES4, SYN_CLOTH],\n \"nodes\": e0_nodes})\n\n# ---------------- entry 1 ----------------\ne1_nodes = [\n {\"id\": 1, \"lang\": \"Avestan\", \"words\": \"vastra 2, vâstra 2\", \"verdict\": \"plausible\",\n  \"derivation\": \"Av. vāstra- n. 'pasture, fodder' and vāstar- m. 'herdsman' (whence vāstrya- 'farmer', vāstryō.fšuyant- 'cattle-breeding farmer') belong to PIE *wes- 'to graze, feed' (Wiktionary *wes- etym. 2, Pokorny 2. ues- 'to feast'), with Hittite wēsi- 'pasture' and wastara- 'herdsman'. The long ā marks it off from vastra- 'garment' (*wes- 'clothe'). Nourai's 'vastra 2' with short a, and the added gloss 'also a lining and cover', mix the two homonyms: 'lining, cover' belongs to vastra- 1 (entry 0). The form vāstra- and the core gloss 'food, fodder' are correct.\",\n  \"derivation_fa\": \"اوستایی vāstra- «چراگاه، علوفه» و vāstar- «شبان» (و از آن vāstrya- «کشاورز» و vāstryō.fšuyant- «کشاورزِ دامپرور») از ریشهٔ *wes- «چریدن، خوردن» است و با هیتی wēsi- «چراگاه» هم‌ریشه است. ā کشیده این واژه را از vastra- «جامه» جدا می‌کند. «vastra 2» با a کوتاه و معنای «آستر و پوشش» با vastra-ی نخست درآمیخته است. پس اصل ادعا درست است ولی جزئیات آن آشفته است.\",\n  \"sources\": [PIE_WES, W + \"𐬬𐬀𐬯𐬙𐬭𐬀\"],\n  \"ref_check\": [{\"ref\": \"POK:1171\", \"status\": \"supports\", \"note\": \"POK_full.txt l.92405ff 'Root / lemma: ues-2 Meaning: to feast ... Avestan vāstra- Fresse, muzzle [sic, OCR], vāstrəm food, vāstar- Hirte' (Page 1171).\"},\n    {\"ref\": \"WLD1:307\", \"status\": \"supports\", \"note\": \"WLD Bd. I 307 (leaf 316): '2. ues- schmausen ... av. vāstra Fresse, Maul ... Zu av. vāstra Futter, vāstar- Hirte s. Bartholomae, Airan. Wb. 1413'.\"}],\n  \"consulted\": [{\"src\": \"BRT\", \"where\": \"col. 1413-1416 (via a-vāstra-, gavāstrya-, BRT.txt l.5184, 10177)\", \"stance\": \"supports\", \"note\": \"'a-vāstra- Adj. was kein Futter hat'; 'gavāstrya- Adj. was sich auf die Weide des Rinds bezieht, landwirtschaftlich'; Walde-Pokorny cites Bartholomae col. 1413 for vāstra- 'Futter', vāstar- 'Hirte'.\"},\n    {\"src\": \"SYN\", \"where\": \"3.17 PASTURE (SYN.txt l.4014)\", \"stance\": \"supports\", \"note\": \"'Av. vāstrya-, deriv. of vāstra- fodder and pasture (cf. also vāstar- herdsman), this prob. : Skt. vas- consume (rare), OE wist food, etc. Walde-P. 1.306 ff.'\"}]},\n {\"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vâstr; vastriuš\", \"verdict\": \"confirmed\",\n  \"derivation\": \"MP wāstar [w'stl] 'pasture, fodder' and wāstaryōš [w'stlywš] 'husbandman', the third estate of Sasanian society. MacKenzie and Nyberg treat both as learned borrowings from Avestan (vāstra-; vāstryō.fšuyant-, with the second member reduced). Nourai's 'farm, meadow' and 'farmer' are acceptable glosses. 'vastriuš' is his spelling of wāstaryōš / vāstriyōš.\",\n  \"derivation_fa\": \"پهلوی wāstar «چراگاه، علوفه» و wāstaryōš «کشاورز» (طبقهٔ سوم جامعهٔ ساسانی) هر دو به گفتهٔ مکنزی و نیبرگ از اوستایی vāstra- و vāstryō.fšuyant- وام گرفته شده‌اند. «vastriuš» نگارش نورایی برای wāstaryōš است. ادعای نورایی درست است.\",\n  \"sources\": [PIE_WES],\n  \"ref_check\": [{\"ref\": \"SNS:260\", \"status\": \"supports\", \"note\": \"SNS index 'vastryōš 260/9' (SNS_pages.txt l.15772); glossary lines 'vāstr ... (1385) vastra-', 'vāstryōš ... (1416) vāstryō.fšuyant-' (l.10293-10310).\"}],\n  \"consulted\": [{\"src\": \"PHD\", \"where\": \"s.v. wāstar, wāstaryōš (PHD.txt l.623-625)\", \"stance\": \"supports\", \"note\": \"'wāstar [w'stl] pasture, fodder'; 'wāstaryōš [w'stlywš = Av. wāstryō.fšuyant-] husbandman'.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary s.v. vāstr, vāstriyōš (NYB_vol2_glossary.txt l.4019-4020)\", \"stance\": \"supports\", \"note\": \"'vāstr [w'stl] pasture, (cattle) food — Borrowed from Av. (1414) vāstra-'; 'vāstriyōš [w'stlywš] cattle-breeder ... the third class of the Sassanian society — Borrowed from Av. (1028, 1416) vāstryō.fšuyant-'.\"}]},\n {\"id\": 3, \"lang\": \"Persian\", \"words\": \"vâstar; vâstriyŭš\", \"verdict\": \"plausible\",\n  \"derivation\": \"NP vāstriyūš 'farmer, the farming estate of Sasanian times' is in Mo'in, tagged [په.] (Pahlavi). It is a learned, bookish revival of MP wāstaryōš, not a word inherited through spoken Persian: an inherited form would show w- > b- or g-. vāstar 'meadow, farm' is likewise a dictionary transposition of MP wāstar and is not in Mo'in's online lexicon. The chart's NOTE says the link to NP vās 'wheat' is unclear. No source consulted connects vās with this root, so that question remains open.\",\n  \"derivation_fa\": \"«واستریوش» به معنی «کشاورز، طبقهٔ کشاورزان در دورهٔ ساسانی» در فرهنگ معین با نشان [په.] آمده است. این واژه وام‌گیری ادبی و کتابی از پهلوی wāstaryōš است، نه دنبالهٔ طبیعی آن؛ در آن صورت w آغازی به ب یا گ بدل می‌شد. «واستر» نیز صورت فرهنگی پهلوی wāstar است و در معین برخط یافت نشد. پیوند «واس» (گندم) با این ریشه را هیچ منبعی تأیید نمی‌کند. ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [\"https://vajehyab.com/moein/واستریوش\"],\n  \"ref_check\": [{\"ref\": \"MON:4946\", \"status\": \"supports\", \"note\": \"vajehyab Mo'in s.v. واستریوش: '(تَ) [په.] (اِ.) کشاورز و آن یکی از طبقات چهارگانهٔ عهد ساسانی به شمار می‌رفته. ج. واستریوشان'. واستر has no Mo'in entry online.\"},\n    {\"ref\": \"SNS:260\", \"status\": \"supports\", \"note\": \"SNS p.260 l.9 vastryōš (index l.15772), the Pahlavi source of the NP form.\"}],\n  \"consulted\": [{\"src\": \"HRN\", \"where\": \"grep vāstar/vāstriyūš\", \"stance\": \"silent\", \"note\": \"no entry in Horn (the word is not part of the inherited NP lexicon).\"},\n    {\"src\": \"HUB\", \"where\": \"grep vāstar\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v1/v2/v3/v4_pages.txt grep واستر\", \"stance\": \"silent\", \"note\": \"not found in the OCR text.\"},\n    ARY_SILENT]},\n]\n\nentries.append({\n \"entry\": 1, \"root\": \"Wes 4\", \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *wes- 'to graze, feed, consume' (Pokorny 2. ues- 'schmausen')\",\n \"note\": \"Pokorny 1171 '2. ues- to feast'; Walde-Pokorny I 307 '2. ues- schmausen' with Av. vāstra 'Futter', vāstar- 'Hirte'; Wiktionary *wes- (etym. 2) 'to graze, consume, eat' with Hitt. wēsi- 'pasture', Av. vāstar-, vāstra-. Root and gloss are correct. Watkins/AHD does not list this root. Nourai's 'Compare with Ed: to eat' refers to the semantic overlap only; the two roots are unrelated.\",\n \"note_fa\": \"ریشهٔ هندواروپایی *wes- «چریدن، خوردن، خوراک دادن» در پوکورنی (ص ۱۱۷۱) و والده-پوکورنی (ج ۱ ص ۳۰۷) با گواه اوستایی vāstra- «علوفه» و vāstar- «شبان» آمده است. ادعای نورایی دربارهٔ ریشه درست است. این ریشه از ریشهٔ هم‌آوای *wes- «پوشیدن» جداست.\",\n \"sources\": [PIE_WES],\n \"ref_check\": [{\"ref\": \"POK:1171\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root / lemma: ues-2 Meaning: to feast' (Page(s): 1171).\"},\n   {\"ref\": \"WLD1:307\", \"status\": \"supports\", \"note\": \"WLD Bd. I 307: '2. ues- schmausen; aufgeräumt sein'.\"}],\n \"consulted\": [{\"src\": \"AHD\", \"where\": \"Watkins 1985 wes-1 ... wes-4\", \"stance\": \"silent\", \"note\": \"AHD lists wes-1 'buy', wes-2 'wet', wes-3 'dwell', wes-4 'clothe' — no 'feed' root.\"},\n   {\"src\": \"SYN\", \"where\": \"3.17 (SYN.txt l.4014)\", \"stance\": \"supports\", \"note\": \"'Skt. vas- consume (rare), OE wist food ... Walde-P. 1.306 ff.'\"}],\n \"nodes\": e1_nodes})\n\nout = {\"pdf_page\": 551, \"book_page\": 521, \"verified_by\": \"claude-opus-5.5\", \"verified_on\": \"2026-10-16\", \"entries\": entries}\njson.dump(out, open(\"/home/sfmqrb/git/rishe-private/data/verification/page-551.json\", \"w\"), ensure_ascii=False, indent=1)\n"
}
```


### [2026-10-17T00:09:13.805Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-551.py (file state is current in your context — no need to Read it back)
```


## [2026-10-17T00:09:17.429Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c 'واستر' BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; grep -n 'واستر' incoming/BQT/*.txt BQT_v*_pages.txt | head -5 | cut -c1-200"
}
```


### [2026-10-17T00:09:17.800Z] TOOL RESULT

```
incoming/BQT/BQT_v5_pages.txt:0
BQT_v1_pages.txt:6
incoming/BQT/BQT_v4_pages.txt:3
incoming/BQT/BQT_v3_pages.txt:12
BQT_v2_pages.txt:7
BQT_v2_pages.txt:6893:‫چموش» بروزن خموش ‪ ۰‬اسب واستر‬                      ‫راه و لرم رفتار را هم‬      ‫باشند ‪ -‬و اسب خوش‬
BQT_v2_pages.txt:11030:‫واستر وخر وامثال آن باشدکه چدار وبشاوبرآن‬              ‫یشم اول و فتح ثالث ‪٠‬‏ ربزء‬           ‫حرده‬
BQT_v2_pages.txt:13544:‫خناده" = بفتح‌اول بروزن‌فلاده» بزبان | است که خر واسب واستر را بهم میرسد و آنرا‬
BQT_v2_pages.txt:22010:‫واسب واستر وخربرا کیوزبند که از کل تا‬                            ‫و زای قطه دار (‪ » )۱‬رنگك و لون راگوند‬
BQT_v2_pages.txt:23309:‫ت مطلقاً امم ازاسب واستر‬
```


## [2026-10-17T00:09:20.365Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'واستر\\|واستریوش\\|واستریو' incoming/BQT/BQT_v4_pages.txt | cut -c1-200"
}
```


### [2026-10-17T00:09:20.868Z] TOOL RESULT

```
11654:مه ر کشاورزی ( واستربوشی ) است . از باوری این آتش است که کشاورزان ازکار کشاورزی دالاتر
20750:منداغوری وبطیطی‌پیزدامند. واسترج واسترنج معرب‌استرنگه 3 ای 1
21280:گردد. گوبند علت برقان واسترخای اعضارا برد وه - بفتم اول و ثالی مشدد , بمعنی
```


## [2026-10-17T00:09:27.373Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-551.py'; s=open(p).read()\ns=s.replace('''\"consulted\": [POK1172 | {\"src\": \"POK\", \"where\": \"p. 1172 ues-5\", \"stance\": \"supports\"} if False else {\"src\": \"POK\",''','''\"consulted\": [{\"src\": \"POK\",''')\ns=s.replace(\"والde-پوکورنی\",\"والده-پوکورنی\")\ns=s.replace('''{\"src\": \"BQT\", \"where\": \"BQT_v1/v2/v3/v4_pages.txt grep واستر\", \"stance\": \"silent\", \"note\": \"not found in the OCR text.\"}''','''{\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt l.11654 (Mo'in's note on a fire-temple headword)\", \"stance\": \"partial\", \"note\": \"only an incidental mention, '... کشاورزی ( واستریوشی ) است', using the learned term for the farming estate. There is no headword واستر/واستریوش in vols 1-5 (the other hits are «و استر» 'and mule').\"}''')\nopen(p,'w').write(s)\nEOF\npython3 build-551.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-551.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 551"
}
```


### [2026-10-17T00:09:27.942Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'transcription_suspect': 1, 'plausible': 7, 'confirmed': 10}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'not_found': 2, 'not_checked': 8, 'partial': 2}
books consulted: {'supports': 27, 'partial': 7, 'contradicts': 2, 'silent': 13} | by book: {'HRN': 6, 'PHD': 5, 'WLD': 4, 'SYN': 4, 'ARY': 4, 'BRT': 3, 'HUB': 3, 'NYB': 3, 'BQT': 3, 'MON': 2, 'KNT': 2, 'SOD': 2, 'KLN': 2, 'POK': 2, 'AHD': 2, 'ISS_alt_DKS': 1, 'SKT': 1}
```


## [2026-10-17T00:09:38.125Z] TOOL CALL #74: SubagentHandback

```json
{
 "message": "Page 551 (book p. 521) is verified, and `verify_check.py 551` reports 0 PROBLEM lines (18/18 nodes).\n\n- **Roots:** both confirmed.\n  - Wes 3 is Pokorny 1172 \"5. ues- to dress, put on\". Walde-Pokorny I 309 and Watkins (wes-4) both call it an extension of *eu-, which explains the \"Ew-es, Eu-es\" heading.\n  - Wes 4 is Pokorny 1171 \"2. ues- to feast\" (Walde-Pokorny I 307: Av. vāstra 'Futter', vāstar- 'Hirte').\n- **Nodes:** 10 confirmed, 7 plausible, 1 transcription_suspect, 0 disputed.\n\n**Transcription suspect:**\n- Wes 3 #1 (Avestan): the book prints \"vašaiti\". That is Nourai's misprint for vaŋhaiti, the form Pokorny and Bartholomae give, so the error is in the book. \"vahna, vanhna\" are loose spellings of vaŋhana-, and aothra- 'shoe' comes from the base root *eu-, not from *wes- itself. The page image is saved at `data/verification/sources/refs/ocr/BOOK/551.png`.\n\n**Main plausible items:**\n- **#2 bām/bān and bānū:** Hübschmann (p. 25) rejects bān < OP *vahana- and doubts that bānū comes from bān. Wiktionary leaves the origin of bānū open. The chart's own NOTE about this is justified.\n- **#4–6 vahāna → vahānak → bahāna:** this chain follows Hübschmann p. 32 no. 244 (the 'garment → cover → pretext' path), but OP *vahāna- is a reconstruction, not an attested word. MacKenzie reads the Pahlavi word as wihān(ag), which makes the link harder.\n- **#7 apa-vasta/pavasta/pastô:** OP pavastā- and the derivation from 'covering' are accepted (Wiktionary, Gharib). Bartholomae marks Av. pəsta- as of unknown etymology, and Kent's 1950 lexicon has no pavastā-, so KNT:196 is not_found.\n- **Wes 4 #1:** the 'lining, cover' gloss mixes in vastra- 'garment' from the other root.\n- **Wes 4 #3:** vāstar/vāstriyūš are learned borrowings from Pahlavi; Mo'in tags واستریوش [په.]. No source supports a link to vās 'wheat'.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Files:**\n- `/home/sfmqrb/git/rishe-private/data/verification/page-551.json`\n- `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/427.vision.txt` and `427.png` (BQT p. 427, Mo'in's footnote on پوست)\n- Web sources are archived under `data/verification/sources/web/`. The Etymonline fetches and a few Wiktionary pages (واستر, واستریوش, the Proto-Iranian page) failed and are not cited."
}
```


### [2026-10-17T00:09:38.453Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
