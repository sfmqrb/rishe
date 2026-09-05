# Verification process log — verify-page-94


## [2026-09-05T14:06:22.023Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 94 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-94.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-94.json. Write /home/sfmqrb/git/rishe/data/verification/page-94.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 94` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:06:23.368Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:06:24.107Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:06:24.122Z] TOOL RESULT

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


## [2026-09-05T14:06:24.647Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-94.txt"
}
```


### [2026-09-05T14:06:24.662Z] TOOL RESULT

```
1	=== PDF page 94 (book page 64) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bheu 3 : to exist, grow  (refs POK:146)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:146; BQT:111 | bŭta, bav : to exist, become ; bŭšyant, bŭšyeity : will exist
5	  #2 (parent #1) [Persian] refs=POK:147; BQT:111,314; MON:603; AEF:293 | bŭdan «بودن» : to be ; bâšîdan «باشیدن» : to be ; bovesh «بُوَش» : being, existence | extra: باد۲ ، بادا ، بو۲؛ باشنده ، باش ، باشد
6	#3 (parent #0) [Avestan / Old Persian] refs=POK:146; BQT:111; KNT:200 | bŭmî : earth ; bŭmî-mathan : earthquake ; urvarâ : plant
7	  #4 (parent #3) [Pahlavi] refs=AEF:298 | bŭm 2 : earth ; bŭmahan : earthquake ; urvar : plants
8	    #5 (parent #4) [Persian] refs=POK:147; BQT:320; MON:401; AEF:299 | bŭm 2 «بوم ۲» : earth, country ; bŭmmahan «بومَهَن» : earthquake ; ŭrvar «اورْوَر» : plant | extra: بومهین
9	  #6 (parent #3) [Sogdian] refs=SOD:115 | bwmb : earth, world
10	#7 (parent #0) [Avestan] refs=BQT:223; SYN:1503; POK:146 | bŭiti, buiti daevo : name of a demon encouraging idolatry | NOTE: BQT:233 claims Avestan name "buiti" is cognate with the Sanskrit word "bhŭta: a being, phantom, ghost" from the Indo-European root "Bheu".
11	  #8 (parent #7) [Avestan] refs=BQT:234 | bŭiti-kata : idol house ☞Ket
12	    #9 (parent #8) [Persian] refs=MON:472; BQT:234 | bot «بت» : idol | extra: بتکده ، بتخانه ، بت پرست | NOTE: See "Pwt" for another possible root.
13	      #10 (parent #9) [Hindustani] refs=None | 
14	        #11 (parent #10) [Portuguese] refs=None | 
15	          #12 (parent #11) [English] refs=SKT:366; LKT:30; AID:233 | pagoda : prayer house | NOTE: See HJB:652 for a discussion on this word.
16	#13 (parent #0) [Sanskrit] refs=SYN:1503; POK:146 | bhu : become be ; bhŭta : a being, ghost, phantom
17	#14 (parent #0) [Germanic] refs=None | 
18	  #15 (parent #14) [English] refs=AHD; POK:149 | be, build, beam, booth, boom, husband, neighbor, arbor, herb, bower
19	#16 (parent #0) [Greek] refs=AHD | phuein : to make grow
20	  #17 (parent #16) [English] refs=None | physics
21	#18 (parent #0) [Latin] refs=AHD | futurus : that is to be ; pro-bhwo : growing forward ; super-bhwo : being above ; tri-bhu : third being, the third, a section of the Roman empire
22	  #19 (parent #18) [English] refs=AHD | future ; prove ; superb ; tribe, tribune, contribute
23	
```


## [2026-09-05T14:06:28.871Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-94.json",
 "description": "Read source JSON for page 94"
}
```


### [2026-09-05T14:06:28.952Z] TOOL RESULT

```
{
  "pdf_page": 94,
  "book_page": 64,
  "entries": [
    {
      "root": {
        "name": "Bheu 3",
        "lang": "Indo-European",
        "refs": "POK:146",
        "gloss": "to exist, grow"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:146; BQT:111",
          "words": [
            {"translit": "bŭta, bav", "gloss": "to exist, become", "script": null},
            {"translit": "bŭšyant, bŭšyeity", "gloss": "will exist", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:147; BQT:111,314; MON:603; AEF:293",
          "words": [
            {"translit": "bŭdan", "gloss": "to be", "script": "بودن"},
            {"translit": "bâšîdan", "gloss": "to be", "script": "باشیدن"},
            {"translit": "bovesh", "gloss": "being, existence", "script": "بُوَش"}
          ],
          "script_extra": "باد۲ ، بادا ، بو۲؛ باشنده ، باش ، باشد",
          "note": null,
          "quote": {
            "text": "چو یزدان چنین راند اندر بوش - برآن بود چرخ روان را روش",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:146; BQT:111; KNT:200",
          "words": [
            {"translit": "bŭmî", "gloss": "earth", "script": null},
            {"translit": "bŭmî-mathan", "gloss": "earthquake", "script": null},
            {"translit": "urvarâ", "gloss": "plant", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "AEF:298",
          "words": [
            {"translit": "bŭm 2", "gloss": "earth", "script": null},
            {"translit": "bŭmahan", "gloss": "earthquake", "script": null},
            {"translit": "urvar", "gloss": "plants", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:147; BQT:320; MON:401; AEF:299",
          "words": [
            {"translit": "bŭm 2", "gloss": "earth, country", "script": "بوم ۲"},
            {"translit": "bŭmmahan", "gloss": "earthquake", "script": "بومَهَن"},
            {"translit": "ŭrvar", "gloss": "plant", "script": "اورْوَر"}
          ],
          "script_extra": "بومهین",
          "note": null,
          "quote": {
            "text": "برآمد یکی بومهن نیمشب - تو گفتی زمین دارد از لرزه تب",
            "poet": "Garshâsp"
          }
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Sogdian",
          "refs": "SOD:115",
          "words": [
            {"translit": "bwmb", "gloss": "earth, world", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:223; SYN:1503; POK:146",
          "words": [
            {"translit": "bŭiti, buiti daevo", "gloss": "name of a demon encouraging idolatry", "script": null}
          ],
          "script_extra": null,
          "note": "BQT:233 claims Avestan name \"buiti\" is cognate with the Sanskrit word \"bhŭta: a being, phantom, ghost\" from the Indo-European root \"Bheu\".",
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Avestan",
          "refs": "BQT:234",
          "words": [
            {"translit": "bŭiti-kata", "gloss": "idol house", "script": null, "see": ["Ket"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:472; BQT:234",
          "words": [
            {"translit": "bot", "gloss": "idol", "script": "بت"}
          ],
          "script_extra": "بتکده ، بتخانه ، بت پرست",
          "note": "See \"Pwt\" for another possible root.",
          "quote": {
            "text": "در دل ندهم ره پس از این مهر بتان را - مُهرِ لب او بر در این خانه نهادیم",
            "poet": "Hâfez"
          }
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Portuguese",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "SKT:366; LKT:30; AID:233",
          "words": [
            {"translit": "pagoda", "gloss": "prayer house", "script": null}
          ],
          "script_extra": null,
          "note": "See HJB:652 for a discussion on this word.",
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SYN:1503; POK:146",
          "words": [
            {"translit": "bhu", "gloss": "become be", "script": null},
            {"translit": "bhŭta", "gloss": "a being, ghost, phantom", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD; POK:149",
          "words": [
            {"translit": "be, build, beam, booth, boom, husband, neighbor, arbor, herb, bower", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "phuein", "gloss": "to make grow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "physics", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "futurus", "gloss": "that is to be", "script": null},
            {"translit": "pro-bhwo", "gloss": "growing forward", "script": null},
            {"translit": "super-bhwo", "gloss": "being above", "script": null},
            {"translit": "tri-bhu", "gloss": "third being, the third, a section of the Roman empire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "future", "gloss": null, "script": null},
            {"translit": "prove", "gloss": null, "script": null},
            {"translit": "superb", "gloss": null, "script": null},
            {"translit": "tribe, tribune, contribute", "gloss": null, "script": null}
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


## [2026-09-05T14:06:29.392Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and read source matrix"
}
```


### [2026-09-05T14:06:29.469Z] TOOL RESULT

```
agent
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
---
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


## [2026-09-05T14:06:37.091Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','KNT','SOD','SYN','AEF','SKT','LKT','AID','HJB','AHD','BRT','PHD','NYB','HRN','HUB','CHEUNG','WLD','IEC','KLN']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-05T14:06:37.909Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-93.json 2>/dev/null || ls data/verification | tail -30",
 "description": "Check a nearby verification file"
}
```


### [2026-09-05T14:06:39.252Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فر
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in bold at line start; grep -n '^Word'.", "notes": ""}
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online a
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== CHEUNG null
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
```


### [2026-09-05T14:06:39.287Z] TOOL RESULT

```
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
page-90.json
page-91.json
process
sources
```


## [2026-09-05T14:06:45.312Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK leaf for p146 (POK_01 leaf=p+8 => 154) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==155' POK_01.txt | head -80",
 "description": "Print Pokorny p.146 area"
}
```


## [2026-09-05T14:06:46.067Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bheu-\" POK_full.txt | head -20; echo ---; grep -n \"^bheu\" POK_full.txt | head",
 "description": "Grep POK_full for bheu"
}
```


### [2026-09-05T14:06:46.873Z] TOOL RESULT

```
=== POK leaf for p146 (POK_01 leaf=p+8 => 154) ===
  ags.  brunna^  burna  , Brunnen' (aisl.  brunn)y  mit  Metathese  nhd.  (ndd.)  Born.
Mit  ähnlicher  Bed.  russ.  brujd  ,Strömung',  bruith  ,stark  reißend  strömen, ■dahinfließen',  wruss.  brüjic  ,harnen'  (diese  Bed.  auch  in  mhd.  brunnen  und in  nhd.  dial.  brunzen,  bair.  brunnlen  ,harnen'  von  Brunnen),  formal  näch- stens zu  lit.  br{i)dujs,  br{i)dutis  ,sich  mit  roher  Gewalt  vordrängen'  (*bhreu-), lett.  brauligs  ,geil';  auch  apr.  breicingi  , forderlich'?
bhre-n-U'  (Präsens  mit  Nasalinfix,  vgl.  nhd.  brennen)  mit  Beziehung -auf  züngelnde  Flammen  liegt  vor  in  got.  ahd.  as.  bi-innan,  ais.  brinna, .ags.    beornan,    birnan   ,brennen',    Kaus.   got.    brannjan,   aisl.   brenna,  ahd.
145
Iretinan,  ags.  haernan  ^brennen^,  wozu  u.  a.  ahd.  hrant  ,Brand^,  brunst Brennen^  Brand^,  aisl.  hruni,  ags.  hryne  ^Brand'^  ahd.  hronadoj  ags.  hrunapa Jucken;  Hitze  am  Körper^,  schwed.  bränad  ^Brunst'^;
hhreu-  :  bhruu-  in:  ahd.  hriuwan,  ags.  breowan  ,brauen^,  aschwed. bryggja  (aus  *bryggwa)  ds.;  germ.  *bruda-  in:  aisl.  ags.  brod^  ahd.  prod BrUhe^  {:  defrütum,  air.  bruthy  thrak.  ßQvrog:  mhd.  brodelen,  nhd.  brodeln)-, trerm.  *brauda-  in:  aisl.  braud,  ags.  bread,  ahd.  6rö^  ,Brot^  (von  dem Gärstoff);  über  ahd.  tüm^es  pril^  ^Windsbraut^  s.  Kluge ^^  692.
WP.  II  167  f.,  WH.  I  333  f.,  487.  •        .
bhergh'  ^bergen^  verwahrend
Got.  bairgan  ^bergen,  verwahren^;  aisl.  bjarga^  ags.  beorgan,  ahd.  bergan j as.  gi-bergan  ^bergen*^;  ablautend  ags.  byrgan  ^begraben^,  byrgen  i^burgizno), byrgels,  as.  burgisli  ^Begräbnis^  und  ahd.  bor(a)gen  ^sich  wovor  hüten,  sich wovor  in  Sicherheit  bringen,  acht  worauf  haben,  schonen,  anvertrauen, borgen^,  ags.  borgian  ,behüten,  borgend  Slav.  *bergg  in  aksl.  bregq,  brästi '  ^sorgen^  in  nebrästi  ,vernachlässigen^,  russ.  beregü,  berech  ,hüten,  bewahren, •  schonen,  sparen^,  skr.  älter  brzem,  brijeci  , bewachen,  bewahren,  sorgen; feiern^;  ablautend  klr.  oborih,  gen.  oboröha  ,Heuschober^,  öech.  brah  ,Heu- schober,  Haufen'^,  poln.  brög  ,Scheune,  Schober^  (daraus  lit.  brägas  ds.); schwundstufig  öech.  brh  ,Höhle,  Hütte,  Zelt^;  ostlit.  birginti  ,sparen^
Vielleicht    hierher    gallo-rom.    (rhät.-ill.)    bargä    ,gedeckte    Strohhütte^, falls  aus  Horgä]  Tagliavini  ZrP.  46,  48 f.,  Bonfante  BSL.  36,  141  f. WP.  II  172,  Trautmann  31,  Feist  76.     Vgl.  oben  S.  141.
bheTug",  hhrug-f  hhorg-  ,Schlund,  Luftröhre^
Arm.  erbuc  ,Brust,  Bruststück  von  geschlachteten  Tieren^  (*bhrugo-) gr.  g)dQv^j  -vyogj  später  (nach  Xdqvy^)  cpägvy^,  -uyyog  ,Luftröhre,  Schlund^ lat.  frümen  n.  ,Kehlkopf,  Schlund^  (*fräg-smen)]  ohne  u  aisl.  barki  ,Hals {bhor-g-j  formell  näher  zu  cpdgay^  ,Kluft,
```


### [2026-09-05T14:06:46.930Z] TOOL RESULT

```
---
```


## [2026-09-05T14:06:51.489Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la POK_full.txt; head -c 500 POK_full.txt; echo; echo \"=== grep bheu in POK_01 ===\"; grep -n \"bheu\" POK_01.txt | head -30",
 "description": "Check POK_full and grep bheu"
}
```


### [2026-09-05T14:06:51.554Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Ce
=== grep bheu in POK_01 ===
1449:Slav.  Huza-  :  H^z^-  .Holunder^  in  russ.  buz  m.  :  slov.  bez,  russ.  dial.  Jo^ bleiben  wohl  fern;  ebenso  kurd.  büz  ,eine  Art  Ulme^  das  auf  älteres  vik (aus  idg.  *uigös)  zurückgeht.  Mhd.  büche^  biuche  ^Lauge^  biuchen,  buchen ,m  Lauge  kochen  oder  waschen'  gehört  eher  zur  Wz.  bheug{h)-  .reinigen,
1580:ju  nc  II  (y^-\.  air.  maq  ,YqW,  Dat.  muig  <  *mages),  so  daß  es  nicht  nötig  ist, *bheug(h)-  ,biegen^  anzuknüpfen;  mcymr.  di-vwng  ^unbeugsam';  zur  ße- A  tuno"  besieo-en^  vgl.  air.  maidid  for  nech  ,es  bricht  über  einen  herein^  = wird  besiegt^  Auf  o  weist  auch  mir.  hoimm  ^Bissen^  aus  ^bhog-smn- '  lit  bangä  ^Welle,  Menge,  Platzregen^,  prabangä  ,Übermaß^,  lett.  buogs dichte  Menge^,  dazu  lit.  bangüs  ,rasch,  heftig^  (von  Bächen  und  Regen- !rUssen),  blngüs  ,mutig^  (von  Pferden),  bengiit,  bengiaü,  befigti  ,beenden^, ^abangä  f.  ,Beendigung^;  pr.  pobanginnons  ,bewegt^;  in  der  Bed.  ,beendi- eeii^  entstehen  durch  Ablautentgleisung  Formen  mit  ei,  ai  (vgl.  Endzelin Lett.  Gr.  60)  in  lett.  beigas  PI.  ,Ende,  Neige^,  lit.  pabaigä  ds.,  beigiü  und iQiqiit  ,ende^,  lett.  beidzu  ds. ;  da  lett.  buoga  auch  ,steiniger  Platz^  be- deutet, gehört  wohl  auch  russ.  büga  ,überschwemmtes  Waldgebiet^  hierher; anders  über  heig-  (zu  bhei-  ,schlagen^)  Kuiper  Nasalpräs.  184.
2073:bheu-,  bheuQ'  (bbuä-,  bhue-)  :  bhou-  :  bhü-:  ursprünglich  ,wachsen,  gedei- hen' (wohl  =  , schwellen'),  vgl.  ai.  prdbhüta-h  mit  ai.  bhäri-h  usw. unter  *b(e)u-,  bh(e)u-  , aufblasen,  schwellen',  woraus  , entstehen,  werden, sein',  weiters  , gewohnheitsmäßig  wo  sein,  wohnen';  io/i- Präsens bhu-iiö,  bhu-iie-sif  bhu-i-si  usw.  als  Verbum  ,sein'  suppliert  oft das  Paradigma  von  es-  ,sein';  erweiterte  Wz.  bheui-^  bhuei-]
2086:Arm.  bois^  Gen.  biisoy  , Schößling,  Kraut,  Pflanze',  busanim  , sprieße  auf^, ferner  vielleicht  boin,  Gen.  bunoi  ',Nest'  (*bheu-nO'),  schwundstufig  bun. Gen.  bnoi  , Stamm'.
2102:air.  buiih  ,sein'  (ursprgl.  Dat.  des  ä-St.  both  <  Hhuta  ==  cymr.  bod, corn.  bos,  bret.  bout  =  air.  both  f.  ,Hütte',  cymr.  bod  f.  , Wohnung'  :  lit. bütas  ,Haus';  hierzu  auch  mir.  for-baid  ,Grabtuch,  Bahre'),  Fut.  -bla ,wird  sein'  (=  lat.  fiat),  Prät.  1.  Sg.  bä  {*bhuäm),  3.  Sg.  bol  (*bhöue), Pass.  Prät.  -both  ,man  war'  {Hhu-to-) ;  das  Paradigma  des  Verbum  Subst. und  der  Kopula  besteht  aus  Formen  von  es-  und  bheu-,  z.  B.  hat  die 1.  Sg.  Präs.  Konj.  air.  beu  (*bh-esö)  den  Anlaut  von  bheu-  bezogen;
2127:Specht  will  (KZ.  59,  58  f.)  unter  Heranziehung  von  gr.  (paJ^og  , Licht, Heil'  =  ai.  bhava-  , Segen,  Heil',  cpaa-al-ußQOTog  usw.  unsere  Wz.  als *bhaud-^  nicht  als  *bheud-  ansetzen.    S.  auch  oben  S.  91.
2128:bheudh-,    nasal,    bhu-n-dh-    ,wach    sein,    wecken,    beobachten;    geweckt, geistig   rege,   aufmerksam   sein,  erkennen,   oder  andere   dazu    veran- lassen (aufpassen  machen,  kundtun,  gebieten;  darbieten)'. Themat.  Präs.  in  ai.  bödhati,  bödhate  , erwacht,  erweckt,  ist  wach,  merkt, wird    gewahr',    av.    baodaiti    ,nimmt   wahr',    mit  paiti-  ,sein   Augenmerk worauf  richten'  (=  gr.  7tsvd^o(.iaij  germ.  *biudan,    abg.    bljudg);    Aor.    ai. bhuddnta  (=  invd-ovTo),  Perf.  bubödlia,  bubndhimd  (:  germ.  *baud,  *budurn), Partiz.  buddhd-  , er  wacht,  verständig;  erkannt'  (=  gr.  ä-nvarog  ,unkundig; unbekannt'),    buddhi-    f.    , Einsicht,  Verstand,    Meinung,    Absicht'    (=  av. paiti-busti-    f.    ,das    Bemerken',    gr.  nvotig    ,das    Nachforschen,    Fragen; Kunde,  Nachricht');  Kausativ  in  ai.  5öc^M7/a<i  , er  weckt;  belehrt,  teilt  mit', av.    baodayeiti   ,bemerkt,    fühlt'  (=  abg.    buzdg,    buditi,   lit.  pasibaudyti)] Zustandsverb  in  ai.  budhydte  ,erwacht,  wird  gewahr;  erkennt',  av.  buiöyeiti
2147:1.  bheug-  ,fliehen',  nach  Kretschmer  (Gl.  30,  138)  zu  2.  hheug(hy  (av.  baol
2155:Av.  baog-,  bunja-  ,lösen,  retten,  sich  retten  vor'  {bunjainti  ,sie  befreien! retten',  büjayamnö  ,ablegend',  bunjayät  ,er  rette'),  büjim  Akk.  ,Reinigung'j qzö-buj-  ,aus  Not  befreiend',  baoxtar-  ,Befreier';  pehl.  paz.  böxtan  ,retteii, erlösen',  südbal.  böjag  ,öffnen,  lösen,  losbinden',  als  pers.  Lw.  arm.  huzem ,heile,  rette,  befreie',  boi^  , Heilung,  Befreiung';  päli  paribhuüjati  ,reinigT, kehrt  aus';  aber  päli  bhujissa-  ,freigelassen  (von  früheren  Sklaven)'  = ai.  bhujisyä-  ,frei,  unabhängig'  (Lex.,  in  der  Lit.  als  ,nutzbar',  Subst. ,Diener(in)'),  zu  4.  bheug-.
2158:Die  Doppelheit  germ.  gh  :  ar.  g-  auch  bei  bheugh-  (nhd.  biegen) :  bheug-  (ai. bhujati  usw.)  ,biegen'.     Wohl  identisch  damit.
2160:3.  bheug-,  hheugh-  ,biegen'.
3406:av.  dab'  ,betrügen,   um   etwas   bringen' :  davqi-d-yä  G.  Sg.  f.  ,der  betrl genden',  davayeinü  N.  Sg.  f.  ,die  betrügende',   ddbdnaotä  2.  PI.  Präs.  (a *dbha7icm-mi,  idg.  *dbh-en-eumi'),  Inf.  diwiaidyäi  (ohne   desiderative  B( mehr,   aber  =  ai.   dipsa-ti),  Partiz.  Perf.  Pass.  dapta-  (Neuerung);  d^l vayat  ,er   soll   betören'   (Wzf.  *dbheu-)j   a-ddbaoman-  n.  ,Betürung';  oss3 dawin  , stehlen';   hitt.  te-ip-nu-  , gering  achten',  Pedersen  Hitt.  144.
5109:es-  jSein*,  Kopula  und  Verbum  Substantivum ;  bildet  ursprünglich  nur  ein duratives  Präsens  wird  daher  einzelsprachlich  vielfach  durch  die Wurzel  bheud- :  bhü-  suppliert.
```


## [2026-09-05T14:06:56.968Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=2073 && NR<=2130' POK_01.txt | head -70\necho \"=== leaf number of line 2073 ===\"\nawk 'NR<=2073{n+=gsub(/\\f/,\"\")} END{print n}' POK_01.txt",
 "description": "Print Pokorny bheu- entry"
}
```


### [2026-09-05T14:06:58.726Z] TOOL RESULT

```
bheu-,  bheuQ'  (bbuä-,  bhue-)  :  bhou-  :  bhü-:  ursprünglich  ,wachsen,  gedei- hen' (wohl  =  , schwellen'),  vgl.  ai.  prdbhüta-h  mit  ai.  bhäri-h  usw. unter  *b(e)u-,  bh(e)u-  , aufblasen,  schwellen',  woraus  , entstehen,  werden, sein',  weiters  , gewohnheitsmäßig  wo  sein,  wohnen';  io/i- Präsens bhu-iiö,  bhu-iie-sif  bhu-i-si  usw.  als  Verbum  ,sein'  suppliert  oft das  Paradigma  von  es-  ,sein';  erweiterte  Wz.  bheui-^  bhuei-]
zahlreiche  Nominalbildungen  mit  den  Bed.  ,das  Sein,  Wesen,  Wohnen, Wohnsitz',  wiQ  bbato-,  bhatä,  bhati-,  bhutio-,  bhümen-,  bhülo-, bhüro'  usw.
Ai.  bhdvati  ,ist,  ist  da,  geschieht,  gedeiht,  wird'  =  av.  bavaiti  ,wird, entsteht;  geschieht;  wird  sein',  apers.  bavatiy  ,wird';  Fut.  ai.  bhaviSydtif av.  büsyeiti  Partiz.  büsyant-  ,der  ins  Dasein  treten  wird'  (letztere  =  lit. busiuj  ksl.  bys^Heje  ,to  (.lillov^,  vgl.  gr.  q)i(j(o)]  Aor.  ai.  dbhüt  (==  gv.  ecp^)- und  bJiüvat,  Perf.  .  babhuva,  Partiz.  Perf.  Akt.  babhüvän,  f.  babhüvusl (:  gr.  7t6q)V(bg,  Ttecpvvla,  lit.  büvo,3iks\.  byvati),  Inf.  bhdvitum,  Absol.  bhütvä (vgl.  lit.  büty,  Supinum  ,zu  sein',  apr.  büton  Inf.);
a.i.  bhütd-h,  av.  büta-  ,ge worden,  seiend,  ai.  bhütd-m  ^Wesen^  (:  lit.  büta jgewesen',   aisl.    büd  f.  , Wohnung',   russ.  byU  , Wesen,    Lebensart';    mit  ö
-«^'1 ^w
147
<rr.  wvtdv,  air.  -hoth  ,man  war^,  both  L  ,Hütte^,  lit.  bütas  ,Ha.us')  ]  prd- ^}ifUa-h  yVeichWch,  zahlreich*,  npers.  Int.  büdaii  ,sein';
ai.  blititi-h,  bhüti-h  f.  ,Sein,  Wohlsein,  guter  Zustand,  Gedeihen^  (av. bäti-  m.  ,Name  eines  daeva'7  =  aksl.  za-,  'po-^  pre-byth,  russ.  byth,  Inf. aksl.  bytl,  lit.  öw^i;  mit  ü  gr.  cpvGig).
Pass.  ai.  bhüyate]  kaus.  bhävayati  ,bnngt  ins  Dasein;  hegt  und  pflegt, erfrischt^,  Partiz.  bhävita-h  auch  , angenehm  erregt,  gut  gestimmt^  (==  aksl. iz-baviti  , befreien,  erlösen^),  mit  ders.  Dehnstufe  bhävd-h  ,Sein,  Werden, Zuneigung^  ( -  russ.  za-bdva  f.  , Unterhaltung^)  neben  bhavd-h  , Entstehung, AVohlfahrt,  Heil';
bhavitram  ,Welt'  (ablaut.  mit  gr.  cpvrla  ,Natur,  Geschlecht'  und  lit. bühlä  , WohnungV  usw.,  und  mit  germ.  *bupla-  und  *böpla-,  woneben  mit Formans  -dhlo-  cech.  bydlo)\  bhavana-m  ,das  Werden;  Wohnstätte,  Haus (:alb.  bane,  aber  mir.  büan  , standhaft'  aus  *bkou-7io-),  ablaut.  bhüvana-m ,Wesen';
ai.  bhü-  f.  ,Erde,  Welt',  bhümlj  hJiumih-j  av.  ap.  bümi-j  npers.  büm  ,Erde', ai.  bhuman-  n.  ,Erde,  Welt,  Sein'  (=  gr.  cpv^a),  bhümdn-  m.  ,Fülle,  Menge, Reichtum';  fra-bhü-li  ,mächtig,  hervorragend';
5-St.  bhavis-nu-h  , werdend,  gedeihend',  bhüsati  , macht  gedeihen,  stärkt', hhüsayati  , schmückt',  bhüsana-m  , Amulett,  Schmuck'.
Die  I-Basis  *bl2(e)ui-,  wie  es  scheint^  im  ai.  böbhavlti  Intens,  und  bhdvt- -tva-k  , zukünftig*;  über  iran.  6i-Formen  s.  unten.
Arm.  bois^  Gen.  biisoy  , Schößling,  Kraut,  Pflanze',  busanim  , sprieße  auf^, ferner  vielleicht  boin,  Gen.  bunoi  ',Nest'  (*bheu-nO'),  schwundstufig  bun. Gen.  bnoi  , Stamm'.
Thrak.  ON  Kaol-ßovvov.
Gr.  (pvo)  (lesb.  (pvlo)  wie  osk.  fuia^  s.  unten),  , zeuge'  (Aor.  eq)V(7a), (pvo^ai  ,werde,  wachse'  (vgl.  Schwyzer  Gr.  Gr.  I,  686),  wohl  Neubildungen zum  Aor.  eq)vv  , wurde',  daneben  (Neubildung?)  icpvrjv]  cpvrov  , Gewächs, Pflanze,  Kind,  Geschwür',  q)vri  ,Wuchs;  Natur,  Charakter',  cpviia  n.  , Ge- wächs, Geschwür',  (pvaig  , Natur',  (pvXov  n.  , Stamm,  Geschlecht,  Art',  (folrj , Gemein  de  und  von  ihr  gestellte  Heeresabteilung'  (:aksl.  byh,  Z-Partiz.  byhje); dehnstufiges  *bhö[u]lo-  vielleicht  in  gjwAsdg,  q}ü}X€i6g  , Schlupfwinkel,  Lager wilder  Tiere',  cpcjXsvco  , schlafe  in  einer  Höhle',  qxoXls  ,ein  Seefisch,  der sich  im  Schlamm  verbirgt';  aber  aisl.  böl  n.  , Lager  für  Tiere  und  Men- schen', ist  kein  von  böl  (wohl  aus  %öpla)  , Wohnstätte'  verschiedenes  Wort; dazu  schwundstufig  schwed.  mdartl.  bylja,  bölja  ,kleines  Nest'  aus  *bitlja.
Als  2.  Kompos.-glied  in  vftsgcpvi^g,  vTC€Q-g)[*f]iaXog.    Über  q)Trv  s.  unten.
Illyr.  VN  Buni,  ON  Bovvvog  (:  iilb.  bune).
Messap.  ßvQLov  6Lxr][.i(Xj  ßavqla'  ohia  Hes.  (:ahd.  bür);
10*
148
alb.  hujj  hüj  (*bunjö)  ,wohne,  übernachte',  burr,  burre   (*buro-)   ,Manu^i; Ehemann',  baue  ,Wohnung,  Aufenthalt,  halb  verfallenes  Haus'  {*bhouona: a,i.  bhavanam),  banoj  , wohne';  bun{e)  , Sennhütte'  {Hhuna)]  vielleicht  auch böte  ,Erde,  Boden,  Welt,  Leute'  (*bhiiä-tä  oder  *bhue-tä).
Lat.  fui  (alat.  füi)  ,bin  gewesen'  aus  */ü-ai,  Umgestaltung  des  alten Aor.  *füm  (==  gr.  e-cpvv,  ai.  d-bhüt  ,er  war*),  fu-türus  ,künftig',  forein ,wä.r q',  fore  ,sein  werden',  alat.  Konj.  fuam,  fuat  ,sei'  (^bhuuäm;  vgl.  Üt, büvo  ,war'  aus  *bhuuät),  daneben  -bam  (*bhuäm  :  osk.  fu-fans  ,erant',  air. -bä  ,ich  war')  in  lege-bam  usw.,  vgl.  lat.-fal.  -bö  (aus  *bhuö)  in  amä-ho alat.  veni-bö,  fal.  pipafp  usw.  mit  dem  ir.  6-Futurum  (do-rlmiub  ,ich  werde aufzählen'  aus  "^to-rlm-l-buö),  Intensiv  futävit  ,fuit';
osk.  fu-fans  ,erant',  fu-fens  ,fuerunt',  fusid  =  lat.  foret,  fust  (=  umbr. fust)  ,erit'  und  ,fuerit',  fuid  Konj.-Perf,  ,fuerit';  aber  über  futir  ,Tochter'  s. Vetter  Gl.  29,  235,  242  ff.  gegen  WH.  I  557,  867;
umbr.  fust  ,erit',  furent  ,erunt'  (*fuset,  *fusent),  f^fure  ,fuerint',  futu ,esto'  (fuuetöd  oder  fu-töd).
Ein  ^o/^-Präs.  zur  Wz.  ^^i/iz^-  :  *bhu-iiö  liegt  vor  in  lat.  flöj  fien ,werden,  entstehen,  erzeugt  werden',  das  l  statt  i  von  fls^  fit  {*bhu-i-si^ *bhu-l-ti)  bezogen;  osk.  fiiet  {^bhuiient)  ,fiunt',  umbr.  fito  , facta,  bona?-, fuia  ,flat',  fuiest  ,flet'  (*bhu-{ö  neben  *bhuiiö  wie  in  lesb.  cpvio),  s.  oben);
lat.  Nominalbildungen  nur  in  dubius  , zweifelnd,  unsicher'  (*du'bhi- iio-s  ,doppelgestaltig',  vgl.  umbr.  difue  ,bifidum'  <  *dui-bhuiom),  probns ,gut  gedeihend,  redlich'  (*pro-bhuos  :  ai.  pra-bhü-h  , hervorragend'),  osk. am-prufid  ,improbe',  prufatted  ,probävit',  umbr.  prüfe  ,probe';  lat.  super-bns ,hochmütig'.
Über  lat.  moribundus  s.  Niedermann  Mel.  Meillet  104,  Benveniste MSL.  34,  189.
Air.  bae  ,Nutzen'  {Hhud-iom),  büan  ,standhaft,  gut'  (Hhouno-,  dazu cymr.  bun  ,Königin,  Frau');  mir.  baue  ,Heim,    Ort'  (Hhud-liio-)-^
air.  buiih  ,sein'  (ursprgl.  Dat.  des  ä-St.  both  <  Hhuta  ==  cymr.  bod, corn.  bos,  bret.  bout  =  air.  both  f.  ,Hütte',  cymr.  bod  f.  , Wohnung'  :  lit. bütas  ,Haus';  hierzu  auch  mir.  for-baid  ,Grabtuch,  Bahre'),  Fut.  -bla ,wird  sein'  (=  lat.  fiat),  Prät.  1.  Sg.  bä  {*bhuäm),  3.  Sg.  bol  (*bhöue), Pass.  Prät.  -both  ,man  war'  {Hhu-to-) ;  das  Paradigma  des  Verbum  Subst. und  der  Kopula  besteht  aus  Formen  von  es-  und  bheu-,  z.  B.  hat  die 1.  Sg.  Präs.  Konj.  air.  beu  (*bh-esö)  den  Anlaut  von  bheu-  bezogen;
air.  -biu  ,ich  pflege  zu  sein',  mcymr.  bydaf  corn.  bethaf  mbret.  bezaff ds.  {Hhuij,ö  =  lat.  fiö,  daneben  *bhui-  in  air.  blth,  mcymr.  bit  ,estö'  = lat./tO;
gall.  PN  Vindo-bios  {*-bhuiios),  vgl.  cymr.  gwyn-fyd  ,Glück'  (, weiße  Welt', byd),  air.  su-b{a)e  ,Freude'  {*su-bhuiio-\  du-b{a)e  (du  =  gr.  dvg-)  ,Trauer';
149
o-ot.  hauan  ^wohnen,  bewohnen'^  ald  bauan  ^ein  Leben  fübren'^  gabauan W'obnung'  aufscblagen^  {*hhöuö,  Vokalismus  wie  in  ai.  hhävayati,  bhäva-h, slav.  baviti),  aisl.  büa  (bjö,  büinn)  ^wobnen^  instand  bringen,  ausrüsten^, acrs.  büan  und  buic{i)an  (büde,  gebüen)  , wohnen,  bebauen^  (daneben  ags. löqian,  afries.  bögia  , wohnen^,  lautlicher  Typus  von  got.  stöja  aus  *stöioijö und  ö  als  ursprünglichen  Vokal  stützend),  abd.  büan  (büta^  gibüan)  ,wohnen, bebauen^;  nhd.  bauen]  aisl.  byggja  ,an  einem  Orte  wohnen,  bebauen,  be- völkern*, später  , erbauen,  bauen'  (aus  *buwwjan?  *bewwjan?)]  aisl.  bü  n. \A^ohnort,  Wirtschaft,  Haushalt',  ags.  bü  n.  ,Vi^ohnung'  (PI.  by  n.  vom i-St.  *büwi-  =  aisl.  byr  m.  ,  Wohnstätte,  Hof;  ähnlich  lit.  6üm5 , bleibender Aufenthalt*),  abd.  bü,  mhd.  bü.  Gen.  büwes  m.,  selten  n.  ,Bestellung des  Feldes,  Wohnung,  Gebäude',  nhd.  Bau-,
aisl.  büd  f.  ,Wohnung,  Zelt,  Hütte';  aschwed.  böp,  mnd.  böde,  mhd. biiode  und  büde  , Hütte,  Gezelt',  nhd.  Bicde  (%hö[u]-tä);  mnd.  bödel  ,Ver- mögen',  böl  , Landgut',  ags.  bold  und  botl  n.  ,Wohnung,  Haus',  *byldan, engl,  to  build  ,bauen',  afries.  bold  und  bödel  ,Haus,  Hausgerät,  Eigentum' (*böpla-  aus  idg.  *bhö[u]tlo-  und  *bupla-,  vgl.  lit.  büklä  und  westsl.  bydlo), ebenso  aisl.  böl  n.  ,Wohnstätte'  (s.  oben  auch  zu  böl  , Lager');
aisl.  bür  n.  , Vorratshaus,  Frauengemach',  ags.  bür  m.  , Hütte,  Zimmer', abd.  bür  m.  ,Haus,  Käfig',  nhd.  (Vogel-) Bauer,  wovon  ahd.  nähgibür,  ags. neahgebür,  nhd.  Nachbar,  engl,  neighbour  und  ahd.  gibür{o),  mhd.  gebür(e)f dann  bür,  nhd.  Bauer  ,rusticus';
ags.  beo  ,ich  bin'  (*bhunö  =  lat.  /lö,  air.  -6m),  daneben  beom,  ahd. 6im  usw.  nach  *m  von  *es-  ,sein',  wie  ahd.  bis(t),  ags.  6i5  nach  is.
Vielleicht  got.  bagms,  ahd.  böum,  ags.  6eam  ,Baum'  aus  *bhou{d)mo' ,(pvt6v'  und  aisl.  bygg  n.  ,Gerste',  as.  Gen.  Fl.  bewö  ,Saat,  Ertrag',  ags. beoic  n.  , Gerste'  (*6ei(;u;a-)  als  , Angebautes'.
Lit.  buti  (lett.  öw^,  apr.  boüt)  ,sein',  bidu  Supin.  ,zu  sein'  (apr.  büton Inf.),  Partiz.  bütas  , gewesen',  Fut.  büsiu  (lett.  büsu),  Frät.  büvo  ,er  war' (vgl.  auch  buvö-ju,  -ti  ,zu  sein  pflegen'  und  aksl.  Iter.  byvati),  Opt.  apr. bousai  ,er  sei',  Prät.  bei,  be  ,ev  war*  (von  einer  mit  -ei-  erweiterten  Basis);
lit.  büvis  m.  ,Sein,  Leben',  buvinUi  ,hie  und  da  ein  Weilchen  bleiben', apr.  buwinait  , wohnet!';
lett.  büsana  ,Sein,  Wesen,  Zustand',  apr.  bousennis  , Stand';  lit.  bixtas, apr.  (Akk.)  buttan  ,Haus';
lit.  büklas  (*bütla-)  ,cubile,  latebrae  ferarum',  pabuklas  ,Instrument, Gerät;  Erscheinung,  Gespenst',  büklä,  bükle  ,praesentia,  Wohnung',  ostlit. bükle  ds.  (s.  oben;  dazu  buklüs  ,weise,  schlau');
aksl.  byti  , werden,  sein',  lo-  Partiz.  byh  , gewesen'  (davon  byhje  , Kraut; Heilkraut',  vgl.  zur  Bed.  cpvTÖv),  Aor.  be  ,war'  (*bhue-t)]  Imperf.  b^ase, Fut.  Partiz.  ksl.  by§esteje,  by§qsteje  ,Td  fxsllov,  Kondiz.  3.  PL  bg  (*bhuä-nt),
150  •
Partiz.  za-Hvem  ^vergessen',  neben  sonstigem  Partiz.  *byt  z.  B.  in  russ. zahytyj  , vergessen^,  vgl.  dazu  auch  Subst.  russ.  byt^  ^Wesen,  Lebensart' u.  dgl.^  apoln.  byto  ^Nahrung^,  aksl.  ^z-byt^k^  ^Überfluß,  Rest^  u.  dgl,  bythj^ ,das  Dasein^;
aksl.  zabyth  ^Vergessen',  pobyth  ,^ieg',  pi-ebyth  , Aufenthalt^;  russ.  hyt^ ,Wesen;  Geschöpf;  Tatbestand^;
Präs.  aksl.  bgdg  ^werde,  ylyvo^ai^  als  Fut. :  , werde  sein^  (ob  zu  lat.  Adj. auf  -bundus?)',  Kaus.  aksl.  izbaviti  , befreien^  erlösen'  n.  dgl.  (:  ai.  bhäva- yati,  vgl.  zum  Vokalismus  auch  got.  bauan  und  aksl.  zabava  ^Vervreilen Beschäftigung,  Zeitvertreib');  cech.  bydlo  , Aufenthaltsort,  Wohnung',  poln^ bydh  ,Vieh'  (aus  *,Stand,  Wohlstand,  Habe').
Vielleicht  hierher  (Pedersen  Toch.  228^)  tocb.  B  pyautk-^  A  pyotk- AB  pyutk-  ,zustande  kommen',  med.  ,zustande  bringen'.
Von  der  Basis  bh(e)ui-:
npers.  Imp.  bl-d  ,seid!';  apers.  Opt.  bi-yä^  setzt  Wackernagel  KZ.  46, 270  ==  ai.  bhü-yä-h,  -t-
gr.  (ptzv  n.  ,Keim,  Sproß'  =  q)iTv^La,  (pijvo)  , erzeuge,  säe,  pflanze';
lit.  alt.  bit(i)  ,er  war',  auch  Kondit.  1.  PI.  {süktum-)  bimej  lett.  biju.^ bij ß  jichj  er  war'  (lett.  bijä-  erweitert  aus  athemat.  *bhul-);  ablaut.  aprj bei,  s.  oben;
aksL.  Kondit.  2.  3.  Sg.  bi  , wärst,  wäre'  (*bhul-s,  *bhui-t),  m'ozu  sekundär 1.  Sg.  bi-mh  mit  Primärendung.
WP.  II  140f.,  WH.  I  375 f.,  504f.,  557  f.,  865,  867,  EM.  812f.,  1004f., Trautmann  40  f..  Feist  83  f.
Specht  will  (KZ.  59,  58  f.)  unter  Heranziehung  von  gr.  (paJ^og  , Licht, Heil'  =  ai.  bhava-  , Segen,  Heil',  cpaa-al-ußQOTog  usw.  unsere  Wz.  als *bhaud-^  nicht  als  *bheud-  ansetzen.    S.  auch  oben  S.  91.
bheudh-,    nasal,    bhu-n-dh-    ,wach    sein,    wecken,    beobachten;    geweckt, geistig   rege,   aufmerksam   sein,  erkennen,   oder  andere   dazu    veran- lassen (aufpassen  machen,  kundtun,  gebieten;  darbieten)'. Themat.  Präs.  in  ai.  bödhati,  bödhate  , erwacht,  erweckt,  ist  wach,  merkt, wird    gewahr',    av.    baodaiti    ,nimmt   wahr',    mit  paiti-  ,sein   Augenmerk worauf  richten'  (=  gr.  7tsvd^o(.iaij  germ.  *biudan,    abg.    bljudg);    Aor.    ai. bhuddnta  (=  invd-ovTo),  Perf.  bubödlia,  bubndhimd  (:  germ.  *baud,  *budurn), Partiz.  buddhd-  , er  wacht,  verständig;  erkannt'  (=  gr.  ä-nvarog  ,unkundig; unbekannt'),    buddhi-    f.    , Einsicht,  Verstand,    Meinung,    Absicht'    (=  av. paiti-busti-    f.    ,das    Bemerken',    gr.  nvotig    ,das    Nachforschen,    Fragen; Kunde,  Nachricht');  Kausativ  in  ai.  5öc^M7/a<i  , er  weckt;  belehrt,  teilt  mit', av.    baodayeiti   ,bemerkt,    fühlt'  (=  abg.    buzdg,    buditi,   lit.  pasibaudyti)] Zustandsverb  in  ai.  budhydte  ,erwacht,  wird  gewahr;  erkennt',  av.  buiöyeiti
■m
151
=== leaf number of line 2073 ===
155
```


## [2026-09-05T14:07:24.093Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT bumi ===\"; grep -n \"^bumi\\|^būmi\\|bumi-\" KNT.txt | head -20\necho \"=== KNT bav ===\"; grep -n \"^bav\\|bav-\" KNT.txt | head -20\necho \"=== AHD bheu ===\"; grep -n -i \"bheu\" AHD_watkins1985.txt | head -30",
 "description": "Grep Kent and AHD"
}
```


### [2026-09-05T14:07:24.159Z] TOOL RESULT

```
<persisted-output>
Output too large (32.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bp1zc31rs.txt

Preview (first 2KB):
=== KNT bumi ===
=== KNT bav ===
709:bavatiy DNb 14, bawatiy DNbv 14.
1418:ОР. 2d sg. opt. biyā, 3d sg. biya', from *bhy- né-, to root *bheus; see Lex. siy bav-.
2901:ПІ. The verb bav- ‘become’ may fairly be con- sidered here, cf. the German true passive with werden ‘become’, while Gm. sein ‘be’ forms only a passive of state, in which the participle is merely an adjective. With predicate participles OP bav- appears only in XPh 55, just cited; m DSf 25 yaà katam abava the participle has become sub- stantival and is subject.
5741:bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
5743:biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
=== AHD bheu ===
...
</persisted-output>
```


## [2026-09-05T14:07:25.743Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT pagoda ===\"; grep -n -i \"^PAGODA\\|pagoda\" SKT.txt | head\necho \"=== LKT pagode ===\"; grep -n -i \"pagod\" LKT.txt | head\necho \"=== AID pagoda ===\"; grep -n -i \"pagoda\" AID.txt | head\necho \"=== HJB pagoda ===\"; grep -n -i \"^PAGODA\" HJB.txt | head",
 "description": "Grep pagoda in SKT LKT AID HJB"
}
```


### [2026-09-05T14:07:25.822Z] TOOL RESULT

```
=== SKT pagoda ===
23625:Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
=== LKT pagode ===
1017:373.  Pers.  batkädä: 'Götzentempel'  [aus  pers.  but  'Götzen- bild' Horn  NpEt  S.  42,  Nr.  182  und kädä  'Haus'  ebenda  S.  188,  Nr.  844; käd,  kädä  ist  in  Zusammensetzungen der  Ort,  wo  sich  etwas  dauernd  befindet, untergebracht  oder  aufbewahrt  wird, vgl.  BARTHOLOMAE  in  ZfdWf  VI,  354] ; hieraus  ergab  sich  durch  Kontamination mit  präkrta  bhagodi  'göttlich,  heilig' [aus  sskr.  bhaga-vatl,  d.  h.  'Gott-begabt', also  'göttlich',  vgl.  Ascoli,  Studi  orien- tali  e  linguistici  S.  268/269,  Nr.  5,  wo auch  gesagt  ist,  daß  zuerst  die  Münzen mit  dem  Bilde  der  Pärvati,  Sivas  Gattin, so  hießen]  der  pg.  Ausdruck  pagoda, eugl.  pagoda,  pagode,  dtsch.  Pagode,  it. pagodo,  rum.  pagoda,  poln.  pagoda. Hierunter  versteht  man  jetzt  einen  Tem-
1020:pel,  besonders  in  China  solche  von  ganz bestimmtem  Äußeren,  für  das  der  nun zerstörte  Porzellanturm  von  Nanking als  typisch  angesehen  werden  kann; zahlreiche  vorzügliche  Abbildungen  von Pagoden  s.  bei  Ernst  Boerschmann, Baukunst  und  Landschaft  in  China. Berlin  s.  a.  (1923),  z.  ß.  S.  7—9,  45.  — [Zahlreiche  andere  Ableitungen,  wie Verdrehung  eines  ind.  Wortes  dagoha oder  aus  pg.  pagäo  aus  lat.  paganus oder  aus  chines.  pai-ku-td  'Turm  der weißen  Knochen',  sind  weniger  wahr- scheinlich.] [Hobson-Jobson  652/657. Hirth  ChinFW  200.
3079:Ebenso  tamul.  Ungarn  'membrum  virile', das  buddhistische  Emblem  des  Mahä, Deva  (Siva),  das  sich  als  Kegel  aus schwarzem  Stein  in  den  Pagoden  dieser Gottheit  findet.  In  den  Reisebeschrei- bungen über  Indien  häufig  als  Lingam, engl,  lingam  erwähnt.
6122:pagoda  373
7150:pagodo  373
7691:pagoda  373
8731:pacea  1601 paciaurä  1602 padi^a(c)h  1604 pafta  165 pagodä  373 paiantä  1611 paic  1608 pa/a  1615 pahnac  1636 ^?a/o^'  1615 pambria  1617 pangea  1621 pajjucßj  1625 2>ar«  1626 paradis  1631 paraleü  1626 parmac(lic)  1636 pastramä  261 ^Jasi»  1652 pälämar  1616 pärälujä  1626 pätlägea  161 pehlivan(ie)  1607 i^eZie«  1645 j>e/<»c  1646 pemheü  1617 perciun(at)  1629 perrfaf  1637 i>errfea  1630 perdeluß  1630 i^er^Äe/  1635 peruzea  609 2)ervaz  1638 pesmet  1642 pe^ches  1663 peschir  1660 pesim  1662 1662 pestimun  1674 pezevenche  1658 pezevenchm  1658 pezevencl'ic  1658 ^f'c«"«  1653 i>jf^/c  1670 ^tVaf  1656 pivgea  1620 pingelui  1620 pisicä  1661 /)?7ar  1654
=== AID pagoda ===
562:Archdka.  [Kanarese.]  The  officiating priest  of  a   pagoda.
1089:Bhatta.  [Sanskrit.]  A   title  used  in addressing,  01  affixed  to  the  name of,  a   learned  Brdhman.  In  Tamil it  denotes  the  officiating  priest  in  a pagoda.
2869:Hoon.  [Hindi  huny  from  the  Kana- rese  honnu^  gold.]  A   gold  coin,  the star  pagoda.
5145:Pagoda.  [According  to  Webster  from the  Persian  but,  an  idol,  and  kodak , a   house ;   but  perhaps  only  a   corrup-
5147:Pagoda.  A   gold  or  silver  coin,  for- merly coined  at  Madras,  and  worth about  three  and  a   half  or  four  rupees. It  used  to  be  thought  that  the  coin was  so  called  from  the  device  of  a temple  which  it  bore,  but  the  name seems  to*be  older  than  the  device, and  the  derivation  from  Bhagawati (said  to  be  a   name  of  Pdrwati)  is now  generally  accepted.  The  pa- goda was  divided  into  forty-five fanams.
7090:Varahd.  [Tamil.]  The  gold  coin commonly  called  by  Europeans pagoda.
=== HJB pagoda ===
16191:PAGODA.
16214:PAGODA,  s.  This  obacure  and remarkable  word  is  used  in  three different  senses.
16216:PAGODA.
16218:PAGODA.
16232:PAGODA.
16234:PAGODA,
16243:PAGODA.
16245:PAGODA.
16262:PAGODA,
16264:PAGODA.
```


## [2026-09-05T14:07:35.666Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in \"SKT.txt 23625\" \"AID.txt 5145\" \"LKT.txt 1017\" \"HJB.txt 16214\"; do set -- $f; echo \"== $1 line $2 leaf: $(awk -v L=$2 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n}' $1)\"; done",
 "description": "Compute leaf numbers"
}
```


## [2026-09-05T14:07:36.008Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16214,16250p' HJB.txt",
 "description": "Read Hobson-Jobson PAGODA entry"
}
```


### [2026-09-05T14:07:37.168Z] TOOL RESULT

```
awk: cannot open "SKT.txt 23625" (No such file or directory)
== SKT.txt 23625 line  leaf: 
awk: cannot open "AID.txt 5145" (No such file or directory)
== AID.txt 5145 line  leaf: 
awk: cannot open "LKT.txt 1017" (No such file or directory)
== LKT.txt 1017 line  leaf: 
awk: cannot open "HJB.txt 16214" (No such file or directory)
== HJB.txt 16214 line  leaf:
```


### [2026-09-05T14:07:37.215Z] TOOL RESULT

```
PAGODA,  s.  This  obacure  and remarkable  word  is  used  in  three different  senses.
a.  An  idol  temple ;  and  also  specifi- cally, in  China,  a  particular  form  of religious  edifice,  of  which  the  famous "Porcelain  tower"  of  Nanking,  now destroyed,  may  be  recalled  as  typical. In  the  17th  century  we  find  the  word sometimes  misapplied  to  places  of Mahommedan  worship,  as  by  Faria-y- Sousa,  who  speaks  of  the  ""ncoda  of Mecca."
PAGODA.
653
PAGODA.
b.  An  idol.
C.  A  coin  long  current  in  S.  India. The  coinB  so  called  were  both  gold  and silver,  but  generally  gold.  The  gold pagoda  was  the  vardha  or  htln  of  the natives  (see  BOON) ;  the  former  name (f r.  Skt.  for  *  boar ')  being  taken  from the  Boar  avatar  of  Vishnu,  which  was ■figured  on  a  variety  of  ancient  coins  of the  South ;  and  the  latter  signifying *gold,'  no  doubt  identical  with  sond, :and  an  instance  of  the  exchange  of  h And  8,    (See  also  PABDAO.)
Accounts  at  Madras  down  to  1818 were  kept  in  pagodas,  fanaTtis,  and  kds (see  Cash)  ;  8%^ = 1  fanam,  42  fanams =  1  pagoda.  In  the  year  named  the Tiipee  was  made  the  standard  coin.* The  pagoda  was  then  reckoned  as «(^uivalent  to  3^  rupees.
In  the  suggestions  of  etymologies for  this  wora,  the  first  and  most })rominent  meaning  alone  has  almost tilways  been  regaraed,  and  doubtless justly ;  for  the  other  uses  are  de- duceable  from  it.  Such  suggestions have  been  many.
Thus  Chinese  origins  have  been propounded  in  more  than  one  form  ; e.g,  Pao-t^ahy  'precious  pile,'  and  Poh- Jeuh-fah  (*  white-bones-pile ').t  Any- thing can  be  made  out  of  Chinese monosyllables  in  the  way  of  etymology  ; though  no  doubt  it  is  curious  that  the first  at  least  of  these  phrases  is  actually applied  by  the  Chinese  to  the  polygonal towers  which  in  China  foreigners  speci- ally call  pagodas.  Whether  it  be possible  that  this  phrase  may  have ()een  in  any  measure  formed  in imitation  of  pagoda,  so  constantly  in the  mouth  of  foreigners,  we  cannot say  (though  it  would  not  be  a  solitary example  of  such  borrowing  —  sea IfEELAM)  ;  but  we  can  say  with  confi- dence that  it  is  impossible  pagoda should  have  been  taken  from  the Chinese.  The  quotations  from  Corsali and  Barbosa  set  that  su^^^tion  at  rest.
Another  derivation  is  given  (and adopted  by  so  learned  an  etymologist as  H.  Wedgwood)  from  the  Portuguese pagao,  *&  pagan.'  It  is  possible  that this  word  may  have  helped  to  facili- tate the  Portuguese  ado|)tion  of  i7a^o(2a; it  is  not  possihle  that  it  should  have given  rise  to  the  word.  A  third  theory makes  pagoda  a  transposition  of  da-
*  f^naep's  Uuful  Tablet,  by  E.  ThGmM,  p.  19. t  Giles,  Glo$$aiTf  ofltefennee,  8.  v.
goba.  T]ie  latter  is  a  genuine  woid, used  in  Ceylon,  but  known  in  Conti- nental India,  since  the  extinction  of Buddhism,  only  in  the  most  rare  and exceptional  way.
A  fourth  suggestion  connects  it  with the  Skt.  bhagavat,  'holy,  divine,'  or Bhagavatiy  applied  to  Durga  and  other goddesses ;  and  a  fifth  makes  it  a corruption  of  the  Pers.  but-kadah, *  idol-temple ' ;  a  derivation  given below  by  Ovington.  There  can  be little  doubt  that  the  origin  really  lies l>etween  these  two.
The  two  contributors  to  this  book  are somewhat  divided  on  this  subject : —
(1)  Against  the  derivation  from hhagavaty  *holy,'  or  the  Mahr.  form bhagavant,  is  the  objection  that  the word  pagode  from  the  earliest  date  has the  final  e,  which  was  necessarily  pro- nounced. Nor  is  bhagavant  a  name for  a  temple  in  any  langua^  of  India. On  the  other  hand  but-kadan  is  a  phrase which  the  Portuguese  would  constantly hear  from  the  Mahommedans  with whom  they  chiefly  had  to  deal  on their  first  arrival  in  India.  This  is the  view  confidently  asserted  by  Rei- naud  (M^moires  sur  VInde,  90),  and  is the  etymology  given  by  Littre.
As  regards  the  coins,  it  has  been supposed,  naturally  enough,  that  they were  called  pagoda,  because  of  the figure  of  a  temple  which  some  of  them bear ;  and  which  indeed  was  borne  by the  pagodas  of  the  Madras  Mint,  as may  be  seen  in  Thomas's  Prinsep,  pi. xlv.  But  in  fact  coins  with  this  im- press were  first  struck  at  Ikkeri  at  a date  after  the  word  pagode  was  already in  use  among  the  Portuguese.  How- ever, nearly  all  bore  on  one  side  a  rude representation  of  a  Hindu  deity  (see e,g,  Krishnaraja's  pagoda,  c.  1520),  and sometimes  two  such  images.  Some  of these  figures  are  specified  bv  Prinsep (Useful  Tables,  p.  41),  and  Varthema speaks  of  them;  "These  pardai  .  .  . liave  two  devils  stamped  upon  one  side of  them,  and  certain  letters  on  the other"  (115-116).  Here  the  name may  have  been  appropriately  taken from  bhagavat  (A.  B.l.
On  the  other  hana,  it  may  be  urged that  the  resemblance  between  btU- kadah  and  pagode  is  hardly  close enough,  and  that  the  derivation  from but-mdah  does  not  easilv  account  for all  the  uses  of  the  word.  Indeed,  it seems  admitted  in  the  preceding  para-
PAGODA.
654
PAGODA,
graph  that  bhagavat  may  have  had  to do  with  the  origin  of  the  word  in  one of  its  meanings.
Now  it  is  not  possible  that  the  word in  all  its  applications  may  have  had its  origin  from  hkagavai,  or  some current  modification  of  that  word? We  see  from  Marco  Polo  that  such  a term  was  currently  known  to  foreign visitors  of  S.  India  in  his  day— a  term almost  identical  in  sound  with  pagodoy and  bearing  in  his  statement  a  religious application,  though  not  to  a  temple.* We  thus  have  four  separate  applications of  the  word  pacatUa,  or  pagoda^  picked \xp  by  foreigners  on  the  shores  oi  India from  the  13th  century  downwards,  viz. to  a  Hindu  eiaculatory  formula,  to  a place  of  Hindu  worship,  to  a  Hindu idol,  to  a  Hindu  coin  with  idols  repre- sented on  it.  Is  it  not  possible  that  all are  to  be  traced  to  hhagavaJt^  ^sacred,' or  to  Bhapavat  and  Bhcigavati,  used  as names  of  divinities — of  Buadha  in Buddhist  times  or  places,  of  Krislma and  Durga  in  Brahminical  times  and places?  (uses  which  are  fact).  How common  was  the  use  of  Bhagavaii  as the  name  of  an  object  of  worship  in Malabar,  may  be  seen  from  an  ex- ample. Turning  to  Wilson's  work  on the  Mackenzie  MSS.,  we  find  in  the list  of  local  MS.  tracts  belonging  to Malabar,  the  repeated  occurrence  of Bhagavati  in  this  way.  Thus  in  this section  of  the  book  we  have  at  p.  xcvi. (vol.  ii.)  note  of  an  account  "of  a temple  of  Bhagavati '' ;  at  p.  ciii. "Temple  of  Mannadi  Bhagavati  god- dess .  .  .";  at  p.  civ.  "Temple  of Mangombu  Bhagavati  .  .  . "  ;  "  Temple of  Paddeparkave  Bhagavati  .  .  . " ; "Temple  of  the  goddess  Panndyennar Kave  Bhagavati  .  .  .";  "Temple  of the  goddess  PatdU  Bhagavati  .  .  ." ; "  Temple  of  Bhagavati  .  .  .  "  ;  p.  cvii., "Account  of  the  goddess  Bhagavati  at, &c.  .  .  . " ;  p.  cviii.,  "  Ace.  of  the goddess  Yalanga  BhagavaHy"  "Ace.  of
♦  "  The  prayer  that  they  say  daily  oonaists  of these  words :  '  Paeauta  !  PaccnUa!  PaomUa/ '  And this  they  repeat  104  times.  "—(Bk,  lii.  ch- 17.)  The word  is  printed  in  Ramusio  fMcauoa ;  but  no  one fomiliar  with  the  constant  conftiHion  of  e  and  t  in medieval  manuscript  will  reject  this  correction  of M.  Fauthier.  Bishop  Caldwell  obeerves  that  the word  was  probably  Bagavd,  or  Pagava^  the  Tamil form  of  Bhaaavata^  "  Lord  " ;  a  word  reiterated  in their  sacred  formulie  by  Hindus  of  all  sorts, especially  Vaishnava  devotees.  The  words  given by  Marco  Polo,  if  written  ** Pagoda/  Pagoda f Pagoda/"  would  be  almost  undistingoishable  In sound  from  PaeatUa,
the  goddess  Vallur  Bhaaavati,"  The- term  Bhagavati  seems  uius  to  have been  very  commonly  attached  to objects  of  worship  in  Malabar  temples (see  also  Fra  Paolinoy  p.  79  and  p.  57, quoted  under  c.  below).  And  it  is- very  interesting  to  observe  that,  in  & ^per  on  "Coorg  Superstitious,"  Mr. Kittel  notices  parenthetically  that Bhadra  Kali  {i,e.  Durga)  is  "also called  Pogddi,  Pavodiy  a  tOidbhava  of Bagavati"  (Ind.  Antiq,  ii  170)— an incidental  remark  that  seems  to  brin^ us  very  near  the  possible  origin  of pagode.  It  is  most  probable  that  some form  hkepogodi  or  pagode  was  current in  the  mouths  of  foreign  visitors  be- fore the  arrival  of  the  Portuguese ; but  if  the  word  was  of  Portuguese origin  there  may  easily  have  oeen some  confusion  in  their  ears  between BagavcUi  and  hut-kadah  which  shaped the  new  word.  It  is  no  sufficient  ol>> jection  to  sav  that  bhagavati  is  not  a term  applied  by  the  natives  to  a temple ;  the  (question  is  rather  what misunderstanding  and  mispronuncia- tion by  foreigners  of  a  native  term may  probably  have  given  rise  to  the term?-(H.Y.)
Since  the  above  was  written.  Sir Walter  Elliot  has  kindly  fumi^ed  a note,  of  which  the  following  is  an extract : —
"I  took  some  pains  to  get  at  the origin  of  .the  word  when  at  Madras, and  the  conclusion  I  came  to  was  that it  arose  from  tbe  term  used  cenerally for  the  object  of  their  worsSin,  viz., Bhagavat^  '^od' ;  bhagavatiy  'goadess.'
"Thus,  the  Hindu  temple  with  ita lofty  goptiram  or  propylon  at  once attracts  attention,  and  a  stranger  en- quiring what  it  was,  would  be  told, '  the  house  or  place  of  Bhagavat.*  The village  divinity  throughout  the  south is  always  a  form  of  Durga,  or,  as  she is  commonly  called,  simply  *2>m'(or Bhagavati,^  the  godaeaa^.  .  .  .  In  like manner  a  figure  of  Durga  is  found  on most  of  the  gold  Hum  (i,e,  pagoda coins)  current  in  the  Dakhan,  and  a foreigner  inquiring  what  such  a  coin was,  or  rather  what  was  the  form stamped  upon  it,  would  be  told  it  was *  the  goddess,*  t.e.,  it  was  '  BhagavaiiJ  "
As  my  friend,  Dr.  Bumell,  can  no longer  represent  his  own  view,  it  seems right  here  to  print  the  latest  remarks
PAGODA.
665
PAGODA.
of  bis  on  the  subject  tbat  I  can  find. They  are  in  a  letter  from  Tanjore, dated  March  10,  1880:  —
'*  I  think  I  overlooked  a  remark  of yours  r^iardinff  my  observation  that the  e  in  Pagoae  was  pronounced,  and that  this  was  a  difficulty  in  deriving it  from  Bhagavat.  In  modem  Portu- guese eia  not  sounded,  but  verses  show that  it  was  in  the  16th  century.  Now, if  there  is  a  final  vowel  in  Pagoda,  it must  come  from  Bhagavati;  but  though the  goddess  is  and  was  worshipped  to a  certain  extent  in  S.  India,  it  is  by other  names  (Amirui,  &c.).  Qundert and  Kittel  give  ^Pogodi'  as  a  name  of a  Durga  temple,  but  assuredly  this  is no  corruption  of  Bhagavati,  but  Pa- goda !  Malayalam  and  Tamil  are  full of  such  adopted  words.  Bhagavati  is little  used,  and  the  j;oddess  is  too  in- significant to  give  nse  to  pagoda  as  a general  name  for  a  temple.
*^  Bhagavat  can  only  appear  in  the S.  Indian  languages  in  its  (Skt.) nominative  form  bha^avdn  (Tamil payuvdn).  As  such,  in  Tamil  and Malayalam  it  equals  Vishnu  or  Siva, which  would  suit.  But  pagoda  can't be  got  out  of  hkagavdn;  and  if  we  look to  tne  N.  Indian  forms,  bhagavant,  &c., there  is  the  difficulty  about  the  e,  to say  nothing  about  the  nt."
The  use  of  the  word  by  Barbosa  at so  early  a  date  as  1516,  and  its  appli- cation to  a  particular  class  of  temples must  not  be  overlooked.
1616.— "There  ia  another  sect  of  people among  the  Indians  of  Malabar,  which  is called  Cujavm\Kn$havan,  Logan.,  Malabary i.  115].  .  .  .  Their  business  is  to  work  at baked  clay,  and  tiles  for  covering  houses, with  which  the  temples  and  Royal  buildings are  roofed.  .  .  .  Their  idolati^  and  their idols  are  different  from  those  of  the  others  ; and  in  their  houses  of  prayer  they  perform a  thousand  acts  of  witchcraft  and  necro- mancy;  they  call  their  temples  pagodes, and  they  are  separate  from  the  others." — BarboM,  185.  This  is  from  Lord  Stanley  of Alderley's  translation  from  a  Spanish  MS. The  Italian  of  Ramusio  reads:  "nelle  loro orationi  fanno  molte  strigherie  e  necromatie, le  quali  chiamano  Pa^^es,  differenti  assai dall'  altre"  {Ramutio,  i.  f.  308v.).  In  the Portuguese  MS.  published  by  the  Lisbon Academy  in  1812,  the  words  are  altogether absent  ;  and  in  interpolating  them  from Ramnsio  the  editor  has  given  the  same  sense as  in  Lord  Stanley's  English. .  1616. — "  In  this  city  of  Goa,  and  all  over India,  there  are  an  infinity  of  ancient  build-
```


## [2026-09-05T14:07:58.628Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"SKT.txt:23625\" \"AID.txt:5145\" \"LKT.txt:1017\" \"HJB.txt:16214\"; do f=${p%%:*}; L=${p##*:}; echo \"== $f line $L leaf: $(awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n}' $f)\"; done\necho \"=== BRT buiti ===\"; grep -n \"būiti\\|buiti\\|Būiti\" BRT.txt | head -20\necho \"=== BRT bumi ===\"; grep -n \"^būmi\\|būmi-\" BRT.txt | head -10",
 "description": "Leaf numbers and Bartholomae greps"
}
```


### [2026-09-05T14:08:00.531Z] TOOL RESULT

```
== SKT.txt line 23625 leaf: 639
== AID.txt line 5145 leaf: 251
== LKT.txt line 1017 leaf: 57
== HJB.txt line 16214 leaf: 698
=== BRT buiti ===
=== BRT bumi ===
```


## [2026-09-05T14:08:09.009Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"pagod\" SKT.txt | head -20\necho \"=== leaf 386 (p.366) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==387' SKT.txt | head -40",
 "description": "Find Skeat pagoda entry"
}
```


### [2026-09-05T14:08:10.928Z] TOOL RESULT

```
23625:Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
=== leaf 386 (p.366) ===
cf.  mod.  E.  to  Afljf.  to  pxktt.^V.  poeAr,  a bag  ;  see  pouoh,  sv.  Poko  (i).
Pock  (I),  a  pustule.  (E. ;  ptrhaps  C.) Smali  pes  «  small  /«'*'.  where  pwki  ii pi.  of  poek,  M.  E.  pokke,  a  pock,  pi. Pekkes.  A.  S.  pec,  a  pustule.  +  Du.  pock, Gpcckit  a  (KKk.  ^.  Prob.  of  Celtic  origin, and  allied  to  poki  (i),  a  hag:  cf.  Gael. pMcaid,  a  pimple.  Irish  ptKoid,  a  pustule. ^£adM,  a  swelling  up,  Gael,  /or,  to  become like  a  hag. Focket;  see  Poke  (i). Pod;  «eeFad  (i).
Poem.  (F.-L. -Gk.)  F.i\7/w,Cot-L, /evwa.  — Gk.  woi^^,  a  woric,  composition, poem.  —  Gk.  iroui'i',  to  make.
po«sy.  (F.-L.-Gk.)  M.EpMsie^ F.  polite.  —  L.  poiiin.  ace.  of  pofsis,  poetry. —  Gk.  wm'ijnit,  a  composition,  poem.  — Gk, woitiv,  to  make.
poet.  i,F.  -  L.  -  Gk.)  F.  pofte.  -  L. po€i(i  — Gk.»o*i;Tni,  a  maker.  — Gk.  «t>i#r-i», to  make;  with  suffix  -t^i  of  the  agent.
posy.  (F.— L— Gk.)  In  all  its  senses, it  15  short  for  po<sy.  It  meant  a  short poem,  esp  a  ^ort  motto  in  verse  on  knives andrings.Hamlci.iii.i.i'^i;  hence  it  meant a  nosegay,  because  the  ftowers  chosen  for  it. enigmatically  rcptescn\*-(\  9^  \<^3vj  c^i  -mnwc^^
pchgkakt:
FOLTlUXnC
LT%
boa  oT  r*&^  Bvk^Ski.
lor  ncj  ia  Ike
MA  otf  iBMiiiim    (F.— Um
m1    vidi  /»Ay,    6oa
II  bM  aothbw  BodOL—
POOU
361
t  piee«
DttctageK^GIc
ef  ■lilM^  ia  oujiy ;  cnr.  oe«l  aif
!■»  ft  iowtr.  (U-Gk.)  L vk.  ««X^o#Df .  BUDy-  flowcnd. frany ;  i»#«t,  flower.
lay  wives.  •»  Gk.  nAv-,  madi ;
•vmknw  aunj  Un^ufcs. !»•,  ma,  many;  ^Xwrma ^  kapu^ ;  ue  OIom.
\m.  maay-ttilcil   pUne  figure.
Uk^,  nuay ;  Twrfo,  tn  angle,
(aee.
In.  ■  maay-tideH  solid  figiire.
|k^,  maay;  •ld^»',  for  IV<^  ^
h».  to  n't ;  see  Sit.
kL  (Gk.  offJ  L)     CoiDcd  lo
M«/.-Gk.  roA^,  maoy;  L.
k  terai.
Vl  animal  with  many  feet.
L.  f^yftu.  —  Gk.  voAuvot^,
P  Gic.  »oA^,  many ;  wvir,  foot.
U*.  (Gk.)     From  /W/-  aad
p.   (Gk.)     From  /0/j*-  and
^ommftde.  (F.-ltal.-L.)
Mmatam ;  so  called  becaose
mplea.  >•  lial.  /vmaJa^^^mata,
Ripple  one's  lips,  fip-salve/
```


## [2026-09-05T14:08:25.533Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"total leaves:\"; awk 'END{}{n+=gsub(/\\f/,\"\")} END{print n}' SKT.txt\nsed -n '23600,23640p' SKT.txt\necho \"=== printed page markers near leaf 639 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=636 && NR<=642 {print \"---LEAF\",NR; print substr($0,1,300)}' SKT.txt",
 "description": "Inspect Skeat appendix"
}
```


### [2026-09-05T14:08:27.428Z] TOOL RESULT

```
total leaves:
656
French  from  Italian:  bojilion,  bauble (j).  bergamot,  brigade,  brigand,  brigantine, brig,  bnisquc,  burlesque,  bust,  caprice,  ca- puchin, caronsal  (a),  casemate,  charlatan, frigate,  gala,  gallery,  gallias,  gazette,  gusset, maroon  (i),  pavjuin.  pa-^ninade,  pistol, pistole,  ravelin,  rodomontade  theorbo,  ton- tine.
Spanish :  anchovy,  banana,  basUnado, battledoor,  bilbo,  bilboes,  brocade,  cigar, cinchona  (chinchona),  embargo,  filigree, galleon,  galloon  ?,  imbargo,  paraquito, quixotic  rusk,  sarsaparilla.  tiHce  (1).
/'Yenchfrom  Sf>anish :  barricade,  bizarre, capstan,  caracole,  oordwainer,  morion  (mur  | rion),  shallop.
Portiigueu  :  cocoa  (1),  dodo,  cmn,  yam.
TTiis  is  a  general   term,  including   Russian,
French  from   OertnaM  from   Servian:
vampire-
Jiussian  :  drosky,  morse,  rouble  (ruble), stcin>e,  verst.
French  from  ICiiSsian :  ukase.
13.  A  word  of  LITHUANIAN  origin.  Curiously  enough,  there  Is  only  om Iglilh  word  which  can  be  traced  to  Lithuanian,  and  the  mtroductton  of  it  into fUsh  is  due  to  the  fact  that  it  had  been  borrowed  from  that  laagoage  by  the  Danes, '  it  talk.
French  from  Ifalian  from  Latin  from Greek  from  O.  Persian :  rice.
Spanish  from  Latin  from  Greek  from  ^ Persian:  pistachio  (pistacho).
Frc$ick    from     Lai  in    from    Pcrsianil peach  (0.
French  from  Low  Latin  from  Persian  \ zcdoary.
Jtalian  from  f^rsian :  sciaietar  (< icr)  ?.
14.  Words  of  PERSIAN  origin.
flertiani  bang  (t),  barbican?,  bashitw, LT,  caravan,  caravansary',  dervia  (der- bi.  divan,  durbar,  6rman,  ghoul,  bonri, leal,  jasmine  ijetsambe),  Lascar,  mohur,
b^hau,   I'artce,    pasha    (^lacha,    pashaw, saw),  peri,  »aih  Ca)>  Kpoy,  ibab,  shawl,
fftrntrntani  from    Persian-.    lamindar,
Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
Freneh  from  Italian  from  Persian:  car- case (^carcass),  jargonelle,  mommy,  orange« rebeck,  taffeta  (u(^tV^^.
French    from    S;«nuK    from    P«r»a» ]ulep,  (arabanA.
VI.     DISTRIBUTION   OF  WORDS,   ETC.
1
I
Portuguese  from  Persian :  pagoda,  v»- rnnHa  (verandah")?.
French  from  Portuptese  from  Persian  : be?  Oft  r.
French  from  Persian:  check,  chcckci (chequer),  checkers  (chequers),  che^s  ex- chequer, jar  (a),  lemoo,  lime  (3),  ounce (2)  ?,  rook  {%\  scarlet.
Dutch  from  Persian :  gherkin.
15.  Word*  of  SANSKRIT  origin.
Sanskrit',  avatar,  banyan,  brahmin  (brah- man), champak,  pundit,  lajnb,  Sanskrit^ nittec,  Veda.
I^tin  from  Greek  from  Sanskrit :  hemp, pepper,
French  from  iMtn  from  Greek  from Sanskrit;  beryl,  briUioiit,  ginger,  mace (a),  saccharine.
Fretuh  from  Latin  from  Greek  from Persian  from  Satukrit:  naid.
French  from  Spanish  from  Latin  from Greek  from  Persian  from  Sanskrit :  in- digo.
French  from  Latin  from  Persian  from Sanskrit:   musk.
Lorn  Latin  from  Arabic  fr^A borax.
Frettek  from  S/anish  from Persian:    hatard.    tahour    (tal hour?,  tambourine?.     FerkaPi
Spanish  from    TurkUk  frot lilac.
French   from    Arakir  from atmc
French  from  ftaiian  from  Latin  from
=== printed page markers near leaf 639 ===
---LEAF 636
soprano,  stanza,  stilcno,  trio.
mbonc?,    nmbrclla,     velvet,    vermicelli.
ifcta,  volcano.
Frtfukfrom  Italian  from  IjUim:  alarm {•.lanim),  alert,  apaitnunt,  arcade,  artii>an, nbum,  battalion,  bulletin,  cab  (i),  cabbage ;!>,  cape  (i),  capriole,  carnival,  cascade, ftfique.
---LEAF 637
ectern  (leetum). magnesia,  pericranium.
French  from  Leno  f-atin  from  Greek : acolyle.allegor}',  almanac,  anchoret  (anchor- ite), apostasy,  apostate,  botllc(i),  butler, jibuttery,  bushel,  calender,  calm,  carbine, card  (O,  CRile,  cnt»logue,  cauterise,  celan- dine, chronicle,  cl
---LEAF 638

smack  (3),  snaffle,  snap,  snip,  snuff  (O. spelicans,  splice,  spoor,  sprai,  stipple,  stiver, stoker,  stove,  ilrand  (a)  ?,  etnpe.  autler, swab,  switch,  tang  (Oi  tattoo  (i).  toy, trick  (t),  irick  (a),  trick  {7,\  trigger,  up- roar, wagoo  (waggon),  wainscot,  yacht, yawl 
---LEAF 639
 dialect,  though  dculy  ~ iiig  to  the  Teutonic  family.
French  from  Teutonic :  bacon,  bonrd  ?, brawl(a),  broil  (1),  burgeon, cantle, crochet, crosier,  crotchet,  croup  ^a),  crupper,  crush, damel  ?,  guide,  hoop  (a),  hubbub,  huge  !, label,  moat,  mock,  moraine,  patrol,  patt
---LEAF 640
 Curiously  enough,  there  Is  only  om Iglilh  word  which  can  be  traced  to  Lithuanian,  and  the  mtroductton  of  it  into fUsh  is  due  to  the  fact  that  it  had  been  borrowed  from  that  laagoage  by  the  Danes, '  it  talk.
French  from  Ifalian  from  Latin  from Greek  from  O.
---LEAF 641
n. Jrtm     Latin    from     Hebrew :
}m  Hebrew :  cabal. \ plates  in  PaJcstim :  bedlam,
Mantnatha. from  Greek  from  Syrieu  :  abbot,
BlftintQOD.
\  frmm  Latin  fr»m    Greek  from abbey,  damson.
Italian    from    Sjrriae :
ww  iM**  talmud,  targnm. tO:  alkali,  alkoran,  arrack,  atta
---LEAF 642
 [perhaps  Canarese]^ caddy,  cassowary,  cockatoo,  crease  \2'\  or creese,  dugong,  gong,  gntla-perclia,  lory (luiy),  mango,  mudc  (amuck),  orang- outang, proa  ( prow },  rattan,  sago, apas.
French  from  Malay:  ratafia.
French  from  Arabic  from  Malay:  cam- phor.
Ckineu'.  china,  Ch
```


## [2026-09-05T14:08:41.205Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n \"^būm\\|^bum\\|^bwm\\|^urwar\\|^but \\|^bwt\\|^būdan\\|^bawēm\\|^būdan\" PHD.txt | head -20\necho \"--- PHD grep loose but/bum ---\"; grep -n \"^b[uū]m\\|^but\\b\\|urwar\" PHD.txt | head -20\necho \"=== NYB ===\"; grep -n \"^bum\\|^būm\\|^but\\|^urvar\\|^urwar\" NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie and Nyberg lookups"
}
```


### [2026-09-05T14:08:41.270Z] TOOL RESULT

```
=== PHD ===
1125:but bē.
--- PHD grep loose but/bum ---
596:tru(f)š 84 urwar
599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
1125:but bē.
3148:plant (n.) urwar; medicinal ~ rürag; useless — züz.
4194:vegetable aroyisnig, tarrag, urwar; ~s ümiz.
=== NYB ===
557:urvar har cé ne ~ (se. hösitan) à nē hošet 9612-13, 9810-11; — apāyet būtan it is bound to happen, of predestination, explains jäyisn 271, brihenisn 16°; used itself as a nominal expression of Predestination: apäyet-bütan rād 16!!; — b) taking a v. n. as its complement: -šān ... gošt z"arisneh ne — it is not allowed for them to eat meat 10420-21; — e) governing a subordinate clause introduced by kū 8!. 1181-14 by ka 56?? (gl); without an introductory particle, with the governed vb. in ind. or in Subju.: ~ stdyé thou shalt profess 596; bē ~ apesihät 4419-19, v.s. v. apa- sistan. — MPrs ’b’yd with inf. (A-H II); Paz. āwāyastan āwāyad; āwāyastaa ‘re- quisite, desire’ (SGV); NP bäyistan, bā- yad; andar-vdi ‘desire, need (cf above no. 3; to be distinguished from andarvāt ‘atmosphere’, g. v.). Den. of OIr *updya- < *upa-aya- ‘that which comes upon, is imposed upon, affects a p.' = 1. need, 2. duty, cf Av. (150) upa-ay-, v. HP II, 17 sg.; Verbum 168; Ghilain 48. apāyišnīk ['p'dányk] proper, fit, fitting, handsome, nice, exquisite, comp. ~-tar, 33-5. 422, etc. passim; pl. cas. obl. ~-dn the qualified ones 1052,
978:but (also) 455-5; — b) but, however, contin- uing the narration: HajB:8 (second BL") [= bes HajA:7, v. below]; 197-24. 2115 ete. — MPrs by only with the enel. --c: byc ‘but’ (v. 4b) and in by-rwn (v. beron), in all other cases 5b’, to be read bd, shortened form in proclitic position (cf k? = ka, v.s.v. ka); MPrth byh ‘outside’, ^ byh, ^w byh ’rg; conj. byc, byž ‘but, however’, Prth. inscr. bes (v. below). Paz. be, bi, be; NP only prev. bi-. Original form *bét, cf bēt-ānak ‘an outsider, foreigner’; MPrs bydwm ‘outermost’ (S) = Paz. bétum (SGV). [MPrth byd ‘again, further’ (= MPrs dwdy) belongs to the numeral ‘two’, and not to this w.] — BR? 19% is a wrong ideogr. for beh, opt. of bütan.
2124:but we are here in a part of Iran where Greeks reigned for about 200 years after Alexander (v. Tarn, The Greeks in Bactria & India, 1951). There is every reason to believe that their kings and magnates erected monumental buildings over their tombs, with which the Yvy1 of the de- ceased was in some way connected. The Greek Yvx1 could, however, only be ren- dered in Iranian by jän, as the ruvān belonged to a quite different sphere. Prob- ably these seven jdnakdns were built in the seven cities which Alexander founded in Bactriana and Sogdiana (Justin XII, 5, 8). The later attribution of such ancient monuments to the primordial heroes of East Iranian antiquity is a phenomenon too well known to need comment, cf Taxt + Jamsid, Nags 1 Rustam and the like. — Strictly speaking the reading HY?-d’n' = jän-dän 're- captacle of the jan’ would be admissible (cf uvnuciov Ļvxījg of the cinerary urn Sophocles, Electra 1126-1127), but this interpretation is perhaps too hazardous. — jānakān has a parallel in MPrs rw’ng’n, MPrth ’rw’ng’n ‘belonging to, serving the ruvan’, of pious works.
3853:urvar [^wlwl] plant, generally coll. plants, passim; pl. cas. rect.: ~ rust hend 41?*; 6 čišan ~, v.8.v. öl, 6; pl. cas. obl. w-än 215. 8919, 9335; pl. —-iha 105!. — Av. (401 sqq.) urvarä-; MPrs ’wrwr.
3854:urvar-eihrak [~-cyhlk'] containing the seed of the plants 87°. — V. chr and cih- rak, and cf āp-cihrāak.
5397:urvará-: urvar
6499:bum: ~
```


## [2026-09-05T14:08:42.245Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN budan/bum/but ===\"; grep -n \"būdan\\|budan\" HRN.txt | head -20\necho \"--- HRN but ---\"; grep -n \"but 'Götze\\|Götze\" HRN.txt | head -20",
 "description": "Horn lookups"
}
```


### [2026-09-05T14:08:42.300Z] TOOL RESULT

```
=== HRN budan/bum/but ===
--- HRN but ---
1991:W82. but ^Götzenbild; Liebchen.
11113:20Ii. nxd{i)st (meist uj' geschrieben) *), uzd{i)stäv 'Götzen-
11114:bild', nzd{i)stparast(i)&nlh 'Götzenanbetung (Men.),
11115:uzdejär (päz. uzdezdr) *Götzentemper.
```


## [2026-09-05T14:08:50.958Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 182 ===\"; sed -n '1985,2000p' HRN.txt\necho \"=== HRN leaf of 1991 ===\"; awk 'NR<=1991{n+=gsub(/\\f/,\"\")} END{print n}' HRN.txt",
 "description": "Read Horn entry 182 but"
}
```


### [2026-09-05T14:08:52.738Z] TOOL RESULT

```
=== HRN 182 ===
(Men., Bund.); vergl. ai. babhrü- *braun, Ichneumon.
Das np. Wort bezeichnet den *Biber' nicht, es scheint
aber lautlich identisch zu sein. Ob Biber heute in
Fersien vorkommen, ist nach Blanford, Seite 51,
zweifelhaft.
r
W82. but ^Götzenbild; Liebchen.
aw. Büiti- N. pr. ; phlv. Büt, Bütjan (Gemme, Hörn,
Mitteilungen, Heft IV, S. 40, Note).
Wenn die Zusammenstellung richtig ist, so gehört
np. but in dieselbe Kategorie wie gStl^ ätes, petyäre
u. a. m.
188. hiziSk, bijisk (*bishk) 'Arzt* (Sahn. I, 32 Vers 180,
182), bmski (Sahn. I, 25 Vers 43).
aw. baesaza^ 'Arzenei, Arzt'; phlv. bBsazak (PPGl.),
*) Tiger kommen in den kaspischen Provinzen Persiens vor.
=== HRN leaf of 1991 ===
63
```


## [2026-09-05T14:08:53.201Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bum ===\"; grep -n \"bum \\[\\|būm \\[\\|bwm'\" PHD.txt | head\necho \"=== PHD bawēm/būdan ===\"; grep -n \"bawēm\\|bûdan\\|būdan\\|bwtn\" PHD.txt | head\necho \"=== PHD but idol ===\"; grep -n \"idol\" PHD.txt | head",
 "description": "MacKenzie bum, budan, but"
}
```


### [2026-09-05T14:08:53.269Z] TOOL RESULT

```
=== PHD bum ===
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
=== PHD bawēm/būdan ===
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
942:be būdan, ēstādan, h-.
2178:guilty, be — of pēšār būdan.
=== PHD but idol ===
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
2354:idol but, uzdés.
2355:idolater uzdésparist. i
2356:idolatry déw-ésnih / -ézagih, uzdés- paristišnīh.
```


## [2026-09-05T14:09:11.221Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB but/Büiti ===\"; grep -n \"Büiti\\|Buiti\\|but .Götze\\|Götzenbild\" HUB.txt | head -20\necho \"=== HUB 182 ===\"; grep -n \"^182\\.\\|182\\. but\" HUB.txt | head",
 "description": "Hübschmann on but"
}
```


### [2026-09-05T14:09:11.278Z] TOOL RESULT

```
=== HUB but/Büiti ===
=== HUB 182 ===
821:182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
```


## [2026-09-05T14:09:12.907Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT loose ===\"; grep -n \"Bûiti\\|Bûiti-\\|būiti\\|Buiti\" BRT.txt | head\necho \"=== BRT 'Name eines Daeva' ===\"; grep -n -i \"buiti\" BRT.txt | head\necho \"=== SOD bwmh ===\"; grep -n \"bwmh\\|βwmh\\|earth, world\" SOD_pages.txt | head -10",
 "description": "Bartholomae and Sogdian lookups"
}
```


### [2026-09-05T14:09:12.982Z] TOOL RESULT

```
=== BRT loose ===
=== BRT 'Name eines Daeva' ===
=== SOD bwmh ===
12072:     earth, world                                                        TSP 2.1154; BSTBL, Intox. 36; perf. St.
```


## [2026-09-05T14:09:15.737Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '818,845p' HUB.txt; echo \"leaf:\"; awk 'NR<=821{n+=gsub(/\\f/,\"\")} END{print n}' HUB.txt",
 "description": "Read Hübschmann 182"
}
```


## [2026-09-05T14:09:17.114Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12060,12085p' SOD_pages.txt; echo \"---\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F'[' '{print}' | sed -n '1,3p'",
 "description": "Sogdian dictionary bwmh entry"
}
```


### [2026-09-05T14:09:17.470Z] TOOL RESULT

```
Nach Noldeke ist vabr 'Klippdachs* „wohl echt
arabisch**.
*) Also falsoh ftir vavar, vgl. avar oben Nr. 53.- 26 -
182. Np. hut ^Gotzenbild, Idol' (afgh. LW. but) nach Fr.
Miiller = Buddha, nach H o r n ~ zd. buiti 'Name eines
Damons' (vd. 19, 1). Beides schon im grossen Bunde-
hesh, vgl. Darmesteter, le Zend-Avesta II, p. 259.
184. Np. haSa, haSSa Munges, Kind' = phi. vacak (aus
*vaccak = vaUcaK*^) ist zunachst zu trennen von osset;
vdss *Kalb', bal. gvask *Kalb, Kalbchen (Geiger, Lautl.
p. 26), wax. vusk, sar. vi^k *Kalb', die auf iran. "^vasa^
-~ skr. vatsd' *KaIb' (vgl. skr. vatsaka- 'Kalbchen')
zuriickgehen und einem np. *vah' entsprechen wurden
(vgl. maht Tisch' = zd. masya^, skr. matsya-).
187. In bal. gvadil *feige' (aus ^gvaddil = *gvat-dil) ist
dil sicher persisches LW., dagegen wird goat echt sein
= np. badf phi. vat (arm. LW. vat) =■ ap. ^vata-. Da
es aber nur in gvadil vorkommt, nahm ich an, dass
gvadil altes Lehnwort sei -= mp. *vaddil (vgl. paz.
vad schlecht* und dil *Herz').
189. Fiir *avatasti' wiirde ich *ddast, tnr *abitasti- : *awdast,
audast erwarten.
196. Zu barda *Gefangener' = phi. vartak hat schon Geiger
an der von Horn citierten Stelle richtig zd. vareta-
gefangen' gestellt. Dazu afgh. LW. barda *a female
slave.'
199. Np. barman 'Quartier' ist nicht — ap. vardana- *Stadt',
das doch zu np. *balan geworden ware. Zd. verezena-
leaf:
36
```


### [2026-09-05T14:09:19.164Z] TOOL RESULT

```
      salvation                                                     2920 pwrt    B                        ? J*-*-j «& <fjj
        SCE 215
                                                                        swelling ?, dent ?
                                                                        Purt ?
2910 bwq}                                                               SCE 96 n p35; Gersh. IF 1970, 305, <*burti
     Poka ©lsg. fut. inj. =»Pw-
                                                                   2921 pwrt- B                                           d>y
        C2, 69V21
                                                                        Purt, Prt ©Yaghn. vurta ©pt. st.; perf. st.
2911 pwmh     B, S                       ^0y/^j^
                                                                           =5>|3rt-
     pum ©<OP. Jw/wf ©ob. -y(h)                                          0<?)bring, OcObear, (ro)endure
     earth, world                                                        TSP 2.1154; BSTBL, Intox. 36; perf. St.
     VJ 226, 228, 1218; SCE 4.214; TSP; BSTBL, Vim.
        102, Dhu. 142, 293, Dhy. 125 etc.; Frag. Len.
        114.3                                                      2922 *pwrt)rmyk *± pwyt'rmyk
                                                                           ftwrtw6yr-
                                                                   2923 pwrtVmykyKkh)    M                            ^u^
2912 bwn*      C                                      ><c'j>-           Purtarmikya(k)
     Puna      ©f. ob. bwny>, pi. bwnyt   =»Pwn(h),
                                                                         patience
                                                                         GMS   469, 1105; BBB 627, 636; W-Li, ii; Hen.
       celPw  hokh
          l, n> le, cave
                                                                           Talcs. 473; Sogdica. 3; KG 603, 611
       ST SC   28, 46; C2, 11R27, 77R10, 16, 68V 10
---
```


## [2026-09-05T14:09:38.570Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD page tag near 12060 ===\"; awk 'NR<=12072 && /\\[pdf page/ {last=$0; ln=NR} END{print ln\": \"last}' SOD_pages.txt\necho \"=== BQT v1 page tags sample ===\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; grep -c \"\\[pdf page\" BQT_v1_pages.txt",
 "description": "Page tags in SOD and BQT"
}
```


### [2026-09-05T14:09:45.651Z] TOOL RESULT

```
=== SOD page tag near 12060 ===
: 
=== BQT v1 page tags sample ===
0
```


## [2026-09-05T14:09:49.416Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 SOD_pages.txt; echo \"...\"; grep -n \"pdf page\\|page \" SOD_pages.txt | head -5\necho \"=== leaf of line 12072 in SOD_pages ===\"; awk 'NR<=12072{n+=gsub(/\\f/,\"\")} END{print n}' SOD_pages.txt\necho \"=== BQT_v1 head ===\"; head -3 BQT_v1_pages.txt; ls -la BQT_v1_pages.txt BQT_v2_pages.txt",
 "description": "Inspect page-tag conventions"
}
```


### [2026-09-05T14:09:51.088Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English


...
2086:    The English Meaning comprises the next line of           the page and line or paragraph is added. For certain
3221:   See "Remarks" (page xxxv) for the differences in
3267:with an older /z/, by palatalization. Isl also merges               116. On Sogdian vocalic j% see page xxxii.
=== leaf of line 12072 in SOD_pages ===
180
=== BQT_v1 head ===
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
-rw-rw-r-- 1 sfmqrb sfmqrb 2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
```


## [2026-09-05T14:09:57.596Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:234 2>&1 | head -60",
 "description": "Fetch BQT page 234"
}
```


### [2026-09-05T14:10:01.317Z] TOOL RESULT

```
no scan of BQT covers printed page 234 (see 'scans' in refs_online.json)
```


## [2026-09-05T14:10:07.276Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== bwti / بوتی ===\"; grep -n \"بوتی\" BQT_v1_pages.txt | head -10\necho \"=== بتکده ===\"; grep -n \"بتکده\" BQT_v1_pages.txt | head -5\necho \"=== بومهن ===\"; grep -n \"بومهن\\|بومهين\\|بومهين\" BQT_v1_pages.txt | head -5\necho \"=== leaves ===\"; awk 'END{}{n+=gsub(/\\f/,\"\")} END{print \"leaves:\",n}' BQT_v1_pages.txt",
 "description": "Grep Borhan vol 1"
}
```


### [2026-09-05T14:10:08.836Z] TOOL RESULT

```
=== bwti / بوتی ===
25960:۴ -ازچرخ ثاکبوتی واز مرخ نا شتو
=== بتکده ===
=== بومهن ===
21731:ارل بومهن است کمزازله و زمین لرزه باشد. ۷
=== leaves ===
leaves: 776
```


## [2026-09-05T14:10:14.425Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"leaf of 21731:\"; awk 'NR<=21731{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt\nsed -n '21715,21750p' BQT_v1_pages.txt",
 "description": "Context around bumahan in Borhan"
}
```


### [2026-09-05T14:10:16.024Z] TOOL RESULT

```
leaf of 21731:
540
بومادران اسنت که نام
گیاهی باشد عابل به
کمودت و تیزی .
بو ماره بر وزن‌جوباره,نامپر نده‌است
غیر معلوم .
بوم کند باکاف بر وزن سودهند »
خانه‌ای را گوشدکه در زیر زمین کنند بجهت
کوم‌فندان ومسافران .
بومهی ۴ - بفتح ات و ها و سکون
نون, زمین لرزه‌بائد که‌بمربی زلرله خوانند؟ -
۱ - یر ایستا
۵
ورود کوسفندی را ن ز کون دکه از سکن باه
نکرده باشند ۵, ویمعنی اول بسکون نالث حم
آهله است ؛ راين اصح تم
او ههسین ع بر وزن‌خوشه چن. بمعنی
ارل بومهن است کمزازله و زمین لرزه باشد. ۷
ون « بفتح اور و سکون انی و نون.
بمعنی حصه و بپره باشد - و نم اول زهدان
و بچه دان‌که بعربی رحم کویند - وآسمان را
نیز گفته اند - و بن و نهایت و پابان و انتهای
هر چیز باشد ۷ - و رود گوسفند وگاو وامثال
آن کهآ نرا باك لکرده باشند .
بو فلس 4 - ینم اول و انی و سکون‌اك
ودال ابجد » بمعنی آهستگی باشد - و بفتح ثانی
و کسر انی بمعتی باشند - و مرد صاحب‌نخوت
و هدتی را نیز گوبند .
بو فده - بن اول وئانی وسکون‌ثالك
و فتح دال ابجد . مه‌نی هرود هته وربا لگنج
باشد - و بفتح ثانی و کسر ثانی مرد با حستی
و هیبت و ساحب نخون را کویند . ٩‏
لو ۵ » سم ٌم اول و فتح ثانی ۰ درختی‌را
گویند که هر کز بار و ثمر ناورد - و مردم
آهسته را نیز کنته‌اند ۸
۲ص ۳۱ ۰ ۱۷۱ ۰
سنابی غزنوی بدوممتی آورده :
```


## [2026-09-05T14:10:27.063Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"صنم\" BQT_v1_pages.txt | head -20",
 "description": "Search Borhan for sanam (idol)"
}
```


### [2026-09-05T14:10:27.137Z] TOOL RESULT

```
4645:۸5۱26۱6 ۳۵2۵۱ ۲0 :۹۵80162 ,8 ۷۰) عصنممع194-11
4678:2 عطع ۵۶ بومامم۳(۵ 1۳6 ,(.8 با ۵۰) عمصنمما -210
10386:است ۰ وئغ‌بت را کویند وعربان صنم خوانند .
11761:و آموزانده باشد - و داند صنمتی از امور
17455:وهسجوو کافران باش دکه‌بعربی صنم خوانند
19640:و شارسی صنمل دانه خوانند ؟ .
24989:چونکه زرن قدحی در کف حسمین صنمی
27362:یر صنتعا - مراد از شيخ صنمان است
31673:درباچهٌ آرال - که جفرافی نوسان فرون وطی [ نرادر یاچ خوارژم نیز تاصنماند ‏ اعدا داشته
```


## [2026-09-05T14:10:30.907Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"leaf of 10386:\"; awk 'NR<=10386{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt\nsed -n '10375,10400p' BQT_v1_pages.txt\necho \"=== leaf 17455 ===\"; awk 'NR<=17455{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt\nsed -n '17448,17470p' BQT_v1_pages.txt",
 "description": "Borhan bot entry context"
}
```


### [2026-09-05T14:10:32.593Z] TOOL RESULT

```
leaf of 10386:
307
ار تحك « بنتح جم بر وزن اسپرك :
برق برادر رعد را کوشد » و بکسر جیم حم
شظن آمده است . ۶ه
ار نگ » بر وزن فرهتگه » نگارخانة
مانی نقاش باشد - و نام بتخانةٌ چين هم هست -
و کی لت که لا مایت ما من
تقش است ؛ و بضی این لفت دا بجای حرف
ئالك ثای مثلثه آورده اند و کفته اند کهدرافت
فارسی بغیر از اين لفت و لغت ثغ بثای سه نقطه
)۱( چك : بوده .
و غین قطه دار دیگر لفتی بثای سه نقطه نبامده
است ۰ وئغ‌بت را کویند وعربان صنم خوانند .
ار تشدار * - با :حتالی مجهول
وشین فرشت و دال ابجد بر وزن پرهیز کار ؛
لشکری و سیاهی را گونند - ونم رود خاله‌ایست
بسپار بزرکث در حدود قبجاق .
از ث_بانای مثلئه بر وزن ابجد . نام
بیخی است که تخم آنرا فلفل بری و حب‌الفقد
خوانند و بات آنرا پنجنگشت و ذوخمة اوراق
ادج - بفتح اول و سکون الی و جیم
بمشی قدرو قیمت ومرتبه و حد واندازه‌باشد ۷
چه ارجمند صاحب فدر وقیمت و مرتبه را گویشد
و مند بمعتی صاحب و خداوند آمده اه نت
وبمعتی کندن و جدا کردن هم هست - ونامعرغی
است که پرهای او بسیار نرم میباشد و در میان
بالش کنند و بترکی قو ۷ خواند - وک رکدن
=== leaf 17455 ===
453
۱ ر۵ : : افکندن .
پس ازین ماده آهده ؛ صحیح است 0
( برهان فاطع ۳۴ )لت » بفتح اود و سکون ثانی. آهار
جولاهگان را گوینده بمتی ه بردوی کار
مالئد ودر عربی نیز همین‌معنی دارد ۷ - ربمعنی
لیف جولاهکان هم آهفه است- و مرغابی را نز
کویند و معرب آن بط است - و چشم اول‌حعبود
وهسجوو کافران باش دکه‌بعربی صنم خوانند
و کثابه ازممشوق هم هست .
ِا - بختح اول بروزن‌عطا ۰ دوعی ازطمام
باشد که عربان هط و مات گویند» وباین عمنی
با نشدید ثانی هم آمده است - وبکس اول ام
بگذاشتن یمنی بگذار .
زتاده ه بروزن شراره , لیف جولاهگان
و شومالان بائد » وآن جاروب مانندی اس تکه
بدا آش و آهار بر تار مالند .
بتاو اد ه بروزن سزاوار . عافت‌رانجام
و آخر کار باشد .
بتاییدن بکسراول وبای حطی‌بروزن
گرایدن ؛ بمعنی گذاشتن باشه
تخاگ - بنم اول و سکون الی وخای
تقطهرار بالف کشده ویکاف زده » نام موضعیاست
ترديك بکابل .
```


## [2026-09-05T14:10:46.645Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor r in 453 454; do echo \"=====RECORD $r\"; awk -v R=$r 'BEGIN{RS=\"\\f\"} NR==R' BQT_v1_pages.txt | head -60; done",
 "description": "Print Borhan records 453-454"
}
```


### [2026-09-05T14:10:48.828Z] TOOL RESULT

```
=====RECORD 453
سموده
رستم اندر کوههای ۰ و پوست آبرا
جیبه جامه ساخت . خاصیتش آنست که درآتش
سیب درآب غرق شود و هیچ حربه مر آن‌کار
؛ وکویند وقتی‌درزمان الوشیروانآ نجالور
آن جاتور در مبان] نجماعت افتادم‌همه رامجروح
سلخت و کشت و خورد - و دسای منقش رومی‌را
نیز گفته‌اند که هر ساعت برنگی نماید .
یسوده ۱
با سین بی فطه بر وزن .
لیلسی ه بفتح اول و سکون ثانی و ضم
لام و سن بی‌قطهٌ ساکن. ریتی باشد که ازنان
خشك با روغن و دوشاب کنند , و ببای فارسی‌حم
بای - بکس اول, امربایستادن وتوقف
کردن باشد بمنی باست وتوفف کن ۴- وامربه
در نظر‌داشتن هم هست که از پاییدن ۴ باشك .
لیر یش » بکسر اول وسکون ثانی‌ورای
بی‌هطه بتحتانی رسیده وشین نقطه‌دار مفتوح بدال
ابجدزده» یعتی پریثان کند ویر کنده مازد ۴
بعمنی سودن و ساوبدن باشد .
پیسودان ۴ با دال ابجد بروزن دل
سوزان » سعنی لنس و لاهسه باشد یعتی دست‌با
عنوی را بچیز ی کشیدن با بجابی مالیدن .
لیسو دق « بر وزن بسر‌بودن » بمعنی
فیفا - بانین شطه داربروزن طبفا .طوطی
لیگن - بر وژن و معنی بشکن است ٩‏
که امر برافکندن باشد بعنی بیفکن - و کثابه
ازطنام سرباز زدن هم‌هست - و ککی‌راییز گویند
که از غابت سیری نگاه بطمام نکند ۷ .
بیوست کسی افتادن - کنابه از
- در تازی تاه
۱ ر۵ : : افکندن .
پس ازین ماده آهده ؛ صحیح است 0
( برهان فاطع ۳۴ )
=====RECORD 454
لت » بفتح اود و سکون ثانی. آهار
جولاهگان را گوینده بمتی ه بردوی کار
مالئد ودر عربی نیز همین‌معنی دارد ۷ - ربمعنی
لیف جولاهکان هم آهفه است- و مرغابی را نز
کویند و معرب آن بط است - و چشم اول‌حعبود
وهسجوو کافران باش دکه‌بعربی صنم خوانند
و کثابه ازممشوق هم هست .
ِا - بختح اول بروزن‌عطا ۰ دوعی ازطمام
باشد که عربان هط و مات گویند» وباین عمنی
با نشدید ثانی هم آمده است - وبکس اول ام
بگذاشتن یمنی بگذار .
زتاده ه بروزن شراره , لیف جولاهگان
و شومالان بائد » وآن جاروب مانندی اس تکه
بدا آش و آهار بر تار مالند .
بتاو اد ه بروزن سزاوار . عافت‌رانجام
و آخر کار باشد .
بتاییدن بکسراول وبای حطی‌بروزن
گرایدن ؛ بمعنی گذاشتن باشه
تخاگ - بنم اول و سکون الی وخای
تقطهرار بالف کشده ویکاف زده » نام موضعیاست
ترديك بکابل .
بتخال - منم اود و سکون آخ رکهلام
باشد . لمبتخانهٍیست کهآ نرابتخاله بروزن برغاله
هم میکوبند . *
لتر چا - بتتم اول و انی و سکون رای"
که مفعدمردان وفرح زنان باشد - و فرجشماین
داخن و گوشت ث را عم کفته اندکه چرك در آن
جمع میشود ۰
عم « بکر اود و سکون تانی و عن
بض یکویند از عل و بسنی کونند از خرمای
ثر سلژفك -
بت فر یس « بنم اول وکر فاو رای
؟ - باین معنیمعرب
دانته‌اند و تخنین اسح
۵ تاالاظ (بوئیتی
وستی وتیل ووست نظیربوئیتی
کی مرد بدئلم اوخیربد
که‌بتضانهراهیچ نگذاشتی
دکی روزشبگیر سوداپهرفت
فرسنش(سیاوش‌را)" بسوی‌شبسنان‌خوش
زدوده دل ومفز و جاش ز بد
نف در برده او داشتی ۱
1 9۳4
بر شاه ابران خرامید تفت .
بر خواهران وففستان‌خوش ۳ ۳
```


## [2026-09-05T14:11:04.346Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor r in 443 444; do echo \"=====REC $r\"; awk -v R=$r 'BEGIN{RS=\"\\f\"} NR==R' BQT_v1_pages.txt | head -45; done",
 "description": "Borhan records 443-444 (p.223)"
}
```


### [2026-09-05T14:11:06.121Z] TOOL RESULT

```
=====REC 443
باشت با نی فرشت بر وزن چاشت »
چوب زر کی‌را گون که سقف‌شها نهرا بدان‌پوشتف .
باشتبن بروزن آستین» باری ومیوه‌ای
را گویند که از مبان درخت برآید بی آنکه کل
کند و بهار دهد - و تلم بلو کیست ازسبزوار .
باشگی فه » بروزن,ممنی باز کوداست
که بعربی عکس و قلب خواند ۱
باشنگ . بروز نآهنگه » خوش؛ٌانگور
آووز ب ۳ درخت از کویتد زر و و خ شا نکوز
۱۳۲۵۵۹۵۱0 27 ۱
باشو . بروزن‌ساو » چلیاسهرا گو بند
باشو هه - بنتح میم , ی
باخه ری وش شاه زاف نس
و حعرب آن باشقق است
وکنابه از تسر طایر ونر وافع همست ,رآنها
دو صورت اند از حملهٌ صور چهل و هشت کانةً
فلك .
باس ۰ بکر ءایحطی وسکون سین
بی نقطه » ببونانی عیوه ایب تکه آنرا توت سه
کل خوانند و بمربی ثمرةالعلیق گوبند و درخت
]راس هکل نامند . اکر ب رکه و بارآ نرا با هم
بحوشانند خمابی باشد جهت موی رش 7
و امثاد اف
پاعودا » باعين بی نقطه پواو رسیده
و رای بی‌تقطه بالف کشیده . نامپدر پلعم است که
علیه‌السلام و عافبت ایمان برباد داد و اورا بلعام
یز میگفته‌اند .
گوند ۴ ۳ و کتابه‌از ۱3 ۹
باغ بدیع اشاره‌به بپشت استکهخلد
پرین باشد .
باغچ پقتح ثالث وسکون جیم‌فارسی .
ااگور نیم بخته را گوشد ۰
باغ دفیي ه بنج رای قرشت » بمعنی
باغ بدیم است ک هکنابه از بهشت عنبر سرشث
باشد . ۱
باغر ۵ « بسکون ثالكث وفتح رای‌فرشت.
در 6۷ ۲۷۳ را گونن که دراعضا پیب آزارودردمندی
دیگر بهمرسد مثل آنکه از پای کسی دنبلی بر
آمده باشد بمب آن در کش ران کرهها بیدا
شوده _باسر بربالین بدنهادهباشد. بدان‌سبب در گردن
کرهها بهمرسد ؛ وبسی گویشد زحمتی اس تکه
بسبب ژحمت دیگر پیدا شود , و عال هر دو
سکست :
۳
؟ ‏ همرة باز [ رك : باز .]» در
=====REC 444
تسف ی
باغ‌ز اغان - نم بافیت از باغ
ای رات
باع‌ستخا ع کنایه از دنیا باشد -
و کنابه از هردم صاحی‌همت و-خاوت‌هم تا
باع سیاو شان نام صوئی است
از موسیقی .
باع شیر ین - نام نوایست ازموسیفی»
و ام لحن چهارم باشد ازسی لحن باربك .
باع قدس ه بضم قاف ؛ اشاره به
هشت است .
باغل- بروزن بابل .جای کاو و گوسفند
و امثال آن باشد هو
باغنج س بفتح الث بروزن نارنج ؛انگور
نیم‌زی دا گویند 0
باغنكه ‏ بررزن بافنده » پنبةٌ حلاجی
کردهرا گویند که بجهت رشتن گلوله کرده‌باشند ۰
باع‌و سیع « کنابه‌از جنةالمأوی است
پاغوش ه بر رزن آغوش . چیزی را
با ب‌فروبر‌دن باشد - و بمعنی سرباب فرویردن
و خوطه خوردن هم هست ۰
ومیم 3 فاقات اند 0 را گویند
و بضم دال حم توت ات ؟ ۰
۱ ۲
نهای «بونکر 4۹ و بافدم م رکب |
کرده است
۳ خویشئن از ره راست کم
مخفف : بافت کار . ۴
بافکار ۴
را کوند  .‏
باقلی ۴ - و و ی
ساکن » ممروف است ۱
و آن غله‌ای باشد که
در آشها کنند و بعربی
باقلا گویند بتشدید لام
بالف کشیده . اک ر کل
۳ در هاون ارزیز
بکویند ور آفتاب نهند
وبدان‌خناب کنند موی‌رابغات
س بروزن آ شکار. بافندموجولاهه
هالك « بروزن خاك . اندیشه و تری‌ویم
باشد .- وبیعثی التفات‌نمودن - و ازپس‌نگرستن
بائد - و ترجمةٌ نوع هم هست .
با گر ه » بسکون کاف فارسی » بر وزن
و معنی باغره است بعنی زحمتی که در اعضای
```


## [2026-09-05T14:11:19.802Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=====REC 331 (p~111)\"; awk 'BEGIN{RS=\"\\f\"} NR==331' BQT_v1_pages.txt | head -40\necho \"=====REC 535 (p~314)\"; awk 'BEGIN{RS=\"\\f\"} NR==535' BQT_v1_pages.txt | head -40",
 "description": "Borhan pages 111 and 314"
}
```


### [2026-09-05T14:11:21.358Z] TOOL RESULT

```
=====REC 331 (p~111)
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
کلها و رباحین باشد مطلقا - و ریحانی را نیز
گون که آنراشاه اسپرم خوانند - و. بمعلی‌سبزه
ليز آمده است و یتح اول وسکون قین سم
کفته‌اند ‏
ایسبر اه باکان فارسی پروزن بهتركه
سوازه ۲ فاب ۱ : ۲۲۵ .
1 ۷ *. + اساهید ‏ رك
1
=====REC 535 (p~314)
۱ 2۳9
شبیه‌به ثیهولیک نکوچکتر ازاوست" وا نرا بعربی
سلوی خوانند .
بو ر نم اول و انی مجهول ر رای
قرشت هردو ماکن» اسب سرخ ونك را گویند ۴
بودش
‌
بودص - بکر دال ابجد بروزن
سوزش » بیعتی هستی و بود باشد و بعربی کون
خوانند ۱ . #
و ذ نه - تجح دال وئون : درنده است
که‌آنر! نیپومیگوبند. ریسضی کوبند پرنده‌اٍیست
۱ - معنولا اسم مصتر در فارسی آزريشة فعل (< دوم شخص مفرد از امر) ب؛ «ش »
ت کیب شود رلی بودش ازسوم شخص مقرد ماضي و« ش » تر کیب بافته برخلاف قیاس » و ناصر
. خسرو آنر | تن . رل : زادالمسافرین ۳۹4: ۰۱ ۳ 98۲ روباه» اسب؛ سرخ فهوه‌بی:
سانسکریت ۵۵11۲۷1 ( سرخ فهوه‌بی, فهومبی ) < اسفا ۱ : ۲ ص 4٩‏ * اوستا 02۷۲۵ اساسا
بممنی سرخ ( در نداول عوام بور شدن ؛ بعنی سرخ وخجل شدن) است که سیی بجانوری که در
فارسی ببر ( بدو فتح ) کویند اطلاق شده ( ۵ ۰م )» پهلوی تلا < بندهش ۱۲۱ و ۲۲۹ ۰
«بوستی. بندهش ۰۹۰۶ ؛ طبری 0۷1۲ ( زرد ) « واژه نامه ۱۵۴ > دزفولی 5102۲ - ناه را
یُمعنی ۶ لر » بکار برند چه لرهای خوزستان سوار اسب‌بور شوند .
۵ بودن - بغنعم سوم » چهلوی 00488 «منای ۰۶۲۷۰ 00127] داونوالا ۳۸۳»؛ ازريعة
آزبایی ۵2۷ , ۵۱08 (بهمن معنی) «نب یکت 4۱ اوستا 02۷۵141 , سانسکربت ۷2 قتا
(سوم شخص) . لانینی ۱20۳260]» اسلاو 1396 (مسدر) «۲براهامیان» وركك : فپرست اسقا ۱ : ۳؛
استن . وجود داشتن» هستی داشتن- وجود, هستی . ۱
یقه ازصفحهٌ ۳۱۳
72 , مادر وی مایا دوی[06۷ - 1۷1812 نام داشت . سوددنه راجه بود
وبرقببلهُسا کیا درکاینله وستولاا25 12۳112-۷ ( جنوب غربی نبار ۱۷6021 در هند شمالی )
حکومت میکرد " و مادر بودا نیز دختر راجه ۳۲20۵0412 - لاگ بود وبتابراین بودا اطبة
2 ( نجبا ر امرا)است واو در حدود سال ۵۹۶ ق.م ( بقول وبلیامز حدود ۵*۰ ق .م)
متولد شد . وی موسی آین بودایی احت و این آبن مبتنی است بر اشکه : حات رتج است
و رنج از هوی زاید و تركك فس تنها وسیلهٌ رهایی ازهوی وه‌وی‌است . کمالمطلوب بودابی عبارت
است ازوصول به 3۳۷۵7۵[ بافنای کل .
د رگد بودا در هشتاد 7 انفاق اقتاد . امروزه در حدور ۰۰۰۰۰۰۰۰ تن در حسّد
وبیرمانی وسراندیب وتبت‌وچین وژاپن پیرو آین بودابی هسند. رك: فرهنك سانسکرت‌بانگلسی.
مونبه وبلیامز ص ۷۳۳ سنون ۲ ؛
ماع :۲۵۲۱5۵ فلت مظ بل ۱۷۸6 ما ,4نافاا6 ۷5۸76(
: 1942 - ۱94۱ هاانهاج) ۰ ۷۵۱6 2 بتصکنطان9۵ عناعده۳۵( ۲۱۲ق۴ , 0۵16([
۰ 7 ۲۵۵۵008 مر 1 ,۷۵۱ رک5اظ0 ۳.6.۱۷۵۵
و رك : بد و پوداسپ. ۱
بوداسب» 4و اسب - مسلمانان نام بوداسب ور سوسس اساطیری مذهسی صایه اطلاق
```


## [2026-09-05T14:11:58.655Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T14:11:58.663Z] TOOL RESULT

```


```


## [2026-09-05T14:12:02.767Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%AA",
 "prompt": "Give the full Persian etymology section for بت (bot) \"idol\": what is it derived from (Middle Persian, Sogdian, Sanskrit buddha, or Avestan Būiti?), and any cited sources. Quote exactly."
}
```


## [2026-09-05T14:12:03.769Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pagoda",
 "prompt": "Quote the full etymology of \"pagoda\" verbatim, including the Portuguese, Persian butkada and Sanskrit bhagavati proposals."
}
```


### [2026-09-05T14:12:09.382Z] TOOL RESULT

```
# Persian Etymology for بت (but/bot) "idol"

## Derivation

The word is **inherited from Middle Persian** and ultimately traces to **Sanskrit**.

## Exact Sources

According to the Wiktionary entry:

> "Inherited from Middle Persian [Book Pahlavi needed] (bwt' /⁠but⁠/, "Buddha, idol"), ultimately from Sanskrit बुद्ध (buddha)."

The entry also notes it is a "Doublet of بد (bud / bod, 'Buddha')."

## Key Points

- **Middle Persian origin**: The phonetic form was *bwt'* pronounced /but/
- **Ultimate source**: Sanskrit *buddha*
- **Semantic evolution**: The word extended from its original meaning (Buddha, idol) to include "beautiful person; the beloved" in Classical Persian

No Sogdian or Avestan etymologies are cited in this source material.
```


### [2026-09-05T14:12:10.968Z] TOOL RESULT

```
# Etymology of "Pagoda"

Here's the full etymology from the source:

"1580s, in Burma, India, Siam, China, etc., 'a sacred tower, richly adorned,' pagode, pagody (modern form from 1630s), from Portuguese pagode (early 16c.), perhaps from a corruption of Persian butkada, from but 'idol' + kada 'dwelling.' Or perhaps from or influenced by Tamil pagavadi 'house belonging to a deity,' from Sanskrit bhagavati 'goddess,' fem. of bhagavat 'blessed, adorable,' from *bhagah 'good fortune,' from PIE root *bhag- 'to share out, apportion; to get a share.'"

The entry presents three possible origins: the Portuguese term (possibly derived from Persian), or alternatively a Tamil/Sanskrit lineage. The Persian route traces through *butkada* (idol-dwelling), while the Sanskrit path connects to *bhagavati* (goddess) and ultimately the Proto-Indo-European root meaning to distribute or allot.
```


## [2026-09-05T14:12:15.919Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-",
 "prompt": "Give the reconstructed root, its meaning, and the list of derived terms/descendants (Indo-Iranian, Greek, Latin, Germanic). Quote the headline gloss exactly."
}
```


## [2026-09-05T14:12:17.523Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85",
 "prompt": "Give the Persian etymology sections for بوم: the one meaning \"land, earth, country\" (from Middle Persian bwm, Old Persian būmi-, Avestan) and any other homonyms. Quote exactly."
}
```


### [2026-09-05T14:12:21.442Z] TOOL RESULT

```
# Proto-Indo-European Root *bʰuH-

**Reconstructed Root:** *bʰuH- (perfective)

**Meaning:** "to be, become, grow, appear"

**Major Descendant Language Groups:**

**Indo-Iranian:**
- Sanskrit: भवति (bhávati)
- Persian: بودن (budan)
- Avestan: 𐬠𐬀𐬎𐬎𐬀𐬌𐬙𐬌 (bauuaiti)

**Greek (Hellenic):**
- Ancient Greek: φύσις (phúsis), φυτόν (phutón), φῦλον (phûlon)

**Latin (Italic):**
- probus, superbus, tribus

**Germanic:**
- Proto-Germanic: *beuną, *būrą

**Additional Key Derivatives:** Albanian botë, Lithuanian bùtas, Old Prussian būton, and various Slavic forms through Proto-Slavic *byti.
```


### [2026-09-05T14:12:23.214Z] TOOL RESULT

```
# Persian Etymology Sections for بوم

## Etymology 1 (Land/Earth/Country)

"From Middle Persian 𐭡𐭥𐭬 (būm), from Old Persian 𐏏 (būmiš), from Proto-Iranian *búHmiš, from Proto-Indo-Iranian *bʰúHmiš"

This meaning encompasses "land, soil, earth; field, terrain; country, realm, region; environment, habitat."

## Etymology 2 (Owl)

"Borrowed from Arabic بُوم (būm)."

## Etymology 3 (Colloquial)

No classical source etymology is provided. This entry notes it is "Spoken form of بام (bâm)" and is marked as colloquial.

The first meaning directly traces back to Middle Persian and Old Persian origins, while the second represents a borrowing from Arabic. The third is a modern colloquial variant without etymological attestation.
```


## [2026-09-05T14:12:35.808Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD bheua ===\"; grep -n -i \"bheu\\|bhcu\" AHD_watkins1985.txt | head -20\necho \"=== AHD 'to be, exist, grow' ===\"; grep -n \"to be, exist, grow\" AHD_watkins1985.txt | head",
 "description": "AHD Watkins bheu root"
}
```


### [2026-09-05T14:12:35.885Z] TOOL RESULT

```
=== AHD bheua ===
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
321:yawn, gape: BAY2, BEVEL; ABASH, ABEYANCE. 2. Possibly Vulgar Latin *abbaidre (> Old French (a)baiier), to bay: BAY‘*.] [battuere. To beat. Latin verb of unknown origin. (BATE?), BATTER!, (BATTER’), (BATTERY), BATTLE; ABATE, COMBAT, DEBATE, (RABBET), (REBATE?), (RE- BATO).] bel-. Strong. 1. Suffixed o-grade form *bol-iyo- in Russian bol’shoi, large: BOLSHEVIK. 2. Prefixed form *dé-bel-i- (dé-, privative prefix; see de-), “without strength,” in Latin débilis, weak: DEBILITATE, DEBILITY. [Pok. 2. bel- 96.] bend-. Protruding point. 1. Germanic *pannja-, “struc- ture of stakes,” in Old English penn, pen for cattle: PEN2. 2. Germanic *pund- possibly in Old English pund- (> Middle English pound), pundfald, enclosure for stray animals: POND, POUND3; IMPOUND, PINFOLD. 3. Germanic *pin- in Old English pintel, penis: PINTLE. [Pok. bend- 96.) beu-'. Also bheu-. Appears in words loosely associated with the notion “to swell.” I. Root form *beu-. 1. Ger- manic *puk- in: a. Old English pocc, pustule: POCK; b. Old French po(u)che and Old North French poke, bag: POACH!, POCKET, POKE3, POUCH, (PUCKER). 2. Old Eng- lish pyffan, to blow out: puFF. 3. Old English -piite, “fish with large head” (in aele-piite, eelpout): pouT?. II. Root form *bheu- with various Germanic derivatives. 1. Old English bdsm, bosom: Bosom. 2. Old English biic, belly, pitcher: BUCKBOARD. 3. Frankish *biak (> Old French buc), trunk of the body: TREBUCHET. 4. Old English bye), pustule: BorL?. 5. German dialectal baustern, to swell, akin to the source of Middle English bost, a bragging: BoasT!. III. Root form *beu-. 1. Latin bulla, bubble, round object, amulet (> Old French boule and Spanish bola, ball): BILL!, BILLET!, BOLA, BOULE?, BOWL’, (BULL?2), BULLA, BULLATE, BULLET, (BULLETIN); BOULE- VERSEMENT. 2. Latin bullire (> French bouiller), to bubble, boil: BOIL!, BOUILLON, BUDGE!, (BULLION), BULLY?; BOUILLABAISSE, EBULLIENCE, GARBOIL, PAR- BOIL. 3. Possibly Latin bucca (> Old French boucle, buckle, curl, and Spanish boca, mouth), (inflated) cheek: BOCACCIO, BOUCLE, BUCCAL, BUCKLE!, BUCKLE?; DE- BOUCH, DISEMBOGUE, EMBOUCHURE. 4. Greek boubén, groin, swollen gland: BUBO. [Pok. 2. beu- 98.] beu-2. Root imitative of muffled sounds. 1. Latin bitié (perhaps > Old French butor), bittern: BITTERN!. 2. Latin bited, a kind of hawk: BUZZARD. [Pok. 1. b(e)u- 97.] bha-'. To shine. Contracted from *bhas-. 1. Germanic *baukna-, beacon, signal, in: a. Old English béac(e)n, beacon: BEACON; b. Old English denominative bécnan, biecnan, to make a sign, beckon: BECKON. 2. Perhaps Germanic *bazja-, berry (< “bright-colored fruit”), in Old English berie, berige, berry: BERRY. 3. Germanic *bandwa-, “identifying sign,” banner, standard, sash, also “company united under a (particular) banner,” in: a. Spanish banda, sash: BANDOLEER; b. Late Latin ban- dum, banner, standard: BANNER, (BANNERET). 4. Suf- fixed form *bhaw-es- in Greek phds (stem phét-), light: PHOS-, PHOT, PHOTO-; PHOSPHORUS. 5. Extended and suffixed form *bhan-yo- in Greek phainein, “to bring to light,” cause to appear, show, and phainesthai (passive), “to be brought to light,” appear: FANTASY, (PANT), PHANTASM, (PHANTOM), PHASE, PHENO-, PHENOMENON; DIAPHANOUS, EMPHASIS, EPIPHANY, HIEROPHANT, PHAN- EROGAM, (PHANTASMAGORIA), PHOSPHENE, SYCOPHANT, THEOPHANY, (TIFFANY). [Pok. 1 bha@- 104.] bha-2. To speak. Contracted from *bhaa-. 1. Latin fari, to speak: FATE; AFFABLE, (FANTOCCINI), INEFFABLE, IN- FANT, (INFANTRY), PREFACE. 2. Greek phanai, to speak: -PHASIA; PROPHET. 3. Suffixed form in Germanic *ban- wan, *bannan, to speak publicly (used of particular kinds of proclamation in feudal or prefeudal custom; “to proclaim under penalty, summon to the levy, declare
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
351:[busk-. A bush. Germanic root, possibly connected with the root bheue-. 1. Old French bosc, forest: BOSCAGE, BOUQUET. 2. Old French bois, wood: HAUTBOY, (OBOE). 3. Italian busco, splinter: BUSK!. 4. Latin buscus, forest: (AMBUSCADE), AMBUSH.]
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
434:el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.]
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
1105:uper. Over. 1. Extended form *uperi in Germanic *uberi in: a. Old English ofer, over: OVER; b. Middle Dutch over, over: ORLOP. 2. Variant form *(sjuper in: a. Latin super, super-, above, over: SOUBRETTE, SOVEREIGN, SUPER-, SUPERABLE, SUPERIOR, SUPREME, (SUPREMO), SUR-; SIRLOIN; b. suffixed form *(s)uper-no- in Latin supernus, above, upper, top: SUPERNAL,; C. suffixed form *super-bhw-o-, “being above” (*bhw-o-, being; see bheue-), in Latin superbus, superior, excellent, arrogant: SUPERB; d. suffixed (superlative) reduced form *sup-mo- in Latin summus, highest, topmost: SUM, SUMMIT; @. var- iant form *(s)juprd in Latin supra, above, beyond: (so- PRANINO), SOPRANO, SUPRA-; SOMERSAULT. 3. Basic form *uper in Greek huper, over: HYPER-. [Pok. uper 1105.]
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1279:BAYy3 badyo- BAY‘ bat- BAYADERE gWele-1 BE bheue-
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1296:BID bheudh-, ghedh- BIDE bheidh- BIDENTATE dent- BIDONVILLE weik-1 BIENNIUM at-
1297:BIER bher-1 BIFORATE bher-2 BIGEMINAL yem- BIGHT bheug-3
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1310:BOG bheug-3 BOIL! beu-!
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
=== AHD 'to be, exist, grow' ===
```


## [2026-09-05T14:12:37.188Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN 1503 leaf = 1503? SYN leaf=printed+24 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==1528' SYN.txt | head -30\necho \"=== total leaves SYN ===\"; awk '{n+=gsub(/\\f/,\"\")} END{print n}' SYN.txt",
 "description": "Buck SYN page 1503"
}
```


### [2026-09-05T14:12:38.880Z] TOOL RESULT

```
=== SYN 1503 leaf = 1503? SYN leaf=printed+24 ===
udicial courts, not necessary). It was the most general word for ‘court’ (as still in Eng-
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
lish) until the introduction of tribunal, after which it was used mainly of special higher courts. REW 2032. Wartburg 3.851 f. NED s.v. court.
It. tribunale, etc., fr. Lat. tribunal ‘the raised platform on which seats of magis- trates were placed’ (: tribinus ‘tribune’, orig. ‘magistrate of the tribe, tribus’).
3. Ir. airecht, orig. ‘assembly of nobles’, fr. aire ‘noble’ (19.36).
NIr. cwirt, fr. ME, NE court.
W. llys, Br. lez, orig. ‘castle, court’ (of a noble) : Ir. liss, less ‘fortified place’ (further etym. dub.; Stokes 247, Walde- P. 2.99), judicial sense doubtless after French and English.
4. ON, OE ping, OHG ding, etc., in the older period the most general word for the popular assembly both for legisla- tive and judicial purposes (cf. Norges Gamle Love 5.737 ff.; Liebermann, Ge- setze der Angelsachsen 2.222, 449 f.) : Goth. Jeths ‘time’ (14.11), with develop- ment through ‘appointed time’. Walde- P. 1.724 f. Falk-Torp 1268. Feist 494.
ON dodmr ‘judgment’ (21.17), also ‘court’. So rarely OE dom. Lieber- mann, op. cit. 2, 2.54. Bosworth-Toller Suppl. s.v.
ON logrétta (‘legislature’ and ‘court’), epd. of log ‘law’ and -rétta : rétta ‘straighten, adjust, raise’, rétir ‘law’, etc. (21.11). On history of its uses, cf. Vigfusson 405, and Heusler, Das Straf- recht der Islindersagas, p. 24.
OE riht, MHG reht, Dan. ret, Sw. rdtt ‘law’ (21.11), used also for ‘court of
LAW
Digitized by Arya Samaj Foundation Chennai and eGangotri
1427
law’. Hence collectives OHG girihti, MHG (ge)rihte, NHG gericht, and epds. Du. rechtbank, gerechtshof (both orig. the place, like NHG gerichtshof, but ex- tended to the body).
OE gemot, ME imét, mot, mote, NE (obs.) moot, the most general word for assembly (: ON mt ‘meeting, assembly’, Goth. gamdtan ‘have room’, etc.) and for the judicial assembly more usual than the general Gme. ping (cf. Liebermann, op. cit. 2.94, 449), also OE mét in epds., folc-mat, etc. NED s.v. moot, sb.'.
OE mepel, OHG mahal, also general ‘assembly’ and ‘discourse’ : Goth. mapl ‘meeting place, market’, ON mal ‘speech, lawsuit, case’, Gmc. *mapia-, prob. fr. the same root as OK gemét, etc. (above). From the Gme., MLat. mal- lum, mallus ‘court’. Walde-P. 2.304. Falk-Torp 685 f. Feist 349 f.
5. Lith. tetsmas (meolog. for sudas), Lett. tiesa ‘truth’ (as Lith. tiesa), ‘right’, but esp. ‘court’? (Mihl.-Endz. 4.212) : Lith. teisé ‘law’ (21.11), teisus ‘right’ (16.73), tiesus ‘straight’ (12.73), etc.
Lith. sudas, loanword fr. Slavic (be- low, 6). Brickner, Sl. Fremdworter 139.
6. SCr., Russ. sud, Boh. soud, Pol. sqd = ChSI. sqdi ‘judgment’ (21.18).
7. Skt. adhikarana- (in many senses, but i
=== total leaves SYN ===
1544
```


## [2026-09-05T14:12:57.640Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD index TRIBE/HERB/ARBOR/HUSBAND ===\"; grep -o \"TRIBE [a-z()ë-]*\\|TRIBUNE [a-z()ë-]*\\|CONTRIBUTE [a-z()ë-]*\\|HERB [a-z()ë-]*\\|ARBOR [a-z()ë-]*\\|HUSBAND [a-z()ë-]*\\|BEAM [a-z()ë-]*\\|BOOM. [a-z()ë-]*\\|PHYSIC [a-z()ë-]*\\|FUTURE [a-z()ë-]*\\|PROVE [a-z()ë-]*\\|SUPERB [a-z()ë-]*\\|BUILD [a-z()ë-]*\" AHD_watkins1985.txt | sort -u | head -40",
 "description": "AHD index lookups"
}
```


### [2026-09-05T14:12:57.698Z] TOOL RESULT

```
=== AHD index TRIBE/HERB/ARBOR/HUSBAND ===
ARBOR koro-
BEAM bheue-
BEAM ker-
BOOM? bheue-
BUILD bheue-
FUTURE bheue-
HERB 
HUSBAND bheue-
PHYSIC bheue-
PROVE es-
PROVE per
SUPERB uper
TRIBE tere-
```


## [2026-09-05T14:12:59.325Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN bhuta ===\"; grep -n \"bhūta\\|bhuta-\\|bhūta-\" SYN.txt | head\necho \"=== SYN index leaf check 1527-1529 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=1526 && NR<=1530 {print \"--LEAF\",NR; print substr($0,1,400)}' SYN.txt",
 "description": "Buck lookups"
}
```


### [2026-09-05T14:13:00.708Z] TOOL RESULT

```
=== SYN bhuta ===
=== SYN index leaf check 1527-1529 ===
--LEAF 1526
sultus ‘experienced, skilled’ (also used
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Bei)
——
Digitized by Arya Samaj Foundation Chennai and eGangotri
LAW 1425
alone in legal sense), pple. of cdnsulere ‘reflect, take counsel’.
Lat. advocatus, pple. of advocare ‘call, summon’, hence ‘one called’ (to assist), esp. in legal matters, and in imperial times ‘lawyer�
--LEAF 1527
someone’. Kluge-G. 474.
NHG rechtsanwalt and (like U.S. at- torney) also simply anwalt = MHG an- walte ‘deputy, agent’ : walten ‘have pow- er, rule’.
5. Lith. advocatas, Lett. advocats, see above, 2.
6. ChSl. zakonintki (renders voptxés, for which see above, 1), fr. zakont ‘law’ (21.12).
SCr. pravnik, Boh. prdvntk, Pol.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
aie
--LEAF 1528
udicial courts, not necessary). It was the most general word for ‘court’ (as still in Eng-
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
lish) until the introduction of tribunal, after which it was used mainly of special higher courts. REW 2032. Wartburg 3.851 f. NED s.v. court.
It. tribunale, etc., fr. Lat. tribunal ‘the raised platform on which seats of magis- trates were pl
--LEAF 1529
ncluding ‘court’, for which also esp. dharmadhikarana, cpd. with dharma- law’), fr. adhi-kr- ‘place at the head, ap- point’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1428 SELECTED INDO-EUROPEAN SYNONYMS
21.16 JUDGE (vb.)
Grk.  Stxatw, xptrw : Goth. ddmjan, stdjan Lith. _teistz, spresti NG btxdtw, xplyw ON dema Le
--LEAF 1530
�divide’ : teil, etc. ‘part’ (18.23). Kluge-G. 646. Franck- v. W. 477.
OHG-NHG rihten, richten, fr. reht, recht, ‘law’ (21.11).
OHG suonen (NHG siihnen ‘expiate,
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
LAW
atone’), fr. suona ‘judgment, court, atonement’ (21.17).
5. Lith. testi (neolog. for sudyti) : teisus ‘right’ (16.73), teisé ‘law’ (21.11).
Lett
```


## [2026-09-05T14:13:20.735Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"HERB[A-Z]* [a-zë()-]*\" AHD_watkins1985.txt | sort -u | head\necho \"---TRIBE/TRIBUNE index---\"; grep -o \"TRIB[A-Z]* [a-zë()-]*\" AHD_watkins1985.txt | sort -u | head\necho \"--- tere- entry ---\"; grep -n \"^tere-\\|tere-\\?\\. \" AHD_watkins1985.txt | head -5\necho \"--- treb / trei ---\"; grep -o \"TRIBE [a-z-]*\" AHD_watkins1985.txt | head",
 "description": "AHD index for HERB and TRIBE"
}
```


### [2026-09-05T14:13:20.838Z] TOOL RESULT

```
HERB 
---TRIBE/TRIBUNE index---
TRIBE tere-
TRIBOELECTRICITY tera-
TRIBOLOGY tera-
TRIBRACH mregh-u-
TRIBULATION tera-
--- tere- entry ---
1018:ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
--- treb / trei ---
TRIBE tere-
```


## [2026-09-05T14:13:26.998Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"trei-\\. Three[^]]*\" AHD_watkins1985.txt | head -c 2000\necho; echo \"=== herba ===\"; grep -o \"herba[a-z, ]*\" AHD_watkins1985.txt | sort -u | head",
 "description": "AHD trei- entry and herba"
}
```


### [2026-09-05T14:13:27.081Z] TOOL RESULT

```
trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.

=== herba ===
herban, a summoning to military service
```


## [2026-09-05T14:13:56.594Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"KNT leaf of 5743:\"; awk 'NR<=5743{n+=gsub(/\\f/,\"\")} END{print n}' KNT.txt\necho \"KNT leaf of 5741:\"; awk 'NR<=5741{n+=gsub(/\\f/,\"\")} END{print n}' KNT.txt\necho \"=== BRT urvara ===\"; grep -n \"urvarā\\|urvara-\\|Pflanze\" BRT.txt | head -8",
 "description": "Kent leaf and Bartholomae urvara"
}
```


## [2026-09-05T14:13:57.587Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tribe",
 "prompt": "Quote the full etymology of \"tribe\" verbatim, including any tri- + bhu- analysis and de Vaan/uncertainty notes."
}
```


### [2026-09-05T14:13:58.195Z] TOOL RESULT

```
KNT leaf of 5743:
224
KNT leaf of 5741:
224
=== BRT urvara ===
4009:'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4778:;von  Arn.  geschützten  Pflanzen",  in  Dual- verbindung mit  haurvatat-  (sva.  Wasser): 3^ar3%3m  myasdam  haurvatä  °r)tata  gäus huha  haomitnca para.haomamid Y.8.i;j.i, 4.1,  6.1T,  7.26.
4917:*)  Ursprünglich  des  Fesis  der  Heimkehr  von Hirt  und  Herden  aus  der  Senne  (s.  u.).   Später ist    es    dem   Andenken    an   die  SchaiTung   der Pflanzen  geweiht   Der  letite  (30,)  Tag  fällt  auf den  30.  des  7.  Monats,    d.  i.  in  alter  Zeit  auf den  3.  Okiober,  heutzutage  auf  Mitte  ApriL    S. im  übrigen  unter  yüirya-  und  miuiySisaiH: Ableit.  aas  'a-yä%ra.  n.  (iura  V.  yä-)  'Heim- kehr',  als   Adj.  ftlso  'was  mit  der  Heimkehr in  Beziehung  steht';  s.  Roth  ZDMG.  J4.  704. j.  ayiri.dräjS  N.  43:  lies  ayari.dr',
5095:•  g.  ava-pastöiä  In£  'hinabzufallen':  kasnä d>r»tä  samcü  ads  nabasSä  avap°  kl  aps urvarasca  "wer  wahrte  die  Erde  unten und  den  Luftraum,  dass  sie  nicht  hinab- iielen,  wer  Wasser  und  Pflanzen?"  Y.  44. 4'"
7131:—  y5  "tr^iii  uruzdipäk»tn  däitlm  gätUm avi  avaiaraiti  V.S.Sz;  83—96'*;  —  näi/ faahö  ahmst  ^ad^mm  vtr^nyäti  yaaöit Ptti:rahe  .  .  nasQm  pacät  paiti  '^re  üAfm baräiY.iO.iT; — yd  naiäum  matgü^qm ..'tr^m  ,'l../rabarinH\.y.2^.  a)neben| Wasser,  Rind,  Pflanzen,  Barssman  usw.:' para  asmgm  .  .  äpim  .  .  zqm  .  .  gqm  .  . urrarq/n  . . 'trwi  Y.ig.2;  —  iulia  "tnm , .  .  äpfm  .  .  zqm  .  .  gqm  .  ,  urvarqm  . . yaaidainni  V.ii.j;  3,  $,  9,  10,^.33,  42;
7193:•  j.  ■ätr«.ä«Ta-  Adj.  (fem.  =rJ-)  'ignis '  "^s'-  '"""»''"•'  "'"^■''«'■■'-  -  ■>  So  V.  r8. seraen  continens,  worin  das  Feuer  seine,«  J-  ätt.r»'p5ta-  m.  EN.  eines  Gläubigen: Nahrung  findet",   von  Pflanzen:   aSsma  .  ..'i>'^'  '^^'"""'^  Yt.7?.io2.
8182:•  j,  uxsyat-urvarä-  Adj.  (mask.  •ra-')  'bei dem,  durch  den  die  Pflanzen  wachsen': salavalsS  .  .  "rö  Yt.  /^-44;  43;  —  mC^nrn .  .  °r?m  Yt.io.6i;  —  xh'iua  äzüitt  .  . tacat.,ipa  'ra  (ADm.)  Y./6.8.
```


### [2026-09-05T14:14:02.832Z] TOOL RESULT

```
# Etymology of "Tribe"

According to the Online Etymology Dictionary, the word "tribe" originated in the mid-13th century from Old French *tribu* or Latin *tribus*, meaning "one of the three political/ethnic divisions of the original Roman state."

The source notes: "The first element generally is held to be *tri-* 'three,' and the whole to represent a PIE indication of 'tripartite division' (de Vaan)."

However, the entry explicitly states the word is "of unknown origin," indicating that despite the *tri-* analysis, the etymology remains uncertain. The meaning expanded from its original Hebrew and Roman contexts to refer to modern ethnic groups by the 1590s.
```


## [2026-09-05T14:14:12.765Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==225' KNT.txt | head -6\necho \"...\"; awk 'BEGIN{RS=\"\\f\"} NR==225' KNT.txt | tail -4\necho \"=== BRT urvarä- headword ===\"; grep -n \"urvarä-\\|urvara-\" BRT.txt | head -6",
 "description": "Kent page header and Bartholomae urvara headword"
}
```


### [2026-09-05T14:14:14.425Z] TOOL RESULT

```
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
...
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. 
=== BRT urvarä- headword ===
2733:holz  zum  mindesten  darbringend  ist  man  Inf-  <^t^^;  Absol.  'agi?m,  •iünbrn. r.f'  N.106;  —  iat  tä  °ma  (^V.)  yaoz-  i)  '(etwas)  suchen,  suchen  nach  -, dayqn  ar>h>n  V.  7. 28;  ■ — ■  pairi  urvarä-  aufsuchen':  yd  aüm  mainimnö  ahm byasca  varsoäbyasca  'tnaiil^ö  "abseits  von  isimnS  ahm  apa.rao'iayeiU  {sA.)  .  .  dru- Bäumen  und  Sträuchem,  die  Brennholz  jimca  vinasti  V.  7.78;  —  Med.  auch  in sind  (geben)"  V. /6'.  2;  —  Auskam  °m»m  reflex,  Sinn:  vSrrinahe  .  .  yS  vazaite  .  . Y.JI.8; — Auskanqm  ..  'manqm  ,.  nafi-  axsa/hi  {sä.)  xsa/hTm  tsfmnS  \'t  14.  20; tanqm  ..  xraozdvanam  ..  varidvanamY.    ao.  a)  mit  Dat.  comm.:  vlstäspahe  ..
7275:ä^rat  .  .  apat  .  .  bar}sm»n  V .  ^.  ii ;  16, /6".4,  77.4;  —  zqm  ahurd'Mtlqm  .  .  sp^m tacintqm .  .yavünqm  uru'imqin  V,  ig. 36;  — a'ia  fiaomya  (da  apa  (IS.)*'  »"^a  aiwyä- uhana  (näml.  ratufris)  N.  108.  a)  Du. in  Verbindung  mit  urvarä-  Du.;  yal  k?r)- naol  ..   atihaoiimne  äpa   urvaire  \.g.\;
8182:•  j,  uxsyat-urvarä-  Adj.  (mask.  •ra-')  'bei dem,  durch  den  die  Pflanzen  wachsen': salavalsS  .  .  "rö  Yt.  /^-44;  43;  —  mC^nrn .  .  °r?m  Yt.io.6i;  —  xh'iua  äzüitt  .  . tacat.,ipa  'ra  (ADm.)  Y./6.8.
8467:•  j.,  g.  urvarä-  f.  Tflanze',  meist  Plur.; Sing,  äwich  koll.'*;  oft  göttlich  verehrt; I )  im  AUgemeben,  hauptsächlich  von  den Nutz-  und  NährpSanzen:  eaiti  hsnti  'ranqm sar»fia  "wie  viel  Arten**  von  Pflanzen giebt  es?"  V.5.19  PitZ.;  —  a^ra  »;? raoomti  vUpk  vispSjarvoö  V,5.  19;  — yerihe  paiti  pourujar^a  s»mSoa  usuxlyeinii •rä  Yt  /j,  10;  —  avqm  vanqm  .  .  yä visps.bis(_sd.)  nqma  yqm  upairi  vjspanqm •ranqm  iacxma  nilayal  YL  /2. 1 7 ;  —  vis- paaqm  'ranqm  taoxma  .  .  ysi  hmti bartzisia^a  hubaotaitsmaca  V.  2.  28; 'ranam  (als  Subi.)  zairi^aonanam  tarp- matm  paiti  amäca  *usuxsyänti  Yt7.4'';
8468:urvara-  1  403
8474:403  urvara-  2  —
```


## [2026-09-05T14:14:32.957Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=====REC 541\"; awk 'BEGIN{RS=\"\\f\"} NR==541' BQT_v1_pages.txt | tail -30\necho \"=====REC 539\"; awk 'BEGIN{RS=\"\\f\"} NR==539' BQT_v1_pages.txt | tail -25",
 "description": "Borhan bum/bumahan footnotes"
}
```


### [2026-09-05T14:14:34.673Z] TOOL RESULT

```
=====REC 541
او ههسین ع بر وزن‌خوشه چن. بمعنی
ارل بومهن است کمزازله و زمین لرزه باشد. ۷
ون « بفتح اور و سکون انی و نون.
بمعنی حصه و بپره باشد - و نم اول زهدان
و بچه دان‌که بعربی رحم کویند - وآسمان را
نیز گفته اند - و بن و نهایت و پابان و انتهای
هر چیز باشد ۷ - و رود گوسفند وگاو وامثال
آن کهآ نرا باك لکرده باشند .
بو فلس 4 - ینم اول و انی و سکون‌اك
ودال ابجد » بمعنی آهستگی باشد - و بفتح ثانی
و کسر انی بمعتی باشند - و مرد صاحب‌نخوت
و هدتی را نیز گوبند .
بو فده - بن اول وئانی وسکون‌ثالك
و فتح دال ابجد . مه‌نی هرود هته وربا لگنج
باشد - و بفتح ثانی و کسر ثانی مرد با حستی
و هیبت و ساحب نخون را کویند . ٩‏
لو ۵ » سم ٌم اول و فتح ثانی ۰ درختی‌را
گویند که هر کز بار و ثمر ناورد - و مردم
آهسته را نیز کنته‌اند ۸
۲ص ۳۱ ۰ ۱۷۱ ۰
سنابی غزنوی بدوممتی آورده :
کشوری را که عدل عام تدیف
بوم در بومش ایچ بام ندید .
روت :
۳ - ۵۶۵۵۵0 از
۳ ۷ ۹
۵ رك: نون.
تو کفتی زمین داردی لرز وتب. اسدی‌طوسی
۲ - ر۵: ول ۸ - رك : بونده.
( بر های فاطی۳ )
=====REC 539
غین نقطه دار و نون و چیم ساکن . شوئیز را
کوه 2 و ان تفن است ره .و سا وگ
و عربی حبة السودا خوانند - و فوشنج را نیز
کفته اند و آن ضبه ایست در خراسان تزديك
قندهار ۴ .
وه » بر وزن صوف » پرنده ایست
که بنحوست اشتهار دارد » و آنرا بوم نیز
گونده . ۳
بو فروش» بکر فا , عطار و مك
فروی را گوبند . :
وق - نم اول و سکون ثانی و قاف »
سفید مهرء باشد و آن چیزیست که در حمامها
وآسیاها و هنگامها نوازند" - و با انی مجهول
چادر بزرکی باشد که رختخواب درآن بندند .
بو قلمون -
دیبای رومی را گونند,
و آن جامه ات که
هراحظه برتگی‌تماید
و کنابه‌از کمی‌است که
هرساعت خودرا برنگی
۴ - بونانی 007 -<
۵ در ادییات زرتشتی نام جفد .
توباز سدره نثینی فك نشیمن تست
چرا چو بوف کی‌آشان بوبرانه.
دفاب ۱: ۳۷۲۱ * ورك: اسفا ۱ : ۲ ص۰۷
```


## [2026-09-05T14:14:44.929Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بومهن ===\"; grep -n \"بومهن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5\necho \"=== MON بتکده ===\"; grep -n \"بتکده\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5\necho \"=== MON بوش ===\"; grep -n \"بُوَش\\|بوش \" MON_part1.txt 2>/dev/null | head -3\nls -la MON_part1.txt MON_part2.txt",
 "description": "Grep Mo'in dictionary"
}
```


### [2026-09-05T14:14:45.031Z] TOOL RESULT

```
=== MON بومهن ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26222:بومهن: «دطه-ستا [- بومهین - بوم + مهن 
MON_part1.txt:26222:بومهن: «دطه-ستا [- بومهین - بوم + مهن 
=== MON بتکده ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:21193:بتستان: 00۱-۵)6۵(۲ (امر.) تخانه» بتکده. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:21196:بتکده: (ع-)۵02(-00۱ (امر .) ستخانه» شستان. 
MON_part1.txt:21193:بتستان: 00۱-۵)6۵(۲ (امر.) تخانه» بتکده. 
MON_part1.txt:21196:بتکده: (ع-)۵02(-00۱ (امر .) ستخانه» شستان. 
MON_part2.txt:5965:بتکده. بتخانه. (.) هر شهر حسن‌خیز: جایی 
=== MON بوش ===
18674:(مفرد» غم.) - بوش (غم.) فرومایگان؛ 
26131:می آوردند و بوش دربندی میگفتند. 
33424:پسوشنه: (0-)3-272ت۲ (امر.) سربوش که 
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-05T14:14:47.983Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26218,26230p' MON_part1.txt\necho \"=== بت entry ===\"; sed -n '21185,21200p' MON_part1.txt\necho \"=== بوم entry ===\"; grep -n \"^بوم:\" MON_part1.txt | head -3",
 "description": "Read Mo'in entries"
}
```


### [2026-09-05T14:14:48.072Z] TOOL RESULT

```
گل‌هایش سفید با صورتی و گلبرگ‌هایش 
ریز و خوشبو است؛ زهرة القندیل» علف 
هزار برگ. 

بومهن: «دطه-ستا [- بومهین - بوم + مهن 
- مثنه. حرکت] (ا.) زمین لرزه» زلز له. 
بون: 2 [ع.] (.) دوری» جدایی. 

بود: (.) بجه‌دان» زهدان» رحم. 

بول: ۳5۰ [- بن ] (.) نهایت و پایان هر چیزء 
بویا: 7 (ص.) دارای بو. خوشو» معطر. 
بوی‌افزار: 0۵۷-۰۴2۴ [- بوافزار - بوزار] 
=== بت entry ===
بتاو ر: 92۱5۷2 (.) عاقست» انجام. 
بتخانه: (0-)۳۰۰«۵۴۵ (امر.) جایی که بت‌ها 
را گذارند» معید بت پرستان» صنم خانه؛ 


ستگده. حرم» ح مسرا» متام رنان و 
معشو قگان شاهان و بزرگان) فغستان. 
بتر : ۲ |[ - بد تر ] (ص تفضد.) بد تر. 
بتستان: 00۱-۵)6۵(۲ (امر.) تخانه» بتکده. 
بتفوز: ۳۷۲02 [پتفوز] (.) پیرامون دهان 
اسان و حوان. منقار مرغان» نو کث. 
بتکده: (ع-)۵02(-00۱ (امر .) ستخانه» شستان. 
بتو: 02-۷ (.) جایی که غالا آفتات در 
آنجا بتابد) مق. نسا. مشرق؛ مق. مغرب. 
بتو: ۲۸45 (.) قیف. قبه و گوی سر عصا و 
دمجتی: سر 
=== بوم entry ===
26209:بوم: سنا (ع.] (1.) (جاد.) جغدء بوف.
```


## [2026-09-05T14:14:56.358Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^بت:\\|^بت ‌\\|^بودن:\\|^بوم ۲\\|^بوم:\" MON_part1.txt | head\necho \"---\"; sed -n '26205,26215p' MON_part1.txt\necho \"--- بت ---\"; grep -n \"بت:\" MON_part1.txt | head -5",
 "description": "Mo'in bot, budan, bum entries"
}
```


### [2026-09-05T14:14:56.440Z] TOOL RESULT

```
4715:بودن: این لباس به شما می آید. (تد.) حرکت 
4934:بودن: بر آن عقبده بودن» چنین فصد داشتن. 
21177:بت: 92۱ [- معر. بط ] (.) (جان.) مرغابی» 
26023:بودن: 0-0 (- بدن | (بوده بود - باشد» 
26209:بوم: سنا (ع.] (1.) (جاد.) جغدء بوف. 
46681:بودن: روان ودن» متداول ودن» رایج نودن. 
59942:بودن: دخالت کردن» داخل شدن. پناه بردن» 
60200:بودن: مقید بودن» محبوس بودن. 
61115:بودن: تهیدست بودن» مسفلس سودن» هیچ 
79039:بودن: سالم بودن. به سلامت ماندن: در امان 
---
نقاشی نك ز مه بارچهة زر دوزی شده. 
زمينة کتاب» درفش» کاغذ. مرز و بوم: 
سرزمین» ناحیه. 

بوم: سنا (ع.] (1.) (جاد.) جغدء بوف. 
بوع: 00۷-۱ (فع.) اول شخص مفرد از فعل 
مضارع از «بودن»؛ باشم. 

بومادران: 0۳-802۲ [- بوی‌مادران < 
بوماران] (امر.) (گیا.) گیاهی از تیر مرکبان 
دارای ساقه‌های بلند و برگ‌هایش سیار 
--- بت ---
7192:اجابت: اوه [ع.] (مصم.) پاسخ دادن» 
9220:اذهابت: 0 [ع.] (مص .) لطس 
11446:اسستجچابت: ادةلعاعه [ع. اسستجابة] 
12486:استنابت: 0 [ع. استنابه ] (مص م.) 
13694:اصابت: :«ن3ه» (ع. اصابة] (مص‌ل.)
```


## [2026-09-05T14:15:04.893Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hurwar%C4%81",
 "prompt": "What is the reconstruction and meaning, and what is its etymology (which PIE root)? List descendants including Avestan uruuarā and Middle Persian urwar."
}
```


## [2026-09-05T14:15:05.474Z] TOOL CALL #55: WebSearch

```json
{
 "query": "Avestan Buiti daeva Vendidad 19 etymology Buddha idol Persian but"
}
```


### [2026-09-05T14:15:07.974Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T14:15:13.834Z] TOOL RESULT

```
Web search results for query: "Avestan Buiti daeva Vendidad 19 etymology Buddha idol Persian but"

Links: [{"title":"Daeva | Demonology | Fandom","url":"https://genies.fandom.com/wiki/Daeva"},{"title":"Daeva","url":"https://en.wikipedia.org/wiki/Daeva"},{"title":"AVESTA: VENDIDAD (English): Fargard 19.","url":"https://www.avesta.org/vendidad/vd19sbe.htm"},{"title":"Avesta | Encyclopedia MDPI","url":"https://encyclopedia.pub/entry/35018"},{"title":"AVESTA: VENDIDAD (English): Fargard 19. - Zoroastrian .org.uk","url":"http://www.zoroastrian.org.uk/lib/avesta-org/vendidad/vd19sbe.htm"},{"title":"“Avesta, The Bible of Zoroaster” – World Mythology, Volume 1: Gods and Creation","url":"https://open.maricopa.edu/worldmythologyvolume1godsandcreation/chapter/avesta-the-bible-of-zoroaster/"},{"title":"Vendidad","url":"https://en.wikipedia.org/wiki/Vendidad"},{"title":"Vedic Elements in the Ancient Iranian Religion of Zarathushtra Subhash Kak","url":"https://www.ece.lsu.edu/kak/zoro.pdf"}]

Based on the search results, I found information about Buiti and Vendidad 19:

In Vendidad 19, Angra Mainyu sends the demon Buiti to kill Zarathushtra; Zarathushtra sings aloud the Ahunwar, and the demon flies away, confounded by the sacred words and by the glory of Zarathushtra.

However, the search results do not contain specific information about the etymology connecting "Buiti" to "Buddha" or "idol" or Persian linguistic connections to the Buddha. The results focus on the narrative role of Buiti as a demon in the Vendidad text itself, but do not address the etymological relationship you're asking about.

To provide more detailed information about that specific etymological connection, a more specialized search focusing on comparative Indo-Iranian linguistics and potential Buddhist-Zoroastrian textual interactions would be needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T14:15:23.168Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.avesta.org/vendidad/vd19sbe.htm",
 "prompt": "Quote the passage in Fargard 19.1-2 mentioning the demon Buiti, and any footnote about Buiti (e.g. whether it is identified with Buddha or with the idol but)."
}
```


### [2026-09-05T14:15:28.483Z] TOOL RESULT

```
# Fargard 19.1-2 on the Demon Buiti

**The Passage:**

"The Druj came rushing along, the demon Buiti, who is deceiving, unseen death." (Fargard 19.1)

**Footnote Information:**

According to note 3, Buiti receives scholarly identification in the _Greater Bundahishn_ as the Bût (an idol worshipped by Budasp, a corruption of Bodhisattva). The note suggests Buiti represents a personification of Buddhism, which flourished in Eastern Iran during the centuries before and after Christ. An alternate pronunciation, Buidhi, appears in Vendidad 11.9 and may be more accurate.
```


## [2026-09-05T14:15:41.229Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%AA' --note 'page 94, root Bheu 3, node 9: Persian بت \"idol\" — Wiktionary derives it from MP bwt \"Buddha, idol\" < Sanskrit buddha, not from Avestan Būiti' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/pagoda' --note 'page 94, node 12: pagoda < Port. pagode, perhaps < Pers. butkada or Tamil pagavadi/Skt bhagavati' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-' --note 'page 94, root Bheu 3 = PIE *bʰuH- \"to be, become, grow\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85' --note 'page 94, nodes 3-5: Persian بوم \"land, earth\" < MP būm < OP būmiš' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/tribe' --note 'page 94, nodes 18-19: Latin tribus, tri- + *bhu- analysis (de Vaan), origin uncertain' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.avesta.org/vendidad/vd19sbe.htm' --note 'page 94, node 7: Vendidad 19.1 daeva Buiti; Darmesteter note identifies him with the But idol of Budasp/Bodhisattva' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:15:44.307Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5fa53052e7ca5ebf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/94fc3e84fa3260cf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0540edd459bc9cc5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/18175ceb85ad6f57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/87e6906438234759.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/549046594df6e626.txt
```


## [2026-09-05T14:15:50.181Z] TOOL CALL #58: Bash

```json
{
 "command": "pdftoppm -f 94 -l 94 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg94 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 94"
}
```


### [2026-09-05T14:15:52.498Z] TOOL RESULT

```
total 31096
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:15 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66054 Sep  5 10:10 mk89.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157177 Sep  5 10:09 pg92_500.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8494 Sep  5 10:09 pg92_avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3476 Sep  5 10:09 pg92_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
```


## [2026-09-05T14:15:55.328Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg94.png"
}
```


### [2026-09-05T14:15:55.982Z] TOOL RESULT

```

```


## [2026-09-05T14:15:55.981Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T14:16:14.722Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg94.png')\nprint(im.size)\nim.crop((1650,900,2000,1090)).resize((1400,760)).save('pg94_urvar.png')\nim.crop((650,1080,1050,1220)).resize((1600,560)).save('pg94_sogd.png')\n\"",
 "description": "Crop page 94 regions"
}
```


### [2026-09-05T14:16:16.788Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-05T14:16:19.048Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg94_urvar.png"
}
```


### [2026-09-05T14:16:19.074Z] TOOL RESULT

```

```


## [2026-09-05T14:16:29.188Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg94_sogd.png"
}
```


### [2026-09-05T14:16:29.207Z] TOOL RESULT

```

```


## [2026-09-05T14:18:00.906Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN arbour/herb ===\"; grep -n \"^arbor \\|^arbour\\|^herb \" KLN_1971.txt | head -5\necho \"=== WLD Bd2 bheu ===\"; grep -n \"bheu-\\|bhen-\" incoming/WLD/WLD_Bd2_pages.txt | head -5\necho \"=== IEC bheu ===\"; grep -n \"^bhe[uw]\" IEC.txt | head -8",
 "description": "Klein, Walde-Pokorny, Mann lookups"
}
```


### [2026-09-05T14:18:00.982Z] TOOL RESULT

```
=== KLN arbour/herb ===
18666:arbor , ‘tree*. 
18692:arbor escens, gen. -entis, pres. part, of arborSs- 
18708:arbor vitae, n., an evergreen tree of the genus 
112521:herb and -accous. 
112543:herb bennet, a European herb with an astringent 
=== WLD Bd2 bheu ===
9065:140                                                               bheu-
9099:bheu-          ursprgl.     „wachsen" (wohl = „schwellen“, vgl.                                            pralhrita-h mit ah
9126:                                                                     bheu-                                          141
9200: 142                                                              bheu-
9223:Verbum Subst. und Kopula, woran Formen von ^’5- und bheu- beteiligt
=== IEC bheu ===
1266:bheudhó ‘prompt, arouse, exhort; be awake’. Cf. bhudh-. WP II, 147 Skt. bódhami; Gk. peüthomai (lit. “be prompted', hence ‘hear of); Go. cf. ana-, faür-biudan; OHG biotan; OE beodan 'de- clare; order": ON bjóða ‘offer’; OFris. biada; OCS bljudo, bljusti ‘guard’
1267:bheudhos ‘offertory, bowl, platter’. Cf. bheudho Phryg. (in Gk.) beüdos “a coloured garment’; Go. biups ‘table’; OE beod ‘table, dish, bowl’; MHG biute ‘kneading-trough’; ON bjóð ‘table, bowl’; OCS bljudü “dish?
1268:bheugo (bhoug-) ‘flee’. WP II, 144
1277:bheuros, see bheuəros
1278:bheuən-, bheun- ‘dwelling’. Cf. bhou-, bheuó Skt. (ambig.) bhavan; Alb. bun “mountain- hut’; cf. MHG biu-lich
1279:bheuəros, bheur- ‘awful, enormous’. Cf. bhour-, bhur- Av. baevaro ‘10,000; LW in Arm. biwr, wd: Oss. bīrä, beurä, berä ‘many’; W bur (i-st. ‘rage’); OCS cf. (o-gde) burja ‘storm’; Li. biaurùs ‘nasty, boorish’
1280:bheuð (bhou- bhü-) ‘be’. Cf. bhou-, bhū- as separate entries Skt. bhávàmi; Av. bavai(mi) beside buye, mp.; Arm. cf. bovem ‘wait, expect’; Alb. buj ‘lodge, spend the night; W cf. bu ‘he was; MHG biuwen, bouwen, büwen ‘dwel; Go. cf. (o-grade) bauan, id.
```


## [2026-09-05T14:18:07.702Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '112510,112525p' KLN_1971.txt\necho \"=== klein arbour ===\"; grep -n \"arbour\" KLN_1971.txt | head -4",
 "description": "Klein herb and arbour"
}
```


### [2026-09-05T14:18:07.778Z] TOOL RESULT

```
ding see subst. suff. -ite. 

herb, n. — ME. herbe, erbe, fr. OF. erbe (F. her- 
be ), fr. L. herba , ‘grass, herb’, which is of un- 
certain origin. The spelling with h is due to the 
influence of L. herba . Cp. yerba and the second 
element in contrayerva. 

Derivatives: herb-y, herb-less, adjs. 
herbaceous, adj., pertaining to, or resembling, 
herbs. — L. herbaceus, ‘grassy’, fr. herba. See 
herb and -accous. 

herbage, n., herbs collectively. — ME. erbage , fr. 
F. herbage, fr. ML. herbaticum, fr. L. herba. 
See herb and -age. 
=== klein arbour ===
18659:arbor, arbour, n., a shady retreat. — Fr. earlier 
18665:to arbor, arbour is due to a confusion with L. 
25937:barber, n. — ME. harbour , fr. OF. barbeor (as 
109641:harbor, harbour, n. — ME. hereberge, herberwe,
```


## [2026-09-05T14:18:10.720Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18659,18668p' KLN_1971.txt\necho \"=== HRN budan ===\"; grep -n \"biidan\\|bfldan\\|'sein'\" HRN.txt | head -8",
 "description": "Klein arbour and Horn budan"
}
```


### [2026-09-05T14:18:10.803Z] TOOL RESULT

```
arbor, arbour, n., a shady retreat. — Fr. earlier 
arber , fr. ME. herbier , ‘a garden of herbs’, fr. 
OF. (— F.) herbier , fr. L. herbarium , of s.m., 
fr. herba , ‘herb’. See herb and cp. herbarium. 
For the change of e (in ME. herbier) to a (in 
arber ) cp. carve , harbor. The change of arber 
to arbor, arbour is due to a confusion with L. 
arbor , ‘tree*. 

arbor, n., tree. — L., of uncertain origin. Cp. ar- 
=== HRN budan ===
```


## [2026-09-05T14:18:19.637Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg94.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/94.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T14:18:19.718Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
```


## [2026-09-05T14:34:12.279Z] TOOL CALL #67: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-94.json",
 "content": "{\n  \"pdf_page\": 94,\n  \"book_page\": 64,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Bheu 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *bʰuH- (Pokorny *bheu-, bheuə- : bhou- : bhū-) 'to grow, thrive' > 'to become, to be'\",\n      \"note\": \"Pokorny IEW p. 146 heads the entry 'bheu-, bheuə- (bhuā-, bhuē-) : bhou- : bhū-: ursprünglich \\\"wachsen, gedeihen\\\" (wohl = \\\"schwellen\\\") ... woraus \\\"entstehen, werden, sein\\\"'; Watkins/AHD has 'bheuə-. Also bheu-. To be, exist, grow' — Nourai's gloss 'to exist, grow' is verbatim AHD. The language label 'Indo-European' and the page citation POK:146 are both exact. The entry runs POK 146–150, which is why the page's nodes cite 146, 147 and 149. Two claims inside the chart do NOT belong to this root: Avestan urvarā- 'plant' (nodes 3–5) and English arbor/herb (node 15); see those nodes. Nourai's 'Bheu 3' numbering is his own (he splits several homophonous 'Bheu' roots); Pokorny keeps one entry.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰuH- «روییدن، بالیدن» و از آنجا «پدید آمدن، شدن، بودن». پوکورنی در «فرهنگ ریشه‌شناختی هندواروپایی» ص ۱۴۶ همین ریشه را با صورت‌های bheu-/bhou-/bhū- آورده و معنای نخستین آن را «رشد کردن» دانسته است؛ واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage نیز آن را «بودن، هستی داشتن، رشد کردن» معنی کرده که واژه‌به‌واژه همان چیزی است که نورایی نوشته است. پس عنوان ریشه، برچسب زبانی و معنای آن هر سه درست است و ارجاع POK:146 دقیق است. تنها دو ادعا در این نمودار به این ریشه پیوند ندارد: اوستایی urvarā- «گیاه» و انگلیسی arbor و herb.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:146\", \"status\": \"supports\", \"note\": \"POK_01.txt line 2073 = leaf 155 (leaf = p + 8, so printed p. 146): 'bheu-, bheuə- (bhuā-, bhuē-) : bhou- : bhū-: ursprünglich \\\"wachsen, gedeihen\\\" (wohl = \\\"schwellen\\\") ... woraus \\\"entstehen, werden, sein\\\", weiters \\\"gewohnheitsmäßig wo sein, wohnen\\\"'. The entry continues to p. 150.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bheuə-\", \"stance\": \"supports\", \"note\": \"'bheuə-. Also bheu-. To be, exist, grow. ... [Pok. bheu- 146.]' (AHD_watkins1985.txt line 340) — same gloss and the same Pokorny page.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 140\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt line 9065 has the running head '140 bheu-' and line 9099 'bheu- ursprgl. \\\"wachsen\\\" (wohl = \\\"schwellen\\\") ...' — the source Pokorny cites as 'WP. II 140 f.'\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. bheuə (bhou- bhū-)\", \"stance\": \"supports\", \"note\": \"Mann, IEC.txt line 1280: 'bheuə (bhou- bhū-) \\\"be\\\". Cf. bhou-, bhū- as separate entries. Skt. bhávāmi; Av. bavai(mi) beside buye, mp.; Alb. buj \\\"lodge\\\"; Go. (o-grade) bauan'.\"},\n        {\"src\": \"SYN\", \"where\": \"grep of SYN.txt\", \"stance\": \"silent\", \"note\": \"grep -n 'bhūta|bhuta-' in Buck's Selected Synonyms returns nothing; Nourai's SYN:1503 could not be matched (see nodes 7 and 13).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"bŭta, bav : to exist, become ; bŭšyant, bŭšyeity : will exist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old Iranian inherited the PIE root as *bav- / *bū-. Avestan has the thematic present bavaiti 'becomes, is' (= Skt. bhávati) and Old Persian bavatiy 'becomes' (DNb 14, XPh 55), from *bʰew-e-ti; the past participle Av. būta- 'become, being' continues *bʰuH-tó- (= Skt. bhūtá-, Lat. -fu-tus). The future stem Av. būšyeiti, participle būšyant- 'who will come into being' is the desiderative-future *bʰuH-s-ye/o-, exactly parallel to Skt. bhaviṣyáti and Lith. būsiu. Nourai's 'bav' is the bare stem bav- as Kent lists it for Old Persian; 'bŭta' and the two būšy- forms are Avestan only (Old Persian has no attested future), so the joint label 'Avestan / Old Persian' is a simplification but not an error.\",\n          \"derivation_fa\": \"ریشهٔ هندواروپایی *bʰuH- در ایرانی باستان به‌صورت ستاک bav-/bū- بازمانده است: اوستایی bavaiti «می‌شود، هست» و پارسی باستان bavatiy «می‌شود» (کتیبهٔ داریوش، نقش رستم ب، سطر ۱۴) هر دو از *bʰew-e-ti اند و با سنسکریت bhávati هم‌ریشه‌اند. صفت مفعولی اوستایی būta- «شده، بوده» دنبالهٔ *bʰuH-tó- است، و ستاک آیندهٔ būšyeiti با اسم فاعل būšyant- «آنکه به هستی خواهد آمد» همان ساخت آیندهٔ ‑س‑ی‑ است که در سنسکریت bhaviṣyáti و لیتوانیایی būsiu نیز دیده می‌شود. ادعای نورایی درست است؛ تنها باید یادآور شد که صورت‌های būta و būšy- تنها اوستایی‌اند و در پارسی باستان گواهی نشده‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:146\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 155 (= printed p. 146): 'Ai. bhávati \\\"ist, ist da, geschieht, gedeiht, wird\\\" = av. bavaiti \\\"wird, entsteht; geschieht; wird sein\\\", apers. bavatiy \\\"wird\\\"; Fut. ai. bhaviṣyáti, av. būsyeiti Partiz. būsyant- \\\"der ins Dasein treten wird\\\"' and 'ai. bhūtá-ḥ, av. būta- \\\"geworden, seiend\\\"'. Every one of Nourai's four forms is on this page.\"},\n            {\"ref\": \"BQT:111\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt record 331 (the offset leaf ≈ printed + 220 is fixed by بت on record 454 = p. 234 and بومهن on record 541 = p. 320) carries the اسپـ headwords (اسپرغم، اسپرس، اسپرسب); no bav-/būdan material found there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Lexicon, p. ~199 s.v. bav-\", \"stance\": \"supports\", \"note\": \"KNT.txt line 5741 (leaf 224, header 'LEXICON'): 'bav- vb. \\\"become, be\\\": present stem bava- (§213), Av. bavaiti, Skt. bhávati, Gk. φύω \\\"grows\\\", Lt. fui \\\"I was\\\", Lith. būti \\\"to be\\\", NEng. be, pIE *bheu-. See also būmi-.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bheuə-\", \"stance\": \"supports\", \"note\": \"Zero-grade *bhu- and lengthened *bhū- are set out there with the same Indo-Iranian evidence.\"},\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb. s.v. bav-\", \"stance\": \"silent\", \"note\": \"The local BRT.txt OCR is too corrupt to retrieve the bav-/būta- columns (grep for 'būta', 'buiti' etc. returns nothing usable); Kent and Pokorny were used instead.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"bŭdan «بودن» : to be ; bâšîdan «باشیدن» : to be ; bovesh «بُوَش» : being, existence\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP بودن būdan continues Middle Persian būdan, present stem baw- (MacKenzie: 'būdan, b(aw)- [YHWWN-tn' ; bwtn', b- | M bwdn, bw-, N būdan] be, become'), itself the Old Iranian participial infinitive *bū-tanai to the stem bav-/bū-; intervocalic -t- of *bū-ta- is voiced to -d- in Middle Persian (*būtan > būdan), the regular change seen in Av. dāta- > MP dād. The subjunctive/optative forms in Nourai's script_extra are the same paradigm: باد bād 'may it be' (< MP bawād < OIr. *bavātu), بادا bādā, and the imperative بو bow / باش bāš. باشیدن bāšīdan is a late New Persian secondary infinitive built on the present stem باش bāš-, which is the Middle Persian imperative/subjunctive stem of the same verb, and not an independent root. بُوَش bovaš is MP bawišn 'becoming, genesis' (MacKenzie lists 'bawišn: becoming, genesis' under būdan), with the regular MP abstract suffix -išn > NP -eš and the -w- retained before it.\",\n          \"derivation_fa\": \"«بودن» دنبالهٔ فارسی میانهٔ (پهلوی) būdan با ستاک حال baw- است که مکنزی در «فرهنگ کوچک پهلوی» به‌صورت būdan, b(aw)- ثبت کرده؛ خودِ آن از ایرانی باستان *bū-tanai از ستاک bav-/bū- است و ت میان دو واکه در فارسی میانه به د نرم شده است (*būtan > būdan)، همان دگرگونی که در dāta- اوستایی > داد پهلوی دیده می‌شود. «باد۲» و «بادا» صورت‌های التزامی و دعایی همین فعل‌اند (پهلوی bawād) و «بو» و «باش» صیغهٔ امر آن. «باشیدن» مصدر ثانوی و متأخر فارسی نو است که روی ستاک حالِ «باش» ساخته شده، نه ریشه‌ای جداگانه. «بُوَش» همان bawišn پهلوی «شدن، هستی» است؛ پسوند اسم‌ساز ‑išn پهلوی در فارسی نو به ‑ش بدل شده است. حاشیهٔ معین بر برهان قاطع (ص ۳۱۴) نیز «بودن» را پهلوی būdan از ریشهٔ ایرانی bav-/bū با گواه اوستایی bavaiti و سنسکریت bhavati می‌داند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:147\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 155, printed p. 147: 'prábhūta-ḥ \\\"reichlich, zahlreich\\\", npers. Inf. būdan \\\"sein\\\"' — Pokorny names New Persian būdan on exactly the page Nourai cites.\"},\n            {\"ref\": \"BQT:314\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt record 535 ≈ printed p. 314, Mo'in's footnote 5: 'بودن ... پهلوی būdan ... از ریشهٔ ایرانی باستان bav-, bū (به‌همین معنی) ... اوستا bavaiti، سانسکریت bhavati (سوم شخص) ... اسلاو byti (مصدر)'. Exactly Nourai's arrow.\"},\n            {\"ref\": \"BQT:111\", \"status\": \"not_found\", \"note\": \"record 331 ≈ p. 111 carries اسپـ headwords only (see node 1).\"},\n            {\"ref\": \"MON:603\", \"status\": \"partial\", \"note\": \"Mo'in's بودن entry is present (MON_part1.txt line 26023: 'بودن: bu-dan [= بدن] (بوده، بود ـ باشد ...)') but the Adena 2-vol. reprint on disk has its own pagination, so the page number 603 of the 6-vol. Amir Kabir edition cannot be confirmed; the content agrees.\"},\n            {\"ref\": \"AEF:293\", \"status\": \"not_checked\", \"note\": \"Khaleqi-Motlaq's Persian translation of Horn is not online (refs_online.json: 'Not online (searched archive.org, ketabnak, noorlib, web)'); checked against Horn/Hübschmann instead.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. ~19 s.v. būdan\", \"stance\": \"supports\", \"note\": \"PHD.txt line 292: 'būdan, b(aw)- [YHWWN-tn! ... bwtn', b- | M bwdn, bw-, N būdan] be, become. bawišn: becoming, genesis.' — supplies both بودن and بُوَش.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. بودن\", \"stance\": \"supports\", \"note\": \"MON_part1.txt line 26023 'بودن: bu-dan ... (بوده، بود ـ باشد)'.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 314, Mo'in's fn. 5\", \"stance\": \"supports\", \"note\": \"see ref_check above; Mo'in gives the whole Old Iranian → Pahlavi → New Persian chain.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"bŭmî : earth ; bŭmî-mathan : earthquake ; urvarâ : plant\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"būmī- is correct and well supported: Av. būmi-, OP būmi- 'earth, land' (Kent: 'deriv. of root bhav- ... in grade bhū-'), from *bʰuH-mi- 'the grown/existing one' = Skt. bhū́mi-, and the direct ancestor of MP/NP بوم. 'bŭmî-mathan' is NOT an attested Old Iranian compound: neither Kent's Old Persian lexicon nor Bartholomae has it; it is Nourai's back-projection of New Persian بومهن (see node 5), whose second element Mo'in analyses as مهن 'movement'. The third word is the real problem: Avestan urvarā- f. 'plant' (Bartholomae s.v. 'urvarā- f. \\\"Pflanze\\\", meist Plur.') has nothing to do with *bʰuH-; it continues Proto-Iranian *(H)urwarā-, cognate with Skt. urvárā 'fertile field', and no dictionary derives it from bheu-. Pokorny's bheu- entry lists Av./OP būmi- but never urvarā-. This arrow is therefore rejected by modern scholarship.\",\n          \"derivation_fa\": \"دربارهٔ būmī- ادعای نورایی درست است: اوستایی būmi- و پارسی باستان būmi- «زمین، سرزمین» از *bʰuH-mi- «آنچه روییده/هست» است، هم‌ریشه با سنسکریت bhū́mi- و نیای مستقیم «بوم» فارسی؛ کنت در واژه‌نامهٔ پارسی باستان آن را صراحتاً «مشتق از ریشهٔ bhav- در درجهٔ bhū-» می‌خواند. اما būmī-mathan صورتی گواهی‌نشده است و نه در کنت و نه در بارتولومه یافت نمی‌شود؛ این بازسازیِ خودِ نورایی از «بومهن» فارسی نو است. مشکل اصلی واژهٔ سوم است: اوستایی urvarā- «گیاه» (بارتولومه: urvarā- f. «Pflanze») هیچ پیوندی با ریشهٔ *bʰuH- ندارد و دنبالهٔ ایرانی آغازین *(H)urwarā- و هم‌ریشه با سنسکریت urvárā «کشتزار بارور» است؛ پوکورنی نیز در مدخل bheu- تنها būmi- را آورده و نامی از urvarā- نبرده است. پژوهش امروزی این پیوند را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:146\", \"status\": \"partial\", \"note\": \"Pokorny does give 'ai. bhū- f. \\\"Erde, Welt\\\", bhū́mi-, bhū́miḥ, av. ap. būmi-, npers. būm \\\"Erde\\\"' — but on p. 147, one page past Nourai's citation, and with no mention of urvarā- or of a compound *būmī-mathan.\"},\n            {\"ref\": \"KNT:200\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 225 (running head 'LEXICON', the b- entries of Kent's lexicon, pp. 199–200): 'būmi- sb. \\\"earth (= world or ground)\\\": Av. būmi-, NPers. būm, Skt. (RV) nom. bhū́mi bhū́miṣ; deriv. of root bhav- (see bav-) in grade bhū-, cf. Skt. aor. ábhūt, Gk. ἔφυ.' Exactly Nourai's arrow for būmī.\"},\n            {\"ref\": \"BQT:111\", \"status\": \"not_found\", \"note\": \"record 331 ≈ p. 111 has اسپـ headwords only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb. s.v. urvarā-\", \"stance\": \"contradicts\", \"note\": \"BRT.txt line 8467: 'urvarā- f. \\\"Pflanze\\\", meist Plur.; Sing. auch koll.; oft göttlich verehrt' — Bartholomae's entry gives no connection whatever with bav-/bū-, and the word is filed under u-, not under the bū- family.\"},\n            {\"src\": \"KNT\", \"where\": \"Lexicon s.v. būmi-\", \"stance\": \"supports\", \"note\": \"see ref_check; Kent derives būmi- from bav-.\"},\n            {\"src\": \"POK\", \"where\": \"p. 147\", \"stance\": \"partial\", \"note\": \"'av. ap. būmi-, npers. būm \\\"Erde\\\"' present; urvarā- absent from the whole bheu- entry (pp. 146–150).\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"bŭm 2 : earth ; bŭmahan : earthquake ; urvar : plants\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"MP būm [bwm] 'land, earth, country' is the regular continuation of OP/Av. būmi-: the i-stem loses its final vowel in Middle Persian (*būmi- > būm), as in *zami- > zamīg. MacKenzie confirms both būm and urwar 'plant(s), vegetable' [ʾwlwl | Manich. ʾwrwr], and Nyberg's glossary explicitly links the latter to 'Av. urvarā-'. The arrow #3 → #4 is therefore right form-for-form. Two reservations: (a) 'bŭmahan' is not attested in Pahlavi — MacKenzie's word for earthquake is būm-čandag [bwm-cndk'] 'earth-shaking', and the Book Pahlavi texts also use bum-larzišn; būmahan looks like Nourai's Pahlavi-ising of NP بومهن; (b) urwar is inherited from Av. urvarā- but, as at node 3, does not belong under the root Bheu at all.\",\n          \"derivation_fa\": \"«بوم» فارسی میانه [bwm] «سرزمین، زمین، کشور» دنبالهٔ منظم būmi- ایرانی باستان است؛ واکهٔ پایانی ستاک ‑i در فارسی میانه می‌افتد (*būmi- > būm)، همان‌گونه که *zami- > zamīg. مکنزی هر دو واژهٔ būm و urwar «گیاه» را ثبت کرده و نیبرگ در واژه‌نامهٔ پهلوی خود urvar را صراحتاً به اوستایی urvarā- بازمی‌گرداند؛ پس پیوند گرهٔ ۳ به ۴ از نظر صورت درست است. اما دو نکته: نخست آنکه būmahan در پهلوی گواهی نشده است و واژهٔ مکنزی برای زمین‌لرزه būm-čandag «لرزش زمین» است، و būmahan ظاهراً صورتی است که نورایی از «بومهن» فارسی نو به پهلوی برگردانده؛ دوم آنکه urwar گرچه به‌درستی از urvarā- اوستایی است، اما همچون گرهٔ ۳ اصلاً به ریشهٔ Bheu تعلق ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AEF:298\", \"status\": \"not_checked\", \"note\": \"Asās-e Eshteqāq-e Fārsi (Khaleqi-Motlaq's Persian Horn) is not available online or on disk; substituted MacKenzie and Nyberg, which are the standard authorities for Pahlavi.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. ~19 s.v. būm, urwar\", \"stance\": \"partial\", \"note\": \"PHD.txt line 292: 'būm [bwm | N ~] land, earth, country. ~-čandag [-cndk'] earthquake.' and line 599: 'urwar [ʾwlwl | M ʾwrwr] plant(s), vegetable.' — būm and urwar confirmed, but MacKenzie's earthquake word is būm-čandag, not būmahan.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. urvar\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt line 3853: 'urvar [ʾwlwl] plant, generally coll. plants, passim ... — Av. (401 sqq.) urvarā-; MPrs ʾwrwr.' Confirms the Avestan → Pahlavi step for urvar (but not a bheu- origin).\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"bŭm 2 «بوم ۲» : earth, country ; bŭmmahan «بومَهَن» : earthquake ; ŭrvar «اورْوَر» : plant\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP بوم būm 'land, country, region' (as in مرز و بوم) is straight from MP būm, OP būmiš — Wiktionary: 'From Middle Persian 𐭡𐭥𐭬 (būm), from Old Persian 𐏏 (būmiš), from Proto-Iranian *búHmiš'. It must be kept apart from the homograph بوم 'owl', which Mo'in marks [ع.] i.e. an Arabic loan. بومهن / بومهین 'earthquake' is a genuine Persian word: Borhan-e Qate' p. 320 defines بومهن 'زمین‌لرزه باشد که به‌عربی زلزله خوانند' and بومهین as its variant, and Mo'in analyses it as بوم + مهن 'movement' — i.e. a New Persian compound, not an inherited one, which is why no Old or Middle Iranian antecedent exists. اورور urvar 'plant' is a rare learned word taken over from Pahlavi urwar; the arrow #4 → #5 holds for all three words, but the ultimate root of urvar is not Bheu (see node 3). Nourai's supporting verse (بر آمد یکی بومهن نیمشب / تو گفتی زمین دارد از لرزه تب) is Asadi Tusi's Garshāspnāma, quoted at exactly that page of Borhan.\",\n          \"derivation_fa\": \"«بوم» به معنی «سرزمین، کشور» (چنان‌که در «مرز و بوم») بی‌واسطه از فارسی میانهٔ būm و آن از پارسی باستان būmiš است؛ باید آن را از هم‌نگاشتِ «بوم» به معنی «جغد» جدا داشت که معین آن را با نشانِ [ع.] وام‌واژهٔ عربی می‌شمارد. «بومهن/بومهین» واژه‌ای اصیل فارسی است: برهان قاطع (ص ۳۲۰) آن را «زمین‌لرزه که به‌عربی زلزله خوانند» معنی کرده و معین آن را ترکیب «بوم + مهن (حرکت)» دانسته است؛ یعنی ترکیبی نوساخته در فارسی دری، و از همین رو صورت کهن ایرانی برای آن در دست نیست. «اورور» واژه‌ای کم‌کاربرد و برگرفته از urwar پهلوی است. پیوند گرهٔ ۴ به ۵ برای هر سه واژه درست است، ولی ریشهٔ نهایی «اورور» ریشهٔ Bheu نیست. بیت گواهِ نورایی («برآمد یکی بومهن نیمشب / تو گفتی زمین دارد از لرزه تب») از گرشاسپ‌نامهٔ اسدی طوسی است و در همان صفحهٔ برهان نقل شده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D9%85\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:147\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 155, p. 147: 'av. ap. būmi-, npers. būm \\\"Erde\\\"'.\"},\n            {\"ref\": \"BQT:320\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt record 541 (≈ printed p. 320): 'بومهن ... بفتح اول و ها و سکون نون، زمین لرزه باشد که به‌عربی زلزله خوانند' and 'بومهین ... بمعنی اول بومهن است که زلزله و زمین لرزه باشد'; the footnote on the same page carries the Asadi Tusi verse 'تو گفتی زمین داردی لرز و تب' that Nourai quotes.\"},\n            {\"ref\": \"MON:401\", \"status\": \"partial\", \"note\": \"Mo'in's entry is verbatim present (MON_part1.txt line 26222: 'بومهن: bum-mahan [= بومهین = بوم + مهن = حرکت] (ا.) زمین‌لرزه، زلزله'), but the Adena reprint on disk repaginates, so page 401 of the Amir Kabir edition could not be checked.\"},\n            {\"ref\": \"AEF:299\", \"status\": \"not_checked\", \"note\": \"AEF not available (see node 4).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. بومهن\", \"stance\": \"supports\", \"note\": \"'بومهن ... [= بومهین = بوم + مهن = حرکت] زمین‌لرزه، زلزله' (MON_part1.txt line 26222) — Mo'in's own morphological analysis, identical to Nourai's reading.\"},\n            {\"src\": \"BQT\", \"where\": \"p. 320\", \"stance\": \"supports\", \"note\": \"see ref_check; both بومهن and بومهین are headwords there.\"},\n            {\"src\": \"PHD\", \"where\": \"s.v. būm\", \"stance\": \"supports\", \"note\": \"'būm [bwm | N ~] land, earth, country' — MacKenzie explicitly equates the Pahlavi and New Persian forms.\"}\n          ],\n          \"extraction_note\": \"Minor diacritic difference: the printed page shows «اورَوَر» (fatḥa on the first rāʾ) where the JSON has «اورْوَر» (sukūn). Everything else in this node matches the page.\"\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Sogdian\",\n          \"words\": \"bwmb : earth, world\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The word itself is right and the arrow is right: Gharib's Sogdian Dictionary no. 2911 (printed p. 114/115) reads 'βwmh (B, S) βūm ⟨< OP. būmī⟩ obl. -y(h) — earth, world', with references VJ 226, 228, 1218; SCE 4.214 etc. Sogdian βūm continues Old Iranian *būmi- with the regular East Iranian lenition of initial b- to β- and loss of the final vowel; the -h of βwmh is the Sogdian orthographic 'silent he', not a consonant. Nourai's 'bwmb' has a final -b where the dictionary has -h. The 300 dpi rendering of the printed page (data/verification/sources/refs/ocr/BOOK/94.png) shows unmistakably 'bwmb', so the JSON extraction is faithful and the misprint is the book's.\",\n          \"derivation_fa\": \"خودِ واژه و پیوند آن درست است: قریب در «فرهنگ سغدی» شمارهٔ ۲۹۱۱ (ص ۱۱۴/۱۱۵ چاپی) آورده است βwmh «زمین، جهان» و آن را از būmī پارسی باستان می‌داند. βūm سغدی دنبالهٔ *būmi- ایرانی باستان است؛ ب آغازین در ایرانی شرقی به β نرم شده و واکهٔ پایانی افتاده است، و ‑h پایانی در املای سغدی «های خاموش» است نه صامت. اما نورایی به‌جای ‑h، ‑b نوشته است. تصویر ۳۰۰ نقطه‌ایِ صفحهٔ چاپی به‌روشنی «bwmb» نشان می‌دهد؛ پس خطای خوانش اسکن نیست، بلکه خطای چاپی خودِ کتاب است و صورت درست βwmh (bwmh) است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"bwmb\",\n          \"correct_form\": \"βwmh (bwmh), Gharib no. 2911\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:115\", \"status\": \"supports\", \"note\": \"SOD_pages.txt lines 12071–12076 (leaf 180; printed ≈ leaf − 66 = 114/115), entry '2911 βwmh B, S — βūm ⟨< OP. būmī⟩ ob. -y(h) — earth, world — VJ 226, 228, 1218; SCE 4.214; TSP; BSTBL, Vim. 102, Dhu. 142, 293, Dhy. 125 etc.' Nourai's page number and gloss are right; only the transliteration's last letter is wrong.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"no. 2911, p. ~115\", \"stance\": \"partial\", \"note\": \"supports the derivation ('< OP. būmī') and the gloss 'earth, world', but prints βwmh, not bwmb.\"},\n            {\"src\": \"PHD\", \"where\": \"s.v. būm\", \"stance\": \"supports\", \"note\": \"'būm [bwm | N ~] land, earth, country' — the West Iranian counterpart of the same *būmi-.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Avestan\",\n          \"words\": \"bŭiti, buiti daevo : name of a demon encouraging idolatry\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Būiti is a genuine Avestan daēva: Vendidad 19.1 'The Druj came rushing along, the demon Būiti, who is deceiving, unseen death', sent by Angra Mainyu against Zarathustra; a variant Buiδi appears at Vd 11.9. Pokorny does list the name under this root — but on p. 147, under bhūti- 'Sein', and with a question mark: 'av. būti- m. \\\"Name eines daēva\\\"?'. So the attachment to Bheu is a possibility Pokorny himself flags as uncertain, not a settled derivation. Nourai's gloss 'a demon encouraging idolatry' is not what the Avesta says: it is Darmesteter's note on Vd 19.1 that identifies Būiti, in the Greater Bundahišn, with the Bût (idol) worshipped by Būdāsp (a corruption of Bodhisattva) and reads the demon as a personification of Buddhism in Eastern Iran. That is a late Zoroastrian identification of the demon with the Buddha-idol, not an etymology of the demon's name. The chart's NOTE (BQT:233, Būiti cognate with Skt. bhūta- 'a being, phantom, ghost') is likewise only plausible: Skt. bhūta- is certainly from *bʰuH-, but no modern Iranist derives Būiti from it.\",\n          \"derivation_fa\": \"«بوئیتی» نام دیوی راستین در اوستاست: در وندیداد فرگرد ۱۹ بند ۱ اهریمن دیو بوئیتی را برای کشتن زرتشت می‌فرستد، و صورت دیگر آن Buiδi در وندیداد ۱۱٫۹ آمده است. پوکورنی این نام را در مدخل همین ریشه آورده، اما در ص ۱۴۷ زیر bhūti- «هستی» و با علامت پرسش: «av. būti- m. نام یک دیو؟». پس پیوند آن با ریشهٔ Bheu گمانی است که خود پوکورنی نیز آن را قطعی نمی‌داند. توضیح نورایی («دیوی که مردم را به بت‌پرستی برمی‌انگیزد») در متن اوستا نیست؛ این از حاشیهٔ دارمستتر بر وندیداد ۱۹ برمی‌آید که بوئیتی را بنا بر بندهش بزرگ همان «بت»ی می‌داند که «بوداسپ» (تحریف بودی‌سَتوَه) می‌پرستید و او را تجسّم آیین بودایی در ایران شرقی می‌شمارد — یعنی این‌همانیِ دینیِ متأخر است، نه ریشه‌شناسی نام دیو. ادعای برهان قاطع (ص ۲۳۳) نیز که بوئیتی را هم‌ریشهٔ bhūta- سنسکریت می‌داند تنها با احتیاط پذیرفتنی است. حکم: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://www.avesta.org/vendidad/vd19sbe.htm\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:146\", \"status\": \"partial\", \"note\": \"the item is there but one page later: POK_01.txt leaf 155, printed p. 147, under 'ai. bhūtí-ḥ, bhū́ti-ḥ f. \\\"Sein, Wohlsein\\\"' comes '(av. būti- m. \\\"Name eines daēva\\\"?' — with Pokorny's own question mark.\"},\n            {\"ref\": \"BQT:223\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt records 443–444 (≈ printed pp. 223–224) contain the باشـ/باغـ headwords (باشتین، باشنگ، باغل، باغنج …) and nothing about بوئیتی. The Būiti footnote is on p. 234 (record 454), so Nourai's '223' looks like a slip for the '233' he gives in his own NOTE.\"},\n            {\"ref\": \"SYN:1503\", \"status\": \"not_found\", \"note\": \"By Buck's stated offset (leaf = printed + 24) p. 1503 = leaf 1527, which in SYN.txt falls in chapter 21 (Law: 'lawyer', 'court'); grep of the whole file for 'bhūta'/'bhuta-' returns nothing. Could not locate any Buck passage on būiti or bhūta.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 26, no. 182\", \"stance\": \"partial\", \"note\": \"'Np. but \\\"Götzenbild, Idol\\\" (afgh. LW. but) nach Fr. Müller = Buddha, nach Horn ~ zd. buiti \\\"Name eines Dämons\\\" (vd. 19,1). Beides schon im grossen Bundehesh, vgl. Darmesteter, le Zend-Avesta II, p. 259.' Hübschmann records the Būiti link as one of two competing views.\"},\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb.\", \"stance\": \"silent\", \"note\": \"the local BRT.txt OCR yields no retrievable Būiti column (grep 'buiti', 'Būiti' returns nothing); the OCR of this scan is heavily degraded in the b- section.\"},\n            {\"src\": \"POK\", \"where\": \"p. 147\", \"stance\": \"partial\", \"note\": \"see ref_check — listed, but queried.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"bŭiti-kata : idol house ☞Ket\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"There is no attested Avestan compound *būiti-kata-. Bartholomae has no such headword, and Būiti occurs in the Avesta only as a demon's name (Vd 19.1, 11.9), never in a compound meaning 'idol house'. The word Nourai is really explaining is New Persian بتکده but-kada / بتخانه but-xāna, and every authority treats that as a New Persian compound formed in Islamic times: Lokotsch no. 373 (pp. 30–31) states plainly 'Pers. batkādā \\\"Götzentempel\\\" [aus pers. but \\\"Götzenbild\\\" (Horn NpEt S. 42, Nr. 182) und kadā \\\"Haus\\\" (ebenda S. 188, Nr. 844)]'. The second element kada is indeed Av. kata- 'chamber, cellar' (Nourai's cross-reference '☞Ket' is correct for that half), but the compound as a whole is New Persian, not Avestan. So the node is Nourai's own reconstruction and is rejected as an Avestan form.\",\n          \"derivation_fa\": \"ترکیب اوستایی *būiti-kata- در هیچ متنی گواهی نشده است؛ در فرهنگ ایرانی باستان بارتولومه چنین سرواژه‌ای نیست و «بوئیتی» در اوستا تنها نام دیو است (وندیداد ۱۹٫۱ و ۱۱٫۹) و هرگز در ترکیبی به معنی «بتخانه» نیامده. آنچه نورایی در واقع توضیح می‌دهد «بتکده / بتخانه»ی فارسی نو است، و همهٔ منابع آن را ترکیبی نوساخته در دورهٔ اسلامی می‌دانند: لوکوچ (شمارهٔ ۳۷۳، ص ۳۰–۳۱) صریحاً می‌نویسد «فارسی batkādā \\\"بتخانه\\\" از but \\\"بت\\\" و kadā \\\"خانه\\\"». جزء دوم یعنی «کده» به‌راستی از kata- اوستایی «اتاق، سرداب» است و ارجاع نورایی به مدخل Ket در این نیمه درست است، اما کل ترکیب فارسی نو است نه اوستایی. حکم: پژوهش امروزی این صورت اوستایی را رد می‌کند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"BQT:234\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt record 454 (≈ printed p. 234) has the Persian headwords بتخانه ('جایی که بت‌ها را گذارند') and بتخال/بتخاله, and a footnote in which the form «بوئیتی» is legible twice — i.e. Mo'in there connects Persian بت with Avestan Būiti — but Borhan gives no Avestan compound *būiti-kata.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 373, pp. 30–31\", \"stance\": \"contradicts\", \"note\": \"'Pers. batkādā: \\\"Götzentempel\\\" [aus pers. but \\\"Götzenbild\\\" Horn NpEt S. 42, Nr. 182 und kädä \\\"Haus\\\" ebenda S. 188, Nr. 844]' — a New Persian compound, formed from but + kada, not an Avestan one.\"},\n            {\"src\": \"BRT\", \"where\": \"Altiran. Wb.\", \"stance\": \"silent\", \"note\": \"no headword būiti.kata- or anything comparable is retrievable in BRT.txt.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. بتکده، بتخانه\", \"stance\": \"partial\", \"note\": \"MON_part1.txt lines 21193–21196: 'بتستان … بتخانه، بتکده' / 'بتکده … بتخانه، بت‌ستان' — Mo'in treats them as ordinary New Persian compounds of بت.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"bot «بت» : idol\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Modern scholarship derives NP بت but/bot 'idol' not from Avestan Būiti but from Sanskrit buddha 'the Buddha' by way of the Buddhist Middle Iranian of the East: MacKenzie's Pahlavi dictionary gives '*but [bwt' | = M, N ~] Buddha; idol', i.e. the Middle Persian and Manichaean Middle Persian word means primarily 'Buddha', the sense 'idol' arising from the images of the Buddha that Iranians met in Bactria and Sogdiana; Wiktionary: 'Inherited from Middle Persian bwt' /but/ \\\"Buddha, idol\\\", ultimately from Sanskrit बुद्ध (buddha)', and it makes بت a doublet of بد bud 'Buddha'. Nourai's route (Av. Būiti → bot) is Horn's 1893 proposal — Horn no. 182, p. 42: 'but \\\"Götzenbild; Liebchen\\\". aw. Būiti- N. pr.; phlv. Būt, Būtjān ... Wenn die Zusammenstellung richtig ist ...' (with Horn's own conditional) — and Hübschmann p. 26 sets it side by side with Fr. Müller's Buddha etymology. The Buddha etymology has since prevailed; the Būiti connection survives only as the medieval Zoroastrian identification recorded in the Greater Bundahišn. Nourai's own note ('See \\\"Pwt\\\" for another possible root') shows he knew of the alternative. The derivatives بتکده، بتخانه، بت‌پرست are ordinary New Persian compounds on this word.\",\n          \"derivation_fa\": \"پژوهش امروزی «بت» را نه از Būiti اوستایی، بلکه از buddha سنسکریت «بودا» می‌داند که از راه ایرانی میانهٔ شرقی و محیط بودایی بلخ و سغد به فارسی رسیده است: مکنزی در فرهنگ پهلوی خود می‌نویسد «but [bwt] بودا؛ بت»، یعنی معنای نخست آن در فارسی میانه و پهلوی مانوی «بودا» است و معنای «بت» از پیکره‌های بودا برخاسته؛ ویکی‌واژه نیز آن را وام‌واژه‌ای از پهلوی but و در نهایت از سنسکریت buddha و دوگانهٔ واژهٔ «بُد» می‌شمارد. مسیری که نورایی کشیده پیشنهاد هرن (۱۸۹۳، شمارهٔ ۱۸۲، ص ۴۲) است که خود او هم با شرط آورده («اگر این هم‌سنجی درست باشد …»)، و هوبشمان (ص ۲۶) آن را در کنار ریشه‌شناسی فریدریش مولر (= بودا) می‌گذارد. امروزه ریشهٔ بودایی پذیرفته شده است و پیوند با بوئیتی تنها این‌همانیِ دینیِ بندهش بزرگ است. خود نورایی هم در یادداشتش به مدخل Pwt ارجاع داده است. «بتکده، بتخانه، بت‌پرست» ترکیب‌های عادی فارسی نو از همین واژه‌اند. حکم: پژوهش امروزی این ریشه‌یابی را رد می‌کند و به‌جای آن buddha سنسکریت را می‌نشاند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%AA\",\n            \"https://www.avesta.org/vendidad/vd19sbe.htm\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:234\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt record 454 ≈ printed p. 234: the بت entry lists among its senses 'و چهارم معبود و مسجود کافران باشد که به‌عربی صنم خوانند'; the page's footnote carries «بوئیتی» twice, i.e. Mo'in's Būiti connection that Nourai is following.\"},\n            {\"ref\": \"MON:472\", \"status\": \"partial\", \"note\": \"Mo'in's بت and بتکده entries are on disk (MON_part1.txt lines 21177–21196) and give the sense but no Avestan derivation; the Adena reprint repaginates, so p. 472 of the Amir Kabir edition could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. ~19 s.v. but\", \"stance\": \"contradicts\", \"note\": \"'*but [bwt! | = M, N ~] Buddha; idol' — MacKenzie's gloss puts 'Buddha' first, i.e. the Buddhist etymology, not Būiti.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 182, p. 42\", \"stance\": \"supports\", \"note\": \"'but \\\"Götzenbild; Liebchen\\\". aw. Būiti- N. pr.; phlv. Būt, Būtjān (Gemme, Horn, Mitteilungen, Heft IV, S. 40, Note). Wenn die Zusammenstellung richtig ist, so gehört np. but in dieselbe Kategorie wie ǰādū, ātaš, patyāre u. a. m.' — Nourai's source, but hedged by Horn himself.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 26, no. 182\", \"stance\": \"partial\", \"note\": \"'nach Fr. Müller = Buddha, nach Horn ~ zd. buiti \\\"Name eines Dämons\\\"' — Hübschmann leaves both open.\"},\n            {\"src\": \"MON\", \"where\": \"s.v. بت\", \"stance\": \"silent\", \"note\": \"the entry gives the senses (مرغابی / صنم) without an etymological tag in the two-volume reprint.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Empty pass-through node. It stands for the Indo-Muslim usage that carried Persian but 'idol' and but-kada 'idol-temple' into the Urdu/Hindustani of the Delhi Sultanate and the Deccan, where the Portuguese first heard it in the early 16th century. Hobson-Jobson (p. 654) makes exactly this point for the Persian etymology: 'but-kadah is a phrase which the Portuguese would constantly hear from the Mahommedans with whom they chiefly had to deal on their first arrival in India.' The intermediary is real as a route of transmission, though no Hindustani form is printed in the box.\",\n          \"derivation_fa\": \"این گره خالی است و تنها گذرگاه است: نمایندهٔ کاربرد هندی‌ـ‌اسلامی است که «بت» و «بتکده»ی فارسی را به اردو/هندوستانی دورهٔ سلطنت دهلی و دکن برد، همان‌جا که پرتغالی‌ها در آغاز سدهٔ شانزدهم آن را شنیدند. یول و برنل در «هابسن‌جابسن» (ص ۶۵۴) همین را می‌گویند: «but-kadah عبارتی است که پرتغالی‌ها پیوسته از مسلمانانی می‌شنیدند که در نخستین سال‌های ورودشان به هند بیشتر با آنان سروکار داشتند». پس مسیر انتقال واقعی است، هرچند در کادر کتاب هیچ صورت هندوستانی چاپ نشده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"pp. 652–655 s.v. PAGODA\", \"stance\": \"supports\", \"note\": \"'On the other hand but-kadah is a phrase which the Portuguese would constantly hear from the Mahommedans with whom they chiefly had to deal on their first arrival in India. This is the view confidently asserted by Reinaud (Mémoires sur l'Inde, 90), and is the etymology given by Littré.'\"},\n            {\"src\": \"AID\", \"where\": \"p. 233 s.v. Pagoda\", \"stance\": \"supports\", \"note\": \"'Pagoda. [According to Webster from the Persian but, an idol, and kodak, a house; but perhaps only a corrup[tion] …]' — Whitworth records the same Persian route through Anglo-Indian usage.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Portuguese\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Empty pass-through node for Portuguese pagode, first attested in Barbosa 1516 ('they call their temples pagodes', quoted at Hobson-Jobson p. 655) and in Corsali; Etymonline dates Portuguese pagode to the early 16th century. The Portuguese form is the immediate source of every European word (Fr. pagode, It. pagoda, Ger. Pagode, Eng. pagoda), which is why Lokotsch no. 373 lists 'der pg. Ausdruck pagoda, engl. pagoda, pagode, dtsch. Pagode, it. pagodo, rum. pagoda, poln. pagoda'. What is not settled is what the Portuguese were adapting — Persian but-kada or Tamil/Sanskrit bhagavatī (see node 12).\",\n          \"derivation_fa\": \"این گره نیز خالی و گذرگاه است: نمایندهٔ pagode پرتغالی که نخستین‌بار در گزارش باربوسا (۱۵۱۶ م) آمده است («معابدشان را pagodes می‌خوانند»، نقل هابسن‌جابسن ص ۶۵۵) و اتیمانلاین نیز آن را از آغاز سدهٔ شانزدهم می‌داند. همین صورت پرتغالی سرچشمهٔ همهٔ صورت‌های اروپایی است؛ لوکوچ (شمارهٔ ۳۷۳) فهرست می‌کند: pagoda پرتغالی، pagoda/pagode انگلیسی، Pagode آلمانی، pagodo ایتالیایی، pagoda رومانیایی و لهستانی. آنچه هنوز حل نشده این است که پرتغالی‌ها کدام واژه را برگردانده‌اند: «بتکده»ی فارسی یا bhagavatī تامیلی‑سنسکریت (نگاه کنید به گرهٔ ۱۲).\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pagoda\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"p. 655\", \"stance\": \"supports\", \"note\": \"Barbosa 1516: 'they call their temples pagodes, and they are separate from the others'; Ramusio's Italian 'le quali chiamano Pagodes'.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 373, pp. 30–31\", \"stance\": \"supports\", \"note\": \"'der pg. Ausdruck pagoda, engl. pagoda, pagode, dtsch. Pagode, it. pagodo, rum. pagoda, poln. pagoda' — Portuguese as the pivot.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"English\",\n          \"words\": \"pagoda : prayer house\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"English pagoda (pagode, pagody 1580s; modern form 1630s) is from Portuguese pagode. The Persian route Nourai draws — but 'idol' + kada 'house' → but-kada → Port. pagode → Eng. pagoda — is one of two etymologies that are still live, and it is the one Lokotsch, Littré, Reinaud, Burnell and Whitworth adopt. The competing derivation is from Tamil pagavadi / Sanskrit bhagavatī 'goddess' (Yule's view; PIE *bʰag- 'to apportion', an entirely different root). Etymonline keeps both: 'from Portuguese pagode (early 16c.), perhaps from a corruption of Persian butkada, from but \\\"idol\\\" + kada \\\"dwelling.\\\" Or perhaps from or influenced by Tamil pagavadi \\\"house belonging to a deity,\\\" from Sanskrit bhagavati \\\"goddess\\\"'. Hobson-Jobson, which Nourai cites, prints the two contributors disagreeing with each other on exactly this point ('There can be little doubt that the origin really lies between these two'). The phonetic objection to the Persian route is that but-kada does not easily give the -go- and the final -e of the earliest Portuguese pagode. Verdict plausible, not confirmed.\",\n          \"derivation_fa\": \"«pagoda» انگلیسی (نخست pagode و pagody در دههٔ ۱۵۸۰، صورت امروزی از ۱۶۳۰) از pagode پرتغالی است. مسیری که نورایی کشیده — «بت» + «کده» ← بتکده ← pagode پرتغالی ← pagoda انگلیسی — یکی از دو ریشه‌شناسی زندهٔ این واژه است و همان است که لوکوچ، لیتره، رنو، برنل و ویتورث پذیرفته‌اند. ریشه‌شناسی رقیب آن را از pagavadi تامیلی و bhagavatī سنسکریت «الهه» می‌داند (رأی یول)، که از ریشهٔ یکسره دیگری (*bʰag- «بخش کردن») است. اتیمانلاین هر دو را نگاه داشته است. در «هابسن‌جابسن» — همان صفحه‌ای که نورایی به آن ارجاع داده — دو نویسندهٔ کتاب آشکارا بر سر همین نکته با یکدیگر اختلاف دارند و می‌نویسند «تردید اندکی هست که خاستگاه واقعی میان این دو است». ایراد آوایی بر مسیر فارسی آن است که از but-kada به‌آسانی ‑go‑ و ‑e پایانی کهن‌ترین صورت پرتغالی به دست نمی‌آید. پس: با احتیاط پذیرفتنی، نه قطعی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/pagoda\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SKT:366\", \"status\": \"not_found\", \"note\": \"Skeat's Concise (1911, SKT.txt) has no PAGODA headword at all; grep -i 'pagod' yields a single hit, in the appendix 'VI. Distribution of Words' — 'Portuguese from Persian: pagoda, veranda?' — at leaf 639 ≈ printed p. 619, not p. 366 (leaf 387 ≈ p. 361–366 holds POCK/POEM/POESY). That appendix does back the Persian route, but the page number does not match this edition.\"},\n            {\"ref\": \"LKT:30\", \"status\": \"supports\", \"note\": \"LKT.txt line 1017, leaf 57 ≈ printed p. 31 (entry no. 373 begins on p. 30): 'Pers. batkādā: \\\"Götzentempel\\\" [aus pers. but \\\"Götzenbild\\\" … und kädä \\\"Haus\\\"]; hieraus ergab sich durch Kontamination mit prākṛta bhagodi \\\"göttlich, heilig\\\" … der pg. Ausdruck pagoda, engl. pagoda …' and it closes '[Hobson-Jobson 652/657]' — the very cross-reference Nourai repeats.\"},\n            {\"ref\": \"AID:233\", \"status\": \"supports\", \"note\": \"AID.txt line 5145, leaf 251 (leaf = printed + 18, so p. 233): 'Pagoda. [According to Webster from the Persian but, an idol, and kodak, a house; but perhaps only a corrup[tion] …]'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"pp. 652–655 s.v. PAGODA\", \"stance\": \"partial\", \"note\": \"'a fifth makes it a corruption of the Pers. but-kadah, \\\"idol-temple\\\" … There can be little doubt that the origin really lies between these two' — Hobson-Jobson leaves Persian and bhagavatī undecided, with Burnell for Persian and Yule for bhagavatī.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 373\", \"stance\": \"supports\", \"note\": \"explicitly prefers the Persian etymology and dismisses dagoba, pagão and Chinese pai-ku-ta as 'weniger wahrscheinlich'.\"},\n            {\"src\": \"SKT\", \"where\": \"Distribution of Words, p. ~619\", \"stance\": \"supports\", \"note\": \"'Portuguese from Persian: pagoda, veranda?' — Skeat classes pagoda as Persian via Portuguese, though not on the page Nourai cites.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"bhu : become be ; bhŭta : a being, ghost, phantom\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. bhū- 'to be, become' (present bhávati) is the Indic reflex of *bʰuH-, and bhūtá- is its past participle *bʰuH-tó- 'become, been', substantivised as bhūtá-m 'a being, creature' and, in the popular religion, 'ghost, spirit'. The Avestan cognate būta- of node 1 and Latin -fu-tūrus stand at exactly the same point in the paradigm. Nourai's semantic note 'a being, phantom, ghost' matches the Sanskrit lexicons; the ghost sense is a secondary Indian development from 'being' and is the sense that later fed the Bundahišn identification discussed at node 7.\",\n          \"derivation_fa\": \"ریشهٔ bhū- سنسکریت «بودن، شدن» (زمان حال bhávati) بازتاب هندیِ *bʰuH- است و bhūtá- صفت مفعولی آن یعنی *bʰuH-tó- «شده، بوده» که سپس به‌صورت اسم bhūtá-m «موجود، آفریده» و در باورهای عامیانه «روح، شبح» به کار رفته است. هم‌ریشهٔ اوستایی آن būta- (گرهٔ ۱) و لاتینی ‑fu‑tūrus دقیقاً در همین جایگاه صرفی‌اند. معنایی که نورایی داده با فرهنگ‌های سنسکریت می‌خواند؛ معنای «شبح» تحوّلی ثانوی و هندی از «موجود» است و همان است که بعدها این‌همانیِ بندهش را (نگاه کنید به گرهٔ ۷) پدید آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:146\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 155, p. 146: 'Ai. bhávati \\\"ist, ist da, geschieht, gedeiht, wird\\\"' and 'ai. bhūtá-ḥ, av. būta- \\\"geworden, seiend\\\", ai. bhūtá-m \\\"Wesen\\\"'.\"},\n            {\"ref\": \"SYN:1503\", \"status\": \"not_found\", \"note\": \"as at node 7: leaf 1527 of SYN.txt (= printed 1503 by the file's stated offset) falls in Buck's Law chapter, and grep for 'bhūta' across the whole file finds nothing.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 146\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. bheuə\", \"stance\": \"supports\", \"note\": \"Mann IEC.txt line 1280: 'bheuə (bhou- bhū-) \\\"be\\\" … Skt. bhávāmi; Av. bavai(mi)'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə-\", \"stance\": \"supports\", \"note\": \"zero-grade *bhu-, *bhū- is the form underlying the Indic material.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through node standing for Proto-Germanic. The root survives in Germanic in three shapes that Pokorny sets out on p. 149: the *bheu-yō present *biju- (OE bēo 'I am'), the lengthened o-grade *bhōw- in *būaną 'to dwell, cultivate' (Goth. bauan, ON búa, OHG būan), and the zero-grade *bhū- in the nouns of dwelling *būraz (OE būr 'chamber'), *bōþlą / *buþlą (OE bold, botl 'dwelling') and *būþō (ON búð, MLG bōde 'booth'). The box carries no words, so nothing here can be wrong; the derivations are checked at node 15.\",\n          \"derivation_fa\": \"این گره خالی و نمایندهٔ ژرمنی آغازین است. ریشهٔ *bʰuH- در ژرمنی سه صورت دارد که پوکورنی در ص ۱۴۹ برمی‌شمارد: زمان حالِ *bhu-i̯ō یعنی *biju- (انگلیسی کهن bēo «هستم»)، درجهٔ کشیدهٔ *bhōw- در *būaną «سکونت گزیدن، آباد کردن» (گوتی bauan، نورس کهن búa، آلمانی علیای کهن būan)، و درجهٔ صفر *bhū- در نام‌های مسکن: *būraz (انگلیسی کهن būr «اتاق»)، *bōþlą/*buþlą (bold و botl «خانه») و *būþō (نورس کهن búð، آلمانی سفلای میانه bōde «کلبه»). چون در کادر واژه‌ای چاپ نشده، خطایی هم در آن نیست؛ ارزیابی مشتقات در گرهٔ ۱۵ آمده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 149\", \"stance\": \"supports\", \"note\": \"'got. bauan \\\"wohnen, bewohnen\\\", ahd. būan … aisl. búð f. \\\"Wohnung, Zelt, Hütte\\\"; aschwed. bōþ, mnd. bōde, mhd. buode und būde \\\"Hütte, Gezelt\\\", nhd. Bude … ags. bold und botl n. \\\"Wohnung, Haus\\\", *byldan, engl. to build \\\"bauen\\\" … ags. bēo \\\"ich bin\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- II–IV\", \"stance\": \"supports\", \"note\": \"'Lengthened o-grade form *bhōw- in Germanic *bōwan' and 'Zero-grade form *bhū- … Germanic *būram, dweller … Germanic *būrjam, dwelling'.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"be, build, beam, booth, boom, husband, neighbor, arbor, herb, bower\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Eight of the ten are correct and are exactly the words Watkins files under bheuə-: BE (OE bēon < *bhwiyo-), BUILD (OE bold/byldan < *bhu-tlo-), BOOTH (via ME bothe from Old Danish bōth < *bhō[u]-tā), BOOM² 'a spar' (Middle Dutch boom 'tree' < *bhou(ə)mo-), HUSBAND (ON hús-bóndi, bóndi being the participle of búa 'to dwell'), NEIGHBOR (OE gebūr 'dweller' + nēah 'near'), BOWER¹ (OE būr 'dwelling space, chamber'), and BEAM (OE bēam 'tree, beam', from the same *bhou(ə)mo-, though Pokorny prefixes 'Vielleicht' and Watkins 'Possibly'). Two are wrong. ARBOR 'a shady retreat' is from Middle English herbier, Old French herbier, Latin herbārium, from herba: Klein, 'arbor, arbour, n., a shady retreat. — fr. earlier arber, fr. ME. herbier, \\\"a garden of herbs\\\", fr. OF. herbier, fr. L. herbarium … The change of arber to arbor, arbour is due to a confusion with L. arbor \\\"tree\\\"'; the AHD index files ARBOR under koro- (via harbour), not under bheuə-. HERB is Latin herba, 'which is of uncertain origin' (Klein) and does not appear in the AHD root appendix at all. Neither belongs to Bheu.\",\n          \"derivation_fa\": \"هشت واژه از ده واژهٔ این کادر درست است و دقیقاً همان‌هایی است که واتکینز زیر bheuə- آورده: be (انگلیسی کهن bēon از *bʰwi-yo-)، build (انگلیسی کهن bold/byldan از *bʰu-tlo-)، booth (از راه دانمارکی کهن bōth از *bʰō[u]-tā)، boom۲ «تیر بادبان» (هلندی میانه boom «درخت»)، husband (نورس کهن hús-bóndi که bóndi اسم فاعل búa «سکونت گزیدن» است)، neighbor (انگلیسی کهن gebūr «ساکن» + nēah «نزدیک»)، bower (انگلیسی کهن būr «اتاق، جای زیست») و beam (انگلیسی کهن bēam «درخت، تیر»، هرچند پوکورنی با «شاید» و واتکینز با «possibly» آورده‌اند). اما دو واژه نادرست است: arbor «سایه‌بان، آلاچیق» از انگلیسی میانهٔ herbier و فرانسهٔ کهن herbier و لاتینی herbārium از herba است — کلاین می‌نویسد تبدیل arber به arbor از خلط با arbor لاتینی «درخت» پدید آمده — و در نمایهٔ AHD زیر koro- ثبت شده نه bheuə-؛ و herb نیز از herba لاتینی است که به گفتهٔ کلاین «خاستگاهش نامعلوم است» و اصلاً در پیوست ریشه‌های AHD نیامده. هیچ‌یک از این دو به ریشهٔ Bheu تعلق ندارد؛ در این دو مورد پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt line 340 s.v. bheuə- yields BE, BOOTH, BUILD, BOODLE, BOWER¹, NEIGHBOR, BOOR, BYRE, FUTURE, PHYSIC, PHYLUM, BONDAGE/HUSBAND, and 'VI. Possibly Germanic *baumaz (and *bagmaz), tree … BEAM; … BOOM²'. The index confirms 'BEAM bheue-', 'BOOM² bheue-', 'BUILD bheue-', 'HUSBAND bheue-', 'BE bheue-', 'PHYSIC bheue-'. It also shows 'ARBOR koro-' — i.e. AHD does not put arbor under this root — and has no index line for HERB at all.\"},\n            {\"ref\": \"POK:149\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 155, printed p. 149: 'got. bauan … aisl. búð f. \\\"Wohnung\\\" … mnd. bōde, mhd. buode und būde \\\"Hütte\\\", nhd. Bude … ags. bold und botl n. \\\"Wohnung, Haus\\\", *byldan, engl. to build … ahd. nāhgibūr, ags. nēahgebūr, nhd. Nachbar, engl. neighbour … ags. bēo \\\"ich bin\\\" … Vielleicht got. bagms, ahd. boum, ags. bēam \\\"Baum\\\"'. Pokorny's p. 149 covers be, build, booth, neighbor, bower, beam/boom — but not arbor or herb.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. arbor, arbour and s.v. herb\", \"stance\": \"contradicts\", \"note\": \"'arbor, arbour, n., a shady retreat. — fr. earlier arber, fr. ME. herbier, \\\"a garden of herbs\\\", fr. OF. herbier, fr. L. herbarium, of s.m., fr. herba, \\\"herb\\\"' (KLN_1971.txt line 18659) and 'herb, n. — ME. herbe, erbe, fr. OF. erbe, fr. L. herba, \\\"grass, herb\\\", which is of uncertain origin' (line 112521).\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins index\", \"stance\": \"partial\", \"note\": \"'ARBOR koro-'; no HERB entry — see ref_check.\"},\n            {\"src\": \"POK\", \"where\": \"p. 149\", \"stance\": \"partial\", \"note\": \"supports the eight Germanic words, silent on arbor and herb.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Greek\",\n          \"words\": \"phuein : to make grow\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. φύω phúō 'I bring forth, make grow', middle φύομαι 'I grow, become', aorist ἔφυν (= Skt. ábhūt, Lat. fuī), is the direct Greek continuation of *bʰuH-. Pokorny p. 147: 'Gr. φύω (lesb. φυίω …) \\\"zeuge\\\" (Aor. ἔφυσα), φύομαι \\\"werde, wachse\\\"'; Watkins: 'Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature'. Nourai's infinitive citation form phuein and the gloss 'to make grow' are Watkins' own wording, and the derivatives φύσις 'nature', φυτόν 'plant', φῦλον 'tribe' all belong here.\",\n          \"derivation_fa\": \"φύω یونانی «می‌رویانم، پدید می‌آورم»، در وجه میانی φύομαι «می‌رویم، می‌شوم» و ماضی ساده ἔφυν (برابر ábhūt سنسکریت و fuī لاتینی)، دنبالهٔ مستقیم *bʰuH- در یونانی است. پوکورنی در ص ۱۴۷ می‌نویسد «gr. φύω … \\\"zeuge\\\"، φύομαι \\\"werde, wachse\\\"» و واتکینز نیز «phuein، to bring forth, make grow» آورده است — یعنی صورت مصدری و معنایی که نورایی نوشته واژه‌به‌واژه از واتکینز است. مشتقات φύσις «طبیعت»، φυτόν «گیاه» و φῦλον «تیره» همگی از همین ریشه‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 340, s.v. bheuə- III.2: 'Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE …'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 147\", \"stance\": \"supports\", \"note\": \"'Gr. φύω … \\\"zeuge\\\" (Aor. ἔφυσα), φύομαι \\\"werde, wachse\\\" … φυτόν \\\"Gewächs, Pflanze\\\", φύσις \\\"Natur\\\", φῦλον n. \\\"Stamm, Geschlecht, Art\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- III.2\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. bheuə\", \"stance\": \"supports\", \"note\": \"Mann groups the Greek forms with Skt. bhávāmi and Av. bavai(mi) under the same root.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"physics\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"From Gk. φύσις phúsis 'growth, nature' (the -sis abstract to φύω) came τὰ φυσικά ta phusiká, the title given to Aristotle's treatises on nature; Latin physica, Old French fisique 'medical science' (whence English physic 'medicine', 13th c.), and in the 1580s–1590s English physics as a plural noun after the Greek and Latin titles, its modern restriction to the science of matter and energy settling in the 17th century. Watkins files PHYSIC, PHYSIO-, PHYSIQUE and -PHYTE under bheuə- III.2 with phuein/phusis, so the arrow Greek → English is exactly AHD's.\",\n          \"derivation_fa\": \"از φύσις یونانی «رویش، طبیعت» (اسم مصدر ‑σις از φύω) عنوان τὰ φυσικά برای رساله‌های طبیعیات ارسطو ساخته شد؛ از آنجا physica لاتینی، fisique فرانسهٔ کهن به معنی «دانش پزشکی» (که physic انگلیسی در سدهٔ سیزدهم از آن آمد) و سرانجام در دههٔ ۱۵۸۰–۱۵۹۰ صورت جمع‌نمای physics در انگلیسی به پیروی از عنوان یونانی و لاتینی. محدود شدن آن به دانش ماده و انرژی در سدهٔ هفدهم قطعی شد. واتکینز واژه‌های PHYSIC و PHYSIO- و PHYSIQUE را در همان بند bheuə- در کنار phuein و phusis آورده است؛ پس پیکان «یونانی ← انگلیسی» همان چیزی است که AHD می‌گوید. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0uH-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; the parent box's AHD citation covers it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- III.2 and index 'PHYSIC bheue-'\", \"stance\": \"supports\", \"note\": \"'phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON'.\"},\n            {\"src\": \"POK\", \"where\": \"p. 147\", \"stance\": \"supports\", \"note\": \"'mit ū gr. φύσις' — Pokorny derives φύσις from the lengthened zero grade of the same root.\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Latin\",\n          \"words\": \"futurus : that is to be ; pro-bhwo : growing forward ; super-bhwo : being above ; tri-bhu : third being, the third, a section of the Roman empire\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four are secure. Latin futūrus 'about to be' is the future participle supplied to sum from *bhu-tu-ro- (Watkins: 'Suffixed form *bhu-tu- in Latin futūrus, \\\"that is to be\\\", future'), beside fuī 'I have been' < *fū-ai and fīō 'I become' < *bhu-yō. probus 'upright, good' is *pro-bhw-o- 'growing well or straightforward' (Watkins under per¹, cross-referring to bheuə-); superbus 'proud' is *super-bhw-o- 'being above' (Watkins under uper). The fourth is doubtful: Latin tribus, the division of the Roman citizen body (three original tribes: Ramnes, Tities, Luceres), is analysed by many as *tri- + *bhu- 'three-fold being', but Etymonline, following de Vaan, calls the word 'of unknown origin' and says only that 'the first element generally is held to be tri- \\\"three\\\", and the whole to represent a PIE indication of \\\"tripartite division\\\"'; an alternative connects it with *treb- 'dwelling' (Umbrian trifu). Nourai's gloss 'a section of the Roman empire' is also loose — tribus is a division of the citizen body of the Republic, long predating the empire.\",\n          \"derivation_fa\": \"سه واژه از چهار واژه استوار است. futūrus لاتینی «آنچه خواهد بود» صفت فاعلی آیندهٔ فعل sum است از *bhu-tu-ro-، در کنار fuī «بوده‌ام» از *fū-ai و fīō «می‌شوم» از *bhu-yō. probus «راست، نیک» همان *pro-bhw-o- «نیک‌رونده» است و superbus «گردن‌فراز» همان *super-bhw-o- «بالانشین»؛ واتکینز هر دو را با ارجاع به bheuə- آورده است. اما واژهٔ چهارم مورد تردید است: tribus لاتینی، نام بخش‌های پیکرهٔ شهروندان رم (سه تیرهٔ نخستین: رامنس، تیتیس، لوکرس)، را بسیاری *tri- + *bhu- «سه‌بخشی» تحلیل کرده‌اند، ولی اتیمانلاین به پیروی از دِ فان آن را «با خاستگاه ناشناخته» می‌خواند و تنها می‌گوید «جزء نخست را عموماً tri- \\\"سه\\\" می‌دانند». تحلیل دیگری آن را با *treb- «خانه، جایگاه» (اومبریایی trifu) می‌سنجد. افزون بر این، توضیح نورایی («بخشی از امپراتوری روم») دقیق نیست: tribus بخشی از پیکرهٔ شهروندان دوران جمهوری است و سده‌ها پیش از امپراتوری وجود داشته. حکم: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tribe\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. bheuə- V: '*du-bhw-io- … *pro-bhw-o-, \\\"growing well or straightforward\\\" (see per¹). 3. *super-bhw-o-, \\\"being above\\\", in Latin superbus' and IV.4 '*bhu-tu- in Latin futūrus'. Latin tribus, however, is NOT in the bheuə- entry, and Watkins' trei- entry (Three) lists TREY, TRIO, THIRD, TERTIUS … but no TRIBE; the index line reads 'TRIBE tere-'. So AHD supports futurus, probus and superbus but not tri-bhu.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 148–149\", \"stance\": \"partial\", \"note\": \"'Lat. fuī (alat. fūī) \\\"bin gewesen\\\" aus *fū-ai … fu-tūrus \\\"künftig\\\" … probus \\\"gut gedeihend, redlich\\\" (*pro-bhuos : ai. pra-bhū-ḥ \\\"hervorragend\\\") … lat. superbus \\\"hochmütig\\\"'. Pokorny gives futurus, probus and superbus; tribus does not appear.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- IV.4, V.2–3\", \"stance\": \"partial\", \"note\": \"see ref_check.\"},\n            {\"src\": \"SYN\", \"where\": \"chapter 21 (Law), s.v. tribunal\", \"stance\": \"partial\", \"note\": \"SYN.txt leaf 1528: 'Lat. tribunal \\\"the raised platform on which seats of magistrates were placed\\\" (: tribūnus \\\"tribune\\\", orig. \\\"magistrate of the tribe, tribus\\\")' — Buck derives tribunus from tribus but offers no PIE analysis of tribus.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"English\",\n          \"words\": \"future ; prove ; superb ; tribe, tribune, contribute\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"future: Latin futūrus → Old French futur → Middle English futur (14th c.) → future. prove: Latin probāre 'to test, judge good', denominative of probus, → Old French prover → Middle English proven; the noun proof shows the same base. superb: Latin superbus → French superbe → English superb (1540s, first 'noble, magnificent'). tribe/tribune/contribute all rest on Latin tribus: tribūnus 'officer of a tribe' → Old French tribun → tribune; contribuere 'to bring together, add to' (com- + tribuere 'to allot, pay tribute', itself denominative of tribus) → contribute; tribus → Old French tribu → English tribe (mid-13th c., first of the twelve tribes of Israel, generalised to ethnic groups by the 1590s). Every step from Latin onward is well documented; the node inherits the uncertainty of its parent, since if tribus is not *tri-bhu- then tribe, tribune and contribute do not belong to this root at all.\",\n          \"derivation_fa\": \"future: از futūrus لاتینی به futur فرانسهٔ کهن و از آنجا به انگلیسی میانه (سدهٔ چهاردهم) و سپس future. prove: از probāre لاتینی «آزمودن، نیک شمردن» — فعل ساخته‌شده از probus — به prover فرانسهٔ کهن و proven انگلیسی میانه؛ اسم proof نیز از همین ستاک است. superb: از superbus لاتینی به superbe فرانسوی و superb انگلیسی (دههٔ ۱۵۴۰، نخست به معنی «باشکوه»). tribe و tribune و contribute هر سه بر tribus لاتینی استوارند: tribūnus «کارگزار تیره» ← tribun فرانسهٔ کهن ← tribune؛ contribuere «باهم آوردن، افزودن» (com- + tribuere که خود از tribus است) ← contribute؛ و tribus ← tribu فرانسهٔ کهن ← tribe انگلیسی (میانهٔ سدهٔ سیزدهم، نخست دربارهٔ دوازده سبط بنی‌اسرائیل و از دههٔ ۱۵۹۰ برای اقوام). همهٔ گام‌ها از لاتینی به بعد مستند است؛ ولی این گره تردیدِ گرهٔ پدر را به ارث می‌برد: اگر tribus از *tri-bhu- نباشد، tribe و tribune و contribute اصلاً به این ریشه تعلق ندارند. حکم: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/tribe\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins gives FUTURE under bheuə- IV.4, PROVE under per¹ (from the compound *pro-bhw-o-) and SUPERB under uper (from *super-bhw-o-); the index lines read 'FUTURE bheue-', 'PROVE es-, PROVE per', 'SUPERB uper'. TRIBE is indexed as 'TRIBE tere-' and is absent from the bheuə- entry, so AHD does not support the tribe/tribune/contribute limb.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins index and s.v. per¹, uper\", \"stance\": \"partial\", \"note\": \"'*pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheuə-), in Latin probus … PROBE, PROBITY, (PROOF), PROVE' (s.v. per¹) and '*super-bhw-o-, \\\"being above\\\" (*bhw-o-, being; see bheuə-), in Latin superbus … SUPERB' (s.v. uper).\"},\n            {\"src\": \"SKT\", \"where\": \"Concise Etym. Dict.\", \"stance\": \"silent\", \"note\": \"no entry retrievable for tribe/tribune in the local OCR that bears on the PIE analysis.\"},\n            {\"src\": \"SYN\", \"where\": \"chapter 21, tribunal\", \"stance\": \"partial\", \"note\": \"'tribūnus \\\"tribune\\\", orig. \\\"magistrate of the tribe, tribus\\\"' — confirms the Latin word-family but not its root.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T14:34:12.316Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-94.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T14:34:16.802Z] TOOL CALL #68: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-94.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 94",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-05T14:34:19.498Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'confirmed': 6, 'disputed': 4, 'plausible': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 13, 'not_found': 7, 'partial': 9, 'not_checked': 7}
books consulted: {'supports': 28, 'silent': 5, 'contradicts': 4, 'partial': 15} | by book: {'AHD': 8, 'POK': 8, 'PHD': 5, 'BRT': 4, 'MON': 4, 'LKT': 3, 'HJB': 3, 'KNT': 2, 'BQT': 2, 'HUB': 2, 'SKT': 2, 'IEC': 2, 'SYN': 2, 'NYB': 1, 'SOD': 1, 'HRN': 1, 'AID': 1, 'KLN': 1}
```


## [2026-09-05T14:34:42.885Z] AGENT

Done. `data/verification/page-94.json` written and validated; `verify_check.py 94` reports 19/19 nodes and **0 PROBLEM lines**.

**Page 94 (book p. 64) — one entry, root "Bheu 3" [Indo-European] "to exist, grow"**

Verdicts: root `confirmed`; nodes — confirmed 6, plausible 8, disputed 4, transcription_suspect 1.
Ref checks: supports 13, partial 9, not_found 7, not_checked 7. Books consulted: POK, AHD, WLD, IEC, SYN, KNT, BRT, PHD, NYB, HRN, HUB, SOD, BQT, MON, KLN, SKT, LKT, AID, HJB.

Disputed / suspect items:
- **#3 Av./OP `urvarâ` "plant"** — Av. *urvarā-* (BRT: "urvarā- f. 'Pflanze'") continues Proto-Iranian *(H)urwarā-, cognate with Skt. *urvárā* "fertile field"; it is absent from Pokorny's whole bheu- entry. Also `bŭmî-mathan` is unattested in Kent/Bartholomae — a back-projection of NP بومهن.
- **#8 Av. `bŭiti-kata` "idol house"** — no such Avestan compound exists; Lokotsch 373 derives Pers. *batkādā* from NP *but* + *kada*, i.e. a New Persian compound of Islamic date.
- **#9 Persian `bot` «بت»** — modern view: MP *but* "Buddha; idol" (MacKenzie) ← Skt. *buddha*, via Buddhist Eastern Iran; Nourai follows Horn no. 182 (who himself hedged) and the Bundahišn identification of the daēva Būiti with the Buddha-idol. Nourai's own note "See Pwt" flags it.
- **#15 English `arbor, herb`** — Klein: *arbor* < ME *herbier* < L. *herbārium* < *herba*; *herb* < L. *herba*, "of uncertain origin". AHD indexes ARBOR under *koro-*, has no HERB root at all. The other eight words (be, build, beam, booth, boom, husband, neighbor, bower) are correct per AHD/POK 149.
- **#6 Sogdian `bwmb`** (transcription_suspect) — Gharib no. 2911 (p. 114/115) prints **βwmh** "earth, world < OP būmī". `error_in: "book"` — the 300 dpi page render clearly shows "bwmb", so the extraction is faithful and the misprint is Nourai's. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/94.png`.

Citation problems found in Nourai's own refs:
- `BQT:111` (nodes 1, 2, 3) — Borhan p. 111 carries the اسپـ headwords; nothing on bav-/būdan. `not_found`.
- `BQT:223` (node 7) — p. 223 has باشـ/باغـ entries; the Būiti footnote is on p. 234. Likely a slip for the "233" in his own NOTE.
- `SKT:366` (node 12) — Skeat's Concise has no PAGODA headword; the only mention is the appendix "Portuguese from Persian: pagoda" at p. ~619.
- `SYN:1503` (nodes 7, 13) — Buck p. 1503 falls in the Law chapter; no bhūta/būiti material anywhere in the file.
- Confirmed exact: POK:146/147/149, KNT:200 (Kent's Lexicon s.v. būmi-), SOD:115, BQT:314 (Mo'in's būdan footnote), BQT:320 (بومهن + the Asadi Tusi verse Nourai quotes), BQT:234 (بت), LKT:30, AID:233, HJB:652.

Extraction errors for the owner to fix (JSON vs printed page): only one, trivial — node 5 has «اورْوَر» (sukūn) where the page prints «اورَوَر» (fatḥa). Everything else on the page matches the JSON exactly.
