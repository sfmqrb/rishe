# Verification process log — verify-page-124


## [2026-09-05T18:21:42.768Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 124 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-124.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-124.json. Write /home/sfmqrb/git/rishe/data/verification/page-124.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 124` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:21:43.889Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:21:44.553Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:21:44.572Z] TOOL RESULT

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


## [2026-09-05T18:21:45.130Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-124.txt"
}
```


### [2026-09-05T18:21:45.149Z] TOOL RESULT

```
1	=== PDF page 124 (book page 94) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dhě 2 : to do, set  (refs AHD:1512; POK:235)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:235 | ma[n]dz-dha : done learning, wise ☞Men 1 ; ahura-mazdha : wise spirit (God) ☞An 1,Men 1
5	  #2 (parent #1) [Persian] refs=KLN:1095 | Mazdâ «مزدا» : wise (God) ; Ahûrâmazdâ «اهورا مزدا» : God
6	#3 (parent #0) [Avestan] refs=BQT:169,418; POK:238 | dâman 2 : statute ; han-dâma : put together, shape ☞Sem ; paiti-dâma : protection for body ☞Pa
7	  #4 (parent #3) [Pahlavi] refs=None | handâm : figure ; pa-dâm, panum : a cloth mouthpiece worn to protect the holy fire
8	    #5 (parent #4) [Persian] refs=MON:813 | andâm «اندام» : body, shape ; panâm «پنام» : a protective mouthpiece ; panâmîdan «پنامیدن» : to prevent, deprive
9	#6 (parent #0) [Avestan] refs=POK:235; HRN:236; KNT:168; FFD:52 | dâta 1, dâ 1 : to put, set ; ni-dâ : to put down, lay down, also to hide ☞Nî 1 ; upa-ni-dâ : hidden ☞Upo ; apa-dâna : the concealed part of a palace ☞Apo
10	  #7 (parent #6) [Persian] refs=BQT:2211, 2214 | nahâdan «نهادن» : to do ; nahân «نهان» : covered, hidden ; âpâdânâ «آپادانا» : the throne room | extra: نهاد ، پنهان
11	#8 (parent #0) [Avestan] refs=POK:238 | dhana : vessel, holder, pot ; gao-dana, gao-di : milk container ☞Gwou
12	  #9 (parent #8) [Sogdian] refs=SOD:174 | gwd`k : container
13	  #10 (parent #8) [Persian] refs=BQT:818 | dân «دان ۱» : vessel, holder | extra: گلدان ، زهدان ، چمدان | NOTE: Note that "-dân" in Persian "nâv-dân: water gutter", is from a different root (see Dâ 2 ).
14	#11 (parent #0) [Avestan] refs=POK:235; FFD:52 | dâ 2 : to settle, to give ; dâtô, dâta 3 : that which is settled, law ; dâtô-vare : carrier of judgment, judge ☞Bher 1
15	  #12 (parent #11) [Persian] refs=BQT:807,814,821; HRN:118; NYB:60 | dâd «داد» : justice ; dâvar «داور» : judge, referee | extra: دادسرا ، دادستان ، دادرس | NOTE: NYB:60 derives "dâd" from "dâdan:to give one's right"
16	  #13 (parent #11) [Pahlavi] refs=HRN:127 | dast-war : judge, priest ; dâtastân : law, a legal case (story) | NOTE: NYB:59 claims "dastwar" from Avestan "dah:to teach"
17	    #14 (parent #13) [Persian] refs=BQT:862 | dastûr «دستور» : story, priest, agenda ; dâstân «داستان» : story | extra: دستان
18	
```


## [2026-09-05T18:21:49.017Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-124.json",
 "description": "Read source JSON for page 124"
}
```


### [2026-09-05T18:21:49.058Z] TOOL RESULT

```
{
  "pdf_page": 124,
  "book_page": 94,
  "entries": [
    {
      "root": {
        "name": "Dhě 2",
        "lang": "Indo-European",
        "refs": "AHD:1512; POK:235",
        "gloss": "to do, set"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:235",
          "words": [
            {"translit": "ma[n]dz-dha", "gloss": "done learning, wise", "script": null, "see": ["Men 1"]},
            {"translit": "ahura-mazdha", "gloss": "wise spirit (God)", "script": null, "see": ["An 1", "Men 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "KLN:1095",
          "words": [
            {"translit": "Mazdâ", "gloss": "wise (God)", "script": "مزدا"},
            {"translit": "Ahûrâmazdâ", "gloss": "God", "script": "اهورا مزدا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:169,418; POK:238",
          "words": [
            {"translit": "dâman 2", "gloss": "statute", "script": null},
            {"translit": "han-dâma", "gloss": "put together, shape", "script": null, "see": ["Sem"]},
            {"translit": "paiti-dâma", "gloss": "protection for body", "script": null, "see": ["Pa"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "handâm", "gloss": "figure", "script": null},
            {"translit": "pa-dâm, panum", "gloss": "a cloth mouthpiece worn to protect the holy fire", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:813",
          "words": [
            {"translit": "andâm", "gloss": "body, shape", "script": "اندام"},
            {"translit": "panâm", "gloss": "a protective mouthpiece", "script": "پنام"},
            {"translit": "panâmîdan", "gloss": "to prevent, deprive", "script": "پنامیدن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "بتا نگارا از چشم بد بترس همی - چرا نداری باخویشتن همی تو پنام",
            "poet": "Shahîd Balkhî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:235; HRN:236; KNT:168; FFD:52",
          "words": [
            {"translit": "dâta 1, dâ 1", "gloss": "to put, set", "script": null},
            {"translit": "ni-dâ", "gloss": "to put down, lay down, also to hide", "script": null, "see": ["Nî 1"]},
            {"translit": "upa-ni-dâ", "gloss": "hidden", "script": null, "see": ["Upo"]},
            {"translit": "apa-dâna", "gloss": "the concealed part of a palace", "script": null, "see": ["Apo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:2211, 2214",
          "words": [
            {"translit": "nahâdan", "gloss": "to do", "script": "نهادن"},
            {"translit": "nahân", "gloss": "covered, hidden", "script": "نهان"},
            {"translit": "âpâdânâ", "gloss": "the throne room", "script": "آپادانا"}
          ],
          "script_extra": "نهاد ، پنهان",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:238",
          "words": [
            {"translit": "dhana", "gloss": "vessel, holder, pot", "script": null},
            {"translit": "gao-dana, gao-di", "gloss": "milk container", "script": null, "see": ["Gwou"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Sogdian",
          "refs": "SOD:174",
          "words": [
            {"translit": "gwd`k", "gloss": "container", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT:818",
          "words": [
            {"translit": "dân", "gloss": "vessel, holder", "script": "دان ۱"}
          ],
          "script_extra": "گلدان ، زهدان ، چمدان",
          "note": "Note that \"-dân\" in Persian \"nâv-dân: water gutter\", is from a different root (see Dâ 2 ).",
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:235; FFD:52",
          "words": [
            {"translit": "dâ 2", "gloss": "to settle, to give", "script": null},
            {"translit": "dâtô, dâta 3", "gloss": "that which is settled, law", "script": null},
            {"translit": "dâtô-vare", "gloss": "carrier of judgment, judge", "script": null, "see": ["Bher 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "BQT:807,814,821; HRN:118; NYB:60",
          "words": [
            {"translit": "dâd", "gloss": "justice", "script": "داد"},
            {"translit": "dâvar", "gloss": "judge, referee", "script": "داور"}
          ],
          "script_extra": "دادسرا ، دادستان ، دادرس",
          "note": "NYB:60 derives \"dâd\" from \"dâdan:to give one's right\"",
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "Pahlavi",
          "refs": "HRN:127",
          "words": [
            {"translit": "dast-war", "gloss": "judge, priest", "script": null},
            {"translit": "dâtastân", "gloss": "law, a legal case (story)", "script": null}
          ],
          "script_extra": null,
          "note": "NYB:59 claims \"dastwar\" from Avestan \"dah:to teach\"",
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "BQT:862",
          "words": [
            {"translit": "dastûr", "gloss": "story, priest, agenda", "script": "دستور"},
            {"translit": "dâstân", "gloss": "story", "script": "داستان"}
          ],
          "script_extra": "دستان",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T18:21:49.183Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:21:49.221Z] TOOL RESULT

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


## [2026-09-05T18:22:20.021Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AHD','POK','KLN','BQT','MON','HRN','KNT','FFD','SOD','NYB','PHD','BRT','WLD','IEC','SYN','HUB','CHEUNG','ARY','IRN']:\n    v=d.get(k)\n    if v is None: print(k,'MISSING'); continue\n    print('==',k, json.dumps({kk:vv for kk,vv in v.items() if kk!='cites'}, ensure_ascii=False)[:900])\n\"",
 "description": "Inspect refs_online.json entries"
}
```


## [2026-09-05T18:22:21.024Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && head -c 3000 data/verification/page-66.json",
 "description": "List verification dir and sample file"
}
```


### [2026-09-05T18:22:21.613Z] TOOL RESULT

```
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 =
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": ""}
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate."}
CHEUNG MISSING
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.",
```


### [2026-09-05T18:22:21.660Z] TOOL RESULT

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
page-118.json
page-119.json
page-120.json
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
---
{
  "pdf_page": 66,
  "book_page": 36,
  "verified_by": "claude-fable-5-1",
  "verified_on": "2026-09-04",
  "entries": [
    {
      "entry": 0,
      "root": "A`.s.r",
      "verdict": "confirmed",
      "modern_form": "Arabic root ع ص ر ʿ-ṣ-r 'to press, squeeze (the juice out)'; West Semitic *ʿṣr 'to press, restrain, retain'",
      "note": "The root box is right on all three counts: the Arabic verb عَصَرَ ʿaṣara 'he pressed, squeezed' is real, the language label is right, and the gloss 'to squeeze (the juice out)' is almost word for word the gloss of the AHD Appendix of Semitic Roots ('ʿṣr — West Semitic, to press, restrain, retain … alizarin, probably from Arabic al-ʿuṣāra, the juice, from ʿaṣara, to squeeze'). Two refinements. (a) The root is not specifically Arabic but common West Semitic: AHD labels it West Semitic and Klein, s.v. alizari, compares Hebrew ʿātzar, Aramaic-Syriac ʿătzar 'he retained' — so 'Arabic' should read 'Arabic (West Semitic)'. (b) The derived noun is vocalised ʿuṣāra عُصَارَة by AHD and by Wiktionary, ʿaṣārah by Klein; Nourai follows Klein's a-vocalism ('a`sârah'), and since both variants are attested this is not an error, only a choice of source. The European branch of the chart (Sp. → Fr. → Eng. alizarin) is Klein's and AHD's account, but AHD hedges it with 'probably', Dozy explicitly declared the origin unknown, and Wiktionary/Webster's 1913 now prefer an Ottoman-Turkish route — see node #3.",
      "note_fa": "ریشهٔ «ع ص ر» به معنای «فشردن، آب چیزی را گرفتن» ریشه‌ای اصیل و درست است و برچسب زبانی و معنای آن در نمودار نورایی با آنچه پیوست ریشه‌های سامی فرهنگ American Heritage می‌آورد یکسان است؛ تنها نکته آن است که این ریشه ویژهٔ عربی نیست و سامی غربی است (کلاین هم عبری «عَصَر» به معنای «نگاه داشتن» را هم‌ریشهٔ آن می‌داند). گونهٔ اسمی آن در فرهنگ‌های امروزی عُصارة و در کلاین عَصارة ضبط شده و نورایی ضبط کلاین را برگزیده است؛ هر دو ضبط پذیرفتنی است و خطا نیست. شاخهٔ اروپایی این نمودار (اسپانیایی ← فرانسوی ← انگلیسی alizarin) از کلاین گرفته شده، ولی همان‌گونه که در گرهٔ ۳ گفته می‌شود، این بخش قطعی نیست و ویکی‌واژه امروزه راه دیگری (از راه ترکی عثمانی) پیشنهاد می‌کند. در مجموع ادعای نورایی دربارهٔ خودِ ریشه درست است.",
      "sources": [
        "https://www.ahdictionary.com/word/semitic.html",
        "https://www.ahdictionary.com/word/search.html?q=alizarin",
        "https://en.wiktionary.org/wiki/عصارة"
```


## [2026-09-05T18:22:24.626Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T18:22:24.677Z] TOOL RESULT

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
```


## [2026-09-05T18:22:34.061Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f pages: $(tr -cd '\\f' < $f | wc -c)\"; done; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==244' POK_01.txt | head -80",
 "description": "Print Pokorny leaf 244 (p.235)"
}
```


### [2026-09-05T18:22:35.664Z] TOOL RESULT

```
== POK_01.txt pages: 363
== POK_02.txt pages: 433
== POK_03.txt pages: 429
---
nen,  -ön  ,zweifach  zusammendrehen',  mhd.  ziüirn^  mnd.  tioern ,doppelt  zusammengedrehter  Faden'  wohl  =  ags.  twlrij  holl.  twijn  , Zwirn, Leinen'  (ags.  getwinne  ,bini',  getwinnas  , Zwillinge'  ist  dann  auf  *twi-nja- zurückzuführen).  Daneben  auf  Grund  eines  *ticllia-j  idg.  '^dtiei-ko-,  got. ticeihnai  ,zwei',  ags.  Dat.  tweonum^  betweonum^  engl,  betiveen  ,z wischen';
lit.  m.  PL  dvynat,  russ.  dvöjni  ,Zwillinge'.  /
Mit  -ko-:  /
ai.  dvikd-  ,aus  zweien  bestehend,  zweifach'  (dvakd-  ,paarweise  verbunden nach  ekakd-)',
ahd.  zioe(h)o,  as.  twe{}i)Oj  ags.  tweo  m.  ,Zweifel',  ags.  be-tioih,  -tioeoli ,zwischen',  mid  unc  twlh  ,zwischen  uns  beiden'  (vgl.  oben  got.  tweih-nai)]
von  duis-  aus:  ahd.  zwisk,  as.  twisk  ,zweifach',  PL  , beide'  Dat.  PL  ahd. {undar,  en)  zioisken,  nhd.  zwischen]  dazu  ags.  getwisa  m.,  as.  gitioiso,  mhd. zwiselinc  ,Zwilling'.
232
Mit  duis-  ^zweimal^  identisch  ist  diiis-  ^entzwei,  auseinander^  in  got.  tx standan  ^sich  trennen^  und  den  Ableitungen  anord.  tvistra  ^trennen^_,  m£J afries.  ticlst,  mhd.  zwist  , Zwist  (Entzweiung)^  und  mengl.  ticist  =  anoi kvistr  ^Zweig'^  (wie  auch  bair.  zioist),  ferner  anord.  kvisl  f.  , gespaltener  Zwei oder  Werkzeug,  Arm  eines  Flusses^  (dies  mit  idg.  ei)\  ferner  anord.  ^viVüc ^zweimaF,  tvistr  ^zwiespältig,  traurig^  (=  ai.  dvistJia-  ,zweideutig^ *diaTOQ  in  dLaxaC^co  ,zweifle^,  idg.  *dui{s)-sto- -.Wz.  stä-,  allenfalls  duis^i mit  formantischem  -to-),  ags.  twisla  ,Arm  eines  Flusses^,  twislian  ^zwe teilen^,  ahd.  zwisila,  nhd.  Ziviesel  ^gabelförmiger  Gegenstand,  Zweigt,  mli^ zwisel  ,doppelt^j  hierher  sehr  wahrscheinlich  ar.  dvls-  ,hassen^  (s.  untel *duei-  ,fürchten^).
6.  Idg.  Nebenform  dis-  in  lat.  dis-j  as.  afries.  te-,  ti-,  ags.  te-j  ahd.  zi-^  zt (jünger  zir-  durch  Verquickung  von  zi-  und  ir-)  ,zer-^,  got.  dis-  ,auseinau^ der^  (wohl  aus  dem  Lat.  entlehnt,  kaum  vortonig  aus  *tis-  =  lat.  du^ alb.  tsh-  z.  B.  in  tshk'ep  ,auf trennen^,  gr.  dia  (d.  i.  nach  ^asra  usw.  auS gefülltes  *Jt[(7]a),  z.  B.  dia-axilI,o)  :  lat.  discindo,  ,durch^  (,*mitten  entzwei*) als  Präf.  auch  ,durch  und  durch*  =  ,sehr^  (äol.  ^a-).
WP.  I  817 ff.,  WH.  I  104ff.,  354f.,  381  ff.,  860,  861,  Feist  484ff.,  Traut- mann  64,  Schwyzer  Gr.  Gr.  I  588  f.,  Wackernagel-Debrunner  Ai.  Gr.  III, 342  f.
Dh.
j.  dh^bb'  ;Stauiien;  betreten^  sprachlos  sein^  nasaliert  dbamb(h)-]  vermutlich als  ^geschlagen,  betroffen  sein^  aus  einer  Grundbed.  .schlagen*'. Gr.  'rdq)og  n.  .Staunen,  Verwunderung'.  Perf.  ep.  ion.  ze&rjTta,  Partiz. Aor.  tacpoyv  .erstaunen'.  d^cjjtTWy  S-üjtisvu)  (.staune  an  =)  schmeichle'  (s. Boisacq  s.  v.  d-öjxp),  nasaliert  d-d(,ißog  n.  .Staunen.  Verwunderung.  Schrecken'. i^aixßso)  .staune,  erstaune,  erschrecke';  zum  ß  vgl.  Schwyzer  Gr.  Gr.  I  333, 833;
o-ot.  afdöhn  .verstumme!'.
Unter  Voraussetzung  einer  Grundbed.  .schlagen'  kann  folgende  germ. Sippe  angereiht  werden:  anord.  dafla  .im  Wasser  plätschern',  norw.  dial. dahba  .stampfen,  festklopfen',  ano
```


## [2026-09-05T18:22:41.658Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dhē-\" POK_full.txt | head -40; echo ===; grep -n \"235\" POK_full.txt | grep -i \"dh\" | head -20",
 "description": "Grep POK_full for dhe root"
}
```


### [2026-09-05T18:22:41.718Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T18:22:44.001Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60; echo '---'; ls POK*",
 "description": "List refs dir"
}
```


### [2026-09-05T18:22:44.053Z] TOOL RESULT

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
---
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
```


## [2026-09-05T18:22:47.386Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"dhe-\" POK_full.txt | head -30; echo '###'; grep -n \"Page in Pokorny: 235\" POK_full.txt | head; echo '###'; grep -n \"235\" POK_full.txt | head -20",
 "description": "Search POK_full structure"
}
```


### [2026-09-05T18:22:47.470Z] TOOL RESULT

```
22131:Note: (:dha/- <m- and dhe- d^a-) s. esp. Schuize KZ. 27, 425 = Kl. Schr. 363. 
22241:See also: s. also above d^e-/, d^e-dhe-. 
71258:dhe-; 
###
###
6349:that point and about the borrowing question Schrader RL.II^ 394, G. Ipsen IF. 39, 235 f., 
11138:References: WP. II 184 f., Trautmann 29, Meillet Slave commun2 220, 235, Schwyzer Gr. 
13914:'; but about /^////-'daughter' s. Vetter Gl. 29, 235, 242 ff. against WH. I 557, 867; 
16209:References: Meillet MSL. 22, 142, 539 f., Trautmann 35, Specht Dekl. 42 f., 203, 235. 
17556:wood board ', s. Boisacq 174 m. Lithuanian and to meaning esp. Schuize KZ. 45, 235; 
19777:Page(s): 235 
22276:Page(s): 235 
22510:Page(s): 235-239 
23689:235); 
23704:Servius to Aen. Ill 235 also as sabin. and Umbrian stated word, so that df- instead of b/- 
25827:Celtic by Pedersen KG. II 235, Thurneysen Gr. 323, however, cymr. 5 can not belong to it. 
49896:References: WP. I 430 f., WH. I 86 f., 235; 
50341:'believe' (Melchert, 1987:197-198; MA:262-263)] (Sapir, 1936:263, VW:235; H:100). 
57442:References: WP. II 235. 
64842:References: WP. II 2 f., WH. II 232 f., 235 f., 245 f., Trautmann 209. 
70056:References: WP. II 346, Trautmann 235 f., Specht Indo Germanic Dekl. 115. 
70975:References: WP. II 369, Trautmann 235. 
91821:B Obi. yerkwantai {yertwantai), Pedersen Tocharian 235. 
91824:235, Frick151.
```


## [2026-09-05T18:22:49.803Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22440,22520p' POK_full.txt",
 "description": "Print Pokorny dhe- entry 235-239"
}
```


### [2026-09-05T18:22:49.857Z] TOOL RESULT

```
Old Indie dhaman-v\. " statute, law, dwelling, troop, multitude, crowd etc', Avestan 
daman-, dqman- n. "site, creature', gr. ava-9r|MCi " anything devoted to evil, an accursed 
thing ', £ni-9r|MCi " something put on, a lid, cover; statue on a grave', 9r||JU)v m. "heap'; 
£u9niJU)v "probably keeping tidy, keeping in order '; thrak. plant name Koa-5apa 
TTOTa|JOY£iTU)v (Dioskor.) (from *k"a-6^emn) " water settlement ', PN Uscu-dama; 
secondary (after Qta\(^ gr. 9£|ja n. " that which is placed or laid down: money deposited, 
deposit; also, of grain; treasure, pile, of loaves, coffer, position, situation, nativity, common 
burial-place, common land, private burial-ground, something proposed as a prize, case 
proposed for discussion, theme of an argument, proposition, premise, arbitrary 
determination, primary (non-derivative) element or form, of the present tense, mode of 
reduction of an irregular syllogism ', compare also Inf. 9£|j£vai; Avestan dami- f. " creation 
', Adj. (alsofem.) " constituting, originating, creator, god'; gr. 9£pi(; "that which is laid down 
or established by custom'. Gen. originally 9£piaT0(; "*allowed by the laws of God and men, 
righteous ' as Goddess's name, then "right, law, custom', 9£p£9Aa PI. " the foundation of a 
building; the innermost, core ', 9£|j£Aioi Ai9oi " the foundation-stones ', hom. 9£pi£iAia (£i 
metr. lengthening) " the foundations, lowest part, bottom, ground'; 

Alb. themer the foundation of a building; the innermost, core ' : hom. 9£M£iAia (£i metr. 
lengthening) " foundation, ground' [probably a loanword]; themen^\\ee\, bottom of the foot'. 

zero grade: Qa\xd "*massed; frequent, often ', 9a[jiv6q "frequent, often, massed', hom. 
Qa\xtzc„ femin. 9aM£iai PI. " the piled up, tightly packed, crowded, close-set, thick ' (from 
*9apu(;), 9apvo(; " thicket, shrubbery, bush, shrub'; in a t|ha-/77c»-' settlement, branch, 
dwelling' (compare 9ai[j6(; oiKia, an6po(;, cpurda Hes. [*6^amJo-], also Old Indie dhaman- 
"dwelling') or "heap, troop, multitude, crowd (the servant)' correlates one perhaps rightly 
also with Latin famulus^ a servant, a male slave, attendant ', familia^ a household (of 
slaves), establishment ', Oscan famer a servant, a male slave, attendant ', famelo^ a 
household (of slaves), establishment ', Umbrian famenas^ a household (of slaves), 
establishment '; 

Note: 

Common Latin d- > f- shift 

o-grade gr. 9(j0[j6(; "heap, barn, haystack'; Phrygian Soujjoq "an assembly, meeting, 
congress, a living together', Latin ai^-o'd/T?©/? "lower abdomen' as "intimate, hidden, secret 
part', compare Old High German intuoma^ the chief internal organs of the body, significant 
organs ' (would be Latin *inddmen). Middle Low German ingedome, bayr. ingetum6s., 
Gothic domsm. "judgement, fame' (o'o/77/5/7 "adjudicate'; from dem Germanic russ. duma 



'thought, notion, care; council meeting ' etc, s. Berneker 237), Old English o'o/t? "opinion, 
sense, mind, judgement, court'. Old High German /i/0/77 'judgement, feat, deed, act, 
custom, state, status', Lithuanian dome, domesys^ attention, directing of the thought and 
will on something ', also Lithuanian deme' spot upon which attention is directed ' etc, 
demetis = dometis ' wonder, care, concern, follow, go, take interest '. 

Old Icelandic daeir easy to do, easy, without difficulty ' ( W^e-li-s); compare Proto Norse 
dalidun^ they did ' (preterit of Germanic *delian), Lithuanian pa-delys^ nest-egg (the hen 
lays an egg) ', priedele, priedelis' inclosure ', Old Bulgarian delou. 'work', wherefore (see 
Berneker 195 f., Trautmann 48) Old Church Slavic deija, de/jbrnavn. Gen. 'because of, 
Lithuanian del, del, deliai, Latvian o'e/ with Gen. 'because of, for the sake of. 

Maybe from Slavic /7e'not' + Old Church Slavic: o'e/o'work, matter' = Bulgarian HOflena 
{nedel'a), Serbian nedeija, Czech nedele, Polish n/edz/e/a^ Sunday, holiday = no work' : 
Lithuanian: o'e//c»//"put down, away' : Albanian q^ie/e'Sunday, holiday'. 

An occasional formation compare still gr. t£9|j6c; (Pind.), GeGjjoc; (lak. etc), Bza[}6q (Attic) 
' statute ' after Th urn eysen (KZ. 51, 57) to Old Irish dedm, cymr. deddf{*&^e-6!"-ma) ds. 
(different Schwyzer Gr. Gr. I 492''2); Gojri, Attic Gwa: ' punishment '. Very doubtful a s- 
extension would be attributed to Old Icelandic des {* dasjo) ' hay stick, hay rick ' (loanword 
from dem Old Irish?), Old Irish dais {* dasti-) 'heap, hay rick', wherewith E. Lewy (KZ. 52, 
310) compares rather osset. dasun^^We up, lump'. 

References: WP. I 826 ff , WH. I 266, 362 f , 439 ff , 863, Trautmann 47 ff , Schwyzer Gr. 
Gr. I 492, 686, 722, 725, 741, Pedersen Hittite 141 ff., 192. 
Page(s): 235-239 



Root / lemma: 6^6-3, d^^- 

Meaning: to disappear 

Material: Latin famesi. 'hunger', ad fatim, affatim^a6 lassitudinem, zurGeniJge', fatTgo 

'hetze ab, ermijde', fatJsco, -o^'gehe auseinander; ermatte';
```


## [2026-09-05T18:22:54.978Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22280,22440p' POK_full.txt",
 "description": "Print start of Pokorny dhe- entry"
}
```


### [2026-09-05T18:22:55.033Z] TOOL RESULT

```
Material: Old Indie dadhati, Avestan dadaiti^ he places ', Old pers. Impf. Sg. adada^ he 
has installed ', Old Indie Aor.a-o'/75-/r7"l placed', Med. 3. Sg. a-dhita{= gr. eGeto) ; to 
participle Old Indie hita-h{-dhita-h\v\ ved. compounds) "set, settled ' (= Latin con-ditus, ab- 
ditus, creditus, probably also gr. Qzioq, " sedate, calm, settled, placed, set; having position; 
taken as one's child, adopted '), with full grade Avestan Old pers. data- (= Lithuanian detas 
" sedate, calm, settled ', Old Prussian sen-ditans f\Vk. PI. f. " folded ', also gr. Ghtov poopov 
Hes., actually " set raised platform, placed stand '); Inf. Old Indie dha-tum{= Lithuanian 
o'e/z/Supin., Old Church Slavic detb "to place' : Latin [late] conditus, -usm. " pickled, 
preserved; of corpses, embalmed; in gen., seasoned, savory ', Supin. -um, -u, compare 
also Old Indie dhatu-h), m. " component, set', Avestan vT5atu- n. " grounds, rationale, 
steady acquiescence ');„/c>-present Old Indie dhayate^ places for oneself ' (= Latvian deju, 
det^p\ace, lay eggs', deju det^ solder together ', Old Church Slavic o'eyip"lay, place'. Old 
Czech deju^xx\ake')\ Perf. Old Indie dadhau, dadhima, Avestan 3. Sg. da5a{\ gr. TsGspai, 
Latin -didT, Oscan pru-ffed. Old High German tetaeXc). 

Armenian edAor. "he placed' (= Old Indie a-dhat, 1. Sg. edi, 2. Sg. edit), present dnem^ 
I place ' {*dinem, Indo Germanic *d'^e-A7o, compare russ. denu^sW., put, lay, place', Serbo- 
Croatian djenem " do, put, lay '); 

Maybe nasalized alb. Geg me ndejVio sit, while, stay', A7o'ey"hang lose, place' 

Phrygian zbazc, "has placed' ( *e-6^a-es-f7 rather = Hittite da-a-is)\ 

gr. TiGriM' "puf (Aor. sGriKO - see below -, iQz\xzy, sGsto, Fut. Gnaw, participle Getoc;); 

Messapic hi-pa-of has placed ' {*ghi-po-&^es-t, J. B. Hofmann KZ. 63, 267); 

Latin abdere^ put away, remove, set aside, stow away', con-dere^ to put together, 
make by joining, found, establish, build, settle' (in addition Census [*kom-d-to-] av\ ancient 
deity, god of secret plans), perdere^ to make away with, destroy, ruin, squander, dissipate, 



throw away, waste, lose ', credere 'beWeve, trust' (see below 'Areref/- "heart'); about the 
interference of darew\t\r\ respective forms s. WH. I 362; Perf. cond/dfetc, Oscan pru-ffed' 
has placed ' {*-fefed). 

Note: 

Common italic-Latin o'->/- shift. 

With einer /r-extension Latin fac/o, -ere, fecT{: £0r|Ka), factum' to make, form, do, 
perform; of feelings and circumstances, to cause, bring about ', Oscan fakiiad, Umbrian 
facia ' he/she makes, constructs, fashions, frames, builds, produces, composes ', fakurent 
Fut. II [subjunctive] "they will have made, constructed, fashioned, framed, erected, 
produced, composed ', praen. (passionate inscription) FheFhaked'helshe has made, 
constructed, fashioned, framed, erected, produced, composed ', Oscan fefacitKou]. Perf. 
"let he/she have made, constructed, fashioned, framed, erected, produced, composed ', 
fefacustFut II "he/she will have made, constructed, fashioned, framed, erected, produced, 
composed '; 

with *fek- Umbrian fe/tu, /e/i/ [Imperative]" he/she will have made, constructed, 
fashioned, framed, erected, produced, composed ': 

fac/7/s "( feasible) easy to do; easy to manage, convenient, favorable ', Umbrian facefele 
ds.; fades' shape, form, figure, outward appearance; esp. face, countenance. Transf., 
character, nature; seeming, pretence ', facinus, ponti-fex, arti-fex bene-ficus \ to meaning 
of interficid " to put out of the way, destroy, bring to naught, slay, kill' ("*allow to disappear') 
compare Old Indie antar-hita-h' vanished '. 

The same A'-extension besides in gr. £9r|Ka also in 6nKr| " receptacle ', Old Indie dha-ka- 
/?" container' and Phrygian a5-5aK£T " afflicts, causes death ', Med. a5-5aK£Top; Venetic 
vhaxs&o' he/she makes, constructs, fashions, frames, builds, erects, produces, composes 
' {*fak-s-to, the /probably from Ital.); 

Hittite dak-ki-es-zi {dakkeszi) " makes, places down ' (: Latin facessd), dak-su-ul {daksul) 
"friendly' (: Old Latin facul); perhaps Tocharian A taka'\ was, became', B takawa diS. 
(different Pedersen Tocharian 194); 

gall, dede' he/she has placed '; compare Latin con-, ab-, cre-didT, Old High German teta 
" I made, did'; Old Irish -tarti'Qwes, yields ' {*to-ro-ad-dI't irom *6'^e-t), Perf. do-rat {*to-ro- 
ad-datirovn *d'^e-t}, Thurneysen Gr. 35; 



Old High German torn, tuom, Old Saxon ton, Old English dom'do'. Inf. Old High 
German tuon. Old Saxon Old English don {*d^d-m) "do', preterit Old High German teta'\ 
made, did' (2. Sg. tat/, PI. tatu-m; reshaped after the type of Gothic setum). Old Saxon 
deda{2. Sg. dedos, 3. PI. dadun, dedun). Old English dyde< dud/ {see above to Old Indie 
dadhau); particle Perf. Pass. Old High German gi-tan. Old English don^ done ' from *d^e- 
no- =Old Church Slavic o-dent ' wrapped, dressed '; 

in the ending of reduced Prater. (Gothic salbo-dedun eic) one tries to seek mostly the 
root d^e- whereas in Gothic kunt^a^ granted ', must contain the Indo Germanic -/-, to 
accept an other formation, compare Hirt, Indo Germanic Gr. IV, 99, Sverdrup NTS. 2, 55 
ff., Marstrander, NTS. 4, 424 f., Specht KZ. 62, 69 ff., Kretschmer Sbb. Wien, 225. Bd., 2. 
Abh.,6f. 

Lithuanian det/lay, place, put', present 2. PI. old deste{*d^e-6^-te), Sg. demi, desie-s, 
destC/J {compare Buga Kalba irs. 158, 213), neologism dedu, Latvian det{see above); 

Old Church Slavic det/lay, place, say', present dezdg {* ded/o) and dejg{see above); 
dejg, dejatr\a\i, place, do'; -i/a-iterative Old Church Slavic o-devati\\.o put), dress ', russ. 
devatb "set down, do, place'; 

in addition probably Lithuanian deviu, devet/'wear a dress'; a formant ua\so in gr. 
*9oFaKOc; and (assim.) *9aFaK0(;, compare Goa^w "sit, put', Ionian 0aJKO(; (hom. 06u)ko(; 
written for 96[F]aKO(;) "seat', GapaKOv Gqkov ri Gpovov Hes., Attic also GaKO(; ds., hom. 
Gaaaau) "sit', Attic poet Gaaou) ds. (see to gr. group Bechtel Lexil. 161 f., Boisacq 335); 
compare also thrak. -dava^ settling, settlement ' from *6!"euaor *d^9ua; probably 
reshuffling after the concurrent *dd-: *dou- "bestow, give'; 

Note: 

The suffix -dava' settling, settlement ' frequently scattered over the thrak. territory and city 
names is absent in lllyrian toponyms, hence lllyrian-alb. and trak. were two different 
people. 

Hittite da-a-i{dai) " places, lays ', 1. Sg. te-eh-hi{tehhi), 3. PI. //■a/>z/(Pedersen Hittite 
91, 112 f., 166), preterit 3. Sg. da-a-is, perhaps also dak-ki-es-zi {see above); 

Hittite: dai-, tai- (II) ' place, lay, put ', tija- (I) ' step, tread, be positioned ', tittanu- (I) ' put, 

place ', zikk- (I) ' lay, place ' (Friedrich 202-203, 223-225, 260-261) 

Hittite: te- (I) 'say' (Friedrich 219-220) : Old Church Slavic deti^ay, place, say' 



Tocharian A ta-, tas-, tas-, B tes- "lay, place' fd^e-s- Pedersen Tocharian 186 f.); 

Tocharian B tatta- 'to place, set' (Adams 283 f) 

Lycian ta- "lay, place' (Pedersen. Lycian and Hittite 30 f.). 

Root nouns (in compositions): e.g. Old Indie vayo-dha-h^ imparting vitality ', saifi-dhai. 
" pact, agreement, promise ' (: Lithuanian arkli-de^ stable '), sarh-dh-a-m' association ' (: 
Lithuanian sam-das), ratna-dh-a-h^ imparting treasure ', ni-dh-i-hm. " container, treasure, 
tribute', sam-dh-f-hvn. " association, covenant, fusion ', Avestan gao-5i-^ milk container'; 
Lithuanian samdas^ rent, rental ', //7o'a5 "vessel', nuodaf poison ', (old) nuodzia^ debt, 
blame, offense ', padis^ the hen lays an egg '; 

Old Prussian umnode^ bakehouse ', Lithuanian pelude, Latvian pelade^ chaff container ', 
Old Church Slavic obb-dou. "Gnoaupoq', sp-o'b"Kpiai(;, KpTpa'; compare Berneker 193 ff., 
Trautmann 47 f.; if so also Old Icelandic oddr. Old English ord. Old High German c»/'/"cusp, 
peak' as *ud-6yo-s " pointed up'? 

nominal formation: 

Old Indie dhatar-xw. " instigator, founder', dhafar-^ creator, god' (compare also Old 
Church Slavic detelb "perpetrator'), gr. Gsirip, Latin con-ditor^ a founder; hence, in gen., 
contriver, composer, author '; 

compare t|ha-//c»-in Old Irish dal, acymr. dati, ncymr. dadi, abret. o''ao'/"congregation, 
meeting', nbret. daer contest, quarrel ' (compare to meaning Phrygian 5ou|JO(;); 

t|ha-//-in Old Indie -dhiti-hi. " stead ', deva-hiti-h' God's statute ', gr. GsoK^f. " statute, 
order', Latin con-diti-oi. " an agreement, stipulation, condition, compact, proposition, 
terms, demand '; tl*^e-//-sin Avestan ni-5aiti-i. " laying down, putting away, hiding ', Gothic 
gadeds^ deed, position, place ', Old Icelandic dad^ skillfulness, deed, act'. Old English 
dsed. Old High German /a/"deed, act', Lithuanian detis^ load, burden ', PI. detys^ lay of 
the chicken, the goose ', Old Church Slavic blago-detb " Grace, blessing, gratitude '; tl^a- 
t-\r\ thrak. PN Aaroc;, alb. dhate{*^^9-t§) " site '; *^^d-t-\r\ Avestan dami-da-V the created 
creature ', Latin sacer-dos^ a priest, priestess ' {*sacro-(ii'^dt-s). 

Old Indie dhana-m^ container', el. auv0r|vai (?) "pact, covenant'. Old High German 
participle gitan. Old English don^ done ', Old Church Slavic c»-o'e/7b "(completed), vested '; 
Old Indie dhana-m^ sacrifice, offering, price in competition etc ', nidhanam' layover, stay, 
inhabitation etc', godhana-m^ cattle possession ', Avestan gao-5ana-r\. " milk container '.
```


## [2026-09-05T18:23:01.704Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22265,22282p' POK_full.txt; echo '######## mazda'; grep -n -i \"mazda\" POK_full.txt | head -20",
 "description": "Pokorny root header and mazda"
}
```


### [2026-09-05T18:23:01.777Z] TOOL RESULT

```
Turk. c/ay/"unc\e' derived from russ. djac/ja 'unc\e' while alb. dajan. f. "uncle' could have 

existed before turk. day/'unc\e', however, alb. cognate is phonetically identical with other 

cognates: also turk. /7a/a "paternal aunt' : alb. /75//a "paternal aunt', turk. /eyze "maternal 

aunt' : alb. /eze "maternal aunt'. 

References: WP. I 826, Trautmann 47, Schwyzer Gr. Gr. I 193. 

Page(s): 235 

Root / lemma: d^e-2 
Meaning: to put, place, say 

Material: Old Indie dadhati, Avestan dadaiti^ he places ', Old pers. Impf. Sg. adada^ he 
has installed ', Old Indie Aor.a-o'/75-/r7"l placed', Med. 3. Sg. a-dhita{= gr. eGeto) ; to 
######## mazda
57058:n. " fattening ', medyati, medate^ becomes fat ', medya-la\! {meda-irom *mazda-, Indo 
59307:Material: Old Indie medha^ wisdom, discernment, reason', Avestan mazda, mazdah-x\. 
59309:"Gedachtnis, remembrance ', mazdah-m. name of the highest God {*maz6,^a iroxr\ *mn6^-
```


## [2026-09-05T18:23:05.816Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '59295,59330p' POK_full.txt",
 "description": "Pokorny mazdā entry"
}
```


### [2026-09-05T18:23:05.867Z] TOOL RESULT

```
mefl, corn. meul6s., Celtic -it*/- from -mbl-??Vox Gothic p compare Specht Indo Germanic 

Dekl. 261, Anm. 1. 

References: WP. II 261 f. 

Page(s): 725 

Root / lemma: mehnA^- 

Meaning: to pay attention to; vivacious, wisdom 

Material: Old Indie medha^ wisdom, discernment, reason', Avestan mazda, mazdah-x\. 

"Gedachtnis, remembrance ', mazdah-m. name of the highest God {*maz6,^a iroxr\ *mn6^- 

ta); 

gr. ijavGavu) (secondary present to) paOnoopai, paGsTv "learn', Doric-Aeolic fJCiQn. Ionian 
IjaOog n., Ionic-Attic \xbBr\o\Q, " learning, lesson '; |jev9npr| "forehead; cppovTi(;'; perhaps 
MoOaa (*[jov0ja) " Muse, any of nine goddesses who are associated with inspiration and 
creativity for the arts (Greek Mythology)'; 

Maybe Albanian mesoj: Griko Salentino mattenno: Latvian macTties: Lithuanian mokytls^ 
learn'. 

alb. mund^ can, win '; 

Maybe alb. mundoj^ exhaust '. 

Maybe {*mundi) MujT Heracles of Albanians ', mundje^ struggle, defeat ' 



cymr. mynnu'\Nant, desire, will', corn. mennar\ will', mynnes, mynnas'\Nant, desire, 
will, volition', (common Celtic -ns-, -nt- > -nn-), cymr. go- f/n{n) long, want, bid, beg, ask,
```


## [2026-09-05T18:23:18.435Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=59300 && NR<=59420 && /Page\\(s\\)/' POK_full.txt | head -3; echo '### AHD dhe'; grep -n -i \"dhē-\\|dhe-\\b\" AHD_watkins1985.txt | head -20",
 "description": "Pokorny mendh page; AHD dhe"
}
```


### [2026-09-05T18:23:20.321Z] TOOL RESULT

```
Page(s): 725 
Page(s): 730 
Page(s): 729 
### AHD dhe
375:mild, gentle: DAFT. 2. Probably suffixed form *dhabh-ro- in Latin faber, artisan (< “he who fits together”): FABRIC, (FABRICATE), FORGE}. [Pok. 2. dhabh- 233.] dhal-. To bloom. Suffixed form *dhal-yo- in Greek thal- lein, to flourish, bloom, sprout (> thallos, a shoot): THALIA, THALLUS; PROTHALLUS. [Pok. dhail- 234.] dhé-', To set, put. Contracted from *dheo-. 1. O-grade form *dhé- in Germanic *don in Old English dén, to do: Dol; FORDO. 2. Suffixed form *dhé-ti-, “thing laid down or done, law, deed,” in Germanic *dédiz in Old English déd, doing, deed: DEED. 3. Suffixed o-grade form *dho-mo- in Germanic *démaz in: a. Old English dom, judgment (< “thing set or put down”): Doom; b. Old English -d6m, abstract suffix indicating state, condition, or power: -DOM; c. Old Norse -démr, condition (see ka-); d. Gothic déms, judgment, akin to the Germanic source of Russian Duma, Duma: Duma; e. Germanic denomina- tive *“ddmjan in Old English déman, to judge: DEEM. 4. Suffixed o-grade form *dhé-t- in Latin agential suffix -dés in Latin sacerdés, priest, “(performer of sacred rites” (see sak-). 5. Zero-grade form “dha- in: a. prefixed form *kom-dha- in Latin condere, to put together, establish, preserve (*kom, together; see kom): CONDIMENT; AB- SCOND, INCONDITE, RECONDITE, SCONCE?; b. compound *kred-dha- (see kerd-'). 6. Suffixed zero-grade form *dha-k- in: a. Latin facere (< *fak-yo-), to do, make (> French faire, to do), and Latin combining form -fex (< *.fak-s), “maker”: -FACIENT, FACT, FACTION, FACTITIOUS, FACTOR, FASHION, FEASIBLE, FEAT!, FEATURE, (FETISH), -FIC, (-FY); AFFAIR, AFFECT!, (AFFECT2), (AFFECTION), AMPLIFY, ARTIFACT, ARTIFICE, BEATIFIC, BENEFACTION, BENEFIC, (BENEFICE), (BENEFICENCE), BENEFIT, CHAFE, COMFIT, CONFECT, (CONFETTI), COUNTERFEIT, (DEFEA- SANCE), DEFEAT, DEFECT, (DEFICIENT), (DISCOMFIT), EDIFICE, (EDIFY), EFFECT, (EFFICACIOUS), (EFFICIENT), FACSIMILE, FACTOTUM, FORFEIT, HACIENDA, INFECT, JUSTIFY, MALEFACTOR, MALFEASANCE, MANUFACTURE, MISFEASANCE, MODIFY, MOLLIFY, NIDIFY, NOTIFY, NUL- LIFY, OFFICINAL, PERFECT, PETRIFY, (PLUPERFECT), PON- TIFEX, PREFECT, (PROFICIENT), PROFIT, PUTREFY, QUALIFY, RAREFY, RECTIFY, REFECT, (REFECTORY), RU- BEFACIENT, SACRIFICE, SCIRE FACIAS, SPINIFEX, SUF- FICE, (SUFFICIENT), SURFEIT, TUBIFEX, TUMEFACIENT, viviry; b. Latin derivative faciés, shape, face (< “form imposed on something”): FACADE, FACE, (FACET), (FA- CIAL), FACIES; (DEFACE), EFFACE, PRIMA FACIE, (SUR- FACE); c. Latin compound officium (< *opi-fici-om), service, duty, business, performance of work (*opi-, work; see op-'): OFFICE; d. further suffixed form *dha-k-li- in Latin facilis (< Old Latin facul), feasible, easy: FACILE, (FACILITY), FACULTY; DIFFICULTY. 7. Suffixed zero-grade form *dha-s- in Latin fds, divine law, right: NEFARIOUS. 8. Possibly Latin -farius, -doing: MULTIFARIOUS, OMNI- FARIOUS. 9. Reduplicated form *dhi-dhé- in Greek tithe- nai, to put: THESIS, THETIC; ANATHEMA, ANTITHESIS, APOTHECARY, (APOTHECIUM), BODEGA, BOUTIQUE, DI- ATHESIS, EPENTHESIS, EPITHET, HYPOTHESIS, METATHE- SIS, PARENTHESIS, PROSTHESIS, PROTHESIS. 10. Suffixed form *dhé-k- in Greek théké, receptacle: THECA, TICK?; AMPHITHECIUM, BIBLIOTHECA, CLEISTOTHECIUM, ENDO- THECIUM, PERITHECIUM. 11. Suffixed zero-grade form *dha-mn in Greek thema, “thing placed,” proposition: (THEMATIC), THEME. 12. Reduplicated form *dhe-dhé- in Sanskrit dadhdti, he places: SANDHI. 13. Reduced form *dh- (see aw-2). [Pok. 2. dhé- 235.] dhé-2. To vanish. Contracted from *dhea-. 1. Possibly Old Norse d%sa, to languish, decay: DASTARD. 2. Possibly Old Norse *dasa, to tire out (attested only in reflexive form dasask, to become exhausted), akin to the Scandi- navian source of Middle English dasen, to stun: DAZE. [Pok. 3. dhé- 239.] dheb-. Dense, firm, compressed. Germanic suffixed form *dap-ra- in Middle Dutch and Middle Low German
```


## [2026-09-05T18:23:28.257Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"ahura\" KLN_1966.txt KLN_1971.txt | head -20; echo '### Ormuzd'; grep -n -i \"ormuzd\\|Ormazd\\|Mazdaism\\|Mazdean\" KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Grep Klein for Ahura Mazda"
}
```


### [2026-09-05T18:23:28.347Z] TOOL RESULT

```
KLN_1971.txt:10008:ahura, n., a benevolent deity {Persian mythology). 
KLN_1971.txt:10009:— Avestic ahura-, *a god, a good spirit’, rel. to 
KLN_1971.txt:10013:Ahura- Mazda, n. — See Ormazd. 
KLN_1971.txt:15499:mous, unanimity. Cp. also ahura, anemo-, an- 
KLN_1971.txt:21752:courage, wish, derive’. See animus and cp. ahura 
KLN_1971.txt:168883:fr. Avestic Ahuramazda , lit. ‘wise lord’, a com- 
KLN_1971.txt:168884:pound of ahura-, ‘a god, a good spirit’ (see 
KLN_1971.txt:168885:ahura), and ma(n)dzdhd > ‘wise’, which is a com- 
KLN_1966.txt:2036:ahura,  n.,  a  benevolent  deity  (Persian  mythology). —  Avestic  ahura-,  ‘a  god,  a  good  spirit',  rel.  to OL  dsurah,  of  same  meaning.  Sec  asura  and  cp. the  first  element  in  Ormazd.
KLN_1966.txt:2037:Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
KLN_1966.txt:2828:animus,  n.,  1)  intention;  2)  animosity.  —  L., ‘soul,  spirit,  mind,  courage,  wish,  desire’,  rel.  to anima,  ‘breath  of  air,  air,  breath,  soul,  life’,  and cogn.  with  Gk.  avE|jto<;,  ‘wind’,  fr.  I.-E.  base *an-,  ‘to  blow,  breathe’,  whence  also  OI.  ani-ti, ana-ti,  ‘breathes’,  ani-lah,  ‘breath’,  OIr.  anal,  W. anadl,  MBret.  (with  metathesis)  alazn,  ‘breath’, OIr.  animm,  Co.,  Bret,  eneff,  ‘soul’,  Goth,  uz- anan,  ‘to  exhale’,  ON.  anda,  ‘to  breathe’,  andi, ond,  ‘breath,  soul,  spirit’,  OE.  edian  (for  *an- j>jan ),  ‘to  breathe’,  OSlav,  vonja,  ‘smell’.  Alb. Gheg  o/.Tosk  Jh/I  sweH’,  Toch.  A  afima.  Arm. anjn ,  ‘soul’.  Cp.  animadvert,  animal,  animal¬ cule,  animate,  animosity,  equanimity,  exanimate, exhale,  inhale,  longanimity,  magnanimous,  mag¬ nanimity,  pusillanimous,  pusillanimity,  unani¬ mous,  unanimity.  Cp.  also  ahura,  anemo-,  an- helation,  asthma,  asura,  prana, anion,  n.,  a  negatively  charged  ion  ( physical chem.)  —  Gk.  aviov,  neut.  of  avicbv,  pres, part,  of  avi£vai,  ‘to  go  up’,  fr,  ava  (see  ana-) and  isvai,  ‘to  go’,  which  is  cogn.  with  L.  ire, ‘to  go’.  See  itinerate.  The  word  anion  was  in¬ troduced  into  electricity  by  the  English  physi¬ cist  and  chemist  Michael  Faraday  (1791-1867); cp.  ion,  cation.
KLN_1966.txt:3778:asura,  n.,  a  god,  a  good  spirit;  later  an  evil  spirit (Hindu  mythol.)  —  Ol.  asurah,  prob.  rel.  to  OI. asuh  (for  *nsu-),  ‘breath  of  life',  fr.  I.-E.  base *an-,  ‘to  blow,  breathe',  whence  also  OI.  ani-ti, dna-ti ,  ‘breathes’,  L.  anima,  ‘breath  of  air, breath,  soul,  life’,  animus,  ‘soul,  spirit,  mind, courage,  wish,  derive'.  See  animus  and  cp.  ahura and  sura,  ‘spirit,  demon’.
KLN_1966.txt:26581:Orleans,  n.,  1)  a  kind  of  purple  plum) ;  2)  worsted- and-cotton  fabric.  —  In  both  senses  named  after the  city  of  Orleans,  south  of  Paris, orlop,  n.,  the  lowest  deck  of  a  ship.  —  Du.  over¬ loop,  ‘deck  of  a  ship’,  lit.  ‘that  which  runs  over", fr.  overlopen,  ‘to  run  over’;  (see  over  and  leap); so  called  because  it  covers  the  ship’s  hold. Ormazd,  n.,  the  principle  of  good  in  the  Zoro- astrian  religion.  —  Pers.,  fr.  OPers.  Auramazda, fr.  Avestic  Ahuramazda,  lit.  ‘wise  lord',  a  com¬ pound  of  ahura-,  ‘a  god,  a  good  spirit’  (see ahura),  and  ma(n)dzdha-,  ‘wise’,  which  is  a  com¬ pound  formed  from  the  I.-E.  bases  *men-dh~,  ‘to apply  oneself  to’,  and  *dhe-,  ‘to  put,  place’. From  base  * men-dh -  derives  also  OI.  medha, ‘wisdom,  intelligence’.  For  other  derivatives  of this  base  see  mathematical.  For  base  *dhe-  see do  and  cp.  theme,  fact.
### Ormuzd
KLN_1971.txt:10011:the first element in Ormazd. 
KLN_1971.txt:10013:Ahura- Mazda, n. — See Ormazd. 
KLN_1971.txt:74550:and in Ormazd. 
KLN_1971.txt:146556:element in Ormazd. 
KLN_1971.txt:147109:Mazdaism, also Mazdeism, n., Zoroastrianism. 
KLN_1971.txt:147111:— See Ormazd and -ism. 
KLN_1971.txt:168881:Ormazd, n., the principle of good in the Zoro- 
KLN_1966.txt:2036:ahura,  n.,  a  benevolent  deity  (Persian  mythology). —  Avestic  ahura-,  ‘a  god,  a  good  spirit',  rel.  to OL  dsurah,  of  same  meaning.  Sec  asura  and  cp. the  first  element  in  Ormazd.
KLN_1966.txt:2037:Ahura-Mazda,  n.  —  See  Ormazd. ai,  n.,  the  three-toed  sloth.  —  Tupi  ai,  a  word imitative  of  the  cry  of  the  animal, aid,  tr.  v.  —  OF.  aidier,  aider  (F.  aider),  fr.  L. adjutare,  ‘to  help’,  freq.  of  adjuvare  (pp.  adju- tus),  ‘to  help’,  sustain’,  fr.  ad-  and  juvare,  ‘to help’,  which  is  of  uncertain  origin.  Cp.  adju¬ tant,  adjuvant,  coadjutor,  jocund,  jury,  adj. Derivatives:  aid-er,  n.,  aid-ful,  adj. aid,  n.  —  OF.  ( =  F.)  aide ,  back  formation  fr.  aider. See  aid,  v.
KLN_1966.txt:11938:‘I  place’,  aor.  ed,  ‘he  placed’,  Gk.  riDivoa,  ‘to put,  place,  set’,  f )eai;,  ‘a  placing,  setting’,  fHjxr], ‘case  in  which  to  put  something’,  flejxa,  ‘that which  is  placed’,  Difxi?,  Tight,  decree’,  Ssajxo;, Taw,  rule,  precept’,  lit.  ‘that  which  is  laid  down’, fb)(xtov,  Htop.61;,  ‘heap’,  flcueOXa  (pi.),  Homeric (pi.),  ‘foundation’,  L.  facere,  ‘to  make, do’,  -dere  in  ab-dere,  ‘to  hide,  conceal’,  con-dere, ‘to  found,  establish’,  per-dere,  ‘to  lose,  throw away,  ruin’,  OSIav.  dejp,  deti,  ‘to  place,  lay’, Lith.  deti,  Lett,  del,  ‘to  place,  put’,  OSIav. o-denu,  ‘clothed,  dressed’,  Gael,  deck,  ‘placed’. Cp.  ado,  deed,  deem,  doff,  -dom,  don,  v.,  doom, dout,  dup.  Cp.  also  theme  and  words  there referred  to.  Cp.  also  fact  and  words  there  re¬ ferred  to.  Cp.  also  abdomen,  abscond,  condiment, Consus,  dagoba,  dam,  ‘an  earthbank’,  family, fetial,  hoard,  perdition,  recondite,  sacerdotal, samadh,  samadhi,  sconce,  ‘a  metal  bracket’, stridhana.  Cp.  also  the  second  element  in  creed and  in  jubilate,  and  the  third  element  in  divide and  in  Ormazd.
KLN_1966.txt:23122:learned,  learning,  science’,  from  the  aorist p,a&£tv  (whence  the  pres,  [iavffaveiv ),  ‘to  learn’, fr.  *mndh-,  reduced  form  of  I.-E.  base  *men-dh-, ‘to  have  one’s  mind  aroused,  apply  oneself to’.  From  the  same  base  (resp.  its  reduced  form) prob.  derive  Gk.  p.Ev(H)p7],  ‘care’,  Lith.  man- dr  as,  mandrils,  ‘wide-awake’,  OSlav.  mqdru, ‘wise,  sage’,  Goth,  mundon  sis,  ‘to  look  at’,  ON. munda,  ‘to  aim’,  OHG.  mendan,  ‘to  rejoice , OHG.  muntar,  MHG.  munter,  munder,  ‘eager, agile,  nimble",  G.  munter,  ‘awake,  lively,  gay, merry,  vigorous’,  W.  mynnu ,  ‘to  want,  wish  , Alb.  mund,  ‘I  can,  I  am,  victorious’,  and  pos¬ sibly  also  Ol.  medha,  ‘wisdom,  intelligence',  Gk. Mouaot  (if  fr.  *M6vffia),  ‘Muse’.  Base  *men-dh- is  an  enlargement  of  base  *men-,  ‘to  think’. See  mind  and  cp.  Muse,  Epimetheus,  Prome¬ theus.  Cp.  also  the  second  element  in  chresto- mathy,  opsimath,  polymath.  Cp.  also  the  second element  in  Ormazd.
KLN_1966.txt:23215:Mazdaism,  also  Mazdeism,  n.,  Zoroastrianism.
KLN_1966.txt:23216:—  See  Ormazd  and  -ism.
KLN_1966.txt:26581:Orleans,  n.,  1)  a  kind  of  purple  plum) ;  2)  worsted- and-cotton  fabric.  —  In  both  senses  named  after the  city  of  Orleans,  south  of  Paris, orlop,  n.,  the  lowest  deck  of  a  ship.  —  Du.  over¬ loop,  ‘deck  of  a  ship’,  lit.  ‘that  which  runs  over", fr.  overlopen,  ‘to  run  over’;  (see  over  and  leap); so  called  because  it  covers  the  ship’s  hold. Ormazd,  n.,  the  principle  of  good  in  the  Zoro- astrian  religion.  —  Pers.,  fr.  OPers.  Auramazda, fr.  Avestic  Ahuramazda,  lit.  ‘wise  lord',  a  com¬ pound  of  ahura-,  ‘a  god,  a  good  spirit’  (see ahura),  and  ma(n)dzdha-,  ‘wise’,  which  is  a  com¬ pound  formed  from  the  I.-E.  bases  *men-dh~,  ‘to apply  oneself  to’,  and  *dhe-,  ‘to  put,  place’. From  base  * men-dh -  derives  also  OI.  medha, ‘wisdom,  intelligence’.  For  other  derivatives  of this  base  see  mathematical.  For  base  *dhe-  see do  and  cp.  theme,  fact.
```


## [2026-09-05T18:23:35.851Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target,pat in [(26581,'Ormazd'),(2036,'ahura'),(23122,'mathematical')]:\n    pre='\\n'.join(lines[:target])\n    print(pat,'leaf',pre.count('\\f'))\nEOF",
 "description": "Compute Klein leaf numbers"
}
```


### [2026-09-05T18:23:37.880Z] TOOL RESULT

```
Ormazd leaf 586
ahura leaf 33
mathematical leaf 508
```


## [2026-09-05T18:23:46.145Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==587' KLN_1966.txt | head -5; echo '...TAIL...'; awk 'BEGIN{RS=\"\\f\"} NR==587' KLN_1966.txt | tail -3",
 "description": "Print Klein leaf 586 for page numbers"
}
```


### [2026-09-05T18:23:47.794Z] TOOL RESULT

```
s  American  birds  of  the  family Icteridae.  —  F.  oriol,  fr.  OF.,  fr.  ML.  oryolus, fr.  L.  aureolus,  ‘golden’,  dimin.  of  aureus,  fr. aurum,  ‘gold’.  See  aureate  and  dimin.  suff.  -ole. Oriolidae,  n.  pi.,  a  family  of  birds  ( ornithol .)  — ModL.,  formed  with  suff.  -idae  fr.  ModL.  orio- lus,  fr.  ML.  oryolus.  See  prec.  word.
Orion,  n.,  1)  a  giant  hunter  slain  by  Artemis  and made  into  a  constellation  ( Greek  mythol .) ;  2)  a constellation  near  Tauris  (astron.)  —  L.  Orion, fr.  Gk.  ’flptcav,  which  is  of  uncertain  origin, -orious,  adj.  suff.  meaning  ‘pertaining  to,  serving to’,  as  in  meritorious.  —  Compounded  of  L.  on- in  -dri-us  (see  adj.  suff.  -ory)  and  -ous. orison,  n.  (usually  in  pi.),  prayer.  —  ME.  oreisun, fr.  OF.  oreison,  orison  (F.  oraison),  fr.  L.  oratio- nem,  acc.  of  oratio,  ‘speech,  prayer'.  See  oration and  cp.  words  there  referred  to.
-orium,  subst.  suff.  denoting  ‘a  place  or  a  thing used  for  something’,  as  in  audit  orium,  ‘a  place for  hearing’.  —  L.  -orium,  prop.  neut.  of  the  adj. suff.  -orius.  See  adj.  and  subst.  suff.  -ory. Orlando,  masc.  PN.  —  Italian  form  of  Roland (q.v.)
orle,  n.,  a  narrow  border  following  the  outline  of the  shield  (her.)  —  MF.  (=  F.)  orle,  fr.  orler  (F. ourler),  ‘to  border,  edge,  hem’,  fr.  VL.  *oruldre (whence  also  It.  orlare,  ‘to  border,  edge,  hem’), fr.  VL.  *orulus  (whence  also  It.  orlo,  ‘border, edge,  hem’),  dimin.  formed  fr.  L.  dra,  ‘margin, border’ ;  see  oral.  Sp.  orla,  ‘border,  fringe’ (whence  orlar,  ‘to  border,  edge’),  derives  fr.  VL. *drula,  dimin.  of  L.  ora.
Orleans,  n.,  1)  a  kind  of  purple  plum) ;  2)  worsted- and-cotton  fabric.  —  In  both  senses  named  after the  city  of  Orleans,  south  of  Paris, orlop,  n.,  the  lowest  deck  of  a  ship.  —  Du.  over¬ loop,  ‘deck  of  a  ship’,  lit.  ‘that  which  runs  over", fr.  overlopen,  ‘to  run  over’;  (see  over  and  leap); so  called  because  it  covers  the  ship’s  hold. Ormazd,  n.,  the  principle  of  good  in  the  Zoro- astrian  religion.  —  Pers.,  fr.  OPers.  Auramazda, fr.  Avestic  Ahuramazda,  lit.  ‘wise  lord',  a  com¬ pound  of  ahura-,  ‘a  god,  a  good  spirit’  (see ahura),  and  ma(n)dzdha-,  ‘wise’,  which  is  a  com¬ pound  formed  from  the  I.-E.  bases  *men-dh~,  ‘to apply  oneself  to’,  and  *dhe-,  ‘to  put,  place’. From  base  * men-dh -  derives  also  OI.  medha, ‘wisdom,  intelligence’.  For  other  derivatives  of this  base  see  mathematical.  For  base  *dhe-  see do  and  cp.  theme,  fact.
...TAIL...
orpine,  orpin,  n.,  stonecrop,  Sedum  telephium.  — F.  orpin,  ‘stonecrop’,  lit.  ‘a  plant  with  yellow flowers’,  shortened  fr.  orpiment.  See  prec.  word. Orpington,  n.,  a  breed  of  domestic  fowl.  —  Named after  Orpington,  a  village  in  Kent,  England, orra,  adj.,  odd ;  extra ;  superfluous.  —  Dial.  Scot. ; of  uncertain  origin.
orrery,  n.,  an  apparatus  showing  the  motions  of the  planets.  —  Called  by  its  inventor  Rowley after  the  name  of  his  patron  Charles  Boyle,  4th Earl  of  Orrery.
orrho-,  combining  form  meaning  ‘serum’.  —  Gk. oppo-,  fr.  oppoc  or  op 6q,  ‘watery  fluid,  whey’, which  is  cogn.  with  L.  serum,  of  s.m.  See  serum, orris,  n.,  gold  or  silver  lace  or  braid.  —  Corrup¬ tion  of  OF.  orphreis.  See  orphrey. orris,  n.,  the  Florentine  iris.  —  Prob.  fr.  ML. yreos,  �
```


## [2026-09-05T18:23:58.006Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\nlines=t.split('\\n')\nprint('leaf of Ormazd:', '\\n'.join(lines[:168881]).count('\\f'))\nprint('leaf of ahura:', '\\n'.join(lines[:10008]).count('\\f'))\nEOF",
 "description": "Check KLN_1971 pagination"
}
```


### [2026-09-05T18:24:00.066Z] TOOL RESULT

```
formfeeds 0
leaf of Ormazd: 0
leaf of ahura: 0
```


## [2026-09-05T18:24:16.364Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nprint('leaves',t.count('\\f'))\nimport re\npages=t.split('\\f')\n# find leaves whose text contains standalone 4-digit numbers 10xx-11xx\nfor i,p in enumerate(pages):\n    m=re.findall(r'(?<![\\d])1(?:0|1)\\d\\d(?![\\d])',p[:200])\n    if i in range(575,600):\n        print(i, repr(p[:60].replace('\\n',' ')), m[:5])\nEOF",
 "description": "Inspect Klein leaves near Ormazd"
}
```


### [2026-09-05T18:24:18.206Z] TOOL RESULT

```
leaves 902
575 'OHG.  ort,  ‘point  (esp.  of  a  weapon  or  a tool),  angl' []
576 'e  ecology, oecumenic,  oecumenical,  adjs.  —  See  ecumeni' []
577 '  The  sense  development  is due  to  a  confusion  of  the' []
578 ' the  ending  see  suff. -aceous. Olethreutidae,  n.  pi.,  ' []
579 "ding, portentous,  ominous',  fr.  omen,  gen.  ominis.  See" []
580 'pretation  of  dreams. oneiromancy ooze oneiromancy,  adj., ' []
581 'aining  eggs  (zool.)  — ModL.  ootheca,  compounded  of  oo' []
582 ';  anything  soothing;  tr. opinable 1088 1089 v.,  to  trea' ['1088', '1089']
583 'ts.  —  F.  opticien,  fr.  ML.  optica.  See next  word  an' []
584 'ng  to  an  orator’,  fr.  orator.  See  orator, oratory,  n' []
585 ' coin,  prop,  subst.  use  of  the  adj. aureus,  ‘of  gold' []
586 's  American  birds  of  the  family Icteridae.  —  F.  oriol' []
587 '�orris  root’,  which  is  identical  with  Gk. Epecoe,  gen' []
588 '  vowel  osche-,  combining  form meaning  the  ‘scrotum’.  ' []
589 'a  vowel, osteal,  adj.,  bony.  —  Formed  with  adj.  suff' []
590 'h’.  See oto-  and  cyst. otolith,  n.,  chalky  matter  in ' []
591 'fr.  OE.  ofen,  rel.  to  OFris., MDu.,  Du.  oven,  OHG.  ' []
592 "ddling,  moderate,  indifferent,  tol¬ erable',  orig.  ‘bei" []
593 'n.,  a  genus  of  plants  of  the  staff-tree family  (bot.' []
594 '  n. paginal,  adj.  —  Late  L .paginalis,  ‘pertaining  to' []
595 '  fr.  L.  pala- tium,  ‘palace’.  See  palace, palatinate, ' []
596 'n. Derivatives :  pall ,  tr.  v.,palli-al,  adj ,,pall-ed, ' []
597 ' palpitdre,  ‘to  move  quickly,  tremble, throb’,  freq.  o' []
598 '  in  choledoch,  synec¬ doche. pandemic,  adj.,  widely  ep' []
599 '� ed  of  raxv-  (see  pan-)  and  <1096?,  ‘wise,  clever’.' ['1096']
```


## [2026-09-05T18:24:30.495Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"hanä\" \"handāma\" \"handama\" \"haṇdāma\" \"paitidāna\" \"paiti.dāna\" \"gao.dana\" \"gaoδana\" \"gaodana\" \"dātō.bara\" \"dāto.bara\"; do echo \"--- $w\"; grep -n -- \"$w\" BRT.txt | head -5; done",
 "description": "Grep Bartholomae for Avestan forms"
}
```


### [2026-09-05T18:24:32.408Z] TOOL RESULT

```
--- hanä
4696:•  j.  ama'vant-,  g.  Sma'vant-  Adj.  (fem. 'vaifi-)  'kräftig,  stark,  mächtig,  gewaltig, wuchtig'i  a)  vona)  Menschen  und  ß)  Göttern : o)  narf .  .  pancajiasanhö . ,  hrpzats  avi.- amahe  'vatö  Yi.S.i$;  — ya'ia  agj?  'va .  .fraxitäne  z?ma  paiti  Y.5. 20;  —  aisäta "iwa  'vantaslä  buyamä  (sd.)  Y.4J.4;  — , ^vm  yäka  ^vifrö  naväso  Vyt2;  Az,2;  — | faritJm  il  ^icJ  yähanä  tat  °vatqm  kyat ^wä  xiayqs  (sd.)  aissm  dyll  'vantim  "eine Frage  von  dir  (d.  i.  Zar^  ist  ja  wie  eine Frage  Mächtiger.."  Y.^l^.io,  zit.  A.  4. 3, wo  amavanlam  und  amavant^m ;  —  °fa (NSm.)''  äs  Vfri^rava"^  nqma  v^rp^rava] Os  'va  nqma  Yt.  i4'S9-  ß)  ralnul bjrTZö  yö  '»i  Yt,JO,ioo,  i2.6;  /7.16,  J2. ' 5;  — yö  {sraolö)  .  .  niaza  'va  firS^raja'^ , Vr./5.3;  —  °va  mt^rä  Yt  10.  loj ;  6,  25, loa;  —  airyamarigm  .  .  'vantpm  vprjhrd- ^
4842:dayil(sd.)  SiSvä  marftaHbyU  Y.2g.'];  —  «j.  ayaptö.dä't^ma- Adj. 'der  am  meisten 34.2  (^adhanä); — ydha  ta  r..»(5><fÄriiSi 'Almosen  gibt',  mit  Dat.:  ^Jt  ^awÄiw  «a«ij'^ .  .  yä  voha  y.3<).  4;  35. 3  (vahista).  S.  \  asavabyS  'masca  (statt  NP.)  asp»rjzö.dät?- noch  r,  (/.  masca  P.  4Q.
6073:—  yS  möi  'säi  haülm  (sd.)  hatä  var9saiti\hnii  'sähe  yat  vahistahe  (näml.  ratavö) Y.  46.  19;  —  spinia  mainyB  vahiiiäcä  \  mazds.frasästa  .  .  Y.  7. 10;  usw.  0)  GS. manatjhä  'säl  haiä  lyaohanäcä  valaahälä  ,  mit  gai'^ä-  (sd-,  auch  fdSt)'*:  'sähe  gatia ahmäi  dqit  .  .  mazda  "für  den  heiligen  |  Y.  ^.  3 ;  usw.  e)  AbL  mit  haca  dnw. Geist  und  für  das  nach  dem  göttlichen!  2  a  ß,  mit  vahista-,  yazatoHbyB  . .  y5i Recht  beste  Denken,  Handeln  und  Reden  I  h^nii  yasnyäca  vahmyäca  'sül  haca  yat wird  uns   -"  Y,  47.  i.         b)  im  jAw.:  1  vahiltät  Y,  1. 19;  77.  10,  V.  j.  2,  Yt  8. 15,
7871:•  g.  i  cnkl.  Part,  der  Hervorhebung": iiä  T  AaPiyä  (sd.)  Y.5J.6;  —  äira  l kudaitkl  yahanä  vaidtmnäi  manankä  Y. JI.a2.
10715:gAw. :  ahya  '"kräXa  maziiiäcä  *hvapa- nhäisca  (sd.)  tsm  at  ,  .  yasamaidl  Y.^J/. a;  —  kudä  (sd.)  asim  vohuca  maus '%r)m^ä  Y.  25.  1 1 ;  —  yüism  aäbyS  .  . aogü  data  .  .  '%nmc3  .  .  yl  kuhitts  rä- mqmcS  (sd-)  däl  Y.  2p.  10;  —  isasä  (sd.) . .  maibyö  '"^nm  aojönahvat  yehy3  vfndä (sd.)  vanalmS  *drujim  Y.J/.  4;  benutzt V.ao.  8;  —  tat  mazdä  tava  '>rfm  yä  .. düAf  drigaov!\sA.)  vaiyj  Y.ß^.g;  — yJ vahyJ  varihSuS  dagdi..ahurö  '"S^rä  mazdä Y.5J.  6;  —  tici  '^rä  mazdä  dqmis  (sd.) ahurS  'V.4$.T,  9;  —  maibyS  masds  tavä rafinS  JräxStuiam  (sd.)  kyat  ^wä  °&rJ a/Jt  hacä  frqifa  Y.  4!?.  1 4 ;  34. 15;  —  y} dfmanahyä  'hnm  M^rahya  vä  daSySu:" va ../radahäi{sA.)  aspinzatä  Y.Ji,  16;  — yastJm  °ärJ/  mazäJ  mSÜai  (sd.)  jyätSul Vä  Y.  46.  4;  —  at  ratqm  zara'iuitrS  .  . dadäiij  paurvatätim  . .  mazdiU . .  ux^aHyäcß (sd.)  ifraespm  '"irimcä  "..  den  Gehorsam und  die  Herrschgewall"  \.33.i4;  benutzt Yt  IJ.  88 ;  —  vauhstts  dazd,l{%ü.)  manau/iS lyaöhananqm  a»fiSus  mazdäi  ''knmca ahuräi  a  X.2-j.iy,  —  hux^a^rSJimäi (sd.)  .  .  '"ir^m  .  .  äad)mahicä  cismahicä *hvqnmakicä  Y.^5. 5;  —  yS  dngvSUi '"^nm  hunüiiJ  {?,d.)  Y.j/,  15;  —  yais *ffrMm3{sd.)  asäivaratä..°'^r3mca  lianqm *dnfim  Y. 32.13;  —  '>rais  yujin  (sd.) karapanU  .  .  akäis  syaohanäis  .  .  Y.  46. II.  a)  mit  Gen.  'über  — '  (s.  2  a);  tarn
--- handāma
--- handama
18377:in  eschatologischem  Sinn'';  i)  in  den'  —  *>  Anders  Gdn.  stad,  /.  103, Gäha%:  ärmaiii  tjmi/lm  (sd.)  äaivj..a/ii  ,  j.  ßan-  V.,  nur  mit  zT 'auseinander- AatS  (sd.)  Smavat  vpäB  mananhs  *°ÄJ«  !  renken'.  Praes.  30  (Iter.) /jS««^«-. "durch  Arm.  schenk  . .,  durch  VM.  diel  '(durchziehen,  Zerren)  verrenken':^«/ Belohnung"  Y.j^-"-  a)  mit  AbL  und ' .  . /^5  ♦^a^Ä'»»  nämayänH  vT  maü.yafvm äsva. 'Entschädigung  für-':  iu%ra  ärötf  ßs„ayänH  vupa  handama  razayeinH"vam *a*-tuikukram?nidiia  axrtat"woiaidt\\^  ^  (sie)  das  Rückgrat  (des  Rinds)  ein- die  Vergeltung   iUr  das  (erlittene)   Leid,,  drücken,  den  Rumpf  verrenken,  alle  Glieder
--- haṇdāma
--- paitidāna
--- paiti.dāna
--- gao.dana
9788:•  j.gao-dana,  °jiana-  n.  1)  'Milchgeföss': frä  tl  Aasaanm  xam  aam  . .  frasnaymi ''.an?m  avi  hatUaiinh  ya^  asti  puirake >rims"^e  tausend  Quellen,  die  zum  Milch- gefiss  zusammenfliessen,  das  die  Nahrung des  Kindes  ist"  V.  21. 7  ".  s)  überh. 'Gcfäss,  Napf,  Schüssel'  (nur  Komp.,  s. N.  64).
--- gaoδana
--- gaodana
4006:—  Vgl.  gaodana-.  —  Pü.:  transski.  (als  EN.).
14930:8^9  '*'paiti£a.gaodana-
14931:•  j.  *paitida.gaodana-''  Adj.  'verschiedene
15005:•  j.  pattina- Adj.  (fem.'nj-)  i) 'verschieden, gesondert':[°nam]"  hämcj^ariha  *pailiia.- gaodana  (sd.)  *nam  alte  *xläudrini  tao- '^ram  darsis  hamqm  päpthwqm  N.  64't 64'-  a)  ASf.  °nqm  als  Adv,  'diverse' (nur  Komp.).  2)  'einzeln' :_yjini^  ahmst yämanqm  'nqm  sairinqm  (sd.)  aSaval  .  . V.Ä8s;  — yavat  ahtnäi  'n
15007:•  j.  paitinqm.  gaodana-  Adj.  'verschiedene Schüsseln,  Näpfe  benützend,  aus  ver- schiedenen Schüsseln  trinkend':  paitinam.- i^ariia  (sd.)  'na  (ND.)  N.  64.
--- dātō.bara
--- dāto.bara
```


## [2026-09-05T18:24:40.144Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"handäma\" \"hqndäma\" \"haqdäma\" \"paitidäna\" \"paitiifäna\" \"paitida-na\" \"Mundbinde\" \"dätö.bara\" \"dätöbara\" \"Richter\" ; do echo \"--- $w\"; grep -n -i -- \"$w\" BRT.txt | head -6; done",
 "description": "More Bartholomae greps"
}
```


### [2026-09-05T18:24:42.111Z] TOOL RESULT

```
--- handäma
19642:_fr(rydit . .  a  *yqnasat  (AblS.)  •>  a  mnhrt- sascit  V.  6. 2  7 ;  —  ava  hl  yarum  bSjyamanS Vd.20.  ß)  bei  Tieren,  sva.  'Rumpf: ^faräim  .  .  vT  'yqram  fiänaydnti  (sd.) handäma  . .  Yti4.  $6.  b)  des  Heers, 'Zentrum' :  visfie  karanS  rasmanS. .  yqrum . . sfi^ahe  Yt  lo.  36;  13. 39.
25224:i)  'richten,  gerade  richten,  ordnen':  yat \sp3ta  han/asänte  .  .  ra/t^m  rasma  kata- rasHt  "wenn  die  beiden  Heere  zusammen !  treffen  .  .,  ein  jedes  eine  (in  Reihen)  ge- richtete Phalanx"  Yt  i4-  43;  —  antan \  rästa(ADm.)rasmanaYti4.4T, — yahmya !  sästärU . .  paoiril  Irs  (sd.)  rätayente  Yt.  10. 14.  a)raii';'walsAdv.  sbes.  a)'recken (gewaltsam),  verrenken':  vT  maityqmm fiänayeinti  {s^)  vTspa  handäma  räzayänti Yt  14-  56.
--- hqndäma
--- haqdäma
--- paitidäna
--- paitiifäna
--- paitida-na
--- Mundbinde
--- dätö.bara
--- dätöbara
--- Richter
3156:•  j.  a-Caetar-  m,  'Bestrafer,  Richter': mHr)m  ..'tär>m  mti:rö.dru)qm  YtlO.  26.
6749:Ableit.  —  Pü.:  amar  zaminih.  —  ')  NA.  hat  I  der  (beste)  Richter  ist  er  (näml.  Zar.) hier  und  V.  /.  54  i/^sonsi  (8mal)  sisi.  gemäss  dem  heüigcn  Recht,   der  .  .*'  Y.
6752:•  ).  a-ham.baoS^mna-  Adj,  'nicht  wahr-  Oberherm  und  Richter  und  als  den nehmend'  sva,  'der  seine  Sinne  nicht  zu  ersten  Lehrer  der  Menschheit"  Yt. /_J.  1 5  a ; brauchen  weiss'  (vom  Hund):  yat  ..  sfä\ —  ya^a  fr3  loa  (sd.)  ämraot  yat  dim •n<s  Tä  haiat  aoäitySjxratus  "wenn . .  ander- '  ahümca  ratutn^a  ääadat  "'ya^a'  sagt  aus, seits  ein  Hund  seine  Sinne  nicht  zu '  dass  sie  ihn  (näml.  Zar^  als  A.  und  R. brauchen  weiss,  der  (weil  er)  nicht  recht  eingesetzt  haben"  Y.Jfj.u;  Yt  7^.92;  — bei  Verstand  ist"  V.  /_J,  35;  —  yesi  nnl<yailqm  ns  ahurS  maeäh  .  .  vatsks  valaa spS  'nS  mafye  v3  .  .pai'jyäite  aAmai(sA.)\{sA.)  atiqm  zaraiustr5  ankuca  (NS.)'' heüa  irisylt  "sonst  könnte  der  Hund,  der  ratu^ca  Vi.iö.i;  Yt./j.gi;  —  allai  dim seine  Sinne  nicht  recht  zu  brauchen  weiss,  lUsfanam  maziit?m  dazäyli  (sd.)  ahümca in  eine  Grube  ..  geraten"  V.  j_j.  37.  .^ratämca  yim    ahunm    mazdqm    Y.  27.  i;
6761:hen',  m  Vcrbmdung  mit  oder  m  Gegen-  ^^  Amt  des  *,«»:..»  hatte  im  Gegen  sativum saU  zu  ralav-  (sd.)  —  wie  stets"  —  Amt  des  tiafmini  der  Richter,  denen  in  Iran vom  Inhaber  der  'Königsgerichtsbarkeit'  der  eine  Jlalaf  gegenliberstandf,  der  dem  Prie- (Leist  Altar.  Jus  genL  349)  oder  dessen  =""',''.",^  anBehöri  haben  ,v,rd).S.  noch  No*-) ,-  j    ■'      .°     .  ,■'  V         ,      j         .        und  •*•>.  —  •*)  Das  Rind  ist  dazu  geschaffen,
6767:herro  noch  Richter  gemäss  dem  heiligen  ^ämi-,  erl.:  ^atäl;  a^ih;  s.  noch  No.  3f. Recht"  Y.  2^,  6"';  —  is  aSs'qm  (näml.  der  —  ■)  V.  i^.  13  beweist  nichts.—  Die  Stelle Bewohner    des    Var)   asH    anhuifa   (NS.)  '>       von  aAü-  in  der  Verbindung  mit  ralav-  wird
6828:Leben  heilende  Richter',  von  Zaraiustra:  ySi  rS  fyaoiaiiais  särmte {?,&.)  »rJ  (s.  aa)«
```


## [2026-09-05T18:24:59.032Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== PHD handam/padam/panam/dastwar/dadestan/dan'; grep -n \"^handām\\|^handam\\|^padām\\|^padam\\|^panām\\|^dastwar\\|^dādestān\\|^dādistān\\|^dād \\|^dādwar\\|^dāwar\\|^dān \\|^dāstān\\|^nihādan\\|^nihān\\|^nihuftan\" PHD.txt | head -30; echo '=== PHD_mackenzie'; grep -n \"^handām\\|^padām\\|^dastwar\\|^dādestān\\|^dādwar\\|^dāstān\\|^nihān\" PHD_mackenzie.txt | head -30",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-05T18:24:59.104Z] TOOL RESULT

```
=== PHD handam/padam/panam/dastwar/dadestan/dan
513:nihuftan 60 nizar
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
5345:dastwar dastwarih jastan dastag dast(a)gird
5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
=== PHD_mackenzie
1916:dastwar [dstwbll M dstwr, N dastilr] authority, priest, minister.
```


## [2026-09-05T18:25:03.635Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"handām\" \"padām\" \"dastwar\" \"dādestān\" \"dādwar\" \"dāstān\" \"nihān\" \"dān\\b\"; do echo \"--- $w\"; grep -n -o -- \".\\{0,160\\}$w.\\{0,200\\}\" PHD.txt | head -4; done",
 "description": "Context grep MacKenzie"
}
```


### [2026-09-05T18:25:24.670Z] TOOL RESULT

```
--- handām
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,200}
                         \___exceeds complexity limits


--- padām
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits


--- dastwar
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,200}
                         \___exceeds complexity limits


--- dādestān
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,200}
                            \___exceeds complexity limits


--- dādwar
ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,200}
                         \___exceeds complexity limits


--- dāstān
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,200}
                          \___exceeds complexity limits


--- nihān
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,200}
                        \___exceeds complexity limits


--- dān
161:with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wn
166:earless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=
191:i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' =
191: Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, wardi
```


## [2026-09-05T18:25:30.225Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in handām padām dastwar dādestān dādwar dāstān nihān; do echo \"--- $w\"; grep -n -F -- \"$w\" PHD.txt | cut -c1-40 | head -4; done; echo; echo '=== python context'; python3 - <<'EOF'\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor w in ['handām','padām','panām','dastwar','dādestān','dādwar','dāstān','nihān','nihādan','dān [','dādan']:\n    print('###',w)\n    for m in list(re.finditer(re.escape(w),t))[:3]:\n        print('  ...',t[m.start()-60:m.start()+160].replace('\\n',' '))\nEOF",
 "description": "Python context search in PHD"
}
```


### [2026-09-05T18:25:31.935Z] TOOL RESULT

```
--- handām
392:hamēstār, —ih [hmyst!l, -yh] = h
396:hannàm [%7m | = M] = handām. Harbo
2634:limb handām, (hannām), pēšag.
2776:member handām, (hannām), pēšag.
--- padām
--- dastwar
310:das [d’s | N ~] sickle. dàs?r [d�
897:authority dastwar(ih), sálárih.
1473:ar. custom dastwarih, éwén(ag). c
2816:minister dastwar; prime — wuzurg-
--- dādestān
172:a-dàd [471], a-dādestān [?- DYNA,
306:īdabr [dpi] sinner, deceiver. *dabr
757:agreeable ham-dādestān.
1168:case (law) dādestān, jadag,
--- dādwar
306:īdabr [dpi] sinner, deceiver. *dabr
5543:dādwar Sy тех dādwarīh xD у 
--- dāstān
--- nihān
512:nest [LOY T! < А P?yty | M nyst, N 
3552:secret (a.) nihānīg, razig.
5242:weh . nihānīg nihān wehih wehdin

=== python context
### handām
  ... ] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise. handāxtan
  ... ytn' | N ~] = hixtan. hannām 43 hixtan hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlw
  ... ón, hamgonag. liking dēšišn, passand(išn). lily sēsan. limb handām, (hannām), pēšag. limbo hammistagàn. lime Carag; (a.) čārūgēn. limit kanarag, karan, saman, wim- and. limited brin, kanáragomand, wiman- dig, wimandómand
### padām
### panām
### dastwar
  ... àrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. daš
  ... s. auspicious humurwag. authoritative радіхха(у). authority dastwar(ih), sálárih. axtar(ājmār,  staró$màr e-- chamber pādixšāyīh, 103 authorized pādixšā(y). autumn pādēz. average mayānag. avert ānāftan. Avesta abestāg. a
  ... on balén, Бап. бео аа (of stray animals) apédag- ar. custom dastwarih, éwén(ag). customary šūnīg. cut (n.) brin. cut (v.) b(u)ridan, tāšīdan. cutting (a.) burāg. cutting (n.) burišn. cypress sarw. daevic creature wišūdag
### dādestān
  ... itable, Jee ~ag [-k'] compelled. a-dad 5 -ag a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitive
  ... reation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg
  ... ed, be — ayārdīdan. agitation ayārdēnišn. 102 agreeable ham-dādestān. agreement husāzagīh; pašn, past; (document) pādixšīr. agriculture warz. Ahuramazda Ohrmazd. air andarwāy, way; of the ~ andar- wayig. alas ala. alert 
### dādwar
  ... egal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl
  ... S t€. X5 dādgāh Tr хэ dādīg 155 t$ dad, jad, yat, yazd weno dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI E
  ... h Tr хэ dādīg 155 t$ dad, jad, yat, yazd weno dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 O
### dāstān
### nihān
  ... e, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few. nihuftan 60 nizar nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) 
  ... gahan, 132 ENGLISH-PAHLAVI INDEX secrecy nihan. secret (a.) nihānīg, razig. secret (n.) raz. sect ristag. sectary kēšdār; v. heretic. section kardag; darak, had. security graw(ih), graw(a)gàn. sedentary maniStag. see did
  ... dgirdag wād wādrang wüdrangboy wādbān nabānazdišt tāt weh . nihānīg nihān wehih wehdin wihēz wihcz- wihczagig wihezag Iwiydbin wivüftan 1 wistan PAHLAVI KEY up pase va Uni ale) VA rene VOU el S ve» 1st rer) We? 2S rex Zu
### nihādan
  ... gwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] conceal
  ... m(ag). purposeful čimīg. purulence rëm. purulent тётап. put nihādan; ~ on pēšīdan, paymóx- tan. quadruped čahārpāy. quail karak. quake čandīdan, wizandidan. quaking wizandag ; wizandišn. quality (accidental) jadišn. quan
### dān [
  ... а, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: p
  ... h: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unsk
  ... in. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert
### dādan
  ...  M the same spelling in M, etc. ADDENDA ET CORRIGENDA /abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity.
  ... аа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N
  ...  damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N g
```


## [2026-09-05T18:25:45.937Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor w in ['veil','mouth','pandām','panám','padám','pad?m','dād [','dād,','law dād','justice']:\n    print('###',w)\n    for m in list(re.finditer(re.escape(w),t))[:4]:\n        print('  ...',t[max(0,m.start()-120):m.start()+200].replace('\\n',' '))\nEOF",
 "description": "PHD veil/mouth/dad"
}
```


### [2026-09-05T18:25:48.268Z] TOOL RESULT

```
### veil
  ... N ~] goat. Cübuk 21 čāšnīģ `” C čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-ра
  ...  (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] acco
  ... āy. Vega Wanand. vegetable aroyisnig, tarrag, urwar; ~s ümiz. ENGLISH-PAHLAVI INDEX vehemence tundih. vehicle wardyūn.. veil čādur, pardag. vein rag, rahag. vengeful kénig, kénwar. venom wii, zahr. venomous wišoūmand. Venus Anāhīd. vernal waharig. vertebra muhrag. very abēr, saxt, staft, Skeft. vessel jām(ag), kabārag,
### mouth
  ... 2 āsūdan arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfittin
  ...  M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land. dahigan 24 darzig dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; 
  ... eive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M 
  ...  wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-yt
### pandām
### panám
### padám
  ... čīdan pēš pēšānīg pēšūbāy pēšūbāyīh PE pēšār pēšārwār pēšgāh pēšēnīg pēšēmāl pēšēmālīh pēšūbāy pēšūbāyīh pēškār, pēšyār padám payádag 1-2pay, pīh pas, "pay pés pēsišn passand passand- passandišnīg passandišn passandīdan penīh pen payg pir pil payray- fīlāsūfā payrāyag pērāmēn Payrāstan pīrīh péroz pérézih pérozgar C 60
### pad?m
### dād [
  ... yz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn:
  ... n, pillow. bam [bm | = M] brilliance, glory, splendour. bāmbišn [MLK TTA < A тіке; РпЬй! | M Pnbyfu] queen. < dmana- bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P 
  ... ereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix 
### dād,
  ... d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : 
  ... lerate sāxtan. toleration sāxtārīh. tomb aspānūr, dādgāh, daxmag, hazzān. tomorrow fradāg. tongue uzwān, (zuwān). tooth dād, dandān. top bālēn, bašn, sar; v. summit. torment (n.) āzār(išn), bēšišn. torment (v.) āzārdan, (āza/urdan), bištan, (béSidan). tortoise kašawag. totality hamagih. touch (n.) pahrmahagih, pahrmāhi
  ... te haménidan. united ēwkard(ag); be ~ hambüdan. universality hamagih. ENGLISH-PAHLAVI INDEX universe hamkišwar. unjust adād, unlike ahomanag. unlimited akanárag. unmixed agumég. unpleasant axwaš. unreliable anēst. unrepentance | anabaxíáwandih, a- petitigih. unrepentant anabaxšāwand, apetitig. unrest anāštīh; v. turmo
### law dād
### justice
  ... cI] inevitable, Jee ~ag [-k'] compelled. a-dad 5 -ag a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: 
  ... br [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. giv
  ... dār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da
  ... a/urdan), wizastan, (wizüdan), xastan. injurious wizayišnig; v. harmful. injury āzārišn, azarm, wizāyišn, wizend. 120 injustice adadih, adadestanih. inn aspinj. innocent awināh, abēwināh. innumerable amar, anēšmār, азар. insert passāxtan. inside andarēn. insight, spiritual ~ ménégwénih; having ~ ~ méndgwén. insolvency
```


## [2026-09-05T18:25:58.412Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in 118 127 236; do echo \"############ HRN printed p.$p (leaf $((p+21)))\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -60; done",
 "description": "Print Horn pages 118, 127, 236"
}
```


### [2026-09-05T18:26:00.029Z] TOOL RESULT

```
############ HRN printed p.118 (leaf 139)
- 118 —
533. ~dän 'Behälter , vergl. äbdän, nemekdän etc.
aw. awz\da?ia- ; ai. -dhäna- *Behälter\
oss. d. 'döne, t. do7i (110); wa/. sar. -dän,
534. daniHteti 'wissen*, Praes. dän-em, dünä, danls^ ferzam
(No. 815).
g. znnädmün^ ta e-züni (2. Sing.); taJ. züne, hezin
(Impt.) ; gel. dänisten; mäz. dänussin, ddn^ dün (Inipt.);
Kä§. züneden^ zönö^imün^ ziinün, zönäti, zön6n (Aor.).
ap. adänä er wusste' (ap. V^ dan- — arisch I/^ian-);
aw. [/^zaU' 'wissen', paiti].2änatä; phlv. dän(i)stan,
dünak, dänakihj dän(i)sn ; ai. jfändti {l/^Jan- ')) ; arm.
canatif 'bekannt*, ancan 'unbekannt*, cmiäcem 'kennen'
(H. No. 134).
kurd. zänin 'wissen* ; af/. pezanam {ijuti-) ; oss.
d. zönum^ zönun, t. zönin^ zönin (134); bei. zdnag,
n. zänay (422); sar. pad-züti-am, va-zün-am, v/a/. paz-
dan-am,
Friedrich MüUer's Aufstellung, WZKM. IV, 309
scheint mir im Wesentlichen verfehlt.
535. däne 'Korn , arab. dänaj (auch säli]dänaj, sah\danag,
pers. säh]dane)^ dänöe 'Linse*.
aw. düiiiö.^karsa' 'körnerschleppend'; phlv. dänak;
ai. dhänd' 'Getreidekörner*.
kurd. däni (LW.), daneki; bei. (LVV. ?) dän, däniu/,
n. dän, danay 'Korn' (74); af/. LW. däne; sar. pinj]-
dand 'Fünfkorn* d. i. 'Hirse*.
536. dang, däneg 'eine Münze bezw. ein Maass*.
ap. öavay.r} (Herakleides im Etyni. magn.); phlv. dang
(PPGl.), arm. LW. dang, arab. LW. danaq , mand.
LW. Np3xn 'Obolus*, syr. talmüd. LW. pr\ (de
Lagarde, Ges. Abh. 32).
Ursprünglich mit däne (No. 535) identisch.
537. däwer 'Richter*, däwen,
aw. *dätö,bara'; phlv. dätwar, däthar (bezw. dätebar),
dawar, arm. LW. datavor, vergl. a7ia\^aöovd<i 'Heeres-
richter* (Chron. pasch, p. 709, 1, 2).
») Vcr^l Bartholomae, BB. X, 278.
############ HRN printed p.127 (leaf 148)
- 127 -
ap. "^dastabara-; phlv. dastwar, dastbar.
Nicht zu dest *Hand\ sondern zu der in aw. dqsfva-
etc. steckenden Wurzel dmts- (Darmestetor, Et. ir.
I, 115 Note)'). Zu derselben Wurzel stellt Nöldeke
(mündliche Mitteilung) auch np. dästan-), destan *Go-
schichte, Erzählung .
5()9. duH^^är, duSvär 'schwierig*, dus/'ün, dusvan,
aw. vergl. duzadra- (Geldner, KZ. 25, 478, Studien
I, 17 folgg.); phlv. dus/J'är, dmx'arlh.
Die neup. phlv. Formen sind Neubildungen aus
dus+x"^'^ (No. 49G).
570. destän 'menstruirende Frau'.
aw. da/stavaitl-; phlv. dastän (arm. LW. dasfan;
chald. LW. ]P\'^'^)j dastan(i)stan^ vorgl. dayßak,
571. dil *Herz', diler (reimt auf ser, Sahn. I, 195, 1194).
aw. zered- (y. :n, 12), zaredaya- *lIorz*; phlv. dil,
päz. diler (Men.); ai. hfd-, hfdaya-; arm. sirf (IT.
No. 250).
kurd. zar 'Herz*; af/. zra; oss. d. zärdd^ t. z'ardä
(131); bei. ^^zVc/c (420); sar. zärd^ si;'n. -^^Il), <m//,
sangl. mrütj^ minj. 2?/.
np. rf// ist ausserdem in alle iranischen Sprachen
entlehnt, meist ohne einen Bedeutuugsunterschi(^d mit
dem betreffenden einheimischen Woite aufzuweisen
(Ausnahme: Tomaschek, S. 78()).
572. dem 'Atem, Atemzug', deine^ demulen 'wehen, blas(Mi\
demäy^ demär,
ai. V^dham-', dhdmiti 'hauchen, bhisen*; phlv. dam;
ksl. dümq, dqti 'blasen'.
< . •
') Bartholomae (BB. 15, 86) legt dieser Wurzel die Bedeutunjij
einweihen, weihen* bei. Dazu passen aber inoht die ebenfalls dazu
gehörigen ai. dasmä-^ dasrä-. Geldner übersetzt KZ. 30, 329 aw.
dldaihhe mit 'ich wurde unterwiesen*.
«j Anders Fr. Müller, WZKM. 5, 354. - Rückert hat
V ••
übrigens in seinen Bemerkungen zu MohTs Sähnäme-Ubersolzung
auch np. (h'sfür mit desf zu voroinigon versucht.
############ HRN printed p.236 (leaf 257)
- 236 —
1052. nÜH jetzt, nun', vergl. ekniln, kunün.
aw. nü, nürem jetzt', vergl. oss. d. mtr, t. njr 'nun'
(207); §iyn. nur, sar. nur *heute*; phlv. nun; ai.
nündm,
bei. nü^ nun jetzt, nun (270).
1053. uuved *frolie Botschaft.
Die übliche Erklärung aus ni -j- l^vaed-, vergl.
aw. niva^dayemij ist erstens wegen der auffälligen
Erhaltung des d bedenklich und zweitens scheint
wegen np. pizöhlden im PehlevT n(i)v(i)hmUan, nicht
n(i)vedinltan gelesen werden zu müssen (vergl. No. 314).
1054. nöylden 'klagen (Sahn. I, 183 Vers 986, Calc),
necä 'Klage', nevtden, vergl. nevaliden, nallden.
ai. i/'nav-, nünti, ndvate 'brüllen (von Tieren)'; vergl.
np. zlnüden (No. 672).
1055. ne (geschrieben neh) nicht'.
aw. na; päz. na\ ai. nd.
kurd. ne; af/. na; oss. d. ne, t. nä (201).
1056. nu (geschrieben nah) neun'.
ap. navama- 'neunter ; aw. nava, näuma-, naoina-
neunter; phlv. wawm; d^.,ndva; arm. iw« (H. No. 115).
kurd. ne(h), ne(h); aty, LW. nu{h); wa,/, siyn. ndo,
sangl. minj. nao, yayn. nau, sar. nev.
Np. nuhiim ist eine ganz junge Bildung, die man
nicht auf das PehlevT übertragen darf.
1057. nihäden ^hinlegen, hinsetzen', Praes. w/Ä-e/w, aber
neht (AM. 65 Zeile 10).
aw. ni + 1^2 da- {nidadät) 'hinsetzen'; phlv. n(i)hatan
(AV.); ai. m+ l^l dha- (nldadhäti),
1058. nihän Verborgen, heimlich*.
ap. ^nidäna- 'etwas (heimlich) hingelegtes*, vergl.
ind. ni -f- [/'dhä- 'niederlegen zur Aufbewahrung oder
um zu verbergen'; phlv. n(i)hän.
nehmär 'zahllos* siehe sumär (No. 791).
1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
niheirihiden ^), nnhumhtden ^).
') Geschrieben -wZ>-.
```


## [2026-09-05T18:26:14.863Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==148' HRN.txt | tail -30",
 "description": "Horn p.126 end"
}
```


### [2026-09-05T18:26:16.605Z] TOOL RESULT

```
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


## [2026-09-05T18:26:30.007Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls NYB*; for p in 59 60; do echo \"######## NYB II p.$p (leaf $((p+8)))\"; awk -v n=$((p+8+1)) 'BEGIN{RS=\"\\f\"} NR==n' NYB_vol2_glossary.txt | head -70; done",
 "description": "Print Nyberg glossary pages 59-60"
}
```


### [2026-09-05T18:26:31.637Z] TOOL RESULT

```
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
######## NYB II p.59 (leaf 67)
 drg ‘lang’ (A-H ITI); .
MPrs dyr (S); Paz. NP dér.
dagr-pattai [dglpt’y] long-lasting, ever- lasting 10515, — dagr + pattäi (q. v.). Dahäk [dh’k'] n. pr. a devic king, the Dragon 341, 9023. 9512, 9822.27, 993-7. 1064. 11015, v. Aži-dahāk, of which ~ is an abbreviation. — Av. (704) dahäka-; Paz. Dahäk; NP arabized Zahhäk (written Dahhäk ‘the Laugher’).
dahän [PWMH] mouth 1217. 509. 101". 10422, — < *dafän, the SW form of Av. (1657) zafan-, zafar-, v. zafar; MPrs dhyn; Paz. dahan; NP dahán.
dahänömand [—-^wmnd] having a mouth 3912.13.24. i
Dahöstän [dhyst’n'] n. pr. a town in Gurgan 114"; "' Dihistän in the extremity of Mazandaran near Khwarizm and Jur- jan" Yagut 2, 632
Cöl [cwlj n. pr. 1. the name of a Turkish people in Eastern Iran: ~ sākān 113%, — 2. the name of a town in the neighbour- hood of Darband 114!? (Arab Sil, Yàqut 3, 485). — Cat. 39, 44; Arm Cor, AG 218 Sq.
eovčgan [cwpyg’n'] the stick used in playing polo 16!!; the game of polo itself 314.15, 49. 167. — NP caugän; Arab. lw. saulajün-; Fraenkel, Aram. Fremdw. 291; Horn, NP Et. no. 499 and Hubsehmann,
- Prs. St. 53; on the spread of this w. in the
European languages v. Lokotsch, Et. Wb. d. europ. Worter orient. Ursprungs, no. 434.
dahišn [dhšn'] 1. creation, the act of creating 3615-16, 4117.18, 1099. — 2. coll. the created things: dám u ~ 3311. 762. 772.18.14.20, 7913. 881.16, 894, 915-9, 923; — created being, pl. cas. obl. —-ān : ast-~- an, v. ast; menöi u getäh —-än the heaven- ly and the earthly created beings 8816; — 621. From dätan; Paz. dahisn(i). Not in MPrthPrs (NP dihiš ‘gift, alms’ is a recent formation). Coincides in writing with dāšn and jahišn, v. these ws.
dahisneh det. v. n. the act of giving, with a preceding obj.: han hir apér-ic — that this wealth was given too abundantly 1367; kamak ~, hayyārēh ~, v. these ws.
Dahman äfrin [d’hm’n' »"pryn!] “The Blessings of the Holy ones”, a god, the bestower of Justice and Righteous- ness 9210.18, _ dahmän pl. cas. obl. of Av. (704sq.) 'dahma- ‘the religiously fully instructed and initiated member of the Zoroastrian community’ (dah- ef s. v. dastavar); v. (330) Dahma- äfriti-, in- voked in Y. 60 = Afringan I, Phl. v. in Dhabhar, ZkhA 141-147. V. also BdA p. 1756-18, Paz. dahma ‘pious, holy’, Skr. v. uitama (Aog.).
dahom [d’hwm, 10-wm] the tenth 8213, 842, — Av. (701). dasama-; MPrs dhwm (S); Paz. NP dahum.
www.parsianjoman.org | ool wok
dahyupat
dahyupat [dhywpt'] ruler, king: Fran ~ of Vistasp-sah 1917. 6017-2. 1118; of Manušcihr 47°; of the Great King killed by Alexander 107’; Vadagān (g. v.) ~ of Dahäk 902; — pl. cas. obl. ~-dn in a general sense 110?!. 1192”; — subordinated to the Great King: xtatäi u ~ 1274, 7223; xvatčiydn u an [ZK] ~-dn 727); zuatai u ~u sardar u dastavar % den 1081-?, — Av. (681 sq.) datyhu-pati- < *dahyu-pati- ‘lord of the country’; MPrs dhybyd (A-H I); Paz. dahevad, Skr. v. rājan (Mx), dehavad, Skr. v. grāmapati, svamin (SGV). al-Biru- ni, Chronologie 22077, transliterates dahü- fadiya = dahyupatčh.
Daiti [d’yty] the Avestan name of the river Oxus 4024, 565-14. — Av. (730) Dāt- tyā-.
dak [d^k'], v. hu-däk, kār-dāk, véh-dak. dälman [d'lmn'] a raptorial bird, prob- ably the vulture 942128, — < *darnu- mani-, SW form of Av. (1683) zaranu- mani-, an epithet of the kahrkasa, v. karkas. — Phl. Vd. in à commentary on T? has ~ with the NP gl. bim ‘owl’. — NP dalman. V. Bailey, ZP 137 n. 2. dam [d’m] creation, preferably referred to Ohurmazd, but also to Ahriman: created being 637; — coll. the cre
######## NYB II p.60 (leaf 68)
ated beings, the created world 31?! and passim ; ~ u dahišn, v. dahišn; — pl. cas. obl. ~-ãn 7319. 7624. 7716, 7917. 8012, 8922-28, 10215. — From dà-, v. datan; Av. (736) dämi-; MPrthPrs d?m; Paz. dam, Skr. v. srsti; NP dam of animals.
damik [dmyk] earth: 1. as opposed to the firmament 3377. 37, 526, 83-93 passim. — 2. the terrestrial world, 515. 5211, 6710, 8913, 99-104 passim. — 3. ground, soil 926, 21-29 passim. 3316-21, 3916, 606. 89-95 passim, etc. — 4. in a geographical sense 719. 86, 1134. 11517-18, 1173; pl. ~ tha 109%. — SW form of zamik (Ps. zmyk), which occurs just as often in MSS and editions. MPrth Prs zmyg, NP zami, archaic form for modern zamin; Av. (1662 sqq.) zam-.
danistan
damik-cihrak [dmyk cyhlk'] containing the seed (the constituent element) of the Earth 879. — V. cihr- and cihrak and cf äp-cihrak.
damistän [dmst?n'] winter 3711 and often; a dev 8573, 8612; created by the devs 103’; — year 778. — SW form of Av. (1699 sq.) zyam-, zom- (v. hazangrö-zim) + -stän; MPrs dmyst’n (A-H I); Paz. damastan ; but NP NW form: zamistän.
dänäk [d’n’k] wise, learned 217. 5522, 807; comp. ~-tar 11814.22-28, 1201; — subst. a sage, the sage 68—88, passim; pl. cas. obl. ~-dn 22. 415, 55.25, 139. 1074, 1217-12, as cas, rect. 11814, 1193. — MPrs dg; Paz. NP dänä; from dänistan. danakéh wisdom, knowledge 53°. 595. 8817, 9917, 118°; den ~ 27, veh-den m 112!” knowledge of the true religion, theology; v. also visp-dänäkeh.
dänäkihä wisely, with good insight, or judgment 4". 5119. 5322; sup. ~-tom with the best wisdom 59%.
danb [dnby] shore, bank of a river P 1: 3. - SW form; NW zanb: KZSPrth l. 19 znb = Prs l. 24 dnby, Gr. v. yeiXoc.
dandan [dnd’n'] tooth, coll. teeth 29%. 3116, 327-8. — Av. (683) dantan- ; NP dan- dàn (sg., not pl.!).
danditan [dndytn'] to scream, of the speech of devic beings 4214-19, 5022, 541, 5719. 6121. 10312. — < "damditan: MPrth dmdyft, dmdw’’g probably ‘foolishness’, ‘speaking foolishly or mutteringly’, Sogd. 49, cf Benveniste, JA 228, 1936, 234. — Cf *apatundtha.
danistan [YD‘YTN-stn'] dan-, Ist p. sg. danem [YD‘YTN-ym] 21? or danam [~- m] 2819-20, 2nd p. sg. dane [YD*YTN-yh, -y, -yd; d’nyh 41]; cond. 3d p. sg. dänist häh 321: to know, with kū ‘that’ or in- troducing direct speech 2% etc. passim; with indirect interrogative clause in- troduced by ki: ki cand how many 213-4, ku katäm who 21°, ki cé what 218. 305, ku ... atvāp whether ... or 2022-23;
www.parsianjoman.org | ool wok
danistan
dast
~ kē that 397?; with obj.: passim; with inf. to know how to, to manage to 5026.27, 511-2, — Av. (1659) zan-, OP dan-; MPrth z’n’dn z’n-; MPrs d'nystn d’n-; Paz. dä- nastan, dänestan dan-, NP dänistan. danišn [d'nšn'] knowledge 661, 803-5; ~ u kār-ākāhēh 881.23; m <u> xrat 4 martömän 10414; akahéh u ~ 1095, ~ u ākāhēh 111’. — MPrs d’nysn; NP dans. dānišnēh det. v. n.: uspurrikiha (q. v.) ~ 10615-16.
danišnomand [—-"wmnd] possessing know- ledge 803.
dänük [d’nwk'] knee 332. — SW form of zānūk, q. v.; cf Sogd 49-50.
dar [BB”] door 75"; gate, pl. ~ -ihā 8713.18, 11472; hac an ~ in another way 813; har ~ every category 111”; — a royal person's court P1:4. P2:9. 39. 55, 131, 1710, 208-9. 617. 705. 1077. 1097. 1123. — SW form of Av. (766) dvar-, OP duvara-: MPrs dr, Paz. NP dar- as against NW: MPrth br, NP bar. — V. darak, dar-band and dar-handarz-pat.
dar [d?l] tree 3319. 42?! ; pat ~ apar kartan to crucify 208. — Av. (738) dāru-, dru-; MPrs adj. d’rwyn; d’r-gyrdyyh ‘crucifix- ion’ (S); MPrth d’lwg (v. dari
```


## [2026-09-05T18:26:42.383Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dastavar' in p or 'dastvar' in p:\n        print('LEAF',i,'-> printed',i-8)\nfor w in ['dastavar','dätastän','datastan','dāt [','dāt-','dätwar','datvar']:\n    print('###',w)\n    for m in list(re.finditer(re.escape(w),t))[:4]:\n        print('  ...',t[max(0,m.start()-200):m.start()+500].replace('\\n',' '))\nEOF",
 "description": "Find Nyberg dastavar entry"
}
```


### [2026-09-05T18:26:44.174Z] TOOL RESULT

```
LEAF 61 -> printed 53
LEAF 67 -> printed 59
LEAF 69 -> printed 61
LEAF 102 -> printed 94
LEAF 130 -> printed 122
LEAF 136 -> printed 128
LEAF 171 -> printed 163
LEAF 242 -> printed 234
LEAF 281 -> printed 273
LEAF 286 -> printed 278
LEAF 290 -> printed 282
### dastavar
  ... fratäk rēc ce bavet thou knowest what will happen to-mor- row 21°; apdyet butan, v. apčiyistan; būt i zivist u būt i murt hend there were some who survived, and there were some who died 95?” sg.; būt dastavar ké-§ guft there was a certain Dastur who said 1018; būt kē-š guft there was someone who said, erat gut diceret 103?9; h&c kas nē būt ke ... dänist there was nobody 4 % bitan nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; a
  ... the bestower of Justice and Righteous- ness 9210.18, _ dahmän pl. cas. obl. of Av. (704sq.) 'dahma- ‘the religiously fully instructed and initiated member of the Zoroastrian community’ (dah- ef s. v. dastavar); v. (330) Dahma- äfriti-, in- voked in Y. 60 = Afringan I, Phl. v. in Dhabhar, ZkhA 141-147. V. also BdA p. 1756-18, Paz. dahma ‘pious, holy’, Skr. v. uitama (Aog.). dahom [d’hwm, 10-wm] the tenth 8213, 842, — Av. (701). dasama-; MPrs dhwm (S); Paz. NP dahum. www.parsianjoman.org | ool wok dahyupat dahyupat [dhywpt'] ruler, king: Fran ~ of Vistasp-sah 1917. 6017-2. 1118; of Manušcihr 47°; of the Great King killed by Alexander 107’; Vadagān (g. v.) ~ of Dahäk 902; — pl. cas. obl. ~-dn i
  ... 07’; Vadagān (g. v.) ~ of Dahäk 902; — pl. cas. obl. ~-dn in a general sense 110?!. 1192”; — subordinated to the Great King: xtatäi u ~ 1274, 7223; xvatčiydn u an [ZK] ~-dn 727); zuatai u ~u sardar u dastavar % den 1081-?, — Av. (681 sq.) datyhu-pati- < *dahyu-pati- ‘lord of the country’; MPrs dhybyd (A-H I); Paz. dahevad, Skr. v. rājan (Mx), dehavad, Skr. v. grāmapati, svamin (SGV). al-Biru- ni, Chronologie 22077, transliterates dahü- fadiya = dahyupatčh. Daiti [d’yty] the Avestan name of the river Oxus 4024, 565-14. — Av. (730) Dāt- tyā-. dak [d^k'], v. hu-däk, kār-dāk, véh-dak. dälman [d'lmn'] a raptorial bird, prob- ably the vulture 942128, — < *darnu- mani-, SW form of Av. (1683) zaranu
  ... āzītan F:1, reading. very uncertain. KZSPrth l. | to play a bad game, to play the game www.parsianjoman.org | ool wok dast daštan badly 121%, — Av. (1685) zasta-, OP dasta; MPrtPrs dst, Paz. NP dast. dastavar [dstwbl], cas. obl. dastavareh [dstwblyh] 9815 : 1. valid religious doctrine, custom, law 10871; canon of religious doctrines etc. 109°; decision (of a relig- gious authority): pat ~ % oi 101%; <pat> ~ + Hušetar 96; pat hàn à Husetarmäh ~-éh 9814-15, — 2. an expert in religious matters, a theologian, a Dastur, also of the Zoroastrian clergy in general: a theo- logian 1018; x“atai u dahyupat u sardār u ~ + den 1081-2; pl. cas. obl.: ~-dn u dätavarän u hérpatàn u magupatān u den- burtärän
### dätastän
### datastan
### dāt [
  ... ], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place, datistan to deposit 922. 10912; — bē ~ to deposit 395.7:22. 402. 4910. 48?2. 4098-9.22-23, 501
  ...  YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place, datistan to deposit 922. 10912; — bē ~ to deposit 395.7:22. 402. 4910. 48?2. 4098-9.22-23, 5015, 9427; pat damīk bē ~ to lay (an enemy) in the dust 3329; to take off (clothes) 577; — (bé) 0 . . . — to transfer to . . . 88%. 953. 12016, — 2. to create 397. 577-8, 76 20.22 etc. passim. — to prepare 4216, with the gl
  ... 92. 595). — From varz-, v. varz, varzitan. év-bar [’ywb’l] once 1011; (all) at one time 2413-15; pat ~ (both) at one time 10218; once upon a time, in days of yore 1071, — V. žē and bar. Paz. ebär. ēv-dāt [ywd^t'] = ēvak-dāt created alone: gāv îi ~ 10418. év-kanak [’ywk’nk'] unanimous, acqui- escent 574, 68’; pl. cas. obl. —-än clients 712. — Paz. ēugāna; MPrs ‘ywg’ng ‘of the same kind’ (A-H II). évkanakéh [’ywk’nkyh] acquiescence 42°. 712. www .parsianjoman.org | ool jb ēv-mēk frahang ēv-mēk [’ywmwk'] one-shoed, with only one shoe 694, — Paz. émók, v. mok. év-tàk [’ywt’k'] unique, unequalled 56?. 8022. — Paz. ēvadā; cf NP yak-td. farrax" [plhw'] fortunate, blissful, glori- ous 6?; sup. ~-tom
  ... xcretion’ from par? + harz- (v. histan), cf Av. (1793) patri-haroz- ‘to filtrate’, patri-frā-haroz- ‘to ejaculate (sperm).’ — Paz. substitutes pésidr, Skr. v. purah mütraprasräva (for -prasräva). Pēš-dāt [pyšd't'] honorary title of the first king, viz. Hösang 471%. - Renders Av. (854) Para-öäta- ‘put at the head’, ‘the first of his dynasty’. pēšēnīk [pyšynyk] predecessor, pl. cas. obl. ~-dn ancestors 11115, 11216; the troops of the front-line 181, — Derived from pésé, v.s.v. pés. MPrs pysyn ‘earlier’, pl. pyšyng'n; Paz. pl. pēšīnaga; NP pesin(ah), pl. pēšīnagān, pesiniyan. pēš-karp [pyš klp'] of conspicuous shape 56’, with the gl. ku pat tan cašmtar bit. pčš-nčvak [~ ndwk'] foremost in bra- 
### dāt-
### dätwar
### datvar
```


## [2026-09-05T18:26:56.213Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==70' NYB_vol2_glossary.txt | head -60",
 "description": "Nyberg leaf 69 = p.61"
}
```


### [2026-09-05T18:26:58.104Z] TOOL RESULT

```
), @rwbdg ‘crucified’ (S; a much discussed w., v. Verbum 223 sq.; JA 228, 1936, 197). NP ddr "wood, gibbet'; v. also dari.
Darai [dy], patron. Däräyän [d*Pd'*n'] Dareios 18-11-12, 61, 10815, 11613, — OP Dā- raya-vahu-; MPrth d?rw (S), v. Darav- kirt.
darak [dik'] chapter 11218-21, — From dar. Däräv-kirt [d?Ppkrt'| the town Däräb- gird 116%. — Arab Däräbjird, Yägüt 2, 517. Däräv = Däräi (q.v.); as to the alternation -Gv : -di cf s. v. x"atàá.
dar-band [BB? bnd] barrier, fortifications 2377, 241, - = NP.
dar-handarz-pat v. handarz-pat. *darik [*dlyk] courtier, court dignitary
27 drykn s’rr = Prs 1. 33 dlyk?n srd’r, Gr. v. tod tri TOV Špuydvov, cf Syria 35, 1958, 329 n. 15.
dārišn [YHSNN-šn'] v.n. of dāštan: 1. used as pred. (is) to be held 907°. 12118. — 2. [d'lšn'] maintenance (of the body) 682, 7615-17, [YHSNN-Sn] 117%; x%arišn u ~ 2204
dārišnēh [d?linyh] det. v.n. of dāštan: (pus) pat tušn ~ in order to keep (his son) quiet 41°.
darmän [dlm’n'] medicine, remedy 4816-27, 4914, 502. 907. — MPrs drm?n; Paz. NP darmán, Skr. v. ausadha (SGV), pathya ‘wholesome’ (Mx).
därök [d'Iwk] medicine, drug 90". — MPrthPrs @rwg; Paz. NP dari, Skr. v. ausadha.
darrak [drky] ravine, or rock HajB: 7. 13, Prth. equivalent vēm (q. v.). - NP darrah ‘a valley between hills. V. Nyberg, Christensen Vol., p. 69.
dart [dlt'] pain, illness 43?3. 5415, 8620, 905, — MPrthPrs drd, Paz. NP dard.
dārū [*d’lw'] tree 2622, MPrth d’lwg (cf s. v. dar); as for the passage 267? cf A-H III, e, RI, 11-12: ’wn @lwg wzrg ky bšn'n "mšt ‘Oh big tree whose branches were crushed’.
dast [YDH, Prth YD’; dst'], with the indef. art. dast-ē [YDH + 1] 1. hand HajA:11.14. B:12.16. 9% and passim; power 1924, 24%. 304; — ~~ apar nihātan to put one's hand to 6215; — ~ avis burtan to deal with a th. 8119-29; — frac ~ Sustan to wash one’s hands 443-9, with hac to dissociate oneself from, to break off all relations with 384; — a ~ 4... rasitan to come to close quarters with a p. 24?, — pat ~ daštan to have a hold on, to hold sway over 87%, — 2. ~ i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
F:1, reading. very uncertain. KZSPrth l. | to play a bad game, to play the game www.parsianjoman.org | ool wok
dast
daštan
badly 121%, — Av. (1685) zasta-, OP dasta; MPrtPrs dst, Paz. NP dast.
dastavar [dstwbl], cas. obl. dastavareh [dstwblyh] 9815 : 1. valid religious doctrine, custom, law 10871; canon of religious doctrines etc. 109°; decision (of a relig- gious authority): pat ~ % oi 101%; <pat> ~ + Hušetar 96; pat hàn à Husetarmäh ~-éh 9814-15, — 2. an expert in religious matters, a theologian, a Dastur, also of the Zoroastrian clergy in general: a theo- logian 1018; x“atai u dahyupat u sardār u ~ + den 1081-2; pl. cas. obl.: ~-dn u dätavarän u hérpatàn u magupatān u den- burtärän 107'3-14, — MPrs dstwr ‘a priest’ (S); Paz. dastūr, Skr. v. ācārya, guru; NP dastür in profane senses (v. Steingass). — dast- from Av. (746) dqh- ‘to teach’, cf (745) dqstvà ‘religious doctrine’; hence MPrth dst ‘able, skilful? (A-H III). Cf Bailey, ZP 160, n. 5; TPhS 1945, 8.
dastavaréh 1. cas. obl. of dastavar (q. v.). — 2. abstr. the state of a Dastur 109%.
 dast-gir [dstgyl] assistance 66%, — NP dastgir ‘an assistant (now mostly ‘a prisoner’); -gir v. griftan.
dast-kārēh [YDH k’lyh] ‘“handiwork’’, making, of the
```


## [2026-09-05T18:27:15.057Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'dātan [YHBWN' in p or 'to give SPrs' in p or ('dātistān' in p) or ('dat-var' in p) or ('dātavar' in p):\n        print('LEAF',i,'printed',i-8, p[:80].replace('\\n',' '))\nEOF",
 "description": "Locate Nyberg datan entry"
}
```


### [2026-09-05T18:27:16.623Z] TOOL RESULT

```
LEAF 18 printed 10  anything to do with adarvär BdJ 3511, 5710 = adarvārak BdA p. 103°. 120? ‘lower
LEAF 71 printed 63 9725, 984, dat [dt'] wild animal 9725, 984, — Av. (678) daitika-; NP dad(ah). da
LEAF 78 printed 70  driyu- (in nom.); Paz. daryoš, Skr. v. durbala; NP darvēš, old daryoš, daryos. 
LEAF 82 printed 74 10018; and cand yašt-ē [-1] 651°; pat har 40 sal hac zan-ē u mart-é frazand-é [a
LEAF 83 printed 75 therwise ... 1181-15, as in Arab in halla wa'illa; hac Armail ~ except (by) Arma
LEAF 103 printed 95 ü ham. Hamadan [hmd’n'] 115%. — The NP form; the Milr forms are: 1. h’nmt’n = Hä
LEAF 248 printed 240 utuatā, *vivatà instr. adv. of *vi-vat- *'separation, dispersion’, derived from
```


## [2026-09-05T18:27:19.244Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==72' NYB_vol2_glossary.txt | head -70",
 "description": "Nyberg leaf 71 (p.63) dat/datan"
}
```


### [2026-09-05T18:27:20.936Z] TOOL RESULT

```
9725, 984,
dat [dt'] wild animal 9725, 984, — Av. (678) daitika-; NP dad(ah).
dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,
datistan
to deposit 922. 10912; — bē ~ to deposit 395.7:22. 402. 4910. 48?2. 4098-9.22-23, 5015, 9427; pat damīk bē ~ to lay (an enemy) in the dust 3329; to take off (clothes) 577; — (bé) 0 . . . — to transfer to . . . 88%. 953. 12016, — 2. to create 397. 577-8, 76 20.22 etc. passim. — to prepare 4216, with the gl. kū sāxt; — to bring about 451, v. ax"àyis- neh; — fräc ~ to put into existence by creation 932, 949. — Av. OP (711 sqq.) lda-; MPrth d?dn dh-; MPrs d'dn dy-, dyy-; Paz. dädan dah- (deh-, dih-); NP dadan dth-.
dātār [d^t?]] the Creator 5711; epithet of Ohurmazd, passim; creative principle 64°. dātārēh 1. the act of giving 704. — 2. the quality of being the Creator 71°.
datavar [d’twbl] judge P2: 2; pl. cas. obl. v-ān 10733, — < Olr. *dāta-bara-, v. dāt (1); KZŠPrth 1. 24 d*ibr; MPrth d?dbr; Ps. @twbl-; MPrs d’ywr; Talm. lw. dw’r, dwwr; Paz. NP davar.
ditavarčh l. judicial decision, judgment 7813. 7515-17, — 2. sg. cas. obl. of datavar: pat — kartan to make a p. one's judge, arbitrator 10314,
datéh [d’tyh] 1. the quality of being created, createdness, ''ereatureness'' 5513. — 2. cas. obl. of dāt (2) (q. v.).
dātihā [d'tyh?] righteously 631. 81?!. — MPrs d'dyh? (S).
datikéh [d’tykyh] the tenets of the third section of the Avesta called dätik ‘relat- ing to the Sacred Law’ 98". V. DkM 6771 sqq.; GrIrPh II, 20 sq., and cf gā- hānīk and hät-mänsr.
dätistän [d'tst'n'; DYN?] decision 451. 68 title. 818. 1054; judgment 7274; as opposed to passand (g. v.): a judgment which exceeds the formal prescriptions of the law, the utmost rigour of the law 70! [in other cases also: favour awarded above the formal prescriptions of the law]; ménóyé ~ the Heavenly Justice (personified) 7712; kar um (as a hendiadys) proper use 41%; lawful, righteous deeds
www .parsianjoman.org | ool sa,
datistan
7014; — affair, inatter 4°; condition, state 523-8.13, 964. — MPrs d’dyst’n; Paz. ddéstq, Skr. v. nyàya; NP dästän ‘a tale, story’. datistanéh [d’tst’nyh]. v. yuvat-~ and cf a-dätistäneh, -ihā.
datistanomandeh [~-’wmndyh] adjudie- ation 541°. — Paz. ddéstanmandi, Skr v. nyāyamattā (SGV XVI, 102).
davän [dwb?n'] pt. running 151%. — V. davistan.
davanik [dw?nyk] transliteration of the broken pl. dawānīg of Arab dānag, -iq,
```


## [2026-09-05T18:27:39.748Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('total leaves',len(pages))\nfor i in range(0,14):\n    print(i,'|',pages[i][:90].replace('\\n',' '))\nEOF",
 "description": "Nyberg first leaves"
}
```


### [2026-09-05T18:27:41.831Z] TOOL RESULT

```
total leaves 295
0 | www.parsianjoman.org IN n 
1 | A MANUAL OF PAHLAVI by HENRIK SAMUEL NYBERG II Ideograms, Glossary, Abbreviations, Index, 
2 | (C) Otto Harrassowitz, Wiesbaden 1974 Alle Rechte vorbehalten Photographische und photomec
3 | 2 HENRIK SAMUEL NYBERG A MANUAL OF PAHLAVI II www.parsianjoman.org |e Job P J 8 luga)
4 | ? www.parsianjoman.org sel
5 | l PREFACE The second volume of my Manual of Pahlavi appears at quite a long interval: ten 
6 |  [aola VIII Preface bibliographical references for every word. This is not a compilation o
7 | an.org | olw CONTENTS Prefače US OE A A O IRA CA teg pt RC ZU DEN VII IdčoSTaMN su a pow d
8 | man.org | Coll www.parsianjom
9 | an.org | oe wb IDEOGRAMS: The Aramaic ideograms used in this Manual are listed here, toget
10 |  1 No distinction is made in the alphabetical order between d (ae) and ‘ (‘ayn) Ideograms 
11 | DKY’: DAKYA pure "DMH 392? (my conjecture for MH): DAME similar DYN’: DINA lawsuit, judgem
12 | early KHDH: KA-HADA ‘as one’ = together KLB': KALBA dog KLSH: KARSEH his belly KLYT’: QELL
13 | efore (a p.) MDYN’: M'DINA town MH: MA what? MHL: M'HAR to-morrow MHSy> corrupt writing of
```


## [2026-09-05T18:27:51.253Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(14,24):\n    print(i,'|',pages[i][:110].replace('\\n',' '))\nEOF",
 "description": "Nyberg leaves 14-23"
}
```


### [2026-09-05T18:27:53.263Z] TOOL RESULT

```
14 |  Ps): *S'GA DEH, v. SGDH SGYTN-: SGY to go SHYDWNY: SIHIYÖN = Syr Sehyón Sion SKYN’: SAKKINA knife SLY, SLY’-:
15 | : artificially shortened form of YIHWE impf. 3d p. sg. of HWY to be YHW^ (Prs inser.): YIHW E imp. 3d p. sg. o
16 | ph. ZAK RA; later D'KAR, DIK
17 | RA ZLYTN-: ZRY to scatter, to distribute, later DRY (Arab darà) ZNH (inser., Ps.), ZNH (BP; also in the inser.
18 |  anything to do with adarvär BdJ 3511, 5710 = adarvārak BdA p. 103°. 120? ‘lower jaw’, also:the rendering of A
19 |  - Paz. aguma. V. gumän and ape-gumän. ah [^h] thus, then 3312. — Av. (62 sqq.) ada. ahanj- Phnc-] pres., to d
20 | t- cf ayinaftan, hanžaftan. Cf also Gxrdm-. ahramög [hlmwk'] heretic, apostate 1074, — Borrowed from Av. (257)
21 | nah ‘Friday’, for Islamic (yaumu-)l-jum'a, cannot be etymologically connected with ātvēnak, as Markwart has it
22 | antly written in Prs. in- scriptions and in the Ps.; this is wanting in Prth (quite exeptionally written in si
23 | m 39°; with enel. copula 2nd p. pl. —-& 58’; subj. of an intrans. pret.: raft hénd ~ 5812; — -b) eas. obl. —-à
```


## [2026-09-05T18:28:12.220Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nfor k,v in d.items():\n    if k!='cites': print('==',k,':',str(v)[:1500])\n\"",
 "description": "BQT ref details"
}
```


### [2026-09-05T18:28:14.179Z] TOOL RESULT

```
== title : Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
== kind : archive_djvu+local_scan_ocr
== url : https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
== lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
== page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
== covers_etymology : True
== notes : Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \f; leaf N = N-th \f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pag
== scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
```


## [2026-09-05T18:28:21.039Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor leaf in [264,271,275,278,319]:\n    print('======== leaf',leaf,'~ printed',leaf+543)\n    print(pages[leaf][:1500])\nEOF",
 "description": "BQT vol2 candidate leaves"
}
```


### [2026-09-05T18:28:22.776Z] TOOL RESULT

```
leaves 684
======== leaf 264 ~ printed 807
                                                                                                                            ‫خیشفوج‬
 ‫==‬




‫میگویند نه مطلق خوی را؛ وبسضی کویندبمعنی‬                                                ‫بی‌نقطه آءرده است (‪ )۱‬اه اعلم ‪.‬‬
‫اول عربیادت ‪ -‬وحوالی باشد کهآنرا ازرسمان‬
                                                              ‫حیشفو ج ‪١‬‏ بفتح اول و سکون ثانی‬
‫پنبه بافته باشند ‪ -‬و رندش زوده و شکنبه را‬                     ‫وفتح ثالث وفای بواورسده و ‪,‬جم زده ‪,‬دنبددانه‬
‫روده‬       ‫و‬   ‫از شکنده‬    ‫انجه‬   ‫ەی‬
                                                                 ‫راگویند وبعربی حب‌القطن‌خوانند‪ .‬سینه وسرفه‬
     ‫۔‬
     ‫سشمدبهم‬
           ‫ری‌چ‬
              ‫بتراشند ‪-‬وفی وچر کیکه‌در گوشها‬                                                                    ‫را ناف ات ‪8.‬‬
‫ولعابی که آزدهان وبینی مردم براید ‪ -‬و بمعنی‬
                                                                 ‫بر وزن فیل ‪۰‬‬             ‫(ل‪)۲‬‬
                                                                                             ‫حیل ‪ -‬بکر او‬
                                                              ‫اماب علدظی را بند که ازبینی‌مردم‌برمیآید ‪۴‬۔‬
‫را‬    ‫دبوانه ومحنون‬        ‫هم آمده است ك‬           ‫جراحت‬


‫و بفتح اول درعربی بمعنی خیمه‬                ‫نیز گوبند ‪-‬‬        ‫و بفتح اول در عربی بمعتی جماعت و طایفه‬
                                                 ‫باشد ‪. ¥‬‬                           
======== leaf 271 ~ printed 814
 ‫دار شش‌دو‬                                                                                      ‫سس‬   ‫‪۱۱‬‬


‫دارخال = با خای نقطه دار بر وزن‬                       ‫دار با‪ » ۱‬بابای ابجد بالف کشیده ‪۲‬‬
‫پارسال ‪ ,‬درختی که آنرا پوند نکرده باشند ‪-‬‬                       ‫مابحتاج وضروری ودرباست راگویند ‪.‬‬
‫وشاخ‌درختان(‪ )۳‬توشانده رائیز گویند ‪ - ۷‬وهر‬            ‫دار بار ‪ - ۲‬بروزنکارساز ‪,‬شخصی را‬
‫بونه ودرختی بود که از جابی بر کنده باشند(‪)4‬‬
                                                      ‫کوبند که چوب بلندیرا در زمين محکم سازد‬
                       ‫ودرجای دیگربنشانند ‪.‬‬               ‫وبر اطراف آن ریسمانها بندد ویربالایآن چوب‬
‫داردار کردن ‪ ۰ ۲‬کنابه از در‬                                          ‫رود وبازبپای عجیب وغریب کند ‪.‬‬
‫پاییدن وثبات داشتن ‪ -‬ومدارا کردن ‪ -‬و بيار‬             ‫دار بام ‪ = ۳‬بروزن شادکام " شاه تیررا‬
                            ‫ماندن باشد (‪)e‬‏ ‪.‬‬         ‫کویند » وان چوب برزکی باشد که بدان بام‬
                                                                                            ‫خاله بوشند ‪.‬‬
‫دار دان‪ .‬وبزرن‌اردان» بمعنی‌تخمدان‬
‫برآن‬   ‫باشد» وآن زمینی‌است که شاخهای درخت‬
                                                      ‫دار بر = بضم بای ابجد و سکون رای‬
‫فبرروند تاسبز شاوزدآونجا بجای دیگر هل‬                 ‫قرشت(‪ » )۱‬نام مرغیست سبزرنگ که درختانرا‬
                                                      ‫ممنقار سوراخ کند * و آن را بشیرازی دار نمك‬
                                            
======== leaf 275 ~ printed 818
 ‫داغ سو‬                                                                                                            ‫س‬
                                                                                                                   ‫ری ‪۱‬‬
                                                                                                                      ‫تس‬


 ‫داشن ‪ = ۲‬بروزن دامن؛ عطا وبخشش‬                             ‫خوشه است ‪٩‬‏ ‪-‬وداسی را گیوزیند که غله‬
‫وانعام باشد ‪ -‬واجر ومکافات لیکیرا هم گوبند‬                                                    ‫‪۰‬‬   ‫کنند ‪۳‬‬           ‫بدان درو‬


 ‫ودر زند (‪)۱‬مرقوم است که داشن نقد وجنیرا‬                   ‫داش س بر وزن فاش » کوره ایکه‬
                                                                                ‫‪۰‬‬                          ‫=‬



‫گوبند که پارسیان‌درعید وجشنهابرسم نذرباصدقه‬                   ‫وخموکاسه و کوژه وامثال ‏ ن‌دران‌بیز ند‪۰ ۴‬‬                ‫حشت‬

                   ‫بففرا ومسا کین بدهند ‪. ۸‬‬                                         ‫وهمعني کاستان همکفته‌اند ‪۰‬‬

‫داع ‪ = ۹‬بروزن باغ» ممروف‌است *‪-۱‬‬                              ‫داشاب = بروزن داراب » بمعنی داد‬
‫وبمعنی‌شان همآمده است ومعنیی (‪ )۲‬که شاعر‬                                    ‫ودهش وچیزی بمردم دادن باشد ‪.‬‬
                                       ‫چ‬
‫ند جا ببندد ‪ -‬ونام شاعرکه درغزل و فصده‬                        ‫داشاك « بروزن آزاد » بمعنی شاط ‪-‬‬
                                           ‫مذ کور شود‬
  
======== leaf 278 ~ printed 821
  ‫بح‬        ‫یز‬

 ‫سله وسبدی باشد بز رکه که دوچوب بدروطرف‬                        ‫دامن بارفشاندن ک»نابه از سفر‬
    ‫ومد لد وبدان سر کنو وامثار آن کشند ‪.‬‬
                                         ‫ن‬               ‫آ‬     ‫کردن و کرچ لمودن ‪ -‬وترك دادن ‪ -‬و اعراض‬
 ‫داموع = بروزن آروغ » فرباد وفغان‬                                                                      ‫کردن باشد ‪.‬‬
                          ‫ولاله وزاری باشد ‪.‬‬                   ‫دام خشك ک‪-‬نابه از دامن خالی‬
‫‪ ۰‬صیاد را‬        ‫‪٣۷‬‏ وزن جامی‬       ‫دامی ا‬                           ‫باشد ‪ -‬وعدم صلاح‌وتقوی را گیوزبند ‪.‬‬
                                                       ‫ق‬        ‫داهن جوز شید » کنابه از آسمان‬
‫دامیار" ‪ -‬بروزنکامکار‪.‬دامی‌استکه‬                                              ‫چهارم ‪٣‬‏ وروشنی خورشید باشد ‪.‬‬
                                               ‫صاد باشد‬
                                                               ‫دامن دبرای افتادن ‪ -‬کنابه از‬
‫دامیدن = بروزن بالیدن (‪ » )۱‬بر بالا‬                            ‫اضطراب باشد ‪ -‬وازروی اضطراب بگخرتن رانیز‬
‫و بن‬    ‫و از بیخ‬          ‫وبرابر چیزی شدن ‪-‬‬          ‫رفتن ‪-‬‬                                     ‫گوبند ‪.‬‬
‫برکندن ‪ -‬وتخم افتاندن ‪ -‬وبردن مادخا کرا ‌‬
                                                               ‫کرشیدن در دامن کشیدن»‬
                                                                                   ‫دامی د‬
‫ذاهیده ‪ - ۴‬بروزن نا دیده ‪,‬بربالای‬                
======== leaf 319 ~ printed 862
                                                                                                    ‫<‬
                                                                                                    ‫‪.‬ی‬


                            ‫نکیوزبند ‪.‬‬             ‫ومند حکومتی رالیزکوبند کهبرسر‬                    ‫باشد ‪-‬‬

 ‫دستره ^ = بر وزن مسخره ‪ ۰‬بمعنی‬                    ‫ان قنل و کشتن واقع شود ؛ وبسکون ثالث بر‬
 ‫دسترباشد که دای کوچك دندانه دار است واصل‬                                          ‫وزن لمل کون هم هت ‪.‬‬
                      ‫آن دست اره بو‪:‬ه است ‪.‬‬        ‫دست دادن ‪ ۰‬کنابه‌ازحاصل‌شدن ‪۱‬۔‬
 ‫دست رن ‪ -‬با زای هوز (‪ )۱‬بر وزن‬                     ‫وبمل آمدن ‪ -‬وبیعت کردن ‪ -‬وآرام گردیدن‪.‬‬
 ‫کفش کن ‪.‬کنابه ازمردم ادم ویشیمان باشه =‬                                             ‫ومضبوط کشتن باشد ‪۰‬‬
‫و صاحب طرب و سرودگوی و خوشحال را لیز‬                ‫دست دآرستیی داشتی ‪ -‬کاه‬
 ‫کویند و کی رانز گفته‌اند کهدست مرچیزی‬                                         ‫از فارغ بودن ازکارهاست ‪.‬‬
                      ‫زد ومترسل بکی شود ‪.‬‬          ‫دست در آستین کردن = کنامه‬
  ‫دست سنگ‪ .‬باسین بی لقطه بورزن‬                                ‫‪.‬‬   ‫ازری‬
                                                                     ‫از باز داشتن ومنم کردن نود ا‬
‫هت رنگ ‪ .‬بمعنی دستاسنگك است که فلاخن‬
                                          ‫باشد ‪.‬‬
                                                   ‫دست دکرسه ردن د کنابه از‬
 ‫دست سو زه = بروزن هفت
```


## [2026-09-05T18:28:38.192Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in [279,280,281,282]:\n    print('======== leaf',leaf)\n    print(pages[leaf][:2200])\nEOF",
 "description": "BQT v2 leaves 279-282"
}
```


### [2026-09-05T18:28:39.817Z] TOOL RESULT

```
======== leaf 279
 ‫داشور‬

‫دا نژه گ بازای فارسی» بروزن وهعتی‬                           ‫و واو وضم رای قرشت (‪ )۱‬و سکون جيم اول‬
                 ‫دالجه است که عدی اند ‪.#‬‬                    ‫وبای ابجد (‪ )۲‬وجیم آخرء حبی است که آنرا‬

‫داش ® ‪ -‬بروزن بال » بىمنىعلم‬                                ‫که از‬              ‫وبه‬
                                                                                 ‫بشیرازی انجکك خوانند وکازبکلوه‬
                                                                                           ‫ولات فاری است آورند ‪.‬‬
                 ‫وفطل ودااستن چزی باشد ‪.‬‬

‫د بکر بای فارسی‬         ‫دانش پژوه‬                            ‫بفتح‌ثالك وواو وبای‬                  ‫دانج و بر ‪1‬‬
‫وزای فارسی بواو کشیده و بها زده » بمعئی علم‬
                                                             ‫ابجد ‪ .‬دانۂ ویراست که حبالرای باشد ‪٠‬‏ وآن‬
 ‫وفضل جوینده وطالب علم‌باشد چه پژوه جوننده‬                  ‫تخمی است زردرنگه وطعم آن نلخ میباشد و از‬
                        ‫وتفحص کننده رکاوبند‪.‬‬                                    ‫وردستان مبآورند ‪.‬‬
                                                                                                ‫کوهتان فاری ک‬

‫دانشگر ‪- ۲‬باکان‌فارسی روزن‌داشور‪,‬‬                            ‫دا نحه ‪ = ۲‬بسکون ثالث و فتح جيم ‪,‬‬

 ‫داشمند و دانا و بیار دان و عالم و فاضل‬                                               ‫غله‌است که بعربی عدس کوند ‪.‬‬
                                             ‫باشد ‪. ¥‬‬        ‫انك ‪ » ۴‬بفتح‌ثاكك وسکون‌دال ابجد‪.‬‬
 ‫دانشور ‪ = 4‬با واو بورزن داشگر»‬                                   ‫‪۱‬‬                    ‫بمعنی تواند باشد ‪.‬‬
                                                   ‫وبا ‪۰‬‬   ‫)‪ (۱‬چك‪:‬‬                    ‫(‪ )۱‬چك ‪ :‬وضم را ‪.‬‬

 ‫دالره (ھ م‪ ۰ ( ۰‬دانجه دز فارسی‬      ‫‪-‬‬        ‫‪۴‬‬              ‫‪۰‬‬       ‫ودر‬   ‫‪:‬‬    ‫رك‬   ‫دالهٌوبر ‪.‬‬    ‫معرب‬         ‫‪۱‬‬


  ‫مضارع‬   ‫) مفردمغاب)‬   ‫شخص‬    ‫سوم‬   ‫‪- ۳‬‬                         ‫› ‪.‬‬       ‫بمعتی ‪( 61111061‬فر) است « لصك‪۹۷‬‬
  ‫‪ ۴‬ر=انجه (ه‪.‬م ) از ‪ :‬دان(دانه) ‪-۲‬ژه (یوند صفیر) رکه‪ :‬دانك ‪.‬‬                                 ‫آزمصدر دانتن(هم ) ‪.‬‬
                        ‫
======== leaf 280
 ‫=‬    ‫=“‬
                                                                                               ‫داشومد‬

‫بف هد تا ازآن سرانجام خوردلی‬    ‫روفف هرىكڭزرى‬       ‫وخداو ند ودارندة داش باشد»چه ورىمەنى‬              ‫صاحب‬

‫ومایحتاج آن نر كنف ‪ -۳۴‬و فتح تااث اساب‬                                ‫ام‬     ‫و خداو ند ودارنده‬        ‫صاحب‬



                                                     ‫دا نشوهنك ‪ ۱‬ب‪-‬فتح‌ميم وسکون نون‬
                          ‫باد ©‬     ‫و متاع و کل‬


                                                     ‫و دال ایسد » بمعتی دانشمتد وحکیم وسباردان‬
                                                                                                  ‫‪۰‬‬   ‫باشف‬




                                                     ‫دانشی ‪ -‬بکرثالث ورایع وسکون‬
                                    ‫وامثال آن ‪.‬‬
                               ‫‏‪٩‬‬
                                                     ‫وانا‬
                                                        ‫تحتانی " بمعنی دانشگر امت که داشمند ر‬
‫د بفتح نالك وسکون‌ميم‪ .‬نمعدی‬        ‫دانم‬                                                          ‫باشد ‪.‬‬
                                    ‫توانم باشد ‪.‬‬
                                                    ‫دانك؟ = بفتح نالك و سکون كاف ‪٠‬‏‬
‫بروزنآغوش‪.‬نام‌شضصی است‬         ‫دناوش‬                 ‫گمنادزم و جو و ماش‬‫ناد اع‬  ‫به ر‬
                                                                                  ‫ودان‬
                                                                                     ‫گلق‬
                                                                                       ‫مط‬
‫ازبود معشوقة‬              ‫که عذرا را بفروخت‬         ‫ودص و غیره ‪ -‬وبضم الث آن باشد که بوقت‬
                                                                                        ‫ع‬
‫وامق ‪ ۰‬وفصهه ابغان مشپور است ؛ وآنرا دوانوش‬         ‫دندان نزآوزدن اطفال اقام دانها از جنس کندم‬
‫هم میگوبند که حرف انی واو باشد بر وزن‬               ‫وجو وماش وعدس وامثال آنها را باکله و پاچ‬
‫قدایوش ؛ ودلواش نیز گفته‌اند که حرف انی نون‬         ‫گوسفندپز دوبخانهای دوستانو خوبشانومصاحدان‬
‫باشد پروزن اوباش؛ و دیانوش نبینزظرآهده است‬  
======== leaf 281
  ‫داوردان‬                                                                                                    ‫==‬


 ‫قمار نیز هت » وآن ازهفده زیاده تمیباشد چه‬                                                              ‫‪.‬‬   ‫مت‬
                                                                                                             ‫ه‬ ‫نمودن ه‬
 ‫ازدیادآن جز طاق یت ومراتب اعداد متحصر‬                      ‫ب‪-‬روزن خاندان » ظرفی‬                    ‫دانه دان‬
 ‫است تا به نه ‪,‬پدساواول یکی است ودوم سه‬                 ‫وجایی باشد کهغله وداله درآنکنند ‪ -‬وبمعنی ‏‬
‫وسيم پنج وهمچنین هفت ونه وبازده تا هفده که‬
‫که مرنبة نهم اعداداست مپرود تائمام میشود‪- ۴‬‬                 ‫رالیز گوبند که درآ ن‌تخمکاشته ماف وزهتتی‬
 ‫ودعوی‌کازبرانیز گفته‌اند؟ ‪ -‬وبمعنی‌فحش ودشنام‬              ‫درخت فرو برند تا سیر شود‬                ‫که درآن شاخہای‬


‫هم‌آمده است ‪ -‬وهرچینه و(‪)۱‬مرتبه ورده باشد‬                                  ‫وازآنجا بجای دیگر نقل نمابند ‪.‬‬
‫که از دبوا رکلی بربالای حمگذارند وآرا دای‬                   ‫با زای هوز بروزن‌آمدن‪.‬‬                  ‫دانه دن ‏‬
                                    ‫گهومبند ‪.‬‬               ‫نوعی ازساحران وجادو گران باشند درهندوستان‬
 ‫‪ -‬بر وزن خاور ‪ ,‬نام خدای‬          ‫داور‬                     ‫که دانة ارزن وجورایز عفران زرد کتند وافسونی‬
‫عزوجل است ‪ -‬و یادشاه عادل وپرمتش کنندمرا‬
‫نیز گونند(‪ )۲‬ودراصل دادور بروزن داد گربوده ‪۰‬‬                    ‫‪۱‬‬                                  ‫که دار ند بواریق ‪۳‬‬


‫اد انشراز عنمی وت وا‬              ‫تورود ام خف‬
                      ‫ودرمان هم بنظر آ مده ات‬                          ‫‪۳‬‬   ‫وکالا ومتاع‌دنوی‌باشد؟‬               ‫دانه‪.‬اسباب‬



 ‫داو ردان = بادالابجد بروزن‌دافرمان‪,‬‬                        ‫‪ ۵4‬کردن ‪ -‬کنابه از پراکنده‬
 ‫نام دهی است که در طرف غربی و بفكرسخی‬
 ‫تکیبیآن خدادان‬
              ‫‪-‬معنی ر‬
                    ‫واسط واقع است‪ ۷‬و‬                        ‫داو » بر وزن‌گاو ‪ .‬بمعنی نوبت بازی‬
                     ‫وحا کمشنای باشد ‪.‬‬                       ‫وباده کردن خصل‬ ‫شطراج ونرد وغیره باشد ‪ -‬ز‬

 ‫(‪ )۷‬چك‪ .‬چش‪ + :‬معنی شخصی که مبان ليك وبد‬                                   ‫هر ‪.‬‬      ‫‪1‬‬         ‫‪۱‬‬
  
======== leaf 282
    ‫ح‬
    ‫ر‪۷‬‬                                                                                                                     ‫دأوری‬


‫يدام لصب کنند تاجانوران‬         ‫صادان درصحراتزدىك‬         ‫داور ی‪ = ۱‬بر وزن لاغری » جنگه‬
                  ‫دام آ بند ‪5‬‬   ‫رم کرده بجالب‬   ‫ازآن‬           ‫یت‬
                                                                ‫اغصه‬
                                                                   ‫کو‬‫شظلم‬
                                                                        ‫ونی ت‬
                                                                            ‫وخصومت باشد ‪ -‬و به‌ع‬
‫داهم ‪ < ۱‬بروزن‌کاظطم تاج پادشاهانرا‬                       ‫پیش کسی بردن‪ -‬ومحا کمه نمودن ویک وکردن‬
                                                                        ‫ميان نك وید همآمده اسن‬
‫گوبند وآلرا دبهیم نزخوانند ‪ -‬و تخت شاهی‬
                      ‫وجتر بادشاهی راهم گفته‌اند ‪2‬‬        ‫داو ناف ‪ ۳‬کهنابه ازناشتن نقشی‬
‫بمعنی‌داهل‬   ‫بروزن افول ‏‬         ‫‪۰‬‬   ‫داهول‬                                                                     ‫بمراد باشد ‪.‬‬
‫ات ‪. ۷‬وان علامتی باشد کهدهقانان بجهت‌دفع‬                  ‫‪۳‬‬    ‫کنر ك ویرستارباشد‬              ‫بروزن‌ماه‪.‬‬       ‫‪-‬‬         ‫داه‬

‫جانورانز بانکردرمیان زراعت نصب کنند وصیادان‬               ‫رایز‬    ‫ده‬   ‫وعشد‬       ‫وناکس را همگفته‌اند ‪-‬‬                     ‫مددل‬   ‫و‬


‫کبنرار دام‌سازند ‪ -‬و بمعنی تاج ءرصم هم‌بنظ‬                                   ‫ند که بعربی عشره خوانند ‪. ۴‬‬
                                       ‫آهده است ‪. ۸‬‬
                                                          ‫داها ‪ .‬بروژن باها ء یمعنی دره و عار‬

                                                                                                                     ‫کوه باشد ‪.‬‬
‫وميم » بمعنی دیهیم است که تاج مرصع باشد ‪.‬‬
                                                             ‫داهل ‪ - °‬نم ثالك بر وزن ک کل ‪.‬‬
 ‫دای ‪ -‬بروزن‌لای‪.‬هرچینه‌ورده‌ومرتبه‌را‬
                       ‫‪3‬‬    ‫از دبوارکلی ‪۰‬‬       ‫کون‬
                                                             ‫آزن برمند‬
```


## [2026-09-05T18:28:51.249Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in [267,274,278,322]:\n    print('======== leaf',leaf,'-> printed',leaf+540)\n    print(pages[leaf][:2600])\nEOF",
 "description": "BQT v2 leaves 267,274,278,322"
}
```


### [2026-09-05T18:28:53.010Z] TOOL RESULT

```
======== leaf 267 -> printed 807
 ‫داد‬

‫داخم د بكر اك بروزن قاسم »‬                          ‫فرشت (‪ )۱‬ولام‌بتحتانی کشیده ویمیم زده » طایفه‬

                     ‫یمعنی رزق وروزی باشد ‪.‬‬         ‫وقومی اند که پادشاهی سومنات بدیشان مخصوص‬
                                                                                                 ‫است ‪١‬‏ ‪.‬‬
‫خاول ‏ باواومجهول بروزن شاغول‪.‬‬     ‫د‬
‫اهان باشن‬    ‫بمعتی داخل است ‪ ۷‬کبهاددر گشاه‬          ‫‪ -‬بادونو تایفرشت بر‬               ‫دنابتون‬
‫ودکه و سکوبرا نز گویند که بر درگاه اکار‬             ‫وزن بازو شکن » بلغت زند و پازند (‪ )۲‬بمعنی‬
‫وسلاطین بجهت شتن سازند ‪ -‬وعلامتی را فز‬                           ‫دادن باشد کهنقیض کرفتن است ‪.‬‬
 ‫گفته اندکه صیادان در صحرا نزديك یدام صب‬             ‫داتو بر ‪ ۴‬ب‪۰‬ا تای قرشت بوای‬
  ‫همی‬‫رابادا‬‫کنند تاصید از بآتنرسد و بج‬               ‫ابجد بر وزن جادو کر ‪ ۰‬بمعتی داور و دادری‬
‫شود‪ -‬وعیلیازمتی‌باشد که براطراف زراعت سازند‬                                                       ‫ماش ‪.‬‬
                  ‫بجهت منم وحوش وطیور ‪.‬‬
                                                    ‫كرجوز=ن‌تاج » شبتارك وتاریکی‬
                                                                               ‫ب‬
‫داحیدن = بروزن باشیدن » بممنی‌از‬
                                                    ‫گبورباند ‪ - ۴‬و بانشدید جیم درعربی مکاری‬   ‫ش‬
‫هم جدا کردن ‪ -‬ونظربرچیزی افکندن ودبدمور‬                                      ‫وتجار را خوانشد © ‪.‬‬
                                   ‫شدن باشد ‪.‬‬
                                                    ‫داچك(‪ -)۳‬بفتح جیم فارسی بر وزن‬
‫كاك = بروزن باد‪ .‬بمعنی عمروسن وسال‬                                  ‫گوشواره را گونند ‪۰‬‬       ‫»‬   ‫ناوك (ع)‬


‫آدمی باشد ‪ -‬ونام جوششی است با خارش یار‬              ‫‪۵‬احتن = بروزن‌ساختن؛ بمعنی داستن‬
‫که‌آنرا بعریی قوباکویند وبهندی یزاین علت‬                                                           ‫باشد ‪.‬‬
  ‫مهدمه‬
      ‫آان‬
        ‫‪-‬نی فریاد و فت‬
                     ‫بندمع‬
                         ‫را داد خووان‬
‫است ‪ -‬ویمعنی راستی و عدل وعدالت و اعدال‬             ‫داخل؟ ‪ -‬بثناملك بر وزن کاکل‪,‬‬
 ‫باشدھ ‪ -‬وتظلم‌ووارسیدن‪٩‬‏ وبهرمرا نکیزفتها‬                                 ‫در گاه یادشاهانر | گوبند ‪1‬‬




            ‫(‪ )۳‬خم ‪ :۱‬داچذ‪.‬‬          ‫(‪ )۲‬چك‪ :‬ژند ویاژند ‪.‬‬               ‫(‪ )۱‬چك‪ :‬قرشت ‪.‬‬
                                                               ‫بروزن ناوك ‪۰‬‬   ‫‪۳‬‬   ‫)‪ (£‬چش‪:‬‬



  ‫ائثل‬   ‫‏‪ =١‬دیشليم » نام بادشاهی ات که درکمله ودمنهٌاین المتفع ( چاپ محمد حن‬

                                                              ‫المرصفی ‪ ۷۲۹۱‬م
======== leaf 274 -> printed 814
      ‫ا‪6‬س‬

               ‫داستخاله است که مذ کور شد ‪.‬‬              ‫است مانند دای ودسته دزازی هم دارد و حرية "‬
                                                         ‫و استخوان ماهی را لیز‬           ‫‪۱‬‬       ‫مردم کیلان ات‬
‫دستحاله ‪ = ۷‬بخاای نقطه‌دار بروزن‬
                               ‫ا‬
‫پارساله » بمعنی داستکاله است که دای کوچك‬                                                                   ‫کوبند ‪.‬‬
 ‫باغبادان باشد ‪ -‬وعصای سر کج را نکیفزته‌اند‪.‬‬
                                                          ‫داساد ؟ ب‏روزن پاکر‪ ,‬دلال راکوند‬
‫داس ر رین د کنابه از ماه نو ات‬                                               ‫وحریی سمسار خوانند ‪.‬‬
                             ‫وبعربی هلال گوبند ‪.‬‬          ‫داستاره بانای فرشت بر وزن نادار‬
                   ‫داسفاله ‪ ۷‬د باغن‬                       ‫یمعئی دامار است که دلال وسمار باشد وبعربی‬
                   ‫نقطه‌دار» بروزن ومعنی داسخاله‬

                  ‫است که دای کوچك و عسای‬                  ‫داستان؟ س بروزن پاسبان » شهرت ‪-‬‬
‫داسفاله (داسکاله)‬             ‫سر کج باشد‪.‬‬                ‫و مثل باشد ‪ - ۴‬و حکات و افانه را لز‬
                                                                                                       ‫کونند ® ‪.‬‬
‫داسگاله ‪ ۲‬ه با کاف‪ .‬بروزن ومعنی‬
                           ‫وفته شد ‪.‬‬
                                   ‫داسفاله است گ‬
                                                          ‫داستخاله ‪ - ۱‬باخای قطه دار بالف‬
                                                                                     ‫کشیده و فتح‬
                                                         ‫لام ؛ دای کوچکی باشد که بدان‬
‫‪ -‬نات و قتح‌دال‬             ‫وس‬
                             ‫داس ود‬                                                                           ‫سمزی‬
                                                         ‫امثال[ ترا‬   ‫تاك و‬   ‫وتره درو کنند و درخت‬
‫وسن بینقطه (‪ )۱‬زده »‬
                   ‫ابجد ولام بواو رسیده ب‬
                                                                                  ‫بزدان به‌ییرانند ۔‬
                                                         ‫عصای سر کج رالیز کفته‌اند‪.‬‬                ‫ل‬
 ‫این‌کلمه ازانباع است‌همچونتار ومار وترت ومرت؛‬
‫بمعنی ضایم وایتر ودورافکندلی باشد مانند خار‬                           ‫وبمعنی ممتوقه همبنظرآمده است ‪.‬‬
‫وخس وخاش وخماش وامثال آن ‪ -‬وبمعنی سفیه‬                    ‫داستغاله ‪ . ۲‬با غین قطه دار‪,‬بروزن‬
                                                                                                ‫و‬
                       ‫‪.‬‬    ‫‪ -‬وس
======== leaf 278 -> printed 818
  ‫بح‬        ‫یز‬

 ‫سله وسبدی باشد بز رکه که دوچوب بدروطرف‬                        ‫دامن بارفشاندن ک»نابه از سفر‬
    ‫ومد لد وبدان سر کنو وامثار آن کشند ‪.‬‬
                                         ‫ن‬               ‫آ‬     ‫کردن و کرچ لمودن ‪ -‬وترك دادن ‪ -‬و اعراض‬
 ‫داموع = بروزن آروغ » فرباد وفغان‬                                                                      ‫کردن باشد ‪.‬‬
                          ‫ولاله وزاری باشد ‪.‬‬                   ‫دام خشك ک‪-‬نابه از دامن خالی‬
‫‪ ۰‬صیاد را‬        ‫‪٣۷‬‏ وزن جامی‬       ‫دامی ا‬                           ‫باشد ‪ -‬وعدم صلاح‌وتقوی را گیوزبند ‪.‬‬
                                                       ‫ق‬        ‫داهن جوز شید » کنابه از آسمان‬
‫دامیار" ‪ -‬بروزنکامکار‪.‬دامی‌استکه‬                                              ‫چهارم ‪٣‬‏ وروشنی خورشید باشد ‪.‬‬
                                               ‫صاد باشد‬
                                                               ‫دامن دبرای افتادن ‪ -‬کنابه از‬
‫دامیدن = بروزن بالیدن (‪ » )۱‬بر بالا‬                            ‫اضطراب باشد ‪ -‬وازروی اضطراب بگخرتن رانیز‬
‫و بن‬    ‫و از بیخ‬          ‫وبرابر چیزی شدن ‪-‬‬          ‫رفتن ‪-‬‬                                     ‫گوبند ‪.‬‬
‫برکندن ‪ -‬وتخم افتاندن ‪ -‬وبردن مادخا کرا ‌‬
                                                               ‫کرشیدن در دامن کشیدن»‬
                                                                                   ‫دامی د‬
‫ذاهیده ‪ - ۴‬بروزن نا دیده ‪,‬بربالای‬                               ‫کنابه ازاعراض واجتناب نه‌ودن باشد ازچیزی ‪-‬‬
‫وافشانده‬     ‫واز بخ وین بر کنده ت‬          ‫‪-‬‬   ‫شده‬    ‫چری‬                                      ‫وترك صحبت کردن ‪.‬‬
                                               ‫شده باشد ‪.‬‬
                                                               ‫امزت ‪۳‬‬     ‫داهن گیر ‏ کنابه از مصاحب‬

‫بر وزن‌نان ‪ ۰‬مطلق‌دانه را گوشد‬         ‫دان ت‬                   ‫کونابه ازمدعی_ وباعث سکون‪ -‬ومانم‌شدن هم‬
                                                                                                ‫هت ‪.‬‬
‫‪,‬يهى بدان ‪ - ۱‬وچون درآخ رکلمه آبد معنی‬                         ‫داهنی = بروزن‌دادنی » سراندازومقنمة‬
‫طرفت بخشد‪ ۷‬ھمجوقلمدان و کبفدان‌رقهوه‌دان‬
                                                                                                 ‫‪. ۱‬‬      ‫گنوراند‬
                                                                                                                ‫زا‬
                                       ‫‪3‬‬       ‫ومانشد آن‬
                                                               ‫داهو ‪ 
======== leaf 322 -> printed 862
 ‫‪“A‬‬                                                                                                              ‫مو ره‬        ‫وت‬


                                 ‫نمودن را نگیوزبند ‪.‬‬                    ‫کسهی‌کاری کرده باشد‪ -‬رمکافات‌نیکی وبدیرا‬
‫باراو بررزن دمتیار »‬              ‫دستو ار ‪٩‬‏‬                                                                         ‫فیز گویند ‪.‬‬
                                                                        ‫مور ه = بورزن هفقت روزه ؛‬                    ‫ست‬
                                                                                                                      ‫ك‬
‫برتجن را از کفته اند‬         ‫وت‬
                              ‫الت تا و‬               ‫هم آ وت‬
                                                                             ‫یممنی تحفه وارمفان ‪ -‬ودست آوبز باشد ‪.‬‬
               ‫ز نان باشد‪ .‬وچوب دستی‬             ‫که وه‬
                                                                        ‫دست موسی س کناه از آقاب‬
‫وسطیر‬   ‫کنده‬




 ‫که شبانان بدست گیرند‪ -‬وهرچیز پارهکه بقدمار‬                                                                  ‫عالمتاب ات ‪٩‬‏‬
                                                                        ‫دستنمو ی ؟ «کاوله‌ای باشدکهآنرا‬
                                            ‫‪۳‬‬   ‫باشد‬      ‫دسی‬

‫دستو ار و ‪ = ۷‬بروزن نعل (‪ )۱‬باره »‬
                                                                        ‫از اقام عطربات سازند و پوسته دردست کیرند‬
‫واره بمعتی مانند‬    ‫باشد جه‬        ‫مانند‬        ‫دست‬      ‫نمهدی‬
                                                                   ‫وبوی کنن وآنچه از لخلخه وخوشبوی که نرا‬
         ‫است ‪ -‬وهرچیز که بمقدار دستی باشد‬
                                                                        ‫بدست توان کرفت وبعربی شمامه کوبند ‪ -‬و هر‬
                         ‫دستو انه ‪۸‬‬
                                                                    ‫مبوه‌ای که بجهت بوییدن بردست گیر ندعموماه‬
 ‫مجاس ومند باشد‪ -‬ودستینه زنان ‪ -‬وساعد نند‬                           ‫ووجك والوان شبیه بخربزه‬
                                                                                          ‫وبانی باشد کرد ک‬
‫آهنن مدران را بز گفته اند که در روز جنکه‬                                                                                    ‫جوا‬
‫دردست کنند وآنرابعر بیقفازباقاف وزای‌تنقطه‌رار‬
‫بروزن حفاظ خوانند و بتر کی قولحاق گونند ‪.‬‬                               ‫دستذرو یه‪ - ۴‬بتتح تحانی ‪ ۰‬بسنی‬
                                                                    ‫که‬       ‫وهره‌موه‬
```


## [2026-09-05T18:29:20.803Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor leaf in range(266,284):\n    txt=pages[leaf]\n    head=txt.strip().split('\\n')[0][:60]\n    # find persian-digit sequences\n    print(leaf, leaf+540, '|', head)\nEOF",
 "description": "BQT v2 running heads 266-283"
}
```


### [2026-09-05T18:29:22.421Z] TOOL RESULT

```
266 806 | ‫گفتار هم‬
267 807 | ‫داد‬
268 808 | ‫یارس‬    ‫¬‪۸‬‬                                            
269 809 | ‫=‬         ‫‪06‬‬
270 810 | ‫وت‬                                                        
271 811 | ‫دار شش‌دو‬                                                 
272 812 | ‫داز شمان‬
273 813 | ‫دای‬                                                       
274 814 | ‫ا‪6‬س‬
275 815 | ‫داغ سو‬                                                    
276 816 | ‫”‪“AI‬‬                                                    
277 817 | ‫دامن بدندا نکرفتن‬                                         
278 818 | ‫بح‬        ‫یز‬
279 819 | ‫داشور‬
280 820 | ‫=‬    ‫=“‬
281 821 | ‫داوردان‬                                                   
282 822 | ‫ح‬
283 823 | ‫بیان دویم‬
```


## [2026-09-05T18:29:40.596Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in [274,267,278,281]:\n    print('==== leaf',leaf,'printed',leaf+540,'TAIL')\n    print(pages[leaf][-1800:])\nEOF",
 "description": "BQT footnotes on those pages"
}
```


### [2026-09-05T18:29:42.126Z] TOOL RESULT

```
==== leaf 274 printed 814 TAIL
                                              ‫و‬
                       ‫‪.‬‬    ‫‪ -‬وسفله ودون هم هست‬           ‫معنی داسخاله است که دای کوچك ‪ -‬و عصای‬

‫داسه ‪ -‬بروزن‌کاسه ‪ ,‬خهای سرتیزی‬
                                                                                     ‫سر کج‪ -‬وممشوقه باشف ‪.‬‬


‫که برصر دندانهای کندم وحوی )‪ (+‬بود که در‬                  ‫داستگاله ‪ - ۲‬باکاف‪ ..‬بروزن ومعنی‬
                                          ‫چش ‪ :‬جو ‪.‬‬       ‫(‪)۷‬‬           ‫(‪ )۱‬چك ‪ - :‬یی شطه ۔‬


                              ‫رکه ‪ :‬داستار‪.‬‬   ‫‪۳۳‬‬    ‫‪۳‬‬                     ‫‪ :‬دهره ‪.‬‬     ‫رکه‬       ‫‪- ۱‬‬

 ‫بازند و ‪naêtsiãd‬‏ باژند‬            ‫‪"0۳0‬‬           ‫پارسی را حمرمثة‬        ‫رک ‪021584‬‬
                                                                                  ‫‪ - ۴‬س‬
                                ‫‪.‬‬   ‫‏‪ ) dûãtastãn,‬حق » قانون ) بهلوی میداند ‪ « .‬تب رکه ‪۳-6۵‬‬
                                                             ‫داستان زدن » مثل آوردن ‪:‬‬                  ‫‪۴‬‬
               ‫که یکوزد این داستان » هوشیار‬                     ‫چدی کفت با مادر اسفندیار‬
               ‫چو کوبی سخن باز بابی بکوی ‪.‬‬                      ‫که‌پیش زاان‌رازهرکزمگوی‬
  ‫‪.‬‬    ‫«شاهنامه بخ ج ص‪۲۳۹‬‬           ‫فردوحی طوسی‪.‬‬

             ‫فراوان بدو اندرون داستان ‪.‬‬                          ‫® ‪ -‬یکی امه بد ازکه باستان‬
  ‫فردوسی‌طوسی ‪« .‬شاهنامة بخ ج ‪٩۸‬‏ ‪.‬‬
      ‫‪ -‬در اراک بز ‪ 2188580‬ادلی کوچکی‬                             ‫‪۰‬‬   ‫‪ 0‬داستفاله‬   ‫داأماله‬   ‫‪n‬‬    ‫‪۹‬‏‬


  ‫(دای) «سالنامة‬    ‫که باآن علف و بولسه و شبدردرو کنند )(مکی نواد) د رکلپابگانی ‪alãhgsed‬‏‬

                      ‫فرهتک کلپایگان ‪ = »۵4‬داستخاله " داستفاله »داستکاله‪,‬داسخاله‪ ,‬دامکاله ‪.‬‬
  ‫(برهای فاطع ‪)۷۰۱‬‬

==== leaf 267 printed 807 TAIL
ن‬
        ‫‪-‬نی فریاد و فت‬
                     ‫بندمع‬
                         ‫را داد خووان‬
‫است ‪ -‬ویمعنی راستی و عدل وعدالت و اعدال‬             ‫داخل؟ ‪ -‬بثناملك بر وزن کاکل‪,‬‬
 ‫باشدھ ‪ -‬وتظلم‌ووارسیدن‪٩‬‏ وبهرمرا نکیزفتها‬                                 ‫در گاه یادشاهانر | گوبند ‪1‬‬




            ‫(‪ )۳‬خم ‪ :۱‬داچذ‪.‬‬          ‫(‪ )۲‬چك‪ :‬ژند ویاژند ‪.‬‬               ‫(‪ )۱‬چك‪ :‬قرشت ‪.‬‬
                                                               ‫بروزن ناوك ‪۰‬‬   ‫‪۳‬‬   ‫)‪ (£‬چش‪:‬‬



  ‫ائثل‬   ‫‏‪ =١‬دیشليم » نام بادشاهی ات که درکمله ودمنهٌاین المتفع ( چاپ محمد حن‬

                                                              ‫المرصفی ‪ ۷۲۹۱‬م ص(‪ )۹۲‬آمده ‪.‬‬
  ‫‪ - ۴‬داج و داجی (عر ) آز مصدر‬                ‫‪ .‬رك‪ :‬داور‬    ‫بپلوی است‬    ‫‪۴‬‬            ‫«بونکر “‪FA‬‏ ‪.‬‬

  ‫(عر) «داج‌شد جیمء خرباده‌ها ویادم‌های‬         ‫©‬          ‫دجوبمعنی تاريك شدست‪« .‬شرح قاموس»‪.‬‬
  ‫شحنه و بازرگانانندو ازابن است حدیث ‪ :‬هولاءالداج‌ولیوا بالحاج » بمنی پستند حج کزارنده‬
   ‫‪ ۰‬ر=اخوز(«‪.‬م‪).‬‬             ‫بلکه کرابه کش و بداده های شحنه وبازرکانانند‪« » .‬شرح قاموی» ‪.‬‬
   ‫‪ _ ۸‬بهلوی ‪( 120‬قانون) «مناس ‪۱۷۲:۲٥‬‏ ‪ ۰‬یارسی باستان ‪-‬‬                  ‫رك‪ :‬داخل ‪.‬‬      ‫‪۲‬‬
  ‫(قانون» دستور) (ازرشة‪)20202 ۰ 20 .‬؛ اومتاها‪( 2‬ازرسة ‪4d.‬‏ ‪, 1412020‬‬       ‫‪2‬‬
  ‫ارمنیع ‪ » 3‬قس‪ :‬هندی باستان ‪( 02018111 -‬فانون؛دمتور)( ازرسةٌ ے‪0‬ل ‪,‬نا‪4‬طقه) ‪.‬‬
         ‫لب رگ “‪o‬‏ رکه ‪ :‬ح ‪٩‬‏ ‪-‬‬        ‫‪۶‬ارتولمه ‪۹۲‬‬
                                                 ‫« اسدق ‪ » ۸۱0‬ب‬               ‫کردی و افعانی ع ‪0‬‬
                                                                 ‫‏‪ - ٩‬بدو معنی آخیر ‪:‬‬
         ‫و کرتومي ندهی‌داد > روز دأدی صست‪.‬‬           ‫ز کوش پنبه برون‌آر وداد خاق بده‬
   ‫«کلتان ‪. ۹16‬‬

==== leaf 278 printed 818 TAIL
ن‬
                                                               ‫داهو ‪ ۵‬ه بر وزن ابود » بمعنی عفو‬
‫بفردوسی تک‬        ‫‪ ۹۳۳‬اشاره‬      ‫طوس‬   ‫دانای‬
                                                                ‫وبخشیدن کناهی است که بهو ازکی صادرشده‬
                                  ‫وخواجه صیراست ‪.‬‬                                                             ‫باشد ‪.‬‬
 ‫دانج ابروج * بدنتح‌ثالك وهمزه‬                                  ‫بفتح واووسکون‌زای‌نقطه‌دار‪,‬‬     ‫و ره‬    ‫دام‬




                                                                          ‫(‪ )۱‬چك ‪ ,‬چش ‪ :‬مالیدن ‪.‬‬
  ‫بار‬   ‫‪-‬‬   ‫از‪ :‬دام‬   ‫ك‬    ‫‪۳‬‬           ‫ی (ثبت) ‪.‬‬          ‫از‪ :‬دام‬     ‫‪۴‬‬            ‫‪.‬‬     ‫اكم؛ك‬
                                                                                             ‫د ر‬
                                                                                               ‫‪۱‬‬
  ‫(داده ‪ ,‬آفریده)‬         ‫‪2120‬‬    ‫را ازر‪.‬شة قدمی‬        ‫این یوند‬    ‫‪ ۳‬داره‌ستتر (نتبعات‌ایر انی‪ev( .1.‬‏‬    ‫(بوند)‬

              ‫دانته‪ .‬اماهرن احتمال داده از ‪ 2۲80-4‬باشد بمعنی دارنده « اسشق ‪۱۲۱۱٩‬‏ ‪.‬‬
  ‫‪,‬بلکی ‪. 62080‬‬‫© = راله ‪ ,‬تپرانی ‪ 000‬گ‬          ‫‪ ۴‬ےک اسم مفعول از «رأمیدن» ‪۰‬‬


  ‫‪ - ۷‬اوستا ‪ , 2081‬هندی باستان ‪ 20201 .‬۔ (منبع) »‬                                      ‫دانتن‬   ‫‪ "۳ ۹‬رك‪:‬‬

   ‫استی ‪ 6061‬و ‪ . 00‬وخی وسریکلی ‪ « _ 021‬اسذق ‪ ۰۰ ۳۳۰‬پپلوی ‪( 020‬در ‪280.5‬نام‬
                                                     ‫بمعنی بدچهان » زهدان ) «بندهش ‪ ۶۹۰‬ک‪۰‬یلکی ‪. 081‬‬
   ‫‪ = ۸‬دانج ابروج ‪ .‬یز دالج [‪ 612‬قرائت شده‌ولی‌شکل فارسی آن دانك ‪616020‬‬
                                                              ‫‪ ( e.e‬رایج‌تراست ‪« .‬لك ‪۲‬ص ‪.*۷‬‬               ‫‪12040‬‏‬

==== leaf 281 printed 821 TAIL
   ‫‪۳‬‬    ‫دانگانه‬       ‫‪:4‬‬       ‫‪۳‬‬


  ‫حالی‌من اندر عاشقی داوتمامی میزنم ‪.‬‬                 ‫‪ - ۴‬اورنگه کو؟ کلچهر کونفش وفاومهر کو؟‬
  ‫«حافط شبرازی ‪۹۳۲٩‬‏ ‪.‬‬
  ‫* یولهب ‪‎ 120۷27 , ,0۵0027 020۳721 . 0202027‬اتسوا ‪,# 0۵10-02۲2‬‬
                            ‫عیتمرا ‪ « 1803۷07‬قشسا ‪» ۵۳۷‬ههگربند ‪:‬كرو ‪‎‬ربوتاد ‪.‬‬
  ‫‪ 4‬شهر یه از نواحی‬   ‫«راوودان»‬   ‫مصحف‬   ‫یچ ظ»‬    ‫‪۷‬‬                  ‫«دارو» («‪.‬م‪۰ ).‬‬           ‫مصحف‬
                                                                                                  ‫‪_ ۹‬‬

                                                                                         ‫امعم البلدان» ‪۰‬‬            ‫سره‬

                                                                                                   ‫فاحزةٌ ‪۰۲۸‬‬
                                                                                                            ‫صبه‬
                                                                                                              ‫بق‬
   ‫سمنالی ‪ * 80000‬منگری و لاسکردی ‪ . 6881‬سرخەبى ‪ ۰ 6802‬شهمیرزادی ‪49‬‬
                        ‫َة میوه ها‪ -‬بکعدد اژ غله باهيوه ‪:‬‬                  ‫‪ -‬تخم و‬             ‫ه‬
                                                                                               ‫‪: ۲‬‬
                                                                                                 ‫ح‬ ‫‪۸۱‬‬           ‫«ك‪۲ .‬ص‬

            ‫که دانه تا ففشانی نرود ‪.‬‬                                ‫بزرگی بایدت بخشند کی کن‬
   ‫«کلستان ‪.۱1‬‬
  ‫دأاجه ودااژه ورك‪ :‬دائرقا لمعارف اسلام ‪« :‬رانق»‬      ‫‪-‬آبله چنة پرتد گان» دان (ه‪.‬م‪).‬ورك‪:‬‬

                                                                            ‫‪.‬‬       ‫ومزدسنا ‪ 4 ۰۲‬وفاب‪۸۹۱ :۱‬‬
```


## [2026-09-05T18:30:09.049Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if 'اندام' in p and i<500:\n        print('اندام leaf',i)\nfor i,p in enumerate(pages):\n    if 'پنام' in p:\n        print('پنام leaf',i)\nEOF",
 "description": "Locate اندام and پنام in BQT v1"
}
```


### [2026-09-05T18:30:11.611Z] TOOL RESULT

```
leaves 777
اندام leaf 71
اندام leaf 328
اندام leaf 356
اندام leaf 384
اندام leaf 385
اندام leaf 433
اندام leaf 465
پنام leaf 644
```


## [2026-09-05T18:30:16.392Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor leaf in [384,385,644]:\n    print('======== leaf',leaf)\n    p=pages[leaf]\n    print(p[:1200])\n    print('  ---- TAIL ----')\n    print(p[-1400:])\nEOF",
 "description": "BQT v1 andām and panām pages"
}
```


### [2026-09-05T18:30:18.718Z] TOOL RESULT

```
======== leaf 384
انج - بفتح اول وسکون ثانی و جیم»
اطراف 2 روی و رخار ( ۱ ) باشد -
«بمعنی بیرون رفتن وبیرون کشیدن‌هم آمدم‌است
- وامر بان معنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند که‌بنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطه‌دار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزن‌بدبخت»
انش ‌ باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاك‌بروزن‌ب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتی‌و صحرادیست غیرمعلوم-
و مرزنگوش را نیز گوبند و آن نومی آزرباحین
است که در دوا ها بکاد برند و درعریی ! ذان‌الفار
کویند ۴ .
اتجره - بروزن پنجره ؛ نباتی است که
آنرا بعربی بنات النار گویند بقتح بای ابجد ؛ و
نخم آن را قرض‌خوانند وتخم آن مستعمل‌است.
سه‌درم آنرا با شیر نازه بشورند قوت باه دهد
و بکوبند وبا عصل برقضیب مالند سطب کرداند .
)نج ۴ - بنتح اول و سکون ثٌانی
وکسر جیم و سین بی‌نقطة بالف کشده ؛ بمعنئی
ابوخلسا ۴ است که نوعی ازسرخ مردیاشد و آنرا
عربی شجرءالدم گویند , خون شکم را 
  ---- TAIL ----
عنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند که‌بنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطه‌دار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزن‌بدبخت»
انش ‌ باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاك‌بروزن‌ب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتی‌و صحرادیست غیرمعلوم-
و مرزنگوش را نیز گوبند و آن نومی آزرباحین
است که در دوا ها بکاد برند و درعریی ! ذان‌الفار
کویند ۴ .
اتجره - بروزن پنجره ؛ نباتی است که
آنرا بعربی بنات النار گویند بقتح بای ابجد ؛ و
نخم آن را قرض‌خوانند وتخم آن مستعمل‌است.
سه‌درم آنرا با شیر نازه بشورند قوت باه دهد
و بکوبند وبا عصل برقضیب مالند سطب کرداند .
)نج ۴ - بنتح اول و سکون ثٌانی
وکسر جیم و سین بی‌نقطة بالف کشده ؛ بمعنئی
ابوخلسا ۴ است که نوعی ازسرخ مردیاشد و آنرا
عربی شجرءالدم گویند , خون شکم را ببندد .
انح - با خن نقطهدار » بروزن و ععنی
انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
انحکك - باکاف مروزن‌مردمك ءدانه‌ای
باشد سیله شبیه یداه امرود و مفز فد دارد
وآنرا بخورند . خاصتشآاست که هرچند فراش
خبال جاروب سنبل ی تا
بوست آن باه نون
۴ - ۹6۱66۱ «لك۱ سی۱۹۷*.
انحرك « لك ۱ مس ۱۱۲ > .
۶ ملای ۲:۲۷ *.
است توجهی نکر دها ند)
======== leaf 385
- بو -
) فحل س بفتم اول وکسر ثالث و سکون
نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳
عالمتاب است .
انجمن! - ینم اك و قح میم وسکون
نون ۰ مجلس و مجمم را کویشد - بمعنیکروه
انحوج - بروزن محلوح , چوب عود
باشد ؛ و بهترین وی‌آن تکهدر ته آب‌شیند .
کونند عود یخ درختی است که آنرا میکنند
و در زیر خاكث دفن میکنند تا مدنی همین بعداز
آن برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی باشد .
افحوخ - بررزن مطبوخ . چن‌وشکن
روی و اندام باشد از عابت چیری دا سبسد: ۳
و بژمرده شدن میوه را نیز گفته اند - و بمعنی
آب ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
ک
  ---- TAIL ----
برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی باشد .
افحوخ - بررزن مطبوخ . چن‌وشکن
روی و اندام باشد از عابت چیری دا سبسد: ۳
و بژمرده شدن میوه را نیز گفته اند - و بمعنی
آب ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
کندنای کوهی باشد که‌بمربی حشیشةالکلب‌خوااند
و صوف‌الارض نب زکویند - و دشوار زابیدن زنان
را سودمند بود - و بفارسی بمعثی دبزه‌ریزه کرده
شده باشد .
انحیر بر وزن
زنجیس ۰ میوه است
معروف -ومطلق‌سوراخ
را کویندعموماسوسوراخ
کون,! خصوصا - ونام
جوی ات درهرات
و آنرا جوی‌انجیل بلام
هم میگویند .
انجیر ۸3 ه ناممیوءاست درهندوستان
) نحیر دن « بنتح‌اول ودال ابجدیروزن
شمشیر زن» بمعنی سوراخ کردن باشد, چه‌انجیر
بممتی سوراخ است .
انجیره * بروزنزتجیره ۰ بمعنی‌آنجیر
۲ ۰ و ره : دائرمالمعارف اسلام .
9 افجرك .
بمعنی پاشیدن , جممعا : از هم پاشیدن .
======== leaf 644
بیان هیجد هم (۱)
در بای فارسی با نون مشتمل بر شصت ودو لت و کنات
واعمالی که بجهت دفم چشم زخم کنند- وبمعنی
پوشیده و پنهان هم آعده است و بلغت زند
وپازند (۲) پارچه ای باشد چهار کوشه که در دو
کوشة آن دود دوژند ومتابعمان زردشت دروقت
خواندن زند و پازنه (۲) و اوستا آن را برروی
لین « بفتح اول وسکون ثانی» بمعنی اما
وبممنی لیکن باذد.
لنأث « بروزن سواد ؛ بمعنی هوا باشد
وزمن کرده است . خود ندند ۷ .
ودبیر و نوسنیه را گوبشد - وتار ابریشم را ثبز ورخت را گوشة .
گفته اند - و بضه مانندی باشد از رسمان
خش که دور دوك بچیده شود - و ماشوره را
نیز کوبند.
بنام بفتح أول بروزن کلام ۰ تعویذی
ناه ۴ - بفتح اول و الی بالف کشیده
و بهاء زده» بمعنی حمایت باشد- وسابة دیوار را
نیز پئاء گوبند - و امر بدیین ععنی هم هست
یعنی یناه ببر وپناه بخ
ناهد - باها ودالابجد بروزن‌صباحت.
0 در اوستا 8202 - ۳2101 , در هازی 0 , 024۳70201 و 27110 . در
کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏
ینام جزواساحه ولوازم يك‌مرد جنگی بشمار آمده, بجزاین معانی دراوستا وپهاوی پنام عبارت‌است
از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد .
زرنستیان ایران آن دا هروبند» لمتد. این برد؛ کوچك که بنا بتوضیحات ضیر پپلوی اوستا باید
دوبند انگشت پاین‌تر ازدهان باشد» دروقتی بکاربرده ممشودک
  ---- TAIL ----
د ۷ .
ودبیر و نوسنیه را گوبشد - وتار ابریشم را ثبز ورخت را گوشة .
گفته اند - و بضه مانندی باشد از رسمان
خش که دور دوك بچیده شود - و ماشوره را
نیز کوبند.
بنام بفتح أول بروزن کلام ۰ تعویذی
ناه ۴ - بفتح اول و الی بالف کشیده
و بهاء زده» بمعنی حمایت باشد- وسابة دیوار را
نیز پئاء گوبند - و امر بدیین ععنی هم هست
یعنی یناه ببر وپناه بخ
ناهد - باها ودالابجد بروزن‌صباحت.
0 در اوستا 8202 - ۳2101 , در هازی 0 , 024۳70201 و 27110 . در
کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏
ینام جزواساحه ولوازم يك‌مرد جنگی بشمار آمده, بجزاین معانی دراوستا وپهاوی پنام عبارت‌است
از دو قطعه ارچ سفید از جنس پتبه که بروی دهان آویخته با دو نوار پیشت سر کره میززنشد .
زرنستیان ایران آن دا هروبند» لمتد. این برد؛ کوچك که بنا بتوضیحات ضیر پپلوی اوستا باید
دوبند انگشت پاین‌تر ازدهان باشد» دروقتی بکاربرده ممشودکه موبد درمقابل آتش مقدی » اوستا
سراید ومراسم دیتی بجاآورد . استعمال پنام برای آن‌است که نفی وبخار دهن‌بعتصر حقدی‌ترسد.
پنام‌از لوازم آ تربانان (موبدان) است. #يشت ۱ص ۷۹۳ و۲۹۵ ح و۳۵۵4
بتا ! نگارا ! ازچشم بدبترس همی چرا نداری پاخویشتن همی تو ینام ؛
ازین بیت پیداست که مراد همان روبند است نه‌تمویذ (مذ کور درعتن) وفرهنگه‌نویسان
مقر منة چشم بد چنن درك کرده‌اند 1 «کاتها ص۱۲ . زرانشت هرام در اردای وبراف نامه کوبد:
بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
۴ بهلوی 0۵0۵ [ ۳202۵10 یناهی. بناه بردن | از ۶02)8۵1 0808۵1 #از
2 * « تیب رکه ۱۱۹ بنقل‌از هوشمان» و رك: اسشق ۳۲۸-۳۲۷ .
```


## [2026-09-05T18:30:40.742Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(380,400):\n    p=pages[i]\n    head=p.strip().split('\\n')[0][:50]\n    print(i,'|',head,'|','ندام' in p, 'اندر' in p, 'اندك' in p)\nEOF",
 "description": "Scan BQT v1 leaves 380-400"
}
```


### [2026-09-05T18:30:42.720Z] TOOL RESULT

```
380 | که زر بائد! .۷ | False True False
381 | یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان | False False False
382 | اتبارش | False False False
383 | سب ی ٩5‏ | False True False
384 | انج - بفتح اول وسکون ثانی و جیم» | True False False
385 | - بو - | True False False
386 | انجین | False False False
387 | -۱۹۹ - | False True False
388 | اندر خور | False True False
389 | اف | False True False
390 | انسجان | False False False
391 | رن | False False False
392 | اگارده است که افسانه و سر گذشت باشد . | False False False
393 | مردم فررنگ «م هست ٩‏ ۰ | False False False
394 | انگشت ب حرف‌نهادن - کنابه | True False False
395 | یاف | False False False
396 | انگوز زیتونی . . | False False False
397 | نوهیان - بکرم بروزن‌مجوسیان. | False False False
398 | کوبند که بدشواری از انا شود و حل | False False False
399 | رل اس | False False False
```


## [2026-09-05T18:30:48.887Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[387]\nprint(p[:1300]); print(' ---- TAIL ----'); print(p[-1500:])\nEOF",
 "description": "BQT v1 leaf 387 (p.169) andām"
}
```


### [2026-09-05T18:30:50.806Z] TOOL RESULT

```
-۱۹۹ -
)اد « بروزن پرواژ ؛ ممنی شسد -
و میل نمودن - و حمله کردن باشد - و امر
باين معنی هم هست عنی فص دکن ومیل تمای -
است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱
و بممنی مصدرهم افخة ابت که انداختن ,اشد.
انداده ۷ » بروزن خمیازه ۰ یمانتهر
چیز را گویند - و فیای کردن و اندازه گرفتن
را نیز گفته‌اند , و تعرببش بهندسه کرده‌اند ۴ -
۰ بمعنی قدرت و فوت هم آمده است :
) ند ام ۴ « بروزن انجام , معروفت که
بدن رعنو آدمی باشد - و عر کاربر! نیز گویند
که آراسته و بنظام و با اصول بود - و بمعنی
زیبا ‏ و زیبایی هم آمده است - و ادب وآداب
و فاعده .ٍ روش را نیز کویند - و فنای خانه را
هم کنته اند .
ا او - بسکون واو . ترهتیزك باشد ,
/ آن سبزی است خوردنی د آنرا اهل مستان
نره میرم وعربان جرجیر خوانند , وبسضی کویند
جرجیر صحرایبی است که ابپقان باشد .
انداوه بفتح واو , مالهٌ استادان بثا
باشد , و آن افزارست که بدان کل و کچ بریام
ودیوار مالند - وشکوه وشکات - +غیبت رألیز
نند .
)ندایش بر وزن افزاش ؛ بسسنی
کاهگل کردن و گلابه و گچ‌مالیدن باشد .
| ند ایشگر ه بنتح تاف فارسی‌وسکون
رای فرشت. کاهگل و کلابه بربام ودیوار مالندمرا
گومثف .
آبدربایست
آثای4 « بروزن هسابه , بمعنی‌انداوه
. است که مالةٌ اسادان کل کار باشد - و شکوه
وشکایت - وغیبت را نیز گویند .
ودال بی‌نقطه مفترح بخای نفطه‌دار وسن بی‌لقَطةٌ
زده » حمات کننده ودشت ویتاه را گوشد ۰
اند خس و اده » اندخی‌سملوم. وواو
بالف کشنده و رای بی‌نقطة عفتوح ۰ قلعه وصاز-
وجایگاه ب 
 ---- TAIL ----
ایی هم آمده است - و ادب وآداب
و فاعده .ٍ روش را نیز کویند - و فنای خانه را
هم کنته اند .
ا او - بسکون واو . ترهتیزك باشد ,
/ آن سبزی است خوردنی د آنرا اهل مستان
نره میرم وعربان جرجیر خوانند , وبسضی کویند
جرجیر صحرایبی است که ابپقان باشد .
انداوه بفتح واو , مالهٌ استادان بثا
باشد , و آن افزارست که بدان کل و کچ بریام
ودیوار مالند - وشکوه وشکات - +غیبت رألیز
نند .
)ندایش بر وزن افزاش ؛ بسسنی
کاهگل کردن و گلابه و گچ‌مالیدن باشد .
| ند ایشگر ه بنتح تاف فارسی‌وسکون
رای فرشت. کاهگل و کلابه بربام ودیوار مالندمرا
گومثف .
آبدربایست
آثای4 « بروزن هسابه , بمعنی‌انداوه
. است که مالةٌ اسادان کل کار باشد - و شکوه
وشکایت - وغیبت را نیز گویند .
ودال بی‌نقطه مفترح بخای نفطه‌دار وسن بی‌لقَطةٌ
زده » حمات کننده ودشت ویتاه را گوشد ۰
اند خس و اده » اندخی‌سملوم. وواو
بالف کشنده و رای بی‌نقطة عفتوح ۰ قلعه وصاز-
وجایگاه ب ویناه رتکه گاه ماشد - و بناه دنله
ویشتیوانرا دز کنته‌انه 3
| فد جسیدن » بر وزن کم رضیدن ,
.حمایت سودن وپشتی کردن وپشاه دادن- و پناء
کرفتن باشد .
| فك ر؟ » بروزن بندر » بسعثی در باشد
وعریی فی کوبند حمجتانکه الدران و اندر خانه
هنی درون ودرخانه - و افاده ععنی شرت 0
میکند چون بامادر ویدر وخواهر وپرادر کیب
کنند همجو: مادراندر و پدر اندر و خواعر اندر
ار آب » بروزن منجلاب » شهری
است از ولات بدخشان مایین هندوستانوغزلن -
اندر بای » با بلی ایجد بروزن‌صتدل
سای ۰ بمعنی ضروری و حلجت و محتاح البه
وذربایست باشد 9 - ونگون‌وسرازیر وآوشه را
لیز گوبند ٩‏ .
) ندر 1 یست ه بکرتحتالی و کون
سین و فوقانی بمعنی اندربای است که ضروری
وحاحت ومحتاج اله باشف
انداختن .
۴ ماس *: پارسی باسسان؟,8]142.
۱ .رك : اندروای.
```


## [2026-09-05T18:31:01.530Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor leaf in [293,294,296,297]:\n    p=pages[leaf]\n    print('==== leaf',leaf,'| printed ~',leaf+1+1917)\n    print(p[:900])\nEOF",
 "description": "BQT v4 nahādan/nahān pages"
}
```


### [2026-09-05T18:31:03.214Z] TOOL RESULT

```
leaves 553
==== leaf 293 | printed ~ 2211
[pdf page 294]
-۲۱۱- هار
لای غفی هربی هم هست۱ + مهمانی ودیدن مردمان بزر که پوشند ویغیر از
نهاد؟ - بکسراول, ماضی‌نهادن‌است که | این روزها درجایی بسته نگاه دازند.*
بمعتی گذادتن باشد - وبنیاد و سرشت و خلفت نهاره بنتم اول بروزن بهارءمخغف باهار
وطیتت - وباطن را نیز کویند۴ - و بفتح اول » | است که چیزی اخوردن ازبامداد باشد تامدتی‌از
بمعنی طرز وروش ورسم وعادت باشد۴ . روز - ودر عربی از وقت طلوع صبم‌سادق‌است
نهادگی* «بر وزن فتادگی جامه | تاوقت برآمدن آفتاب"- وچ خرچال و سنگه
و لباسی راکوپند که در روزهای مید و روزهای خوارك را نیز گوبند ۷ - و بکر اول » بمعنی
۹ - فارسی جدید 288 ( امروزه 88 تلفظ شود م .م . ) -383 » پهلوی 88 (هز .
7 1) . ایرایی باستان 98811 . اوستا 2۵11 « بارتولمه ۱*۷۲ « لیب رکه ۱۵۹ > هرن
کوید : 86 ( 868 نوشته شود ) » اوستا 82 ۰ پازند 88 , هندی باستان 24 ۰ افغانی 22 ۰
آستی 36 ۰ 28 «اسفق ۱۶۵۵ ر4 : اه هوبشمان ۱*۵۵ کردی 88 (نه) » زازا 26 , 2606
« ابا ۰۰4۲۹ ۴ -رك : نپادن ۰ ۴ - باطن و درون :
==== leaf 294 | printed ~ 2212
[pdf page 295]
هارمه -۱۲ وت
تری وبیم ۱ - و کاهش وکدازنی تن باشد ۴ ؛ | کردن ۷ ؛ وباین معنی بفتح اول هم‌آمده است-
وپاین ممتی‌بفتح اول هم گفته‌اند. نهار - بنم اول بر وزن کداز , بزی
فهاره ۴ - بفتح اول بر وزن هزاره » | وکوسفندیرا کوبند که پیش پیش كلهٌ کوسفندان
بمعنی‌نهاری باشد (۱) وآن طعام اند کی‌است(۲) | براء رود و بعربی کراز خوانند ۸ - و .بطریق
که بدان ناشتا کنند - استعاره بر سروران و پیشوایان قوم اطلاق کنند؛
نهاری ۴ - بروزن‌هزاری, بممنی‌هاره ۱ و باین معنی بفتح اول هم‌آمده است - و بکس
باهد که طعام اند کی است وبدان ناشتاکنند. اول » بمعنی تری و یم باشد ‎٩‏ - وامربترسیدن
نهاریدن » بنتح اول. مسدر بپاراست و واهمه کردن هم هت ‎٩‏ .
که چیزی خوردن اند باشد 8 - و پکسراول, نهاز ید *۱- پشی ترسید و واهنه
بمعنی کداختنوکاستن بدن۹ - وترسیدن وواهمه | کرد .
() چك . چش : نهاری است. () چك . چش : طعامی اندك باشد .
۱ ظ. مصحف « نپاز > (ه.م.) ورك: نهازیدن ۰ ۴ - « لهار , کاهش بود . فرخی
( سیستانی ) کوید :
ملك پرفت 
==== leaf 296 | printed ~ 2214
[pdf page 297]
نهائه که ۷۱-۳

نهاله 4۳ ۱ - بکر اول و قح کاف خانه پسازند - وخانه‌ای را نیز گونتد که درژیر

فارسی , عمخفف نهاله گاه است که شکارکاه | زمین سازند بجهت لشستن درهواهای گرموبغریی
باهد #۰ حقره(۱) خواند ۴ .

8 نهامین - بنتح اور و کر میم بروزن نهان دره - بنتح دال ورای بی‌ضله ۰
سلاطین » بمعلی آهنگر باشد ۴ که عربان حداد بمعنی نهانخانه است که کنجینه ومخزن و خالهٌ
میگویند ؛ و باین معنی بحذف نون آخرهم بنظن زیرزمینی باشد ۴ .
آمد. است که نهامی بروزن تعامی باشد. | اه

نهان پیگران - بنتم بای فرسی . نهاوند * - بکراولوتحواووسکون
کنایه از فرشتگان وملابکه باشد- وجن وپری نون و دال ابجد » یعنی شهرآوند چه له یمعنی
وامثال ایغان را نیز کوبند . 1 شهر باشد وآوند ظروف واوانی راکویند ودرآن
نهان خانه - بروزن‌میان‌خانه, کنجینه آشهر بسیار میاخته‌اند ‎٩۹‏ - و بمعنی شهرستان‌هم.
ومخزبی راگویند که در میان دو دیوار پاکوشة | "آمده است ۷ - و بفتح اول هم هت که بروزن

0 خم ۱: حقیره .

۹ تهاله کاه («م.) :۰

بکوه بر 
==== leaf 297 | printed ~ 2215
[pdf page 298]
-۷۱۵- به رزاق :

دملوند باغد وآن از عراق مجم است ۱ - ولوح | پیچیدن و پیچ وتاب باشد .

میالم بای آن شهر بوده و آنرا اوحاو هه حجره -کنابه از به آسمان است.

یگفته‌اند یعنی لوح نشت ولوح مسند. چه پای

مت یوم میالم ود وآوند تخت وستد و نه حبر که حرمهای حضرت رسالت پذاه

هم‌آمده است و یکثرت استممال نهاوند شد.۴ - صلوات ال علیه وآله می‌بودند +

ونام شعبه‌ای هم‌عست از موسیقی ۳ + نه حصار مینا - پسنی‌سمجرءاست
نهاوندی ۴ - بکر اول بروزن | که نه‌آسمان باشد .

کرامندی , منسوب بنهاوند راگویند - و نام نه‌خر اس ‎٩‏ - با غای قله‌دار» بممنی .

پرده‌ای هم هست ازموسیقی * واین غیرازنهاوند | به حصاراست که کنایه ازنه‌آسمان باشد ‎ .‏

مذکور است که شمیة موسیقی باغدر نه خوش - بفتح اول وخای نقطه‌دار
با < پایای ایجد بالفکنیده ریم .با واو معدوله و اسکون شین قرشت , تاك دشتی

زده کنایه آزنه آسمان است. ۰ راگویشه وآن را بمریی کرمة البیضا خوا ۷
نه پایه - با بای فارسی یالف کشیده | . ونه خوش‌جهت آن کوبندش که میوة
```


## [2026-09-05T18:31:14.394Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT; python3 - <<'EOF'\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[295]\nprint(p[:2500])\nEOF",
 "description": "BQT v4 leaf 295 (p.2213) nahān"
}
```


### [2026-09-05T18:31:16.096Z] TOOL RESULT

```
[pdf page 296]
سنمدها انمک
نهازیدن ۲ - بممنی ترسیدن وواهمه باشد که مخقف شکارگاه - وکمین گاه بلشد.
کردن وبیم بردن باشد . نهاله+ «بکس اول بروزن پیاله.درخت
نهاز یده ۲ ترسیده و واهمه کرده | موزون لورسته باشد ۸ - و شاخهای درختی را
راکویند . نز کوبند که صیادان برسرآن جامهای کهنه بر
نهال - بکر اول بروزن وسال,درخت .| بندند و بر يك جالب دام بر زمین فرو پرد انا
موزون ۳۷ روا را ۳ -و بمعنی |[ جانوران ازآن‌رم کرده بجانب دامآیند۹ -ویمعنی
بستن ونهالی وتوشك هم‌آمده است ۴ - و بمعنی [ کار ۸ - وشکارگاه وکمین گاه صیاد هم آمده
شکار هم هست چه شکارگاه را بهالگاء نیز ‎)٩(‏ اس 1 ۳
میگوشرن ۹ نهاله‌گاه ۷۱ بکر اور 0
نهانگاه > بروزن و معنی شکارگاه 0 ول * یی
باشد - و کمین گاه صیاد را نیز کوبند. شکارگاه - و کمین گاه باشد » چه لهاله بمعنی
تهالگه ۷ - بر وزن و معنی شکارکه ]| شکارهم‌آمده است .
() چش : هم .
۱ - از: هاز (۶.م.) + بدن ( پوند مصدری ) « نهازید , چنان باشد که کوبی بترسید
[ از کی ] با از چیزی . طیان ( مرغزی ) گوید :
لبت کوبی که نیم کفته گل‌است می و نوش اندرو بهفتستی »
زلف کوبی ز لب نهازیده امت بگله سوی چشم رفتستی -
لغت فری ص ۰4۱۶۵
۴ - اسم مفعول از ۸ نهازیدن > . ۴ <نهاله ( «.م. )کردی 2081 (کیاه ۰
درختچه) « ژابا ص4۲۹ >. « لهال » درخت نونشانده بود . عنصری ( بلخی )کفت :
بيك ماء بالاگرفت آن بهال فزون زانکه دیگر درختان بال.»
« لغت فری ص ۰۳۱۲
۴ <هالی < نهالین :
بروز جوانی بدین مایه سال چرا خاك را برکزیدی تال ؟
« فردوسی طوسی . شاهنامة بخ ج ۷ ۰۴۱۹۱۵
و رك : فهرست ولف . - ماله (و.م.) قن :کردی [20۷8 ( کردنه , دره ,
تنکه) , [28۷8 . وقی : هندی 201180 « ژابا س 4۷4 *. ‎٩‏ - از : ال (و.م.) +
کاء ( پوند مکان ) * نپالگه ۳ نهاله کاه (هم). ۷ < نپانگاه < نهاله گاء (ه.م.)
۸ - نهال (هم.)
‎٩‏ - تا زهوای توام ببند ویتاله ( به ندبه وناله . دحخدا )
عشق تو بر جان من نپاد تهاله ‏
شهره آفاق « لغت فری ص 4۳۰ >.
*- باین معنی اصل « نهالهگاء » (ه.م.) است . ۱ از : هاله (ه.م.) + کاه
( پوند مکان ) ۳ نپانگاه ۳ نهاله گه * نهالگه :
ا ز که ری در نهالهگاه توآیند روز شکار تو صد هزار شکاری .
فرخی سیستانی « رشیدی > +
```


## [2026-09-05T18:31:24.172Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gwd\" SOD.txt | head -20; echo '### pages file'; grep -n \"gwd\" SOD_pages.txt | head -20",
 "description": "Grep Gharib Sogdian for gwd'k"
}
```


### [2026-09-05T18:31:24.241Z] TOOL RESULT

```
8298:ayuste  (*ywst)  ©Parth.  >gwd,  }gwst\  MP  }gwh- 
17160:aryawan   ©Akk.  argamanu;  Aram,  argwdnd 
### pages file
4156:    ayuste (*ywst) ©Parth. >gwd, }gwst\ MP }gwh-                      GMS 124, 570, 182 n 1
7958:     aryawan ©Akk. argamanu; Aram, argwdnd                          armin
```


## [2026-09-05T18:31:31.461Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"container\" SOD_pages.txt | head -20; echo '### 174 entry'; grep -n \"^ *174 \\|^174 \" SOD_pages.txt | head",
 "description": "SOD container search"
}
```


### [2026-09-05T18:31:31.529Z] TOOL RESULT

```
16166:            vessel, container, pitcher, measure                            C2, 60R26
37923:(^)conceal    1271, 6866, 7691                container 4362                         counting 6675, 7936, 9271
### 174 entry
```


## [2026-09-05T18:31:34.072Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '16158,16175p' SOD_pages.txt; echo '### entry 4362'; grep -n \"4362\" SOD_pages.txt | head -5",
 "description": "SOD context around container"
}
```


### [2026-09-05T18:31:34.141Z] TOOL RESULT

```
                                                                                                                            174
       yw&kih)

       4362 Yw&'kGi) B         (jjy ; jL^j), jio;l ^j^T ^U=t<o>            monastery
                                                                           Yumr ? ©loc. -y>
            Yo5e (ywdy) ©<Av. gaoiSL, gaoSana
            vessel, container, pitcher, measure                            C2, 60R26
            GMS 1117n 1; TSP 8.108; Dhy. 277, BSTBL; Frag.
                                                                     4374 ywmt'nc      B
              Len. 100c 12; Hen. LW 99; JRAS 1944, 143n3;
                                                                           xumdan                     (j^r JJ <JO*^ /-k) j'-^jp-
              STi 43.9, 10; C2, 94V 21 n pl77                              Hsian-fu(a^,xwmt,n
                                                                                       town in China)
      4363 ywd'r- C                        o^jo^-tjxif                     TSP 2.1233; Ywmt'ncw knS, GMS 1047
                                                                                                                         «/<uo
           ywaSar- ?, yuSar ? ®<wYd}r <wYtw5}r ©perf.
### entry 4362
16163:       4362 Yw&'kGi) B         (jjy ; jL^j), jio;l ^j^T ^U=t<o>            monastery
37923:(^)conceal    1271, 6866, 7691                container 4362                         counting 6675, 7936, 9271
38846:  9638                                   measure       4362, 7756                 millet    1529,4429
39102:pasture      3250, 6541                  period  343, 1045, 1577, 2139,            pitcher      4362, 4453, 9621
39828: vessel 4362                             (to)ward off 3990                       Wehshapur      10557
```


## [2026-09-05T18:31:41.750Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"apadāna\\|apadana\" KNT.txt | head -10; echo '### page 168 leaf 183'; awk 'BEGIN{RS=\"\\f\"} NR==184' KNT.txt | head -50",
 "description": "Kent apadana"
}
```


### [2026-09-05T18:31:43.765Z] TOOL RESULT

```
749:V. Final m is lackmg in туа DB 4.90; tuva XPh 46; X Syana A'Sb; apadāna A'Sa 3, A?Ha 5; ab*yapara A’Sa 4. For all but the last, the forms with -m are found in other passages. Cf. also буа AsH 9, 13°, for буйт ($52. ПІ, $56. V).
4709:Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
### page 168 leaf 183
rnment in Media and Persia, gathered an army of Medes and Persians and marched toward Babylon, passing near Elam. As he passed he sent orders to the Elamites, and in terror they seized Acina and brought him in fetters to Darius, who slew him ($17).
Darius with his army went on toward Babylon against Nidintu-Bel ($18), and in his absence from Media and Persia several rebellions started (§21)— some perhaps started earlier, but news of them did not reach Darius before he had set out against Nidintu-Bel: (a) that of Vahyazdata in Persia, with the adherence of Sattagydia and perhaps of a faction in Arachosia (§45); (b) that of Martiya in Elam; (с) that of Phraortes in Media, with the adherence of Armenia (§26), of Assyria, and of Parthia, including Hyreania (885); (d) that of Frada in Margiana; (e) that of Egypt; (f) that of Skunkha in Seythia (821).
Darius came upon Nidintu-Bel and his army at the Tigris, forced the crossing, and defeated him in IX 26 ($18), and though Nidintu-Bel rallied his forces and took the offensive, again defeated him at Zazana on the Euphrates, X 2 ($19); he pursued him and his few remaining horsemen to Babylon, took that city and Nidintu-Bel with it, and put the rebel to death ($20).
Meanwhile events were progressing elsewhere. Against Frada, who had made himself ruler of Margiana, Darius had sent Dadarshi, a Persian officer who was governor of the neighboring prov- ince of Bactria, with his local forces, and Dadarshi won a decisive victory on IX 23 (838), restoring Darius’s rule in Margiana (839).
Phraortes, claiming to be Khshathrita, of the family of Cyaxares, had made himself king of a great part of the Empire ($21). Darius’s first step was to send Vaumisa, a Persian officer, against the rebels in Armenia; he must have sent Vaumisa early in the Babylonian campaign, for Vaumisa, on the way north, was met by the rebels at [zala in Assyria, on X 15. What forces Vaumisa had at his disposal is not stated, but no mention 1s made of sending troops with him; presumably he gathered up loyal troops on the way. By,this battle Vaumisa
162
drove the rebels back into Armenia, where he fought a second battle with them some months later ($80; see below).
Although the force of Medes and Persians which Darius had with him in Babylonia was small, he had been obliged, at an early date, probably not much after the battle at the Tigris, to send Hydarnes, a Persian officer, with a strong force against Phraortes in Media. Hydarnes met an army of Phraortes (but not Phraortes himself) in battle at Maru in Media, and fought a battle on X 21; but it seems to have been indecisive, for thereafter Hydarnes waited for the arrival of Darius and his army from Babylonia (825).
Parthia and the neighboring distriet of Hyreania had both gone over to Phraortes, but Darius's father Hystaspes was in command of the army in Parthia, and the army remained loyal. In a battle at Vishpauzati, on ХП 22, Hystaspes fought the rebels, but the victory was not decisive.
After the death of Nidintu-Bel at Babylon, Darius set forth for Media against Phraortes (§31). His march took him near Elam, where a Persian named Martiya had set himself up as King under the name of Imanish. At the approach of Darius the Elamites were terrified, and seized Martiya and killed him (§22-§23) Darius now sent a force of Persians and Medes under Arta- vardiya, a Persian officer, against Vahyazdata, who had made himself King in Persia; he himself, with the rest of the Persian force, went on into Media (§41) and at Kunduru was attacked by Phraortes himself and his army, on I 25, 521/0 (§31). Phraortes’ army was routed; he himself es- caped with a few horsemen, but was overtaken and captured at Raga, and mutilated and put to death with torture at Ecbatana ($32). From Raga Darius sent a force of Persians to reinforce Hystaspes in Parthia (§36).
Hereupon a Sagartian named Cicantakhma, perhaps commander of local forces that had ad-
3 Poebel, AJSLL 55.154, sets the undated killing of Martiya after the death of Phraortes, because in the sculptured line of captives on the Behistan Rock the order is Gaumata, Аста, Nidintu-Bel, Phraortes, Martiya, Cigantakhma, Vahyazdata, Arkha, Frada.
```


## [2026-09-05T18:31:50.790Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in [5516]:\n    print('leaf',('\\n'.join(lines[:ln])).count('\\f'))\nimport re\nfor w in ['apadāna-','dāta-','dā- ‘','dātā']:\n    print('###',w)\n    for m in list(re.finditer(re.escape(w),t))[:5]:\n        print('  ...',t[max(0,m.start()-250):m.start()+300].replace('\\n',' '))\nEOF",
 "description": "Kent lexicon dana/apadana leaf"
}
```


### [2026-09-05T18:31:52.714Z] TOOL RESULT

```
leaf 212
### apadāna-
### dāta-
### dā- ‘
### dātā
```


## [2026-09-05T18:31:56.696Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==213' KNT.txt | head -30; echo '=== search dā entries'; grep -n \"apadàna\\|apadāna\\|apadana-\" KNT.txt | head; grep -n \"‘to make, do; put'\" KNT.txt | head",
 "description": "Kent leaf 212"
}
```


### [2026-09-05T18:31:58.592Z] TOOL RESULT

```
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
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
Dàdar&- sb. 'Dadarsh?', (1) an Armenian, (2) а Persian, satrap in Bactria: Elam. da-tur-%-18, Akk. da-da-ar-5u. Репу. of darš- ‘dare’, with re- duplication; Skt. dadhyst- ‘bold’ ($30, §76.III, $152.1, §164.1V). Раат пет. DB 2.29, 31f, 48; 3.18, 15. Dédarsim asm. DB 2.33, 38, 44.
idan- vb. ‘flow’: Skt. dhdn-vati. датира] DZe 9 (or danu[taiy] mid., Wb. KIA 104, after al- ternative suggestion of Bthl. AiW 683); $216, §216.n1.
*dan- vb. ‘be acquainted with’, see z$nà-.
dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
ldar- vb. ‘hold; (intrans.) dwell’: Av. dar-, Skt. dhr-, Lt. fir-mus ‘firm’, Lith. daryti ‘to make’, pIE *dher- ($76.11, $122). See also Upadarma-, Dérayavau-, duruva-, Vidarna-. Present stem dàraya- and conj. 58215. dárayümiy Ist sg. (226.1) AmH 5f; AsH 11, 14; DB 1.26; DPh 4f;
189
DNb 14; DH 4. dárayatty DNd 2 (reading cer- tain, acc. to Wb.’s marginal note to AbkSGW 29.- 142). dàáraya"liy 3d pl. (82321) XPh 23f, 24f. adāraya imf. ($2281) DB 1.85;2.9,3.23; DNa 41; DSe 20Ї°; XPh 19; adáraiya DNa 22 ($48; Wb. AbkSGW 29.33, cf. Kent, JAOS 35.947n; wrongly Hz. ApI 132, as passive). adaá[rayat]à imf. mid. with passive meaning DB 4.90f ($235.II; JAOS 62.268). adaršiy Ist sg. aor. mid. (8218 T, 8233. V) DPe 8. adáüriya imf. pass. ($220, $228JT) DB 2.15, 90.
ham- + dar- ‘get hold of, obtain’: hamadárayaiy Ist sg. imf. (5233. TIT) DB 1.26.
*dar- vb. ‘be angry’, see daríana-.
daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.19
=== search dā entries
749:V. Final m is lackmg in туа DB 4.90; tuva XPh 46; X Syana A'Sb; apadāna A'Sa 3, A?Ha 5; ab*yapara A’Sa 4. For all but the last, the forms with -m are found in other passages. Cf. also буа AsH 9, 13°, for буйт ($52. ПІ, $56. V).
4705:A’Ha = Artaxerxes IT, HAMADAN A. 1 Gatiy : Artax&agà : XS : vazraka : XS : XSyanim : XS : DHyünàm : XŠ : ah 2 yaya : BUyà : Dárayavasahy& : XShya : puça : Dérayavasahyd : ArtaxSatra 3 hyà : XShy& : puça : Artaxšaðrahyā : Xšayāršahyā : XShya : puça : XSayar 4 šahyā : Darayavagahya : XShya : puça : Dérayavasahyd : V?Stáspahyà : puça 5 : Haxàmanisiya : imam : apadàna : vašnā : AM : Anah*la : иа : Mitra : adam : akun 6 ат : AM : Anah'ta : uta : Mitra : mam : püluv : ћасӣ : vispd : gaslá : ut Т & : imam : tya : akunà : mà : vijanátiy : mà : vinátayàtuy Notes то А?На: *? ArtazXatrahyá, acc. to Tm. Lex. 54, and not -cahyd. * [hacd : gastá] WB; [utàmaiy : zsagam] Tm.; [ћасӣ : vispé : gasta] Kent, after A°Sd. " akuna for akundm, and ma with following lost verb, as in A'Sa;
4708:АНЬ = Artaxerxes П, HAMADAN В. apadànam : stünàya : afagainam : ArtaxSaca : XS : vazraka : akunaus : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
4709:Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
4999:apaddna- sb. ‘palace’: from apa- + déna- ($147.I) to root *dà-, cf. Skt. apadhá- ‘conceal- ment’, Gk. атоблк ‘storehouse’. For development in later Iranian, with ара- by secondary length- ening (but not OP appa-, cf. $130), see Henning, Trans. Philol. Soc. 1944.110n. apadünam asm. D*Sal; АНЬ. apadàna (852.V) A’Sa 3, 4; A?Ha 5.
5516:dàna-, in apadana-, daivadàna-: Skt. dhana-m ‘container, receptacle’; from OP *dé- + suffix -na- ($147.1).
```


## [2026-09-05T18:32:10.974Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nleaf=('\\n'.join(lines[:4999])).count('\\f')\nprint('apadana leaf',leaf)\npages=t.split('\\f')\nimport re\np=pages[leaf]\nprint([x for x in re.findall(r'(?m)^\\s*(\\d{3})\\s*$',p)])\nprint(p[:300])\nprint('...')\nprint(p[-400:])\nEOF",
 "description": "Kent apadana page number"
}
```


### [2026-09-05T18:32:12.611Z] TOOL RESULT

```
apadana leaf 190
[]
. Skt. apa, Gk.
and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
apataram adv. ‘farther off, far off’; nsn. of
apatara-, which is apa- + comp. -fara- ($82,
5190.111), ef. Gk. adv. ётотіро. DNa 18; DSe 16f; 
...
*ej(h)om; seen in OP tuvam (cf. adam T’), iyam, imam, patisam, cf. Skt. fuvám тубт imám ete.
ama- sb. ‘offensive power’, see ArSdama-.
amaxamaté, DB 4.92, read by KT, and ap- parently corresponding to Elam. ‘were pleased (at the inscription)’ (cf. Wb. KIA 72n, quoting vari- ant interpretations): possibly for ham-axmatá, aor. mid. of ham- + kam- ‘like, love’ (OP Хата- ‘wish’, Skt. vb. kam- ‘love’),
```


## [2026-09-05T18:32:18.989Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD; python3 - <<'EOF'\nt=open('FFD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i,p in enumerate(pages):\n    if '[pdf page 57]' in p or '[pdf page 58]' in p:\n        print(p[:2000]); print('-----')\nEOF",
 "description": "FFD page 52"
}
```


### [2026-09-05T18:32:20.709Z] TOOL RESULT

```
leaves 115
[pdf page 57]
فعلهای فارسی دری
خوردن
خورد + فارسی میانه ۷۵7۵4 + ایرانی باستان ۷۷۵۲-1۵*. برای 2 آراست.
: خور + فارسی میانه 5۷۵7 < ایرانی باستان ۴*3۵۲-۵. برای 8 -> آرای.
و 3۷/8۲ به معنی (خوردن» و «نوشیدن» هر دو به کار رفته‌اند.
خوشیدن
«خوشید» مادةٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
خوش « فارسی میانه 355 < ایرانی باستان 8۸۵05-8*. برای ۵ -> آرای. ريشةٌ 1205 به
معنی «خشک شدن» است.
واژةٌ «خشک» از ريشهٌ ۳203 گرفته شده است. صورت فارسی ميانةٌ آن 1031 است. از
ایرانی باستان 8۵5-2*. 1805 صورت ضعیف ريشه و 1۵ پسوند است.
دادن
داد < فارسی میانه 434 < ایرانی باستان 43-12*. برای "18 > آراست. ريشهٌ 45
به‌معنی «دادن» است. در ایرانی باستان دو ريشةٌ 48 وجود داشته است: ۱-به معنی
«دادن»» ۲- به معنی «نهادن». «نهادن» از 13 به معنی «نهادن)» آمده است. >
نهادن.
ده < فارسی میانه 42 < ایرانی باستان ۵4۵۵5". 4202 ماد مضاعف است از 43.
داشتن
داشت + فارسی میانه 4381. به جای 4381 باید 417۵ می آمد از 4۲-12* ایرانی باستان.
7 صورت ضعیف ريشةٌ 447 است. برای 1۵ -> آراست. 4351 به قیاس با 137 1351
به‌وجود آمده است.
دار < فارسی میانه 437 < ایرانی باستان 437-۵*. برای 2 -> آرای. 437 صورت بالانده
ريشهٌ 487 است. 447 به معنی «داشتن» است.

-----
[pdf page 58]
ماده‌های ماضی و مضارع فارسی دری ۳ تا ۵۳
دانستن
دانست < فارسی میانه 420191. 432181 در فارسی میانه مادهٌ ماضی جعلی است.
دان + فارسی میانه 438 + فارسی باستان 4202* < ایرانی باستان 2288*: دانستن.
دراییدن
درایید ج فارسی میانه 473[14. در فارسی میانه 47316 مادءٌ ماضی جعلی است که از
7[ ماده مضارع و 14 ساخته شده است.
درای + فارسی میانه 473 « ایرانی باستان 472۳-۵7۵*. 278 برای ساختن مادهٌ
مضارع از ربشه به کار می‌رفته است. 41739 صورت بالاندهُ ريشهٌ 7۷ است و آن به معنی
«گفتن». ۳۷ وازژه‌ای اهریمنی بوده» یعنی برای اهریمن و دیو به کار می‌رفته است.
همین‌طور 4۲371120 واژه‌ای اهریمنی بوده است. در فارسی دری» که در آن واژه‌ها به
اهریمنی و اهورایی تقسیم نشده» «دراییدن» به معنی «یاوه گویی» به کار رفته است.
درودن
درود < فارسی میانه 4۳04 < ایرانی باستان 4۲8-۵*. برای 1۵ > آراست. 475
صورت ضعیف ريشةٌ 478۷ است. 4729 به معنی «درو کردن» است.
درو < فارسی میانه 47۵۷* < ایرانی باستان 45۵۳-۵* برای 2 > آرای. در
فارسی میانهٌ مانوی 47 به جای 4۲3* ایرانی باستان آمده» ۶ و لاجایه‌جا
شده‌اند.
دمیدن
دمید < فارسی میانه 4281۳4 .مادهٌ ماضی جعلی است. از مادةٌ مضارع ساخته شده
است. مادهٌ ماضی اصلی در فارسی میانه 4811 است. از ایرانی باستان 4۵1-1۵*. برای >
13 آراست. کل به جای 427 آمده است. 127 «وزیدن» معتی می‌دهد.
دم « فارسی میانه 487 < ایرانی باستان 4۵-۵*. برای 2 > آرای.

-----
```


## [2026-09-05T18:32:36.752Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,40p tools/fetch_source.py",
 "description": "Check fetch_source tool"
}
```


### [2026-09-05T18:32:36.796Z] TOOL RESULT

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


## [2026-09-05T18:32:43.743Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D8%AF%D9%86\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 124, root Dhe 2, node verification\" ; done",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-05T18:32:47.870Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5f46c64056f8ef06.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b424706bc06183d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3bb0526fa942bdde.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4f8330cd8d3ec994.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/615b2a7bf480027a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/060cb2e73004300f.txt
```


## [2026-09-05T18:32:50.968Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in b424706bc06183d6 3bb0526fa942bdde 4f8330cd8d3ec994 615b2a7bf480027a 060cb2e73004300f; do echo \"########## $f\"; grep -n -A14 -m1 \"Etymology\" $f.txt | head -40; done",
 "description": "Read fetched wiktionary etymologies"
}
```


### [2026-09-05T18:32:52.717Z] TOOL RESULT

```
########## b424706bc06183d6
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
76- 1.4.2 
77- Descendants 
78-
79- 1.5 
########## 3bb0526fa942bdde
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
########## 4f8330cd8d3ec994
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Descendants 
69-
70- 1.3 
71- Further reading 
72-
73- 2 
74- Persian 
75-
76- Toggle Persian subsection 
########## 615b2a7bf480027a
76: Etymology 
77-
78- 2.3 
79- Pronunciation 
80-
81- 2.4 
82- Noun 
83-
84- 2.4.1 
85- Derived terms 
86-
87- 2.4.2 
88- Descendants 
89-
90- 2.4.3 
########## 060cb2e73004300f
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3
```


## [2026-09-05T18:32:56.118Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in b424706bc06183d6 3bb0526fa942bdde 4f8330cd8d3ec994 615b2a7bf480027a 060cb2e73004300f; do echo \"########## $f\"; grep -n \"From \\|Middle Persian\\|Proto-Iranian\\|Proto-Indo-Iranian\\|Avestan\\|Old Persian\" $f.txt | sed -n 1,25p; done",
 "description": "Extract etymology lines"
}
```


### [2026-09-05T18:32:58.229Z] TOOL RESULT

```
########## b424706bc06183d6
146: From Wiktionary, the free dictionary
159: Akin to Middle Persian hndʾm ( handām , “ member, limb ” ) (whence هندام ( handâm ) ), Manichaean Parthian 𐫍𐫗𐫅𐫀𐫖 ( hndʾm /⁠handām⁠/ , “ limb, member; part, section ” ) , Northern Kurdish hinav ( “ organ ” ) , Central Kurdish هەناو ( henaw , “ organ ” ) , Avestan 𐬵𐬀𐬧𐬛𐬁𐬨𐬀 ( haṇdāma , “ limb ” ) . Ultimately from Proto-Indo-European *sem- ( “ together ” ) + *dʰeh₁- ( “ to put ” ) + *-mn̥ .
########## 3bb0526fa942bdde
219: From Wiktionary, the free dictionary
234: Proto-Indo-Iranian *ȷ́ʰástas 
235: Old Persian 𐎭𐎿𐎫 ( d-s-t ) 
236: Middle Persian 𐭩𐭣𐭤 ( ydh ) 
451: Proto-Indo-Iranian *ȷ́ʰástas 
452: Old Persian 𐎭𐎿𐎫 ( d-s-t ) 
453: Middle Persian 𐭩𐭣𐭤 ( ydh ) 
483: Proto-Indo-Iranian *ȷ́ʰástas 
484: Old Persian 𐎭𐎿𐎫 ( d-s-t ) 
485: Middle Persian 𐭩𐭣𐭤 ( ydh ) 
539: Inherited from Proto-Iranian *dasta-bara- , from Proto-Indo-Iranian *ȷ́ʰástas ( “ hand ” ) + Proto-Indo-European *bʰer- ( “ to bear, carry ” ) . [ 1 ] 
541: Alternatively, inherited from Proto-Iranian *danh- ( “ to teach, instruct ” ) , from Proto-Indo-European *dens- ( “ to become skillful; to instruct, teach ” ) , and cognate with Ancient Greek διδάσκω ( didáskō , “ to teach ” ) and Hittite [script needed] ( dassu- , “ strong ” ) . [ 2 ] 
677: Proto-Indo-Iranian *ȷ́ʰástas 
678: Old Persian 𐎭𐎿𐎫 ( d-s-t ) 
679: Middle Persian 𐭩𐭣𐭤 ( ydh ) 
708: Categories : Arabic terms derived from Proto-Indo-Iranian 
709: Arabic terms derived from Old Persian 
711: Arabic terms derived from Middle Persian 
728: Ottoman Turkish terms derived from Middle Persian 
729: Ottoman Turkish terms derived from Proto-Indo-Iranian 
730: Ottoman Turkish terms derived from Old Persian 
741: Persian terms derived from Old Persian 
743: Persian terms derived from Middle Persian 
744: Persian terms inherited from Middle Persian 
745: Persian terms derived from Proto-Indo-Iranian 
########## 4f8330cd8d3ec994
217: From Wiktionary, the free dictionary
276: Probably a clipping of Middle Persian [script needed] ( dātistān /⁠d'tst'n'⁠/ , “ law, process, court case ” ) , from Proto-Iranian *dāt-ya- ( “ of the law ” ) , from Proto-Iranian *daH- ( “ to place, put ” ) , from Proto-Indo-European *dʰeh₁- ( “ to do, place ” ) . [ 1 ] [ 2 ] 
465: From Classical Persian دَاسْتَان ( dāstān ) .
491: Persian terms inherited from Middle Persian 
492: Persian terms derived from Middle Persian 
493: Persian terms inherited from Proto-Iranian 
494: Persian terms derived from Proto-Iranian 
524: Requests for native script for Middle Persian terms 
########## 615b2a7bf480027a
158: From Wiktionary, the free dictionary
682: From Middle Persian [script needed] ( dʾtwbl /⁠dādwar⁠/ , “ judge ” ) . By surface analysis , داد ( dâd , “ justice ” ) +‎ ـور ( -var ) .
765: Requests for native script for Middle Persian terms 
########## 060cb2e73004300f
141: From Wiktionary, the free dictionary
149: From Middle Persian [script needed] ( HNHTWN-tn' /⁠nihādan⁠/ ) , from Proto-Iranian *ni- + *dádaHtī ( from Proto-Indo-Iranian *dʰádʰaHti , from Proto-Indo-European *dʰédʰeh₁ti ) . Compare Northern Kurdish nan , niyan , nihan ( “ to put ” ) , Central Kurdish نان ( nan , “ to put ” ) , Zazaki naene . Northern Luri نیاٸه ( nyae ) , Bakhtiari نݖاڊن ( naaḍen ) .
639: Categories : Persian terms inherited from Middle Persian 
640: Persian terms derived from Middle Persian 
641: Persian terms derived from Proto-Iranian 
642: Persian terms derived from Proto-Indo-Iranian 
651: Hidden categories: Requests for native script for Middle Persian terms
```


## [2026-09-05T18:33:12.011Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/Ahura_Mazda\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/apadana\" \\\n \"https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%AF\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 124, root Dhe 2 (PIE *dheh1-), node verification\" ; done",
 "description": "Archive more Wiktionary pages"
}
```


### [2026-09-05T18:33:17.422Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c93d75a030a9b8ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4a9a197fa4bf72d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea474232e2342af9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b19b0445730b9ccc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7b55cb70afd1a003.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6c23981d4db04917.txt
```


## [2026-09-05T18:33:20.658Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in c93d75a030a9b8ed b4a9a197fa4bf72d ea474232e2342af9 b19b0445730b9ccc 7b55cb70afd1a003 6c23981d4db04917; do echo \"########## $f\"; grep -n \"From \\|Inherited\\|Avestan\\|Old Persian\\|Middle Persian\\|Proto-Iranian\" $f.txt | sed -n 1,14p; done",
 "description": "Read second batch etymologies"
}
```


### [2026-09-05T18:33:22.476Z] TOOL RESULT

```
########## c93d75a030a9b8ed
169: From Wiktionary, the free dictionary
189: Transliteration of Avestan 𐬀𐬵𐬎𐬭𐬀 𐬨𐬀𐬰𐬛𐬁 ( ahura mazdā ) . Doublet of Aramazd and Hormuz .
228: Avestan: 𐬀𐬵𐬎𐬭𐬀 𐬨𐬀𐬰𐬛𐬁 ( ahura mazdā ) 
255: Old Persian: 𐏈 ( AM /⁠a(h)uramazdā⁠/ ) 
291: Borrowed from Avestan 𐬀𐬵𐬎𐬭𐬀 𐬨𐬀𐬰𐬛𐬁 ( ahura mazdā ) .
318: Categories : English terms borrowed from Avestan 
319: English transliterations of Avestan terms 
320: English terms derived from Avestan 
328: Portuguese terms borrowed from Avestan 
329: Portuguese terms derived from Avestan 
351: Terms with Avestan translations 
367: Terms with Old Persian translations 
########## b4a9a197fa4bf72d
236: From Wiktionary, the free dictionary
246: From the root د ي ن ( d y n ) . Compare Hebrew דן .
1700: From the root د و ن ( d w n ) .
1974: From Proto-Indo-European *deh₃- ( “ to give ” ) .
2230: From زبڵ ( zibil , “ rubbish ” ) + -dān to form زبڵدان ( zibildan , “ dustbin, trash can ” ) . 
2249: From Middle Persian [script needed] ( dʾn' /⁠dān⁠/ ) , from Proto-Iranian *daHnáH , from Proto-Indo-Iranian *dʰaHnáH , from Proto-Indo-European *dʰoHnéh₂ .
2320: Inherited from Arabic أُذُن ( ʔuḏun ) .
2363: Persian terms inherited from Middle Persian 
2364: Persian terms derived from Middle Persian 
2365: Persian terms inherited from Proto-Iranian 
2366: Persian terms derived from Proto-Iranian 
2391: Requests for native script for Middle Persian terms 
########## ea474232e2342af9
191: From Wiktionary, the free dictionary
308: From Middle Persian [Book Pahlavi needed] ( nyhʾn' /⁠nihān⁠/ , “ concealment, secrecy ” ) .
390: Persian terms inherited from Middle Persian 
391: Persian terms derived from Middle Persian 
402: Requests for Book Pahlavi script for Middle Persian terms 
########## b19b0445730b9ccc
########## 7b55cb70afd1a003
164: From Wiktionary, the free dictionary
178: From Old Persian 𐎠𐎱𐎭𐎠𐎴 ( a-p-d-a-n /⁠apadāna⁠/ ) . Doublet of iwan .
207: Old Persian: 𐎠𐎱𐎭𐎠𐎴 ( a-p-d-a-n /⁠apadāna⁠/ ) 
225: Borrowed from Old Persian 𐎠𐎱𐎭𐎠𐎴 ( a-p-d-a-n ) .
297: Categories : English terms borrowed from Old Persian 
298: English terms derived from Old Persian 
304: Polish terms borrowed from Old Persian 
305: Polish terms derived from Old Persian 
330: Terms with Old Persian translations 
########## 6c23981d4db04917
181: From Wiktionary, the free dictionary
209: Inherited from Proto-Middle Indo-Aryan *𑀤𑀸𑀤𑁆𑀤 ( *dādda ) .
238: From Middle Persian [script needed] ( dʾt' /⁠dād⁠/ , “ law, justice ” ) , from Old Persian 𐎭𐎠𐎫𐎶 ( d-a-t-m /⁠dātam⁠/ , “ law ” ) , from Proto-Iranian *daHtáh , from Proto-Indo-European *dh₃tós ( “ given ” ) . Compare the Iranian borrowings: Classical Syriac ܕܬܐ ( dāṯāʾ ) , Hebrew דָּת ( dāṯ ) , Old Armenian դատ ( dat ) .
349: Persian terms inherited from Middle Persian 
350: Persian terms derived from Middle Persian 
351: Persian terms inherited from Old Persian 
352: Persian terms derived from Old Persian 
353: Persian terms inherited from Proto-Iranian 
354: Persian terms derived from Proto-Iranian 
374: Requests for native script for Middle Persian terms
```


## [2026-09-05T18:33:40.910Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '2235,2270p' b4a9a197fa4bf72d.txt; echo '#### panam file'; wc -l b19b0445730b9ccc.txt; head -30 b19b0445730b9ccc.txt",
 "description": "Check dān and panām entries"
}
```


### [2026-09-05T18:33:40.966Z] TOOL RESULT

```
 Conjunction
 [ edit ] 

 دان 

 Jawi spelling of dan .‎

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 From Middle Persian [script needed] ( dʾn' /⁠dān⁠/ ) , from Proto-Iranian *daHnáH , from Proto-Indo-Iranian *dʰaHnáH , from Proto-Indo-European *dʰoHnéh₂ .

 Alternative forms
 [ edit ] 

 دون ( dun ) ( eye-dialect ) 

 Noun
 [ edit ] 

 دان • ( dân ) 

 grain 

 Derived terms
 [ edit ] 

 دانه ( dâne ) 

 دان‌دان ( dân-dân ) 

 References
#### panam file
5 b19b0445730b9ccc.txt
URL: https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%85
FETCHED: 2026-09-05T18:33:16Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T18:34:02.084Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/124.jpg 2>/dev/null; pdftoppm -f 124 -l 124 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg124 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 124"
}
```


### [2026-09-05T18:34:04.666Z] TOOL RESULT

```
site/pages/124.jpg
total 36600
drwx------ 3 sfmqrb sfmqrb    12288 Sep  5 14:34 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58735 Sep  5 14:20 mk120.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62270 Sep  5 14:32 mk121.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  5 14:28 p117
-rw-rw-r-- 1 sfmqrb sfmqrb     1984 Sep  5 14:27 p125_butik_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64316 Sep  5 14:23 p125_dhemo.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8603 Sep  5 14:30 p125_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62327 Sep  5 14:23 p125_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2177 Sep  5 14:27 p125_tem_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30941 Sep  5 14:26 p125_tem.png
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
-rw-rw-r-- 1 sfmqrb sfmqrb   330167 Sep  5 14:18 pg121_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82335 Sep  5 14:17 pg121.png
-rw-rw-r-- 1 sfmqrb sfmqrb   461010 Sep  5 14:18 pg121_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61026 Sep  5 14:18 pg123.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91077 Sep  5 14:34 pg124.png
-rw-rw-r-- 1 sfmqrb sfmqrb   300310 Sep  5 14:27 pg125_900.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75202 Sep  5 14:23 pg125.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


## [2026-09-05T18:34:09.351Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg124.png"
}
```


### [2026-09-05T18:34:09.954Z] TOOL RESULT

```

```


## [2026-09-05T18:34:09.951Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T18:35:50.029Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo '=== BRT Mundbinde variants'; grep -n -i \"undbind\\|Mundb\" BRT.txt | head -5; echo '=== BRT paiti.d'; grep -n \"paiti\\.d\\|paitid\" BRT.txt | head -12; echo '=== HRN penhan'; grep -n -i \"penhän\\|pinhän\\|penhan\" HRN.txt | head -5; echo '=== MON andam'; grep -c \"اندام\" MON_part1.txt MON_part2.txt 2>/dev/null; echo '=== book Da 2 root'; grep -rl '\"name\": \"Dâ 2\"' /home/sfmqrb/git/rishe/data/extracted/batch/ | head -3",
 "description": "Assorted verification greps"
}
```


### [2026-09-05T18:35:50.146Z] TOOL RESULT

```
=== BRT Mundbinde variants
=== BRT paiti.d
4147:Wesenheit,  Menschheit,  alle  Welt':  tarn  . . alva  vispahe  'nhlui  astvatS  anaiwyästis iunahiY,  18.^0;  31;  —  :^aSaya  .  .  vispd 'jtkui  astvä  *)vaiti  anläse  framiryeite  Y.3. 33;  J-i.  5-4,  Y./p.io,  F.^h;  —  zam  .  . yä  vTspsm  °hBm  astvant>m  baraiti  jumca iristitnifaYl.  13.^;  129,  JO.51,  ;(),94,  Y./"?. 2,  57.16,  Y.  18.16,  A.4.6;  —  vjspähe 'lik^ul  asti'ais  sragstim  Y.O.  i;  Yt7.  2', ÄS4,  y.152,  75.79,  P.2.^  ^-84,  Vyt. 36.  ß)  insbes.  von  der  Gesammtheit  der nichtpriesterlichenOemeindeangehörigen**: zaotars{^d.)  iairim  .  .vacimca  °wÄf(DS.)'^ astvaite  paiti.dhayai  N.  72.  b)  'das  erste, d.  i.  das  materielle  Dasein,  Leben':  yaii ä  °rihul  *pa<mruyS  bavat  (sd.)  Y.  2S.11; — *_j'((^ö  äis  i^ä  vansaitg  yä  data  'uAiuf paouruyehyä  ratul iyao^ana  rasistä(sd.) .  . Y.33.1;  zit.  55.6;  —  °uASus  sq>di  (sd.) paouruyehyäY.  48.(>.  c)  'dieses,  d.  i.  das irdische  Leben,  Dasein':  "»hSus  maraxtärö (sd.)  ahyä  Y. 32.\^'>'i;  —  'ijAjus  ahyü paourrtm  *yqm  mSi  vtdvä  (sd.)  .  .  "was zu  Anfang  dieses  Lebens  .  ."  4^5-3;  4;  — ahyä  'uhiuif  vtspa  maS>ä  (sd.)  Y.J4-6; —  ahmäicä  °huyg(Xi5-)  manahyäicäY.  4f>. 2;  —  aliKa  °uh}us  manahyeheca  'uhsus Vyt  32;  —  s.  noch  unter  a.  d)  'das
10302:81;  81,  85.  a)  in  der  Rechtssprache Ort  des  Gerichts,  Gerichtshof,  Forum': vff  *naird  *p^rpnp/ni/äi  nöit  paiti.däöaiti 'tiimca  *varaua(sd.)  zrvünainca  Y . 4c;  — yS  nara  'tum  baraiteY.4A^)^'.  3)'Slätte zum  Ruhen,  Liegen,  Sitzen'  sva.  'Lager- statt, Bett,  Divan,  Sessel,  Thron',  auch im  Plur.:  ava  kl  (näml,  dem  Leichnam) 'tum  barayan  ätryehe  (sd.)  vä  .  .  V.  <?.8;
11344:•  j.  äidrö.daxSta-  Adj.  'der  ein  offen- bares, deutliches  Zeichen  hat,  bietet  von  ~, für  —'  (Gen.):  agmca  ahe  'ts  anhat  alm ii>rS.paiti.dayB  V./.  14  Gl.
11346:•  j.  didrö.-paiti.daya-  Adj.,  'der  ein  offen- bares, deutliches  Merkmal  hat,  bietet  von  — , fiir— '(Gen.):  almca  ahe  cihrsJaxstS  ar^hal aim  'yö  V.J.  14  Gl.
12480:•  j.  'daeva-  Adj.  (fem.  'dapvj-)  'den Dapva  zugehörig,  von  ihnen  herrührend (usw.),  rfa?iisch':  kB  asti  'vö  ks  da^aySzB "wer  gehört  zu  den  Z>.,  wer  ist  ein  Z>.- Anbeter?"  V.Ä31;  32';  —  kva  asti  'vB kva  datvaydzB  Y.y.sz'y  54'.  yt77.6;  — yat  nürsm  vyämbura  (sd.)  'va  maSyäka da^vayäsB  vohuntm  vä  täc^änti  YL  7^.  54; — -  ga%Bittsca  'vJsüa  *handramana  (sd.) N.  5j;  Yt.  77, 6.  et)  sonst  von  drug-: aiXm  dahaktm  ..  'vTm  *dru/im  V.5. 8;  — Hat  ki  ha,  paiti.davata  ya.  'vi  druxl  V. 18.  $1;  —  nase  °vJ  druxs  SrB.j;  — sraosim  ..yd  janta  °vaya  drujB  Y.57. 15.
12768:j  2.  7;  9,  35;  —  paiti.dämm  *ainim  baraiti
13272:mit  paiti  'mit  seinem  Blick  begegnen, treffen,  erblicken':  mä  mam  drvS  paiti *di>.sis  {2SPrA.)'>  Vyt  50;'  —  yai  nsif näiriia  a>re  *raoxmqm  paiti.ätöyät^'' "sonst  könnte  die  (menstruirende)  Frau des  Feuers  Flammen  mit  ihren  Blicken treffen"  V.  j6'.  2**;  —  mmö  mSuhai  .. paiti.dJiäi  "Verehrung  dem  Mond  ,  . dem  erblickten"  Yt?.  i.
14057:'halten,  an  sich,  mit  sich  haben,  führen', Med:  ys  *paeurvd  väs?m  (sd.)  vazäite qxna  (sd.)  drazaite  väsake  Yt  5. 1 1 ;  — saranaitam  paiti.dän>m  vaauhi  Aiitatte drazimnö  (statt  NSf.)  andvi  Vt  5. 133.  a)  bes.  mit  IS.  oder  LS.  aus sasta-  m.:  tardhustrS  .  .  asänS  %asta äraiimrtö  V. /(^,  4;  —  *avazaite .  .  snai- äi7  sastaya  drasimnS  Y.  57.  31;  V.  ig. 15;  —  mtkirfm  yS  . .  aiwyäiti  .  .  vazrvm tastaya  *dra3imitiiYt.io.g6.  Unklar: kva  hs  draiahe  aiiiAs  lamS  .  .  V.  ig.  4.
14105:•  j.  drSd-a-  m.  EN.  emes  Gläubigen: '^ahe  alaota . . paiti.drä^ahe . .  Yt,y,i09.
14931:•  j.  *paitida.gaodana-''  Adj.  'verschiedene
14947:•  j.  paiti.daya-  m.  i)  'der  die  Aufsicht führt,  Beaufsichtiger':  tiltrJm  ..yim  ratäm 'daimca'^  vTspaesqm  stärqm  frada%al ahurO  mazda  ya%a  narqm  zardiuftnm Yt  S,  44.  3)  'Erkennungszeichen,  Merk- mal' (?,  nur  Komp.).
14949:•  j.  paiti.darana-  n.  'Ort  des  Verweilens, Aufenthaltsort':  /m  imqm  damqm  .  .  fra- pinaoiti  satim  * paitiltananqm  (sd.)  haxaa- nm  °ranqm  (GP.)  V._j.  31.
=== HRN penhan
3140:332. penhän, pinhän Verborgen'.
3144:es wird von den Wörterbüchern als aus penhän con-
3187:röl pinhän mehimed z'esän heröz
13263:penhän 144, 332.
13268:I penhän 332.
=== MON andam
MON_part2.txt:102
MON_part1.txt:117
=== book Da 2 root
```


## [2026-09-05T18:35:57.848Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12760,12775p' BRT.txt; echo '#### Horn 332'; awk 'BEGIN{RS=\"\\f\"} NR==(144+21+1)' HRN.txt | sed -n '1,40p'",
 "description": "Bartholomae paiti.dana and Horn penhan"
}
```


### [2026-09-05T18:35:59.593Z] TOOL RESULT

```
Substantiv  oder  subst.  Pronomen:  ä  Aaoms
upait  sara%u/lr?m..ä  °im  (ASm.)  p>r7sai
sarahuäröY.g.i;  'Vt.S.$j,  lO.  ixi,  I2.i,
VyL2/;  —  ya^a  tiyri/ yim  a^hat..  laoa
*°rm''>  ahurS masdä  avqn  Yt(V,6t;  38,  ai,
23  (Vm)",  25,  io.\  (*iÄ>«)",  77. 82,  ig.
68,  H.2.16,  34,  P.^2;  —  yS  nars  asaonS
urva  .  .  ü  °im  väiS  upa.vilvB  saoayeiti  H,
j  2.  7;  9,  35;  —  paiti.dämm  *ainim  baraiti
\.  .  mä  'im  mruya  a%rava>am  V.  18.1;  —
■yat  duids  fradvaraiti  .  .  *yufydU   välmt
1  mi^rS  .  .  rasmS.jatfiH  vä  'im  Jainti  amU.- ■Jatim  va  Yt.  10.53 ;  Fr.<?.  i,  V.5.83,  Ä 10"',
20.  3, ''A.^j.  13'-'*;  —  (ÄJÄMfl  dahmäi  aoxte
dby  Google
68s
day- 1  I
#### Horn 332
— 144 —
bei. LW. zal 'Frau', spec. 'Ehefrau, Gattin (419);
af/. zör; yidg. zör 'alter Mann, Greis.
Hier stehen r und / im Neupersischen neben einander
(vergl. zer, No. 655). Nach den persischen Wörter-
büchern ist dieser Fall sehr häufig, doch läuft hier
viel Dialektisches mit unter. Meine Sammlungen über
den Gegenstand sind noch nicht abgeschlossen, so dass
ich über die Stellung des Neupersischen zu Brug-
mann's Erwartung (Grundriss I, 210, 211) noch kein
Urteil habe gewinnen können. Doch glaube ich nicht
an wichtige, positive Ergebnisse.
G48*^'« i^änü 'Knie .
aw. zänti' 'Knie' in zänu,[dräjao , vergl. frasnu-
(skr. prajUn-) ^) ; phlv. zünük, jfänäk (letzteres entweder
dialektisch oder auch zänük zu lesen); 2l\, jdnu- 'Knick-
arm, cunr 'Knie* (H. No. 138).
kurd. zCLna; af/. zangün^ cangün; bei. zän (421);
wa;^. zatij sar. zm^ sangl. zong.
649. t^äiv 'Spalt, Riss'.
Zu [/"gap" {Jap-) 'klaifen, tief sein , vergl. aw. Ja/ra-
jqfnH' (Nöldeke, mündliche Mitteihmg).
i)i}0, ^ehän, zuhän (AM.) 'Zunge*, zefan-),
g. izvFin (Käs. Q. ilzün ist natürlich arab. lisän).
ap. izavani'^) 'die Zunge*; aw. hizü'\ phlv. nzvän
bezw. huzDän, ziivän bezw. zavän ; ai. jikvä-,
kurd. azmän 'Zunge'; af/. ziha\ oss. t. äuzdg (4);
hol. LW. ztivan^ n. zavan (311); siyn. zev, sar. ziv,
wa/. zik.
Über die indogerm. Grundform hat zuletzt Johans-
son Indog. Forsch. II, 1 folg. gehandelt.
051. lieber 'über, darüber, auf, zewer, vergl. zehet'dest 'die
Oberhand besitzend'.
') Über znii' wird hoffentlich die neue Ausgabe Klarheit bringen.
2j z/f/. X^'ärezm. Fol. 656 r (Berliner Handschrift); jedenfalls
dialektisch, vielleicht ;^^'ärezmisch.
'j Vordflchti<»o Form; Bartholoniao, BB. XIV, 245 vermutet
hiznrani.
```


## [2026-09-05T18:36:05.731Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -A8 \"^332\\. penhän\" HRN.txt | head -20",
 "description": "Horn entry 332 penhan"
}
```


### [2026-09-05T18:36:05.779Z] TOOL RESULT

```
3140:332. penhän, pinhän Verborgen'.
3141-phlv. pa (pO) nihan (s. No. 1058) ; Nöldeke, Kärnämak
3142-67, Note 2.
3143-Np. pendm bedeutet ebenfalls Verborgen, bedeckt';
3144-es wird von den Wörterbüchern als aus penhän con-
3145-trahirt angesehen (zu m für n vergl. bam, bau 'Dach') ^) ;
3146-mit parsisch penäm (jpenöm)^ aw. paiti.däna-, phlv.
3147-padäm, wird np. penäm Verborgen' nichts zu thun
3148-*) loh orgreife diese Gelegenheit, um den BB. XVII, 261 Note 2
```


## [2026-09-05T18:36:18.763Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D9%87%D8%A7%D9%86\" \\\n \"https://www.iranicaonline.org/articles/dastur\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 124, root Dhe 2: penhan and dastur origin\" ; done; echo ---; grep -n \"From \\|Inherited\\|Middle Persian\\|Proto-Iranian\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/%D9%BE%D9%86%D9%87%D8%A7%D9%86'.encode()).hexdigest()[:16])\").txt | head -6",
 "description": "Fetch penhan and Iranica dastur"
}
```


### [2026-09-05T18:36:22.433Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fbaa26332eb29108.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfba0cc8b5e1adcf.txt
---
144: From Wiktionary, the free dictionary
157: From Middle Persian [Book Pahlavi needed] ( PWN /⁠pad⁠/ , “ to, at, in, on ” ) + Middle Persian [Book Pahlavi needed] ( nyhʾn' /⁠nihān⁠/ , “ concealment, secrecy ” ) . originally a contraction of elements equivalent to New Persian به ( be , “ in ” ) + نهان ( nehân , “ hiding ” ) , i.e. "in hiding".
248: Categories : Persian terms inherited from Middle Persian 
249: Persian terms derived from Middle Persian 
257: Hidden categories: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-09-05T18:36:25.274Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; head -6 dfba0cc8b5e1adcf.txt; grep -n -i \"dastwar\\|dastūr\\|dast-\\|hand\" dfba0cc8b5e1adcf.txt | head -12",
 "description": "Check Iranica dastur fetch"
}
```


### [2026-09-05T18:36:25.332Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/dastur
FETCHED: 2026-09-05T18:36:22Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 500: Internal Server Error
```


## [2026-09-05T18:36:30.616Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nfor m in list(re.finditer('اندام',t))[:6]:\n    print('...',t[max(0,m.start()-200):m.start()+250].replace('\\n',' '),'\\n')\nEOF",
 "description": "Mo'in andam entry"
}
```


### [2026-09-05T18:36:32.799Z] TOOL RESULT

```
...  کنند» مخزن اب؛ ایدان» ایکین تالات.    اب‌انداز؛ 7-. 23 (امر .) تو قفگاه ستوران    در میان دو منزل برای رفع خستگی. . جوبی  مبان تهی که جوب دیگٌر در میان 9  برند و به فشار آب در آن کنند؛ آب‌دزدکک.  آب‌اندام: 2.0 (ص‌مر. آمر.) آنکه  دارای پبیکری زیبا است. خوش شکل؛  خوش قد و قامت.   ابانگان: 2027-00 (امر.) جشنی در ایران  باستان که در روز آبان (دهم) از ماه آبان بر پا  می‌داشتند.   آب‌انگاه: ۰ 20210-850 (امر.) روز دهم  فروردین. . گویند اگر در این روز ب 

...  از عمارت مرکب از چند اطاق و ضمایم  آنها. (ند.) ساختمان مجزا و مستقل.  ایاندیس: 528 (۱.) (جان.) زایدة کیسه  مانند کوچکی است در قسمت تحتانی اعور؛  آویزه (فر ه۵.)) ضمیمه اعور» زابده رودة  کور. قسمتی از اندام‌های حشرات (از قبیل  پنجه و آرواره‌ها).   اپ‌اندیسیت: م1۱54 (.) (بز.) ورم  ضممه رودة کور که سیار دردناک و گاه  کشنده است.   آتربان: 2107-00 (امی.) در آیین زردشتی  نگهبان آتشن ققداش:   اترویین: 2017 (.) (بز.) شبه قلیابی  است سمی که از مه رگیاه گر 

... مق. روبه ابره» ظهاره. (نق.) رنگ اولی که  ه روی در و دیوار و بوم مالند.   استر: 2-6-۲ [- آن سوی‌تر ] (ق.) 11  سوی تر. زاستر.   انشجمات : «6ا)هجرعآاوع (.) (بر. فز .)  عارضهاق که ور شخ رط وس و  نمی‌توان اندام جسمی را بطور واضح و  آشکارا دید. این عب به علت نامنظم بودن  قرنیه ( که کروی نباشد) و یا جلیدیه (که  نامنظم باشد) ایجاد می‌شود. در این صورت  از آن وال تم تست که توا  قسمت‌های مختلف یک جسم بر روی نقطة  زرد کارا بل برای رفع ۱ بسن  عیب از شیشه‌های  

... الات: :715 (ع.] (.) ج. آلت. انزارها  اسزارها)ا؛ ادوات» اسیات. آلات تغد به:  مجمو ع عضوهایی که در کار تغد به بکار  است. الات تناسل: عضوهایی در حبوان از  نر و ماده که سب تولید مثل و نتاج است.  الا ین : اندام‌ها از حنجره و ریه و غیره  که در حیوان وسئلهة تنفس است. آلات  حیات: آنچه از اعضاء و غیر آن که برای  ادامةٌ زندگانی لازم است. آلات جارحه:  افزارهای طبیعی و غیر آن از چنگال و دندان  و شمشیر و کارد و غیره که برای جراحت  وارد آوردن بکار رود. آلات دف 

... سر.) (بز.)  ازدیاد مواد سفیده‌یی (پروثیدی) در ادرار»  ازدیاد مواد ات آلی ادرار.   آلت: ؛هاة (ع. آلة] (ا.) واسطٌ میان فاعل و  مفعول در رسیدن ائر» چون اره برای نجار»  افزار» ابزارء ادات. سبب؛ مایه. عضو اندام.  زین و ب رگ (اسب)» براق (اسب). (جاد.)    ات تسناسلی زن و مرد؟ ج. ات ات  رجولیت: الت مردی. آلت زنانگی: (جان.)   قبفت خارجی عضو ساسی زن؛ فرج)  دریچه مهبل» آلت مادگی. لش مادگی:  (جاد.) عضو تناسلی کلیه حوانات ماده و  انسان؛ آلت زنانگی. آالت مردی:  

... یی»  الهی» غیبی.   آنسه: (م)ععهة (ع. آنسة] (افا.) منك  وه خانم (غم.)؛ ج.  آنسات.   آنک: 20-1 کلمه‌ای است دال بر اشاره به  دور اعم از مکان و زمان. آنگاه» آنحا؛ مق.  اینکث.   آنک: : 501 ((.) آبله که بر اندام هی | نلن:  انی؛ ۰ 3006 [ع.] (.) سرب» اسرب.   آنک: (2-160 [- آنکه] (ضم. + موصول)  آنکه.   آن‌کجا: 2-113 (ضم. ب+ موصول) آنکه,  آن کس که. آنجه.   انگاه: ۰ 270-888 (ق. زمان) زرمان» آن  وفت» آن هنگام. , پس از آن» سپس بعد» در  آخر. . مع‌هدذ اه مع‌دلک
```


## [2026-09-05T18:36:42.689Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%A7%D9%85/\" --note \"pdf 124 node 5: Mo'in's entry for andām\" 2>&1 | tail -2; python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A7%D9%85/\" --note \"pdf 124 node 5: Mo'in/Dehkhoda entry for panām\" 2>&1 | tail -2",
 "description": "Fetch abadis Mo'in entries"
}
```


### [2026-09-05T18:36:48.092Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c6519b38359f13f8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3dc12538b80b07c1.txt
```


## [2026-09-05T18:36:51.797Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"=== andam\"; grep -n -o \"فرهنگ معین.\\{0,300\\}\" c6519b38359f13f8.txt | head -3; grep -n -o \"اندام.\\{0,200\\}\" c6519b38359f13f8.txt | head -5; echo \"=== panam\"; grep -n -o \"پنام.\\{0,250\\}\" 3dc12538b80b07c1.txt | head -6",
 "description": "Read abadis entries"
}
```


### [2026-09-05T18:36:53.701Z] TOOL RESULT

```
=== andam
60:فرهنگ معین
171:فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راه
4:اندام - معنی در دیکشنری آبادیس
6:اندام - معنی در دیکشنری آبادیس 
10:اندام
13:اندام : بدنه، پیکر، تن، تنه، جثه، جسم، قامت، قد، کالبد، هیکل، آلت، جوارح، عضو، ارگانیسم
20:اندام. [ اَ ] ( اِ ) بدن. ( برهان قاطع ) ( سروری ) ( هفت قلزم ). بدن و تن. ( انجمن آرا ) ( ناظم الاطباء ). بمجاز تمام بدن بلکه مطلق جسم را گویند لهذا اندام گل ، اندام کوه و اندام آفتاب هم آمده. ( غیاث اللغ
=== panam
4:پنام - معنی در دیکشنری آبادیس
6:پنام - معنی در دیکشنری آبادیس 
10:پنام
16:پنام (پسر) (فارسی) (تلفظ: panām) (فارسی: پَنام) (انگلیسی: panam) 
22:پنام. [ پ َ ] ( اِ ) در اوستا پئیتی دان و در پهلوی پدام و پندام و پنوم گویند. در آبان یشت ، کرده 29 آن عبارت است از جامه ای که در زیر زره پوشند. در فرگرد 14 از وندیداد در فقره 9 پنام در جزو اسلحه و لوازم یک مرد جنگی شمرده شده است. گذشته از این چند فقرات 
22:پنام در اوستا و کتب پهلوی عبارت است از دو قطعه پارچه سفید از جنس پنبه که به روی دهان آویخته با دو نوار بپشت سر گره میزنند. زرتشتیان ایران آن را روبند نامند. این پرده کوچک که بنا به توضیحات تفسیر پهلوی اوستا باید دو بند انگشت پائین تر ازدهان باشد در وقتی
```


## [2026-09-05T18:37:08.795Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls incoming/WLD/; python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find leaf containing 'dhē-' style header near 826\nfor i,p in enumerate(pages):\n    if 'gao-' in p and ('Milchgef' in p or 'dhana' in p):\n        print('LEAF',i,p[:200].replace('\\n',' '))\nEOF",
 "description": "Look for Walde-Pokorny dhe entry"
}
```


### [2026-09-05T18:37:10.461Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 895
LEAF 836 828                                                             dhe-     Ai. dhatar- „Anstifter, Gr under", dhatar- „Schopfer" (vgl. auch oksl. detch „Tat"), gr. der go, lat. con-ditor.   Ygl. *dh 9-t
```


## [2026-09-05T18:37:13.238Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[836]\nprint(p[:3000])\nEOF",
 "description": "Walde-Pokorny p.828"
}
```


### [2026-09-05T18:37:14.953Z] TOOL RESULT

```
828                                                             dhe-


  Ai. dhatar- „Anstifter, Gr under", dhatar- „Schopfer" (vgl. auch oksl.
detch „Tat"), gr. der go, lat. con-ditor.
  Ygl. *dh 9-tlo- iu (Fick II 4 40), air. dal, aeymr. dutl, neymr. dadl, abret.
                                                       1



dad! „V ersammlung", nbret. dael contestation, querelle" (vgl. zur Bed.
phryg. doi\uog; nicht nach Pedersen KG. I 135 zu *da(i)- „teilen");
  ai. dhiti-h „das Stellen", devd-hiti-h „Gottersatzung“, gr. beoig „Satzung,

Ordnung";                av. ni-daiti-          f.    „das Niederlegen, Ablegen, Verbergen", got.
gadeds „Tat, Lage",                     dad „Tiichtigkeit, Tat", ags. deed, ahd. tat „Tat",
                                        aisl.

lit.    d'et is        „Last", pi. detys „Lege des Huhns, der Gans", aksl. blago-dets
,;   ydgig,   Gnade, Dank".
                           el. awdyvat „Yertrag“, ahd. Ptc. gitan, ags. don
       Ai. dhana-m ,,Behalter",
,.getan“,     o-dem „(umgetan) bekleidet"; ai. dhdna-m „Einsatz, Preis
                       aksl.
im Wettkampf usw.“, nidhdnam „das Sichfestsetzen, Aufenthalt usw.“, go-
dhana-m ,,Rinderbesitz“, av. gao-dana- n. „HilchgefaB“.
  Ai. dhaman- n. „Satzung, Gesetz, Wohnstatteschar usw.“, av. daman-,
daman- n. „Statte, Wohnstatte; Geschopf", gr. dvabyga „das Aufgestellte,
Weihgesehenk", Inldgya „das Daraufgestellte odor -gesetzte Deckel Bild-                         :
                                                                                                            ;


siiuleauf einem Grabe", dyfunv m. „Haufe"; ev&ypcov „wohl in Ordnung
haltend"; &efia n. „liinterlegtes Geld, aufgestellte Behauptung, Satz; Stamm-
form (Gramm)", vgl. auch Inf. {ieyevai av. dami- f. „Schopfung“, Adj.    ;


(auch         fern.)       „schaffend, Schopfer";                    gr. deyag,   gen. ursprgl. dejuwzog „die
 fest  und unverbriichlich stehende" als Gottinname, dann „Recht, Gesetz,
 Sitte, Brauch" (nach Frankel Gl. 4, 22 ff. de/ni-, Zsform von &e/uegog in
 beuegy fiefiata [oe/ur>], in welcher Bed. zu *dhem- „stieben“] evara&rjg lies,
                  •




 und Wznomen ora- „stehend ‘); be/uovg' Siadeoeig Hes., vija be/ua>ae „(der
 Wind) trieb das Schiff ans Land", dijuebXa PI. „die Grundlagen eines Ge-
 baudes das tiefste, innerste", btuehoi U&oi „die Grundsteine", hom. b tael-
               ;



 ha (ei metr. Dehnung) „Grundlage, Grund"; da/id „in Haufen, scharen-
 weise;               haufig,   oft",     da/uiva          „haufig,    oft",   da/ihg,   dajueiai   PI.   „gehauft,
 haufig,              dicht gedrangt",               bduvog „Dickicht, Gebiisch, Strauch";                (so   auch
 aisl. dammr, nhd. Dumml s. u. *dheb- „dick“); aut ein *dhd-mo- „Nieder-
 lassung, Wohnstatte" (vgl. baipog     olxla, oeiogog, cpvTela lies., auch ai.
                                                                 *



 dhaman- „ Wohnstatte") oder „Haufe, Schar (der Diener)"
```


## [2026-09-05T18:37:27.739Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for w in \"537\" \"533\" \"568\" \"1057\" \"1058\"; do echo \"--- HUB entry $w\"; grep -n -A4 \"^ *$w\\. \" HUB.txt | head -12; done",
 "description": "Hübschmann entries by Horn numbers"
}
```


### [2026-09-05T18:37:29.774Z] TOOL RESULT

```
--- HUB entry 537
--- HUB entry 533
--- HUB entry 568
--- HUB entry 1057
3642:1057. Pr. niham aus *nihiham, vgl. pr. diham von dddan,
3643-Dazu np. nihdd *fundaraentum, natura, indoles', vgl.
3644-unser *Anlage',
3645-Hierher nach Salem ann: np. nahar = nahOr^
3646-naxdra (afgh. LW. niharai 'breakfast*) 'Fasten, Friih-
--- HUB entry 1058
```


## [2026-09-05T18:37:34.974Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"däwer\\|dätöbara\\|dätö\\.bara\\|dästän\\|destur\\|dastür\" HUB.txt | head -12; echo '--- dan Behälter'; grep -n \"Behälter\\|dän \" HUB.txt | head -10",
 "description": "Hübschmann relevant words"
}
```


### [2026-09-05T18:37:35.042Z] TOOL RESULT

```
--- dan Behälter
```


## [2026-09-05T18:37:41.230Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor w in ['اندام','داور','نهادن','دستور','داستان']:\n    hits=[i for i,p in enumerate(pages) if w in p]\n    print(w, hits[:6])\nEOF",
 "description": "Aryanpur cross-check"
}
```


### [2026-09-05T18:37:42.995Z] TOOL RESULT

```
اندام [94]
داور [38, 299]
نهادن [47]
دستور [7, 19, 20, 22, 28, 40]
داستان [14, 16, 19, 35, 39, 47]
```


## [2026-09-05T18:37:46.795Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; python3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,w in [(94,'اندام'),(299,'داور'),(47,'نهادن')]:\n    p=pages[i]\n    m=re.search(w,p)\n    print('=== leaf',i,'printed',i+1,'|',w)\n    print(p[max(0,m.start()-400):m.start()+500].replace('\\n',' '))\n    print()\nEOF",
 "description": "Read Aryanpur entries"
}
```


### [2026-09-05T18:37:48.494Z] TOOL RESULT

```
=== leaf 94 printed 95 | اندام
[pdf page 95] ۶ ۲ اووی :  یادداشت:  معنی این واژه در زبان‌های ژرمنی: قوزکه» مچ‌پا.  معنی این واژه در سانسکریت: اندام» عضو پدن. : ۱  معنی اين واژه در زبان‌های ارمنی و یرنانی و رومانس؛ گوشه) خمی. ۱ ۱ وی اوستایی (4587400): ۸7 ۸۷۸۶ اسلاوی کهن (ع4۷1آ5 2711001 2ا0):  پارسی باستان (/۶8۸۹14۸ 11۸17۷:)012 ,۸۷۸ ۸ 0۷3 پهلوی (2۸(1۲1): 09,30 08 ب۸۷۳ لهستانی (۳0.187): 0۸ ,0 ارستی (0897/6): 1 چکک ((220). ۸ ,00 کردی (00157): اند صربی (/55814): 0۵۷۸7 افغانی (پشتر) (/7ل۸لا0 ۸7): 2 ,1۸ اسلواکی 5]07۸0): ۸ ,(0 تخاری 4 (۸ [(۸ل7ل707)+ 01  تخاری 8 (8 [(۸ل7077۸): 1 پسگشت‌ها 5 سانسکریت (8۸(/88207): ۸۸ 4 ۶005  ارمنی (۸/۵(/82/744): 

=== leaf 299 printed 300 | داور
[pdf page 300] رای (به چم *تدبیر و داوری و مقتضای عقل") / ۳۰۱ آوستایی (/45374): پیگشت‌ها ‏ 35 ال 8۸ 823 زا 1 رس پهلوی (477آل۸7): (82۷)03۸۷0 0 (81) :۸402/2/5 کردی (070/54). 8۸ 2237102 ال ل482ل۸ 75 سانکریت (5۸۸/5/7): ,18۷۸/۷۲ لش زک 52/0 7628 0۶۳ 0167/0 5 ,م3۸ ,8۸۷1۷۸۷۲ 4 (85) :ها لانین (7107): 8 ,855 3 (0110) 0/0 برهان قاطع + ۹۳ یادداشت, ۱- واژه‌ی ,33۸ در زبان‌های انگلیسی و فرانسه نیز از این واجریشه‌است: 891 (7:)8۸7 ۰8۸80۷13۸1۹ ۲- چم این واژه دز زبان‌های ایرانی یشین: چیزدار؛ دارا, چم این واژه در زبان لاتین: چیز شیلی» دارائی. اوستای

=== leaf 47 printed 48 | نهادن
[pdf page 48] دیباچه / ۴۹ بررسی قرار داد. این گوئه توضیحات که معمولاً همراه با یک داستان ارائه می‌شوند جالب‌اند ولی افسوس که درست نیستند! مثلاً گفته می‌شود که وجه تسمیه «تبریز» این است که در آنجا شاهزاده‌ای که سخت بیمار برد خوب شد و تب او «ریختء و لذا نام شهر را «تبریز» نهادند! باید پرسید قبل از این رویداد نام تبریز چه پود؟ امید برای پژوهشهای آینده :  همانطور که در بالاگفته شد» این کتاب عبارت است از گامی نخستین در راه یافتن همه‌ی واجریشه‌های هند و اروپایی زبان فارسی.گام‌های نختین معمولاً خالی از کاستی و لغزش نیستند. امید من این است که پژوهشگران دیگر به تدریج کاستی‌ها را برطرف کرده و فرهنگه‌های کاملتری از ریشه‌های هند و اروپایی زبان فارسی ارائه دهند. هنوز صدها واژه‌ی ناب فارسی وجود دارند که یافتن واجریشه‌ی هند و اروپایی آنها به  بن‌بست برخورده است. برای مثال به
```


## [2026-09-05T18:37:59.357Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nfor l in open('data/verification/sources/web/index.jsonl'):\n    d=json.loads(l)\n    if 'page 124' in d.get('note','') or 'pdf 124' in d.get('note','') or 'pdf page 124' in d.get('note',''):\n        print(d['status'], d['url'])\n\"; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg124.png data/verification/sources/refs/ocr/BOOK/124.png && echo copied",
 "description": "List archived URLs and copy page image"
}
```


### [2026-09-05T18:38:01.104Z] TOOL RESULT

```
200 https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%A7%D9%85
200 https://en.wiktionary.org/wiki/%D8%AF%D8%B3%D8%AA%D9%88%D8%B1
200 https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86
200 https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%88%D8%B1
200 https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D8%AF%D9%86
200 https://en.wiktionary.org/wiki/Ahura_Mazda
200 https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D9%86
200 https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D9%86
-1 https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%A7%D9%85
200 https://en.wiktionary.org/wiki/apadana
200 https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%AF
200 https://en.wiktionary.org/wiki/%D9%BE%D9%86%D9%87%D8%A7%D9%86
-1 https://www.iranicaonline.org/articles/dastur
200 https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%A7%D9%85/
200 https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A7%D9%85/
copied
```


## [2026-09-05T18:38:06.059Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; head -5 data/verification/sources/web/5f46c64056f8ef06.txt; grep -n \"Root\\|to put, to place\\|dʰeh₁\" data/verification/sources/web/5f46c64056f8ef06.txt | head -8",
 "description": "Check PIE dheh1 fetch"
}
```


### [2026-09-05T18:38:06.110Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-
FETCHED: 2026-09-05T18:27:50Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/dʰeh₁- - Wiktionary, the free dictionary

4:TITLE: Reconstruction:Proto-Indo-European/dʰeh₁- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/dʰeh₁- - Wiktionary, the free dictionary 
62: Root 
78: Reconstruction:Proto-Indo-European/ dʰeh₁- 
135: See also: Reconstruction:Proto-Indo-European/dʰeh₁(y)- 
142: Root
145: *dʰeh₁- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 
154: Terms derived from the Proto-Indo-European root *dʰeh₁- (200 c, 0 e)
```


## [2026-09-05T18:38:08.554Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '142,160p' data/verification/sources/web/5f46c64056f8ef06.txt",
 "description": "PIE dheh1 root gloss"
}
```


### [2026-09-05T18:38:08.595Z] TOOL RESULT

```
 Root
 [ edit ] 

 *dʰeh₁- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to do 

 to put , place 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *dʰeh₁- (200 c, 0 e) 

 *dʰéh₁-t ~ *dʰh₁ént ( athematic root aorist ) [ 1 ] 

 *dʰé-dʰoh₁-ti ( athematic reduplicated present ) [ 1 ] 

 *dʰéh₁-lo-m [ 4 ]
```


## [2026-09-05T18:40:10.457Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:50:51.965Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk124.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nSRC = {\n \"pie\": W+\"Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-\",\n \"andam\": W+\"%D8%A7%D9%86%D8%AF%D8%A7%D9%85\",\n \"dastur\": W+\"%D8%AF%D8%B3%D8%AA%D9%88%D8%B1\",\n \"dastan\": W+\"%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86\",\n \"davar\": W+\"%D8%AF%D8%A7%D9%88%D8%B1\",\n \"nahadan\": W+\"%D9%86%D9%87%D8%A7%D8%AF%D9%86\",\n \"ahura\": W+\"Ahura_Mazda\",\n \"dan\": W+\"%D8%AF%D8%A7%D9%86\",\n \"nahan\": W+\"%D9%86%D9%87%D8%A7%D9%86\",\n \"apadana\": W+\"apadana\",\n \"dad\": W+\"%D8%AF%D8%A7%D8%AF\",\n \"penhan\": W+\"%D9%BE%D9%86%D9%87%D8%A7%D9%86\",\n \"ab_andam\": \"https://abadis.ir/fatofa/%D8%A7%D9%86%D8%AF%D8%A7%D9%85/\",\n \"ab_panam\": \"https://abadis.ir/fatofa/%D9%BE%D9%86%D8%A7%D9%85/\",\n}\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"ma[n]dz-dha; ahura-mazdha\", \"verdict\": \"confirmed\",\n \"derivation\": \"The Avestan words are mazdā- / mazdah- n. 'memory, wisdom' and the divine name ahura- mazdā- 'Lord Wisdom' (Ahura Mazda). The second member really is this root: the compound is Proto-Indo-Iranian *mns-dʰeh₁- 'to set (something) in mind, commit to memory', i.e. *men- 'think' + *dʰeh₁- 'put'; Pokorny treats it under mendʰ- (Page(s): 730): 'Avestan mazda, mazdah- n. „Gedächtnis“, mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'. Nourai's odd transliteration 'ma[n]dz-dha / ahura-mazdha' is copied letter for letter from Klein s.v. Ormazd ('ma(n)dzdha-, ‘wise’, which is a compound formed from the I.-E. bases *men-dh- and *dhe- ‘to put, place’'); the actually attested Avestan spelling is mazdā-, so the -dh- here is Klein's etymologising respelling, not an Avestan form. The gloss 'done learning, wise' and the cross-reference to Men 1 are both correct.\",\n \"derivation_fa\": \"واژهٔ اوستایی mazdā- / mazdah- به معنی «خرد، یاد» و نام ایزدی ahura-mazdā- «سرورِ خرد» از ترکیب هندوایرانی آغازین *mns-dʰeh₁- «در یاد نهادن» ساخته شده است؛ یعنی ستاک *men- «اندیشیدن» به علاوهٔ همین ریشهٔ *dʰeh₁- «نهادن». پوکورنی این واژه را در صفحهٔ ۷۳۰ ذیل mendʰ- آورده (نه در صفحهٔ ۲۳۵ که نورایی ارجاع داده). املای غریبِ «ma[n]dz-dha» عیناً از کلاین (ذیل Ormazd) گرفته شده و صورت اوستایی واقعی mazdā- است. در مجموع ادعای نورایی درست است.\",\n \"sources\": [SRC[\"ahura\"], SRC[\"pie\"]],\n \"ref_check\": [{\"ref\": \"POK:235\", \"status\": \"partial\", \"note\": \"POK_full.txt lines 22276-22510: the lemma at 'Page(s): 235-239' is 'dʰe-2, Meaning: to put, place, say' and it does NOT mention mazdā anywhere. Pokorny discusses mazdā s.v. mendh- at 'Page(s): 730' (line 59307: 'Avestan mazda, mazdah- n. \\\"Gedächtnis\\\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'). The -dhā element is this root, so the claim holds, but the cited page is the wrong one.\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"p.730 s.v. mendh- (POK_full.txt line 59307)\", \"stance\": \"supports\", \"note\": \"'Avestan mazda, mazdah- n. \\\"Gedächtnis\\\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)' — the compound of *men-dh- + *dhē-.\"},\n  {\"src\": \"KLN\", \"where\": \"p.1096 s.v. Ormazd (KLN_1966.txt leaf 586)\", \"stance\": \"supports\", \"note\": \"'fr. Avestic Ahuramazda, lit. \\\"wise lord\\\", a compound of ahura- ... and ma(n)dzdha-, \\\"wise\\\", which is a compound formed from the I.-E. bases *men-dh- ... and *dhe-, \\\"to put, place\\\"' — Nourai's spelling and analysis come from here.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, passim (e.g. BRT.txt line 10715)\", \"stance\": \"supports\", \"note\": \"OCR of the headword column is unreadable, but the god's name is spelt mazdā / mazdå throughout the quoted Gāthā passages ('ahurō mazdā', 'tat mazdā tava'), never *mazdha — confirming that Nourai's '-dha' is an etymological respelling.\"}]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"Mazdâ «مزدا»; Ahûrâmazdâ «اهورا مزدا»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Modern Persian مزدا and اهورامزدا do continue the Avestan words, but not by unbroken sound change: the inherited line is Av. ahura- mazdā- > OP Auramazdā > MP Ōhrmazd/Ohrmazd > NP هرمز/اورمزد (Klein s.v. Ormazd: 'Pers., fr. OPers. Auramazda, fr. Avestic Ahuramazda'). The forms مزدا and اهورامزدا with their Avestan shape are learned reintroductions made by Parsi and Iranian scholarship in the 19th-20th centuries from the Avesta itself (the same route by which English Ahura Mazda is 'a transliteration of Avestan ahura mazdā'). So the arrow Avestan → Persian is right in substance, with the qualification that it is book transmission rather than inheritance.\",\n \"derivation_fa\": \"«مزدا» و «اهورامزدا» در فارسی نو بازگرداندهٔ مستقیمِ صورت اوستایی است و نه دنبالهٔ آوایی آن. زنجیرهٔ موروثی چنین است: اوستایی ahura-mazdā- ← پارسی باستان Auramazdā ← فارسی میانه Ōhrmazd ← فارسی نو «هرمز/اورمزد». اما صورتِ «اهورامزدا» از سدهٔ سیزدهم/چهاردهم هجری و از راهِ پژوهشِ اوستاشناسان دوباره وارد فارسی شده است. پس پیکان نورایی درست است، با این یادآوری که این وام‌گیری عالمانه است نه تحول آوایی پیوسته.\",\n \"sources\": [SRC[\"ahura\"]],\n \"ref_check\": [{\"ref\": \"KLN:1095\", \"status\": \"supports\", \"note\": \"Klein 1966-67 s.v. Ormazd: 'Pers., fr. OPers. Auramazda, fr. Avestic Ahuramazda, lit. \\\"wise lord\\\"'. In the archive scan the entry sits on leaf 586, and the calibration leaf 582 = printed pp.1088/1089 puts it on pp.1096-97, i.e. one page past Nourai's 1095 — same entry, page number off by about one.\"}],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"p.1096 s.v. Ormazd; p.42 s.v. ahura ('Ahura-Mazda, n. — See Ormazd')\", \"stance\": \"supports\", \"note\": \"Klein routes Persian Ormazd through Old Persian Auramazda from Avestan Ahuramazda.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. Ahura Mazda\", \"stance\": \"supports\", \"note\": \"'Transliteration of Avestan ahura mazdā. Doublet of Aramazd and Hormuz' — i.e. the modern form is a transliteration, the inherited doublet is Hormuz.\"},\n  {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, passim\", \"stance\": \"supports\", \"note\": \"the Avestan source form is ahurō mazdā in the quoted passages.\"}]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan\", \"words\": \"dâman 2; han-dâma; paiti-dâma\", \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Two of the three words are right, the third is a misprint. (a) Av. dāman-/dąman- n. is real and belongs to this root, but it means 'place, dwelling; creation, creature' — Walde-Pokorny I 828 'av. dāman-, dąman- n. \\\"Stätte, Wohnstätte; Geschöpf\\\"'; the gloss 'statute' that Nourai gives is the gloss of the Old Indic cognate dhāman- '‚Satzung, Gesetz‘'. (b) Av. haṇdāma- 'limb, member' is correct and is exactly ham- 'together' + dāman-, i.e. PIE *sem- + *dʰeh₁- + *-mn̥ (Wiktionary s.v. اندام); it is attested Yt.14.56 'vīspa haṇdāma rāzayaṇti' ‘they wrench all the limbs’ (Bartholomae). (c) 'paiti-dāma' is wrong: the Avestan mouth-veil is paiti.dāna- n., with -n-, attested V.18.1 'paiti.dānəm ainim baraiti' and Yt.5.133 'saraŋaitīm paiti.dānəm ... drazimnō' (Bartholomae); Horn no.332 writes 'parsisch penām (penōm), aw. paiti.dāna-, phlv. padām'; and Mo'in's own footnote in Borhān p.418, which Nourai cites here, reads «در اوستا پئیتی‌دان و در پهلوی پدام». The printed page 124 of the book itself shows 'paiti-dâma', so this is Nourai's own misprint (assimilated to the han-dâma above it), not a scanning error; the word is a paiti- 'against, in front of' compound of dāna- (node #8), not of dāman-.\",\n \"derivation_fa\": \"از سه واژهٔ این خانه دو تا درست است و یکی غلطِ چاپی. اوستایی dāman-/dąman- هست، اما معنای آن «جای، جایگاه؛ آفریده» است (والده‐پوکورنی، جلد ۱ ص ۸۲۸)؛ معنای «قانون» که نورایی آورده معنای هم‌ریشهٔ سنسکریتِ dhāman- است. اوستایی haṇdāma- «اندام، عضو» درست است و از ham- «با هم» و dāman- ساخته شده. ولی «paiti-dāma» نادرست است؛ صورت درست paiti.dāna- است — همان که معین در حاشیهٔ برهان قاطع (ص ۴۱۸) «پئیتی‌دان» نوشته و هرن هم در شمارهٔ ۳۳۲ همین را آورده است. تصویر صفحهٔ چاپی کتاب نشان می‌دهد که خودِ کتاب «paiti-dâma» چاپ کرده؛ پس خطا از مؤلف است نه از خوانش اسکن.\",\n \"error_in\": \"book\",\n \"book_prints\": \"paiti-dâma : protection for body\",\n \"correct_form\": \"paiti.dāna- (Av.), Pahl. padām, NP panām\",\n \"sources\": [SRC[\"andam\"], SRC[\"ab_panam\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:169\", \"status\": \"supports\", \"note\": \"Borhān-e Qāte‘ vol.1, leaf 387 of BQT_v1_pages.txt (running head '۱۶۹') carries the headword «اندام - بروزن انجام، معروف است که بدن و عضو آدمی باشد»; Mo'in's etymological footnote on that page is not legible in this OCR.\"},\n  {\"ref\": \"BQT:418\", \"status\": \"supports\", \"note\": \"vol.1 leaf 644 = p.418, the «پنام» entry; Mo'in's long footnote there reads «در اوستا paiti-dāna ... در وندیداد بند ۹ پنام جزو اسلحه و لوازم یک مرد جنگی بشمار آمده ... دو قطعه پارچهٔ سفید که بروی دهان آویخته», and it prints the Avestan with -n-, contradicting Nourai's 'paiti-dâma'. Same page carries the Shahīd Balkhī couplet the chart quotes.\"},\n  {\"ref\": \"POK:238\", \"status\": \"supports\", \"note\": \"POK_full.txt (dhe-2, pp.235-239): 'Old Indie dhaman- n. \\\"statute, law, dwelling ...\\\", Avestan daman-, dąman- n. \\\"site, creature\\\"' — both the Indic 'statute' gloss Nourai used and the Avestan word.\"}],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I p.828 s.v. dhe-\", \"stance\": \"supports\", \"note\": \"'Ai. dhāman- n. „Satzung, Gesetz, Wohnstätte...“, av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“' — the 'statute' sense is Indic, the Avestan sense is 'place, creature'.\"},\n  {\"src\": \"BRT\", \"where\": \"BRT.txt lines 19642 and 25224 (Yt.14.56), line 12768 (V.18.1), line 14057 (Yt.5.133)\", \"stance\": \"partial\", \"note\": \"confirms haṇdāma 'Glied' ('vīspa handāma rāzayānti', 'alle Glieder ... verrenken') and paiti.dānəm with -n- ('paiti.dānəm *ainim baraiti'); no *paiti.dāma exists.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 332, p.75 area\", \"stance\": \"contradicts\", \"note\": \"'mit parsisch penām (penōm), aw. paiti.dāna-, phlv. padām' — Avestan -dāna-, not -dāma-.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. اندام\", \"stance\": \"supports\", \"note\": \"'Avestan haṇdāma (\\\"limb\\\") ... Ultimately from Proto-Indo-European *sem- (\\\"together\\\") + *dʰeh₁- (\\\"to put\\\") + *-mn̥.'\"}]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"handâm; pa-dâm, panum\", \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary has both: 'handām [hndʾam | = P(arthian), N andām] member, limb' and 'padām [pdʾam | (N panām)] mask for the mouth, worn by a celebrating priest'. Pahl. handām is the regular continuation of Av. haṇdāma-, and Pahl. padām of Av. paiti.dāna- (paiti- > MP pad- with the usual reduction of paiti to pad, and -āna- > -ām by the same nasal shift that gives the variants Dehkhoda records: «در پهلوی پدام و پندام و پنوم گویند»). Nourai's second form 'panum' is the Parsi ritual term penōm/panūm (Horn no.332: 'parsisch penām (penōm)'), still the name of the cloth mouth-veil the mōbad wears before the fire so that his breath does not defile it. Nourai's gloss 'figure' for handām is loose; the Pahlavi word means 'limb, member' — the sense 'figure, physique' is a later Persian development.\",\n \"derivation_fa\": \"مکنزی هر دو واژه را دارد: handām «عضو، اندام» و padām «نقاب دهان که موبد هنگام آیین می‌بندد». handām دنبالهٔ مستقیمِ اوستایی haṇdāma- است و padām از اوستایی paiti.dāna-: پیشوند paiti- در فارسی میانه به pad- کوتاه شده و پایانهٔ -āna به -ām بدل گشته (دهخدا: «در پهلوی پدام و پندام و پنوم گویند»). «panum» همان penōm پارسیان هند است. ادعای نورایی درست است؛ تنها معنای «figure» برای handām سهل‌انگارانه است؛ معنای پهلوی آن «عضو» است.\",\n \"sources\": [SRC[\"ab_panam\"], SRC[\"andam\"]],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no refs= in the book; verification rests on MacKenzie, Horn and Dehkhoda/Mo'in instead.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"s.v. handām (p.43 area) and s.v. padām (p.65 area)\", \"stance\": \"supports\", \"note\": \"'handām [hndʾam | = P, N andām] member, limb'; 'padām [pdʾam | (N panām)] mask for the mouth, worn by a celebrating priest'.\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary), leaves 61-72\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary is restricted to the texts he edits and has neither handām nor padām.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 332\", \"stance\": \"supports\", \"note\": \"'mit parsisch penām (penōm), aw. paiti.dāna-, phlv. padām' — the exact chain for Nourai's 'pa-dâm, panum'.\"}]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"andâm «اندام»; panâm «پنام»; panâmîdan «پنامیدن»\", \"verdict\": \"confirmed\",\n \"derivation\": \"اندام < MP handām with the regular New Persian loss of initial h- before a vowel (cf. MP handarz > NP andarz, MP hangōsag > NP angōsa); the word therefore goes back to Av. haṇdāma- 'limb' and, through it, to *sem- + *dʰeh₁-. پنام < MP padām, with -d- assimilated to the following nasal (padām > pandām > panām; Dehkhoda records all three Pahlavi variants پدام/پندام/پنوم). Borhān's پنام entry (p.418) glosses it as an amulet against the evil eye and quotes exactly the couplet the chart prints («بتا نگارا از چشم بد بترس همی ...»), on which Mo'in comments «ازین بیت پیداست که مراد همان روبند است نه تعویذ» — i.e. the veil, not the amulet, so Nourai's gloss 'a protective mouthpiece' follows Mo'in rather than Borhān's text. پنامیدن 'to shield, prevent' is a denominal verb built on پنام with the ordinary infinitive suffix -īdan; it is a dictionary word rather than one attested in the classical poets.\",\n \"derivation_fa\": \"«اندام» از فارسی میانهٔ handām است؛ هٔ آغازین در فارسی نو افتاده است — همان‌گونه که handarz به «اندرز» بدل شد. «پنام» از پهلوی padām است که دالِ آن به نون بدل شده (padām > pandām > panām؛ دهخدا هر سه صورت را آورده). برهان قاطع (ص ۴۱۸) همین بیتِ شهید بلخی را که در نمودار آمده شاهد آورده است و معین در حاشیه تاکید کرده که مقصود همان روبند است. «پنامیدن» فعلی است ساخته از همین اسم و بیشتر فرهنگ‌نامه‌ای است. ادعای نورایی درست است.\",\n \"sources\": [SRC[\"andam\"], SRC[\"ab_andam\"], SRC[\"ab_panam\"]],\n \"ref_check\": [{\"ref\": \"MON:813\", \"status\": \"not_checked\", \"note\": \"Mo'in's Farhang-e Fārsi is on disk only as unpaginated OCR (MON_part1/2.txt) and the online copies (vajehyab, abadis) reproduce the entry text without page numbers, so p.813 cannot be located. The substance is confirmed from Dehkhoda's entries for اندام and پنام on abadis and from Mo'in's own footnote in Borhān p.418.\"}],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol.1 p.418 s.v. پنام (leaf 644)\", \"stance\": \"supports\", \"note\": \"the headword, the Shahīd Balkhī couplet, and Mo'in's footnote deriving it from Av. paiti-dāna / Pahl. padām.\"},\n  {\"src\": \"PHD\", \"where\": \"s.v. handām, padām\", \"stance\": \"supports\", \"note\": \"MacKenzie gives the New Persian outcomes himself: 'N andām', '(N panām)'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 332\", \"stance\": \"supports\", \"note\": \"distinguishes np. penām 'verborgen' (contracted from penhān) from the ritual penām < phlv. padām — the chart's panām is the latter.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. اندام\", \"stance\": \"supports\", \"note\": \"'Akin to Middle Persian hndʾam (handām, \\\"member, limb\\\") ... Avestan haṇdāma (\\\"limb\\\")'.\"}]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Avestan\", \"words\": \"dâta 1, dâ 1; ni-dâ; upa-ni-dâ; apa-dâna\", \"verdict\": \"plausible\",\n \"derivation\": \"The core is right, two details are not. Av. dā- 'to put, set' and its participle dāta- are exactly Pokorny's material for this root ('with full grade Avestan Old pers. dāta-', POK 235). Av. ni-dā- 'to lay down, put away, hide' is likewise attested — Walde-Pokorny I 828 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“' — and gives NP nihādan/nihān (node #7). But (a) 'upa-ni-dā : hidden', which is meant to yield NP پنهان, is doubtful: Horn no.332 analyses penhān/pinhān as 'phlv. pa(t) nihān', i.e. the preposition pad + nihān, and Wiktionary follows him ('originally a contraction of ... به + نهان, i.e. \\\"in hiding\\\"'), so no upa- prefix is involved. (b) apa-dāna- is OLD PERSIAN, not Avestan: it occurs only in the Achaemenid inscriptions (A²Sa 3-4, A²Ha 5 'imam apadāna ... akunam'), and Kent's Lexicon reads 'apadāna- sb. \\\"palace\\\": from apa- + dāna- to root *dā-, cf. Skt. apadhā- \\\"concealment\\\", Gk. ἀποθήκη \\\"storehouse\\\"'. The word means 'palace, columned audience hall'; Nourai's gloss 'the concealed part of a palace' is built on Kent's Sanskrit comparison rather than on the Old Persian usage.\",\n \"derivation_fa\": \"هستهٔ این خانه درست است: اوستایی dā- «نهادن» و صفت مفعولی dāta- همان مادهٔ پوکورنی در ص ۲۳۵ است، و ni-dā- «فرونهادن، پنهان کردن» نیز (والده‐پوکورنی ۱: ۸۲۸ ni-δaiti-). اما دو نکته جای چون و چرا دارد: یکم اینکه «پنهان» را هرن (شمارهٔ ۳۳۲) از pad + nihān گرفته و نه از پیشوند upa-؛ دوم اینکه apadāna واژه‌ای پارسی باستان است نه اوستایی (کنت، واژه‌نامه ص ۱۶۷–۱۶۸) و معنای آن «کاخ، تالار بار» است؛ معنای «بخش نهانِ کاخ» برگرفته از مقایسهٔ کنت با سنسکریت apadhā- است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC[\"apadana\"], SRC[\"penhan\"], SRC[\"nahadan\"], SRC[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:235\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: dʰe-2, Meaning: to put, place, say ... with full grade Avestan Old pers. data-'; 'Page(s): 235-239'.\"},\n  {\"ref\": \"HRN:236\", \"status\": \"supports\", \"note\": \"Horn p.236 (leaf 257), no.1057 'nihāden „hinlegen, hinsetzen“ ... aw. ni + √dā- (nidadāt)' and no.1058 'nihān „verborgen, heimlich“. ap. *nidāna- „etwas (heimlich) hingelegtes“'.\"},\n  {\"ref\": \"KNT:168\", \"status\": \"supports\", \"note\": \"Kent's Lexicon (KNT.txt line 4999, leaf 190 ≈ printed p.167-168): 'apadāna- sb. „palace“: from apa- + dāna- (§147.I) to root *dā-, cf. Skt. apadhā- „concealment“, Gk. ἀποθήκη „storehouse“'. Note that Kent files it as Old Persian, not Avestan.\"},\n  {\"ref\": \"FFD:52\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'lhā-ye Fārsi-ye Dari p.52 (pdf 57) s.v. دادن: «در ایرانی باستان دو ریشهٔ dā وجود داشته است: ۱- به معنی دادن، ۲- به معنی نهادن. نهادن از dā به معنی نهادن آمده» — exactly the 'dā 1' of this node.\"}],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I p.828\", \"stance\": \"supports\", \"note\": \"'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“' — the 'put down, also hide' sense the chart gives.\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.vv. apadāna-, dāta-, dāna-\", \"stance\": \"partial\", \"note\": \"supports the derivation but classes apadāna- as Old Persian; also 'dāta- sb. „law“: Av. dāta-, NPers. dād; nt. ptc. to *dā-'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 332\", \"stance\": \"contradicts\", \"note\": \"for پنهان Horn gives 'phlv. pa(t) nihān (s. No. 1058)', not an upa-ni-dā- compound.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. apadana, s.v. پنهان\", \"stance\": \"partial\", \"note\": \"'apadana — From Old Persian apadāna'; 'پنهان — From Middle Persian pad + nihān'.\"}]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"nahâdan «نهادن»; nahân «نهان»; âpâdânâ «آپادانا»\", \"verdict\": \"confirmed\",\n \"derivation\": \"نهادن (nihādan; Nourai's Dari-style nahâdan) continues MP nihādan, present nih- (MacKenzie: 'nihādan, nih- [TNH TWN-tnʹ < A hnht | M nyd, nyh-, N ~] put, place, establish'), from Old Iranian *ni-dā- (Horn no.1057; Hübschmann no.1057 'pr. niham aus *nihiham, vgl. pr. diham von dādan. Dazu np. nihād \\\"fundamentum, natura, indoles\\\"'). The chart's gloss 'to do' is a slip: the verb means 'to put, place'. نهان continues MP nihān 'concealment, secrecy' from OP *nidāna- 'something laid down (out of sight)' (Horn no.1058); the chart's extra پنهان is pad + nihān. Mo'in's footnote in Borhān vol.4 p.2211 s.v. نهاد gives the same chain («پهلوی nihātan ... ایرانی باستان *ni-dā- ... اوستا dā», citing Bartholomae and Horn). آپادانا, by contrast, is a twentieth-century learned re-borrowing of Old Persian apadāna- through European Achaemenid scholarship, used as the name of the columned halls at Persepolis and Susa; it is not an inherited Persian word, so the chart's arrow is right only in the sense of a scholarly revival.\",\n \"derivation_fa\": \"«نهادن» از فارسی میانهٔ nihādan (مادهٔ مضارع nih-) است، و آن از ایرانی باستان *ni-dā- «فرونهادن» می‌آید (هرن شمارهٔ ۱۰۵۷؛ مکنزی). معنایی که کتاب داده («to do») لغزشی است؛ معنا «نهادن، قرار دادن» است. «نهان» از فارسی میانهٔ nihān و پارسی باستان *nidāna- «آنچه پنهان نهاده شده» است (هرن ۱۰۵۸)، و «پنهان» ترکیب pad+nihān است. ولی «آپادانا» واژه‌ای موروثی نیست؛ وام‌گیری عالمانهٔ سدهٔ چهاردهم هجری از پارسی باستان apadāna- است. در مجموع ادعای نورایی درست است.\",\n \"sources\": [SRC[\"nahadan\"], SRC[\"nahan\"], SRC[\"penhan\"], SRC[\"apadana\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:2211\", \"status\": \"supports\", \"note\": \"Borhān vol.4, pdf page 294 = printed 2211 (offset printed = pdf+1917): headword «نهاد ... ماضی نهادن است که بمعنی گذاشتن باشد» with Mo'in's footnote «پهلوی nihātan ... ایرانی باستان *ni-dā- ... اوستا dāح بارتولمه ... هرن».\"},\n  {\"ref\": \"BQT:2214\", \"status\": \"supports\", \"note\": \"Borhān vol.4, pdf 297 = printed 2214: the نهان block (نهان‌پیکران، نهان‌خانه، نهان‌دره); the simple headword نهان falls in the same two-column spread.\"}],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"p.236, nos. 1057-1058\", \"stance\": \"supports\", \"note\": \"'nihāden ... aw. ni + √dā- (nidadāt) „hinsetzen“; phlv. n(i)hatan'; 'nihān „verborgen“ ... ap. *nidāna-'.\"},\n  {\"src\": \"HUB\", \"where\": \"no. 1057\", \"stance\": \"supports\", \"note\": \"'Pr. niham aus *nihiham, vgl. pr. diham von dādan. Dazu np. nihād „fundamentum, natura, indoles“'.\"},\n  {\"src\": \"PHD\", \"where\": \"s.vv. nihādan, nihān\", \"stance\": \"supports\", \"note\": \"'nihādan, nih- ... put, place, establish'; 'nihān [nyhʾanʹ | N ~] concealment, secrecy'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.vv. نهادن, نهان, apadana\", \"stance\": \"supports\", \"note\": \"'نهادن — From Middle Persian nihādan, from Proto-Iranian *ni- + *dádaHtī ... from Proto-Indo-European *dʰédʰeh₁ti'.\"}]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Avestan\", \"words\": \"dhana; gao-dana, gao-di\", \"verdict\": \"confirmed\",\n \"derivation\": \"The container word of this root is amply attested in Avestan, though only in compounds: Bartholomae has 'j. gao-dana-, °δana- n. 1) „Milchgefäss“' with the Vidēvdād passage V.21.7 about the thousand springs that flow together into the milk-vessel that is the child's nourishment; and Pokorny's root-noun list under this same article gives 'Avestan gao-δi- „milk container“' beside 'Avestan gao-δana- n. „milk container“'. Both are gau- 'cow' (Nourai's Gwou cross-reference) + the *dʰeh₁-no-/-ti- derivative 'that in which something is placed'. The one caveat is the simplex Nourai prints: 'dhana' with dh- is not an Avestan form. The Avestan is dāna- (attested only as a second member, e.g. apa-dāna-, daiva-dāna-, gao-dāna-); dhāna-m 'Behälter' is the Old Indic cognate (WLD I 828, Kent s.v. dāna-). Nourai is using his usual PIE-style respelling under an Avestan label rather than misreading a source.\",\n \"derivation_fa\": \"واژهٔ «ظرف» از این ریشه در اوستا فقط در ترکیب می‌آید: بارتولمه gao-dana-/gao-δana- «ظرف شیر» را از وندیداد ۲۱،۷ شاهد می‌آورد و پوکورنی در همین ماده gao-δi- «ظرف شیر» را نیز دارد. هر دو از gau- «گاو» و مشتقی از *dʰeh₁- ساخته شده‌اند. تنها نکته این که صورت سادهٔ «dhana» اوستایی نیست؛ صورت اوستایی dāna- است و dhāna- هم‌ریشهٔ سنسکریت آن است. این املا شیوهٔ نویسشِ نورایی بر پایهٔ صورت هندواروپایی است، نه خطای منبع. ادعای نورایی درست است.\",\n \"sources\": [SRC[\"pie\"]],\n \"ref_check\": [{\"ref\": \"POK:238\", \"status\": \"supports\", \"note\": \"in the dʰe-2 article (pp.235-239) the root-noun paragraph reads 'Avestan gao-δi- „milk container“' and the closing paragraph 'Old Indic dhāna-m „container“ ... Avestan gao-δana- n. „milk container“' — both of Nourai's compounds, on the pages he cites.\"}],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"BRT.txt line 9788, s.v. gao-dana-\", \"stance\": \"supports\", \"note\": \"'j. gao-dana-, °δana- n. 1) „Milchgefäss“: ... frašnaymī °anəm avī ... V.21.7 ... 2) überh. „Gefäss, Napf, Schüssel“ (nur Komp.)'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I p.828\", \"stance\": \"supports\", \"note\": \"'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“' — note the simplex is Indic dhāna-, the Iranian is dāna-.\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. dāna-\", \"stance\": \"supports\", \"note\": \"'dāna-, in apadāna-, daivadāna-: Skt. dhana-m „container, receptacle“; from OP *dā- + suffix -na- (§147.1)'.\"}]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Sogdian\", \"words\": \"gwd`k\", \"verdict\": \"confirmed\",\n \"derivation\": \"Gharib's Sogdian Dictionary, entry 4362 on printed page 174, has γwδʾak(h) / γwδy, read γoδē, glossed 'vessel, container, pitcher, measure' (attested C2, 60R26) and etymologised by Gharib herself with the note '© < Av. gaoδi-, gaoδana-' — which is precisely the arrow Nourai draws from node #8. The Sogdian form shows the usual Middle Iranian spirantisation of initial g- to γ-, monophthongisation of *au to ō, and the productive nominal suffix -ʾak (-ē in the later pronunciation): *gau-dāna-/*gau-di- > γōδ- + -ʾak.\",\n \"derivation_fa\": \"در فرهنگ سغدیِ قریب، مدخل ۴۳۶۲ در صفحهٔ ۱۷۴، صورت γwδʾk / γwδy (خوانده γoδē) به معنی «ظرف، پیمانه» آمده و خودِ قریب ریشهٔ آن را «< اوستایی gaoδi-, gaoδana-» دانسته است — دقیقاً همان پیکانی که نورایی کشیده است. در سغدی گِ آغازین به γ سایشی بدل شده، مصوت مرکب *au به ō ساده شده و پسوند -ʾak افزوده شده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"SOD:174\", \"status\": \"supports\", \"note\": \"SOD_pages.txt line 16158 ff.: the column carries the printed page number '174' and entry '4362 γwδʾak(h) B ... γoδē (γwδy) © < Av. gaoδi-, gaoδana- / vessel, container, pitcher, measure / C2, 60R26'. The dictionary's English index confirms 'container 4362', 'vessel 4362', 'pitcher 4362', 'measure 4362'. So Nourai's SOD:174 is a PAGE number, and the entry number is 4362.\"}],\n \"consulted\": [\n  {\"src\": \"SOD\", \"where\": \"no. 4362, p.174\", \"stance\": \"supports\", \"note\": \"Gharib's own etymology '© < Av. gaoδi-, gaoδana-'.\"},\n  {\"src\": \"BRT\", \"where\": \"s.v. gao-dana-\", \"stance\": \"supports\", \"note\": \"supplies the Avestan source form 'Milchgefäss'.\"},\n  {\"src\": \"POK\", \"where\": \"pp.238-239\", \"stance\": \"supports\", \"note\": \"'Avestan gao-δana- n. „milk container“'.\"}]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"dân «دان ۱»\", \"verdict\": \"confirmed\",\n \"derivation\": \"The Persian element -دان 'holder, container' in گلدان, زهدان, چمدان, نمکدان continues MP dān < Old Iranian *dāna-: Horn no.533 (p.118) 'dān „Behälter“, vergl. ābdān, nemekdān etc. aw. *aŋz-dāna-; ai. -dhāna- „Behälter“', and Mo'in's footnote on the very page Nourai cites (Borhān p.818) gives 'اوستا dāna-، هندی باستان dhāna-، ... پهلوی dān (در zahdān)'. Two cautions. First, the free-standing New Persian noun دان that Borhān lemmatises ('مطلق دانه را گویند ... و چون در آخر کلمه آید معنی ظرفیت بخشد') is primarily 'grain, birdseed', which is a different word (*dʰoh₁-neh₂, Skt. dhānā-, whence دانه); Borhān runs the two together and Nourai follows him. Second, the chart's NOTE that the -dān of ناودان belongs to a different root could not be confirmed: Dehkhoda and Mo'in analyse ناودان simply as ناو 'trough, channel' + the ordinary -دان.\",\n \"derivation_fa\": \"پسوندِ «‐دان» در گلدان، زهدان، چمدان و نمکدان از فارسی میانهٔ dān و ایرانی باستان *dāna- است؛ هرن (شمارهٔ ۵۳۳، ص ۱۱۸) و حاشیهٔ معین بر برهان قاطع (ص ۸۱۸) هر دو همین را می‌گویند. اما دو هشدار: نخست آنکه «دان» مستقل در فارسی بیشتر به معنی «دانه، خوراک پرنده» است و آن واژهٔ دیگری است (هم‌ریشه با سنسکریت dhānā- «دانه»)؛ برهان قاطع این دو را یکجا آورده و نورایی هم از او پیروی کرده است. دوم آنکه یادداشت نمودار دربارهٔ «ناودان» تأیید نشد؛ دهخدا و معین آن را همان «ناو + دان» می‌گیرند.\",\n \"sources\": [SRC[\"dan\"]],\n \"ref_check\": [{\"ref\": \"BQT:818\", \"status\": \"supports\", \"note\": \"Borhān vol.2, leaf 278 of BQT_v2_pages.txt = printed p.818 (running-head calibration leaf+540, checked against داد=807 and داور=821): headword «دان بر وزن نان، مطلق دانه را گویند ... و چون در آخر کلمه آید معنی ظرفیت بخشد، همچو قلمدان و کیفدان و قهوه‌دان», with footnote 7 'اوستا dāna-، هندی باستان dhāna-، ... پهلوی dān'.\"}],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"p.118, no. 533\", \"stance\": \"supports\", \"note\": \"'-dān „Behälter“, vergl. ābdān, nemekdān etc. aw. *aŋz-dāna-; ai. -dhāna- „Behälter“; oss. dōne, don; waḵ. sar. -dān'.\"},\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. dāna-\", \"stance\": \"supports\", \"note\": \"'dāna-, in apadāna-, daivadāna-: Skt. dhana-m „container, receptacle“; from OP *dā- + suffix -na-'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. دان (Persian, Etymology 1)\", \"stance\": \"partial\", \"note\": \"treats the free-standing دان as 'grain', 'From Middle Persian dʾanʹ, from Proto-Iranian *daHnáH ... from Proto-Indo-European *dʰoHnéh₂' — i.e. the homonym, not the container suffix.\"},\n  {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\", \"note\": \"grep for dān / 'Behälter' in HUB.txt returns nothing (Part I follows Horn's numbering but the OCR of this entry is lost).\"}]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Avestan\", \"words\": \"dâ 2; dâtô, dâta 3; dâtô-vare\", \"verdict\": \"plausible\",\n \"derivation\": \"The material is right but the label on the box conflates two Indo-European roots. Av./OP dāta- 'law' is the participle of dā- 'to put, establish' — Kent: 'dāta- sb. „law“: Av. dāta-, NPers. dād; nt. ptc. to *dā-'; Nyberg II 63: 'dāt 1. law ... Av. (726) dāta-, NP dād „justice, equity“'. 'That which is settled' is therefore an exact rendering. The judge is Av. *dātō.bara- 'law-bearer' (a starred form: Horn no.537 'aw. *dātō.bara-; phlv. dātwar, dātbar'), the second member being *bʰer- 'carry' — Nourai's cross-reference to Bher 1 is right, but his spelling 'dātō-vare' already carries the Middle Persian -w-/-v-, so it is not an Avestan shape. The real problem is the gloss 'to settle, to give': 'to give' belongs to PIE *deh₃-, a different root that merged with *dʰeh₁- in Iranian (both give dā-). Nourai's own cited reference makes the distinction: Abolghasemi FFD p.52 writes 'در ایرانی باستان دو ریشهٔ dā وجود داشته است: ۱- به معنی دادن، ۲- به معنی نهادن'. Modern reference works differ over which root dāta- 'law' belongs to — Pokorny, Kent, Bartholomae and Nyberg put it here, under *dʰeh₁-, whereas Wiktionary currently tags NP داد as PIE *dh₃tós 'given' — which is precisely why the box should not have been given both glosses at once.\",\n \"derivation_fa\": \"مادهٔ این خانه درست است ولی معنای دوگانهٔ آن دو ریشهٔ متفاوت را درهم آمیخته است. dāta- «قانون، آنچه نهاده شده» صفت مفعولی dā- «نهادن» است (کنت؛ نیبرگ، ج ۲ ص ۶۳)، و *dātō.bara- «داد‐بر، داور» صورتی بازسازی‌شده است که هرن (شمارهٔ ۵۳۷) با ستاره می‌آورد؛ املای «dātō-vare» در کتاب صورتی فارسی میانه‌وار است نه اوستایی. مشکل در معنای «to give» است: «دادن» از ریشهٔ دیگری (*deh₃-) است که در ایرانی با این ریشه همریخت شده است؛ خودِ ابوالقاسمی در همان صفحهٔ ۵۲ که نورایی ارجاع داده این دو را جدا کرده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [SRC[\"dad\"], SRC[\"davar\"], SRC[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"POK:235\", \"status\": \"supports\", \"note\": \"'with full grade Avestan Old pers. data-' in the dʰe-2 article (Page(s): 235-239); the 'law' sense is developed in the same article ('gr. θέμις „that which is laid down or established by custom“').\"},\n  {\"ref\": \"FFD:52\", \"status\": \"partial\", \"note\": \"Abolghasemi p.52 (pdf 57) supports the root but explicitly splits it: 'در ایرانی باستان دو ریشهٔ dā وجود داشته است: ۱- به معنی دادن، ۲- به معنی نهادن' — against the chart's combined gloss 'to settle, to give'.\"}],\n \"consulted\": [\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. dāta-\", \"stance\": \"supports\", \"note\": \"'dāta- sb. „law“: Av. dāta-, NPers. dād; nt. ptc. to *dā-'; OP dātam DNa 21, XPh 18f.\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.63\", \"stance\": \"supports\", \"note\": \"'dāt [dʾatʹ] 1. law ... — 1. Av. (726) dāta- NP dād „justice, equity“'; 'dātavar [dʾatwbl] judge ... < OIr. *dāta-bara-'.\"},\n  {\"src\": \"HRN\", \"where\": \"p.118, no. 537\", \"stance\": \"supports\", \"note\": \"'dāwer „Richter“ ... aw. *dātō.bara-; phlv. dātwar, dātbar (bezw. dātebar), dawar, arm. LW. datavor'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I p.828\", \"stance\": \"supports\", \"note\": \"lists the *dʰə-ti-/*dʰə-t- nominal derivatives of dhe- including 'gr. θεσις „Satzung, Ordnung“'.\"}]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\", \"words\": \"dâd «داد»; dâvar «داور»\", \"verdict\": \"confirmed\",\n \"derivation\": \"داد 'justice, law' is the direct continuation of MP dād [dʾatʹ] 'law, justice' (MacKenzie) < OP dātam / Av. dāta-. Mo'in's footnote on Borhān p.807, the page Nourai cites, gives that chain verbatim: 'پهلوی dāt (قانون) ... پارسی باستان dāta- (قانون، دستور) ... اوستا dāta- ... قس: هندی باستان dhāta- ... بارتولمه'. داور is MP dādwar/dātōbar 'judge' < *dāta-bara- 'law-bearer', with the regular loss of intervocalic -d- and of -b-/-w- (dātōbar > dādwar > dāwar/dāvar); Borhān itself says 'و در اصل دادور بروزن دادگر بوده' and has a separate headword 'داتوبر ... بمعنی داور و دادری'. The chart's own note is a fair report of Nyberg, whose Middle Persian dātan means both 'to give' and 'to put, to create' (the two roots having merged), but Nyberg's own etymology of dāt 'law' is 'Av. dāta-, NP dād'.\",\n \"derivation_fa\": \"«داد» دنبالهٔ فارسی میانهٔ dād «قانون، دادگری» است که خود از پارسی باستان dātam و اوستایی dāta- می‌آید؛ حاشیهٔ معین بر برهان قاطع (ص ۸۰۷) همین زنجیره را با ارجاع به بارتولمه می‌آورد. «داور» از فارسی میانهٔ dādwar/dātōbar و ایرانی باستان *dāta-bara- «داد‐بر» است؛ دالِ میان‌واکه‌ای و سپس و/ب افتاده است (dātōbar > dādwar > dāvar). خودِ برهان می‌نویسد «در اصل دادور بوده» و مدخل جداگانهٔ «داتوبر» را نیز دارد. ادعای نورایی درست است.\",\n \"sources\": [SRC[\"dad\"], SRC[\"davar\"]],\n \"ref_check\": [\n  {\"ref\": \"BQT:807\", \"status\": \"supports\", \"note\": \"vol.2 leaf 267 = p.807 (running head داد): the داد entry 'وبمعنی راستی و عدل و عدالت', footnote 8 'پهلوی dāt (قانون) ... پارسی باستان dāta- ... قس: هندی باستان dhāta- ... بارتولمه', and the neighbouring headword 'داتوبر ... بمعنی داور و دادری' with the note 'پهلوی است، رک: داور'.\"},\n  {\"ref\": \"BQT:814\", \"status\": \"not_found\", \"note\": \"vol.2 leaf 274 = p.814 by the same calibration is the داس‌/داستان page (داسار، داستاره، داستان، داسخاله); it contains nothing on داد or داور. Its Mo'in footnote (deriving داستان from Pahlavi dātastān 'حق، قانون') belongs to node #14, not here.\"},\n  {\"ref\": \"BQT:821\", \"status\": \"supports\", \"note\": \"vol.2 leaf 281 = p.821 (running head داوردان): 'داور - بر وزن خاور، نام خدای عزوجل است - و پادشاه عادل ... و دراصل دادور بروزن دادگر بوده', with the Latin-script footnote giving Pahl. dātōbar/dātbar/dātwar, Av. dātō-bara, Arm. datavor.\"},\n  {\"ref\": \"HRN:118\", \"status\": \"supports\", \"note\": \"Horn p.118 (leaf 139) no.537 'dāwer „Richter“ ... aw. *dātō.bara-; phlv. dātwar, dātbar'; the same page also carries no.533 -dān.\"},\n  {\"ref\": \"NYB:60\", \"status\": \"partial\", \"note\": \"Nyberg's entries 'dāt 1. law ... Av. dāta-, NP dād' and 'dātan ... A. to give ... B. to put, to place ... to create' stand on p.63 of the 1974 Glossary by the leaf-minus-8 mapping (leaf 71), not on p.60 (which is damik-dar); the substance of Nourai's note is nevertheless accurate.\"}],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"s.vv. dād, dādwar\", \"stance\": \"supports\", \"note\": \"'dād [dʾatʹ | M dād, N ~] law, justice'; 'dādwar [dʾatwbl | (M dʾadywr, P dʾadbr), N dā(d)war] judge'.\"},\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.63\", \"stance\": \"supports\", \"note\": \"'dātavar [dʾatwbl] judge P2:2 ... < OIr. *dāta-bara-, v. dāt (1) ... Paz. NP davar'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.vv. داد, داور\", \"stance\": \"partial\", \"note\": \"'داد — From Middle Persian dād “law, justice”, from Old Persian dātam “law”, from Proto-Iranian *daHtáh, from Proto-Indo-European *dh₃tós (“given”)' — the Iranian chain agrees with the chart, but Wiktionary assigns the PIE preform to *deh₃- 'give' rather than to *dʰeh₁-. 'داور — From Middle Persian dʾatwbl (dādwar, “judge”). By surface analysis, داد + ـور'.\"},\n  {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā, OCR\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for داور returns only incidental occurrences inside other entries; no headword found in the OCR.\"}]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Pahlavi\", \"words\": \"dast-war; dâtastân\", \"verdict\": \"disputed\",\n \"derivation\": \"Half of this box is right and half is rejected by every source I could check, including the one Nourai cites. dātastān / dādestān 'judgement, law, court case' is indeed dāta- + the abstract suffix -stān (MacKenzie: 'dādestān [DYNA < A dyn; dʾatstʾanʹ | M dʾa(d)ystʾan, N dā(de)stān] judgement, justice, law; case, process'; Nyberg II 63 'dātistān ... decision ... NP dāstān „a tale, story“'). But dastwar does NOT belong to dā- at all. Horn p.127 — exactly the page Nourai gives — says the opposite in so many words: 'ap. *dastabara-; phlv. dastwar, dastbar. Nicht zu dest „Hand“, sondern zu der in aw. dąstva- etc. steckenden Wurzel daṇs- (Darmesteter, Et. ir. I, 115 Note)'. Nyberg II 61 agrees: 'dastavar ... dast- from Av. (746) dąh- „to teach“, cf. (745) dąstvā „religious doctrine“'. Wiktionary offers only two candidates, Proto-Iranian *dasta-bara- 'hand-bearer' or Proto-Iranian *daṅh- 'to teach' (PIE *dens-). Nyberg's own Pahlavi text even lists dastavarān and dātavarān side by side as two different offices in one sentence (DkM 107), which shows they are separate words. So the chart's arrow dā 2 → dast-war is wrong; the note Nourai himself adds ('NYB:59 claims dastwar from Avestan dah: to teach') is the view modern scholarship actually holds.\",\n \"derivation_fa\": \"یک نیمهٔ این خانه درست است و نیمهٔ دیگر رد می‌شود. dātastān/dādestān «دادرسی، دعوی، قانون» درست از dāta- با پسوند -stān ساخته شده است (مکنزی؛ نیبرگ ج۲ ص ۶۳). اما dastwar هیچ پیوندی با dā- ندارد: همان صفحهٔ ۱۲۷ هرن که نورایی ارجاع داده می‌نویسد «پارسی باستان *dasta-bara-؛ نه از dast دست، بلکه از ریشهٔ daṇs- که در اوستایی dąstva- هست»، و نیبرگ (ج۲ ص ۶۱) آن را از اوستایی dąh- «آموختن» می‌گیرد؛ ویکی‌واژه هم یا *dasta-bara- «دست‌دار» یا *danh- «آموختن» را پیش می‌نهد. پس پژوهش امروزی این پیکان را رد می‌کند؛ و جالب آنکه خودِ یادداشتِ نورایی در همین خانه همین نظر را نقل کرده است.\",\n \"sources\": [SRC[\"dastur\"], SRC[\"dastan\"]],\n \"ref_check\": [{\"ref\": \"HRN:127\", \"status\": \"contradicts\", \"note\": \"Horn p.127 (leaf 148), continuation of no.568 destūr: 'ap. *dastabara-; phlv. dastwar, dastbar. Nicht zu dest „Hand“, sondern zu der in aw. dąstva- etc. steckenden Wurzel daṇs-'. The page Nourai cites explicitly denies a connection with dā-.\"}],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.61 s.v. dastavar\", \"stance\": \"contradicts\", \"note\": \"'dast- from Av. (746) dąh- „to teach“, cf (745) dąstvā „religious doctrine“; hence MPrth dst „able, skilful“'. The same entry quotes '~-ān u dātavarān u hērpatān' — dastavarān and dātavarān as distinct offices.\"},\n  {\"src\": \"PHD\", \"where\": \"s.vv. dastwar, dādestān\", \"stance\": \"partial\", \"note\": \"'dastwar [dstwbl | M dstwr, N dastūr] authority, priest, minister' (no etymology given); 'dādestān ... judgement, justice, law; case, process' — supports the dātastān half only.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. دستور\", \"stance\": \"contradicts\", \"note\": \"'Inherited from Proto-Iranian *dasta-bara-, from Proto-Indo-Iranian *ǵ́ʰástas (\\\"hand\\\") + *bʰer- ... Alternatively, inherited from Proto-Iranian *danh- (\\\"to teach, instruct\\\"), from Proto-Indo-European *dens-' — neither is *dʰeh₁-.\"}]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\", \"words\": \"dastûr «دستور»; dâstân «داستان»\", \"verdict\": \"confirmed\",\n \"derivation\": \"Both Middle-to-New Persian steps drawn here are correct; only the ancestry of dastwar one box up is in doubt. دستور continues MP dastwar 'authority, high priest, minister' unchanged but for the regular Middle Persian -war > New Persian -ūr in this word (MacKenzie: 'dastwar ... N dastūr'). داستان continues MP dādestān/dātistān 'legal case, judgement' with syncope of the middle syllable — MacKenzie writes the outcome as 'N dā(de)stān' and Nyberg glosses his dātistān entry 'NP dāstān „a tale, story“'; Wiktionary: 'probably a clipping of Middle Persian dātistān “law, process, court case” ... from Proto-Indo-European *dʰeh₁-'. Mo'in's footnote in Borhān on the داستان entry (p.814) derives it from Pahlavi dātastān 'حق، قانون'. The semantic path is 'the case in court' > 'the account of a case' > 'tale, story'; دستان, the chart's extra, is the contracted doublet. One slip: the gloss 'story' attached to dastūr belongs to دستان, not to دستور, which means 'minister, high priest, rule, permission'. Note also that Horn p.127 records Nöldeke's alternative, attaching np. dāstān/destān to the same daṇs- root as dastūr; Nyberg's and MacKenzie's derivation from dātistān is the one modern scholarship follows.\",\n \"derivation_fa\": \"هر دو گامِ فارسی میانه به فارسی نو درست است؛ آنچه محل تردید است تبارِ dastwar در خانهٔ پیشین است. «دستور» همان dastwar پهلوی است که پایانهٔ -war آن در این واژه به -ūr بدل شده. «داستان» از dādestān/dātistān پهلوی با افتادن هجای میانی ساخته شده است؛ مکنزی خود می‌نویسد «N dā(de)stān» و نیبرگ در ذیل dātistān می‌آورد «NP dāstān ‘a tale, story’»؛ حاشیهٔ معین بر برهان (ص ۸۱۴) نیز آن را از پهلوی dātastān «حق، قانون» می‌داند. تحول معنایی چنین است: «دعوی، پرونده» ← «گزارش دعوی» ← «قصه»؛ و «دستان» دوگانهٔ کوتاه‌شدهٔ آن است. تنها لغزش، معنی «story» است که به دستور داده شده و در حقیقت از آنِ دستان است.\",\n \"sources\": [SRC[\"dastan\"], SRC[\"dastur\"]],\n \"ref_check\": [{\"ref\": \"BQT:862\", \"status\": \"supports\", \"note\": \"vol.2 leaf 322 = printed p.862 by the leaf+540 calibration (verified against داد=807, دان=818, داور=821): the page carries the دست‌/دستوار block ('دستوار ... دستوانه') immediately preceding the دستور headword; دستان stands a few pages earlier in the same دست‐ run.\"}],\n \"consulted\": [\n  {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II p.63 s.v. dātistān\", \"stance\": \"supports\", \"note\": \"'dātistān [dʾatstʾanʹ; DYNʾ] decision ... judgment ... MPrs dʾadystʾan; Paz. dādēstā; NP dāstān „a tale, story“'.\"},\n  {\"src\": \"PHD\", \"where\": \"s.vv. dādestān, dastwar\", \"stance\": \"supports\", \"note\": \"'dādestān ... N dā(de)stān'; 'dastwar ... N dastūr'.\"},\n  {\"src\": \"BQT\", \"where\": \"vol.2 p.814, footnote to داستان\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote reads the word as Pahlavi dātastān 'حق، قانون'.\"},\n  {\"src\": \"HRN\", \"where\": \"p.127, no. 568\", \"stance\": \"partial\", \"note\": \"'Zu derselben Wurzel stellt Nöldeke (mündliche Mitteilung) auch np. dāstan-, destān „Geschichte, Erzählung“' — i.e. Horn/Nöldeke attach dāstān to daṇs- rather than to dātistān; this is the minority view today.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. داستان\", \"stance\": \"supports\", \"note\": \"'Probably a clipping of Middle Persian dātistān “law, process, court case”, from Proto-Iranian *dāt-ya- ... from Proto-Indo-European *dʰeh₁- (\\\"to do, place\\\")'.\"}]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Dhě 2\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)\",\n \"note\": \"The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dțhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.\",\n \"note_fa\": \"خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δaiti-، gao-δana-، dāman-) هم عیناً از همین مادهٔ پوکورنی است. سه لغزش در بخش یکم هست: ۱) صورت اوستایی «پنام» paiti.dāna- است نه paiti-dāma — خطای چاپی کتاب؛ ۲) apadāna پارسی باستان است نه اوستایی و معنایش «کاخ، تالار بار» است؛ ۳) پهلوی dastwar هیچ ربطی به این ریشه ندارد و هرن (ص ۱۲۷) و نیبرگ (ج۲ ص ۶۱) آن را از ریشهٔ daṇs-/dąh- «آموختن» می‌گیرند. نکتهٔ کوچک‌تر آنکه معنای «دادن» در خانهٔ ۱۱ متعلق به ریشهٔ دیگر *deh₃- است و ابوالقاسمی در همان FFD:52 این دو را جدا کرده است. در مجموع، ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n \"sources\": [SRC[\"pie\"]],\n \"ref_check\": [\n  {\"ref\": \"AHD:1512\", \"status\": \"supports\", \"note\": \"Watkins's Indo-European appendix (local file AHD_watkins1985.txt line 375): 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235.]' — the same list Nourai cites by its 1975 New College page 1512 (roots are alphabetical over pp.1505-1550, so 'dhē-' falls in the right place); the copy on disk is the 1985 standalone reprint with different pagination.\"},\n  {\"ref\": \"POK:235\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 22276-22510: 'Root / lemma: dʰe-2 / Meaning: to put, place, say' ... 'References: WP. I 826 ff ... Page(s): 235-239'.\"}],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"pp.235-239, dʰē-2\", \"stance\": \"supports\", \"note\": \"supplies not only the root but every Iranian form of the chart: 'Avestan Old pers. data-', 'Avestan ni-δaiti- f. „laying down, putting away, hiding“', 'Avestan gao-δi- „milk container“', 'Avestan gao-δana- n. „milk container“', 'Avestan daman-, dąman- n. „site, creature“'.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I pp.826-830 (p.828)\", \"stance\": \"supports\", \"note\": \"the parent article of Pokorny's; p.828 carries 'av. ni-δaiti- f. „das Niederlegen, Ablegen, Verbergen“', 'Ai. dhāna-m „Behälter“ ... av. gao-dana- n. „Milchgefäß“', 'av. dāman-, dąman- n. „Stätte, Wohnstätte; Geschöpf“'.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. dhē-¹\", \"stance\": \"supports\", \"note\": \"'To set, put. Contracted from *dheə.' Same gloss as Nourai's 'to do, set'.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/dʰeh₁-\", \"stance\": \"supports\", \"note\": \"'*dʰeh₁- (perfective): to do; to put, place.'\"}],\n \"nodes\": nodes,\n}\n\nout = {\n \"pdf_page\": 124,\n \"book_page\": 94,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-124.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk124.py",
 "description": "Generate page-124.json"
}
```


### [2026-09-05T18:50:55.201Z] TOOL RESULT

```
ok 14
```


## [2026-09-05T18:51:00.807Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-124.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 124",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T18:51:02.858Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 10, 'transcription_suspect': 1, 'plausible': 2, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 3, 'supports': 18, 'not_checked': 2, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 37, 'partial': 7, 'contradicts': 4, 'silent': 3} | by book: {'Wiktionary': 9, 'HRN': 8, 'PHD': 6, 'BRT': 5, 'NYB': 5, 'WLD': 4, 'KNT': 4, 'POK': 2, 'KLN': 2, 'BQT': 2, 'HUB': 2, 'SOD': 1, 'ARY': 1}
```


## [2026-09-05T18:51:07.619Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json,io\np='data/verification/page-124.json'\nd=json.load(open(p))\nn=d['entries'][0]['note']\nd['entries'][0]['note']=n.replace(\"Dțhě 2\",\"Dhě 2\")\nassert \"Dțhě\" not in d['entries'][0]['note']\nwith io.open(p,'w',encoding='utf-8') as f:\n    json.dump(d,f,ensure_ascii=False,indent=2); f.write(\"\\n\")\nprint('fixed')\nEOF\npython3 tools/verify_check.py 124 | tail -3; ls -la data/verification/page-124.json data/verification/sources/refs/ocr/BOOK/124.png",
 "description": "Fix typo and re-check"
}
```


### [2026-09-05T18:51:09.927Z] TOOL RESULT

```
fixed
root verdicts: {'confirmed': 1}
ref checks: {'partial': 3, 'supports': 18, 'not_checked': 2, 'not_found': 1, 'contradicts': 1}
books consulted: {'supports': 37, 'partial': 7, 'contradicts': 4, 'silent': 3} | by book: {'Wiktionary': 9, 'HRN': 8, 'PHD': 6, 'BRT': 5, 'NYB': 5, 'WLD': 4, 'KNT': 4, 'POK': 2, 'KLN': 2, 'BQT': 2, 'HUB': 2, 'SOD': 1, 'ARY': 1}
-rw-rw-r-- 1 sfmqrb sfmqrb 63803 Sep  5 14:51 data/verification/page-124.json
-rw-rw-r-- 1 sfmqrb sfmqrb 91077 Sep  5 14:38 data/verification/sources/refs/ocr/BOOK/124.png
```


## [2026-09-05T18:51:29.977Z] AGENT

Page 124 (book p. 94) — root **Dhě 2** = PIE *dʰeh₁- 'to put, place; to do', 1 entry, 14 nodes. `verify_check.py 124`: 14/14 nodes, 0 PROBLEM lines.

Verdicts: root **confirmed**; nodes **10 confirmed, 2 plausible, 1 disputed, 1 transcription_suspect**.
Ref checks: 18 supports, 3 partial, 1 contradicts, 1 not_found, 2 not_checked.

Flagged items:
- **transcription_suspect — #3 `paiti-dâma`**: the Avestan mouth-veil is `paiti.dāna-` (Bartholomae V.18.1, Yt.5.133; Horn no. 332 "aw. paiti.dāna-, phlv. padām"; and Mo'in's footnote on Borhān p. 418, the very page Nourai cites, prints «پئیتی‌دان»). Printed page 124 shows `paiti-dâma`, so this is **Nourai's misprint**, assimilated to `han-dâma` above it; the extraction is faithful. Page image saved to `data/verification/sources/refs/ocr/BOOK/124.png`.
- **disputed — #13 `dast-war`**: HRN:127, Nourai's own citation, says the opposite ("Nicht zu dest 'Hand', sondern zu der … Wurzel daṇs-"); Nyberg II 61 derives it from Av. dąh- 'to teach'; Wiktionary offers only *dasta-bara- or *danh-. Nothing links it to dā-. (The `dâtastân` half of the node is correct.)
- **plausible — #6**: `apa-dâna` is Old Persian, not Avestan, and means 'palace/audience hall' (Kent, Lexicon p. 167-8); "concealed part" is Kent's Skt. apadhā- comparison. Also `upa-ni-dâ` → پنهان is contradicted by Horn no. 332 (pad + nihān).
- **plausible — #11**: gloss "to settle, to give" conflates *dʰeh₁- with *deh₃-; Nourai's own FFD:52 (Abolghasemi p. 52) separates the two Old Iranian dā- roots explicitly.
- **BQT:814 (node #12) not_found**: that page is the داس/داستان spread, not دād/داور — it belongs to node #14's dāstān. (BQT:807, 818, 821, 862 all verified against the vol-2 running-head calibration leaf+540.)
- Page-number drift worth noting: POK:235 for node #1 is wrong (mazdā is at Pokorny 730); NYB:60 → the dāt/dātavar entries are on p. 63 of the 1974 glossary; NYB:59 → dastavar is on p. 61. MON:813 could not be checked (Mo'in on disk is unpaginated OCR).

**No extraction errors** — the JSON matches the printed page everywhere, including `nahâdan : to do` (the book's own slip for 'to put') and `dhana` under an Avestan label (Nourai's PIE-style respelling of Av. dāna-).

Nice finds: Gharib's Sogdian entry 4362 (p. 174) carries the etymology "© < Av. gaoδi-, gaoδana-" itself, confirming node #9 and node #8 in one line; and Nyberg (II 63) and MacKenzie both give NP dāstān directly as the outcome of MP dātistān/dādestān, confirming node #14. 15 web sources archived via `fetch_source.py`.
