# Verification process log — verify-page-132


## [2026-09-05T20:02:45.653Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 132 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-132.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-132.json. Write /home/sfmqrb/git/rishe/data/verification/page-132.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 132` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:02:47.435Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:02:48.194Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:02:48.208Z] TOOL RESULT

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


## [2026-09-05T20:02:48.260Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-132.txt"
}
```


### [2026-09-05T20:02:48.279Z] TOOL RESULT

```
1	=== PDF page 132 (book page 102) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dheye : to see  (refs POK:243)
4	#1 (parent #0) [Avestan] refs=POK:243; BQT:373,910; SOD:421 | dâ 3, dây, dâi, dî : to see ; vaěna 2 : observer ; upa-dîta : apparent ☞Upo ; daěman : eye
5	  #2 (parent #1) [Pahlavi] refs=BQT:74,373,910 | dîtan : to see ; âděnak : mirror ; pa-dît : apparent ; děmân : appearance | NOTE: HUB:38 claims "pa-dit" was first formed in Pahlavi.
6	    #3 (parent #2) [Persian] refs=BQT:74,910,915 | dîdan «دیدن» : to see ; dîm, dîmeh «دیم، دیمه» : light | extra: آینه ، پدید ، پدیدار ، پدیده
7	#4 (parent #0) [Old Persian] refs=KNT:191; AEF:322; FFD:55 | dî, dây, wai, vâe : to see ; vâe-na, vaina : observer ; vainâhiy : if I see ; věn-am, vaenâmi : I see ; adhi-vaina : ornament
8	  #5 (parent #4) [Pahlavi] refs=BQT:340 | věn-âk, věn-âg : one sees ; adhvěnak : ornament
9	    #6 (parent #5) [Persian] refs=BQT:29,340; SNS:291; AEF:80 | bînâ «بینا ( بینش )» : one who sees ; âzîn «آذین» : ornament ; âîn «آیین ( هر آیینه )» : ceremony, customs ; âdîneh «آدینه» : day of "ornaments", Friday | extra: بین ، دوربین ، ذرّه بین | NOTE: SOG:17 derives "âzîn" from "âzîdan:to sew".
10	#7 (parent #0) [Sanskrit] refs=POK:243 | dhi : to see, to think ; dhyânah : seeing mentally
11	  #8 (parent #7) [Pahlavi] refs=BQT:558 | gyân, jân : soul
12	    #9 (parent #8) [Persian] refs=HUB:49; BQT:558 | jân «جان ( جانور )» : soul, life | NOTE: HRN:93 derives this from AV "dhay:to see"
13	#10 (parent #0) [Avestan / Old Persian] refs=POK:243; KNT:191; FFD:33 | dais : to show, think ; ham-dais-a : to think ☞Sem 1
14	  #11 (parent #10) [Pahlavi] refs=FFD:33 | handěš : thought
15	    #12 (parent #11) [Persian] refs=FFD:33 | andîšîdan «اندیشیدن» : to think | extra: اندیشه ، اندیش ، اندیشمند
16	#13 (parent #0) [Avestan] refs=POK:243 | daěna : insight, religion
17	  #14 (parent #13) [Pahlavi] refs=BQT:916 | dîn : religion
18	    #15 (parent #14) [Persian] refs=BQT:916; MON:1597; FSF:191 | dîn 1 «دین ۱» : religion
19	    #16 (parent #14) [Arabic] refs=BQT:916; FVQ:131 | dîn 1 : religion | NOTE: FVQ:132 claims Arabic borrowed "dîn 1" from Iranian and "dîn 2: judgment day" from Aramaic. See root "Dînu".
20	      #17 (parent #16) [Persian] refs=FVA:148 |  «ادیان ، دیانت» ;  «تدیّن ، متدیّن»
21	#18 (parent #0) [Sogdian] refs=SOD:148,421 | wyn : to see ; dyn, dynh : religion ; dyn-d`r : religious
22	#19 (parent #0) [Greek] refs=POK:243; AHD | sema : things seen, signs
23	  #20 (parent #19) [Arabic] refs=VDQ:275 | sîmâ : sign, symbol
24	    #21 (parent #20) [Persian] refs=MON:1983 | sîmâ «سیما» : sign, face
25	  #22 (parent #19) [English] refs=AHD | semantics
26	
```


## [2026-09-05T20:02:51.690Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-132.json | head -200",
 "description": "Read source JSON for page 132"
}
```


### [2026-09-05T20:02:51.737Z] TOOL RESULT

```
{
  "pdf_page": 132,
  "book_page": 102,
  "entries": [
    {
      "root": {
        "name": "Dheye",
        "lang": "Indo-European",
        "refs": "POK:243",
        "gloss": "to see"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:243; BQT:373,910; SOD:421",
          "words": [
            {"translit": "dâ 3, dây, dâi, dî", "gloss": "to see", "script": null},
            {"translit": "vaěna 2", "gloss": "observer", "script": null},
            {"translit": "upa-dîta", "gloss": "apparent", "script": null, "see": ["Upo"]},
            {"translit": "daěman", "gloss": "eye", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:74,373,910",
          "words": [
            {"translit": "dîtan", "gloss": "to see", "script": null},
            {"translit": "âděnak", "gloss": "mirror", "script": null},
            {"translit": "pa-dît", "gloss": "apparent", "script": null},
            {"translit": "děmân", "gloss": "appearance", "script": null}
          ],
          "script_extra": null,
          "note": "HUB:38 claims \"pa-dit\" was first formed in Pahlavi.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:74,910,915",
          "words": [
            {"translit": "dîdan", "gloss": "to see", "script": "دیدن"},
            {"translit": "dîm, dîmeh", "gloss": "light", "script": "دیم، دیمه"}
          ],
          "script_extra": "آینه ، پدید ، پدیدار ، پدیده",
          "note": null,
          "quote": {
            "text": "بدانگه که صبح زمان دیمه داد - زراتشت فرّخ ز مادر بزاد",
            "poet": "Zartosht-Nâmeh"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:191; AEF:322; FFD:55",
          "words": [
            {"translit": "dî, dây, wai, vâe", "gloss": "to see", "script": null},
            {"translit": "vâe-na, vaina", "gloss": "observer", "script": null},
            {"translit": "vainâhiy", "gloss": "if I see", "script": null},
            {"translit": "věn-am, vaenâmi", "gloss": "I see", "script": null},
            {"translit": "adhi-vaina", "gloss": "ornament", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "BQT:340",
          "words": [
            {"translit": "věn-âk, věn-âg", "gloss": "one sees", "script": null},
            {"translit": "adhvěnak", "gloss": "ornament", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:29,340; SNS:291; AEF:80",
          "words": [
            {"translit": "bînâ", "gloss": "one who sees", "script": "بینا ( بینش )"},
            {"translit": "âzîn", "gloss": "ornament", "script": "آذین"},
            {"translit": "âîn", "gloss": "ceremony, customs", "script": "آیین ( هر آیینه )"},
            {"translit": "âdîneh", "gloss": "day of \"ornaments\", Friday", "script": "آدینه"}
          ],
          "script_extra": "بین ، دوربین ، ذرّه بین",
          "note": "SOG:17 derives \"âzîn\" from \"âzîdan:to sew\".",
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:243",
          "words": [
            {"translit": "dhi", "gloss": "to see, to think", "script": null},
            {"translit": "dhyânah", "gloss": "seeing mentally", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": "BQT:558",
          "words": [
            {"translit": "gyân, jân", "gloss": "soul", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "HUB:49; BQT:558",
          "words": [
            {"translit": "jân", "gloss": "soul, life", "script": "جان ( جانور )"}
          ],
          "script_extra": null,
          "note": "HRN:93 derives this from AV \"dhay:to see\"",
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:243; KNT:191; FFD:33",
          "words": [
            {"translit": "dais", "gloss": "to show, think", "script": null},
            {"translit": "ham-dais-a", "gloss": "to think", "script": null, "see": ["Sem 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Pahlavi",
          "refs": "FFD:33",
          "words": [
            {"translit": "handěš", "gloss": "thought", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "FFD:33",
          "words": [
            {"translit": "andîšîdan", "gloss": "to think", "script": "اندیشیدن"}
          ],
          "script_extra": "اندیشه ، اندیش ، اندیشمند",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:243",
          "words": [
            {"translit": "daěna", "gloss": "insight, religion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Pahlavi",
          "refs": "BQT:916",
          "words": [
            {"translit": "dîn", "gloss": "religion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
```


## [2026-09-05T20:02:52.438Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ && sed -n '1,80p' tools/verify_check.py",
 "description": "List verification dir and check script"
}
```


### [2026-09-05T20:02:52.506Z] TOOL RESULT

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


## [2026-09-05T20:02:56.679Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '200,400p' data/extracted/batch/page-132.json; echo ---; python3 -c \"\nimport json;d=json.load(open('data/extracted/batch/page-132.json'));print(len(d['entries']));\nfor e in d['entries']: print(e['root'], len(e['nodes']))\"",
 "description": "Rest of source JSON"
}
```


## [2026-09-05T20:02:57.477Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '80,200p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-05T20:02:59.868Z] TOOL RESULT

```
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Persian",
          "refs": "BQT:916; MON:1597; FSF:191",
          "words": [
            {"translit": "dîn 1", "gloss": "religion", "script": "دین ۱"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بیاموز آیین و دین بهی - که بی دین ناخوب باشد مهی",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 16,
          "parent": 14,
          "lang": "Arabic",
          "refs": "BQT:916; FVQ:131",
          "words": [
            {"translit": "dîn 1", "gloss": "religion", "script": null}
          ],
          "script_extra": null,
          "note": "FVQ:132 claims Arabic borrowed \"dîn 1\" from Iranian and \"dîn 2: judgment day\" from Aramaic. See root \"Dînu\".",
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Persian",
          "refs": "FVA:148",
          "words": [
            {"translit": null, "gloss": null, "script": "ادیان ، دیانت"},
            {"translit": null, "gloss": null, "script": "تدیّن ، متدیّن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:148,421",
          "words": [
            {"translit": "wyn", "gloss": "to see", "script": null},
            {"translit": "dyn, dynh", "gloss": "religion", "script": null},
            {"translit": "dyn-d`r", "gloss": "religious", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:243; AHD",
          "words": [
            {"translit": "sema", "gloss": "things seen, signs", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Arabic",
          "refs": "VDQ:275",
          "words": [
            {"translit": "sîmâ", "gloss": "sign, symbol", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Persian",
          "refs": "MON:1983",
          "words": [
            {"translit": "sîmâ", "gloss": "sign, face", "script": "سیما"}
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
            {"translit": "semantics", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
---
1
{'name': 'Dheye', 'lang': 'Indo-European', 'refs': 'POK:243', 'gloss': 'to see'} 22
```


### [2026-09-05T20:02:59.906Z] TOOL RESULT

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
```


## [2026-09-05T20:03:41.299Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'));\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][2],ensure_ascii=False,indent=1))\n\"",
 "description": "Sample previous verification style"
}
```


## [2026-09-05T20:03:41.583Z] TOOL CALL #8: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:03:44.326Z] TOOL RESULT

```
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
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
   "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
   "stance": "silent",
   "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
  }
 ]
}
{
 "id": 1,
 "lang": "Avestan",
 "words": "dam; da-dhmainya",
 "verdict": "plausible",
 "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
 "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root."
  }
 ],
 "consulted": [
  {
   "src": "BRT",
   "where": "Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)",
   "stance": "partial",
   "note": "'j. däSmainya- Adj. \"sich aufblasend, -blähend\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \"er bläst\", np. damidan \"blasen\"' — supports the root and the link to Persian, but shows the form is a participle, not '1sg I inflate'; and Bartholomae has no Avestan verb entry dam- 'to blow' (his dam- entries are 'Haus, Wohnung' and a present stem of dar- 'to hold')."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*AVESTAN: Y Av. daδmainiia- \"blowing up (intr.)\" (V 14.5, V 18.73)' listed as the only Avestan reflex of *damH³."
  },
  {
   "src": "WLD",
   "where": "Bd. I 851 f.",
   "stance": "supports",
   "note": "'av. dadmainya- \"sich aufblasend, blähend, von Fröschen\" (siehe Bartholomae Airan. Wb. 731 f.)'"
  }
 ]
}
{
 "id": 3,
 "lang": "Germanic",
 "words": "",
 "verdict": "confirmed",
 "derivation": "An empty pass-through box: it stands for the Germanic branch of the root, which Pokorny sets out on p.248 as three parallel enlargements of dhem- — with -p-: MHG dimpfen, dampf 'dampfen, rauchen', OHG/MHG dampf 'Dampf, Rauch', MDu./Eng. damp 'Dampf, feuchter Nebel'; with -b-: Swed. dial. dimba 'dampfen, rauchen', ON dumba 'Staub, Staubwolke'; and with -mm-: ON dimmr, OFris./OE dimm 'dunkel', OHG timber. In modern terms Proto-Germanic *dimbaną 'to smoke, fog', whence the noun/adjective *dampaz 'vapour, damp'. The box carries no reference of its own and asserts nothing beyond 'Germanic continues the root', which Pokorny and Walde-Pokorny both state.",
 "derivation_fa": "این جعبهٔ خالی تنها نشان‌دهندهٔ شاخهٔ ژرمنی ریشه است. پوکورنی در صفحهٔ ۲۴۸ سه گسترشِ موازیِ ریشهٔ dhem- را در ژرمنی برمی‌شمارد: با -p- (آلمانی میانه dimpfen «دود کردن»، dampf «بخار، دود»، هلندی میانه و انگلیسی damp)، با -b- (سوئدیِ گویشی dimba «دود کردن»، نورس کهن dumba «گرد و غبار») و با -mm- (نورس کهن dimmr، فریزیِ کهن و انگلیسیِ کهن dimm «تاریک»، آلمانیِ کهن timber). به زبانِ امروزی: ژرمنیِ آغازین *dimbaną «دود کردن» و از آن نام/صفتِ *dampaz «بخار، نمناک». این گره ارجاعی ندارد و ادعایی جز «ژرمنی دنبالهٔ این ریشه است» نمی‌کند، و همین را پوکورنی و والده-پوکورنی هر دو تأیید می‌کنند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/dampaz"
 ],
 "ref_check": [
  {
   "ref": "(none)",
   "status": "not_checked",
   "note": "the box carries no reference in the printed chart; the claim is covered by the POK:248 citation on the English node below."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 248 (POK_01.txt lines 3524-3530)",
   "stance": "supports",
   "note": "'mit germ. -p-: mhd. dimpfen, dampf ,dampfen, rauchen', ahd. mhd. dampf m. ,Dampf, Rauch', mnd. engl. damp ,Dampf, feuchter Nebel'' … 'mit germ. -b-: schwed. dial. dimba … anord. dumba ,Staub, Staubwolke' (daneben mit -mm- anord. dimmr ,dunkel', afries. ags. dimm ds. … ahd. timber)'."
  },
  {
   "src": "WLD",
   "where": "Bd. I 851 f.",
   "stance": "supports",
   "note": "same Germanic material ('norw. daam (*dhemo-) „dunkel“, daame m. „Wolkenschleier“ … anord. dǫkk …') listed under dhem-."
  }
 ]
}
```


### [2026-09-05T20:03:44.361Z] TOOL RESULT

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


## [2026-09-05T20:03:48.841Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dhei̯\" POK_01.txt | head -20; echo \"=== search dheia\"; grep -n \"dhei\" POK_01.txt | sed -n '1,40p'",
 "description": "Grep Pokorny for dhei root"
}
```


### [2026-09-05T20:03:48.909Z] TOOL RESULT

```
=== search dheia
794:Ai.  rädhnöti,  rädhyati  ;macht  (passend)  zurecht;  bringt  zustande;  gerät; gelingt;  hat  Glück  womit;  befriedigt;  gewinnt  jemanden';  rädhayati  ;bringt zustande;  befriedigt';  rädha-h  m.,  rädhah  n.  ;Segen;  Gelingen;  Wohltat, Gabe;  Freigebigkeit';  av.  rädaiti  ;macht  bereit',  rada-  m.  ;Fürsorger'; rädah-  n.  , Sichbereitstellen,  Bereitwilligkeit  (in  religiöser  Hinsicht)',  apers. rädiy  (Lok.  Sg.)  , wegen'  (vgl.  aksl.  radi  s.  unten),  npers.  äräyad,  ärästan ,schmücken';  air.  imm-rädim  ;überlege;  überdenke';  acynir.  amraud  ;mens'; ncymr.  amrawdd  ;Gespräch'  mit  ders.  Bed.  wie  air.  no-räidiu,  no-rädi^n jSage',  mcjmr.  adrawd  ,erzählen'  und  got.  rödjan^  anord.  reda  ,reden^ (vgl.  auch  oben  nhd.  Rede,  reden]  no-räidiu  und  rödjan  setzen,  wie  sL, raditi,  ein  kaus.-iter.  *rödheiö  fort);  got.  garedan  ,worauf  bedacht  sein, Vorsorge  treffen',  urredan  ,urteilen,  bestimmen'  (vgl.  zur  Bed.  bes.  lat. rerl),  undredan  , besorgen,  gewähren',  ahd.  rätan  , raten,  beratschlagen, worauf  sinneu;  anstiften,   deuten  (Rätsel),    auffordern,  wofür  sorgen,  ver-
2714:Ein  Zusammenhang  mit  dheig-  ,stechen'  ist  nicht  nachweisbar.
3354:Über  dhäu-  , staunen^  s.  u.  dheid-,
3421:äbS(i)'  (daneben  dh-ei-  ?)  .saugen,  säugen'  ( :  c?Äai-.  dJvt-  und  dhe-j  dhd-)  s. bes.  Schulze  KZ.  27.  425  =  Kl.  Sehr.  363.  Nominalbildungen:  dhe-lä .Mutterbrust',  dhi-lo-  , Zitze',  dbe-lu-  .säugend'.  dbQi-l-  ds.,  dhei-nä .trächtig',  dhe-nä  .Fruchtertrag',  dhedhn-  .(saure)  Milch'. Ai.  dhäya-h  .ernährend,  pflegend',  dhäyas-  n.  .das  Saugen',  dhäyü-  .durstig'. dhätave    .zu    saugen',    Fut.  dhäsyati,    i^or.    ddhät   ,er    sog',    su-dhä    .Saft, Nektar',  dhätrl  .x4mme.  Mutter',  dhenü-  f.  .milchend'  =  av.  daenu-  .Weib- chen von  vierfüßigen  Tieren',  ai.  dJiBnä  .Milchkuh',  ablaut.  dhud-  .gesogen*^, Perf.  Plur.  1.  3.  da-dhi-md  (i  =  »),    da-dh-üh]   redupl.   Nomen    da-dh-an-j Nom.  dd-dh-ij  Gen.  dadhnds  .saure  Milch'  (:  apr.  dadaUj  alb.  djathej'j
3433:Lat.  felix  , fruchtbar,  glücklich'  zu  feläre  geht  auf  ein  fem.  Subst. *fell-c-  ,die  säugende  =  fruchtbare'  zurück,,  nach  Specht  (KZ.  62,  237) aus  '^felui-k-s,  Femin.  zu  ai.  dhäru-,  gr.  d-fjXvg',  lat.  fecundus  ,fruchtbar^, fetus,  -üs  ,das  Zeugen,  Gebären',  feta  , schwanger,  trächtig',  auch  ,was geboren  hat',  effeta  , durch  vieles  Gebären  geschwächt',  fenus,  -oris  , Er- trag, Zinsen,  Wucher',  vielleicht  auch  fenum  ,Heu'  (als  , Ertrag')  erklären sich  aus   einer  Sonderanwendung  von   dhei-  , säugen'  für  , fruchtbar  sein';
3450:dheigh'   ,Lehm  kneten  und  damit  mauern  oder  bestreichen  (Mauer,  Wall-
3452:kneten  (Bäckerei)';  dhij-ii-io-s  , Former';   dheigho-s,  dhoigbo-s  ßa^
3463:lat.  fingö,  -ere,  finad,  fictum  ,eine  Masse  gestalten,  bilden,  formen;  er- dichten; streichelnd  betasten',  /^wZws  , Töpfer'  (:  germ.  *dizidaz),  filum {*figslom)  , Gestalt',  effigies  ,(plastisches)  Abbild',  figüra  ,Bildung,  Gestalt, Figur',  fictiö  ,das  Bilden,  Formen;  Bildung,  Gestaltung,  Erdichtung*, fictilis]  ,aus  Ton  gebildet,  irden,  tönern'  (zum  lat.  g  statt  h  s.  Leumana Lat.  Gr.  133;  nach  letzterem  stammt  aus  Formen  wie  fictus  auch  das  Ä  von altfalisk.  fifiked  ,finxit',  osk.  fifikus  etwa  ,du  wirst  ausgedacht  habenOr" wahrscheinlich  umbr.  fikla,  ficlam  ,fitillam,  libum',  lat.  fltilla  ,Opferbrei, Opfermus'  (mit  dial.  t  aus  et))  osk.  feihüss  ,muros'  (*dheigho-)]
3481:Eine  Parallelwz.  *dheig-  sucht  Wood  Mod.  Phil.  4,  490  f.  in  mhd.  flehen jSchaffen  usw.';  ags.  diht{i)an  ,dictare',   ahd.  tihtön  ,erfinden  und  schaffen; dichten'  stammen  aus  spätlat.  dlctäre. \yP.  I  833  f.,  WH.  I  501  f.  507.
3511:Ags.  dolg  n.,  alid.  tolc,  tolg,  dolg  n.  _,Wunde^  (;*Schlag^),  anord.  dolg  n. ,Feindschaft^_,  dolgr  ,Feind^,  dylgja  ^Feindschaft^,  wozu  wohl  ndd.  dalgen, daljen  jSchlaLgen^  (entlehnt  norw.  mdartl.  dalga  ds.),  nhd.  (hess.-nassauisch, ostpreuß.)  dalgen,  talken  ,prügeln,  schlagen'^,  mhd.  talgen  ,kneten^  Nach Havers  KZ.  43,  231,  IF.  28,  190  ff.  wäre  auch  für  gr.  Mlyw  ,bezauhere, betöre  usw.^,  d-shATcog,  d^el'ArrJQy  -d-eXycTi^Qiog  ,bezaubernd,  verlockend^,  d^eX^ig .  ,Bezauberung^  (idg.  *dhelg-  neben  *dhelgh-?)  die  Grundbed.  ,Bezauberung durch  Schlagt  wahrscheinlich,  so  wie  auch  die  TeXxlveg,  OsXytveg  durch einen  Schlag  die  Gesundheit  der  Menschen  schädigende  Dämonen  und zugleich  Schmiede  waren.  Alles  ganz  unsicher.  Eher  könnte  noch  toch.  A talke  n.,  B  telki  ,Opfer^  dazugehören.
3559:Air.  dingid,  for-ding  ,unterdrückt'  (s.  auch  dheigh-)'^  vgl.  Pedersen II  506;
3718:Arm.  di'Jt  , Götter*  (PI.  *dheses)',  lat./eWae  (alat. /esiae)  ,Tage,  an  denen keine  Geschäfte  vorgenommen  wurden,  Feiertage*,  festus  ,f estlich,  feier- lich, ursprüngl.  von  den  der  religiösen  Feier  gewidmeten  Tagen',  osk. fiisnam  Akk.  ,templum',  umbr.  fesnaf-e  ,in  fanum'*,  tiefstufig  lat.  fänum {*fas-no-m)  , heiliger,  den  Göttern  geweihter  Ort'  und  ai.  dhisnya-  , an- dächtig, fromm,  heilig'  (unsicherer  dhisanyant-  u.  dgl.,  s.  unter  dheid- , sehen');  über  gr.  d-eog  ,Gott'  s.  unter  dheues-,  über  lat.  fäs,  fästus  oben S.  105f.
```


## [2026-09-05T20:03:51.084Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find page containing 'sehen, schauen'\nfor i,p in enumerate(pages):\n    if 'schauen' in p and ('dhei' in p or 'dhi' in p or 'dhy' in p):\n        print('---',i, p[:200].replace('\\n',' | '))\nEOF",
 "description": "Find Pokorny page with sehen schauen"
}
```


### [2026-09-05T20:03:53.150Z] TOOL RESULT

```
364
--- 48 ohin),  gegen,  über— hin^, als  Präf.  ,nach;  von— weg^  (s.  auch  Bezzenberger  KZ.  44,  304);  aksl.  na m.  Akk.  und  Lok.  ,auf— hin;  auf,  an^  (dazu  nach  pre  :  pre-d^  neugebildet na-d
--- 253 iuf,  filiu  ,lactantes';   mir.  del  , Zitze'  (*dhi-lo-),  delech  ,Milchkuh',  danT dcel  , Milchdrüsen  oder  Euter  bei  der  Sau',  schwed.  mdartl.  del  m.  jZitze*^ ahd.  tila  f.  ,weiblich
--- 254 .  (Gr.)   , Gedanke';   dhi-h,  Akk. Jjy^am  ,Gedanke,  Vorstellung,  Einsicht,  Verstand,  religiöses  Nachdenken, Andacht',  dhl-ti-  ,Wahrnehmung,  Gedanke,  Andacht',  dhira-  ,sehend,  klug, wei
```


## [2026-09-05T20:03:58.995Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (253,254,255):\n    print('=========== page idx',i)\n    print(pages[i][:3000])\nEOF",
 "description": "Print Pokorny pages around dheia"
}
```


### [2026-09-05T20:04:01.361Z] TOOL RESULT

```
=========== page idx 253
iuf,  filiu  ,lactantes';   mir.  del  , Zitze'  (*dhi-lo-),  delech  ,Milchkuh',  danT dcel  , Milchdrüsen  oder  Euter  bei  der  Sau',  schwed.  mdartl.  del  m.  jZitze*^ ahd.  tila  f.  ,weibliche  Brust',  ags.  delu  f.  ,Brustwarze,  Zitze',  anord.  dilkrl ,Lamm,   Junges';   lett.   dels   ,Sohn',  dele    ,Blutegel',    lit.  dele    ds.,  pirmdell '^ ,die  zum  ersten  Male  geboren  hat',  pirmdelys  ,was  gerade  geboren  worden ist';  lett.  dile  ,saugendes  Kalb',  dllit  ,säugen'.
Ob  gr.  d^tjad-ai  {^d^wisad-ai) , schmausen',  d^oivi]  ,Schmaus'  (aus  *d-(x}L-vG?) mit  Abtönung  hierher  gehöre,  ist  fraglich;  ob  d-Co^ai  und  (dor.)  d-a^ai ^lied-vaai^  als  ^d^oia'/.-(Jai  auf  eine  leichte  Wz.  *dhÖi-  (ebenso  dann  d^oirt]] auch  d'üJa-d'aL  kann  d-oia-od-ai  sein)  weisen?
Lat.  felix  , fruchtbar,  glücklich'  zu  feläre  geht  auf  ein  fem.  Subst. *fell-c-  ,die  säugende  =  fruchtbare'  zurück,,  nach  Specht  (KZ.  62,  237) aus  '^felui-k-s,  Femin.  zu  ai.  dhäru-,  gr.  d-fjXvg',  lat.  fecundus  ,fruchtbar^, fetus,  -üs  ,das  Zeugen,  Gebären',  feta  , schwanger,  trächtig',  auch  ,was geboren  hat',  effeta  , durch  vieles  Gebären  geschwächt',  fenus,  -oris  , Er- trag, Zinsen,  Wucher',  vielleicht  auch  fenum  ,Heu'  (als  , Ertrag')  erklären sich  aus   einer  Sonderanwendung  von   dhei-  , säugen'  für  , fruchtbar  sein';
dazu  aber  nicht  *dhönä-  , Getreide'  :  ai.  dhänäh  f.  PL  , Getreidekörner', dhänyd-  n.  , Getreide',  np.  däna  ,Korn',  av.  dänö-karsa-  ,eine  Ameisenart', d.  i.  , Körner  (=  Ameiseneier)  schleppend',  toch.  B  tano  ,Getreide'  und lit.  ddona,  lett.  duona  f.  ,Brot'  (ursprüngl.  , Getreide',  alit.  , Ausgedinge'); dor. -illyr.  (kret.)  ÖTjal  .  .  .  ai  KQid^ai  EM.,  örjTTcci'  al  inTLGf.i€vaL  xQi&ai (*c?Äe-Ä;-ia-)  Hes.;  anders  Jokl  bei  WH.  I  475;
s.  auch  oben  1.  dhe-,  dhe-dhe-.
WP.  I  829  ff.,  WH.  I  474  ff.,  864,  Trautmann  51.
245
.  rihiä-  :  dhi-  .sehen,  schauend -     *Ai.    ddldhet   ,Qr    schaute',    PL    dldUmah,    Med.   didhye,    ddldkUa,    Konj. thdhayat  (vielleicht  zum  Präs.  umgewandeltes  Perf.,  vgl.  Perf.  dldliaya)'^ jf^ya-th  dhyä-ya-ti  (lO-Präs.)  ^schaut  im  Geiste,  d.  i.  denkt,  sinnt',  Partiz. »j^yj.^rt-und  dhi-tä-,  dhyä  ,das  Denken,  Sinnen',  dhyä-tar- , Denker^,  dJiyä-na- „    ,das   Sinnen,   Nachdenken',   dhyäman-  n
=========== page idx 254
.  (Gr.)   , Gedanke';   dhi-h,  Akk. Jjy^am  ,Gedanke,  Vorstellung,  Einsicht,  Verstand,  religiöses  Nachdenken, Andacht',  dhl-ti-  ,Wahrnehmung,  Gedanke,  Andacht',  dhira-  ,sehend,  klug, weise,  geschickt',   avadhlrayati  ,verschmäht  (despicit),  weist  zurück,  ver- achtet', prakr.  herai  ,sieht';  s-Bildung  ai.  dhiyasänd-  ,auf merksam,  achtsam'; vermutlich  auch  dhisdna-.  wenn  ,verständig,  klug',  dhisanyant-  wenn  ,auf- jncrksam,    andächtig',   dhisd   Instr.  Adv.  wenn   ,mit  Andacht,   Eifer   oder Lust',  doch  vgl.  andererseits  das  zu  lat.  festus,  fänum,  idg.  dhes-  , religiös' 5.  gehörige  dhisnya-  ,andächtig';  .
.'•  av.  dä{y)-  ,sehen',  z.  B.  ä-diöäHi  ,betrachtet',  daiSyantö  Nom.  PI.  Partiz. i  dio  sehenden'  (usw.,  s.  Bartholomae  Airan.  Wb.  724);  Partiz.  paiti-dlta- "  ,erblickt',  -diti-  f.  ,das  Erblicken',  dä^a-  ,einsichtig,  klug'  (dehnstufig  wie \,-diöäHi),  -dä{yy,  -dl-  f.  als  2.  Kompositionsglied  , Sehen,  Blick;  Einsicht, '..Absicht';  -däman-  ,Absicht';  fZaemaw-  n.  ,Auge,  Augapfel;  Blick',  döid-ra- ,  n.  ,Auge',    daenä    ,Religion'    und   ,inneres  Wesen,   geistiges.  Ich';    npers.
dldan  ,sehen',  dlm  , Gesicht,  Wange'; t       gr.  ofn-ia^   dor.   oäna  , Zeichen,   Kennzeichen,    Merkmal  usw.'  (*dJiiä-mn mss  ai.  dhyäman-]  Lit.  bei  Boisacq  s.  v.,  vgl.  Schwyzer  Gr.  Gr.  I  322;  nach rYj»  Leumann  [Abb.  Kunde  d.  Morgenl.  20,   1,  S.  96]  vielmehr  zu  sakisch i^dma  , Zeichen'),  arj^alvü)  , mache  durch  ein  Zeichen  kenntlich  usw.^; alb.  diturej  ditme  ,Weisheit,  Gelehrsamkeit',  dinak  ,listig'. Auf  ein  bedeutungsgleiches  ^dhäu-  geht  zurück:
Gr.  d-avfia  ,was  Bewunderung,  Staunen  erregt;  Bewunderung,  Staunen* {*dhdu-mn)  ^av(.id^(ü  , erstaune,  verwundere  mich,  bewundere',  woneben mit  Abtönung  ■d-aj(v)fj,a',  vgl.  böot.  Q(x}f.icüVj  dor.  Qo)(.idvTag  (Lit.  bei  Boisacq u.  -d-avf.ia]  über  d^^ßog'  d^av^ia  Hes.  wohl  d-fjJ^ogy  s.  Boisacq  u.  d-dfißog  m. Lit.);  att.  d^ea  ,das  Anschauen,  Anblick;  Schauspiel'  aus  *d'äSa,  vgl.  syrak. ^aa,  ion.  O^rjsoi^iaiy  dor.  ^äeofiac  , betrachte'  (att.  d'edofxai  nach  d^ea  um- gebildet), usw.,  s.  Boisacq  u.  d^sä  und  S^scogög  (zu  letzterem  noch  Ehrlich KZ.  40,  354  Anm.  1).  Außergr.  Entsprechungen  fehlen. WP.  I  831  f.,  Schwyzer  Gr.  Gr.  I  349,  523.
dhSigli-  :  dhöig^-  :  dhig^-  ,stechen,  stecken,  festsetzen'.
Ijüt.  figö,  -ere  , heften,  anheften;  festsetzen;  hineinstecken'  (urlat.  i,  vgl. flgiei'  S.  C.  Bacch.),  alat.  flvö,  umbr.  fiktu  ,figitö',  afiktu  ,infigitö';   wahr-
16*
244
scheinlich  dazu  als  ^festgestecktes^  auch  flnis  , Grenze^  Ziel,  Ende'  ( dygsnis  , Stich'),  vgl.  finiö,  -Ire  auch  , festsetzen,  bestimmen';
=========== page idx 255

ags.  die  , Abzugsgraben,  KanaP,  ndd.  dlk,  aisl.  dik{i)nj  mhd.  tlchj  worau^ nhd.  Deich,  Teich,  eigentlich  ,Ausstich^
lit.  dygstu,  dygti,  lett.  digt  ,keimen'  (eigentlich  ,hervorstechen',  lit.  dy^ ,spitzig,   stachelig'),    dazu  dygiit,  dygUi  ,stechenden  Schmerz   empfind' dyglys  ,Dorn',  dyge  , Stachelbeere',  apr.  digno  , Schwertgriff'  (wie  nhd.  fi; ,  Seh  wertgriff',    d.  h.  ,  worin    die   Klinge   eingeheftet  ist,    zu  heften)'^  J^, stufig  lit.  diegiu^  diegti,  lett.  diegt  ,stechen',  lit.  diegas  ,Keim',  apr.  dei ,Stätte',    ursprüngl.  ,Punkt,    Stich';   mit   öi:   lit.    ddigas    ,Keim,    Setzli ddiktas  , Punkt;  Sache',  daigmti  ,keimen  machen';
WP.  I  832 f.,  WH.  I  495 f.,  865;  Trautmann  49 f.
dheigh'   ,Lehm  kneten  und  damit  mauern  oder  bestreichen  (Mauer,  Wall-
Töpferei;    dann   auch   von   anderweitigem   Bilden);    auch   vom  Tei».
kneten  (Bäckerei)';  dhij-ii-io-s  , Former';   dheigho-s,  dhoigbo-s  ßa^
bilde,  Wall' ;  s.  zum  Sachlichen  Meringer  IF.  17,  147.
Ai,  dBhmi  ,bestreiche,  verkitte'  (3.  Sg.  digdhi  statt  *dedhi),  ebenso  Partiz.
digdhd-,  deha-  m.  n.  ,Körper',  dehi  f.  ,Wall,  Damm,  Aufwurf,   av.  pairi-
daezayeiti  , mauert  ringsum'  (==  ai.  Kaus.    dehayati)   uzdiHa   3.  Sg.   Med.
,hat  (einen  Damm)  errichtet',  Partiz.  iiz-diUa-,  uz-daeza-  m.  ,AufhäufuDo'
WalP,  pairi-daeza-  m.  ,Umfriedigung'  (daraus  gr.  nagadeiaog),  apers.  didä
,Festung'  (aus  *dizä-,  Wurzelnom.  auf  -a),  npers.  diz,  dez  ds.;
arm.  dizanem  (Aor.  3.  Sg.  edez)  ,häufe  auf,  dizanim  ,häufe  mich  auf, dez  ,Haufe';
thrak.  -di^ogj  -di^cc  ,Burg'  (:  apers.  didä  oder  *dhigh-{a)-  auch  ös^iov, ON  Jei^ag,  Burto-dexion,  Burtu-dizos,  Jiyyiov  (:  lat.  fi'ngö)]  pannon.  VN An-dizetes  ,Burgan wohner' ;
gr.  reXxoq  n.,  rotxoq  m.  (formell  =  ai.  deha-)  ,Mauer,  Wand';  ^lyydvw, Aor.  d-iysTv  ,mit  der  Hand  berühren'  (Bed.  wie  lat.  fingere  auch  ,streichelnd betasten'.   Media  g  bereits  ursprachlich  aus  der  nasalierten  Präsensform);
lat.  fingö,  -ere,  finad,  fictum  ,eine  Masse  gestalten,  bilden,  formen;  er- dichten; streichelnd  betasten',  /^wZws  , Töpfer'  (:  germ.  *dizidaz),  filum {*figslom)  , Gestalt',  effigies  ,(plastisches)  Abbild',  figüra  ,Bildung,  Gestalt, Figur',  fictiö  ,das  Bilden,  Formen;  Bildung,  Gestaltung,  Erdichtung*, fictilis]  ,aus  Ton  gebildet,  irden,  tönern'  (zum  lat.  g  statt  h  s.  Leumana Lat.  Gr.  133;  nach  letzterem  stammt  aus  Formen  wie  fictus  auch  das  Ä  von altfalisk.  fifiked  ,finxit',  osk.  fifikus  etwa  ,du
```


## [2026-09-05T20:05:08.798Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"===BRT daeman\"; grep -n \"daeman\\|daēman\\|daöman\\|dae-man\" BRT.txt | head -10; echo \"===BRT daena\"; grep -n \"^daenä\\|daenä-\\|daena-\" BRT.txt | head -20; echo \"===BRT vaen\"; grep -n \"vaen-\\|vaenämi\\|vaenaiti\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:05:08.880Z] TOOL RESULT

```
===BRT daeman
12457:•  j.  daeman-n.  1) 'Auge,  Augapfel';  mi^rd .  .  a%ra  naram  mi^rSJrujqm  .  .  *pairi 'ma  (AP.)  värayeiti  Yt  10. 4*8;  —  yat  .  . uB  pairtjäarayeifttH^ä)  °ma  (als  AD.)  . . pairi.urvaBayänti  Yt  14. 56.  a)  "Blick': irtra  datäiti  •mäna  (AP.?)'>  darätsüka dsi'iräiya  Yt  10. 107  (?).
27156:•  j.  smarSnö-daeman-  Adj.  'mit  -  ?  - Augen':  uftrS  ..  'ma  Yt  14.12.
===BRT daena
3054:•  j.  a/a.daenä-  Adj.  (mask.  °na^  'der der  üblen  Religion  zugetan  isf:  ydia azöif  dahnkni  °na  Az.j.
8456:•  j.  ubdaena-  Adj.  (fem.  °nT-)  'aus  Web- stoff, Zeug':  vastrim  .  .  'tarn  va  Tzaimm Tv7  V.S.a^;  — yesi  avAat  izaätt/  (sd.)  .  . yesi  a»hat  -tfU  V.  7. 14  f.
11768:—  iGebr.  des  Pron.  s.  auch  Cld.  Fron.  4.  — Pii.:  an,  öi;  öiän;  mehrmals  weggelassen,  iB. Yl.  /.  19,  s.  No.  2;  fiir  tu  auch  IS,  iB.  Y. 32.  15.  43-  IS.  39-  '■  —  '*  Doch  ist  der  dort in  Note  2  angeführte  Punkt  allein  nicht  ent- scheidend; s.  IFAni.  /.  10.  Vgl.  aber  iB.  Y. 46.  8  (tä).  Yt.  /.  19  (^(i),  V.  il.  3  (Va).  YL  17.  21 {lifm;  s.  das  folgende  he),  lg.  96,  N.  68  {la(), V.  3,  30  (le)  niw.  —  ")  Hd».  vTsqslaca  (so NA.)  oAet  vünslaifa.  Pü.  (blos)i  apt  falirend. ~  3>  Konstruktion  nach  dem  Sinn.  —  4)  Das Verbum,  etwa  anhi  'ich  werden  sein'  (etill. Eine  gani  ähnliche  Ellipse  findet  Eich  an  der Parallelslclle  V.  49.  4di  s.  'daenä-  mit  No.  4.
12399:'daenä-  2
12417:•  j.,  g.  'daenä-  t  'Religion';  i)  im  gAw.'>: tqm  °nqm  ys  Aatqm  (Sp.  268  o.)  vaMstä .'.  3r»s' daidyat  (sd.)  Y..^^.  lo;  —  iaS<7 tSng  a  vtpmyät  (sd)  ärmaitis  yaHbyS masda  %wsi  vasyetE  'nä  ".  .  denen  deine Religion  verkündet  wird,  o  M."  Y.  44. 1 1 ; —  »ns  vTcidyai  (sd)  tqm  °nqm  yä  xsma- vatö  (sd.)  Y.  4:^.6;  — '  a'iw^V  (sd.)  mzüT fa^ö  yqm  'nqm  ahurö  sao^yantd  dadät ^-  53- ''  —  iiiit  vanhav-  Adj. :  ya^S  Asi dab»n  (sd)  . .  'naya  vankuyh  ucSiä  iyao- %anacä  Y.  5_J.  I.  2)  im  jAw.:  aya 'na  (IS.)  disyat  (sd.)  yS  .  .  aiwyir»Aqm (sd)  nöit  aiwyästi  \.  18.^;  —  anraAt mainySus  nasiltqm   'nqm  dalvayasnanqm
12421:■daenä-  A  8  a
12436:'daena-  Noten
12440:KonpA.,    E.    —    Et?    Gon.S  Versuch,   der '*daiaä-  und  *dainä-  etjrmologiich  gleichselit -  inm  V.  Väty)-  -  überzeugt  mich  nicht,    S. noch  No.  I.   —   np,  din.  —   Pü.:   den,   Sü.: dätih{%    —    I)  Wo  a?  im  Metram   für  iwei Silben   rechnet;    s.    'dainä-.     Also   wohl   ae ans  ar.  d^i^,  %  St. •  j.,  g.  'daena-  £  Hniieres  Wesen,  geistiges Ich,  Individualität',  öfters  kaum  übertrag- bar"; i)im  gAw.'':^<i/«J  maadapaour- vTm  gai%äslä  la^  'näs^  %wä  manankä xratüica"^  du,  qM.,  zu  Anfang  Individuen schufst  und  Individualitäten  durch  deinen Geist,   und  Verstandeskräfte"  Y.  3t.  1 46.  6;    —    nSit  nä    manä    ,  .   s}ngA3 xraiavö  .  .  varanä  (sd.)  .  .  uxla  .  .  }yi "hanä  .  .  "na  .  .  urvaaB  hacainil  Y.  4$. —  vaauklmcä  °nqm  ..  fstratam .. ärmaitim "^•37-  5i  —  ^^  ^'^  ux^äis  fyao%an3  'tiä (IS.)   a&m  spnvat  (sd.)  Y.5/.  ar;  —  y7 *iat  manS  vahyS . .  aSyaslä  (sd.)  kvö  'nqm iyaoiianacS  valanhScä  V.4S.4;   —  yqm yao/  (sd.)  •nqm  .,  dämyam  *hudJnao^ .. y.44.^;  —  yS  'nqm  vohü  ^sänltä  (sd.) ftananhä  Y.  49-  5 1  —  '?«"  ^^^  dqstvam (sd.)  'nayai  frävao'a  Y. 46^.7;  — frö  .  . a-sä    'na  fradaxsaya  (sd.)  Y.  j^.  13;    — AvB  tat  .  ,  ahtnäi  dazäz  (sd.)  'nayä  (IS.) z-aldMtttö  Y.57. 19";  —  mSnÜl  T  mqtdas- düm  *valds.düm  'näbll  aiyasta  (sd.)  ahBm yJ  . .  Y-53-  s";  — yas/ä  .  .  tarJ.mqsia  ,  . sao^aiUS   Sng  (sd.)   patdU  spmiä    'nä urvahs  .  .  ".  .  des  Saelyant  .  .  Ich  wird ihm  Freund  sein  ,  ."  Y.  45. 1 1***;  —  tJm aAfSfum  . .  'nä  saoiyantqm  yä  . .  urväxiat (sd.)  hyat  .  .  mTedtm  .  .  Y._j4.  '3;  —  yä "nü     vairXm    hanät   mjedtm    asahya  yssa astftt  (sd.)  Y.  54. 1 ;  —  hyai  'na  vakUn yBjpn  (sd.)  mlzdlH.49-  9;  —  ^y<'i  mlSdjm ^trtavai^lm   (sd.)  fradadä^S    'näbyni^  Y. 40.  I  ;    —    harthus  (sd.)  .  .  dadät   aAurS 'fiayüi  va^huyai  Y.  5j.  4;  —  'nayäi  va»- ktiy^i  yqm  ksi  Uyam  (sd.)  äatü  . .  ahuri>
12444:KompE.  —  Et.?  Ob  gleich  'daenä-  (sd.)?  S. No.  I.  —  Pü.:  den;  s.  noch  No.  3,  5.  — >)  Wo  ae  im  Metrum  für  iwei  Silben  rechnet wie  bei  ^daeaS:  —  »  Vgl.  (lu  V.5/.  19,  SS-  S) Y.J/.ai.  — 1)  Pü.;  fl  rfmWä«;  vgl.  PüErl.  zu den  inY.j7.  aj.—  4)DasVerbum,  etwa  atih>n, ist  zu  ergänzen,  yä  drjgvalö  daenä  statt  aKyäi daenayäi  yä  dr'.  Eine  ganz  ähnliche  Ellipse zeigt  V.  4q.  5  d;  5.  Sp.  614  m.  mit  No.  4.  — 5)  Pu.:  den,  erl.i  kiimin;    s.  dazu  No.  7f.  —
12447:daenävazab-
13845:•  ').,  g.  duz-daenä-  Adj,  (mask.  'na-)  'des Ziafnä  (Ich)  übel  ist':  yünd  dusmanarahs . .  'nahe  H.  2. 36;  —  'riing  .  .  drtgvalJ  Y. 4g,  II;  —  ma  *dus.^adhnäi  ma  °nai  Y. Ö5.  7 ;  —  'na  at»rS  mainyus  FrW.  4.2; — a6i/  ^rita/ä  'nJ  Yt.  IQ.  47,  49;  —  ta- '^ryavantim  'mm  YLp.31,  5.109.
29837:Der  lingste  Tag  (»u  16  Stunden,  s.  Bd.  25.  5)  1 »  J-  hamo.daena-  Adj.  (mask.  -na-)   'der wird  F.  37  b  gleich  12  langen  (vgl.  •ivaJajaa-  ■  gleichen  Religion,  des  gleichen  Glaubens': AAra-},  18  mittleren  und  24  kurzen  .M  gerechnet. Nach    der   obigen  Stelle  wäre  das  kiirieste  //. etwa  gleich  j/,  Sekunde.  Vgl.  West  SBE.  5. 93-
30241:•  j.  hu^daenä-,  *8aenä-*>Adj.  (mask.  °na-) 'des  Ich  gut  ist"*:  yvän>m  humanatihim i^A^  hvacarthtm  husyaoiitwm  'nfm'^x.^.y, —  yS7^  humanajihs  ..'nahe  H.  2.  18;  VyL ij;  —  yBnal  haca  humanankat  .  .  'nat ^•33i  —  y*^  humum  .  .  'na  (VS.)  H. 2.  II,  la;  —  Aaxayö  humanaahs . .  'oafna Yt.  ip,  95 ;  —  yä  'nS  asava  Yt.  4.  9;  9.
30631:hudaenä-
===BRT vaen
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
```


## [2026-09-05T20:05:10.152Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"===KNT vain\"; grep -n \"vain\\|vaina\" KNT.txt | head -30; echo \"===KNT dii\"; grep -n \"adi-vaina\\|adivaina\" KNT.txt|head",
 "description": "Grep Kent for vain"
}
```


### [2026-09-05T20:05:10.216Z] TOOL RESULT

```
===KNT vain
625:837. OLD PERSIAN FINAL 1 was always written with added у ($46): ат" = атту, Skt. dsmz; авчу = astiy, Skt. ásti; this includes the diph- thong -ai: vint1y* = vainalaty.
626:But final -hi, which would be expected to give -hiye = -hiy, must be written -hy = -hy, since h*i is almost never written for hi (§27): атау = amahy, for *as-masi; ига = vaindhy.
982:Also vaindhy, Skt. ind. vénati; haind, Skt. sénd; айа, duvaislam, gaibam, naibam, -tary, -$au, tyaty.
1122:I. pIE -d-n- became plr. -n- (shortening of -nn-, $130), as in pIE *yeid-ne-, ОР vainämiy Ч see’, Av. 3d sg. vaēnaiti; cf. the same root with nasal infix (instead of nasal suffix) in Skt. vindáti ‘he finds’, and in OP Ve"da'-farnah- ‘Intaphernes’ (see Lex. s.v.; -n- proved by Gk., Elam., АКК. transliterations).
1605:{07 &; $$ šas in OP usa- ‘camel’, Av. ustra-; §79. pIE dn > pAr. nn > plr. n as in OP vaindmiy Ч
1674:$139. CONTRACTION or VOWELS IN SANDHI is to be expeeted in combination with enclities, but the situations which produce it rarely oceur in ОР; there is one probable instance, vaina[pi]y XPz 71, for vasnd + apiy.
2430:pIE *ueid-ne-/-no- in OP vainamiy Ч see’, 3d sg. vainatiy, mid. vainataiy; Skt. véndm? ‘I desire’, vénati, vénate. $211. Tug PnEsENT-TENSE SYSTEM OF TYPE
2539:II. Thematic stems have subjunctives with the long thematie vowel throughout, Ist sg. and 181 and 3d pl. o, other forms é; 2d and 3d sg. and mid. as in Skt. bhár-àsi -àt -àse -äte : OP zšnāsāhy, Gahy (for *6aháhy), apa-gaudayàhy, \drau\jiyahy, pati-parsühy, pari-barühy (and -Gh*-d13), vainahy; ni-rasütty, xsndsdtiy, pati~parsatiy, bavatiy, vaind- tty; maniyahaty (for variant spellings, see Lex. s.v. ‘man-); maniydtaiy, gaubdtaty, 6adayátaty, yadataiy, vainātaiy. 3d pl. act. as in Skt. -dnis: OP vi-naéaya*tty (restored form).
2566:І. The primary ending -si was attached directly to the present stem, whether thematic or non- thematie, but happens to oceur in OP only in sub- junetive forms: pali-parsühy (on -hy, $87), Skt. prechasi; pari-barühy and -barüh*-di& ($136), vi- kanühy and -kanáh-dif, kunavahy, xindsdhy, à- tínavühy, vainahy, apa-gaudayahy, Idrau|jtyahy; 6ühy for *даћаћу ($131); ahy for short-vowel sub- junctive (8222.1) *ahahy = Skt. dsast.
2598:I. The primary ending was pIE -taz, as in Gk. perar, Skt. bhdrate; this is seen in ОР yadatary (= Skt. ydjate), gaubataty, ha”-taxSatary, vaina- lary, varnavatary, and in the subjunctives yaddtary, gaubdtary, etc. (§222).
2881:(4) The following middle forms have passive meaning: ind. vainaiaiy ‘is seen, is seen to be, seems’ DNb 2, XPa 16, and subj. varndtacy DNb 35; anayata ‘was led’ DB 1.82, 2.78, 5.26°: probably kunavalary DNb 56, and the restored forms {ajhlyaija ‘was thrown’ DB 1.95 and adá- Irayatlà DB 4.90f. This use of the middle is found in Avestan (Reichelt, Aw. Elmb. §614); and the middle forms are the basis of the passive forms of Greek and Latin.
2916:(b) Volitional uses: affirmative commands bavatiy DNa 43, 45f, vaindiaiy DNb 35; negative commands with mä or matya, draujiyáhy DB 443, wkanàhy DB 471, kunavdtaiy DNb 56, bavdtiy DNb 59. Negative wishes possibly in (restored) vijanātiy, vināðayātiy A?Sa 5, A?Ha 7 (though optative or injunc- tive or imperative forms are equally pos- sible in these passages).
2919:(a) In a relative clause of general future mean- ing, depending upon an expression of com- mand or prayer: àhy DB 4.37, 68, 87, DSt 10°; ahatiy DB 4.38, 68, 68f; kunavahy DB 4.75, 79; patiparsdhy DB 4.42; patiparsitiy DB 4.48; vainahy DB 4.70; vainatiy DS] 5°.
2924:mand or a prayer, once a future statement (DPe 22): apagaudayahy DB 4.55; 6ahy DB 4.55, 58; vaindhy DB 4.78, 77; vikanàhy DB 4.73; wikanàle-di$ DB 4.77; pattbarah*-dis DB 4.74; patibarühy DB 4.78; maniyáhaty DB 4.89, DPe 20, DNa 38, XPh 47; ahatty DPe 22.
2926:(c) In alternative general clauses, the first intro- duced by ya6ü ‘when’ and the second by yadi-và ‘or if’; the main clause omits the copula: vaindhy . . . drsnavéhy DNb 29f.
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
3151:Another type of stylistic omission is found when a clause is repeated, and one or more words of the prior clause are not repeated in the second, but are to be understood from the prior clause. Thus DNb 35-7 yaciy vaindmiy hamiciyam yaciy пату vainamiy (sc. hamiciyam) ‘whatever I see (to be) rebellious, whatever I see (to be) not (rebellious)’; and similarly in DNb 38-40.
3472:13 айту : Dārayavauš : xSayafiya : ima : dahyava : {уа : mand : paliyaisa : vain
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
3633:90 maiy : basta : adáriya : haruvasim : kara : avaina : pasavasim : Arbair&yá :
3835:4] vainà : Auramazdaha : hamahyày& : багаа : akunavam : tuvam : ka : һуа
3860:70 yavauS : xSayafiya : tuvam : kā : hya : aparam : imim : dipim : vainàhy : ty
3863:73 diy : imam : dipim : vainühy : imaiv& : patikarà : naiydis : vikanahy : uta
3871:77 yafiya : yadiy : imam : dipim : imaiva : patikarà : vaināhy : vikanah*dis : ut 78 ataiy : уйуй : tauma : ahatiy : natydiš : paribaráhy : Auramazdátaiy : jatà : b 79 iyā : ut&taiy : taumd : mà : biyá : uta : tya : kunav&hy : avataiy : Auramazd
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4120:2 ma : fra&am : tya : vainataiy : hya : adadā : Ši 3 уйі : martiyahyä : hya : xradum : ut
4131:20 y : tya : kartam : vainahy : yadivà : ахќпау-
4136:34 tiy : hamaranakara : am^iy : uShamaranakara : hakara 85 шегу : u&ty& : раба và : vaindtaiy : yacty :
4137:36 vainàmiy : hamiciya’m : yaciy : naly : vainà
4140:39 diy : vainàmiy : hamiciyam : yaa : yadiy :
===KNT dii
```


## [2026-09-05T20:05:23.063Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG uain\"; grep -n \"^\\*uain\\|\\*uain \" CHEUNG.txt | head; echo; grep -n \"uain\" CHEUNG.txt | head -20; echo \"=== CHEUNG daiH\"; grep -n \"\\*daiH\\|\\*daiH¹\\|daiH\" CHEUNG.txt | head -20",
 "description": "Grep Cheung for uain and daiH"
}
```


### [2026-09-05T20:05:23.143Z] TOOL RESULT

```
=== CHEUNG uain

2277:Y Av. bauuainti (Yt 5.94, Yt 10.20, Yt 13.15, etc.), YAv. pairi.bauuainti (V 19.27), YAv. ham.bauuainti 
2282:OAv. b(a)uuaiti (Y 30.10), OAv. b(ajuuat (Y 28.11), YAv. buuat, 3pl. OAv. b(a)uuainti (Y 33.10, Y 
5066:Pres. nu-: IND. 3pl. YAv. upadarosnuuainti (Yt 8.44) 
8599:hangouruuaiiata (Yt 19.35 f£), 3р1. YAv. fora gouruuain (Y 28.0), SUBJ. 3sg. ҮАУ. gouruuaiiat (Yt 8.60, 
8646:understand, know, be acquainted with’ || (+ *uz-) BSogd. zyrf- ‘to exalt’, BSogd. 
10128:Pres. nu-: IND. 3pl. YAv. apa.x'anuuainti (Yt 14.46); Partic.: (pres.?, aor.?) YAv. x'anat ° (Yt 17.1, Yt 
10129:9.2). 0 On the interpretation of Y Av. apa.x'anuuainti see Narten 1970: 173ff. 
11391:Pres. n-.: IND. 3pl. YAv. fröronuuainti (Yt 13.46), INJ. 3sg. YAv. froronaot (Y 11.4, Yt 13.146), SUBJ. 
13968:Pres. {1} nu-: IND. med. 3sg. YAv. voronüite (V 18.35, V 18.41, V 18.47), 3pl. YAv. varanuuainti (Yt 
14938:Pres. {1} ua-: IND. 3sg. YAv. juuaiti (V), 1р1. OAv. juuamahi (Y 31.2), 3pl. YAv. juuainti (V 2.41, V 
15774:10.13), 3sg. Y Av. koronaoiti (V 13.41, V 13.51, V 19.43, etc.), 3pl. YAv. "koronuuainti (Yt 13.26), impf. 
23320:N 60), 3р1. YAv. ()upa.surunuuainti (N 21), ОРТ. Zeg. YAv. surunuiia (Y 68.9); Aor. {1} athem.: IND. 
27183:Pres. {1} nu-: IND. med. 3sg. YAv. voronüite (V 18.35, V 18.41, V 18.47), 3pl. YAv. varanuuainti (Yt 
27669:*uat ‘to inspire, be informed, acquainted’ 
27671:*AVESTAN: vat- ‘to inspire ?, be informed, acquainted’ || (+ *api-) ‘to be acquainted 
27703:«PIE *uet- ‘to be informed, acquainted’ — LIV: 694 | Pok.: 346 
27887:nature’ (< *abi-uahäka-), 'BwYN- ‘to withhold strength’ (< *abi-uain). || Samadi: 
30171:*CHORESMIAN: m/n’s- ‘to become acquainted, accustomed’, (caus.) m/n’sy- ‘to 
30172:acquaint’ (n = [nn] < *zn- ?, rather than *xsn-, MacKenzie IV: 532) || (+ *apa-) 
30506:3sg. YAv. zauuaiti (Y 11.1 f£), 3pl. YAv. zauuainti (Y 11.1); Partic.: pres. {1} YAv. zbaiiant-, perf. med. 
=== CHEUNG daiH
4249:*daiH! ‘to look, see’ 
4262:*daiHl 49 
4279:now envisage a connection with the root *daiH'. The Parthian form would go back 
4317:50 *daiH2 
4328:(initial long à- points to *ä-abi-daiH' ?) || (+ *2-) NP äyinah, Bal. adén(k) ‘mirror’ || 
4342:*daiH', whereas the pres. stem is formed with the root *uai(H)n. An IE etymology 
4358:*daiH? ‘to shine, radiate; to light a fire’ 
10907:Ghilain, l.c., but rather from *daiH?, cf. Morgenstierne, EVS: 55a. 
14409:dinisäi/di(ya)nisi о be seen, appear’ are unconnected: they contain the root *daiH!, 
26754:dyd, v. *daiH'). © Also the ‘nose’ word, MMP wynyg, ВМР wynyk /wénig/, 
26761:*PARTHIAN: wyn- ‘to see’ (pres. supplet. of dy-, *daiH!) || (+ *apa-) 'bwyn- ‘to 
26771:Bailey (DKS: 25b f., but rather from *4- + *daiH!), on which see Emmerick, SVK I: 
26788:*NWIR: NP bin- (supplet. st. did- < *daiH'), Kurd. bin- (supplet. st. did-), Gur. vin-, 
26805:many WIr. forms *uai(H)n is part of a suppletive system with *daiH!. 
55198:*daiH' (s.v.), *датН? (s.v.), 
56330:*daiH' (s.v.), *Hai (s.v.), *fan 
57068:*braHz, *daiH’ 
57081:*daiH! , *haiz, *kas! , *kaus? 
57768:Soa), *daiH! , *dars, *hais, 
57794:*braHz, *daiH’
```


## [2026-09-05T20:05:25.264Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','KNT','BQT','HUB','HRN','SOD','FVQ','VDQ','FFD','AEF','SNS','MON','FSF','FVA','SOG','AHD','PHD','NYB','ARY']:\n    v=d.get(k)\n    print('##',k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n\"",
 "description": "Look up ref metadata"
}
```


### [2026-09-05T20:05:26.951Z] TOOL RESULT

```
## POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
## KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
## BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
## HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
## HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
## SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
## FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
## VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "
## FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
## AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 
## SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
## MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
## FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
## FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
## SOG {"title": "W. B. Henning, Sogdica (James G. Forlong Fund XXI), London 1940", "edition_found": "reprint in W. B. Henning Selected Papers II (Acta Iranica 15, 1977)", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt", "page_offset": "Original pagination (1-67) is printed in the reprint margins; grep -n 'SOGDICA' to find the section (~leaves 158-340 of the scan). local file has \\f between leaves (0-based leaf in
## AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
## PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
## NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
## ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


## [2026-09-05T20:05:31.039Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4249,4360p' CHEUNG.txt",
 "description": "Print Cheung daiH entry"
}
```


### [2026-09-05T20:05:31.118Z] TOOL RESULT

```
*daiH! ‘to look, see’ 

*AVESTAN: d(a)i- (ба1-) ‘to look, see’ || (+ *aua-) ‘to see off || (+ *a-) ‘to look, see 
to’ || (+ *upa-) ‘to to look on’ || (+ *pati-) ‘to meet (with one’s eye)’ || (+ ш-) ‘to let 
one’s eyes wander’ = Liste: 30 

Pres. {1} athem. red.: IND. 3sg. YAv. dióaiti (Y 33.14), Y Av. adióaiti (Yt Yt 10.15), INJ. 15р. YAv. auua 
óióaem (Vyt 43), 3р1. OAv. daidiiat (Y 44.10), SUBJ. 3sg. YAv. dióat (Yt 19.94); Pres. {2} them. red.: 
INJ. YAv. daidiiama (Vyt 43), SUBJ. 3sg. YAv. paiti.daidiat (V 16.2), ОРТ. 25р. YAv. paiti daióiiois 
(Vyt 50), IMPV. 2sg. YAv. "upa.daióiia (Yt 17.15); Perf.: IND. 3sg. YAv. adióaiia (Y 62.8); Partic.: pres. 
{1} YAv. daióiiant- (Yt 10.45), perf. Y Av. vidióuuah- (Yt 14.13) 


*daiHl 49 


*OLD PERSIAN: di- ‘to see’ — Kent: 191а 

Pres. athem.: IMPV. 2sg. didiy <di-i-di-i-y> (DNa 41, DNb 57) 

«MIDDLE PERSIAN: MMP dyd, BMP dyt (HZYTWN-) /did/ (pret. stem) “о see’ || (+ 
*(a-)abi-) MMP ’ywyn, BMP 'dwyn /ewen/ ‘manner, custom, form’ || (+ *a-) ? 
MMP ’ywyng ‘mirror ?’ (contaminated with MMP ’ywyng ‘manner, kind, fashion’ 
?) || (+ *pati-) IMP pyt’k, pty’k, MMP pyd’g, BMP pyt’k /paydäg/ ‘visible, obvious, 
revealed’ (< Pth.). O The etymology of MP /paydag/, NP padid, payda has been 
controversial. Horn 1893: 78 compared it with Av. paitiiank- ‘turned towards’, 
which was doubted by Hübschmann 1895: 360 f., but accepted by Nyberg II: 149. It 
can hardly come from *pati-ka@a- or *pati-y-ä-kas-, which were reconstructed by 
Back 1978: 252 and resolutely rejected by MacKenzie 1982: 290. This enigmatic 
form can be resolved if we assume that it was originally a Parthian form: we may 
now envisage a connection with the root *daiH'. The Parthian form would go back 
to *pati-diHä-ka-, which became subsequently *paddyag > *padyag. The 
inscriptional Middle Persian form pty’k bears witness to this stage. The form pyd’g 
in Pth. appears to be the result of epenthesis, /paydag/, which in turn could have 
been borrowed again in MP. The NP form padid no doubt derives from Parthian: 
ppp. *pati-diHta- ‘appeared, seen against’. > DMMPP: 149a, 82a, 289a 

Partic.: perf. pass. MMP dyd, BMP dyt /did/ 

*PARTHIAN: dyd (pret. stem) ‘to see’ || (+ "(a-Jabi-) "bdyyn, *bdyn ‘custom(ary), 
habit; manner, way’ || (+ *a-) ’dyng, "dyng ‘mirror’ || (+ *pati-) pyd’g ‘visible, 
obvious, revealed" = Ghilain: 84, 96 | DMMPP: 149a, 9b, 26a, 289a 

Partic.: perf. pass. dyd; Inf.: dydn ‘to see; [subst.] appearance’ 

*KHOTANESE: dai- ‘to see, look’, (mid.) ‘to appear’, dyafi- (caus.) ‘to make appear, 
reveal’ || (+ bays- < ?) baysdai- ‘to look at, observe’ || (+ *apa-, *pati) püy- ‘to look’ 
|| (+ *aua-) üy- (vüy-) ‘to survey’ || (+ *4-) OKh. äyä-, LKh. avi-, ayi- ‘to be reflec- 
ted, seen, appear’ || (+ *uz-) OKh. uysdai- ‘to look up (at) = SGS: 45, 47, 95, 85, 
19, 9, 16 

*SOGDIAN: (+ *a-) BSogd. ’’dyn’k, BSogd. ’’6’yn’k ‘mirror’ || (+ *ui-) BSogd. 
wyö’y- ‘to disappear, be distinguished’ || (+ *ham-) BSogd. ’nö’yk, CSogd. 'dyq? 
‘custom, habit, manner’, MSogd. ’nö’yk, MSogd. ’nö’ykh ‘appearance’ 

(+ *ш-) Pres.: IND. 35р. BSogd. wyö’yt, 3р1. BSogd. wyóy nt, OPT. 3sg. BSogd. wydy’y; Inf.: BSogd. 
wyóy y, pret. BSogd. wyöy’t 

*CHORESMIAN: бу- (pret. stem) ‘to see’ © Samadi: 224 

*BACTRIAN: M- (supplet. pres. otv-) ‘to see’ || (+ *(a-Jabi-) aBddivo ‘custom’ 
c» S-W, Bact.: 201b, 173a 

*NWIR: Widely attested: NP didan / (supplet. bin-), Bal. dit, ói(0)/ (supplet. gind- < 
*yaid’, Korn, Le: 79, fn. 26), Kurd. ditin, (also Sor.) din (supplet. bin-), Zaz. ditis/ 
(supplet. vinen-), Abyan. dia/ (supplet. vin-), Abz. dida/ (supplet. vin-), Awrom. 


50 *daiH2 


diáy/ (supplet. win-) ‘to see’, (also) diay/dia- ‘to look [intr.]’, Gil. (Rsht.) deoen/din- 
(with analog. d-), Gur. (Kand.) di-/ (supplet. -in-, (subj.) vin-), Ham. diyän/ (supplet. 
vin-), Jow. bam-di/ (supplet. ai:n-), Meim. dian/ (supplet. a-vin-), Mah. -dī/ (supplet. 
-vin) ‘to see’, Nn. di-/ (supplet. vin-), Natan. -di-/ (supplet. vin-), Qohr. dida/ 
(supplet. vün-, yin-), Semn. -di(&)-/ (supplet. m-éin-) Sang. -dia/ (supplet. vin-), 
Shamerz. bä-dimän/ (supplet. vin-), Siv. dien, Soi di(d)-/ (supplet. ä-ün-, ä-ün-), 
Sorkh. ba&-dian/ (supplet. vin-), Lasg. ba&-di-/ (supplet. vin-) “о see’, (ppp.) Bal. 
dista ‘seen’ || (+ *(a-)abi-) NP äyın ‘rite, custom; common law; mode, form, manner’ 
(initial long à- points to *ä-abi-daiH' ?) || (+ *2-) NP äyinah, Bal. adén(k) ‘mirror’ || 
(+ *pati-) NP padid ‘visible’, payda ‘visible, apparent, evident’ (old LW) 

*NEIR: Pash. Па/ (supplet. pres. st. win-) ‘to see’ || (+ *a-) Oss. I. ajdæn, D. ajdane, 
M. äina, Yi. äino ‘mirror’ 

*MISC: (+ *(a-)abi-) Arm. (LW) awren-k* ‘institution, the Law’, Syr. (LW) b-avden 
“similar to’ (< Pth.) 

*SANSKRIT: dhay ‘to look (at), to perceive’ (RV+) = EWAia I: 777 

9 As with many Iranian roots containing *d(-), a variant with the voiceless corres- 
pondence is attested as well: Bakht. te (pl. tia), Bal. telog (> Brah. tela) ‘eye’. Most 
Middle and New Iranian forms have a suppletive paradigm: the pret. stem contains 
*daiH', whereas the pres. stem is formed with the root *uai(H)n. An IE etymology 
for this Пг. root is uncertain, in the absence of any credible cognates. Only Alb. di 
‘knows’ can be cited in LIV: Le, which is hardly encouraging. Gr. ofa / сбра 
“sign, mark’ is unrelated. 

«PIE? © LIV: 141 f. | Pok.: 243 

*REFERENCES: КРЕТ. 81a, 139b f., 206b f., 245b f.; EVP: 36; KPF II: 199; Christensen, Contributions I: 
65, 259; Christensen, Contributions II: 55 f., 114 f., 159; Abrahamian 1936: 111; Lambton 1938: 42a, 
77b; Abaev, Slovar’ I: 41; MacKenzie 1966: 94; Lecoq 1974: 60; DKS: 19a f.; Rossi 1979: 54; Vahman — 


Asatrian 1987: 140; Werba 1997: 299 f.; Paul 1998: 296a; Cabolov 2001: 321 f.; Cheung 2002: 150; 
Lecoq 2002: 121, 123, 125 (passim); МЕУР: 88; ESIJa II: 291 Ё; Korn 2005: 79, 314, 375 (passim) 


*daiH? ‘to shine, radiate; to light a fire’ 

*MIDDLE PERSIAN: ? ВМР dyk /dég/ ‘pot, vessel’ (etym. uncertain) || (+ *pati-) MMP
```


## [2026-09-05T20:05:31.208Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26740,26815p' CHEUNG.txt",
 "description": "Print Cheung uain entry"
}
```


### [2026-09-05T20:05:31.260Z] TOOL RESULT

```
(F 411), 3pl. ҮАУ. vaénon (Yt 10.92), SUBJ. 35р. Y Av. vaenat (Yt 19.94, N 16), med. 35р. YAv. vaenaite 
(V 2.24), med. 3pl. YAv. ham.vaénante (V 9.1), OPT. 25р. YAv. auuaenois (H 2.13), 3sg. YAv. vaenoit 
(Y 9.29), med. 1р1. YAv. ham.vaenoimaidi (Y 58.6), IMPV. 25р. OAv. auuaena (Y 46.2), 2р1. OAv. 
auuaenata (Y 30.2); Partic.: pres. YAv. vaenant- (Yt 5.129), med. YAv. vaénamna- (Yt 19.34, Yt 19.80); 
Inf.: pres. OAv. уаёпађћг (Y 32.10). © The initial a^ of OAv. auuaéna is the result of shortening in front 
of *u, cf. De Vaan 2003: 123 ff. 

*OLD PERSIAN: vain- ‘to see’ > Kent: 206a 

Pres. them.: IND. 159. vainami <va-[i]-n-a-mi-y> (DNb 36, <va-i-n-a-mi-y> (DNb 39 Ё), med. pass.) 
3sg. vainataiy <v-i-n-t-i-[y]> (DNb 2), <v-i-n-t-i-y> (XPa 16), impf. 3sg. avaina <a-v-i-[n]> (DB 2.76), 
<a-v-i-n> (DB 2.90, DNa 32), SUBJ. 2sg. vainähy <v-i-n-a-h-y> (DB 4.70, DB 4.77), <v-i-n-a-h-[y]> 
(DB 4.73), 3sg. vainätiy <v-i-n-a-t-i-y> (DSj. 5), med. (= pass.) 3sg. vainätaiy <v-i-n-a-t-i-y> (DNb 35) 
«MIDDLE PERSIAN: MMP wyn-, BMP wyn- (HZYTWN-) ‘to see’ (pret. supplet. stem 
dyd, v. *daiH'). © Also the ‘nose’ word, MMP wynyg, ВМР wynyk /wénig/, 
probably contains *uai(H)n. 

Pres.: IND. Leg. MMP *wynwm, 35р. MMP wynyd, SUBJ. 3sg. MMP wyn’d, 2pl. MMP wyn’d, 3р1. 
MMP *wyn’nd, IMPV. 2pl. MMP wynyd, wynyyd; Pass.: pres. IND. Zeg. MMP wynyhyd, ОРТ. 3sg. 
MMP wynyhyy 

*PARTHIAN: wyn- ‘to see’ (pres. supplet. of dy-, *daiH!) || (+ *apa-) 'bwyn- ‘to 
dislike, disapprove’ || (+ *fra-) frwyn- ‘to forecast, foresee’ = Ghilain: 84 | 
DMMPP: 354, 15a, 158a 

Pres.: IND. 15р. wyn’m, 35р. wynyd, 2р1. wynyd, wynynd, SUBJ. 15р. wyn’n, 25р. wyn’h, 3sg. wyn’h, 
IMPV. 25р. wyn, wyyn, 2р1. wynyd, OPT. wynyndyh || (+ *apa-) Pres.: SUBJ. 25р. ’bwyn’h || (+ 
*fra-)Pres.: IND. 3sg. "frwynyyd, 3р1. “frwynynd, 25р. frwyn; Partic.: pres. frwyng, frwyng’n (pl.), perf. 
pass. II frywyn’d 

*KHOTANESE: 9 avida ‘he sees, he is seen’ is not from *a-uai(H)n-, as assumed by 
Bailey (DKS: 25b f., but rather from *4- + *daiH!), on which see Emmerick, SVK I: 
72 f. 

*SOGDIAN: SSogd. wyn, BSogd. wyn, CSogd. wyn, MSogd. wyn ‘to see’ || (+ *abi-) 
BSogd. Bywyn ‘to foresee’, CSogd. bywny? (m.) ‘prophet’ 


*uaij 413 


Widely attested: Pres.: IND. 1sg. BSogd. wyn’m, dur. CSogd. wynmsq, 2sg. SSogd. wyny, 3sg. SSogd., 
BSogd., CSogd. wynt, med. CSogd. wynty, dur. CSogd. wyntq, etc. || (+ *abi-) Impf.: IND. 3sg. BSogd. 
B'ywn (GMS: $434, fn. 2.) 

*CHORESMIAN: (+ *abi-) "BwYN- ‘to withhold strength’ || (+ *upa-) bwyn- ‘to 
advise, admonish’ => Samadi: 42, 30 f. 

*NWIR: NP bin- (supplet. st. did- < *daiH'), Kurd. bin- (supplet. st. did-), Gur. vin-, 
Zaz. winen-, Bal. gind-, Tal. vind- ‘to look, observe’, Anar. ewin-, Awrom. win- 
(supplet. diay), Fariz. -vin- (supplet. di-), Yar. -vin- (supplet. di-), Gz. ven- (supplet. 
di-), Gur. -in-, (subj.) vin- (supplet. di-), Isfah. venän/ven-, Khuns. vin- (supplet. 
di-), Jow. ai:n- (supplet. bam-di), Meim. a-vin- (supplet. dian), Nn. vin- (supplet. 
di-), Natan. vin- (supplet. -di-), Semn. m-éin- (supplet. -di(&)-), Sang. vin- (supplet. 
-dia), Shamerz. vín- (supplet. bä-dimän), Siv. vin- (supplet. di-), Soi a-ün-, ä-ün- 
(supplet. di(d)-), Sorkh. vin- (supplet. boe-dian), Lasg. vin- (supplet. bae-di-) ‘to see’ 
*NEIR: Oss. I. wynyn/wynd, D. winun/wind, jinun/jind, Pash. win-, Sh. win-/wint, 
Khf. win-/wint, Rosh. wun-/wunt, Sanq. weyn-/wand, Ishk. wen-/wend-, Sangl. 
win-/wind-, Wa. win-/wind-, vin-/vind-, Yi. win- (supplet. lisC-), M. win- (supplet. 
lisk"-) Yghn. wen-/wéta ‘to see’ 

*SANSKRIT: ven- ‘to look for’ (RV+) = EWAia II: 582 

© This Пг. root is nominal in origin, from the noun *uai(H)na- ‘watch, survey(or)’, 
cf. Skt. vená- ‘watch’, YAv. vaena- ‘nose’, cf. Goto 1987: 298 for references. In 
many WIr. forms *uai(H)n is part of a suppletive system with *daiH!. 

«PIE *uei(H;)-no- ‘survey’ => LIV: 668 f., fn. 5 | Pok.: 1123 

*IE COGNATES: Lat. venari ‘to chase, hunt? 

*REFERENCES: КРЕ I: 139b f., 206b f., 245b f.; Ivanow 1926: 420; EVP: 87; KPF II: 199; Christensen, 
Contributions I: 162, 259; IFL II: 262a, 548; Christensen, Contributions II: 55 f. 114 f. 159; 
Abrahamian 1936: 133; Lambton 1938: 42a, 77b; Andreev — PeSéereva: 351b; MacKenzie 1966: 94;
```


## [2026-09-05T20:05:55.525Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n \"gyān\\|gyan \\|dēn \\|dēm\\|ēwēn\\|āzēn\\|ādēnag\\|ādēn\\|dīdan\\|paydāg\" PHD.txt | head -40",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T20:05:55.591Z] TOOL RESULT

```
=== PHD
67:The phonetic realizations of these phonemes can only be sup- posed to have been similar to those of the corresponding sounds of present-day Western Iranian speech. The only allophonic variation of importance concerns the voiced stops b, (d?), g, and affricate J. Between a vowel and a following consonant, in the same morpheme or close juncture, these almost certainly became the fricatives [B, (8), у, 2] respectively. Thus abd, tigr, dujdēn represent pronunciations [*afd, tiyr, duZdén]. How far, or when, this development affected the same phonemes elsewhere in post- vocalic position is uncertain. It is sufficient to regard [B, 8, y, Z] as possible realizations of postvocalic b, d, g, j.!
123:?bóy ... add incense. buland ... add aloud. čandīdan ... | (M cn-ystn), J ~]...
225:ayābāģ Dy'p()£!] acquisitive, receptive. ~ih: comprehension. ayād Pbyd?t' | M? yd, N yad] memory. ~ kardan; remember. ~gar LEI | N —gàr] memoir. āyaft Pdypt' | M ?ypt, N āyift] boon, favour, gift. ayāftan, ayüb- [5?5-tn! | M *3pt,*?b-, N yāftan, yab-] obtain, acquire, attain. ayār [kdybl | M hy’r, N yar] helper, friend. ~th: help, friendship. ayārdēnīdan, ayārdēn- ['4?/tyn-ytn!] boil, agitate. ~i&n: agitation. ayārdīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe. ayārīdan, ayür- [hdyb'l-ytn! | N yār-īdan] 1. help, assist; 2. be able, dare. ayürómand [hdyb’Pwmnd | N yarmand] helpful, friendly. ~ih: helpfulness, friendliness. ayāsīdan, ayās- [’byq’s-yin' | M ?y^s-] remember, be mindful of. „išn(īh): memory. ayāstan [by@’sin' | M *)*st] = ayāsīdan. āyišm [dšm] moon. aydxšust [ywhhhwst! = Av. ayóxfusta- | M ”ywxšyst 1] metal. ~€n [-yn'] metallic. āydoxtan, āyēz- ['ywhtn!, ?ywc-] join, yoke. ~išn: union, alliance. 14ydzidan Pyweytn'] = āyēūxtan. tāyozīdan, āyoz- Pywe-ytn' | Р уші, ?ywz-] trouble, disturb; strive, struggle. ^-i$n(ih): endeavour, strife. laz [MN < A mn; hc | Mc, ?z, N ~] from, than. žaz Dell dragon. *az [ANE < A?nh | P >z] I. āz Pc | M ?z, N ~] greed, lust. Ba, z- azabar [hcpl | M?c?br, № zabar] above. 7 āzād Pot! | M ?zd, N ~] r. noble; 2. free. āzādīh Petyh] т. freedom; 2. gratitude, thanks. ~ ģuftan, ~ hangardan, ~ kardan, pad ~ dāštan: thank, give thanks. атат [?с?[ | N ~] torment. āzardan сіп! | M ”zyrdn] = azardan. āzārdan, āzār- Pc/-tn! | № ~] torment, injure. ~išn: torment, injury. lāzarm [clm | M ??zrm, N ~] honour, respect. *'ázarm [?clm | M ?zrm-] harm, injury. a-zarmān Pz/mn!] ageless, unaging. āzarmīģ [clmyk'] honoured, respected. ~th: honour, respect.
296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
701:abrade randīdan.
755:agitate ayārdēnīdan. agitated, be — ayārdīdan. agitation ayārdēnišn.
792:animal gyānwar; zāyišnīg; tame ~ dam; wild — dad.
793:animate gyānwar, ustanómand.
893:audience handēmānīh; pēšgāh.
964:before handēmān, pēš.
1238:circumstance čē-ēwēnagīh.
1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
2098:ghost (soul) gyān, uštān; give up the — gyan kandan.
2259:help (v.) ayārīdan, frayādīdan.
2331:how čiyēn, čē-ēwēnag.
2714:man mard, wir; (—kind) mardēm; the First ~ Gayómart; old ~ zarmān; young — mérag.
2821:mirror ēwēnag.
2962:obvious āškārāg, CaSmagah, čašmdiīd, paydāg, гӧ&пар.
3211:presence handēmānīh; in the — of handēmān.
3251:properly pad ēwēn.
3259:propriety ēwēn(ag).
3303:quake čandīdan, wizandidan. quaking wizandag ; wizandišn. quality (accidental) jadišn. quantity čandīh.
3342:reckless gyānabespār.
3425:reveal āškārāgēnīdan, paydāgēnīdan.
3426:revealed paydāg; be — paydāgīhistan.
3436:revolve gardīdan.
3566:seethe ayārdīdan.
3774:spiritual gyānīg, menógig, ruwānīg, waxšig.
4232:visible čašmdīd, (pad) didàr, paydāg, wēnābdāg, wēnišnīg.
4234:vital gyānīg.
4324:wise dānāg, frazānag, xradēmand, zīrak.
4471:tar, tarr tarazén- tarāzēnīdan tarāzūg piht
4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
4727:pēsišn passand passand- passandišnīg passandišn passandīdan penīh
4762:petig, sti stendag sidig, stéy sidigar stér stézag stowih stūwēn- stowēnīdan stē Sadwēs dīdan -istan stūn stūnag stor, stür sturg stūrīh stórgáh storban stard *stūš stūdan star
```


## [2026-09-05T20:05:57.188Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf for p93\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor p in (93+21,):\n    print('--- leaf',p)\n    print(t[p][:3000])\nEOF",
 "description": "Print Horn p.93"
}
```


### [2026-09-05T20:05:58.821Z] TOOL RESULT

```
=== HRN leaf for p93
412
--- leaf 114
— 93 —
412. jäme 'Kleid, Gewand'.
ai. V^yam- mit chardis- etc. *ein Dach, einen Schirm,
Schutz überhalten , lett. ju^m-f *dachdecken*, ksl. /)o-
jata 'Dach' (Fick); phlv. jämak bezw. yamak (z. B.
vd. 6 (71) Gl.)i).
kurd. yüma 'grobes baumwollenes Zeug (H,-Sch.);
LW. afy. jama, bei. jfämag (113).
Hörn, KZ. 32, 583 No. 11.
413. Jan 'Leben, Seele', Janver.
aw. daenä' 'Seele, zu [/'dliay-, dhyO- (oder nach
Bartholomae, ZDM6. 43, 665 dhai-) „'sehen' im
geistigen Sinn, subjektiv die Erkenntniss als psy-
chischer Faktor, objektiv die Erkenntniss als das
wahr Erkannte, Glaube, Bekenntniss" (Geldner,
BB. 15, 261); phlv. jän, jätwar,
LW. kurd. bei. (114) afy. Jan,
Geldner, KZ. 25, 562 Note 140, Hübschmann,
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
») Fr. Müll er 's Lesung .^ar^rmw (WZKM. 5, 380J ist unmöglich.
```


## [2026-09-05T20:06:08.937Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor p in (49+10, 38+10):\n    print('=== leaf',p,'(printed',p-10,')')\n    print(t[p][:2500])\nEOF",
 "description": "Print Hübschmann pp.38,49"
}
```


### [2026-09-05T20:06:10.545Z] TOOL RESULT

```
300
=== leaf 59 (printed 49 )
— 49 —
kommen doppelt vor!), 339, osset. dxtong 'Bauchgurt*,
dumStbng *Schwaiizriemen*, afgh. ta-tang *Sattelgurt',
tang ^Sattelgurt*.
399. Dazu np. tanasta 'tela araneae', afgh. LW. tanista
*Spinnewebe , tdnista *the warp in weaving'. KaS. tUnS
Aufzug' Shuk. 91 = np. tWna.
400. Np. to *du, paz. tho d. i. to Min. GI. 198, Shk. 269
= zd. tava wie man *ich' = zd. mana etc., Fr. Mil Her,
WZKM. 8, 93.
Np. toSa 'Reisevorrath* = arm. LW. Mak u. s. w.
ist nach Fr. Mil Her, WZKM. 7, 372 = skr. Ma^
'Befriedigung'. Unsicher der Bedeutung wegen.
403. Np. tola junger Hund' ist nicht = zd. tauruna^, da
es eine u-Epenthese im Persischen nicht giebt. Zd.
tauruna- kann doch auch nicht gleichzeitig = np. tar,
tarr *feucht, frisch' (Nr. 382) and == tola junger
Hund' sein!
406. Es ist absolut ausgeschlossen, dass das altpersische
* Tlru des 5. Jhd. a. Chr. aus tistrya- entstanden ist.
408. Bal. te» ist LW.
409. Zu np. tey *Spitze, Schwert, Klinge, arm. LW. tSg
'Spitze der Lanze, Lanze', afgh. LW. tBy a sword' etc.
gehSrt auch np. tSya 'lamina', modern t%yd * Klinge'
(Rosen, Sprachfuhrer p. 55).
412. Fr. Mil Her vergleicht besser n^. Jama 'Kleid' aus
phi. yamak = ap. ^yohma" mit gr. '(^vi^a, WZKM. 8, 93.
413. Zd. da^a- kann nicht gleichzeitig = np. jdn und
= np. din (Nr. 597) sein. Ich setze Jdn *Seele' = skr.
dhydna- *Nachsinnen. Justi und Fr. M tiller ver-
kniipfen jdn mit zd. gay a- Xeben', was lautlich un-
zulassig ist. Kurd, gdn bei Rhea und im Dialekt
von Sivend (Journ. asiat. 1893, p. 248) ist schwerlich
urspriinglich.
415. Bartholomae's Bemerkungen sind verfehlt. Np.
Jdvldan *kauen etc. gehSrt zur idg. Wurzel giv, gyu^\
die in ksl. zHvati *kauen', deutsch kaum (vgl. K 1 u g e ,
*) Vgl. die Wurzel apiv = apyu *speien*.
Hubsohmann, PersUche Studien.
=== leaf 48 (printed 38 )
— 38 —
286 Anm. Np. p%r alt' aus ^p^rvya- = ap. p(a)rumya-
(haca parumyata Von Alters her') ? Vgl. mirad *stirbt*
aus *infyatai.
287. Np. pid/ram erfreut' wird aus ^paiti-raman- erklart.
Warum dann nicht *pairam*i^
289. Streiche die Worte: „al80 aw. ^upadtti-'' und vgl.
oben Nr. 144. Das Wort padid sichtbar ist erst im
Mittelpers. componirt aus pa und dU == 'in Sicht'
wie padrud aus pa und drut (Horn, Nr. 288).
291. Np. padtra 'entgegen = paz. padtra Min. Gl. 151,
Shk. 261, phi. patlrak Gl. and Ind. 95 etc. lasst sich,
da phi. paVSrak fest steht, nicht auf ein phi. "^patglrak
zuriickfiihren und mit Nr. 290 : padlruftan ( entgegen-
nehraen, annehmen = phi. patgrafian (ap. patiy H-
grh) vermitteln. Ich glaube, dass die beiden Worter
wurzelhaft verschieden *) sind und nur die Praep. pad-
= ap. patiy gemein haben, dass aber phi. patgraftan,
pr. *patg%ram 'entgegennehmen' friih von patlrak *ent-
gegen* lautlich beeinflusst worden ist. Sonst sind auch
die Lautverhaltnisse von padlruftan unerklarbar. Denn
warum heisst es nicht: *paigriftan, *paigiram?
295. Np. pardgandan zerstreuen', phi. pargandak 'scat-
tered* (61. and Ind. 103) passt jedenfalls nicht zur
Wrzl. kan graben'. Es gab ja wohl auch noch andere
Wurzeln kan oder gan. Vgl. Nr. 41 : agandan VoU-
stopfen'.
296. Np. partav 'Licht, Strahl* (auch afgh. LW.) mit auf-
falligem t fiir d, Anlehnung an tab, taftan etc.?
297. Np. pardaxtan hat bei Vullers 12 Bedeutungen,
es ist schwer zu entscheiden, auf welche man die
Etymologie bauen soil. Die gewohnliche Bedeutung:
VoUenden, beendigen, sich mit etwas beschaftigen'
(vgl. afgh. LW. pardaxt performance, relinquishment,
*) paSira = phi. patirdh gehort zu zd. paiti + ar^ wovon pat-
tyUra' 'Opposition', paiti-ereiti- 'Widerstand, Hinderniss*, apaitiereta-
'ohne Widerstand, ungehemmt'. Ich setze paSira = ap. ^pati-jrya-.
```


## [2026-09-05T20:06:30.846Z] TOOL CALL #21: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:06:30.857Z] TOOL RESULT

```


```


## [2026-09-05T20:06:33.006Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT vyana\"; grep -n \"vyäna-\\|vyana-\" BRT.txt | head -10; echo \"=== HRN 289\"; grep -n \"^289\\.\\|^288\\.\\|^290\\.\" HRN.txt | head",
 "description": "Grep BRT vyana and Horn 289"
}
```


### [2026-09-05T20:06:33.073Z] TOOL RESULT

```
=== BRT vyana
24698:•  j.  vyäna-  Adj.,  PPM.:  s.  vä{y);
=== HRN 289
2826:288. pedrad 'Heil, Lebewohl*.
2829:289. pedJd 'sichtbar.
2832:290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
```


## [2026-09-05T20:06:36.297Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2820,2845p' HRN.txt; echo \"=== BRT vyana context\"; sed -n '24690,24705p' BRT.txt",
 "description": "Horn 289 and BRT vyana"
}
```


### [2026-09-05T20:06:36.358Z] TOOL RESULT

```
puränd'^ skr. purcUana-,- 65 —
Die Form pid könnte man bei FirdüsT an den Stellen
einsetzen, wo nach peder keine Izäfe steht (vergl. pus) ;
sonst kommt sie neupersiseh nur in den Patet's vor.
287. pidräm 'schön, fröhlich' (Sahn. III, 1803, V. 372).
aw. *2)aiti.raman' ; vergl. np. räm (No. (504).
288. pedrad 'Heil, Lebewohl*.
phlv. pa i]^t) + drüt (Nöldeke, Kam. 65).
Vergl. np. durüd (No. 555).
289. pedJd 'sichtbar.
phlv. pa du {^\y\rr^^\ ps), Nöldeke, Karn. 40; also
aw. Sipa.dHi-,
290. peölruften 'empfangen, annehmen', jüd.-pers. J nenne,
Praes. peöJr-em, peSlr,
ap. *patit/ -f- i/^grufj-; phlv. patgriffan bezw.
«
patiraftan (Bund., sonst stets inJltJ^pD), päz. padlraftan
'empfangen, annehmen .
Vergl. np. giriften (No. 909).
291. peöfre entgegen*.
phlv. patlrak *) (mit verkürztem k , nicht patirag),
übersetzt aw. paiti.
Zur vorhergehenden Nummer.
292. per-, Praefix.
1) ap. /)am- 'weg {paräbara, parägmata); aw. para
Vor, weg* ; phlv. par-, ai. pdrä- 'weg, fort*.
=== BRT vyana context
vAbleit.  —  Vgl.  vy^xa-.  —    '>  NA.  vyax',  s.
vyambura-  147S
•  j.  vyaxman'ya-  den.  Praes,  31  'con- tionari'.
'contionari,  in  der  Versammlung  spre- chen': hs  i%ra  vyäxmanyeili  hS  i^ra  *p^^ sanyeiti  Yt  tf.  1 5 ;  —  As  avaha  vysxmanyata Yt.  19. 43.
•  j.  vyatana-  m.  EN.  eines  Gläubigen: yaüus^us  -nahe  alaonS  Yt  13. 1 23.
Eiß.  Bed.?     Wohl  fi+jöC;    s.  ai.  yälana-  n.
•  j.  vy-ädä-  i)  Adj.  "heimzahlend,  ver- gehend' (nur Komp.).  2)  f.  'Vergeltung flir  Verdienst,  Belohnung,  Dankabstattung': narsca  asaonS  x?nuiti7nca  *arfitlmca  'das- (AP.)ia  paili^aintyas^a  P.  jp;  —  ta  ahmt nmäne  jamyani  yk  asaonqm  xlnätasca aSayasla  'daibii'\As  Subj.)f'o  paiti.zanla- yasca  Y.  60. 2.
KompEL  —  Pü. ;  apc  dahismh.  —  O  D.  i. "'vyädbis,  nach  der  kons.  Dekl.;  K  18  (S.  157) hat  vyädanbyasca.
•  j.  vyäna-  Adj.,  PPM.:  s.  vä{y);
•  i.*vyänay-''  f.  —  ?— :  vispä  antan  °nls
P.?7.
Pii. ;  vaS  fa  harvisp  andark  api  pärihä  (bei Blochet  partkS),  erl. :  kus  afie  päyihä ;  mir unverständlich;  s.  No.  2.  —  O  So  Blocket; DST.  tiiän'.  —  »)  DsT.  ZA.  j.  66  überset«: "et  ne  faire  qae  regarder  dans  rinlervalle" und  verweist  auf  V.  ig.  19.
•  g-  *vyänä-  f.  'Gescheitheit,  Weisheit', ur  IS  :  kl  uzamSm  (sd.)  cSrti  •naya  pu- .  r)m  pi^fl  Y.  44-  7 ;  —  <^t^  vaocat  ahur5
masää  ..  °nayä  "daspracherselbst,/4^JI/., .  mit  Weisheit"  Y.  29.  6.
Komp.:  vl-^^yänä;  zum  V.  yä-,  Bed.  ond  Et. unsicher.  -  Pü.  (dRn.):  Aaiar  vinditütn,  vi- cärüii.  —  ')  Sü.  hat  dafür  yal  gj-hnali,  nicht labhaU,  womit  vindtl  sonst  übersetzt  wird.
•  j.  vyäne  Inf.  'auszubreiten,  zu  ver- breiten':   mi^rtm  .  .  yahmi  vy'  da»tayai
```


## [2026-09-05T20:06:37.952Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D9%86",
 "prompt": "Give the full Persian etymology section for جان (jān) 'soul, life': what Middle Persian form, what Proto-Iranian reconstruction, what cognates and sources are cited?"
}
```


### [2026-09-05T20:06:45.911Z] TOOL RESULT

```
# Persian Etymology for جان (jān)

## Middle Persian Form
The entry cites Middle Persian forms in Book Pahlavi script: "HYA" and "yʾn'" with the transliteration "gyʾn /⁠gyān⁠/" meaning "soul, ghost."

## Proto-Iranian Reconstruction
The reconstructed Proto-Iranian form is "*wyaHnáH" which is described as equivalent to "*wi-" + "*HanH-" ("to breathe").

## Proto-Indo-European Origin
The term ultimately derives from Proto-Indo-European "*h₂enh₁-" meaning "to breathe," with Proto-Indo-Iranian "*wiyaHnás" as an intermediate stage.

## Cognates
The entry lists these related words:
- Northern Kurdish "giyan"
- Central Kurdish "گیان" (giyan)
- Avestan "𐬬𐬌𐬌𐬁𐬥𐬀𐬌𐬌𐬁" (viiānaiiā)
- Sanskrit "व्यान" (vyáná)
- Latin "animus"

The etymology also notes a comparison to Latin "animus" as a cognate descendent.
```


## [2026-09-05T20:06:56.915Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%DB%8C%DB%8C%D9%86",
 "prompt": "Give the full etymology of Persian آیین (āyin) 'custom, rite': Middle Persian form and spelling, Proto-Iranian reconstruction, and any alternative etymologies or sources cited. Also mention any related entries such as آذین."
}
```


## [2026-09-05T20:06:58.644Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%E1%BF%86%CE%BC%CE%B1",
 "prompt": "Give the full etymology of Ancient Greek σῆμα (sêma) 'sign': what reconstructions and cognates are proposed (Sanskrit dhyāman?), what does Beekes say, and is it considered Pre-Greek or of Indo-European origin?"
}
```


### [2026-09-05T20:07:00.959Z] TOOL RESULT

```
Based on the provided Wiktionary page, I cannot give you the full etymology you're requesting. The page content shows that **آیین** (âyin) is listed as an alternative spelling of **آئین**, but it does not include etymology information, Middle Persian forms, Proto-Iranian reconstructions, or discussions of related entries like آذین.

The page only states: "alternative spelling of _آئین_" without providing historical linguistic details or etymological development.

To find comprehensive etymological information for this Persian word, you would need to consult more detailed etymological references or the full Persian Wiktionary entry, which this English Wiktionary stub does not contain.
```


### [2026-09-05T20:07:04.551Z] TOOL RESULT

```
# Etymology of Ancient Greek σῆμα (sêma)

## Reconstruction and Cognates

The word derives from Proto-Indo-European *dʰyéh₂mn̥, ultimately from the root *dʰyeh₂- meaning "to notice." The primary cognate cited is Sanskrit dhyāyati ("think of, imagine") and dhyāna ("meditation").

## Beekes' Position

The entry explicitly notes: "although Beekes is skeptical of the semantics." This indicates scholarly reservation about whether the semantic connection between the PIE root and the Greek sense of "sign" is fully satisfactory, despite accepting the phonological derivation.

## Origin Classification

The word is classified as **Indo-European in origin**, not Pre-Greek. It is categorized as an "Ancient Greek term inherited from Proto-Indo-European" and "derived from Proto-Indo-European," establishing clear IE ancestry rather than a substrate borrowing.
```


## [2026-09-05T20:07:10.205Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%A6%DB%8C%D9%86",
 "prompt": "Give the full etymology of Persian آئین/آیین (āyin) 'custom, rite, ceremony': Middle Persian form and spelling, Proto-Iranian reconstruction, cognates and sources cited."
}
```


## [2026-09-05T20:07:11.506Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%AF%DB%8C%D9%86%D9%87",
 "prompt": "Give the full etymology of Persian آدینه (ādine) 'Friday': Middle Persian form, reconstruction, and any explanation of its origin and sources cited."
}
```


### [2026-09-05T20:07:15.441Z] TOOL RESULT

```
# Etymology of Persian آئین/آیین (āyin)

Based on the Wiktionary entry provided, the etymology information is limited:

The source states the word is "Akin to Old Armenian _օրէն_ (ōrēn), an Iranian borrowing."

Unfortunately, the document does not provide:
- The Middle Persian form or spelling
- A Proto-Iranian reconstruction
- Additional cognates beyond the Armenian parallel
- Scholarly sources explaining the deeper etymological pathway

The entry cites historical references (Dehkhoda, Hayyim, Steingass) but does not elaborate on their etymological analyses within this visible content. To obtain a complete etymological account including Middle Persian attestations and Proto-Iranian roots, consulting those referenced works directly or accessing more detailed etymological resources would be necessary.
```


### [2026-09-05T20:07:19.016Z] TOOL RESULT

```
# Etymology of Persian آدینه (ādine) 'Friday'

**Middle Persian Origin:**
The word derives from Middle Persian *ʾdynk'* /ādēnag ~ āyēnag/, which appears in Pazand texts as 𐬁𐬛𐬉𐬥𐬀 (ādēna) and 𐬁𐬜𐬉𐬥𐬀 (āδēna).

**Possible Source:**
The etymology suggests "perhaps from Parthian," though the exact Parthian form is not definitively established.

**Cognate Evidence:**
The word is cognate with related terms across multiple languages, including Northern Kurdish *eynî* and *în*, Central Kurdish *heynî*, Zazaki *îne*, Sogdian *āδēnē* (meaning "Friday"), and Khwarezmian *āδēnek* (also meaning "Friday"). This linguistic network suggests the term's roots extend across ancient Iranian language families.

The underlying semantic connection appears linked to concepts of "appointment" or "gathering," though the precise semantic evolution remains somewhat obscure in the available sources.
```


## [2026-09-05T20:07:33.156Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD azen/ewen\"; grep -n \"āzēn\\|azén\\|ēwēn\\|ewén\\|éwén\" PHD.txt | head -20; echo \"=== NYB\"; grep -n \"ēwēn\\|āzēn\\|gyān\\|ādēn\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep PHD/NYB for ewen azen gyan"
}
```


### [2026-09-05T20:07:33.229Z] TOOL RESULT

```
=== PHD azen/ewen
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
1208:chase (v.)  pazdénidan, tazénidan.
1215:chess Catrang; (pieces) K šah, Q frazén, B pil, Kt asp, R mādayār, P payādag.
1238:circumstance čē-ēwēnagīh.
1473:ar. custom dastwarih, éwén(ag). customary šūnīg.
1976:flow (v.) āšixtan, réxtan, taxtan, (tazidan); cause to ~ tüxtan, tazénidan.
2010:form (n.) brahm(ag), čihr, dēs(ag), éwén(ag), gēn(ag), jadag, kālbod, kirb; of the same — hamdēsag.
2299:homogeneous haméwénag,
2331:how čiyēn, čē-ēwēnag.
2525:kind (n.) gón(ag), sàn, sardag, šēn; of the same ~ haméwénag.
2821:mirror ēwēnag.
3190:pour āšixtan, réxtan, tüxtan, tazén- idan; ~ out wéxtan.
3251:properly pad ēwēn.
3259:propriety ēwēn(ag).
3490:run dawīdan, (dawistan), póy-, tax- tan, (tazidan); (daevic) dwāridan, (dwaristan); cause to ~ tàxtan, tazénidan.
4297:weigh saxtan, tarazénidan. weight garanih.
4456:tabangog tabarzad tabišn taftīg taftan taz- tazàg tazén-
4471:tar, tarr tarazén- tarāzēnīdan tarāzūg piht
=== NYB
333:äivenak [’dwynk'] kind, sort, species, genus 478, 3917, 7611, 8028, 9417-20, 1083.10; nature 100!4; — manner: pat han =, pat én ~ in this, in such a manner; being in such a state; thus: 1129-21, 3416, 8519; the thing (event, situation) being so, connected with ditan 21. 322, 917.27, ]]6.14, 123. 1215; with āšnūtan 814, — cë ~ A813, pat ce ~ 1620.21, 788 how?; pat ciš-ic ~ ma 708, pat hec ~ ... ne 792-3 in no way, by no means; pat han ~ ka griyét so that he is weeping 11"; — pat ~ i guaršet like the sun 441?; pat Susr ~ some- thing like a sperm 95!7; pat ēzanišn ~ by (means of) killing 103%; har 2 — in both respects 110%, — MPrs ’ywyng (S, A-H JI), yng (List 80); Paz. dina, ŠGV àinaa, Skr. v. prakära, SGV also vidhà, riti. [MPrth ”dyng, List 79, NP Ginah ‘mirror’ seems to go back to *ä- dayana-]. — Note: — NP ädinah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it (v. above s.v. ātvēn); it probably goes back to MIr *atēnak < Olr *ati-ayana- (OP ati-ay- ‘to go along’), ci MPrs 'dyn ‘entrance’ (S, A-H II), with secondary lengthening of the initial a-: *ādēnay ‘congregation’. — V. also ham-ātvēnak.
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
3847:ulēh [L’L’-yh], wë [+ -c: D’L’y-c] up- wards, above: pat uléh emphasizing the prev. ul in pat uleh ul nikérit 51%*-*%; pat uleh ul vāzēnēm 60°; — ule-c on high 42). - Cf Av. (351) loc. orodvaya ‘in upright, standing position’; cf also nıküneh.
4059:vizčnitan [w’cynytn'] to bring, to take a p. to a place (andar) 49?’; to lead (a horse) up to (0) a p. 5413-15; à tē pat ulēh ul vāzēnēm we shall carry thee up in the air 60%. — Caus. of väzitan.
4060:vāzēnītār one who draws, pulls: asp i rahy ~ a chariot-horse 581”.
```


## [2026-09-05T20:07:34.457Z] TOOL CALL #30: WebSearch

```json
{
 "query": "فارسی آذین ریشه‌شناسی حسن‌دوست فارسی میانه āzēn آیین"
}
```


### [2026-09-05T20:07:42.266Z] TOOL RESULT

```
Web search results for query: "فارسی آذین ریشه‌شناسی حسن‌دوست فارسی میانه āzēn آیین"

Links: [{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد - ایبنا","url":"https://www.ibna.ir/news/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"بررسیِ «فرهنگِ ریشه‌شناختیِ زبانِ فارسی - پارسی انجمن","url":"https://parsianjoman.org/6278/%D8%A8%D8%B1%D8%B1%D8%B3%DB%8C%D9%90-%D9%81%D8%B1%D9%87%D9%86%DA%AF%D9%90-%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C%D9%90-%D8%B2%D8%A8%D8%A7%D9%86%D9%90-%D9%81%D8%A7/"},{"title":"بررسیِ «فرهنگِ ریشه‌شناختیِ زبانِ فارسی","url":"http://parsianjoman.org/?p=6278"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"}]

Based on the search results, here's what I found about your query regarding Persian etymology and Hassan Doust's work:

The "Farhang-e Riešeh-šenāxti-ye Zabān-e Fārsī" (Dictionary of Persian Etymology) is a specialized dictionary for Persian etymology authored by Mohammad Hassan Doust, published in 2014 in five volumes by the Iran Academy of Persian Language and Literature.

The book was recognized as a distinguished work in the 33rd cycle of the Islamic Republic of Iran Book of the Year Award in the "Ancient Languages" category.

The work traces each Persian word back to its origins in Middle Persian or Pahlavi, and earlier forms in ancient Iran, then traces the word's root.

The main text of the Persian Etymology Dictionary (letters A-Y) is contained in the first four volumes, comprising 2,955 pages with 5,514 entries.

The search results show that Hassan Doust's etymological work is a significant contribution to Persian linguistic studies, providing comprehensive historical and linguistic analysis of Persian vocabulary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:08:03.718Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "BQT metadata"
}
```


## [2026-09-05T20:08:04.778Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"SOGDICA\" HENNING_selected_papers.txt | head -5; echo \"=== azin sew\"; grep -n -i \"āzīn\\|azin\\|to sew\" HENNING_selected_papers.txt | head -20",
 "description": "Find Henning Sogdica"
}
```


### [2026-09-05T20:08:05.658Z] TOOL RESULT

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
```


### [2026-09-05T20:08:05.729Z] TOOL RESULT

```
158:SOGDICA
898:18 SOGDICA
=== azin sew
846:Commentary: (2) The MPers. form ocours in Mir, Man., i, see Bailey, BSOS., vii, pp. 84 sqq. Sogd. =“‘he is vehement, ardent, impetuous” (lit. “one whose desire is opened, loose ")—(3) “ They y.""—(4a) “Without hurting, enmity,” see BBB., p, 53 (on 483)—{48) Sogd. 2nd sing. subj., =“ you should mix.” There. fore dé participle of necessity —(5) MPers. “thoy are being collected, guined, saved”, Sogd. “ itis collected, see BSOS., x, p. 1 (cf. BBB., p. (7a, 8a) MPers, “bzyn-"" to sew, tailor ” is fre
854:quently met with in Mir BSOS,, ix, 80. Cf. ZIL, ix, p.214; Horn, Gr. Ir. Pers. dzin-: dsidan “to sew. See also B. Geiger,
20489:«To buy * Supplied from Kearavi (had) * Of, seri (ink) “to fee" Kearavl ertmin (abore p. 108, n. 1) = vert na To sew.” * Supplied from Kesravi
21082:Not only wi- becomes i (cf. also ‘wsye «twenty», ‘wid «widen, but also wr, eg. ‘wr(y)k «wolf» (fem. ‘wrk’n), ‘wipk «hunger, ‘wiynd «hungry», ‘winyeyk «male», ‘wEnyk «neighbour» (AV, varazinya-). -h- is mostly lost (eg. s’k «hare», n'c «nose»), but sometimes maintained (w"h «price», pxw'h-nye pteple. from pxy- «cut», Sogd. pxw'y-; hwny «blood»), sometimes added (1° «thief» from tdyu-, hrs «bear, h’ké «mountain goat», Wakhi yuks), -)- is lost after -s and -d- (s'w «black», ksb «tortoise», mé'n «middle»). Initial xw- becomes ux- or ax-, but sometimes x-, cf, "x «sister» = uxa (from xwahd), ‘xy «sweat, mayd «he beat» (Oss. xvayun), but xyr «sun» beside ‘xr, xsr «father-in-law»; xwd- remains or is axwie, e.g. "xw'dk «weak» (Sogd. xt), beside which we find mx’st = mux(x )dis-t « grew tired» (Sogd. xw's-, Parth. wx’). While -Ow- appears as ~/-," ofr «four», ¢f'rys- «forty», as in Parthian, -diw- becomes -68- as in Sogdian, e.g, dfcy, Sfleym «second», 82k «thick», 5Br «door», ‘rBPk «erect» (Av. aradwa-), 6f'ny~ «winnow» (see IIFL., ii, 222), bSpzydh whe unfolded, spreat out», intrans. impf. b'6fxsyd, participle b’éfycyk (cf. Sogd. wydfiys-etc.). Similarly, z  [s0, not 2k] «tongue». Irregular for-w- perhaps in fc (?) «rice», Byk «mark, (warna-?), and b2'B'r «lean, cf, Pers. nizar (if indeed from mi
23413:ba Sulfaqar(-i)? ‘aql guSayi saxYan *pa-2ir? faryid azin zamine *azin *qahr{-i]# marduman faryid azin zamine zamine-i® sitingic*
```


## [2026-09-05T20:08:18.930Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor leaf in (18,370,375,376):\n    print('=========== leaf',leaf,'(printed ~',leaf+540,')')\n    print(t[leaf][:2200])\nEOF",
 "description": "Print BQT v2 leaves for jan/din pages"
}
```


### [2026-09-05T20:08:20.805Z] TOOL RESULT

```
leaves 684
=========== leaf 18 (printed ~ 558 )
  ‫"‪٩‬‏چحص‬   ‫سب ‪۵‬‬
                                                                                                  ‫جاندارو‬

                       ‫وآب حیات را هم میگویند ‪.‬‬           ‫همآمده است ‪٩‬‏ ‪ -‬ورزق‌وروزی وقوت لابموترا‬
                                                                                             ‫لیز گفته‌اند ‪.‬‬
‫الت و قاف بتحتالی‬             ‫سقیک‏ون‬
                                    ‫جبا ف‬
‫کنکاش کردن و مصلحت‬              ‫و‬    ‫‪٠‬‏ مشورت‬   ‫کشده‬      ‫جاند ارو ۔ کنابه از ترباك است‬
 ‫و صلاح دیدن جممی باشد باهم » و محذف‬                                                 ‫که افون باشد ‪*.‬‬
‫‪O‬‬                       ‫است ؟‪ .‬‏‪E‬‬                          ‫جاندا نه= بورزن کارخانه » اپزیش‬
                                                         ‫صرجایی راکوبند که در کودکی ارم و چهنده ‏‬
‫جان گزا ‪ -‬بفتح کفاافرسی و زای‬                                          ‫هیب‌اشد » و بعریی بافوخ گوبند‪.‬‬
 ‫دار بالف کشیده » کاهنده واشت رسائندة‬              ‫شمه‬
                                                         ‫ایهه از آست که‬
                                                                      ‫نان‬
                                                                        ‫کمی‬
                                                                          ‫جان ذر‬
 ‫جافراگوبند ‪ -‬وروح حیوالی را هممیگویند ‪-‬‬
                                                                     ‫مرا باتو بجان مضایقه یت ‪.‬‬
‫وحیوانات موذی و غیر موذی باشد از سباع‬
             ‫وبہایم ‏ وزهرفاتل را لز کونند ‪۶# .‬‬           ‫جان مین ه کنابه ازبزه وگل‬
                                                                                              ‫وصوه باشد ‪.‬‬
‫جانوسار ت باسین بلیقطه بر وزن‬
‫دارای‬      ‫بوره همدالی ملازم‬        ‫کاهوزار ‪ ۰‬تلم شخصی‬   ‫جان شکر = بکر شین قطه داروفتح‬

‫واو دارای صاحب خود را در‬                  ‫ابن دارابن ‪.‬‬    ‫کاف وسکون رای قرشت * شکار کنندة جان‌باشد‬
‫جنگه سکندر بفریب ومکر وحیله بقتل آورد‬                     ‫بعنی عزرائیل » چه شکر بمعنی شکار است ‪-‬‬
‫و سکندر لیز او را ببب فتل دارا بجهنم‬
                                            ‫فرستاد ؟‪.‬‬    ‫جان فزا ‪ -‬لامروز بیست وسيم آست‬
 ‫جائوسیا
=========== leaf 370 (printed ~ 910 )
 ‫=‬                                                                                                    ‫دیع‬

‫دیده بان ‪ ۲‬س بروزنبی‌زبان» همان‬                           ‫یدبدا س بفتح اول بروزن شیدا » بمعنی‬
            ‫دیدیان است که بعربی ربیثه خوائند ‪.‬‬                                      ‫وم شده باشد ‪.‬‬
                                                                                                ‫تاپیدا ک‬
‫دید بانان عالم ت کنابه از هفت‬
                                                          ‫د دار ‪ ۱‬عم بر وزن دیوار » ترجمهةٌ‬
‫ک وکباست کهزحل‌ومشتری‌ومرشو فتاب‌وزهره‬                     ‫روت است ‪ -‬وبمعنی رخ وروی وچهره باشد ‪-‬‬
                             ‫وعطارد وماه باشد ‪.‬‬           ‫ویمعتی رخ لمودن ردیدن هم هست ‪ - ۴‬وچشم‬
‫دید م بان فلك ‪ -‬کنابهاز کوکبزحل‬                           ‫ویاعيننند ‪ -‬و ببنابی‬  ‫خرب‬
                                                                                  ‫کاویبزندکه یم‬‫ر‬
                    ‫است که درفلك هفتم میباشد ‪.‬‬             ‫وقوت باسرء رایز کفته‌اسوبمعنی پیدا ویدیدار‬
 ‫دیده بان کبود حصار ک‪-‬نابه‬                                                                          ‫همهت ‪.‬‬
‫از زحل است ‪ -‬وهربك اکزواکب سبع سیاره‬                       ‫بابای‌ابجدبروزن رسمان‪,‬‬        ‫دید بان ‪۴‬‬
                          ‫را بگیوزبند ‪.‬‬                  ‫شخصی را کویند که برجای بلند مانند سرکوه‬
‫‪ ۵‬بك ه بر داشتی د کنابه از منتظر‬                           ‫و بالای کشتی شیند وهرچه ازدوربیند خبردهد‬
                      ‫بودن وانتظار کشیدن باشد ‪.‬‬                          ‫نند ‪#.‬‬   ‫ایه‬‫ور‬
                                                                                      ‫خریی‬
                                                                                         ‫و او را خ‬
‫دة لشت = منم بای فارسی ‪ .‬اشاره‬
                             ‫د‬                             ‫‪ ۵‬بد ه = بااول بثالی رسیده وفتح‌ثالك‬
        ‫بمنفذ سفلی است که صوراخ مقعد باشد ‪.‬‬
                                                          ‫چشم را کوبند (‪ -)۱‬و بعضی مردمك چشم را‬
‫ذبده دار د بروزن کیسه دار» بمعنی‬                           ‫گفتماند؟ ‪ -‬وبمعنی‌مرگی ومشاهده شده‌باشد ‪۵‬‬
‫دیده بان است
=========== leaf 375 (printed ~ 915 )
                                                                                                                       ‫‪--‬ي ‪۱4‬‬


‫بر وزن ریبوای » نرجمة‬                ‫دیماس ‪1‬‬                        ‫عربی سختی‬        ‫ر‬
                                                                                     ‫دو‬‫باشد ‪- ۱‬‬                ‫ویچك‬
                                                                                                                  ‫ککه ن‬
‫ظاهر گردسن‬       ‫‪0‬‬       ‫باشد که از واضح شدن‬       ‫توضیح‬
                                                                    ‫گروایند ‪ -‬و جابیرا‬        ‫وه‬
                                                                                               ‫ارن‬
                                                                                                 ‫ززمکا‬
                                                                                                     ‫و محنت رو‬
                                                   ‫‪.‬‬    ‫ا‬           ‫نیز گفته‌اند که مردمان وهورچگان درآ نجاجمع‬

‫یدماطی ‪ -‬با طای‌حطی‌بروزن میقانی؛‬                                                                                      ‫شوند ؟ ‪.‬‬
‫بخار سوخته راکوبند که ازبرق بهم حیرسد وبر‬                           ‫دیلمان ‪ « ۴‬بر وزن بیزبان ؛ بمعنی‬
‫سوخته‌آن سیمایر | منمقد گرداند؛‬               ‫جاحامخورد‬
                                                                             ‫رهی باشد اگزیلان ‪.‬‬ ‫هست ک‬
                                                                                                    ‫شم ا‬
                                                                                                       ‫دیل‬
‫و بعی گویند دیماطی لوعی از ستگت است که‬
                                          ‫در دریا مباشد ‪۰‬‬
                                                                    ‫ی‪۵‬لهاث ‪ -‬بااول بثالی مجهول کشید‪.‬‬
                                                                     ‫لوری‬
                                                                        ‫ا»‬‫وسکون ثالث و میم مفتوح یکاف زحده‬
‫دیماو ند ‪ = ۷‬بفتح واو وسکون لون‬
                                                    
=========== leaf 376 (printed ~ 916 )
  ‫‪6‬‬                                                                                                     ‫دیمیاد‬

‫دلن ‪ - ۴‬بکر اول بروزن سین ‪ ۰‬نام‬                       ‫روشنی وضیا بود ‪ -‬وغله ای را نکیوزیند که با‬
‫فرشته‌ابست که بمحافظت قلم مأموراست ‪ -‬و نام‬              ‫آب باران حاصل مشود ‪ -‬و بمعنی باران وشم‬
 ‫روز بیست وچهارم بود از ماههای شمی ‪ .‬نيك‬                ‫حم آمده ؛ و بعضی گوبند بمعنی باران عربی‬
 ‫است درین روز فرزند بمکتب فرستادن و نکاح‬                                                              ‫‪١‬‏ ‪.‬‬    ‫ات‬
  ‫کیش‬
    ‫کردن ‪ - ۴‬ودر عربی بمعنی راه وروش و‬                 ‫هیا ‪۲-‬با بای حطی بروزن دبوزاد ‪.‬‬
                                                                                     ‫د‬
 ‫وعادت و فرمان برداری وشن وشو کت و مرتبه‬               ‫آنست که‬
                                                             ‫و آ‬             ‫باند‪.‬‬
                                                                                 ‫تکفسو ر‬          ‫غررور‬
                                                                                                      ‫ک‬
 ‫_ومالك ‪ ,‬یادشاه باشد ‪ -‬وبفتح اول هم درعربی‬
                                                        ‫اموال فانِةٌ خسبه را در نظر نیاورد وبربذل أن‬
                            ‫فرض و وام را گویند ‪:‬‬                                                  ‫فادر باشد ‪۱‬‬

 ‫دیا = بورزن بینا * نام خواهر بوسف‬                      ‫دمین = ‪,‬کر اول و انی مجهول بر‬  ‫ی‬
 ‫علیه‌اللام است ‪ -‬ویمه‌نی داور وداوری و فتوی‬             ‫وزن مين » چلك بازیرا گویند وآن دوچوب‬
                       ‫نوشتن حم آمده ات ® ‪.‬‬
                                                        ‫دار سه وجب و دیگری بقدر بك‬
                                                                                 ‫م یقکی‬
                                                                                      ‫ابست‬
‫د ينار ‪ = 1‬بر وزن بیمار » زر سرخ را‬                     ‫قبضه وهردوسر جوب کوچك تيز میباشد واکثر‬
‫همچو تمام‬        ‫همست‬
                    ‫‌تم‬
                      ‫می م‬
                         ‫هعن‬
                           ‫بم‬            ‫ام‬
```


## [2026-09-05T20:08:40.524Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (374,375):\n    print('=========== leaf',leaf,'(printed ~',leaf+540,')')\n    print(t[leaf])\nEOF",
 "description": "BQT p.914-915 dim"
}
```


### [2026-09-05T20:08:42.847Z] TOOL RESULT

```
=========== leaf 374 (printed ~ 914 )
 ‫‪-4۱-‬‬                                                                                      ‫دنگ‬
                           ‫آهنین باشد ‪٩‬‏ ‪.‬‬       ‫واز بونه برآورند تفلکه در ته بوته مانده باشد‬
 ‫د یگ بر دینگ = بکسراولوسکون‬                     ‫مرقشیشاست » وآنرا دیفروجس بحذف الف یز‬
                                                ‫کفته‌اند ‪ .‬چون ارا سحق کنند وبرموی غلیظ‬
‫کاف آخر بر وزن بیخ ببریخ » م رکه موش‬                              ‫افشانند رقیق وترم کرداند ‪#.‬‬

                                                  ‫دلگ » بکسراول وسکون‌انی معروف‬
                                                ‫و کاف فارسی » بمعنی دی باشد که روز گنشته‬
                                                ‫است ‪ - ۱‬و بعربی خروس را کوبند ‪ - ۴‬و با‬
 ‫خسس‬   ‫و‬   ‫و دال بی نقطه ‪ ,‬کنابه از مردم شل‬
                                                 ‫تحتالی مجپول» ظرفیکه درآن چیزی پزند؟ ‪-‬‬
                                     ‫باشد ‪3.‬‬
                                                 ‫وتوپ بزر که رالیز گویند که بدانکلوله برقلمه‬
‫دیل ‪ -‬بر وزن فل » بمعتی تقعاه است‬                                                        ‫اندازند ‪.‬‬
 ‫که طرف خط باشد چه‌تعرف نقطه بطرف خط‬             ‫دیگ افز ار ‪ - ۴‬افزار دبک را‬
‫کرده اند ‪ -‬ودل را نیز گوبندکه بعربی قلب‬          ‫گوند‪ .‬یعنی آنچه دردیگه طمام ریز ندازنشود‬
                                                 ‫و کشمش وبادام وفلفل ودارچینی وقرلفل وزبره‬
‫کوسفندان وکاوان و دیگر چاریابان در آنجا‬          ‫ومانندآن ویعربی تابل خوانند وجمع‌آن توّابل‬
                                     ‫باشند ‪.‬‬             ‫است ‪ -‬ودنگه بزر که را نگیفزته‌اند ‪.‬‬

 ‫دیلم = با اول بتحتالی مجهول رسینه‬               ‫دیگ اورار ‪٩‬‏ با واو بوررن‬
 ‫اکیلان‬
      ‫وفتح لام وسکون میم‪ ,‬نام شهپری است ز‬        ‫ومعنی‌دیگه افزاراست که نخود وبادام کوشمش‪-‬‬
 ‫وموی مردم! لجاپیچیده ومجد میباشد و یشتر‬                   ‫ردنگه بز ر گے باشد ی‬     ‫وداروی کرم ‪۳‬‬


 ‫حربة ایشان تبر هیزم شکنی و زویین (‪ )۱‬امت‬        ‫‪-‬عنی‌دیکدان وسه با‬
                                                                  ‫دیگ پایه بم‬

                                                                   ‫(‪ )۱‬چك‪ :‬ژوبین ‪.‬‬

                          ‫تازی ‪.‬‬   ‫ک)اباف‬
                                        ‫‪ ( ۴‬عر‬                      ‫‪.‬‬   ‫‪ :‬دی‬   ‫رك‬    ‫‪۱‬‬


   ‫(دبکه)) از بارسی باستان_ ‪861120‬‬     ‫بقول هوبشمان دنگه فارسی (اففالیع ع‬            ‫‪۴‬‬
  ‫کردی ع‬     ‫ید بد آمده‪ .‬عکل بهلوی ‪gêd‬‏ (دنگه) هیأت عازه انت از آن د هوشمان ‪>» 14۹۵‬‬
  ‫‏‪ , dîzik‬افتانی ع ‪ . 26060 , 884‬بلوچی ع‪ 1862 1064 . 21 4‬وخی‌وسر بکلی‬
       ‫‪ = ۴‬دیکه اوزار ‪ .‬رك‪ :‬افزار‪.‬‬             ‫‪ « 8‬اسشق ‪ . 4۹۰۰‬کیلکی ‪ » 81‬ورك‪ :‬دیز ‪.‬‬
   ‫‪ - ۱‬ویز نر واقم راگونند (کاه شماری‬              ‫‪ = ۵‬دبک افزار ‪ .‬رك ‪ :‬اوزار ‪.‬‬
  ‫‪ ۵‬ببنقل آزفپرست کتابخانة مجلس شورای ملی بنقل ازترجمةٌ فارسی صورالکوا کب عبدالرحمن‬
  ‫‪ = ۲۷‬عاوناعدا‪( »2‬فر) «لك‪ ۲‬ص ‪- ۸ ۰ .۱2۱‬کیلکی نبزاقل‪.‬رك‪ :‬مد‪.‬‬                    ‫صوفی)‪.‬‬
                                              ‫‪ #‬دضاقوس ‏ رك‪ :‬دیشافوی ()‬
   ‫‪ #‬دیگر ‪ -‬بکسر اولوفتح سوم» پهلوی ‪lj_arak :1۱26101‬‏ _ ‪« ayîtivd#‬اسفا‪»۱‬‬
   ‫‪ ۹۸ ۱‬و‪ ۷0-‬درکلمه ‏ ل ‪ ,‬پازند ‪ 7381021‬فارسی دیک ‪.‬قس ‪ :‬پهلوی انل دریبکه‬
  ‫‪ ۷‬ورك‪ :‬اسشق وهوشمانه‪ . ۹۵‬مخفف آن «دکر» (ه‪.‬م‪ ).‬؛ کلمه‌ای که بیان میکند شخص با‬
  ‫چیزی‌را علاوه برشخص و چیزی که پیش بیان کرده‌اند » علاوه» زباده » باز ج*زازین ‪ .‬جز از‬
                                                            ‫آن ‪ .‬مخفف آن د«دکر» (ه ‪ .‬م‪).‬‬

=========== leaf 375 (printed ~ 915 )
                                                                                                                       ‫‪--‬ي ‪۱4‬‬


‫بر وزن ریبوای » نرجمة‬                ‫دیماس ‪1‬‬                        ‫عربی سختی‬        ‫ر‬
                                                                                     ‫دو‬‫باشد ‪- ۱‬‬                ‫ویچك‬
                                                                                                                  ‫ککه ن‬
‫ظاهر گردسن‬       ‫‪0‬‬       ‫باشد که از واضح شدن‬       ‫توضیح‬
                                                                    ‫گروایند ‪ -‬و جابیرا‬        ‫وه‬
                                                                                               ‫ارن‬
                                                                                                 ‫ززمکا‬
                                                                                                     ‫و محنت رو‬
                                                   ‫‪.‬‬    ‫ا‬           ‫نیز گفته‌اند که مردمان وهورچگان درآ نجاجمع‬

‫یدماطی ‪ -‬با طای‌حطی‌بروزن میقانی؛‬                                                                                      ‫شوند ؟ ‪.‬‬
‫بخار سوخته راکوبند که ازبرق بهم حیرسد وبر‬                           ‫دیلمان ‪ « ۴‬بر وزن بیزبان ؛ بمعنی‬
‫سوخته‌آن سیمایر | منمقد گرداند؛‬               ‫جاحامخورد‬
                                                                             ‫رهی باشد اگزیلان ‪.‬‬ ‫هست ک‬
                                                                                                    ‫شم ا‬
                                                                                                       ‫دیل‬
‫و بعی گویند دیماطی لوعی از ستگت است که‬
                                          ‫در دریا مباشد ‪۰‬‬
                                                                    ‫ی‪۵‬لهاث ‪ -‬بااول بثالی مجهول کشید‪.‬‬
                                                                     ‫لوری‬
                                                                        ‫ا»‬‫وسکون ثالث و میم مفتوح یکاف زحده‬
‫دیماو ند ‪ = ۷‬بفتح واو وسکون لون‬
                                                                    ‫است شبیه بعنكبوت ولعاب اومهلك میباشد اوو‬
                         ‫و دال ‪ ۰.‬تام کوه دماو ند ادخ ‪۰‬‬
                                                                    ‫را بعربی رتبلا خوانند ‪ -‬و بفتح ثالث صفیردیلم‬
 ‫دیمر * س بر وزن دیگر > بمعنی دم‬                                                                                           ‫ام‬
      ‫باشد ویعربی خد گوبند ‪.‬‬               ‫است که رخاره‬
                                                                    ‫كلم = بسکون انی بورزن جیم ‪ ۰‬روی‬
‫یند» مخفف‬       ‫دل‬       ‫بروزن‬   ‫د بمو فك ‪= ۲‬‬
                                                                    ‫ورخاره باشد وبعربی خد گویند ‪ - ۴‬ولوعی‌از‬
      ‫دیماوند است که ناکموه دماوند باشد ‪.‬‬                           ‫چرم هم هست که سازی ادم خوانندش ‪ -‬وبفتح‬

                                                                     ‫انی در عربی جمع دیمه است که باران سخت‬
‫روی ورخاره باشد ‪ - ۸‬وبفتح اول بمعنی‬                                                                ‫باشد ® ‪.‬‬

  ‫‪ ۰‬شهرستالپای ابرانشپر‬              ‫» مار کوارت‬       ‫‪mulêD‬‏‬        ‫‪ ۰‬بهلوی‬    ‫قومی حاکن دبلمان‬           ‫‪۳ ۱‬‬

                                                       ‫‪ ۳‬و‬
                                     ‫‪-‬یمعنی شده و غلام ‪:‬‬                         ‫‪.‬‬   ‫ص ‪۹۷ ۸۷۰ ۷۷۰ ۰ ۲۵ ۰ ۱۳۳‬‬
       ‫هندو شه تکسرتان‪.‬‬                  ‫امبلكل»‬
                                               ‫بلم‬
                                                 ‫دب‬                  ‫در که کورا زشهان ودی‬         ‫همان‬     ‫این است‬

  ‫« خاقالی شروألی ‪. ۳۸۹۳‬‬
‫از ‪ :‬دیلم ‪ +‬ان (یسوند) ؛ مکلن دیلم ها ‪« :‬لاحت دیلم ناحیتی است آبادان و با‬                                          ‫‪۴‬‬
 ‫خواسته ومردمان وی همه لشکری اند با برزعگر وزناشان فيز برزیگری کنند و اشان را هیچ‬
                       ‫شهوری بامنبر فیست وشهرشان کلارست و چالوس » « حدودالمالم ‪.*۷۸‬‬
 ‫‪ _ ۴‬اوستا ‪ , 820۳621 -‬پهلوی ‪ 08076002 ۲86‬پ(ذیرفته‪ .‬برده ‪ ۰‬مشتغل )؛‬
  ‫اورامالی‬    ‫ارمنی ع ‪mêd‬‏ » اسثق ‪٦‬ه“‏ »کروی ‪mêd‬‏ (روی) »افغالی ‪amêl‬‏ «هو شمان ‪۹‬ء‬
  ‫»هرودی و سمنانی ‪ 71‬ک‪,‬شه‌یی ‪ « 011‬ك‪ .‬اورامان ‪۲*۰ : ۱۲۱‬‬
                                                      ‫«ك‪ .‬اورامان ‪ ۱۲۱۰‬ک‬                                                    ‫‪0‬‬
  ‫رك‪ :‬دیمه‪:‬‬          ‫©‬           ‫‪.‬‬    ‫‪ e‬ورك‪ :‬دمه‬       ‫‪GAF‬‏‬    ‫طری‬    ‫(رو) » صاب‬      ‫‏‪ .dîim‬طر ی ‪md‬‏‬                  ‫کیلکی‬

       ‫نعاشه کس کشت باد » غاشة او دەم ‪.‬‬                               ‫رعد‪ .‬مقرعةٌ او درحش‬         ‫مقرعه ز ن گشت‬


  ‫«منوچپری دامفانی ‪٩۵٩‬‏ ‪.‬‬
 ‫«مضفی لماند که دیمای در کتب لفت عربی مثل قاموی و غیرآن بمعنی پوشید کی‬                                             ‫‪۱‬‬
  ‫بمعنی حمام ونام محسی‬               ‫شغال ز بر زمن کنده باشند و‬          ‫ویمعنتی خانه‌ای که حوانات مل روناه و‬

  ‫و طاهر‬     ‫و واضح شدن‬          ‫و اما یمعخی توضرح‬            ‫است‬    ‫أ‬    ‫‪۰‬‬    ‫يود‬   ‫ساخته‬    ‫که حجاح بن توسفب‬

  ‫کردیدن که مصنف آورده درهبچ کتاب از کت متداولة عربی وفارسی بنظر نرسیده ‪ « » .‬چك‬
             ‫رك ‪ :‬دماو لك‪.‬‬           ‫‪۷‬‬          ‫آست‪.‬‬    ‫از بر‌ساخته حهای فرقة آنر کوان‬            ‫‪۰‬‬   ‫وظ‬       ‫‪.‬‬   ‫‪۴‬‬   ‫ح‬    ‫‪°‬‬

                                                                                        ‫‪.‬‬    ‫دم‬    ‫رك‪:‬‬     ‫_‬       ‫‪4‬‬
```


## [2026-09-05T20:09:11.231Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor leaf in (239,240,284,285):\n    s=t[leaf]\n    print('=========== leaf',leaf, s[:900].replace('\\n',' ')[:900])\nEOF",
 "description": "Probe BQT v1 leaf numbering"
}
```


### [2026-09-05T20:09:12.802Z] TOOL RESULT

```
leaves 777
=========== leaf 239 ت برایو بی اه آرامی رة حواشی صفحة .۳ ۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین در پبرامون کوبر ومشرق رود اردن وبحرالمیت میزیستند. اين شبانان چلدرنشین ویابان نورد ازخوشاوسان تزديك اسرائیلیان بودند و بغلط برخی آنان را کلدانی خوانده‌اند . ازفرن ۱۶ق.م.. آرامیان به سرزحی‌های عتمدن همایبة خودروی آوردند ودست بفارث زدند. سوربه وشماق سسن‌النهرین میدان تاخت‌وتاز آنان گردید. در کتیبه‌های آشور متملق بال۱۳۲۰ ق.م. این قبابل اخلایه ۸۵۵۵6 ودرآ تار متاخرنر آرامه ۳81796 خوانده شده‌اند . شلمااسر 51181۳1310366 اول, پلدشاه آ شور در سال ۱۲۸۰ ق .م. با آراهیان در زد وخورد برد . انان بهرجاکه روی ۳۳ «مم [ ۵ | رارق انید ییا رید وی | دسج | مین کردند کتاورزان را بفرمان خود در آورده و بازر گانی ر بدست گر فتند ۳۰ جاوما جوا مج چ + | »| و بر راهپای کارواغی تسلط بافتند و در و اووا و ادووا <وا و :| و | و | دا سرزهین هابی که بچنگه آوردته از | و | همم ۱ ها دا جااب خود شهربارانی گماشتند . در و بو + ۳۰۹5 
=========== leaf 240 آرامی - پرایی ۷۲٩‏ س آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی‌است وآموختنش برای‌هزدم مأی زبان دشوار یست باخط آرامی که الفبابی.ساده بود سراسر کشورهای اقولم سامی نژاد را فرا کرفته از بلحرالروم نایشتکوه (زاگری) وخلیج قاری زبان. بین‌المللی محصسوب حیشد. هنگامیکه ابرانبان بسرزمین‌های آشور وبابل وآسبای صفیر وسوربه وعصر دست بافتند باافوامی سروکار پیدا کردند که زبان وخط وسیلهٌ ارتباط دبوان های دولتی هشامثشیان و متصرفات غربی ابران‌شد. درتوراة , کتاب عزرا باب4 بند۷ آمده: #در روز کار اردشیر اول(هخامنشی) بشلام 21520 ر مهرداد وئبیل [۲20 وباران دیگر آنان مخط آرامی و با ترجمةٌ آرامی نامه‌ای باردشیر یادشاه ابران نوشتند. » ازفرائن پیداست که خط میخی برای‌حوائج روزانه بکاردمیرفت" واین‌خط برای کنده کری اختصاص داشت " اماالفبایآرامی با ۲۴ حرف برای کتابت آسانتر بود . خط سکه‌های محلی دور حضامنشی و وزنه‌هابی که رویآ نبا خط آرامی نوشنه‌شده وخط بیاری ازمهرهای ابرانبان که ,خطا آرام یکنده کری‌شده » بخوبی
=========== leaf 284 اسکنف‌دی؟ - آینه‌ای‌بود ازعنرهای ارسطو " که ابجهت آگاهی از حال فرنگه بر سر منارٌ اسکندربه که در حدود فرنگه برکنار دربا بنا کرد اسکندریود اصب کرده بودند. شبی‌پاسبانان غافل شدند و فردگیان فرصت یافته آنرا درآب اساختند و اسکتدربه را برهم ژدند » و عاقبت . ارسطو آترا از آب‌بیرون آورد- و کنابه از قتاب ح‌ حست .۰ آینه آسمان و آئیتة آسمان - ونخلوق خواهند؟ . آلن « تح الث بر وزن و حمنی آهن آ دنه و ]دنه که صورت چزها در آن‌نمابان کردد و کاهی از فولاد یز سازید , آینة دستی 7 بنة اسکنددی و 7ینف «لت‌نامه». .۰ ۴ - پپلوی2162021 «منای »۷4٩‏ وعق20۵0» بارنیآدینگ ۹۷۵8" رد : 0۸6 18 ابر صمنطا:2 200 عبمم عازن ۲ اک ۸بع‌دنجدهع۲۲ ۱۷/۰8 (۰ 0,79 ۸ ,۷۵ در بلوچی 2060 , حاعهتع۵0 ,حعط20 ,2202 « جیلبرتسن +4۲ » مشثق از ربشة له (پارسی باستان 9 بیین . پارسی دبدن) , یمنی آلتی که خود را در آن بسیننه « از افادات ذغاهی استاد حنينك » : فرستاد از آن آهن تیره رنگ یکی آینه کرده دوشن ز ژنگه. فردوسی < لفت نامه >. ۴ - در نظم وش پارسی «1ب
=========== leaf 285 .کنایه از آ غاب عالمتاب باشد . ] بنه اق و ز و آیینه افر ود - صیقل گر و روش نکر را کوبند » و آن شخصی باشد که چیزها را جلا دهد و صقل کند . 3 آینة چرخ و آینة چرخ - بععتی آبنهٌ آسمان ابت که کنابه از خورشد جهان آرا باشد . آینة چینی و آئینه چینی - آبنه است که ازتال‌سازند وآنرا بعربی«سجنجل» اف بت ۱ آینةخاودی و آیینة خاودی- آبنه دار و]بینه داد ۰ سرراش و حجام را گویند ۴ آبنه ددای و آئنه زدای - بمعنی آیینه افروز است که صیقل کر و ردشن هو تاعروس‌وحجز ی آییژ + ۵ صفیر آینة شش جهت و آیینة ششی هت « آشاره بر دل سرور کاینات است صلوات اف علیه - و کنابه از اسحاب کهف باشد - ورجال الغیب راهم کنته اند ومشاهدات راز گونند . ۱ آبنه فرور و آیینه فرود - بیعتیآبینه زدای است که صیقل کر وروش نکر باشد . آینة گر دان و آبينةً "ار دان- باضافت فو ی ان صمت: ام 9 با زای و شرار؛ آش راگوند ۴ . ۳ رو و و زشت و آرایش س پر وزن پایین » بمعنی زیب است ۷ و رسم و عادت و طرز ۴ نیز, آنکه آیته دریش دارد ۴ - ئز بویمادران ؛ ائث» آیدو ایدهم
```


## [2026-09-05T20:09:30.716Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor w in ['آذین','آدینه','آدنه']:\n    print('###',w)\n    for i,p in enumerate(t[:400]):\n        if w in p:\n            print('  leaf',i,'printed~',i-210)\nEOF",
 "description": "Find azin/adine leaves in BQT v1"
}
```


### [2026-09-05T20:09:32.441Z] TOOL RESULT

```
### آذین
  leaf 237 printed~ 27
### آدینه
### آدنه
```


## [2026-09-05T20:09:35.377Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (236,237,238):\n    print('=========== leaf',leaf)\n    print(t[leaf][:2600])\nEOF",
 "description": "Print BQT azin page"
}
```


### [2026-09-05T20:09:37.398Z] TOOL RESULT

```
=========== leaf 236
آخر کون نت
آ داد کش ها یکی کنق. و کون
بحتانی مجپول و شین قسرشت » آتش پرست را
کونند ؟ . #
آذر ۵ ه بفتح رابعم و سکون - میم ,
زین اسبی را کویندکه نمدزین آن دونیم باشد -
و بمعنی نمدژین هم آمده است ۴ .
آ ذد ماه - تم ماه هم است از مار
های شمسی » و ان بودن افتاب بود در برح
فوی ۴ .
]در نگ - بت الث بر وزن لاله
رنگ » بمعنی روشن و نورانی و آتش باشد ۵
و بمعنی رنج و محنت صعب وغم سخت وهلاکت
نیز گفته‌اند .
آذر نوش . بخم نون و سکون او
وشین ». بمعنی نوس آذر است و آن آنشکده دوم
باشد اجملهٌ هفت آتشکد فارسیان ۷ .
کویند - و بمعنی برق هم آمده است- و آتش-
ای رجا روط
فرشته‌ییت موکل بر آتش و پیوسته در آتش
مقام دارد ؛ و معنی ترکیبی آن آتش جهنده
باشد چه آذر بمعنی آش و کشپ بمنی‌جهنده
و خیز کننده آمده است واین‌منی مناسبتی نملم
ببرق دارد .
آذّد گون - جنم کاف فارسی و سَئون
واو و تون . نوعی از شفائق است که کنار
های آن سرخ و میانش سیاه می باشد » و بعضی
کون دکیاهی است سرخ رن که در میان آب
میروید - دمگر گفته‌اند که نوعی از بابونه است
و گل هميشه بپار را نیز کویند ۱ ؛ و حعنی
تر کیبیآن اس داد ات چه آند بسنی‌آاش
و گون بمعشی مانند باشد - ونلم اسی هم هست.-
و سمندر را هم میگویشد .
٩‏ - درعربی «آذربون». کیاهی‌است بباندی يك نراع » دارای بر گهای کشیده بطول يك
انگشت و گلهای سرخزرد . و بوی بد , و میان‌آن سیاه رن است . هوبت اب نگیاه هنوز تعیبن
شده دربونانی 8278۲108 206۲۵ مترادف ۷۷۱۵۵۲15 568630 (60۳۲۲۷۵ 56۳608) است.
تفصیلاتی که لو ند گان عرب در یاب این کیاه آورده اند «خحر باتخاب بن 06( و
کتاهمنع: ۵6۲ 2160012 ( کل‌همیشه‌بهار) گردیده‌است . «داثرة المعارف اسلام : آذرگون»
مت رد ِ مدع و «مزدستا ۱۸۷-۸ .
وا ۵ 1 دوف و ۷۳ ۵ مخفف آذر رنگ یمعتی آتش رنگه .
۹ - این همان آتشکده است که فردوسی آیرا « نوش‌اذر » خوانده جاي انرا بلیع داند
در لشک رکشی ارجاسب کوید :
شپنشاه لهراسب در شهر بلخ بکشتند و شد روز ما تار و تلخ
وز آنجا بنوش آذر اندر شدند ردو هیرید راهمه سر زدند . فردوسی
ی مزدسنا ۷۲ و )۳۵ »
و آذر کیوان - یکی از روحانیان بزرکث زرتشتی مماصر صفوبه . از حردم شیراز
با حوالی آن . وی ما بر ۰ از ردان خود بهندوستان . فتات . این
گروه بقفمت شمالی هند سفر کردند ودر پتنه ۳۵۸۳2 اقامت کزیدند (اواخر فرندهم هجری ).
آذر کیوان موسس فرفه‌ابت مذهب ی که قزر گینان ات ازادبان زرندی ۰ اسللام» برهمتی ومسیحی.
وی‌را زوالعلوم نب داده‌اند و منظوعه‌ای بناء *جام کیخرو» درشرح مشاهدات وی بدومنشسوست .
۰ 0۲۱60۵ 20۱۵ عظ1 0۲ . ]بام[) ۷۵0ن۱2 عم اعد , ۳0۵ . 7۶[
.20 ۷۵ .ورك : دمتان‌المذای و دساتیر . ۵ آذ رگشنب ره : آذرکشپ .
=========== leaf 237
7 در هما بون - بن‌ها . بابساحرهای
بوده از نسل سام و. خدمت آتشکده صفاهان
میکرد وذوالقرنین اورا به بلینای‌حکیم دادوبدین
پیب بلینای را جادوکر میگفتند ۱ .
است که بمجم مبعوث شد واو را « مه آباد »
یز گوبند و اسان لو را ۶ آثذر هوهنگان »
خوانند ۴ . #
]ذر اس ه با تحتانی بالف کشد.
و سین بی‌نقطه زده » صمغ درخت سداب کوهی
است ردر استقا بکار برند ؛ وفتح همر مه هم‌آهده
أست .
امتان آذر هوشنگه را گویند و او پیغمبر اولی
آذین
ادد ون ه بی وزن و صعنی
بهار باشد و شبرازیان آن را کل کار چشم ه
گویند - ونام نبانی است که شکوفه‌ای درنهایت
سرخی مي باشد . بر ورمهای صللب طلا کنند
افع آ ید .
آذون » بر وزن هامون . بمعنی آن
چنان باشد چنانکه ایدون بمشنی چنن است .
آ ذییش - بکس ثالث و سکون تحتالی
رشن‌فرشت ۰ چوبی را کوین که بر آمتانهٌ در خاده
اسنوار کنند - وبمعنی ریز چوب وخس وخاشالك
هم آمده است .
آی *ه بر وژن د معنی آبین است
که زب و زشت و آراش - و رسم و قاعده
وفانون باشد - و بمعنی آآت ی که روغرا از دوغ
جدا مبکند عم هت ۱. *
۴ - از بر ساخته های دساثیر .
(۷210 برابر دیدن) . رك : تس کت ۳.
۴ را : آند ن ۰
صه هصمحف باشد «لغت نامه" .
بود . رل : زبان آذری تألیف سید احم دکسروی سمیاپ ۱۳۰4 ۰ ۱۳۱۷ و ۱۳۲۹ نهران‌ومجلة
باد کار سال دوم شمارژ ۳ «يك سند مهم دریاب زبان آنری» بقلم آقای اقبال و «يك‌سند تاربنی‌از
کوش آذری‌تبریز» . - ترکان عثمانی و بتبم آنان خاورشناسان «آذری» را بلهجه کی معمول
درآ نربایجان اطلاق کرد‌اند . ره:دائرةالممارف اسلام: آنری۸2211. درمت نکتاب حاضر هفت لفت
ذبل از آنری نقل شدء ؛ ائبن » چارق , چرامینه » شم , کام , کنکی , ملاص . رل : هرك از
لغات مذ کور . ۱
# آد - (یوند) علامت فاعلیت : رل : ص, له از دیباچه , بعض معاسرانآنرا علامت
صفهٌ مبالفه دانند . «* قرب » دستور زیان فارسی ۱۳۱۰ ص ٩۳‏ » - علامت حاصل مهدرر » ره :
ص . لو از دبباچه » مسنی مماصران آنرا علامت اسم هصدر کگرفته اند . »
د قرب . حمانکتاب ص ۹۵ *.
=========== leaf 238
آرا
آداه بروزن خارا . آرایش. وآرایش
کننده و آراینده را کویند همچو خن آرا
و بزمآرا وامی باینمعتی هم هت ممنیآرایم
کن و بارا .
9
و پنجم است از هرماه شمی - و ام فرشته ای
باشد (۱) که حوکلست بر روز آراد . و اسور
ومصالح این روز تعلق باو دارد . کوبند: درایتروز
جامةٌ نو (۲) پوشیدن بیار خوست وسفر کردن
بیار بد .
آر ازذش » بکس زای هوز بر وزن
آسایش » بمعنی خیر وخیرات کُردن و درراء خدا
چیزی بکی دادن باشد (۳) ۶
1 مر رز تلم : بش
سکون و فرار - و طاقت - و اطاعت باشد .
و نی اکن شنت و فا گرفتن هم هست جت
ساکن شو وقراربگیر . - و بمعني جا و مقلم هم
امه کت < و کی با بر م۳ مر رین
شهر و صبه و ده باشد .
]رام لن - .بفتح بای ابجد و سکون
نون . بمعنی آخی آرام است که باغ میان شهر
و قصبه و ده باشد . ۱
ادامش س بی‌وزن ومعنی آمایش‌است
آد ات » بروزن باران . تام ولایتی‌است۴
وارنج را نیز کویند که مرفق باشد ۴
آرای بروزن بارای»آرایش وآراش
کتنند و آراننه وا کرد - و امر به آراستن
هم هت یعنی بیارا و آرایش کن ‏ :
آدایش ۹- بر وژن آصایش ه بمعنی
زب وزینت باشد - و رسم و عادت وآیین را نیز
کویند - و نام نوابی است از موسیقی .
] ر اش خور شید - نام لسن اول
ست از سی لحن باربد و خطی که بي عارض
7 3
آرت . بقتح ثالث و سکون فوفانی .
آرنج را گوشد که‌بند گاه ساعد وبازوست وبعریی
مرفق خوانند ۴ .
دج - ختح. ناك
فآ ات کم باشد ۷ - ونامپر ندم‌ای
آرد. بتح نله و ال ان
؟ ‏ رك : 1
آرت ۰ رد : : آرن
۰ رك : آرمیدن
۹ - رك:آران ۰
کردن » مهیا سلختن .
۳ هاده
کردن » آسودن . ساکن شدن .
```


## [2026-09-05T20:10:04.121Z] TOOL CALL #38: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py",
 "description": "Read ref_page.py header"
}
```


### [2026-09-05T20:10:04.158Z] TOOL RESULT

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
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-05T20:10:13.356Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (558,559,560,561,592,593,594):\n    print('=========== leaf',leaf,'| head:', t[leaf][:260].replace('\\n',' '))\nEOF",
 "description": "Probe BQT v1 leaves 558-594"
}
```


### [2026-09-05T20:10:15.172Z] TOOL RESULT

```
=========== leaf 558 | head: از "1 رن اه لیشه » بر وزن ربشه جنگل و نستانرا گونند و بعربی اجم خوانند؟ - وسازی هم‌هنت از ني, که شبانان نوازند. و بسنی کوشد سازیست شبه بچنگه » و بعضی دیگی گونند شبیه است پرباب . بیضه ] آشین «کنایدازآقاب‌عالمتاب و با انی معروف‌نلمبیخی است‌مهلك وکشنده ٩‏ شبیه بم
=========== leaf 559 | head: ۳۹۳6 سد بیقاد ه بنتح اولبروزن نیزار , سرزنش وطعنه باشد. بیغاره بر وزن گهواره » بمعنی بیفار ات که سرزش وطمنه باشد ٩‏ . بیغال » بکر اول بر وزن فیفال » بمعنی نیزه باشد که بعربی رمح خوانند .*# بیگار ‌- با انی محپول و کاف فارحی بر وزن بی زار , کار فرمودن بی مزد بود
=========== leaf 560 | head: بنم ثانث مر وزث میگفت اه ستارژ زهره را گوبند . بیلقان ‏ بنتح اول و و بر وزن نهروان ۰ شپرست از ولات اران مابین شروان و آذربایجان؟ . ۱ پادشانعان - و قبالة خانه و باغ و امثال آنرا کونند؟ - و تبربرا دز کنته اند که ییکان آن دو شاخ باشد - و بکر اول وئانی مجهول‌نوعی 
=========== leaf 561 | head: ۳:۱ ماه است که بعربی شه ر گوبندا . که مردمرا در حالت ماشفه دیده میشوده وآنرا مربی ممایثه کوش دریجهٌ خانه را گوند . بیناساك .. بسکون سینو کاف, بمعنی بیناس باشد که دربحهٌ خانه است ۰ رب بای فارسی هم‌آحده ۱ سست ه بنایی بروزن‌زیبابی» بمعنی‌دیده‌وری و بینند گی باشد 
=========== leaf 592 | head: پتفوز ود « بافا بروزن سردوز" کردا کرد دهان + منفارمرغان باشد ۱ و کردا کرد کلاهوا ی کفته‌اند. و بمعنی اول بحای حرف اول ى ی خاسك وچکش آهنگری من وامثال آن پروژن | گونند؟ . بتنگ بکر اول بر وزن درنگه , دربجه و منفذی را گود که در خانبا مجهت ررشنایی گذارند . نی - بعت
=========== leaf 593 | head: » بفتح اول و سکون ثانی » بممنی کوه باشد وآنرا جربی جبل خوانندا . پجاد - بفتح اول بر وزن هزار , بععنی پچ است که کوه باشد . پجول - بنم اود بروزن ترول » بمعتی کب گنتق : پجیو + بفتح اول و کر انی و سکون اضاد پمرماییدن مودم بلشه مکی . و.آنرا سالوسی و ربا خوانند . ٩‏
=========== leaf 594 | head: آیان ششم در بای فارسی باخای نقطه دار مشتمل بر بست و سه لفت م4 بفتح اول,سکون‌ئانی» بمعنی‌خوش دیگر - وبفتح اول بمعنی پهن و پخش باشد؟ا ویه باشد » وان بممنی په‌په وخوئ‌خونی | مثلآنکه چیزی در زیرپای آدمی‌با حیوان‌دبگر استد ]را بعربی‌بخ بخ‌خوانندوطوبی لكومرحبابكت |
```


## [2026-09-05T20:10:24.372Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'پدید' in p and 550<i<650:\n        print('leaf',i,'printed~',i-220)\nprint('---- leaf 561 full ----')\nprint(t[561][:3000])\nEOF",
 "description": "Find padid leaf and print bina page"
}
```


### [2026-09-05T20:10:26.008Z] TOOL RESULT

```
leaf 597 printed~ 377
---- leaf 561 full ----
۳:۱
ماه است که بعربی شه ر گوبندا .
که مردمرا در حالت ماشفه دیده میشوده وآنرا
مربی ممایثه کوش
دریجهٌ خانه را گوند .
بیناساك .. بسکون سینو کاف, بمعنی
بیناس باشد که دربحهٌ خانه است ۰ رب بای فارسی
هم‌آحده ۱ سست ه
بنایی بروزن‌زیبابی» بمعنی‌دیده‌وری
و بینند گی باشد - و گاه بینابی گویند و از آن
چشم اراده نماد که عین است
ین ب یکر اول و فتح ثانی و سکون
ی و هتند؟ باشد که از
هستی و بودن است
تی‌تماری ان از
زنان باشد .
بی نمکی کر دن - کنابه از بیوفایی
و بی‌عز گی- وبی وضع ی کردن باشد .
پیتنگ ه / با نون دیگربروزن‌زببنده,
بمسی شخص بینا و صاحب وفوف و عاقبت‌اندیش
باشد - و چشم را نیز کوند که بعربی عبن
خوانند ۵,
حیض آمدن
وقار باشد » چه شک به‌سنی عب و عار است. 8
مصد)
۵ - به بینندکان آفرشنده را
٩‏ رگ : ور
سوباردن
ی فیاد۱ - بسني غیرمحناج و توانگر
وبی احتیاج باشد . چه نیاز بمعنی احتیاجاست
الیو « بختح اول و نم ثانی وسکون واو
مجهول » بمه‌نی عروس_ باشد ۷ - و بکسر اول
و سکون انی مجهول و وا کرمکی باشد که
امه یشمین و کاغة را بخورد و ضایع کند۸ .
پیواد - با نانی مجهولبر وزن دیوار,
عدد ده هزار را هنشت و باین حمثی. محذف الف
پیواده » با تالی مجهول بر وزن
بیجاره ؛ بیکس و غریب وتنها -- وبی‌قدروهرتبه
وبی اعتبار را گویند - و چویکه بدان كلولة
خمیر انرا تنك سازند .
یو اد با نانی مجهول بروزن شیراز »
شیره باشد که آنرا مرغ عیسی گونشد و بعر بی
خفاش خوانند - و بمعنی اجابت و فبولهم آعده
است. و پاسخ وجوابرانیز کویند*۱» وباین معنی
بجای حرف الی لون هم‌بنظرآمده است»وبمعنی
اول بجای حرف اول بای فارسی هم آعده است
پیو بادیدن » بکس ارل و اك
مجهول بر وزن فرو باریدن, ناجاویده فرو ,بردترا
کون که بمربی بلم خوانند ؛ و بفتح انی حم
آمده است که بر وزن شکم خاربدن باشد واین
اصح است . چه در اصل این لفت باوبارسن
بوده است همزه را ببایدل کرده اند بیوباربدن
؟ از:یا. ۳ بی(حاصل
۴ ۳ آسم فاعل ازددن
۷ باین معنی « بيوك » هم آمدهءو در
۸ اظ م مصحف: _ (هم).
بتواچث رد جواب ۴ سحیح ی
سرخه 1 ۷50 ۳ شهمیرزادی از «ء ۰ ی اه جزء ۲ عموداً
ی مشاتی و دهان فرار دارد و قو شامه در جوف آنت .
```


## [2026-09-05T20:10:34.420Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[597][:3200])\nEOF",
 "description": "Print BQT padid page"
}
```


### [2026-09-05T20:10:36.325Z] TOOL RESULT

```
مت ۳۱۲
فد ۱۵ - بروزن‌فرسود؛ بمععنی‌سلامت
باشد - و بمعنی وداع فیزآمده است -
لف‌4۵ ت بر وژن صدمه » بمعنی حصه
وبهره وزله باشد - و هرچیز رانیز گوبند که در
لنگی ورومالی(۱) بسته باشتد ,
ید ند ر ۴ بر وزن سکندر, پدرسبییر۱
کویند که شوهر مادر است » و بر وزن نضنفر
و حق نظر عم آمده است .
بدو ار بروزن پرواز ۰ دوچوب بلند
باشد که هردو را از عم باندگ فاصله برزمین فرو
بر نده و چوب دیگر بمرض بربالای‌آنها بندند تا
کبوتران و گاهی جانوران شکاری برآن نشیتند
وآنرا بعربی میقعه خوانند۴ - و در موبدالفنلا
کردا کرد کلاء ودهان انسان و حبواتات دنگر
ببان
باشد از جالب بیرون - ومنقار مرغان: . .
پل « بفتح اول و ثانی, دام درختی‌است
که هرکز بار ومیوه ندهد و آنرا بعریی غرب
خوانند ۴ و منم اول چوپ پوسیده بائد که
آراآتشگره سازند. و بمر بی‌حراقه گوید ۹
و باینیمنی فتح اول هم آمده‌است. *
بمعثی ظهور باشد که از ظاهر شدن و نمابان
کردبدن امت- وبمعنی موجود هم هست‌چنانکه
کوبند + پدیدار آمد» یعنی موجود شد.
پد سار باسینبی‌نقطه بروزن پدیدار,
برسرکاری دفئن باشدکه پیش ازین شروع درآن
کرده باشند و
پر قت « یکر اول و سکون شانی
و رای بیطةٌ مضموم بفا و فوفالی زده » ماضی
(۱) چش : رومال .
پذرفئن باشد بعنی قبول کرد و معترف شد » چه
۱ - پهلوی 04ت +08 «نولدکه . کارنامه »٩۵‏ (قس : درود) «اسشق ۲۸۸ : «( علی
فریب) بامن (بوصر مشکان) خالی کرد و گفت : بدرءدیادای دوست نك که بروز کار دراز بیکجا
بودمييم و ازنکدیگر آزار ندارم .» «بیهقی ۵۳*. ؟ ‏ مخقف پدراندر. ۳ - از
شواهدی که بدواز درآ نها آحدهه چنن مستفاد میشود که آن جای عرغعان شکاری وشاید شنک
دد ان درمحلی مرتفع باکوهی باشد. « لفت نامه » وركث: پتواز.
فهناه:طاوناه وباآنام0ظ «ناتی۱۹۱۹* :
این نج درختند که مي‌نارد بار بید ویده وسرو وسفیدار وچنار.«لفت نامه».
۵ عطات باذ چوباران دل موافق خوید اهب آش و جان مخالفان پده باد .
شهید بلخی. «لفت امه» ورك: بد.
۱ - از: پدید ار (پسوند). ۲ - رك:پذیرفتن.
» بدید -بفتح اول. بهلوی 4 0۵ د«یرند که .کرنامه 44۰ ؛ فر اوستانااه 00۳02
«اسشق ۲۷۸۹ , نبرک پهلوی آنرا 16 084 نوشنه. «یب رکه 0۷»؛ آشکار. سامان,
```


## [2026-09-05T20:10:56.407Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins dheia\"; grep -n \"dheiə\\|dheia\\|dhei-\\|dheye\" AHD_watkins1985.txt | head -10; echo; grep -n \"semantic\\|sema\" AHD_watkins1985.txt | head -10; echo \"=== KLN sema\"; grep -n \"semantics\\|sematic\\|Gk. sema\\|sēma\" KLN_1966.txt KLN_1971.txt | head -15",
 "description": "Grep AHD and Klein"
}
```


### [2026-09-05T20:10:56.485Z] TOOL RESULT

```
=== AHD watkins dheia
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended

95:root ker-', “horn,” plus the noun suffix -wo-, plus the nominative singular ending -s. The root contained the basic semantic kernel, the underlying notion, which the suffix could modify in various ways. It was primarily the suffix that determined the part of speech of the word. Thus a single root like prek-, “to ask,” could, depending on the suffix, form a verb *“prk-sko-, “to ask” (Latin poscere), a noun *prek-, “prayer” (Latin precés), and an adjective *prok-o-, “asking’’ (underlying Latin procus, “suitor’). Note that *prek-, *prok-, and “prk- have, respectively, e-, o-, and zero grade.
105:A word of caution should be entered about the semantics of the roots. It is perhaps more hazardous to attempt to reconstruct meaning than to reconstruct linguistic form, and the meaning of a root can only be extrapolated from the meanings of its descendants. Often these diverge sharply from one another, and the scholar is reduced in practice to inferring only what seems a reasonable, or even merely possible, semantic common denominator. The result is that reconstructed words and particulary roots are often assigned hazy, vague, or unspecific meanings. This is doubt- less quite illusory; no human society from Proto-Indo-European times to the present day would be viable if conversation were limited to vague generalities. The apparent haziness in meaning of a given Indo- European root often simply reflects the fact that with the passage of several millennia the different words in divergent languages de- rived from this root have undergone semantic changes that are no longer recoverable in detail.
118:Reconstructions are by no means confined to general, imprecise meanings such as these; we have also such specific semantic values as nes-', “to return safely home“ (NOSTALGIA).
123:A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, Latin bonus, and Greek aga- thos have nothing to do with each other, and each is confined to its own branch of the family.
140:firm, solid,” and from it is derived not only the family of English TREE but also that of English TRUE. Note that the semantic evolu- tion has here been from the general to the particular, from “solid” to “tree” (and even “oak” in some dialects), and not the other way around.
208:The text of each entry describes in detail the development of Modern English words from the root. In some cases no semantic or morphological development needs to be ex- plained, and the lemma (the historically at- tested representative of the root) is immediately given:
276:aks-. Axis. 1. Suffixed form *aks-lo- in Old Norse éxull, axle: AXLE. 2. Suffixed form *aks-i- in: a. Latin axis, axle, pivot: axis; b. Latin diminutive axilla, armpit (< “axis point of the arm and shoulder”): AXILLA. 3. Suf- fixed form *aks-ld- in Latin dla (< *axla), wing, upper arm (see axilla in 2. b. for semantic transition): AISLE, ALA, ALAR, ALARY, ALATE, ALULA; ALIFORM. 4, Suffixed form *aks-on- in Greek ax6n, axis: AKON; MONAXON. [In Pok. ag- 4.]
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
369:*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (obtained from the pine tree): TAR}. 7. Suffixed variant form *dri-ro- in Latin diirus, hard (of whose English derivatives many represent a semantic cross with Latin dirdre, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; (DURA MA- TER), ENDURE, INDURATE, OBDURATE. 8. Lengthened zero-grade form *dré- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD. 9. Reduplicated form *der-drew-, dissimilated with suffix in *den-drew- on in Greek dendron, tree: DENDRO-, DENDRON; PHILO- DENDRON, RHODODENDRON. 10. Celtic compound *dru-wid-, “knower of trees” (*wid-, to know; see weid-), the Celtic priestly caste, associated with a tree-cult, probable source of Latin druides, druids: DRUID. 11. O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]
370:deu-'. To lack, be wanting. 1. Possibly suffixed form *deu-s- in: a. Germanic *teuzdn in Old English téorian, tyrian, to fail, tire (< “to fall behind”): TIRE}; b. Greek dein, to lack, want: DEONTOLOGY. 2. Suffixed form *deu-tero- in Greek deuteros, “missing,” next, second: DEUTERO-; DEUTERAGONIST, (DEUTERIUM), DEUTERON- omy. (For suffixed zero-grade form *du-s-, combining form of *dew-es-, a lack, see dus-.) [Pok. 3. deu- 219.] deu-2. To do, perform, show favor, revere. 1. Suffixed form *dw-enos in Latin bonus (> Old French bon, femi- nine bonne), good (< “useful, efficient, working”): Bo- NANZA, BONBON, BONITO, BONNE, BONUS, BOON?, BOUNTY; BONHOMIE, DEBONAIR. 2. Adverbial form *dw-ené in Latin bene, well: BENEFACTION, (BENEFAC- TOR), BENEFIC, (BENEFICENCE), BENEFIT, BENEVOLENT, BENIGN, (HERB BENNET). 3. Diminutive *dw-ene-lo- in Latin bellus (> Italian bello, feminine bella), handsome, pretty, fine: BEAU, BEAUTY, BELLE; BELDAM, BELLA- DONNA, BELVEDERE, EMBELLISH. 4. Possibly suffixed zero-grade form *dw-eye- in Latin bedre, to make blessed: BEATITUDE; BEATIFIC, BEATIFY. 5. Possible (but unlikely for formal and semantic reasons) suffixed zero-grade form *du-na- in Greek dunasthai, to be able: DYNAMIC, DYNAMITE, DYNAST, (DYNASTY); AERODYNE. [Pok. 2. deu- 218.]
=== KLN sema
KLN_1971.txt:42648:center and semantics. 
KLN_1971.txt:70018:‘sign 7 . See semantics. 
KLN_1971.txt:72962:(see di-, ‘two’), and oTjfxa, ‘sign’. See semantics 
KLN_1971.txt:217402:<pd)V7){xa, ‘sound’. See semantics and cp. hy- 
KLN_1971.txt:217405:taining to semantics. — Gk. a^avTwcos, ‘signi- 
KLN_1971.txt:217408:'semantics, n., the science of the meanings of 
KLN_1971.txt:217428:semasiology, n., semantics. — G. Semasiologie, 
KLN_1971.txt:217437:topic)’. See semantics and -logy, 
KLN_1971.txt:217438:sematic, adj., serving as a sign or warning. — 
KLN_1971.txt:217440:ovjpLaTo?, ‘sign’. See semantics, 
KLN_1971.txt:217460:avjp.a, ‘sign’. See semantics, 
KLN_1971.txt:242831:cri}fia, ‘sign’. See semantics, 
KLN_1971.txt:244942:See semantics. 
KLN_1971.txt:253653:and crij^a ‘sign’. See semantics, 
KLN_1966.txt:6982:Centrosema,  n.,  name  of  a  genus  of  the  family Fabaceae  (bot.)  —  ModL.,  compounded  of  Gk. x£vxpov,  ‘spur’,  and  rr/jti.a,  ‘sign,  standard  .  See center  and  semantics.
```


## [2026-09-05T20:10:57.681Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ din\"; grep -n -i \"^\\s*din\\b\\|dīn\\|Din \" FVQ_pages.txt | head -20; echo \"=== FVQ sima\"; grep -n -i \"sima\\|sīmā\" FVQ_pages.txt | head -20",
 "description": "Grep Jeffery for din and sima"
}
```


### [2026-09-05T20:10:57.739Z] TOOL RESULT

```
=== FVQ din
2175:and Phon. DIN for man in general, though the use of O I ^i in
2925:Syr. or Aram. The Heb. DIN (cf. Phon. PX), from a verb !TIK, to
2952:and thus approaches even more closely than DIN the Qur'anic use of
11000:DIN 5(f
=== FVQ sima
```


## [2026-09-05T20:11:09.032Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor leaf in (148,149,150):\n    print('=========== leaf',leaf,'(printed ~',leaf-17,')')\n    print(t[leaf][:2600])\nEOF",
 "description": "Print Jeffery din entry"
}
```


### [2026-09-05T20:11:10.982Z] TOOL RESULT

```
leaves 335
=========== leaf 148 (printed ~ 131 )
FOREIGN VOCABULARY OF THE QUR 5 AN 131
, ^r
They are not very happy over the form, however, for ,*- 1) is fern.
and we should expect 451^0 not v5u^ Exactly the same form, how-
ever, is found in a verse of Khidash b. Zuhair
D ^ ^ .**
IsUo Lfc 4J li^rLs I'lji j*.^ ^U 1C!
" There came to us 'Amir desiring entertainment from us, so we
filled for him a full cup."
so Sibawaih suggested that it should be taken not as an adj. to u-uD
but as a verbal noun. 1
There is ground, however, for thinking that the word is not Arabic
at all. 2 Fraenkel, Fremdw, 282, would relate it to plTl, which we
find in Heb. pHR to crowd, oppress, thrust ; Aram. pPPT ; Syr. %!>
to crowd, squeeze, which is the Ar. T*pO to drive away, expel. The
change of PI to H he would explain as Mesopotamia!!. Thus
would mean " a cup pressed out", referring to the wine pressed to
fill the cup.
Of very frequent occurrence. Of. i, 3 ; ii, 257, etc.
Judgment, Religion, and in ix, 29, verbally " to make profession
of faith ".
fj- ^
In the Qur'an we find also o a debt, that which one owes
*> ^
(cf. iv, 12, 13 ; ii, 282), and i JL for one who receives payment of a
X 1
debt (xxxvii, 51 ; Ivi, 85), besides the verb ^ ]JS " to become debtors
to one another " (ii, 282). These, however, are later developments of
the word within Arabic.
The Muslim authorities usually treat it as an Arabic word (cf.
1 Vide LA, xi, 395, 396.
2 Horovitz, Parodies, 11, says : '* Auch die Herkunft von jUj . . ist unsicher."
=========== leaf 149 (printed ~ 132 )
132 FOREIGN VOCABULARY OP THE QUR^AN
Raghib, Mufradat, 175), and derive it from jlS " to do a thing as a
habit", but this verb seems to be denominative from <jO in the
sense of obedience, which, like Al^Ju and jlS (i.e. lAl^jSo and
|uj), is a borrowing from the North, connected with Akk. danu,
Heb. fH ; Syr. tO>. There was a suspicion among the philologers,
however, that it was a foreign word, for LA, xvii, 27, notes tttat some
authorities admitted that it had no verbal root, and al-Khafaji, 90, and
ath-Tha'alibi, Fiqh, 317, include it in their lists of foreign words.
As a matter of fact we have here two separate words of different
origin. 1 (i) In the sense of religion the word is a borrowing from Iranian.
In Phlv. we find jjy den meaning religion? from which come ^xyfo
dendk for religious law, ))0j" ^w-*^ of the same religion, 3 and
)W)0 dendn, used in the sense of "the religious 1 ', i.e. true
believers. This Phlv. j)O is derived from Av. *i)uj^ daena,
religion 4 (though this itself is probably derived from the Elamitish
den)* and besides being the origin of the Mod. Pers. JO, 6 was
borrowed into Arm. as ^te meaning religion, faith (and also law 7
in the sense of a "religious system", e.g. ijJA 1/^/^1% =
u)wo-u. >))($ the Mazdian religion or Law), (ii) In the sense of
Judgment it is a borrowing from the Aramaic. Thus we find in common
use the Rabbinic WH, Syr. U*?> and Mand. WH, all meaning
judgment and, indeed, the judgment of the last day. 8
From the Aramaic the word passed into S. Arabian lrfp| and
1 Noldeke in ZDMG, xxxvii, 534. See also Von Kremer, Mreifsilge, p. vii, and
Ahrens, Christliches, 28, 34.
2 PPGl, 110 ; 8&ya* 9 Glossary, 160, and the den of the Turfan Pahlavi ; Sale-
mann, Manichaische, Mudien, i, 67. For the borrowing (f. Noldeke-Schwally, i, 20 ;
Vollers, ZDMG, 1, 641 ; Noldeke, Mand. Gram, 102.
a Cf. the Av. Al)H)AlA G-^W' Weat ' Gl 8sar y> 35 '
Bartholomae, AI W, 662; Horn, Grundrixs, 133; cf. also the Pazend edlni
= irreligion.
* But see Bartholomac, AIW, 665, and Ziramern, Akkad. Fretndw, 24, who derives
it from Akk. de(i)nu. . .
Addai Sher, 69, discusses its meaning. Curiously enough it is given by the
Lexicons as a borrowing from Arabic, cf. Vullers, Lex, i, 956, but see Bartholomae,
AIW, 665.
7 Hubschmann, Arm. Gramm, i, 139.
Montgomery, Aramaic. Incantation Texts from Nippur, Glossary, p. 285,
8
=========== leaf 150 (printed ~ 133 )
FOREIGN VOCABULARY OF THE QUR'AN 133
Eth. T with its verbal forms Rf V and f-ftfV (and Amharic
judge ; Tigrina &*! judfl c ) \ into Iranian, where we find the
Phlv. ideogram njy dena judgment, decree, 1 and also into Arabic. 2
As used in the Qur'an it closely corresponds to Jewish use ; in fact
the constantly occurring ^jj^\ *$ so exactly corresponds with the
Rabbinte WH OF = THH DV that on the surface it seems obviously
a borrowing from Jewish sources. The fact, however, that in Syriac,
besides IL*; meaning judgment, we have also a ^J meaning
religion, borrowed from the Iranian (Brockelmann, Lexicon Syriacwn,
1516), giving us the same double usage as in Arabic, makes the
probabilities seem in favour of the borrowing having been from a
Christian source. 3 In any case it was an early borrowing for it is found
not uncommonly in the early poetry. 4
jLlo (Dinar).
iii, 68.
A dinar.
The name of a coin, the Lat. denarius, Gk. 8r)vdpiov. The Muslim
authorities knew that it was a loan-word and claim that it came from
Persian, though they were not unanimous about it. al-Jawaliql, Mu'arrab,
62, whose authority is accepted by as-Suyut!, 5 gives it as Arabicizcd
lU
from the Pors. Lo, but ath-Tha'alibl, Fiqh, 317, places it among the
' x-
words which have the same form in both Arabic and Persian. as-Suyuti,
Muzhir, i, 139, places it among the words about which the philologers
were in doubt, and Raghib, Mufntddt, 171 , while quoting the theory that
it is of Pers. origin compounded from JO and jl, 6 yet gives his
n
own opinion that it is from jl_O and an Arabic word. Similarly the
1 Frahany, Glossary, p. 79.
2 Hirschfeld, Beitratje, 44 ; Koldeke, Xcue Beitrdge, 39 ; Fracnkel, Vocal), 22.
3 Mingana, Synac. Influence, 85; Ilorovitz, AT, 62.
4 Sec references in Horovitz, op. eit. Cheikho, $a*raniya> 171.
5 Itq, 320 ; Mutaw, 46, vide also al-Khafaji, 86.
6 Vide Vullers, Lex, i, 25 and 56. Dvorak, Fremdw, 66, points out that the late
Greek explanations of the word take it to be from din-ar, i.e. 8eKaxaA/coi> ; of. Steph.,
Thesaurus, ii, 1094 : TO 8eKaxaA*ov ovrcus Ka\ciro Srympiov, or the even more
ridiculous TO ra Seiva dipeiv nape
```


## [2026-09-05T20:11:22.747Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sima\\|slma\\|sTma\\|simiya\\|Sima\" FVQ.txt | head -20; echo \"=== try search of greek sema in FVQ\"; grep -n \"arjfjia\\|sema\\|orj/xa\" FVQ.txt | head",
 "description": "Grep FVQ for sima"
}
```


### [2026-09-05T20:11:22.807Z] TOOL RESULT

```
=== try search of greek sema in FVQ
1665:In Assemani, Bibl. Or., i, 359 ff. * " 7 Ed. Chabot, ii, 183 ff. 
1829:p. 191). Assemani, liibl. Or., iii, 2, 606, mentions Monophysite Bishops of al-Hira.
```


## [2026-09-05T20:11:24.607Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%85%D8%A7",
 "prompt": "Give the Arabic entry for سيما (sīmā) 'mark, sign': its etymology (is it from Greek σῆμα or from a Semitic root w-s-m?), meanings, and any Persian entry سیما."
}
```


### [2026-09-05T20:11:30.444Z] TOOL RESULT

```
# سيما Entry Analysis

Based on the Wiktionary content provided, here's what's available:

**Entry Definition:**
The page shows "سِيمَا" (sīmā) as "alternative form of سِيمَى (sīmā)" without providing the specific meaning you're asking about. The content doesn't include the definition relating to 'mark' or 'sign.'

**Etymology:**
No etymological information is present in the provided excerpt—neither Greek origin (σῆμα) nor Semitic root (w-s-m) is mentioned or discussed.

**Persian Entry:**
The page does not contain any Persian language entry for سیما. The interface indicates "3 languages" with links to Arabic, Hungarian, and Turkish Wiktionary versions, but no Persian variant is shown in this excerpt.

**Note:**
To find the etymological information and complete definitions you're seeking, you would need to consult the full Arabic Wiktionary entry or a more comprehensive Arabic lexical resource, as this English Wiktionary page provides minimal detail beyond grammatical declension tables.
```


## [2026-09-05T20:11:33.824Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%85%D9%89",
 "prompt": "Give the Arabic entry for سِيمَى (sīmā): etymology (root, any Greek σῆμα connection or derivation from و س م w-s-m), meaning, and any related terms."
}
```


## [2026-09-05T20:11:35.426Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD wyn\"; grep -n \"wyn\\b\" SOD.txt | head -10; echo \"=== SOD dyn\"; grep -n \"^dyn\\|dyn'\\|dynh\\|dynd\" SOD.txt | head -15",
 "description": "Grep Gharib Sogdian"
}
```


### [2026-09-05T20:11:35.495Z] TOOL RESULT

```
=== SOD wyn
4320:}nkwyn  (Kcai-yUan),  in  the  year  of  the  dragon,  it  was 
5975:cstw}n-  (poor)  <  B  6stw}n-  and  C  dystwyn-. 
18960:1722  >swswyn't(t)   S 
19723:=^wy(hy,  Jwyn,  wysn,  ZKw,  }ww,  w-,  ww 
27158:frwyn-   ©impf.  fi}ywn   =>Pywn-,  P'ywn- 
34506:4076  y}w  rwyn   B,  M  jf "  j3J 
34507:yaw-royn  =»rwyn 
34540:4081  Y'y  'nkwyn   B         (Jt&  ^<JUU  j/)^  j>!^l  (rb) 
36351:4347  ywpnw  wyn-   B  o±*->lj>- 
37397:4496  Ywyn-  B  jj-t-oy^  iojJu*j±\y*-  ijjii«juiU 
=== SOD dyn
4158:dynasty  (225  A.D.),  the  history  of  Sogdiana  is  again 
32374:^dynd^y* 
32384:3774  dynd'ry1  C  ^jIj^j  <tf.y.f  ^  ta,  <LJS"  <*^jUjj 
32428:Sendarya   ^dynd'ry* 
89044:dynasty    4062 
109781:(dynd'r, 
109799:dynd»r  C
```


### [2026-09-05T20:11:36.574Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:11:43.867Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor leaf in (214,487):\n    print('=========== leaf',leaf,'(printed ~',leaf-66,')')\n    print(t[leaf][:1500])\nEOF",
 "description": "Print Gharib pages 148 and 421"
}
```


### [2026-09-05T20:11:45.644Z] TOOL RESULT

```
leaves 645
=========== leaf 214 (printed ~ 148 )
                                                                                        MM             un


 149
                                                                                                                      Synyfrn
                                                                   order of electi
        GMS 1043; pi. Syn'fir'st, Syn'fir'st
                                                                   BBB 554 a4; W-Lii
 3759 Syn'pr'nyg M         (^^*<*J)+j£t><iSj>£±>
      SenaParanig                                             3772 5yn5"r     B, M, S   jj)^ $ <6jo jf ^ < jLlj j ^Ij ^>
      DenavarCa Manichean seet)
      BBB bl                                                       5en5ar     (8yn8}r, dnd>r) ©pi. -f; ob. pi. -ty
 3760 Syn'pr'st M, S                      ^U ^jf ^ jU j
                                                                   religious,
                                                                     ^dynd^y*priest, monk, electus
      SenaParast ©pi. -^Syn'Pr'nc
                                                                   GMS 1135-6; TSP 2.823, 7.41; VJ 22, 121; BBB
      electae
                                                                     f 30, 32, 623; STii 3.1, 5, 43, 58, 6.2; Sund.
       GMS 260; 6ym*fir>su Frag. Len. 45.4                           AoFviii 1981 p214, 8R4; KG 351; C2 gloss.
 3761 5ynJk B                                          ^
      6ene ©pi. ->y/ =*8yn>y                          
=========== leaf 487 (printed ~ 421 )
                                                                                                                     420



wydb'y
                                                                   image
           734, 945, 5.69; SCE 193; BSTBL, Vim. 96, 185;
           Dhu. 69, 288; STii 5.4; Frag. Len. 38.6, 67.4,          BSTBL, Dhy. 64, 179; Benv. Notesiv 507
           KG 396, 516, 557, 590; MSP b43, 63; Hen.         10361 wy8rfs}n M                     OUKp < jljj>
           AION 1965, 32 n
                                                                  wiSrafsan ©*wySrfs-> P&nhrfrafs- ©pres.
                                                                  shining
10347 wydb'y      C -> wySp>y
10348 wySp'ycy B, S                      ^j^^                     GMS 1033
      wiSpayci ®<*wy6J3}7c\ Parth. wydby*g
                                                                      part,
                                                            10362 wydsntnyq    C                 ^j t^Li dxj*
      eloquent
      SCE 503, 535; BSTBL; Vim. 2; GMS 1006; ob.                  wiSesandnik ? ©*wi-dais-anta-, anta
          pi. wySpYctyi BBB 734, KG 411; wySpYsty,                conspicuous, exposed to view
          apud. Sund. KG pl91                                     BSTii 905.25;C2, 57V25 n pl23; Schwartz. AI 5,
                                                                    211.25
10349 wyfip'ys- B, S               oA*~* '^A
      wi8Paxs (wySPxs, wy8pys-) ©Khwa
```


## [2026-09-05T20:11:58.586Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 480<=i<=500 and re.search(r'\\bwyn', p):\n        idx=[m.start() for m in re.finditer(r'wyn',p)]\n        print('leaf',i,'printed~',i-66)\n        for j in idx[:6]:\n            print('   ...',p[max(0,j-120):j+200].replace('\\n',' '))\nEOF",
 "description": "Find Sogdian wyn to see"
}
```


### [2026-09-05T20:13:08.406Z] TOOL RESULT

```
leaf 486 printed~ 420
   ... , 132, 10332 wyd'r- C                                                       162, 214, 225       wiSar ©perf. ^wytwS'r-, wyn-, wyt-                             =4wy8y                                                      tJJLO   10343 wyS'y- B                     OxS^^U- <oJ£JUJbb       (fo)see       C2,64R24, 104R13, 57
leaf 488 printed~ 422
   ... oice                                                                 MSP b 151; GMS 213 n 1                             wyn-       wex, wix ©loc. -y-> pi. -f =4wyx       root                                                10385 wyjt- =* wjt-        VJ 954r 137a, TSP 2.165, 1021; BSTBL, Dhu. 75,     10386 wyjtk}ry(yh) M
   ... s (wyyrys-) ©impf. =^wyr}ys-       (to)wake, (ro)arouse                                                           10393 wyn B, C                       ^*tjj ^^     « J-^* <JLi->        C2, 83Ria, wyYr'ys, TSP 1325 n p228; S W, IIJ            wen ©ob. -y          1976, p55.25, 56 n p                                     
   ... -               1020, 16.32; BSTBL pl42; C2, 61V23, 25;       wiyas ©impf. =»wys-*, wyyws-                              wynyy VJ 364; Dhu. 97       OcOrejoice                                          10394 wyn-                            (u>> j^~> jj)bJ**       VJ 27b, 1458; C2, 86V2                                    
   ... yws-                              wynyy VJ 364; Dhu. 97       OcOrejoice                                          10394 wyn-                            (u>> j^~> jj)bJ**       VJ 27b, 1458; C2, 86V2                                    wen     ©<*waina-, A v. vaena ©inf. -(>)y =»wyt- 10383 wyys-2 C                       
leaf 489 printed~ 423
   ...                                                                                                                  422    wyn*            pill; Sund. AoFviii 1981 p219                           BSTii 832.2, 905.10.14, 915.7; C2, 39V7, 57V10,                                                                      14, 104R2, 
   ... 915.7; C2, 39V7, 57V10,                                                                      14, 104R2, 48R15, 18 10395 wyn> M, C                          (g^ijtiJ^       wina, wina(k) (wyn'kCh)) ©Khot. bina ©f. n.           10406 wyn}ndyy M                     ^yT<^U-«jUj#       harp, lute                             
   ...                            14, 104R2, 48R15, 18 10395 wyn> M, C                          (g^ijtiJ^       wina, wina(k) (wyn'kCh)) ©Khot. bina ©f. n.           10406 wyn}ndyy M                     ^yT<^U-«jUj#       harp, lute                                                  wenande (wyn>ntk, wyn>nty) ©pres. part,      
   ... 18 10395 wyn> M, C                          (g^ijtiJ^       wina, wina(k) (wyn'kCh)) ©Khot. bina ©f. n.           10406 wyn}ndyy M                     ^yT<^U-«jUj#       harp, lute                                                  wenande (wyn>ntk, wyn>nty) ©pres. part,       GMS 971, lllln 1; Hen. Tales. 467, 11, 13, 1
   ...  wyn}ndyy M                     ^yT<^U-«jUj#       harp, lute                                                  wenande (wyn>ntk, wyn>nty) ©pres. part,       GMS 971, lllln 1; Hen. Tales. 467, 11, 13, 18,              visible, present, actual         30, 33 41; C2, 60V21: BSTii 890.53; Benv. Eti             GMS 1068; TS
   ...  M                     ^yT<^U-«jUj#       harp, lute                                                  wenande (wyn>ntk, wyn>nty) ©pres. part,       GMS 971, lllln 1; Hen. Tales. 467, 11, 13, 18,              visible, present, actual         30, 33 41; C2, 60V21: BSTii 890.53; Benv. Eti             GMS 1068; TSP 2.204, 
leaf 494 printed~ 428
   ...                                                                 wituxs =4wyt*yc-, wyt'xs-, wytwyt-       wit ©pt. st. =»wyn-, wyd'r-, wytw8>r-                       0<9)melt away, (ra)disappear       (to)scc                                                                   TSP 2.106a, BTSBL, Dhy. 157; BBB 62.516,
```


## [2026-09-05T20:13:17.703Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['FFD'],ensure_ascii=False,indent=1)[:1500])\"",
 "description": "FFD metadata"
}
```


### [2026-09-05T20:13:19.555Z] TOOL RESULT

```
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
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Se
```


## [2026-09-05T20:13:23.502Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nt=open('FFD_pages_faseng.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# printed = pdf - 5 ; leaf N = pdf N+1 -> printed = leaf + 1 - 5 = leaf - 4\nfor pr in (33,55):\n    leaf=pr+4\n    print('=========== printed',pr,'leaf',leaf)\n    print(t[leaf][:1800])\nEOF",
 "description": "Print FFD pages 33 and 55"
}
```


### [2026-09-05T20:13:25.253Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-05T20:13:28.865Z] TOOL CALL #53: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/; cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor pr in (33,55):\n    leaf=pr+4\n    print('=========== printed',pr,'leaf',leaf)\n    print(t[leaf][:1600])\nEOF",
 "description": "List FFD dir and print pages"
}
```


### [2026-09-05T20:13:30.623Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
leaves 115
=========== printed 33 leaf 37
[pdf page 38]
ماده‌های ماضی و مضارع فارسی دری ا ‏ ۳۳
مضارع ساخته شده است.
اندیش + فارسی میانه 127۵88 + ایرانی باستان ۸۵۳-4219-8*. برای 2 -> آرای. 240
پیشوند فعلی است. ريشةٌ 489 به معنی «نشان‌دادن» است.
انگاردن. انگاشتن
انگارد < فارسی میانه 1478374 < ایرانی باستان ۴1۵۳-37-12. برای 18 -> آراست.
0 پیشوند فعلی است.
7۳ صورت بالاندةٌ ریشهٌ 127 است. ريشهٌ 127 به معنی «فکر کردن» است. «انگاشت»
صورت , ر ر به معتی
به قیاس با 13۶ و 1331 به وجود آمده است.
انگار < فارسی میانه 127837 < ایرانی باستان ۳۸۵0-37-8 برای 2 -> آرای.
نگاردن هم از ریشهٌ ۵۲ به معنی «فکر کردن» آمده است. > نگاردن.
انگ کم
انگیخت + فارسی میانه 12888 + ایرانی باستان ۸۵۳-۴۵۵۳1۵*. برای 1۵ >
آراست. 1800 پیشوند فعلی است. ان صورت اصلی 8۳ است» 1 پیش از 1 به # بدل
شده است. ريشةٌ 8۷« ریشه‌ای است فرضی و معنی فرضی آن هم می‌تواند
«حرکت‌کردن» باشد.
انگیز ج فارسی میانه 128857 < ایرانی باستان ۵-:-82۵*. برای 8 - آرای. ‏
به‌جای ۴ آمده است.
اوباردنء اوباشتن
اوپارد + فارسی میانه 60370 < ایرانی باستان 3۷۵-037-12*. برای 1۵ -> آراست. 48
پیشوند فعلی است. 037 صورت بالاندهٌ ريشهٌ 087 است. 087 به معنی «پر کردنْ» است.
انباردن هم از ريشهٌ 0۵7 به معنی «پر کردن» آمده است > انباردن. «اوباشت» به قیاس با
7 و 331 به وجود آمده است.
اوبار < فارسی میانه 6037 < ایرانی باستان ۴*۵۷/۵-037-8. برای ۵ -> آرای.

=========== printed 55 leaf 59
[pdf page 60]
ماده‌های ماضی و مضارع فارسی دری نا ۵۵
بین < فارسی میانه ۷۷68 + ایرانی باستان ۹/۵۱-3* 23 نشانه‌ای بوده که برای ساختن
مادهٌ مضارع از ريشه به کار می‌رفته است. ريشةٌ ۷۵ به معنی «دیدن» است.
«دیدن» و «بین» چون «آمدن) و «آی» دو ریشه‌ای است.
رامیدن
۰ آرامیدن
راندن
راندن مخفف «روانیدن» است و آن فعل واداری از «رفتن» است. در فارسی دری
فعل واداری از مادةٌ مضارع + «ان» و «(عن» ساخته می‌شود. «۵۶) در متون کهن آمده
مادهٌ ماضی فعل واداری هميشه جعلی است و به جای «انید» ممکن است («اند» به
کار رود.
ربودن
ربود + فارسی میانه 1010.
ربای + فارسی میانه 1003 +« ایرانی باستان ۵رقم۳*, 2رقم" از ۳803: اسم
به‌معنی «ربودن» و 8نشانه‌ای که برای ساختن مادةٌ جعلی از اسم به کار می‌رفته» ساخته
شده است.
مادهٌ ماضی باید «رّفت» < فارسی میانه ۳۵۶۲ < آیرانی باستان ۵۵ می آمد. به قیاس
با 573 و 5736 «ربود» آمده است.
3 از ریشةٌ 780 به معنی «ربودن» و پسوند 3 ساخته شده است.
رّستن
رّست + فارسی میانه 7291 < فارسی باستان ۴۶۵۶-1۵ برای 1۵ -> آراست. 724
صورت اصلی 78 است» ‎٩‏ پیش از 1به 9بدل شده است.
```


## [2026-09-05T20:13:50.370Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD dheia\"; grep -n \"dhiā-\\|dhiä-\\|,sehen, schauen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== POK deik 188\"; grep -n \"deiK-\\|deik̂-\\|,zeigen'\" POK_01.txt | head -10; echo \"=== SNS ewen\"; grep -n -i \"ewén\\|éwén\\|ëwën\\|wēnāg\\|venak\\|aivenak\" SNS.txt | head -10",
 "description": "Grep WLD, POK deik, SNS"
}
```


### [2026-09-05T20:13:50.456Z] TOOL RESULT

```
=== WLD dheia
=== POK deik 188
2716:deik-  ,zeigen',  woraus  lat.  und  germ.  z.  T.  ,mit  Worten  auf  etwas  hinweise] sagen',  mehrfach  auch  ,das  Recht  weisen,  auf  den  Täter  hinweisej beschuldigen'  entwickelt;  Partiz.  Pass.  dik-tö-s;  dikä  ,Richtunj dik'ti-  ,  An  Weisung',  deiko-s  ,Richtung'.
2720:got.  gateihan  ,anzeigen,  verkündigen',  anord.  tea,  jünger  tia  ,zeigen, darstellen,  ankündigen',  ags.  teon  ,anzeigen,  verkündigen',  ahd.  zlhan  ,an- schuldigen,  zeihen^,  wozu  anord.  tigenn  ,(*monstratus)  vornehm',  t'ign  f. ,Rang;  vornehmer  Mann';  ahd.  zeigön  ,zeigen',  wovon  zeiga  ,Weisung'; inziht  usw.  s.  oben;  ferner  anord.  teigr  m.  ,geradliniges  Wiesenstück' (,*Richtung'  =  ai.  desd-h  ,Gegend,  Platz,  Land'),  ablautend  ags.  tig,  tili , Anger,  Weide',  mnd.  tl{g)  m.  öffentlicher  Sammelplatz  eines  Dorfes', ahd.  zieh  , forum'.
2736:air.  deck  ,der  beste'  (=  lat.  decus);  auch  in  PN  Ecliuid  (^ekvo-de%-^ Gen.  Echdach,  Lnguid,  Gen.  Luigdech  (urir.  Lugu-deccas  mit  cc  =  k),  falls nicht  e  für  älteres  i  steht;  dann  zu  deik-  ,zeigen',  in  der  Bed.  ,befehlei
=== SNS ewen
```


## [2026-09-05T20:13:56.507Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2714,2720p' POK_01.txt | cut -c1-1200; echo \"=== WLD try\"; grep -n \"dheiə\\|dhei9\\|dhiā\\|dhya-mn\\|dhyäman\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head; echo \"--- alt\"; grep -n \"sehen, schauen\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head",
 "description": "POK deik and WLD search"
}
```


### [2026-09-05T20:13:56.594Z] TOOL RESULT

```
Ein  Zusammenhang  mit  dheig-  ,stechen'  ist  nicht  nachweisbar.
WP.  I  777.
deik-  ,zeigen',  woraus  lat.  und  germ.  z.  T.  ,mit  Worten  auf  etwas  hinweise] sagen',  mehrfach  auch  ,das  Recht  weisen,  auf  den  Täter  hinweisej beschuldigen'  entwickelt;  Partiz.  Pass.  dik-tö-s;  dikä  ,Richtunj dik'ti-  ,  An  Weisung',  deiko-s  ,Richtung'.
Ai.  didestij   disdti,   deiayati  , zeigt,   weist',   av.  daes-  Aor.  döU-  ;Zeig^ {daesayeiti,    disyeiti,    daedöiU)    ,zeigen ;    jemandem    etwas    zuweisen, sprechen',  Partiz.  ai.  distd-  (=  lat.  dictus) ;  dlsti-h  ,Weisung,  Vorschrift av.   ädiHi-§  , Anweisung,   Lehre'   (=  lat.  dicti-ö,  ags.  tiht  , Anklage',  ahc in-,  bi'Ziht  ds.,  nhd.  Verzicht),  ai.  dis-  f.  , Weisung,  Richtung',  diSä  .Richtum (=r  SUt]  ,Recht',  woraus  wohl  lat.  dicis  causa  ,nur  der  Form  wegen,  zuiä Schein'),  desd-h  ,(Richtung),  Gegend'  =  an.  teigr  s.  unten;
gr.  dsUvv[.iL,  sekundär  öeL-Kvvo)  ,zeige',  kret.  TtQO-öUvVTi  ,irtLÖsUwai^ öeT^ig  ,das  Zur-Schau-Stellen'  (mit  sekundärer  Hochstufe),  dUrj  s.  obei^ öUaLog,  ÖLTLccl^u),  SSrAog',  das  Perf.  Med.  öiösiyfxai,  und  dety^a  ,Beweis,  Bei^ spiel'  nicht  mit  idg.  g,  sondern   gr.  Neuerung;
lat.  dlcere  ,sagen',  dlcäre  ,feierlich  verkünden,  zusprechen,  weihen',  oskJ deikum  ,dicere',  umbr.  teitu,  deitu  ,dicito',  ablautend  osk.  dicust  ,dixerit'^ umbr.  dersicust  ds.,  osk.  da-dikatted  ,dedlcavit' ,  lat.  diciö  ,die  Macht  eines Herrn  über  andere,  Botmäßigkeit,  Gerichtsbarkeit',  indicäre  ,anzeigen', index  ,Anzeiger,  Angeber;  Zeigefinger'  (wie  auch  ai.  deHnl  ,Zeigefinger^), iudex  ,der  das  Recht  Weisende',  vindex  (yindicäre  =  vim  dicere),  causidicus] über  urir.  *Ekuo-decas,  Lugudec(c)as  (Gen.  Sg.)  s.  unter  1.  dek-.
got.  gateihan  ,anzeigen,  verkündigen',  anord.  tea,  jünger  tia  ,zeigen, darstellen,  ankündigen',  ags.  teon  ,anzeigen,  verkündigen',  ahd.  zlhan  ,an- schuldigen,  zeihen^,  wozu  anord.  tigenn  ,(*monstratus)  vornehm',  t'ign  f. ,Rang;  vornehmer  Mann';  ahd.  zeigön  ,zeigen',  wovon  zeiga  ,Weisung'; inziht  usw.  s.  oben;  ferner  anord.  teigr  m.  ,geradliniges  Wiesenstück' (,*Richtung'  =  ai.  desd-h  ,Gegend,  Platz,  Land'),  ablautend  ags.  tig,  tili , Anger,  Weide',  mnd.  tl{g)  m.  öffentlicher  Sammelplatz  eines  Dorfes', ahd.  zieh  , forum'.
=== WLD try
--- alt
39374:acech. hladati, poln. glqdac „sehen, schauen" (weiteres bei Berneker 
52378:dheia- (oder *dhaia-T) : dhl- „sehen, schauen“.
```


## [2026-09-05T20:14:00.068Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52370,52430p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print Walde-Pokorny dheia entry"
}
```


### [2026-09-05T20:14:00.119Z] TOOL RESULT

```
961, I 2 323, II 2 1, 526 zur Wzf. *bhu-e- von bheu- „werden“ gestellt 
werden (auch cpvco zeigt trans. Anwendung fiir hervorbringen) ; fecundus, 
fetus sehen aus wie von einem Yerbum *feo oder *feor gebildet (Stowasser 
Lat. Wb. u. femina ), doch ist wenigstens fiir fenus eine solche Yermitt- 
lung nicht anzunehmen, da es zur altertiimlichen Gruppe neutraler -nes- 
St. mit der Bed. von „wertvolle Habe, Geldeswert, Eigentum“ wie ai. 
rcknas- „Habe“, dt. Lehen , lat. pignus gehort. 

dheia- (oder *dhaia-T) : dhl- „sehen, schauen“. 

Ai. ddldhet „er schaute“, pi. didhimah , med. didhye, ndldhlia, konj. 
didhayat (nach Brugmann II 2 3, 1 07 vielleicht zum Praes. umgewandeltes 
Pf., vgl. Pf. didhaya ; ai. -ay-, -e- sprechen, sofern man nicbt Reimbildung 
zu dideti „scheint", d/dayat usw. zuhilfe rufen will, gegen den Ansatz der 
Wz. idg. *dhai-, der an dem parallelen *dhau-, s. u., keine verlaBlicbe 
Stutze hat), dhya-ti, dhya-ya-ti (letzteres jo-Praes., s. Persson Beitr. 700, 
nicht auf Grund einer Wzf. ar. dhyai- nach Wackernagel Ai. Gr. I 87) 
„schaut im Geiste, d. i. denkt, sinnt“, Ptc. dhycL-ta- und dhi-ta-, dhya „das 
Denken, Sinnen“, dhya-tar- „Denker“, dhyil-na- n. „das Sinnen, Nachdenken“, 
dhyaman- n. (Gr.) „Gedanke“; dht-h, acc. dhiy-am „Gedanke, Yorstellung, Ein- 
sicht, Yerstand, religioses Nachdenken, Andacht“, dhi-ti- „Wahrnehmung, Ge- 
danke, Andacht", dhtra- „sehend, klug, weise, geschickt", a vadlurayati „ver- 
schmaht (despicit), weist zuriick, verachtet", prakr. herai „sieht“;5-Bildung wie 
got. fludeisei ) ai. dhiyasana- „aufmerksam, achtsam' £ (nach Uhlenbeck Ai. 
Wb. 126 auch dhlsamdna- RV. 10, 26, 6; vermutlich auch dhisana- wenn „ver- 
standig, klug“, dhisanyant- wenn , aufmerksam, andachtig“, dhisa Instr. Adv. 
w r enn „mit Andacht, Eifer oder Lust ‘, doch vgl. andererseits das zu lat. festus, 
fanuni , idg. *dhes- „religios“ gehorige dhisnya- „andachtig‘ £ ; sehr fraglich 
ist, ob die in ai. dJn-h auftretende Anwendung der Wz. auf religiose Be- 
schaulichkeit so alt ist, daB sie auch zur Deutung von gr. -&iaoos „Ver- 
ein zur Yeranstaltung gottesdienstlicher Handlungen" verwendet werden 
diirfte, Lit. bei Boisacq s. v.); 

av. da{y)- „sehen“, z. B. a-dida'ti „betrachtet daidyanto Nom. pi. Ptc. 
„die sehenden" (usw., s. Bartholomae Airan. Wb. 724). Ptc. paiti-dita- „er- 
blickt“, -diti- f. „das Erblicken", dad a- „einsichtig. klug“ (dehnstufig wie 
- dida'ti ), -da(y)-, -dt- f. als 2. Zsglied „Sehen, Blick; Einsicht; Absicht“; 



532 


dhau- — dheig- 


-daman- als 2. Zsglied „Absieht“; daeman- n. „Auge, Augapfel; Blick“, 
doidra- n „Auge“, dacna „Religion“ und „inneres Wesen, geistiges Ich“ 
(s. Reickelt Av. Elem.-B. 448, vgl. etdcolov und dt. „Gewissen“); np. d/dan 
,sehenA dim ,.Gesicht, Wange“. 

Gr. oijfxa , dor. oaya „Zeichen, Kennzeichen, Merkmal usw/‘ ( *dhia-mn 
= ai. dhyaman - ; Lit. bei Boisacq s. v. ; iiberholt Wackernagel KZ. 30, 295, 
Schrader KZ. 30, 481), og/uatvw ,,mache durch ein Zeichen kenntlich usw.“. 

Alb. diture , ditme ,.Weisbeit, Gelehrsamkeit“, dinak „listig“; got. filu- 
deisei .,Schlauheit, Arglist“ (vgl. o. ai . dhiyasana-) 1 ). Lit . (Timst(a), cTing(a) 
„diinkt“ (nach Uhlenbeck Ai. Wb. 137 aus Ace. *dliii»> = ai. dhiyam , *sta-t, 
jW-t „stebt im Sinn, geht in den Sinn ein“). 

Vgl. Fick I 4 74, 466 (anord. dls ,.Gottin” ist aber fernzuhalten; s :) III 4
```


## [2026-09-05T20:14:07.192Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF din\"; python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'دین' in p and 'کیش' in p:\n        print('leaf',i, p[:400].replace('\\n',' '))\nEOF",
 "description": "Grep Noushin for din"
}
```


## [2026-09-05T20:14:08.077Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/semantic",
 "prompt": "Give the etymology of 'semantic'/'semantics' and of Greek sema: what PIE root is given and what is the chain?"
}
```


### [2026-09-05T20:14:28.611Z] TOOL RESULT

```
=== FSF din
leaves 485
leaf 38 ‫آن سر‬   ‫گرگین برای فریب دادن بیژن گورفتار‬                   ‫از اسدی ( گرشاسب‌نامه ‪:)۸۵-۶۳‬‬  ‫ساختن او در توران زمین‪ ,‬به فرمان‬                   ‫تو گفتی که بد جنگییی در کمین‬ ‫کسیخسرو در زندان است‪ .‬رستم از‬               ‫تنش سربهسرآلت جنگ و کین‬       ‫کیخسرو بخشایش او را می‌خواهد‪:‬‬         ‫در بیت زیر «الت تخت شاهی» بكار‬                ‫گر آمرزش شاه نایدش پیش‬         ‫رفته و مراد
leaf 45                                                                               ‫آهیختن‬   ‫خوب گفتن پیشه کن باهر کسی‬ ‫کاین برون آهیخد از دل بیخ کین‬                                            ‫‪:)۵۳۶۴-۱۳‬‬  ‫منروز همی بینمو گویی تو شبست این‬                 ‫کرا دوست داری و کام تو اوست‬   ‫خنجر‬           ‫یهخی‬                   ‫هم ک‬                      ‫آواه‬                         ‫رت خ‬   
leaf 100 ‫برز‬                   ‫ی‬‫کر‬                   ‫ید ه‬                      ‫خانهٌ خود باز رو‬                                    ‫برخ (به فع اول)‬ ‫همتای برد‪.‬‬         ‫شد‬                     ‫اکی‬‫بلس‬                          ‫اط‬                                         ‫بهر بهره نصیب‪:‬‬                                     ‫برداشتن‬             ‫برین نیز چندی بگردید چرخ‬                  
leaf 255                                                 ‫‪Yar‬‬                                            ‫دیزه‪‎‬‬                            ‫فرهنگ بهدینان)‪:‬‬             ‫معنی دراز کردن به درازا کشیدن]‪ :‬دیرپاء‬                         ‫(دقیقی ‪:)۶-۸۶-۰۵‬‬                                                ‫دیرگذر‪:‬‬                   ‫بیاموز آیین و دیسن بهی‬ ‫که بی‌دین ناخوب باشد مهی‬                
leaf 321                                            ‫‪۳1۸‬‬   ‫درد دوری و جدایی کسی را یا چیزی رابا‬                                ‫(رودکی‪ .‬نفیسی‪:)۹۳۴ .‬‬   ‫شکیبایی و بردباری به خود هموار نمودن‪:‬‬                ‫سخت شکوهم که عجز من بنماید‬  ‫سیاوش از پدر رنجیده به توران پناه برده‬          ‫ورچه صریعم ابا فصاحت سحبان‬   ‫است‪ .‬افراسیاب دربارة او به پیران گوید‪:‬‬                            ‫(ناصر ‪
leaf 462  ‫وین‬                                          ‫‪۹۵۴‬‬              ‫فرود آمد از تخت ويله کنان‬                        ‫سزاوار هر کس ببخشید گنج‬  ‫زنان بر سروموی و رخ راکنان‬                         ‫بویژه کسی کش فزون بود رنج‬  ‫)‪(1-۳-4۳‬‬                                           ‫(‪)۲-۲۲۱-۲۶۸‬‬                                           ‫وین‬         ‫‪-۳‬ویژه‪.‬ویذگان‪:‬حاصءخاصان‪,‬آشنایان نزد
```


### [2026-09-05T20:14:34.429Z] TOOL RESULT

```
# Etymology of Semantic/Semantics

**PIE Root:** The word traces back to the Proto-Indo-European root *dheie-, meaning "to see, look."

**Etymological Chain:**

1. **Greek origin:** The term derives from Greek *sēma* ("sign, mark, token; omen, portent; constellation; grave"), which comes from the PIE root *dheie-.

2. **French intermediary:** The French term *sémantique* was applied by Michel Bréal in 1883 to describe the psychology of language.

3. **English adoption:** The adjective "semantic" entered English in 1894, defined as "relating to significance or meaning."

**Related Development:** The Greek *sēmantikos* literally means "significant," derived from *sēmainein*, meaning "to show by sign, signify, point out, indicate by a sign."

**Cross-linguistic connections:** The same PIE root produced Sanskrit *dhyati* ("he meditates"), linking semantic meaning to contemplation across ancient languages.
```


## [2026-09-05T20:14:41.954Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(d['FSF'].get('page_offset'));print(d['MON'].get('page_offset'));print(d['SNS'].get('page_offset'))\"",
 "description": "Get page offsets"
}
```


### [2026-09-05T20:14:43.765Z] TOOL RESULT

```
484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking
None
242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
```


## [2026-09-05T20:14:44.391Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85%D8%A7/",
 "prompt": "What does Farhang-e Mo'in (فرهنگ معین) say for سیما — its origin tag (e.g. [ع.] Arabic) and meanings? Also report Dehkhoda's note on its origin if shown."
}
```


### [2026-09-05T20:14:50.140Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for سیما

**Origin Tag:** (اِ) — indicating Arabic origin

**Meanings listed:**
1. "چهره ، قیافه" (face, appearance)
2. "علامت ، هیئت" (sign, form/bearing)

---

## Dehkhoda's Note on Origin

Dehkhoda describes سیما as originating from Arabic (ع اِ), defining it as "نشان و علامتی که شناخته شود بدان خیر و شر" — a distinguishing mark by which good and evil can be recognized. The lexicographer notes this meaning appears in classical Islamic linguistic sources like *Ghiyas al-Loghat* and *Tarjoman al-Quran*.
```


## [2026-09-05T20:15:02.985Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"wasama\\|w-s-m\\|wasm\\b\" FVQ.txt | head -10; echo \"---- list of entries with 'mark'\"; grep -n \"^.\\{0,20\\}mark,\" FVQ.txt | head -20; echo \"=== KLN sema entry\"; sed -n '217402,217470p' KLN_1971.txt",
 "description": "Search FVQ and Klein"
}
```


## [2026-09-05T20:15:03.570Z] TOOL CALL #62: WebSearch

```json
{
 "query": "Arabic sīmā سيما \"sign, mark\" borrowed from Greek σῆμα Qur'an loanword etymology"
}
```


### [2026-09-05T20:15:04.740Z] TOOL RESULT

```
---- list of entries with 'mark'
4850:sign or mark, was used quite generally, for signs of the weather (Gen. 
6192:nearer the mark, however, in suggesting that l^fi is a borrowing from Mesopotamia 
11514:Sign, mark, token. 
13929:Fraenkel's remark, Fremdw, 149), though some claimed that it was 
=== KLN sema entry
<pd)V7){xa, ‘sound’. See semantics and cp. hy- 
pheme, morpheme, solideme. 
semantic, adj., 1) pertaining to meaning; 2) per- 
taining to semantics. — Gk. a^avTwcos, ‘signi- 
ficant, meaning’. See next word. 

'semantics, n., the science of the meanings of 
words. — F. semantique, coined by Michel 
Br6al, author of Essai de semantique (1897) fr. 
Gk. aY][iavTLx6^, ‘significant, meaning’, fr. 
CTTjfiatveLv, ‘to signify’, fr. cri^a, ‘sign’, which 
is cogn. with OI. dhlh, dhyanafy , ‘thought’, 
dhyati, dhydyati, ‘thinks’. See dhyana and cp. 
semeio-, asemia, and the second element in 
teloseipe, diseme, triseme, tetraseme. For the 
ending see suff. -ics. 

semaphore, n., an apparatus for'signaling. — F. 
semaphore, lit. ‘a bearer of signals’, compound- 
ed of Gk. <rr\\x&, ‘sign’, and ~96po<;, ‘carrying’. 
See prec. word and -phore. 

Derivatives: semaphore, tr. and intr. v., serna- 
phor-ic, semaphor-ic-al, adjs., semaphor-ic-al-ly, 
adv., semaphor-ist , a. 

semasiology, n., semantics. — G. Semasiologie, 
lit. ‘the study of meaning’, coined by Christian 
Karl Reisig [1792(?)-1829] fr. Gk. cr^aota, 



‘significance, meaning’ (fr. C7^a, ‘sign’), and 
-Xoyia, fr. -X6yo?, ‘one who speaks (in a cer- 
tain manner); one who deals (with a certain 
topic)’. See semantics and -logy, 
sematic, adj., serving as a sign or warning. — 
Formed with adj. suff. -ic fr. Gk. ot^oc, gen. 
ovjpLaTo?, ‘sign’. See semantics, 
semblable, adj., resembling. — F., fr. sembler, ‘to 
seem, resemble’. See semble and -able, 
semblance, n., likeness; outward appearance. — 
ME. semblaunce, fr. OF. semblance, ‘resem- 
blance’ (in F. this word occurs only in derivatives 
and compounds), fr. OF.(= F.) semblant, pres, 
part, of sembler ; ‘to resemble’, fr. L. simulare , 
‘to make like, represent’. See semble and -ance 
and cp. vraisemblance. 

semble, intr. v., it seems (legal term). — F., 3rd p. 
sing. pres. ind. of sembler , ‘to seem, resemble’, 
fr. L. simulare , ‘to make like, represent’. See 
simulate and cp. resemble. 
sem£, adj., sown, powdered. — F., ‘sown’, pp. of 
semer , fr. L. semindre, ‘to sow’, fr. semen , gen. 
seminis , ‘seed’. See semen, 
semeio-, combining form meaning ‘sign, symp- 
tom’. — Gk. avjpLet.0-, fr. arjp.eiov, ‘sign’, fr. 
avjp.a, ‘sign’. See semantics, 
semeiology, n., 1) the art of using signs, sign lan- 
guage ; 2) the study of the symptoms of a disease, 
symptomatology. — Compounded of semeio- 
and Gk. -Xoyta, fr. -X6yo c,, ‘one who speaks (in 
a certain manner) ; one who deals (with a certain 
topic)’. See -logy. 

Derivatives : semeiolog-ic-al,ad)., semeiolog-ist,n. 
semeiotic, adj., 1) pertaining to signs; 2) pertain- 
ing to symptoms. — Coined by the American
```


### [2026-09-05T20:15:13.980Z] TOOL RESULT

```
Web search results for query: "Arabic sīmā سيما "sign, mark" borrowed from Greek σῆμα Qur'an loanword etymology"

Links: [{"title":"سيماء - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%85%D8%A7%D8%A1"},{"title":"Simiyya","url":"https://en.wikipedia.org/wiki/Simiyya"},{"title":"σῆμα - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CF%83%E1%BF%86%CE%BC%CE%B1"},{"title":"σημεῖον - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CF%83%CE%B7%CE%BC%CE%B5%E1%BF%96%CE%BF%CE%BD"},{"title":"\"سيماء\" meaning in Arabic","url":"https://kaikki.org/dictionary/Arabic/meaning/%D8%B3/%D8%B3%D9%8A/%D8%B3%D9%8A%D9%85%D8%A7%D8%A1.html"},{"title":"145 Aramaisms in the Qur’—n and their Significance Robert M. Kerr","url":"https://almuslih.org/wp-content/uploads/Library/Kerr,%20R%20-%20Aramaisms%20in%20the%20Quran%20and%20their%20Significance.pdf"},{"title":"Hebrew (עברית) – Omniglot Blog","url":"https://www.omniglot.com/bloggle/?cat=121"},{"title":"σῆμα - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CF%83%E1%BF%86%CE%BC%CE%B1"}]

Based on the search results, here's what I found about the etymology of Arabic sīmā (سيما):

Arabic سيماء (sīmā) was borrowed from Aramaic סִימָא (sīmā) / סִימָנָא (sīmānā), which came from Ancient Greek σῆμα (sêma) and σημεῖον (sēmeîon).

The Greek root σῆμα means "mark" or "sign," and it derives from Proto-Indo-European *dʰyéh₂mn̥, from *dʰyeh₂- meaning "to notice".

This is a clear example of a loanword that traveled from Greek through Aramaic (likely Syriac) into Arabic. The word appears in the Qur'an and has been adopted into Islamic Arabic vocabulary, where it retains its original meaning of "sign" or "mark."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:15:25.166Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%85%D8%A7%D8%A1",
 "prompt": "Give the Arabic entry سيماء (sīmāʾ): full etymology (Aramaic? Greek σῆμα?), meanings, and any note about the root w-s-m."
}
```


## [2026-09-05T20:15:26.585Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian دیدن (didan) 'to see': Middle Persian form, Proto-Iranian root, and what it says about the suppletive present stem بین (bin-)."
}
```


### [2026-09-05T20:15:30.848Z] TOOL RESULT

```
# Arabic Entry: سيماء (sīmāʾ)

## Etymology
The word is "Borrowed from Aramaic סִימָא (sīmā) / סִימָנָא (sīmānā), from Ancient Greek σῆμα (sêma), σημεῖον (sēmeîon)."

## Meanings
1. Sign, mark, or trait
2. Look, appearance, or expression

The Qur'anic citation (48:29) illustrates the second sense: "The mark of them is on their foreheads from the traces of prostration."

## Note on w-s-m Root
The page references a related Arabic term شِيم (šīm), suggesting a connection to marking or distinctive features, though the etymological entry does not explicitly discuss the Semitic root system. The word ultimately derives from Greek origins rather than developing from the native Semitic w-s-m root family.
```


### [2026-09-05T20:15:32.691Z] TOOL RESULT

```
# Etymology of Persian دیدن (didan)

**Middle Persian Form:**
The word derives from Middle Persian dytn' (/didan/), which underwent phonetic changes over time.

**Proto-Iranian Root:**
It traces back to Proto-Iranian *daiH- meaning "to look, see," with cognates appearing in Avestan diδāiti and Old Armenian dēt.

**Suppletive Present Stem:**
The present stem بین (bin-) represents a suppletive formation, meaning the verb uses completely different roots for different tenses. As the source explains: "This verb's present stem is suppletive, it is from Middle Persian wēn-, the present stem of dīdan, ultimately from Proto-Indo-European *weyd- ('to see')."

This dual etymology—where the past tense uses the daiH- root while the present uses the weyd- root—illustrates how Persian merged two originally distinct Indo-European verbs meaning "to see" into a single paradigm.
```


## [2026-09-05T20:15:42.239Z] TOOL CALL #65: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%CF%83%E1%BF%86%CE%BC%CE%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D8%AF%DB%8C%D9%86%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%B3%D9%8A%D9%85%D8%A7%D8%A1' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D8%AF%D9%86' \\\n 'https://www.etymonline.com/word/semantic' \\\n 'https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85%D8%A7/' \\\n 'https://en.wiktionary.org/wiki/%D8%A2%D8%A6%DB%8C%D9%86' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 132, root Dheye: jan/sema/adine/sima/didan/ayin' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:15:48.473Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d233a82c39fefcdb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c841fb8b2c28e58c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/06039bd0ab15664f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/244465165dfbaccc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ae52bfb460c4fde.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b5ec98434093ce8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a32bc938067979f6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/098d0f038098036f.txt
```


## [2026-09-05T20:16:01.237Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[17]\nprint('=== leaf 17 (printed ~557) tail:')\nprint(p[-1800:])\nEOF\necho \"=== SNS\"; grep -n -i \"vēnāk\\|venak\\|vinak\\|ādēn\\|aden\\|dēn\\b\" SNS.txt | head -10\necho \"=== IEC dhi\"; grep -n \"dhiā\\|dhī-\\|dhiiā\" IEC.txt | head -10",
 "description": "BQT jan page, SNS, Mann"
}
```


### [2026-09-05T20:16:03.001Z] TOOL RESULT

```
=== leaf 17 (printed ~557) tail:
                                  ‫آلذهب؛ سلامان و ابال‪ ,‬تحفة الاحرار» سبحة‬
                                                         ‫وجنون »‬
                                                               ‫لابرار‪ .‬یوسف و زلخا ‪ .‬لیلی م‬
                                                         ‫و تألیفات او بنش‬           ‫خرد نامه اسکندری‬
                                                         ‫فارسی ‪ :‬نقد النسوص فى شرح شش الفصوص »‬
                                                         ‫تفحات‌الانی " لواح » لوامم > شواعدالنبوة »‬
                                                         ‫‪ .‬وفات جامی‬        ‫اشعة اللمه‌ات وبهارستان است‬
                                                         ‫بال ‪۸٩۸‬‏ در هرات اتفاق افتاد « تاریخ‌ادیبات‬
                                                          ‫ابران‪ .‬کدترشفق‪ .‬تهران‪ .‬چایشان‪#‬داش ‪۱۲۳۱‬‬
                                                         ‫‪ « > ۷۵۳‬جامی ‪ .‬علی اصغر‬              ‫‪-‬‬    ‫‪۳۳‬‬
                                                                                                    ‫ص‬
                                                         ‫چايخانةٌ بانك ملی‬     ‫‪ .‬پران ‪۰۲۳۱‬‬             ‫حکت‬
                                                                                                  ‫ابرآن >‬

                                                         ‫جالای ‪ -‬از ‪:‬جان ‪ +‬ان ( نبت ) ‪:‬‬
                                                         ‫‪,‬حبوب ‪ « :‬شرط مودت قباشدباندیشه‬
                                                                                       ‫ممشوق م‬
                                                                   ‫بگررفتن »‬      ‫جان دل اجزامهنران‬
                                                          ‫‪.‬‬     ‫‪ +‬کلتان ‪۵۳۱‬‬

=== SNS
992:2 parts, Wiesbaden, 1964. 
15331:"'AoVj* -*-^- ir^^j Jjl^ . W .orf^rvissaden: ^"•l 
28322:vinakti f -vivekti 272/18 
33745:ayadenisn 84/20 
=== IEC dhi
```


## [2026-09-05T20:16:03.429Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%DB%8C%D9%86/",
 "prompt": "What does Farhang-e Mo'in (فرهنگ معین) give for دین — origin tag in brackets (e.g. [په.] Pahlavi or [ع.] Arabic) and meanings? Also Dehkhoda's note on origin if present."
}
```


### [2026-09-05T20:16:09.843Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for دین

According to Farhang-e Mo'in (the Moein Dictionary), the word دین has the following classifications:

**Origin Tags:**
- [ع.] (Arabic): قرض، وام (debt, loan) - plural: دیون
- [په.] (Pahlavi): 
  1. آیین، کیش (religion, creed)
  2. راه، روش (way, method)
  3. نام روز بیست و چهارم از هر ماه شمسی (name of the 24th day of each solar month) and also the name of a Zoroastrian deity guardian of that day

**Dehkhoda's Note on Origin:**
Dehkhoda's extensive entry indicates that while دین appears in Arabic with meanings of "judgment" and "law" (referencing Akkadian origins), the word in Persian carries meanings rooted in the Avestan دَئِنا (daēna), signifying conscience, spiritual characteristics, and moral consciousness—one of the five inner faculties of humans.
```


## [2026-09-05T20:16:19.627Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in range(12,22):\n    p=t[leaf]\n    lat=[l for l in p.split('\\n') if re.search(r'[A-Za-z]{3}',l)]\n    print('=== leaf',leaf,'printed~',leaf+540)\n    for l in lat[:8]: print('   ',l.strip()[:200])\nEOF",
 "description": "Find Mo'in footnote for jan"
}
```


### [2026-09-05T20:16:21.344Z] TOOL RESULT

```
=== leaf 12 printed~ 552
    ‫‪ .‬آوردن «بولکر‬     ‫‪ ۰.‬بهلوی ‪natruwã‬‏‬     ‫(‪natan ۰ [۷2 21‬‏ _‬              ‫هز ‪7 ۰‬‬     ‫‪۴‬‬
    ‫‏‪۲ ۱ Jl andhara‬نونک للاسم رد‌عقاوم«باجنپ هدودح‪.‬یکسرون ‪ ۱۱ ۰۹۲4‬‏‪G.‬ها‪11‬خا‪_1‬‬
=== leaf 13 printed~ 553
=== leaf 14 printed~ 554
    ‫‪natinêl)al(maj‬‏‬                   ‫اما‬      ‫‪ ( .‬نقل کرده‬        ‫امن کمه را تسلا » جامتئوشن ‪ ) €‬وم‬          ‫موف‬
    ‫‪6 ۸۸‬‬    ‫بونکر‬        ‫«‬       ‫گفتن است‬            ‫‪natfug‬‏‬       ‫ونطامر آن ‪ 0‬حزوارش و بپلوی آن‬          ‫و ‪02610۳‬‬
    ‫بارسی باستان‬                  ‫‪kamãy‬‏‬          ‫مولر بهتر توضیح داده و «حامه» را از کلمة پهلوی‬
=== leaf 15 printed~ 555
=== leaf 16 printed~ 556
    ‫اوستایی ‪ ( 2128‬زندگی کردن) ازبکرشه‌است‪:‬‬           ‫‏‪ Justi‬و‏‪ ۶۳ . Miller‬جان بکالمةٌ‬
=== leaf 17 printed~ 557
=== leaf 18 printed~ 558
=== leaf 19 printed~ 559
=== leaf 20 printed~ 560
    ‫( ابدیت ) ؛ ‪ ( ۵۷۵۷‬الى الابد ) » پهلوی ‪› 0۵۱6۷2۷‬‬             ‫و ‪ -‬اومتا ‪taY‬‏‬
=== leaf 21 printed~ 561
```


## [2026-09-05T20:16:28.138Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[16][-2200:])\nEOF",
 "description": "Print BQT jan footnote"
}
```


### [2026-09-05T20:16:30.930Z] TOOL RESULT

```
 ۷۸‬کردی و بلوچی و اففانی ( دخیل )‬
  ‫« استق ‪ ( > ۳۱‬وجه اشتقاق هرن رماردود دانته اند ) « هوبشمان ‪ » :۳۱‬اورامالی‬          ‫‪2‬‬
  ‫مزع < ‪ .4‬اورامان‪ »۲۲۱‬کیلکی ‪ 02‬ابن‌سینا جان‌را بمعنی‌شی بادکرده ‪ *:‬دیگر ( ازانواع‬
 ‫حکمت ) آن بود که از حال هستی چیز هامارا آ کاهی دهد تجاان ما صورت خوش بابد‬
  ‫(وح‬
    ‫بود ‪ .‬د»ا«شنامه ‪۸٩‬‏ و مط » در ادیبات فارسی متر ادف روان ر‬           ‫لنی‬ ‫اآ‬‫هشت‬
                                                                                ‫جیکی‬‫و‬
                                                        ‫‪۱‬‬             ‫اسانی ) همآمده ‪:‬‬
                                      ‫اکر موری سخن کوبد و کر موبی روان دارد‬
            ‫من‌آن‌مور سخن گویم» من‌آن موم که جان‌دارد‪.‬‬
        ‫‪ ۶‬عمعق بخاری >‪.‬‬
                  ‫‪:‬سشق‪.۳۵۹‬‬
                         ‫‪ - ۴‬باین معنی ازرشة اوستابی ‪ (021‬زدن »کشتن ) رك ا‬
  ‫‏‪ ٥‬جماي ‏ نورالدین عبدالرحمن جامی بن نظام الدین دشتی متولد بال ‪ ۷۱۸‬در‬
 ‫ارادت بشیخ‬      ‫و نیز ببب‬     ‫)‬
                               ‫م(‬‫اویش‬
                                    ‫جد خ‬
                                       ‫‪.‬ی بمناسبت مول‬
                                                    ‫خرجرد اوزلابت جام خراسان و‬
  ‫رفت‬     ‫قند‬
            ‫مترو‬
               ‫سرا‬
                 ‫الالام احمد جامی ( متوفی در ‪ ) ۹۳۵‬جامی تخلص کرد ‪ .‬او همراه بدر به‬
   ‫ودرآن دیار یکب علم و ادب پرداخت و در علوم دینی و ادب و تاریخ کمال یافت وسپس‌بسیر‬
  ‫وواجه علی سمرقندی وقاضی زاده رومی کرد‬   ‫ولوك اقتاد و ببروی سمدالدین محمدکاشفری خ‬‫ص‬
  ‫و بمرتبة ارشاد رسید و در سلك بزرگان طریقةٌ نقشیندی در آمد» ویس از وفات سعدالدین‬
  ‫کاشقری خکلهیغة قشبندی بود خلافت ابن طربقت‌بدو تعلق بافت و شهرت وی شایم شدومورد‬
   ‫کزشت‬
      ‫احترام بزرکان عر کردید ‪ .‬جامی سفری بحج رفت و از راه دمشق توبریز بهرات با‬
  ‫(‪ . ) ۸۷‬پادشاه مماصر وی ابوالغازی سلطان‌حسین بایقرا و وزبر عصی امیر علیشیر بود ‪ .‬جامی‬
                                                                                      ‫‪۸‬‬
 ‫زار منظوم او ‪ :‬دبواق اشمار ( مشتمل بر‬
                                     ‫بزرکترین شاعر و ادیب قرن نهم حجری است ‪ .‬اآث‬
 ‫(برهان اطع ‪)۵۷‬‬                                                  ‫بقیه درسضحهٌ ‪۹٠٠‬‏‬
```


## [2026-09-05T20:16:51.808Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD den/didan\"; grep -no \"dēn \\[dyn[^]]*\\][^.]*\\.\\|dīdan[^.]*\\.\\|gyān \\[[^]]*\\][^.]*\\.\" PHD.txt | head -10; echo \"=== NYB den gyan\"; grep -no \"dēn \\[[^]]*\\]\\|gyān \\[[^]]*\\]\\|handēšišn\\|dītan \\[\" NYB_vol2_glossary.txt | head -10",
 "description": "MacKenzie/Nyberg den gyan didan"
}
```


### [2026-09-05T20:16:51.880Z] TOOL RESULT

```
=== PHD den/didan
123:dīdan .
225:dīdan, ayārd- Py’lt-ytn! | M ?y^rd-] be agitated, seethe.
296:dīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake.
512:dīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle.
701:dīdan.
755:dīdan.
2259:dīdan.
3303:dīdan, wizandidan.
3436:dīdan.
3566:dīdan.
=== NYB den gyan
1388:dēn [dwšdyn']
1849:dēn [h'mwdyn']
```


## [2026-09-05T20:16:56.268Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"dīdan, wēn- \\[[^]]*\\][^.]*\\.\\|dēn \\[dyn'[^]]*\\][^.]*\\.\\|gyān \\[gy[^]]*\\][^.]*\\.\" PHD.txt | head; echo \"---\"; grep -n \"HZYTWN\" PHD.txt | head -3; echo \"=== NYB gyan/den entries\"; grep -n \"^gyān\\|^dēn\\|gyän\\|dên\" NYB_vol2_glossary.txt | head -10",
 "description": "Find MacKenzie didan/den/gyan entries"
}
```


### [2026-09-05T20:16:56.347Z] TOOL RESULT

```
---
99:didan, wën- [HZYTWN-tn' < A Угу; dytn', wyn- | M dydn, wyn-, N =, bin-] see. 7-ASn : sight, seeing. ««išnīģ : visible.
=== NYB gyan/den entries
1261:dēn-kart [dyn'krt'] *Religion's Decisions",
```


## [2026-09-05T20:17:56.225Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"dēm \\[[^]]*\\][^.]*\\.\\|dēmān[^.]*\\.\\|dēsag[^.]*\\.\" PHD.txt | head -8; echo \"=== BRT dai/di root 724\"; grep -n \"^•  j\\.,  g\\.  dä{y)\\|dä{y)-\\|dā(y)-\" BRT.txt | head -5",
 "description": "PHD dem, BRT day root"
}
```


### [2026-09-05T20:17:58.666Z] TOOL RESULT

```
394:dēmān [hndym’n' | = M] before, in the presence of.
394:dēmānģar [kndym’ nkl] introducer (into the presence).
893:dēmānīh; pēšgāh.
964:dēmān, pēš.
2010:dēsag.
2300:dēsag.
3211:dēmānīh; in the — of handēmān.
=== BRT dai/di root 724
```


## [2026-09-05T20:18:03.959Z] AGENT

Now I have enough evidence. Writing the verification file.


## [2026-09-05T20:30:30.469Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build132.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Dheye\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰeyh₂- (Pokorny dheiə- : dhyā- : dhī-) 'to see, look; to perceive mentally'\",\n \"note\": \"Pokorny IEW 243 heads the entry 'dheiə- : dhyā- : dhī- „sehen, schauen“' and gathers under it exactly the material of this chart: Skt. dīdheti / dhyāyati / dhyāna- / dhī-, Av. dā(y)- 'sehen', daēman- 'Auge', daēnā 'Religion', NP dīdan, dīm, and Gk. σῆμα. Nourai's headword 'Dheye', the language label 'Indo-European' and the gloss 'to see' are therefore a fair rendering of the root box, and POK:243 is the right page. Two structural caveats run through the whole chart and are argued node by node below: (a) the Old-Persian/Pahlavi/Persian present stem vain- / wēn- / bīn- (nodes 4, 5, 6, and the Sogdian wyn of node 18) does NOT belong to this root — it continues a separate root, Pokorny 1123 *wei(H)-no-/*weyd-ne-, and is only the suppletive present partner of dī- in the Iranian paradigm; Nourai's own source Abolghasemi (FFD:55) says so in as many words. (b) Av./OIr. daiš- 'to show' (node 10, whence andīšīdan) belongs to PIE *deiḱ- 'zeigen' (Pokorny 188), not here. Modern Iranian scholarship (Cheung 2007 s.v. *daiH¹) also warns that the Indo-Iranian root *dai̯H- has no secure cognates outside Indo-Iranian, so the Greek branch (node 19) is less certain than Pokorny's page suggests.\",\n \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۲۴۳ فرهنگ خود مدخل «dheiə- : dhyā- : dhī- «دیدن، نگریستن»» را آورده و همان مواد این نمودار را زیر آن گرد کرده است: سنسکریت dīdheti و dhyāyati و dhyāna- و dhī-، اوستایی dā(y)- «دیدن»، daēman- «چشم»، daēnā «دین»، فارسی نو «دیدن» و «دیم»، و یونانی sêma. پس نام ریشه، برچسب «هندواروپایی» و معنای «دیدن» و نیز ارجاع POK:243 همه درست است. اما دو اشکال ساختاری در سراسر نمودار هست: نخست آنکه ستاک حال vain- / wēn- / بین (گره‌های ۴ و ۵ و ۶ و wyn سغدی در گرهٔ ۱۸) از این ریشه نیست، بلکه دنبالهٔ ریشهٔ جداگانهٔ *wei(H)-no- (پوکورنی ۱۱۲۳) است و تنها در نظام صرفی ایرانی همکار مکمّل (suppletive) ستاک گذشتهٔ دید- شده است — ابوالقاسمی، که خودِ نورایی به او ارجاع می‌دهد (FFD ص ۵۵)، به‌صراحت می‌نویسد «دیدن» و «بین» دو ریشه‌ای است. دوم آنکه daiš- «نشان دادن» (گرهٔ ۱۰، سرچشمهٔ «اندیشیدن») از ریشهٔ *deiḱ- (پوکورنی ۱۸۸) است نه از این ریشه. افزون بر این، چونگ (۲۰۰۷) هشدار می‌دهد که ریشهٔ هندوایرانی *dai̯H- بیرون از هندوایرانی هم‌ریشهٔ مطمئنی ندارد و بنابراین شاخهٔ یونانی (گرهٔ ۱۹) به آن استواری که صفحهٔ پوکورنی می‌نماید نیست.\",\n \"sources\": [W+\"%CF%83%E1%BF%86%CE%BC%CE%B1\", W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n  {\"ref\":\"POK:243\",\"status\":\"supports\",\n   \"note\":\"POK_01.txt, form-feed page 253/254 (IEW p.243): '…dhiā- : dhī- ,sehen, schauen'. Ai. dīdheti ,er schaute'… dhyā-ya-ti (jo-Präs.) ,schaut im Geiste, d. i. denkt, sinnt'… av. dā(y)- ,sehen'… daēman- n. ,Auge, Augapfel; Blick', dōiθra- n. ,Auge', daēnā ,Religion' und ,inneres Wesen, geistiges Ich'; npers. dīdan ,sehen', dīm ,Gesicht, Wange'; gr. σῆμα, dor. σᾶμα ,Zeichen…' (*dhiā-mn = ai. dhyāman-)'. The root box as drawn.\"}\n ],\n \"consulted\": [\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 831 f. (WLD_Bd1 djvu lines 52378-52420)\",\"stance\":\"supports\",\n   \"note\":\"'dheiə- (oder *dhaiə-?) : dhī- „sehen, schauen“.' — the same list, with 'av. da(y)- „sehen“ … Ptc. paiti-dita- „erblickt“ … daēman- n. „Auge, Augapfel; Blick“, dōiθra- n. „Auge“, daēna „Religion“ und „inneres Wesen, geistiges Ich“ … np. dīdan „sehen“, dīm „Gesicht, Wange“. Gr. σῆμα, dor. σᾶμα „Zeichen…“ (*dhiā-mn = ai. dhyāman-)'. Note that the Avestan participle it prints is paiti-dīta-, never *upa-dīta-.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985, d-list (AHD_watkins1985.txt line 377)\",\"stance\":\"supports\",\n   \"note\":\"'dheiə-. To see, look. Variant form *dhyā- (< *dhyaə-) in: a. suffixed form *dhyā-mn̥ in Greek sēmeion and sēma (stem sēmat-), sign: SEMANTIC… b. Sanskrit dhyāti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheiə- 243.]' — Nourai's 'AHD' citations on nodes 19 and 22 are this entry.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"Etym. Dict. of the Iranian Verb, s.v. *daiH¹ (CHEUNG.txt lines 4249-4356)\",\"stance\":\"partial\",\n   \"note\":\"'*daiH¹ “to look, see” … «PIE? ⊙ LIV: 141 f. | Pok.: 243»' and the closing note 'An IE etymology for this IIr. root is uncertain, in the absence of any credible cognates. Only Alb. di “knows” can be cited in LIV… Gr. σῆμα / σᾶμα “sign, mark” is unrelated.' Cheung accepts the Indo-Iranian root and Pokorny's page number but not the Greek branch.\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, Indo-European Comparative Dictionary (grep 'dhiā', 'dhī-' in IEC.txt)\",\"stance\":\"silent\",\n   \"note\":\"no headword for this root turned up; Mann's d-section has no *dhiā-/*dhī- 'see' entry, so he neither confirms nor contradicts.\"}\n ],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\":1, \"lang\":\"Avestan\", \"words\":\"dâ 3, dây, dâi, dî; vaěna 2; upa-dîta; daěman\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Two of the four items are exactly right, two are not. (a) Av. dā(y)- / dī- 'to see' is real: Bartholomae AiW 724 ff. lists the reduplicated present ā-diδāiti 'betrachtet', the participle daiδyantō 'die sehenden', and Pokorny 243 quotes the same forms; Nourai's 'dā 3' is simply Bartholomae's third homonym dā- and his 'dây/dâi/dî' are the ablaut variants day-/dī- of that root, so the citation is faithful. (b) daēman- n. is likewise real and correctly glossed: Bartholomae AiW col. 731 (BRT.txt line 12457) 'j. daēman- n. 1) ‚Auge, Augapfel‘ … 2) ‚Blick‘' (Yt 10.48, Yt 14.56) — it is a -man- derivative of the same root and the direct ancestor of MP dēm / NP dīm. (c) 'vaēna 2 : observer' does NOT belong here: Av. vaēn- 'to see' (vaēnaiti, auuaēnata) is a denominative of *wai(H)na- 'watch, survey' (YAv. vaēna- 'nose'!), which Cheung 2007 s.v. *uai(H)n takes back to PIE *uei(H₁)-no- (Pok. 1123, Lat. vēnārī), and which Gharib s.v. entry 10394 derives from *waina-, Av. vaēna-. It is the suppletive present partner of dī-, not a form of it. (d) 'upa-dīta : apparent' is not an attested Avestan word: Bartholomae and Pokorny print paiti-dīta- 'erblickt' with paiti-, and Nourai's *upa-dīta- comes from Horn's Grundriss no. 289 by way of Mo'in's footnote on پدید (BQT p.373) — Hübschmann, Persische Studien 38, deletes it outright, and the chart's own note records that. Hence plausible, not confirmed.\",\n \"derivation_fa\":\"از چهار صورتِ این گره دو تا درست است و دو تا نه. ۱) ریشهٔ اوستایی dā(y)- / dī- «دیدن» واقعی است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۲۴ به بعد) ستاکِ حالِ مضاعفِ ā-diδāiti «می‌نگرد» و اسم فاعلِ daiδyantō «بینندگان» را می‌آورد و پوکورنی نیز در ص ۲۴۳ همین صورت‌ها را نقل می‌کند؛ «dā 3» در کتاب نورایی همان dā- سومِ بارتولومه و «dây/dâi/dî» گونه‌های آواییِ همان ریشه است. ۲) daēman- «چشم، مردمکِ چشم؛ نگاه» نیز درست است (بارتولومه، ستون ۷۳۱) و همان است که در فارسی میانه dēm و در فارسی نو «دیم» شده است. ۳) اما «vaēna» به این ریشه ربطی ندارد: فعلِ اوستاییِ vaēn- «دیدن» از نامِ *wai(H)na- «دیده‌بانی، نگاهبان» ساخته شده (سنجید‌ه شود با vaēna- «بینی» در اوستای نو) و چونگ آن را به هندواروپاییِ *uei(H₁)-no- (پوکورنی ۱۱۲۳، لاتین vēnārī) می‌برد؛ این ستاک تنها همکارِ مکمّلِ ستاکِ گذشتهٔ dī- است نه صورتی از آن. ۴) «upa-dîta» هم واژهٔ اوستاییِ گواهی‌شده نیست؛ بارتولومه و پوکورنی صورتِ paiti-dīta- «دیده‌شده» را دارند، و *upa-dīta- از شمارهٔ ۲۸۹ گرامرِ هرن و از راهِ حاشیهٔ معین بر «پدید» (برهان قاطع ص ۳۷۳) به کتاب نورایی رسیده است؛ هوبشمان در «مطالعات فارسی» ص ۳۸ آن را صریحاً حذف می‌کند. پس ادعای این گره با احتیاط پذیرفتنی است.\",\n \"sources\":[W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"POK:243\",\"status\":\"supports\",\"note\":\"IEW 243 (POK_01.txt f-f page 254): 'av. dā(y)- ,sehen', z. B. ā-diδāiti ,betrachtet', daiδyantō Nom. Pl. Partiz. ,die sehenden' (usw., s. Bartholomae Airan. Wb. 724); Partiz. paiti-dīta- ,erblickt' … daēman- n. ,Auge, Augapfel; Blick''. Supports dā(y)-/dī- and daēman-; prints paiti-dīta-, not upa-dīta-, and does not list vaēna- here.\"},\n  {\"ref\":\"BQT:373\",\"status\":\"supports\",\"note\":\"Mo'in's footnote to پدید, BQT_v1_pages.txt leaf 597 (printed p.373): 'پدید … پهلوی pa dīt «نولدکه، کارنامه ۴۰»؛ قس اوستا upa-dīta …؛ آشکار، نمایان' — this is where Nourai's Avestan 'upa-dîta' comes from.\"},\n  {\"ref\":\"BQT:910\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 370 (printed ~910): the دید / دیده / دیده‌بان block, 'دیده … چشم را گویند … و بمعنی دیدن و مشاهده شده باشد'.\"},\n  {\"ref\":\"SOD:421\",\"status\":\"partial\",\"note\":\"Gharib, Sogdian Dictionary entry 10394 (SOD_pages.txt leaf 488, printed ~421-422): 'wyn- … wēn ⊙ <*waina-, Av. vaēna- ⊙ inf. -(ʾ)y ⇒wyt-'. The page is real and does carry the Sogdian verb, but Gharib derives it from *waina- / Av. vaēna-, i.e. from the other root, not from dī-.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. 731, s.v. daēman- (BRT.txt line 12457)\",\"stance\":\"supports\",\"note\":\"'j. daēman- n. 1) ‚Auge, Augapfel‘ … 2) ‚Blick‘' with Yt 10.48 and Yt 14.56 — Nourai's 'daěman : eye' verbatim.\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 831 f.\",\"stance\":\"partial\",\"note\":\"lists 'av. da(y)- „sehen“ … Ptc. paiti-dita- „erblickt“, -diti- f. „das Erblicken“ … daēman- n. „Auge, Augapfel; Blick“' — supports dā(y)- and daēman-, but again only paiti-dīta-.\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien 38, no. 289 (HUB.txt leaf 48)\",\"stance\":\"contradicts\",\"note\":\"'289. Streiche die Worte: „also aw. *upa-dīti-“ und vgl. oben Nr. 144. Das Wort padīd ‚sichtbar‘ ist erst im Mittelpers. componirt aus pa und dīt = ‚in Sicht‘' — Hübschmann strikes out the Avestan form Nourai prints.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *uai(H)n (CHEUNG.txt lines 26740-26805)\",\"stance\":\"contradicts\",\"note\":\"'This IIr. root is nominal in origin, from the noun *uai(H)na- “watch, survey(or)”, cf. Skt. vená- “watch”, YAv. vaēna- “nose” … «PIE *uei(H₁)-no- “survey” ⇒ LIV: 668 f. | Pok.: 1123»' — vaēn- is a different root from *daiH¹.\"}\n ]\n})\n\nN.append({\n \"id\":2, \"lang\":\"Pahlavi\", \"words\":\"dîtan; âděnak; pa-dît; děmân\",\n \"verdict\":\"plausible\",\n \"derivation\":\"MP dīdan 'to see' is exactly MacKenzie's 'dīdan, wēn- [HZYTWN-tn' < Aram. ḥzy; dytn', wyn- | M dydn, wyn-, N ~, bīn-]' (PHD p.26) — past stem dīd < OIr. *dita-, the regular ppp. of *daiH-, with intervocalic loss of the laryngeal and OIr. -i- lengthened to MP ī. 'ādēnak' is MP ādēnag / ēwēnag 'mirror' [ʾdynk'], for which Mo'in's footnote to آینه (BQT p.74) cites Parthian ʾdyng and Balochi ādēnk and, on Henning's oral authority, derives it from the root day- as 'the instrument in which one sees oneself' (*ā-daya-na-ka-); Cheung s.v. *daiH¹ lists it as '(+ *ā-) MMP ʾywyng “mirror” … NP āyīna'. 'pa-dīt' is MP pad dīd 'in sight' = NP padīd, and here Nourai follows Nöldeke and Mo'in; Cheung 1982-2007 shows the form is in fact Parthian, from *pati-diHtā-ka- > *paddyag > paydāg (whence MP pyt'k, pyd'g), NP padīd going back to the ppp. *pati-diHta-, so the segmentation 'pa + dīt' is the older, looser analysis of a form that is genuinely from this root. 'dēmān : appearance' is not in MacKenzie as a free word, but it is the second element of his handēmān 'before, in the presence of' (< 'face to face'), and Mo'in's footnote to دیم (BQT p.915) gives 'اوستا daēman-, پهلوی dēmān' — so the form is attested in the lexicographical tradition Nourai used, though its gloss is nearer 'face' than 'appearance'.\",\n \"derivation_fa\":\"«دیدن» فارسی میانه همان است که مکنزی می‌آورد: dīdan, wēn- [HZYTWN-tn'؛ dytn', wyn-]، یعنی ستاک گذشته dīd از ایرانی باستان *dita-، صفت مفعولی ریشهٔ *daiH-، با کشیدگیِ i به ī در فارسی میانه. «آدینک» همان ādēnag/ēwēnag «آینه» است؛ معین در حاشیهٔ «آینه» (برهان قاطع ص ۷۴) پارتی ʾdyng و بلوچی ādēnk را می‌آورد و به گفتهٔ شفاهی هنینگ آن را از ریشهٔ day- می‌گیرد، «آلتی که خود را در آن ببینند» (*ā-daya-na-ka-)؛ چونگ نیز آن را زیر *daiH¹ می‌آورد. «pa-dît» همان pad dīd «در دید» و برابرِ «پدید» فارسی است؛ اینجا نورایی از نولدکه و معین پیروی کرده است، ولی چونگ نشان می‌دهد که این صورت در اصل پارتی است و از *pati-diHta- «دیده‌شده» می‌آید، پس تجزیهٔ «pa + dīt» تحلیلِ کهنه‌تر و سست‌ترِ صورتی است که به‌هرحال از همین ریشه است. «dēmân» در فرهنگ مکنزی سرواژهٔ مستقل ندارد، اما جزء دومِ handēmān «در حضورِ، روبه‌رو» است و معین هم در حاشیهٔ «دیم» (برهان قاطع ص ۹۱۵) «اوستا daēman-، پهلوی dēmān» را می‌آورد؛ معنای دقیق‌ترش «رو، چهره» است نه «نمود». روی‌هم‌رفته گره پذیرفتنی است با همین اصلاح‌ها.\",\n \"sources\":[W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:74\",\"status\":\"supports\",\"note\":\"BQT_v1_pages.txt leaf 284 (printed p.74), Mo'in's footnote to آینه: 'پهلوی ādēnak … پارتی ādēnag ʾdyng … در بلوچی ādēnk … مشتق از ریشهٔ dai (پارسی باستان dī «ببین»، پارسی دیدن)، یعنی آلتی که خود را در آن ببینند، از افادات شفاهی استاد هنینگ' — exactly Nourai's 'âděnak : mirror' from this root.\"},\n  {\"ref\":\"BQT:373\",\"status\":\"supports\",\"note\":\"leaf 597 (printed p.373): 'پدید … پهلوی pa dīt «نولدکه، کارنامه ۴۰»' — Nourai's 'pa-dît' verbatim.\"},\n  {\"ref\":\"BQT:910\",\"status\":\"supports\",\"note\":\"leaf 370 (printed ~910): the دید/دیده entries which the chart's Persian node draws on.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary p.26 (PHD.txt line 99)\",\"stance\":\"supports\",\"note\":\"'dīdan, wēn- [HZYTWN-tn' < A ḥzy; dytn', wyn- | M dydn, wyn-, N ~, bīn-] see. ~išn: sight, seeing; ~išnīg: visible.' Also 'mirror ēwēnag' (English index line 2821) and 'handēmān [hndym'n'] before, in the presence of' (line 394).\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *daiH¹, Middle Persian section (CHEUNG.txt lines 4262-4290)\",\"stance\":\"partial\",\"note\":\"'MMP dyd, BMP dyt (HZYTWN-) /dīd/ (pret. stem) “to see” || (+ *(ā-)abi-) MMP ʾywyn, BMP ʾdwyn /ēwēn/ “manner, custom, form” || (+ *ā-) ? MMP ʾywyng “mirror?” || (+ *pati-) … /paydāg/' with the long note 'The NP form padīd no doubt derives from Parthian: ppp. *pati-diHta- “appeared, seen against”' — same root, but pati- not pa-, and Parthian mediation.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II, s.v. āivēnak (NYB_vol2_glossary.txt line 333)\",\"stance\":\"partial\",\"note\":\"'āivēnak [ʾdwynk'] kind, sort, species, genus … MPrs ʾywyng … [MPrth ʾdyng, List 79, NP āinah “mirror” seems to go back to *ā-dayana-]' — confirms the mirror word from *ā-day-ana-.\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien 38, no. 289\",\"stance\":\"supports\",\"note\":\"'Das Wort padīd ‚sichtbar‘ ist erst im Mittelpers. componirt aus pa und dīt = ‚in Sicht‘' — the chart's own NOTE reports this correctly; Hübschmann is right that the compound is Middle Iranian, and Cheung refines it to Parthian *pati-diHta-.\"}\n ]\n})\n\nN.append({\n \"id\":3, \"lang\":\"Persian\", \"words\":\"dîdan «دیدن»; dîm, dîmeh «دیم، دیمه»\",\n \"verdict\":\"plausible\",\n \"derivation\":\"NP دیدن continues MP dīdan without change (past stem دید < *dita-); its present stem بین is suppletive and belongs to the other root (see node 6). The script_extra آینه ، پدید ، پدیدار ، پدیده are all correct members of the family: آینه < MP ādēnag (Mo'in, BQT p.74), پدید < *pati-dita- (Parthian, per Cheung), پدیدار / پدیده built on it in New Persian. The one flaw is the gloss of دیم / دیمه as 'light'. Borhān-e Qāṭeʿ p.915 defines دیم as 'روی و رخاره باشد و بعربی خد گویند' — 'face, cheek, Arab. khadd' — and Mo'in's footnote there gives 'اوستا daēman-, پهلوی dēmān, ارمنی dēm, کردی dēm (روی), گیلکی dīm, طبری dīm', which is precisely Pokorny's 'npers. dīm ,Gesicht, Wange''. The gloss 'light' comes from the NEXT Borhān entry, دیمه, which the dictionary glosses 'روشنی و ضیا بود — و غله‌ای را نیز گویند که با آب باران حاصل می‌شود — و بمعنی باران و شبنم هم آمده' (p.915-916), and it is that entry which carries the Zartosht-nāmeh verse quoted in the JSON. So دیم 'face' is from this root; دیمه 'brightness / rain-fed crop / rain' is a separate lexeme that Nourai has merged with it and whose gloss he has transferred to both.\",\n \"derivation_fa\":\"«دیدن» فارسی نو بی‌هیچ دگرگونی دنبالهٔ dīdan فارسی میانه است (ستاک گذشته «دید» از *dita-)؛ ستاک حالِ آن، «بین»، مکمّل (suppletive) است و به ریشهٔ دیگری می‌رسد (نگاه کنید به گرهٔ ۶). واژه‌های افزودهٔ نمودار — آینه، پدید، پدیدار، پدیده — همه به‌درستی از همین خانواده‌اند: «آینه» از ādēnag فارسی میانه (حاشیهٔ معین، برهان قاطع ص ۷۴)، «پدید» از *pati-dita- پارتی، و «پدیدار/پدیده» ساخته‌های فارسی نو بر همان. تنها ایراد، معنایی است که برای «دیم/دیمه» آمده. برهان قاطع در ص ۹۱۵ می‌نویسد: «دیم … روی و رخاره باشد و بعربی خد گویند»، و حاشیهٔ معین در همان‌جا «اوستا daēman-، پهلوی dēmān، ارمنی dēm، کردی dēm (روی)، گیلکی dīm، طبری dīm» را می‌آورد — درست همان که پوکورنی می‌گوید: «npers. dīm ،Gesicht, Wange‌‌‌‌». معنای «روشنی» از مدخل بعدیِ برهان، یعنی «دیمه»، آمده است («روشنی و ضیا بود — و غله‌ای را نیز گویند که با آب باران حاصل می‌شود — و بمعنی باران و شبنم هم آمده»، ص ۹۱۵–۹۱۶) و بیتِ زرتشت‌نامه هم شاهدِ همان مدخل است. پس «دیم» به معنی «رو» از این ریشه است، ولی «دیمه» واژه‌ای دیگر است و نورایی این دو را یکی گرفته و معنای دومی را به هر دو داده است. ادعای گره با این اصلاح پذیرفتنی است.\",\n \"sources\":[W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:915\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaf 375 (printed ~915): 'دیم = بسکون ثانی بر وزن جیم. روی و رخاره باشد و بعربی خد گویند' with Mo'in's footnote 4 'اوستا daēman-، پهلوی dēmān، ارمنی dēm … کردی dēm (روی) … گیلکی dīm، طبری dīm'. Supports the etymology, contradicts the gloss 'light': دیم means 'face, cheek'. The gloss 'light' belongs to دیمه on the next page (leaf 376, printed ~916): 'روشنی و ضیا بود…'.\"},\n  {\"ref\":\"BQT:74\",\"status\":\"supports\",\"note\":\"leaf 284 (printed p.74): آینه with Mo'in's Henning-derived note (see node 2) — covers the script_extra آینه.\"},\n  {\"ref\":\"BQT:910\",\"status\":\"supports\",\"note\":\"leaf 370 (printed ~910): 'دیده … چشم را گویند … و بمعنی دیدن و مشاهده شده باشد' plus دیده‌بان etc.\"}\n ],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"IEW 243\",\"stance\":\"partial\",\"note\":\"'npers. dīdan ,sehen', dīm ,Gesicht, Wange'' — Pokorny knows dīm only as 'face, cheek', never as 'light'.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss no. 289 and no. 545 region (HRN.txt leaf 86 ff.)\",\"stance\":\"supports\",\"note\":\"Horn no. 289 'pedīd ‚sichtbar‘ — phlv. pa dīt … also aw. *upa-dīti-' is the source of the چart's پدید chain; Horn's Persian material for dīdan/dīm is what Pokorny quotes.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.26\",\"stance\":\"supports\",\"note\":\"'dīdan, wēn- … N ~, bīn-' — the New Persian outcome is given by MacKenzie himself.\"}\n ]\n})\n\nN.append({\n \"id\":4, \"lang\":\"Old Persian\", \"words\":\"dî, dây, wai, vâe; vâe-na, vaina; vainâhiy; věn-am, vaenâmi; adhi-vaina\",\n \"verdict\":\"disputed\",\n \"derivation\":\"This node fuses two different Indo-European roots and adds one form that does not exist. Only 'dī' is Old Persian for 'see' from *daiH-: Kent, Old Persian, Lexicon p.191a has exactly one form, the imperative didiy <di-i-di-i-y> (DNa 41, DNb 57), and Cheung s.v. *daiH¹ cites it as '*OLD PERSIAN: di- “to see” ⇒ Kent: 191a'. So Nourai's KNT:191 is the right page — but only for that one word. All the vain- forms (vainatiy, vaināhiy, vaināmiy 'I see', avaina 'he saw') stand on Kent p.206a, and Kent derives them elsewhere: §130 and §211, 'pIE *ueid-ne-, OP vaināmiy “I see”, Av. 3d sg. vaēnaiti; cf. the same root with nasal infix in Skt. vindáti', and again 'pIE *ueid-ne-/-no- in OP vaināmiy “I see” … Skt. vénāmi “I desire”, vénati'. Cheung reconstructs *uai(H)n from PIE *uei(H₁)-no- 'survey' (Pok. 1123, Lat. vēnārī); Wiktionary s.v. دیدن says the present stem 'is from Middle Persian wēn-, … ultimately from Proto-Indo-European *weyd-'. Whichever of the two is right, it is not *dheyh₂-. Nourai's own reference Abolghasemi, Fe'lhā-ye Fārsi-ye Darī p.55 (FFD:55, cited on this very node) states it flatly: 'بین < فارسی میانه wēn < ایرانی باستان *waina- … ریشهٔ wai به معنی «دیدن» است. «دیدن» و «بین» چون «آمدن» و «آی» دو ریشه‌ای است' — 'dīdan and bīn, like āmadan and āy, are bi-radical.' Finally 'adhi-vaina : ornament' is no Old Persian word at all: nothing of the kind occurs in Kent's lexicon or texts; it is Nourai's back-formation from the Book-Pahlavi spelling ʾdwyn' of ēwēn (node 5), whose ʾd- is the historical spelling of *abi-day-, not of *adhi-vain-.\",\n \"derivation_fa\":\"این گره دو ریشهٔ جدا را در هم آمیخته و یک صورتِ ناموجود هم افزوده است. تنها «dī» فارسی باستان از ریشهٔ *daiH- است: کنت در واژه‌نامهٔ «فارسی باستان» ص ۱۹۱a تنها یک صورت دارد، فعل امر didiy (DNa ۴۱، DNb ۵۷)، و چونگ نیز همان را زیر *daiH¹ می‌آورد و به «Kent: 191a» ارجاع می‌دهد؛ پس ارجاع KNT:191 درست است، اما فقط برای همین یک واژه. همهٔ صورت‌های vain- (vainatiy، vaināhiy، vaināmiy «می‌بینم»، avaina «دید») در ص ۲۰۶a کنت است و کنت آن‌ها را از ریشهٔ دیگری می‌گیرد: «هندواروپاییِ *ueid-ne-، فارسی باستان vaināmiy «می‌بینم»، اوستایی vaēnaiti؛ سنجیده شود با سنسکریت vindáti». چونگ *uai(H)n را از *uei(H₁)-no- «دیده‌بانی» (پوکورنی ۱۱۲۳، لاتین vēnārī) می‌داند و ویکی‌واژه ستاکِ حالِ «بین» را به *weyd- می‌رساند. هر کدام درست باشد، از *dheyh₂- نیست. خودِ مأخذی که نورایی برای همین گره آورده — ابوالقاسمی، «ماده‌های فعل‌های فارسی دری» ص ۵۵ — به‌صراحت می‌نویسد: «بین < فارسی میانه wēn < ایرانی باستان *waina- … ریشهٔ wai به معنی «دیدن» است. «دیدن» و «بین» چون «آمدن» و «آی» دو ریشه‌ای است.» سرانجام «adhi-vaina» اصلاً واژهٔ فارسی باستان نیست و در واژه‌نامه و متونِ کنت نشانی از آن نیست؛ این صورت را نورایی از املای پهلویِ کتابیِ ʾdwyn' (گرهٔ ۵) بازسازی کرده، حال آنکه ʾd- در آن املا بازماندهٔ *abi-day- است نه *adhi-vain-. بنابراین پژوهش امروزی این گره را رد می‌کند.\",\n \"sources\":[W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"KNT:191\",\"status\":\"partial\",\"note\":\"Kent's Lexicon p.191a is the entry dī- 'to see' (imperative didiy), which Cheung cites as '*OLD PERSIAN: di- “to see” ⇒ Kent: 191a'. It supports 'dî' only. The vain- forms are on Kent p.206a, and Kent's grammar (KNT.txt lines 1122, 2430) derives them from 'pIE *ueid-ne-', not from dheiə-.\"},\n  {\"ref\":\"FFD:55\",\"status\":\"contradicts\",\"note\":\"Abolghasemi, ماده‌های فعل‌های فارسی دری p.55 (FFD_pages.txt leaf 59): 'بین < فارسی میانه wēn < ایرانی باستان *waina- … ریشهٔ wai به معنی «دیدن» است. «دیدن» و «بین» چون «آمدن» و «آی» دو ریشه‌ای است' — Nourai's own source says dīdan and bīn are two distinct roots.\"},\n  {\"ref\":\"AEF:322\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Persian version of Horn (Asās-e Eshteqāq-e Fārsi) is not digitised anywhere (refs_online.json: 'Not online'); the German original Horn was checked instead (see consulted).\"}\n ],\n \"consulted\":[\n  {\"src\":\"KNT\",\"where\":\"Kent, Old Persian §130 and §211 (KNT.txt lines 1122, 2430)\",\"stance\":\"contradicts\",\"note\":\"'pIE -d-n- became pIr. -n- …, as in pIE *ueid-ne-, OP vaināmiy “I see”, Av. 3d sg. vaēnaiti; cf. the same root with nasal infix … in Skt. vindáti “he finds”' and 'pIE *ueid-ne-/-no- in OP vainamiy “I see”, 3d sg. vainatiy, mid. vainataiy; Skt. vénāmi “I desire”, vénati, vénate.'\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *uai(H)n, Old Persian section (CHEUNG.txt line ~26754)\",\"stance\":\"contradicts\",\"note\":\"'*OLD PERSIAN: vain- “to see” ⇒ Kent: 206a … «PIE *uei(H₁)-no- “survey” ⇒ LIV: 668 f. | Pok.: 1123» *IE COGNATES: Lat. venari “to chase, hunt”.' A different root and a different Pokorny page.\"},\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. s.v. vaēn- (BRT.txt line 7945 region)\",\"stance\":\"partial\",\"note\":\"Bartholomae files vaēn- (vaēnaiti, avaēnata) as its own verb, separate from his dā(y)- 'sehen' at col. 724 — the two are not one entry in the standard Avestan dictionary either.\"},\n  {\"src\":\"TLM\",\"where\":\"Tolman, Ancient Persian Lexicon (grep 'adivaina', 'adhi-vaina' in TLM.txt)\",\"stance\":\"silent\",\"note\":\"no such Old Persian form; the search returns nothing, as it does in Kent.\"}\n ]\n})\n\nN.append({\n \"id\":5, \"lang\":\"Pahlavi\", \"words\":\"věn-âk, věn-âg; adhvěnak\",\n \"verdict\":\"disputed\",\n \"derivation\":\"'wēnāg' is right and well attested: MacKenzie p.90 'wēnāg [wyn'k' | M wyn'g, N bīnā] seeing. ~īh: seeing, sight' — a -āg agent adjective on the present stem wēn- < OIr. *waina-, the direct ancestor of NP بینا; that half of the node is sound (though it descends from *wain-, not from this chart's root: see node 4). 'adhvēnak' is Nourai's reading of the Book-Pahlavi spelling ʾdwynk', i.e. ēwēnag, and here both the analysis and the gloss are wrong. MacKenzie p.30 reads it 'ēwēn [ʾdwyn' | M ʾywyn, (N āyīn)] manner, custom, form, propriety; pad ~: properly' and 'ēwēnag [ʾdwynk' | M ʾywyng] = ēwēn', with a second '*ēwēnag [ʾdwynk' | (N āyīna)] mirror'; Nyberg II p.24 gives 'āivēnak [ʾdwynk'] kind, sort, species, genus; nature; manner'. Neither dictionary knows a Pahlavi word 'ornament'. Etymologically the ʾd- of the spelling is the historical writing of *abi-day-, not of *adhi-vain-: Cheung files the word under *daiH¹ as '(+ *(ā-)abi-) MMP ʾywyn, BMP ʾdwyn /ēwēn/ “manner, custom, form”', with Parthian ʾbdyyn and the Armenian loan awrēn-kʿ 'institution, the Law' as witnesses. So the word is from the 'see' root of this chart, but through *abi-daya-na-, and it means 'manner, custom', not 'ornament'; the parent drawn (OP vain-) is the wrong one.\",\n \"derivation_fa\":\"«wēnāg» درست است و گواهی محکم دارد: مکنزی (ص ۹۰) می‌آورد «wēnāg [wyn'k' | فارسی نو bīnā] بیننده؛ wēnāgīh دیدن، بینایی» — صفتِ فاعلیِ -āg بر ستاکِ حالِ wēn- از ایرانی باستان *waina-، که نیای مستقیمِ «بینا»ی فارسی است؛ این نیمهٔ گره درست است (اما از ریشهٔ *wain- می‌آید نه از ریشهٔ این نمودار؛ نگاه کنید به گرهٔ ۴). اما «adhvěnak» خوانشِ نورایی از املای پهلویِ کتابیِ ʾdwynk' یعنی ēwēnag است و در اینجا هم تجزیه و هم معنا نادرست است. مکنزی (ص ۳۰) آن را چنین می‌خواند: «ēwēn [ʾdwyn' | فارسی نو آیین] شیوه، رسم، صورت، شایستگی» و «ēwēnag = ēwēn»، و صورتِ دیگرِ «*ēwēnag [ʾdwynk' | فارسی نو آیینه] آینه»؛ نیبرگ نیز (جلد ۲ ص ۲۴) «āivēnak [ʾdwynk'] گونه، سنخ، جنس؛ سرشت؛ شیوه» می‌آورد. هیچ‌کدام واژه‌ای پهلوی به معنی «زیور» نمی‌شناسند. از نظر ریشه‌شناسی ʾd- در این املا بازماندهٔ *abi-day- است نه *adhi-vain-؛ چونگ این واژه را زیر *daiH¹ می‌آورد: «(+ *(ā-)abi-) ʾywyn / ʾdwyn ‏/ēwēn/ «شیوه، رسم، صورت»» با گواهیِ پارتیِ ʾbdyyn و وام‌واژهٔ ارمنیِ awrēn-kʿ «نهاد، قانون». پس این واژه به‌راستی از همین ریشهٔ «دیدن» است، اما از راهِ *abi-daya-na-، و معنایش «شیوه و رسم» است نه «زیور»؛ و پدری که نمودار برایش کشیده (vain- فارسی باستان) نادرست است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"BQT:340\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 561 (printed ~340-341) is the بینا / بینایی / بیننده block: 'بینایی … بمعنی دیده‌وری و بینندگی باشد', 'بیننده … بمعنی شخص بینا و صاحب وقوف'. It documents the Persian outcome of wēnāg, but the OCR of Mo'in's footnote on that page is too damaged to read a Pahlavi form, and nothing there speaks of 'ornament'.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie pp.30 and 90 (PHD.txt lines 323 and 649)\",\"stance\":\"partial\",\"note\":\"'ēwēn [ʾdwyn' | M ʾywyn, (N āyīn)] manner, custom, form, propriety. pad ~: properly. ēwēnag [ʾdwynk' | M ʾywyng] = ēwēn; *ēwēnag [ʾdwynk' | (N āyīna)] mirror' and 'wēnāg [wyn'k' | M wyn'g, N bīnā] seeing. ~īh: seeing, sight'. Supports wēnāg → bīnā; contradicts the gloss 'ornament' for ʾdwynk'.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II p.24, s.v. āivēnak (NYB_vol2_glossary.txt line 333)\",\"stance\":\"contradicts\",\"note\":\"'āivēnak [ʾdwynk'] kind, sort, species, genus …; nature; manner … MPrs ʾywyng … [MPrth ʾdyng …, NP āinah “mirror” seems to go back to *ā-dayana-]' — 'manner/kind', never 'ornament', and the etymon is *ā-dayana-.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *daiH¹, MP and Parthian sections\",\"stance\":\"contradicts\",\"note\":\"files ēwēn under *daiH¹ as '(+ *(ā-)abi-)', i.e. *abi-daya-na-, and lists Parthian 'ʾbdyyn, ʾbdyn “custom(ary), habit; manner, way”' and 'Arm. (LW) awrēn-kʿ “institution, the Law”' — no vain- element anywhere.\"}\n ]\n})\n\nN.append({\n \"id\":6, \"lang\":\"Persian\", \"words\":\"bînâ «بینا ( بینش )»; âzîn «آذین»; âîn «آیین ( هر آیینه )»; âdîneh «آدینه»\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Four words, three verdicts. (1) بینا < MP wēnāg is beyond doubt (MacKenzie 'wēnāg … N bīnā'), and بینش، بین، دوربین، ذره‌بین are its regular New Persian relatives; but all of them belong to *wain-, not to the root of this chart (node 4). (2) آیین < MP ēwēn is also certain (MacKenzie 'ēwēn … (N āyīn) manner, custom'), and Cheung derives it from *(ā-)abi-daiH¹ with the note 'NP āyīn “rite, custom; common law; mode, form, manner” (initial long ā- points to *ā-abi-daiH¹?)' — so āyīn is genuinely from the 'see' root, but through *abi-day-, and its gloss 'ceremony, customs' is right. (3) آذین 'ornament': the chart's own NOTE reports that Henning, Sogdica p.17-18, connects it with a verb 'to sew', and that note is faithful — Henning writes 'MPers. ʾzyn- “to sew, tailor” is frequently met with in Mir…; cf. Horn, Gr. Ir. Phil., āzīn-: āzīdan “to sew”'. Mo'in's own footnote in Borhān (s.v. آذین) instead glosses it 'برابر دیدن'. Modern scholarship has no settled answer, but no standard dictionary derives آذین from an Old Persian *adhi-vaina 'ornament', which does not exist. (4) آدینه 'Friday' is the clearest error: Nyberg (Manual of Pahlavi II, s.v. āivēnak) states explicitly that 'NP ādīnah “Friday” … cannot be etymologically connected with āivēnak, as Markwart has it; it probably goes back to MIr. *ātēnak < OIr. *ati-ayana- (OP ati-ay- “to go along”) … *ādēnag “congregation”'. Wiktionary likewise takes ādīne from MP ʾdynk' /ādēnag/, with Sogdian āδēnē and Khwarezmian āδēnek 'Friday', the sense being 'appointed gathering', never 'day of ornaments'. Because the whole node hangs from the wrong parent and two of its four words are wrongly derived, the node is disputed.\",\n \"derivation_fa\":\"چهار واژه و سه حکم. ۱) «بینا» از wēnāg فارسی میانه بی‌گمان درست است (مکنزی: «wēnāg … فارسی نو bīnā») و «بینش، بین، دوربین، ذره‌بین» هم هم‌خانواده‌های قاعده‌مندِ آن‌اند؛ اما همهٔ این‌ها از ریشهٔ *wain- می‌آیند نه از ریشهٔ این نمودار (نگاه کنید به گرهٔ ۴). ۲) «آیین» از ēwēn فارسی میانه نیز قطعی است (مکنزی: «ēwēn … فارسی نو آیین، شیوه و رسم») و چونگ آن را از *(ā-)abi-daiH¹ می‌گیرد و می‌نویسد «آ»ی کشیدهٔ آغازین به *ā-abi-daiH¹ اشاره دارد؛ پس «آیین» به‌راستی از ریشهٔ «دیدن» است، اما از راهِ *abi-day-، و معنایی که نمودار داده («رسم و آیین») درست است. ۳) «آذین» به معنی «زیور»: یادداشتِ خودِ نمودار می‌گوید هنینگ در Sogdica ص ۱۷–۱۸ آن را با فعلِ «دوختن» می‌سنجد و این نقل درست است — هنینگ می‌نویسد «ʾzyn- فارسی میانه «دوختن، خیاطی کردن» در متون مانوی بسیار می‌آید؛ سنجیده شود با هرن، āzīn-: āzīdan «دوختن»». در برابر، حاشیهٔ معین بر «آذین» در برهان قاطع آن را «برابر دیدن» می‌داند. پژوهش امروزی در این واژه به نتیجهٔ قطعی نرسیده است، ولی هیچ فرهنگِ معتبری «آذین» را از *adhi-vaina «زیور» فارسی باستان — که اصلاً وجود ندارد — نمی‌گیرد. ۴) «آدینه» آشکارترین خطاست: نیبرگ در ذیل āivēnak صریحاً می‌نویسد که «آدینه» را نمی‌توان به āivēnak پیوند داد (چنانکه مارکوارت کرده) و آن را از *ati-ayana- ایرانی باستان (فارسی باستان ati-ay- «پیش رفتن») به معنی «گردهم‌آیی» می‌داند؛ ویکی‌واژه هم آن را از ādēnag فارسی میانه با هم‌ریشه‌های سغدیِ āδēnē و خوارزمیِ āδēnek «آدینه» می‌گیرد، با مفهومِ «هنگامِ گردآمدن»، نه «روزِ آذین». چون کلِ گره از پدرِ نادرست آویخته و دو واژه از چهار واژه‌اش نادرست ریشه‌یابی شده، حکمِ گره «رد شده» است.\",\n \"sources\":[W+\"%D8%A2%D8%AF%DB%8C%D9%86%D9%87\", W+\"%D8%A2%D8%A6%DB%8C%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:29\",\"status\":\"partial\",\"note\":\"BQT_v1_pages.txt leaf 237 (printed p.27-29 region; the vol.1 leaf→page offset drifts by ±2 here) carries the آذین entry: 'آذین … بمعنی آیین است که زیب و زینت و آرایش — و رسم و قاعده و قانون باشد — و بمعنی آلتی که روغن را از دوغ جدا می‌کند هم هست', with Mo'in's footnote pointing to 'برابر دیدن'. It supports the sense 'ornament/rite' and a link to 'seeing', but not an Old Persian *adhi-vaina.\"},\n  {\"ref\":\"BQT:340\",\"status\":\"partial\",\"note\":\"leaf 561 (printed ~340): بینا / بینایی / بیننده — supports بینا only.\"},\n  {\"ref\":\"SNS:291\",\"status\":\"not_found\",\"note\":\"grepped SNS.txt / SNS_pages.txt (Tavoosi's Shāyast nē Shāyast glossary) for 'ēwēn', 'āivēnak', 'wēnāk', 'ādēn': no hit; the OCR of this scan is very poor and the printed page numbers are not readable, so the cited page could not be located.\"},\n  {\"ref\":\"AEF:80\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Asās-e Eshteqāq-e Fārsi is not digitised (refs_online.json); Horn's German original was consulted instead.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie pp.30, 90\",\"stance\":\"partial\",\"note\":\"'ēwēn … (N āyīn) manner, custom, form, propriety' and 'wēnāg … N bīnā' — supports bīnā and āyīn, gives no 'ornament' sense and no ādīne.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg II p.24 s.v. āivēnak (NYB_vol2_glossary.txt line 333)\",\"stance\":\"contradicts\",\"note\":\"'Note: — NP ādīnah “Friday”, for Islamic (yaumu-)l-jumʿa, cannot be etymologically connected with āivēnak, as Markwart has it; it probably goes back to MIr *ātēnak < OIr *ati-ayana- (OP ati-ay- “to go along”), cf MPrs ʾdyn “entrance”, with secondary lengthening of the initial a-: *ādēnag “congregation”.'\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *daiH¹, NWIr. section\",\"stance\":\"partial\",\"note\":\"'(+ *(ā-)abi-) NP āyīn “rite, custom; common law; mode, form, manner” (initial long ā- points to *ā-abi-daiH¹?) || (+ *ā-) NP āyīna, Bal. adēn(k) “mirror”' — āyīn belongs to the see-root, but via *abi-day-; āzīn and ādīne are absent.\"},\n  {\"src\":\"HENNING\",\"where\":\"Sogdica pp.17-18 (HENNING_selected_papers.txt lines 846-854)\",\"stance\":\"partial\",\"note\":\"'MPers. “ʾzyn-” “to sew, tailor” is frequently met with in Mir[anian]… Cf. ZII, ix, p.214; Horn, Gr. Ir. Phil., āzīn-: āzīdan “to sew”' — the source behind the chart's own NOTE (SOG:17); Henning is talking about a verb 'to sew', not about vain-.\"}\n ]\n})\n\nN.append({\n \"id\":7, \"lang\":\"Sanskrit\", \"words\":\"dhi; dhyânah\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Both words are the classic Indic members of the root. Skt. dhī́- f. (acc. dhíyam) is the zero-grade noun 'thought, perception, insight, religious meditation' (RV+), and dhyā́na- n. 'meditation' is the -na- verbal noun of dhyā́yati '(he) sees in the mind, thinks', a jo-present built on the full-grade variant *dhyā- (< *dhi̯eh₂-). Pokorny 243 and Walde-Pokorny I 831 print exactly this set (dhyāti / dhyāyati, dhyā́na-, dhyāman-, dhī́ḥ, dhī́ti-, dhī́ra- 'sehend, klug'), and Watkins/AHD give 'Sanskrit dhyāti, he meditates (< “he observes mentally”)'. The semantic bridge 'see' → 'see mentally' → 'meditate' is the same one that produces Av. daēnā 'insight, religion' in node 13; the Buddhist term dhyāna is the ancestor of Pali jhāna, Chinese chán and Japanese zen.\",\n \"derivation_fa\":\"هر دو واژه نمایندگانِ کلاسیکِ این ریشه در هندی‌اند. dhī́- (رایی dhíyam) نامِ درجهٔ صفر است به معنی «اندیشه، دریافت، بینش، تأملِ دینی» (از ریگ‌ودا به بعد)، و dhyā́na- نامِ مصدریِ -na- از dhyā́yati «در اندیشه می‌بیند، می‌اندیشد» است، ستاکِ حالِ jo- بر گونهٔ درجهٔ کاملِ *dhyā- (< *dhi̯eh₂-). پوکورنی (ص ۲۴۳) و والده-پوکورنی (جلد ۱ ص ۸۳۱) دقیقاً همین مجموعه را می‌آورند (dhyāti/dhyāyati، dhyā́na-، dhyāman-، dhī́ḥ، dhī́ti-، dhī́ra- «بینا، هوشمند»)، و واتکینز نیز «سنسکریت dhyāti «می‌اندیشد» (< «در ذهن می‌نگرد»)» را ثبت کرده است. همان پلِ معناییِ «دیدن ← در ذهن دیدن ← اندیشیدن» در اوستایی daēnā «بینش، دین» (گرهٔ ۱۳) هم دیده می‌شود. اصطلاح بودایی dhyāna نیایِ jhāna پالی و chán چینی و zen ژاپنی است. ادعای نورایی درست است.\",\n \"sources\":[W+\"%CF%83%E1%BF%86%CE%BC%CE%B1\"],\n \"ref_check\":[\n  {\"ref\":\"POK:243\",\"status\":\"supports\",\"note\":\"IEW 243 (POK_01.txt f-f page 253 end/254): 'Ai. dīdheti ,er schaute'… dhyā-ti, dhyā-ya-ti (jo-Präs.) ,schaut im Geiste, d. i. denkt, sinnt', Partiz. dhyā-ta- und dhi-tā-, dhyā ,das Denken, Sinnen', dhyā-tar- ,Denker', dhyā-na- ,das Sinnen, Nachdenken', dhyāman- n. ,Gedanke'; dhī-ḥ, Akk. dhiyam ,Gedanke, Vorstellung, Einsicht, Verstand, religiöses Nachdenken, Andacht''.\"}\n ],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 831 (WLD_Bd1 djvu lines 52380-52395)\",\"stance\":\"supports\",\"note\":\"the same Sanskrit paragraph verbatim, adding 'dhīra- „sehend, klug, weise, geschickt“' and 'prakr. herai „sieht“'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. dheiə- (AHD_watkins1985.txt line 377)\",\"stance\":\"supports\",\"note\":\"'b. Sanskrit dhyāti, he meditates (< “he observes mentally”): ZEN BUDDHISM.'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein, s.v. semantics (KLN_1971.txt line 217408)\",\"stance\":\"supports\",\"note\":\"Gk. sêma 'is cogn. with OI. dhīḥ, dhyānaḥ, “thought”, dhyāti, dhyāyati, “thinks”. See dhyana' — Klein even carries dhyana as an English headword.\"}\n ]\n})\n\nN.append({\n \"id\":8, \"lang\":\"Pahlavi\", \"words\":\"gyân, jân\",\n \"verdict\":\"disputed\",\n \"derivation\":\"The Pahlavi word is real — MP gyān [gyʾn], NP jān 'soul, life' (MacKenzie's index has gyān for 'ghost (soul)', gyānwar 'animal', gyānīg 'spiritual') — but neither its parent nor its route is right. First, a Middle Persian word cannot descend from Sanskrit; at best Nourai means 'from the same Indo-Iranian etymon as Skt. dhyāna-'. That equation is Hübschmann's, Persische Studien 49 no.413 ('Zd. daēnā- kann nicht gleichzeitig = np. jān und = np. dīn sein. Ich setze jān ‚Seele‘ = skr. dhyāna- ‚Nachsinnen‘'), and Nourai cites exactly HUB:49 on the daughter node, so he is following the 1895 view. Modern scholarship rejects it. MP gyān goes back to Proto-Iranian *wyaHnáH = *wi- + *HanH- 'to breathe' (PIE *h₂enh₁- 'to breathe'), with Avestan viiānaiiā and Sanskrit vyāná- 'the breath that circulates in the body' as direct cognates and Latin animus as the semantic parallel; the initial *wy- gives MP gy- regularly (as in *wyāxman > gyāxman), whence NP j- by the ordinary MP gy- > NP j- change (cf. MP gyāg > NP jāy). Skt. dhyāna- would have given MP *dyān/*zyān, never gyān. Verdict: disputed.\",\n \"derivation_fa\":\"واژهٔ پهلوی درست است — gyān [gyʾn] «جان، روان»، که در فارسی نو «جان» شده (مکنزی: gyān، gyānwar «جانور»، gyānīg «جانی، روحانی») — اما نه پدرش درست است و نه راهش. نخست آنکه واژه‌ای فارسی میانه نمی‌تواند از سنسکریت «فرود آید»؛ در بهترین حالت مقصود نورایی این است که هر دو از یک صورتِ هندوایرانی‌اند. این برابرنهاد از آنِ هوبشمان است در «مطالعات فارسی» ص ۴۹ شمارهٔ ۴۱۳: «daēnā- اوستایی نمی‌تواند هم‌زمان برابرِ «جان» و برابرِ «دین» فارسی باشد؛ من «جان» را برابرِ dhyāna- سنسکریت «اندیشیدن» می‌گذارم» — و نورایی هم دقیقاً همین HUB:49 را در گرهٔ فرزند آورده، پس پیروِ دیدگاهِ ۱۸۹۵ است. پژوهش امروزی این را رد می‌کند: gyān فارسی میانه از ایرانیِ آغازینِ *wyaHnáH یعنی *wi- + *HanH- «دمیدن، نفس کشیدن» (هندواروپایی *h₂enh₁-) می‌آید، با هم‌ریشه‌های مستقیمِ اوستاییِ viiānaiiā و سنسکریتِ vyāná- «دمی که در تن می‌گردد» و همتای معناییِ لاتینِ animus؛ *wy- آغازین در فارسی میانه قاعده‌مند به gy- بدل می‌شود و gy- فارسی میانه در فارسی نو به «ج» (چنانکه gyāg > «جای»). اگر واژه از dhyāna- سنسکریت می‌آمد در فارسی میانه *dyān یا *zyān می‌شد نه gyān. پس ریشه‌شناسی این گره رد می‌شود.\",\n \"sources\":[W+\"%D8%AC%D8%A7%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:558\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaves 16-18 (printed ~556-558) carry جان and its compounds (جاندارو، جانور، جان‌گزا، جانوسار…). Mo'in's footnote on the جان page notes that Justi and Fr. Müller connected جان with Avestan gaya- 'to live' and remarks that Horn's derivation has been rejected ('وجه اشتقاق هرن را مردود دانسته‌اند'), citing Hübschmann. So Borhān documents the word and the controversy but does not support a Sanskrit dhyāna- origin.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, English index (PHD.txt lines 792, 793, 2098, 3774)\",\"stance\":\"partial\",\"note\":\"'ghost (soul) gyān, uštān; give up the ~ gyān kandan', 'animal gyānwar', 'spiritual gyānīg' — the Pahlavi word is gyān, with initial gy-, which a Sanskrit dhy- cannot yield.\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien 49, no. 413 (HUB.txt leaf 59)\",\"stance\":\"supports\",\"note\":\"'413. Zd. daēnā- kann nicht gleichzeitig = np. jān und = np. dīn (Nr. 597) sein. Ich setze jān ‚Seele‘ = skr. dhyāna- ‚Nachsinnen‘. Justi und Fr. Müller verknüpfen jān mit zd. gaya- ‚Leben‘, was lautlich unzulässig ist.' This is Nourai's source — it says precisely what the chart draws, and it is the view modern work has abandoned.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss no. 413, p.93 (HRN.txt leaf 114)\",\"stance\":\"partial\",\"note\":\"'413. jān ‚Leben, Seele‘, jānvar. aw. daēnā ‚Seele‘, zu √dhay-, dhyā- (oder nach Bartholomae, ZDMG. 43, 665 dhai-) ‚sehen‘ im geistigen Sinn…; phlv. jān, jānvar.' The chart's NOTE (HRN:93) is a faithful report: Horn does route jān through daēnā and the 'see' root — but through Avestan, not Sanskrit, and Hübschmann rejected it a year later.\"}\n ]\n})\n\nN.append({\n \"id\":9, \"lang\":\"Persian\", \"words\":\"jân «جان ( جانور )»\",\n \"verdict\":\"disputed\",\n \"derivation\":\"NP جان continues MP gyān directly: MP gy- > NP j- (cf. gyāg > جای, gyāwar/gyānwar > جانور), so the form-history within Iranian is uncontroversial and 'جانور' is gyānwar 'possessing a soul, animal'. What is disputed is the deeper origin, which the node inherits from its parent: Nourai's route (Skt. dhyāna- 'meditation' > MP gyān 'soul') is Hübschmann's 1895 conjecture, cited by Nourai himself as HUB:49; today جان is derived from Proto-Iranian *wyaHnáH < *wi-HanH- 'to breathe out/around' (Av. viiānaiiā, Skt. vyāná- 'circulating breath'), i.e. 'breath' > 'life' > 'soul', matching Lat. anima/animus, Gk. psūkhē 'breath, soul', and matching the Kurdish cognates giyān/gyan, which preserve the initial gy- that a dhy- etymon cannot explain. The chart's own NOTE, which cites Horn p.93 for a derivation from Av. dhay- 'to see', is a correct report of Horn but of a view that Hübschmann and later scholars set aside.\",\n \"derivation_fa\":\"«جان» فارسی نو مستقیماً دنبالهٔ gyān فارسی میانه است: gy- فارسی میانه در فارسی نو به «ج» بدل می‌شود (چنانکه gyāg > «جای» و gyānwar > «جانور»)، پس تاریخِ صوریِ واژه در درونِ ایرانی جای چون‌وچرا ندارد و «جانور» همان gyānwar «جان‌دار» است. آنچه محلِ اختلاف است ریشهٔ ژرف‌تر است که از گرهٔ پدر به این گره رسیده: راهی که نورایی می‌کشد (dhyāna- سنسکریت «اندیشه» ← gyān فارسی میانه «جان») همان حدسِ هوبشمان در ۱۸۹۵ است که خودِ نورایی هم به آن (HUB:49) ارجاع می‌دهد؛ امروز «جان» را از ایرانیِ آغازینِ *wyaHnáH < *wi-HanH- «دمیدن، نفس کشیدن» می‌گیرند (اوستایی viiānaiiā، سنسکریت vyáná- «دمِ گردنده در تن»)، یعنی «دم ← زندگی ← روان»، درست همانند anima/animus لاتین و psūkhē یونانی؛ هم‌ریشه‌های کردیِ giyān/gyan نیز همان gy- آغازین را نگاه داشته‌اند که از dhy- بیرون نمی‌آید. یادداشتِ خودِ نمودار که هرن ص ۹۳ را برای اشتقاق از dhay- اوستایی نقل می‌کند، نقلی درست از هرن است، اما از دیدگاهی که هوبشمان و پس از او دیگران کنار گذاشتند. پژوهش امروزی این ریشه‌شناسی را رد می‌کند.\",\n \"sources\":[W+\"%D8%AC%D8%A7%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"HUB:49\",\"status\":\"supports\",\"note\":\"Persische Studien 49, no.413: 'Ich setze jān ‚Seele‘ = skr. dhyāna- ‚Nachsinnen‘' — Nourai's citation is exact; the reference does say what the arrow says. It is simply superseded.\"},\n  {\"ref\":\"BQT:558\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt leaves 16-18 (printed ~556-558): the جان block with Mo'in's footnote reporting Justi's and Müller's Av. gaya- proposal and noting that Horn's derivation 'را مردود دانسته‌اند'. Documents the word, not the Sanskrit route.\"}\n ],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"Grundriss no.413, p.93\",\"stance\":\"partial\",\"note\":\"'aw. daēnā ‚Seele‘, zu √dhay-, dhyā- … ‚sehen‘ im geistigen Sinn … phlv. jān, jānvar' — the chart's NOTE is accurate about Horn.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, English index s.v. 'ghost (soul)', 'animal'\",\"stance\":\"partial\",\"note\":\"'gyān', 'gyānwar' — the Middle Persian antecedent of جان and جانور, with gy-.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"Etym. Dict. of the Iranian Verb (grep 'gyān', 'wyaHn')\",\"stance\":\"silent\",\"note\":\"Cheung's verb dictionary has no entry for this noun; his *daiH¹ article does not list gyān/jān among the reflexes of the 'see' root — a silence that is itself telling.\"}\n ]\n})\n\nN.append({\n \"id\":10, \"lang\":\"Avestan / Old Persian\", \"words\":\"dais; ham-dais-a\",\n \"verdict\":\"disputed\",\n \"derivation\":\"The forms are real, the parent is not. Av. daēs- 'to show' (daēsayeiti, disyeiti, ādisti- 'Anweisung, Lehre') belongs to PIE *deiḱ- 'to show, point out', Pokorny IEW 188, whose family is Skt. diśáti 'zeigt, weist', Gk. deíknumi, Lat. dīcere/dicāre, Goth. gateihan, Germ. zeihen. That root is phonologically incompatible with *dheyh₂-: it has a plain *d-, not an aspirate *dh-, and a palatal *ḱ that shows up as Av. s / Skt. ś, features the 'see' root simply does not have. Nourai's own reference for the node's Old Iranian shape, Abolghasemi FFD p.33, says the root outright: 'ریشهٔ daiš به معنی «نشان دادن» است' — 'the root daiš means “to show”'. The compound *ham-daiša- ('to think' < 'to put together in view, design') is likewise correct and is the etymon of node 11; the reference ☞Sem 1 for the prefix ham- (< PIE *sem- 'one, together') is right. So everything inside the node is sound, and only its attachment to Dheye is wrong.\",\n \"derivation_fa\":\"صورت‌ها درست‌اند، اما پدرشان نه. daēs- اوستایی «نشان دادن» (daēsayeiti، disyeiti، ādisti- «رهنمود، آموزه») از ریشهٔ هندواروپاییِ *deiḱ- «نشان دادن» است (پوکورنی ص ۱۸۸) که خانواده‌اش سنسکریت diśáti، یونانی deíknumi، لاتین dīcere و dicāre، گوتی gateihan و آلمانی zeihen است. این ریشه از نظر آوایی با *dheyh₂- سازگار نیست: نخستین واکِ آن d سادهٔ بی‌دمش است نه dh دمیده، و در پایان یک ḱ کامی دارد که در اوستایی s و در سنسکریت ś می‌شود — چیزی که ریشهٔ «دیدن» ندارد. خودِ مأخذی که نورایی برای صورتِ ایرانیِ باستانِ این گره آورده، یعنی ابوالقاسمی ص ۳۳، صریح می‌نویسد: «ریشهٔ daiš به معنی «نشان دادن» است.» ترکیبِ *ham-daiša- («اندیشیدن» از «در نظر گرد هم آوردن، طرح کردن») نیز درست است و نیایِ گرهٔ ۱۱ است؛ ارجاعِ ☞Sem 1 برای پیشوندِ ham- (از *sem- «یک، با هم») هم درست است. پس هرچه درونِ گره است درست است و تنها پیوندِ آن به ریشهٔ «Dheye» نادرست است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"POK:243\",\"status\":\"contradicts\",\"note\":\"IEW 243 (the dheiə- article) contains no daēs-/dais- at all. The forms stand instead in IEW 188 (POK_01.txt line 2716 ff.): 'deik- ,zeigen'… Ai. didesti, diśáti, deśayati ,zeigt, weist', av. daēs- Aor. dōiš- ,zeigen; jemandem etwas zuweisen'… av. ādišti-š ,Anweisung, Lehre'… gr. δείκνυμι… lat. dīcere ,sagen''. So Nourai's own POK page does not support this node.\"},\n  {\"ref\":\"KNT:191\",\"status\":\"not_found\",\"note\":\"Kent's Lexicon p.191a is dī- 'to see' (imperative didiy); no daiš-/dais- verb is entered for Old Persian at all in Kent's lexicon (the OP evidence for this root is the noun *diš- in personal names, not a verb).\"},\n  {\"ref\":\"FFD:33\",\"status\":\"supports\",\"note\":\"Abolghasemi p.33 (FFD_pages.txt leaf 37): 'اندیش ← فارسی میانه handēš ← ایرانی باستان *ham-daiš-a. … ham پیشوند فعلی است. ریشهٔ daiš به معنی «نشان دادن» است.' Supports the form and the analysis — and identifies the root as 'to show', not 'to see'.\"}\n ],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"IEW 188, s.v. deik- (POK_01.txt lines 2716-2736)\",\"stance\":\"contradicts\",\"note\":\"the Avestan daēs- material is filed under deik- 'zeigen', a separate root with plain *d- and palatal *-ḱ-.\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 776 f. (the deik- article, referenced at IEW 188 as 'WP. I 777')\",\"stance\":\"contradicts\",\"note\":\"Pokorny's cross-reference 'WP. I 777' at the head of the deik- entry places the Avestan daēs- forms in Walde-Pokorny's deik- article, not in the dheiə- article at I 831 f.\"},\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. s.v. daēs-/dis- (grep 'daēsayeiti', 'disyeiti')\",\"stance\":\"contradicts\",\"note\":\"Bartholomae files daēs- 'zeigen' as its own verb, wholly separate from dā(y)- 'sehen' (col. 724); Pokorny quotes him for both.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. deik-\",\"stance\":\"contradicts\",\"note\":\"Watkins keeps 'deik-. To show, pronounce solemnly' apart from 'dheiə-. To see, look' — two entries, two Pokorny pages (188 and 243).\"}\n ]\n})\n\nN.append({\n \"id\":11, \"lang\":\"Pahlavi\", \"words\":\"handěš\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"MP handēš- is the present stem of handēšīdan 'to think, consider, reflect': MacKenzie p.41 'handēšīdan, handēš- [hndyš-ytn' | M hndyš-, N an~] think, consider, reflect. ~išn: thought, reflection.' It continues Old Iranian *ham-daiša- exactly as Nourai's reference states: ham- 'together' + the present stem of daiš- 'to show'; *ham-dai̯š- > MP handēš- with the regular monophthongisation of OIr. -ai- to MP -ē- and the assimilation of *m before d to n. The semantic step 'set out together / design' → 'think over' is the same as in Latin cōgitāre (co-agitāre) and English con-sider. The only correction to make is the one already made at node 10: the ultimate root is *deiḱ-, not *dheyh₂-.\",\n \"derivation_fa\":\"handēš- ستاکِ حالِ فعلِ handēšīdan «اندیشیدن، سنجیدن» در فارسی میانه است؛ مکنزی (ص ۴۱) می‌آورد: «handēšīdan, handēš- [hndyš-ytn' | فارسی نو اندیشیدن] اندیشیدن، سنجیدن؛ handēšišn: اندیشه». این صورت دنبالهٔ *ham-daiša- ایرانی باستان است، درست همان‌گونه که مأخذِ نورایی می‌گوید: پیشوندِ ham- «با هم» + ستاکِ daiš- «نشان دادن»؛ *ham-dai̯š- > handēš- با تکْ‌واکه شدنِ قاعده‌مندِ -ai- ایرانیِ باستان به -ē- در فارسی میانه و همگونیِ *m پیش از d به n. تحولِ معناییِ «با هم نشان دادن، طرح افکندن ← اندیشیدن» همان است که در cōgitāre (co-agitāre) لاتین و consider انگلیسی می‌بینیم. تنها اصلاحی که باید کرد همان است که در گرهٔ ۱۰ گفته شد: ریشهٔ نهایی *deiḱ- است نه *dheyh₂-.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"FFD:33\",\"status\":\"supports\",\"note\":\"Abolghasemi p.33: 'اندیش ← فارسی میانه handēš ← ایرانی باستان *ham-daiš-a' — the Pahlavi form and its Old Iranian antecedent exactly as drawn.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary p.41 (PHD.txt line 394)\",\"stance\":\"supports\",\"note\":\"'handēšīdan, handēš- [hndyš-ytn' | M hndyš-, N an~] think, consider, reflect. ~išn: thought, reflection. handēšīdār [hndyšyt'l] thoughtful.'\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (grep 'handēš')\",\"stance\":\"silent\",\"note\":\"the Shāyast/Kārnāmag glossary Nyberg excerpts does not happen to contain the verb; no contradiction.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"Etym. Dict. of the Iranian Verb (grep 'handēš', 'daiš')\",\"stance\":\"silent\",\"note\":\"Cheung's *daiš article was not reachable in the local OCR under that spelling; his *daiH¹ entry, which is complete, does NOT list handēš among the reflexes — consistent with node 10's finding that handēš belongs to a different root.\"}\n ]\n})\n\nN.append({\n \"id\":12, \"lang\":\"Persian\", \"words\":\"andîšîdan «اندیشیدن»\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"NP اندیشیدن is MP handēšīdan with the regular New Persian loss of initial h- (han- > an-, as in handām > اندام, handarz > اندرز, hangām > هنگام beside anbāz < hambāz) and the MP ē preserved as Persian ī in اندیش-. The derivatives in the chart's extra field are all transparent New Persian formations on that stem: اندیشه (verbal noun in -a), اندیش (bare present stem, used as a compound member: نیک‌اندیش, دوراندیش), اندیشمند (with the possessive suffix -mand). The chain OIr. *ham-daiša- > MP handēš- > NP andīš- is the standard account and is what Nourai's reference FFD:33 gives; the caveat remains that the ultimate root is *deiḱ- 'to show' (Pokorny 188).\",\n \"derivation_fa\":\"«اندیشیدن» فارسی نو همان handēšīdan فارسی میانه است با افتادنِ قاعده‌مندِ h- آغازین (han- > an-، چنانکه handām > «اندام»، handarz > «اندرز»، hambāz > «انباز») و ماندگاریِ ē فارسی میانه به‌صورتِ «ی» در «اندیش-». واژه‌های افزودهٔ نمودار همه ساخته‌های شفافِ فارسی نو بر همین ستاک‌اند: «اندیشه» (اسمِ مصدر با پسوندِ -ه)، «اندیش» (ستاکِ حالِ برهنه، در ترکیب‌هایی مانند نیک‌اندیش و دوراندیش) و «اندیشمند» (با پسوندِ دارندگیِ -مند). زنجیرهٔ *ham-daiša- ایرانی باستان ← handēš- فارسی میانه ← «اندیش-» فارسی نو همان است که ابوالقاسمی (ص ۳۳) می‌آورد و در ریشه‌شناسیِ امروزی پذیرفته است؛ تنها یادآوری آنکه ریشهٔ نهایی *deiḱ- «نشان دادن» است (پوکورنی ۱۸۸).\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"FFD:33\",\"status\":\"supports\",\"note\":\"Abolghasemi p.33 is precisely an entry on the Persian verb اندیشیدن: 'اندیش + فارسی میانه handēš + ایرانی باستان *ham-daiš-a'.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.41\",\"stance\":\"supports\",\"note\":\"'handēšīdan, handēš- … N an~' — MacKenzie himself equates the Pahlavi verb with New Persian andēšīdan.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss (grep 'andēšīden', 'andīšīden' in HRN.txt)\",\"stance\":\"silent\",\"note\":\"the OCR of Horn's entry for this verb is too damaged to quote; no contradiction found.\"}\n ]\n})\n\nN.append({\n \"id\":13, \"lang\":\"Avestan\", \"words\":\"daěna\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Av. daēnā- is exactly as glossed: Bartholomae's dictionary carries two homonyms, ¹daēnā- f. 'Religion' (Y 44.11, Y 53.4 etc.) and ²daēnā- f. 'inneres Wesen, geistiges Ich, Individualität' (Y 31.11, Y 45.11), and Pokorny 243 and Walde-Pokorny I 831 f. list them together under the 'see' root as 'daēnā ‚Religion‘ und ‚inneres Wesen, geistiges Ich‘' — so Nourai's 'insight, religion' renders the pair accurately. Formally daēnā- is a -nā- abstract on the root day-/dī- (as Reichelt, Aw. Elementarbuch 448, argues, comparing Gk. eidōlon and German Gewissen for the semantics 'what one sees inwardly' > 'conscience, religion'). It is fair to note that Bartholomae himself printed 'Et.?' at the foot of the entry and was unconvinced by attempts to unite the two homonyms under dā(y)-, and that Jeffery repeats an old suggestion of an Elamite source; but the derivation from day- 'to see' is the one Pokorny, Walde-Pokorny and current handbooks give, so the box as drawn is confirmed.\",\n \"derivation_fa\":\"daēnā- اوستایی درست همان است که در نمودار آمده: بارتولومه دو هم‌آوا ثبت کرده است، ¹daēnā- «دین» (یسنا ۴۴٫۱۱، ۵۳٫۴ و …) و ²daēnā- «ذاتِ درونی، منِ معنوی، فردیت» (یسنا ۳۱٫۱۱، ۴۵٫۱۱)، و پوکورنی (ص ۲۴۳) و والده-پوکورنی (جلد ۱ ص ۸۳۱) هر دو را زیر ریشهٔ «دیدن» می‌آورند: «daēnā «دین» و «ذاتِ درونی، منِ معنوی»» — پس ترجمهٔ نورایی («بینش، دین») دقیق است. از نظر ساخت، daēnā- اسمِ معنایِ -nā- بر ریشهٔ day-/dī- است (چنانکه رایشلت در «کتابِ مقدماتیِ اوستایی» ص ۴۴۸ استدلال کرده و برای معنا با eidōlon یونانی و Gewissen آلمانی سنجیده است: «آنچه آدمی در درون می‌بیند» ← «وجدان، دین»). انصاف آن است که یادآوری شود بارتولومه خود در پایانِ مدخل «Et.?» گذاشته و کوششِ یکی‌کردنِ دو هم‌آوا زیرِ dā(y)- را نپذیرفته، و جفری هم پیشنهادِ کهنهٔ خاستگاهِ عیلامی را نقل کرده است؛ اما اشتقاق از day- «دیدن» همان است که پوکورنی و والده-پوکورنی و کتاب‌های امروزی می‌دهند. پس این جعبه تأیید می‌شود.\",\n \"sources\":[W+\"%D8%AF%DB%8C%D8%AF%D9%86\"],\n \"ref_check\":[\n  {\"ref\":\"POK:243\",\"status\":\"supports\",\"note\":\"IEW 243 (POK_01.txt f-f page 254): '… daēman- n. ,Auge, Augapfel; Blick', dōiθra- n. ,Auge', daēnā ,Religion' und ,inneres Wesen, geistiges Ich'; npers. dīdan ,sehen'…' — daēnā is filed under this root, with both senses.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"Altiran. Wb. 662 ff., s.v. ¹daēnā- and ²daēnā- (BRT.txt lines 12417-12444)\",\"stance\":\"partial\",\"note\":\"'j., g. ¹daēnā- f. ‚Religion‘' with Y 44.11, Y 53.4, and 'j., g. ²daēnā- f. ‚inneres Wesen, geistiges Ich, Individualität‘'; at the foot: 'Et.? … — np. dīn. — Pü.: dēn'. Bartholomae confirms the meanings and the Pahlavi/NP outcome but leaves the etymology open.\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 832 (WLD_Bd1 djvu, dhau-/dheig- page)\",\"stance\":\"supports\",\"note\":\"'daēna „Religion“ und „inneres Wesen, geistiges Ich“ (s. Reichelt Av. Elem.-B. 448, vgl. εἴδωλον und dt. „Gewissen“)' — the semantic argument for deriving it from 'to see'.\"},\n  {\"src\":\"FVQ\",\"where\":\"Jeffery, Foreign Vocabulary of the Qur'ān p.132\",\"stance\":\"partial\",\"note\":\"'This Phlv. dēn is derived from Av. daēnā, religion (though this itself is probably derived from the Elamitish den)' — Jeffery accepts the Avestan word but floats a now-abandoned Elamite source for it.\"}\n ]\n})\n\nN.append({\n \"id\":14, \"lang\":\"Pahlavi\", \"words\":\"dîn\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"MP dēn [dyn'] 'religion' is the direct continuant of Av. daēnā-: OIr. -ai- monophthongises to MP -ē- and the final -ā of the feminine ā-stem is lost, giving dēn; the word is ubiquitous in Zoroastrian Middle Persian (dēn ī māzdēsn, weh-dēn 'of the good religion' — MacKenzie s.v. weh: '~dēn [-dyn' | N bih-dīn] of the good (Mazdean) religion'; Dēnkard 'Acts of the Religion' — Nyberg 'dēn-kart [dyn'krt'] “Religion's Decisions”'). Nourai's transcription 'dîn' rather than dēn is his usual practice of writing Middle Persian ē as î; the underlying form is the standard one, and Jeffery p.132 prints the Pahlavi word in the same shape ('In Phlv. we find dēn meaning religion, from which come dēnīg for religious law, ham-dēn of the same religion, and dēnān “the religious”').\",\n \"derivation_fa\":\"dēn [dyn'] فارسی میانه «دین» دنبالهٔ مستقیمِ daēnā- اوستایی است: دوواکهٔ -ai- ایرانیِ باستان در فارسی میانه به -ē- بدل می‌شود و -ā پایانیِ ستاکِ مؤنث می‌افتد، و dēn به دست می‌آید؛ این واژه در فارسیِ میانهٔ زردشتی بسیار پرکاربرد است (dēn ī māzdēsn؛ weh-dēn «به‌دین» — مکنزی: «weh-dēn [-dyn' | فارسی نو بهدین] از دینِ نیک (مزدیسنا)»؛ Dēnkart «کردارهای دین» — نیبرگ: «dēn-kart [dyn'krt']»). نوشتنِ «dîn» به‌جای dēn شیوهٔ همیشگیِ نورایی در آوانگاریِ ē فارسی میانه است؛ صورتِ زیرین همان صورتِ استاندارد است، و جفری هم در ص ۱۳۲ همین صورت را می‌آورد: «در پهلوی dēn به معنی دین داریم که از آن dēnīg «شریعت»، ham-dēn «هم‌دین» و dēnān «دین‌داران» آمده است.»\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"BQT:916\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 376 (printed ~916): the دین entry — 'دین … نام فرشته‌ای است که بمحافظت قلم مأمور است — و نام روز بیست و چهارم بود از ماه‌های شمسی … و در عربی بمعنی راه و روش و کیش و عادت و فرمانبرداری…'. Borhān gives both the Zoroastrian day-name Dēn and the sense 'religion', with Mo'in's footnote keyed to it.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie s.v. weh (PHD.txt line 649)\",\"stance\":\"supports\",\"note\":\"'weh [SPYL; wyh | M wyh, N bih] better, good. ~dēn [-dyn' | N bih-dīn] of the good (Mazdean) religion' — the Pahlavi word dēn [dyn'] in situ.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt lines 1261, 1388, 1849)\",\"stance\":\"supports\",\"note\":\"'dēn-kart [dyn'krt'] “Religion's Decisions”', 'duš-dēn [dwšdyn']', 'hām-ō-dēn [h'mwdyn']' — the stem dēn 'religion' in compounds throughout the glossary.\"},\n  {\"src\":\"FVQ\",\"where\":\"Jeffery p.132\",\"stance\":\"supports\",\"note\":\"'In Phlv. we find dēn meaning religion, from which come dēnīg for religious law, [ham-]dēn of the same religion, and dēnān, used in the sense of “the religious”, i.e. true believers. This Phlv. dēn is derived from Av. daēnā, religion.'\"}\n ]\n})\n\nN.append({\n \"id\":15, \"lang\":\"Persian\", \"words\":\"dîn 1 «دین ۱»\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"NP دین 'religion' is MP dēn with the regular raising of MP ē to NP ī (as in šēr > شیر, bēš > بیش). Mo'in's own dictionary tags the word [په.] — Pahlavi — for the senses 'آیین، کیش', 'راه، روش' and 'نام روز بیست و چهارم از هر ماه شمسی و نام ایزد نگهبان آن روز', and keeps it strictly apart from the homograph [ع.] دین 'debt, loan' (pl. دیون) which really is Arabic. Dehkhoda's article likewise traces the Persian word to Avestan daēnā 'conscience, inner spiritual faculty'. The Ferdowsī verse recorded in the JSON (بیاموز آیین و دین بهی / که بی‌دین ناخوب باشد مهی) is the standard Shāhnāmeh attestation and stands in Nushin's Vāžanāmak under دین, which is what Nourai's FSF:191 points to. Note that this Persian دین is not a re-borrowing from Arabic: it descends in an unbroken Iranian line, while Arabic دين (node 16) is itself the borrower.\",\n \"derivation_fa\":\"«دین» فارسی نو همان dēn فارسی میانه است با فرازشِ قاعده‌مندِ ē فارسی میانه به «ی» در فارسی نو (چنانکه šēr > «شیر» و bēš > «بیش»). خودِ فرهنگ معین این واژه را با نشانِ [په.] یعنی پهلوی می‌آورد، در معانیِ «آیین، کیش»، «راه، روش» و «نام روز بیست و چهارم از هر ماه شمسی و نام ایزدِ نگهبانِ آن روز»، و آن را به‌کلی از هم‌نگاشتِ [ع.] «دین» (قرض، وام؛ جمع: دیون) جدا نگاه می‌دارد که به‌راستی عربی است. دهخدا نیز واژهٔ فارسی را به daēnā اوستایی «وجدان، نیروی درونیِ معنوی» می‌رساند. بیتِ فردوسی که در داده‌ها آمده («بیاموز آیین و دین بهی / که بی‌دین ناخوب باشد مهی») شاهدِ شناخته‌شدهٔ شاهنامه است و در «واژه‌نامک» نوشین ذیلِ «دین» آمده — همان که ارجاعِ FSF:191 به آن اشاره دارد. نکتهٔ مهم آنکه این «دین» فارسی وام‌گیریِ دوباره از عربی نیست: زنجیرهٔ ایرانیِ آن ناگسسته است و برعکس، «دین» عربی (گرهٔ ۱۶) وام‌گیرنده است. ادعای نورایی درست است.\",\n \"sources\":[\"https://abadis.ir/fatofa/%D8%AF%DB%8C%D9%86/\"],\n \"ref_check\":[\n  {\"ref\":\"BQT:916\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 376 (printed ~916): the دین entry with the day-name and the sense 'کیش'.\"},\n  {\"ref\":\"MON:1597\",\"status\":\"supports\",\"note\":\"Farhang-e Mo'in s.v. دین (read via abadis.ir/fatofa/دین): the entry is split, '[ع.] قرض، وام؛ ج. دیون' versus '[په.] ۱. آیین، کیش ۲. راه، روش ۳. نام روز بیست و چهارم از هر ماه شمسی و نام ایزدی که نگهبان آن روز است' — Mo'in tags the religion-word Pahlavi, exactly as the chart requires.\"},\n  {\"ref\":\"FSF:191\",\"status\":\"supports\",\"note\":\"Nushin, Vāžanāmak (FSF_pages.txt leaf 255, the د section) carries the very verse the JSON records: 'بیاموز آیین و دین بهی / که بی‌دین ناخوب باشد مهی' — the Shāhnāmeh citation for دین.\"}\n ],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in, s.v. دین (vajehyab/abadis text)\",\"stance\":\"supports\",\"note\":\"origin tag [په.] for the religion-word; [ع.] only for 'debt'.\"},\n  {\"src\":\"BQT\",\"where\":\"Borhān-e Qāṭeʿ p.916 with Mo'in's footnote\",\"stance\":\"supports\",\"note\":\"'دین … و در عربی بمعنی راه و روش و کیش و عادت و فرمانبرداری و شأن و شوکت و مرتبه … و بفتح اول هم در عربی فرض و وام را گویند' — Borhān itself separates the Iranian 'religion' word from the Arabic 'debt' word.\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien 49, no.413 (cross-reference to no.597)\",\"stance\":\"supports\",\"note\":\"'Zd. daēnā- kann nicht gleichzeitig = np. jān und = np. dīn (Nr. 597) sein' — Hübschmann's point is that daēnā gives np. dīn (and NOT jān); i.e. he confirms this node while denying node 9.\"}\n ]\n})\n\nN.append({\n \"id\":16, \"lang\":\"Arabic\", \"words\":\"dîn 1\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Arabic دين 'religion' is a loan from Middle Persian dēn, and Nourai's chart states this correctly. Jeffery, Foreign Vocabulary of the Qur'ān pp.131-132, is the classic statement and is exactly what the chart's NOTE reports: 'As a matter of fact we have here two separate words of different origin. (i) In the sense of religion the word is a borrowing from Iranian. In Phlv. we find dēn meaning religion … besides being the origin of the Mod. Pers. دین, was borrowed into Arm. as dēn meaning religion, faith. (ii) In the sense of Judgment it is a borrowing from the Aramaic' (Rabbinic dīn, Syr. dīnā, Mand. dīn, ultimately Akkadian dīnu). The Arab lexicographers themselves suspected a foreign origin: Jeffery notes that Lisān al-ʿArab xvii.27 records authorities who admitted the word 'had no verbal root', and that al-Khafājī p.90 and al-Thaʿālibī, Fiqh 317, list it among foreign words; the denominative verb dāna 'to make a habit of' is secondary. The borrowing is pre-Islamic (the word is frequent in the early poetry). So the arrow MP dēn → Arabic dīn is confirmed, and the chart's cross-reference to a separate root 'Dīnu' for the Semitic 'judgment' word is the right treatment.\",\n \"derivation_fa\":\"«دین» عربی به معنی «کیش» وام‌واژه‌ای از dēn فارسی میانه است و نمودار این را درست آورده است. جفری در «واژه‌های دخیل در قرآن» صص ۱۳۱–۱۳۲ کلاسیک‌ترین بیانِ این نکته را دارد و یادداشتِ خودِ نمودار هم دقیقاً همان را نقل می‌کند: «در واقع ما در اینجا دو واژهٔ جدا با دو خاستگاهِ متفاوت داریم. ۱) در معنیِ «دین» این واژه وام‌گرفته از ایرانی است. در پهلوی dēn به معنی دین داریم … که خاستگاهِ «دین» فارسی نو نیز هست و به ارمنی نیز به‌صورتِ dēn وام رفته است. ۲) در معنیِ «داوری» وام‌گرفته از آرامی است» (dīn ربّانی، dīnā سریانی، dīn مندایی، و در نهایت dīnu اکدی). خودِ لغویانِ عرب هم به بیگانه بودنِ آن گمان برده‌اند: جفری یادآور می‌شود که «لسان‌العرب» (ج ۱۷ ص ۲۷) از کسانی نام می‌برد که پذیرفته‌اند این واژه ریشهٔ فعلی ندارد، و خفاجی (ص ۹۰) و ثعالبی («فقه اللغه» ص ۳۱۷) آن را در فهرستِ واژه‌های دخیل آورده‌اند؛ فعلِ dāna «عادت کردن» ساختی ثانوی و برگرفته از خودِ اسم است. وام‌گیری پیش از اسلام روی داده است، چون واژه در شعر جاهلی فراوان است. پس پیکانِ dēn فارسی میانه ← «دین» عربی تأیید می‌شود و ارجاعِ نمودار به ریشهٔ جداگانهٔ «Dînu» برای واژهٔ سامیِ «داوری» نیز درست است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"FVQ:131\",\"status\":\"supports\",\"note\":\"Jeffery p.131 (FVQ_pages.txt leaf 148) opens the entry دين: 'Judgment, Religion, and in ix, 29, verbally “to make profession of faith”… There is ground, however, for thinking that the word is not Arabic at all.'\"},\n  {\"ref\":\"BQT:916\",\"status\":\"partial\",\"note\":\"Borhān p.916 lists the Arabic senses of دین ('و در عربی بمعنی راه و روش و کیش و عادت و فرمانبرداری…') without stating the direction of borrowing; Mo'in's footnote supplies the Iranian etymology.\"}\n ],\n \"consulted\":[\n  {\"src\":\"FVQ\",\"where\":\"Jeffery pp.131-133 (FVQ_pages.txt leaves 148-150)\",\"stance\":\"supports\",\"note\":\"'we have here two separate words of different origin. (i) In the sense of religion the word is a borrowing from Iranian… This Phlv. dēn is derived from Av. daēnā, religion… (ii) In the sense of Judgment it is a borrowing from the Aramaic. Thus we find in common use the Rabbinic dīn, Syr. dīnā and Mand. dīn, all meaning judgment and, indeed, the judgment of the last day.' The chart's NOTE (FVQ:132) is an accurate summary.\"},\n  {\"src\":\"AFA\",\"where\":\"Fraenkel, Die aramäischen Fremdwörter im Arabischen (cited by Jeffery ad loc.)\",\"stance\":\"supports\",\"note\":\"Jeffery's notes to the entry cite Fraenkel, Vocab. 22, and Nöldeke ZDMG xxxvii.534 for the double origin — Fraenkel's book supports the Aramaic half.\"},\n  {\"src\":\"KLN\",\"where\":\"Klein (grep 'din', 'deen' as a Semitic headword in KLN_1971.txt)\",\"stance\":\"silent\",\"note\":\"Klein's English dictionary has no entry for Arabic dīn; nothing for or against.\"}\n ]\n})\n\nN.append({\n \"id\":17, \"lang\":\"Persian\", \"words\":\"«ادیان ، دیانت» ; «تدیّن ، متدیّن»\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"These are Arabic derivatives of the (borrowed) stem d-y-n that Persian took back from Arabic — a classic Persian → Arabic → Persian round trip. أديان adyān is the broken plural of dīn (pattern afʿāl); ديانة diyāna is the abstract noun in -a of the same stem; تديّن tadayyun is the maṣdar of the reflexive form V tadayyana 'to profess a religion'; متديّن mutadayyin is its active participle 'religious, pious'. None of these could have been formed in Persian, since they use Arabic templatic morphology; they entered Persian as learned Arabic vocabulary in the Islamic period, alongside the inherited دین which was already there. The node's own claim — that these Persian words come from Arabic dīn (node 16) rather than directly from Pahlavi — is therefore right, and it is the standard treatment of such doublets.\",\n \"derivation_fa\":\"این‌ها ساخته‌های عربی بر ستاکِ (وام‌گرفتهٔ) د-ی-ن‌اند که فارسی دوباره از عربی پس گرفته است — نمونهٔ روشنِ گردشِ فارسی ← عربی ← فارسی. «ادیان» جمعِ مکسّرِ «دین» بر وزنِ أفعال است؛ «دیانت» اسمِ معنایِ همان ستاک با تاءِ پایانی؛ «تدیّن» مصدرِ بابِ تفعّل از «تدیّن» یعنی «دین‌ورزی کردن»؛ و «متدیّن» اسمِ فاعلِ همان باب به معنی «دین‌دار». هیچ‌یک از این‌ها نمی‌توانست در فارسی ساخته شود، چون همه بر پایهٔ صرفِ قالبیِ عربی‌اند؛ این‌ها در دورهٔ اسلامی همچون واژگانِ فاضلانهٔ عربی وارد فارسی شدند، در کنارِ «دین»ِ موروثی که از پیش در زبان بود. پس ادعای این گره — که این واژه‌های فارسی از «دین» عربی (گرهٔ ۱۶) آمده‌اند نه یکراست از پهلوی — درست است و همان است که در بررسیِ چنین دوگانه‌هایی معمول است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"FVA:148\",\"status\":\"not_checked\",\"note\":\"Nahvi's فرهنگ واژه‌های عربی در فارسی is not digitised on any permitted platform (refs_online.json: 'Searched archive.org, ketabnak, noorlib, web: no digital copy found'), so the cited page could not be read.\"}\n ],\n \"consulted\":[\n  {\"src\":\"FVQ\",\"where\":\"Jeffery pp.131-132\",\"stance\":\"supports\",\"note\":\"Jeffery notes the Arabic-internal expansion of the stem — 'the verb dāna “to do a thing as a habit” … seems to be denominative from dīn' and 'these, however, are later developments of the word within Arabic' — which is exactly the status of tadayyun/mutadayyin.\"},\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in, s.v. دین / دیانت (abadis text)\",\"stance\":\"supports\",\"note\":\"Mo'in marks the Arabic-morphology members of this family [ع.] while marking the inherited دین [په.] — the two layers the node distinguishes.\"},\n  {\"src\":\"PLA\",\"where\":\"Asbaghi, Persische Lehnwörter im Arabischen (grep 'dīn' in PLA_pages.txt)\",\"stance\":\"silent\",\"note\":\"Asbaghi's list of Persian loans in Arabic did not yield a readable dīn entry in the local OCR; no contradiction.\"}\n ]\n})\n\nN.append({\n \"id\":18, \"lang\":\"Sogdian\", \"words\":\"wyn; dyn, dynh; dyn-d`r\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Two of the three items are right and one hangs from the wrong root. Sogdian δyn / δynh (Gharib transliterates with δ: δēn, δēnē) 'religion' and δynδʾr (δēnδār) 'religious, priest, monk, electus' are on Gharib pp.148-149, entries 3759-3772 (δynʾβrʾnyg, δynʾβrʾst 'electae', δynʾk 'δēnē', δynδʾr) — genuine continuants of Iranian *dainā-, spread in Sogdian largely through Manichaean and Christian religious usage, and so real reflexes of the daēnā branch of this chart (node 13). But 'wyn : to see' is Gharib's entry 10394 (printed pp.421-422), where he writes 'wyn- … wēn ⊙ <*waina-, Av. vaēna- ⊙ inf. -(ʾ)y ⇒wyt-' — i.e. Sogdian wēn- is from *waina-, the root discussed at node 4, and its own suppletive preterite is wyt- (< *daiH-). Cheung confirms: 'SOGDIAN: SSogd. wyn, BSogd. wyn, CSogd. wyn, MSogd. wyn “to see”' under *uai(H)n. So the node is right about the religion-words and misfiled about the verb.\",\n \"derivation_fa\":\"از سه قلمِ این گره دو تا درست است و یکی از ریشهٔ نادرست آویخته است. سغدیِ δyn / δynh (قریب با δ آوانگاری می‌کند: δēn، δēnē) «دین» و δynδʾr (δēnδār) «دین‌دار، روحانی، برگزیده» در صفحه‌های ۱۴۸–۱۴۹ فرهنگ قریب آمده‌اند (شماره‌های ۳۷۵۹ تا ۳۷۷۲: δynʾβrʾnyg، δynʾβrʾst، δynʾk، δynδʾr) و دنبالهٔ راستینِ *dainā- ایرانی‌اند که بیشتر از راهِ کاربردِ دینیِ مانوی و مسیحی در سغدی گسترده شده‌اند؛ پس بازتاب‌های درستِ شاخهٔ daēnā در این نمودارند (گرهٔ ۱۳). اما «wyn: دیدن» شمارهٔ ۱۰۳۹۴ قریب است (صص ۴۲۱–۴۲۲) که در آنجا می‌نویسد: «wyn- … wēn ⊙ < *waina-، اوستایی vaēna- ⊙ مصدر -(ʾ)y ⇒ wyt-» — یعنی wēn- سغدی از *waina- است، همان ریشه‌ای که در گرهٔ ۴ سخنش رفت، و ستاکِ گذشتهٔ مکمّلِ خودش wyt- (از *daiH-) است. چونگ نیز همین را زیرِ *uai(H)n می‌آورد. پس این گره دربارهٔ واژه‌های «دین» درست است و دربارهٔ فعل نادرست جای گرفته است؛ با این تفکیک، پذیرفتنی است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"SOD:148\",\"status\":\"supports\",\"note\":\"Gharib, Sogdian-Persian-English Dictionary p.148-149 (SOD_pages.txt leaf 214): entries '3759 δynʾβrʾnyg M — Δēnāβarānīg — Dēnāvarīya (a Manichean sect)', '3760 δynʾβrʾst M, S — δēnāβarāst — electae', '3761 δynʾk B — δēnē', '3772 δynδʾr B, M, S — δēnδār (δynδʾr, δnδʾr) — religious, priest, monk, electus'. Exactly the words of the node.\"},\n  {\"ref\":\"SOD:421\",\"status\":\"partial\",\"note\":\"Gharib entry 10394 (SOD_pages.txt leaf 488, printed ~421-422): 'wyn- … wēn ⊙ <*waina-, Av. vaēna- ⊙ inf. -(ʾ)y ⇒wyt-'. The verb is on the cited page, but Gharib derives it from *waina-, not from the root of this chart.\"}\n ],\n \"consulted\":[\n  {\"src\":\"SOD\",\"where\":\"Gharib pp.148-149 and 421-422\",\"stance\":\"partial\",\"note\":\"see the two ref_check quotations: supports δēn/δēnδār, contradicts the placement of wyn-.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *uai(H)n, Sogdian section\",\"stance\":\"contradicts\",\"note\":\"'*SOGDIAN: SSogd. wyn, BSogd. wyn, CSogd. wyn, MSogd. wyn “to see” || (+ *abi-) BSogd. βywyn “to foresee”, CSogd. bywnyʾ (m.) “prophet”' — filed under *uai(H)n, not *daiH¹.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *daiH¹, Sogdian section\",\"stance\":\"partial\",\"note\":\"under *daiH¹ Cheung lists only the derived Sogdian words '(+ *ā-) BSogd. ʾʾdynʾk, ʾʾδʾynʾk “mirror” || (+ *ham-) ʾnδʾyk “custom, habit, manner”' — the Sogdian reflexes of THIS root are the mirror and custom words, not wyn-.\"}\n ]\n})\n\nN.append({\n \"id\":19, \"lang\":\"Greek\", \"words\":\"sema\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Gk. σῆμα (Doric σᾶμα) 'sign, mark, token; grave-mound; portent' has been derived since the nineteenth century from *dhi̯eh₂-mn̥, the exact formal match of Skt. dhyā́man- 'thought', with the regular Greek treatment of initial *dhy- as s- (cf. σήμερον). Pokorny 243 prints 'gr. σῆμα, dor. σᾶμα ,Zeichen, Kennzeichen, Merkmal usw.' (*dhiā-mn = ai. dhyāman-)' together with σημαίνω 'mache durch ein Zeichen kenntlich'; Walde-Pokorny I 832 has the same; Watkins/AHD has 'suffixed form *dhyā-mn̥ in Greek sēmeion and sēma (stem sēmat-), sign'; Klein s.v. semantics says sêma 'is cogn. with OI. dhīḥ, dhyānaḥ “thought”'. So Nourai's POK:243 + AHD are precisely on target, and the gloss 'things seen, signs' is a fair paraphrase. The reason for 'plausible' rather than 'confirmed' is that the equation is no longer unanimous: Wiktionary keeps *dʰyéh₂mn̥ but adds that 'Beekes is skeptical of the semantics'; Pokorny himself notes Leumann's alternative, that σῆμα is rather to be compared with Khotanese Saka dyāma 'sign'; and Cheung 2007, in the entry for the Iranian side of this very root, states flatly 'Gr. σῆμα / σᾶμα “sign, mark” is unrelated'. The traditional derivation is still the majority view but is contested.\",\n \"derivation_fa\":\"σῆμα یونانی (در گویش دُری σᾶμα) «نشان، علامت، نشانه؛ گورتپه؛ فالِ آسمانی» را از سدهٔ نوزدهم تاکنون از *dhi̯eh₂-mn̥ گرفته‌اند، که از نظر ساخت درست برابرِ dhyā́man- سنسکریت «اندیشه» است، با تحولِ قاعده‌مندِ *dhy- آغازین به s- در یونانی (سنجیده شود با σήμερον). پوکورنی در ص ۲۴۳ می‌نویسد: «یونانی σῆμα، دُری σᾶμα «نشان، علامت و جز آن» (*dhiā-mn = dhyāman- سنسکریت)» و در کنارش σημαίνω «با نشانه شناساندن»؛ والده-پوکورنی (جلد ۱ ص ۸۳۲) همان را دارد؛ واتکینز نیز «صورتِ پسوندیِ *dhyā-mn̥ در یونانی sēmeion و sēma» را می‌آورد؛ و کلاین ذیلِ semantics می‌گوید sêma هم‌ریشهٔ dhīḥ و dhyānaḥ سنسکریت است. پس ارجاعِ POK:243 و AHD در جای خود درست است و ترجمهٔ «چیزهای دیده‌شده، نشانه‌ها» برگردانی پذیرفتنی است. اما اینکه حکم «با احتیاط پذیرفتنی» است نه «تأییدشده»، از آن روست که این برابرنهاد دیگر اجماعی نیست: ویکی‌واژه همان *dʰyéh₂mn̥ را نگاه می‌دارد ولی می‌افزاید که بیکس در سویهٔ معنایی تردید دارد؛ خودِ پوکورنی جایگزینِ لویمان را یاد می‌کند که σῆμα را با dyāma ختنی-سکایی «نشان» می‌سنجد؛ و چونگ (۲۰۰۷) در مدخلِ ایرانیِ همین ریشه به‌صراحت می‌نویسد «σῆμα / σᾶμα یونانی «نشان» بی‌ارتباط است». پس اشتقاقِ سنتی هنوز دیدگاهِ اکثریت است اما مورد اختلاف.\",\n \"sources\":[W+\"%CF%83%E1%BF%86%CE%BC%CE%B1\", \"https://www.etymonline.com/word/semantic\"],\n \"ref_check\":[\n  {\"ref\":\"POK:243\",\"status\":\"supports\",\"note\":\"IEW 243: 'gr. σῆμα, dor. σᾶμα ,Zeichen, Kennzeichen, Merkmal usw.' (*dhiā-mn = ai. dhyāman-; Lit. bei Boisacq s. v., vgl. Schwyzer Gr. Gr. I 322; nach Leumann [Abh. Kunde d. Morgenl. 20,1, S.96] vielmehr zu sakisch dyāma ,Zeichen'), σημαίνω ,mache durch ein Zeichen kenntlich usw.''. Supports the arrow — and itself records Leumann's dissent.\"},\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"ref_full\":\"AHD (Watkins) s.v. dheiə-\",\"note\":\"Watkins 1985: 'Variant form *dhyā- (< *dhyaə-) in: a. suffixed form *dhyā-mn̥ in Greek sēmeion and sēma (stem sēmat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC'.\"}\n ],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny I 832\",\"stance\":\"supports\",\"note\":\"'Gr. σῆμα, dor. σᾶμα „Zeichen, Kennzeichen, Merkmal usw.“ (*dhiā-mn = ai. dhyāman-; Lit. bei Boisacq s. v.; überholt Wackernagel KZ. 30, 295, Schrader KZ. 30, 481), σημαίνω „mache durch ein Zeichen kenntlich usw.“'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. semantics (KLN_1971.txt line 217408)\",\"stance\":\"supports\",\"note\":\"'fr. Gk. σῆμα, “sign”, which is cogn. with OI. dhīḥ, dhyānaḥ, “thought”, dhyāti, dhyāyati, “thinks”. See dhyana.'\"},\n  {\"src\":\"CHEUNG\",\"where\":\"s.v. *daiH¹, closing note\",\"stance\":\"contradicts\",\"note\":\"'An IE etymology for this IIr. root is uncertain… Gr. σῆμα / σᾶμα “sign, mark” is unrelated.'\"},\n  {\"src\":\"SYN\",\"where\":\"Buck, Dictionary of Selected Synonyms (grep 'sema', 'sign' §22.44)\",\"stance\":\"silent\",\"note\":\"Buck's 'sign, mark' section could not be located in the OCR under a usable string; nothing found either way.\"}\n ]\n})\n\nN.append({\n \"id\":20, \"lang\":\"Arabic\", \"words\":\"sîmâ\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Arabic سِيمَا / سِيمَاء 'mark, sign; look, mien' — the Qur'anic word of 48:29 'sīmāhum fī wujūhihim min athari s-sujūd', 'their mark is on their faces from the traces of prostration' — is indeed a Greek word, but it did not come straight from Greek: Wiktionary (s.v. سيماء) gives 'Borrowed from Aramaic סִימָא (sīmā) / סִימָנָא (sīmānā), from Ancient Greek σῆμα (sêma), σημεῖον (sēmeîon)', i.e. the ordinary Hellenistic route by which Greek technical and administrative vocabulary reached Arabic — through Syriac/Jewish-Aramaic in the centuries before Islam. The Arab grammarians instead attached the word to the native root و س م wasama 'to brand, mark' (whence wasm, sima), which explains its long life and its productivity in Arabic (سيمياء 'sign-magic'); the Greek etymology explains the unusual shape and the Aramaic intermediary. So the substance of Nourai's arrow (Gk. sēma → Arab. sīmā) is accepted, with the route corrected to Greek → Aramaic → Arabic; and since the Greek word's own descent from the root of this chart is itself only 'plausible' (node 19), so is this node.\",\n \"derivation_fa\":\"«سیما / سیماء» عربی به معنی «نشان، علامت؛ چهره و هیئت» — همان واژهٔ قرآنیِ آیهٔ ۲۹ سورهٔ فتح، «سیماهم فی وجوههم من أثر السجود» — به‌راستی واژه‌ای یونانی است، اما نه یکراست از یونانی: ویکی‌واژه (ذیل «سيماء») می‌نویسد «وام‌گرفته از آرامیِ sīmā / sīmānā، از یونانیِ باستانِ σῆμα و σημεῖον»، یعنی همان راهِ معمولی که واژگانِ فنّی و دیوانیِ یونانی در سده‌های پیش از اسلام از گذرِ سریانی و آرامیِ یهودی به عربی رسیده‌اند. در برابر، نحویانِ عرب این واژه را به ریشهٔ بومیِ «و س م» (وَسَمَ «داغ زدن، نشان کردن»، و از آن «وَسْم» و «سِمَة») بسته‌اند، و همین است که ماندگاری و زایاییِ آن را در عربی توضیح می‌دهد («سیمیاء» یعنی جادوی نشانه‌ها)؛ اما ریشه‌شناسیِ یونانی صورتِ ناهنجارِ واژه و میانجیِ آرامی را توضیح می‌دهد. پس جانِ ادعای نورایی (σῆμα یونانی ← «سیما» عربی) پذیرفته است، با این تصحیح که راه از یونانی به آرامی و از آرامی به عربی بوده؛ و چون خودِ پیوندِ واژهٔ یونانی با ریشهٔ این نمودار تنها «با احتیاط پذیرفتنی» است (گرهٔ ۱۹)، این گره هم همان حکم را می‌گیرد.\",\n \"sources\":[W+\"%D8%B3%D9%8A%D9%85%D8%A7%D8%A1\"],\n \"ref_check\":[\n  {\"ref\":\"VDQ:275\",\"status\":\"not_checked\",\"note\":\"VDQ is Badreh'i's Persian translation of Jeffery (noorlib.ir/book/view/12868), whose viewer is JavaScript-only and cannot be fetched (refs_online.json: 'needs a browser'). The substance was therefore checked in the English original: Jeffery's FVQ (FVQ.txt / FVQ_pages.txt) was grepped for 'sima', 'sīmā', 'simiya' with no hit, so سيما does not appear to be one of Jeffery's own entries — the claim may belong to the translator's added notes, which could not be read.\"}\n ],\n \"consulted\":[\n  {\"src\":\"FVQ\",\"where\":\"Jeffery, Foreign Vocabulary of the Qur'ān (grep 'sima', 'sīmā' in FVQ.txt)\",\"stance\":\"silent\",\"note\":\"no entry for سيما found; Jeffery's Qur'anic loan list does not treat it.\"},\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. semantics / semeio- (KLN_1971.txt lines 217408, 217460)\",\"stance\":\"partial\",\"note\":\"Klein documents Gk. σῆμα and σημεῖον and their spread through learned vocabulary, but says nothing about an Arabic borrowing.\"},\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in / Dehkhoda s.v. سیما (abadis.ir)\",\"stance\":\"partial\",\"note\":\"Mo'in and Dehkhoda mark the word عربی and gloss it 'نشان و علامتی که شناخته شود بدان خیر و شر'; they take it as Arabic without discussing an ultimate Greek source.\"}\n ]\n})\n\nN.append({\n \"id\":21, \"lang\":\"Persian\", \"words\":\"sîmâ «سیما»\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Persian سیما 'countenance, face; sign' is a straightforward Arabic loan, taken over unchanged in form (an invariable ā-final noun) and slightly extended in sense: from 'mark, distinguishing sign' to 'face, features, countenance' — the shift being mediated by the Qur'anic phrase 'their mark is on their faces', so that the mark on the face came to stand for the face itself. Mo'in's dictionary tags the entry as Arabic — '(اِ) ۱. چهره، قیافه ۲. علامت، هیئت' — and Dehkhoda glosses it 'ع اِ. نشان و علامتی که شناخته شود بدان خیر و شر', citing Ghiyāth al-Lughāt and Tarjumān al-Qurʾān, i.e. the classical Islamic lexicographical tradition. Nourai's MON:1983 is therefore the right kind of reference for the right claim: the Persian word comes from Arabic, and only through Arabic from Greek.\",\n \"derivation_fa\":\"«سیما» در فارسی وام‌واژه‌ای عربی است که بی‌هیچ دگرگونیِ صوری گرفته شده (اسمی پایان‌یافته به الف که صرف نمی‌شود) و اندکی گسترشِ معنایی یافته است: از «نشان، علامتِ شناسایی» به «چهره، رخسار» — و این تحول را همان تعبیر قرآنیِ «سیماهم فی وجوههم» میانجی شده است، چنانکه نشانِ روی، خودِ رو را نمایندگی کرده است. فرهنگ معین این مدخل را عربی می‌داند و می‌نویسد «(اِ) ۱. چهره، قیافه ۲. علامت، هیئت»، و دهخدا آن را «ع اِ. نشان و علامتی که شناخته شود بدان خیر و شر» معنا می‌کند و به «غیاث اللغات» و «ترجمان القرآن» ارجاع می‌دهد، یعنی به سنّتِ لغت‌نویسیِ کلاسیکِ اسلامی. پس ارجاعِ MON:1983 نورایی هم مأخذِ درستی است هم برای ادعای درست: واژهٔ فارسی از عربی آمده و تنها از راهِ عربی به یونانی می‌رسد. ادعای این گره درست است.\",\n \"sources\":[\"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%85%D8%A7/\", W+\"%D8%B3%D9%8A%D9%85%D8%A7%D8%A1\"],\n \"ref_check\":[\n  {\"ref\":\"MON:1983\",\"status\":\"supports\",\"note\":\"Farhang-e Mo'in s.v. سیما (read via abadis.ir/fatofa/سیما): '(اِ) ۱. چهره، قیافه ۲. علامت، هیئت', an Arabic-marked entry; Dehkhoda on the same page: 'ع اِ. نشان و علامتی که شناخته شود بدان خیر و شر' with Ghiyāth al-Lughāt and Tarjumān al-Qurʾān as authorities.\"}\n ],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in, s.v. سیما\",\"stance\":\"supports\",\"note\":\"see ref_check; Mo'in treats it as an Arabic noun in Persian.\"},\n  {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e Rishe-hā-ye Hend-o-Orupāyi (grep 'سیما' in ARY_pages.txt)\",\"stance\":\"silent\",\"note\":\"Aryanpur's Indo-European root dictionary does not carry سیما, which is consistent with its being an Arabic loan rather than an inherited Iranian word.\"}\n ]\n})\n\nN.append({\n \"id\":22, \"lang\":\"English\", \"words\":\"semantics\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"English semantics is a nineteenth-century learned formation, not an inherited word: French sémantique was coined by Michel Bréal (Essai de sémantique, 1897; the term is used from 1883) from Gk. σημαντικός 'significant, having meaning', the verbal adjective of σημαίνειν 'to show by a sign, signify', itself denominative from σῆμα. English took the adjective semantic in 1894 and the noun semantics soon after (with the plural -ics of the names of sciences). Klein s.v. semantics gives exactly this chain, and Watkins/AHD lists SEMANTIC among the English descendants of dheiə- through sēma; Etymonline agrees, tracing 'semantic' to 'PIE root *dheie- “to see, look”'. Nourai's bare reference 'AHD' is therefore accurate, and the box needs no correction — subject only to the caveat on node 19 about whether σῆμα really belongs to this root.\",\n \"derivation_fa\":\"واژهٔ انگلیسیِ semantics ساخته‌ای فاضلانه از سدهٔ نوزدهم است نه واژه‌ای موروثی: sémantique فرانسوی را میشل بره‌آل ساخت (رسالهٔ Essai de sémantique، ۱۸۹۷؛ خودِ اصطلاح از ۱۸۸۳ به کار رفته) از σημαντικός یونانی «معنادار، دلالت‌کننده»، صفتِ فعلیِ σημαίνειν «با نشانه نشان دادن»، که خود از σῆμα ساخته شده است. انگلیسی صفتِ semantic را در ۱۸۹۴ و اندکی پس از آن اسمِ semantics را گرفت (با پسوندِ -ics که نامِ دانش‌ها را می‌سازد). کلاین ذیلِ semantics همین زنجیره را می‌دهد، و واتکینز نیز SEMANTIC را در شمارِ بازماندگانِ انگلیسیِ ریشهٔ dheiə- از راهِ sēma می‌آورد؛ اتیمانلاین هم آن را به «ریشهٔ هندواروپاییِ *dheie- «دیدن، نگریستن»» می‌رساند. پس ارجاعِ کوتاهِ نورایی («AHD») درست است و این جعبه نیازی به اصلاح ندارد — جز همان احتیاطی که در گرهٔ ۱۹ دربارهٔ تعلقِ σῆμα به این ریشه گفته شد.\",\n \"sources\":[\"https://www.etymonline.com/word/semantic\"],\n \"ref_check\":[\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. dheiə- lists 'SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC' as the English words reaching this root through Greek sēma/sēmeion.\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein, Comprehensive Etymological Dictionary, s.v. semantics (KLN_1971.txt lines 217402-217420)\",\"stance\":\"supports\",\"note\":\"'semantics, n., the science of the meanings of words. — F. sémantique, coined by Michel Bréal, author of Essai de sémantique (1897) fr. Gk. σημαντικός, “significant, meaning”, fr. σημαίνειν, “to signify”, fr. σῆμα, “sign”, which is cogn. with OI. dhīḥ, dhyānaḥ, “thought”.'\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etymological Dictionary (grep 'semantic' in SKT.txt)\",\"stance\":\"silent\",\"note\":\"Skeat's concise dictionary, whose last revision predates the term's naturalisation, has no entry.\"},\n  {\"src\":\"WEB\",\"where\":\"Webster's New Twentieth Century Dictionary (grep 'semantics' in WEB_vol1.txt)\",\"stance\":\"silent\",\"note\":\"the local OCR volume covers only part of the alphabet; no usable entry retrieved.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 132,\n \"book_page\": 102,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [root]\n}\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-132.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint('nodes', len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build132.py",
 "description": "Build page-132.json"
}
```


### [2026-09-05T20:30:35.723Z] TOOL RESULT

```
nodes 22
```


## [2026-09-05T20:30:43.147Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-132.json'\nd=json.load(open(p,encoding='utf-8'))\nfor n in d['entries'][0]['nodes']:\n    for rc in n.get('ref_check',[]):\n        rc.pop('ref_full',None)\njson.dump(d,io.open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint('ok')\nEOF\npython3 -m json.tool data/verification/page-132.json > /dev/null && echo \"JSON valid\"\npython3 tools/verify_check.py 132",
 "description": "Clean and validate"
}
```


### [2026-09-05T20:31:53.625Z] TOOL RESULT

```
ok
JSON valid
nodes verified: 22/22
node verdicts: {'plausible': 6, 'disputed': 6, 'confirmed': 10}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 24, 'partial': 10, 'contradicts': 2, 'not_checked': 4, 'not_found': 2}
books consulted: {'supports': 26, 'partial': 19, 'contradicts': 13, 'silent': 12} | by book: {'CHEUNG': 10, 'PHD': 9, 'WLD': 5, 'NYB': 5, 'KLN': 5, 'FVQ': 5, 'BRT': 4, 'HUB': 4, 'HRN': 4, 'MON': 4, 'POK': 2, 'AHD': 2, 'KNT': 1, 'TLM': 1, 'HENNING': 1, 'BQT': 1, 'AFA': 1, 'PLA': 1, 'SOD': 1, 'SYN': 1, 'ARY': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-05T20:32:03.497Z] TOOL CALL #75: Bash

```json
{
 "command": "ls site/pages/132.jpg 2>/dev/null || pdftoppm -f 132 -l 132 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg132 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render printed page 132"
}
```


### [2026-09-05T20:32:05.503Z] TOOL RESULT

```
site/pages/132.jpg
total 15516
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:31 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:32:43.870Z] TOOL CALL #76: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/132.jpg"
}
```


### [2026-09-05T20:32:43.900Z] TOOL RESULT

```

```


## [2026-09-05T20:33:17.952Z] AGENT

Verification file written and validated. Printed page 132 checked against the extraction — no extraction errors.

**Page 132 (book p. 102), root "Dheye" (PIE \*dʰeyh₂- 'to see'), 1 entry, 22 nodes**

- Root: **confirmed** (Pokorny IEW 243 verbatim; Walde‑Pokorny I 831 f., Watkins/AHD agree).
- Node verdicts: **confirmed 10, plausible 6, disputed 6**. `verify_check.py 132` → 22/22 nodes, **0 PROBLEM lines**.

Disputed items:
- **#4 Old Persian `dî, dây, wai, vâe / vaina / adhi-vaina`** — merges two roots. Kent §130/§211 derives OP vain- from PIE \*ueid-ne- (lexicon p. 206a, not 191a); Cheung: \*uai(H)n < \*uei(H₁)-no-, Pok. 1123. Nourai's own ref FFD:55 says outright «"دیدن" و "بین" … دو ریشه‌ای است». `adhi-vaina 'ornament'` is no Old Persian word at all — a back‑formation from Pahlavi ʾdwyn'.
- **#5 Pahlavi `adhvěnak 'ornament'`** — MacKenzie/Nyberg read ʾdwynk' as ēwēnag 'manner, custom / mirror'; Cheung files it under \*(ā-)abi-daiH¹, not vain-. (wēnāg 'seeing' is fine.)
- **#6 Persian `âdîneh`** — Nyberg (s.v. āivēnak) explicitly: ādīnah "cannot be etymologically connected with āivēnak"; < \*ati-ayana- 'congregation'. `âzîn` unsupported (Henning, Sogdica 17, = MP āzīn- 'to sew', as the chart's own note says).
- **#8/#9 Pahlavi/Persian `gyân, jân` ← Sanskrit dhyāna** — Hübschmann 1895 p. 49 (Nourai's ref) does say this, but modern view is MP gyān < PIr \*wyaHnáH = \*wi- + \*HanH- 'to breathe' (Av. viiānaiiā, Skt. vyāná-); dhy- cannot yield gy-.
- **#10 Avestan/OP `dais, ham-dais-a`** — belongs to PIE \*deiḱ- 'to show' (Pokorny **188**, not 243); Nourai's own FFD:33 says «ریشهٔ daiš به معنی "نشان دادن" است». The node's internal content (→ handēš → andīšīdan) is correct.

Notable "plausible": #1 (`upa-dîta` unattested — Hübschmann 38 strikes it; Bartholomae/Pokorny have paiti-dīta-), #3 (`dîm` = 'face, cheek' per Borhān 915 + Mo'in's footnote; the gloss 'light' belongs to the separate entry دیمه), #19 (Gk. sēma: Pokorny/Watkins/Klein support, but Beekes doubts the semantics and Cheung calls it "unrelated"), #20 (Arabic sīmā came via Aramaic, not straight from Greek).

References not checkable: AEF:322 / AEF:80 (Khaleqi Motlaq — not digitised), FVA:148 (Nahvi — no copy), VDQ:275 (noorlib JS viewer; substance checked in Jeffery's English original, which has no سيما entry), SNS:291 (OCR unusable). Eight web pages archived via `fetch_source.py`.
