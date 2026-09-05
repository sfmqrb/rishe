# Verification process log — verify-page-143


## [2026-09-05T20:08:31.219Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 143 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-143.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-143.json. Write /home/sfmqrb/git/rishe/data/verification/page-143.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 143` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:32.741Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-05T20:08:33.427Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:33.441Z] TOOL RESULT

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


## [2026-09-05T20:08:33.744Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-143.txt"
}
```


### [2026-09-05T20:08:33.767Z] TOOL RESULT

```
1	=== PDF page 143 (book page 113) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dus : bad, evil  (refs POK:227)
4	#1 (parent #0) [Avestan] refs=POK:227; FSF:179, 183 | duš, duž, duždâo : bad, evil ; duš-manah : with evil thoughts ☞Men 1 ; duš-nâma : bad name ☞Nomn ; duš-vâre : difficult to carry ☞Bher 1 ; duš-xv-athra, duž-âthra : not easy ☞Čter
5	  #2 (parent #1) [Persian] refs=BQT:850,853,867; HRN:126; MON:1536 | dozd «دزد» : thief ; došman «دشمن (دُژمان، دُژم، دُژمناک)» : enemy ; došnâm «دشنام ( دُژنام )» : insult ; došvâr «دشوار ( دُژوار )» : difficult ; došxâr «دشخوار» : difficult | extra: دُژآگاه ، دُژآلود ، دُژآهنگ ، دُژبرو
6	  #3 (parent #1) [Avestan] refs=BQT:897; VIE:31; TZF:22 | duš-haem : bad tempered ☞Haem ; duš-yâta : backbite ☞Yem ; daoš-ahva, duž-axva : evil world ☞An 1 ; duš-pithwa : bad fat, abscess
7	    #4 (parent #3) [Pahlavi] refs=SBK:214 | dužax : hell
8	      #5 (parent #4) [Persian] refs=BQT:896; HRN:129; VIE:31; TZF:21 | dožxîm «دژخیم (دُژخیم)» : bad tempered ; došyâd «دشیاد» : humiliation of people in their absence ; dŭzax «دوزخ» : hell ; dožpîh «دُژپیه ( دُشپیل ، دُژک ، دُمَل )» : abscess | NOTE: See "Dumb" for another possible derivation of "domal"
9	  #6 (parent #1) [Avestan] refs=BRT:755; BQT:1063 | duž-aka : with bad sting hooks, porcupine ☞Ang | NOTE: BRT:755 is not quite certain about this derivation.
10	    #7 (parent #6) [Pahlavi] refs=SNS:168; BQT:1063 | žužag, zuzag, jujag : porcupine, chicken
11	      #8 (parent #7) [Persian] refs=BRT:755; BQT:1063; HRN:152; MON:1250,1320; IEC:1391 | žŭž «ژوژ ( ژوژه )» : porcupine ; jŭjeh «جوجه ( جوژه، چوژه )» : chicken
12	  #9 (parent #1) [Avestan] refs=AVG:237 | duš-kareta : ill-done ☞Kwer ; duš-cithra, duš-citra : of evil seed (race) ☞Skai ; duš-uxta : ill-spoken ☞Wegwh ; duš-daěna : of evil conscience ☞Dheye
13	#10 (parent #0) [Greek] refs=AHD | dus : bad
14	  #11 (parent #10) [Latin] refs=None | dys- : faulty, diseased
15	    #12 (parent #11) [English] refs=None | dysfunction, dystrophy
16	--- entry 1 ---
17	ROOT Dvei -> redirect to Dwei
18	
```


## [2026-09-05T20:08:37.028Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-143.json",
 "description": "Read source JSON for page 143"
}
```


### [2026-09-05T20:08:37.114Z] TOOL RESULT

```
{
  "pdf_page": 143,
  "book_page": 113,
  "entries": [
    {
      "root": {
        "name": "Dus",
        "lang": "Indo-European",
        "refs": "POK:227",
        "gloss": "bad, evil"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:227; FSF:179, 183",
          "words": [
            {"translit": "duš, duž, duždâo", "gloss": "bad, evil", "script": null},
            {"translit": "duš-manah", "gloss": "with evil thoughts", "script": null, "see": ["Men 1"]},
            {"translit": "duš-nâma", "gloss": "bad name", "script": null, "see": ["Nomn"]},
            {"translit": "duš-vâre", "gloss": "difficult to carry", "script": null, "see": ["Bher 1"]},
            {"translit": "duš-xv-athra, duž-âthra", "gloss": "not easy", "script": null, "see": ["Čter"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:850,853,867; HRN:126; MON:1536",
          "words": [
            {"translit": "dozd", "gloss": "thief", "script": "دزد"},
            {"translit": "došman", "gloss": "enemy", "script": "دشمن (دُژمان، دُژم، دُژمناک)"},
            {"translit": "došnâm", "gloss": "insult", "script": "دشنام ( دُژنام )"},
            {"translit": "došvâr", "gloss": "difficult", "script": "دشوار ( دُژوار )"},
            {"translit": "došxâr", "gloss": "difficult", "script": "دشخوار"}
          ],
          "script_extra": "دُژآگاه ، دُژآلود ، دُژآهنگ ، دُژبرو",
          "note": null,
          "quote": {"text": "چنین گفت باو یل اسفندیار - که کاری گرفتیم دشخوار خوار", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:897; VIE:31; TZF:22",
          "words": [
            {"translit": "duš-haem", "gloss": "bad tempered", "script": null, "see": ["Haem"]},
            {"translit": "duš-yâta", "gloss": "backbite", "script": null, "see": ["Yem"]},
            {"translit": "daoš-ahva, duž-axva", "gloss": "evil world", "script": null, "see": ["An 1"]},
            {"translit": "duš-pithwa", "gloss": "bad fat, abscess", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "SBK:214",
          "words": [
            {"translit": "dužax", "gloss": "hell", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:896; HRN:129; VIE:31; TZF:21",
          "words": [
            {"translit": "dožxîm", "gloss": "bad tempered", "script": "دژخیم (دُژخیم)"},
            {"translit": "došyâd", "gloss": "humiliation of people in their absence", "script": "دشیاد"},
            {"translit": "dŭzax", "gloss": "hell", "script": "دوزخ"},
            {"translit": "dožpîh", "gloss": "abscess", "script": "دُژپیه ( دُشپیل ، دُژک ، دُمَل )"}
          ],
          "note": "See \"Dumb\" for another possible derivation of \"domal\"",
          "quote": {"text": "چنان مهربان بود دژخیم شد - وزو شهر ایران پر از بیم شد", "poet": "Ferdowsî"}
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BRT:755; BQT:1063",
          "words": [
            {"translit": "duž-aka", "gloss": "with bad sting hooks, porcupine", "script": null, "see": ["Ang"]}
          ],
          "note": "BRT:755 is not quite certain about this derivation.",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "SNS:168; BQT:1063",
          "words": [
            {"translit": "žužag, zuzag, jujag", "gloss": "porcupine, chicken", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BRT:755; BQT:1063; HRN:152; MON:1250,1320; IEC:1391",
          "words": [
            {"translit": "žŭž", "gloss": "porcupine", "script": "ژوژ ( ژوژه )"},
            {"translit": "jŭjeh", "gloss": "chicken", "script": "جوجه ( جوژه، چوژه )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 1,
          "lang": "Avestan",
          "refs": "AVG:237",
          "words": [
            {"translit": "duš-kareta", "gloss": "ill-done", "script": null, "see": ["Kwer"]},
            {"translit": "duš-cithra, duš-citra", "gloss": "of evil seed (race)", "script": null, "see": ["Skai"]},
            {"translit": "duš-uxta", "gloss": "ill-spoken", "script": null, "see": ["Wegwh"]},
            {"translit": "duš-daěna", "gloss": "of evil conscience", "script": null, "see": ["Dheye"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "dus", "gloss": "bad", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "dys-", "gloss": "faulty, diseased", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "dysfunction, dystrophy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Dvei",
        "redirect": "Dwei"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:08:37.854Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---MATRIX---\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-05T20:08:37.912Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-05T20:09:10.688Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','FSF','BQT','HRN','MON','VIE','TZF','SBK','BRT','SNS','IEC','AVG','AHD','PHD','NYB','WLD','SYN','KLN','SKT']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-05T20:09:11.112Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-127.json"
}
```


### [2026-09-05T20:09:12.692Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== VIE {"title": "M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985", "kind": "local_scan_ocr", "url": "https://parsianjoman.org/?p=5160 (Parsi-Anjoman hosts the 253-page scan)", "lookup_hint": "Not found.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_sajjadieh1364_parsianjoman.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/VIE/VIE_pages.txt"], "page_offset": "253 leaves; printed page = PDF page − 6 (PDF 100 = p.94). Only the 'fas' OCR pass was run for this book (VIE_pages.txt).", "covers_etymology": true, "notes": "Open scan (image-only) downloaded and OCRed. Image-only scan OCRed locally with tes
== TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
== SBK {"title": "M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942", "kind": "archive_djvu", "url": "https://archive.org/details/1_20250928_20250928_1159 (3 vols; vol 1 = سبک شناسی_1)", "lookup_hint": "grep in SBK.txt (raw djvu, no page breaks); use inside.php with doc='سبک شناسی_1'. Later printings keep the 1st-edition pagination approximately; verify.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SBK.txt"], "page_offset": null, "covers_etymology": false, "notes": "Persian OCR fair. galaxy_ub2007_yahoo_20151117 is another (tiny-OCR) copy."}
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== AVG {"title": "A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892", "edition_found": "1892", "kind": "archive_djvu", "url": "https://archive.org/details/pt1avestagrammar00jackuoft", "identifier": "pt1avestagrammar00jackuoft (also an-avesta-grammar-in-comparison-with-sanskrit, in.ernet.dli.2015.47742)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt", "page_offset": "leaf = printed + 54 (e.g. leaf 61 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar by numbered §; grep the § number or Avestan
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
```


### [2026-09-05T20:09:12.724Z] TOOL RESULT

```
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
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = rieche
```


## [2026-09-05T20:09:16.824Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==235' POK_01.txt | head -80",
 "description": "Print Pokorny page 227"
}
```


## [2026-09-05T20:09:17.691Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dus-\" AHD_watkins1985.txt | head -20",
 "description": "grep AHD for dus-"
}
```


### [2026-09-05T20:09:19.860Z] TOOL RESULT

```
]
o-ot.  tuggö  Ly  an.  as.  tunga^  ags.  tunge,  ahd.  zitnga^  mit  -ön-  statt  -ä; als  Ablautneubildung  vielleicht  hierher  ^nord.  tangi  ,Griffstück  der  Klinge^ rand.  tange  _,Sandrückea  zwischen  zwei  Sümpfen^;
bsl.  inzä-  m.  in  apr.  insuwis]  lit.  liezüvis  (nach  liezti  ,lecken');  aksL j§zy-ki,  skr.  jezik,  poln.  jezyk^  russ.  jazyk;  zum  Schwund  des  anlaut.  c^- s.  J.  Schmidt,  Krit.  77;
toch.  A  käntu,  Gen.  käntwis,  B  känfwo,  Obl.  käntwa  sa  {^kantwaj  um- gestellt aus  '^tankica,  idg.  *dnghua).
WP.  I  1792,  WH.  I  8U6f.,  Trautmann  104,  Specht  Dekl.  83,  Havers Sprachtabu  123  f.
cfö-  :  d9',  auch  dö-u-  :  dQU-  :  cfu-  ,geben^  (perfektiv),  Aoristwurzel  mit  sekun- därem    Präsens     di-dö-mi,     Nominaibildungen:    do-no-m,    dö-ro-tn^ dö'ti-s,    d9-ti-s    ,Gabe',    dö-ter-    ,Geber^,    Partiz.    dö-to-s,    dQ-to-s, 'd-tos,  Infinitiv  dö-men-ai,  dö-uen-ai. Ai.    dd-dä'ti  (Aor.  d-dä-m,   Opt.   deyäm,   Fut.  däsydti,   Aow  Med.  ddita ==  gr.    eöozo,   Inf.  ddmane  :  gr.  ööjxsvai,   vgl.   lat.  daminl,  falls   ursprüngh Infinitiv)  ^gibt*"  (päli  cZmna  zu  einem  Präs.  "^di-dä-ti),  av.  dadäiti  ds.,  apers. Imp.    dadätuv    ,er    soll   geben';  Wurzelnomen    ai.    dä[s]  dstu  ,dator    estu'; Infin.    dätum    (:lat.    Supin.    cZa^wm);    Partiz.    ditd-h    (unbelegt),    sekundär dattd-h,  schwundstuf,  in  ä-t-td-h,  prd-t-ta-h  ^hingegeben',  ablaut.  in  tvä-däta-h ,von  dir  gegeben',  av.  däta-j  zum  Fut.  ai.  däsyämi  (:  lit.  düosiu)  s.  Schwyzer Gr.  Gr.  I  78811;
arm.  ta-m  ,dö',  ta-m¥  ,damus'  {*dd-ie-mi)j  Aor.  etu  (==  d-dä-m,  idg. *e-c?ö-m);
224
gr.  öl'dco-^u  ,gebeS  Aor.  edcüVM,  Opt.  öoi7]v  (*donem),  Fut.  dwao),  Aor. Med.  l'JoTO;  Partiz.  doTÖg,  Infin.  hom.  öö^evai  und  hom.  tliess.  usw.  do'^jj, (su  ffixloser  Lokativ) ;
ven.  zoto  ,dedit^  =  gr.  eöoTO]  zonasto  ^döiiävit^  vielleicht  aus  *dönä-s-to von  einem  denom.  *dönäiö  (*c?ö?20-m  :  lat.  dömim)]  mess.  pi-do  (*dö-t:^[^ ■a-dät):
alb.  da-sh'd  Aor.  ^icli  g'aV  (*dd-S7n)]
lat.  döj  das,  dat,  dämus  (*dd-mös),  dätis,  dänt  (sekundär  für  *dent  aus *{di)-dn-ti),  alat.  danunt;  dedl,  dätum,  däre  ;gebe^  gewähre^,  refl.  ^begebe niich^  [das  mit  ä  nach  stä-  für  *c?ö  =  lit.  diid,  düo-h  [Specht  KZ.  55 182],  gr.  hom.  di-öio-d-i)',
vest.  di-de-t  ^dat^^,  pal.  cZi-<?a  ,det-,  mixCov.  dir sa,  der sa,  tera  ^det^  (*didät) tePtu,  dirstu,  titii  ^dato^  (*d{-de-töd),  tefte  ,datur^  {*di-da-ter)j  a-tef-a-fnst jCircumtulerit^  (^am-de-da-fos-t)-^  osk.  da\^da]d  ^dedaf^  (*däd(-di)-däd),  dadid ,dederit^  (*däd(-de)-did),
```


### [2026-09-05T20:09:19.902Z] TOOL RESULT

```
123:A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, Latin bonus, and Greek aga- thos have nothing to do with each other, and each is confined to its own branch of the family.
370:deu-'. To lack, be wanting. 1. Possibly suffixed form *deu-s- in: a. Germanic *teuzdn in Old English téorian, tyrian, to fail, tire (< “to fall behind”): TIRE}; b. Greek dein, to lack, want: DEONTOLOGY. 2. Suffixed form *deu-tero- in Greek deuteros, “missing,” next, second: DEUTERO-; DEUTERAGONIST, (DEUTERIUM), DEUTERON- omy. (For suffixed zero-grade form *du-s-, combining form of *dew-es-, a lack, see dus-.) [Pok. 3. deu- 219.] deu-2. To do, perform, show favor, revere. 1. Suffixed form *dw-enos in Latin bonus (> Old French bon, femi- nine bonne), good (< “useful, efficient, working”): Bo- NANZA, BONBON, BONITO, BONNE, BONUS, BOON?, BOUNTY; BONHOMIE, DEBONAIR. 2. Adverbial form *dw-ené in Latin bene, well: BENEFACTION, (BENEFAC- TOR), BENEFIC, (BENEFICENCE), BENEFIT, BENEVOLENT, BENIGN, (HERB BENNET). 3. Diminutive *dw-ene-lo- in Latin bellus (> Italian bello, feminine bella), handsome, pretty, fine: BEAU, BEAUTY, BELLE; BELDAM, BELLA- DONNA, BELVEDERE, EMBELLISH. 4. Possibly suffixed zero-grade form *dw-eye- in Latin bedre, to make blessed: BEATITUDE; BEATIFIC, BEATIFY. 5. Possible (but unlikely for formal and semantic reasons) suffixed zero-grade form *du-na- in Greek dunasthai, to be able: DYNAMIC, DYNAMITE, DYNAST, (DYNASTY); AERODYNE. [Pok. 2. deu- 218.]
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
410:dus-. Bad, evil; mis- (used as a prefix). Derivative of
411:deu-'. Greek dus-, bad: pys-. [Pok. dus- 227.]
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
```


## [2026-09-05T20:09:25.784Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dus-\" POK_01.txt | head -20; echo \"=== find page 227 marker ===\"; grep -n \"^227$\\|^ *227 *$\" POK_01.txt | head",
 "description": "grep Pokorny for dus-"
}
```


### [2026-09-05T20:09:27.519Z] TOOL RESULT

```
2605:Alb.  dhune  (*dus-n-)  ,Leid,  Schmerz,  Gewalt,  üble  Tat;  Schmach,  Be3 leidigung'  (dhunon  ,schmähe';  dhxn  ,bitter',  ursprgl.  ^unangenehm'?  oderj wie  sl.  gorhhb  , bitter'  :  goreti  ^brennen'?)  mit  *du-s-  (vermutlich  als  Tief-] stufe  eines  -es-St.  =  oder  wie  gr.  dä{J^)og)j  tosk.  dere  ,bitter'  (*deu-nO')]
2680:Ablautstufe  diu-  in  ai.  dyu-mndm  , Himmelsherrlichkeit',  dyu-mdnt-  ,hell, licht',  verbal  dyut-  ,leuchten'  in  dyötate,  i^Lor.  ved.  ddyaut  ,leuchtet^  (mit  t wohl  nach  ^vit-  ,hell  sein');  vgl.  auch  aksl.  d^zdh  , Regen',  russ.  dozd\  acech. deUj  usw.,  aus  *dus-diu-  , schlechtes  Wetter',  Trubetzkoj  Z.  sl.  Ph.  4,  62  ff.
3254:Ai.  dus-,  dur-,  av.  diLS-,  duz-  ,miß-,  übel',  arm.  t-  ,un-',  gr.  ovo-  ,miß-, übel',  lat.  in  difficilis  ,schwierig',  air.  do-j  du-  ds.  (lenierend  nach  dem Vorbild  von  so-,  su-),  got.  tuz-  (in  tuz-werjan  ,zweifeln'),  anord.  ags.  tor-j ahd.  2;wr-  ,un-',  slav.  in  abg-.  d^zdh  {^duz-djus  ^schlechter  Himmel'  ==)  ,Regen', russ.  dozdh,  poln.  deszcz^  aöech.  desc.  Gen.  dsce  und  analogisch  deH4.  Zu- sammenhang mit  deus-  ,ermangeln'  ist  sehr  wahrscheinlich.
3255:Erst  ind.  aus  dus-  entwickelt  ist  düsyati  ,verdirbt,  wird  schlecht', dusta-  ,verdorben,  schlecht',  düsdyati  ,verdirbt,  versehrt'.
=== find page 227 marker ===
3248:227
```


## [2026-09-05T20:09:31.031Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3244,3258p' POK_01.txt",
 "description": "Pokorny p.227 dus- entry"
}
```


### [2026-09-05T20:09:31.090Z] TOOL RESULT

```
WP.  I  821,  WH.  I  372,  Trautmann  60.
dregh-   ,unwillig,  verdrossen^,  oder  vielleicht  ursprünglicher  ,schlaff,  zähe^ sein^?  -^
Got.    trigo   ,Trauer,  Widerwille^,   anord.    tregi    m.    ,Trauer,    Hindernis'/^ tregr  ,un willig,  ungeneigt^,  treginn  ,betrübt^,  ags.  trega  m.  ,Trauer,  Leiden',  _
^s^-
227
treqo  m.  ^Schmerz^,,  tregan  (nur  Inf.)  mit  Dat.  ^leid  sein^,  mndl.  tregen ficu  Hut  verlieren^  auord.  trega  =  ags.  tregian  ,betrüben^;  vgl.  mit  einer '-olil  alten  konkreten  Bed.  ^zähe,  zähe  haftend'  norw.  radartl.  treg  auch au'=;dauernd^  fest^^  trege  ,zähe  Faser^  Sehne^  harte  Haut^,  ischwed.  trägen 'unermüdlich^;  dehnstufig-  ahd.  trägi  ^träge,  langsam,  verdrossen'^  as.  trag 'schlecht'^  ags.  trüg  f.  ,Leiden^  Übel';  as.  ahd.  trägl  f.  ^Trägheit,  Verdruß'; lit.  dryz-tü,  drizau,  drizti  ^matt^  schlaff  werden'  (Büga  Kalba  ir.  s.  219)^ drizinti  ^schlaff  machen';  zum  lit.  ri  vgl.  Hirt  Idg.  Gr.  II  83. Wr.  I  ^21  f.;  Persson  Beitr.  46  f.
dumh-  (-hh?)  ^penis^  Schwanz',  vielleicht  eigentlich  ^Stab'.
Av.  duma-  m.  ^Schwanz',  npers.  durrij  dumb  (*dum(}i)ma-)j  ahd.  zumpfo penis';  mhd.  zum2J>f{e),  zumpfelin  (Sütterlin  IF.  4,  93);  dazu  vielleicht  av. dumna-  n.  ;Hand  (?)'  (*dumbna-),  s.  Scheftelowitz  IF.  33,  142  mit  zahl- reichen Parallelen  für  die  Bed.-Entw.  ^Stange^  Stab  —  penis,  Schwanz' und  ,Stab  —  Arm,  Hand'.  Wohl  zu  mnd.  timpe  ;Spitze_,  Gipfel',  ags. atiinplian  ,mit  Nägeln  versehen',  nasal.  Form  von  germ.  *tippa  ,Zipfel' in  engl,  tip  _,Spitze',  mhd.  zipf[el)]  germ.  *tuppa-  ,Zopf'  in  anord.  toppr ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
WP.  I  816,  Fick  III  155,  164,  168,  Petersson  Heterokl.  70  f.
cfus-  ,übel,  miß-'  als  1.  Kompositionsglied.
Ai.  dus-,  dur-,  av.  diLS-,  duz-  ,miß-,  übel',  arm.  t-  ,un-',  gr.  ovo-  ,miß-, übel',  lat.  in  difficilis  ,schwierig',  air.  do-j  du-  ds.  (lenierend  nach  dem Vorbild  von  so-,  su-),  got.  tuz-  (in  tuz-werjan  ,zweifeln'),  anord.  ags.  tor-j ahd.  2;wr-  ,un-',  slav.  in  abg-.  d^zdh  {^duz-djus  ^schlechter  Himmel'  ==)  ,Regen', russ.  dozdh,  poln.  deszcz^  aöech.  desc.  Gen.  dsce  und  analogisch  deH4.  Zu- sammenhang mit  deus-  ,ermangeln'  ist  sehr  wahrscheinlich.
Erst  ind.  aus  dus-  entwickelt  ist  düsyati  ,verdirbt,  wird  schlecht', dusta-  ,verdorben,  schlecht',  düsdyati  ,verdirbt,  versehrt'.
WP.  I  816,  E.  Fraenkel  M^  Pedersen  453.
duei-  ,fürchten'.
Av.  dvaed-ä  ,Bedrohung'j
```


## [2026-09-05T20:09:37.418Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dus-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "grep WLD Bd1 for dus-"
}
```


### [2026-09-05T20:09:37.508Z] TOOL RESULT

```
10872:(Trautmann aaO.); apr. austo „Mund“ (n. plur.?; akk. sg. uustin). lit. dus- 
11317:„arm“ (su-, dus-op-smio-, Strachan BB. 20, S). 
48439:alb. (nach Jokl SB. Wiener Ak. 168, 1,19) dune ( *dus-n -) ..Leid, Schmerz, 
51476:dus- „fibel, miB-“ als 1. Zsglied. 
51478:Ai. dus-, dur-, av. dus-, duz- „miB-, fibel“, arm. t- (Hfibscbmann Arm. 
51486:Erst ind. aus dus- entwickelt ist dusyati „verdirbt, wird schlecht“, dusta- 
51781:Ohne Stiitze ist wurzelhafte Yerkniipfung mit idg. *dus- „miB-“ und 
53343:oder *dhstio- zu anord. dust; Berneker 248), eher *dus-dius, zu Praf. dus-
```


## [2026-09-05T20:09:38.370Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duž-aka\\|dužaka\\|duz-aka\\|dužuka\\|duzuka\" BRT.txt | head -20; echo \"=== col 755 ===\"; grep -n \"^755$\\| 755 \" BRT.txt | head",
 "description": "grep Bartholomae for duz-aka"
}
```


### [2026-09-05T20:09:40.180Z] TOOL RESULT

```
=== col 755 ===
13793:755
```


## [2026-09-05T20:09:42.802Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51470,51495p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD Bd1 dus- entry"
}
```


### [2026-09-05T20:09:42.852Z] TOOL RESULT

```
„penis“, mhd. z ump [(e), zumpfelm (Sfitterlin IF. 4, 93) ; dazu Yielleicht av. 
dumna- n. „Hand (?)“ ( *dumbna -), s. Scheftelowitz IF. 33. 142 mit zahl- 
reichen Parallelen ftir die Bed.-Entw. „Stange, Stab — penis, Sch\vanz“ 
und „Stab — Arm, Hand“. Oder zu mnd. timpe „Spitze, Gipfel“, ndl. timp 
„Semmel“, ags. atimplian „mit Nageln versehen"? 

dus- „fibel, miB-“ als 1. Zsglied. 

Ai. dus-, dur-, av. dus-, duz- „miB-, fibel“, arm. t- (Hfibscbmann Arm. 
Gr. I 495) „un-“, gr. Sva- „miB-, fibel“, air. do-, du- ds. (aspirierend nach 
dem Yorbild von so-, su-), got. taz- (in tuz-ioerjan „zweifeln u = „unglau- 
big sein“), anord. ags. tor-, abd. zur- „un-“. Curtius 5 239 f. Zusammen- 
hang mit deus- „ermangeln“ ist sehr wahrscheinlich, dagegen solcber mit 
*duou „zwei“ als „entzwei“ (z. B. Fick III* 169), oder *dau- „brennen; 
qualen“ (Fick I * 233) kaum zuzugeben. 

Erst ind. aus dus- entwickelt ist dusyati „verdirbt, wird schlecht“, dusta- 
„verdorben, schlecht“, dfisdyati „verdirbt, versebrt“. 

dlkii-(?) „sfiB w . 

Gr. yXvxvg „suB“, yXevxog „Most K , lat .dulcis „sfiB“ (Curtius 5 358), Gdf. 
unklar; sicher ist, daB gr. yX- aus dl- entstanden ist (J. Schmidt KZ. 25, 
153, Wiedemann BB. 13, 302; Sevxog ^yXeuxog 11 , devxrjg „ yXvxv g u mit 6 - 
aus dX- dissimilatoriscb in Yerbindungen wie *SXvxv yeh, vgl. Boisacq 179). 
Hirt Abl. 1 1 9 setzt idg. *doleuk- an, welchenfalls dulcis aus *dulucis. Dfirfte
```


## [2026-09-05T20:09:43.486Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13780,13830p' BRT.txt",
 "description": "Bartholomae col 755 region"
}
```


### [2026-09-05T20:09:43.528Z] TOOL RESULT

```
—  vupe  tJns9ntu  -^tf/ (NP.)'>  Yt. /^.jS;
—  vanätna  vtspe  'yus'^  (AP.)  Yt.  70. 34; Ny.j.  10;  —  nijan?  buye  vJspe  °ya  (AP.)^'
'  A.  7. 1 1 ;  —  *''ya  (AP.)  ^>  */ananbm  Az.  7;
—  paitiJaitJm  'yunam  Y.  ,57.  a6;  —  paiti.- jaitlm  'yavanqmS^  *YLro.ii,Vyt.25.  [Yt. 14.57:  streiche  du/mainyatt/^K]
mp.  drismhi.  —  PQ.:  dusman,  dusmFitisii.  — ')  Zweimal  ha.t  NA.  duim'.  —  »)  S^P^Nachtr. —  3)  S  407.—  1)  Them.;  s.  S  407  Nlr.  Vgl. auch  die  Var.  lu  Y.  5/.  26,  A.  /.  9.  —  S)  Ent- sprechend der  Lesung  von  F  l  usw. j.  duimainyü.jayanlam  hx.7:  \it%  dmmatttyü jananUm-,  s.  Sp.  490  u.
•  p.  dusiyär-  n.  'Missjahr,  Misswachs': imäm  dahyäum  mä  ajamiyl^  . .  mä  'ram (NS.)'>  D.^3;  —  imäm  dahyäum  c^ura''- mazdä  pätuv  hacä  kainäya  hacä  °ra'  D. 4.3.
Komp.;  *dui-^yar-,%370ii.'2\  \g\.  duiyairya- und  S  ^04  n.  9  No.  ~   ')  Them.
•  j.  duä-soDha-  Adj.  'übte,  böse  Sprüche sprechend.Verwiinschungen  aussprechend':
Hat  ml  ake  °nhake  paräca  valfaya  manS aal  ahe  ni  manS  manS  yö  ml  'nhs  hislaiU (sd.)  "so  wend  denn  ab  den  Anschlag des,  der  mich  verwünscht,  (mach)  zu nichte  Anschlag  um  Anschlag  des,  der sich  gegen  mich  in  Verwünschungen  er- geht" Y. /o.  12.
ai.  duhiamsa-  Adj.  —  Pü.;  diäiOA'aH,  SÜ.: du!t<uz»iräh.
•  j.,  g.  duä.8astay-  i)  f  'üble  Lehre, Misslehre':  '/ii  F.  j4'\  2)  Adj.  'des Lehre  übel  ist,  Misslehrer':  -ft'/  sravä mönndat  (sd.)  Y._?2. 9;  —  nöit  daibitlm 'iis  a/iOm  (si)  m^rasy^t  "nicht  soll  der Misslehrer  das  zweite  Leben  zerstören" Y.45.1.
Pü.  (dRn.)';  du^mSlilttlh,  pa  duiämöasriih,  duilh ämöxlär  (Sü.:  diifloHfyäpilä).  —  ■)  Stammt  vll. aus  Y.  32.  9,  s.  2  und  Pu.
dby  Google
755
tiuI.sravaA-
duzuxta-
756
•  j.  dus.sravah'  Adj.  'der  einen  üblen Rur,  Leumund  hat,  Su7KXr)j^.
Ableit.  (s.  auch  diuLir').
•  j.  duS.sravahyä-  f.  'Übelberiichtigtheit, übler  Leumund':  'vaMi  (NS.  oder  IS.) Y.i4.
Ableit.  aus  '*diä.sriaiak-.  —  Vgl.  lOuijravah:
—  Pä.!  dulsriw-ik,
•  g.  duä.syaoft'ana-,  j.  "Diia-  Adj.  'des Tun  Übel  ist,  des  Taten  Übel  sind':  dui- manatihe  .  .  Jusva/ar^Ae  .  .  *'^ftai'*  Y. tfj.  7;    —  yOnS  .  .  'hnaAe  H.  2.  36;    —
'haiiing  duivacatihs  duidalnSng  *duimana' nhs  y.  4:p-  1 1 ;  —  yai  .  .  '^ans  (NP.)  Y. 34.');  —  dngvaiti . .  °^anai  Y.31. 15. Pü. :  duliunün.  —  0  NA.  '%iiitäi.
•  j.  du§.-ha,m.sästa-  Adj.  (fem.  '/ä-) 'schwer  zurechtzuweisen,  unlenksam':  näi- riiayäi  . .  AusJtam^äsfqyHi  .  .  jahikayäi  .  . 'tayäi  H.  2. 18-36.
SQ.:  äuiämSxt.
•  g.  duS-x^araS^-  n,  'üble  Speise"*; dar>gim  äyü  (sd.)  timanks  *°'i3m  ''. .  üble Speise"  Y.31.  20;  —  vaya.b?r?dubyB  (sd.) '%Sm  Y.5;.  6.
Pu.:  äuS^ariSn,  mit  denErl.!  tui x'ariSn  i  vat äahmd  und  kid  vUaia  (in  Aw.-Buchst.,  aus H.  2.  36)  dakend.  —  ')  Wie  sie  den  Seelen der  Gottloien  gereicht  wird;  s.  V.  4g.  11, H.  i.  36.
•  j.  duä-x*ar9nah-  Adj.  'übelberüchtigt': 'na  (NS.)  naStS  rasüta  asätS  asti  anuhaya (sd.)  Yt.  10.  105;  105;  —  alsmö..  "na  Yt. ^9-  95  i  —  ""''  *w^  mainyui  Vyt4S-
•  }.,    g.    dui'    Adv.,    nur    KompA.:    s.
dui\
•  j.  duzaka-  m.  (gemeiner  oder  Spott) Name  des  sfis  va»AaparS {'\gi\')*^:  spämm .  .  yim  vankäpanm  (sd)  yim  tnasyaka avi  duzvacanhS  'k>m  nama  aojaitt  V.  ig.  2.
*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
*sayana-Ti.,  lum  V.  jiiy- ;  ai,  inj'««.!- n. 'Lager'
—  ['iL:  duliilya/:')  'mit  schlechtem  Schatten'
erl. :  mm  säyatJA  l  hi  *s3yai  1  draxiän  pa tan  val  asi;  dazu  als  Glosse:  {ait)  ii  äii  i iSfän  gffmtt.  —  ■>  Ohne  Berechtigung  vermutet FkMOller  WZKM.  4.  ZÖ2  deshalb  ein  urspr. ahÖjay*y
•  j.  duz-aohav-  m.  'Hölle':  spmt>m  main- yüm  haca  raox^a  garö  nmäna  .  .  a/^rtm mainyäm  »nyata  haüa  'iawAi/'' Yt  Jp.  44; —  aHihm  -ianhavö  (GS.)  P.  i4.
Ableit.  (s.  daBi'\  —  Eig,  'schlechtes  Sein'  sva. 'Ort  des  schlechten  Seins',  s.  Sp.  109  m. ; falsch  BB.  15.  209.  —  Pü.:  */  an  1  vat  ajr*" ääret.  —  >)  Statt  'iaifuha  (S  268.  30),  IS.  wie xri^taa,  %  40^.
•  j.  dui£-anay-  Adj.  'der  einen  üblen  Atem, d.  i.  Geruch  hat' :  macirinam  artukanam  . . 'aininqm  V.  14.  5-
Zum  V.  an-,  —  pa.:  di^amün.
•  g.   du^-azöbä-  Adj.  'übelberufea,  be-
riichtigt":  dr^gvä  .  .  'bä  (NSm.)  Jias  a^üis lyaolianais  ähSmuits  (sd.)  Y.46.^.
ö  ist  Fjnschubvolcal,  S  JOO.  5.  —  'a-itä-  f., lum  V.  tiä-i  ai.  äAvä-  f.  -Name";  GON.  BB. 14.  II').  —  Pü.:  dusilaxmai.  —  O  Andre, mir  unglaubliche  Deutungen  bei  Mills  SBE. 31.  136,  G.  551,  JusTi  NB.  337,  PrJ.  **  345-
•  j.  duz-ä*ra-  n.  '(schlechtes  Atmen  sva.) Miäsbehagen':  ravash  :!fä'hnmca..asaonö stBii  qzasca  'nmia  .  .  drvatS  stuis  Y.  <V. 8.  a)  'Not,  Ungliick':  aha  apare  (sd.) ayan  'r^m  Aog.^;?.
Pü.:  duii^ärlA,  Sii.:  ahdAant.
•  j,  duzäpya-  n.  'Schwer-,  Unbeikömm- lichkeit',  mit  Akk.  (des  Obj.):  yaesam anhat  'fim  änval.psntum  "für  welche  die (^-Brücke  schwer  (beikömmlich,  sva.)  _un- überschreitbar  sein  wird"  V.  y,  3.
Ableit.  aus  'dui-äfa-  Adj.  'dem  man  achwer beikommen  kann';  zumV.  a/-;  ai.  .l'urä^- Adj. —  Pii.:  *dulayäfai.  —  ')  W6rtl.:  'quorom  erit insaperabilitas  . .'.
•  j.  diiz-ita-  i)  Adj.  a)  'schwer  gangbar, schwer  zugänglich':  upa  kvirint^m  *t»m Yt.  J5.  19.  b)  'gefUhrlich'  (nur  Ab- leit.) 2)  n.  'Schwierigkeit,  Not,  Gefahr': bdiwranam  'latiqmca  .  ,  %walsä  (sd)  Yt 13.20.
Ableit  —  ai,  dunlä'  1)  Adj.  'schwierig',  i)  n. 'Not'.
i  j.  duzitctara-  Adj.  'der  gefährlichere':
'tarasea..ydha  anya  v^Aria  V.  ij. 4^;  4a-
```


## [2026-09-05T20:10:17.010Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== duzda / duzdao ===\" && grep -n \"duzdä\\|duzda-\\|dužda\\|duzdaw\\|duzdä-\" BRT.txt | head -20; echo \"=== dus-manah ===\"; grep -n \"duS-manah\\|dus-manah\\|dusmanah\\|duimanah\" BRT.txt | head -10; echo \"=== dus.naman ===\"; grep -n \"dus.näman\\|duS.näman\\|dus-nama\\|duinäman\" BRT.txt | head",
 "description": "grep Bartholomae for duzda, dusmanah, dusnaman"
}
```


### [2026-09-05T20:10:17.095Z] TOOL RESULT

```
=== duzda / duzdao ===
11707:•  ].,  g.  tä  Adv.  a)  im  gAw.:  1)  'in  Folge dessen,  deshalb',  zurückweisend:  ävs  da- msi^  drüjd  Aunul  ta  duzdä  (sd.)  ySi  hfiiix V-Si.  10;  —  ai/a  ahmäi  varmäi  . .  nidä- Um  ai>m  sütdyäi  ikaisäi  (sd.)  räsayaihl druxsta  vanAfus  sarS{sd^  *izyS  manar?hä Y.  4p.  3;  —  yastä  dam^ng  .  .  tarS.mqstä Y.45. 11;  5;.  z.  z) 'damit,  so';  a)  zu- rückweisend: tä  drigvats  *mar»daite  daotä *»r?aaos{&A.)  haihim  Y.JJ,  13.  b)  voi^ ausweisend,  mit  folg.  Ayat  'damit . .  dass; indem':  nsil  tä  im  x/näus  vai^5  (sd.) zardiustnm  .  .  Ayat  aAmf  urüraost  asts Y.j/.  12.  3)  'in  dieser  Weise',  voraus- weisend, mit  folg.  _>'3  'iUi..  vV :  yü/ yOita /ramlmdiä  (sd.)  yH  masyä  oHstä  dants 'axhntl  daivB^tustä    Y.  32.  4.  b)   im
20531:*drazimnö  Yt70.  gsf.;  15;  —  aat  äbyB döi^mbyS  .  .  a<,aoyB  asti  °rff  yB  balvar^.- spasanB  ,  .  Yt/o.  81;  —  'mm  y7  paoiryB tarö  harqm  asnatiiti (sd.)  paurva.natmäi.. kü  yat  auniatjtspa/ie  . .  ahäi  vüptm  ädi- haiti  Yt;o.  13;  — gairinqm  asasflüfrattqm *äsnaeiti  (sd.)  'rsm  (statt  NS.)  AuzaOum V,  7p.  28;  — yttiAf  asta  rätayB  vupahu paiti  banzahu  spasB  äahäire  'rahe  Yt 70.45;  —  ''^"^  -  ■  yeÄhe  paurva.nal>i>3t vazaite  vrn^rayt^  ahur«i'MltBY\.io.-;o;  — yat  duzdä  fradvaraiti  . .  %wäs>m  *yi//yeiie vahm  'rB  Vt70.  52; — yal  'rö  fravazaite avi  haüiayä  xrri/yäti/  .  .  a^ra  narqm mi^rBJrujqm  apql  gavö  darfzaydti  Yt 70.48;  —  ui^ojanä  'räi  .  .:  äi  'ra  .  . ime  HB  .  .  aspa  para  *'ra  *i3a'*  aayetite ime  nB  *wyra  bäzava  karata  'ra  sHnda- yeinti;  pascalta  dis  fraspayäti  'rB  Ytio. 4a  f.;  —  'r^m  .  ,  yetihe  ,  ,  bäzava  fra- griwmü  "mi^rBMüjauhB  (sd.)  .  .yatHt  vi- maibJm  (sd.)  airiha  zamS  t?mat  'rö  han- gn/simiiö  *pairi.apaya  (sd.)  Yt/0.  I04£; I —  'rB  zayüt  (iÄ^  sara%u3r?m  Y.g.i PUZ.         a)  bes.  mit  dem  Beiwort  z'ouru-
=== dus-manah ===
13772:•  j.  duS-manah-,  g.  *duz-manah-"  Adj. i)  'des  Denken  übel  isf:  dusixldkrSng duS.ryadhanSng  dusvacarihS  duidalnSng 'nar3As^'>  dngvats  Y.  4jg.  11;  —  °na>jhe  . tütivacanhe  .  .  ^dul'.syaoä^nili  Y.  6^.  7 ;  — yBnS  AumanavAS  .  .  yäni-    'nanl^   H.  2.
=== dus.naman ===
```


## [2026-09-05T20:10:18.550Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dušox\\|dwšhw\\|dušax\\|duzax\\|dōšox\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20",
 "description": "grep MacKenzie and Nyberg for hell"
}
```


### [2026-09-05T20:10:18.611Z] TOOL RESULT

```
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:2254:hell dušox, dwārišn.
PHD.txt:2255:hellish dušoxīg.
PHD.txt:5415:duSoxig dušox dušxwaršt dušhumat gūšūsrūd dušxwadāyīh dušāgāh dušāgāhīh dūšāram dušarz dušīh dujdānāg yojdahr yójdahrih yojdahrgar yējdahrgarīh dujdén dušgēwišn dujgand dujgandīh dujdēysšrīh dūšīzagīh dēšīzag dujdatt
NYB_vol2_glossary.txt:1326:dēšax" [dwšhw'] hell 2015, 347-27, 6512.18 etc. passim; andar ~ 251%, 2813. 318, 617. 6811; pat ~ 768-1, 8419-20, — Av, (675) daožahva-; MPrth dwjx; MPrs dwswx; Arm. lw. džox-k'; Paz. dēžax, NP dózaa.
NYB_vol2_glossary.txt:1390:duš-humat [dwšhwmt'] Evil Thought, the first stage down to Hell 75%, — The neg- ative of humat (q. v.). Cf dušmat, which Paz. found here.
NYB_vol2_glossary.txt:1391:duš-huvaršt [dwšhwwlšt'] evil deed 641. 651°; Evil Deed, the third stage down to Hell 75°. — The negative of huvarst (g. v.). Av. (759 sq.) duž-varšta-; Paz. duž-
NYB_vol2_glossary.txt:1394:duš-hūxt [dwšhwht'] evil speech 63°’. 6510; Evil Speech, the second stage down to Hell 7524, — The negative of hüxt (q. v.). Av. (756 sq.) duž-ūxta-; Paz. dūžūst corresponding to Phl *dusüzt. duš-kām-kartārēh [dwSk’mkrt’lyh] bad exercise of authority, outrage, violence 7211. — Cf kam.
NYB_vol2_glossary.txt:1407:duš-x"ār [dwšhw'l] annoying 4%. — The antonym of z"àr (g. v.).
NYB_vol2_glossary.txt:1410:duš-x'atāyēh [dwšhwt?dyh] evil kingship, government; misrule 1%. 11624,
```


## [2026-09-05T20:10:26.993Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 147 (p126) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==148' HRN.txt | head -60",
 "description": "Horn p.126"
}
```


### [2026-09-05T20:10:28.732Z] TOOL RESULT

```
=== HRN leaf 147 (p126) ===
— 126 -
504. duzd *Dieb', diizdl, dtizdlden.
g. diizadmün *stelilen*, duz 'Dieb'.
aw. duzdäo ^Bösewicht'; phlv. duz (geschrieben duc;
Kommentar für aw. täyu-), diizTh (Mön.), didd,
duzditan (geschrieben duct" ; AV.), duzdlha (geschrieben
duct"; PPGl.), dtizdU (geschrieben dfutU; Bund.), päz.
auch überall dMzd",
LW. (?) kurd. diz *Dieb', dizhi 'stehlen'; bei. duz,
diizl (88).
np. duzd stimmt lautlich ganz genau zu aw. duzddo
(zu z aus z vergl. np. miizd^ ^mizd 'Lohn gegen aw.
mizda- und zu dem Abfall der Endung np. Hor]muzd
gegen aw. Mazdäo). Im Fehle vT ist überall z zu lesen
bis auf die junge Form des Bundehes; duz^ duzJh sind
dann schon noch jüngere Formen.
505. duS', duS' {diz-, dez-) *übel, böse'; vergl. dust (Bahn.
I, 15 Vers 38).
ap. dus-; aw. dtis-, duz-; phlv. dws-; ai. dus-, rfwr-;
gr. Ovo-; arm. LW. dz-, echt ^ (H. No. 267).
Mit duZ'j dtiS' gebildete Composita, deren Zu-
sammensetzung vollständig durchsichtig ist, wie
duz/lm, dmnüm, dmmen sind im Folgenden nicht
aufgeführt.
560. deSe ^Siegel*.
aw. i^daJ/Z', dazaiti Verbrennen'; phlv. dazitan; ai.
[/dali- ddhatl 'brennen, verbrennen',
bei. n. diday, pp. da/fa 'brandmarken' (433).
507. dest 'ITand', vergl. destek^ deste (arab. dastaj ^)), destl
'Hilfe'.
ap. dasta- Hand'; aw. zasta-; phlv. dast; ai. hdsta-.
Allgemein entlehnt: kurd. dest; afy. las (Darmeste-
ter, LXIII, Npte) , dast; bei. dast (51); wa;^. ^ast,
siyn. döst, sar. düst, sangl. dast, minj. last, yidg. lust.
508. destur 'Minister, Vertrauter; Verhaltungsmassregel,
Vorschrift'.
') (^Iml.l. LW. pppi, arm. LW. (htsfnk.
```


## [2026-09-05T20:10:37.710Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN p129 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==151' HRN.txt | head -50; echo \"=== HRN p152 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==174' HRN.txt | head -50",
 "description": "Horn pages 129 and 152"
}
```


### [2026-09-05T20:10:39.597Z] TOOL RESULT

```
=== HRN p129 ===
- 129 -
af/. dvalas; oss. d. duades, t. duädäs.
Die neupersische Form (eine Analogiebildung) ist
entlehnt in kurd. duänzdih (hier findet sich noch
ausserdem das n von np. sänzdeh), hol. duäzdeh,
oll. (\)dö%ten *anheften, durchbohren, nähen', Praes.
döz-em, döz, dözene, kun\döz grosse Nadel' (AM. 52
ZeUe 6, 116 Zeile 2 v. u.).
maz. düj, düjene,
phlv. döc *Speer (Dat. d. 21, 8), phlv. pjiz. dö/tav,
dözEm (PPGl.)
oss. än-düzün, d. än-dozun ^befestigen (von
Stackeiberg, ZDMG. 43, 671); bei. dööag , n.
dösay *nähen (91).
578. (2)döy(ten 'melken', Praes. dös^em, dösTden, döy saure
Milch' (AM. 216 Zeile 5) ').
ai. [/"döh-, dogdhi 'melken', dögha^; phlv. dö/fan
(Bund.), dösUan (Bund., PPGL).
kurd. dötifiy düsim, di-dösim melken'; afy. Ivasal;
oss. d. docufiy t. dücifi (111); bei. dösay (94); wa;^.
dtc-am^ dögnam, sar. dauz-am.
579. dFfd 'Rauch', diidmän 'Familie.
phlv. dfit 'Rauch', dütahnan (AV.), vorgl. dütal'
'Familie' Bahmyst (Spiegel, Trad. Lit. S. 4()G); ai.
vergl. dhümä' 'Rauch'; lat. //7mMs, lit. diima-s, ksl.
dymü,
kurd, du; af/. lü; bei. düt, dlt (90); wa;^. dit, sijn.
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
Hör II, Qrundriss d. neup. Etymologie. 9
=== HRN p152 ===
- 152 —
z.
684. £äle 'Hagel, Keif.
Ri.hrädünl' 'Hagel'; gr. ;faAa^a; hdt, (jranclo; ksl.
fjradü.
Nöldeke (mündliche Mitteilung). Neupersische
Grundform *zrade^ *zärde.
Diese Etymologie verdient vor der meinigen (KZ.
32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
los den Vorzug.
685. Serf 'tief*, PJniT (Is. 29, 15 ^), zerfi;.
aw. jfafra- 'tief; phlv. zufar^ zafr.
kurd. ziör, zaza /ör; afy. zavar; bei. juhl, n. jahl
(178).
686. MobTti, zöpm-), zöpin 'kurzer Speer (in Gelän bezw.
Delem gebräuchlich)', pDIT (Jer. 50, 42).
LW. ^ißvvt] (^Cvßivrj) etc. , arm. suin , syr. JOID
(de Lagarde, Ges. Abh. 67).
Die Herkunft des Wortes ist dunkel; vergl.
Hübschmann, ZDMG. 46, 250 No. 110.
687. zü$e 'Igel'.
mäz. arzarnldijl (?) ; g. jujlk,
aw. duzaka- Igel' (als Schimpfname des Hundes
verwandt) ; phlv. zUzak,
kurd. LW. arm]ijl (H.-Sch.)?, züzl (J.-J.).
S.
688. süyfeii 'machen, ausführen', Praes. säz-em, säz 'Gerät*.
Käs. Q. bäsöj, K. lesöj.
aw. i/^saC' , mit aiwi 'darbringen , ausführen
{yasnenif ; phlv. säxtan, sac(i)sn.
*) Nach Castle (bei Vullers) ,7V/.
2) Vis und Rämin, S. 49 Vers 15; z^^n^ S^*di, Bostän, S. 127
Vers 878.
```


## [2026-09-05T20:10:52.146Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -20 BQT_v2_pages.txt && echo \"...\" && grep -c \"\" BQT_v2_pages.txt && grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5 && grep -n \"\\[pdf page\" BQT_v2_pages.txt | tail -3",
 "description": "Inspect BQT v2 pages file"
}
```


### [2026-09-05T20:10:52.217Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬‬
‫‪ ۰‬و زل رسوا »وا روون لات سا روصا مواقم‬      ‫وتان‬

                      ‫‪۴2 ۱‬‬

                  ‫رک یمن‬
                  ‫م سارو کی و ررك‬


                 ‫جلررومدا‬
             ‫چاپ دوم فروردین ‪۳۴۳۱‬‬
                 ‫با تجدید نظر کامل‬
          ‫بسرمایه کتابفروشی ابن سیتناپران‬
...
41071
```


## [2026-09-05T20:10:56.563Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json,glob\nfor f in ['page-127.json','page-125.json','page-124.json','page-123.json']:\n    d=json.load(open(f))\n    s=json.dumps(d,ensure_ascii=False)\n    import re\n    for m in re.finditer(r'\\{[^{}]*\\\"BQT\\\"[^{}]*\\}',s):\n        print(f, m.group()[:400]); print()\n\" | head -40",
 "description": "See how BQT was cited previously"
}
```


### [2026-09-05T20:11:17.639Z] TOOL RESULT

```
page-127.json {"src": "BQT", "where": "leaf 338 = printed p.878, s.v. دماوند", "stance": "contradicts", "note": "Moʿin's footnote ۵: «دماوند که در مآخذ اسلامی \"دنباوند\" آمده، بنا به تحقیق مرحوم کسروی … مرکب است از \"دما\" (ضم دال) بمعنی پشت و دنبال، چنانکه \"نهاوند\" نیز مرکب است از \"نها\" بمعنی پیش … جزو دوم در هر دو نام \"وند\" پسوند …» — i.e. Damāvand belongs to the dumb 'tail, rear' root, not to dam 'vap

page-127.json {"src": "BQT", "where": "leaf 347 = printed p.887, s.v. دن / دنه", "stance": "partial", "note": "p.887 has «دن ‑ … در زیر لب آهسته آهسته با خود حرف زدن باشد از روی قهر و غضب» and, separately, «دنه … و بمعنی نعمت دنیوی و شادی ‑ و صدا و ندا و زمزمه از غایت خوشحالی هم آمده است» — the 'joyful shouting' sense belongs to دنه, not to Nourai's headword دَن."}

page-125.json {"src": "BQT", "where": "BQT_v1_pages.txt / BQT_v2_pages.txt", "stance": "silent", "note": "grep for بوتیک/پرانتز/تم returns nothing usable; Borhan-e Qate' is a 17th-century dictionary and cannot contain modern French loans."}

page-125.json {"src": "BQT", "where": "BQT_v2_pages.txt (Borhan-e Qate', د section)", "stance": "silent", "note": "grep 'دده' over the Borhan OCR returns only broken OCR fragments of other words; no usable دده article, so Mo'in's footnotes there could not be read."}

page-124.json {"src": "BQT", "where": "vol.1 p.418 s.v. پنام (leaf 644)", "stance": "supports", "note": "the headword, the Shahīd Balkhī couplet, and Mo'in's footnote deriving it from Av. paiti-dāna / Pahl. padām."}

page-124.json {"src": "BQT", "where": "vol.2 p.814, footnote to داستان", "stance": "supports", "note": "Mo'in's footnote reads the word as Pahlavi dātastān 'حق، قانون'."}
```


## [2026-09-05T20:11:24.794Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 310 313 327; do echo \"########## leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -60; done",
 "description": "Print BQT v2 leaves 310,313,327"
}
```


### [2026-09-05T20:11:26.480Z] TOOL RESULT

```
########## leaf 310
 ‫دربو‬                                                                                                  ‫‪٩‎‬و‬

‫و کردا کرد خانه واطراف هرچیز رادز کفته‌اند‬                ‫در یم د بکراول وانی‌سحتانیمجهول‬
‫در انداژند تا در کشوده‬        ‫و چوییکه در پس‬             ‫طمه ابست که آبرا‬
                                                                        ‫کشده و یفن نقطه دار زده »‬
          ‫لگردد ؛ ویکراول هم مده است `‬                    ‫درمقام تأسف و حسرت کویند ‪ -‬وبمعنی افوس‬
                                                           ‫شتته‬‫ذا‬‫گصیر‬
                                                                    ‫واندوه ودشوار واندوه کردن بر تق‬
‫در بور ‪ ۴‬هبسر وزن هر روز ‪ ۰‬بمعلی‬
                                                                     ‫باشد؛ وبضم اول هم بنظرآمده است ‪.‬‬
         ‫و کدابی باشد ‪.‬‬       ‫به‬
                               ‫کتدکه‬
                                   ‫دربوزه ام‬

‫در بوری ‪ = ۴‬بروزن هرروزه » بسعئی‬
                                                          ‫دریگان ‪ ۱‬بااك مجهول کواف‬
                                                         ‫فارسی بروزن حریفان ‪ ۰‬نوعی از اعمال و اشکال‬
          ‫دربوزاست که کدبه و کدابی باشد هة‬
                                                                  ‫فجومی باشد » ومعرب آن دریجان است ‪.‬‬
‫در بوش ؟ ‪ -‬بروزن خر کوش کدا‬
                                   ‫‪a‬‬


                                                         ‫در یو اس (‪)١‬ہ‏ با الك مجهول وواو‬
                  ‫ومسکن را گونند ‪۰‬‬          ‫ودرورش‬
                                                          ‫بروزن بلیناس » چارچوب در خانه راکویند =‬




                                                                          ‫)‪ (۱‬چش ‪ :‬دربوای (‪)۱‬‬

  ‫درکان ‪ 202606۲‬درهندوی‌مر کب از‪( ۱۲ = 1۲1 :‬ے) ‪ ( 20۵۷ +‬بخش»‬                                       ‫‪۱‬‬
 ‫بیرولی درتحقیق ماللهند(ص‪ )۷۰۳‬کوید ‪ 2:‬الا ثلاثو نسمی دریکان ولافائدة‬                 ‫بپر) * نی سه‌بهره‬
  ‫فی‌ذ کرها لانها ای تسمی عندنا دربجانات سنها؛‪ .‬وهمو درالتنهیم (س ‪ )4۰4‬آرد‪«:‬دریگان‌چست؟‬
 ‫وخداو ندانثان بخلاف و حوه»‬    ‫‪ ۰‬ومردمان ما آ را در بسجان‌خوانند»‬      ‫برجهااند نزديك حندوان‬            ‫هم سك‬

‫يدجم برجرا ازاو ‪ 1‬وسوم‌خداو ند‬         ‫خداوند‬    ‫ازهر برجی خداو ندش راباشد ‪a‬‏ ودوم‬   ‫دریسجان‬       ‫نشتین‬     ‫که‬


  ‫هم را» وسپس بیرونی جدول خداوندان وجوه ودریگان رائت کرده است ‪ .‬رك ‪ :‬التاهیمص ‪404‬‬
        ‫رك ‪:‬درنوژه ‪.‬‬      ‫‪۳‬‬             ‫‪.‬‬   ‫‪۷۳۳‬‬    ‫مورك‪ :‬تقی زاده‪ .‬گاه شماری ص‬       ‫(متن‌وحاشه) و‪۵*4‬‬

            ‫‪.‬‬   ‫رك‪ :‬دبروزه‬     ‫‪۴‬‬             ‫‪.‬‬    ‫دربوز = درىوش‬     ‫درویزه سس رویز‬       ‫‪= ۳‬‬


                                                                                      ‫بقه اصزفحهة ‪۸4۸‬‬
                                         ‫زی)‬
                                           ‫مر‬‫‪ #‬ودراجه ‪ -‬بفتحاولو کر يلجم ( درلپجة ک‬

                                        ‫از دربا ‪ +‬چه( پود نسنیر ) = دریاژه حدو«دالمالم ‪۱۱۰‬‬
                                                                                               ‫‪۰‬‬        ‫و‪۸۹‬‬




                                       ‫فگرروفتن ‪ ۶:‬اماچون شراب دربافت وبخفتند خماری منکر آرد‬
                                        ‫که بیدارشوند و دوه روز بدارد؟ «بیهقی ‪۵-٩‬‏ ‪ -‬چاره کردن‪.‬‬
            ‫درناچه‬                      ‫جبران وتلافی کردن ؛ استدراك »تدارك‪ « :‬واگر جانبی را خللی‬
                ‫نامه و صوار دربافتندی» «یسهعی ‪ *۵‬ت فهسدن ‪ 1‬معلوم کردن ‪ 0‬ادر ال ‪۲‬‬                       ‫افتاده ودی‬
########## leaf 313
                                                                                                                        ‫جد‬
      ‫ح‬
      ‫ب‪ ۷‬ی‬                                                                                                           ‫درا لون‬



‫دلنواز» بمعنی زشت خوی ‪ -‬وبدلما و لا زیبا ‪-‬‬                                 ‫‪۰‬‬   ‫وقهر آ لود باشد‬       ‫ومهم ناك‬        ‫خشمگین‬

                                                                                                                 ‫~~‬
‫وخشم| لود وسهمگین ‪ -‬وخام طمعوعیب جوی‬                            ‫در | لون ‪ -‬بروزن طلا کون ‪ ۰‬تمعتی‬
‫باشد ؛ وبفتح انوفلزدرست است ؛ وبابای فارسی‬                      ‫حیف ودریغ وافوی باشد ودرمۇ‪,‬دالفضلا بهمین‬
                          ‫هم امده است ‪.‬‬
                                                                ‫ممنی بعد از واو الف نوشته بودند که دژالوان‬
‫دز براران ‪ -‬و داژتیر‌ابنابای ابجد‬                                                                                        ‫باد ‪.‬‬
‫‪ ۱‬است که بمعنی‬              ‫از‬
                             ‫رجمم‬
                                ‫بی ‪.‬‬
                                   ‫ژارس‬
                                      ‫دای ف‬
                                          ‫وب‬                ‫نظام‬    ‫فارسی‌بروزن‬       ‫ماف‬   ‫‪a‬‏‬   ‫‪۱‬‬    ‫درانگاه‬


               ‫عیب جوبان ولا‪.‬زیبایان وغیره بلشد ‪.‬‬          ‫و خشمآ لود‬          ‫گاه‌است که سهمگین‬               ‫بمعنیدژآ‬    ‫شاه“‬



‫دز برو ‪ = ۴‬بکراول‪ ۸‬وسکون انی‬                                                                                    ‫وقپر ناك باشد‬


‫واو ساکن » خشمگین‬
                ‫وضم الث ورای قرشت و‬                         ‫بهفتح ها و سکون نون‬                      ‫هرن|ح؟‬
                                                                                                       ‫‪۰‬‬

                                                                                                          ‫د‬      ‫‪2‬‬   ‫ب‬




‫وقپرآلود گوره برایرو زننده راگونند » ویفتح‬                      ‫وجدم» بدخوی وخشمگین وسپمناك ‪ -‬وکبرددار‬
                             ‫اوز ‪ ۸‬هم درست است ‪.‬‬                ‫باشد ‪ -‬وبمعنی‌تیر تخش ‪ -‬وژوبین (‪ )۱‬که سنان‬
‫دز بسن بتح اول ‪ ۸‬سین بی‌نفطه‬
                                                                ‫دهرن|گه ‪ « ۴‬باکاف فارسی بروزن‬
                                                                                                                     ‫و‬
‫بروزن سربلند ‪ :‬بمعنی‌زاهد وپرهیز کارباشد *‪.‬‬
‫کله بای‬
      ‫د‪۰‬ر‪ 94۳‬بکر اول ‪ ۸‬و تا‬                                 ‫و بد کردار‬          ‫و معنی دژآهنج است که بخدوی‬

‫فارسی‌باشد وسکون انی وهای حوز(‪ )۲‬گرهپابی‬                        ‫‪-‬ژویین(‪)۱‬‬
                                                                        ‫وخشمناله وسهمگین ‪ -‬و تیرتخش و‬
                                                                                               ‫باشد ‪.‬‬
‫رگوابند که در میان گوشت و پوست آدمی‬
‫»‬    ‫وحوانات دیگر میباشد » ومربی غگدودنند‬                       ‫دز ]هنگ افراسیاب ‪ ۴‬م غاری‬
                             ‫وبفتح اول نیز گفته‌اند ‪.‬‬                   ‫بود که افراسیاب بدانجا کربخته بود ‪.‬‬
                                                                                                           ‫‪۰‬‬         ‫‪۳‬‬
‫دز په ‪ ۲‬بکراول ‪ ۸‬ثوالك وسکون‬                                    ‫سفتح بای ابجد بر وزن‬
                                                                                   ‫در برار ِ ب‬

                                           ‫‪ :‬وها ‪.‬‬   ‫چك‬   ‫(‪)۲‬‬                         ‫)‪ (۱‬چك ‪ :‬زوین ‪۰‬‬


########## leaf 327
          ‫تا‬                                                                                                                             ‫دشتان‬

‫تن‬       ‫سوزن کشند‬          ‫که هر‬      ‫را گوند‬            ‫تایده‬    ‫رشته‬
                                                                                             ‫وبضم اول بمعنی بد وزشت بود ‪٩‬‏ ‪.‬‬
‫کسر‬       ‫اول و‬   ‫وسم‬       ‫را همکفته‌اند ؛‬           ‫خام‬    ‫و ربمان‬
                                                                             ‫تانی‬     ‫سکون‬   ‫بقتح اول و‬             ‫‪ ۴‬ت‌‬   ‫دشتان‬

‫نزرامده‬      ‫فارسی‬      ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
                                                                             ‫وفوقالی‌بالف کشیده وبنون زده‪ .‬حالض‌رامی‌گوبند‬
                                                                   ‫ان‬
                                                                                               ‫یعنی زیکه خون حیضش آید ‪۰‬‬
‫‪ ۰‬رسمان‬           ‫خشکی‬       ‫‪ ۰ ۸‬بر وزن‬               ‫دشکی‬
                                                                             ‫بضم اول بروزن بدتی » زلورا‬                        ‫دشتی‬
‫خامی که زتانر سند و مردوك مانند تنضه بنخده‬                                   ‫جون‬      ‫رنگه ‪,‬‬   ‫آن کرمی باشد سیاه‬                     ‫و‬   ‫گونند‬

‫وفرموله خوانند‪.‬‬              ‫ی‬    ‫وان بفه مانندرا دب‬                ‫شود‬      ‫بر عمنوی از اعنای آدمی بح یانند خون ازان‬
                                                                                                                                            ‫ا‬
          ‫باشد شبیه بماش وبعربی درجم خوانند ‪۶#.‬‬
                                                                                      ‫بمعنی بدباد لمودن وغیبت کردن ‪ ۴‬باشد ‪.‬‬
                                                      ‫‪۰‬‬    ‫ار ان است‬         ‫وواو‬     ‫شف‬   ‫با خای‬            ‫ار )‪۱‬‬             ‫دشخو‬



‫دشمیر "اه بروزن نقصیر» بمعتی‌قیض‬                                             ‫بروزن و معنی دشوار است که مشکل‬                          ‫‪۰‬‬    ‫معدوله‬


‫وعناصر اردمه راهم کفته‌اند که خاك‬                         ‫باشد ك‬   ‫و مد‬
                                                                                                                                          ‫باشد ‪.‬‬



‫دشن د بنتح‌ارل وسکون ثالی ونون »‬                                             ‫سین بی‌نقطه وفتح فوقالی» بمعنی محوی باشد‪.‬‬
                                                                                                         ‫‪۰‬‬    ‫ودبشستها به‌عتی محوسات‬


                                                             ‫باشد ‪۴3.‬‬

                                                                                                ‫(‪ )۱‬چش ‪ :‬دشتخوار ‪.‬‬
         ‫‪ - ۴‬اوستا ‪_itiavathsxad‬‏ ‪ .‬پپلوی ‪82111520‬‬                                         ‫در (بد) ‪.‬‬          ‫=‬     ‫رش‬     ‫=‬     ‫‪۱‬‬
 ‫از‪ :‬دشت ( = رش = رژ بد) ‪ ۳‬بار‬
                             ‫‪۴‬‬                                                    ‫هد« اسشق ‪. › ۰۲۷۵‬‬                 ‫( ارمنی ع ‪0۶‬‬
 ‫از ‪ :‬دش ( ‪ ۳‬دز » بد)‬                             ‫‪۵‬‬               ‫رکک‪ :‬شتها ‪ . ۱‬یور داود ص ‪- ۱۷‬‬                      ‫‪۴‬‬           ‫‪۰‬‬       ‫(‪.۵‬م‪).‬‬


     ‫‪۰‬‬    ‫م‪ . ( .‬ر که ‪ :‬اسشق وهوشمان ‪٩۹۵‬‏‬                          ‫دشوار )‬    ‫=‬        ‫‪ +‬خوار (ھ‪.‬م ) بهلوی ‪0 -_2-/۳3‬‬
     ‫یبر که ‪۲٩‬‏ وە‌ناس‪۲۷۲:۲‬؛ در اراک (سلطانآباد) ‪( ۲2201500‬مشکل) «مکیراد» ‪« :‬ملكرا‬
     ‫‪ 1‬کے اؤ دساتبر‬                          ‫ایرد سخن ( سخن شاکرد کشتی گیر) دشخوار آمد ‪« ».‬کلتان ‪٩4۹‬‏ ‪-‬‬
 ‫‪ ۷‬دراراکے ( ملطان آباد ) نخ خیاطی (لخ قرقره ) را‬                 ‫« فرهنك دساتبر ‪. ۵۸۲‬‬
                        ‫‪۰‬‬    ‫دعك‬     ‫دسك » دمه ‪.‬‬
                                       ‫رك‪:‬‬    ‫_‬ ‫کویند « مکی‌نژاد» » رک ‪:‬‬
                                                  ‫‪۸‬‬                                 ‫‪۵‬‬
   ‫برساخته دساشر «فرهنك دساتیر ‪ « ۵6۲‬فاب‪.> ۷1 :۱‬‬         ‫‪۴‬‬                                          ‫‪۰.‬‬       ‫دسصر‬   ‫رك‪:‬‬    ‫‪= ۹‬‬


                                              ‫‪ -۷‬امروز دشت (بفتح‌ارل) کویند ‪.‬‬
          ‫‏‬‫‪٩‬یر‪۲‬کف‬
                ‫‪ ۶#‬دده‌ن ‪ -‬ضم اول وفتح سوم » پهلری ‪ « 07-15۱0‬متاس ‪۷۲:۲۲٩‬‏ ‪#‬تب‬
     ‫«**‪.‬اورامان‬                 ‫از ارستا ‪ ° 2082170-1511‬بارتولمه ‪”eve‬‏ «نببرکه ابضا* » اورامانی ‪0‬‬
     ‫معرب دشمان «دزیج‬                   ‫‪:۲‬‬    ‫«لد‪ .‬ص‪۹۸‬‬                            ‫» فریز ندی » بر نی ونطنزی‬                ‫‏‪ ‘(TY‬گرا ‪5‬‬
```


## [2026-09-05T20:11:49.877Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /دزد/ {print \"LEAF \" NR}' BQT_v2_pages.txt | head -20; echo \"=== leaf with دوزخ ===\"; awk 'BEGIN{RS=\"\\f\"} /دوزخ/ {print \"LEAF \" NR}' BQT_v2_pages.txt | head -20; echo \"=== ژوژه ===\"; awk 'BEGIN{RS=\"\\f\"} /ژوژه|جوجه/ {print \"LEAF \" NR}' BQT_v2_pages.txt | head -20",
 "description": "Find BQT leaves containing key headwords"
}
```


### [2026-09-05T20:11:51.870Z] TOOL RESULT

```
LEAF 32
LEAF 67
LEAF 73
LEAF 92
LEAF 108
LEAF 148
LEAF 156
LEAF 160
LEAF 212
LEAF 270
LEAF 311
LEAF 312
LEAF 325
LEAF 341
LEAF 345
LEAF 369
LEAF 395
LEAF 396
LEAF 424
LEAF 426
=== leaf with دوزخ ===
LEAF 46
LEAF 60
LEAF 342
LEAF 357
LEAF 578
LEAF 638
LEAF 658
=== ژوژه ===
LEAF 55
LEAF 57
LEAF 58
LEAF 59
LEAF 129
LEAF 526
LEAF 622
```


## [2026-09-05T20:11:59.066Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 311 312; do echo \"########## leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -n \"دزد\" ; done",
 "description": "Look at dozd context in BQT leaves"
}
```


### [2026-09-05T20:12:37.237Z] TOOL RESULT

```
########## leaf 311
28:‫د بکراول وسکون ثالی‬               ‫درهر چ‬                             ‫معاون وباری دهنده وثربك دزد باشد ‪.‬‬
34:‫پیشینیان باشد و آنرا بسربالی ایلیا ‪ ۷‬خواند‬                 ‫ومماون‬     ‫‪a‬‏ تحعتی دزد افشار است‪ .‬که عمق‬          ‫بی‌قطه‬
37:                                                                                           ‫وشربك دزد باشد ‪.‬‬
49:                 ‫رك‪ :‬افثار و دزد افشره ‪۰‬‬        ‫‪۴‬‬            ‫‪.‬‬   ‫معرب‌آن نیز «رزدار» دزی جح‪۱‬ص ‪۹۴‬‬
51:   ‫ت‬   ‫دوم) قلمها‬   ‫و تشد نف‬   ‫(یکراول‬    ‫کے درمار‬   ‫‪۵‬‬            ‫افثار ‪.‬‬   ‫افثره و دزد‬    ‫رك‪:‬‬         ‫‪۴‬‬
58:   ‫‪»nil‬‏ ‪« hZud ۰ ۷۲:۷‬ناوادیا ‪,dhzud« ۰۱:۲‬‏‬                      ‫‪ #‬دزد ‪ -‬بضم ارل» پهاوی ‪7‬‬
########## leaf 312
65: ‫دزدان عرب بر سر کوهی نشته بودند و منفذکاروان بسته »‬                                               ‫ق‪:‬‬
70: ‫‪#‬زدیدی ‪ -‬بض اول و فتح پنجم ‪ ,‬از ‪ :‬دزد ‪-۳‬بدن ( پود مصدری ) ؛ سرقت »‬
```


## [2026-09-05T20:12:44.037Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v n=311 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | sed -n '55,65p'",
 "description": "BQT dozd footnote lines"
}
```


### [2026-09-05T20:12:45.807Z] TOOL RESULT

```
             ‫‪ :-‬ابلا ‪.‬‬
                     ‫رك‬‫‪۷‬‬                ‫‪e‬‏ دزهر ح )‪(۱‬‬    ‫‪ .‬رك‪ :‬دزهضت ‪ :‬دژهخت کنك ‪ ۰‬دز دوست‬                   ‫هوخت؟‬

   ‫‪»nil‬‏ ‪« hZud ۰ ۷۲:۷‬ناوادیا ‪,dhzud« ۰۱:۲‬‏‬                      ‫‪ #‬دزد ‪ -‬بضم ارل» پهاوی ‪7‬‬
  ‫اوتا ‪( 020۳2‬بدجنس) ک»ردی ‪( 21‬سارق)‪(81210 .‬سرفت)» بلوچی<‪ ۰ 2۱‬أا ‪ .‬رك‬
  ‫بقیه درصفبحةٌ‪۱۵۸:‬‬
```


## [2026-09-05T20:13:03.651Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 356 357; do echo \"########## leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt; done",
 "description": "BQT leaves 356-357"
}
```


### [2026-09-05T20:13:05.540Z] TOOL RESULT

```
########## leaf 356
      ‫دز رو‬                                                                                                    ‫ی ‪#‬پزرحه‬

 ‫دور دست = کنابة از چیزی است که‬                                       ‫باشد که نام بادشاه ساحران وجادوگران است ‪۰‬‬
               ‫رسیدن بان چیزبیار مشکل بائده ‪.‬‬                         ‫واوپادشاهی بوده بفایت‌ظالم وجادو گر ‪ ۰‬و کوبند‬

  ‫دورس د باسینبیلقطه و حرکت‬
                                                                      ‫زردشت در زمان اوبهم رسید و اومیخواست که‬
         ‫بکر‬ ‫کبرا‬
           ‫وشو‬    ‫مجهول‪ ,‬گیاهی‌است کهتخ‬
                ‫نمآ‬                                                  ‫زردشت را بکشد بنا بآرنکه (‪ )۱‬باوگفتند این‬
      ‫ناد‪.‬‬
                                                                       ‫مرد پیغمبرخداست وآبین ترا برهم میزندا ‪۰‬‬
  ‫خوردن بیخ‌آن جنونآورد‪ .‬وبعضی کوبند دوری‬
 ‫دود ای »بر وزن جوبای ‪ .‬اب یکه بگییخاهی است که تخم آنرا شوکران خوانند‬
  ‫و آلرا ازنفت بدا ورند وبدوری تفتی مشهوراست‬                         ‫مطربان نوازند وآ ترابعربی مزمارخوانند ؛ و با‬
                                      ‫وبعربی طحماء گویند ‪:‬‬                            ‫زای نقطه‌دار گهفمته‌اند (‪. )۲‬‬
 ‫دور قرو = ضم‌ارل وکرفا و رای‬                                                                    ‫دپوا‬
                                                                      ‫رش ه با بای ایجد‪ ,‬امر از دور‬
 ‫بواو رسیده » چیزی‪ .‬بسیار عمیق و صاحب قعر‬                             ‫شدن ‪ ۴‬باشد‪ -‬و نیزه‌ای رانیزکوبند که سناش‬
                                   ‫باشد ‪.‬‬                            ‫دوشاخه بود درقدیم چوب آنرآءررصع مبکرده‌اند‬
 ‫دور قمری» ‪ ۱‬بکر الك ‪ ۰۷.‬دور‬                                          ‫ویشایثر یادشاهان می‌برده‌اند تامردمان‌بدانند که‬
‫وویند دور ‪,‬هر‬ ‫آخرکواکب ساره است » ک‬                                   ‫پادشاه میابدخود را بکناری کشند ‪ -‬و چاوش‬
 ‫کو کبی هفت هزارسال میباشد» هزارسال بخودی‬                             ‫ولقب فافله رانیز گمته‌اند وآن‌چوبی که چاوش‬
   ‫گلر‬ ‫ب سا‬  ‫خود صاحب عمل است » و ششه‬
          ‫دزار‬                                                       ‫قافله بردست میگیرد ‪ -‬وعصا و نیز کوچك را‬
 ‫و کب دیگر ‪ ۰‬و آدم علیه‌اللام‬                    ‫بمشار کت شن‬         ‫نیز کوبند ‪ -‬و بمعنی ناچخ یز آمده است که‬
 ‫دراول دورقمری(‪ )۳‬بظپور ‪-‬د» وآن دوره بایان‬                                                     ‫تبرزین باشد ‪ -‬ک‬
                                                                     ‫ونابه ازآهی باشد که ازته دل‬
                                                 ‫رسف )‪.A (4‬‏‬                                                      ‫براید ‪.‬‬

‫دور گیر ان = بقتح اول » بممنی باده‬                                    ‫دو ر بل" سیفتح بای بجدبروزن‌مورچل»‬
  ‫نوشان وم‌خوارکان‪ - ۹‬ویادشاهان (‪ )۵‬باشد‪.‬‬                                           ‫مردم بیوفا وبی‌حقیقت راگوبند ‪.‬‬
 ‫دو روه نم اول وخفای انی و ثالت‬                                      ‫دور حو لی ع سبضم‌اول وخای قطه‌دار‬
 ‫بواو رسده ‪.‬کل رعا را گوشد جه بکروی آن‬                               ‫بواورسیده ولام بتحتانی کشیده » نوعی از سوسن‬
 ‫زرد ویکروی سرخ هیباشد ‪ -‬وکتابه از هردم‬                              ‫صحرابی‌است » تورآابعربی سیف الفراب خوانند‪,‬‬
                      ‫متافق ومذبذین هم «ست*‪.٩‬‏ ‪#‬‬                                       ‫چه بر کهآن بش‌شیرمیماند ‪.‬‬
                      ‫(‪ )۲‬جك‪ :‬کفته است ؛ چش‪ :‬آهده است ‪.‬‬
                               ‫)‪ (£‬خم ‪ : ۳‬آن دوره را مادان رسالید ‪۱‬‬                    ‫(‪ )۳‬خم ‪ : ۳‬قمر ‪.‬‬
                                                                                 ‫‪ -۳‬پادشاهان ‪.‬‬
                                                                                             ‫(ه) خم ‪:‬‬
  ‫‪:‬‬    ‫‪ ۳‬ات رك‬         ‫‪.‬‬   ‫>‬   ‫بودن‬    ‫از« دور‬    ‫‪۳‬‬    ‫‪۳‬‬    ‫است‪.‬‬   ‫«ارجاءب»‬     ‫بدین صفات‬   ‫‪-‬بادشاه متصف‬   ‫‪۱‬‬


                  ‫‪.‬‬            ‫‪۸‬‬‫‪۳‬ص‬
                                 ‫‪۷۱‬‬‫‪»ld 8101010162‬‏‬                 ‫حولی (باحای حطی) =‬         ‫‪-‬ر‬
                                                                                               ‫دو‬‫‪۴‬‬                ‫دول ‪.‬‬
              ‫‪ - ۷‬و فتح چهارم و ینجم ‪.‬‬                       ‫‪ - ۱‬بقتح اول ‪.‬‬            ‫*ج‪-‬ایی بعید ‪.‬‬
                                                                                                   ‫و‬
          ‫آری چکنم دولت (فتنة) دور قمری بود‪.‬‬                         ‫‪ - ۸‬ازچنگه منش اختر بدمهر بدربرد‬
  ‫‪١٩٤۱‬‏ › ‪.‬‬      ‫یفرظازی‬
                       ‫شحا‬
                         ‫«‬

                                  ‫‪ - ٩‬بمنانیت آنکه ساقیان جام باده را دور مجلس میگردانند‪. ‎‬‬
                                  ‫بممشوق)‪: ‎‬‬          ‫معنی آمده (خطاب‬    ‫هردو‬    ‫» درادن بت‬    ‫دوروی‬   ‫~‪۰‬‬

  ‫‪٩٩۸‬‏‬        ‫حرهٌ‬
                 ‫فد‬‫صیه‬
                     ‫بق‬

########## leaf 357
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

  ‫*المدسد» وامرادوری» ودرتر کی «رورلد» بمعنی‌طر فی که دهالهآن‬                   ‫فر تان دورق‬     ‫‏‪- ٩‬‬

   ‫زای (زانده)‬      ‫‪ ۳" ۴‬از ‪ :‬دول‬                     ‫‪ - ۴‬رك‪« :‬دورای»‬                      ‫است تفس“‬      ‫»طح‬

 ‫‪4‬ت‪2‬ا‪« ۵۷0۳202_0‬بارتولمه ‪۵۷٩‬‏ » از‬
                                 ‫‪ - ۴‬بہاوی ‪« ۷720564‬منای ‪ . ۲۷۲۰‬او‬
   ‫ایرانی باستان ‪o 2۷720200 - . ۷220 -‬‏ (جهنم) در اوستای متاخر ا‪۱8)02020‬‬
  ‫«پارتولمه ‪ ۹۵۷۰‬در ارهنیع ‪“k‬‏ ‪ . xohud .‬از ‪ .۵ ۷202۵۱‬در ارراق تورفان ‪, ۷۳5۷0‬‬
  ‫ربکف ‪۸‬ه * افتالی ع‬
                   ‫(رژ ‪ ,‬بد) است ‪ .‬رك ‪ :‬ت‬  ‫بازىد ‪ » 20۳2۵‬جزو اول = ‪050۷‬‬
  ‫‪80۳260 ,‬‬        ‫‪ ۰ 2260 ۰‬کردی ‪ . 60200‬بلوچی ‪êzêd , 62264‬‏ ‪22۵60 ,‬‬
                                                                        ‫ورك ‪ .‬هوبشمان ابساً ‪.‬‬       ‫«اسشق ‪۱‬‬
              ‫‪.‬‬    ‫اختبار کنند‬   ‫دوزخ‬       ‫عافلان‬              ‫‪ - 9‬کر ترا در بپشت باشد جای‬
  ‫«کلتان ‪. ۲۱‬‬
  ‫‪ - ۸‬ماضی‬               ‫دوزنه ( هم ) ‪.‬‬         ‫=وژله ‏‬
                                                      ‫‪ ۷‬د‬                   ‫= دوژننه (هم) ‪.‬‬
                  ‫‪( ۰‬ھ‪۷ ( .‬‬   ‫آن «دوصدن‬          ‫‪ ۰‬و لاز‬    ‫دفانمدن‬     ‫=‬   ‫‪4‬‬            ‫‪( ۰‬ھ م )‬   ‫«دوسالیدن‬
                     ‫‪€‬‬                          ‫‪€‬‬

                                                                                           ‫شه اصزفحه ‪۵٩۸‬‏‬
       ‫بهکلت آنکه دوروی وفددراست آنکه‌یتیم؟‬                     ‫به شمی و دو روست همی طعنه زد‬
  ‫‪ +‬ی ( مصبری ) » عمل دورو » کیفیت‬                         ‫ی‬
                                                           ‫ودو‬
                                                             ‫ر‪:‬‬‫‪ -‬بفتح اول »از‬            ‫‪ #‬دروولی‬
                                                                                             ‫دو رو ( هم ‪. ).‬‬
```


## [2026-09-05T20:13:19.527Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"دژخیم\" \"دشیاد\" \"دژپیه\" \"دشپیل\" \"دمل\" \"دژاگاه\"; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} $0 ~ w {print \"LEAF \" NR}' BQT_v2_pages.txt | head -8; done",
 "description": "Find BQT leaves for dozxim etc"
}
```


### [2026-09-05T20:13:21.641Z] TOOL RESULT

```
== دژخیم
== دشیاد
== دژپیه
== دشپیل
LEAF 326
== دمل
== دژاگاه
```


## [2026-09-05T20:13:26.882Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v n=326 'BEGIN{RS=\"\\f\"} NR==326' BQT_v2_pages.txt | grep -n \"دشپیل\" -A3 -B3; echo \"=== search dozxim variants ===\"; for w in \"دزخیم\" \"دژخم\" \"خیم\"; do echo \"== $w\"; awk -v w=\"$w\" 'BEGIN{RS=\"\\f\"} $0 ~ w {print \"LEAF \" NR}' BQT_v2_pages.txt | head -8; done",
 "description": "BQT dashpil and dozxim search"
}
```


### [2026-09-05T20:13:28.818Z] TOOL RESULT

```
5- ‫‪.‬هت‬
6-   ‫بج‬‫وشد‬
7-       ‫بد وزشت وپیل (‪ )۳‬بمعنی کره با‬                              ‫دس » بفتح‌اول وسکون‌تانی» خودآرایی‬
8:‫تخفیف تارا الداخته‌الد دشپیل(‪)4‬شده‌است همجو‬                       ‫وخود راساختن وآراستن ‪ -‬وصورت خوش‪ -‬وشبه‬
9-‫دشمن که آن دشت من بوده معنی بد دل وزشت‬                                                        ‫رظیر ومانند ‪١‬‏ باشد ‪. ۴‬‬
10-‫‪ ۰‬ودشنام‬         ‫دل» چه من بمحنی دل همآمده ست‬
11-                                                                  ‫دشل ‪ -.)۱( ۳‬نم اول بروزن مقبل »‬
--
33-
34-  ‫دژ (بد ) چنانکه در‪ :‬دشمن‪,‬‬             ‫‪ - ۴‬وم اول =‬                     ‫(مخفف درس) ‪.‬‬           ‫‪ - ۷‬رلك‪ :‬دس‬
35-
36:  ‫‪ - ۴‬در اراک (سلطانآباد) ‪« 8۷500‬مکی‌نژاد» وکره‪ :‬دشپیل ‪.‬‬                                              ‫دشخو ار ‪۳‬‬           ‫دشنام‪.‬‬
37-
38-
39-   ‫ت‌فوق‪.‬‬
=== search dozxim variants ===
== دزخیم
LEAF 312
== دژخم
LEAF 314
== خیم
LEAF 11
LEAF 68
LEAF 69
LEAF 70
LEAF 105
LEAF 120
LEAF 122
LEAF 131
```


## [2026-09-05T20:13:38.679Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==314' BQT_v2_pages.txt | grep -n \"دژخم\\|خیم\\|خم\" | head -20; echo \"---- leaf 312 ----\"; awk 'BEGIN{RS=\"\\f\"} NR==312' BQT_v2_pages.txt | grep -n \"دزخیم\" -B4 -A6",
 "description": "BQT dozxim entries"
}
```


### [2026-09-05T20:13:40.946Z] TOOL RESULT

```
14:                                                              ‫‌‬                    ‫دز خم ‪ = ۱‬یکر اول و خای تقطه‌دار‬
17:            ‫و پرهیز گاروخواجه سرا باشد ‪.‬‬                                           ‫چه دژ بمعنی بد وخم بم‌عنی‌خوی‌وطبیمت باشفب‬
32:                                                        ‫آمده است ‪.‬‬                 ‫دز خیم ‪ = ۴‬بکراور‪ ۴‬بروزن‌اقلیم»‬
33: ‫دژمان ‪ - ۷‬بکسراول بروزن کرمان‪,‬‬                                                    ‫پمعنی دژخمادت که بدخوی ودطبیعت وبدروی‬
54:  ‫‪ ۰‬بل‬       ‫(لفة بدنهاد‬       ‫‪1‬‬   ‫(ھ‪.‬م‪(.‬‬      ‫خم‬       ‫) ‪+‬‬        ‫رش‬   ‫) =‬   ‫دز‬   ‫از ‪0‬‬   ‫‪۳‬‬    ‫‪۳‬‬                ‫‪۳‬‬    ‫دزخدم‬   ‫رك‪:‬‬            ‫‪۱‬‬
57:  ‫نافظ صحیح‬                ‫‪۳‬‬        ‫‪۳‬‬    ‫آن)‬    ‫( موف‬             ‫‪ ۱‬دز خم ‪ ۰‬دژخی‬        ‫رك‬    ‫‪٩‬‏ و‬   ‫‪4۵‬‬     ‫ص‬       ‫فاب ‪۱‬‬    ‫‪ ,‬بد خلقه‬             ‫سرشت‬
---- leaf 312 ----
39-
40-
41-     ‫‪.‬هلوی ‪. 01511 -‬هندی باستان_ ‪5100‬‬
42-                                    ‫دژ= دش » پارسی باستان _ ‪05‬لا " اوا ‪ 5110 -‬ب‬
43: ‫دشنام ‪ ۰‬دشمن ) ودو ا گاه) آمده‬                  ‫ِ دزخیم ‪a‬‏‬           ‫مر کب بل‬            ‫‪ ۰‬در کلمات‬       ‫‪020 -‬‬       ‫‏_‪ ۰ dur‬آرئی ‪2‬‬
44-
45- ‫آنجاکه از بدی‬              ‫آباد " لفة »‬   ‫) ‪+‬‬        ‫ح ‪۲‬‬       ‫از ‪ :‬دژ (بضم اول ‪ .‬رك ‪:‬‬                   ‫‪- ۴‬‬                ‫اسشق داه“ ‪.‬‬
46- ‫دژا کام‪۰ ‎‬‬       ‫‪ ۳۳‬ره ‪:‬‬   ‫‪o‬‬               ‫‪۰‬‬   ‫دژکامه‬     ‫‪۰‬‬    ‫درکام‬   ‫‪۰‬‬     ‫امه‬
47-                                                                                ‫رك‪ :‬دکژا‬             ‫‪۴‬‬                ‫وخشم معمور است ‪.‬‬
48- ‫)‬      ‫»مر کب از ‪ :‬دژ( حرش‬                ‫«مناس ‪YT‬‏‬                  ‫‪ - ۷‬پهلوی ‪sãkãhsud‬‏‬                                ‫درکام ‪ ۰‬درکامه ‪۰‬‬
49-
```


## [2026-09-05T20:14:05.333Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"žūžag\\|zuzag\\|žužag\\|jujag\\|zūzag\" SNS.txt SNS_pages.txt PHD.txt NYB_vol2_glossary.txt 2>/dev/null | head -20",
 "description": "grep for zuzag porcupine in Pahlavi sources"
}
```


### [2026-09-05T20:14:05.387Z] TOOL RESULT

```
PHD.txt:5077:zūzag
```


## [2026-09-05T20:14:08.529Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zūzag\" -B2 -A2 PHD.txt; echo \"=== index line context ===\"; sed -n '5070,5080p' PHD.txt | head -20; echo \"=== search hedgehog ===\"; grep -n \"hedgehog\" PHD.txt NYB_vol2_glossary.txt | head",
 "description": "MacKenzie zuzag"
}
```


### [2026-09-05T20:14:08.614Z] TOOL RESULT

```
5075-zardag, zardak
5076-va NS
5077:zūzag
5078-zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
5079-any!
=== index line context ===
-gār
PAHLAVI KEY
[114]
130a AS
zāy-! zāyišnīgi zāyišnī! zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(i)gar kàr-! kistárt kištant zalüg zraw- zarwan zruftan zarmānīh zarmān zardālūg zardīh zard Zardu(x)št
zardag, zardak
va NS
zūzag
zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
any!
narī nibés-t nibištant Ozan-! Ozadant
=== search hedgehog ===
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:685:züzag [zwzk! | (N žūža)] hedgehog.
PHD.txt:2249:hedgehog xārpušt, xūkar(ag), züzag.
```


## [2026-09-05T20:14:19.389Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; echo \"--- search جوجه ---\"; grep -n \"جوجه\" MON_part1.txt MON_part2.txt | head -10; echo \"--- ژوژه ---\"; grep -n \"ژوژه\" MON_part1.txt MON_part2.txt | head -10",
 "description": "grep Mo'in for juje and zhuzhe"
}
```


### [2026-09-05T20:14:19.471Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
--- search جوجه ---
MON_part2.txt:246:آوردن جوجه زیر غاز ۰ تاه ۱ تحم 
MON_part2.txt:1565:چنانکه جوجه را فوری به دانه چیدن و مرغ 
MON_part2.txt:14972:است و جنس ماد آن فقط برای جوجه کشی 
MON_part2.txt:14975:روی تخم‌ها می‌خوابد تا جوجه‌ها خارج 
MON_part2.txt:17019:است و « کاتوز» با « کاتوزی» سهیجوجه در 
MON_part2.txt:19921:پاشند. کباب تر: (کد.) برف. کباب جوجه: 
MON_part2.txt:19922:نوعی کباب که از جوجه تهیه کنند. کباب در 
MON_part2.txt:20121:تخم‌ها می‌خوابد تا جوجه‌هایش از تسخم 
MON_part2.txt:20132:جوجهٌ کبک بیرون آید. جوجهً کبک 
MON_part2.txt:20190:جوجه‌ها تا مدت سه تا چهار هفته بدر و مادر 
--- ژوژه ---
```


## [2026-09-05T20:14:20.372Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==710' IEC.txt | head -40",
 "description": "Mann IEC leaf 710"
}
```


### [2026-09-05T20:14:22.049Z] TOOL RESULT

```
 ness’; Br. serch, mf. ‘concubine’; OCS strěxa, f. "roof besides (o-gde, and com. Sl.) straža, f. ‘guard’; Srb. stráZa, id.; R stràža, f. (OCS style) beside o-storðZnyj, adj. “careful'; cf. straxovát, v. ‘insure’ (fr. *storgs-)
sterá- (storg-, střĝ-) “lack, fail, collapse; failure, ruin". Cf. WP II, 642 Gk. stérgo, v. ‘want, lack, accede to’; Ir. (ambig.) (?) searg, adj. (decayed, shrivelled', but see serguh-); seirg, adj. ‘parched’; sear- gaim, v. ‘shrivel, decay’; MLG stérke, stirke, wf. ‘heifer’; OE stirc, Scots stirk, id.; Cz. cf. střízlý, adj. ‘stunted, puny’; (o-gde in) Hitt. stark-, v. “be ill; Gk. storgé, f. ‘love’; Cz. strázeň, f. ‘pathos’; (z-gde in) Lat. strages, f. ‘overthrow’, fr. *str&-; Go. ga-staürknan, v.
stenos — stero (sterno)
20
25
30
35
40
45
1286
‘wither’; ON storkna, intr. ‘shrivel; be stifled’; G storkig, adj. ‘dried up, spoilt, withered’. LG stark ‘heifer is prob. fr. *ster&- with secondary length
sterið ‘run dry, become barren’; sterios ‘run dry, sterile, barren; sterile animal. WP II, 640. (Variant: sther-, sthr-) Skt. starih, acc. sg. staryám, npl. staryás, f. ‘barren cow, heifer’; Oss. stålin, Dig. ast'ålun, inf. ‘collapse, go to ruin’; Tokh. sçire, adj. ‘rough, stiff; Arm. teri, adj. ‘defective’ beside taram, adj. (faded', fr. *sterəmos); Gk. steíro, v. ‘make sterile’; steréo, v. ‘deprive, extort’; steiros, adj. ‘barren’; Alb. shterr, v. ‘run dry, become barren’; tr. ‘make barren, sterilize’; shterrë, f. ‘heifer’; Lat. cf. sterilis, adj. "bar. ren’; sterilésco, v. “become sterile’; Go. staíro, wf. ‘barren animal; MHG stëre, stër, wm. Tan; Li. cf. sterilüs, adj. (‘sterile’: OLat. ste- rilus, id. Lucretius); cf. also Alb. shtrof, shtroh, v. (run dry”, fr. *st(e)resKo: Li. stérstu & stéru, sterti, v. ‘grow numb, turn to wood or stone’). Extns. of type *steribho-, *sterbh- in Gk. stériphos “hard, solid"; sterphos, eos, n. ‘hard skin’; OCS strüblü E streblü, adj. in Jo tělo “fit, robust. Z-gde in Skt. sthiráh “solid”, and in OCS strüví, strüvo, R steríva *car- rion, corpse'. Cf. sterp-
sterk- (sterkt-, střk-) ‘foul; filth’. Cf. ster- Lat. stercus, oris, n. id.; W cf. serth, adj. (2) ‘obscene’; Alb. shtrek, pl. shtriqe, m. (“car- rion’, fr. *strk-). (Isophone is OCS strëkú, strükü “goad”)
stern- ‘spread, extended; spread, lay-out'. Cf. ster (stern-) Lat. cf. lecti-sternium, n. ‘bedspread’; Br. stern, pl. -iu, m. ‘frame, bedstead; team’; W cf. sarn, pl. -au, f. ‘paving’; sarnu, inf. (“pave”, fr. *stərn-)
sterð (sterno), pp: strtós ‘strew, extend, spread, scatter’. WP II, 639 Skt. stárami beside Vedic strnómi, pp: strtáh, id.; Av. star-, id.; Lat. sterno, pf: stravi, sup. stratum, v. id.; cf. segi-sterium 'pigswill; Gk. cf. (o-gde) stórnümi, v. 'spread', etc.; Olr. Mir sernaim, v. id.; (z-gde) Alb. shtrij, shtrij, id.; and in OCS stro, stréti, Cz. stru, střít, id.; (o-gde in) Cz. pro-stor, m. ‘expanse’;
1287
OCZ. pp: pro-strt: Lat. pro-stratum. Formative element *extent, side" (?) in Lat. dexter, sini- ster, au-ster, cf. OHG wini-star ‘left-hand’ etc.
sterp- ‘stiff, hard, barren, withered, dead’. (Variant strp-) Alb. shterpë, adj. ‘barren’; f. ‘barren cow’; Rum. substrate sterp, id.; Rumansh sterp, m., sterpa, f. (briar, dead twig’. Substr. Ligurian); OHG, MHG stërbo, stërbe, wm. ‘plague’; OE steorfa, wm. ‘plague; carrion’; Icel. stjar- fur, adj. ‘stif? beside stirfinn, adj. ‘peevish’; (Gmc. LW in) OCS strüví & strúvo, R steriva ‘carrion’. Cf. WP II, 632. Verbal types in OHG stërban, OE steorfan, sv. 3. ‘die’ and in Li. dial. (z-gde) stirpstù, inf: stifpti, v. ‘grow up, become adult, lit. ‘harden’. The proto- type is uncertain in Arm. t'ormim, v. ‘fade, wither’; t'aram, adj. ‘faded, withered’, perh. from *storp- : *strp-, but cf. ster- above.
steu- ‘boost, display, propagate’. Cf. stuuð Skt. cf. staumi, stáve & stavīmi, pp: stutáh, v. ‘praise’; cf. Vedic stav
```


## [2026-09-05T20:14:29.687Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^1391$\\|^ *1391 *$\" IEC.txt | head; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} /^1391$|\\n1391\\n/ {print NR}' IEC.txt | head",
 "description": "Find page 1391 in Mann"
}
```


### [2026-09-05T20:14:31.268Z] TOOL RESULT

```
18483:1391
---
766
```


## [2026-09-05T20:14:33.566Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18470,18510p' IEC.txt",
 "description": "Mann page 1391 context"
}
```


### [2026-09-05T20:14:33.616Z] TOOL RESULT

```
25
30
35
40
45
1390
Germanic variant: tigus) Mir, tiug, adj. ‘thick, dense’; Br. téó “fat, bul- ky; W tew “fat, thick’; Cor. tew, id., MHG dic, gs: dickes, adj. id. (fr. *tigus); Fris. Sw. tjock, id.; ON pjokkr, id. beside pykkr, id.; cf. Icel. piótta, f. (tough meat”, fr. *teugtà or *tiguta). (For OCS togü, Cz. tuhy, R tugój, see tongh-)
teuk- (teukos, à) (1) “tip, point, peak, beak’. Cf. tuk- (1) & keukos, à (1) Skt. Gokab, am. mn. ‘a root'; Per. cf. Caugan, s. “bat, club’; čukuš, s. ‘hammer’; Alb. suké, f. “hill, peak’; Ligur. (in Swiss) tschuggi, f. id.; Mir tuag, f. ‘axe’; Br. Suk, m. ‘nape, shoulder, chignon’: Blg. čuk, m. ‘hammer’; Srb. &üka, f. Cpeak, point’, fr. a variant *keuka); Latv. cf. Cukurs, m. “peak, point, gable’. (Indo-Iran. forms ambig.)
teuk- (2) “press; pressure, force’. Cf. tuk- (2) and next. See teuquó Arm. tok, ost ‘persistence’; tokam, v. (per. sist, endure'. Cf. SEM: AIE: § 56: IE -eu- > Arm. -0-); OHG diuhen, wv. “press, force” beside dühen, id. (fr. *tükio); G deuen, v. *tolerate; atone for; Li. cf. tüksti, intr. v. ‘bang’. (Gmc. forms ambig. Cf. teuquó as a variant in OE)
teuk- (touk-, tuk-) (3) “fat; fat part, buttock’. Cf. tuk- (2) & touk-. WP I, 711 Tokh. B cf. wi-cükaine ‘the two haunches, buttocks'; Olr. cf. (*-eu- or *-ou-) tuachail, adj. ‘pregnant’; OHG dioh, n., MHG diech, gs: diehes, n.; OE péoh, n.; ON þjó, n. ‘thigh, haunch’; Icel. ‘buttock’; Du. dij, f. as OHG; EMDu. dije, f. id.
teukså “girl, young female’. Cf. teuquio. (Norse type: touksàá) Norw. (landmal) taus, def: tausa; Norw. tós, Sw. tös, f. & n. ‘girl, wench’, (o-gde); Slovene Cuba, f. ‘heifer’; Blg. cf. (dim.) čuška, f. *cun- nus”. (Isophonic: Skt. Coksab, à, adj. pure)
teukso, ið (1) ‘chatter, twaddle’ W cf. tuch, m. ‘grunt, groan’; Rust, s. “non- sense’; Li. Ciauksti, v. (1) “twitter; stammer”; cf. čiauškalas, m. ‘twittering; twaddle’ beside (o-gde) tauskiu, tauksti, v. ‘twaddle’
teuksó, ið (2), see touks-. E-gde in MHG diusen, v. (lug, tousle; get muddled’; Blg. cuslja, v. 'shuck — grain’; Morav. Cz.
1391
cuchat, inf. ‘tousle’
teul- (1) ‘ball’. See next and toul- (1) & (2) Skt. cf. o-gde tolah, adj. ‘poised’; tolakalr, am, mn. (a weight); tolika, f. (*rampart'. See next); Br. tül, s. (“fistful”, also dül, id.); G Deul, m. ‘pig of iron (fr. *toulis); Slovene cula, f. ‘bag, bundle’; (LW in) Alb. cule, f. ‘bundle, trap- pings, chattels'
teul- (2) ‘wrapping, envelope, husk’. Same as (1) (?). Cf. toul- Alb. cull, m. ‘blanket; W tul, pl. -ion, m. “envelope, shroud’; Latv. caula ‘shell, husk’; (z-gde in) Li. tüloti, inf. ‘wrap up, muffle'
teul- (3) ‘docked, lopped, stunted' Oss. cula, Dig. cola, adj. ‘docked; inbent, dented'; Blg. čul, adj. “dockeared'; (LW in) Alb. cull, id. Cf. Skt. čolah “jacket?
teul- (4) ‘swing, surge; verve, impetus’. Alb. sul, súlem, v. ‘attack; dash’; Cz. cf. čilý, Slovak čulý, adj. ‘lively’; Srb. culjati, inf. ‘swing, shake, rock, dandle’
teum- (teumos, à, On, is) “pile, hill’. Cf. tum-, tumolos. (Alb. & Ir. ambig.) Alb. (ambig.) tum, m. "mound: Ir. (ambig.) tuaim, f. ‘mound’; G Dieme, f. and Diemen, wm. ‘rick, stack’; Srb. cuma, f. ‘pile’. (Iso- phonic: Ir. tuam, s. 'burdock ).
teup- ‘move’ (?) Skt. (ambig.) čopāmi, v. id.; Cz. cupu, cupat, v. ‘tramp, dodder’; Srb. cf. cupnati, inf. jump’. (Isophonic: Pol. cupnac, inf. ‘crouch’, Li. am- biguously Ciáupiu, ti ‘squeeze, pucker’; čiau- pýtis, inf. “jib”)
teuquolis, os, à (?). (Variants). Cf. keuk- Alb. cf. sukë, f. ‘hillock, peak’; Srb. Blg. Cuka, f. ‘peak, summit” beside Blg. Cukla, f., Cukar, m. id. (Isophones: Alb. cukél, f. ‘bundle; huzzy'; sükull, f. ‘rag; shred, snowflake’; sukel, f. *snowflake")
teuquio “female, girl; vulva’. Cf. WP I, 716 Per. Cuz, s. fcunnus'; Cüze, s. ‘chick’; Alb. cucé, f. “girl; nipple’; cf. cukél, f. (2) *huzzy'; Go. (ambig.) piwi, f. ‘girl, maid; OS thiwi & thiu- wa, wf. id.; OHG diu, gs: diuwi, id.; OE bëo- we, id.; ON py, f. mad Cz. dial. číča, f. ‘wench; cunnus'; (Slav LW in) Alb. çuçë, f. id.
teuquo, ið ‘thrust, force’. Cf. tüqu- and teuk-
teul- — teut- (teuto, ið)
20
25
30
33
40
45
1392
(2). (ambiguities) Alb. cuk, v. ‘stab; squeeze, cram"; Lat. cf. tüc- etum, n. 'forcemeat'; MHG diuhen, v. ‘press, shove’; OE peowan, v. (2) “press, force, crush; stab; threaten; grapple with'; Cz. cukat, cuk- nout, inf. ‘shove, buffet’; Srb. cukati, inf. ‘knock’; Blg. čukam, v. ‘bang, beat, clink’
teur- (1) ‘resist, oppose’ W turio, inf. ‘reverse’; tur, m. ‘reversal’; Sw. tjura, v. ‘jib’; R cf. (o-gde) unt, turnùť, v. ‘repel’; Srb. turati, turiti, v. ‘push’
teur- (2) ‘grope, root about. Variants Alb. cf. turî, def: turîni, m. ‘snout’; Br. türia, inf. ‘grope, root; Slovak türit, inf. ‘ferret out
teur- (3) “observe? (?) Ir. tuaraim, v. ‘guess, conjecture’; Slovak túr- nut, inf. ‘notice’
teus- (teusõ, i0; touseio) (1) ‘quieten; grow quiet’. Cf. tous-, tus- Skt. cf. (o-gde) tosayami, v. ‘appease; gladden’; (z-gde) tusami, v. ‘settle down’; Av. tuš-, v. (3) radical: "be silent; Arm. ğokim, v. ‘sub- side’ fr. an induced formula *teusuio); Slovak čušať, čušiť, inf. “be silent
teus- (2) 'stir, rouse'. Cf. touks- MHG diusen, wv. ‘lug, tousle’; intr. ‘get mud- dled'; (o-gde in) ON peysa, inf. *press, drive, urge’; Ukr. čuxaty, inf. ‘scratch’; BIg. cf. čuš- kam, v. (4) ‘push’; Srb. cf. cusa, f. *boar's snout’. Same as next (?)
teus- (3) “buffet, damage? Av. tu$-, radical “harm, damage’; Srb. Cuáati, čušiti, v. (2) ‘slap; MHG diusen, see (2)
tent- (teuto, ið) (1) “meet, join” Br. tüta, oda, inf. (gather, mass”, tr.); OE péodan, v. “join; approach'; cf. peod, m. (2) ‘fellowship’; Icelandic pyóast, reflexive vb. “attach o's to’; Ukr. Cutyty, inf. ‘adduce’. (Alb. cys, aor: cyta, v. “touch” is ambig. Cf. teud- (2) and teuqu-)
teut- (teutó, ið) (2) “watch, notice, cherish, look after'. Cf. tu- Hitt. cf. duddu(mi) (spg. of *tutu-, queried: ‘watch over, observe, manage"); MHG diuten, wv. ‘show, indicate, mean’; ON cf. þýða, wv. “explain, mean’; Lat. cf. tüto, are, v. freq. of tueor ‘defend’; OCS cf. o-Stusto, -Stutiti, v. ‘feel, sense’; OCz. &ücu E cütím, inf: cütiti,
```


## [2026-09-05T20:14:44.556Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AVG p237 (leaf 291) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==291' AVG.txt | head -40",
 "description": "Jackson Avesta Grammar p.237"
}
```


### [2026-09-05T20:14:46.358Z] TOOL RESULT

```
=== AVG p237 (leaf 291) ===
v.  afyrya-  m.  'pupil' ;  Av.  n&vhaipya-  n.  nomen  propr. , cf.  Skt.  nasatya-;  Av.  v&strya-  adj.  'farming',  m.  'farmer'; — Av. avhuya-  f.  'lordship'.  —  Adjective.  From  a-stem:  Av.  aha'rya- 'lordly'  (observe  vrddhi  fr.  akura-)  Yt.  13.82,  14.39;  Av.  ajrya- 'topmost'  =  Skt.  dgrya-,  agriyd-;  Av.  haomya-  'relating  to  haoma" =^  Skt.  somyd- ;  Av.  fyaflrya-  'kingly'  =  Skt.  kfatriya- ;  Av.  yesnya- 'revered'  =  Skt.  yajfiiya-.  —  From  <f-stem :  Av.  halnya-  'belonging to  an  army'  =  Skt.  sinya- ;  Av.  galpya-  'material,  earthly'.  —  From a-stem:  Av.  rapwya-  'reasonable',  cf.  Skt.  ftviya-;  Av.  po*ruya- 'first'  =  Skt.  purvyd-;  so  Av.  gaoya-,  gSvya-  'belonging  to  the  cow* =  Skt.  gdvya-. —  From  consonant  stem:  Av.  visya-  'of  the  clan'  = Skt.  viiya-.
Note.  Observe  the  few  forms  that  show  -aya  as  remarked  upon just  above  §  852  c.  Examples  are:  Noun.  Av.  zar*daya-  n.  'heart'  =  Skt. hfdaya- ;  Av.  zar'maya-  adj.  'green',  n.  'verdure',  cf.  Skt.  harmyd-.  —  Ad- jective. Av.  aspaya-  (ace.  aspalm]  'belonging  to  a  horse'  =  Skt.  dtvya-; Av.  nSvaya-  'flowing,  navigable'  =  Skt.  n&vya.-,  cf.  §  68  Note  3.
26.  Av.  -ra  —  Skt.  -ra  (Whitney,  §§  1226,  474). §  853.     This  suffix  occurs  in  a  very  few  words ,   chiefly  pronominal derivatives.     Examples  are:
Av.  adara-  adj.  'under,  lower*  =  Skt.  ddhara-;  Av.  afara-  adj. 'later,  behind'  =  Skt.  dpara-;  Av.  upara-  adj.  'further,  above'  = Skt.  upara-.  Probably  Av.  hazavra-  adj.  and  n.  'thousand'  =  Skt. saAdsra-.  Observe  Av.  ahura-  m.  'lord,  Ahura'  =  Skt.  dsura-,
27.  Av.  -va,  (-vya)  •=.  Skt.  -va,  (-vya),  Whitney,  §   1228. §  854.     The  ending  -va  as  secondary   suffix   occurs   in   a   very   few adjectives.    These  must  be  distinguished  from  orig.  ^-adjectives  transferred to  the  a-inflection.     Examples  of  -va  as  secondary  suffix  are :
Second.  Deriv. :  —Suffix  -ra,  -va,  -vya,  -van,  -va'rf,  -vana,  -vatit.      235
Av.  ajrava-  'belonging  to  the  head'  (ajra-);  Av.  bftnava-  'be- longing to  the  tail'  (buna-  §  185).
Note.  The  suffix  Av.  -vya  =  Skt.  -vya  (Whitney,  §  12280)  is  dis- guised in  one  or  two  words,  names  of  kindred :  Av.  br&tu'rya-  m.  'uncle' §  191,  cf.  Skt.  bhratrvya-.
28.  Av.  -van,  (f.  -va
```


## [2026-09-05T20:14:50.165Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==293' AVG.txt | head -40",
 "description": "Jackson p.237"
}
```


### [2026-09-05T20:14:51.854Z] TOOL RESULT

```
e  MSS.  and  each is  followed  by  a  point,  the  compounds  are  not  always  so easily  recognized  as  in  Skt.,  nor  are  the  rules  of  Sandhi so  rigorously  carried  out.
Verbal  Composition  has  been  sufficiently  treated  above, §  749  seq. ;  it  is  necessary  here  to  take  up  only  the  Noun- Compounds.
Note.  In  printed  texts  the  compounds  are  differently  marked  in different  editions;  Geldner's  Avesta  has  the  compound  united  in  printing and  retains  the  separating  point  (.) ;  Westergaard  likewise  but  a  small dash  (-)  is  used;  Spiegel's  edition  does  not  designate  the  compounds.
NOUN-COMPOSITION.
§  859.  Noun-compounds  have  either  a  substantival  or an  adjectival  force.  They  consist  usually  of  two  members, more  rarely  of  three  (§  894),  e.  g.  drva-a$a-ci]>ra  'the  sound offspring  of  righteousness'.  The  members  which  enter  into composition  may  be  nouns,  adjectives,  or  indeclinables ; or  they  may  be  parts  of  a  verb,  either  radical  or  parti- cipial. The  final  member  of  the  compound  receives  the inflection.  The  first  member  is  subject  to  some  modifica- tion in  form,  generally  assuming  the  weak  grade.
§  860.  Examples  of  different  combinations,  nouns, adjectives,  etc.,  entering  into  composition  are:
Noun-Composition: — Union  of  the  Members.  237
Av.  vispa'ti  (subst.  -f-  subst.)  m.  'lord  of  the  clan'  =  Skt.  vispdti-; Av.  dar'ja.l>azu-  (adj.  -j-  subst.)  adj.  'longimanus'  =  Skt.  dirgha- liahu-;  Av.  wspo.bamya-  (adj.  -\-  adj.)  adj.  'all-shining';  Av.  kvaspa- (indecl.  -J-  subst.)  adj.  'well-horsed'  =  Skt.  svahia-;  Av.  rafaelta-, rapaeitar-  (subst.  -j-  rad.)  m.  'warrior  standing  in  chariot'  =  Skt. ratheffhd- ;  Av.  nidasnaipiH-  (rad.  -f-  subst.)  adj.  'having  weapons laid  down';  Av.  star'to.bar'sman-  (ptcpl.  -j-  subst.)  adj.  'with  out- spread barsom'.  Likewise  some  other  combinations.
Union   of  the   Members   of  Compounds.
a.  Contraction  and  Hiatus.
§  86 1.  The  rules  of  Sandhi  for  concurrent  vowels  and consonants  are  in  great  measure  carried  out,  though  some- times they  are  disregarded.  Hiatus,  for  example,  is  at times  allowed  to  remain  between  concurrent  vowels.
§  862.  Examples  of  the  different  methods  of  treat- ment of  vowels  are :
With  Contraction  or  Resolution.  Av.  a"ru$Sspa-  'having  white horses'  (auruja  -j-  aspa);  Av.  a'wydma-  'over-mighty'  (a*wi  -j-  aw); Av.  pa'lySsti-,  pa'tyasti-  (v.  1.  fa'^i.asti-),  paipyesti-  'repetition'  (pafti -j-  as0}
```


## [2026-09-05T20:14:57.436Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duS\\.\\|dus\\.\\|duz\\.\\|duS-\\|duz-\" AVG.txt | head -20",
 "description": "grep Jackson for dus- compounds"
}
```


### [2026-09-05T20:14:57.481Z] TOOL RESULT

```
189:nu  Im  vispd  ciprS  zl  mazdaiwhddum not}  daibitim  dus.sastis  ahum  m'rqgydf akd  varand  drzgva*  hizvm  dvar'to.
925:Av.  zbayemi  'I  invoke'  =  Skt.  hvdydmi;  GAv.  duz-
1097:Av.  ifavo  'arrows' =  Skt.  ifavas;  Av.  vahisto  'best' =  Skt.  vdsitfkas;  Av.  raejjaydf  'may  wound'  =  Skt. re$dydt;  Av.  srae$yeiti  'it  clings',  cf.  Skt.  slifyati. — Av.  duS.tor'tjm  'ill-done'  =  Skt.  du$-krtdm;  Av.  muSti- 'fist'  =  Skt.  mufft-;  Av.  gao&m  'ear'  =  Skt.  ghdfam; Av.  tao$ayeiti  'makes  still'  (Yt.  10.48)  =  Skt.  tdfdyati. —  Av.  usdiwm  'bull'  =  Skt.  uk$dnam;  GAv.
2051:§  339-  Av.  -w-»r"»w  hvacah-  (adj.  m.  f.)  'well-speaking' =  Skt.  suvdcas-.  Av.  -orr--^  vacah-  n.  'word'  =  Skt.  vdcas-; Av.  -«rT-"»QO>3  duz-vacah-  (adj.)  'evil-speaking' = Skt.  durvacas-.
4862:2.  Adjective  value  (Whitney,  §   1282):  Av.  vispo.bamya-  'all- brilliant',  upard.kairya-  'making  higher,  raising  up'.   With  advbl.  pre- fixes (a-,  an-,  hu-,  duS-,  ar?-  etc.),  Av.  hukfr'ta-  'well-made',  Av. arlu^da-  'right-spoken'.     Likewise  some  others.
5471:duz-vacah-,   dcln.  339. d*b*naota   569. 22.
```


## [2026-09-05T20:15:02.323Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4862' AVG.txt | tr -cd '\\f' | wc -c; echo \"---context---\"; sed -n '4855,4870p' AVG.txt",
 "description": "Locate AVG line 4862 page"
}
```


### [2026-09-05T20:15:04.063Z] TOOL RESULT

```
298
---context---
242  Word-Formation:  Compound  Stems.
the  latter  member  as  though  it  were  governed  by  the  latter. The  force  of  the  prior  member  is  that  of  an  oblique case  (ace.,  instr.  gen.  etc.)  depending  upon  the  latter; and  actual  case-forms  in  such  instances  do  sometimes  occur, see  §  877  above.  The  compound  has  noun  or  adjectival value  according  to  its  final  member.
1.  Noun  value  (Whitney,  §   1264):    Accusative  relation.    Av. mipro.druj-  m.  'one   that   breaks  his  pledge".  —  Gen.  relation.    Av. •vispani-  m.  'lord    of  the    clan'.  —  Loc.   relation.     Av.  rafiaiita-  m. 'warrior  standing  in  a  chariot'  (rape  =  actual  loc.,  cf.  §  877).
2.  Adjective  value  (Whitney,  §   1265):    Ace.  relation.    Av. kanur'dd.jan-  'smiting  the  head'. — Dat.  relation.  Av.  damiddta-  'created for  all  creatures'. — Instr.  relation.  Av.  ahuradata-  'made  by  Ahura'. —  Abl.  relation.  A\.  qzo.buj-  'freeing  from  distress'.  —  Loc.  relation. Av.  z'mar'guz-  'hiding  in  the  earth'.
b.  Descriptive  Compounds. (Cf.  Whitney,  Skt.  Gram.  §   1279  seq.)
§  882.  Descriptive  Compounds  (Skt.  Karmadharya) are  those  in  which  the  former  member  stands  not  in  a case-relation  but  in  attributive  relation  to  the  second and  adds  some  qualification  to  it.  The  value  of  the  com- pound itself  is  substantival  or  adjectival  according  to  its final  member.
1.  Noun  value  (Whitney,  §   I28ob,  d):    Av.  dar»jo.$iti-  f.  'a long  residence',  pir'no.m&aha-  n.   'full-moon' ; — Av.  ultradaenu-  f. 'she-camel',  cf.  Whitney,  Ski.   Gram.  §  I28od.
2.  Adjective  value  (Whitney,  §   1282):  Av.  vispo.bamya-  'all- brilliant',  upard.kairya-  'making  higher,  raising  up'.   With  advbl.  pre- fixes (a-,  an-,  hu-,  duS-,  ar?-  etc.),  Av.  hukfr'ta-  'well-made',  Av. arlu^da-  'right-spoken'.     Likewise  some  others.
iii.  Secondary  Adjective  Compounds.
(Cf.  Whitney,  Skt.  Gram.  §   1292  seq.)
§  883.  The  secondary  adjective  compounds  are  of two  kinds,  (a)  Possessive,  (b)  those  with  governed'  final member.
Noun-Composition: — Determinative,  Adjective  Compounds.       243
a.  Possessive  Compounds. (Cf.  Whitney,  Skt.   Gram.  §  1293  seq.)
§  884.  Possessive  Compounds  (Skt.  Bahuvrihi)  are composite  adjectives  formed  from  a  corresponding  Deter- minative compound  (§  880)  merely  by  adding  to  the  latter the  idea  of  'having'  or  'possessing'  that  which  the  deter- minative itself  denotes.
§  885.  The  Skt.  shows  a  difference  of  accent  between  a Determinative  and  its  corresponding  Possessive';  in  Av.,  as  there  is  no written  accent,  the  distinction  cannot  be  drawn  in  that  manner.
§  886.  The  second  member  of  the  Possessive  is  ge- nerally a  substantive ;  the  first  member  may  be  a  substan- tive, adjective,  pronoun,  numeral,  participle  or  indeclinable. The  force  of  the  compound  always  remains  adjectival.
```


## [2026-09-05T20:15:13.087Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1097' AVG.txt | tr -cd '\\f' | wc -c; awk 'NR<=2051' AVG.txt | tr -cd '\\f' | wc -c",
 "description": "Locate AVG pages for dus.kereta and duz-vacah"
}
```


### [2026-09-05T20:15:14.960Z] TOOL RESULT

```
105
152
```


## [2026-09-05T20:15:24.606Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSF grep دژ ===\"; grep -n \"دژ\" FSF_pages.txt | head -20; echo; echo \"=== FSF pdf page markers near ===\"; grep -n \"\\[pdf page\" FSF_pages.txt | head -3",
 "description": "grep FSF for dozh"
}
```


### [2026-09-05T20:15:24.668Z] TOOL RESULT

```
=== FSF grep دژ ===
843: ‫‪(-۱‬نقیض بنده برده) اصیل‌زاد‪ .‬اصیل‬                             ‫بازرگان به روئین‌دژ آمده‪:‬‬
855:                                                           ‫دگرگفت کو از دژ گنېدان‬
1711:          ‫دو فرسنگ چون اژدهای دژم‬                        ‫درآویختن و دست به گریبان شدن‪:‬‬
4608:                  ‫به واژة چرخ نگاهکنید‪:‬‬                              ‫دیوار دژ سازند‪:‬‬
5278: ‫تو از تخم ساسانی ای بندژاد‬                       ‫(‪)۲-۱۶۱-۵۲۵‬‬
5729:        ‫بسی باره و دژ که کردیم پست‬                ‫ای بسیار داشته باشد» (برهان)‪:‬‬
5837:‫(‪)۴-۲۵۷۱‬‬                                             ‫به می تازه داریم روی دژم‬
6769:                                                                            ‫دژ آ‬
7337:                                                          ‫بسی باره و دژ که کردیم پست‬
8532:‫از آن بارة دژ برآمد تراک‬                       ‫(‪)۶-۵۹۱۰-۱۱۵‬‬
8817:           ‫همانا به مردی سبک داریم‬                      ‫دژم خفته بر جایگاه نشست‬
10476:     ‫چو شیرنربرآن خوک دژم تاخت‬                     ‫رسستم در نسخستین نبرد ابسافندیار‬
10984:‫بدنهاد‪.‬‬    ‫جزء دوم واه مرکب دژخیم‬                ‫زبان خیره پرتاب و دل پردروغ‬
11107: ‫داروگیر‬      ‫خروشیدن‬   ‫برامد‬                    ‫کزین دژ برآرم به خورشید گرد‬
11718:                                       ‫د=زدژ‬                         ‫‪-۲‬به درازا کشنده دیرانجام‪:‬‬
11725:                           ‫دژاگاه (باپیش اول)‬
11736: ‫بدو بر به رفتن دژاگاه بود‬
11741: ‫چشویر دژاگاه نخچیر جوی‬
11747:                   ‫‪۲‬دژخيم روزبان جلاد‪:‬‬
11750:                 ‫به دژخیم فرمود شاه اردشیر‬

=== FSF pdf page markers near ===
```


## [2026-09-05T20:15:26.023Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SBK دوزخ ===\"; grep -n \"دوزخ\" SBK.txt | head -10; echo \"=== VIE pdf 37 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==37' incoming/VIE/VIE_pages.txt | head -40",
 "description": "SBK and VIE lookups"
}
```


### [2026-09-05T20:15:27.910Z] TOOL RESULT

```
=== SBK دوزخ ===
1600:خواپ‌سیری‌در بپشت‌ودوزخ کرد واحکامید کر پیدا اورد که‌در کتاب‌ار تایو بر اف نامك 
3018:خوانده| ند ازمو بدان معروف عصر اردشر وشایور اول است که درعا لم «سیر > بپشت ودوزخ را 
3248:ودوزخ و مینوان بود فرو گزارد ودیران نوشتند و ناما ن کتاب اردای ویر افنامك است . 
9725:ر : دوزخو دوزخ 
11115:بو دعذاب مخالفان تو دروی کر ٹم ماه همی بدوزخ ه انست 
17109:وتنگث خودرا مستحق دوزخ مکن. 
=== VIE pdf 37 ===
[pdf page 37]
همان بغ فارسی است .ريشه وهمطزدر زبان های روسی ؛اوگراشینی »بلوروسی
بلغاری » مقدونی »یوگسلاوی »چک و لهسنانی دیده می‌شود و درزبان مفولی
بصورت بایات ( نام خدا نام ایل) .بایاژ ( ثروتمند شدن) .بایان
( ثروتمند ) ملاحظه می‌شود زیرا ريشه بگ و پر یکی است وذط انگلیسی
بمعنی بزرگ و و بیط شخص متشخص از همین ريشه است . بعلاوه کلمه
بیک بدنبال تام اشخاص مشهور بویژه از تبار عثمانی و ناکشورهای عربی در
زبان انگلیسی فرآوان مشاهده شده است که همان بگ ترکی می‌باشد .
درفارسی علاوه بریغ واژه بگ هم دیده می‌شود » چنانچه بگ و لک‌به
معنی رعناگی و بهتری آمده‌است" خسروی گفت :
آن یکی بی هنر عزیز چراست
واندگر مانده خوار زیسر.سمک.
این علامت نسه فرهی ,اشد
پس‌چه دعوی کنی‌بدویک‌ولسک (۷)
واگر کسانی منکر رأبطه و وبغ باشند رابطه و83 بایگ ( رعناعی و
بهتری) را نمی توانند منکر شوند .
بگ در واژه بکتاش» مرادف خواجه تاش فارسی نیز برجای ماده‌است.
869 بعقیده بعضی زبان شناسان +268 دگرگون شده بهشت است
زیرا اصولا " بهشت کلمه عالی اوستائی است و درزبان‌آوستائی یکی ازعلاقم
صفت عالی پسوند و1 ايشت واشت است .ازکلمه ,+۷0۳ واژه ا8نط۷2
ساخته شده که بهشت کنونی از آن زاده شده و بهشت درمعنی "بهترین "
اسث هماتکه در انگلیسی است .
فردوس برین وآنچه که درفارسی امروز بهشت خوانده می‌شود دراوستا
به گونه 1912-220۵ ل72آوهیشت اخو بوده است بمسعنی بهترین جهان
دربرابر " دوش|خو " بدترین جهان که واژه* اخبر دگرگون شده و به صورت
دوزخ درآ مده‌است .
۷۰ لغت فرس آسدی توسی .
۳۱
```


## [2026-09-05T20:15:38.217Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 11715 11760; do echo -n \"line $L -> leaf \"; awk -v n=$L 'NR<=n' FSF_pages.txt | tr -cd '\\f' | wc -c; done; echo \"--- context ---\"; sed -n '11710,11760p' FSF_pages.txt",
 "description": "FSF dozh entries context and leaf"
}
```


### [2026-09-05T20:15:40.663Z] TOOL RESULT

```
line 11715 -> leaf 237
line 11760 -> leaf 237
--- context ---


                               ‫(حافظ ‪۰۸‬‬                     ‫گی بدند‬   ‫نرک‬
                                                                        ‫جد ه‬
                                                                           ‫همه کشته ش‬
 ‫من اگرنیکم اگربدتوبرو خود را باش‬                     ‫به پیش صف اندر درنگی بدند‬
‫هر کسی آن درود عاقبت کار که کشت‬                       ‫(‪)۶-۱۶۱-۵۲۴‬‬       ‫‪۱‬‬

                                       ‫د=زدژ‬                         ‫‪-۲‬به درازا کشنده دیرانجام‪:‬‬
                               ‫قلعه‪ .‬حصار‪:‬‬                       ‫سواران بیاراست افراسیاب‬
               ‫بر آن خرمی روز هرگر نبود‬               ‫گرفتش ز جنگ درنگی شتاب‬
‫پی مرد بی راه بردز نبود‬                               ‫(‪)۷-۴۲-۲۷۲‬‬
                                                                                             ‫دروه‬
‫‏)‪(FVA-YOA-£‬‬
                                                      ‫حواستاری و آرزومندی» تندرستی و‬
                           ‫دژاگاه (باپیش اول)‬
                                                      ‫بهروزی و آرامش و کام‪ .‬آفرین‪ .‬ستایش‪,‬‬
 ‫‪١‬۔سهمگین»‏ خشمگین» بیمناک‬
                                                      ‫نیایش (پهلوی «‪ -60۳4‬تندرستی» آرامش»‬
                                ‫هراس آور‪:‬‬
                                                                    ‫_شکند گمانیک ویچار ‪:)۲۷۲‬‬
            ‫چنین تا بیامد یکی زرف رود‬                               ‫درود فریدن فرخ دهم‬
  ‫پروود‬
      ‫سپپرهاشگدنده چون تا‬
                                                      ‫سخن هرچ پرسند پاسخ دهم‬
          ‫بنش زرف و پهناش کوتاه بود‬                   ‫(‪)۱-۲-۵‬‬
 ‫بدو بر به رفتن دژاگاه بود‬
                                                              ‫چو کشتی ز دشت اندر آمد بهرود‬
‫‏)‪(TT 'A-Y1¥-F‬‬
                                                      ‫داد نیکی دهش را درود‬        ‫همی‬
            ‫سوی مرز توران چو بنهاد روی‬                ‫(‪)۳-۹۱۲-۸۴۳۳‬‬
 ‫چشویر دژاگاه نخچیر جوی‬
                                                       ‫باربد به خسروپرویز که به فرمان پسرش‬
                                                                     ‫ات‬
 ‫(‪)۲-۱۷۱-۸۱‬‬


                   ‫‪۲‬دژخيم روزبان جلاد‪:‬‬
                                     ‫‪-‬‬
                                                            ‫کهگر دست من زین سپس نیز رود‬
                 ‫به دژخیم فرمود شاه اردشیر‬
                                                      ‫بسباید‪ ,‬مبادا به من بر درود‬
‫که رو دشمن پادشارا بگیر‬
                                                      ‫‪-٩(‎‬شیرویه ‪)۴۰۹‬‬                        ‫‪e‬‬
               ‫به خنجر میانش به دو نیم کن‬                                                  ‫رودن‪‎‬‬
 ‫دل بدسگالان پر از بیم کن‬                                                            ‫درو کردن‪:‬‬

             ‫بیامد دژاگاه و فرمان گزید‬                              ‫در ان نیستان بيش شير بود‬
 ‫شد آن نامدار از جهان ناپدید‬                          ‫که پیلی نیارست ازو نی درود‬
 ‫(‪)۷-۱۰۲۴‬‬                                             ‫(‪)۲-۱۹-۳۹۲‬‬
                             ‫دژخیم‬                                   ‫پشیمانی آنگه نداردت سود‬
```


## [2026-09-05T20:15:48.203Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==233' FSF_pages.txt | head -60",
 "description": "FSF leaf 233"
}
```


### [2026-09-05T20:15:50.101Z] TOOL RESULT

```
‫در زمان‬                                        ‫‪۳۳۹‬‬


                                       ‫دربدر‬                                           ‫[زهر]در‬
                           ‫بخش به بخش‪:‬‬                          ‫لعبو‪:‬‬
                                                                    ‫طوضو‬
                                                                       ‫مهرم‬
                                                                          ‫از هرگونه‪ .‬از‬
               ‫‏‪ENE‬‬                                                ‫نسویسنده را پیش بنشاندند‬

‫به کیخسرو آمد همه در به در‬                             ‫دیند‬
                                                          ‫ن هم‬
                                                             ‫اها‬
                                                               ‫رخن‌‬
                                                                  ‫زر در س‬
                                                                        ‫ه‬
 ‫‪۵۸۱۳۰۲۸۳۱‬‬                                           ‫(‪)۱-۱۱۰۲-۰۱۰۱‬‬

                     ‫درج (بروزن برج ‪-‬تازی)‬                    ‫گواه به جای «زهر» در «زهرگونه»‬
‫قوطی‪ ,‬جعبه که در آن پیرایه‌های گرانبها و‬                    ‫زهر گونه‌ای رفت بر خوان سخن‪...‬‬
                 ‫جواهر گذارند‪ .‬پیرایه‌دان‪:‬‬           ‫‏)‪(YAY-AF-F‬‬
            ‫چنان بدکهقیصر بیان چندگاه‬                                                    ‫دراج‬
‫رسولی فرستاد نزدیک شاه‬                                                         ‫نوعی قرقاول‪:‬‬
        ‫ابانامه و مدیه و ببانتار‬                                   ‫لدهمیبلبلازشاخسرو‬
‫یکی درج و قفلی برو استوار‬                            ‫چو دراج زیر گلان با تذرو‬
‫(‪۸‬نوشیروان ‪)۵۵۵۳‬‬                                     ‫(‪)۳-۰۷۱-۱۹۵۲‬‬

                                     ‫درخشش‬                                               ‫درای‬
‫[اسم مصدر از درخشیدن ]‪ :‬درخشندگی‪:.‬‬                                          ‫‪-۱‬پتک آهنگری‪:‬‬

                          ‫تابندگی» فروغ‪:‬‬                       ‫از آنکچارمهنگران پشت پای‬
    ‫میان بزرگان درخشش مراست‬                          ‫بپوشند هنگام زخم درای‬
‫چو بخشایش وداد و بخشش مراست‬                          ‫(‪)۷۲۶۹۲۲‬‬
‫(‪۸‬هرمزد ‪)۶۳‬‬                                                   ‫همان کاوهآن بر سر نیزه کرد‬
                            ‫درد (با پیش اول)‬         ‫گرد‪.‬‬     ‫ارست‬
                                                                 ‫حبازا‬
                                                                     ‫رز‬‫بنگه‬
                                                                          ‫هما‬
          ‫ته‌نشینشراب و سرکهو مانندآن‪:‬‬                                       ‫‪-۲‬زنگ‪ .‬جرس‪:‬‬
             ‫ازین آشتی جنگ بهر منست‬                             ‫خروشیدن کوس باکرنای‬
‫همه نوش تدورد و زهر منست‬                             ‫همان زنگ زرین و هندی درای‬
‫‪۱۷۰۶۸۰6‬‬                                              ‫)‪(1-۷۴1-۸01‬‬
                                     ‫درزمان‬                    ‫ان‬
                                                                ‫ردواز‬
                                                                    ‫کایاآم‬
                                                                         ‫چو بانگ در‬
                    ‫بی‌درنگ» زود فوری‪:‬‬               ‫همی رفت پیش اندرون ساروان‬
‫چو بازور [نام افسونگر] در کوهشد در زمان‬              ‫(‪)۶-۲۹۱-۰۸۴‬‬
‫بسرامد یکی برف و باد دمال‬                                                  ‫(منوجهری» ‪:)۰۶۱‬‬
‫(‪)۴-۷۳۱۰-۹۲۳‬‬                                              ‫شاد باشید کهجشن مهرگان آمد‬
                        ‫(ویس» ‪:)۰۹۱-۳۱‬‬           ‫ای درای کاروان آمد‬  ‫وو‬‫آنگ‬
                                                                         ‫با‬
```


## [2026-09-05T20:16:04.810Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 73 77; do echo \"###### leaf $L\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' FSF_pages.txt | head -12; done",
 "description": "FSF leaves 73 and 77"
}
```


### [2026-09-05T20:16:06.605Z] TOOL RESULT

```
###### leaf 73
         ‫به بالای تو بر چمن سرو نیست‬
‫چو رخسار تو تابش پرو نیست‬                    ‫‪-۱‬به معنی «با» کهافادة معنی استعانت و‬
‫(‪)۱-۱۶۱-۹۸۳‬‬                                                               ‫وسیله کند‪:‬‬
                    ‫‪-۲‬مفیل معني هنگام‪:‬‬                 ‫‪...‬بهرگس گل سرخ را داد نم‬
         ‫سپاس از جهاندار فریادرس‬              ‫(‪)۱-۷۸۱-۱۱۸‬‬

‫کس‬    ‫او دست‬   ‫نگیرد به سختی جز‬             ‫ربگاس چگشلم‌گونه را نمداد با‬
                                                                       ‫نعنی‬
                                                                          ‫[ی‬
‫(‪)۱-۴۲۱-۸۵۷‬‬                                                     ‫اشک گونه را ترکرد‪].‬‬
                                             ‫وخنوران گاهبجای «به حرف اضافه «با»‬
                                                                              ‫س‬
###### leaf 77
 ‫بار‬


          ‫بهقلب اندرون بیژن تيز چنگ‬                              ‫چو بشنید خراد برزین سخن‬
  ‫جای جنگ‬           ‫بزمگاه آمدش‬     ‫همی‬             ‫بدانست کانکاراکوشهدن‬
          ‫سران سواران چو برگ درخت‬                                ‫که بهرام دادش به ایران اميد‬

  ‫فرو ریخت از بارو برگشت بخت‬                      ‫سخن گفتن من شود باد و بيد‬
  ‫(‪)۵-۰۸-۶۲۲۱‬‬                                     ‫‏(‪٩‬رویز ‪)۴۱۵۲‬‬
                                                              ‫پ‬
 ‫واژه «بار» معنی‌های مختلف دارد که یکی‬            ‫این است که‪ :‬بهرام‬       ‫ر‬‫خبیت‬‫آنی‬
                                                                                 ‫(مسع‬
```


## [2026-09-05T20:16:25.050Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 236 237 238; do echo \"###### leaf $L ($((L-54)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' FSF_pages.txt | grep -o \"دژ[^ ‪]*\\|دش[^ ‪]*\" | sort -u | head -20; done",
 "description": "FSF leaves 236-238 dozh/dosh words"
}
```


### [2026-09-05T20:16:27.388Z] TOOL RESULT

```
###### leaf 236 (182)
دش
###### leaf 237 (183)
دش
###### leaf 238 (184)
دژ
دژ‬
دژاگاه
دژخيم
دژخیم
دژخیم‬
دشارا
دشت
دشمن
دشیر‬
```


## [2026-09-05T20:16:37.985Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9700,9740p' SBK.txt",
 "description": "SBK context around duzax"
}
```


### [2026-09-05T20:16:38.026Z] TOOL RESULT

```
رز : زرفاك 
د : زوش 


غ : گریز 


زرف 
زرف 


کریغ 


۱ - تبدیل: ز بغین درزبان دری متداولت ماندء کرین کريغ - تیغ- تیر ستیژه و این 


قىد لات مر بوط بلپجه‌هاست ۰ 


۳۰ گفتار پنجم 
پهلوی : فارسی‌دری 
۹ ژ: تبدیل‌شده‌است به : 


ر : دوزخو دوزخ 

2 کارزار کارزار 

پهردر پھر بر پرهیر 
ش : وريزیتك برشته 

ر : توا تور(یس‌فر_دون) 


س: آبدیل‌شده‌است به : 


ث : اسییان(لجه‌ای ازآئوپیان) ائفیان(آبتین- پدر فریدون)" 
خ : ماس ماخ (مام) 
ف : آسروله آذروان
```


## [2026-09-05T20:16:47.358Z] TOOL CALL #47: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:16:47.363Z] TOOL RESULT

```


```


## [2026-09-05T20:16:51.457Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B2%D8%AF",
 "prompt": "Give the full Persian etymology of دزد (dozd) 'thief': Middle Persian form, Old Iranian/Avestan antecedent, and any cited authorities."
}
```


## [2026-09-05T20:16:52.289Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B2%D8%AE",
 "prompt": "Give the full Persian etymology of دوزخ (duzax/dozax) 'hell': Middle Persian, Avestan antecedent, morphological analysis, cited authorities."
}
```


### [2026-09-05T20:16:57.627Z] TOOL RESULT

```
# Persian Etymology of دزد (dozd) 'Thief'

**Middle Persian Form:** The word derives from Middle Persian [script needed] (dwz, "thief").

**Proto-Indo-Iranian Antecedent:** It comes from Proto-Indo-Iranian "*duš-" meaning "bad, wrong," which itself traces to Proto-Indo-European "*dus-" with the same meaning.

**Avestan Connection:** The page notes cognates including Avestan "duš-" ("bad"), demonstrating the word's ancient Iranian roots through this related language.

**Cited Authority:** The etymology section references Francis Joseph Steingass's *A Comprehensive Persian–English dictionary* (1892) as a scholarly source for this entry.

The etymological chain shows how a root meaning "bad" or "wrong" evolved into a term for someone who commits wrongful acts—a thief.
```


### [2026-09-05T20:17:01.035Z] TOOL RESULT

```
# Persian Etymology of دوزخ (duzax/dozax) 'Hell'

## Middle Persian Origin
The term derives from Middle Persian 𐭣𐭥𐭱𐭧𐭥𐭩 (dušox, "hell"), representing a continuation of Old Iranian forms.

## Morphological Analysis
The word's structure reveals a compound construction: "bad existence." It combines two Proto-Iranian elements:
- *duš- ("bad")
- *Háhuš (from Proto-Indo-Iranian *Hásuš, meaning "life, existence, being")

The complete Proto-Iranian form *dušHáhuš literally translates to this compound meaning.

## Avestan Antecedent
The Avestan language preserves related forms: 𐬛𐬀𐬊𐬲𐬀𐬎𐬎𐬀 (daožauua) and 𐬛𐬎𐬲𐬀𐬢𐬵𐬎 (dužaŋhu), demonstrating the antiquity of this term within Iranian languages.

## Cited Authority
The entry references D. N. MacKenzie's *A concise Pahlavi dictionary* (1971), which documents "dušox" as the Middle Persian form, providing scholarly grounding for the etymological reconstruction.
```


## [2026-09-05T20:17:04.817Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%AC%D9%87",
 "prompt": "Give the etymology of Persian جوجه (juje) 'chick, chicken' — any Middle Persian or onomatopoeic origin, cited authorities."
}
```


## [2026-09-05T20:17:06.235Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%98%D9%88%DA%98%D9%87",
 "prompt": "Give the etymology and meaning of Persian ژوژه — hedgehog/porcupine? Middle Persian and Avestan antecedents."
}
```


### [2026-09-05T20:17:09.178Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:17:09.732Z] TOOL RESULT

```
# Etymology of Persian جوجه (juje)

According to the Wiktionary source, the Persian word likely derives from **Sogdian origin**: "Probably from Sogdian...(/⁠čužăk⁠/, 'chick')."

The entry notes a related Turkish term _civciv_ ("chick"), which could be imitative in nature. The Sogdian connection suggests the word traveled through ancient trade routes, though the ultimate origin may involve onomatopoeia—the sound of a chick.

The source cites **Sevan Nişanyan's dictionary** (2002–) as an authority on related etymological material, particularly regarding the Turkish cognate's imitative properties.
```


## [2026-09-05T20:17:16.292Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"čwz\\|cwz\\|čužāk\\|cuzak\\|čuzāk\" SOD.txt SOD_pages.txt 2>/dev/null | head -10; echo \"=== chick ===\"; grep -n \"chick\" SOD.txt | head -10",
 "description": "grep Gharib Sogdian for chick"
}
```


### [2026-09-05T20:17:16.347Z] TOOL RESULT

```
SOD.txt:29408:3308  cwz'kk   B  <^r 
SOD.txt:29417:cuzak   ©Yaghn.  cuja%  Khwar.  twzk 
SOD.txt:52857:pacwast   ©pt.  st.  =»pcwz- 
SOD.txt:52867:pacwastu/o  ©adv.  -^pcwstw,  pcwz-2 
SOD.txt:52888:6709  pcwz-'   M,  B,  S    (jy  y--^  j->)o>jj^j  <O^TolS:** 
SOD.txt:52901:6710  pcwz-2  C  u^'jU^ 
SOD.txt:53121:paciwaz  ©impf.  =»pcwz-1 
SOD_pages.txt:13198:       3297 ctf'rwystmyq          C =* stfrwystmyq                           3308 cwz'kk       B                                  <^r
SOD_pages.txt:13201:        cuzak ©Yaghn. cuja% Khwar. twzk                               caxste =*cys-, cysty
SOD_pages.txt:22978:     pacwast ©pt. st. =»pcwz-                 *s>            6714 pcxw'k M                                            ^U
=== chick ===
29419:chicken 
88160:chicken     3308
```


## [2026-09-05T20:17:18.827Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29404,29424p' SOD.txt",
 "description": "Gharib Sogdian cwz'kk entry"
}
```


### [2026-09-05T20:17:18.881Z] TOOL RESULT

```
GMS  1527,  1546;  cw>ty>  GMS  1511;  BBB  f76 

3307  cww    M  =>  cw 

3308  cwz'kk   B  <^r 


131 


cym'yS  (h) 


cuzak   ©Yaghn.  cuja%  Khwar.  twzk 

chicken 

SCE  233;  TSP  2332 

3309  cwZY    B,  S  =»  cwty
```


## [2026-09-05T20:17:25.727Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dys-",
 "prompt": "Give the etymology of the prefix dys-: Greek dys-, PIE root, and how it reached English (via Latin?). Also mention dysfunction and dystrophy if present."
}
```


## [2026-09-05T20:17:26.779Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dus-",
 "prompt": "What does this reconstruction page say about PIE *dus- 'bad, evil': meaning, descendants (Greek, Indo-Iranian, Germanic, Celtic), and relation to *dew-/*deus-?"
}
```


### [2026-09-05T20:17:32.607Z] TOOL RESULT

```
# Etymology of the Prefix Dys-

## Origin and Path to English

The prefix **dys-** comes from Greek *dys-*, which itself derives from the Proto-Indo-European (PIE) root ***dus-*** meaning "bad, ill, evil." This PIE root is also the source of related forms in Sanskrit (*dus-*), Old Persian (*duš-*), Old English (*to-*), Old High German (*zur-*), and Gothic (*tuz-*).

The ultimate source traces back to the PIE root ***deu-*** meaning "to lack, be wanting." The prefix entered English through Greek, as English adopted Greek word-forming elements rather than through Latin intermediaries.

## Meaning

The prefix means "bad, ill; hard, difficult; abnormal, imperfect." As the source notes, it "destroying the good sense of a word or increasing its bad sense."

## Examples

Two relevant compounds appear in the article:

- **Dysfunction** (1914): combining *dys-* + *function*, meaning "failure to function, abnormality or impairment of function," originally used in medicine and anatomy.

- **Dystrophy**: listed among related words, following the same pattern of combining the prefix with another root.

The prefix was "very productive in ancient Greek," attaching even to proper names and generating numerous creative formations.
```


### [2026-09-05T20:17:33.849Z] TOOL RESULT

```
# PIE *dus- 'bad' Overview

**Meaning:** The reconstruction indicates that *dus- functions as "a prefix meaning bad" with the antonym being *h₁su-.

**Etymology:** The entry presents competing theories. One suggestion links it to *dews- ("to lack"), while De Vaan proposes derivation from *dwóh₁ ("two") with semantic evolution from "into two" through "apart" to "bad."

**Major Descendants:** The prefix appears across multiple language families:
- Greek and Italic: Proto-Hellenic *dus- and Latin dis-
- Indo-Iranian: Proto-Indo-Iranian *duš-
- Germanic: Proto-Germanic *tuz-
- Celtic: Proto-Celtic *dus-
- Balto-Slavic: Proto-Balto-Slavic *dúsdjus
- Armenian: possibly Old Armenian t-

**Connection to *dew-/*deus-:** The page does not directly address a relationship between *dus- and forms like *dew- or *deus-. The only etymological connection mentioned is the speculative link to *dews- ("to lack"), which is presented as one possible explanation among several competing theories about the prefix's origin.
```


## [2026-09-05T20:17:46.576Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dys-,\" KLN_1966.txt | head -5; echo \"---\"; grep -n \"^dys-\\|dys-, pref\" KLN_1966.txt SKT.txt | head -5; echo \"=== search 'dysentery' ===\"; grep -o \"dys-[^.]\\{0,200\\}\" KLN_1966.txt | head -5",
 "description": "grep Klein and Skeat for dys-"
}
```


### [2026-09-05T20:17:48.958Z] TOOL RESULT

```
12514:dys-,  pejorative  suff.  used  esp.  in  the  senses  ‘hard to,  difficult  at,  slow  of’ ;  the  opposite  of  the  pref. eu-.  —  Gk.  8uo-,  meaning  ‘hard,  bad,  ill’,  cogn. with  the  suffixes  OI.  dug-,  Avestic  dush-,  duz-, of  s.m..  Arm.  t-  (negative  pref.),  Goth,  tuz-, OHG.  za-,  zi-,  zu-,  zar-,  zir-,  zur-,  MHG.,  G. zer-,  ‘apart,  asunder’,  ON.  tor-,  ‘difficult,  hard’, OIr.  do-,  du-,  ‘bad,  ill’,  OS.  to-,  te-,  ti-,  OE.  to-, te-,  tor-,  ‘apart,  asunder’,  and  perh.  also  with OL.  dvis  (whence  L.  bis),  ‘twice’.  See  dis-. dysacousia,  dysacousis,  dysacusia,  n.,  a  condition in  which  sounds  cause  discomfort  ( med .)  — Medical  L.,  fr.  dys-  and  Gk.  Axovaic,  ‘a  hearing’, fr.  dtxouro  (for  *axou<uco),  ‘I  hear'.  See  acoustic and  cp.  words  there  referred  to. dyschroa,  dyischroia,  n.,  discoloration  of  the  skin (med.)  —  Medical  L.,  formed  fr.  dys-  and  Gk. Xp6a,  resp.  ypoid,  ‘color’.  See  -chroia. dyscrasia,  n.,  an  ill  state  of  the  body  (med.)  — Medical  L.,  formed  fr.  dys-  and  xpacn;,  ‘a mixing,  blending’.  See  crater  and  cp.  crasis. For  the  ending  see  suff.  -ia. dysenteric,  adj.,  1)  pertaining  to  dysentery;  2) having  dysentery.  —  L.  dysentericus,  fr.  Gk. Suaevxepixo;,  ‘pertaining  to  dysentery’,  fr. Suaevxepta.  See  next  word  and  -ic. dysentery,  n.,  inflammation  of  the  large  intestine.
---
KLN_1966.txt:12514:dys-,  pejorative  suff.  used  esp.  in  the  senses  ‘hard to,  difficult  at,  slow  of’ ;  the  opposite  of  the  pref. eu-.  —  Gk.  8uo-,  meaning  ‘hard,  bad,  ill’,  cogn. with  the  suffixes  OI.  dug-,  Avestic  dush-,  duz-, of  s.m..  Arm.  t-  (negative  pref.),  Goth,  tuz-, OHG.  za-,  zi-,  zu-,  zar-,  zir-,  zur-,  MHG.,  G. zer-,  ‘apart,  asunder’,  ON.  tor-,  ‘difficult,  hard’, OIr.  do-,  du-,  ‘bad,  ill’,  OS.  to-,  te-,  ti-,  OE.  to-, te-,  tor-,  ‘apart,  asunder’,  and  perh.  also  with OL.  dvis  (whence  L.  bis),  ‘twice’.  See  dis-. dysacousia,  dysacousis,  dysacusia,  n.,  a  condition in  which  sounds  cause  discomfort  ( med .)  — Medical  L.,  fr.  dys-  and  Gk.  Axovaic,  ‘a  hearing’, fr.  dtxouro  (for  *axou<uco),  ‘I  hear'.  See  acoustic and  cp.  words  there  referred  to. dyschroa,  dyischroia,  n.,  discoloration  of  the  skin (med.)  —  Medical  L.,  formed  fr.  dys-  and  Gk. Xp6a,  resp.  ypoid,  ‘color’.  See  -chroia. dyscrasia,  n.,  an  ill  state  of  the  body  (med.)  — Medical  L.,  formed  fr.  dys-  and  xpacn;,  ‘a mixing,  blending’.  See  crater  and  cp.  crasis. For  the  ending  see  suff.  -ia. dysenteric,  adj.,  1)  pertaining  to  dysentery;  2) having  dysentery.  —  L.  dysentericus,  fr.  Gk. Suaevxepixo;,  ‘pertaining  to  dysentery’,  fr. Suaevxepta.  See  next  word  and  -ic. dysentery,  n.,  inflammation  of  the  large  intestine.
=== search 'dysentery' ===
dys- and  the  second  element  in  sapsago
dys-  and  Gk
dys-,  pejorative  suff
dys-  and  Gk
dys-  and  Gk
```


## [2026-09-05T20:17:55.055Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"dystrophy[^.]\\{0,220\\}\" KLN_1966.txt | head -3; echo \"---\"; grep -o \"dysfunction[^.]\\{0,200\\}\" KLN_1966.txt | head -3",
 "description": "Klein dystrophy/dysfunction"
}
```


### [2026-09-05T20:17:56.822Z] TOOL RESULT

```
dystrophy,  hypertrophy
dystrophy,  dystrophia,  n„  defective  nutrition (med
dystrophy
---
```


## [2026-09-05T20:17:59.545Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"dystrophy,  dystrophia,  n„[^§]\\{0,400\\}\" KLN_1966.txt | head -2",
 "description": "Klein dystrophy full entry"
}
```


### [2026-09-05T20:18:01.423Z] TOOL RESULT

```
dystrophy,  dystrophia,  n„  defective  nutrition (med.)  —  Medical  L.  dystrophia,  fr.  dys-  and Gk.  xpotpv),  ‘nourishment’.  See  trophic  and  cp. atrophy,  hypertrophy.
```


## [2026-09-05T20:18:08.577Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%98%D9%88%DA%98%D9%87/",
 "prompt": "What do the Persian dictionaries (فرهنگ معین، دهخدا) say for ژوژه? Give the definition and any origin tag."
}
```


## [2026-09-05T20:18:10.249Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84",
 "prompt": "Is دمل (domal/dommal) 'boil, abscess' Arabic or Persian in origin? Give the etymology given for Arabic دمل and for Persian دمل."
}
```


### [2026-09-05T20:18:13.962Z] TOOL RESULT

```
# Persian Dictionary Definitions of ژوژه

**Dehkhoda Dictionary (لغت نامه دهخدا):**
The entry defines ژوژه as "خارپشت" (hedgehog), noting it is an animal that was highly regarded in ancient Iranian culture for being an enemy of ants and harmful creatures. The dictionary provides etymological notes, tracing the word back through Pahlavi texts.

**Moein Dictionary (فرهنگ معین):**
Listed simply as "(ژَ یا ژِ ) (اِ. ) خارپشت" — defining the term as "hedgehog" with variant pronunciation markers.

Both dictionaries consistently identify ژوژه primarily as a hedgehog, with the Dehkhoda entry providing extensive historical and cultural context about the animal's significance in ancient Persian literature and Zoroastrian texts.
```


### [2026-09-05T20:18:15.319Z] TOOL RESULT

```
# Etymology of دمل (Boil/Abscess)

Based on the Wiktionary content provided, I can only confirm the **Arabic etymology**. The page states:

**Arabic origin:** "From the root د م ل (d m l). Compare Persian _دنبل_ (donbal, 'boil')."

This indicates the Arabic word derives from a three-letter root system (د م ل), with a note that it resembles the Persian cognate "donbal," suggesting a potential relationship between the two languages rather than establishing Persian as the origin.

**Persian etymology:** Unfortunately, the web content provided does not include the Persian Wiktionary entry for دمل, so I cannot provide the etymology claimed by Persian sources. To answer your question completely, you would need to consult the Persian Wiktionary directly.
```


## [2026-09-05T20:18:26.281Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"haima\" \"duz.uxta\\|duzuxta\\|duz-uxta\" \"duidaSna\\|dus.daena\\|duidaena\" \"duS.ci\\|dus.ci\\|duici\" \"pi3wa\\|piθwa\\|pitliwa\\|pithwa\"; do echo \"== $w\"; grep -n \"$w\" BRT.txt | head -4; done",
 "description": "grep Bartholomae for node 3 and 9 forms"
}
```


### [2026-09-05T20:18:28.000Z] TOOL RESULT

```
== haima
28007:—  aoa  Stars  'ta  paiti  apa.g3urvayat  Yl //7.48i  —  yat  *haima  (sd.)  'iff  (AD.)  .  . miiamt  V.  5. 59;  —  ava  paZo  ava  'ts {AD.)  .  .Järayalw?m  Vr. /j.  i;  Yt,  y.  147;
28725:j.  hao?om  F.  ap:  lies  haimam.
== duz.uxta\|duzuxta\|duz-uxta
13795:duzuxta-
== duidaSna\|dus.daena\|duidaena
== duS.ci\|dus.ci\|duici
13762:•  j.  duS-ciOra-  Adj.  (fem.  'ra-)  'des .\nblick  übel  ist,  hässlich  anzusehen': drujim  yam  °rqm  timanhainJm  YL  /^.gs;
28400:(sd.)  saranamya  V.2. 10.  ^dus.cihrayä  Yt  79.94.
== pi3wa\|piθwa\|pitliwa\|pithwa
```


## [2026-09-05T20:18:35.581Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duzuxta-\\|duz-uxta-\" -A6 BRT.txt | head -30; echo \"=== dus.kereta ===\"; grep -n \"duS.k\\|dus.k\\|duskrta\\|kar'ta\" BRT.txt | head -8; echo \"=== daena ===\"; grep -n \"duidaena\\|duS.daena\\|duidaSna\\|duz.daena\" BRT.txt | head -5",
 "description": "Bartholomae duzuxta, duskereta, dusdaena"
}
```


### [2026-09-05T20:18:35.659Z] TOOL RESULT

```
13795:duzuxta-
13796-756
13797-•  j.  dus.sravah'  Adj.  'der  einen  üblen Rur,  Leumund  hat,  Su7KXr)j^.
13798-Ableit.  (s.  auch  diuLir').
13799-•  j.  duS.sravahyä-  f.  'Übelberiichtigtheit, übler  Leumund':  'vaMi  (NS.  oder  IS.) Y.i4.
13800-Ableit.  aus  '*diä.sriaiak-.  —  Vgl.  lOuijravah:
13801-—  Pä.!  dulsriw-ik,
=== dus.kereta ===
13361:Eig.  PPA.  (S  sog.  5),  aus  einem  Praes.  29  b (Int.),  mit  11  nach  S  ^yo.  8  für  ','  aus  ar.  tin, weshalb  k  (nicht  /,  %62.  1  No.)i)j  vgl.  zBild. soBsuHlayö.  Eig.  Bed,?,  s.  No.  2.  —  'I  Das Richtige  über  h  bei  JOppert  Act.  6.  Congr. Ot.,  Sect.  S^m.  63g.  Falsches  neuerdings WZKM.  //.  254.  —  ')  Der  Bildung  scheint ein  Praes.  8  ar.  *,i(Jiyim-  \  'd[k)Hnas.  lu  Grunde lu  liegen;  ob  eig.  'schnaufend,  keuchend'  zu lit.  .hiesiu,  dusik}
13748:•  j.  duS.k«r9t-''  Adj.  'übeltuend,  Übel- täter'(?):  äat  ana  parB  -ta  V.  2/.  6".
=== daena ===
```


## [2026-09-05T20:18:49.594Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pi[t93&θ]wa\\|pitu-\\|pTwah\\|pivah\\|pTvah\" BRT.txt | head -10; echo \"=== dus.p ===\"; grep -n \"duS\\.p\\|dus\\.p\\|duip\" BRT.txt | head -8",
 "description": "Bartholomae pithwa / dus-p compounds"
}
```


### [2026-09-05T20:18:49.656Z] TOOL RESULT

```
16356:pivah-
16384:•  j.  pipivah-  Adj.,  nur  fem.  pipyßst-  'die Milch  in  der  Brust  hat,  säugt':  yS  nairi- kam  yqm  apu^rqm  °pyBsim  va  apipyästm va  anasaxtqm  (sd.)  para  xludra  avi fra^hiTszaiti  ". .  eine  Frau  . .  gleichviel  ob
16387:•  j.  pivah-  n.  'Fett,  Speck':  iiar) pascaita
=== dus.p ===
```


## [2026-09-05T20:18:58.260Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Speise'\" BRT.txt | sed -n '1,15p' | cut -c1-160",
 "description": "Bartholomae Speise entries"
}
```


### [2026-09-05T20:18:58.310Z] TOOL RESULT

```
15983:•  j.  pIpidTWä-''  f  'feste  (nicht  flüssige) Speise':  yä  '^wa  vasS  aHstSe  (sd.)  N. 62.  a)  insbes.  'feste  Opferspeise,  Speise- opfer'''
16360:•  j.  pitav-  m.  'Speise',  insbes.  feste,  'Fleisch- speise': yim  (näml.  azim)  upairi  kirssaspB .  .  °täm  pacata  ".  .  sich  (Reise h) sp
```


## [2026-09-05T20:19:12.578Z] TOOL CALL #65: Bash

```json
{
 "command": "grep -rl '\"Čter\"' data/extracted/batch/ | head -3",
 "description": "Find root Cter"
}
```


### [2026-09-05T20:19:12.631Z] TOOL RESULT

```
data/extracted/batch/page-143.json
```


## [2026-09-05T20:19:13.531Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"x.a9ra-\\|xva9ra\\|x'ä9ra\\|x\\*ä9ra\\|Behagen\" BRT.txt | head -8",
 "description": "Bartholomae xvathra"
}
```


### [2026-09-05T20:19:13.590Z] TOOL RESULT

```
5164:—  Sal  dli  ävaidayamahi  . .  "vatthe  Y.4. 6.  a)  ellipt:  'vaiiihe..  timänS.paite'^xa Hilfe!  Hausherr"  V./Ä19;  31,22.  LS. avöaüs  Inf.  sbes.  2)  'Ergötzen,  Behagen' (nur  Komp.).
6348:•  j.  aäa.x''ä*i^-"  Adj.  'der  das  Behagen, Glück  des  Ala  gewährt' (?),  von  Bergen: gairlm  usi.darmjin    ..    "rim  Y,  1'.  14;  —
6362:•  j.  a-säite'*  Inf.  'sich  zu  freuen,  behag- lich zu  fühlen':  ya'iia  vätS ..  vJsp^m  ahUm .  .frähatica  .  .  aiwüa  as°  Jsmayäiti  "wie der  Wind . .  die  ganze  Welt . .  in  Behagen versetzt"  A.  4-  6-
11338:•  g.  CiSriLavah-,  j,  ^Äiftra.avah- "  Adj. 'deutliches,  augenfälliges  Ergötzen,  Behagen schaffend':  at  tsi  atrSm  ahurä  usSmakJ.. ^aslstjm  imavaithm  f/ö((sd.)  raparUE  'vav- h)m  ai  .  .  "von  deinem  Feuer  {Ätar),  o Ah.,  . .,  dem  verheissenen ,  machtvollen, wünschen  wir,  dass  es  dem  Getreuen  augen- fälliges Behagen  (schaffe),  aber.,"  ^.34. 4*>;  —    narqm  ..  *°Z'anhqm  Ny.j.  10'*.
16318:•  j.  pourus-x'^Sra-  Adj,  {fem,  'rä-)  'der  j viel  Behagen,  Glück,  Wonne  gewährt':, alis  'ra  Yt.  15.54;  —  kahmsi  istlm  °rqm\ azim  baxsäni  Yt/o.io8;  Y.6Ä11-
24443:•  j.  vispa  Jt'aÖTa-  Adj.  'der  alles  Behagen, Glück,  alle  Wonne  besitzt  und  gewährt":
```


## [2026-09-05T20:19:34.210Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%88%D8%A7%D8%B1",
 "prompt": "Give the etymology of Persian دشوار (došvār) 'difficult': Middle Persian form and the analysis of its second element (xwār 'easy'? or bar- 'to carry'?)."
}
```


## [2026-09-05T20:19:35.348Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D9%88%D8%AC%D9%87/",
 "prompt": "What does فرهنگ معین say for جوجه — definition and any origin/etymology tag? Also any Dehkhoda etymological note."
}
```


### [2026-09-05T20:19:39.580Z] TOOL RESULT

```
# Etymology of Persian دشوار (došvâr)

## Middle Persian Origin
The word derives from Middle Persian *dwšw'l* (/⁠dušwār⁠/), which itself comes from Old Persian.

## Morphological Analysis
According to the Wiktionary entry, the word breaks down as: "دش (duš-, 'bad') +‎ خوار (xvâr, 'easy; mean, abject'), denoting the opposite of easy." This surface analysis suggests the second element relates to *xvâr* meaning "easy," not *bar-* ('to carry').

The prefix دش- derives from Proto-Iranian *\*duš-* ("bad"), while the second component خوار carries the semantic sense of "easy," creating a compound meaning roughly "not easy" or "difficult."
```


### [2026-09-05T20:19:42.719Z] TOOL RESULT

```
# Definition from فرهنگ معین

**Definition:** "(جِ) (اِ. ) ۱ - نوزاد پرندگان . ۲ - نوزاد مرغ خانگی"

This translates to: newborn birds (1) and newborn domestic chickens (2). The entry includes a note about "جوجه سوخاری" (breaded chicken nuggets) and "جوجه کباب" (chicken kebab).

# Dehkhoda Etymology Note

According to Dehkhoda's dictionary, "جوجه" is equivalent in weight and meaning to "جوژه," denoting baby birds. The entry references "برهان" (Burhan) as a source and includes traditional Persian sayings like "جوجه را آخر پائیز می شمارند" (one counts the chick at autumn's end).

Neither source provides explicit etymological origin information, though Dehkhoda establishes its relationship to the variant form "جوژه."
```


## [2026-09-05T20:19:57.980Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B2%D8%AF|page 143 root Dus, node 2: Persian dozd < MP duzd < Av. duždā̊' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B2%D8%AE|page 143, nodes 3-5: dozax < MP dušox < PIr *duš-Hahu- bad existence' \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%AC%D9%87|page 143 node 8: juje chick, Sogdian cuzak not Av. duz-aka' \\\n 'https://www.etymonline.com/word/dys-|page 143 nodes 10-12: Greek dys- to English, not via Latin' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dus-|page 143 root box: PIE *dus- bad' \\\n 'https://abadis.ir/fatofa/%DA%98%D9%88%DA%98%D9%87/|page 143 node 8: Moin/Dehkhoda zhuzhe = kharposht hedgehog' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84|page 143 node 5: domal Arabic root d-m-l, cf. Persian donbal' \\\n 'https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%88%D8%A7%D8%B1|page 143 nodes 1-2: doshvar = dush + xwar easy, not bar- carry' \\\n 'https://abadis.ir/fatofa/%D8%AC%D9%88%D8%AC%D9%87/|page 143 node 8: Moin juje = nestling, no origin tag' \\\n ; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:20:04.565Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b5d71d80a44d841e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/75aed0463242b710.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/584b9d2304d5c29c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d41583dd453aad4e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d5cc63242ed46ede.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/560311b7ae5b47e8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fe6cbcfe68dab237.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fbd77c143863436f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4b7f67f4e4828106.txt
```


## [2026-09-05T20:20:15.133Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT dus ===\"; grep -n \"duš\\|duš-\\|dus-\" KNT.txt | head -8; echo \"=== HUB dus ===\"; grep -n \"duzd\\|duš\\|dus-\" HUB.txt | head -8",
 "description": "Kent and Hubschmann for dus"
}
```


### [2026-09-05T20:20:15.192Z] TOOL RESULT

```
=== KNT dus ===
530:бїйрї i is found for the gen. iy’ = act. -tiy, mid. -laiy, personal ending of the third singular. pruc* = риса, but would represent also paura if ~ such a word had to be written. | $25. PosTCONSONANTAL у was written as -ty-; thus any? = aniya, Skt. anyás, d'usiyarm = duSiyéram famine’, from *dus- + 1йг- ‘year’, But hy was not nd Му, since 1 was not
1068:established’ (on -$-, §117), Skt. dsddayam. pIE insep. prefix *dus- ‘ill’, ОР duš-, Av. dus,
1401:root, kan- ‘dig’ + pass. -ya-, in akaniya ‘was dug’. *duS- ll’ + *yür- ‘year’, in dušiyãram ‘famine’. wamarsiyus nsm. ‘by self-death’, Skt. mriyú-š
1696:ҮП. Initial y- after a final consonant of the prior element must of course appear as -2y-, as in dusiydram, from duš- + уйат.
1876:5169. Noun AND Apsective COMPOUNDS IN ОР, apart from phrasal adverbs (§191.1V), may have as prior element an inseparable adverb as in a- zsata- ,"u-cüra-, dus-iydra-, ham-arana- (8268); or a prepositional adverb, as in apa-dàna-, pati-kara- (5268); or a noun or adjective stem! They have as second element a noun or adjective stem, which may receive an additional suffix.
1983:U(v)ja Elam’, including city (usa, village Abird- duš. | III. Semitic provinces:
2010:57 Same as Fem. as Derivative Pl. Ethnic Masc. as Province Ethnic Province Ethnic as Province Province Babirus X Babiruviya Maka Maciya* Мастӣ Майа X Mudraya X Mudraya Yauna X Yauna Saka X Saká Saka Sug(u)da Skudra x* Sparda Spardtya Zraka x* Натайа Harawats§ Harauvatiya* Hiduš Hiduya*
2834:duš- ll’.
=== HUB dus ===
4883:Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
7016:= zd. handcLma-^ u. s. w. ; duzd *Dieb' = zd. duzd& *Bose-
7336:schwierig', zd. duzddra- (vgl. § 108); paz. padasx^drgar
8153:Ind. 213, 217; duzd 'Dieb' =^ zd. duzd& (phi. geschrieben
8155:diiS' *iibel, bose* H. 565 = ap. dus-, zd. duz- und dm-^
8156:phi. dm- Gl. and Ind. 276 flg., paz. dus- Shk. 242, arm.
```


## [2026-09-05T20:20:16.515Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW dys ===\"; grep -n \"dysenteria\\|dys-\" LEW_1910.txt LAT.txt | head -8; echo \"=== NYB zuzag ===\"; grep -ni \"zuzag\\|igel\\|hedgehog\" NYB_vol2_glossary.txt | head -8",
 "description": "Latin dicts and Nyberg hedgehog"
}
```


### [2026-09-05T20:20:16.580Z] TOOL RESULT

```
=== LEW dys ===
=== NYB zuzag ===
```


## [2026-09-05T20:20:24.664Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7330,7340p' HUB.txt; echo \"=== 8150-8160 ===\"; sed -n '8150,8160p' HUB.txt",
 "description": "Hubschmann context"
}
```


### [2026-09-05T20:20:24.717Z] TOOL RESULT

```
kuchen', zd. zao&ra- 'Opferspende, Opfertrank, Weihwasser.
Ueber gohar s. oben p. 96.
Ausser in pUr, Sdpui% MUddy Ardaslr und zdr liegt r
fiir hr noch vor in: ddra 'Gehalt* = zd. dddra- 'Gabe';
x^dr *leicht*, phi. x^'dr, zd. x^dd^ja-; dusvdr, dnsx^dr^schwie-
rig', phi. dusx^dr Gl. and Ind. 277, arm. dzvar *schwer,
schwierig', zd. duzddra- (vgl. § 108); paz. padasx^drgar
Min. Gl. 151, phi. patasx^drgar Phi. Vd. p. 6, Z.3-2 v. u.,
BB. 4, 47, padaSx^'drgar Bdh. p. 22, 1 ; 23, 9 ein Gebirge
in Gelan --^ zd. "^paitisx^ddra-] arm. Parxar ein Gebirge
nahe dem Lande der Chalder [xalti-K) Laz. Pharp. 219 —
=== 8150-8160 ===
z oder z: muzd^ muzd Lohn, Preis*, muzda (mizda) frohe
Botschaft' = zd. mizda-^ gr. juta&og, idg. ^mizdho-, phi.
m(u)zd, muzd (mit dem Zeichen fiir z geschrieben) 61. and
Ind. 213, 217; duzd 'Dieb' =^ zd. duzd& (phi. geschrieben
duct Gl. and Ind. 274, wegen t verdachtig); duz- neben
diiS' *iibel, bose* H. 565 = ap. dus-, zd. duz- und dm-^
phi. dm- Gl. and Ind. 276 flg., paz. dus- Shk. 242, arm.
dz^ neben fs- (also phi. "^diiz- neben dws-); arm. nzdeh
*Fremdling (5. Jhd.) = ap. '*mzdahyu' = zd. *nisdanhu-
'der ausserhalb des Landes ist'.^ 229 ~
§ 120. Ap. i (= idg. g^^ g^h) im Aniaut = np. j,
```


## [2026-09-05T20:20:34.902Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo -n \"leaf for 7336: \"; awk 'NR<=7336' HUB.txt | tr -cd '\\f' | wc -c; echo -n \"leaf for 8153: \"; awk 'NR<=8153' HUB.txt | tr -cd '\\f' | wc -c; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['HUB'].get('page_offset'))\"",
 "description": "HUB page offsets"
}
```


### [2026-09-05T20:20:36.547Z] TOOL RESULT

```
leaf for 7336: 216
leaf for 8153: 238
leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-05T20:20:58.061Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT dys ===\"; grep -o \"DYS[^.]\\{0,120\\}\\|dys-[^.]\\{0,120\\}\" SKT.txt | head -5; echo \"=== HRN xem ===\"; grep -n \"x'em\\|xem\\|hem 'Natur\\|Gemüt\" HRN.txt | head -8; echo \"=== BRT haema ===\"; grep -n \"haSma-\\|haema-\\|hafma-\" BRT.txt | head -6",
 "description": "Skeat dys, Horn xem, Bartholomae haema"
}
```


### [2026-09-05T20:20:59.841Z] TOOL RESULT

```
=== SKT dys ===
=== HRN xem ===
31:Dies ist ein digitales Exemplar eines Buches, das seit Generationen in den Realen der Bibliotheken aufbewahrt wurde, bevor es von Google im
4114:xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
8360:965. -man '-Sinn, Gemüt' in peiijman, sad\man, qehr\man
12775:xemlden 446.
=== BRT haema ===
```


## [2026-09-05T20:21:04.261Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *4[0-9][0-9]\\. \\|xim\\b\" HRN.txt | head -3; echo \"--- around 4114 ---\"; sed -n '4105,4125p' HRN.txt; echo \"=== find entry xem ===\"; grep -n \"xim\\|x[iî]m \" HRN.txt | head -10",
 "description": "Horn xem context"
}
```


### [2026-09-05T20:21:04.331Z] TOOL RESULT

```
3739:400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
3744:401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
3749:402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
--- around 4114 ---
Säle mann, Mol. asiat. IX, 233 Note 20.
446. cernber (geschrieben cenber) 'Kreis, Ring (z. B. Vis
und Ramin, S. 89 Vers 1)'.
V
phlv. cambar head-fiUet' (Säy. näSäy. HI, 4).
Zu np. cep 'links' (No. 435), gr. yAfiiJxct) 'biege',
adfinvXog (Nöldeke, mündliche Mitteilung).
Fick setzt als Wurzel für ai. capa- und gr. ad^iTiTO)
qep' an. Zu derselben Wurzel wird übrigens auch np.
xem, x^mm {*xeinp) — verschrieben in cem, Vullers s. v.
No. 12 — 'krumm, gebogen, yemtden etc. gehören.
447. eend 'einige*; wie viel?*, cendän, dendm, cendi,
aw. cvant' 'wie viel?'; phlv. cand.
kurd. LW. dend , dm; bei. cunt 'wie viel?' (64);
af;'. cof»[ira, com\ra wie viel?*; wa/. vum^ ciin, sar.
cund.
448. cöh 'Holz*.
phlv. 6öp 'Holz' (Guj. Ab.); kurd. cö, siw (H.-Sch.);
bei. LW. vöp (66); wa/. ^öpk, sar. /Jih,
7*--- 100 -^
Lässt sich lautlich nicht mit skr. kSupa- 'Staude,
=== find entry xem ===
```


## [2026-09-05T20:21:18.919Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"•  j.  yäta-\\|j\\.  yäta-\\|yäta-  n\\.\\|yäta-  m\\.\" BRT.txt | head -5; echo \"=== PHD yad ===\"; grep -o \"yàd \\[[^]]*\\][^.]\\{0,80\\}\\|yad \\[[^]]*\\][^.]\\{0,80\\}\" PHD.txt | head -5",
 "description": "Bartholomae yata, MacKenzie yad"
}
```


### [2026-09-05T20:21:20.947Z] TOOL RESULT

```
21540:•  j.  'yäta-  n.  'der  Jemandem  zugewiesene Anteil;  Besitz':  myazdavh  raiui  amyasda- vatam  raiunaim  *tfm  gal'hanqm  frapirf- naotti  ". .  verurteilt  den . .  Laien  zum  Ver- lust seines  Anteils  an  Hab  und  Gut"  A. ^.11;  —  bao6asca  urvStitmla  'Um  gaz'ia- natu  paiti.jaihydnti  dahm  astvainti  aahvB **, .  befragen  sie  nach  dem  Anteil  an  Hab und  Gut,  der  (dem  Verstorbenen)  . .  ver- lieben war"  V.jp.  29";  F.^f
21542:•  j.  'yäta-  n.  Terni.  techn.  für  die  der Schwere  nach  dritte  Art  von  Körperver- letzung"; %rUäm  tarS  x^araya  (sd.)  .  . vUp)m  larS  *yär?Jräjahehim  °t)m  ästrydti N.42i  F.4f.i  —  'fa  raifqm  . .  N.77T{?).
=== PHD yad ===
yad [yt' | P yd] until; so that
```


## [2026-09-05T20:21:28.643Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"ayād[^.]\\{0,90\\}\\|ay[āa]d \\[[^]]*\\][^.]\\{0,80\\}\" PHD.txt | head -5; echo \"=== xem ===\"; grep -o \"xém \\[[^]]*\\][^.]\\{0,60\\}\\|xēm \\[[^]]*\\][^.]\\{0,60\\}\" PHD.txt | head -3",
 "description": "MacKenzie ayad and xem"
}
```


### [2026-09-05T20:21:30.689Z] TOOL RESULT

```
ayād [?7’byd’t'] forgotten
ayād Pbyd?t' | M? yd, N yad] memory
ayād [plyd’t' | M pry'd, N faryàd] help, assistance
ayād- [plyd?t-ytn! | M pry'd-] help, assist
ayādaģ [pd’tk! | М py’dg, N piyada] on foot, foot-soldier, (chess) pawn
=== xem ===
xém [-hym] evil-natured
xém [hwhym] of good character, good-natured
xém [лут] nature, character
```


## [2026-09-05T20:21:34.699Z] TOOL CALL #78: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:21:34.745Z] TOOL RESULT

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


## [2026-09-05T20:21:37.340Z] TOOL CALL #79: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-05T20:21:37.382Z] TOOL RESULT

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


## [2026-09-05T20:22:33.809Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"duS\\.v\\|dus\\.v\\|duz\\.v\\|duivar\\|duS-vär\" BRT.txt | head -8; echo \"=== dus.vacah ===\"; grep -n \"duivacah\\|duS.vacah\" BRT.txt | head -3",
 "description": "Bartholomae dus-v compounds"
}
```


### [2026-09-05T20:22:33.880Z] TOOL RESULT

```
4836:•  Ji  g-  '^Y'  subst  Fron,  dem.,  nur  enkL Akk.  mask.  und  neutr.'*,  'ihn,  es;  sie', hinter  dem  ersten  (hochtonigen)  Wort  des Satz-  und  Versteils'*;  i)  zurückweisend, a)  auf  ein  Nomen:  atjhiuS  ,  ,  yS  im  dät Y.45.4;  —  mq>r)7n  ..ya^ä  Tm  mlnätHä vaocacä  Y. 43.3;  —  yastat  .  .  yi  .  .  ku tSin . .  *maimS  atihal  paouruyi  vTdvä  avatn yn  im  anhat  ap^mii  (sA.)  Y. 44.1g;  — yS,.dasdi  *a!na»iAi  tiöit  ahyä .. paityaogit (sd.)  ta  akmai  JasSit  . .  ya  im  pmySl  Y. 46,%;  5/.12  (valpys),  46.^{ayaiit^m),  ig. i2f.J  (a/iurym)i  —  vahistim  %wa..yäs3 . .  f»rala6str3i  maibyacd  yaiibyas^ä  J?  ri- aha^m  Y.2ÄS;  4j.  10  {ahm),  J5.6} {vohs);  —  nä  zil  ^almainX  vyädamtm vatfhSuS  mainySus  iyao^anahyä  tixfiahyScS "denn  nun  will  ich  es  (xla'i:r?m)  mit  dem Auge  erschauen,  (das  Reich)  des  guten Gedankens,  Werks  undWotts"  Y.4$.Z^^; —  aya  nStt  3r?s  vlsyätä  daivännä  hyat if  ä.dfbaoma  {sä.)  ..  ups.jasat  Y.jo.6; 31.1&  idr?gvatS),  32.1$  (maraxtJrff),  44, 4  {drggvasa),  46.  12  {naptyai^ü),  31.  14 {karapans),  ^.8  {duivarMai^hö),  33.9 {duivar?näi/)i   —    slU^fnf  . .  mraeml . .
13769:•  j.  duä-mata-  Adj.  'übel  gedacht':  aibi- gairya(sd.)  daii^  vJspä  kumatäcä . . paili- ricya  dtü^l  i'lsfä  'tä^a  Y.  /;.  1 7 ;  —  lirayqm aiiitanqm  aiwii^yS  buyata  'taheca  tnana- nhs  .  .  y.  18.  ij;  —  ysi  aipi.k?rmhnti vUp?m  'Um  .  .  duioxltm  .  .  duivarststn  Y, 7/.  8;  7,  V.J.  2o,  4a,  7.53  PiiZ.,  Yt/0.io6;
16609:•  j,  bao8ö.var§ta-  Adj.  'mit  Erkenntnis, £jnsicht  (in  die  Folgen)  getan':  nispa kumata  .  .  hoxta  .  .  kvarsta  -ta  vjspa du^mata  . .  duiüxia  ,  .  duivarsta  nSii  'ta FrW.^.  I.  a)  als  ntr.  Subst'»  im  Straf- gesetz eine  mit  (trotz)  Erkenntnis  der Folgen  begangene  strafbare  Handlung, insbes.  Körperverletzung,  'vorsätzliche Körperverletzung'*':  Hkayat  sunahe  ralsS Hake  ^ihaya  ".  .  mit  der  Strafe  für  vor- sätzliche Körperverletzung"  V./j.ro;  7.38, 1$.  13,  22,  Vyt.4^,  F.2C,  25a,
18234:Pü.!  frih  duivaril.  —  i)  Vgl.  ia/räyd.liiimala:
19041:US  (Sp.  426  M.)  asraesyanam  tanunam  asahe  yS  n°  jyölämi^ä.)  hanar}  vtnasti . .  olnatshB .  .''vlZaiti'^  'S.  15;  N. ^2,  Nik.i;  —  «"  «S  . ,,  Y.^/.  15;  —  yöi  n*  aspm  mainyanta  (sd.) aSvan'  dva  n°*  ..asahe  tf  asayS  fräl3fiii'>  ■\.34-^\  —  yallam  n'  kvarstäis  vai  (sd.) (Sp.  360  u.)  V.44;  V.J5. 48»;  —  n°  na  duivarstä  ¥.49.4;  —  tacit  . .  ya  n°  va
19047:—  atat  dim  «•  räsaymte  Yt/0.21;  —  jAw.;  zu  I);  yS  «°  pashUa  hus^afa aß  narym  n°  jainti  V. 5.  8;  9;  —  jvascil\yat  .  .  Y. 57.  17;  N. 24;  —  yS  «•  kahmai tr  bvat  asava  (Sp.  253  o.)  mfsascit  «• '  (Sp.  426  u.)  mikrB.druJqm  ..  ae/S  daÖaiti baxlaiti  vahistahe  argkSus  V.5.  61;  Y\.io.n'  xävarp  Yt /O.  6a;  62';  —  yS  n'  jv5 3o3;  —  mit  Ellipse  der  Kopula:  vlspa*  sraosyqm  tavirgzyeiti  V.  f^.  3;  p.  47,  18.') duivarstä  n'  baote.varsta  FrW.  J.  i ;  — ;  (s.  2),  P.  48;  —  yS  n'  narvm  asavan»m  . . vtrahrarjnS ..n'  narS{y<iV.) yesnyS  vahmy5\xSnaolta  vä  xsnavayeUe  va  P.45;  —  ^'"«
20768:jAiw.;  das  Relativ  ist  a)  substantivisch: yOi  däityayaona  ''car^nta  ..noil  aitaEsqm.. N.52;—  s.  noch  N.55(Sp.  1205  0. j; — mit  Gen.  part:  yatca  aSaliqm  ra%wqm faoiryö  paiti  ä./asät  hävanänim  (sd.)  a^m astayeiti  N.  ^2;  —  die  Beziehung  ist  un- genau: yä(AFn.)  *malz5  vä  ..  *srävayeiti aUaiiqm  (Sp.  1 4  u.)  vacqm . .  N.  J7.  ß)  ad- jektivisch :  yä  (NDm.)  nara  iämSjfarn^a . . hamqm  aSe  *x^äudrim  (sd.)  saoisram  ba- rälB'lü.64.  e)  ta-  (Sp.617  m.);'A)  im gA^.;  das  Relativ  ist  et)  substantivisch: yastap''  mxidsm  . .  nsit  däill  ia  iim . .  Y. 44. 19;  — yBi  aisirMtn  varadm  ..yaisqtn nSit  Avarstäis  vas  duivar/ia  tst . .  Y.  4g. 4; —  ffyi  urvafymisd.)  cazdsnnhvadi^s tainS-.vaocH  Y.J/.3; — ^^(NPn.)  vS  abi- frä  ta  xsairakya  'Y.33. 13;  — yn  (APn.)W( asä  ya  asäi  g7ul  tasä  (sd.)  mraot ..  tä  . . Y.  46.  g;  31.7,  44.6; — yqscä  haxSai  . . fi-5  mis  vJspäis..  Y.46. 10;  —  yfngs/S"'^ ..  hadimöi  mina/fsd.)  ..  ßng  zbayä  Y. 46.14;  —  mit  Gen.  part:  hyat  vä  tsi nämanqm  väzut>tn  .  .  tä  'hwa  pairijasä- maidl  Y.36.3;  —  die  Beziehung  ist  un- genau: ylf  akftn  dr>gväiti . .  zastSibyä  (sd.) va  varisaitl  vanhäu  va  cöihait!{sd.)  asftm tdi  varäi(sd.)  rädtnilY.ss.z*'^; — yehya . ,  vahist3in  valda  (sd.)  mazda  . .  tq  yatäi Y.  5/,  2a*>;  —  hyaX"'>  miidsm  ..  magavabyö (sd.)  Mit  para  ta  vf..saväi/*c>vTii(,s±) Y. 5/.  15;  —  yam"^  da  .. ränSibya  xSnüt^ni /i>'o/(Sp. I20I  m.)  urvatim  ..tat  n} .,  vaocä Y.^J.3;  vgL57.9  (Sp.  1216  m.);  —  ya (zu  ß)  frasä  (sd.)  avl^ya  yä  (zu  ß)  . .  *p)r?- salte..y}  vä  ..  ayaniaite*baßm  /J(APn.) . .  valnahi  Y.31. 13  "''.  3)  adjektivisch: yäsc'ä  tat  g?nä  . .  vairya  tä  yazamaide  Y. 38.  r ;  —  yä  vS  .  .  *namqm  dadät . .  täis va yasamaidlY. 38.  i,\—  yä  ihids  dadtnts da%ranqm  (sd.)  hacä  ai'äunS  yäs{za.  it)a . .  dngvSJjbyö  ya%a   tä  a»Am  Y.j/.  14;
22358:asavatum  .  .  yd  anhat  °/j  arsvacH  (sd.) V.  ^.  2;  —  sonst  nur  neben  manah- (zum  Wortlaut  der  Stellen  s.  Sp.  11 39 unter  o)  und  ^aohna-:  yänJm  manö  .  , •CS  ,  .  ^ae%p>m  zar^uitrahe  Y.  i8.  o; V.7.  51',  Äioo,  Yty.  83; — ma  apama .  .  mä  manaaha  .  .  'canha  ,  ,  Syao%na ^mäha  ka%acina  *paiti.jime  Vr.  22,  a;  Y. 1.21,  Ji.  18  (•caaAä);  —  vJ  Jasväi/ .  . iarim  mruyl  .  .  vT  matisbli  .  .  °cSbll  ,  . ^ao%anaU  Y. /2. 4;  —  pairl  manä  .  . °/ä  .  .  iyao^ana  .  .  dadsmahl  Y.  $8.(s;  — nazdys  ahmt  .  .  atahlui  astvats  *matiasca 'cäs/a'>  *iyao%naca  ya^a  .  .  P.  2<S';  — t^m  yazala  .  .  zarahustrS  V3r7'hraynake paiti  manahi  . .  'caki  . .  ^aohne  Yt- 14.  a8; —  vavatu  buye  ra%wya  manaaha  .  . °iaf)ha  .  .  syaö>na  A.  ;.  1 1 ;  —  yas^a  .  . imat . .  vacö  (s,  Sp.  1341c)  fravaocäi  asa.- sara  manaaha  .  .  'canha  .  .  fyadhna  Yt. 11.4;  —  sSksi  manarthe  .  .  -cofske  .  . syaohnahe  H.68.4;  —  iistuyi  humaüm manS  hüxtim  'l5  Avarsüm  iyaü%anfm  Y. J2.  8;  Vr,  2.  s;  —  ma  %rayqm  vaAista- nam  aiwi^yS  iuyata  humataheca  manaighs hüxtaheca  'canhs  kvarstakeca  syaö^nahe %rayqm  aiistanqm  aiwi^yO  buyata  dul- mataheca  mananhö  duzüxtaheca  'caahd duivarsiahe'a  syaehnahe  V.  iK  17;  Yt. 16. 5,  3)    'Ausspruch,    Spruch,    Wort,
=== dus.vacah ===
```


## [2026-09-05T20:23:12.619Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 523 524 525 526; do echo \"### leaf $L (p$((L+540)))\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | grep -o \"ژوژ[^ ‪]*\\|ژوز[^ ‪]*\\|خارپشت\" | sort -u | head; done",
 "description": "BQT leaves near 1063 for zhuzh"
}
```


### [2026-09-05T20:23:14.409Z] TOOL RESULT

```
### leaf 523 (p1063)
### leaf 524 (p1064)
### leaf 525 (p1065)
### leaf 526 (p1066)
ژوژه
```


## [2026-09-05T20:23:17.193Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==526' BQT_v2_pages.txt | grep -n \"ژوژه\" -B6 -A10",
 "description": "BQT zhuzhe entry"
}
```


### [2026-09-05T20:23:19.159Z] TOOL RESULT

```
41-  ‫کاین مشك حشو شبی است ازخم ژواغار ‪».‬‬                    ‫گفتاکه یکی مشکی است نی‌مشك تبتی(؟)‬
42-         ‫‪ = ۴‬زولك «لنت‌نامه» ‪:‬‬      ‫نامه ‪.‬‬             ‫ء رك‪ :‬لفت‬       ‫برای تصحیح ست‬        ‫‪٩۱6‬‏‬      ‫لفت فرس‬
43-
44-  ‫وآن زررك(ژولك) وآن صموه از آن داده اذان را ‪-‬‬                         ‫شارك چو مؤذن بحر حلق کشوده‬
45-  ‫سنایی‌غز لوی‪ » .‬لفت نامه ‪. ۴‬‬
46-
47:  ‫‪ - ۱‬اومتا ‪ » 268۷0‬د رگرارش‬                    ‫‪۰‬‬   ‫رك ‪ :‬خارشت‬         ‫® _‬           ‫‪ ۴‬رك ‪ :‬ژوژه ‪.‬‬
48-  ‫پهلوی ( = زند = فير )‪62‬لا ‪ ۰‬دربندهشن پپلوی(فصل ‪۱‬ب‪٤‬ن‏د‪ )۹۱‬ده جنس‌سکه برشمرده‬
49:   ‫شده و در میان آنها از ژوژه نیز تام برده شده کوبدآن را خاریشت خوانند‪ .‬رك ‪ :‬فاب ‪۱‬ص ‪۲۱۷‬‬
50-  ‫‪e‬‏ طدری ‪îjemra‬‏ (خاریشت) ‪ +‬ماز سرانی‬              ‫کردی ع ازاز «‪nıra‬‏ ‪ îhjûhj‬ی اسشق ‪۷‬‬                      ‫‪.۳۱۲-‬‬
51-  ‫اسم‌مقمول از «ژرلیدن» ‪.‬‬     ‫‪۸‬‬     ‫‪ = ۲۷‬جرایدن(ه‪.‬م‪. ).‬‬                 ‫کنونی ‪« 0760۳72‬واژه‌نامهه‪. »۱‬‬
52-                ‫کوید ‪:‬‬    ‫(بلخی)‬   ‫عنصری‬   ‫‪۰‬‬   ‫«زو؛دربابود‬   ‫‪:‬‬   ‫زو(‬   ‫‪ ۹۳‬بقتح اول (ر که ‪:‬‬       ‫ژو‬   ‫‪2‬‬
53-
54-
55-                                                ‫ملاح تىز اند که رو(پیراند که کو ‪ .‬دهشدا! )‬                 ‫هرد‬
56-
57-  ‫«لفت فرس ‪ ۸۱46‬وکره‪ :‬لفت‌نامه ‪.‬‬                ‫راد برباد کشتی ألدر ژو ‪.‬‬
58-
59-
```


## [2026-09-05T20:23:31.344Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zwzk\\|ژوژ\\|جوج\\|uzag\\|üzag\\|zag \" SNS_pages.txt | head -10; echo \"--- leaves ---\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt",
 "description": "SNS search for zuzag"
}
```


### [2026-09-05T20:23:32.918Z] TOOL RESULT

```
1809:                          •ij'-^jj '0**4^ ««.*i>T^ ;                       avSzag dad: joxj-Som*           (Mir. Man.                           J
1834:         mOzag +tf, ab§         -*i**b «j^oj->* -*i>\*                       :ab§mOzag: 4«.
12864:                                                                                          ducra:blzag                 :    cl^ ;';  1                1
15648:                                                            zQzag 168/10
15679:xasm 87/15               xVfibSnd 44/4                       x v arisn andazag 70/12    yat 295/10
15730:                          vidardagan 268/19              vissadfin 274/4           vuhunzag 263/9
15784:                                                              v3zag 258/12              vardfid 279/20
15807:sSdarvan 196/9        savSnd 203/20-272/3              s&zag 202/13           tabah 147/13
15902:prtzag 138/1               ran 224/5                         rasn-astad 227/10      rO n 239/1
15911:pursld 141/10              ratustaitlh 226/6                 ravisn 229/7           rOzag 230/12
--- leaves ---
242
```


## [2026-09-05T20:23:37.302Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"zQzag\\|zOzag\\|zuzag\\|zGzag\" SNS_pages.txt | head -10",
 "description": "SNS zuzag entry"
}
```


### [2026-09-05T20:23:37.351Z] TOOL RESULT

```
15648:                                                            zQzag 168/10
```


## [2026-09-05T20:23:41.900Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خارپشت\\|خارپشتك\\|zag:\" SNS_pages.txt | head -20",
 "description": "SNS hedgehog"
}
```


### [2026-09-05T20:23:41.952Z] TOOL RESULT

```
1801:                                                                           :ab$zag/avSzag: •>«...          /\»*S   .   jp^i-wT .j^ji^T : 3pus bav£d:                  **«**-> -oie^*
1834:         mOzag +tf, ab§         -*i**b «j^oj->* -*i>\*                       :ab§mOzag: 4«.
9866:                                                  .jX.'jr :mozag:                                                                                                                f lfto«4«r           (1)
10005:                                                 t/ftl5   1(   wt<*> :mizag:
10239:                                                                                                                           •flo/IT^               u/A^ .ijy.^lj :vazag:                                     4d>M
10390:                                                          ^       1    rvuhunzag:            ^W         (£W •&*»«&) *K^*>*j:vuhuxsatr-gah:                        -o-M_>\enj.»-ot«
10950:                                                                                                                           -,          sSnlzag: t3ot^*                   :   o.jjb^bi^lj o-'Jfe^f                      ^daM
12866:                                                                                                                                                                     •*>*••» :dubezag:                          ?        -9«-j_)V
13299:                                                                                                                                                                                                           :gomizag: ££>•£*
```


## [2026-09-05T20:23:54.542Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:30:10.187Z] TOOL CALL #86: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk143.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_DOZD=\"https://en.wiktionary.org/wiki/%D8%AF%D8%B2%D8%AF\"\nW_DOZAX=\"https://en.wiktionary.org/wiki/%D8%AF%D9%88%D8%B2%D8%AE\"\nW_JUJE=\"https://en.wiktionary.org/wiki/%D8%AC%D9%88%D8%AC%D9%87\"\nETY=\"https://www.etymonline.com/word/dys-\"\nW_DUS=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dus-\"\nA_ZHU=\"https://abadis.ir/fatofa/%DA%98%D9%88%DA%98%D9%87/\"\nW_DOMAL=\"https://en.wiktionary.org/wiki/%D8%AF%D9%85%D9%84\"\nW_DOSHVAR=\"https://en.wiktionary.org/wiki/%D8%AF%D8%B4%D9%88%D8%A7%D8%B1\"\nA_JUJE=\"https://abadis.ir/fatofa/%D8%AC%D9%88%D8%AC%D9%87/\"\n\nnodes=[]\n\nnodes.append({\n \"id\":1,\"lang\":\"Avestan\",\n \"words\":\"duš, duž, duždâo; duš-manah; duš-nâma; duš-vâre; duš-xv-athra, duž-âthra\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Av. duš- (before voiceless sounds) / duž- (before voiced ones) is the regular Iranian continuant of PIE *dus-, exactly parallel to Skt. duṣ-/dur- and OP duš- (Kent, Old Persian §169 and lexicon: 'PIE insep. prefix *dus- ‘ill’, OP duš-, Av. duš', with OP duš-iyāram 'famine' = duš- + yār- 'year'). duždā̊ is the nom. sg. of duž-dā- 'doing evil' (duž- + the root dā- 'to put, to do'), glossed 'Bösewicht' by Horn and Hübschmann, and it is the etymon of NP dozd (node 2). duš-manah- 'whose thought is evil' is a real Avestan adjective (Bartholomae col. 753-754, cited from Y.49.11, Y.65.7); duš-nāman- 'ill-famed' underlies MP duš-nām; duš-xᵛāθra- / duž-āθra- are genuine — Bartholomae col. 756 has duz-āθra- n. '(schlechtes Atmen sva.) Missbehagen' beside the well-attested xᵛāθra- 'Behagen, Glück' (pouruš-xᵛāθra-, vīspa-xᵛāθra-), so Nourai's gloss 'not easy' is right. The one bad member is duš-vāre 'difficult to carry' referred to the root Bher 'carry': no *duš-vāra- exists in Bartholomae (the Avestan duž-compounds in v- are duž-vacah- 'evil-speaking' and duž-varšta- 'evil deed'), and Hübschmann, Persische Studien p.206 explicitly puts both forms under one etymon — 'dušvār, dušxᵛār ‘schwierig’, phl. dušxᵛār, arm. dzvar, zd. duzāθra-' — i.e. NP došvār is simply došxvār with xᵛ reduced to v, not a compound of bar- 'to carry'.\",\n \"derivation_fa\":\"پیشوند اوستایی duš-/duž- («بد، ناخوش») دنبالهٔ منظمِ *dus- هندواروپایی است و با duṣ-/dur- سنسکریت و duš- پارسی باستان (کنت: duš-iyāram «قحطی» از duš- + yār- «سال») یکی است؛ پیش از واکِ بی‌واک duš و پیش از واکدار duž می‌آید. صورت duždā̊ (نهادیِ duž-dā- «بدکردار») که هرن و هوبشمان آن را «Bösewicht» گزارده‌اند، خاستگاه «دزد» فارسی است. duš-manah- «بداندیش»، duš-nāman- «بدنام» و duš-xᵛāθra-/duž-āθra- «ناخوشی، ناآسانی» همگی در فرهنگ بارتولمه (ستون‌های ۷۵۳ تا ۷۵۶) ثبت‌اند و معنایی که نورایی داده درست است. اما «duš-vâre» به معنی «سخت‌بَر» و ارجاع آن به ریشهٔ bher «بردن» پذیرفتنی نیست: چنین واژه‌ای در اوستا نیست و هوبشمان در «مطالعات فارسی» ص ۲۰۶ آشکارا هر دو صورتِ دشوار و دشخوار را از همان duž-āθra-/duš-xᵛāθra- می‌گیرد، یعنی «دشوار» همان «دشخوار» است با کاهش خوا > وا. بنابراین این یک بند از گرهٔ ۱ را پژوهش امروزی رد می‌کند.\",\n \"sources\":[W_DOSHVAR,W_DUS],\n \"ref_check\":[\n  {\"ref\":\"POK:227\",\"status\":\"supports\",\"note\":\"POK_01.txt line 3254 (printed p.227): 'dus- ‘übel, miß-’ als 1. Kompositionsglied. Ai. dus-, dur-, av. duš-, duz- ‘miß-, übel’ ... gr. δυσ- ... Zusammenhang mit deus- ‘ermangeln’ ist sehr wahrscheinlich.' — exactly the arrow root→Avestan as drawn.\"},\n  {\"ref\":\"FSF:179, 183\",\"status\":\"partial\",\"note\":\"Noushin, Vazhe-namak, leaf 238 of FSF_pages.txt (≈ printed p.183/184): headwords «دژ = دز» (fortress), «دژآگاه (باپیش اول) ۱- سهمگین، خشمگین، بیمناک، هراس‌آور» and «دژخیم: روزبان، جلاد», and at line 10984 «جزء دوم واژهٔ مرکب دژخیم ... بدنهاد». The glossary documents the Persian دژ-/دش- prefix but says nothing about the Avestan forms themselves, and nothing about duš-vāre.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"cols. 753-756 (BRT.txt lines 13748-13800)\",\"stance\":\"partial\",\"note\":\"'j. duš-manah-, g. *duz-manah- Adj. ‘des Denken übel ist’ ... Pü. dušmen'; 'g. duš-xᵛarəθa- n. ‘üble Speise’'; 'j. duz-āθra- n. ‘(schlechtes Atmen sva.) Missbehagen’'; 'j. duš.kərət- Adj. ‘übeltuend’'. No entry *duš-vāra- anywhere in the dictionary — the v-compounds are duž-vacah- and duž-varšta-.\"},\n  {\"src\":\"KNT\",\"where\":\"Kent, Old Persian, lexicon s.v. dušiyāra- (KNT.txt lines 1068, 1401)\",\"stance\":\"supports\",\"note\":\"'PIE insep. prefix *dus- ‘ill’, OP duš-, Av. duš'; '*duš- ‘ill’ + *yār- ‘year’, in dušiyāram ‘famine’' — the Old Iranian prefix as the chart draws it.\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien, leaf 216 = p.206 and leaf 238 = p.228 f.\",\"stance\":\"contradicts\",\"note\":\"p.206: 'xᵛār ‘leicht’, phl. xᵛār, zd. xᵛāθra-; dušvār, dušxᵛār ‘schwierig’, phl. dušxᵛār ..., zd. duzāθra- (vgl. §108)' — one etymon for both, against Nourai's separate duš-vāre from bher-. p.228: 'duzd ‘Dieb’ = zd. duzdā̊; duz- neben duš- ‘übel, böse’ = ap. duš-, zd. duz- und duš-, phl. duš-'.\"}\n ]\n})\n\nnodes.append({\n \"id\":2,\"lang\":\"Persian\",\n \"words\":\"dozd «دزد»; došman «دشمن (دُژمان، دُژم، دُژمناک)»; došnâm «دشنام ( دُژنام )»; došvâr «دشوار ( دُژوار )»; došxâr «دشخوار»\",\n \"verdict\":\"plausible\",\n \"derivation\":\"All five are duš-/duž- compounds inherited through Middle Persian, and MacKenzie's Pahlavi dictionary prints the whole set on one page (PHD p.28-29): 'duz(d) [dwc(t) | M dwz, N duzd] thief', 'dušmen [dwšm(y)n' | N dušman] enemy', 'duš-nām [-nʾm | N ~] abuse, insult', 'dušwār [dwšwʾl | M dwšwʾr, N ~] difficult', 'duš-xwar [...| N ~] = dušwār'. Phonetics: Av. -ž- > MP/NP -z- (Horn no.504 compares mižda- > مزد and Mazdā̊ > (Hor)muzd for the loss of the final -ā̊), so duždā̊ > MP duzd > NP دزد; Av. duš-manah- > MP dušmen > NP دشمن (Mo'in's footnote in Borhan p.867: «دشمن ... پهلوی dušmen ... از اوستا duš-manah- بارتولمه»); duš-nāman- > duš-nām > دشنام. The doublets دژ-/دش- reflect the old voiced/voiceless alternation and are still both productive (Borhan p.852 footnote: «دژ = دش، پارسی باستان duš، اوستا duš/duž، آریایی duš/dur، پهلوی duš؛ در کلمات مرکب مانند دژخیم، دشنام، دشمن و دژآگاه»). Only the split of došvâr from došxâr is wrong: they are one word (MP dušwār / dušxwār), so the two boxes should not go back to two different Avestan etyma. The extra forms دُژآگاه، دُژآلود، دُژآهنگ، دُژبرو are all on Borhan p.853, exactly as Nourai cites.\",\n \"derivation_fa\":\"هر پنج واژه ترکیب‌هایی با پیشوند دش-/دژ- اند که از راه فارسی میانه به فارسی نو رسیده‌اند؛ مکنزی همهٔ آنها را در یک صفحه آورده است: duz(d) «دزد»، dušmen «دشمن»، duš-nām «دشنام»، dušwār و duš-xwar «دشوار». از نظر آوایی، ژِ اوستایی در فارسی میانه و نو به ز بدل شده (هرن، بند ۵۰۴، آن را با mižda- > مزد و افتادن پایانهٔ -ā̊ در Mazdā̊ > (هر)مزد می‌سنجد)، پس duždā̊ > duzd > «دزد». معین در حاشیهٔ برهان قاطع ص ۸۶۷ «دشمن» را از اوستایی duš-manah- و پهلوی dušmen می‌گیرد و در ص ۸۵۲ می‌نویسد «دژ = دش ... در کلمات مرکب مثل دژخیم، دشنام، دشمن و دژآگاه». دوگانهٔ دژ-/دش- بازماندهٔ همان جفتِ واکدار/بی‌واکِ ایرانی باستان است. تنها ایرادِ کار آن است که «دشوار» و «دشخوار» یک واژه‌اند و نباید به دو ریشهٔ جداگانهٔ اوستایی بازگردانده شوند؛ پس ادعای نورایی با این اصلاح پذیرفتنی است.\",\n \"sources\":[W_DOZD,W_DOSHVAR],\n \"ref_check\":[\n  {\"ref\":\"BQT:850,853,867\",\"status\":\"partial\",\"note\":\"BQT_v2_pages.txt: leaf 313 (= p.853) carries دژآلود، دژآگاه، دژآهنگ، دژبرو exactly as the chart's extra forms; leaf 327 (= p.867) has دشخوار with footnote «دشوار = دش + خوار (ه.م) پهلوی dušxvār ... رک: اسشق و هوبشمان ۹۵» and the دشمن footnote «پهلوی dušmen ... از اوستا duš-manah- بارتولمه». But p.850 (leaf 310) is still the دربوزه/دریگان column; دزد with Mo'in's footnote «پهلوی duzd ... اوستا duždā̊ (بدجنس) ...» stands one page later, on leaf 311 (= p.851).\"},\n  {\"ref\":\"HRN:126\",\"status\":\"supports\",\"note\":\"Horn, Grundriss, leaf 148 = p.126: '504. duzd ‘Dieb’ ... aw. duzdā̊ ‘Bösewicht’; phlv. duz (geschrieben duc) ... np. duzd stimmt lautlich ganz genau zu aw. duzdā̊'; '505. duš-, duž- (dyž-, dež-) ‘übel, böse’ ... Mit duž-, duš- gebildete Composita, deren Zusammensetzung vollständig durchsichtig ist, wie dužxīm, dušnām, dušmen sind im Folgenden nicht aufgeführt.' The cited page carries the arrow for all five words.\"},\n  {\"ref\":\"MON:1536\",\"status\":\"not_checked\",\"note\":\"Mo'in's Farhang-e Farsi is online at vajehyab/abadis without page numbers, and the local scan is the 2-volume Adena reprint with different pagination, so p.1536 of the Amir Kabir edition could not be located.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, p.28-29 (PHD.txt line 318)\",\"stance\":\"supports\",\"note\":\"'duz(d) [GN BA < A gnbʾ; dwc(t) | M dwz, N duzd] thief'; 'dušmen [dwšm(y)nʾ | = M, N dušman] enemy'; 'duš-nām [-nʾm | N ~] abuse, insult'; 'dušwār [dwšwʾl | M dwšwʾr, N ~] difficult'; 'duš-xwar [... | N ~] = dušwār' — the last entry shows došvār and došxâr are one word.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 504-505, p.126\",\"stance\":\"supports\",\"note\":\"see ref_check; Horn adds Kurdish diz 'thief', dizīn 'to steal', Baluchi duz.\"},\n  {\"src\":\"HUB\",\"where\":\"p.228 f. (leaf 238)\",\"stance\":\"supports\",\"note\":\"'duzd ‘Dieb’ = zd. duzdā̊ (phl. geschrieben duct ..., wegen t verdächtig)'.\"},\n  {\"src\":\"BQT\",\"where\":\"leaf 311 (≈ p.851), Mo'in's footnote to دزد\",\"stance\":\"supports\",\"note\":\"«# دزد ـ بضم اول، پهلوی duzd ... اوستا duždā̊ (بدجنس)، کردی diz (سارق)، dizīn (سرقت)، بلوچی duz».\"}\n ]\n})\n\nnodes.append({\n \"id\":3,\"lang\":\"Avestan\",\n \"words\":\"duš-haem; duš-yâta; daoš-ahva, duž-axva; duš-pithwa\",\n \"verdict\":\"disputed\",\n \"derivation\":\"Only the third item is a real Avestan word. Bartholomae col. 755 has 'j. duz-aŋhav- m. ‘Hölle’ ... Eig. ‘schlechtes Sein’ sva. ‘Ort des schlechten Seins’', i.e. duž- + ahu- 'existence', with the vrddhi-form daožaŋhva- of Vd. and Yt.19.44 — this is the etymon of MP dušox and NP دوزخ, and Nourai's 'evil world' gloss and his ☞An 1 cross-reference are right. The other three are Nourai's own back-formations. Bartholomae has no *duš-haēma-; the Persian second element is MP xēm 'nature, character' (MacKenzie p.94 'xēm [hym] nature, character', 'duš-xēm evil-natured', 'hu-xēm of good character'). He has no *duš-yāta- either, and Avestan yāta- means 'the share allotted to someone, property' (col. 1288) or a technical term for a degree of bodily injury — nothing to do with 'backbiting'; NP یاد 'memory' goes back to MP ayād [ʾbyʾdʾtʾ] (MacKenzie p.15), not to yāta-. Finally *duš-piθwa- is absent, and piθwā- is 'feste (nicht flüssige) Speise' (food), while the 'fat' of Persian دژپیه is پیه < MP pīh < Av. pivah- n. 'Fett, Speck' (BRT col. 906) — a different word.\",\n \"derivation_fa\":\"از چهار صورتِ این گره تنها یکی اوستایی راستین است: بارتولمه در ستون ۷۵۵ می‌آورد «duz-aŋhav- m. ‘دوزخ’ ... در اصل ‘بودنِ بد’ یعنی ‘جای بودنِ بد’»، یعنی duž- + ahu- «هستی»، با صورتِ وریدیِ daožaŋhva-؛ همین است نیای فارسی میانهٔ dušox و «دوزخ» فارسی، و گزارشِ نورایی («جهانِ بد») درست است. اما *duš-haēma- و *duš-yāta- و *duš-piθwa- در اوستا نیامده‌اند و ساختهٔ خودِ نویسنده‌اند: جزء دومِ «دژخیم» همان xēm فارسی میانه («خوی، سرشت»، مکنزی ص ۹۴) است؛ yāta- در اوستا «بهرهٔ کسی، دارایی» معنی می‌دهد و «یاد» فارسی از ayād پهلوی است نه از yāta-؛ و piθwā- «خوراکِ سُفت» است، حال آنکه «پیه» در «دژپیه» از pivah- اوستایی («چربی») می‌آید. پس این گره را جز در موردِ دوزخ باید رد کرد.\",\n \"sources\":[W_DOZAX],\n \"ref_check\":[\n  {\"ref\":\"BQT:897\",\"status\":\"supports\",\"note\":\"BQT_v2_pages.txt leaf 357 (= printed p.897), s.v. دوزخ, Mo'in's footnote 6: «پهلوی dwšhwʾ ... از ایرانی باستان *duž-aŋhu- (جهنم)، در اوستای متأخر daožahva- «بارتولمه ۵۷۰»، در ارمنی džoxkʾ از dužoxᵛ، در اوراق تورفان dwžx ... جزو اول = duž (دژ، بد) است» — exactly the arrow duš- → duž-aŋhu-.\"},\n  {\"ref\":\"VIE:31\",\"status\":\"supports\",\"note\":\"Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, pdf leaf 37 = printed p.31: «در اوستا به گونهٔ vahišta-ahu بوده است بمعنی بهترین جهان، در برابر «دوش‌اخو» بدترین جهان که واژهٔ اخیر دگرگون شده و به صورت دوزخ درآمده است» — duš-ahu 'worst world' > دوزخ, the chart's daoš-ahva.\"},\n  {\"ref\":\"TZF:22\",\"status\":\"not_checked\",\"note\":\"Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi: refs_online.json records no local copy and no open scan (ketabnak requires a login), so p.22 could not be read.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"col. 755 s.v. duz-aŋhav-; col. 1288 s.v. yāta-; col. 906 s.v. pivah-; col. ~950 s.v. piθwā-\",\"stance\":\"partial\",\"note\":\"'duz-aŋhav- m. ‘Hölle’ ... Eig. ‘schlechtes Sein’' supports the hell word; but 'ʾyāta- n. ‘der Jemandem zugewiesene Anteil; Besitz’', 'piθwā- f. ‘feste (nicht flüssige) Speise’' and 'pivah- n. ‘Fett, Speck’' show the other three compounds are not Avestan and are wrongly analysed.\"},\n  {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II, glossary p.65 s.v. dōšaxᵛ\",\"stance\":\"supports\",\"note\":\"'dōšaxᵛ [dwšhwʾ] hell ... — Av. (675) daožahva-; MPrth dwjx; MPrs dwswx; Arm. lw. džox-kʾ; Paz. dōžax, NP dōzax.'\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.15 (ayād), p.94 (xēm)\",\"stance\":\"contradicts\",\"note\":\"'ayād [ʾbyʾdʾtʾ | M ʾyd, N yad] memory' and 'xēm [hym] nature, character' — Persian یاد and خیم descend from these, not from Nourai's *duš-yāta- and *duš-haēm.\"}\n ]\n})\n\nnodes.append({\n \"id\":4,\"lang\":\"Pahlavi\",\n \"words\":\"dužax\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"The Middle Persian word for 'hell' is written dwšhwʾ and read dušox / dōšox: MacKenzie p.29 'dušox [dwšhwʾ | M dtwš(w)x] hell. ~ig hellish'; Nyberg's glossary p.65 'dōšaxᵛ [dwšhwʾ] hell ... Av. (675) daožahva-; MPrth dwjx; MPrs dwswx; Arm. lw. džox-kʾ; Paz. dōžax, NP dōzax'. It continues Av. daožaŋhva-/duž-aŋhu- 'bad existence' (node 3) with the regular loss of the intervocalic nasal-stem ending and -ŋh- > -x-. Nourai's spelling dužax with ž is the Manichaean-Parthian shape (dwjx) and the Pazand dōžax rather than the Book-Pahlavi one, but it is not wrong: the ž is what the Armenian loan džoxkʾ and Pazand both presuppose, and it is exactly the stage from which NP دوزخ (with ž > z) comes.\",\n \"derivation_fa\":\"واژهٔ فارسی میانه برای «دوزخ» به خطِ پهلوی dwšhwʾ نوشته می‌شود و dušox/dōšox خوانده می‌شود؛ مکنزی ص ۲۹ آن را «dušox ... hell» و نیبرگ در واژه‌نامهٔ خود ص ۶۵ «dōšaxᵛ ... از اوستایی daožahva-، پارتی مانوی dwjx، ارمنی وام‌گرفته džoxkʾ، پازند dōžax، فارسی نو dōzax» می‌آورد. این صورت دنبالهٔ daožaŋhva-/duž-aŋhu- اوستایی («هستیِ بد») است با تحولِ ŋh به x. صورتی که نورایی نوشته (dužax با ژ) صورتِ پارتی مانوی و پازند است نه صورتِ پهلویِ کتابی، ولی نادرست نیست؛ همین مرحله است که با ابدالِ ژ به ز «دوزخ» فارسی از آن برآمده. ادعای نورایی درست است.\",\n \"sources\":[W_DOZAX],\n \"ref_check\":[\n  {\"ref\":\"SBK:214\",\"status\":\"partial\",\"note\":\"Bahar, Sabk-shenasi I: SBK.txt has no page breaks so p.214 itself could not be isolated, but the relevant passage was found (SBK.txt line ~9725), a table of Pahlavi→Dari sound changes headed «ژ: تبدیل شده است به: ز:» with the example «دوژخ ← دوزخ», which is precisely the change this arrow needs.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, A Concise Pahlavi Dictionary p.29\",\"stance\":\"supports\",\"note\":\"'dušox [dwšhwʾ | M dtwš(w)x] hell. ~ig [-ykʾ] hellish'; the English-Pahlavi index p.132 'hell dušox, dwārišn'.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg II, glossary p.65\",\"stance\":\"supports\",\"note\":\"'dōšaxᵛ [dwšhwʾ] hell 201ʸ, 347·27, 65¹².18 etc. passim ... — Av. (675) daožahva-; MPrth dwjx ... Paz. dōžax, NP dōzax.'\"}\n ]\n})\n\nnodes.append({\n \"id\":5,\"lang\":\"Persian\",\n \"words\":\"dožxîm «دژخیم (دُژخیم)»; došyâd «دشیاد»; dŭzax «دوزخ»; dožpîh «دُژپیه ( دُشپیل ، دُژک ، دُمَل )»\",\n \"verdict\":\"plausible\",\n \"derivation\":\"دوزخ is the only one of the four that really descends from the Pahlavi hell-word of node 4: MP dušox/dōšox > NP dōzax/dūzax, ž/š > z, as Bahar's sound-change table and Horn no.581 ('dōzaχ ‘Hölle’; aw. (aŋhəuš) daozaŋhahe, vergl. duzaŋhu- ‘Hölle’; phlv. dōšaχ (pāz. dūzaχ, dōzaχ)') both state. The other three are duš-compounds of the same prefix but do not come through dužax at all, so the arrow is drawn one level too low: دژخیم = دژ + خیم, i.e. MP duš-xēm 'evil-natured' (MacKenzie p.29), still 'ill-tempered' in the dictionaries and 'executioner, jailer' in the Shahnameh (Noushin, Vazhe-namak p.183 «دژخیم: روزبان، جلاد»); دشیاد = دش + یاد (< MP ayād 'memory'), i.e. 'ill remembrance', speaking ill of the absent; دژپیه/دشپیل = دژ + پیه 'fat' (< MP pīh < Av. pivah-), and Borhan p.866 itself glosses «دشپیل» with the footnote «ضم اول = دژ (بد) چنانکه در: دشمن، دشنام، دشخوار». The variant دُمَّل bracketed with them is not a duš-word at all: it is Arabic دُمَّل from the root د-م-ل, compared by Wiktionary with Persian دنبل — which is what Nourai's own NOTE ('See ‘Dumb’') half-concedes; modern scholarship takes the Arabic side.\",\n \"derivation_fa\":\"از این چهار واژه تنها «دوزخ» به‌راستی دنبالهٔ واژهٔ پهلوی گرهٔ ۴ است: dušox/dōšox پهلوی با ابدالِ ژ/ش به ز به «دوزخ» رسیده، چنانکه بهار در جدولِ دگرگونی‌های آوایی و هرن در بند ۵۸۱ («dōzaχ ‘دوزخ’؛ اوستا daozaŋhahe، پهلوی dōšaχ، پازند dūzaχ») آورده‌اند. سه واژهٔ دیگر ترکیب‌هایی با همان پیشوندِ دژ-اند اما از راهِ «دوزخ» نیامده‌اند و پیکانِ نمودار یک پله پایین‌تر کشیده شده است: «دژخیم» = دژ + خیم (پهلوی duš-xēm «بدسرشت»، مکنزی ص ۲۹) که در شاهنامه معنیِ «جلاد، روزبان» یافته (نوشین، واژه‌نامک ص ۱۸۳)؛ «دشیاد» = دش + یاد (پهلوی ayād)؛ «دژپیه/دشپیل» = دژ + پیه (پهلوی pīh، اوستایی pivah- «چربی») و خودِ برهان قاطع ص ۸۶۶ در حاشیه می‌نویسد «ضم اول = دژ (بد) چنانکه در: دشمن، دشنام، دشخوار». اما «دُمَّل» که در کنارِ آنها آمده اصلاً ایرانی نیست؛ عربی است از ریشهٔ د-م-ل و ویکی‌واژه آن را با «دنبل» فارسی می‌سنجد — همان که خودِ نورایی در یادداشتش نیم‌بند پذیرفته است.\",\n \"sources\":[W_DOZAX,W_DOMAL],\n \"ref_check\":[\n  {\"ref\":\"BQT:896\",\"status\":\"partial\",\"note\":\"the دوزخ article with Mo'in's etymological footnote is on leaf 357 of BQT_v2_pages.txt = printed p.897 (see node 3), not 896; دژخم/دژخیم are on leaf 314 (= p.854) with the footnote «از: دژ (= دش) + خم (ه.م) ... بدنهاد، بدسرشت، بدخلقه», and دشپیل on leaf 326 (= p.866). No article دشیاد was found in the Borhan OCR.\"},\n  {\"ref\":\"HRN:129\",\"status\":\"partial\",\"note\":\"Horn, leaf 151 = p.129, no. 581: 'dōzaχ ‘Hölle’. aw. (aŋhəuš) daozaŋhahe, vergl. duzaŋhu- ‘Hölle’; phlv. dōšaχ (pāz. dūzaχ, dōzaχ)'. The page carries only دوزخ; Horn deliberately omits dužxīm and the other transparent duš-compounds (his no.505).\"},\n  {\"ref\":\"VIE:31\",\"status\":\"supports\",\"note\":\"printed p.31 (pdf leaf 37): «… در برابر «دوش‌اخو» بدترین جهان که واژهٔ اخیر دگرگون شده و به صورت دوزخ درآمده است».\"},\n  {\"ref\":\"TZF:21\",\"status\":\"not_checked\",\"note\":\"no accessible copy of Abolghasemi's Tarikh-e Mokhtasar-e Zaban-e Farsi (see node 3).\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.29 and p.94\",\"stance\":\"supports\",\"note\":\"'duš-|-xēm [-hym] evil-natured'; 'xēm [hym] nature, character'; 'hu-xēm [hwhym] of good character' — دژخیم is duš + xēm, independent of dušox.\"},\n  {\"src\":\"BQT\",\"where\":\"leaf 314 (= p.854) s.v. دژخم/دژخیم; leaf 326 (= p.866) s.v. دشپیل\",\"stance\":\"supports\",\"note\":\"«دژخم ... چه دژ بمعنی بد و خم بمعنی خوی و طبیعت باشد»; footnote to دشپیل: «ضم اول = دژ (بد) چنانکه در: دشمن، دشنام، دشخوار».\"},\n  {\"src\":\"FSF\",\"where\":\"Vazhe-namak leaf 238 ≈ p.183\",\"stance\":\"partial\",\"note\":\"«دژخیم: روزبان، جلاد» with the Ferdowsi lines «به دژخیم فرمود شاه اردشیر / که رو دشمن پادشا را بگیر» — in the Shahnameh the word means 'executioner', not simply 'bad-tempered'.\"}\n ]\n})\n\nnodes.append({\n \"id\":6,\"lang\":\"Avestan\",\n \"words\":\"duž-aka\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Bartholomae col. 755 does have the word: 'j. duzaka- m. (gemeiner oder Spott) Name des sūs vaŋhāpara- (‘Igel’)', attested once, Vd. 18.2, where the hedgehog is given a term of abuse by the 'evil-speaking' (duž-vacah-). But two reservations. (a) The animal is the HEDGEHOG (Igel, خارپشت), a creature of Ahura Mazda and the enemy of ants in the Bundahišn, not the porcupine; Mo'in and Dehkhoda both gloss the Persian reflex ژوژه as خارپشت. (b) The analysis duž- + aka- 'with bad sting-hooks' is Bartholomae's own guess and he marks it as such — 'Et.? Vgl. HORN KZ. 3?.437 ... *duž-aka- ‘der schlimme Haken (Stacheln) hat’?' — which is exactly what the chart's NOTE says, so Nourai has represented his source honestly. Modern Iranian etymology has not improved on it; the initial duz- may equally be opaque, and the Pahlavi/NP forms show the assimilation of the initial consonant to the second (duz- > ž/z).\",\n \"derivation_fa\":\"بارتولمه در ستون ۷۵۵ این واژه را دارد: «duzaka- m. نامِ عامیانه یا ریشخندآمیزِ vaŋhāpara- (خارپشت)»، تنها یک بار در وندیداد ۱۸٫۲. اما دو نکته: نخست آنکه جانورِ مورد نظر «خارپشت» است نه «جوجه‌تیغیِ بزرگ/تشی»؛ معین و دهخدا نیز «ژوژه» را خارپشت می‌گزارند و در بندهشن خارپشت آفریدهٔ اورمزد و دشمنِ مورچگان است. دوم آنکه تحلیلِ duž- + aka- («دارندهٔ چنگک‌های بد») حدسِ خودِ بارتولمه است و او با نشانهٔ پرسش آورده: «Et.? ... *duž-aka- ‘der schlimme Haken (Stacheln) hat’?». پس یادداشتِ نمودار («BRT:755 در این اشتقاق چندان مطمئن نیست») گزارشِ درستی از مأخذ است و این گره با احتیاط پذیرفتنی است.\",\n \"sources\":[A_ZHU],\n \"ref_check\":[\n  {\"ref\":\"BRT:755\",\"status\":\"supports\",\"note\":\"BRT.txt col. 755: 'j. duzaka- m. (gemeiner oder Spott) Name des sūs vaŋhāpara- (‘Igel’): spānəm .. yim vaŋhāparəm .. yim mašyāka avi duž-vacaŋhō ‘kəm nāma aojaiti V.18.2. ... Et.? Vgl. HORN KZ. 3?.437, HBM.AGT.AI 41 ... *duž-aka- ‘der schlimme Haken (Stacheln) hat’? — mp. (Pü.): žūžak; np. žūža; Assimilation der silbenanl. Kons.' The '?' confirms the chart's own caveat.\"},\n  {\"ref\":\"BQT:1063\",\"status\":\"partial\",\"note\":\"the ژوژه article with Mo'in's etymological footnote is on leaf 526 of BQT_v2_pages.txt ≈ printed p.1066, not 1063: «اوستا duzaka، در گزارش پهلوی (= زند) žūžag ... در بندهشن پهلوی (فصل ۱، بند ۹۱) ده جنس سگ برشمرده شده و در میان آنها از ژوژه نیز نام برده شده، گویند آن را خارپشت خوانند».\"}\n ],\n \"consulted\":[\n  {\"src\":\"HRN\",\"where\":\"Grundriss no. 687, leaf 174 = p.152\",\"stance\":\"supports\",\"note\":\"'687. žūže ‘Igel’. ... aw. duzaka- ‘Igel’ (als Schimpfname des Hundes verwandt); phlv. žūžak' — the same chain, and again 'hedgehog'.\"},\n  {\"src\":\"BQT\",\"where\":\"leaf 526 ≈ p.1066, Mo'in's footnote to ژوژه\",\"stance\":\"supports\",\"note\":\"«اوستا duzaka ... پهلوی žūžag ... گویند آن را خارپشت خوانند».\"}\n ]\n})\n\nnodes.append({\n \"id\":7,\"lang\":\"Pahlavi\",\n \"words\":\"žužag, zuzag, jujag\",\n \"verdict\":\"plausible\",\n \"derivation\":\"MacKenzie p.99 has 'zūzag [zwzkʾ | (N žūža)] hedgehog', and the English index p.146 lists 'hedgehog xārpušt, xūkar(ag), zūzag'; Bartholomae quotes the Pahlavi translation (Pü.) of Vd. 18.2 as žūžak. So both žužag and zuzag are genuine Middle Persian, and the shift duz- > žūž-/zūz- is the assimilation of the syllable-initial consonants that Bartholomae expressly names ('Assimilation der silbenanl. Kons.'). Two corrections: the gloss should be 'hedgehog', and the third form 'jujag' is not Middle Persian — no Pahlavi dictionary (MacKenzie, Nyberg) records a jujag, and no Pahlavi word for 'chicken' of that shape exists; it has been imported into this box from the Persian جوجه of node 8, whose source is different (see there).\",\n \"derivation_fa\":\"مکنزی ص ۹۹ می‌آورد «zūzag [zwzkʾ | فارسی نو žūža] خارپشت» و در نمایهٔ انگلیسی‌اش خارپشت را xārpušt، xūkar(ag) و zūzag می‌گزارد؛ بارتولمه نیز گزارشِ پهلویِ وندیداد ۱۸٫۲ را žūžak می‌خواند. پس هر دو صورتِ žūžag و zūzag پهلویِ راستین‌اند و دگرگونیِ duz- به žūž-/zūz- همان همگونیِ همخوان‌های آغازِ هجاست که بارتولمه نامش را برده است. دو اصلاح لازم است: معنی باید «خارپشت» باشد، و صورتِ سومِ jujag پهلوی نیست؛ در هیچ فرهنگِ پهلوی (مکنزی، نیبرگ) چنین واژه‌ای به معنی «جوجه» نیامده و از گرهٔ ۸ به این جعبه راه یافته است.\",\n \"sources\":[A_ZHU],\n \"ref_check\":[\n  {\"ref\":\"SNS:168\",\"status\":\"supports\",\"note\":\"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the reverse index in SNS_pages.txt line 15648 reads 'zūzag 168/10', i.e. the word zūzag is registered for p.168 line 10 of the text — the page Nourai cites. (The glossary article itself is unreadable in this OCR.)\"},\n  {\"ref\":\"BQT:1063\",\"status\":\"partial\",\"note\":\"see node 6: Mo'in's footnote at ≈ p.1066 gives the Pahlavi form as žūžag, but nothing about a Pahlavi 'chicken'.\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie p.99 (PHD.txt line 685) and index p.146\",\"stance\":\"partial\",\"note\":\"'zūzag [zwzkʾ | (N žūža)] hedgehog' — supports žužag/zuzag but glosses 'hedgehog', and the dictionary has no jujag; its word for a bird's young is not of this shape.\"},\n  {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II, glossary\",\"stance\":\"silent\",\"note\":\"grep for zūzag/žūžag/jujag/hedgehog over NYB_vol2_glossary.txt returns nothing — the Shayast/Bundahišn passages Nyberg edits do not include the word.\"}\n ]\n})\n\nnodes.append({\n \"id\":8,\"lang\":\"Persian\",\n \"words\":\"žŭž «ژوژ ( ژوژه )»; jŭjeh «جوجه ( جوژه، چوژه )»\",\n \"verdict\":\"disputed\",\n \"derivation\":\"ژوژ/ژوژه is fine: MP zūzag/žūžag > NP žūža with the regular loss of final -ag, and Mo'in and Dehkhoda both define ژوژه as خارپشت 'hedgehog' (Dehkhoda quotes the Bundahišn passage on the hedgehog as the ant's enemy). جوجه 'chick' is a different word and does not belong under duž-aka. Wiktionary derives it 'probably from Sogdian čwzʾʾk (/čužāk/) ‘chick’', and that Sogdian word is in Gharib's dictionary no. 3308: 'cwzʾʾkk ... cuzak, Yaghn. čujak, Khwar. čwzk, ‘chicken’ (SCE 233; TSP 2332)'. Decisively, Nourai's own citation IEC:1391 says the same thing against him: on that column Mann files 'Per. čūze, s. ‘chick’' (with čuz 'cunnus') under the entry 'teuquio ‘female, girl; vulva’. Cf. WP I, 716', beside Alb. cucë 'girl', Goth. þiwi, OHG diu — i.e. under a quite different IE etymon, and in any case not under *dus-. The variants چوژه/جوژه with initial č- point the same way, since duž-aka could never give č-.\",\n \"derivation_fa\":\"«ژوژ/ژوژه» بی‌ایراد است: از zūzag/žūžag پهلوی با افتادنِ پایانهٔ -ag، و معین و دهخدا هر دو آن را «خارپشت» می‌گزارند. اما «جوجه» واژهٔ دیگری است و جای آن زیرِ duz-aka نیست. ویکی‌واژه آن را «احتمالاً وام‌واژه‌ای از سغدیِ čužāk ‘جوجه’» می‌داند و همین واژه در فرهنگِ سغدیِ بدرالزمان قریب، شمارهٔ ۳۳۰۸، آمده است: «cwzʾʾkk /čuzak/ جوجه، یغنابی čujak، خوارزمی čwzk». از این مهم‌تر، خودِ مأخذی که نورایی آورده (مان، IEC ستون ۱۳۹۱) خلافِ او را می‌گوید: مان «čūze فارسی ‘جوجه’» را ذیلِ مدخلِ teuquio «مادینه، دختر» و در کنارِ cucë آلبانیایی و þiwi گوتی آورده، نه ذیلِ *dus-. صورت‌های «چوژه/جوژه» با چِ آغازین نیز نشان می‌دهند که duž-aka نمی‌تواند خاستگاهِ آن باشد. پس پژوهشِ امروزی این بخش از ادعای نورایی را رد می‌کند.\",\n \"sources\":[W_JUJE,A_JUJE,A_ZHU],\n \"ref_check\":[\n  {\"ref\":\"BRT:755\",\"status\":\"partial\",\"note\":\"Bartholomae's entry duzaka- ends 'mp. (Pü.): žūžak; np. žūža' — it takes the chain only as far as ژوژه and says nothing about جوجه.\"},\n  {\"ref\":\"BQT:1063\",\"status\":\"partial\",\"note\":\"the ژوژه footnote is at ≈ p.1066 (leaf 526) and derives only ژوژه from duzaka; Borhan's جوجه article (leaf 129 region, vol.2) carries no such etymology.\"},\n  {\"ref\":\"HRN:152\",\"status\":\"partial\",\"note\":\"Horn no. 687, p.152: 'žūže ‘Igel’ ... aw. duzaka- ‘Igel’; phlv. žūžak; kurd. LW. arm|jī?, žūžī'. He also cites Gilaki jujik under this word, but as a dialect form of 'hedgehog', not as the standard جوجه ‘chick’.\"},\n  {\"ref\":\"MON:1250,1320\",\"status\":\"not_checked\",\"note\":\"page numbers of the Amir Kabir Farhang-e Farsi cannot be located online; the entries themselves were read on abadis (فرهنگ معین: «ژوژه (ژَ یا ژِ) (اِ.) خارپشت»; «جوجه (جِ) (اِ.) ۱ ـ نوزاد پرندگان ۲ ـ نوزاد مرغ خانگی» — no origin tag).\"},\n  {\"ref\":\"IEC:1391\",\"status\":\"contradicts\",\"note\":\"Mann, IEC col. 1391 (IEC.txt line 18483 ff.): 'teuquio ‘female, girl; vulva’. Cf. WP I, 716 — Per. cf. čuz, s. ‘cunnus’; čūze, s. ‘chick’; Alb. cucé, f. ‘girl; nipple’ ... Go. þiwi, f. ‘girl, maid’ ...'. Nourai's own reference puts Persian čūze/جوجه under a different IE etymon, not under *dus-.\"}\n ],\n \"consulted\":[\n  {\"src\":\"SOD\",\"where\":\"Gharib, Sogdian Dictionary no. 3308 (SOD.txt line 29408)\",\"stance\":\"contradicts\",\"note\":\"'3308 cwzʾʾkk B ... cuzak ©Yaghn. čujak, Khwar. čwzk — chicken. SCE 233; TSP 2332' — the Sogdian source of جوجه.\"},\n  {\"src\":\"MON\",\"where\":\"فرهنگ معین via abadis, s.vv. ژوژه and جوجه\",\"stance\":\"partial\",\"note\":\"«ژوژه ... خارپشت» (hedgehog, not porcupine); «جوجه ... ۱ ـ نوزاد پرندگان ۲ ـ نوزاد مرغ خانگی» with no etymological tag, and Dehkhoda merely equates جوجه with جوژه.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 687, p.152\",\"stance\":\"partial\",\"note\":\"see ref_check — Horn covers ژوژه only.\"}\n ]\n})\n\nnodes.append({\n \"id\":9,\"lang\":\"Avestan\",\n \"words\":\"duš-kareta; duš-cithra, duš-citra; duš-uxta; duš-daěna\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"All four are attested Avestan duš-/duž- compounds and all are formed exactly as the arrow says, the prefix taking the weak grade of the second member. Bartholomae col. 754: 'j. duš.kərət- Adj. ‘übeltuend, Übeltäter’ (Vd. 21.6)', and Jackson's Avesta Grammar gives the neuter duš.kərətəm ‘ill-done’ = Skt. duṣ-kṛtám (p.~50). duž-uxta- 'ill-spoken' is a headword at col. 756 and is glossed by Nyberg (II, p.66) as the source of Pahl. duš-hūxt ‘evil speech’, the second of the three downward stages to hell; duž-varšta- ‘evil deed’ is its counterpart. duš-daēnā- 'of evil religion/conscience' occurs in the same Y.49.11 line that Bartholomae prints under duš-manah-: 'dušxratūš duš.šyaoθanəng dušvacaŋhō dušdaēnəng dušmanaŋhō'. The one nuance: Bartholomae glosses duš-ciθra- as 'des Anblick übel ist, hässlich anzusehen' (ugly to look at) rather than 'of evil seed (race)'; both senses of čiθra- ('appearance' and 'seed, lineage') exist, so Nourai's gloss is a defensible but minority reading of the same word.\",\n \"derivation_fa\":\"هر چهار صورت در اوستا گواه دارند و ساختِ آنها همان است که پیکان نشان می‌دهد. بارتولمه در ستون ۷۵۴ «duš.kərət- ‘بدکردار’» را از وندیداد ۲۱٫۶ می‌آورد و جکسون در دستورِ اوستایی duš.kərətəm را برابرِ duṣ-kṛtám سنسکریت می‌گذارد. duž-uxta- «بدگفته» مدخلی مستقل در ستون ۷۵۶ است و نیبرگ (ج۲ ص ۶۶) آن را نیای پهلویِ duš-hūxt، دومین پلهٔ فرود به دوزخ، می‌داند؛ همتای آن duž-varšta- «بدکرده» است. duš-daēnā- «بددین، بدوجدان» در همان بندِ یسنا ۴۹٫۱۱ آمده که بارتولمه ذیلِ duš-manah- نقل کرده است. تنها نکتهٔ ظریف آنکه بارتولمه duš-ciθra- را «زشت‌رو، بدمنظر» می‌گزارد نه «بدتخمه»؛ چون čiθra- هم «چهره، نمود» و هم «تخمه، نژاد» معنی می‌دهد، خوانشِ نورایی پذیرفتنی اما اقلیت است. در مجموع ادعای این گره درست است.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"AVG:237\",\"status\":\"partial\",\"note\":\"Jackson's Avesta Grammar leaf 293 = printed p.237 opens the section on Noun-Composition (§§859-862: 'Noun-compounds have either a substantival or an adjectival force ... The first member is subject to some modification in form, generally assuming the weak grade'), which is the general rule behind these compounds, but the duš- examples themselves stand elsewhere in the book: p.242 §882 ('With advbl. prefixes (a-, an-, hu-, duš-, arš- etc.), Av. hu-kərəta- ‘well-made’, Av. arš-uxδa- ‘right-spoken’') and p.~50 ('Av. duš.kərətəm ‘ill-done’ = Skt. duṣ-kṛtám') and p.~97 ('Av. duz-vacah- (adj.) ‘evil-speaking’ = Skt. durvacas-').\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"cols. 753-756, 762\",\"stance\":\"supports\",\"note\":\"'j. duš.kərət- Adj. ‘übeltuend, Übeltäter’(?): āat aŋha parō -ta V.21.6'; 'j. duš-ciθra- Adj. ‘des Anblick übel ist, hässlich anzusehen’: drujim yam °rąm Yt.14.95'; the headword duzuxta- at col. 756; and the Y.49.11 string 'dušxratūš duš.šyaoθanəng dušvacaŋhō dušdaēnəng dušmanaŋhō' under duš-manah-.\"},\n  {\"src\":\"NYB\",\"where\":\"Manual of Pahlavi II, glossary pp.66-67\",\"stance\":\"supports\",\"note\":\"'duš-hūxt [dwšhwhtʾ] evil speech ... Av. (756 sq.) duž-ūxta-'; 'duš-huvaršt ... Av. (759 sq.) duž-varšta-'; 'duš-humat ... the negative of humat' — the Pahlavi triad continuing exactly these Avestan compounds.\"},\n  {\"src\":\"AVG\",\"where\":\"Jackson pp.237, 242\",\"stance\":\"partial\",\"note\":\"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\":10,\"lang\":\"Greek\",\n \"words\":\"dus\",\n \"verdict\":\"confirmed\",\n \"derivation\":\"Greek δυσ- 'bad, ill, hard, un-' is the inherited Greek reflex of PIE *dus-, the antonym of εὐ- (< *h₁su-), and it is the branch through which the element entered the western learned vocabulary. Pokorny p.227 lists it in the same breath as the Indo-Iranian forms ('gr. δυσ- ‘miß-, übel’'), Watkins/AHD s.v. dus- says simply 'Greek dus-, bad: DYS-', and Klein s.v. dys- has 'Gk. δυσ-, meaning ‘hard, bad, ill’, cogn. with ... OI. duṣ-, Avestic dush-, duz-'. It was highly productive in ancient Greek (δυσεντερία, δύσπεπτος, δυστυχής).\",\n \"derivation_fa\":\"پیشوندِ یونانیِ δυσ- («بد، ناخوش، دشوار») بازتابِ ارثیِ *dus- هندواروپایی در یونانی و ضدِ εὐ- (از *h₁su-) است، و همین شاخه است که این جزء را به واژگانِ علمیِ اروپایی رسانده. پوکورنی در ص ۲۲۷ آن را در کنارِ صورت‌های هندوایرانی می‌آورد، واتکینز در پیوستِ فرهنگِ امریکن هریتیج می‌نویسد «یونانی dus- ‘بد’: DYS-»، و کلاین ذیلِ dys- آن را هم‌ریشهٔ duṣ- سنسکریت و duš-/duz- اوستایی می‌داند. در یونانیِ باستان بسیار زایا بوده است (δυσεντερία، δυστυχής). ادعای نورایی درست است.\",\n \"sources\":[ETY,W_DUS],\n \"ref_check\":[\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 (AHD_watkins1985.txt line 410): 'dus-. Bad, evil; mis- (used as a prefix). Derivative of deu-¹. Greek dus-, bad: DYS-. [Pok. dus- 227.]' — precisely this arrow.\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein, s.v. dys- (KLN_1966.txt line 12514)\",\"stance\":\"supports\",\"note\":\"'dys-, pejorative [prefix] ... the opposite of the pref. eu-. — Gk. δυσ-, meaning ‘hard, bad, ill’, cogn. with ... OI. duṣ-, Avestic dush-, duz-, ... Goth. tuz-, ... OIr. do-, du-, ‘bad, ill’ ... and perh. also with OL. dvis (whence L. bis), ‘twice’.'\"},\n  {\"src\":\"POK\",\"where\":\"IEW p.227\",\"stance\":\"supports\",\"note\":\"'gr. δυσ- ‘miß-, übel’' listed among the reflexes of dus-.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 p.16 (introduction) and s.v. dus-\",\"stance\":\"supports\",\"note\":\"'There are also the two prefixes su-, ‘good, well-’, and dus-, ‘bad, ill-’, in the Greek forms borrowed as EU- and DYS-.'\"}\n ]\n})\n\nnodes.append({\n \"id\":11,\"lang\":\"Latin\",\n \"words\":\"dys-\",\n \"verdict\":\"plausible\",\n \"derivation\":\"There is no inherited Latin prefix dys-. Latin's own reflex of *dus- is the di- of difficilis (Pokorny p.227: 'lat. in difficilis ‘schwierig’'), and Walde-Hofmann and Ernout-Meillet have no dys- entry at all. What the box is really describing is the learned transmission: classical Latin took over individual Greek compounds whole (dysenteria, dyscrasia, dyspepsia, all first Greek nouns), and from the 16th c. onwards Medical/New Latin used dys- freely as a live prefix — which is how Klein consistently labels the words, e.g. 'dysenteric — L. dysentericus, fr. Gk. δυσεντερικός' but 'dyscrasia — Medical L., formed fr. dys- and κρᾶσις'. So the arrow Greek → Latin is right only for borrowed and Neo-Latin vocabulary, not for an inherited Latin form, and the gloss 'faulty, diseased' belongs to that medical usage.\",\n \"derivation_fa\":\"پیشوندِ dys- در لاتینِ ارثی وجود ندارد. بازتابِ لاتینیِ *dus- همان di- در difficilis است (پوکورنی ص ۲۲۷: «lat. in difficilis ‘دشوار’») و در فرهنگ‌های ریشه‌شناسیِ لاتین (والده-هوفمان، ارنو-مِیه) مدخلی به نامِ dys- نیست. آنچه این جعبه در واقع نشان می‌دهد راهِ وام‌گیریِ عالمانه است: لاتینِ کلاسیک ترکیب‌های یونانی را یکجا وام گرفت (dysenteria، dyspepsia) و از سدهٔ شانزدهم به بعد لاتینِ پزشکی/نوین dys- را همچون پیشوندی زنده به کار برد؛ کلاین همین را با برچسبِ «Medical L.» نشان می‌دهد. پس پیکانِ یونانی ← لاتینی تنها دربارهٔ واژگانِ وام‌گرفته و لاتینِ نوین درست است، نه دربارهٔ صورتی ارثی؛ با این توضیح پذیرفتنی است.\",\n \"sources\":[ETY],\n \"ref_check\":[\n  {\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this box (refs=None in the source JSON).\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. dyscrasia, dysentery, dystrophy\",\"stance\":\"partial\",\"note\":\"'dyscrasia ... — Medical L., formed fr. dys- and κρᾶσις'; 'dysenteric ... — L. dysentericus, fr. Gk. δυσεντερικός'; 'dystrophy, dystrophia ... — Medical L. dystrophia, fr. dys- and Gk. τροφή' — i.e. Medical/New Latin, not classical Latin.\"},\n  {\"src\":\"LEW\",\"where\":\"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\",\"stance\":\"silent\",\"note\":\"grep for 'dys-' and 'dysenteria' returns nothing: the Latin etymological dictionary has no such prefix.\"},\n  {\"src\":\"LAT\",\"where\":\"Ernout-Meillet (LAT.txt)\",\"stance\":\"silent\",\"note\":\"same grep, no hit.\"},\n  {\"src\":\"POK\",\"where\":\"IEW p.227\",\"stance\":\"partial\",\"note\":\"'lat. in difficilis ‘schwierig’' — the genuine Latin reflex is di-, not dys-.\"}\n ]\n})\n\nnodes.append({\n \"id\":12,\"lang\":\"English\",\n \"words\":\"dysfunction, dystrophy\",\n \"verdict\":\"plausible\",\n \"derivation\":\"Only one of the two comes through Latin. dystrophy is from Medical Latin dystrophia, itself dys- + Greek τροφή 'nourishment' (Klein s.v. dystrophy), so the chain Greek → New Latin → English holds. dysfunction, however, is a 20th-century English coinage — Etymonline dates it to 1914, 'dys- + function', originally medical/anatomical — and English has taken dys- directly from Greek as a live prefix ever since the Renaissance rather than through Latin; Etymonline's dys- entry says the prefix 'entered English through Greek, as English adopted Greek word-forming elements'. So the box's words are correctly at the end of the *dus- family, but the intermediate Latin step applies to dystrophy only.\",\n \"derivation_fa\":\"از این دو واژه تنها یکی از راهِ لاتین آمده است: dystrophy از لاتینِ پزشکیِ dystrophia (کلاین: «Medical L. dystrophia از dys- و τροφή یونانی») گرفته شده و زنجیرهٔ یونانی ← لاتینِ نوین ← انگلیسی دربارهٔ آن درست است. اما dysfunction ساختهٔ خودِ انگلیسیِ سدهٔ بیستم است؛ اتیمولوجی‌آنلاین آن را ۱۹۱۴ و «dys- + function» می‌داند، و انگلیسی از دورهٔ رنسانس به این سو پیشوندِ dys- را همچون جزئی زنده مستقیماً از یونانی گرفته است نه از راهِ لاتین. پس هر دو واژه به‌راستی به خانوادهٔ *dus- تعلق دارند، ولی پلهٔ میانیِ لاتین تنها دربارهٔ dystrophy صادق است.\",\n \"sources\":[ETY],\n \"ref_check\":[\n  {\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this box (refs=None in the source JSON).\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. dystrophy\",\"stance\":\"supports\",\"note\":\"'dystrophy, dystrophia, n., defective nutrition (med.) — Medical L. dystrophia, fr. dys- and Gk. τροφή, ‘nourishment’. See trophic and cp. atrophy, hypertrophy.'\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat, Concise Etymological Dictionary\",\"stance\":\"silent\",\"note\":\"grep for 'dys-' returns nothing; Skeat's concise list does not carry the medical prefix.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985, index\",\"stance\":\"supports\",\"note\":\"'DYS- dus-' in the index of English words to roots, and 'DYSENTERY en, DYSLEXIA leg-¹, DYSPEPSIA pekw-, DYSTROPHY' among the compounds — the family assignment is right.\"}\n ]\n})\n\nentry={\n \"entry\":0,\n \"root\":\"Dus\",\n \"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *dus- 'bad, ill, mis-' (an inseparable prefix; antonym *h₁su- 'good, well')\",\n \"note\":\"Pokorny IEW 227 heads the entry 'dus- ‘übel, miß-’ als 1. Kompositionsglied' and lists 'Ai. duṣ-, dur-, av. duš-, duz- ‘miß-, übel’, arm. t- ‘un-’, gr. δυσ- ‘miß-, übel’, lat. in difficilis ‘schwierig’, air. do-, du-, got. tuz-, anord. ags. tor-, ahd. zur-, slav. in abg. dъždь ... ‘Regen’'; Watkins/AHD prints 'dus-. Bad, evil; mis- (used as a prefix). Derivative of deu-¹. Greek dus-, bad: DYS-. [Pok. dus- 227.]'. Language label, gloss and page reference are all correct; the only refinement is that *dus- is a bound first-compound-member, never a free adjective, so the two branches of this chart (Iranian and Greek) are branches of a prefix, not of a word. Both Pokorny and Watkins derive it from *deu-/*deus- 'to lack, be wanting'; Wiktionary records de Vaan's alternative from *dwóh₁ 'two' ('into two' > 'apart' > 'bad'), so the internal etymology is open, but the prefix itself is not in doubt. Within the chart the Iranian side is largely sound; the weak spots are the compounds Nourai reconstructs himself (nodes 1 duš-vāre, 3 duš-haēm / duš-yāta / duš-piθwa) and the attachment of جوجه to the hedgehog word (node 8), where his own source, Mann IEC:1391, says otherwise.\",\n \"note_fa\":\"جعبهٔ ریشه همان *dus- هندواروپاییِ آغازین است: پیشوندی به معنی «بد، ناخوش» و ضدِ *h₁su-. پوکورنی در صفحهٔ ۲۲۷ مدخل را چنین می‌آغازد: «dus- ‘بد، ناخوش’ همچون جزءِ نخستِ ترکیب» و duṣ-/dur- سنسکریت، duš-/duz- اوستایی، t- ارمنی، δυσ- یونانی، di- در difficilis لاتین، do-/du- ایرلندی کهن، tuz- گوتی و zur- آلمانیِ علیای کهن را برمی‌شمارد؛ واتکینز نیز در پیوستِ فرهنگِ امریکن هریتیج همین را با ارجاع به «Pok. dus- 227» می‌آورد. پس نام، برچسبِ زبان، معنا و شمارهٔ صفحه همه درست است. تنها نکته آن است که *dus- واژهٔ آزاد نبوده بلکه پیشوند است. دربارهٔ خاستگاهِ درونیِ آن، پوکورنی و واتکینز آن را از *deu-/*deus- «کم داشتن» می‌گیرند و ویکی‌واژه گمانِ دِ ڤان را (از *dwóh₁ «دو») نیز یاد می‌کند. در خودِ نمودار، شاخهٔ ایرانی بیشتر درست است و سستی‌ها در ترکیب‌هایی است که نویسنده خود بازسازی کرده (گره‌های ۱ و ۳) و در پیوند دادنِ «جوجه» به «ژوژه» در گرهٔ ۸ که مأخذِ خودِ او (مان، ستون ۱۳۹۱) آن را نمی‌پذیرد.\",\n \"sources\":[W_DUS,ETY],\n \"ref_check\":[\n  {\"ref\":\"POK:227\",\"status\":\"supports\",\"note\":\"POK_01.txt lines 3253-3256 (the page number 227 stands at line 3248): 'dus- ‘übel, miß-’ als 1. Kompositionsglied. Ai. duṣ-, dur-, av. duš-, duz- ‘miß-, übel’ ... gr. δυσ- ‘miß-, übel’, lat. in difficilis ‘schwierig’ ... Zusammenhang mit deus- ‘ermangeln’ ist sehr wahrscheinlich. WP. I 816.'\"}\n ],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny Bd. I 816 (WLD_Bd1 djvu line 51476)\",\"stance\":\"supports\",\"note\":\"'dus- ‘übel, miß-’ als 1. Zsglied. Ai. duṣ-, dur-, av. duš-, duz- ‘miß-, übel’ ... gr. δυσ- ... Zusammenhang mit deus- ‘ermangeln’ ist sehr wahrscheinlich, dagegen solcher mit *duou ‘zwei’ als ‘entzwei’ ... kaum zuzugeben.' — note that Walde-Pokorny expressly rejects the *dwo- etymology that de Vaan later revived.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985, s.v. dus- (line 410) and p.16\",\"stance\":\"supports\",\"note\":\"'dus-. Bad, evil; mis- (used as a prefix). Derivative of deu-¹. Greek dus-, bad: DYS-. [Pok. dus- 227.]'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein s.v. dys-\",\"stance\":\"supports\",\"note\":\"the same cognate set (Gk. δυσ-, OI duṣ-, Avestic duš-/duz-, Arm. t-, Goth. tuz-, ON tor-, OIr. do-).\"}\n ],\n \"nodes\":nodes\n}\n\nout={\"pdf_page\":143,\"book_page\":113,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-05\",\"entries\":[entry]}\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-143.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk143.py",
 "description": "Generate page-143.json"
}
```


### [2026-09-05T20:30:13.017Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:30:19.943Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-143.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 143",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:30:22.063Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'disputed': 3, 'plausible': 6, 'confirmed': 3}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 8, 'partial': 11, 'not_checked': 6, 'contradicts': 1}
books consulted: {'partial': 9, 'supports': 19, 'contradicts': 3, 'silent': 4} | by book: {'PHD': 5, 'NYB': 4, 'BRT': 3, 'HRN': 3, 'BQT': 3, 'KLN': 3, 'HUB': 2, 'POK': 2, 'AHD': 2, 'KNT': 1, 'FSF': 1, 'SOD': 1, 'MON': 1, 'AVG': 1, 'LEW': 1, 'LAT': 1, 'SKT': 1}
```


## [2026-09-05T20:30:44.162Z] AGENT

Page 143 (book p.113) verified — `data/verification/page-143.json`, `verify_check.py 143` shows 0 PROBLEM lines (12/12 nodes).

**Counts** — root: 1 confirmed. Nodes: 3 confirmed, 6 plausible, 3 disputed. Ref checks: 8 supports, 11 partial, 1 contradicts, 6 not_checked. Books consulted: 19 supports, 9 partial, 3 contradicts, 4 silent.

**Disputed**
- Dus, #1 `duš-vâre` "difficult to carry" (←Bher): no *duš-vāra- in Bartholomae; Hübschmann p.206 derives both dušvār and dušxvār from Av. duž-āθra-/duš-xᵛāθra- — دشوار is just دشخوار reduced, not from bar- "carry". Rest of node 1 confirmed.
- Dus, #3 `duš-haem`, `duš-yâta`, `duš-pithwa`: unattested; Av. yāta- = "allotted share", piθwā- = "solid food" (پیه is from pivah-), and خیم/یاد go back to MP xēm / ayād. Only daoš-ahva/duž-aŋhu- "bad existence" (BRT col. 755) is real — that one is confirmed.
- Dus, #8 `jŭjeh` جوجه: from Sogdian čužāk "chick" (Gharib no. 3308; Wiktionary). Nourai's own citation IEC:1391 files Persian čūze under Mann's *teuquio "female, girl", not under *dus-. ژوژ/ژوژه itself is fine.

**Other notable findings (not flagged)**
- #6/#7/#8: the animal is the hedgehog (خارپشت), not the porcupine, per Bartholomae ("Igel"), MacKenzie ("zūzag … hedgehog"), Mo'in and Dehkhoda; and Pahlavi "jujag" is in no Pahlavi dictionary. Bartholomae's own "Et.?" matches the chart's honest NOTE.
- #5: only دوزخ descends from Pahlavi dužax; دژخیم، دشیاد، دژپیه are duš-compounds hanging one level too low. دُمَل is Arabic (root د-م-ل), supporting Nourai's own "see Dumb" note.
- #11/#12: no inherited Latin dys- (Latin reflex is di- in difficilis; LEW and Ernout-Meillet silent). Klein labels the words "Medical L."; dystrophy goes via New Latin dystrophia, but dysfunction is a 1914 English coinage straight from Greek.
- Cited-page drift in Nourai's Borhan references: دزد is at p.851 (he cites 850), دوزخ at p.897 (he cites 896), ژوژه at ≈p.1066 (he cites 1063).

**Extraction errors:** none — the JSON matches the chart text faithfully; no `transcription_suspect` nodes, so no page image was needed.
