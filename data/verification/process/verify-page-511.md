# Verification process log — verify-page-511


## [2026-10-15T02:44:16.475Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 511 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-511.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-511.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-511.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 511` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.546Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.191Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.213Z] TOOL RESULT

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


## [2026-10-15T02:44:19.691Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-511.txt"
}
```


### [2026-10-15T02:44:19.754Z] TOOL RESULT

```
1	=== PDF page 511 (book page 481) ===
2	--- entry 0 ---
3	ROOT [Tamil] Tôkei, Tôgei : peacock  (refs KLN:1143; SKT:378)
4	#1 (parent #0) [Sanskrit] refs=BQT:1346 | 
5	  #2 (parent #1) [Arabic] refs=BQT:1346 | tawoos : peacock
6	  #3 (parent #1) [Aramaic] refs=MON:2203 | tausâ : peacock
7	    #4 (parent #2) [Persian] refs=BQT:1346; MON:2203 | tâvŭs «طاوس (طاووس)» : peacock ; tâvosî «طاوسی (طاووسان)» : a plant
8	      #5 (parent #4) [Latin] refs=SKT:378 | pâuo, pâvô : peacock ; pâvonîs : peacock
9	      #6 (parent #4) [Greek] refs=KLN:1143; SKT:378 | taws, taos : peacock
10	        #7 (parent #5) [Old English] refs=AHD | pea : peacock
11	          #8 (parent #7) [English] refs=SKT:378 | peacock ; peafowl
12	--- entry 1 ---
13	ROOT Tr -> redirect to Ter 1
14	--- entry 2 ---
15	ROOT [Indo-European] Trei : three  (refs POK:1090)
16	#1 (parent #0) [Avestan / Old Persian] refs=POK:1090; SYN:941; KLN:1611; GPL:41 | thri, thrâyô : three ; thrisat : thirty ; thri-dasa : thirteen ☞Dekm ; thri-thatra : a three-stringed musical instrument ☞Ten 1
17	  #2 (parent #1) [Persian] refs=BQT:1194 | seh «سه» : three | extra: سی ، سیزده
18	  #3 (parent #1) [Persian] refs=BQT:1096 | se-târ «سه تار» : a musical instrument, originally with only three strings
19	    #4 (parent #3) [Hindustani] refs=None | 
20	      #5 (parent #4) [English] refs=AHD:1210 | sitar
21	    #6 (parent #3) [Greek] refs=KLN:687 | kithara : sitar
22	      #7 (parent #6) [Arabic] refs=SAP:1381 | qîtâr ; qeetarah
23	        #8 (parent #7) [Spanish] refs=None | 
24	          #9 (parent #8) [French] refs=KLN:687 | guitare
25	            #10 (parent #9) [Persian] refs=MON:3502 | gîtâr «گیتار»
26	            #11 (parent #9) [English] refs=KLN:687 | guitar
27	#12 (parent #0) [Sogdian] refs=SOD:143 | dry : three
28	#13 (parent #0) [Germanic] refs=AHD | thrijiz : three
29	  #14 (parent #13) [English] refs=None | three, thirty, thirteen
30	#15 (parent #0) [Latin] refs=None | teri, tri : three ; tes-tis : third person, witness ; tribus : third class citizens in Roman empire, tribes
31	  #16 (parent #15) [English] refs=AHD | tertiary, tricycle ; testimony, contest, protest ; tribe, tribune, tribute
32	
```


## [2026-10-15T02:44:20.503Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-511.json"
}
```


### [2026-10-15T02:44:20.552Z] TOOL RESULT

```
1	{
2	  "pdf_page": 511,
3	  "book_page": 481,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tôkei, Tôgei",
8	        "lang": "Tamil",
9	        "refs": "KLN:1143; SKT:378",
10	        "gloss": "peacock",
11	        "note": "Tanil is a Dravidian language spoken in south India"
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Sanskrit",
18	          "refs": "BQT:1346",
19	          "words": [],
20	          "script_extra": null,
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Arabic",
28	          "refs": "BQT:1346",
29	          "words": [
30	            {"translit": "tawoos", "gloss": "peacock", "script": null}
31	          ],
32	          "script_extra": null,
33	          "note": null,
34	          "quote": null
35	        },
36	        {
37	          "id": 3,
38	          "parent": 1,
39	          "lang": "Aramaic",
40	          "refs": "MON:2203",
41	          "words": [
42	            {"translit": "tausâ", "gloss": "peacock", "script": null}
43	          ],
44	          "script_extra": null,
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 2,
51	          "lang": "Persian",
52	          "refs": "BQT:1346; MON:2203",
53	          "words": [
54	            {"translit": "tâvŭs", "gloss": "peacock", "script": "طاوس (طاووس)"},
55	            {"translit": "tâvosî", "gloss": "a plant", "script": "طاوسی (طاووسان)"}
56	          ],
57	          "script_extra": null,
58	          "note": null,
59	          "quote": {
60	            "text": "زلف مشکین تو در گلشن فردوس عذار - چیست طاووس که در باغ نعیم افتادست",
61	            "poet": "Hâfez"
62	          }
63	        },
64	        {
65	          "id": 5,
66	          "parent": 4,
67	          "lang": "Latin",
68	          "refs": "SKT:378",
69	          "words": [
70	            {"translit": "pâuo, pâvô", "gloss": "peacock", "script": null},
71	            {"translit": "pâvonîs", "gloss": "peacock", "script": null}
72	          ],
73	          "script_extra": null,
74	          "note": null,
75	          "quote": null
76	        },
77	        {
78	          "id": 6,
79	          "parent": 4,
80	          "lang": "Greek",
81	          "refs": "KLN:1143; SKT:378",
82	          "words": [
83	            {"translit": "taws, taos", "gloss": "peacock", "script": null}
84	          ],
85	          "script_extra": null,
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 7,
91	          "parent": 5,
92	          "lang": "Old English",
93	          "refs": "AHD",
94	          "words": [
95	            {"translit": "pea", "gloss": "peacock", "script": null}
96	          ],
97	          "script_extra": null,
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 7,
104	          "lang": "English",
105	          "refs": "SKT:378",
106	          "words": [
107	            {"translit": "peacock", "gloss": null, "script": null},
108	            {"translit": "peafowl", "gloss": null, "script": null}
109	          ],
110	          "script_extra": null,
111	          "note": null,
112	          "quote": null
113	        }
114	      ]
115	    },
116	    {
117	      "root": {
118	        "name": "Tr",
119	        "redirect": "Ter 1"
120	      },
121	      "nodes": []
122	    },
123	    {
124	      "root": {
125	        "name": "Trei",
126	        "lang": "Indo-European",
127	        "refs": "POK:1090",
128	        "gloss": "three"
129	      },
130	      "nodes": [
131	        {
132	          "id": 1,
133	          "parent": 0,
134	          "lang": "Avestan / Old Persian",
135	          "refs": "POK:1090; SYN:941; KLN:1611; GPL:41",
136	          "words": [
137	            {"translit": "thri, thrâyô", "gloss": "three", "script": null},
138	            {"translit": "thrisat", "gloss": "thirty", "script": null},
139	            {"translit": "thri-dasa", "gloss": "thirteen", "script": null, "see": ["Dekm"]},
140	            {"translit": "thri-thatra", "gloss": "a three-stringed musical instrument", "script": null, "see": ["Ten 1"]}
141	          ],
142	          "script_extra": null,
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 2,
148	          "parent": 1,
149	          "lang": "Persian",
150	          "refs": "BQT:1194",
151	          "words": [
152	            {"translit": "seh", "gloss": "three", "script": "سه"}
153	          ],
154	          "script_extra": "سی ، سیزده",
155	          "note": null,
156	          "quote": null
157	        },
158	        {
159	          "id": 3,
160	          "parent": 1,
161	          "lang": "Persian",
162	          "refs": "BQT:1096",
163	          "words": [
164	            {"translit": "se-târ", "gloss": "a musical instrument, originally with only three strings", "script": "سه تار"}
165	          ],
166	          "script_extra": null,
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 4,
172	          "parent": 3,
173	          "lang": "Hindustani",
174	          "refs": null,
175	          "words": [],
176	          "script_extra": null,
177	          "note": null,
178	          "quote": null
179	        },
180	        {
181	          "id": 5,
182	          "parent": 4,
183	          "lang": "English",
184	          "refs": "AHD:1210",
185	          "words": [
186	            {"translit": "sitar", "gloss": null, "script": null}
187	          ],
188	          "script_extra": null,
189	          "note": null,
190	          "quote": null
191	        },
192	        {
193	          "id": 6,
194	          "parent": 3,
195	          "lang": "Greek",
196	          "refs": "KLN:687",
197	          "words": [
198	            {"translit": "kithara", "gloss": "sitar", "script": null}
199	          ],
200	          "script_extra": null,
201	          "note": null,
202	          "quote": null
203	        },
204	        {
205	          "id": 7,
206	          "parent": 6,
207	          "lang": "Arabic",
208	          "refs": "SAP:1381",
209	          "words": [
210	            {"translit": "qîtâr", "gloss": null, "script": null},
211	            {"translit": "qeetarah", "gloss": null, "script": null}
212	          ],
213	          "script_extra": null,
214	          "note": null,
215	          "quote": null
216	        },
217	        {
218	          "id": 8,
219	          "parent": 7,
220	          "lang": "Spanish",
221	          "refs": null,
222	          "words": [],
223	          "script_extra": null,
224	          "note": null,
225	          "quote": null
226	        },
227	        {
228	          "id": 9,
229	          "parent": 8,
230	          "lang": "French",
231	          "refs": "KLN:687",
232	          "words": [
233	            {"translit": "guitare", "gloss": null, "script": null}
234	          ],
235	          "script_extra": null,
236	          "note": null,
237	          "quote": null
238	        },
239	        {
240	          "id": 10,
241	          "parent": 9,
242	          "lang": "Persian",
243	          "refs": "MON:3502",
244	          "words": [
245	            {"translit": "gîtâr", "gloss": null, "script": "گیتار"}
246	          ],
247	          "script_extra": null,
248	          "note": null,
249	          "quote": null
250	        },
251	        {
252	          "id": 11,
253	          "parent": 9,
254	          "lang": "English",
255	          "refs": "KLN:687",
256	          "words": [
257	            {"translit": "guitar", "gloss": null, "script": null}
258	          ],
259	          "script_extra": null,
260	          "note": null,
261	          "quote": null
262	        },
263	        {
264	          "id": 12,
265	          "parent": 0,
266	          "lang": "Sogdian",
267	          "refs": "SOD:143",
268	          "words": [
269	            {"translit": "dry", "gloss": "three", "script": null}
270	          ],
271	          "script_extra": null,
272	          "note": null,
273	          "quote": null
274	        },
275	        {
276	          "id": 13,
277	          "parent": 0,
278	          "lang": "Germanic",
279	          "refs": "AHD",
280	          "words": [
281	            {"translit": "thrijiz", "gloss": "three", "script": null}
282	          ],
283	          "script_extra": null,
284	          "note": null,
285	          "quote": null
286	        },
287	        {
288	          "id": 14,
289	          "parent": 13,
290	          "lang": "English",
291	          "refs": null,
292	          "words": [
293	            {"translit": "three, thirty, thirteen", "gloss": null, "script": null}
294	          ],
295	          "script_extra": null,
296	          "note": null,
297	          "quote": null
298	        },
299	        {
300	          "id": 15,
301	          "parent": 0,
302	          "lang": "Latin",
303	          "refs": null,
304	          "words": [
305	            {"translit": "teri, tri", "gloss": "three", "script": null},
306	            {"translit": "tes-tis", "gloss": "third person, witness", "script": null},
307	            {"translit": "tribus", "gloss": "third class citizens in Roman empire, tribes", "script": null}
308	          ],
309	          "script_extra": null,
310	          "note": null,
311	          "quote": null
312	        },
313	        {
314	          "id": 16,
315	          "parent": 15,
316	          "lang": "English",
317	          "refs": "AHD",
318	          "words": [
319	            {"translit": "tertiary, tricycle", "gloss": null, "script": null},
320	            {"translit": "testimony, contest, protest", "gloss": null, "script": null},
321	            {"translit": "tribe, tribune, tribute", "gloss": null, "script": null}
322	          ],
323	          "script_extra": null,
324	          "note": null,
325	          "quote": null
326	        }
327	      ]
328	    }
329	  ]
330	}
331	
```


## [2026-10-15T02:44:23.717Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat data/verification/sources/SOURCE_MATRIX.md | head -120; ls data/verification/sources/refs/ | head -100; ls data/verification/ | head; wc -c tools/verify_check.py",
 "description": "Read source matrix and list reference files"
}
```


### [2026-10-15T02:44:24.311Z] TOOL RESULT

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
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  agent
drwxr-xr-x     - sfmqrb 14 Oct 22:34  process
drwxr-xr-x     - sfmqrb 14 Oct 22:19  sources
.rw-r--r--  9.7k sfmqrb 14 Oct 22:19  COORDINATOR.md
.rw-r--r--   89k sfmqrb 14 Oct 22:14  page-31.json
.rw-r--r--   33k sfmqrb 14 Oct 22:14  page-32.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-33.json
.rw-r--r--   85k sfmqrb 14 Oct 22:14  page-34.json
.rw-r--r--   87k sfmqrb 14 Oct 22:14  page-35.json
4283 tools/verify_check.py
```


## [2026-10-15T02:44:26.961Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat tools/verify_check.py; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','SKT','BQT','MON','POK','SYN','GPL','AHD','SAP','SOD','WLD','IEC','ARY']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "Read check script and ref metadata"
}
```


### [2026-10-15T02:44:27.608Z] TOOL RESULT

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
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f betwee
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f betwee
GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar organi
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).", "local_file": null, "page_offset": null, "c
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-10-15T02:44:30.470Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/page-5*.json; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'))\ne=d['entries'][0]; print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]); print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "View a previous verification for style"
}
```


### [2026-10-15T02:44:30.884Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  data/verification/page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  data/verification/page-51.json
.rw-r--r--   50k sfmqrb 14 Oct 22:14  data/verification/page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  data/verification/page-53.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-54.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  data/verification/page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  data/verification/page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  data/verification/page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  data/verification/page-58.json
.rw-r--r--   75k sfmqrb 14 Oct 22:14  data/verification/page-59.json
{
 "entry": 0,
 "root": "Tel",
 "verdict": "confirmed",
 "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)",
 "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-",
  "https://en.wiktionary.org/wiki/Ἄτλας",
  "https://en.wiktionary.org/wiki/τάλαντον"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "KLN:122",
   "status": "supports",
   "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τ
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "tulâ, tulya",
 "verdict": "confirmed",
 "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.",
 "derivation_fa": "سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).",
 "sources": [
  "https://en.wiktionary.org/wiki/तुला",
  "https://en.wiktionary.org/wiki/तुल्य",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "AHD",
   "status": "supports",
   "note": "Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'"
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I p.738 s.v. 1. tel-",
   "stance": "supports",
   "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
  },
  {
   "src": "KLN",
   "where": "1966 s.v. tolerate / talent",
   "stance": "supports",
   "note": "Klein 1966 s.v. tolerate (KLN_1966.txt line 39457): 'L. tolerare ... from the stem of tollere ... cogn. with ... ταλάντον 'balance', ''A-τλας 'the Bearer (scil. of Heaven)', L. lātus (for *tlatos) 'borne', OI. tulā 'balance', tulayati 'lifts up, weighs' ... All these words derive fr. I.-E. base *tel-, *tol-, *tal-, *tl- 'to bear, carry, endure, suffer'.'"
  },
  {
   "src": "IEC",
   "where": "s.v. tl- (1) (IEC.txt line 18624)",
   "stance": "silent",
   "note": "Mann: 'tl- (1) ..
```


## [2026-10-15T02:44:34.791Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls site/pages/511.jpg; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 511 -l 511 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg511",
 "description": "Render page 511 image"
}
```


## [2026-10-15T02:44:35.245Z] TOOL CALL #8: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/pg511.png"
}
```


### [2026-10-15T02:44:36.003Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   75k sfmqrb 14 Oct 22:15  site/pages/511.jpg
```


### [2026-10-15T02:44:36.356Z] TOOL RESULT

```

```


## [2026-10-15T02:44:36.352Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-10-15T02:44:55.012Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *peacock|tokei|tôkei|tokai\" KLN_1966.txt | head; grep -n -i -E \"^peacock|^pea-|^pea,\" SKT.txt | head; grep -n -i -E \"^ *pavo|taōs|ταώς|ταῶς\" KLN_1966.txt | head",
 "description": "Grep Klein and Skeat for peacock"
}
```


### [2026-10-15T02:44:55.581Z] TOOL RESULT

```
27770:peacock,  n.  —  ME.  pecok,  fr.  OE.  pdwa,  pea, ‘peacock’,  and  coc,  cocc,  ‘cock’.  The  first  ele¬ ment  derives  fr.  L.  pavo,  gen.  pavonis,  ‘peacock’ [whence  also  OHG.  pfawo  (MHG.  pfawe,  pfa, G.  Pfau),  MLG.  pawe,  Du.  patiw  and  OSlav. pavu],  which,  together  with  Gk.  Taco?,  prob. comes  ult.  fr.  Tamil  tokei,  tdgei  (whence  also Heb.  tukkiyyim,  ‘peacocks’).  The  initial  p-  in  L. pavo  is  due  to  imitative  influence;  cp.  L.  pau- pulo,  ‘the  natural  sound  of  the  peacock’.  Cp. Pavo,  pavonazzo,  pavonine,  ponceau,  ‘corn poppy’.  For  the  second  element  see  cock. Derivatives:  peacock,  intr.  v.,  peacock-ery,  n., peacock-ish,  peacock-like,  peacock-y,  adjs. peag,  n.,  beads  made  of  shells.  —  Aphetic  for Algonquian  wampum  peag,  ‘white  strings’.  See wampum.
13510:PEA-JACKE'
13526:Peacock.    (L.  -  Gk.  -  Pert.  •  Tk anJM.)     M.  V.. pec»k , petecU x  where K.  coek.     Wc   oliO   fit.d  M.  E. paitfe,  borrowed  fiom  L.  /a««  ;i paauiv,    G.   p/att,    F.     '  "- from  Gk.  tu*t,  for  r« change  from  r  to/  bci 1>eing  ill  umlcrstood,  as  il  v to    L.    and    Gk.  —  Pers.    r peacock.  —  O.  T cock;  sec   M.    ^ J33  (Sth  ed.).     9i\    ----^ still  a  suniame.
13527:Pea-jacket,  a  coarse  thick  jsei«t.j anJ  F.)    The  prefix  pta  is  bcniw Da.  pij^pift.  a  coat  of  a  coaiia ttolT;    Hexham  has  O.  Du.  /#s  '*
27747:pavonine,  adj.,  related  to,  or  resembling,  a  pea¬ cock.  —  L.  pdvoninus,  ‘of,  or  like,  a  peacock’,  fr. pavo,  gen.  pavonis,  ‘peacock’.  See  peacock  and -ine  (representing  L.  -inus). paw,  n.  —  ME.  pawe,  powe,  fr.  MF.  poue,  from  a pre-Celtic  form  *pauta  (whence  also  Proven?. pauta  and  Catal.  pote,  MDu.  poot,  pote,  Du. poof,  G.  Pfote,  ‘paw’),  which  is  prob.  of  imitative origin.  Cp.  patois,  patrol,  pattee,  patten,  pud. Derivatives:  paw,  tr.  and  intr.  v.,  paw-er,  n., paw-ing,  n.
```


## [2026-10-15T02:44:59.164Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -A8 \"^Peacock\" SKT_dli_revised.txt | head -30; grep -n -i -E \"tōkei|tokei|togei\" SKT*.txt | head",
 "description": "Grep Skeat revised for peacock"
}
```


### [2026-10-15T02:44:59.525Z] TOOL RESULT

```
55507:Peacock. (L. ~ Pers. — Tamil ; and 
55508-E.) M E. pecok, pocok ; where cok ~ E. 
55509-cock. We also find M. E. po', AS. pea, 
55510-pdwa ; all from L pduo (whence Du. 
55511-paauzv, G. pfau, F. paon). The same 
55512-as Gk. raws, for rafws, a peacock ; the 
55513-change from r io p being due to the fact 
55514-that the word was foreign both to L. and 
55515-I Gk. — Pers tdwus, tdus, a peacock.- O. 
SKT.txt:4196:{cunt\  togeilier;  and  O.  I  i
SKT.txt:22654:384.  base  SAM.  also  found  as  SA~  (at the  begiiming  of  a  word),  togeibcr,  to- gether with.  From  the  pronon^inal  bate BA,  he.  this  one.
SKT_dli_revised.txt:16161:figurdie, to put togeihci. — L. lon- p mn i ;
```


## [2026-10-15T02:45:02.033Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 55515,55525p SKT_dli_revised.txt; grep -n -E \"ط[اآ]و[و]?س\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | head; grep -n -c \"\" incoming/BQT/BQT_v3_pages.txt",
 "description": "More Skeat; grep Borhan for tavus"
}
```


### [2026-10-15T02:45:02.402Z] TOOL RESULT

```
I Gk. — Pers tdwus, tdus, a peacock.- O. 
Tamil tdkei, idgei, a peacock; see Max 
Muller, Lect. on Lang. 1. 190 (ed. 1891). 
^ Also pocock, which is still a surname. 
Pea-jacket, a coarse thick jacket. 
(Du. and F. ) The prefix pea- is borrowed 
from Du. ptj, ptje, a coat of a coarse 
woollen stuff ; Ilexham has M. Du. pije, 

‘ a pie-gowne, rough gowne, such as sea- 
men weare.’ The same as Low G pije, 
incoming/BQT/BQT_v3_pages.txt:10388:RAT ‏طاوس‎
incoming/BQT/BQT_v3_pages.txt:10395:طاوسآ تش پر ‎ale‏ از آتاب
incoming/BQT/BQT_v3_pages.txt:10398:طاوس پران ‎Ce par!‏ رین .
incoming/BQT/BQT_v3_pages.txt:10404:‏طاوس خلد = ‎LS‏ ازحور و غلمان
incoming/BQT/BQT_v3_pages.txt:10407:‏طاوس مشرق خر ام - کنابه از
incoming/BQT/BQT_v3_pages.txt:10463:‏#طاوس ءطاووس - (عر) مصفر ‎OT‏ طریس ‎wlll‏
incoming/BQT/BQT_v3_pages.txt:10464:‏5 ,آرامی طاوسا ‎tausd‏ «تیمرن. لفات دخید اکدی
incoming/BQT/BQT_v3_pages.txt:42385:وبا يك ‎gly‏ هم درست است همچوکاوی‌وطاوس.
BQT_v2_pages.txt:11668:‫دویم خروسك است که پارژ گوشت ميان فرح‬                                   ‫خر وسان طاوس دم د کنابه‬
BQT_v2_pages.txt:27453:   ‫‪ ۴‬رك‪ :‬زاو‪.‬‬          ‫‪ ۴‬رك‪ :‬آیك‪.‬‬               ‫‪ 2‬منتهی الارب»‪.‬‬    ‫زاوق ‪ ,‬کطاوس» صماب‬             ‫زواووق ‪.‬‬
51425
```


## [2026-10-15T02:45:04.620Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 10380,10475p incoming/BQT/BQT_v3_pages.txt | grep -n -E \"pdf page|طاوس|tau|ta[uw]|سنسکر|یونان|تامیل\" ",
 "description": "Read Borhan tavus entry context"
}
```


### [2026-10-15T02:45:05.086Z] TOOL RESULT

```
8:[pdf page 139]
9:RAT ‏طاوس‎
16:طاوسآ تش پر ‎ale‏ از آتاب
19:طاوس پران ‎Ce par!‏ رین .
25:‏طاوس خلد = ‎LS‏ ازحور و غلمان
28:‏طاوس مشرق خر ام - کنابه از
84:‏#طاوس ءطاووس - (عر) مصفر ‎OT‏ طریس ‎wlll‏
85:‏5 ,آرامی طاوسا ‎tausd‏ «تیمرن. لفات دخید اکدی
95:[pdf page 140]
```


## [2026-10-15T02:45:06.787Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1346 --image 2>&1 | tail -40",
 "description": "Fetch Borhan page 1346"
}
```


### [2026-10-15T02:45:11.522Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 141; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1346.png
REF: BQT:1346  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 141  OCR-lang: fas

شفا ۱۳۸
طبقا - بنتح اول و سکون نانی و قال | اطبل‌درز یر گلیم‌ما ندن - کنایه
بالف کشید.. بلفت رومی نوعی ازکندم‌باغدلیکن | از بی‌فام وشان بودن باشد.
پاریکتی از کندم‌است وآلرا بفارسی؟ا کل گویند. طبل واپس ر طبل وآپسین-
خوردن آن اسب را ضرر لرساند لیکن آدمی را هر دو بمعتی طبل ماتم است یمنی طبل ی که در
شرر یمعده رساند. عاشورا وماتم فوازند.
طبقری - بروزن جعفری , طبقچه را طبنلگ -» بنتح اول ونابی » بروزن (۱)
کوبند ۱ - وبمعنیکنار ودامن هم‌عست-وجایی | وممنی تبنك‌است ۴ وآن طبقی باشد پپن‌وبز رکه
ومقامی باشد غیر مطلوم ۴ . از چوب که بقالان اجنای درآن کنند.
۱ طبق ز نود کنایه از خان زبور طبیخ « بفتح اول و نالی‌بت<نانی رسیده
۹ طبل خوردن < کنایه از رم کردن وهای رفطهدار(۲)ازده؛بممتی خربزء‌است کهءربان
و رمیدن باعد ۴ . لیخ گوبند 8 - و درعربی هرچیز پخته شده
طبل در زیرگلیم زدن کناب | باشد :
از پنهان داعتن آمری است که آن ظاهر وهویدا طبیعت شناس کنایه‌ازطبیب ومعالج
بود و شهرت بافته باشد. باشد ‎٩‏ ۴۰
(۱) چك : بوزن * (۲)چك : وا
۱ - یکی لیشکر داشت بر طبقری چپ و راست گردید بر امعتری .
بوستّان صمدی .
۴ - درمعجم البلدان وحدودالمالم‌نيامده ۰ ۴ - همریست کزعطای تومن‌طبل میخورم-
مولوی. «رشیدی». ۴ -ر4 : تبنك . 8 - (عر) «طبیخ (بکسراول و دوم مشدد)
خربزه . آخة فی‌البطیخ» «منتهی‌الارب» ‏
‎٩‏ - امید عافیت آنگه بود موافق طبع که شی را بطبیعت شنای بنمائی .
سعدی . «اشراح ن
# طبیدن - رك : لفات متفرقهٌ پایان کتات .
* طثر ج - ر4 : لفات متفرقةٌ پایان کتاب :
* طخلیقوی - ر4 : لفات متقرقهة یایان کتاب ور4 : طفشیقون .۰
```


## [2026-10-15T02:45:14.212Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1346 --image --pdf-page 139 2>&1 | head -3; python3 tools/ref_page.py BQT:1346 --image --pdf-page 139 2>&1 | grep -n -E \"طاوس|tau|پرتو|یونانی|سنسک\" ",
 "description": "Fetch Borhan pdf page 139"
}
```


### [2026-10-15T02:45:14.777Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1346.png
REF: BQT:1346  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 141  OCR-lang: fas
```


## [2026-10-15T02:45:17.841Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; pdftoppm -f 139 -l 139 -r 150 -png -singlefile data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf $S/bqt511-139; ls $S; python3 tools/ref_page.py --help 2>&1 | head -20",
 "description": "Render Borhan pdf page 139"
}
```


### [2026-10-15T02:45:19.222Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:29  dl499
drwxr-xr-x     - sfmqrb 14 Oct 22:45  dl518
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tb
.rw-r--r--   440 sfmqrb 14 Oct 22:44  agents.txt
.rw-r--r--   68k sfmqrb 14 Oct 22:45  bqt511-139.png
.rw-r--r--   44k sfmqrb 14 Oct 22:33  gen-499.py
.rw-r--r--   115 sfmqrb 14 Oct 22:34  msg-499.txt
.rw-r--r--   57k sfmqrb 14 Oct 22:26  pg499.png
.rw-r--r--   82k sfmqrb 14 Oct 22:44  pg502.png
.rw-r--r--   74k sfmqrb 14 Oct 22:44  pg506.png
.rw-r--r--   86k sfmqrb 14 Oct 22:44  pg507.png
.rw-r--r--   82k sfmqrb 14 Oct 22:44  pg511.png
.rw-r--r--   59k sfmqrb 14 Oct 22:44  pg512.png
.rw-r--r--   76k sfmqrb 14 Oct 22:44  pg513.png
.rw-r--r--   72k sfmqrb 14 Oct 22:44  pg516.png
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


## [2026-10-15T02:45:20.960Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt511-139.png"
}
```


### [2026-10-15T02:45:21.003Z] TOOL RESULT

```

```


## [2026-10-15T02:45:29.802Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cp $S/bqt511-139.png 1346.png; cat > 1346.vision.txt <<'EOF'\n[Borhan-e Qate' ed. Mo'in, printed p. 1346 = BQT_v3_picofile.pdf page 139 (the default offset -1205 lands on pdf 141 = p. 1348; use --pdf-page 139). Transcribed from the page image.]\n\n(footnote, Mo'in) *طاوس ، طاووس - (عر) معرب آن طویس ، یونانی Taôs ، آرامی طاوسا tausâ «تسیمرن . لغات دخیل اکدی ص۵۲» طبق تحقیق استاد پور داود اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته ؛ مرغی از انواع ماکیان که اصل آن از نواحی هند و مالهٔ ورای آن ... که چون بگشاید نیم‌دایره‌ای برنگهای لطیف مختلف تشکیل دهد .\n[picture captioned طاوس]\n\n(headwords on the page include) طاوس آتش پر - کنایه از آفتاب عالمتاب است. طاوس پران اخضر ... طاوس خلد - کنایه از حور و غلمان بهشتی باشد. طاوس مشرق خرام - کنایه از آفتاب است.\nEOF\nls",
 "description": "Save Borhan transcription and image"
}
```


### [2026-10-15T02:47:31.039Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: b47dosd6u). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/b47dosd6u.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-15T02:47:33.192Z] TOOL CALL #18: Bash

```json
{
 "command": "head -c 300 /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1346.vision.txt; echo; file /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1346.png",
 "description": "Verify saved files"
}
```


### [2026-10-15T02:47:33.760Z] TOOL RESULT

```
[Borhan-e Qate' ed. Mo'in, printed p. 1346 = BQT_v3_picofile.pdf page 139 (the default offset -1205 lands on pdf 141 = p. 1348; use --pdf-page 139). Transcribed from the page image.]

(footnote, Mo'in) *طاوس ، طاووس - (عر) معرب آن طویس ، یونانی Taôs ، آرامی طاو
/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1346.png: PNG image data, 825 x 1273, 8-bit/color RGB, non-interlaced
```


## [2026-10-15T02:47:36.599Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"طاووس|طاوس\" MON_part*.txt incoming/MON/*djvu.txt | head -15; grep -n -E \"سه تار|سه‌تار|سه.تار|گیتار\" MON_part*.txt incoming/MON/*djvu.txt | head",
 "description": "Grep Mo'in for tavus, setar, guitar"
}
```


### [2026-10-15T02:47:37.228Z] TOOL RESULT

```
MON_part1.txt:21254:(کد.) اشکك گلگون. بجچهٌ طاوس علوی: 
MON_part1.txt:30747:پرطاوس: 2۵۲5 آف. ع.] (امر.) نوعی 
MON_part1.txt:88990:موثق و عادل امامی باشند. (این‌ طاوس» لف.) 
MON_part1.txt:91059:کوب. آسیب. (مج.) کعبتین» طاوس» قرعه. 
MON_part1.txt:91927:طاوس فرهنگ فارسی مین ۷ "۱ 
MON_part1.txt:91933:طاوس: ۷5 (طاووس) [دراو بدی هندی] 
MON_part1.txt:91944:طاوس رابه‌عنوان یکث پرنده زینتی 
MON_part1.txt:91945:نگهداری می‌کنند. طاوس در سال ۴ تا ٩‏ 
MON_part1.txt:91950:می‌گردند. طاوس در حدود ۳۰ سال عمر 
MON_part1.txt:91951:می‌کند. غیر از طاوس‌های رنگین طاوس 
MON_part1.txt:91952:سفید ساده و طاوس آبی رنگ هم وجود 
MON_part1.txt:91955:ترکیبات اسمی: طاوس آیگون خضرا: ( کد.) 
MON_part1.txt:91956:طاوس آتشین بر: ( کد.) آفتاب. طاوس پران 
MON_part1.txt:91957:اخضر: (کد.) فرشتگان» ستارگان. طاوس 
MON_part1.txt:91959:غلمان. طاوس مشرق‌خرام: (کت.) آفتاب؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:18456:تار و سه تار و کمانجه و غبره. (گیا.) حقة 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:21963:کوچک و سه تار کرسی بزرگند و معمولا 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:37256:گیتار: 0و () (سه.) سازی است خوش‎ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:37300:گیتار 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:60807:عود طنبورء گیتار؛ ج. معازف. 
MON_part1.txt:30422:قیل تار و سه تار و غیره که‌دارای برده 
MON_part1.txt:33219:که بر روی کاسه تار و سازهای دیکر کشند. 
MON_part1.txt:43949:کو جک مانند سه تار دارد. 
MON_part1.txt:56105:چوبی» که روی کاسه تار نصب کنند و 
MON_part1.txt:75495:سه‌تار | (امر.) (مس.) سازی که در قدیم دارای
```


## [2026-10-15T02:47:40.108Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91925,91945p MON_part1.txt; echo ----; sed -n 75490,75500p MON_part1.txt; echo ----; sed -n 37254,37262p incoming/MON/MON_2vol_Adena_v2_djvu.txt; grep -n -E \"^ ?سه[: ]\" MON_part1.txt | head -5; grep -n -E \"طاوسی|طاوسان\" MON_part1.txt | head",
 "description": "Read Mo'in entries"
}
```


### [2026-10-15T02:47:40.594Z] TOOL RESULT

```
طاوس فرهنگ فارسی مین ۷ "۱ 


بز رگ حاد ثه عظیم) 
قیامت. 

طاوس: ۷5 (طاووس) [دراو بدی هندی] 
(.) (جان.) برنده‌ای است از راستة ما کیان‌ها 
که اصلش از هندوستان و مالزری است. دارای 
پرهابی زیبا است و صدایی بلند و تا حدی 


: طامات. (اح.) روز 


ناراحت کننده دارد؛ نر این برنده چتر زیبایی 
بادم خوو تسا ردب سشیببرهای زب 
طاوس رابه‌عنوان یکث پرنده زینتی 
نگهداری می‌کنند. طاوس در سال ۴ تا ٩‏ 
----
را قطع کنند» وی قادر به ترمیم آن می‌باشد و 
بازوی قطع شده نیز حیوان کاملی را می‌تواند 
بوجود آورد» ستارٌ بحری. 

ستاره: (6-)50272 [- استاره ‏ ستار - 
سه‌تار | (امر.) (مس.) سازی که در قدیم دارای 
سب سیم نو د۵. 

ستاره‌شناسی: -36025-.: (حامص.) 
اخبر مناسی) تجوم: 

----

۱ ۵ ٩ 
گیتار: 0و () (سه.) سازی است خوش‎ 
آهنگ که شش سیم دارد و اه کشت‎ 
و گاه با مضرات نو ازند.‎ 
کین 1 (۱.) جهان» عالم. عالم سفلی»‎ 
کرة زمین. آن گیتی: آخرت؛ آن جهان. این‎ 
این دنیا» این جهان. و کش زو‎ ۳ 
3 حهان؛ دو عالم» کونین. ( کد.) وضع‎ 
4885:سه معنی «آمیزنده) ات مردم آمیز» 
7103:سه حرف بش ندارد. 
16191:سه حرف است: ا؛ ۶ ب؛ پ» ت» ث» ج» 
25344:سه ستارة صف‌زده از هفت ستارهة بنات 
31605:سه روز پیش از دیروز. 
91967:طاوسی: -۱200 [سعر. ف.] (ص‌نسه.) 
91974:ممزوج بود. نوعی یاقوت طاوسی رنگ. 
91985:است. طاوسی به علت گل‌های زیبا و 
91989:برگ بنظر می‌رسد . گل‌های طاوسی از 
91991:زرد رنگ است. از شاخه‌های طاوسی
```


## [2026-10-15T02:47:44.723Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 91967,91992p MON_part1.txt | tr '\\n' ' '; echo; grep -n -E \"^سه‌تار|سه تار:|^سه: \" incoming/MON/MON_2vol_Adena_v1_djvu.txt | head",
 "description": "Read Mo'in tavusi entry"
}
```


### [2026-10-15T02:47:45.187Z] TOOL RESULT

```
طاوسی: -۱200 [سعر. ف.] (ص‌نسه.)  مسنوب به طاوس. سبز زرین» سبز  دینارگون. آنکه به چند رنگ زند. (.)  نوعی جامة رنگین. نوعی مروارید که    سفیدی او با سیاهی و سبزی و سرخی  ممزوج بود. نوعی یاقوت طاوسی رنگ.  (گیا.) گیاهی است از تيرة پروانه‌واران که  بصورت درختجه‌ای است که ارتفاعش به  حدود ۱/۵ تا ۲ متر می‌رسد و غالباً در کنار  جاده‌ها و اراضی سیلیسی و بایر اروپای  مرکزی و آسیای صغیر و ایران می‌روید. این  کیاه سافه‌های مستعدد و فراوان دارد.  شاخه‌های جوان آن زوایه‌دار و بی‌کر ک و به  رنگ سبز می‌باشد. گل‌هایش بزرگ و  و به رنگ زرد طلایی است. میوه‌اش  شجل نم و پوشیده از کرک‌های بان  است. طاوسی به علت گل‌های زیبا و  معطری که دارد به عنوان زینتی در باغچه و  اکثر باغ‌های اپران کشت می‌شود. . برگک‌های  آن کم است بطوری که ظاهرا گیاه عاری از  برگ بنظر می‌رسد . گل‌های طاوسی از  لحاظ شکل شبه گل‌های درخت اقاقیا ولی  زرد رنگ است. از شاخه‌های طاوسی  می‌توان الیافی جدا کرد و از آن طناب یا  
75495:سه‌تار | (امر.) (مس.) سازی که در قدیم دارای 
75706:سه: (6-)56۱12 [آرا.] 0( (گیا.) انگور. 
81543:سه تار: 48-ع» [- ستار - سه تا| (امر.) (مس.)
```


## [2026-10-15T02:47:49.566Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py",
 "description": "Read fetch_source usage"
}
```


### [2026-10-15T02:47:49.998Z] TOOL RESULT

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


## [2026-10-15T02:47:55.531Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://en.wiktionary.org/wiki/ταώς\" \"https://en.wiktionary.org/wiki/pavo\" \"https://en.wiktionary.org/wiki/peacock\" \"https://en.wiktionary.org/wiki/طاووس\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tréyes\" \"https://en.wiktionary.org/wiki/sitar\" \"https://en.wiktionary.org/wiki/guitar\" \"https://en.wiktionary.org/wiki/κιθάρα\" \"https://en.wiktionary.org/wiki/testis\" \"https://en.wiktionary.org/wiki/tribus\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrīz\" \"https://en.wiktionary.org/wiki/سه\" \"https://en.wiktionary.org/wiki/guitarra\" \"https://en.wiktionary.org/wiki/سه‌تار\" \"https://www.etymonline.com/word/peacock\" \"https://www.etymonline.com/word/guitar\" \"https://www.etymonline.com/word/sitar\" \"https://www.etymonline.com/word/testimony\" \"https://www.etymonline.com/word/tribe\" \"https://en.wiktionary.org/wiki/தோகை\" \"https://en.wiktionary.org/wiki/پاو\" \"https://en.wiktionary.org/wiki/tertius\"; do echo \"$u => $(python3 tools/fetch_source.py \"$u\" --note \"page 511, Tokei/Trei verification\" 2>&1 | tail -1)\"; done",
 "description": "Archive web sources for page 511",
 "timeout": 300000
}
```


### [2026-10-15T02:48:20.667Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/ταώς => /home/sfmqrb/git/rishe-private/data/verification/sources/web/1c43ead66d7a319b.txt
https://en.wiktionary.org/wiki/pavo => /home/sfmqrb/git/rishe-private/data/verification/sources/web/1e7c9013080c44aa.txt
https://en.wiktionary.org/wiki/peacock => /home/sfmqrb/git/rishe-private/data/verification/sources/web/bdf03f9395b7585a.txt
https://en.wiktionary.org/wiki/طاووس => /home/sfmqrb/git/rishe-private/data/verification/sources/web/9c30c8c93f423444.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tréyes => /home/sfmqrb/git/rishe-private/data/verification/sources/web/057ab9c0b2a4ac8c.txt
https://en.wiktionary.org/wiki/sitar => /home/sfmqrb/git/rishe-private/data/verification/sources/web/4f0007efba68ca07.txt
https://en.wiktionary.org/wiki/guitar => /home/sfmqrb/git/rishe-private/data/verification/sources/web/fb369480c8d82900.txt
https://en.wiktionary.org/wiki/κιθάρα => /home/sfmqrb/git/rishe-private/data/verification/sources/web/9fae7ffb1bbfef4b.txt
https://en.wiktionary.org/wiki/testis => /home/sfmqrb/git/rishe-private/data/verification/sources/web/731d59684859d6a0.txt
https://en.wiktionary.org/wiki/tribus => /home/sfmqrb/git/rishe-private/data/verification/sources/web/54f125ced8cc632b.txt
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrīz => /home/sfmqrb/git/rishe-private/data/verification/sources/web/253d07718379c184.txt
https://en.wiktionary.org/wiki/سه => /home/sfmqrb/git/rishe-private/data/verification/sources/web/774403a33fb41fee.txt
https://en.wiktionary.org/wiki/guitarra => /home/sfmqrb/git/rishe-private/data/verification/sources/web/a80eeeaefe2726d0.txt
https://en.wiktionary.org/wiki/سه‌تار => /home/sfmqrb/git/rishe-private/data/verification/sources/web/223810e93712a689.txt
https://www.etymonline.com/word/peacock => /home/sfmqrb/git/rishe-private/data/verification/sources/web/838b5757e76d2d4e.txt
https://www.etymonline.com/word/guitar => /home/sfmqrb/git/rishe-private/data/verification/sources/web/f57c28f3a4d9149f.txt
https://www.etymonline.com/word/sitar => /home/sfmqrb/git/rishe-private/data/verification/sources/web/2fe9b41983a0c372.txt
https://www.etymonline.com/word/testimony => /home/sfmqrb/git/rishe-private/data/verification/sources/web/87c1c0952f7df9da.txt
https://www.etymonline.com/word/tribe => /home/sfmqrb/git/rishe-private/data/verification/sources/web/87e6906438234759.txt
https://en.wiktionary.org/wiki/தோகை => /home/sfmqrb/git/rishe-private/data/verification/sources/web/64a619d67fcc0a6b.txt
https://en.wiktionary.org/wiki/پاو => /home/sfmqrb/git/rishe-private/data/verification/sources/web/3d9681270a6826c9.txt
https://en.wiktionary.org/wiki/tertius => /home/sfmqrb/git/rishe-private/data/verification/sources/web/2303b39172968337.txt
```


## [2026-10-15T02:48:24.067Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -22 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n  d=json.loads(l); print(d.get('status'),d.get('bytes'),d['url'])\"; W(){ grep -i -m3 -A6 \"^Etymology\" $1 | head -${2:-14}; echo =====; }; W 1c43ead66d7a319b.txt; W 1e7c9013080c44aa.txt 10; W 9c30c8c93f423444.txt; W 64a619d67fcc0a6b.txt 10",
 "description": "Check fetch status and read etymologies"
}
```


### [2026-10-15T02:48:24.716Z] TOOL RESULT

```
Exit code 1
200 17265 https://en.wiktionary.org/wiki/τέρπω
200 7991 https://en.wiktionary.org/wiki/κιθάρα
200 15386 https://en.wiktionary.org/wiki/testis
200 7294 https://en.wiktionary.org/wiki/Terpsichore
200 16125 https://en.wiktionary.org/wiki/tribus
200 5126 https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrīz
200 10896 https://en.wiktionary.org/wiki/Euterpe
200 7637 https://en.wiktionary.org/wiki/سه
200 18684 https://abadis.ir/fatofa/طرح/
200 17936 https://en.wiktionary.org/wiki/برادر
200 19269 https://en.wiktionary.org/wiki/guitarra
200 5072 https://en.wiktionary.org/wiki/سه‌تار
200 17252 https://abadis.ir/fatofa/ترور/
-1 39 https://www.etymonline.com/word/peacock
-1 39 https://www.etymonline.com/word/guitar
-1 39 https://www.etymonline.com/word/sitar
-1 39 https://www.etymonline.com/word/testimony
200 2386 https://en.wiktionary.org/wiki/தோகை
200 11857 https://en.wiktionary.org/wiki/پدر
200 8507 https://abadis.ir/fatofa/مطرح/
-1 39 https://en.wiktionary.org/wiki/پاو
200 6234 https://en.wiktionary.org/wiki/tertius
W: ==== not found
```


## [2026-10-15T02:48:27.539Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 1c43ead66d7a319b 1e7c9013080c44aa 9c30c8c93f423444 64a619d67fcc0a6b bdf03f9395b7585a; do echo \"=== $f\"; grep -i -A5 \"Etymology\" $f.txt | grep -v \"^\\s*$\" | head -14; done",
 "description": "Read peacock-related etymologies"
}
```


### [2026-10-15T02:48:27.879Z] TOOL RESULT

```
=== 1c43ead66d7a319b
 Etymology 
 1.3 
 Pronunciation 
 1.4 
--
 Etymology 
 2.2 
 Noun 
 2.2.1 
--
 Etymology
 [ edit ] 
 From an earlier *τᾰϝώς ( *tăwṓs ) , of Pre-Greek origin; possibly from an eastern source, perhaps from Dravidian (compare Tamil தோகை ( tōkai , “ peacock ” ) ) [ 1 ] or a Turkic source (compare Turkish tavuk ( “ hen ” ) ). Cognates include Latin pāvus , pāvō , and perhaps Hebrew טַוָּס ( ṭawwā́s ) , Aramaic טַוסָא ( ṭawsā ) , Arabic طَاوُوس ( ṭāwūs ) .
 Pronunciation
=== 1e7c9013080c44aa
 Etymology 
 1.2 
 Pronunciation 
 1.3 
--
 Etymology 
 2.2 
 Pronunciation 
 2.3 
--
 Etymology 
 3.2 
 Pronunciation 
 3.3 
=== 9c30c8c93f423444
 Etymology 
 1.2 
 Noun 
 1.2.1 
--
 Etymology 
 2.3 
 Pronunciation 
 2.4 
--
 Etymology 
 3.2 
 Pronunciation 
 3.3 
=== 64a619d67fcc0a6b
=== bdf03f9395b7585a
 Etymology 
 1.2 
 Pronunciation 
 1.3 
--
 Etymology
 [ edit ] 
 Etymology tree
 Pre-Greek bor. 
 Ancient Greek ταώς ( taṓs ) bor. ? 
 Latin pāvō bor. 
 Proto-Germanic *pāwô 
--
 Pages with etymology trees
```


## [2026-10-15T02:48:30.955Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E \"pāvō|Pre-Greek|imitative|Middle English|pēa|pawa\" bdf03f9395b7585a.txt | head -8; echo; grep -n -E \"From|Borrowed|Aramaic|Greek\" 9c30c8c93f423444.txt | head -12; echo; grep -n -E \"Latin|From|Borrowed|onomat|Greek\" 1e7c9013080c44aa.txt | head -10; echo; cat 64a619d67fcc0a6b.txt | head -40",
 "description": "Extract key etymology lines"
}
```


### [2026-10-15T02:48:31.347Z] TOOL RESULT

```
222: Pre-Greek bor. 
224: Latin pāvō bor. 
228: Middle English pe 
234: Middle English cok 
236: Middle English pecok 
239: From Middle English pecok , pekok , pocok , pacok , first component from Old English pēa , pāwa ( “ peacock, peafowl ” ) , ultimately from Latin pāvō ; equivalent to pea +‎ cock . Compare Old Norse páfugl ( “ peacock ” , literally “ peafowl ” ) , and English peahen , peachick , etc.
482: Latin: pāvō   (la)   m 
582: Lower Sorbian: paw   m , pawa   f ( female ) 

187: From Wiktionary, the free dictionary
199: Pre-Greek bor. 
200: Ancient Greek ταώς ( taṓs ) bor. 
201: Aramaic טַוסָא ( ṭawsā ) bor. 
204: Borrowed from Aramaic טַוסָא ( ṭawsā ) , borrowed from Ancient Greek ταώς ( taṓs ) .
417: Inherited from Arabic طَاوُوس ( ṭāwūs ) , borrowed from Aramaic טַוסָא ( ṭawsā ) , borrowed from Ancient Greek ταώς ( taṓs ) , borrowed from Pre-Greek .
443: Borrowed from Arabic طَاوُوس ( ṭāwūs ) , borrowed from Aramaic טַוסָא ( ṭawsā ) , borrowed from Ancient Greek ταώς ( taṓs ) , borrowed from Pre-Greek .
512: Categories : Arabic terms derived from Ancient Greek 
513: Arabic terms borrowed from Aramaic 
514: Arabic terms derived from Aramaic 
515: Arabic terms derived from a Pre-Greek substrate 
525: Moroccan Arabic terms derived from Aramaic 

108: Latin 
110: Toggle Latin subsection 
191: Latina 
262: From Wiktionary, the free dictionary
297: From Latin pāvō and Yiddish פּאַווע ( pave ) .
349: Pre-Greek bor. 
350: Ancient Greek ταώς ( taṓs ) bor. ? 
351: Latin pāvō 
354: Inherited from Latin pāvō .
379: Latin

URL: https://en.wiktionary.org/wiki/தோகை
FETCHED: 2026-10-15T02:48:19Z
STATUS: 200
TITLE: தோகை - Wiktionary, the free dictionary

தோகை - Wiktionary, the free dictionary 

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
```


## [2026-10-15T02:48:33.732Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E \"peacock|tail|Etymology|Dravidian\" 64a619d67fcc0a6b.txt | head; for f in 1e7c9013080c44aa; do sed -n 380,420p $f.txt | grep -v \"^\\s*$\" | head -15; done",
 "description": "Read Tamil tokai and Latin pavo entries"
}
```


### [2026-10-15T02:48:34.087Z] TOOL RESULT

```
154: tail of a peacock 
157: peacock 
160: tail of an animal 
 [ edit ] 
 pāvō 
 Etymology
 [ edit ] 
 Likely borrowed from Ancient Greek ταώς ( taṓs , “ peacock ” ) , or possibly imitative (compare paupulō ( “ to call like a peacock ” ) ).
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈpaː.woː] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈpaː.vo] 
 Noun
 [ edit ] 
 pāvō   m ( genitive pāvōnis ) ; third declension 
 peacock , peafowl ; a bird associated with Argus and sacred to Hera or Juno ; eaten as a delicacy.
 8 CE , Ovidius , Fasti 6.177 : et praeter pennās nihil in pāvōne placēbat and, besides the feathers, nothing in the peacock was pleasing 
(In other words, an ancient time before the bird was considered a delicacy .)
```


## [2026-10-15T02:48:37.559Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 057ab9c0b2a4ac8c 4f0007efba68ca07 fb369480c8d82900 9fae7ffb1bbfef4b a80eeeaefe2726d0 223810e93712a689 774403a33fb41fee 253d07718379c184; do echo \"=== $f $(sed -n 1p $f.txt)\"; grep -n -E \"From |Borrowed|Inherited|borrowed|Avestan|Sogdian|Old Persian|Proto-Iranian\" $f.txt | head -8; done",
 "description": "Read three/sitar/guitar etymologies"
}
```


### [2026-10-15T02:48:37.924Z] TOOL RESULT

```
=== 057ab9c0b2a4ac8c URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tréyes
139: From Wiktionary, the free dictionary
=== 4f0007efba68ca07 URL: https://en.wiktionary.org/wiki/sitar
316: From Wiktionary, the free dictionary
335: From Hindi सितार ( sitār ) / Urdu ستار ( sitār ) , from Classical Persian سه‌تار ( si-tār , literally “ three strings ” ) . [ 1 ] [ 2 ] Doublet of setar .
450: Proto-Iranian *θráyah 
451: Old Persian 𐏂 ( ç ) 
1217: From Persian سه‌تار ( se-târ ) , meaning “three strings”.
1251: Proto-Iranian *θráyah 
1252: Old Persian 𐏂 ( ç ) 
1262: Borrowed from Hindi सितार ( sitār ) .
=== fb369480c8d82900 URL: https://en.wiktionary.org/wiki/guitar
271: From Wiktionary, the free dictionary
301: From Spanish guitarra , from Arabic قِيثَارَة ( qīṯāra ) , from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) . Doublet of cithara , cither , and zither , but not related to sitar .
743: From guit +‎ -ar .
1079: English terms borrowed from Spanish 
=== 9fae7ffb1bbfef4b URL: https://en.wiktionary.org/wiki/κιθάρα
189: From Wiktionary, the free dictionary
=== a80eeeaefe2726d0 URL: https://en.wiktionary.org/wiki/guitarra
337: From Wiktionary, the free dictionary
381: Borrowed from Arabic قِيثَارَة ( qīṯāra ) . Doublet of cítara and cistre .
425: Inherited from Old Galician-Portuguese guitarra , borrowed from Arabic قِيثَارَة ( qīṯāra ) , borrowed from Aramaic קיתרא ( qīṯārā ) , borrowed from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) , from Pre-Greek . Doublet of cítara and cítola .
496: Borrowed from Spanish guitarra .
522: Borrowed from Arabic قِيثَارَة ( qīṯāra ) . Doublet of cítola .
569: Borrowed from Arabic قِيثَارَة ( qīṯāra ) , borrowed from Aramaic קיתרא ( qīṯārā ) , borrowed from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) , from Pre-Greek . Doublet of cedra .
614: Inherited from Old Galician-Portuguese guitarra , borrowed from Arabic قِيثَارَة ( qīṯāra ) , borrowed from Aramaic קיתרא ( qīṯārā ) , borrowed from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) , from Pre-Greek . Doublet of cítara , cítola , and cistre .
704: Inherited from Old Spanish guitarra , borrowed from Arabic قِيثَارَة ( qīṯāra ) , borrowed from Aramaic קיתרא ( qīṯārā ) , borrowed from Ancient Greek κῐθᾰ́ρᾱ ( kĭthắrā ) , from Pre-Greek . Doublet of cítara , cítola , and cedra .
=== 223810e93712a689 URL: https://en.wiktionary.org/wiki/سه‌تار
138: From Wiktionary, the free dictionary
154: Proto-Iranian *θráyah 
155: Old Persian 𐏂 ( ç ) 
163: From سه ( si  / se , “ three ” ) +‎ تار ( tār  / târ , “ string ” ) .
=== 774403a33fb41fee URL: https://en.wiktionary.org/wiki/سه
199: From Wiktionary, the free dictionary
244: From Proto-Iranian *cáywaH 
266: Inherited from Middle Persian [script needed] ( sh /⁠sē̆⁠/ ) , from Old Persian *çayaʰ , from Proto-Iranian *θráyah , from Proto-Indo-Iranian *tráyas , from Proto-Indo-European *tréyes .
268: Indo European cognates include Avestan 𐬚𐬭𐬌- ( θri- ) , Northern Kurdish sê , Pashto درې ( dre ) , Sanskrit त्रि ( tri ) , Greek τρεις ( treis ) , Italian tre , English three , Latin trēs , French trois , Spanish tres , etc. False cognate of Korean 세 ( se ) .
424: Mazanderani terms inherited from Proto-Iranian 
425: Mazanderani terms derived from Proto-Iranian 
430: Persian terms derived from Old Persian 
431: Persian terms inherited from Old Persian 
=== 253d07718379c184 URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/þrīz
138: From Wiktionary, the free dictionary
148: From earlier *þreiz , from earlier * þrejiz , from Proto-Indo-European *tréyes ( “ three ” ) . [ 1 ]
```


## [2026-10-15T02:48:43.484Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -A3 -E \"^ Etymology$\" 9fae7ffb1bbfef4b.txt | head -8; grep -n -E \"Avestan|Sogdian|Old Persian|Latin|Germanic\" 057ab9c0b2a4ac8c.txt | head -20; for f in 731d59684859d6a0 54f125ced8cc632b 2303b39172968337; do echo \"== $f\"; grep -n -A3 -E \"^ Etymology( 1)?$\" $f.txt | grep -v \"^\\S*-\\s*$\" | head -6; done",
 "description": "Read kithara, PIE three, Latin pages"
}
```


### [2026-10-15T02:48:43.805Z] TOOL RESULT

```
199: Etymology
200- [ edit ] 
201-
202- According to Beekes, acquired from Pre-Greek . [ 1 ] Said Pre-Greek term may be ultimately derived from or at least related to Proto-Hurro-Urartian *kinnar ( “ lyre, harp ” ) .
--
342: Etymology
343- [ edit ] 
344-
444: Proto-Germanic: *þrīz ( see there for further descendants )
== 731d59684859d6a0
289: Etymology
290- [ edit ] 
292- Learned borrowing from Latin testis .
341: Etymology
342- [ edit ] 
344- Learned borrowing from Latin testis ( “ testicle ” ) .
== 54f125ced8cc632b
275: Etymology
276- [ edit ] 
278- From Latin tribus ( “ tribe ” ) .
290: Etymology
291- [ edit ] 
293- From Latin tribus . Doublet of tribe .
== 2303b39172968337
198: Etymology
199- [ edit ] 
201- Etymology tree
```


## [2026-10-15T02:48:46.513Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E \"tri-st|terstis|\\*tri|Umbrian|trifu|three\" 731d59684859d6a0.txt 54f125ced8cc632b.txt 2303b39172968337.txt | head -12; sed -n 400,470p 057ab9c0b2a4ac8c.txt | grep -v \"^\\s*$\" | head -40",
 "description": "More Latin and PIE detail"
}
```


### [2026-10-15T02:48:47.158Z] TOOL RESULT

```
731d59684859d6a0.txt:388: For *terstis , from Proto-Italic *tristos , from Proto-Indo-European *tristh₂s ("a third party standing", after the two parties to a contract or dispute), from *tréyes ( “ three ” ) and *steh₂- ( “ to stand ” ) . Compare Oscan trstus ( “ witnesses ” , nominative plural ) . [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] 
2303b39172968337.txt:204: Proto-Indo-European *tri- 
2303b39172968337.txt:208: Proto-Indo-European *tritós 
2303b39172968337.txt:209: Proto-Italic *tritios 
2303b39172968337.txt:212: From Proto-Italic *tritios , from Proto-Indo-European *tr̥tyós ~ *tritós , ordinal form of *tréyes . Akin to Ancient Greek τρίτος ( trítos ) , Proto-Germanic *þridjô and Proto-Slavic *tretь .
54f125ced8cc632b.txt:1046: An old compound from the stem of trēs ( “ three ” ) , cognate with Umbrian 𐌕𐌓𐌉𐌚𐌖 ( trifu ) . Either from: [ 1 ] [ 2 ] 
54f125ced8cc632b.txt:1048: Proto-Italic *triðus if from Proto-Indo-European *dʰeh₁- ( “ to put, place, set ” ) , thus Proto-Indo-European *tri-dʰh₁-o- ( “ rendered in three, tripartite ” ) but changed to a u -stem; cf. with Skt. multiplicatives in -dhā such as Sanskrit त्रिधा ( tridhā , “ threefold ” ) , and with other derivatives such as Lithuanian iñdas ( “ dishware ” ) < *h₁n̥-dʰh₁-o- . This would be evidence to the development of PIt. *þ before vocalic *u as after it;
54f125ced8cc632b.txt:1050: Proto-Italic *triβus if from Proto-Indo-European *bʰuH- ( “ to grow, become, come into being, appear ” ) ; in that case, the u -suffix was originally part of the root.
54f125ced8cc632b.txt:1052: Originally referring to three divisions of the (Roman) people. Cognate to Umbrian trifu ( “ tribe, people ” ) .
54f125ced8cc632b.txt:1059: One of the three original tribes of Rome: Ramnes , Tities , Luceres .
54f125ced8cc632b.txt:1204: Inflected form of trēs ( “ three ” ) 
 —
 *trisú 
 instrumental
 —
 —
 *trimís , *tribʰís 
 Derived terms
 [ edit ] 
 *tri- ( compounds ) 
 *trís 
 *tritós ~ *tr̥tyos 
 Descendants
 [ edit ] 
 Terms derived from the Proto-Indo-European word *tréyes 
 Proto-Albanian: *treje ( see there for further descendants )
 Proto-Anatolian: *trḗs 
 Hittite: 𒐈𒂊𒌍 ( 3-e-eš /⁠*teriyēs⁠/ ) , [script needed] ( teri-janna- , “ the third time ” ) , [script needed] ( tri- ) 
 Lycian: 𐊗𐊕𐊁𐊆 ( trei ) 
 Luwian: 𔑰𔖱𔓯 ( tara/i- ) 
 Milyan: 𐊗𐊕𐊆- ( tri- ) 
 Proto-Armenian: 
 Old Armenian: երեք ( erekʻ ) Armenian: երեք ( erekʻ ) 
 Proto-Balto-Slavic: *tríjes ( see there for further descendants )
 Proto-Celtic: *trīs ( see there for further descendants )
 Proto-Germanic: *þrīz ( see there for further descendants )
 Proto-Hellenic: *tréyes ( see there for further descendants )
 Proto-Indo-Iranian: *tráyas ( see there for further descendants )
 Proto-Italic: *trēs ( see there for further descendants )
 Messapic: [script needed] ( tri- ) 
 Phrygian: θρί- ( thrí- ) 
 Proto-Tocharian: *treyä [ 1 ] ( see there for further descendants )
 See also
 [ edit ] 
 Proto-Indo-European cardinal numbers from 1 to 90
 —0
 —1
 —2
 —3
```


## [2026-10-15T02:48:52.389Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Root /lemma: trei|^trei\" POK_full.txt | head; grep -n -i -E \"θrisat|ϑrisat|ϑrisąs|ϑrida|θrida|ϑrī\\.|ϑriϑ|θriθ|ϑrāyō|ϑrāy\" BRT.txt | head -20",
 "description": "Grep Pokorny and Bartholomae for three"
}
```


### [2026-10-15T02:48:52.828Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:48:55.474Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"trei-|tréyes|trejes\" POK_full.txt | head; grep -n -E \"Page\\(s\\): 1090\" POK_full.txt | head; grep -n -E \"[θϑ]risa|[θϑ]rida|[θϑ]rāyō|[θϑ]ri[θϑ]a|thrisa\" BRT.txt | head -20",
 "description": "Search Pokorny, Bartholomae variants"
}
```


### [2026-10-15T02:48:55.946Z] TOOL RESULT

```
82334:B. strei-, steri-: 
82514:Note: also stere-. stre- strei-, streu-, with g, b, d^ (or /) extended; identical with ster- 
86018:Latin tero, -ere, trTvT, trTtum^rub, grind ', the prefixed present forms from the basis trei-, 
86031:from the same basis trei-, tn- {as trMetc.) Middle Irish /Ae///? "weak', and gr. rplpw 
87142:Root / lemma: trei- 
87182:drittoeic; Lithuanian trecias, Latvian /resa/s (//le- instead of //> after *trejes'7 also:) Old 
87567:lemma: trei-\ "three' tris-no-\x\ gr. GpTva^ "trident, three pronged weapon of Poseidon'.) 
87210:Page(s): 1090-1092
```


## [2026-10-15T02:48:57.515Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 87142,87212p POK_full.txt | cut -c1-260",
 "description": "Read Pokorny trei entry"
}
```


### [2026-10-15T02:48:57.904Z] TOOL RESULT

```
Root / lemma: trei- 
Meaning: three 

Grammatical information: Nom. m. tre/es, Nom. Akk. n. tn, Akk. n. trins, f. tis(o)res, 
(dissimil. from *tris(o)res, etc.) 

Material: 1. Old Indie trayahm., tn, newer tnniu., tisrahi.; Avestan &rayd, ^rayasm., &ri 
n., tisroi.; Armenian erek {treies); gr. Tp£T(;, gort. Tpee(;, m. f., alb. tre, f. //v' (originally 
neutrales *tn)\ Latin /res (Akk. also tns), tr/a{tn-'\n tn-g/nfa' 30'), Oscan tr/s 'ires', Umbrian 
tr/f, tref, f\kk. "tres', triia'\x\a'; Old Irish tri, f. teoir, Akk. teora {* tisoras, *tri-sor-ns); cymr. tri 
m., tairi., mcymr. bret. teir {*tedres < *tisres, das e after the Vierzahl), compare gall, tidres 
(?); Gothic t^reis, Akk. I=>rins, n. Mja, Old Icelandic t^nr. Old High German dnetc; Old 
Prussian tr/s {Gen. treon), Lithuanian trys, Latvian tns{n. tr/"\n Lithuanian try-lika 
"dreizehn', compare Latin tn-ginta'ZO'); Old Church Slavic trijeru. and trii. n.; Hittite tri- 
'drei'; Tocharian A trexr\., tri- f., B fra/m., taryat 

composition form ///-in Old Indie tripad-, gr. rpinouq, Latin tripes. Old English drifete, 
Lithuanian //7/rQ^/s'dreifuftig'; Avestan z?/7-/ra/77a/'a^5-'dreikopfig', Armenian ere-am'6re'\ 
years old'; lllyrian PN Tpi-Tsura, PN Tpi-Kopviov; Celtic PN Tri-toutos, gall. tri-garanus'W\Vc\ 
drei Kranichen'; Old Irish tri'ar'6re\ man' {*tri-uirom); russ. -Church Slavic trb-gub'b 
"dreifach' (= Lithuanian tri-gubas6s); perhaps Latin //7Z?^5 "dividing off, partitioning off of 
people, administrative district ', Umbrian trifu, tr/fo Akk. Sg. from *tr/-b^u-{to *b'^eu-aboye 
S. 146); Latin frfgat 'Dreigespann' (shaped after t>rgaeP\. "Zweigespann' from *t>Hugae, 
see above S. 230 and 508); unclear Old Irish //'e-//7e/7c'Dreiheit' besides Middle Irish de- 
cheng 'ZweWneW, compare Old Icelandic Mdjungr' DntteV; 

'dreizehn': Old Indie trayodasa-= Latin tredecim {*tres-decim); compare gr. rpsK^-Kai- 
5£Ka; 

"dreiftig': Old Indie trfmsat-t, Avestan ^risat-, gr. rpiaKOvra, Latin trf-ginta. Old Irish 
*trTcho, Gen. trTchot {* trhkomtos). Middle Irish trfcha, bret. tregonf{6as efrom trede 
"dritter'), gall. Abl. PI. tricontis, Tocharian A taryak, B taryaka ( *trliaRnt-s). 



2. ordinals: altererbt Old Indie tr-ffya- = Old Prussian tfrts, otherwise is //> for tr- 
eingetreten: Old Indie PN Tr/ta-, Avestan ^r/'ta-, Avestan &ritya-. Old pers. &ritiya-ox -tTya; 
Armenian erir, errord, gr. TpiTO(;; homer. TpiraTOc; extended as £p56[jaTO(;; Lesbian Tsproc; 
from *TpiTO(;; alb. trete, lllyrian PN Tritus, Latin tertius, Umbrian tertiu^X.erWd', /e/Y/"tertium' 
(from *tritio-)\ gall. PN Tritios, cymr. try-dydd, bret. trede; Gothic Mdja, Old High German 
drittoeic; Lithuanian trecias, Latvian /resa/s (//le- instead of //> after *trejes'7 also:) Old 
Church Slavic tretijb; Baltic trit- in Lithuanian //7/a//7/5"Dritter; 

Old Irish tress {ne\Ner triss) 'the Dritte' {*tristo-), //'e(/)sse'triduum', compare Latin testis 
' witness, testifier ' (also "testicle'); Ablat. Oscan trfstaamentud\s probably from Latin 
testa mentum borrowed; 

Tocharian B trit, Hittite tarriianaiii-^ihe dritte', fte-rij-ia-an-na' 6ntter'. 

3. tris' thrice, three times ': Old Indie tr/h, Avestan ^ris, gr. Tpi(;, Latin ter, older terr 
(from *tr/s), Old Irish fo-tiirf thrice, three times '; extended Avestan &rizvaT thrice, three 
times ', Old Icelandic Msvar, Old High German driror. Old English driwa, dreowa ds.; ein 
uo-suffix also in Avestan &risva- n. "Drittel' and gr. GpTov Teigenblatt' from *TpiaFov; in 
addition *tris-no-\v\ gr. GpTva^ 'Dreizack'; Latin terni {*tri-no-) "je drei' (besides trmiby PI. 
tantum from *tris-no- parallel with bmi, see below dudu). Old Icelandic A'/'e/7/7/''dreifach', 
t^renner' dxQ< (by Kollektiven); 

Maybe alb. tresh, trish^\v\ three' 

auf *//7a/7c>A7goes back Old Irish tr'i'an, acymr. trean, cymr. traean^Dn{{e\\ compare also 
gall. Akk. PI. //75/7/s' Drittel'? 

4. collective treio-, tmio-:0\6 Indie traya- '6re\fach', trayamn. 'Dreiheit', Lithuanian treji, 
f treJos^dre\' (by Pluralsubstantiven), Latvian treji, f. trejas6s., Old Church Slavic trq/im. 
PI.; aui * treiodio- based on Old Irish //-eoofe 'dreifach'. 

References: WP. I 753 f., WH. II 668 f., 702 f., Trautmann 327 f., Vasmer 3, 137, 
Wackernagel-(Debrunner) 3, 346 f. 
Page(s): 1090-1092 

Root / lemma: trek-
```


## [2026-10-15T02:49:01.776Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"risa[tf]|rida[sś]a|ri[dθϑ]atr|ridasa|riSa\" BRT.txt | head -15; grep -n -i -E \"^ *ϑr|^ *&r|^ *thr\" BRT.txt | head -5",
 "description": "Grep Bartholomae for thirty, thirteen"
}
```


## [2026-10-15T02:49:04.226Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Lexicon|^tri-|^ç[i]|çitiya|ϑritiya|θritiya|çiš|çi-\" KNT_full.txt | head -10; grep -n -E \"^ *(sih|sē|se|sīh|sizdah|sēzdah)\\b\" PHD_mackenzie.txt | head; grep -n -E \"three|thirty|thirteen\" PHD_mackenzie.txt | head",
 "description": "Grep Kent and MacKenzie for three"
}
```


### [2026-10-15T02:49:04.710Z] TOOL RESULT

```
804:107 Lexicon and Concordance 164; Numerals 
858:H. C. Tolman, Ancient Persian Lexicon and Texts 
993:Н. C. Tolman, Ancient Persian Lexicon and Texts, 
1358:Tm. Lex. = Tm. Ancient Persian Lexicon and 
1800:and in the Lexicon, s.vv.: 
2792:Lexicon: 
2926:arašaniš, Skt. arainí-; see also Lexicon. 
2947:vazraka, a disputed word; see reff. in Lexicon. 
3091:Elam., Akk., Gk. transcriptions in Lexicon; 
3278:given at the end of the Lexicon, where their oc- 
4544:se-pay [3-p)d I N sipa] three-legged.
4546:se-Aabag [3-fph l ] three-night-Iong, trinoctial.
4553:sih [30 I M syh, N si] thirty.
9309:sih:-l, tOI                      ;>    ranJcn~, rozcn~                   -t"C;~
255:fl. A represents the capital form of ) (>iilep). There are three
4535:s~ [3; TLTA < A tit' 1M sh, N si] three.
4544:se-pay [3-p)d I N sipa] three-legged.
4546:se-Aabag [3-fph l ] three-night-Iong, trinoctial.
4549:sezdah [syedh I M syzdh, N .......] thirteen.
4553:sih [30 I M syh, N si] thirty.
7755:tasteless abemizag.                       thirteen sezdah.
7757: Taurus Gaw.                              thirty sih.
7768:tender nazuk.                             three se.
7769:tendon pay.                               three-legged sepay.
```


### [2026-10-15T02:49:04.753Z] TOOL RESULT

```
3112:rim  stagr»m  (sd.)  arijö  V,  7. 41;  43'; —  uitraAe  k?hrpa  °yehe  P.^2;  —  aspahe paiti  arshö  °yehe  "um  einen  Rosshengst erster  Qualität"  V.9.37;  37';  —  dvada- satih£ir3m  (sd.)  asti  "rim  ayan  F.  27  b; '";  —  'krisatdkw)m  frasnütse  .  .  "yqtn paiti  usnaitJm  ".  .  (also)  mit  Abwaschung erster  Ordnung"  V,  Ä  98  (?) '' ;  —  mi>nm  . . taxm?m  mainyaam 'rJmYtw.i 40.  [P. 32:  lies  ayryö.mdaimasl°.'\
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4916:•  j,  ayäOrima-  m.  Name  der  Gottheit der  vierten  Jahreszeit  und  des  an  deren Ende  gefeierten  fünftägigen  Fests**  (mit dem  letzten,  30.  als  Haupttag) ;  °m»m/ra- ourvaihrimim  (sd.)  * varlnihar!t)mla  (sd.) asavatwm  alahe  ratüm  Vr.  2.  2;  Y,3.9;  — °make  'itrimaAe'a  'staheSa  Vr. /.  s;  A.j. j;  —  'mSi  'hrimsi  'siaica  Y./,9J  — tüiryeheca  nä  myazdakt  ddäiti  (sd.)  . .  yat 'maAeA.3.10;  —  "äirisatim  "mähe  ftW^rahe anayranqm  "30  [Tage  sinds  bis  zum (Hauptjtag]  des  A.  [ira  Monat]  des  M, [am  Tag)  des  ewigen  Lichts"  A._j,  10,
5683:PPA.,  aus  *arfsya-  Praes.  a;.  —  ai.  Ir/yali  'et beneidet'.  —  Vgl.  ataska-,  iriSay  und  BTHL. IFAni.Ä  13,  Hbm.  lFAni..f/.SS,  FroehdeBB, 20.  186. —  Pü. ;  undeull-.  So.;  achedani  kurii. j.  airiyq  N.  6/;  lies  irisyq.
5841:uta  ärvh  "ppm  *isaiii  Aog.A'a;  —  ^risattm upstananqm  (Stverz.)  upäzsit  'pahe  aStraya \.4. 19, usw.;  —  'paecafaiti  vTraica  Yt/O. 101 ;  —  'palsu  vJraSsu  Yt  1$.  53;  —  'pa  ' (NP.)  hubaräita  (sd.)  rai:a  kvasäna  VyL , 4.V;  —  äiuica  'ps  dirizrasca  *väsö  YL '3-  S^'<  —  i^^  '"•^  'pake  vansa  (sd.) Vd-j;  S,  N.jt*;  —  ^iüirya  payh{iA.)  .  . 'paySatca  *xarayäatca  H.6^;  —  °paya (GS.)  paurvöMzya  (sd.)  ar^jS  N.  <?5;  — •/kJ  «r/a  (sd.)  Yt  74-  31.  39,  'Ö-  10;  — "/.?Ä^  paiii  arsriiJ  (sd.)  ayryehe  V.  <?,  37; /4.11;  —  jtfil'w  'panam  arsnam  Yt.  5. 21;  V.  22.  20;  —  'pä  (ISf.)  -/äsv«  (sd.) ar.>p  "um  den  Preis  für  eine  Rossstute" V.  ^,  4a;  —  Aasannm  "panqm  (GPf.) , daZimnqm  (sd.)  paiti.puiiranqtit  A,  _J.  9; —  'p5  ayryöJimö  datihve  varnnanö  *a^la gai-qm  asinqin  aryd  "das  edelste Ross  aus  der  Auslese  eines  Landes  hat den  Wert  von  acht  trächtigen  Kühen" F.jh.         [N.J7.-  lies  iar3.asps.]
7026:frabarfm  .  .  ä-  yimai  xia^räi  '^risatö.- zima  *hsnjas3iita  3°  he  Tm  zä  bvat  p>r3tt4 .  .  3°  yimäi  paiH.va&ialm  .  .  ä'  yimS  fra- Säsat  .  .  ä°  yimS  imqm  zqm  vilsvayat  V. 2.2— 11;  —  3ai  (s.  2)  aoxta  ahurö  masda yim3i  .  .  avl  ahüm  .  .  *s)mS  jatthintu  .  . ä"'  t3m  var?m  kirinava  . .  ä'  masta  yimö ..  ä'  aoxta  ahurö  mazäh  ..  3' yimö  avä^a k»r3tiaot . .  ä°  yimö  vanm  kir?naoi .  .ä°  .. V.  2.22-33;  —  äai  (s.  8)  .  .  mtrr^S  yö farödari  .  .  äürö  vahm  surunaoiti  ä°  .  . fraävaraiti  bBsyqsta  FrW.;o.4if.;  —  tat x^annö  apata^at  .  .  3'   us.patat  frat»rase
7235:ahüm  fraparayeni  .  .  3  vakistat  atfhaot  a . .  as3t  a  . .  raocSby3  '^.ig.6. '  b)  zeit- lich :  fravasayS  . .  ya  kaca  gayät  marp^nat 3  saosyaHtät  vfrsiiraynat  Y.  s6. 10;  — pu^rS . .  apara.itCbintS  *3  d3tai'*^  vii3taot (sd.)  Yl/^.  II,  22,  28; —  apam  ..fratiS .. kaca  hü  vaxi'at  ä  ^An'^'  frasml!.datsit pairisafaiH  '^.48;  Yt5.9r,  V.  y.i;  — a  tnaiiyat  xlapat  N.  50, 46;  —  a  darr/at :^3Miry3l  (sd.)  Y.O'0.6;  —  vTsp^m  3 ahmai  sbes.  c)    'in,    bei',   räumlich:
7254:frabanm  .  .  ä'  yimai  xia'irai  "iirisats, zima  *Amjas?nta  il'  he  tm  za  bvat  psnne .  .  ä°  yim3i  paüi.vaäiaim  . .  ä'  yimS  fra- sBsaJ  .  .  ä°  yimS  tmam  zam  vlsSvaya^  V. 2.2— 11;  —  äat{s.2)  aoxla  ahurö  mazdä yimäi  .  .  avi  ahSm  .  .  *z3m5  Janhtntu  .  . 3°'  t>m  var?m  kgnnava  . .  ä°  mqsta  yimS . .  3°  aoxta  aAurS  mazdä  . ,  S°  yimS  ava'^a kinnaot . .  ä°  yimö  var)m  k^rmaot .  .ä° . . V.2.22-33;  —  3at  (s.  8)  .  .  mjrr/ff  y5 paröJari  .  .  airö  väbm  surunaoitt  3°  .  . fradvaraiti  büsyqsta  FrW./o.4if.;  —  tat y^arjnd  apatacat  .  .  ä°   us.patal  franrase
8263:(LS.)  paoiryäi  nisasta  %risat^m  upäsana- nqm  upäiSit  "für  die  erstmalige  Begattung, für  die  erstmalige  Beschlafung  soll  er  .'." V.J6-.IS.
8421:•  j.  upäzana-  n.  'was  Jemandem  als  Busse zudiktirt  wird,  körperliche  Abstrafung, Hieb':  ka  hs  asti  (li-al  .  .  panca  'na aspahe  aSttaya  panca  sraosJ.caranaya ".  .  fünf  Hiebe  mit  der  Pferdepeitsche, fünf  mit  dem  Zuchtriemen"  V. 4. 18;  18, 18  ("10,  15  Hiebe");  —  ^risat^m  'nanqm upäzsit  (sd.)  aspahe  astraya  'irisatim sraosS.caranaya  ". .  30  Hiebe  . ."  V.^.19; 19,  19.  19-20,11,  6.21,^.36,4.12,13, Mi  15.  J'37,  H--i  {dRn.  "50,  70,  90,  200,
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
8565:td^w^m  frasnat!e{sd.)  ürisataüw^m  upa- srt'We  ayiyqm  (sd.)  paiti  'snäitimV.S.qZ.
10069:kommen,  (zeitlich)  voll  werden':  äat  yimäi xiairai  *'^risat5.%3ma  *ijnjaspnta's>  "aad dem  Reich  des  Y.  wurden  dreihundert Winter  voll"  V.  2. 8;  —  aü«  vlsp:>m  .7 ahmat  yat  hs  hanjasaili  (cäiirmum  yari) "(und)  so  bis  dahin,  dass  ihm  ein  Viertel- jahr voU  wird"  N,  42;  43.  4)  'angehen, sich  wenden  an  — '  (Akk.),  Med.;  t^m r^ra  hanjasante  * ma>ir3m.sp?nt3m.balsaz3m (sd.)  V.7.44.
11733:manS,  vehu  manS  taj  vanaiti  Yt. /p.  96;  jA'w.;  hazannm  azinqm  .  .  ava.janyät .  . —  parä  .  .  *daiahSui  anhat  b?r3t5  (sd.)  ■  "hrisattm  frascimbananqm  frasHmbaySit ..; vSstrvm:  ttm  {ah  ASn.)  aß paurvavazai-'tat  aiAhe  aiti  paititil  tat'  ..V.  18.1  ^Z.; lyai  (sd.)  V.  2. 24;  —  hixrsm  .  .  ast^m  .  .'P.4j;  — asavamm  . .  ajyei^yai  mraomt..; aaÄai^Tm  .  .;  ta  (APa)  hdhra  frafrS-^  tat  zl  vatiks  Y.7/-13;  —  dazdi  m!  ydka vayaAi  y.S.16;  —  hixr?m  .  .  aslim  ....  mjanani  ..  dahat  ahmäi  ..  ya;%a  ta aishaihim  .  .;  ta  (APn.)  Aa'hra  /ra/rä-'(]S.)upauha(at\t.i5.^t; — iviqm  iainitiS vaySmi;  ti  (statt  NPn.)  kiitmti  yzary.-  \ . .  failySnte  . ,;  tarn  tä  (AP.)  aiibys  .  . yiarmtts..  V.5,i8£;  —  a%ra  ml  urvarä'.msirinavahi  Yt5.87;  —  yB  dim  *fra- raöhnü  vTspä  ,.;  ta  (statt  APf.)  ha%ra  hinan  {sA.)..,  anairyanqtn  tai  dahytmqm vJvärayemi^ . 5.  \^i.;  —  vTspanqm  narqm\vfrihrai  uzjasaiti  N.ffff;  —  agtmanqmat ..  vispanqm  gSus  sar^anqm  . .;  //(ADf.)'*'.  .  vazyail {sA.)  . .  ratSui  nmStum  fi-anäia- larpnava  müwaireisd.)  ..  V,2.27f.;  — 'yatayezi  tajyayata  naväj  tatyayata(sd.) mit  Numeniswechsel:  jahi  . .;  tisca  t^A-j.s;  s\  s',  4';  —  ym  i^  (tiDxi.)  yaf- mraomi  jq%wS.lara  ..  V.i&öa— 65;  — '  tatary  {sd.) 'S.  4  g;  —  ASn.  in  kollektivem "mi^rS.ao/anAs  ..  yatcit  vlmaiiim  (sd.)  Smo:  umarä  baiiazyä ..,- tat  vlsp^m /rTttä- ai^ha  s3mS,   t»mSt  tnihrS  hangrp/simnS  mahi,  tat'  vuppm'  . .  V,  20.  4£  a)  in
13924:'fesseln  sva.  einschränken,  Einhalt  tun';  I''''^''"'? ''"«^'' *'i'«^'''^(s'i-)*''«''"'-'i'''?"' m  aihms  «r'>  dyätam  (3SIM.,  in  pass.  1  "■  ■  zwölf.."  F.27a;  —  cäkwarasca  ai,a Sinn)  paia  nmim  pattz^*  *sysdäm  (sd.)  k'^'IVi'  ca^warisatimla  (sd.)  dvaila  (Nn.) y.  ^.  j.  \saite  dvatca    kaza»re  Yt.ig.-j;    —    duye
10312:Thron',  arm.  LW,  gaA.   —   PQ.:  gäk  (geschr.
```


## [2026-10-15T02:49:10.194Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"dreizehn|dreisaitig|dreisait|dreisaitig|'drei'|„drei“|Kard\\. .drei\" BRT.txt | head -10; grep -n -o -E \".{150}(Drei|drei)saitig.{150}\" BRT.txt | head",
 "description": "Search Bartholomae for 'drei' glosses"
}
```


### [2026-10-15T02:49:10.673Z] TOOL RESULT

```
14500:•  j.  ftray-  Zw.,  fem.  tisr-  'drei',  Plur.: nSit  atvd  nSii  dva  nsit  %rayB  (Nm,)  nSit\ fräyanhs  T.44',  —  aivahe  pasvS  .  .  dvä ..  iryam'^  .  .  caturqm  N.  65;  —  aSva lirUva  ,.  dva  %riiha  . ,  %ribyS  %risvaiiöyö V.  2.  ii£;  —  aevahe  ..  *as)maeyahe  .. dvayä  .  .  %rayqm  ,  ,  caiiWärS  V.  iS.ii; F./,  P.2^,  V.  1$.  49,  iS.  17';  —  %rays zavainti  gäusca  aspasca  haomOscaY.ll.i; 20,3,  21.  i,  Az.  5J,  Vyt_5;  —  aitbyö  ratu- byS yöi  hinti  %rayasca'^  %risqsca  "..33.." Y. /.  10;  —  "ibräyd  (als  Am.)  anya  maya nihw?r»sBii  V.p.  9;  ti^,  5. 10,  Vd.  12;  — är(/(Ain.)  mätahs  ußa.baolayan  .  .  xAias mänhs  V.  7.  i4f.i  N.  66,  67,  '88.  57^;  — ^ris  mayam^^  ava.kanaym  V.  Ä37,  16. 12;  j.  51;  —  %rJ  (An.)  *malima.safnqn asamäj  P. g;  — -  %rlvä  azsiti  (sd)  sraois.-
14631:•  j,  dridasa-  Adj.  'der  dreizehnte':  das^mS . .  aivandasB . .  dvadasS . .  'ss  s»i>ist3  Yt  /.  8 ; —  's^m  asarihqmca  .  .  V,  j.  1 6.
```


## [2026-10-15T02:49:14.544Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14500,14640p BRT.txt | grep -n -o -E \"^.{0,4}•  j[,.]  [^ ]+  [^']{0,40}'[^']{0,60}'\" | head -40",
 "description": "List Bartholomae headwords near thri"
}
```


### [2026-10-15T02:49:14.975Z] TOOL RESULT

```
1:•  j.  ftray-  Zw.,  fem.  tisr-  'drei'
8:•  j.  'fl-rav-  V,  'alere'
11:•  j.  *3Tav-  V.,  nur  mit  aoi  und  ava  'auf- schichten'
37:•  j.  ^ratay-  f.   'Schirm,   Schutz'
49:•  j.  ^rätö.t»iiia-  Adj.  'der  am  besten beschirmt'
65:•  j,  flräya'van-  :  'yaon-  Adj.  —  ?  — ,  Bei- wort des  a'
70:•  j.  Sräyö.drij'av-  Adj,  'die  Armen  schir- mend, fUr  sie  sorgend"*:  maridikim  '
72:•  j.  fl-räyö.drijTi'tama-  Adj,  'der  die Annen  am  besten  beschirmt,  am  besten versorgt'
74:•  j.  SrtjfBÄa-,  9T^f8a-'>  Adj.  (fem.  "oä-) '
79:•  j.  dri-afsman-  Adj.  'drei  Verszeilen enthaltend"'
85:•  j,  3-ri.lEaräa-  a  'Dreigefurche'
87:•  j.  drigämya-  n.  'Raum,  Entfernung von  drei  Schritten'
132:•  j,  dridasa-  Adj.  'der  dreizehnte'
134:•  j.  dri-paüa-  n.  'Längenausdehnung  von drei  Fuss,  drei  Fusslängen'
136:•  j,  *ri-pi9Twa-  Adj.  'der  drei  Mahl- zeiten bekommt'
```


## [2026-10-15T02:49:18.376Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14636,14760p BRT.txt | grep -n -o -E \"^.{0,4}•  j[,.]  [^ ]+  [^']{0,40}'[^']{0,60}'\" | head -40; grep -n -i -E \"θraētaona|sitar|setar\" HRN.txt | head -3; grep -n -E \"^ *[0-9]+\\. *(sih|sī|si|se|sitar|sih)\\b\" HRN.txt | head",
 "description": "More Bartholomae; Horn search"
}
```


### [2026-10-15T02:49:18.802Z] TOOL RESULT

```
6:•  j,  (hri-bda-  m.  'dreifache  Fessel'
7:•  j.  Srima-  m.  'Nahrung,  Sättigung; Stäilcung,  Stärke'
9:•  j.  Sri-mlhya-  Adj,  'drei  Monate dauernd'
20:•  j.  Sri.yaxätay-",  itryaxStay-'*  m.,  Plur. '
23:•  j.  ftri-sata-  Zw.  'dreihundert"'
25:•  j.  '^risata',  nur  KompA.  und  Ableit''
29:•  j.  ^risata'd'wa-  n.  'Dreissigheit,  rpioKäi'
31:•  j.  ^risatö.zyain-  m.,  Plur,  'dreihundert Winter'
33:•  j.  SrisaSTwant-  Adj.  'dreissigfach'
35:•  j.  Sri-sant-  fem.  Zw.  'dreissig*:  yiA  htnti a^ake  ratavS  %rayasi!a  '
38:•  j.  *{hrisa8't»raa-  Adj.  'der  dreissigste'
46:•  j.  8Ti-zantav-  Adj.  (auch  fem.)  'drei  Gaue umfassend'
48:•  j.  9-ri.zar9maya-  i)  Adj.  'drei  Frühlinge umfassend'
50:•  j.  ^►riS  Adv.  'dreimal'
52:•  j.  dris-ä'mruta-  Adj.  'dreimal  aufzu- sagen'
55:•  j.  BriS.urvarä-  Adj.  (maslc.  Ta-)  'drei Pflanzenstengel  enthaltend,  daraus  be- stehend'
60:•  j.  Sriäva-  n.  'Drittel'
73:•  j.  ^SriS-hastra-'*  n.  'Versammlung  von dreien'
76:•  j.  Srizant-  n.  'Drittel'
81:•  j.  Orizvat  Adv.  'dreimal'
89:•  j.  jbaeä-,  dvaeS-,  g.  dvbaeS-''
11035:Vergl. np. sitare (oben No. 711).
6360:121. se^'üT, sera *PaIast*.
6614:759. si (geschrieben sih) 'drei', siyum^ seyum (AM.), poiHD
6640:763. si^deh 'dreizehn*.
```


## [2026-10-15T02:49:21.142Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 6614,6650p HRN.txt | cut -c1-200; grep -n -E \"sizdah|sī 'dreissig|si 'drei|sitār|setār\" HUB.txt | head",
 "description": "Read Horn on se, sizdah"
}
```


### [2026-10-15T02:49:21.483Z] TOOL RESULT

```
759. si (geschrieben sih) 'drei', siyum^ seyum (AM.), poiHD
(Is. 37, 30).
ap. I^Httya- dritter'; aw. ^n- 'drei'; phlv. s(i)\tigar
'dritter*, päz. sl ; ai. tri- ; arm. ereU (H. No. 100).
') Vergl. np. ä/efi'i säg (»Sälin. T, 16 Vers 42).— 168 —
kiird. LW. sl; idy, dre; wa/. tral, sangl. trdl, ya/n.
OeraT, miuj. sardi, sar haröi, si/n. arrai,
760. st 'dreissig'.
aw. drisatent 'dreissig; phlv. sih, päz. si\ ai. trincdt.
kurd. LW. s7; af/. der6\
761. siyah *scliwarz', sit/dhi.
Semn. suah.
aw. st/äva- 'schwarz' in SyävarsCmU'y Syäiaspi-;
phlv. siyak, siyäh (PPGrl.), raand. LW. N"'1N''D ; ai.
Qyävd' 'braun, schwarzbraun'; arm. LW. ^) seao
'schwarz'.
kurd. bei. (348) LW. siyäh 'schwarz ; oss. saa (222);
wa/. sü, sangl. s6L
Als Grundform von . np. siyäh ist *syaoaka' anzu-
setzen.
762. sex (i'^i^iit auf be/^), Sa di, Gul. 46 Zeile 5 v. u., Spr.)
*Bratspiess'.
skr. gikha- 'Spitze (eines Pfeiles etc.)', vergl. cekh-
ara- (?).
kurd. stx^^ si/ü *Lunte* ; bei. slh^ sl *Bratspiess, Lad-
stock' (344).
763. si^deh 'dreizehn*.
aw. dridasa 'dreizehnter'; phlv. sicdahum^) (päz. seS,
sez"); ai. trdyödasa,
kurd. dausCf slzdeh (LW.); afy. dyärlas.
np. sizdeh ist eine Analogiebildung.
764. s~ui% 'Kummet'*).
aw. sima^ vergl. siimiSra- yt. 10, 125 (Geldner,
KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
(nach Geldner; PW. hat 'Zapfen, Holznagel, Keil,
1) Nach Nöldeke bei Hübsohmann, KZ. 23, 402.
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
2758:*) 'V'gl. jud. tat. se *drei\ aber si 'dreissig' (Miller p. 79); kg§.
7250:pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig =
```


## [2026-10-15T02:49:24.049Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 7244,7254p HUB.txt | cut -c1-200; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"7250\")) {}}' /dev/null; grep -n -c $'\\f' HUB.txt",
 "description": "Read Hübschmann on se"
}
```


### [2026-10-15T02:49:24.379Z] TOOL RESULT

```
dust (3. Jhd.), Cureton, Spicil. 25, nach NSldeke)
Zardust, arm. Zradest, Zradast, phi. Zaratust {Zara-
fuxst) => zd. ZaraO^ustra-.
3. Fur Or : fr in FrSdun, siehe p. 207.
§ 96. Ap. &^ wird im Np. zu s oder hr:
a) zu 5 in: si, [liter se *drei' (s. oben p. 78) = zd. g.
pi. x^rayqm, vgl. ap. ^Htiya- *der dritte*; si 'dreissig =
ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
nach pidar u. s. w.) = ap. pud^a-; pas 'Wache', phi. pOs
Gl. and Ind. 91, Bdh. Gl. 96, paspamh *Schutz' Bdh. Gl. 96,
zd. padra^; das ^Sichel', phi. das Gl. and Ind. 181, skr.
291
```


## [2026-10-15T02:49:30.209Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"δry|ðry|dry \" SOD_pages.txt | head -8; grep -n -E \"^[0-9]{4} +(δry|dry)\\b\" SOD.txt | head; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BQT'].get('page_offset'), str(d['BQT'].get('lookup_hint'))[:800]); print(d['SOD'].get('page_offset'))\"",
 "description": "Grep Sogdian dictionary; BQT offsets"
}
```


### [2026-10-15T02:49:30.684Z] TOOL RESULT

```
8797: 1741 »gkVt-      B, M,S                                Cp/JU            dry land
12908:             condar, candar        ©c-ndry *haca-antar =*cyndr,                     candan
22424:     (to)dry up                                                      paB ©ob. -y =^55
24537:     (to)dry up, 0<?)wipe off                                          to it, to the, for, in, on
25353:                                                                 (to)dry up
26656:                                                                     dry           I
30354:9225 sqr- C =#> skr-                                               dry land
30380:                                                                     dry =* 'sk'wrSy*
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | Fo
printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
```


## [2026-10-15T02:49:33.727Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==210' SOD_pages.txt | grep -n -i -E \"three|thir|dry|ry \" | head -20",
 "description": "Look at Sogdian dict page 143"
}
```


### [2026-10-15T02:49:34.137Z] TOOL RESULT

```
15:         b36 cl6? GMS 1331; Ssmykw* MSP bl24                    3648 dstb'ry C =» 8stJ3'ry
18:      tenth                                                     3651 Sstpry S (M)
25:      handtowel                                                 3653 dstwb'ry C
26:                                                                     Sastu-Pare =*8st}wPry              j^-ijlT tv^-i jiT
40:     8asta ?                                                    3655 Sstwpry => Sst'wPry
52:3644 SstNvpry B                        c^.> X <J^c                   eighth and fifteenth day of the month
53:     Sastu-Pare (SstwPry) ^dstwb'ry                                  GMS 109, 276, 443
```


## [2026-10-15T02:49:37.238Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /three/ {n=split($0,a,\"\\n\"); for(i=1;i<=n;i++) if (a[i] ~ /(^|[^a-z])three([^a-z]|$)/) print NR-1\": \"a[i]}' SOD_pages.txt | head -20",
 "description": "Find 'three' in Sogdian dictionary"
}
```


### [2026-10-15T02:49:37.817Z] TOOL RESULT

```
30: variants of each term in the three different scripts and noting down the source
31: Persian and English - and three parts. The                 transliteration in bold letters and in Sogdian
31:    The three parts of the Dictionary are the Lexicon,      possible.                     V
39:         demonstrated that since the sixth century A.D.,                  related to three great religions, Buddhism,
41: were three Sogdian fragments.                                  Sogdian collection is done by N. Sims-Williams and
42: Hilfsmittel-Sutra" (Intox.). E. Benveniste wrote a                   Helsinki, 1980 and three Buddhist Sutras published
45: Testament   Fragments.75   In     1934, Muller, together           Sogdian cursive script, three in Chinese, one in
46: by three other Russian scholars. The most important             mainely illustrated in a series of narrative wall-
47:    Another inscription written three centuries                   Pakistan, Vol. 1, 1989, and his major work by the
48: reading and photographs of Shatial 1, Rocks 1-39.                  All three are based on the Semitic writing system
48:    The rock inscriptions are very short, generally              the vowels. Of the three scripts, the "Sogdian" is the
48: Sogdian texts are written in three different scripts.           in Sogdian script.
48: script. The Manichean materials are mostly written                   variants. Of the three scripts, M is the only one which
49: materials, distinguishes all the voiceless sprirants,         Sogdiana, three main varieties can be distinguished:
50: to Middle Western Iranian language) to represent                  Christian, according to the three different scripts in
50: consonants, Sogdian Christians added three new                           words in Persian".106
51: orthographies of a single word in the three scripts,
54:   3) [;] occurs after n:                                        /se/               B ^Sry, sy,             three        Av. tfraya-
90:      C2, 31V22 n p!84; S W, SGI 1986, 408                                 three thousand
208:        three
```


## [2026-10-15T02:49:39.958Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==209' SOD_pages.txt | grep -n -B3 -A3 \"three\" | head -30; awk 'BEGIN{RS=\"\\f\"} NR==55' SOD_pages.txt | grep -n -B2 -A2 \"three\"",
 "description": "Read Sogdian 'three' entry"
}
```


### [2026-10-15T02:49:40.400Z] TOOL RESULT

```
61-3618 8ry   B                           (j^-^^                        3631 ds> C => 8sc,)
62-       Ore, se ©<*Qraya-y Khwar. sy; Yaghn. tiray%                   3632 5sc,) B, M, S                        (j^   >-* ^)oS
63-         Parth. hry =^tSrty, >Sry, sy2                                    5asa, 8as (Ssh, ds}) ©<dasa\ Yaghn. das
64:       three
65-                                                                          ten
66-       GMS 1316; EGSii 100
67-                                                                          GMS 1316; VJ 1407; 6sh, MDii
4-                                                                historical spelling.
5-  azdyu       B >ztyw       exiled       Olr. *uzdahyu-
6:  3) [;] occurs after n:                                        /se/               B ^Sry, sy,             three        Av. tfraya-
7-                                                                                   M 'dry, C jy
8-  anjaman     M ynjmn-        assembly      *ham-gamana-
```


## [2026-10-15T02:49:44.283Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *three, (adj|n)|^three,\" KLN_1966.txt | head -3; grep -n -E \"^ *guitar, n|^ *cithara, n|^ *sitar, n|^ *testis, n|^ *tribe, n|^ *tertiary, adj|^ *testimony, n\" KLN_1966.txt | head",
 "description": "Grep Klein for three, guitar, sitar etc."
}
```


### [2026-10-15T02:49:44.601Z] TOOL RESULT

```
39127:three,  adj.  and  n.  —  ME.  thre,  threo ,  thri,  fr.  OE. prt,  prie  (masc.),  preo  (fem.  and  neut.),  rel.  to OS.  thria  (masc.  and  fem.),  thriu  (neut.),  ON. prir  (masc.),  prjar  (fem.),  prju  (neut.),  Dan., Swed.,  Norw.  tre,  OFris.  thre  (masc.),  thria (fem.),  thriu  (neut.),  MDu.,  Du.  drie,  OHG.  dri (masc.),  drio  (fem.),  driu  (neut.),  MHG.  dri,  drie (masc.  and  fem.),  driu  (neut.),  G.  drei,  Goth. *preis  (masc.  and  fem.),  prija  (neut.),  ‘three’,  fr. I.-E.  base  *treyes,  whence  also  OI.  rrdyah, (masc.),  tisrdh  (fem.),  tri  (neut.),  Avestic  Pray 5 (masc.),  tishard  (fem.),  Toch.  A  tri  (masc.)  tre (fem.),  Hitt,  tri-,  Arm.  erek‘.  Alb.  tre  (masc.),  tri (fem.),  Gk.  xpeu;  (masc.  and  fem.),  xptot  (neut.), L.  tres  (masc.  and  fem.),  tria  (neut.),  Umbr.  trip (acc.),  triia,  Oscan  iris,  OSlav.  trije,  trije (masc.  and  fem.),  tri  (neut.),  Lith.  trys,  OIr.  tri (masc.),  teoir,  teora  (fem.),  W.  tri  (masc.),  teir (fem.),  ‘three’.  Cp.  third,  thirteen,  thirty,  thrice. Cp.  also  drill,  ‘woven  material’,  ter-,  tercel, tercet,  tern,  ‘group  of  three’,  ternal,  tertian,  ter¬ tiary,  terzetto,  Thrinax,  tierce,  trammel,  trefoil, tresillo,  trey,  tri-,  triad,  triangle,  triarii,  Trias, tribe,  Tribolium,  triceps,  tricerium,  trident,  triens, triental,  Trillium,  trine,  trinity,  trio,  Trithrinax, triune,  trivet,  trivial,  trivium,  troika.  Cp.  also  the first  element  in  testament,  testicle,  testify  and  in sebundy,  teapoy.
```


## [2026-10-15T02:49:46.801Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *(guitar|cithara|sitar|testis|tribe|tertiary|testimony|zither),  \" KLN_1966.txt | cut -c1-900",
 "description": "Grep Klein guitar, sitar, testis, tribe"
}
```


### [2026-10-15T02:49:47.154Z] TOOL RESULT

```
38722:tertiary,  n.,  a  member  of  third  order  in  a  monas¬ tic  system.  — •  See  prec.  word, tertium  quid,  something  intermediate  between two  things.  —  L.,  ‘a  third  something’,  transla¬ tion  of  Gk.  xptxov  xt.  See  tertian  and  quiddity, teruab,  n.,  a  succession  of  9  tremulous  notes  of the  shophar  (Jewish  Religion).  —  Heb.  t6rii'dh, ‘shout,  cry,  alarm,  blast  of  trumpet  or  shophar, a  succession  of  tremulous  notes’,  formed  from the  stem  of  herfa',  ‘he  sounded  a  signal,  he shouted  in  triumph"  (in  Mishnaic  Heb.  also  ‘he blew  the  shophar’),  which  is  prob.  rel.  to  Arab. ragha,  ‘he  shouted’.
```


## [2026-10-15T02:49:49.392Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"(guitar|sitar|cithara|testis|tribe),  n\\.  —.{0,700}\" KLN_1966.txt | head -8",
 "description": "Grep Klein entries loosely"
}
```


### [2026-10-15T02:49:49.905Z] TOOL RESULT

```
40044:tribe,  n.  —  ME.  tribu,  fr.  OE.  tribu,  fr.  L.  tribus, ‘tribe’,  prob.  meaning  orig.  ‘the  third  part  of the  Roman  people’,  rel.  to  Umbr.  trifu,  fr.  Ital¬ ic  *tribhu-,  ‘a  third’,  which  is  compounded  of *tri-,  ’three’  (see  tri-),  and  I.-E.  *bhu-,  *bheu-,  ‘to be’,  whence  also  L .futurus,  ‘about  to  be,  future’, OE.  beon,  ‘to  be’;  OBret.  treb,  ‘subdivision  of the  people',  and  Ir.  treb,  ‘tribe’,  are  prob.  Latin loan  words.  See  be,  future,  and  cp.  tribunal,  tri¬ bune,  tribute.
```


## [2026-10-15T02:49:52.516Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"(guitar|gu'tar|gultar|sitar|cithara|testis|testimony)[,.] .{0,30}(n\\.|ME|fr\\.).{0,600}\" KLN_1966.txt KLN_1971.txt | head -8",
 "description": "Search Klein guitar variants"
}
```


### [2026-10-15T02:49:55.243Z] TOOL RESULT

```
ugrep: error: error at position 151
}(n\.|ME|fr\.)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,600}
                      exceeds complexity limits___/
```


## [2026-10-15T02:49:58.119Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -o -E \"^ *(guitar|sitar|cithara|testis|testimony),? +(n\\.|adj).{0,600}\" KLN_1966.txt KLN_1971.txt | head -8; /usr/bin/grep -n -o -E \"kithara.{0,200}\" KLN_1966.txt | head -5",
 "description": "Search Klein with GNU grep"
}
```


### [2026-10-15T02:50:02.087Z] TOOL RESULT

```
KLN_1971.txt:47824:cithara, n., an ancient musical instrument re- 
KLN_1971.txt:107243:guitar, n., a stringed musical instrument. — F. 
KLN_1971.txt:244684:testimony, n. — ME., fr. Late L. testimonium, ‘tes- 
KLN_1971.txt:244691:testis, n., testicle. — L., ‘witness; testicle’. See
```


## [2026-10-15T02:50:04.449Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 107243,107256p KLN_1971.txt; echo ---; sed -n 47824,47834p KLN_1971.txt; echo ---; /usr/bin/grep -n -E \"^testament|^testify, \" KLN_1971.txt | head -3",
 "description": "Read Klein guitar and cithara"
}
```


### [2026-10-15T02:50:04.925Z] TOOL RESULT

```
guitar, n., a stringed musical instrument. — F. 
guitare , fr. Sp. guitarra, fr. Arab. qitdra h , fr. 
Gk. xiftapa, fr. Pers. sihtar. See cither and cp. 
gittern, zither. 

Derivative: guitar -ist, n. 

gula, n., the upper throat (zool.) — L., ‘throat*. 
See gullet. 

Derivative: gul-ar, adj. 

gulch, n., a deep ravine. — Prob. fr. dial. E. 
gulch, ‘to swallow greedily’, fr. ME. gulchen , 
---
cithara, n., an ancient musical instrument re- 
sembling a lyre. — L., fr. Gk. xt&apa. See 
next word. 

cither, also cithern, a stringed musical instru- 
ment. — F. cithare, fr. L. cithara , fr. Gk. xiDdcpa, 
fr. Pers. sihtar. Cp. cithara, citole, cittern, git- 
tern, guitar, kit, ‘a small fiddle’, zither, 
citizen, n. — ME. citezein , formed — prob, under 
the influence of denizen — fr. OF. citeain (F. 
citoyen), which was formed fr. cite (F. cite) with 
---
193729:testament. 
244579:testament, n. — ME., fr. Eccles. L. testamentum, 
244596:testify, testimonial, testimony. For the ending
```


## [2026-10-15T02:50:09.477Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^trei-|^ *trei-\\. \" AHD_watkins1985.txt | head; /usr/bin/grep -n -E \"^Guitar|^Sitar|^Testimony|^Tribe\" SKT_dli_revised.txt | head",
 "description": "Grep AHD Watkins and Skeat"
}
```


### [2026-10-15T02:50:09.830Z] TOOL RESULT

```
1093:trei-
33736:Guitar. (F.-L.-Gk.) Y.guUare.^^ 
82890:Tribe, a race. (F. — L.) ¥. tribu, ‘a 
88917:Tribes of Guiana, 1868, p. 140.
```


## [2026-10-15T02:50:11.912Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^ *trei-\" AHD_watkins1985.txt | head; sed -n 33736,33742p SKT_dli_revised.txt",
 "description": "Find trei in AHD body"
}
```


### [2026-10-15T02:50:12.344Z] TOOL RESULT

```
1093:trei-
Guitar. (F.-L.-Gk.) Y.guUare.^^ 
L. cithara. — Gk. KiBapa, a lyre; see 
Cithern. 

Gules, red. (F.-L.^ M. E. gouhs.-^ 
F. giieules; gules, red ; answering to Late 
J..gulaj (pi. of gulal), meaning (i) mouth,
```


## [2026-10-15T02:50:14.493Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -i -E \"Three\\. \\(|\\*trei|trei\\b\" AHD_watkins1985.txt | head -20",
 "description": "Search AHD for trei entry"
}
```


### [2026-10-15T02:50:14.820Z] TOOL RESULT

```
127:complete agreement on the numerals from two to ten: dwo- (*duw6), trei- (*treyes), kvetwer- (*k”etwores), penk”e, s(w)eks, septm, oktd(u), newn, dekm. For the nu- meral “one” the dialects vary. We have a root sem-' in some derivatives, while the western Indo-European languages Germanic, Celtic, and Latin share the form oi-no-. The word for “hundred,” formed from dekm, “ten,” was *(d)kmtom. No common form for “thousand” or any other higher number can be reconstructed for the protolanguage.
999:nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1029:strei-. To hiss, buzz. Imitative root. 1. Extended form *strid- in Latin stridére, to make a harsh sound: sTRI- DENT. 2. Extended variant form *trig- in Greek trismos, trigmus, a scream: TRISMUS. [Pok. 3. streig- 1036.] streig-. To stroke, rub, press. I. Basic form *streig-. 1. Germanic *strikan in Old English strican, to stroke: STRIKE. 2. Germanic diminutive *strik-ila- in Old Eng- lish stricel, implement for leveling grain: STRICKLE. 3. Germanic *strikén- in Old English strica, stroke, line: STREAK. II. O-grade form “stroig- in Germanic *straik- in Middle English stroke, stroke: STROKE. III. Zero-grade form *strig-. 1. Suffixed form *strig-d- in Latin striga, row of grain, furrow drawn lengthwise over the field: STRIGOSE. 2. Suffixed form *strig-yd- in Latin stria, furrow, channel: sTRIA. 3. Nasalized form *stri-n-g- in Latin stringere, to draw tight, press together: STRAIN}, STRAIT, STRICT, STRIGIL, STRINGENDO, STRINGENT; ASTRINGE, CONSTRAIN, DISTRAIN, PRESTIGE, RESTRICT. [Pok. 1. streig- 1036; 4. ster- 1028.] strenk-. Tight, narrow. Possible root. 1. O-grade form *stronk- in: a. Germanic “strangi- in Old English streng, string: STRING; b. Germanic *strangaz in Old English strang, strong, powerful, strict: STRONG; c. Germanic *strangithé in Old English strengthu, strength, strict- ness: STRENGTH. 2. Variant *strang- in: a. Greek strang- alé, halter: STRANGLE, (STRANGLES), (STRANGULATE);
1093:trei-
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1096:5. Greek trias, the number three: TRIAD. 6. Greek trikha, in three parts: TRICHOTOMY. 7. Greek compound triérés, galley with three banks of oars, trireme (-érés, oar; see era-'): TRIERARCH. 8. Suffixed form “*tri-to- in Greek tritos, third: TRITIUM; TRITANOPIA. 9. Compound form *tri-pl-, “threefold” (*-pl- < combining form *-plo-; see pel-3), in Greek ¢triploos, triple: TRIPLE. 10. Compound form *tri-plek-, “threefold” (*-plek-, -fold; see plek-), in Latin triplex, triple: TRIPLEX. 11. Compound form *tri-st-i, “third person standing by” (see sta-), in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Per- sian si, three: straR. III. Extended zero-grade form “iris, “thrice.” 1. Latin ter, thrice: TERN?; TERPOLYMER. 2. Greek tris, thrice: TRISOCTAHEDRON. 3. Suffixed form *tris-no- in Latin trini, three each: TRINE, (TRINITY). IV. Suffixed o-grade form *troy-o- in Russian troje, three: TROIKA. [Pok. trei- 1090.] trem-. To tremble. Possibly related to trep-' and tres- through a hypothetical base *ter-. Latin tremere, to shake, tremble: TREMENDOUS, TREMOR, TREMULOUS. [Pok. trem- 1092.] trep-'. To tremble. Possibly related to trem- and tres- through a hypothetical base *ter-. Latin trepidus, agi- tated, alarmed: TREPID; INTREPID. [Pok. 1. trep- 1094.] trep-2. To turn. 1. Greek trepein, to turn: -TROPOUS; APOTROPAIC, TREPONEME. 2. O-grade form *trop- in: a. suffixed form *trop-o- in Greek tropos, a turn, way, manner: TROPE, TROPO-, TROVER; CONTRIVE, (RE- TRIEVE); b. suffixed form *trop-d- in Greek tropé, a turning, change: TROPHY, TROPIC; ENTROPY. [Pok. 2. trep- 1094.] tres-. To tremble. Possibly related to trem- and trep-1 through a hypothetical base *ter-. Metathesized form *ters- in o-grade suffixed (causative) form *tors-eyo- in Latin terrére, to frighten (< “to cause to tremble”), with vowel e from terror (< *ters-os-), terror: TERRIBLE, TERROR; DETER, TERRIFIC. [Pok. tres- 1095.] treud-. To squeeze. 1. Suffixed o-grade form *troud-o- in Germanic *thrautam in Old English thréat, oppression, use of force: THREAT. 2. Variant form *trid- in Germanic “thristjan in Old Norse thrysta, to squeeze, compress: THRUST. 3. Latin tridere, to thrust, push: ABSTRUSE, EXTRUDE, INTRUDE, OBTRUDE, PROTRUDE. [Pok. tr-eu-d 1095.] trozdo-. Thrush. 1. Germanic *thrust- in Old English throstle, thrush: THROSTLE. 2. Germanic *thruskj6n- in Old English thrysce, thrush: THRUSH}. 3. Zero-grade reduced form *trzdo- in Latin turdus, thrush: STURDY. 4. Perhaps altered in Greek strouthos, sparrow, ostrich: STRUTHIOUS; (OSTRICH). [Pok. trozdos 1096.] tu-. Second person singular pronoun; you, thou. 1. Lengthened-grade form “ti (accusative “te, *tege) in Germanic *thii (accusative *theke) in Old English thi (accusative thec, thé), thou: (THEE), THOU!. 2. Suffixed extended form *éwjei-no- in Germanic *thinaz in Old English thin, thine: THINE, THY. [Pok. tu- 1097.] twei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
1266:ASTERIATED | ster-3 ASTERISK ster-3 ASTERISM  ster-3 ASTEROID ster-3 ASTIGMATISM _ steig- ASTONISH (s)tena- ASTRAEA | Ster-3 ASTRAGAL ost- ASTRAGALUS ost- ASTRAL  ster-3 ASTRAPHOBIA | ster-3 ASTRINGE | streig- ASTRO-  Ster-3 ASTROBLEME gWele-1 ASTROLABE (s)lagW- ASTRONAUT nau-2 ASTRONOMER nem- ASTRONOMY nem- ASTUTE wes-3 ASTYLAR sta- ASUNDER sen-2 ASYNDETON dé- AT ad- ATARACTIC dher-1 ATAVISM atto-, awo- ATAXIA tag- ATHEISM dhés- ATHELING _ athal- ATLANTIC tele- ATLAS tele- ATMAN étmen- ATMOSPHERE wet-' ATOM tem- ATONE ol-no- ATRABILIOUS ter- ATRIUM ater- ATROCIOUS ter- ATROPHY threph- ATTACH steg- ATTACK steg- ATTAIN tag- ATTEND ten- ATTENUATE ten- ATTEST trei- ATTITUDE ap-! ATTO- okt6(u) ATTORN  tere-! ATTRACT tragh- ATTRITION tere-1 AUBADE albho- AUBURN = albho- AUCTION aug-1 AUDIBLE au-5 AUDIENCE au-5 AUDIENT au-5 AUDILE au-5 AUDING au-5 AUDIO- au-5 AUDIT au-5 AUDITOR au-5 AUDITORIUM § au-5 AUDITORY au-5 AUGEND aug-1 AUGER nobh- AUGHT! = aiw- AUGHT2 wekti- AUGITE aug-2 AUGMENT aug-1 AUGUR aug-t AUGUST aug-1 AUK el-2
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2138:PROSTYLE sta- PROTAGONIST ag- PROTASIS ten- PROTECT (s)teg- PROTEIN per! PROTEROZOIC per! PROTEST trei- PROTHALLUS dhal- PROTHESIS dhé-1 PROTHONOTARY gnd- PROTIST per! PROTO- pert PROTOCOL koli- PROTON per! PROTONEMA (s)né- PROTOPATHIC kWent(h)- PROTRACT tragh- PROTRUDE treud- PROTUBERATE teue- PROUD es-
2188:RIDE reidh- RIDGE sker-3 RIDING? _trei- RIFE rei-1
2249:SEQUESTRUM sekw-1 SERAC ser-2 SERE! saus- SERENE ksero- SERF servus SERGEANT servus SERIES ser-3 SERIF skribh- SERIOUS swer-5 SERMON ser-3 SEROTINOUS sé@-2 SERPENT serp-2 SERPIGO serp-2 SERRIED ser-3 SERTULARIAN ser-3 SERUM ser-2 SERVAL_ ker-! SERVE servus SERVICE servus SERVILE servus SERVITUDE servus SESQUI- kwe, sémi- SESQUIPEDALIAN ped-! SESSILE sed-1 SESSION sed-1 SESTERCE sémi-, trei- SESTET s(w)eks SESTINA s(w)eks SET! sed-1 SETTLE sed-1 SEVEN septm SEVER pere-! SEVERAL pere-1 SEVERE WEér0- SEW syu-
2265:SITAR ten-, trei- SITH sé@-2 SITUATE tkei- situs tkei-
2320:STRIA streig- STRICKLE  streig- STRICT streig- STRIDENT strei- STRIGIL  streig- STRIGOSE  streig- STRIKE streig- STRING  strenk- STRINGENDO | streig- STRINGENT streig- STROBILE  streb(h)- STROBOSCOPE streb(h)- STROKE streig- STROMA ster-2 STROMATOLITE  ster-2 STRONG  strenk- STROP streb(h)- STROPHANTHIN andh- STROPHE streb(h)- STROPHOID streb(h)- STROPHULUS  streb(h)- STRUCTURE ster-?
2354:TENTH dekm TENUOUS ten- TENURE ten- TENUTO ten- TEPID tep- TERATOCARCINOMA kWer-1 TERATOGEN kWer-1 TERATOID kWer-1 TERATOMA kWer-1 TERCEL trei- TERCET trei- TEREDO tera-! TERETE tere-1 TERGIVERSATE wer-3 TERM ter- TERMINATE ter- TERMINUS _ter- TERN? trei- TERPOLYMER trei- TERPSICHORE gher-!, terp-
2355:TERRACE 108 TUMESCENT TERRACE ters- THRASH tere-1 TORQUE! terkw- TRIAD trei-
2358:TERRAQUEOUS ters- THREE trei- TORRID ters- TRIBRACH mregh-u-
2361:TERRESTRIAL ters- THRESH tera-! TORTICOLLIS kWel-1, terkw- TRICERATOPS ker-1 TERRE-VERTE ters-, virére THRESHOLD tere-1 TORTUOUS terkw- TRICHINA  thrix TERRIBLE tres- THRICE trei- Tory ret- TRICHO-  thrix TERRICOLOUS ters- THRILL tere-2 TOTAL teuta- TRICHOME _ thrix TERRIER ters- THRONE dher-2 TOUGH denk- TRICHOTOMY _ trei- TERRIFIC tres- THROSTLE trozdo- TOUPEE tap- -TRICHOUS _ thrix TERRIGENOUS §ters- THROUGH tere-2 Tow! deuk- TRICHURIASIS ors- TERRITORY ters- THROW tere-1 Tow? taw- TRICLINIUM klei-, trei- TERROR tres- THRUM?2 ter- TOWN dhino- TRICORN ker-1 TERTIAN trei- THRUSH! trozdo- TOXIC tekw- TRICROTIC  kret-2, trei-
2362:TERTIARY trel- TESSERA kWetwer- TESTAMENT trei- TESTIFY trei- TESTIMONY trei- TETCHY deik- TETRA- kWetwer- TETRACHORD ghere- TETRAD kWetwer- TETRADYMITE dwo-
```


## [2026-10-15T02:50:19.118Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^ ?tr[ei]?[ie]?y?es|^trejes|^treies|^tréies|^trei\" IEC.txt | head -5; /usr/bin/grep -n -E \"trei-|tréi-\" incoming/WLD/WLD_Bd1_pages.txt | head -5; /usr/bin/grep -n -E \"^ ?THREE|three\\b\" SYN.txt | head -5",
 "description": "Grep IEC, WLD, SYN for three"
}
```


### [2026-10-15T02:50:19.556Z] TOOL RESULT

```
18884:treies, m. ‘three’. Cf. tri-, tosrio (tosr). WP I, 753 Skt. trayah, m. beside trí, mn. id.; cpds: tra- yas-; Av. Oráyo, m. id.; Per. si; Oss. ártá; Pa- miri arrai; Tokh. A tre, tri; B trey, trai; Arm. erek, g: eric. ab. eriwk; Hitt. tri-es (for *trés), id. cf. triala-, adj. extn.; Lyc. trijo; Gk. treis, mf.; Alb. tre (f: tri); Lat. tres (n: tria: Gk. tria); Osc. Dis, f.; Umb. triia, n.; MIr. & Ir. trí; cpds: tré-; OBr. W tri; Br. tri, m. id.; Cor. try, id.; Go. *preis; OHG dri, rt: OE preo, prie; ON prír; OCS (and com. S1.) tri; Li. trys; Latv. tris (lit. 'spinning-fingers'?)
18885:treio ‘turn, twist, bore’. Cf. traio and WP I, 728 Gk. fut. tréso, id.; adj. fr. pp. trétós “bored; Alb. cf. m-troj, v. ((deceive', fr. *mbhi-?); MHG drajen, wv. tr. & intr. “twist, turn; OE cf. pràwan, sv. 7. id.; E cf. to throw a pot; Du. draaien, intr. id. (& 'spin); ON cf. (?) þrá, s. ‘obstinacy’; þrár, adj. ‘stubborn’; þráast, v. refl. ‘persist’. (For Br. troeza, træœæža, inf. ‘twist’, see tràió)
18886:treios ‘threefold; three together; three- some’. Cf. treies, tri-. WP I, 753 Skt. trayáh, adj. ‘threefold’; Oss. ärtäjä “all three’; Arm. erir, adj. ‘third, threefold’; OCS (and com. Sl.) troje “all three’; Li. trejas, adj. (‘threefold’; usu. pl. treji, m., tr&jos, f.)
18912:tresoros, is (force, movement, impulse’. Cf. tresó and next Arm. erer, s. ‘movement’; MIr. treoir, f. ‘force’; Gk. trëron, onos, adj. ‘timorous’; Hes. trerón, adv. ‘rapidly’; radical in Li. tresià, f. ‘flighty girl’; trésena, f. “dash, haste’; o-gde in Go. prasa-balpei, f. ‘belligerence’; ON þrasa, v. ‘rage, bluster’
18913:tresk- (1) ‘press, tread, trample, urge, egg on’. (Variant trekst-) Mir. cf. tresc, m. (queried: ‘incitement of dogs’); Ir. treasc, m. (1) beside tríosc, m. (‘ré- fuse, offa, *-e-: -8-); MHG dreschen, sv. 3. ((2) “take the field, run out of hounds); OE cf. presc-wald, -wold, m. “threshold, limit’; Norw. treskel, id.; cf. Sw. dial. tresk, adj. ‘stubborn’; treska, f. ‘obstinacy’; treskas, v. *be obstinate'; Norw. tresk, adj. ^wily'; Cz. tfestit, inf. ‘madden; rampage’; vy-tfestit oci
71331:                                                                                     trei-                                                              753
71389:trei- „drei'               £
71418:zu auf idg. *trei- weisenden Zs. s. Brugmann Distrib. 65 ff.
71921:trl-vi usw. gehorigen idg. Wzf. *trei-k-), mit gramm. Wechsel aisl. pryngua,
724:THE PHYSICAL WORLD IN ITS LARGER ASPECTS 13 | world (which fill some thirteen columns The early philosophers (Pythagoras 1 in the NED), we may note three main | first, according to the frequently repeat- + types as of especial importance in the | ed tradition) applied this term to the
1231:The words for ‘water’, with few ex- belong to certain widespread nates, one of these reflect- ing what was clearly the general IE word for ‘water’, and three others also reflecting I words for ‘water’ , but per- haps in some more special application, such as ‘running water’ or ‘rain water’. Many words belonging to these groups appear in other lists, as under ‘sea’, “vave’, ‘river’, ‘rain’.
1955:The present differentiation of NE mist, fog, and haze cannot be matched in the other languages, where with some eX- ceptions the same word answers roughly to all three. Many of the words are cop- nate with some of those for ‘cloud’. Others are from such diverse notions as ‘vapor’, ‘dim’, ‘gray’, ‘wet’, ‘winter’, etc.
2918:2.45. ‘Sister’. 1. IE *swesor-, prob. *swe-sor-, cpd. of the refl. *swe-, the sec- ond part related to the rare Grk. dap ‘wife’, Av. hairigt- ‘female’, Lat. uxor ‘wife’ (2.32), and the fem. numeral forms like Skt. tisras ‘three’. Walde-P. 2.583 f. Ernout-M. 958f. Wacker- nagel, Altind. Gram. 3.349. Benveniste, BSL 85.1.104 f.
3248:‘Cousin’ is understood here in the stricter and usual current sense of NE cousin, namely as ‘first cousin, cousin- german’. Even so, it covers eight more specific varieties of relationship, there being three pairs of variable factors, that is, ‘father’s (or mother’s) brother’s (or sister’s) son (or daughter)’.
```


## [2026-10-15T02:50:22.046Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 71389,71400p incoming/WLD/WLD_Bd1_pages.txt | cut -c1-200; /usr/bin/grep -n -E \"13\\.13|'Three'|‘Three’\" SYN.txt | head -5",
 "description": "Read WLD trei; find Buck 'Three'"
}
```


### [2026-10-15T02:50:22.455Z] TOOL RESULT

```
trei- „drei'               £

                               ,
                                   Xom. m. trejes, n. tri, f. tis(o)rcs (diss. aus *tris(o)rvs).
     Ai. trdynh m., in (ved.), trini n., tisrdh f.  av. dr ago in., dri n., tisni f.                 ;



arm. erek (gen. eri-e, instr. eri-vk ); gr. tq£i± (gort. t gtsz), rgia; alb. tri7, fem.
tri (ursprgl. n. *tri, G. Meyer Alb. Wb. 435, Pedersen KZ. 34, 291); toch. tri
                                                                                                             ££
lat.       tries,    tria           ( *irl             in tri-yinUx ),             osk. Iris        „tres         ,
23353:13.13 WHOLE
23429:13.13 WHOLE
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
```


## [2026-10-15T02:50:25.199Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^13\\.3[0-9]?|THREE\" SYN.txt | head -6; /usr/bin/grep -n -E \"Av\\. ?.r[aā]y\" SYN.txt | head -5",
 "description": "Find Buck 13.3 THREE"
}
```


### [2026-10-15T02:50:25.697Z] TOOL RESULT

```
23365:13.31 Norse on THE NUMERALS
23366:13.32 Onn
23367:13.33 Atonz, Onty
23368:13.34 Iimsr
23369:13.35 Last
23370:13.41 THREE
1249:GAs, 74 Goth. marei Lith. jira (mares) i ee ieee ON haf, ser (marr) Lett. jira NG Oédacca, téAayos Dan. hav (s4) ChSl. morje Lat. mare (aequor, etc.) Sw. hav (sjé) SCr. more It. mare OE s@ (mere, haf) Boh. moje Fr. mer ME _ see Pol. morze Sp. mar NE sea Russ. more Rum. mare Du. zee Skt. sdgara-, samudra-, Tr. muir, fairrge, ler OHG mari, séo etc. NIr.  fatrrge, muir, lear MHG mer, sé Av. zrayah-, OPers. W. mor NHG meer, see (fem.) drayah- Br. mor
1278:Av. zrayah-, OPers. drayah- (NPers. darya ‘sea’ or ‘large river’) : Skt. (Vedic) jrayas- ‘flat surface’ (so BR), in which case one would compare the Iranian use with that of Grk. wé\ayos, Lat. aequor (above), but according to Geldner, Ved. Stud. 2.248 ff., ‘onset, onrush, course’, fr. jri- ‘rush upon’. Walde-P. 1.660.
18154:Av. frayana-, cpd. of fra + ayana (Skt. prayana- ‘entrance, beginning’): i-, Skt. 7- ‘go’ (10.47). Barth. 989.
19535:wealth’ (also rayi-), Av. ray0 (gen. sg.) ‘wealth’, rayi- ‘splendor’, Skt. ra- ‘give’. Walde-P. 2.343. Ernout-M. 861f.
23561:924 SELECTED INDO-EUROPEAN SYNONYMS 13.16 MORE Grk. —-rAclwy, zAbwy Goth. managiza (maizo, Lith. daugiaus NG meptoadrepos mais adv.) Lett. vairak Lat. _pliis ON metri; fleiri (pl.) ChSl.  bolzjt, MUNOzZE;t, vedte It. pitt Dan. mer; flere (pl.) SCr. vide Fr. plus de Sw. mer; flere (pl.) Boh. _ vic(e) Sp. mas OE ma Pol. —- wiecej Rum. maz mult ME mo; more (sg.) Russ. _bol’Se Ir. mo; lia (pl.) NE more Skt. bhilyas-, bahutara- NIr. —tuilleadh; lia (pl.) Du. meer Av. Srayah- W. mwy OHG = mér, méro; manigiron Br. mut, mutoc’h (pl.)
```


## [2026-10-15T02:50:28.317Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^13\\.41|13\\.41 \" SYN.txt | head; awk 'BEGIN{RS=\"\\f\"} NR==966 || NR==967' SYN.txt | head -30 | cut -c1-400",
 "description": "Read Buck p. 941 THREE"
}
```


### [2026-10-15T02:50:28.701Z] TOOL RESULT

```
23370:13.41 THREE
23956:13.41 13.42 THREE THIRD (Ordinal) Tpets tptros
24060:13.41. IE stem *tri-, nom. pl. *treyes. Walde-P. 1.753. Brugmann, Grd. 2.2.11 f.
. miatki (also ‘finely ground’), Russ. melkij (also ‘small, fine’), prob. through ‘finely ground, fine’ : ChSI. mléti, Lat. molere, etc. ‘grind’. Berneker 2.48.
SCr. plitak, Pol. piytki : SCr. plivatt, Pol. plywaé, ChSl. plavati ‘swim, float’ (11.34), hence of fordable water (cf. Pol. plyt ‘a raft, float’), that is, ‘shallow’, then also of dishes. Briickner 422.
7. Skt. gadha- ‘fordable, shallow’, etym.? Walde-P. 1.665. Uhlenbeck 79.
Endz. 3,814. 12.71 FLAT
adarbs, medtvds Goth. ibns Lith. lék3tas xebw6s, TAaKWTOS ON flair Lett.  lézns, plans planus Dan. /flad ChSl. ploskit piano, piatto Sw. fiat, platt SCr. plosnat plat OE efen Boh.  plochy, plosky
. plano ME  flat(t), playne Pol.  plaskt
. es, lat NE flat Russ. ploskij
reid Du. vlak, plat Skt. | sama- reidh OHG flah Av. flat, gwastad MHG vlach kompes, plat NHG _ flach, platt
for ‘flat’ belong to an inherited group
with basic notion of ‘spread out’. i But many words for ‘equal’ (12.91) ot even’ are also used for ‘level, flat’. = : few exceptions (where there tat) a no more common words for a = are not included in the list. ils lee -buadbs ‘even, level’ : Lat. sim- tana th ar’, Grk. duds ‘the same’, Goth. _ CSame’, Skt. sama-‘equal, same’ 0 "even, level, flat? UR ade Dla’ gf; ge vehi (cf. sama-bhimi- z is rk,
, flat? . : ’
Mion) Tait tbns, OF efen, etc. (see ' ygus, Lett. lidzens ‘equal’
The majority of the common words | (: Goth. ga-leiks ‘like’, etc.) and ‘level,
flat’; ChSl. raviniw (renders zediwés Lk. 6.17, elsewhere in Gospels tcos), ete., general Slavic for ‘equal, even’ and so sometimes ‘level, flat’, whence words for ‘plain’ sb. (1.23) : Goth. rims ‘roomy, spacious’, Av. ravah- ‘open space’, Lat. ras ‘country’, etc.
2. Derivs. of IE *pela-, *pla- with no- tion of ‘spread out flat’, seen in Lith. ploti ‘flatten’ etc., also in several words for ‘wide, broad’ (12.61). Walde-P. 2.61, 90f., 99f. Ernout-M. 776. REW 6581, 6586. Falk-Torp 230.
With no-formation, Lat. planus (> It. piano, OF r. plain, Sp. plano, llano), Lett. plans (mostly ‘thin’, like Lith. plonas); with guttural extension (cf.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
894 SELECTED INDO-EUROPEAN SYNONYMS
Grk. rAd ‘flat surface’), OHG flah, MHG vlach, NHG flach, Du. vlak; with dental extension, Grk. wAazts ‘broad, flat? (> VLat. *plattus > It. piatto, Fr. plat > Br. plat, Du. plat; LG plait > NHG platt > Sw. platt), ON flair
 (> ME flatt, NE flat > W. jflat), Dan. jlad, Sw. flat: ChSI. ploskt (*plat-sko- or *plak-sko-?), SCr. plosnat, Boh. plosky (Boh. plochy prob. fr. OHG flah, Ge- bauer 1.441, Vondrak 1.436; otherwise Brickner 419), Pol. ptaski, Russ. ploskij.
3. Grk. wedtevds, later redivés, only of ‘flat’ country, deriv. of zedloy ‘plain’ : mébov ‘ground’,
NG z\axwrés ‘compressed, flat’, fr. mhaxavw ‘compress’, deriv. of rAdé ‘flat stone’.
4. Rum. ges, only of ‘flat’ country, fr. Lat. sessus ‘seated, settled’. Tiktin 1411. Puscariu 1586.
Rum. lat ‘broad’ (11.61), used also for ‘flat’ dishes. Tiktin 892.
5. Ir. réid, NIr. réidh, also ‘clear, open, ready, smooth’ prob. orig. ‘pas-
sable’ (of a road, ete.) : riadazy ON rida id., ete. Pedersen 1.58.
W. gwastad ‘level, flat’, also and orig ‘steady, constant’ : Ir. fossad ‘firm’, fr *upo-stato-, IE *sta- ‘stand’, Walde-p. 2.605. Pedersen 1.34,
Br. kompes, also ‘smooth, polished’ MBr. compoes ‘equal’, beside W. cafe hwys-iad ‘adjustment, quality’, prob, epd. of kom-, cym- ‘co~’ and poez ‘weight? (fr. Lat. pénswm). Loth, Mots lat. 156, Henry 75.
6. Goth. ibns (only dat. Sg. ana stada tbnamma = emt rérov redwod Lk. 6.17), OE efen (ME, NE even), etc., general Gme. word for ‘even, level’ and so some- times of ‘flat’ land, etc., etym. dub. Walde-P. 1.102. Feist 287.
```


## [2026-10-15T02:50:31.500Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23956,23960p SYN.txt | cut -c1-700; sed -n 24060,24064p SYN.txt | cut -c1-500; awk 'BEGIN{RS=\"\\f\"} NR==54' GPL.txt | /usr/bin/grep -n -i -E \"three|sih|thirt\" | head",
 "description": "Read Buck THREE and Platts p.41"
}
```


### [2026-10-15T02:50:31.934Z] TOOL RESULT

```
13.41 13.42 THREE THIRD (Ordinal) Tpets tptros
rpets tplros trés terlaus
tre lerzo {rois_ —«stroisiéme tres lercero . fret al treilea tri tris(s) tri triomhadh tri tryddydd Iri trivel, trede Goth. preis  pridja prir pridt tre tredje tre tredje pri pridda thre thride, thirde pee third rie derde QHG dri ritto me dri. dritte drei dritte trys tretias [ ike treSazs §¢ ey trethjt tj trec eiira ett Russ, it trzeci ting tretij 0 Yas iritya- ray Oritya-
’ a _ NED s.v. last
Kluge-G. 356. deriv. of paskut b ei . Skt. pacca, Lat. post, igftely ii p.1 1,79). Leskien, Bildung
13.41. IE stem *tri-, nom. pl. *treyes. Walde-P. 1.753. Brugmann, Grd. 2.2.11 f.
Here belong all the words listed, like- wise Alb. tre, Toch. B trai, A tre, fem. t77-, Hitt. tri-.
A peculiar fem. form *tis(o)res is at- tested by Skt. tisras (cf. also catasras,
fem. of catvadras ‘four’), Av. tisrd, Ir. teoir, teora, MW, Br. teir, W. tair. This is prob. fr. *tri-sores (with dissimilatory loss of r), a epd. with a word for ‘woman seen in IE *swe-sor- ‘sister’ and perh. Lat. uxor ‘wife’.
13.42, The ordinals for ‘third’ are derived from the cardinal, most of them
```


## [2026-10-15T02:50:34.302Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"\\bsih\\b|\\bsi\\b.*three|three.*\\bsi\\b\" GPL.txt | head -8",
 "description": "Grep Platts grammar for 'three'"
}
```


### [2026-10-15T02:50:35.027Z] TOOL RESULT

```
595:§ 55. Fractions which have the unit (1) for their numerator are expressed as follows: 4 = يك‎ s» (= Phi. si-évak ‘of three, one’); a je, or يك‎ ile, or (by contrac.) چريت‎ or Ones go = v9; ۲. = eh زبازده‎ zip = eh زصد‎ and so on. ‘A half’ is expressed by یم‎ OF نیمه‎ (= Phl. nimak; Z. naéma), or more commonly by the Arabic ]و نصف‎ The same fractions may also be expressed by means of the genitive ;); as یکی از سه‎ ‘one of three, one-third’; and this is the method adopted when the numerator exceeds 1; e.g. دو از سه‎ ‘two-thirds’; از چهار‎ s» ‘three-fourths’; or the Arabic fractional numbers are employed for the denominator the numerator being Persian; e.g. 2 = WB دو‎ du suls; 3 = ر‎ sw sth rub (v.§ 172). In mixed numbers, the integer, as in English, precedes the fraction ; 29 و یم�� eh ‘one and a half’; wy سع و چهار‎ ‘three and one-fourth’.
```


## [2026-10-15T02:50:37.664Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"Z\\. ?.r[aā]y|Zend|sizdah|sīzdah|si-zdah|thrisat|Cardinal\" GPL.txt | head -10",
 "description": "Grep Platts cardinal numerals"
}
```


### [2026-10-15T02:50:38.046Z] TOOL RESULT

```
127:1 Modern Persian is the language of Persia under Islam. Pehlevi was the language of Persia under the Sassanides, and is the direct parent of Persian. Old Persian was the language of Persia under the Achemenides—the language in which the inscriptions of the monarchs of that dynasty were written ; the character used was the cuneiform. The sister-language of the Old Persian was the Median, or (as it is commonly, though incorrectly, called) Zend. Pehlevi is a relative noun from pahlav = parthava (i.e. pehlert = parthaviya), and means ‘the language of the Parthava or Parthians’.
168:b. Conjunct >. The letter ¢ in conjunction with و‎ (>) occurs at the beginning of some Persian words, most of them words of common occurrence; but »> is regarded by Persians as a simple sound, the و‎ being neglected in pronunciation ; e.g. حود‎ khud or khad ‘self’ (pronounced as though written aS or JS, the latter, however, only in poetry or rhyming prose) ; خوش‎ khush or khash ‘happy’; خوردن‎ khurdan ‘to eat’; خواستن‎ khastan ‘to wish’ (not to be confounded with خاستن‎ khastan ‘to rise’); خوان‎ khan ‘table’ (but yb 0 ‘ prince’); خواهر‎ khahar ‘sister’; خویش‎ khish (archaic khésh) ‘ one’s own’; حوی‎ khai ‘sweat’. y> in such words is originally a conjunct, appearing in Phl. as ۳ Av; and in Zend as hva (S. swa); e.g. خود‎ = Phi. hvat = Z. hwato- (S. swa-tas). Persian grammarians appear to have lost cognizance of this fact. They regard the é and و‎ as separate and independent letters and term the اشمام ضمع  و‎ gly vaiv-t-eshmam- i-zamma ‘the vav that has a soupgon of zamma "or according to some grammarians واو معد وله‎ vav-i-ma‘dila ‘the deflected or removed va’, which latter term is, however, more correctly given to the 3 of the words رتو ردو‎ and y=. This letter is to be omitted in trans- literation except in the last-mentioned words in which it appears as u, e.g. du, tu, and chu.
520:Numerals—The Cardinal Numbers Al
537:30. r- سی‎ (Phi. sth O.P. thrisat).
919:(the Zend vohwmano, S. vasu-manas), and the‏ باهمان or‏ بهمان or‏ بهمان
1817:fem. The Phi. zshn is, no doubt, as Darmesteter ' points out, derived from the O.P., although no such affix is found in O.P. texts. It is said to be absolutely unknown in Zend. The Vedic Sanskrit equivalent is the affix -¢shnw, which however has always an active sense.
1846:to be a modern creation. There is no trace of it either in Zend or in Sanskrit.
2550:Tar NUMERALS I. The Cardinal Numbers
```


## [2026-10-15T02:50:40.072Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 520,540p GPL.txt | cut -c1-200",
 "description": "Read Platts numerals page 41"
}
```


### [2026-10-15T02:50:40.473Z] TOOL RESULT

```
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
```


## [2026-10-15T02:50:49.328Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-499.json'))\nfor e in d['entries']:\n  for n in e['nodes']:\n    print(e['entry'],n['id'],n['lang'],n['words'][:40],n['verdict'])\"; grep -n -E \"tār|târ\" data/verification/sources/refs/HRN.txt | head -5",
 "description": "Check precedent verdicts on page 499"
}
```


### [2026-10-15T02:50:49.793Z] TOOL RESULT

```
0 1 Sanskrit tulâ, tulya confirmed
0 2 Avestan tara-âz, tara-âzu plausible
0 3 Persian tarâz; tarâzu disputed
0 4 Greek a-tlâ; Atlas plausible
0 5 Arabic  plausible
0 6 Persian atlas; atlas; atlas disputed
0 7 French  confirmed
0 8 Persian Âtlântîk confirmed
0 9 English atlas 1; Atlantic confirmed
0 10 Greek telos; talanton confirmed
0 11 English toll; talent plausible
0 12 Latin tolĕre; lâtus; trans-latŭs confirmed
0 13 English tolerate; relate; translate confirmed
```


## [2026-10-15T02:50:55.179Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 551 552 553 554 555; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | /usr/bin/grep -n -E \"سه ?تار|ستار|setâr|sitâr|si-târ\" | head -3 | sed \"s/^/leaf $n: /\"; done; for n in 648 649 650 651 652 653; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | /usr/bin/grep -n -E \"سه|thri|θri|sih|sē\" | head -4 | sed \"s/^/leaf $n: /\" | cut -c1-200; done",
 "description": "Locate Borhan pages 1096 and 1194"
}
```


### [2026-10-15T02:50:56.295Z] TOOL RESULT

```
leaf 648: 56:                 ‫ررمنق‬‫دی د‬‫آنجا جمع آیند بقدرت خدای تعالی » و باهر یکی سه زیتون یک‬
leaf 650: 37:    ‫گبهرای پهن وبراق ازخاك بیررن میآبد و کیولی سهخانه میازد که‬    ‫بزر که میشود و دربهار با‬
leaf 651: 16:‫غومشوار را نیز گفته اند ‪ -‬و بمعنی ‪ .‬ارمغان‬       ‫وکاسه‌ای شکته داشت ‪ .‬فرمان رسید کههمانجا‬
leaf 652: 50:   ‫و در فرادوی‬        ‫‪ - ۴‬در ارویای فرون وسطی ‪2‬‬                     ‫(«‪.‬م‪۳ ).‬‬   ‫صوسه‬        ‫‪۱‬‬
leaf 653: 1: ‫وحیله باشسوکرم کندم خوار رایز گوینده ‪.‬‬           ‫سو‌سه ‪ = ۱‬بروزن بوسه ‪ ۰‬کرمی باشد‬
leaf 653: 43:‫زلد کی هوشمند وزیرك است » خردمند‪.‬حکمای سبعهٌ ولان را ‪latsihpoS‬‏ میتاهید لد ‪ -‬درآتن‬
```


## [2026-10-15T02:51:01.944Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} { if ($0 ~ /ستار/) print NR-1 }' BQT_v2_pages.txt | tr '\\n' ' '; echo; awk 'BEGIN{RS=\"\\f\"} { if ($0 ~ /سه تار|سه‌تار|سهتار/) print NR-1 }' BQT_v2_pages.txt | tr '\\n' ' '; echo; awk 'BEGIN{RS=\"\\f\"} { if ($0 ~ /sitar|setar|thri|ç[iy]|Oray|θray/) print NR-1 }' BQT_v2_pages.txt | tr '\\n' ' '",
 "description": "Find Borhan leaves mentioning setar"
}
```


### [2026-10-15T02:51:02.635Z] TOOL RESULT

```
14 17 26 29 48 67 68 69 85 134 166 177 189 204 235 238 240 241 255 274 282 287 289 296 298 300 303 310 315 316 318 333 343 350 352 358 371 396 408 434 439 450 451 463 464 476 478 482 510 535 557 558 559 560 563 578 598 609 631 658 659 670 674 676 
658 660 
372
```


## [2026-10-15T02:51:05.396Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 557 558 658 659 660; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | /usr/bin/grep -E \"ستار|سه تار|سه|târ|tar|pdf page|صفحه\" | head -8 | cut -c1-250; done",
 "description": "Inspect candidate Borhan leaves"
}
```


### [2026-10-15T02:51:06.134Z] TOOL RESULT

```
== leaf 557
                        ‫بفتح اول هم آ مده ات‬              ‫وسه ببالهةٌ شرابی را نز گویند که بموجب قرار‬
                                                           ‫گویند ‪ - ۴‬و بمعنی سه توی و سهلای باشد ‪-‬‬
                                         ‫آمده است ‪.‬‬       ‫و سه تای بمعنی باز و لاله غاله و سه تووسه‬
                                        ‫‪ ۳‬رك ‪ :‬ستاره » ستار ‪.‬‬           ‫‪ :‬ستار » ستاره ‪.‬‬   ‫رك‬   ‫‪۴‬‬
  ‫ستاره‪.‬و ر که‪ :‬خاله کی‬    ‫=‬    ‫‪۹‬‬         ‫=هنا‪.‬‬
== leaf 558
 ‫‪۱۰۵۹‬‬                                                                                                                     ‫ستار‬
‫بمرض دوانگشت بافکموترل‪,‬اادزباجوب واستضوان‬                       ‫ستاره باشد که‌بعربی کو کب خوانندا ‪-‬وخیمه‌ای‬
                                                                ‫ستاره ‪ -‬بفتح اول بروزن شرارهءنوعی‬
‫ستارة رهیی ه‌کنانه از سنگه طلق‬
‫ستاره شمر ‪ ۰ ۸‬بن شین نقطه‌دار »‬
                    ‫منجم وستاره شنای رگاوبند ‪.‬‬                  ‫آمده است که بروزن آشاره باشد ؛ وبکسر اول‬
‫ستاره شمردن ‪ -‬کنابه از بدا‬                                      ‫طنبوره وسازیرا گویند که ‪-‬ه‌تار داشته‌باشد وباین‬
‫شمر‬   ‫بمعنی‌ستاره‬    ‫=‬   ‫ستاره شناس ‪٩‬‏‬                          ‫کوبند ® ‪ -‬و افزار جدول کثانرا ‪ ۱‬حم ستاره‬
== leaf 658
 ‫سه زر ‪ = ۴ ۵‬بفتح بای (‪ )۳‬فارسی ورای‬                          ‫ا سسهیه = بکر اول و فبتحای‬
‫مع»نی سه‌پرك است » و آن خطی چند‬
 ‫سه تا * ف=وبقانیبالف کشید‪..‬طنبوری‬                           ‫خواهد که‬     ‫و سیب این آدت که چون شخصی‬
               ‫رگاویند که بان سه‌تار سته باشند‪.‬‬              ‫وزود بچانی رود سه‌امب هم اه میرد تا‬   ‫تمل‬
‫سه جاده ‪ -‬باجیمبالفکشیده و فتح‬                                  ‫هر کدام که مانده شود دگربرا سوار شود‪.‬‬
 ‫دال » بمعنی ابماد ثلثه (‪ )4‬است که طول وعرض‬                  ‫سها ل‪ 4۱‬هیر وزن نخاله‪ ,‬خرده(‪)۲‬وریزه‬
                                                                 ‫یه ا‬    ‫نعا‪-‬‬   ‫سه ایوان دکما‬
      ‫له‬                  ‫ا‬       ‫خوان‬         ‫سه‬                ‫الل ومحل حفظ باشد ‪. ۴‬‬        ‫یمح‬
== leaf 659
                                                     ‫سه خواهران‪ *۰.‬کنابه‌ازبنات‌باشد‪.‬‬
                      ‫سشهر =ب‬                       ‫وآن سه ستاره است بهلوی حم از حجملهعت متارء‬
‫ورای فرشت » عمارلی بوده مشتمل‌برسه گنبد که‬           ‫بنات‌النمش که آنرا هفت اورنکه و دبا کبرلیز‬
 ‫بدان سبب سه‌دیرمیگفنه‌اندوعربان معرب ساخته‬          ‫› پمعنی‬   ‫ایجد‬   ‫دال‬
                                                                              ‫سه ذختر ‪ -‬جم‬
                 ‫سه دبر بروزن غدیر ءیخوانند ‪. ۴‬‬     ‫سه خواهران ات که کنابه ازسه سناره باشد از‬
‫قرشت کاو را میگوبند و عربان بخقويانند ‪۰‬‬              ‫سه درك = بفتح دال » بروزن ومعنی‬
‫و بعضی کوبند هر ماده کاو است ‪ - ۴‬وبفتح‌اول‬          ‫سه پرك است » وآن خطی باشد که بجهت قمار‬
== leaf 660
 ‫‪-۱۱-‬‬                                                                                                   ‫سه روح‬
‫سه غر هُدهاع = بسنی سه ابوان‬                                                          ‫بود و اورا لدانته کشت‪.‬‬
                                       ‫دماغ اس‬             ‫سه روح = بارای قرشت بواو کشیده‬
‫سه غرفه هغز= پنینی سه غرفة‬                                                    ‫حیوان ولبات وحماد باشد ‪.‬‬
       ‫دماغ است که محل فکر و محل خی‬                         ‫سه رود = با رای قرشت (‪ )۱‬بواو‬
                                    ‫حااظه باشد ‪. ۷‬‬          ‫رسیده و بدال زده » بمعذی سه‌تار است کهطنبور‬
                       ‫زن‬‫سه فمرو‬                           ‫تساهرسته باشد ؛ و بعضی کوبند چنگ و رباب‬
‫سه ھانه = باکاف فارسی بالف کشیدہ‬                            ‫سهستن ‪ = ۱‬بفتح اول و سکون سین‬
```


## [2026-10-15T02:51:12.835Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==559' BQT_v2_pages.txt | head -3; awk 'BEGIN{RS=\"\\f\"} NR==559' BQT_v2_pages.txt | /usr/bin/grep -n -E \"sitâr|setâr|sitar|Sitar|[a-z]{3,}\" | head; for n in 654 655 656 657; do echo \"== $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | head -2 | cut -c1-200; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v2_pages.txt | /usr/bin/grep -E \"[a-zA-Z]{3,}\" | head -5 | cut -c1-250; done",
 "description": "Read Borhan headers and Latin footnotes"
}
```


### [2026-10-15T02:51:13.936Z] TOOL RESULT

```
 ‫‪۱۰۵۹‬‬                                                                                                                     ‫ستار‬
‫تک ناف و آن چیزست راست ‪ ۳‬تنک و بهن‬
                                                                     ‫فر»‬
37:  ‫و ]‪ahg‬‏ ‪( rats‬چشم)‪ .‬استی ‪, stali‬‬
== 654
  ‫=( =‬                                                                                         ‫سکوك‬

== 655
                                                                                          ‫اس‬

                         ‫‪.‬ردی‬                                                            ‫‏‪ِsnd‬‬
                ‫?ھوشثمان ‪۰ ۷۰۷‬‬        ‫د اسشق ‪ , ۷۰۷۰‬افتالی ع ‪dnaguas‬‏ ‪ .‬بازند ‪10‬‬
== 656
 ‫کردیده ‪ ,‬وآن نام بتی بود ومعنی ترکیبی آن‬                        ‫سو منات ‪ = ۹‬هم اول وفتح میم‌ولون‬
‫سوم نات است بعنی صنمی است امول قمر» چه‬                           ‫بالف کشیده بروزن مهمالات‪:‬خانه‌ای بودم‌درملك‬
   ‫ازو شکو ‪۰‬ه بردلف ‪.‬‬      ‫) بیشرهتر مایل شد واگ خواهران دشبدر‬                    ‫به روهی ( ‪inihoR‬‏‬        ‫ا‬
      ‫‪EEF egy‬‬        ‫‪IEP‬‬      ‫‪TTPFITT‬‬     ‫‪ENTIRE‬‬            ‫‪OP‬‬    ‫‪0‬‬
== 657
                                                                                                                 ‫‪-۱ ۱۳-۰‬‬
‫سوی بادیدن د کنایه از شرمنده‬                                                                ‫باشد‪.‬‬          ‫اتها وحوف وطرف‬
       ‫‪SSS‬‬                                ‫سوهان ‪-‬بضماول مخفف آن سوحن («‪=: °0.‬‬
        ‫‪.nc‬‏‬                            ‫سان («‪.‬م‪ = ).‬سار(ھ‪.‬م‪ ).‬؛دراراك (سلطانآ باد) ‪nos‬‏ «مکی‬
```


## [2026-10-15T02:51:19.118Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 100 python3 tools/ref_page.py BQT:1096 --image 2>&1 | head -5; timeout 100 python3 tools/ref_page.py BQT:1194 --image 2>&1 | head -5",
 "description": "Fetch Borhan pages 1096 and 1194",
 "timeout": 220000
}
```


### [2026-10-15T02:51:19.610Z] TOOL RESULT

```
no scan of BQT covers printed page 1096 (see 'scans' in refs_online.json)
no scan of BQT covers printed page 1194 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:51:25.642Z] TOOL CALL #68: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; mkdir -p $S/dl511; cd $S/dl511; for n in 555 558; do curl -sL -m 60 -o bqt2-$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n$n.jpg\"; file bqt2-$n.jpg; done",
 "description": "Download Borhan vol 2 leaf images"
}
```


### [2026-10-15T02:51:29.511Z] TOOL RESULT

```
bqt2-555.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
bqt2-558.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-10-15T02:51:33.225Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511; for n in 555 558; do convert bqt2-$n.jpg -resize 900x bqt2-$n-s.png 2>/dev/null || magick bqt2-$n.jpg -resize 900x bqt2-$n-s.png; done; ls",
 "description": "Downscale images"
}
```


### [2026-10-15T02:51:34.528Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:51:37.286Z] TOOL CALL #70: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511/bqt2-558-s.png"
}
```


### [2026-10-15T02:51:37.306Z] TOOL RESULT

```

```


## [2026-10-15T02:51:44.230Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511; for n in 657 658; do curl -sL -m 60 -o bqt2-$n.jpg \"https://archive.org/download/borhan-ghate-v2/page/n$n.jpg\"; magick bqt2-$n.jpg -resize 900x bqt2-$n-s.png; done; ls",
 "description": "Download Borhan leaves 657-658"
}
```


### [2026-10-15T02:51:48.320Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:51:51.231Z] TOOL CALL #72: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511/bqt2-657-s.png"
}
```


### [2026-10-15T02:51:51.246Z] TOOL RESULT

```

```


## [2026-10-15T02:51:53.226Z] AGENT

Leaf 657 = p. 1193, so 658 = p. 1194.


## [2026-10-15T02:51:54.615Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511/bqt2-658-s.png"
}
```


### [2026-10-15T02:51:54.637Z] TOOL RESULT

```

```


## [2026-10-15T02:52:09.199Z] TOOL CALL #74: Bash

```json
{
 "command": "D=/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/dl511; cp $S/bqt2-558-s.png $D/1096.png; cp $S/bqt2-658-s.png $D/1194.png; cat > $D/1096.vision.txt <<'EOF'\n[Borhan-e Qate' ed. Mo'in, printed p. 1096 = archive.org borhan-ghate-v2 leaf n558 (BQT_v2_pages.txt 0-based leaf 558). Transcribed from the page image.]\n\nستار - بفتح اول بروزن قطار ، مخفف ستاره باشد که بعربی کوکب خوانند(۱) - وخیمه‌ای را نیز گویند که بجهت منع مگس و پشه زنند و آنرا درین زمان پشه‌دان گویند ؛ وبمعنی اول بکسر اول هم آمده است و این اصح است - و ساز طنبور را هم میگویند(۲) .\nستاره - بفتح اول بروزن شراره ، نوعی ازچادر باشد که آنرا شامیانه خوانند - ... وبکسر اول طنبوره و سازیرا گویند که سه تار داشته باشد و باین معنی منفصل باید نوشت(۴) ...\n\nfootnotes:\n۱ - رك : ستاره . ۲ - در زبان کنونی نیز se târ ( آلت موسیقی که دارای سه سیم است) رك : ستاره .\n۴ - از : سه + تار + ه (نسبت) : دارای سه سیم ؛ رك : ستار .\nEOF\ncat > $D/1194.vision.txt <<'EOF'\n[Borhan-e Qate' ed. Mo'in, printed p. 1194 = archive.org borhan-ghate-v2 leaf n658 (BQT_v2_pages.txt 0-based leaf 658); p. 1193 is leaf 657. Transcribed from the page image.]\n\nبیان بیست و سوم در سین بی نقطه با ها مشتمل بر سی و شش لغت و کنایت\nسه تا - با فوقانی بالف کشیده ، طنبوری را گویند که بر آن سه تار بسته باشند . (fn: رك : ستا ، ستار)\n\n(Mo'in's footnote) * سه - بکسر اول se ، پهلوی sê «نیبرگ ۲۰۳» ، ایرانی باستان çaya ، پارسی باستان th(r)itîya (سوم) ، اوستا thri ، هندی باستان trî ، «اشتق ۷۵۹» ، پازند se ، ارمنی se (در Sebuxt = فارسی سه‌بخت) ، مخفف sê ، کهن‌تر sai = اوستایی در حالت جمع اضافه thrayâm ، پارسی باستان th(r)ayâm ، بلوچی sai «هوبشمان ۷۵۹» ، کردی sî ، افغانی drê ، وخی trûi ، سنگلیچی trâi ، یغنوبی thêraî ، منجی sharâi ، سریکلی harôi ، شغنی ârrai «اشتق ۷۵۹» ؛ گیلکی sa]ta ... عددی بین دو و چهار ، دوی بعلاوهٔ یك .\nEOF\necho ok",
 "description": "Save Borhan transcriptions for 1096, 1194"
}
```


### [2026-10-15T02:52:09.593Z] TOOL RESULT

```
ok
```


## [2026-10-15T02:52:15.327Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \"https://abadis.ir/fatofa/گیتار/\" \"https://abadis.ir/fatofa/طاووس/\" \"https://abadis.ir/fatofa/سه‌تار/\"; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 511, Mo'in entry check\" 2>&1 | tail -1); echo \"$u $f\"; /usr/bin/grep -o -E \".{0,80}(\\[فر\\.|\\[دراو|فرانسوی|guitare|معین).{0,120}\" \"$f\" | head -5; done",
 "description": "Archive abadis Mo'in pages"
}
```


### [2026-10-15T02:52:24.720Z] TOOL RESULT

```
https://abadis.ir/fatofa/گیتار/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/7a84b9c8dc75f783.txt
 گیتار. ( فرانسوی ، اِ ) آلتی است از آلات موسیقی شبیه ویولون که با مضراب نواخته گردد. قیتار. قیثار. ( از المنجد ). 
 فرهنگ معین
واژه guitar در زبان انگلیسی، gitarre در زبان آلمانی و guietare در زبان فرانسوی، همگی برگرفته از واژه guitarra در زبان اسپانیایی هستند که آن خود از واژه قیثاره در زبان عربی اندلسی برگرفته شده است. ای
ترنه، گیترن ( Giteren ) ( سازی سیمی مفتولی و منسوخ شده شبیه به گیتار که به زبان فرانسوی گیترنه و به زبان اسپانیایی گیتارا گفته می شد ) و شیتارا معین شدند. در همان زمان گروه زیادی از سازهای خانواده کوردوفون، 
• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
https://abadis.ir/fatofa/طاووس/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/da7474bd3458113f.txt
 فرهنگ معین
 و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات 
https://abadis.ir/fatofa/سه‌تار/ /home/sfmqrb/git/rishe-private/data/verification/sources/web/32297b544be6d90e.txt
 فرهنگ معین
• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
 و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات
```


## [2026-10-15T02:52:27.577Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; /usr/bin/grep -A3 \"فرهنگ معین\" 7a84b9c8dc75f783.txt | head -6; /usr/bin/grep -A3 \"^ *فرهنگ معین\" da7474bd3458113f.txt | head -6",
 "description": "Read Mo'in sections"
}
```


### [2026-10-15T02:52:27.944Z] TOOL RESULT

```
 فرهنگ معین

 [ فر. ] (اِ. ) از سازهای زهی که دارای شش سیم می باشد و با انگشتان دست نواخته می شود. 

--
 آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
 فرهنگ معین

 [ معر. ] (اِ. ) = طاوس : مرغی است از نوع ماکیان که پرهای زیبا دارد به ویژه نر آن که دُم چتری بسیار زیبایی دارد. پاهای این مرغ زیبا نیست که بر اساس برخی از افسانه ها ابلیس به صورت ماری بر پای آن پیچید و وارد بهشت شد.
```


## [2026-10-15T02:52:35.543Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"قيثار|قیثار|قيتار\" AFM*.txt FVQ.txt AFA.txt ARB_mo3rb.txt 2>/dev/null | head -6; /usr/bin/grep -n -i -E \"qīṯār|qithar|qîthâr|kithara|guitarra\" LKT.txt DEV.txt PHN.txt DOZ.txt LAM.txt AFA.txt | head -8; /usr/bin/grep -n -E \"^SITAR|^Sitar|SITAR, s\\.\" HJB.txt AID.txt | head; /usr/bin/grep -n -E \"طاووس|طاوس\" AFM*.txt FVQ.txt ARB_mo3rb.txt | head -4; /usr/bin/grep -n -i -E \"tāwūs|ṭāwūs|tawus|ta[ou]s\\b\" LKT.txt FVQ.txt AFA.txt | head -5",
 "description": "Grep Semitic loan sources for qitar, tawus"
}
```


### [2026-10-15T02:52:36.176Z] TOOL RESULT

```
ARB_mo3rb.txt:16707:(م) ”*طاؤوس"" بالطهمزة وأصلها الواو ولذلك قد تسبل فيقال *”طاووس'“ 
LKT.txt:37:^  Ein  Unterschied  zwischen  Lehn-  und  Fremdwörtern,  deren  theoretische Definition  als  bekannt  vorausgesetzt  werden  darf,  konnte  hier  unmöglich  gemacht werden,  da  die  Grenzen  zwischen  ihnen  so  verschwommen  sind,  daß  in  der  Praxis in  den  weitaus  meisten  Fällen  der  persönliche  Geschmack  oder  die  Willkür  die Entscheidung  über  die  Zugehörigkeit  eines  Wortes  zu  der  einen  oder  anderen Klasse  von  Entlehnungen  treffen  müüite.
LKT.txt:41:Die  weitaus  bedeutsamste  Verbindung  des  Morgen-  und  Abendlandes im  Altertum  wurde,  wenn  von  einer  Besprechung  der  Wirkung  der  Perser- kriege in  sprachlicher  Hinsicht  abgesehen  werden  darf,  durch  den  Zug Alexanders  des  Großen  hervorgerufen.  Bis  auf  diese  Zeiten  läßt  sich  der erste  reichlichere  Abfluß  orientalischer  Begriffe  und  Wörter  in  die  griechische Sprache  und  in  den  darauf  folgenden  Jahrhunderten  ins  Latemische  zurück- führen; seitdem  erstreckt  sich  die  Wirkung  in  ununterbrochenem  Flusse bis  auf  die  heutigen  modernen  Sprachen  und  Dialekte  Europas.  Das  folgende hellenistische  Zeitalter  begünstigte  aus  hier  nicht  zu  erörternden  Gründen die  Entlehnung  orientalischen  Sprachgutes  in  hervorragendem  Maße:  die Verbreitung  des  Judentums  und  die  Entstehung  des  Christentums  gaben Anlaß  zur  Übernahme  vieler  hebräischer  und  aramäischer  Wörter  ins Griechische  und  Lateinische  [besonders  in  die  als  Kichenlatein  bezeichnete Färbung].  Mit  dem  Mittelalter  beginnt  der  Einfluß  des  Arabischen.  Nach- dem sich  der  Islam  von  den  malayisclien  Inseln  bis  zu  den  Gestaden  des Atlantischen  Ozeans  verbreitet  hatte,  war  eine  riesige  Berührungslinie  des arabischen  Sprachgebiets  mit  dem  Abendlande  geschaffen.  Der  Wortschatz der  Sprachen  der  Pyrenäenhalbinsel,  des  Spanischen,  Portugiesischen  und Katalanischen,  und  in  geringerem  Umfange  anch  der  des  ProvenzaHschen, Französischen  und  Italienischen  werden   mit  arabischen   Wörtern  derart
AFA.txt:4427:Ji^.^ iJife. 1. SS5.S ^(JLii >Grünspecht" entlehntaus
AFA.txt:8362:anzunehmen; wenigstens ist das Umgekehrte weitaus ge-
```


## [2026-10-15T02:52:40.149Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16705,16712p ARB_mo3rb.txt; /usr/bin/grep -n -E \"قيثار|قِيثار|قیتار|كيتار\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -4; /usr/bin/grep -n -i \"guitar\" DEV.txt PHN.txt DOZ.txt LAM.txt | head -4; /usr/bin/grep -n -E \"^ *SITAR|Sitar, s|SITAR,\" HJB.txt | head -3",
 "description": "Arabic mu'arrab tawus; guitar in Arabism books"
}
```


### [2026-10-15T02:52:40.503Z] TOOL RESULT

```
(م) ”*طاؤوس"" بالطهمزة وأصلها الواو ولذلك قد تسبل فيقال *”طاووس'“ 
0( اضطرب كلام أن دو يد فى ذلك ٠.‏ نقال فى (: 8خ" ) : « وطاؤزس أمحمى 


© وقد 

PHN.txt:9737:ne s'applique , chez les Orientaux , qu'à une espèce de guitare à
PHN.txt:9740:passant, que celui qui joue de cette guitare s'appelle en arabe
LAM.txt:6974:lyre (2), guitare, ou mandoline, comme traduit M. Bar-
```


## [2026-10-15T02:52:45.356Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 16708,16716p ARB_mo3rb.txt | cut -c1-200; /usr/bin/grep -n -i -E \"sitar|setar|seh-t[aā]r\" HJB.txt AID.txt | head -5; /usr/bin/grep -n -i -E \"^ *Tooky|tukki|peacock.*Tamil|togei\" HJB.txt | head -5",
 "description": "Hobson-Jobson sitar and peacock"
}
```


### [2026-10-15T02:52:45.834Z] TOOL RESULT

```
0( اضطرب كلام أن دو يد فى ذلك ٠.‏ نقال فى (: 8خ" ) : « وطاؤزس أمحمى 


© وقد 


تكلمت به العرب © ٠‏ وقال فى (؟ 9) :ج والطوس فعل ممأت ؛ ومنه أشْيّقَاق طاؤوس . 


HJB.txt:14064:form  maangkhut  ^ven  in  M'Farland's Siamese  Grammar  is  probably  from  the Malay  manggusta.  It  was  very  inter- esting to  me  to  find  that  some  distinct trace  of  this  word  was  still  preserved in  the  name  of  this  fruit  at  Patani- Kelantan  on  the  K  coast,  where  it  was called  bawah  'seta  (or  *8etar)y  i.e.  the *setar  fruit,'  as  well  as  occasionally mestar  or  mesetar,  clearly  a  corruption of  some  such  old  form  as  m^inggmar.'^ This  delicious  fruit  is  known  through- out the  Archipelago,  and  in  Siam,  oy modifications  of  the  same  name  ;  the delicious  fruit  of  the  Garcinia  Mango- stana  (Nat.  Ord.  Guttiferae).  It  is strictly  a  tropical  fruit,  and,  in  fact, near  the  coast  does  not  bear  fruit further  north  than  lat.  14**.  It  is  a native  of  the  Malay  Peninsula  and  the adjoining  islands.
```


## [2026-10-15T02:52:50.317Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -o -i -E \".{100}(tokei|t[oō]gai|tôkei|tukk?iy).{200}\" HJB.txt IEC.txt | head -4; /usr/bin/grep -n -o -E \"^pāw-.{0,300}|pauo.{0,200}\" IEC.txt | head -3; /usr/bin/grep -n -E \"^ *pavo|^ *pāvo\" LAT.txt | head -3",
 "description": "More peacock sources"
}
```


### [2026-10-15T02:52:51.315Z] TOOL RESULT

```
74746:pavo?, 720.
```


## [2026-10-15T02:52:54.513Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"pāuō|pāvō|pauō|pāuo\" LAT.txt | head -5; /usr/bin/grep -n -E \"pavo|pāvo\" LEW_1910.txt | head -5",
 "description": "Ernout-Meillet and Walde on pavo"
}
```


### [2026-10-15T02:52:54.937Z] TOOL RESULT

```
3836:heiyo I 806 Aetpavov I 809 Aewwxooncs I 789 dexavn I 761 héxoc, hexic I 761 Aéxoava I 744 hexgot 1798 héxto L778 - héxtoov I 778 Aéhnua, héAdua [821 hehinua I 763, 767 Achoxvia I 778 Aehvyiouévog I 841 AéuBocg I 781 AéEtc I 780 Aeoitay (el.) I 767 Aéxcadvov I 745 hémac, hematoc T761 Aenac I 785 Aexcaotn I 786 Aéxoow (sizil.) I 786 Aénoc, Aeric I 785 Réxoa I 785 Aentoc I 785 Réndoov I 785 héxnw 1761, 762, 785, 790 héoyn L778 hevyahéos I 830 Aevxalw I 824 hedvun I 824 Aebduoc I 27 Aevxdsg I 824, 825 Aevods I 837 Aedvdoow I 824 Aedwo, Aevotne (att.) LUG
4023:poxléo, -edw IT102 ‘ poxddc IT 102 po, wed IT 117 poaé II 129 pvdw II 140 poypes IT 119 pvddo IT 7, 122 pddoc ,,Nasse“ IR 122) 126 pdsoos ,,dpavoc* IT 139
4058:pavog (dor.) IT 93
4323:nind IT 309 miodxrva (lak.) I 493 atoea IT 212 ataoc IT 311 alooa Il 212, 311, 312 muatoc, niotic I 494 niovoes (aol.) IZ 401 nitynut, mtv IT 262, 298, 489 suttaxiov IT 311 ITixtaxocg IT 311 altvhoc IT 297, 298 TUTVWOC, MLTVVOS IT 308 nitveov IT 400 nituc IT 212, 308 smugahhic II 309 aipavoxw I 455, 521 nipiyE IT 309 atov II 211, 306, 850 ndayd (dor.) IT 315 mhaytoc, mAdyia II 314 nhayoc I 772, II 314 whaddw IT 243 mAdlw IT 315 mhaxoetc IT 313, 315 thaxodc IT 313, 388 nhavdw, mhayvdouat IT 241, 318 nhdyng IT 318 ahavoc, nAdvyn IT318 RAGE. [1 313, 315, 388 nAdoow, IT 388 nAdotwyé IT 240 mAdtiov (dor.) 11277 mhatoc IT 316 thatds I 769, ME BUG, BSE mhéec (hom., lesb.) II 328 mAEDoov I 246 ahew (att.) IT 328 ahelwv, mdetor, mAetotog (hom., att.) I 328
```


## [2026-10-15T02:53:15.629Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; /usr/bin/grep -n -E \"TREI|TREYES|TREI-\" ARY_latin_index_pages.txt | head -5; /usr/bin/grep -n -E \"^ ?سه\\b|سه تار|سه‌تار|سیزده\" ARY_pages.txt | head -8; /usr/bin/grep -n -E \"طاووس|طاوس|گیتار\" ARY_pages.txt | head",
 "description": "Grep Aryanpur for se, setar"
}
```


### [2026-10-15T02:53:16.006Z] TOOL RESULT

```
5549:BUCK: (FEAR) 1153-1155 ‘TARBEO, TREO, TREIN
10617:TRCEZI POLISH) glong) AL TREILEA —:(RUMANIAN) gly,
10655:(OLD CHURCH SLAVIC) 45 53% TREIS, TRIA GREEK) gb»
10706:DERTIEN (DUTCH) sacle ‘TREIZE (FRENCH) Wil
10709:‘TRINAST SLOVAK) | ul ‘TREIDPREZECE’ :{RUMANIAN) gh,
180:و اسب‌سواران ماهری پودند. این مردم در طی هفت قرن (از سده‌ی ششم تا سیزدهم پس از میلاد) طی
666:گسترش اقوام ترک زبان (سده‌های ششم تا سیزدهم میلادی) موجب آمپزش آنها با ایرانیان و
795:سه تیره از مردم ژرمن (به نام‌های: انگل‌ها ۸۷01.35 و سا کسون‌ها 5۸۳0875 و جوت‌ها
10904:سیزده / ۳۶۹
```


## [2026-10-15T02:53:19.437Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; sed -n 10640,10660p ARY_latin_index_pages.txt | cut -c1-200; /usr/bin/grep -n \"pdf page\" ARY_latin_index_pages.txt | awk -F: '$1<10655' | tail -1; sed -n 10895,10912p ARY_pages.txt | cut -c1-200; /usr/bin/grep -n \"pdf page\" ARY_pages.txt | awk -F: '$1<10904' | tail -1",
 "description": "Read Aryanpur 'three' pages"
}
```


### [2026-10-15T02:53:19.804Z] TOOL RESULT

```
- BARNHART: (HONE) 489 HEIN:(OLD SCANDINAVIAN) 4S 5-1-4!
ONINOS: (HONE) 446 HAR (OLD HIGH GERMAN) ls lsT
SKEAT: (HONE) 276 HAN HOLD ENGLISH) oS 8s
14H y Hevy. sgbily HONE ENGLISH) 83
HEN DANISH) 5 jlait>
at
DRE _ AFGHANT) (4) gi TARAY, THRI- §—(AVESTAN) (plea!
TRE, TRI-- :(TOKHARIAN A) A gibi (OLD PERSIAN) dials ga sh
TRAL, TARYA :(TOKHARIAN B) B s,s SAYA, THRAYAM.
(SANSKRIT) 2 Suile SE, SE(PAHLAV) jy
TRAYAS, TISRAS, TRI sT (KURDISH) 52,
EREKH, SE ARMENIAN) ga! sal BALUCHI) go sh
Be
[pdf page 367]
: dee tthe | TFA
(OLD CHURCH SLAVIC) 45 53% TREIS, TRIA GREEK) gb»
TRUE, TRI TRES (LATIN) 3
TRZY #(QLISH) eo) TROIS .(FRENCH) sil 5
a , ae wn TRES SPANISH) glilya!
Ohi (CZECH) Se ‘TRE (ITALIAN) glSls!
TRI SERBIAN) gp TREL H{RUMANIAN) gag,
10653:[pdf page 367]
هلندی (4ع7ا0): دای برهان قاطم + ۱۹۴
:
اوستایی (4ر۸۲787): اوستی (0855710): تاه
«شاند5 ,52810 ,85۷2۸ کردی (ل80.0(5): 1
پارسی باستان (288812 010): بلوچی (۲71ناستهه): 2
,81۷20۸3 سانسکریت (54(57417):
پهلری (۲ماللم۳): 59۸ ,ق5۷7۸ بکق819۸ 8 82 ب85۷2
ای
[pdf page 368]
سیزده / ۳۶۹
ارمنی (7ل40158(4): . مان پروسی کهن (۶514(۷ن2۸ ۰:۵2 517۳۸8۲
برنانی 07880)(اسم خاص) ‏ 118108
لاتین (۸710ل): »6 پسگشت‌ها هرا ۲
اسلاوی کهن (۲10شا5 نات صا): 1 و۸0 ۱
تین هام0
روسي (/551(#): زیون 9 (5011833 کتهم)
صربی (۷ل14ق588): 57 4 (کشاآم) ما ها
آلیترانی (1۸(0/هناب# 7 برهان قاطع : " ۱۹
10903:[pdf page 368]
```


## [2026-10-15T02:53:31.820Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; /usr/bin/grep -n -i -E \"Aristoph|5th|BCE|Hebrew\" 1c43ead66d7a319b.txt | head -5; /usr/bin/grep -n -E \"Proto-Iranian|Middle Persian|Avestan\" 4f0007efba68ca07.txt | head -5; /usr/bin/grep -n -E \"From|Borrowed\" 7a84b9c8dc75f783.txt | head -2",
 "description": "Check a few remaining details"
}
```


### [2026-10-15T02:53:32.154Z] TOOL RESULT

```
188: From an earlier *τᾰϝώς ( *tăwṓs ) , of Pre-Greek origin; possibly from an eastern source, perhaps from Dravidian (compare Tamil தோகை ( tōkai , “ peacock ” ) ) [ 1 ] or a Turkic source (compare Turkish tavuk ( “ hen ” ) ). Cognates include Latin pāvus , pāvō , and perhaps Hebrew טַוָּס ( ṭawwā́s ) , Aramaic טַוסָא ( ṭawsā ) , Arabic طَاوُوس ( ṭāwūs ) .
195: ( 5 th BCE Attic ) IPA ( key ) : /ta.ɔ̌ːs/ 
450: Proto-Iranian *θráyah 
1251: Proto-Iranian *θráyah 
1474: Cebuano terms derived from Proto-Iranian 
1503: Portuguese terms derived from Proto-Iranian
```


## [2026-10-15T02:57:21.032Z] TOOL CALL #85: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-511.py",
 "content": "import json\n\nW = \"https://en.wiktionary.org/wiki/\"\nTAOS = W + \"ταώς\"\nPAVO = W + \"pavo\"\nPEACOCK = W + \"peacock\"\nTAVUS = W + \"طاووس\"\nTOKAI = W + \"தோகை\"\nTREYES = W + \"Reconstruction:Proto-Indo-European/tréyes\"\nSITAR = W + \"sitar\"\nGUITAR = W + \"guitar\"\nKITHARA = W + \"κιθάρα\"\nTESTIS = W + \"testis\"\nTRIBUS = W + \"tribus\"\nTHRIZ = W + \"Reconstruction:Proto-Germanic/þrīz\"\nSE = W + \"سه\"\nGUITARRA = W + \"guitarra\"\nSETAR = W + \"سه‌تار\"\nTERTIUS = W + \"tertius\"\nAB_GITAR = \"https://abadis.ir/fatofa/گیتار/\"\nAB_TAVUS = \"https://abadis.ir/fatofa/طاووس/\"\n\n# ---------- shared reference checks ----------\nKLN_PEACOCK = {\"ref\": \"KLN:1143\", \"status\": \"partial\", \"note\": \"Klein 1966 s.v. peacock (KLN_1966.txt line 27770): 'OE. pāwa, pēa ... fr. L. pāvo, gen. pāvonis, 'peacock' ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim, 'peacocks'). The initial p- in L. pavo is due to imitative influence'. Klein supports the Tamil root and the Latin/OE/English chain, but routes Latin and Greek directly from the eastern source, not through Persian/Arabic, and has no Sanskrit link.\"}\nSKT_PEACOCK = {\"ref\": \"SKT:378\", \"status\": \"supports\", \"note\": \"Skeat, Concise Etym. Dict. s.v. Peacock (SKT_dli_revised.txt line 55507): '(L. - Pers. - Tamil; and E.) M.E. pecok ... AS. pea, pāwa; all from L. pāuo ... The same as Gk. ταώς, for ταϝώς, a peacock; the change from τ to p being due to the fact that the word was foreign both to L. and Gk. - Pers. tāwus, tāus, a peacock. - Tamil tōkei, tōgei, a peacock'. This is exactly Nourai's chain (Tamil > Persian > Greek/Latin > OE > E.); it is Skeat's 1911 view, now abandoned.\"}\nBQT1346 = {\"ref\": \"BQT:1346\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' p.1346 (BQT_v3_picofile.pdf page 139; the tool's default offset lands on pdf 141, use --pdf-page 139; transcription saved in ocr/BQT/1346.vision.txt), Mo'in's footnote s.v. طاوس: '(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ «تسیمرن. لغات دخیل اکدی ص۵۲» طبق تحقیق استاد پور داود اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته'. Source of Nourai's Dravidian > Sanskrit > Arabic/Aramaic chart (after Pourdavoud); Mo'in himself lists the Greek and Aramaic forms side by side without making Greek a daughter of Persian.\"}\nMON2203 = {\"ref\": \"MON:2203\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang-e Farsi vol.2 s.v. طاوس (MON_part1.txt line 91933): 'طاوس (طاووس) [دراویدی هندی] (اِ.) (جان.) پرنده‌ای است از راستهٔ ماکیان‌ها که اصلش از هندوستان و مالزی است'; abadis (Mo'in) s.v. طاووس: '[معر.] = طاوس'. Supports the Indian origin and the Arabic-mediated Persian form; the Aramaic tausâ is from the Borhan footnote, not this entry.\"}\n\n# ---------- shared consulted ----------\nC_KLN_PEACOCK = {\"src\": \"KLN\", \"where\": \"1966 s.v. peacock (KLN_1966.txt line 27770)\", \"stance\": \"partial\", \"note\": \"'L. pavo ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim) ... initial p- in L. pavo is due to imitative influence; cp. L. paupulo, 'the natural sound of the peacock''.\"}\nC_SKT_PEACOCK = {\"src\": \"SKT\", \"where\": \"s.v. Peacock (SKT_dli_revised.txt line 55507)\", \"stance\": \"supports\", \"note\": \"'from L. pāuo ... The same as Gk. ταώς, for ταϝώς ... Pers. tāwus, tāus, a peacock. - Tamil tōkei, tōgei' (Skeat's Tamil > Persian > Greek > Latin chain).\"}\nC_BQT1346 = {\"src\": \"BQT\", \"where\": \"p.1346, Mo'in fn. s.v. طاوس (ocr/BQT/1346.vision.txt)\", \"stance\": \"partial\", \"note\": \"'(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ ... اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته' (after Pourdavoud).\"}\nC_MON_TAVUS = {\"src\": \"MON\", \"where\": \"vol.2 s.v. طاوس (MON_part1.txt line 91933); abadis s.v. طاووس\", \"stance\": \"partial\", \"note\": \"'طاوس (طاووس) [دراویدی هندی] ... اصلش از هندوستان و مالزی است'; abadis/Mo'in s.v. طاووس '[معر.] = طاوس' (Arabicized).\"}\nC_ARB_TAVUS = {\"src\": \"ARB\", \"where\": \"al-Mu'arrab (ARB_mo3rb.txt lines 16707-16712)\", \"stance\": \"partial\", \"note\": \"'(م) «طاؤوس» بالهمزة وأصلها الواو ... وقال [ابن دريد]: وطاؤوس أعجمي ... وقد تكلمت به العرب' - the Arab philologists already treated ṭāwūs as a foreign word, without naming the source.\"}\n\nentries = []\n\n# =================== ENTRY 0: Tôkei ===================\ne0_nodes = [\n {\n  \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"\", \"verdict\": \"disputed\",\n  \"derivation\": \"Empty pass-through box: Nourai (following Pourdavoud via Mo'in's Borhan footnote) routes the Tamil word through Sanskrit before it reaches Aramaic and Arabic. No Sanskrit form of the tōkai/ṭāwūs type is attested: the Sanskrit words for 'peacock' are mayūra-, śikhin-, barhin-, kalāpin-. Modern scholarship (Wiktionary s.v. ταώς, Klein s.v. peacock) derives the Mediterranean/Semitic words either from Pre-Greek ταώς or directly from a Dravidian (Tamil tōkai) or other eastern source by sea trade, with no Sanskrit intermediary.\",\n  \"derivation_fa\": \"این خانهٔ خالی «سنسکریت» را نورایی به پیروی از پورداوود (در حاشیهٔ معین بر برهان قاطع) میان تامیلی و آرامی/عربی گذاشته است. اما در سنسکریت واژه‌ای از گونهٔ tōkai یا ṭāwūs برای طاووس دیده نمی‌شود؛ نام‌های سنسکریت طاووس mayūra، śikhin و barhin است. پژوهش امروزی (کلاین، ویکی‌واژه) واژهٔ یونانی ταώς را پیش‌یونانی می‌داند یا آن را مستقیم به منبعی شرقی مانند تامیلی tōkai می‌رساند، و گذر از سنسکریت را تأیید نمی‌کند.\",\n  \"sources\": [TAOS, TOKAI],\n  \"ref_check\": [BQT1346],\n  \"consulted\": [\n   C_KLN_PEACOCK,\n   {\"src\": \"SKT\", \"where\": \"s.v. Peacock (SKT_dli_revised.txt line 55507)\", \"stance\": \"contradicts\", \"note\": \"Skeat's chain is 'Pers. tāwus ... - Tamil tōkei' with no Sanskrit stage.\"},\n   {\"src\": \"MON\", \"where\": \"vol.2 s.v. طاوس (MON_part1.txt line 91933)\", \"stance\": \"partial\", \"note\": \"Only the tag '[دراویدی هندی]' - Dravidian/Indian, no Sanskrit form given.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Arabic\", \"words\": \"tawoos\", \"verdict\": \"disputed\",\n  \"derivation\": \"Arabic ṭāwūs (طاووس, also طاؤوس) 'peacock' is real, but it is not taken from Sanskrit: it is borrowed from Aramaic ṭawsā (טַוסָא), itself borrowed from Greek ταώς (Wiktionary s.v. طاووس: 'Borrowed from Aramaic ṭawsā, borrowed from Ancient Greek ταώς, borrowed from Pre-Greek'). The emphatic ṭ- reflects the Aramaic spelling of Greek t-, and the long ū the Greek long ō. Arab lexicographers (Ibn Durayd in al-Jawālīqī's al-Mu'arrab) already call it a foreign word (أعجمي).\",\n  \"derivation_fa\": \"«طاووس» عربی (طاؤوس) به معنای طاووس واژه‌ای واقعی است، اما از سنسکریت گرفته نشده است؛ ویکی‌واژه آن را وام‌واژه از آرامی ṭawsā و آن را از یونانی ταώς می‌داند. ط عربی برابر t یونانی در نوشتار آرامی است و ū بلند برابر ō بلند یونانی. ابن درید (در المعرّب جوالیقی) نیز آن را «أعجمی» شمرده است. پس اصل واژه درست است ولی مسیر «سنسکریت ← عربی» را پژوهش امروزی نمی‌پذیرد.\",\n  \"sources\": [TAVUS, TAOS],\n  \"ref_check\": [BQT1346],\n  \"consulted\": [C_ARB_TAVUS, C_BQT1346, C_KLN_PEACOCK]\n },\n {\n  \"id\": 3, \"lang\": \"Aramaic\", \"words\": \"tausâ\", \"verdict\": \"disputed\",\n  \"derivation\": \"Aramaic ṭawsā / ṭāwsā (טַוסָא) 'peacock' is attested and Mo'in quotes it as tausâ (after Zimmern, Akkadische Fremdwörter p.52). Wiktionary derives it from Greek ταώς (5th c. BCE Attic), the definite ending -ā being the Aramaic emphatic state; it was the channel through which the word reached Arabic. Nourai's derivation of the Aramaic word from (an unattested) Sanskrit form is not supported; the Hebrew tukkiyyim (1 Kings 10:22), which Klein ties to Tamil tōkai, is a different word.\",\n  \"derivation_fa\": \"آرامی ṭawsā (طاوسا، tausâ) «طاووس» در منابع هست و معین آن را از تسیمرن (واژه‌های دخیل اکدی، ص۵۲) نقل کرده است. ویکی‌واژه آن را از یونانی ταώς (یونانی آتیکی سدهٔ پنجم پیش از میلاد) می‌داند؛ ā پایانی نشانهٔ حالت معرفهٔ آرامی است، و همین واژه راه رسیدن طاووس به عربی بوده است. اشتقاق آن از سنسکریت پذیرفته نیست؛ واژهٔ عبری tukkiyyim (کتاب پادشاهان) که کلاین آن را با تامیلی tōkai می‌سنجد واژهٔ دیگری است.\",\n  \"sources\": [TAVUS, TAOS],\n  \"ref_check\": [{\"ref\": \"MON:2203\", \"status\": \"not_found\", \"note\": \"Mo'in's Farhang s.v. طاوس (MON_part1.txt line 91933) gives only '[دراویدی هندی]'; the Aramaic form tausâ is in his Borhan footnote p.1346 ('آرامی طاوسا tausâ «تسیمرن. لغات دخیل اکدی ص۵۲»'), not in the Farhang entry.\"}],\n  \"consulted\": [C_BQT1346, C_ARB_TAVUS, {\"src\": \"KLN\", \"where\": \"1966 s.v. peacock (KLN_1966.txt line 27770)\", \"stance\": \"silent\", \"note\": \"No Aramaic form; mentions only 'Heb. tukkiyyim' from Tamil.\"}]\n },\n {\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"tâvŭs; tâvosî\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian ṭāvūs / ṭāvus (طاووس، طاوس) 'peacock' is the Arabic ṭāwūs taken over with its Arabic spelling (ط), which is why Mo'in tags it [معر.] 'Arabicized' (abadis/Mo'in s.v. طاووس) and Wiktionary 'borrowed from Arabic'; the Arabic → Persian arrow is therefore right. ṭāvūsī (طاوسی) is the Persian relational adjective in -ī 'peacock-like, peacock-coloured', and as a noun the name of a plant: Mo'in s.v. طاوسی '(گیا.) گیاهی است از تیرهٔ پروانه‌واران ... گل‌هایش بزرگ و به رنگ زرد طلایی' (a broom-like shrub of the pea family). The Hafez couplet quoted in the box uses طاووس.\",\n  \"derivation_fa\": \"«طاووس/طاوس» فارسی همان ṭāwūs عربی است که با املای عربی (ط) به فارسی آمده؛ از این رو معین آن را [معر.] نشان داده و ویکی‌واژه آن را وام‌واژه از عربی می‌داند؛ پس پیکان عربی ← فارسی درست است. «طاوسی» صفت نسبی با پسوند ـی (به رنگ طاووس) است و در گیاه‌شناسی نام درختچه‌ای از تیرهٔ پروانه‌واران با گل‌های زرد طلایی (معین). ادعای نورایی در این خانه درست است.\",\n  \"sources\": [TAVUS, AB_TAVUS],\n  \"ref_check\": [BQT1346, MON2203],\n  \"consulted\": [\n   C_MON_TAVUS,\n   {\"src\": \"MON\", \"where\": \"vol.2 s.v. طاوسی (MON_part1.txt lines 91967-91992)\", \"stance\": \"supports\", \"note\": \"'طاوسی [معر. ف.] منسوب به طاوس ... (گیا.) گیاهی است از تیرهٔ پروانه‌واران که بصورت درختچه‌ای است ... گل‌هایش بزرگ و به رنگ زرد طلایی است'.\"},\n   C_BQT1346,\n   {\"src\": \"HRN\", \"where\": \"grep طاوس / tāvūs\", \"stance\": \"silent\", \"note\": \"Horn does not treat Arabic loanwords; no entry.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"pâuo, pâvô; pâvonîs\", \"verdict\": \"disputed\",\n  \"derivation\": \"Latin pāvō, genitive pāvōnis (also pāvus; written pauo in inscriptions) 'peacock' is correct (Ennius, Varro, Ovid). It cannot come from Persian ṭāvūs, which is a medieval Arabic loan, far later than Latin pāvō. Wiktionary: 'Likely borrowed from Ancient Greek ταώς, or possibly imitative (compare paupulō, to call like a peacock)'; Klein: Latin and Greek share an eastern source, 'the initial p- in L. pavo is due to imitative influence'. Nourai's arrow follows Skeat (1911), who wrote 'L. pāuo ... Gk. ταώς ... Pers. tāwus'.\",\n  \"derivation_fa\": \"لاتین pāvō (حالت اضافی pāvōnis) «طاووس» درست است، اما نمی‌تواند از «طاووس» فارسی باشد که خود وام‌واژهٔ عربیِ دورهٔ اسلامی و بسیار جوان‌تر از واژهٔ لاتین است. ویکی‌واژه pāvō را به احتمال از یونانی ταώς یا نام‌آوا (مقایسه با paupulō «بانگ طاووس») می‌داند و کلاین p آغازی را اثر نام‌آوایی می‌شمارد. نورایی از اسکیت (۱۹۱۱) پیروی کرده؛ این مسیر را پژوهش امروزی رد می‌کند.\",\n  \"sources\": [PAVO, TAOS],\n  \"ref_check\": [SKT_PEACOCK],\n  \"consulted\": [C_KLN_PEACOCK, C_SKT_PEACOCK, {\"src\": \"LAT\", \"where\": \"index 'pavo' (LAT.txt line 74746, p.720)\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet has pāuō at p.720; only the index line is legible in the OCR.\"}]\n },\n {\n  \"id\": 6, \"lang\": \"Greek\", \"words\": \"taws, taos\", \"verdict\": \"disputed\",\n  \"derivation\": \"Greek ταώς (taṓs, older *ταϝώς; Attic ταῶς) 'peacock' is attested from the 5th c. BCE (Aristophanes), centuries before any Persian ṭāvūs, so it cannot derive from the Persian word. Wiktionary: 'of Pre-Greek origin; possibly from an eastern source, perhaps from Dravidian (compare Tamil tōkai)'; the Aramaic and Arabic words are in fact borrowed from the Greek. The chart's direction Persian → Greek is reversed; Klein (KLN:1143) himself only says Greek and Latin 'prob. come ult. fr. Tamil'.\",\n  \"derivation_fa\": \"یونانی ταώς (taōs، کهن‌تر *tawōs) «طاووس» از سدهٔ پنجم پیش از میلاد (آریستوفانس) گواهی دارد، یعنی سده‌ها پیش از «طاووس» فارسی؛ پس نمی‌تواند از فارسی گرفته شده باشد. ویکی‌واژه آن را پیش‌یونانی و شاید از منبعی شرقی (تامیلی tōkai) می‌داند و واژه‌های آرامی و عربی را وام از یونانی. جهت پیکان «فارسی ← یونانی» وارونه است.\",\n  \"sources\": [TAOS, TAVUS],\n  \"ref_check\": [\n   dict(KLN_PEACOCK, status=\"contradicts\", note=KLN_PEACOCK[\"note\"] + \" For this node: Klein derives Gk. ταώς from Tamil, not from Persian.\"),\n   SKT_PEACOCK\n  ],\n  \"consulted\": [C_SKT_PEACOCK, C_KLN_PEACOCK, C_BQT1346]\n },\n {\n  \"id\": 7, \"lang\": \"Old English\", \"words\": \"pea\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Old English pēa, pāwa (pāwe) 'peacock' is an early West Germanic borrowing of Latin pāvō (Proto-Germanic *pāwô, cf. OHG pfāwo, German Pfau, Dutch pauw), the Latin -v- surviving as -w-. Klein: 'OE. pāwa, pēa, 'peacock' ... fr. L. pavo'; Skeat: 'AS. pea, pāwa; all from L. pāuo'; Wiktionary s.v. peacock agrees.\",\n  \"derivation_fa\": \"انگلیسی کهن pēa و pāwa «طاووس» وام‌واژهٔ کهن ژرمنی غربی از لاتین pāvō است (ژرمنی آغازین *pāwô؛ آلمانی Pfau، هلندی pauw)؛ v لاتین در اینجا به w بدل شده است. کلاین، اسکیت و ویکی‌واژه همه همین را می‌گویند؛ ادعای نورایی درست است.\",\n  \"sources\": [PEACOCK],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"Watkins' IE-roots appendix (AHD_watkins1985.txt) has no entry for peacock/pea (a non-IE loanword); grep 'PEACOCK' finds nothing.\"}],\n  \"consulted\": [C_KLN_PEACOCK, C_SKT_PEACOCK]\n },\n {\n  \"id\": 8, \"lang\": \"English\", \"words\": \"peacock; peafowl\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English peacock < Middle English pecok, pocok = OE pēa 'peafowl' + cock 'male bird'; peafowl (pea + fowl) and peahen are later parallel compounds. Wiktionary s.v. peacock: 'From Middle English pecok ... first component from Old English pēa, pāwa (peacock, peafowl), ultimately from Latin pāvō; equivalent to pea + cock'; Skeat and Klein the same.\",\n  \"derivation_fa\": \"انگلیسی peacock از انگلیسی میانه pecok، ترکیبی از pēa انگلیسی کهن (طاووس) و cock «پرندهٔ نر» است؛ peafowl و peahen ترکیب‌های همانندِ بعدی‌اند. ویکی‌واژه، اسکیت و کلاین این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\": [PEACOCK],\n  \"ref_check\": [SKT_PEACOCK],\n  \"consulted\": [C_KLN_PEACOCK, C_SKT_PEACOCK]\n }\n]\n\nentries.append({\n \"entry\": 0,\n \"root\": \"Tôkei, Tôgei\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Tamil tōkai (தோகை) 'peacock's tail; peacock' - a proposed, not proven, eastern source of Greek ταώς\",\n \"note\": \"Tamil tōkai 'tail of a peacock; peacock' is a real word (Wiktionary தோகை), and Klein (KLN:1143) and Skeat (SKT:378) both name 'Tamil tokei, tōgei' as the ultimate source of the peacock words, so Nourai's root box faithfully reports his references; Wiktionary today calls Greek ταώς 'of Pre-Greek origin; possibly ... perhaps from Dravidian (compare Tamil tōkai)', i.e. only a possibility. The internal chart, however, is wrong in its routing: (1) there is no Sanskrit intermediary (Sanskrit has mayūra-, śikhin-); (2) Arabic ṭāwūs comes from Aramaic ṭawsā, which comes from Greek ταώς, not from Sanskrit; (3) Greek ταώς (5th c. BCE) and Latin pāvō cannot derive from medieval Persian ṭāvūs - the arrows from the Persian box to Greek and Latin reproduce Skeat's 1911 chain and are reversed. Persian ṭāvūs < Arabic, OE pēa < Latin pāvō and English peacock are correct. The book's root note prints 'Tanil' for Tamil (misprint in the book, faithfully extracted). No extraction errors: JSON matches the printed page.\",\n \"note_fa\": \"تامیلی tōkai «دم طاووس؛ طاووس» واژه‌ای واقعی است و کلاین (۱۱۴۳) و اسکیت (۳۷۸) هر دو «tokei/tōgei» تامیلی را سرچشمهٔ نهایی نام طاووس در زبان‌های اروپایی دانسته‌اند؛ ویکی‌واژهٔ امروز یونانی ταώς را پیش‌یونانی و تنها «شاید» از دراویدی می‌داند. پس ریشه با احتیاط پذیرفتنی است. اما مسیرهای درون نمودار نادرست است: گذر از سنسکریت گواهی ندارد؛ «طاووس» عربی از آرامی ṭawsā و آن از یونانی ταώς است؛ و یونانی ταώς و لاتین pāvō که بسیار کهن‌ترند نمی‌توانند از «طاووس» فارسی (که خود معرّب است) آمده باشند - پیکان‌ها وارونه‌اند و از اسکیت (۱۹۱۱) گرفته شده‌اند. «طاووس» فارسی از عربی، pēa انگلیسی کهن از لاتین و peacock انگلیسی درست است. «Tanil» در یادداشت کتاب خطای چاپی به جای Tamil است؛ خطای استخراج دیده نشد.\",\n \"sources\": [TOKAI, TAOS, TAVUS, PAVO, PEACOCK],\n \"ref_check\": [KLN_PEACOCK, SKT_PEACOCK],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"vol.2 s.v. طاوس (MON_part1.txt line 91933)\", \"stance\": \"supports\", \"note\": \"'[دراویدی هندی]' - Mo'in also gives a Dravidian/Indian origin.\"},\n  C_BQT1346,\n  {\"src\": \"HJB\", \"where\": \"grep tokei/togai/tukki\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson OCR yields no Tamil peacock entry.\"}\n ],\n \"nodes\": e0_nodes\n})\n\n# =================== ENTRY 2: Trei ===================\nPOK1090 = {\"ref\": \"POK:1090\", \"status\": \"supports\", \"note\": \"Pokorny IEW pp.1090-1092 (POK_full.txt line 87142 'Root / lemma: trei-', 'Meaning: three'): 'Avestan θrāyō, θrayasm., θri n.' ... 'dreißig: Old Indie triṃśat-, Avestan θrisat-, gr. τριάκοντα, Latin trīginta' ... 'Latin tertius' ... 'Old Irish tress ... compare Latin testis witness' ... 'perhaps Latin tribus ... Umbrian trifu ... from *tri-bhu-'; 'Gothic þreis, Old English ...'. References 'WP. I 753 f.'\"}\nC_WLD = {\"src\": \"WLD\", \"where\": \"Bd. I p.753 (WLD_Bd1_pages.txt line 71389)\", \"stance\": \"supports\", \"note\": \"'trei- „drei“ Nom. m. trejes, n. tri, f. tis(o)res ... Ai. tráyaḥ m., trī (ved.), trīṇi n., tisráḥ f.; av. θrāyō m., θri n., tisrō f.; arm. erek; gr. τρεῖς ... lat. trēs, tria'.\"}\nC_AHD_TREI = {\"src\": \"AHD\", \"where\": \"Watkins, AHD IE Roots s.v. trei- (AHD_watkins1985.txt lines 1094-1096)\", \"stance\": \"supports\", \"note\": \"'trei-. Three. I. Nominative plural form *treyes. 1. Germanic *thrijiz in Old English thrīe, thrēo, thrī, three ... thritig, thirty, and thrēotīne, thirteen ... II. Zero-grade form *tri- ... b. Latin tertius ... TERTIARY ... 11. Compound form *tri-st-i-, \\\"third person standing by\\\" ..., in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY. 12. Persian sih, three: SITAR. [Pok. trei- 1090.]'\"}\nC_IEC = {\"src\": \"IEC\", \"where\": \"s.v. treies (IEC.txt line 18884)\", \"stance\": \"supports\", \"note\": \"'treies, m. 'three'. Cf. tri-, tosrio. WP I, 753 Skt. trayaḥ ... Av. θrāyō, m. id.; Per. si; Oss. ärtä; Pamiri arrai ... Lat. trēs ... Go. *þreis; OE þrēo, þrīe'.\"}\nC_SYN = {\"src\": \"SYN\", \"where\": \"13.41 THREE, p.941 (SYN.txt lines 23956, 24060)\", \"stance\": \"supports\", \"note\": \"'13.41. IE stem *tri-, nom. pl. *treyes. Walde-P. 1.753 ... Here belong all the words listed'; table lists 'Av. θrāyō'.\"}\nKLN_THREE = {\"ref\": \"KLN:1611\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. three (KLN_1966.txt line 39127): 'fr. I.-E. base *treyes, whence also OI. tráyaḥ (masc.), tisráḥ (fem.), trī (neut.), Avestic θrāyō (masc.) ... L. trēs ... Cp. third, thirteen, thirty ... tertiary ... tribe ... Cp. also the first element in testament, testicle, testify'.\"}\nGPL41 = {\"ref\": \"GPL:41\", \"status\": \"supports\", \"note\": \"Platts & Ranking, Grammar of the Persian Language p.41 §46 (GPL.txt lines 520-537): '3. ۳ سه (O.P. thri)' ... '13. ۱۳ سیزده (O.P. thridasa)' ... '30. سی (Phl. sih; O.P. thrisat)'. This is the source of Nourai's forms thri, thri-dasa, thrisat; Platts labels them 'O.P.' although they are Avestan/reconstructed (Old Persian has θr > ç).\"}\nSYN941 = {\"ref\": \"SYN:941\", \"status\": \"supports\", \"note\": \"Buck 13.41 THREE p.941 (SYN.txt lines 23956-24064): 'IE stem *tri-, nom. pl. *treyes. Walde-P. 1.753'; Avestan θrāyō in the table.\"}\nC_BRT_THRI = {\"src\": \"BRT\", \"where\": \"col. 800-806 s.vv. θray-, θridasa-, θrisant- (BRT.txt lines 14500, 14631, ~14670)\", \"stance\": \"partial\", \"note\": \"'θray- Zw., fem. tisr- 'drei'' (θrayō, θrāyō, θri); 'θridasa- Adj. 'der dreizehnte'' (ordinal, not cardinal 13); 'θri-sant- fem. Zw. 'dreissig''; no entry *θri-θatra- or any word for a three-stringed instrument among the θri- compounds (θri-afsman-, θri-gāmya-, θri-pada- ... θri-zantav-).\"}\n\ne2_nodes = [\n {\n  \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"thri, thrâyô; thrisat; thri-dasa; thri-thatra\", \"verdict\": \"plausible\",\n  \"derivation\": \"Avestan θrāyō (nom. pl. masc.), θri (neut., and compound stem θri-) continue PIE *tréyes / *tri- with the regular Iranian change of *t before *r to θ (Proto-Iranian *θráyah). Avestan θrisant-/θrisatəm 'thirty' (PIE *tri-ḱomt-, cf. Skt. triṃśat-) and θridasa- (Bartholomae: 'der dreizehnte', the ordinal 'thirteenth'; the cardinal is not separately attested) are correct apart from the 13th/13 gloss. Old Persian proper turns *θr into ç (çitiya- 'third', *çayah 'three'), so 'thri' is not the Old Persian shape; Nourai took the forms 'O.P. thri, thridasa, thrisat' from Platts's grammar (GPL:41). thri-thatra 'three-stringed instrument' is not attested in Avestan (absent from Bartholomae's θri- compounds); it is Nourai's reconstruction (θri- + *tāθra-/tār 'string', root Ten 1) to explain Persian se-tār.\",\n  \"derivation_fa\": \"اوستایی θrāyō (نهادی جمع مذکر) و θri (خنثی و ستاک ترکیبی) از هندواروپایی آغازین *tréyes / *tri- است و t پیش از r در ایرانی به θ بدل شده (ایرانی آغازین *θráyah). θrisant-/θrisatəm «سی» و θridasa- (به گفتهٔ بارتولومه «سیزدهم»، عدد ترتیبی) نیز درست است. در پارسی باستان θr به ç می‌گراید (çitiya «سوم»)، پس «thri» صورت پارسی باستان نیست؛ نورایی این صورت‌ها را از دستور پلتس (ص۴۱) گرفته است. «thri-thatra» (ساز سه‌سیم) در اوستا گواهی ندارد و در فرهنگ بارتولومه نیست؛ بازسازی خود نورایی برای توضیح «سه‌تار» است. بنابراین خانه در کل با احتیاط پذیرفتنی است.\",\n  \"sources\": [TREYES, SE],\n  \"ref_check\": [POK1090, SYN941, KLN_THREE, GPL41],\n  \"consulted\": [C_BRT_THRI, C_WLD, C_AHD_TREI, C_IEC,\n   {\"src\": \"KNT\", \"where\": \"Old Persian lexicon (KNT_full.txt)\", \"stance\": \"partial\", \"note\": \"Old Persian has only the ordinal θritiya-/çitiya- 'third' (Pokorny: 'Old pers. θritiya-'); no cardinal *θri attested.\"}]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"seh\", \"verdict\": \"confirmed\",\n  \"derivation\": \"New Persian se (سه, older written sih) 'three' < Middle Persian sē [3; Manichaean sh] (MacKenzie) < Old Persian *çayah < Proto-Iranian *θráyah (Wiktionary s.v. سه): the Old Persian/South-West Iranian change θr > ç > s gives the initial s- (Hübschmann §96: 'Ap. θr wird im Np. zu s ... si, später se 'drei''), so the Persian word is the cognate of Avestan θrāyō rather than its direct descendant. The extra forms in the box: sī (سی) 'thirty' < MP sīh < OP *çisat- (Av. θrisat-), and sīzdah (سیزده) 'thirteen' < MP sēzdah (Horn 763: 'np. sīzdeh ist eine Analogiebildung').\",\n  \"derivation_fa\": \"«سه» فارسی (در نوشتار کهن «سه/سِه») از فارسی میانه sē (مکنزی)، از پارسی باستان *çayah و ایرانی آغازین *θráyah است؛ در پارسی باستان و گویش‌های جنوب غربی θr به ç و سپس به s بدل شده (هوبشمان §۹۶)، پس «سه» هم‌ریشهٔ اوستایی θrāyō است، نه فرزند مستقیم آن. «سی» از فارسی میانه sīh (اوستایی θrisat-) و «سیزده» از فارسی میانه sēzdah است که هرن آن را ساختهٔ قیاسی می‌داند. ادعای نورایی درست است.\",\n  \"sources\": [SE, TREYES],\n  \"ref_check\": [{\"ref\": \"BQT:1194\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p.1194 (archive.org borhan-ghate-v2 leaf n658; transcription ocr/BQT/1194.vision.txt), Mo'in's footnote s.v. سه: 'سه - بکسر اول se، پهلوی sê «نیبرگ ۲۰۳»، ایرانی باستان çaya، پارسی باستان th(r)itîya (سوم)، اوستا thri، هندی باستان trî «اشتق ۷۵۹» ... کهن‌تر sai = اوستایی در حالت جمع اضافه thrayâm'.\"}],\n  \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"s.v. sē, sēzdah, sīh (PHD_mackenzie.txt lines 4535, 4549, 4553)\", \"stance\": \"supports\", \"note\": \"'sē [3; TLTA < A tlt' | M sh, N si] three'; 'sēzdah [syzdh | M syzdh] thirteen'; 'sīh [30 | M syh, N si] thirty'.\"},\n   {\"src\": \"HRN\", \"where\": \"nos. 759, 760, 763 (HRN.txt lines 6614-6641)\", \"stance\": \"supports\", \"note\": \"'759. si (geschrieben sih) 'drei' ... ap. θritiya- 'dritter'; aw. θri- 'drei'; phlv. s(i)tīgar'; '760. sī 'dreissig'. aw. θrisatəm'; '763. sizdeh 'dreizehn'. aw. θridasa 'dreizehnter' ... np. sizdeh ist eine Analogiebildung'.\"},\n   {\"src\": \"HUB\", \"where\": \"§96 (HUB.txt line 7248)\", \"stance\": \"supports\", \"note\": \"'Ap. θr wird im Np. zu s oder hr: a) zu s in: si, später se 'drei' = zd. g. pl. θrayąm, vgl. ap. θritiya- 'der dritte'; sī 'dreissig' = ap. *θrisat-, zd. θrisat-'.\"},\n   {\"src\": \"ARY\", \"where\": \"s.v. سه, pdf page 367-368 (ARY_latin_index_pages.txt line 10640ff.)\", \"stance\": \"supports\", \"note\": \"Aryanpur lists 'THRAYO, THRI- (AVESTAN)', 'ÇAYA, THRAYAM (OLD PERSIAN)', 'SE (PAHLAVI)', with a citation 'برهان قاطع ۱۱۹۴'.\"},\n   {\"src\": \"NYB\", \"where\": \"Mo'in cites Nyberg p.203 for Pahlavi sē\", \"stance\": \"supports\", \"note\": \"Cited via Borhan 1194 fn. ('پهلوی sê «نیبرگ ۲۰۳»'); not re-checked in NYB OCR.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"se-târ\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian se-tār (سه‌تار) 'a lute, originally with three strings' = se 'three' + tār 'string, thread' (Wiktionary s.v. سه‌تار: 'From سه (three) + تار (string)'). tār goes back to Middle Persian tār 'thread', from the root *tan- 'stretch' (Nourai's 'Ten 1'). Borhan-e Qate' (p.1096) records the instrument names سِتار 'ساز طنبور' and سِتاره 'طنبوره و سازی که سه تار داشته باشد', and Mo'in notes 'در زبان کنونی نیز se târ (آلت موسیقی که دارای سه سیم است)'. The arrow from Avestan θri- is right only in the sense that the first element is the numeral 'three'; the compound itself is New Persian, not Avestan.\",\n  \"derivation_fa\": \"«سه‌تار» از «سه» و «تار» (رشته، سیم) ساخته شده است (ویکی‌واژه). «تار» از فارسی میانه tār «رشته» و از ریشهٔ *tan- «کشیدن، تنیدن» است (ریشهٔ Ten 1 نورایی). برهان قاطع (ص۱۰۹۶) «سِتار» را «ساز طنبور» و «سِتاره» را «طنبوره و سازی که سه تار داشته باشد» آورده و معین در حاشیه نوشته است: «در زبان کنونی نیز se târ، آلت موسیقی که دارای سه سیم است». ترکیب، فارسی نو است نه اوستایی، ولی پیوند جزء نخست با عدد سه درست است.\",\n  \"sources\": [SETAR, SITAR],\n  \"ref_check\": [{\"ref\": \"BQT:1096\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' p.1096 (archive.org borhan-ghate-v2 leaf n558; transcription ocr/BQT/1096.vision.txt): 'ستار ... و ساز طنبور را هم میگویند(۲)'; 'ستاره ... وبکسر اول طنبوره و سازیرا گویند که سه تار داشته باشد(۴)'; Mo'in fn. 2: 'در زبان کنونی نیز se târ ( آلت موسیقی که دارای سه سیم است)'; fn. 4: 'از: سه + تار + ه (نسبت): دارای سه سیم'.\"}],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. سه‌تار (MON_part1.txt line 75495; MON_2vol_Adena_v1 line 81543)\", \"stance\": \"supports\", \"note\": \"'سه‌تار (امر.) (مس.) سازی که در قدیم دارای سه سیم بود'; 'سه تار: [= ستار = سه تا] (امر.) (مس.)'.\"},\n   {\"src\": \"BQT\", \"where\": \"p.1194 s.v. سه تا (leaf n658)\", \"stance\": \"supports\", \"note\": \"'سه تا - ... طنبوری را گویند که بر آن سه تار بسته باشند'.\"},\n   {\"src\": \"AHD\", \"where\": \"IE Roots s.v. trei- II.12 (AHD_watkins1985.txt line 1096)\", \"stance\": \"supports\", \"note\": \"'12. Persian sih, three: SITAR'; index 'SITAR ten-, trei-' - Watkins also derives the second element from *ten- 'stretch'.\"},\n   {\"src\": \"HRN\", \"where\": \"grep sitār/setār\", \"stance\": \"silent\", \"note\": \"Horn has no entry for the instrument (line 11035 only 'np. sitāre' 'star').\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Hindustani\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Empty pass-through box: Hindi सितार / Urdu ستار sitār, borrowed from Classical Persian si-tār 'three strings' (Classical Persian kept the vowel i, si/sih, which the Indian form preserves), names the long-necked North Indian lute developed in the 18th century; English took the word from Hindustani (Wiktionary s.v. sitar: 'From Hindi सितार (sitār) / Urdu ستار (sitār), from Classical Persian سه‌تار (si-tār, literally three strings)').\",\n  \"derivation_fa\": \"این خانهٔ خالی هندوستانی است: هندی/اردو «سِتار» (sitār) وام‌واژه از فارسی کلاسیک «سه‌تار» (si-tār) است که تلفظ کهن si را نگه داشته؛ نام سازی زهی و دسته‌بلند در شمال هند (سدهٔ هجدهم). انگلیسی این واژه را از هندوستانی گرفته است. ادعای نورایی درست است (ویکی‌واژه).\",\n  \"sources\": [SITAR],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"IE Roots index 'SITAR ten-, trei-' (AHD_watkins1985.txt line 2265)\", \"stance\": \"supports\", \"note\": \"Watkins assigns SITAR to Persian sih 'three' (trei-) + *ten- 'stretch'.\"},\n   {\"src\": \"HJB\", \"where\": \"grep sitar/setar (HJB.txt)\", \"stance\": \"silent\", \"note\": \"Hobson-Jobson has no sitar entry (only 'setar fruit' s.v. mangosteen, line 14064, unrelated).\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"English\", \"words\": \"sitar\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English sitar (attested from the 1840s) is borrowed from Hindi/Urdu sitār < Persian si-tār 'three-stringed' (Wiktionary s.v. sitar; 'Doublet of setar'). Watkins (AHD) lists SITAR under trei- ('Persian sih, three') and ten- (tār 'string').\",\n  \"derivation_fa\": \"انگلیسی sitar (از دههٔ ۱۸۴۰) از هندی/اردو sitār و آن از فارسی «سه‌تار» گرفته شده است؛ واتکینز (AHD) آن را زیر ریشهٔ trei- («سه» فارسی) و ten- («تار») آورده است. ادعای نورایی درست است.\",\n  \"sources\": [SITAR],\n  \"ref_check\": [{\"ref\": \"AHD:1210\", \"status\": \"partial\", \"note\": \"AHD:1210 is a page of the main dictionary (s.v. sitar), not on disk; the IE-roots appendix (Watkins, AHD_watkins1985.txt line 1096) says '12. Persian sih, three: SITAR', and the index line 2265 'SITAR ten-, trei-' - same derivation.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1971 grep 'sitar'\", \"stance\": \"silent\", \"note\": \"No sitar entry found in the Klein OCR.\"},\n   {\"src\": \"SKT\", \"where\": \"grep Sitar (SKT_dli_revised.txt)\", \"stance\": \"silent\", \"note\": \"Skeat has no entry.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Greek\", \"words\": \"kithara\", \"verdict\": \"disputed\",\n  \"derivation\": \"Greek κιθάρα (kithára) 'lyre-like stringed instrument' is attested from Homer's era onward (κίθαρις in the Iliad/Odyssey, 8th c. BCE), long before any Persian se-tār (a New Persian compound of se 'three' + tār). The resemblance is chance. Modern view (Wiktionary, after Beekes): 'acquired from Pre-Greek', possibly related to Hurro-Urartian *kinnar 'lyre' (cf. Hebrew kinnōr). Klein's 'fr. Pers. sihtar' (s.v. cither/guitar) is the old view that Nourai followed; Skeat stops at Greek.\",\n  \"derivation_fa\": \"یونانی κιθάρα (کیثارا، سازی زهی چون چنگ کوچک) از روزگار هومر (κίθαρις، سدهٔ هشتم پیش از میلاد) گواهی دارد، یعنی بسیار پیش از «سه‌تار» که ترکیبی فارسی نو است؛ همانندی این دو واژه تصادفی است. پژوهش امروزی (بیکس، ویکی‌واژه) آن را پیش‌یونانی و شاید با هوری‌ـاورارتویی *kinnar «چنگ» (عبری kinnōr) مرتبط می‌داند. سخن کلاین «از فارسی sihtar» دیدگاه کهنه‌ای است که نورایی از آن پیروی کرده؛ پژوهش امروزی آن را رد می‌کند.\",\n  \"sources\": [KITHARA, GUITAR],\n  \"ref_check\": [{\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein 1971 s.v. guitar (KLN_1971.txt line 107243): 'F. guitare, fr. Sp. guitarra, fr. Arab. qītāra, fr. Gk. κιθάρα, fr. Pers. sihtar'; s.v. cither (line 47828): 'fr. Gk. κιθάρα, fr. Pers. sihtar'. Klein does state Nourai's claim; it is rejected by modern scholarship (see derivation).\"}],\n  \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Guitar (SKT_dli_revised.txt line 33736)\", \"stance\": \"partial\", \"note\": \"'Guitar. (F.-L.-Gk.) F. guitare - L. cithara - Gk. κιθάρα, a lyre' - no Persian source.\"},\n   {\"src\": \"KLN\", \"where\": \"1971 s.v. cithara (KLN_1971.txt line 47824)\", \"stance\": \"supports\", \"note\": \"'cither ... fr. L. cithara, fr. Gk. κιθάρα, fr. Pers. sihtar'.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Arabic\", \"words\": \"qîtâr; qeetarah\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic qīthār / qīthāra (قيثار، قيثارة) 'lyre, lute' is borrowed from Greek κιθάρα through Aramaic qīthārā (קיתרא) (Wiktionary s.v. guitarra: 'borrowed from Arabic قِيثَارَة (qīṯāra), borrowed from Aramaic קיתרא (qīṯārā), borrowed from Ancient Greek κιθάρα'). Greek k- > Arabic q- and th > ṯ (often pronounced t, hence Nourai's qîtâr) are the regular renderings. Nourai's transliterations stand for qīthār and qīthāra.\",\n  \"derivation_fa\": \"عربی «قیثار/قیثارة» (qīṯāra) «گونه‌ای چنگ و عود» از یونانی κιθάρα و از راه آرامی qīṯārā گرفته شده است (ویکی‌واژه). k یونانی در عربی ق و th به ث (که اغلب t تلفظ می‌شود) بدل شده است؛ «qîtâr» و «qeetarah» نورایی همان قیثار و قیثاره است. ادعای نورایی درست است.\",\n  \"sources\": [GUITARRA, GUITAR],\n  \"ref_check\": [{\"ref\": \"SAP:1381\", \"status\": \"not_checked\", \"note\": \"Sayyah's Persian al-Munjid is not accessible (refs_online: purchase only).\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1971 s.v. guitar (KLN_1971.txt line 107243)\", \"stance\": \"supports\", \"note\": \"'fr. Sp. guitarra, fr. Arab. qītāra, fr. Gk. κιθάρα'.\"},\n   {\"src\": \"MON\", \"where\": \"abadis s.v. گیتار (Dehkhoda section)\", \"stance\": \"supports\", \"note\": \"'گیتار ... قیتار. قیثار. (از المنجد)' - the Arabic forms equated with the guitar.\"},\n   {\"src\": \"PHN\", \"where\": \"PHN.txt line 9737\", \"stance\": \"silent\", \"note\": \"Pihan speaks of 'une espèce de guitare' among Orientals but gives no qīthāra etymology.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Spanish\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Empty pass-through box: Spanish guitarra (Old Spanish guitarra, 13th c.) is borrowed from Andalusian Arabic qīthāra (Wiktionary s.v. guitarra: 'Inherited from Old Spanish guitarra, borrowed from Arabic قِيثَارَة (qīṯāra) ... Doublet of cítara'), with the Arabic q- rendered by Romance gu- [g].\",\n  \"derivation_fa\": \"این خانهٔ خالی اسپانیایی است: guitarra اسپانیایی (سدهٔ سیزدهم) وام‌واژه از عربی اندلسی «قیثارة» است و ق عربی در اسپانیایی به gu (گ) بدل شده است (ویکی‌واژه). ادعای نورایی درست است.\",\n  \"sources\": [GUITARRA],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this box.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1971 s.v. guitar\", \"stance\": \"supports\", \"note\": \"'F. guitare, fr. Sp. guitarra, fr. Arab. qītāra'.\"},\n   {\"src\": \"DEV\", \"where\": \"grep guitar (DEV.txt)\", \"stance\": \"silent\", \"note\": \"Devic has no guitare entry in the OCR.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"French\", \"words\": \"guitare\", \"verdict\": \"confirmed\",\n  \"derivation\": \"French guitare (17th c.; earlier guiterne) is borrowed from Spanish guitarra. Klein: 'F. guitare, fr. Sp. guitarra'; Skeat: 'F. guitare'.\",\n  \"derivation_fa\": \"فرانسوی guitare (سدهٔ هفدهم؛ پیش‌تر guiterne) از اسپانیایی guitarra گرفته شده است (کلاین، اسکیت). ادعای نورایی درست است.\",\n  \"sources\": [GUITAR, GUITARRA],\n  \"ref_check\": [{\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein 1971 s.v. guitar (KLN_1971.txt line 107243): 'F. guitare, fr. Sp. guitarra'.\"}],\n  \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Guitar (SKT_dli_revised.txt line 33736)\", \"stance\": \"supports\", \"note\": \"'Guitar. (F.-L.-Gk.) F. guitare'.\"},\n   {\"src\": \"KLN\", \"where\": \"1971 s.v. guitar\", \"stance\": \"supports\", \"note\": \"as above.\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"Persian\", \"words\": \"gîtâr\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian gītār (گیتار) is a modern borrowing of French guitare (the usual route of European musical terms into Persian in the 19th-20th c.); Mo'in tags it [فر.] 'French': 'از سازهای زهی که دارای شش سیم می‌باشد'.\",\n  \"derivation_fa\": \"«گیتار» فارسی وام‌واژه‌ای نو از فرانسوی guitare است و معین آن را [فر.] نشان داده و «از سازهای زهی که دارای شش سیم می‌باشد» تعریف کرده است. ادعای نورایی درست است.\",\n  \"sources\": [AB_GITAR],\n  \"ref_check\": [{\"ref\": \"MON:3502\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi vol.3 s.v. گیتار (abadis.ir/fatofa/گیتار/, Mo'in section): '[ فر. ] (اِ.) از سازهای زهی که دارای شش سیم می باشد'; Adena 2-vol ed. (MON_2vol_Adena_v2_djvu.txt line 37256): 'گیتار ... (مو.) سازی است خوش‌آهنگ که شش سیم دارد'.\"}],\n  \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Adena ed. s.v. گیتار (line 37256)\", \"stance\": \"supports\", \"note\": \"'سازی است خوش‌آهنگ که شش سیم دارد و ... با مضراب نوازند'.\"},\n   {\"src\": \"ARY\", \"where\": \"grep گیتار (ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"Aryanpur (IE roots of Persian) has no entry for the loanword.\"}\n  ]\n },\n {\n  \"id\": 11, \"lang\": \"English\", \"words\": \"guitar\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English guitar (1620s; earlier gittern from Old French guiterne) is from French guitare / Spanish guitarra < Arabic qīthāra < Greek κιθάρα (Wiktionary s.v. guitar: 'From Spanish guitarra, from Arabic قِيثَارَة (qīṯāra), from Ancient Greek κιθάρα. Doublet of cithara, cither, and zither, but not related to sitar'). The chain French → English is as drawn; note Wiktionary's explicit 'not related to sitar', which contradicts the Persian start of this branch (node #6).\",\n  \"derivation_fa\": \"انگلیسی guitar (دههٔ ۱۶۲۰) از فرانسوی guitare و اسپانیایی guitarra، از عربی قیثاره و یونانی κιθάρα است؛ ویکی‌واژه آن را دوگانهٔ cithara و zither می‌داند و صریحاً می‌گوید با sitar هم‌ریشه نیست. خود این پیکان (فرانسوی ← انگلیسی) درست است.\",\n  \"sources\": [GUITAR],\n  \"ref_check\": [{\"ref\": \"KLN:687\", \"status\": \"supports\", \"note\": \"Klein 1971 s.v. guitar (KLN_1971.txt line 107243): 'guitar, n., a stringed musical instrument. — F. guitare, fr. Sp. guitarra, fr. Arab. qītāra, fr. Gk. κιθάρα'.\"}],\n  \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"s.v. Guitar (SKT_dli_revised.txt line 33736)\", \"stance\": \"supports\", \"note\": \"'Guitar. (F.-L.-Gk.) F. guitare - L. cithara - Gk. κιθάρα'.\"},\n   {\"src\": \"KLN\", \"where\": \"1971 s.v. guitar\", \"stance\": \"supports\", \"note\": \"as above.\"}\n  ]\n },\n {\n  \"id\": 12, \"lang\": \"Sogdian\", \"words\": \"dry\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian δry /θrē, šē/ 'three' (Buddhist script δry, Manichaean 'dry, Christian šy) continues Old Iranian *θraya- < PIE *tréyes; Gharib entry 3618: 'δry B ... θre, se < *θraya-; Khwar. sy; Yaghn. tiray; Parth. hry ... three'. Nourai's 'dry' is the transliteration δry with δ rendered d.\",\n  \"derivation_fa\": \"سغدی δry (θrē، با املای مانوی 'dry و مسیحی šy) «سه» از ایرانی باستان *θraya- و هندواروپایی آغازین *tréyes است؛ قریب (مدخل ۳۶۱۸) آن را با خوارزمی sy، یغنابی tiray و پارتی hry سنجیده است. «dry» نورایی همان δry است. ادعای نورایی درست است.\",\n  \"sources\": [TREYES],\n  \"ref_check\": [{\"ref\": \"SOD:143\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary p.142-143 (SOD_pages.txt 0-based leaf 208), entry 3618: 'δry B ... θre, se < *θraya-; Khwar. sy; Yaghn. tiray; Parth. hry ... three. GMS 1316; EGS ii 100'. Also intro (leaf 54): '/se/ B δry, sy ... three Av. θraya-'.\"}],\n  \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"intro table, leaf 54\", \"stance\": \"supports\", \"note\": \"'/se/ B δry, sy, M 'dry ... three Av. θraya-'.\"},\n   {\"src\": \"POK\", \"where\": \"p.1090 (POK_full.txt line 87142)\", \"stance\": \"silent\", \"note\": \"Pokorny lists Avestan, not Sogdian, forms.\"}\n  ]\n },\n {\n  \"id\": 13, \"lang\": \"Germanic\", \"words\": \"thrijiz\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *þrijiz (Watkins' *thrijiz; Wiktionary *þrīz 'from earlier *þreiz, from earlier *þrejiz, from PIE *tréyes') shows Grimm's law *t > þ and the nominative plural ending *-es > *-iz; it underlies Gothic þreis, Old Norse þrír, OHG drī, Old English þrīe, þrēo.\",\n  \"derivation_fa\": \"ژرمنی آغازین *þrijiz (ویکی‌واژه: *þrīz از *þrejiz کهن‌تر) از هندواروپایی *tréyes است؛ بر پایهٔ قانون گریم t به þ (ث) بدل شده و پایانهٔ جمع *-es به *-iz. گوتی þreis، نورس کهن þrír و انگلیسی کهن þrēo از آن است. ادعای نورایی درست است.\",\n  \"sources\": [THRIZ, TREYES],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. trei- (AHD_watkins1985.txt line 1094): 'I. Nominative plural form *treyes. 1. Germanic *thrijiz in Old English thrīe, thrēo, thrī, three'.\"}],\n  \"consulted\": [C_WLD, C_IEC, {\"src\": \"POK\", \"where\": \"p.1090\", \"stance\": \"supports\", \"note\": \"'Gothic þreis, Akk. þrins, n. þrija, Old Icelandic þrír, Old High German drī'.\"}]\n },\n {\n  \"id\": 14, \"lang\": \"English\", \"words\": \"three, thirty, thirteen\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English three < OE þrīe/þrēo < PGmc *þrīz; thirty < OE þrītig (*þrī- + -tig 'ten', with metathesis þri- > thir- in Middle English); thirteen < OE þrēotīne (þrēo + tīene 'ten'), likewise metathesized. Watkins: 'thrītig, thirty, and thrēotīne, thirteen: THREE, THRICE, THIRTY, THIRTEEN'; Klein s.v. three.\",\n  \"derivation_fa\": \"انگلیسی three از انگلیسی کهن þrēo/þrīe است؛ thirty از þrītig (سه + ‑tig «ده») و thirteen از þrēotīne (سه + «ده») که در انگلیسی میانه با قلب thri به thir بدل شده‌اند. واتکینز و کلاین این را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\": [THRIZ],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this box.\"}],\n  \"consulted\": [C_AHD_TREI, {\"src\": \"KLN\", \"where\": \"1966 s.v. three (KLN_1966.txt line 39127)\", \"stance\": \"supports\", \"note\": \"'three ... ME. thre, threo, thri, fr. OE. þrī, þrīe (masc.), þrēo ... Cp. third, thirteen, thirty, thrice'.\"}]\n },\n {\n  \"id\": 15, \"lang\": \"Latin\", \"words\": \"teri, tri; tes-tis; tribus\", \"verdict\": \"plausible\",\n  \"derivation\": \"Latin has trēs, tria 'three', the combining form tri- (tripēs) and ter 'thrice', tertius 'third' (< *tritios, Wiktionary s.v. tertius); 'teri' is not a Latin word - it looks like Nourai's abstraction of the ter- of ter/tertius (Hittite has teri-). testis 'witness' < *terstis < Proto-Italic *tristos < PIE *tri-sth₂-i- 'third party standing by' (Wiktionary s.v. testis; Watkins *tri-st-i-; Oscan trstus) - confirmed. tribus 'tribe, one of the three original divisions of the Roman people (Ramnes, Tities, Luceres)' is traditionally *tri- + *bʰuH- 'be' (Pokorny 'perhaps', Klein) or *tri-dʰh₁-o- (Wiktionary gives both); the link with 'three' is accepted, but Nourai's gloss 'third class citizens' is a misunderstanding of 'a third part (of the people)'.\",\n  \"derivation_fa\": \"در لاتین «سه» trēs/tria است، با جزء ترکیبی tri-، ter «سه بار» و tertius «سوم» (از *tritios)؛ «teri» واژهٔ لاتین نیست و گویا برداشت نورایی از ter/tertius است. testis «گواه» از *terstis و هندواروپایی *tri-sth₂-i- «سومین کسی که (کنار دو طرف دعوا) می‌ایستد» است و درست است. tribus «قبیله، یکی از سه بخش نخستین مردم روم» را از *tri- و ریشهٔ *bʰuH- «بودن» (یا *dʰeh₁- «نهادن») می‌دانند؛ پیوند با «سه» پذیرفته است ولی معنای «شهروندان طبقهٔ سوم» در کتاب نادرست است (یعنی «یک‌سوم مردم»). در کل با احتیاط پذیرفتنی است.\",\n  \"sources\": [TESTIS, TRIBUS, TERTIUS, TREYES],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference cited for this box; Pokorny p.1090-1092 (root ref) covers it: 'Latin tertius ... compare Latin testis witness ... perhaps Latin tribus ... Umbrian trifu ... from *tri-bhu-'.\"}],\n  \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.1090-1092 (POK_full.txt lines 87142-87210)\", \"stance\": \"supports\", \"note\": \"'Latin trēs (Akk. also trīs), tria ... Latin tertius ... (from *tritio-)' ; 'compare Latin testis witness, testifier (also testicle)'; 'perhaps Latin tribus dividing off of people, administrative district, Umbrian trifu ... from *tri-bhu-'.\"},\n   {\"src\": \"KLN\", \"where\": \"1966 s.v. tribe (KLN_1966.txt line 40044)\", \"stance\": \"supports\", \"note\": \"'L. tribus, 'tribe', prob. meaning orig. 'the third part of the Roman people', rel. to Umbr. trifu, fr. Italic *tribhu-, 'a third', which is compounded of *tri-, 'three' and I.-E. *bhu-, *bheu-, 'to be''.\"},\n   C_AHD_TREI\n  ]\n },\n {\n  \"id\": 16, \"lang\": \"English\", \"words\": \"tertiary, tricycle; testimony, contest, protest; tribe, tribune, tribute\", \"verdict\": \"confirmed\",\n  \"derivation\": \"tertiary < Latin tertiārius 'of the third' (tertius); tricycle is a 19th-c. hybrid of Latin/Greek tri- + Greek kyklos (via French tricycle); testimony < Late Latin testimōnium, contest < contestārī 'call to witness', protest < prōtestārī 'declare publicly', all from testis 'witness' (Watkins: 'TESTAMENT, (TESTIMONY); ATTEST, CONTEST ... PROTEST'); tribe < Latin tribus, tribune < tribūnus 'head of a tribe', tribute < tribūtum 'tax levied by tribes' (Klein: 'cp. tribunal, tribune, tribute').\",\n  \"derivation_fa\": \"tertiary از لاتین tertiārius (از tertius «سوم»)؛ tricycle ترکیبی دورگه از tri- و یونانی kyklos (سدهٔ نوزدهم)؛ testimony، contest و protest از ستاک testis «گواه»؛ و tribe، tribune (سرکردهٔ قبیله) و tribute (باج گرفته‌شده بر پایهٔ قبیله‌ها) از tribus لاتین‌اند. واتکینز و کلاین همه را تأیید می‌کنند؛ ادعای نورایی درست است.\",\n  \"sources\": [TESTIS, TRIBUS, TERTIUS],\n  \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins s.v. trei- (AHD_watkins1985.txt lines 1094-1096): 'Latin tertius ... TERCEL, TERCET, TERTIAN, TERTIARY'; '2. Latin tri-, three: TRI-'; '*tri-st-i- ... in Latin testis, a witness: TESTAMENT, (TESTIMONY); ATTEST, CONTEST, DETEST, OBTEST, PROTEST, TESTIFY'. Watkins does not list TRIBE under trei-.\"}],\n  \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 s.v. tribe (line 40044), three (line 39127)\", \"stance\": \"supports\", \"note\": \"'See be, future, and cp. tribunal, tribune, tribute'; s.v. three: 'tertiary ... tribe ... Cp. also the first element in testament, testicle, testify'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Tribe (SKT_dli_revised.txt line 82890)\", \"stance\": \"supports\", \"note\": \"'Tribe, a race. (F. - L.) F. tribu ... L. tribus'.\"}\n  ]\n }\n]\n\nentries.append({\n \"entry\": 2,\n \"root\": \"Trei\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *tréyes (nom. pl. m.), stem *tri- 'three' (Pokorny trei- 1090-1092; Watkins trei-)\",\n \"note\": \"Pokorny pp.1090-1092 'trei- three', Watkins/AHD 'trei-. Three', Walde-Pokorny I 753, Buck 13.41 and Mann 'treies' all agree; root, label and gloss correct. Nearly all branches are standard. Problems: (1) the Avestan/Old Persian box mixes genuine Avestan θrāyō, θri, θrisat-, θridasa- ('thirteenth') with the unattested θri-θatra 'three-stringed instrument' (Nourai's reconstruction) and labels Platts's forms 'O.P.' though Old Persian has ç < θr; (2) Greek κιθάρα is not from Persian se-tār (Klein's old view, which Nourai follows; modern: Pre-Greek, cf. kinnōr) - the guitar line (Arabic qīthāra > Spanish > French > Persian/English) is itself correct but belongs to κιθάρα, not to 'three'; (3) Latin 'teri' is not a Latin form and the gloss of tribus as 'third class citizens' is a misreading of 'a third part of the people'. No extraction errors: the JSON matches the printed page.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *tréyes «سه» (ستاک *tri-) را پوکورنی (ص۱۰۹۰–۱۰۹۲)، واتکینز، والده‌ـپوکورنی (۱/۷۵۳)، باک و مان تأیید می‌کنند؛ ریشه، برچسب و معنا درست است و بیشتر شاخه‌ها پذیرفته‌اند. اشکال‌ها: در خانهٔ اوستایی «thri-thatra» (ساز سه‌سیم) گواهی ندارد و بازسازی خود نورایی است و صورت‌ها به پیروی از پلتس «پارسی باستان» نامیده شده‌اند، حال آنکه در پارسی باستان θr به ç بدل می‌شود؛ یونانی κιθάρα از «سه‌تار» فارسی نیست (دیدگاه کهنهٔ کلاین؛ امروز آن را پیش‌یونانی می‌دانند)، هرچند زنجیرهٔ قیثاره ← guitarra ← guitare ← گیتار/guitar درست است ولی به «سه» ربطی ندارد؛ و «teri» لاتین نیست و tribus «یک‌سوم مردم» است نه «شهروندان طبقهٔ سوم». خطای استخراج دیده نشد.\",\n \"sources\": [TREYES, THRIZ, SE],\n \"ref_check\": [POK1090],\n \"consulted\": [C_WLD, C_AHD_TREI, C_IEC, C_SYN, C_BRT_THRI],\n \"nodes\": e2_nodes\n})\n\nout = {\n \"pdf_page\": 511,\n \"book_page\": 481,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-10-14\",\n \"entries\": entries\n}\nwith open(\"/home/sfmqrb/git/rishe-private/data/verification/page-511.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\")\n"
}
```


### [2026-10-15T02:57:21.057Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/gen-511.py (file state is current in your context — no need to Read it back)
```


## [2026-10-15T02:57:28.183Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; /usr/bin/grep -n -E \"^ ?(çitiya|ϑritiya|θritiya|citiya)|çitiya-|ϑ?ritiya- \" KNT_full.txt | head -5",
 "description": "Grep Kent for 'third'"
}
```


### [2026-10-15T02:57:28.721Z] TOOL RESULT

```
26313:citiya- adj. ‘third’: Av. 6ritya-, Sks. trtiya-,
```


## [2026-10-15T02:57:36.316Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='gen-511.py'; s=open(p).read()\ns=s.replace('''{\"src\": \"KNT\", \"where\": \"Old Persian lexicon (KNT_full.txt)\", \"stance\": \"partial\", \"note\": \"Old Persian has only the ordinal θritiya-/çitiya- 'third' (Pokorny: 'Old pers. θritiya-'); no cardinal *θri attested.\"}''','''{\"src\": \"KNT\", \"where\": \"lexicon s.v. çitiya- (KNT_full.txt line 26313)\", \"stance\": \"partial\", \"note\": \"'çitiya- adj. 'third': Av. θritya-, Skt. tṛtīya-' - Old Persian attests only the ordinal, with ç < θr; no cardinal *θri, *θrisat or *θridasa in Old Persian.\"}''')\ns=s.replace('''{\"src\": \"MON\", \"where\": \"abadis s.v. گیتار (Dehkhoda section)\", \"stance\": \"supports\", \"note\": \"'گیتار ... قیتار. قیثار. (از المنجد)' - the Arabic forms equated with the guitar.\"}''','''{\"src\": \"Dehkhoda (web)\", \"where\": \"abadis.ir/fatofa/گیتار/ (Dehkhoda section)\", \"stance\": \"supports\", \"note\": \"'گیتار. (فرانسوی، اِ) آلتی است از آلات موسیقی ... قیتار. قیثار. (از المنجد)' - the Arabic forms equated with the guitar.\"}''')\nopen(p,'w').write(s)\nEOF\ngrep -c \"Dehkhoda (web)\" gen-511.py; grep -c \"line 26313\" gen-511.py; python3 gen-511.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-511.json >/dev/null && echo valid && python3 tools/verify_check.py 511",
 "description": "Patch, generate, validate, run check"
}
```


### [2026-10-15T02:57:36.935Z] TOOL RESULT

```
1
1
written
valid
nodes verified: 24/24
node verdicts: {'disputed': 6, 'confirmed': 16, 'plausible': 2}
root verdicts: {'plausible': 1, 'confirmed': 1}
ref checks: {'partial': 5, 'not_found': 2, 'supports': 16, 'contradicts': 1, 'not_checked': 5}
books consulted: {'partial': 17, 'contradicts': 1, 'silent': 11, 'supports': 37} | by book: {'KLN': 16, 'SKT': 10, 'MON': 5, 'BQT': 5, 'AHD': 5, 'HRN': 3, 'POK': 3, 'ARB': 2, 'WLD': 2, 'IEC': 2, 'ARY': 2, 'LAT': 1, 'BRT': 1, 'KNT': 1, 'PHD': 1, 'HUB': 1, 'NYB': 1, 'HJB': 1, 'Dehkhoda (web)': 1, 'PHN': 1, 'DEV': 1, 'SOD': 1}
```


## [2026-10-15T02:57:49.586Z] TOOL CALL #88: SubagentHandback

```json
{
 "message": "I verified page 511 (book page 481) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-511.json. `verify_check.py 511` reports 24/24 nodes verified and 0 PROBLEM lines. The page has 2 roots to check; Tr is a redirect and was skipped.\n\n**Verdicts**\n- **Nodes (24):** 16 confirmed, 2 plausible, 6 disputed.\n- **Roots:** Tôkei is plausible. Klein and Skeat name Tamil tōkei as the source; Wiktionary today says only \"perhaps Dravidian\". Trei is confirmed (PIE *tréyes, Pokorny 1090).\n\n**Disputed (6)**\n- **Tôkei #1, Sanskrit (empty box):** no Sanskrit form of this kind exists (Sanskrit has mayūra-, śikhin-). The Sanskrit step comes from Pourdavoud, quoted in Mo'in's footnote in Borhan-e Qate' (BQT 1346).\n- **Tôkei #2, Arabic tawoos:** Arabic ṭāwūs comes from Aramaic ṭawsā, which comes from Greek ταώς, not from Sanskrit.\n- **Tôkei #3, Aramaic tausâ:** borrowed from Greek ταώς, not from Sanskrit.\n- **Tôkei #5, Latin pâvô:** cannot come from medieval Persian ṭāvūs, which is itself an Arabic loan. It is from Greek ταώς or imitative. Nourai is following Skeat's 1911 chain.\n- **Tôkei #6, Greek taos:** attested in the 5th c. BCE, centuries before the Persian word, so the arrow runs the wrong way.\n- **Trei #6, Greek kithara:** κιθάρα is Homeric and has nothing to do with Persian se-tār. Modern sources treat it as Pre-Greek (compare kinnōr). Klein (KLN:687) does say \"fr. Pers. sihtar\", but that view is outdated.\n\n**Plausible (2)**\n- **Trei #1, Avestan:** thri-thatra is unattested (Nourai's own reconstruction). θridasa- means \"thirteenth\", not \"thirteen\". The forms are labelled Old Persian after Platts (GPL:41), although Old Persian turns θr into ç.\n- **Trei #15, Latin:** \"teri\" is not a Latin form. Tribus means \"a third part of the people\", not \"third-class citizens\".\n\n**Extraction errors:** none; the JSON matches the printed page. The root note's \"Tanil\" for Tamil is a misprint in the book itself, copied faithfully.\n\n**Files I added**\n- In data/verification/sources/refs/ocr/BQT/: transcriptions 1346.vision.txt, 1096.vision.txt and 1194.vision.txt, with the matching .png page images.\n- **BQT:1346 points at the wrong page.** The tool's default offset (-1205) renders the wrong pdf page; the entry is on pdf page 139 of BQT_v3. I overwrote 1346.png with the correct page.\n- BQT 1096 and 1194 are not covered by ref_page.py. I took them from archive.org borhan-ghate-v2, leaves n558 and n658.\n- All web sources are archived with fetch_source.py. Etymonline returned errors on fetch, so it is not cited.\n"
}
```


### [2026-10-15T02:57:49.949Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
