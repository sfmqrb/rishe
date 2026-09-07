# Verification process log — verify-page-351


## [2026-09-07T18:17:46.974Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 351 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-351.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-351.json. Write /home/sfmqrb/git/rishe/data/verification/page-351.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 351` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:17:49.046Z] AGENT

I'll start by reading the instructions and the source materials.


## [2026-09-07T18:17:49.795Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:17:49.809Z] TOOL RESULT

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


## [2026-09-07T18:17:50.497Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-351.txt"
}
```


### [2026-09-07T18:17:50.524Z] TOOL RESULT

```
1	=== PDF page 351 (book page 321) ===
2	--- entry 0 ---
3	ROOT Ndher -> redirect to En
4	--- entry 1 ---
5	ROOT Ndhi -> redirect to En
6	--- entry 2 ---
7	ROOT Ndhos -> redirect to En
8	--- entry 3 ---
9	ROOT [Indo-European] Ne 1, Nei 3, An 4 : no, not  (refs POK:756; KNT:167)  PART 1
10	#1 (parent #0) [Avestan / Old Persian] refs=POK:756 | na 1, ni 3, naiy : no, not ; ni-us-tavah : not out of power, strong ☞Ud 1,Těu 1
11	  #2 (parent #1) [Persian] refs=BQT:2210 | na «نه (نا ـ)» : no ; nastŭh «نستوه» : energetic (fighter)
12	#3 (parent #0) [Avestan / Old Persian] refs=POK:757; KNT:167 | a- 2, â- 2, an- : no, not
13	  #4 (parent #3) [Pahlavi] refs=BQT:264; KNT:209 | a-purn-ây : "not full of life", young ☞Aiw
14	    #5 (parent #4) [Persian] refs=BQT:264 | bornâ «بُرنا» : young
15	  #6 (parent #3) [Avestan / Old Persian] refs=BQT:36,72,788 | an-âhita : not dirty, innocent ☞Ahu ; an-aoša : not mortal ☞Ôus 1 ; â-zarema-dugedâ : ageless woman ☞Ger 2 ; a-xšae-na : not bright, dark blue ☞Ksei 2
16	    #7 (parent #6) [Persian] refs=MON, BQT | ânâhîtâ «آناهیتا (ناهید)» : "innocent, pure" ; anŭšeh «انوشه (انوشیروان)» : eternal ; âzarmîdoxt «آزرمیدخت» : "ageless woman" ; xašan «خشن (خشیسار ، خشنسار)» : a blue bird ☞Ksei 2
17	  #8 (parent #3) [Avestan / Old Persian] refs=BQT:46; POK:594,743 | a-karana : endless ☞Karana ; a-muyamnô : not movable ☞Mew ; a-sŭr : not morning yet, dawn ☞Keu 4 ; an-usant : not willing, reluctant ☞Wek
18	#9 (parent #0) [Sanskrit] refs=AHD | a-, an- : not
19	#10 (parent #0) [Germanic] refs=AHD | ne, na, un-
20	  #11 (parent #10) [English] refs=None | no, none, not, nothing, nor, neither, never, un-, undo
21	#12 (parent #0) [Sogdian] refs=SOD:32 | n` : no, not ; n`-krtk : "not done", uncoined silver ☞Kwer
22	  #13 (parent #12) [Persian] refs=BQT:2157 | noqreh «نقره» : silver
23	#14 (parent #0) [Latin] refs=AHD | ne : not ; ne-ŭllus : not any, null ☞I 2 ; ni-scîre : not knowing, silly ; nek, neg : not ; negâre : to negate, deny
24	  #15 (parent #14) [Arabic] refs=TAD:73 | naker, n.k.r : to negate, deny, not recognize
25	    #16 (parent #15) [Persian] refs=FVA:415 | enkâr «انکار» : denial | extra: مُنکر ، نکیر ، نکره
26	  #17 (parent #14) [English] refs=AHD | null, nice, negative, neglect, negotiate, deny
27	
```


## [2026-09-07T18:17:54.058Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-351.json | head -200",
 "description": "Read source JSON for page 351"
}
```


## [2026-09-07T18:17:54.771Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T18:17:55.276Z] TOOL RESULT

```
{
    "pdf_page": 351,
    "book_page": 321,
    "entries": [
        {
            "root": {
                "name": "Ndher",
                "redirect": "En"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ndhi",
                "redirect": "En"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ndhos",
                "redirect": "En"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Ne 1, Nei 3, An 4",
                "lang": "Indo-European",
                "refs": "POK:756; KNT:167",
                "gloss": "no, not"
            },
            "part": 1,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:756",
                    "words": [
                        {
                            "translit": "na 1, ni 3, naiy",
                            "gloss": "no, not",
                            "script": null
                        },
                        {
                            "translit": "ni-us-tavah",
                            "gloss": "not out of power, strong",
                            "script": null,
                            "see": [
                                "Ud 1",
                                "T\u011bu 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Persian",
                    "refs": "BQT:2210",
                    "words": [
                        {
                            "translit": "na",
                            "gloss": "no",
                            "script": "\u0646\u0647 (\u0646\u0627 \u0640)"
                        },
                        {
                            "translit": "nast\u016dh",
                            "gloss": "energetic (fighter)",
                            "script": "\u0646\u0633\u062a\u0648\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:757; KNT:167",
                    "words": [
                        {
                            "translit": "a- 2, \u00e2- 2, an-",
                            "gloss": "no, not",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Pahlavi",
                    "refs": "BQT:264; KNT:209",
                    "words": [
                        {
                            "translit": "a-purn-\u00e2y",
                            "gloss": "\"not full of life\", young",
                            "script": null,
                            "see": [
                                "Aiw"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": "BQT:264",
                    "words": [
                        {
                            "translit": "born\u00e2",
                            "gloss": "young",
                            "script": "\u0628\u064f\u0631\u0646\u0627"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 3,
                    "lang": "Avestan / Old Persian",
                    "refs": "BQT:36,72,788",
                    "words": [
                        {
                            "translit": "an-\u00e2hita",
                            "gloss": "not dirty, innocent",
                            "script": null,
                            "see": [
                                "Ahu"
                            ]
                        },
                        {
                            "translit": "an-ao\u0161a",
                            "gloss": "not mortal",
                            "script": null,
                            "see": [
                                "\u00d4us 1"
                            ]
                        },
                        {
                            "translit": "\u00e2-zarema-duged\u00e2",
                            "gloss": "ageless woman",
                            "script": null,
                            "see": [
                                "Ger 2"
                            ]
                        },
                        {
                            "translit": "a-x\u0161ae-na",
                            "gloss": "not bright, dark blue",
                            "script": null,
                            "see": [
                                "Ksei 2"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "MON, BQT",
                    "words": [
                        {
                            "translit": "\u00e2n\u00e2h\u00eet\u00e2",
                            "gloss": "\"innocent, pure\"",
                            "script": "\u0622\u0646\u0627\u0647\u06cc\u062a\u0627 (\u0646\u0627\u0647\u06cc\u062f)"
                        },
                        {
                            "translit": "an\u016d\u0161eh",
                            "gloss": "eternal",
                            "script": "\u0627\u0646\u0648\u0634\u0647 (\u0627\u0646\u0648\u0634\u06cc\u0631\u0648\u0627\u0646)"
                        },
                        {
                            "translit": "\u00e2zarm\u00eedoxt",
                            "gloss": "\"ageless woman\"",
                            "script": "\u0622\u0632\u0631\u0645\u06cc\u062f\u062e\u062a"
                        },
                        {
                            "translit": "xa\u0161an",
                            "gloss": "a blue bird",
                            "script": "\u062e\u0634\u0646 (\u062e\u0634\u06cc\u0633\u0627\u0631 \u060c \u062e\u0634\u0646\u0633\u0627\u0631)",
                            "see": [
                                "Ksei 2"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
```


### [2026-09-07T18:17:55.312Z] TOOL RESULT

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


## [2026-09-07T18:18:36.561Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-351.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-07T18:18:37.910Z] TOOL RESULT

```
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 3,
                    "lang": "Avestan / Old Persian",
                    "refs": "BQT:46; POK:594,743",
                    "words": [
                        {
                            "translit": "a-karana",
                            "gloss": "endless",
                            "script": null,
                            "see": [
                                "Karana"
                            ]
                        },
                        {
                            "translit": "a-muyamn\u00f4",
                            "gloss": "not movable",
                            "script": null,
                            "see": [
                                "Mew"
                            ]
                        },
                        {
                            "translit": "a-s\u016dr",
                            "gloss": "not morning yet, dawn",
                            "script": null,
                            "see": [
                                "Keu 4"
                            ]
                        },
                        {
                            "translit": "an-usant",
                            "gloss": "not willing, reluctant",
                            "script": null,
                            "see": [
                                "Wek"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "a-, an-",
                            "gloss": "not",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ne, na, un-",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "no, none, not, nothing, nor, neither, never, un-, undo",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 0,
                    "lang": "Sogdian",
                    "refs": "SOD:32",
                    "words": [
                        {
                            "translit": "n`",
                            "gloss": "no, not",
                            "script": null
                        },
                        {
                            "translit": "n`-krtk",
                            "gloss": "\"not done\", uncoined silver",
                            "script": null,
                            "see": [
                                "Kwer"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "BQT:2157",
                    "words": [
                        {
                            "translit": "noqreh",
                            "gloss": "silver",
                            "script": "\u0646\u0642\u0631\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ne",
                            "gloss": "not",
                            "script": null
                        },
                        {
                            "translit": "ne-\u016dllus",
                            "gloss": "not any, null",
                            "script": null,
                            "see": [
                                "I 2"
                            ]
                        },
                        {
                            "translit": "ni-sc\u00eere",
                            "gloss": "not knowing, silly",
                            "script": null
                        },
                        {
                            "translit": "nek, neg",
                            "gloss": "not",
                            "script": null
                        },
                        {
                            "translit": "neg\u00e2re",
                            "gloss": "to negate, deny",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "Arabic",
                    "refs": "TAD:73",
                    "words": [
                        {
                            "translit": "naker, n.k.r",
                            "gloss": "to negate, deny, not recognize",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 15,
                    "lang": "Persian",
                    "refs": "FVA:415",
                    "words": [
                        {
                            "translit": "enk\u00e2r",
                            "gloss": "denial",
                            "script": "\u0627\u0646\u06a9\u0627\u0631"
                        }
                    ],
                    "script_extra": "\u0645\u064f\u0646\u06a9\u0631 \u060c \u0646\u06a9\u06cc\u0631 \u060c \u0646\u06a9\u0631\u0647",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 14,
                    "lang": "English",
                    "refs": "AHD",
```


## [2026-09-07T18:18:38.354Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','BQT','MON','SOD','AHD','TAD','FVA','BRT','PHD','HRN','HUB','ARY','PLA','AFM','KLN','WLD']:\n    v=d.get(k)\n    print('===',k)\n    print(json.dumps(v,ensure_ascii=False)[:900])\n\"",
 "description": "Ref metadata"
}
```


### [2026-09-07T18:18:39.639Z] TOOL RESULT

```
=== POK
{"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
=== KNT
{"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; sec
=== BQT
{"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
=== MON
{"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
=== SOD
{"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca
=== AHD
{"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
=== TAD
{"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
=== FVA
{"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
=== BRT
{"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
=== PHD
{"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
=== HRN
{"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
=== HUB
{"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
=== ARY
{"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
=== PLA
{"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py P
=== AFM
{"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image", "covers_etymology": true, "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.", "
=== KLN
{"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
=== WLD
{"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
```


## [2026-09-07T18:18:45.306Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==413 || NR==414 {print \"=== leaf \"NR-1\" ===\"; print}' POK_02.txt | head -120",
 "description": "POK p.756-757"
}
```


## [2026-09-07T18:18:46.296Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^naiy\\|^na \\|naiy\" KNT.txt | head -30; echo \"---209---\"; grep -n \"puθra\\|apurnāy\\|purnāy\" KNT.txt | head",
 "description": "KNT naiy"
}
```


### [2026-09-07T18:18:46.555Z] TOOL RESULT

```
=== leaf 412 ===
 formica  (vgl.  zum  lautlichen  oben  lat.  formldö:  gr. (.LOQ{.id))]  gr.  !xvQf.iog  (Lycophr.),  (,iVQi.irj^j  dor.  (xvguä^  (Ä-Erw.  zum  ä-St., wie  bQi.Liyt.ag  lat.  formica^  ai.  valml-ka-  zum  I-St.,  und  ai.  vamra-hd  zum o-St.) ;    unklar  arm.  mrjiun  [*murjimno-)^  Gen.  mrjman.
Auf  norm- :  gr.  ßvqiia^,  ßoQi-ia^  Hes.  {ß-  Schriftbehelf  für  /,  vgl.  auch 8Q(j,iKag'  ^VQ(.i7]^  Hes.);  ai.  vaZTTiiÄa- m.  , Ameisenhaufen';  daneben  mit  ganz alleinstehender  Lautfolge  vamrd-  m.,  vamri  f.  , Ameise'.
Auf  mouro-'.  aisl.  maurr^  daneben  *meur-  in  dän.  myre^  schwed.  myi^a {*meu'i'iön-),  mndl.  Fl.  mure  (einmal  belegt)  miere,  nndl.  mier,  mnd.  mlre (zum  l  s.  van  Wijk),  mengl.  mire,  myre  (skand.  Lw.),  ags.  myre,  engl,  mire, heute  nur  noch  fis-mire  (vom  Ausspritzen  ihrer  Säure),   krimgot.  miera.
WP.  II  306  f.,  WH.  I  531  f.,  Trautmann  170,  Specht  Idg.  Dekl.  45.
750
niö[u]-lo- :  mu-lo-  , Wurzel,  Pflanze^;  als  ,Mund  der  Pflanze^  zu  mü-  S  7fsi Ai.  müla-  n.  ^WurzeF,  müla-karman-  n.  , Zauberei  mit  Wurzeln'
ir
art
gr.  fX(üXv  ,e'm  fabelhaftes  Wunderkraut  (Hom.) ;  gelbblühende  Knoblau  k
b  (Theophr.  Dioscor.)',  {.icblv^a  ,Knoblauchart^
WP.  II  303,  310,  Wackernagel  Sitz.-Ber.  Pr.  Akad.  1918,  410  f.
i22Ö[u]-ro-  :  znü-ro-  , stumpfsinnig,  töricht^.
Ai.  mürd-  ,stumpfsinnig,   blöde,   dumm^ ;    gr.   iio)q6q,  att.  ixwqoq  ,duiinn  -* töricht^  (daraus  lat.  mörus  ,närrisch,  albern^).  ^t^
WP.  II  303,  WH.  II  lt4.  '-§
■   ^- moz-g-o-,  moz-g-en-,  mos-k-o-  ,Mark,  Hirn^  '^
Ai.  majjdn,   majjä,   majjas-   ,Mark*,  mastülca-  , Gehirn',  mdstaka-  ,KopL  - Schädel*;  SiV.  mazga-  ,Mark,  Hirn';  ahd.  mar (a)^,  mar{a)kj  a.s.  mar g^  a^s» mearg,  aisl.  mergr  (Gen.  mergjar)  ,Mark*,   aschwed.  micergher]    ksl.  mozg^  ^ , Gehirn',  mo^dam  {*mozgem)^  Akk.  PL  mozdeni  ,Mark',  apr.  musgeno  ,Mark* wozu   (mit  Umstellung   aus  *mazgenes)   lit.   f.   PL   smageneSj  lett.  smadenet , Gehirn';  toch.  A  mäisunt  ,Mark'.
WP.  II  309,  Trautmann  172  f.,  Specht  Idg.  DekL  78  f.
mozgho-s  ,junges  Rind';  nur  arm.  und  griech.  ;^
Arm.  mozi   ,junges   Rind   ,Kalb*  =  gr.  ^oaxlov,    Demin.   zu  ixoc^og  m.
jjunger  Stier,  Kalb',  f.  Junge  Kuh,  Mädchen' ;  wohl  identiscsh  mit  i^öaxog
,Pflanzentrieb,  Schößling'.
WP.  II  309.  .
tnrk-  , eßbare  Wurzel,  Mohrrübe,  Möhre'?
Gr.  ßodyiava  , wildes  Gemüse'  Hes. ;  ahd.  mor{a)ha  ,Daucus  carota',  nhd. Mohr-rübe,  Möhre,  ags.  more,  moru  ds.,  spätahd.  Demin.  morhila  ,Morchel^ (möhrenähnlicher  Pilz);  dagegen  scheint  russ.  morkovh,  morkva  ,Möhre', serb.  mrkva  aus  dem  Germ,  entlehnt  zu  sein.
WP.  II  313.
•
inregh-in{n)o-  , Hirnschale,  Hirn'.
Gr.  ßQSxiiögy  ßqexua  n.  (und  ßgeyi-ia)  , Vorderkopf,  Oberschädel',  ags. hregen,  brcegen  n.  , Gehirn'  (engL  hrain),  afries.  brein,  mnd.  bragen,  bregen, nhd.  Bräge
=== leaf 413 ===
n  m.  ds.
WP.  II  314.
mreghu-,  mrghu-  ,kurz'.
Präkr.  mühu-,  av.  mdrdzu-jlti-,  -Jva-  ^ßoaxvßiog^,  sogd.  murzak  ,kurz'; gr.   ßgaxvQ   ,kurz',   ßgdxscc   , seichte   Stellen';    dazu    ßQaxfaiv    , Oberarm', Komparativ  neben  ßQaaacjVj
751
lat.  Irevis  (zunächst  aus  dem  Fem.  *6re(x)wl)  ,kurz',  hrüma  ,Winter- sonnen wende,  Winter,  Kälte*  {*brevi-mä,  *hreu-ma  ,Zeit  der  kürzesten  Tage);
got.  gamaürgjan  ,verkürzenS  alid.  murg{i)  ,kurz',  murgfäri  ,zerbrechlich*, a^-s.  myrge  , angenehm*,  engl,  merry. Vf.  II  314,  WH.  I  115.
j.  IZ2U-  Schallnachahmung  für  den  mit  gepreßten  Lippen  erzeugten  dumpfen Laut:  jUndeutlich  reden,  unartikuliert  murmeln  (daher  auch  Worte  für ,stumm*);  Mund,  Maul;  den  Mund  geschlossen  halten  oder  schließen'; mü-ko-  , stumm'.
1.  Gr.  ^v,  ixv  , Ausruf  gepreßten  Schmerzes',  lat.  mü  facere^  mutmut facere  ,mucksen'.
2.  ai.  mnka-  ,stumm',  arm.  mwnj  , stumm',  gr.  ftCxdg,  (.(VTig,  uvTTÖg,  j^vSog, ^wagögf  Hes.  (j^vvöög  ,stumm',  lat.  mütus  ,st,umm';  vgl.  auch  älter  dän. muej  norw.  mua  ,schweigen,  nicht  mucksen';  ahd.  mäwen  , schreien',  lett. maunu,  mäwu^  maüt  , brüllen',  cech.  myjati  , muhen';  hierher  auch  nhd. Möioßj  ags.  rriziOj  meWy  aisl.  mär  (PL  mävar),  as.  meu  ds.
3.  [Ai.  mukhd-  n.  ,Mund'  stammt  aus  dem  Davidischen];  gr.  ^vXXov ^Lippe';  fj,vXXaivo)  , verziehe  den  Mund,  schneide  Gesichter'  (fxvara^  , Ober- lippe, Schnurrbart',  s.  Boisacq  m.  Lit.),  ahd.  mala  f.,  mhd.  mül  n.  ,Maul', mnd.  müle  ,Maul,  Schnauze',  aisl.  müli  ,Maul,  bes.  Oberlippe  an  Tieren, hervorragende  Felsspitze',  got.  faurmüljan  ,das  Maul  zubinden'  (ob  mit anl.  s-  dazu  norw.  smaul,  lett.  smaule  ,Maul'??);  s.  auch  unter  möu-lo- S.  750.
4.  Mit  dentalen  Formantien:
ludiX.  muttiö,  -Ire  ,mucksen',  muttum  nullum  ,keinen  Muckser'  (vgl.  oben mutmut) ;  ahd.  mutilön  jmurmeln^,  rieseln*,  müsse  , Quelle',  aisl.  mudla  ,mur- meln*,  daneben  mit  germ.  t:  norw.  dial.  mutra,  mengl.  muteren,  engl. mutter  ds. ;  lit.  mute  ,Maul*.
5.  Gutturalerweiterungen  (vgl.  oben  2.):
Mit  k:  gr.  [,iVycdo^aL  ,brülle*,  ixvx&iC^a)  ,schnaube,  spotte',  mhd.  mühen, mügen,  müwen  , brüllen',  abg.  myH  ,Gebrüll',  russ.  mycath  ,brüllen*,  skr. slov.  öech.  mukati  ,brüllen*.
Mit  g:  ai.  münjati,  möjati  ,gibt  einen  Ton  von  sich*  (Dhätup.);  mucchanä »schwellender  Ton* ;  gr.  (j,vKco  ,bringe  mit  geschlossenen  Lippen  einen  Laut hervor,  stöhne*  (daraus  lat.  mussäre),  iivyy
```


### [2026-09-07T18:18:46.608Z] TOOL RESULT

```
705:DNa 22. amánaya DB 2.48, 2.63; amanaiya DB 2.28. paradraya DNa 28f; paradraiya A?P 24 (cf. draya,
1254:pàr. root kar- ‘make, do’, OP pres. kunautzy, imf. pass. akariya, züra-kara- ‘evil-doer’; but *ker- in pres. inf. cartanaiy, *kér- in ucdram ^well- done, successful’, *be-kr- in perf. opt. caxriyd.
1519:*peik- ‘cut’ in ni-paiStanaiy ‘to inscribe’; *pik- in pte. ni-piStam ‘inscribed’,
1634:(2) pAr. palatalization of velars before palatal vowels, giving an alternation in OP k/c, g/j ($78.11): Maka Maciyà, kunautiy kartam car- lanaiy, kašciy cisci, drauga draujana adurujiya, pard-gmala ha"gmalà à-jamiyü.
1806:Expressing abstracts (actions): fem. fra-má-nà-, loc. adv. aS-naiy, adj. *u-rada-na-, yà-na-, vaš- na-, ham-ara-na-; possibly fem. Patt-graba-né-, becoming a place-name.
2544:navinaiy, 3d sg. kunavatazy. var-, pres. varnay(a)-: varnavátauy. xsnav-, pres. zinav(a)-: ü-z5navàhy. kan-, pres. kan(a)-: vi-kandhy (and -àh*-di$). jan-, pres. jan(a)-: perhaps (restored) 3d pl. vi-
2559:It is to be noted that certain of these endings cannot be distinguished in the OP syllabary. The endings -ti -tai -nti are all written -2°, though normalized -tiy -taty -"tzy on the evidence of the context or of other forms of the same verb; -ta and -nta are both written -Ёа, and normalized -tă and -^là; -s -t -nt are all unrepresented in the writing if preceded by -ã-, though, like the n in -nti and -nia, they may optionally be represented by raised letters in the normalization. The subjunctive end- ings -ni and -nat also are both written -nzy’, though normalized -niy and -naiy. Further, the Aryan change of both pIE e and pIE o to a makes it impossible to distinguish the quality of the the- matic vowel by citation of Aryan forms merely; for this purpose, Greek cognates have been cited.
2608:$238. THe INFINITIVE occurs in OP only in the present active, with the suffix -tanazy, the ancestor of the NPers, infinitive ending -tän or -ddn: carta- naiy ‘to do’, to kar-; ka*tanaty ‘to dig’, to kan-, cf. NPers. kdndén; bartanaiy ‘to bear’, to bar-; тїраї {апаш ‘to engrave’, to nt-paid-. The c- of cartanaty is evidence for the -e- ablaut-grade in this formation ($98); NPers. kárdün ‘to do’ has k- gen- eralized from the rest of the paradigm.-In form,
2610:the -tanaiy is dat. sg. of а -tan- stem (other forms of -an- stems! occur as infinitives in Indic and elsewhere, which makes it unlikely that -tanaty is loc. sg. of а -lana- stem).
2647:The same formation probably stands also in the adv. a’naiy (see Lex. s.v.).
2696:G. Ав dative of indirect object, in DB 1.12 Auramazdá хёасат manā frübaro, DB 1.81f kürahy& naiy azdà абага ‘it was not known to the people’, DB 1.75 kdrahyd агава afaha, DSa 5 nsahyd frasam badaydtary.
2819:ПІ. A descriptive adjective is likewise incor- porated within the clause, in DB 2.30f (and 2.50f) kāra hya hamiçiya mana лашу gaubataiy ‘the hos- tile army which does not call itself mine’; but such adjectives usually stand outside, as in DB 2.84 küram hamiciyam hya тапа naiy gaubdtaiy, cf. also DB 2.21, 3.86.
3496:48 v :xšāyaðiya :abava —— :08tiy : Dàrayavaus : xSayafiya : naiy : aha : martiya : 49 naiy : Разза : naiy : Mada : пазу : amàxam : taumáyà : kaSeiy : һуа : avam : Gau 50 matam : буз : magum : xSacam : ditam : caxriyà : kiraSim : hac& : багат : а 51 tarsa : kàram : vasiy : av&janiy& : һуа : paranam : Bardiyam : adánà : avahyar 52 айу : кагат : avájaniyà : mátyamà&m : xénàsátyy : tya : adam : naiy : Bard
3526:71 5: vilam : {уйт : amáxam : naiy : рагабага
3541:94 cartanaiy : pasiva : hamaranam : akumá : Auramazdámaiy : upastüm : abara : vašnā : Aurama 95 zdīha : küram : tyam : Naditabairahyd : adam : ajanam : vasiy : aniya : üpiyá : уай : à
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3594:51 hya : hamiciya : mana : naiy : gaubataiy : avam : jadiy : pasiva : Vaumisa : a
3610:67 gaubatà : ài$ : hadā : kara : patiš : mim : hamaranam : cartanaiy,: pasáva : hamarana
3619:76 dra : avaina : pasivasim : Hagmatànaiy : uzmay&patiy : akunavam
3627:84 dram : hamigiyam : һуа : mana : naiy : gaubataly : avam : jatà : pas
3718:36 hada : kara : patiš : Artavardiyam : hamaranam : eartanaiy : pas
3743:60 va : tyam : Vahyazdata : früisaya : abiy : Vivànam : hamaranam : cartanaiy : К 61 āpišakāniš : nàmà : didà : ауада : hamaranam : akunava : Auramazdimal _
3841:47 m [ауа : ahy&y& : dipiyàf: палу : nipistam.: avahyarádiy : naiy : n
3849:55 hadugàm : naiy : apagaudaydhy : kürahy& :8àhy : Auramazdà : fuvām :
3857:63 yàha : bagitha : tyaiy : hatiy : yaf : палу : апка : Sham : пау : draujana : арат : na 04 iy : zürakara : &ham : поту : adam : поталу : tauma : upariy pev omis ~ 65 yam : naiy : škaurim : naiy : tunuvatam : züra : akunavam : martiya : һуа : hamata 66 xšatā : manā : vityà : avam : ubartam : abaram : hya : viyanüfaya : avam : ufrasta 67 т: aparsam | : фу : Юйгауауац$ : xSayafiya : tuvam : К : xšāyaðiya :
3863:73 diy : imam : dipim : vainühy : imaiv& : patikarà : naiydis : vikanahy : uta
3896:WB, from Wb.'s reading of Rl.s squeezes, add the fol- lowing, also in roman, which were not visible to KT, nor to RI.: ! абаһа : adam; ** draujana ; 5 apagaudayihy; " miyapaiBam : imaivd; ^ ahatiy; 78 iaumá : ahatiy : naiydis; 9 алаа; ** Vàyaspàrahya; % puça : Pārsa : Gaubarusa; * puça : Рагва : Vidarna; 9 g&bignahy& : puça; 95 Bagabuzsa; * Ardumanis : nàma : Vahaukahyá : puça; 9? kå : z5agafiya.
3949:14 uS: mand :abava — :98tày : Dürayavaus : xSdyahi 15 ya : avaiy : Uvjiya : ariká : dha : utāšām : Aurama 16 zdà : naiy : ayadiya : Auramazdém : ayadaiy : уара : А 17 uramazdéha : уада : mam : Ката : avabadi§ : akunavam |. 18 : вайу : Dérayavaués : xSdyadiya : hya : Auramazda 19 m : yaddtaty : yàvà : іаита : ahatiy : ша : jivah
3951:23 y : pasdva : уаба : adam : апау : abiy : draya : a 24 vürasam : avadà : hadd : Ката : pis : viyatara 25 yam : pasiva : adam : Saké : vasiy : ajanam : aniyam : aga 26 rbdyam : haw : basta : anayalà : abiy : mam : ut 27 ükim : avdjanam : maBiSstaSüm : Skuxa : nàma : avam : aga 28 rbdya : wd : anaya : abiy : màm : avadà : aniyam : таб 29 iam : akunavam : yaéd : тат : ката : dha : pasàva : da 80 hyüu$:manà:abava : Patty : Dàrayavaus : xšāya 91 буа: араш : Saka : атка : Gha : uti :naiy : Auramazd 32 asam : ayadiya : Auramazdam : ayadaiy : vasna : Aurama 33 zdüha : yaðā : mim : Ката : waðādiš :akunavam —— :08t 34 iy : Dárayavaus : z5àyatrya : hya : Auramazdim : yadata 85 iy : ydvà : taumā : ahatiy : utà : jivahya : uta
4126:10 : naima : ava : kàma : tya : tunuvā : skaudais : r 11 афу : mia : kariyai$ : tya : rástam : ауа : mam : 12 kama : martiyam : draujanam : naiy : dausté : 4m 18 iy : naiy : manauviS : ату : (yàmaiy : dartana 14 ya : bavatiy : darsam : dárayàmiy : manaha : 15 uvaipasiyahyà : darsam : xSayamna : amy : 16 martiya : hya : hataxSataiy : anudim : hakarta? 17 hyà : ауадай : paribaráàmiy : hya : 0° 18 máfayatiy : anudim : vinastahyd : ava
---209---
```


## [2026-09-07T18:18:54.286Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=418 && NR<=422 {print \"=== leaf \"NR-1\" ===\"; print}' POK_02.txt | head -160",
 "description": "POK leaves 417-421"
}
```


### [2026-09-07T18:18:55.648Z] TOOL RESULT

```
=== leaf 417 ===
(Nom.  näuh)  , Schiff,  Boot'  (nävya-  .schiffbar');  ap.  näviyä , Flotte'  (:  gr.  vriioq  ,zum  Schiff  gehörig');  näväja-  m. , Schiffer',  av.  navaza-  ds. (:  gr.  vav-rjyög  ds.,  vgl.  auch  lat.  nävig-äre,  -ium)-,  av.  nävaya-  , schiffbar' (über  ai.  ati-nu  s.  Brugmann  11^  137  Anm.  2);  arm.  nav  , Schiff'  (aus  dem Pers. ?);  gr.  hom.  vtjvg,  vrjög  {*vaf6g),  att.  vavg,  vscbg  , Schiff';  lat.  nävis  ds. (ursprüngl.  kons.  St.,  vgl.  Akk.  navem  =  ai.  nävam,  gr.  vfja) ;  air.  ndu  (Gen. nöe,  Dat.  PL  nöib)  , Schiff';  cymr.  noe  , flaches  Gefäß,  Backtrog',  bret.  neo ds.  (*näuia)]  hierher  gall.  (vorrom.)  navä  , Talschlucht',  auch  FIN;  gall. nausum , Schiff';  aisl.  nör  m. , Schiff',  nau-st  , Schiffsschuppen',  nöa-tün  (nöa  = gr.  viywv)  , Schiffsburg',  ags.  nöwend  , Schiffer',  (aber  mhd.  näwe,  ncdwe ,kleines  Schiff',  nhd.  dial.  iVawe  aus  dem  Lat.) ;  norw.  nö  ,Trog  aus  einem ausgehöhlten  Baumstamm',  nela  (*nöwilön-)  ,großer  Trog,  schweres  Boot',
48*
756
ahd.  nuosc,  mhd.  nuosch  m.  ,Trog,  Rinne',  afries.  nöst  ,Trog'',    mnd.  nöste  i
, Viehtrog',  Wassertrog' ;  hierher  der  lit.   FIN  Nova,  polonis.  Nawa.  -M
WP.  II  315,  WH.  II  148  f.,  J.  Hubschmid  R.  int.  d'Onom.  4,  3  ff.  ^;
2.  näu-  :  nou-  :  nü-   A.  ,Tod,   Leiche',    B.  ,bis   zur   Erschöpfung  abquälen.
ermattet  zusammensinken';  näuis  , Leiche'.  :
A.  Got.  naus  , Leiche*  {ga-nawiströn  , begraben*),  aisl.  när  ds,,  ags.  ntU) m.  ds. ;  aruss.  navh  , Leiche',  aöech.  ndv,  -i  m.  ,Jenseits,  Hölle',  lett.  ndwt ,Tod',  davon  ndwet  , töten',  näwities  ,sich  mühen,  sich  töten';  apr.  nowig ,Rurapf'.
B.  air.  7iüne  (älter  naunae)  f.,  cymr.  newyn  m.  ^Hungersnot'  (*w9w,mo-)  ;. bret.  naoun  (^ndu^no-)  ds. ;  mcymr.  neued  , Sehnsucht,  Not*  {*näu-ita) ;  lett.  i' ndwUies  (s.  oben),  lit.  novyti  , quälen,  töten',  is-novyti  , vernichten';  Kausat.  "^ aksl.  cech.  unaviti  , ermüden'.  Postverbal  cech.  ünava  , Ermüdung',  russ.  ^- dial.  ondva  , Müdigkeit',  schwundstufig  aksl.  unyti  ,schlaff  sein,  erschlaffen',  '^ öech.  nyti  ,dahinschmachten',  russ.  nyth  ,schwermüti^  werden'.  %
nou-ti-  in  got.  naups  f.  ,Not,  Zwang',  aisl.  naud,  naudr  f.  ,Zwano'  - Drangsal,  Notwendigkeit',  as.  nöd,  ahd.  not  ,Bedräng'nis,  Drangsal,  Not', ags.  nead-,  med  f.  ,Not,  Pflicht,  Drangsal';  apr.  nautin  (*näuti-)  (Akk.) ,Not' ;  im  Slav.  Formen  mit  u  und  g,  t  und  d  (s.  Meillet,  Slave  commun^ 61  f.):  aksl.  nqzda  , Zwang,  Gewalt,  Notwendigkeit'^,  poln.  n^dza  ,Not', abg.  ngditi  ,nötigen',  aber  auch  aksl.  nuzda  , Zwang,  Not',  nuditi  ,nötigen', poln.  nuda  , Langeweile';  mit  t  poln.  net  , Lockung',  bulg.  nut  , Zwang', poln.  nucic  (16.  Jhdt.)  , zwingen';  das  -d-  steht  als  idg.  Erweiterung  neben -t-,  das  
=== leaf 418 ===
g  ist  durch  sekundäre  Nasalierung  entstanden.
WP.  II  316,  Trautmann  201  f.;  Loth  RC  45,   199 ff.
I.  xze,  ne,  nei  Satznegation  der  reinen  Verneinung  (ne  einzelsprachlich  auch   * Wortnegation   geworden);   n-  Wortnegation;  ne-k"o-s  , nicht  einer', nei-k^o-s  ds. ;  ne-k^e  ,und  nicht*,  ne-ue  ,oder  nicht*. ne:  ai.  nd  ,nicht',   ned   (iidid)   ds.,   av.  ap.  na-  ,nicht',   av.  nöit  (=  ai. ned),  ai.  nd-vä  =  av.  na-va  ,oder  nicht'  (vgl.  lat.  ne-ve,   und  genauer  air.  nö s.  unten) ;  ai.  naca  ,und  nicht'  (=  lat.  neque  usw.) ;
über  ne-  im  Arm.  {nual  ,langmssant'  aus  *ne-val-,  usw.)  s.  Dumezil BSL.  40,  48  f. ;
gr.  vB-  nur  (als  Ersatz  von  n-)  vor  verbalen,  dann  auch  andern  Adj. mit  dem  Anlaut  a,  I,  o,  mit  denen  es  kontrahiert  ist,  z.  B.  vTjy^saTog,  vrjXsrjg, rcüvu|u(>')os  (danach  sekundäres  vrj-  in  vrjTtoLvog  ,ungerächt',  dor.  värtoivog, usw.);
lat.  n^-  in  ne-fäs,  ne-sciö  (ne-sciens,  ne-scius),  ne-cesse,  ne-uter,  n'unquam, nusquam,  nüllus,  nön  (*n'oinlom'],  vgl.  ahd.  nhd.  nein),  ne-que  ,und  nicht,
757
jedenfalls  nicht'  (=  osk.  nep,  got.  nih,  air.  na[cK]  ,nicht^  ai.  na-ca),  osk. ne  ,non,  ne';  vgl.  auch  lat.  neg[äre,  -ötium']  oben  S.  418;  lat.  neu,  ne-ve, ^It  neive,  nlve  ,oder  nicht' ;
air.  oie-ch  ,aliquis^  cymr.  nep  ,quispiam'  (=  ai.  najcis  ^niemand',  aber mit  Abstreifung  des  negativen  Sinnes  in  Sätzen  mit  wiederholter,  aber einander  nicht  aufhebender  Negation ;  derselbe  Vorgang  in  lit.  nekas  ,irgend etwas^  nekurh  ,quidam',  usw. ;  ähnlich  gelangte  ne-ue  ,oder  nicht'  zur positiven  Bed.  ,oder'  in  :)  air.  nö,  nü,  cymr.  neu,  abret.  nou  ,oder',  auch verbale  Stützpartikeln  (für  Pronomina  infixa  und  das  relative  -n-)  air. no-,  nu-,  mcymr.  neu-  als  ursprüngl.  formelhaft  vorgesetztes  ,oder  nicht?'; proklitisches  *ne  ergab  *na  (wie  z.  B.  ir.  ass-  ,ex')  im  Vorton  in  der Verbindung  air.  na\_Gh],  mcymr.  nac  (usw.)  ,nicht'  aus  ne-k^e  mit  urkelt. Apokope(?)  des  ausl.  -e;
got.  ni,  ahd.  as.  ni,  ne,  ags.  ne  , nicht';  aisl.  ne  in  der  nur  poet.  Bed.  ,non', während  ne  in  der  Bed.  ,n^que'  ==  got.  nih  (gleichbed.  mit  ni  geworden) aus  *ne-k^e  =  ahd.  nih-ein,  as.  (mit  gramm.  Wechsel)  nig-en  ,kein'  (aber as.  nee  ,und  nicht'  ==  lat.  neg-^  s.  oben  S.  418) ;  ahd.  Konjunktion  noh  ,noch' aus  *neÄ  (^ne-k^e)  oder  aus  ne  +  ahd.  ouch  ,auch' ;  ahd.  nein,  as.  nen  ,nein' aus  *ne  +  oinom  , nicht  einer'  (s.  oben  lat.  nön,  nüllus);  ags.  nä  ,me,  nicht, nein',  engl,  nö  ,nein'  (auch  aisl.  nei  ,nein'  aus  *ni  +  aiw  =  as.  ahd.  nio ,nie') ;
apr.  ni,  lit.  ne  , 
=== leaf 419 ===
nicht',  nekas,  nekurls  (s.  oben);  aksl.  ne  ,nicht';
hitt.   natta  ,nicht*,  näwi  ,noch  nicht'.
ne:  ai.  (ved.)  na  ,nicht';  lat.  ne  , nicht'  in  ne-quidem,  nequäquam,  nsqm- quam,  nequam,  gekürzt  wahrscheinlich  in  neutiquam  (aber  ne-uter  mit altem  *ng,  s.  oben),  ne  Konj.  ,daß  nicht',  osk.  ni  ,ne'  (nz-p  ,neve'),  marruc. ni  ,ne';  air.  ni,  mcymr.  ny,  ncymr.  ni,  corn.  ny,  bret.  ne  ,nicht'  (z.  T.  mit sekundärer  Kürzung);  air.  nl  ,ist  nicht'  ist  das  gewöhnliche  nl  mit  aus- gelassener Kopula;
got.  ne  ,nein'.
12 ei  betontes  ,nicht':  av.  nae-cis  ,keiner',  adv.  ^laecis  verstärkte  Negation; lat.  7ü,  altlat.  nei  Adv.  und  Konj.  1.  älter  ,nicht,  daß  nicht',  2.  ,si  non', quid-nl-,  osk.  nei  ,nicht'  (nei-p  ,neque');  got.  nei  {&TC.ley.)  ,nicht^  aisl.  nl ,nein',  ahd.  nl  emphatisches  ,nicht';  lit.  nie-kas  ,niemand',  ne%  ,auch  nicht, nicht  einmal' ;  aksl.  ni  ,neque',  ni-Uto  ,niemand' ;  die  germ.  Formen  viel- leicht aber  =  ai.  ned  ,durchaus  nicht,  damit  nicht',  av.  nöit,  ap.  nay  aus idg.  *ne  id  ,das  nicht';  vielleicht  ist  idg.  nei  aus  *ne-\-l  (vgl.  ovtoa-l)  zu deuten.
h-  Verneinungspartikel  als  erstes  Glied:  ai.  av.  ap.  a-,  vor  Vokalen  (auch i,  u)  an-',  gr.  ä-,  vor  Vokal  a»'-;  lat.  in-,  ältest  en-  (die  vorkonsonantische
758  '
Form);  osk.  umbr.  an-;  air.  in-  (vor  Med.),  e-  (vor  Tenuis),  an-  (y^  ' Vokal),  cymr.  com.  bret.  an-]  got.  ahd.  as.  ?m-,  aisl.  ö-,  ö-;  im  g^i durchaus  durch  ne-  verdrängt;  über  ksl.  ne-je-veTb  , ungläubig',  '^^-je-sytt, ,unersättlich  =  Pelikan'  s.  Berneker  429;  toch.  AB  a(w)-,  am-^  efnV em-,  071- ;  durch  mehrere  Sprachen  durch-gehende  Entsprechungen  sind  z.  B  » ai.  amfta-,  ^(.ißgoTog,  immortalis]  ai.  djnäta-,  Hyrcorog,  arm.  ancanaut' ignötus,  air.  ingnad,  got.  unJcunps]  ai.  anudrd-,  äwögog,  usw.
WP.  II  319f.,  WH.  II  150f.,  152,  165f.,  Trautmann  194f.,  Schwyzer Gr.  Gr.  1,  431  f.,  2,  590  ff.
:2.  22e,  ne,  enklit.  Partikeln  s.  oben  S.  320  f.
5.  ne-,  no-,  Plur.  nes-,  nbs-  ,wir'  (ursprüngl.  außerhalb   des  Nominativs* Nom.  s.  unter  *we).
1.  Ai.  Du.  Akk.  Dat.  Gen.  nau,  gthav.  G^n.  nä,  aksl.  nä,  gr.  yw,  hom. ywt  aus  *v(ü-J^t  (dessen  2.  Glied  der  Nominativst.  *ue-,  *id-  ist) ;  air.  nä(tha)r  ^ Gen.,  got.  ughis,   as.  wwc,   anord.   o^Är  ,uns  beide  (n)'  (unc  =  *n-ge,  vgl. mik  aus  *me-ge).
2.  Pluralisch:  ai.  waA  enklit.,  av.  W9,  nä,  nö,  lat.  nös,  alb.  na  Nom.  (*nd«), Tie  Gen.  Dat.  Akk.  (*nös);  ir.  ni  usw.  (scheint  *s-7ies).  Gen.  ar  n-  (*ns-rö-m),  ~" cymr.  corn.  bret.  ni,  ny  ,wir'  (*we5),  got.  ahd.  uns, 
=== leaf 420 ===
 as.  w«,  anord.  oss  ,uns' (*ns),   aksl.  nas^  Gen.  (j^nös-söm),  apr.  nöuson  (ebenso) ;  £■_
auf  *nsme  (wohl  ns  -j-  Partikel  *sm-,  verwandt  mit  dem  -sm-  der  Pron.- Dekl.,  z.  B.  ai.  td-sm-ät)  beruhen  av.  ahma  (ai.  asmän,  ap.  Gen.  amäxam) =  äol.  ^'^u^-,  dor.  ö^-,  ion.-att.  ij^u- ;  Poss.  lesb.  ä^(j,og,  dor.  ß^iog  =  av. ahma-,  ion.   -att.   'fj^hsgog)  usw. ;   hitt.  Datt.  Akk.  anzäs,   enkl.  was  ,uns*.
WP.  II  320  f.,   Schwyzer  Gr.  Gr.  1,  600  f.
I.  nebh-  ,bersten'??
Ai.   ndhhate  , birst';    aisl.  ncefr  ,die  äußere  Birkenrinde'  als   ,berstend, sich  losschälend'. WP.  II  330.
2.  nebh-  s.  oben  S.  315  f.
I.  ned- ;  zicd-  , zusammendrehen,  knüpfen';  i2Öcfo-/-ä  , Geknüpftes'.
1.  Lat.  nödus  , Knoten'  (idg.  *nödos)',  vermutlich  nassa  (*nad-s-a)  , Fisch- reuse, geflochtener  Korb  mit  engem  Halse';  nectö,  -ere,  nexl,  nectum ,knüpfen,  binden'  ist  Neubildung  nach  j^Zec^ö;  mit  der  Bed.  ,nahe'  aus  ,eng verknüpft' :  osk.  nessimas  Nom.  PL  f.  ,proximae',  umbr.  nesimei  ,proxime';
air.  Kompar.  nessa,  Sup.  nessam  ,propior,  proximus',  cymr.  nes,  nessaf, corn.  nes,  mbret.  nes,  nessaß  ds. ;  air.  nascim  ,binde,  verpflichte*  (*n^d-sJcö),
759
arrienas  ,1  will  bind'  (usw.),  naidm  ,das  Binden,  Vertrag-^  for-naidm  ,Band^ nasc  ,Ring'  (^S^-  zur  -sÄ-Bildung  ahd.  nusca^  das  auch  im  u  =  ,  überein- stimmt^ ferner  av.  naska-  ,Textsammlung',  wahrscheinlich  eig.  ,Bündel'); bret.  nasJca  ^anbinden';
got  nati,  ahd.  nezzi,  as  net,  netti,  ags.  aisl.  net  ,Netz%  dehnstu%  (wie lat.  nödus),  aisl.  not  f.  ,großes  Netz';
mit  formantischem  -s-k-,  -s-t- :  ahd.  nuska,  mhd.  nüsche  ,Mantelschnalle', as.  nusk(i)a  , Spange'  (s.  oben);  aisl.  nist,  nisti  n.  , Spange  am  Kleid',  nista ^zusammenheften';  nesta  , festheften,  festnageln',  mhd.  nes^en  (nesteln)  , fest- binden" schnüren',  ahd.  nestilo,  nestila  ,Schleife,  Schnürriemen,  Binde', nhd.  Nestel,  as.  nestila  , Binde,  Haarband',  agutn.  nast,  nestli;  reduktions- stufig ags.  nos(t)le  ,Band';
daß  ned'  eine  Erw.  von  (s)?ie-  ,zusammendrehen'  sei,  wird  außer  durch die  Bed.  auch  durch  die  s-anlaut.  Formen  air.  snaidm  , Knoten'  (vgl. oben  naidm)  und  nhd.  hess.  Schnatz  ,das  geflochtene  und  um  die  Haar- nadel gewickelte  Haar  der  Frauen,  Kopfputz  der  Bräute'  (*snatta-  mit srerm.  -tt-)  wahrscheinlich.
2.  Hierher  vermutlich  die  Bezeichnungen  der  Nessel  (als  alter  Gespinst- pflanze) :
Gr.  didiyL7]  {*nd-ikä) ;  ahd.  nazza,  aisl.  nqtr,  ahd.  nezzila  (germ.  *natilön), ags.  netele]  daneben  mit  idg.  -t-  (also  *n9-t-,  nö-t-  als  ^Erw.  zur  vermut- lichen Wurzel  (s)ne-)  apr.  noatis,  lit.  notere,  notre  , Nessel',  nötryne  ,Taub
=== leaf 421 ===
- nesseP,  lett.  ndtrCj  nätra  ,Nessel',  slav.  *nat'b  , Krautblätter'  in  slov.  nät (Gen.  nati),  poln.  nac  ds.  und  allenfalls  (als  redupl.  urkelt.  *ni-nati-?) mir.  nenaid,  nir.  neantög  ,Nessel',  dissimil.  bret.  linad  ds. '  WP.II  328  f.,  WH.n  144  f.,  155  f.,  172  f.,  Trautmann  194,  H.  Jacobsohn Arier  u.  Ugrofinnen  90 f.;  s.  unter  (s)we-.
2.  ned-  ,tönen,  brüllen,  rauschen'.
Ai.  nddati  ,tönt,  brüllt,  rauscht',  nada-  m.  ,Brüller,  Stier,  Fluß*,  nadi- f.  ,Fluß,  Flut',  nadl-na- m.,  nadl-sa-  m.  ,Meer',  usw.;  av.  wacZ- , schmähen'; gr.  (illyr.)  FIN  Neda  (Arkad.),  Nedwv  (Messen.);  thrak.  FIN  NeOTog] illjr.  FIN  Nearog  (Dalm.)  aus  *ned-to-.
A.  Mayer  Mel.  Boisacq  II  132  f.,  Krabe  IF.  58,  209  ff.
nedo-  ,Schilf'?
Ai.  nada-  m.  vermutlich  , Schilfrohr',  npers.  nai,  dial.  nad  , Schilf;  arm. net    ,Pfeil';   lit.    nendre   (und    Undre)   ,Schilfrohr'   (mit  Nasal   nach    lenkti ,biegen'?);    lett.  nasli  , Schilf  aus  *nadslis? WP.  II  329 ;  vgl.  Kuiper,  Proto-Munda  82.
760  •
negh-  , durchbohren,  stechen'.
Mir.  ness  , Wunde'  {*negh-8-)]  reduktionsstufig  aksl.  v^-nhzq  , steck hinein',  Infin.  v^-nhzngt^,  Kaus.  russ.-ksl.  v^-noziti  , hineinstechen'-  aksl nozh  , Messer';  ob  hierher  ai.  dhsu-  , Stange'  (*ngh-su-)?
WP,  II  326  f.,  Trautmann  200.
1.  nei-,  neio-ini-  , führen'.
Ai.  ndyati  (Partiz.  nltd-),  av.  nayeiti  , führt',  mpers.  nltan  , führen treiben',  ai.  nlthä  f.  , Führung,  Weg',  nltho,  netä^  ,Führer',  nitar-,  netdr- m.  ds.,  netrd-  n.  , Führung,  Auge';  mir.  ns,  nla  ,Krieger,  Held'  {*neit-i\ Gen.  Sg.  urir.  netas,  air.  niatJi  {*nei-t-os\  s.  auch  2.  nei-)]  hitt.  näi-,  lenken führen'.
WP.  II  321,  Pedersen  Hitt.  §  77  f.,  81,  Frisk  Suffixales  -th-  öf.
2.  nei-,  neis-  :  ni-  , lebhaft   bewegt   sein,    erregt   sein,   glänzen';    noi-bho-^
,gut,  heilig';  kelto-germ.  nei-to-,  ni-tu-  , Leidenschaft'.
Lat.  niteö,  -ere  ,glänze,  strahle',  nitidus  , glänzend',  nitor  ,  Glanz'  (von einem  Partiz.  *ni-tö-) ;  vielleicht  re-nldeö  , erglänzen'  (mit  präsensbildendem -d(hy)]  *nei-bhO'  in  mir.  nlab  , Lebenskraft',  cymr.  nwyf  ds. ;  noi-bho- in  apers.  naiba-,  npers.  new  , schön,  gut',  air.  nolh  , heilig';  *nei-mä  in mir.  nlam  , Glanz,  Schönheit';  *nei-Jco-  in  mir.  mach  m.  ,Held',  nlachus m., Tapferkeit';  *nei-to-  in  cjmr.  nwyd  , Leidenschaft',  hispan.  Kriegs- gott Netö]  air.  PN  Nlall  (Gen.  NeiU)  aus  *neit-s-lo-s]  steckt  vielleicht auch  in  air.  ma  ,Held'  (s.  1.  nei-)]  germ.  ^nipa-  in  got.  neip  n.  ,Neid', ags.  m(J  m.  , Kampf,  Haß,  Feindschaft',  as.  afries.  nith  , Eifer,  Haß,  Neid\ aisl.  nid  ,Hohn,  Schmach';  könnten  auch  zu  air.  nlth.  n.  (idg.  *i2ifu-) ,Kampf  gehören;  zweifelhaft  ai.  nila-  , schwarzblau',  naya
```


## [2026-09-07T18:19:09.208Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 405 406 256 257; do echo \"=== POK_02 leaf $((n-1)) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt | head -40; done",
 "description": "POK 594 and 743"
}
```


## [2026-09-07T18:19:10.060Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 182 183 224; do echo \"=== KNT leaf $((n-1)) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -60; done",
 "description": "KNT 167 and 209"
}
```


### [2026-09-07T18:19:11.663Z] TOOL RESULT

```
=== POK_02 leaf 404 ===
.  mos,
ags.  meos  ,Moos,  Mies',  aisl.  myr-r  f.  {*meuz-i-)  ,Moor,  Sumpf;  lit.  müsaX m.  PI.  , Schimmel  auf  saurer  Milch',  ablaut.  müsos  f.  PL ;  abg.  m^chb ,Moos'  (*musos),  nbulg.  much^l  ,Schimmel';  dazu  vermutlich  arm.  mamur ,fucus,  alga,  muscus,  situs'  (^memus-ro-).
5.  Mit  formantischem  Guttural:  lat.  muscus  m.  ,Moos';  norw.  dial.  musk ,Staub,  feiner  Regen,  Dunkelheit',  dän.  dial.  musk  ,Schimmel',  mndl.  mosch, mosse  ds. ;  aksl. ;  muzga  (*mouz-ga)  ,Lake,  Weiher',  russ.  mzgnuth  ,verderben', mozgnutb  , abmagern',  abg.  m^zditi  ,schwächen',  russ.  mozg^  ,regnerisches Wetter',  mozsith  ,einweichen'.
6.  meut- :
arm.  mut''  , dunkel;  Dunkelheit,  Nebel',  mt'^ar  , dunkel';  mir.  mothar ,Dickicht,  dichte  Masse',  nir.  , Sumpf  (*mutrö-  =)
mnd.  modder  , Schlamm'  =  md.  moder  , verfaulender  Stoff,  Sumpf (nhd.  Moder,  echt  nhd.  Essig-,  Weinmutter),  engl,  mother  ,Hefen'  (*mutro-)j engl,  mud  , Schlamm',  mnd.  mudde  , dicker  Schlamm'  (holl.  modde),  md. mot  (-tt-),   .Torferde,   Morast'  (schweiz.  mott  ,Torf),  ostfries.  mudden  ,be-
743
schmutzen';  muddig  ^schmutzig',  schwed.  modd  , Schneeschmutz',  dial. jntiddig  ^schmutzig';
mit  anl.  s-  mnd.  afries.  smudden  ^beschmutzen',  ndd.  smudden  ,fein regrien',  wfläm.  smodder  ,Morast',  mengl.  smod  ^Schmutz',  smudderen,  ndl. ^^tnodderen  ^schmutzen',  älter  ndl.  auch  ^schmausen'  (ursprüngl.  ^unreinlich essen  und  trinken';  so  auch  ostfries.  smUs,  nhd.  Schmaus,  älter  ndl. sjnwisteren  ^schmausen'  und  ^beschmieren',  nd.  ndl.  smullen  ^schmausen' und  ,sudeln,  beschmutzen'  wohl  aus  *smud-lön]  lit.  smütnas  ,traurig'  stammt aus  poln.  smutny  ds.  (Vasraer  brieflich).
WP.  II  249  f£.,  WH.  II  126  f.,  130,  134,  136,  Trautmann  172,  188, 190  ff.;  Specht  Indog.  Dekl.  65,  257  f.
2,  meu~,  meuQ-  (arisch  z.  T.  auch  mieud-  :  mlu-)  ,fortschieben'.
Ai.  mivati  ,schiebt,  drängt,  bewegt'  =  av.  ava-mivämaJii  ,wir  beseitigen, nehmen  weg',  ar.  a-muyamnö  ;Unbeweglich,  wovon  nicht  abzubringen'; ai.  kdma-müta-  ;Von  Liebe  bewegt',  mürd-  ;drängend;  eilend';
gr.  d^svoaad'aL  jVorankommen,  übertreffen'  (wohl  aus  ,sich  vorschieben')^ gortyn.  dfxsJ^vaaad^ai  ;Handel  treiben',  äfitvo)  ,wehre  ab'.  Med.  ,verteidige mich  (*schiebe  weg)',  ^{.ivvtüjq  ;Abwehrer;  Rächer';  f.t'övaa&ai  ;Vorschützen'; fj.tvrj  , Vorwand,  Ausflucht';  vgl.  air.  mün-  ,unterrichten'  (E.  Lewy);
lat.  moveöj  -ere  ,in  Bewegung  setzen,  bewegen  (ursprüngl.  durch  Fort- schieben)', Partiz.  mötus  (^movi-to-s)  =  umbr.  comohota  Abi.  
=== POK_02 leaf 405 ===
Sg.  f.  ,com- mota' ;
lit.  mdujUj  mduti  ,aufstreifen,  anstreifen  (z.  B.  einen  Ring  an  einen Finger)',  ix&movä  ,alles,  was  aufgestreift  wird',  ranktif,  üzmova  ,Muff' ;  mnd. mouwe  f.  ,Muff',  nhd.  hemds-mauen  , Hemdärmel'.
Eine  s-Erweiterung  scheint  *meu-s-  in  ai.  musnäti,  mösati  , stiehlt', mö?a-  ,Räuber;  Dieb',  fränk.  (Lex  salica)  chreo-mösido  ;Leichenberaubung'; s.  unten  S.  753  unter  müs.
WP.  II  252  f.;  WH.  II  116;  Trautmann  172.
;  meudh-,  znQudh-,  znüdh-  etwa  ;Worauf  bedacht  sein,  sehnlich  verlangen'.
Npers.  möja  ;Klage'  (-j-  aus  -cZ-,  vgl.:)  must  ,klage'  (st-  aus  -dhst)] gr.  ^vd-og  m.  ,Rede',  iLVd-eoixai  ,rede,  überlege';  got.  maudjan,  ga-maud- jan  ,jemanden  erinnern';  lit.  maudziii,  maüsti  ,sehnlich  verlangen',  ä'p- maudas  ,Verdruß,  Sorge';  abg.  mysh  ;Gedanke'  (*müd-slio-)]  vielleicht nir.  smuainidh  , denkt'.
WP.  II  255  f.;  Trautmann  171  f.
L  meug-  ;heimlich  und  tückisch  lauern'.
Lat.  muger  ,der   Falschspieler   beim  Würfelspiel'  (*mug-ro-s   ;lauernd'); ahd.  mühhari,  mühh{e)o  , Wegelagerer,  Straßenräuber',  muhhön  ,heimllch
744  ^
lauern;  anfallen^,  mhd.  vermüchen  ^heimlich  auf   die   Seite  schaffen^    ST>ät ahd.   mühhiläri  (zu  *müchilön),   nhd.    Meuchler,   mhd.   miuchel   ^heimlich' ahd.    müh-heimo   ^Grille^,    ablaut.   mhd.  mocken  ^versteckt   liegen',  men^l* micJier  ,Dieb^,  engl.  dial.  to  mich  ^versteckt  sein,  stehlend
WP.  II  255,  Wissmann  Nom.  postverb.  137;  wohl  zu  Folgendem.
2.  meug-y  meuk-,  auch  mit  anlaut.  s-:  A.  ,schlüpfen,  schlüpfrig^,  daraus ,schleimig,  Schleim';  andererseits  B.  , darüber  streichen,  gleiten,  ent- gleiten'; muk-to-  , weich',  muk-ti-  ,Entgleiten'.
A.  Lat.  mücus  ,Schleim',  mücor  , Schimmel',  e-mungö,  -ere  ,ausschneuzen' (übertragen  ,um  Geld  prellen');  mügil  m.  ,Schleimfisch' ;
gr.  &TCO-iivaau)  ,schneuze;  betrüge',  dTtö-f-Lv^cg  ,das  Schneuzen'  (:  lat. e-munctio)j  fj,v'/,TrjQ  ,Nase,  Nüstern',  (.iv^a  ,Schleim,  Nase'  (beruht  auf *lj,v'ii-a-ög  , schleimig',  wie  auch:)  fiv^og,  {.iv^Tvog,  ^v^cov  , Schleimfisch' (auch  aixv^cüv  mit  anl.  s-,  wie  bei  Hes.  auch  oi^voaezai
=== POK_02 leaf 255 ===
n.  Sg.  %eävTog  (^yirjJ^avr-),  neuatt.  exavaa,  Med.  episch yf,r]dfi7]v,  Pass.  iyi^rjv,  iy.av&rjVj  delph.  nTjVä  ,^vOLa\  yirjia'  Tiad-aQ^iaia  und Y,Ela  ds.  Hes.,  hom.  y,r](bdr]g  , duftig,  wohlriechend'  (von  einem  *yifjßog , Brand,  Räucherwerk'),  y,avaigy  y,avi.ia  n.  , Brand',  y,älov  ^trockenes  Holz' (*xaJ^-€Xov),   äol.  yiavaXsog  , brennend   heiß',    hom.  xrjXsog  (^-/.äJ^aXeog)  usw.;
lit.  hületi  , brandig  werden,  vom  Getreide',  küll  ,Getreidehrand'.
WP.  I  376  f.
keuh-  ,Dorn,  Dornstrauch'??
Asächs.    hio]po   , Dornstrauch',   ahd.    hiufo    ds.,  ags.  heo'pa   m.,    heope  f., engl,  hip,  norw.  Ä/wpa  , Hagebutte'; apr.  Tcaäuhri  ,Dorn'. WP.  I  380  f.
keuod-,  kud-  , schreien ;  anschreien,  schelten,  höhnen,  spotten'.
Ai.  hutsdyati  , schmäht,  tadelt',  Icutsa  , Schmähung,  Tadel',  npers.  nikü- hidan  , tadeln,  schmähen';
gr.  Y.vd(xC,o)^  -o^iai  , schmähe,  beschimpfe',  %vdayxag'  y^äxccg^  XoLÖOQiag Hes.,  y,vdayxöiJ^sva'  XoLÖOQOvixsva  Hes.;  von  einem  St.  kvöol- :  Y,vdoLi.L6g , Schlachtlärm,  -getümmeP,  y^vdoif-ielv  ,Lärm,  Tumult  verursachen',  -kvöol- doTtäv  ds. ;
agutn.  huta  , herbeirufen',  norw.  dial.  huta  , schreien,  lärmen,  einen  Hund drohend  anschreien,  verächtlich  behandeln'  (mengl.  hüterij  hüten,  neugl.  to hoot  , schreien,  jucheien'  aus  anord.  höta  , drohen');  ags.  hüsc  {*'küd-sko-)j ahd.  as.   liosc  (*küd-sJco-)  , Schmähung,   Spott,   Hohn',   ags.  hosp  , Schande,
38*
596  •
Schmach,  Beleidigung^  hyspan  ^spotten'  (mit  -sp-Suffix),  mhd.  hiuze  , frech,! munter',  hiuzen  ,sich  erfrechen'  (,*herausf ordernd  schreien'),  gehiuze,  gehuzt ,Lärm,  Geschrei,  Spott,  Hohn',  hiuzen,  hüzen  ,zur  Verfolgung  rufen'  (dazu" die  Interj.  hussa?);
mit  anlaut.  s-  (erst  nach  schallen,  schreien  u.  dgl.?)  vielleicht  meugl.  schüteii ,vociferari',  engl,  to  shout  ,laut  schreien,  rufen,  jauchzen',  aisl.  sJcüta,  sküti , Spott,  Stichelei';
abg.  Jcuzdg,  huditi  ,zugrunde  richten',  ksl.  auch  , schmähen,  tadeln',  russ. proJcüdih , schlechte  Streiche  machen,  Schabernack  spielen',  küd^  f. , Schwarz- kunst', skr.  hudlm,  -iti  ,tadeln,  verleumden',  poln.  dial.  prze-,  przy-lcudzi6 , verderben,  langweilen'.
WP.  I  378  f.
(keusp-:)  kuep-,  kusp-,  küp-,  woneben  vereinzeltes  keu{e)p',  k{e)uep^ , rauchen,   wallen,   kochen;   auch   seelisch   in  Aufruhr,  in   heftiger  Be- wegung sein'.  Aus  ku-  mehrfach 
=== POK_02 leaf 256 ===
 bloßes  k-  wohl  durch  bereits  uridg. Vereinfachung;  kup-ro-s  , erwünscht';  kuQpo-s  ^Dunst^ Ai.   hüpyati   (=  lat.  cupiö)   , gerät   in  Wallung,    zürnt',    Jcöpa-   m.  , Auf- wallung, Zorn',  Tzöpdyati  , erschüttert,  erzürnt';  cöpati  ,bewegt  sich,  rührt sich';  hapi-  (unbelegt)  , Weihrauch',  wozu  als  ,*rauchfarben'  Jcapild-,  hapUd- ,bräunlich,  rötlich',  auch  Tcapi-  m.  ,Affe';
alb.  hapitem  ,atme  schwer'  (wie  lit.  hüpuoti)]
gr.  "^aTtvög  , Rauch',  hom.  dcTtd  de  ipvx^v  iy.d7tvaaev  , hauchte  aus'  :  ytdjtvg und  KdftOQ'  Ttvev^a  Hes.,  y^y,7]q)s'  TsdT7jy,s  Hes.,  v.eyiaq)7]ÖTa  Hom.  ,aushau-  -, chend' ;  zur  Dissimilation  von  *Jcuap-no-s  zu  TcaTtvög  vgl.  Schwyzer  Gr. ' '' Gr.  I  302;
lat.  cupiö,  -ere  ,begehren'  (=  ai.  Jcüpyati),  cuppedo  =  ,cupldo',  auch cuppes  ,lüstern,  bes.  auf  Leckereien',  cuppedium  ,Näscherei,  Leckerbissen'; umbr.  Cubrar  ,Bonae^  sabin.  cuprum  ,bonum'  (,*erwünscht,  begehrens- wert' mit  passivischem  Formans  -ro-  wie  clärus  usw.) ;  vapor  , Dunst, Dampf,  Brodem',  alt  uapös  (*huapös) ;
air.  ad-cohra , wünscht'  (*-]cuprat)j  Verbaln.  accobor  (^ad-kupro-)  ,  Wunsch', Thurneysen  Gr.  139;
got.  afhapjan  (*kudb-  neben  sonstigem  *kudp-)  , ersticken,  auslöschen', afhapnan  , erlöschen'  ( :  äno-Y.aTtvo)),  mhd.  verwepfen  , kahmig  werden,  vom Wein',  nisl.   hvap  ,dropsical  flesh';
lit.  kväpas  m.  ,Hauch,  Dunst,  Wohlgeruch'  (:  lat.  vapor),  kvepiü,  -Ui , duften'  (-g-  kann  balt.  Ablautneubildung  sein),  kvepiü,  kvlpti  ,hauchen', lett.  kvept  ,qualmen',  kvepes  PI.  ,Hauch,  Qualm,  Ruß',  kvepet  ,räuchern', ablautend    lit.    küpüoti    ,schwer    atmen',    lett.    küpet    , rauchen,    dampfen.
597
stäuben^  kuplnäties  , aufgehen  (vom  Teig)',  Jcupt  ,gären',  apr.  hupsins  ,Nebel' (Ableitung  von  einem  es-St.  wie  lat.  vapor);
aksl.  hypljg,  kypeti  , wallen,  überlaufen',  JcypTb  ,locker,  porös',  cech. hyp'ry  alt  , strebsam,  emsig,  frisch';  klr.  Jcväpyty  ia  ,sich  sputen,  eilen'; mit  (idg.)  geschwundenem  u  russ.  Jcöpoth  {^Tcojput-)  f.  , feiner  Ruß,  Staub', Icoptith  , mit  Rauch  schwarz  machen,  räuchern';  vielleicht  aksl.  hopr^  ,Dill' (riechende  Pflanze;  s.  Berneker  564).
WP.  I  379  f.,  WH.  I  312  f.,  Trautmann  147.
kejjero-,  köuero-  (auch  sküro-?)  ,Nord,  Nordwind'.
Lat.  caurus  (cörus)  ,Nordwind'  {*kduero-)]
lit.  sidure  f.  ,Norden',  Haurys  m.  , Nordwind';
abg.  sever^  (*keuero-)  ,Norden';
hierzu  vielleicht  ablautend  und  mit  anlaut.  s-:
arm.  curt  ,kalt;  Kälte,  Schauer'  (*skür-do-) ;
aisl.  ahd.  skür  ,Ungewitter',  nhd.  Schauer ^  afries.  as.  ags.  scür,  sceor , Schauer',  got.  sküra  windis  , Wirbelwind',  norw.  dial.  skeyra  (*skauriön-) , Windschauer',  skjera  (*skeurön-)  ds.,  norw.  skeyra,  sküra  ,blindlings  auf etwas  losfahren',  aisl.  skyra  , schnell  dahinrennen'.
WP.  I  377,  WH.  I  190,  0.  Szemerenyi  KZ.  70,  65.
keuk-  , leuchten,  hell,  weiß  sein,  glühen'.
Ai.  söcatij  iucyati  ,leuchtet,  glänzt,  glüht,  brennt,  leidet  heftigen  Schmerz, trauert',  iocdyati  ^entzündet,  betrübt;  ist  traurig,  beklagt',  s
```


### [2026-09-07T18:19:12.894Z] TOOL RESULT

```
=== KNT leaf 181 ===
sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, originated in the line of Darius as a means of discrediting the line of Cyrus and of. justifying Darius in his seizure of the imperial power. The particular occasion might well be the unsuccessful revolt of Cyrus the Younger against his brother Artaxerxes IT, whom Ctesias served as personal physieian. Cf. JAOS 66.211 (1946).
IL SMERDIS AND GAUMATA
According to Behistan 510-513, Cambyses son of Cyrus killed his full-brother Smerdis, with such secrecy that his death was not known to the people; he then invaded Egypt. While he was on this expedition, rebellions developed in Persia and in Media and elsewhere. Notably a Magian named Gaumata headed the rebels, claiming to be Smerdis son of Cyrus, and he gained the kingship in all the rebellious territory. Cambyses, still in Egypt, committed suicide.
Gaumata started his rebellion in XII 14 of 523/2, and received the adherence of the Empire on IV 9 of 522/1. But Darius, a distant cousin of Cambyses, knowing that Gaumata was not the real Smerdis, with the aid of a few men fought with and slew Gaumata and his chief followers, on
VII 10 of the same year, at Sikayauvati, a fortress in Nisaya, a district of Media. Thereafter Darius became King.
Herodotus tells the same story at much greater length, in Book 3, chapters 1-38, 61-88. Cambyses invaded Egypt (chap. 1), and the reasons for the invasion and the course of the campaign are given (1-26). At Memphis he inflieted a fatal wound on the sacred bull which was worshipped as the God Apis (27-9), and thereupon lost his reason. Jeal- ous of his brother Smerdis’s prowess with the great bow which had come from the Ichthyophagi, he sent Smerdis back to Persia, and then, after a dream which betokened that Smerdis would sup- plant him, he sent his henchman Prexaspes to murder him secretly, which he did (30-8), esp. 30).
160
The Magus Patizeithes had been left by Cambyses as managing steward of his palace at Susa, and he was one of the few who knew of the death of Smerdis. He had himself à brother who greatly resembled Smerdis in appearance, and, says Herodotus, this brother's name was also Smerdis. Patizeithes put his brother Smerdis on the throne, under the pretense that he was Smerdis son of Cyrus and brother of Cambyses. The false Smerdis, by not admitting to his presence any one who had known the true Smerdis, successfully con- cealed his true identity for some time (61-2). But the news reached Cambyses in Egypt, and he knew the truth, because Prexaspes assured him that he had slain the real Smerdis. Resolved to fight the usurper, he leaped upon his horse to lead his army back to Susa, but as he did во he accidentally struck the point of his sword into his thigh, and from the wound he died (63-6). Thus the false Smerdis ruled for some months; but a Persian
OLD PERSIAN
nobleman, Otanes son of Pharnaspes, suspecting his identity, managed by a ruse to prove it to himself (67-9), and secured the help of five other trusted noblemen, to whom there was added Darius, who had come to Susa from his father Hystaspes, governor of Persia (70; see App. IIT). Darius insisted on immediate action against the two Magi (71-3). Helped by the confusion follow- ing the public confession of Prexaspes that he had murdered the true Smerdis, and by his suicide, the seven men burst into the presence of the two Magi and slew them (74-9). They then agreed upon a method of selecting one of their number to hold the throne, and Darius, aided by the trickery of his groom Oebares, was the winner (80-8).
The two accounts, it will be seen, agree in the main features, but differ considerably in the de- tails. Herodotus’ story has clearly entered into t
=== KNT leaf 182 ===
he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Persian noblemen who co- operated with Darius in slaying Gaumata the false Smerdis, are given in Behistan §68 and in Herodotus 3.70; there is agreement in the names of the first five:
Behistan Herodotus Vi"dafarnd son of Vayaspdra —— Intaphernes {Дата son of 8uxra Otanes son of
Pharnaspes
Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
Herodotus, it will be seen, differs from the Behistan account in the name of the father of
Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
The Behistan inscription mentions Vidarna again in §25, as defeating one of Phraortes’ armies in Media; Vi"dafarna in $50, as defeating the rebels at Babylon; Gaubaruva in $71, as crushing the last revolt of the Elamites.
IV. Tug Persian CALENDAR AND Benistan I-IV
In Behistan 4.4, Darius states that the 19 battles recorded by him in the first three columns of the inscription, with the attendant capture of 9 usurpers, took place hamahyáyà 6arda ‘in one and the same year’. For eighteen of the battles dates are given in the Persian calendar, with translation into the Elamite and the Akkadian. The difficulty has been to arrange these dates within one year, beginning with the killing of Gaumata, the false Smerdis; for the order of the months in the Persian
calendar, and in the other calendars, was by no means certain. Now, however, with evidence from additional Akkadian and Elamite tablets which have no Old Persian version, Arno Poebel has suc-
ceeded in reconstructing the lists of months, as
follows:!
! AJSLL 55.139-42. The Persian calendar has been the subject of many studies, but Poebel’s studies have sup- planted them all: ALSLL 55.130-65, 285-314, 56.121-45. Cf. also Hinz, ZDMG 96.326-31;
TEXTSIWITH NOTES AND TRANSLATION
Old Persian Elamite Akkadian Equivalent
1 Adukanaiša Hadukanna$ Nisabbu Mch.- Apr. 2 Otiravahara Turmár Andru Apr.- May 30üigarci$ — Sdkurrisif —— Simannu May- June 4 Garmapada Karmabada$ Dwūzu June- July ОТОТ Turnabagi$ Abu July- Aug. ена агра (та) & — Ulülu Aug.- Spt. 7 Bügayüdi$ — Bagijüti Taxritu = Spt.- Oct. 8 *Vurkazana Margaíana$ Arahsamna Oct.- Nov. 9 Aciyadiya  Haifuüt(;a)& Küslimu — Nov.- Dec. 10 Anémaka HandmakaS Tebétu Dec.- Jan. It Sami(ia)maS Sabitu Jan.- Feb. 12 Viyarna = =Mitia)kannaS Addàru Кер. Мер.
The narrative of the revolts, however, is not given in temporal sequence in Columns Т-Ш, but rather in а geographical order conditioned by the order in which the rebellious provinces are named in $22: Persia, Elam, Media, Assyria, Egypt, Parthia, Margiana, Sattagydia, Seythia. If we should reduce the story to a more easily intelligible pattern, it would be аз follows:
After Cambyses, son of Cyrus the Great, secretly slew his full-brother Smerdis and went on the expedition to conquer Egypt, uprisings against his rule took place in Persia and in Media and elsewhere (810). Notably a Magian named Gaumata led the revolt, claiming to be Smerdis, whose death was known to but few; he started his revolt on XII 14 of 528/2, and received the adherence of the entire Empire, becoming King on IV 9 of 522/1? Cambyses died by his own hand, either intentionally or accidentally, in Egypt soon after hearing of Gaumata’s revolt, (§11).
Three months later Darius and his associates killed Gaumata and his ehief followers at Sikayau- vati in Media, on VII 10 of 522/1. Thereby Darius
2 The months will be indicated by Roman numerals.
161
became King, but at the very outset his rule was contested by Agina in Elam, and by Nidintu-Bel (claiming to be Nebuchadrezzar son of Nabonidus) in Babylon, who were recognized as King each in his locality. But Аспа did not last long; Darius, after organizing the gove
=== KNT leaf 223 ===
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
```


## [2026-09-07T18:19:32.356Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"naiy adv\\|naiy conj\\|^naiy\\|nay adv\" KNT.txt | head; echo \"=== a- privative in KNT ===\"; grep -n \"a- ‘not\\|a- 'not\\|negative prefix\\|priv\\.\" KNT.txt | head -20",
 "description": "KNT naiy lexicon entry"
}
```


### [2026-09-07T18:19:32.437Z] TOOL RESULT

```
5123:ašnaiy adv. ‘near’, lsn. of ašna- ‘near’ (Hz. Ap] 98-9), Av. dsna- ‘near’, in loc. dsnaé-ca, asne ‘near’, abl. asna ‘from near’; from pAr. root end- ing in $ or 2 (pIE Ё or ў: Skt. aánóti ‘attains’ and djatt ‘drives’ hardly suit); not *à-zd-na-, pte. to à + *had- ‘herangehen’ (Bthl. AiW 1755; but *had-, which always has prefix d, is only a semantic vari- ation of thad- ‘sit’), cf. Skt. dsanna- as adj. ‘near’ (Bthl. AW 220). Possibly from plE *afijh- ‘choke, throttle’, cf. Lt. атаб, Gk. &yxw, sb. Lt. angor, Av. azah-, Skt. qhas-: *afijh- + pte. -no- (806, §147.1, $191.11I, $243); for semantics, cf. Gk. &yx« adv. ‘near’ (JAOS 62.276-7). Not ‘on the march’, to pAr. root *aé-, Skt. djatt, Lt. agit (Bthl. А 264); nor ‘m friendship’ on the basis of the Elam. kanna ети git (WB; KT); nor ‘at peace’, cf. Av. dxsitd ‘peace’, dx Sta- ‘peaceful’ (Ву. BSLP 31.2.67-9). Elam. kan- recurs as the translation of dausid ‘friend’, but this meaning eliminates only ‘on the march’, since ‘friendship’, ‘peace’, and ‘nearness’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
5581:naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
=== a- privative in KNT ===
947:*bhndh-to-, OP basta- ($85), Skt. baddhá-, cf. Eng. bound. negative prefix *n- in a-zSatna-, a-xsala-, etc. *sm-dhe, OP hadà, Skt. sahá ‘with’. I. Before a vowel ог; or у, pIE » and m must,
2832:a- an-, the common negative prefix.
```


## [2026-09-07T18:19:33.241Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 188 189 230 231; do echo \"=== KNT leaf $((n-1)) ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' KNT.txt | head -25; done",
 "description": "KNT pages near 167 and 209"
}
```


### [2026-09-07T18:19:34.625Z] TOOL RESULT

```
=== KNT leaf 187 ===
t built, unrepaired’; neg. a- + pte. of kar- ‘make’. {akarta] nsf. DSe 47 (conj. of Kent, JAOS 54.43).
azíaina- adj, with kdsaka-, ‘turquois’ (so Bleichsteiner, WZKM 37.103-4, and Konig, Burg- bau 63-4, but considered dubious by Hinz, ZDMG 95.235-6; hardly ‘gray amber’, with Hz. AMI 3.05—7, ApI 232; not ‘hematite’, with Scheil 21.29- 30): Av. arSaéna- ‘dark-colored’, borrowed in Gk. Порто “Atevos ‘Black Sea’ (‘in-hospitable’, by Gk. popular etymology, and euphemistically changed to Еф о), from neg. a- + z&atna-, cf. Av. xSaéta- ‘shining’ (§102, 5147.1). azšaina nsm. DSf 39.
axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl 70-1). azšałā nsf, DPe 23.
aguru- sb. ‘baked brick’ (8158.1). lagurum] asm. DSf 53, supplied by König, Burgbau 52, after a-gur-ru of the АКК. text, ef. NPers. ágür in the same meaning. alg|ura[và] Ism. DB 4.89 (restored by Kent, JAOS 62.267, after König, Klotho 4.45); but read амуй аһа with Cameron.
agriya- adj. ‘topmost, excellent, loyal’: Av. ayrya- ‘first in quality, etc.’, Skt. agriyd- agryd- ‘foremost, principal, etc.’, deriv. ($144.1V) to Av. ayra ‘der erste, oberste; (nt.) Anfang, Spitze’, Skt. dgra- ‘foremost, prominent, best; (nt.) tip, sum- mit, best part’ ($148.I). agriya пет. DB 1.21, as read by Cameron, replacing KT’s ag*r^ ++ (and the restorations thereof: dgar[ia] Wb. ZDMG 61.725, Tm. Vdt. Stud. 1.9, ef. Bthl. WZKM 22.72; ágra"|6a] Jn. Indian Stud. Lanman 255-7; ügr[mata] Konig, RuID 65; ágr[mà] Hz. Арі. 59- 62).
aciy adv. ‘then, at that time’ ($291.1V): Av. ajčit ‘and indeed’, Lt. ecquid (interrog.) ‘anything’, pIE *ed-g*id, see *a- ‘this’ and particle -cty ($105, $130; Ву. BSLP 33.2.152-3; Hz. AMI 4.125-6, 8.41, ApI 55-6; Wb. ЖА 41.319). ХРЇ 21.
Atamaita- sb. ‘Atamaita’, an Elamite rebel: Elam. Atameta (854.I, §76.V; Hüsing ар. Prašek,
166
IMP 2.78.08; König, Кир 78; not Umamaita after the Ummaima of Oppert, Médes 158, based on Rawlmnson’s J-im"im*^, later altered by KT's тт). {[Ajtamacta nsm. DB 5.5.
_ ütar- sb. ‘fire’: Av. diar- dór-, NPers. абат; in Á ciyadiya- and verhaps in Acina- ($152.Г).
atar (i.e. ачат), prep. with ace., ‘within, among’: Av. antara, Skt. antar, Lt. inter, pIE tenter (831). DB 1.21; 2.78; 4.32, 92; XPh 30, 35.
ali-, prefix, ‘beyond, across’: Av. aiti, Skt. dti, Gk. ёт ‘yet, longer’, Lt. et ‘and’, pIE *eti ; with ay-, yam-. Cf. also айту.
abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, cf. OP asan-, asman- (S87, S151, $155.1); see also a(againa-. afagam asm. DSf 24, 48.
abagaina- (Le. aba^gaina-) adj. ‘of stone’: deriv. of абада- (147.11), perhaps with vriddhi (§126; déagaina-?). alagaina nsm. DPe. abagainam asm. D'Sa 1; A*Hb. afagainüm asf. ASe 6; abagandm asf. (852. VI) for nsf. (856.V) A’Pa 22. afagainiya прі. (S152.IT, $179.11, $190.I; JAOS 53.20; wrongly Konig, Burgbau 68; not abagainiy nsf. to sg. collective stind, as taken by Hz. AMI 3.68) DSf 45.
Gahavaja, word of unknown meaning, DB 4.90 (reading of KT); hardly, with Morgenstierne, Acta Or. 1.252, d@a*ha-vaja ‘word, speech of proc- lamation’, ef. Skt. aqsd- ‘hope, expectation’, + vacas- ‘word’. Perhaps G@aha- (§143.1; with Morgenstierne) + root-noun vaj- ($142) ‘procla- mation-strengthener, seal’, gsm. (JAOS 62.268; not abl. as instr., with Konig, Klotho 444—5).
abiy prep. with acc. ‘to’: DB 1.91. Apparently doublet to айу (Ву. Gr. §102), possibly by con- tamination of *a; antevocalic and ati antecon- sonantal, in sandhi ($80; Mt. Gr. $103).
Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune
=== KNT leaf 188 ===
’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore ‘having the fragrance of the truth’).  <Aé@iydbausinahya gsm. Sa 4-7.
Aéura sb. ‘Assyria (and Syria)’, a province of the Persian Empire ($6, $106.11): Elam. aš- &i-ra, АКК. áš-šur, Gk. 'Аттурв‚ but Aram. абиг. Aéuré nsf. DB 1.14f; 2.7; DPe 11; DNa 26f; DSe 26°; DSm 7°; XPh 22. Aéurayd lsf. (5186) DB 2.58f.
A@uriya- adj. ‘Assyrian’: deriv. to preceding .
($144.1), perhaps with vriddhi in first syllable (8126; Aburiya- ?). A@uriya пет. DN xvii; DSf 32; А?Р 17.
Agina- sb. ‘Acina’, ап Elamite rebel: Elam. ka-iš-ši-na, Akk. a-Si-na. Either borrowed from Elam. (Foy, KZ 37.498); or shortened from an IE name beginning with OP äç- = Av. átar- 007- ‘fire’ ($147.11, §152.1), ef. atoro-dáta- ‘Fire-given or Fire-created’ and other names (Vd. 18.52; Justi, INB 50; Bthl. AiW 324). Agina пет. DB. 1.74, 82: 4.10; DBe 1f. Acinam asm. DB 1.76.
Ld
A ciyádiya- adj. ‘Aciyadiya’, the ninth month, .
Nov.-Dec.: Elam. haššiyatiyaš, АКК. kislimu, Cpd. of átar- ‘Are’ + deriv. of yad- ‘worship’ ($126; $152.D: ‘Fire-Worship Month’. Agiyddiyahya gsm. DB 1.89; 3.18.
ada- adv. ‘then’: GAv. ald, LAv. ада, Skt. .
ба ‘therefore’ cf. Gk. трбе-бє (and -Gev) ^n front of’: pIE *e-dhe, to root in *a- ($76.11; $191.II); see also adakaty. — ada-taiy DNa 48, 45.
adakaiy adv. ‘then’: OP ada- + -kazy, Gk. aly. то ‘somewhere’, pIE *q¥ei, Isn. to int.-indef. stem ($135). DB 2.11, 24; 4.81, 82; DNb 38.
adam pron. “Р: Av. azam, Skt. adm, plE .
*eühom ($109), ef. pIE *ейб in Gk. yo, Lt. ego (8193.1). adam nsm. AmH 5,8; AsH 14; CMa 1; DB 1.1, 10, 12, 39, 52, 54 bis, 56, 59, 60, 62, 63, 64, 66, 67, 68 bis, 70, 72, 73, 75, 18, 82, 83, 86, 89, 91, 95; 23, 5, 6, 10°, 11, 15°, 19, 28, 30, 48, 50, 68, 64, 69, 72, 80, 81, 88; 3.1, 13, 25, 29, 50, 77, 80, 84; 48, 8, 11°, 14, 16, 19, 21, 24, 27, 29, 32, 40, 45, 59, 64, 71, 81, 89; 5.2, 6f, 13, 21°, 23°, 25°; DBa 1, 16; DBb 4, 6; DBe 5; DBd 3, 6; DBe 5, 8; DBf 3f; рве 5; DBh 4f, 8; ОВ: 4, 9; ОВ] 4; DPd 20; DPe 1, 7; DPh 4; DNa 8, 17, 34, 37, 531; DSa 1, 4; DSb 1; DSe; DSd 1°; DSe 7f, 16°, 34, 44°; DSf 5, 18°, 21°; D8g 1, 3°; DSi 1; DSj 1°, 2°. DSk 1, 4; DSm 1°, 6°; DSy 1; DZe 4, 7, 8, 11;
LEXICON
DE 11; DH 3f; XPa 6, 13, 14; XPb 11; XPe 6; XPd 8, 17; XP£ 8, 34f, 36, 39, 41; XPg 9; XPh 6f, 15, 29, 34, 37, 40, 421, 43, 50; ХР] bis; XSe 1°, 3°, 4°, XE 12; XV 9, 23; A!Pa 9°, 21°; D'8b 1°, 4°; A'Sa 4; A’Sb; A'8d 1, 3; A?Ha 5°; A’He 9, 16; Азра 11f; Wa 2; Wb 1; We 2; Wd 2; SDa; SDb; SXb 1; SXe 1. adam-áaty DB 2.731. айат-йт (839) DB 1.62, 83; 4.6; DNa 35. adam-sam DB 1.14; DNa 18; DSe 17 adam-[$am]; XPh 16.
mam asm. (Av. mam, Skt. mdm, рЕ *me + acc. -m; 5193.11) AsH 7, 11; DB 1.52 (métya-mam, $133), 82f, 93°; 2.18, 28, 48, 63, 67, 73, 88; 3.30; 4.35, 91; 5.13, 17, 26, 28°, 29°, 33; DPh 9; DNa 33, 31,51; ОХЬ 11, 22, 26, 46, 49; DSe 50°; DSf 9, 10, 14f, 17 bis, 57; DSi 3°; DSj 4, 6°; Рб 4°; DSs 6; DSt 7°; DZe 12; DH 71; XPa 18; XPb 27; XPe 12; XPd 17; XPf 31, 45; XPg 12; XPh 57; X8e 4°. XV 25; A!Pa 22°; A’Sa 5^; A’Sd 4; A?Ha 6; A?Hb?; A?Hc 19; A?Pa 5, 23, 24; 224, 26 ({56.У; for mand ?).
-mā asm. епс]. (Av. md, Skt. md, pIE *mé, 6193.1; cf. enel. *me in Gk. pe): nai-mā ОМ 8 (na[ima]), 10, 19; nai-pati-ma ОМ 20.
mand gsm. (Av. mana, Skt. máma, pAr. *mana, cf. Lith. mano; $193.11T) AmH 6, 10; AsH 9; DB 1.4, 9, 12, 18, 18, 19 bis, 28, 27, 60; 2.19f, 21, 25, 27, 29f, 31, 35, 40, 46, 49, 51, 55, 601, 82, 84, 87, 91f, 93; 3.0f, 10, 13, 15, 17, 20, 20f, 31, 32, 38, 45, 53, 56, 62, 67, 75f, 76, 84, 86; 4.2, 12, 35, 42, 49, 52, 531, 66, 821; 5.8, 14°, 30; Ва 5, 14£; DPd 7, 13; DPe 9; DNa 19, 21, 33; DNb 56°; DSe 18°, 20°, 38; DSf 12, 13, 58; DS} 5°; DSk 4; DSs 6°; XPa 19; XPb 23; XPe 11; XPf 16, 23, 31, 46; XPg 7; XPh 17, 19; Ха 2; XV 18; A!Pa 20°; D'Sb 4^; A’He 18.  mana-eá (8135) DPd 9f.
-maiy gsm. (gen.-dat. GAv. mót, LAv. mé, Skt. me, Gk. dat. но, pIE *mot) enclitic to айа (ns
=== KNT leaf 229 ===
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8).
*Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ
Ы
LEXICON | 205
8.513-6; Hz. ApI 244-9; Nyberg, Rel. 477-8). Yadayd absf. ($141, $175) DB 3.26.
yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DSf 11; ‘whenever’, with pres. ind., DNb 38f, 39.
yàna- sb. ‘favor, boon’: Av. yand-; deriv. of
‚ yam-, probably *ya- from *m-, with lengthening
and suffix -na- (5147.1). yànam asm. DPd 21, 23°; XSe 4°.
yaniy соп]. ‘where, whereon’: lsn. *ya^mi (= Skt. ydsmi-n, Av. yahmy-a ‘where’) to relative stem ya-, with -n- after isn. *yand, cf. isn. lyand to tya- (hardly yanazy, loc. formed on stem yana- extracted from isn. *yand, as taken by Bthl. Ат 1262; not miswritten for tyanaty, as taken by Müller, WZKM 7.112; other theories in Tm. Lex. 120 s.v.). Syntax $296. XV 22.
yam- vb. ‘stretch, reach out’: Av. yam- pres. yasaiti, Skt. yam-, pres. ydechati, OP pres. yasa-, pIE *im-ske-. See also уйпа-.
а + yam- ‘reach out for, (mid.) take as one's own’: ãyasatā imf. mid. (§97, $215, $235.IT) DB 147; 34, 49f.
ай- + yam- ‘reach beyond, present, read aloud to’: [аја] уа (823.T, $140.IIT, $220) imf. pass. DB 4.91 (conj. of Kent, JAOS 62.268; for -i-, ef. niyasaya, below).
ni- + yam- ‘reach out and down; (caus.) set down’: niyasaya imf. caus. (823.I, $140.IIT, $215) DNb 5, 46, 49 (In. JAOS 38.123-4; MB Gr. $199; Johnson, Gr. $4780; Hz. ApI 359-61).
уйа con]. ‘as long as’, isn. of *ydva-, exten- sion of pIE rel. */o-, pAr. *ia-, cf. Skt. ydvat, Av. yavala, Gk. dos (from *ayos); hardly from* yàva! à = GAv. (Ys. 43.8) yavat à, with contraction (Wackernagel, KZ 46.275-80). With subj. to show future time ($208): DB 4.71, 74, 78; 5.19, 35°.
raucah- sb. ‘day’: Av. raocah- ‘light’, Phi. rüé, NPers. róz, Skt. rócas- ‘light’, pIE *leugos ($70, $107, $156.ID, ef. Gk. Xexó-s adj. ‘ight’. тамса nsn. ($119, $1851) DB 3.8. rauca-pati-và
(899, $133) asn. DB 1.20. raucabiš ipn. ($119, 51851) DB 1.38, 42, 56, 89f, 96; 2.26, 36, 42, 47, 56, 691, 98^; 3.181, 39, 47, 63, 68, 88f.
ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2, AW 800). rauta nsn. anacoluthic in naming phrase (wrongly gen.-abl. to stem таш-, Mt. MSLP 19.56-7, MB Gr. $167, $316) DZc 9.
Razé- sb. ‘Rakha’, а town m Persia: Elam. rak-qa-an (S100). Ваха nsf. DB 3.34.
тахйайш! DNb 60, imv. of vb. of unknown etymology and uncertain meaning (§76.II, V, $103.IIT, $213, $237.II), perhaps ‘inflict punish- ment upon’, cf. АКК. version (Lg. 15.174; see also Hz. ApI 284-5).
ra”ga- sb. ‘speed, haste’: Av. rang- "leicht, flink werden’ (Bthl. AiW 1511), Skt. rdhale ‘has- tens, speeds’, rahas- nt. ‘speed, quickness’ (for fur- ther connections, see Uhlenbeck, Wrtb. d. altind. Sprache 241). ragam asn. (or asm.?) as adv. (§143.1, $191.IIT) DB 4.44, perhaps with develop- ment to ‘eagerly’ or ‘confidently’.
Raga- sb. ‘Rhages’, a district in Media: El
=== KNT leaf 230 ===
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
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
-vä encl. conj. ‘or’ (8133, $291.1
```


## [2026-09-07T18:19:50.806Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find leaf containing given strings\nfor pat in ['a- an-, the common negative prefix','naiy adv. ‘not’','apurnay','purnay']:\n    for i,l in enumerate(leaves):\n        if pat in l:\n            # find printed page numbers in leaf\n            nums=re.findall(r'^\\s*(\\d{3})\\s*$',l,re.M)\n            print(pat,'-> leaf',i,'nums',nums[:5])\n            print('  ctx:',l[max(0,l.find(pat)-300):l.find(pat)+300].replace('\\n',' '))\n            break\nEOF",
 "description": "Locate KNT entries"
}
```


### [2026-09-07T18:19:52.082Z] TOOL RESULT

```
a- an-, the common negative prefix -> leaf 103 nums []
  ctx: ivative noun. pasă, prep. w. aec. and gen. fra-, pref. w. verbs and nouns, and in phrasal ad- verb. yàlà, prep. w. loc. уйй à, prep. w. abl. radiy, postp. w. gen. vi-, pref. w. verbs and nouns. hacà, prep. w. abl., loc., instr., adv. hadā, prep. w. instr. The inseparable prefixes are the following: a- an-, the common negative prefix. u- (= *u-) ‘well’, duš- ll’. ha- ham-, equal in meaning to Gk. civ and Lt. com- as prefixes. The uses as prepositions (and postpositions) will be discussed in the following sections; other uses are adequately described in the Lexicon. $269. PREPOSITIONS WITH THE Á
naiy adv. ‘not’ -> leaf 216 nums ['193']
  ctx: e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23. naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; : from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis
```


## [2026-09-07T18:20:03.337Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==233' KNT.txt | head -30",
 "description": "KNT p.209"
}
```


## [2026-09-07T18:20:04.120Z] TOOL CALL #16: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py; echo ...; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "ref_page tool and BQT metadata"
}
```


### [2026-09-07T18:20:04.583Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-07T18:20:05.809Z] TOOL RESULT

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
...
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


## [2026-09-07T18:20:14.966Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor i in range(228,240):\n    l=leaves[i]\n    nums=re.findall(r'(?m)^\\s*(\\d{3})\\s*$',l)\n    print(i,nums, l[:80].replace('\\n',' '))\nEOF",
 "description": "KNT leaf survey"
}
```


## [2026-09-07T18:20:15.517Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== borna in v1 ===\"; grep -n \"برنا\" BQT_v1_pages.txt | head -20",
 "description": "BQT borna"
}
```


### [2026-09-07T18:20:17.299Z] TOOL RESULT

```
Exit code 1
nleaves 232
228 ['204'] so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a provi
229 [] d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; 
230 ['206'] am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71
231 [] 1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
IndexError: list index out of range
```


### [2026-09-07T18:20:17.362Z] TOOL RESULT

```
=== borna in v1 ===
8863:باید خرد شاه را نا گزبر هم آموزش مرد برنا وییر . فردوسی < لفت‌نامه *.
8900:۸ - چوآعیغ برنا شدآراسته
9869:۲ - پپلوی 200792 , 20117۲02 بمعنی برناء جوان « بونکر ۹۹ ».
17257:اعمال هرات برناحية بادغیس ۷ .
18281:بروزن سرتراشك » بممنی برناشك أست .
19010:بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
19020:و تعصب باشد چه برنایشتی کردن بمعنی پشتی
24992:با درخشنده چراغی ممبان برنا .
26378:بشد برغخت زر اردای وبراف ۱ پنامی بررخ و کستی‌اش برناف .
27022:برنافتن- وترلك دادن و اجتناب نمودن و احتراژ
```


## [2026-09-07T18:20:24.800Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\n# find leaf containing line 9869 content\nkey='بمعنی برناء جوان'\nfor i,l in enumerate(leaves):\n    if key in l:\n        print('leaf',i)\n        print(l[-2500:])\n        break\nEOF",
 "description": "BQT borna footnote leaf"
}
```


### [2026-09-07T18:20:26.070Z] TOOL RESULT

```
nleaves 777
leaf 295
کت آیرویز
نحتانی مجهول و واو » بسعنی آبی باشد و آن
ا ییون « بر وزن و ممنی افیون است
که تربالك باشد ونام داروبی حم هست که بیهوشی
می اورد ۴ ۰
ونگی ات ععروف. ابی سك ۳ ۲ بای حطی
۱ ۱ 3 ۱ ‌ ‌‌ هح ‌
یود ج ( 3 رب وسکون های‌هوز و کسرمیم رتحتانی‌بالف کشیده,
و دال بی نقطه ؛ نام شهرست در خراسان مایین بزبان یونانی توعی از تشنج باشد که مانع حس
سرخس ونساآله آنها نیزهريك شهری باشند! ۰ | و حرکت کرده
درهمزه با بای فارسی مشتمل بر بازده لغت
آر ؟ س بفتح اول و سکون ثانی ورای بی و بکاف زده » بلقت زند و یازند (۵) نوچه و نو
نقطه بالف کشیده , بلنت زند و پازید (۷) خالء | جوان را گوبند ۷ - و جماعتی از ترکان حم
را گوبند و بعربی تراب خوانند ۴ . 9
اپراهام * - بکر اول و حای (۳) ابر فداخ - با داد بی قطه و خای
بالف کشیده و بمیم زده , نامی است دارسی استان تن مان » سختان و تیماح
۰ که آنرا ممرب کرده «ابراهیم» گویند . را گویند
آ پر خیله - بنتح اول وکسر خای‌نفطه آیر و دز با راو و تجتانی حجهول بر
دار پروزن تترسیده . بممنی صریح است چنانچه
پرخینه بمعئی ایما و اثارت (۶) باشد ۷ .
وزن سحر خیز , بمعنی پرویز است چنانکه
افربدون فربدون باشد - و بمعتی مظفر ومتصور
ایر ناك ه , نم ثانی و نون بالف کشیده و عزیز و کرامی هم آمده است ٩‏ .
)۱ چك : : سوم ۰ )۱( مك : زند ویاژند ۰ ۳ چك : هك.
4 چكث » چب 5 : اشاره ۰ () جكث ژند وداژند ۲
- اییورد و علورد سس کفتهاند وباورد همان « باأرت ۰ واباورت» زمان قد‌است وغاهراً
1 «زوستن؟ و وم «#یلین» همین شهراست. «امران‌باستان ۰۸-۲۲۰۷
باقوت کویدٍ : اسورد شهری اس بخراسان من سرخس و تسا و آب‌وهوای آن‌ناسالم امست و أین‌شهر ۱
دست این علعرینکریز بسال۳۱ « فتح شد وبصنی کنته اند بیش از این زمان بست‌احنفین
ی تن کقوده هف ۰ * معجم الملدان ‌ ۳ . رك ؛ ایبویه
۴ - مصحف کلمة بوتانی اییلمبنینا « لفت‌نامه » ۳118170021120618 ممعنی‌ناگهان
تن ۴ هزوارش 2 , 2۱۷۲2 . بهلوی خالك 22 « بونکر۱۰۰ 5
۵ رگ : ابرهام. ۱ - ازلفات دساتیر است ؛ رك : فرهنگه دساثبر صس۲۳۷۲ .
۲ - پپلوی 200792 , 20117۲02 بمعنی برناء جوان « بونکر ۹۹ ».
۸ - رك : اپیرنداخ » پرنداخ. ٩‏ - بپپلوی 2097۷۵ بمعنی پرو زگر » غاح
«منای ۲-۷۹۷ *.
```


## [2026-09-07T18:20:45.170Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n -i \"purnay\\|purnāy\\|burnay\\|aburn\\|apurn\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"purnay\\|aparnay\\|apurnay\\|burnak\" NYB_vol2_glossary.txt | head -20; echo \"=== HRN/HUB ===\"; grep -n -i \"burnā\\|burna\\b\\|barnā\" HRN.txt HUB.txt | head -20",
 "description": "Pahlavi purnay lookups"
}
```


### [2026-09-07T18:20:45.264Z] TOOL RESULT

```
=== PHD ===
PHD.txt:130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:734:adult dād-meh, purnāy.
PHD.txt:1223:child aburnüy(ag), frazand, waččag, zadag, zahag.
PHD.txt:1225:childhood aburnāyīh, rahigih.
PHD_mackenzie.txt:828:aburnay ['p(w)ln'd, v. purnay I N burna] under age, child.
PHD_mackenzie.txt:830:aburnayag ['p(w)ln'(d)yk'] child.
PHD_mackenzie.txt:4273:purnay [pwln)d] adult.
PHD_mackenzie.txt:5887:abode awarisn, bunag, manist,             adult dad-meh, purnay.
PHD_mackenzie.txt:6173:cauldron deg.                           child aburnay(ag), frazand, rahig,
PHD_mackenzie.txt:6176:cavity gabr.                            childhood aburnayih, rahigih.
PHD_mackenzie.txt:8730:purnay              ..AAI~ leu                frazandih                   .A\Y ""CD
PHD_mackenzie.txt:11396:aburnay                .No'~~          abzonig                       \»\$~
PHD_mackenzie.txt:11397:aburnayih           .-.u--'~U'         abzon                           \,~ Q)'
PHD_mackenzie.txt:11454:aburnay                     ~~'Q)I            iibestan
PHD_mackenzie.txt:11458:aburnayag             \ UN ~ ,Q,)t            abecim                -fit OCU'
=== NYB ===
=== HRN/HUB ===
HUB.txt:4182:oder opecak?; burna 'Jiingling' = paz. awarnai Shk. 238,
HUB.txt:5037:skr. brhant- ; burna *Jungling' = zd. aperenayii- ; bus 'Hals,
HUB.txt:9258:a) rn bleibt in: burna, barnd *Jungling', zd. apere-
```


## [2026-09-07T18:20:46.361Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (483,484,485,486):\n    l=leaves[i]\n    print('=== leaf',i,'===')\n    print(l[:1200])\nEOF",
 "description": "BQT v1 leaf ~484"
}
```


### [2026-09-07T18:20:47.809Z] TOOL RESULT

```
=== leaf 483 ===
5
رما ۱ ه بر وزن نتزك ؛ دام جابی
و مقامی و ولایتی است - و لقب جعفر پدر خالد
نیز هست . گویند او مردی بوده در نهایت فنل
و کرم وتمبش بملوك فری میرسد و در اوابل‌حال
مجوی بود و متولی سدانیه که از موفوفات‌نوبهار
که آن بثخانه و آتشکده بلخ است شد وبعبادت
آتش مشفول بود . و گویند هرکس متولی آنجا
متفه او وا مرطاقة میکاقه الاو ی وهگر
کفته‌انه چون جمال حالش بزبور اسلام آراسته
کردید با عبال واطقال بجانب دمشق کهدارالملك
حکام منی‌امبه بود ثوجه نمود . مد از چند روز
ببا رگاه سلیمان‌ین عبدالملك آمد (۱) چون‌چشم
سلیمان پرجعفر افتاد دنکش مثفیر شد ۰ اشاره
فرمود تا او را از مجلس بیرون بردند . خواص
و ندمای ءجلس از صدور این حکم تعجب نموده
از سب آن پرسیدند . سلیمان کفت این شخص
زهر مرا دارد . گفتند چون معلوم‌خداوند شد؟
کفت : دومهره بر بازوی من بسته است که هر
گاه زهر با طعام وشرابزهردار بمجلس‌درآورند
(۱) چپ ۱ ۰ چش : آهده .
برحوژه
آنها محسب خاصیت ح رکتی() عثیف میکنند.
حنا رکیفیت حال از جعفی پرسیدند . جوام‌داد:
بلی قدری زهر در زیر نگن انکشتر دارم مجهت
آنکه در هنگام شدت‌الم برمکم. لهنا او مرك
و اولاد او ببرمکی ملقب و مشهور شدتد .
بر مکان - باءاف فارسی بروزن‌قلمدان»
موی زحار باشد و آن بالای موضم آلت هردی
و زنی است ؛ و آنرا بعربی عانه میگویند . **
ار هو ع بروزن بدخوءیمعتی اتظارباشد»
وبجای رای‌قرشت دال آبجدهم بتظر آ
=== leaf 484 ===
برحه
بر هه ۱ « بروزن کرعه: مثفب‌درود گری
باش که بدان چوب و نخته سوراخ کنند .
برن ‏ بروزن چمن . ام فصبه‌است در
فر فا ۴ ع بنتح اوز و سکون ثانی و نون
بالف کشیده . جوان و نوچة اول عمر و ظریف
را گونند - و بمعتی خوب و نيك هم هست -
و حنا را نیز کون دکه بردست و پا بندنده وضم
اول هم آمده است .
بر فاخی الستادن » کنابد از اطات
کردن و بلدب ایستادن باشد .
بر فاص ۴ - بروزن کربای, بمعنی‌غافل
و عادان - و غافلی و ناداتی باشد .
بر ناك ۴ « چختح اول بر وزن غمناله ۰
بمعنی برنا است که جوان و نوچةٌ اول عمر باشد
ور حنای دلت و بارا نیز گفته‌اند. و خ‌اوژهم
۱ رك : برماه.
1 نو ای
یعنی آدجه برس رکتابتهار نامها نویستد » وسسربی
القاب و عنوان گویند۷ .
بر ناه » بروزن حمراه » جوان و نوچة
اول عمر را گویشدب وحنای دست و پارا نیز
بر نایشتی - یکر بای حطیو سکون
شین فرشت و فوفانی‌بتحتانی رسیده ۰ بمعنی پشتی
و تعصب باشد چه برنایشتی کردن بمعنی پشتی
کردن و تسب نمودن است . #*
بر فج - فتح اول و انی و سکون نون
و جیم » آن‌باشد اکه سیب کوری‌با بجهت‌ناریکی
دست خور را مر دبوار با جابی بمالند تا وک
بیدا کاند ۷ ْ
پر فاد - بکس اود بر وزنکرفتار .
جوان اراده کنند . ناصر خسرو بلخی کوید :
داسفا ۱ : ۲ س ٩۹۳‏ . اه
۵ مرکب‌از: پیشوند بر (بار) ۳ نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌اس
=== leaf 485 ===
۱۲ حسه برد
ی ۰
این شممها که در دل بسحق بر فروخت
از رهگذار نور(۱) برنج شماله بود ۴ .
مخقف بر نج‌زار است که شالی‌زار باشد ۰
بر نجاسب بکسر اول وثالی وسکون
کشیده و بسین بر نج کابلی - نغمی است دواییو آن
می نقطه و بای کوچك وبز رک میباشد و کوچك آن بپتراست»
باشد ٩‏ کهآ نرا کرم و خشك است . مفاصل را نافم است .
بوی مادران ۱ بر نج مثاك بروزن ومعنی‌فلنج‌عشك
کوند و بعربی است که بالنگوی خودروی باشد ۴ . بواسیر را
حبق الراعی تافع است .
خانه بگسترندجمیم گزندکان بگریزند ؛ وباین
معنی‌بجای حرف آخر تای قرشت هم آمده‌است .
پر نحاسف ه با فا . بر وزن و ععنی
برنجاسپ است که کباه بوی‌مادران باشد .
بر نج شماله - بنتح شین نقطهدارومیم
بالف کشیده و لام مفنوح » بممنی مزعفر است ۰
و آن طعامی‌باشد معروق . گوبند درشیرازطباخی
بود که پیوسته شبها برسرراهی تشستیو زردپلاوی
با پرنج درشتی پختی و درپیش خود فانوسی‌داشتی
رگاهی دوسه مشمل افروختی و فرباد کرد ی که
*یا به برنج شماله» و این بیت را نیز خواندی:
از طلا و نقره و امثال آن که زنان در دست‌ویای
7 آنسه وروت کتلت دست برنجن وآنچه
دریای کنند پای برنجن خوالند .
بر فجین ه بفتح اول بر وزن تبرزین »
بسعنی برنجن است که حلقَةٌ طلا و نفرء بلش د که
زئان در دست و با کنند .
یر فف « بنم اول بروزن خجند ؛ وبفتح
اول بروزن سمند ؛ هر دوآعده است بمعنی تیغ
و کمقی کر و آبدار و جوهردار ؛ و باین‌منی

=== leaf 486 ===
برنداف
بر ناف س بفتح اولو انی و سکون‌ثالث
و رامع بالف کشیده و فا زده » بمعنی تسمه‌ودوال
باشثك - و رودها را دز گویند اعم از آعکه رودء
اسان با حیوان دسگر باشد .
پر ند » بفتح اول و انی و رأبع
وسکون ثالث و کاف » کوه كوييك ويشتة خرد را
گویند , و بستی گویند برندك پدنه‌است کوچك
۱۲ هیان دشت و صحرا واقم باشد 1
و ثالث و رابع غیرمعلوم و کف بالف کشيده‌وبميم
زده .کیاهی باشد که آنرا بابونة کاو گوشد ۰
بر ده س بروژن‌رو نده , معلوم‌است -
و پروانه را نیز گویند و آن جانوری باشد که
شبها خود را بثعلهٌ شمع و چراغ زند 1
بر لس ع سم اول وثالث پروزن‌سندس »
جامه و کلاه يشمن گنده باشد که بشتر صارا
و ترسایان پوشند و بوسر نهند . و بعضی گوشد
نام کلاء تصرانیان است که فرنگیان (۱) باشند »
و بکر ثالك مروزن مفلس هم بنظر آمده‌است.
و بعفی گوبند بمعنی کلاء عربی است ۴  .‏
بر فشسقی س کنابه ازسوارشدن‌باشد ۴.
بر نگ - بفتح اول وثانی بروزن‌خدنگ»
بمعتی جچری و درای و لق‌درخانه باشد - وکید
را نیز گویند که عربان مفتاح‌خوانند ؛ وبایشععنی
بش
با زای قطددار هم آمده است - و بضم اولوئانی
بمه‌نی اندوخثه و ذخیره و پی‌انداز باشد -. ونم
ولایتی است که قطب جنوبی آنجا دیده میشود -
و بکر اول و انی برنج کابلی را کویند » وآن
بر و بر وزن بدخو ۰ دبای تنك
بر و س ‏ بفتم اول بر وزن افوی »
کی از مچددقان نت۵ کی ولیک
را نیز گومشد , و باینمعنی با شین تقط
```


## [2026-09-07T18:21:09.774Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[484][1100:])\n\"; echo \"=== HUB context ===\"; sed -n '4178,4186p;5033,5040p;9254,9262p' HUB.txt",
 "description": "BQT leaf 484 footnotes and HUB context"
}
```


### [2026-09-07T18:21:11.112Z] TOOL RESULT

```
نامه, ۷2۲-۲۵103
« اسفا ۱ : ۲ص ۱۹۰ . 1 - آمروز نمی دستورعملبکار
رود. ععرب آن «یر نامج». «رزی>.
غله‌است (3201۷3 ۳۷2۵()) که درمازندران. کلان » استراباد.
خوزستان؛ اسفهان وبرخی‌تقاط دیگر ابران ودر هندوسثان شرفی
و ژاين و چن میروید . « فرهنکگ روستابی ۲۶۵ » « کل کلاب
=== HUB context ===
phi. a6 = ap. haca, sonst aber (in mp. Zwei- oder Mehr-
silblern) abfiel^):
be- *ohne* in Komp. = paz. awe-, phi. ape-, arm. ape-,
api^; beza, veza Vein' = paz. awUa Shk. 235, phi. apejak
oder opecak?; burna 'Jiingling' = paz. awarnai Shk. 238,
phi. apurnai, apurnayak, zd. aperendyu-, aperenayuka- ;
baxtar^)=^fsiz, awaxtar, phi. apaxtar, zd. apaxtara- *nord-
^) Yon diesem a ist das vorgeschlagene a (abiii 'Augenbraue*
= skr. bhru') zu unterschoiden.
bereta-j skr. bhrta- (dazu Uvurdafiy avaram = aram 'bringe') ;
burram *schneide' = ap. *bmamiy (oben p. 28) ; burz *hoch',
Alburz ein Gebirge', bidand *hoch* = zd. berez-, hereza^,
in Komp. berezi- *hoch*, hara-berezaifi , berezant- *hoch' =
skr. brhant- ; burna *Jungling' = zd. aperenayii- ; bus 'Hals,
Mahne*, phi. bm Gl. and Ind. 84, bal. busk 'Pferdemahne',
afgh. vrai, zd. baresa- (aus *brsa-); dmurzTdan 'verzeihen*,
skr. mrj (3. pi. mrjdnti) *abwischen, reinigen', zd. merez
Tflugschar*.
Lautgruppen mit r.
§ 156. Ap. rn bleibt als rn oder wird assimilirt zu
rr, das zu r vereinfacht werden kann.
a) rn bleibt in: burna, barnd *Jungling', zd. apere-
nCLyU", phi. apurndi, paz. awarnai Shk. 233 (neben pur
Voir = zd. perena-l); zarnt 'Auripigment* , arab. zamfq,
zarnfx, aber arm. zarik (Mos. Geogr.) *Auripigment, Ar-
senik' (= ap. *zarnii/a ftir zd. zaranya- *6old*) neben- 259 -
```


## [2026-09-07T18:21:29.600Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef leaves(p):\n    return open(p,encoding='utf-8',errors='replace').read().split('\\f')\nv1=leaves('BQT_v1_pages.txt'); v2=leaves('BQT_v2_pages.txt')\nfor i in (246,247,282,283):\n    print('=== v1 leaf',i,'(p~%d)'%(i-210 if i<300 else i-220),'===')\n    print(v1[i][:1500])\nEOF",
 "description": "BQT v1 pages 36 and 72"
}
```


### [2026-09-07T18:21:30.884Z] TOOL RESULT

```
=== v1 leaf 246 (p~36) ===
آزدن
رذن . بازای فارسی » بروزن و معنی
آزدن بلشد که خلانیدن سوزن وامشالآنست .-
و استره زنب واژنه وگ اشفا زدن نزدمك
سکدیگر را کوبند .
]رده بروزن آمدم .یمعئی رنگهکرده
و خلانیدم شده بلشد » اعم از سوزن وغیره .
3 بازای‌ظرسی, بروزننو ععنی‌دوم
آزده است که خلانیده شده و اجده ده شده
باشی اعم ا ]که باسوزن با چبزی یگ اد
1رد یتح لت و وزن سور ز سغنت
آزار است - وامر بآزردن وآزار دادن هم هست-
و ومعنی کج طبع نیز آمده است - ودر عربی‌نام
آیرا اهیم علبه‌اللام است‌چه بدراین هي علیه‌اللام
۰ ترح » تلم داشته است لیکن سد ازفوت تار ی
آزر اورا پرورده است ۷ .
زر واه ۴ هه یابایایجد بروزن‌مادرزاد
تلم بسر عاراسیند است و او موبدی موده از اولاد
ژردشت معاصراردشیر بایکان ودر آن زمان‌حکیمی
مانتد او نبوده است گر اردای بر وبرانی ۳
که اعلم از او بوده است -
]ررخش ۴ س بر وزن تاج بخش ۰
شورش و صاعقه را گوند عتی. سرما ورعدوبرة
رده س بقتح ثاث وسکون رابع وداا.
ایجد » بمعنی رنگ» ولون باشد .
۲ رده پشت «کنابه از پ رکوژیشت
باشد - و چاروایی را نیز گوبند که پشت او ز انم
و جراحت شده باشد .
آ دم * - پتح ثاك و سکون دابع
و حیم» چند معنی دارد : ۱-.حیا" و شوم باشد .
۲ - بزرگی و عزت و حرمت را کوند . ۳ .
تاب و طاقت بود . ۶ب رحم وشفقت ومپروححبت
و نرمی ومردمی وآدمت. 4- غم واندوه وتشگی
وسختی‌والم را گویند. -٩‏ عدل واتصاف و یکدلی
باشد. ۷- طاهر و آشکارا را گویند . ه سلاحتی
وراحت بود ۰ - نگاهداشت وباس خاطر وتحمل
یائد. *۱ - غب و قهر ر خشم را گویند .
۱- بخواری و زاری گذاشتن باشد. ۷۲- تقصیی
و گذاه را کویند. ۱۳ - بمعنی حسامان شدن‌باشد.
6 - دام دختر خسرو پروم است ۰۸ واو چهار
ماه پادشاهی کرد .
]زر میداخت ۰۷ بکی مم و خم
دال , نام دخترخسرو پرویز اس
=== v1 leaf 247 (p~37) ===
ده
آ زر نگ - بفتح رأیم بوزن با درنگه .
بمعلی غم سخت و محنت صعب و رنج و هلا کت
باشد - وبمعنی خیارسبز هم پنظ آمده است ٩‏ .
گت یتح الت وسکون خی تقطمدار»
درختان دیگر ببرند و آنرا بعریی * جلمه »
خوانند ؟ .
دوعص
ادع بزای فارسی » پروزن و معنی
آزغ‌است که شاخهای‌درخت بربده‌باشد؟ - ولیف
خرما را فیث گوشد ۰
آز فنداك - بفتح‌فا وسکون نون ودال
اد بالف کشده و یکاف زده 4 قوی قرح را
گویشد . ی
]رز فندا لك « بازای‌فارسی»بروژن‌ومعنی
آزفندالك اس که قوی قرح باشد -
1۳ ۳
] ذ گن « بازای فارسی ساکن وکس
کاف فارسی شوت زده » دری باشد که آ ترا مانتد
پنجره ساخته باشند و از ععب آن وان نگاه
(۱) چب ۲ , چش : آکندن .
آژنگه
کرد . *
] ز هثل » بامیم بروزن پای‌بنده خداوند
حرص داز باشد یمنی حریص وصاحب خواهش »
چهنند بمعنی صاحب وخداوند است . #
| د هون بر وزن واژگون , آزما
و امتحان رااگوینب ۴ ۰
]زر ند - با زای فارسی بر وزن یایند ء
کلی باش که بر روی خشت به نکنند و خشت
دیگر بربالای آنگذارند ‏ وگل و لای‌ته حوض
و جوی را نیز کوبند - و کلابه را هم گفتهاند .
آجیده کردن باشد .
 یتع‎
! ز ثف ین » بروزن‌واخندسن, درمیان
]زر زگ ت‌ بفتح ال وسکون رابع‌وکاف
فارسی , چين و شکنجی را کوین دکه بر روی
و آندام مردم اند خواه از ری و خواه ازروی
بسیاراست ؛ یکی دو مثال که بعض فرهنگها برای آزرنگه با زاه میآورند عن‌بسش شواهد آنرنگه
است و اما معنی خیار سب زکه باين کلمه داده اند پی شك اشتباهی است که ظاهرا تخت صلحب
اداة الفشلاء را دست داده است و مثشاء اشتباه کلمةٌ بادرنگه بوده که برای تعبی وزن آنرنگ دد
سخه ای دیده و آرا معنی‌کلمة آذرنگ صو رکرده است . < لفت نامه 5
۴ ره : آزمایش وآزمودن » درذیل .
ه آزمایش پهلوی صلاوز202ه مرکب از 2 + ۳2 « تب رک ۰۸ صه
ما2
=== v1 leaf 282 (p~72) ===
آهو پای
عب را نیز گفته اند "۱ خواه با مردم باشد و
خواء با چیزهای دبگر-
و یمعتی رم باشد که از
رمیدن است چه آحوبی
رمیدگی را کوبند - و
بمعنی قرباد و آواز بلئد . . ۳
عم آمنه است - و تام
مرضی و عأی حم صست احو
که آیزا جربی ضیق‌النفی خوانند - و بطریق
استماره چشم را نیز آهو مبگویند - و شاهد
و ممثوق را عم کنته ان .
]هو بای » با بای‌فارسی بالف کشده
و خالةٌ شش پپلو را گویند -
19
آهوردی با واو مجهول بی وزن
لاهوری » یمعنی‌خردل باشد ؛ و آن داروبی است
یار تند و نیز ؟ . 8 ۱
] هون بر وزن قارون » رخنه و قب
را کونند ۴
سم
"هون پر « بفئح بای ایجد بر وزن "
عالمتاب است .
آهوی لقن س بسن یآهوی‌خاورست
که کنابه از خورشید جهان آرا باشد .
" آهوی دی - کنابه از آفتاب
است - و صراحی طلا را نیز گفته‌اند .
هوی‌سیهین « ساتی سفید پوست را
گویند و آن صاحب حنئی است که در عجلس
بمردم شراب میدحد .
آهوی شیر اقکن - چن-طلوب
و تیش و مت ی
صست .
آهوی فاك. 0 از خورشید
است
از با اصافی کردن باشد .
۱ آهو یی - بکسر بای اول و سکون
بای ثأنی » بمعنی رمید کی ۷ و عیب ناکی باشد.
ول وعیب باه اکن :
یتیآن جاور که ژاید مك
2 ای‌مبا رکه منای آهویای
< بشت۱ ص۱۱۵ ب*.
ابوالفرج ردلی ۶ لخت نامه ‌.
گاه بررفتن ی است نیز
م شهاب طلحه . رک : ات ناعه.
۵ - بدل درفکندی چنان چاکه را
۷ - رمندگی لت نامه» .
که هشن آهون‌بران خا کت ۳ «لفت نامه».
مخز آحومند » مختل » مخبط :
زیبری مفزت آهومند گشته است
( برهان فاطع ۱۴)
=== v1 leaf 283 (p~73) ===
(۱) بىمنیآهو باش د که عربان«غزال» کوبند ۱ .
]هیافه » بکر تالك مروزن نازبانه »
استضوان بای دماغ را کویند و آنرا بیبی
وس وس نب ی 9
باشد لیکن" آباک سار واه است وبیی
«حناك» عیگوف .
آهیخت ۴ ت بر وزن آوبثت ؛
نی يکنی و برآورد 2 پاشدبا
ری ده
آهیختی ی ده
پر کشیدن و بر آوردن باشه مطلفا ۶..
آهیخته ۲
بر آورده و بر کشیده باشد .
و استفهام باشد - وگاء بجهت امتفار و استخبار
ت لغتی‌است درآ هو 0 نه هزواری .
بصول خواهد پیوست بانه ۰4 - و کاهی درمقام
ی » بر وزن آواز » نام غلام سلطان
محمود غزلوی بود - و بعضی کویند نام یکی از
امرای سلطان اپراهیم بن‌سعود بن محمودغز نوی
است ۵ .
[بشتنه ۷ - بای فردت شت و نون بروزن
دارشکنه , جاسوس را گویند - و بععنی‌چاپلوی
هم آمده است
ا یشم ۷ + بکر ثاكث و سکون شین
که پرتو ماه باشد -
و فتج نون » بمعتی آیشتنه است که جاسوی -
و چاپلوی باشد .
| یشه ۱ - بروزن عابشه ء بممنیآمشنه
است که جاسوس ۸ و چاپلوی باشد٩‏ .
و تای فرشت » پممنی حاجتی باشد که از خالق
؟ ‏ ره : آهیختن . ۴ ساژه‌صدر
متخ کردن 1 ۹ . رك : لفت نافه ..
کاندر این راه جمله را شرط اتتت
۷ .4 : اسشه..
ت کردن ب‌ براق کردن ‌
عثتق محمود و خدحت آباز .
سناگی « لفت نامه »
9 درنامداد فارسی ۳ آمده ات۰ .
واژه نامه ۲۱۶ ۰
و صحیفی است از آن : رك:: ابنشهن
و* اشبین » بمعنی نگاه کردن
۱- هلری 226 < افدیه و سهیکیه
اخه در صفحةٌ ۷6 :
```


## [2026-09-07T18:21:44.216Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(t))\nfor i in (247,248,249):\n    print('=== v2 leaf',i,'(p',i+540,') ===')\n    print(t[i][:1600])\n\"",
 "description": "BQT v2 p.788"
}
```


### [2026-09-07T18:21:45.641Z] TOOL RESULT

```
n 684
=== v2 leaf 247 (p 787 ) ===
 ‫خوره‬                                                                                                ‫اس‬


‫مودلد به دیر‪ ۴‬موسوم ساختند چه‌بزبان پهلوی‬            ‫حور ههر ‪ -‬من اول و سکون ثالی‬
                     ‫‪:‬‬   ‫را دیر گوند‬   ‫)‪۱‬‬   ‫گنف‬     ‫نام‬   ‫‪0‬‬   ‫بی لقطهٌ زده‬       ‫مھا ورای‬   ‫میم مکور‬      ‫‪£‬‬   ‫وئالت‬


‫خور نگاه ‪ .‬با انی معدوله یر وزن‬                                           ‫شمشیرسلیمانعلیهالسلام است ‪.‬‬
‫بهرام‬   ‫که عمارت‬   ‫انت‬   ‫یمعئی خورلق‬   ‫قدمگاه ‪۰‬‬
                                                       ‫مف‬        ‫‪:‬اثانی‌معدو له روزن‬        ‫حو ر ند ‪-‬‬
       ‫خانه را لگیز‬
 ‫وند © ‪.‬‬                    ‫کور بواشیدی‪-‬شگاه‬
                                                     ‫بمعنی درخور و زیبا و لابق باشد ‪ -‬و نام روز‬
                                                                      ‫‪۴‬‬   ‫‪۱‬‬       ‫ازهر ماه شمی‬   ‫دوآزدهم است‬



                    ‫ویشگاه خانه باشد‬        ‫گور =‬
                                                      ‫خور نق = بر وزن فرزدق » معرب‬
                                                    ‫»وان عمارتی نوده بار عالی که‬                 ‫‪۴‬‬   ‫ات‬       ‫خورنه‬

‫حو ر نه = بفتح‌اول وثانی ورابع‌وسکون‬                  ‫نعمان‌بن منذربجهت بهرام گورساخته بودوعجمان‬
‫ثالث بروزن ومعنی‌خورنق‌است که کوشك بهرام‬
                                ‫کو باشد ‪۷۰‬‬            ‫نبد‬
                                                        ‫گه‬‫نشستن بطعام خوردن» وقصر دوم را که س‬
‫حور ه ‪ ۸‬پیب بفتح اول‌وئالت و ثالی‌معدو له‬            ‫وبادتخانه تمام کرده‬
                    
=== v2 leaf 248 (p 788 ) ===
           ‫ات‬
            ‫سپو‬                                                                                                       ‫خوره‬


 ‫خورة استخر »‪.‬خورة داراب » خورة شایور‪ .‬خورة‬                               ‫بوری است از جالب خهای تعالی که بر خلابق‬
 ‫قباد ‪ - ۴‬و ناممرضی است مهلك وانرا بعربی‬                                  ‫بوسله آن فادر شو ند بر باست‬     ‫که‬    ‫فار مشود‬

 ‫جذام خوانند؟ ‪ .-‬ویفتح اول وسطون وفتح ثالث‬                                ‫وضمتها ‪ .‬و ازین نورآ نجه خاص است‬            ‫وخ_فتها‬
 ‫است که‬               ‫درختی‬    ‫آڼ‬    ‫‪9‬‬   ‫‪۰‬‬
                                             ‫خر زهره کروایند ‪۴‬‬             ‫بیادشاهان بزر که عالم و عادل تعلق مبگیرو ‪-‬‬
     ‫رت اف سای ‪۶‬‬                                      ‫و‬    ‫کان‬
     ‫بمعنی پابمال هم آمده اس‬                      ‫و‬   ‫دفلی خوانند ‪-‬‬        ‫<سد‬   ‫حکمای فری‌فاری رایپنج حصه کرده‌اند وه‬

‫ار‬        ‫|نرا بر‬
                ‫ا‬       ‫کد‬     ‫‪۵‬‬    ‫ی‬
                                    ‫اول نوعی از جوال ا ت‬       ‫وسم‬       ‫‪ :‬خورءا ردشیر ‪.‬‬   ‫ترهب‬
                                                                                              ‫نام نهادهأ ند ماين ت‬   ‫را خوره‬




     ‫=) است ( رک ‪ :‬خورة آردشیر) مجازاً‬
                                     ‫‪ - ۱‬ماین معنی نیز مأخوز ازه‌منی خوره ف(ر‬
     ‫خوره ( = خره ) را یمعئی ناجیه و بخش گرفته اند و اختصاص بقاری ندارد ‪ .‬معرب آن‬
     ‫«ولات پاری بنج کورندت ‪ .‬هر کورتی بیادشاهی که نهار آن‬                                                  ‫«کورة » است‬
         ‫‪۰‬ورة دارایجرد ک‪.‬ور
=== v2 leaf 249 (p 789 ) ===
```


## [2026-09-07T18:21:55.415Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"خشیسار\\|خشنسار\\|خشین\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -20; echo \"=== anushe ===\"; grep -n \"انوشه\" BQT_v1_pages.txt | head -10; echo \"=== anahita ===\"; grep -n \"آناهیتا\\|ناهید\" BQT_v1_pages.txt | head -10",
 "description": "grep BQT for xašan, anusheh, anahita"
}
```


### [2026-09-07T18:21:55.500Z] TOOL RESULT

```
incoming/BQT/BQT_v3_pages.txt:3650:‏۸ - مقلوب «خشنشار» = خشنسار (هم) ‎col‏ و رشیدی کوید « اصح خشبار است .
incoming/BQT/BQT_v3_pages.txt:4584:‏۴ لب چشمه‌ها برخشین سار و ‎gle‏
incoming/BQT/BQT_v3_pages.txt:26933:‏-فروآید زیشتش پورملعون . شدهکالفته چون خرسی‌خشینه. لبیبی«لفت فرس44۲.‎ ۴
BQT_v2_pages.txt:12527:‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
BQT_v2_pages.txt:12654:  ‫‪ - ۲‬مصحف خشنسار (ه‪.‬م‪ ).‬و(خشینسار‬                 ‫مخفف | خشیج (ھ‪.‬م‪(.‬‬           ‫خشیج»‬         ‫جمم‬      ‫‪-‬‬   ‫‪۹‬‬
BQT_v2_pages.txt:12662: ‫میماندچه خشین بازسیاه رنگه؛ وساربه‌عنی مالند‬             ‫بای فارسی وسکون‬     ‫بقح‬     ‫=‬   ‫ند‬     ‫حشن‬
BQT_v2_pages.txt:12666: ‫خشینه = بروزن دفینه ‪ ۰‬بمعنی خشین‬
BQT_v2_pages.txt:12673:‫رنگ است‪ .‬بکبودی مابل ‪ - ۴‬و بمعنی سفید‬                     ‫خشین ساد؟ ‪ -‬با سین بی نقطه بر‬
BQT_v2_pages.txt:13806:   ‫(«‪.‬م‪ ).‬ورك ‪ :‬خشین‬      ‫خشتار‬   ‫مصحف‬      ‫‪۳‬‬       ‫(«‪.‬م‪.).‬‬    ‫‪ - ۱‬مشفف «خنده خرش ‏‬
=== anushe ===
=== anahita ===
1582:و ناهید یعنی دختر ناریستان نیزموید این قول است » پس اصل در این لشت
1730:ومفولی پیوستگیداشته باشد.اين ز بان‌راخودساز نده‌اش زبان آسمانی‌ناهیده
1733:سپپر برین ۲ گاه‌نيستيم و باز بانپای‌چرخ » کیوانو ناهید آشذایی نداریم بهتر
1769:وفر لاس وورلاس‌خوانده میشو ند؛نامپای‌خرد وروآن‌وتن‌ناهید(زهره)نر وان
12338:ناهید بود وبسنی کویند اسکندر پیغمبرشد واورا
15874:(52520 موبد معبد اناهید دد استخر) ؛ و او نیز بشفل پدر متصوب کشت و وی پدر اردشیراول
17179:پالیك - بر ون ناهید . ماضی بالیدن
26390:پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
29024:ساخته‌اند وبهمن سب‌این نخت‌را «نخت خورشید» نز ناهیده‌اند . نخت طاوی در مواقع عادی »
```


## [2026-09-07T18:22:01.560Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'خشین باز سیاه' in l or 'خشین بازسیاه' in l or 'میماندچه خشین' in l:\n        print('leaf',i,'printed p',i+540)\n        print(l)\n        break\nEOF",
 "description": "Find BQT xašan page"
}
```


### [2026-09-07T18:22:02.893Z] TOOL RESULT

```
leaf 215 printed p 755
  ‫جع بت چدم‬                                                                                          ‫~ ‪۷۷‬‬


 ‫بنند که ییاز سیامرنگه‬    ‫وآ‬ ‫گهت‬
                               ‫را خشن سار بج‬
 ‫میماندچه خشین بازسیاه رنگه؛ وساربه‌عنی مالند‬             ‫بای فارسی وسکون‬     ‫بقح‬     ‫=‬   ‫ند‬     ‫حشن‬

                                             ‫باشف ‪.‬‬

 ‫خشینه = بروزن دفینه ‪ ۰‬بمعنی خشین‬
 ‫است که هر چیز سباه رنگه مابل (‪ )۱‬بکیودی‬
                                                          ‫ا وی زک نوی ار اچ ات ران‬
                                                          ‫بمفتی کبودرتگڭ‬     ‫خسن‬     ‫باشف جه‬    ‫می‬      ‫کیودرنگف‬

‫باشد ‪ - ۴‬و بازبرا نیز گوبند که پشت اوکبود‬                                       ‫وید یمعئی غلواح باشد ‪.‬‬
‫و ثیره رنگگ بود ؛ و بعضی گوبند مرغابی سیاه‬
‫رنگ است‪ .‬بکبودی مابل ‪ - ۴‬و بمعنی سفید‬                     ‫خشین ساد؟ ‪ -‬با سین بی نقطه بر‬
 ‫گلوهیند‬
       ‫و خودرنگ‌هم بمنظدرهآ‌است کهآ نرا م‬                ‫باشد که شت او‬      ‫نوعی از مرعای‬           ‫وزن زم‌ندار‬

                         ‫مشدد ‪.‬‬         ‫امم‬
                                          ‫لمی‬
                                            ‫وتح‬
                                              ‫بف‬          ‫داردواو‬   ‫سفیدی‬   ‫سرخال‬    ‫ویرمان‬     ‫ساه رنگف است‬




                                                 ‫بیان بدارهم‬

          ‫برسه لغت و کنات‬               ‫در خای نقطه دار با صاد بی‌نقطه مشتمل‬


       ‫ضدیتی که باهم دارند ‪.‬‬   ‫ار بعه است ببب‬             ‫وسل »‬       ‫» بنتح اول بورذزن‬             ‫حصل‬
 ‫چشم ‪ ۰‬کنابه از کطان‬        ‫حصم بك‬
                                                             ‫نرد وشرط وییمان درتیراندازی و گروبندی(‪)۲‬‬
‫است ‪ -‬و دجال را لگیوزبند ‪ -‬و بمعنی دلهم‬
                                                             ‫قمار نیزهست‪ = ۹‬ویمه‌نی کمبتین هم بنظرآمده‬
‫هت که بعربی قلب خوانند ‪ -‬وکنایه ازآسمان‬                                                                 ‫است ‪. ۷‬‬
                                             ‫باشد ‪.‬‬
                                                             ‫خصمان سفلي ‪ -‬کنابه از عناصر‬




                                             ‫(‪ )۲‬چش ‪ + :‬در ‪.‬‬                   ‫(‪ )۱‬جك ‪ :‬مائل‪.‬‬

                  ‫« افئین »‬    ‫مصحف‬      ‫‪,‬‬   ‫ظ‬    ‫حدود العالم و معجم البلدان نیامده ‪.‬‬      ‫در‬   ‫‪-‬‬   ‫‪۱‬‬

                         ‫(و‪ -‬م‪(.‬‬    ‫خشسار‬         ‫) =‬    ‫(ه‪.‬م‪٣+ (.‬‏ سار ) سر‬        ‫از ‪ 2‬خشن‬    ‫‪_۴‬‬

                                  ‫گتاکن (مروزی) گو ف ‪:۰‬‬             ‫جر مه رنك دود‬    ‫(خشمته‪.‬‬    ‫‪۳ ۳‬‬


               ‫که فرستد لبای حور المین‪».‬‬                             ‫خشننه را بهار‬    ‫کوهار‬

   ‫ورك ‪ :‬خشن ‪.‬‬    ‫‪۶‬‬     ‫«لفت فرس‬

               ‫(عر)‪ .‬رك ‪ :‬فاموس وشرح آن ‪:‬‬                ‫‪6‬‬            ‫رك ‪ :‬خشن » خشن ‪.‬‬              ‫‪۴‬‬

  ‫و نیز درعربی‌یکی‬      ‫‪۱‬‬           ‫‪.‬‬    ‫خصلت اصاف زخصلش مجوی ‪ .‬نظامی گنجوی «گنجینه ‪۲۵‬‬
                                                                  ‫ازنامهای لۇلۇ ‪«.‬الجماهر ببرونی‪. ۷۰۱‬‬
```


## [2026-09-07T18:22:15.723Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if 'انوشیروان' in l or 'انوش' in l:\n        print('leaf',i,'~p',i-215, l[:200].replace('\\n',' '))\nEOF",
 "description": "Find anush in BQT v1"
}
```


### [2026-09-07T18:22:17.035Z] TOOL RESULT

```
leaf 64 ~p -151 مقدمه شحاه وشش |ماهیچکد|م از خودنیر سید ندا گردساتدرست‌است چرا هيچيك ازفرهنگ-- هایی که پیش از بر هان‌قاطع نوشته‌شده لفت‌های آنرایاد نکرده‌اند؟ چرا دراشمار شعرای پیش از خودشان یکی‌از اين لفت‌ها هم‌دیده
leaf 67 ~p -148 پنجاه ونه دسانیر برهان‌رااصلاح کر ده ازروی خود دسانیر آسمانی‌ارزش ومعنی [ نبا رانگاشته است ؛ بسیار جای انسوس است که برهان قاطم وانجین آرا درایران‌طرف دای فا خلت جپانگازی و مجمم | لفر س‌سر وری که بپتر 
leaf 139 ~p -76 جد وس و يككث کتاب حاضر اتوء بطری »رادیو» کتری ؛ ماشین » مونوو وفیره. ِ ۱ بر ای تکمیل کتاب‌حاضر» برخیز اعلامرا که‌با تاریخ اعلام اضافی و ادب فارسی رابطه دارد در حاضه افزوده‌ایم مانند: آذ رکیوان »7زادچه
leaf 195 ~p -20 ٩۱ ۷‏ دستور ز بان پارمی دییگر واو مفتوح است و آن سه قسم میباشد: اول واو عطف است " و آن‌دو نوع بود : مکی آنکه‌مذ کور شد ودیگر؟ آنکه چون شخصی کلمه ای بگوید شخص‌دیگر ایشدا بواو کرده آن کلمه را تمام سازدچ
leaf 289 ~p 74 - ۷ - ایکا کبا و سکون الث و ها و رای قرشت ؛ نام اصلی نیشابور است و ممدن فیروزه آلجاست ٩‏ . ابر قباك ع من فان . نام ولایتی است از توابم اره جان ۱ که میان اهواز و فاری واقم است و آباد کرد قباد شهربار اس
leaf 309 ~p 94 خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است وتا کردة اوست . اردجان س با جیم بر وزن همزبان» از جد اول اهل نجوم است و در احکام مرقوم. ار دش 7 س بفتح اول و ثانی وضم‌دال می نفطه و سکون‌شن نفطه دار , 
leaf 329 ~p 114 ۱ << رومی است . 1 2 بکویتد و باشیر تازه بیامیز ند وبرزیر خصه‌بمالند نموظ عجبآورد۱ اساسه بفتح نی رو اس : بمعتی نگرستن بگوشة چشم ووایس دیدن‌باشد ۴ وبکی اول نیز گفته اند . اسا لیطوس یکی لام و سکون تحنالی
leaf 346 ~p 131 که آنسخها از بدن اوجته برآن کس میخورد وفرومیرود ؛ و گویندهرچنداورا بز ند فربه‌ترشود. که خاریشت بر انداز باشد . اسفا دور بفتح اول وسکون ئانی و قای بالف کشیده و بای ابجد بواو دسیده و بای قرشت زده » نام 
leaf 411 ~p 196 ۱ اهور * - بنتع اول و ثالث و سکون ثانی و زای نقطمدار ۰ نلم تیرآندازی بوده بفایت قادرانداز در زمان انوشیروان » کوبند باسیف ذو بزن (۱) همراه شده بود . بادشاه حبشهرابيك‌تبر بر روی نخت کشت و ملکش راگرفت .
leaf 415 ~p 200 وه آبرسا اول نیشاپور است ۷ . از پادشاهان بابل هم بوده است ار ج ‏ بکسراول و سکون ثانی‌مجهول الیرسا « بکس اول و سکون انیوثاك و #الك مقتوح بجیم زده ؛ نام پس فربدون است | و سین بی‌فقطٌبالف کشیده » بیونانی
leaf 467 ~p 252 ۷ ۱ : ۱ برانه پر اغلیدن - بروزن‌جفا کنیدن» مخخف برآغالیدن است که بمنیتحرض (۱) کردن وبر انگیختن باشد و بعربی اغرا هگویند . بر ااق‌جم « کنابه ازبادی اس تکه‌تخت سلیمان علیه‌السلام را میبرد . بر ! کوه (۷)
leaf 468 ~p 253 براو او هتح اول و سون آخ رکهراو بر ) و ددهسررزن سرایرد» ». شخصیرا کویند که‌امرا وسلاخین اورابلند مرنبه گردانیده بباشند - و بمعنی بنا و امای و دیوار عمارت‌هم آمده است - و بمعتی قلمه و حصار نیز هست - و 
leaf 493 ~p 278 آب بندند( ‏ و سکون ثابی گوی باشد که آب درآن جمع شود - و رنگهآبرا نیز کوبند . * بز چا لهفلاك - کنابه از برج جدی است . بز سم - بنتح اول و انی و سین بی قطه و میم. و سکون الك . جل وزغ را گویند و آن چیز سب
leaf 584 ~p 369 ۳ پای‌اوز اده ختح همزه و سکون واو و زای فارسی بالف کشیده و رای بیط مقئوح» بععنی دویم پای افزار است. وان‌دوتختة کوچك باشد باندام نعلین که بافند کان بوفت پای باف ‏ با بای‌اببد,الف کشیدهرفا زده : حولاخه 
leaf 619 ~p 404 همت و مضاوت وخوش رفتاری و جلوه کردن‌هم اه اطع پر و یز قلاك «کنایه از خورشیداست. رو لزان ه بروزن گردبدن » آلتی باشد که‌بدان! ردوشکر و ادوبة حارة کوفته پرومزن و امثارآن بیژ ند . روش - با بای مجپول بر وز
leaf 749 ~p 534 زو کت 1 مکلرها کوچك ومسندی که کم‌بدست آ بده هم آمدماست. لطات و نهایت آبی دوعی از بلور است در غایت لطافت تنگ دوی» نم ثانی » کنابه از شهرت . دی خخصی است که باندك مبالفه مطلب بزرگی را لگ فتر < ۱ تشگ ه بک
```


## [2026-09-07T18:22:25.891Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD n'krtk ===\"; grep -n \"krtk\\|nʾkrtk\\|n'krtk\" SOD_pages.txt | head -20; echo \"=== SOD entry 32 area ===\"; grep -n \"^ *32 \\|uncoined\\|نقره\" SOD_pages.txt | head -20",
 "description": "SOD lookups"
}
```


### [2026-09-07T18:22:25.957Z] TOOL RESULT

```
=== SOD n'krtk ===
4202:    akarte (»krtk)                                        150 "m'k =» >myk
4242:142 »krtk =* »k'rtk                                       158 "m'tk ** »m>t>k
6009:                                                                        (o)krt-kare, oki-karc      ©Parth. krtkny\ Pahl.
6086:    (o)krte Okrtyy, >krt'k, *krtkt 'ktyy, }qtyy) ©ace.               overseer
6099:822 >krtk => >krt>y                                                 GMS
6987:      anskartc Onskrtk) ©pp.                                                 group, assembly
6991: 1119 'nskrtk =¥ 'nskrt'y
20207:                                                                      0-u na-krte, nak(s)te, nakarte (n'krt'y, n>krtk)
20234:                                                                      5761 n'krtk -> n»krt>k
20243: 5762 n'krtkvwnc B                                                            ^            (o/)silver, silvern
20249: 5763 n>krtk-(w) B, S
29033:     stupid                                                 8789 skrtky'h M                           iSMjz'Jj*?
=== SOD entry 32 area ===
3960:  32 "cYy B                                       fjLoU
```


## [2026-09-07T18:22:28.162Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('n',len(leaves))\nfor i,l in enumerate(leaves):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    pdf=int(m.group(1)) if m else i+1\n    if 'نستوه' in l or 'نقره' in l:\n        print('leaf',i,'pdf',pdf,'printed',pdf+1917, [w for w in ['نستوه','نقره'] if w in l])\nEOF",
 "description": "BQT v4 nastuh/noqreh pages"
}
```


### [2026-09-07T18:22:29.406Z] TOOL RESULT

```
n 553
leaf 40 pdf 41 printed 1958 ['نقره']
leaf 51 pdf 52 printed 1969 ['نقره']
leaf 115 pdf 116 printed 2033 ['نقره']
leaf 141 pdf 142 printed 2059 ['نقره']
leaf 200 pdf 201 printed 2118 ['نقره']
leaf 217 pdf 218 printed 2135 ['نقره']
leaf 239 pdf 240 printed 2157 ['نقره']
leaf 240 pdf 241 printed 2158 ['نقره']
leaf 328 pdf 329 printed 2246 ['نقره']
leaf 331 pdf 332 printed 2249 ['نقره']
leaf 359 pdf 360 printed 2277 ['نقره']
leaf 400 pdf 401 printed 2318 ['نقره']
leaf 427 pdf 428 printed 2345 ['نقره']
leaf 433 pdf 434 printed 2351 ['نقره']
leaf 550 pdf 551 printed 2468 ['نقره']
```


## [2026-09-07T18:22:35.620Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20195,20260p' SOD_pages.txt",
 "description": "SOD nakrtk entry"
}
```


### [2026-09-07T18:22:35.663Z] TOOL RESULT

```
         5744 nYn     B                                                     BSTii 889.21; Benv. JA 1955, 310; C2, 27R10 "not

h             naxa/un (n'yn) (DKhot. nahane
              nail                                                     5755 nVstn'k
                                                                              desiring" B          (U->;/ ^     :jt^>)v^U «>^J
                                                                            nak-astane
              VJ 1465, 1468, 1477; TSP 5.1, 11, 68, 88; nTn,
                                                                           bathing poo\(dragon-pond)
                TSP 2.456; Gersh. AHM 277n; Bailey. Prolexis
                                                                           TSP 3.126; BSTBL, Vim. 80; GMS 1118
                 132                                                          =>n'qty
        5745 nVr B                          *j>s«lj£ <Uifc Jj£ oy     5756 nWk       B                  (•>J'li)SJLJsc*ji
                                                                      0-u na-krte, nak(s)te, nakarte (n'krt'y, n>krtk)
             naxar -^n'h'r
             foodless, without food, in fast                                si\ver(not coined)
             GMS 63; Gersh. Sogd. Cpds. 1945, 142; VJ 317,
                                                                            VJ 85, 55d, 558, 618, 8C; BSTBL, Dhy. 259,
               1092; TSP 3.50; Benv. "not able to walk"                       n>krt}kw; VJ 46, 12(, 976, n'krt'y, VJ 84, 494,
        5746 n*yn ■* nYn                                                      1163; Dhy. 257
                                                         ;Lu i^^jUU
        5747 n'yrpty M
                                                                      5757 n'krt'y B =» n'krt'k
             na-yarPde, na-yrapde
             incomprehensible                                         5758 n5krt>y p>my B                                   ^*j6
                                                                           na-krte- Pame
             GMS 1158-9
                                                                            silver coloured
        5748 n^rpyny      M
                                                                            BSTBL, Dhy. 262
             na-yarPene =»L} yrPyny
             ignorant                                                 5759 n'kr^yn'k    B                                  ^j,
                                                               OfcU
             GMS 1157, 1636                                                 nakrtene (n'krt'yn'y, n'krtyn'k) ^n'ktn'k,
    !
        5749 n^wstw'nypttL'ywstw'nyf) S(M) ^x^of>*l                          n^tynyy, n'krtynch
                                                                           silvern
            na-xustwanift                                                  BSTBL, Dhy. 259, 260, 261
            one who does not practise confession                      5760 n'krt'yn'y =» n'krt'yn'k, n'ktynyy
            GMS 1160
                                                                      5761 n'krtk -> n»krt>k
                                                                                                                                         n'mqyn
                                                                                               —■^■^^^AHH^^^M^^
                                                                                                                                              mmm


 231


 5762 n'krtkvwnc B                                                            ^            (o/)silver, silvern
      na-krte-yonc                                                   j/»j*                 GMS 1054; Hen. Tales. 473.47; BBB
        silvern
                                                                                      5774 n'm     *                    (0>>>^       j-O^.^^
        BSTBL, Dhy. 290, 292                                                               nam ©<naman-        ©ob. -y; pi. -/
                                       >n*qty                                              name
 5763 n>krtk-(w) B, S
                                                                                           GMS 332, 940
      na-krte, nak(ar)taku
      silver                                                                          5775 n'm-     B, C, S                         ^b^jU
                                                                                           nam
        VJ 46, 12(, 976; Anc. Lett. 5.10, 21, 22, 27;
          BSTBL, Dhy. z*0, 292                                                             (fo)be named
 5764 n'krtyn'k =* n'krt'yn'k                                                              GMS 604; VJ 151, 412, 48d; TSP; BSTBL, Dhu. 95,
                                                                                             Dhy. 388; STi; Sund. AoFviii 1981 p2l6; BSTii
 5765 n'krtynch S                                                          ^ju                -t(h)C2, 1R17, 18, 94R12; MDii Nov. 3R5
                                                                                             826:
      na-k(or)tenc, nakrtcne           ©f. adj. =»n}ktync,
```


## [2026-09-07T18:22:36.809Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[239][:2500])\nEOF",
 "description": "BQT p.2157"
}
```


### [2026-09-07T18:22:38.069Z] TOOL RESULT

```
[pdf page 240]
-۱۷- ره
کربا راگوبند ۱ - و بمعتی فریاد همست ۲ | تختانی » حکم وفرمانی باش که سلاطین وحکام
- وعربان گریز راگویند که از کربختن‌است ۴. | بجهت جمع شدن و کرد آمدن سپاء ار لشکر

نغیر نامه - بفتح اول و کسرنانی‌وسکون | می نوسند (۱).
بیان شانزدهم
درنون با قاف مشتمل برسی وسه لغت و کنایت
نقاب خصرا - کنتابه از آسمان | بهردومعثی آمده است 8 .
است ۴ . نقد شش روزه * - کنایه ازدیا
نقاب ثیلی - کنایه از مب است که و مافیها امت ۴ .
بمربی لیل کوبند ۴ . فقد گیر ان ‎٩‏ «کنایه ازمردمانی باشد
نقد جان - کنایه از جان است که | که رشوت میگیرند ورشوت میخوراد - وطالبان
روح باشد - وزر وسیم سره رایج را نیز گفته‌اند. دیا را ی ز کوبند ۴ .
نقد روآن - بسمنی‌نند جان است که فقره « بنم اول, معروف است که بعریی
کنایه از جان - و زر وسیم رایج باشد چه روان | فنه‌کوبند ۷ - وکنایه ازهرچیز سفید هم‌هت
(۱) چش : لوسند . َ
۱ - شکل قدیمترآن « بیور» .کردی 3811۳8 (شیپور) « ژابا ص 4۲۲ > » معرب نقیر
« دزی ج ۲ ص ۷۶۰ >. مجازاً قضمی ازکرباکه بیشترفلندران دارند وبآن « شاخ نقیر» و «بوق
اغیر» هم کویند « فرهنگه نظام ».- درموسیقی نام آوازست ازدستگاه همایون «فرهنگه نظام».
۴ - نه من کردم از دست جورت لفیر که خلفی ز خلفی یکی کشته کیی :
5 سمدی 2 فرهنگه نظام > .۰

و رك : تذکرةالاولیاه چاپ اروپا ج ۱ ص۲۱۱ یه ۴ - (عر) « نفیرکامیر » گروه هردم

ازسه تا ده - وفومی که بکاری‌پیش روند وبا کسی کریزند پاازهم گربزند درجنگه.*«متتهی‌الارب».

۴ - رك : رشیدی - * - ر4 : روان . ‎٩‏ - جمع « نقدکیر» ( از: تقد

(عر) + کیرل کیرنده] ).

۷ - درسندی 87۴۲۸ (سیم) رل : 60۳82۵176 46 89921 ,3.860۷601816

5 .۱929,0 و۲ ۰ عناندم عس 2 5808416006۰ وآن مر کیت از*8 (۱ه نا) مد

(کرده)؛ و عراد نامسکوء است (از افادات شفاهی استاد بنولیست) . درعربی ممانی‌متعدد

دارد از جمله « القطمةالمذاية من‌الذهب والفسة . وفی‌الاساس ( من‌الفضة ) .> «اقرب‌الموارد > ولی
بمعنی‌سیم وسیم درمعدن مستحدث است "یدزی اج ص۱۰ >. فلزی قیمتی‌سپید رنگه ده ازجهت

آرزشی پی از زر (طلا) قرار دارد :

تنش نقرغ پاك و رخ چون بهشت برو بر لبینی يك اددام زشت .
فردوسی طوسی « شاهنامه بخ ج اص ۱۳۷ . دربارة تر کیب اضافی « سیم نقره > رله: نهج‌الادب

ی ۰۵۸-۹۵۷
```


## [2026-09-07T18:22:57.591Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(t))\nprint(t[98][:1200])\n\"",
 "description": "SOD printed page 32"
}
```


### [2026-09-07T18:22:58.863Z] TOOL RESULT

```
n 645
                                                                                                                        'kySrp




33

     sinner                                                           TSP 2; Hen. Texts. 716; GMS 1558
     GMS      1125                                               854 'kwprm =» )kw5prm
                                                                 855 >kwrS(5) M                                           UT
841 'kt'nyy M                                        .lAjUjlT
                                                                     kur5 =»kwr5(5), qwrG
    (o)ktani ^'kr^nyCh), qt>ny                                       where
    sin, evil deed
                                                                      GMS 159, 1533
    BBB f9, 24; GMS 1035, 1038

842 >ktVk M                                          u^<*^3      856 'kwrts'r =» kwrts}r
    (o)kt-ark ©ob. pi. -tyy                                      857 'kws'nyk S
    dutiful, having carried out
                                                                      kosanik      ^kws'nyk^
    Gcrsh. Sogd. Cpds. 142; Sund. KG 2328
```


## [2026-09-07T18:22:59.099Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"نكر\\|نكير\\|منكر\" TAD_pages.txt | head -20; echo \"=== TAD leaves ===\"; python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('n',len(t))\nfor i in (66,67,68,69,70):\n    print('--- leaf',i,'---'); print(t[i][:600])\n\"",
 "description": "TAD nakara"
}
```


### [2026-09-07T18:23:00.624Z] TOOL RESULT

```
32: ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬
80:‫فاى أن هذهالطريقةلابعتزيقاةلالكلام معبانكرة وممهما‬   ‫يربخفل‬‫أمونضاع الع‬
123: ‫الكمرتى أوالمنكرت و خنع ءانه وقأدة الحامض ذو‪ 7‬نت لاله بوجد فرق‬
259: ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬
=== TAD leaves ===
n 87
--- leaf 66 ---
‫فاتدير سموا به وحيد القرن على سبيل المشاعبة أدذمهها ‪:50‬عتاوهاء فراسوه‬
‫وعر وه كروكدحنأييد القرن الهنديويوز أنيكون الاسمفينيقي« قرنإحد»‬
                                                        ‫أي وحيد القرن‬
               ‫كستك وكشتبج فارمبي ‪ 9‬ع ‪ 6‬معناه خبط غليظ‬

‫الوا ‪:‬فاه ونيفاة‬            ‫“كتوفت لعن بوالقين الفولة حمر‬
‫تقممان النوروقدتكسف الشمس لهاولة القمربينهاويين الارض مرادفه احتجي‬
‫"ابح لاتق دءمفادن وهو شجر وف اليونانية «م«ماوةا سمي‬
                                   ‫باسممدينة فى بلاد اليونان مهدا الامبر‬

        ‫"تان حب فارسي « انكشتانه » معناه اصبعي مرادفه فمالخباط
--- leaf 67 ---
  ‫‪ 1‬وبراد به منطقة من شعر ‪1‬‬            ‫فارسي « كر ‪ 4‬ا‬              ‫‪0‬‬      ‫‪3‬‬

                                                                       ‫اعلحىقوين‬
‫اه فى الغارسية والتركية مرادفه دار التمكس وما يؤخد‬           ‫كلك سوم‬
                                   ‫على البضائع والسلم ‪ 0‬له مكساج مكوس‬
   ‫كنحة ‪ 9‬فسارسي «كانجه » وهيآلةطرب ذات أوتار تشبه الربابة‬
              ‫كنار مدفازني‪ «:‬كنار »وهو اقيق أ بهل شير المدد‬
 ‫“نار أتوار تسرهو عماتور مقن "لزان يللد الوص ال غار‬
                                                       ‫كناريا فى غرى افريقية‬
        ‫‪ 0-5‬
--- leaf 68 ---
                               ‫به اسه‬   ‫سكم‬




‫نونانى عترمهط وهي حشيشة تقتل برائحنها البراغيث والختافس‬              ‫‪5‬‬
                                                         ‫اشةغيث‬
                                                              ‫رشي‬
                                                                ‫اقالل لبهاح‬
                                                                          ‫وي‬
‫«نوشتا » الارامية لا من ‪8‬زهقاكاتاه إليونانية ومعناها‬
                                                   ‫كندسة ‏ من ك‬
                                                         
--- leaf 69 ---
                               ‫اخسب سد‬
                            ‫الكشك مرادفه المبضوم أي مطبوخ المعدة والخثارة‬
 ‫بوناني تسطنةمعم‪ -‬أواتك معناه الف غرام وهو بساوي ؟الم‬        ‫كيلوغرام‬    ‫[ْ‬


          ‫‪.٠‬‏‬   ‫‪73‬‬                    ‫ة‬   ‫‪8‬‬           ‫‏‪٠.‬‬
 ‫يمس معئاه سيال وعصارة وف العلب هو‬              ‫وين ‪ -‬وونابي ‪5‬‬
‫استحالة الطعام فى المدة بعد الحضم الجوعر اشر هو مادة عتنة” الى الامقراد‬
          ‫تأخذ لونها غالبامنلونالغذاء الذي تتحلبمنهمرادفه عصارة الحضم‬
 ‫كيميا ‏ في اليونانية ‪#‬نسيرا معنا اختلاط وامئزاج وهو الاكير عند‬
                               ‫القد
--- leaf 70 ---
                                 ‫ف أفنا© ممناه ست من محاس يفسل فيه‬
‫ا وقد يكال‬        ‫الث ‪ -‬فارسي‪ 0‬نك © وهوصبغأجمريصبغبهويطلى‬
                                      ‫الابطالية و‪ 21‬والى الافر نسية ‪6921‬‬
              ‫لما نونالي ‪ 580021‬معنأه لامعوالمراد به السراج والمصباح‬
‫أوجادت اللقنازيية ليهولزها ‪#‬جنقا عن اتناك يلاهالحتد كرت انيه‬
‫هندي وهو نبات يعرش له سنوف فها حبوب لونما أبيض وأحمر ويقال له‬
                   ‫‪1‬‬                                           ‫الدرجر والثامر‬
‫تركواو قدا شعوق التو ‪:‬ولوذا فىالنازسية لاون عن‬                        ‫‪0‬‬
```


## [2026-09-07T18:23:23.514Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ne\\.\\|^ne \\|ne-. Not\\|Not. 1\\.\" AHD_watkins1985.txt | head -20; echo \"---\"; grep -n \"nescire\\|nescius\\|nullus\\|negare\\|neg-\" AHD_watkins1985.txt | head -20",
 "description": "AHD ne root"
}
```


### [2026-09-07T18:23:23.585Z] TOOL RESULT

```
774:ne. Not. 1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nd, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO!, NO2, NONE, (NoR!), NOT, NOTHING; b. Old Norse ne, not: NAY; c. Old High German ne, ni, not: NIx?. 2. Latin ne-, not, and nullus, none (ne- + illus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY, NULLIPARA. 3. Latin nimis, too much, exces-
---
774:ne. Not. 1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nd, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO!, NO2, NONE, (NoR!), NOT, NOTHING; b. Old Norse ne, not: NAY; c. Old High German ne, ni, not: NIx?. 2. Latin ne-, not, and nullus, none (ne- + illus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY, NULLIPARA. 3. Latin nimis, too much, exces-
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
971:sneg-. To creep; creeping thing. 1. Suffixed o-grade form *snog-on- in Germanic *snak-6n- in Old English snaca, snake: SNAKE. 2. Variant Germanic root *sneg- in suf- fixed o-grade form *snag-ila- in Old English snzxg(e)l, sneg(ejl, snail: SNAIL. [Pok. ? sneig- 974.]
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
```


## [2026-09-07T18:23:24.548Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(70,87):\n    print('--- leaf',i,'---', t[i][:200].replace('\\n',' '))\n\"",
 "description": "TAD later leaves"
}
```


### [2026-09-07T18:23:25.755Z] TOOL RESULT

```
--- leaf 70 ---                                  ‫ف أفنا© ممناه ست من محاس يفسل فيه‬ ‫ا وقد يكال‬        ‫الث ‪ -‬فارسي‪ 0‬نك © وهوصبغأجمريصبغبهويطلى‬                                       ‫الابطالية و‪ 21‬والى الافر
--- leaf 71 ---                                    ‫بين‬                                      ‫عدؤ‬                                        ‫مع‬                      ‫ومارعندنا وعندم بر داد به قدرس أمام أسمالقديس خاصة
--- leaf 72 ---                                                       ‫سسيم اإ‪#‬ا‪ 9‬اصمع‬     ‫بالابطالية هنائةودعدده على سبيل الاستعارة وهو الاقحوان زهر معروف ‪ .‬أما‬                                              
--- leaf 73 ---   ‫و‪ 060‬راقب‬           ‫وونانى مركب من معازم أي صغير ‪0‬‬                             ‫كرس كونة‬                                                                ‫ورصد مرادفه مجهر‬ ‫النسكاج على الأشي
--- leaf 74 ---                                      ‫فيه انهكانموجودا قبل التاريخ فقط‬  ‫مناورات عا افرنسي ‪67‬ناوهتلةتة فى الاصل اللاتيتي معناه عاملليد‬                                                ‫ولكنترادباهلآ
--- leaf 75 ---  ‫مينا ‪ -‬مأخوذ ممنينا الفارسي وهذا من اندسة الافرنسي وهذا من‬  ‫‪ 0‬الايطالى وهذا من هنااقتتدة الجرماتى وهذا مظنالم العربى وبراد به يللاء‬  ‫مركب من سحيق الزجاج والصوان والقلى وغبرها "كان عرب الاندل
--- leaf 76 ---                                  ‫يي للد‬   ‫سس‬     ‫اصل سكن معبد أي مكان الرحال في‬                              ‫انالهلفي‬                                     ‫‪-‬ذلى وموم مع‬                      
--- leaf 77 ---                  ‫وي‬                   ‫عبرشت ‪ -‬فارسي م ركبمننمأي نصف وبرشمتشأي‬                                            ‫‪ -- 0‬فارمي « ثامه » معناه كتاب‬      ‫‪3‬لوىاهط ( ولشا )‬             
--- leaf 78 ---                                           ‫‪6» 8 5‬‬                     ‫سكمس‬                       ‫ونالى وهاه وهو الطنياوة والدارة حولالقمر واك‬                   ‫هالة ‪-‬‬   ‫وعتكر دقاكنة‬      
--- leaf 79 ---  ‫العرب اليكل مجازاً الضخم من الحيوان فقالوا فرس هيكل وللطويل من النبات‬ ‫أما استعاله فى حلبعمنى المذبح فخهطواء فاحش ومخالف المعنى الرمزي الذ‪:‬‬ ‫«ل ‪ 6‬الذييستعمله بعضهم فزمىاتنا عه‬    ‫ينك‬ ‫هىا‬ 
--- leaf 80 --- ‫بانسون ب وثانى «مونسة وهو نبات زهره اسن طن الرانحة ويستقطرون‬                                                            ‫ققيمعنه‬                                                                 ‫الن
--- leaf 81 --- ‫افسىه ‪ :‬البرهان يبان الحجة مالنبرهرهة وهي البيضاء‬  ‫سري‬                                                      ‫أمخش‬                                                         ‫قال الز‬  ‫‪ 0‬اري كاا
--- leaf 82 ---                                   ‫لامؤلف نسه‬ ‫‪-‬تاناتةأتصوع قا تتساعق أمظ‬                          ‫بع‪2‬صده‪ 1‬ت‬        ‫‪1‬‬                       ‫‪“. 51‬أ‬  ‫ملعم ‪1‬ام ‪0‬‬   ‫ب‪,‬أناءلاطأرا
--- leaf 83 ---                                  ‫‪0000‬‬       ‫املب فاليمأأوس من ‪.‬تن الاغة العربية والاصطلاحات‬                                                 ‫طعج‬                                               
--- leaf 84 --- 
--- leaf 85 ---                         ‫‪:‬ات عاهر بيهقيمة‬                                        ‫مطبو ع‬    ‫تطلب من مكتبة العرب لصاحبها الشيخ بوسف توما البستانى بالفحالة عصر‬                          ‫لذن قرش صا
--- leaf 86 ---
```


## [2026-09-07T18:23:43.650Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"anāhita\" \"anahita\" \"anaoša\" \"anaosa\" \"axšaēna\" \"axsaena\" \"akarana\" \"amuyamna\" \"anušant\" \"anusant\" \"apərənāyu\" \"aperenayu\" \"zarəmaya\" \"zarema\" \"ništāvah\" \"nistavah\" \"uštavah\"; do echo \"--- $w\"; grep -n -i \"$w\" BRT.txt | head -4; done",
 "description": "Bartholomae greps"
}
```


### [2026-09-07T18:23:45.037Z] TOOL RESULT

```
--- anāhita
--- anahita
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
--- anaoša
--- anaosa
--- axšaēna
--- axsaena
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
--- akarana
3211:'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
4247:uranfinglich' :  akarana  'ra  asaonS  sUs^sA.) YtÄ48;  F.  7.  a)  'ra  raocä  (iA.)  "die!
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
26561:—  asmamm  ..  *gaä^Im  *gaH&yayä  stSis Vr.  7. 4.  a)  mit  GS.  aiaone{^^.  251  u.): yaca  upairi  (sd.)  iS  akarana  anayra  a^acnS Sil/  aSi  Yt.  Ä",  48;  —  ^antim  trvamm mainyava  stx/*asaonS data  .w(Sp.a76ni.) V.  2.  igPüZ.  et)  mit  vlspa--.  vTspqm asaenS  stim  .  .  mainynfm/ä  gaihyqmcä Y.  3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g;
--- amuyamna
5815:•  j.  a-st9n»ta-  Adj.  'nicht  niederzuwerfen': 'taca  amuyamna  yazamaide  Vr.  7.  i.
25241:•  ].,  g.  raziita-  Adj.  (fem.  *ta-)  'der  ge- radeste, richtigste,  rechtlichste,  gerechteste': *ya%a  *äis  lä  J  vansaitl  yä  data  ataJau! paouruyehyä  ratüi  iyaohana  °tä  (APn.) dngvata^ä  hya^cä  *aiäomye^aca . .  "wie es  den  Gesetzen  fiir  das  erste  Leben  ge- mäss ist,  so  wird  er  (näml.  Zara^u/tra) als  Richter  in  gerechtestem  Tun  gegen den  27rt(fgenossen  verfahren  und  gegen den,  bei  dem . ."  Y.j;^.  i''.  a)  von^an- tay-  (usw.) :  °öw  pantqm  daoaiti  ätars  . . ySi  ftißirym  lUfil  aiwidruzinÜ  "den  ge- radesten Pfad  gibt  (weist)  A.  .  .  denen, die  . ."  Yt  /o.  3;  —  mit  3  und  Abi.  oder Akk.  'hin  —  zu':  'tah^  pa%S .  .yS  asti  't3 j  aiäi  vahist)m!a  oASrn  asaonqm  "des geradesten  Pfeds  . .,  der  der  geradeste  ist hin  zu  Asa  und  zum  besten  Leben  der Gerechten"  Y.  6Ä  13.  a)  ahatpantay- (usw.),  das  aber  hinzuzudenken  ist:  yö dai^hsus  rqxlyqi^yh para  •/Jfnäml^a^i) baraiti  Yt.  io,  37*';  —  äid3?ar?nä  nastö •ta  (näml.  /a^a)  ". .  der  vom  geradesten Weg  abgegangen  ist"  Yt.  10. 105^';  — amuyamna  (sd.)  'tanqm  (näml.  pa^qm) Vi.17.1j;  13.3s-  b)  von  rainav-  m. (Stverz):  rar'hus 'tH  V.  13.  g  PUZ.jusw.;  — 'tfm,  'tat,  •iahe,  'ta  (VS.).  A)  mit  asts-  f. (Stverz.)  Name  einer  Gottheit:  °ta  ästa \'t.i6.7  usw.;   —  'tqm,  'taya,  'te  (VSf.).
30509:I  gegeben,    gehörig  verkündet':    saauhasca \paiti  °taya  . .  amuyamnaya  . .  avarwnnayä Yty.133. I      ')   So   NA.   nach   Mf3;    aber  F  I,  J  10  usw.
--- anušant
--- anusant
4535:•  j.  an-uso  Adv.:  s.  anusant-,
--- apərənāyu
--- aperenayu
--- zarəmaya
--- zarema
--- ništāvah
--- nistavah
--- uštavah
```


## [2026-09-07T18:23:58.344Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"nahita-\" \"naosa-\" \"muyamna-\" \"anusant-\" \"xsaena-\" \"p9r9nayu\" \"perenayu\" \"pornayu\" \"zar9m\" \"zaram\" \"dug9dar\" \"dugdar\" \"nyus\" \"us.tav\" \"ustav\"; do echo \"--- $w\"; grep -n -- \"$w\" BRT.txt | head -3; done",
 "description": "BRT OCR-tolerant greps"
}
```


### [2026-09-07T18:23:59.650Z] TOOL RESULT

```
--- nahita-
--- naosa-
--- muyamna-
--- anusant-
4535:•  j.  an-uso  Adv.:  s.  anusant-,
--- xsaena-
--- p9r9nayu
--- perenayu
--- pornayu
--- zar9m
14683:•  j.  9-ri.zar9maya-  i)  Adj.  'drei  Frühlinge umfassend':  yS  'malm  ratüm  aiwyänkqm (sd.)  nBit  aiwyästi  V,  s8. 9.  a)  n.  'Zeit- raum von  drei  FrUblingen  (sva.  Jahren)': 'maOn  xratOm  asavanfm  aiwyäiahal  (sd.) N.Ji.
19658:•  j.  mai8yöi.zar9maya-')  m,  Name  der Gottheit  der  ersten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*> (mit  dem  letzten,  45.  als  Haupttag):  'maem Payanhim  (sd.)  alavansm  alahe  ratäm  Vr. 2.3;  Y.2.9,  A.^,  3;  —  'mayehe  payaahö Vr.  1.  3;  A.3.  a;  —  'mayäi  Y.  J.  9;  — pagiryeheca  na  myazdahe  a&siti  (sd)  .  .yai •mayehe  A.^.  7;  — pan^^a  ^a%war)iafom •mayehe  alaAe  vaAistahe  da%usö  "45  [Tage sin<^  bis  zum  (Haupt)tag]  des  M.  [im Monat]  AV.  [am  Tag]  des  Schöpfers" A.^.?.
--- zaram
5989:•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
24830:•  j.  rao^a-  n.  'Butter',  mit  *taramaya- Adj.  'Friihlingäbutter',  Bezeichnung  der Speise  der  Seligen:  i^ari%aiiqm  hi  barg- tqm  (sd.)  *zaramayeAe  "nahe  tal  atti  yünS ..  hudalnahe  ifarüim  pasca  para.iristjm H.  2.18".
--- dug9dar
--- dugdar
--- nyus
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2962:uüdvanayal . .  nOii  °ra  avßirisyät  (s^.)  Yt.  Untergang  ausgesetzt,  vergänglich,  slerb- 5.62;  —  'ra  vatiuhls  ußa.saaa  {%A.)  VLjlich':  azdibl^  ,. 'sati/iat'^yäs?  tanvö  V.4. y.  147;  —  paracil  mraoüs  (sd.)  'r^lcä ;  $0;  —  am  "/uwAs"  'iaauAaiti^^  qshm yairJ  mainyus  drfgvats  ^-  53-T,  —  °ra\isaili  tanva  Aog.4<?;  —  ahmi  dhn  patti F.  7;  —  *°rä(a'>  paraca  tarasl'a  F._ya.     \  fran/nnzal  {&&.)    ahmi  fw    bazal  'lanha
3020:.A;./^-   mainyus-  a^t>m  fra^har^tayat   ^0- ^"Zlll.  i'^l'l^^TaZTri'l'.V^
--- us.tav
--- ustav
8803:•  j.    'ustavajti-    f.   EX.   einer    gläubigen    'riiiAo  . .  saiiit.kjo/a  ai.manauAa  Yt  i~. Frau;  '-,-aily,°i  aiao'iy.l  Yt./J.  139.  13;  —  das.i  asp'i  . .  °r^m^a  Y.44.18;  —
9086:JrSiä-,^.  ÄS;I  ■""--  ^l!'-  """■-  Snbsl'Wohl,Heil,Grack':  iäl.  i,  rf«,.,,,,,, .  j.  ■ustaviiti-  f.  Name  eines  Flusses,  I !?  .f*""' .!'™  '"°"'  ?''f,  *'  <>»' '»"8« ZnHus!esdesA-«../«W,™,)-Sees:  zrvi,,"'i  '"  "'.',  S™"^.»  "?  H-£-'6-  , yat  kasaim  .  .    avi    tmi    avt.hanlaautt  ...         ,      ,      v  .      ,    _
9089:•  j.    'ustavaiti-    f.   EN,   einer   gläubigen  i  °r>h^hi>  . .  saini.kaofa  as.mananha  Yt.  iy. Frau:  'vaitya  aiaoiryJ  Yt.  y.  13g.  ,  13;  —  dasS  asps  . .  'nm^ä  \.44. 18;  —
```


## [2026-09-07T18:24:11.229Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5985,5995p' BRT.txt; echo \"=== nayu ===\"; grep -n -- \"nayu-\" BRT.txt | head -6; echo \"=== nahit ===\"; grep -n -i -- \"nahit\" BRT.txt | head -6; echo \"=== naosa ===\"; grep -n -- \"naosa\\|naoia\\|naola\" BRT.txt | head -8; echo \"=== a-nusant ===\"; grep -n -- \"anusant\\|an-usant\\|an-usa\" BRT.txt | head -5",
 "description": "More BRT greps"
}
```


### [2026-09-07T18:24:11.324Z] TOOL RESULT

```
Hilirikaca  apprmäyükasla  varai'i^lm  (sd.) pantam  azöil  V.j.ii;  — gäui . .  varaülm {sd.) pantam  azaifeXt  10.3S.  4  a)  Akt '(als  Strafe,  Busse)  auferlegen',  b)  Med. 'auferlegt  bekommen,  auf  sich  zu  nehmen haben':  a)  tairyehe  5:rt  vä  Ozaiti , .  aslraya
kada  mazda  yöi  uxsand  "snam  . .  /rärmtg
Y.46-7,.
Abkit.  —  ai.  ähnäm  usw.  (NS.  ihar).  —  Pü. : rS^.  —  ''S  3S.  1.  Doch  beruht  dei  Ansati azan-  lediglich  auf  dem  au  ähan-.  — ")  Thcm.
•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
V
ob,Google
"S
azarsäant-
az^m  4
326
=== nayu ===
=== nahit ===
4458:•  j.  an-ähita-,  p.  *an-ähita-'*  Adj.  (fem. 'tä-)  'woran  kein  Fleck,  kein  Makel  ist, haftet,  makellos':  mihnm  .  .  yim  yazata haemö . .  't^m  'Is  "tili  parü  bartsm^n  °tayst pars  zaohräyat  'talibyS  farS  vayzibyS  Yt. JO.88;  —  tiilrtm  .  .  dßrät  vyavantsm bämtbyS  raoxsnibyi}  'iaäbyJ'^X.S.z;  —  'ta F. 5.  o)  bes.  von  der  Ar>dvT  (sd.): anduya  äpS  'tayh  Ny.  4,0,  Vr.  7.5;  Yt. /.  2i;  ^  sonst  mit  sQra-  Adj,  verb.;  ap?in andvJm  sürqm  Hqm  Y.  Ö5.  i  usw.'';  — aridvt  süra  °ta  Y.ö'5.4  USW.";  —  arpdvl Sure  'te  (VS.)  YL5.18  usw.'\  A)  als weibliche  Gottheit*',  Avamfi*:  D  «*«/'a*- masdä  "atfh'C  (=  anahiti')  Uta  mitriß mäm  pätuv  Am.  4;  Am.  j'.
5480:kainlnö  kihrpa  srJrayh  Yt5.64;  —  bow- raini  vastrh  vat»hala  °dvl  süra  anilAi/a Yt.5. 129;  7,19,88,91,  95,96,  123,  127, laS;  —  avaj  nyapt^m  dazdi  me  vami/ii snisU  -dvliyS.)  süre  anil/iile  yäh  a  . .  Yt 5-  18;  9.  63.  77',  »S.  87,  90-  94.  130. 131,  Ny.  /.  19;  —  paili  dim  p»r>sal  zara- %uilrS  "dvltn  sürqnt  anahitqm  yt5.9o; I,  9,  62,  94,  Vr,2.  7,  Ny.4.9.
6278:—  tnatihsm . ,  "savan^m  Yt.  7. 3 ;  —  anduyä 3p5  ,.  'laottyä  ay.4-o',  —  arpdvjm  ., 'saonTm  asahe  ratum  Ny,  4-  9i  Y.  65. 1*;  — arxivi  sBre  anahite  °saone  (VS.)  Ny.j.19;
16992:ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
17086:•  j.  bänav-  m.  'Lichtstrahl,  Strahl':  tifirim .  .  darat  vyävant^m  (sd.)  -«aJj'ff  (alslnstr.) *raoxSmbyS  anahitaHbyS  Yt*.  2;  —  as? srire . .  bänummti  säiti  vyävaiti  (sd.)  °nubyS (alslnstr.)  Yt/7.6;— df^ra/  hala  'nuwe^y^ aisma  frasaocayahi  {sA)  V.  Ä  75.
18697:srz.)  wer.."  Y.44.4;  3"*'; — is  urva'iä (sd.)  tpUamai  saraiuHräi  nä  mazdä  Y. 5/.  11;  —  kS  möi  paiSiii  ks  tnS  na  "i^rStä vistd . .  azää  {iA.)  Y.30.  i;  —  ataf  ahmäi .  .  üiä  (Sp.  134  o.)  ankaitl  .  .  yi . .  vandayaita  (sd.)  Y.50.3;  —  a^ yS  rna nä  trtanxlaiti  attyida  (sA)  ttvS  . .  Y.5/. 10;  —  at  yasßm  rtö'it  nä  is^mnS  äyst. (Sp.  150  Q.)  .  .  hs5  .  .  \.46.6;  —  yi  1/ ahmai  ?r?:ux'jä  {%A^  nä  däitl  '^.44.  19; —  aat  yd  na  hli  fräyazaite ..ahmäi .,  Yt 'JSi;  'S,  152;  —  Mä  tfm  urvaijm  .  . fräyavayöis  .  .  aom  nar>m  daitlm  y5  nä . .  frayatät  (sd.)  Yt  /.  24 ;  —  y3  . .  kv5 nä  */rasrBiäyäi  (sA.)  ifTf^Tvö  \ . 4ß.  i y, — /ivö  ma  n  a  sravä  tnörmdat  (sd.)  yS  ,  . Y._^2. 10;  —  a/  hv5  var^Aius  vahyä  (sd.) nä  aibJ.jamyät  yS  ..  Y.^^j.  3;  —  hvS  tat na  ahmai  dasdi(^^.  715  u.)  Y.5/.  19;  — hicä  nä  ßüma  nHaaharatü  hs  aiwyä- xsayatü  Y.5Ä4;  —  yezica  ma  hau  nä ava  snaHita  (sd.)  .  .  aJnavät  P.  2/j  — nai'a  paicaaa  *hau  *«J'^  .  .  isaäa  .  . apasütHt  (sd.)  P.  23;  —  aisS  nä  yS yaoidä'hryS  V.  g.  39,  40,  42,  ip.  31,  Vd. *?,  10,  V.  5.  41,  4.  49  (wo  naröy-,  — h'at  hS  nä  atthuyäite  (sd.)  cvat  hö na  alayäti  hat  ahmäi  naire  miidam aahatyl  .  .  A.4.^i.;  6',  V.Ä81,  p.  39', 44,  Y.Ö2. 1,  Yl/o.  i37£3;  —  yesi^  hö nä  paitiMncSit  yS  nöi}  apivatäite  damaya sva, "wenn einer.,,  der.."  V.^. 47;  —  taEca narSg3rpo5Ji3r3lasca{iA.)..'^.j.7^;  24;  — yasia  mi  aS^m  narpm  .  .paili  utiärayat sva.  "und  wer  ihn  .  ."  V.iS.  10; — paiti- tjm  ahe  nari yavaiea  ..  V.^.ai;  —  ndtt zT  ahmt  paiti  nairi  .  .  rSna  (sd.)  .  .  V. 7.  5»;  —  anätartta  a^byS  nprtbyö  . . yöi  .  .  Yt  13.  30;  —  hauca  *anayä  narä (GD.)  vohu  man3  jäg)r)bustare  arfhat yS ..  V.  4. 48.  B)  Ohne  Attribut  steht 'ein  Mann'  im  Sinn  von  'einer,  Jemand'; insbesondere  hat  der  NS.  na  in  der  Stellung der  Enklitika  häufig  die  Bedeutung  unsres 'raa.ii'-.yB  nar»m  anduIa{zA.)  sna'iajainti V.4.  »6;  18,  ai ;  —  äfs  nanm  jainti  vä V.5.  8;  8f.3;  — yB  *naire"^  aoxte  Jrä im  «Ä  (sd.)  "wer  zu  einem  sagt :  . ."  F. 4A;  —  na  tat  (Sp.  630U.)  paraJri^yeiti V.  5.  i;  a,  5;  —  mit  der  Negation  'nie- mand': nüit  spsJ>3ntS  .  .  nasui  nar?m nsil  *ästarayäti  V.  5.  3,  a)  NS.  na  in
=== naosa ===
5218:—  t^m  yaxata  kutaosa  vJsS 'vi  naoiaranqm   :
24390:•  j.  vi'starav-  m,  EN.  eines  iranischen Helden":  tarn  (näml.  andvlm)  yazata 'taurus  yS  naotairyqnd  upa  apim  yani VTtafiuhaitlm  ". .  V.,  der  Naotande  . ." Yt5.  76;  —  'taraos  naoiairyanake  alagn
26930:•  S-  (>  P-)  späda-,  j.  späda-  m.  'Heer, Hecrschaar':  'hm  . .  drvalam  dalvayasna- nqin  Yt5. 68j  —  aom  °hm  .  .  yS  ml p'asMt  vazaite  Yl 74.58;  58';  —  ''^<'^' xrvisyantake  Yl  iO.  36;  —  yat  'la  (ND.) hanjasante  \x.i4.a,y,  —  hyal  hSm  °ää (ND,)  anaolatfkä  (sd.)  jamaitt  Y.44. 15.
=== a-nusant ===
4524:•  '}.  an-usant'  Adj.  (fem,  •saitt-)  'der (etwas)  nicht  (tun)  will,  widerwillig,  ohne CS  zu  wollen':  ndit  mam  vTspe  yazatat>hs •Sf/ttfm  fraerscinta  "nicht  mich  gegen meinenWillen.."Yt  i7. 19;  19;  —  v?r3zyjt usaitica  *°ja(//Vfl(NSf.)''"..  mag  sie  wollen oder  nicht"  N.  6\  —  virszylt  usaiti  (sd.) neu  *'saili'^  N.ö;  — yat  ■j^(NS.)  vi/yei- tii'aisA.)..  M.S.  a6.  a)  "jiJNSm.  alsAdv.J» 'widerwillig':  'sS..  avat  kvar»  ätäpaite{i^) •tJ  h-tu  ma  °s5  ave  stärB  V.9.41;  — frä ahmät  parö  vlspe  daiva  'SS  tarsta  mmanle Y.  57. 18.  o)  sva,  'mit  Gewalt':  vaim>m (sd.)  's5  pai'iy3ife^.4.i,^;  53.
4528:•  *j.  an-usa'vant-  Adj.  'was  keinen  Ausfluss, kein  Leck  luit,  nicht  rinnt':  *hävanalibya ratufris  , .  yesi  'van/a  {liD.y>  "mit  einem Pressgerät  . .  ist  man  r.,  sofern  es  nicht rinnt-  N.707.
4535:•  j.  an-uso  Adv.:  s.  anusant-,
```


## [2026-09-07T18:24:40.447Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5989,6010p' BRT.txt; echo \"=== axsaen ===\"; grep -n -- \"axsaen\\|axiaen\\|a-xsae\" BRT.txt | head -5; echo \"=== anaos ===\"; grep -n -- \"an-aos\\|anaosa\\|an-aoi\\|amosa\\|amaosa\" BRT.txt | head -5; echo \"=== zarama dug ===\"; grep -n -- \"zaramaya.dug\\|zar9maya.dug\\|dugadar\\|dugddar\\|dug'dar\" BRT.txt | head -5",
 "description": "BRT azarema, axsaena, anaosa"
}
```


### [2026-09-07T18:24:40.536Z] TOOL RESULT

```
•  j.  a-zarama-  Adj.  (fem,  'mä-)  'nicht
V
ob,Google
"S
azarsäant-
az^m  4
326
abnehmend'  (an  Stärke,  von  der  Stimme) : fra  staotfi»  v<ü5  yesnitn  °mya  (ISt)  vaca mneyä  FrW./.  i.
*amma-  m. 'Verkommen',  lum  ai.  V.j'frya/i;
•  j.  a-zanäant-  Adj.  'nicht  alternd':  jiat
kiTynaiiqn  .  .  ahum.  'hrOgm  YtJp.  11;  —
bvaivlips anhus  . .  *'/ff'>  F.jh;  Vyt^^j".
PjAorA,   inm    w.  \.  jiryaH  'altert';   s.  unler
imirina;     (Zum  Verhallois  von  a-tarts-anl'  zu iL/ärii-uA  s.  BTHL.IF.7.70;  falsch  JSCHMIDT Plor.  3S6.)  —  Pü. ;  asarwän.  —  ■)  Hds.  "JA j.  azurtm  N.  j)3:  lies  aW/m,
•  j.  a-zäta-  Adj.  (fem.  °td-)  '(noch)  nicht geboren'  sva,  '(noch)  zu  gebären,  künftig* : hätamca  aaAusämca  zätanamca  'tanamla aiamamY.6^.6',  —  irfri^u/am  ../vantam .  .  narqm  '/anqm  frasBxar^ram  saol- yattiqmY.24.y,MLi3.i7,ig.az;  —  yat  asti airyanqm  äaAyunqm  sätanqm  'tanqmca (GPt)  ". .  den  jetzigen  und  den  künftigen" Vl  ig,  s6.
ü.  ijäla-  Adj.,  mp.  (Pü.)  ami. g.  itid^  Y-  50.  7:  s.  zö-. j.  oufu  Yt.  14.  38:  lies  asrü-ai'.
•  g.  *a-zi"  Inf. 'vorzugehen  gegen— (Akk.), anzugreifen'*':  *uzirndyäi  a°  sarxiana (sd.)  snighakylt  Y.4:j-i4-
Znm  V.  a»-.  —  Pü.:  raiuätz.  —  '}  NA.  öümjl, L  aber  GON.  KZ.  jo.  331.  —  ')  GdN.  a.  0. : "Jedenfalli  bedeutet  das  Verbum  'kommen', wie  die  P.V.  unser  aij  übersetzt".  Falsch; TOTDän  bcdcniet  'gehend'l  ~  3)  Wonach  Sü.:
•  j.  az«m,  g.  azSm,  p.  adam  NS.  Fron. 1.  Pers.  'ich'.  Es  wird  gesetzt  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegt)  a)  bei  Gegenüberstellung:  1  naiy 'iam  fuümaiy  taumä  Bh.  >^.  1 1 ;  —  11  ima' ttsuam  (sd.)  Aauv  rtiyastaya^  ktftanaty.. pasavr  'dam  niyastäyam  ..  X.  7.3;  —  i^a maätyOe  dta^arynä  . .  äat  azim  manya  . . \\jo.  I  o  s  t ;  —  'Um  iBi  sis  ^pouruyifravsi- vJdl  (sd.)  vJspSt^  anySng  .  .  \.  44.11;  — yä^a  't^m  avata  V3r3%ra  hacane  ya^a vltfie  *anye  aire  Yt.  5.69;  —  b^r^JoyStiti il .  .  strSuica  titäuApmca  .  .  'z^mca  kl  öptp- jttlm  yö  äaiiva  ahurd  mazdä  V.  7.52''; —  S  mann  taumäyä  ^*  paruvam  xfäya- ^t^ä  a/tcT  'dam  navami^  Bh.  7.4;  — ö^J  aäJ  csit  (sd.)  akurS  .  .  ^öti  sara- "^uärg  , ,  a%a  *'ifmhi  yö  mazdayasno .  .  vimrvyi  Y,  12.  6  '*;  Vr.  11.  19";  — yd^a  avat  kvanxsait^m  ..  av<£k>a  'zsmHl.
Yt.  10. 118;  — Ivasiy  aniyalSy  naidam  (sd.) tjic^  adam  akunavam  utamaiy  tyJ*  pitä a6unausX.l.y, — \\kal!iy  naiy  adarsaauS (sd.)  tisHy  .  .  ^asianaiy  pariy  gaumätam .  .  yats  'dam  arasam  "keiner  .  .,  bis  ich kam"  Bh. /.  13;  — ya%a  °z>m  taurvaymi vlspe  dasvB  .  .  yai  mqm  naScU  taurvayät nSit  dalüö  ..  Yt/. 6;  6;  —  ks  mqm stavät  .  .  kakmai  °vm  upanAa^ayeni  Yt J.8;  8.  15,  10.  io8-iio*,  I4-M,  '5- S6(?).  b)  sonst:  -zSmctt  ahyä ..  %wqm mlAhj pagurvlm  7iaaÄm(sd.)  Y.2^.10;  — havanätum  ästaya  °z?m'''  vlsäi  {sd.)Yi.j. ,.  j6i).  — Wc^ur^mtuda  yäha  avainc^ imäm  bamim  *yaud<^Hm  (sd.)  pasävi^dim manä  frabartr  mam  xsäydhiyam  akunauS -dam  xsaya%iyt^  amiy  "als  AhM.  .  ,  sah, da  hat  er  sie  mir  übergeben,  mich  hat er  zum  König  gemacht,  ich  bin  König" D.  6^4;  —  mqm  dd^at  ahurS  mazda  .> mana  raya  . .  pasvasca  . .  vXcannta  . .  °t»m bdil .  .  tä  nipayemi  Yt  5. 89.  2)  ||  wenn der  Satz  nur  aus  dem  Subjekt  und  einem nominalen  Praedikai  besteht  (Dbr.  VglS. ^.11):  "dam  karui  xsaya^iya^  Aaxä- manisiyt^  K.;  Bh.7.1,  D.5.  j,  6.2,  12,  iS, ig,  X.1.2,  Am.  2,  Ao. /.2.  3)  vor  einem attributiven  Relativ(satz) :  pairi  dim  tanava 'z^m  yS  ahurS mazda  Y.  ig.T,  6,  Y.j/.is; —  a%a  °z>m  ys  ahurS  mazdä  urvarA baisasa  uzbanm  V.  20.4;  /,  2,  2.2,  ^.6, 5.  \tV,  2o,  is-zt)',  iS.zti,  YL5.  6,  8.  25, i2.4,  P.  2^,  JA", _FrW.  4.  2,  Nik.2;  — "s;-/« yB  akurS  masda  'zim  yS  data  vanAvqm yas»  tat  nmärum  aksrm^m  ..  uzaymi  ..  V. 22.1;  —  nava  ahmt  p>lJ.s3rS  °Z3m  yö haomö  .  .  Y. //.j;  —  haxSaya  'z?mcit  yS zardkuitrö ,  ,  Y.8.T,  —  s.  noch  V.  7.  52, Y.i2.7,  Vr./J.i9  unter  i  a.  4)  sonst beliebig:  -zfm  tais^wa /raxshl{%A.)  avami mazda  .  .  \.44.ji';  —  'zpm  bä  U  ahmt yum  . .  ya  kava  dama  H.  2. 1 1 ;  —  kö nan  ahx yim  °z3m..sralst)m  dsdar>sa,.'i aaj  ml  alm  pattyaoxta  .  .  °z?m  ahmi .  . haomöY.g.i  f.;  Yt  70,54',  /7.17;  —  °zym d(&qm  .  .  asö  r3mö.daUim  (sd.)  . .  y^i  zJ 'am  fiBit  daiayqm  ..  V, /.  i;  YlÄSo,  52, ij.  II,  4.1,  18. 1,  3;  —  aal  yat  mi^nm ,,/radaäqm  "zim  spitama  aal  dim  dahqm.. Yt.  10.  I ;  Vd.  8,  12;  —  daxdi  ml .  .  tat äyaptim  ydha  azani . .  uta  'z?m  ni/anani . . Ytp.3oCj  31';  —  avai  ayaphm  dazdi ml . .  yat  bavani  aiwi.vanyä  .  .  yd^  a  'zim
dby  Google
827
=== axsaen ===
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
29609:Bed.  nach  Pü.  —  Ich  verbinde  das  Wort  mit pairiila-akara-  und  weiter  mit  ai.  jar/if-n.  — i'ü.;  i/iirw;  s.  zu  liaierämacu-.  —  >)  Statt anumayaitifm  hanlanum  v' ;  Abkürzung  mit der  Komp-  statt  Kasusform  im  mittleren  von drei  zusammengehörigen  Nomina  mit  gleichem Ka-susausgang;  S.  nocli  ahoUai'inakt  urvnti Jiaspaianahi  Yt,  14.  II,  varäzahe  pailijrtnö liii.dqslra&t  YL  14.  IJ  ,  giBqttqm  piiuru.sat>'iS virB,T/if%amnqta  Vr.7'.  5,  aspanqm  avnialö  d^riü.- /akanqm  und  itiiranqm  iirvald  sdeHi.kaofanqm  V. S2.  3  (aber  V.  32.  4  steht :  gavqni  axiaenanqm apirilBjanunqm,  weil  die  Ausginge  nicht  gleich sind);  s,  femer  un/A%ä-  No.
=== anaos ===
=== zarama dug ===
```


## [2026-09-07T18:24:42.697Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD stoh ===\"; grep -n -i \"stōh\\|stoh\\|stōw\\|a-stō\" PHD.txt PHD_mackenzie.txt | head -12; echo \"=== HRN nastuh/sotuh ===\"; grep -n -i \"sitüh\\|situh\\|astüh\\|nastüh\\|stöh\" HRN.txt HUB.txt | head -12",
 "description": "Pahlavi stoh"
}
```


### [2026-09-07T18:24:42.763Z] TOOL RESULT

```
=== PHD stoh ===
PHD_mackenzie.txt:9975:nibastan                  \\\'UJ CU,    wastohmag
=== HRN nastuh/sotuh ===
HRN.txt:8084:gärzin stöhnen* (89).
HRN.txt:10545:oss. d. yärzun, t. qärzin 'stöhnen (89).
```


## [2026-09-07T18:25:14.073Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT aosa Tod ===\"; grep -n -- \"aoia-  m.\\|aosa-  m.\\|'Tod'\" BRT.txt | head -8; echo \"=== BRT an-aos ===\"; grep -n -- \"an-ao\" BRT.txt | head -8; echo \"=== PHD anosag/stow ===\"; grep -n -i \"anōšag\\|anosag\\|anwsg\\|stōw\\|stow\\b\" PHD.txt | head -8; echo \"=== PHD suf/asur ===\"; grep -n -i \"sūr \\|sūrāg\\|dawn\" PHD.txt | head -8",
 "description": "BRT aosa, PHD anosag"
}
```


### [2026-09-07T18:25:14.157Z] TOOL RESULT

```
=== BRT aosa Tod ===
5858:Komp.:   aspii-+ä'j/aoia-  m.  'KampP,    zum  V. yaaii'X  at.  vgl.  äyadhatia-  n.  'Kampf.  —  0  An- ders JusTi  NB.  46  a. j.  asp>n'  i  s.  unter  aipaii:
5976:j.  a-zaosa-  m.  'Nichtwille,  NichUbsicht'; yezi  zaela  yezi  -/a  (IS.)  "sei  es  absicht- lich, sei  es  unabsichtlich"  Y. ;.  21.
8956:•  j.  kaoia-  m.  EN.  eines  Gläubigen :  ^ac- raosahe  'iaAe  asaonS  "des  Fr.,  Sohns  des
17510:•  j.  fraoraosa-  m.  EN.  eines  Gläubigen: 'sähe  kaosahe  asaens  "des  Fr.,  Sohns  des K.  .  ."  Yty.122.
22698:♦)  Der  mit  Asis.v^älav  in  Verbindung  steht; vgl.  Bd.  38,  3S,  West  SBK.  5.  iii  No.  7i  37- 223  No.  7,  DsT.  ZA.  2.  68,  Barthelemy  Gab. 45.  GrBd.  [bei  Dst.  aO.)  stellt  beide  filschlich gleich.  Sü.  gibt  v'  mit  kälak  'Tod'  wieder,  ». auch  Npü.  marg  im  Mx.-Gloss.  203.
27243:•  j.  sraoSa-,  g.,  j.'>  svraoia-  m.  I)  'Gehör, Gehorsam,  gehorsamer  Sinn'  uzw.  des Menschen  gegenüber  dem  göttlichen  Willen: at  hei  voha  "iS  janta  manaaha .  .yahtnäi vaii  (Sp.  1382  m.) . .  Y.  44. 16;  —  vacs . . ySi  mSi  ahtnai  °s>m  dqn  Äyai(Sp.  426  m.)^^ V.  4:5-5;  —  hadä  (sd'.)  vSita  vahming  -iä radanhö  Y.4^.  17;  —  at  rätqm  (sd.) sara%uitrS . .  dadain  paurvafat)m  (sd.)  . . 'um   x/a'&rymiSp.  543  m.)i?o   Y.  33.  14'';
30215:vämoruh,  gr.  «aXJjiiiTO,-);  *laoia-  m.  "Dickbein,
=== BRT an-aos ===
4237:•  g.  an-ao£ah-  Adj.  'unfriedlich,  feind- lich': hyat  hSm  spadä  'c'anhJiüD.)  Jamale "wann  die  (einander)  feindlichen  Heer- schaaren*'  sich  treffen"  Y.  ^.  15-
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
=== PHD anosag/stow ===
3016:overcome stowénidan, wānīdan.
4762:petig, sti stendag sidig, stéy sidigar stér stézag stowih stūwēn- stowēnīdan stē Sadwēs dīdan -istan stūn stūnag stor, stür sturg stūrīh stórgáh storban stard *stūš stūdan star
=== PHD suf/asur ===
252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
520:368 Paws] dawn.
522:6š(e)bam [w$b?m | M "wsyb^m] dawn.
572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
657:wizürd-wars [wc'/t' wls] with parted hair. wizāstan, wizāy- [wyz'stn!, wyz'd- | M wy2’y-, N guzáy-] injure, impair, prejudice. ~išn: injury. ~išnīg: injurious. wizén [wcyn! | N guzin] choice. wizend [wz(y)nd | M wzynd, N guzand] hurt, harm, injury. wizéngar [wcynkl] chooser; selective. | wizidan, wizin- [weytn', wcyn- | M weyd, N guzīdan, guzīn-| choose, select, prefer, discriminate. wizihidan, wizīh- [w(y)cyh-ytn'] be separated. „išn(īh): separation; dawn(ing). wizin- , v. wizidan. wizir [weyl] decision, judgement. wiziristan, wizir- [wcyl-stn! | J bzyr-, N guzir-) be able to dispense with, avoid. ~iSnig : avoidable. wizistan [westn' | M weyst] teach. wizóstan, wizóh/y- [wewstn', wewd- | (J bzwb-, N pizohidan)] examine, investigate. -~i§n : investigation. wizüdan [wyzwin'] = wizastan. wizurd [wewlt'] valid, genuine, true. ~th: validity, truth. Wērūbaršt [w’wklwblst' = Av. wouru.barasti-] the north-western con- tinent of the earth. Wērūjaršt [w>wklwelft' = Av. wouru.jarasti-] the north-eastern con- tinent of the earth. wurróyistan, wurróy- [H YMNN-stn! < A hymn, У °тп | M wrwyst, (wrw-), J *brwy-, grww-, N brw-, girawidan] believe; choose. —išn [wlwdén'] belief. wuzurg [LBA < Arb’; wc(w)lg | M wzrg, N buzurg] big, great. ~ith: size, greatness. wuzurg-framadar [LBA plm't I) prime minister.
1121:burrow sūrāg.
1122:burrowing sūrāgīg.
1495:dawn bamdad, ēš, ós(e)bàm.
```


## [2026-09-07T18:25:31.878Z] TOOL CALL #42: Bash

```json
{
 "command": "ls site/pages/351.jpg 2>/dev/null; pdftoppm -f 351 -l 351 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg351 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render printed page 351"
}
```


### [2026-09-07T18:25:33.603Z] TOOL RESULT

```
site/pages/351.jpg
total 29152
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 14:25 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1011 Sep  7 14:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T18:25:34.633Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT sura Morgen ===\"; grep -n -- \"'Morgen'\\|a-sQra\\|a-süra\\|asura-\" BRT.txt | head -8; echo \"=== BRT ni-us ===\"; grep -n -- \"ni-us\\|niui.tav\\|nius.tav\" BRT.txt | head -5; echo \"=== KLN nice ===\"; grep -n \"nescius\\|nice, adj\\|^nice\" KLN_1966.txt | head -5",
 "description": "BRT sura, KLN nice"
}
```


### [2026-09-07T18:25:34.761Z] TOOL RESULT

```
=== BRT sura Morgen ===
5775:•  g.  a-süra-  Adj.  'unstark,  unvcnnögend': yj  anass»m  xsqnmJng  (sd.)  raditn  *vaHm n?ris  'rahya  V.2_9.<).
26203:Vll.  Ableit.  aus  »sasiah-  n.  'Morgen';  »gL lavakh.  —  Fü.;  transskr.  —  ')  So  Ks,  Mfl; NA.  s-ru:
=== BRT ni-us ===
=== KLN nice ===
8801:conscious,  adj.  —  L.  conscius,  ‘knowing,  aware of’,  fr.  con-  and  scire,  ‘to  know’.  Cp.  L.  nescius, inscius,  ‘not  knowing’,  which  are  analogously formed,  and  see  science.
25377:Nicaean,  adj.,  Nicene.  —  See  Nicene  and  -an. nice,  adj.  —  ME.,  ‘not  wise,  foolish,  wanton’,  fr. OF.  nice,  ‘ignorant,  foolish’,  fr.  L.  nescius,  ‘not knowing,  ignorant’,  fr.  neg.  part,  ne-  and  the stem  of  scire,  ‘to  know’,  see  nescient.  The original  meaning  of  E.  nice  was  ‘not  wise, foolish’.
```


## [2026-09-07T18:25:46.359Z] TOOL CALL #44: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/351.jpg"
}
```


### [2026-09-07T18:25:46.384Z] TOOL RESULT

```

```


## [2026-09-07T18:26:13.413Z] TOOL CALL #45: Bash

```json
{
 "command": "grep -l '\"Keu 4\"' data/extracted/batch/*.json | head; python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('data/extracted/batch/*.json')):\n    d=json.load(open(f))\n    for e in d.get('entries',[]):\n        r=e.get('root') or {}\n        n=r.get('name','')\n        if n in ('Keu 4','Karana','Ôus 1','Ger 2','Ahu','Aiw','Mew','Wek','Kwer','Ksei 2','Těu 1','Ud 1'):\n            print(f, n, r.get('lang'), r.get('gloss'), r.get('refs'), r.get('redirect'))\nEOF",
 "description": "Find cross-referenced roots"
}
```


### [2026-09-07T18:26:14.729Z] TOOL RESULT

```
data/extracted/batch/page-264.json
data/extracted/batch/page-354.json
data/extracted/batch/page-351.json
data/extracted/batch/page-279.json Ksei 2 Indo-European bright WLD1:501; BRT:541 None
data/extracted/batch/page-38.json Ahu Avestan defect, fault BQT:72 None
data/extracted/batch/page-41.json Aiw Indo-European vitality, eternity POK:17 None
data/extracted/batch/page-516.json Ud 1 Indo-European up, out, away POK:1103 None
data/extracted/batch/page-537.json Wek Indo-European to wish, desire POK:1135; KNT:207 None
```


## [2026-09-07T18:26:20.633Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nfor f,names in (('data/extracted/batch/page-264.json',('Keu 4',)),('data/extracted/batch/page-354.json',None),('data/extracted/batch/page-279.json',None)):\n    d=json.load(open(f))\n    for e in d['entries']:\n        r=e.get('root') or {}\n        if r.get('name','').startswith('Keu'):\n            print(f, json.dumps(r,ensure_ascii=False))\n            for n in e['nodes'][:6]:\n                print('   ',n['id'],n.get('lang'),n.get('refs'),[w.get('translit')+' : '+str(w.get('gloss')) for w in n['words']])\nEOF",
 "description": "Keu 4 root"
}
```


### [2026-09-07T18:26:21.916Z] TOOL RESULT

```
data/extracted/batch/page-264.json {"name": "Keu 4, Keu-bh", "lang": "Indo-European", "refs": "POK:594", "gloss": "to shine, bright"}
    1 Avestan POK:594; BRT:221,1631; SYN:995 ['sŭr, savah 2 : morning', 'sŭram : early morning', 'a-sŭr : not (yet) morning, dawn', 'sŭirya : breakfast', 'savahî : the East']
    2 Pahlavi HRN:166 ['sŭr : breakfast, meal, festivity']
    3 Persian BQT:1185; HRN:237 ['sŭr : festivity, party', 'sŭrnâ : a horn played at festivities']
    4 Old Persian POK:594 ['caune : bright red, a plant with bright colored fruits']
    5 None None []
data/extracted/batch/page-264.json {"name": "Keub", "redirect": "Gěu 1"}
data/extracted/batch/page-264.json {"name": "Keu-bh", "redirect": "Keu 4"}
data/extracted/batch/page-264.json {"name": "Keud", "redirect": "Keued"}
data/extracted/batch/page-264.json {"name": "Keued, Keud, Qeud, Skeud 2", "lang": "Indo-European", "refs": "POK:595", "gloss": "to yell"}
    1 Persian POK:595; WLD1:378; HUB:102 ['nekŭkîdan : to blame']
    2 Sanskrit POK:595 ['kutsa : blame']
    3 Middle English POK:596; SYN:1251 ['sčŭten : to yell']
    4 English None ['shout : None']
```


## [2026-09-07T18:26:36.527Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"suirya\" \"sQirya\" \"süirya\" \"'Morgen\" \"savaAi\" \"savahi\" \"sûram\" \"süram\" \"suram\"; do echo \"--- $w\"; grep -n -- \"$w\" BRT.txt | head -4; done",
 "description": "BRT sūra morning"
}
```


### [2026-09-07T18:26:37.835Z] TOOL RESULT

```
--- suirya
--- sQirya
--- süirya
26434:•  ').  süirya-  n.  'FrUhmahl,  -stück':  yaHbyS afm  (näml.  ätarl)  kamfpacaiti  xlsfitlmca 'rJmca  "denen  er  das  Nacht-  und  das Frtihmahl  kocht"  Y.6'2.  7; —  «jff/n  (sd.) "rJtn  is»mnS  Vt.  14.  20.
--- 'Morgen
5918:•  j.  a-svar-  :  'ssr-  n.  'Morgendunis  el, -dämmening':   'sSiri  (LS.)  süirim  ispmnS .»  j.  'a-srata-  Adj.  (fem.  'tä-)  'nicht  ge-
8703:•  j.,  g.  uSah-  :  uä-''  f.  1)  'Morgenröte, Morgen':  kS  yi  'Sa  (NS.)  arSm.ptiwä (sd.)  xiapsca  Y.44.$;  — ■  ayram  usailTm 'sirihtm  Yt/4-2o;  — /räymat  *s3nA?m süraya  *i'ft'i/f/«  (sd.)  Yt.  J.62;  62,  /5.S5;
17093:KompE.;  Ableit  —  Zum  V.  bä-.  —  ai.  bhama. m.;  np.  bim  'Morgen(-Frühlielit)'.  —  S.  dazu Hbm.  PSt.  34.
24829:-  »)  So  L4  und  K  I  (wVO;  Jp  i  usw.  und  NA. mi\  Pü. !  tti  'Morgenröte'.     S.  lu  ^vah-.
--- savaAi
4959:, .  Ailu  maza  m^rr/S  .  .  "ve  awrä  YL  z^.  *malnis  (sd.)  atiAat  pouruye  vTdv^  "vqm 41,  a)  mit  einem  ergänzenden  odsT  yä  im  af^Aaeapjma{^.)Y. 44.1g.  II)in erläuternden  Relativ:  'z'aj  karsvar}  _yff/' schwachdeiktischem  Sinn  'jener,  der'; *ar3zaAi  *savaAi  .  .  imat  iar^ar?  yat\  I)  auf  Vorhergenanntes,  Vorausgehendes :i^amra^sm  V.ip.^t);  39';  —  imS  /-irciv/ j  (Wort  oder  Satz)  zurückweisend;  i)  auf barizist^m  barszimanqm  °3raJ'>  yat  hvars  ein  Substantiv,  a)  adjektivisch,  auch  im avacT  "das  Licht  hier  (und)  jenes  Höchste !  Sinn  unsres  Artikels  (des  schwachtonigen unter  den  Hohen  dort,  was  Sonne  heisst"  'der'):  I  ka"bajiyJ' .  .  paruram  idä  xsäya- Y.  j6. 6.  2)    ohne    solchen    (ausge-  aya"  aAJ^  °vaAyü  k(fbüßyaAyS  brälä  bar-
--- savahi
6129:noch  No.  s-8,  10-15,  ^^f-  — Vgl.  alafojria-)  mit  No.  —  '1  Es  ist  ebenso unmöglich,  fiberall  die  verschiedenen  Bedeu- tungen des  Worts  auseinanderzuhalten,  als überall  zu  entscheiden,  ob  der  Begriff  oder dessen  Fersonitiliation  gemeint  ist;  vgl.  BB. 74.  10.  JAOS.  20.  31,  277,  IF.  12.  130.  - 3)  Vgl.  Cld.  KZ.  JO.  540,  jt.  268,  Gdn.  KZ. jt.  319,  Bthl.  Stud.  3.  124.  —  41  VgL  I  X b  &  —  i)  Hds.  aiava.  Pü. :  fia  hulaadlk  S  U i  akrirv  bulandih  ,.(?).  —  ')  Pü.  erl.:  rät  1 /rärön.  —  7)  -Pü.i  6t  vfh  mart  i  akrav  bül hFnd.  —  B)  So  Pt4.  NA.!  aiaakäeä,  %  26S. 30.  Pü. ;  an  i  fit  i  göspandän  —  tu  däi —  u  aArä- Hh—silt  i  iwiiW.  —  9)ünd  vgl.  Y,^/.  1  unter I  1  a.  —  u)  So  MI3  usw.  NA,  asira  nach Jp  I,  M[  2  usw.  und  angeblicli  nach  Pü.;  s. aber  oben  unter  Pü.  mitND.25.  —  lOPü.:  ic  ä ahräkik  ^aläiiA  iästt,  erl. :  fätixSäfüh  pa  frä- rämh  därii.  —  ")  Pü.  erl.:  an  i  pa  miiä  i akrSkiA  däränlA  afe  daAend,  Sü.:  yah praiäda^ panyasamgrake  diyalt.  —  1 1)  Pü. :  fa  öiän iuniln  !mäk  aAräiiA  S  imäi  daAJhef,  erl.: mild.  —  14)  ra. :  »e  .  .  aAräiiA  .  .  *viadil, erl.:  kiii  karpak  vinäi  ape  ni  kanel.  —  iS)Pü.: kc  .  .  räsBA  iSsel,  erLi  ku  viSir  (oder  däiawa- riA)  kunei.  —  '6)  Anders  Gdn.  KZ.  sy.  248, B>,  Stud-  /.  3i4>  West  SEE.  37.  175  (wo auch  lU  Pü.),  DsT.  ZA.  /.  200.  —  'ti  Vgl.  zu aiJAi«-3.  EN.— '»)NA.fli3.ÄfW.  Y^.:  SArmazd u  asavahisl  ki  tan  an  ...  —  '9)  NA,  asäjii. —  »)  VIL  lu  'asa-,  s.  DsT.s  Übersetzung.  — ")  Heilst  das:  "Soll  sie  für  ihn  die  kirckat- dienstUiAe  Vfrtichlung  vollziehen?"?  Pö.:  (un- deutlich): cigön  öl  iHtrai  rai  5  yazalän  lariä- iäslh...  —  "}  Ob  adverbial?  Pü.  hat  ein- fach aAräiiA.  —  >}>  Pü. :  haiar  ast  ahräkTA  iut xtat  nnirai.  —  '»  Np.  tägitd,  das  FrMOller WZKM.  5.  66  beraniieht,  ist  gewiss  femzu- hallen.  Eher  ist  'ai-ä^kj-lßi-  zu  Grunde  zu legen,  s.  np.  iarta  unter  ai.variiah-  und  unten Sp.  309,  —  »S)  Vgl.  zu  aiay-  mit  No.  9  f.
7938:idjektivisch :  D  'mam  bumim  ..  aram  as- mänam  D.6.1,  X.1.1,  6.  j,  Ao./.ij  — attm  asman>m  ys  'mam  sqm  äca  pairi^a bväva  Yt/j.  a;  153;  —  ava  raoffi  .. -mam  zqm  Yt  10.85,  89;  H./.  16;  —  'ms raoch  .  '.  avat  (sd.)  y.li  hzar}  aväcl  Y.jö', 6;  —  'mat  nmäniin  ..  käu  mat^a  trnrrjS ..  ace  awni  Yt.14.41.  a)  mit  einer relativischen  Ergänzung:  avat  karhar» yat  *ar7zaki  *savahi  .  .  'mat  karh-an yat  ^anira'i9m  V.  IQ. ^9.  2)  ohne  sol-
26003:savahi-
26040:•  j.  savahi-  (n.)  Name  des  im  Osten  ge- legenen Erdteils  (iarfyar-,  sd.):  avi  ar>- zahi  ''<4i{AD,)  Yt. /o.  15;  133,  *V.  ip.  39''; —  upa  karhan  yat  'hi  YLJ2. 10;  — anzahibyS  (sd.)  'hibyS  fradata/suiiyS  .  . Vr.  10. 1.
--- sûram
--- süram
7188:•  j.  ätrv.karst-  Adj.  'der  sich  mit  dem  j  ')  Nämt.  dem  Mann,  der  seinerieit  {»/•"  süram Feuer  zu  tun  macht,  dabei  tätig  ist':  'tä,  /raB.i-^y^nm)  aus  dem  im  Schlaf  ergossenen p  _                                                                             !  Samen  erstehen  soll;  rgl.  v.  iS.  40,  51.
23911:süram  ..  'nam  Y.  6j.  i.  "  J-   vi-galK    f.   'Einsenkung,  Schluchf;
24022:•  j.  vl-daeva-,  -dSiva-  (fem.  °va-)  'gegen die  Daiva  gerichtet,  ihnen  feind':  Jra-\ varänl  mazdayasnS  zara'hu^tri^'vS  aAura.- '. tka^sS  Y.  12. 1 ;  Vr. 5. 3,  Yt  13. 89,  Y. p.  1 3;  j —  andvTtn  süram  anShitam  .  .  °vqm  | ahura.tkaisqm  Y.65,  i ;  —  väHm . .  'dsyum  "  l ahurs.ikalssm  Yt.  13.  90';  —  mq%ra!a  \ spsnia  .  .yS  °vö  'vahe  astä  mazdä  ahuraht\ "und  (mit  Unterstützung)  des  heüigen Worts,  des  Z).-feindlichen,  des  Boten  des ' Z>.-feindlichen  AhAf."  Yt  13. 146.  a)  bes. , von    'data-  n.  (Stverz.):    dstam    'dSyBm'K
--- suram
23094:•  j,  varsni-haräta-  Adj.  '(admissuram habens,  d.  i.)  wofür  die  Zulassung  dei Widder,  der  Widdersprung  bezeichnend ist',  toa  Ayä^rima- (^sA.):  ayohrimtm  fra- ourvalltriimm  'tim  Y.  2. 9;  —  ayä%ri- m3i  .  .  °taica  Y.i.g;  —  aya^rimahe  .  . 'lahe^a  Vr.  /,  2.
```


## [2026-09-07T18:26:54.624Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nv1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('=== v1 leaf 256 (p46) ===')\nprint(v1[256][:900])\nv4=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('=== v4 pdf 293 (p2210) ===')\nprint(v4[292][:2200])\nEOF",
 "description": "BQT p.46 and p.2210"
}
```


### [2026-09-07T18:26:56.069Z] TOOL RESULT

```
=== v1 leaf 256 (p46) ===
آشناو ۳ ف_
رای فرشت ۰ بمعنی شناور باش که شناکننده | شور و فتده و غوغا - و بمعتی فاعل و امر باین
۳ ۱ .
است چین معتی هم هست . ٩۶‏
/ و - بسکون واو » بمعنی شناور ] شوردن « بارا ودال بی‌تقطه بروزن
متفه ۷ : 1
۱ آشنا ور- ۰ می آخشا گر ی ات
0 4 ۳ 2 عصی و خسمس مودن باشد ۴ .
آشوغ ب بروزن‌آروغ , شخص‌مجهول
غیر عمروف را گویند .
۲ شوفتی ۴ با فا بروژن واسوختن ,
یمنی آشفتن و مهم سس آمدن باشد .
] شبان ۴ » بایای حطی بروزن ما کبان,
خابةٌ مرغان (۱)- وسقف خانه باشد . .
آ شناه د بروزن‌یادشاه , بععنی‌شنا کردن
باشد - و شناکنندة را نیز گوبند ٩‏ ۰
! شو ه منم الث وسکون واو . مخفف
1 ۱[ ۰ بمعنی هم
برآحدن ۱ است کهبعربی «مدغله» گونند - ویمعتی
(۱) چك : د را گوشد 2
۱ - ره : آشتا. ۴ - نیز آشفتن خوا بکسی را : مرادل نامد که اسان‌را بیدار کنم
وخواب برایشان بباشورم . «نفیرابوالفتوح بنقل‌لفت‌نامه». ۳ ره : آشفتن. ۴ - مرکب از
پیشوند 2 و511812108 پمعنی جای وسرای » ارمتی 51360 (بمعنیده » قربه) «بارتولمه ۱۷۰۷*.
آشور - ۸65۲۲2 . بپلو
=== v4 pdf 293 (p2210) ===
[pdf page 293]
نویده ۱۰۳
نویده" بروزن‌خمیده, بمعنی‌لرزیده | کوبند که‌از درخت‌رسته باشدوعر بان(۱) سر
وجنبیده ونالیده وزاری کرده باشد - خوانند .
نویم۲ « بفتح اول بروزن قدیم. لفظی نوییی؟ « بائانی مجهول بروزن‌موبین,
است که آلرادرعربی محض میگویند همچنانکه | بمعتی اول نوبان است که‌پادشاهزاده باشدءوملو4
کوبند «بنویم دیدن شناخت» بمنی بمحض‌دیدن | وسلاطین راکه خوش‌وقوم وقرایت باشدلیزبدین
شناخت* . تام خوانند ؛ ویعضی کویند ترکان سلاطین‌خودرا
نویه « بروزن موبه » شاخ نی وتازمرا | بدین نام خوانند.
بیان لیست وسیم
در نون با ها مشتمل بر هفتاد لغت و کنایت
3 « بکراول‌وظپورتانی, بممتی‌شهراست | میگوبند ۸ - واشاره برنه فلك - و نه سوراخ
مربان مدینه وبلد خوانند همچوشابو رکه‌نه | قالب آدمی باشد که آن دوسوراخ کوش ودوچشم
5 مت شیر خاندرةه ۰
ایور است بمتی‌شپرشاپور٩‏ ولهاوند مت شهن ام بینی‌ودهان اغ مه وس است-
آوند" چه‌درآنجا ظروف‌واوانی سپارمیاختهاس |" ً رخقای 6 سرا میکند
وامربنهادن هم هت بعنی بنه ویگذار۷ سوم وبفتح اول و انی. افاده معتی لیاقت‌هب
اول وظپورها(») عددی است که آنرا بعریی‌تمه | همچو شاخانه وبزرکانه ودرویشانه ‎٩‏ - وتضین
() چش: - وعربان - (۲) خم۱ : ثانی.
۱ - انم مقعول از « نویدن» (هم.) ۴ - از دساتیر ۶ فرهنگه دساتیرص ۰۶۲۷۱
۴ -« السرع والسرعرع » آنچه ببالد ازسرشاخ رز» «مهذب‌الاسماء نخةٌ خطی کتابغان
دهخدا! > و ر4 : منتهی‌الارب . ۴ نوبان (ه.م.). رك: جفتایی ص ۵۱۱: « خافان‌منصور
قلب میمنه و میسرة سهاه اف پناه را بنور طلمت خاء زادکان آفتاپ احتشام و فر وجود نوبینان
بهرام انتقام زیت و استحکام داده بمیدان جنگه و ممرکهٌ نام و اشگه فرستاد . > « میرخواند .
حبیب‌المیر. چاپ خیام اج ‎٩‏ ص۲۰۹*. 8 - فقه‌اللفهٌ عامیانه . رك : نیشاپور +
۹ - ققه‌اللقهٌ عامیانه . رك : نهاوند . ۷ - رك : نهادن -
۸ - پارسی باستان -38۷21738 (مم) ۰ اوستا 88۷2 821۷0138-۰ ۰ (نم)
پهلوی 32113 , هندی باستان 8۷8 , ارمنی 188 ۰ افغانی ع (320)10 ۰ وخی و شفنی ۰340
سنگایجی ومنجی 320 ۰ پفنوبی 831 ۰ سربکلی36۷ « اسشق ۱۶۵۹ > ورد: هوبشمان۹۱*۵۹
کردی 8610 ۰ 2۵ . 285 ۰ 8610 ۰ زازا 2821 ۰ دوجیکی 210 «ژابا س ۶۲۸ »پهلوی880.
ایرانی‌باستان -82۷8 ۰ بقرابت « ده » 1210 ساخته شدم. فارسی‌جدید 8118 از 8۵0 از -28۷8
با 8 بقیای 48 ۸« یب رکه س۶ ۱۵ > ‎٩‏ - درین کلمات پسوند ۶ آنه» است.
‎٩‏ نوین - ر4 : نوبان .
( برهان قاطع ۳۷۹ )
```


## [2026-09-07T18:27:10.099Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nv4=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(v4):\n    if 'ستوه' in l or 'نستو' in l:\n        print('pdf',i+1,'printed',i+1918, [x for x in re.findall(r'\\S*ستوه\\S*',l)][:6])\nv3=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(v3):\n    if 'ستوه' in l:\n        print('v3 pdf',i+1, [x for x in re.findall(r'\\S*ستوه\\S*',l)][:6])\nEOF",
 "description": "Find nastuh in BQT"
}
```


### [2026-09-07T18:27:11.979Z] TOOL RESULT

```
pdf 32 printed 1949 ['پرستوها']
pdf 221 printed 2138 ['ستوه', 'بستوه', 'ستوهی', 'ستوه', 'لستوهی', 'ستوه']
pdf 491 printed 2408 ['ستوه']
v3 pdf 253 ['فراستوه']
v3 pdf 254 ['فرستوه']
v3 pdf 400 ['ستوه»']
v3 pdf 689 ['ستوه']
```


## [2026-09-07T18:27:15.241Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nv4=open('incoming/BQT/BQT_v4_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(v4[220][:2500])\n\"",
 "description": "BQT p.2138 nastuh"
}
```


### [2026-09-07T18:27:16.571Z] TOOL RESULT

```
[pdf page 221]
دنك -۱۳۸-
ستردن است که کل دربن باشد + و بر وزن | برس کوه:ازچوب وعلف سازند ‎٩‏ - ومطلق سایه
پرملون هم‌آمده است. راگویند عموماً وسایة کومراخصوضاً ‎٩‏ - ویمعنی
۰ سای کلاه هم بنظر آمده است ؛ و بمعنی سابیان
ز لگ « بکر اول بر وزن خفتك ۰ یه کل هم بنظن هد * و بعمتی بیان
4 کوش ۱ یکراول هم کفته‌اند ‎٩‏ - و پفتح اول و سکون
محلوج باری ۳ پس ای بزبان عربی کرکس باشد۷ وآن پرنده‌است
لحتوه ۲ - بروزن ادوم, مردم جنگی مردارخوار . گویند | گرازمشرق پروا ز کند وبلند
و ستیزنده و جنگه آور و ستیهنده - و ابید قعل شود در یکروزیمغرب رود و باز از مغرب پرواز
وزشت راگوبند - وکسی که از جنگه و بحك ی
کند و بلند شود درهمان روز بمشرق آید ۸ ؛
ومخاسمت نمودن عاجز نشود وبتنگه یلید ی | رن اه
نگردانت - و نام پپلوا دار #۳ و این بسیار عجیب است . آنه اعلم - و دام دو
و لام پپخوالی‌هم بوده ابرالی 5 ۹
سم ۲ ستاره است در قلك موسوم بنسن طایر واقسر
نستهن * » با ها بروزن دترن » دم واقع ۷ .
برادر پیران وسه است که درکوه کناید بر دست ۰ 5
کته شد هرد - بنتم اول و ضم رای قرشغت
ن ۰ ۰ وسکون ثالی و دال ابجد » شکاری و شکارکننده
تون " - باها بر وزن رقسیدن ۰ | راکوبند ٩؛‏ وبفتح اول وضم‌انی وجنم اول‌وانی
همان ستهن برادر پیران وسه است که درجنکه | هم‌کفته‌اند .
دوازده رخ بر دست ییجن کشته شد . نهر - بر وزن همدم . نام بتی است
هر - بفتح اول و ثالی بر وزن سفر » | جورت زلی در بتضانهٌ بامیان نزديك بسرخ بت
بممنی سار باشد و آن جایی است از کوهتان | واخنگه بت؛ واورا ستواهم میگوبند با سین بی
وغیره که‌آفتاب کمتر درآن تابد۹ - وسایبان ی که | ققطه و تای قرشت .

۱ - بعمین معنی در رشیدی‌آمده .۴ - لفة خستگی نایذیر » ناافتاده « پوستی.
نام نامه صس ۲۲۹ » ضد * ستوه » (ه.م.) و ‎٩۸‏ بستوه » ؛ و اسم معنی ( حاصل مصدر )آن ستوهی
(«م.) است. « ستوه » ستیبنده بآشد درسخن وکارها . رودکی ( سمرقندی ) کوید :

ابا ( ایا . دهخد!) خورشید سالارانگیتی سوار رزم ساز وکرد نتوه . >
۰ لفت فرِّض ۰۸۵۰

۴ - ر4 : فهرست ولف » ورك : پوستی . نام نامه س ۲۲۹ + ۰

۴ - ر4 : ستیهن . 8 - رك : فپرست ولف. ‎٩‏ - مشقف «سار» (ه.م.)
ورك : دیرم .۷ - ر4 : محیطالمحیط » اقرب‌الموارد » ور :کرکس .

۸ اقانه ات . ‎٩‏ - جهانگیری بدون شاهد بهمین معنی آورده .

لستوهی - از: ستوه (ه.م.)۳ی (حاصل مصدرء اسم‌ممنی)؛ ستیهندگنجنگجوبی:
سیاهی با شگفتیها ودستانهای کونا کون زدتوهی فزون ازحد , ز البوی قزون از مر .

معزی لیشاپوری سس ۱۹۹ نه
(برهای قاطع ۳۷۰)
```


## [2026-09-07T18:27:40.671Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG stav ===\"; grep -n -i \"stōh\\|sutōh\\|nastōh\\|stauk\\|\\*staug\" CHEUNG.txt | head -12; echo \"=== MON nastuh ===\"; grep -n \"نستوه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -6; echo \"=== MON anahita/anusheh/azarmidokht ===\"; grep -c \"آناهیتا\" MON_part1.txt MON_part2.txt 2>/dev/null",
 "description": "Cheung + Mo'in greps"
}
```


### [2026-09-07T18:27:40.761Z] TOOL RESULT

```
=== CHEUNG stav ===
=== MON nastuh ===
MON_part2.txt:75790:نستوه: ۷۸-۱ [- نه (- نا) + ستوه (<- 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:75790:نستوه: ۷۸-۱ [- نه (- نا) + ستوه (<- 
=== MON anahita/anusheh/azarmidokht ===
MON_part2.txt:0
MON_part1.txt:0
```


## [2026-09-07T18:27:47.696Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75785,75800p' MON_part2.txt; echo \"=== search MON ===\"; grep -n \"اناهیتا\\|آناهیتا\\|ناهید:\" MON_part1.txt MON_part2.txt | head -6; echo \"=== anusheh ===\"; grep -n \"^انوشه\\|انوشه:\" MON_part1.txt | head -6; echo \"=== azarmi ===\"; grep -n \"آزرمیدخت\\|آزرم:\" MON_part1.txt | head -6",
 "description": "Mo'in entries"
}
```


### [2026-09-07T18:27:47.825Z] TOOL RESULT

```
تقو ۱ )۸5 (ع. نسخ تعلیق | (امر.) 
(خط.) یکی از خطوط معروف اسلامی 
معروف در ايران و افغانستان و شبه قارة هند 
و آن از خط نسخ و خط تعلیق اتخاذ شده. 
صحت کر دن. 
نستوه: ۷۸-۱ [- نه (- نا) + ستوه (<- 
انتتوه)|(ض.) نعشکی ندب کش که از 
جنگ و بحث و مخاصمت عاجز نشود و 
روی نگرداند؛ ستبهنده در سخن و کار و 
: ۱۵5 [ع.] (سص ع.) بافتن. (امسص.) 
بافت. (1.) (بز. گیا. جان.) بافت. (ص.) بافته 
شده مسنسوج. نسیج؟ ج. نسوج. نسج 
عنکیوت: تار عنکبوت 
نسح: ۸۵ [ع.] (مص‌ع.) باطل کر دن؛ زابل 
کردن. (مصل.) تغییر صورت دادن. (فل.) 
انتقال یافتن روح انسانی پس از مرگك جسمی 
=== search MON ===
=== anusheh ===
18546:انوشه: 22:۳7:0 [- نوشه - شاه‌نو] (امر.) 
=== azarmi ===
2915:آزرم: 2 (.) داد» انصاف. . شرم» حیا.
```


## [2026-09-07T18:27:56.696Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18540,18556p' MON_part1.txt; echo \"=== BQT anush ===\"; python3 -c \"\nimport re\nv1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(v1):\n    if 'انوشه' in l or 'انوش' in l and 'انوشیروان' in l:\n        print('leaf',i,'~p',i-215)\n\"",
 "description": "Mo'in anusheh"
}
```


### [2026-09-07T18:27:58.173Z] TOOL RESULT

```
درخشانتر» تابنا کتر» فروزانتر. (ص.) تاننا کث» 
درخشان. 

انسوشه: 20-2 (ص مر .) جاوید؛ باقی» 
پایدار. خوش» خرم» خوشحال. 

انوشه: 22:۳7:0 [- نوشه - شاه‌نو] (امر.) 
بادشاه نوء شاه جوان» نو شه. 

انهاء: 8 (ع. ف. انها] (مصم.) ۲ گاه 
کردن» اطلاع دادن» خبر دادن. رسانیدن 
۳ 

انهاب: ع.] (مص عم.) به تاراج دادن 
به غارت دادن. 

انهاج: آقطجه [ع. ۰] (مصل.) راه بیدا کردن؛ 
=== BQT anush ===
leaf 289 ~p 74
leaf 309 ~p 94
leaf 329 ~p 114
leaf 346 ~p 131
leaf 411 ~p 196
leaf 493 ~p 278
leaf 619 ~p 404
```


## [2026-09-07T18:28:04.405Z] TOOL CALL #54: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T18:28:04.413Z] TOOL RESULT

```


```


## [2026-09-07T18:28:08.521Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne",
 "prompt": "Give the reconstructed root, its meaning, and the descendants listed for Indo-Iranian (Avestan, Old Persian, Sanskrit), Germanic, Latin, and any note on the privative *n̥-."
}
```


## [2026-09-07T18:28:10.199Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7",
 "prompt": "What is the Persian etymology given for برنا (barnā/bornā) 'young'? Quote the Middle Persian and Avestan forms and any cited sources."
}
```


### [2026-09-07T18:28:13.379Z] TOOL RESULT

```
# Proto-Indo-European *né

**Reconstructed Root:** *né

**Meaning:** "not"

**Key Descendants:**

**Indo-Iranian:**
- Old Avestan: 𐬥𐬀𐬉 (naē)
- Old Persian: 𐎴𐎡𐎹 (n-i-y /naiy/)

**Germanic:**
- Gothic: 𐌽𐌴 (nē)
- Old Norse: né, ní, nei

**Latin:**
- nī, nōn

**Note on *n̥-:** The entry references "*n̥-" as a "derived term" with instruction to "see there for further descendants," indicating this represents a zero-grade variant of the negation particle, though specific descendants aren't detailed in this section.
```


### [2026-09-07T18:28:16.204Z] TOOL RESULT

```
# Persian Etymology of برنا

According to the Wiktionary entry, برنا derives from Middle Persian with the following etymological path:

**Middle Persian form:** The entry notes "[Book Pahlavi needed]" (ʾpwlnʾd /⁠aburnāy⁠/, "underage, youth"), described as "a Zoroastrian legal term."

**Avestan source:** The term was "borrowed from Avestan _𐬀𐬞𐬆𐬭𐬆𐬥𐬁𐬌𐬌𐬎_ (apərənāiiu, 'underage'), the negative of _𐬞𐬆𐬭𐬆𐬥𐬁𐬌𐬌𐬎_ (pərənāiiu, 'adult')."

**Proto-Iranian origin:** The ultimate source is listed as "Proto-Iranian _[\*pr̥Hnáh](/wiki/Reconstruction:Proto-Iranian/pr%CC%A5Hn%C3%A1h)_ ('full, filled')."

The entry does not cite specific published scholarly sources for these etymological claims—it presents the reconstruction directly without reference citations.
```


## [2026-09-07T18:28:22.740Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87",
 "prompt": "What etymology is given for Persian نقره (noqre) 'silver'? Is a Sogdian nʾkrtk / *nā-karta 'uncoined' origin mentioned? Also report the Arabic نقرة entry if present."
}
```


## [2026-09-07T18:28:24.634Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%83%D8%B1",
 "prompt": "What is the Arabic etymology of the root ن ك ر / نكر (nakira) 'to not know, deny'? List any Semitic cognates (Hebrew, Akkadian, Aramaic) and any Proto-Semitic reconstruction. Is any Latin or Indo-European origin mentioned?"
}
```


### [2026-09-07T18:28:26.995Z] TOOL RESULT

```
# Etymology of Persian نقره (noqre) 'Silver'

According to the Wiktionary entry, the Persian word is "Borrowed from Arabic _نُقْرَة_ (nuqra)."

The entry includes a reference to Sogdian: "Gharib, B. (1995), 'n'krtk-(w)', in _Sogdian dictionary: Sogdian–Persian–English_". However, the specific Sogdian etymology you mention (*nā-karta 'uncoined') is **not explicitly discussed** in the visible content of this page.

## Arabic Entry

The Arabic نقرة entry is **not present** in the provided web page content. The page only shows the Persian entry from the English Wiktionary.
```


### [2026-09-07T18:28:32.033Z] TOOL RESULT

```
# Etymology of Arabic نكر (nakira)

## Semitic Cognates

According to the Wiktionary entry, the root ن ك ر (n k r) has several documented Semitic cognates:

- **Hebrew**: נָכְרִי (nākhərī) meaning "foreign, non-Jew"
- **Ugaritic**: 𐎐𐎋𐎗 (nkr)
- **Akkadian**: 𒉽 (nakāru) meaning "to be an enemy or hostile, to oppose or be at war with a nation; to be alien, foreign or an outsider"

## Proto-Semitic and Indo-European

The document does not provide a Proto-Semitic reconstruction or mention any Latin or Indo-European origins for this root.

## Summary

The word belongs to the Semitic language family with attestations across multiple ancient languages (Hebrew, Ugaritic, Akkadian), suggesting an ancient Semitic origin related to concepts of foreignness, hostility, and denial. However, the source material offers no reconstructed proto-form or connections to Indo-European languages.
```


## [2026-09-07T18:28:45.393Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PLA nuqra ===\"; grep -n \"نقرة\\|nuqra\\|nuqrat\" incoming/PLA/PLA_pages.txt | head -8; echo \"=== AFM ===\"; grep -n \"نقرة\" AFM_pages.txt | head -6; echo \"=== LKT ===\"; grep -n -i \"nuqra\\|nakrtk\" LKT.txt | head -5; echo \"=== KLN negate/deny/null ===\"; grep -n \"^negate\\|^negation\\|^deny\\|^null, adj\\|^negotiate\\|^neglect\" KLN_1966.txt | head -8",
 "description": "nuqra in Arabic-loan books; KLN English words"
}
```


### [2026-09-07T18:28:45.480Z] TOOL RESULT

```
=== PLA nuqra ===
=== AFM ===
=== LKT ===
=== KLN negate/deny/null ===
10887:deny,  tr.  v.  —  ME.  denien,  fr.  F.  denier,  fr.  L.  de¬ ne  gar  e,  ‘to  deny,  reject,  refuse’  (whence  also  It. dinegare.  Proven?.,  Sp.,  Port,  denegar),  fr.  de- and  negdre,  ‘to  say  no,  to  deny,  refuse’.  See
10888:negate.
25141:negation,  n.,  denial.  —  MF.  (=  F.)  negation,  fr. OF.  negation,  fr.  L.  negationem,  acc.  of  negdtio, ‘a  denying,  denial’,  fr.  negatus,  pp.  of  negare. See  prec.  word  and  -Ion.
25142:negationist,  n.,  one  who  contents  himself  with mere  negation.  —  See  prec.  word  and  -ist. negative,  adj.,  1)  expressing  denial;  2)  the  oppo¬ site  of  positive.  —  MF.  (=  F.)  negatif  (fern. negative),  fr.  OF.  negatif,  fr.  L.  negativus,  ‘that which  denies’,  fr.  negatus,  pp.  of  negare.  See negate  and  -ive.
25147:neglect,  n.  —  L.  neglectus,  ‘a  neglecting’,  fr. neglectus,  pp.  of  neglegere,  negligere.  See neglect,  v.
```


## [2026-09-07T18:28:52.799Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Anahita",
 "prompt": "What etymology is given for Anahita? Quote the Avestan form anāhitā and its analysis (a- privative + āhita 'defiled'), and the Middle/New Persian forms (Anāhīd, Nāhīd)."
}
```


## [2026-09-07T18:28:53.892Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nice",
 "prompt": "Give the full etymology chain for 'nice' back to Latin nescius / ne- + scire, and note any mention of PIE *ne."
}
```


### [2026-09-07T18:28:56.919Z] TOOL RESULT

```
# Etymology of Anahita

Based on the Wiktionary content provided, the etymology section states:

"From Old Persian _𐎠𐎴𐏃𐎡𐎫_ (a-n-h-i-t /⁠anahita⁠/)."

The document does not include the Avestan form, its privative analysis, or the Middle/New Persian derivatives you mentioned. The etymology information presented is limited to the Old Persian origin, without the detailed linguistic breakdown requesting the a- privative prefix or āhita 'defiled' component analysis.
```


### [2026-09-07T18:28:59.990Z] TOOL RESULT

```
# Etymology Chain for "Nice"

The word "nice" traces back through the following pathway:

**Modern English** → **Old French** → **Latin** → **Proto-Indo-European**

## Detailed Breakdown

**Late 13th century onwards:** The English adjective "nice" entered usage with the meaning "foolish, ignorant, frivolous, senseless."

**Old French (12c.):** The word derives from Old French *nice*, meaning "careless, clumsy; weak; poor, needy; simple, stupid, silly, foolish."

**Latin:** The Old French term ultimately comes from Latin *nescius*, defined as "ignorant, unaware," with the literal sense of "not-knowing."

**Latin Components:**
- *ne-* meaning "not"
- *scire* meaning "to know"

**Proto-Indo-European:** The prefix *ne-* traces back to the PIE root **\*ne-** meaning "not," while *scire* connects to the PIE root **\*skei-** (related to the concept of knowing).

The semantic evolution of "nice" is notable, shifting dramatically from "foolish" through "timid," "fastidious," "delicate," and "precise" before eventually arriving at the modern sense of "agreeable, delightful" by 1769.
```


## [2026-09-07T18:29:05.918Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://iranicaonline.org/articles/anahid",
 "prompt": "What does the article say about the etymology and meaning of the name Anāhīd / Avestan Arədvī Sūrā Anāhitā? Quote the analysis of anāhita ('immaculate, undefiled') and the Middle Persian / New Persian forms Anāhīd, Nāhīd."
}
```


### [2026-09-07T18:29:07.330Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T18:29:07.955Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D8%AA%D9%88%D9%87",
 "prompt": "What etymology is given for Persian ستوه (sotuh) 'exhausted, weary, vanquished'? Give the Middle Persian form and any Avestan/Old Iranian source. Also mention نستوه if present."
}
```


### [2026-09-07T18:29:11.438Z] TOOL RESULT

```
# Etymology of Persian ستوه (sotuh)

Based on the Wiktionary content provided, **no etymology is given** for this word. The entry explicitly states:

"(This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium.)"

No Middle Persian forms, Avestan sources, Old Iranian cognates, or information about the related term نستوه (nastuh) are provided in the available documentation. The page actively solicits contributions to complete this etymological information.
```


## [2026-09-07T18:29:16.539Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Anahita",
 "prompt": "Quote the etymology section: the Avestan name Arədvī Sūrā Anāhitā, the meaning of each element (especially anāhitā 'immaculate/undefiled' as a- privative + *āhita), and the Middle Persian Anāhīd / New Persian Nāhīd forms."
}
```


## [2026-09-07T18:29:18.309Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Azarmidokht",
 "prompt": "What etymology/meaning is given for the name Azarmidokht (Āzarmīgduxt)? Quote any analysis of āzarm and duxt, and any statement that it means 'elderly/venerable daughter' or 'ageless'."
}
```


### [2026-09-07T18:29:21.670Z] TOOL RESULT

```
# Etymology of Anahita

The Avestan name **Arədvī Sūrā Anāhitā** comprises three elements:

- **Arədvī**: "a word otherwise unknown, perhaps with an original meaning 'moist'" that is specific to this divinity
- **Sūrā**: a generic Avestan adjective meaning "mighty"
- **Anāhitā**: a generic adjective meaning "pure," derived from the a-privative prefix combined with a root meaning "undefiled"

These descriptive epithets also appear applied to other divine concepts in Zoroastrian texts. The goddess's name evolved through linguistic history: in Middle Persian texts, it became **Ardwisur Anāhīd**, and in New Persian, it is rendered as **Nāhīd** or similar forms.
```


### [2026-09-07T18:29:22.279Z] TOOL RESULT

```
# Etymology of Azarmidokht

According to the Wikipedia article, the name's meaning is provided as follows:

"Azarmidokht" is the New Persian variant; her original name was Middle Persian _Āzarmīgdukht_, meaning **"daughter of the respected one,"** referring to her father Khosrow II.

The article does not provide a detailed etymological breakdown of the individual components (_āzarm_ and _duxt_), nor does it mention interpretations such as "elderly/venerable daughter" or "ageless."
```


## [2026-09-07T18:29:38.460Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nv1=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(v1[246][1300:])\n\"; echo \"=== HRN/HUB azarm ===\"; grep -n -i \"âzarm\\|azarm\\|äzarm\" HRN.txt HUB.txt | head -8; echo \"=== PHD azarm ===\"; grep -n -i \"azarm\" PHD.txt | head -5",
 "description": "BQT azarm footnote; Horn/MacKenzie azarm"
}
```


### [2026-09-07T18:29:39.793Z] TOOL RESULT

```
ند .
۱- بخواری و زاری گذاشتن باشد. ۷۲- تقصیی
و گذاه را کویند. ۱۳ - بمعنی حسامان شدن‌باشد.
6 - دام دختر خسرو پروم است ۰۸ واو چهار
ماه پادشاهی کرد .
]زر میداخت ۰۷ بکی مم و خم
دال , نام دخترخسرو پرویز است ؛ و آوچپازساه
و ببعنی گوبند شش‌عاه پادشاهی کرد- ونام شهری
هم‌هت که او بنا کرده است .
هيچيك از مدارد قدیمه اسن نام برای پدر ابراهیم نیامده و نام حقیقی او تارح با تارج است .
قرتکل126061] بدلابلی«عازر» و«آزرگرا ماود ازکلمه عبری ج و و(
دانته گوید آن تام‌خادم وفادار ابراهیم بود *جفری ۵۴ - ۵*
و رگ : * داش‌قائمعارف ابلام » و او به بت گرویت نراش معروف است : منت جاهلان است که
چون بدلیل از خس قرو مانند سلسلهٌ خصومت جنبانند چون آزر بت تراش‌ که . ۰۰« کلستان »
۶ لت نزمه * . ۴ صحیم آذرباد است . ره : آذرباد . ۴ - ره :
اردا وبراف. ۴ - تحرف «آترخش». . ۵ -بهپلوی222۳۳70 «منای ..»۲۹4‏ * - مراد
ِ صسلددوات است که اعتاهاً آنرا یر ۳ از آزرم ۱ آزرءنبخت ( داستهاند ۵ ره 4 آزرمیدخت.
۴- ۰ آژرمی ۲+ دخت . ج. اول در اوستا 8۰22۳6702 که خود مرکب است
از 2 علامت نی و 22۲6002 حم رد 2211۳102 و 2217188 که هر دو صفت است بمعنی
قرغوت و شکته و 281801 در سانسکریت 2۲201[ بپمن معنی است , 22117۷2 بمعنی پیری
بقه در صفحاٌ ۳۷
=== HRN/HUB azarm ===
HUB.txt:8718:i^eiz, Anosrua^i; Azarmiduxt (Sebeos) = phi. *^^(irw?A;f/Ma?^,
HUB.txt:8719:np. Azarmiduxt \ eritasard 'Jiingling = phi. *re^ai:sard (phi.
HRN.txt:661:deutung *Ehre, Achtung* (GF.), anäzarm (Men.), vergl. Vis und Kämln,
=== PHD azarm ===
224:ayabag 15 azarmigih
753:ageless azarman. aggression hénih. aggressive mustabarmand. agile čābuk.
2205:harm (n.) ak, anāgīh, azarm, bei, bēšišn, wizend, zyàn.
2441:injury āzārišn, azarm, wizāyišn, wizend.
4108:unaging azarmān.
```


## [2026-09-07T18:30:01.565Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN negate/null/negotiate ===\"; grep -n \"^negate\\|^null,\\|^negotiate\\|^none,\\|^not, adv\\|^no, adv\" KLN_1966.txt | head -8; echo \"=== SKT ===\"; grep -n \"^No, not\\|^No (1)\\|^Not, \\|^None, \\|^Nice, \" SKT.txt | head -8; echo \"=== SYN not ===\"; grep -n \"NOT\\b\" SYN.txt | head -6; echo \"=== IEC ne ===\"; grep -n \"^ne 'not\\|^ne, not\\|nē 'not\" IEC.txt | head -6",
 "description": "KLN/SKT/SYN/IEC for negation"
}
```


### [2026-09-07T18:30:01.671Z] TOOL RESULT

```
=== KLN negate/null/negotiate ===
10888:negate.
25749:null,  adj.  —  Fr.  F.  nul — or  directly — fr.  L. niillus,  ‘not  one,  not  any,  none’,  contraction  of *ne(e)  oin(o)los,  ‘not  one’,  fr.  neg.  pref.  ne-  and dimin.  of  OL.  oinos  (whence  L.  unus),  ‘one’.  See no,  adv.,  and  one  and  cp.  nullify,  nullity,  annul, nullah,  n.,  a  ravine;  a  watercourse  (Anglo-Ind.) —  Hind,  nald,  ‘brook,  watercourse,  ravine’, nullification,  n.  —  Late  L.  nullificatio,  gen.  -dnis, fr.  nullificatus,  pp.  of  nullificare.  See  next  word and  -ion.
=== SKT ===
12261:Nice,  fastidious,  deticioiii. M.  £.  nut,  fooli&h.  simple,  later' and  lastly  delicious.  *  O.  F.  MrVr. simple :  orig.  ignorant.  —  L.  n/mira of  ntscius,  ignorant.  ~  L.  nt,  not ;  ai know.    See  No  (i)  and  Solenoe.
=== SYN not ===
32:PARP OOP HOOP Oy OPE x a LS A. ; ° Gg Gegs laa wry ; NOT TO BE is-U: : -~~ > rbird daly Dalrndinetin tts Dratoatin? ci te dnl, rtp tind bodied t &. = -
13913:SCELLANEOUS PHYSICAL ACTS, ETC. 551 wisCE 9.192 KNOT (sb.) : Lith. mazgas aur knutr Lett. mazgs oe Dan. knude ChSl.  (qzlii) sae Sw. knut SCr.  uzao tod OE cnolta Boh. _uzel cud ME knotte Pol. wezel aD NE knot Russ. — uzel 7 Du. knoop Skt. — granthi- snaidm OHG knodo, knoto, knopf Av. pee snaidhm MHG  knode, knote, knopf NHG knoten
=== IEC ne ===
```


## [2026-09-07T18:30:10.366Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('n',len(leaves))\n# find leaf with page 319 content: look for 'Satznegation' or 'ne, ne, nei'\nfor i,l in enumerate(leaves):\n    if 'Satznegation' in l or 'Verneinungspartikel' in l:\n        print('leaf',i, l[:1400].replace('\\n',' '))\n        print('---')\nEOF",
 "description": "Walde-Pokorny ne"
}
```


### [2026-09-07T18:30:11.774Z] TOOL RESULT

```
n 725
leaf 323                                                                ne, ne, nei,      n                                                319  lie,    ne, nei Satznegation    einzelspracUich auchWortnegation geworden,          s.   Brugmann BSGW. 1901, 102,  Grdr. II^ 1, 105 f.), n Wortnegation.          Vgl. die ZusammenfassuDgen bei Brugmann II ^ 3, 974 ff.; zur Ablosung          des prohibitiven     durch ne aufierhalb des Ar. Arm. Gr. Alb. s. II          3,   827.          Eine Abl.-Stufe no--                   ist   nicht nachzuweisen.        '^ne:        ai.    na „Tiicbt“ (iiber na „wie, gleichsam^* und das                                      gleichartige        lit.  iiei^   klr. poln. ni „\Yie, gleicbsam”,                          sowie iiber anderes, dessen Deutung aus dem negativen ^ne                          strittig    ist,    s. unter no- Pron.-St.), av. ap. na „nicht’‘,  ai. nd-va           = av. na-va „oder nicht^' (vgl.                         lat. ne-ve,      und genauer ir,         w       s.   u.)  ai.naca „und nicht^' (= lat.                                  neque usw.),           gr. ve-     nur    (als   Ersatz von n-) in Zs.mit verbalen, dann auch andern Adj. mit dem Anlaut              e, a, mit  denen es kontrabierfc ist, z. B. vrjxeoTog^ vrjXe'qg^ vAvv^ivog (die Form vd- dann auch z. T. in Zs. mit kons. anl. 2. Glied verschleppt; vr\noivog. dor. vaTioivog) 
---
leaf 324                                                                                ;     ^d20                                                       ne-, no*, nes-, nos-    Hdb. 32, 152; hingegen geht Pedersen KZ. 40, 147, KGr. I 250, 301 von idg. *ne aus, dasaber                        —                           auBer im betonten nc-ch        wohl durchaus die                      — Proklisenentwicklung zu na erfabren hat, s. o.); mit der Kopula kontrahiert air. ni „ist nicht^^ aus ^nest^ ^ne-est (Pedersen KG*. II 421 sieht darin das gewohnliche ni mit ausgelassener Kopula)   got. 7ie „nein“. tJber aksl. ne~hbio „jemand^^ u. dgl. s. Pedersen KZ. 40, 147.      '*nei betontes „nicht“, av. nae~cis „keiner^‘, adv. iiaecis verstarkte Negation; lat.    n7, altlat. 7iei             Adv. und Konj.                1.    alter „nicht,     daB      nicht“, 2, „si non'', qiiid-nt;          osk. nei „nicht“ {nei-p „neque“);                               got. 7iei (dji.key.) „nicht",    ahd. m emphatisches „nicht“;                             lit.    nS-Jcas ,.niemand“,          7iel   „nicht einmal"     (iiber nei „wie“           s.    o.);abg. 7ii „neque% 7^^-'k^to „niemand" (iiber klr. poln. ni „wie“,       s. o.).       Die germ. Formen vielleicht aber = ai. 7ied „durchaus nicht, damit nicht", av. ndit^ ap. 7iay aus idg. id „das nicht", Osthoff PBrB. 8, 312; Prellwitz BB. 22, 77 Anm. sucht d
---
```


## [2026-09-07T18:30:24.949Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne' \\\n 'https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7' \\\n 'https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D9%86%D9%83%D8%B1' \\\n 'https://www.etymonline.com/word/nice' \\\n 'https://en.wikipedia.org/wiki/Anahita' \\\n 'https://en.wikipedia.org/wiki/Azarmidokht' \\\n 'https://en.wiktionary.org/wiki/Anahita' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 351, root Ne 1/Nei 3/An 4 (PIE *ne \"not\"): root + nodes na/naiy, a-/an-, borna, Anahita, Azarmidokht, noqreh, Arabic n-k-r, English nice' 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-07T18:30:29.107Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cdc8f2896cc9caef.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5660da974237acbf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcf39b8ae8d46151.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/134980f7e7bdf40c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/947bb0e6db01c883.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca1b7985511dbef3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1658c7edf418ab0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cffbe374515ee25b.txt
```


## [2026-09-07T18:30:32.872Z] TOOL CALL #70: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T18:30:32.911Z] TOOL RESULT

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


## [2026-09-07T18:30:46.922Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ndef nearby(path,lineno,win=40):\n    L=open(path,encoding='utf-8',errors='replace').read().split('\\n')\n    lo=max(0,lineno-1-win); hi=min(len(L),lineno-1+win)\n    nums=[]\n    for k in range(lo,hi):\n        for m in re.finditer(r'(?m)^\\s*(\\d{2,4})\\s*$',L[k]):\n            nums.append((k+1,m.group(1)))\n    return nums\nfor ln in (4241,4247,4458,4524,5918,5989,3658):\n    print('BRT line',ln,'nums',nearby('BRT.txt',ln)[:8])\ndef leafof(path,lineno):\n    t=open(path,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nfor ln in (4182,5037,9258):\n    print('HUB line',ln,'leaf',leafof('HUB.txt',ln),'-> printed p',leafof('HUB.txt',ln)-10)\nprint('WLD Bd2 leaf 323 -> printed 319 (marker seen in text)')\n# AHD page for 'ne. Not.'\nprint('AHD leaf', leafof('AHD_watkins1985.txt',774))\nEOF",
 "description": "Locate page/column numbers"
}
```


### [2026-09-07T18:30:48.607Z] TOOL RESULT

```
BRT line 4241 nums []
BRT line 4247 nums []
BRT line 4458 nums [(4478, '27')]
BRT line 4524 nums [(4533, '130'), (4552, '131'), (4555, '132')]
BRT line 5918 nums [(5957, '224')]
BRT line 5989 nums [(5957, '224'), (5995, '326'), (6010, '827')]
BRT line 3658 nums [(3618, '80'), (3657, '82'), (3691, '84')]
HUB line 4182 leaf 130 -> printed p 120
HUB line 5037 leaf 154 -> printed p 144
HUB line 9258 leaf 268 -> printed p 258
WLD Bd2 leaf 323 -> printed 319 (marker seen in text)
AHD leaf 73
```


## [2026-09-07T18:31:57.183Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ne / anosag ===\"; grep -n \"^nē \\|nē \\[\\|not, nor\\|anōšag\\|anōš \" PHD_mackenzie.txt | head -8; echo \"=== KLN munkar/nakir ===\"; grep -n -i \"munkar\\|nakir\\|Nakir\" KLN_1966.txt | head -5; echo \"=== FVQ nakir ===\"; grep -n -i \"munkar\\|nakir\\|n-k-r\" FVQ_pages.txt | head -5; echo \"=== MON enkar ===\"; grep -n \"^انکار\\|انکار:\" MON_part1.txt | head -4; echo \"=== POK leaf 252-253 ===\"; python3 -c \"\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (251,252,253):\n    print('--- leaf',i,'---')\n    print(t[i][:400])\n\"",
 "description": "Final greps"
}
```


### [2026-09-07T18:31:58.548Z] TOOL RESULT

```
=== PHD ne / anosag ===
=== KLN munkar/nakir ===
=== FVQ nakir ===
=== MON enkar ===
18344:انکاره: 0-6 ,208281-3 (.) بندار؛ وهم. 
22058:برانکار: ۲ (.) تختی که بیماران و 
23382:بستانکار: 602۱-2۲ (ص‌فا.) طلبکار 
35709:پیمانکار: ۲-7 (ص‌شغ.) کسی که انجام 
=== POK leaf 252-253 ===
--- leaf 251 ---
h  Banateanu  REtlE.  1,  120  aus  semit. quhbäh-,  Van  Windekens  Lexique  48  vergleicht  toch.  A  kumpäc  , Trommel');
Tiv^ßj]  ;Kopf,  'Avq}r]^  EM.,  Suid.;,  hom.  xvußaxog  ^Spitze  eines  Helmes' (vgl.  yiv(,ißrj),  s.  Leumann  Hom.  Wörter  231  ff.;
lat.  (mit  präsentischer  Nasalierung)  -cumbö  (s.  oben  S.  590);
mir.  comm  , Gefäß',  cummal  , Becher,  Schale',  cymr.  cwmm  ,
--- leaf 252 ---
. §üra-)  , stark,  gewaltig',  Superl.  sdvista-  (=  ai.  sdvistha-)]  süra-  m.  ,Loch, lacuna',  npers.  süräx  ,Loch^  ( :  ytvag  =  ilögog  :  ijöcoQ ;  s.  auch  arm.  sor^ allenfalls  lat.  caver-na)]
arm.  sun  (s.  ohen  zu  ai.  süna-  , Leere');  sor  ,Loch'  (*so[v]oro-  aus  *sovaro- =  ai.  *savira-j  gr.  -nvag),  soil  , Höhle'  (*keu-lo-)',
alb.  thele  ,tief'  (=  xd(/)tAog;  o
--- leaf 253 ---
 ;  hierher  auch  cavea  f.  , Käfig', mlat.  cavellum  ,Korb',  roman.  *caväneum  (M.-L.  1786)  ,Korb,  Wiege';
gall.  PN  Kavaqog,  Cavarillus  (assimil.  aus  *covaro-  :  ai.  savira-),  cymr. cawr  (*cawar),  com.  caur  ,Riese';  mir.  Nom.  Plur.  cöraid  , Helden',  kirchlich
38
594
zu  ,Sünder^  verschlimmert;  mir.  cüa  (^kouios)  ,hohl^  ( :  xdo^,  lat.  cavus);juas8 ,Höhle^;   bre
```


## [2026-09-07T18:32:15.544Z] AGENT

Now I have enough evidence. Let me write the verification file.


## [2026-09-07T18:39:50.750Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /home/sfmqrb/git/rishe/data/verification/page-351.json <<'JSONEOF'\n{\n  \"pdf_page\": 351,\n  \"book_page\": 321,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 3,\n      \"root\": \"Ne 1, Nei 3, An 4\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ne / *nē / *nei 'not' (sentence negation), with the zero-grade word-negation *n̥- (privative)\",\n      \"note\": \"Pokorny 756-758 heads the entry '1. ne, nē, nei Satznegation der reinen Verneinung … n̥- Wortnegation', i.e. exactly Nourai's three-way split Ne 1 / Nei 3 / An 4. Watkins (AHD) has 'ne. Not.' with '[Pok. ne 756]'. Walde-Pokorny II 319-321 the same. The language label 'Indo-European' and the gloss 'no, not' are correct; the privative *n̥- is the zero grade of the same particle, so treating it as a fourth heading (An 4) under the same root is standard practice rather than a separate root. Nourai's page split (PART 1) is only a layout device. The one blank box on the printed page (to the right of node #8) is empty in the book itself, so no content is missing from the extraction.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ne / *nē / *nei به معنی «نه، نـ (نفی جمله)» است و صورت بی‌واکهٔ آن *n̥- پیشوند نفی واژگانی (privative) را می‌سازد؛ پوکورنی (صص ۷۵۶–۷۵۸) و والده‑پوکورنی (ج ۲، ص ۳۱۹) و واتکینز (AHD) هر سه همین را می‌آورند. سه سرواژهٔ نورایی (Ne 1، Nei 3، An 4) در واقع سه صورت آواییِ یک ریشه‌اند، نه سه ریشهٔ جدا. برچسب زبانی و معنای ریشه در نمودار درست است؛ ادعای نورایی در سطح ریشه پذیرفتنی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:756\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 418 (printed p.756-757): '1. ne, nē, nei Satznegation der reinen Verneinung (ne einzelsprachlich auch Wortnegation geworden); n̥- Wortnegation; ne-kʷo-s \\\"nicht einer\\\" …' — the entry begins on p.756, exactly Nourai's citation.\"},\n        {\"ref\": \"KNT:167\", \"status\": \"partial\", \"note\": \"Kent's Lexicon pp.166-167 (KNT.txt leaves 187-188) is the a-privative section: 'akarta … neg. a- + pte. of kar-', 'axšaina- … from neg. a- + xšaina-', 'axšata- … neg. a- + pte. of xšan-'; the negation entry itself ('naiy adv. \\\"not\\\": Av. nōit̰, Phl. nē, Skt. néd; from pIE *ne') stands at p.192-193 (leaf 216), not p.167. So p.167 documents An 4 but not Ne 1/Nei 3.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"pp. 756-758 (POK_02.txt leaves 418-419)\", \"stance\": \"supports\", \"note\": \"'ne: ai. ná \\\"nicht\\\", ned … av. ap. na- \\\"nicht\\\", av. nōit̰ (= ai. ned) …'; 'nei betontes \\\"nicht\\\": av. naē-ciš \\\"keiner\\\" … ap. nay'; 'n̥- Verneinungspartikel als erstes Glied: ai. av. ap. a-, vor Vokalen an-'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 319-321 (incoming/WLD/WLD_Bd2_pages.txt leaf 323-324)\", \"stance\": \"supports\", \"note\": \"'ne, nē, nei Satznegation (einzelsprachlich auch Wortnegation geworden), n̥ Wortnegation … av. ap. na \\\"nicht\\\" … nei betontes \\\"nicht\\\", av. naē-ciš \\\"keiner\\\" … ap. nay'. Also 'Eine Abl.-Stufe no- ist nicht nachzuweisen.'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'ne' (AHD_watkins1985.txt leaf 73)\", \"stance\": \"supports\", \"note\": \"'ne. Not. 1. Germanic *ne-, *na- … 2. Latin ne-, not, and nullus … 8. Zero-grade combining form *n̥- in: a. Germanic *un-; b. Latin in-; c. Greek a-, an-; d. Sanskrit a-, an-. [Pok. ne 756.]' — the whole shape of Nourai's chart in one entry.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"na 1, ni 3, naiy; ni-us-tavah\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. and OP na 'not' is the unstressed reflex of PIE *ne (Pokorny 756: 'av. ap. na- \\\"nicht\\\"'); OP naiy (𐎴𐎡𐎹, Behistun passim, e.g. DB 1.81 'kārahyā naiy azdā abava') and Av. nōit̰ / naē-ciš go back to the stressed *nei, or to *ne + id 'that not' (Kent's own analysis: 'naiy … from pIE *ne … + *id, asn. of pron. i-'). Nourai's middle form 'ni 3' is problematic: the Avestan/Old Persian reflex of *nei is naē-/nōit̰/naiy, while a bare 'ni' as a negation is Germanic (Gothic, OHG ni) and Baltic (Lith. ne, Pruss. ni), not Iranian — Old Iranian ni- is the preverb 'down'. The second word, ni-us-tavah 'not out of power', is Nourai's own reconstruction for the ancestor of NP nastūh: no such compound is in Bartholomae or Kent (grep of BRT.txt for 'ni-us', 'ustav' finds only ustavaiti- as a proper name), so the arrow is an inference, not an attested Old Iranian word.\",\n          \"derivation_fa\": \"«نه» ایرانی باستان از *ne هندواروپایی است: در اوستایی و پارسی باستان na، و صورت تکیه‌دار *nei در اوستایی nōit̰ / naē-ciš و در پارسی باستان naiy (بارها در سنگ‌نوشتهٔ بیستون) بازتاب یافته است. صورت میانیِ «ni» که نورایی به اوستایی/پارسی باستان نسبت می‌دهد پذیرفتنی نیست؛ بازماندهٔ ایرانیِ *nei همان naē-/naiy است و ni- در ایرانی باستان پیشوندِ فعلی به معنی «فرود» است، در حالی که ni حرف نفی در ژرمنی (گوتی ni) و بالتی است. صورت ni-us-tavah «بی‌توان‌نشده» نیز بازسازی خودِ نورایی است و در فرهنگ بارتولومه و کنت شاهدی ندارد؛ پس این بند با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:756\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 418, p.756-757: 'ne: ai. ná \\\"nicht\\\", ned (ned id) ds., av. ap. na- \\\"nicht\\\", av. nōit̰ (= ai. ned)'; and leaf 419, p.757-758: 'nei betontes \\\"nicht\\\": av. naē-ciš \\\"keiner\\\" … ap. nay'. Supports na and naiy; says nothing about a compound ni-us-tavah.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"p.192-193 s.v. naiy (KNT.txt leaf 216)\", \"stance\": \"supports\", \"note\": \"'naiy adv. \\\"not\\\": Av. nōit̰, Phl. nē, Skt. néd; from pIE *ne, Skt. na, Lt. ne-scio \\\"I don't know\\\", + *id, asn. of pron. i-, Lt. id, OP id-am' — the OP form and its PIE source exactly as drawn.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt, greps for 'ni-us', 'nius.tav', 'us.tav'\", \"stance\": \"silent\", \"note\": \"Bartholomae has no *ni-uz-tavah- (the only near hit is 'j. ustavaitī- f. EN. einer gläubigen Frau', a woman's name, and the river-name Ustavaitī); the compound Nourai posits is unattested in Avestan.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-320\", \"stance\": \"supports\", \"note\": \"'av. ap. na \\\"nicht\\\" … av. nōit̰, ap. nay aus idg. *ne id \\\"das nicht\\\"' — same two Iranian forms, same PIE source.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"na «نه (نا ـ)»; nastŭh «نستوه»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP نه na / نا nā- is the direct continuation of MP nē (< Old Iranian *na/*naiy < PIE *ne); Kent already gives the chain 'OP naiy … Phl. nē'. The prefix نا- is the same particle in composition (ناتوان, نادان). نستوه nastūh 'indefatigable, a fighter who does not tire' is genuine and old (Rudaki, Ferdowsi), but its second element is not Nourai's *us-tavah: Mo'in analyses it in Farhang-e Fārsi as «نستوه [= نه (= نا) + ستوه]» and in his footnote to Borhan-e Qate' p.2138 as «لغةً خستگی‌ناپذیر، ناافتاده … ضدّ ستوه», i.e. na- + ستوه sotuh 'worn out, vanquished' (MP stōh). So the negative element comes from *ne exactly as the chart says, but the compound was formed inside Persian on ستوه, not inherited from an Avestan/OP *ni-us-tavah; that half of the arrow is the author's reconstruction.\",\n          \"derivation_fa\": \"«نه» و پیشوند «نا-» در فارسی نو بازماندهٔ مستقیم nē فارسی میانه و آن از *na/*naiy ایرانی باستان و در نهایت از *ne هندواروپایی است (کنت: OP naiy … Phl. nē). «نستوه» واژه‌ای کهن است (رودکی، فردوسی) و معین در «فرهنگ فارسی» آن را «نه (= نا) + ستوه» و در حاشیهٔ برهان قاطع (ص ۲۲۱۰/۲۱۳۸) «لغةً خستگی‌ناپذیر، ناافتاده … ضدّ ستوه» می‌داند. پس جزء نفیِ آن درست از همین ریشه است، اما ترکیب در دورهٔ فارسی نو (یا میانه) بر پایهٔ «ستوه» ساخته شده و صورت اوستایی/پارسی‌باستانِ *ni-us-tavah که نورایی می‌آورد سندی ندارد؛ بنابراین این بند با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2210\", \"status\": \"partial\", \"note\": \"BQT vol. 4, pdf p.293 = printed 2210 (incoming/BQT/BQT_v4_pages.txt): this is the head of the نـه section ('بیان بیست و سیم — در نون با ها مشتمل بر هفتاد لغت و کنایت'), so it does cover نه; but the نستوه entry is at printed p.2138 (pdf 221), where Mo'in's footnote reads «لغةً خستگی‌ناپذیر، ناافتاده … ضدّ ستوه (ه.م.) و بستوه».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. نستوه (MON_part2.txt line 75790)\", \"stance\": \"partial\", \"note\": \"«نستوه [= نه (= نا) + ستوه] (ص.) … کسی که از جنگ و بحث و مخاصمت عاجز نشود و روی نگرداند» — Mo'in derives it from نه + ستوه, i.e. the negative particle plus an Iranian word for 'worn out', not from *ni-us-tavah.\"},\n            {\"src\": \"BQT\", \"where\": \"printed p.2138 s.v. نستوه (BQT vol. 4, pdf 221)\", \"stance\": \"partial\", \"note\": \"«نستوه: مردم جنگی و ستیزنده و جنگ‌آور و ستیهنده … و کسی که از جنگ و مخاصمت نمودن عاجز نشود و بتنگ نیاید» + Mo'in's note «ضدّ ستوه». Confirms the word and the negative prefix, not the Avestan compound.\"},\n            {\"src\": \"KNT\", \"where\": \"p.192-193 s.v. naiy\", \"stance\": \"supports\", \"note\": \"'naiy … Phl. nē' — the Middle Persian intermediate for NP نه.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"a- 2, â- 2, an-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Indo-Iranian privative prefix a- (before consonants) / an- (before vowels) is the regular zero grade *n̥- of *ne, syllabified as a- in Indo-Iranian exactly as it becomes Greek a-/an- and Latin in-. Pokorny 757-758: 'n̥- Verneinungspartikel als erstes Glied: ai. av. ap. a-, vor Vokalen (auch i, u) an-'. Kent's Lexicon shows it working in Old Persian compounds: akarta- 'not built' (neg. a- + pte. of kar-), axšaina- (neg. a- + xšaina-), axšata- 'unhurt' (neg. a- + pte. of xšan-), and lists 'a- an-, the common negative prefix' among the inseparable prefixes. The variant ā- with long vowel that Nourai adds is the Avestan lengthened/compositional form seen in his next node (ā-zarema-), and is standard in compounds where the following syllable was originally vowel-initial.\",\n          \"derivation_fa\": \"پیشوند نفیِ هندوایرانی a- (پیش از همخوان) و an- (پیش از واکه) همان درجهٔ صفرِ *n̥- از ریشهٔ *ne است که در هندوایرانی به a- و در یونانی به a-/an- و در لاتین به in- بدل شده است. پوکورنی (صص ۷۵۷–۷۵۸) صریحاً می‌نویسد: «n̥- ادات نفی در جزء نخست: سنسکریت، اوستایی و پارسی باستان a-، پیش از واکه an-». کنت نیز آن را در میان «پیشوندهای جدانشدنی» پارسی باستان می‌آورد و نمونه‌هایی چون a-karta «ساخته‌نشده»، a-xšaina و a-xšata «آسیب‌نادیده» را شاهد می‌گیرد. ادعای نورایی در این بند درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:757\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 419 (printed pp.757-758): 'n̥- Verneinungspartikel als erstes Glied: ai. av. ap. a-, vor Vokalen (auch i, u) an-; gr. ἀ-, vor Vokal ἀν-; lat. in-, ältest en- …' — exactly the node.\"},\n            {\"ref\": \"KNT:167\", \"status\": \"supports\", \"note\": \"KNT.txt leaves 187-188 (printed pp.166-167) carry the OP a-privative compounds: 'akarta … neg. a- + pte. of kar- \\\"make\\\"'; 'axšaina- … from neg. a- + xšaina-'; 'axšata- adj. \\\"unhurt, undisturbed\\\": neg. a- + pte. of xšan-'. The prefix itself is listed in the grammar as 'a- an-, the common negative prefix'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt, the a-/an- entries (e.g. an-āhita-, an-aoša-, an-usant-, a-zarəma-, a-sūra-)\", \"stance\": \"supports\", \"note\": \"Bartholomae's whole a-/an- section is built on this prefix; e.g. 'j. an-usant- Adj. \\\"der (etwas) nicht (tun) will, widerwillig\\\"' and 'j. a-zaošа- m. \\\"Nichtwille, Nichtabsicht\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-321\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny gives the same 'n̥ Wortnegation' beside 'ne, nē, nei Satznegation', with the Indo-Iranian a-/an- reflexes.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'ne', §8\", \"stance\": \"supports\", \"note\": \"'8. Zero-grade combining form *n̥- in … d. Sanskrit a-, an-, not' — the same privative, same root.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"a-purn-ây\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MP aburnāy [ʾp(w)lnʾd] 'under age, child' is the privative a- (node #3) prefixed to purnāy [pwlnʾd] 'adult'; MacKenzie's entry reads 'aburnāy … under age, child. ~īh: childhood' and 'purnāy [pwlnʾd = Av. pərənāyu-] adult'. The Avestan source apərənāyu- 'minor' is itself a- + pərəna- 'full' (PIE *pelh1- 'fill') + āyu- 'life-span, age' (PIE *aiw-, Nourai's ☞Aiw), so Nourai's gloss \\\"not full of life\\\" and his cross-reference to Aiw are both on target. Bartholomae attests the derivative at V.5.11 (hiθrikaca apərənāyūkasca). In Middle Persian the Old Iranian intervocalic -p- of the second element was voiced after the prefix (a-p- > ab-), whence the transliteration ʾpwlnʾd; Nourai's 'a-purn-āy' keeps the etymological -p-.\",\n          \"derivation_fa\": \"فارسی میانه aburnāy (نگارش: ʾp(w)lnʾd) «نابالغ، خردسال» از پیشوند نفیِ a- و purnāy «بالغ» ساخته شده است؛ مکنزی می‌نویسد: «purnāy [pwlnʾd = Av. pərənāyu-] adult» و «aburnāy … under age, child». صورت اوستاییِ apərənāyu- خود از a- (نفی) + pərəna- «پر» (از ریشهٔ *pelh₁- «پر کردن») + āyu- «عمر، زندگی» (ریشهٔ *aiw-) است؛ پس معنای «پر از عمر نشده، نابالغ» و ارجاع نورایی به ریشهٔ Aiw درست است. در گذار به فارسی میانه پِ ایرانی باستان در جایگاه میان‌واکه‌ای به ب نرم شده (a-p- > ab-)، ولی نورایی نگارش تاریخیِ a-purn-āy را نگه داشته است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:264\", \"status\": \"partial\", \"note\": \"BQT vol. 1 leaf 484 = printed p.264 is indeed the برنا page ('برنا: … جوان و نوچهٔ اول عمر و ظریف را گویند'), but the Pahlavi etymology is not footnoted there; Mo'in gives it at BQT p.85 (leaf 295) s.v. اپرناک: «۷ - پهلوی aparnāy, apurnāy بمعنی برنا، جوان «یونکر ۹۹»».\"},\n            {\"ref\": \"KNT:209\", \"status\": \"not_found\", \"note\": \"The local OCR of Kent (KNT.txt, 232 form-feed leaves) ends at printed p.207 (leaf 231 = 'z-' entries), so p.209 could not be read; nothing in Kent's Lexicon between pp.164-207 mentions purnāy/aburnāy, and the word is Middle Persian, not Old Persian, so the citation looks misplaced.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp.5 and 69 (PHD.txt lines 170, 551; PHD_mackenzie.txt lines 828, 4273)\", \"stance\": \"supports\", \"note\": \"'aburnāy [ʾp(w)lnʾd, v. purnāy | N burnā] under age, child. ~īh: childhood'; 'purnāy [pwlnʾd] adult' and in the addenda 'purnāy [pwlnʾd = Av. pərənayu-] adult'. Note MacKenzie glosses it 'under age', not 'young'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.120 and p.258 §156 (HUB.txt lines 4182, 9258)\", \"stance\": \"supports\", \"note\": \"'burna \\\"Jüngling\\\" = paz. awarnai Shk. 238, phl. apurnai, apurnayak, zd. apərənāyu-, apərənāyuka-'; and §156 'rn bleibt in: burna, barnā \\\"Jüngling\\\", zd. apərənāyu-, phl. apurnāi, paz. awarnai … (neben pur \\\"voll\\\" = zd. pərəna-)'. Hübschmann's transliteration 'apurnāi' is Nourai's very form.\"},\n            {\"src\": \"BRT\", \"where\": \"BRT.txt line 5985 (Vd. 5.11)\", \"stance\": \"supports\", \"note\": \"Bartholomae quotes 'hiθrikaca apərənāyūkasca varaiθīm … pantam azōit̰ V.5.11', attesting the Avestan derivative apərənāyūka- 'minor'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"bornâ «بُرنا»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP برنا bornā / برنا barnā 'young, youth' continues MP aburnāy: the unstressed initial a- of the prefix was lost in New Persian (aphaeresis, as in MP abrēšom > NP abrēšam/برشم, MP apē- > NP بی-), the voiced -b- of a-b(u)rnāy remained as the initial, and MP final -āy became -ā. Hübschmann sets this out twice: §156 'rn bleibt in: burna, barnā \\\"Jüngling\\\", zd. apərənāyu-, phl. apurnāi, paz. awarnai', and p.120 among the words in which Middle Persian ap- yields NP b-. Semantically 'minor, not of full age' shifted to the positive 'young man, youth' already in early New Persian (Ferdowsi: «آموزش مرد برنا و پیر»); Borhan-e Qate' p.264 glosses برنا 'جوان و نوچهٔ اول عمر'. Wiktionary gives the same chain (Av. apərənāiiu > MP aburnāy > NP برنا).\",\n          \"derivation_fa\": \"«بُرنا/بَرنا» در فارسی نو بازماندهٔ aburnāy فارسی میانه است: الفِ آغازینِ بی‌تکیهٔ پیشوند در فارسی نو افتاده (همان فرایندی که در ape- > بی- دیده می‌شود)، بِ نرم‌شدهٔ درون واژه آغازگر شده و -āy پایانی به -ā بدل گشته است. هوبشمان در «مطالعات فارسی» (بند ۱۵۶ و ص ۱۲۰) صریحاً می‌نویسد: «burna, barnā «جوان» = اوستایی apərənāyu-، پهلوی apurnāi، پازند awarnai». از نظر معنایی «نابالغ» به «جوان، نوجوان» تحول یافته است و برهان قاطع (ص ۲۶۴) آن را «جوان و نوچهٔ اول عمر» می‌آورد. پس ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%86%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:264\", \"status\": \"supports\", \"note\": \"BQT vol. 1 leaf 484 = printed p.264: «بَرنا: بفتح اول و سکون ثانی و نون بالف کشیده. جوان و نوچهٔ اول عمر و ظریف را گویند - و بمعنی خوب و نیک هم هست»; the same page has برناک 'بمعنی برنا است که جوان و نوچهٔ اول عمر باشد' and برناه.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.258 §156 and p.120 (HUB.txt lines 9258, 4182)\", \"stance\": \"supports\", \"note\": \"'a) rn bleibt in: burna, barnā \\\"Jüngling\\\", zd. apərənāyu-, phl. apurnāi, paz. awarnai Shk. 233 (neben pur \\\"voll\\\" = zd. pərəna-)'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. aburnāy\", \"stance\": \"supports\", \"note\": \"'aburnāy … | N burnā] under age, child' — MacKenzie himself equates MP aburnāy with New Persian burnā.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (checked via the BQT footnote apparatus)\", \"stance\": \"silent\", \"note\": \"The Mo'in lexicon OCR on disk (MON_part1/2) has no برنا headword with an etymology; the Pahlavi note is in his Borhan footnote at p.85 instead.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"an-âhita; an-aoša; â-zarema-dugedâ; a-xšae-na\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four are exactly right in Bartholomae. (1) Av. an-āhita- (OP *an-āhita-) 'woran kein Fleck, kein Makel ist, haftet, makellos' — an- + āhita- 'stained' (to hi-/ā-hi- 'defile'), the standing epithet of Arəduuī Sūrā Anāhitā and, in OP, the divine name Anāhita of Artaxerxes II's inscriptions; Nourai's ☞Ahu points at NP آهو 'blemish, defect', the same root, and BQT p.72 does gloss آهو as 'عیب'. (2) Av. an-aoša- 'dem kein Verderben droht, unsterblich' (Yt.10.125) — an- + aoša- 'destruction, death'. (3) Av. a-xšaēna- 'dark-coloured' (Vd. 22.4, 32.3 'gavąm axšaenanąm'), a- + a derivative of xšaēta- 'shining', i.e. literally 'not bright' > 'dark blue', which is Nourai's gloss precisely; Kent adds that Greek borrowed it as Πόντος Ἄξεινος. (4) 'ā-zarema-dugedā \\\"ageless woman\\\"' is not an attested Avestan compound: Bartholomae has a-zarəma- 'nicht abnehmend (an Stärke, von der Stimme)' and a-zarəšant- 'nicht alternd', and no compound with dugdar- 'daughter'. It is Nourai's reconstruction of the name Āzarmīduxt, and it follows Mo'in's footnote in Borhan p.36 verbatim (see ref_check), so it is a defensible reading rather than an invention — but the word as drawn is unattested, which is why the node cannot be marked confirmed.\",\n          \"derivation_fa\": \"سه واژه از چهار واژهٔ این بند دقیقاً در فرهنگ بارتولومه هست: (۱) اوستایی an-āhita- «بی‌لکه، بی‌عیب، پاک» از an- + āhita- «آلوده»، لقب ثابتِ اردویسور اناهیتا و در پارسی باستان نامِ ایزدبانو Anāhita در سنگ‌نوشتهٔ اردشیر دوم؛ ارجاع نورایی به ریشهٔ Ahu (فارسی «آهو» = عیب) نیز درست است. (۲) اوستایی an-aoša- «نامیرا، جاویدان» از an- + aoša- «مرگ، تباهی». (۳) اوستایی a-xšaēna- «تیره‌رنگ، کبود» از a- + مشتقِ xšaēta- «درخشان»، یعنی «نادرخشان»، همان معنایی که نورایی می‌دهد؛ کنت می‌افزاید که یونانی آن را در Πόντος Ἄξεινος وام گرفته است. (۴) اما ترکیبِ ā-zarema-dugedā «زنِ پیرنشدنی» در اوستا شاهدی ندارد؛ بارتولومه فقط a-zarəma- و a-zarəšant- «پیرنشدنی» را دارد. این صورت بازسازیِ نورایی برای نامِ «آزرمیدخت» است و درست همان تحلیلی است که معین در حاشیهٔ برهان قاطع (ص ۳۶) آورده؛ پس با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Anahita\",\n            \"https://en.wikipedia.org/wiki/Azarmidokht\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:36\", \"status\": \"supports\", \"note\": \"BQT vol. 1 leaf 246 = printed p.36 has آزرم and آزرمیدخت ('نام دختر خسرو پرویز است') and Mo'in's footnote: «آزرمی + دخت. جزء اول در اوستا a-zarəmaya که خود مرکب است از a علامت نفی و zarəmaya … و zarəmān در سانسکریت jaraṇa بهمین معنی است، zarəmāya بمعنی پیری» — i.e. Mo'in analyses it exactly as a-privative + 'aging', which is Nourai's arrow.\"},\n            {\"ref\": \"BQT:72\", \"status\": \"supports\", \"note\": \"BQT vol. 1 leaves 282-283 = printed pp.72-73: «آهو … و بمعنی عیب را نیز گفته‌اند» and «آهویی: بمعنی رمیدگی و عیب‌ناکی باشد» — the NP word for 'blemish' behind Nourai's ☞Ahu and behind an-āhita 'not stained'.\"},\n            {\"ref\": \"BQT:788\", \"status\": \"not_found\", \"note\": \"BQT vol. 2 leaf 248 = printed p.788 is the خوره entry (خورهٔ اردشیر, خورهٔ استخر …), which has nothing to do with this node. The page that carries خشن/خشین (the reflex of a-xšaēna-) is printed p.755 (BQT_v2_pages.txt leaf 215): «خشن: … بمعنی کبودرنگ باشد» and «خشین: هر چیز سیاه‌رنگ مایل به کبودی … و بازی را نیز گویند که پشت او کبود و تیره‌رنگ بود؛ و بعضی گویند مرغابی سیاه‌رنگ است، بکبودی مایل».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt s.v. an-āhita- (line 4458), an-aoša- (line 4241), a-zarəma- (line 5989)\", \"stance\": \"partial\", \"note\": \"'j. an-āhita-, p. *an-āhita- Adj. (fem. -tā-) \\\"woran kein Fleck, kein Makel ist, haftet, makellos\\\" … A) als weibliche Gottheit: anahita (= anāhiti) … Am. 4'; 'j. an-aoša- Adj. \\\"dem kein Verderben droht, unsterblich\\\": aurvantō … anaošāŋhō Yt.10.125'; but 'j. a-zarəma- Adj. (fem. -mā-) \\\"nicht abnehmend\\\" (an Stärke, von der Stimme)' and separately 'j. a-zarəšant- Adj. \\\"nicht alternd\\\"' — no *ā-zarəma-dugdar-.\"},\n            {\"src\": \"KNT\", \"where\": \"p.166 s.v. axšaina- (KNT.txt leaf 187)\", \"stance\": \"supports\", \"note\": \"'axšaina- adj. with kāsaka-, \\\"turquois\\\" … Av. axšaēna- \\\"dark-colored\\\", borrowed in Gk. Πόντος Ἄξεινος \\\"Black Sea\\\" … from neg. a- + xšaina-, cf. Av. xšaēta- \\\"shining\\\"' — exactly Nourai's a-xšae-na 'not bright, dark blue'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. azarmān (PHD.txt line 4108, 753)\", \"stance\": \"partial\", \"note\": \"'unaging azarmān' / 'ageless azarmān' — Middle Persian does have an a- + zarmān 'ageless' formation, which makes Nourai's morphology possible, but MacKenzie's word for the queen's name element is āzarmīg 'respected' (PHD.txt line 224 azarmīgīh).\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"ânâhîtâ «آناهیتا (ناهید)»; anŭšeh «انوشه (انوشیروان)»; âzarmîdoxt «آزرمیدخت»; xašan «خشن (خشیسار ، خشنسار)»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four descend from node #6 as drawn. (1) Av./OP Anāhitā gave MP Anāhīd (Ardwīsūr Anāhīd) and, with loss of the initial syllable, NP ناهید Nāhīd, the name of the planet Venus; the learned form آناهیتا is a modern re-borrowing of the Avestan name. (2) Av. an-aoša- 'immortal' > MP anōšag > NP انوشه anūša/anūšeh 'immortal, blessed'; Avestan/MP -au-/-ō- gives NP -ū-, and the MP adjective suffix -ag > NP -a/-eh. The royal name انوشیروان Anūšīrvān is MP Anōšag-ruwān 'of immortal soul' (the epithet of Khosrow I). (3) آزرمیدخت, the Sasanian queen (630-631), is MP Āzarmīg-duxt. Nourai (following Mo'in's Borhan footnote, p.36) reads the first element as a-zarəm(aya) 'not aging'; the prevailing modern reading is MP āzarm 'respect, honour' + duxt 'daughter' = 'daughter of the respected one' (so Wikipedia and the Sasanian prosopography), which does not involve the privative at all. Hence the node is plausible, not confirmed. (4) NP خشن xašan / خشین xašīn 'dark blue; a blue-black bird' and the compounds خشین‌سار/خشن‌سار (a dark-backed duck or hawk) continue Av. axšaēna- 'dark-coloured': Borhan p.755 glosses خشن 'کبودرنگ' and خشین as a black-blue bird, so both form and meaning match.\",\n          \"derivation_fa\": \"سه واژه از چهار واژه همان‌گونه که در نمودار آمده از بندِ پیشین می‌آیند: (۱) Anāhitā اوستایی/پارسی باستان در فارسی میانه Anāhīd (اردویسور اناهید) و با افتادن هجای آغازین در فارسی نو «ناهید» (نام سیّارهٔ زهره) شده است؛ صورت «آناهیتا» وام‌گیریِ نوِ عالمانه از خودِ نام اوستایی است. (۲) اوستایی an-aoša- «نامیرا» > فارسی میانه anōšag > فارسی نو «انوشه»؛ ō/au ایرانی به ū فارسی نو و پسوند -ag فارسی میانه به -ه بدل شده است، و «انوشیروان» همان Anōšag-ruwān «جاویدان‌روان»، لقب خسرو اول، است. (۳) «آزرمیدخت» (شهبانوی ساسانی، ۶۳۰–۶۳۱ م) در فارسی میانه Āzarmīg-duxt است؛ نورایی به پیروی از حاشیهٔ معین بر برهان قاطع جزء نخست را a-zarəmaya «پیرنشدنی» می‌خواند، اما خوانش رایج امروزی «آزرم» (احترام، شرم) + «دخت» است، یعنی «دختِ آن ارجمند»، که در آن پیشوند نفی نقشی ندارد. (۴) «خشن/خشین» و ترکیب‌های «خشین‌سار، خشن‌سار» بازماندهٔ axšaēna- اوستایی است؛ برهان قاطع (ص ۷۵۵) «خشن» را «کبودرنگ» و «خشین» را پرنده‌ای سیاه‌مایل‌به‌کبود می‌آورد. بنابراین این بند در مجموع با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wikipedia.org/wiki/Anahita\",\n            \"https://en.wikipedia.org/wiki/Azarmidokht\",\n            \"https://en.wiktionary.org/wiki/Anahita\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. انوشه (MON_part1.txt line 18546 area): «انوشه (ص مر.) جاوید؛ باقی، پایدار. خوش، خرم، خوشحال» — 'eternal, lasting', Nourai's gloss. (A homonymous second انوشه 'شاه نو' is listed separately and is not this word.) s.v. آزرم (line 2915): «داد، انصاف؛ شرم، حیا».\"},\n            {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"Borhan p.755 (BQT_v2_pages.txt leaf 215) for خشن/خشین/خشین‌سار, and p.36 (BQT_v1_pages.txt leaf 246) for آزرمیدخت with Mo'in's a-zarəmaya footnote; both are the pages behind Nourai's Persian forms.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"printed pp.36 and 755\", \"stance\": \"supports\", \"note\": \"«آزرمیدخت: نام دختر خسرو پرویز است» (p.36) and «خشن: بمعنی کبودرنگ باشد» / «خشین: … مرغابی سیاه‌رنگ است بکبودی مایل» (p.755).\"},\n            {\"src\": \"MON\", \"where\": \"s.v. انوشه, آزرم\", \"stance\": \"partial\", \"note\": \"Supports انوشه 'جاوید، باقی، پایدار'; but for آزرم Mo'in's lexicon gives 'داد، انصاف؛ شرم، حیا' ('justice; modesty'), i.e. the 'respect' sense that underlies the rival reading of آزرمیدخت.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. azarmān, azarmīgīh\", \"stance\": \"partial\", \"note\": \"MP azarmān 'unaging' beside āzarmīg/azarmīgīh 'respected/respect' — both elements exist in Middle Persian, which is precisely why the name is ambiguous.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"a-karana; a-muyamnô; a-sŭr; an-usant\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are genuine a-privative formations attested in Bartholomae. (1) Av. a-karana- 'ohne Ende, endlos, uranfänglich' (Yt.13.48 'akarana anaγra ašaonō stiš'; also of Vayu, 'akaranahe vayaoš uparō.kairyehe') — a- + karana- 'end, limit' (Nourai's ☞Karana). (2) Av. a-muyamna- 'unbeweglich, wovon nicht abzubringen' (Vr.7.1, Yt.17.15) — a- + the middle participle of mav-/mu- 'to move, push', which Pokorny lists under '2. meu-, meuǝ- \\\"fortschieben\\\"' on exactly the page Nourai cites: 'ar. a-muyamnō \\\"unbeweglich, wovon nicht abzubringen\\\"' (POK 743). (3) 'a-sūr' is Bartholomae's a-svar- / a-sar- n. 'Morgendunkel, -dämmerung' (loc. asōiri, beside sūirya- n. 'Frühmahl, -stück'), i.e. literally 'when it is not yet sūr (morning meal / morning)' — Nourai's gloss 'not morning yet, dawn' is right, and his ☞Keu 4 chart (p. 264) collects Av. sūr/savah 'morning', sūram, sūirya 'breakfast', savahī 'the East' (all in Bartholomae) around it. (4) Av. an-usant- (fem. -saitī-) 'der (etwas) nicht (tun) will, widerwillig, ohne es zu wollen' — an- + the present participle of vas- 'to wish' (Nourai's ☞Wek), Yt.17.19 'nōit̰ mąm vīspe yazataŋhō anusaṇtəm frāərəsəṇta'.\",\n          \"derivation_fa\": \"هر چهار صورت، ترکیب‌های اصیلِ پیشوند نفیِ a- هستند و در فرهنگ ایرانی باستانِ بارتولومه گواه دارند: (۱) اوستایی a-karana- «بی‌کرانه، بی‌پایان» از a- + karana- «کرانه، پایان» (یشت ۱۳ بند ۴۸). (۲) اوستایی a-muyamna- «جنبش‌ناپذیر، برنگشتنی» از a- و اسم فاعل میانهٔ ریشهٔ mav-/mu- «جنبیدن، راندن»؛ پوکورنی درست در همان صفحه‌ای که نورایی ارجاع می‌دهد (ص ۷۴۳، ذیل *meu- «فرا راندن») می‌نویسد: «ar. a-muyamnō \\\"جنبش‌ناپذیر\\\"». (۳) «a-sūr» همان a-svar-/a-sar- بارتولومه است، «تاریکیِ بامدادی، سپیده‌دم» (در کنار sūirya- «چاشتِ بامدادی»)، یعنی «هنگامی که هنوز بامداد نشده»؛ پس ترجمهٔ نورایی درست است. (۴) اوستایی an-usant- «ناخواه، بی‌میل» از an- + اسم فاعل ریشهٔ vas- «خواستن» (یشت ۱۷ بند ۱۹). ادعای نورایی در این بند درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:743\", \"status\": \"supports\", \"note\": \"POK_02.txt leaf 404-405 (printed p.743): '2. meu-, meuǝ- (arisch z. T. auch mieud- : miu-) \\\"fortschieben\\\". Ai. mivati \\\"schiebt, drängt, bewegt\\\" = av. ava-mivāmahi \\\"wir beseitigen, nehmen weg\\\", ar. a-muyamnō \\\"unbeweglich, wovon nicht abzubringen\\\"' — verbatim support for a-muyamnō.\"},\n            {\"ref\": \"POK:594\", \"status\": \"partial\", \"note\": \"POK_02.txt leaves 252-253 (printed pp.593-594) is inside Pokorny's '1. keu-, keuǝ- \\\"schwellen; hohl, Höhlung\\\"' entry (ai. śū́ra- 'stark', sū́ra- 'Loch', npers. sūrāx); Pokorny's keuk- 'leuchten, hell, weiß sein, glühen' — Nourai's gloss for Keu 4 — is on p.597. Neither page mentions the Avestan a-svar-/a-sūr; the support for that word comes from Bartholomae, not Pokorny.\"},\n            {\"ref\": \"BQT:46\", \"status\": \"not_found\", \"note\": \"BQT vol. 1 leaf 256 = printed p.46 carries آشنا/آشناور/آشوب/آشور; none of this node's four words (and no Persian reflex of them) appears there.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"BRT.txt s.v. a-karana- (lines 3211, 4247, 26561), a-svar- (line 5918), an-usant- (line 4524), a-stənəta-/amuyamna- (lines 5815, 30509)\", \"stance\": \"supports\", \"note\": \"'akarana anaγra ašaonō stiš … \\\"uranfänglich\\\"' (Yt.13.48); 'j. a-svar- : -sər- n. \\\"Morgendunkel, -dämmerung\\\": asōiri (LS.) sūirim isəmnō'; 'j. an-usant- Adj. (fem. -saitī-) \\\"der (etwas) nicht (tun) will, widerwillig\\\"'; 'a-stənəta- … -taca amuyamna yazamaide Vr.7.1' and 'paiti -taya … amuyamnaya … Yt.17.15'.\"},\n            {\"src\": \"KNT\", \"where\": \"p.166 s.v. akarta-, axšata- (KNT.txt leaf 187)\", \"stance\": \"partial\", \"note\": \"Kent shows the same privative pattern productive in Old Persian ('akarta … not built, unrepaired; neg. a- + pte. of kar-'), but none of these four particular compounds is Old Persian — they are all Avestan.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-321\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny's 'n̥ Wortnegation' section is the source of Pokorny's, and lists the Indo-Iranian a-/an- compounds as the productive type.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"a-, an-: not\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit a- (before consonants) / an- (before vowels) is the same PIE zero-grade privative *n̥- as the Iranian prefix of node #3: a-mṛta- 'immortal' (: Gk. ἄμβροτος, Lat. immortalis), a-jñāta- 'unknown' (: Gk. ἄγνωτος), an-udra- 'waterless' (: Gk. ἄνυδρος) — the very equations Pokorny cites on p.758. Watkins lists 'Sanskrit a-, an-, not' as branch 8d of the root, with AHIMSA and AMRITA as the English words that carry it. The label 'Sanskrit' and the gloss are correct; the arrow from the root box is the standard one.\",\n          \"derivation_fa\": \"پیشوند نفیِ سنسکریت a- (پیش از همخوان) و an- (پیش از واکه) همان درجهٔ صفرِ *n̥- است که در ایرانی نیز a-/an- شده است: a-mṛta- «نامیرا» (برابرِ یونانی ámbrotos و لاتین immortalis)، a-jñāta- «ناشناخته»، an-udra- «بی‌آب» — همین برابری‌ها را پوکورنی در ص ۷۵۸ می‌آورد. واتکینز نیز آن را شاخهٔ ۸د همین ریشه می‌شمارد. برچسب زبانی و معنا در نمودار درست است و ادعای نورایی پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 73 s.v. 'ne': '8. Zero-grade combining form *n̥- in … d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.758 (POK_02.txt leaf 419)\", \"stance\": \"supports\", \"note\": \"'durch mehrere Sprachen durchgehende Entsprechungen sind z. B. ai. amṛta-, ἄμβροτος, immortalis; ai. ajñāta-, ἄγνωτος … ai. anudra-, ἄνυδρος'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-321\", \"stance\": \"supports\", \"note\": \"Same privative section, Indo-Iranian a-/an- listed first among the reflexes.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'ne', §8d\", \"stance\": \"supports\", \"note\": \"'Sanskrit a-, an-, not'.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Germanic\",\n          \"words\": \"ne, na, un-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic inherited both the sentence negation and the privative: *ne/*na (Gothic ni, OHG/OS ni, ne, OE ne 'not', ON né; OE nā 'no, not at all' < *ne + aiw 'ever') and the zero-grade privative *un- (Gothic/OHG/OS un-, ON ó-/ú-, OE un-). Pokorny p.757 lists 'got. ni, ahd. as. ni, ne, ags. ne \\\"nicht\\\"; aisl. né …; ags. nā \\\"ne, nicht, nein\\\", engl. nō' and p.758 'got. ahd. as. un-, aisl. ó-, ú-; im germ. durchaus durch ne- verdrängt'. Watkins has 'Germanic *ne-, *na-' as branch 1 and 'Germanic *un-' as 8a. Nourai's three forms are exactly these; the label 'Germanic' is right (Proto-Germanic rather than any single daughter).\",\n          \"derivation_fa\": \"ژرمنیِ آغازین هم ادات نفی جمله و هم پیشوند نفی را به میراث برده است: *ne/*na (گوتی ni، آلمانی علیای باستان ni/ne، انگلیسی باستان ne، و nā «هرگز نه» از *ne + aiw) و درجهٔ صفرِ *un- (گوتی و آلمانی و انگلیسی باستان un-، نورس باستان ó-/ú-). پوکورنی در ص ۷۵۷ صورت‌های ژرمنی nا و در ص ۷۵۸ پیشوند un- را می‌آورد و واتکینز نیز *ne-/*na- را شاخهٔ ۱ و *un- را شاخهٔ ۸الف همین ریشه می‌داند. سه صورتی که نورایی آورده همین‌هاست و ادعای او درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 73 s.v. 'ne': '1. Germanic *ne-, *na- in: a. Old English ne (> Middle English ne), not, and nā, no …; b. Old Norse ne, not: NAY; c. Old High German ne, ni, not: NIX' and '8a. Germanic *un- in Old English un-, not: UN-1'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp.757-758 (POK_02.txt leaves 418-419)\", \"stance\": \"supports\", \"note\": \"'got. ni, ahd. as. ni, ne, ags. ne \\\"nicht\\\"; aisl. né … ahd. nein, as. nēn \\\"nein\\\" aus *ne + oinom \\\"nicht einer\\\"; ags. nā … engl. nō'; and for the privative 'got. ahd. as. un-, aisl. ó-, ú-'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. null, nice, deny (KLN_1966.txt lines 25749, 25377, 10887)\", \"stance\": \"partial\", \"note\": \"Klein treats the Germanic negative as 'neg. pref. ne-' and cross-refers 'See no, adv.'; he covers the Latin branch in detail and the Germanic one under the individual English words of node #11.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-321\", \"stance\": \"supports\", \"note\": \"Same Germanic material (got. ni, ahd. ni/ne, ags. ne, got. nei) under 'ne'/'nei'.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"no, none, not, nothing, nor, neither, never, un-, undo\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Every item is a Germanic negative compound built on OE ne/nā: no < OE nā (*ne + ā 'ever'); none < OE nān (ne + ān 'one'); not < ME not(t), a reduced form of nought < OE nāwiht (nā + wiht 'thing'); nothing < OE nān þing / nā þing; nor < ME nor, contracted from nother (ne + ōþer); neither < OE nāhwæþer (ne + ā + hwæþer); never < OE næfre (ne + æfre 'ever'); un- < OE un- (the zero-grade privative); undo < OE undōn. Watkins's entry for 'ne' names exactly this list under the Old English branch: 'NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO1, NO2, NONE, (NOR1), NOT, NOTHING' plus 'UN-1'. The node carries no reference of its own, but it needs none: it is the ordinary English continuation of node #10.\",\n          \"derivation_fa\": \"همهٔ این واژه‌ها ترکیب‌های نفیِ ژرمنی بر پایهٔ ne/nā انگلیسی باستان‌اند: no از nā (یعنی *ne + ā «هرگز»)، none از nān (ne + ān «یک»)، not صورت کوتاه‌شدهٔ nought از nāwiht (nā + wiht «چیز»)، nothing از nān þing، nor کوتاه‌شدهٔ nother (ne + ōþer)، neither از nāhwæþer، never از næfre (ne + æfre)، و un-/undo با همان پیشوند نفیِ درجهٔ صفر. واتکینز در مدخل ne دقیقاً همین فهرست را زیر شاخهٔ انگلیسی باستان می‌آورد. این بند ارجاعی از خود ندارد ولی نیازی هم ندارد؛ ادامهٔ طبیعیِ بند ژرمنی است و ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no refs= in the book (printed page 351 shows the English box with no reference icon), so there is nothing of Nourai's to check; the claim is covered by AHD s.v. 'ne', consulted below.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'ne', §1a and §8a (AHD_watkins1985.txt leaf 73)\", \"stance\": \"supports\", \"note\": \"'Old English ne (> Middle English ne), not, and nā, no: NAUGHT, (NAUGHTY), NEITHER, NEVER, NILL, NO1, NO2, NONE, (NOR1), NOT, NOTHING' … '*un- in Old English un-, not: UN-1' — Nourai's list minus 'undo', which is simply un- + do.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. null / no, adv. (KLN_1966.txt line 25749)\", \"stance\": \"supports\", \"note\": \"'null, adj. — Fr. F. nul … fr. L. nūllus, \\\"not one, not any, none\\\", contraction of *ne(c) oin(o)los, \\\"not one\\\", fr. neg. pref. ne- and dimin. of OL. oinos … See no, adv.' — Klein's cross-reference shows he treats English no/none as the Germanic reflex of the same particle.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Nice (SKT.txt line 12261)\", \"stance\": \"supports\", \"note\": \"'Nice … L. nescius … L. ne, not; scire, know. See No (1) and Science.' — Skeat's 'No (1)' is his headword for the native negative, which he derives from the same particle.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Sogdian\",\n          \"words\": \"n`: no, not; n`-krtk: \\\"not done\\\", uncoined silver\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian nʾ (Buddhist/Christian/Manichaean) is the regular reflex of Old Iranian *na, the same particle as Av./OP na (node #1); Gharib's dictionary has a run of nʾ- negative compounds (nʾ-yrapde 'incomprehensible', nʾ-xustwānīft 'one who does not practise confession', etc.). The compound nʾkrtk / nʾkrtʾk, read na-krte / nakarta(ku), is Gharib no. 5756 and 5763, glossed 'silver (not coined)' and 'silver', with derivatives nʾkrtʾynʾk 'silvern' (5759), nʾkrtkyʾwnc 'silvern' (5762) and nʾkrtʾy pʾme 'silver coloured' (5758). Morphologically it is nā- 'not' + krta- 'made, wrought' (past participle of kar- 'to do', Nourai's ☞Kwer), i.e. 'unwrought, uncoined (metal)' — precisely the analysis and gloss in the chart.\",\n          \"derivation_fa\": \"«nʾ» سغدی بازماندهٔ منظمِ *na ایرانی باستان است، همان اداتی که در اوستایی و پارسی باستان na است؛ در فرهنگ قریب رشته‌ای از ترکیب‌های نفیِ nʾ- آمده است. ترکیبِ nʾkrtk (خوانش: nā-krta/nakarta) شمارهٔ ۵۷۵۶ و ۵۷۶۳ فرهنگ قریب است با معنی «سیم، نقرهٔ سکه‌ناخورده»، همراه با مشتقاتی چون nʾkrtʾynʾk «سیمین» و nʾkrtʾy pʾme «سیم‌رنگ». ساختِ آن nā- «نه» + krta- «کرده» (اسم مفعول ریشهٔ kar-) است، یعنی «ناکرده، نامسکوک»؛ همان تحلیل و همان معنایی که نورایی می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:32\", \"status\": \"not_found\", \"note\": \"Neither reading of '32' fits: Gharib entry no. 32 is 'ʾcʾy B' (unrelated), and printed p.32 (SOD_pages.txt leaf 97-98, printed page = leaf − 65) holds entries 838-857 (ʾktʾnyy, ʾkwrδ, ʾkwsʾnyk …). The material Nourai uses is at entries 5741-5765, printed p.231 (SOD_pages.txt lines 20195-20260): '5756 nʾkrtʾk … na-krte, nak(s)te, nakarte (nʾkrtʾy, nʾkrtk) — silver (not coined)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 5756-5763, printed p.231 (SOD_pages.txt lines 20207-20250)\", \"stance\": \"supports\", \"note\": \"'nʾkrtʾk … na-krte, nak(s)te, nakarte (nʾkrtʾy, nʾkrtk) silver (not coined). VJ 85, 55d, 558, 618; BSTBL, Dhy. 259'; '5763 nʾkrtk-(w) B, S — na-krte, nak(ar)taku — silver'; '5762 nʾkrtkyʾwnc B — na-krte-yōnc — silvern'.\"},\n            {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to Borhan p.2157 (BQT vol. 4, pdf 240)\", \"stance\": \"supports\", \"note\": \"«در سغدی nʾkrtk (سیم) … و آن مرکب است از *nā (نه، نا) + krt (کرده)؛ و مراد نامسکوک است (از افادات شفاهی استاد بنونیست)» — Mo'in, on Benveniste's oral authority, gives exactly Nourai's segmentation nā + krta 'uncoined'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"noqreh «نقره»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Two derivations compete. (a) Nourai's, which is Mo'in's: NP نقره noqre 'silver' < Sogdian nʾkrtk *nā-krta 'unwrought, uncoined (metal)'; Mo'in states this in his footnote to Borhan-e Qate' p.2157, crediting Benveniste's oral communication, and cites Gharib's Sogdian entry. On this view the Arabic نُقْرَة nuqra 'ingot, piece of silver' is itself the Iranian word arabicised, and the Persian shape with -q- and the ta marbuta spelling ه would be the round-trip form (Sogdian > Arabic > Persian). (b) The view of Wiktionary and the Arabic lexica: نقره is simply borrowed from Arabic نُقْرَة, a normal derivative of the native root ن‑ق‑ر 'to hollow out, peck' (نُقْرَة 'cavity, hollow'; hence 'a hollowed lump of metal, ingot'), the sense 'silver' developing in Arabic and being taken into Persian. Note that neither Asbaghi (PLA) nor Addi Shir (AFM) lists نقرة among the Persian loanwords in Arabic, which weakens (a). The Sogdian etymon and the Persian word both exist and the semantics fit well ('uncoined silver' > 'silver'), but the transmission is unproven, so the arrow is plausible rather than confirmed.\",\n          \"derivation_fa\": \"دو ریشه‌شناسی در برابر یکدیگرند. الف) رأی نورایی که همان رأی معین است: «نقره» از سغدی nʾkrtk، یعنی *nā-krta «ناکرده، نامسکوک»؛ معین در حاشیهٔ برهان قاطع (ص ۲۱۵۷) این را به «افادات شفاهی استاد بنونیست» نسبت می‌دهد. بر این پایه، نُقْرَهٔ عربی خود معرّبِ همین واژهٔ ایرانی است و «نقره»ٔ فارسی صورت بازگشتی (سغدی › عربی › فارسی) خواهد بود. ب) رأی ویکی‌واژه و فرهنگ‌های عربی: «نقره» وام‌واژه‌ای است از نُقْرَهٔ عربی، مشتقِ عادیِ ریشهٔ ن‑ق‑ر «کندن، گود کردن» (نُقْرَه «گودی» › «شمشِ گودشده» › «سیم»). اصباغی و ادّی شیر نیز نُقْرَه را در شمار وام‌واژه‌های فارسی در عربی نیاورده‌اند، که رأی الف را سست می‌کند. هم واژهٔ سغدی و هم تحول معنایی «سیمِ نامسکوک › سیم» پذیرفتنی است، اما راه انتقال گواه قطعی ندارد؛ پس این بند با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%82%D8%B1%D9%87\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2157\", \"status\": \"supports\", \"note\": \"BQT vol. 4, pdf p.240 = printed 2157 (incoming/BQT/BQT_v4_pages.txt): headword «نقره: بضم اول، معروف است که بعربی فضه گویند»; Mo'in's footnote 7 reads «در سغدی nʾkrtk (سیم) … Gauthiot-Benveniste … و آن مرکب است از *nā (نه، نا) + krt (کرده)؛ و مراد نامسکوک است (از افادات شفاهی استاد بنونیست). در عربی معانی متعدد دارد از جمله «القطعة المذابة من الذهب والفضة» … ولی بمعنی سیم و سیم در معدن مستحدث است (دزی ج ۲)».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"Gharib nos. 5756/5763, printed p.231\", \"stance\": \"supports\", \"note\": \"'nʾkrtʾk … silver (not coined)' — the etymon exists with the required meaning.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen (incoming/PLA/PLA_pages.txt, grep نقرة / nuqra)\", \"stance\": \"silent\", \"note\": \"No entry for نقرة/nuqra: Asbaghi does not count the Arabic word as a Persian loan, so he offers no support for the round-trip route.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-Fārisiyya al-Muʿarraba (AFM_pages.txt, grep نقرة)\", \"stance\": \"silent\", \"note\": \"No نقرة headword; Addi Shir likewise does not treat it as an arabicised Persian word.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi\", \"stance\": \"partial\", \"note\": \"The lexicon volumes on disk tag نقره only as Arabic-mediated; Mo'in's Sogdian etymology is stated in the Borhan footnote (above), not in the Farhang entry.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Latin\",\n          \"words\": \"ne: not; ne-ŭllus: not any, null; ni-scîre: not knowing, silly; nek, neg: not; negâre: to negate, deny\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin kept both grades. Unstressed nē-/ne- appears in nĕ-fās, nĕ-sciō, nĕ-cesse, nĕ-uter, nūllus, nōn (< *ne oinom), neque; the stressed *nei gives nī (Old Latin nei). nūllus is a contraction of *ne + ūllus (diminutive of ūnus 'one'), so Nourai's 'ne-ūllus' is the correct segmentation (his ☞I 2 is the *oi-no- 'one' root). ni-scīre stands for nescīre / nescius 'not knowing, ignorant' — the ancestor of nice; Nourai writes ni- for nĕ-, a minor slip in the vowel. Italic *nek gives the prefix neg- (neglegere, negōtium 'nec-otium, no leisure') and the verb negāre 'to say no, deny'; Pokorny p.757 refers to 'lat. neg[āre, -ōtium]' under the same root, and Watkins has '6. Italic *nek, not, in: a. Latin prefix neg-: NEGLECT, NEGOTIATE; b. Latin negāre, to deny: NEGATE'.\",\n          \"derivation_fa\": \"لاتین هر دو درجهٔ ریشه را نگه داشته است: صورت بی‌تکیهٔ ne- در nĕ-fās، nĕ-sciō، nĕ-uter، nūllus، nōn (از *ne oinom) و neque؛ و صورت تکیه‌دارِ *nei در nī (لاتینِ کهن nei). nūllus ادغامِ *ne + ūllus (مصغّرِ ūnus «یک») است، پس تجزیهٔ نورایی درست است. صورت ni-scîre همان nescīre/nescius «نادان» است — نیای واژهٔ انگلیسی nice — که نورایی واکهٔ آن را ni- نوشته و این لغزشی کوچک است. از *nek ایتالیکی پیشوند neg- (neglegere، negōtium یعنی nec-otium «بی‌فراغت») و فعل negāre «نه گفتن، انکار کردن» برآمده است؛ پوکورنی (ص ۷۵۷) و واتکینز هر دو همین را زیر همان ریشه می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nice\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 73 s.v. 'ne': '2. Latin ne-, not, and nullus, none (ne- + ullus, any; see oi-no-): ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL …; 5. Latin non, not (< *ne-oinom …); 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negāre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE).'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p.757 (POK_02.txt leaf 418)\", \"stance\": \"supports\", \"note\": \"'lat. nĕ- in ne-fās, ne-sciō (ne-sciens, ne-scius), ne-cesse, ne-uter, n'unquam, nusquam, nūllus, nōn (*n'oinom) … ne-que \\\"und nicht\\\" …; vgl. auch lat. neg[āre, -ōtium] oben S. 418'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. null, nice, deny, negation, negative, neglect (KLN_1966.txt lines 25749, 25377, 10887, 25141-25147)\", \"stance\": \"supports\", \"note\": \"'null … fr. L. nūllus … contraction of *ne(c) oin(o)los … fr. neg. pref. ne- and dimin. of OL. oinos'; 'nice … fr. L. nescius, \\\"not knowing, ignorant\\\", fr. neg. part. ne- and the stem of scire'; 'deny … fr. L. denegare … fr. de- and negāre, \\\"to say no, to deny\\\"'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 319-320\", \"stance\": \"supports\", \"note\": \"Same Latin material under 'ne'/'nei' (lat. nī, altlat. nei; osk. nei 'nicht' (nei-p 'neque')).\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Arabic\",\n          \"words\": \"naker, n.k.r: to negate, deny, not recognize\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Arabic root ن‑ك‑ر (nakira 'to not know, fail to recognise, deny'; ankara 'to deny'; munkar, nakīr, nakira) is Common Semitic, not a Latin borrowing. Cognates: Akkadian nakāru 'to be strange, foreign, hostile, to be at war with', Ugaritic nkr, Hebrew נָכְרִי nokrī 'foreign, stranger' and hikkīr 'to recognise' / nikkēr 'to treat as foreign', Aramaic/Syriac nukrāyā 'stranger'. The semantic core is 'be foreign/other', from which both 'fail to recognise' and 'deny' follow; the resemblance to Latin negāre (Italic *nek + -āre) is accidental, since Latin neg- is a compound of the PIE negation with *k(ʷ)e and has no k-r sequence at all. There is no route by which a Latin verb could have supplied a triconsonantal Semitic root already attested in second-millennium-BCE Akkadian. Modern scholarship therefore rejects the arrow Latin > Arabic drawn here; the two are unrelated look-alikes.\",\n          \"derivation_fa\": \"ریشهٔ عربی ن‑ک‑ر (نَکِرَ «نشناختن، انکار کردن»، أنکر، مُنکَر، نکیر) ریشه‌ای سامیِ مشترک است و وام‌واژه‌ای از لاتین نیست. هم‌ریشه‌های آن: اکدی nakāru «بیگانه و دشمن بودن»، اوگاریتی nkr، عبری نُکْری «بیگانه» و هِکّیر «شناختن»، و آرامی/سریانی nukrāyā «بیگانه». هستهٔ معنایی «بیگانه بودن» است که از آن هم «نشناختن» و هم «انکار کردن» برآمده است. شباهت آن به negāre لاتین تصادفی است، زیرا neg- لاتین خود ترکیبِ ادات نفیِ هندواروپایی با *kʷe است و هیچ توالی k-r در آن نیست، و ریشهٔ سامیِ سه‌حرفی پیش از هزارهٔ دوم پیش از میلاد در اکدی گواه دارد. پژوهش امروزی این پیکان (لاتین › عربی) را رد می‌کند و این دو را همانندهای تصادفی می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%83%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"TAD:73\", \"status\": \"not_found\", \"note\": \"Tobia al-Unaysi's Tafsīr al-alfāẓ al-dākhila, printed p.73 (TAD_pages.txt leaf 69, page numeral '73' visible on the leaf) is in the ك section (كشك, كيلوغرام, كيموس, كيميا — Greek and Persian loanwords). Grepping the whole book for نكر / منكر / نكير finds no headword at all (only incidental occurrences at lines 32, 80, 123, 259), so TAD nowhere claims that نكر is a loanword.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966, grep 'nakir', 'munkar'\", \"stance\": \"silent\", \"note\": \"Klein has no entry for the Arabic root (it produced no English word), so he neither supports nor contradicts; his Latin negāre entry derives it wholly within Indo-European.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an (FVQ_pages.txt, grep نكر/munkar/nakir)\", \"stance\": \"silent\", \"note\": \"Jeffery does not list ن‑ك‑ر among the Qur'anic foreign words — i.e. he treats it as native Arabic, which cuts against a borrowing of any kind.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir (AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"No نكر headword among the arabicised Persian words.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"enkâr «انکار» (extra: مُنکر ، نکیر ، نکره)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The arrow itself (Arabic > Persian) is correct: NP انکار enkār is the Arabic verbal noun إنْكار inkār, the maṣdar of form IV أَنْكَرَ ankara 'to deny, disavow', from the root ن‑ك‑ر; it entered Persian with the rest of the Arabic religious-legal vocabulary after the 7th-8th c. and is fully naturalised (انکار کردن). The three extra forms on the printed page belong to the same stem: مُنکِر munker 'one who denies' (form IV active participle), نکیر Nakīr (with مُنکَر Munkar, the two angels who interrogate the dead — Islamic eschatology), and نکره nakre/nakera 'indefinite (grammar); unpleasant'. What makes the node less than confirmed is only its position in the chart: it hangs from node #15, so as drawn NP انکار is made a distant relative of Latin negāre, which modern scholarship denies (see #15). Take away that upstream link and the Arabic-to-Persian step is standard and uncontroversial.\",\n          \"derivation_fa\": \"خودِ پیکان (عربی › فارسی) درست است: «انکار» فارسی همان إنْکار عربی است، مصدرِ بابِ افعال از أنْکَرَ «انکار کردن» از ریشهٔ ن‑ک‑ر، که همراه با انبوهِ واژگان دینی و حقوقی عربی از سدهٔ اول و دوم هجری به فارسی آمده و کاملاً بومی شده است (انکار کردن). سه صورت افزودهٔ صفحهٔ چاپی نیز از همین ستاک‌اند: «مُنکِر» (اسم فاعل بابِ افعال)، «نکیر» (با «مُنکَر»، نام دو فرشتهٔ بازپرس در باورهای اسلامی) و «نکره» (در دستور، نامعیّن). تنها اشکال این بند جای آن در نمودار است: چون زیر بندِ عربی (شمارهٔ ۱۵) نشسته، «انکار» را خویشاوندِ دورِ negāre لاتین نشان می‌دهد و پژوهش امروزی این پیوند را رد می‌کند. با کنار گذاشتن آن حلقهٔ بالادست، گام «عربی › فارسی» بی‌هیچ اختلافی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%83%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:415\", \"status\": \"not_checked\", \"note\": \"S.M. Nahvi, Farhang-e Vāzhehā-ye ʿArabi dar Fārsi (1368/1989) — refs_online.json records 'no digital copy found on any permitted platform (re-searched 2026-09); catalogue record only' (OpenLibrary OL2012991M), so p.415 could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 (grep munkar/nakir)\", \"stance\": \"silent\", \"note\": \"No entry; the Arabic stem gave no English word.\"},\n            {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Fārsi (MON_part1.txt, انکار/انکاره region, line 18344)\", \"stance\": \"partial\", \"note\": \"The OCR has «انکاره … (ا.) پندار؛ وهم» (a different, native word) adjacent to the Arabic انکار entries; Mo'in tags the Arabic loans with [ع.], i.e. Arabic, with no Indo-European ancestry claimed.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery (FVQ_pages.txt)\", \"stance\": \"silent\", \"note\": \"ن‑ك‑ر is not listed among the Qur'an's foreign words, consistent with إنكار being an ordinary Arabic form IV maṣdar.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"null, nice, negative, neglect, negotiate, deny\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are Latin-derived, all six carry the *ne particle. null < Latin nūllus (< *ne + ūllus) via French nul, 15th c.; nice < Middle English nice 'foolish, ignorant' < Old French nice < Latin nescius 'not knowing' (ne- + scīre), the sense sliding through 'fastidious, precise' to 'agreeable' only by 1769; negative < Old French negatif < Latin negātīvus, from negāre; neglect < Latin neglectus, pp. of neglegere (neg- + legere 'to gather, heed'); negotiate < Latin negōtiārī, from negōtium 'business' = neg- + ōtium 'leisure', i.e. 'not-leisure'; deny < Middle English denien < Old French denier < Latin dēnegāre (dē- + negāre). Watkins names the same six words (NULL, NICE, NEGATIVE via NEGATE, NEGLECT, NEGOTIATE, DENY) under 'ne', and Klein and Skeat give the individual chains.\",\n          \"derivation_fa\": \"هر شش واژه از راه لاتین آمده‌اند و همه ادات نفیِ *ne را در خود دارند: null از nūllus لاتین (از *ne + ūllus) به واسطهٔ nul فرانسوی؛ nice از nice فرانسهٔ کهن و آن از nescius لاتین «نادان» (ne- + scīre) که معنایش از «نادان» به «سخت‌پسند، دقیق» و سرانجام در ۱۷۶۹ م. به «خوشایند» تحول یافته؛ negative از negātīvus لاتین (از negāre)؛ neglect از neglectus، اسم مفعولِ neglegere (neg- + legere «برچیدن، توجه کردن»)؛ negotiate از negōtium یعنی neg- + ōtium «فراغت»، پس «بی‌فراغتی، کار»؛ و deny از dēnegāre لاتین (dē- + negāre) به واسطهٔ denier فرانسهٔ کهن. واتکینز همین شش واژه را زیر مدخل ne می‌آورد و کلاین و اسکیت نیز زنجیرهٔ هر یک را تأیید می‌کنند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nice\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt leaf 73 s.v. 'ne': the English words listed for the Latin branches are 'ANNUL, NEFARIOUS, NESCIENCE, NEUTER, (NICE), NISI, NULL, NULLIFY' and 'NEGLECT, (NEGLIGEE), NEGOTIATE … NEGATE; ABNEGATE, DENY, RENEGADE' — Nourai's six words exactly.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. nice, null, negation/negative, neglect, deny (KLN_1966.txt lines 25377, 25749, 25141-25147, 10887)\", \"stance\": \"supports\", \"note\": \"'nice, adj. — ME., \\\"not wise, foolish, wanton\\\", fr. OF. nice … fr. L. nescius … fr. neg. part. ne- and the stem of scire'; 'negative … fr. L. negativus … fr. negatus, pp. of negare'; 'neglect, n. — L. neglectus … fr. neglegere, negligere'; 'deny … fr. L. denegare … fr. de- and negare'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Nice (SKT.txt line 12261)\", \"stance\": \"supports\", \"note\": \"'Nice … M.E. nice, foolish, simple, later … and lastly delicious. O.F. nice, simple: orig. ignorant. — L. nescius, ignorant. — L. ne, not; scire, know. See No (1) and Science.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. 'ne'\", \"stance\": \"supports\", \"note\": \"Same entry; '[Pok. ne 756]' ties the English words to the root box of this chart.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-351.json > /dev/null && echo \"JSON OK\"",
 "description": "Write verification JSON"
}
```


### [2026-09-07T18:39:55.910Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T18:39:59.202Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 tools/verify_check.py 351",
 "description": "Run verify_check for page 351"
}
```


### [2026-09-07T18:40:00.470Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'plausible': 6, 'confirmed': 10, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'partial': 3, 'not_found': 5, 'not_checked': 2}
books consulted: {'supports': 32, 'silent': 9, 'partial': 10} | by book: {'WLD': 6, 'KLN': 6, 'BRT': 5, 'MON': 5, 'KNT': 4, 'AHD': 4, 'PHD': 4, 'BQT': 3, 'POK': 3, 'HUB': 2, 'SKT': 2, 'SOD': 2, 'AFM': 2, 'FVQ': 2, 'PLA': 1}
```


## [2026-09-07T18:40:21.998Z] AGENT

Verification complete — 0 PROBLEM lines.

**Page 351 (book p. 321) — root `Ne 1, Nei 3, An 4` (PIE \*ne "not"), 1 entry + 17 nodes; 3 redirect entries skipped.**

Verdicts: root **confirmed**; nodes **10 confirmed / 6 plausible / 1 disputed**.
Ref checks of Nourai's own citations: 14 supports, 3 partial, 5 not_found, 2 not_checked. Books consulted: POK, WLD (Bd. II 319-321), AHD/Watkins, KNT, BRT, PHD, NYB-area, HUB, KLN, SKT, SOD (Gharib), BQT vols 1/2/4, MON, PLA, AFM, FVQ.

Disputed:
- **#15 Arabic `naker, n.k.r` ← Latin `negāre`** — ن‑ك‑ر is Common Semitic (Akkadian *nakāru*, Ugaritic nkr, Hebrew *nokrī*), attested long before any Latin contact; the resemblance to Latin neg- (PIE \*ne + \*kʷe) is accidental. Nourai's own reference TAD:73 is the ك section and TAD has no نكر headword at all.

Plausible (each explained in the file):
- #1/#2 `ni-us-tavah` → نستوه: the negative element is right, but the Avestan compound is unattested; Mo'in (Farhang + Borhan p.2138) analyses نستوه as نه + ستوه. Also "ni" as an Avestan/OP negation is a slip (that form is Germanic/Baltic).
- #6/#7 `â-zarema-dugedâ` → آزرمیدخت: unattested compound; Mo'in's Borhan footnote p.36 gives exactly Nourai's a-privative + "aging" analysis, but the prevailing reading is MP *āzarm* "respect" + *duxt*. The other three words in each node are confirmed (BRT an-āhita-, an-aoša-, KNT axšaina-).
- #13 نقره ← Sogdian nʾkrtk: Mo'in/Benveniste support it (BQT:2157 verbatim), but Wiktionary and the Arabic lexica derive it from Arabic نُقْرَة, and neither Asbaghi nor Addi Shir counts it a Persian loan.
- #16 انکار: the Arabic→Persian step is standard; only the upstream Latin link is wrong.

Wrong/unusable page citations by Nourai (no data fix needed, book-side):
- `BQT:788` (#6) → p.788 is خوره; the right page for خشن/خشین is **755**.
- `BQT:46` (#8) → p.46 is آشنا/آشور; nothing relevant.
- `SOD:32` (#12) → nʾkrtk is entries 5756/5763, printed **p.231**.
- `KNT:209` (#4) → local Kent OCR ends at p.207; the word is Middle Persian anyway.
- `POK:594` (#8) is inside keu- "swell/hollow"; Pokorny's keuk- "to shine" is p.597.
- `FVA:415` (#16) — no digital copy exists (catalogue record only).

Extraction accuracy: I compared the JSON against the printed page (`site/pages/351.jpg`) — **no extraction errors**. One note for the owner: the printed page has a blank rectangle to the right of node #8 (an empty box with an arrow into it); it is empty in the book, so nothing is missing from the JSON.
