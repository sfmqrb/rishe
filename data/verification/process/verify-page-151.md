# Verification process log — verify-page-151


## [2026-09-05T20:24:19.214Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 151 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-151.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-151.json. Write /home/sfmqrb/git/rishe/data/verification/page-151.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 151` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:25:29.333Z] AGENT

I'll start by reading the instructions and the relevant files.


## [2026-09-05T20:25:30.031Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:25:30.050Z] TOOL RESULT

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


## [2026-09-05T20:25:30.228Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-151.txt"
}
```


### [2026-09-05T20:25:30.248Z] TOOL RESULT

```
1	=== PDF page 151 (book page 121) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ekwos : horse  (refs POK:301)
4	#1 (parent #0) [Avestan] refs=POK:301; DVS:42; BQT:1819 | aspa : horse ; aspa-bâra : horse load, rider ☞Bher 1
5	  #2 (parent #1) [Pahlavi] refs=BQT:119 | asp : horse ; asbâr : rider
6	    #3 (parent #2) [Persian] refs=MON; BQT | asb «اسب» : horse ; savâr «سوار» : rider
7	#4 (parent #0) [Avestan] refs=BQT; POK:1082; KNT; HRN:206; AEF:324 | tum-âspa : (with) strong horses ☞Těu ; keresa-aspa : (with) lean horses ☞Kerk ; višta-aspa : (with) gray or old horses ; baevare-aspa : (with) 10,000 horses ☞Baevare
8	  #5 (parent #4) [Persian] refs=None | Tahmâsb «تهماسب» : with strong horses ; Garšâsp «گرشاسپ» : with lean horses ; Goštâsp «گشتاسپ» : with old Horses ; Bîvarasp «بیوراسپ» : with 10,000 horses
9	#6 (parent #0) [Avestan] refs=BQT; POK:1082; KNT; HRN:206; MON5:419 | aršan-aspa : (with) male horses ☞Eres 1 ; aurvat-aspa : (with) swift horses ☞Er 1 ; arejat-aspa : (with) valuable horses ☞Algwh ; jâm-âspa : owning horses
10	  #7 (parent #6) [Persian] refs=MON | Aršâsp «ارشاسپ» : "with male horses" ; Gošnâsp «گشناسپ» : "with male horses" ; Lohrâsb «لهراسب» : "with swift horses" ; Arjâsp «ارجاسپ» : "with valuable horses" ; Jâmâsb «جاماسب» : "owning horses"
11	#8 (parent #0) [Avestan] refs=BQT:1819 | aspa-asa : horse food ☞Ed
12	  #9 (parent #8) [Pahlavi] refs=BQT:119 | aspast : horse food, alfalfa
13	    #10 (parent #9) [Persian] refs=None | aspast «اسپست» : alfalfa | extra: سپست
14	    #11 (parent #9) [Syriac] refs=BQT:119 | pespesta : alfalfa
15	      #12 (parent #11) [Arabic] refs=None | alfesfeseh : alfalfa
16	        #13 (parent #12) [Persian] refs=MON:2547 | fasfaseh «فسفسه» | extra: فصفصه
17	        #14 (parent #12) [English] refs=AHD:32 | alfalfa
18	#15 (parent #0) [Sanskrit] refs=MON:246; BQT:125 | asva-tara : related to a horse
19	  #16 (parent #15) [Pahlavi] refs=None | 
20	    #17 (parent #16) [Persian] refs=None | astar «استر» : mule
21	#18 (parent #0) [Greek] refs=AHD | hippos : horse ; philo-hippos : horse lover ☞Bhili
22	  #19 (parent #18) [Latin] refs=None | 
23	    #20 (parent #19) [French] refs=AHD | 
24	      #21 (parent #20) [Persian] refs=MON | Fîlîp «فیلیپ» : "horse lover"
25	    #22 (parent #19) [English] refs=AHD | hippopotamus, Philip
26	
```


## [2026-09-05T20:25:33.803Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-151.json",
 "description": "Read source JSON for page 151"
}
```


### [2026-09-05T20:25:33.841Z] TOOL RESULT

```
{
  "pdf_page": 151,
  "book_page": 121,
  "entries": [
    {
      "root": {
        "name": "Ekwos",
        "lang": "Indo-European",
        "refs": "POK:301",
        "gloss": "horse"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:301; DVS:42; BQT:1819",
          "words": [
            {"translit": "aspa", "gloss": "horse", "script": null},
            {"translit": "aspa-bâra", "gloss": "horse load, rider", "script": null, "see": ["Bher 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:119",
          "words": [
            {"translit": "asp", "gloss": "horse", "script": null},
            {"translit": "asbâr", "gloss": "rider", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON; BQT",
          "words": [
            {"translit": "asb", "gloss": "horse", "script": "اسب"},
            {"translit": "savâr", "gloss": "rider", "script": "سوار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT; POK:1082; KNT; HRN:206; AEF:324",
          "words": [
            {"translit": "tum-âspa", "gloss": "(with) strong horses", "script": null, "see": ["Těu"]},
            {"translit": "keresa-aspa", "gloss": "(with) lean horses", "script": null, "see": ["Kerk"]},
            {"translit": "višta-aspa", "gloss": "(with) gray or old horses", "script": null},
            {"translit": "baevare-aspa", "gloss": "(with) 10,000 horses", "script": null, "see": ["Baevare"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "Tahmâsb", "gloss": "with strong horses", "script": "تهماسب"},
            {"translit": "Garšâsp", "gloss": "with lean horses", "script": "گرشاسپ"},
            {"translit": "Goštâsp", "gloss": "with old Horses", "script": "گشتاسپ"},
            {"translit": "Bîvarasp", "gloss": "with 10,000 horses", "script": "بیوراسپ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "افسانه شد حدیث فریدون و بیوراسپ - زین هر دوان کدام به مخبر نکوتر است",
            "poet": "Khâqânî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT; POK:1082; KNT; HRN:206; MON5:419",
          "words": [
            {"translit": "aršan-aspa", "gloss": "(with) male horses", "script": null, "see": ["Eres 1"]},
            {"translit": "aurvat-aspa", "gloss": "(with) swift horses", "script": null, "see": ["Er 1"]},
            {"translit": "arejat-aspa", "gloss": "(with) valuable horses", "script": null, "see": ["Algwh"]},
            {"translit": "jâm-âspa", "gloss": "owning horses", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Aršâsp", "gloss": "\"with male horses\"", "script": "ارشاسپ"},
            {"translit": "Gošnâsp", "gloss": "\"with male horses\"", "script": "گشناسپ"},
            {"translit": "Lohrâsb", "gloss": "\"with swift horses\"", "script": "لهراسب"},
            {"translit": "Arjâsp", "gloss": "\"with valuable horses\"", "script": "ارجاسپ"},
            {"translit": "Jâmâsb", "gloss": "\"owning horses\"", "script": "جاماسب"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دشمن دیو خوی چون ارجاسپ - حالش از هیبت تو گشته تباه",
            "poet": "Qâ`ânî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:1819",
          "words": [
            {"translit": "aspa-asa", "gloss": "horse food", "script": null, "see": ["Ed"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "BQT:119",
          "words": [
            {"translit": "aspast", "gloss": "horse food, alfalfa", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "aspast", "gloss": "alfalfa", "script": "اسپست"}
          ],
          "script_extra": "سپست",
          "note": null,
          "quote": {
            "text": "سنبل و سوسن کجا آمد بدست از روضه ای - کاندرو تخم سپست و سیر و سیسنبر برند",
            "poet": "Sanâî"
          }
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Syriac",
          "refs": "BQT:119",
          "words": [
            {"translit": "pespesta", "gloss": "alfalfa", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "alfesfeseh", "gloss": "alfalfa", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:2547",
          "words": [
            {"translit": "fasfaseh", "gloss": null, "script": "فسفسه"}
          ],
          "script_extra": "فصفصه",
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 12,
          "lang": "English",
          "refs": "AHD:32",
          "words": [
            {"translit": "alfalfa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "MON:246; BQT:125",
          "words": [
            {"translit": "asva-tara", "gloss": "related to a horse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Pahlavi",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "astar", "gloss": "mule", "script": "استر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hippos", "gloss": "horse", "script": null},
            {"translit": "philo-hippos", "gloss": "horse lover", "script": null, "see": ["Bhili"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "Fîlîp", "gloss": "\"horse lover\"", "script": "فیلیپ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 19,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hippopotamus, Philip", "gloss": null, "script": null}
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


## [2026-09-05T20:25:36.477Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','DVS','BQT','KNT','HRN','AEF','MON','AHD','WLD','BRT','PHD','NYB','HUB','ARY','SOD','KLN','SKT','IEC','SYN','CHEUNG','FVQ','AFM','PLA']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-05T20:25:38.496Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
DVS {"title": "P. Davies, Roots: Family Histories of Familiar Words, McGraw-Hill 1981", "edition_found": "1981 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsfamilyhisto0000davi (lending)", "identifier": "rootsfamilyhisto0000davi", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 202
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG MISSING
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
```


## [2026-09-05T20:25:42.499Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo ---- && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T20:25:42.554Z] TOOL RESULT

```
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
----
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
```


## [2026-09-05T20:25:43.163Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-124.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False)[:3000])\n\""
}
```


### [2026-09-05T20:25:44.887Z] TOOL RESULT

```
{"entry": 0, "root": "Dhě 2", "verdict": "confirmed", "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)", "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.", "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.", "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"], "ref_check": [{"ref": "AHD:1512", "status": "supports", "note": "Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the
```


## [2026-09-05T20:26:39.426Z] AGENT

Now let me research the local reference library. Starting with the IE root.


## [2026-09-05T20:26:42.291Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK ekwo ===\"; grep -n -i -E \"ek[^ ]{0,3}u.{0,2}o-s|ekuo-s|ek̂u̯o|Pferd.*ekuo\" POK_full.txt | head -20\necho \"=== POK 301 context ===\"; grep -n \"301\" POK_full.txt | grep -i -E \"page|seite\" | head -10\necho \"=== AHD ekwo ===\"; grep -n -i -A6 \"^ekwo\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-05T20:26:43.978Z] TOOL RESULT

```
=== POK ekwo ===
74514:Schlagworten *suelio[n]-, suesor-, suekuro-s, suekru-) are: 
=== POK 301 context ===
24780:Page(s): 299-301 
24796:Page(s): 301 
25106:Page(s): 301-302 
=== AHD ekwo ===
433:ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN, EQUINE, EQUITANT, (EQUITATION); EQUISETUM. 2. Greek hippos, horse: EO- HIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]
434-el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.]
435-el-2. Red, brown (forming animal and tree names). 1. Ex-
436-el-?
437-tended form *elmo- in Germanic *elmo-, *almo- in Old English elm, elm: ELM. 2. Germanic extended form *aliza, alder, in Old English alor, alder: ALDER. 3. Possi- bly Old English ellen, ellzrn, the elder: ELDER?. 4. Ex- tended o-grade form “olki- in Germanic “alkiz, elk, in Old Norse elgr, elk, akin to Old English eolh, elk: ELK. 5. Perhaps Germanic extended form *alk- in Old Norse alka, auk: auK. 6. Extended form *elno- in Greek ellos, hellos, fawn: HELLEBORE. 7. Extended form *elani- in Lithuanian élnis, stag: ELAND. [Pok. 1. el- 302.]
438-el-3, To go. Suffixed extended form *ela-un-yo- in Greek elaunein, to drive (< “to cause to go”): ELASTIC, ELATER, ELATERITE; ELASMOBRANCH. [Pok. 6. el- 306.]
439-[elaia. Olive. Greek noun (earlier form elaiwd) of Medi- terranean origin. OIL, (-OLE), OLEAGINOUS, OLEASTER, OLEO-, OLIVE; (AIOLI), (ANELE), (PETROLEUM).]
```


## [2026-09-05T20:26:44.674Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT aspa ===\"; grep -n -E \"^\\s*aspa-?\\b|aspa- .*Pferd\" BRT.txt | head -20\necho \"=== BRT aspō ===\"; grep -n -i \"asp\" BRT.txt | grep -i -E \"asti|fodder|Futter\" | head -10\necho \"=== BRT taxma ===\"; grep -n -i \"taxma\" BRT.txt | head -20\necho \"=== BRT vistaspa ===\"; grep -n -i -E \"vī.t.aspa|vishtaspa|Vīštāspa\" BRT.txt | head -10"
}
```


### [2026-09-05T20:26:44.777Z] TOOL RESULT

```
=== BRT aspa ===
27425:•  j.  srifa-  m.  'Nüstern':  yal .  .  aspa- nqmca  'fa  xsfufsqn  "und  wenn  die  Nüstern der  Pferde  in  Aufregung  geraten"  Yt /0.113.
=== BRT aspō ===
3112:rim  stagr»m  (sd.)  arijö  V,  7. 41;  43'; —  uitraAe  k?hrpa  °yehe  P.^2;  —  aspahe paiti  arshö  °yehe  "um  einen  Rosshengst erster  Qualität"  V.9.37;  37';  —  dvada- satih£ir3m  (sd.)  asti  "rim  ayan  F.  27  b; '";  —  'krisatdkw)m  frasnütse  .  .  "yqtn paiti  usnaitJm  ".  .  (also)  mit  Abwaschung erster  Ordnung"  V,  Ä  98  (?) '' ;  —  mi>nm  . . taxm?m  mainyaam 'rJmYtw.i 40.  [P. 32:  lies  ayryö.mdaimasl°.'\
4678:maca  *frast3niite  .  .  ditSi  °iiye  (NPm.)  .  .  'nyeke  räkWB  V.  7.4.  I  i)  wiederholt *vaäsäz*/ramravainti..vTspa^qmia  aiwi.'  'Aex  eine  .  .  der  andere';  dsityB  *'inyS'^ srurwai/i  (sd.)  K.60;  —  aivB  pants  yB  havam  {^d^  *daityö  ^'inyB^  ya'ia  *va  . . a^ahe  vTspe  'nyalhm  apatitqm  {%A.)  \.y2.  li.107;  P.57;  —  yal  he  pukra  us^zaydi^e 11;  —  ^pasävi^  adam  käram  ..fraisayam  , .  .  tiaisB  'nys  .  .  aat  'iiyB  ,  .  Y.5. 10;  — hyt^  upa  mäm  äkJ* , .  hyJ^  °niyJ'  kärJ'  avi  *'iiy3^^  suruiiraiti  (statt  Du.)  nsil  'inyS ".  .  reliquus  exercitus  . ."  Bh.^.6;  —  eä  'S. 24;  — yay^  osH  'nyS  rasnus  razUtB asti  masyB  ..  an^rn  datpm  ..upairi'tiyai^'W.J^.^'PüZ.  (unvollst  Zitat);  — \,°myam sraväis  .  .  !  .  .  ya'^a  zrayB  vountJtahm '  (näml,  käram)  *ustrabilrim  akunavam upairi  °nyh  äpB  V. §.32{.;  —  vayaol . .  'myahyJ  aspilf^A^ paiiyariayatn^'Acnem^a taratatB  (Stverz.)  'tiysis  (als  APn.)  dämqtt  \  Teil  (des  Heers)  machte  ich  kamelberit- Y.22. 24;usw.; —  \' a^urcrmazdämaiy  upas-  ten  .  ."  Bh.7. 18'';  5. 4;  —  armaeflä  'iiyA
6263:äfaiÄ  Y.  7<?.2o; —  vahilt?m  akßm  'Saonqm raocaahpm  (Stverz.)  Y.  (J.19USW.;  —  xshätä 'saotiatn  urvänS  pärayänti  .  ,  avt  garö nrnaium.  V,/(),33;  *Y.  2.4,  *42.4;  —  kaur- TtUa  am^nläta  ySi  sis  mlzd?m  'saonam parSMsH  jasMiqm  Yt.  J.  25;  —  vJspim 'iavansfH  vahiltjm  ä  oAüm  ä.baraUi'S.24; — iäbm  *dä^aifi  urvqtam  'saonS  *irfn'^3- naht  F.  24.;  *_J5;  —  vis/ipm  "iavafum  .  . kvavayarsÄ^m  jas>nt»m  paiti.baraAi  Y.55. 4;  —  t3  ahmt  nm3ne ]amy3r?? yä  'saenqtn xtnstatca  aSayasca  Y.  60. 2;  —  ya^raca xihaa  'sava  Yt7y.36;  25;  —  -savamm ti  'iaonat  äfyeihyai  (sd.)  mraomi'^.-ji.\y, —  visp»m  'iavarum  vlspäi  'saone  para.- cinasti  Y.20.2;  a';  —  vahistim  'iovamm vaiüitäi  °iaone  Y-2/.4;  —  tumas?  tS dä'^rö  baxt»tn  vahistäi  -saone  anazq^äi 'sttone  V.  2M;  —  tumd  aAurSt  mazdäi tvms  atnsiaiikyS  spmtalibyS  rrnnS  anyailqm (sd)  'saonqm  V./().2s;  33.  Yt7.3o;  '— yähaZa  zhayenU  °Iaone  ahm  anasti  Y.  20. 3;  YL/J.  24;  —  amamm  ..  yas»  %ws  .. ynaite  6arö.taohrS  'sava  "das  Haus  des Gläubigen,  der  zu  dir  betet .  ."  Yt  /0.30; 56;  —  •savaram  vahistsmea  avasöjcla- 'inmca  Y.  ig.^a;  —  nSit  'savarum  aint^tii (sd.)  ästarayei/i  P.  12;  ^N.JOj?";  —  aipi.- Pänrnnäi  ,  .  'saone  V.S.ioj;  —  näämnäi (i&.)'säone'V .g.^o;  —  'iavanum  makrka%äi Y.  79. 1 2 ;  —  kaaa  nS  '/aum  agats  .  .  V. '5-  3  ' ;  Y.  7/.  1 6 ;  —  "iavansm  manaspaoiryS V.  19. 19  {?);  —  sava  'SavabyS  yazatnaide Vr.i^j.i;    Y.77.6'.  a)    von    nament-
6288:—  avä  dämqn  'ZavanS  (als  APn.)"'  .. yä  hmti  paoirya.d3ta  Yt.-j.^;  —  sfimtö.- dätäis  dämqn  'idvanB  (als  APn.)*"'  Vr. 75.1;  1;  —  vTspe  .  .  k)  asti  voku  'sava antan  tarn  asmatamca  Y.  68.  15;  — xartmcS  yim  'lavansm  Y.  42.4;  —  'im-a (ASn.)  yra^a.savs  Vr.  7p.  2  (?) ;  —  aspi>.- kthrpqm  (sd.)  'laonlm  YtÄ8(?);  — mSurum  'Savan»m  V,  7.5;  16;  —  kat)haya . .  -savanaya  (LSm.)  Yt5. 54;  —  Hnval-- ppr?tBm  ..  'saortlm  S.  2. 30;  — garayS  . . 'lavana  (als  APm.)  Y.  2. 14;  —  dunman .  .  maeyS.kara  °savanJ  (als  NPn,)  '">  Yt. ^■^y,  —  urvarqm  'laonTm  V.7p.35;  Y. 2, 1 1,  N.  77,  57;  —  urvaire  .  .  masdaü3te 'saone(Y^{.)  Y.if).i8,  Yyt  22;  ~  haema .  .  spitita  '/avana  (als  NP.)  Vr.().  3;  — äp3  . .  '/aenis'Y.2.12',  16.4,  Ö5.7,  ö'(?.7; 2.5,  Yt2. 12;  —  imai  6ar>sma  .,  'sava- tum  aiahe  ratüm  Y.  77.23*';  —  ralavff upapanqm  . .  upasmanqm  . .  "saonqm  asahe ra^wqm  Vr.  7. 1 ;  —  dalnqm  . .  'identtn Y,72.9;  YtJj.ioo;  —  xratüm  °savan>m
7423:eifer"  V.  .^p.  10;  —  daStiqm Syaoiianä  »nS  daidyai  (sd.)  Y.44-io',  — tsm  iiS  yasnäis  'töÜ  mimayzS  (sd.)  Y.  45- 10;  - —  ahyä  *mamyJuf  .  .  vahiStun  .  . Siänü  .  .  °töis  zastsibyä  iyad^anä  vsrpzyai Y.  47.  z;5/.  21,  5^- 3;  —  'matte  dar>ir»m P.  26'(?)'';  —  sp>ntqm  v3  °ffm  va^uAlm vanmaidl  (sd.)  Y.js.  2";  —  vaauAimal /s^atßm  (sd.)  vaauAim^ä  'timY.3y.Si  — vanhuyS  *fs»ratvS  vauhuyä  "tsil  Y.  _j_'y. 5.  a)  Plur.  in  Verbindung  mit  Jiä- usw.,  Flur.:  ySscä  tsi  g>nS  ^ahura.mazdä .  .  liii  yaoitayB  foraitayS  'iayS  (als  AP.) . .  yazamaidi  ". .  den  Glaubenseifer,  die Rührigkeit,  das  Sichberatenlassen  und  die Frommergebenheit.."  Y._jÄif.  A)a]s Gottheit  (Am^saSp^/ita)*'';  I)  im  gAw.: yy  sfvistff  (sd.)  ahurö  mazdascä  'tis/ä aspm^ä  Jrädaig:a£i»m  (sd.)  manascä  voku
7446:•  j.,  g.  asav-  Adj.  'schnell,  rasch':  yä (mi^rs)  'sutiqm  °sus  Yt  10.  65;  —  srao- f^m..laxmym  "jäot  Y.57.1 1;  —  aurvanfym ..yS  °sui  asti  uzgasts  Yt5.i3i;  —  Aqm.- varfittm  . .  yä  saot  *äsyayä  Vr.  7.  3 ;  — buyät  -suua  asps  dtnzrasca  *vais  Yt  13. 52;  —  aspatfks  . .  °savö  Ytij.  12;  — i!  väiäi  dvqnmaibyasca  (sd.)  yaog^t  'sa (ASn.)  sva. '  'die  Schnelligkeit'  Y.  44, 4,  a)  ASn.  'SU  als  Adv.  'cito':  dayä ml  .  .  -SU  Y./i2.4i;  F.  7.
7883:1)  'hin  zu  gehen  zu -',  mit  Dat. ■>  (statt  ,_(,aj«,j,-  Vr.;5.2;  V.jff.i^s'  (wo  "0,7),  2;. Akk.):  husiti  ..  äanyuMti  (sd.)  ite  vJse  (,^  Yti-agS;  —  aim  mSt  'äS  iw/y  (sd.) afrXnümi  yahmat  haca  . .  ".  .  in  (dessen) ' yj  „5  a?i-ö  . .  Y.  2(J.8;  —  iv//tt  -ö«  . .  hvar- Haus  zu  gehen,  von  dem  .  .'■  ^.6S.^lt)m  lyaoi:ni>m  S-s^i^i; —ya>a  yat '<.a 14.  a)'einzugehenauf-':iJOTff^^ä^W/|ana/rj'rf  daiühus  hakat  m^a  us./raraysil moi  data  danga/tya  *yaoi  ySm  vä  *nagas  (sd.)  YL  75.68;  V. 5.56,  y.55;  —  ime  nö däfMt  its  vairya  stdt/isd.)  "..ihn  sollt  ihr|.  .  aspa  para  *miira  *'c,a'>  iiaymU  (sd.) mir  gewähren,  auf  den  einzugehen  keiner  yt.io.  42;  60;  —ha  hl  asti  ä>a  ..aipi.- euch  zwingen  kann,  (den  Wunsch) .."  Y.  panmnäi  'oa  aSaone  V.Ä107;  —  ktj'M 43-^'h-  'ffff(sd.)''oa  alsum  agate  Y.ig.^i;  —  'oa
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
8197:astiy  kartam  "und  nach  dem  Willen  A/1M.5 ist  von  mir  noch  viel  andres  getan  worden" Bh.4.8.  a)  nachgestellt '>  hinter  a'i^ä  und ya'^3:  a'ia  *hax>mqm  hyät..  a^ä  vS  'ta AyamiJ  Y.40.4;  —  ya^/j  ap  'tä  nä  vä tiairTvä  valdä  hatitm  Y.  J5.6.  III)  zur Anfügung  einer  partizipialen  Ergänzung  der Aussage:  tarn  yazata  kaosya»h6  .  .  sat?m aspanqm  .  .  °ta  zaoirqm  frabarS  Yt.  p.  3. Undeutlich:  Y./o.7,'YL2.3';  IIBh.5.1% 3,  4>  6',  D.  77.3.  [Yt  75.47:    lies  uiti
8421:•  j.  upäzana-  n.  'was  Jemandem  als  Busse zudiktirt  wird,  körperliche  Abstrafung, Hieb':  ka  hs  asti  (li-al  .  .  panca  'na aspahe  aSttaya  panca  sraosJ.caranaya ".  .  fünf  Hiebe  mit  der  Pferdepeitsche, fünf  mit  dem  Zuchtriemen"  V. 4. 18;  18, 18  ("10,  15  Hiebe");  —  ^risat^m  'nanqm upäzsit  (sd.)  aspahe  astraya  'irisatim sraosS.caranaya  ". .  30  Hiebe  . ."  V.^.19; 19,  19.  19-20,11,  6.21,^.36,4.12,13, Mi  15.  J'37,  H--i  {dRn.  "50,  70,  90,  200,
=== BRT taxma ===
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
4754:—  yal:iä  ro  data  °/il  (VP.)  spsntä  a^iä na  >räzäa?n  Y.5#.  5;  II.  iZ,  14.  i,  42.1, • — ■  mai^amnt  . .  yat  ksrmlun  "la  (NS.) sp>nta  vispe  hazaesaYLio.$i;  7.3',  /0.92, y.ga,  Y. 57.^23,  60.6;  —  /ml  '/ä  (NP.) spmtä  gaiia  giurvain  Y.2S.0;  Ny.l.i, VyL^o;- —  spmtsttg  °s3ng  yava^yff  yavaSsvB Y.,J.')-3;  4-A\  —  °^^  sptrüa  huxiäi:ra hmfmhs  (Stverz.)  Vr. ;/.  12;  usw.;  —  -sS spints  vatihali  srlräi^  namqn  äebaya  Y. /  5. 1 ;  Vr.  6.1;  —  vlspqscä  'iq  spintq  yasa- maidsY.42.()\  —  °h  spinlS alaonam  yasa- maideY.yi.2,  G.  2. 6  (wo  'sJtca);''*  — 'sanqm  sp)ntanqm  xialtanqm  vinzidsi- %ranqm  Ötnzatqm  aiwyämanqm  taxmanqm ähuiryanqm  ySi  aihy^anhs  alwvanB  ysi hapta  iam^.manavAö.. Yt  lj.82f.;Y.j. 4, 20,3;  — y3i  hapta  'sä  spmta  Yt.2.3;  — ape  °ianam  spmtanqm  dähXtn  Y./9.8;  Yt. ;^.  8 1 ' ;  —  vankubyS  yazataiibyS  yat  'laii- byS  spmtaHbys  Vr. 8.\;  ff. 4, 13. \,Yt.4.y,
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5555:•)    Über   die   Bedeutung   des  Gotls   ist   den    t'isjie  °va   Vlspe  taxma   .  .  kave  HK.1Q.1z; ,i'j5i sehen  Teilen  nichu  Klnies  lu  entnehmen;   —    'v3  as.vancS   kava    usa  Yt5.45;   —
5713:idn^taxma^  näma"  °tiyi^    Bh.^.  i  /p.g,  Yt  /_y.  28;  —  öarjimrS  ^avaühe  'htS
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
7470:•  j.  äsu.aspya-  n.  'Besitz  schneller  Rosse, Reichtum  an  schnellen  Rossen':  'pTm da'jiiiti  mi%rU  Ytjo.3; —  '^wqm  naracit yöi  taxma  Jat'iyhnte  -ptm  YL5.86;  98.
8304:—  mihnm  .  .  yetike  valnn  Aangrgwnäiti asii vamihi ..yat  dim  dätnBis  °ns  AuÄrixtim (sd.)  .  ,  irinaxH  YL/O.  68;  —  dahmaya vaakuyi  a/ritöii' uyrni  dümsis  '■näi  \.fi.t, S. /.30; —  uyraAe^a  taxmaAe  dämsii "nahe yazatahe  Y.  /.  1 5 ;  —  uyr^m  taxmem  dämeis 'n?m  Y.2.1S,  7.26,  77.23.
8334:•  j.  upara'tSt-  f.  'Superiorität,  Über- lefenheif:  ^wam  nara^it  ysi  taxma jai'jyhrtte  .  .  sfarfttanAasca  'tätS  (AP.) YL5.86.  a)  sonst  mit  vananl-  Adj.: dasdi  .  .  tai  äyafUm  .  .  V9r9%rar}n}mea aAurdoat?m  vanaintimla  *t3t>m  Yt  ro. 33;  5-86.  y-34.  A'i,  X-57-33;  —  vin- liraynaAeca  . ,  vanaintySsca  paiti  'täto  Yt. 8.11.  A)  als  Gottheit:  avistayalca  .  . amavaihya  faurvatäis  amavaihyä  Häts (GS.)  Vr.(f,4.  a)  sonst  mit  vanani-  Adj.: v^ry^rayramca  ..vanaintimca  '/aftw  Y.2.6; Vr.2.8;  —  vfhhraynahe  .  .  vanainiyäsca 'tätö  Y./.6,  Vr./.6,  Vt.J4.o.
10879:•  j.  xStävay-  Adj.  'zur  Familie  der Xstavay  gehörig,  Xstavi-^a.nvi^ -.  ysi  taxma 'vayS  dänubyö  azm  pilana  Yt  13. 37 ;  38.
11331:•  p,  tSi&'a°'taxma-  m.  EN.  eines  Sagar- tiers,  der  sich  gegen  Darius  I.  empörte,
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
11819:taxma-  62Ö
11841:*  j-i  g-  (.  P-)  taxma-  Adj.  (fem.  °mä-) 'fortis,  tapfer,  tüchtig,  energisch,  helden- haft'; a)  von  a)  Menschen  und  ß)  Göttern: a)  masyänqm  .  .  'manqm  V.  20.  i ;  —  nä •Mö  Yt  jj.  67,  Aog.Ä^;  Vyt.  2j;  —  narU 'ma  (NPm.)  Yty.  27;  5.86,  iS-Hn^^h
11843:627  taxman-
11845:•  j.  taxman-  n. 'Lauf  fliessenden  Wassers: %risum  apqm  '^raotö.stäcqm  °manqm  pairi- itayeiii  "ein  Drittel  der  im  Flussbett  fliessen- den Wasser  hindert  er  an  ihrem  Lauf V.  7*63.
11847:•  p,  taxma-späda-  m,  EN.  eines  Heer- führers Darius  I, :  'dc^  näma'  madei'  Bh. 2.14;  14.
11851:•  j.  taxmö.Mma-"'  Adj.  'der  tapferste, energischste,  heldenhafteste' :  taxms. .  "tsma (stattNSna.)  n^ffia  ahmt  Yt  73.46;  —  vamt ('den  Vayav^)  taxmanqm  'tsm^m  Yt  75.  57.
11894:'damit,  auf  dass'  vorher:  yat  yavo  (sd.) pourus  baväf  aha  ma'hnm  *t'  ^  mairyat ^•3-a-  3)  'damals,  da',  ini  Wechsel mit  ta6a  (sd.)*':  tala  dim  akurS  mazdä avqn  (Sp.  1 1 2  m.)  . .  t°  apu  urvaras<a  YL 8."];  —  fravasayS  .  .  yä  .  .  laoa  nijasm (Sp.  500  m.)  xÜiviwyS  *pi^  yöi  taxma xstävayB  dänubyS  az>n  pthnh  Yt.  13. 37.  4)  'dann,  alsdann':  yas>  t  *api- vataiti  (sd.)  parmtarim  (sd.)  issil  N. 12.  a)    zusammen    mit    aaf:    US  patti
11988:•  j.  tan£iita-  Adj.  (fem.  'li-)  'der  tapferste, energischste,  heldenhafteste';  i)von  a)Men- schen  und  ß)  Göttern:  a)  tBtn  xara^u/tra .  .  yö  aojists  .  .  °ts .,  %waxiWs . .  abaval mainivä  dämqn  Y.p,  15;  —  'timca  darae- ^at»«  YL3.73;  —  häuca  ii:ra..taxmanam
=== BRT vistaspa ===
```


## [2026-09-05T20:26:50.974Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24770,24800p' POK_full.txt"
}
```


### [2026-09-05T20:26:51.029Z] TOOL RESULT

```
Maybe alb. Ilura : zero grade alb. {*llura) Lura PN 

the full grade *E/5- besides in Tsarcus sWW in many Baltic FIN: *Eisia, Lithuanian lesia, 
* Eisia, Lithuanian lesIa, Lithuanian Eisra, etc. (Buga RSI. 6, 9 f., Rozwadowski RSI. 6, 47); 
whereas Buga introduces back wruss. Istra, Latvian Sea name Istra, Lithuanian FIN Isra, 
Old Prussian FIN Instrutis^ Inster ' and thrak. "lorpoqfrom *lnstr-\ yet one could explain 
"laTpo(; from *ls-ro-s\ 

References: WP. I 106 f., WH. I 717 f., Schwyzer Gr. Gr. I 282, 4825, 491, 679^, 681, 694, 
700, 823. 
Page(s): 299-301 

Root / lemma: ei-s-2, ei-n- {*heis-) 
Meaning: ice 

Material: Avestan isu-^ icy', aexa- n. "coldness', pamir. /s'coldness', osset. yex, /A-'ice', 
afghan. asa/'frost' (if from inchoative formation *is-sR-l\ different Specht Dekl. 18, 201, 
234); 

Old Norse fss, PI. fssarm. 'ice'. Old English /sn.. Old Saxon Old High German Middle 
High German /sn. "ice'; 

Balto Slavic *//7/a-m. and Tmia-vn. " hoarfrost ' in Church Slavic inej, //7y" snow flurry', 
russ. fnejm. and Old Czech y//7/en. " hoarfrost ', Lithuanian yn/sm. (also fem. /-stem). 

References: WP. I 108, Trautmann 104. 
Page(s): 301 

Root / lemma: ei- {*hei-) 

Meaning: to go
```


## [2026-09-05T20:26:52.553Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 1082 ===\"; grep -n \"Page(s): 108[0-9]\" POK_full.txt | head\necho \"=== KNT aspa/asa ===\"; grep -n -i -E \"asa- .*horse|asabara|Vishtaspa|Vištāspa|Vistaspa\" KNT.txt | head -20"
}
```


### [2026-09-05T20:26:52.631Z] TOOL RESULT

```
=== POK 1082 ===
86809:Page(s): 1080-1085 
86950:Page(s): 1086-1087 
87066:Page(s): 1088-1089 
=== KNT aspa/asa ===
423:xsdyabiya : dahytiném : Vistaspahyà : Dérayavahaus : z5ayattyahyà : puça : Haxámanisya : puça : Haxdémanisiya : hya : imam : lacaram : akunaus
498:III; but Vistaspa etc. elsewhere.
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
1566:wvüsabüra ‘good horseman’ (*hv-dsa-), to asa- ‘horse’; asabaéra with d is rendered probable by the unlengthened vowel in uSabart- ‘camel- borne’.
2800:IV. This pronoun as article occasionally pre- cedes its noun to attach to it an adjective or a genitive; there are these examples: DB 1.8 and DBa 12f hyà атахат iauma; DB 1.28 tyand mand айй, cf. DNa 21; DB 3.32 hya aniya kāra Parsa; DB 4.87f tyäm imatsam martiyanàm taumam; DB 5.12 tyamsém тай йат; DNa 56f hyd Auramaz- daha framünà; ПОЇ 12f hya тала mia Vistaspa
3046:$308. Тнк Position or Apposittves. Apposi- tives, whether nouns or adjectives, usually follow! that to which they are appositive; but the position is otherwise free. Appositives to a subject implied in the verbal ending may stand in any place; cf. DNb 41-5. Chiasmus sometimes is the result of stylistic considerations: XPh 47f уйа ahaniy Jiwa щй marta ariàvà ahaniy ‘happy may I be while living, and when dead blessed may I be'; DSf 12f hya mand pità Vištāspa ша Arama hya mand niydka ‘my father Hystaspes and Arsames my grandfather’, in which the appositive precedes in one instance,
3463:4 Darayavaus : xSayafflya : manā : pita : Vistàspa : Vistaspahyd : pità : Ars
3553:КІ. has the following correct readings, in which he reeords as visible certain characters, here indicated by roman type, which were not visible to KT: !zsiyattya |: zsayal9iy-; * dahylinam; 4 ViStaspahya; * zšāyaðļiya; М adamsam,  Horauvatis; mand;  "* Dàrayava-; 2 ай]; ?* алайа; 9 Bardiya; ?! büjilya : avam; ^ pasá]- va; S Aya; " par[ulva[m]eliy; 2 Аста; *agau[balà; 87 Auramazddmaiy; 9 ауада; * Bübirum : yale; * miam; М hamaranam; **dpryà.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3636:93 kana : hamiciya : abava : hacáma : Fravartazf : agaubatà : Vistaspa : mand : pita : ha
3637:94 uv : Paréavaty : aha : avam : Ката : avaharda : hamigiya : abava : pasava : Vištāspa :
3751:72 15 : asabaraibis : айтуауа : Aršādā : пата : didà : Harauvatiyà : а 73 vapara : atiy&i$g pasáva : Vivàna : hada : kara : nipadiy : tyaiy :aNya © 7777 74 va : avadāšim : agarbaya : ula : martiya : tyaisaly : fratama : anuSiya :
3961:4 ArSimahyi : napá : HaxàmaniSiya ; даћу : I 7 Раа 1 5 yavauš :xSáyaüiya :manà:pità: Vistaspa ;Vi — : 6 štāspahyā : pità : Arsama : ArSamahyà : pi
4037:DPa = Darius, PERSEPOLIS A. 1 Darayavaus : xsayafiya : 2 vazraka : xsdya(lya : x&à 8 yafiyánàm : xšāyaðiya : 4 dahyünàm : Vistaspahy 5 à : puça : Haximanidiya : h 6 ya : imam : tacaram : akunaus
4067:4 $4m : parünàm : Vištāspahyā :
4204:DSc = DaniUs, Susa C. adam : Darayavaus XS : vazraka XS XSyanam : ViStaspahya : риса TRANSLATION OF DSc: I am...(= DPa 1-3, 4-5). DSd = Danrus, Susa р.
4206:2 ahyáyà BUyà Vistaspahya : puça : Бахатал уа ba
4245:10 w : mam : XSyam : akunaus : haumaiy : ima : xša П gam : frábara : tya : vazrakam : {уа : uvaspam : uma 12 rtiyam ;'valnà : Auramazdaha " hya : mand : pita 13 : Vištāspa : uta : ArSdma : һуа : manā : niyàka :
4321:DSk = Darius, SUSA К. 1 adam : Darayavaus : XS : vaaraka : XŠ : XŠy 2 anim : XS : DHnàm : Vistaspahya :
4393:3 ünàm : XS : аћудуд : 4 büm?yà : vazrakáyà : 5 Vištāspahyā : pu
```


## [2026-09-05T20:26:59.986Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Meaning: horse\" POK_full.txt | head\necho \"--- lemma with horse ---\"\ngrep -n -i -E \"Root / lemma: e.?k.?u\" POK_full.txt | head"
}
```


### [2026-09-05T20:27:00.061Z] TOOL RESULT

```
25047:Meaning: horse 
57432:Meaning: horse 
--- lemma with horse ---
```


## [2026-09-05T20:27:01.597Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC ekwos ===\"; grep -n -i -E \"ekwos|ekṷos|equos.*horse\" IEC.txt | head -10\necho \"=== SYN horse ===\"; grep -n -i -E \"^4\\.2[0-9]|equus.*hippos\" SYN.txt | head -10"
}
```


### [2026-09-05T20:27:01.673Z] TOOL RESULT

```
=== IEC ekwos ===
3516:eKuos, à “horse; mare’. WP I, 113 Skt. á$vah, -à; Av aspo, -a; OPer. asa-; Medic aspa-; Per. asb; Oss. jàfs, äfsä ‘mare’; Per. (in Gk.) as- in as-trábe, as-tándes, and cf. peg-asos “flying horse’; Tokh. yuk, B yakwe; Arm. es, dim. iSuk ‘donkey’; Hurrian (in Hitt.) asu-sani ‘horseman’; H-Hittite a$uwa-; Lyc. esve-; Thrac. cf. -espios, -aspios, adj.; Venet. ekvon (acc. sg.); Mlr. ech; Ir. each; cf. eachan ‘gale’; Gaul. epo-; Sequanian equos, pl. ‘gales’; Br. cf. é-al, éb-œl, W eb-ol ‘foal’; cf. Br. kén-ep, -eb “in foal’; OE eoh; ON jór, beside ess; Go. cf. aíhva-tundi (&horse-tooth', i.e. ‘briar; OS cf. ehu-skalk, m. ‘groom’; OLi. esva, Li. a$va ‘mare’. Extended forms; eKuolos, à in Lat. equulus, a: W ebol; Cor. ebol ‘colt, foal’; eKu-ridh- in Gaul. epo-redias, acc. pl. *horse-tamers'; OS eorid-folk, ierid-
=== SYN horse ===
5195:4.29 Turoar 4.30 SHovutprer
5564:4.20 HHAD Grk. _xedady, xapa (poet.) Goth. haubip Lith. galva NG Kepare ON hofud, haufud Lett. galva Lat. caput Dan.  hoved ChSl. glava It. testa, capo Sw. huvud SCr. glava Fr. léle OE héafod, hafela Boh.  hlava Sp. cabeza ME __heved, hed Pol. glowa Rum. cap NE head Russ. golova Tr. cend, cenn Du. hoofd Skt. ¢iras-, cirsan-, NIr. ceann OHG = houbit mitrdhan- W. pen MHG houbet, kopf Ay. sarah-, sdra-, vayda- Br. penn NHG kopf, haupt na-, kamaraéa-
5592:4.202 SKULL ne ae Goth. hwairnei Lith. kiau¥é, kaukolé Lat cae enene ON hauss Lett. kauss ee Dan. hovedskal, hjerneskal ChSI. kranijevit (adj.), libit Ir is Sw. huvudskalle, skalle SCr. lubanja Sp. craneo (cal OE héafodpanne (-ban) Boh. eb, lebka Rum. Bante ee) ME skulle, pan Pol. czaszka in) Spe NE skull Russ. erep Nh, cloigeann Du. schedel Skt.  mastaka-, kapdala-, W. penglo 9 OHG hirniscala karpa rda- Br. klopenn MHG  schedel, hirneschal Av. mastrayan- (in pl.) NHG  schédel, hirnschale ords for ‘ ? a f : hate with Words ee : nome are cog- | relation is with words for ‘bowl, cup’, Such with Words for ead’ or epds. of etc., owing to the similarity in shape and
5682:4.205 FOREHEAD
5714:4.206 EYEBROW
5731:4.207 JAW 4.208 CHEEK 4.209 CHIN
5768:4.207. Several of the words for ‘jaw’ owe this use to some resemblance in shape, as that of a ‘sickle’ to the lower jaw in side view, of a ‘wagon, cart’ to the palate or upper jaw, of a ‘box’ to the
5811:4.208. In several of the words for ‘cheek’ this sense is clearly Secondary to ‘jaw’, and in some itis a specialization of ‘face’. Others are mostly based on a no- tion of swollen or curved rounded sur- face.
5922:4.24 MOUTH Grk.  orépa Goth. munps Lith.  burna NG oroya ON munnr (midr) Lett. mute Lat. Gs Dan. mund ChSl. usta It. bocca Sw. mun SCr. usta Fr. bouche OE mip Boh. iista Sp. boca ME mouthe Pol. usta, geba Rum. gurd NE mouth Russ. rot Ir. gin, béoil Du. mond Skt. mukha-, Gs-, ete, NIr. _béal OHG mund Ay. Gh-, zafar- W. geneu MHG munt Br. genou NHG mund
5947:4.25 LIP
```


## [2026-09-05T20:27:05.163Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '25040,25110p' POK_full.txt"
}
```


### [2026-09-05T20:27:05.225Z] TOOL RESULT

```
" way, row of mowed grain ', Swedish mundartl. an 6s. 

References: WP. I 102 ff., WH. I 406 ff., 658 f., 668 f., 723, Schwyzer Gr. Gr. I 674. 
Page(s): 293-297 

Root / lemma: eRuo-s {*heRuo-) 

Meaning: horse 

Note: 

Horses were often considered the most precioys sacrifice for the sea god. That is why 

from Root/ lemma: sAr"'^- (correct alcS). ek"- {* hek"^ : 'water, river' derived Root/ lemma: 

eRuo-s {* heRu-): 'horse'. 

Material: 

Old Indie asva-h, Avestan aspa- Old pers. asa- 'horse'; about osset. yafssee below; 

gr. TiTTToq ds. m. f. (originally without Asper: "AAk-itttto(; etc.); 

thrak. PN BsTsanioc;, OuTaaTTiO(;, Autesbis, Esbenus, Lycian KaKaapO(;; about Lycian 
esbe-di^ cay a\ry' (Phrygian loanword?) s. Pedersen Lycian and Hittite 51, 67 {*eRuiio-m?); 

Latin equus^a horse, steed, charger' (compare Oscan names Epius, Epidius, EpetTnus, 
yet s. Schuize EN 2204, 355); 

Old Irish ech, gall. epo-(\r\ Eporedia, Epona^ The Celtic horse goddess whose authority 
extended even beyond death, accompanying the soul on its final journey ', etc.), cymr. 
corn. ebor\od\s' {*epalo-); 



Old English eohm., Old Norse /io^'horse', Old Saxon in ehu-ska/k' groom, stableman ', 
Gothic in a/fva-tund/"br\ar' ("*horse tooth '); 

Tocharian A yuk, Gen. yukes, B ya/rwe "horse' with prothet. y(as in ossei. jafs. New 
Indie dial. yasp6s.)\ out of it borrowed tijrk. etc. Juk^ horse's load ', from which russ. Juk^ 
gaumlast ' etc. 

Common /7->y- Slavic Albanian; /?- >7-, y- Old Indie Tocharian. 

About Latin as/nus'an ass', h/nnus ' {r\u\e' , (under the influence of common Celtic -/7S-, - 
/?/- > -nn-), gr. 6vo(; etc. s. WH. I 72 f., 647, 849. 

fem. Old Indie asva, Avestan aspa-, Latin equa, Old Lithuanian asva, esva^mare' (the 
formation held by Meillet BSL. 29, LXIV rightly for single-linguistic, Lommel Indo Germanic 
Fem. 30 f. for previously proto form); 

Old Indie asv(i)ya-, Avestan aspya-, gr. TnniO(; ' of a horse, of horses '; Latin equTnus^ of 
a horse, of horses ', Old Prussian aswinanu. "kumys, mare milk', Lithuanian asvfenisvn. 
"stallion', compare also FIN Asvine, Asva; gr. inn6T-r|<; " equestrian, horseman ' : Latin 
eques, -itis m. ds "a horseman, rider', (letzteres from *eq"ot-). 

The gr. word could exist because of tarent. epid. \kkoc, lllyrian loanword; compare 
Pannonian PN Ecco, Eppo, maked. PN 'En6-KiAAo(;, the builder of the Trojan horse 
'Ensioc;, VN EnsioT in lllyrian Elis, etc. (Krahe Festgabe Bulle 203 ff.); neither the Asper 
nor I can be explained by gr., yet the various treatments from ku-\v\ gr. were not surprising, 
because also the labiovelars are treated dialectically differently there (Risch briefl.). 

References: WP. I 113, WH. I 412 f., 862, Trautmann 72, Schwyzer Gr. Gr. I 68, 301, 351, 

499. 

Page(s): 301-302 

Root / lemma: elg- 

Meaning: miserable, poor
```


## [2026-09-05T20:27:14.763Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=86740 && NR<=86815' POK_full.txt | grep -n -E \"Root / lemma|Meaning|Page\" \necho \"====\"\ngrep -n -B2 -A4 \"Page(s): 1076\\|Page(s): 1077\\|Page(s): 1078\\|Page(s): 1079\" POK_full.txt | head -40"
}
```


### [2026-09-05T20:27:16.464Z] TOOL RESULT

```
70:Page(s): 1080-1085 
72:Root / lemma: ff-ti- (ti)til- 
74:Meaning: chirping of birds 
====
85881-
85882-
85883:Page(s): 1076 
85884-
85885-
85886-
85887-Root / lemma: tei1(-, trek- {fork-, trok-) 
--
86333-
86334-
86335:Page(s): 1077-1078 
86336-
86337-
86338-
86339-Root / lemma: ters- 
--
86388-
86389-References: WP. I 737 f., WH. II 636 f., 694. 
86390:Page(s): 1078-1079 
86391-
86392-Root / lemma: tet(e)r- 
86393-
86394-Meaning: to quack (expr. root) 
--
86458-
86459-References: WP. I 705 f., WH. II 713 f.. Loth RC 43, 160 ff. 
86460:Page(s): 1079-1080 
86461-
86462-Root / lemma: teup- 
86463-
86464-Meaning: to get down, conceal oneself
```


## [2026-09-05T20:27:25.695Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=86630 && NR<=86815' POK_full.txt | grep -n -E \"Root / lemma|Meaning:\" | head\necho \"=== find lemma before 86809 ===\"\nawk 'NR<86809 && /Root \\/ lemma/ {l=NR\": \"$0} END{}' POK_full.txt\ngrep -n \"Root / lemma\" POK_full.txt | awk -F: '$1<86809' | tail -3\necho \"=== tumas / taxma in POK teu ===\"\nsed -n '86470,86500p' POK_full.txt"
}
```


### [2026-09-05T20:27:27.690Z] TOOL RESULT

```
182:Root / lemma: ff-ti- (ti)til- 
184:Meaning: chirping of birds 
=== find lemma before 86809 ===
86507:Root / lemma: teya- tua- 
86519:Root / lemma: teg- tag- 
86536:Root / lemma: teu- teu-, teua-, tuo- tu- 
=== tumas / taxma in POK teu ===
German duchti.. Old English doftds. (wherefore Old Icelandic t^optixw. " Mitruderer', Old 

English ^edc»//a "comrade'. Old High German gidufto' Mitruderer, comrade') and Gothic 



I=>iubjd^ clandestine ', t^iubs^\h\ef, Old Icelandic t^jofr, Old English deof. Old Saxon thiof, 
Old High German oVioZ? 'thief; 

Lithuanian tupiu, tupt/'s\ch hinhocken, in die Knie place', tup/'u, tupetr crouch, in den 
Knien sit', Latvian tupt^ crouch '. 

References: WP. I 714. 
Page(s): 1 085 

Root / lemma: teus- 

Meaning: to empty 

Material: Avestan Kaus. taosayeiti^ makes loose, allows loose' {*touseid), Inchoativ {*tus- 

sRo) Avestan fus9n's\e verlieren die Fassung', baluci fusag, thuay' abandon become'; 

Old Indie tuccha-, tucchya- {*tus-sRo-, *tus-sR-Jo-) " empty, bare, lacking, deserted, 

abandoned, forsaken, worthless', afghan. tas^ empty, bare, lacking'; Latin tesquau. PI. 

"Einoden' {*tueskua)\ Old English dost^ manure'. Old High German dostds. 

("*Ausleerung'); Old Church Slavic tbstb ' kevoc,' , russ. tosc/j" empty, bare, lacking; lean,
```


## [2026-09-05T20:27:32.228Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '86536,86545p' POK_full.txt\necho \"--- avestan forms in teu- section ---\"\nawk 'NR>=86536 && NR<=86810' POK_full.txt | grep -n -i -E \"avestan|tuma|taxma|tav\" | head -20"
}
```


### [2026-09-05T20:27:34.271Z] TOOL RESULT

```
Root / lemma: teu- teu-, teua-, tuo- tu- 

Meaning: to swell; crowd, folk; fat; strong; boil, abscess 

Note: extended with b^, g, k, I, m, n, r, s, t 

Material: Old Indie tav/'f/"\s strong, has Macht', Perf. tutava; in addition /ai/as- 'strong, 

stalwart ', as Subst. Akk. tavasam, Instr. tavasa^ power, strength '; tavyas- tavTyas- 

--- avestan forms in teu- section ---
7:Material: Old Indie tav/'f/"\s strong, has Macht', Perf. tutava; in addition /ai/as- 'strong, 
9:stalwart ', as Subst. Akk. tavasam, Instr. tavasa^ power, strength '; tavyas- tavTyas- 
11:"stronger', tavasvant- 'strong', tavismant- 'strong, mighty', /ai//5^- 'strong', tavisTi. 'force, 
17:Avestan tav- ' to be capable of ', tavah- n. 'power, force', tavTsTi. ' physical strength '; 
18:ap. atavayam'\ am able ', tunuvant- 'mighty', tauvTyah- 'stronger' (: Old Indie tavTyas-), 
116:Old Indie /J-/^/77^-"wirkungsvoir, /i//77/'a- "strong, thick', tumala-, /^/77^/5- "gerauschvoll, 
117:larmend', tuma/a-m'd\n, fuss, noise' ("*Schwall, das larmende Durcheinandera 
118:zusammengedrangten Menge'); Avestan *tuma-\n Tumaspana- Irom Tumaspa- {that \s to 
140:Tocharian B tumane, tmane, A tman^'^ 0.000'. 
175:Avestan tuiri- n. " caseous gewordene milk, whey '; gr. aoopoc; "heap' {*tud-r6-s), in 
202:8. s-formations, connected ^\\h the es-stem Old Indie tavas-, Avestan tavah- etc.:
```


## [2026-09-05T20:27:46.067Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '86648,86656p' POK_full.txt\necho \"=== BRT Tumaspana ===\"; grep -n -i -E \"tumaspa|tumäspa|tum.spana\" BRT.txt | head\necho \"=== BRT kirisaspa/keresaspa ===\"; grep -n -i -E \"k.r.sāspa|kdrdsaspa|kirisaspa|k.r.saspa\" BRT.txt | head -5\necho \"=== BRT baevare ===\"; grep -n -i -E \"baēvarə.aspa|baevare|baevar\" BRT.txt | head -5"
}
```


### [2026-09-05T20:27:46.204Z] TOOL RESULT

```
5. m- derivatives: 

Old Indie /J-/^/77^-"wirkungsvoir, /i//77/'a- "strong, thick', tumala-, /^/77^/5- "gerauschvoll, 
larmend', tuma/a-m'd\n, fuss, noise' ("*Schwall, das larmende Durcheinandera 
zusammengedrangten Menge'); Avestan *tuma-\n Tumaspana- Irom Tumaspa- {that \s to 
say einem, dessen Rosse fat, obese are) stammend'; gr. korkyr. tOjjoc; "TU[jpO(;'; 

gr. TU|jpO(; "burial mound, hillock' = Middle Irish tommm. "hill, bush', cymr. tomt 
=== BRT Tumaspana ===
12327:•  j.  tumäspana-  palr.  Adj.  'von  Tumospa  '> stammend,  dessen  Nachkomme*:  usavahe -nahe  asaonS  Yt/y.  131.
=== BRT kirisaspa/keresaspa ===
30058:•  j.  hitäspa-  m.  EN,  eines  Gegners  des Kjrisaspa:  yat  kama  nijasäni  az>m  (näml lar?säipS)    brü%rS   "urvaxsaya    (sd.)    yat
=== BRT baevare ===
16470:•  j.  baevan-,  baevar-  n.  'Zehntausend, Myriade';  navaca  navaitlsca  navaca  saia navaca  hasattra  navasJs{sA.Ya  •v_qn{^.) Yt  13.  59,  V.  22.  2 ;  —  fravasays  .  .  yä mao^mitncil  myesäinam  °vam  (NP.)  upa- vazinle  "..die  (als  sva.)  inMyriaden . .  herzu- fahren" Yt.jj.  64;  —  urvarh  ..  satavaiti- nqm  hazanravaitinqm  °varf  'varanqm '' V.5.  19  GI.(?).  a)  mit  Gen.:  saümca kasaiirTmca  'vanla  *parianqm  Yt/5. 71; JO.82,  5.21,  $.3,  H./.S,  sVar.,  12,  Y. öiS'-iS.  V.J.  31,  5'.  81,  i4.'i-i.(>"-\—  ys janai  azsqm  äaivanqm  . .  °r5i '>  'vand  (soll heissen)  "..  10000  mal  loooo"  Yt.j.  10; 4.2,  VytJß.  A)  attributiv  gebraucht: *vafv  yjnqnh  nisirinaoiH  Yt.  /o-  a  7 ;  — kakra  . .  yatataiibyS  . .  pan^asaiblsca  sa- täflca  /lasaarSisca  'variblsca  ahaxitäisca Vr.Äi.
16472:•  j.  baevara-yav-   Adj.    'loooofachen
16475:•  j.barvarö.tBniö.-baevar-  n.  'das  loooo-
16478:•  j.  baevara-yna-  n,,  Plur.  'loooo Schläge':  pancascrinsi  .  .  Aazanraynai 'ynäisca  baluarj-jttäi  *aAqxsicrfnäisca  (sd.) V.  7.  S3-         DS.  °ynai  als  Inf.  sbes.
16480:"  j.  baevar9-}iiäi  Inf.  '10000  zu  schla- gen': b°  *ahqxsiaynäisca  (sd.)  V.7.53. Vgl,  6an/ai-?THa-.  —  Pii. :  pa  bevor  ianiinik. ■  j.  baevara.£a§man-  Adj.  'zehntausend- äugig',  nur  von  Müra :  mt^nm  . .  hazattra.- gaossm  'tnatam  Y.  2.  3;  Yt/O.  7,  6.<,\  — mi^rahe  .  .  'manö  Y. /.  3;  —    mitral  .  .
```


## [2026-09-05T20:27:47.724Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD asp/aspast/astar/aswar ===\"; grep -n -i -E \"^asp|aspast|astar|asw[aā]r|asb[aā]r\" PHD.txt | head -30"
}
```


### [2026-09-05T20:27:47.786Z] TOOL RESULT

```
=== PHD asp/aspast/astar/aswar ===
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
458:mastarg [mstlg | (M. mstgrg)] skull.
501:narm [nlm | M nrm, N ~] meek, humble, soft. nasā [ns’y | M n(y)s?h, № ~] corpse, carrion. nask [nsk' | N ~] a division of the Avesta. nasrušt(īh) [xslwšt', -yh] pollution, corruption. nastaran [nstln' | N ~] dog-rose, sweet briar. nawad [90 | N —] ninety.
521:Ošastar ['wsstl] east.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
621:wastar [wstl = Av. wastra-] clothing, garment.
624:wastarag [wstlg] = wastar.
865:aspen spéd-dar.
1083:briar, sweet ~ nastaran,
1256:clothing jamag, paymog, wastar(ag).
1258:clover aspast.
1583:destroyer, destructive kastar, zadar.
1617:diminisher kastar.
1674:dog-rose nastaran.
1728:east OXastar, xwarāsān.
1797:escape (n.) rastarih, wirég.
1987:fodder wastar, P wāš.
2076:garment jàmag, kabàh, paymog, paymózan, warr, wastar(ag).
2320:horsemanship aswarih.
2684:lucerne aspast.
3443:rider aswār.
3445:riding aswārīh.
3686:skull mastarg.
4302:west dēšastar, xwarófràn, xwarwarān, what Ze, kadam.
4312:wilful wastar.
4823:[140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī NINE maškabarzēn NS ey wi? makkizag 1923 556 1-2mašk way deh! ATES dehgiin! uses madār У. о mih мес madan, 1-3mihr мео
4913:rag атат, sīhom” hazārag* larz- larzīdan ram abgan-! abgandan! ramag ras- rascn- rasenidan rahig rasidan rastarih rastan rastag
5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
```


## [2026-09-05T20:28:03.738Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-05T20:28:03.780Z] TOOL RESULT

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
```


## [2026-09-05T20:28:05.296Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mule ===\"; grep -n -i -E \"mule\\b|astar\\b\" PHD.txt | head -5\necho \"=== HUB aspast/astar ===\"; grep -n -i -E \"aspast|aspist|sipist|astar|Maulesel\" HUB.txt | head -20\necho \"=== HRN aspast ===\"; grep -n -i -E \"aspast|aspist|sipist|Luzerne|Maulesel|astar\" HRN.txt | head -20"
}
```


### [2026-09-05T20:28:05.378Z] TOOL RESULT

```
=== PHD mule ===
314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
521:Ošastar ['wsstl] east.
621:wastar [wstl = Av. wastra-] clothing, garment.
624:wastarag [wstlg] = wastar.
1256:clothing jamag, paymog, wastar(ag).
=== HUB aspast/astar ===
134:astar *Sunde' zu fassen; es geh5rt zu zd. anastareta--
970:LW. pastar 'Decke, Teppich*, das mit einer andern
2598:716. Fiir die Volksetymologie {astarvan^ jiid. pers. astar-
2599:vund = *Maulesel-ahnlich', also aus astar^vand) liesse
2687:aatar 'Maulesel*, skr. agvatara- (neben ap. uvaapa^ ViStaspa, Aspacana,
3666:animal, puncture, lancet'; nastar und nestar a lancet' ;
4276:"^asawdra- aus "^aspabara- ; astar 'Maulesel' = ap. *asatara'
4465:(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
4903:bruch* Min. Gl. 104, zd. usah- *Morgenr6the , usastara- *58t-
5257:•Grundriss die W9rter: arm *Arm*, astar 'Maulesel*, afsar
6039:siturg, suturg 'stark*, astarvan, satarvan, suturvan unfrucht-
6288:asp *) 'Pferd' = zd. aspa-, dazu aspist Xuzerne' H. 79 ; as-
6304:esel* = np. astar gegen skr. agvatara-] ^saka- *Hund' =
6657:aus *duvesat, astar ^Maulesel' aus "^asatar = skr. agvatara-).
6953:ddstan, ptc. dast Gl. and Ind. 182 — 183, nom. act. dastar
7560:ap. asabara-] astar ^Maulesel' = ap. ^asatara-, skr. agva-
9485:p. 281), paz. hdsbdm 'daybreak', hosastar 'eastern' Min. Gl.
=== HRN aspast ===
1127:79. esjnst, uspust, ispist 'Luzerne'.
1128:phlv. aspast 'Luzerne'.
1189:86. ester ^Maulesel'.
1190:phlv. astar; ai. agvatard- 'Maulesel'.
2894:phlv.paras^* Verehrer, parastar,parastakzh, i)arast(i)sn
3027:pas^ Comp, pastara (287).
5242:dösastar, vergl. s(i)dös (geschrieben s(i)t") ') ; ai. dösä-,
6276:Die neuper?ische Volksetymologie 'Maulesel ähnlich*
7634:g. kasük, kastar (Comp.); Käs. V. kessär, kesserUr,
9898:218. Dazu arDi. LW. pastar, Hübschmann, KZ. 26, 605.
10138:28. aspastän 'Pferdestall'; arm. LW. aspastan.
10744:133. mastarg (PPGl.), mastiiry (AV.) 'Gehirn, Hirnschäder.
10745:aw. mastareyan- 'Gehirn'; ai. vergl. indstaka- *Kopf,
10979:aw. sastar-; skr. ^as^tdr- 'Gebieter, Züchtiger; arm.
11263:215. vastr, vastarak ') *Kleid, Gewand', häutig.
11286:') So ist statt vastary zu lesen; vgl. mand. LW. Xpl^DONZ-
15630:aspast 79.
15631:aspastän 28.
20660:pastara 315.
```


## [2026-09-05T20:28:16.544Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN entry 206 ===\"; grep -n \"^206\\.\\|^ *206\\.\" HRN.txt | head\necho \"=== HRN page markers? ===\"; grep -c $'\\f' HRN.txt; head -c 300 HRN.txt"
}
```


## [2026-09-05T20:28:17.480Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5\necho \"---\"\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | sed -n '100,140p'"
}
```


### [2026-09-05T20:28:18.437Z] TOOL RESULT

```
=== HRN entry 206 ===
2185:206. bern 'Egge'.
11127:206. vaydän (auch vaytdn geschrieben^)) 'Haupt* (von
=== HRN page markers? ===
396
Google
This is a digital copy of a book that was prcscrvod for gcncrations on library shclvcs bcforc it was carcfully scannod by Google as pari of a projcct
to make the world's books discoverablc online.
It has survived long enough for the Copyright to expire and the book to enter the public domain.
```


### [2026-09-05T20:28:18.497Z] TOOL RESULT

```
---
```


## [2026-09-05T20:28:22.605Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==227' HRN.txt | head -60"
}
```


## [2026-09-05T20:28:23.090Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -20 BQT_v1_pages.txt; echo \"=== markers ===\"; grep -n -m5 -E \"\\[pdf|page\" BQT_v1_pages.txt | head"
}
```


### [2026-09-05T20:28:24.108Z] TOOL RESULT

```
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


### [2026-09-05T20:28:24.156Z] TOOL RESULT

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
=== markers ===
```


## [2026-09-05T20:28:28.792Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==228' HRN.txt | head -50"
}
```


## [2026-09-05T20:28:28.865Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,40p tools/ref_page.py; ls data/verification/sources/refs/ocr | head"
}
```


### [2026-09-05T20:28:30.637Z] TOOL RESULT

```
— 206 —
er auf gtisäde-dil 'fröhlich* verweist. Somit würde es
zur aw. [/sä-, gä&, äyCL^ 'weilen, ruhen, behagen' ge-
hören, zu der auch np. säd (No. 767) zu stellen ist
(Hübschmann, ZDM6. 38, 431). Da indess gusäde-
du u. a. m. sich sehr wohl aus der Bedeutung *offen
erklären lassen, so bleibt die Etymologie sehr zweifel-
haft. Barth olomae (briefl. Mitteilung) denkt daher
besser an Ableitung von einer aus ai. 1 l/'cay- weiter-
gebildeten i/^Ci/O- -f vi, ursprüngl. etwa vom Türvorhang
gesagt (vergl. ai. vi + 1 Kcay-, Bedeutungen 2 und 4).
Die Form mit A:, z. B. jehänkusäl 'Welteroberer , ist
jedenfalls trotz päz. ktisäden ohne etymologischen Wert.
924. fftisuften 'zerstreuen ; verwelken (Vis und RamTn,
S. 55 Vers 3)'; gusuf (gtfsöf) Zerstreuung.
aw. *vi + l^/saoh'; ai. vi 4- l^ksöbh- *in Bewegung,
in Schwanken, in Aufregung geraten*, Causat. skr. 'ver-
wirren*; phlv. v(i)söftan, Praes. v(i)söpet (Men., AV.),
v(i)söp(i)sn (ZPGL).
Verbessert aus kiisuften etc. der Wörterbücher.
Vergl. np. Osuften (No. 32).
925. ffusn ^Männchen, männlich*.
aw. varsni- männlich (Widder)'; phlv. gtisan, vergl.
N. pr. Gusnasp; ai. vfsni^ 'Widder*.
oss. t. Urs 'Hengst' (84).
LW. mand. xr^nj;, syr. n:51^in 'Hengst* (Nöldeke,
ZDM6. 28, 96 ; doch sind diese nicht aw. uysan- *Stier*,
ai. tiksdn- 'Stier, Ochse*, got. auhsa *Ochse'?).
926. guften sprechen, Praes. göy-etn, guftar 'Rede', gep,
'Witz.
g. gaf 'Gespräch*.
ap. \/^gaub', gauhataiy sprechen, sagen* ; phlv. guftan,
guftar, guv{i)Sn (geschrieben gub""), gtiv{i)smh, guv{i)smk,
kurd. giitin ; wa;^. Jög-am, sar. xtig-am,
927. fful *Kose*, arab. LW. jtdah 'Rosenwasser ^).
Semn. vdle (vergl. np. vel *Blüte des Weinstocks*).
Daraus sind bokanntlich entlehnt it. ghdehhe ^ fr. julep^ sp.
julepe *Küliltrank*.
```


### [2026-09-05T20:28:30.680Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

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
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
```


## [2026-09-05T20:28:40.742Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:119 2>&1 | head -60"
}
```


## [2026-09-05T20:28:42.171Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON فصفصه ===\"; grep -n \"فصفصه\\|فسفسه\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON استر ===\"; grep -n \"اسپست\\|سپست\" MON_part1.txt MON_part2.txt BQT_v1.txt | head -5"
}
```


### [2026-09-05T20:28:42.510Z] TOOL RESULT

```
no scan of BQT covers printed page 119 (see 'scans' in refs_online.json)
```


### [2026-09-05T20:28:42.590Z] TOOL RESULT

```
=== MON فصفصه ===
MON_part1.txt:83926:فصفصه» شدر چمنی» شبدر کل قرمزء حند 
MON_part1.txt:97960:(انسان). (گیا.) اسپست» فصفصه. (تص.) 
=== MON استر ===
BQT_v1.txt:42214:و نلم عیوه‌ای هم هت شبیه بسپستان » و بستی 
MON_part2.txt:11409:قت: (۸۸0« [ع.] ((.) (گیا.) بونجه؛ اسپست 
MON_part2.txt:41498:حقیقت یکی از گونه‌های سپستان است. 
MON_part2.txt:51306:پز.) سپستان. 
MON_part2.txt:90590:(غالباً سنجدء سپستان» سبزی» سمنوء سماق»
```


## [2026-09-05T20:28:50.301Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT_v1 aspast latin ===\"; grep -n -i -E \"aspast|aspO|asp\\b|aswar|asbar|astar\" BQT_v1.txt | head -20\necho \"=== form feeds ===\"; grep -c $'\\f' BQT_v1.txt"
}
```


## [2026-09-05T20:28:51.371Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T20:28:52.018Z] TOOL RESULT

```
=== BQT_v1 aspast latin ===
=== form feeds ===
0
```


### [2026-09-05T20:28:53.935Z] TOOL RESULT

```
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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
```


## [2026-09-05T20:29:06.479Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v1 اسپست leaves ===\"; awk 'BEGIN{RS=\"\\f\"} /اسپست/ {print \"LEAF=\"NR-1; print substr($0,1,400)}' BQT_v1_pages.txt | head -60"
}
```


## [2026-09-05T20:29:06.506Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1819 2>&1 | head -50"
}
```


### [2026-09-05T20:29:08.255Z] TOOL RESULT

```
=== v1 اسپست leaves ===
```


### [2026-09-05T20:29:16.101Z] TOOL RESULT

```
REF: BQT:1819  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 616  OCR-lang: fas

-۹۱۸۱۹- ۱ کناب
کنایه از مردم فصیح و بلیغ باشد ‎٩‏ - استعمال مبکنند چنانکه کوبند: ۶« مستم دگشت»
کشاده هنگامان ۲ (۱) - کنابه | بعنی مپیا شد وآماد هگردید - و سیروکشت را
از فصول اربعه است که بپار و تابستان و پاییز | لیزکوبند ۷ - و بمعنی ح كکردن‌ومحوساختن
و زمتان باشد . هم کفته‌اند ۸ - و خریزه را هم میگوبند ‎٩‏ اب
گناس ۲ < بسکون سین بی لاقطه وبمعنی حنظل نیز آمده است ‎٩‏ - ویمعنی دیدن
و بای ابجد » همان کشتاسب مشپور است: که ونظاره کردن هم بنظر رسیده است.
یادشاهی بود پدر اسفندبار رویین تن و بکسد شتا ۱۰ نم اول و فوقالی بالف
وشصت سال پادشاهی کرد . کشیده . بهشت را گونند که مربی‌جنت‌خوانند.
گشاك ؟ - بنم اول ونالی بالف کنیده گشتاسب ۱۱- بن‌اول بروزن‌لهراسب,
وبکاف زده , بازوی درازخانه راگوبند وآن‌ازس نام برزخی است که میان خلق و خالق باشدبرای
دوش است تا ارلج . رسیدن فیض حق ۱۳- و نام پادشاهیاست‌ممروف
گشب * » بنم اول و سکون ثانی‌وبای و او پدر اسفندپار رویین تن بود . گویند یکسد
ابجد » بمعنی جهنده وخیزکننده باشد . و شست سال پادشاهی کرد ودین زردشت پذیرت
گشت ‎٩!‏ - بروزن طشت . بممنی کردید | و چون زردشت کشته کردید بجای او متصوب‌شد
باشد که ماضی گردیدن است ؛ و در مقام شد وآبین زردشت را بریای داشت .
() چش :کعاد هنگامان .
۱ - جوانی بيامدکناده زبان (دقیقی) یخن گفتن خوب و روشن روان .
فردوسی طرصی « شاهنامةٌ بت اج ۱ص ۹ -
۲ - جمم «کناده هنگام » يك افصل‌ازچهار فصل سال؛ برساختهٌ دساتیر«فرهنگه دساتیر
س ۰.۲۹۶ ۴ - مخفف با مصحف «کسباسپ». .۴ -اظ . مصحف «کعال» . قس:
کمالهٌ ران ( در تداول. ) 8 - مخغفف «کگشنپ > کشب (ه.م.) ومعنی‌مذ کوردرمتن
نیز مجعول است : رك : آذرکشپ آذ رگشسپ, کشسب. ‎٩‏ - رك :گت .
۷ - مسدر مرخم . قس ؛کردی ع 865101 ( تفریح ) « ژاباص 6۳۹۳ ۰
۸ سنا او ز لقش‌چهرة خود پرده برگرفت ‏ مالقش دیگران ز ورق میکنیم کشت.
آوحدی 3« رشیدی » .
‎٩‏ - و بمعنی خربزه نیز آهده » لیکن بعی بمعنی حنظل گفته‌ان د که خربزه ابوجهل
باشد .» « رشیدی ؟ وآن مصحف «کیست» (.م.) است بمعنی حنظل و خریزه تلخ -
*- فرائتی از رسم الخط پپلوی ۷201501 ( بهشت ) . رك : بهشت و ر4 : باروچا
صس ۳۳۶ :
زانکه کشتای خوب کاران راست جمله عقبی حلال خوارانت .
سنائی غزنوی « رشیدی » .
۱۱ در اوستا و پارسی باستان ۷1918908 . ( ۳ پونانی ۷51290889 ) » مرکب از
دو جزء : ۷1512 بمعنی از کار افناده » ترسو و محجوب و جزء دوم 85702 همان اسب است »
جمماً یمنی دارلدة-۱سب از:". افتاده « پارتولمه ۱۶۷ > ور : فاب ۱ص ۲۲۷ ؛ مورخان‌ایرانی
و عرب نام او را« بشتاسب " و « بشتاسف » نیز ضبطکرده‌اند . رك : مزدستااص ۳۲۳ ببعد .
۴ این معنی مجعول ات .
```


## [2026-09-05T20:29:32.872Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 327 328 329 330; do echo \"=== LEAF $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -30; done"
}
```


### [2026-09-05T20:29:34.576Z] TOOL RESULT

```
=== LEAF 327 ===
ما
ارم » جح اول و سکون.تانی و میم »
بنتی فد باشد ‏
ارمل س بر وژن جدول » بمنی بسیار
وکثیرباشد. وصدا وآوازرا یز گومند - وبمعنی
همه و مجبوغ هم آمده است
از ناو با نون و واو بی وزن غرفاو .
نم ناحیه‌ایست از نواحی حمدان .
از ناوه ت شتح اول وواو» سعنی ازناو
است که ناحیهای باشد از نواحی همدان ‏
از فس « بر وزن مذحب . بمعتی رنجش
باشد که از رنجیدن است - و در عربی فربه را
کونند که ضد لاعی باشد .
ار نقش گلور خار دستن .
کتابه از خواری و بی اعتباری باشد .
از ود - باواو بروزنشبگرد » دوابی
است که آنرا بفارسی انده فوقو گویند و بعربی
آژوها:
روغن بجوشانند و برطفل یکه دب سمرکت آمد
بمالند زود بحرکت آبده و جمیم یادها را نافع
است .
ارودری بر وژن سرصری » بلفت
بربری نام درختی است سطبر و خار دار ؛ پوست
آن سرخ و گنده میباشد» در دوایی بکار برند .
ار هر اه ه بفتح های هوز و رای می
نفطه بالف کشیده ۳ اسلی تساه
ماران است ا .
ار ای وزدضر ۱ مخفف زبرا
هد که از رای سلیل است » نی از برای اين
و از این جپت .
=== LEAF 328 ===
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی‌را نیز گویندکه ازجلهة
چهل و حشت صورت فلك باشد ٩‏ .
ارم خح اول و سکون انی و غن
نقطه دار , شاخهابی را گویند که از درخت بریده
باشند و بعربی جلمه خوانند٩‏ .
ار کان با کاف‌بروزن دربان ؛ بمعتی
مردم کاهل و باطل و مهمل و بیکار باشد .
باگد شبکه دار که ازیس آن نگاه توان کرد .
۱
ظ
از گهی -باها پروزنک رکدن : بمعنی
از کهان است که کاهل و باطل و مهمل وبیکار
بش
۸ ۰
آز لد - بفتح اول و انی و سکون نون
و دال ایجد . کلی باشد که بر روی خشت بهن
کنند و خشتی دیگر بربالای آن نهند - و گل
و لای ته حوض را نیز گفته اند .
اژ نگ -بر یزن پلنگ , چين پیشانی
وروی و اندام باشد.
اه « بنتح اول و انی , آهك را گویند
و بعربی کلس و نوره خوانند .
‌ و ۲ ۳
=== LEAF 329 ===
۱ <<
رومی است . 1 2 بکویتد و باشیر تازه
بیامیز ند وبرزیر خصه‌بمالند نموظ عجبآورد۱
اساسه بفتح نی رو اس :
بمعتی نگرستن بگوشة چشم ووایس دیدن‌باشد ۴
وبکی اول نیز گفته اند .
اسا لیطوس یکی لام و سکون
تحنالی وضم طای حطلید واو وسین می‌نقطهسا کن»
بیونانی گلی‌است کهآ نرا بعربی طی ىکرمی‌خواننده
و آن کلی باشد سیاه رنگه و آترا طین کرمی
از آنجیت گوبند که در اول میک بر آوردن
درخت انگور ازان گل بردرخت مالند تا کرمی
که ب رکه آبرا میخورد ب رکه آنرا نخورد
وچشمهای تا را نباه نکند . ۱
اسالیون - بکس لام و ضم تحتانی
وسکون واو ونون » کم کرفس کوهی باشد ۴ .
اسب ب بکس اول و سکون ثانی و بای
فارسی ؛ عویزهار
ومویدبرباشد؟ -
ویفتح اول معروف
است و بعربی‌فری
خواند ۵ - و نام
یکی از مپره‌های
شطرنج هم هست . *
)۱( چك : هردهم -
آسپ» افکن مردم دلاور و بهادر
و دلیر و شجاع را کوبند که تنها و ییکه برفوج
عنیم اسب اندازد » منی بتازد .
اسیاثیر ۱ ه با بای بالف کشیده
ویشون زده وضم بای دیگر وسکون رای قرشت»
=== LEAF 330 ===
اسپخحول بکسر اول و سکون‌انی
و بای فارسی مکور و خای نقطه دار حضموم‌بواو
ولام زده » بععتی‌پیخال است که فضله وافکند گی
اسیر ۱ س با بای فارسی بر وزن مهتر»
سپررا گونند و بعریی جثه خوانند .
اسپر اثین )0 بابای فارسی» بروزن
وممنی اسفرائین باشد. وآن شهرست مشهور در
خراسان » و چون رسم و عادت مردم آنجا چنان
بوده که یوسته با سیر می‌بوده اند لهذا بدین‌نلم
موسوم شده است . #
اسب رد س یا بای فارسی و زای هوز
اسب رس « بفتح‌اول بروزن دستری:
(۱) چش : اسیرآئن .
۱ و
اراشی آهکی عمیق خوب میرو‌بد .
- ۱۸۱ « کل کلاب ۷۱ >.
روستامی ۱۸۱ > .
۷ تب ره 2 اسپناخ.
و
ت که عرصه و میدان باشد»
و ۳
بیعنی اسب رز است
و گس اول هم آمده لت
اسیر سب « بسکون مين و بای اپجد »
بیعنی اسپ ری انت که عرصه و میدان باشد»
و یکس اول هر کنتانه ۴
آسپر سیف « بافاء بروزن‌ومعنیاسپرسب
است که فنا و عرصه و میدان باشد ۴ .
اسیرغم - بکر اول و فتح ثبالث
وغین نقطمدار و سکون‌ثانی ورابم و عیم » بمعنی
```


## [2026-09-05T20:29:50.888Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 151 -l 151 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg151 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T20:29:53.131Z] TOOL RESULT

```
total 15064
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:29 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     395 Sep  5 16:10 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:29:54.505Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁é%C4%B8wos\" ; do echo; done\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁éḱwos\" --note \"page 151, root Ekwos, PIE horse root\" \npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/اسب\" --note \"page 151, Persian asb 'horse'\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/سوار\" --note \"page 151, Persian savar 'rider'\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/استر\" --note \"page 151, Persian astar 'mule'\"\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/alfalfa\" --note \"page 151, alfalfa English etymology\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/alfalfa\" --note \"page 151, English alfalfa\"\n"
}
```


### [2026-09-05T20:29:58.191Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a5bfc0369169ffe6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e94efffb5dbedf5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/53f1222b786f8f19.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30f512cff912830f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/01b2b5ab2d62475e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3957c14073214b5e.txt
```


## [2026-09-05T20:30:02.480Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== PIE h1ekwos ===\"; grep -n -i -A3 \"Proto-Indo-European\" a5bfc0369169ffe6.txt | head -40\necho \"=== size ===\"; wc -c a5bfc0369169ffe6.txt 6e94efffb5dbedf5.txt 53f1222b786f8f19.txt 30f512cff912830f.txt 01b2b5ab2d62475e.txt 3957c14073214b5e.txt"
}
```


### [2026-09-05T20:30:02.570Z] TOOL RESULT

```
=== PIE h1ekwos ===
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁éḱwos
2-FETCHED: 2026-09-05T20:29:56Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/h₁éḱwos - Wiktionary, the free dictionary
5-
6:Reconstruction:Proto-Indo-European/h₁éḱwos - Wiktionary, the free dictionary 
7-
8- Jump to content 
9-
--
57: Proto-Indo-European 
58-
59: Toggle Proto-Indo-European subsection 
60-
61- 1.1 
62- Etymology 
--
87: Reconstruction:Proto-Indo-European/ h₁éḱwos 
88-
89- 2 languages 
90-
--
144: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
145-
146: Proto-Indo-European
147- [ edit ] 
148-
149- Etymology
--
171: According to the linguist Mate Kapović, a reconstruction *éḱwos is equally capable of yielding the known reflexes in the Indo-European daughter languages. However, the term is often reconstructed as *h₁éḱwos because it is generally thought that most Proto-Indo-European words began with a consonant. [ 7 ] 
172-
173- Inflection
174- [ edit ] 
--
297: ^ Ranko Matasović (2012), Areal Typology of Proto-Indo-European: The Case for Caucasian Connections. Transactions of the Philological Society, Volume 110, Issue 2, pages 283–310 
298-
299- ^ Václav Blažek (2019) "Toward the question of Yeniseian homeland in perspective of toponymy" 
300-
--
307: ^ Kapović, Mate ( 2017 ), “Part 1 Chapter 1: Proto-Indo-European phonology”, in Kapović, Mate , editor, The Indo-European Languages (Routledge Language Family Series), 2nd edition, London, New York: Routledge, →ISBN , page 44 
=== size ===
 9429 a5bfc0369169ffe6.txt
 7593 6e94efffb5dbedf5.txt
15739 53f1222b786f8f19.txt
 4150 30f512cff912830f.txt
 6973 01b2b5ab2d62475e.txt
24294 3957c14073214b5e.txt
68178 total
```


## [2026-09-05T20:30:06.118Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== h1ekwos etym+desc ===\"; sed -n '149,200p' a5bfc0369169ffe6.txt\necho; echo \"=== ASB (wikt fa) ===\"; grep -n -i -B2 -A8 \"Etymology\" 6e94efffb5dbedf5.txt | head -40"
}
```


### [2026-09-05T20:30:06.178Z] TOOL RESULT

```
=== h1ekwos etym+desc ===
 Etymology
 [ edit ] 

 Usually explained as a derivation of the adjective *h₁éḱus ( “ quick, swift ” ) , also seen in e.g. Ancient Greek ὠκύς ( ōkús ) , Latin ōcior ( “ faster ” ) and Sanskrit आशु ( āśú , “ fast, quick ” ) (all < PIE *h₁oh₁ḱus ( “ swift ” ) ). The thematic derivation would express association with a root noun *h₁eḱ- ( “ swiftness, celerity ” ) , thus denoting “that which has swiftness” or “the swift one”. The adjective would have to be derived from the root by reduplication, which is unusual in PIE nominal word formation. Many linguists therefore reject it as popular etymology and suggest other sources:

 Kulanda argues that the PIE word is borrowed from North Caucasian; [ 1 ] compare East Circassian шы ( šə ) , Abkhaz аҽы ( aĉə ) , Avar чу ( ču ) , Karata ичва ( ičva , “ mare ” ) , Lezgi шив ( šiv , “ horse ” ) etc. (NCED 520). This etymology has been criticized by Matasović who argues that the direction of borrowing is probably from PIE into North Caucasian: steppe horses were probably traded for Mesopotamian imports on the North Caucasus in the Eneolithic period. The fact that we find fricatives and affricates in the Caucasian reflexes of this word indicates that the source could have been an IE dialect of the satem type. [ 2 ] 

 Blažek proposes that PIE is borrowed from Proto-Yeniseian *ʔɨʔχ - *kuʔs "male horse". [ 3 ] 

 The original thematic form is also disputed. According to Kloekhorst, the original derivation was a u-stem, to which Anatolian reflexes point particularly, which presume a Proto-Anatolian u-stem *h₁éḱu- , as opposed to the thematic (o-stem) derivation in all the other PIE branches. There is no known phonological development through which PIE *h₁eḱwo- could yield PAnat. *h₁eḱu- , and in view of the productivity of the o-stem inflection in Anatolian it is unlikely that PIE *h₁eḱwo- would have yielded PAnat. *h₁éḱu- through secondary developments. We therefore must conclude that the Proto-Anatolian u-stem *h₁éḱu- reflects the original state of affairs and that the thematicization as visible in the non-Anatolian IE languages (which would be a trivial development) must be regarded as a common innovation of them. [ 4 ] In other words, this is a piece of evidence supportive of the Indo-Hittite hypothesis. In that case, the original paradigm would have been *h₁éḱ-u-s , *h₁éḱ-u-m , *h₁ḱ-u-és , from the stem *h₁eḱ-u- ( “ swift ” ) .

 Noun
 [ edit ] 

 *h₁éḱwos   m ( non-ablauting ) [ 5 ] [ 6 ] 

 stallion , horse 
 Synonyms: *ǵʰéyos , *márkos , *mend- 

 Reconstruction notes
 [ edit ] 

 According to the linguist Mate Kapović, a reconstruction *éḱwos is equally capable of yielding the known reflexes in the Indo-European daughter languages. However, the term is often reconstructed as *h₁éḱwos because it is generally thought that most Proto-Indo-European words began with a consonant. [ 7 ] 

 Inflection
 [ edit ] 

 Thematic

 singular

 nominative

 *h₁éḱwos 

 genitive

 *h₁éḱwosyo 

 singular

 dual

 plural

 nominative

 *h₁éḱwos 

 *h₁éḱwoh₁ 

 *h₁éḱwoes 

=== ASB (wikt fa) ===
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 2 
68- Persian 
69-
70- Toggle Persian subsection 
--
74-
75- 2.2 
76: Etymology 
77-
78- 2.3 
79- Pronunciation 
80-
81- 2.4 
82- Noun 
83-
84- 2.4.1 
--
194- [ edit ] 
195-
196: Etymology
197- [ edit ] 
198-
199- From Proto-Iranian *Hácwah (compare Northern Kurdish hesp , esp , Avestan 𐬀𐬯𐬞𐬀 ( aspa ) , Persian اسب ), from Proto-Indo-Iranian *Háćwas (compare Sanskrit अश्व ( áśva ) ), ultimately from Proto-Indo-European *h₁éḱwos .
200-
201- Noun
202- [ edit ] 
203-
204- اسب ( asb ) 
--
218- عَسْب ( ʿasb ) ( dialectal , Shushtar , Khansar ) [ 1 ] 
219-
220: Etymology
221- [ edit ]
```


## [2026-09-05T20:30:10.114Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== اسب Persian section ===\"; sed -n '218,260p' 6e94efffb5dbedf5.txt\necho; echo \"=== سوار ===\"; grep -n -A6 \"Etymology\" 53f1222b786f8f19.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:30:10.231Z] TOOL RESULT

```
=== اسب Persian section ===
 عَسْب ( ʿasb ) ( dialectal , Shushtar , Khansar ) [ 1 ] 

 Etymology
 [ edit ] 

 PIE word 
 *h₁éḱwos 

 From earlier اسپ ( asp ) , from Middle Persian [script needed] ( ʾsp̄ /⁠asp⁠/ ) , from Old Persian 𐎠𐎿𐎱 ( aspa ) , from Old Median *aspah (compare Old Persian 𐎠𐎿 ( asa ) ), from Proto-Iranian *Hácwah (compare Avestan 𐬀𐬯𐬞𐬀 ( aspa ) , Northern Kurdish hesp , esp , Pashto آس ( ās ) , Ossetian ефс ( efs ) ), from Proto-Indo-Iranian *Háćwas (compare Sanskrit अश्व ( áśva ) ), ultimately from Proto-Indo-European *h₁éḱwos (compare Ancient Greek ἵππος ( híppos ) , Armenian էշ ( ēš , “ donkey ” ) , Lithuanian ašva ( “ mare ” ) , Latin equus ).

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈʔasb/ 

 ( Dari, formal ) IPA ( key ) : [ʔäsb] 

 ( Dari, formal ) IPA ( key ) : [ʔäsb] 
 ( Kabuli ) IPA ( key ) : [ʔäsb] 

 ( Hazaragi ) IPA ( key ) : [ʔɔːs] 

 ( Iran, formal ) IPA ( key ) : [ʔæsb̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔäsb] 

 Rhymes: -asb 

 Readings

 Classical reading ? 

 asb

 Dari reading ? 

 asb

 Iranian reading ? 

 asb

 Tajik reading ? 

=== سوار ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
96: Etymology 
97-
98- 3.2 
99- Pronunciation 
100-
101- 3.3 
102- Noun 
--
113: Etymology 
114-
115- 4.3 
116- Pronunciation 
117-
118- 4.4 
119- Noun 
--
142: Etymology 
143-
144- 5.3 
145- Pronunciation 
146-
147- 5.4 
148- Noun 
--
159: Etymology 
160-
161- 6.2 
162- Pronunciation 
163-
164- 6.3 
165- Noun 
--
176: Etymology 
177-
178- 7.2 
179- Noun 
180-
181- Toggle the table of contents 
182-
--
256: Etymology
257- [ edit ] 
258-
259- Though Fraenkel assumed that the Arabic word is genuine and not a loan, likely a perhaps early loan from a byform of Aramaic שֵׁירָא / ܫܶܐܪܳܐ ( šērā ) , see the exposure at ش ج ر ( š j r ) . Juxtapose قُلْب ( qulb , “ bracelet ” ) for a Syriac loan. Compare also دُمْلُوج ( dumlūj ) .
260-
261- Pronunciation
262- [ edit ] 
--
472: Etymology
473- [ edit ] 
474-
475- From Middle Persian ʾswbʾl ( aswār , “ horseman, rider ” ) .
```


## [2026-09-05T20:30:15.803Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '470,485p' 53f1222b786f8f19.txt\necho \"=== استر ===\"; grep -n -A8 \"Etymology\" 30f512cff912830f.txt | tail -30\necho \"=== etymonline alfalfa ===\"; grep -n -i -A6 \"alfalfa\" 01b2b5ab2d62475e.txt | head -40"
}
```


### [2026-09-05T20:30:15.874Z] TOOL RESULT

```
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian ʾswbʾl ( aswār , “ horseman, rider ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /swɑːɾ/ 

 Noun
 [ edit ] 

 سوار ( swar ) 
=== استر ===
--
172: Etymology 1
173- [ edit ] 
174-
175- Inherited from Middle Persian [script needed] ( ʾstl /⁠astar⁠⁠/ ) , from Old Persian *asatarah , from Proto-Iranian *Hacwataráh , from Proto-Indo-Iranian *Haćwatarás .
176-
177- Noun
178- [ edit ] 
179-
180- استر • ( astar ) ( Tajik spelling астар ) 
--
195: Etymology 2
196- [ edit ] 
197-
198- Noun
199- [ edit ] 
200-
201- استر • ( astar ) 
202-
203- alternative form of آستر ( āstir  / âster , “ lining ” ) 
--
205: Etymology 3
206- [ edit ] 
207-
208- Persian Wikipedia has an article on: استر 
209-
210- Wikipedia fa 
211-
212- Proper noun
213- [ edit ] 
=== etymonline alfalfa ===
1:URL: https://www.etymonline.com/word/alfalfa
2-FETCHED: 2026-09-04T19:35:56Z
3-STATUS: 200
4:TITLE: Alfalfa - Etymology, Origin & Meaning
5-
6:Alfalfa - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of alfalfa 
22-
23: alfalfa (n.) 
24-
25: common name in North America for "lucerne," a plant in the legume family important as a forage crop, 1845, from Spanish alfalfa , earlier alfalfez , said by Iberian sources to be from Arabic al-fisfisa "fresh fodder." Watkins says it is ultimately from an Old Iranian compound *aspa-sti- "alfalfa, clover," from *aspa- "horse" (from PIE root *ekwo- "horse") + -sti- "food," from suffixed form of PIE root *ed- "to eat."
26- also from 1845 
27-
28: Entries linking to alfalfa 
29-
30- *ed- 
31-
32- Proto-Indo-European root meaning "to eat," originally "to bite." 
33-
34: It might form all or part of: alfalfa ; anodyne ; comedo ; comestible ; eat ; edacious ; edible ; escarole ; esculent ; esurient ; etch ; ettin ; fret (v.); frass ; jotun ; obese ; obesity ; ort ; postprandial ; prandial .
35-
36- It might also be the source of: Sanskrit admi "I eat;" Avestan ad- "to eat;" Greek edo "I eat;" Latin edere "to eat;" Lithuanian ėdu "I eat," ėdžioti "to devour, bite;" Hittite edmi "I eat," adanna "food;" Armenian utem "I eat;" Old Church Slavonic jasti "to eat," Russian jest "to eat;" Old Irish ithim "I eat;" Gothic itan , Old Swedish and Old English etan , Old High German essan "to eat."
37-
38- *ekwo- 
39-
40- Proto-Indo-European root meaning "horse." Perhaps related to *ōku- "swift."
--
42: It might form all or part of: alfalfa ; Eohippus ; equestrian ; equine ; equus ; hippo- ; hippocampus ; Hippocratic ; Hippocrene ; hippocrepian ; hippodrome ; hippogriff ; Hippolytus ; hippopotamus ; Philip ; philippic ; Philippines ; Xanthippe .
43-
44- It might also be the source of: Sanskrit açva- , Avestan aspa- , Greek hippos , Latin equus , Old Irish ech , Old Church Slavonic ehu- , Old English eoh , Gothic aihwa- all meaning "horse."
45-
46- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
47-
```


## [2026-09-05T20:30:27.256Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/فصفصة\" --note \"page 151, Arabic fisfisa 'alfalfa', Persian/Syriac origin\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/ἵππος\" --note \"page 151, Greek hippos\"\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/Philip\" --note \"page 151, Philip < Philippos 'horse lover'\"\npython3 tools/fetch_source.py \"https://www.etymonline.com/word/hippopotamus\" --note \"page 151, hippopotamus\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/گشتاسب\" --note \"page 151, Goshtasp < Av. Vistaspa\"\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/garsasp\" --note \"page 151, Garsasp/Keresaspa\"\n"
}
```


### [2026-09-05T20:30:35.466Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/542d1573ebc70335.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c759022bb21dd9c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6c4469d3276fcdf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14311f4929a44d5a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e2beed8e6bb872a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bafbde67fc027a59.txt
```


## [2026-09-05T20:30:38.794Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== فصفصة ===\"; grep -n -A6 \"Etymology\" 542d1573ebc70335.txt | head -30\necho \"=== hippos ===\"; grep -n -A6 \"Etymology\" 1c759022bb21dd9c.txt | tail -25\necho \"=== Philip ===\"; sed -n '20,40p' f6c4469d3276fcdf.txt\necho \"=== hippopotamus ===\"; sed -n '20,35p' 14311f4929a44d5a.txt"
}
```


### [2026-09-05T20:30:38.907Z] TOOL RESULT

```
=== فصفصة ===
=== hippos ===
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
183: Etymology
184- [ edit ] 
185-
186- PIE word 
187- *h₁éḱwos 
188-
189- From Proto-Hellenic *íkkʷos (compare Mycenaean Greek 𐀂𐀦 ( i-qo ) ), from Proto-Indo-European *h₁éḱwos , from *h₁oh₁ḱu- ( “ swift ” ) . [ 1 ] The expected inherited form is **έπος ( **épos ) , and there is no explanation for why ῐ̔́ππος ( hĭ́ppos ) has ῐ in place of ε , word-initial rough breathing, and double ππ ( pp ) , each of which is of unclear origin; possibly borrowed from another Indo-European language where such sound changes are regular. Cognates include Sanskrit अश्व॑ ( áśva ) , Latin equus , Lithuanian ašva , Gaulish epos , Old Armenian էշ ( ēš , “ donkey ” ) , Icelandic jór , and Old Irish ech .
=== Philip ===

 Origin and history of Philip 

 Philip 

 masc. proper name, most famously in classical history king of Macedon, father of Alexander the Great (compare philippic ); the from Latin Philippus , from Greek Philippos "fond of horses," from philos "beloved, loving" (see philo- ) + hippos "horse" (from PIE root *ekwo- "horse").

 In old poetry, imitative of the chirp of a sparrow, hence a common name for one (Skelton, Cartwright, etc.). In 16c., Philip and Cheyney was a way to say "any two common men."

 You remember the story of the poor woman who importuned King Philip of Macedon to grant her justice, which Philip refused : the woman exclaimed, "I appeal" : the king, astonished, asked to whom she appealed : the woman replied, "From Philip drunk to Philip sober." [Emerson, "New England Reformers," 1844] 

 Entries linking to Philip 

 philippic (n.) 

 "a bitter invective discourse, a denunciation," 1590s, from French philippique , from Latin (orationes) Philippicæ , a translation of Greek Philippikoi (logoi) , referrimg to the series of orations made in Athens by Demosthenes in 351-341 B.C.E. urging Greeks to awaken to their danger and unite to fight the rising power of Philip II of Macedon, father of Alexander the Great. The Latin phrase was used of the speeches made by Cicero against Marc Antony in 44 and 43 B.C.E.

 Philippa 

 fem. proper name, modern, fem. of Philip .

=== hippopotamus ===

 Origin and history of hippopotamus 

 hippopotamus (n.) 

 omnivorous ungulate pachydermatous mammal of Africa, 1560s, from Late Latin hippopotamus , from Greek hippopotamos "riverhorse," an irregular formation from earlier ho hippos potamios "the horse of the river"), from hippos "horse" (from PIE root *ekwo- "horse") + adjective from potamos "river, rushing water" (see potamo- ). Replaced Middle English ypotame (c. 1300), which is from the same source but deformed in Old French. Glossed in Old English as sæhengest . Translated as river-horse in Holland's Pliny (1601).

 Ypotamos comen flyngynge. ... Grete bestes and griselich ["Kyng Alisaunder," c. 1300]

 Related: Hippopotamic .
 also from 1560s 

 Entries linking to hippopotamus 

 hippo (n.)
```


## [2026-09-05T20:30:46.233Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -20 542d1573ebc70335.txt; echo \"...\"; wc -c 542d1573ebc70335.txt\necho \"=== گشتاسب ===\"; grep -n -A6 -i \"etymology\\|Vištāspa\\|From \" 0e2beed8e6bb872a.txt | head -30; wc -c 0e2beed8e6bb872a.txt\necho \"=== iranica garsasp ===\"; head -40 bafbde67fc027a59.txt"
}
```


### [2026-09-05T20:30:46.305Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/فصفصة
FETCHED: 2026-09-05T20:30:29Z
STATUS: 200
TITLE: فصفصة - Wiktionary, the free dictionary

فصفصة - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
...
8205 542d1573ebc70335.txt
=== گشتاسب ===
138 0e2beed8e6bb872a.txt
=== iranica garsasp ===
URL: https://www.iranicaonline.org/articles/garsasp
FETCHED: 2026-09-05T20:30:35Z
STATUS: 200
TITLE: GARŠĀSP-NĀMA - Encyclopaedia Iranica

GARŠĀSP-NĀMA - Encyclopaedia Iranica Skip to main content 
 Search Iranica...

 search in 8,977 entries of Encyclopædia Iranica. 

 Close Search 

 search 
 account 
 Menu 

 Explore 
 News & Events 
 Editorial Current Board 
 Former Boards 

 Authors 
 Style Guide 
 About About Iranica 
 Ehsan Yarshater 
 Advisory Board 
 Board of Directors 
 FAQ 
 Contact 

 Donate 
 search 

 account 

 GARŠĀSP-NĀMA

 Browse Iranica 

 GARŠĀSP-NĀMA
```


## [2026-09-05T20:30:52.707Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -i -E \"persian|aramaic|syriac|alfalfa|lucerne|Noun|فصفصة\" 542d1573ebc70335.txt | sed -n '1,40p'"
}
```


### [2026-09-05T20:30:52.754Z] TOOL RESULT

```
1:URL: https://en.wiktionary.org/wiki/فصفصة
4:TITLE: فصفصة - Wiktionary, the free dictionary
6:فصفصة - Wiktionary, the free dictionary 
62: Noun 
69: فصفصة 
130: Noun
142: Declension of noun فَصْفَصَة ( faṣfaṣa )‎; فِصْفِصَة ( fiṣfiṣa )
412: Retrieved from " https://en.wiktionary.org/w/index.php?title=فصفصة&oldid=87597927 "
415: Arabic nouns 
416: Arabic singulative nouns 
417: Arabic feminine nouns 
418: Arabic nouns with triptote singulative in -a 
419: Arabic nouns with basic triptote collective 
420: Arabic nouns with sound feminine paucal 
421: Arabic nouns with broken plural 
422: Arabic nouns with basic diptote broken plural 
455: فصفصة
```


## [2026-09-05T20:30:56.537Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/گشتاسپ\" --note \"page 151, Goshtasp\"\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/kersasp\" --note \"page 151, Keresaspa/Garshasp\"\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/jamasp-avestan-jamaspa\" --note \"page 151, Jamasp\"\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/lohrasp\" --note \"page 151, Lohrasp < Aurvat.aspa\"\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/arjasp\" --note \"page 151, Arjasp < Arejat.aspa\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/aspast\" --note \"page 151, MP aspast\""
}
```


### [2026-09-05T20:31:14.102Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/e3db0cc428b3e00c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb42475c6f2853fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6597b3b37464699b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/47122c9c2c0e9a16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9e8c329beb9254b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcdff84c7a4d76fb.txt
```


## [2026-09-05T20:31:18.044Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '125,145p' 542d1573ebc70335.txt\necho \"=== گشتاسپ ===\"; wc -c e3db0cc428b3e00c.txt; grep -n -A4 -i \"etymolog\" e3db0cc428b3e00c.txt | tail -20\nfor f in eb42475c6f2853fd 6597b3b37464699b 47122c9c2c0e9a16 9e8c329beb9254b1 bcdff84c7a4d76fb; do echo \"=== $f ===\"; sed -n '1,6p' $f.txt; wc -c $f.txt; done"
}
```


### [2026-09-05T20:31:19.917Z] TOOL RESULT

```
 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Noun
 [ edit ] 

 فَصْفَصَة or فِصْفِصَة • ( faṣfaṣa or fiṣfiṣa )  f ( singulative , collective فَصْفَص   m ( faṣfaṣ ) or فِصْفِصَ   m ( fiṣfiṣa ) , plural فَصَافِص ( faṣāfiṣ ) ) 

 singulative of فِصْفِص ( fiṣfiṣ ) 

 alternative form of فِصْفِص ( fiṣfiṣ ) 

 Declension
 [ edit ] 

 Declension of noun فَصْفَصَة ( faṣfaṣa )‎; فِصْفِصَة ( fiṣfiṣa )

 singulative

=== گشتاسپ ===
4072 e3db0cc428b3e00c.txt
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
--
162: Etymology
163- [ edit ] 
164-
165- Inherited from Middle Persian 𐭢𐭥𐭱𐭲𐭮𐭯 ( gwštsp /⁠guštāsp⁠/ ) , from Old Persian 𐎻𐏁𐎫𐎠𐎿𐎱 ( vi-š-t-a-s-p /⁠vištāspaʰ⁠/ ) , borrowed from Avestan 𐬬𐬌𐬱𐬙𐬁𐬯𐬞𐬀 ( vištāspa ) .
166-
=== eb42475c6f2853fd ===
URL: https://www.iranicaonline.org/articles/kersasp
FETCHED: 2026-09-05T20:31:03Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found141 eb42475c6f2853fd.txt
=== 6597b3b37464699b ===
URL: https://www.iranicaonline.org/articles/jamasp-avestan-jamaspa
FETCHED: 2026-09-05T20:31:06Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found156 6597b3b37464699b.txt
=== 47122c9c2c0e9a16 ===
URL: https://www.iranicaonline.org/articles/lohrasp
FETCHED: 2026-09-05T20:31:09Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found141 47122c9c2c0e9a16.txt
=== 9e8c329beb9254b1 ===
URL: https://www.iranicaonline.org/articles/arjasp
FETCHED: 2026-09-05T20:31:13Z
STATUS: 200
TITLE: ARJĀSP - Encyclopaedia Iranica

ARJĀSP - Encyclopaedia Iranica Skip to main content 
4239 9e8c329beb9254b1.txt
=== bcdff84c7a4d76fb ===
URL: https://en.wiktionary.org/wiki/aspast
FETCHED: 2026-09-05T20:31:14Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found132 bcdff84c7a4d76fb.txt
```


## [2026-09-05T20:31:27.393Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '20,50p' 9e8c329beb9254b1.txt"
}
```


### [2026-09-05T20:31:27.440Z] TOOL RESULT

```
 Former Boards 

 Authors 
 Style Guide 
 About About Iranica 
 Ehsan Yarshater 
 Advisory Board 
 Board of Directors 
 FAQ 
 Contact 

 Donate 
 search 

 account 

 ARJĀSP

 Browse Iranica 

 ARJĀSP

 Article by 

 Aḥmad Tafażżolī 

 Last Updated February 15, 2013

 Print Detail Vol. II, Fasc. 4, p. 412

 Published December 15, 1986
```


## [2026-09-05T20:31:31.192Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT amaspa (Jamaspa) ===\"; grep -n -i -E \"j.m.spa|jämäspa|jamaspa\" BRT.txt | head -5\necho \"=== BRT aurvat ===\"; grep -n -i -E \"aurva.\\.aspa|aurvat|auruua\" BRT.txt | head -5\necho \"=== BRT arajat ===\"; grep -n -i -E \"ar.ja.\\.aspa|arejat|ar.jal\" BRT.txt | head -5\necho \"=== BRT arsan ===\"; grep -n -i -E \"arsan-|aršan|arsan\\b\" BRT.txt | head -5\necho \"=== BRT kdrdsaspa ===\"; grep -n -i -E \"kar.saspa|k.r.saspa|kirisaspa|kdrdsäspa\" BRT.txt | head -5"
}
```


### [2026-09-05T20:31:31.345Z] TOOL RESULT

```
=== BRT amaspa (Jamaspa) ===
2071:AwdS.:    AwdViä  II  sahitJhä  i  Saiaslän.      Autgabc    yon  JamaspjiMJamaspASANA.      Bombay    1897. At:  A/nn  i  Zaraäf;  s.  S.  IX.  7.
2118:IF.:  Indogermanische  Forschungen.    Herausgeg.  von  KBRUGUAnn  und  WStreitberg.   Strassburg. IFAni.:  Anzeiger  usw.,  Beiblatt  zu  den  IF. JA:  Journal  Asiatiquc.     Paris. Jamaspji  (MJamaspAsana)  Dict.O:  Pahlavi  GujarSti  and  English  Diclionary.     Bombay   1877 ff.
3594:•  j.  apara-zäta-  Adj.  'als  späterer,  zweiter geboren',  hinter  EN.  'der  jüngere'  (zur Unterscheidung  von  einem  älteren  gleichen Namens):  jämäspahe  °taht  ..  mathydi.- mätihahe  "tahe  . .  urvatatnarahe  "iahe  Yt y.i27.
11617:•  j.  Jätnäspa-,   g.  däjlmäspa- ''  m,  EN.
11623:•  j.  Jämäspana-  patr.  Adj.  'von  Jamaspa stammend,  dessen  Nachkomme':  Aar?hau- riisJ  'nahe  asaoriS  Yt.J_y,i04;  —  varhiahe . .  'nahe  FrD.  7.
=== BRT aurvat ===
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4776:kaurvatüt-,  xlaisröi  hU  haurvüta  'ntäla
=== BRT arajat ===
20072:•  j.  mairya-  Adj.  (fem.  ya-)  'betrügerisch, tückisch,  schurkisch;  Schurke':  *ahalcti ♦»/•«'>  (NSf.)  nas'atagca  'ys  "und  es  wird  zu Grunde  gehen  die  Schurkin  und  verder- ben wird  der  Schurke"  Yt/p.ia;  4.Z; —  armatsis  deihrubya  avästryaia  (sd.) -ys  Yt/.  29;  —  tmnniaite  vJspqm  daiti- haom  'yS  mihrSjruxl  YLJ0.3;  —  °yS drvi  bizangrs  V.  5,  35;  —  sii^rqm yqm  karafnqmüa  'yanqmla  bieangn aimcur/anqmca  Y,  <>.  18;  —  *JanyS. 'yayh  Y.  JO.  15;  —  mä  hl 'y3  giurvayHt ma  /akika  Yt.<?.59;  —  nSU  *'yehe'''  ttSij jakikayä  t.io;  —  'yS  tBiryS  franrase  Yt. J.41,  J5-S6.  82;  8»,  77.5-5°;  —  'r^^ tairim/raarasyanam  YL5. 18,  zz,  ip.  77, Y. //.  7;  —  °yeke  tyaonaAe  ar»jal.aspahe Yt.  5.  30 ;  —  tafsatca  AS  °yB  (näml.  aiis srvarü)  Y.p.  11;  —  "«(NSC)  .  .  bSsyqsta FrW, /0.4a;  —  Sai  mqm  °yS  äkasat  atsrö mainyui"V.22.a;  2.  '  a)  ASn.  'rfm  ' Adv. 'trügerischer Weise.betrüglich':  a/trqm *rTm  küsayeiti  (sd.)  anaiwySstS  dalnqm "betrüglich  handhabt  die  Strafgeissel,  wer nicht  . ."  V.  18.  41'.  \az»M  maire  Yt /.  ag:  lies  zamara^
22647:•   ).    vandan'maiius-"    m.    EN.    eines j.  ^o-i««  F.  8:  lie«  x.^««.  A5.<w»«fiirsteii,  Bruders    des    Ar^jaljupa:
=== BRT arsan ===
5619:'raAe  paiti  iamgnöfm'W.ig.^^i^y, —  'raAe\»].  'arSan- m.  EN.  eines  iranischen  Fürsten gtwaya  . .  yat  ahmya  äalva  kandvannti  ausder^ai'ix)'djTiastie,EnkelsdesÄijW(7/a'': "..wo  die  Ä  zusammenkommen"  V.J.  7.   -{■awa^»»    'srum  Yti^.71;  —  Aavöis  'Ins
5631:—  Vgl.   'arSan-.   —   ai.  fifoia-   Name   eines  \  —  'mar  Ao.  J.  2.
5634:•  J.   (g-.  P)   'arSan-  m.   l)  'Mann,  Mann-        Helden';  ».  '<^io«-  und  Bgu.  Grdr.  2.  A eben'  (geschlechtlich)'»:  a)  von  Menschen:      .      ,_ .  .,.,,,
10819:Komp.:  xsayri;\-arsan;  eig,  'der  atsan- ('Hengst,  Held')  unter  den  Herrschern';  vgl. ai.  räjariatha-  m.  Anders  FoV  KZ.  J7.  544, wo  weitere  Litt.  —  >)  Zum  Stammansatz  nnd znei.  s.  S  3lt.  I  b.  2/j.  2,  —  »)  Verunglückte CS.-Bildune.  i  fehlerhaft  fSr  h  der  ZDMG. $4.  [27  gezogene  Schluss  scheint  mir  höchst fraglich.  —  i)  Sollte  GS.  sein.
12415:•  j.  daenav-  f.  'femina',  von  (vierftissigen) Tieren  (im  Gegensatz  zu  arsan-,  uxsan- und  varsnqy-),  in  Verbindung  mit  dem Tiernamen":   ka'iwa   'nu  (IS.)   ,  ,  gava
=== BRT kdrdsaspa ===
30058:•  j.  hitäspa-  m.  EN,  eines  Gegners  des Kjrisaspa:  yat  kama  nijasäni  az>m  (näml lar?säipS)    brü%rS   "urvaxsaya    (sd.)    yat
```


## [2026-09-05T20:31:43.250Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg151.png"
}
```


### [2026-09-05T20:31:43.785Z] TOOL RESULT

```

```


## [2026-09-05T20:31:43.783Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:32:04.038Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 151 -l 151 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg151_hi\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg151_hi.png'); print(im.size)\nw,h=im.size\n# node7 persian box: displayed x 980-1200 y 690-880 of 1545x2000 -> fractions\nbox=(int(0.60*w),int(0.335*h),int(0.80*w),int(0.44*h))\nim.crop(box).save('node7.png')\nbox2=(int(0.24*w),int(0.20*h),int(0.55*w),int(0.30*h))\nim.crop(box2).save('node4.png')\n\"\nls -la node7.png node4.png"
}
```


### [2026-09-05T20:32:43.912Z] TOOL RESULT

```
(3400, 4400)
-rw-rw-r-- 1 sfmqrb sfmqrb 11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  7427 Sep  5 16:32 node7.png
```


## [2026-09-05T20:32:46.229Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/node7.png"
}
```


### [2026-09-05T20:32:46.247Z] TOOL RESULT

```

```


## [2026-09-05T20:33:04.018Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN alfalfa ===\"; grep -n -i -m3 \"alfalfa\" KLN_1966.txt KLN_1971.txt | cut -c1-600\necho \"=== KLN Philip ===\"; grep -n -i -m2 \"Philippos\\|Philip,\" KLN_1966.txt | cut -c1-500\necho \"=== SKT alfalfa/hippopotamus ===\"; grep -n -i -m3 \"alfalfa\\|hippopotamus\" SKT.txt | cut -c1-400\necho \"=== LKT fisfisa ===\"; grep -n -i -m5 \"fisfisa|fiṣfiṣa\\|fisfise\\|Luzerne\\|alfalfa\" LKT.txt | cut -c1-400"
}
```


### [2026-09-05T20:33:04.131Z] TOOL RESULT

```
=== KLN alfalfa ===
KLN_1971.txt:10963:alfalfa, n., lucerne. — Sp., fr. Arab. al-fd?fa?a h . 
KLN_1971.txt:10966:al-fd$fasa h and Sp. alfalfa.). 
KLN_1971.txt:140831:lucerne, n., a plant grown for forage, alfalfa. — 
KLN_1966.txt:2169:alfalfa,  n.,  lucerne.  —  Sp.,  fr.  Arab,  al-fasfasa  . (Cp.  the  collateral  Sp.  form  alfalfez,  which  rep¬ resents  the  intermediate  form  between  Arab. al-fdsfasah  and  Sp.  alfalfa.). alfaqui,  n.,  a  Mohammedan  scholar.  —  Sp.,  fr. Arab,  al-faqfh,  fr.  al-,  ‘the’,  and  faqih,  ‘learned, intelligent’,  fr.  fiqh,  ‘knowledge,  intelligence’, alfenide,  n.,  an  alloy  of  nickel  and  silver.  —  So called  after  the  chemist  Halphen,  who  invented this  alloy  in  1850.  For  the  ending  see  suff.  -ide. Alfred,  masc.  PN.  �
KLN_1966.txt:22230:lucent,  adj.,  bright;  transparent.  —  L.  liicens,  gen. -ends,  pres.  part,  of  lucere,  ‘to  shine’,  fr.  lux,  gen. lads,  ‘light’,  fr.  I.-E.  base  *leuq-,  ‘to  emit  light, to  shine;  bright’.  See  light,  ‘brightness’  and  -ent and  cp.  luce,  lucerne,  lucid,  lucule,  luculcnt, Luzula,  relucent,  translucent,  Noctiluca. lucerne,  n.,  a  plant  grown  for  forage,  alfalfa.  — F.  luzerne,  fr.  ModProvenf.  luzerno,  which  is prob.  a  figurative  use  of  luzerno,  ‘glowworm’ ;  so named  in  allusion  to  the  glittering  g
KLN_1966.txt:23283:—  ModL.,  fr.  Gk.  MvjSixr),  name  of  the  alfalfa, lit.  ‘the  Median  (plant)'.  See  medic.
=== KLN Philip ===
17838:hippish,  adj.,  somewhat  depressed  ( colloq .)  — Formed  with  suff.  -ish  fr.  hip,  ‘melancholy*, hippo-,  before  a  vowel  hipp-,  combining  form meaning  ‘horse*.  —  Gk.  fonro-,  bnr-,  fr.  (777704, ‘horse’,  rel.  to  dial.  Gk.  (xxo4,  for  I.-E.  *ekwos, whence  also  OI.  asvah,  L.  equus,  ‘horse*.  See equine  and  cp.  the  second  element  in  Eohippus, ephippium,  Philip,  Xanthippe, hippo,  n.  —  Short  for  hippopotamus. Hippoboscidae,  n.  pi., 
28516:Philip,  masc.  PN.  —  L.  Philippas,  fr.  Gk.  ®(Xi7r- 1T05,  fr.  91X1717505,  ‘fond  of  horses’,  compound¬ ed  of  91X05,  ‘beloved;  loving’,  and  171:7105, ‘horse’.  See  philo-  and  hippo-  and  cp.  philippic and  the  second  element  in  Xanthippe.
=== SKT alfalfa/hippopotamus ===
=== LKT fisfisa ===
1505:59S.  Ar.  fasfasu: 'Luzerne  Medicag-o  sativa  L.',  auch  fis- fifa;  hieraus  sp.  alfalfa,  alfafe  'dass., spanischer  Klee,  foenum  Burgundiacum', engl,  amerik.  alfalfa.  [DE  100/101. Eguilaz  156.    ML  4002  Anm.
```


## [2026-09-05T20:33:07.348Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA fisfisa ===\"; grep -n -i -m5 \"fisfisa\\|fi.fi.a\\|aspast\\|Luzerne\" PLA*.txt 2>/dev/null | cut -c1-400; ls PLA* 2>/dev/null; ls incoming/PLA 2>/dev/null\necho \"=== AFM fisfisa ===\"; grep -n -m5 \"فصفصة\\|الفصفصة\" AFM_pages.txt AFM.txt 2>/dev/null | cut -c1-300\necho \"=== FVQ ===\"; grep -n -i -m3 \"fisfisa\\|fasfasa\" FVQ_pages.txt 2>/dev/null | cut -c1-300\necho \"=== NYB asp ===\"; grep -n -i -m5 \"aspast\\|^asp\\b|aswar\" NYB_vol2_glossary.txt | cut -c1-300"
}
```


### [2026-09-05T20:33:07.441Z] TOOL RESULT

```
=== PLA fisfisa ===
(eval):2: no matches found: PLA*.txt
(eval):2: no matches found: PLA*
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
=== AFM fisfisa ===
=== FVQ ===
=== NYB asp ===
```


## [2026-09-05T20:33:16.060Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA ===\"; grep -n -i -m6 \"fisfisa\\|fi.fi.a\\|aspast\\|Luzerne\\|Klee\" incoming/PLA/PLA_pages.txt | cut -c1-400\necho \"=== AFM فصفص ===\"; grep -n -m6 \"فصفص\" AFM_pages.txt AFM.txt AFM_alt.txt 2>/dev/null | cut -c1-300\necho \"=== NYB ===\"; grep -n -m6 -i \"aspast\\|asp \\|aswar\" NYB_vol2_glossary.txt | cut -c1-300"
}
```


### [2026-09-05T20:33:16.173Z] TOOL RESULT

```
=== PLA ===
1426:mel - "asfast:                     "Luzerne,              Futterpflanze"           pers.      7 aus       pers.     ul       aspast
1427:           MP.     ana       aspast           8
10163:>22         - Sambalid: "Bockshornklee" < pers. un                                                    sanbalile           ! <—Imp.      yo
11787:fasätin                                                                        210                                                fisfisa
11811:ansıms - fisfisa:                            "Luzerne"         pers.         ?. 7, dtsch.              Alfalfa.
11831:wLs3_                 fisaäfis:             Pl.     veoes          fisfisa q. v.
=== AFM فصفص ===
=== NYB ===
21:My linguistic analysis has been greatly aided by ihe new and revolutionary insight into the character of Middle Iranian bestowed by the Turfan texts. Thanks to them we have an incomparably firmer grasp of Book Pahlavi than was ever possible before. This glossary is therefore closely linked to the
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy .
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.;
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ...
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing 
695:asp ['sp'; SWSY?] horse 4? etc., passim; pl. eas. obl. —-än (’sp’n' ; SWSY?-n' 1922. 271) — Av. (216 sq.) aspa- = OP, Skr
```


## [2026-09-05T20:33:22.822Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA 1420-1432 ===\"; sed -n '1420,1432p' incoming/PLA/PLA_pages.txt | cut -c1-500\necho \"=== PLA 11805-11835 ===\"; sed -n '11805,11835p' incoming/PLA/PLA_pages.txt | cut -c1-500\necho \"=== NYB 695 ===\"; sed -n '695,697p' NYB_vol2_glossary.txt | cut -c1-700"
}
```


### [2026-09-05T20:33:22.912Z] TOOL RESULT

```
=== PLA 1420-1432 ===
er!          -     > isfaranf:               ein    Ort     in       Samarkand,    aus     dem    pers.      Zusı        esfarang     6

      05                                 -
1                - "isfarani:                     Nisba    ve             ”isfarang

     3
mel - "asfast:                     "Luzerne,              Futterpflanze"           pers.      7 aus       pers.     ul       aspast
           MP.     ana       aspast           8


 gut - ”isfanab:                         "Spinat" = ”isbänäh                    q. v.

     .93                                                         9
=== PLA 11805-11835 ===
a3»           - fustuga:                    nom,        un.   v.    is        fustug          "eine    Pistazie".


OR            - fustugi:                     "pistaziengrün".


ansıms - fisfisa:                            "Luzerne"         pers.         ?. 7, dtsch.              Alfalfa.

o5lhs - faßsäga:                             "Rakete",


Als-
     “.               faß$äka
                             ’          - fafääga             q. v.

Aas_          fafakı:             Pl.       v. Es fafaka ga. v

 .
Ais-              fafaka:              "Patrone".

     a,
ls _ faSaka:                           "Patronentasche".


E-                fi$anf:              ägypt.           Ar.   = ar.       faßaka vers.                   Ks fe$ang 8,

wLs3_                 fisaäfis:             Pl.     veoes          fisfisa q. v.

29            _       fisfisa:               "Luzerne"             pers.cuuul                asbast     od.    a,   asfast    9


=== NYB 695 ===
asp ['sp'; SWSY?] horse 4? etc., passim; pl. eas. obl. —-än (’sp’n' ; SWSY?-n' 1922. 271) — Av. (216 sq.) aspa- = OP, Skr
a-soyisn [ "swdšn']
ästavän
```


## [2026-09-05T20:33:37.846Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/فصفص\" --note \"page 151, Arabic fisfis 'alfalfa' etymology\"\npython3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=alfalfa\" --note \"page 151, AHD entry alfalfa (AHD:32)\"\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/اسپست\" --note \"page 151, Persian aspast\"\ncd data/verification/sources/refs\necho \"=== BRT Futter ===\"; grep -n -i -m8 \"asti-.*Futter\\|Futter.*Pferd\\|aspO.asti\\|asp..asti\" BRT.txt | cut -c1-300"
}
```


### [2026-09-05T20:33:41.325Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c914e43b5ccf730f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf07a5b227667cb6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d4c585e6cd04941c.txt
=== BRT Futter ===
```


## [2026-09-05T20:33:45.020Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== فصفص ===\"; grep -n -B2 -A8 -i \"etymology\" c914e43b5ccf730f.txt | head -40; wc -c c914e43b5ccf730f.txt\necho \"=== AHD alfalfa ===\"; grep -n -i -A4 \"alfalfa\" cf07a5b227667cb6.txt | head -30\necho \"=== اسپست ===\"; wc -c d4c585e6cd04941c.txt; grep -n -A6 -i \"etymology\" d4c585e6cd04941c.txt | tail -20"
}
```


### [2026-09-05T20:33:45.107Z] TOOL RESULT

```
=== فصفص ===
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
69-
70- 1.2.2 
--
144- Wikipedia ar 
145-
146: Etymology
147- [ edit ] 
148-
149- PIE word 
150- *h₁éḱwos 
151-
152- Borrowed from Aramaic אַסְפַּסְתָּא ( ʾaspastā ) / ܐܰܣܦܷܣܬܳܐ ( ʾaspestā , “ lucerne ” ) , from Akkadian 𒊍𒉺𒊍𒋾 ( aspastu , “ presumably lucerne ” ) , from Old Median *aspāstiš ( “ lucerne ” ) , from Proto-Iranian *HacwaHastiš ( “ lucerne ” , literally “ horse-food ” ) from Proto-Iranian *Hácwah ( “ horse ” ) + Proto-Indo-European *h₁ed- ( “ related to eating ” ) +‎ *-tis , the Assyrians having it borrowed when modelling their cavalry after the Medes and thus taking over this name for a plant serving as horse food, passing it to the Babylonian, which is the most likely linguistic evolution.
153-
154- Noun
12003 c914e43b5ccf730f.txt
=== AHD alfalfa ===
1:URL: https://www.ahdictionary.com/word/search.html?q=alfalfa
2-FETCHED: 2026-09-05T20:33:40Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: alfalfa
5-
6:American Heritage Dictionary Entry: alfalfa 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
--
48: [Spanish, from Arabic al-fa ṣ fa ṣ a : al- , the + fa ṣ fa ṣ a , alfalfa (variant of fi ṣ fi ṣ a , ultimately (probably via Coptic p-espesta : p- , masculine sing. definite article + espesta , alfalfa) from Aramaic espest ā , from Middle Persian aspast , from Old Iranian aspasti- : *aspa- , horse; see ekwo- in the Appendix of Indo-European roots + *-sti- , food, fodder; see ed- in the Appendix of Indo-European roots ).]
49- (click for a larger image) 
50: alfalfa Medicago sativa 
51-
52- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
53-
54- Indo-European & Semitic Roots Appendices
=== اسپست ===
4231 d4c585e6cd04941c.txt
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
155: Etymology
156- [ edit ] 
157-
158- From Middle Persian [Book Pahlavi needed] ( ʾspst' /⁠aspast⁠/ ) , from Middle Median *aspast , from Old Median *aspāstiš , from Proto-Iranian *HacwaHastiš ( “ alfalfa, lucerne ” , literally “ fodder for horses ” ) .
159-
160- Pronunciation
161- [ edit ]
```


## [2026-09-05T20:34:02.930Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON fasfase ctx ===\"; sed -n '83920,83930p' MON_part1.txt | cut -c1-300; echo \"---\"; sed -n '97955,97965p' MON_part1.txt | cut -c1-300\necho \"=== MON astar ===\"; grep -n -m6 \"استر ]\\|استر (\\|استر:\" MON_part1.txt | cut -c1-300\necho \"=== KNT Vistaspa lexicon ===\"; grep -n -m6 \"Vistaspa-\\|Vištāspa- \" KNT.txt | cut -c1-400"
}
```


### [2026-09-05T20:34:03.069Z] TOOL RESULT

```
=== MON fasfase ctx ===
رم ت‌ 
بندرت دارای گل زرد می‌باشند. گل آذینش 
خوشه‌یی کروی است. در حدود ۰ گونه 
از اين گیاه شناخته شده که همه مصرف 
علوفه دارند و جزو کیاهان مرغوب مرتع 
می باشند؟ رطبه» ی رسیم احمرء 
فصفصه» شدر چمنی» شبدر کل قرمزء حند 
فوقفی» دوثلات الوان» ذوخمسة الوان» 
طریفان» شبذر. شبدر صحرایی: (گیا.) 
کوچک است و در کنار نهرها و مزارع 
می‌روید؛ رجل الارنب» ارنسبی. شبدر 
---
محبت از دل سالك به علت دور ماندن از 
افاضات و عنایات مرد کامل (دکتر گوهرین؛ 
فرهنگ مثنوی ۱۱۴). از توی (میان) علف 
سبز نشده‌ایم: (عسم.) دارای پدر و مادر و 
خانواده هستیم. آزوقه» توشه» خواربار 
(انسان). (گیا.) اسپست» فصفصه. (تص.) 
شهوات و آرزوهای نفس (فرم. سج.) 
علف‌چر: .2 [غ. ف.] [- علف‌چر نده] 
(ص‌فا.) چرند؛ علف» علفخوار (.) 
مقداری علف که جهت دسته‌ای از ستور 
صرف شود. زمینی پر علف که گاو گوسفند 
=== MON astar ===
3139:استر: ۰۲ (.) پارچه‌ای که در طرف 
3144:استر: 2-6-۲ [- آن سوی‌تر ] (ق.) 11 
11742:استر: ۲ [- ستر؛ مربوط به اسب قس. 
65763:راستر: ۲25-۲ [- راست‌تر ] (ص‌ تفض.) 
75572:ستر: ۲صاده [ - استر ] (۱.) استر» بغل. 
=== KNT Vistaspa lexicon ===
1192:pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
```


## [2026-09-05T20:34:09.983Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11740,11748p' MON_part1.txt | cut -c1-400\necho \"=== KNT Vistaspa entry ===\"; grep -n -m6 \"Vistaspa\\b.*name\\|Hystaspes\" KNT.txt | cut -c1-400\necho \"=== KNT asabara ===\"; sed -n '1188,1196p' KNT.txt | cut -c1-600"
}
```


### [2026-09-05T20:34:10.060Z] TOOL RESULT

```
استذ کارات. 

استر: ۲ [- ستر؛ مربوط به اسب قس. 
قاطر ] (.) (جان.) قاطر . 

استراتژی: 2 (.) فن ادارة 
عملیات جنگی؛ دانش رهبری عملیات 
نظامی؛ سوق الجیش. 

=== KNT Vistaspa entry ===
383:Vistdspa ‘Hystaspes’, father of Darius, with sp from ky?
424:Grotefend recognized correctly that the names of two different kings were followed by titles, ‘great king, king of kings’, and then a third simi- lar title in the one which was lacking in the other; that then followed the name of the king’s father, who was the same person in one inscrip- tion as the king in the other, and that in the other the father did not bear the title king. He deci
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya паз
3046:$308. Тнк Position or Apposittves. Apposi- tives, whether nouns or adjectives, usually follow! that to which they are appositive; but the position is otherwise free. Appositives to a subject implied in the verbal ending may stand in any place; cf. DNb 41-5. Chiasmus sometimes is the result of stylistic considerations: XPh 47f уйа ahaniy Jiwa щй marta ariàvà ahaniy ‘happy may I be 
3082:1The only exception is A'Hc 14f Vrslaspahyá пата риса ‘son of Hystaspes by name’, where пата modifies the genitive and is not followed by a generic word; the cast of the sentence eliminates the possibility of a resumptive pronoun.
3136:genitives; further phrases are of the type of the second. At the end, ‘Achaemenian’ is appositive to the initial ‘Artaxerxes’. We may imitate this scheme in English, as follows: ‘Artaxerxes, . . . son of Darius the King, of Darius (who was) son of Artaxerxes the King, of Artaxerxes (who was) son of Xerxes the King, of Xerxes (who was) son of Darius the King, of Darius (who was) son 
=== KNT asabara ===
nsf. ра уй DB 4.91, and perhaps as the first
element of the place-name Paiiiya*uvddd- (see
Lex. s.vv.). $90. PIE fu became pár. Sy, and then Av. sp,
Med. sp, OP s, Skt. gv:
pIE *efuo- ‘horse’, OP asa- in aec. asam and in аѕађата-; OP aspa- (with Med. sp) in waspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. бра, Lt. equos.
pIE *yikuo-, OP visa- ‘all’, also in visadahyu-; OP nspa- (with Med. sp) in vispaeana-; Av. vispa-, Skt. visva-.
pIE *kyd- in Av. spá- ‘throw, set down’, OP sä- ‘erect, build’, in s-aor. pass. früsah[ya] DSf 27 (etymology not certain!). $91. PIE ghu became pAr. Zhu, and then Med.
and Av. zb, Skt. he, but OP z; the OP texts
have one example of the Median value and one of the OP value:
```


## [2026-09-05T20:34:35.666Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor w in تهماسب گرشاسپ لهراسب جاماسب ارجاسپ گشناسب بیوراسپ; do echo \"--- $w\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 151, Persian name $w from Avestan compound in -aspa\"; done"
}
```


### [2026-09-05T20:34:40.833Z] TOOL RESULT

```
Exit code 1
--- تهماسب
/home/sfmqrb/git/rishe/data/verification/sources/web/e55c442b91c16bd1.txt
--- گرشاسپ
/home/sfmqrb/git/rishe/data/verification/sources/web/20f4122769513ca0.txt
--- لهراسب
/home/sfmqrb/git/rishe/data/verification/sources/web/5d4fa5f46b76dd24.txt
--- جاماسب
/home/sfmqrb/git/rishe/data/verification/sources/web/c67782c10d403dd4.txt
--- ارجاسپ
/home/sfmqrb/git/rishe/data/verification/sources/web/b072f5d5d511765a.txt
--- گشناسب
/home/sfmqrb/git/rishe/data/verification/sources/web/8b88ee56d8e1af84.txt
--- بیوراسپ
/home/sfmqrb/git/rishe/data/verification/sources/web/2abd4d8332741352.txt
```


## [2026-09-05T20:34:44.253Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in e55c442b91c16bd1 20f4122769513ca0 5d4fa5f46b76dd24 c67782c10d403dd4 b072f5d5d511765a 8b88ee56d8e1af84 2abd4d8332741352; do echo \"=== $f ($(wc -c <$f.txt) bytes) ===\"; grep -n -A4 \"^ Etymology$\" $f.txt | head -12; done"
}
```


### [2026-09-05T20:34:45.955Z] TOOL RESULT

```
=== e55c442b91c16bd1 (138 bytes) ===
=== 20f4122769513ca0 (138 bytes) ===
=== 5d4fa5f46b76dd24 (138 bytes) ===
=== c67782c10d403dd4 (138 bytes) ===
=== b072f5d5d511765a (138 bytes) ===
=== 8b88ee56d8e1af84 (138 bytes) ===
=== 2abd4d8332741352 (140 bytes) ===
```


## [2026-09-05T20:34:54.919Z] TOOL CALL #61: ToolSearch

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 3
}
```


### [2026-09-05T20:34:54.924Z] TOOL RESULT

```


```


## [2026-09-05T20:35:34.010Z] TOOL CALL #62: WebSearch

```json
{
 "query": "Tahmasp etymology Avestan Taxma-aspa \"strong horses\" Middle Persian name"
}
```


## [2026-09-05T20:35:34.359Z] TOOL CALL #63: WebSearch

```json
{
 "query": "Gushnasp etymology Avestan varshni \"male\" Adur Gushnasp name aspa"
}
```


### [2026-09-05T20:35:42.031Z] TOOL RESULT

```
Web search results for query: "Tahmasp etymology Avestan Taxma-aspa "strong horses" Middle Persian name"

Links: [{"title":"Jamaspa - Wikipedia","url":"https://en.wikipedia.org/wiki/J%C4%81m%C4%81sb"},{"title":"What is the status of a horse in Zoroastrian religion? (TMY – JJ of 8-7, 15-7, 22-7 and 29-7-18) | Ramiyar Karanjia","url":"https://ramiyarkaranjia.com/2018/09/07/what-is-the-status-of-a-horse-in-zoroastrian-religion-tmy-jj-of-8-7-15-7-22-7-and-29-7-18/"},{"title":"Tahmuras","url":"https://en.wikipedia.org/wiki/Tahmuras"},{"title":"PERSONAL NAMES, IRANIAN ii. AVESTAN NAMES - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/"},{"title":"Arjasp","url":"https://en.wikipedia.org/wiki/Arjasp"},{"title":"Jamaspa","url":"https://en.wikipedia.org/wiki/Jamaspa"},{"title":"Amazasp I","url":"https://en.wikipedia.org/wiki/Amazasp_I"},{"title":"Tahmasp - Name Meaning, Origin, Popularity, and Related ...","url":"https://www.name-doctor.com/meaning/tahmasp"},{"title":"Ashva","url":"https://en.wikipedia.org/wiki/Ashva"},{"title":"The Ts of Persian names | Onomastics Outside the Box","url":"https://onomasticsoutsidethebox.wordpress.com/2023/04/24/the-ts-of-persian-names/"}]

Based on the search results, here's what I found regarding the etymology of Tahmasp:

The name Tahmasp derives from Ancient Persian "Ṭahmāsp," composed of two elements: "takhma" (strong, brave, courageous) plus "asp," from the Old Persian "aspa" (horse). More specifically, it derives from the Old Persian word "takhma > Takhmaspa > Ṭahmāsp".

The search results confirm that Tehmāspa means "having a strong horse", which aligns with your query about the meaning "strong horses." The "-aspa" element is widely documented in Persian names, where the second word means aspa, i.e. horse, and this element is also found in the names of people like Vishtaspa, Arjaspa and Lohraspa.

The results also show that Taxma comes from compounds with Avestan taxma- meaning "brave, courageous", which corresponds to the "takhma" element you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T20:35:42.909Z] TOOL RESULT

```
Web search results for query: "Gushnasp etymology Avestan varshni "male" Adur Gushnasp name aspa"

Links: [{"title":"Gushnasp","url":"https://en.wikipedia.org/wiki/Gushnasp"},{"title":"ĀDUR GUŠNASP – Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/adur-gusnasp-an-atas-bahram-see-atas-that-is-a-zoroastrian-sacred-fire-of-the-highest-grade-held-to-be-one-of-/"},{"title":"Adur Gushnasp","url":"https://en.wikipedia.org/wiki/Adur_Gushnasp"},{"title":"Mah-Adhur Gushnasp","url":"https://en.wikipedia.org/wiki/Mah-Adhur_Gushnasp"},{"title":"Azen Gushnasp","url":"https://en.wikipedia.org/wiki/Azen_Gushnasp"},{"title":"Aspad Gushnasp","url":"https://en.wikipedia.org/wiki/Aspad_Gushnasp"},{"title":"Adhur Gushnasp","url":"https://en.wikipedia.org/wiki/Adhur_Gushnasp"},{"title":"Izad Gushnasp","url":"https://en.wikipedia.org/wiki/Izad_Gushnasp"},{"title":"Arvand Gushnasp","url":"https://en.wikipedia.org/wiki/Arvand_Gushnasp"}]

Based on the search results, I found information about the etymology of Gushnasp related to Adur Gushnasp:

The name Gušnasp means "Stallion." The search results indicate this refers to a male horse. According to legend, the fire is called "Gušnasp" because it settled upon the mane of a horse (asp).

However, the search results don't contain specific information about the Avestan term "varshni" meaning "male" or its connection to the name Gushnasp's etymology. The results focus on the meaning of "Gushnasp" as a whole (stallion/male horse) rather than breaking down the components "varshni" + "aspa" that you're asking about.

If you're looking for more detailed etymological analysis connecting the Avestan word "varshni" (male) with the "aspa" (horse) component, you might need to consult specialized Avestan linguistic resources or scholarly articles specifically on Iranian onomastics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:35:49.718Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/\" --note \"page 151, Iranica: Avestan personal names in -aspa (Vistaspa, Keresaspa, Aurvat.aspa, Arejat.aspa, Jamaspa)\"\npython3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Gushnasp\" --note \"page 151, Gushnasp 'stallion' name element\"\n"
}
```


### [2026-09-05T20:35:55.977Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a0dcd2f79e777235.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bac3b8cddc480f2e.txt
```


## [2026-09-05T20:35:58.864Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== iranica avestan names: aspa mentions ===\"; grep -n -o -E \".{200}aspa.{200}\" a0dcd2f79e777235.txt | head -20"
}
```


### [2026-09-05T20:35:58.985Z] TOOL RESULT

```
=== iranica avestan names: aspa mentions ===
64:slender horses” (cf. above), Vīštāspa- (no. 379) “Possessing horses untied (for racing)” (based on an ancient technical term of Aryan horse-racing; cf. above) and a number of other names containing – aspa- “horse”; Paršaṱ.gu – (no. 248) “Possessing spotted bullocks”; Pərəθuu-aršti – (no. 255) “Possessing a far-reaching spear” and other forms with – aršti- “spear”; Pouru-čistā -, fem. (no. 263) “Posses
68:. 146) from Av. friia – “dear, own”; Kāta – (no. 211) from compounds with Av. – kāta- “desired”; Pəṧana – (no. 256) from Av. pəṧana – “battle, fight”; Spiti – (no. 292) perhaps shortened from *Spitii-aspa – “Possessing white horses” (since his brother is named Ǝrəzrāspa – “Possessing fleet horses”); Taxma – (no. 304) from compounds with Av. taxma- “brave, courageous”; Uštra – (no. 331) based on the co
79:i besides) from Frašaoštra -, Karsn-aiiana – from Karsna -, Vaŋhuδāt-aiiana- from Vaŋhuδāta- ; with -ā/ăna – Frāiiazəṇt-ana – from Frāiiazəṇta -, Frii-āna – from Friia -, Haēčaṱ.asp-āna – from Haēčaṱ.aspa -, Jāmāsp-ana – from Jāmāspa -, Kahrk-ana – from *Kahrka -, Tūmāsp-ana – from *Tūmāspa -, Xšuu iβrāsp-ana – from Xšuuiβrāspa -, but also Gaiiaδāstaii-ana – from Gaiiaδāsti – and Gaoraii-ana – from Ga
```


## [2026-09-05T20:36:06.890Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -o -E \".{250}(Kərəsāspa|Auruua|Arəǰa|Arəja|Jāmāspa|slender horses|Tūmāspa).{250}\" a0dcd2f79e777235.txt | head -12"
}
```


### [2026-09-05T20:36:06.946Z] TOOL RESULT

```
64:i.1 (possessive compounds): Aiβi-xvarənah – (no. 6) “Possessing splendor lavishly”; Aṧa.nəmah – (no. 37) “Showing reverence to the Truth” (cf. above); Hao-srauuah – (no. 167) “Possessing good reputation” (cf. above); Kərəsāspa- (no. 216) “Possessing slender horses” (cf. above), Vīštāspa- (no. 379) “Possessing horses untied (for racing)” (based on an ancient technical term of Aryan horse-racing; cf. above) and a number of other names containing – aspa- “horse”; Paršaṱ.gu – (no. 248) “Possessing spotted bullock
79:-aiiana – (showing vrddhi besides) from Frašaoštra -, Karsn-aiiana – from Karsna -, Vaŋhuδāt-aiiana- from Vaŋhuδāta- ; with -ā/ăna – Frāiiazəṇt-ana – from Frāiiazəṇta -, Frii-āna – from Friia -, Haēčaṱ.asp-āna – from Haēčaṱ.aspa -, Jāmāsp-ana – from Jāmāspa -, Kahrk-ana – from *Kahrka -, Tūmāsp-ana – from *Tūmāspa -, Xšuu iβrāsp-ana – from Xšuuiβrāspa -, but also Gaiiaδāstaii-ana – from Gaiiaδāsti – and Gaoraii-ana – from Gaori -; with – iia – Naotair-iia – (with enlarged Naotairii-āna -) from Naotara
```


## [2026-09-05T20:36:15.615Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o -E \"• *j\\.[^:]{0,60}aspa[^:]{0,120}\" BRT.txt | head -30"
}
```


### [2026-09-05T20:36:18.441Z] TOOL RESULT

```
ugrep: error: error at position 625
\xf4[\x80-\x8f][\x80-\xbf][\x80-\xbf]){0,120}
                exceeds complexity limits___/
```


## [2026-09-05T20:36:20.890Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"aspa-\" BRT.txt | grep \"• *j\\.\" | cut -c1-260 | head -30"
}
```


### [2026-09-05T20:36:20.940Z] TOOL RESULT

```
5400:•  j.  auniSaspa-  Adj.   'des  Rosse   weiss  |     AbleiL  -  Zum  V.  a,^--.   -   mp.  (Fü.)  a^i, sind':  mi'irim  °f)m  Yt/o.ioa.  1     np.  nn,  «f/.
5412:•  j.  araja^aspa-  m.  EN.  eines  Hyaona- Fürsten":  mairyehe  hyaonahe  "pake  \'tf/. 30;  —  drfantptn^a  'piin  Yt.5.  109;  — tum  yazata    vandar^mainis  (sd.)    'ps  Vt.
5566:•  j.  'airyaman-  m.  Name  des  mit  J  (7/r- ,  •  j.  'aurvataspa-  Adj.  'der  schnelle ysmä  isys  beginnenden  Gebets  Y.54.1:  Rosse  hat';  a)  von  ^rar-imd  Äj'ari>.tiiji^u-: 'matiim  mq^ranqm  maBittm  Yt.j.5;  —  Är'ur?  "toffi  YL/0
5835:KompA.    —    Vgl.    aHt-n-.    —    ai.  vgl.  asihaii- vänl;    asihima-l-    Adj.  S)     —    Pü. :    ailömaaii, laaSmai-d.  —  ■)  Hds.  aslir.i'.  —  »)  Them.  An 2.  St.  Hds.  ast.ahc.  —  J)  Slveri.  unter  aa/ia-.-. —  4
5845:•  j.  aspa-nhad-  Adj.  'Rosse  an-,  über- fallend': alis  -nhms  (NS.)"'  Aog.  7..?.
7465:•  j.  Isu.aspa-  Adj.  'der  schnelle  Rosse hat':  laxtnim  staotänm  .  .  "pfm  Yt.  ij. 12;  —  yat  mqm  Iura  pazdayanta  °fia naotaraca'1  Yt.  77.55;  S^.
8999:•  j.  kadrva.aspa-  m.  Name  eines  Bergs oder  Gebirgs:  ahmat  haia  garayS  frao- xsyqn  .  .  'pasta  Yt.  ig.  6  ",
11150:•  j.  caS'wara.aspa-  n.  'TE'äfnnio»,  Vier- gespann': yuxta  (sd.)  °/«^^  F.^t
15285:•  j.  'payah-  n.  'Milch',  auch  Plur.:  *'yB F.  10  i  —  nsit  *yB  fsuta  (sd.) , .  toit  gstd . . ^■7-  77;  —  aipi.yiaurvatqm  aspayanqm^a °yar3hqm  gävayanamcä  malsinatiqmca  buz- yanqmla  hqm.vaoirinqm  la.vaoirinqm  V. 5.  5a;  
16225:•  j.  pouru.aspa-  Adj.  'der  viele  Rosse  be- sitn,  rossereich':  'ps  yaka  paourusaspahe Vyt  a; —  '^J»»  b«tvSMya%a  *pouruiaspahe Az.4.
16313:•  j.  pourusaspa- '*  m.  EN.  des  Vaters Zara^ustras:  'ps ..yat  hi  tum  ussayaaha .  .  tara%ultra  nmänahe  'paheH.g.xy,  V. IQ.  4,  46,  F.4£;  —  puhnm  yai  'pahe  . . zarahustnm  Yl  5.  18;  V.  jp.  6;  —  mä OtaraySis  saraiustrak
17508:•  j.  fraoftataspa-  Adj,  "mit  schnauben- den Rossen':  masa  xiahra  . .  "pa  (APn.) Yt5.i30.
21841:•  j.  yuxta.aspa-  Adj.  (fem-  'pä-)  'ge- schirrte Rosse  habend':  drväspqm  .,'pam var>lli.ra%qm  Yt.p-a.
25166:•  j.  ranjat.aspa-  Adj.  (fem.  -/ä-)  'der die  Rosse  flink  laufen  lässt':  uiänhfm  .  . TTOlm  'pqm  G.5.  5.
25184:•  j.  ravat-aspa-  Adj.  (fem.  'pä-)  'der  die Rosse  flink  laufen  lässt':  usatjfum  . .  xJ^iy riTm  °pqm  G.j.  J.
27425:•  j.  srifa-  m.  'Nüstern':  yal .  .  aspa- nqmca  'fa  xsfufsqn  "und  wenn  die  Nüstern der  Pferde  in  Aufregung  geraten"  Yt /0.113.
28658:•  j.  'haek- V.  'giessen'.  Praes.  3  hi'a-, 9  hinla-. —  PPfP.  °Aixta-;  Inf.  Aixtayai-ca, •Aincäi;  Absol.  'lalhm.  [S.  noch  "^haf- c<U.aspa-:[
29294:•  j.  babaspa-  m.  EN.  eines  Gläubigen: •pake  asaotiS  Yt  13. 10a.
29705:Yt. /o.  141;  —  mihrpm  ..  -ra^aossm  Vt.  •  j.  hazaorö.aspa-  Adj.  (fem.  °/5-)  'mit
30725:•  j.  "hv-aspa-,  p.  "uv-aapa-  Adj.  (fem. 'Pä-)  'des  Ross(e)  gut,  tüchtig  ist  (sind)': 'ps  ahi  *hurähvS  Yt  i0.j6;  —  lä^wan.- satim  ayan.baranqm  (sd.)  'p3i  naire banmnSi
```


## [2026-09-05T20:36:57.169Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16482,16500p' BRT.txt | cut -c1-400\necho \"=== search baevar aspa ===\"; grep -n \"aspa\" BRT.txt | grep -i \"baevar\\|bJvar\\|bävar\" | cut -c1-300 | head"
}
```


### [2026-09-05T20:36:57.241Z] TOOL RESULT

```
(NS.)"  Yt.;o,i4i.
Pü.!  bevor  iahn,  (lu  Yt  /)')  erl.;  vat  bevor iasmik  f  kus  SOOO  menük  d  sar  äsäyend  u  iär i  cahnth  JkunenJ\  Tgl.  tu  hataBra^aoia'-,  — ')  Them.   —   s>  Elwas  abweichend  lu  Yt.  6.
•  j.  baevar9.patay-  ni.  'Herr  Über  Zehn- tausend": pu%rar»hs  'tayd  Yt.  r^.  59;  — ää'iunqm  'paitinqm ''  Yt.  13. 38.
■)  warum  heiEiendie^.  so?  Ggr.s Erkliinmg, OK.  T96  halte  ich  für  unwahrscheinlich,  die TOn  Gdn.  3YL  136  und  Jm.  JAOS.  13.  cccc für  unmöglich.
•  j.  baevara.fraskomba-  Adj.  'auf  zehn- tausend Tragbalken  ruhend':  nmämm  .  . saiö.raocamm  .  .  hazatirS.sfunim  .  .  'bim Ytj.ioi.
•  j.  bacvar9.mi§ta-  Adj.  'mit  zehntausend T(irnien'(?) :  nmän?m  ..  satS.stärum  haza- f}rB.frasHmban»m  'tfm  ba^jar>.va^ayan7m "ein  Haus  ..  mit  loooo  Türmen,  loooo Warten"  V.  z.V.  28,  zit  *Vyt.#j.
*miila-  n.[  -  ?  -.  —  Pü. :  xänak  I ..  bevor  mos iri-ar  3parlak  "ein  Haus  . .  10  ooo  grosse, loooo  kleine" (?).
•  j.  baevar3.vaeSayana-  Adj.  'mit  zehn- tausend Warten':  nmämm  . .  bagvan.misUm 'tarn  V.  18.  aS;  zit  Vyt  4$.
Pü. :  s.  boevar/.miita:
•  j.  baevarfl.vär-  m.,  Flur,  'zehntausend Regentropfen'(?):^(i>'i»'<i  äunma ..upa.apjm Aazanrö.varayö (sd.)  -värascii (NP.)  V. 21.%.
Pü. !  bhiar-  vjrön.
•  j.  baevar«.spasan-  Adj.  'der  zehn- tausend Späher,  Wächter  hat',  von  Mikra: mi%rs  .  .  yS  'sanS  (NS,)"'  Yt  to.  24;  — mi^rB  .  .  yS  'sänö  (NS.)"  Yt  10.  60.
Zum  V.  sfas:  —  ')  Them.
•  j.  baeSatastura-  patr.  Adj.  'von  BaSsata- stura'-'>  abstammend,  dessen  Nachkomme': fratura  asntta  'rä  (GS.)  asaomJYt.  13.12$.
Ableit  (mit  Verschiebung  des  Wortakzents) aus  *baFiata'ilura-')  a>.  EN.  (Bed,?  *baeJoia- vU.  PFP.,  s.  bii-  und  *mtmataseura-).  —  >)  S. aber  No.  2.  —  »)  Oder  aber  aus  *iiSo/os/ura; zn  S  /00  a.  B?
•  j.  bae^aza-  1)  Adj.  (fem.  'sr-)  'heilend, heilkräftig,  heiltätig';  a)  von  Mond  imd Sternen:  mawi^m  ..  bay>m  'Km  Yt". 5;  —  vanantim  stär>m  .  .  °wm  Yt  21. 1.  b)  sonst:  als3  , ,  asti  °zanqm  bag- sai:yS.t)mö  yat  *mq%r?m.sp>nt»m.batiasyB V.7.44;  zitYtj.6;  —  mq^ranqm  'am .  .  bal^atyBJimim  Yt  J.  S;  —  vaca  ars- uxoa    van'hrayms    'zis    (A
dby  Google
915
baesaza.kai-
=== search baevar aspa ===
```


## [2026-09-05T20:36:58.386Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Jamaspa\" --note \"page 151, Jamasp/Jamaspa name meaning\"; python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Arjasp\" --note \"page 151, Arjasp < Av. Arejat.aspa\""
}
```


### [2026-09-05T20:37:00.690Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4b12144eb927f000.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2baae0e3ffbe4077.txt
```


## [2026-09-05T20:38:21.670Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bewar ===\"; grep -n -o -E \"b[eē]war[a-z]*[^ ]*.{0,120}\" PHD.txt | head -5\necho \"=== NYB bewarasp ===\"; grep -n -i -m3 \"bevarasp\\|bēwarasp\\|bevar\" NYB_vol2_glossary.txt | cut -c1-200\ncd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Jamaspa wiki ===\"; grep -n -i -m6 -A3 \"name\\|etymolog\" 4b12144eb927f000.txt | sed -n '1,30p'"
}
```


### [2026-09-05T20:38:25.574Z] TOOL RESULT

```
=== PHD bewar ===
2880:bēwar.
=== NYB bewarasp ===
995:bevar [bywl] ten thousand; 2 — späh an army of 20000 men 1811-16-17; 12 ~ späh 29233; won 15 ~, 14 ~, 13 ~ 2372.17, 248-11; 131 ~ ziön äyend 24115; 12 x 12 ~ 2427; 12 ~~ 251; 3 ~ nēzak (g. 
=== Jamaspa wiki ===
63: Name 
64-
65- 2 
66- In the Avesta 
--
158: Illustration of Jamaspa in the Shahnameh 
159-
160- In-universe information 
161- Affiliation Vishtaspa 
--
166: Name
167- [ edit ] 
168-
169: The name Jamaspa is widely considered to be a contraction of tetrasyllabic jāma-aspa , an Avestan compound term, where the second word means aspa , i.e. horse. This term is also found in the names of people like Vishtaspa , Arjaspa and Lohraspa . [ 2 ] Since they all originate from the same story, it has been interpreted as an important element in their culture. However, the meaning of the first term is unclear. [ 1 ] One interpretation connects jāma- to Vedic kṣāmáh- , with the meaning burnt, singed . [ 3 ] On the other hand, Gershevitch proposed leading horses , [ 4 ] whereas Schwartz has argued for he who bridles horses . [ 5 ] 
170-
171- In the Avesta
172- [ edit ] 
--
181: According to later tradition, it is Jamaspa , who acquires a leadership role in the Zoroastrian community after the death of Zarathustra and it is him who writes down his teachings in the Avesta . [ 7 ] He is a prominent figure in the Jamasp Namag ( Story of Jamasp ), also known as Ayatkar i Zamaspik ( Memorial of Jamaspa ). [ 9 ] This text discusses a number of topics framed as a dialogue between him and Vishtaspa. [ 10 ] He also appears in works like the Denkard , the Ayadgar i Zariran and the Shahnameh . [ 1 ] 
182-
183- References
184- [ edit ] 
--
212: \n<!-- B -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Boyce"},"first":{"wt":"Mary"},"author-link":{"wt":"mary Boyce"},"year":{"wt":"1987"},"chapter":{"wt":"Ayādgār Ī Jāmāspīg"},"title":{"wt":"Encyclopædia Iranica"},"title-link":{"wt":"Encyclopædia Iranica"},"location":{"wt":"New York"},"publisher":{"wt":"Routledge and Kegan Paul"},"volume":{"wt":"III"},"pages":{"wt":"126–127"},"chapter-url":{"wt":"https://www.iranicaonline.org/articles/ayadgar-i-jamaspig-memorial-of-jamasp-a-short-but-important-zoroastrian-work-in-middle-persian-also-known-as-the-/"}},"i":1}},"\n<!-- F -->\n<!-- F -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Malandra"},"first":{"wt":"William W."},"year":{"wt":"2008"},"chapter":{"wt":"Jāmāspa"},"title":{"wt":"Encyclopædia Iranica"},"title-link":{"wt":"Encyclopædia Iranica"},"location":{"wt":"New York"},"publisher":{"wt":"Routledge and Kegan Paul"},"volume":{"wt":"XIV"},"pages":{"wt":"456–457"},"chapter-url":{"wt":"https://www.iranicaonline.org/articles/jamaspa/"}},"i":2}},"\n* ",{"template":{"target":{"wt":"cite book ","href":"./Template:Cite_book"},"params":{"title":{"wt":"The Cambridge History of Iran"},"title-link":{"wt":"The Cambridge History of Iran"},"chapter":{"wt":"Zoroastrian Pahlavi Writings"},"last":{"wt":"de Menasce"},"first":{"wt":"Jean P."},"author-link":{"wt":"Jean de Menasce"},"editor-last":{"wt":"Yarshater"},"editor-first":{"wt":"Ehsan"},"editor-link":{"wt":"Ehsan Yarshater"},"year":{"wt":"1983"},"publisher":{"wt":"Cambridge University Press"},"volume":{"wt":"3(2)"}},"i":3}},"\n<!-- G -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Gershevitch"},"first":{"wt":"Ilya"},"author-link":{"wt":"Ilya Gershevitch"},"year":{"wt":"1969"},"title":{"wt":"Studia classica et orientalia Antonino Pagliaro oblata"},"chapter":{"wt":"Amber at Persepolis"},"location":{"wt":"Roma"},"publisher":{"wt":"Herder"},"volume":{"wt":"II"},"pages":{"wt":"981"}},"i":4}},"\n<!-- J -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Jackson"},"first":{"wt":"A. V. Williams"},"author-link":{"wt":"A. V. Williams Jackson"},"year":{"wt":"1965"},"title":{"wt":"The Prophet of Ancient Iran"},"location":{"wt":"New York"},"publisher":{"wt":"Columbia University Press"},"url":{"wt":"https://archive.org/details/zoroasterprophet00jack"}},"i":5}},"\n<!-- M -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Mayrhofer"},"first":{"wt":"Manfred"},"author-link":{"wt":"Manfred Mayrhofer"},"year":{"wt":"1992"},"title":{"wt":"Etymologisches Wörterbuch des Altindoarischen - 1. Band"},"location":{"wt":"Heidelberg"},"publisher":{"wt":"Carl Winter Universität"},"url":{"wt":"https://archive.org/details/zoroasterprophet00jack"},"archive-url":{"wt":"https://archive.org/details/etymologischesworterbuchdesaltindoarischenmayrhoferewa11992rep_25_b/mode/2up"},"archive-date":{"wt":"2020-04-10"},"access-date":{"wt":"2026-01-10"}},"i":6}},"\n<!-- S -->\n* ",{"template":{"target":{"wt":"Cite book","href":"./Template:Cite_book"},"params":{"last":{"wt":"Schwartz"},"first":{"wt":"Martin"},"year":{"wt":"1975"},"title":{"wt":"Monumentum H. S. Nyberg"},"chapter":{"wt":"Proto-Indo-European √gīem-"},"location":{"wt":"Tehran, Liège"},"publisher":{"wt":"Bibliothèque Pahlavi"},"series":{"wt":"Acta Iranica"}},"i":7}},"\n<!-- V -->\n<!-- W -->\n<!-- Y -->\n* ",{"template":{"target":{"wt":"cite book ","href":"./Template:Cite_book"},"params":{"title":{"wt":"The Cambridge History of Iran"},"title-link":{"wt":"The Cambridge History of Iran"},"chapter":{"wt":"Iranian National History"},"last":{"wt":"Yarshater"},"first":{"wt":"Ehsan"},"author-link":{"wt":"Ehsan Yarshater"},"editor-last":{"wt":"Yarshater"},"editor-first":{"wt":"Ehsan"},"editor-link":{"wt":"Ehsan Yarshater"},"year":{"wt":"1983"},"publisher":{"wt":"Cambridge University Press"},"volume":{"wt":"3(1)"},"isbn":{"wt":"978-0-521-24693-4"},"chapter-url":{"wt":"https://archive.org/details/yarshater-1983-iranian-hist-trad/page/358/mode/2up"}},"i":8}},"\n",{"template":{"target":{"wt":"refend","href":"./Template:Refend"},"params":{},"i":9}}]}'> 
213-
214- Boyce, Mary (1987). "Ayādgār Ī Jāmāspīg" . Encyclopædia Iranica . Vol.   III. New York: Routledge and Kegan Paul. pp.   126– 127. 
215-
```


## [2026-09-05T20:39:08.238Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mule ===\"; grep -n -o -E \".{0,80}mule.{0,80}\" PHD.txt | head -5\necho \"=== PHD astar ===\"; grep -n -o -E \"astar \\[[^]]*\\][^.]{0,60}\" PHD.txt | head -5\necho \"=== HRN asb entry ===\"; grep -n -E \"^[0-9]+\\. *(esb|asb|esp)\" HRN.txt | head -5\necho \"=== HUB 4465 ctx ===\"; sed -n '4460,4470p' HUB.txt\necho \"=== HUB 6288 ctx ===\"; sed -n '6285,6292p' HUB.txt\necho \"=== HUB 7558 ctx ===\"; sed -n '7556,7562p' HUB.txt"
}
```


### [2026-09-05T20:39:11.849Z] TOOL RESULT

```
=== PHD mule ===
ugrep: error: error at position 80
][\x80-\xbf]*){0,80}
                    \___exceeds complexity limits


=== PHD astar ===
314:astar [dušstl] west
521:astar ['wsstl] east
621:astar [wstl = Av. wastra-] clothing, garment
=== HRN asb entry ===
1114:77. esp, esb 'Pferd'.
1134:80. espend 'Raute', esfend, isfend, spend,
=== HUB 4465 ctx ===
a) einigemal vor Zischlauten (s, z, s, z) und y sowie
nach den Palatalen 6 und /: atis Teuer (so immer bei Vullers)
fiir alteres atas (vgl. Horn Nr. 7), afgh. LW. atas, paz.
ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
jfidan = pasanjldan 'besprengt werden, aus "^pal-sinc-Uan
(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
pieman (pazmdn^ puzmdn) *bereuend* aus paseman; hizisk
*Arzt*, arm. hzisk (aus^hizisk iuv ^bisizk), skr. bhisdj- 'Arzt'
(unter Mitwii^kung des i der ersten Silbe); hiayar Viel* =
ap. ^vasi-ddra- zu bas Viel' = ap. vasiy (unter Mitwirkung
des folgenden y) ; dadistan 'Urtheir = paz. dadastan, u. s. w. ;
=== HUB 6288 ctx ===
pasa-: erst in jiingerer Zeit entlehnt?
§ 71. Nach dem (tonlosen) s ist p als p geblieben
(gleichviel ob sp = ap. sp auf idg. sp oder k^v zurtickgeht);
asp *) 'Pferd' = zd. aspa-, dazu aspist Xuzerne' H. 79 ; as-
pand *Raute* H. 80, gospand Kleinvieh' H. 942 ; supar Tflug
H. 696; supurdan 'anvertrauen H. 697; sipas Dank, Lob'
(Etym.?) H. 698; sipah 'Heer H. 699; sipar 'SchM H. 700;
sipardan *auf etwas treten' H. 701; supurz *Milz H. 702;
=== HUB 7558 ctx ===
r = phi. paz. np. s: asp *Pferd* = ap. aspa-; aspand
*Raute' = zd. spenta-; siped Veiss' = zd. spaeta-; sipihr
'Himmel* = ap. 2md-Qi-, skr. gvitra-; phi. harvisp jeder=^
ap. haruva- -)- vispa- ; mit Ausfall des p : suvHr *Reiter =
ap. asabara-] astar ^Maulesel' = ap. ^asatara-, skr. agva-
tara-; sa^ Hund', medisch andau, zd. spa; — siyah *schwsirz
•^ zd. syava- (aber kasaf 'Schildkrote' = zd. kasyapa-,
```


## [2026-09-05T20:39:17.931Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1114,1135p' HRN.txt; echo \"-----\"; sed -n '1189,1200p' HRN.txt\necho \"=== HRN suvar ===\"; grep -n -E \"^[0-9]+\\. *(suvar|suvär|suvâr)\" HRN.txt | head"
}
```


### [2026-09-05T20:39:17.996Z] TOOL RESULT

```
77. esp, esb 'Pferd'.
ap. Aspa[cana-, uv]aspa- fschöne Pferde habend');
aw. aspa- 'Pferd'; phlv. asp; ai. dgva-,
kurd. hasp; af>'. fls, aspa (fem.) 'Pferd, Stute'; oss.
d. äfsä, t. yäfs 'Stute' (41); bei. aps, haps (LW. asp)
(4); wa;K. yas, minj. ydsap, yasp,
ap. asa[hara' und np. es[^^r (No. 86) stützen sich
gegenseitig und scheinen eine Nebenform asa- zu be-
weisen. Arm. LW. aspet steht natürlich für '^asp{a)pet,
78. isper ud^ isperü, isferüd 'ein kleiner Vogel' (bei AM. 226
Zeile 11 neben dem Sperling genannt).
Nöldeke (mündliche Mitteilung) vergleicht deutsch
Sperling (siehe Kluge, s. v.).
79. esjnst, uspust, ispist 'Luzerne'.
phlv. aspast 'Luzerne'.
bei. LW. aspust (7).
Wörtlich 'Pferdefutter' von esp und [/'ad-, Nöldeke,
ZDMG. 32, 408, Kärnämak, 54 '). Bartholomae
macht mich auf die ganz ähnliche Bedeutung von got.
aihvatundi aufmerksam.
80. espend 'Raute', esfend, isfend, spend,
aw. spenta- heilig ; phlv. spand, arm. LW. spand
-----
86. ester ^Maulesel'.
phlv. astar; ai. agvatard- 'Maulesel'.
kurd. istir, histir; bei. istal, n. hastal (438).
87. iiStur *Kameer, sutur.
aw. ustra- 'Kameel'; phlv. ustrlastän (vd. 15, 68);
ai. üstra-,
kurd. LW. (?) hustur^ sutur; bei. hustar etc. (161);
wa/. ü^tür^ siyn. stur, sar. xtiir, LW.(?).
88. eSk *Thräne .
g. sah,
aw. *asraka (vergl. skr. dgra-), *arsaka (Hörn, Indog.
Forsch., II, 136).
=== HRN suvar ===
```


## [2026-09-05T20:39:25.685Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -m3 -A3 \"3\\.41 HORSE\\|3.41 Horse\" SYN.txt | cut -c1-800\ngrep -n -m2 -o -E \".{0,200}equus.{0,300}\" SYN.txt | head -3"
}
```


### [2026-09-05T20:39:29.852Z] TOOL RESULT

```
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
3745-In the inherited names of animals | pent’, ‘hare’, and ‘mouse’ here and there is little to be said about their se- there, is attributed to taboo (cf. esp. mantic source. For in most of them the Meillet, Ling. hist. 281 ff.). This has Toot connection is wholly obscure. The | doubtless played a part in individual interest in this chapter lies rather in the | cases. But one hesitates to make too oes, substitutions, and shifts of appli- | much of this factor when one observes cation, that virtually every inherited animal eas a of certain inherited animal | name (and for that matter nearly every = ee e that of the ‘bear’ in Slavic | inherited word in other classes, as in the
3746-€rmanic and those for ‘wolf’, ‘ser- | words of relationship, etc.) has been dis-
3747-135
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,300}
                       \___exceeds complexity limits
```


## [2026-09-05T20:39:33.393Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"3.41 Horse\\|3.41 HORSE\\|3.41 Hors\" SYN.txt | head; awk 'NR>3800 && NR<4200 && /aspa|equus|equos|hippos/' SYN.txt | cut -c1-700 | head -6"
}
```


### [2026-09-05T20:39:35.439Z] TOOL RESULT

```
3744:CHAPTER 3 ANIMALS 3.45 Foau, Cott gal eANo 3.46 Ass, DonKEY 3.12 Mate (adj.) 3.47 Mute gia ene 3.51 Hen, Catcxen (Generic) Blan CASTE 3.52 Cock Blo ESTO 3.53 CAPON 3.16 PasTuRE (vb.) aa ee ON chaaeh Pe, 3.55 CHICKEN 3.18 HerDSMAN aA Goan 3.19 STABLE, STALL ne Duue 3.20 CATTLE (Bovine Species) et at ae se 3.612 Purry a oe 3.62 Car 3 4 CALF 3.63 Mouse eed tae AM ; eS a 3.66 FISHERMAN 3.28 Ews 3.71 Wo.ur | 3.29 Lams 3.72 Lion 3.31 Swint 3.73 BEAR 3.32 Boar 3.74 Fox | 3.33 Barrow 3.75 DEER i 3.34 Sow 8.76 MonxkEY 3.35 Pie 3.77 ELEPHANT 3.36 Goat 3.78 CAMEL | 3.37 Hu-coar 3.79 Hunt (vb.) 3.38 Kip 3.81 InsEctT 3.41 Horse (Generic) 3.82 BEE 3.42 Srantion 3.83 Fy : 3.43 GrLpine 3.84 Worm 344 Mare 3.85 SNAKE
```


## [2026-09-05T20:39:37.782Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"aspa-\" SYN.txt | cut -c1-500 | head -6"
}
```


### [2026-09-05T20:39:37.858Z] TOOL RESULT

```
4524:ANIMALS 167 3.41 3.42 3.43 3.44 3.45 HORSE STALLION GELDING MARE FOAL, ae, tarros 6, dxetov tarmos exrepvd- trmos 7) aos Grk. pevos . BapBaro adoyo, tite  GAoyo povvouxt- dopdéa movhape NG adoyo opéevo wus (equus) admissa- cantérius equa pullus (eculus) Lat. & us avallo stallone cavallo castrato cavalla puledro It. Feil étalon hongre jument poulain aay caballo caballo padre caballo castrado equa polro Be, eal armésar jugan tapa minz I ech, mare (capall) (ech-)cullach gerran lair serrac
4532:aspa- (OPers. also asa-); Toch. A yuk, B yakwe.
4552:8. Skt. agva-, Av. aspa-, above, 1. Skt. haya- : hi- ‘set in motion, impel’. Walde-P. 1.546.
4599:3.44. ‘Mare’. 1. Expressed by fem. forms of word discussed under ‘horse’ (3.41), as Grk. 4 immos, Lat. equa (> OFr. ive, Sp. yegua, Rum. iapd), It. cavalla, ON merr, OF mere, etc., Skt. agua-, Av. aspa-.
28531:Grk.  daxpu Goth. tagr Lith. aSara NG daxpu ON lar Lett. asara Lat. lacrima Dan.  aare ChSl. _ sliza It. lacrima Sw. tdr SCr. — suza Ir. larme OE téar, teagor Boh. © slza Sp. ldgrima ME tere Pol. iza Rum.  lacrimdé NE tear Russ. — sleza Tr. dér Du. traan Skt. acru-, baspa- Nir. deor OHG zahar, trahan Av. asru- W. deigryn MHG zaher, trahen
28538:3. Skt. baspa- (also ‘steam’), prob:
```


## [2026-09-05T20:39:44.724Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4525,4535p' SYN.txt | cut -c1-600\necho \"=== ARY ===\"; grep -n -m4 \"EKWOS\\|ekwos\" incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200\ngrep -n -m4 \"اسب\" incoming/ARY/ARY_pages.txt | cut -c1-200"
}
```


### [2026-09-05T20:39:44.794Z] TOOL RESULT

```
the IE languages pointing to an IE word for ‘horse’ and its great frequency in Personal names do not prove the IE domestication of the horse (cf. the simi- lar situation for ‘wolf’), there is strong Pe ey on other grounds that the orse was at least partially domesticated n the If period, and further that the ae the horse for drawing war chariots eee came to western Asia and see seueh the medium of IE-speak- a Oples of Asia Minor. Schrader, &x, 2.170 ff. For Celtic cf. also
43.113 ff.
1. IE *ekwo-, root connection wholly obscure. Walde-P. 1.113. Ernout-M. 307. Grk. tos, dial. also ixxos (but with
some unexplained phonetic features and taken as an Illyr. loanword by Kretsch- mer, Glotta 22.120); Lat. equus (with fem. equa ‘mare’); Ir. ech, Gall. *epo- in names Eporedia, etc. (W. ebol, Br. ebeul ‘colt?); ON jor (poet.), OK eoh ‘war- horse’ (Goth. aihwa-tundi ‘bramble bush’, lit. ‘horse-tooth’); Lith. (obs.) esva, asva ‘mare’; Skt. agva-, Av., OPers.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
168 SELECTED INDO-EUROPEAN SYNONYMS
aspa- (OPers. also asa-); Toch. A yuk, B yakwe.
Thus the word is attested in all the main branches of the IE family except Slavic, and it is still that in use in most of the modern Iranian languages (N Pers. asp, etc.). But in all the European lan- guages it has sooner or later been dis- placed by other terms (but cf. Sp. yegua, Rum. zapdé ‘mare’). Likewise in the Indie vernaculars, mostly by forms an- swering to the late and obscure ghota-, ghotaka-, on which cf. Sommer, IF 31.363 ff.
2. NG adoyo, fr. neuter of Gri. &oyos ‘unreasoning’, not with primary applica- tion to the horse, to which it would be relatively inappropriate, but through the medium of ‘animal’ (so ra &\oya. ‘ani- mals’ in Plato, etc.) with specialization starting in military parlance, in which one commonly coupled 4av@pwro and adoya ‘men and beasts’, that is, ‘men and horses’. Hatzidakis, Meo. 1.142.
Byz. ¢apas, dapiov, MHG varis, etc., rather widespread medieval word for ‘horse, steed’, fr. Arab. faris ‘rider’. Lokotsch 591. Berneker 279.
=== ARY ===
162:دارای ارابه و اسب پودند» تحرکك آنها از کشاورزان روستانشین بیشتر بود و در ناحیه‌ی وسیع‌تری
165:علاوه‌ی مجهز بودن به اسب و ارابه و سلاح‌ها و ترفندهای رزمی پیشرفته و دارا بودن خصلت
180:و اسب‌سواران ماهری پودند. این مردم در طی هفت قرن (از سده‌ی ششم تا سیزدهم پس از میلاد) طی
290:کشاورزی شده است. چون واژه‌های «اسب» و «ارابه؛ و «چرخ» در اکثر زبانهای هند و اروپایی
```


## [2026-09-05T20:39:58.595Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 334 335 336; do echo \"=== LEAF $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | grep -n \"استر\\|اسپست\\|سپست\" | head -6; done\necho \"=== find استر leaf ===\"; awk 'BEGIN{RS=\"\\f\"} /استر[ ،:؛]/ {print \"LEAF=\"NR-1}' BQT_v1_pages.txt | head -20"
}
```


### [2026-09-05T20:40:00.513Z] TOOL RESULT

```
=== LEAF 334 ===
=== LEAF 335 ===
=== LEAF 336 ===
=== find استر leaf ===
LEAF=97
LEAF=216
LEAF=232
LEAF=254
LEAF=268
LEAF=270
LEAF=275
LEAF=320
LEAF=337
LEAF=339
LEAF=340
LEAF=341
LEAF=353
LEAF=378
LEAF=389
LEAF=463
LEAF=484
LEAF=510
LEAF=557
LEAF=603
```


## [2026-09-05T20:40:03.121Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==338' BQT_v1_pages.txt | grep -n -B2 -A4 \"استر\" | head -40"
}
```


### [2026-09-05T20:40:04.981Z] TOOL RESULT

```
8-و ممثی اسیغول است که بزر فطونا باشد .
9-است » بفتح اول و سکون تانی و ای
10:فرشت ۰ مضفف استر باشد که از دواب مشهوره
11-است. کوند ازجملة صرفات فرعون است ۱ -
12-و استخوان آدمی و ساير حیوانات ۴ - و تشم
13-ودانهٌ میوه‌ها را نیز گویند؟ - و تضیر کتاب زئد
14-و پاژند (۱) هم‌هست که‌آنرا استا نیز خوانند »
--
23-بالف کشده شیر کتاب زند (۷) است و آن
24-(۱) چك
25:۱ - رگ : استر
26-۴ رك : اوستا
27-۱ رگ : اوستا..
28-: ژند ویاژند .
29-۲ - ره :
--
42-کلیه و جزلیه را دز استاد کودند . ۶
43-استاد باك » بکر اول.نم‌شهریانت
44:در طبرستان مشهور باسترآباد *۷.
45-استاده ه بکر اول ممروف است که
46-متاره و ک و کب باشد- و شامیانه و سایبان راهم
47-گفته اند - و مسطر فولادی و چوب جدول
48-کشانرا نیز گوبند - و بمعنی طنبور سه تار هم
--
54-۸ - ره : زند
55-پازند 01 « باروج ۹4
56:استان . 9۰ - رگ : استرآباد .
57-فرمنگی لامیجان برصر راه رشت
58-۶ اشت: ی«
59-و
60-- بونانی قآلاناها٩‏ ( دانهٌ انگور )
```


## [2026-09-05T20:40:14.099Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==337' BQT_v1_pages.txt | head -40"
}
```


### [2026-09-05T20:40:17.126Z] TOOL RESULT

```
ابجد و ظهور های هوز ؛ مخفف اسباه است که
لشکر و سپاه باشد - و سگه را ليز کوشد که
بتازی کلب خوانند» وبا پای‌فارسی هم گفته‌اندا .
اسبهان » سر وزن و مصنی اصفهان
است, وآن شهری باشد داراللطنه در ملك‌عراق
و با بای فارسی هم آهده است » و آن شهر رادد
قدیم دارالیهود ی گنتندی ء گوشد دجال ازآنسا
خروج کند .و ابتدای قحط عالم از آخجا شود »
وه رکه چهل روز درآن شهرباشد بخیل ومسك
شود - و جمم سیاه یز هست - و چنم‌سگم
کفته اند که بازی کلب خوانند , چه در دتاب
معجم‌البلدان در صحیح نام اصفهان کفته اند نه
«لاصبهان ۴ اس‌مشتق من الجندية و ذلكان‌لنظ
اسبهان اذا رد الی اسمه بالفارسية کان ا-باهان
و هی جمم اسباه و اسباه اسم للجند والخنل ۴
وبشفت‌فیقال‌اسبه ۴ وجمعه‌بالفارسية اسبهان6 .»
۱ رك : اسباه و سیاه
0
است مخصوص ملول طبرستان ۷ - و بنعنی سپه
سالاز هم آهده است که‌سردار و خداوند (ثکر
باشد چه بد بمعنی خداوند و صاحب و اسپه
سیاه ولشکر بود » و نم بای‌ابجد هم گفته اند
و محرب آن اخفییه لست .
آسهید خو ده » بنتح خای قطمدار
و رای بی نقطه و واو معدولهٌ ماکن ۰ اشرافیان
فاری نفی تاطفه را کون دکه ا وت متعنیة
انانی انت ۷ .۵
اسبیچاب » با تتای مجهول و جبم
فارسی‌بر وزن استیعاب , نام شهری است
ماوراء النپر که آنرا بترکی شبران بنر وزن
۱ ۱
آسییل # . تسه کیت که فش
سیاه باشد - و بمعنی بی نقش و بی‌لون هم‌آهده
است . 4۶
آسیید‌دو ۵ « دم رودخانه است اژ
آذربایجان که بدیلمان و گیلان گنرد .
ت ازولات
۴ - ممجم‌البلدان ( این ) : فعلی هذا جمعوا
۰۵ ۱3۲ 9 ۹۸+
رك: سکه شناسی‌طبرستان. اونوالا ۰۳۹-۷۸
```


## [2026-09-05T20:40:28.553Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 331 332; do echo \"=== LEAF $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -45; done"
}
```


### [2026-09-05T20:40:30.219Z] TOOL RESULT

```
=== LEAF 331 ===
فآ فا برگه زرد چوبه است -
ودرخت خربزه را نیز گوبند .
اسیر لو س « بالام وسین بی‌نقطه ووار
مجپول بروزن کشورسوز » خانه وسرای پادشاحان
و سلاطین و حکام را کوبند .
اسیر 8 - بکسر اول و فتح ثالث ورابم
و سکون ثانی و میم » بمعنی اول اسپرغم است
که مطلق کلها و رباحین باشد ۱ .
اسر ۵] لب « دارو های پآب‌جوشانیده
باشد که بدن بیمارانرا بدان پشویند و بعربی
نطول خوانند .
اسیر نگ » بر وزن ومعنی اسفریگه
است ؛ و آن شهرست ترديك سمرفند و مولد
سف لجاست .
اسپر ود - بکس اول و شم الث
ورابع و سکون ثالی و واو مجهول و زای هوز »
تلم کوهیست بسیار بلند و رفیم» و ختح ثالث‌هم
کفتفانن ۳
اسر هم ۴ ه باهای‌هوز, بروزن ومعنی
اول اسپرغم است که مطلق کلها و رباحین باشد.
آسپر ی « بر وزن‌مهتری » بمعنیپست
۱ رك : اسپرهم .
اسیغول
شده و معدوم کردیده وآخرشده وبنهایترسیده
باشد - وبمعنی تمام شدن وباأخر رسیدن ونیست
گردانیدن - وصور کردن عم آمده است .
اسیر یز فتح اون و سکون تحتانی
مجهول بر وزن رم خیز » بمعتیاسب ری‌است
که میدان و سا و عرصه باشد ۳ تس اول
مم آمده است ؟ .
اسب د لسي - باسین بی‌هطه » بروزن
۲
دوالیدن باشد6 ؛ وبکسر اول همهست وسین‌دوم
قطبدارهم ۳ است وبا کیش قافیه کرده اند .
اسیست ۱ ب بفتح اول و کسر الث
وسکون »نی وسن‌سفنص
وئای قرشت» صیست را
کوندو آن علفی است
خوانتد و سریی ضصفصه
و تخم آنرا بدرالرطبه
گویند . اسیت
اسپقول - بکسر اول وفتح الث» بزد
۹۰
۴ ب ورگ : اسپرجس-.
بیعنی راه » اسپریس ا: کلمات فارسی است که سین پهلوی بجا مانده ؛ اسپرس بتصریح مضر
=== LEAF 332 ===
قطونا باشد ۷ » و معنی ت رکیبی آن گوش اسب ۱
است ۰ چه غول بدمنی کوش هم آعده است ؛
وجط یکونند چون ب رکه آن بگوش اسب‌شبه
و معنی اسفناج است »
و آن سبزی باش د که در
آش و هله کنند , سرفه
است‌بنابرین اسب‌غول خوانند و بضی بشپش‌تشبیه | دا نافع ات (,
کرده اند , و جتح اول هم درست است . اسینانج .
باجیم مر وزن اصفهانك »
بمعنی اسفناح ننک 5
سبزی آش باشد ۴ . اسیناخ ( اسپناج )
ا سید ه معروفاست و (۲) آن دانه‌ای
باشد که بجپت چشم زخم در آش ریزند ۵ .
اسیندار بمعنی شمح باشد که معشوق
اسیلفج « بنتم اول و م لام و سکون ‏
ثانی و ثالث و نون و جیم ۴ کیاهی است (۱)
دوابی که آنرا صفاهان شنك و در خراسان‌رش
یزخال دار و بعرمی لحیةالنیس خوانند . طبیعت
آن سرد و خشك است » خون بینی و جمم‌اعضا
ببندد و ربهای کهنه را نافم باشد و فرحه
اععارا سود دارد » و آذناب‌النیل همان است . 4
پروانه است - و نام پکشناسب هم هست ٩‏
اسناخ ۴ باخای نقطه دار 1 بروزن
-ء بودن لیراعظم باشد دربرج حوت و 5
(۱) چك : - است . (۲) چش : کد.
لِ - جهانگری بمعنی پبخال آورده ۰ دلیلی ندارد چه در قدیم توبن فرهتگها مانند
حلشة قرهنگه اسدی تخجواتی بمعنی بزرقطونا ضبط کر‌ده‌اند واين شمریهرامی را شاهد! وردماند:
هیجگاه نارم بخانه کرد مقام ازانکه خانه پراز اسیغول جانور است .
واسیخول در شمرمذ کور بی‌شك بمعنی ماس است . « لفت‌نامه > -
۴ حکیم مومن وصاحب مخزن‌الادوبه « املنج > آورده اند . « لفت‌نامه » .
؟ - بلت‌علمی 50102012 بانگلی 5۳18260 با 50101286, بفرانسه 60102۲05
با لمانی01024کوعربی اسفاناخ» وفارسی‌اسیناخ»اسیناج» اسینانج,اسپاناج.اسپانج» اسباناج» اسباناخ‌ودد
طبری اسینا «واژه نامه۲۸> حمه‌ازيك ربشه است. داودشرسر انطا کی‌درتذ کرخود گوید : اسفاناج
مرب عن‌فارسية هواسباناح * ۰ دربونانی 5۳1081108 « اختینگاس » وآن از تیر* اسفناجیان ؛
ودارای ربشة قرمز دنگ وب رگهای خوراکی و کلهای نرومادء آن جداست . « کل گلاب4 ۰*۲۷
ی فرحنگه روستایی ۱۸-۱۸۳ > . ۴ راد : اسیناج ۱ ۵ در اوستا ٩۳۵1۵‏
بمعتی مقدس < بارتولمه۱۹۱۹ > ۰ طبری 65۳021 « واژه‌نامه ۷۷ ۰۲ کیلکی ٩۳20-4202‏ ,
قظرسی نیز اسفند . 18۱98 112۲۳0812 این گیاء در اغل نفاط ابران خود روست . «فرهنگه
روستابی۱۸4 * . ۱ ره : اسیندبار. ۷ ر4: امیندارمة .
خبه از صفحة ۱۱4۹
پورداود . بقما ۲ : ۱۲ * پهلوی 25۳25 « اونوالا ۲۸۰ > .
۵ اسبله - با سیلی 212015 51۷0۲135 از ماهیان
استخواندار که بچةٌ ماهیان پربهارا میخورد واز همین نظر ماهی
مسیارمضری‌است وقسمت عمده زند گانیرا در کودالهای‌رودخانه‌ها
سرسبرد ۵ ددیای خزد 64۱۳۳ اسله
```


## [2026-09-05T20:40:47.977Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==332' BQT_v1_pages.txt | tail -25\necho \"=== 333 footnote continuation ===\"; awk 'BEGIN{RS=\"\\f\"} NR==333' BQT_v1_pages.txt | grep -n \"۱۱۹\\|سریانی\\|aspast\\|pespest\" "
}
```


### [2026-09-05T20:40:49.777Z] TOOL RESULT

```
که میدان و سا و عرصه باشد ۳ تس اول
مم آمده است ؟ .
اسب د لسي - باسین بی‌هطه » بروزن
۲
دوالیدن باشد6 ؛ وبکسر اول همهست وسین‌دوم
قطبدارهم ۳ است وبا کیش قافیه کرده اند .
اسیست ۱ ب بفتح اول و کسر الث
وسکون »نی وسن‌سفنص
وئای قرشت» صیست را
کوندو آن علفی است
خوانتد و سریی ضصفصه
و تخم آنرا بدرالرطبه
گویند . اسیت
اسپقول - بکسر اول وفتح الث» بزد
۹۰
۴ ب ورگ : اسپرجس-.
بیعنی راه » اسپریس ا: کلمات فارسی است که سین پهلوی بجا مانده ؛ اسپرس بتصریح مضر
اوسنا در زمان ساسانیان ونامةٌ پهلوی بندهش, میدان ناخت ونازاسب » بدرازای دوهزار کلم است.
د ذاب ۰ ۱ : ۲۷۵-۷۲6 > . ۱ - در اوستا ویارسی باسنان 254 - 25۳0 » ای کلم
م رکب لفظاً یمنی « اسب میخورد * , جزه اول همان اسب است وجزه دوم از مصدر 24 مطایق
0 لانینی و655650 آلمانی و 6۵ (10) انکلیسی است بمعنی خوردن ( چنانکه رد اوستابی
ربثة آراستن وراست فارسی است ) . درپپلوی نیز 25۳356 آعده » از زبان یپلوی داخل‌سربانی
وازسربانی بعربی‌رفته « فصفصه » (جمم. فصافص) شد. وازعربی دراسپانیابی وارد شده صورت‌الفلفه
8 هه اسپانیولیانآنرا بآمبکا بردند و درآن سرزمین نیز الفلفه خوانند . «بونجه (اسیست)
بقیه درصفحة ۱۲۰
=== 333 footnote continuation ===
```


## [2026-09-05T20:41:55.904Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Gushnasp ===\"; grep -n -o -E \".{0,300}(stallion|Gušnasp|meaning).{0,200}\" bac3b8cddc480f2e.txt | head -5\necho \"=== Arjasp iranica ===\"; grep -n -o -E \".{0,200}(Arəǰa|Arjāsp|Av\\.).{0,250}\" 9e8c329beb9254b1.txt | head -5"
}
```


### [2026-09-05T20:42:01.787Z] TOOL RESULT

```
=== Gushnasp ===
ugrep: error: error at position 105
meaning)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                exceeds complexity limits___/


=== Arjasp iranica ===
ugrep: error: error at position 100
\.)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,250}
           exceeds complexity limits___/
```


## [2026-09-05T20:42:05.340Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Gushnasp ===\"; grep -n -i \"stallion\\|gušnasp\\|male horse\" bac3b8cddc480f2e.txt | cut -c1-300 | head -6\necho \"=== Arjasp ===\"; grep -n -i \"Arəǰa\\|arejat\\|Avestan\\|Hyaona\" 9e8c329beb9254b1.txt | cut -c1-400 | head -6"
}
```


### [2026-09-05T20:42:05.404Z] TOOL RESULT

```
=== Gushnasp ===
=== Arjasp ===
57: ARJĀSP (Av. Arəǰaṱ.aspa), a chief of the Iranian tribe of the Xyōns (Av. Hyaona-), and an enemy of Kay Goštāsp (Kavi Vištāspa), patron of Zoroaster ( Yašt 9.30, 5.109). In the later tradition he is represented as a king of Tūrān and the son of Šavāsp, brother of Afrāsīāb (Ṭabarī, II, pp. 617, 677), or according to Moǰmal (p. 51) as Afrāsīāb’s grandson, or according t
```


## [2026-09-05T20:42:08.839Z] AGENT

Now I have enough evidence. Writing the verification file.


## [2026-09-05T20:42:11.468Z] TOOL CALL #85: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg151.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/151.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T20:42:11.534Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T20:44:27.260Z] TOOL CALL #86: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151a.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁éḱwos\"\nW_ASB   = \"https://en.wiktionary.org/wiki/اسب\"\nW_SAVAR = \"https://en.wiktionary.org/wiki/سوار\"\nW_ASTAR = \"https://en.wiktionary.org/wiki/استر\"\nW_ASPAST= \"https://en.wiktionary.org/wiki/اسپست\"\nW_FISFIS= \"https://en.wiktionary.org/wiki/فصفص\"\nW_FISFISA=\"https://en.wiktionary.org/wiki/فصفصة\"\nW_HIPPOS= \"https://en.wiktionary.org/wiki/ἵππος\"\nW_GOSHT = \"https://en.wiktionary.org/wiki/گشتاسپ\"\nE_ALF   = \"https://www.etymonline.com/word/alfalfa\"\nE_PHIL  = \"https://www.etymonline.com/word/Philip\"\nE_HIPPO = \"https://www.etymonline.com/word/hippopotamus\"\nAHD_ALF = \"https://www.ahdictionary.com/word/search.html?q=alfalfa\"\nIR_NAMES= \"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/\"\nIR_ARJ  = \"https://www.iranicaonline.org/articles/arjasp\"\nWP_JAM  = \"https://en.wikipedia.org/wiki/Jamaspa\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"aspa; aspa-bâra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. aspa- 'horse' is the direct Iranian continuant of PIE *h₁éḱwos: the palatal *ḱ gives Proto-Iranian *ć, and the cluster *ćw yields Avestan/Median sp (Old Persian s), so *h₁eḱwo- > PIr. *Hácwah > Av. aspa-, OP asa-; Kent §90 states the rule verbatim ('pIE *eḱuo- \\\"horse\\\", OP asa- ... OP aspa- (with Med. sp) in Vistaspa-; Av. aspa-, Skt. aśva, Lt. equos'). Bartholomae's dictionary has aspa- and dozens of compounds in -aspa-. The second word is the weak point: the attested form is Old Persian asa-bāra- 'horseman' (DB 2.2 asabaraibiš), not an Avestan *aspa-bāra-; Avestan uses aspa- in compounds but the 'rider' word is Old Persian/Median, built on the byform asa- + -bāra- from PIE *bher- 'to carry' (Nourai's ☞Bher 1 is right). The literal sense is 'borne by a horse' rather than 'horse load'.\",\n \"derivation_fa\": \"اوستایی aspa- «اسب» بازماندهٔ مستقیم هندواروپایی آغازین *h₁éḱwos است: کام‌واکِ *ḱ در ایرانی به *ć بدل شده و خوشهٔ *ćw در اوستایی و مادی به sp و در پارسی باستان به s تبدیل شده است (aspa- در برابر asa-)؛ کِنت (بند ۹۰) همین قاعده را می‌آورد. امّا جزء دوم، «aspa-bāra»، در اوستا گواهی نشده؛ صورت گواهی‌شده پارسی باستان asa-bāra- «اسب‌سوار» است (سنگ‌نبشتهٔ بیستون) که از صورت فرعی asa- به علاوهٔ -bāra- از ریشهٔ *bher- «بردن» ساخته شده. پس ادعای نورایی دربارهٔ aspa درست است ولی برچسب زبانیِ aspa-bāra باید «پارسی باستان» می‌بود.\",\n \"sources\": [W_PIE, W_ASB],\n \"ref_check\": [\n  {\"ref\":\"POK:301\",\"status\":\"supports\",\"note\":\"Pokorny IEW 301-302, lemma 'eḱuo-s, Meaning: horse': 'Old Indie aśva-h, Avestan aspa-, Old pers. asa- \\\"horse\\\"' (local POK_full.txt line 25047 ff., 'Page(s): 301-302').\"},\n  {\"ref\":\"DVS:42\",\"status\":\"not_checked\",\"note\":\"P. Davies, Roots: Family Histories of Familiar Words (1981) is lending-only on archive.org (refs_online.json kind=archive_restricted); no copy accessible.\"},\n  {\"ref\":\"BQT:1819\",\"status\":\"not_found\",\"note\":\"Borhān-e Qāṭeʿ printed p.1819 (vol.3 pdf p.616, rendered with tools/ref_page.py BQT:1819) is the گشتاسب/گشاده entry, with Moʿin's footnote 11 on Vištāspa; it contains nothing on aspa 'horse' or on aspa-bāra. The page is relevant to nodes #4-#5, not to this box.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BRT\",\"where\":\"Altiranisches Wb., aspa- and its compounds (BRT.txt: aurušaspa-, arəǰaṱ.aspa-, aurvat.aspa-, pouru.aspa-, hazaŋrō.aspa- etc.)\",\"stance\":\"supports\",\"note\":\"Bartholomae has aspa- 'Ross/Pferd' throughout and a long series of possessive compounds in -aspa-, e.g. '• j. ʼaurvataspa- Adj. \\\"der schnelle Rosse hat\\\"'; there is no headword aspa-bāra-.\"},\n  {\"src\":\"KNT\",\"where\":\"Old Persian §90 and Lexicon s.v. asa-, asabāra-\",\"stance\":\"partial\",\"note\":\"'pIE *eḱuo- \\\"horse\\\", OP asa- in acc. asam and in asabāra-; OP aspa- (with Med. sp) in uvaspa-, Aspacanah-, Vistaspa-; Av. aspa-, Skt. aśva, Lt. equos' and 'uvāsabāra \\\"good horseman\\\" (*hv-āsa-), to asa- \\\"horse\\\"' — the rider word is Old Persian, not Avestan.\"},\n  {\"src\":\"SYN\",\"where\":\"Buck 3.41 'Horse'\",\"stance\":\"supports\",\"note\":\"'1. IE *ekwo-, root connection wholly obscure. Walde-P. 1.113 ... Skt. aśva-, Av., OPers. aspa- (OPers. also asa-); Toch. A yuk, B yakwe.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"asp; asbâr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary p.13 has 'asp [SWSYA; sb | N ~] horse' (the Aramaic heterogram SWSYA masks the Iranian word) and p.14 'aswār [ʾswbʾl, ʾshwʾl | N suwār] horseman, rider; ~īh horsemanship'. Book Pahlavi ʾswbʾl is read both aswār and asbār — the -bār/-wār fluctuation is the ordinary Middle Persian lenition of intervocalic -b- to -w-, so Nourai's 'asbâr' is a legitimate reading of the same word. Both continue Old Iranian *asa-bāra- with regular loss of the final -a and of the compositional vowel.\",\n \"derivation_fa\": \"در فارسی میانه asp «اسب» (مکنزی، ص ۱۳، با هزوارش SWSYA) و aswār/asbār «سوار، اسب‌سوار» (نوشتهٔ ʾswbʾl) آمده است؛ نوسان میان b و w همان نرم‌شدن ب میان دو واکه در فارسی میانه است، پس ضبط «asbâr» نورایی درست است. هر دو از *asa-bāra- ایرانی باستان‌اند با افتادن واکهٔ پایانی. ادعای نورایی درست است.\",\n \"sources\": [W_SAVAR],\n \"ref_check\": [\n  {\"ref\":\"BQT:119\",\"status\":\"supports\",\"note\":\"Borhān-e Qāṭeʿ printed p.119 = BQT_v1_pages.txt leaf 331 (the اسپست entry); Moʿin's footnote there ends '... در پهلوی نیز aspast آمده، از زبان پهلوی داخل سریانی و از سریانی به عربی رفته «فصفصه» ... و از عربی در اسپانیایی وارد شده صورت الفلفه' — the page indeed carries Moʿin's Pahlavi material for this box (asp/aspast).\"}\n ],\n \"consulted\": [\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.13-14 (PHD.txt lines 219, 221)\",\"stance\":\"supports\",\"note\":\"'asp [SWSYA ...| N ~] horse' ; 'aswār [ʾswbʾl, ʾshwʾl | N suwār] horseman, rider. ~īh: horsemanship, riding.'\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (Glossary) s.v. asp (NYB_vol2_glossary.txt line 695)\",\"stance\":\"supports\",\"note\":\"'asp [ʾsp\\\\'; SWSYA] horse 4² etc., passim; pl. cas. obl. -ān ... = Av. (216 sq.) aspa- = OP, Skr.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"asb «اسب»; savâr «سوار»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP اسب asb continues MP asp unchanged but for the late orthographic/phonetic b for p (classical and Dari still asp; the spelling اسب is the modern Iranian norm, اسپ the older one). NP سوار savār is MP aswār with loss of the initial unstressed a- (aphaeresis) — Hübschmann §, 'mit Ausfall des p: suvār \\\"Reiter\\\" = ap. asabāra-', i.e. OP asabāra- > MP aswār > NP suwār/savār; the word is thus a doublet-free direct descendant, and the Persian phrase اسب‌سوار is a later recompounding. Wiktionary gives the same chain (اسب < MP asp < OP aspa/Median *aspah; سوار < MP ʾswbʾl aswār).\",\n \"derivation_fa\": \"«اسب» دنبالهٔ مستقیم asp فارسی میانه است؛ املای قدیمی‌تر «اسپ» بوده و ب پایانی از تحول متأخر خطّ و آواست. «سوار» از aswār فارسی میانه است با افتادن الفِ آغازین (aswār > suwār > savār)؛ هوبشمان همین را می‌گوید: «با افتادن p: suvār «سوار» = پارسی باستان asabāra-». پس هر دو واژه درست‌اند و ادعای نورایی تأیید می‌شود.\",\n \"sources\": [W_ASB, W_SAVAR],\n \"ref_check\": [\n  {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"Moʿin's Farhang (2-vol condensation, MON_part1.txt) has اسب as the ordinary word for 'horse' and استر '[= ستر؛ مربوط به اسب قس. قاطر] (جان.) قاطر' under the same root family; no page is given by Nourai so only the lemma could be checked.\"},\n  {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"Borhān-e Qāṭeʿ vol.1 leaf 329 (printed ~p.117) 'اسب ... بفتح اول معروف است و بعربی فرس خوانند' — the horse word, with the آسپ variant beside it.\"}\n ],\n \"consulted\": [\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss no. 77 (p.19)\",\"stance\":\"supports\",\"note\":\"'77. esp, esb \\\"Pferd\\\". ap. Aspa[cana-, uv]aspa- ; aw. aspa- \\\"Pferd\\\"; phlv. asp; ai. aśva- ... ap. asa[bāra-] und np. es[t]er (No. 86) stützen sich gegenseitig und scheinen eine Nebenform asa- zu beweisen.'\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien §71 and §on p-loss (HUB.txt lines 6288, 7560)\",\"stance\":\"supports\",\"note\":\"'asp \\\"Pferd\\\" = zd. aspa-, dazu aspist \\\"Luzerne\\\" H.79' and 'mit Ausfall des p: suvār \\\"Reiter\\\" = ap. asabāra-'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\",\n \"words\": \"tum-âspa; keresa-aspa; višta-aspa; baevare-aspa\",\n \"verdict\": \"disputed\",\n \"derivation\": \"All four are possessive (bahuvrīhi) compounds whose second member is aspa-, so the arrow from the root is right; two of the four glosses are not what the sources say. (1) tum-āspa: Pokorny p.1082 under *teu- 'to swell; fat; strong' does list 'Avestan *tuma- in Tumaspana- from Tumaspa- (i.e. one whose horses are fat)', and Bartholomae has 'tumāspana- patr. Adj. \\\"von Tumāspa stammend\\\"' (Yt.13.131) — so the Avestan name is real, but its sense is 'having fat/plump horses', and Schmitt's Iranica survey lists *Tūmāspa- only through the patronymic Tūmāspāna-. (2) kərəsāspa- is confirmed: Iranica, 'Kərəsāspa- (no. 216) \\\"Possessing slender horses\\\"'. (3) vīštāspa- is confirmed as a word, but modern onomastics glosses it 'possessing horses untied (for racing)' (Iranica no. 379, an old Aryan horse-racing term, vi- + šta- from stā-); Moʿin (Borhān p.1819, after Bartholomae col.1467) reads 'دارندهٔ اسب از کار افتاده' = 'whose horses are spent', which is Nourai's 'old horses'; nobody supports 'gray'. (4) baēvarə- '10,000' is Avestan (Bartholomae, with baēvarə.patay-, baēvarə.spasan- etc.), but there is no Avestan headword baēvarə.aspa-; the compound bēwar-asp is a Middle Persian epithet of Dahāg, so the box's language label is one stage too early.\",\n \"derivation_fa\": \"هر چهار واژه ترکیب دارندگی (بهوریهی) با جزء دوم aspa هستند، پس پیوند آنها با ریشه درست است؛ ولی دو معنی نادرست است. پوکورنی (ص ۱۰۸۲، ذیل *teu- «آماسیدن، فربه، نیرومند») صورت اوستایی *Tūmāspa- را از راه نام پدرسالاری Tūmāspāna- می‌آورد و آن را «دارندهٔ اسبان فربه» معنی می‌کند؛ بارتولمه هم tumāspana- را دارد. Kərəsāspa- «دارندهٔ اسبان لاغر» است (ایرانیکا). امّا Vīštāspa- را ریشه‌شناسی امروزی «دارندهٔ اسبان رهاشده (برای مسابقه)» می‌داند و معین در حاشیهٔ برهان (ص ۱۸۱۹، به پیروی بارتولمه ستون ۱۴۶۷) «دارندهٔ اسب از کار افتاده» می‌آورد؛ معنی «خاکستری» هیچ پشتوانه‌ای ندارد. سرانجام baēvarə «ده‌هزار» اوستایی است ولی ترکیب baēvarə.aspa- در فرهنگ بارتولمه نیامده و «بیوراسپ» لقب پهلوی ضحّاک است، نه واژه‌ای اوستایی.\",\n \"sources\": [IR_NAMES, W_GOSHT],\n \"ref_check\": [\n  {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"Borhān p.1819 (vol.3, ref_page.py BQT:1819) footnote 11: 'در اوستا و پارسی باستان Vištāspa (در یونانی Hystaspes)، مرکب از دو جزء: višta بمعنی از کار افتاده ... و جزء دوم aspa همان اسب است، جمعاً یعنی دارندهٔ اسبِ از کار افتاده. بارتولمه ۱۴۶۷' — supports 'old' but not 'gray'.\"},\n  {\"ref\":\"POK:1082\",\"status\":\"supports\",\"note\":\"Pokorny, root *teu- 'to swell; crowd; fat; strong', pp.1080-1085; in the m-derivatives section: 'Avestan *tuma- in Tumaspana- from Tumaspa- (that is to say, one whose horses are fat)'. Exactly the source of Nourai's tum-âspa and of the ☞Těu cross-reference.\"},\n  {\"ref\":\"KNT\",\"status\":\"partial\",\"note\":\"Kent gives Vištāspa- (OP 𐎻𐏁𐎫𐎠𐎿𐎱, 'Hystaspes, father of Darius') and §90 'OP aspa- (with Med. sp) in ... Vistaspa-', but offers no gloss for the first element and none of the other three names.\"},\n  {\"ref\":\"HRN:206\",\"status\":\"not_found\",\"note\":\"Horn's printed p.206 (HRN.txt \\\\f-leaf 228) contains nos. 924-927 (gusuftan, gušn, guftan, gul); it bears on Gušnasp (node #7), not on any name of this box.\"},\n  {\"ref\":\"AEF:324\",\"status\":\"not_checked\",\"note\":\"Ḵāleqi Moṭlaq's Asās-e Eštteqāq-e Fārsi (the Persian version of Horn+Hübschmann) is catalogue-only in refs_online.json; no scan available.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BRT\",\"where\":\"Bartholomae, Altiran. Wb. s.vv. tumāspana-, baēvar-/baēvarə- compounds, aurvat.aspa- (BRT.txt lines 12327, 16470-16490)\",\"stance\":\"partial\",\"note\":\"'• j. tumāspana- patr. Adj. \\\"von Tumāspa stammend, dessen Nachkomme\\\": Yt.13.131'; the baēvarə- article lists baēvarə.patay-, .fraskəmba-, .miθta-, .vaēδayana-, .vār-, .spasan- but NO baēvarə.aspa-.\"},\n  {\"src\":\"POK\",\"where\":\"IEW 1080-1085 (*teu-) and 301-302 (eḱuo-s)\",\"stance\":\"supports\",\"note\":\"see ref_check; both cited pages carry exactly the material Nourai draws.\"},\n  {\"src\":\"web/Iranica\",\"where\":\"Personal Names, Iranian ii: Avestan Names (Schmitt)\",\"stance\":\"partial\",\"note\":\"'Kərəsāspa- (no. 216) \\\"Possessing slender horses\\\", Vīštāspa- (no. 379) \\\"Possessing horses untied (for racing)\\\" (based on an ancient technical term of Aryan horse-racing)' and, in the patronymics list, 'Tūmāsp-āna- from *Tūmāspa-'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"Tahmâsb «تهماسب»; Garšâsp «گرشاسپ»; Goštâsp «گشتاسپ»; Bîvarasp «بیوراسپ»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Three of the four are textbook: Garšāsp < MP Kirsāsp < Av. Kərəsāspa- 'having slender horses' (Iranica no. 216; the Av. cluster rəs > NP rš/rs and final -a is lost); Goštāsp < MP Guštāsp < OP Vištāspa (itself the Median/Avestan Vīštāspa-), Wiktionary s.v. گشتاسپ giving exactly 'MP gwštsp < OP vi-š-t-a-s-p < Av. vištāspa', with the regular NP shift wi- > gu- (as in wišān > گشن, Av. vəhrka- > گرگ); Bīvarasp is the epithet of Żaḥḥāk/Dahāg, MP Dahāg ī bēwarasp 'having 10,000 horses', bēwar 'myriad' being Nyberg's 'bēvar [bywl] ten thousand'. The first name is the problem: Tahmāsb is standardly Av. Taxma-aspa- 'having brave/strong horses' (Av. taxma- 'brave, courageous', Iranica no. 304; MP Tahmāsp with xm > hm), not Pokorny's *Tūmāspa- 'having fat horses', which survives only in the patronymic Tūmāspāna- and is not continued in Persian. Nourai has crossed two homophonous-looking Avestan names.\",\n \"derivation_fa\": \"سه نام از چهار نام درست است: «گرشاسپ» از Kirsāsp پهلوی و آن از Kərəsāspa- اوستایی «دارندهٔ اسبان لاغر»؛ «گشتاسپ» از Guštāsp پهلوی، از Vištāspa پارسی باستان/اوستایی، با تبدیل قاعده‌مند wi- آغازین به gu- در فارسی (مانند vəhrka- > گرگ)؛ «بیوراسپ» لقب ضحّاک، از bēwar پهلوی «ده‌هزار» + asp. امّا «تهماسب» را ریشه‌شناسی امروزی از Taxma-aspa اوستایی «دارندهٔ اسبان دلیر» می‌گیرد (taxma- «دلیر»؛ xm > hm)، نه از *Tūmāspa- پوکورنی که تنها در نام پدرسالاری Tūmāspāna- مانده و در فارسی دنباله ندارد. پس این یک پیوند خطاست و نورایی دو نام همانند را در هم آمیخته است.\",\n \"sources\": [W_GOSHT, IR_NAMES],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference of its own on the printed page (p.121); the refs of its parent box were checked instead.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BQT\",\"where\":\"Borhān-e Qāṭeʿ p.1819 s.v. گشتاسب, Moʿin's footnote 11\",\"stance\":\"supports\",\"note\":\"'در اوستا و پارسی باستان Vištāspa ... جزء دوم aspa همان اسب است ... بارتولمه ۱۴۶۷؛ مورخان ایرانی و عرب نام او را «بشتاسب» و «بشتاسف» نیز ضبط کرده‌اند' — the Goštāsp link is exactly as drawn.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg II 46 s.v. bēvar (NYB_vol2_glossary.txt line 995)\",\"stance\":\"supports\",\"note\":\"'bevar [bywl] ten thousand; 2 ~ spāh an army of 20000 men' — the first element of Bīvarasp.\"},\n  {\"src\":\"web/Iranica\",\"where\":\"Personal Names, Iranian ii (Schmitt), short names section\",\"stance\":\"contradicts\",\"note\":\"'Taxma- (no. 304) from compounds with Av. taxma- \\\"brave, courageous\\\"' — the source of Tahmāsp, distinct from *Tūmāspa-.\"}\n ]\n})\njson.dump(nodes, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_a.json','w'), ensure_ascii=False)\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151a.py"
}
```


### [2026-09-05T20:44:30.029Z] TOOL RESULT

```
ok 5
```


## [2026-09-05T20:46:21.425Z] TOOL CALL #87: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW_ASTAR = \"https://en.wiktionary.org/wiki/استر\"\nW_ASPAST= \"https://en.wiktionary.org/wiki/اسپست\"\nW_FISFIS= \"https://en.wiktionary.org/wiki/فصفص\"\nW_FISFISA=\"https://en.wiktionary.org/wiki/فصفصة\"\nE_ALF   = \"https://www.etymonline.com/word/alfalfa\"\nAHD_ALF = \"https://www.ahdictionary.com/word/search.html?q=alfalfa\"\nIR_NAMES= \"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/\"\nIR_ARJ  = \"https://www.iranicaonline.org/articles/arjasp\"\nWP_JAM  = \"https://en.wikipedia.org/wiki/Jamaspa\"\n\nnodes = []\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\",\n \"words\": \"aršan-aspa; aurvat-aspa; arejat-aspa; jâm-âspa\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the four are exactly right, one is unattested and one is glossed on a guess. aurvaṱ.aspa- is in Bartholomae as '• j. ʼaurvataspa- Adj. \\\"der schnelle Rosse hat\\\"', used of the sun (hvarə.xšaēta- ... aurvaṱ.aspəm, Yt.6.1) and as the name of Vīštāspa's father — Nourai's '(with) swift horses' is verbatim right. arəǰaṱ.aspa- is likewise in Bartholomae, '• j. arəǰaṱ.aspa- m. EN. eines Hyaona-Fürsten' (Yt.9.30, 5.109), from arəj- 'to be worth', so '(with) valuable horses' is the standard analysis (Iranica s.v. ARJĀSP). Jāmāspa- is a real Avestan name (Bartholomae s.v., with the patronymic Jāmāspana-), but the first element is admittedly obscure: proposals are Vedic kṣāmá- 'singed', Gershevitch's 'leading horses' and Schwartz's 'he who bridles horses'; 'owning horses' is nobody's. Finally *aršan-aspa- is not in Bartholomae at all: aršan- 'male, stallion' is well attested on its own, and compound names like auruša.aspa- 'having white horses' show the type, but this particular compound has to be reconstructed.\",\n \"derivation_fa\": \"دو نام از چهار نام دقیقاً درست است: aurvaṱ.aspa- را بارتولمه «دارندهٔ اسبان تندرو» معنی می‌کند (صفتِ خورشید در یشت ۶) و arəǰaṱ.aspa- نام سرکردهٔ خیونان است (یشت ۹/۳۰) از ریشهٔ arəj- «ارزیدن»، پس «دارندهٔ اسبان گران‌بها» درست است. امّا Jāmāspa- گرچه نامی اوستایی است، جزء نخست آن روشن نیست و پیشنهادها «سوخته» (قس. سنسکریت kṣāmá-)، «رهبری‌کنندهٔ اسبان» (گرشویچ) و «لگام‌زنندهٔ اسبان» (شوارتز) است؛ معنی «دارندهٔ اسب» پشتوانه‌ای ندارد. همچنین ترکیب *aršan-aspa- در فرهنگ بارتولمه نیامده است، هرچند aršan- «نر، نریان» به‌تنهایی گواهی شده و ترکیب‌هایی مانند auruša.aspa- «دارندهٔ اسبان سپید» این الگو را نشان می‌دهد.\",\n \"sources\": [IR_ARJ, WP_JAM, IR_NAMES],\n \"ref_check\": [\n  {\"ref\":\"BQT\",\"status\":\"not_checked\",\"note\":\"no page given; the Borhān entries for ارجاسپ/جاماسب lie in vol.1-2 whose OCR (BQT_v1_pages.txt) did not yield a legible headword for them.\"},\n  {\"ref\":\"POK:1082\",\"status\":\"contradicts\",\"note\":\"IEW 1080-1085 is the root *teu- 'to swell; fat; strong' — relevant to tum-âspa in the box above, not to aršan-/aurvaṱ-/arəǰaṱ-/jāmāspa. The reference block appears to have been copied from the previous box.\"},\n  {\"ref\":\"KNT\",\"status\":\"partial\",\"note\":\"Kent has aršan- only inside the royal name Xšayāršan- (Xerxes) 'hero among kings'; none of these four compounds appears in his Old Persian lexicon.\"},\n  {\"ref\":\"HRN:206\",\"status\":\"contradicts\",\"note\":\"Horn p.206 no.925: 'gušn \\\"Männchen, männlich\\\". aw. varšni- \\\"männlich (Widder)\\\"; phlv. gušan, vergl. N. pr. Gušnasp; ai. vṛṣṇi- \\\"Widder\\\"' — Horn derives the Gušnasp of the daughter box from varšni-, NOT from aršan-.\"},\n  {\"ref\":\"MON5:419\",\"status\":\"not_checked\",\"note\":\"Moʿin's vol.5 (اعلام) is not online in any form (refs_online.json notes repeated searches); vajehyab/abadis carry no proper-name entries from Moʿin.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. s.vv. ʼaurvataspa- (line 5566), arəǰaṱ.aspa- (line 5412), Jāmāspa-/Jāmāspana- (lines 11617, 11623), ʼaršan- (line 5634)\",\"stance\":\"partial\",\"note\":\"'• j. ʼaurvataspa- Adj. \\\"der schnelle Rosse hat\\\"'; '• j. arəǰaṱ.aspa- m. EN. eines Hyaona-Fürsten'; '• j. Jāmāspa-, g. Jāmāspa- m. EN.' (no etymology); '• j. (g., p.) ʼaršan- m. 1) \\\"Mann, Männchen\\\"'; no *aršan.aspa- headword.\"},\n  {\"src\":\"web/Iranica+Wikipedia\",\"where\":\"ARJĀSP (Tafażżoli) and Jamaspa (name section)\",\"stance\":\"partial\",\"note\":\"'ARJĀSP (Av. Arəǰaṱ.aspa), a chief of the Iranian tribe of the Xyōns (Av. Hyaona-), and an enemy of Kay Goštāsp'; for Jāmāspa 'the meaning of the first term is unclear ... One interpretation connects jāma- to Vedic kṣāmáh- ... Gershevitch proposed leading horses, whereas Schwartz has argued for he who bridles horses.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"Aršâsp «ارشاسپ»; Gošnâsp «گشناسپ»; Lohrâsb «لهراسب»; Arjâsp «ارجاسپ»; Jâmâsb «جاماسب»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Lohrāsb, Arjāsp and Jāmāsb are straightforward continuants of the Avestan names of the parent box: Auruuaṱ.aspa- > MP Lohrāsp (Av. aurvaṱ- > MP lohr- with the familiar r-metathesis/dissimilation of the Šāh-nāma onomastics) — he is Goštāsp's father in the epic; Arəǰaṱ.aspa- > MP/NP Arjāsp, the Xyōn king (Iranica); Jāmāspa- > MP Jāmāsp, Vīštāspa's minister, the -b of جاماسب being the same late spelling as in اسب. Gošnāsp, however, does not belong under aršan-aspa: NP/MP gušn 'male, stallion' comes from Av. varəšni- / PIr. *wr̥šni- with the regular Persian change of initial *w- before a rounded vowel to g- (exactly as Av. vəhrka- > گرگ gorg), and Horn, on the very page Nourai cites (no.925, p.206), spells this out and names Gušnasp as the example. Aršāsp itself is a Šāh-nāma-tradition name best derived from *Aršan-aspa-, but neither the Avestan compound nor the Persian name could be documented in an accessible reference (Moʿin's vol.5, which Nourai cites, is not available).\",\n \"derivation_fa\": \"«لهراسب»، «ارجاسپ» و «جاماسب» دنبالهٔ همان نام‌های اوستاییِ خانهٔ بالایند: Auruuaṱ.aspa- > لهراسپ (پدر گشتاسپ در شاهنامه)، Arəǰaṱ.aspa- > ارجاسپ شاه خیونان، و Jāmāspa- > جاماسپ وزیر گشتاسپ. امّا «گشناسپ» زیر aršan-aspa جای ندارد: gušn فارسی «نر، نریان» از varəšni- اوستایی (*wr̥šni- ایرانی آغازین) است با تبدیل قاعده‌مند *w آغازین به g پیش از واکهٔ گرد ــ درست مانند vəhrka- > گرگ ــ و هرن در همان صفحهٔ ۲۰۶ که نورایی به آن ارجاع می‌دهد همین را می‌گوید و «گشنسپ» را مثال می‌آورد. «ارشاسپ» را احتمالاً باید از *Aršan-aspa- گرفت، ولی نه ترکیب اوستایی و نه نام فارسی در منابع در دسترس گواهی نشد.\",\n \"sources\": [IR_ARJ, IR_NAMES],\n \"ref_check\": [\n  {\"ref\":\"MON\",\"status\":\"not_checked\",\"note\":\"the names are in Moʿin's اعلام volumes (5-6), which are not online; the 2-vol condensation (MON_part1/2.txt) has no entries for ارشاسپ/گشناسپ/لهراسب/جاماسب.\"}\n ],\n \"consulted\": [\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss no.925, p.206\",\"stance\":\"contradicts\",\"note\":\"'925. gušn \\\"Männchen, männlich\\\". aw. varšni- \\\"männlich (Widder)\\\"; phlv. gušan, vergl. N. pr. Gušnasp; ai. vṛṣṇi- \\\"Widder\\\". oss. t. urs \\\"Hengst\\\".'\"},\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. s.vv. arəǰaṱ.aspa-, ʼaurvataspa-, Jāmāspa-\",\"stance\":\"supports\",\"note\":\"the three Avestan originals of Arjāsp, Lohrāsp and Jāmāsp are all headwords there (see node #6).\"},\n  {\"src\":\"web/Iranica\",\"where\":\"ARJĀSP (Encyclopaedia Iranica II/4, p.412)\",\"stance\":\"supports\",\"note\":\"'ARJĀSP (Av. Arəǰaṱ.aspa) ... an enemy of Kay Goštāsp (Kavi Vištāspa), patron of Zoroaster (Yašt 9.30, 5.109).'\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Avestan\", \"words\": \"aspa-asa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The analysis 'horse' + 'eat' is right and is precisely what Nourai's own source says: Moʿin's footnote on Borhān p.119 explains اسپست as 'این کلمهٔ مرکب لفظاً یعنی «اسب می‌خورد»، جزء اول همان اسب است و جزء دوم از مصدر ad مطابق edere لاتینی و essen آلمانی و (to) eat انگلیسی'; Horn no.79 says the same ('Wörtlich \\\"Pferdefutter\\\" von esp und √ad-', after Nöldeke ZDMG 32,408). Two corrections: the compound is not attested in the Avesta (Bartholomae has no aspa.asa-/aspō.asti- headword), and the standard reconstruction is Old Iranian *aspa-sti- / *aspāsti- with the noun *-sti- 'food' rather than a bare verbal asa-: AHD s.v. alfalfa gives 'Old Iranian aspasti- : *aspa-, horse ... + *-sti-, food, fodder; see ed-', and Wiktionary reconstructs PIr. *HacwaHastiš. So the box should read Old Iranian *aspa-sti-, and the ☞Ed cross-reference is correct.\",\n \"derivation_fa\": \"تحلیل «اسب + خوردن» درست است و دقیقاً همان چیزی است که منبع خود نورایی می‌گوید: معین در حاشیهٔ برهان (ص ۱۱۹) می‌نویسد «این کلمهٔ مرکب لفظاً یعنی «اسب می‌خورد»، جزء اول همان اسب است و جزء دوم از مصدر ad ... به معنی خوردن»؛ هرن (شمارهٔ ۷۹) نیز آن را «خوراک اسب» از esp و ریشهٔ ad- می‌داند. دو تصحیح لازم است: این ترکیب در اوستا گواهی نشده (بارتولمه چنین مدخلی ندارد) و بازسازی پذیرفته‌شده *aspa-sti- ایرانی باستان با اسمِ *-sti- «خوراک» است، نه asa-. پس ارجاع نورایی به ریشهٔ Ed درست است ولی برچسب «اوستایی» و صورت واژه باید اصلاح شود.\",\n \"sources\": [AHD_ALF, E_ALF, W_ASPAST],\n \"ref_check\": [\n  {\"ref\":\"BQT:1819\",\"status\":\"not_found\",\"note\":\"printed p.1819 is the گشتاسب entry (see node #1); the اسپست material with the aspa+ad analysis is on p.119, which Nourai cites on the daughter boxes instead.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb., searched for aspa.asa-/aspō.asti-/'Futter' compounds\",\"stance\":\"silent\",\"note\":\"no such Avestan headword; the aspa- compounds listed are aspa-nhad-, āsu.aspa-, čaθwara.aspa-, yuxta.aspa- etc.\"},\n  {\"src\":\"AHD\",\"where\":\"American Heritage Dictionary online s.v. alfalfa\",\"stance\":\"partial\",\"note\":\"'from Middle Persian aspast, from Old Iranian aspasti- : *aspa-, horse; see ekwo- ... + *-sti-, food, fodder; see ed-' — same two elements, different (nominal) second member.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn no.79, p.19\",\"stance\":\"supports\",\"note\":\"'Wörtlich \\\"Pferdefutter\\\" von esp und √ad-, Nöldeke, ZDMG. 32, 408.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Pahlavi\", \"words\": \"aspast\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie p.13: 'aspast [ʾspst\\\\' | N ~] clover, lucerne'; the word is Book Pahlavi ʾspst\\\\' , i.e. asp 'horse' + -ast < *-asti- 'fodder', with the Middle Persian loss of the internal vowel. Moʿin's footnote to Borhān p.119 states 'در پهلوی نیز aspast آمده' and cites Unvala 280, and Horn no.79 gives 'phlv. aspast \\\"Luzerne\\\"' as the source of NP espist/ispist. Wiktionary reconstructs MP aspast < Middle Median *aspast < Old Median *aspāstiš.\",\n \"derivation_fa\": \"مکنزی (ص ۱۳): «aspast [ʾspst] شبدر، یونجه»؛ واژه از asp «اسب» و -ast (از *-asti- «خوراک») ساخته شده با افتادن واکهٔ میانی در فارسی میانه. معین در حاشیهٔ برهان (ص ۱۱۹) می‌نویسد «در پهلوی نیز aspast آمده» و به اونوالا ۲۸۰ ارجاع می‌دهد؛ هرن (شمارهٔ ۷۹) نیز «phlv. aspast» را اصلِ espist/ispist فارسی می‌داند. ادعای نورایی درست است.\",\n \"sources\": [W_ASPAST, AHD_ALF],\n \"ref_check\": [\n  {\"ref\":\"BQT:119\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 331 (printed p.119), Moʿin's footnote: '... در پهلوی نیز aspast آمده، از زبان پهلوی داخل سریانی و از سریانی به عربی رفته «فصفصه» (جمع: فصافص) شد' — the whole chain of nodes #9-#12 in one sentence.\"}\n ],\n \"consulted\": [\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.13 (PHD.txt line 219; English index line 1258 'clover aspast', 2684 'lucerne aspast')\",\"stance\":\"supports\",\"note\":\"'aspast [ʾspst | N ~] clover, lucerne.'\"},\n  {\"src\":\"HRN\",\"where\":\"Horn no.79, p.19\",\"stance\":\"supports\",\"note\":\"'79. espist, uspust, ispist \\\"Luzerne\\\". phlv. aspast \\\"Luzerne\\\". bal. LW. aspust.'\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien p.130 (HUB.txt line 4465)\",\"stance\":\"supports\",\"note\":\"'aspist (ispist, uspust) \\\"Luzerne\\\" = phl. aspast'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"aspast «اسپست» (also سپست)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP اسپست aspast, with the aphaeretic variant سپست sepest quoted from Sanāʾi in the box, is the direct continuant of MP aspast; Horn no.79 registers the New Persian forms as espist, uspust, ispist, and Borhān-e Qāṭeʿ p.119 has the headword اسپست glossing it as the fodder plant and equating it with Arabic فصفصه and بذرالرطبه for its seed. The loss of the initial vowel in سپست is the same process as اسپید/سپید and اسپاه/سپاه. The modern Persian name of the plant is یونجه (a Turkic loan), which Moʿin's dictionary glosses as 'اسپست، فصفصه'.\",\n \"derivation_fa\": \"«اسپست» فارسی و گونهٔ کوتاه‌شدهٔ آن «سپست» (شاهد سنایی در همین خانه) دنبالهٔ مستقیم aspast فارسی میانه است؛ هرن (شمارهٔ ۷۹) صورت‌های espist، uspust و ispist را ثبت کرده و برهان قاطع (ص ۱۱۹) مدخل «اسپست» را دارد و آن را با «فصفصه» عربی و «بذرالرطبه» برای تخم آن برابر می‌گیرد. افتادن الفِ آغازین در «سپست» همان فرایندِ اسپید/سپید و اسپاه/سپاه است. نام رایج امروزی این گیاه «یونجه» است که معین آن را «اسپست، فصفصه» معنی می‌کند. ادعای نورایی درست است.\",\n \"sources\": [W_ASPAST],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference of its own; BQT:119 (the parent's reference) covers it and does support it.\"}\n ],\n \"consulted\": [\n  {\"src\":\"BQT\",\"where\":\"Borhān-e Qāṭeʿ p.119 (BQT_v1_pages.txt leaf 331)\",\"stance\":\"supports\",\"note\":\"headword 'اسپست ... و آن علفی است ... و عربی فصفصه ... و تخم آنرا بذرالرطبه گویند'.\"},\n  {\"src\":\"MON\",\"where\":\"Moʿin (2-vol condensation) s.v. یونجه/علف (MON_part1.txt line 97960)\",\"stance\":\"supports\",\"note\":\"'(گیا.) اسپست، فصفصه' — Moʿin equates the two words as names of the same plant.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn no.79\",\"stance\":\"supports\",\"note\":\"'espist, uspust, ispist \\\"Luzerne\\\"' as the NP reflexes of phlv. aspast.\"}\n ]\n})\njson.dump(nodes, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_b.json','w'), ensure_ascii=False)\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151b.py"
}
```


### [2026-09-05T20:46:24.140Z] TOOL RESULT

```
ok 5
```


## [2026-09-05T20:47:42.361Z] TOOL CALL #88: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151c.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW_ASTAR = \"https://en.wiktionary.org/wiki/استر\"\nW_FISFIS= \"https://en.wiktionary.org/wiki/فصفص\"\nW_FISFISA=\"https://en.wiktionary.org/wiki/فصفصة\"\nE_ALF   = \"https://www.etymonline.com/word/alfalfa\"\nAHD_ALF = \"https://www.ahdictionary.com/word/search.html?q=alfalfa\"\n\nnodes = []\n\nnodes.append({\n \"id\": 11, \"lang\": \"Syriac\", \"words\": \"pespesta\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Aramaic/Syriac stage is certain, the exact form less so. Syriac/Jewish Aramaic has ʾaspastā / ʾaspestā 'lucerne' (Wiktionary s.v. فصفص: 'Borrowed from Aramaic אַסְפַּסְתָּא (ʾaspastā) / ܐܰܣܦܷܣܬܳܐ (ʾaspestā, \\\"lucerne\\\"), from Akkadian aspastu, from Old Median *aspāstiš'), i.e. with initial a-, not p-. AHD explains the p-form as Coptic: Arabic fiṣfiṣa comes 'probably via Coptic p-espesta: p-, masculine sing. definite article + espesta, alfalfa, from Aramaic espestā, from Middle Persian aspast'. So the pespesta Nourai puts in a Syriac box is the form that mediated to Arabic, but its p- is most likely the Coptic article agglutinated to the Aramaic word, and the borrowing route Pahlavi > Aramaic/Syriac > Arabic is exactly what Moʿin states on Borhān p.119.\",\n \"derivation_fa\": \"مرحلهٔ آرامی/سریانی قطعی است ولی صورتِ دقیق آن جای بحث دارد. در سریانی و آرامیِ یهودی ʾaspastā/ʾaspestā «یونجه» ثبت شده است (ویکی‌واژه ذیل «فصفص»، با ارجاع به اکدی aspastu و مادیِ باستان *aspāstiš)، یعنی با الفِ آغازین نه با p. فرهنگ American Heritage صورتِ p-دار را قبطی می‌داند: «احتمالاً از راه قبطی p-espesta که p- حرف تعریف مذکر قبطی است». پس «pespesta» همان صورتی است که به عربی رسیده، ولی p آغازین آن به احتمال زیاد حرف تعریف قبطی است؛ در عوض مسیر پهلوی ← سریانی ← عربی همان است که معین در حاشیهٔ برهان (ص ۱۱۹) می‌نویسد. ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_FISFIS, AHD_ALF],\n \"ref_check\": [\n  {\"ref\":\"BQT:119\",\"status\":\"supports\",\"note\":\"Moʿin's footnote, Borhān p.119: 'در پهلوی نیز aspast آمده، از زبان پهلوی داخل سریانی و از سریانی به عربی رفته «فصفصه» (جمع: فصافص) شد' — Nourai's Pahlavi > Syriac > Arabic arrows are Moʿin's own.\"}\n ],\n \"consulted\": [\n  {\"src\":\"AHD\",\"where\":\"AHD5 online s.v. alfalfa (etymology bracket)\",\"stance\":\"partial\",\"note\":\"'ultimately (probably via Coptic p-espesta: p-, masculine sing. definite article + espesta, alfalfa) from Aramaic espestā, from Middle Persian aspast'.\"},\n  {\"src\":\"PLA\",\"where\":\"Asbaghi, Persische Lehnwörter im Arabischen, p.~26 s.v. ʾasfast (PLA_pages.txt line 1426)\",\"stance\":\"supports\",\"note\":\"'asfast: \\\"Luzerne, Futterpflanze\\\" pers. اسپست aspast, MP. aspast' — Asbaghi keeps the Persian source but does not name the Aramaic intermediary here.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Arabic\", \"words\": \"alfesfeseh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic فِصْفِصَة fiṣfiṣa (also فَصْفَصَة faṣfaṣa, coll. فِصْفِص, pl. فَصَافِص faṣāfiṣ) 'lucerne' with the article al-fiṣfiṣa is the Arabic reshaping of the Aramaic/Syriac form: the initial (ʾ)a- was taken for the article and dropped, and the resulting stem was fitted to the quadriliteral reduplicated pattern fiʿfiʿa, whence the plural faṣāfiṣ. Asbaghi (Persische Lehnwörter im Arabischen, p.210) lists 'fiṣfiṣa: \\\"Luzerne\\\" pers. اسپست asbast od. اسفست asfast', and Lokotsch no.598 'Ar. faṣfaṣa \\\"Luzerne, Medicago sativa L.\\\", auch fiṣfiṣa; hieraus sp. alfalfa'. Klein and AHD agree.\",\n \"derivation_fa\": \"عربی «فِصْفِصَة» (و «فَصْفَصَة»، جمعِ فصافص) از صورت آرامی/سریانی گرفته شده است: الفِ آغازین را حرف تعریف پنداشته و انداخته‌اند و ستاک باقی‌مانده را بر وزن رباعیِ مضاعف fiʿfiʿa ریخته‌اند، از همین رو جمع مکسّر «فصافص» ساخته شده. اصباغی (وام‌واژه‌های فارسی در عربی، ص ۲۱۰) می‌نویسد «fiṣfiṣa: یونجه، از فارسی اسپست/اسفست» و لوکوچ (شمارهٔ ۵۹۸) همین را می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [W_FISFIS, W_FISFISA, AHD_ALF, E_ALF],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the Arabic box carries no reference on the printed page; the parent's BQT:119 covers the step and supports it.\"}\n ],\n \"consulted\": [\n  {\"src\":\"PLA\",\"where\":\"Asbaghi 1988 p.210 (PLA_pages.txt lines 11811, 11831)\",\"stance\":\"supports\",\"note\":\"'fisfisa: \\\"Luzerne\\\" pers. ?, dtsch. Alfalfa' and 'fisfisa: \\\"Luzerne\\\" pers. اسپست asbast od. اسفست asfast'.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no.598\",\"stance\":\"supports\",\"note\":\"'598. Ar. faṣfaṣa: \\\"Luzerne Medicago sativa L.\\\", auch fiṣfiṣa; hieraus sp. alfalfa, alfafe ... engl. amerik. alfalfa.'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. alfalfa (KLN_1966.txt line 2169)\",\"stance\":\"supports\",\"note\":\"'alfalfa, n., lucerne. — Sp., fr. Arab. al-faṣfaṣa. (Cp. the collateral Sp. form alfalfez, which represents the intermediate form between Arab. al-faṣfaṣah and Sp. alfalfa.)'\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"fasfaseh «فسفسه» (also فصفصه)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"فصفصه (written also فسفسه) is the Arabic word taken back into Persian as a learned/pharmacological term for the same plant — a round trip: Old Iranian *aspa-sti- > MP aspast > Aramaic > Arabic fiṣfiṣa > Persian فصفصه, alongside the inherited اسپست/سپست of node #10. Moʿin's dictionary treats the two as synonyms of یونجه, and Borhān s.v. اسپست already glosses it with Arabic فصفصه, which shows the borrowed form circulating in Persian herbals. The Persian pronunciation fasfase reflects the Arabic faṣfaṣa vocalisation.\",\n \"derivation_fa\": \"«فصفصه» (به املای «فسفسه» نیز) همان واژهٔ عربی است که دوباره به فارسی بازگشته و در متون دارویی و گیاه‌شناسی به‌کار رفته است؛ یعنی یک سفر رفت‌وبرگشت: *aspa-sti- ایرانی باستان ← aspast پهلوی ← آرامی ← فصفصهٔ عربی ← فارسی، در کنارِ صورت موروثیِ «اسپست/سپست». معین این دو را هم‌معنی «یونجه» می‌آورد و برهان قاطع نیز در مدخل «اسپست» معادل عربی «فصفصه» را می‌دهد. تلفّظ فارسی fasfase بازتاب صورت عربی faṣfaṣa است. ادعای نورایی درست است.\",\n \"sources\": [W_FISFISA],\n \"ref_check\": [\n  {\"ref\":\"MON:2547\",\"status\":\"partial\",\"note\":\"the 6-vol Farhang is not online and no scan exists (refs_online.json); in the 2-vol Adena condensation (MON_part1.txt lines 83926, 97960) فصفصه appears twice as a synonym of شبدر/یونجه ('... رطبه، فصفصه، شبدر چمنی' and '(گیا.) اسپست، فصفصه'), which is the entry content Nourai cites, but the page number could not be verified.\"}\n ],\n \"consulted\": [\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt lines 83926, 97960\",\"stance\":\"supports\",\"note\":\"'فصفصه، شبدر چمنی، شبدر گل قرمز' and '(گیا.) اسپست، فصفصه'.\"},\n  {\"src\":\"BQT\",\"where\":\"Borhān p.119 s.v. اسپست\",\"stance\":\"supports\",\"note\":\"the entry itself equates اسپست with the Arabic فصفصه.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"alfalfa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The etymology is right but one link is missing from the chart: English alfalfa (first attested 1845, in American agricultural writing) is from Spanish alfalfa, earlier alfalfez, from Arabic al-faṣfaṣa; it did not come into English from Arabic directly. AHD, the very dictionary Nourai cites (AHD:32 = the entry alfalfa), prints '[Spanish, from Arabic al-faṣfaṣa: al-, the + faṣfaṣa, alfalfa (variant of fiṣfiṣa, ultimately ... from Aramaic espestā, from Middle Persian aspast, from Old Iranian aspasti- : *aspa-, horse; see ekwo- ... + *-sti-, food, fodder; see ed-)]'. Moʿin's Borhān footnote likewise ends '... و از عربی در اسپانیایی وارد شده صورت الفلفه ... اسپانیولی‌ها آن را به آمریکا بردند'. Etymonline dates the English word to 1845 and cites Watkins for the Old Iranian compound.\",\n \"derivation_fa\": \"ریشه‌شناسی درست است ولی یک حلقه از نمودار افتاده: alfalfa انگلیسی (نخستین کاربرد ۱۸۴۵ در نوشته‌های کشاورزی آمریکا) از اسپانیایی alfalfa (کهن‌تر alfalfez) و آن از عربی «الفصفصة» است؛ مستقیم از عربی به انگلیسی نرفته است. خودِ فرهنگ American Heritage که نورایی به آن ارجاع می‌دهد (AHD:32) می‌نویسد «از اسپانیایی، از عربی al-faṣfaṣa ... از آرامی espestā، از فارسی میانه aspast، از aspasti- ایرانی باستان». معین هم در همان حاشیهٔ برهان می‌گوید «از عربی در اسپانیایی وارد شده صورت الفلفه ... اسپانیولی‌ها آن را به آمریکا بردند». پس تنها نقصِ نمودار نبودِ خانهٔ اسپانیایی است.\",\n \"sources\": [AHD_ALF, E_ALF],\n \"ref_check\": [\n  {\"ref\":\"AHD:32\",\"status\":\"supports\",\"note\":\"AHD entry 'alfalfa' (p.32 of the New College Edition; checked in the current online AHD5): '[Spanish, from Arabic al-faṣfaṣa ... from Middle Persian aspast, from Old Iranian aspasti- : *aspa-, horse; see ekwo- in the Appendix ... + *-sti-, food, fodder; see ed- in the Appendix]' — the whole chart in one bracket, with Spanish added.\"}\n ],\n \"consulted\": [\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. alfalfa\",\"stance\":\"partial\",\"note\":\"'Sp., fr. Arab. al-faṣfaṣa' — Spanish intermediary, no Iranian prehistory.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch no.598\",\"stance\":\"partial\",\"note\":\"'hieraus sp. alfalfa ... engl. amerik. alfalfa' — again via Spanish.\"},\n  {\"src\":\"web/Etymonline\",\"where\":\"etymonline.com/word/alfalfa\",\"stance\":\"supports\",\"note\":\"'1845, from Spanish alfalfa, earlier alfalfez ... from Arabic al-fisfisa \\\"fresh fodder.\\\" Watkins says it is ultimately from an Old Iranian compound *aspa-sti- \\\"alfalfa, clover\\\", from *aspa- \\\"horse\\\" ... + -sti- \\\"food\\\".'\"}\n ]\n})\njson.dump(nodes, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_c.json','w'), ensure_ascii=False)\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151c.py"
}
```


### [2026-09-05T20:47:44.457Z] TOOL RESULT

```
ok 4
```


## [2026-09-05T20:49:58.177Z] TOOL CALL #89: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151d.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW_ASTAR = \"https://en.wiktionary.org/wiki/استر\"\nW_HIPPOS= \"https://en.wiktionary.org/wiki/ἵππος\"\nW_PIE   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁éḱwos\"\nE_PHIL  = \"https://www.etymonline.com/word/Philip\"\nE_HIPPO = \"https://www.etymonline.com/word/hippopotamus\"\n\nnodes = []\n\nnodes.append({\n \"id\": 15, \"lang\": \"Sanskrit\", \"words\": \"asva-tara\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Sanskrit अश्वतर aśvatara- is a real word and does belong to *h₁éḱwos: it is aśva- 'horse' plus the contrastive/comparative suffix -tara- (as in Lat. dexter, Gk. -teros), literally 'the more horse-like one' — but its lexical meaning is 'mule', not the vague 'related to a horse' of the chart, which is Moʿin's paraphrase (Moʿin s.v. استر: '[= ستر؛ مربوط به اسب، قس. قاطر] (جان.) قاطر'). Horn no.86 cites 'ai. aśvatará- \\\"Maulesel\\\"'. The formation is old and shared: the same suffix on the same noun gives Old Persian *asatara- and Middle Persian astar, so aśvatara- is best regarded as the Indic member of an Indo-Iranian pair, not as a source (see node #16).\",\n \"derivation_fa\": \"سنسکریت aśvatara- واژه‌ای واقعی و از همین ریشه است: aśva- «اسب» به‌علاوهٔ پسوند برتری/تقابل -tara-، تحت‌اللفظ «آنکه بیشتر اسب‌گونه است»؛ امّا معنای فرهنگ‌نامه‌ای آن «استر/قاطر» است نه «مربوط به اسب» که تعبیر معین است (معین ذیل «استر»: «[= ستر؛ مربوط به اسب، قس. قاطر] (جان.) قاطر»). هرن (شمارهٔ ۸۶) نیز «ai. aśvatará- \\\"استر\\\"» می‌آورد. این ساخت هندوایرانی مشترک است و همان پسوند بر همان اسم، *asatara- پارسی باستان و astar پهلوی را داده است.\",\n \"sources\": [W_ASTAR],\n \"ref_check\": [\n  {\"ref\":\"MON:246\",\"status\":\"supports\",\"note\":\"Moʿin's entry for استر (checked in MON_part1.txt line 11742, the 2-vol condensation of the same dictionary): 'استر: [= ستر؛ مربوط به اسب قس. قاطر] (جان.) قاطر' — Nourai's gloss 'related to a horse' is a literal rendering of Moʿin's 'مربوط به اسب'.\"},\n  {\"ref\":\"BQT:125\",\"status\":\"partial\",\"note\":\"Borhān vol.1, printed p.~125 = BQT_v1_pages.txt leaf 337, the است/استاد/استرآباد block; the running text there says 'مخفف استر باشد که از دواب مشهوره است' with footnote '۱ - رک: استر', i.e. the استر entry is on this page range, but the OCR of the entry itself is too damaged to quote Moʿin's Latin footnote.\"}\n ],\n \"consulted\": [\n  {\"src\":\"HRN\",\"where\":\"Horn no.86, p.20\",\"stance\":\"supports\",\"note\":\"'86. ester \\\"Maulesel\\\". phlv. astar; ai. aśvatará- \\\"Maulesel\\\".'\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien (HUB.txt lines 2687, 7560)\",\"stance\":\"partial\",\"note\":\"'astar \\\"Maulesel\\\", skr. aśvatara- (neben ap. uvaspa, Vištāspa, Aspacana)' and 'astar \\\"Maulesel\\\" = ap. *asatara-, skr. aśvatara-' — a cognate pair, not a loan.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Pahlavi\", \"words\": \"\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The empty box stands for Middle Persian astar 'mule', and the arrow drawn into it — Sanskrit aśvatara- > Pahlavi — is the wrong direction of transmission. Hübschmann derives the Persian word from an Old Persian *asatara- built on the byform asa- (with the same loss of p as in suvār < asabāra-) and treats Skt. aśvatara- as its cognate, not its source: 'mit Ausfall des p: suvār \\\"Reiter\\\" = ap. asabāra-; astar \\\"Maulesel\\\" = ap. *asatara-, skr. aśvatara-'. Wiktionary agrees: NP استر is 'inherited from Middle Persian ʾstl /astar/, from Old Persian *asatarah, from Proto-Iranian *Hacwatarāh, from Proto-Indo-Iranian *Haćwatarás'. There is no evidence of a Sanskrit loan into Middle Persian here; the chart's Pahlavi box should hang directly from the root.\",\n \"derivation_fa\": \"این خانهٔ خالی نمایندهٔ astar «استر» در فارسی میانه است و پیکانی که از سنسکریت به آن کشیده شده جهتِ درستِ انتقال نیست. هوبشمان این واژه را از *asatara- پارسی باستان می‌گیرد که بر صورت فرعی asa- ساخته شده (با همان افتادن p که در suvār < asabāra- دیده می‌شود) و aśvatara- سنسکریت را هم‌ریشهٔ آن می‌داند نه اصلِ آن. ویکی‌واژه نیز می‌گوید «استر» موروثی است از astar فارسی میانه، از *asatarah پارسی باستان، از *Hacwatarāh ایرانی آغازین. هیچ نشانی از وام‌گیری از سنسکریت در کار نیست؛ پس پژوهش امروزی این پیکان را رد می‌کند و خانهٔ پهلوی باید مستقیماً از ریشه گرفته شود.\",\n \"sources\": [W_ASTAR],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference on the printed page.\"}\n ],\n \"consulted\": [\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien (HUB.txt lines 4276, 6657, 7560)\",\"stance\":\"contradicts\",\"note\":\"'*asawāra- aus *aspabāra-; astar \\\"Maulesel\\\" = ap. *asatara-' and 'astar \\\"Maulesel\\\" aus *asatar = skr. aśvatara-' — an inherited Iranian formation, not a borrowing from Indic.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary\",\"stance\":\"silent\",\"note\":\"searched PHD.txt for astar/'mule': MacKenzie's glossary has aštar 'whip', dōšastar 'west', wastar 'clothing' but no entry astar 'mule' (the word is attested in Pahlavi Vd./Bd. texts, cf. Horn's 'phlv. astar').\"},\n  {\"src\":\"HRN\",\"where\":\"Horn no.86\",\"stance\":\"supports\",\"note\":\"'phlv. astar' is given as the immediate ancestor of NP ester/astar.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Persian\", \"words\": \"astar «استر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP استر astar/ester 'mule' continues MP astar without change beyond the New Persian vowel notation; Horn no.86 lists 'ester \\\"Maulesel\\\": phlv. astar; ai. aśvatará-' with the Kurdish and Balochi cognates istir/histir, istal. The semantic development is Indo-Iranian: the -tara- derivative of 'horse' names the animal that is 'horse-ish' without being a horse. A late Persian folk etymology reading it as 'astar-vand ~ Maulesel-ähnlich' is noted and rejected by Hübschmann (p.716).\",\n \"derivation_fa\": \"«استر» فارسی نو دنبالهٔ بی‌واسطهٔ astar فارسی میانه است؛ هرن (شمارهٔ ۸۶) آن را با هم‌ریشه‌های کردی istir/histir و بلوچی istal می‌آورد. تحول معنایی هندوایرانی است: مشتقِ -tara- از «اسب» جانوری را می‌نامد که «اسب‌گونه» است ولی اسب نیست. ریشه‌شناسی عامیانهٔ متأخری که آن را «استروند = شبیه استر» می‌خواند، هوبشمان (ص ۷۱۶) رد کرده است. ادعای نورایی درست است.\",\n \"sources\": [W_ASTAR],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference; MON:246 on the grandparent box does cover the Persian word and supports it.\"}\n ],\n \"consulted\": [\n  {\"src\":\"HRN\",\"where\":\"Horn no.86, p.20\",\"stance\":\"supports\",\"note\":\"'86. ester \\\"Maulesel\\\". phlv. astar; ai. aśvatará- \\\"Maulesel\\\". kurd. istir, histir; bal. istal, n. hastal.'\"},\n  {\"src\":\"MON\",\"where\":\"Moʿin s.v. استر (MON_part1.txt line 11742)\",\"stance\":\"supports\",\"note\":\"'استر: [= ستر؛ مربوط به اسب قس. قاطر] (جان.) قاطر.'\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann p.716 (HUB.txt lines 2598-2599)\",\"stance\":\"partial\",\"note\":\"'Für die Volksetymologie (astarvan, jüd.-pers. astarvund = \\\"Maulesel-ähnlich\\\", also aus astar+vand) liesse...' — records and rejects the folk etymology.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Greek\", \"words\": \"hippos; philo-hippos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. ἵππος híppos 'horse' is the Greek reflex of *h₁éḱwos, via Proto-Hellenic *íkkʷos (Mycenaean i-qo); as Pokorny and Wiktionary both stress, the word is phonetically irregular — the expected form would be **épos, and the ι for ε, the rough breathing and the geminate -ππ- are unexplained (Kretschmer and Pokorny suspect an Illyrian/other IE dialect loan; the dialectal ἴκκος of Tarentum and Epidaurus points the same way). φίλιππος phílippos 'fond of horses' is a regular Greek possessive compound of φίλος 'dear, loving' + ἵππος, used from the classical period as an adjective and as the personal name Φίλιππος; Nourai's ☞Bhili cross-reference to the root of φίλος is right.\",\n \"derivation_fa\": \"یونانی ἵππος «اسب» بازتاب *h₁éḱwos است از راه هلنیِ آغازین *íkkʷos (میسنی i-qo)؛ چنانکه پوکورنی و ویکی‌واژه هر دو تأکید می‌کنند این صورت از نظر آوایی بی‌قاعده است: صورت مورد انتظار **épos بوده و ι به‌جای ε، دمِ درشت (rough breathing) و دوگانگیِ -ππ- توضیح‌ناپذیر است (کرچمر و پوکورنی وام‌گیری از گویشی ایلیریایی را محتمل می‌دانند؛ گونهٔ گویشی ἴκκος نیز همین را نشان می‌دهد). φίλιππος «اسب‌دوست» ترکیبی قاعده‌مند از φίλος «دوست‌دارنده» و ἵππος است که از دورهٔ کلاسیک هم صفت و هم نام خاص (Φίλιππος) بوده است. ادعای نورایی درست است.\",\n \"sources\": [W_HIPPOS, W_PIE, E_PHIL],\n \"ref_check\": [\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins's appendix, entry 'ekwo-. Horse ... 2. Greek hippos, horse: EOHIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]' (AHD_watkins1985.txt line 433).\"}\n ],\n \"consulted\": [\n  {\"src\":\"POK\",\"where\":\"IEW 301-302\",\"stance\":\"supports\",\"note\":\"'gr. ἵππος ds. m. f. (originally without Asper: Ἀλκ-ιππος etc.) ... neither the Asper nor ι can be explained by gr.'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. hippo- (KLN_1966.txt line 17838)\",\"stance\":\"supports\",\"note\":\"'hippo-, before a vowel hipp-, combining form meaning \\\"horse\\\". — Gk. ἱππο-, ἱππ-, fr. ἵππος, \\\"horse\\\", rel. to dial. Gk. ἴκκος, for I.-E. *ekwos, whence also OI. aśvah, L. equus.'\"},\n  {\"src\":\"SYN\",\"where\":\"Buck 3.41\",\"stance\":\"supports\",\"note\":\"'Grk. ἵππος, dial. also ἴκκος (but with some unexplained phonetic features and taken as an Illyr. loanword by Kretschmer, Glotta 22.120).'\"}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The empty Latin box is the transmission stage for the two Greek words: Latin Philippus (the Macedonian king's name, then a Christian name through the apostle) and Late Latin hippopotamus, taken from Greek ἱπποπόταμος, itself an irregular univerbation of ὁ ἵππος ποτάμιος 'the horse of the river'. Latin's own inherited reflex of the root is equus, which the chart does not draw here. So the box is right as a route (Greek > Latin > French/English) but it holds borrowings, not an inherited Latin form.\",\n \"derivation_fa\": \"این خانهٔ خالی لاتینی، ایستگاه انتقالِ دو واژهٔ یونانی است: Philippus (نام پادشاه مقدونی و سپس نامی مسیحی از راه نام حواری) و hippopotamus لاتینیِ متأخر از یونانی ἱπποπόταμος که خود ترکیبی بی‌قاعده از ὁ ἵππος ποτάμιος «اسبِ رودخانه» است. صورت موروثیِ خودِ لاتین از این ریشه equus است که در نمودار نیامده. پس این خانه به‌عنوان مسیرِ انتقال درست است، ولی آنچه در آن است وام‌واژه است نه صورت موروثی.\",\n \"sources\": [E_PHIL, E_HIPPO],\n \"ref_check\": [\n  {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the box carries no reference on the printed page.\"}\n ],\n \"consulted\": [\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. Philip (KLN_1966.txt line 28516)\",\"stance\":\"supports\",\"note\":\"'Philip, masc. PN. — L. Philippus, fr. Gk. Φίλιππος, fr. φίλιππος, \\\"fond of horses\\\", compounded of φίλος ... and ἵππος.'\"},\n  {\"src\":\"web/Etymonline\",\"where\":\"etymonline.com/word/hippopotamus\",\"stance\":\"supports\",\"note\":\"'1560s, from Late Latin hippopotamus, from Greek hippopotamos \\\"riverhorse\\\", an irregular formation from earlier ho hippos potamios.'\"},\n  {\"src\":\"POK\",\"where\":\"IEW 301\",\"stance\":\"partial\",\"note\":\"'Latin equus \\\"a horse, steed\\\"' — the inherited Latin word, not the one transmitted here.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The empty French box stands for Philippe, the French form of Latin Philippus (Old French Philippe, with the Latin -us dropped and the stress-final syllable reduced), the name of six kings of France and hence a standard European Christian name. It is the immediate model for the modern Persian transcription in the next box. No French word from this root reaches English on this chart, so the box's only function is the route Latin > French > Persian.\",\n \"derivation_fa\": \"خانهٔ خالی فرانسوی نمایندهٔ Philippe است، صورت فرانسویِ Philippus لاتینی (فرانسویِ کهن Philippe، با افتادن پایانهٔ -us لاتین)، نام شش پادشاه فرانسه و از همین رو نامی رایج در اروپا. همین صورت الگوی مستقیم آوانویسی فارسیِ خانهٔ بعدی است. کارکرد این خانه تنها نشان‌دادن مسیر لاتین ← فرانسه ← فارسی است.\",\n \"sources\": [E_PHIL],\n \"ref_check\": [\n  {\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins's appendix under ekwo- lists PHILIP among the English derivatives but says nothing about a French stage; the AHD main entry Philip gives 'Latin Philippus, from Greek Philippos'.\"}\n ],\n \"consulted\": [\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. Philip\",\"stance\":\"partial\",\"note\":\"Klein takes English Philip straight from Latin; the French Philippe is the parallel Romance outcome and the model for later borrowings into other languages.\"},\n  {\"src\":\"web/Etymonline\",\"where\":\"etymonline.com/word/Philip\",\"stance\":\"partial\",\"note\":\"'masc. proper name ... from Latin Philippus, from Greek Philippos \\\"fond of horses\\\"' — no French intermediary for English, which is consistent with the chart drawing French only towards Persian.\"}\n ]\n})\n\nnodes.append({\n \"id\": 21, \"lang\": \"Persian\", \"words\": \"Fîlîp «فیلیپ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"فیلیپ Filip is a modern Persian transcription of the European name, taken through French Philippe (whence the final -p and the long ī of the second syllable, against English 'Philip' with reduced vowel); Persian renders French /f/ with ف and both vowels with ی, the usual pattern for 19th-20th c. French borrowings (compare فیلسوف, فرانسه). Its ultimate sense 'horse lover' is the Greek φίλιππος, so the box is right; it is a learned borrowing, not a Persian inheritance from the root — a fact the chart shows correctly by hanging it from French rather than from the Iranian branch.\",\n \"derivation_fa\": \"«فیلیپ» آوانویسی امروزیِ نام اروپایی است که از راه فرانسوی Philippe به فارسی رسیده (از همین رو پایانهٔ -p و کشیدگی هجای دوم، برخلاف Philip انگلیسی)؛ الگوی آوانویسی همان الگوی وام‌واژه‌های فرانسویِ سدهٔ سیزدهم و چهاردهم خورشیدی است (قس. فیلسوف، فرانسه). معنای بنیادی آن «اسب‌دوست» یونانی است، پس محتوای خانه درست است؛ این واژه وام‌واژه‌ای فرهیخته است نه میراث ایرانیِ این ریشه، و نمودار هم درست آن را زیر فرانسوی آورده است.\",\n \"sources\": [E_PHIL],\n \"ref_check\": [\n  {\"ref\":\"MON\",\"status\":\"not_checked\",\"note\":\"personal names are in Moʿin's vols 5-6 (اعلام), which are not online; the 2-vol condensation has no entry فیلیپ.\"}\n ],\n \"consulted\": [\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. Philip\",\"stance\":\"supports\",\"note\":\"'L. Philippus, fr. Gk. Φίλιππος ... \\\"fond of horses\\\"' — the meaning Nourai gives the Persian form.\"},\n  {\"src\":\"web/Etymonline\",\"where\":\"etymonline.com/word/Philip\",\"stance\":\"supports\",\"note\":\"same chain; confirms the sense 'fond of horses'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 22, \"lang\": \"English\", \"words\": \"hippopotamus, Philip\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both English words come through Latin from Greek, exactly as drawn. hippopotamus is attested in English from the 1560s, from Late Latin hippopotamus < Gk. ἱπποπόταμος; it displaced Middle English ypotame (c.1300), which reached English through Old French from the same Greek word, and Old English had glossed the animal sǣhengest 'sea-horse'. Philip is Latin Philippus < Gk. Φίλιππος; Watkins's appendix lists both HIPPOPOTAMUS and PHILIP among the English descendants of ekwo-.\",\n \"derivation_fa\": \"هر دو واژهٔ انگلیسی از راه لاتین از یونانی آمده‌اند، درست همان‌گونه که در نمودار کشیده شده است. hippopotamus از دههٔ ۱۵۶۰ در انگلیسی گواهی شده، از لاتینیِ متأخر hippopotamus و آن از ἱπποπόταμος یونانی؛ این واژه جای ypotame انگلیسی میانه (حدود ۱۳۰۰، از راه فرانسویِ کهن از همان واژهٔ یونانی) را گرفت و در انگلیسی باستان این جانور را sǣhengest «اسب دریایی» می‌نامیدند. Philip از Philippus لاتینی و آن از Φίλιππος یونانی است. واتکینز در پیوست ریشه‌های هندواروپایی هر دو را زیر ekwo- می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [E_HIPPO, E_PHIL],\n \"ref_check\": [\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 433, s.v. ekwo-: '2. Greek hippos, horse: EOHIPPUS, HIPPOCAMPUS, HIPPOGRIFF, HIPPOPOTAMUS. [Pok. ekuo-s 301.]'; the current AHD appendix adds PHILIP, PHILIPPIC, XANTHIPPE.\"}\n ],\n \"consulted\": [\n  {\"src\":\"KLN\",\"where\":\"Klein s.vv. hippo-, Philip\",\"stance\":\"supports\",\"note\":\"'hippo-, ... fr. ἵππος \\\"horse\\\" ... cp. the second element in Eohippus, ephippium, Philip, Xanthippe' and 'Philip ... L. Philippus, fr. Gk. Φίλιππος'.\"},\n  {\"src\":\"web/Etymonline\",\"where\":\"etymonline.com/word/hippopotamus and /word/Philip\",\"stance\":\"supports\",\"note\":\"'Replaced Middle English ypotame (c. 1300) ... Glossed in Old English as sæhengest'; 'the from Latin Philippus, from Greek Philippos \\\"fond of horses\\\"'.\"}\n ]\n})\njson.dump(nodes, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part_d.json','w'), ensure_ascii=False)\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151d.py"
}
```


### [2026-09-05T20:50:00.394Z] TOOL RESULT

```
ok 8
```


## [2026-09-05T20:50:50.635Z] TOOL CALL #90: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151z.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nSP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\nnodes=[]\nfor p in ['part_a.json','part_b.json','part_c.json','part_d.json']:\n    nodes += json.load(open(SP+p))\nassert [n['id'] for n in nodes]==list(range(1,23)), [n['id'] for n in nodes]\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁éḱwos\"\nW_ASB = \"https://en.wiktionary.org/wiki/اسب\"\nAHD_ALF = \"https://www.ahdictionary.com/word/search.html?q=alfalfa\"\nIR_NAMES= \"https://www.iranicaonline.org/articles/personal-names-iranian-i/personal-names-iranian-ii-avestan/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Ekwos\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₁éḱwos 'horse, stallion' (Pokorny 301-302 eḱuo-s; Watkins/AHD ekwo-)\",\n \"note\": \"The root box is right on all three counts. Pokorny's lemma is 'eḱuo-s (*heḱuo-), Meaning: horse, Page(s): 301-302', so 'Indo-European Ekwos : horse, POK:301' reproduces his headword, gloss and page exactly; Watkins's appendix has 'ekwo-. Horse ... [Pok. ekuo-s 301.]'. Modern reconstruction writes it *h₁éḱwos (Wiktionary; Kapović would drop the laryngeal), traditionally explained as a derivative of *h₁oh₁ḱus 'swift', though Buck already warned that the 'root connection [is] wholly obscure'. The chart is a good one: the Iranian side (Av. aspa-, the long series of -aspa names, aspast/alfalfa, astar) and the Greek side (hippos, Philippos) are both genuine and are carried by good references — Moʿin's footnote on Borhān p.119 supplies the entire alfalfa chain in one sentence and AHD:32 supplies it again. Five corrections are needed, none of them touching the root: (1) aspa-bāra is Old Persian asa-bāra-, not Avestan; (2) Tahmāsb belongs to Av. taxma- 'brave', not to Pokorny's *Tūmāspa- 'having fat horses'; (3) Vīštāspa means 'having horses untied (for racing)' (Iranica) or, with Moʿin/Bartholomae, 'having spent horses' — 'gray' is unsupported; (4) Gošnāsp comes from Av. varəšni- 'male (ram)' as Horn says on the very page cited (HRN:206), not from aršan-; (5) Middle Persian astar is inherited from OP *asatara-, a cognate of Skt. aśvatara-, not a borrowing from Sanskrit. Two smaller points: the Avestan compound behind aspast is better reconstructed *aspa-sti- (AHD) and is not attested in the Avesta, and English alfalfa passed through Spanish. The two BQT:1819 citations on the aspa and aspa-asa boxes point to the گشتاسب page and belong to the Vīštāspa box instead.\",\n \"note_fa\": \"خودِ ریشه از هر سه جهت درست است: پوکورنی مادهٔ eḱuo-s «اسب» را در صفحات ۳۰۱–۳۰۲ آورده و واتکینز در پیوست فرهنگ American Heritage همان را با ارجاع «Pok. ekuo-s 301» تکرار کرده است؛ بازسازی امروزی *h₁éḱwos است. نمودار در کل استوار است: هم شاخهٔ ایرانی (aspa اوستایی، زنجیرهٔ نام‌های -اسپ، اسپست/الفلفه، استر) و هم شاخهٔ یونانی (hippos، Philippos) اصیل‌اند و حاشیهٔ معین بر برهان قاطع (ص ۱۱۹) تمام زنجیرهٔ «اسپست ← سریانی ← فصفصه ← الفلفه» را در یک جمله می‌آورد. پنج تصحیح لازم است و هیچ‌یک به خودِ ریشه مربوط نیست: ۱) aspa-bāra پارسی باستان (asa-bāra-) است نه اوستایی؛ ۲) «تهماسب» از taxma- اوستایی «دلیر» است نه از *Tūmāspa- «دارندهٔ اسبان فربه»؛ ۳) معنای Vīštāspa «دارندهٔ اسبان رهاشده (برای مسابقه)» یا به گفتهٔ معین و بارتولمه «اسبان از کار افتاده» است و «خاکستری» پشتوانه ندارد؛ ۴) «گشناسپ» از varəšni- اوستایی است ــ همان‌گونه که هرن در صفحهٔ ۲۰۶ که نورایی به آن ارجاع داده می‌گوید ــ نه از aršan-؛ ۵) astar پهلوی موروثی است از *asatara- پارسی باستان و هم‌ریشهٔ aśvatara- سنسکریت، نه وام‌گرفته از آن. دو نکتهٔ کوچک‌تر: بازسازی بهترِ اصلِ «اسپست» *aspa-sti- است و در اوستا گواهی نشده، و alfalfa انگلیسی از راه اسپانیایی رفته است.\",\n \"sources\": [W_PIE, W_ASB, AHD_ALF, IR_NAMES],\n \"ref_check\": [\n  {\"ref\":\"POK:301\",\"status\":\"supports\",\"note\":\"Pokorny IEW: 'Root / lemma: eḱuo-s (*heḱuo-), Meaning: horse ... Old Indie aśva-h, Avestan aspa-, Old pers. asa- \\\"horse\\\"; gr. ἵππος ... Latin equus ... References: WP. I 113 ... Page(s): 301-302' (local POK_full.txt lines 25045-25105).\"}\n ],\n \"consulted\": [\n  {\"src\":\"AHD\",\"where\":\"Watkins, AHD Indo-European Roots (AHD_watkins1985.txt line 433)\",\"stance\":\"supports\",\"note\":\"'ekwo-. Horse. Possibly originally derived from kwon-. 1. Latin equus, horse: EQUESTRIAN... 2. Greek hippos, horse: ... HIPPOPOTAMUS. [Pok. ekuo-s 301.]'\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, Indo-European Comparative Dictionary col. ~319 s.v. eḱuos (IEC.txt line 3516)\",\"stance\":\"supports\",\"note\":\"'eḱuos, ā \\\"horse; mare\\\". WP I, 113 Skt. áśvah; Av aspō, -a; OPer. asa-; Medic aspa-; Per. asb; Oss. jäfs ... Tokh. yuk, B yakwe; Arm. eš ... Lat. (Sequanian) equos; Mir. ech.'\"},\n  {\"src\":\"SYN\",\"where\":\"Buck, Selected Synonyms 3.41 'Horse'\",\"stance\":\"supports\",\"note\":\"'1. IE *ekwo-, root connection wholly obscure. Walde-P. 1.113 ... Skt. aśva-, Av., OPers. aspa- (OPers. also asa-) ... Thus the word is attested in all the main branches of the IE family except Slavic.'\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 113 (cited by both Pokorny and Mann as the source article)\",\"stance\":\"supports\",\"note\":\"not read directly (Bd. I is a poor DLI scan); both POK and IEC give 'WP. I 113' as the reference for eḱuo-s, so the Walde-Pokorny article is the standard treatment behind Nourai's POK:301.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 151,\n \"book_page\": 121,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\npath='/home/sfmqrb/git/rishe/data/verification/page-151.json'\nwith open(path,'w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\nprint(\"written\", path, os.path.getsize(path))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build151z.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-151.json > /dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 151"
}
```


### [2026-09-05T20:50:52.816Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-151.json 74787
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 7, 'confirmed': 10, 'disputed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 12, 'not_checked': 12, 'not_found': 3, 'partial': 5, 'contradicts': 2}
books consulted: {'supports': 38, 'partial': 14, 'contradicts': 3, 'silent': 2} | by book: {'HRN': 8, 'KLN': 7, 'BRT': 5, 'HUB': 5, 'web/Etymonline': 5, 'PHD': 3, 'POK': 3, 'web/Iranica': 3, 'BQT': 3, 'MON': 3, 'SYN': 2, 'NYB': 2, 'AHD': 2, 'PLA': 2, 'LKT': 2, 'KNT': 1, 'web/Iranica+Wikipedia': 1}
```


## [2026-09-05T20:50:58.280Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'PY'\nimport json\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: idx.add(json.loads(line)['url'])\n    except: pass\nd=json.load(open('data/verification/page-151.json',encoding='utf-8'))\nused=set()\ndef collect(o):\n    for s in o.get('sources',[]): used.add(s)\ne=d['entries'][0]; collect(e)\nfor n in e['nodes']: collect(n)\nmiss=[u for u in used if u not in idx]\nprint(\"used\",len(used),\"missing\",miss)\nPY\npython3 tools/verify_check.py 151 | grep -i problem; echo \"exit=$?\""
}
```


### [2026-09-05T20:51:00.225Z] TOOL RESULT

```
used 16 missing []
exit=1
```


## [2026-09-05T20:51:17.224Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-151.json` written; `verify_check.py 151` shows 22/22 nodes, 0 PROBLEM lines.

**Page 151 (book p.121), one entry: PIE *Ekwos "horse" — root confirmed** (Pokorny 301-302 *eḱuo-s*; Watkins/AHD; Mann; Buck).
Node verdicts: 10 confirmed, 7 plausible, 5 disputed.

Disputed:
- **#5 Tahmāsb** — from Av. *taxma-* "brave" (Iranica no. 304), not from Pokorny's *Tūmāspa-* "having fat horses"; Nourai conflated two Avestan names.
- **#4 višta-aspa "gray or old horses"** — Iranica: Vīštāspa- "possessing horses untied (for racing)"; Moʿin/Bartholomae (Borhān p.1819): "spent, worn-out horses". "Gray" is unsupported.
- **#6 jām-âspa "owning horses"** — first element admittedly obscure (kṣāmá- "singed" / Gershevitch "leading" / Schwartz "bridling"); also *aršan-aspa-* is not a Bartholomae headword.
- **#7 Gošnāsp** — from Av. *varəšni-* "male (ram)" (*w- > g-, cf. *vəhrka- > گرگ); **Horn p.206, the page Nourai himself cites, says exactly this** and names Gušnasp.
- **#16 Pahlavi astar ← Sanskrit** — wrong direction: MP *astar* < OP \*asatara- (Hübschmann, Wiktionary); Skt. *aśvatara-* is a cognate, not the source.

No transcription errors: the printed page (rendered at 400 dpi, copied to `sources/refs/ocr/BOOK/151.png`) matches the JSON exactly, Persian script included (لهراسب، جاماسب، ارجاسپ…). Nothing for the owner to fix in the data.

Reference notes: BQT:119 is a bullseye — Moʿin's footnote there gives the whole aspast → Syriac → فصفصه → alfalfa chain, matching AHD:32 (which adds the Spanish step Nourai omits). BQT:1819 on nodes #1/#8 is misplaced (it is the گشتاسب page, belonging to #4/#5), POK:1082 on #6 is copied over from #4, and HRN:206 on #4 is likewise the Gušnasp page. DVS:42, AEF:324, MON5:419 and MON personal names are not accessible in any copy.
