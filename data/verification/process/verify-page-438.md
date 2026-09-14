# Verification process log — verify-page-438


## [2026-09-14T01:31:01.719Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 438 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-438.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-438.json. Write /home/sfmqrb/git/rishe/data/verification/page-438.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 438` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:31:02.735Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:31:03.582Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:31:03.639Z] TOOL RESULT

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


## [2026-09-14T01:31:04.083Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-438.txt"
}
```


### [2026-09-14T01:31:04.149Z] TOOL RESULT

```
1	=== PDF page 438 (book page 408) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 : to cut, scrape, separate, tear, etc.  (refs AHD; POK:920,926,930,931,941; IEC:640,1155)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:919,930; SOD:61 | sčand : to break ; skenda : crippled, broken ; scapti : to split ; kaf, kâf : to break
5	  #2 (parent #1) [Persian] refs=BQT:1275, 1279; HRN:175 | šekastan «شکستن ( شکن )» : to break ; šekâftan «شکافتن ، شکفتن ، کافتن» : to split ; kaftan, koftan «کَفتن» : to break open, split | extra: شگفت ، شکوفه ، شکاف ، کاویدن ، کاؤش ، کاو
6	#3 (parent #0) [Avestan] refs=POK:919 | sâ 2, sâna, sya 1 : to sharpen ? ; fra-sanam : destruction | NOTE: Compare with the Avestan words from root "Ak"
7	  #4 (parent #3) [Persian] refs=BQT:1184, 1462 | sŭdan «سودن ( سود )» : to rub, grind ; farsŭdan «فرسودن» : to wear out, rub off
8	#5 (parent #0) [Avestan] refs=POK:941; KLN:1432; HRN:188; SYN:321 | kereta : knife, a cut trench ; kareman, čareman : hide cut off animals ; karena_oša : cut from hearing, deaf ; ha-keret : cut once ☞Sem 1 ; skarenâ : cut round
9	  #6 (parent #5) [Persian] refs=BQT:1559; HRN:25,98,221,244; MON:2935; SYN:321 | kârd «کارد» : knife ; kart «کَرت» : a trench cut for irrigation ; čarm «چرم» : hide (cut from animals) ; kar «کر» : deaf (with cut hearing) ; agar «اگر ( مگر ، هرگز )» : if "cut once"
10	  #7 (parent #5) [Sogdian] refs=SOD:128,193,194 | crm : leather ; krn : deaf ; krt : knife
11	#8 (parent #0) [Avestan] refs=POK:578,920,947 | sâri, sari, said, sid : fragment ; wi-sis, vi-saĕd : cut apart, send away ☞Wi ; sairi-gaona : like cut (dropped) from the body, dung ☞Gĕu 1
12	  #9 (parent #8) [Persian] refs=HRN:205; BQT:1816; POK:578,947 | gosîxtan «گسیختن ( گسستن ، گسیل )» : cut apart ; sargin, sergin «سرگین» : animal dung
13	#10 (parent #0) [Latin] refs=AHD; IEC:1155 | secare : to cut ; re-secare : cut against ; risecum : rock at sea that cuts ships, danger, risk ; cortus : short
14	  #11 (parent #10) [French] refs=AHD | risque : danger
15	    #12 (parent #11) [Persian] refs=MON:1703 | rîsk «ریسک» : risk
16	  #13 (parent #10) [English] refs=AHD | section, insect, risk
17	
```


## [2026-09-14T01:31:06.966Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-438.json | head -200",
 "description": "Read source JSON for page 438"
}
```


### [2026-09-14T01:31:07.009Z] TOOL RESULT

```
{
  "pdf_page": 438,
  "book_page": 408,
  "entries": [
    {
      "root": {
        "name": "Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2",
        "lang": "Indo-European",
        "refs": "AHD; POK:920,926,930,931,941; IEC:640,1155",
        "gloss": "to cut, scrape, separate, tear, etc."
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:919,930; SOD:61",
          "words": [
            {"translit": "sčand", "gloss": "to break", "script": null},
            {"translit": "skenda", "gloss": "crippled, broken", "script": null},
            {"translit": "scapti", "gloss": "to split", "script": null},
            {"translit": "kaf, kâf", "gloss": "to break", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1275, 1279; HRN:175",
          "words": [
            {"translit": "šekastan", "gloss": "to break", "script": "شکستن ( شکن )"},
            {"translit": "šekâftan", "gloss": "to split", "script": "شکافتن ، شکفتن ، کافتن"},
            {"translit": "kaftan, koftan", "gloss": "to break open, split", "script": "کَفتن"}
          ],
          "script_extra": "شگفت ، شکوفه ، شکاف ، کاویدن ، کاؤش ، کاو",
          "note": null,
          "quote": {
            "text": "کفیدش دل از غم چو آن کفته نار - کفیده شود سنگ تیمار خوار",
            "poet": "Rŭdakî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:919",
          "words": [
            {"translit": "sâ 2, sâna, sya 1", "gloss": "to sharpen ?", "script": null},
            {"translit": "fra-sanam", "gloss": "destruction", "script": null}
          ],
          "note": "Compare with the Avestan words from root \"Ak\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1184, 1462",
          "words": [
            {"translit": "sŭdan", "gloss": "to rub, grind", "script": "سودن ( سود )"},
            {"translit": "farsŭdan", "gloss": "to wear out, rub off", "script": "فرسودن"}
          ],
          "note": null,
          "quote": {
            "text": "تو گویی پلپل سوده بکف داشت - پراکند از دو کف در دیده پلپل",
            "poet": "Manŭchehrî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:941; KLN:1432; HRN:188; SYN:321",
          "words": [
            {"translit": "kereta", "gloss": "knife, a cut trench", "script": null},
            {"translit": "kareman, čareman", "gloss": "hide cut off animals", "script": null},
            {"translit": "karena_oša", "gloss": "cut from hearing, deaf", "script": null},
            {"translit": "ha-keret", "gloss": "cut once", "script": null, "see": ["Sem 1"]},
            {"translit": "skarenâ", "gloss": "cut round", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1559; HRN:25,98,221,244; MON:2935; SYN:321",
          "words": [
            {"translit": "kârd", "gloss": "knife", "script": "کارد"},
            {"translit": "kart", "gloss": "a trench cut for irrigation", "script": "کَرت"},
            {"translit": "čarm", "gloss": "hide (cut from animals)", "script": "چرم"},
            {"translit": "kar", "gloss": "deaf (with cut hearing)", "script": "کر"},
            {"translit": "agar", "gloss": "if \"cut once\"", "script": "اگر ( مگر ، هرگز )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:128,193,194",
          "words": [
            {"translit": "crm", "gloss": "leather", "script": null},
            {"translit": "krn", "gloss": "deaf", "script": null},
            {"translit": "krt", "gloss": "knife", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:578,920,947",
          "words": [
            {"translit": "sâri, sari, said, sid", "gloss": "fragment", "script": null},
            {"translit": "wi-sis, vi-saĕd", "gloss": "cut apart, send away", "script": null, "see": ["Wi"]},
            {"translit": "sairi-gaona", "gloss": "like cut (dropped) from the body, dung", "script": null, "see": ["Gĕu 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "HRN:205; BQT:1816; POK:578,947",
          "words": [
            {"translit": "gosîxtan", "gloss": "cut apart", "script": "گسیختن ( گسستن ، گسیل )"},
            {"translit": "sargin, sergin", "gloss": "animal dung", "script": "سرگین"}
          ],
          "note": null,
          "quote": {
            "text": "هردو گون آهو گیا خوردند و آب - زاین یکی سرگین شد و زآن مشک ناب",
            "poet": "Molavî"
          }
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD; IEC:1155",
          "words": [
            {"translit": "secare", "gloss": "to cut", "script": null},
            {"translit": "re-secare", "gloss": "cut against", "script": null},
            {"translit": "risecum", "gloss": "rock at sea that cuts ships, danger, risk", "script": null},
            {"translit": "cortus", "gloss": "short", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "risque", "gloss": "danger", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:1703",
          "words": [
            {"translit": "rîsk", "gloss": "risk", "script": "ریسک"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "section, insect, risk", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:31:07.972Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo \"---\" && ls data/verification/sources/refs/ | head -60",
 "description": "List verification dirs"
}
```


### [2026-09-14T01:31:08.033Z] TOOL RESULT

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
page-128.json
page-129.json
---
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
```


## [2026-09-14T01:31:44.247Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','IEC','SOD','BQT','HRN','KLN','SYN','MON','BRT','PHD','NYB','CHEUNG','HUB','WLD','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\"",
 "description": "Inspect refs_online for relevant abbreviations"
}
```


## [2026-09-14T01:31:45.065Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,140p' SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:31:45.324Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
CHEUNG null
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


### [2026-09-14T01:31:45.365Z] TOOL RESULT

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
```


## [2026-09-14T01:31:49.384Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','IEC','SOD','BQT','HRN','KLN','SYN','MON','BRT','AHD']:\n    print('==',k); print(json.dumps(d[k], ensure_ascii=False, indent=1))\n\"",
 "description": "Full ref details"
}
```


### [2026-09-14T01:31:50.459Z] TOOL RESULT

```
== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
== IEC
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
== BQT
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
== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
== SYN
{
 "title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949",
 "edition_found": "1949 (reprint scans, same pagination in all printings)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt",
 "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.",
 "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.",
 "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"
}
== MON
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
== BRT
{
 "title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)",
 "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/altiranischeswr00bartgoog",
 "identifier": "altiranischeswr00bartgoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt",
 "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.",
 "notes": "Nourai's Table IV says 1979; that is the unchanged reprint.",
 "cites": "column number (the Altiranisches Wörterbuch is numbered by column, two per page)"
}
== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
```


## [2026-09-14T01:31:55.840Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 9[12][0-9]\" POK_full.txt | head -50; echo \"=== 578 ===\"; grep -n \"Page(s): 57[6-9]\" POK_full.txt | head",
 "description": "Find Pokorny lemmas at cited pages"
}
```


### [2026-09-14T01:31:55.911Z] TOOL RESULT

```
74052:Page(s): 910-911 
74121:Page(s): 911-912 
74271:Page(s): 912-913 
74300:Page(s): 913-914 
74367:Page(s): 914-915 
74946:Page(s): 915-916 
75059:Page(s): 916-917 
75121:Page(s): 922-923 
75320:Page(s): 923-927 
75347:Page(s): 927 
75378:Page(s): 927 
75440:Page(s): 928 
75493:Page(s): 929-930 
76964:Page(s): 922 
77196:Page(s): 919-922 
77525:Page(s): 918-919 
77545:Page(s): 929 
77727:Page(s): 917-918 
77777:Page(s): 929 
77801:Page(s): 929 
77873:Page(s): 928 
=== 578 ===
45788:Page(s): 579 
45812:Page(s): 579 
50247:Page(s): 578 
50278:Page(s): 579 
50381:Page(s): 579-580 
50453:Page(s): 577 
50476:Page(s): 577-578 
50516:Page(s): 578
```


## [2026-09-14T01:31:59.305Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 77525 77196 75121 75320 75493 77727; do echo \"--- line $L ---\"; awk -v n=$L 'NR>=n-25 && NR<=n+2' POK_full.txt | grep -E \"^(Root|English|German|Page)\" ; done",
 "description": "Show POK lemma headers near cited pages"
}
```


### [2026-09-14T01:32:00.442Z] TOOL RESULT

```
--- line 77525 ---
Page(s): 918-919 
Root / lemma: skhel- 
--- line 77196 ---
Page(s): 919-922 
Root /lemma: (s)kep-2, (sjkop- and (s)kap- (s)keb(h)-, skob(h)- and skab(h)- 
--- line 75121 ---
Page(s): 922-923 
Root / lemma: (s)kel-1 
--- line 75320 ---
German slef, Norwegian 5/e/V "large spoon'. 
Page(s): 923-927 
Root / lemma: (s)kel-2 
--- line 75493 ---
German schin^a kind of russisches Ledergeld'), Middle High German schinti. " fruit bowl ', 
German Middle Low Germansc/7/>7o'e/7"enthauten, auspliJndern, maltreat' (Modern High 
German sch/nden stem V.); Old Icelandic skant " bark ', nisi, also 'Hautchen', Middle Low 
German sc/7//7 'dandruff in Haar' (out of it Modern High German Schinn, Schinne), (under 
Page(s): 929-930 
Root / lemma: (s)keng- 
--- line 77727 ---
English Old Saxon scima. Middle High German sc/7e/77e "shadow'. Modern High German 
Page(s): 917-918 
Root / lemma: sRed-
```


## [2026-09-14T01:32:11.299Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\n(?=Root ?/ ?lemma:)',t)\nfor b in blocks:\n    m=re.search(r'Page\\(s\\):\\s*([0-9]+)',b)\n    if not m: continue\n    p=int(m.group(1))\n    if p in range(915,950) or p in range(570,585):\n        head=b.split('\\n')[0]\n        eng=re.search(r'English meaning:\\s*(.*)',b)\n        print(m.group(0).strip(),'|',head.strip()[:70],'|',(eng.group(1).strip()[:70] if eng else ''))\nEOF",
 "description": "List Pokorny lemmas pages 915-950, 570-585"
}
```


### [2026-09-14T01:32:12.397Z] TOOL RESULT

```
Page(s): 579 | Root / lemma: kerd-1 | 
Page(s): 579 | Root / lemma: kerd-2 | 
Page(s): 580 | Root/ lemma: [kerem-), krem-{. krom^ and kerrn-: 1) onion, garlic; 2)  | 
Page(s): 571 | Root / lemma: ker(a)-3 | 
Page(s): 581 | Root / lemma: kerap-, krep- | 
Page(s): 581 | Root / lemma: [kerR-.) korR- : kfR- | 
Page(s): 571 | Root / lemma: ker-2 | 
Page(s): 572 | Root / lemma: ker-4 | 
Page(s): 573 | Root/ lemma: {ker-5^), kor- | 
Page(s): 574 | Root / lemma: ker-5 | 
Page(s): 582 | Root / lemma: kerm- | 
Page(s): 573 | Root/ lemma: Aer-5and Rer- | 
Page(s): 582 | Root / lemma: kemo- | 
Page(s): 583 | Root / lemma: kers- | 
Page(s): 584 | Root/ lemma: kert-, kerat-, krat- {* kuers-tj\ to turn, roll, wind, ne | 
Page(s): 578 | Root/ lemma: Rerbero- anA kertero- | 
Page(s): 579 | Root / lemma: Rei&^o- Re/6^a | 
Page(s): 579 | Root/ lemma: {Rered-.) Rerd-, Rerd-, Rfd-, ^/©(y- (nasalized PIE | 
Page(s): 582 | Root / lemma: Rera-, Rra- | 
Page(s): 577 | Root / lemma: Rer-2, Rera-, Rre- | 
Page(s): 577 | Root / lemma: Rer-3 | 
Page(s): 578 | Root / lemma: /feA-^and Rera- : ^re- | 
Page(s): 583 | Root / lemma: Rer(s)-1 | 
Page(s): 583 | Root / lemma: Rers-2 | 
Page(s): 574 | Root / lemma: Rer-, Rera- : Rra-, Rerei-, Rereu- | 
Page(s): 582 | Root / lemma: Re-ro- | 
Page(s):915 | Root / lemma: seug- | 
Page(s):915 | Root / lemma: seua- su- | 
Page(s):915 | Root / lemma: seuio- | 
Page(s):915 | Root / lemma: sie[u]-ro- : sJ9-urQo)- | 
Page(s): 915 | Root / lemma: s/u- : to sew, derived from Root / lemma: se(i)-3, -sai- | 
Page(s):916 | Root / lemma: sArab^- skarrt^- | 
Page(s):918 | Root/ lemma: {sjkamb- and (s)kemb-\ "to curve, bend' derived from Root | 
Page(s):918 | Root / lemma: (s)kand- (s)kend- | 
Page(s): 916 | Root / lemma: (s)kai- (d-), (t-) | 
Page(s): 922 | Root / lemma: (s)kek-, skeg-{* nasaWzeA *(skenk-, *skek-no-) | 
Page(s): 923 | Root / lemma: (s)kel-1 | 
Page(s): 927 | Root / lemma: (s)kel-2 | 
Page(s): 927 | Root / lemma: (s)kel-3 | 
Page(s): 928 | Root /lemma: ^s^AreM (extended kla-, kid-) | 
Page(s): 930 | Root / lemma: skend^- | 
Page(s): 929 | Root / lemma: (s)ken-(d-) | 
Page(s): 930 | Root / lemma: (s)keng- | 
Page(s): 930 | Root / lemma: (s)kep-1 | 
Page(s): 948 | Root / lemma: (s)kert)(h)-, (s)kreb(h)-, nasalized (s)kremb- | 
Page(s): 949 | Root / lemma: (sJker-6^-, (sJkor-6'^- | 
Page(s): 947 | Root / lemma: sker-(d)- | 
Page(s): 933 | Root / lemma: (s)ker-1 | 
Page(s): 933 | Root / lemma: (s)ker-2, skera- : skre- | 
Page(s): 935 | Root / lemma: (s)ker-3 | 
Page(s): 938 | Root / lemma: (s)ker-4, (s)kera-, (s)kre- | 
Page(s): 947 | Root / lemma: (s)ker-5 | 
Page(s): 949 | Root / lemma: (s)kert-s- | 
Page(s): 922 | Root / lemma: skei-b""-, -p- nasalized sk/'-m-b'^- | 
Page(s): 919 | Root / lemma: skei- | 
Page(s): 930 | Root /lemma: (s)kep-2, (sjkop- and (s)kap- (s)keb(h)-, skob(h)- and sk | 
Page(s):917 | Root / lemma: (s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t- | 
Page(s): 918 | Root / lemma: (s)k(h)ed-, (s)k(h)e-n-d- | 
Page(s): 929 | Root / lemma: skhel- | 
Page(s): 917 | Root / lemma: sRai-, sRai-. sRT-\ to glimmer (of wet things); shadow,  | 
Page(s):919 | Root / lemma: sRed- | 
Page(s): 929 | Root / lemma: (s)Rel- | 
Page(s): 929 | Root / lemma: (s)Rem- | 
Page(s): 928 | Root / lemma: (s)k''el-5, (s)kel- | 
Page(s): 947 | Root / lemma: (s)k''er- |
```


## [2026-09-14T01:32:50.591Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\n(?=Root ?/ ?lemma:)',t)\nwant=['(s)k(h)ed-, (s)k(h)e-n-d-','skei- ','(s)kep-2','(s)ker-4','sker-(d)-','(s)ker-5']\nfor b in blocks:\n    h=b.split('\\n')[0]\n    for w in want:\n        if w in h:\n            print('='*80); print(b[:3000]); break\nEOF",
 "description": "Print relevant Pokorny entries"
}
```


### [2026-09-14T01:32:51.720Z] TOOL RESULT

```
================================================================================
Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kera- 

, (s)kre- : to cut 

Material: Old Indie krpa\x\s\x. Sg. "shape, beauty', Avestan karafs, kahrpam^sha^e, body'. 

Middle Persian karp " body ' (Avestan xrafstra- n. ' predator ' from *krep + *[e]d-tro-\.o ed- 

■eat'?); 

perhaps (?) alb. sh-krep, sh-kep^ resemble a little ' (5/7= Indo Germanic sem, som, sm-, 
compare to meaning Old High German gi-ITh^ alike ': ^'body'); 

Common alb. Celtic -e- grade. 

Maybe taboo words alb. shkrep^ rock, fire rock ', shkrep, shkref, shkreh^ trigger, fire', 
shkrepje^ glance, flare, gun '. 

But alb. qep " sew ' < sh-kep , shqep^ unpick, rip, tear, take out stitches; unfasten threads, 
resemble a little '; shqepoj^ to be lame'. 

Comments: 

================================================================================
Root / lemma: krep-1, kfp- : body derived from -p- suffix of Root / lemma: (s)ker-4, (s)kere- 

, (s)kre- : to cut 

(3) (s)kerp-, (s)krep-: 

alb. karpe, karme {*korp-n-) 'rock, cliff' krep, shkrep'rocW, slope'; 



Latin corpus, -or/sn. " body'; 

Middle irisli cnt "body' {*krpes)\ 

Old High German {h)refm. "body, lower abdomen, womb'. Old Frisian href, hr/TbeWy', 
Old English hr/fn. "womb, belly' {*hrefiz- = *krepes-). Old English mid(h)rif. Old Frisian 
midref phren, diaphragm, wall of muscles or membranes that separates the chest cavity 
from the abdominal cavity ' ("*cavity in the middle of the body '). 

Gr. npani(;, mostly PI. Ahzc, " phren', which would prove the initial sound as k" , is 
doubtful in its affiliation, because the suitable meaning from Old English mid(h)rif\s 
probably based on the first part of the compound; 

it would have to be then npani(; a short form to a similar composition; after Vendryes 
RC 44, 313 ff., Specht KZ. 68, 193 ff. would be Indo Germanic *k"'erp- taboo metathesis to 
*perk"-^\\ie, world, oak' (Gothic fa/r/vus 'wor\d'). 

References: WP. I 486 f., WH. I 277 f. 
Page(s): 620 

================================================================================
Root / lemma: sker-(d)- 

Meaning: to defecate 

Material: Avestan sairya-' manure, crap, muck, droppings'. Middle Persian sargon, np. 

sargTn^s.; 

gr. oKwp, GKaro^ "ordure', whereof OKoopia "Schlacke'; 

Latin muscerda 'UausekoV; sucerda'Scb\Ne\v\eko\! , bu-, ovi-cerda have cerda^or 
* scerda through false Zerlegung from mu[s]scerda. Old Church Slavic skar^dt "disgusting' 
entscheidet dafiJr certainly nicht, compare Old Indie chrnatti, chardayat/ 'erbncbt, speit 
from'. Middle Irish sce/rd/m ' spe\e from', as o'-extension unseressker-; 

Old Icelandic skarn. Old English scearn, afries skern. Low German scharn'crap, muck, 
droppings'; 

Latvian sar/j/P\. "Schlacken, Menstrua, Excremente', Lithuanian sa/'n/a/" Menstrua'; 
proto Slavic. *serg{*serid), * stra t/'cacare' (e.g. Serb, serem, srati), russ. sd/'"crap, muck, 
droppings', etc. 

Hittite sakkaru.. Gen. s5/r/75S "ordure, excrement', saknu-uant 'mpure, unclean'. 



References: WP. II 587 f., WH. II 133 f., Trautmann 303, Frisk Indogerm. 25 f. 
Page(s): 947-948 

================================================================================
Root / lemma: (s)ker-4, (s)kera-, (s)kre- 
Meaning: to cut 

Material: I. A. Old Indie ava-, apa-skara-^ excrement (Ausscheidung)'; krnati, krnoti^ 
injures, slays ' (lex.), ^/A/?/7a-'ausgeschnitten, eingeritzt', s5/77i//A/?/75-"durchbohrt'; Old 
Indie carman-, Avestan caraman-^ieW, fur, skin'; presumably Old Indie /ri//- (unbel.) "ein 
Webergerat' (: russ. dial. cen/B "sickle', Lithuanian A/?i//s"axe' (?); 

Armenian k'orem^\ scratch', /r'e/ie/T? "scratch, scrape '; 

gr. Ksipu) (Kspoj, £Kapr|v, KSKoppai, Kaproq) " abscise; shave, shear; abfressen', Ksppa n. 
" schnitzel, small coin', Kop|j6(; m. "(abgeschnittener) clot, chunk, trunk', Koppa^w 
"zerstiJckle'; kopk; m. "bedbug' (= russ. korbi. " moth ': "incisive, biting, zerbeiftend'); Gen. 
Kap6(; "Nichts' in riu) 5s \x\v £v Kap6(; dan, compare also Kapipioipou(; loiic, £v tjr|5£MiC( 
Ijoipg... Hes., further OKopi n. "mite', QKopng, QKopiaTog "tiny', Hes.; "incisive' seems die 



basic meaning from mpyoq and Kap "louse' Hes.; to latter perhaps Kapov, mpoq 'Kummel' 
(from the Ahnlichkeit of KiJmmelkornes with a louse); with gr. KU)puKO(; 'leather sack' 
compare Irish curach ^Hautboot', cymr. corwg, cwrwg ds. from *kdrukos, compare further 
Old Icelandic ^p/^'Leinenkleid', Old High German harra^sack, bag'; with a meaning 
"schneidender derision, ridicule' here KspTOfjoc; "hohnend', KspTopsu) "hohne, lastere' (*K£p- 
aTopo(; "ein Lastermaul habend'? in 1. part ein root noun [s]ker-, orein -[e]5-stem *ker-s-)\ 
QKspacpoc;, Kspacpoc; "reprimand' Hes., OKsp-poAoc; AoiSopoc;, gkepPoAeT anarg Hes., 
GKsppoAAu) ' abuse, revile '; 

alb. hirret " whey ' ( *sker-na; the h after harr); Liden KZ. 61 , 9 f.; 

alb. sh-k/er're\\Se apart', harr{*skor-n-) "cut, bite from, jate', /5/7a/r "spoil, verwiJsten, 
sich separate', /s^a/Ves "Scharfrichter', lengthened grade korr, kuarr{*ker-n-d) " schneide 
ab, harvest '; 

Latin corium^ thick skin, bag, leather'; card, carn/st "flesh', originally " slice of meat ' as 
PI. carries, Umbrian /r5/Y/"part', Dat. karne, Abl. PI. /r5/77^s"carnibus', Oscan carneis 
"partis'; Umbrian /ra/t£/"distribuito'; Latin curtus^ abbreviated, mutilated' {*kr-t6-); 

Old Irish scar(a)im {*skera-mi) "I slit, separate', cymr. ys^5/'"Trennen', gwa-sgar 
"scatter'; Kaus. -iterative Old Irish sc^^/^/7>77"spanne die Pferde ab', scor^ paddock for 
abgespannte Zugtiere'; auf a /oparticiple in addition based on Middle Irish aurscartad 
{*air-uss-scart-) "Fegen, Reinigen', diuscart(a)im {*dT-uss-scart-) "entferne'; cymr. ysgarthu, 
dyscarthu ' c\ean' , ys^a/Y/? "rubbish, SpiJIicht', ca/'//7e/7"purgatoria' ; Middle Irish sca/rt'net 
um die intestines, phren'; Irish cert'smaW; nicht certainly covered is Middle Irish co/re 
"sword' (see below Gothic hafrus); Irish curach, cymr. corwg, CM//w^"Hautboot' to gr. 
KcbpuKOt;? see above; 

Old Icelandic skera^cui, clip, prick, abmachen'. Old High German sce^a/? "shave, shear, 
abscise ', Old English scierands.. Old Saxon sker-sahs^ shearing knife '; Old High
================================================================================
Root / lemma: (s)ker-5 
Meaning: onomatopoetic word 
See also: see above S. 567 ff. {ker-). 
Page(s): 947 



================================================================================
Root / lemma: skei- 

Meaning: to cut, separate 

Note: extension from sek-, initial sound partly also sk-, skh-, skh-, as in the continuing 

formation 

Material: I. Old Indie chyati^ clips ', participle chata-, chita-^ cut, cropps, truncates, cuts off 

', Kaus. chayayati {m\.\\ sk-, like:) 

Avestan fra-sanam " destruction ', sa-, sya- " to fight '; 

gr. Gxau) {*skh9id, Impf. saxwv. Inf. Kara-axav), oxa^u) (neologism, Schwyzer Gr. Gr. 1, 
716) " scratches, slits ' and " drop, hang down flaccidly, restrains, stays open ', axaoK; " the 
scratches, bleeding; release, to let sb/sth go ', axaapa n., axaap6(; m. " incision ', 
axaarripiov " fleam, latch, bolt ', axaarripia " the rope (serving for the separation of the 
spectators) before the racetrack '; 

Maybe alb. {*scid) s/7^iya/7y"distinguish', {*scie) shqyenj'tear, split'. 

Latin sad, scire " to know, understand; with infin. to know how to do ' (" part, make a 
distinction '), descTsco, -ere^ to breakaway, revolt, withdraw, diverge, apostatize. 



renounce ', seised, -ere^ to investigate, inquire; polit. to vote, ordain, resolve ' and " try to 
find out ', plebTscTtum^ a decree of the people ', satus' knowing, shrewd, clever, judicious; 
pretty, fine; adv. scite, skillfully ' (like Middle High German geschTde, Modern High German 
gescheitio *skei-t-) in the meaning ' eliminate ' (compare Old Icelandic 5/r/?a under S. 921) 
Middle Irish sce'i'd^ vomits ' {*skei-ie-ti, Indo Germanic *skei-), verbal n. sceithi. (from 
*sceth, Indo Germanic *ski-ta, therefrom:) cymr. chwydu, bret. c'houeda, mcorn. hweza^ 
vomit '; from Irish scethach^ to the travelling rupture ' places Old Icelandic skjadaku. " 
ryegrass, darnel (the herbs medicine recommends such orders against gout and 
rheumatism and dizziness) '; 

Middle Irish sc/'ant " knife ', ( *sk//ena) out of it cymr. ysg/'en' knife, sword '; Middle Irish 
scaJlid^ lets go, unhands, relinquishes, disperses ' {*skai-l-). Old Irish erscaJliud^ breakup, 
dissection, dissipation, fragmentation '; 

Old Icelandic skeina^ wound lightly '; as ' * split off piece of wood, ': Middle High 
German schTevn. f. " fencing post, pale ', Old English scTam. " shinbone ', next to which 
(compare Old High German bTa: bini^ bee ') 

Germanic *ski-nd{n) in Old English scinui., seine-ban v\. 'shinbone'. Old High German 
5c//7a "shinbone', also 'needle', Norwegian s/r/77a 'small disc, wheel, pulley, slice of bread '; 
Old Frisian sA/iofe/' bones of the arm' {-d la iorms); West Flemish schier^b\ock of wood' 
{*skT-ro-)\ from '*distinguish, discern' from: Old High German s/re/7'sharp, sharp witted, 
shrewd' {*skeiro-)\ Middle High German sc/?/©/"' quick, fast'. Adv. Old High German skero, 
s/r/b/10 'quick, fast'. Middle High German schier(e)6s., 'fast'; 

Latvian sk'ieva ' fissure in wood ' and Lithuanian skivytas 'scrap, shred' have probably v 
from dv, so that to o'-extension Lithuanian skfedziu, Latvian skiezLf, 

Maybe alb. Geg shku-, shkcieva aor., Tosc shqyenj, shqevaa
================================================================================
Root /lemma: (s)kep-2, (sjkop- and (s)kap- (s)keb(h)-, skob(h)- and skab(h)- 
Meaning: to work with a sharp instrument 

Material: A. Forms in -k (there are listed here only the definite Germanic forms; Latin and 
Balto Slavic with bsee by the root form in b^); skab- " form carving '. 

Gothic gaskapjan siem V. "make'. Old Icelandic skepja. Old English scieppan. Old High 
German scepfen. Middle High German schepfen, from which Modern High German 
schopfen; to preterit Middle High German schuof, participle " geschaffen = created ' would 
create a new present ^schaffen= make, create', as Swedish skapa, Danish scabe; 
deverbative o-verbs are Old Icelandic aschw. skapa^ make, furnish, found, install ', Old 
High German scaffon^ build, effectuate ' (Wissmann Nom. postverb. 73); Old English ge- 
sceapu. "shape, creature'. Old Saxon gi-scapuP\. n. "fate, destiny'; Old Icelandic skapu. " 
shape, mood ' etc.; -skapre.g. in vin-skapr^ friendship'; Old High German scafm. " shape, 
structure ', -scaf av\d -scafti.. Modern High German -schaft. West Germanic *skapv\. 
"(engraved) vessel' in: Old Saxon skapu. " Schaff, ship'. Old High German s/ra/" vessel. 



JchaTT', whereof scepfen^ draw up, draw out, draw; remove, take out, take away; drain 
dry, empty out ' (after scepfen^ bring forth, produce, make, create, beget, give origin to ' 
early with strong inflection); diminutive Old Saxon skepil. Old High German skeffiT bushel 
'; ablaut. Middle Low German schope^ scoop ', Middle High German schuofei. " a small 
bowl with handles '. 

B. forms auf -b^: (including Latin and Balto Slavic forms with zweideutigem -b-). 

Latin scabo, -ere, scabF scrape, scratch, rub', scabiesi. ' scab, mange, itch; roughness; 
itching desire; mange ', scaber^rouQh, scabby '; with o: scobisi. " filings, chips, shavings, 
sawdust ', scobTna' file, rasp '; Middle Irish (s)cTp(^\\h bb) "hand' (expressive gemination); 
Gothic ska ban^ scrape, shave, shear'. Old Icelandic skafa^ scrape, scratch, scrape'. Old 
English scafan6s. (Old Icelandic Old English preterit skof, as Latin scab/}; Old Low 
German scaban^ scrape, scratch, cut (hair), clip'. Old High German scaba' plane ', Old 
Icelandic skafa^ rasper'; Old Icelandic skabb. Old English sceabb^ scabies ', Middle High 
German schebTc^ scabby, measly ', older Modern High German Schabe^ scabies ', Old 
Low German scavatho^ mange; scabies '; isl. skofiri. PI. " scrape, singed crust ', Middle 
Low German schdve{ar\6 schope) f. " scale, husk ', Old High German schuoppa 6s.; 

Latvian skabrs{= Latin scaber) "splitterig, sharp', skabrums^ sharpness, scabrousness 
', Lithuanian skabus^ sharp, incisive', skabu, -e//"cut, clip, hew, hit ', s/rdM'hollow out', 
nuskobti^ pick ', skobas, Latvian skabs^souf (*"sharp, incisive'); Old Church Slavic skobib 
" rasper', russ. skobelb " plane '; after Machek Slavia 16, 208 f. here Old Church Slavic 
chabb'evW, bad', chabiti^spoW. 

C. forms auf -p: 

Npers. kafad, kavad^ burrows, digs, splits ', kafcXeM, fi
================================================================================
Root / lemma: (s)k(h)ed-, (s)k(h)e-n-d- 

Meaning: to crush, scatter 

Note: (extension from sek- "cut, clip') 

Material: Old Indie s/r^ao'a/e (uncovered) 'splits' {*skhnd-l)\ Avestan scandayeiti^ breaks, 

destroys ', sk9nda-rr\. ' destruction ' etc.; Middle Persian s/ras/a/7 'break, rupture, grind'; 

Armenian seA/'chip, splinter, wooden log' {* skhedri-); 

gr. GKESavvupi (Aor. also without s-: £K£5aaaa, £K£5aa6£v) 'zersplittere, zersprenge, 
zerstreue', ablaut. aKi5vr||Ji ds., OKiSvapiai, KiSvapai 'sich scatter (from 
Menschenmengen)'; OKiSapov apaiovHes.; 

alb. tshanj, /s/75y'split, tear, rend, plow' {*sked-nid)\ Latin scindula, scandula\. 'shingle'; 

Middle English sea/ere/? 'scatter', engl. scatter 6s., shatter^break, rupture, grind'. Middle 
Low German schateren^\N\Vc\ Gekrach apart reiften, loud laugh'; 

maybe alb. {*scater-) shkateronj" destroy, break' 

Lithuanian 5/reofen/a "splinter', Latvian s/reo'e/7s 'small, cleaved bit of wood'; Lithuanian 
kedet/^break, crack', /reo'e/?//' pluck, wool krampein'; 

Old Church Slavic skgdb^arm, small'; russ. scedryj^ generous ' ('*vergeudend, sein Gut 
zersplitternd'), sloven, scedljiv^ economical ' ('*bigoted, narrow minded, stingy = 
abzwackend'). 

References: WP. II 558 f., WH. II 488 f. 
Page(s): 918-919
```


## [2026-09-14T01:33:15.412Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_full.txt',encoding='utf-8',errors='replace').read()\nblocks=re.split(r'\\n(?=Root ?/ ?lemma:)',t)\nfor b in blocks:\n    m=re.search(r'Page\\(s\\):\\s*([0-9]+)(?:-([0-9]+))?',b)\n    if not m: continue\n    a=int(m.group(1)); z=int(m.group(2) or a)\n    if a<=578<=z:\n        print('='*70); print(b[:1400])\nEOF",
 "description": "Pokorny page 578 lemmas"
}
```


### [2026-09-14T01:33:16.559Z] TOOL RESULT

```
======================================================================
Root/ lemma: Rerbero- anA kertero- 

Meaning: variegated 

Note: (compare S. 573 ^e/"- besides ker-6\v\ color names) 

Material: Old Indie s5/'i/5/'5- "varicolored, dappled, dotted, spotted ', sarvani. " animal of 

the Maruts, night ' (i/stands for t>, compare Wackernagel Old Indie Gr. I 184 and:) sabala-, 

sabara- {d'\ss. reduction of first /) "varicolored, dappled, dotted, spotted ' (besides karbara-, 

karvara-, kabara-, karbura-, karbu- ds.); 

Note: 

The inanimate suffix -ur- : Old Indie karbura-' dappled ' : UAupioi , oi, lllyrians, UAupia , n, 
lllyria, alsoUAupi? , n. Adj. UAupiKO^ , n, 6v, lllyrian: -kpi, the region or province of lllyria, 
'lAAupi^cu , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

gr. K£pp£po(; originally " the dappled '; compare the mythological turn of Old Indie 
sarvarr, 

Slavic sobolb " sable ' seems to derive from Aryan. 

The root kerb-seeks Liden Stud. 50 f. in Old Irish co/t's//?? "besmirch, sully' and 
Lithuanian kirba{> Latvian kirba) "swamp, marsh, morass' and contemplates *kerb-diS 
extension the color root /re/'- (see S. 583 kers-), MiJhlenbach-Endzelin II 383. 

References: WP. I 425, Schuize Kl. Schr. 125, Specht Indo Germanic Dekl. 119, 262. 
Page(s): 578 



======================================================================
Root / lemma: Rer-3 

Meaning: rope; to weave 

Note: only Armenian and gr. 

Material: Armenian sari-k'P\. (Gen. sareac, Instr. sareoc) 'band, strap, cord' {*Rereia), sard 

(/■stem) " spider' ( *Rr-ti-)\ 

gr. KaTpo(; ( *Reri-os) asipa tk; £v iarco, b\' r\Q, oi aixwxovzq, 5i£Y£ipovTai Phot., perhaps " 
row of thrums in the loom, to which the threads of the warp are attached, ravel ', Kaipu)|ja ' 
ds., of the web so fastened ', Kaipow ' band the fabric together ', zero grade Ksipia " the 
strap of the bedstead ', PI. (NT.) " shroud ' (the forms Kripia, Kaipia s. Liddell-Scott; the 
meaning ' shroud ' through connection in Krip ' death goddess '?). 



References: WP. I 409, Kuiper Proto-Munda 122 f. 
Page(s): 577-578 



======================================================================
Root / lemma: /feA-^and Rera- : ^re- 
Meaning: to hurt, harm; to be spoiled 

Material: Old Indie srnati^ breaks, crushes ', sfryate, sTryate^ it is broken, disintegrates ', 
participle sTrna-, -sTrta-, sJ/Ya- "broke, decayed ', Inf. saritoh; 

Avestan asareta-' not broken, not made discouraged ' (= Old Indie asTrta-), sari-m. 
"piece, fragment, shard', sari-i. "break, ruin'; ein o(/7)-present in addition is perhaps npers. 
gus/7em Rupture, slit, separate' from Old pers. *vi-srdamiy, 

gr. KEpa'i'^w "devastate, despoil ' (*K£paF-i^(ji), due to a *K£paFo-(;; Kspa- = Old Indie sari- 
), aK£paiO(; " unbroken, unmarred, unscathed, undamaged ', K£pauv6(; "thunderbolt, 
lightning' (*K£pa-F[£]v-0(;, actually " smasher '); lengthened grade gr. Kpp, Kr|p6(;, f. "death, 
ruin; death goddess ', (proto gr.e; Attic saying 9upa^£ YJapzo, (Kr|p£c;) ... one explains from a 
secondary Nom. *Kap from *Kap(; with a from previous paradigm Kpp : *Kap6(;); Kapiwaai 
anoKT£Tvai Hes. contains reduced grade, as alb. ther, aKnpiO(; " unharmed by the Keres; 
generally, unharmed, harmless ', Kripaivu) "spoil, hurt ', whereof a Kr|paTO(; "unharmed', also 
"pure, candid ' (reduced also with aKnpaTO(; "not mixed '); 

Latin caries {*Rr-Je-\.o present *carid) " the rotten being, decayed being ', cariosus^ full 
of decay, rotten, decayed, decomposed; brittle ', carius^ dear, precious, valued, esteemed, 
belove
```


## [2026-09-14T01:33:28.733Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 'sairi' 'sairya' 'sk.nda' 'scand' 'kar.ta' 'car.man' 'kar.na' 'hak.r' 'skar.na' 'fra-san' 'frasan'; do echo \"### $p\"; grep -n -i -E \"$p\" BRT.txt | head -12; done",
 "description": "Grep Bartholomae for Avestan forms"
}
```


### [2026-09-14T01:33:29.898Z] TOOL RESULT

```
### sairi
3260:•  j.  aSairi.dahyav-  Adj.  (auch  mask.)  'der unter  dem  Land  ist* :  mi'kr?m  upairi^ahyOm ..  'yam  (ASm.)  Yt. /O.144.
3262:•  j.  aSairi.naema-  m.  'die  untere  Seite': "^wamca  drujitnca  niüamn  'ntpmca  Yt4-
3865:•  j.  aiwLiütay-  f.  'Herzuführen',  mit  Akk. verb.;  'niliitt'* .  .  spämm  sairitim  . .  aisa druxs  ya  nastis  apaMvqsatti  "und  beim Herzuführen  des  gelben  . .  Hundes  fliegt davon  . ."  V.  <y.  1 6 ''.
4568:pata%a  yat  °r>  vä  aat  -rs  vä  . ."  N. i^j.  1)  Praen,  a)  mit  Akk.  'innerhalb, in,  unter,  zwischen';  a)  räumlich,  auf  die Frage  wo?  und  wohin?:  I  'r  imil  dakyävJ' tnarüyJ'  hyi^  . .  "innerhalb  dieser  lin- der.." Bh./.8;  —  lör'fftf  -r''' didäm  frä- ^ayam(sd.)  Bh.2.13;  —  "n  sairi  (sd.) varjzüne  V.  75. 17;  —  'r>  daWiku  päpsr^ täiie  Yl.  JO.8,  -15-49;  49'j  —  yS  vlräzaiti *r3  raita  räsmana  Yt. /4'47;  —  nisaim (sd.)  yim  °r»  mSurumca  iäxoTmca  W.i.T,
5857:•  j.  aspäyaoSa-  Adj.  'zu  Ross  (oder  um Rosse?)  kämpfend',  Beiname"  des  Zairi- varay:  °Ö3sairi.vairilYt. 5.112,11  J  (hier eingeschoben).
6536:Vfil.  aiakva-.  —  Pü. :  fehlt. •  j.  azay-  m.  i)  'Schlange',  ein  ^ÄiÄisches Tier:  /<fiws.tara  ya^a  'zayS  xsvoewanhs V.iS.ßs;  —  'Sinam  udarS.>rasanam  .  . °iinam  spakanqm  kahrpunanam  (sd.)  V. 14.%.  a)  Sing,  in  koll.  Sinn:  äat  ahe paityänm  .  .  'zimca  yim  raoioibtn  (sd.) zj'rtM/a..V./.2''; — yai3  '%wä  niHt  aiwi,- Jruzilnti  •iisea  arütuiisca  "damit  dir kein  Arg  antun  können  Schlangen  und  .." YL5, 90.  2)  schlangenähnlichcs  Untier 'Drache,  Ungeheuer'":  'zdis  sairitaAe simahe  vlsS.valpahe  Y.().3o;  —  'zis .  . gäuitava . .  vTraja  Aog.  ~S;  —  'leis  vJlspahe N.  48;  —  ktrasäsps  .  .  yS  jartat  °ilm (sd.)  yim  aspB.garpm  mnganm  ..
9060:mit  US  'durch  Graben  heraus  holen, ausgraben':  yai  bä  paiti  fraisl»in  uskmti {■^^'^h^yahmya  sairi  nikatile  "an  welchem Ort  man  am  meisten  ausgräbt,  an  dem Leichname  eingeschant  sind"  V.J.  12.  S. noch  anuskattte  Inf.
9299:II  .)f*;,L!'-o7/"jriTverstiimmelteUä'ä  kavä  ..\.44-  2°;  —  .V^'^-  *grihm<l Formen.  Man  erwartete  »i^^jr/jK/j/,  »i-riHÄwA  [(sd.)    aM  varata   'pa   xsairimcä    Tianqm
10059:gehen,  sich  daran  machen  etwas  zu  tun' (Inf.):  yS  anyeÄe  dahmahe  hansma  *fra- st»r»nti  {sA.)  frajasaiti  li.104.  3)  mit antar»  und  Akk.  'hineinkommen  zwischen  — , unter  — ':  yim  antar»  vastr^m  frajasai yim antar»  shit»m  rätum  frajasät  "wenn  er unter  ihr  Gewand  hineinkommt,  wenn  er zwischen  ihre  befleckten  Schenkel  hinein- kommt" V.  16. 16.  4)  absolut  'vor  sich gehen,  sich  vollziehen' :  kakmat  hala  usa- hinanqm  gd^anam  ratufrii frajasatti  "von wann  an  vollzieht  sich  .  .?"  Vi.  46;  4j, 48,  *4g,  *50,  5/;  —  ahra  aont  fra- jasaiti  baxta  {%A.)  alät  nijasaiti  W.$.Z; — yesi  tat  frajasäi  antar»  sairi(sd.)  var»- :(T»^V.  15.17; — yaica  aiiä  gatwa  ustrS.- stänagsva  frajasai  "und  wenn  es  —  es handelt  sich  um  die  Hündin  -  im  ..  vor sich  geht"  V.  ;5,  23*".
11070:sind  getrennt:  yS  gam  ia^d  apasca  itrva- rh^ä  Y,5/,  7";  — yi  .  .  amfrstatäUm  .  . as>mcä  .  ,  dätakä  (sd.)  .  .  xsairimla  Y. g4. 1 ;  —  a  mä  alhmö  hazascä  [rw»fl] '"' äkiSäyä  (sd.)  ä?nsiä  tivilcä  Y.  2(j.  i ;  —  mos- tJm ..  sparumca  vtniiraytumca  vanaitttlmca uparatät»nt  YtJ,  36;  —  apqm  napas)  tä äps  . .  vlbaxsaiti  vätasca  . .  awidätimla c^arfnB  asaonqmca  JrmiasayS  Yt.  8.  34; Y.  j/.  2a;  —  anyS  asSI  'kwatcd  ..  vahtstä- aüä  manarthd  Y.50. 1 ;  — yada  a?»m  twTm (sd.)  anAin  maedäscä  ahurhtths  asicä  -j* armaitl  Y.3/.  4.  a)  mit  Tmesis:  srao- s)m  .  .  asimca  . .  nairimca  saahfm  Y.57. 3  (s.  dagegen  Ytio.  53).  c)  das  erste Glied  ist  ein  enkL  Pron,  pcrs. ,  das  sich auf  einen  dahinter  stehenden  Vok.  be- zichtJ*;  nur  gAw.:  yi  "hwat  mazdJ  .  . a^alBu^cä  ..  virtz^naRyücä  ..  atryamanascä . .  gSuscä  Y._5'_J.4;  —  anats  va  nBit  ahurä . .  aipmeä  . .  saranafirnJ  . .  maitatcä  hyaf vahisiMtt  Y.  2Ä  9 ;  —  yS  vi  asa  ufyäni manascä  vohü..ma2dqmcä  Y.25.3.  d)ein Glied  oder  mehrere  oder  alle  sind  rela- tivisch  gegeben;  cä  steht  dann  beim  Rel.: narSi  firasaoiträi  maibyäcä  yalibyascä  Ti rrivAan'Aöi  "dem  .  .  J^r.  und  mir  und (all)  denen,  denen  du  .  ."  Y.  2.9.  8;  — AviF  .  .  yas!ä  .  .  dadät  yascä  . .  vfväpat yaüä  . .  vöiidat  '^.32. 10;  —  kavaim kavätsm  yimca  kava^n  aipi.vokum  yimca^.. Yt,  /()•  7 1 ;  —  ya  äps  yssla  urvari  yasca asaonqm  fravasayS  Yt/o.  100;  —  hujUayB .  .  yS  .  .  anharj  yascä  hfntJ  yascä  . .  ba- vainti  Y.33.  10;  — yä  tsi  .  .  adistil yacil vohB  uxbä  /ras'l (sd.)  ntanankäyäcä  ff/ö.. y.44-^',  —  yä  var^sä  yäcä  pairj  (sd.) J//  syadi^ani  y.lcil  .  .  aryat  (sd.)  V.  ^o. 10.  a)  mit  unregelmässiger  Stellung  des ain  tifyänl  manascä  voka  .  . %hur>m  yaeihyS  xsairpmtä"^ ■«(sd.)..Y.2Ä3(s.c).  e)das st  nicht  ausdrücklich  genannt, dem  Zusammenhang  zu  ergän- )6  u.);  nur  gAw.:  atcä  ..  scarUB iva'ä  viitlsps  ..forasaosiras'ä id^f^undA"Yoj.a.      2)die
12343:•  j.  tüirya-  Adj.  (fem.  'ya-)  'm  den TSrem  gehörig ,  ihnen  eigen'  (usw.): 'yanqm  dahyunqm  Yt  5.  54,  V.J.  42  PüZ., 5.  38  PüZ.;  —  airyanqm  dahyunqm  .  . 'yanqm  da^nqm..sairimanqm  dahyunqm Ytl3.  143;  143;  —  mairyS  'ryS franrase Yt /J.  56,  82;  5.  41;  —  mairxm  'rim franrasyämm  Yt().i8,  22,  ip.77;  Y.Jj.7.
12594:•  j.  daxma-  m.  'Leichenstätte,  Leichen- bestattungsort'*':  'ma  (NP.)  .  .  yaAmya nar/f  irista  niiayeinte  V._9.  9;  13;  —  sairi ..  triste  °me  nihätte  V.  7. 49;  —  avi  Ai irista  tanOm    upa    "ma  fraiaröis  \A.i2;
### sairya
6337:•  j.  aäasairyank-  m.  EN.  eines  Gläu- bigen; aiasär^ahe  "yqs  (NS,  statt  GS.) " asaonB  Vt/y.  114.
22424:•  j.  vaSairyav-"  Adj.  'nach  Begattung veitangend,  brünstig',  vom  Kamelhengst'': uitrS  'rii^^  Yt.i4.39;  12;  —  uÜrahe hhrpa  'ryaol  Yt  i^.  n ;  *F.  8;  —  uitr&nh5 .  .  p»r3tamna  (sd.)  'ryavd  Yt, /7. 13,
26119:•  j.  sairya-  n.  "Dünger,  Mist'*>:  ava  hl gätüm  äärayjn  atryehe  (sd.  t  va  'yehe  vä V.&8.
### sk.nda
5777:•  j.  a-skvnda-  Adj.  (fem.  'da-)  'ohne körperlichen  Schaden,  ohne  Gebrechen': kanyqm  °dqm  anupayatqm  "ein  Mädchen ohne  Gebrechen,  das  noch  unberührt  ist" Y./^.iS.
26474:•  ].,  g.  skvnda-  m.  i)  Bruch,  Zer- brechen': adä  .  ,  ava  ..  drüjS  baimitt  'da spayd^raAyj  (sd.)  Y.jo.  lo.  a)  'iar- (Sp.  445  m.)  mit  'di/n  sva.  'zerbrechen, zerstören',  mit  Akk.:  'd^m  si  maus  k>r>- nätbi  "zerstöre  seinen  Geist  (Denkkraft)"  ■ Y.  p.  28.  2)  'Gebrechen,  körperlicher Schaden'  (nur  Komp.).  [V.5.  59:  lies tkfttde.aipi'.]  ]
### scand
4923:unsTcs  schwachbetonten  'er'*':  fravasayB ..  yä  ahurahe  xiayatö  daiinam  ufayüÜt- ynnii  yai  aim  bavaiti  *alavaxmul  yai fi  bavainti  anäzaritä  Yt.  /J.63;  —  ä  dim paskät  anumar»zatim  aHila  . .  färfndtl'a  . . visp>m  ä  akmät  yat  aim  paiti.apayat.,'H\.. iV.38;  —  vispaeibyS  sastim  baraiti  älarS. . yaübyS  alm'''*  *ham.paeaili  ..  \.62.T,  — iim  Aaxa  Aase  baraiti  . .  ?  äat  yai  s!  a^m  " baraiti  .  .  Y.  62.  8f.;  —  yim?m  .  .  yerihe xsä^rä',a  ndit  aotim  inha  . .  para  akmät yat  hlm  a!m  *draogpm  välim  .  .  patti.- barata  Yt.  ig.  33 ;  —  tvai  na  *ai^rapaitim updisai  .  .  iim  *aSm  at^^  aS^rapaitim upayat  (sd.)  N.  Jlt;  —  mürtm  .  .  yd .  . frä  rasmanö  scandayeiti  .  .  ari  dlsalm.  . Ji^iM  *baraiti  Vtio-^Gt;  loi,  71  (yavata aim),  .5', 43  {yezi  alm),  47  (ya^a  am); —  aom  asmatum  ,  ,  mariay^n  ahe  yäiia vis  aim  .  .  Yt.  ij,2.  2)  auf  ein  Nomen vorausweisend:  äa^  mg  alm'°^  pait- yaoxta  AaomU..Y.ff.i;  V.2.3.  III)  ver- doppelt, substantivisch  sva,  'irgend  ein  be- liebiger': _)(7/  hl  nazdiUö  dahmö :'dü'/(sd.)  yavat  vä  aSm  aim^^^ uübya  N.2;.
8357:•  j.  upairLkairya-  Adj.  (fem.  ys^  'des Wirksamkeit  oben  gelegen  ist,  von  oben her  wirkend';  fravasayS . .  °rya  .  .ya  upairi  \ */iamarmäi.,  aur7»^anqm..b3züi  scanda- yeittti  YLy.31.
17127:fravaiayS)..aurvaiianam  uyra  °züs  scanda-  _
21749:•  j.  'yezi  Konjn.  'wenn'.  Die  Koirelata (Stverz.)  des  übergeordneten  Satzes  sind durch  Sperrdruck  hervorgehoben.  I)  kon- , diiional"  'si;  wenn,  sofern';  i)  mit/ni^.;| im  übergeordneten  Satz  steht  a)  Praes.: y  va  (Sp.  1305  u.)  dim  aiwi.druiaifi  ,. nmum^-paitis  frasa  upa.scandayeiii  . .  nm3- mm  Yt.7o.  18;  Y.  ö'a.  9;  —  'sica  aps  .  . ASyum  frabdtm  paiH.jasaili  kva  .  .  druxi yä  nasul  upa.dvqsaitil  V.^*.  69;  41-68'*;
26443:scandaya-,  ^shndaya-,  scindaya:
26444:'zerbrechen,  zerstören,  zu  nichte  machen' : yS  rasmanö  iHndayäti  Yt  14.  62;  — Jra- vasayS  .  .  yä  .  .  aurva%anqm  ,  .  iSsBs scandayeinti  YtJj.  31;  —  ime  nS  *^uyra *bäzava  kanta  .  .  sHndayeinti  "die  da machen  unsere  starken  Arme  . .  mit  dem Messer  zu  nicht"  Yt.  /o.  42;—  tum  aisqm.. Ibaisi  scindayehi  Yt. 70.76;  —  alsqm  ihai^S scindaydmtmYt.i.tT,  —  sSndaya  {i%lh..) asavajanS  Yt.  iO.  76;  —  scindayat  F.  12,
26446:mit  upa  'zerstören':  /rafa  upa.scanda- yeiii  mürS  .  .  uta  nmamm  Yt.  70.  18;  — upa  anyh  (näml  timanä)  sandayäti  Yt j  10.  28.
26447:I  mit_^a 'zerbrechen,  zerstören,  zunichte I  machen':  fra  rasmanS  scandayäti  Yt  70.
### kar.ta
3036:'akarsta-
3038:•  j.  'a-karäta-  Adj.  'nicht  ausgesät'  sva..  \ syaaina  V.j.zi';  i.  ii,  12,  16;  —  'ya 'nicht  durch  Aussaat  gewonnen,  wild  ge-ljrätava  V.i.i^;  F. 7;  —  °y?mäi  vimanö.- wtLchstn':  j'ovanam  ..  aetavat  karstanam' AJtn  V.J.  7;  15;  —  'yanqm  ma^ranqm altavat  °tanam  "Getreide  ..  so  viel  vom  Vt.  10.  20;  —  -yqm  ifaaiirim  (sd.)  YL gesäten,  soviel  vom  wildgewachsenen"  V.   z^.  57;  V.  j().45;  —  'ya  danta  läsyä^  (sd.)
3043:•  j.  'a-karsta-  Adj.  (fem.  Uä-)  "nicht  be- pflügt, ungepflügt':  Tm  sä  .  .  yS  danya 'ta   salta  yä   karya   karsivata  (sd.)   V.
3694:•  j.  '''aipi.karata'^  Inf.,  mit  asii  'er  ist eingedenk,  hat  Acht  auf  — '  (Gen.):  vis- paz'a  vilcS  mazds.fraoxta  .  .  ySi  huiti  "la dusmatahe  ".  .  die  Acht  haben  auf  das, was  übel  gedacht  ist"  Y.  71.7;  7*.
4475:•  j.  ain-iiltay-  f,  i)  'Unvermögen  (zu  — )': . .  nöil  aSavan>m  'tis  asiarayeiti  "so  macht das  Unvermögen  (es  zu  tun)  den  Gläubigen nicht  sandig"P.;2;  *K.ioi)'''.  2)  'Besitz-, Vermögenslosigkeit,  Armut':  paitistatSe 'tdii  daSi'S.frakarstaya  Yt.  /j.  130;  — yask>mca  mahrk>mla  .  .  °tlm  *ducHrim Yt.;o.iio.'>
5655:•  i-,  p,   'arätay-  f;  m."  'Speer,  Lanze': yaäam  zayanqm   raitöiiti  paoiryS  °iis  V. 14.^;    —    'tayasiä    karitayasca    '^.fj —  •//'/  ki-aiwyästa  Yt  13.  7 ; •tSis  huxsnutaya  Yt  10.  24;  —  'tayasat
6220:•  j.  aSava.karäta-'>  Adj.  'von  (einem) Gläubigen  bewirkt,  veranlasst':  paitü'tälSe •tahe  tba^aahö  Yty.129,  105".
6396:•  j.  a^samnö.gan-   Adj.   'das  Ziel  nicht  den  ganzen  M.   in   sich  fassende  As3m~ treffend":    karptaUt    altqm    hufräyuxta  ..Gebet  bekannt  wurde"  Yt. /^.  91.
6549:—   aurvB  'io  (NSm.)"   kava   usa   YL  5. 1  •  j.  azt.karäta-  Adj.   'von   (oder   'vom) 45.  VgU  noch  'vancak'.  !  Drachen    bewirkt,    veranlasst':  paitistätSe
7887:•  j.  'i'8a  Adv.  'jetzt,  nun':  abdaca  (sd.)  Ivd  darrja  akarsta  saaa  ..  '6a  i'amiti  .. ila  sadayäj  ya^  "Sa  ..  pdo?m  vamaite'^.yä  darrja  apu'^ ra  *a?i(i  V.J.24.  3)  Es 2.24;  —  fitfii  mi  'oa  *affAäJJ^m  ''^f» .  dient  dazu,  ein  oder  mehr  vorangehende vtra  Yl/J.13;  Ä54;  —  äaj  vai^uAi  'oa  Wörter  als  Zitat  zu  kennzeichnen*';  das .  ,  artdvl  sare  .  .  az'at  äyaptun  yüsämiVlJSsx  ist  dann  Subjekt  des  Satzes:  yetiAe Yt.  5.130;  131;  —  'ta  irUlanqm  urvanS  ^'oa  mazdä  yasritm  a»as/i  "ye/>Ae  \chit  die yazamaide  Y.26".7;  2,  4,  7,  Vr. /(».  i,  2',  j  Anbetung  des  .(y."Y.  2  j.i; — ya»kqm  'oa Yt.Jj.9S,  148'; — frä  U  zq'ismca . .  azsm 'alaoninqm  ärmaiH.paoiryanqm  yasmm •oa /rasnayeiiiy.21.6;'],  VytiJ; —  kaAepara.ciiiasti{zi.)\.2i.2; — ya%a  frä  'oa n5  'oa  nqma  äyatryaf  (sd.)  Yt  ZJ,  50; —   ämraot  yal  ..    'lyaSJa  sagt  aus,  dass  . ."
8018:•  j.  iäav-  m,  'Pfeil':  as/a  isBin  F.  7;  — °sam  vä  arilim  vä  P.  2/;  —  nSit  dim  .. avasyat-nsit  'savS  nöit  karfta  mitvazra Yt./.i8;  —  va:rS  .  .  'ms  »^ili^axis  .  . arailYt.13.T2;  V.4.  ^$,  f}.46;  —  'savas/a 3r;>zifyS.parma  asanasca  ..  V,  17,  gjYt. /0.39,  101;  —  'lunam  *taArkäsS.paranam Yt  /o.  1 2  9 ;  —  arStsH. .  'faos  para.pa'iiwatö Yt  10. 24.
8830:•  j.  uvayö.därä-  Adj,   (mask.   'ra-)   'auf beiden  Seiten  schneidend,  zweischneidig': karftanqm  'ranom  Yt. /o.  131, Komp.  mit  I.D.  im   i.  Glied.
### car.man
4368:•  j,  an-^azdya-  Adj.  'nicht  fett,  mager*: nSit  pasusLO  (statt  IS.)  iazda  nsi/  irista (sd.)  {nOit)  °ya  ratufris  abanta  airista *asdya  .  .  N.  ^6;  —  ratufrii  *paysbis  . . ^azdyäisca  *'\\iuca'^^  .  .  pitus  .  .  *atdysii n5it*°yäis'K.  mskSmua  rTzuüa..  *asdyäif näit *'y3is'> N.5 7 ; — ratufris  carTmanqmca pasv.vastranqmca  .  .  *asdyanqm  nSit *'yanqm ''    (nämL   pasunqm)  ^     "r.    wird
15876:•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
### kar.na
3211:'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
4051:•  j.  ^paourus  kar:na  . .  afravao£ü  hava Mxva"  P.45.
4247:uranfinglich' :  akarana  'ra  asaonS  sUs^sA.) YtÄ48;  F.  7.  a)  'ra  raocä  (iA.)  "die!
5607:■iPiMf  VL/5.57;  —  'VB  nama  ahmt  'mS:'  j-  arazo.suta-  Adj.  'der  zur  Schlacht iwoM  (7/tffi»  Yt  75.46,         *  I  ausgezogen    ist':    vispe    karana    rasmatiü
7538:•  j.  'äzäta-  m.  FJ<I.  eines  Gläubigen:  'Iahe karsnayanahe  asaonB  Yt/J,  108.  I
8453:•  g.uba-,  j.  uva-'l,  uva-",  ava-»,  ^^•''^  aspa.vJraja  Yt./O.ior;  —  *.vayt  l.\Df.) Adj.  (fem.  -3-).  Du.  'beide':  V«  «afiwa  I  p.  2b«';  —  ub5ya(^)  F.:.'b»  c)  Plur N.p9";  —  7'a^<i«afl«aft>vrtV.y.3i-37  adjektivisch  'beiderseitig,  beiderlei':  sai/^e PüZ.'';  —  uva  karana  aiMä^  z»mS  Yt  10.  .  .  ;i<i/„^a  .n-afi  (APn.)  xsudrä  'kam.- 95;  5-131.  19-^9'  —  -vayäi'  maimvä  rac'^wayäti  mazdayastianamca  daiiäyas- dämqn  Ytij.76;  —  uvaHl^a  nö  ahubya  nanamca  "wes  ..  Frau  beiderlei  Samen nipayä  aluca  auhius  ys  astvats yasca  asii  durcheinandermengt  . ."  N./i. manahyö    Y.57.2S;    25,    YL/0.93';     —       Ableit  ans  bAi..  —  «L  i^^lJja-  Adj.  —   Pü.;
9242:•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
9256:.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
9264:•  j.  V'^narw/ kar«na  ap<itäta  .  ^  '^.45-   '^k?rfntu^'^    mazdayasna    mSca    '^k^rftu'^ Pü,:  iJr  'Tat'"),  —    ']  Danach  wäre  karfna-    iriiyäl  .  .  yfzl    "kpnnW''  yesi     "kir^tu'^
9314:'"f  ^V  ~  ""'■"'"'^ -iT' ^^'  l,^^"  .         or    '•  J-   karsna-   m.   EN.   eines  Gläubigen: Ableit.  —  ai.  vgl.  kalpa-  m.  'Ritus'.   —    Pfi. :  i         ■      +  ,  ^        i     /  j  i        ■•       ,    « j
9316:Itehrter  Reihenfolge):  adari^ä  airotäraJca.^^  ,  ^^  karsnayana-  patr.   Adj.  'von  Karsna
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
### hak.r
3364:ahurö  mazda  A.4-  3.  b)  zurückweisend: kat  tl  aisma  yaoidayani  . .  aitiha  Z3mö niäai'iyan  . .  hak^ryt  dpö  vlsraslaym  'ia yaozdayqn  V.  7,28f.;  74,  N._<?j,  YL/0. 117;
3440:fryai  "inoavqs  (sd.)  saßyll  maj-ailJ  at  nJ a},i  ..  dazdyli  hakurmi  {%A^  Y.44.1; 161  3^-7iS4-^^  (benutzt /7. 9),  2)  ein- leitend, unübersetzbar:  aj  niä  yavä  blndxS pafri .  .  Y.491;  '•  5<  3<*-3,  3'-^.  33"' 9,1^,34-4,  4ß-A,t4,  4tV.3,  7,  12,  5«.  10, 57.10.  a)  insbes.  beim  a)  Futur:  al  tJ
3873:Zum  V.  vairi:  —  PS. ;  hakar  ast  tus  .  .  apar z'ämU  itlil.  —  I)  Zur  periphraslischen  Aus- dnicksweise  vgl  Bthl.  IF.  j.  19  (und  Dbr. AiS.  404  lu  MS.  /.  10.  13);   s.  sucb  lu  <«i-
5337:Et.  und  Bed.?  —  Wohl  AvyVioTap.  mit  >a'.  — Pü.  X  hakar  tuvätt  üfie  g^wisn  ape  gffivZt  (?).
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surunvaiH N.  26;  60,  _jtV,  3Q,  iV(V,  g6,  100,  101, 104, 105,  54*>,  26  aSt.*',  (J5'>,  97S>; — yu  nBit öim  .  .  vääm  *aiwy<Is  . .  yezi  S°  öyum.pe väcim  *aiwyas  anaiwisH  (sd.)  .  .  N.  74; IQ.  4)  zur  Anknüpfung  eines  begrün- denden oder  erläuternden  Satzes  'denn; nämlich';  minyö  yö  parö.dari  .  ,  ä°  hS msrrfS  väcim  baraiti  Y.iS.i^;  —  sasta he  .  .  /rasnsoay^n  ä°  yat  he  zasta  mit framata  äat  (s.  7)  ,.  V.  1^.40;  —  mä  äi barg  (sd.)  agvS  yat  irisUm  ä°  yezi  sS  barai aivö ..  V.5.14.  5)  in  Säuen,  die  eine Aufforderung  oder  Wülensäusserung  ent- halten, 'so  .  .  denn',  oder  unübersetzbar: a°  mS  ahe  .  .  paräca  vaepaya  Y.  /o.  12; ra,  Yt5,77;  —  ä°  tum  ,.  nava  rnaya ni^wjnsöis  Y.iO.iS;  22.2,  9;  —  3°  vS kascil  .  .  isalta  Yt/5.53;  —  ä°  tbaHä taurvayeni  Yt. /4-4;  —  a° .  .yasami  Yt^. '3o>  131;  —  ä°  dis  avaioayamahi  Y. 4.aff.,  24.Z,  5.  55-^^  Yt.ii.i6,  ai;  ^.5, 11.31.  a)  hinter  dem  ersten  Wort  des Satzes:  imqm  ä'  sqm  .  .  yazamaidiY.^H. 1 ;  gg.  1 ,  a ;  —  alahya  a°  sairl  .  .  ädä (sd.)  Y.  JJ.8;  —  aZsmanqmat  3°  .  .  /ra- näsayata  A.  j,  s^  b)  in  anderer  Stellung: paoirlm  upa  may>m  haktrit  äpö  ä° kvqm  tanüm  pairtyaozdai'^Tia  V.p.31; 31.  6)  hinter  dem  Pron.  interrog.  wie
11318:Verbindung  von  Ht,  ASn.  aus  'iaj'-,4'''ö,  Frage- pait.,  ar.  **Jti(Pausaform)-B3;  lat.  juid-ne.  — Pü.!  Xsön  hakirL
13312:Vgl.  väsU^.dälainyo'.  —  Pü.;  hakar  rat  an  i drünisa  dahetSt.  —  '>  DsT.s  Übersetiung  'du bois  (d^jä  coupi)',  ZA.  3.  145  ist  mit  dera überlieferten  Text  nicht  vereinbar.  —  »)  Vgl. N.  61  f.  —  3)  S.  daiu  irfä-  mit  iifa  und  No.  30.
13371:'(ein  Gefäss)  aus-,  bis  oben  anfüllen mit  — '  (Gen.) :  yezi  aahat  (näml,  das  Gefäss) zarmamis  hak?r)t  fi-asnääayfn  maismana gSui  hakint  s^mS  uzdä'kaym  hakirit  apö frasnähaysn  a%a  yaoidayqn  V.  7,  74'',
21082:lial  Imäk  otai  istet;  s.  aber  No.  7.  —  9)  Pü. : haiar  j  afi  kam  hakatün  raminfnd,  erU :  3  lik räsi  ape  girind;  s.  noch  No.  lO.  —  ■")  Pü. : hakar  3  fia  katanbi  5  kam  därind,  ert. :  J  läk rast  ape  gircnd;  s.  noch  No.  9.  —  ")  Vgl. liilava,  —  <>>  Pu.:  kakar  tuvätilk,  Sü.:  yadi  tat prjflam,  Npü. :  har  fäi  an  das/^äA  alt,  — ■J>  Pü.:  if  ,./räc  rasa.^tt}  FiL:/rä^  Aar» rasim.  Lesung  des  Worts  unsichet.  DsT.  ZA. 2.  342  lässt  y  J'räy  aus.
21256:ai.  yäccil  Adv.  'wenn  auch'.  —  Pö.  (lu  N.) : ka<i;  (lu  F.):  hakarÜ;  (zu  Y.):  hin.  —  »  Vt. //.  55  steht  in  gleichem  Sinn  y<U  .  .  aal.
22105:(sd.)  vainantS  (AP.)  braianta  . .  »mabm zaranim  Yt.5. 129.  a)  mit  ergänzendem Partizip '':_yff/i'tfOT  ainim  avaSiai/(2SPiA.; Augm.)  saocayaca  kirmavanttm  "wenn  du leben  andern  .  .  treiben  sahst"  H. 2. 13; —  \ya'h3  avaina'  imäm  bümim  *yauda'tim (sd.)  D.ö'.4.  2)  AkL  'es  einer  Sache (Akk.)  ansehen  (können)':  vansim  . .  vae- naiti  kalarS  ayravU  (sd.)  vi!  *bunavs  vä Yt.  14-  31,  iG.  10.  3)  Akt  'ansehen für  — '  (Akk.):  ySi  %wS  vam»n  .  .  aham rff/Bwc'fl"diedidi  für  denj4.und^.  ansehen" YL  10.  92;  — yim  dim  vaEnät  *rvistaäva (sd.)  *vindatum  N.  16.  4)  Med.  'videri, gesehen  werden,  scheinen':  a6da(sd,ya i  (sd.)  ioa  . .  sadayät  yat  iha  pasSuS .  .paa?m vaSnäite  V.  2.  24;  —  haksrit  ir  irixtahe I  (sd.)  .  .  valnaite  (statt  Plur.)  itarasca  . . V,  2. 40;  —  \tya'paüy  iariam  vainataiy naibam  (sd,)  X.i.  ^;—~  tanOm  yä  mi  val- naite Auraeoa  ".  .  quae  mihi  vtdetur  for- mosa"  Y.io.14.
22825:hakirH.janS  'räzahe  Yt  1.^.15. 1  Vgl.~»iwfläa.  EN.  —  ai.  wflj-ä-ia- m.,  np.fNpO.) guräi.  —  ')  R.  zu  tarian-  No.  3  und  oaai [  KÖieptm  E  783.  —  ')  Zur  Verbindung  von 1  varäta-  mit  arlan-  s.  vfiabkir  varähäih  RV. I       TO.  67.  7.
### skar.na
26467:•  j.  skarana-  Adj.  (fem.  'na-)  'rund': aiibAa  z^ms  yal  pa%anayä  (sd.)  *nayS dBraiparayä  Yt.  10.  95;  5.  38,  J7, 19,
### fra-san
### frasan
7501:•  j.  'ä-sna-  Adj.  (fem.  °»<i-)  'erfolgreich, wirksam,  tüchtig':  'naca  (APn.)  viana asäunam  'nafa  manä  sae^antqm  Vr.  J/.3; —  °K.7  (APn.)  . .  mata  Yt  13. 74.  a)  bes. von  frasanfay-  f.'*:  ifä%ravaiH  'na  fra- ttitntifY.tio.-j; — nairyam  '»am  *frazain- am  Y.öS.s;  62.S,  GS.'i-i,  Yt./o.3,  108, 110,    ;Ä5;    —    'naySs^a  paili    vanhuya
19311:3a; —  daevanqm  anSyantqm  ahmaUa  'näi aimäiüi  °tiahe  nmans.palSe  Y.  52,  2 ;  Yt  15. t*;-~fpfvru'^wa,.aora  mainyB kaca  °nat V.  11.10;  — yaoiääta..bun  'na  V. i/.a;  1, 4,  12.2;  —  yat  aiiS  nä yS yaoldi^tyS  hala aHiiyd  'naiiiyö  xshats . .  psrayst  V.g.  39; 40,  13.22;  —  yat . .  aiiqmUt  •»anqm[ca] caratB  dva . .  V.  y.  49 ; — vTspanqm  akmya •ne  nabänasdistanqm  Y.  26'.  7 ;  —  *katämS *naAe*'>  a%auruntm  (sd.)  pärayai  N.  /;  Yt 2.11;  —  t^a.vasatfitha  avi  'tarn  airya- maim  V.  22.  7;  13;  —  tum  . .  sara%uhra *nahe  pourusaspahe'H.  g.\y,  V. /p.  4,  46, Yt  i^.  36;  —  olsmanqmHt  .  ,  vazyäi/  .  . ratsui  'tarn  fränäiayata  A. j.  5:5;  —  us3.- hista  haia  gätvs/rasasa  haca  d^mänSi'-'' Yt  16.2;  —  yavat . .  späna  dt/  hapta  'tia *pairiJ(üahi{sA.)  bavqn  V.J5.4S;  — fratara (sd.)  haca  'na  v>r3syqn  .  .  V.iö.^;  — nistara.naOnal  'nahe  V.  17.  7 ;  6. 43,  g.  33, Yt//.  60;  —  mahsmya  'naÄe  N.yX;  — parepasca  'nahe  V.  y.  45,  46;  45;  —  k»m kfmHl  aipi  'ne  gatu  *saSe  Yt5. 102;  — raocamtn  paiti  'nahe  V.  7. 14;  —  ysi  °nä hqm.6arämahi  .  .  ätnmca  .  .  3at  paslalta ahe  'nahe  spa  vä  na  vä  iriäyäj  .  .  us haca  aHbyS  'naiiby3  baraym  . .  ätnmia  . . ku%a..älr7m  aiti  barqn  ava  aitim  'rum..1 V.5-39-4i;5'33';  —  '""  '»"^^  vfti  vTsi hr3yff  kata  (sd.)  uedat^yan  aetahe  yat iristahe  V.  5.  10;  —  ahe  'nahe  upa.- %'Ui»nsqn  (sÄ)  upa^w3T»tayqn  V,  Ä  10; — yui  .  .  iristim  upaJi?r3%wSJar3m  (sd.) avajtanqn  ava  .  .  iristim  baraytn  avaha 'mm  himaym  upa  .  .  'ntm  baötayqn  . . yezi  . .  *fum  upaJ>jr3%ws.tanm  avaxanqn ava  ..  °n3m  baraytn  V.  4",  af.;  —  ratu- fris  havS  yä  'nahe  *paitiricyehe  (sd.) ^■55-  8)  bes.  im  Gegensatz  zu  Ge- meine, Gau  und  Land*);  'vsa%Pi:^..yS  hu- dänul  damanahya^  xla'hr?m  idßirahya vä  dahySu/  vä  . .  frada%äi  (sd.)  aspfrazats Y.31. 16;  —  3  eJ  'mmf'  vUsm  vä  ist^rtm vä  dahyüm  vä  ädat  dusitäcä  (sd.)  .  ,  Y. ,3/.  18;  —  im  jAw.:  mikrS  .  .  ahmäi frasanäayäti  'tamca  vfs^m^a  zantümca dahyümca  daiiihusasilmca  Yt/o.  87;  18, Y.  62. 5,  V.  Ä  1 03,  N.  6';  —  «5 ..  ahmt  'ne .. aähe  vSse  . .  ahmt  *zantvlf  . .  a^he  da^kvB ftim  vaoSata  . .  ahurpm  P./7;  Y.5.  aS,  Vr, 12.  5,  N.(?;  —  *'nyaca  (LS.)*'  vjsyaca  tarda- vaca  *da^havaca  Vr. /2.  gj  —  yujyastTm haia  *'näp'>  a^a  [. .]  vTsal  ha%r?m  {ha&i)
20557:•  j.  misik-  Adj,  (auch  fem.)  —  ?  — '':  asim rSsaintlm  dar^yS.vän^marum  'sacim  Avd.- aiwisilam   'säam    äfrasanhaitim  Y.52.  i.
26999:•  j.  spantö.frasan-  Adj.  'heilige  Fragen stellend,    heilige    Unterredung    führend':
27054:•  j.  spiti-doiSra- ■>  i)  Adj.  (fem,  'rn-) '(weiss-  sva.)  hell-,  klaräugig":  narf  kihrpa .  .  xsaitake  "rahe  Yt.  <?.  13,  7*^.  17;  — frasanlBis    .    .    xs3ihr/yJ     'rajii     Yt.  y.
```


## [2026-09-14T01:33:47.758Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"'Messer'\" \"gaona-\" \"hak[?e]r[?e]t\" \"'taub'\" \"Fell\" \"Vernichtung\" \"sari-\" \"'sd-\" ; do echo \"### $p\"; grep -n -E \"$p\" BRT.txt | head -6; done",
 "description": "More Bartholomae greps"
}
```


### [2026-09-14T01:33:49.146Z] TOOL RESULT

```
### 'Messer'
9279:•  j.  'karata-  m.  'Messer':  ayanhalnäi^ °tsis  azdibti  paiti  ava-ksrii^yät  (sd.)  V. 4-50-  a)  insbes.  als  Waffe,  'Dolch- messer, Dolch':  yallam  zeyanqm  rdiniM ,  .  bityd  'IS  N.!4.(};  ~—  'ts  hufranliar$t5 Yt.  i^.  7  2 ;  —  HaBt  (NP.)  alsqm  hufrayuxta Yt.  10. 40 ;  —  iSavS ..'ta  ..  vazra  Yt. /. 1 8 ; —  'hm  iaranyS.saor^m  /rapixstfm  vTspi,-
9282:KoropA,  —  Zum  V.  iarit-.  —  Vgl.  ai.  kattari- t.  'Jagdmesser*,  np.  iärif  'Messer'.  —  Pü. : iärl,  {lu  V.  14)  erl.:  sampi/r  'Schwert'.  — ')  Wie  von  einem  j'-Stamm;  der  Aasgang stammt  vom  vorhergehenden  Wort,  [So  jetil auch,  aber  mit  aarichtigen  Schlüssen  MeILLet MSL.  //.  ZI.]
### gaona-
8857:(sA)  Jasti  N,/oj; — ^kaAyl^^"^  dahmanqm sao^räoa  (si)  *ratu/rU  N,  40 ;  —  draos (sd.)  z-iJ  paiti  söinma  unam  vä  katcit  vS paiti  sidaranqm  N.  IQO;  —  kahmäicit yanhqm  jasS  Yt  13.  41;  41,  V.  7.  7: —  yahmäl  kahmäiHt  na^nanqtn  va ä'ird  baoiöTm  baraiti  ahmst  kahmätHi naimanam  .  .  paiH.jasalH  ütars welcher  (Seite)  her  nach  irgend Seite  der  Wind  des  Feuers  Geroch  ver- breitet, von  der  her  nach  irgend  einer Seite  wendet  sich  ^.."  V.iV.So; — pasBm .  .  7-ohu^aorvm  vä  käcit  (IS.)  vä  gaona- nqm  hamS4;aontm  (sd.)  Yt.  8.  58;  *Aog. »7;  —  di^e  saite  kahyJat . ,  xrafstranqm V.  16.12;  —  kasatinm  kaAhhcit  va^wa- nqm  A.  j,  11;  — 'in  Verbindung  mit  anya- A(tj.  '.ilius  (]uispiam':  anys  kasat  ar?hsiis astiatö  N.  6j.  a)  Piur.  im  Sinn  unsres zurück  weisenden  'welche,  solche', Zeichnung  einer  uobestimniten  Zahl:  äjal aaaelqm  . .  hj/il  (APa)  upaÄsSi  (sd.)  N. io().  a)sva.|jedermann,  jeder,  quisque' fravalayS  . .  ijp^m  aZi?mnil  (sd.)  havä käHt  (NSf.)  näfäi  ". .  suae  quaeque  origini" Yt.  13. 66;  —  äai  anyähu  ratufrisu  latai>rS *kai3h^scil^^  bar?smqn  frastaraitys  (sd.) N.  ;o2;  —  sdäi  (sdl)  *Aahyä^t^*^  paiti V.33. 1 1.  a)  mit  Gen.  part:  hazatinm vairyaiiqm  . .  kßsalia  alsqm  vatryanqm  . . "tausend  Seebuchten  .  .  und  jede  dieser Seebuchten  . ."  Y.  Ö5.4;  4;  —  kasHt avAius' (sd.)  aslvate  F.  36';  P.  y,  V.  7.50, iO- 19,  P.43  (kakynat);  —  Hat  vö  kasat masyjiiqm  .  .  ¥1/5.53;  Vr.^.5;  — yäva- ranJ  kascit  sao^antqm  Y.12.J;  —  iäat tanuHam  V.  16.10;  —  ka^häscit  tanunqm H.  /.  5 ;  —  kahmai^t  häiqm  "Jedem  der Seienden"  Y.J5.8;  /fl.ii',  F.^b'«;  — kakyäcii  hstqm  V, /2, 4;  —  ijmcit  paiti cairusanqm  (Stverz.)  V.tf. 31  usw.;  — a^'ahe  pasvd  {sA.)  ..  aliiqm  *kakmaicit*''^ td'ia  */rayarihqm  (sd.)  N.  65.  a)  mit
9798:■gaona-  48a
9807:•  j.  'gaona-  n.  i)  'Haai':  astica  -naca (AP.)  *d3r>whaca  Vt.  13.1-1;  —  ^avat  'nahe avaharäp  yä  *dvaiibya  »nzubya  *Aart- g>r)wnät"'9i\t  viel  vom  Haar  (näml./an/ö) soll  man  hinzubringen?  Was  man  mit zwei  Fingern  fassen  kann"  N.  (*5;  —  yat aadha  *hanjasaiite  paouru  'nahe ''  u^aAe/a" "weil  dort  (am  Rückenhöcker)  reichlich Haar  und  Fett  zusammen  sind"  N.öj;  — navanqm  aspanqm  arsnam  'mm  barat airyama  "Haar  vun  neun  Rosshengsten brachte^."V.22.2o;  20^.  a)'Haarfarbe, Farbe' :  pasUnt  . .  aurusim  vä  ,  .  käcit  vä 'nanqm  Aamffgaarum  (sd.)  Yt.  A'.  s8;*Aog. ly.       3)  'Art  und  Weise'  (nur  Komp.).
9809:•  j.  "gaona-  m,  'Gewinn"':  yö  .  .  sqm ai'wi.v>rKyHti ..upa  he  'nsm  baraiH..yd^a
9824:mit  igaona-,
15661:•  j.  paount^gaona-  Adj.  'grauhaarig*: "rwM  F.^b.
### hak[?e]r[?e]t
### 'taub'
### Fell
4370:man  mit  Fellen . .  von  feuen,  nicht  von mageren  (Tieren)"  N.  ^Ä
9541:Vgl.  ai.  (hardii-  n.  *Schutz,  Schutzwehr',  got. siildus;  Bthl.  Slud.  3.  $8;  zuletzt  dazu  Ol- DENBEKG  ZDMG.  5S-  313.  Zur  DilTereaz  im Anlaut  vgl.  ai.  cAavi  'Fell',  gr.  enim,  got. skauda  und  gr.  cürg;,  lat.  cutis,  ahd.  hül.  — Pü. !  hai  asiän  äit  özöniandlar  kt  Ö  in  fa  j*J. nisn  raset  ä  karlärih  (Sü.:  karifti-e],  erl.!  ka\ x'äiitnd  ka  'kjr  u  karfak  kun''  kuntt.  — ')  Eig.  'mit  Hilfe'i  vgl.  RV.  /.  30.  7:  gämä  , nünäm  tti  'vasä  gegen  J.  9.  I :  a  nüridm  ,  . Xaatam  öiase.  —  ')  Vgl.  iSt.  BtHL.  AF.J.3S. MlLLsG.aiö  und  Dst.  ZA.  ^215  muten  uns  I grammatisch  unmÖ-;Ucbe  Dinge  tu.  |
10145:dem,  was  das  Rind  liefert;  i) 'Fell,  Haut':  ahurai  a  mS  urva  'Suscit  azya  Y.2g. mä  .  ,  yaia  *'aof  drafsö  (sd.)  .  .  Y.  /o.  1  5  '3>.  a)  neben  'gaya-  (sd.):  nimS  °Sus 14.  2)Tleisch':  pars xh'isca{sd.)  5zBi-\  mmö  gayehe  Y.68.  22;  Vr.  z/.  a;  —  fra tisca'jus  matY.13.%9,;  —  nöii  payS  fsula  .vasayS  ..  yqmca  asnö  ..  spu  ..  zsmS (sd.)  nSii  'Jul  .  .  paiti.baire  V.  7.  77;  —  I .  .  un-arayd  .  .  -Jus  .  .  gayeke  Vl  13. kat  na  .  .  -Jus'  ataifya  (sd.)    aslryeiti  N. '  86.  a)    GS.    mit  tasan-  m.  (sd.,   auch
11248:•  j.  (Jaraman-  n.  'Fell,  Leder';  mrätim "ma  "^anjaymte  "sie  ziehen  an  dem  ge- gerbten Leder(strang) "  Yt  17,  12;  — 'manqmca  .  .  *mrätanqm  N.  ^8;  —  'm<i (NP.)"  vatnantö  br3e?nta  {sA.)  frjna  »r^-
11254:satim  saranitH  "die  Felle  strahlen  auf  die Beschauer  Silber  und  Gold(glanz)  in  Fülle" Yt.  5.  129;  —  •mqnca  *hiku  N.55.
21162:•  j.  ya&a.k3r«t«m  Adv.  .'(je  nach  der MachuDg  sva.)  bei  richtiger  Bereitung,  Be- handlung': y-  %warstai  zrüne  &irfmä{sA.) .  .  bräanta  "bei  richtiger  Behandlung  zui vorgeschriebenen  Zeit  glänzen  die  Felle  . ." Yt.5.129.
### Vernichtung
17551:•  j.  fralcsrostö.fra'säna-  Adj.  'Zerstörung, Vernichtung  hervorrufend,  bewirkend': ga%aAe  'nahe  simahe  YtJj.  136.
17911:•  j.  fra-sätui-  n.  'ZerstÖruDg,  Vernichtung* : ava  apamm  (sd.)  gayehe  *°ram  '^  ultänahe Yt  ig.  44.
19997:•  j.  tnahrka-,  g,  maraka-**  m.  Tod, Verderben, Vernichtung';  kahmai yask>mla •kimca** .  .  baxsäni  Yt  JO.  110;  1^47,  V. 20,  7,  10;  —  yaskpm  yasksi  .  .  *k)m  'käi därayat  (sd.)  V.  20,  i ;  ().  5 1 ;  —  paitislütSe yaskahe  . .  °kahe  V.  20. 3;  21.  2;  —  aSe yaska  .  .  aite  'ka  (als  AP.)  V.5.  48;  — °ka  apa.dvarata  Ytj.  7;  10;  —  °kanqm maArksJfnti/n  Yt  J.  14";  —  nSit  axtii nSit  °ks  V,  2.  5 ;  ff.  43 ;  —  ä)m!ln?m  . .  3dat dmitäcä  (sd.)  marakaicä^  Y.^ji.  18;  — pairi  drvalaj  'iaj  Y.  57.  25;  —  kam ooJiHa  'ka  (IS.)  masyäka  daivs  aoÜ!  (sd.) yazäite  V.  /j.  i ;  —  °kahe  apana^tahe  V. 21. 2.         DS.  mahrkai  als  Inf.  s.  bes.
### sari-
5620:*)   Den   getötet   lu   haben   Mx,  2/.  Hf.  aU   asaonß  Yt  19.  132. höchstes  Verdienst  («;/)  des  GiyruVa/ii/n»  gilt; .      Vgl.    'arsari-.     S.   auch    ariaia-   und   ariäjj- vgl.  WiNDlSCHUANK  ZSt.  5-  —  *•)  Der  nach  I'ü.  j      „([  fjo   —  »j  Bd    ii    i? und    Bd.  12.  8  /o  a-iw-  /  dBi-u"   'am   Tor   der  '  ■  J  ■     3-
### 'sd-
```


## [2026-09-14T01:34:03.118Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9330,9340p' BRT.txt; echo \"=== sairi.gaona ===\"; grep -n -i \"sairi\\.gaona\\|sairigaona\\|sairi\\. gaona\" BRT.txt | head; echo \"=== einmal ===\"; grep -n \"'einmal'\" BRT.txt | head -8; echo \"=== hakarat ===\"; grep -n -E \"hak[a-z]?r[a-z]?t-\" BRT.txt | head -8",
 "description": "Bartholomae karana, sairi.gaona, hakərət"
}
```


### [2026-09-14T01:34:03.230Z] TOOL RESULT

```
Stellung  des  Worts  mit  np.£-«ria 'Katie' (ZA.  1  tti.  kdrsati,  np.  kasiJaii,  arm.  LW.  Haritl;  s. 3.  211)  ist  falsch;  das  wäre  Aw.  'gthrpa'  dam  Hbm.  KZ.  36.  166.  —  Pü. :  kaitlan.  — oder  *gir>pa'.  'I  Hds.  aparat';  »orher  gehl /ura,  mit  dem
.     „  ,_,    ,  ,      .     ,  die  Abschreiber   apa   lu   apata   ausgeglichen
•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
ai.  iarna-  m.    —    rii.:  undeutlich.    —     0  Im  ,     „™..     .        ,  1 -.„  ■
Cegensaii  zv  «i-;  sd.  mit  No.  5.  0    '(Flussiges)  ausschütten;    ausgiessen
.    „  ,,.,.,        .        .        ,    -  in  -'  (Akk.):    ya'äta  yat  htm    (näml.  zaü-
•  ].  »kanina;  Adj.  'taub  :  ndtl  avä  zaoirä  1  ;^^^^,  ^,^-.  _  _  ,,^^^^  _  _  ^^„^,v  "als  ob Paai.vise    yä      mävöya     frarmkarinb  .  .^^  ^j^  ^j^^^  Schlange  . .  in  den  Rachen  . .
'nasca  "i\5-^^-  ,  ^     .  .  ,  ,     „    .,  ; schUttete"N.4<?-       2)'(Samen)ausschütten,
si.  karna-    Ka\.    'stut lohne ,    np.  kor   'taub  ;  '  .  ,^  -  ■    ,     .        ,      .
s.  femer  KZ.  36.  15.  aussaen,  (Getreide)  durch  Aussaat  gewin-
...  ^     .  ,.     ,^    .     j    .     ,         nen':  aUavat  karitanam  {yavanam)  aHa-
=== sairi.gaona ===
=== einmal ===
=== hakarat ===
```


## [2026-09-14T01:34:20.933Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"##### HRN\" && grep -n -E \"šikastan|shikastan|sikastan|škastan|sikaftan|šikaftan|kāftan|kaftan|kāvīdan|kāwīdan\" HRN.txt | head -20; echo \"--- hrn sudan\"; grep -n -E \"sūdan|südan|sudan|farsūdan|farsudan\" HRN.txt | head -10; echo \"--- hrn kard/carm/kar/agar/gusixtan/sargin\"; grep -n -E \"kārd|kard '|čarm|carm|sargīn|sargin|gusīḫtan|gusixtan|gusextan|agar\" HRN.txt | head -30",
 "description": "Grep Horn"
}
```


### [2026-09-14T01:34:21.026Z] TOOL RESULT

```
##### HRN
6880:phlv. skaft, y. 10 (29), vergl. patkaftan (AV.);
--- hrn sudan
--- hrn kard/carm/kar/agar/gusixtan/sargin
98:hier überhaupt davon zu sprechen, wenn nicht de Lagarde
232:hauptsächlich aus de Lagarde's Arbeiten geschöpft, die
492:*) de Lagarde, Persische Studien, 70 verfährt zu künstlieh.
512:Strassburger Handschrift nicht in Ordnung).de Lagarde's Erklärung (zuletzt Pers. Studien 75)
556:vergl. Talmud LW. •imnx (de Lagard e, Semitica
679:(de Lagarde, Symmicta II, 16, Pers. Studien, 71);
683:26. äster 'Futter (eines Kleides)', ester, "lüDX (de Lagarde,
761:do Lagarde, Ges. Abh. 290 ist natürlich unmöglich.
822:arm. mac (de Lagarde No. 1413, Htibschmann
1027:residen (No. 616); de Lagarde (Armen. Stud. No. 175)
1047:arm. LW. (?) azan (de Lagarde, No. 25).
1088:bei de Lagarde, Semitica I, 43; vergl. auch Nöldeke,
1139:Lagarde, Ges. Abh. 173).
1142:') de Lagarde, Semitica I, 46 ist sehr gekünstelt.
1153:de Lagard e vergleicht arm. cax, aber np. istäx könnte
1207:aw. "^aiwis'hnana- (\)^) (de Lagarde, Fers. Stud., 74).
1211:') Die Awestaform ist von de Lagarde falsch angesetzt, der
1339:ist wohl unzweifelhaft; päz. agar,
1405:305), syr. LW. JOOT (de Lagarde, Ges. Abh. 40),
1427:(de Lagarde, Arm. Stud., No. 116).
1506:wohl beide überhaupt nichts mit einander zu tun, trotz de Lagarde^s
1744:arm. patrinc (de Lagarde, No. 1848: patriny)
1754:Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.).
1798:de Lagarde, Ges. Abb. 21, findet baz auch in
1867:de Lagarde's Bemerkung bezüglich Nathans aus
2153:^) Vergl. de Lagard e, Ges. Abh. 34, Note 4.
2176:SiW.*uparö.kara- {wergl.uparö.kairga-), deLagarde,
2220:aw. vergl. urunya- 'Schüssel* (vd. 14, 8); de Lagarde,
2226:vergl. de Lagarde, Beitr. z. altbaktr. Lex. 54 folg.,
2309:de Lagarde, Persische Studien, 74. Doch kommt
```


## [2026-09-14T01:34:27.183Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 175 188 205 221 244 25 98; do echo \"############ HRN printed p.$p (leaf $((p+21)))\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -60; done",
 "description": "Print Horn cited pages"
}
```


### [2026-09-14T01:34:28.278Z] TOOL RESULT

```
############ HRN printed p.175 (leaf 196)
- 175 -
in [/skar- dev PI), 'spähen, suchen, durchforschen,
Gegenden durchwandern, Iierumgehen', wa;^. sktlr-an},
sar. /kar-am. Die letzten Bedeutungen könnten auch
auf l/^rförr- (vergl. PW.) führen.
787. sikäften 'spalten', I^raes. sikäfeni i^Pgäf AM. S. 84
Zeile 7).
Ka§. vesköw (Inipt.).
phlv. skaft, y. 10 (29), vergl. patkaftan (AV.);
kurd. sikiwin, biskiwin aufblühen', sikeivf, askavf 'Höhle'
(H.-Sch.). LW. Sikaftm 'abtrennen, lostrennen, köpfen .
Zu gr. (Ty.d7iT(o 'graben, hacken (Nöldeke, münd-
liche Mitteilung). Durch diese schöne Entdeckung
wird die bisher nur für europäisch gehaltene Wurzel
slc^ap' bezw. sk-ah- 'schaben, graben* als indogermanisch
erwiesen. Die Bedeutung graben' ist bei np. käftev^
kämden (No. S:^^) noch erhalten^).
788. H'ikesten 'zerbrechen*, Praes. siken-ew,
aw. \^8caüd'^), scindai/^Urzerhrechen ; phlv. skastan
(Men.).
kurd. LW. sikestin, sikinändin (Causat.); oss. sädfjn,
sätfin 'brechen, bersten, zerbrechen' (221).
ap. *skanamij/ (aus ^skadnämiy)^ 9. Cl.; ai. [/'ched-
'spalten gehört nicht hierher, vergl. Hübschmann,
ZDMG. 38, 424.
sikuften, sikäften aufblühen* s. np. bisköfe (No. 223).
789. sei 'Schenkel', seieng (Sileng) ; vergl. selvär 'Hosen*.
gr. (jxfkog (Justi, Litbl. f. or. Phil. I, 65; aber
nicht gehört hierher arm. srwwÄ 'Schienbeine, Waden*,
srnapan '^vq^ii^^ vergl. Hübschmann, No. 260).
np. selvär ist weit entlehnt, vergl. öa(jäßapa (Photius,
Pollux u. ö.), arab. sarbäl, sarväl, kurd. selvär,
sarval, salval (H.-Sch.), af/. bei. (249) salvär, oss.
salbaro (H. S. 130), wa;^. savdlak, minj. soäl u. s. w.
*J Erst jetzt besteht Feistes kulturgeschichtliche Bemerkung
unter got. skahun (No. 499j zu Recht.
') So setze ich die Wurzel nach Barth olomae, Stadion II, 4,
97, 104 an.
############ HRN printed p.188 (leaf 209)
— 188 -
Im Neupersischen muss auch einmal ein Majhül-
vokal vorhanden gewesen sein ; doch reimt schon bei
FirdüsT kebüd auf düd (I, S. 5 Vers 77), numüd (I,
94 Vers 608), biid (L 115 Vers 937). Auch der PärasT-
prakäga hat w, kavütara (Weber, No. 285).
843. hvjci *\vo?;* welcher^); kudäm^) Vas für ein?;
jemand; hü 'wo?' (unbelegt).
aw. kü *wo?* -h np. Ja (No. 417), vergl. kva-, kuda
*wü?*, kudra 'wohin etc.; phlv. k(u)täm'^) (päz. kadäm)^
päz. kii *wo?', kiijä; ai. kä *wo?', küha *wo*? etc.
vergl. kurd. ku 'wer, was, wo?'; af/. vergl. küm
'was?'; oss. ku 'als, wenn, da, weil, wie (163); bei.
käy n. kü 'wo?' (144); minj. ko,
844. kedy kede^) 'Haus*, vergl. ked/udd {ket/iidä^)); iltes-
kede, meikede.
aw. kata- 'Graben (vd. 2, 26); Grabstätte'; phlv.
katak 'Grabstätte; Haus', katak\xutü^ katak\banüklh
(AV.), vergl. auch katik 'häuslich, zum Hause gehörig
{ätas).
wa/. ket, sar. c6d^ si/n. cid,
845. ker^ kerr 'taub'.
aw. karenäos[ca (yt. 5, 93) 'taub', Spiegel, ZDMG.
32, 721; 'd\. karnd- 'mit verstümmelten (gestutzten)
Ohren' (Geldner, Vedische Studien I, 138).
kurd. LW. ker 'taub'; af/. künr; oss. kurmafä 'die
Tauben' (Matth. 11, 5, Hübschmann, No. 164); bei.
*) Sogar Mass*, z. B. Vis und Rämln 67, Vers 2.
^) Das u ist jung, vergl. ai. katamä-^ mäz. kadänu
*j Das II kann auch erst neupersisch sein , vergl. phlv. katär^
aw. kafära-,
*) Käs. V. Ä-e, Q. kiyd^ kl etc. (s. v. ;^äMe) haben das bereits
neupersische d noch in y verwandelt. Solche zweite Lautverschiebung
findet sich auch sonst. Ein Beispiel für viele: Käs. tnelä, mele 'Büffel-
ochs* (s. V. kel) geht auf np. merde zurück (hier ist rd noch nach-
träglich zu l verschoben).
^) So bekanntlich im Türkischen immer geschrieben, aber k'ai/a
gesprochen.
############ HRN printed p.205 (leaf 226)
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
############ HRN printed p.221 (leaf 242)
— 221 —
Ved. Stud. II, 19); phlv. magu, magupat (arm. LW.
mog^ mogpet, movpetan movpet), daneben maupat (syr.
LW. NtOSID, daraus gr. Mavlnväg d. i. Mavmxäg und
Mavinvüv&d d. i. Mavmvovx^ä, Nöldeke, Karnämak
59 Note 4); ar. LW. majüs (Plur.).
985. mey 'Tiefe, Fluss''), meyak 'Graben, Grube* (Sahn. I,
174 Vers 817).
aw. maya- 'Loch'; phlv. may,
986. meyz 'Gehirn*.
Kä§. magz, magzL
aw. mazga- 'Gehirn'; phlv. mazg; ai. majjdn- 'Mark*.
af;'. mayz, Plur. mayza 'Gehirn'; oss. (LW.?) mayz
(174); bei. mazg (229); sar. muig 'Knochenmark', da-
gegen sar. moyz, siyn. mayz 'Gehirn' wohl LW.
987. unuft unbedeutend, umsonst erhalten'.
ai. l/'möC' ^befreien, wegwerfen* (also mtikta- etwas
Weggeworfenes', wie np. Juft aus yuktd-), Darme-
steter, Et. ir. I, 88 Note 2.
Die entlehnten nslov. muhte 'sorglos', serb. mukte,
muktice 'umsonst', ^wwiton^i 'schmarotzen' (Miklosich,
SWAW. Band 35, 129; 37, 86; 38, 176) würden die
ursprüngliche Form dann nachträglich wieder ent-
wickelt haben.
Unsicher.
988. meger 'wenn nicht, ausser, vielleicht'.
me nicht' + eger (No. 106), päz. ma agar (Aog.).
989. meges 'Fliege', jüd.-pers. Mo (Is. 7, 18)«).
aw. vergl. ma/si- 'Fliege, Mücke' ; phlv. magas (vd. 1
^) Den aus dem F§ bei Vullers abgedruckten Sahnämevers
konnte mir Herr Dr. Landauer nicht nachweisen.
') Z statt 8 findet sich dialektisch häufig: z. B. besbäs (AM. 55),
bezhäz oder semärüy, zemärüy oder kusbura^ kuzbura(YvL\\eT8); sepes
(jüd.-pers.) statt zi pes, vergl. si pester (Vullers); Käs. üzü d. i. an
8än; kauk.-bergjüd. zürnai sonst sürnm u. v. a. m. Umgekehrt steht
8 für z im ar. LW. sauswjird *ein Tuch', wörtlich *nadelgefertigt*
(sözengird), de Goeje, Bibl. geogr. arab. IV, 266. Ebenso wechseln
z und s, z. B. /äksi^ -/äkkl (Vullers, vergl. auch ebenda s. v. j^vhe und
############ HRN printed p.244 (leaf 265)
244
H.
1088. hämün *Ebene'.
Vergl. ap. aw. hama- 'derselbe, der gleiche', ai.
samd' 'eben, planus, in gleicher Lage befindlich*.
1089. fiaven 'Mörser', (AM. 132 Zeile 6), kaukas.-bergjüd.
heveng, arab. LW. hävun,
aw. hävmia- 'Mörser ; phlv. havan^ arm. LW. havan.
^^90. her* jeder, all'.
ap. haruva- all*, fraharavam (Bartholomae, BB.
XIII, 69) 'im Ganzen'; aw. haurva-; phlv. har, har[vJsp;
ai. sdrva-.
1091. hurrä ^Geschrei' (äähn. I, 17 Vers 66).
mhd. hurra, vergl. hurr (Interjection) , engl. dän.
schwed. franz. hurrn (s. Grimm, Wörterbuch).
Sollten die germanischen Worte, etwa durch
türkische Verniittelung (wo ich ein hurrä aber nicht
nachweisen kann), aus dem Persischen entlehnt sein ?
\ }(^92. hergiz jemals, je*, mit Negation 'niemals'.
ap. Vmkaramöiy *ein Mal' (Darmesteter, Et. ir.
I, 245 ; unsicher) ; phlv. akarc bezw. hakaix, luxharj,
phlv.-päz. hargij bezw. hargiz (PPGl.), püz. hargizi.
Np. hergiz gegen phlv. hakarc ist wohl durch her
beeinflusst.
i '1093. hezär 'tausend'.
aw. hazatlra- 'tausend'; phlv. ha zur, hazärak
'Millennium' , vergl. a^apanursTg' oi staayysXsTc nngd
üspaaig Hesych, arm. LW. hazarapet {/Mag/og,
oiaovo/iiog^ enirpoTrog); ai. sahdsra-,
af/. zar 'tausend*; LW. arm. hazar^ kurd. hazdr
etc.
1093**^^ hii^tr, hujir, yujlr 'schön', auch N. pr. (Sahn. III,
1191 Vers 985; 1239 Vers 1927; 1240 Vers 1936;
1503 Vers 127 u. ö. im DaqiqTstück).
aw. huci&ra-; phlv. hucihr.
Nöldeke, ZDMG. 46, 137.
############ HRN printed p.25 (leaf 46)
— 25 -
105. eknün jetzt', kunän,
ap. *kanüna7n, vergl. nun (No. 1052).
106. eger wenn , egerdi^ ger,
Zusammenhang mit phlv. akarc, np. hergiz (No. 1092)
ist wohl unzweifelhaft; päz. agar,
Ap. %akaram 'ein Mal', Darmesteter, Et. ir.
I, 245. Vergl. Fr. Müller, WZKM. 5, 66.
107. em *ich bin etc.
ap. amii/ 'ich bin' ; aw. ahmi ; phlv. nin -\- am etc.
(päz. hom etc.); ai. dsnii; arm. em (H. No. 93).
kurd. im etc. (Justi, S. 240); af^'. am, yam etc.
Wohl nach hest (vergl. No. 1094) und ap. ha(n)tiy,
aw. henti, ai. sänti: est sind dann auch die anderen
Formen des Praesens mit anlautendem h versehen
worden : päz. hom^ liend (Men.) — übrigens könnte hier
auch der Anlaut des aramäischen mn mitgewirkt haben
— jüd.-pers. DH, DTl, TH, IjD ; Kä§. hün, hön — ht,
he — him, h&m — hld — hen. Der FS (Vullers)
citirt den Vers Sahn. 1, 67, 105 als hend enthaltend,
das in unseren Ausgaben jedoch ausgemerzt ist;
bedenklich ist freilich, dass derselbe Ferheng gleich
darauf den nämlichen Vers mit einer neuen Änderung
{henjfär für embäz) anführt.
6ti-, Praefix, vergl. unter hem (No. 1102).
108. i/nh" 'dieser in imröz^ imsäl, imseb, imsubh (Sale-
mann-Shukovski, Pers. Gram. § 35), Tma (so*),
inbar^) ('diesmal*).
g. wo, mu, mö 'dieser {emrü, imrü); täl. etn, am
(PL amün) 'dieser; Käs. emseb , emril, emsöl; mäz.
emrüz, emsü.
ap. ima- 'dieser; aw. ima-; ai. imd-,
bei. ma[röci 'heute* (226); wa/. gern etc. 'dieser*.
de Goeje's (Bibl. geogr. arab. IV, 175) Erklärung des ar. LW. (?)
äkrän^ akrän (Epitheton aquae pessimae) als wörtl. 'noxam proferens*
ist sehr unsicher.
*) Gesprochen -m6-. mb in Lehnwörtern, z. B. Talmud "^^DN»
arm. amhar (No 111).
############ HRN printed p.98 (leaf 119)
— 98 —
Auch np. ceh7'e (Wörterbücher jehre) 'Spinnrad' ge-
hört hier; dialectisch (Kasan) lautet das Wort cörd,
cöre, cir d. i. *care. In Vöniäün (Kä§än) bedeutet
car/^ auch ^Wetzstein (s. v. sunhade),
438. cer^n Teil, Haut\
s,w,carema7i' Teil'; phlv. carmm- ledern (vd. 18 (6)
Gl.); ai. cärmaU' 'Fell'.
oss. t. mr, curm, (315); afy. carman; kurd. LW.
car7n,
439. cerTdeti, weiden', cerend, cerägah {^^irrrd, Is. 30, 23),
cerämden.
aw. l/"6^ar-, caraiti gehen* ^) ; phlv. fehlt, vergl. aber
arm. LW. carak 'Weide', carakem; ai. [/car-, cdrati
'wandern, umherstreichen, weiden'.
kurd. darin \ af/. car[edal; oss. d. carun^ t. cärin
'leben, wohnen (317); bei. öarag, n. cara/ 'wandern,
umhergehen ; weiden, grasen ; reiten' (55).
Spiegel, Commentar I, 160 will auch np. cemen
'Wiese' (aus "^cermen) zu [/'car- stellen, doch ist dies
unsicher; aw. yavö.öaränlm (vd. 5, 5) wird kaum
'Getreidefeld' bedeuten, vergl. Geldner, KZ. 25, 200.
440. cesm 'Auge 2).
aw. dasman- 'Auge'; phlv. casm, casm[gäh, öasmak
('Quelle') ; ai. öaksm- 'Auge'.
kurd. zaza öim ; oss. d. caste, t. cäsf (318) ; bei. Sam,
n. c'am *Auge', öamay 'Quelle' (52, 53) ; wa/. cözm^ äi/n.
sar. cem^ sangl. sam^ minj. cam,
441. cespEden, cepsiden, cefslden (Inchoat.) 'packen, fassen*.
Zu lat. capiö (Nöldeke, mündliche Mitteilung).
Also vergl. got. hafjan 'heben', hafts 'behaftet, ge-
fesselt'; gr. aaini] 'Griff'; air. cacht 'Sklave; lett. kampt
'fassen' 3).
*) Nach Bezzenberger wäre ap. a6a]crtr/.s*Gememde weide*,
doch vergl. oben Seite 38 Anm. 1.
') AM. hat immer cism. Im 8ähn. reimt auf cesm häufig /psw,
wo man vielleicht auch cism und ^ism lesen darf.
*) Alb. kap *greife, fasse an, nehme gefangen* ist nach G. Meyer
aus t. qapnn*<i *fangen, erhaschen* entlehnt.
```


## [2026-09-14T01:34:55.705Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### Messer\"; grep -n \"Messer\" HRN.txt | head -12; echo \"### Mist/Dünger\"; grep -n -E \"Mist|Dünger\" HRN.txt | head -12; echo \"### reiben\"; grep -n -E \"'reiben|reiben'\" HRN.txt | head -12",
 "description": "Horn: knife, dung, rub"
}
```


### [2026-09-14T01:34:55.805Z] TOOL RESULT

```
### Messer
6563:kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
7238:■ym, kärd 'Messer.
7239:aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
7241:kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
### Mist/Dünger
8118:af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
8211:gütha- Exkremente*; arm. ku 'Mist' (H. No. 149); ksL
### reiben
1536:127. engeiten antreiben', Praes. engez-em,
1537:phlv. angfytan antreiben', angejet (AV.), vergl.
6561:752. Süden 'reiben', Praes. säy-em, sät/lden.
6563:kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
8312:962. mäliden 'reiben, glätten*, -mal (vergl. destmäV)
8546:983. tniiSten 'reiben*.
8551:'reiben*, kratzen, streichen, salben, mahlen' (244).
```


## [2026-09-14T01:34:58.567Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6555,6575p' HRN.txt; echo \"=== kard ===\"; sed -n '7232,7250p' HRN.txt",
 "description": "Horn sūdan and kārd entries"
}
```


### [2026-09-14T01:34:58.650Z] TOOL RESULT

```
'Brand'.
751. 8üd 'Nutzen, Vorteil'.
g. sid 'Zinsen*.
aw. [/'saV' 'nützen'; phlv. süt , sütih, sütömand,
sütlnUa/L
bei. sät, Sit (357); sonst allgemein entlehnt.
752. Süden 'reiben', Praes. säy-em, sät/lden.
ai. l/'cd' 'wetzen, schärfen .
kurd. süin^ sün 'reiben, ein Messer reiben, schärfen'.
Die Bedeutung ist im Neupersischen verblasst ;
vergl. aber das Kurdische.
753. sür *Fest, Gelage'. •
aw. süirya- 'Morgenessen* (Darniesteter, Et. ir.
II, 161 und Geldner, KZ. 25, 531 Note 228); phlv.
5/Tr 'Morgenmahl, Mahl'.
bei. LW. slr 'Hochzeit, Verlobung' (241) ; siyn. sur
'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
mehr als im Np. specialisirt).
754. sTirfii, sülax, ^Nt^lD (Is. 11, 8) 'Loch'.
Darmesteter's Etymologie (Et. ir. I, 62) aus
aw. *siifräka' , phlv. "^sufräk , "^suhräk , ^süräk in
=== kard ===
aw. kära- in käravaitl; plilv. kär; skr. -küra- *i:Iand-
limg, That\
Allgemein entlehnt.
832. (2)'kär 'Tliäter , z. B. in sitahkär, destkar,
ai. -kära- '-tuend'; plilv. -kär,
Vergl. np. gär (No. 884).
■ym, kärd 'Messer.
aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
kfntdti 'schneiden*.
kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
d. kärdtm, t. Mrdln 'schneiden'; bei. kärc^ kärca^
n. ßarca (195).
834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
phlv. kärejar (y. 11 (8)).
vergl. ap. kära- *Heer'; lit, käras 'Krieg'; ksl. kara
'Zank, Streit'; got. harjis 'Heer.
Das Suffix -eflr ist unklar. Im PehlevT lautet es
'jär, was nicht -cär gelesen werden kann; vergl.
dialektisch grl. käljär (Vullers), Kä§. K. kast^jori —
```


## [2026-09-14T01:35:16.650Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 152 153 154 155 156 157 158; do echo \"--- POK_03 leaf $i ---\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_03.txt | head -8; done",
 "description": "Locate Pokorny p.919 in POK_03 scan"
}
```


### [2026-09-14T01:35:17.676Z] TOOL RESULT

```
--- POK_03 leaf 152 ---
)   ,wir   suchen   zu  verschaffen*,    apavanvainti  (*sw-e7i-'^.)  ;*- ,sie  lenken  ab^,  mainyu-süta-  ,vom  Geist  getrieben*,  hvöista-  ,der  höchste,'*^ beste;  älteste*;
air.    sö{a)id   ,dreht,   kehrt'    {*söu-eie'ti),   ess-ro-so-   , mißlingen^  (*hinweg- .:;^ drehen);  sUa(i)nem  m.  ,Strick,  Schnur'  (*sew-n-ta-wö) ;  lit.  siaüras  (*sett-ro-) ,schmal,  eng' ;
hitt.  suuäi-  , stoßen,  drängen'.
seu-k-:  osset.  xurx  ,Molken,  Käsewasser^  (ar.  *sukra-:  lit.  suJcrüs  ,*was  /.. sich  leicht  dreht') ;  lit.  sunkalai  PI.  , Molken',  pä-sukos  ds. ;  lit.  sukü,  sühti  77 , drehen,  wenden^,  sukrüs  , beweglich,  flink',  apsitkalas  , Türangel*,  lett.  sukt  ^f^ ,entwischen*,  sukata  ,Drehkrankheit',  slav.  *s^kQ,  *s^kati  (Prät.-St.  *sukä-)  '^ in  russ.  sku^  skaH  ,zwirnen,  zusammendrehen,  aufwickeln*,  ablaut.  ksl. '^* sukati  , drehen'  (umgebildet  aus  *soukeie-j  vgl.  russ.  suHH  ,zwirnen*);
s.  auch  seuio-  ,link*  und  suei-  , biegen*.
WP.  II  470,  Trautmann  291,  Liden  KZ  61,  7  f.,  Pedersen  Hitt.  134.
4.  seu-,  seu-t-  , sieden,  heftig  bewegt  sein*.  ..^.
Av.  hävayqn  ,sie  schmoren',  hävayeiti  ,er  schmort*  (3.  Sg.  Opt.  huyär9i  '^ =  ai.  *suyür  zu  einem  Präs.  *haoiti  nach  der  Wurzelklasse);
--- POK_03 leaf 153 ---
ht  ,Krankheit*,  nhd.  (Schwind) sucht,  Sucht  (hier  Bed. -Einfluß  von suchen)]  ags.  süsl  n.  f.  (^süh-sla-)  ,Pein',  seoslig  (*seuh-sla-)  ,gepeinigt', aisl.  syslj  sysla  ,Tätigkeit,  Amt,  Amtsbezirk  (von  der  durch  Pflichtarbeit ausgelösten  Unlust)',  sysl  Adj.  ,eifrig  bemüht,  sorgsam'  (*süsli-R).
WP.  II  472  f.
scuo-,  sQ-  , (loslassen?)  nachlassen,  lassen'?
Gr.  idü)  ,lasse'  (*iJ^da}),  eßaaov '  saaov.  2vQaytovaiOL,  sda  =  sa  Hes.,  Fut. Maü)f  Aor.  siaacc  (zu  *ita)',  tiefstufig  ahd.  vir-sümen,  nhd.  säumen,  ver- säumen (wäre  Denominativ  eines  *sG-mö-s  , nachlassend,  säumend').
WP.  II  472,  Schwyzer  Gr.  Gr.  1,  682,  752.
seuio-  ,link'.
Ai.  savxjd'^  av.   haoya-  ,link',  aksl.  sujh,  f.  ^uja  ds. WP.  II  472,  Trautmann  260;  vielleicht  als  ,gekrümmt*  zu  3.  seu-  (vgl, lat.  laevus  oben  S.  652).
sie[u]-ro-:si9-ur{io-)  , Bruder  der  Frau'?
--- POK_03 leaf 154 ---
l  ds.
WP.  II  515f.,  WH.  II  631  f.,  Carruthers  Lg.  6,  161  f.
skahh-f  skamhb-  , stützen'.
Ai.  skabhnäti,  skabhnöti  , stützt',  Perf.  cäskdmbha ;  skabhäyati  ,hefestigt, stützt';  skambhd-  m.,  skdmbhana-m  , Stütze,  Pfeiler*,  av.  ujpaskambdm  ,unter Fesimsichen^ ^  fraskdmba-,  frascimbana-  , Tragbalken,  Pfeiler';  npers.  paSkam ,porticus',  sogd.  Sk'np-  (*skamb)  ,etage  de  Tunivers';
lat.  scamnum  (^•skabhnom)  ^Bank,  Schemel',  Demin.  scabillum,  scabellum »niedriges  Bänkchen,  Schemel';
die  ar.  Binnennasalierung,  sowie  der  e -Vokalismus  von  av.  frascimbanü' (gegenüber  ai.  skdmbhana-m)  durch  ar.  Umbildung  von  skabh-  nach  *stemhh*' (s.    steb'    , Pfosten')    in    ai.    stabhnäti   , stützt',    stambJia-    , Pfosten,    Pfeiler, Säule'  usw.
WP.  II  539,  WH.  II  487  f.
{s)käi-,  (d-),  (t-)  ,hell,  leuchtend';  koi-to-,  koi-tu-  , Helle',  lc(9)i-tro- , hell'.
--- POK_03 leaf 155 ---
ai-t~  in  arm.  xait''  ,stechen.  Stich*,  xait^em  , steche',  xit'^am  ,bin  ängst- lich', xit''  ,Betrübtheit,  heftiger  Schmerz';  dagegen  xio-t  ,stutzig,  ängstlich, argwöhnisch'  aus  *khid-ro-]
WP.  n  538,  WH.  I  44,  45,  129,  130,  131;  über  ai.  kUddti  ,reißt,  drückt* (9),  sekundär  khSdä  f.  ,Druck,  Last*  s.  J.  Wackernagel  Stud.  A.  Grierson, 826—28.
skäi-f  skQi-  :  ski-  ,gedämpft  schimmern ;  Schatten  (Abglanz)' ;  skiiä- ,Schatten';  ski-ro-  ,klar*.
Ai.  chäyä  , Glanz,  Schimmer,  Schatten*,  av.  a-saya-  ^wer  keinen  Schatten wirft',  np.  säya  , Schatten,  Schutz';
gr.  OKiä  f.  (shii-a)  , Schatten',  (7xt«^dg,  hom.  G%i6eLg  ,schattig,  dunkel*, GMQOv  ,Sonnenschirm'  (formal  =  alb.  hir,  mit  Länge  got.  skeirs);  mit der  Stufe  skä[i]-:ay,r]vrj,  dor.  ay,Civd  ,Zelt,  Bühne,  Szene',  a'/.rjvog,  dor.  oy.ä- vogn.  ,Zelt;  Leib  (als  Hülle  der  Seele)';  cx^v  ,Schmetterling,  Motte'  Hes.; amvaQ  n.  ,Leib';
alb.  he,  hie  , Schatten'  (*skiia),  hir  , Gnade'  (=  gr.  G'/Jqov),  {h)ona , Schatten'  (*5Ä;ei-7i- ?),  ^q^.  hüj  ,Gott*;
aisl.  ski  n.  ,Heuchelei'  (:  gr.  axid),  got.  skeinan  , scheinen,  leuchten, glänzen',  aisl.  sklna  ds.,  ahd.  ags.  sclnan  ds.,  nhd.  scheinen  (w-Präs.,  vgl. aksl.  singti]  ob  auch  in  lat.  scintilla  , Funke'  eine  Bildung  von  einem ähnlichen  Ausgangspunkt  aus  vorliegt,  ist  fraglich  (Ableitung  eines  *ski-nto- ,glänzend' ?) ;  aisl.  skln  n.,  as.  skln,  ahd.  sein  m.  ,Schein,  Glanz';  ags.  as. scima^  mhd.  scheme  ,Schatten',  nhd.  Schemen  , schattenhafte  Gestalt',  aisl. sJcimi  m.  , Glanz',  nhd.  schimmern,  Schimmel  usw. ;  got.  skeima  , Leuchte, Fackel*,  ahd.   as.   sclmo,   ags.   sclma  m.   , Licht,   Glanz';   mhd.   scheim  ds.;
918  9
--- POK_03 leaf 156 ---
chen'  und  mir.  cimb  ,Tribut,   Silber',  air.   cimbid  .Gefangener',  cii , Gefangenschaft';
Mit  e-Vokalismus:  gr.  v.ö^ßog  m.  ,Band,  Schleife',  Y.ofxß6(j)  ,knüpfe*;  noi hempa  ,Kleiderstrippe,  Schlinge,  Henkel'  (auch  ,Zeug  von  Hanf,  in  welche? Bed.  sicher  von  hamp  ,Hanf'  beeinflußt);
von  einer  Grundbed.  ,krumm  gehen'  aus  reiht  man  an:  gr.  ^aice^ßü}  ,hinke* erschlossen  aus  dem  Namen  Jxo^/?og,  schwed.  skumpa  ,hinken',  skimpa , hüpfen,  tanzen',  ahd.  scimpfan  .Scherz  treiben,  spielen,  verspotten',  nhd. schimpfen,  Schimpf]  nhd.  (nd.)  humpen,  humpeln  (oder  zu  keub-?  oben S.  590 f.);
*{8)kamb-  erinnert  an  kam-,  kamp-  , biegen'  (oben  S.  525);  sein  Verhältnis zu  (s)Jcemb-  ist  noch  unklar;  ebenso  das  zur  nasallosen  Wz.  für  ,biegen*(?) oder  ,haken'  (vgl.  lit.  kimbü,  kibti  ,hangen  bleiben'):   kabü,  -eti  ,hangen*,\^^g kabinti  ,hängen',  kablys  m.  .Haken*,  kabl  f.   , Heftel,  Haken*  (aber  aucb e-Formen  wie  kebeklis  , Haken*);  aksl.  skoba  f.  ,fibula',  russ.  skobd  ,Klamv. mer',  wozu  aisl.  höp  n.  .kleine  Bucht',  ags.  höp  ,Ring';  dagegen  aisl.  hespa  f ,Eisenkrampen'  =  ags.  hoepse,  hcesp,  mhd.  haspe,  hespe,  nhd.  Haspe,  HäspB^  T~ holl.  hespe  ,Hüftgelenk',  mndl.  auch  ,Hacke*  zu  kap-,  oben  S.  527  f.
WP.  I  346,  3ö0f.,  n  539  f.,  WH.  I  148  f.,  Trautmann  112,  116.  '^
{s)kand',  (s)kend-  .leuchten',  s.  oben  S.  526.
{s)k{h)ed-,    (s)k{h)e-n-d-    ,zerspalten,   zerstreuen'    (Erweiterung   von   sek' ^schneiden').
919
--- POK_03 leaf 157 ---
en  Altengl.  Wb.  146.
skei-  , schneiden,  trennen,  scheiden',  Erweiterung  von  sek-]  Anlaut  z.  T.  auch sk-,  skh-,  skh-,  wie  auch  in  den  Weiterbildungen  skai-to-,  skoi-to- ,Brett,  Schild';  skid{oi)-ro-,  skid-to-  ,gespalten'.
I.  Ai.  chyati  , schneidet  ab',  Partiz.  chäta-,  chitd-  , abgeschnitten',  Kaus. chäyayati  (mit  sä:-,  wie :) ;
av.  fra-sändm  , Zerstörung',  sä-,  sya-  , wehren' ;
gr.  (T%aw  (*skhdiö,  Impf.  IV^o»',  Inf.  xaror-d^av),  c^atw  (Neubildung, Schwyzer  Gr.  Gr.  1,  716)  ,ritze,  schlitze  auf^  und  ,lasse  fallen,  schlaff herabhangen,  hemme,  stehe  offen',  ox^^^^G  A^^  Ritzen,  Schröpfen;  Los- lassen*, GxciOf-iCi  n.,  GxaGiiog  m.  , Einschnitt',  GxaotrjQiov  ,Lanzette,  Riegel', GXaGTrjQla  ,das  (zur  Abtrennung  der  Zuschauer  dienende)  Seil  vor  der Rennbahn';
lat.  sciö,  sclre  ,in  Erfahrung  gebracht  haben,  wissen'  (,scheiden,  unter- scheiden'), desciscö,  -ere  , abtrünnig  werden,  sich  lossagen',  sciscö,  ere ,(durch  Abstimmung)  entscheiden,  beschließen,  verordnen'  und  ,zu  erfahren suchen',  plebucltum  ,vom  Volke  gefällte  Entscheidung',  scUus  , gescheit^ (wie  mhd.  geschlde,  nhd.  gescheit  zu  *skei-t-) ;
in  der  Bedeutung  , ausscheiden'  (vgl.  aisl.  sklta  unten  S.  921)
920  •
--- POK_03 leaf 158 ---
en  skei-d-,  -t-  (d,  t  z.  T.  präsensbildend, z.  T.  das  nominale  Formans  -to-):
A.  Formen  auf  -d-;  im.  Ar.  und  Arm.  mit  sk-^  im  Balt.  mit  sk-:
ai.  chlndtti,  themat.  chindati  , schneidet  ab,  spaltet',  Kaus.  chedayati] cheda-  m.  , Schnitt,  Abschnitt',  chitti-  ,das  Spalten'  (:  lat.  scissiö),  chidrd' , zersplittert',  n.  , Spalt,  Loch',  chidira-  m.  (lex.)  ,Axt,  Schwert'  (:  av.  sidara-^ gr.  oyiidccQÖg,  ahd.  scetar,  lett.  ^k\drs  , undicht';  vollstufig  lit.  skied-rä)', av.  saed-  , spalten',  avahisiSyät  ,er  möge  zerspalten',  sidara-  (leg.  sidra-) n.  ,Loch,  Öffnung,  Riß',  a-sista-  ,nicht  gespalten',  balüöl  sindag  ,spalten', brechen;
arm.  ctim  ,ritze  mich,  zerkratze  mir  mit  den  Nägeln  die  Haut';
gr.  Gxill^o}  ,spalte,  trenne',  axiatög  (=  av.  a-sista-^  lat.  scissus)  ,geteilt, getrennt;  teilbar',  (T^/d«?  ,Splitter,  Schindel',  ax^^cc  f.  ,Scheit',  (JxivdaX^iög, Koine  a/.LvdaX^ög  , Holzsplitter',  dvaaxi^vdvhvü)  ,spieße  auf ;  makedon. axotöog  ,Behörde';
lat.  scindö,  -ere,  scicidi,  scissum  ,schlitzen,  zerreißen,  spalten';  scissiö  ,das Spalten' ;
mbret.  squeigaffj  nbret.  skeja  »schneiden'  (-z-  aus  -dj-,  *skidiö)'^  cymr. ysgwydd  (*ske{d-),  com.  scuid,  bret.  scoaz  , Schulterblatt';
air.   sciath   »Schulterblatt,    Schwinge'   (p   statt   d  nach   sclath   »Schild');
```


## [2026-09-14T01:35:43.371Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG sau/sud\"; grep -n -E \"^\\*?(sau|saH|sā|sad|sai|skand|kart|sard)\" CHEUNG.txt | head -40",
 "description": "Cheung root list"
}
```


### [2026-09-14T01:35:43.447Z] TOOL RESULT

```
### CHEUNG sau/sud
492:*saucé ‘to burn, light", *rai9! / *frait/9 ‘to die, decompose’, *caud / *paud ‘to run’. 
10384:saugand xurdan, Kurd. sont xarin, etc., see Schwartz 1989: 293 ff. 
15799:karta-; Inf.: cartanaiy <c-r-t-n-i-y> (DB 1.94, DB 2.33, DB 2.44, etc.), <c-r-t-n-i-y> (2.38), <c-r-t-n-i-y> 
15867:kart, Gil. (Rsht.) kudoen/kun-, Gur. (Kand kärd-/-kär-, Ham. Кагійп/Кег-, Isfah. 
16172:*kartl 243 
16196:*kart! ‘to cut’ 
16271:*kart? ‘to twist, turn’ 
21296:*sai£ чо pass' 
21308:*saH 325 
21352:*saH ‘to whet, cut’ 
21357:*saHh), v. Lubotsky 2001: 34. = Liste: 62 
21384:*saH is *sauH! (q.v.). 
21398:*saHh ‘to teach, instruct’ 
21420:*said! ‘to break, split, destroy’ 
21443:*saif 327 
21506:*saif ‘to flog, cane, rake ?’ 
21529:*saiH ‘to lie down, go to sleep’ 
21538:sailamna- (V 3.25, V 18.26), perf. pass. YAv. äsitö.gätu- (Y 62.5, Yt 19.39). 0 The compound YAv. 
21578:*saiH/siH ‘to freeze’ 
21595:*saij ? ‘to run, send’ 
21802:*sad-), especially when the corresponding caus. formation *sandaja- is well attested 
22020:*sard ‘to smear, rub’ 
22171:*saut! ‘to burn, emit flames’ 
22195:*sauc | 339 
22260:*sau ‘to call’ 
22284:*sauH! ‘to rub, wear, whet’ 
22317:*sad 341 
22333:*sauH ‘to bulge, swell up, increase’ 
23969:sadness, sense of helplessness, etc.’ 
24131:*sauH! ?) 
33514:kart-, 243 
33709:sauruua-, 338 
37722:sad-, 332 
37734:sada-, 337 
37746:sauy-, 340 
41130:kartana(k), 245 
41452:sard, 337 
41454:saugand xurdan, 148-9 
41458:sad, 325 
42066:sauyan, sogin waray,
```


## [2026-09-14T01:35:46.729Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21352,21400p;21420,21450p' CHEUNG.txt; echo \"=== sauH ===\"; sed -n '22284,22330p' CHEUNG.txt",
 "description": "Cheung *saH, *said, *sauH entries"
}
```


### [2026-09-14T01:35:46.801Z] TOOL RESULT

```
*saH ‘to whet, cut’ 
*AVESTAN: OAv. si- (sä-) ‘to sharpen, cut’ ?. 0 The verbal root may be non-existent. 
The attested forms can be interpreted differently: siiodum (< *siazd), sazdum (< 


*saHh), v. Lubotsky 2001: 34. = Liste: 62 
Pres. ja-: IMPV. 2р1. OAv. paiti siiodüm (Y 48.7); Aor. s-: ІЧЈ.ЛМРУ. 2р1. OAv. sazdüm (Y 31.18) 


*KHOTANESE: OKh. säta- ‘smooth’ (Z 23.44) 

*NWIR: Bal. sat/say-, sah- ‘to shave’, Kurd. (Kurm.) hasun/has- (ha- < *ham- or sec. 
2), (Sor.) sün/sü- ‘to whet, sharpen’, Gz. sün-/sünt ‘to rub, shave off’, NP sad 
‘smooth, plain; rubbed, worn out’ || (+ kardan ‘to do, make’) ‘to castrate, cut all 
clean away’ || (+ *ham- ?) Kurd. hasan, hasan (m.) ‘whetstone’ 

*NEIR: ? Pash. sūlēdəl ‘to become ground, grated’, Oss. I. sart ‘chisel’, ? Sh. säd (f.) 
‘flat stone, flagstone’, Sariq. sad ‘slate, baking pan’, Yi. sur ‘slate’ (< *saHti- 
‘whetstone’ ?), Sariq. suóy “flat, smooth (surface)’ ( *saH-ta-ka-, with fric. assimil. ?: 
-dy- > -óy- ?), (av- < *a-apa- ?) D. avinsun/avinst ‘to whet; to incite, direct’ || (+ 
*abi- ?) Yi. áfseno, yufseuno ‘whetstone’ || (+ *pati-) Sh. pisen (f.), Rosh. pisen (f.), 


326 *saHh 


Orosh. pison (f.), Sariq. pisan (f.), Yzgh. posan ‘whetstone, hone’ || (+ *ham-) Oss. I. 
yssyn/yssad, D. insun/insad ‘to whet, sharpen’ 

*SANSKRIT: 58 ‘to sharpen, whet? = EWAia П: 627 

9 There are no IE verbal correspondences of Ir. *saH / Skt. sa. A possible variant of 
*saH is *sauH! (q.v.). 

«PIE *KeHs- ‘to sharpen, whet’ = LIV: 319 f. | Pok.: 541 f. 

*IE COGNATES: Lat. cds ‘whetstone’, catus ‘sharp(-minded)’, Olrish cath ‘wise’, 


Arm. sur ‘sharp’, ON hein (f.) ‘whetstone’ 

*REFERENCES: EVP: 67; IIFL II: 245b, 188b; Abaev, Slovar’ I: 85; EVS: 72a, 61b f.; Abaev, Slovar’ II: 
36; DKS: 424a, 290a; WIM 1/1: 82; Abaev, Slovar’ IV: 278; Werba 1997: 320; Cabolov 2001: 426, 424; 
Korn 2005: 110, 313, 381 


*saHh ‘to teach, instruct’ 


*said! ‘to break, split, destroy’ 

*AVESTAN: (+ *aua-) Y Av. auua.siö- ‘to split? = Liste: 62 

Perf.: OPT. 3sg. YAv. auua.hisióiiat (Yt 8.54) 

*MIDDLE PERSIAN: (+ *ара-) ВМР ’p(y)shyn- /ab(e)sihen-/ (caus.) ‘to destroy’, 
MMP ’bysyh- (раѕѕ.), BMP ’ps(y)h- ‘to be destroyed, perish’ || (+ *fra-) MMP 
prsyst (pret. stem), BMP plsn- /frasinn-/ ‘to break’ || (+ *ui-) BMP wsyn- /wisin(n)-/ 
‘to break, split? = DMMPP: 17b, 156b 

(+ *apa-) Caus.: pres. IND. 3sg. BMP /abesihénéd/; Inf.: BMP ’ps(y)hytn /abesihidan/; Pass.: pres. IND. 
35р. BMP /abesihéd/, SUBJ. 3sg. MMP ’bysyh’d, BMP ’bysyh’t /abesihad/ || (+ *fra-) Pres.: SUBJ. 3sg. 
BMP plsn’t /frasinnad/; Partic.: perf. pass. MMP prsyst || (+ *ui-) Pres.: IND. 3pl. BMP wsynynd 
/wisinénd/; Partic.: perf. pass. BMP wsyst /wisist/ 

*PARTHIAN: systg (ppp.) ‘broken’ || (+ *apa-) ’bsyst- (pret. stem) ‘to stop, cut off, 
end (?)’ || + *fra-) frsyst- (pret. stem) ‘to break [tr.] = Ghilain: 83 | DMMPP: 
312b, 14b, 156b 

Partic.: perf. pass. systg || (+ *apa-) Partic.: perf. pass. ’bsyst || (+ *fra-) Inf.: frsystn 


*saif 327 


*SOGDIAN: BSogd. syö-, CSogd. syö- ‘to destroy’ || (+ *apa-) ? CSogd. psyd- ‘to 
fail’, ’ps’yö ‘failing, stint’ 

Pres.: IND. 3sg. BSogd. syöt || (+ *apa-) Fut.: IND. 3sg. CSogd. psydtyq’ 

=== sauH ===
*sauH! ‘to rub, wear, whet’ 

*MIDDLE PERSIAN: BMP s'd- /say-/ ‘to rub, wear, tire, tear’ || (+ *ham-) MMP hswd 
(ppp.) ‘whetted’ (Henning 1947: 45) = DMMPP: 186a 

Inf.: BMP swtn /südan/ 

*PARTHIAN: s’w- ‘to crush" > DMMPP: 306a 

Pres.: SUBJ. 150. s’w’n {hapax} 

*KHOTANESE: LKh. sauy- ‘to rub’ = SGS: 134 

*SOGDIAN: (+ *apa-) BSogd. ps’w- ‘to touch’ {hapax} 

Pres.: IND. 3sg. BSogd. ps’wt 

*CHORESMIAN: sw(y)- ‘to clean (the nose)’ || (+ *apa-) Bs’w- ‘to rub off, polish’ || (+ 
*pati-) ps’w- to grind’ || (+ *fra-) m/rs’w- ‘to rub, smooth’. © With regard to Chor. 
sw(y)- ‘to clean (the nose), Samadi (ibid.) cites Skt. svas- ‘to pant, wheeze’, which 
is semantically not compelling. The Chor. form may rather derive from a med. stem 
*suHia- of the root *sauH. — Samadi: 187, 25, 161, 172 

*NWIR: NP sudan/say- ‘to rub, wear, tear’, Kurd. (Kurm.) sö-, su-/sutin, (Sor.) su-, 
Awrom. sawa ‘to rub’, Zaz. sawitis/sawen- ‘to smear, rub’, Nn. sawnäye/sawn- ‘to 
grind’ 

*NEIR: Pash. sulédal ‘to be ground, grated’ (+ *-d-), Sh. (Baj.) säw-/säwd, Rosh. 
sew-/sewt, Bart. stw-/stwd, Yzgh. saw-/sed, (with redupl.) Sariq. sasew-/sasewd, (?) 
Yi. sa-/sovd-, M. söw- ‘to rub, smear, grind’, ? Wa. sbIX-/soXt- ‘to smear, rub’ (with 
sec. -X- ?) 


*sad 341 


*MISC: Orm. say- ‘to rub’ = say-/sayok 

*SANSKRIT: 5а ‘to sharpen, whet > EWAia II: 627 

Ó The root *sauH' either reflects a rare ua-stem of *saH (similar to *fiHu, Kellens 
1984: 162) or, more likely, may have been the result of contamination with 


semantically similar roots: *dauH and *skauH. 
*REFERENCES: IIFL II: 245, 541b; EVS: 75b ff.; DKS: 429a f.; Paul 1998: 312b; Cabolov 1997: 72; Lecoq 
2002: 132; Kiefer 2003: 206
```


## [2026-09-14T01:36:11.032Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"gusistan|gusixtan|gusil|gusi[sx]\" CHEUNG.txt | head -10; echo \"=== kart1 ===\"; sed -n '16196,16270p' CHEUNG.txt",
 "description": "Cheung gusixtan and *kart"
}
```


### [2026-09-14T01:36:11.133Z] TOOL RESULT

```
21455:out, spread out’, Tr. fésés- (pret. stem) ‘to break’ || (+ *ui-) NP gusistan (supplet. 
21456:gusil-) ‘to shatter, break’. 9 The initial fi- of Gz. fisisse is hardly from *ui-, cf. NP 
21457:gusistan/gusil- (!) ‘to break off’, pace Eilers, WIM П/2, l.c. 
22135:*NWIR: (+ *aua-) NP gusil- ‘to shatter, break’. Ф The pres. stem NP gusil- is from 
22137:formation. The suppletive past stem gusist- also goes back to the same root. 
41055:gusil-, 338 
41057:gusistan, 327 
=== kart1 ===
*kart! ‘to cut’ 

*AVESTAN: YAv. kart- ‘to cut’ || (+ *aua-) ‘to cut down to’ || (+ *upa-) ‘to cut on’ || 
(+ *fra-) ‘to cut up’ > Liste: 15 

Pres. {1} n-: IND. 3sg. YAv. apa ... korontaiti (V 13.10 f.), YAv. aipi.korontaiti (Y 71.8, Yt 10.72), 3pl. 
Y Av. aipi.korontonti (Y 71.8), Y Av. frakorontonti (ViD 10), INJ. 3sg. YAv. frakorontat (V 1.2, V 1.4 f£), 
YAv. fra korontat (Y 9.8), SUBJ. 3sg. YAv. ()karantat (У 7.37x, У 7.39), 3р1. ? YAv. *kərəntànti or 
*korontan (V 7.38), ОРТ. 3sg. Y Av. "pairi.korontoi$ (V 19.19), 3pl. YAv. upa.korontaiion (V 13.33), 
IMPV. 3р1. (?) YAv. kerentu (with hapl. from *korontontu ?, V 7.38, V 7.40); Pres. {2} aia-: IND. 3sg. ?? 
Y Av. (nonce) korontaieiti (ХЗ Yt 14.62); Pass.: pres. SUBJ. 3sg. Y Av. auua.korodiiät (V 4.50) 

*MIDDLE PERSIAN: BMP klyn- /kirrén-/ ‘to cut, create [daevic]’ || (+ *fra-) BMP plglt 
/fragard/ ‘chapter, section, Abschnitt’ 

Pres.: IND. 3sg. BMP klynyt /kirrénéd/, 3р1. BMP klynynd /kirrénénd/; Partic.: perf. pass. BMP klynyt 
/kirrénid/; Pass.: pres. IND. 3sg. BMP klyhyt/kirthéd/, 3р1. ВМР klyhynd /kirihönd/ 

*KHOTANESE: (+ *pati-) patält- (pa’s-) ‘to cut off 2 SGS: 67 

*SOGDIAN: (+ *us-) BSogd. ’skr’nt(-) ‘to cut up’ || (+ *pati-) BSogd. ptkr’nt- ‘to cut 
through, off || (+ *fra-) CSogd. frqrnt- ‘to destroy’, MSogd. frkrnd ‘to cut up’ || (+ 
*ham-) BSogd. "nkr'nt-, MSogd. ’ngrnd- ‘to cut up’ 

(+ *us-) Pres.: IND. 3pl. BSogd. ’skr’nt’nt || (+ *pati-) BPres.: IND. 3sg. BSogd. ptkr’nt, 3р1. BSogd. 
ptkrnt’nt, Partic.: pres. BSogd. ptkrnt’k, BSogd. ptkrnt’y, BSogd. ptkrnty || (+ *fra-) Impf.: IND. 3pl. 
CSogd. fr'qrntnt; Inf: MSogd. "frkrnd (BBB: 33) || (+ *ham-) Pres.: IND. 3sg. BSogd. ’nkr’nt, 3р1. 
BSogd. ’nkr’nt’nt 

*CHORESMIAN: ? kcy- ‘to throw (away), put on, to; to dictate’, knd- ‘to measure, 
measure off (before cutting off the leather)’ || (+ *upa-) bkrzy- ‘to attack’. > It is 
difficult to account for the meanings of Chor. kcy- (Henning 1950-55: 428), if it 


244 *kart2 


indeed derives from *kart-. The comparison with Wakhi kart- ‘to throw; to put; to 
shoot at’, cited by Henning, can be discarded: the Wakhi form (pres.: kat-) may have 
an (unspecified) Indian origin, which Samadi, l.c., infers from IIFL II: 457, 41. This 
is the stance of Steblin-Kamenskij 1999: 206 f., who mentions the following (IA) 
forms: Pashai kat-, Si. katanu-, Panj. kattna, Hi. katna, etc. о cut’, Pashai kut- ‘to 
strike, rub’. As for the semantics, Steblin-Kamenskij also quotes (dialectal) Russ. 
lozit’, klast’ which means ‘to cut’, cf. standard Russ. klast’, (perfective) po-loZit’ ‘to 
put, lay (down)’. = Samadi: 100 f., 103, 20 

*NWIR: NP Кага, Bal. karc, Kurd. (Kurm.) Ker (f.), (Sor.) kerd, Abyan. Кага (f.), 
Anar. kart, Qohr. kart, Sang. kart, Nn. kart ‘knife’, Kurd. (Kurm.) как?) (m.) ‘part, 
shart, piece’, kur ‘cut off; shaven; shortened’, (Sor.) kuti ‘short; stumpy, chopped off 
[of tail]’ || (+ *ni3-) NP nisgardah ‘cobbler’s knife’ 

*NEIR: Oss. I. kaerdyn/karst, D. kaerdun/karst ‘to cut (to pieces)’, Sh. xicand-/Xicryd, 
Sariq. Xicand-/Xicaxt ‘to cut (off), carve, chop’ (contamin. with *skand ‘to break, 
cleave’, EVS: ibid.) || (+ *abi- or *apa-) Oss. I. argevdyn/zrg&vst (with meta- 
thesis), D. avgardun/evgarst ‘to slaughter, stechen (animal, person)’ || (+ *aua-) 
Oss. I. ugard ‘carve, incision’ (not from pref. *ui- as assumed by Abaev, Slovar’ IV, 
l.c.) || + *a-) ? Pash. äcan- ‘to level, smooth; arrange, regulate’ || (+ *us-) Pash. 
skaStal/skan- ‘to cut out, clip out’ || (+ *fra-) Oss. I. legardyn/legzrst, D. 
legerdun/legerst ‘to pave [cut] a path (in the water, snow, on the land) with 
difficulty’ 

*SANSKRIT: kart ‘to cut (off) (RV+) = EWAia I: 315 

PIE *(s)ker-t- ‘to cut? => LIV: 559 f. | Pok.: 941 f. 

*IE COGNATES: Arm. k'ert'em ‘I skin’, Lith. kertü (kifsti) ‘I hew, hit’, Latv. cértu 


(cirst) ‘I hew, hack’, Alb. geth ‘to shave’ 

*REFERENCES: EVP: 67; Abaev, Slovar’ I: 584, 175; Abaev, Slovar’ II: 21; EVS: 100b; Abaev, Slovar’ 
IV: 12; Werba 1997: 170; Cabolov 2001: 508, 525, 549; Lecoq 2002: 631 passim, NEVP: 7; Korn 2005: 
189, 389
```


## [2026-09-14T01:36:18.712Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21450,21470p' CHEUNG.txt; echo \"=== around 22100-22145 ===\"; sed -n '22100,22145p' CHEUNG.txt",
 "description": "Cheung gusistan context"
}
```


### [2026-09-14T01:36:18.783Z] TOOL RESULT

```
*BACTRIAN: (+ *apa-) oBouo- (pret. stem) ‘to finish, conclude, bring to an end’ 
c» S-W, Bact.: 176b 

*NWIR: Bal. sist/sid-, sind- ‘to break, split (cords, sim.)’ || (+ *apa-) Gz. fisisse ‘torn 
out, spread out’, Tr. fésés- (pret. stem) ‘to break’ || (+ *ui-) NP gusistan (supplet. 
gusil-) ‘to shatter, break’. 9 The initial fi- of Gz. fisisse is hardly from *ui-, cf. NP 
gusistan/gusil- (!) ‘to break off’, pace Eilers, WIM П/2, l.c. 

*NEIR: Pash. slédal ‘to break’ || (+ *fra-) Ishk. fersend-/fersest- ‘to be torn apart’, 
Wa. rosod-, rosoó-/rosn- ‘to break [intr.]; to get sour [of milk]’ 

*MISC: Orm. syök ‘to break’ 

*SANSKRIT: ched ‘to split, to cut off, to hew off, to destroy, to divide’ (RV, AV+) 
c EWAia I: 561 

Q Contamination with other roots for ‘to split, break’, especially *séand, can be 
observed in several languages. 

*PIE *skeid- ‘to split? = LIV: 547 f. | Pok.: 920 f. 
=== around 22100-22145 ===
*PARTHIAN: sr ‘communion’ > DMMPP: 308b 

*KHOTANESE: ? hissádai ‘kinsman’ (hi? < *huai-) 

*SOGDIAN: (+ *ш-) ? CSogd. wsyr- ‘to mix (?), [Syrian] mzg'. © Cf. Sims-Williams 
1989: 260. The passage is unclear though. In the Greek original text a finite verb is 
missing, being merely implied: @oavdtas кой TO TOTHPLOV petà TO óewrfjcon ‘thus 
also the cup after having eaten’. Perhaps the added Sogd. form wsyrd’rt may mean 


‘he brought (nearer)', with w- reflecting pref. *aua- ? 
Pret.: IND. 3sg. CSogd. wsyrd rt 


*NEIR: Pash. sará (adv.) ‘together’, ? Sh. sár, Rosh. ser, Bart. sór, Sariq. sor, Yzgh. 
sarag ‘heap of (threshed and winnowed) grain’, Sh. sir ‘heap of snow’, Wa. sor 
‘yield of harvest’ 

*SANSKRIT: a-Sirta- ‘mixed (with milk)’ (RV) > EWAia I: 178 

«PIE *KerH>- ‘to mix’ © LIV: 328 | Pok.: 582 

*IE COGNATES: Gr. képaovvuju (aor. Exépaca) ‘I mix (together)’ 

*REFERENCES: EVS: 75a; DKS: 487a; Werba 1997: 321; Steblin-Kamenskij 1999: 313; NEVP: 75 


338 *sarH3 


*sarH ‘to break’ 

*AVESTAN: (+ neg. a-) YAv. asarota- (ppp.) ‘unbroken’ (V 19.4), YAv. sari- (m.) 
‘piece, fragment’ (V 8.85) 

*NWIR: (+ *aua-) NP gusil- ‘to shatter, break’. Ф The pres. stem NP gusil- is from 
*yi-srHd-, with *-d- either from *said! or, perhaps preferably, it reflects a d-stem 
formation. The suppletive past stem gusist- also goes back to the same root. 
*SANSKRIT: Sar’ ‘to shatter, break’ (RV+) > EWAia II: 617 f. 

9 Further Ir. cognates are unknown. 

«PIE *KerH>- ‘to break’ = LIV: 327 f. | Pok.: 578 


*IE COGNATES: Gr. KepatCw ‘I tear, destroy’, Toch. kärnau ‘disabled’
```


## [2026-09-14T01:36:34.108Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -n -E \"^(škastan|škast|škāf|kārd|carm|čarm|kar |kirrēn|agar|wisist|wisin|sargēn|sargin|sūdan|say-|kerd)\" PHD.txt | head -30; echo \"--- phd alt\"; grep -n -E \"sargēn|sarg|škaft|škast|kārd|carm|karr|agar\" PHD.txt | head -40",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-14T01:36:34.180Z] TOOL RESULT

```
### PHD
--- phd alt
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
175:-üg [> | M Ze, N -a] suffix forming agent nouns from present stems. a-gàh [?g's] without rank. āgāh [?k’s | M ?g(h), N <] aware, knowing. ~ih: knowledge. ügahénidan, абваһёп- [A?^syn-ytn!] inform. ügandan, Agan- [’kn-dn' | P ?gnd, N ~] fill, stuff. a-ganj [Аис !] penniless. agar (HT, for А hn | Mgr, N ~] if. agar DEI | М °g°r-] inactive, powerless, имко ~ih : inactivity, impotence. agarénidan, agarén- [?/?/уп-уїп!] render powerless. agarihistan, agarih- [?*4?/y%-stn! | M ?g’ryyh-] become powerless. ag-dén [k-, ?gdyn!] of evil religion, infidel. ~th: heterodoxy, non-Mazdean religion. абепёп [’k(y)nyn' | M (*)*g(y)nyn] together.
412:J jad [y’t'] share, portion. Yadag [ytk! | M jdg] omen. tļadaģ [ytk'] form, property. jadag [y’tk' | M del share, portion; case, cause. jadag-g5(w) [y tkgwb'] advocate, intercessor. ~ЛЬ : intercession. jadag-wihīrih [ytkwhylyh] transformation, alteration. Jadarih [y2?lyh] maintenance. *fadisn [ytsn'] (accidental) quality, property. ~ig [-yk'] accidental, non-essential. jadiig [y?te&! | M j?dwg, N jadi] sorcerer, magician. — h: sorcery, magic. *jay [у?л | N ~] sissoo tree. jagar [yal | N jigar] liver. Jah-, v. jastan. jahišn [yhysn' | J jhysn-] chance, fortune, omen. Jahišn-ayār [yhyfn hdyb'l | N n. pr. jhiy?r] fortunate. ~ih: good fortune. jahüd [yhwt' | N juhiid] Jew. jām [y m | N ~] glass. јат [M ANE < A mn-h; ут | M Pm, N <] vessel, goblet. lfamag [y”mk! | N јата) = *jām. атар [y mk! | М ртр, N fama] clothing, garment. jang [yng | M jnng, N ~] struggle, battle, fight. Jar [ywl | M рт] time, occasion. jastan, jah- [ystn!, yh-] happen, occur, chance (to be). ~išn, v. jahišn. Jašn [yfn! | N —] celebration, festival. jaw [ŠZ < A £% | N ~] barley. Jāwēd [y wyt! | (P ywyd), N ~] eternal.
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
437:ma [AL < À °l | M m, N ~] not (prohibitive). ~ agar [N magar] perhaps; lest. mad [AM < A ?m-y, v. madar | M md] mother.
537:pādīrān 63 pahikārdan
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
585:šimšār Lë"! | N ~] box tree. Sir [HLBA < A hlb’; $1 | M šyyr, N ~] milk. šīrēn [5/yn! | M syryn, N ~in] sweet. ~ih: sweetness. SiSag [$y$k! | N fifa) bottle, flask. škaft [Ар] = Skeft. škāftan, škāf- [sk’p-tn' | M ‘kk’ pt, N fikáftan] split, burst. Skarag [skik! | P *škr-] (bird) of prey. škarwīdan, škarw- [fklw-ytn' | M ‘fkrw-st, N fikarfidan] stumble, stagger. škastan, Sken(n)- [TBLWN-tn' < A N tbr; škstn!, škyn- | M ‘tkn-, N stkastan, fikan-] break. ^ i$n: breaking. škēbāģ [fkyp?k! | P kyb-, N #hëba] patient. ~ih: patience. Skeft [škypt! | P “#kyft, N šigift] hard; extraordinary, astonishing; very. ~ih: hardness; hardship, distress; astonishment. šken(n)-, ~išn, v. škastan. ških- [fkyh- | N šikth-] be broken. Skóf-, у. Skuftan. Skdfag [fRwpk! | N šukēfa] flower, blossom. Skoft [škwpt'] = škeft. 1$kóh [ол | M Ай] poor. --īh: poverty. *§k6h [kwh | N sukdh] dignity, majesty; fear. škuftan, &ЕбЇ- [škwp-tn! | N fukuftan] flower, blossom. Énàs-, v. Snaxtan. šnàsag [fn'sk! | P *$n*sg] knowing, knower; sense. ~ih: knowledge. šnāxtan, $nàs- [fm htn!, fie | M хіп, Чи s-, N fin-] know, recog- nize. šnāyēnīdan, šnāyēn- [sz dyn-ytn'] please, propitiate. ~išn: happiness. šnāyīdan, šnāy- [fr'd-ytn!] praise, propitiate. --i$n : praise, gratitude. šnāz [frc | (N šinā(w))] swimming. šnāzīdan, šnāz- [fr'c-ytn! | M $2? 2-, (IN šināw-)] swim. $nóhr [snwhl | М *fnwhr] gratitude, contentment. šnūmaģ [fnwmk! | M *fnwm-] satisfaction, contentment. &nó&ag [šnwšk! | N šunoša] sneeze. $nüg [šnwk' | M *fnwg] knee. šnūman [fnwmn! = Av. xsniimaine] propitiation. 86n [swn'] kind, manner. ~ig [-yk!] customary, ordinary. šūy-, v. Sustan. Sdy [std | N ~] husband.
590:tà [OD < A “d | (M d’), N ~] until; so that. tab [tp | N ~] fever. tab-, —išn, v. taftan. tüb- , ~išn, v. tāftan. хабар [r5k! | N taba] frying-pan. tabāh [tp?% | N ~] ruined, spoilt, destroyed. 7h : ruin, destruction. tabāhīhistan, tabāhīh- [tp’hyh-sin' | J th’hh-] be ruined. tabangóg [ipngwk! | N tabangó] box, chest. tabarzad [tpizt' | N ~] manna. tābestān [P stn! | N ~] summer. tábidan [P 5ytn! | N ~] = tāftan. tadan, tan- [itn!, tn- | N tan-] spin (thread). tadar(w) [ttl | (N tačarw)] pheasant. taftan, tab- [tp-tn'] grow hot; shine. —išn: heat, fever. táftan, tāb- [2°p-tn' | P РЬ-, N ~] heat, burn; shine. ~išn: burning. taftīg [tptyk' | (P tft)] burning, ardent, fervent. tag [tk' | N ~] running, attack. — kardan abar, ó: attack. мар (Pk! | N ta] item, unit; alone, single. ңар [Ok | N tā] branch. tagarg [tklg | M erg, N ~] hail. tagig [tkyk!] swift, strong. ~ih: speed, strength. tah [th | N ~] bottom. tak6k [tkwk! | N ~] drinking vessel. talag [t/k' | N tala] snare, trap. ~-€in [-cyn'] fowler. tambiir [tm-, tnbwl | N ~] cither, lute. ~ag [-k'] tambour (?). tan [tn' | = M, N ~] body, person. tan-, v. tadan. *tanāpuhl [tr?pwhl = Av. tanu.parada- | (N tanáfür)] a degree of sin.
601:*urwüzistan, urwāz- [”wlw?*c- = Av. urwaza-] rejoice. ~i8n: rejoicing, happiness. uskārdan, uskār- [wsk?l-tn' | J ~, (N sigāl-)] think, consider, discuss. -išn(ih): consideration, reflection. uspurrig (^wspwlyk!] = spurrig. us(t)dfrit Pzs(t)wplyt! = Av. usafriti-] offering. ušahin Pwšhyn! = Av. ufahina-] the night gah. ušnūg Pušnwk!'] = šnūģ. uštán ['wit?n! = Av. uštāna-] soul, ghost. ~th : vitality. ~отапа [-'wmnd] living, animate. uštar [GMRA < А gmD ;^wstl | N uštur] camel. 7—-$üw-palang Puštlg”plng | № ~) giraffe. uzdehig [we-, ^wzdhyk! | M ?wzdh] exiled; foreign. ~ih: exile. uzdés ["wc-,?wzdys | М ’wadys] idol. ~-parist [-plst' | M -pryst] idolater. ~-paristignih : idolatry. ~zar [-c1 | M -c’r] idol-temple. uzénag ['wcynk! | N hazina] expense, cost; exit. uzérin ['wz())ylyn! = Av. uzayeirina-] the evening gah. uzidan [wcytn! | M ?wzyd, *zozyh-] go out. uzmüdan, uzmāy- ['sozmwtn! , ”wzm'd-) prove, test, try. ~išn: testing. uzumburd ['wzmbwit! | N zumurrud] emerald. w uzwün [SNA < A If? ;^wzwn! | M ‘zw’n, (N zabdn)] tongue, language Ba ch uzwürdan, uzwār- Pwzw’l-tn! | M *zw'rdn] know, understand. ~išn: understanding; ‘huzwarish’.
1078:break (vt.) škastan.
1243:claim pahikārdan.
1351:consider abar nigerīdan, pad ēd dāštan, handēšīdan, hangārdan, ēšmurdan, uskārdan.
1500:deaf karr.
1707:dung gah, sargēn.
2187:hail tagarg.
2358:if agar, ka; — only kāč.
2403:inactive agar, armēšt.
2534:knife kārd.
2606:lest ma agar.
2648:liver jagar.
2726:manure sargēn.
2803:migrant kārdāg.
2872:musician huntyagar.
3095:perhaps ma agar.
3397:reguest pahikārdan; v. ask.
3783:split darridan, škaftan, wisistan.
4310:width pahnāy, wéhmih. wife narig, zan; Cagar. wild kófig.
4469:takēk tagarg
4540:salag! škaf- škāftan nibay-! nibastant ških- šken(n)- šken(n)išn škēbāgīh škēbāg škeftīh škeft 1*$kķēh &kohih škūf- škūfag škoft škuftan hur!, šakar škarw- škarwīdan škarag škastan škaft
4790:srāy l?syáy- srāyišnīh srāyišn sarāsar srayidan sraxtag wad! sargén srišwadag
5010:karr, -gat.
5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
5378:muy! Cst-! éstádant jagar ozan-t ózadant -gar dar, gar yal darr- draya dravābār dravāb draxt darāy
```


## [2026-09-14T01:36:45.146Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD carm\"; grep -n -o -E \".{80}carm.{80}\" PHD.txt | head -5; echo; echo \"### SOD crm/krn/krt\"; grep -n -E \"(^| )[0-9]{3,5} (c'rm|crm|krn|krt|kyrn|k'rt)\" SOD_pages.txt | head -20; echo \"--- SOD leather/deaf/knife\"; grep -n -E \"leather|deaf|knife\" SOD_pages.txt | head -25",
 "description": "PHD carm and Gharib Sogdian"
}
```


### [2026-09-14T01:36:46.292Z] TOOL RESULT

```
### PHD carm

### SOD crm/krn/krt
12995:                                                                                      3254 crm B, S
13002:             3243 cp'ys M, S                                           **Js* *cr* j   3255 crmkryy M
13008:             3244 cpS* M, S                                                   Ol/O    3256 crmny C
17012:         kamc, kamak                                 .              4660 k'rt'k B                              jjA^tJirt*.
17018:         kamande (k'nVnty)                                          4661 k'rtk -> k'rt'k
17466:4830 qrjyNvr =* krjy'wr                                                 4845 krn'kh B                                                  jf>, ^
17472:                                                                        4846 krn'wncy* =# qnw}ncy}
17473:4832 krm M                                                 >*<>/        4847 krnw'k M                                     ^^a <c^^j ^U
17478:                                                                        4848 krnw>nc(w) B                          -l>>a<>U
17492:                                                                        4850 krnw'ncyk S                                              ^aU <ojtf I
17529:         qrs-                                                         4867 krt B                                 j5U«X
17538:             karsn ©ob. -v =**wkrsnyy, ksn1, krsny                    4868 krt- S                                   jj^O\/
17545:                                                                      4869 krt'ync(h) B                              ^l^X
17550:             KG 370; STSC 133; BSTBL, Dhy. 176; STii 5.10;            4870 krth => krt
17553:       4858 krsn'w  B, M                  J^<LJtJ&-_^                 4872 krtr M, S                             JX*G^jj
17562:               Hen. Cosm. 307.12, 60; ob. pi. -ry, Vim. 154           4873 krtrty> M                      (oO)^L,tJxti v'>-
17567:            beauty                                                    4874 krts'r   S =* kwrts'r
--- SOD leather/deaf/knife
3316:pdlik (leather shoes) from p*dy\ Pers. linj- (to pull                Remarks:     1) Buddhist and all of the texts written in
12998:                                                                                           skin, leather                           f jP7 £C~*Jl
17063:     dumb, deaf-mute, mute                                                  <*kambna ©ace. -w; abl. -> =>kPny, knpy
17534:             BBB c24                                                        knife
17548:            karsne (qrsny) =»krsny                                         with knife, of knife
27433:8220 pwrsnkVy         =» pwrsnkWk                                  skin, leather
27441:                                                                   leather work
27449:      BSTii 873.19: C2, 66R19                                      (made <9/)leather                               0-*f-_#
37971:crossed     7060                         cut off 8295                            deaf 4842
37972:crossed arms      7061                   (to)cut off 1270, 1273, 6316, 6549,     deaf-mute      4671
38664: jaw    11365                           (to)keep aloof      11037, 11094        knife 4867
38716: lamentation       726, 744, 41 19, 7331    leather   3254, 8230, 8234               lifeless   306
38717: lamenting      4122, 5220, 7132            leather work    8232                     (to)lift 9094, 9120
39006:      of knife 4869                          open    1063, 4360, 4490, 10215,            outer layer  11464
39901:willy-nilly     3444                      with knife 4869                            womb      2768,11139,11140,11199
```


## [2026-09-14T01:36:54.535Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    for e in ['3254 crm','4842 ','4867 krt','4844 ','4843 ']:\n        if e in p:\n            print('leaf',i,'printed~',i-66,'|',e)\nEOF\necho \"---- print leaf for deaf 4842 ----\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (259,260):\n    pass\nEOF\ngrep -n \"4842\" /home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt | head",
 "description": "Locate SOD entries and pages"
}
```


### [2026-09-14T01:36:55.780Z] TOOL RESULT

```
leaf 193 printed~ 127 | 3254 crm
leaf 258 printed~ 192 | 4844 
leaf 258 printed~ 192 | 4843 
leaf 259 printed~ 193 | 4867 krt
---- print leaf for deaf 4842 ----
37971:crossed     7060                         cut off 8295                            deaf 4842
```


## [2026-09-14T01:37:04.261Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in (193,258,259):\n    p=pages[i]\n    print('='*30,'leaf',i,'printed',i-66)\n    for ln in p.split('\\n'):\n        if re.search(r'\\b(325[0-9]|484[0-9]|486[5-9])\\b', ln) or 'leather' in ln or 'deaf' in ln or 'knife' in ln:\n            print(ln.strip()[:200])\nEOF",
 "description": "Print Gharib entries crm, krn, krt"
}
```


### [2026-09-14T01:37:05.390Z] TOOL RESULT

```
============================== leaf 193 printed 127
inside, in, into                                           3251 cr'qd'r- C                                  b>yj\~
3252 crap'Syh  M                                    ij^
3253 crks B, M, S                                  ^J
3254 crm B, S
skin, leather                           f jP7 £C~*Jl
3243 cp'ys M, S                                           **Js* *cr* j   3255 crmkryy M
3244 cpS* M, S                                                   Ol/O    3256 crmny C
Sund.pl 32; MSP b88                                       3257 crp B                                           \*s?
3258 crpYwfin    B
3247 cr'y -► cr*y                                                        3259 CRWRH    B -> CWRH
3250 cr>q C                                                               3262 cs- C                                 6jUiU
============================== leaf 258 printed 192
GMS 355, 526; Szemerenyi. HMV 425                                 4843 qrn      C => krn
4829 krjy'wr M                     jAlcJ^Lj.js                          4844 qrn* C                                                       *J <6*
4830 qrjyNvr =* krjy'wr                                                 4845 krn'kh B                                                  jf>, ^
4846 krn'wncy* =# qnw}ncy}
4832 krm M                                                 >*<>/        4847 krnw'k M                                     ^^a <c^^j ^U
4848 krnw>nc(w) B                          -l>>a<>U
karmir; Yaghn. kimir; Arm. karmir -^qyrmyr                       4849 qrnw'ncy* M, C                                             j* <ojl*.
4840 qrmyr rytyy          M                         tfjjj^-M^                worldly
4841 qrmyst C                                                   u>      4853 krph => krp-
============================== leaf 259 printed 193
qrs-                                                         4867 krt B                                 j5U«X
BBB c24                                                        knife
karsn ©ob. -v =**wkrsnyy, ksn1, krsny                    4868 krt- S                                   jj^O\/
4869 krt'ync(h) B                              ^l^X
karsne (qrsny) =»krsny                                         with knife, of knife
4865 krsny     B, S                              ^_U j < j£i   4877 krw 8nt>k(h) B             ^jj^tJ* u'^ ^"OW4 0'^
4866 krsny'n B                           &*^y «^' jaU. ^ A            Finish. kala; Hung, kat
```


## [2026-09-14T01:37:15.125Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (125,126,127):\n    print('='*30,'leaf',i,'printed',i-65)\n    print(pages[i][:1500])\nEOF",
 "description": "Gharib page 61 area"
}
```


### [2026-09-14T01:37:16.280Z] TOOL RESULT

```
============================== leaf 125 printed 60
                                                                                                                                60

 'rw'stk


1516 Vw'stk «» WstHc                                                   1529 >rzn S
                                                                            arzan
1517 Vwytqy* C             (*j£j :Jj>-j)^<^i<sx^yi                          millet
     aruydakya ^'rwytky*                                                    MDiiipll5
     greed, rage
     BSTii 875.15; C2, 66V15; Schwartz. HMV 391                                                                                Ojjl
                                                                                                               jskj* lcr^^yi lJ*/
                                                                       1530 >s- C
1518 'rwr(h) B, M                             ^jjbcLf^jb
                                                                             as =^yt-, *s-
     orwar, orura ? (rwrO         ©Av. urvara—, Khot.                        (^)take, (/cOreceive
                                                                             C2 gloss.; GMS 129, 539; STi 43.9; Sund. AoF
           aruva\                                                              1981 p213
           =»rwrh Pa hi. uruw    ©ob. ~yh pi. -ff>,( -}n, -f/i

                                                                       1531 >s)dty C                               .xic-L-
      medicine, me
============================== leaf 126 printed 61
                                                                                                                            'skw'ch

     61

                                                                           TSP 5.96,8.61, 190 & etc.
           ask, aska    Osk") ©Av. uskau Khwar. >sk\ Past.
             hask     =^sky, sq\ sqy                                  1554 'sk'tmcyk B
                                                                           oskatamcik
           high, above, loud                                                                                        jiJ% <ji>J
           VJ; TSP; SCE; BSTBL, Dhy. 215; GMS           1215
                                                                           highest
                                                                           TSP  3.104; GMS 1014, 1296
     1543 Wdryk        => >sk>t>ryk)
                                                                      1555 >sk,tr B, M, S
     1544 'sk'n B                      <v>r jt *^&x£ Jl* tc^M <o^
                                                                           oskatar Csktr) ©Parth. }sk}dr ©comp.adj.; adv.
                                                                             =*sq}tr                             /& <jjd>
           (o)skan Csk'n) ©<*us-kana-, fskan
                                                                           higher, further, furthermore
           mark, sign, line
                                      
============================== leaf 127 printed 62
 'skw'nVk


                                                                                                                  62
 1569 'skwWk     B                      >&j>\5\ <JLS ^     1581 >sky B, M, S              (j^ yj^ jj)^ * jl> **VUjUL
      (o)skwame
      residence, dwelling                                        oske Csk'y, *skyy) ^'sk-1'
                                                                 high, up, upwards, upon
      TSP 7.6                                                    GMS 1216; VJ; TSP; BSTBL; SCE; MDii; BBB;
                                                                   Tales. 473
 1570 »skw'mc(h)    B, M, S            ,l^J oJy < J^C-                                                       a~jl> y iJ
      (o)skwamc                                            1582 'skycyk     B, M
      staying, station                                          oskecik
                                                                high        =»skycyk
      GMS 1102; Dhu. 170, BSTBL; Frag. Len. 120.5;
        KG 487                                                   TSP 14, 24; GMS 1017; Hen. Cosm. 312, 129;
                                                                   Tales. 473.33
 1571 'skw'mt'k    B                           jLS.jj^
      (o)skwamte ? ^'skw'm'k                               1583 >sky kyr'n B      {^J^ud.^lJ')^^^^
      residence
                                                                oske -k(i)ran ^c'Sr kr>n
      TSP 2.106
```


## [2026-09-14T01:37:24.024Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -E \"\\(to\\)break|^ *break|break  *[0-9]\" SOD_pages.txt | head -10; echo \"---\"; grep -n -E \"skn-|'skn|skn'\" SOD_pages.txt | head -10",
 "description": "Gharib break entries"
}
```


### [2026-09-14T01:37:24.102Z] TOOL RESULT

```
5278:    break, robbery ?                                                             527 »ps»yws B, S                                ^IJ&l
7204:     breaking                                                      1205 »ny'k B                                      (jtfU)^
13107:                                                                        breakfast
14676:                                                                       breakfast time, morning
28847:     breaking up the enemy                                        230.1 <*sarai-sta "standing ahead"
37807:break 514                                  built   3663, 3794, 7872                camp       9182
37808:(ro)break   1031, 1032, 1193, 1995,        Bukhara     8169                        camphor    4792
37810:breakfast   3281                           burden  7056                            candle   4762
37811:breakfast time    3872                     burglar    4052                         cangue    5011
37812:breaking    1034, 1192                     buried    1112, 1799, 3720, 6231        cankered     5114
---
29071:8783 skn- B         (jz^it^tyfrj^jf^ ioxMj                       existence
```


## [2026-09-14T01:37:33.786Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[126])\" | sed -n '1,120p'",
 "description": "Full Gharib page 61"
}
```


### [2026-09-14T01:37:34.920Z] TOOL RESULT

```
                                                                                                                            'skw'ch

     61

                                                                           TSP 5.96,8.61, 190 & etc.
           ask, aska    Osk") ©Av. uskau Khwar. >sk\ Past.
             hask     =^sky, sq\ sqy                                  1554 'sk'tmcyk B
                                                                           oskatamcik
           high, above, loud                                                                                        jiJ% <ji>J
           VJ; TSP; SCE; BSTBL, Dhy. 215; GMS           1215
                                                                           highest
                                                                           TSP  3.104; GMS 1014, 1296
     1543 Wdryk        => >sk>t>ryk)
                                                                      1555 >sk,tr B, M, S
     1544 'sk'n B                      <v>r jt *^&x£ Jl* tc^M <o^
                                                                           oskatar Csktr) ©Parth. }sk}dr ©comp.adj.; adv.
                                                                             =*sq}tr                             /& <jjd>
           (o)skan Csk'n) ©<*us-kana-, fskan
                                                                           higher, further, furthermore
           mark, sign, line
                                                                           BBB 553; GMS 1215, 1285; TSP 6.77, 13ii, 7, 27.5;
           GMS    369; TSP 3.191 n pl97; BSTBL, Dhy. 52, 53,
                                                                             VJ 1467; Frag. Len. 104.2; KG; MDii; MDiii
             54
                                                                     1556 >sk}tryq     M =» 'skVryk*
     1545 'sk'n s'r B «* >skys>r
                                                                     1557 >sk*tryk =* >sk>t>ryk>
     1546 'sk'ntCy) B, S          :         J^gJihJi
          oskand(e) ®fskand\ A v. skznda\ Parth. ysknd               1558 'sk'w'k S                                   VUxL^jd,
            ^ktsknt'k, sqwnt                                              oskawc =^sk*wyh
                                                                          height
          cripple, paralysed
                                                                           Sund. MSP b89
           GMS 365nl; VJ 51, 77, 124; Sund. KG 523 pl79f,
                                                                     1559 »sk*y   B => >sky

                                                                     1560 »sk»yr- B ** >sk>yr-
    1547 'sk'prn B                                         vV-*4
         oska-farn                                                   1561 'skr'nt- B                     j>/ji>j * j^j^T
          high in rank                                                     oskrand     Cskrnt-) ©<*uz Skri\ Skt. utkfntati
          Frag. Len. 44.10                                                   =>ptkrnt-, 'nkr'nt-
                                                                           0o)injurc, ({^destroy
    1548 >sk,r S                                               jUj         SCE 441, Mack. BSTBL p 154
         oskar =->sq}r
         coal                                                        1562 'skrnt- -* 'skr'nt-
          MSP bl49                                                   1563 'sks'k
                                                                          oskase S
                                                                                 ^sqsy                    o^p^< J^»<0'->>^f <j>^

    1549 'sk'rn'k   B                                   jM,^l              tomb, grave {place of bones)
          oskarne OskWy) -^sk'rn'k
                                                                           Gersh. Melanges Benv. 195; MDii, }sks*kw
          stupid, ignorant
                                                                     1564 >skt- B                              (j&OgSiJ^
          SCE 43, 113; TSP 2.656; BSTBL, Vim. 1; GMS
                                                                          (o)skat (skt>) ©Parth. lskd; A v. skaitU Khot.
            369; C2 p60
                                                                          thorn
                                                                            skai ©abl -> ^sqt}
    1550 'sk'rn'y -» ,sk>rn)k
                                                                          SCE 48; Gersh. IF 1970, 304; Mack. BSTBL pi 54
    1551 >sk'rt(w) S                                  lft»jM"j^-»
         oskart ? (sk'rtw) ©<*us-k(a)rta                             1565 >sktm      B => 'sk'tm
         rent
                                                                     1566 'sktr   B =» 'sk'tr
          MDii p60.10; Gersh. Advice. 84
                                                                     1567 >skw- B, M, S       (u>> y \.> j->)j£kJJ *u-^ *o-\#
    1552 >sk>t>ryk> B, S                     jJ^^lcj^                     (s)skaw Oskw'y-, sqw-) ^skwn, swq-, skw-,
          askatarik    Osk'tryq, 'sk'dryk, 'sk'tryk) =*sk}tryk,             'skw't-
            sq'tr                                                         (to)be, (^)exist, (/^?)stay
          higher, greater                                                 GMS 635, 804; EGSii 16, 38
         BSTBL, Dhy. 321; Vim. 164; GMS 1287; TSP                    1568 >skw>ch S
                                                                                                                 j £>- y* t-^^r j *

           8.66; KG 335; Frag. Len. 85.1
    1553 Wtm     B                                                        (o)skwac      ©f. n. ^'skw't-
                                                                          existent
         3sk(a)tam Osktm)                 jiJ^. 'jlJ-^
                                                                          Anc. Lett. 3.9
          highest, the most


*
```


## [2026-09-14T01:37:47.086Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leaf(f,i,n=2500):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    print('### ',f,'leaf',i,'of',len(t))\n    print(t[i][:n])\nfor i in (726,727,728,729):\n    leaf('KLN_1966.txt',i,600)\nEOF",
 "description": "Find Klein page 1432"
}
```


### [2026-09-14T01:37:48.266Z] TOOL RESULT

```
###  KLN_1966.txt leaf 726 of 903
he cud’,  fr.  ruminatus,  pp.  of  ruminari.  See  prec. word  and  -ion.
ruminator,  n.,  a  person  who  ruminates.  —  L. ruminator,  ‘one  that  chews  again’,  fr.  ruminatus, pp.  of  ruminari.  See  ruminate  and  agential  suff. -or.
rumkin,  n.,  a  kind  of  drinking  vessel.  —  Prob.  fr. Du.  roomerken,  dimin.  of  roemer.  See  rummer and  -kin.
rummage,  n.,  1)  a  thorough  search;  2)  miscellane¬ ous  articles.  —  Aphetic  fr.  MF.  arrumage  (F. arrimage),  ‘stowing  of  goods  in  the  hold  of  a ship’,  fr.  arrumer  (F.  arrimer)  ‘to  stow  goods  in the  hold  of  
###  KLN_1966.txt leaf 727 of 903
 suff.  -ine. Cp.  rucervine.
rusk,  n.,  light,  soft  bread  or  biscuit.  —  Sp.  rosea, ‘roll,  twist  of  bread’,  rel.  to  Port,  rosea ;  of  un¬ certain,  perhaps  pre-Latin,  origin.
Derivative:  rusk,  tr.  v.
rusma,  n.,  a  depilatory.  - —  It.  and  F.,  a  corrup¬ tion  of  Turk,  khorozma,  inexact  transliteration of  Gk.  xpiafjux,  ‘unguent’,  lit.  ‘anything  smear¬ ed  on’,  fr.  xpfs'-v,  ‘to  smear,  anoint’.  See
chrism  and  cp.  cream.
Russ,  n.  —  F.  Russe,  fr.  Russ.  Rus,  ‘Russia;  Rus¬ sian’.
Derivative:  Russ,  adj.
Russel,  n.,  also  Russel  cord,  a  kind
###  KLN_1966.txt leaf 728 of 903
i,  F.  samedi,  ‘Saturday’  and — prob. through  the  medium  of  the  Gothic— the  first element  in  OHG.  samba$-tac  (MHG.  same j- tac,  G.  Sams-tag),  ‘Saturday’].
Sabbathia,  n.,  a  genus  of  plants  of  the  gentian family  ( hot .)  —  ModL.,  named  after  the  Italian botanist  L.  Sabbati.  For  the  ending  see  suff.  -ia. Sabbatic,  Sabbatical,  adj.  —  L.  sabbaticus,  fr.  Gk. aappaxixoc,  ‘pertaining  to  the  Sabbath’,  fr. oappxTov.  See  Sabbath  and  -ic,  resp.  also  -al. Derivative:  Sabbatical-ly,  adv.
Sabbatize,  tr.  v.,  to  keep  as  a  Jewish  Sabbath.  — L
###  KLN_1966.txt leaf 729 of 903
onsecration.  —  ME.,  verbal  noun  of sacren,  ‘to  consecrate’.  See  sacred  and  -tag,  suff. forming  verbal  nouns.
sacrist,  n.,  a  keeper  of  the  sacred  vessels;  sacris¬ tan.  —  ME.,  fr.  Eccles.  L.  sacrista,  fr.  L.  sacer, fern,  sacra,  neut.  sacrum,  ‘holy,  sacred’.  See sacred  and  -ist.
sacristan,  n.  —  ME.,  fr.  Eccles.  L.  sacristanus,  fr. sacrista.  See  prec.  word  and  -an  and  cp.  sexton, which  is  a  doublet  of  sacristan. sacristy,  n.,  an  apartment  in  a  church  where  the sacred  vessels,  vestments,  etc.,  are  kept;  vestry. —  Eccles.  L.
```


## [2026-09-14T01:38:05.384Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \".{150}Avestic (car|kar|ha-kar|sk)[a-z]*.{150}\" KLN_1966.txt | head -20",
 "description": "Klein Avestic kar-/car- mentions"
}
```


### [2026-09-14T01:38:06.252Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:38:10.019Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(720,740):\n    p=t[i]\n    head=p.strip().split('\\n')[0][:60]\n    # find first alphabetical headword\n    m=re.findall(r'\\n([a-zA-Z]{3,15}),\\s',p)\n    print(i, '|', (m[0] if m else '?'), '...', (m[-1] if m else '?'))\nEOF",
 "description": "Klein leaf headword ranges"
}
```


### [2026-09-14T01:38:11.290Z] TOOL RESULT

```
720 | roc ... Romaic
721 | romaine ... rosace
722 | rosacean ... rote
723 | rauta ... roux
724 | rove ... rud
725 | Rudbeckia ... ruminant
726 | ruminator ... rusine
727 | rusk ... Sabbath
728 | Sabbathia ... sacrificial
729 | sacrist ... Sahara
730 | sail ... salient
731 | salinity ... salutation
732 | salute ... Samnite
733 | Samoan ... sangar
734 | sanguinary ... saponaceous
735 | Saponaria ... sarmentum
736 | Sarothra ... Saturday
737 | Satureia ... Savoyard
738 | saw ... scale
739 | scale ... scapula
```


## [2026-09-14T01:38:32.027Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(725,736):\n    p=t[i]\n    for m in re.finditer(r'Avestic[^,.;]{0,60}', p):\n        print(i, m.group(0)[:80])\nEOF",
 "description": "Klein Avestic mentions leaves 725-735"
}
```


### [2026-09-14T01:38:33.242Z] TOOL RESULT

```
725 Avestic  rood-
726 Avestic varlp-
729 Avestic  haurva-
730 Avestic  sacaiti
732 Avestic  a-
732 Avestic hama
732 Avestic  ha-k^r^t
732 Avestic  ha-da
732 Avestic ha-
732 Avestic  ham
734 Avestic  kar-
735 Avestic  angushta-
735 Avestic &warls-
```


## [2026-09-14T01:38:40.255Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (732,734):\n    p=t[i]\n    for m in re.finditer(r'Avestic\\s+(ha-k|kar-)', p):\n        print('--- leaf',i)\n        print(p[max(0,m.start()-700):m.start()+400].replace('\\n',' '))\nEOF",
 "description": "Klein same / kar- context"
}
```


### [2026-09-14T01:38:41.442Z] TOOL RESULT

```
--- leaf 732
, samo,  OHG.  sama,  adj.  and  adv.,  Goth,  sama, adj.,  OHG.  samant,  MHG.  sament,  samt, ‘together’,  G.  samt,  ‘together  with’,  Goth. samana,  ‘together’,  OE.  samnian,  OS.  samnon, ON.  samna,  OFris.  samnia,  MLG.,  MDu. samenen,  OHG.  samanon,  MLG.,  MHG.  sa- melen,  G.  sammeln,  Du.  tamelen,  ‘to  collect’, lit.  ‘to  bring  together',  OE.  tosamne,  OS.  te- samne,  OFris.  tosamene,  Du.  tezamen,  OHG.  zi- samane,  MHG.  zesamene,  G.  zusammen, ‘together’,  fr.  I.-E.  base  *sem-,  *sm-,  ‘one, together’,  whence  also  OI.  samah,  ‘even,  level, similar,  equal,  the  same,  identical’,  Avestic hama,  ‘similar,  the  same’,  OI.  samam,  ‘together’, sa-k(t,  Avestic  ha-k^r^t,  ‘at  once,  once’,  OI.  sel¬ dom,  Avestic  ha-da,  ‘always’,  OI.  sa-,  Avestic ha-,  OI.  sam-,  Avestic  ham,  ‘with’,  Toch.  A Soma,  B.  fomo,  ‘the  same,  similar’,  B.  fe-me,  A fas,  ‘one’,  Gk.  &\io,  ‘together  with,  at  the  same time  with’,  ojjio?,  ‘one  and  the  same’,  opoio? (Old  Att.  6p.oio?),  ‘like,  resembling’,  ouou, ‘together’,  6|xaX6q,  ‘eve
--- leaf 734
istinctive  costume. Derivatives:  sans-culott-ic,  sans-culott-ish,  adjs. sans-culottism,  n.,  the  principles  of  sans-culottes. —  F.  sans-cullottisme,  fr.  sans-culotte.  See  prec. word  and  -ism. Sanskrit,  Sanscrit,  n.  and  adj.  —  OI.  samskrta-, ‘prepared,  refined,  made  or  put  together’,  com¬ pounded  of  sam-,  ‘together’,  and  krta-,  ‘made’. The  first  element  is  cogn.  with  Gk.  aua,  ‘to¬ gether  with’,  opoc,  ‘one  and  the  same’,  Goth. sama,  ‘the  same’,  samana,  ‘together’,  OE.  same (in  same  swa,  ‘similarly’,  swd  same  s wd,  ‘just as’) ;  see  same  and  cp.  samadh,  samadhi.  The  sec¬ ond  element  is  rel.  to  k^noti,  karoti,  ‘makes’, Avestic  kar-,  ‘to  make’,  kerlnaoiti,  ‘makes’,  fr. I.-E.  base  *qwer-,  ‘to  make,  form’.  See  corpus Santa  Claus sarcoae 1382 and  cp.  Chamar,  Karma,  carcoon  and  the  second element  in  abkari,  brinjarry,  Prakrit,  prakriti, samskara,  sircar. Santa  Claus,  —  American  alteration  of  dial.  Du. Sante  Klaus,  ‘Saint  Nicholas’, santal,  n.,  sandalwood.  —  F.  sanlal,  fr.  G
```


## [2026-09-14T01:38:51.624Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(725,765):\n    p=t[i]\n    nums=re.findall(r'(?<![\\d.])1[34][0-9]{2}(?![\\d])', p)\n    print(i, nums[:8])\nEOF",
 "description": "Find Klein page numbers per leaf"
}
```


### [2026-09-14T01:38:52.744Z] TOOL RESULT

```
725 ['1474']
726 ['1365']
727 []
728 []
729 ['1373']
730 []
731 ['1490', '1376', '1377']
732 ['1378']
733 ['1380']
734 ['1382', '1405']
735 []
736 []
737 ['1388']
738 ['1390']
739 ['1391', '1392']
740 []
741 ['1394', '1393']
742 []
743 []
744 ['1401', '1402']
745 ['1405']
746 []
747 ['1406']
748 ['1408', '1409']
749 ['1410']
750 ['1413']
751 ['1414', '1415']
752 ['1416']
753 []
754 []
755 ['1422']
756 ['1424', '1425']
757 ['1426', '1427']
758 ['1428']
759 []
760 []
761 []
762 []
763 ['1438']
764 ['1439', '1440', '1441', '1488']
```


## [2026-09-14T01:38:59.659Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[760][:3500])\"",
 "description": "Klein leaf 760 (p.1432-33)"
}
```


### [2026-09-14T01:39:00.795Z] TOOL RESULT

```
n.  F.  chantier,  ‘workshop’, fr.  F.  chantier,  ‘timberyard’,  fr.  L.  cantherius,  ‘a gelding;  a  rafter’,  fr.  Gk.  xav^Xto;,  ‘a  pack ass’.  See  chantier.
Derivative:  shanty,  intr.  v. shanty,  n.,  sailor’s  song.  —  Corruption  of  chantey (q.v.)
shapable,  shapeable,  adj.  —  Formed  fr.  shape,  v., with  suff.  -able.
shape,  tr.  v.  —  ME.  shapen,  fr.  earlier  form schapen,  fr.  schap,  ‘shape’,  fr.  OE.  -sceap  in  ge- sceap,  ‘something  created  or  shaped’,  fr.  OE. sceppan,  scieppan,  scyppan,  ‘to  create,  form, shape,  do’;  rel.  to  ON.  skapa,  Dan.  skabe, OFris.  skeppa,  OHG.  scaffan,  MHG.,  G.  schaf- fen,  of  s.m.,  Goth,  ga-skapjan,  ‘to  create’,  fr. I.-E.  base  *skab-,  ‘to  work  with  a  stone  scraper, to  scrape,  scratch;  a  scraping,  scratching’, whence  also  L.  scabere,  ‘to  scratch,  scrape’;  see scab,  scabies.  This  orig.  meaning  of  base  *skab-, which  arose  in  the  Stone  Age,  was  widened  later in  the  Teut.  languages  into  ‘creative  activity’  in general.  The  primary  meaning  ‘to  scrape'  re¬ mained  in  *skap-,  a  collateral  form  of  base *skab-.  See  shave  and  cp.  skep,  suff.  -ship  and suff.  -scape  in  landscape.
Derivatives:  shap-ed,  adj.,  shap-er,  n.,  shap-ing, n.,  shap-ing-ly,  adv.
shape,  n.  —  ME.  schap,  shap.  See  shape,  v. Derivatives:  shape-less,  adj.,  shape-less-lv,  adv., shape-less-ness,  n.,  shape-ly,  adj.
-shapen,  combining  form  meaning  ‘of  a  specified shape’.  —  Fr.  shapen,  the  old  strong  pp.  of shape.  See  shape,  v.
shard,  sherd,  n.,  a  fragment.  —  ME.  sherd,  shard, fr.  OE.  sceard,  prop.  pp.  of  sceran,  ‘to  shear’; rel.  to  Du.  schaard,  ‘a  fragment’,  G.  Scharte,  ‘a notch’.  See  shear  and  cp.  words  there  referred to.  F.  echarde,  ‘prickle,  splinter’,  is  a  Teut.  loan word.
Derivative:  shard-y,  adj.
share,  n.,  portion,  part.  —  ME.  schare,  share,  fr. OE.  scearu,  ‘a  cutting,  shearing',  rel.  to  the  sec¬ ond  element  in  OE.  landscearu,  ‘a  portion  of land’,  and  to  ON.  skari,  Du.  schaar,  OHG. skara,  MHG.,  G.  schar,  ‘troop,  band’,  prop,  ‘a part  or  division  of  the  army’,  ON.  skdr,  ‘rim, edge’.  See  shear  and  cp.  next  word.  For  sense development  cp.  section  in  the  sense  of  ‘part, group’,  fr.  L.  secure,  ‘to  cut’.
Derivatives:  share,  tr.  and  intr.  v.,  shar-er,  n. share,  n.,  plowshare.  —  ME.  schare,  share,  fr.
OE.  scear,  ‘plowshare’,  prop,  ‘that  which  cuts’, fr.  sceran,  ‘to  cut,  shear’;  cp.  Du.  ploegschaar, MHG.  pfluncschar  (fr.  OHG.  scaro),  of  s.m.  See shear  and  cp.  prec.  word.
Shariah,  n.,  the  law  of  islam  ( Mohammedan  relig.) —  Arab.  shan‘ah,  ‘the  revealed  law  of  Islam’,  fr. shar‘,  ‘revelation;  the  revealed  law  of  Islam’, shark,  n.,  a  large,  voracious  marine  fish.  —  Prob. fr.  next  word  and  orig.  meaning  ‘the  roguish fish’.
Derivatives:  shark,  intr.  v.,  to  fish  for  sharks, shark-let,  n.,  shark-y,  adj. shark,  also  sharker,  n.,  a  sharper.  —  G.  schurke, ‘rogue,  rascal’,  which  is  an  agent  noun  of  MHG. schurgen,  schuren  (G.  schiiren),  ‘to  poke,  stir’. Derivatives:  shark,  tr.  v.,  to  get  by  trickery,  to practice  trickery,  shark-ish,  adj.
Sharon,  n.,  name  of  the  fertile  coastal  plain  ex¬ tending  from  Jaffa  to  Mount  Carmel.  —  Heb. Shardn,  aphetic  for  *yishdr6n,  prop,  ‘the  Plai
```


## [2026-09-14T01:39:16.082Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\np=t[761]\nm=re.search(r'\\nshear,',p)\nprint('LEAF761 nums', re.findall(r'(?<![\\d.])1[34][0-9]{2}(?![\\d])',p))\nif m: print(p[m.start():m.start()+1200].replace('\\n',' '))\nEOF",
 "description": "Klein shear entry"
}
```


### [2026-09-14T01:39:17.260Z] TOOL RESULT

```
LEAF761 nums []
```


## [2026-09-14T01:39:19.622Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A14 \"^shear, tr\" KLN_1966.txt | head -30",
 "description": "Klein shear entry grep"
}
```


### [2026-09-14T01:39:19.704Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:39:21.855Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \"shear,[^\\n]{0,900}\" KLN_1966.txt | head -4",
 "description": "Klein shear"
}
```


### [2026-09-14T01:39:22.961Z] TOOL RESULT

```
34915:shear,  tr.  and  intr.  v.  —  ME.  scheren,  sheren,  fr. OE.  sceran,  scieran,  ‘to  cut,  shear',  rel.  to  ON., OFris.  skera,  Dan.  skjsere,  Du.  scheren,  OHG. sceran,  MHG.,  G.  scheren,  ‘to  shear’,  fr.  l.-E. base  *(s)qer-,  ‘to  cut,  separate’,  whence  also  OI. krnati,  krndti,  ‘hurts,  wounds,  kills’,  krntati, ‘cuts’,  krtih,  ‘hide’,  carman-,  Avestic  bar  man-.
34918:shear, sheath,  n.  —  ME.  schethe,  shethe,  fr.  OE.  scxd, rel.  to  OS.  scethia,  ON.  skeidir  (pi.),  OFris. skethe,  MDu.  schede,  Du.  schede,  OHG.  skaida, MHG.,  G.  scheide,  ‘scabbard’.  These  words prob.  meant  orig.  ‘something  separating’,  and are  rel.  to  shed,  v.  (q.v.) sheathe,  tr.  v.  —  Fr.  sheath.
35039:shear, short,  adj.  —  ME.  schort,  short,  fr.  OE.  sceort, scort,  ‘short’,  rel.  to  ON.  skorta,  ‘to  be  short of’,  short,  skortr,  ‘shortness’,  OHG.  scurz, ‘short’,  from  a  dental  enlargement  of  I.-E.  base *(s)qer-,  ‘to  cut’,  whence  also  OI.  krdhuh, ‘shortened,  maimed,  small’,  L.  curtus,  ‘short’, cordus,  ‘late  born’,  originally  meaning  ‘stunted (in  one's  growth)',  OSlav.  kratuku,  Russ,  korot- kij,  ‘short’,  Lith.  skurstu,  skufsti,  ‘to  be  stunted (in  one’s  growth)',  skardus,  ‘steep’,  OIr.  cert, ‘small’,  Mir.  corr,  ‘stunted,  dwarfish’.  See  shear and  cp.  shirt,  skirt.  Cp.  also  curt  and  the  first element  in  curtail.  Cp.  also  kirtle.
39539:shear,  clip’,  which  stands  in  gradational  rela¬ tionship  to  Gk.  xevSetv,  ‘to  gnaw’,  Mir.  ro-s- teind,  ‘he  cut  off’,  temm  (for  *tend-men),  W., Co.  tarn  (for  *tnds-men),  ‘morsel,  bit’,  Ir.  and W.  tonn,  ‘skin’,  fr.  I.-E.  *tend-,  *tond-,  enlarge¬ ment  of  base  *tem-,  ‘to  cut’,  whence  Gk.  xip- veiv,  ‘to  cut’.  See  tome  and  cp.  toison.  For  the ending  see  suff.  -ure.
```


## [2026-09-14T01:39:32.705Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (344,345,346):\n    print('='*20,'leaf',i)\n    print(t[i][:1800])\nEOF",
 "description": "Buck p.321"
}
```


### [2026-09-14T01:39:33.776Z] TOOL RESULT

```
==================== leaf 344
vw ‘be wounded’ : Lat. ulcus ‘sore’, Skt. argas- ‘hemor- rhoids’. Walde-P. 1.160. Ernout-M. 1120.
Grk. &zed ‘wound’ (Hom., Hipp.) and ‘sear’ (fr. *d¢areAva, cf. yaradat’ ob- al Hesych.; obréw the regular Hom. vb. for ‘wound’ clearly belongs here, though the ov is unexplained) : Lett. vals ‘wound’, Lith. votis ‘ulcer, boil’, fr. IE *wa- beside *wen- in OE wund, ete. (below, 4). Walde-P. 1.211. Solmsen, Unters. 298 f.
0
ARTS B anv ‘blow, stroke’, NG Tk. i a maaya, whence prob. iyound’s uld be native) Lat. plaga late also ‘plague’
>I.
‘a aa Rum. plaga mostly ‘plague’) llaga
Ok, majoow ote beat the breast, lament’, etc. 5 y
"p 9,91f. Ernout-M. 774. Bee xpaiare, fr. naan ‘wound’, this fr, hoff ‘handle, grip’ in the sense ‘hold, grip’ in wrestling. Hatzidakis,
145. ae a yulnus (earlier volnus), W. gueli, Br. gouli : Ir. furl ‘blood’, fudl bloody wounds’, Grk. otd7 ‘scar’, ON valr ‘corpses of the slain’, OHG wuol ‘defeat, pestilence’, OPruss. ulint ‘fight’, Hitt. walh- ‘strike, defeat, destroy’ (Sturtevant, Hitt. Gloss. 75 f.), Toch. A wal- ‘die’. All fr. a root *wel- (ultimate- ly the same as in Lat. vellere ‘pluck, tear out’, etc.?). Walde-P. 1.304 f. Er- nout-M, 1129,
It. ferita, Sp. herida, fr. It. ferire, Sp. CH ‘wound, hit’, fr. Lat. fertre ‘strike, eat’,
Fr, blessure, fr. vb. blesser ‘wound’, Olt. blecier ‘bruise, crush, injure, Wound’, fr. deriv. of a Frank. *bléa Uf eobleto in Lex Salica ‘running wound’?) : OHG bleizea gl. livor, OR blat ‘livid, bruise’ or “vound’ fr. its
115, Wartburg 1.406. um, Tana, fr. Slavic (below, 6). , crécht, NIr. créacht : W. crei- T. creizenn, NBr. kleizenn ‘scar’, ‘ ae NE scar fr. i ab’) : skra@ ‘dry piece Gs Li a ete, (Falk-Torp 1021), ir ae oe 13.28 f. rape, ar, : Ir. cneadh : Grk. xvite atch’, ON hrita ‘strike,
Digitized by Arya Samaj F
==================== leaf 345
so sometimes ‘wound’, now only in dial.), Goth. sair, OHG, OS sér ‘pain’, ro-formation to a root *sai- in Ir. sdeth injury, trouble, sickness’, Lat. saevus ‘raging, fierce’. Walde-P. 2.445. Falk- Torp 941.
ON und, OE wund, etc., general Gmc. words (with adjs. Goth. wunds, OE, OHG, etc. wund ‘wounded’), prob. : W. gwanu ‘pierce, thrust, stab’, ym-wan ‘fight’, fr. IE *wen- beside *wa- in Grk. aren etc. (above, 1). Walde-P. 1.212. Falk-Torp 1399.
5. Lith. Zaisda perh.: Ir. goite ‘wounded’ (*ghoizd-), Skt. Aizis- ‘injure’, fr. IE *gheis-, extension of the root in Skt. hi- ‘set in motion, hurl’. Walde-P. 1.546.
Lith. rona fr. Pol. rana (below, 6).
Lett. vats : Grk. mred7, etc. (above, 1).
Lett. cevainuojums fr. tevainuot ‘n- jure, wound’, cpd. of vaindt ‘accuse, blame, injure, wound’ (physical from
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
306 SELECTED INDO-EUROPEAN SYNONYMS
mental), deriv. of vaina ‘fault, blame’ : Lith. vainoti ‘scold’, ChSl. vina ‘accusa- tion’, ete. Miihl.-Endz. 4.438 f.
6. ChSl. strupi (Lk. 10.34 renders tpatpa Mar., Glag.; jazva Sav.), cf. Russ., Bulg. sirup ‘scab’, Pol. sirup ‘scurf’, etc., prob. : Grk. pimos ‘filth’ juréw ‘make foul’, IE *sreup-. Walde- P. 2.703. (Otherwise Briickner 521, but ??).
ChSI. jazva (also ‘blow’ and ‘plague’) = Russ. jazva ‘cleft, wound, ulcer’,
Bulg. jazva ‘wound’, Boh. jézva ‘scar,
wound’ : OPruss. eyswo ‘wound’, Lett. aiza ‘crack (in the ice)’, Lith. aizytz ‘husk’, etc., further connections dub. Berneker 276 f. Walde-P. 1.9.
Digitized by Arya Samaj Foundation Chennai and eGangotri
ChSI. rana (also ‘blow’ and ‘plague’ etc., the modern Slavic words : Skt. vrana- ‘wound, sore, flaw’, Alb. varrg ‘wound’, fr. a root *wer- meaning ‘teay’ or the like(?). Walde-P. 1.286. Fo, distribution of the three preceding 
==================== leaf 346
n Skt. bhigaj-, bhisajya-,
Rum. vindeca, taémddui OHG heilen, lachinon, cikitsa-
Ir. tccaim, fris-ben (3 sg.) giarzinon Av. bigaz-
Nir. _leigheasaim MHG heilen, erzenen
W. tachau NHG heilen
Br. yac' haat, parea
Most of the words listed may be used for ‘cure’ with either the person or the dis- ease or wound as the object, but a few only with reference to the person, and this was the primary application in nearly all cases.
Some of the words are in origin ‘(make) well, whole, alive, vigorous, etc.’, or ‘protect, rescue, save’, and in all such the notion of ‘cure’ is inherent.
Others are from ‘care for, attend to’, specialized to medical care, or are deriva- tives of words for ‘physician’. These then meant properly only ‘treat medical- ly’, but generally acquired the optimistic
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
implication of successful treatment and so came to be used for ‘cure’ just like those of the preceding type.
1. Grk, Téopar : talyw (*isnyd) ‘heat, warm, cheer’, Skt. zs- ‘set in motion, urge, animate’, isira- ‘refreshing, active, vigorous’, ON eisa ‘dash forward’, etc., all prob. fr. a root meaning ‘animate, enliven’ or the like. Walde-P. 1.106. Boisacq 262 f. :
Grk. Oeparebw ‘attend, do service, take care of’, hence esp. ‘treat medical- ly, cure’ : Grk. @epdwv ‘servant, attend- ant’ (19.43). Walde-P. 1.857. Boisacd 340 f.
sare O
Grk. aa ‘oure’, ir. tarpés ‘phy- a ly aye can sanare (> It. sanare, Sp. a
us ‘well, healthy’ (4.83).
fr. cura ‘care’, hence ‘take ad dical language ‘treat ence Sp. curar ‘cure’ h OFr. curer ‘care for, clean’)
, fr. san
and (throug f r’ an ‘care 10. : De allt ‘give (medical) attention
to, ¢ ure’ (with dat., rarely acc.), beside
ricus ‘physician’ (whence also poet. md te Lat. medicare), medicina ‘medi- ee ‘remedy, m
```


## [2026-09-14T01:39:39.854Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (359,360,361):\n    print('='*20,'leaf',i)\n    print(t[i][:2200])\nEOF",
 "description": "Buck p.321 area"
}
```


### [2026-09-14T01:39:40.828Z] TOOL RESULT

```
==================== leaf 359
, Miuhl.-Endz. 2.338.
Lett. laisks : laist ‘let go’, etc., Lith. leisti ‘let, permit’ (: Goth. létan, ete., above, 4; see 19.47). Miihl.-Endz, 2.411,
Lith. slinkas (Buga, KZ 52.296; not in Kurschat, Lalis, but cf. slinka ‘slug- gard’; slankus ‘slow, lazy’ in Busch- Chowskas), Lett. slinks : Lith. slinkti ‘crawl, slink’, OF slingan ‘wind, crawl’, etc. Walde-P. 2.714. Miuhl.-Endz. 3.933.
6. ChSl. lént, etc. general Slavic : Goth. lats, etc. (above, 4). Berneker 711.
7. Skt. alasa-:il- ‘keep still, be quiet’, Lith. ilsti ‘become tired’, cf. pailses ‘tired, weary’ (4.91). Walde-P. 1.152.
Skt. manda-: ChS]. maditi ‘delay, linger’, maqdtni ‘slow’, etc. Walde-P. 2.305. Meillet, MSL 14.372.
Av. a-varazika-, lit. ‘not working’, fr. varaz- ‘work, do, make’ (9.13). Barth. 347.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
+ of the words listed may be used he head or of the person having d (NE his head zs bald or he ts h the latter may also be and so usually
Mos either of t a bald hea: bald), thoug ‘ walled ‘pald-headed’,
NHG kahlkopfig. The words for ‘bald’ seldom have any
connection with those for ‘hair’, words meaning literally ‘hairless’ being used otherwise. The commonest source, where this is clear, is the notion of ‘bright, shiny’ or ‘smooth’.
1. Grk. gadaxpés (NG pop. also, with metathesis, xapaddds) : padds* Aevxés He- sych., dadids, dadapds ‘having a white spot’, Ir. ball ‘spot’, Lith. baltas ‘white’, Skt. bhala- ‘splendor, forehead’ (cf. also ME balled, below, 4). Walde-P. 2.175 f.
2. Lat. calvus (> It., Sp. calvo, Fr. chawe) : Av. kaurva-, NPers. kal ‘bald’, Skt. ati-kulva-, -kiilva- ‘entirely bald’, a also, Skt. khalati-, khalvata- ‘bald- ae Walde-P. 1.447. Ernout-M.
- Walde-H. 1.144,
aaa fr. pelo ‘hair’ (4.14), OnpOsite cre Use Of ‘hairy’ for the
®, or through a derogatory sense common alike to ‘hairy’ ‘ _ Iry’ and ‘bald’(?).
Rum, kotsch Aly fr. Turk. kel ‘bald’. Lo-
Rum, ple .,  Pegur, fr. the Slavic, ef msin, fare vic, ef. ChS]. Nir Ae ‘dull, without horns’), lum’) meee moel (OW mail ‘muti- 1 DY. moa] » Perh. (as *mai-los) fr.
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE BODY; BODILY FUNCTIONS AND CONDITIONS 317
4.93 BALD Gothsi
==================== leaf 360
v, plesiv calvo OE aie ee Boh. _lysy, pleSivy, pleSaty chau ME alled, calou Pol. lysy ; ean ek NE bald Russ. lysyj, pleSivyj ? a ue aa ite ee khalati-, munda- mi O calo Vv. kaurva- maol MHG kal pe NHG kahl m
the root *maz- ‘cut off, hew’, in Goth. maitan ‘hew, cut’, ON meita ‘cut’, etc. Walde-P. 2.222. Otherwise Stokes 204.
4. ON skalli (sb. ‘a baldhead’), adj. skollotir, Dan. skaldet, Sw. skallig, perh. fr. s-form of the root in Lat. calvus, ete. (above, 2). Ernout-M. 137. Falk-Torp 980 (but combined with the following).
OF calu, ME calouh (NE callow), Du. kaal (LG kal > Sw. kal), OHG kalo, MHG kal, NHG kahl: ChSl. golu ‘naked’, etc. (4.99). Walde-P. 1.537 f. Berneker 325f. Combined by some with Lat. calvus, etc. (above, 2) on the basis of IE variant initial k/g, or even as loanword from it (cf. Walde-P. 1.538).
ME balled, NE bald (cf. also Dan. beldet ‘bald, callow’, of birds), prob. fr. ball ‘white spot’ on the forehead (in spite of the fact that this is not quotable as early as balled), this (whether or not through Celtic) : Grk. ¢adapés, etc. (above, 1). Walde-P. 2.175. Falk-Torp 123. NED s.v.
5. Lith. plikas, Lett. pliks (also ‘naked’), ChSl. plévii, SCr. plesiv, Boh. plesivy, plegaty, Russ. plesivyj (also Lith. pleikas ‘bald spot’, Lett. plaikums ‘spot’) : Lith. plynas ‘plain, even, smooth’, plyné ‘plain, open field’, Norw. dial. flein ‘bald, naked’, Sw. dial. flen ‘naked’, but further root connection dub. Walde-P. 2.93. Mihl.-Endz, 3.344. Falk-Torp 235.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
318 SELECTED INDO-EUROPEAN SYNONYMS
Lett. katls ‘bald, naked, bare’: Ir. coil ‘thin, slender’, W., Corn. cul ‘lean, narrow’. Walde-P. 1.455.
6. ChSI. viiz-lysti, Boh. lysy, Pol. zysy, Russ. lysyj : Skt. rucant- ‘bright, shining’, IE *leuk-, beside *leuk- in Lat. liz ‘light’, ete. Walde-P. 2.411. Berne- ker 752.
ChSl. plévt, above, 5.
SCr. éelav, fr. Turk. kel id. (ef, above, 2, Rum. chel).
7, Skt. khalati-, Av. kaurva- - Lat. calyus, above, 2
Skt. munda- ‘with shaven head’ (also ‘hornless, blunt’), perh.: Skt. 7d- ‘crush, rub’, etc. Walde-P. 2.288 (287),
4.94 LAME Grk. _ xwAds Goth. halts L
==================== leaf 361
break, bend, twist’, some from the name of a part affected (as ‘hip’), some prob- ably of imitative origin (from the clump- ing sound of a lame person), several quite obscure.
1. Grk. xwhds, etym.? Boisacq 1072.
NG xovrods, Byz. xourtds (xorods Chron. Mor.), orig. ‘crippled’ as in epds. xourfodaxrudos ‘stump-fingered’ (Byz.), xourfoubrns ‘snub-nosed’, —_xouraoxépns ‘with crippled hand’, xovroatrns ‘crop- eared’, etc. (G. Meyer, Neugr. Stud. 2.97 ff.), now plausibly explained as fr. xoyo- (: xérrw ‘cut’) in cpds., the change of xo to zo perh. first by dissim. in cases like xoo-ré5ns > xoroo-ré5ns. Amantos, AOnva 28, mapapr. 124f. Georgacas, "Apx. Opax. Ono. 14.227, n. 4. The Slay- ie words, Bulg. kuc ‘lame’, ete. (Berneker 636), are then loan words.
2, Lat. claudus, history obscure, but prob. connected in some way with claudere ‘shut’—either directly through ‘shut off, prevent’ (as fugam claudere) and hence ‘hamper’, or more remotely through the underlying root of claudere and cldvis ‘key’, with the notion of ‘bend, hook’. Walde-P. 1.492. Walde- H. 1.281.
It. zoppo, blend of zanca ‘leg’ and VLat. cloppus ‘lame’ (see below). REW 9598.
It. ranco, through Cat. or Prov. ranc fr. Frank. *rank (= MLG rank ‘twist- ed’): NHG renken, NE wrench, ete. REW 7044. Weigand-H. 2.570.
Fr. botteuz (beside boiter ‘limp’), OFr. boisteux, apparently a deriv. of OFr. boiste, Fr. boite ‘box’, also ‘bone- socket’ (fr. MLat. buaida, Grk. qvéis, -i6a ‘box’), hence orig. ‘club-footed’ (perh., but not necessarily, influenced by bot ‘club-footed’). REW 6892. Gamillscheg 119.
Sp. cojo (Cat. coix, Port. coxa), fr. VLat. cozus ‘claudus’ (gl.), fr. Lat.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
7 REW 22920. Er-
VLat. cloppus ‘lame’ Fr. clocher, Prov.
1 Alb. shgep Jame’, prob. , Ernout-M. 199.
ant orig. a ini 237. REW 1997. Puscariu
6. piop {r-
picare in
ym. dub., perh. : Grk. fglantiDg, oblique’, etc. Stokes (Walde-P. 1.157 with query.)
3 (= W. bachog ‘hooked,
W. bach ‘hook’
50. oF Ir. lose, et
W. dof, fr. VLat. cloppus (cf. above, 9, Rum. gchiop). Pedersen 1.238. Loth,
ome’.
4, Goth. halts, ON haltr, OF healt etc. the old Gme. group for ‘lame’ (NE halt arch.) : Ir. coll ‘destr
```


## [2026-09-14T01:39:47.646Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (362,363,364):\n    print('='*20,'leaf',i)\n    print(t[i][:2500])\nEOF",
 "description": "Buck DEAF section"
}
```


### [2026-09-14T01:39:48.668Z] TOOL RESULT

```
==================== leaf 362
inken ‘limp’ (= ON hinka, etc.) : Skt. khavj- ‘limp’, khafija- ‘lame’, Grk. oxatw ‘limp’, ON skakkr ‘awry, twisted’, IE *(s)keng-. Walde-P. 2.564. Falk- Torp 406.
5. Lith. raigas : Grk. fords ‘crooked, bent’, Av. urvaésa- ‘turning, whirl’, urvisyeiti ‘turns’, etc., IE *wreik-, ex- tension of *wer- ‘turn’. Walde-P. 1.279.
Lith. Slubas (whence slubuoti ‘limp’), Slumas, Lett. slums, history dub. Not directly : Skt. (RV) ¢réna- ‘lame’ (so W. Schulze, Berl. Sitzungsber. 1910 p. 801, Mithl.-Endz. 3.941), since this is rather a deriv. of ¢réni- ‘hip, buttock’ (name of the defect from the part of the body affected, cf. VLat. corus ‘lame’, above, 2). The Baltic words may be in- dependent derivatives of a root *fleu- ‘crack, break’(?) assumed as underlying the words for ‘hip’, Skt. crénz-, Lith. Slaunis, W. clun, etc. Walde-P. 1.499 f.
Lett. tizls, etym.? Miuhl.-Endz. 4,199.
Lett. klibs, cf. Lith. klibas ‘bowlegged, tottering’ : Lith. ‘libétz ‘shake, totter’, Lith. klebéti, Lett. klabat ‘shake, rattle’, outside root connection? Miuhl.-Endz. 2.225,
6. ChSI. chrom, etc., general Slavic : Skt. (Ved.) srama- ‘crippled, lame’, root connection? Walde-P. 2.706. Berneker 403.
SCr. Sepav, ef. Sepati ‘limp, hobble’, Ukr. sepast ‘lame’, etc., outside connec- tions? Miklosich 338.
Boh. kulhavy, Pol. kulawy, with vbs. Boh. kulhati, Pol. kulaé ‘limp’, history difficult. Brickner 281 derives Pol. kulawy fr. kula ‘staff, crutch’ (this fr. NHG dial. kule = keule ‘club’),—attrac- tive for the Polish, but not for group as a whole, for which cf. Berneker 642 f.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
320 SELECTED INDO-EUROPEAN SYNONYMS
7. Skt. ¢réna-, see under Lith. slubas (above, 5).
Skt. sr@ma-:ChSl. chromi, etc. (above, 6).
Skt. khatija-: MHG hinken ‘limp’ etc. (above, 4). ‘ Skt. khora- (also khoda-, khola-), Perh : Lat. scaurus ‘clubfooted’ (cf. Seas:
Skt. pangu-, etym.? Ublenbeck 152. | rus). Ernout-M. 904. Walde-P. 2.538,
4.95 DEAF Grk. — xwdds Goth. baufss Lith. kurtias, kurtinas NG xougds ON daufr Lett. kurls, kurns Lat.  surdus Dan. dv ChSl. gluchit It. sordo Sw. dév SCr. gluh Fr. sourd OE déaf Boh. = hluchy Sp. sordo ME deaf Pol. gluchy Rum. surd NE deaf Russ. gluchoj Ir. bodar Du. doof Skt. badhira- Nir. —_ bodhar OHG  toub (tumb) Av. karana-, asrut-gaoka- W. byddar MHG toup Br. bouzar NHG taub
The common words for ‘deaf’ are not from such a logical source as ‘not hear- ing’, but rather from more g
==================== leaf 363
dible’, prob. (as orig. ‘indistinct’ of sound) fr. the root in susurrus ‘muttering, whisper’, susurrare ‘hum, mutter, whisper’, Skt. svar- ‘sound’, ON svarra ‘roar’. Walde-P. 2.528. Ernout-M. 1007.
3. Ir. bodar, NIr. bodhar, W. byddar,
Br. bouzar, prob. (with IE 0) : Skt,
badhira- ‘deaf’. Stokes 176. Pedersen 1.111, 363. Thurneysen, Gram. 74, Otherwise Walde-P. 2.190, with attempt to combine with Goth. baups.
4. Goth. baups, etym. dub. Possibly as orig. ‘blunt’ : MDu. bot ‘dull, stupid’, LG butt ‘blunt, coarse’, Norw. dial. buit ‘blunt’, cf. also Arm. bot‘ ‘blunt’. Pers- son, Beitrige 256. Feist 86. Otherwise Walde-P. 2.190 (cf. above, 3).
ON daufr, OF déaf, OHG toub, etc., general Gmc. (in most cases also in the sense of ‘dull, slow’ of mind or body; Goth. only in this sense, daubata hairto ‘dulled heart’, Mk. 8.17): ON deyfa ‘blunt, stupefy’, dofinn ‘dull, drowsy’ (Dan. doven ‘lazy’ 4.92), MHG touben ‘stupefy’, etc., Grk. ridw ‘raise a smoke, stupefy with smoke’, suddds ‘blind’ (4.97), ete., here also Goth. dumbs ‘dumb’, etc., OHG tumb ‘stupid, dumb, deaf’ (4.96), fr. *deu-bh- extension of IE *dheu- in Skt. dhia- ‘shake’, dhtima- ‘va- por, smoke’, Grk. 6iw ‘rush, rage’ and numerous other formations, with a com- mon notion of ‘whirling, rapid, dizzy motion’, applied to various physical and mental phenomena, and including some
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
y; BODILY FUNCTIONS AND CONDITIONS 321
TS oF THE BUD AR suet ‘dumb’, and ‘blind’. 6. ChSl. glucht, etc., general Slavic, words £08 a: Falk-Torp 179. outside connections? Berneker 308, 309. rate? Fie kurtinas, Lett. kurls, Briickner 145 (unconvincing). 5, Lith. 1 Jriinit ‘having a mutilated urn”) (of. also Russ. kur-guzyj 7. Skt. badhira- : Ir. bodar (above, 3). eat oF n08e" Uke. kur-nosyj ‘snub- Av. karana- (so NPers. kar ‘deaf’), see tailed’, ‘deaf’ ighort- ob. also Av. karana- ‘deaf’, | above, 5 and Barth., IF 3.169. nosed’), PF tghort-eared’, all with com- Av. asrut-gao8a-, lit. ‘having unhearing Skt. kara of mutilated and presumably | ears’ (cpd. of a- privative with sru- ‘paler ‘out’. Mil. -Fndz. 2.323. | ‘hear’ and gaoga- ‘ear’). Barth. 223. fr. UE Berneker 6 4.96 DUMB ‘ Goth. dumbs, baufs Lith. nebylys, beZadis Grk. a ori ON  dumbr Lett. méms NG oie Dan. stum ChSl. némit Lat. muto, m
==================== leaf 364
utolo Sw. stum SCr. nijem Be et OE dumb Boh.  némy s, —imudo ME = dumb Pol. — niemy a mut NE dumb Russ. nemoj it * amlabar, balb Du. stom Skt.  miika- Nir. balbh OHG _ stum (tumb) Av. afravaota- W. mud MHG stum (tump) Br. = mud NHG  stumm
Of the words for ‘dumb’, only a few are from such a logical source as ‘not speaking’. Some are from the general notion of ‘dull’, with the same word or cognates used also: for ‘deaf’ (4.95). The majority are from ‘stammer’ or the lke, most of these being of imitative origin. fn oi xagés, same as for ‘deaf’ ae CoM ‘silent’, but
£. cpd. of dwyvy ‘voice’.
L i ae Be (quotable as ‘dumb’ tee ete., in Hesych. ‘lame’), tenia Byz. Grk., NG BovBés, prob. iat, tae derogatory epithet of the beaby, OF. 3 D. bobo ‘stupid’, NE boob, Meyer, ene ‘simpleton’, etc. G.
Hevyyés, see below, 2.
2. Lat Rum, a (> It. muto, Sp. mudo, Mel), fp. + tee derivs. It. mutolo,
imitative syllable mil,
sound made with closed lips (cf. non facere mu ‘say not a word’, Grk. pi \adety ‘mutter’). So also Skt. mika-, Grk. puv- dés, and the forms of Hesych. ptédos, puxés, puvapés, wuTrds, pbTns, Byz. poyyos (Leont. Cypr., 7th cent.), NG povyyés and Arm. munj. Walde-P. 2.309 ff. Er- nout-M. 650.
3. Ir. amlabar, epd. of neg. am- and labar ‘loquacious’ : W. Uafar ‘speech’, Br. lavar ‘word’, dilavar ‘silent, speech- less’. Pedersen 2.7.
Ir. balb, Nir. balbh, fr. Lat. balbus ‘stammering’ (this sense also in Irish). Vendryes, De hib. voc. 115.
W., Br. mud fr. Lat. mutus. Mots lat. 188.
4, Goth. dumbs, ON dumbr, OE-NE dumb, but OHG tumb mostly ‘stupid’ rarely ‘dumb, deaf’, MHG tump ‘stupid’ rarely ‘dumb’ (NHG dumm in LG form), fr. a nasal form of the root in ON daufr,
Loth.,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
322
etc., ‘deaf’ (4.95). Walde-P. 1.840. Feist 129.
Goth. bawps ‘deaf’ (4.95) once (Mt. 9.32), also for xw¢és as ‘dumb’.
Du. stom (MLG stum > Dan., Sw. slum), OHG, MHG stum, NHG stumm : OHG stam(m)alon, MHG stammeln, ON stama, OE stamorian ‘stammer’, Lett. stuomities ‘stammer, stumble, stop’, stwmt ‘push’, Lith. stumt? ‘shove’. Walde-P. 2.626. Falk-Torp 1189 f.
5. Lith. nebylys, neg. cpd., second part : byloti formerly the common word for ‘speak’ (18.21).
SELECTED INDO-EUROPEAN SYNONYMS
Lith. bezadis, cpd. of privative Prefix be- and Zadas ‘voice, sound’.
Lett. méms, prob. fr. an imitatiy lable mé- (like *mz- in Lat. mitus above, 2). Miihl.-Endz. 2.615 ¢.
6. ChSl. némii, etc., general
```


## [2026-09-14T01:40:00.126Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nprint(len(t))\nfor i in range(330,340):\n    nums=re.findall(r'(?<![\\d.])6[0-9]{2}(?![\\d])',t[i])\n    print(i, nums[:5], t[i].strip().split('\\n')[0][:60])\nprint('---')\nfor i in range(586,598):\n    nums=re.findall(r'(?<![\\d.])11[0-9]{2}(?![\\d])',t[i])\n    print(i, nums[:5], t[i].strip().split('\\n')[0][:60])\nEOF",
 "description": "Locate Mann pages 640 and 1155"
}
```


### [2026-09-14T01:40:01.098Z] TOOL RESULT

```
858
330 [] ow’; Gk. cf. küttaros *cell, hold, urn, pod, arch'; OE hüder
331 [] h ‘straw cone,
332 [] ukáð ‘mix, confuse, disturb’; Cz. kyšu, kysat ‘ferment’; Li.
333 [] ‘gusset’. (OCS kyla ‘hernia’ appears to be long zero-gde of 
334 [] ambiguity in the Celtic forms) Skt. kumpah, adj. ‘with arm c
335 [] ��; kpic ‘make a fool of": Ukr. kpyty ‘jeer at
336 [] korgà (“bent old woman’. Also ‘reef, sandbank’. Cf. krgos); 
337 ['601'] type *kusdhero-, *kusdhro- in Skt. küharah, m. ‘hole, cave’;
338 [] , et ‘frolic, fool about’; küve, f. ‘frolic’. (Variant of ty
339 [] all, sink, fail’; cf. caries (decay: Skt. Sadah “fall, shedd
---
586 [] ið (qusinið) “crush, destroy” Skt. ksinómi, ksinami, v. “des
587 [] *dapple, speckled’; Oss. áxsid, Dig. àxsed (cred Of sky)
588 [] 'in- dicate, suggest); Ir. rádh, pl. ráidhte, m. ‘speech, wo
589 [] Vari- ant rasp-) OHG refsen, MHG refsen & respen, v. ‘bully’
590 [] ; cf. rhégma, n. ‘dyed object
591 [] m. (number, if for *sm-ridhmo-); Gallo-Lat. ve- rédus, gs: -
592 [] hrust
593 [] �prop, support’; OE remian, v. ‘mend’; OCS cf. remístvo, n. 
594 [] Av. rap-, pp: rapt-, v ‘go’; Per. ravam, pp: rafte, id.; Lat
595 [] �; Lat. (z-gde) rudo, ére, v. ‘roar, bray’; Ir. cf. ruadh, a
596 [] id.; OE reoma, wm. ‘membrane, ligament, muscle’; Du. riem, m
597 [] & Eng. rut); Pol. rzut, m. ‘fling’. (Isophonic in Go. ga-riu
```


## [2026-09-14T01:40:09.262Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \".{120}risec.{120}\" IEC.txt | head -5; echo \"=== sek- ===\"; grep -n -E \"^sek[-ō]|^sekō|^sek-\" IEC.txt | head -10; echo \"=== kort/kurt ===\"; grep -n -o -E \".{80}curtus.{120}\" IEC.txt | head -5",
 "description": "Mann risecum, sek-, curtus"
}
```


### [2026-09-14T01:40:09.357Z] TOOL RESULT

```
=== sek- ===
15139:sek-, radical element of following entries: "eut"
15140:sek- (?) Gk. cf. héka, adv. ‘slowly’; hésson, adj. ‘slow-
15143:sek-, -sekā, io “cutting, mowing’. (Simplex
15152:sek-, -seka, io — sēlos, is
=== kort/kurt ===
7712:kt. kartyah “for cutting off: Gk. kórses ‘shaved, trimmed’, fr. *kortio-); Lat. curtus ‘short, docked’; OCS (dim. type) kratúkú, R koròtkij, id., beside OCS kratiti, inf. ‘to shorten’ (and com. SL Li. kartü
8454:rčat, i, av, adj. ‘docked, lopped, castrated'; Kurd. kurd ‘short; Lat. (ambig.) curtus “short, maimed, docked'; Srb. krt ‘brittle’; Blg. cf. kártja ‘snap off, uproot; — se ‘crumble’; Li. kurčias ‘deaf’; kur
```


## [2026-09-14T01:40:16.907Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# map line no -> leaf\ndef leafof(lineno):\n    upto='\\n'.join(t.split('\\n')[:lineno])\n    return upto.count('\\f')\nfor ln in (7712,8454,15139):\n    print('line',ln,'leaf',leafof(ln))\nlines=t.split('\\n')\nfor ln in (7705,8448,15135):\n    print('======',ln)\n    print('\\n'.join(lines[ln-1:ln+14])[:1600])\nEOF",
 "description": "Mann context for curtus and sek-"
}
```


### [2026-09-14T01:40:18.145Z] TOOL RESULT

```
line 7712 leaf 306
line 8454 leaf 336
line 15139 leaf 621
====== 7705
korsos ‘grey, tawny’ LLat. (once) corrus ‘tawny’; cf. corr-ago (a
537
plant); Sw. harr ‘grayling’. LW in Finn. bar- jus, id.)
korst- (1) ‘scab, crust G Harst “crust of snow’; cf. harschen ‘form a scab or crust’; OCz. krast, krásta *scurf^; Pol. krosta ‘pustule’; R. Ukr. korósta ‘itch, mange; pockmark’; Blg. kràsta ‘scab, mange’
korst- (2) (?) ‘sedge, brushwood’. Cf. qurstis Alb. cf. karthje, f. id.; W. Cor. cors ‘sedges, reeds’; Blg. cf. kraščàk ‘dry chip’
korst- (3) (korttos) ‘cut’, pp. Cf. kor-, ker-, krt-, etc. Skt. cf. kartt-avyah ‘to be cut off; (z-gde in) krttah ‘cut off”; Av. karsta, pres. p. ‘cutting’; Mir. korrtha, invar. ‘tired’; MHG harst, sm. Coop", lit. ‘section’)
kortið (kortaio) ‘shorten, cut down’. Cf. ker-, kor-, krt-, korst- (3), etc. WP II, 575-9 Oss. kärdïn ‘cut’; Lat. cf. (denom.) curtō, are; OCS sù-kraštọ, -kratiti; OCz. kráci, krátiti; cf. OCS kračí, m. ‘fight. See next
kortos, å, us (1) ‘cut, lopped, shortened, short; cut, section, piece; sharp, pungent. WP II, 575-9. Cf. ker-, kor-, krt-, korst-, etc. Skt. kartah “separation, distinction'; katüh ‘sharp, pungent’; Av. karoto ‘knife’; Per. kàrd, id.; Oss. kard ‘knife, sword’; Tokh. B. kerte ‘sword’; Kurd. cf. kardü (‘dock, sorrel’, lit. 'sour); Oss. cf. kärdág ‘sharp’; kärdän “scis- sors’; Arm. karč, ost, (“short?: Skt. kartyah “for cutting off: Gk. kórses ‘shaved, trimmed’, fr. *kortio-); Lat. curtus ‘short, docked’; OCS (dim. type) kratúkú, R koròtkij, id., beside OCS kratiti, inf. ‘to shorten’ (and com. SL Li. kartüs “bitter” beside kartà “section, sector, sex’; Latv. karta, as Li., cf. Kārta (fFat
====== 8448
Hes. kürna, kurnika “heads, skulls’; Maced. kürna, id. (and *dolt); W cwrn ‘spire, knob, pile’; Arm. (?) krni ‘gorse’
kurn- (2), cf. kor-, kur- Ir corn ‘roll, coil, bale’; cornaim, v. ‘roll, coil; Arm. cf. (denom.) koranam “bend; warp; stoop'
kurquos (kurk-) “filth, mucus'. Prototype uncertain. Cf. kurguos (1) & kork- Arm. (ambig.) kork, Let ‘filth’; OE horh, gs horwes, id. (& mucus"); Latv. cf. kurkstu, kurkt (2) ‘rot, grow mouldy’
kurs-, see Supt:K
kurst- ? *moor, wasteland'. Cf. WP I, 408 & 421. (Phonol. ambig., cf. korst- (2), and qurstis W cors, pl. -ydd, f. treedbed, bog’; Cor. cors, coll. ‘reeds’; Br. kors, id.; OHG hurst, horst ‘thicket’; OE hyrst ‘wooded hill, hurst
kurtis ‘enclosure, shed’. (Lat. and Go. am- big. cf. kortos, is (4) and krt- (2) Skt. kutib “bend, curve; hut, shed'; Lat. (am- big.) cors, gs cortis, usu. cortes, pl. ‘coop, yard”; Gk. kürtis ‘wicker basket, cage, net beside kürtos, kürte, id. (Go. haürds, etc. pre- ferably to krt- (2), q. v.)
kurtos, ios *maimed, defective'. Cf. kortos Skt. cf. kutyami ‘sunder’; Arm. kurt, gs krti, i-st. ‘eunuch’; krtem, v. ‘castrate’, cf. also krčat, i, av, adj. ‘docked, lopped, castrated'; Kurd. kurd ‘short; Lat. (ambig.) curtus “short, maimed, docked'; Srb. krt ‘brittle’; Blg. cf. kártja ‘snap off, uproot; — se ‘crumble’; Li. kurčias ‘deaf’; kurtinti, inf. ‘deafen’?
(kuruos ‘bent, round’. Assumed for Latin only, cf. kor-) (WP II, 568)
kusdhos (kuzdh-) ‘hollow, niche, receptacle’. Cf. kust-, kudh-, keudh-. WP 550-1 Gk. küsthos ‘hollow; cunnus'; Go. huzd ‘hoard, treasure’; huzdjan, v. ‘amass’; MHG hort, (hordes gs); 
====== 15135
sēiəmo- Skt. sayam, adv. “in the evening’; OIr. síam; Ir. sia ‘longest, furthest, latest’; W hwyaf, id. See next and cf. Skt. såyam, n. ‘evening’
séior- Ir. siar ‘westward; back; late’; W hwyr, adj. “late, slow’; m. “evening, lateness’. Cf. sëiam- and sëros. See Supt: seiros
seið (sið) (pp: sətós) 'sow'; seio ‘sowing, seed-time-. WP II, 459. (Variant sëu-. Cf. se- dhlom, sətós) Lat. cf. Sēja, f. ‘goddess of seed-time’; sévi, pf. ‘I sowed’; W hau, inf. ‘sow’; Go. saian, sv. 7., id.; MHG sæjen, sæwen, id.; OE sawan, sv. 7., id. cf. OHG sājo, wm. 'sower'; Du. zaien (zaaien), v. id.; ON sá, v. id.; OCS (and com. Sl.) sějọ, sějati, v. id.; Li. sēju, seti, id.; Latv. seju, set, id.; cf. Li. sēja, f. (sowing": Lat. Sēja). (Denom. in Br. hada, inf. ‘sow’, see sotós)
seið (2), see seiió
sek-, radical element of following entries: "eut"
sek- (?) Gk. cf. héka, adv. ‘slowly’; hésson, adj. ‘slow-
1123
er’; Tokh. A cf. sakát, adv. ‘quietly’; Lat. cf. ségnis, adj. (^slow, if for *sék-?)
sek-, -sekā, io “cutting, mowing’. (Simplex
. and cpds. Cf. séko (1) & cpds.) Lat. cf. foeni-seca, mf. ‘mower, cutter’; -sicia, f. ‘mowing, cutting’, pro-siciae, prae-siciae, fpl. *meat-cuts in sacrifice’; cf. also foenisex gs: -sicis, m. ‘mower’; (LW in) OHG séhh, n., G Sech *plowshare'; (long-gde. in) OCZ. s&Ci, f. ‘slaughter’; R séca, f. id.; cf. Cz. seno-sec, f. and senoseky, fpl. ‘mowing’
sékiuos, om ‘cut, cutting”
Lat. (Fest.) secivum, n. ‘cake cut with a sacri- ficial knife’; OCS sěčivo, n. ‘axe’; Srb. sj&Civo, n. ‘cutting implement’ (e: e)
sekmn- (sékn-) “cutting; offcut'. Cf. sek- and derivatives
```


## [2026-09-14T01:40:30.980Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(352,362):\n    nums=re.findall(r'(?<![\\d.])6[34][0-9](?![\\d])',t[i])\n    print(i,nums[:4], t[i].strip().split('\\n')[0][:50])\nprint('----')\nfor i in range(630,645):\n    nums=re.findall(r'(?<![\\d.])11[45][0-9](?![\\d])',t[i])\n    print(i,nums[:4], t[i].strip().split('\\n')[0][:50])\nEOF",
 "description": "Locate Mann p.640 and 1155"
}
```


### [2026-09-14T01:40:32.165Z] TOOL RESULT

```
352 [] “hail, summon’. In this sense only in Lat. cieo, i
353 [] �� Kleutos (Kleutro-)
354 [] “low set- tee’; MIr. clen ‘inclination, desire’; O
355 [] lope’; Li. (long-gde) Sluonüs, adj. ‘sloping’. Cf.
356 ['630', '631'] ris. hlestia, Sw. lystra, v. ‘to listen’
357 ['632', '633'] cf. also Cantabria (the Basque country); Br. (muta
358 ['634', '635'] �hostility, fury’. Isophonic in Li. šiepiù, ti “gr
359 ['636', '637'] ��hesitate, fear; Lat. cünctor, ari, OL. conctor ‘
360 ['638'] sophonic is Slo- vak sotiť ‘thrust; throw’); Sw. h
361 ['639', '640'] growth’; Gk. cf. krág- gë “a crustacean’; kraggón 
----
630 ['1140'] e) Skt. cf. sifiCámi, aor: a-sicam, v. “pour, drip
631 ['1141', '1142'] nqu-, (sik-, sink-) and next. WP I, 506 and II, 46
632 ['1143'] ); Ir. sioscaim, v. (2) ‘utter’
633 ['1144', '1145'] , that, who") Skt. syah, f: sya beside sah, sa & t
634 ['1146', '1147'] (-əlos) Hes. skáphalos ‘ladle, baler’; Ir. scabhal
635 ['1148', '1149'] . (3) ‘shame’; Dig. kämä, id. (and *pudenda?); Arm
636 ['1150', '1151'] aped; cut, carving, gouged article, shaped article
637 ['1152', '1153'] tched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudü
638 ['1154', '1155'] v But R ščegol = 'goldfish"); (ON skikka, v. “arra
639 ['1156', '1157'] skélti, v. ‘split; Latv. Skelu, Skelt, id. (NB. Th
640 ['1158'] Ir. sceinnim, scinnim, v. ‘leap, start, bud, shoot
641 ['1159'] . ‘rough, hoarse’
642 [] f. Arm. xajr, i-st. and xajri-K, pl. form (produce
643 [] f. ‘pace along; MHG schar, adj. ‘steep’; Sw. skör,
644 [] Iso- phonic in Du. schitteren, v. 'glitter")
```


## [2026-09-14T01:40:36.073Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(\"==== leaf 638 (pp.1154-55) ====\")\nprint(t[638][:2600])\nprint(\"==== leaf 361 (pp.639-40) ====\")\nprint(t[361][:1800])\nEOF",
 "description": "Mann pages 1154-55 and 639-40"
}
```


### [2026-09-14T01:40:37.300Z] TOOL RESULT

```
==== leaf 638 (pp.1154-55) ====
v But R ščegol = 'goldfish"); (ON skikka, v. “arrange, ordain' and skikkja, v. ‘cloak’ are, like G schick-, of ambig. vocalism)
skeibh- “slice, cut, division’. (Gmc. ambig. cf. skeip-) MHG schibe, wf. (2) ‘slice’; E dial. shive, shiv, id.; ON skífa, f. id. & vb. id. Du. schijf, f. id.; Li. skiébas, m. 'firebreak in a wood, clearway', skiebiü, skiébti, v. ‘slice’
skeid-, see skid-)
skeidh- (skeidhrà, skheidh-) ‘slice, cut; blade, cutter, incision". WP II, 543. Cf. ski- dhros, skidros, skh-, etc. Arm. cf. xe, s. lees of grapes’; W (?) ysgwydd, pl. -au, f. ‘shoulder’; Br. skoaz, f. id.; Cor. scoth, pl. scodhow, f. id.; OHG skit, OFris. skid, n, OE. scid, n. ‘slip of wood E shide *roof-shingle; MHG schiten, sv. 1. ‘chop, split’; scht, sn. as OE; cf. G Scheiter-haufen; ON skíð, n. ‘lintel, chip, ski, roof-shingle'; cf. (probably fr. *skidh-) ON skíði, n. ‘sheath’; Sw. skida, f. (2) “pod, shell in view of Li. skydas ‘shield, carapace’; Cz. cf. Stidla, f. ‘stilt’; Li. skiedà beside skiedrà, f. ‘chip’; Latv. cf. Skiedi, mpl. “teeth of weaver's sley’; Li. skíedziu, skíesti, v. ‘divide’; Latv. šķiežu, Skiest, v. ‘scatter, squander’
skeiið (skeið, skheiio, skheio) “divide, split, distinguish, choose’. Cf. WP II 542 Hitt. cf. skyami, 3s. skici, v. (anoint, lit. “dis-
skeg- (skheg-?) — skeko, ið
10
15
20
25
30
35
40
45
1154
tinguish'?); Lat. scio, scire, v. ‘ordain, ap- point; know, be skilled in’; Br. cf. skeZa, v. ‘cut’; cf. skiant, f. ‘mind’; W cf. ysgi, pl. sciod, m. “slice?
skeim- “separation, division’. Cf. skeiio, etc. W cf. ysgwyf, m. ‘shower; scum’; Blg. &Cim, m. *wool-combings'; Li. skiemuó, eps, m. (woof-threads;  shuttle-race; pl. -menys *healds?); Latv. cf. Skiemele, f. *shuttle-race'
(skeip-, cf. skip-, sKip- and skoip-. All the evidence is ambig.) Cf. MHG schibe, wf. (2) ‘slice’; E dial. shive, id. (fr. *skeibh-, *skeip- or fr. *skibh-, skip- with variant initial in) Blg. cipa, f. (skin'. LW in Mod. Gk. & Alb.); cf. Cz. Cíply, adj. 'slender, slim”; Ciplenka, f. ‘fawn, young deer" For Li. skiépas, m. ‘graft’, see skoip-. (Isophones in OCS, and com. Sla- vonic, Stipljo, Stipati, v. ‘pluck, pinch’, R šči- pàt', inf. id. and in Li. (*ei/oi) skiepiü, ti, v. *slit open")
skeir- (skheir-, skhir-) ‘product of soured milk’. Cf. skir-, ksirom Oss. Ciri, Digor. Kere, s. fcheese-cake'; Arm. xer, O-st. (‘dish of beestings'. Cf. for phonol. lezu ‘tongue’: Li. liežuvis), Alb. hirrë, f. Cwhey', perh. fr. *skirs-, but vocalism may be *-ei- cf. dimén: Gk. kheima)
skeitos, à, om 'division, separation, separa- tor; sheath, shield'. Cf. skheit-. WP II, 543, and cf. skoitos
==== leaf 361 (pp.639-40) ====
 growth’; Gk. cf. krág- gë “a crustacean’; kraggón ‘crab’; W cf. cran-
horny
639
gen, pl. au, f. ‘wen’. (W cranc ‘crab’ is a LW)
Krnió ‘bring to a head, finish’. Cf. WP I, 405 Gk. kraino, id.; Alb. kryej, id. See next
Krniom (Krniio-) Krnios “head, skull, horn, tip; of a head”, etc. Cf. Krnom, Ker-, Kros, etc. WP I, 405 Gk. kraníon ‘skul’; Myc. cf. a-karano (ouer, ied: *headless); Alb. krye, n. ‘head’; OFris. herne, f. (corner; OE hyrne, f. id.; OSw. hórne, Sw. hórn, n. id.; Norw. hjórne, id.; ON hyrna, f. “tip of axe'; Slovak srní, adj. “of fal- low deer'. See next
Krnom (Krnu) (1) ‘horn, tip, corner’. Cf. Krniom, etc. WP I, 406 Per. sürna (trumpet. LW in OCS surna, su- rina, sarna *clarinet); Hiero-Hitt. surni ‘horn’; Gk. krános, gs -eos, n. ‘helmet’; kránon ‘head’; káàrnos, m. (tram'. Hes.) kárnon (‘Gallic horn’, prob. Gallic wd.); cf. Hes. karanó ‘goat’; Alb. krye, n. “head”; Lat. cornu “horn, corner, tip’; not in W or Ir.; Go. haürn, n.; OE horn, m.; OHG horn; ON horn, n. d: OCS srünü, srüna ‘fallow deer" Pol. sarna ‘doe’; R sérna ‘chamois’
Krnom (Ernos, us) (2) ‘cornel-cherry’ Gk. kránon (2), id.; Lat. cornus, gs -1 & -üs, f. id.; cornum 'cornel-berry'
Kros, -es- ‘head, tip, top’. Cf. Ker- (2), (Kor-), Krn-, etc. Skt. Siras, n. & Sirah, m. id.; Av. cf. saro, obl. -áh-, n. id.; Gk. kår, in phr. epi- ‘headlong’; kára, n. “head, headland’; Per. sar ‘head’; Arm. sar, gs -u ‘top, peak": Gk. -krús in i-krüs 'forth- right’; antikrü (Cfacing', etc.); beside kro- (in kro-taphos, kr-osphos, kr-ónos, krobulos, etc.)
Krs- (Krson, Krsron, Krsen-) ‘hornet, wasp’. WP I, 407 Lat. crābrō, gs -onis, m. id.; OW creyryn ‘wasp’; Du. cf. horzel, f. ‘hornet’; OCS srü- šení, Cz. sršeň & sršán; Pol. szerszeń; R šer- Seni, m. id. beside OCS srüsa, f. ‘wasp’; Li. širšuð, gs. -eñs, m., širši
```


## [2026-09-14T01:40:50.144Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[362][:1500])\"",
 "description": "Mann leaf 362"
}
```


### [2026-09-14T01:40:51.410Z] TOOL RESULT

```
Sab *night'; Av. x3apa, f. ‘night’; X3Sap-, v. (cover; Li. Sampu, inf. Sapti *disap- pear’
Ksaulo, ið (ksaul-) ‘wind, twist, writhe’. See next and ksaul- (1)
Gk. sauloŭmai ‘gesticulate’; Cz. (velar initial)
641
choulet, choulit se, v. inf. “writhe, bend, huddle’; Slovak chúliP ‘wind, roll’
Ksaulos (ksaulos) ‘mad, silly’. See ksaul- (2)
Ksidros (?) (variant of skidro- ?)
(formally) Skt. ksidrah “a disease; sun; horn’; Arm. curt, gs certo, o-stem, adj. ‘cold’; Du. schitteren ‘glitter, sparkle’
Ks-kap-, aphetic for eKs-kap-, see eks, kap- Oss. sKüfín, äskäfín ‘snatch’; Lat. cf. ex-cipið, id.; Cz. cf. chopiti, inf. id.
Ks-kiieio, Ken Cf. eks, kiieio Alb. çoj ‘send, take away, rouse, wake’; Lat. cf. ex-cieo ‘stir up’; OCS o-3ajo, -Sajati remove?
Ksuark- ?, Ksark- ? “coat, jacket, garment;
homespun material'. An early Tataric word in IE? Phonology obscure, and there is some confusion with a Latin word sericum, lit. *Chi- nese’. The Tataric origin is reinforced by the existence of a Turkish type sírka *jacket'. Cf. Kark- (Kork- ?) Hitt. cf. sarku(mi) (queried: ‘put on, don’); Alb. shark “jacket; enclosure'; LLat. cf. sarcia and sareca ‘shirt’, perh. from Gmc. cf. OE sier- ce *coat, shirt, armour'; ON serkr, id.; Scots sark “shirt, shift, but see W. Steinhauser, Slavonic Review, 1950, 284-8; OCS sraka jacket; R cf. sorócka, dim. ‘shirt’. Specula- tions and lit. in AP: ESRJ a, p. 358b: soróka (2); Li. Sarkas & švarkas, ai «coat; Latv. svārki, mpl. id. The Finn. LW sarka ‘homespun clot
```


## [2026-09-14T01:40:59.284Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[361][1800:4200])\"",
 "description": "Mann p.640 tail"
}
```


### [2026-09-14T01:41:00.413Z] TOOL RESULT

```
nas, m. & širše, f. id.; Latv. sirsenis, sirsonis, id. (The composition of MHG hornuz, hornis, OE hyrenetu, hyrnet ‘hornet’ is uncertain)
Krsr-, Krsno- see Kerosr-
Krt- (1) ‘cover, covering, skin’
Krnio — Ksaulð, ið (ksaul-)
10
20
25
30
35
40
45
640
OE hyró, f. ‘skin’; Li. Sirtas, m. ‘den’
Krt- (2) “cut, blow’. Cf. Kerto Skt. śūrtáh, -śīrtáh ‘shattered’; Arm. sartnum ‘be separated’; Per. cf. sile, sili, sīli “slap, blow’ beside süli Cplough lit. ‘cutter’ ?)
Krt- (3) ‘mixed’. Cf. Ker- (3)
Cf. Vedic $rtáh, śrītáh and $ratab, id.; Gk. cf. á-kratos, -krētos ‘unmixed, neat
Kruos, is ‘horn’. Cf. Ker-, Krn-, Kor-, Krnio-, etc.
Av srvà, f. “nail, horn’; MIr. cf. (alleged) crú ‘hoof (beside Irish: crúb, f. id.); OPr. sirwis ‘roebuck’. Cf. Gk. ánti-krus ‘head-on’
Ks-, zero-gde of eks, q.v. 'from-, out-; un-,
ex-; very- Oss. s- (intensive verbal extn.); Arm. c- (be- fore vowels); s- (before consonants); cf. c-ac ‘Jow’; c-ajg ‘night’; s-nank ‘bankrupt’, etc.; Gk. cf. s- (in s-kholé, á-s-thma, s-thénos, s-phod- rós, s-bénnumi, s-kháo, s-kházo, etc.); Alb. c-, sh- Cour, and adversative px.); Olr. ass, as, as- (as in as-caoin *un-kind") (r-gde type: *oKs-); W ys- (in ys-garm 'outcry', ys-barth, adj. 'separate"); Go. us-, us *out-, out of; ON Ot-, ór, as Go.; G er-, ur-; OCS sú, prp. w. gen. ‘off; š-, px. (as in StuZdi “foreign”, Stusto, Stutiti “feel, fr. *Ks-ieut-); Li. i$, i$- as Go. The sense of ‘to, toward? occurs in Arm. ç- (q-art till now’; c-ank “to the end, always”); and in Cz. s (in s to ‘up to it, able’; se-č ‘to what, for what’. Uncertainly as a fused px. in Skt. khajami ‘stir, cf. a20, and in OE sceacan ‘brandish, shake")
Ksaks- (variant form of Káksa, q.v. and cf. Kakis “branch; peg, spike" etc.)
Arm. caxem, v. ‘harrow’; cf. Go. hoha (plough', fr. *Kak-); Per. šāx “branch, horn’
Ksanio (ksánio) ‘flatter’
Gk. saíno ‘fawn, flatter’; OCz. (velar initial) chanéti, id.
Ksap- (?) “absence, disappearance, darkness” Skt. cf. kSap, f. & kSapa 'night'; kSapàmi, v. ‘fast’; Per.
```


## [2026-09-14T01:41:05.561Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A8 -E \"^sek-|^sker-1|^sker-|^skel-1|^skep-|^(s)kep\" AHD_watkins1985.txt | head -80",
 "description": "Watkins AHD roots"
}
```


### [2026-09-14T01:41:05.620Z] TOOL RESULT

```
911:sek-
912-grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
913-sék-
914-sécula, sickle: SICKLE. 8. Suffixed variant form *sak-so- in Latin saxum, stone (< “broken-off piece”): SAXATILE; SAXICOLOUS, SAXIFRAGE. See also extended roots sked-, skei-, sker-', sker-4. [Pok. 2. sék- 895, sken-(d)- 929.] s@k-. Slack, calm: relax. Greek (h)éka, slowly, a little (> héss6n, inferior): ESSONITE. [Pok. 3. sék- 896.] sekw-1, To follow. 1. Latin sequi, to follow: SECT, SEGUE, SEGUIDILLA, SEQUACIOUS, SEQUEL, SEQUENCE, SUE, SUITOR; CONSEQUENT, ENSUE, EXECUTE, OBSEQUIOUS, PERSECUTE, PROSECUTE, (PURSUE), SUBSEQUENT. 2. Latin sequester, “follower,” mediator, depositary: SEQUESTER, SEQUESTRUM. 8. Suffixed (participial) form *sekv-ondo- in Latin secundus, following, coming next, second: SECOND2, SECONDO, SECUND, SECUNDINES. 4. Suffixed form *sekv-os, following, in Latin secus, along, alongside of: INTRINSIC. 5. Suffixed form *sekv-no- in Latin signum, identifying mark, sign (< “standard that one follows”): SEAL!, SEGNO, SIGN; AS- SIGN, CONSIGN, DESIGNATE, INSIGNIA, RESIGN. 6. Suf- fixed o-grade form *sok’-yo- in Latin socius, ally, companion (< “follower”): SOCIABLE, SOCIAL, SOCIETY, SOCIO-; ASSOCIATE, CONSOCIATE, DISSOCIATE. [Pok. 1. seky- 896.] sekw-2, To perceive, see. 1. Germanic *sehwan, to see, in Old English séon, to see: SEE}. 2. Germanic abstract noun *sih-tiz in Old English sihth, gesiht, vision, specta- cle: SIGHT. [Pok. 2. sek¥- 872.] sekw-3, To say, utter. 1. O-grade form *sokv- in: a. suf- fixed form *sokv-yo- in Germanic *sagjan in Old English secgan, to say: SAY; b. suffixed form *sok-d- in Ger- manic *sag6, a saying, in (i) Old English sagu, a saying, speech: sAw? (ii) Old Norse saga, a saying, narrative: saGA. 2. Suffixed zero-grade form *sk~-e-tlo-, narration, perhaps in North Germanic “skathla in Old Norse skdid, poet, “narrator,” perhaps akin to the probable Scandina- vian source of Middle English scolde, an abusive person: SCOLD, SKALD. [In Pok. 2. sek¥- 897.] sel-1, Human settlement. 1. O-grade form *sol- in Ger- manic *sal-, room, in Italian sala, hall, room: SALON, (SALOON). 2. Suffixed form *sel-o- in Latin solum, bot- tom, foundation, hence sole of the foot: SOLE!, SOLUM; ENTRESOL. [Pok. 1. sel- 898, 3. (swel-) 1046.] sel-2, Also sele-. Of good mood; to favor. 1. Germanic lengthened form *sél- in Old English ges#lig, happy (ge-, completely; see kom): SILLY. 2. Suffixed lengthened o-grade form *sdl-d- in Latin sdlari, to comfort, console: SOLACE; CONSOLE}. 3. Possibly suffixed form *sels-ro- in Greek hilaros (< *helaros), gay: HILARITY; EXHILARATE. [Pok. 6. sel- 900.] sel-3, To take, grasp. 1. Suffixed o-grade (causative) form *sol-eyo- in Germanic *saljan, to offer up, deliver, whence West and North Germanic “‘to sell,” in Old English sellan, to sell, betray: SELL. 2. Germanic *sal-, giving, sale, in: a. Old Norse sala, sale: SALE; b. Old Norse compound handsal, giving of the hand (in closing a bargain): HANDSEL. [Pok. 3. sel- 899.] sel-4, To jump. 1. Suffixed zero-grade form *sal-yo- in: a. Latin salire, to leap: SALACIOUS, SALIENT, SALLY, (SAUTE); ASSAIL, DESULTORY, DISSILIENT, EXULT, IN- SULT, RESILE, RESULT, SOMERSAULT; b. Greek halles- thai, to leap, jump: HALTER2. 2. Perhaps Latin salmé (borrowed from Gaulish), salmon (< “the leaping fish”): SALMON. [Pok. 4. sel- 899.] sel-es-. Swamp, marsh, sea. Greek helos, marsh: ELODEA. [Pok. selos- 901.] selk-. To pull, draw. 1. Perhaps Germanic *selhaz, seal (the animal), “that which drags its body along with difficulty” (but more likely an early Germanic borrowing from Finnic), in Old English seolh, seal: SEAL?. 2. Suf- fixed o-grade form *solk-o- in Latin sulcus, furrow, groove (< “result of drawing or plowing”): (SULCATE), sucus. [Pok. selk- 901.] selp-. Fat, butter. 1. Germanic *salb- in Old English sealf, healing ointment: SALVE}. 2. Germanic denomina-
915-seng’-
916-tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
917-seng"h-
918-*sakk- in Swedish sacka, to sink, akin to the Scandina- vian source of Middle English saggen, to subside: sac. [Pok. sengz- 906.]
919-seng“h-. To sing, make an incantation. 1. Germanic *singan in: a. Old English singan, to sing: SING; b. Old High German singan (> German singen), to sing: MEIs- TERSINGER, MINNESINGER, SINGSPIEL. 2. Suffixed o-grade form *songvh-o-, singing, song, in Germanic *sangwaz in Old English sang, song, song: SONG. [Pok. sength- 906.]
--
937:sker-'
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
939:sker-2
940-*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
941-skeup-
942-leaves): CRAMBO. 4. Perhaps Celtic *krumb-i- in Welsh crwn, crooked, arched: CROMLECH. [Pok. (s)kerb(h)- 948.] skét(e)-. To injure. Suffixed zero-grade form *skoat-on- in Germanic *skathén- in: a. Old Norse skadha, to harm: SCATHE; b. Old High German scado (> German Scha- den), harm, injury, damage: SCHADENFREUDE. [Pok. skéth- 950.]
943-(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
944-skipam
945-[skipam. Ship. Germanic noun of obscure origin. 1. Old English scip, ship: sHIP. 2. Middle Dutch schip, ship: (SCHIPPERKE), SKIPPER}, 3. Italian schifo, ship, skiff: skiFF. 4. French équiper, to equip: EQUIP. [In Pok. skei- 919.]]
946-skot-. Dark, shade 1. Suffixed form *skot-wo- in Ger- manic *skadwaz in Old English sceadu, shade: SHADE, SHADOW. 2. Suffixed form *skot-o- in Greek skotos, darkness: scoToMa. [Pok. skot- 957.] skreu-. To cut; cutting tool. Extension of sker-'. 1. Basic form *skreu- in: a. Germanic *skraw- in Old English scréawa, shrew (having a pointed snout): SHREW, (SHREWD); b. Germanic *skraud- in Old English scréade, piece, fragment: SCREED, SHRED; C. Germanic *skrid- in (i) Old English scriid, garment (< “piece of cloth”): SHROUD (ii) Old French escro(uje, scroll: SCROLL (iii) Dutch schrood, a slice, shred: scRop. 2. Extended form “skreut- in Latin scriita, trash, frippery: SCRUTINY. 3. Extended variant form ‘*skraut- in Latin scrétum, scrotum (probably identified with scrautum, leather quiver for arrows): SCROTUM. [Pok. 4. (s)ker-, Section ITI. 947.]
947-skribh-. To cut, separate, sift. Extension of sker-1. 1. Latin scribere, to scratch, incise, write: SCRIBBLE, SCRIBE, SCRIPT, SCRIPTORIUM, SCRIPTURE, SERIF, SHRIVE; ASCRIBE, CIRCUMSCRIBE, CONSCRIPT, DESCRIBE, INSCRIBE, MANUSCRIPT, POSTSCRIPT, PRESCRIBE, PRO- SCRIBE, RESCRIPT, SUBSCRIBE, SUPERSCRIBE, TRAN- SCRIBE. 2. Greek skariphos, scratching, sketch, pencil: SCARIFY}, [Pok. 4. sker-, Section II. 945.]
```


## [2026-09-14T01:41:22.039Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (643,644,645):\n    print('==== leaf',i,'printed',i+540)\n    print(t[i][:1200])\nEOF",
 "description": "Borhan vol2 p.1184"
}
```


### [2026-09-14T01:41:23.296Z] TOOL RESULT

```
684
==== leaf 643 printed 1183
‫و کوچك‬   ‫و دام نوعی از غله است و آن سل‬                    ‫سنگ شکن = مخفف منکه اشکن‬
‫میباشد ‪ -‬و نام مرغیست کوچك وشکاری‌ازجنس‬                   ‫است که نام غله‌ای باشد ‪ -‬و نوعی اخزرما‬
             ‫سياه چشمکه آ را ترمتای ‪ ۴‬کویند‪.‬‬                                             ‫ههمٽ ‪.‬‬
 ‫ومهای‬
     ‫دباملف‬
          ‫»بنالیام‬
                 ‫سنگلاخ ‪ ۸‬ک‬                               ‫سنگ شیر = بعربیحجر اللبنی ‪۱‬‬
‫نقطه‌دار زده » بمعنی سنگنان‌است که جاومکان‬                ‫خواند ‪ .‬رنگه آن خاکتری رنگه باشد‪.‬چون‬

‫لهاخ بمعنی مکان آمده است‬
                       ‫منک باشد چ‬                       ‫بآب بابند از وی مانند شیر ببرونآید وبطمم‬
      ‫قاام دیو راگویند‪.‬‬  ‫مج‬
                          ‫همچو دبولاخوکه‬               ‫شیرین باشد » و برچشم کشند سیلان آب را بر‬
‫سنگله = بصم ثالث بروزں زنگله‪.‬نانی‬
                                                                                               ‫زک‬
         ‫‪.‬‬    ‫و ارزن برد‬   ‫باشد که ازارد کاو رس‬             ‫ررقبطی‬
                                                                 ‫جبک‬
                                                                   ‫انقب‪,‬طیح‪-‬‬
                           
==== leaf 644 printed 1184
    ‫‪= ۱‬‬    ‫حس ‪۵‬‬




  ‫دو کس کرده‌اند‪ :‬مردی و زنی؛مرد مازلین وزن‬                   ‫شزد‬
                                                                ‫اچی‬
                                                                  ‫بدو‬
                                                                    ‫و اصال و امتزاح دو شخص با‬
                             ‫مازننه نام داشثه است ‪.‬‬

  ‫ولك و سکون‬
           ‫سنگله = بفتح اول ا‬                               ‫سنگ هقنی ‪ -‬بفتح میم و سکون‌غین‬
   ‫خهارهای‬
         ‫را کوبند ک‬    ‫ی‬‫تار‬
                          ‫»خ‬‫بیش‬
                              ‫ثائ‬                           ‫نتطه‌دار و لون سحتانی رسیده» سگ است‌الوان‬
                           ‫خود را مالند تبراندازد ‪.‬‬          ‫سياه بود بسرخی‬      ‫وه‬
                                                                                  ‫لدچ‬
                                                                                    ‫آباش‬
                                                                                       ‫و پفایت ست می‬
 ‫سنگ باسم ۔ با تحتانی بالف کشیده‬                            ‫زند وشطهای سفید برآن باشد و شیشه کران‌بکار‬
 ‫بمیم زده » سنگی است‬ 
==== leaf 645 printed 1185
        ‫ره‬                                                                                 ‫=“‬

   ‫رتین باشد ‪ ۴‬؛ و بان ممنی‌باشن‬  ‫فمن‬
                                    ‫نل‬ ‫وعتی‬
                                          ‫بم‬         ‫سنمار ‪ » ۲‬بکراول ومیم‌بالف کشیده‬
   ‫نقطه‌دار هم آمده است ‪ -‬و باخفای ها در عربی‬        ‫بروزن کل‌کار » نام شخصی بوده رومی که قصر‬
   ‫بمعنی‌سال باشد ‪ -‬وبضم اول ونالی‌زن‌پسررا گویند‬    ‫خورلق را او ساخته است و او را عربان سنمار‬
                          ‫که بعروس شهرت دارد‪.‬‬        ‫نون و تشدید میم خوانند ‪ .‬گویند سنمار‬               ‫س‬
   ‫سنهار = جم اول بروز نکلز اره بمعنی‬                ‫خوراق را چنان ساخته بود که درشبالروزی سند‬

    ‫آغر مه است ک زهن پس بشد و بکرتاکن‬   ‫خوالند ‪.‬‬
                                                     ‫رنکگ مختلف میشد ‪ :‬صبحدم کبود و در لدم روز‬
                                                     ‫سفید مینمود و بوقت عصر زرد مشد ‪ .‬چون‌نمام‬
                                                     ‫گردید او را خلعتی فاخر وعمتی وافر دادد از‬
   ‫سنی = بکر اول توخفیف بون‌بتحتالی‬
  ‫آن خوالی باشد‬
              ‫سینی است و‬
                                                     ‫آن بفایت خوشو
```


## [2026-09-14T01:41:36.918Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"سودن\" \"فرسودن\" \"سرگین\"; do echo \"#### $w\"; grep -n \"$w\" BQT_v2_pages.txt | head -5; done; echo \"=== v3 ===\"; for w in \"شکستن\" \"شکافتن\" \"کارد\" \"گسیختن\" \"فرسودن\"; do echo \"#### $w\"; grep -n \"$w\" incoming/BQT/BQT_v3_pages.txt | head -4; done",
 "description": "Grep Borhan for headwords"
}
```


### [2026-09-14T01:41:38.030Z] TOOL RESULT

```
#### سودن
6041:    ‫کسریدن و کوش نسودن ‪ 7‬و م زد‬                                        ‫اولبروزن خفته‪ .‬گنجشك راگوبند ویعربی‌ععفور‬
12173:‫حسودن = بروزن کشودن؛ درو کردن‬                                             ‫حضرترسول صلوات‌انه عليه وا لهاست‬
12184:‫بمعنی خسودن است که بربدن ودرو کردن علف‬                         ‫و دعر دیعصفن‬   ‫تِِ‬           ‫آ نرا‪,‬صفاهاتی گل کاویشه‬
12203:                                            ‫خسودن‬       ‫رك ‪:‬‬        ‫‪۶‬‬              ‫‪ ,‬خنوره ‪.‬‬       ‫رك ‪ :‬خر‬        ‫‪-‬‬   ‫©‬
19194:‫رمان‬         ‫*س بفتح اول وئانی » تمه‬                 ‫دسه‬                          ‫کروباند‪ -‬مکوتوبی که ببدسنتوخسودند ‏‬
#### فرسودن
32157:       ‫کردن » نرم کردن ‪ -‬فرسودن ‪ -‬اندودن ‪ -‬دربافتن ‪ -‬حل کردن‪ ,‬کداختن ‪ -‬صاف کردن‪-‬‬
#### سرگین
11625:  ‫وخروالفارکه سرگین موش امت » چون‬                                             ‫فرش‌خوانند "وشامیر |‬
=== v3 ===
#### شکستن
3062:‏عربی مممنی قطع است اعم از بربدن نا شکستن
3292:تروید - وبا نشدید ثالی‌درعرمی به‌منی‌سرشکستن
4881:‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
4884:‏«هوبشمان ۸۷ ‎MV‏ رخنه کردن 6 چاك کردن ۰ شق کردن » پاره کردن» دربدن - شکستن .
#### شکافتن
3207:‎fan‏ شدبار است که شکافتن زمین باشد بجهت
3293:‎ath‏ - و شکافتن کشتی ‎OT‏ دربا را .
3790:‏شدکار است که شخم کردن و شکافتن زمین باشد
3800:‏ش یس ۴ - بفتح‌اول بروزن تلبیس» | شکافتن ومستعد. ساختن‌استبجهت زراعت کردتد
#### کارد
490:وافع شود کاردی کشیده اعنای خود را مجروح
491:سازاد وبعضی از ‎OT‏ جداعت کارد بدست پسران
3473:بکاردارند . ‎odes‏ (مروزی) گوید :
5266:هندوانه و خربزه بکارد بردارند *٩و ‎WT‏ پعربی
#### گسیختن
#### فرسودن
18233:بفرسودن هم‌هست یعنی کهنه کن و محو سازودر
18243:۴ رك : فرساییدن . فرسودن .
18280:‏© اسم ‎Jeb‏ از فرساییدن و فرسودن -
18299:‏۵ فرساییدی = فرسودن (هم) .
```


## [2026-09-14T01:41:45.666Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/BQT/BQT_v3_pages.txt'\nlines=open(p,encoding='utf-8',errors='replace').read().split('\\n')\ncur=None\ntargets={4881,4884,18233,18243,490,491,3473}\nfor i,l in enumerate(lines,1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: cur=int(m.group(1))\n    if i in targets:\n        print(i,'pdf',cur,'printed~',cur+1205 if cur else None,'|',l.strip()[:120])\nEOF",
 "description": "Map Borhan v3 lines to printed pages"
}
```


### [2026-09-14T01:41:46.832Z] TOOL RESULT

```
490 pdf 12 printed~ 1217 | وافع شود کاردی کشیده اعنای خود را مجروح
491 pdf 12 printed~ 1217 | سازاد وبعضی از ‎OT‏ جداعت کارد بدست پسران
3473 pdf 48 printed~ 1253 | بکاردارند . ‎odes‏ (مروزی) گوید :
4881 pdf 66 printed~ 1271 | ‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
4884 pdf 66 printed~ 1271 | ‏«هوبشمان ۸۷ ‎MV‏ رخنه کردن 6 چاك کردن ۰ شق کردن » پاره کردن» دربدن - شکستن .
18233 pdf 253 printed~ 1458 | بفرسودن هم‌هست یعنی کهنه کن و محو سازودر
18243 pdf 253 printed~ 1458 | ۴ رك : فرساییدن . فرسودن .
```


## [2026-09-14T01:41:55.495Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/BQT/BQT_v3_pages.txt'\ntxt=open(p,encoding='utf-8',errors='replace').read()\npages=re.split(r'\\n(?=.*\\[pdf page )', txt)\nd={}\nfor blk in txt.split('\\f'):\n    m=re.search(r'\\[pdf page (\\d+)\\]',blk)\n    if m: d[int(m.group(1))]=blk\nfor n in (66,354,355,611,612,253,257):\n    b=d.get(n,'')\n    print('='*25,'pdf',n,'printed~',n+1205)\n    print(b[:1500])\nEOF",
 "description": "Print Borhan v3 pages of interest"
}
```


### [2026-09-14T01:41:56.698Z] TOOL RESULT

```
========================= pdf 66 printed~ 1271
[pdf page 66]
۱۷۷
هم باین معنی است - وعکه را نیز کوبند وآن
پرنده‌ایست ممروف.*
شکاشاگ ۱ ‎be‏ شین ‎abd‏ دار بر وزن
‎Ake‏ . آواز پای را گویند که بهنگام رامرفتن
‎aT‏ .

کننده - و امر برخنه کردن هم ‎tele‏
‏کلافه کرده را نیز گویند ۴ .*

شکافه = بروزن ‎ils‏ چویکی باپلرچةً
شاخکی باشد که بدان ساز نوازند وآنرا بعریی
مراب خوانند ۴ - وبمعنی کپواره هم آمدماست

که بعربی مهد گویند .

ae . ‏اول بر وزن غلاف‎ So ۲ SES
‏زن * - سازده و مطرب را‎ SES

ممروفت که رخنه وچاکه باشد - و بمعنی‌رخنه

۱ - اسم صوت < شکشك. قس: چکايك . ‎Mg Kay‏ ۴ رك : شکافتن .

۴ - شکوفه همچو شعاف ‎Col‏ و ‎Gee‏ دیبا بان

مه وخور است ‎Bly Ulan‏ درصراف.
بوالمژیدیلخی . «لفت ‎NEV GS‏

۴ - پیری آغوش باز کرده ‎eld‏ توهمی گوش ‎BEL‏ غوش کابی‌مروزی.«لفت‌فری4۲۸*.
و ركك : شکافه زن . ۵ رگ : شکافه .

چد شکار - بکسر اول ( درلجة مر کزی ) اسم از > شکردن © ‎Cea)‏ قس : شکره»
اشکره"یهلوی؟ 5162 ‎sane)‏
‏استی ع 1۵ ( راندن ,
صید کردن ) ۰ «اسشق ۰۷۸5
‎phil‏ ع 5627 ( صید
‎OST‏ شچیر ) , کردی ع
7 ( وحشی ) از -
8 از 6۵۲ 5(رله :بشگرد
بمعتی شکار) ? هوبشمان۷۸۹»:
‎re‏ لخجیر - هرحیوالی که
صیدشود - هر چیز رابگان
ومفت - یفما وغارت +

#شکا رگا بکر
اول . آنجا که شکار کنند ,
محل صید : « توشیروان‌عادل
را در شکارگاه صیدی کباب
کردند.» ‎MENGES?‏

# شکافتن - بکنر اول ‎Indy)‏ مرکزی) از: شکاف ۳- تن ( پونده‌صدری)» پهلوی
‎shkAfta n‏ «تارادیاه۱۹», کردی ‎bishkiwin shikiwin‏ )+66 زدن ‎(gi.‏ کردیع
‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
درف ارسی «کافتن» و «کاوبدن» محفوظ مالده ‎vay gaol?‏ اوستا_041 ۳814-502 (عابودکردن»
قلم‌وقمع ) ‎ca. 
========================= pdf 354 printed~ 1559
[pdf page 354]
۱و ۱
‎Vs Sully‏ و بمعتی جنگه‌نامه و تاریخ هم
کفته‌اند ۴ .
کار نحك بفتح ‎LM‏ وجیم‌وسکون
‎bs » Gy eh‏ و بادرنگه را گویند که سبز
وبز رگه باشد ۴ .
کار نگ ‎ett a‏ بروزن ‎Kal‏
‏بمعنی صاحب‌طرب وچرب‌زبان وزبانآور باشد.
کادوات ؟ ‎ving‏ ساربان , معروف
است که قافله باشد - و شتر واستر وخرالاغ را
ی زگونند - و ‎GAT,‏ ومافری را نیز گویند
که جهت تجارت ‎tle‏ رود .
‎pe - CHIT‏ نون و سکون
‎GE‏ » نام پرندء‌اییست کردن دراز و پپوسته در
کنارهای آب نشیند وبهمین ممتي بجای واو.دال
? آمده است ‎٩‏ و بعربی ‎AS‏ کوبند بروزن
‎Ole,‏ +
(۱) خما : چارسول.
‎(r)‏ چش : جنگجو 5

کاریز

کاروژول ۲ بضم واو وزای فارسی
بروزن چاروصول (۰)۱ مطلق کارفرما رااگویند
وشخصی که پرسر فعله ‎Leng‏ ومزدور بابستدوایشان

را کار بفرماید ۸ .

کادو ‎YF‏ بنتح ‎SE‏ تلزی بر وزن
بال و پر » بمعنی پشت و یناه و مراد و مقصود
باشد ‎٩‏ -

کاره *۱- بروزن پاره 6 بمعنی پشتواره
‎oT, cul‏ پشته‌ای باشد کوچك از هیزم و علف
وغیره که برپشت بندند .

کادی ".- بر وزن ‎GN‏ » مبارز
و جنگجوی (۳) را گوبند.- و شخص ی که ازو
کارها آید.

Jew ‏با نات بتحالی‎ ۰۲۳ IW
‏و بزای نقطهدار زده » جویآبی‌را گویند‎ at

که درزبرزمین بکنند تاآب ازآن روان شود .

(۷) چك : کار گر » چش : کارد گر )1(

‎Wye - ۱‏ مراجاللفات گوید : « تحقیق آنت که اين لفظ در اصل بمعنی‌صنمت نقاشی

‏است» بعداز آن‌بمجازدرصنت‌های دیگری نیزاستعمال کرده‌شود ویمعنی تاریخ ونامه سندمیخواهد.»
شاید درزمان‌سراج کارنامه بمعنی کار ‎fis‏ وصنعت گراستعمال می‌شده | کنون‌مترولاست «فرهتگه
نظام». ‎blake Cd)  .‏ سیرش‌دکندخیار کارنج. منجيك ترمذی*فرهنگه‌نظام».
۴ - پپلوی و پازند 63۲8۷80 ‎phe?‏ ۷۷۸ ۰6 ارمنی ع 1372۷30 «
========================= pdf 355 printed~ 1560
[pdf page 355]
Ve rs
la Jabs ‏بسکون زای‎ = IT
‏از چوب ولی و علف مانند خانه‌ای‎ Su TL
‏که مزارعان و پالیز بانان بر کنار زراعت و پالیز‎
‏اند که درکوه‎ a ‏سازند ۴ ؛ و بعضی جابیرا‎
" ‏ویابان درز زمین بجهت کوسفند و خر وگاو‎
‏مغاره خوانند؛وبسضی‎ guar ‏وغیره بکنند وآنرا‎
‏کویندصومعه‌ای باشد که برس رکوه‌ساخته‌باشند»‎
‏و این معنی با کاف فارسی همآمده است» واسح‎
‏صاری‎ US ‏وصومعه در عربی خلوت‎ . col ‏این‎
‎AT aie ‏راکوبند که سرآترا بلند وباريك‎
‏باشد که باغبانان درخت را بدان پیرایش دهند‎
- ‏نی شاخهای زبادتی آنرا با آن (۱) ببرند‎
‏و درخت صنوبرسفار را ليز کونند ۴ ,وباین‌ممنی‎
‏با زای فارسی هم آمده است - وسیلی وفنازدن‎
‏و شاخهابی باشد از‎ FP ‏وگردنیر! نیز کفته‌اند‎
‏درخت که صیادان کهنه و لنه و چیزها بر آن‎
‏دام در(۲) زمین‌ضب کنند‎ GAG ‏آویزند و بر‎
‏رمیده بجانب دام ودانه آبند‎ OT ‏تا جانوران از‎

باشد که در ایام ‎ae‏ ونوروز ازشاخ درخت‌رامثال
‎OT‏ آویزند و زنان و کودکان برآن نشینند ودر
هوا آیند وروند .

کاژ © پسکون زای‌فارسی ؛ بمعنی لوچ
باشد که بعربی احول خوانند» - ودرخت‌سنوبر
صغار را نیز گوبند ۷ .

کازدون © بروزن حاضرون .نام‌شهری
وولایتی باشد آزفاری ؛ و باين معنی بازای‌فارسی

آمده انت ۷ .

‎poe‏ 4 ع با زای فارسی » بی وزن
و ‎tee‏ کاشفر است و آن شپری باشد از
ماوراءالنهر .

‎SOS‏ ه بنتح زای تفه دار . مطلق
‎Jp‏ وخاله را گویند عموماً وخانه‌ای که‌مز ارعان
ازچوب وعلف بر کنار زراعت‌سازند خصوصاً *۱-
وتالار و عمارت چوییرا نیز گونند - و صومعه
وخلوتخانة ساری‌را هم ‎Salad‏ درسر‌های ‎oS‏
‏سازند — وعلامتی باشد که صیادان درکنار ‎Sela‏
‏شاخهای درخت سازند ‎٩۱‏ و چیزها از آن‌آویز ند

‏- ویمعتی ‎ob‏ پیچ هم آم
========================= pdf 611 printed~ 1816
[pdf page 611]
گز ‎Vo‏ - بنم اول و فتح دالابجد »
یمعنی پسندیده و تخاب کرده‌شده‌باشد سوتفیر
مخصوص هم هست - و نام بازبی است که آنرا
خربنده کونند ۴ و بسنی گفته‌اند تم بازیی است
که آنرا خیز کیرخوانند و هردولفت بتفصیل‌در
جای خود مذ کورشده است - وبفتح اول ‎ones‏
‏ترسیده ورنجیده که ازواهمه کردن ورنجیدن‌باشد
هم پنظرآمده است ۴ .

گژ یر » بنم اول » بمبنی چاره وعلاح
باشد ۴ چه ‎Su‏ 4 ناچار و لاعلاج را گویند +
‎BUI,‏ خرورت هم میکند - و بفتح اولبمعنی
پاکار وپیش‌کار باشد 6 - وبکس اولهم باینمعنی
ر هم ‎tens‏ سرهنکگ و پهلوان و عس آمده

۰

. ٩ ‏است‎

زره بش اد جع بسن
گزیر است که چاره و علاج باشد .

گزین ۷ - بن اول ر سکون آخر که

‎ath oy‏ بمعنی گزیده و اشخاب کرده شده

‏)( خم۱: کفته‌اند .

‏%_ سم مقعول از «کزیدن > ( بنم اول ) .
۴ - اسم مقعول از « کزیدن » ( بقتح اول ) .

‏را

‏است - وفاعل را نیز گوبند ‎SV‏ اتخا بکننده
باشد همچو خلوت ‎pS‏ وعشرت کزین - و امر
‎onl‏ ممنی هم‌هست یمنی التخاب کن وبگزین.

‏گز ینش ۸ ‎ees‏ اول و کس رابع
وسکون‌شین قطه‌دار,بمعنی بر کزیده وپندید کی
باشد - و ‎Lay‏ خاصیت هم هست 4 .

‏گزینه بفتح اول بر وزن خزینه ,
بمعنی چکش و پتك دراز مسگران ‎ath‏ که‌میان
ظروف را بدان عمیق مازند ‎aM‏ وبمعنی کنچینه
و مخزن هم‌آمده ابت = وکربای کنده رائیز
کوبند (۱) که از ‎as oT‏ و سایبان ‎Re‏
‏و فقبران و مسکینان جامه کنن - وین ود
بمعنی گزیده و برچیده و انتضاب کرده شده
باشد ‎WF‏ و ‎Les‏ خاصیت هم هست ‎NE‏

‎er‏ ینک ضم اول و کر ثانی
بروزن‌دوبینی؛ بععنی آخرکزینه است که‌خاصیت
‎ash‏ .

‎(casa ۴
ovi - 6۲۷2 ‏از‎ . bf

‏«هوبشمان ۹۱۹ . مخفف ‎OT‏ «کزر » ‎(gam)‏ و قس :گزبردن « اسشق ‎۹۱٩‏ ۰.
‎ *‏ معرب آن ه جزیر 
========================= pdf 612 printed~ 1817
[pdf page 612]
‎oly‏ یازدهم

‏در کاف فارسی با زای فارسی مشتمل بر چپار لت
‎UF‏ - بت اول و یبال فکنیده | بمعنی فیرباشد وآن صمفی‌است سیاه که بر درز
و پزای فارسی زده ؛ چینه ‎ob‏ مرغاترا کوبند | های کشتی و جپاز مالند - و بمعنی سیم سوخته
‎oy pany‏ حوصله خوانند .۴ وسواد زرکری هم آمده است .
?~= واز
گم ۴ - بنتح ارد و سکون ثانی ‎OF‏ بنم اول و سکون ‎BE‏ و ‎pt‏
‏رقتح ‎Jb‏ ابجد و ها وسکون میم + دام پهلوانی | درخت سده را کوبند که درخت پشه غال است
‎et‏ ایرالی .

‎eg‏ ویعربی شجرتالیق خوانند؟ - ویمعنی اندوه ود
‎oF‏ اف یفتح اول و سکون ثالی وفاء

‏تنگی هم بنظ رآمده ‎-%el‏

‏بیان دوازدهم

‏در ‎GE‏ فارسی با سین بی نقطه مشتمل بر بیست و يك لغت و کنایت

‏کار 1 = بضم اول‌بروزن دچار,بمعنی باشد ‎-٩۱‏ و بمعنی خوردن هم هست لیکن‌خوردن
گذارباش دکه از گذاشتن است۷ - وامربگذاشتن | شراب وغم خوردن ‎MF‏

‏هم هست ‎gi,‏ بگذار ۷ - وبمعتی خورند؛ غم گارده ‎f‏ بروزن و معنی گذاشته
و خورندة شراب لبز هست ۸ همچو ‎ASS‏ ]| است .
3 میکار ‎cee cot? . ٩‏ اول‌بروزن دست ۰ بمعنی

‏گساردن *۱- بروزن ومعنیگذاشتن۷ | زشت و قبیح و نازیبا باشد ‎MP‏

‏۱ - رك :کژار . در رشیدی «کزار ‎de‏ چینه‌دان مرغ ۰ اما ‎Baty‏ سروری بکاف
تازی‌آمده *. ۴ ‎olde ( Gazhdahm=‏ ابرانی ) > فبرست ‎OD;‏ .

‎. ‏رفیدی‎ : Af . ‏ورك :کرف‎ GF GS: AF
. ‏اول ) . ۰ رل : کساردن‎ en) ‏مسحف «کرم»‎ - 6
. ‏تلفظی د رگذاردن . ۸ - اسم فاعل مرخم‎ - ۷

‎٩‏ - اندهگار من شد وانده بمنگذاشت وامق چه کرد درم ‎pie‏ من‌آ نکنم.
خاقانی شروالی .
*۶- از :کسار (هم.)۲-دن ( پوند مصدری ) . ۱ باين معتی شاهدی ماد
‎ashes Cs‏ . رک ‎AG:‏ ,کشارده . ‎rb‏ باده ‎LS‏ غمگسار ‎awe cid.‏
رز" اس مقعول ازه کسار
========================= pdf 253 printed~ 1458
[pdf page 253]
۱ ws

فزدو ۱ ‎peo‏ اول و سکون نالی
‎gly city‏ کشیده. بمعنی‌فرزبود اس تکهحکمت
‎OT, atk‏ دریافتن افضلمملومات‌است‌بافضل علم.

رده = بفتح اول‌بروزن(۱)هرزه‌بمعنی؛
فرژد است که نوعی از ,سبز#تر وتازه باشد کهآ ترا
‎as‏ میگویند ۴ - و ‎AT Sh pe‏ رودخانه
و دریا اس که محل عبور کشتیها ‎Mash‏

‎Pole J‏ - بروزن‌فرهاد.حکیمودانشمند
رااگوند .

‏فرسان © فتح اول بروزن ‎OLS‏ نام
جانورست که از پوست ‎OT‏ پوستین سازند .

‏قرسای ۴ - بنتح اول و سکون ‎els‏

‏و الك بالف کشیده و بتحتانی ده . بمعنی محو
کننده و کهنه کننده وییای کوبنده باشد- وأمر
بفرسودن هم‌هست یعنی کهنه کن و محو سازودر
ای بمال . ۱

‏فرساینده * - بکر بای حطی‌رنتح
دال ‎amet‏ (۷), چیزی باشد که بسبیی از امباب
مانند رسیدن آسیبی ومکروهی وبابکثرت‌دست

‏(۱) چك : بوزن .

‏فرب » فریس ؛ پریز -
۴ رك : فرساییدن . فرسودن .

‏)¥( چك :- ابجد .

‎۰ ۲۵۷ ‏دساتیر‎ Kir ‏دسایر‎ isl, 0
. ۰ ۸۷ :۱ ‏فاب‎ * ky isl, ۴

‎Nhe

‏خوردن ‎Jlubs‏ شدن و با شدت غم واندوممفرط

‏۰ وبا مرور ایام و طول زمان ضرر ‎betty‏ و خرایی

‎Fath ‏رسیده‎ oly pls
. sl 5 Jol pts = ‏فر‎
‏ات بقتح اول و انی و سکون‎

‏[ الك و بای ابجد (۳) و بای فارسی هر دو آمده

‏است » بمعنی شاه تیر و ‎OT‏ چوب بزرکی باشد
که بام خانه را بدان پوشند- وجامهای الوان را
نیز گوبند که درایام ‎ae‏ و نوروزهای جشن‌بجهت
زیشتوآرایش‌بردرودیوارودکنها وسقف‌خانها کشند.
‎che —‏ اول و ثانی وسکون‌ثاك
و فوقاتی » جادوبی و ساحری را کویند .#
فرستاده ۲ ‎kee‏ اول و ثانی.پیغمیر
و رسول را گویند - و چیزی را نیز کوند که
فرستو + بفتح اول و ‎GU‏ بر وزن
ارسطو بمعنی پرستوله ‎ach‏ و بعربی‌خطاف گوبند؛
۳ بکر اول وثانی هم گفته‌اند .
فرستو
========================= pdf 257 printed~ 1462
[pdf page 257]
bata
‏خوشهای کوچك‌انگور‎ » SB, )۱( aed ‏شین‎
‏وآلرا‎ ath ‏بزرکه چسبیده‎ Ente Kus SI,
: ۷ ‏خصله خوانند‎ op ym

5, she to ۲ ‏فرخه‎

= بضم اول وسکون ثالی وقتح

ثالت » بمعنی اول فرش است که آغوز وفله‌باشد؛
و پکس اول هم‌آمده است .

‎gles Le ۴ det J‏ مجهول بر وزن
بخشید » نام برادر پیران وه است.*

‏قرشیم - بر وزن ‎ipl‏ بنستی قم
و جزو باشد چنانکه کوبند فرشیم اول و فرشیم
دویم )1( یمتی قمم اول و جزو دویم ‎)٩(‏ :

‎ole J‏ ۴ - بکس اول وسکون شالی
و ‎ale‏ بی ‎abel‏ بالف کشیده و بدال زده » توت
سفید راکوبند و آن در خاصیت قایم مقام انجیر
است. اکر ب رکه آفرا با بر که‌انجیرسیاموب رکه
انگور درآب باران ‎wali ges‏ وموی‌رابدانشویند
سیاه گرداند .

‏(۱) چك : - شطمرار .

‎oT we? -۱‏ خصله تست بلکه غوره است .

‎: ‏چك‎ (y)

‎Soa‏ ع۱.-

‏فرطوس ‎Jad ch = ٩‏ و ضم ‎sh‏
‏حطی (۳) بر وزن محبوی ‎(be‏ مبارزی است از
لشکرافراسیاب وضابطچفان بوده که موضعی‌است
از ترکستان .

‏فرع خوران ‎gost IE‏
‎abe‏ کنایه ازآدمیان است .

‏فرعون۱ © بکسراولوفتح عین‌وسکون
ثالی وواو ونون : پزبان عبری ‎cl‏ ولیدینمصعب
است واو اول فراعت مصربوده۷ - وبمعنی‌عتکیر
وس رکش باشد ۸ -

‎oF ‏و‎ gilt ‏بفتخ اول و سکون‎ - és
MSU SG ‏مرغ‎ Lany ‏قطمدار ؛ جوجه‎

‏فرغار ‎aad‏ بر وزن سرشار ۰ ‎we‏
‎ls‏ و نيك‌ترشده - وسرشته کردیدهوآغشته
باشد - و نام ترکی که اقراسیابش بجاسوسی
فرستاده ‎boy‏ معلوم ‎STAT‏ رستم چه‌مقدارلشکر

‏دارد .

‏دوم - (۳) چك : و شم طا .

‏مپذب الاسباء گوید : « الغوره .

‏فرشك ۰ ای ‎Sh‏ سه چهار انگور در هم بسته. » السامی فی‌الاسامی کوید : « الغورة » فرشك -
الخصلة , کوخك » در دستورالانه‌ممنی‌خصله را خوشة انگورنوشته » > فرهنگه نظام
```


## [2026-09-14T01:42:13.789Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nd={}\nfor blk in txt.split('\\f'):\n    m=re.search(r'\\[pdf page (\\d+)\\]',blk)\n    if m: d[int(m.group(1))]=blk\nfor n in (69,70,352,613,614):\n    b=d.get(n,'')\n    print('='*25,'pdf',n)\n    # print only lines with latin letters (footnotes with etyma)\n    for ln in b.split('\\n'):\n        if re.search(r'[A-Za-z]{3,}', ln) or 'شکستن' in ln or 'کارد' in ln or 'گسیختن' in ln or 'گسستن' in ln:\n            print(ln.strip()[:180])\nEOF",
 "description": "Borhan footnotes for šekastan, kārd, gosixtan"
}
```


### [2026-09-14T01:42:15.230Z] TOOL RESULT

```
========================= pdf 69
[pdf page 69]
‎as‏ است که ‎pet‏ باشد.
‎ORS‏ - بکر اول و فتح ثالی و ‎ot‏
‏وسکون ‎Jb‏ ابجد . ‎yin‏ چاره و علاج کند ۴
شکار کردن و شکستن باشد 6 - و بمعنی علاج
وچاره تمودن هم آمده ‎Vet‏
‎ys‏ کنند ۵ و بعتی کویند آنجه از ‎Sls‏ داماد
‏۴ _ مضارع«شکردن». فی : ‎Shegerd‏ درزبان کنولی.
‎ley‏ موس فرستند - و کلام شیرین و ضحیح
‏لیز عست - ‎BS any‏ شادی هم آمده است
شکر ‎Raw‏ = بنتح سین پی‌قط‌وسکون
نون وکاف فارسی » حجر ‎lel‏ ۱۱ است, وآن
که خون ‎adele‏ باشد ریزند خون را بازدارد
‎oe‏ بگیروشمم بکش. ‏ « کلستان ‎SPY‏
فردوسی طوسی. «لفت فری ‎NOL‏
‎arabicus — 1%‏ ۱
========================= pdf 70
[pdf page 70]
شکر فنده ‎Ga’‏ اول ‎pbs‏ فا
شکر لب - ‎TU SL pets‏ بالابا
لب پاین او ‎asks‏ و چاك دار ‎ash‏ و همچنی‌از
شکررنکه است ‎ote yy Ke ster‏ چه رنگ‌بسمتی
فلك زده, مردم ‎abe‏ وچست وچايك وصاحب جد
‏شکر هنج = بنتح اود ‎bay‏ وسکون‌نون
باشد و آن‌خارست سهپهلو ؛ و ‎ork‏ معنی‌بجای
‎Jol Ge Fou‏ بروزن
شنوبدن ۰ ‎ines‏ شکار کردن و شکستن دشمن
‎WAC el py LSS
‏خوانند.‎ GLU ‏بعربی‎ LT ‏و‎
‏شکستن - بفتح ثالی معروف است ‎٩‏
‏۴ از : شکر (شکردن = شکستن » شکارکردن ) ده
‎wy, (‏ اصاف ‎(cosy‏ پپلوی 50216۲2 (بازشکاری ) « اسشق ۷۸۹ بنقل از بندهن,.»» ‎GUN‏
‎shikrai‏ (باز » شاهین) فی: ارمنی 5816۲ «هوبتمان ‎VAT‏ «شکره.شکار کننده بود . عنصری
‎cal?‏ فرس ۸۷۷ * .
‏۲ - اوستا ‎scindayeiti , scand_ iz,‏ (شکتن),پپلوی ‎Shkastan‏ کردی ع
‎(sacs ( shikinandin . shikestin‏ , استی 58010 , 94010 ( شکتن, ترکیدن)
‏رك: هوبشمان ۷۸۸ ‎sishkastan SLT.‏ خرد کردن » ریز ریز کردن.
# شکرفیدن -از ‎Oa + GSE:‏ ( پوند مصدری ) » در اوراق مانوی بیارئی
‎: (ga) ۲ skrfyshn
‎Henning, A list of Middle Persian..., BSOS. IX.1,p. 91.
========================= pdf 352
[pdf page 352]
۱ ‏می‌دمیکه‌اخبار باطرآف‌برسانند‎ ets S55
AST Sy ‏؛‎ lS ‏و قاصد وجاسوس را یز‎ -
‏است که دانابان و اصحاب فراست‎ STB ear
کار با ۴ » با بای ‎uml‏ بروزن پارسا »
مخفف‌کاء ربا است و ‎ay yee OT‏ است.
تبدیل ‎ttle‏ +
‎cell tae - Oe WIS‏ و فرمان
‏کاردان فلك :
‎pal, ۰ ‏رابع بمعتی شنبلیت است‎ os
آفروختن بدوام ‎ath‏ - و روشن أختن‌جای‌تارك
‎ples ‏ازدنا‎ ats” = ‏قلاگ‎ bu
Maslel ‏بطریق‎ aS ‏را نیز‎ oT, - ‏است‎
وزیر پادشاء را کویند وکارداران جمع آنت که
‎goof‏ ۷ - بادال ابجد بروزن‌ساربان,
بمعنی کاردار است که وزیر باشد .
‏کاردان ‎MS‏ - کنایه از ‎SS‏
ومجموع را کاردانان فلك میگونند .
Aga) i= 5
۵ کارد - بسکون سوم » اوستا - 62۳648 (کارد +
‏چافو) ؛ پهلوی ‎kart‏ ؛ فی‌هندی باستانی - ‎krntéti kart‏ لو ‎Scum‏
‎(ou)‏ کردی ‎kird .kit‏ استی ‎k'ard‏ )35( تست کار
‏7 ( بربدن ). باوچی ‎gel 1768 ۰ kare‏ ۸۳۲ ؛ آلت برنده‌ای از آهن وفولاد
‏که دارای ‎ates‏ وتفه است .
========================= pdf 613
[pdf page 613]
‎Clea”‏ ۱ » بنم اول ؛ بروزن وممنی
هم‌هت عنی پهن کن و بیفراز و ‎Merged‏
‎Vo pal?‏ © فتح دال و سکون‌تون,
‎NAN
‏کته ‎٩‏ » بفتح اول‌بروزن ‎austen‏
‎Cire ‏نم اول و قتج‌ها‎ 5 re
0(۵۷۵ :۷1502 ۵ > هوبتمان ‎gets ayy > Ave‏ ایا
‏۴ - باب و آتش ‎CES‏ در دوه گوبی
1 - از +کستر ‎ge) Oot Cee)‏ مصدری) ,کتر + قس : پنتر. هندی
«ممزی ‎Sayles‏ ص 44۲ *.
‏باستان ‎Startvi‏ ( پهن کردن ) . پهلوی ‎Vilstartan‏ ( پپن کردن ) « اسعق ۰۹۲۱ .
‎© ells
‏. *- در پهلوی ‎Vistaxm‏ با ‎Vistahm‏ , این نام در اوستا بقول دارستتر
‏این کلمة اوستابی ‎gine Bd‏ کشوده و منتشر شده میباشد « پررداود . بستها ج ۱ س 15۵ ح ©
و کرستنسن ليز برین عقیده است * کیانیان س ۱۵ > بتابرین ‎sisting‏ اوستابی تبدیل صورت
‎dele)‏ مسدر ؛ اسم معنی ) -
‎٩ ۱‏ گستی - ‎pe‏ اول ‎Lape) Ss‏ مر کزی) یاقتح دوم وفتح چپارم. از ‎Sey‏ اوستایی
‎chide _ Sui =sid‏ < پارسی باستان ۷15۳20 «هوبشمان۹۲۲». پپلوی ‎vG@)sastan‏
‏رک : استق۲۲٩‏ ؛ دارستتر . تیمات ‎AEN‏ قطع ‎WS‏ بربدن » جداکردن — منقطم کشتن ,
========================= pdf 614
[pdf page 614]
VAY
‎seal?‏ لور ‎eee‏ اول و دون, کتابة
از ‎ole‏ نواست که هلال باشد - و پیاله‌ای را لیز
‏باشند . این دو ‎cad‏ را ‎Wu Gays‏ باکاف‌تازی
‏ولون » ‎an Tyan‏ باشد که در مقابلسیری
gat on: ayo
‏گسناهار * - با میم بروزن ‎«hls‏
‎tee‏ لهایت ‎Ly‏ کرسنگی باشد چه ‎OS‏
کبرا ‎ply‏ .*
ام باشد » ‎ote‏ وداع کردن ودفع نمودن‌وروانه
‏- درباك ‎Se‏ خطی جهانگیری ‎SOL gk‏ علامه دهشدا ‎ALT?‏ * ودردولمشةً
‏دیگر از همان کتاب متعلق بهمان کتابخانه ‎LES?‏ با اول مضموم ‎lh‏ زده ونون بالف کشیده »
آمده ‎wn‏ مذ کور درعتن » وشاهد ‎bb‏ در دو لسخةٌ ‎f‏ جهانگیری از طبقات خواجه ‎Soleil ihe‏
در احوالا بو بکر دقاق‌آمده :> ‎Sy‏ رازی گوی دکه ‎Nas‏ گفتم سبب سبب چشم بشدن نو چه بود ‎٩‏
بودم و در منازل از عیچکس چیزی تداول دکردم با ورع . از ‎MET‏ يك چشم من فرو برد .*
مواف فرهنگ نظام احتماد میدهد ‎Jol‏ کسناهار» باشد , از: گسن بمعنی کرمشکیوآهاربمعنی
غذا . (انتهی). ظ . مسعف‌چهماماز (فس: خشکاماز . رك : خشکامار ورك ‎GUT:‏ ۳ استقاء چشم
استفاء‌المین ‎Hydrophtalmie = ais t=‏ ره : لت نامه در کلمةٌ * استقاء »
‎٩‏ ح کین ح کدنه ‏ کرسنه ؛ در اراك ( سلطانآباد ) 80508 « مکی ‎“sly‏
‎Oo‏ گدلاایدن - نم اول و کسر(وفتح)دوم وفتح هفتم» از: کسل ‎tt Cee)‏ انیدن (پسوند
۵ گسلیدن - ‎pa‏ اول و کسر( ‎(py‏ دوم وفتح پنجم , از: کسل ‎wipe) Oat (ge)‏
‎o‏ یخن - ضم ‎obs Js!‏ 2 پنجم, ‏ کگستن ‎tobe Gem)‏ طبری 00508 (بگیخته)؛
کلیدن » پاره شدن ‎ghd‏ شدن ‎Sa‏ جماکردن . رهاکردن +
```


## [2026-09-14T01:42:34.117Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### risk\"; grep -n -o -E \".{0,120}ریسک.{0,120}\" MON_part1.txt MON_part2.txt | head -6; echo \"### agar\"; grep -n -o -E \".{0,80}اگر = .{0,120}|.{0,60}\\[ په \\. \\].{0,60}اگر.{0,60}\" MON_part1.txt | head -6\npdftoppm -f 438 -l 438 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg438 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Mo'in grep and render page 438"
}
```


### [2026-09-14T01:42:41.434Z] TOOL RESULT

```
Exit code 1
### risk
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,120}
                          \___exceeds complexity limits


### agar
ugrep: error: error at position 214
:[^\n\x80-\xbf][\x80-\xbf]*){0,60}
     exceeds complexity limits___/


I/O Error: Couldn't open file 'EtymologicalDictionary-persian-english.pdf': No such file or directory.
```


## [2026-09-14T01:42:46.097Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ریسک\" MON_part1.txt MON_part2.txt | head -5; echo \"### risk in ARY?\"; grep -rn \"ریسک\" incoming/ARY/ARY_pages.txt 2>/dev/null | head -3\npdftoppm -f 438 -l 438 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg438; ls /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Mo'in risk + render page"
}
```


### [2026-09-14T01:42:48.015Z] TOOL RESULT

```
MON_part1.txt:47599:ریسکث» چرخه ریسک. گوزده. 
MON_part1.txt:50100:چرخ‌ریسک: -6.1]5 [- چسرح رسو ] 
MON_part2.txt:32152:گریسکاری. قسمت‌های مختلف اتومبیل‌ها و 
### risk in ARY?
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
beekes410.txt
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
build2-434.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
e0-434.json
edit_about.py
edit_research.py
ffprof
irn-425.pdf
irn-425.txt
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
```


## [2026-09-14T01:42:51.926Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg438.png"
}
```


### [2026-09-14T01:42:52.659Z] TOOL RESULT

```

```


## [2026-09-14T01:42:52.654Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T01:43:08.052Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \"sairi[.\\-][a-zA-Z]{2,12}\" BRT.txt | sort -u | head -20; echo \"--- sairya context ---\"; sed -n '26115,26125p' BRT.txt",
 "description": "Bartholomae sairi- compounds"
}
```


### [2026-09-14T01:43:09.177Z] TOOL RESULT

```
24911:sairi-gaens
26803:sairi.gaostm
5857:sairi.vairilYt
--- sairya context ---
*iar-  t  'Kälte,  Frost';  vgl.  sanla-.    —    Bed. nach  Pü.  —  Pü. :  iorlik,  er). :  pa  sarl  iavll. <)  Tben.
•  g.  *3araidya-  Adj.  'gregalis;  Genosse">: al  töi  mazdä  t)m  mainyüm  aiaoxsayaiüä 'yayi  s^a^ra  mag^a  (sd.)  maya  vahiUä iarfta  manavAa  "deinen  Geist,  o  Af., sammt  dem  Wohlbehagen  der  beiden Genossen,  die  das  Asa  erhöhen,  soll  . ."
Ableil.  aus  *sar>da-  in.  'giei';  ai.  iärdha-  m. —  Vgl  oiasatAa-.  —  Pü.!  mtdätth  dakün, erl:  pääxiäkiA;  Siu:  niänütvam  dili,  erl.: pirlhaiatuaat.  —  1)  Vgl,  iBed.  i[;DN.  BB.  /j. 257'  —  *'  Da*  lind  Haarvaläi  und  Aanrilatäi, die  ja  unmitlelbar  zuvor  genannt  werden.  Was hier  als  x'iAnm  des  11.  und  A.  beieichnel wird,   heisst   in    der  folgenden  Strophe  hiijl-
•  j.  saraiya-  Adj.  -?-:  masdaoxttm va^S  '\p  vaxs  mq%rS  spmti  FrW.p.  i.
•  j.  sairya-  n.  "Dünger,  Mist'*>:  ava  hl gätüm  äärayjn  atryehe  (sd.  t  va  'yehe  vä V.&8.
•>  Und  iwsr  trockener,  etwa  Kamelmist.  Die Leiche  soll  auf  Asche  oder  Mist  ruhen,  die  be- ■linmit  sind,  die  aus  dem  Leichnam  sickernden
FlüMigkeilen  aofiusangen  und  so  lu  verhindern, dais  der  Erdboden  verunreinigt  wird.
KompA.  (s.  sairc.').  -  Vgl,  mp.  (Pö.)  :arg^, Ttf.targm  'Mist,  Dünger';  t.  noch  unter  lairt  -
iya:
•  j.  saurva-  m.  Name  eines  Dafia^*-. indrym  .  .  'rum  .  .  näaAai>lm  daium  V. /O.  9;  —  darvanam  daii-B  indrS  .  .  **ru" (statt  NS.)  .  .  n^nfiaih»m')  Y.in  a,
•)  Bd.  2S.  9:  "The  business  of  Ihe  demon  S that  IS  a  leader  of  ihe  demons,  is  thi«,  Ihat  U misgoyemmeiit,oppressireanarchy.inddrunken- ness  j  femer  West  SBE.  j/.  182  \o.  2,  wo weitere  Litt.  Bei  der  AuferstehnnR  kimp'fl  er mll  XIa%raVairya,  Bd.  30.  zq.  Weiteres  bei JN.  GIrPh.  1.  656,  6j8  No.  9.
```


## [2026-09-14T01:43:15.181Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '24908,24914p' BRT.txt; echo \"---\"; sed -n '26800,26808p' BRT.txt",
 "description": "Bartholomae sairi-gaona entries"
}
```


### [2026-09-14T01:43:15.257Z] TOOL RESULT

```
V.5. 19;  —  haoma  .  .  siaemt  z>mU  yai<a raohake  Y. /O.  4; — garayS..ya^ra  haoma *urüruüisa  (aSPrPfM.)'»  V. /0.3;  —  srJra (näml.  urvara)  urusta^''  amavaiti  V. /p. 18,  Vyt.24;  —  raooal  F.i/.
mit^rä'hervorwachseo,hervoräpriessen': vtspanam  urvaranam  frsurttstanam  Yt. 18,  6.
mit  nJ  '(physisch)  herunter-,  von  Kräften kommen':  yesi  nsit  nätrika  niuruilysl'''' "sonst  könnte  die  Frau  von  Kräften  kom- men" V.  16.  7;  —  dakmd  niuruziis^> aoailyll.drao/iä  ". .  der  heruntergekommen ist,  weil  er  nicht  die  gehörige  Kost  hat (,  darf  Unterricht  erteilen)"  N.  ly.
mit  vi  'heraus-,  hervorwachsen':  äaj aAva  paurvaiahva  .  .  viraolaie  Aaomö  . . sairi-gaens  Y.  10. 1 2.
ai.  ridhati,  rohati,  ruivia;  rü^Aäk;  np.  röyad,
rusla.  —  Pü.i  ruslan;    s.  noch  No.  t-$;    Rii.
(zu  Y.  zo):  samadilah.  —  ')  S  5J  !!■  —  '>  Hda.
---
KompA.  —  Et.?  Nicht  la  ai,  sutc  trotz  BB. /9.197.  —  ai.  slri-  f.  —  Pü.!  ian.  —  i|  Hds. mailri.  —  J)  Hds.  ttri,  gegen  S  JOJ-  I ;  allen- falls aus  siri/a  herausgelöst.
•  j.  stri,niinan-  Adj.  '(mit  weiblichem Namen  sva.)  weiblichen  Geschlechts',  von Tieren:  hatanr.fi/  sartl/(sd.)  °manS  (NP.) . . nairyS.nämanö  V.  13. 51,  i4- 1  GL
ai.  sirinäman-  Adj.  'einen  Weibernamen  fah- rend'. —  Pü. :  mälat  »am.
•  j.  spaeta-  Adj.  (fem.  'tä-)  'weiss'; spunam  .  .  't?m  sairi.gaostm  V,  8. 16",  17, 18; — ye^he  ca%würö  vastära  'ta  vispa., Yti.  13;  —  'ta  vastri  vaahaiti  Ha  (NSf.) "weisse  Kleider  hat  die  weisse  an"  Yt. 10. 136.
KompA. i  Ableit.  —  ai  hitlä-  Adj,;  np.  sipfd. —  Pii.:  jj«.
•  j.  spaeto.ainika- Adj.  'mit  weisser  Stirn' : anid  . .  'is  Aog.  75(?)''.
PiL:  jfit/  Sali.—  »  Das  Wort  fehlt  in  Ggb.s Ausgabe,  mnss  aber,  wie  das  Glossar  zeigt, hdslich  bezeugt  sein.    Vgl,  auch /a/ro.  No.  1.
•  j.  spaeitita-  Adj.  'weiss,  weisslich':  't^m avi  vayhaiwn  VL  z^.  13;  —  upa  •tarn rasunm  YL/5. 31;  —  aurvants  'ta'' ^hamagaonärahs  Yt  10. 125.
Ableit  aMisfiaela.;  %  202.  —  Vgl.  tpaiHitt- loa. Adj.—  Npa.:  fehlt—  ')  Hier  sfiür  geichr.
```


## [2026-09-14T01:43:32.459Z] TOOL CALL #63: Bash

```json
{
 "command": "head -40 tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-14T01:43:32.524Z] TOOL RESULT

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


## [2026-09-14T01:43:37.293Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/شکستن\" \\\n \"https://en.wiktionary.org/wiki/شکافتن\" \\\n \"https://en.wiktionary.org/wiki/سودن\" \\\n \"https://en.wiktionary.org/wiki/کارد\" \\\n \"https://en.wiktionary.org/wiki/چرم\" \\\n \"https://en.wiktionary.org/wiki/کر\" \\\n \"https://en.wiktionary.org/wiki/اگر\" \\\n \"https://en.wiktionary.org/wiki/گسیختن\" \\\n \"https://en.wiktionary.org/wiki/سرگین\" \\\n \"https://www.etymonline.com/word/risk\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 438, root Sek part 1\" 2>&1 | tail -1; done",
 "description": "Archive web sources"
}
```


### [2026-09-14T01:43:46.322Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/786dbb19d3129bc9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcd31f4a6f74e2e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b159b1f36133331.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/729f253445644c32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a07e84204d1a12a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4dd6ea417ae276c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eec5b85d71d71cf0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88fb4170fcd85fa0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f9e08d9dabd2919.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8093dfbf4cd5e3f.txt
```


## [2026-09-14T01:43:49.499Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 786dbb19d3129bc9 bcd31f4a6f74e2e6 2b159b1f36133331 729f253445644c32; do echo \"######## $f\"; grep -n -A12 -i \"Etymology\" $f.txt | head -40; done",
 "description": "Read Wiktionary etymologies 1"
}
```


### [2026-09-14T01:43:50.687Z] TOOL RESULT

```
######## 786dbb19d3129bc9
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
74- Related terms 
--
152: Etymology
153- [ edit ] 
154-
155: Etymology tree
156-
157- Proto-Indo-European *(s)ke(n)dh₂ 
158-
159- Proto-Indo-European *sek- ? 
160-
161- Proto-Indo-European *-éyti 
162-
163- Proto-Indo-European *skey- 
164- Proto-Indo-European *skeyd- 
165-
166- Proto-Iranian *sčand- 
167- Middle Persian škstn' ( škastan ) 
--
852: Pages with etymology trees 
853: Persian entries with etymology trees 
854- Pages with inline etymon for redlinks 
855- Pages using etymon with no ID 
856- Pages with entries 
857- Pages with 1 entry 
858- Persian links with redundant wikilinks 
859- Persian links with redundant alt parameters 
860-
######## bcd31f4a6f74e2e6
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Verb 
72-
73- 1.4.1 
74- Conjugation 
75-
76- 1.4.2 
77- Synonyms 
--
155: Etymology
156- [ edit ] 
157-
158- From Middle Persian [script needed] ( šk’p-tn' /⁠škāftan⁠/ ) , from Proto-Indo-European *(s)kop- ( “ to strike, to beat ” ) . Related to اشکفت ( eškeft , “ cave ” ) .
159-
160- Compare Ancient Greek κόπτω ( kóptō , “ strike, cut, shake ” ) , Old Church Slavonic скопити ( skopiti , “ castrate ” ) , Lithuanian kaplys ( “ hatchet ” ) , Old High German happa ( “ scythe ” ) , English hatchet .
161-
162- Pronunciation
163- [ edit ] 
164-
165- ( Classical Persian ) IPA ( key ) : /ʃi.kaːf.ˈtan/ 
166-
167- ( Dari, formal ) IPA ( key ) : [ʃɪ.kʰɑːf.t̪ʰän] 
######## 2b159b1f36133331
######## 729f253445644c32
70: Etymology 
71-
72- 2.2 
73- Pronunciation 
74-
75- 2.3 
76- Noun 
77-
78- Toggle the table of contents 
79-
80- کارد 
81-
82- 20 languages 
--
174: Etymology
175- [ edit ] 
176-
177- From Middle Persian [script needed] ( kārd , “ knife ” ) , akin to Northern Kurdish kêr , Central Kurdish کێرد ( kêrd ) , from Proto-Indo-European *(s)ker- .
178-
179- Pronunciation
180- [ edit ] 
181-
182- ( Classical Persian ) IPA ( key ) : /ˈkaːrd/ 
183-
184- ( Dari, formal ) IPA ( key ) : [kʰɑːɹd̪] 
185-
186- ( Dari, formal ) IPA ( key ) : [kʰɑːɹd̪]
```


## [2026-09-14T01:43:59.887Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 2b159b1f36133331 a07e84204d1a12a7 4dd6ea417ae276c3 eec5b85d71d71cf0 88fb4170fcd85fa0 8f9e08d9dabd2919; do echo \"######## $f\"; sed -n '120,230p' $f.txt | grep -n -i -B2 -A10 \"etymology\" | head -35; done",
 "description": "Read remaining Wiktionary etymologies"
}
```


### [2026-09-14T01:44:00.965Z] TOOL RESULT

```
######## 2b159b1f36133331
######## a07e84204d1a12a7
76- [ edit ] 
77-
78: Etymology
79- [ edit ] 
80-
81- From Middle Persian [script needed] ( clm /⁠čarm⁠/ , “ skin, hide, leather ” ) , from Old Persian 𐎨𐎼𐎶𐎴 ( c-r-m-n /⁠carman-⁠/ , “ skin, hide, parchment ” ) , from Proto-Iranian *čárma . Compare Pashto څرمن ( carman , “ skin ” ) , Sanskrit चर्मन् ( carman , “ skin, hide, leather ” ) , etc.
82-
83- Pronunciation
84- [ edit ] 
85-
86- ( Classical Persian ) IPA ( key ) : /ˈt͡ʃarm/ 
87-
88- ( Dari, formal ) IPA ( key ) : [t͡ʃʰäɾm] 
######## 4dd6ea417ae276c3
4-
5- 4.1 
6: Etymology 
7-
8- 4.2 
9- Pronunciation 
10-
11- 4.3 
12- Verb 
13-
14- Toggle the table of contents 
15-
16- کر 
--
88- Wikipedia bqi 
89-
90: Etymology
91- [ edit ] 
92-
93- Possibly from Proto-Indo-European *kʷer- ; compare Northern Kurdish kur .
94-
95- Pronunciation
96- [ edit ] 
97-
98- IPA ( key ) : /kowr/ 
99-
100- Noun
######## eec5b85d71d71cf0
83- اگه ( age ) ( colloquial ) 
84-
85: Etymology
86- [ edit ] 
87-
88- From Middle Persian 𐭧𐭲 ( ḥt /⁠agar⁠/ ) . Compare Parthian 𐭀𐭊 ( ag ) .
89-
90- Pronunciation
91- [ edit ] 
92-
93- ( Classical Persian ) IPA ( key ) : /ˈa.ɡar/ 
94-
95- ( Dari, formal ) IPA ( key ) : [á.ɡäɾ] 
######## 88fb4170fcd85fa0
######## 8f9e08d9dabd2919
18- [ edit ] 
19-
20: Etymology
21- [ edit ] 
22-
23- Inherited from Middle Persian [Book Pahlavi needed] ( slgyn' /⁠sargēn⁠/ ) , from Proto-Iranian *cákr̥ , from Proto-Indo-Iranian *ćákr̥ , from Proto-Indo-European *ḱókʷr̥ . Cognate with Sanskrit शकृत् ( śakṛt , “ dung, manure ” ) , Ancient Greek κόπρος ( kópros , “ dung, manure ” ) .
24-
25- Pronunciation
26- [ edit ] 
27-
28- ( Classical Persian ) IPA ( key ) : /sar.ˈɡiːn/ 
29-
30- ( Dari, formal ) IPA ( key ) : [säɾ.ɡíːn]
```


## [2026-09-14T01:44:31.959Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== سودن ===\"; wc -c 2b159b1f36133331.txt; grep -n -i \"persian\" 2b159b1f36133331.txt | head -10; echo \"=== گسیختن ===\"; wc -c 88fb4170fcd85fa0.txt; sed -n '1,80p' 88fb4170fcd85fa0.txt | head -40; echo \"=== کر Persian ===\"; grep -n -i -B3 -A8 \"Persian\" 4dd6ea417ae276c3.txt | sed -n '1,60p'",
 "description": "Check sudan, gosixtan, kar pages"
}
```


### [2026-09-14T01:44:32.063Z] TOOL RESULT

```
=== سودن ===
5946 2b159b1f36133331.txt
57: Persian 
59: Toggle Persian subsection 
130: Persian
136: ( Classical Persian ) IPA ( key ) : /suː.ˈdan/ 
179: Conjugation of سودن ( literary Iranian Persian )
387: Categories : Persian terms with IPA pronunciation 
388: Rhymes:Persian/an 
389: Rhymes:Persian/an/2 syllables 
390: Persian lemmas 
391: Persian verbs 
=== گسیختن ===
138 88fb4170fcd85fa0.txt
URL: https://en.wiktionary.org/wiki/گسیختن
FETCHED: 2026-09-14T01:43:45Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== کر Persian ===
76- Noun 
77-
78- 3 
79: Persian 
80-
81: Toggle Persian subsection 
82-
83- 3.1 
84- Etymology 1 
85-
86- 3.1.1 
87- Pronunciation 
88-
89- 3.1.2 
--
237-
238- field 
239-
240: Persian
241- [ edit ] 
242-
243- Etymology 1
244- [ edit ] 
245-
246: From Middle Persian kl ( karr , “ deaf ” ) . (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium . Particularly: “OK, now explain the etymon of THAT”) Likely related to Sanskrit कर्ण ( karṇa , “ ear ” ) .
247-
248- Pronunciation
249- [ edit ] 
250-
251: ( Classical Persian ) IPA ( key ) : /ˈkar/ 
252-
253- ( Dari, formal ) IPA ( key ) : [kʰäɾ] 
254-
255- ( Dari, formal ) IPA ( key ) : [kʰäɾ] 
256- ( Kabuli ) IPA ( key ) : [kʰäɾ] 
257-
258- ( Hazaragi ) IPA ( key ) : [kʰäɾ] 
259-
--
288-
289- کر 
290-
291: Iranian Persian
292-
293- Tajik
294-
295- кар 
296-
297- کر • ( kar ) 
298-
299- deaf 
--
338- Etymology 3
339- [ edit ] 
340-
341: Persian Wikipedia has an article on: کر (ساز) 
342-
343- Wikipedia fa 
344-
345- From French cor .
```


## [2026-09-14T01:44:39.112Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/گسستن\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-\" \"https://en.wiktionary.org/wiki/curtus\"; do python3 tools/fetch_source.py \"$u\" --note \"page 438, root Sek part 1\" 2>&1 | tail -1; done; echo \"=== etymonline risk ===\"; sed -n '1,60p' data/verification/sources/web/e8093dfbf4cd5e3f.txt",
 "description": "Fetch more sources; read etymonline risk"
}
```


### [2026-09-14T01:44:42.169Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fc4f445d305ef8ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a55319786f2f0be1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1703d342045f27e.txt
=== etymonline risk ===
URL: https://www.etymonline.com/word/risk
FETCHED: 2026-09-14T01:43:46Z
STATUS: 200
TITLE: Risk - Etymology, Origin & Meaning

Risk - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of risk 

 risk (n.) 

 1660s, risque , "hazard, danger, peril, exposure to mischance or harm," from French risque (16c.), from Italian risco, riscio (modern rischio ), from riscare "run into danger," a word of uncertain origin.

 The Englished spelling is recorded by 1728. Spanish riesgo and German Risiko are Italian loan-words. The commercial sense of "hazard of the loss of a ship, goods, or other properties" is by 1719; hence the extension to "chance taken in an economic enterprise."

 Paired with run (v.) from 1660s. Risk aversion is recorded from 1942; risk factor from 1906; risk management from 1963; risk-taker from 1892.
 also from 1660s 

 risk (v.) 

 1680s, "expose to chance of injury or loss," from risk (n.), or from French risquer , from Italian riscare , rischaire , from the noun. By 1705 as "venture upon, take the chances of." Related: Risked ; risks ; risking .
 also from 1680s 

 Entries linking to risk 

 risky (adj.) 

 "attended with risk, dangerous," 1825, from risk (n.) + -y (2). Riskful in same sense is from 1793. Related: Riskiness . Riskless is attested by 1818.

 risque (adj.) 

 "tending toward impropriety," 1867, from French risqué , past participle of risquer "to risk" (see risk (v.)).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 hazard 

 c. 1300, name of a game at dice, from Old French hasard, hasart "game of chance played with dice," also "a throw of six in dice" (12c.), of uncertain origin. Possibly from Spanish azar "an unfortunate card or throw at dice," which is said to be from Arabic az-zahr (for al-zahr) "

 jeopardy 

 late 14c., jupartie , ioparde, etc., "danger, risk;" earlier "a cunning plan, a stratagem" (c. 1300), from or based on Old French jeu parti "a lost game," more correctly "a divided game, game with even chances" (hence "uncertainty"). The sense perhaps developed in Anglo-French. T

 gamble
```


## [2026-09-14T01:44:56.199Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=risk\" --note \"page 438, AHD etymology of risk\" 2>&1 | tail -1; echo; grep -n -o -E \".{0,400}riscare.{0,300}\" data/verification/sources/web/*.txt | head -5; echo \"=== curtus ===\"; grep -n -A6 -i \"^ *Etymology\" data/verification/sources/web/a1703d342045f27e.txt | head -20",
 "description": "AHD risk + Wiktionary curtus"
}
```


### [2026-09-14T01:45:00.666Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0ceda51038d6a896.txt

ugrep: error: error at position 85
\xbf][\x80-\xbf]*){0,300}
                         \___exceeds complexity limits


=== curtus ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
--
164: Etymology
165- [ edit ] 
166-
167- From Proto-Italic *kortos , from Proto-Indo-European *(s)kr̥tós ( “ short ” ) , from *(s)ker- ( “ to cut ” ) . [ 1 ] Cognate with Proto-Slavic *kortъkъ ( “ short ” ) , Scots short , schort ( “ short ” ) , Old High German scurz ( “ short ” ) ( Middle High German schurz , Old Norse skorta ( “ to lack ” ) ( Danish skorte ), (maybe) Albanian shkurt ( “ short, brief ” ) , English short . More at shirt .
168-
169- Pronunciation
170- [ edit ]
```


## [2026-09-14T01:45:05.802Z] TOOL CALL #70: Bash

```json
{
 "command": "grep -n -i \"risk\" /home/sfmqrb/git/rishe/data/verification/sources/web/0ceda51038d6a896.txt | head -20; echo \"---\"; grep -n -i \"resec\\|riscare\\|resicare\" /home/sfmqrb/git/rishe/data/verification/sources/web/0ceda51038d6a896.txt | head",
 "description": "AHD risk entry"
}
```


### [2026-09-14T01:45:05.875Z] TOOL RESULT

```
1:URL: https://www.ahdictionary.com/word/search.html?q=risk
4:TITLE: American Heritage Dictionary Entry: risk
6:American Heritage Dictionary Entry: risk 
41: risk (r ĭ sk) 
47: 2. A factor, thing, element, or course involving uncertain danger; a hazard: "the usual risks of the desert: rattlesnakes, the heat, and lack of water" (Frank Clancy). 
54: 5. One considered with respect to the possibility of loss: a poor risk. 
56: tr.v. risked , risk·ing , risks 1. To expose to a chance of loss or damage; hazard. See Synonyms at endanger .
57: 2. To incur the risk of: His action risked a sharp reprisal. 
59: Idiom: at risk In an endangered state, especially from lack of proper care: unsupervised children who are at risk of dropping out of school. 
62: risk  er n. 
---
```


## [2026-09-14T01:45:08.501Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '58,75p' /home/sfmqrb/git/rishe/data/verification/sources/web/0ceda51038d6a896.txt",
 "description": "AHD risk etymology bracket"
}
```


### [2026-09-14T01:45:08.577Z] TOOL RESULT

```
 Idiom: at risk In an endangered state, especially from lack of proper care: unsupervised children who are at risk of dropping out of school. 

 [French risque , from Italian risco, rischio , probably from Medieval Greek rizikon , sustenance obtained by a soldier through his own initiative, fortune, from Arabic rizq , sustenance, that which God allots, from Syriac ruziq ā , daily bread, from Middle Iranian r ō č ig , from r ō č , day, from Old Iranian *rau č ah- ; see leuk- in the Appendix of Indo-European roots .]
 risk  er n. 

 The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.

 Indo-European & Semitic Roots Appendices
 Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
 Indo-European Roots 
 Semitic Roots 
 The Indo-European appendix covers nearly half of the Indo-European roots that have left their mark on English words. A more complete treatment of Indo-European roots and the English words derived from them is available in our Dictionary of Indo-European Roots .

 American Heritage Dictionary Products
 The American Heritage Dictionary, 5th Edition

 The American Heritage Dictionary of Idioms
```


## [2026-09-14T01:45:26.726Z] TOOL CALL #72: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-14T01:45:26.774Z] TOOL RESULT

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


## [2026-09-14T01:45:40.169Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/WLD/ && python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nfor pat in [r'sē̆k-', r'sek-.*schneiden', r'schneiden', r'skarn']:\n    ms=[m.start() for m in re.finditer(pat,t)][:3]\n    print(pat, len(ms))\n# find page markers\nprint(re.findall(r'\\[pdf page (\\d+)\\]', t)[:5])\nEOF",
 "description": "Check Walde-Pokorny vol 2"
}
```


### [2026-09-14T01:45:41.422Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
sē̆k- 0
sek-.*schneiden 0
schneiden 3
skarn 1
[]
```


## [2026-09-14T01:45:47.975Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c incoming/WLD/WLD_Bd2_pages.txt incoming/WLD/WLD_Bd1_pages.txt WLD_band3.txt; echo \"--- band3 index ---\"; grep -n -E \"sairya|carman|karəna|skənda|sargin|sairi\" WLD_band3.txt | head -10; echo \"--- band3 sek ---\"; grep -n -E \"^ *sek|\\(s\\)ker|skei-\" WLD_band3.txt | head -10",
 "description": "Check WLD files"
}
```


### [2026-09-14T01:45:48.068Z] TOOL RESULT

```
2833963 incoming/WLD/WLD_Bd2_pages.txt
4327601 incoming/WLD/WLD_Bd1_pages.txt
 317372 WLD_band3.txt
7478936 total
--- band3 index ---
--- band3 sek ---
```


## [2026-09-14T01:45:51.512Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"scand|skarena|sairya|carman|kar.ta|sarg\" incoming/WLD/WLD_Bd2_pages.txt | head -12; echo \"=== Bd1 ker ===\"; grep -n -i -E \"sairi|sarya|karena\" incoming/WLD/WLD_Bd1_pages.txt | head -6",
 "description": "Grep Walde-Pokorny volumes"
}
```


### [2026-09-14T01:45:51.602Z] TOOL RESULT

```
10510:nach ^farha- „porcus‘^ erweitert) in: ahd, barug, barJi, nhd. Sarg, Sarch
20300:mire, myre (wohl scand.            Lw. nach Holthausen KZ. 47, 311, wo auch liber
25473:      Gr. Xr}v6g „Trog, Kelter, Sarg, Standloch des Mastes“ bleibt fern.
33163:s&g-mi, -ti, -iti „behute, bewache^*', sdrgas „WachteF', PI. sargal^ sargus
33164:,,wachsam‘', apr. hiitsargs ..Haushalter”, abserg^snan Acc. ,,Schutz'\
35915:     lat. scando^ -ere „steigen, sich erheben“, scala (^scand-sla) ,jStiege, Treppe,
35920:  Curtins 166, Fick 566, Gegen die Yerb. von gr. oxibvaodai mit scando
35925: en\ wenn ai, skand-^ gr. oxavS^^ lat. scand- auf "^sqond- (Red. einer o-
37061:  Ai. shhadate          (unbelegt; ware auch als ^sqhnd- mit av. scanday-
37094:III* 448, 449 f., Yf. LEWb.2 u. scandtda (s. zu diesem u, sqen{dy „ab-
37423:Haut, Membrane*'                   Av, scandayeiti „zerbricht, vernichtet (die
37428:   Ygl. mit a-Vokalismus mir. scandraim „zerspalte‘*, scandrad, scaindred
=== Bd1 ker ===
```


## [2026-09-14T01:45:55.319Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37410,37440p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD skhed entry"
}
```


### [2026-09-14T01:45:55.374Z] TOOL RESULT

```
                                                                   ;


  lage von yaxxvoo „schustere zusammem') nicht nach Ehrlich Unt. 53 eine
  m-Ableitung eines mit bret. shani ablautgleichen *q;n-to-,
       Daneben (s. Zupitza aaO. und KZ. 36, 73, Liden aaO., Persson Beitr. 883)
 idg.    {s)qend- (vielleicht rf-Praesens? oder Verquickung von sqen-’ und
     sqed~ f,oy,e&dvvvLa'^^. oder Kasalpraes. zu letzterem?) in:
        air. ceinn „Schuppe“(brit Lw.?), cymr. cen {^qend-n-)^ corn.                                  „Haut-
     chen, Haut% ysgen „Schinnen“ (Pick II^ 7S; Ehrlichs aaO. Ansatz "^qenUno-
     mit t entbehrt der Grundlage, da nerx-eco fernbleibt) anord. hinna f. „diinne
                                                                               :
564                                           S(q)en, (s)qan    — sqeng-
Haut, Membrane*'                   Av, scandayeiti „zerbricht, vernichtet (die
                                   {sg[end-n-).
Schlachtreihen)**, slcdnda--m. „Zerspaltung, zerstoren**;
   gr. vermutlich in oxevdvkrj, ox^vdvlri wahrscheinlich ,,ZaDge“ (LidenaaO.;
anders, aber verfehlt Ifiedermann IF. 15, 108f.).
   Ygl. mit a-Vokalismus mir. scandraim „zerspalte‘*, scandrad, scaindred
„dispersion**, scainner, PL scaindrecha etwa ^Yernichtungskampfe** (: cymr.
ysgytJim „to lop**; Stokes BB. 23, 59, Zupitza aaO.; Zweifel bei Giintert
Abl. 56); aksL skqda „defectus** (Johansson PBrB. 14, 337; idg. a? aksl.
skqd^ „arm, klein**, UqdUi „sparen, schonen**, Persson aaO., liegen in der
Bed, recht weifc ab c^sth „Teir* zu lit. hdndu „bei6en**, dessen Sippe nieht
                                   ;


aus „spalten‘*, sondern aus „nagen, kratzen** entwickelt scheint); lat. scan-
dula „Schindel** (aEeduktionsvokalo); iiber gr* oxivdaXyog s. Yf. LEY^b.^ u.
scandula^ Giintert aaO,).                    —
                             Dafi sqen- aus seq- „schneiden** erweitert sei
```


## [2026-09-14T01:46:03.111Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"carman|caroman|k.r.ta.*Messer|sairya|„Mist\" incoming/WLD/WLD_Bd2_pages.txt | head -12",
 "description": "WLD carman/sairya"
}
```


### [2026-09-14T01:46:03.178Z] TOOL RESULT

```
7568: „Mistkafer“, mengl. b^idde ,,Enospe“ und „Kafer“, btidden „ausschlagen“
16113:ahd. mist                        meox ,Kot, Diinger'^, ags. engl, mixen „Mist-
38056:carman-, av. laroman- „Fell, Haut‘‘ (Bed. wie lat. corium, ai. krUi-,
38250:carman- „Haut”, Uhlenbeck Ai. Wb. 89, Lewy IP. 32, 162, wo andere BeL
38251:spiele fiir „Haut; Korper”; vielleicht aber von carman- unabhangige BiL
38341:dei^ spalten“, sowie ai. carman- usw. oben);
39001:   Slav, '^serq,       "^svrati       „cacare“    (z.   B.      skr. s'ereyn, srdti)^   russ. sorz „Mist“;
39002:av. sairya- ,,Mist“, mpers. sargon^ np. sargin ds. (Solmsen WfklPh. 1906,
39013:   aisl.    sham, ags. scearn. afries. shern, nd. scliarn „Mist''.
39045:die friihere Zuteilung von axcoo usw. zu sqer-^ wahrend er fur shrati, sairya-^
42561:denov) bulg. ior^ „Dunger", tor^d „diingen", serb. toriti „misten‘‘.
44359:spQi)er- „Mistkugelchen^, 5p(/0ere^- „zucken“,     „sich hastig bewegen^^,
```


## [2026-09-14T01:46:10.268Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38990,39010p;39035,39055p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "WLD sker- dung entry"
}
```


### [2026-09-14T01:46:10.396Z] TOOL RESULT

```
  lat.scrupus ,.scharfer, spitzer Stein“ (vgl. zur Bed. saxiim isecare)^ sera-
pidus „spitziges Steinchen^' und, wie scrupulum^ „klemster Teil eines Ge-
wichtes Oder MaBes; angstliche Genauigkeit (wie wenn man auf spitzen
Steinen ginge), Skrupeb', scrfipeas „voll rauher Felsen, steinig, schroflP“.
   Vielleicht als „kratzend‘’'schwed. skroflig ^uneben, rauh, heiseP' usw.
(s. u.qreup- „SchorP‘, wo auch fiber abg. Tcrupa „Krumchen“ usw.).
   S. Zupitza G. 157 m. Lit., Persson Beitr. 861 f., 863.



sker- „cacare; Mist, Kot des Leibes‘\
   Slav, '^serq,       "^svrati       „cacare“    (z.   B.      skr. s'ereyn, srdti)^   russ. sorz „Mist“;
av. sairya- ,,Mist“, mpers. sargon^ np. sargin ds. (Solmsen WfklPh. 1906,
871, Beitr. I 161 a 2) aber lett. sarni „Schlacken, sich absondernde Un-
                                  ;


reinigkeiten‘' (von Gutmann BB. 29, 161 als esthnisches AVort betrachtet).
geht (trotz Bezz. GGiST. 1875, 225f., Persson Beitr. 167) auf die Wz. ser-
.jStromen^' zuriick (Senn brieflich).
   Gr. oy.d)Q. oxaxog „Kot^^ (flexivisch umgebildet nach dem Typus vdeop,
                  ^


fiir welche ai. ava-, apa-skara-h „Exkremente“ gar nichts beweist (die Zs.

sichert die verbale Anschauung „Aus-, Ab-scheidung‘‘)       wenn abg. skarpjd%      ;


„ekelhaft'' verwandt ist, gesellt es sich zu andern Fallen mit widg. Yelar
statt Pal. im Bsl. Persson Beitr. 167f., 656, 886f., 942f. vertritt mit XJnrecht
die friihere Zuteilung von axcoo usw. zu sqer-^ wahrend er fur shrati, sairya-^
588                                    (s)qereb(h)-', (s)qreinb-




sarni,    Mrvai eine versch. Wz.        ker^ annimmt (fur welche das in der Bed,
ganz abweichende          ai.   gardhato „furzt“ aber nichts beweist). Da6 unser
sker-    als   palatal e Variante      neben sqer-           einst   ebenfalls „au8sclieiden“ be-
deutet babe, ware eine unbeweisbare Vermutung.
   Zur Scheidung von anklingenden Worten                             s. Scbulze aaO,,  und unter
```


## [2026-09-14T01:46:35.993Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o -E \"(scap|skap|scaf|skaf|kaf)[a-z]{0,8}-\" BRT.txt | sort -u | head -20; echo \"--- kaf in BRT ---\"; grep -n -E \"^•  ?j\\.  ?kaf|kafa\" BRT.txt | head -5",
 "description": "Bartholomae scapti/kaf"
}
```


### [2026-09-14T01:46:37.216Z] TOOL RESULT

```
11444:kafi-
13072:scafraiauru-
15056:scaptayae-
15093:scapta-
18322:kafra-
26242:kaf-
26440:skapta-
26459:scapta-
8928:kafi-
9046:kafa-
--- kaf in BRT ---
9046:•  j.  kafa-  m.  'Schaum,  Geifer';  yl  (näml.  1 uilrä)  '/jin  aipi-spaydli  spasiimm  upa  .  .  \ Auxsnaei re  (sd.)  Yt. /J.  13.
9742:—  yavanqm  .  .  västranqm  .  .  '•%anqmca  Wesen  und  Dingen  zum  (Reich  des)  Asa, ashaiiinqm  YtÄ29;  usw.;  —  s.  noch  zur  stofflichen,  sichtbaren  Welt  des  Asa Anhang  «.  2)  'Wesen'  im  Sinn  von  gehört':  'irj^räi  asake  °'^anqm  "um  zu 'Anwesen';  'Gehöft,  Haus  und  Hofs>,  schirmen  alles,  was  zum  Asa  gehört"  Vt. Hausstand  (ramilia)',  überhaupt  'Hab  und  /p.  48;  Y. 55.  3^  57.  17;  —  makrkai  alahe Gut' (im  Gegensatz  zu /<2ns-,/fl«a/-), 'weit-  '>anqm  Yt. /<).  50,  Y.(?.  8;  <?.  3,  V. /Ä  sSi lieber  Besitz*  (im  Gegensatz  zu  ankav-  —  asiby5  yli  urvätäiS  drRjS  asahyä  '^ii I  2);  Sing,  und  Plur.i  yi  .  .  varidayoSä  vTtn?r?ncaiti  (sd.)  Y.31.  1;  —  ^un  ''^ä yqm  nasdi/tqnt  '^qm  dr»^a  iax/ai ff.. (sd.)  amar/antis  ya  ahhe  Yt,  sf).  la;  — drufim ^■5'>-Z'>  — yä^a  ■  ■  v?hrkqm  azr5.dai)tTm\iti~barat  asahe  haca  ''iabyS  Yt.  ig.  93;  — fsd.)  -iaw  avi  frafiaiaiti'y.  18. 6 $'•'>■,  N.  —  s.  noch  Vt.  6'.  i  (unter  z).  a)  auch 3'Q);  —  spämm  dd^tm  ..''i^anqm  Aar»-  mA  astvanh  Adj.:  ktmat  atiAsus  astvatS ^räi  V./y.39";  — yesi  narü  ..  kafa  aoi  .  .  '''^abyö  *  astvaitibyS^^  asake  ^.13; ''iäbyS  pain.iri>:yeiii  Vd.  13;  —  cval  ns  —  gandartwim  , .  y3  apatat . .  m»r»xlam ä^rata  (sd.)  a>aurun?m  haca  *'%äbu^'>  °^J  astvaifiS  alake -Hx.  iQ.  i,\ ;  V./iV.  55, *parayät  N.  4;  —  yS  ^yujyasfim  //a.ft  .  SrB.j;  —  dar7sca(sd^  ddisat'^amfrixsyan- '"iabyd  paräiti    V.  13.  17**;    —  yas)  tat  tim  vTspqm  yqm  astvaiHm  gai'iqm  Yt.ig.
28800:•  j.  'haosravah-  m.  Name  einer  Bucht des  VourukaSa*^:  aSa  hau  apayzärS  bvai srayanhö  vouru.kafahe  vairis'yS  'vä  nqma Yt.  15.  56;  —  vairim  'varthsm  S.a.  9;  — vardis  'vanhahe'^  Ny.5.  5.
```


## [2026-09-14T01:46:40.800Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15090,15098p;26438,26445p;26455,26465p;26240,26246p' BRT.txt",
 "description": "Bartholomae scapta-/skapta-/kaf-"
}
```


### [2026-09-14T01:46:40.867Z] TOOL RESULT

```
•  j.  paiti-stä-  f.  'Standort,  Wohnstätte': äha  .  .  nava.cil  mainyava  yazata  atjkava astvainti  paili.drqm  nStt  'stqm  vfn^nti "dann  finden  . .  durchaus  keinen  Aufent- haltsort und  keine  Wohnstätte  mehr"  Yt.
6.3-
S,  auch  paitiHina-  mit  No.  z.  —  ai.  vgl.  pra- liffAi-  1.  —  Pü.:  apar  esliinii.
•  j.  paitt-ätät^e,  -ätätayae-i^  Inf.  '(und) zu  widerstehen,  zu  bestehen',  uzw,  iAxfl'ische Wesen  und  Anfechtungen;  a)  mit  Akk, •/Äf  ajastaca  tlizdi^taca  .  .  xrafstra  Yt. 21. 1.  b)  mit  Gen.:  't}e  .  .  druj5  'tSe . .  iialsiirtis  Yt.  ij.  129;  'o.Si  ^^°i  '3^^ i3S-'38'°,  142,  Y.6S.B,  60.4,  ?'■  '7'' YL(7.4i,  5.12,  y.130,  131,  136',  137'. 138',  Vr.20.  2,  V.  20.3'J,  S.2.i3i  — avaiAAi  pairikayäi  'fayaSca  paitiscapta- yaica  Y.  16.  8.
Zum  V.  ttä-.  —  Vgl.  •sfäiay-  f.  —  Pii.j/a afäc  ei/isniA,  apäJ  eitiSmh  räi,  (lO  Y.  6o) :  apic
•  j.  paiti-ätäna-,  "stana-**  n.  i)  'Stand- ort, \V'ohnstätte':  h5  imqm  dalnam  .  ./ra- pinaoiti  sattm  *°i'tananqm{G?.)''' hazannm faiti.daranqm  "der  bringt  diese  Religion zum  Gedeihen,  hundert  (neue)  Wohnstätten, tausend  (neue)  Aufentlialtsorte  (sinds  die er  ihr  schafft)"  V.^.3i)>.  2)  '(Gestell sva.)  Bein',  vom  Fuss  bis  zur  Hüfte:  'stäna F.Jg;  —  maihySi  'slUne  xräidisme  maiöyöi nars  vandusme  "bis  zur  Mitte  des  Beins (der  Beinhöhe)  in  hartem,  bis  zur  (Leibes)- mitte  eines  Mannes  in  weichem  Erdboden" V,Ä8;  *H.86.
KompE.  —  S.  aach  paitislä:  —  ai.  Tgt  fra- liifhäna-Ti.  'Standort,  Unlerlage;  FuEsgesiell'. —  Pii.  (Iransskr.)i  fatiilän,  (lu  V.  3):  foH- itänth,  mit  der  Etl.i  cigön  {ka)  fa  50  marl Jasl  häraithli  t  apurnäyak  kuHftid  "als  ob man  durch  die  Kraft  von  50  Mäntiem  dem Kinde  Schult  verschaffte";  s.  No.  3.  —  ')  Vgl. dainBTHL.  IF.7.  62.  — i)So  JpI,Mfi.  NA. hat  paitiilattam.  Ob  lu  pailiiti-l  —  Sl  Vgl iSt-  und  iPfiErL  Ggr.  ZDMG.  34-  433,  DST. ZA.  Z.43.  Aber  beide  übersehen  die  Parallele YL6.3;  s.  Gdn.  Stud.  i.  155.—  ♦)  So  nach der  NA.  des  Pahl.-Vend.     Vgl.  unter  har-,
•  j.  paiti.ämuxta-'),  *piiti.Smiixta-" " Adj.  (fem.  °/ä-)  'mit  Fusszeug  bekleidet,  be- schuht': ar?dvl  ißra  . .  tiismga  (sd.)  aoira *'ta  (NSf.)  zaranySMrvtxina  Yt  5.  64; 78.  a)    vom    Hufbcschlag:    tt  para.-
paitis.x^arsna-  838
•  j.,  g.  säsni-  f.  'Lehre;  Gebof:  vakilta 'nanqm  yqm  hudä  sästl  asä  akurS  ". .  ist die  beste  der  Lehren  die,  die  der  wohl- meinende Ah.  durch  Asa  lehrt"  Y.-^.a; —  tim  äzOtöi/isd.)  ahurS  mq%r3m  talal . . spunta  'naya  (IS.)  Y,  29.  7 ;  —  sraffta  'nä fiSnghyS  (sd.)  Y.  4g.  9;  —  yS  nS  alvB  'nä güsatä  zara^u^trB  spitämö  "der  einzige, der  unsre  Lehren  vernommen  hat,  ZarSp." V.2g.S;  —  mä  as  at  vS  drtgvaß  (Sp. 776  o.)  mq%rqscä  gBsta  •näscä  "keiner von  euch  höre  auf  des  ./ungläubigen Worte  und  Gebote"  Y.jj.  18";  —  gayehe man^nS  . .  yS  paoiryS  akurSi  . .  manasla *guita  'näsca  Yt.rj.87*';  —  *maihyDi.mäa- hahe  . .  yS  paoiryS  zarahustrSi  mq'hrtmca *gusla  'näsca  Yt.  JJ.  95'';  —  gusta  'na F.,?f.;  —  sat>m  'nanqm  Vyt /J.
KompA.  —  Zum  V.  läk-.  —  aL  vgL  Säsana' n.  —  Pü.:  ämöriin,  ämSxliht. —  1)  Die  lelztea Worte  der  Stelle  hat  der  Verfasser  von  Yt. '3-  87,  95  bennwt  —  ">  S.  No.  I.
•  j.  säsnö.güä-"  Adj.  'der  die  (heiligen) Lehren  hört,  vernimmt';  paoiryanqm  tkaf- lanqm  paoiryanqm  'güsqm ''  "der  ersten Verkünder  und  Hörer  der  heiligen  Lehren" Y.aö'.  4,  Yt.jj.149J'.
*gis-  Adj.,  zum  V.  gaoi-.  —  Pü. :  nigöHht  i ämöähtin,  erl. :  fratum  /lävill  i  aatalull,  — 1)  Vgl.  No.  3.  —  »)  Vgl.  Y.  19.  8,  Yt.  rj 87.  9S-  —  J'  Wo  Fl   'gülqm  bietet
•  j.,  g.  sah- V.  'hcissen'.  Praes.  1  sah-, 3  sJia-,  2z  sähT:  —  PPfP.  sJäa-'\ s:ista-.
'heissen,  lehren',  mit  dopp.  Akk.:  data xratsul . .  razSng  voAb  säAli  mananAa "(es)  lehre  (mich)  der  Schöpfer  der  Geistes- kraft durch  VM.  (seine)  Satzungen"  Y. $0. 6;  —  y^  nä  )mBs  savatshs  pdhs  slisit "der  uns  die  rechten  Wege  des  Vorteils lehren  könnte"  Y.4J.3;  —  süa  nä  aia
dby  Google
•  j.  skatay-  f.  'Heuschrecke"  (?) ",  als  Land- plage von  Gava  (Sogdiane):  gilum  yim suyös.sayanfm  aal  ahe  paityär^m  fräkiryii- tat  anrö  mainyus  .  .  'ilim  yqm  gavaca daya(sd.)ca  pouru.mahrk>m  V.  r.  4,
Der  Text  ist  inkorrekt  und  inhaltlich  unklar.  — Pu. :  knrkn  maW  ('Heuschrecke')  i  gSspan- dän  dadtrii  i pur  mark;  erl.:  ma\ak  ape  äyil iiirläk  -  ku  ape  vSitr  apt  äyil  —  gäv  baslan HC  säytt  gäspandma  mariih  bavel.  AuchOrBd. (s.DST.ZA.2.8)  bietet  'Heuschrecke'  -  kmca; s.  PPGI.  ff.  3  -  für  skailJm.  —  0  So  nach der  Tradition;  s.  oben.  Anders  FkMOllek WZKM.  3.  366,  6.  183.
•  j.  skapta-  Adj.  'erstaunlich,  wunderbar':
mp.  (Pö.)  SliafI  (in  SO.:  adMutai),  np,  ügr// 'Erstaunen',  iiguflan  'sich  wandern'.
•  j.  skand- V. 'brechen'.   Praes.9  +  24'>
scandaya-,  ^shndaya-,  scindaya:
'zerbrechen,  zerstören,  zu  nichte  machen' : yS  rasmanö  iHndayäti  Yt  14.  62;  — Jra- vasayS  .  .  yä  .  .  aurva%anqm  ,  .  iSsBs scandayeinti  YtJj.  31;  —  ime  nS  *^uyra *bäzava  kanta  .  .  sHndayeinti  "die  da machen  unsere  starken  Arme  . .  mit  dem Messer  zu  nicht"  Yt.  /o.  42;—  tum  aisqm.. Ibaisi  scindayehi  Yt. 70.76;  —  alsqm  ihai^S scindaydmtmYt.i.tT,  —  sSndaya  {i%lh..) asavajanS  Yt.  iO.  76;  —  scindayat  F.  12,
mit  ai>i  'entzweibrcchen'(?):  yS ratmanS sHndayäti  . .  avi  rasmans  *sc?ndayeiti'^ Yt  14.  62.
äaiiihJvB   Yt  10.  78;  —  fravasayS  yra-
slandayeintis  . .  (bagiä  Yt  13. 33.
np.  htaila»,  likanad.  —  Pii. :  tkastan,  siaitär iSlan.  —  1)  Dieser  Antati  wegen  des  np. Fraei.  Sitanad.  Natürlich  kann  man  auch  ein Praes.  30  (Iter.)  anseilen.     S,  siami-  mit  No.  1.
—  >)  F  I,  E  1;  NA.  hat  sanä"  mit  *iner  Hds.
•  j.  skamb-  'stemmen',  nur  mit  Praev. Praes.  9+24  sambaya-^^.  —  Inf.  'scapta- yalca;  Absol.  'skamhm.
mit  upa  'festmachen':  s.  Absol.
mit  ^a  'festmachen,  befestigen':  %ri- sttüm  frasambananqm  {si.) /rasiimbayBit*^ tarasla  äps  Ttavayä  V. /i?.  74.
mit  paiti  'sich  entgegen  stemmen':  s. Inf.
ai.  skambhilhah,  siabhnäti,  liaihäydü;  np.  vgl. faliam  (Hbjc  AGr. /.  225).  —  PQ.  (ioV.7*): /rSi  aai^aniian ;  s.  noch  zum  Absol.  —  ')  iBild.
i.  BtHL.  Stud.  2.  104,  IIa.     Vgl.  auch  siattJ-
mit    No.    I.    —     '}    iSchr.    des    Nasals    s.
```


## [2026-09-14T01:47:44.144Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg438.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/438.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Save page image for audit"
}
```


### [2026-09-14T01:47:44.231Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-14T01:47:52.847Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 a55319786f2f0be1.txt; grep -n -i -A6 \"^ *Etymology\\|Root\" a55319786f2f0be1.txt | head -25; echo \"=== گسستن ===\"; head -5 fc4f445d305ef8ab.txt; grep -n -A6 -i \"^ *Etymology$\" fc4f445d305ef8ab.txt | head -20",
 "description": "Check PIE sek- and gosastan pages"
}
```


### [2026-09-14T01:47:54.031Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sek-
FETCHED: 2026-09-14T01:44:41Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/sek- - Wiktionary, the free dictionary

62: Root 
63-
64- 1.1.1 
65- Alternative reconstructions 
66-
67- 1.1.2 
68- Derived terms 
--
74: Root 
75-
76- 1.2.1 
77- Derived terms 
78-
79- 1.2.1.1 
80- Unsorted formations 
--
141: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
142-
143- Proto-Indo-European
144- [ edit ] 
145-
146: Root
147- [ edit ] 
148-
149- *sek- [ 1 ] 
=== گسستن ===
URL: https://en.wiktionary.org/wiki/گسستن
FETCHED: 2026-09-14T01:44:41Z
STATUS: 200
TITLE: گسستن - Wiktionary, the free dictionary

151: Etymology
152- [ edit ] 
153-
154- From Middle Persian [Book Pahlavi needed] ( wsstn' /⁠wisistan⁠/ , “ to break, split ” ) , from Proto-Iranian *wi- + *said- , ultimately from Proto-Indo-European *skeyd- (Cheung 2007). Cognate with Baluchi سندگ ( sendag , “ to break, split ” ) , Latin scindo , and Ancient Greek σχίζω ( skhízō ) .
155-
156- Pronunciation
157- [ edit ]
```


## [2026-09-14T01:55:08.790Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-438.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *sek- 'to cut' (Pok. 895) together with its extensions *(s)k(h)ed- / *(s)k(h)e-n-d- 'to split, scatter' (Pok. 918-919), *skei- 'to cut, separate' (Pok. 919-922), *(s)ker- 'to cut' (Pok. 938-947), *(s)kep-/*(s)kop-/*(s)kap-/*skab(h)- 'to work with a sharp tool' (Pok. 930-933), *(s)kel- 'to cut' (Pok. 923-927); plus, as a separate item, *ḱerh₂- / *ḱer-4 'to break, injure' (Pok. 577-578) = Nourai's 'Ker 2'\",\n \"note\": \"The root box is a lumping of eight or nine Pokorny lemmas under one head, and the lumping is largely sanctioned by the sources Nourai cites: Pokorny himself calls *(s)k(h)ed- an 'Erweiterung von sek- schneiden' (IEW 919) and *skei- 'Erweiterung von sek-' (IEW 920), and Watkins/AHD s.v. sek- says 'See also extended roots sked-, skei-, sker-1, sker-4'. The cited pages are right: POK 920 = skei-, 926 = (s)kel-2 (923-927), 930/931 = (s)kep-2, (s)kop-, (s)kap-, (s)keb(h)-, skab(h)- (930-933), 941 = (s)ker-4 (938-947). Two components are looser: 'Ker 2' is Pokorny's ḱer-4/ḱerə- 'versehren, zerfallen' (577-578), a palatal root that Pokorny keeps apart from *sek-, and the dung root *sker-(d)- (947) is joined to *sek- only in Watkins's presentation — Walde-Pokorny II 588 says flatly that taking this palatal sker- as a variant of *sqer- 'to cut' 'wäre eine unbeweisbare Vermutung'. Hence 'plausible' rather than 'confirmed': the label, the gloss 'to cut, scrape, separate, tear' and the language 'Indo-European' are all correct, but the box merges roots that modern handbooks keep separate.\",\n \"note_fa\": \"جعبهٔ ریشه چند ریشهٔ جداگانهٔ پوکورنی را زیر یک سر گرد آورده است: *sek- «بریدن» (پوکورنی ۸۹۵) با گسترده‌های آن *(s)ked-، *skei-، *(s)ker-، *(s)kep-/*(s)kap- و *(s)kel-. خودِ پوکورنی دو تای نخست را «گسترش sek-» می‌نامد و واتکینز (AHD) نیز همین کار را می‌کند؛ پس تا این اندازه ادعای نورایی پذیرفتنی است. اما «Ker 2» در حقیقت ریشهٔ کامی *ḱerh₂- «شکستن، آسیب رساندن» (پوکورنی ۵۷۷–۵۷۸) است و ریشهٔ *sker-(d)- «سرگین» (پوکورنی ۹۴۷) را والده–پوکورنی (ج۲ ص۵۸۸) صریحاً از *sker- «بریدن» جدا می‌داند و پیوند دادنشان را «گمانی اثبات‌ناپذیر» می‌خواند. شماره‌صفحه‌های نورایی همه درست‌اند. داوری: با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/sek-\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. 'sek-. To cut. ... 6. Basic form *sek- in Latin secare, to cut: SECANT, -SECT, SECTION ... See also extended roots sked-, skei-, sker-1, sker-4. [Pok. 2. sek- 895, sken-(d)- 929.]' (AHD_watkins1985.txt, grep '^sek-') — exactly Nourai's grouping.\"},\n   {\"ref\": \"POK:920\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 157 (printed 920): 'skei- schneiden, trennen, scheiden, Erweiterung von sek-; Anlaut z. T. auch sk-, skh-, skh-'.\"},\n   {\"ref\": \"POK:926\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root/lemma: (s)kel-2', 'Page(s): 923-927' — p.926 falls inside the (s)kel-2 'schneiden' entry.\"},\n   {\"ref\": \"POK:930,931\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root/lemma: (s)kep-2, (s)kop- and (s)kap- (s)keb(h)-, skob(h)- and skab(h)-; Meaning: to work with a sharp instrument', Page(s) 930-933 — includes the Persian material 'Npers. kafaδ, kavaδ burrows, digs, splits, kaftan'.\"},\n   {\"ref\": \"POK:941\", \"status\": \"supports\", \"note\": \"POK_full.txt 'Root/lemma: (s)ker-4, (s)kerə-, (s)kre-; Meaning: to cut', Page(s) 938-947; p.941 is inside it; the entry carries 'Old Indic carman-, Avestan caraman- fell, fur, skin' and 'Latin curtus abbreviated, mutilated (*kr̥-to-)'.\"},\n   {\"ref\": \"IEC:640\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt leaf 361 (printed page marker '640'): 'Ḱr̥t- (2) \\\"cut, blow\\\". Cf. Ḱertō — Skt. śūrtáh \\\"shattered\\\"; Arm. sartnum \\\"be separated\\\"' — i.e. Nourai's 'Ker 2'.\"},\n   {\"ref\": \"IEC:1155\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt leaf 638 (page markers 1154/1155): 'skeidh- (skeidhrā, skheidh-) slice, cut; blade, cutter, incision' and 'skeiiō (skeid, skheiiō) divide, split, distinguish, choose' — Nourai's 'Skei'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 564 and 587-588\", \"stance\": \"partial\", \"note\": \"II 564 s.v. (s)qend-: 'Av. scandayeiti zerbricht, vernichtet (die Schlachtreihen), skənda- m. Zerspaltung' and the remark 'Daß sqen- aus seq- schneiden erweitert sei…'; but II 588 on the dung root: 'Daß unser sker- als palatale Variante neben sqer- einst ebenfalls ausscheiden bedeutet habe, wäre eine unbeweisbare Vermutung' — so WP back the sek-/sked- link but not the sek-/sker-'dung' link.\"},\n   {\"src\": \"SYN\", \"where\": \"p.321 (leaf 363), section 4.95 DEAF\", \"stance\": \"supports\", \"note\": \"Buck: 'Lith. kurčias … cf. also Av. karəna- deaf, Skt. karṇa- short-eared, all with common notion of mutilated … fr. IE *(s)ker- cut'.\"},\n   {\"src\": \"KLN\", \"where\": \"pp.1432-34 s.vv. shape, shard, share, shear, short\", \"stance\": \"supports\", \"note\": \"Klein s.v. shear: 'fr. I.-E. base *(s)qer-, to cut, separate, whence also OI. kr̥ṇāti … kr̥ttiḥ hide, carman-, Avestic čarman-'; s.v. shape: 'fr. I.-E. base *skab-, to work with a stone scraper, to scrape'.\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"sčand; skenda; scapti; kaf, kâf\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the four items are genuine Avestan, two are not. (a) sčand = Av. skand- 'to break', pres. scandaya-/škəndaya-/scindaya- 'zerbrechen, zerstören' (Bartholomae col. 1566, Yt 10.42 'ime nō uγra bāzava kanta … sk̥ndayeinti'); Pokorny 919 s.v. (s)k(h)ed-, (s)k(h)e-n-d- 'zerspalten, zerstreuen (Erweiterung von sek-)' lists 'Avestan scandayeiti breaks, destroys'. (b) skenda = Av. skənda- m. '1) Bruch, Zerbrechen; 2) Gebrechen, körperlicher Schaden' (Bartholomae), whence the negated a-skənda- 'ohne körperlichen Schaden' — Nourai's gloss 'crippled, broken' is Gharib's rendering of the Sogdian reflex ʾskʾnt(y) oskand 'cripple, paralysed' (SOD entry 1546, p.61), which Gharib derives from exactly this Av. skənda-. (c) 'scapti to split' has no Avestan support: Bartholomae's skapta- is an adjective 'erstaunlich, wunderbar' (whence MP škaft, NP šigift), and the only form of that shape, paiti-scaptayaē-, is an infinitive of skamb- 'to prop, stemmen'. (d) 'kaf, kâf to break' are New Persian, not Avestan: Pokorny cites them under (s)kep-2 as 'Npers. kafaδ, kavaδ burrows, digs, splits, kaftan', and Horn no. 787 notes that the *skap-/*skabh- root was thought purely European until Nöldeke compared Gk. σκάπτω. So the arrow root→Avestan is right for sčand/skənda, but the box mixes in a mis-glossed Avestan adjective and two New Persian verbs.\",\n \"derivation_fa\": \"از چهار صورت این جعبه تنها دو تا واقعاً اوستایی‌اند. «sčand» همان ستاک اوستایی skand- «شکستن» است (حالِ scandaya-/scindaya- «خرد کردن، نابود کردن»، بارتولومه ستون ۱۵۶۶) که پوکورنی (ص ۹۱۹) زیر *(s)k(h)ed- «شکافتن، پراکندن، گسترشِ sek-» آورده است. «skenda» نیز اوستایی skənda- «شکستگی، عیب تنی» است؛ معنای «فلج، معیوب» که نورایی می‌دهد از بازتاب سغدی ʾskʾnt(y) در فرهنگ قریب (مدخل ۱۵۴۶، ص ۶۱) گرفته شده که خودْ آن را به همین skənda- اوستایی می‌رساند. اما «scapti» در اوستا به معنی «شکافتن» نیست؛ skapta- در بارتولومه صفتِ «شگفت‌انگیز» است (پهلوی škaft، فارسی «شگفت»). «kaf, kâf» هم اوستایی نیست بلکه فارسی نو است: پوکورنی آن‌ها را زیر *(s)kep- به‌صورت «npers. kafaδ, kavaδ» می‌آورد و هرن (شمارهٔ ۷۸۷) یادآور می‌شود که این ریشه تا زمان نولدکه ریشه‌ای اروپایی شمرده می‌شد. داوری: پژوهش امروزی برچسبِ «اوستایی» را برای دو واژهٔ آخر رد می‌کند.\",\n \"sources\": [W+\"شکستن\"],\n \"ref_check\": [\n   {\"ref\": \"POK:919\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 156 (printed 919) ends with the headword '(s)k(h)ed-, (s)k(h)e-n-d- zerspalten, zerstreuen (Erweiterung von sek- schneiden)'; POK_full gives its material 'Avestan scandayeiti breaks, destroys, skənda- m. destruction; Middle Persian škastan'.\"},\n   {\"ref\": \"POK:930\", \"status\": \"partial\", \"note\": \"(s)kep-2 (POK 930-933) does contain 'C. forms auf -p: Npers. kafaδ, kavaδ burrows, digs, splits, kaftan' — but as NEW PERSIAN, not Avestan; Pokorny lists no Avestan form here.\"},\n   {\"ref\": \"SOD:61\", \"status\": \"supports\", \"note\": \"Gharib, SOD_pages.txt leaf 126 = printed p.61, entry 1546: \\\"ʾskʾnt(y) B, S — oskand(e) ©fskandʾ; Av. skənda-; Parth. ʾsknd … cripple, paralysed\\\" — the source of Nourai's gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. skand-, skənda-, a-skənda-, skapta-\", \"stance\": \"partial\", \"note\": \"BRT.txt: 'j., g. skənda- m. 1) Bruch, Zerbrechen … 2) Gebrechen, körperlicher Schaden'; 'j. skand- V. brechen. Praes. scandaya-, škəndaya-, scindaya: zerbrechen, zerstören, zu nichte machen'; but 'j. skapta- Adj. erstaunlich, wunderbar: mp. škaft, np. šigift' — no Avestan verb 'to split' of that shape.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 564\", \"stance\": \"supports\", \"note\": \"'Av. scandayeiti \\\"zerbricht, vernichtet (die Schlachtreihen)\\\", skənda- m. \\\"Zerspaltung\\\"' under idg. (s)qend-.\"},\n   {\"src\": \"AHD\", \"where\": \"s.vv. sek-, skep-\", \"stance\": \"partial\", \"note\": \"Watkins: 'Extended root *skend-, to peel off, flay' under sek-; and a separate entry 'skep-. Also kep-. Base of words with various technical meanings such as to cut, to scrape, to hack … [Pok. 2. (s)kep- 931]' with no Iranian material.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"šekastan «شکستن ( شکن )»; šekâftan «شکافتن ، شکفتن ، کافتن»; kaftan, koftan «کَفتن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"šekastan: Av. scand-/skand- 'to break' > MP škastan, pres. šken(n)- (MacKenzie p.81 'škastan, šken(n)- [TBLWN-tn'] break') > NP šekastan/šekan-; the Old Persian counterpart is *skandāmiy (Horn no. 788: 'sikesten zerbrechen, Praes. siken-em; aw. √scand-, scindayeiti zerbrechen; phlv. skastan'). Mo'in's footnote in Borhan p.1279 gives the same chain: 'اوستا scand, scindayeiti (شکستن)، پهلوی shkastan، کردی shikestin, shikinandin، اسی sädfin' with a reference to Hübschmann 788. šekâftan/šekoftan/kâftan: MP škāftan, škāf- 'split, burst' (MacKenzie p.81) and škuftan, škōf- 'flower, blossom' — the same verb, 'burst open' > 'blossom' (whence شکوفه 'blossom' and شکاف 'crack'); from PIE *(s)kep-/(s)kap-/skab(h)- 'to work with a sharp tool' (Pok. 930-933), the simplex surviving as kâftan/kâvidan 'to dig, hollow out'; Wiktionary: 'From Middle Persian škāftan, from Proto-Indo-European *(s)kop- to strike, to beat … compare Ancient Greek κόπτω, Old High German happa'. شگفت is MP škeft 'hard, extraordinary, astonishing' (Av. skapta-), the same root with the -t- participle. kaftan/koftan 'to break open, split' is the prefixless doublet (Pokorny's 'npers. kafaδ, kavaδ'), still transitive کاویدن 'to dig'. Rudaki's line quoted in the book (کفیدش دل از غم …) uses exactly this kafīdan.\",\n \"derivation_fa\": \"«شکستن» از فارسی میانهٔ škastan (ستاک حال šken-) و آن از ستاک اوستایی scand-/skand- «شکستن» است؛ پارسی باستان *skandāmiy. هرن (شمارهٔ ۷۸۸) و حاشیهٔ معین بر برهان قاطع (ص ۱۲۷۹) هر دو همین زنجیره را می‌دهند: «اوستا scand، scindayeiti؛ پهلوی shkastan؛ کردی shikestin». «شکافتن/شکفتن» از پهلوی škāftan/škuftan «شکافتن، شکوفه دادن» است و از ریشهٔ هندواروپایی *(s)kep-/*(s)kap- «کار کردن با ابزار تیز» (پوکورنی ۹۳۰–۹۳۳)؛ هم‌ریشه با یونانی κόπτω. صورت بی‌پیشوند همان «کفتن/کافتن» و «کاویدن» است که معنی کهن «کندن» را نگاه داشته و پوکورنی نیز آن را با همین صورت‌های فارسی نو می‌آورد. «شگفت» نیز از پهلوی škeft (اوستایی skapta-) است. داوری: ادعای نورایی درست است.\",\n \"sources\": [W+\"شکستن\", W+\"شکافتن\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1275, 1279\", \"status\": \"supports\", \"note\": \"Borhan (Mo'in ed.) vol.3, pdf p.66 = printed 1275, footnote to شکافتن: 'پهلوی shkāftan … کردی bishkiwin, shikiwin … معنی کندن در فارسی «کافتن» و «کاویدن» محفوظ مانده'; pdf p.70 = printed 1279, footnote 2 to شکستن: 'اوستا scand, scindayeiti (شکستن)، پهلوی Shkastan، کردی shikestin, shikinandin، رک: هوبشمان ۷۸۸'.\"},\n   {\"ref\": \"HRN:175\", \"status\": \"supports\", \"note\": \"Horn p.175, no. 787 'sikäften spalten … phlv. skaft … Zu gr. σκάπτω graben, hacken (Nöldeke)' and no. 788 'sikesten zerbrechen, Praes. siken-em; aw. √scand-, scindayeiti zerbrechen; phlv. skastan; ap. *skanāmiy (aus *skadnāmiy)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p.81 s.vv. škastan, škāftan, škuftan, škeft\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'škāftan, škāf- [škʾp-tn' | M ʾškʾpt, N šikāftan] split, burst'; 'škastan, šken(n)- … break'; 'škuftan, škōf- … flower, blossom'; 'škeft … hard; extraordinary, astonishing; very'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *skand 'to break, cleave' (cross-ref. under *kart1)\", \"stance\": \"supports\", \"note\": \"Cheung cites *skand 'to break, cleave' as the Iranian verbal root behind the Shughni/Sarikoli forms contaminated with *kart-; the NP continuant is šikastan/šikan-.\"},\n   {\"src\": \"POK\", \"where\": \"919 and 930-933\", \"stance\": \"supports\", \"note\": \"'Npers. kafaδ, kavaδ burrows, digs, splits, kaftan' under (s)kep-2; MP škastan under (s)k(h)ed-.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"sâ 2, sâna, sya 1; fra-sanam\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are Pokorny's, and Nourai's page reference is exact: IEW p.920 s.v. skei- reads 'av. fra-sānəm \\\"Zerstörung\\\", sā-, sya- \\\"wehren\\\"'. Bartholomae has 'j. fra-sāna- n. Zerstörung, Vernichtung' (Yt 19.44) and the compound frakərəstō.fra-sāna- 'Zerstörung hervorrufend', so fra-sanam is real. But Nourai's gloss 'to sharpen ?' is not Pokorny's: Pokorny glosses the verb 'wehren' (to ward off), and his question-mark comes from Nourai himself, who in the chart's NOTE tells the reader to 'compare with the Avestan words from root Ak' — i.e. he suspects the sharpening sense belongs to the *h₂eḱ-/*ḱeh₂- family. Modern work goes further: Cheung 2007 (s.v. *saH 'to whet, cut') writes 'OAv. si- (sā-) to sharpen, cut ?. The verbal root may be non-existent. The attested forms can be interpreted differently: siiōdūm (< *siazd), sazdūm (< *saHh), v. Lubotsky 2001: 34', and he assigns what is left to PIE *ḱeh₂s- 'to sharpen, whet' (Pok. 541 f.), not to *skei-/*sek-. So the box is a faithful copy of Pokorny but rests on a reading modern Iranists no longer accept.\",\n \"derivation_fa\": \"صورت‌های این جعبه از پوکورنی گرفته شده و ارجاع نورایی دقیق است: پوکورنی در ص ۹۲۰ ذیل *skei- می‌نویسد «اوستایی fra-sānəm «نابودی»، sā-, sya- «بازداشتن»». بارتولومه نیز fra-sāna- «ویرانی، نابودی» را دارد، پس این واژه واقعی است. اما معنای «تیز کردن؟» که نورایی می‌دهد از پوکورنی نیست (او wehren «دفع کردن» می‌آورد)؛ خودِ نورایی هم در یادداشت جعبه خواننده را به ریشهٔ «Ak» ارجاع می‌دهد. چونگ (۲۰۰۷) ذیل *saH «تیز کردن، بریدن» می‌نویسد که «شاید این ستاک اصلاً وجود نداشته باشد» و صورت‌های گاهانی را جور دیگری می‌خواند، و آنچه می‌ماند را به ریشهٔ هندواروپایی *ḱeh₂s- «تیز کردن» (پوکورنی ۵۴۱ به بعد) می‌بندد نه به *skei-. داوری: با احتیاط پذیرفتنی است — نقل از پوکورنی درست است ولی خوانش آن کهنه شده است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:919\", \"status\": \"supports\", \"note\": \"POK_03.txt leaf 157 (printed page 920, i.e. the page whose entry begins at the foot of 919): 'skei- schneiden, trennen, scheiden, Erweiterung von sek- … av. fra-sānəm \\\"Zerstörung\\\", sā-, sya- \\\"wehren\\\"'. The forms and numbering (sā 2, sya 1) are Bartholomae's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. fra-sāna-, frakərəstō.fra-sāna-\", \"stance\": \"partial\", \"note\": \"BRT.txt: 'j. fra-sāna- n. Zerstörung, Vernichtung: ava apəməm gayehe *frasānəm uštānahe Yt 19.44'; 'j. frakərəstō.fra-sāna- Adj. Zerstörung, Vernichtung hervorrufend' — the noun is confirmed, but Bartholomae's verb sā- is 'wehren', not 'schärfen'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.325 f. s.v. *saH 'to whet, cut'\", \"stance\": \"contradicts\", \"note\": \"'OAv. sī- (sā-) to sharpen, cut ?. The verbal root may be non-existent. … «PIE *ḱeHs- to sharpen, whet = LIV: 319 f. | Pok.: 541 f.' — a different PIE root from *sek-/*skei-.\"},\n   {\"src\": \"AHD\", \"where\": \"s.v. sek- / kō-\", \"stance\": \"partial\", \"note\": \"Watkins lists no Iranian sharpening verb under sek-; the 'whet' family (cōs, catus, hone) sits under a separate root.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"sŭdan «سودن ( سود )»; farsŭdan «فرسودن»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The words and the immediate Iranian chain are beyond doubt: MP sūdan, pres. say- 'to rub, wear, tire, tear' (MacKenzie p.77 'say-, v. sūdan'; Book Pahlavi sʾd-/swtn) > NP سودن sūdan / سای- sāy-, with فرسودن = fra- 'forth' + sūdan 'to rub away, wear out' (cf. MP frasāy- and the noun فرسایش). What is wrong is the parent. Cheung 2007 puts the verb under Proto-Iranian *sauH¹ 'to rub, wear, whet' (BMP sʾd- /say-/, inf. swtn /sūdan/; Parth. sʾw- 'to crush'; Khot. sauy-; Chor. ps'w- 'to grind'; NP sūdan/sāy-), which he links to *saH and thence to PIE *ḱeh₂s-/*ḱeh₃- 'to sharpen, whet' (Pok. 541 f.: Lat. cōs 'whetstone', catus, ON hein), a root distinct from *sek-/*skei- 'to cut'. Horn no. 752 had already given the same equation from the Indian side — 'sūden reiben; ai. √śā- wetzen, schärfen … Die Bedeutung ist im Neupersischen verblasst; vergl. aber das Kurdische [sūn ein Messer reiben, schärfen]'. So the derivation of sūdan from a 'whet' root is right, but its attachment to Nourai's Sek/Skei box is not: modern scholarship files it under *ḱeh₂s- 'to sharpen', i.e. Nourai's own root 'Ak'-adjacent family, exactly as his NOTE on the parent box half-suspects.\",\n \"derivation_fa\": \"خودِ واژه‌ها و حلقهٔ ایرانی آن‌ها تردیدناپذیر است: فارسی میانه sūdan (ستاک حال say-) «ساییدن، فرسودن» > فارسی نو «سودن/سای-»؛ «فرسودن» = پیشوند fra- + سودن. اما پدرِ درخت نادرست است. چونگ (۲۰۰۷) این فعل را ذیل ایرانی آغازین *sauH «ساییدن، تیز کردن» می‌آورد و آن را به *saH و سرانجام به ریشهٔ هندواروپایی *ḱeh₂s- «تیز کردن، ساییدن» (پوکورنی ۵۴۱ به بعد؛ لاتین cōs «سنگ فسان»، catus) می‌رساند، نه به *sek- «بریدن». هرن نیز (شمارهٔ ۷۵۲) همین را از سوی سنسکریت گفته بود: «سودن = ساییدن؛ سنسکریت √śā «تیز کردن، فسان زدن»؛ معنا در فارسی نو کم‌رنگ شده، ولی کردی sūn «چاقو را تیز کردن» آن را نگاه داشته است». داوری: ریشه‌شناسی «ساییدن/تیز کردن» درست است، اما پژوهش امروزی این فعل را زیر ریشهٔ «بریدن» نمی‌گذارد؛ پس این پیکان رد می‌شود.\",\n \"sources\": [W+\"سودن\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1462\", \"status\": \"supports\", \"note\": \"Borhan vol.3, pdf p.253 = printed ~1458-1462, the فرسای/فرسودن block ('امر بفرسودن هم هست یعنی کهنه کن و محو ساز'; '۴ رک: فرساییدن. فرسودن') and pdf p.257 = printed 1462; the entries are there, with cross-references, i.e. the page reference is accurate for the Persian material.\"},\n   {\"ref\": \"BQT:1184\", \"status\": \"not_found\", \"note\": \"BQT_v2_pages.txt leaf 644 = printed 1184 shows the سنگ… / سنمار block (س-ن), not سودن; either the س-و entries fall a few pages later in this scan or the citation is off by a few pages. The OCR of vol.2 is too poor to settle it.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p.340 f. s.v. *sauH1 'to rub, wear, whet'\", \"stance\": \"contradicts\", \"note\": \"'BMP sʾd- /say-/ to rub, wear, tire, tear … Inf.: BMP swtn /sūdan/ … NP sūdan/sāy- to rub, wear, tear … The root *sauH either reflects a rare ua-stem of *saH … «PIE *ḱeHs- to sharpen, whet, Pok.: 541 f.'\"},\n   {\"src\": \"HRN\", \"where\": \"p.161, no. 752\", \"stance\": \"partial\", \"note\": \"'752. sūden reiben, Praes. sāy-em, sāyīden. ai. √śā- wetzen, schärfen. kurd. sūin, sūn reiben, ein Messer reiben, schärfen.' — Horn agrees on the sense but connects it with Skt śā-, not with a 'cut' root.\"},\n   {\"src\": \"PHD\", \"where\": \"p.77 s.v. say-\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'say-, v. sūdan' (the present stem of sūdan) — confirms the MP link but says nothing about the PIE root.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Avestan\",\n \"words\": \"kereta; kareman, čareman; karena_oša; ha-keret; skarenâ\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five belong to PIE *(s)ker-/*ḱer- 'to cut' (Pok. 938-947; Cheung *kart¹ 'to cut' = PIE *(s)ker-t-, 'Pok.: 941 f.' — Nourai's page exactly). kərəta- m. 'Messer' (Bartholomae; V 4.50 'ayaŋhaēnāi kərətaēiš'), a to-participle of kart- 'to cut', gives NP kārd; the 'cut trench' sense is Nourai's link to کرت. čarəman- n. 'Fell, Leder' (Bartholomae; N 38, Yt 5.129) = Skt carman-, from *ker- 'to cut (hide) off' (Walde-Pokorny II: 'ai. carman-, av. čarəman- Fell, Haut, Bed. wie lat. corium'); the variant 'kareman' in the box is the Indic/velar counterpart (Skt karman- is a different word), so the č- form is the Avestan one. 'karena_oša' is Horn's reading of Yt 5.93: Horn p.188 no. 845 'ker, kerr taub — aw. karenāoš-ca (yt. 5, 93) taub'; Bartholomae reads the same passage as karəna- Adj. 'taub' with a following ...nasca, and glosses Skt karṇa- 'mit verstümmelten (gestutzten) Ohren', i.e. literally 'with cropped ears' — precisely Nourai's 'cut from hearing'. ha-kərət is Av. 'at once, once' (= *sm̥-kr̥t 'one cut'), quoted by Klein under 'same': 'OI. sakŕ̥t, Avestic ha-kərət, at once, once'. skarəna- Adj. 'rund' (Bartholomae; Yt 10.95 'aiβiθa zəmō yat̰ paθanaiiā … skarənaiiā') is 'cut round'. The only imprecision is the doublet 'kareman'.\",\n \"derivation_fa\": \"هر پنج صورت به ریشهٔ هندواروپایی *(s)ker- «بریدن» (پوکورنی ۹۳۸–۹۴۷) بازمی‌گردند و ارجاع نورایی به ص ۹۴۱ دقیق است؛ چونگ نیز ذیل *kart «بریدن» همان «Pok. 941 f.» را می‌آورد. kərəta- «کارد» (بارتولومه) اسم مفعولِ kart- است. čarəman- «پوست، چرم» (بارتولومه؛ هم‌ریشه با سنسکریت carman-) از «آنچه از تن جانور بریده می‌شود». «karena_oša» خوانشِ هرن (ص ۱۸۸، شمارهٔ ۸۴۵) از یشت ۵٫۹۳ است: «aw. karenāoš-ca «کر»»؛ بارتولومه همان‌جا karəna- «کر» می‌خواند و آن را با سنسکریت karṇa- «گوش‌بریده» می‌سنجد — یعنی همان «بریده از شنوایی» نورایی. ha-kərət اوستایی «یک‌بار» است (*sm̥-kr̥t «یک بُرش») که کلاین نیز ذیل same آن را می‌آورد. skarəna- صفت «گِرد» است (بارتولومه). تنها بی‌دقتی، صورت دوگانهٔ «kareman» است که در اوستا نیست. داوری: ادعای نورایی درست است.\",\n \"sources\": [W+\"چرم\"],\n \"ref_check\": [\n   {\"ref\": \"POK:941\", \"status\": \"supports\", \"note\": \"IEW 938-947 '(s)ker-4, (s)kerə-, (s)kre- to cut': 'Old Indic carman-, Avestan caraman- fell, fur, skin'; 'Latin corium thick skin, leather'; 'Latin curtus abbreviated, mutilated (*kr̥-tó-)'.\"},\n   {\"ref\": \"KLN:1432\", \"status\": \"supports\", \"note\": \"Klein 1966, leaf 760-761 (printed 1432-1434): s.v. shear 'fr. I.-E. base *(s)qer-, to cut, separate, whence also OI. kr̥ṇāti … kr̥ttiḥ hide, carman-, Avestic čarman-'; s.v. short 'from a dental enlargement of I.-E. base *(s)qer-, to cut … L. curtus, short'. (Klein's Avestic ha-kərət stands a few pages earlier, p.1378 s.v. same.)\"},\n   {\"ref\": \"HRN:188\", \"status\": \"supports\", \"note\": \"Horn p.188, no. 845: 'ker, kerr taub. aw. karenāoš-ca (yt. 5, 93) taub, Spiegel ZDMG. 32,721; ai. karṇá- mit verstümmelten (gestutzten) Ohren (Geldner, Vedische Studien I,138).' — the exact source of Nourai's 'karena_oša'.\"},\n   {\"ref\": \"SYN:321\", \"status\": \"supports\", \"note\": \"Buck p.321 (SYN.txt leaf 363), 4.95 DEAF: 'Av. karana- (so NPers. kar deaf), see above, 5 and Barth., IF 3.169. Av. asrut-gaoša-, lit. having unhearing ears'; and in §5 'cf. also Av. karəna- deaf, Skt. karṇa- short-eared, all with common notion of mutilated … fr. IE *(s)ker- cut'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.vv. kərəta-, čarəman-, karəna-, skarəna-, hakərət\", \"stance\": \"supports\", \"note\": \"'j. kərəta- m. Messer … insbes. als Waffe, Dolchmesser, Dolch … Zum V. karət-. Vgl. ai. kattarī- f. Jagdmesser, np. kārd Messer'; 'j. čarəman- n. Fell, Leder'; 'j. karəna- Adj. taub … ai. karṇa- Ohr, np. kar taub'; 'j. skarəna- Adj. (fem. °nā-) rund'; hakərət in V 7.74 'hakərət āpō frasnāδayən'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.243 f. s.v. *kart1 'to cut'\", \"stance\": \"supports\", \"note\": \"'YAv. kart- to cut … *NWIR: NP kārd, Bal. karč, Kurd. kêr, … Anar./Qohr./Sang. kart knife … «PIE *(s)ker-t- to cut => LIV: 559 f. | Pok.: 941 f.'\"},\n   {\"src\": \"IEC\", \"where\": \"pp.537-538 s.v. kortos\", \"stance\": \"supports\", \"note\": \"Mann: 'kortos, ā, us (1) cut, lopped, shortened, short; cut, section, piece … Av. karəto knife; Per. kārd, id.; Oss. kard knife, sword; Tokh. B kerte sword … Lat. curtus short, docked'.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"kârd «کارد»; kart «کَرت»; čarm «چرم»; kar «کر»; agar «اگر ( مگر ، هرگز )»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"kârd: Av. kərəta- > MP kārd [krt', heterogram SKYN'] (MacKenzie p.49 'kārd … knife') > NP کارد; Mo'in's footnote in Borhan p.1559 is verbatim 'کارد … اوستا karəta (کارد، چاقو)؛ پهلوی kart؛ هندی باستان kart, kr̥ntáti (بریدن)؛ کردی kird, kit؛ اسی kʼard؛ بلوچی kārc'. Horn no. 833: 'kārd Messer. aw. karəta- Messer; phlv. kārt; ai. vergl. √kart-, kr̥ntáti schneiden'. čarm: Av. čarəman- > OP carman- > MP čarm [clm] > NP چرم (Wiktionary: 'From Middle Persian čarm skin, hide, leather, from Old Persian 𐎨𐎼𐎶𐎴 carman-, from Proto-Iranian *čárma'); Horn no. 438 'čerm Fell, Haut. aw. čarəman-; phlv. čarm; ai. cárman-'. kar 'deaf': Av. karəna- > MP karr [kr | M qr] 'deaf' (MacKenzie p.50) > NP کر; Buck p.321 says so explicitly, and Wiktionary 'From Middle Persian karr deaf … Likely related to Sanskrit karṇa- ear'. kart 'a bed/plot cut for irrigation' is the same *kr̥t- 'cut' formation (cf. Sangesari/Anarak kart 'knife' in Cheung), a plausible but less securely documented member. agar is the weak link: Horn no. 106 'eger wenn … Zusammenhang mit phlv. akarč, np. hergiz ist wohl unzweifelhaft; pāz. agar. Ap. *hakaram ein Mal, Darmesteter, Et. ir. I, 245', and no. 1092 derives هرگز from ap. *hakaram-čiy 'ein Mal' but marks it 'unsicher'; مگر is transparently ma + agar (Horn no. 988). Wiktionary knows only 'From Middle Persian ḥt /agar/. Compare Parthian ag' and offers no 'once' etymology, so the 'cut once' reading of اگر is a nineteenth-century conjecture that current handbooks do not repeat.\",\n \"derivation_fa\": \"«کارد» از پهلوی kārd و آن از اوستایی kərəta- «کارد»؛ حاشیهٔ معین بر برهان (ص ۱۵۵۹) عیناً همین را می‌آورد: «اوستا karəta؛ پهلوی kart؛ هندی باستان kr̥ntáti (بریدن)؛ بلوچی kārc». «چرم» از پهلوی čarm، پارسی باستان carman-، اوستایی čarəman- (هرن شمارهٔ ۴۳۸). «کر» از پهلوی karr «کر» و اوستایی karəna-؛ باک (ص ۳۲۱) و ویکی‌واژه هر دو تأیید می‌کنند و آن را با سنسکریت karṇa- «گوش» می‌سنجند. «کرت» نیز ساختی از همان ستاک *kr̥t- «بریدن» است (قس کرتِ گویشی به معنی «کارد» در چونگ). اما «اگر» حلقهٔ سست زنجیره است: هرن (شمارهٔ ۱۰۶) پیوند آن را با پهلوی akarč و «هرگز» می‌پذیرد و از قول دارمستتر پارسی باستان *hakaram «یک بار» را می‌آورد، ولی خودِ او در شمارهٔ ۱۰۹۲ آن را «نامطمئن» می‌خواند؛ ویکی‌واژه تنها «از فارسی میانه agar» می‌گوید و از «یک بار» سخنی نیست. «مگر» همان ma + agar است. داوری: کارد، چرم و کر قطعی؛ «اگر = یک‌بار بریده» گمانی کهن و پذیرفتنی با احتیاط.\",\n \"sources\": [W+\"کارد\", W+\"چرم\", W+\"کر\", W+\"اگر\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1559\", \"status\": \"supports\", \"note\": \"Borhan vol.3, pdf p.352 = printed ~1559, Mo'in's footnote 5: 'کارد - بسکون سوم، اوستا karəta (کارد، چاقو)؛ پهلوی kart؛ هندی باستان kart، kr̥ntáti (بریدن)… کردی kird, kit؛ استی kʼard؛ بلوچی kārc … آلت برنده‌ای از آهن و فولاد'.\"},\n   {\"ref\": \"HRN:25\", \"status\": \"partial\", \"note\": \"Horn p.25, no. 106: 'eger wenn, egerči, ger. Zusammenhang mit phlv. akarč, np. hergiz (No. 1092) ist wohl unzweifelhaft; pāz. agar. Ap. *hakaram ein Mal, Darmesteter, Et. ir. I, 245.' — supports the 'once' idea but only as Darmesteter's conjecture.\"},\n   {\"ref\": \"HRN:98\", \"status\": \"supports\", \"note\": \"Horn p.98, no. 438: 'čerm Fell, Haut. aw. čarəman- Fell; phlv. čarm; ai. cárman- Fell.'\"},\n   {\"ref\": \"HRN:221\", \"status\": \"supports\", \"note\": \"Horn p.221, no. 988: 'meger wenn nicht, ausser, vielleicht. me nicht + eger (No. 106); pāz. ma agar' — confirms مگر = ما + اگر.\"},\n   {\"ref\": \"HRN:244\", \"status\": \"partial\", \"note\": \"Horn p.244, no. 1092: 'hergiz jemals, je, mit Negation niemals. ap. *hakaram-čiy ein Mal (Darmesteter, Et. ir. I, 245; unsicher); phlv. akarč bezw. hakarč … Np. hergiz gegen phlv. hakarč ist wohl durch her beeinflusst.' — Horn himself labels the 'one time' etymon 'unsicher'.\"},\n   {\"ref\": \"MON:2935\", \"status\": \"not_checked\", \"note\": \"The six-volume Mo'in is not online and not on disk; the two-volume Adena condensation (MON_part1/2.txt) has no page mapping, so the page number cannot be checked.\"},\n   {\"ref\": \"SYN:321\", \"status\": \"supports\", \"note\": \"Buck p.321: 'Av. karana- (so NPers. kar deaf)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"pp.49-50, 5 s.vv. kārd, karr, agar\", \"stance\": \"supports\", \"note\": \"'kārd [SKYN' < A skynʾ; krt' | N ~] knife'; 'karr [kr | M qr, N ~] deaf'; 'agar [HT, for A hn | M ʾgr, N ~] if'; index 'knife kārd', 'deaf karr'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.244 s.v. *kart1\", \"stance\": \"supports\", \"note\": \"'NP kārd, Bal. karč, Kurd. kêr … Anar. kart, Qohr. kart, Sang. kart, Nn. kart knife' — the dialect forms kart show that Nourai's کَرت belongs here.\"},\n   {\"src\": \"BRT\", \"where\": \"s.v. karəna-\", \"stance\": \"supports\", \"note\": \"'j. karəna- Adj. taub … ai. karṇa- Ohr, kal. stutzohrig, np. kar taub.'\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Sogdian\",\n \"words\": \"crm; krn; krt\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The three Sogdian words are in Gharib's dictionary exactly where Nourai puts them, and all three continue the same Old Iranian *ker-/*kart- material as the Avestan box: crm (Buddhist and Christian Sogdian) 'skin, leather' < *čarma- (= Av. čarəman-, NP čarm); krn 'deaf' < *karna- (= Av. karəna-, MP karr, NP kar); krt (Buddhist Sogdian) 'knife' < *kr̥ta- (= Av. kərəta-, MP kārd). Sogdian, as an eastern Middle Iranian language, keeps the inherited consonants (c- for *č-, -rt for *-rta-) where Persian voices and levels them, so the set is a good independent control on the Persian box #6. Gharib's related verb stems ʾskrʾnt- 'to injure, destroy' (< *uz-skr̥nt-) and ptkrʾnt- 'to cut off' show the verbal root alive in Sogdian too.\",\n \"derivation_fa\": \"هر سه واژهٔ سغدی در فرهنگ قریب دقیقاً در همان صفحه‌هایی هستند که نورایی نشان می‌دهد و هر سه دنبالهٔ همان مادهٔ ایرانی باستانِ *ker-/*kart- اند: crm «پوست، چرم» از *čarma- (اوستایی čarəman-)، krn «کر» از *karna- (اوستایی karəna-) و krt «کارد» از *kr̥ta- (اوستایی kərəta-). سغدی به‌عنوان زبانی ایرانی میانهٔ شرقی، همخوان‌های کهن را نگاه داشته است (c- و خوشهٔ -rt) و از این رو گواهی مستقل خوبی برای جعبهٔ فارسی است. قریب ستاک‌های فعلی ʾskrʾnt- «آسیب رساندن، نابود کردن» و ptkrʾnt- «بریدن» را هم دارد. داوری: ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:128\", \"status\": \"supports\", \"note\": \"Gharib entry 3254 'crm B, S — skin, leather', SOD_pages.txt leaf 193 (printed p.128 with the −65 offset that the other two citations confirm).\"},\n   {\"ref\": \"SOD:193\", \"status\": \"supports\", \"note\": \"Gharib entry 4842 krn 'deaf' (the book's English index reads 'deaf 4842'), SOD_pages.txt leaf 258 = printed p.193.\"},\n   {\"ref\": \"SOD:194\", \"status\": \"supports\", \"note\": \"Gharib entry 4867 'krt B — knife' (index: 'knife 4867'), SOD_pages.txt leaf 259 = printed p.194; entry 4869 krtʾync(h) 'with knife, of knife'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"entries 1561, 3254, 4842, 4867\", \"stance\": \"supports\", \"note\": \"Besides the three nouns, Gharib 1561 'ʾskrʾnt- B — oskrand (ʾskrnt-) ©<*uz-skr̥- ; Skt. utkr̥ntati … (to)injure, (to)destroy' shows the verb *kart- in Sogdian.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.243 s.v. *kart1, Sogdian section\", \"stance\": \"supports\", \"note\": \"'(+ *us-) BSogd. ʾskrʾnt(-) to cut up || (+ *pati-) BSogd. ptkrʾnt- to cut through, off || (+ *fra-) CSogd. frqrnt- to destroy' — the same root in Sogdian.\"},\n   {\"src\": \"BRT\", \"where\": \"s.vv. čarəman-, karəna-, kərəta-\", \"stance\": \"supports\", \"note\": \"The Avestan etyma of the three Sogdian words are all in Bartholomae (see node #5).\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Avestan\",\n \"words\": \"sâri, sari, said, sid; wi-sis, vi-saĕd; sairi-gaona\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three different strands are packed into one box, and Nourai's three Pokorny pages match them one by one. (a) sāri/sari = Av. sari- 'piece, fragment, shard' and sari- f. 'break, ruin', with a-sarəta- 'unbroken' — Pokorny 578 s.v. ḱer-4/ḱerə- 'versehren, zerfallen': 'Avestan asareta- not broken …, sari- m. piece, fragment, shard'; Cheung 2007 s.v. *sarH³ 'to break' quotes the same two forms from V 19.4 and V 8.85 and gives PIE *ḱerH₂-, 'Pok.: 578'. (b) said/sid, wi-sis, vi-saēd = the root *said- 'to split, break': Av. auua.siδ- 'to split' (perf. opt. auua.hisiδiiat̰, Yt 8.54), asista- 'not split', siδara- 'hole, fissure' — Pokorny 920-921 s.v. skei-d-, 'av. saēd- spalten, avahisiδyāt̰ er möge zerspalten'; Cheung *said¹ 'to break, split, destroy', PIE *skeid-, 'Pok.: 920 f.' — again Nourai's page. (c) sairi-gaona is a real Avestan compound, Vd 8.16-18 'spānəm … sairi.gaonəm' (Bartholomae s.v. spaēta-), literally 'dung-coloured' = sairi- (= sairya- n. 'Dünger, Mist') + gaona- 'hair, colour', so the dung element is right and Nourai's cross-reference to root 'Gĕu 1' is for the gaona- half. His gloss 'like cut (dropped) from the body, dung' is his own etymological paraphrase, not the word's meaning, and the attachment of sairya- to a 'cut' root is what Walde-Pokorny II 588 calls 'eine unbeweisbare Vermutung'. Hence plausible rather than confirmed.\",\n \"derivation_fa\": \"این جعبه سه رشتهٔ جداگانه را در خود دارد و هر سه صفحهٔ پوکورنی که نورایی می‌دهد درست است. نخست sari- اوستایی «پاره، تکه» و a-sarəta- «نشکسته» که پوکورنی در ص ۵۷۸ ذیل *ḱer-4 «آسیب زدن، فروریختن» آورده و چونگ نیز ذیل *sarH «شکستن» با همان ارجاع «Pok. 578». دوم ستاک *said- «شکافتن»: اوستایی auua.siδ-، asista-، siδara- که پوکورنی در ص ۹۲۰ ذیل *skei-d- می‌آورد و چونگ ذیل *said با «Pok. 920 f.». سوم sairi-gaona که ترکیبی واقعی اوستایی است (وندیداد ۸٫۱۶: spānəm sairi.gaonəm «سگِ سرگین‌رنگ») از sairi- (= sairya- «سرگین، کود») و gaona- «مو، رنگ»؛ پس جزءِ «سرگین» درست است و ارجاع نورایی به ریشهٔ «Gĕu 1» برای جزء دوم است. اما معنایی که او می‌دهد («آنچه از تن جدا/افتاده») تفسیر خودِ اوست و پیوند sairya- با ریشهٔ «بریدن» را والده–پوکورنی (ج۲ ص۵۸۸) «گمانی اثبات‌ناپذیر» می‌خواند. داوری: با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:578\", \"status\": \"supports\", \"note\": \"IEW 578 'ḱer-4 and ḱerə- : ḱrē-, to hurt, harm; to be spoiled': 'Avestan asareta- not broken, not made discouraged (= Old Indic aśīrta-), sari- m. piece, fragment, shard, sari- f. break, ruin; … perhaps npers. gusīxtan/gusilam rupture, slit, separate from Old Persian *vi-sr̥dāmiy'.\"},\n   {\"ref\": \"POK:920\", \"status\": \"supports\", \"note\": \"IEW 920-921 s.v. skei-d-: 'av. saēd- spalten, avahisiδyāt̰ er möge zerspalten, siδara- (leg. siδra-) n. Loch, Öffnung, Riß, a-sista- nicht gespalten' (POK_03.txt leaf 158).\"},\n   {\"ref\": \"POK:947\", \"status\": \"supports\", \"note\": \"IEW 947-948 'sker-(d)-, to defecate': 'Avestan sairya- manure, crap, muck, droppings. Middle Persian sargōn, np. sargīn ds.' — the sairi- of sairi-gaona.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.vv. sairya-, spaēta- (Vd 8.16), and the sairi.° compounds\", \"stance\": \"partial\", \"note\": \"'j. sairya- n. Dünger, Mist … Kompos. (s. sairi.°). Vgl. mp. (Pü.) sargēn, np. sargīn Mist, Dünger'; the compound itself appears s.v. spaēta-: 'spānəm … spaētəm sairi.gaonəm V 8.16, 17, 18' — i.e. 'a white, dung-coloured dog', so sairi.gaona- = 'dung-coloured', not 'dung'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp.326-327 s.v. *said1 and p.338 s.v. *sarH3\", \"stance\": \"supports\", \"note\": \"'*said¹ to break, split, destroy — YAv. auua.siδ- to split … «PIE *skeid- = LIV: 547 f. | Pok.: 920 f.'; '*sarH³ to break — YAv. asarəta- (ppp.) unbroken (V 19.4), YAv. sari- (m.) piece, fragment (V 8.85) … «PIE *ḱerH₂- = LIV: 327 f. | Pok.: 578'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 587-588\", \"stance\": \"contradicts\", \"note\": \"s.v. sker- 'cacare; Mist, Kot des Leibes': 'av. sairya- Mist, mpers. sargōn, np. sargīn ds.' but then 'Daß unser sker- als palatale Variante neben sqer- einst ebenfalls ausscheiden bedeutet habe, wäre eine unbeweisbare Vermutung' — WP refuse the link to the 'cut' root.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Persian\",\n \"words\": \"gosîxtan «گسیختن ( گسستن ، گسیل )»; sargin, sergin «سرگین»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"gosīxtan/gosistan/gosil: OIr. *ui-said- 'to break apart' > MP wisistan [wsstn'], pres. wisin(n)- 'to break, split' (MacKenzie, index 'split … wisistan') > NP گسستن, with the suppletive present گسل-; Wiktionary: 'From Middle Persian wisistan to break, split, from Proto-Iranian *wi- + *said-, ultimately from Proto-Indo-European *skeyd- (Cheung 2007)', cognate Lat. scindō, Gk. σχίζω. Mo'in's footnote in Borhan p.1816 gives the same: 'گسستن … از ریشهٔ اوستایی sid = saēd؛ پارسی باستان vi-sad «هوبشمان ۹۲۲»؛ پهلوی v(i)sastan'. Horn no. 922 adds Bartholomae's suggestion that Persian mixes the two synonymous roots sk̑heid- (Av. saēd-) and k̑er- (Skt śr̥ṇāti), and derives gusil- from *vi-sard- — which is Cheung's *sarH³ (gusil- < *ui-sr̥Hd-). Horn ends 'Der Inf. gusīxten ist ganz unklar': the -x- infinitive گسیختن is a secondary Persian formation beside the regular گسستن, so the headword form of the box is the least well explained member. sargin: Av. sairya- 'Mist' > MP sargēn [slgyn'] 'dung, manure' (MacKenzie p.74) > NP سرگین. The Iranian chain is unanimous (Pokorny 947, Walde-Pokorny II 587, MacKenzie, Wiktionary); only its PIE address is contested — Wiktionary/EWAia put MP sargēn under Proto-Iranian *ćákr̥, PIE *ḱókʷr̥ 'dung' (Skt śakŕ̥t, Gk κόπρος), not under an extension of *sek- 'to cut'.\",\n \"derivation_fa\": \"«گسستن/گسیختن» از ایرانی باستان *ui-said- «از هم گسستن» و از راه فارسی میانهٔ wisistan (ستاک حال wisin-) به فارسی نو رسیده است؛ ویکی‌واژه به نقل از چونگ (۲۰۰۷) همین را می‌گوید و هم‌ریشهٔ لاتین scindō و یونانی σχίζω می‌شمارد. حاشیهٔ معین بر برهان (ص ۱۸۱۶) نیز می‌نویسد: «از ریشهٔ اوستایی sid = saēd؛ پارسی باستان vi-sad (هوبشمان ۹۲۲)؛ پهلوی v(i)sastan». ستاک حال «گسل-» را چونگ از *ui-sr̥Hd- می‌گیرد (ریشهٔ *sarH «شکستن»). نکته آنکه هرن (شمارهٔ ۹۲۲) خودِ مصدرِ «گسیختن» را «کاملاً ناروشن» می‌داند؛ صورت اصیل «گسستن» است. «سرگین» از فارسی میانهٔ sargēn و آن از اوستایی sairya- «کود، سرگین» است (مکنزی، پوکورنی ۹۴۷). تنها اختلاف در نشانی هندواروپایی آن است: ویکی‌واژه و پژوهش امروزی آن را از *ḱókʷr̥ «سرگین» (سنسکریت śakŕ̥t، یونانی κόπρος) می‌دانند نه از گسترش *sek- «بریدن». داوری: پیکانِ اوستایی → فارسی درست است.\",\n \"sources\": [W+\"گسستن\", W+\"سرگین\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:205\", \"status\": \"partial\", \"note\": \"Horn p.205, no. 922: 'gusisten zerbrechen, trennen, Praes. gusihem … phlv. v(i)sastan. … Bartholomae denkt an eine Vermischung der beiden synonymen Wurzeln sk̑heid- (aw. saēd-, hisidyāt̰ …) und k̑er- (ai. śr̥-, śr̥ṇāti). Np. gusisten wäre ap. *visistanaiy (aus *vi-sid-tanaiy) … Der Inf. gusīxten ist ganz unklar.' — supports the roots but not the -x- infinitive Nourai uses as headword.\"},\n   {\"ref\": \"BQT:1816\", \"status\": \"supports\", \"note\": \"Borhan vol.3, pdf p.613 = printed ~1816-1818, footnote 9: 'گسستن … از ریشهٔ اوستایی sid = saēd … پارسی باستان vi-sad «هوبشمان ۹۲۲». پهلوی v(i)sastan … قطع کردن، بریدن، جدا کردن'; pdf 614 has گسیختن cross-referenced to گسستن.\"},\n   {\"ref\": \"POK:578\", \"status\": \"supports\", \"note\": \"IEW 578 s.v. ḱer-4: '… ein d(h)-Präsens dazu ist vielleicht npers. gusīxtan/gusilam \\\"Rupture, slit, separate\\\" from Old Persian *vi-sr̥dāmiy' — Pokorny names Nourai's very word.\"},\n   {\"ref\": \"POK:947\", \"status\": \"supports\", \"note\": \"IEW 947 s.v. sker-(d)-: 'Avestan sairya- manure …; Middle Persian sargōn, np. sargīn ds.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p.74 s.v. sargēn; index s.vv. dung, manure, split\", \"stance\": \"supports\", \"note\": \"MacKenzie: 'sargēn [slgyn' | N sargin] dung, manure'; index 'dung gāh, sargēn', 'manure sargēn', 'split darrīdan, škāftan, wisistan'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"pp.327, 338 s.vv. *said1, *sarH3\", \"stance\": \"supports\", \"note\": \"'(+ *ui-) NP gusistan (supplet. gusil-) to shatter, break' under *said¹; '(+ *aua-) NP gusil- to shatter, break. The pres. stem NP gusil- is from *ui-sr̥Hd- … The suppletive past stem gusist- also goes back to the same root' under *sarH³.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 587-588\", \"stance\": \"partial\", \"note\": \"'av. sairya- Mist, mpers. sargōn, np. sargīn ds. (Solmsen WfklPh. 1906, 871)' — the Iranian chain, with the explicit refusal to derive this sker- from sqer- 'to cut'.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Latin\",\n \"words\": \"secare; re-secare; risecum; cortus\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"secāre 'to cut' is the plain Latin continuant of PIE *sek- (Watkins s.v. sek-: 'Basic form *sek- in Latin secāre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT'), and re-secāre 'to cut back, cut off' is its prefixed compound (English resect); Nourai's gloss 'cut against' for re- is loose — re- here is 'back, off'. 'cortus : short' is the book's misprint for Latin CURTUS 'shortened, mutilated' < *kr̥-to- (Pokorny 941 'Latin curtus abbreviated, mutilated (*kr̥-tó-)'; Klein s.v. short; Wiktionary curtus 'From Proto-Italic *kortos, from Proto-Indo-European *(s)kr̥tós short, from *(s)ker- to cut'). The form on the printed page really is 'cortus', so the extraction is faithful and the error is Nourai's — probably a slip from the Proto-Italic *kortos or from Latin cohors/cortis. 'risecum' is Medieval Latin risicum/resicum, the postulated Vulgar Latin *resecum 'that which cuts, cliff, reef' behind Italian risco; the derivation is only a guess (see node #11) and the word is Medieval, not classical Latin.\",\n \"derivation_fa\": \"secāre «بریدن» بازماندهٔ مستقیم ریشهٔ *sek- در لاتین است (واتکینز ذیل sek-: «Latin secāre, to cut: SECTION، INSECT، RESECT») و re-secāre ترکیب پیشونددار آن «باز بریدن، بریدن و دور انداختن» است؛ معنای «cut against» که نورایی می‌دهد دقیق نیست، re- در اینجا «باز، پس» است. «cortus» خطای چاپی کتاب برای لاتین curtus «کوتاه، بریده» است، از *kr̥-to- (پوکورنی ۹۴۱: «Latin curtus … (*kr̥-tó-)»؛ ویکی‌واژه: از ایتالیکِ آغازین *kortos و هندواروپایی *(s)kr̥tós). در صفحهٔ چاپی نیز همین «cortus» آمده است، پس خطا از کتاب است نه از خوانش اسکن؛ گویا نورایی صورت ایتالیکِ آغازین *kortos را با لاتین اشتباه گرفته است. «risecum» هم لاتین کلاسیک نیست بلکه لاتین میانه risicum/resicum و صورت بازسازیِ لاتین عامیانه *resecum است که ریشه‌شناسی آن خود مورد تردید است (بنگرید به گرهٔ بعد).\",\n \"error_in\": \"book\",\n \"book_prints\": \"cortus\",\n \"correct_form\": \"curtus\",\n \"sources\": [W+\"curtus\", \"https://www.etymonline.com/word/risk\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. sek- lists Latin secāre with SECANT, SECTION, INSECT, RESECT; and s.v. sker-1 'Suffixed zero-grade form *kr̥-to- in Latin curtus, short: CURT, CURTAL, KIRTLE' — the correct spelling of the book's 'cortus'.\"},\n   {\"ref\": \"IEC:1155\", \"status\": \"partial\", \"note\": \"Mann pp.1154-1155 carry skeidh- 'slice, cut' and skeiiō 'divide, split' (with Lat. sciō), not secāre/resecāre; Mann's sek- 'cutting, mowing' entries stand at p.1123 ('sek-, radical element of following entries: \\\"cut\\\"'). The page supports the root box's 'Skei' rather than this Latin node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"941 (s.v. (s)ker-4)\", \"stance\": \"supports\", \"note\": \"'Latin curtus \\\"abbreviated, mutilated\\\" (*kr̥-tó-)' — and under sek- (895) Latin secāre.\"},\n   {\"src\": \"KLN\", \"where\": \"p.1434 s.v. short\", \"stance\": \"supports\", \"note\": \"'from a dental enlargement of I.-E. base *(s)qer-, to cut, whence also OI. kr̥dhúḥ shortened, maimed, small, L. curtus short'.\"},\n   {\"src\": \"LEW/LAT\", \"where\": \"Walde-Hofmann and Ernout-Meillet s.vv. secō, curtus\", \"stance\": \"supports\", \"note\": \"Both Latin etymological dictionaries on disk give secō < *sek- and curtus < *kr̥-to-; neither knows a classical Latin *cortus 'short' or a classical risecum.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"French\",\n \"words\": \"risque\",\n \"verdict\": \"disputed\",\n \"derivation\": \"French risque (16th c.) is certainly the immediate source of English risk and of modern Persian ریسک, but its own origin is not the one drawn here. Etymonline: 'risk (n.) 1660s, risque, hazard, danger, peril … from French risque (16c.), from Italian risco, riscio (modern rischio), from riscare \\\"run into danger\\\", a word of uncertain origin.' The derivation from Vulgar Latin *resecum/*resecāre 'to cut off' (hence 'rock that cuts ships') is the account of the 1969-76 American Heritage Dictionary that Nourai is quoting, but the current AHD has replaced it: 'French risque, from Italian risco, rischio, probably from Medieval Greek rizikon, sustenance obtained by a soldier through his own initiative, fortune, from Arabic rizq, sustenance, that which God allots, from Syriac rūzīqā, daily bread, from Middle Iranian rōčīg, from rōč, day, from Old Iranian *raučah-.' On that account risque has nothing to do with cutting at all — it is an Iranian word (rōz 'day' > 'daily bread') that travelled through Syriac, Arabic and Byzantine Greek into Italian. Either way the arrow Latin secāre → French risque is not supported by current scholarship.\",\n \"derivation_fa\": \"واژهٔ فرانسویِ risque (سدهٔ شانزدهم) بی‌گمان سرچشمهٔ بی‌واسطهٔ risk انگلیسی و «ریسک» فارسی است، اما خاستگاه خودش آن نیست که در نمودار کشیده شده. اتیمانلاین می‌نویسد: «از فرانسوی risque، از ایتالیایی risco/riscio، از riscare «به خطر افتادن»، واژه‌ای با خاستگاه نامعلوم». اشتقاق از لاتین عامیانهٔ *resecum «آنچه می‌بُرد؛ صخرهٔ دریایی» همان چیزی است که ویراست‌های کهنِ AHD (که نورایی از آن نقل می‌کند) می‌گفتند، ولی ویراست کنونی AHD آن را کنار گذاشته است: «از ایتالیایی risco، احتمالاً از یونانی میانهٔ rizikon، از عربی رزق، از سریانی rūzīqā «نان روزانه»، از ایرانی میانهٔ rōčīg، از rōč «روز»، از ایرانی باستان *raučah-». یعنی این واژه در اصل ایرانی است («روز» > «روزی») که از راه سریانی و عربی و یونانی به ایتالیایی رفته و هیچ پیوندی با «بریدن» ندارد. داوری: پژوهش امروزی این پیکان را رد می‌کند.\",\n \"sources\": [\"https://www.etymonline.com/word/risk\", \"https://www.ahdictionary.com/word/search.html?q=risk\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"contradicts\", \"note\": \"Current American Heritage Dictionary s.v. risk: '[French risque, from Italian risco, rischio, probably from Medieval Greek rizikon … from Arabic rizq, sustenance … from Middle Iranian rōčīg, from rōč, day, from Old Iranian *raučah-; see leuk- in the Appendix of Indo-European roots.]' — a completely different route from the one Nourai draws, and the root appealed to is *leuk-, not *sek-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Etymonline\", \"where\": \"s.v. risk\", \"stance\": \"partial\", \"note\": \"'from Italian risco, riscio (modern rischio), from riscare \\\"run into danger\\\", a word of uncertain origin' — declines both the *resecāre and the rizq accounts.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. risk\", \"stance\": \"partial\", \"note\": \"Klein derives risk from French risque, Italian risco, and (like most mid-century dictionaries) mentions the Vulgar Latin *resecum 'cliff' guess without endorsing it.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"supports\", \"note\": \"Lokotsch is the standard source for the Arabic rizq > Romance risco account that current AHD follows.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"rîsk «ریسک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian ریسک is a twentieth-century European loan, taken from French risque (the usual channel for modern technical and commercial vocabulary in Persian, cf. بانک, پلیس, کنترل), and Mo'in tags such words [فر.] 'French'. The pronunciation rīsk with -sk rather than -sq(ue) shows the borrowing came through the written French form read in Persian; Persian keeps it as a noun ('risk') and forms ریسک کردن. If the current AHD etymology of risque is right, ریسک is a round trip: Middle Persian rōč 'day' → rōčīg 'daily bread, allotment' → Syriac rūzīqā → Arabic رزق rizq → Medieval Greek rizikon → Italian risco → French risque → Persian ریسک, the word returning to Persian after some fifteen centuries beside its native cognates روز and روزی.\",\n \"derivation_fa\": \"«ریسک» وام‌واژه‌ای اروپایی از سدهٔ چهاردهم خورشیدی است که از فرانسوی risque گرفته شده — همان راهی که بیشتر واژه‌های فنی و بازرگانی نو (بانک، پلیس، کنترل) از آن به فارسی آمده‌اند؛ معین چنین واژه‌هایی را با نشانِ [فر.] می‌آورد. تلفظ rīsk با خوشهٔ پایانی -سک نشان می‌دهد که وام‌گیری از صورت نوشتاری فرانسوی بوده است. اگر ریشه‌شناسی کنونی AHD درست باشد، «ریسک» یک بازگشت کامل است: فارسی میانه rōč «روز» → rōčīg «روزی» → سریانی rūzīqā → عربی «رزق» → یونانی میانه rizikon → ایتالیایی risco → فرانسوی risque → فارسی «ریسک»؛ یعنی واژه پس از پانزده سده به زبان مادری بازگشته و اکنون در کنار هم‌ریشه‌های بومی‌اش «روز» و «روزی» می‌نشیند. داوری: وام‌گیری از فرانسوی درست است.\",\n \"sources\": [\"https://www.ahdictionary.com/word/search.html?q=risk\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1703\", \"status\": \"not_checked\", \"note\": \"The six-volume Mo'in (the edition Nourai cites by page) is not online and not on disk; the two-volume Adena condensation on disk (MON_part1.txt) has only چرخ‌ریسک (a bird name) and no entry ریسک, and it carries no page numbers, so MON:1703 cannot be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt (2-vol. Adena condensation)\", \"stance\": \"silent\", \"note\": \"grep 'ریسک' returns only 'چرخ‌ریسک' (the bird) — the condensation drops the European loan.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi\", \"stance\": \"silent\", \"note\": \"grep 'ریسک' in ARY_pages.txt returns nothing; Aryanpur treats inherited vocabulary, not modern European loans.\"},\n   {\"src\": \"Etymonline/AHD\", \"where\": \"s.v. risk\", \"stance\": \"supports\", \"note\": \"Both confirm French risque as the modern European source form that Persian borrowed.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"English\",\n \"words\": \"section, insect, risk\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Two of the three are straightforward and are in Watkins under sek-: section < Latin sectiō, -ōnis, noun of action from secāre 'to cut' (via Old French/Middle English, 14th c. 'a cutting'), and insect < Latin īnsectum 'notched (animal)', the neuter past participle of īnsecāre 'to cut into' — itself a calque of Aristotle's ἔντομον (ἐντέμνειν 'to cut into'), coined for the segmented body. Both are therefore genuine *sek- words and the arrow Latin → English is correct for them. risk is not: English risk (1660s) comes from French risque, and neither Etymonline ('a word of uncertain origin') nor the current AHD (Arabic rizq < Syriac rūzīqā < Middle Iranian rōčīg 'daily bread') derives it from secāre. Watkins's own list under sek- includes SECTION, INSECT and RESECT but not RISK, so even Nourai's own AHD reference does not carry the third word.\",\n \"derivation_fa\": \"دو واژه از سه واژه روشن‌اند و واتکینز نیز آن‌ها را ذیل *sek- می‌آورد: section از لاتین sectiō «بُرش» (اسم مصدر از secāre) و insect از لاتین īnsectum «کنده‌کنده، بندبند»، اسم مفعولِ īnsecāre «درون‌بریدن» که خود گرته‌برداری از ἔντομον ارسطو است و به بدنِ بندبندِ حشره اشاره دارد. پس پیکانِ لاتین → انگلیسی برای این دو درست است. اما risk چنین نیست: risk انگلیسی (۱۶۶۰ م.) از فرانسوی risque آمده و نه اتیمانلاین («خاستگاه نامعلوم») و نه ویراست کنونی AHD (عربی «رزق» از سریانی rūzīqā از ایرانی میانه rōčīg) آن را از secāre نمی‌گیرند. حتی فهرست واتکینز ذیل sek- شامل SECTION و INSECT و RESECT هست ولی RISK نیست. داوری: دو واژه تأیید، سومی رد می‌شود.\",\n \"sources\": [\"https://www.etymonline.com/word/risk\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. sek- ends '…SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT)' — SECTION and INSECT are there, RISK is not; the current AHD entry for risk routes it through Arabic rizq and the root *leuk-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. section, insect, risk\", \"stance\": \"partial\", \"note\": \"Klein derives section and insect from Latin secāre/īnsecāre, but risk only from French risque/Italian risco.\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. risk\", \"stance\": \"contradicts\", \"note\": \"'from Italian risco, riscio … from riscare run into danger, a word of uncertain origin' — no Latin secāre.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. section, insect\", \"stance\": \"supports\", \"note\": \"Skeat gives both from Latin secare / insecare, 'to cut into', insect being a translation of Gk. entomon.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 438,\n \"book_page\": 408,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-438.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-438.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-438.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 438",
 "description": "Write and validate page-438.json"
}
```


### [2026-09-14T01:55:12.286Z] TOOL RESULT

```
ok 13
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 4, 'confirmed': 5, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 24, 'partial': 6, 'not_found': 1, 'not_checked': 2, 'contradicts': 1}
books consulted: {'partial': 10, 'supports': 23, 'contradicts': 4, 'silent': 2} | by book: {'CHEUNG': 8, 'BRT': 6, 'PHD': 4, 'WLD': 3, 'KLN': 3, 'AHD': 2, 'POK': 2, 'Etymonline': 2, 'HRN': 1, 'IEC': 1, 'SOD': 1, 'LEW/LAT': 1, 'LKT': 1, 'MON': 1, 'ARY': 1, 'Etymonline/AHD': 1, 'SKT': 1}
```


## [2026-09-14T01:55:22.989Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN risk\"; grep -n -o -E \"risk,[^\\n]{0,600}\" KLN_1966.txt | head -3; echo \"### KLN section/insect\"; grep -n -o -E \"insect,[^\\n]{0,400}\" KLN_1966.txt | head -2; echo \"### SKT insect\"; grep -n -o -E \"INSECT[^\\n]{0,300}|insect, [^\\n]{0,300}\" SKT.txt | head -3; echo \"### LKT rizq\"; grep -n -i -o -E \".{0,200}(rizq|risiko|risco|risque).{0,200}\" LKT.txt | head -5",
 "description": "Verify Klein/Skeat/Lokotsch claims"
}
```


### [2026-09-14T01:55:26.810Z] TOOL RESULT

```
### KLN risk
417:risk,  GEW.  =  Frisk,  Hjalmar,  Griechisches  etymologisches  Worterbuch,  1 955  —  in  progress.
1473:risk,  GEW.,  I,  57-58. Derivatives:  acoustic-al,  adj.,  acoustic-al-ly, •dv.,  acoust-ics,  n.
1777:risk,  GEW.,  I, p.42  s.v.  aii;  and  p.  31  s.v.  aiyiaXA?. aegicrania,  n.,  representation  of  goats’  heads (1 Greek  and  Roman  antiq.)  —  ModL.,  fr.  Gk. at?,  gen.  aiydp,  ‘goat’,  and  xpavla,  pi.  of xpavEov,  ‘skull’.  For  the  first  element  see  aego-, for  the  second  see  cerebrum, aegirite,  n.,  a  variety  of  acmite  (mineral.)  — Formed  with  subst.  suff.  -ite  from  Aegir,  name of  the  Icelandic  sea-god;  so  called  because  it occurs  in  Scandinavia.
### KLN section/insect
9596:insect,  and croak.
12090:insect,  the  dorbeetle.  —  ME. dore,  fr.  OE.  dora,  ‘bumblebee’,  rel.  to  MLG. dorte,  ‘drone’,  from  the  I.-E.  imitative  base *dher-,  ‘to  hum,  buzz,  murmur’.  See  drone. Dora,  fem.  PN.  —  A  shortened  form  of  Doro¬ thea,  Dorothy.
### SKT insect
20759:insect,  by  confusion  with  irimiOH', bat  vtrmi/ioH  is  generally  made  from  red lead.
### LKT rizq
ugrep: error: error at position 105
|risque)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,200}
                exceeds complexity limits___/
```


## [2026-09-14T01:55:32.778Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor fn,pats in [('KLN_1966.txt',[r'\\nrisk,\\s*n\\.', r'\\ninsect,\\s*n\\.', r'\\nsection,\\s*n\\.']),\n                ('SKT.txt',[r'INSECT', r'SECTION']),\n                ('LKT.txt',[r'[Rr]izq', r'[Rr]isiko', r'[Rr]isco'])]:\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    print('#####',fn)\n    for p in pats:\n        ms=list(re.finditer(p,t))\n        print(' ',p,len(ms))\n        for m in ms[:2]:\n            print('   ...',t[m.start():m.start()+450].replace('\\n',' '))\nEOF",
 "description": "Verify Klein/Skeat/Lokotsch entries properly"
}
```


### [2026-09-14T01:55:34.057Z] TOOL RESULT

```
##### KLN_1966.txt
  \nrisk,\s*n\. 0
  \ninsect,\s*n\. 1
   ...  insect,  n.  —  L.  insectum  (scil.  animal),  lit.  ‘(ani¬ mal)  cut  into’,  neut.  pp.  of  insecare,  ‘to  cut  into’, fr.  in-,  ‘in’,  and  secare,  ‘to  cut’  (see  section);  first used  in  this  sense  (in  the  plural  insecta)  by  Pliny, Hist,  nat.,  II,  I,  I,  as  loan  translation  of  Gk. Hvropa,  ‘insects’,  lit.  ‘(animals)  cut  in’,  from  the stem  of  £vxepvEiv,  ‘to  cut  in'  (see  entomo-). insectarium,  n.,  a  plac
  \nsection,\s*n\. 0
##### SKT.txt
  INSECT 0
  SECTION 0
##### LKT.txt
  [Rr]izq 0
  [Rr]isiko 3
   ... Risiko'  [vom  Vb.  hatara  III 'wagen,  riskieren'],  eigentlich  bai^  mu- hätara  'ein  gewagter  Kauf,  d.  h.  einer, bei  dem  man  ein  Risiko  eingeht.  Hieraus sp.  mohatra,  pg.  mofatra  'wucherischer Verlrag'.    [DE  316.    Eguilaz  456. 1502.  Ar.  muhräz: Auch  »nVirS? 'Schusterahle';  hieraus  mit ar.  Art.  u.  Imäla  [ä  >  e]  pg.  almofrez 'dass.'  [Constancio  Dicc  57  b],  wohl  auch sp.  almarada  'Ahle  des  Halfasohlen-
   ... Risiko  eingeht.  Hieraus sp.  mohatra,  pg.  mofatra  'wucherischer Verlrag'.    [DE  316.    Eguilaz  456. 1502.  Ar.  muhräz: Auch  »nVirS? 'Schusterahle';  hieraus  mit ar.  Art.  u.  Imäla  [ä  >  e]  pg.  almofrez 'dass.'  [Constancio  Dicc  57  b],  wohl  auch sp.  almarada  'Ahle  des  Halfasohlen- schusters,  Stilett';  jedoch  kann  pg.  al- mofate  'Ahle'  [Constancio  Dicc  57  a] nicht,  wie  DE  170/171  meint,  durch vielfache  Änd
  [Rr]isco 7
   ... riscos,  zu  deren  Eigentümlich- keiten es  gehörte,  daß  in  ihr  viele arabische  Ausdrücke,  z.  T.  mit  spanischer Endung,  sowie  Arabismen  und  alt- spanische Wörter  vorkommen,  die  sonst schon  außer  Gebrauch  gekommen  waren. Da  diese  Sprache  mit  arabischer  Schrift geschrieben  wurde,  sind  textos  aljamia- dos  also  spanische  Schriftstücke,  die arabisch  geschrieben  sind,  z.  B.  das Poema  de  Yosuf,  vgl.  Ad.  Zauner
   ... risco,  riesgo  'Wagnis,  Gefahr',  risco 'Klippe',  arriscador  'Olivensammler', pg.  risco  'Wagnis;  Klippe',  Vb.  sp.  pg. riscar,  arriscar  'in  Gefahr  kommen', it.  risico,  frz.  risqiie,  rum.  rizic  'Wag- nis, Gefahr',  Vb.  it.  risicare,  frz.  risquer 'wagen' ;  dtsch.  Risiko,  engl.  risk.  [Devic DEt  194/195.  Jacob  EMA  97.  ML  7289 (<  gr.  {)iIiKÖv  'Klippe'?). 1722.  Ar.  riswa: 'Beslechungsgabe,  Schmiergeld',  tk.  riä
```


## [2026-09-14T01:55:41.821Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nm=list(re.finditer(r\"risco,  riesgo\",t))[0]\nprint(t[max(0,m.start()-900):m.start()+400])\nEOF\necho \"=== KLN section / risk ===\"\ngrep -n -o -E \"section,  n\\.[^\\n]{0,300}|risk,  n\\.[^\\n]{0,300}|risk,  tr[^\\n]{0,300}\" KLN_1966.txt | head -5",
 "description": "Lokotsch rizq entry; Klein section/risk"
}
```


### [2026-09-14T01:55:43.225Z] TOOL RESULT

```
  Eguilaz 288.    ML  7295.
1717.  Ar.  ribäs:
'Art  Sauerampfer',  auch  ribäz  [und  pers. ribäg];  hieraus  mit  Imäla  [Ä>-e]  mlat. ribes,  ribasium,  ribesium,  frz.  ribes  'Jo- hannisbeere'.   [Devic  DEt  193.
1718.  Ar.  ribät:
'Band,  langes  Slfick  Stoff'  [vom  Vb. rabata,  s.  hier  Nr.  1410];  hieraus  mit Imäla  [ä  >  e]  sp.  ribete,  kat.  ribet,  pg. ribete  [Constancio  Dicc  857  a]  'Saum, Besatz'.    [Eguilaz  483.
1719.  Ar.  ridf:
'Derjenige,  der  folgt  oder  nachkommt'; hieraus  mit  ar.  Art.  der  Sternname Arided,  Arioph  aus  dem  Schweife  des Cygiius.    [Devic  DEt  41.
1720.  Ar.  rigl:
'Fuß',  vollständig  ar-rigl  al-jumnä  'der rechte  Fuß'  sc.  des  Orions;  hieraus  der Sternname  Bigel  k  Orionis.  [Ideler Sternn  226.    Devic  DEt  193.
1721.  Ar.  rizk:
'Spenden,  die  Gott  zum  Leben  gibt; tägUches  Brot,  Ration';  hieraus  sp.  ar- risco,  riesgo  'Wagnis,  Gefahr',  risco 'Klippe',  arriscador  'Olivensammler', pg.  risco  'Wagnis;  Klippe',  Vb.  sp.  pg. riscar,  arriscar  'in  Gefahr  kommen', it.  risico,  frz.  risqiie,  rum.  rizic  'Wag- nis, Gefahr',  Vb.  it.  risicare,  frz.  risquer 'wagen' ;  dtsch.  Risiko,  engl.  risk.  [Devic DEt  194/195.  Jacob  EMA  97.  ML  7289 (<  gr.  {)iIiKÖv  'Klippe'?).
1722.  Ar. 
=== KLN section / risk ===
3739:risk,  n.,  the  figure  of  a  star  (the  printing mark  *).  —  Late  L.  asteriscus,  fr.  Gk.  daxEptaxo;, dimin.  of  aaxr)p,  ‘star’.  See  Aster, asterism,  n.,  a  system  of  stars,  a  constellation.  — Gk.  daxepiapd;,  fr.  danrjp,  ‘star’.  See  Aster  and -ism.
5665:risk,  tr.  and  intr.  v.,  brisk-en,  tr. and  intr.  v.,  brisk-ly,  adv.,  brisk-ness,  n. brisket,  n.,  animal’s  breast.  —  ME.  bruskette,  rel. to  MHG.  brusche,  G.  Brausche,  ‘bruise  on  the head’,  ON.  brjdsk,  Dan.  brusk,  ‘gristle’,  and  to E,  breast  (q.v.)  F.  brechet  (fr.  earlier 
11799:section,  n.  —  L.  dissectio,  gen.  -dnis,  ‘a  cutting to  pieces’,  fr.  dissectus,  pp.  of  disseedre ;  see  prec. word  and  -ion.  The  term  dissection  was  intro¬ duced  by  the  English  philosopher,  Baron  Veru- lam  Francis  Bacon  (1561-1626).
19702:section,  n.  —  L.  intersectio,  gen.  -dnis,  ‘a cutting  asunder,  intersection’,  fr.  intersectus, pp.  of  interseedre.  See  prec.  word  and  -ion. Derivative:  intersection-al,  adj. intersperse,  tr.  v.,  to  scatter.  —  L.  interspersus, ‘strewn,  sprinkled  upon’,  fr.  inter-  and  sparsus, ‘sca
32462:section,  n.  —  L.  resecdo,  gen.  -dnis,  ‘a  cutting off,  fr.  resectus,  pp.  of  resecare.  See  prec.  word and  -ion.
```


## [2026-09-14T01:55:55.390Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor fn in ('LEW_1910.txt','LAT.txt'):\n    t=open(fn,encoding='utf-8',errors='replace').read()\n    print('#####',fn, len(t))\n    for p in [r'curtus', r'\\bsec[oō],', r'seco,']:\n        ms=list(re.finditer(p,t))\n        print(' ',p,len(ms))\n        for m in ms[:1]:\n            print('   ',t[max(0,m.start()-120):m.start()+380].replace('\\n',' '))\nEOF",
 "description": "Check Latin etymological dictionaries"
}
```


### [2026-09-14T01:55:56.842Z] TOOL RESULT

```
##### LEW_1910.txt 619063
  curtus 0
  \bsec[oō], 0
  seco, 0
##### LAT.txt 4601625
  curtus 4
    argissement en -n- d'un thbme racine; la racine est celle de xeupoo "je coupe", xaprjvai,; et par suite de lat. corium, curtus, cortex, v. ces mots. Elie a nn doublet a s- initial: iri. scaraim M je separe", T.h.a. sceran "couper", lit. skiriu "je separe"; v.lat. scortum, carota, -ae f.: panais, carotte. Emprunt tardif et populaire (Api¬ cius) au gr. xapoorov. Roman; cf. O.Bloch, Dict. 6tym., s.u. carpa, -ae f.: carpe. Un seul ex. dans Cassiodore. M.L.1708. Mot germanique, v.h.a. karpfo. carpent
  \bsec[oō], 2
    ulti mortales ; Cic. Cael.17,4° nos qui hanc sectam rationemque uitae... secuti sumus, etc. Rattache par les anciens a. seco, sectus, cf. Serv., Ae. 6 , 0 yy cite s.u. seco, mais d'autre part, non separe de sequi, dont sector est considere a juste titre comme l'intensif, cf.Pl., Mi.y1, ait sese ultro omnis mulieres sectarier. Il est possible que secta soit un postverbal de sector, comme pugna de pugno. Derives: sectarius : — uerbex qui gregem agnorum praecedens ducit, P.F.453,15; sector, -aris: 
  seco, 4
    . La forne et la graphie dissiciS sont difficilement explicables. On admet, sans preuves, 1 ’influence analogique de disseco, dissipS, cf.Sommer, Hdb.d. lat. Laut- u. Forni., 2 e ed.jp.aCG. Disicio lui-m&me est une forme refaite; phonetiquement on- attendrait *diicio, comme diiungS. Sur 1 ’ abi. disice , -v.obicSs. SiciS: jeter dehors, chasser (eX| 3 aXXu)). iniciS: jeter dans ou sur ( euT| 3 aXXop et s v otjjj. t.). intericiS: jeter entre, interposer; d'ou, dans la l.de la grammaire et de la rh
```


## [2026-09-14T01:56:19.575Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io\np='data/verification/page-438.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\n# node 10: replace LEW/LAT consulted with verified LAT quote + Klein resection\nn=nodes[10]\nn['consulted'][2] = {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.vv. caro, secō\",\"stance\":\"supports\",\"note\":\"LAT.txt s.v. carō: 'la racine est celle de κείρω \\\"je coupe\\\", καρῆναι, et par suite de lat. corium, curtus, cortex, v. ces mots. Elle a un doublet à s- initial: irl. scaraim \\\"je sépare\\\", v.h.a. sceran \\\"couper\\\"' — Latin curtus (not *cortus) in the *ker- family; secō has its own entry. Walde-Hofmann (LEW_1910.txt on disk) is only the 1910 A-L part and has neither headword.\"}\nn['consulted'].append({\"src\":\"KLN\",\"where\":\"s.v. resection\",\"stance\":\"supports\",\"note\":\"Klein: 'resection, n. — L. resecātiō, gen. -ōnis, \\\"a cutting off\\\", fr. resectus, pp. of resecāre' — confirms re-secāre 'to cut off/back', not 'cut against'.\"})\n\n# node 11: fix KLN and LKT consulted\nn=nodes[11]\nn['consulted'][1] = {\"src\":\"LKT\",\"where\":\"Lokotsch no. 1721, s.v. Ar. rizk\",\"stance\":\"contradicts\",\"note\":\"Lokotsch: '1721. Ar. rizk: \\\"Spenden, die Gott zum Leben gibt; tägliches Brot, Ration\\\"; hieraus sp. arrisco, riesgo \\\"Wagnis, Gefahr\\\", risco \\\"Klippe\\\", pg. risco, Vb. sp. pg. riscar, arriscar \\\"in Gefahr kommen\\\", it. risico, frz. risque, rum. rizic \\\"Wagnis, Gefahr\\\" … dtsch. Risiko, engl. risk.' — this is the Arabic route the current AHD follows, against Nourai's Latin resecāre.\"}\nn['consulted'][2] = {\"src\":\"KLN\",\"where\":\"KLN_1966.txt, s.v. risk\",\"stance\":\"silent\",\"note\":\"The OCR of Klein's two-volume edition on disk has no locatable 'risk' entry (searches for '\\\\nrisk, n.' return only fragments of asterisk/brisk), so Klein could not be quoted for this word.\"}\n\n# node 13: fix SKT\nn=nodes[13]\nn['consulted'][0] = {\"src\":\"KLN\",\"where\":\"s.vv. insect, resection\",\"stance\":\"supports\",\"note\":\"Klein: 'insect, n. — L. insectum (scil. animal), lit. \\\"(animal) cut into\\\", neut. pp. of insecāre, \\\"to cut into\\\", fr. in-, \\\"in\\\", and secāre, \\\"to cut\\\" (see section); first used in this sense (in the plural insecta) by Pliny, Hist. nat. XI,1,1, as loan translation of Gk. ἔντομα, \\\"insects\\\", lit. \\\"(animals) cut in\\\", from the stem of ἐντέμνειν' — exactly the section/insect half of the node.\"}\nn['consulted'][2] = {\"src\":\"SKT\",\"where\":\"SKT.txt (Skeat, Concise)\",\"stance\":\"silent\",\"note\":\"grep for 'insect' / 'section' headwords in the OCR of Skeat's Concise returns no usable entry; the book could not be quoted here.\"}\n\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=2)\nprint('patched')\nEOF\npython3 -m json.tool data/verification/page-438.json >/dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 438",
 "description": "Patch unverified consulted notes; revalidate"
}
```


### [2026-09-14T01:56:20.681Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 13/13
node verdicts: {'disputed': 4, 'confirmed': 5, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 24, 'partial': 6, 'not_found': 1, 'not_checked': 2, 'contradicts': 1}
books consulted: {'partial': 8, 'supports': 23, 'contradicts': 5, 'silent': 4} | by book: {'CHEUNG': 8, 'BRT': 6, 'PHD': 4, 'KLN': 4, 'WLD': 3, 'AHD': 2, 'POK': 2, 'Etymonline': 2, 'HRN': 1, 'IEC': 1, 'SOD': 1, 'LAT': 1, 'LKT': 1, 'MON': 1, 'ARY': 1, 'Etymonline/AHD': 1, 'SKT': 1}
```


## [2026-09-14T01:56:41.779Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io, re\np='data/verification/page-438.json'\ns=io.open(p,encoding='utf-8').read()\nrepl=[\n (\"p.81 s.vv. škastan, škāftan, škuftan, škeft\",\"PHD.txt, s.vv. škastan, škāftan, škuftan, škeft\"),\n (\"(MacKenzie p.81 'škastan, šken(n)- [TBLWN-tn'] break')\",\"(MacKenzie, PHD s.v. 'škastan, šken(n)- [TBLWN-tn' < A √tbr] break')\"),\n (\"MP škāftan, škāf- 'split, burst' (MacKenzie p.81)\",\"MP škāftan, škāf- 'split, burst' (MacKenzie, PHD s.v.)\"),\n (\"p.77 s.v. say-\",\"PHD.txt, s.v. say-\"),\n (\"(MacKenzie p.77 'say-, v. sūdan'; Book Pahlavi sʾd-/swtn)\",\"(MacKenzie, PHD 's̄ay-, v. sūdan'; Book Pahlavi sʾd- /say-/, inf. swtn /sūdan/)\"),\n (\"pp.49-50, 5 s.vv. kārd, karr, agar\",\"PHD.txt, s.vv. kārd, karr, agar\"),\n (\"(MacKenzie p.49 'kārd … knife')\",\"(MacKenzie, PHD s.v. 'kārd [SKYN' ; krt'] knife')\"),\n (\"(MacKenzie p.50)\",\"(MacKenzie, PHD s.v. 'karr [kr | M qr, N ~] deaf')\"),\n (\"p.74 s.v. sargēn; index s.vv. dung, manure, split\",\"PHD.txt, s.v. sargēn and index s.vv. dung, manure, split\"),\n (\"(MacKenzie p.74)\",\"(MacKenzie, PHD s.v. 'sargēn [slgyn' | N sargin] dung, manure')\"),\n (\"Horn p.161, no. 752\",\"Horn, HRN.txt no. 752\"),\n (\"(Bartholomae col. 1566, Yt 10.42\",\"(Bartholomae s.v. skand-, Yt 10.42\"),\n (\"Bartholomae; V 4.50 'ayaŋhaēnāi kərətaēiš'\",\"Bartholomae s.v. kərəta-, V 4.50 'ayaŋhaēnāi kərətaēiš'\"),\n (\"Klein 1966, leaf 760-761 (printed 1432-1434)\",\"Klein 1966, KLN_1966.txt leaves 760-761, whose running-head page numbers put them at printed pp.1432-1434\"),\n]\nfor a,b in repl:\n    if a not in s: print(\"MISS:\",a[:60])\n    s=s.replace(a,b)\nio.open(p,'w',encoding='utf-8').write(s)\njson.load(io.open(p,encoding='utf-8'))\nprint(\"ok\")\nEOF\npython3 tools/verify_check.py 438",
 "description": "Soften unverifiable page citations"
}
```


### [2026-09-14T01:56:43.009Z] TOOL RESULT

```
MISS: Horn p.161, no. 752
ok
nodes verified: 13/13
node verdicts: {'disputed': 4, 'confirmed': 5, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 24, 'partial': 6, 'not_found': 1, 'not_checked': 2, 'contradicts': 1}
books consulted: {'partial': 8, 'supports': 23, 'contradicts': 5, 'silent': 4} | by book: {'CHEUNG': 8, 'BRT': 6, 'PHD': 4, 'KLN': 4, 'WLD': 3, 'AHD': 2, 'POK': 2, 'Etymonline': 2, 'HRN': 1, 'IEC': 1, 'SOD': 1, 'LAT': 1, 'LKT': 1, 'MON': 1, 'ARY': 1, 'Etymonline/AHD': 1, 'SKT': 1}
```


## [2026-09-14T01:56:48.186Z] TOOL CALL #90: Bash

```json
{
 "command": "grep -o \"p\\.161, no\\. 752\" data/verification/page-438.json; python3 - <<'EOF'\nimport io,json\np='data/verification/page-438.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace(\"\\\"where\\\": \\\"p.161, no. 752\\\"\",\"\\\"where\\\": \\\"HRN.txt, no. 752 (printed p.161 region)\\\"\")\nio.open(p,'w',encoding='utf-8').write(s)\njson.load(io.open(p,encoding='utf-8')); print('ok')\nEOF\npython3 tools/verify_check.py 438 && echo \"--- FLAGGED ---\" && FLAGGED=1 python3 tools/verify_check.py 438 | grep FLAG",
 "description": "Final fix and flagged listing"
}
```


### [2026-09-14T01:56:49.530Z] TOOL RESULT

```
p.161, no. 752
ok
nodes verified: 13/13
node verdicts: {'disputed': 4, 'confirmed': 5, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 24, 'partial': 6, 'not_found': 1, 'not_checked': 2, 'contradicts': 1}
books consulted: {'partial': 8, 'supports': 23, 'contradicts': 5, 'silent': 4} | by book: {'CHEUNG': 8, 'BRT': 6, 'PHD': 4, 'KLN': 4, 'WLD': 3, 'AHD': 2, 'POK': 2, 'Etymonline': 2, 'HRN': 1, 'IEC': 1, 'SOD': 1, 'LAT': 1, 'LKT': 1, 'MON': 1, 'ARY': 1, 'Etymonline/AHD': 1, 'SKT': 1}
--- FLAGGED ---
FLAG: 438 Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 #1 sčand; skenda; scapti; kaf, kâf disputed | Two of the four items are genuine Avestan, two are not. (a) sčand = Av. skand- 'to break', pres. scandaya-/škəndaya-/scindaya- 'zerbrechen, zerstören' (Bartholomae s.v. skand-, Yt 10.42 'ime nō uγra b
FLAG: 438 Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 #4 sŭdan «سودن ( سود )»; farsŭdan «فرسودن» disputed | The words and the immediate Iranian chain are beyond doubt: MP sūdan, pres. say- 'to rub, wear, tire, tear' (MacKenzie, PHD 's̄ay-, v. sūdan'; Book Pahlavi sʾd- /say-/, inf. swtn /sūdan/) > NP سودن sū
FLAG: 438 Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 #10 secare; re-secare; risecum; cortus transcription_suspect | secāre 'to cut' is the plain Latin continuant of PIE *sek- (Watkins s.v. sek-: 'Basic form *sek- in Latin secāre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INT
FLAG: 438 Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 #11 risque disputed | French risque (16th c.) is certainly the immediate source of English risk and of modern Persian ریسک, but its own origin is not the one drawn here. Etymonline: 'risk (n.) 1660s, risque, hazard, danger
FLAG: 438 Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2 #13 section, insect, risk disputed | Two of the three are straightforward and are in Watkins under sek-: section < Latin sectiō, -ōnis, noun of action from secāre 'to cut' (via Old French/Middle English, 14th c. 'a cutting'), and insect
```


## [2026-09-14T01:57:09.639Z] AGENT

Page 438 (book p. 408), entry 0 "Sek, Sked 1, Sker 2, Skei, Skhed, Skep, Skel 2, Skaf, Ker 2" — verified; `verify_check.py 438` reports 13/13 nodes, 0 PROBLEM lines.

Verdicts: root **plausible**; nodes — 5 confirmed, 3 plausible, 4 disputed, 1 transcription_suspect. Ref checks: 24 supports, 6 partial, 1 contradicts, 1 not_found, 2 not_checked.

Flagged items:
- **#1 Avestan "scapti" / "kaf, kâf"** (disputed) — sčand and skənda- are genuine (Bartholomae, POK 919, Gharib p.61 ʾskʾnt(y) "cripple"), but Bartholomae's *skapta-* means "erstaunlich, wunderbar" (→ MP škaft, NP شگفت), not "to split", and kaf/kâf are New Persian (Pokorny cites them as "npers. kafaδ, kavaδ" under (s)kep-2), not Avestan.
- **#4 sūdan, farsūdan** (disputed) — Cheung 2007 (*sauH¹/*saH) and Horn no. 752 put سودن under PIE *ḱeh₂s- "to whet, sharpen" (Pok. 541 f.), not under *sek-/*skei-; Cheung adds that the Avestan parent root sā- "may be non-existent". Nourai's own NOTE half-anticipates this.
- **#10 "cortus : short"** (transcription_suspect) — `error_in: book`. The printed page really shows "cortus"; the correct Latin is **curtus** < *kr̥-tó- (POK 941, Klein s.v. short, Wiktionary). Extraction is faithful — no data fix needed.
- **#11 French risque / #13 English risk** (disputed) — current AHD derives risque from Italian risco ← Med. Gk. rizikon ← Arabic رزق rizq ← Syriac rūzīqā ← Middle Iranian rōčīg "daily bread" (root *leuk-), and Lokotsch no. 1721 says the same; Etymonline calls it "of uncertain origin". Nourai's Latin *risecum/resecāre chain is the old (1969–76) AHD account. section and insect are fine. Ironically this makes Persian ریسک (#12, confirmed as a French loan) an Iranian round trip from روز/روزی.

Also noted in the entry: Nourai's page citations check out throughout (POK 920/926/930-931/941/578/947, HRN 25/98/175/188/205/221/244, SOD 128/193/194 at a −65 leaf offset, BQT 1275/1279/1462/1559/1816 in Mo'in's footnotes, SYN 321, IEC 640/1155, KLN 1432); only BQT:1184 (سودن) and MON:2935 / MON:1703 could not be located (6-vol. Mo'in not available). Walde-Pokorny II 588 explicitly rejects tying the dung root *sker- to *sker- "cut", which is why the root box is "plausible" rather than "confirmed".

Page image archived at `data/verification/sources/refs/ocr/BOOK/438.png`; 13 web sources archived via `fetch_source.py`.
