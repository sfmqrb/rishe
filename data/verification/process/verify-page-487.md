# Verification process log — verify-page-487


## [2026-09-14T03:08:29.853Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 487 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-487.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-487.json. Write /home/sfmqrb/git/rishe/data/verification/page-487.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 487` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:30.827Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:31.616Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:31.637Z] TOOL RESULT

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


## [2026-09-14T03:08:32.050Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-487.txt"
}
```


### [2026-09-14T03:08:32.073Z] TOOL RESULT

```
1	=== PDF page 487 (book page 457) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Su 2 : wild boar, pig  (refs POK:1038)
4	#1 (parent #0) [Avestan] refs=POK:1038 | hu 2 : wild boar ; hu-xerpa : boar-shaped, pig ☞Sek
5	  #2 (parent #1) [Persian] refs=HRN:113 | xŭk «خوک» : pig
6	#3 (parent #0) [Greek] refs=AHD | sŭs : swine ; sŭs-philos : friend of swine ☞Bhili ; huaina : hyena
7	  #4 (parent #3) [Latin] refs=AHD:1306; KLN:1561 | Syphilus : name of a shepherd in a poem by a physician (1530) who was the first victim of a disease that was later named after his poem hero, Syphilis. ; hyaena : hyena
8	    #5 (parent #4) [French] refs=None | 
9	      #6 (parent #5) [Persian] refs=MON:1979 | sîflîs «سیفلیس» ; seflîs «سفلیس»
10	    #7 (parent #4) [English] refs=AHD; KLN | hyena, syphilis
11	#8 (parent #0) [Germanic] refs=AHD | swînam : swine
12	  #9 (parent #8) [English] refs=None | swine
13	#10 (parent #0) [Celtic] refs=AHD | sukko : hog
14	  #11 (parent #10) [English] refs=None | hog
15	#12 (parent #0) [Latin] refs=AHD | sus : pig, anything dirty
16	  #13 (parent #12) [English] refs=None | soil
17	--- entry 1 ---
18	ROOT Sŭ 3 -> redirect to Sâwel
19	--- entry 2 ---
20	ROOT Sŭ 4 -> redirect to Seu 3
21	--- entry 3 ---
22	ROOT Sua -> redirect to Kwon
23	--- entry 4 ---
24	ROOT [Indo-European] Suîğ : jump, dance  (refs IEC:1354)
25	#1 (parent #0) [Avestan / Old Persian] refs=HRN:103; ETM:66 | haiz : to rise ; xvîsat : he rises ; xaezanuha : raise, rise ; pairi-xaezanuha : raise, rise ☞Per 1
26	  #2 (parent #1) [Pahlavi] refs=NYB:39; FVS:199 | xâstan, xĕzistan : to rise ; rist-axez : (the day of) rising dead ☞Leith
27	    #3 (parent #2) [Persian] refs=BQT:700,745,948; HRN:103; IEC:1354 | xâstan «خاستن ، برخاستن» : to rise ; rastâxîz «رستاخیز، رستخیز» : rising of the dead | extra: خیز، خیزیدن، برخیزیدن، خزیدن، خَز
28	#4 (parent #0) [Avestan] refs=HRN:102 | haxš : to rise
29	#5 (parent #0) [Middle German] refs=IEC:1354 | swicken : to jump, dance
30	
```


## [2026-09-14T03:08:35.199Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-487.json",
 "description": "Read source JSON for page 487"
}
```


### [2026-09-14T03:08:35.267Z] TOOL RESULT

```
{
  "pdf_page": 487,
  "book_page": 457,
  "entries": [
    {
      "root": {
        "name": "Su 2",
        "lang": "Indo-European",
        "refs": "POK:1038",
        "gloss": "wild boar, pig"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:1038",
          "words": [
            {"translit": "hu 2", "gloss": "wild boar", "script": null},
            {"translit": "hu-xerpa", "gloss": "boar-shaped, pig", "script": null, "see": ["Sek"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:113",
          "words": [
            {"translit": "xŭk", "gloss": "pig", "script": "خوک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "sŭs", "gloss": "swine", "script": null},
            {"translit": "sŭs-philos", "gloss": "friend of swine", "script": null, "see": ["Bhili"]},
            {"translit": "huaina", "gloss": "hyena", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": "AHD:1306; KLN:1561",
          "words": [
            {"translit": "Syphilus", "gloss": "name of a shepherd in a poem by a physician (1530) who was the first victim of a disease that was later named after his poem hero, Syphilis.", "script": null},
            {"translit": "hyaena", "gloss": "hyena", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:1979",
          "words": [
            {"translit": "sîflîs", "gloss": null, "script": "سیفلیس"},
            {"translit": "seflîs", "gloss": null, "script": "سفلیس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "hyena, syphilis", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "swînam", "gloss": "swine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "swine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Celtic",
          "refs": "AHD",
          "words": [
            {"translit": "sukko", "gloss": "hog", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hog", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "sus", "gloss": "pig, anything dirty", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "soil", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Sŭ 3", "redirect": "Sâwel"},
      "nodes": []
    },
    {
      "root": {"name": "Sŭ 4", "redirect": "Seu 3"},
      "nodes": []
    },
    {
      "root": {"name": "Sua", "redirect": "Kwon"},
      "nodes": []
    },
    {
      "root": {
        "name": "Suîğ",
        "lang": "Indo-European",
        "refs": "IEC:1354",
        "gloss": "jump, dance"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "HRN:103; ETM:66",
          "words": [
            {"translit": "haiz", "gloss": "to rise", "script": null},
            {"translit": "xvîsat", "gloss": "he rises", "script": null},
            {"translit": "xaezanuha", "gloss": "raise, rise", "script": null},
            {"translit": "pairi-xaezanuha", "gloss": "raise, rise", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "NYB:39; FVS:199",
          "words": [
            {"translit": "xâstan, xĕzistan", "gloss": "to rise", "script": null},
            {"translit": "rist-axez", "gloss": "(the day of) rising dead", "script": null, "see": ["Leith"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:700,745,948; HRN:103; IEC:1354",
          "words": [
            {"translit": "xâstan", "gloss": "to rise", "script": "خاستن ، برخاستن"},
            {"translit": "rastâxîz", "gloss": "rising of the dead", "script": "رستاخیز، رستخیز"}
          ],
          "script_extra": "خیز، خیزیدن، برخیزیدن، خزیدن، خَز",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:102",
          "words": [
            {"translit": "haxš", "gloss": "to rise", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Middle German",
          "refs": "IEC:1354",
          "words": [
            {"translit": "swicken", "gloss": "to jump, dance", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T03:08:35.756Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:35.808Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
```


## [2026-09-14T03:08:42.524Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 1038 area (sū-) ===\"\ngrep -n \"sū-s\" POK_full.txt | head -30\necho \"--- grep suk\"\ngrep -n \"^sū-, suH\" POK_full.txt | head\ngrep -n \"1038\" POK_full.txt | head -5"
}
```


### [2026-09-14T03:08:42.625Z] TOOL RESULT

```
=== POK 1038 area (sū-) ===
--- grep suk
83273:Page(s): 1037-1038 
84594:Page(s): 1038-1039
```


## [2026-09-14T03:08:44.116Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 1354 ===\"\ngrep -n \"swicken\" IEC.txt | head -20\necho \"=== IEC sweig ===\"\ngrep -n -i \"sueig\\|sweig\\|suīg\\|suig\" IEC.txt | head -30"
}
```


### [2026-09-14T03:08:44.209Z] TOOL RESULT

```
=== IEC 1354 ===
17925:time’; be-swich, m. (1) ‘departure’; OE swican, sv. 1. (1) *wander, MLG (z-gde) swicken, v. ‘hop; wind, bind’; Du. zwikken, v. “get sprained, be wricked'; zwik, m. 'sprain'; E to switch, v. ‘to change"; Icel. cf. svikull, adj. 'elusive'; Cz. (initial variant) švih, m. ‘élan, dash” beside svižný, adj. ‘sprightly’; Li. cf. (o-gde) svaigüs ‘dizzy; intoxicating’. (For OE swican (1) (cheat; Sw. svika, v. id.; svek, n. ‘cunning’, fr. *suoi$- see suei$-)
18061:sulg- (1) “jump, dance’ Av. Xiz-, v. ‘jump’; Per. xizam, Idan, v. “leap, jump up’; Xiz, s. (rise; leap; MHG swicken, v. (D “jump, dance”
=== IEC sweig ===
17907:sual- — sueig- (suoig-, suig-)
17923:sueig- (suoig-, sulg-) ‘turn, twist, spin’. Cf. suoig- as sep. entry W cf. chwi, pl. on m. (‘quick turn, spin’, fr. *suig-); MHG swich, sm. “going, passage of
17926:sueig- (suig-) ‘delude, lure; wander, rave’. Cf. sui$no, ið Arm. cf. keni, gs: Kenvo, ab. s. Kcneav, adj. '*wheedling; Kcnim, v. ‘flatter, wheedle’; OHG, MHG swichan, swichen, v. ‘delude’; swiche, sf. ‘fraud’; OE swican, sv. 1. ‘deviate; delude, cheat; (*-i- in) swic, n. ‘delusion’; ON svíkja, sv. 1. as OHG; svik, npl. as OE; r. cf. seaghain, adj. ‘lovely’; seaghais, f. *pleasure' (ambig.)
17931:suei?- (suig-) — suelo
18060:suigh- (suigh-) ‘dash, swish, whizz’. Cf. suoigh- (sueigh-), etc. Onomat. ON svigi, m. ‘switch, lash’; svigna, v. ‘bend, give way’; svig, n. ‘bend, curve’; W chwi, pl. -on, m. ‘rapid turn’; Cz. (long-gde w. variant initial) švih, Lusat. šwih, m. ‘dash, impulse’; cf. Cz. svižný ‘dashing’
18062:(suig- (2); suig-, see suoiĝ-, suoig-)
18063:sui$- (3) “cheat, lure, seduce’. Cf. sueig-. (Arm. type suifno, ios) Arm. kenem, v. ‘flatter’; Kcni, -vo, -eav, adj. *wheedling'; Ir. cf. seaghain, adj. (charming, lovely”; seaghais, f. (/pleasure', fr. *suigosti-); MHG swiche, sf. (fraud; OE swic, n. *il- lusion, deceit’; swica, swice ‘cheat’; swician, v. id.; ON svik, npl. *fraud'
18126:suoigh- “bend, sway, rush, lunge, topple'. (Gk. ambig. Cf. uoigh-) Gk. (ambig.) oíkhomai, v. “rush, depart, va- nish’; ON sveigja, v. ‘bend’; sveigjast, refl. ‘sway’; Li. svaigstù, svaigti, v. ‘tipple; frolic, fall senseless, faint’; sviegiu, ti, v. (fling, fr. *sueigh- or *suoigh-); svaigùs “intoxica- ting. (Isophones: MHG sweig, sweige, f. ‘drove of cattle; ranch’; sweigen, wv. (tend (cattle); Li. dial. svíegiu, ti smear; punch")
18136:suoios (suoiios), à, om “own, personal; pro- perty, ownership. WP II, 455. Cf. suei-, suiio-, sue-, seu-, etc. Skt. svayám, prn. ‘self’; svayüh, adj. 'indepen- dent, personal; Av. xwae- cpds. 'self-; Oss. xi, Dig. xe, prn. adj. “self; own’; Myc. wojo, gs. prn. ‘own’; Gk. cf. heós, adj. id. (fr. *suejos, which is strictly genitive ‘deriving from’, whereas Myc. wojo for *suoio- is pos- sessive 'acquired by'. Similarly Lat. meus (gen.) as against Slavonic moj (possessive)); MHG cf. sweie, sweige, sweig, swei, f. “farm, herd'; OCS (and com. SL) svoj, adj. "own: OPr. svais, id.
```


## [2026-09-14T03:08:51.649Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '83260,83300p' POK_full.txt"
}
```


### [2026-09-14T03:08:51.705Z] TOOL RESULT

```
Germanie sJ-in Su-gambr/\/N, Old leelandie su-svgrtt 'Sehwarzamsel' ("die whole 
Sehwarze'); 

Lithuanian sudrus'horny, lustful, luseious'; Old Chureh Slavie Sbdravb ' u\/\r\q' , Czeeh 
zo'/'aKy (eompare above Old Indie su-dr'u-) ete.; Slavie *si>bozbje, Czeeh Zi&oz/'Besitztum' 
from *s-b-bog-b (= Old Indie subhaga-, above S. 107); 

su-\s zero grade to "s^e- (above S. 882 f.); eompare Old Indie sva- in sva-dha= su-dha 
" sweet drink, beverage, liquid whieh is swallowed to queneh one's thirst, draught, potion' 
(above S. 241), sva-dhita-= su-db/ta- 't\ght, firm, fit, healthy'; 

References: WH. II 512, E. Fraenkel Mel. Pedersen 443 ff., Vasmer 1, 450 f. 
Page(s): 1037-1038 

Root / lemma: suard- 

Meaning: to laugh 

Material: oapSavioc; 'hohniseh, spottiseh', aap5i^£iv 'hohnlaehen'; eymr. chwarddu, eorn. 

hwerthin. Middle Breton/7^e/'5//7 'laugh'. 

References: WP. II 517. 

Page(s): 1 040 

Root / lemma: suad- 

Meaning: sweet 

Material: 1. suadu-s'sweei': Old Indie svadii-, f. si/ao'i/f "sweet, mellifluous'; gr. n5u(;, f. -sTa 

(*-£Fia), -u, Dorie dbdc, "sweet'; with formants -mo-. aSupoc;, hom. r|5u|J0(; "pleasant'; Latin 

suavis {*suadu/s) "sweet'; Old Saxon swot/. Old High German suoz/. Old English swete. 

Old leelandie Sj^/a" sweet'; gall. PN SuadurTx, -genus, Irish Sadbt PN; about Gothie sut/'s' 

peaeeful, gentle', s. Mayrhofer KZ 71 , 74 f. under 73, 116 f.
```


## [2026-09-14T03:08:52.333Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84580,84620p' POK_full.txt"
}
```


### [2026-09-14T03:08:52.395Z] TOOL RESULT

```
osset. ;^'i//ds.; Latin 5i/ci//a 'young sow'; with expressive Gemination: Celtic *sukko- 
"swine, (pig-) snout, plowshare ' in Old Irish socc saiT guinea pig ' (a fish). Middle Irish soc 
m. ' plowshare, snout (of swine)'. Old Irish FIN Socc, cymr. hwchvn. f., later only f. "swine', 
corn, hoch, bret. houc'h, hoc'hxu. "swine'; from Gallo-Latin derive cymr. swch, corn, soch, 
bret. souc'han6 French soc^ plowshare '; 

Old English sugu^sow', Old Saxon suga, Middle Low German soge, Modern High 
German schwab. suge^sow'; with expressive Gemination Norwegian Swedish sugga. 
Middle Low German sugge. 

References: WP. II 512 f., WH. II 635 ff., Trautmann 294, Vasmer 2, 593, Benveniste BSL 
45, 74 f. 90, Thieme, Heimat d. Indo Germanic Gemeinsprache 26 f., 36 f.; probably 
originally " Gebarerin ', to seu-2. su- " to give birth to children ' (above S. 913 f.); compare 
Old Irish beriVsow' {*b^erentJ)\ or just imitative sound? 
Page(s): 1038-1039 

Root / lemma: sus- 

Meaning: to buzz 

Note: only Germanic and Slavic 

Comments: 

Root / lemma: sus- : to buzz, derived from Root / lemma: Rues-, Rus- : to puff, sigh. 

Material: Old High German suson " buzz, whirr ', Middle Low German susen, Swedish 

susa, Danish s^se ds.; 

Old Church Slavic sysati^ buzz, whirr, whistle'; Old Russian si/5o/ "Zieselmaus, 
Hausratte', Bulgarian sbse/ds.; stskam^ fizz '; compare Latvian susur/s' shrew, small 
mouselike mammal with a long snout ', susers " dormouse '. 

Maybe alb. shushurime: Spanish susurro: French sussurement: Portuguese sussurro: 
Venetian susio^ rustle '. Also Galician susurrar: alb. shushurin^ to rustle '. 

References: WP. II 514, Trautmann 294, Vasmer 3, 50 f. 
Page(s): 1 039 

Root / lemma: sus- {*ksus)
```


## [2026-09-14T03:08:55.909Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84540,84585p' POK_full.txt"
}
```


### [2026-09-14T03:08:56.057Z] TOOL RESULT

```
lupaKU) name eines Sumpfes. 

References: WP. II 513, Trautmann 293 f., Vasmer 3, 49, 58; perhaps to seu(9)-V'\\x\<ZQ, 
sap' (above S. 912 f.); about "milk' to: " coagulated, sour milk'. 
Page(s): 1 039 

Root / lemma: su-s, suu-6s 

Meaning: pig, swine 

Material: Avestan /7j(Gen. Sg. for *huvd) "swine'; gr. ho,, doc,, Akk. uv m. "boar', f. "sow' 

(therefrom uaiva f. "Hyane') besides auc;, oxioo, ds.; in addition ounAai tottoi poppopu)5£i(; 

Hes.; au(p£(i)6(;, au(p6(; m. " pigpen' (*-(p£FiO(;, to cpuw, Indo Germanic b'^eu-, above S. 146 

ff.); constellation the 'OXabzc, "group of pigs'; compare gr. lak. oiKa; 

alb. (*snv) //7/"swine'; Latin sus, s^/s "swine', Umbrian s/rsues', s//77"suem', surum, 
sorsom, sorsalem's\Muxx\' {*su-do-, *su-dali-); 

gall. *su-teg/'s' pigpen' (M.-L. 8492); 

Old High German Old English su. Old Icelandic syr'sow'; 

Latvian suvens, s/Ve'/7s "piglet' (unclear Old Prussian seweynis' pigpen'); Tocharian B 
suwo swine'; 

adjektivische no- derivatives: on the one hand gr. (late) unvoq "from swine', on the other 
hand (ursprachlich) Latin suTnusds., Old Church Slavic svinhds. = Latvian sv/hs 
"smudges'; Tocharian B swanana m/'sa ' pork'; 

substantivized Gothic swein. Old Icelandic sum. Old English Old High German swTn 
"swine'; Old Church Slavic sv/n/ja ' s\N'\ne' probably from *si//77/"(fem. to sv/nb) reshaped. 



k- derivatives: 

Old Indie sukara- m. "boar, swine' (reinterpreted as '5i/-maker'); Middle Persian xuk, 
osset. ;^'i//ds.; Latin 5i/ci//a 'young sow'; with expressive Gemination: Celtic *sukko- 
"swine, (pig-) snout, plowshare ' in Old Irish socc saiT guinea pig ' (a fish). Middle Irish soc 
m. ' plowshare, snout (of swine)'. Old Irish FIN Socc, cymr. hwchvn. f., later only f. "swine', 
corn, hoch, bret. houc'h, hoc'hxu. "swine'; from Gallo-Latin derive cymr. swch, corn, soch, 
bret. souc'han6 French soc^ plowshare ';
```


## [2026-09-14T03:09:07.497Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD su- ===\"\ngrep -n -i \"sukko\\|hyena\\|sucula\\|swine\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T03:09:07.557Z] TOOL RESULT

```
=== AHD su- ===
166:Stockbreeding and animal husbandry were an important part of Indo-European eco- nomic life. The names for all the familiar domesticated animals are present throughout the family: gvou-, “cow and bull,” owi-, “sheep,” ag“h-no-, ‘lamb,’ aig- and ghaido-, “goat,” sd-, “swine,” and porko-, “farrow.” The domestic dog was ancient (kwon-); its name may underlie the common Indo-European word for horse, ekwo-. The expansion and migration of the Indo- European-speaking peoples in the later third and early second millennia B.c. is intimately bound up with the diffusion of the horse. The verbal root deme-?, “to force,” acquired the special sense of “‘to tame horses,” whence English TAME. Stock was a source and meas- ure of wealth; the original sense of peku- was probably “wealth, riches,” as in Latin pecu- nia, whence “wealth in cattle” and finally “cattle” proper. The same evolution from the general to the particular may be observed in the root neud-, “to make use of,” whence English NEAT?.
1034:sii-. Pig. Contracted from *sua-; probably a derivative of seue-'. 1. Suffixed form *sua-ino- in Germanic *swinam in Old English swin, swine: SWINE. 2. Celtic expressive form *sukko-, swine, snout of a swine, plowshare, in: a. British *hukk- in Old English hogg, hog: HoG; b. per- haps Old French soc, plowshare: SOCKET. 3. Germanic *sii- in Old English sugu, sow: sow?. 4. Latin sis, pig: soit’. 5. Greek hus, swine: HYENA; HYOSCINE. [Pok. su-s 1038.]
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
2329:SWIM swem- SWINE si-
```


## [2026-09-14T03:09:08.918Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN syphilis ===\"\ngrep -n -i \"syphilis\\|Syphilus\" KLN_1966.txt KLN_1971.txt | head -20\necho \"=== KLN hyena ===\"\ngrep -n -i \"hyaena\\|hyena\" KLN_1966.txt KLN_1971.txt | head -20"
}
```


### [2026-09-14T03:09:09.043Z] TOOL RESULT

```
=== KLN syphilis ===
KLN_1966.txt:16871:gumma,  n.,  a  soft  tumor,  characteristic  of  tertiary syphilis.  —  Medical  L„  fr.  L.  gummi.  See  gum,
KLN_1966.txt:22268:syphilis.  —  L.  lues,  ‘a  plague,  pestilence',  prop, ‘dissolution’,  fr.  luere,  ‘to  loose,  release’,  which is  cogn.  with  Gk.  Xttetv,  ‘to  unfasten,  loosen,  un¬ tie,  slacken;  to  loose,  release,  set  free,  ransom’. See  lose  and  cp.  -lysis.
KLN_1966.txt:28525:philo-,  before  a  vowel  phil-,  combining  form meaning  ‘loving,  fond  of,  interested  in’,  as  in philosopher.  —  Gk.  91X0-,  91X-,  fr.  91X05, ‘loved,  beloved,  dear’,  as  a  noun,  ‘friend’;  later, in  poetry,  also  used  in  an  active  sense,  ‘loving, friendly',  whence  9iXeiv,  ‘to  love’ ;  of  uncertain origin.  Cp.  philander,  Philemon,  philter,  syphilis.
KLN_1966.txt:33356:L.  rapes,  ‘rock’,  which  is  rel.  to  rumpere,  ‘to break,  burst,  tear,  rend’.  See  rupture  and  -ian. For  the  relationship  between  L.  rupes  and  r am¬ pere  cp.  L.  saxum,  ‘rock,  stone',  which  is  rel.  to secare,  ‘to  cut’,  OE.  clif,  ‘cliff’,  which  is  rel.  to OE.  cleofan,  ‘to  split,  cleave’,  ON.  sker,  ‘an  iso¬ lated  rock  in  the  sea’,  which  is  rel.  to  ON.  skera, ‘to  cut,  shear’,  and  Gk.  Xetta?  ‘a  bare  rock, crag’,  which  is  prob.  rel.  to  Xe-eiv,  ‘to  strip  off, peel’  (see  saxatile,  cliff,  skerry  and  lapidary,  adj.) rupia,  n.,  a  skin  disease  occuring  esp.  in  tertiary syphilis  ( med .)  —  Medical  L.,  fr.  Gk.  portoc, ‘dirt,  filth’.  See  rhyparography  and  1st  -ia. Derivative:  rupi-al,  adj.
KLN_1966.txt:33591:Derivatives  :  salvage,  tr.  v.,  salvag-er,  n. salvarsan,  n.,  a  compound  of  arsenic  used  as  a remedy  against  syphilis.  —  Coined  by  its  inven¬ tor  Paul  Ehrlich  (1854-1915)  in  1910  fr.  L.  sal- vdre,  ‘to  save"  (lr.  salvus,  ‘safe’),  and  G.  Arsen, ‘arsenic’.  See  safe  and  arsenic, salvatella,  n.,  a  vein  of  the  back  of  the  hand (anat.)  —  ModL.,  formed  fr.  L.  salvSre,  ‘to save’,  fr.  salvus,  ‘safe’,  see  safe  and  -ella.  The noun  salvatella  was  formed  in  imitation  of  usdy-
KLN_1966.txt:35634:smallage,  n.,  wild  celery.  —  ME.  smalege,  fr. earlier  smalache,  which  is  compounded  of  smal, ‘small’,  and  F.  ache,  ‘parsley’,  fr.  L.  apium.  See small  and  ache,  ‘parsley’, smallpox,  n.  —  Fr.  earlier  small  pokkes ,  ‘small pox’;  so  called  in  contradistinction  to  the  ‘great pox',  i.e.  syphilis.  See  small  and  pox.  For  sense development  cp.  F.  petite  vdrole,  ‘smallpox’, smalt,  n.  —  MF.  (=  F.),  fr.  smalto,  which  is  of Teut.  origin.  Cp.  OHG.,  MHG.  smalz,  G. Schmalz,  ‘melted  fat’,  OHG.  smelzan,  MHG. smelzen,  G.  schmelzen),  ‘to  melt’,  and  see  smelt. Cp.  also  enamel.
KLN_1966.txt:36033:sovran,  n.,  sovereign.  —  Milton’s  spelling  of sovereign  (as  if  it  derived  from  It.  sovrano). sow,  n.,  female  pig.  — -  ME.  siiwe,  sowe,  fr.  OE. sugu,  sii,  rel.  to  OS.,  OHG.,  MHG.  sit,  G.  Sau, Du.  zeug,  ON.  syr,  Dan.,  Swed.  so,  and  cogn. with  OI.  sitkarah,  ‘wild  boar,  swine’,  Avestic  hit, ‘wild  boar’,  Toch.  B  suwo,  ‘swine’,  Gk.  5g,  crug, ‘swine’,  u'.vog,  ‘swinish’.  Alb.  di,  L.  sits,  ‘swine’, L.  suinus,  ‘pertaining  to  swine’,  OSlav.  svinija, ‘swine’,  Lett,  suvens,  sivens,  ‘young  pig’,  W. hitcc,  Ir.  suig,  ‘swine’,  Olr.  socc,  ‘snout;  plow¬ share'.  All  these  words  derive  from  the  I.-E. imitative  base  *su-,  *suw-,  which  is  proved  by the  OI.  equivalent  su-karah,  lit.  ‘maker  (=  ut- terer)  of  the  sound  sii'.  Cp.  hog,  hyena,  socket, soil,  ‘to  make  dirty’,  suillinc,  sully,  Sus,  swine, and  the  first  element  in  sybotic,  syphilis,  Hyos- cyamus,  Hystrix.
KLN_1966.txt:37911:syphil-,  form  of  syphilo-  before  a  vowel, syphilis,  n.,  an  infectious  venereal  disease.  — ModL.,  from  the  title  of  the  work  by  Girolamo Fracastoro,  Syphilis  sive  de  morbo  Gallico  (  = Syphilis,  or  the  French  disease’),  published  at Verona  in  1530;  so  named  after  the  hero  Syphi- lus,  a  shepherd  whose  name  lit.  means  ‘friend  of swine’,  fr.  Gk.  oup  (gen.  auop)  =  up  (gen.  uop), ‘swine’,  and  tptAop.  ‘friend’.  For  the  first  ele¬ ment  see  sow,  n.,  for  the  second  see  philo-. Derivatives:  syphil-itic,  adj.,  syphil-ize,  tr.  v., syphil-oid,  adj.,  syphilous  (q.v.) syphilo-,  before  a  vowel  syphil-,  combining  form for  syphilis.  —  See  syphilis, syphilology,  n.,  the  study  of  syphilis.  —  Com¬ pounded  of  syphilo  and  Gk.  -Aoyta,  fr.  -Aoyop, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy.
KLN_1966.txt:37913:syphilous,  adj.,  syphilitic.  —  A  hybrid  coined  fr. syphilis  and  -ous,  a  suff.  of  Latin  origin.
KLN_1971.txt:107372:syphilis. — Medical L., fr. L. gummi. See gum, 
KLN_1971.txt:141039:syphilis. — L. lues, ‘a plague, pestilence’, prop, 
KLN_1971.txt:180645:origin. Cp. philander, Philemon, philter, syphilis. 
KLN_1971.txt:210103:syphilis {med.) — Medical L., fr. Gk. putroi;, 
KLN_1971.txt:211694:remedy against syphilis. — Coined by its inven- 
KLN_1971.txt:224552:pox’, i.e. syphilis. See small and pox. For sense 
KLN_1971.txt:227239:and the first element in sybotic, syphilis, Hyos- 
KLN_1971.txt:239644:syphilis, n., an infectious venereal disease. — 
KLN_1971.txt:239646:Fracastoro, Syphilis sive de morho Gallico {— 
KLN_1971.txt:239647:Syphilis, or the French disease’), published at 
KLN_1971.txt:239656:for syphilis. — See syphilis, 
=== KLN hyena ===
KLN_1971.txt:3950:aardwolf, n., a South African hyena-like mam- 
KLN_1971.txt:117187:Hyaena, n., the typical genus of the hyena family. 
KLN_1971.txt:117189:— L. hyaena. See hyena. 
KLN_1971.txt:117724:hyena, hyaena, n. — L. hyaena , fr. Gk. uouva, 
KLN_1971.txt:117725:‘hyena’, lit. ‘sow’ formed with the fern. suff. 
KLN_1971.txt:117730:pig’. The hyena was so called in allusion to its 
KLN_1971.txt:227237:terer) of the sound su'. Cp. hog, hyena, socket, 
KLN_1971.txt:263298:‘wolf’, Ethiop. ze'eb, ‘hyena’. F. avives, ‘vives*, 
KLN_1966.txt:1117:aardvark,  n.,  a  South  African  burrowing  animal. —  Du.,  lit.  ‘earth  pig’,  fr.  aard,  ‘earth’,  and vark,  ‘pig’.  See  earth  and  farrow, aardwolf,  n.,  a  South  African  hyena-like  mam¬ mal.  —  Du.,  lit.  ‘earth  wolf’.  See  prec.  word and  wolf.
KLN_1966.txt:18297:Hyaena,  n.,  the  typical  genus  of  the  hyena  family.
KLN_1966.txt:18298:—  L.  hyaena.  See  hyena.
KLN_1966.txt:18403:Hydras,  n.,  1)  a  fabulous  water  serpent;  2)  a southern  constellation;  the  Water  Snake  (as- iron.)  —  L.,  ‘water  serpent;  the  constellation  of the  Water  Serpent’,  fr.  Gk.  GSpos,  ‘water  ser¬ pent’,  which  is  rel.  to  u8pa,  of  s.m.  See  Hydra, hyena,  hyaena,  n.  —  L.  hyaena,  fr.  Gk.  uaiva, ‘hyena’,  lit.  ‘sow’  formed  with  the  fern.  sufT. -aivz,  fr.  &<;,  gen.  (165,  ‘swine’ ;  see  sow,  ‘female pig’.  The  hyena  was  so  called  in  allusion  to  its bristly  mane.  For  sense  development  cp.  Hun¬ garian  series,  ‘hog,  swine’,  lit.  ‘the  bristly  ani¬
KLN_1966.txt:36033:sovran,  n.,  sovereign.  —  Milton’s  spelling  of sovereign  (as  if  it  derived  from  It.  sovrano). sow,  n.,  female  pig.  — -  ME.  siiwe,  sowe,  fr.  OE. sugu,  sii,  rel.  to  OS.,  OHG.,  MHG.  sit,  G.  Sau, Du.  zeug,  ON.  syr,  Dan.,  Swed.  so,  and  cogn. with  OI.  sitkarah,  ‘wild  boar,  swine’,  Avestic  hit, ‘wild  boar’,  Toch.  B  suwo,  ‘swine’,  Gk.  5g,  crug, ‘swine’,  u'.vog,  ‘swinish’.  Alb.  di,  L.  sits,  ‘swine’, L.  suinus,  ‘pertaining  to  swine’,  OSlav.  svinija, ‘swine’,  Lett,  suvens,  sivens,  ‘young  pig’,  W. hitcc,  Ir.  suig,  ‘swine’,  Olr.  socc,  ‘snout;  plow¬ share'.  All  these  words  derive  from  the  I.-E. imitative  base  *su-,  *suw-,  which  is  proved  by the  OI.  equivalent  su-karah,  lit.  ‘maker  (=  ut- terer)  of  the  sound  sii'.  Cp.  hog,  hyena,  socket, soil,  ‘to  make  dirty’,  suillinc,  sully,  Sus,  swine, and  the  first  element  in  sybotic,  syphilis,  Hyos- cyamus,  Hystrix.
```


## [2026-09-14T03:09:32.924Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT hu- / kehrpa ===\"\ngrep -n \"hū-kǝhrpa\\|hukǝhrpa\\|hu-kehrpa\\|hū- .*Schwein\\|Schwein\" BRT.txt | head -30"
}
```


### [2026-09-14T03:09:32.981Z] TOOL RESULT

```
=== BRT hu- / kehrpa ===
11210:•)  Sva.  paiuia-,  sÄ  und  vgl.  ratascarat:  — Als  Repräsentanten  dieser  Tiecklasse  werden Bd.  14.  6  fiock,  Schaf,  Kamel,  Schwein,  Pferd und  Esel  genannt;  s.  dazu  Yt.  14.  7,  9,  II,  15, 13,  aS-  Als  ihr  Ratav  gilt  nach  Pü.  zu  Vr.  /.  1 und  Bd.  34,  a  der  'weisse  Eselbock'  {xar  iüi  i
22822:'varäza-  m.  'Männchen  des  Schweins, Verbindung  mit  dem  Namen  für
22824:Schwein"':  As(sd.)  k»hrpa  'zähe , .  arÜnS*''
30138:•  j.  hQ-  'Schwein,  Sau':  ahmai  . .  ajasai vinhrafnS  hü  (GS.)'^  kthrpa  varätahe (sd.)  .  .  arins  ".  .  in  der  Gestalt  eines Ebers  .  ."  Yt./rf.  15.
30174:VJ(AP.),  •ralibyU,  'ranqm  -.  Unklar: nSii  ^mairyeke  nSi^  Jahtkayh  tait  sünü  tOii 'rahe''>  V.io. Ableit  —  d.  lui/aträ-  Adj.  —  VgL  den  ^, EN. 'OJ«Vlt  1*- —  Pü. :  »"fl/üi ;  s,  noch  No.  3.— 0  iSt  s.  Bthl.  KZ.  aS.  11;  weitere  Litt,  bei JusTi  PrJ.  S8.  247,  woEu  noch  Gdn.  BB.  13. 9tS.  —  1)  Scheint  ein  andres  Wort  verdrängt lu  haben;  Pü.:  AüA  'Schwein'.  Dst.  ZA.  j. SS  vriU  freilich  "le  roi  des  porcs".  —  3)  S. übrigens  zu  uxsya{jr>la-.
```


## [2026-09-14T03:09:34.340Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN xuk ===\"\ngrep -n -i \"xūk\\|hūk\\|chūk\\|ḫūk\" HRN.txt | head -20\necho \"=== HRN pages ~113 ===\"\ngrep -n \"Schwein\" HRN.txt | head -20"
}
```


### [2026-09-14T03:09:34.416Z] TOOL RESULT

```
=== HRN xuk ===
=== HRN pages ~113 ===
4609:510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
4612:skr. siikard- 'Eber, Schwein*.
```


## [2026-09-14T03:09:44.483Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4595,4625p' HRN.txt\necho \"=== find page marker near ===\"\ngrep -n \"^\\[pdf page\" HRN.txt | head -3"
}
```


### [2026-09-14T03:09:44.560Z] TOOL RESULT

```
^) So auch immer in der Poesie.
*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
7d. 14 (72). - Zu aw. Inträ- vergl. Bartholomae, ZDMG. 37, 459.— 113 —
508. x^^> /ß^i ^^'^^ {^' i- X<^s, jüd.-pers.), (Sahn, /^^es^ daneben
äähn.O, AM.: ;kös) gut, schön, fröhlich* etc.").
Käs. x^Sj /öS.
phlv. /^as hezw, yüs (paz. ;^^as); kurd. /ös, v^; af/.
yöi; bei. vas (407); öij'n. ;Kdi^', sar. yS^.
Nöldeke (mündliche Mitteilung) nimmt als Grund-
form *huakSi- an. Dieselbe Anknüpfung des Wortes
bei Fr. Müller, WZKM. 5, 352.
509. yiiisnüdj x^snü zufrieden, fröhlich*.
aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
/iisnüt, /usnütik (AV.).
510. x^"'*^) 'Schwein, :i)5 (Qiss. Dan. S. 388).
aw. hü kehrpa in Ebergestalt'; phlv. /ük (Bund.),
yßköak hezw, /übadak (Payprus, Ilorn ZDMG. 43, 51);
skr. siikard- 'Eber, Schwein*.
kurd. /ü (H.-Sch.); B>fy.xilg; oss. d. t. yiä (310);
bei. hlk, n. hJy (157) ; wa;r. /äg, sar. y^ug,
511. //rn 'Blut', yümn.
aw. vohuni' *Blut'; phlv. yün, yUnömaud,
kurd. ;^("n (ll.-Sch.); af}'. vTne (f. pl.); bei. LW. hün,
hon (162); wa/. vu/c^n, Uyn. vlyTn, sar. va/ln, sangl.
vain,
512. xöl Helm', yöd.
ap. yauda- *Helm*; aw. ayö],yaoda'.
arab. LW. yu^at 'Helm'; Sify.yöl; oss. d. yodäy t. yüd
(302) ; sar. ydtid *Hut, hohe Mütze aus Schaffell'.
513. yi^'ei 'Schweiss .
aw. yya^öa- 'Schweiss' (ZPGl.), vergl. aw. y'^'Tsctt,
=== find page marker near ===
```


## [2026-09-14T03:09:46.033Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB xuk ===\"\ngrep -n -i \"chūk\\|xūk\\|Schwein\" HUB.txt | head -20\necho \"=== PHD xuk ===\"\ngrep -n -i \"xūk\\|xwk\\|pig\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T03:09:46.132Z] TOOL RESULT

```
=== HUB xuk ===
7638:xUk Schwein' = phi. xUk 61. and Ind. 53 = zd. hu-; xujlr
8512:*Stachelschwein — zd. sukurena- (Neuausgabe, var. suku-
8589:(nom.); dig gestern' (neben di), bal. zlk; xug 'Schwein
=== PHD xuk ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:422:kabk [АрА! | N ~] partridge. ~-anjir [acyl | N ~] a kind of francolin. kabód [kpwt! | N ~] grey-blue; pigeon. kabótar [kpwil | M kbwtr, N ~] pigeon. kāč [с | N kāš(ki)], ~ ka: would that, if only. кадар [01А] game, joke. кадар [ktk' | M kdg, N kada] house. ~-banig [-b'mwk! | N Radbanü] mistress, lady of the house. ~ig [-yk'] domestic; servant. ~-xwaday [-hwty | P gdyxwd?y, N kadxudā] householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар] shoe. ~gar [-k/ | N ~] shoemaker. kaftan, kaf- [kp-in' | P kft, kf-] fall. kah [TBNA < A tbr | N ~] chaff, straw. kān-, ~i§n, v, kāstan. _ kahas [kts | М khs] channel, sewer. kāhēnīdan, káhén- [R'hyn-ytn!] decrease, lessen (tr.). kühidan [P hytn! | N ~] = kastan. kahist [ksst'] least. kah-rubāy [Ара | N —rubá] amber. kahwan [khwbn' | M qhwn, N kukan] old. kākom [RP Rkwm | N ~] stoat. ~ i spéd: ermine. kālbod [Аро | (M k*/byd), N ~] body, shape, form. ~ӧтапа [-wmnd] corporeal. kam [km | M kmb, N ~] little, small, few; v. kem. kam [Em | = M, N ~j will, desire, purpose. kàm-, v. kāmistan. 1катаб [k?mk! | N kama] kinds of gruel, or soup. ?kümag [k?*mk! | N kama] = kam. «-hanjām [-hnc’m] gaining one’s end, successful. -~-hanjamih: success. „ūmand [-wmnd] willing(ly), desirous. ~-widar [-wt?l | N kām-gučār] successful, independent. ~-xwaday [-Awt^y] independent, absolute. kamal [kml | (M km?7)] head (daevic). ~ig [-yR!] chief (daevic).
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:559:rēšaģ [/yšk! | N rēša] root, fibre. rēšīdan, rēš- [lysyin' | N ~] wound, hurt. rëškën [/yškn'] hurtful, harmful. ~th: harmfulness. réxtan, réz- [lyhtn', lyc- | P ryxt, M ryz-, N ~] flow, pour. --išn: flow. ridan, riy- [/ytn', Id- | N ~] defecate, void. rist [lyst' | M ryst] dead. Iristag [lystk'] corpse. 'ristag [/ystk!] way, manner; sect. rist-āxēz [/yst?hyc | M ryst?hyz, N ~] resurrection of the dead, rištaģ [/(y)stk! | N ~a] rope, string, thread. riy-, v. ridan. riyahrih [/d?hlyh] scorn, mockery. rdb [/wp] robbery. rób- [/wp- | N ruftan, ~} rub, sweep. rūbāh [TALE < A tP; lwph | N ~] fox. Irēd [Iowt! | M rwd, N ~] river. *rdd [lwt' | N ~] stringed instrument. réd-bar [lwtb’] | N ~] river bank. rddig [/zvtyk! | (N róda)] intestine, gut; ~4n, (p/.) entrails, guts. тбүп [M(H)SY A < A ті; lwkn! | Р тшеп, (M rwyyn), N rauyan] oil, butter. ~-xwardig [-hwltyk'] sweetmeats. ron [lwn' | M rwn] direction. б... ~: towards. róspig [lwspyk! | N ~i] whore. ~th: whoredom. róstág [lw(t)st?k! | (P rwdyst?g), N rūstā] river-bed; district, province. rošn [lwfn! | M rwšn, N rūšan] light; bright, light. ~ih: light. röšnjag [lwsnk'] clear, obvious. ~gar [-Al | (P gr, M -ygr), N -gar] illuminator. irēy [ltd | M rwy, N ~] face. *rdy [lwd | M rwy, N ~] copper, brass. гбу-, -išn, v. rustan. гӧуап [/wdyn! | N ~] madder. róyen [/wdyn! | M r'wyn, N róyin] (made of) copper, brazen. roz [YWM < А ушт; Гос | M rwc[z, N ~) day. rózag [lwck! | M rweg, N roza] fast, fasting. rozāģ [wc k'] lightning. rózan [/wcn! | N ~] window. roz(b)ānaģ [lwe(p)’nk'] window. rózénidan, rózén- [Iwcyn-ytn! | M rweyn-] lighten, brighten. rozģār [/wck”l | N ~] daytime. r6zig [/wcyk! | N rózi] daily bread, sustenance.
PHD.txt:568:spas dāštan, ~ hangárdan: thank, give thanks. spās-dār [sp?sd?] | N sip~] grateful, thankful. ~ih: gratitude. spās|-ešnās [sp’ssn’s] grateful. —ómand [-’wmnd] grateful. spas [sp = Av. 0Bàsa-] space, atmosphere. spaxr [sp?hl | M ‘spxr, N *siparx] merrymaking, revelry. spazg [spzg | (M ‘spgj), N sipazg-] slanderous. «il: slander. spëd [spyt! | M ‘spyd, N sapéd] white. ~ag [-k! | N -a] white (of egg, etc.). —bàg [-p’k!' | N -bā] curd soup. --dàr [-?1 | N -dár] white poplar, aspen. spenag [sp(y)m?k! = Av. spanta-, cf. $annág] holy. ~ ménóg : the Good Spirit. Spig [spyk' | M ‘spyg, (N sapriy)] т. brilliance; 2. sprout, shoot. spihr [spy(y)hl | (M ‘spyr), N sipihr] sphere, sky, firmament, fate. ~ig [-yk'] heavenly. spinjanagih [spne’nkyh] hospitality. spiš [spyš | (N šipt$)) louse. Spitāmān [spyt?m?^n] of the Spitama family. spiz- [spyc- | M “рухіп, *spyz-] 1. shine; 2. sprout. —išn: 1. brilliance; 2. sprouting. spöxtan, spēz- [spwhtn', spwc- | M *spwxt, N sip~] thrust; overstep, disobey; delay, reject. ~išn: delay, rejection; disobedience. SpOz [spwe | N sipóz] disobedience; delay. ~gar LEIT N ~] disobedient; dilatory. sprahm(ag) [splhm(k') | M *sprhm(g), N siparham] flower, fragrant herb. spul [spwl] spleen. spurdan, spar- [spwiltn', spl- | N sip~] tread, trample. spurrig [spwlyk!' | (M ‘spwr), N sipari] entire, complete, perfect. ~ith: completeness, perfection. spurz [*spiz | P “spwrz, N sipurz] spleen. srat (sit! | cf. Ar. sirát] street. sraw [s/wb'] word, spell. srawénidan, srawén- [slwbyn-ytn'] report, broadcast. sraxtag [s/htk! = Av. sraxti-] side, part. sray [sd | N saray] house, hall. Igrāy-, -išn, v. srüdan. srāyīdan, ?sráy- [sPd-ytn! = Av. @rdya-] protect. ~išn: protection. srešk [sl(y)£h | (P srsk), N sirifk] drop, tear. srištan, *srēš- [s/szn! | P sryi-, N sir-~] mix, knead. sri$wadag [s/ystotk! = Av. Oriswa-] a third. sréd [s/zvt! | M srwd, N suród] song.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:1094:brightness, brilliance Һат, brāzišn, frog, payrég, spig.
PHD.txt:2249:hedgehog xārpušt, xūkar(ag), züzag.
PHD.txt:3124:pig xüg.
PHD.txt:3125:pigeon kabēd, kabótar.
PHD.txt:3636:shoot (n.) spig.
PHD.txt:4781:spihrīg uo ev spenāg wvav spig 135035 spiz- —-Q5 Q335 spīzišn 1^0 2301 spiš ^U" Q335 spitāmān 16” 10 035 spēd-dār `o тез as»
PHD.txt:4929:rospigih rospig
PHD_mackenzie.txt:558:add    hiig [HZWLYA < A ~zyr'; hwk' 1M hwg, N xugj pig.
PHD_mackenzie.txt:2129: ........farrag [-pig I P dw.ffr] unfortunate.
PHD_mackenzie.txt:3120: kabOd [kpwt I N --] grey-blue; pigeon.
PHD_mackenzie.txt:3122:kabotar [kpwtll M kbwtr, N --] pigeon.
PHD_mackenzie.txt:4349:raspig Wspyk'] second officiating priest.
PHD_mackenzie.txt:4612:spig [spyk' I M <spyg, (N sapriy)] I. brilliance; 2. sprout, shoot.
```


## [2026-09-14T03:09:55.381Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"— 10[234] —\" HRN.txt | head\necho \"---\"\ngrep -n -i \"xāstan\\|/āstan\\|haiz\\|hiz\\|xēz\\|/ēz\" HRN.txt | sed -n '1,40p'"
}
```


### [2026-09-14T03:09:55.461Z] TOOL RESULT

```
4234:verfällt.— 103 —
---
300:scheinlich statt hizniurden zu erinnern , ohne der vielen
1997:188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
5440:^) Aw. hizvö raiHm (y. 50, 6) beisst iiacb Bartholomae,
5760:ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
5773:hiznrani.— 145 —
13253:pdhize 277.
16146:hizam 1117,
```


## [2026-09-14T03:09:58.175Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4160,4250p' HRN.txt"
}
```


### [2026-09-14T03:09:58.225Z] TOOL RESULT

```
') Cu ist metrisQh nur kurz, die Länge dazu ist cün (Rüokert,
ZDMO. 10, 133). Cünän z. B. äähn. I, 148 Vera 354, cümn 157 Vers 523.— 101 —
in weit ausgedehnterem Grade verwendet. Vergl. -J
(Nu. 53) unter 'Verlorenes Sprachgut*.
452. 6ehüv 'vier , ceharmn, cär^ darum (AM. neben öehärum),
cärlpäi, car[sa (syr. LW. ''1D1NTO*', arab. LW. cahdrsOg),
cdr[deh (Sahn. I, 211 Vers 1479) etc.
aw. öa^warö Vier*; phlv. cahär, päz. cihär; ai.
catcdms; arm. rorU (H. No. 241).
kurd. (Sihna) cacar; af/. calör; oss. d. aippar, t.
cippar (321); wa;^. cahur, cahiir , sar. cavur, cavor,
%n. cavor, cavdr, yayn. t/ö, sangl. sa/ör, niinj. ca//r.
453. rlhr, cihre 'Ursprung; Angesicht'.
ap. Chira- 'Geschlecht, Ursprung; aw. riiira- Ur-
sprung: Gesicht'; phlv. citre (Münzen, Inschriften),
cihr, cihrak, cihrakömand 'die Merkmale der Periode
habend*; ai. citra- 'hell etc.'
kurd. cdre\ afy. cTra, stra,
454. rihil, 6ü 'vierzig*.
aw. ca&waresata Vierzig*; piiz. cihal^ cihU^ cd; ai.
catvdrirlQdU,
kurd. öel, cehl; afy. cctlve^t.
455. ctden sammeln; schneiden', Praes. öm-em, ein, eine,
aw. i/^cay-, mit Praep. /ra *sammeln*; phlv. citaH,
einet (Men.) 'sammeln', cimtan (vd. 5 (159) Gl.); ai.
|/cay- cinoti sammeln, einsammeln'.
kurd. einin 'erndten*; bei. cwaff, n. J'may 'sammeln,
auflesen, aufheben* (60) ; sar. ciy^am, ctdam 'schneiden,
emdten*.
456. eer wacker, mutig*'), eure, eeregl.
ai. cSrU" 'begehend (ein heiliges Werk), Nöldeke
(mündliche Mitteilung); phlv. cer (für aw. Hyra-), certh.
Das Päzend hat den ursprünglichen Majhülvokal
noch bewahrt, der auch im indischen Persisch ver-
schwunden ist.
457. CT» etwas*.
1) Reimt auf Igr, Vis und Rämln, S. 40 Vera 10, rtahn. I, 132
Vers 62.- 102 —
päz. cih (phlv. HD) + cij/ bezw. c7/, in einem Worte
päz. eis (?) (phlv. cnj?^).
Daneben np. cl 'etwas' (Gul. Sprenger 29 Zeile 17).
X.
458. x'^" (Praefix) gut-'.
Vergl. 'Verlorenes Sprachgut* No. 118.
459. (i)x€^ 'Rinnsal'.
aw. /an-, Nom. /äo 'Quelle*, vergl. np. xäm (No. 466)
und die folgende Nummer.
460. {2)%ä 'Schulter .
aw. /äo, yt. 10, 71 ; 14, 29 'Schultern'.
Geld n er, Studien I, 173. Doch sind beide Worte
im Neupersischen durchaus unbelegt, und die Über-
setzung von aw. /äo durch 'Schultern (man erwartet
einen Dual) nicht sicher^).
461. y^ar, x^^^ 'Fels; Dorn 2), x^*'^ (Häliz 16, 3), ;fä£?e?r
(aus *;^6Zr^^r ?) 3), x^^P^^^ Igel-
skr. khara- 'hart, rauh; scharf; phlv. /ßr, /drpust
Igel* (Bund.); arm. fear 'Stein*.
462. '^Kitsten 'aufstehen*, Praes.;^e2-e/w (AM. 84 Zeile 2 v. u.),
yeztden [x^ztden).
aw. pairi]./aezayiuha^) erhebe dich'; phlv./ös^ (vd. 16
*) Bartholomae (briefl. MitteiluDg) nimmt nach dem Glieder-
parallelismus (s. Neuausgabe)
erezöis x^o
bäzväo aojö
tnnvö vazdvare
für yäo eine mit aojö und vazdvare ungefähr synonyme Bedeutung an.
*) In der Bedeutung Tenis* in alb. Tcär^ kars (G. Meyer,
Alban. Wörterbuch, 176); auch arm. xw (S. Bu gge, KZ. 32, 9).
») Vergl. Rückert, ZDMG. 10, 166, 167 und dann Vullers zu
V ^^
Sahn. I, 196 Vers 1211 (der Rückert, wie gewöhnlich, nicht nennt).
*) D armestet er, 6t. ir. I, 201 weicht hier von Vullers,
Institutiones, ab und macht die Sache nur schlimmer, indem er mi^
dem Pehlevl-Commcntator auf aw. ^'^Isat *er fing an zu schwitzen* (!)
verfällt.— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
AV.), päz. d/ezed (Men.).
oss. ra]xlzai *du willst herabsteigen', d. s^ezun 'hinauf-
steigen' (301).
Das awestische Wort ist nicht sicher; die Päzend-
lesung mit z beweist nichts.
463. xäm *roh, ungekocht'.
ai. amd' *roh*; arm. huni 'roh' (H. No. 171; vergl.
Bartholomae, Studien II, 44. Daneben LW. /aw)5
gr. (Ojiwc; air. 6w.
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
```


## [2026-09-14T03:10:11.961Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG xaiz ===\"\ngrep -n -i \"xaiz\\|xēz\\|xez-\\|haiz\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T03:10:12.021Z] TOOL RESULT

```
=== CHEUNG xaiz ===
9123:*haiz ‘to look, search for pastures ?’ 
10993:*Haiz 159 
11048:*Haiz ‘to long for, desire’ 
11056:160 *Haizd (?) 
11068:*HaiZd (7?) ‘to implore’ 
28483:*xaiz ‘to rise, ascend; increase’ 
28488:*xaiz 441 
28533:*NEIR: Oss. I. xizyn/xyzt, D. xezun/xizt ‘to climb’, Pash. xeZ-/xatol ‘to rise’, Sangl. 
28537:*han-xaiza- ?) 
28546:who argued for the existence of three different roots: *haiz- ‘to rise’, *h/xaiz- ‘to 
28547:creep’, *xaiz- to wait for, look for; to protect, pasture’. For ‘to creep’ I would rather 
28733:‘crawling on earth’, but also as ‘setting on earth’ (*xaiz), also MSogd. txyz ‘setting 
28744:may have been influenced by the (near-)synonym *xaiz ‘to rise’. 
34857:"hyc- /axez-/, 440 
41643:xastan/xez-, 441 
47775:xeZ-/xatol, 441 
55217:*xaiz 
55313:*iam (s.v.), *spas, *xaiz (s.v.) 
56307:*оаНи, *gard, *Hais, *Haiz, 
56783:*zgad (s.v.), *xaiz (s.v.) 
56919:*ғаиН?, *uaxs, *xaiz 
57079:*Haiz, *xsij 
57081:*daiH! , *haiz, *kas! , *kaus? 
57252:*zgad (s.v.), *xaiz (s.v.) 
57640:*xaiz 
57765:*haiz
```


## [2026-09-14T03:10:13.197Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT haxs / xaez ===\"\ngrep -n \"haxš\\|xaēz\\|/aeza\\|xaez\" BRT.txt | head -30"
}
```


### [2026-09-14T03:10:13.253Z] TOOL RESULT

```
=== BRT haxs / xaez ===
```


## [2026-09-14T03:10:14.927Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28483,28560p' CHEUNG.txt"
}
```


### [2026-09-14T03:10:14.984Z] TOOL RESULT

```
*xaiz ‘to rise, ascend; increase’ 
*MIDDLE PERSIAN: (+ *aua-) MMP ’wxyz- ‘to descend’ || (+ *à-) MMP ’xyz-, BMP 
'hyc- (KDMWN-) /4xéz-/ ‘to rise (up), MMP ’xyzyn- (caus.) ‘to raise’ || (+ *pari-) 


*xaiz 441 


MMP prxyz- ‘to stand around, attend, serve; be, exist; dwell in, occupy’ (LW) 
c DMMPP: 79b, 71b, 281b 

(+ *aua-) Pres.: IND. 3sg. MMP "wxyzyd; Partic.: perf. pass. MMP ’wxyst || (+ *ä-) Pres.: IND. 25р. 
MMP ’xyzyh, BMP "hycyh /axezeh/, 35р. MMP "xyzyd, BMP ’xycyt /axezed/, IMPV. 2sg. MMP “xyz, 
2р1. MMP ’xyzyd; Partic.: perf. pass. MMP ’xyst, caus. MMP ’xyzn’d || (+ *pari-) Pres.: IND. 3sg. MMP 
prxyzyd 

*PARTHIAN: (+ *4-) "xyz- ‘to rise’ || (+ *pari-) prxyz- ‘to stand around, attend, serve; 
be, exist; dwell in, occupy’ = Ghilain: 61 f. | DMMPP: 79b, 281b 

(+ *а-) Pres.: IND. 35р. "xyzyd, 3pl. ’xyzynd, SUBJ. 15р. ’xyz’n, 2sg. *’xyz’h, IMPV. 2pl. ’xyzyd; 
Partic.: perf. pass. ’x’st || (+ *pari-) Pres.: IND. 35р. prxyzyd, 3р1. prxyzynd, SUBJ. 1sg. prxyz’n, 35р. 
“prxyz’h; Partic.: perf. pass. prx’st 

*KHOTANESE: (+ *ati-) ? ttihiysde ‘moves up’ || (+ *abi-/*ui-) bihiys- ‘to expand’, 
LKh. bihis- (caus.) ‘to raise’ || (+ *aua-) vahiys- (vahaiys-) ‘to descend’, LKh. vahis- 
(caus.) ‘to make descend’ || (+ *ham-) OKh. hamkhis- ‘to count’. © On ttihiysde cf. 
MacKenzie 1969: 399; differently DKS: 130b "rather tti hrysde with resumptive 
pronoun". || bihiys- with the meaning ‘to mount’, quoted by Bailey, DKS: 294, does 
not exist, on which see Emmerick, SVK I: 90 f. = SGS: 100, 122, 136 

*SOGDIAN: (+ *ati-) CSogd. txyz, MSogd. txyz ‘to set, go down (of sun, moon)’ || (+ 
*aua-) SSogd. ’wxz, BSogd. ’wxz, CSogd. ‘ухх ‘to descend’, SSogd. ’wxyz, 
BSogd. ’wx’yz (caus.) ‘to bring (down)’ || (+ *a-) SSogd. "xst- (past stem) ‘to rise’ 
|| (+ *pati-) BSogd. pcx’yz, MSogd. pcxyz- ‘to kneel’ || (+ *ham-) BSogd. ’nxz-, 
CSogd. "xz- ‘to rise’, BSogd. ’ny’yz, BSogd. ’nx’yz, CSogd. ’xyZ (caus.) ‘to raise’ 
(+ *ati-) Pres.: SUBJ. 350. CSogd. txyzt || (+ *aua-) Widely attested: Pres.: IND. 3sg. BSogd. ’wxzt, 3pl. 
BSogd. ’wxz’nt, SUBJ. 15р. SSogd. ’wxz’n, OPT. 2sg. SSogd. ’wxzy’, etc. || (+ *a-) Pret.: intr. IND. 3sg. 
SSogd. ’’xSt || (+ *pati-) Impf.: IND. 35р. BSogd. pc’yx’yz, MSogd. pcyxyz || (+ *ham-) Widely attested: 
Pres.: IND. 3sg. BSogd. ’nxzt, SUBJ. 3sg. BSogd. "nxz't, 1р1. BSogd. ’nxz’ym, 3р1. BSogd. ’nxz’nt, etc. 
*CHORESMIAN: m/xyz- ‘to rise, get up’, m/xyz(y)- (caus.) “о cause to rise, elevate, 
lift; to cause to grow’ || (+ *ati-) m/cxyz- ‘to arise and proceed; to be stirred up’, 
mjcxyzy- (caus.) ‘to stir up (dust, wind, a certain case)’ || (+ *aua-) ? wXs- (intr.) ‘to 
hang down’ || (+ *fra-) rxyz- ‘to happen, occur (to), come into being’ = Samadi: 
248, 53, 223, 175 

*NWIR: NP xastan/xéz-, Awrom. hur (e)stäy/ hur (e)z-, Gur. (Kand) hur -iz-/hur za 
‘to rise, get up’, Awrom. hur eznay/ hur ezn- (caus.) ‘to make stand up’, Mah. xizis 
‘jump’ || (+ *a-) Kurd. (Sor.) axez ‘climbing, leaving, moving’ (in axez kirdin ‘to 
climb, leave, move [of multitude, herd]’) 

*NEIR: Oss. I. xizyn/xyzt, D. xezun/xizt ‘to climb’, Pash. xeZ-/xatol ‘to rise’, Sangl. 
xäz-/xöt ‘to rise’, Yghn. јах-/Јахіа ‘to rise, ascend, get ready’, Sh. (Baj.) x&z, Rosh. 
xiz, Bart. xiz, Sariq. xeyz ‘straight, right, front’ || (+ *pati-) Wa. potxoz-/potxozd- ‘to 
become tired’ || (+ *ham-) Wa. giz-/gazd ‘to rise’ (< *han-gaiza- < *han-yaiza- < 
*han-xaiza- ?) 


442 *xa(m)p/b 


*MISC: Par. xist kan- ‘to rise, jump’ 

© The "xiz-"forms have been exhaustively treated by Gershevitch 1952a: 488 ff., 
who argued for the existence of three different roots: *haiz- ‘to rise’, *h/xaiz- ‘to 
creep’, *xaiz- to wait for, look for; to protect, pasture’. For ‘to creep’ I would rather 
reconstruct the root as *xaz-, with root vowel *a (on account of NP pres. xaz-). The 
etymology which ties Khot. ham-khis- ‘to count’ to YAv. ahaxsta- ‘unnumerable’ 
(Leumann, Zur nordar. Spr.: 31; ELO: 85f.) is formally difficult. 

“PIE LIV: — | Pok.: 


*REFERENCES: KPF I: 80a; EVP: 98; КРЕП: 190 f.; Andreev — PeSéereva: 266b; MacKenzie 1966: 97; 
EVS: 100a; Abaev, Slovar’ IV: 207 f; Steblin-Kamenskij 1999: 177, 281; Cabolov 2001: 100 


*xa(m)p/b ‘to dismount, descend, move away, leave behind ?’
```


## [2026-09-14T03:10:31.804Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HRN','AHD','KLN','MON','IEC','ETM','NYB','FVS','BQT','HUB','PHD','BRT','WLD','SYN','SKT']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-14T03:10:33.216Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== FVS {"title": "(not in Table IV — probably a typo for FVF or FSF)", "kind": "none", "url": null, "lookup_hint": "Check the two citations against FVF (Emam Shushtari) and FSF (Noushin).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "abbreviation not defined in Nourai's Table IV."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-14T03:10:43.525Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f,targets in [('IEC.txt',[18061,17925]),('POK_full.txt',[84545,83273]),('HRN.txt',[4230,4609]),('AHD_watkins1985.txt',[1034])]:\n    txt=open(f,encoding='utf-8',errors='replace').read()\n    lines=txt.split('\\n')\n    # compute leaf index for a line number\n    for t in targets:\n        pre='\\n'.join(lines[:t])\n        leaf=pre.count('\\f')\n        print(f,t,'leaf(0-based ff count)=',leaf)\nEOF"
}
```


### [2026-09-14T03:10:44.782Z] TOOL RESULT

```
IEC.txt 18061 leaf(0-based ff count)= 745
IEC.txt 17925 leaf(0-based ff count)= 739
POK_full.txt 84545 leaf(0-based ff count)= 0
POK_full.txt 83273 leaf(0-based ff count)= 0
HRN.txt 4230 leaf(0-based ff count)= 123
HRN.txt 4609 leaf(0-based ff count)= 134
AHD_watkins1985.txt 1034 leaf(0-based ff count)= 97
```


## [2026-09-14T03:10:45.388Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB glossary xez ===\"\ngrep -n \"axēz\\|āxēz\\|xēz\\|xēst\\|xāstan\" NYB_vol2_glossary.txt | head -20\necho \"=== NYB rist ===\"\ngrep -n \"rist-\\|ristāxēz\\|rist?\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T03:10:45.456Z] TOOL RESULT

```
=== NYB glossary xez ===
3323:rist-āxēz [lyst?hyc'] the resurrection of the dead 12?5, 6411-13, 7118. 7610. 8326, 8821. 91°. 1057. 12022. — From rist (g. v.) + Gxéz, pres. st. of dxistan (g. v.); Paz. rist-@xeZ (and other spellings); NP rastā- xéz ‘day of resurrection’, ‘tumult’.
3324:rist-āxēzišnēh [~-Snyh] = the preceding w., 1061,
6782:rist: ~ ristaxčž- rist-āxēz rčd: rot
7353:rastāxēz: rist-āxēz.
=== NYB rist ===
1600:fröstitan [ŠDRWN-tn' 38°] frést- [SDR- WN-; 2nd. p. sg. plystyh: fréstéh 3°]; pt. = pret. pass. 3d p. sg. frestit [ply- styt' 44 with act. construction; SDRWN- yt', -t']: to send 211, 39.11, 44 ete. passim. — In FrP 23 some MSS give fréstdtan, others frestitan as the equivalent of the ideogr. MPrs pryst’dn, pt. pryst’d, fryst’d, prystyd, pres. pryst-; NP firistädan firist-. A secondary formation from Av. fračšta- v. fréstak. l
2961:paristätan [plst’tn'], paristitan [plstytn'] parist- to worship, to adore, to submit to, to embrace (a religion) 194. 7511, 82.12, — < pari + stā-, v. ēstātan and cf par- ēstātan; Prth *part-štā- in Arm. lw. am- barišt ‘impious’ < Arm neg. an- + *parištā-, pastaun < *parštaun < "pariš- tamna- (middle pt.) ‘cult, service, office’, past-em ‘to worship’; in SW with -st- > -st-: MPrs pres. pryst-, and the inf. assum- ing the SW ending -ītan (cf MPrth pwrs'dn: MPrs pwrsydn, etc.): Paz. pa- rastidan parast- = NP; Verbum 194 sq.
3323:rist-āxēz [lyst?hyc'] the resurrection of the dead 12?5, 6411-13, 7118. 7610. 8326, 8821. 91°. 1057. 12022. — From rist (g. v.) + Gxéz, pres. st. of dxistan (g. v.); Paz. rist-@xeZ (and other spellings); NP rastā- xéz ‘day of resurrection’, ‘tumult’.
3324:rist-āxēzišnēh [~-Snyh] = the preceding w., 1061,
6782:rist: ~ ristaxčž- rist-āxēz rčd: rot
7353:rastāxēz: rist-āxēz.
```


## [2026-09-14T03:10:54.368Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=txt.split('\\f')\nfor i in (744,745,746):\n    p=pages[i]\n    print('---leaf',i,'---')\n    print(p[:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T03:10:55.505Z] TOOL RESULT

```
---leaf 744 ---
S sestríni, Cz. sestřin, adj. ‘sisters’; R cf. Sürin, m. (*wife's brother’; fr. *sue-suesrino- ?). Cf. suesrios, above) | suesue (suosue), suésu, sus- 'so, thus, as; anyway' Kurd. xo ‘so, well: Umb. svesu ‘so, thus"; Mir feib, Ir. féibh as: Go. swa ‘so’; swaswe "as": OE swa, swaswa & swæ ‘so’; Norw. S
---leaf 745 ---
 fr. *suibhios or fr. *suibios); Gk. cf. a-íphnes, adv. “suddenly”; | 1353 | a-iphnídios, adj. ‘sudden’; cf. a-ipsa immedia- tely'. Consonantism ambig. in Ir. siubhlaim, v. ‘roll along, go’ (cf. suib-) and in MHG swibelen, v. ‘frolic’, cf. mod. E to swivel, (but cf. suiual- for the MHG form) | suid- (1) ‘
---leaf 746 ---
rming, lovely”; seaghais, f. (/pleasure', fr. *suigosti-); MHG swiche, sf. (fraud; OE swic, n. *il- lusion, deceit’; swica, swice ‘cheat’; swician, v. id.; ON svik, npl. *fraud' | sulios “own, one's own; son, pet’. Variant: | 1355 | suiios, suios, cf. suelios, suoi Skt. sviyah, adj. “own, personal’; svi-,
```


## [2026-09-14T03:11:04.244Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON سیفلیس ===\"\ngrep -n \"سیفلیس\\|سفلیس\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== BQT خاستن ===\"\ngrep -c \"\" BQT_v2_pages.txt\ngrep -n \"رستاخیز\\|رستخیز\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-14T03:11:04.353Z] TOOL RESULT

```
=== MON سیفلیس ===
MON_part2.txt:28055:آزردگی, اندوه. (.) (پز.) سیفلیس. (فع.) 
MON_part2.txt:71577:ابتلاء گرفتاری. (عم.) کوفت» سیفلیس. سال 
MON_part2.txt:71675:فرنگ» کوفت» سیفلیس. ار خلیل: آتشی 
MON_part2.txt:71685:دانه‌های مربوط به مرحلهٌ دوم مرض سیفلیس 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:28055:آزردگی, اندوه. (.) (پز.) سیفلیس. (فع.) 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:71577:ابتلاء گرفتاری. (عم.) کوفت» سیفلیس. سال 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:71675:فرنگ» کوفت» سیفلیس. ار خلیل: آتشی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:71685:دانه‌های مربوط به مرحلهٌ دوم مرض سیفلیس 
MON_part1.txt:82279:سیفلیس: ۰18 () (پز.) مرضی عفونی و 
MON_part1.txt:83222:سخت يا شانکر سیفلیسی که مشخص دورة 
=== BQT خاستن ===
41071
incoming/BQT/BQT_v3_pages.txt:18699:‏رستخیز « عخمبی‌است که" آنرا خرفه کویندوفرقع
incoming/BQT/BQT_v3_pages.txt:30601:‎ws cael‏ با فا بروزن رستخیز؛ بمعنی
incoming/BQT/BQT_v3_pages.txt:33252:‏رستخیز ‎bee‏ بزرکه سوراخ دار را کویند
incoming/BQT/BQT_v3_pages.txt:43842:رستخیز + غربال سوراخ تنگه را گوبند .
BQT_v2_pages.txt:24027: ‫—‪AtA-‬‬                                                                                          ‫رستاخیز‪‎‬‬
BQT_v2_pages.txt:24041:‫رستخیز ‪ = ۱‬بنتح اول وثالك » بمعنی‬                                                                  ‫باشث ‪.‬‬
BQT_v2_pages.txt:24043:             ‫رستاخیز است که فیامت باشد و‬
BQT_v2_pages.txt:24058:     ‫‪,‬ازند ‪ 012۵58051۲‬داسشق ‪ ۳۱۱2‬؛ بنابرین رستاخیز (مخفف آن » رستخیز)‬
BQT_v2_pages.txt:24062:                            ‫‪۳‬‬   ‫ومخفف خود آن «سَخز » (م‪).‬‬            ‫رستاخیز («‪.‬م‬    ‫‪ - ۷‬مخفف‬
BQT_v2_pages.txt:26575:                     ‫رك‪ :‬ريدن ‪.‬‬       ‫‪۸ 7‬‬         ‫کی‬                 ‫ر‬             ‫‪۲‬ص‪ ۳۳ ۲‬رك ‪ :‬رستاخیز‪.‬‬
```


## [2026-09-14T03:11:09.002Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24010,24070p' BQT_v2_pages.txt\necho \"=== nearest pdf page tag ===\"\nawk 'NR<=24070 && /\\[pdf page/ {l=NR; t=$0} END{print l, t}' BQT_v2_pages.txt"
}
```


### [2026-09-14T03:11:10.001Z] TOOL RESULT

```
‫کوبند ‪ -۱۷‬وبضم اول ماشی روبیدن باشد معنی‬                    ‫وفساد کردن در ميان مردم باشد و ایذجا بطریق‬
  ‫(‪ )۳‬چك‪ :‬همآ مده است ‪.‬‬                   ‫(‪ )۲‬چك ‪ :‬ژد و بازند ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬رستن‬


      ‫‪ - ۳‬قس‪ :‬رسمان‪.‬‬                 ‫قس‪ :‬بازری ( باز رسنده )‪.‬‬        ‫‪۴‬‬        ‫‪ - ۱‬رکه‪ :‬رسدن‪.‬‬
                                           ‫رزژد » رزد (ه‪.‬م ‪(.‬‬                 ‫؟ ‏ رکه ‪ :‬اری ‪۰‬‬
                   ‫کلو را ز رسی بسر برمیر‪.‬‬                      ‫بیلفنج و زالففد خوش خور‬
  ‫‪.‬‬       ‫ابوشکور بلخی‪(« .‬فت فری ‪٩۹‬‏‬

  ‫‪ ۸‬رکه ‪ :‬رسیدن»‬                        ‫رکه‪ :‬رست ‪.‬‬      ‫‪۷‬‬            ‫رکه ‪ :‬ی‪٩‬‏ همین ستون‪.‬‬     ‫‪۱‬‬
                       ‫‪٩ .‬‏‬        ‫» ابیز « بوتکر‬    ‫بهلوی ‪72‬‬            ‫هز ‪20102 ,‬‬     ‫‪۹‬‬         ‫رشتن ‪.‬‬

                   ‫» رسته‌بود چون صف‪:‬‬     ‫رجه ؛ رژه ‪” :‬رست‬      ‫‪~۹‬‬           ‫رکه ‪ :‬رستن ‪.‬‬     ‫‪°‬‬
                                          ‫چون ملك الهنداست از ریدکانش (آن دهد کاش ‪ .‬دهشدا)‬
               ‫‪.‬‬     ‫خمروی‬    ‫‪.‬‬   ‫بر خادم هندو دو رست‬   ‫کردش‬

      ‫‪€‬‬    ‫د لفت فرس*‪4‬‬
 ‫—‪AtA-‬‬                                                                                          ‫رستاخیز‪‎‬‬
 ‫رستگار است کهبمعنی خلاص و فجات باشد ‪-‬‬                    ‫بموط هم‬     ‫ضحک‬
                                                                        ‫می م‬‫وعت‬
                                                                              ‫روبید وبرآمد ‪ - ۱‬وی‬
 ‫و تزد محققین صاحب دولتی است که زخارف‬                      ‫آمده است ؟ ‪ -‬و نوعی از خاك سخت باشد ‪-‬‬
‫او‬   ‫دامنگیر حال‬   ‫وممنوی‬       ‫و تملقات موری‬    ‫دلوی‬
                                                           ‫ومطلق خاکه را نکیفزته اند‪ -‬و بمعنی شجاع‬
                                                ‫نباشد ‪.‬‬    ‫ودلیر ‪ -‬وچیره وغالب آمدن ومتولی شدن هم‬
                                                                                                  ‫‪۰‬‬   ‫صبت‬
‫‏‪ o‬بروزن افلااء ‪ ۰‬شاج ءازه ای‬        ‫رستاك‬

‫راکومند که ازبیخ درخت برآبد ؛ و پاین معنی‬                   ‫‪)۱‬‬
                                                             ‫رستاخیژ ‪ ۴۰‬با خای قطه د(ار‬
                 ‫بشاین قطه دار هم آمده است‪.‬‬                ‫بر وزن دستاویز ‪ ,‬قیامت را گوبند که محشر‬
‫رستخیز ‪ = ۱‬بنتح اول وثالك » بمعنی‬                                                                  ‫باشث ‪.‬‬
 ‫؛بم اول بمعنی‬
             ‫رستاخیز است که فیامت باشد و‬
                                                            ‫رستاد ‪ - ۴‬بر وزن هقتاد ‪ .‬مخفف‬
                                       ‫لوخیز باشد ‪.‬‬
 ‫رستگار ‪ ۲۰‬با ان فارسی بر وزن‬                              ‫راستاد است که بمعنی وظیفه و راب و روزباله‬
                                                                                                   ‫باشك ‪.‬‬
‫قندهار » بمعتی خلاص ونجات وفیروزی بابنده‬
                                            ‫باشد ‪¥.‬‬         ‫رستار * ‪ -‬بر وژن دستار ‪ .‬مخفف‬

                                                                            ‫(‪ )۱‬چك ‪ :‬باخا ‪.‬‬

                                                ‫هکر ‪‎ :‬یر ‪.‬‬      ‫‪۰‬‬        ‫‪ :‬رستن ‪.‬‬     ‫رکه‬
                                                                                         ‫‪١‬‬
     ‫‪.‬دذرشته) ‪ .‬بهلوی ‪ + 451۲‬خیز (رك ‪ :‬خاستن) ‪,‬‬
                                              ‫‪1‬ست‪۳‬ا‪ ( 805-1‬مرده گ‬
                                                                ‫‪ - ۴‬از او‬
     ‫‪,‬ازند ‪ 012۵58051۲‬داسشق ‪ ۳۱۱2‬؛ بنابرین رستاخیز (مخفف آن » رستخیز)‬
                                                                    ‫پهلوی ‪ 2072۱51۲‬پ‬
         ‫رك‪ :‬راستاد ‪.‬‬   ‫‪۴‬‬              ‫ح ‪۱٩‬‏ ‪.‬‬       ‫لغةبمعنی برخاستن مرد کان است « بشتها اس ‪۳۳۳‬‬
         ‫تار (یودد فاعلی و اصان ‪.‬رکه ‪ :‬دادار) ‪.‬‬             ‫از ‪ :‬رس ( رستن » رهیدن) ‪+‬‬       ‫‪6‬‬
                            ‫‪۳‬‬   ‫ومخفف خود آن «سَخز » (م‪).‬‬            ‫رستاخیز («‪.‬م‬    ‫‪ - ۷‬مخفف‬

                        ‫‪ - ۷‬از ‪ :‬رست (رستن » رهیدن) ‪ +‬کار (یسوند فاعلی ومبالفه) ‪.‬‬
      ‫بضم راء و فتح تاء مرکب ازدو جزو‪ :‬رس =‬               ‫تم‬
                                                           ‫ومس ‪۳‬‬
                                                               ‫رسته‬
                                                                  ‫‪ #‬رستم = رستهم ‪ ۳‬رو‬
     ‫(بالش ‪ ,‬نمو) ر[ستن و روبیدن از همين ربشه است] ‪ +‬نهم = ‪ 301321‬درپارسی‬                             ‫‪8‬‬
     ‫باستان کوانها و دیگر بخشهای اوستا بمعنی دلیرو پپلوان‪ .‬تهمتن ایز ازهمین ریشه است بمعنی‬
=== nearest pdf page tag ===
```


## [2026-09-14T03:11:18.789Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خاستن\" BQT_v2_pages.txt | head -20\necho \"=== خیزیدن ===\"\ngrep -n \"خیزیدن\\|خیز \" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T03:11:18.859Z] TOOL RESULT

```
7254: ‫روزی خواهر ابشانراطلبید » یکی از ابشان خود‬                                  ‫هنگام نشتن وبرخاستن دست برپشت کسی نهد‬
7781:  ‫چهر ه شدن ‪ -‬کناءه ابزرخاستن‬                                  ‫ووی‬
9179:                        ‫‪, ۴۳‬افنانی أقا‪ ( 21‬بلند شدن» برخاستن) «هویشمان‪ »۲۱14‬ر‬
11967:                ‫‪ " 281‬سفدی ‪ 11261‬همریشةٌ خاستن فارسی « لیبرکه ‪iK ۳۳۱‬‏‬                                 ‫بلند شدن ) از ‪-‬‬
12868:                                            ‫برخاستن‬   ‫وفت‬
15429:‫هوز‪.‬بمعنی برخاستن وبرجستن باشد ‪۴٩‬‏ ‪ -‬وامر‬
15431:‫ازبرخاستن همست بعقی برخیز ‪۴٩‬‏ ¬ وبمه‌نی‬                                                        ‫وبی تةزب ت‬
15537:   ‫<< خاستن (ه‪.‬م‪).‬‬                        ‫‪ -‬بهلوی ‪0‬‬                            ‫‪e:‬‏‬             ‫‪۴‬‬         ‫خیروان »ر‬
15634:                                                    ‫از برخاستن و برپایشدن آلت تناسل است ‪-‬‬
18493:                         ‫مفتوح بنون ک‬                                                    ‫که ازییهاری برخاستن باشد ‪۰‬‬
24055:     ‫‪.‬دذرشته) ‪ .‬بهلوی ‪ + 451۲‬خیز (رك ‪ :‬خاستن) ‪,‬‬
24060:         ‫رك‪ :‬راستاد ‪.‬‬   ‫‪۴‬‬              ‫ح ‪۱٩‬‏ ‪.‬‬       ‫لغةبمعنی برخاستن مرد کان است « بشتها اس ‪۳۳۳‬‬
34732:  ‫سپریچیدن = کنابه از سکرثی‬                                    ‫برخاستن ویبدار گردبدن باشد ‪ -‬و کنابه‌ازمسافر‬
=== خیزیدن ===
567:  ‫قر ده است و هر کزآن تربمت‬       ‫بین کوه کته شمشیر و تکبی کره و حاصلخیز است و دارای ‪۳‬‬
1544:                                                          ‫رها شدن و خیز کردن و کرب ‪۱‬ختن باشد ‪- ۷‬‬
3567:       ‫(‪ )۳‬چس‪ :‬خیز زنگه‪.‬‬               ‫(‪ )۲‬چك‪ :‬ژد ویاژند ‪.‬‬                 ‫)‪ ۱‬چش ‪ :‬هده‬
4210:      ‫گفتم که زود خیز وهمی کرد چام چام ‪.‬‬                  ‫کفتا مرا چه چاره که ارام هیچ یت‬
7057:                                                        ‫بمعنی جستن وخیز کردن گ‪-‬رویختن باشد ‪.‬‬
8440:                                                   ‫شهری است حن خیز ‪ -‬و بمعنی قلعه و بارو‬
10150:  ‫بزبادة ان هذا الثور کون بارش خرخیز » و فحن‌تری له من‌الفلظالزائد علی‌عرض‌الاصبعین مابکاد‬
10152: ‫جلبهالی الاوعال من خرخیز اولی‪,‬هلانهم اليه‌اقرب ولم بجلب من‌العراق وخرامان وقدقبل‌فیه ایض‬
10886:                     ‫خر خیز م‬
10919: ‫‪« - ۱‬سخن اندر ناحیت خرخیز » مشرق وی ناحیت چین است و دربای اقیالوی هشرقی‬
10925:  ‫ابشانر! خرخیز خاقان خوانتد ‪ « »...‬حدودالمالم‪ 7210161710 = > ۰۵‬د مینورسکی‪ .‬حدود ‪۲۸۲‬‬
12856:‫بکوبند و درماست کنند وبا طعام خورند )‪(٩‬‏ ‪-‬‬                  ‫خفت و خیز هکنابه ازآهتگی وتانی‬
12978:‫از دهرهای حن خیز است داخل جهاز دختران‬                     ‫« با‬    ‫)‪۱‬‬       ‫است‬   ‫ووامی‬   ‫نام جا وعقامی‬   ‫‪۰‬‬   ‫ویواو رده‬
13134:   ‫‪ - ۴‬در مفرب گیلان ک»وهستانی وسرد سیر » دارای دره های حاسلخیز ‪ ۰‬رمکز آن‬
14706: ‫ولابتی است شکرخیز آزفاری که شوشترشهرآن‬                              ‫طرف سرجوال بگردن باربردار باشد ‪.‬‬
15431:‫ازبرخاستن همست بعقی برخیز ‪۴٩‬‏ ¬ وبمه‌نی‬                                                        ‫وبی تةزب ت‬
15438:        ‫خیز اب ‪ ۶‬بروزن‌میزاب کو‬                                  ‫بهار رائیزگوبند ‪ - ۷‬وبمعتی بيار وغلبه هم‬
15441: ‫خیز بگیر ‪ ۱‬نوعی‌ازبازی‌باشد‪,‬وآن‬
15477:      ‫رکه‪ :‬خیزه گیره ‪.‬‬         ‫_‬   ‫‪۵‬‬    ‫_ از‪ :‬خیز (ه‪.‬م‪ + ).‬آب‪.‬‬           ‫‪۴‬‬    ‫رکه ‪ :‬خز آب ‪.‬‬                      ‫‪۴‬‬
15488:‫‪ -‬بروزن پیش (‪. )۲‬وز اری باشد‬                     ‫خیش‬                 ‫مقدار که خواهند نورآاخیز گیر بحذف بای‌ابجد‬
```


## [2026-09-14T03:11:24.439Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"########## around 11940-11990\"\nsed -n '11940,11990p' BQT_v2_pages.txt\necho \"########## around 15400-15450\"\nsed -n '15400,15450p' BQT_v2_pages.txt"
}
```


### [2026-09-14T03:11:24.515Z] TOOL RESULT

```
########## around 11940-11990
                                            ‫گفته‌اند ‪.‬‬   ‫نامگیاهی بوده‬             ‫»‬    ‫سمنف‬   ‫روزن‬     ‫حز ند =‬




                           ‫‪۰‬‬   ‫همحدون‬      ‫(‪ )۲‬چك» چش ‪:‬‬                        ‫‪ :‬نزدبك‬         ‫چش‬    ‫)‪ (۱‬چك‪.‬‬

                                                                           ‫‪.‬‬       ‫‪۳ :‬و‬     ‫چش‬      ‫چك ‪,‬‬    ‫(‪)۳‬‬


   ‫لند‪-‬‬     ‫قیابی‬
                ‫ررق‬
                  ‫فش‬‫اقات‬
                       ‫وقی‬
                         ‫‪- ۱‬پپاوی ]‪( 22262‬ه ‪ .‬و‪ .‬بلی در مجلة مدرسة تح‬
   ‫ج ‪ , 02‬شمارۂ ‪ ۱‬س ‪.» ) ۲ ۱‬نام قومی که از قدیم در حدود نرکستان و نیزقفقاز اقامت‬
    ‫و بحرخزر ازاسم همین قوم مأخون است ‪ « .‬فرهنکه شاهنامه‬                               ‫خزخزرران‬
                                                                                              ‫وحیت‬
                                                                                                 ‫داشتند وئام نا‬
   ‫‪ «۱ ۴‬سخن اندرناحیت خزران ‪ -‬ناحیتی است؛» مشرق وی دیواری‬                                      ‫‪ :‬خزران ‪.‬‬        ‫رک‬      ‫‪۷‬‬
    ‫است میان کوه ودربا "دویگر درباست و بعضی از رود آتل (= ولگا)‪ ,‬جونوب وی سربرحت‬
    ‫ومغربش کوه است وشمالش براذاس است ‪( ...‬از شہرهای ابن ناحیت است ‪ ):‬آتل » ‪ ...‬سمتدر‪.‬‬
   ‫لن»جر » بيضاساوغر » ختلغ » لكن » سور » مسمدا » ‪ ...‬طولای ‪٠‬‏ لوغر ‪« »..‬حدودالمالم‬
                                                                                  ‫خبمج‬
                          ‫‪ ۲ ۹-۹۱۱۰‬رک ‪ :‬حدود العالم ترجمه وشرح‌مینورسکی ص ‪٩٥٤‬‏ ببعد‪.‬‬
   ‫‪ ۵‬اسم فاعل از«خزیدن»‪.‬‬              ‫‪ ۴‬رکه ‪ :‬خز ‪.‬‬           ‫رفا«ن» ‪.‬‬    ‫خزممح‬‫‪۴‬‬
   ‫‪( 0251261 - ۸‬خلستن‬                ‫‪ - ۷‬رک‌خرزهره‪.‬‬         ‫رکه ‪ :‬خیزدو که ‪.‬‬  ‫‪۱‬‬
                ‫‪ " 281‬سفدی ‪ 11261‬همریشةٌ خاستن فارسی « لیبرکه ‪iK ۳۳۱‬‏‬                                 ‫بلند شدن ) از ‪-‬‬

                                                                     ‫‏‪ ٩‬اسم مفعول ا«زخزبدن؟‪.‬‬
                                                           ‫بیان نهم‬

            ‫در خای نقطه‌دار باسین بینقطه مشتمل برچهل ودو لغت و کنایت‬
                                                                    ‫حس۔ بفتح اول وسکون‌تانی “ معروف‬
                                                                    ‫است که خاشه وخلاعه ءخاشاك باشد ‪۷‬‏ ومردم‬
‫خسائیدی؟ ‪ -‬بروزنوسانیدن‪ .‬سعنی‬
                                                                    ‫فرومایه ویخیل و رذل دون ونا کی وزبوترانیز‬
                                   ‫بدندان کرشردن باشد ‪.‬‬             ‫نگاو کوعسان‬               ‫کرد‬             ‫کی‬
‫مستقمل‬           ‫خساید = بر وزن راید ‪.‬‬
                                                                   ‫می‌باشند‪ .‬خصوسا کفار صحرانشین ؛ وبعضی گوبند‬
    ‫«‬‫خالیدن است منی بدتدان کرشند ‪۵‬‬                                 ‫تاشمعتی هندی است چه خسبز ‪,‬ار عندی قومي‬
                                                                   ‫باشتد از کفار که دکروههای ماین هندوستان‬
‫فرتن ‪ -‬کناب ا‬ ‫خس بدهن گ‬
                                                                   ‫‪ -‬وتام جانور کی است که بدن او‬        ‫اند‬
                                                                                                          ‫نا‌سا‬
                                                                                                              ‫ءکخت‬
         ‫عجز کردن وزیتهار وامان خوامتن باشد ‪#.‬‬
                                                                    ‫شبیه است بدانةٌ جوی کوچك و پابهای اريك‬
‫لوس ۔‪ -‬با بای فارسی بر وزن‬                        ‫جس‬
                      ‫‪۰‬‬                 ‫&‬            ‫‪:‬‬

########## around 15400-15450
‫وانواع آن بہار ا‪:‬ستیکی ازآنها سیاه رنگ‬
                                                                 ‫خیرو = بااول بثالی رسیده والث بواو‬
‫میباشد وآنرا خیری خطابی میگویند ودبگری‬                           ‫» بمعنی خطمی باشد ‪, ۱‬و بعضی گوبند‬
‫رنگ‬           ‫ت‬
                                                                                                                       ‫کشیده‬
              ‫ف و‬
                ‫هدنی‬
                   ‫بئفش است و آنرا خبری مسر‬
                                                                 ‫نوعی اگزل‌خطمی است وآن‌سرخ رنگ وسفید‬
‫دیگر سفید و سرخ است و آن‬                    ‫عی‬
                                             ‫نندو»‬
                                                 ‫وان‬
                                                   ‫خو‬            ‫رنگ هم میباشد وخبازی ‪ ۴‬همان است وممرب‬
‫گونند ‪,‬‬       ‫صحرا‪:‬بی میباشد و آنرا خبری خرامی‬
                                                                 ‫آن‌خیروجاست » وبضی گفته‌اند خیری ‪ ۴‬است‬
‫است وآنرا خبری شیرازی‬                   ‫زعرد‬
                                           ‫وبك نو‬                ‫که گل‌هميشه بهارباشد‪,‬وبمعنی‌اول بازای‌نقطه‌دار‬
‫‏‪a‬‬                                                                                                     ‫نیز بنظر آمده |بسح‬
‫عصفیر و عسفیره خوانند (‪ . )۱‬طبیمت آن گرم‬
 ‫الدکه‬         ‫ته‬
                ‫فی‬‫زوکرا‬
                      ‫و خثك است ‪ -‬و خر‬                            ‫=روزن تیره » غباری رگاویند‬
                                                                                           ‫حیره ب‬
‫خبازی باشد ‪ - ۴۷‬وبمعنی صفه وابوان و طاق‬                          ‫که درپیش چشم پدید آبد ‪ - ۴‬و بمعنی شوخ‬
‫وروأق‌هم هت ‪٩٩‬‏ — ورنگ سرخرا نیز گونند‪.‬‬                          ‫دیده ویشرم وآبزیرم وهرزه وناهموارویحیا *‬
‫حیز ‪ -‬بکسر اول وسکون انی و زای‬
                                                                 ‫ولجوج وس رکش وسخن ناشنوباشد‪ -‬ورند وشجاع‬
                                                                  ‫رایز گفته‌اند؟ ‪ -‬ویمعنی بی‌سیب وبنهوده‬
                                                                                                                            ‫ودلیر‬
‫هوز‪.‬بمعنی برخاستن وبرجستن باشد ‪۴٩‬‏ ‪ -‬وامر‬
                                                                  ‫وتعحب وشگفت بار وحیران‬
‫ازبرخاستن همست بعقی برخیز ‪۴٩‬‏ ¬ وبمه‌نی‬                                                        ‫وبی تةزب ت‬
                                                                  ‫نته و فرومانده هم هت ‪ -- ۷‬بو پمعنی‬
       ‫موج آپ وکوهة آب لزا مداو‬                                                                      ‫وس رگ‬

                        ‫کبوتر ماده در وفت شاط نر‪.‬‬                 ‫آشکار وظاهر ‪ -‬و رة وتاريك ‪ - ۴‬و عضوبکه‬
                                                                 ‫بخواب رفته باشد لیز گفته اند ‪ -‬وگل همیشه‬
 ‫‪.‬عه وموج‬
        ‫خیز اب ‪ ۶‬بروزن‌میزاب کو‬                                  ‫بهار رائیزگوبند ‪ - ۷‬وبمعتی بيار وغلبه هم‬
                                             ‫آب رگاوند‬
                                                                                         ‫بنظرآمده است ‪۸‬‬
 ‫خیز بگیر ‪ ۱‬نوعی‌ازبازی‌باشد‪,‬وآن‬
‫بطریق دابره بر سر با‬               ‫مهمی‬
                                      ‫چنان استج ک‬                ‫خیره دست کنابه از مردم س رکش‬
 ‫می‌شینند و شخصی بردور همین دایره از دتبال‬                                                                                 ‫باشد ‪.‬‬

‫دیگری هیدود‪ .‬اکر همان لحظه اورا گرفت بر‬                          ‫خیره کش ب نم اف وسکون شین‬
‫گردن او سوار مشود و بر دوردایره میگرداند‬                         ‫لوم بوی‌سبب کش باشد ‪-‬‬
                                                                                     ‫طبااکه‬
                                                                                          ‫قرشت ‪ ۰‬بی‌‬
‫وا کرپاره ای دوید ونتوانت بگیرد با نرد مك‬
```


## [2026-09-14T03:11:34.910Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c $'\\f' BQT_v2_pages.txt; grep -n \"pdf page\" BQT_v2_pages.txt | head -3\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor tgt in (11967,15429,24027):\n    print(tgt, 'ff before:', '\\n'.join(lines[:tgt]).count('\\f'))\nprint('total ff', t.count('\\f'), 'lines', len(lines))\nEOF"
}
```


### [2026-09-14T03:11:35.998Z] TOOL RESULT

```
680
11967 ff before: 203
15429 ff before: 262
24027 ff before: 408
total ff 683 lines 41071
```


## [2026-09-14T03:11:42.212Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (200,201,202,203,204,260,261,262,263,406,407,408,409):\n    p=pages[i].strip().split('\\n')\n    print('=== ff',i, '|', ' // '.join(x.strip()[:80] for x in p[:4]))\nEOF"
}
```


### [2026-09-14T03:11:43.357Z] TOOL RESULT

```
=== ff 200 | ‫ره‬      ‫سل‬                                                                   //  // ‫فقیرآنرا با خرما بکوبند وبخوردد ؛ بواینمعتی‬         ‫والث مجهول بر‬ // ‫‪ -‬نم اول ث‬                  ‫خروه‬
=== ff 201 | ‫خرش‬                                                                            //  // ‫و بمعنی شوم ونحس و نامبارك همآمده است‬               ‫جانور کی است که‌هرچه‌برزم // ‫وابوان وصفه را گنفزتەاند ‪.‬‬          ‫وبن دکه‬
=== ff 202 | ‫ان هشتم‬ // ‫بر شانزده لفت‬            ‫نقطه دار مشتما‪5‬‬           ‫در خای نقطه دار ‪ ۳‬را //  // 
=== ff 203 | ‫خز مر‬                                                                          //  //  // ‫شبیه باشنان ‪.‬‬        ‫انی‬
=== ff 204 | ‫بیان نهم‬ //  // ‫در خای نقطه‌دار باسین بینقطه مشتمل برچهل ودو لغت و کنایت‬ // ‫حس۔ بفتح اول وسکون‌تانی “ معروف‬
=== ff 260 | ‫—‬       ‫س‬                                                                    //  // ‫خهی ‪ - ۲‬بفتحاولبروزن زهی کلم‬                              ‫خهله ‪ » ۱‬بنتح ا // ‫ست ازخه وای »نی‬
=== ff 261 | ‫سب‬   ‫ست ‪۵ ۱‬‬ //  //  // 
=== ff 262 | ‫= ‪.‬‬ // ‫خیرو‬ //  // ‫نغری ‪:‬کان ات‬           ‫تاوزن‬           ‫خیری‬                             
=== ff 263 | ‫کز عتارم‬                                                                       //  //  // 
=== ff 406 | ‫‪- 6‬‬                                                                          //  // ‫رر بدن "ت بورژن رسیدن » بمعنی‬                      ‫اندازند وبعربی شربط کوبند  // ‫رنگه کردن باشد ‪.‬‬             ‫خوانند ‪ -‬وسکه انگور را کیفزته‌اند که بتازی‬
=== ff 407 | ‫بیان دهم‬ // ‫رای می نقطه باسین بی نقطه مشتمل بر ببست وبك لفت و کنایت‬                        //  // ‫ویت‬ ‫چیوزی باشد از خحبرکا‬    ‫اضداد است ‪-‬‬                    ‫ر سس س بفتح 
=== ff 408 | ‫—‪AtA-‬‬                                                                        // ‫رستگار است کهبمعنی خلاص و فجات باشد ‪-‬‬                    ‫بموط هم‬     ‫ضحک‬ // ‫می م‬‫وعت‬ // ‫روبید وبرآمد ‪ - ۱‬وی‬
=== ff 409 | ‫با‬                                                                             //  // ‫وفتح فوقالی وها ومیم هردوسا کن » رستم زالرا‬         ‫رسته ‪ ۱‬ب«روزن دسته ‪ ۰‬ // ‫ف‪2‬‬              ‫شده ولجات‌بافته باشد ومطلق صفرالگیوزبند‬
```


## [2026-09-14T03:11:54.599Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (159,160,161,205):\n    print('=== ff',i,'(printed ~',i+540,')')\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-14T03:11:55.593Z] TOOL RESULT

```
=== ff 159 (printed ~ 699 )
  ‫خاکبیز‬                                                                                            ‫‏‪a‬‬
 ‫مانندی باشد ازنقره و طلا ومس و امثالآن که‬                      ‫خالء‪ - ۱‬بسکون کاف تازی » معروف‬
 ‫‪_۴‬‬
             ‫ند‬
             ‫‪°‬‬   ‫‪۱‬‬
                       ‫و‪ ۶‬کر وغیر‬
                       ‫‪۳‬‬   ‫‪۲‬‬     ‫‪۳‬‬    ‫‪۰‬‬
                                               ‫بدانخاك‬
                                               ‫داق‬   ‫‏‪٠‬‬
                                                                ‫وان سک ار عنام آزعه ات و ری‬                 ‫ات‬
 ‫ومنگه انداز برح قلمه وحصار راهم کفته‌اند‬                      ‫قراب خوانند‪ -‬و کنایه ازاشی مطمثنه‪ -‬وشخص‬
  ‫یند کهبردور شامیانه‬   ‫ویز‬‫و پارچه ای رکاب‬                      ‫مط‬‫سلیمالنفس باشد‪-‬رفروننی و افتادکی‪ -‬و‬
‫وایبان دوزدد‪ -‬وبمعنی ساحروسحر کننده هم‬
                                     ‫س‬                         ‫ير و مزار (‪ )۱‬را فيز‬
                                                                                  ‫قو‬‫و فرمان بردار ‪- ۴‬‬
                                                 ‫‪® ۰‬‬
                                                          ‫بی‌قدر وقیمت و ضایم | ‪۳‬‬           ‫هوای‬
                                                                                               ‫‪-۴‬‬‫یز‬
                                                                                                  ‫چیند‬
                                                                                                     ‫گو‬
 ‫کنابه از افتاد کی کردن‬              ‫بودن‬      ‫خا‬              ‫و بکار لیامدنی رالیزهم(‪ )۲‬کفته‌الد‪ -‬وب کون‌کاف‬

                               ‫بودن است ‪٩‬‏ ‪۰‬‬   ‫و متواضع‬         ‫فارسی (‪ )۳‬بمه‌نی تخم هرغ باشد چه خانینه‬
‫خا کییز ‪ ۲‬بابای ابجد بروزن خاك‬                                 ‫باواوممدوله هم‬   ‫وباشمعتی‬     ‫از خا گثاست‪.‬‬   ‫مشق‬

                                                                                ‫آمده است که خواکت باشد ‪.‬٭‬
  ‫بجهت لفع خود جاروب کند و بییزد ‪ -‬کوتایه‬                       ‫خالكا نداز‪ -‬مروف است‪ .‬وآن بل‬
      ‫(‪ )۲‬چنین است دراصل » واین استممال جایز بوده ‪.‬‬                   ‫وطیم ‪ ...‬مزار‪ .‬‏‬
                                                                                     ‫(‪#)۱‬خم‪ - : ۳‬م‬
                                                                              ‫(‪ )۳‬چس ‪ - :‬فارسی ‪.‬‬
      ‫پپلوی ‪ « 62‬دهارله ‪ . › ۵۷۱‬کیلکی )‪ . ×8‬فریز ندی ویر ای وطنزی ‪61
=== ff 160 (printed ~ 700 )
    ‫پا‬     ‫‪۵‬‬




‫‪۰‬‬   ‫با ذال نقطه دار‬       ‫=‬    ‫ذلبلان‬       ‫ځا‬                  ‫ازکسی است که ازیرای حصول بمتصود بکارهای‬
        ‫باشد ‪.‬‬    ‫لان‬
                    ‫جفراانهو‬
                           ‫کنابه ازجسد وقالب کا‬                 ‫سخت و حرفتپای پست قیامدمابد ‪ -‬کنوابه از‬
        ‫ن‬
        ‫وتزبر‬
            ‫خا رنف ‪ -‬بارای قرش‬                                          ‫مردم دقیق‌النظر وباريك بین هم هست ‪.‬‬
            ‫آبکند » بمعنی گرد وغبار باشد ‪.‬‬
 ‫خاك ز لگین ‪ -‬عارت از طلاست ‪-‬‬
‫ولقره را تبز گفته‌اند "‪ ۳‬و کنابه از کلزار ولالهزار‬                               ‫درد ‪.‬‬    ‫از جسد وقاب آدمی(‪)۱‬‬
                 ‫هم هست ‪ -‬وآدمی زاد را لىز کوبند‬
                                                                ‫خاله خسبه "‪ ۳‬بطمخای نقطه‌داروسکون‬
‫خاك ردن‪ -‬کنابه از جاروب کردن‬                                    ‫» پرنده ایست‬    ‫اند‬   ‫سین بی لاطه ر فت بای‬

                                                                       ‫سحرای ی که آبرا بفارسی چرز ‪ ۱‬ورک‬
                                                                 ‫تی‌چفرق‬
                                                                                                         ‫گونند ‪.‬‬
    ‫کشیده » تضمی باشدکه آلرا باکافور دچرشم‬                      ‫امحد بر وزن‬    ‫خا کد ارن؟ = با دال‬
‫کشند » و در عربی بزرالخمخم و بزرالجنه (‪)۲‬‬
                                                                ‫آشمان ‪ ۰‬مزبله راکوبند ‪ -‬کونابه ازدلیا وعالم‬
                                                ‫خوالند ‪.‬‬


‫آندار ‪ ۰‬ممعنی خاك ماشد است چه سار بمعنی‬
‫ماشد هم آهدم است‪-‬و کنابه از چیزی گرد! لود‬
                                                                                  ‫کنهابه از دلیا وعالم باشد ‪.‬‬
 ‫افتاده و درو ش‌ولامرادوخوار‬        ‫ومردم‬   ‫‪-‬‬    ‫هم هت‬          ‫خاکدان غرور» بمسنی خاکدان‬
                                                                               ‫و است که کنانه از دلبا باشد ‪.‬‬
 ‫را کیتزده‌اند‬        ‫وسی‬
                        ‫® ک‬         ‫نزد‬
                                      ‫ا نی‬
                                         ‫ی‬ ‫ور‬
                                            ‫کلیل‬
                                               ‫وذ‬
‫در صف لمال یعنی در کفش کن خانه‬                       ‫که‬

                                         ‫‪‎‬دنیشنب ‪* ٩‬‬                           ‫غروراست که کنابه از دیا باشد ‪۰‬‬


                         ‫)‪ (۱‬خم‪ : ۳‬بذر الخمخم ویترالحنه ‪.‬‬ 
=== ff 161 (printed ~ 701 )
                                                                                            ‫‪o‬‬




‫باشد » و بعربی این بازبرا قثیال کویند بروزن‬           ‫خا‪‎‬‬    ‫شس ‪ ,‬مخفف‬    ‫بر وزن‬      ‫خاکش‪-‬‬
                                  ‫قیفال ‪. ۴‬‬
‫خاك و ]یه کنابه ازجد و فاب‬                                           ‫شبار کرده را بدان هموار کات‪‎‬‬

                                     ‫آدمیزاد باشد ‪.‬‬    ‫=روزن نازیو‪ ,‬تخه‌ی‌است‪‎‬‬
                                                                             ‫ب‬        ‫خا کشو‬
‫خا کی وبزرن یکای » منوب بخاك‬                          ‫صیاه رنگه وریزه کهآفرا ‪ ۲‬کافور درچشم کشند»‪‎‬‬

‫و اشاره بمثلثة خا‪.‬کی امت که‌بزج‬           ‫را گونند‬

‫وله و جدی باشد ‪ -‬و کنابه از مردم‬
                               ‫نب‬‫ثسور‬                 ‫کاشی ‪ -‬بارابم بتحتالی کشید‪. ‎.‬‬
                                                                                   ‫خ‬
  ‫عبتی‬
     ‫الق‬
       ‫‪-‬و‬‫جدم‬
           ‫و فلیل بو‬                   ‫وتاور‬
                                           ‫خحرم‬
                                              ‫بی‬
                                   ‫وقداه‌ای هم هت ‪.‬‬                                 ‫آنرا بشتر دهند ؟‪. ‎‬‬
‫ماکان» مردمان‬          ‫خا کیان؟ = بورزن‬
                                                       ‫خاك مطبق ک‪-‬ایه از کر زمین‬
 ‫وخوار و ذلیل راګوبند ‪.‬‬             ‫رمت‬
                                      ‫حو‬‫یزت‬
                                          ‫ببی ع‬                                                    ‫است‬
‫خا کی کردن ‪ -‬کنابه از افتادکی‬
                                                      ‫خاك معلق ‪ -‬بممنی خامطبق است‪.‬‬
 ‫کردن وبند کی نمودن بکانشداب‪-‬هو‌ازیقراری‬                                           ‫که کر زهین باشد ‪۰‬‬
                                   ‫کردن هم هست ‪۳‬‬
                                                      ‫بفتحنونومیم وسکون‬        ‫‪-‬‬    ‫نماث‬    ‫ځا‬
‫خا کی تهاد » شضصی را گنه که‬
                ‫خلیق و افتاده و متواضع باشد ‪¥.‬‬
                                                      ‫لم کرده ینهان ساز ند‬         ‫چیزی را در لود خاک‬

 ‫خال = بر وزن مال‪ » .‬معروف ات‬                           ‫حر‬
                                                         ‫بخش کنند و‬           ‫و بعد از آن خاك ربادو‬
‫و آن نقطة سیاهی‌باشد که بر روی و اندام‌مردم‬            ‫بخش ازآن کی باشد وآن چیزبکه پنهان‌است‬
  ‫دز_وجنی‬
        ‫نالی‬
           ‫اه ر‬
              ‫‌ک‬‫هبزر‬
                   ‫تا
=== ff 205 (printed ~ 745 )
  ‫خس‌در دهان گرقتن‬                                                                              ‫‪1‬ع‬
                                                                                                 ‫‪۷‬‬


 ‫لباسی باشد که درویشان وفران پوشند وازآن‬              ‫جست ه بفتح اول بروزن مست» ماضی‬
 ‫یشمها وموبها اوبزان باشد‪ - ۷‬وخرقه ایرا لیز‬           ‫حستن و آزرده ساختن باشد بعنی مجروح کرد‬
 ‫کونند که از بارچپای الوان دوخته شده باشد ؛‬            ‫ویند‬ ‫وآزرده ساخت ‪ - ۱‬ورنگ ولون را نکیز‬
                       ‫وفتح اول هم آمده اس‬            ‫ویمعتی تفع وفایده هم‌هست ‪ -‬وبضم اول بمعتی‬
                                                      ‫حامه را لیز‬    ‫و آستن‬        ‫فرار و ارام باشد ‪-‬‬
 ‫خستو نه بضم اول بر وکزلنگونه ‪.‬‬
                                                                                               ‫گفتها ند‬

                                            ‫باشد‬       ‫خستر؟ ‪ -‬برورن کفتر‪,‬حثرات‌الارض‌را‬
 ‫وزن دسته ‪.‬‬   ‫اول بر‬    ‫حسته ‪ -‬بفتح‬
                                                           ‫کوند همچو مورو مار وموش وامثال آن‬
 ‫ثال آن باشدھ ‪-‬‬
              ‫ووزاردم]‬     ‫استخوان‌خرما وش‬
                     ‫لفتوالو‬                          ‫خستی ‪ = ۲‬بپروزن بستن بمعنی‌ مجر وج‬
 ‫ومجروح وزخم خورده وسماررا لیزکو ند ‪ 6‬ہے‬                              ‫کردن ‪ -‬ومجروح شدن باشد ‪.‬‬
    ‫مندخ‪-‬فوف‬
           ‫زومینی که آنرا شریکارده باش‬                ‫حستو ت بفتح اول بروزن بدخو » دانۀ‬
 ‫‪ -‬ونم اول بمعنیهی‬     ‫خاسته وبرخاسته هم هت‬
                                                      ‫میوهارا کوبند همچودانةٌ زآرلدو وشفتالو وخرما‬
                           ‫وبنورة دیوار باشد ‪.‬‬
                                                      ‫و مانند آن ‪ - ۴‬و م اول ناممکی از اکابر‬
 ‫حسته نك = بابای ابجد بروزن هرزه‬                      ‫وبزرکان چن است ‪ -‬واقرار واعتراف کننده را‬
‫لیزگفته‌اند(‪ -)۱‬وبمعنی‌جانورخز ندحهمبذظر آ مده خند ‪ .‬پارچه‌ای کروایند کهچون دستی بایایی‬
 ‫شکته باشد بدان بندند ‪ -‬و کی را تیز گوبند‬                                                      ‫است ® ‪.‬‬
 ‫که زخم را و(‪ )۲‬دست ویای شکستهرا می‌بندد‪-‬‬             ‫خستوان‪ = 1‬یبنرماووزلن‌استخوان »‬
 ‫وهرچیز که انرابرزخ‌بندند خواه پلرچه باشد‬              ‫افرار و اعتراف کنندکان و معترف شکدانرا‬
                                     ‫خواه هر هم‪.‬‬                                     ‫گویند ‪.‬‬
  ‫ان گر فتی‪ -‬بسنی‌خس‬
                   ‫خدسهدر‬                              ‫حستو انه = پم اول‌بروزن خرواله»‬
```


## [2026-09-14T03:12:09.750Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(150,163):\n    p=pages[i]\n    hits=[w for w in ('خاستن','خاسته','برخاستن','خیزیدن','خاست') if w in p]\n    print(i, i+540, hits, ' | head:', p.strip().split('\\n')[0][:60])\nEOF"
}
```


### [2026-09-14T03:12:10.822Z] TOOL RESULT

```
150 690 []  | head: ‫‪~Y‬‏‬                                                     
151 691 []  | head: ‫بیان دوازدهم‬
152 692 []  | head: ‫‪4‬‬                                                       
153 693 []  | head: ‫گفتار هشم‬
154 694 []  | head: ‫‪-61‬‬                                                     
155 695 []  | head: ‫جار خار‬                                                   
156 696 []  | head: ‫ره‬                                                        
157 697 []  | head: ‫‪-4۹-‬‬
158 698 ['خاستن', 'برخاستن', 'خاست']  | head: ‫‪ ۵ 64‬وا‬   ‫ست‬
159 699 []  | head: ‫خاکبیز‬                                                    
160 700 []  | head: ‫پا‬     ‫‪۵‬‬
161 701 []  | head: ‫‪o‬‬
162 702 []  | head: ‫‪۷۰۵ -‬‬
```


## [2026-09-14T03:12:16.385Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[158]\nimport re\nfor ln in p.split('\\n'):\n    if any(w in ln for w in ('خاستن','خاست','برخاست','خیز')):\n        print(repr(ln.strip()[:200]))\nEOF"
}
```


### [2026-09-14T03:12:17.464Z] TOOL RESULT

```
'\u202b\u202a, ۴۳\u202cافنانی أقا\u202a ( 21\u202cبلند شدن» برخاستن) «هویشمان\u202a »۲۱14\u202cر\u202c'
```


## [2026-09-14T03:12:21.303Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[158])\nEOF"
}
```


### [2026-09-14T03:12:22.347Z] TOOL RESULT

```
  ‫‪ ۵ 64‬وا‬   ‫ست‬




‫از دم مقرض استادان خیاط ویوستین دوز و ازدم‬                ‫خاشاك ‪ ۱‬ه بروزن چالاك‪.‬ساق علف‪.‬‬
                              ‫تشه درود گران بریزد ‪۰‬‬      ‫و چوب ریزه های باريك ‪ -‬و خار وخس با خاك‬
‫= بفتح‌خای‌نقطه‌دار‬       ‫خماش‬
                             ‫خاش و‬                                                  ‫‪.‬‬    ‫ند‬
                                                                                          ‫وتهیرا‬
                                                                                               ‫گیش‬
                                                                                                 ‫آم‬
‫نمعنی‌خاش‬         ‫فرشت زده»‬   ‫وشن‬    ‫وميم بالف کشده‬           ‫که‬ ‫افف‬
                                                                   ‫»مخ‬
                                                                     ‫اش‬  ‫خحاك‬
                                                                            ‫خاشك ‪ .‬بنت‬
‫و خار و ریز های دم‬            ‫که خس‬    ‫است ؟‬   ‫خش‬   ‫و‬          ‫و‬
                                                              ‫مشدع‪-‬نی‬
                                                                    ‫است که خس وخار وامثال آبن با‬
‫مقراض وتیشه وچیزهای افکندنی وبکار نیامدنی‬                          ‫ورد ورهز وبیز همآ مده است ‪.‬‬
                                                                                             ‫خرد ه‬
                                                          ‫خاشکدان » بادالبالف کنیده وبنون‬
‫خاشه ه بروزن ماشه ‪.‬خی وخاشاکک‬                            ‫‪۰‬ندوقجۀ زنانرا گویند که‬
                                                                               ‫زده بروزن‌ناچبان ص‬
‫رویزهای چوب وسر کین وامثال آنرا گونند که‬                  ‫‪-‬‬   ‫هناهند‬   ‫ز‬
                                                                       ‫چردىو‬
                                                                           ‫در آن ریز وییز وخرد وم‬
                                                          ‫ودخل دان استادان وقنااللبا آوشپز و امثالآنرا‬
‫همه بهم (‪ )۲‬آمیختم باشد ‪ - ۴‬و بمعنی رشك‬
                                                         ‫فز کفته اند ‪ ,‬وآن ظرفی باشد که قیمتآ نچه‬
                                                          ‫قروخته شود در گآذنارند ‪ -‬وصندوقی را ندز‬
 ‫خاصگی " » بنتح‌صاد بی‌قطه وکر‬
                                                                          ‫کویند که نان درآن نهند ‪.‬‬

                                                        ‫خاش و خش ‪ ۰‬ب يانش لیفنقترازشتوتابعبر‬
‫کنیز که صورنی‬          ‫سکون نحتانی »‬    ‫کاف فارسی و‬

‫ونابه از هر چیز نفیس هم‬
                      ‫را (‪ )۳‬کوبند ‪ -‬ک‬
‫حت اموقر پادشاه > خوزینه وار را نز‬                                   ‫وزن ومی خار وخ باشد » وا‬
                                         ‫‪۴.‬‬
                                          ‫کفته‌انن ‪#‬‬      ‫وش (‪ )۱‬ریزها را نگیوزنند؟ که‬‫ختم‪-‬ا‬‫اس‬

            ‫‏)‪ (e‬خم‪ : ۳‬خوش صورترا‪.‬‬               ‫)<( خم‪ : ۳‬باهم ‪:‬‬          ‫وقماش‪.‬‬   ‫(م) چش‪:‬‬

  ‫کی ( سمرقندی ) گوبد ‪:‬‬             ‫رك‪ :‬خاش» «حخاشالك» رزه ها مود از آن که وعیره » رود‬    ‫‪۱‬‬

            ‫‪۱۰۷‬‬     ‫حرهٌ‬
                       ‫صهف د‬
                           ‫ش‬
    ‫دهچ‌ناند‬
           ‫‪ #‬خاقان ‪ -‬ازترکی « خاقان ‪٩‬‏ بمعنی شاهنشاه " عنوانی است که بدلااطن‬
  ‫رك ‪ :‬دزی‬
         ‫دنتایی ‪ ۶ » ۲۱۳‬الادراك للسارالاتراك ‪ .‬این‌مپناص ‪ › ۵۸۱‬معرب آن یز خاقان ‪( .‬‬
                                                                                  ‫ج‬
  ‫فلتنمهبتان چن وطراز ‪.‬‬                   ‫دخت خافان بنام فما ناز‬            ‫‪۹٩۸۳‬‏ * تقس > ‪:‬‬   ‫ج ‪ ۱‬ص‬
  ‫ظامی کنجوی‪ « .‬کنجینه ‪.‌ ۸4‬‬                                                  ‫ورك ‪ :‬اسفا ‪: ٩۱‬‏ ‪ ۲‬ص ‪۷۰‬‬
  ‫‪ #‬خحاقالی ‪ -‬منوب بخاقان ‪ -‬تخلص افضل الدین بدیل‌ین على خافانی شروانی ( تولد‬
   ‫‪-‬ات حدود ‪)0۹۵‬؛ شاعر قصیده سرای ممروف قرن ششم » تولد وی درشروان‬
                                                                ‫وف‬‫حدود ‪ ۶۲۵‬ه‬
  ‫ووفات او در تبریز انفاق افتاد و در مقبرةالشمرا شدمرال شهرمزبور در کوی سرخاب مدفون شد ‪.‬‬
  ‫وی بدربار خاقان اکبر منوچهربن فربدون شروانشاه اختصاص داشت و نخلص او از عنوان همین‬
  ‫شاه مأخوذاست * وی دارای بیانی امتواروبا طمطراق است وکتیربات مخصوص بخود دارد وصنایم‬
  ‫و سخنوران ‪.‬‬           ‫»خن‬
                          ‫دتر شفق ص ‪ ۵۶۲‬بیمد م‬
                                             ‫بدیعی بکار میبرد ‪ .‬رك ‪ :‬تاریخ ادییات ابران ‪ .‬ک‬
                                                                        ‫فروزانقر ج ‪ ۲‬ص ‪ ۶۶۳‬ببعد ‪.‬‬

                                                                                    ‫هه از صفحة ‪۹۹۹٩‬‏‬
 ‫خ‪#‬استی ‪ -‬فتح‌چپارم؛ پهلوی‪*72/521‬روابات‌بهلوی* ‪.۷‬پهلوی تورقان‪.8 »02)52‬‬
 ‫ه«عاعق‪ 4 - 721۵۵2 ۰ ۵ - :‬یز ‪ ,‬پهلوی ساسانی ‪ . 0251262‬سغدی ‪« 2 - 126‬نبر که‬
   ‫وك ‪ :‬اسفاا‪ ۲:‬ص‪»4۳۱۰۹۰۲‬‬
                        ‫‪, ۴۳‬افنانی أقا‪ ( 21‬بلند شدن» برخاستن) «هویشمان‪ »۲۱14‬ر‬
                                                    ‫‪ ۷۲۲ ۰ ۹‬؛ بلندشدن ‏ قدام‪.‬‬
```


## [2026-09-14T03:12:46.699Z] TOOL CALL #35: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py; echo ---; sed -n '1,40p' tools/verify_check.py"
}
```


### [2026-09-14T03:12:46.752Z] TOOL RESULT

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
---
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
```


## [2026-09-14T03:12:48.592Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '82270,82285p' MON_part1.txt\necho \"=== page tags in MON_part1 ===\"\ngrep -n \"pdf page\" MON_part1.txt | head -3\npython3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('ff before 82279:', '\\n'.join(lines[:82279]).count('\\f'), 'total ff', t.count('\\f'))\nEOF"
}
```


### [2026-09-14T03:12:49.825Z] TOOL RESULT

```
سیسمونی: آ-02صوعلو (عم.) لوازم کودک 
نوزاد (لباس و غیره) که اقوام مادر به رسم 
تحفه فر ستند. 
سیطر ۵ (تد. 52۷]۱2۲2)5672۲6 [ع. سیطر ۳ 
(مصل.) غلبه یافتن» تسلط یافتن» چیره 
کشتن . (امص ۰( غلبه» تسلط» چیر گی. 
سیغ: * و [- هس ] رف نک نغز»ه خوب. 
سیف: 2256۵ [ع.] () شمشیر) ج. 
سیوف. 
سیفلیس: ۰18 () (پز.) مرضی عفونی و 
ساری که به ارث بطور مادرزادی به افراد 
نتقل می‌شود. عامل این ناخوشی باسیلی 
است مارپیچی بنام ترپونم پال. این مرضص 
بطور مستقیم از افرادمبتلی به فراد سالمقابل 
سیفو ر؛ .)22۷60۲ (ا.) بافتة اسر شمی 
لطیف (مانند دیا و اطلس). 
=== page tags in MON_part1 ===
ff before 82279: 0 total ff 0
```


## [2026-09-14T03:12:59.150Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/suH-\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C4%ABka\" \\\n \"https://www.etymonline.com/word/hog\" \\\n \"https://www.etymonline.com/word/soil\" \\\n \"https://www.etymonline.com/word/syphilis\" \\\n \"https://www.etymonline.com/word/hyena\" \\\n \"https://www.etymonline.com/word/swine\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 487, roots Su 2 / Suig\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T03:13:02.847Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/537c40faacd4b172.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87e98b3ce49cadc2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8fa65b77cf244cee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fba84a50bf7592b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/965b0a4c9aecd452.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/929b3cc8044d4049.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c94c1b33a911bb63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed64315852ce598d.txt
```


## [2026-09-14T03:13:05.139Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 537c40faacd4b172 87e98b3ce49cadc2 8fa65b77cf244cee; do echo \"##### $f\"; head -c 2500 $f.txt; echo; done"
}
```


### [2026-09-14T03:13:06.105Z] TOOL RESULT

```
##### 537c40faacd4b172
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/suH-
FETCHED: 2026-09-14T03:13:01Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/suH- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/suH- - Wiktionary, the free dictionary 

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
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Reconstruction notes 

 1.2.2 
 Inflection 

 1.2.3 
 Alternative reconstructions 

 1.2.4 
 Derived terms 

 1.2.5 
 Descendants 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ suH- 

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

 Etymology
 [ edit ] 

 Has been suggested to derive from *sewH- ( “ to give birth ” ) if the original meaning was “sow”. [ 1 ] [ 2 ] 

 Possibly related to Akkadian 𒊺𒄷𒌑 ( še-hu-u₂ , “ pig ” ) (Old Babylonian šahû ), which may be an Indo-European borrowing, as well as Sumerian 𒋚 ( šah ) , 𒂄 ( šaḫ ) and 𒍢𒄴 ( ze₂-eh ) . [ 3 ] [ 4 ] 

 Noun
 [ edit ] 

 *suH- 

 pig , hog , swine 

 Reconstruction notes
 [ edit ] 

 It is conspicuous that the root only occurs in the zero-grade.

 Descendants in several branches, including at least Germanic *sugō and Celtic *sukkos and their descendants, show no trace of the laryngeal where it would be expected, while these two also show a suffix with a velar stop. [ 5 ] [ 6 ] There are several potential explanations for
##### 87e98b3ce49cadc2
URL: https://en.wiktionary.org/wiki/%D8%AE%D9%88%DA%A9
FETCHED: 2026-09-14T02:07:08Z
STATUS: 200
TITLE: خوک - Wiktionary, the free dictionary

خوک - Wiktionary, the free dictionary 

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
 Persian 

 Toggle Persian subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Alternative forms 

 1.3.2 
 Derived terms 

 1.3.3 
 Descendants 

 1.4 
 References 

 2 
 Urdu 

 Toggle Urdu subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 Toggle the table of contents 

 خوک 

 22 languages 

 Azərbaycanca 
 বাংলা 
 فارسی 
 Na Vosa Vakaviti 
 Français 
 Hrvatski 
 Magyar 
 Bahasa Indonesia 
 日本語 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Lietuvių 
 Malagasy 
 Polski 
 Română 
 Русский 
 Sängö 
 Shqip 
 ไทย 
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

 See also: جوگ , جوک , and چوک 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: خوک 

 Wikipedia fa 

 Etymology
 [ edit ] 

 From Middle Persian [Book Pahlavi needed] ( HZWLYA ) / [Book Pahlavi needed] ( hwk' /⁠hūg⁠/ ) , from Proto-Iranian *huHkáh , from Proto-Indo-Iranian *suH- , from Proto-Indo-European *suh₂kéh₂ , from *suH- .
Possibly cognate with English hog .

 Pronunciation
 [ edit ] 

 Dari

 خوک 

 Iranian Persian

 Tajik

 хук 

 ( Classical Persian ) IPA ( key ) : /ˈxuːk/ , /ˈxuːɡ/ 

 ( Dari, formal ) IPA ( key ) : [xuːk] 

 ( Dari, formal ) IPA ( key ) : [xuːk] 
 ( Kabuli ) IPA ( key ) : [xuːk] 

 ( Hazaragi ) IPA ( key ) : [xuk] 

 ( Iran, formal ) IPA ( key ) : [xuːkʰʲ] 

 ( Tajik, formal ) IPA ( key ) : [χuk] 

 Rhymes: -uːk , -uːɡ 

 Readings

 Class
##### 8fa65b77cf244cee
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C4%ABka
FETCHED: 2026-09-14T03:13:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-14T03:13:12.101Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in fba84a50bf7592b3 965b0a4c9aecd452 929b3cc8044d4049 c94c1b33a911bb63 ed64315852ce598d; do echo \"##### $f\"; grep -A25 -m1 \"^ *hog\\|^ *soil\\|^ *syphilis\\|^ *hyena\\|^ *swine\" $f.txt | head -40; echo; done"
}
```


### [2026-09-14T03:13:13.240Z] TOOL RESULT

```
##### fba84a50bf7592b3
 hog (n.) 

 mid-14c., hogge , but probably in Old English (implied late 12c. in hogaster ), "a swine," especially a castrated male, "swine reared for slaughter" (usually about a year old), also used by stockmen for "young sheep before the first shearing" (early 14c.) and for "horse older than one year," suggesting the original sense had to do with age, not type of animal. Possibility of British Celtic origin [Watkins, etc.] is regarded by OED as "improbable."

 Extended to the wild boar by late 15c. As a term of opprobrium for a greedy or gluttonous person, c. 1400. Meaning "Harley-Davidson motorcycle" is attested from 1967. Road hog is attested from 1886, hence hog "rude person heedless of the convenience or safety of others" (1906). To go hog-wild is American English from 1904. Hog in armor "awkward or clumsy person in ill-fitting attire" is from 1650s (later used of the armadillo).

 Phrase go the whole hog (1828, American English) is sometimes said to be from the butcher shop option of buying the whole slaughtered animal (at a discount) rather than just the choice bits. But it is perhaps rather from the allegorical story (recorded in English from 1779) of Muslim sophists, forbidden by their faith from eating a certain unnamed part of the hog, who debated which part was intended and in the end managed to exempt the whole of it from the prohibition.

 Had he the sinful part express'd,

 They might, with safety, eat the rest.

 But for one piece, they thought it hard,

 From the whole hog to be debarr'd

 And set their wits to work, to find

 What joint the prophet had in mind.

 [Cowper, "The Love of the World Reproved"]
 also from mid-14c. 


##### 965b0a4c9aecd452
 soil (v.) 

 early 13c., "to defile or pollute with sin," from Old French soillier "to splatter with mud, to foul or make dirty," originally "to wallow" (12c., Modern French souillier ), from souil "tub, wild boar's wallow, pigsty," which is from Latin solium "tub for bathing; seat" (from PIE root *sed- (1) "to sit") or else from Latin suculus "little pig," from sus "pig." The literal meaning "to make dirty on the surface, begrime" is attested from c. 1300 in English. Related: Soiled ; soiling .
 also from early 13c. 


##### 929b3cc8044d4049
 syphilis (n.) 

 infectious venereal disease, 1718, Modern Latin, originally from the title of a poem, "Syphilis, sive Morbus Gallicus" "Syphilis, or the French Disease," published 1530, by Veronese doctor Girolamo Fracastoro (1483-1553), which tells the tale of the shepherd Syphilus , supposed to be the first sufferer from the disease. Fracastoro first used the word as a generic term for the disease in his 1546 treatise "De Contagione." 

 Why he chose the name and what it meant to him are unknown; it may be intended as Latinized Greek for "Pig-lover" (with Latin sus "pig"). That and derivation from syn- "with" + philos "loving" form "the usual conjectures" [Century Dictionary], but there was as well a Sipylus , a son of Niobe, in Ovid.
 also from 1718 

 Entries linking to syphilis 

 syphilitic (adj.) 

 "pertaining to or of the nature of syphilis," 1786, from Modern Latin syphiliticus , from syphilis (see syphilis ). As a noun from 1881, "person infected with syphilis."

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 Neapolitan 

 In early 18c., Neapolitan consolation meant "syphilis."...

 sarsaparilla 

 .-17c. the dried roots were held to be efficient in treatment of syphilis....

 dose 

##### c94c1b33a911bb63
 hyena (n.) 

 mid-14c., from Old French hiene , from Latin hyaena , from Greek hyaina "hyena," apparently a fem. formation from hys "pig," from PIE *su- "swine" (see sow (n.)). With fem. suffix -aina . So called for its bristles. Applied to cruel, treacherous, and greedy persons at least since 1670s. Adjectival forms that have been attempted in English include hyenaish , hyenaesque , hyenic , hyenine , hyenoid .
 also from mid-14c. 

 Entries linking to hyena 

 sow (n.) 

 Middle English soue , from Old English sugu , su "female of the swine, adult female hog," from Proto-Germanic *su- (source also of Old Saxon, Old High German su , German Sau , Dutch zeug , Old Norse syr ).

 This is held to be from PIE root *su- (source also of Sanskrit sukarah "wild boar, swine;" Avestan hu "wild boar;" Greek hys "swine;" Latin sus "swine," swinus "pertaining to swine;" Old Church Slavonic svinija "swine;" Lettish sivens "young pig;" Welsh hucc , Irish suig "swine; Old Irish socc "snout, plowshare"). The root is possibly imitative of pig noise, a notion reinforced by the fact that Sanskrit sukharah means "maker of (the sound) 'su.' "

 Related to swine . As a term of abuse for a woman, attested from c. 1500. Sowbug "hog-louse, pill-bug" is from 1750; sow in reference to any terrestrial isopod that can roll itself into a ball is from 15c. Also sow-lice (1650s).

 hyaena (n.) 

 see hyena .

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 catfish 

 The name is based on glanos "hyena," the fish being "thus called because of its voracity and the sound it makes" [Beekes]...

##### ed64315852ce598d
 swine (n.) 

 Old English swin "domestic pig, hog, sow; wild boar" (commonly used in a plural sense, of such animals collectively), from Proto-Germanic *sweina- (source also of Old Saxon, Old Frisian Middle Low German, Old High German swin , Middle Dutch swijn , Dutch zwijn , German Schwein , Old Norse, Swedish, Danish svin ), neuter adjective (with suffix *-ino- ). This is from PIE *su- "pig" (see sow (n.)).

 The native word, it has been largely ousted by pig (n.1). Applied to persons from late 14c., "mean or degraded, sensual and coarse." The phrase pearls before swine (mid-14c.) is from Matthew vii.6; an early English formation of it was:

 Ne ge ne wurpen eowre meregrotu toforan eowrum swynon. [c. 1000] 

 The Latin word in the Gospel verse was confused in French with marguerite "daisy" (the "pearl" of the field), and in Dutch the expression became "roses before swine." Swine-drunk is from 1590s (Nashe). Swine-flu is attested from 1921. Earlier terms for infectious pig diseases include swine-plague (1891); swine-pox was originally "chicken pox" (1520s); it is attested from 1764 as a disease of swine.

 Entries linking to swine 

 pig (n.1) 

 Middle English pigge "a young pig" (mid-13c., late 12c. as a surname), probably from Old English *picg , found in compounds, but, like dog , its further etymology unknown. The older general word for adults was swine , if female, sow , if male, boar . Apparently related to Low German bigge , Dutch big ("but the phonology is difficult" -- OED).

 By early 14c. pig was used of a swine or hog regardless of age or sex. Applied to persons, usually in contempt, since 1540s; the derogatory meaning "police officer" has been in underworld slang at least since 1811.

 The pigs frisked my panney, and nailed my screws; the officers searched my house, and seized my picklock keys. ["Dictionary of Buckish Slang, University Wit and Pickpocket Eloquence," London, 1811]

 Another Old English word for the animal was fearh , which is related to furh  "furrow," from PIE *perk- "dig, furrow" (source also of Latin porcus "pig," see pork ). "This reflects a widespread IE tendency to name animals from typical attributes or activities" [Lass].

 Synonyms grunter (1640s), porker (1650s) are from sailors' and fishermen's euphemistic avoidance of uttering the word pig at sea, a superstition perhaps based on the fate of the Gadarene swine, who drowned. The image of a pig in a poke is attested from late 14c. (see poke (n.1)). Flying pigs as a type of something unreal is from 1610s.

 sow (n.)
```


## [2026-09-14T03:13:27.984Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT erhebe dich ===\"\ngrep -n -i \"erhebe dich\\|aufstehen\\|sich erheben\" BRT.txt | head -20\necho \"=== BRT xaez variants ===\"\ngrep -n \"aezaiiuha\\|xaeza\\|haeza\\|zaiiuha\" BRT.txt | head -10\necho \"=== POK sueig ===\"\ngrep -n -i \"sueig\\|su̯eig\\|sweig\" POK_full.txt | head -10\necho \"=== WLD band3 sueig ===\"\ngrep -n -i \"sueig\\|swicken\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T03:13:28.088Z] TOOL RESULT

```
=== BRT erhebe dich ===
26681:mit  us'^  'aufstehen,  sich  erheben,  —  auf- richten von  — '  {kaca  mit  AbL):  us  a%at kiftat  satavalsS  ,  .  arayaiahat  kaca  .  .  Yt "32;  —  uakistat  sara%uitrö  fralosat  ..Y . '9-4!  —  usMstat  gaus  V.  2. 10  PUZ.;  — utihiStai  vohu  manS  kaca  gatvö  zaranyS.- kirats   V.  j^.  3 1 ;   —  pasla  yat   us?Aiität
=== BRT xaez variants ===
22071:•  j.  vaeÄya-,  vaedya-  n.  'Kenntnis, Wissen',  mit  Akk.  oder  Gen.  obj.:  °%Tm mq%rahe  spitttake  Y.  22.  25;  —  -%lm ma^ntn  spintim  Y,  25. 6;  —  maziiläis 'dyäil  damayh  mäedayasnöis  "V.ij.y,  — mastim  spänS  ^iilmca  Yt,/o.  33;  —  sraostm .  .  ye^he  .  .  haeza^waca  ""oyä^a  (IS.)  Y. 57.23;  —  *'Um  F.<V.  [¥.5.27:  lies vaitya.paile.'\
29995:Pü. ;  US  est  kam  äydi  (aSlmp.).  —  ')  Man  er- wartete nach  dem  folgenden  päirLhaezatiuha und  nach  Pü.  eine  2SIM.  vy  yal-  mit  hant', ob  hqm.yoflaaiiha  (lu  yailo;  Praes.  6)?  Un- klare Slelle.
=== POK sueig ===
83428:Note: extended sueizd-, Italian and Germanic sueighl- 
84401:sueig-: QermaxWc also "nachgeben, slacken ' (from suh " dwindle ' derive ) "(cunning) 
=== WLD band3 sueig ===
```


## [2026-09-14T03:13:35.266Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29960,30020p' BRT.txt"
}
```


### [2026-09-14T03:13:35.316Z] TOOL RESULT

```
i8o9
h^m
hi^.var«tay-
iSio
j.  horäla  F.  j  a:  liei  aorala.  1
•  j.  hi^m  i)  Adv.  a)  Praev,  S.  unter *ham.  [Yt  /o,  125:  lies  hqmJvqmca; —  V.  5.  j  7 :  lies  Aam.näiri'.]
•  j.  ba^mö-näfa-  Adj.:  s.  unter  hamUt'.
•  j.  h^mina-  i)  Adj.  'sommerlich':  dasa avä^ra  mänkd  sayana  dva  'na  (ND.)/ hapta  hittti  °nS  (NP.)  '*  manka  panca zayüna  askan  (Sp.  1553  u.)  V.  ;.  3  und 3PiiZ.  a)  n.  'sommerliche  Zeil':  hama^a (sd.)  ,  ,  'mirumca  sayamm^a   Y.  6j,  5.
Ableil.  aus  'Aam-  {mit  Vj-ddhih,  s.  %  apff.  3, /gS).  -  Pü.  (10  V.  /):  ^Jm™^!?),  (zu  Y.  ÖJ): /O  haniin.  —  ')  Unlhem.
•  j.  ^ham.ivä-  f.  Name  eines  Teils  vom  Ge- schirr des  mit  Pferden  bespannten  Wagens, vli  'Deichsel':  äal  ti  (näml.  aurvants)  vXspa /rü.yuxta  'vqmca  simqmca  simöihrqmca dirita  huhr^la  ^upairi.späta  aka  bastom "und  die  (Renner)  sind  alle  angeschirrt an  die  Deichsel  und  den  Halsring  und das  Joch,  die  mit  dem  aufgespaltenen wohlgefertigten  üb  ergesteckten  Zapfen  zu- sammengehalten sind"  Yt.  jo.  ia5(?).
Et.  ?  —  NA,  trennt.
).  hifoiM  V.  7.  59:  lies  hamia.
•  j.  ham.tapta-  Adj.  (fem.  ■«-)'>,  PPfP.:
S.  top:
■)  S.  tap.  No.  a.
•  j.  ham.patana-  Adj.  'comes,  Gefährte', von  i/an^schen  Wesen:  hau  datvanqm kandvatfnB  .  .  'nd  V.  7.  54;  53.
Zum  V.  fal:  —  Pü. ;    hampallinih.
•  j.  (rfan7ö.)hiim.par3t«m  AbsoL  'mit, bei  (lang  dauernder)  Zurateziehung',  mit  | Akk.:  . .  mqm  narS  paskät  yazmie  ahunm  1 raazdatn     darrfSyaSt^mi^A^la    'tfmca    H.  I
2.  14.'  j
Abgekürit  für  dan-jö.yastimia  ilarriii.lu\m,far- 1 iUmia,  vgl.  unter  [^ir?ü^ao%ra-  und  s.  Pü- ' Erl.  —  f  ü. ;  pa  an  i  öhrtnaiai  dir  yaöinlh  u hanipursatih ,  erl. ;  der  iat»än  iasän  ihrmazd Tai  ya:ihi  u  hampursakih_  i  frSrön  tarl  "lange Zeit  machen  sie  dem  Ohrm.  Veiehrung  und BefiüEung".
•  j.  ham.bar^tar-  vaDhva,m  m.  EN,  eines
Gläubigen :  "^rff  vanhvam  laxmahe  asacitS
Eig. 'Ziisammenbiinger  von  Gülern',  vgl.  hm.- kqm.bitil-.  —  Tjoa  V.  'bar-;  ai.  bhartar-ai. — Vgl.  lu  barAri.
•  j.  ham.barstay-  f.  'Zusammentragen, Sammeln':  altavat  <l/r>,saokanqm  'ia(LS.)'> ääitlm  gätüm  avi  ava.baraiti  V.  i¥.  85.
ooss.  ämbird  'Sammlung';  bX,  lU-iambA^lay-  f.;
t.  No.  ~  Pü.!  fehiL  —  ')  Sva.  colligendo; S.  lAusdr.  ai.  smambh^lä  Iva  säm  iharämi  TS. (bei  ZubatV  IF.^.  134,  der  freilieb  die  Form anders  fasst;  zum  Aliient  s.  Reutek  KZ.  j/. 6a6)  und  zu  hdi>ra.jiUay:
•  j.  ha,m.bBr«9'a-  n.  'Versammlung':  cim ''ha  (AP.)  hqmMrayama  (sd.)  ..arszürahe paiti  kam3r3%3m  V, /p.  44;45.
Pü.;  fa  hambariinih.
•  j.  ^h^m.bara^Tvä-  f.  'Fülle,  Vollemte': vispä  :^ar7nUs  para.barqn  '%wqm  pars yavahe  ".  .  abgesehen  von  der  Vollemte des  Getreides"  V.;.  27.
Zum  V.  'bar:  —  Pü,:  iamtariimA.
•  j.  ham.nasav-  Adj.  (auch  fem.)  'mit der  Nasav  (Leichenhexe)  in  Verbindung stehend,  von  ihr  berührt,  befleckt"':  yöi 'süm  (ASf.)  ..tanüm  yaoidai^yqn  V._9.i.
Pu. :  ic  hamnasus  ast,  erl.:  kamrhnatük.  — ')  Vgl.  Jräjtasav:
•  j.  *h^in.niiiri-*'  Adj.  'mit  der  Frau  zu- sammen': anya  dva  vä  nara  .  .  panca vä  .  .  satpm  vä  'rinam  (nämL  naratn) V.5-27.
Pü. :  pa  kammartik,  erl. :  pa  hamiarpak'ih.  — I)  NA.  trennt.
•  j.  usihista  "ham.yaetanhö ''  yaommca avi  tqmla  .  .  usihista  päiriJtaiiamtha yehe  .  .  V.  21.  4.
Pü. ;  US  est  kam  äydi  (aSlmp.).  —  ')  Man  er- wartete nach  dem  folgenden  päirLhaezatiuha und  nach  Pü.  eine  2SIM.  vy  yal-  mit  hant', ob  hqm.yoflaaiiha  (lu  yailo;  Praes.  6)?  Un- klare Slelle.
•  j,  ham.STJta  Inf,  'zu  verwenden,  zu  ge- brauchen', praedikativ  gebraucht:  kai  tä vastra  h°  pasca  yaaldäiti  frasnäiti  (sd.) tae%r€  v5  . .  "sind  die  Kleider  zu  ge- brauchen,.  für  (von)  einen  Z. ..?"  V.5. 57;
, —  niit  tu  vastra  &'  V.  j,  58.
Zum  \.  ydv-.  —  \^.  yülS.  —  Pü. :  kt  eiän vastrak  S  kam  iySieli  mä  dlän  vas/rai  S  kam ayözand.
•  j.  ham.vaoray-  Adj.  'mit  dem  Rahm, nicht  entrahmt':  payanhqm  . , 'vagirinqm
.us.vaairinam  V.  5.  5  a, Pü.:  unklar,
I  •  j.  ham.varatay-,  ham-varetay-**  f, •Wehrhaftigkeit,  Tapfeikeit",  stets  mit nairya-    Adj.    verbunden:     däyä    mt  .  .
'•  nairyqm   .  .  •rsitTm    Y.  62.  5.  A)    als
;  Gottheit:  asii  vanuhi  par>ndica  . .  uyraca naire  'nids  Yt./0.ä6;  ij.a,  JJ.39;  — hahra  nairya  'rata  (LS.)  "zusammen  mit
I  der  mannhaften  Tapferkeit"  Yt.  io.  7 1 ;  —
dby  Google
I8il
hain.var9itivant-
uyranqm    aojistS  . .  nairyayät  parS  (sd.)  |
'ntSii  ytip.  38'';  —  vätahe  .  .  nairyayä
'nidis   S./.aa;  —  tiairyqm  'rjt/m  yaza-
maide  Yt  ig.  39,  S.  2.  22,  Vr.  7. 3.
Ableit.;    1.  auch   nairyqm.liifitt.vär>livani:   —
Zum  V.  tvar-.    —    np.  TgL  gMrd  'Held'.    —
Pö. :  haut  m  1 1  ap  n  k  ih,  er). ;  palütih  1  fa  kSt
»  dälaitän.  —    '}  Nor  in  'v^ntöif  Yt  ig.  38.
•  J,  h^ni.var«iti'vaiit-  Adj.  (fem.  °vaitl-)
'wehrhaft,  tapfer*:  sraosahe  asyehe  . .  tax-
mähe  'vats  Y.57.  33;  — fravaiayD  ,,yä
taxmä  •vaitl!  Vt.  13.  33.
unter    ham.-
```


## [2026-09-14T03:13:36.280Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '84385,84425p' POK_full.txt"
}
```


### [2026-09-14T03:13:36.451Z] TOOL RESULT

```
sve/mn. 'GetiJmmel, tumult', si/e//775'umherziehen'. Middle High German swe/mm. 'das 
Schweben, Schweifen, Schwingen', SM/e//77e/7'sichschwingen, waver'; Norwegian si///n. 
"Spirale; the frizzy Samenbeutel dorschartigerfish'; Low German sty/?'Schwung, gyration, 
Bummein', sw/ren^s\c\r\ schwingend bewegen, umherfliegen, in Saus and Braus leben'. 

sue/b-: Avestan xsvaewayat-astra-^ 6\e Peitsche schwingend', A-siz/Vwa- "agile'; Gothic 
midJa-sweipains^S\v\\^\\}\! (actually "Fegung the center'); Old Icelandic si/e/p5 "throw, 
umhijllen'. Old English 5M/apa/7 "swing, sweep, wash away, drive, push'. Old Saxon swep 
"fegte fort'. Old High German SM/e/>^/7 "swing, schweifen, quarrel', SM/e//"Umschwung, tail' 
= Old Icelandic si/e'/p/'"band, strap, Schlingung, curled hair'. Old Icelandic si//pa"lash, 
scourge, bullwhip, horsewhip; spur'. 

sue/c/-:\n Lithuanian svfesti, Latvian si//es/ "throw', frequentative Lithuanian svaidyti, 
Latvian si/a/(y/7"wiederholt toss, fling'; whether Latvian si/a/Ty/? "anoint, smear' (under under 
sueid-) here? 

sueig-: QermaxWc also "nachgeben, slacken ' (from suh " dwindle ' derive ) "(cunning) 
etwas drehen, dodge, deception ' : Old High German swThhon, Old English swTcian 
"schweifen, wander, cheat, deceive'. Old Icelandic svTkva sykva {u-'^resev\{), si//7^a "cheat, 
deceive, betray ', Old English swTcan^ abandon, cheat, deceive', poet. " leave, depart, 
wander'. Old Saxon swTan6s. "languish'; Old High German sbv/77/75/7 "languish, slacken, 
abandon ', Middle High German swTchm. "Zeitlauf, 5-5ty/C'/7"heimlicher Fortgang', 
SM/e/ic/7e/7 "languish'; Old Icelandic sviku. " betrayal, deceit'. Old English swicu. ds.. Old 
High German biswihrw. ds.; 

Lithuanian svaTgtr dizziness, giddiness; swindle bekommen', svaigineti^ giddy 
umherwanken', russ. 5i//g5/'"herumtreiben'; 

Tocharian A M/5M/e/r£/"gelogen', B waike^\\Q, falsity'. 

sueik-:Q\^ Icelandic si/e/^/'"pliable', m. "flexible stalk', Swedish dial. svTga, sveg 
"sichbiegen', Kaus. Old Icelandic si/e/5y5"bend'. Pass, sv/gna^be bent, bow, nachgeben', 
sv/'g/m. "flexible stalk'; Old High German swe/ga^catt\e shed' (*netting). 

sue/p-:0\6 Icelandic si//7^ "swing, turn, umherschweifen, schweben'. Old English swTfan 
"turn, sweep, wash away (engl. SM///?"quick, fast'), wave'. Old Icelandic sue/f/a ^swng', 



Middle High German swibein, swivelen'\wdc\\ Old High German sweibon^sdcwNebeu, 
swing', 5i4/eM/7'schweben'.
```


## [2026-09-14T03:13:46.988Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"haez\\|hai^z\\|haiz\" BRT.txt | head -20\necho \"=== BRT 'sich erheben' near haez ===\"\ngrep -n \"erheben\" BRT.txt | head -20"
}
```


### [2026-09-14T03:13:47.053Z] TOOL RESULT

```
22071:•  j.  vaeÄya-,  vaedya-  n.  'Kenntnis, Wissen',  mit  Akk.  oder  Gen.  obj.:  °%Tm mq%rahe  spitttake  Y.  22.  25;  —  -%lm ma^ntn  spintim  Y,  25. 6;  —  maziiläis 'dyäil  damayh  mäedayasnöis  "V.ij.y,  — mastim  spänS  ^iilmca  Yt,/o.  33;  —  sraostm .  .  ye^he  .  .  haeza^waca  ""oyä^a  (IS.)  Y. 57.23;  —  *'Um  F.<V.  [¥.5.27:  lies vaitya.paile.'\
28696:wohl    darum,    weil   das  iaiiiche  Konigshaas   •   j.    haez-   V.,    nur   mit  pätri   'spürend,
28698:•  j.  haetumata-  Adj.  'mit  dem  (Fluss)  »sihista  psiri.haizanuka  ytke  sa%aica HaHumant  zusammengehörig,  von  ihm  vaxiaica  yaotifm  dalät  ahurö  matdh  V. gebildet':  srayS  yat  kasaan  (sd.)  -Um  Yt   21.4.
29995:Pü. ;  US  est  kam  äydi  (aSlmp.).  —  ')  Man  er- wartete nach  dem  folgenden  päirLhaezatiuha und  nach  Pü.  eine  2SIM.  vy  yal-  mit  hant', ob  hqm.yoflaaiiha  (lu  yailo;  Praes.  6)?  Un- klare Slelle.
=== BRT 'sich erheben' near haez ===
5256:mit  US  'sich  erheben':  s.  *uzirfidyai Inf.  a)  insbes,  von  Gestirnen,  'aufgehen': fistrUn  .  .  yim  .  .  uzyö.rfnt^m'^  *AispS.- Sinti  Yt.  <V,  36;  —  hi'anxsaltim  vzyS.- rai/i'>^'V.ifi.2S^^;  —  uzayiira3^^>  uzlra^*^* Ava>vx/ag/a\.  21.  5,  17'*;  —  hmat  uzTra^* V.2/.s«>.
5258:mit  US  und  paiti  'sich  wieder  erheben, wieder  auferstehen',  von  den  Toten:  us irista  paiti  aranti^^  FrW.  4.3.
8581:•  j.  usii.hiStan-  Adj.  'sich  erhebend,  auf- stehend': yqm  yazata  ^ara^ustrd  °ta  (NS.) Aaia  gaivö  YL 16.  s.
8612:•  g.  •'uz-iraidyäi''  Inf.  'sich  zu  erheben, sich  aufzumachen':  a/  tS  trisi  nöit  asrultä (sd.)  fairyaoyis  uz'  para  hyai  mH  ü.Jimal suraoüi  ". .  befahlst  du.,:  'Mach  dich  auf, bevor  dass  mein  Sr.  herzukommt'"  Y.^j. 12.  a)  mit  Inf;  uz°  *a:S  sar^anil (sd.)  sJngAaAyJ  V.  43.14.
10451:mit  ui  i)  'hochheben,  erheben':  hakal iiigsr.'ptaiibya  aiigustafibya  uzgpr?piaSi- iya  püsriagiiyn  "mit  gleichzeitig  aufge- stemmten Zehen  und  hochgehobenen i'ersen"  Y.S.'jo;  jj; —  *kainSby5  yä  us xrünm    drafhm  gprswnqn   Y.57, 35;  — |
12025:•  j.  nav-  V.,  in  Verbindung  mit  vayBt ^Vehgeheul  erheben,  ausstossen'.  Praes.  i
13952:mit  afa  Inkoh.  'sich  zum  Rüg  erheben (in  der  Richtung)  nach  -  weg'  (Dat.):  aiia druxl  yä  nasul  apaJvqsaiti  apäx?oraHbyS nalmaHbyS  V.  8.  1 6.
14944:/.  132  und  Pü.  —  Pü.  (lu  l):  patirak  raaiihük, (zu  a):  löäin,  erl.:  fa  ifästaij  i.  zu  A%d.. ■  j.   paiti.tavah-   Adj.  'seine  Kraft   da- gegen   einsetzend,  Widerstand  erhebend': nsit  'vä  iavaiti  (sd.)  Yt.  JO.  48.
15107:—  sich  erhebendesLärmen,  Tosen' :>ü^-55r(l srävayeiti  ap3  V3  's^aine  (LS.)  raö^atths vä  .  .  "wer  die  Gä'^äs  aufsagt,  während sich  ein  Getöse  dagegen  erhebt  '*  hervor- gerufen durch  Wasser  oder  durch  einen Huss"  N.  26.
16757:—  isavasat  .  .  a£>mnS.vl^S  (sd.)  bavaitt (stattPlur.)  Yt70.39;  39 f.^;  —  nSiipaiti.- tava  bavaitt  "er  vermag  keinen  Wder- stand  zu  erheben"  Yt  10. 48.  4)  in gleicher  Bedeutung  auch  mit  Inf.,  uzw. a)  mit  lok.:  yavat  alte  spana  bii  hapta tttnana  *pairiialahi  (sd.)  bavan  V.  7J.  45 ;
16807:stimme, den  Ruf  erheben,  ertönen  lassen*:  tragen,  abreissen,  zerstören':  apa  aetam yS  mq'^rä  {sd.)  . .  *väcim  baraitT  Y,  50,  6;  \distqm  {sd.)  baraym    apa    a!t>m   taddtum
17152:•  j-  d  g-)  barat-  Adj.  i)  'tragend,  bringend', mit  Akk.  verb.:  vasirtm  '/S«"  gave  hu- "hajshe  ,.  gaodäyüm  nar^m  aiavatum  Vr,  2. II.         2)  '(Ruf)  erhebend"* (nur Komp.),
23784:•  g.   vöi  Inf.   'zu  erfireuen,  zu  gefallen',  1  'erheben'.
23785:mit  asti  (Sp.  a  7 1  m.)  sva.  'er  ist  die  Freude  j  '(eine  Waffe)  erheben  gegen  Jemanden' des  .  .'  (Gen.):  äiar/  V  matää  ahurahya  \  (Dat.):  yasca  vadarS  (sd.)  vHidai  asäunt aht  mainyui  v   ahyä   spSnistö  ahl  "alsjY-52.  i-
23789:mit  aiwi  '(das  Haupt)  erheben,  hoch tragen':  malyehe  . .  aiwi.vsizdayantakt*^ kamirio>m  ". .  der  das  Haupt  hoch  trägt" Y.p.31.
26681:mit  us'^  'aufstehen,  sich  erheben,  —  auf- richten von  — '  {kaca  mit  AbL):  us  a%at kiftat  satavalsS  ,  .  arayaiahat  kaca  .  .  Yt "32;  —  uakistat  sara%uitrö  fralosat  ..Y . '9-4!  —  usMstat  gaus  V.  2. 10  PUZ.;  — utihiStai  vohu  manS  kaca  gatvö  zaranyS.- kirats   V.  j^.  3 1 ;   —  pasla  yat   us?Aiität
```


## [2026-09-14T03:13:49.597Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 487 -l 487 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg487 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg487.png"
}
```


### [2026-09-14T03:13:51.298Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 76588 Sep 13 23:13 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg487.png
```


## [2026-09-14T03:14:08.251Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '28690,28710p' BRT.txt"
}
```


### [2026-09-14T03:14:08.308Z] TOOL RESULT

```
HiimandgthKXs,  Saistän:  'mirüim  raivan-
t>m*^  3!°ar?nanuhant3m''>  V.*Z.  13, /^.jg.   'nyS  ra%S  \\..  8.  S^.
AbUit{s.*ina/o-).— Eig.  "reich  an  Diminen'.—        Ablrit.   aus    thainä-,    —    tt.  sinya-  ta.\   »gL
aXf,  hibnanä.    —    Sü.:  Ailömand.     —    1)  Vgl.        liinya-  Adj.
Gdn.  3Yt,   131.    Im  Text  steht  nur  hai,   mit  =    ^j^^,  ,   ^
einer  LQcke   dahinter.    —    »)    Die  Beiwörter  _  '    *
wohl    darum,    weil   das  iaiiiche  Konigshaas   •   j.    haez-   V.,    nur   mit  pätri   'spürend,
vom  ff.  stammt;  s.  unter  iqiaoya-**).  Suchend  umhergehen'.    Praes.  3  ha&a:
•  j.  haetumata-  Adj.  'mit  dem  (Fluss)  »sihista  psiri.haizanuka  ytke  sa%aica HaHumant  zusammengehörig,  von  ihm  vaxiaica  yaotifm  dalät  ahurö  matdh  V. gebildet':  srayS  yat  kasaan  (sd.)  -Um  Yt   21.4.
Ableit.  aus  A«rt,™,„/..   Vgl.  iBild.  ai.  &aima-       "'■  ■  '^  ^'  *"'  **  ■  '  ^''  '*'  ^'«'■
vMä-  (mit  ffdJhi]  Adj.  zu  .i/moMW..  •   p.  hauv,  hau*,  j.  hau  NSm.  und  f.,
•  g,  *hae9'ahya-''  Adj.  'zum  Verband,  P^on.  dem,  'jener';  I)  in  starkdeiktischer zur  Genossenschaft  gehörig;  Genosse',  mit  Verwendung  'jener,  der  dort',  von  dem Gen.:  drap  hvS  dämqn.  '/ij-il  (APn.)  gät  gebraucht,  was  dem  Sprechenden  femer (sd.)  Y.  4^.  6"'.  '  ~  liegt;     nur    adjektivisch:    anusU  .  .  aval
Ableit.  aus  'kai%ah.  n.,  zum  V.  hS^)-.  —  kvar)  ä.tttpatte  anusB  hau  mä  anuso  ave PS.:  addm  ihit\  s.  zu  *(*ai^.  — ')  Vgl.  zLes.  stär5\  .0.  i,\\— ydha  käu  maza  nurztS GDN.^K^  iO.  53*  -nd  NA.  Ntr.    -    -)  Vgl.   .^^^  y^^^    a^/awra    upapi   Yt./^/l;
■j.^^„««j/N,^fl-liesi.-»-,..Sp.i724<..   "  -*^"   "'5'*^"   «^  '""'  *^'«"'ä'(a  (sd.) mit  No.  9.  "*"  "^'^  asnavät  P.  2t\  —  kva  astt  datvo
.  j.  'haena-,  p.  haini-  f.  'Heer,  Heer-  ■  ■  ^'^  Z'^",  h«^_^rinHi  .  .  a3aih>a schar'  uzw.  rfa?^ischer  Wesen,  'Feindes-  'i^^lsva  . .  hau  astt  äafvö. .  avat  daa,a heer,  feindliche  Heerschar':  Wabiy  imäm  ^^'"'^'"■'»^  ' . .  (sva.)  dort  ist  der  Z>. . daÄyäum  mä  5>;/.,>J*  ma  'nä  D.4.3;  V-Z-SafO;  _  s.  noch  H.1.7  (Sp.173»  o.); ^  n^it  i^ra  atryA  dai^hävS  fräs  (%A..)  "  ™  Gegensatz  zu  ÄJ  (Sp.  1718  o.):  >Sff yiyj/  •;«»  YtÄs6;  F.l-^;  -  ^«laäa  «P^-m^r^tS  i%^.  1143  m.)  ,4 5 «  ,.j-;tjr^.- «(■rr-^-b'iT  rfa/Vi^«4>.S  ■««  (NP.)')  frapatänti  '""'^  iäW  ..V.4.AS;  -  zugleich  aul  ein Yt..y.6i:  —  ya'ba  yai  hazarirS.aspam  erläuterndes  Nomen  vorausweisend:  aoa 'nam  avazeit  mäzduya'sni!  avi  vis5  Y.  hau  apa^^arS bvatzraya»ks vouru.kaiahe i8'.i^;  -  Ümäm  daAyüufn  ^ura^mazdj  ^""^  yH  haosravA  nqma  Ytip.sS;  59, patup  haia'nmD.4.6;  —  'nayä^axra-  ^'-  ")  '"  schwachdciktischer  Vcr- vai^yä  z>yazJayä  (sd.)  Aog.  A;  Yt  5.  131,  Wendung  jener,  der';  I)  zurückweisend; 4.  3.  19-  93,  ^-  II  (wo  'nayiuay-'nyhla  ^  *"/  f  ?  ^^O'uen;  a)  auf  ein  Substantiv; .  .  davai^yi  pataihyä  Y.0.18;  —  fiairi  «>  adjektivisch:  II  War««*  näm^  pärsa* ^•nyhsia  pöiynäuyS  Y.  68. 13;  -  ivi  'nayi  1  ■  ■  ''/'"'  ^'^rnaf  hada  kärä  al,yav^  Bh. (AP.)'>  xrvi^ätl!  Yt  10.  8;  />  49,  /<?.  54;  1  ^-  K^^'  '■  »?'  ^-  ?-  5-  • !  —  'Jäw«  /Jwa« —  ;*a.n<i>7'a/4yff*-«ÄS;'?"  Y.i7.asi>.  ^fi-ätfayam  . .  ya-^a  hauv  karJ'  parä- Ableit.  —  Zum  V.  ^(>>.  —  ai.  sinä-  f.  '"öJir  . .  Bh.  5. 1 ;  ü  —  »flr?m  afavarum  .. 'Heer';  mp.  (Pü.)  Äe«.  —  ')  NPn.  aUtt  NPf.  j  *hau  *n3"  .  .  P.2^;  —  zugleich  auf  ein (wie    umgekehrt,  S   ¥"■    3  d).     Vgl.    dazu  1  Rglativum    vorausweisend:    Wkärt/'    hyi^
steht  in  R4  und  Yl  70.  93.  I  ^h.  2.  6:    —   vahyaidätam  .  .  hauv  vah-
.  j.  'haeni-  C  'Geschoss':  liHrM . . ytiiht ''"""^  '''^  '""">''  'i'^'^  El"-.?.'. »»OTo(  (Sp.  931  o.)  ■nmam  *miva  saläil,  1'  ':'\^-  "'  —  "■*>;"«■««*  .  .  iäi-m Imza^rmia   '. .  dem  Ge'schoi«   zu   t^\/rä<!;y'f  ■ -hauv  klrJ- ^RyavJ'  l,am mAcn  900  und  1000"  YtJ.  no'l.  \frluli'yii'  Bh.j.911.         p)  substimtivischt
Ziun  gr.  V.  rjj/ij;  «.  diiu  (luletit)  BoH.  GrGr.3  ^^^  ^^  -  .  ^räiiUitrB  . .  kva  ht  aolS  tin- 373,  KuneVglGr.  546.    —    »  Gemeint  lind  |  (/Jffta?  Hau  Jalvanqm  sna&B  hSu'  ..  V.
55
ob,Google
I73I
```


## [2026-09-14T03:14:23.327Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9118,9150p' CHEUNG.txt"
}
```


### [2026-09-14T03:14:23.382Z] TOOL RESULT

```
«PIE — 

*REFERENCES: Kellens 1984: 102, fn. 8 


*haiz ‘to look, search for pastures ?’ 


*AVESTAN: (+ *pari-) Y Av. haez- ‘to search, scrutinize’ ? = Liste: 73 
MED .; Pres. them.: IMPV. 25р. YAv. pairi.haezar'a (V 21.4, V 21.12, Z 21.16) 


*KHOTANESE: (+ *pati-) ? pachiys- (mid./pass.) ‘to be called, considered’, pachis- 
(caus.) “to regard, consider’ — SGS: 63 

*NWIR: (+ pref. ?) ? Gur. (Kand.) vizin/-iz- ‘seek, (re)search' 

*NEIR: Oss. I. xizyn/xyzt, D. xezun/xizt ‘to pasture, graze’ 


«PIE An IE provenance for this Ir. root cannot be established. 
*REFERENCES: KPF II: 210 f.; DKS: 198a; Abaev, Slovar’ IV: 206 f. 


*hanH ‘to conquer’ 

*AVESTAN: han- ‘to conquer’ © Liste: 71 

Aor. them.: SUBJ. 1sg. OAv. hanani (Y 44.18), 3sg. OAv. hanat (Y 54.1), OPT. med. 2sg. Y Av. hanaesa 
(Y 59.30), 1р1. OAv. hanaema ° (Y 41.4); Partic.: pres. (caus.?) med. YAv. hanaiiamna- (Y 59.30), aor. 
OAv. hanant- (Y 44.19, Y 46.19), perf. YAv. hanhanus- (Yt 13.88), med. Y Av. haghanana- (Yt 13.88); 
Desid.: OPT. med. 3sg. YAv. išaphaëta (Yt 19.53)
```


## [2026-09-14T03:14:30.615Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"haxs\\|haxš\\|hax\\^\" BRT.txt | head -10\necho \"=== BRT hak- ===\"\ngrep -n \"j\\.  hak-\\|hax§\" BRT.txt | head"
}
```


### [2026-09-14T03:14:30.699Z] TOOL RESULT

```
4504:•  j.  anu-matayae-:vr,  "t^e  Inf,  '(und)  im Denken  zu  folgen,  zu  denken  gemäss  -' (Dat",  Gen.):  ya^a  azsm  /nJcayeiie  {sA) .  .  zara%ustr»m  "ISe  dagnayjt  aiiuxtJe  .  . anu.varHSe  Yt.5.18;  —  haxsaya  (sd.)  .  . frat^ma  .  .  aiähl  dasnayj  'iayaeca  , .  Y.
4519:aijuxOe..'t!e  daenayai \t.^.iZ; — haxsaya
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m  dätänmvohunam  damanqm\'^K.i-j.z;  16,  V.  79.  13;  —  us  mg  fita \,  16.  i;  —  nh'afiayemi..daiusj(StvcTZ.)iAaomäi  draond  frSnnaoi  °rS  mazdh  ..  V. °rahe  mazdä  ralvatS  c^annarmAalS  (Sl-  /j,  4;  —  astvatintä  .  .  asts  mazda  °rahe verz.)  mazistahe'a  vahistahe^a  sralHahecaYlx.ig.f)-i;  I3.\\f>,  V./(7.34;  —  buyama xraoMistake'a  xraiwistaheÜa  kukinpttma- ,  'rahe  mazda  frya  väsiita  astayJ  (sd.)  V, he'a  aSät  apanSJtmahe'a  hwiHmanS  vouru.- 1  70. 4;  —  haomö  . .  zaota  °räi  (statt  Gen.) ra/na»/i^  y7  nS  daöa  yd  lata^aylltu^ruy?\mazdai  Vty.88f.;  —  ySs^a  t!  y?na  'ra yj  mainyus  ipmtSJimB  V.  /.  i ;  usw. ;  —  mazda  Vr.  7.  4 ;  —  fravasTm  avqm  yqm pQuru^ar)na)3ha  'ra  mazda  VyL  2^^;  —  °raAe  mazdä  Y.  26.  2;V. 1^.14;  —  vXsp»mca °raki  mazdh  ..  STvUtah!  \.  56.  1;  — ^k^rs/s  'rahe  mazdä  Y.ji,^; —  ««  'rahe ax^aßis  ahi  abai>hJ!  tum  yS  °rD  maxdä  1  mazda  yazamaide  dar?ir3i  (sd.)  mq^rahtr V,  jp.  20;  —  'rät  mazält  .  .  vpr/irayne ■  sp^ntaAe  xralüm  'rahe  masdi  ..  marjirrüi frädat^aliai  yat  huxla'iräi  .  .  ratu-l..  hievam  ° rahe  matdä  . .  fravSkäi  .  .  Yt. xla%rai  Vr.ll.i;  —  huxsa'irSJ^mli.'if  1.2%;  —  gayehe  marP^nS  .  .  yS  paoiryd at  xsa'ir?m  eiyJt  yat  'rät  masdäi  A.^.  °räi  (stitt  Gen.)  mazdJi  manlscä  *git/ta 6;  s.  Y.J5.5;  —  'rät  masdäi  fanhavl  säsnasca  Yt./_J.87;  Y.jp.14;  —  nazdys vohumaill  Y.  I2.\;  "V,  tg.  11;  —  vaAists\ahmi  az>m  (Stverz.,  unter  3)  yö  'rS 'ra  mazda  Y.  /p.  1 5 ;  —  xsayat?  "rahe  I  mazda  vispahe  aukSul .  .  ya^a  .  .  P.  2(.?; mazda  YX.13.-jZ;  —  ise  ^wqm  'ra  mazda ..\  usw.;  Vyt.j^';  —  pascasta  azim  ya  'rS aoaoyf  ahi  a'iaoyS.xratul ..vTsps.viwS  Yi.'mazdil  aoi  urune  urväsma  (sd.)  dassayeni /2,  i;  70.  III,  V.  ig.  20,  a6,  Vr.jp.  i;  — Ivahi/ipmea  ahüm  .  .  V.38;  Y.ig.6,  7;  — °rJ  mazda  hvapis  Yt  5.  85;  Y.  7/.  10  (wo  vasas^a  tu  'ra  mazda  . .  x/ag/a  havanqm ab  Vok.) ;  —  'ra  mazda  mainyl  spinUta  1  däinanqm  Y.  Ä*.  5 ;  —  imat  dqma  yat  "rahe dätar?  gai^anqm  astvaitinqm  asäum  {^\.-\  mazdh  V.jy.14,  17,  34;  Vyt  20,  Vd.  i, verz.,  unter  I  2  a.);  usw.;  —  tsm  bay?m\YX.i(f.iZ,\.22.Z;  —  irrj/^/^-rJ (statt Vok.) t)m  ratüm  ,  .yim  'ram  mazdqm  daovätih?m  \  mazdä  vanuhti  dämqn  .  .  yazamaide  yäü i^t^vcz)  rapant3mtarh'a»h?mt'üpa*voh[i^dadä'ia  pouruca  vanhuia  Y.  7;.  10;  ;.  1, Y.70.1;  usw.;  fo.  9;  —  'rim  mazdqm\  12.  7, Yt  ig.  10,  58,V.  21. 4;  —  azmi  daoqm mainyaem  mainyavanqm  dämanqm  main-...tistrim..ya'ia  mqmcit  yim  'nm  mazdam yaoyä  stSts  ahUm;a  ratümca  Vr.  2.  4;  7,IVlÄ'.5o;  —  ttstrlm  .  .  yahmäi  hazaitnm ^'■57-4j  —  allat  dim  vlspanqm  mazih?m\yaoxstinqm  fradd^at  °rS  mazda  Yt^.45; dazdyäi  (sd.)  ahUm^a  ratUmca  yim  °r}m\iQ.Z%; —  tistrim  ..yim  ratüm  frada'hat masdqm  Y.  27.  i;  Vr.  /;.  21;  —  imimca'  'ro  mazdä  YL<?.  44;  5-  89,  70.103,^5.35; isi"^ rahe paitim ..yim  'rsm  mazdqmY.2.i6;\  —  arpdvjm  . . yeiihe  ca'^wärB  arSäna  ham.- 13.1,  ^.I03{?);  —  ySvaram  °rS  mazdä ..^tlsaX  'rJ  mazdä  Yt. 5.120;  —  ya'ia  vs tä  varmScä  .  .  ahmi  Y.12.  7;  —  mi^rpm  '  'rS  mazdä  fradaiim  haxsat  F.  ^Ib;  —  tä ..yim  yazata  'rS  mazdä  raoxsnlt  paiti  (frava^ayS)  ii3..'ä^rayente  ..aomna  'ra{lS^ gars  nmänlt  Yt.  10.12s;  5- '7!    —    avi\  mazda  Yt  13. 146;  S.7,  $&;  —  äyaptj/r.
7410:•  g.  a-radah-  Adj.  'der  etwas  bereit  macht,  |  k»hrp3m  utayoUis  dadat  -tU  atmä  (sd.)  V. zu  Stande  bringt',  mitAkLij-J  vi  titq'irs  :jo.T,43.6;~..ahur?myaliiy5 xsa^nmcä sravim  -d.i  (NS.)  "dass  euer  Prophet  ■  '^ayiSMvamrum  (sd.)  vartdaitt  'Hs  V.  2^. (auditum  perficiens  sil  sva.)  sich  Gehör  3;  _  ntmlhaxs  *'iil  mainya  *pfnsaiu verschaffe"  Y.2Ä7'>.  \ya^ra  ma^^a  (sd.)  Y.31.13;  —  vankius
9138:vgl.  hax^imanii-  und  invjta-,  —  np.  fiirmn (statt  i«ia;fi,  vgl.  Clrl*.  fh.  24).  —  ■)'  Sollte CS.  sein  und  könnte  Utsächlich  nachlScHMinr Krit.  87  als  GS.  erklärt  werden.
10037:jaAupa  i)  mit  Zielangabe:  'hinkommen, gelangen  zu  -'  (Akk.):  vJipim  a  aimät Vtt'iSit  upa.JasBit  tristam  tanüm  V.  6'.  2  7 ;  —  1 h/a^  möi  mraot  sp>ntöJ7m5 ,.ySi  ..  cayasca \ npä.jim»'!  iaurvata  amaritäta  vatthiui maifiySui  syao^anaii  masdä  ahurS  "was  ' mir  der  heiligste  verkündet  hat . .  - :  'Alle ' die  . .  sollen  zu  H.  und  A.  gelangen  durch die  Tätigkeit  des  guten  Geistes'  -  (er,  näm- lich) MAh.^  y,  45.  s ;  —  ya  tat  upa.- jamyama  tavalä  hax^mä  (sd.)  . .  Y.  40. 2 ;  —  hyat  ts  a.d3bagma  (sd,)  pinsmanJiig "t^-jasalX. 30.(1.  i)  ohne  Zielangabe 'hinzukommen':     upa     %warstaAe    (näml.
11375:—  aiatcjt  haca  Y.2p.  6,  27. 13;  j4. 13;  — hurayasHl  aoa  . .  daidyal . .  astmanqmcit ' . . K.3.4V,  —  aiwi.niticit  .,  span:>m  ..  aisa druxs  .  .  apadvqsaiH  V.  Ä  16;  —  tut  RS ttäcit  vansansY.51.1;  —  zusammen  mit U  (Sp.  367  o.,  586  o.):  f<M:"J«(sd.)  ..ya zl  vävfnzöi  pairl.cihlt  .  .  yScä  var?saiti aipT.ä^Tt  Y.  2g.  4;  —  bei  Zahlwör- tern: spiimm  zairitpm  .  .  xsvaiayacit  .  . vTväoayantu  \ .  8.  IT,  iS'^';  —  puxhmHl nä  arydu/qm  tanBm  ptrydte  V,  4. 17;  — para  mS  .  .  'hrifSt"^  vahista  .  ,  vlsata (sd.)  P.  J5; —  %risHi"'>  ..  hamahe  ayqn Vyt  41;  —  bes.  beim  Pron.  pers.  und dem.:  haxsaya  azsmat ys zara'kustm /ra- timq  .  .  anumatayaica  ..  Y.8.  7;  — pairi ml  tümcit  dayä  kaoma  . .  vahistptn  ahQm Y.ii.\o;  jo.  I9(?),  Vytj;  —  tun  vaimlit yazamaide  YL75.  i;  1;  —  ciknm  bsil yüi>mcil  :^armS . .  ääyaia  Ny.  J.  1 1 ;  VyL •S';  —  Aasat  va  nsit  vä  "der  (kanns)  oder (es  geht)  gar  nicht"  Yt/^- 20;  —  Jrä Mmat  nidar^zaypn  V.  J^.  31; —  tanu.mas5 (sd.)  zX  *altqmcit  alayqm  *pqfre  yat  ,  , P,  i8\    —    mä    ml   aetayasa£    tao^rayä
11741:Korrelat;  a)  substantivisch;  a)  im  gAw.: yaitat  (Sp.öi^m.)  mtzdim  ..  ndil  däifl,  kä tim  (ASm.)  ahyn  *mainis{sd.}  at^fiat  Y.44. 19;  —  ySngstü  masds  .  .  minal  (sd.)  , ., fing  zbaya(s6..)'^.46.  14;  — yqsca  haxsai (sd.)  .  .,  frö  iail  vlspais.  .  \'.46. 10;  — ya^qm  ndi^  hvarltStS  vqs  duzvari'tä,  lOi daft'fng (sA.)  dqn  \.4g.^;  —  Ayat  vä  IBi näntanqm  vazUttm  . ,,  tä  (IS.)  &wä  pairi- jasämaidl  Y.^.y,  —  y3  vS  ..  mazdä *>tämqm  dadät,  täis  vif  yazamaidl,  iai/^.. Y.JA4;  —  ptTMä  . ,  yä  iiudö  dadpntl .., ya^ia  tä  (NSf)  anfun  Y,_J/.  14;  —  yäsca tsi  g3na  ..,  ta  yazamaidi'H.38. 1;  —  hyai Urvätern  . .,  tat  ns  .  .  vüo^  Y.  j/.  3;  — : yä  frasS  (sd.)  ävJsyä  yä  vä  .  .  *p)r3saHl tayä  .  .,  ta  (APn.)  . .  aÜT  vamahi  Y. J/.13;  7  i..St,46.^;—y(i/ravaxIyä,ym tä  .,  Aai^tyi  Y.44. 6;  33-J3i  —  mit Numerus  wechseP*:  Ayat  mt:d)m  zardhustrS magavabyS  (sd.)  cöist  parä  .  .,  tä  (APn.) j'J  .  .  saväis  *avT!l  (sd.)  Y.5J.  15;  — yehyä  .  -  vaAistfm  .  .  vaida  masdä  .  ,,  tq yaaäi  Y.5/,  22;  —  at  yS  aktm  drigväitl . . var.'faiil  vaftkäu  vä  cSiäiaitl  (sd.)  astlm, töi  (NPm.)  värai  (sd.)  rädmtl  .  .  Y. j^.  2.  b)  im  jAw.:  yim  (näml.  a/rumf) vaiänte  aAurStsAS  .  .,  t»m  vafata  .  .  Vt. '4-  39t  —  yaUa  .  .  aiti  mazyS  . ,,  tat  no däyata  Y,  65. 14;  —  y^  -  ■  nigänhinti *msAii,aiti  (sd.),  nsit  tarn  . .  Y. /o.  15;  — yqm  alava  aiayqm  va^a,  tarn  drvä 7VT6va  Vt.  22,  2 ;  —  yeAhl  kätqnt . .  vanAS .  .  ahurS  val%S  .  .  yänAanUä,  tqscä täscll  yazamaidlY.2-j.\^\ — yh  nS  fanti gä'iä    hari^ravaitisca  .  .,  tä  m  Amti
12880:—  ')  S  411-  3  d. •  p.  darga-,  g.  daraga-,  j.  dar«}-a-  Adj. (fem.  °7J-)  'lang';  i)  räumlich:  Ufa  tarn car^am  yqm  'yqm  YtJp.  77;  5.50;  — mi^rtm  . .  yeAha  'yäat  bäeava  .  .  Yt.  10. 104.  z)  zeitlich:  M<?i«(sd.)  tat  äs  nsit 'y?m  Yt.5. 65;  —  "iimal  aipi  zrvätum Y.62.3,\tig.a6;  13.53;  —  °f^^  ^yo (sd.)  t^mattks  Y.31. 20;  —  'yayäsca  paiti danyjjltdis  YL  /y.  1 3  j ;  Y.68.11;  —  tsm (nämL  kämtm)  msi  data  'gahys  *yaos{^^^ vairyS  stSis  Y.  43.  13;  —  hyatcä  -gSm *Jr3gvö.d»dyS  rasö  {sd.)  Y.jo.ii; — ptn- fum/a  (sd.)  barjsma  starane  °y?mca  yasram ..yaaJnS'Vt.iO.iiSi—ya^a  Sicä  *aiivi- iayama  'ya  amiiayana  . .  hr^yrnya^^aSum (sd.)  Yt  70.  7  7 ;  —  °gäi  Tsyai  bfzvait!  hax- maim  (sd.)  Y.  40.  3;  —  'yai  hax^räi  Vt 10.  T),  17.6;  — fravaiayS . .  hulhaxmanS . .  'yaa'fyj  Aax^oralifyff  Vt  13.  30;  —  'y^m Aaxma  V.  60.  j;  —  dättm  tS tanuye  :^ar»nB ' urvnaläi  •y?m  havanfum  (sd.)  Yt77.  22; F.^b;  —  urunaica  'ye  havanhe  A.  i.ii; —  'yäi  AaosravaAAsi  .  .  -yai  AavafiAäi Vjtjs;  —  a  'yät  ^ä.bairyilt  (sd.)  Y. öo.  6;  —  'yqfi  upayanayä  (Stverz.)  Y, /.  13  usw.;  —  'ya  (APn.)  data  .  .  sara- >uäraAe  T.  ^6  {?);  —  iaia  tl  'yim  ävSya (sd.)  aakal  H.2. 34;  16.  a)  Adj.  an Stelle  unsres  Adv.'':  :^afsa  'yd  tna^äka "schlaf  lang,  o  Mensch"  V.  rÄ  16;  — earäiti  .  .  yä  'ya  apu%ra  aHti  V.  3.  34; 34.  b)  ASn.  als  Adv.:  H  utä,  'gam  jlvä
14328:/«%««»  Y.p,  19;  i9ffiS;  —  ana  äwal yasna  yaxäm  YLJ7.61';  —  kasp  %wam\ paoiryS  haotna  . .  hunuta  Y.  p.  3 ;  —  kana  , %wqm  yasna  yassane  Yt.5,  90,  15.  54;  —  ' kana  hwä  yaitia  ..  Yt./j.  54;  Vyt.21;  —  j az)m  'hwä  yasna  yasäfu  Vyt.20;  20;  — toi  äyapt^m, yas)  ^wä yäsämaAiYt  10. 33; 30,  5.90,  17.61,  Y.  Ö2. 1;  —  _>'öi  äioÄ vaffun  . .  Yl  io.  9a;  —  _)'o/  äai  J  dtdvllma Y,  öl?.  I ;  Yl  75. 30;  —  _>wji  %w3  didvalSa Y.J.  ai; — ^aäo  %wqi»  mit  taurvayät . . Yt./5.s6;  —  t^a  %wa  haxsöit  gjul vakwa  Y.63. 10;  10,  Vyty,  22,  45,  Any. 2^;  —  afii  %wä  3l>ayai  avairiAeYt.  lo.jy, 78;  — _/rJ  äwam  xadaraAa paiti  uzuxiäne Yt/9.  50;  48;- —  a/a  .  ,,  dansäma  haiS, pairi  %wa  Jamyama,  kamtm  hwä  haxma (sd.)  Y.  60.  la;  —  aoxtSJtamana  %wä yasna  ..yassi  Yt  /o.  31 ;  56,  Y.p.  27;  — aurvantsm  %tffS  ..iayS  tatasatY. 10.10;  10; —  yaskgm  %wqm  paiHsanhämi  V.20.7; 7";  — yaaamaiäe  %wa  aAuräne  Y .  68.  ^ (vgl.  6,  Sp.  787  o.);  Y.li.  10;  — yatayania %wqni  matdayasna  Yt.  10. 1  ig;  12.1';  — _fra  ff  kfhrpgmla  .  .yaoidäiäni;  ktnnaomi hwqm^^  hacaLpuhram  V, 2/.  6;  ■ —  b^a\ &a  histahe..,  iä^a  %wqm  tarasla  äahsns\ .  .  j^anha  bairydnte  V,^,  29;  verwendet Yyt.41';  —  /?  als  Akk.'"»:  . .  kuha  ti assm  biiazüni  V,  22.  6"*;  —  SU  aitike fraca  stuyl  . .  yezi  tl  aidhe  avil.urSrao%a (sd.)  Y./.ai'".  2)  Abi;  nur  b  i)   im
=== BRT hak- ===
6745:•  j.  ahax§ta-fna-  n.  im  Plur.  '100  000 Schläge' :  patuasaynsi  sataynäisca . .  balva-
```


## [2026-09-14T03:14:35.265Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D8%B3%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%DB%8C%D8%B2%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%81%D9%84%DB%8C%D8%B3\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 487, root Suig / Su 2\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-14T03:14:39.852Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c77527151d2802a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd6a4475dbb86574.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7da02de01117fdf6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7e235c25a6cfcd1d.txt
```


## [2026-09-14T03:14:42.618Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in c77527151d2802a0 bd6a4475dbb86574 7da02de01117fdf6 7e235c25a6cfcd1d; do echo \"##### $f\"; sed -n '/^ *Persian$/,/^ *References/p' $f.txt | head -60; echo; done"
}
```


### [2026-09-14T03:14:43.558Z] TOOL RESULT

```
##### c77527151d2802a0
 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xaːs.ˈtan/ 

 ( Dari, formal ) IPA ( key ) : [xɑːs.t̪ʰän] 

 ( Dari, formal ) IPA ( key ) : [xɑːs.t̪ʰän] 
 ( Kabuli ) IPA ( key ) : [xɑːs.t̪ʰän] 

 ( Hazaragi ) IPA ( key ) : [xɔːs.t̪ʰän] 

 ( Iran, formal ) IPA ( key ) : [xɒːs.t̪ʰæn] 

 ( Tajik, formal ) IPA ( key ) : [χɔs.t̪ʰän] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 xāstan

 Dari reading ? 

 xāstan

 Iranian reading ? 

 xâstan

 Tajik reading ? 

 xostan

 Homophone : خواستن ( xāstan  / xâstan ) 

 Verb
 [ edit ] 

 خاستن • ( xāstan / xâstan ) ( present stem خیز ( xīz / xiz ) , Tajik spelling хостан ) 

 to rise 
 (Can we date this quote?) , “ فریاد [ Outcry ]”, کریم فکور (lyrics), انوشیروان روحانی (music)‎ [1] performed by هایده : روز و شب ز گلویم / ناله خیزد و بس، آه، ناله خیزد و بس ruz o šab ze galuyam / nâleh xizad o bas, âh, nâleh xizad o bas In day and at night, from my throat / Groan rises and that's all, oh, groan rises and that's all 

 Conjugation
 [ edit ] 

 Conjugation of خاستن ( literary Iranian Persian )

 infinitive

 خاستن ( xâstán ) 

 stem


##### bd6a4475dbb86574
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( lystʾhyc /⁠rist-axēz⁠/ , “ resurrection ” ) . That latter part xēz is related to خاستن ( xâstan , “ to rise ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ras.taː.xeːz~ris.taː.ˈxeːz/ 

 ( Dari, formal ) IPA ( key ) : [räs.t̪ʰɑː.xeːz~ɾɪs.t̪ʰɑː.xeːz] 

 ( Dari, formal ) IPA ( key ) : [räs.t̪ʰɑː.xeːz~ɾɪs.t̪ʰɑː.xeːz] 
 ( Kabuli ) IPA ( key ) : [räs.t̪ʰɑː.xeːz~ɾɪs.t̪ʰɑː.xeːz] 

 ( Hazaragi ) IPA ( key ) : [räs.t̪ʰɔː.xeːz~ɾis.t̪ʰɔː.xeːz] 

 ( Iran, formal ) IPA ( key ) : [ɹæs.t̪ʰɒː.xiːz~ɹes.t̪ʰɒː.xiːz] 

 ( Tajik, formal ) IPA ( key ) : [ɾäs.t̪ʰɔ.χez] 

 Rhymes: -eːz 

 Readings

 Classical reading ? 

 rastāxēz~ristāxēz

 Dari reading ? 

 rastāxēz~ristāxēz

 Iranian reading ? 

 rastâxiz~restâxiz

 Tajik reading ? 

 rastoxez

 Noun
 [ edit ] 

 رستاخیز • ( rastāxēz, ristāxēz / rastâxiz, restâxiz ) ( Tajik spelling растохез ) 

 resurrection 
 Synonym: بعث ( ba's ) 

 Further reading
 [ edit ] 

 Hayyim, Sulayman ( 1934 ), “ رستاخیز ”, in New Persian–English dictionary , Teheran: Librairie-imprimerie Béroukhim 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=رستاخیز&oldid=91554003 "

 Categories : Persian terms inherited from Middle Persian 

##### 7da02de01117fdf6

##### 7e235c25a6cfcd1d
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: سیفلیس 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 سفلیس 

 Noun
 [ edit ] 

 سیفلیس • ( siflis ) 

 ( pathology ) syphilis 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=سیفلیس&oldid=87814843 "

 Categories : Persian lemmas 
 Persian nouns 
 fa:Diseases 
 fa:Sexually transmitted diseases 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 31 October 2025, at 23:16.

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

 سیفلیس 

 3 languages
```


## [2026-09-14T03:14:49.613Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg487.png"
}
```


### [2026-09-14T03:14:50.129Z] TOOL RESULT

```

```


## [2026-09-14T03:14:50.125Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:15:06.034Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN swine ===\"; grep -n \"3\\.32\\|sū-s\\|'swine'\" SYN.txt | head -10\necho \"=== SKT hog ===\"; grep -n \"^hog\\|hog, \" SKT.txt | head -5\ngrep -n \"Hog\\b\" SKT.txt | head -5\necho \"=== SKT soil/swine/hyena ===\"; grep -n -i \"hyena\\|Swine, sb\\|Soil (2)\\|Soil, \" SKT.txt | head -10\necho \"=== WLD Bd2 sus ===\"; grep -n -i \"sū-s\\|su-s, suu\\|Schwein\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -10"
}
```


### [2026-09-14T03:15:06.159Z] TOOL RESULT

```
=== SYN swine ===
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
4310:3.32 BOAR
4408:3.32. ‘Boar’. Words that are used only of the ‘wild boar’ are not included (except the Sanskrit and Avestan) un- less they belong with others which are used for the domestic boar. Thus Lat. aper is considered, but not Fr. sanglier, ete.
4439:: ae or Ee , See 3.32.
4451:*s7- (3.31), in this form completely specialized to ‘sow’ in Gme., or belong to other groups discussed in 3.31 or 3.32. The others are:
4562:3. Iv. ech-cullach, or simply cullach, Br. marc’h-kalloc’h, with deriv. of word for ‘testicle’, W. caill, Br. kell. Cf. Ir. (muc-)cullach ‘boar’ (3.32). Also Br. marc’ h-kalc’h with kalc’h ‘penis’.
12792:off, mow’ (3.32). Walde-P. 2.407. Falk-Torp 650.
23366:13.32 Onn
23835:Except for some suffix-variation and actual substitution in the case of ‘one’ (13.32), the IE words for ‘one’ to ‘ten’ have persisted everywhere with only slight changes other than phonetic; like- wise the IE word for ‘hundred’, while for ‘thousand’ there are several different groups.
=== SKT hog ===
14435:porcelain.    \?,  —  ItaJ.  — 'L) from  the  resemblance  of  its  polished to  that  of  the  univalve  sfaell  with name.  —  F.  pontiaim,  pcufrtinm*  \ purple*fish,  the  Venos-sacU;'   Got* pcrullana,  'the  pnrplc-Bah,  t  Ulidflf eaith,   whereof   they    make  . duhcs;'  Florio.     p.    Th-  '»^>' from  the  curved  shape  ■ like  a  pig's  back.  —  It  i dimin.  of  porco^  a  hog,  pig. « t*. occ.  oiportHSj  a  pig.
20482:Urchin,  a  hcdgehoe,  goblin,  imp,  smill child.  (F.-L.)  Urig.hedgchoj i.  I.  ^26):  hence,  goblin,  imp, it  being  supposed  that  some  : . hedgehog's  shape ;  see  Ha^  —  t  > erifon,  htriixoH,  a  hedgehog ;  lo sninx  -OH  {*=  L.  •otum)  from  L.  truim,  % hedgehog,  lengthened  form  of  fr  {eeL. rri-t),  a  hedgehog.  ^  Gk.  xV*  hedgcbcc- Lit.  *  bristly  ;  ■  ct  L.  Aertvrg.  {^CAIA.K)
2788:O&ninfi.  (I>.)  L.  catunur,  tietonging  (o a  Hog.  —  L.  canu,  a  dog ;  see  Hound.
8250:Hog.  (E.)  M.  E  heiggg\  with  same sense  as  .\.S.  hagi^stt,  a  witch,  a  hag.  ^ G.  ktxe,  M.  H.  G-  hackt,  a  witch,  O.  U.  G. ktiitjia  [prob.  short  for  hagasissa*]^  a witch.  Moit  likely  (rom  A.  S  ka^^  a hedge,  bu^h;  it  being  >uppo5ci1  thot  witches were  seen  in  hedges  by  nighi.  See  Hag- gard (i)  below.  ^  We  may  parlicalorly note  Viu.kaagJis,  kaagtdis,  a  lizard  (plainly from  Du  haat;.^  a  heilgc),  which  stnkingly resembles  A.S.  ka^esse.     Cf.  urrhin.
8746:Hog.  (E.)  M.E.  Ai7jj:y,  *maialis,e5tenim porcus  carais  testiculis';  Catbol.  Anglic, p.  1 8  ; .  K  rom  the  verb  hack  \  Scotch  hag),  to cut-  Ci.hcg-shnp.  one  clip|«il  the  first  year.
=== SKT soil/swine/hyena ===
9016:hydrostatics,  the  science  which  treats of  fluids   at  resi.    (Glc.)      Gk.  C^*'-,  for CSa'p,  water  ;  and  Statics,  q.  v. Hyena,  Hysno.  a  sow-like  quadruped. (L.  —  Gk.)    L.  Ayana,  —  Gk.  ^atva,  a  hyena ; lit.  *  sow-like.'  —  Gk.  C-t,  a  sow,  cognate with  E.  Sow;  with  fc-m.  adj.  Buffix  -xuro.       ^| Hymen.  (I..  -  Gk.)     L.  AymtH.  -  Gk.     ■ iVnv",  the  god  of  marriage. Hymn.  i,F.  -  L.  -  Gk.)     W.^ympnt (with  excrescent  /),  —  O.  F.  ymtu  tlater     ^ Aymtu).  —  L.  kymnum^  ace  of  L.  Aymnms.      ■
17585:smut,  a  spot  of  dirt  or  soot.  (Scand.) Formerly  smutch,  put  for  smuts*.  ■•  Swetl. smuts,  smut,  dirt,  Daii.  smuds,  smut; whence  Swed.  smutsa,  Dan.  smudse,  to soil,  -f  G.  schmutt,  dirt :  schtautten^  to smud(;e.  0.  Allied  to  Swcd.  smtt,  grease, fiUh,  smitta,  lo  bedaub,  infect;  A.  S  twit' ttan,  to  spot,  ttsmitan,  to  defile.  AU  from base  of  the  verb  to  smitt  (above).
17739:exile,  banishment.  (F.  —  L.)  O.  F exil,  '  an  exile,  banishment ;  *  Cot.  —  L. txiltHm,  \jc\Xkt  txsiiium^  banishment —1>. txsui,  a  banished  man.  one  driven  from  his native  soil.  — L.  cr,  out  of;  solum  soil, ground  labovc).  %  But  now  geii.  ilcr  from L.  soiiff^  to  leap,  luii.
17740:60II  (t),  ground,  country.  (F  —  L.) M.  E.  W/r.— O.  F.  j«/,  sue/,  Uter  /NriV. threshold  of  a  door.— Late  L..  io//a  soil, ground  i^by  confusion  with  L.  tofum, ground) ;  L.  soUa,  a  sandal,  sole,  timbei  on which  wattled  walls  are  built.  Allied  to L.  solum^  ground ;  whence  F.  sol,  soil, ground  1  from  whidi.  however,  the  £.  word cannot  be  directly  derived).
17914:BoU  (a\  to  defile.  (F.  -  L.)  M.  E. ioiUn,  [Not  allied  to  M.  £.  xwi^n,  E. /»//f  ]  — O.  F.  soiUtfr,  F.  stmiiicr^  to  soil; St  souithr^  to  wallow  as  a  sow  —  O.  F. soil,  soHxf,  '  the  soile  of  a  wild  boare,  the mire  wherein  he  hath  wallowed;'  Cot. [Cf.  ProT.  svihar,  to  »oil,  solh,  mire,  nt/^a, a  sow;  plainly  from  L.  siwu/a,  a  young sow,  dimin-  of  sus,  a  sow.]  — L,  suUlus, Bilj.,  lielonging  to  swine. —  L.  sus,  a  suw. Der.  soUt  sb.,  a  stain ;  quite  distinct  from soii,  ground.
22840:sack,  sage,  sallow,  sap.  sardine,  sash,  saw, say,  scald,  scale,  scar,  scarf,  uonce,  scout ftcrew.  scrip,  scull,  scuttle,  seal,  scam, see,  sell,  settle,  sew,  sewer,  shart,  sbcdi sheer,  shingle,  shiver,  shoal,  shock,  shoitti ihrew,  shrub,  sizt,  skale,  slab,  stay,  s]op( slot,  smock,  smelt,  snite,  snuff,  soil,  sole^ sorrel,  sound,  sow,  spart:,  s]  cU.  spill.  !>pir<e|j spit,  spittle,  spray,  spurt,  squire,  stal^, statist  stapte,  stare,  stay,  stem,  stern^ stiti,  stile,  still,  stoop,  story,  strand,  strotti^ strut,  stud,  sty,  style,  summer,  ftwalluw^i swim.
=== WLD Bd2 sus ===
2735:(Holthausen IF. 32, 334, Engl. St. 50, 33S) „Schweinchen“. Abg. zapr^i^k^ 
3057:Sippen "^porJeos „Schwein'' f^jjAYiibler") und "^perk-, prk- ,,Purche" anreiht, 
3331:Schinken‘‘, lat. perna „die Hiifte nebst dem FuJBe ; Hinterkeule, Schweins- 
5112:porkos „Schwein“. 
5114:Gr. (nach Yarro I. 1. Y, 97 M) noQxog „Schwein“. 
5116:Lat. porous „das zahme Schwein^^ umbr. porca „porcas“; mir. ore „Schwein“ ; 
5119:parszas „mannliches verschnittenes Schwein“, apr. prastian „Ferkel“ (nach 
5121:t erinnert freilich an den slav. -^^-Stamm); ahg.prasg, -ete „Schwein, Ferkeh^ 
5122:Zu lat. poremus „vom Schwein“ vgl. lit. parszma „Ferkelfleisch“, zu lat. 
5123:porcidus „Schweinchen'\ Das lit. parszelis „Ferkel“, ahd. farkeli^ mhd.
```


## [2026-09-14T03:15:15.756Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sü-s\\|su-s,\\|suu-6s\\|suu-os\\|sûs\\|hyaina\\|vaiva\\|sukko\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20\necho \"--- search 'Sau' context\"\ngrep -n \"„Schwein, Sau\\|Sau\\b\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -20"
}
```


### [2026-09-14T03:15:15.832Z] TOOL RESULT

```
33251:SU- (*5^7-5, ‘’^'suu-6s) „Scbwein, Sau". 
--- search 'Sau' context
11534:Mit Abtonungsstufe *bhol- wohl norw. b^l „brunstig, von der Sau‘' (ab- 
33251:SU- (*5^7-5, ‘’^'suu-6s) „Scbwein, Sau". 
33296:Kons.-Dehnung norw. schwed. sugga ,,Sau“ (wenn g nicht ehva aus ic in 
41730:u. drcdk N.); Yrabrscheinlicb lat. troia „Sau“ {Hrogia „die dreckige“; Sommer
```


## [2026-09-14T03:15:17.959Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33251,33305p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T03:15:18.027Z] TOOL RESULT

```
SU- (*5^7-5, ‘’^'suu-6s) „Scbwein, Sau". 

^ ^ c 

Av. lift- „vSchwein" (Bthl. BB. 15, 40); gr. vg, I'd? 5,Schwein'‘ (davon gr, 
vdiva j.Hyane"; uber gr. cvg s. u. 

alb. „Schwein" (Gi. Meyer Wb. 90; dazu siUa PL ^angeschwollene 
Driisen" mit ders. Bed. wie lat. scroplndae^ gr. yoigag; zum Anlaut Ji-'.s- 
s. Pedersen KZ. 36, 282); lat. 5775, 577/5 „Sch\vein“, umbr, sif „sues‘', ^sim 
„auem"; tochar. B. sinvo; 

ahd. ags. 5^7, aisl. syr (Acc. sil) lett. auf Grund von *5zm-, suvens^ 

sirens „rerkel" (zu apr. setveynis „Schweinestair* s. Trautmann Apr. 425, 
Bsl. ^Yb. 294); adj. uo-Ableitungen einerseits gr. (spilt.) vivog „vom Schwein'% 
andrerseits (idg. Bildung) lat. stimns ds., aksl. svim ds. (in stado svinoje 
„Sch\veineherde“; vgl. auch svinija 5,ychwein“, substantiviert got. sivein^ 
aisl. 5 u 7«, ags. ahd. swJn „Schwein*^ : davon wieder ahd. swnim „vom 
Schwein", russ. (usw.) svinina ^^Schweinefleisch". 

^ Mit g-Formans (wie iett. zfiJca, lak. olyM, s. u. *(7/^7-): ai. sfiJcard-li „Eber, 
Schwein" (umgedeutet als ,,Su-macher‘', s. Bgm. II' 1, 483; aber lat. su- 



suro-s 


513 


ctila, -tis ist mit der ital. Deminutivkombination -Icelo- neugebildet, wohl 
unter direkter Xachahmung von 'porcidus): 

cymr, liivch f. „sus, porcus“, corn, lioch^ bret. houcli ,,porcus‘‘, air. 
socc-sad „lolbgo“; damit w^esentlicb identisch ist air. socc „(*Sc}iweine-) 
Schnauze; Pflugschar'%* gallische Lw. sind cymr. such, bret. souch^ corn. 
soch (und frz. sq() „PflugscliaP' (Thurneysen KR. 112, Schrader RL.^ b3l, 
Meyer-Liibke Rom. Et. Wb. 607; Pick II ^ 305 f.; dafi das gleichbed. 
vvvig, vvvi] „Pflugschar“ nach Bgm. IP. 28, 366 ff., s, auch Kretschmer Gl. 
5, 310, aus V- und einem zu dt, ScJinauze^ schnilffeln^ usw. gehorigen, mit 
syi- anl. 2. Gliede zsgesetzt sei, ist nicht sicher, s. Lit. u. "^imfilinis)] 
ags. stigit mud, sage j nhd. schwiib. suge mit deminutivischer 

Kons.-Dehnung norw. schwed. sugga ,,Sau“ (wenn g nicht ehva aus ic in 
gen. ''^suices usw. nacli Bugge PBrB. 13, 504ff., van Helten IF. 18, 102, 
s. auch Falk-Torp u, so K. ; doch ist der Lautiibergang nicht gesichert). 

Idg. sii- ist altes Schallwort wie gift- (z. B. Boisacq u. Og) und nicht von 
seiner Fruehtbarkeit (: "^scu- ,,gebaren'3 z. B. Curtius) oder seine Yorliebe 
fiir Morast und Schmutz (: ^seu- „sucus‘3 Yf. LE^Yb.^ u. siis zw. benannt. 
Ygl. Curtius^ 3S2, Pick I^ Ulf., 332, 565, II ^ 305f, III^ 442. 

Suro-s j.sauer, salzig, bitteP', zunachst von kiisig gerinnendem, schleimig
```


## [2026-09-14T03:15:27.417Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index SU ===\"; grep -n \"SU-\\|SUS\\|XUK\\|KHUK\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY خوک ===\"; grep -n \"خوک\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== ARY خاستن ===\"; grep -n \"خاستن\\|خیزیدن\" incoming/ARY/ARY_pages.txt | head -10\necho \"=== HUB xastan ===\"; grep -n -i \"xāstan\\|chāstan\\|xēz\\|aufstehen\" HUB.txt | head -10"
}
```


### [2026-09-14T03:15:27.525Z] TOOL RESULT

```
=== ARY latin index SU ===
77:$992 4D Mal sT 9 KyarT 9 KlasTD SlHoSly YSUSI 539) Joule
398:SUSE yey pad ad satya gl ys) Spb} 1 tay ork cath eg 9 gheasbh
425:1) Ath AS SUS ony 24 She oS2 )0 9.909 ghey) AS sbdLj e494 ely.)
745:Pb; FV eile lS bby py Cr SLel that Hey te FO SUS CWA SF
961:22 Dba I SUS ey 5S Pus El; 92.2 5 LJ WME AL Gla doe S9y
2105:DELAMARRE: (SUR, AU-DESSUS) 303 {OLD HIGH GERMAN) gS glasT
2783:MACKENZIE: 61 ASU-, ASUS., (SANSKRIT) oy Site
2785:| (ANSU-) 2021 ANSES (GREER) gly
4111:NOS A(SERNIAN) «9 pe NASUS, NARIS (LATIN) 3
4392:PARADISUS (LATIN) 3 PAIRIDAEZA H(AVESTAN) glen!
=== ARY خوک ===
294:«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می‌دهد که این مردم به کشاورزی هم اشتغال"
938:همریشه‌ی مربوط به «اسب» و «گاوه و «گوسفندء و دسگ» و «خوکک؛). همریشگی واژه‌های متعدد
4600:معلی این واژه در ارمنی: ران خوکك.
4931:معنی واژه‌ی .5۳۸۸-۳3681 در زبان آلمانی: خوکك شیرخوار,
7478:خوک ۲۵۵
7524:در بیشتر زبان‌های هند و اروپایی برای "خوک نر" و خوک ماده" واژه‌های متفاوت دارند و این واژه با هم در این
11122:چم این واژه در زبان لاتین و دیگر زبان‌های رومانس: گرازه خوکك وحشی :
11762:۲- چم این واژه در زبان‌های غیراز فارسی: اتانکد» خوکك دونی» غار» کلبه» تفای ی و
=== ARY خاستن ===
=== HUB xastan ===
1840:462. Dazu afgh. xat(}l *sich erheben, aufstehen', pr. 3. p.
```


## [2026-09-14T03:15:31.019Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7470,7540p' incoming/ARY/ARY_pages.txt\necho \"===== nearest pdf page tag\"\nawk 'NR<=7478 && /\\[pdf page/ {t=$0} END{print t}' incoming/ARY/ARY_pages.txt\necho \"===== HUB 1835-1850\"\nsed -n '1832,1852p' HUB.txt"
}
```


### [2026-09-14T03:15:32.063Z] TOOL RESULT

```
۱ 2۷219 ,2611810 81۸0 رالش ت57
بلوچی (041(ادلم8): 20۸ انگلیسی (20/00/5/7): 58۸110۷ ب3ل ۰90"
افغانی (پشتر) (//(۸۲0/۸: 7۸81[ دانمارگی (0۸0۷15/7): اد + 8 ان رن
آرمنی (۸۵4821۸): ,208716 سر دی (5770151): ت57
ایسلندی کهن (۷م هی صرم): نروژی ((۵08۳801۸): 5781618 م5013
3 ,57816۸ ب80133 هلندی (/0076): ندشن ریما
[pdf page 254]
۹ 5
خوک ۲۵۵
پسگشت‌ها انعر ند 1 (5/۸73.0۷0) :00/5
5 ۶002200 37
امه 2 (8]7) ما62 (8۸301)
2 (8[13) ,1099 3۵7۵ت۸ق) : مارا
۸1528 6 (5۸1) ,2 (0378)
1 (081(6) رقلا (5هق) برهان قاطع : ۷۸۸
1 , 328 تاه
بادداشت:
چم این واژه در زبان آلمانی: بزم برپاکردن.
چم این واژه در زبان انگلیسی: با حرص و شتاب خوردن؛ بلمیدن.
اوستایی ([/4887): :1 وتو
پهلری (1الل۲۸). 26 آلمانی ((088944): 7 و8۸
اوستی (0595716): 1 ل70 انگلیسی کهن (5لا84/0 صا0):
کردی (801377(): 2 5617 ,اا5۳ ,ناک
بلوچی (اللتانلمه): ب16 3 انگلیسی (8/0لق2۷0): 1306 ,5712158 ,8017
اففانی (پشتو) (/4۳0//۸/۷): ۰ 216 بکانا311 دانمارکی (0۸]84): 7 ,80
تخاری 8 (8 2427 /51۷22:)7087 ,810۷70 سوئدی (9780/8[7): 5۷1380 ,50 ,81766۸
سانسکریت (7ل84(/58): نروژی (۸۷0۳80140۷). ۰ 5718۲ ,81706۸
7 ممْتهانآو هلندی (07767): 37 ,2876
مین 4 یرنانی (0728/0): ۰ 15058108 ,138 ,1818 ۰ اسلاوی کهن 54۳1۵ 4ل#نابقه صان): ۱
لاتین (/4712ل): ار ۸ ,5۷9
شرآنا6ن51 ,51111178 ر8آنا9 ,818 لهستانی (۳0./5/4): این
گرتیک (0077810): لاد ین روسی (/۷2954): 5713101 ب87177[۸
ایسلندی کهن (۸1۵2/ 52/0 ضام): چکه (2801)): الا ان
۷ بلالآ8 صربی (لفا5578): اناد
ساکسونی کهن (//5۸200 57131:)01-0 ,81۸ برهمی (80[78(/127): لاد
آلمانی کهن ((6284۸ 4ل0الز صا): اسلواکی (81.07:4/4): 51۸
سم
[pdf page 255]
۶ ) خون ‏
لینرانی (4(0لفلا بل 7/): آنا1۸ پسگشت‌ها اشکیت را
لتونی (لتی) (700مل): 8 بو
4۸ ,51۷828 ,81705278 ادا سا

پروسی کهن (۶9۵(۷ت۲۴ ۰:۵ 88۷8۰ 2 (5۷13۵) ,1۵38 600 ی
ایرلندی کهن (تلقل#ا صا0): :3 (م 05
4 806 7 (7818 ,۳۵8۸)
سلتی (کلتی) (81-716-): رده زان 7 (۳16) ۱ :2/5
گالی ([5/.انا0۸): -81 104 نقلاظط
ولزی (877ل8): 8 ,ق1106 005
برتونی (83870/0): ۰ 110011 ,110161 9 (80) ,394 (8717/8)
آلبانی (۸فاالمقام: 713 :57
: 4 (80) ,63۵ (8135)
برهان قاطع + ۷۹۴
یادداشت:
در بیشتر زبان‌های هند و اروپایی برای "خوک نر" و خوک ماده" واژه‌های متفاوت دارند و این واژه با هم در این
فهرست داده شده‌اند.
اوستایی (/47287/40): ۷011181۸ ,-۷0171181 انگلیسی (8۸/0/.1874): 0028
پهلری (1/مال۸ه). ,2:08 نروژی (/(۸/0878014): ۸ 032
کردی (00(57ا). ۸7 ,1۸
بلوچی (تلتاءله8): ,1109 پسگشت‌ها گت دش
اففانی (پشتی) (4507440/1. ۷۷13۷۸ ب۷90 8 20
سانسکریت (8۸(/98577): ۷۸۵۵۸ ب۷۸82 9 (007) ای اما
ایسلندی کهن (010۸1۸۸0/(ی5 صان): 4 (81000) :3 2 ال مار
5۸ ,۷88 6 (81000) لاه
۱ فریزی کهن ((فا5ل۲ صا0): ۳5 8 (0078) :07/105
آلمانی کهن (05701۸(0 24104 صا0): 2 (0073) 37
۷۸8۸۵ 2 (81000) ۸400
آلمانی ((05701۸): نیا برهان قاطع + ۷۳۹۵
انگلیسی کهن (#تخلا80 صان): 15 فرهنگ معین + ۱۴۶۶۲۰
. چا
[pdf page 256]
===== nearest pdf page tag
[pdf page 254]
===== HUB 1835-1850
Afgh. LW. clz und dTz a thing.
460. Ich stimme Bartholomae bei.
461. Np. xdr *Dom' (dazu xOrpust Igel' = Stachel-riicken),
afgh. LW. xar *Dorn' = arm. xar^ xar *Dorn (Galen);
np. xWra^ xara *harte Stein, Fels' = arm. xarak harte
Stein' (Hexam. des Basil.). Ob arm. Kar 'Stein' (als
urverwandt) und xari *penis' (der Worterbiicher) hierher
gehSren, steht dahin.
462. Dazu afgh. xat(}l *sich erheben, aufstehen', pr. 3. p.
xezi. Freilich macht xatql Schwierigkeit, da es nach
Geiger fiir *xaStql stehen soil, das nicht zu np.
xdstan stimmt.
467. Np. xdvar „Herr** wiirde seiner Bedeutung nach nicht
zu zd. x^apara- giitig, gnadig (Epitheton weiblicher
Genien) , phi. x^apar in x^'apar-ddr-lh Truchtbar-
machung (West, PT. I, 29), paz. x^awar 'compassio-
nate' Shk. 256, phi. x^'CLparih compassion' Shk. 182,— 54 —
Z. 2 stimmen, auch wenn es vorhanden ware, was
aber nicht der Fall ist: xcLvar-xudai = der Xavar-
herr Fird. I, 154, 465.
469. In den Nachtragen wird saxudan zerkratzen' (afgh.
```


## [2026-09-14T03:15:45.973Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%D9%84%DB%8C%D8%B3/\" --note \"page 487, Mo'in on سیفلیس (MON:1979)\" 2>&1 | tail -1"
}
```


## [2026-09-14T03:15:48.097Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WEB hog ===\"; grep -n -i \"hog, n\\.\" WEB_vol1.txt | head -3\necho \"=== FSD hog ===\"; grep -n \"hog\\b\" FSD_vol2.txt | head -3\necho \"=== LKT/none ===\"\necho \"=== MON خوک ===\"; grep -n \"^خوک\\|خوک:\" MON_part1.txt | head -5\ngrep -n \"خوک:\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-14T03:15:48.759Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e5aa586b0584b30f.txt
```


### [2026-09-14T03:15:48.875Z] TOOL RESULT

```
=== WEB hog ===
88637:hedge bells, hedge bindweed. hedge’ber’ry, n. the hagberry. hedége bill, hedg/ing bill, a pruning hook for trimming hedges. hedge bind’weed, a climbing vine related to the morning-glory. hedge’born, a. born under a hedge; hence, of low birth; rustic; obscure. hedge giir/lic, a tall, white-flowered weed of the mustard family, with heart-shaped leaves, stiff pods, and the odor of garlic. hedge’hog, n. 1. (a) an insectivorous quadru- ped of the genus Erinaceus, with a shaggy coat and sharp spines on the back, which bristle and form a hedgelike defense when the animal curls up; (b) any of several other an- imals resembling the hedgehog, as the porcu- ee similar American animal of a different amily.
91263:hog, n.; pl. hogs or hog, {ME. hog, hoge, hogge, a gelded hog.]
=== FSD hog ===
411:A   surgeon-ttah  or  teuthiclld.—  d.^gum,  n.  See  hog-gum.— d.spqmp,  72.  Same  sis  dootoh,  n.,  3   (2).— d.«shears,  n.
1355:do-sad',  I   do-sSd';  2   do-sad',  re.  [Hind.)  1.  A   Hindu  of  a low  caste,  whose  occupation  is  to  remove  e.arcasses,  to  per- form other  "unclean"  offices,  and  to  provide e.xecutloners. 3.  A   hog-keeper,  do-sadh'f.  Compare  dome’. dos'-iisdos',  1   do'-za-do';  2   d0'-.3a«d0',  adv.  [P.)  Back to  back;  said  specifically  of  a   figure  in  which  dancers pass  each  other  In  this  manner,  or  of  the  position  of  those sitting  in  a   dog-cart  or  outside  jaunting-car,  and  some  rail- road-cars. [users  are  back  to  back.
2656:PnioB  ?'a  Dr.  BherlttckA,  42. 3.  To  sink  or  come  to  a   close  gradually:  decline;  as,  the day  droops ;   her  life  i.s  droopinij.  4-.  Naut.  To  hug,  a.9 a   ship.  See  hog.  .5.  [Frov.  Eng.)  To  drip.  [<  Ice, driepa,  droop,  <   d.-JUjiti,  drip.]  Syii„*  hetnd,  bow.  decline, fade,  fail,  faint,  flag.  languiiiii,  pitie.  sink,  wither.  See FALL.— Ant.:  blooni,  flourish,  grow,  riiHy,  recover,  revive. •- droop'er,  n.— droop'tiis,  pa.  Inctliilng;  btiiuiing  down- ward; harming  low;  a-s,  a   drooping  Jigtiro;  draupinn  clouds. —   droop'lng-Iy,  udr.— droop'Hort",  jj.  The  drtipwort. droop,  n.  A   sinking  or  hanging  down;  a   drooping,  or  a drooping  position;  a.s,  a   droop  of  the  .whouldcrs. droopt,  pp.  Drooped.  S,  S.
=== LKT/none ===
=== MON خوک ===
58261:خوک: 05 (.) (جان.) پستانداری از راستة 
MON_part1.txt:58261:خوک: 05 (.) (جان.) پستانداری از راستة
```


## [2026-09-14T03:15:52.917Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '58258,58268p' MON_part1.txt\necho \"=== abadis سیفلیس ===\"\ngrep -n -A4 -i \"معین\" /home/sfmqrb/git/rishe/data/verification/sources/web/e5aa586b0584b30f.txt | head -30\necho \"=== WEB hog full ===\"; sed -n '91263,91268p' WEB_vol1.txt"
}
```


### [2026-09-14T03:15:53.030Z] TOOL RESULT

```
و امیدواری» بیم و امید. 

خوک: 05 (.) (جان.) پستانداری از راستة 
سم‌داران که تیره خاصی بنام تبر؟ خوکان 
بوجود اورده. این جانور در هر دست و با 
دارای ۴ انگشت است و همه چیز می‌خورد. 
بدانش دارای چربی بسیار و پوستش ضخیم و 
دارای مو است. خ وک وحشی: (جاذ.) 
گونه‌ای خوک که دارای جهةٌ سنگین و بینی 
پهن است و در جنگل‌های باتلاقی می‌زید و 
=== abadis سیفلیس ===
18: سیفلیس. ( فرانسوی ، اِ ) سفلیس. سیفیلیس. مرض عفونی وساری که به ارث بطور مادرزادی به افراد منتقل میشود. عامل این ناخوشی باسیلی است مارپیچی بنام ترپونم پال این مرض بطور غیرمستقیم از افراد مبتلی به افراد سالم قابل سرایت است. کوفت. ( فرهنگ فارسی معین ). 
19-
20- فرهنگ فارسی
21-
22- ( اسم ) مرضی عفونی و ساری که به ارث به طور مادرزادی به افراد منتقل میشود عامل این ناخوشی باسیلی است مارپیچی به نام ترپونم پال . این مرض به طور مستقیم از افراد مبتلی به افراد سالم قابل سرایت است کوفت . 
--
24: فرهنگ معین
25-
26- [ فر. ] (اِ. ) بیماری واگیر که میکروب آن از طریق مقاربت و معاشرت با مبتلایان به سیفلیس سرایت می کند. این مرض به طور مادرزادی به افراد منتقل می شود، کوفت ، آبله فرنگی . 
27-
28- فرهنگ عمید
--
71: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
72-
73- لینک ها 
74-
75- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
=== WEB hog full ===
hog, n.; pl. hogs or hog, {ME. hog, hoge, hogge, a gelded hog.]
1. a pig; especially, a castrated boar or full- grown pig raised for its meat.
2. by extension, any animal resembling the hog, as the peccary.
3. a greedy, gluttonous, selfish, coarse, or filthy person. [Colloq.]
4. (a) a young sheep not yet shorn; (b) a year-old bullock; (c) a young colt. {Scot. and Brit. Dial.]
5. akind of scrubbing broom for scraping a ship’s bottom under water.
```


## [2026-09-14T03:16:05.668Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['KLN']['page_offset']);print(d['AHD'].get('page_offset'));print(d['IEC']['page_offset'])\"\ncd refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('ff before 37911:', '\\n'.join(lines[:37911]).count('\\f'))\nprint('ff before 18297 (hyena):', '\\n'.join(lines[:18297]).count('\\f'))\nEOF"
}
```


### [2026-09-14T03:16:07.054Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
ff before 37911: 827
ff before 18297 (hyena): 405
```


## [2026-09-14T03:16:19.359Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (826,827,828):\n    p=pages[i]\n    print('=== leaf',i, repr(p[:120]), '...', repr(p[-120:]))\nEOF"
}
```


### [2026-09-14T03:16:20.374Z] TOOL RESULT

```
=== leaf 826 'genus  of  plants,  the  skunk cabbage  (bot.) —  ModL.,  shortened  from  *Sym- ploco-carpus  (see  haplology),  fr.  G' ... '  court  of  justice,  advocate’,  fr.  auv  (see  syn-) and  Slxrj,  ‘custom,  usage;  judgment,  justice’, which  is  '
=== leaf 827 'cogn.  with  L.  dicere,  ‘to  show,  tell’.  See diction  and  words  there  referred  to  and  cp.  esp. dicast.\nDeriv' ... 'one  who deals  (with  a  certain  topic)’.  See  -logy.\nDerivative:  syphilolog-ist,  n.\nsyphilous,  adj.,  syphilitic.'
=== leaf 828 '  —  A  hybrid  coined  fr. syphilis  and  -ous,  a  suff.  of  Latin  origin.\nsyren,  n.  —  See  siren.\nSyria,  n.,  n' ... 'mbr.  tafle,  ‘on  the board’;  of  uncertain  origin.  Cp.  tabellion,  ta¬ bleau,  tablier,  tabula,  tabula  rasa,  e'
```


## [2026-09-14T03:17:31.522Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor tgt in (3323,):\n    ff='\\n'.join(lines[:tgt]).count('\\f')\n    print('rist-axez leaf',ff,'printed ~',ff-8)\n# find axistan\nimport re\nfor i,l in enumerate(lines):\n    if 'āxistan' in l or 'axistan' in l or 'dxistan' in l:\n        print(i, l[:200])\nEOF"
}
```


### [2026-09-14T03:17:32.638Z] TOOL RESULT

```
rist-axez leaf 186 printed ~ 178
818 axistan [hstn'; KDMWM-tn']  dzéz- Phyc-, KDMWN-] to stand up 1418. 3217. 33; apar ~ id. 233-74, passim; apde = to rise from the dead 105'7. — Ps. ^hstny hyc-; MPrs ’zystn ’xyz- (S, A-H I); < ā- + BP v
3322 rist-āxēz [lyst?hyc'] the resurrection of the dead 12?5, 6411-13, 7118. 7610. 8326, 8821. 91°. 1057. 12022. — From rist (g. v.) + Gxéz, pres. st. of dxistan (g. v.); Paz. rist-@xeZ (and other spelling
6277 xistan: axistan makas: *macah pätkös: pätkust razmik āyozišn: äyöz- *takile: kurušk
```


## [2026-09-14T03:17:39.017Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nff='\\n'.join(lines[:818]).count('\\f')\nprint('axistan leaf',ff,'printed ~',ff-8)\nprint(lines[818][:400])\nEOF\necho \"=== BRT hak / haxs lemma ===\"\ngrep -n \"haxs-\\|hak-\\|nachfolgen\\|sich anschliessen\\|sich  anschliessen\" BRT.txt | head -15"
}
```


### [2026-09-14T03:17:40.188Z] TOOL RESULT

```
axistan leaf 49 printed ~ 41
axistan [hstn'; KDMWM-tn']  dzéz- Phyc-, KDMWN-] to stand up 1418. 3217. 33; apar ~ id. 233-74, passim; apde = to rise from the dead 105'7. — Ps. ^hstny hyc-; MPrs ’zystn ’xyz- (S, A-H I); < ā- + BP vistan [hstn'] x&- [hyc-];
=== BRT hak / haxs lemma ===
6172:•  j.,  g.  ato-Bhak-  Adj.  (auch  fem.)  '*  'von A/a  begleitet':  yazattm  'ahaHm  Y.  41. 3'>.      2)  'der  Geiechtigkeit,  Rechtschaflen-
6427:•  j.  asiä.hak-  Adj.  'der  Asay  anhängend, ergeben':  tDttß . .  'JiSgit  (NSn.)  Srmaili/.- hägtt  Y.  $8- 1-  a)  NSn.  'kägst  als  Adv. 'in  Ergebenheit  gegen  A':  vTspaica  alte 'hsgst  ärmaitii.hägft  (zbayemify  yazama- daEca  "und  all  diese  (rufe  ich  an)  in  Er- gebenheit gegen  A.  und  Ä.,  und  wir  beten sie  an"  Y.  -]!.  ii.
6429:•  j.  asi§.häg9t  Adv.:  s.    'hak-. j.  asuiya  F.  g:  lies  usibya. j.  astar)  V.  /.  3  PüZ.;  s.  'sak-  mit  No.   1.
7346:•  g.  änuä.hak-  Adj.  (auch  fem.)  'der Reihe  nach  sich  anschliessend,  von  einem zum  andern  hingehend"';  'haxi  (NSf.) *ärmaitii  mainyü  *p?r}saits  ytdrä  mae>ii (sd.)  Y.J/.12.
7435:•  j.  ärmaitiä.hak-  Adj.  'der  Arm.  an- h^gend,  ergeben':  mmS  . .  asis.hiig>t 'kägit  (NSn.)  Y.5^.1.  a)  ASd.  'ItS^i als  kAs.:  'in  Ergebenheit  gegen  Ärm.\ vispaica  aSe  ans.h/fgtt  (sd.)  °hilg»t  yaza- mädaica  Y.  ji.  11.
7437:•  j.  iirtnattiä,häg3t  Adv.:  s.  -hak-.
11209:•  j.  Öanra-Dhak-  Adj.  (auch  fem.)  "was mit  der  Weide  zusammen,  auf  der  (zuge- wiesenen) Weide  heimisch  ist,  von  den domestizirten  Landtieren*';  gäus  yä  'äxs Yt/0.38;  —  ratavö  'Sca  (AP.)  Vr.2.1; —  vTspqmca  gqm . .  ravanaratamia  'ä^asca "all  Getier,  . .  das  in  der  Freiheit  haust, und  die  auf  der  Weide  heimischen  (Tiere)" Y.  71. 9;  —  ratavS  'äcqm  Vr.  /.  i ;  —  ururtJ .  .  'ä(qm  YL  y.  74.
11230:AbleiL  (s.  j'a-^J./ariaya-).  —  Zum  V.  ii-ar-.  — Vgl  np.  -Sir  (woiu  GlrPH.  f  b.  192)3),  gr. «■oXoC  -J  tUTaßißhyuni  y^  tl(  naTaaittpäi (HeSVCH).  —  Pü.!  tarlär  r  'factor  es'.  — •)  Die  Wortstellung  ist  anl^llig;  daher  auch die  Bed.  des  Worts  unsicher.  —  ')  Wegen np.  iiirldan  s.  zu  caiiraahak-.
12678:Et.?')  —  PiL:  te  äH  iöini/rt/iSr')--aAnonöf - ätnöxlun  i  den  i  vrh  pa  siu^an  u  hmiht.  — «)  Falsch  KZ.  ja  528,  36.  140;  s.  noch  No.  2.  — )>  Also  tu  ^dab-;  die  an  Pü.  sich  anschliessen- den Oberseliungen  -  zuletzt  von  Dst.  und Mills  -  gehen  keinen  Sinn.
19384:•  g.  hoA  eukL  Part,  der  Hervorhebung; i)  dem  ersten  Hochton  des  Versteils  sich anschliessend;  a)  hinter  Pron.:  ivlJ  ma  nH sravä  mannäat  (sd.)  Y._^2. 10;  —  yS  mä dngvä  %wä  lava  (sd.)  paitijntg  Y.  44- 12;  —  *ys  *mä''>  vas^ml  *liäjcsa%rJm  Y. 2p- 9;  —  tai^t  «ä  msrtnd?n  (sd.)  jystüm Y._^2.  n.  b)  hinter  Nom.:  asahyä  mä yava{  isäi  manyät  (sd.)  Y.  43. 9 ; — äkästSng (sd.)  mä  nilqsyä  da%Sm  ääkvS  Y.  50. 2.  c)  hinter  Praev.:  apn  ma  litim afiayantä  (sd.)  ..  Y.J2. 9.  d)  hinter Verb.:  yä  . .,  JÄ«ff(sd.)  wJ  tä  tsi  t  ' tnanaaAa  Y.  46. 9.  2)  sonst,  hinter /iya(:  at  tU  rnui  äai/  (Sp.  6j  2  a.)  altm hyai  ma  saozaomX  'V. 43.10;  —  para Ayai  mä  ya  mSng  p?r3%ä  (sd.)  jimaitX  Y. 48.2,
19394:—  manS  J'ur<^tnasds  upasiam  baratuv . .  Uta  imam  dahySum  . .  pätuv  D.  4. 3 ;  — vas^i  (^urJ'mazdäkJ'  manacS  däray<^- vaAaui"D.4.2;  —  iya*  mana  kartam  utä fyc^maiy  /iS'ö*  kartam  X.7.4;  —  avam käram  .  .  hyj*  mana  naiy  gaubataiy*^ Eh.2. 6,  j,3,  14;  2.14.  zu  1  b):  J'urt^- masda  ya'ha  avaina*  imäm  bümim  *yau- d<rHm  (sd.)  pasüvt^dim  martä  fräbart^ mam  (s.  i  i  b)  . .  D.  61 4 ;  — pasavo^  dahyUui mana  abavJ'  Bh.j.  a,  4,  iz.  zu  3): kari^  hy<^  hamüi'iyc^  mana  naiy  gau- &ataiy*'>  Eh.  2.  7,  10.  b  n)  im  jAw.; zu  I  a):  Hat . ,  mana  asti  vjjaymift^m  . . attivam  asti  vJmamiiftim  Yt  /.  a;  — s.  noch  bei  a.  zu  1  b):  mana  raya  .  . pawasla  staorüta  upairi  tarn  vTcarmta Yt  5.  89;  /.  a6  (?).  zu  a):  ya%a  .  . Os  zaofff  mana  yat  ahurakt  matda  Yt ig.  8a;  V.  ig.  14;  —  ar»hu^  y3  mana yai  ahurahe  mazdä  P.  40;  —  zugleich zu  1  a):  manada  yatmm  yat  ahurahe mazda  a^rasca  P.Jp.  11)  schwach- tonige  Formen  stehen  a)  enklitisch i)  hinter  dem  ersten  Wort  des  Satz-  oder Versteils,  von  dem  sie  aber  a)  durch  ein andres  enklitisches  Wort  getrennt  sein können;  a)  hinter  einem  Praenomen; 3)  selten  in  anderer  Stellung;  b)  pro- klitisch5>;  das  hochbetonte  Wort,  an  das sie  sich  anschliessen,  hat  keine  bestimmte Stellung.  I)  Akk,;  a)  im  Ap.;  zu  a  1): avada  mam  cita  amanayJ"  Eh.  2. 6;  — y^a  mam  kame^  Bh.4.4;  D. ö. 4, 17-3)
26055:1)  'vereinigen  mit—,  anschliessen  an (Instr.):  y!  damqm  vohä  *s3rjstä^''  mana- tahä  ärmatöii  kasclt  .  .  huzSntus  (sd.) "wer  immer  sein  Ich  mit  VM.  vereinigt . ." Y.^ys''.  2)  Med.  'sich  vereinigen  mit  -, sich  anschliessen  an  — ;  es  halten  mit  — ' (Instr.);  aHfys  mazda  ahurB  sartmns voha  manarihä  xsä^räi  hacä  patti.mraot asa  hui.haxä  :^Snvaiä  "ihnen  erteilte MAh.,  der  mit  VM.  vereinte,  mit  dem lichten  A.  wohlbefreundete,  durch  Xs.  die Antwort"  Y.^2.  23>;  —  a  vi  *g3us.ä  (sd.) hSm.yantü  ySi  v!  fyao%an3is  sännte  ahurs aiä  *hisva  ux^aisvat>A7u/mafiaisAff"..die es  in  den  Taten,  in  der  Zunge  Reden mit  euren  Worten,  o  AA.  und  As'a,  mit denen  des  VM.  halten"  Y.5/.  3*'.
27748:ai.  hävate,  jukSmäii,  }6kaväi,  ki/äyali;  mp.  vgl- äiiäj^n.  —  Pü. :  Landau,  Sü. ;  {satn^hväna- yiium,  äkärayiluvi;  frätliayilum;  a,  noch No.  5,  g.  —  >)  D.  i.  ä-'Erweitemng;'  au  an--; ■.  Bthl.  Stud.  2.  izi.  Daiu  -siä/a;  ferner tiä/ar-  nnd  duiatxbä:  —  ')  In  taoiäuyt,  3SPM. (für  'zvi,  S  36S.  ig).  Ist  die  Fonn  acht  (vgL IF.  4.  tz),  so  laut»  lie  durch  Kontamination von  zaiKU',  Pracs.  7  und  *iäu',  Piaes.  5  ent- itanden  «ein.  —  3)  sbaytmi  .  .  yatamaidf, 'madaeia:  der  Numerus  wechselt;  ecst  spricht der  Zaolar  allein,  dann  die  Ralav  (oder  U/^l- srcKlary   S.  noch  aÜi.hak-  No.  I.  —  *)  Them.
28820:•  j.,  g.  'hak-  V.  'sequi*.  Fracs.  1  Äai-, si;  2  haca-,  5  *his.hak-\  hisk-,  15  haxsa-, 16  (Des.)  hixia'^,  2  +  24  hacaya-,  30 (Her.)  häcaya:  —  PPfP.  'haxta-;  Inf. haxtSit.
28823:'hak- 2  b
```


## [2026-09-14T03:17:50.944Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"خاستن\\|رستاخیز\\|خیزیدن\" FSF_pages.txt | head -10\necho \"=== IRN? ===\"\ngrep -n \"خاستن\" incoming/IRN/IRN_pages.txt 2>/dev/null | head -5"
}
```


### [2026-09-14T03:17:51.040Z] TOOL RESULT

```
712: ‫زمانهدگر گوتاتر شدبه نگ‬                                      ‫برینگونه از جای برخاستند‬
714:                 ‫همه دل پر از بیم برخاستند‬      ‫)‪(1-11-4۷‬‬
4696:           ‫به کسر حرف سین تلفظ می‌کنند)‬                        ‫برخاستن‪ ,‬دمیدن وزیدن‪:‬‬
7682:‫چه جای بهغم نشستن و خاستن است‬                  ‫بهنزد کس این هر دو را چاره نیست‬
13273:                 ‫سهراب دربار؛ رستم گوید‪:‬‬          ‫مخفف رستاخیز‪ .‬پهلوی ریست‌اخز‬
13276:‫که‌بامن همی گردد اندر نبرد‬                        ‫ریست به‌معنی مرده و خیز از خاستن؛‬
13277:     ‫زبالای من نیست بالاش کم‬                      ‫یعنی برخاستن مردگان (یا به گفتة اسدی‬
13450:          ‫دو روز اندر آن کار شد روزگار‬              ‫روز واپسین روز رستاخیز» روز شمارش‬
=== IRN? ===
3356:بهترین جا به‌جستجوی زمین‌ها و شهرستان‌ها برخاستند که بهترین آب و هوا را
```


## [2026-09-14T03:17:55.870Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=13273 && /\\[pdf page/ {t=$0; l=NR} END{print l,t}' FSF_pages.txt\nsed -n '13268,13282p' FSF_pages.txt"
}
```


### [2026-09-14T03:17:56.995Z] TOOL RESULT

```
                                                        ‫همراران اگر نوبهاران و تیر‬
 ‫(‪)۵-۵۶-۶۳۸‬‬                           ‫‪۱‬‬
                                   ‫رسن ردن‬    ‫برآید نه بیمارگرددنه پیر‬

                   ‫ربیاسمان اندازه گرفتن‪:‬‬                                   ‫رستخیز (بازبر اول)‬
                 ‫سهراب دربار؛ رستم گوید‪:‬‬          ‫مخفف رستاخیز‪ .‬پهلوی ریست‌اخز‬

       ‫به هومان چنین گفت کاین شیرمرد‬          ‫(وست ‪-‬هوگ ‪ )۵۳۱‬مرکب از‬                ‫‪2۵:۲‬‬
‫که‌بامن همی گردد اندر نبرد‬                        ‫ریست به‌معنی مرده و خیز از خاستن؛‬
     ‫زبالای من نیست بالاش کم‬                      ‫یعنی برخاستن مردگان (یا به گفتة اسدی‬
‫به رزم اندرون دل ندارد دزم‬                        ‫توسی «روز انگیختن»‪ :‬ز یزدان و از روز‬
     ‫برو كتف و يالش همانند من‬                     ‫انگیختن «بیندیش وبس کن ز حون‬
 ‫توگویی که داننده برزد رسن‬                                          ‫ریختن)؛ روز قیامت‪:‬‬
 ‫(‪)۲-۲۳۲-۹۱۸‬‬                                              ‫به کین من امروز تارستخیز‬
                           ‫رطل (بروزن سطل)‬        ‫نبینی جز از گرز و شمشیر تیز‬
```


## [2026-09-14T03:18:02.122Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('ff before 13273:', '\\n'.join(lines[:13273]).count('\\f'), 'total ff', t.count('\\f'), 'lines', len(lines))\nEOF\ngrep -n \"pdf page\" FSF_pages.txt | head -2"
}
```


### [2026-09-14T03:18:03.281Z] TOOL RESULT

```
ff before 13273: 266 total ff 484 lines 23569
```


## [2026-09-14T03:20:00.788Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg487.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/487.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/487.png"
}
```


### [2026-09-14T03:20:00.865Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 76588 Sep 13 23:20 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/487.png
```


## [2026-09-14T03:20:03.971Z] TOOL CALL #67: Bash

```json
{
 "command": "sed -n '40,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:20:04.016Z] TOOL RESULT

```
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


## [2026-09-14T03:27:59.082Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-487.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 487,\n \"book_page\": 457,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Su 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *suH- (*sū-s, gen. *suH-ós) 'pig, swine'\",\n   \"note\": (\"Pokorny 1038-1039 has exactly this root: 'Root / lemma: su-s, suu-os — Meaning: pig, swine ... Page(s): \"\n            \"1038-1039', with Av. hū, Gk. hys/sys and hyaina, Lat. sūs, Goth. swein, Celtic *sukko-, MP xūk. \"\n            \"Watkins/AHD p.1034 of our scan: 'sū-. Pig. Contracted from *suə-; probably a derivative of seuə-... [Pok. su-s 1038.]'. \"\n            \"Modern citation form is *suH- (Wiktionary), noted as conspicuous for occurring only in the zero grade and possibly \"\n            \"derived from *sewH- 'to give birth'. Nourai's language label, form and gloss are all right; 'wild boar' is the \"\n            \"Indo-Iranian specialisation (Av. hū-, Skt. sūkara-) rather than a PIE nuance. The chart is a faithful digest of the \"\n            \"AHD sū- article: swine (Gmc.), hog (Celtic), soil (Latin), hyena (Greek) are AHD's own four English outcomes.\"),\n   \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *suH- (صورت اسمی *sū-s) به معنی «خوک، گراز» است؛ پوکورنی در صفحهٔ ۱۰۳۸–۱۰۳۹ همین ریشه را \"\n               \"با شواهد اوستایی hū، یونانی hŷs/sŷs، لاتین sūs، گوتی swein و فارسی میانهٔ xūk آورده است و واتکینز (AHD) نیز آن را \"\n               \"با ارجاع «Pok. su-s 1038» تکرار می‌کند. در ویکی‌واژه یادآور شده‌اند که این ریشه تنها در درجهٔ صفر (zero grade) به کار \"\n               \"رفته و شاید از *sewH- «زاییدن» آمده باشد. ادعای نورایی دربارهٔ خودِ ریشه، برچسب زبانی و معنای آن درست است؛ تنها \"\n               \"معنای «گراز» ویژگی شاخهٔ هندوایرانی است نه معنای آغازین.\"),\n   \"sources\": [W+\"Reconstruction:Proto-Indo-European/suH-\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:1038\", \"status\": \"supports\",\n      \"note\": \"POK_full.txt l.84545ff: 'Root / lemma: su-s, suu-6s / Meaning: pig, swine / Material: Avestan hu (Gen. Sg. for *huvo) \\\"swine\\\"; gr. ho, sos ... (therefrom uaiva f. \\\"Hyane\\\") ... Latin sus, suis \\\"swine\\\" ... Gothic swein ... Middle Persian xuk ... Celtic *sukko- ... Page(s): 1038-1039'. Exactly the chart's root and most of its branches.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 512-513 (WLD_Bd2_1927_dli_106624_djvu.txt l.33251)\", \"stance\": \"supports\",\n      \"note\": \"'SU- (*su-s, *suu-6s) \\\"Schwein, Sau\\\". Av. hu- \\\"Schwein\\\" (Bthl. BB. 15, 40); gr. hys, sys \\\"Schwein\\\" (davon gr. hyaina \\\"Hyane\\\") ... lat. sus, suis \\\"Schwein\\\" ... got. swein, aisl. svin, ags. ahd. swin ... ai. sukarah \\\"Eber, Schwein\\\" ... cymr. hwch ... air. socc.'\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. sū- (AHD_watkins1985.txt l.1034)\", \"stance\": \"supports\",\n      \"note\": \"'sū-. Pig. Contracted from *suə-; probably a derivative of seuə-. 1. Suffixed form *suə-ino- in Germanic *swīnam in Old English swin, swine: SWINE. 2. Celtic expressive form *sukko-, swine, snout of a swine, plowshare... 4. Latin sūs, pig: SOIL². 5. Greek hus, swine: HYENA; HYOSCINE. [Pok. su-s 1038.]'\"},\n     {\"src\": \"KLN\", \"where\": \"s.v. sow, n. (KLN_1966.txt l.36033)\", \"stance\": \"supports\",\n      \"note\": \"'... cogn. with OI. sūkaraḥ, \\\"wild boar, swine\\\", Avestic hū, \\\"wild boar\\\", Toch. B suwo, Gk. hys, sys, Alb. thi, L. sus ... Olr. socc ... Cp. hog, hyena, socket, soil, \\\"to make dirty\\\", ... Sus, swine, and the first element in sybotic, syphilis.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"hu 2; hu-xerpa\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Av. hū- 'Schwein, Sau' is Bartholomae's own lemma (AiW, s.v. hū-, in the h-columns near 1810; BRT.txt l.30138: \"\n        \"\\\"j. hū- 'Schwein, Sau': ... vindrafno hū (GS.) kǝhrpa varāzahe .. arš̥no '.. in der Gestalt eines Ebers ..' Yt.14.15\\\"). \"\n        \"It continues PIE *suH- with the regular Indo-Iranian change of initial *s- to h- before a vowel (as in *septm̥ > Av. hapta) \"\n        \"and *uH > ū. The second item is the weak point: 'hu-xerpa' is not an Avestan compound but the two-word phrase of that very \"\n        \"passage, hū kǝhrpa (varāzahe) 'in the shape (kǝhrp-, instr. kǝhrpa) of a boar', which Horn no. 510 quotes in abbreviated form \"\n        \"as 'aw. hū kehrpa \\\"in Ebergestalt\\\"' — Nourai has run Horn's citation together into a single lemma. (The cross-reference \"\n        \"☞Sek is to kǝhrp- 'form, body', which is correct.) Note also the homophonous Avestan prefix hu- 'good' (< PIE *h1su-), a \"\n        \"different morpheme that must not be confused with hū- 'pig'.\"),\n     \"derivation_fa\": (\"در اوستایی hū- «خوک، گراز» واژه‌ای است که بارتولومه در فرهنگ ایرانی باستان خود آورده و شاهد آن بند ۱۵ از یشت ۱۴ است. \"\n        \"این واژه بازماندهٔ *suH- هندواروپایی است؛ «س» آغازین هندواروپایی در ایرانی باستان پیش از واکه به «ه» بدل شده (مانند *septm̥ که در \"\n        \"اوستایی hapta شده است). اما «hu-xerpa» واژهٔ مرکب نیست، بلکه همان عبارت دو کلمه‌ای hū kǝhrpa (varāzahe) «در پیکرِ گراز» است که هرن \"\n        \"(شمارهٔ ۵۱۰) به‌اختصار «hū kehrpa = در ریخت گراز» نقل کرده و نورایی آن را یک مدخل واحد پنداشته است. هشدار دیگر آنکه پیشوند اوستایی \"\n        \"hu- «نیک» (از *h1su-) تکواژی جداست و نباید با hū- «خوک» اشتباه شود. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/suH-\"],\n     \"ref_check\": [\n       {\"ref\": \"POK:1038\", \"status\": \"supports\",\n        \"note\": \"POK_full.txt l.84547: 'Material: Avestan hu (Gen. Sg. for *huvo) \\\"swine\\\"' — the Avestan word and its descent from *sū-s are exactly Pokorny's, on the cited page.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW s.v. hū- (BRT.txt l.30138)\", \"stance\": \"partial\",\n        \"note\": \"'j. hū- \\\"Schwein, Sau\\\": ahmāi .. ajasat̰ vindrafno hū (GS.) kǝhrpa varāzahe .. aršno \\\".. in der Gestalt eines Ebers ..\\\" Yt.14.15' — has hū- 'pig' but shows kǝhrpa varāzahe as a separate phrase, not a compound *hu-kǝhrpa-.\"},\n       {\"src\": \"HRN\", \"where\": \"no. 510, p. 113 (HRN.txt l.4609-4612)\", \"stance\": \"supports\",\n        \"note\": \"'xūk \\\"Schwein\\\" ... aw. hū kehrpa \\\"in Ebergestalt\\\"; phlv. xūk (Bund.) ... skr. sūkara- \\\"Eber, Schwein\\\".' Horn is evidently Nourai's immediate source for 'hu-xerpa'.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 512\", \"stance\": \"supports\",\n        \"note\": \"'Av. hū- \\\"Schwein\\\" (Bthl. BB. 15, 40)' heads the material of the root.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"xŭk\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP خوک xūk 'pig' descends through MP xūg (Book Pahlavi hwk', Aramaic ideogram HZWLYA; Manichaean hwg) from \"\n        \"Proto-Iranian *huHka- (Wiktionary: *huHkáh), a k-suffixed *suH-k- beside Skt. sūkara-, Lat. sucula and Celtic *sukko-. \"\n        \"Initial PIr. *h- before the rounded vowel was strengthened to x- in Middle Persian (the same xʷ-/x- strengthening seen in \"\n        \"xwāhar, xšnūdan), and the MP final -g appears as -k in the New Persian spelling; Ossetic xuy and Kurdish xû continue the \"\n        \"same form. Pokorny already registers 'Middle Persian xūk' among the k-derivatives of the root, and Horn no. 510 (p. 113, \"\n        \"Nourai's citation) gives the whole chain. The chart's arrow jumps Avestan → Persian, skipping the Middle Persian stage.\"),\n     \"derivation_fa\": (\"«خوک» در فارسی نو از فارسی میانهٔ xūg (در پهلوی کتابی hwk'، با هُزوارش HZWLYA) و آن از ایرانی باستان *huHka- است؛ \"\n        \"این صورت با پسوند ‑k ساخته شده، همان‌گونه که سنسکریت sūkara- و لاتین sucula و سلتی *sukko- ساخته شده‌اند. «ه» ایرانی باستان پیش از \"\n        \"واکهٔ گردِ کشیده در فارسی میانه به «خ» سخت شده است (مانند xwāhar و xšnūdan) و «گ» پایانیِ فارسی میانه در املای فارسی نو «ک» نوشته \"\n        \"شده است؛ آسی xuy و کردی xû نیز از همین صورت‌اند. پوکورنی خود «فارسی میانه xūk» را در شمار مشتق‌های ‑k این ریشه آورده و هرن (شمارهٔ \"\n        \"۵۱۰، ص ۱۱۳) همهٔ زنجیره را ثبت کرده است. ادعای نورایی درست است؛ تنها حلقهٔ فارسی میانه در نمودار حذف شده است.\"),\n     \"sources\": [W+\"%D8%AE%D9%88%DA%A9\"],\n     \"ref_check\": [\n       {\"ref\": \"HRN:113\", \"status\": \"supports\",\n        \"note\": \"Horn, Grundriss no. 510, printed p.113 (HRN.txt: the marker '— 113 —' stands at l.4595, no. 510 at l.4609): 'xūk \\\"Schwein\\\" ... aw. hū kehrpa; phlv. xūk (Bund.), xūkōak bezw. xūbadak; skr. sūkara- \\\"Eber, Schwein\\\"; kurd. xū; oss. xuy; bal. hūk.' Exactly Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. xūg (PHD.txt l.661; addenda l.125)\", \"stance\": \"supports\",\n        \"note\": \"'xūg [HZWLYA < A hzyr; hwk' | N ~] pig'; the addenda add 'hūg [HZWLYA < A ḥzyr'; hwk' | M hwg, N xūg] pig'.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien (HUB.txt l.7638)\", \"stance\": \"supports\",\n        \"note\": \"'xūk \\\"Schwein\\\" = phl. xūk 61. and Ind. 53 = zd. hu-'.\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, خوک (ARY_pages.txt [pdf page 254-255])\", \"stance\": \"supports\",\n        \"note\": \"The entry خوک lists اوستایی hū, پهلوی xūk, اوستی, کردی, سانسکریت sūkara, یونانی, لاتین sūs, گوتیک, سلتی and cites برهان قاطع ۷۹۴.\"},\n       {\"src\": \"MON\", \"where\": \"Mo'in, خوک (MON_part1.txt l.58261)\", \"stance\": \"silent\",\n        \"note\": \"'خوک: (جان.) پستانداری از راستهٔ سم‌داران...' — a definition only, no origin tag (the word being inherited, Mo'in marks nothing).\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Greek\", \"words\": \"sŭs; sŭs-philos; huaina\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Gk. ὗς / σῦς (hŷs / sŷs) 'swine' is the direct athematic reflex of *suH-s, the h-/s- doublet reflecting dialectal \"\n        \"retention versus the normal Greek loss of initial *s-; ὕαινα (húaina) 'hyena' is ὗς plus the feminine suffix -αινα, literally \"\n        \"'the sow-like beast', so named for its bristly mane (Klein s.v. hyena; Walde-Pokorny II 512 'gr. hyaina \\\"Hyäne\\\"'). Both are \"\n        \"sound. The third item is not: *sŭs-philos 'friend of swine' is NOT an attested Greek word. It is the etymology conventionally \"\n        \"proposed for the invented Neo-Latin name Syphilus (node #4), and Etymonline (citing the Century Dictionary) records that \"\n        \"Fracastoro's motive is unknown and that 'syn- + philos' and Ovid's Sipylus are equally 'usual conjectures'. Nourai's breve in \"\n        \"'sŭs' is also wrong: the Greek vowel is long (σῦς).\"),\n     \"derivation_fa\": (\"یونانی ὗς/σῦς (hŷs/sŷs) «خوک» بازماندهٔ مستقیم *suH-s است؛ دوگانگی h-/s- بازتاب نگه‌داشت یا افتادنِ «س» آغازین در \"\n        \"گویش‌های یونانی است. ὕαινα (húaina) «کفتار» از همان ὗς با پسوند مؤنث ‑αινα ساخته شده، یعنی «جانورِ خوک‌مانند»، و کلاین آن را به \"\n        \"یال زبرِ کفتار نسبت می‌دهد. اما جزء سومِ این خانه، یعنی *sŭs-philos «دوستدارِ خوک»، واژهٔ یونانی ثبت‌شده‌ای نیست؛ تنها ریشه‌شناسی \"\n        \"پیشنهادی برای نامِ ساختگی و لاتینِ Syphilus است و اتیمانلاین به نقل از فرهنگ سنچری یادآور می‌شود که انگیزهٔ فراکاستورو ناشناخته \"\n        \"است و حدس‌های دیگری (syn- + philos یا Sipylus در دگرگونی‌های اوویدیوس) نیز هست. پس این خانه با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/hyena\", \"https://www.etymonline.com/word/syphilis\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"Watkins 1985 s.v. sū- has '5. Greek hus, swine: HYENA; HYOSCINE' — it supports Gk. hys and hyena but says nothing about any Greek *sys-philos.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. hyena (KLN_1966.txt l.18403)\", \"stance\": \"supports\",\n        \"note\": \"'hyena, hyaena, n. — L. hyaena, fr. Gk. huaina, \\\"hyena\\\", lit. \\\"sow\\\" formed with the fem. suff. -aina, fr. hys, gen. hyos, \\\"swine\\\" ... The hyena was so called in allusion to its bristly mane.'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hyena (SKT.txt l.9016)\", \"stance\": \"supports\",\n        \"note\": \"'Hyena, Hyaena, a sow-like quadruped. (L.—Gk.) L. hyaena. — Gk. huaina, a hyena; lit. \\\"sow-like.\\\" — Gk. hys, a sow, cognate with E. Sow; with fem. adj. suffix -aina.'\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 512\", \"stance\": \"supports\",\n        \"note\": \"'gr. hys, sys \\\"Schwein\\\" (davon gr. hyaina \\\"Hyane\\\")' — and no *sys-philos anywhere.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"Syphilus; hyaena\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Two very different things share this box. (a) Lat. hyaena is the ordinary Latin transcription of Gk. ὕαινα \"\n        \"(y for upsilon, ae for αι), the source of OFr. hiene and of English hyena — certain. (b) 'Syphilus' is Neo-Latin, not \"\n        \"classical: the Veronese physician Girolamo Fracastoro (1483-1553) published the hexameter poem 'Syphilis sive Morbus \"\n        \"Gallicus' at Verona in 1530, whose shepherd Syphilus is the first man struck by the disease, and Fracastoro then used the \"\n        \"word as a generic disease name in 'De Contagione' (1546). Klein derives the name from Gk. σῦς + φίλος 'friend of swine', \"\n        \"which is exactly Nourai's chart; but Etymonline reports that 'why he chose the name and what it meant to him are unknown', \"\n        \"with 'syn- \\\"with\\\" + philos' and Ovid's Sipylus, son of Niobe, as rival conjectures. The chart's own gloss is therefore an \"\n        \"accurate summary of Klein but overstates the certainty of the Greek etymon.\"),\n     \"derivation_fa\": (\"در این خانه دو چیزِ یکسره متفاوت کنار هم آمده‌اند. نخست، لاتین hyaena صورت آوانویسیِ معمولِ یونانی ὕαινα است \"\n        \"(y برای اوپسیلون و ae برای αι) و از راه فرانسهٔ کهن hiene به انگلیسی hyena رسیده؛ این بخش قطعی است. دوم، Syphilus واژه‌ای \"\n        \"لاتینِ نو است نه کلاسیک: ژیرولامو فراکاستورو، پزشکِ ورونایی، در سال ۱۵۳۰ منظومهٔ «Syphilis sive Morbus Gallicus» را منتشر کرد \"\n        \"که در آن چوپانی به نام سیفیلوس نخستین قربانی بیماری است، و خود او در ۱۵۴۶ این واژه را نام عامِ بیماری کرد. کلاین این نام را از \"\n        \"یونانی σῦς «خوک» + φίλος «دوست» می‌داند و همین را نورایی آورده است؛ اما اتیمانلاین می‌گوید انگیزهٔ فراکاستورو ناشناخته است و \"\n        \"حدس‌های رقیبی هم (syn- + philos، یا Sipylus پسر نیوبه در اووید) وجود دارد. پس با احتیاط پذیرفتنی است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/syphilis\", \"https://www.etymonline.com/word/hyena\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:1561\", \"status\": \"supports\",\n        \"note\": \"Klein s.v. syphilis (KLN_1966.txt l.37911, scan leaf 827): 'syphilis, n. ... ModL., from the title of the work by Girolamo Fracastoro, Syphilis sive de morbo Gallico ... published at Verona in 1530; so named after the hero Syphilus, a shepherd whose name lit. means \\\"friend of swine\\\", fr. Gk. sys (gen. syos) = hys (gen. hyos), \\\"swine\\\", and philos, \\\"friend\\\".' Word-for-word Nourai's box. (Our scan carries no printed page numbers; the leaf-to-page formula puts this nearer p.1630 than p.1561, so the page figure may be slightly off.)\"},\n       {\"ref\": \"AHD:1306\", \"status\": \"not_checked\",\n        \"note\": \"Nourai's AHD page numbers are for the 1975/76 New College Edition main dictionary, which is not open online; only the Watkins roots appendix is on disk (AHD_watkins1985.txt), and it has no 'syphilis' article.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. philo-, hyena, sow (KLN_1966.txt l.28525, 18403, 36033)\", \"stance\": \"supports\",\n        \"note\": \"'philo- ... Cp. philander, Philemon, philter, syphilis'; 'hyena ... L. hyaena, fr. Gk. huaina'; sow cross-refers to 'the first element in sybotic, syphilis'.\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hyena\", \"stance\": \"supports\",\n        \"note\": \"Confirms Lat. hyaena < Gk. huaina; Skeat has no syphilis entry.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"The empty French box is the transmission stage, and it is the right one: Neo-Latin syphilis was taken into \"\n        \"French as syphilis (in French medical use from the early 18th c., generalised in the 19th), and Latin hyaena gave OFr. hiene \"\n        \"> Fr. hyène. Persian borrowed the word from French, not from Latin or English — Mo'in tags سیفلیس '[فر.]' (French) and \"\n        \"Dehkhoda opens the entry '(فرانسوی، اِ)'. Nourai gives the box no forms and no reference, but the link it draws is correct.\"),\n     \"derivation_fa\": (\"خانهٔ خالیِ «فرانسوی» حلقهٔ میانجیِ وام‌گیری است و درست جای خود نشسته است: لاتینِ نو syphilis در فرانسه به صورت \"\n        \"syphilis پذیرفته شد (از آغاز سدهٔ هجدهم در متون پزشکی) و لاتین hyaena از راه فرانسهٔ کهن hiene به hyène رسید. فارسی این واژه را \"\n        \"از فرانسه گرفته است نه از لاتین یا انگلیسی؛ معین در برابر «سیفلیس» نشانهٔ «[فر.]» می‌گذارد و دهخدا نیز «(فرانسوی، اِ)» می‌نویسد. \"\n        \"نورایی برای این خانه نه صورتی آورده و نه ارجاعی، ولی پیوندی که رسم کرده درست است.\"),\n     \"sources\": [\"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%D9%84%DB%8C%D8%B3/\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"The box carries no refs= in the book (confirmed on the printed page, pdf p.487); nothing of Nourai's to check.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, سیفلیس\", \"stance\": \"supports\",\n        \"note\": \"فرهنگ معین: '[ فر. ] (اِ.) بیماری واگیر ... کوفت، آبله فرنگی.' — the '[فر.]' tag is Mo'in's own statement that the route is French.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. syphilis / hyena\", \"stance\": \"partial\",\n        \"note\": \"Klein takes English syphilis straight from Modern Latin and hyena through Old French hiene; he does not need a French stage for English, but the French form he cites (hiene) is the one that matters for the Persian branch.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Persian\", \"words\": \"sîflîs; seflîs\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Persian سیفلیس sīflīs, with the shorter variant سفلیس seflīs, is a modern medical loan from French syphilis, \"\n        \"part of the Franco-Persian technical vocabulary that entered Persian through the Dār al-Fonūn and the 19th-20th c. medical \"\n        \"schools. French [si.fi.lis] is rendered with سی- for the first syllable and ف for the French -ph- [f]; the unstressed second \"\n        \"syllable is syncopated in the popular سفلیس. Wiktionary lists سفلیس as the alternative form of سیفلیس; Mo'in marks the word \"\n        \"'[فر.]' and Dehkhoda '(فرانسوی، اِ) سفلیس. سیفیلیس ... کوفت'. The inherited Persian names are کوفت and آبلهٔ فرنگی.\"),\n     \"derivation_fa\": (\"«سیفلیس» و گونهٔ کوتاه‌ترش «سفلیس» وام‌واژه‌ای نو از فرانسهٔ syphilis است که در دورهٔ دارالفنون و مدارس پزشکی سدهٔ \"\n        \"سیزدهم و چهاردهم خورشیدی همراه انبوهی از اصطلاحات پزشکی فرانسوی وارد فارسی شد. تلفظ فرانسویِ [si.fi.lis] با «سی‑» در هجای نخست و \"\n        \"«ف» برای ph فرانسوی بازنویسی شده و در گونهٔ عامیانه هجای بی‌تکیهٔ دوم افتاده و «سفلیس» شده است. ویکی‌واژه «سفلیس» را گونهٔ دیگرِ \"\n        \"«سیفلیس» ثبت کرده، معین نشانهٔ «[فر.]» گذاشته و دهخدا «(فرانسوی، اِ)» نوشته است. نام‌های بومیِ این بیماری «کوفت» و «آبلهٔ فرنگی» \"\n        \"است. ادعای نورایی درست است.\"),\n     \"sources\": [W+\"%D8%B3%DB%8C%D9%81%D9%84%DB%8C%D8%B3\", \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%D9%84%DB%8C%D8%B3/\"],\n     \"ref_check\": [\n       {\"ref\": \"MON:1979\", \"status\": \"partial\",\n        \"note\": \"The entry is Mo'in's and says what the chart needs — MON_part1.txt l.82279 'سیفلیس: ... (پز.) مرضی عفونی و ساری ...', and the online Mo'in gives the origin tag '[فر.]'. The page number could not be verified: our local Mo'in is the 2-volume Adena reprint with its own pagination, and vajehyab/abadis print no page numbers.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"Mo'in, سیفلیس (MON_part1.txt l.82279; abadis 'فرهنگ معین')\", \"stance\": \"supports\",\n        \"note\": \"'[ فر. ] (اِ.) بیماری واگیر که میکروب آن از طریق مقاربت ... کوفت، آبله فرنگی.'\"},\n       {\"src\": \"ARY\", \"where\": \"Aryanpur, ریشه‌های هندواروپایی\", \"stance\": \"silent\",\n        \"note\": \"grep of ARY_pages.txt for 'سیفلیس' and 'سفلیس' returns nothing — Aryanpur's dictionary covers inherited Iranian vocabulary, not modern European loans.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"hyena, syphilis\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"hyena entered English in the mid-14th c. as hiene/hyena from Old French hiene, from Latin hyaena, from Greek \"\n        \"ὕαινα. syphilis was taken into English in 1718 directly from Fracastoro's Modern Latin title (Etymonline: 'infectious venereal \"\n        \"disease, 1718, Modern Latin, originally from the title of a poem'), so English did not go through French even though Persian \"\n        \"did — Nourai's single French box feeding both the Persian and the English branch is a simplification of the chart layout \"\n        \"rather than a claim about English. Watkins/AHD lists HYENA under sū-; Klein gives both chains.\"),\n     \"derivation_fa\": (\"واژهٔ hyena در میانهٔ سدهٔ چهاردهم میلادی از فرانسهٔ کهن hiene و آن از لاتین hyaena و یونانی ὕαινα به انگلیسی \"\n        \"راه یافت. اما syphilis در سال ۱۷۱۸ یکراست از عنوان لاتینِ نوِ منظومهٔ فراکاستورو به انگلیسی رفت و از مجرای فرانسه نگذشت؛ پس \"\n        \"خانهٔ واحدِ «فرانسوی» در نمودار که هم به فارسی و هم به انگلیسی پیکان می‌دهد، ساده‌سازیِ ترسیمی است نه ادعایی دربارهٔ انگلیسی. \"\n        \"واتکینز در پیوستِ ریشه‌های AHD واژهٔ HYENA را زیر sū- آورده و کلاین نیز هر دو زنجیره را ثبت کرده است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/hyena\", \"https://www.etymonline.com/word/syphilis\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. sū-: '5. Greek hus, swine: HYENA; HYOSCINE'; the index line confirms 'HYENA sū-'.\"},\n       {\"ref\": \"KLN\", \"status\": \"supports\",\n        \"note\": \"Klein s.v. hyena ('L. hyaena, fr. Gk. huaina') and s.v. syphilis ('ModL., from the title of the work by Girolamo Fracastoro...').\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Hyena\", \"stance\": \"supports\", \"note\": \"'Hyena, Hyaena, a sow-like quadruped. (L.—Gk.)'\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dict.\", \"stance\": \"silent\",\n        \"note\": \"Our WEB_vol1.txt scan breaks off in the h-range around 'hedge-'; no usable hyena/syphilis article could be printed.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Germanic\", \"words\": \"swînam\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Proto-Germanic *swīnan (neuter) is the substantivised adjective *suH-i-no- 'belonging to the pig' — the same \"\n        \"*-ino- suffix as in Latin suīnus, Old Church Slavonic svinŭ and Latvian svīns — with pre-Germanic *su- appearing as *sw- \"\n        \"before the suffix vowel and *-ī- from *-iH-. It gives OE swīn, OS/OHG swīn, ON svín, Goth. swein, Du. zwijn, Ger. Schwein. \"\n        \"Nourai's 'swînam' is Watkins's citation form *swīnam (the Proto-Germanic neuter nominative/accusative in *-am).\"),\n     \"derivation_fa\": (\"ژرمنی آغازین *swīnan (خنثی) در اصل صفتِ اسم‌شدهٔ *suH-i-no- «متعلق به خوک» است؛ همان پسوند ‑ino- که در لاتین \"\n        \"suīnus و اسلاوی کلیسایی کهن svinŭ و لتونیایی svīns دیده می‌شود. «سو» پیشاژرمنی پیش از واکهٔ پسوند به *sw- بدل شده و ī از *iH \"\n        \"آمده است. بازمانده‌های آن انگلیسی کهن swīn، ساکسونی و آلمانی علیای کهن swīn، نورس کهن svín، گوتی swein، هلندی zwijn و آلمانی \"\n        \"Schwein است. صورت «swînam» که نورایی آورده همان صورت استنادیِ واتکینز است. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/swine\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. sū-: '1. Suffixed form *suə-ino- in Germanic *swīnam in Old English swin, swine: SWINE.' — verbatim Nourai's box.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW 1038f.\", \"stance\": \"supports\",\n        \"note\": \"'substantivized Gothic swein, Old Icelandic svin, Old English Old High German swin \\\"swine\\\"' under the no-derivatives of su-s.\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 512\", \"stance\": \"supports\",\n        \"note\": \"'(idg. Bildung) lat. suinus ds., aksl. svinŭ ds. ... substantiviert got. swein, aisl. svin, ags. ahd. swin \\\"Schwein\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"swine\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"OE swīn 'domestic pig, hog, sow; wild boar', a neuter a-stem with zero plural, gives ME swin and ModE swine, \"\n        \"the OE ī becoming /aɪ/ by the Great Vowel Shift and the old zero plural surviving (one swine, many swine). It was the native \"\n        \"general word until pig displaced it from the 14th c.; the abusive application to persons is attested from late 14c. \"\n        \"('pearls before swine' translating Matthew vii.6 is mid-14c.).\"),\n     \"derivation_fa\": (\"انگلیسی کهن swīn «خوک خانگی، گراز» اسمی خنثی از ستاک ‑a با جمعِ بی‌نشانه بود؛ در انگلیسی میانه swin و در \"\n        \"انگلیسی نو swine شد، «ای» کشیدهٔ انگلیسی کهن بر اثر «جابه‌جایی بزرگ واکه‌ها» به /aɪ/ بدل شد و جمعِ بی‌نشانه برجا ماند. این واژه \"\n        \"تا سدهٔ چهاردهم واژهٔ عام و بومیِ «خوک» بود و سپس pig جای آن را گرفت؛ کاربرد دشنام‌آمیزش دربارهٔ آدمیان از پایان سدهٔ چهاردهم \"\n        \"گواه دارد. ادعای نورایی درست است.\"),\n     \"sources\": [\"https://www.etymonline.com/word/swine\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"The box carries no refs= in the book; the parent Germanic box's AHD citation covers it ('...in Old English swin, swine: SWINE').\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"s.v. sow / swine\", \"stance\": \"supports\",\n        \"note\": \"Klein s.v. sow lists 'swine' among the words derived from the I.-E. base *su-, *suw-.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins index 'SWINE sū-'\", \"stance\": \"supports\",\n        \"note\": \"AHD_watkins1985.txt l.2329: 'SWIM swem- SWINE sū-'.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Celtic\", \"words\": \"sukko\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"Celtic *sukko- 'swine; pig's snout; ploughshare' is a k-suffixed *suH-k- with expressive gemination of the -k-, \"\n        \"the same suffix as in Skt. sūkara- and Lat. sucula. Pokorny 1038f. lists it explicitly: 'with expressive gemination Celtic \"\n        \"*sukko- \\\"swine, (pig-) snout, plowshare\\\" in Old Irish socc sail ..., Middle Irish soc \\\"plowshare, snout\\\", Welsh hwch, \"\n        \"Cornish hoch, Breton houc'h'; from the Gallo-Latin form come Welsh swch, Breton souc'h and French soc 'ploughshare'. \"\n        \"Nourai's gloss 'hog' is Watkins's English wording for the Celtic etymon, not a Celtic meaning.\"),\n     \"derivation_fa\": (\"سلتیِ آغازین *sukko- «خوک؛ پوزهٔ خوک؛ تیغهٔ گاوآهن» صورتی با پسوند ‑k و مصوّت‌زداییِ تشدیدیِ نمایشی است، همان \"\n        \"پسوندی که در سنسکریت sūkara- و لاتین sucula هست. پوکورنی در ص ۱۰۳۸ به‌روشنی آن را آورده است: «با مشدّدسازیِ نمایشی، سلتی \"\n        \"*sukko- «خوک، پوزهٔ خوک، تیغهٔ خیش» در ایرلندی کهن socc، ایرلندی میانه soc، ولزی hwch، کورنی hoch، برتونی houc'h»؛ و از صورت \"\n        \"گالی‑لاتینِ آن ولزی swch و برتونی souc'h و فرانسوی soc «تیغهٔ گاوآهن» آمده است. معنای «hog» که نورایی نوشته واژهٔ انگلیسیِ \"\n        \"واتکینز برای این ستاک است نه معنای سلتی آن. ادعای نورایی درست است.\"),\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/suH-\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"supports\",\n        \"note\": \"Watkins 1985 s.v. sū-: '2. Celtic expressive form *sukko-, swine, snout of a swine, plowshare, in: a. British *hukk- in Old English hogg, hog: HOG; b. perhaps Old French soc, plowshare: SOCKET.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW 1038f.\", \"stance\": \"supports\",\n        \"note\": \"'with expressive Gemination: Celtic *sukko- \\\"swine, (pig-) snout, plowshare\\\" in Old Irish socc ... cymr. hwch ... bret. houc'h.'\"},\n       {\"src\": \"WLD\", \"where\": \"Bd. II 513\", \"stance\": \"supports\",\n        \"note\": \"'cymr. hwch f. \\\"sus, porcus\\\", corn. hoch, bret. houch \\\"porcus\\\" ... air. socc \\\"(*Schweine-)Schnauze; Pflugschar\\\"; gallische Lw. sind cymr. such, bret. souch, corn. soch (und frz. soc) \\\"Pflugschar\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\", \"words\": \"hog\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Watkins/AHD is Nourai's source and does say '*sukko- ... a. British *hukk- in Old English hogg, hog: HOG', and \"\n        \"Klein likewise cross-refers hog to sow. Modern lexicography rejects this. Etymonline, following the OED, records the Celtic \"\n        \"hypothesis as explicitly doubted: 'Possibility of British Celtic origin [Watkins, etc.] is regarded by OED as \\\"improbable\\\"'. \"\n        \"The semantic evidence is against it too: ME hogge (mid-14c.; implied in the Latinised hogaster from late 12c.) meant a \"\n        \"castrated male swine reared for slaughter, usually about a year old, and was equally used by stockmen of a yearling sheep \"\n        \"before the first shearing and of a horse older than one year — so the original criterion was age, not species, which no \"\n        \"*sukko- 'pig' etymology can explain. Formally, too, British Celtic gives hwch/hoch, not *hukk-. The modern verdict is that \"\n        \"the origin of hog is unknown.\"),\n     \"derivation_fa\": (\"سرچشمهٔ نورایی پیوستِ ریشه‌های AHD است که می‌گوید «*sukko- ... در بریتونیِ *hukk- و انگلیسی کهن hogg, hog» و \"\n        \"کلاین نیز hog را به sow ارجاع می‌دهد. اما فرهنگ‌نویسی امروزی این را نمی‌پذیرد: اتیمانلاین به پیروی از فرهنگ آکسفورد می‌نویسد که \"\n        \"«احتمال خاستگاه سلتی بریتانیایی (واتکینز و دیگران) از دید OED نامحتمل است». شواهد معنایی نیز مخالف است: hogge در انگلیسی \"\n        \"میانه (میانهٔ سدهٔ چهاردهم، و در صورت لاتینی‌شدهٔ hogaster از پایان سدهٔ دوازدهم) به معنی خوکِ نرِ اخته‌ای بود که برای کشتار \"\n        \"پروار می‌کردند و معمولاً یک‌ساله بود، و دامداران همان واژه را برای گوسفندِ یک‌سالهٔ پشم‌نچیده و اسبِ بیش از یک‌ساله هم به کار \"\n        \"می‌بردند؛ پس ملاکِ آغازین سن بود نه گونهٔ جانور. از نظر آوایی هم سلتیِ بریتانیایی hwch/hoch می‌دهد نه *hukk-. پژوهش امروزی این \"\n        \"اشتقاق را رد می‌کند و خاستگاه hog را ناشناخته می‌داند.\"),\n     \"sources\": [\"https://www.etymonline.com/word/hog\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"The box carries no refs= of its own; the claim rests on the parent Celtic box's 'AHD', which is quoted and evaluated above.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sū-\", \"stance\": \"supports\",\n        \"note\": \"'2. Celtic expressive form *sukko- ... a. British *hukk- in Old English hogg, hog: HOG' — the only modern reference that backs the chart.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. sow (KLN_1966.txt l.36033)\", \"stance\": \"partial\",\n        \"note\": \"'Cp. hog, hyena, socket, soil...' — Klein groups hog with the su- family but gives no British Celtic *hukk- chain in the sow article.\"},\n       {\"src\": \"WEB\", \"where\": \"Webster's 2nd, s.v. hog (WEB_vol1.txt l.91263)\", \"stance\": \"contradicts\",\n        \"note\": \"'hog, n.; pl. hogs or hog, [ME. hog, hoge, hogge, a gelded hog.]' — Webster traces the word no further than Middle English, offering no Celtic source.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Latin\", \"words\": \"sus\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Latin sūs, gen. suis 'pig, sow, swine' is the direct athematic reflex of *suH-s / *suH-és, matching Gk. ὗς and \"\n        \"Umbrian sif 'sues' (Walde-Pokorny II 512; Pokorny 1038). That much is certain. But the gloss is wrong: Latin sūs means only \"\n        \"'pig'; there is no Latin sense 'anything dirty'. Nourai has read back into the etymon the sense of its derivatives — the \"\n        \"adjective suīllus 'of swine' and the Vulgar-Latin diminutive suculus/sucula 'little pig, piggery', whose 'wallow, mire' \"\n        \"sense is what the next node (soil) actually requires. Arrow correct, gloss anticipatory.\"),\n     \"derivation_fa\": (\"لاتین sūs (اضافی suis) «خوک، ماده‌خوک» بازماندهٔ مستقیمِ صورتِ بی‌میانوندِ *suH-s / *suH-és است و با یونانی ὗς \"\n        \"و اومبریایی sif «sues» برابر می‌افتد (والده‑پوکورنی، ج ۲ ص ۵۱۲؛ پوکورنی ص ۱۰۳۸). تا اینجا تردیدی نیست. اما معنایی که نورایی \"\n        \"نوشته نادرست است: sūs در لاتین تنها «خوک» است و معنای «هر چیز چرک و پلید» ندارد. او معنای مشتق‌ها را به خودِ ستاک بازگردانده \"\n        \"است؛ یعنی صفت suīllus «خوکی» و مصغّرِ لاتینِ عامیانه suculus/sucula «خوک کوچک، خوک‌دانی» که معنای «گِل‌ولای و لجن‌زار»شان \"\n        \"همان است که خانهٔ بعدی (soil) بدان نیاز دارد. پس پیکان درست است ولی معنا جلوتر از موعد آمده؛ با احتیاط پذیرفتنی است.\"),\n     \"sources\": [W+\"Reconstruction:Proto-Indo-European/suH-\"],\n     \"ref_check\": [\n       {\"ref\": \"AHD\", \"status\": \"partial\",\n        \"note\": \"Watkins 1985 s.v. sū-: '4. Latin sūs, pig: SOIL².' — supports the arrow and the English outcome, but glosses sūs simply 'pig', with no 'anything dirty'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"WLD\", \"where\": \"Bd. II 512\", \"stance\": \"supports\",\n        \"note\": \"'lat. sūs, suis \\\"Schwein\\\", umbr. sif \\\"sues\\\", sim \\\"suem\\\"' — 'Schwein' only.\"},\n       {\"src\": \"POK\", \"where\": \"IEW 1038\", \"stance\": \"supports\",\n        \"note\": \"'Latin sus, suis \\\"swine\\\", Umbrian sif \\\"sues\\\", sim \\\"suem\\\", surum, sorsom, sorsalem \\\"swine\\\" (*su-do-, *su-dalis).'\"},\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Soil (2) (SKT.txt l.17914)\", \"stance\": \"partial\",\n        \"note\": \"'— L. suillus, adj., belonging to swine. — L. sus, a sow.' Skeat too gets the 'dirty' sense only from the derivative, not from sus.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"English\", \"words\": \"soil\", \"verdict\": \"plausible\",\n     \"derivation\": (\"The word meant is soil 'to defile, make dirty' (early 13c. soilen), not soil 'ground'. It comes from Old French \"\n        \"soillier 'to splatter with mud, to wallow' (12c., ModFr. souiller), from the noun souil 'tub; wild boar's wallow, pigsty'. \"\n        \"Skeat (s.v. Soil (2)) and Klein derive souil from Latin suillus 'of swine' / sucula 'young sow', diminutive of sūs, which is \"\n        \"exactly Nourai's chain, and Watkins/AHD likewise files SOIL² under sū-. But Etymonline and the OED leave the choice open: \"\n        \"souil may equally be from Latin solium 'tub for bathing, seat' (PIE *sed- 'to sit'). Since two derivations remain live, the \"\n        \"node is plausible rather than confirmed. It should be stressed that the homonym soil 'ground, earth' (from Lat. solum, via \"\n        \"OFr. soel) is unrelated — Skeat marks it 'quite distinct from soil, ground' — and Nourai's unglossed box invites the confusion.\"),\n     \"derivation_fa\": (\"واژه‌ای که در این خانه منظور است soil به معنی «آلودن، چرک کردن» (از آغاز سدهٔ سیزدهم، soilen) است نه soil به \"\n        \"معنی «خاک و زمین». این واژه از فرانسهٔ کهن soillier «به گِل آلودن، در لجن غلتیدن» (سدهٔ دوازدهم، فرانسهٔ امروز souiller) آمده و \"\n        \"آن از اسم souil «تغار؛ لجن‌زارِ گراز، خوک‌دانی» است. اسکیت و کلاین souil را از لاتین suillus «خوکی» یا sucula «خوکِ کوچک»، \"\n        \"مصغّرِ sūs، می‌گیرند و همین زنجیره است که نورایی رسم کرده؛ واتکینز هم SOIL² را زیر sū- آورده است. اما اتیمانلاین و فرهنگ آکسفورد \"\n        \"راه دیگری را نیز باز می‌گذارند: souil می‌تواند از لاتین solium «تغارِ حمام، جایگاه» (از ریشهٔ *sed- «نشستن») باشد. چون هر دو \"\n        \"اشتقاق همچنان زنده‌اند، این خانه با احتیاط پذیرفتنی است. افزون بر این باید تأکید کرد که همنامِ آن، soil «خاک» (از لاتین solum \"\n        \"از راه فرانسهٔ کهن soel) هیچ پیوندی با این ریشه ندارد و اسکیت به‌صراحت آن دو را جدا می‌داند؛ خانهٔ بی‌معنای نورایی این اشتباه را \"\n        \"آسان می‌کند.\"),\n     \"sources\": [\"https://www.etymonline.com/word/soil\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"The box carries no refs= of its own; the parent Latin box's 'AHD' (Watkins 'Latin sūs, pig: SOIL²') is the supporting citation and is evaluated above.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SKT\", \"where\": \"Skeat s.v. Soil (2), to defile (SKT.txt l.17914)\", \"stance\": \"supports\",\n        \"note\": \"'Soil (2), to defile. (F.—L.) M.E. soilen ... — O.F. soillier, F. souiller, to soil; se souiller, to wallow as a sow — O.F. soil, souil, \\\"the soile of a wild boare, the mire wherein he hath wallowed\\\" ... plainly from L. sucula, a young sow, dimin. of sus, a sow ... quite distinct from soil, ground.'\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. sow (KLN_1966.txt l.36033)\", \"stance\": \"supports\",\n        \"note\": \"'Cp. hog, hyena, socket, soil, \\\"to make dirty\\\", suilline, sully, Sus, swine...' — Klein files soil (v.) under the su- family.\"},\n       {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sū-\", \"stance\": \"supports\",\n        \"note\": \"'4. Latin sūs, pig: SOIL².'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 4,\n   \"root\": \"Suîğ\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Mann's PIE *suĭg- 'jump, dance' (= Proto-Iranian *xaiz- 'to rise', of no established IE ancestry)\",\n   \"note\": (\"Nourai's root box reproduces his source exactly. Mann, An Indo-European Comparative Dictionary, p. 1354 (IEC.txt l.18061, \"\n            \"scan leaf 745, which carries the printed page markers 1353 and 1355): 'suĭg- (1) \\\"jump, dance\\\" Av. xiz-, v. \\\"jump\\\"; \"\n            \"Per. xizam, xizidan, v. \\\"leap, jump up\\\"; xiz, s. \\\"rise; leap\\\"; MHG swicken, v. (1) \\\"jump, dance\\\"'. But the root is \"\n            \"Mann's alone. Pokorny has no *sueig- 'jump, dance': his sueig- (p. 1042, in the su̯ei- complex) is 'nachgeben, slacken; \"\n            \"(cunning) etwas drehen, dodge, deception' with OHG swīhhōn, OE swīcan; Watkins/AHD has nothing of the kind; and Cheung, \"\n            \"Etymological Dictionary of the Iranian Verb (2007) p. 441, prints under Iranian *xaiz 'to rise, ascend' the line \"\n            \"'*PIE LIV: — | Pok.: —', i.e. no Indo-European etymology is established (and under the homophone *haiz he adds explicitly \"\n            \"'An IE provenance for this Ir. root cannot be established'). The Iranian family itself (xāstan / xēz-) is perfectly secure; \"\n            \"what is unproven is the PIE root box and the Germanic cognate hanging from it.\"),\n   \"note_fa\": (\"خانهٔ ریشه دقیقاً از منبعِ خودِ نورایی گرفته شده است: مان در «فرهنگ تطبیقی هندواروپایی» ص ۱۳۵۴ می‌نویسد «suĭg- (۱) «جستن، \"\n               \"رقصیدن»: اوستایی xiz- «جستن»؛ فارسی xizam، xizidan «جهیدن، برجستن»؛ xiz «برخاستن، جهش»؛ آلمانی میانهٔ علیا swicken «جستن، \"\n               \"رقصیدن»». اما این ریشه تنها از آنِ مان است. پوکورنی چنین ریشه‌ای به معنی «جستن» ندارد؛ sueig- او (ص ۱۰۴۲) به معنی «سست شدن، \"\n               \"پیچاندن، فریفتن» است با شواهد آلمانی علیای کهن swīhhōn و انگلیسی کهن swīcan. واتکینز نیز چیزی ندارد. چونگ در «فرهنگ \"\n               \"ریشه‌شناختی فعل ایرانی» (۲۰۰۷) ص ۴۴۱ زیر *xaiz «برخاستن» به‌صراحت می‌نویسد «PIE LIV: — | Pok.: —»، یعنی هیچ ریشهٔ \"\n               \"هندواروپایی‌ای برای آن ثابت نشده است. خانوادهٔ ایرانیِ خاستن/خیز استوار است؛ آنچه ثابت نشده خودِ خانهٔ ریشه و خویشاوندِ \"\n               \"ژرمنیِ آویخته به آن است. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n   \"sources\": [W+\"%D8%AE%D8%A7%D8%B3%D8%AA%D9%86\"],\n   \"ref_check\": [\n     {\"ref\": \"IEC:1354\", \"status\": \"supports\",\n      \"note\": \"Mann p.1354 (IEC.txt l.18061): 'suĭg- (1) \\\"jump, dance\\\" Av. xiz-, v. \\\"jump\\\"; Per. xizam, xizidan, v. \\\"leap, jump up\\\"; xiz, s. \\\"rise; leap\\\"; MHG swicken, v. (1) \\\"jump, dance\\\"'. The page is right: the surrounding leaf carries the printed markers 1353 and 1355.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"POK\", \"where\": \"IEW 1041-1042, s.v. sueig- (POK_full.txt l.84401)\", \"stance\": \"contradicts\",\n      \"note\": \"'sueig-: Germanic also \\\"nachgeben, slacken\\\" ... \\\"(cunning) etwas drehen, dodge, deception\\\": Old High German swīhhōn, Old English swīcan ...' — Pokorny's *sueig- means 'bend/slacken/deceive', not 'jump, dance', and he lists no Iranian material.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 441 s.v. *xaiz (CHEUNG.txt l.28483ff.)\", \"stance\": \"contradicts\",\n      \"note\": \"'*xaiz \\\"to rise, ascend; increase\\\" ... *NWIR: NP xāstan/xēz- ... *PIE LIV: — | Pok.: —' — Cheung records no PIE source at all for the Iranian root.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, root list\", \"stance\": \"silent\",\n      \"note\": \"grep of AHD_watkins1985.txt for 'sueig/sweig/swicken' returns nothing; the appendix has no such root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"haiz; xvîsat; xaezanuha; pairi-xaezanuha\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Nourai's cited source is Horn, Grundriss no. 462 (which begins on p. 102 and runs onto p. 103) and he reproduces \"\n        \"it faithfully: 'xāstan \\\"aufstehen\\\", Praes. xēz-em, xēzīdan (xīzīdan). aw. pairi.xaēzaŋuha \\\"erhebe dich\\\"', plus, in Horn's \"\n        \"footnote 4, Darmesteter's reading aw. xᵛīsat̰. Three things in the box are nevertheless wrong. (a) The Avestan verb is attested \"\n        \"only in the imperative pāiri.haēzaŋuha (Vd. 21.4, 21.12, 21.16), and Bartholomae lemmatises it 'j. haēz- V., nur mit pāiri \"\n        \"\\\"spürend, suchend umhergehen\\\"' — 'to go about tracking, searching', not 'to rise'. Gershevitch (1952) and Cheung 2007 file \"\n        \"it accordingly under a separate root *haiz 'to look, search for pastures?' (with Oss. xizyn 'to pasture, graze', Khot. pachiys-), \"\n        \"while the 'rise' root *xaiz has NO Avestan attestation at all. Horn himself warned 'Das awestische Wort ist nicht sicher; die \"\n        \"Pāzend-Lesung mit z beweist nichts'. (b) 'xvîsat: he rises' is Darmesteter's xᵛīsat̰, which Horn quotes only in order to reject \"\n        \"it — Horn glosses it 'er fing an zu schwitzen (!)' ('he began to sweat') and says Darmesteter 'macht die Sache nur schlimmer'. \"\n        \"(c) The 'Old Persian' half of the language label is unsupported: neither Kent's lexicon nor Bartholomae records any Old Persian \"\n        \"form of this verb. The spellings themselves (xaezanuha = xaēzaŋuha) are faithful renderings of Horn, so this is a substantive \"\n        \"error, not a transcription one.\"),\n     \"derivation_fa\": (\"منبع نورایی «اساس ریشه‌شناسی فارسی نو» هرن، شمارهٔ ۴۶۲ (که از ص ۱۰۲ آغاز می‌شود و به ص ۱۰۳ می‌کشد) است و او \"\n        \"همان را وفادارانه نقل کرده: «xāstan «برخاستن»، ستاک حال xēz-em، xēzīdan/xīzīdan؛ اوستایی pairi.xaēzaŋuha «برخیز»»، به‌علاوهٔ \"\n        \"خوانشِ دارمستتر (xᵛīsat̰) که هرن در پانوشت آورده است. با این همه سه اشکالِ اساسی در این خانه هست. نخست، آن فعل اوستایی تنها در \"\n        \"صورت امریِ pāiri.haēzaŋuha (وندیداد ۲۱٫۴ و ۲۱٫۱۲ و ۲۱٫۱۶) به کار رفته و بارتولومه آن را زیر مدخل «haēz-، تنها با pairi: \"\n        \"«جست‌وجوکنان و رَدیاب‌وار گشتن»» آورده است، نه «برخاستن»؛ گرشویچ (۱۹۵۲) و چونگ (۲۰۰۷) نیز آن را زیر ریشهٔ جداگانهٔ *haiz «نگریستن، \"\n        \"چراگاه جستن» (با آسی xizyn «چریدن») می‌گذارند و برای ریشهٔ «برخاستن» هیچ شاهد اوستایی‌ای نمی‌شناسند. خودِ هرن هم هشدار داده است \"\n        \"«واژهٔ اوستایی مطمئن نیست». دوم، «xvîsat: برمی‌خیزد» همان xᵛīsat̰ دارمستتر است که هرن تنها برای ردّ کردن نقل می‌کند و معنایش را \"\n        \"«او به عرق کردن آغاز کرد (!)» می‌آورد. سوم، برچسبِ «پارسی باستان» پشتوانه ندارد؛ نه کنت و نه بارتولومه هیچ صورت پارسی باستانی \"\n        \"از این فعل ثبت نکرده‌اند. خودِ آوانویسی‌ها (xaezanuha = xaēzaŋuha) درست و مطابق هرن است، پس این خطای محتوایی است نه خطای چاپ یا \"\n        \"خوانش. پژوهش امروزی این خانه را رد می‌کند.\"),\n     \"sources\": [W+\"%D8%AE%D8%A7%D8%B3%D8%AA%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"HRN:103\", \"status\": \"supports\",\n        \"note\": \"Horn no. 462 (HRN.txt l.4229ff., the page marker '— 103 —' at l.4234): 'xāstan \\\"aufstehen\\\", Praes. xēz-em ..., xēzīdan (xīzīdan). aw. pairi.xaēzaŋuha \\\"erhebe dich\\\"; phlv. xēst (vd. 16 (7) Gl.), rīst.xēzēe, ā.xēzēt ... Das awestische Wort ist nicht sicher.' Horn supports the forms but not the confidence.\"},\n       {\"ref\": \"ETM:66\", \"status\": \"not_checked\",\n        \"note\": \"ETM = Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374; refs_online.json records that no digital copy exists on any permitted platform (catalogue/purchase only).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW s.v. haēz- (BRT.txt l.28696-28698, the h-columns near 1730)\", \"stance\": \"contradicts\",\n        \"note\": \"'j. haēz- V., nur mit pāiri \\\"spürend, suchend umhergehen\\\". Praes. 3 haēza: usihista pāiri.haēzaŋuha yaθe saxvaica vaxəδraica yaoždaθəm daθāt̰ ahurō mazdā̊ V.21.4.' Bartholomae's gloss is 'to go about tracking/searching', not 'to rise'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 441 (*xaiz) and the *haiz entry (CHEUNG.txt l.28483, l.9123)\", \"stance\": \"contradicts\",\n        \"note\": \"*xaiz 'to rise' is listed with MP/Parthian/Sogdian/Khotanese/NP material but NO Avestan; the Avestan pairi.haēz- 'to search, scrutinize' stands under the separate *haiz 'to look, search for pastures?', of which Cheung says 'An IE provenance for this Ir. root cannot be established.' He also cites Gershevitch 1952a: 488ff. for three distinct roots.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon\", \"stance\": \"silent\",\n        \"note\": \"grep of KNT.txt / KNT_full.txt for haiz/xaiz/xēz finds no Old Persian verb of this shape — the 'Old Persian' label on the box has no support.\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien no. 462 (HUB.txt l.1840)\", \"stance\": \"partial\",\n        \"note\": \"'462. Dazu afgh. xatəl \\\"sich erheben, aufstehen\\\", pr. 3. p. xēzi. Freilich macht xatəl Schwierigkeit, da es nach Geiger für *xaštəl stehen soll, das nicht zu np. xāstan stimmt.' Hübschmann adds Pashto but flags a formal difficulty; he supplies no Avestan support.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"xâstan, xĕzistan; rist-axez\", \"verdict\": \"plausible\",\n     \"derivation\": (\"The Middle Persian verb is normally cited with the preverb: ā-xistan / āxēz- (Book Pahlavi ʾhstn' : ʾhyc-, \"\n        \"ideogram KDMWN-tn'), Nyberg Glossary p. ~41: 'āxistan ... āxēz- to stand up ...; abar ~ id.; abāz ~ to rise from the dead'; \"\n        \"Manichaean MP ʾxyz-, past ʾxyst, Parthian ʾxyz- / ʾxʾst (Cheung p. 441). The pair past *xāst- : present xēz- goes back to \"\n        \"*xaista- : *xaiza-. rist-āxēz 'resurrection' is amply attested (MacKenzie s.v. rist-āxēz [lyst'hyc]; Nyberg: 'rist-āxēz the \"\n        \"resurrection of the dead ... From rist (q.v.) + āxēz, pres. st. of āxistan'), the first element being rist 'dead', the past \"\n        \"participle of the unrelated verb 'to die'. Nourai's forms are therefore right in substance but not the standard citation \"\n        \"forms: the bare xāstan is Pāzand/New Persian rather than Book Pahlavi (MacKenzie's Pahlavi xastan [hstn'] means 'to wound'), \"\n        \"and Mo'in's footnote in Borhān-e Qāṭeʿ gives 'پهلوی ساسانی xēzīdan', not xēzistan.\"),\n     \"derivation_fa\": (\"فعلِ فارسی میانه را معمولاً با پیشوند می‌آورند: ā-xistan / āxēz- (در پهلوی کتابی ʾhstn' : ʾhyc-، با هزوارش \"\n        \"KDMWN-tn')؛ نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» (حدود ص ۴۱) می‌نویسد «āxistan ... āxēz- برخاستن ...؛ abāz ~ از مردگان \"\n        \"برخاستن». در فارسی میانهٔ مانوی ʾxyz- و ستاک گذشتهٔ ʾxyst و در پارتی ʾxyz-/ʾxʾst آمده است (چونگ ص ۴۴۱). جفتِ گذشتهٔ *xāst- در \"\n        \"برابر حالِ xēz- از *xaista- : *xaiza- است. «rist-āxēz» (رستاخیز) نیز شواهد فراوان دارد: مکنزی آن را با نویسهٔ lyst'hyc آورده و \"\n        \"نیبرگ می‌نویسد «از rist + āxēz، ستاک حالِ āxistan»، و rist همان صفت مفعولیِ فعلِ «مردن» است که ریشه‌اش با این خانواده یکی نیست. \"\n        \"پس صورت‌های نورایی از نظر محتوا درست‌اند ولی صورت‌های استنادیِ معیار نیستند: xāstanِ بی‌پیشوند پازند و فارسی نو است نه پهلوی \"\n        \"کتابی (xastan در مکنزی به معنی «زخمی کردن» است) و معین در حاشیهٔ برهان قاطع «پهلوی ساسانی xēzīdan» نوشته نه xēzistan. با احتیاط \"\n        \"پذیرفتنی است.\"),\n     \"sources\": [W+\"%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2\"],\n     \"ref_check\": [\n       {\"ref\": \"NYB:39\", \"status\": \"supports\",\n        \"note\": \"Nyberg, Manual of Pahlavi II (Glossary), s.v. āxistan (NYB_vol2_glossary.txt l.818, scan leaf 49 = printed ~p.41, i.e. the cited p.39 ±2): 'āxistan [ʾhstn'; KDMWN-tn'] āxēz- [ʾhyc-, KDMWN-] to stand up ...; abar ~ id. ...; abāz = to rise from the dead ... < ā- + BP xistan [hstn'] xēz- [hyc-].' And s.v. rist-āxēz (p.~178): 'the resurrection of the dead ... From rist (q.v.) + āxēz, pres. st. of āxistan; Pāz. rist-āxēz; NP rastāxēz.'\"},\n       {\"ref\": \"FVS:199\", \"status\": \"not_checked\",\n        \"note\": \"'FVS' is not defined in Nourai's Table IV (refs_online.json: 'probably a typo for FVF or FSF'). If FSF (Noushin, Vazhe-namak) is meant, its رستخیز entry does say exactly this: 'مخفف رستاخیز. پهلوی ریست‌اخز ... ریست به‌معنی مرده و خیز از خاستن؛ یعنی برخاستن مردگان' (FSF_pages.txt l.13273-13277).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. rist-āxēz (PHD.txt l.557)\", \"stance\": \"supports\",\n        \"note\": \"'rist [lyst' | M ryst] dead. ... rist-āxēz [lyst?hyc | M ryst?hyz, N ~] resurrection of the dead.' Note MacKenzie's separate 'xastan [hstn' | M xst, N ~] wound, injure', which is NOT this verb.\"},\n       {\"src\": \"NYB\", \"where\": \"Glossary s.v. āxistan and rist-āxēz\", \"stance\": \"supports\",\n        \"note\": \"quoted in the ref_check above.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 441 s.v. *xaiz\", \"stance\": \"supports\",\n        \"note\": \"'*MIDDLE PERSIAN: (+ *ā-) MMP ʾxyz-, BMP ʾhyc- (KDMWN-) /āxēz-/ \\\"to rise (up)\\\", MMP ʾxyzyn- (caus.) \\\"to raise\\\" ... Partic.: perf. pass. MMP ʾxyst || *PARTHIAN: (+ *ā-) ʾxyz- \\\"to rise\\\" ... perf. pass. ʾxʾst.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"xâstan; rastâxîz\", \"verdict\": \"confirmed\",\n     \"derivation\": (\"NP خاستن xāstan 'to rise' (present stem خیز xēz- > xīz-), with the compound برخاستن bar-xāstan and the secondary \"\n        \"infinitives خیزیدن xēzīdan and برخیزیدن bar-xēzīdan, continues MP āxistan/āxēz- with loss of the preverb ā- (which survives in \"\n        \"the compound), MP ē becoming Iranian-Persian ī. رستاخیز rastāxīz (short form رستخیز rastaxīz) 'resurrection' is inherited whole \"\n        \"from MP rist-āxēz 'the rising of the dead', its first element rist 'dead' having been reshaped by folk etymology on رستن rastan \"\n        \"'to escape, be saved'; Mo'in's footnote at Borhān-e Qāṭeʿ p. 948 states this expressly. Of the extras printed in the Persian box, \"\n        \"خیز، خیزیدن، برخیزیدن belong here without question; خزیدن xazīdan 'to creep' and خَز are more doubtful — Cheung reconstructs \"\n        \"'to creep' as *xaz with root vowel a (on account of the NP present xaz-) and keeps it apart from *xaiz 'to rise', although \"\n        \"Mo'in's own footnote on خزیدن calls the Sogdian form 'هم‌ریشهٔ خاستن فارسی'.\"),\n     \"derivation_fa\": (\"«خاستن» با ستاک حالِ «خیز» و مرکبِ «برخاستن» و مصدرهای ثانوی «خیزیدن» و «برخیزیدن» دنبالهٔ فارسی میانهٔ \"\n        \"āxistan/āxēz- است با افتادنِ پیشوند ā- (که در «برخاستن» با پیشوندِ دیگر جبران شده)؛ «ای» کشیدهٔ فارسی میانه (ē) در فارسی نوِ ایران \"\n        \"به «ی» (ī) بدل شده است. «رستاخیز» (و کوتاه‌شدهٔ آن «رستخیز») یکسره از فارسی میانهٔ rist-āxēz «برخاستنِ مردگان» به ارث رسیده و جزء \"\n        \"نخستِ آن rist «مرده» است که بر اثر ریشه‌شناسی عامیانه با «رستن» (رهیدن) آمیخته شده؛ معین در حاشیهٔ برهان قاطع ص ۹۴۸ همین را \"\n        \"می‌نویسد: «از اوستا ... (مرده) + خیز (رك: خاستن) ... پهلوی ristāxēz ... به‌معنی برخاستن مردگان است». از واژه‌های افزودهٔ این خانه، \"\n        \"«خیز، خیزیدن، برخیزیدن» بی‌گمان از همین خانواده‌اند، اما «خزیدن» و «خَز» تردیدآمیزند: چونگ «خزیدن» را از ستاک *xaz با واکهٔ a \"\n        \"بازسازی می‌کند و آن را از *xaiz «برخاستن» جدا می‌داند، هرچند خودِ معین در حاشیهٔ «خزیدن» صورت سغدی را «هم‌ریشهٔ خاستن فارسی» \"\n        \"خوانده است. ادعای نورایی درست است.\"),\n     \"sources\": [W+\"%D8%AE%D8%A7%D8%B3%D8%AA%D9%86\", W+\"%D8%B1%D8%B3%D8%AA%D8%A7%D8%AE%DB%8C%D8%B2\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:700\", \"status\": \"supports\",\n        \"note\": \"Borhān-e Qāṭeʿ, Mo'in's footnote on خاستن, continued onto this page ('دنباله از صفحهٔ ۶۹۹'; BQT_v2_pages.txt leaf 158): 'خاستن ... پهلوی *xāstan «روایات پهلوی»، پهلوی تورفان ... : xēz، پهلوی ساسانی xēzīdan، سغدی ... افغانی (بلند شدن، برخاستن) «هویشمان»'.\"},\n       {\"ref\": \"BQT:745\", \"status\": \"partial\",\n        \"note\": \"The page reached by the same offset (BQT_v2_pages.txt leaf 203-204) carries Mo'in's footnote 8 on خزیدن: 'xazīdan (بلند شدن) از ... سغدی ... هم‌ریشهٔ خاستن فارسی «نیبرگ»'. It supports the خزیدن/خَز extras rather than خاستن itself; the OCR page numbering drifts by ~3 leaves in this stretch, so the match is approximate.\"},\n       {\"ref\": \"BQT:948\", \"status\": \"supports\",\n        \"note\": \"BQT_v2_pages.txt leaf 408, running head رستاخیز and page number ۹۴۸: entry 'رستاخیز: بر وزن دستاویز، قیامت را گویند که محشر باشد' with Mo'in's footnote 'از اوستا ... (مرده) + خیز (رك: خاستن) ... پازند ...؛ بنابرین رستاخیز (مخفف آن، رستخیز) پهلوی ristāxēz ... بمعنی برخاستن مردگان است'. Exactly the chart's claim.\"},\n       {\"ref\": \"HRN:103\", \"status\": \"supports\",\n        \"note\": \"Horn no. 462: 'xāstan \\\"aufstehen\\\", Praes. xēz-em, xēzīdan (xīzīdan)' and 'phlv. ... rīst.xēzēe'.\"},\n       {\"ref\": \"IEC:1354\", \"status\": \"supports\",\n        \"note\": \"Mann p.1354: 'Per. xizam, xizidan, v. \\\"leap, jump up\\\"; xiz, s. \\\"rise; leap\\\"'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnotes at pp. ~699-700, ~745, 948\", \"stance\": \"supports\", \"note\": \"quoted in the ref_check entries above.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 441 s.v. *xaiz\", \"stance\": \"supports\",\n        \"note\": \"'*NWIR: NP xāstan/xēz-, Awrom. hur(e)stāy/hur(e)z-, Gur. hur-iz-/hur za \\\"to rise, get up\\\" ... Mah. xizis \\\"jump\\\"'; and for 'creep' he says 'I would rather reconstruct the root as *xaz, with root vowel *a (on account of NP pres. xaz-)', which is why خزیدن is doubtful here.\"},\n       {\"src\": \"FSF\", \"where\": \"Noushin, Vazhe-namak, s.v. رستخیز (FSF_pages.txt l.13273-13277)\", \"stance\": \"supports\",\n        \"note\": \"'رستخیز: مخفف رستاخیز. پهلوی ریست‌اخز ... مرکب از ریست به‌معنی مرده و خیز از خاستن؛ یعنی برخاستن مردگان (یا به گفتهٔ اسدی طوسی «روز انگیختن»)؛ روز قیامت.'\"},\n       {\"src\": \"HUB\", \"where\": \"Persische Studien no. 462\", \"stance\": \"partial\",\n        \"note\": \"adds Pashto xatəl/xēzi but notes the formal difficulty (see node #1).\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Avestan\", \"words\": \"haxš\", \"verdict\": \"disputed\",\n     \"derivation\": (\"Nourai's source is again Horn no. 462, but what Horn says (on p. 103, not the cited p. 102) is that the Pahlavi \"\n        \"Vendīdād renders Avestan √haxš- by ā.xēzēt — a translator's equivalence, not an etymological one, and Horn immediately adds \"\n        \"that 'das awestische Wort ist nicht sicher'. Avestan haxš- is in fact a present stem of a completely different verb: \"\n        \"Bartholomae lemmatises 'j., g. ¹hak- V. \\\"sequi\\\". Praes. 1 hak-, sc-; 2 haca-, 5 *his.hak-, hisk-, 15 haxša-, 16 (Des.) hixša-' \"\n        \"— i.e. haxša- is the 15th present class of hak- 'to follow, accompany' (Skt. sac-, Gk. hépomai, Lat. sequor, PIE *sekʷ-), the \"\n        \"root of Av. haxā- 'companion' and haxman- 'company'. It has nothing to do with rising and nothing to do with Mann's *suĭg-. \"\n        \"The word is real; the gloss 'to rise' and the arrow from this root are wrong.\"),\n     \"derivation_fa\": (\"منبع نورایی باز هم هرن شمارهٔ ۴۶۲ است، اما آنچه هرن (در ص ۱۰۳، نه ص ۱۰۲ که نورایی داده) می‌گوید این است که \"\n        \"ترجمهٔ پهلوی وندیداد، فعلِ اوستایی √haxš- را با ā.xēzēt برگردانده است؛ این برابرنهادِ مترجمِ پهلوی است نه اتحادِ ریشه‌شناختی، و \"\n        \"هرن بی‌درنگ می‌افزاید «واژهٔ اوستایی مطمئن نیست». در واقع haxš- ستاکِ حالِ فعلی یکسره دیگر است: بارتولومه مدخلِ «hak- «پیروی \"\n        \"کردن، همراهی کردن»» را می‌آورد و haxša- را ستاکِ حالِ ردهٔ پانزدهمِ همین ریشه می‌شمارد؛ این همان ریشه‌ای است که در سنسکریت \"\n        \"sac-، یونانی hépomai، لاتین sequor و هندواروپایی *sekʷ- دیده می‌شود و واژه‌های اوستایی haxā- «همراه» و haxman- «همراهی» از \"\n        \"آن‌اند. پس واژه واقعی است اما معنای «برخاستن» و پیکانی که از این ریشه به آن کشیده شده نادرست است؛ پژوهش امروزی این خانه را \"\n        \"رد می‌کند.\"),\n     \"sources\": [W+\"%D8%AE%D8%A7%D8%B3%D8%AA%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"HRN:102\", \"status\": \"partial\",\n        \"note\": \"Horn's no. 462 begins on p.102 but the haxš- remark falls on p.103 (HRN.txt l.4235): 'rīst.xēzēe, ā.xēzēt (Phlv.-Vend. für aw. [√ha]xš-; AV.)'. Horn records a Pahlavi-Vendīdād rendering, not an Avestan verb meaning 'to rise', and adds 'Das awestische Wort ist nicht sicher'.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"AiW s.v. ¹hak- (BRT.txt l.28820)\", \"stance\": \"contradicts\",\n        \"note\": \"'j., g. ¹hak- V. \\\"sequi\\\". Praes. 1 hak-, sc-; 2 haca-, 5 *his.hak-, hisk-, 15 haxša-, 16 (Des.) hixša-, 2+24 hacaya-, 30 (Iter.) hācaya-; PPfP. haxta-; Inf. haxtōit̰.' — haxš- is a present stem of 'to follow', not a verb 'to rise'.\"},\n       {\"src\": \"CHEUNG\", \"where\": \"EDIV, *xaiz (p.441) and *haiz\", \"stance\": \"contradicts\",\n        \"note\": \"Neither entry cites any Avestan haxš-; Cheung lists no Avestan attestation whatever for *xaiz 'to rise'.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, Old Persian\", \"stance\": \"silent\",\n        \"note\": \"grep finds no haxš- of this meaning; Kent's hac-/hak- material belongs to 'follow/accompany'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Middle German\", \"words\": \"swicken\", \"verdict\": \"plausible\",\n     \"derivation\": (\"Mann is the sole authority, and he does say what the box says: IEC 1354 'MHG swicken, v. (1) \\\"jump, dance\\\"', \"\n        \"while his neighbouring entry (IEC 1353) has 'MLG swicken, v. \\\"hop; wind, bind\\\"' beside Du. zwikken 'get sprained' and Eng. \"\n        \"switch. So a Middle German swicken 'to move abruptly, hop' is real enough, and Nourai's label 'Middle German' stands for \"\n        \"Mann's MHG. What is not established is the equation with the Iranian xēz- family: Pokorny files the whole Germanic swik-/swig- \"\n        \"group under sueig- 'bend, slacken; deceive' and sueik- 'pliable' (IEW 1042), with no Iranian material, and Cheung finds no IE \"\n        \"source for *xaiz at all. Plausible as a German word, unproven as a cognate of xāstan.\"),\n     \"derivation_fa\": (\"تنها مرجعِ این خانه مان است و او دقیقاً همین را می‌گوید: در ص ۱۳۵۴ «آلمانی میانهٔ علیا swicken «جستن، رقصیدن»» \"\n        \"و در مدخل مجاور (ص ۱۳۵۳) «آلمانی میانهٔ سفلا swicken «جهیدن؛ پیچیدن، بستن»» در کنار هلندی zwikken «رگ‌به‌رگ شدن» و انگلیسی \"\n        \"switch. پس واژهٔ آلمانیِ میانه‌ای به صورت swicken با معنای «جهیدن، تکان ناگهانی خوردن» وجود دارد و برچسبِ «آلمانی میانه»ی نورایی \"\n        \"همان MHG مان است. آنچه ثابت نشده، هم‌ریشه بودنِ آن با خانوادهٔ ایرانیِ «خیز» است: پوکورنی همهٔ گروهِ ژرمنیِ swik-/swig- را زیر \"\n        \"sueig- «خم شدن، سست شدن؛ فریفتن» و sueik- «نرم و خم‌شو» (ص ۱۰۴۲) می‌آورد و هیچ شاهد ایرانی‌ای در آن نیست، و چونگ نیز برای \"\n        \"*xaiz هیچ سرچشمهٔ هندواروپایی نمی‌شناسد. پس واژه واقعی است ولی هم‌ریشگی‌اش با «خاستن» اثبات‌نشده؛ با احتیاط پذیرفتنی است.\"),\n     \"sources\": [],\n     \"ref_check\": [\n       {\"ref\": \"IEC:1354\", \"status\": \"supports\",\n        \"note\": \"Mann p.1354 (IEC.txt l.18061): 'suĭg- (1) \\\"jump, dance\\\" ... MHG swicken, v. (1) \\\"jump, dance\\\"'. Verbatim.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"POK\", \"where\": \"IEW 1042 s.v. sueig-, sueik- (POK_full.txt l.84401ff.)\", \"stance\": \"contradicts\",\n        \"note\": \"'sueig-: ... Old High German swīhhōn, Old English swīcan \\\"schweifen, wander, cheat, deceive\\\" ... sueik-: Old Icelandic sveigr \\\"pliable\\\" ...' — Pokorny assigns the Germanic sw-ig/ik words to 'bend/deceive' roots and cites no Iranian cognate.\"},\n       {\"src\": \"IEC\", \"where\": \"Mann p.1353 (IEC.txt l.17925)\", \"stance\": \"partial\",\n        \"note\": \"'... MLG (z-gde) swicken, v. \\\"hop; wind, bind\\\"; Du. zwikken, v. \\\"get sprained, be wricked\\\"; zwik, m. \\\"sprain\\\"; E to switch ...' — Mann himself puts a swicken under a different entry with a different gloss.\"},\n       {\"src\": \"KLN\", \"where\": \"s.v. switch / swig\", \"stance\": \"silent\",\n        \"note\": \"Klein has no swicken and makes no connection between any Germanic sw-ik- word and Persian xāstan.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-487.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-487.py"
}
```


### [2026-09-14T03:28:00.331Z] TOOL RESULT

```
ok
```


## [2026-09-14T03:28:04.368Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-487.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 487"
}
```


### [2026-09-14T03:28:05.552Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 7, 'confirmed': 8, 'disputed': 3}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 5, 'not_checked': 7}
books consulted: {'partial': 7, 'supports': 31, 'silent': 6, 'contradicts': 6} | by book: {'KLN': 7, 'WLD': 5, 'SKT': 5, 'POK': 4, 'CHEUNG': 4, 'BRT': 3, 'HUB': 3, 'MON': 3, 'AHD': 3, 'PHD': 2, 'ARY': 2, 'WEB': 2, 'KNT': 2, 'HRN': 1, 'NYB': 1, 'BQT': 1, 'FSF': 1, 'IEC': 1}
```


## [2026-09-14T03:28:20.432Z] AGENT

Page 487 (book p. 457) verified — `data/verification/page-487.json`, `verify_check.py 487` shows 0 PROBLEM lines.

Counts: 2 non-redirect entries (3 redirects skipped), 18/18 nodes.
- Root verdicts: Su 2 confirmed, Suîğ plausible.
- Node verdicts: 8 confirmed, 7 plausible, 3 disputed.
- Ref checks: 14 supports, 5 partial, 7 not_checked (ETM and FVS have no digital copy; FVS is undefined in Nourai's Table IV).

Disputed:
- Su 2 → Celtic *sukko* → English **hog**: AHD/Watkins is the only backer; OED (via Etymonline) calls a British Celtic origin "improbable", and ME *hogge* originally meant a yearling animal (also sheep, colt), not a pig species.
- Suîğ → Avestan/Old Persian **haiz, pairi-xaezaŋuha**: Bartholomae lemmatises Av. *haēz-* (Vd. 21.4) as 'spürend, suchend umhergehen', and Gershevitch/Cheung 2007 file it under a separate root \*haiz 'search for pastures'; \*xaiz 'to rise' has no Avestan attestation. Also *xvîsat* is Darmesteter's reading that Horn quotes only to reject ('he began to sweat'), and no Old Persian form exists.
- Suîğ → Avestan **haxš**: Bartholomae has *haxša-* as a present stem of *hak-* 'sequi, follow' (PIE \*sekʷ-); Horn only reports that the Pahlavi Vendīdād renders it by *ā.xēzēt*.

Extraction errors: none in the words/refs (page image checked, `sources/refs/ocr/BOOK/487.png`). One gap: the printed page shows an arrow from the `haxš` box into an **empty unlabelled box** at the right, which the JSON does not represent — harmless but worth knowing if node counts are audited against the page.

Other notes for the owner: Nourai's `KLN:1561` for *syphilis* may be off (our scan's leaf mapping puts the entry nearer p. 1630); `HRN:102` for *haxš* should be 103; `MON:1979` could not be page-verified (local Mo'in is the 2-vol reprint).
