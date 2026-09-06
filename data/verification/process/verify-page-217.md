# Verification process log — verify-page-217


## [2026-09-06T15:07:16.735Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 217 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-217.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-217.json. Write /home/sfmqrb/git/rishe/data/verification/page-217.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 217` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:07:18.239Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:07:19.039Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:07:19.052Z] TOOL RESULT

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


## [2026-09-06T15:07:19.196Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-217.txt"
}
```


### [2026-09-06T15:07:19.207Z] TOOL RESULT

```
1	=== PDF page 217 (book page 187) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwou : cow, ox, bull  (refs KLN:364; POK:483)
4	#1 (parent #0) [Avestan] refs=KLN:364 | gâuš, gave, ga 3, gâvô, gavâm, gao : cow, domestic animal
5	  #2 (parent #1) [Persian] refs=SYN:202; BQT:1856; HRN:210; MON:3430 | gâv «گاو» : cow ; gŭ-pân «گوپان» : one who looks after cows ☞Pa ; gŭ-sâleh «گوساله» : calf ☞Kel 1 ; gŭšt «گوشت» : meat
6	  #3 (parent #1) [Avestan] refs=BQT:1855; POK:237 | gao-spenta : holy farm animal, sheep ☞Kwen ; gao-di, gao-dana : milk container
7	    #4 (parent #3) [Persian] refs=HRN:210 | gŭspand, gôsfand «گوسپند،گوسفند» : sheep
8	#5 (parent #0) [Sanskrit] refs=POK:482 | gâuh : cow ; gô-pâ-h, gôpâ : shepherd, protector ☞Pa
9	  #6 (parent #5) [Avestan / Sanskrit] refs=HRN:237 | gôp, gôh : to protect, preserve | NOTE: See HRN:237 notes for discussion
10	    #7 (parent #6) [Avestan] refs=HRN:237 | ni-gôp : to hide, protect ☞Nf 1
11	      #8 (parent #7) [Pahlavi] refs=SNS:262 | nihuftan : to hide | NOTE: FFD:80 derives this word from Old Persian "ni-thuf-ta: hide".
12	        #9 (parent #8) [Persian] refs=MON:4870; HRN:236 | nehoftan «نهفتن» : to hide
13	#10 (parent #0) [Old Persian] refs=SOD:180 | gaithâ : herd
14	  #11 (parent #10) [Sogdian] refs=SOD:180 | gydh : herd
15	#12 (parent #0) [Germanic] refs=KLN; AHD; POK | koŭs : cow
16	  #13 (parent #12) [English] refs=None | cow
17	#14 (parent #0) [Latin] refs=AHD | bôs, bov- : cow
18	  #15 (parent #14) [English] refs=None | beef
19	#16 (parent #0) [Greek] refs=AHD | bous : cow
20	  #17 (parent #16) [English] refs=None | buffalo, butter
21	#18 (parent #0) [Indo-European] refs=AHD:1520; POK:483 | Gwôu : dung
22	  #19 (parent #18) [Avestan] refs=POK:484 | gutha : dung
23	    #20 (parent #19) [Persian] refs=BQT:1723,1863; HRN:211; SOG:57 | goh «گوه» : dung ; cŭd «کود» : fertilizer ; tŭdeh «توده» : pile, heap
24	--- entry 1 ---
25	ROOT Gwôu -> redirect to Gwou
26	--- entry 2 ---
27	ROOT Gwŭnâ -> redirect to Gwen 1
28	--- entry 3 ---
29	ROOT Gyeu -> redirect to Geu 3
30	
```


## [2026-09-06T15:07:23.700Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-217.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','POK','SYN','BQT','HRN','MON','SOD','AHD','SNS','FFD','SOG','WLD','BRT','PHD','NYB','HUB','IEC','ARY','CHEUNG','SKT','FSD','WEB','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T15:07:25.460Z] TOOL RESULT

```
{
  "pdf_page": 217,
  "book_page": 187,
  "entries": [
    {
      "root": {
        "name": "Gwou",
        "lang": "Indo-European",
        "refs": "KLN:364; POK:483",
        "gloss": "cow, ox, bull"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:364",
          "words": [
            {"translit": "gâuš, gave, ga 3, gâvô, gavâm, gao", "gloss": "cow, domestic animal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SYN:202; BQT:1856; HRN:210; MON:3430",
          "words": [
            {"translit": "gâv", "gloss": "cow", "script": "گاو"},
            {"translit": "gŭ-pân", "gloss": "one who looks after cows", "script": "گوپان", "see": ["Pa"]},
            {"translit": "gŭ-sâleh", "gloss": "calf", "script": "گوساله", "see": ["Kel 1"]},
            {"translit": "gŭšt", "gloss": "meat", "script": "گوشت"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "BQT:1855; POK:237",
          "words": [
            {"translit": "gao-spenta", "gloss": "holy farm animal, sheep", "script": null, "see": ["Kwen"]},
            {"translit": "gao-di, gao-dana", "gloss": "milk container", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "HRN:210",
          "words": [
            {"translit": "gŭspand, gôsfand", "gloss": "sheep", "script": "گوسپند،گوسفند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:482",
          "words": [
            {"translit": "gâuh", "gloss": "cow", "script": null},
            {"translit": "gô-pâ-h, gôpâ", "gloss": "shepherd, protector", "script": null, "see": ["Pa"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Avestan / Sanskrit",
          "refs": "HRN:237",
          "words": [
            {"translit": "gôp, gôh", "gloss": "to protect, preserve", "script": null}
          ],
          "script_extra": null,
          "note": "See HRN:237 notes for discussion",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Avestan",
          "refs": "HRN:237",
          "words": [
            {"translit": "ni-gôp", "gloss": "to hide, protect", "script": null, "see": ["Nf 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": "SNS:262",
          "words": [
            {"translit": "nihuftan", "gloss": "to hide", "script": null}
          ],
          "script_extra": null,
          "note": "FFD:80 derives this word from Old Persian \"ni-thuf-ta: hide\".",
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:4870; HRN:236",
          "words": [
            {"translit": "nehoftan", "gloss": "to hide", "script": "نهفتن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "آن شنیدی که شاهدی به نهفت - بادل از دست رفته ای میگفت", "poet": "Sa`dî"}
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SOD:180",
          "words": [
            {"translit": "gaithâ", "gloss": "herd", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Sogdian",
          "refs": "SOD:180",
          "words": [
            {"translit": "gydh", "gloss": "herd", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "KLN; AHD; POK",
          "words": [
            {"translit": "koŭs", "gloss": "cow", "script": null}
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
            {"translit": "cow", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "bôs, bov-", "gloss": "cow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "beef", "gloss": null, "script": null}
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
            {"translit": "bous", "gloss": "cow", "script": null}
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
            {"translit": "buffalo, butter", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "AHD:1520; POK:483",
          "words": [
            {"translit": "Gwôu", "gloss": "dung", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "Avestan",
          "refs": "POK:484",
          "words": [
            {"translit": "gutha", "gloss": "dung", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "Persian",
          "refs": "BQT:1723,1863; HRN:211; SOG:57",
          "words": [
            {"translit": "goh", "gloss": "dung", "script": "گوه"},
            {"translit": "cŭd", "gloss": "fertilizer", "script": "کود"},
            {"translit": "tŭdeh", "gloss": "pile, heap", "script": "توده"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Gwôu", "redirect": "Gwou"},
      "nodes": []
    },
    {
      "root": {"name": "Gwŭnâ", "redirect": "Gwen 1"},
      "nodes": []
    },
    {
      "root": {"name": "Gyeu", "redirect": "Geu 3"},
      "nodes": []
    }
  ]
}
=== refs_online keys ===
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
SOG {"title": "W. B. Henning, Sogdica (James G. Forlong Fund XXI), London 1940", "edition_found": "reprint in W. B. Henning Selected Papers II (Acta Iranica 15, 1977)", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
CHEUNG null
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-06T15:07:29.258Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo \"---\" && head -60 data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:07:29.308Z] TOOL RESULT

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
```


## [2026-09-06T15:07:35.531Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','SYN','HRN','BQT','SOD','SNS','BRT','KNT','PHD','NYB','HUB','IEC','SOG','MON','FFD','WLD']:\n    v=d.get(k) or {}\n    print('==',k, '| local:', v.get('local_file'), '| offset:', v.get('page_offset'), '| hint:', (v.get('lookup_hint') or '')[:300])\n\""
}
```


### [2026-09-06T15:07:37.569Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== SOD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== SNS | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SOG | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt | offset: Original pagination (1-67) is printed in the reprint margins; grep -n 'SOGDICA' to find the section (~leaves 158-340 of the scan). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Glossary section of Sogdica lists Sogdian words with NP cognates.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== FFD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
```


## [2026-09-06T15:07:41.511Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: g\" POK_full.txt | grep -i \"ou\\|ṷou\\|ou-\" | head -30\necho \"=== POK_full gʷou block ===\"\ngrep -n \"Page(s): 482\\|Page(s): 483\\|Page(s): 484\\|Page(s): 482-483\\|Page(s): 483-485\" POK_full.txt | head -20"
}
```


### [2026-09-06T15:07:41.584Z] TOOL RESULT

```
7815:ek"- : water, river, derived from zero grade of Root / lemma: ghag^h- : young of an animal 
10319:fish' = Root / lemma: g^er-l, g^era- : " to devour; throat ' + zero grade of Root / lemma: 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
18344:lemma: ghesor-1, ghesr-: hand'; Root/ lemma: ghesto-2\ "hand, arm' through lllyrian 
30181:lemma: gel-1\ "to curl; round' into gleg- + Root/ lemma: ok"-: "to see; eye'. 
32160:(: gl9t{h)-) and glet{h)- {\glt{h)-) of Root/ lemma: gel-1\ "to curl; round' [see above]. 
32732:Root / lemma: ghel-ou-, ghelu- 
33470:It is a compound of Root/ lemma: ghosti-s\ stranger; guest + Root/ lemma: poti-s: 
33501:Root / lemma: ghou-ro-s 
33523:Root / lemma: ghous- 
33551:Root / lemma: ghou(e)- 
34145:Root / lemma: ghroud- 
34354:Root / lemma: goua- (or gaua-1.) gu- 
34389:Root / lemma: gou- goua- gu- 
34979:Root/ lemma: gerrt^-, gn[t^-\ to bite; tooth ' : Root/ lemma: gep(h)-, ^eb^-: jaw, mouth' 
35517:Root/ lemma: gep(h)-, ^eb^-: jaw, mouth' : Root/ lemma: gerrid^-, gixt"^-: to bite; tooth' 
36027:Alb. shows that Root/ lemma: ghuen-: "to sound' derived from Root/ lemma: ghau-, 
36958:Albanian proves that Root / lemma: g''er-1, g''era-\^ to devour; throat ' derived from Root/ 
37133:Root / lemma: gheslo- : thousand' derived from Root / lemma: ghesor-1, ghesr- : "hand, 
37188:lemma: ghesor-1, ghesr-: hand'; Root/ lemma: ghesto-2\ "hand, arm' through lllyrian 
37257:lemma: gheu- : to pour + -tra suffix. 
38157:Alb. shows that Root/ lemma: ghuen-\ "to sound' derived from Root/ lemma: ghau-, 
39398:g^era-: to devour; throat; but from Root/ lemma: gher-5, ghor-na\ bowels, [common alb. 
39507:Root / lemma: g^er-l, g^ere-: " to devour; throat ' > Root/ lemma: b'^arH^a: " beard' 
39846:Root/ lemma: gh^ena^ woman, wife, *goddess' could be a truncated Root/ lemma: ghau- 
40435:Root / lemma: g^ou- 
40528:Root / lemma: g^ou- g^u- 
47601:geleb{h)-, gleb{h)- (: glab{h)-) and glet{h)- {:g/b{h)-) of Root/ lemma: ge/-1: "to curl; round, 
47729:Root/ lemma: knid-, Rnid-, sknid-: " louse, nit ' derived from Root/ lemma: gtien-: "to 
47905:lemma: gel-1\ 'to curl; round' [see above]. 
=== POK_full gʷou block ===
40403:Page(s): 482 
40422:Page(s): 482 
40433:Page(s): 482 
40526:Page(s): 482-483 
40606:Page(s): 483-485
```


## [2026-09-06T15:07:43.967Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40420,40700p' POK_full.txt"
}
```


### [2026-09-06T15:07:44.020Z] TOOL RESULT

```
References: M. Leumann, Homer. Worter 141 f. 
Page(s): 482 

Root / lemma: g''or-g''(or)o- 

Meaning: dirt, dung 

Material: Armenian /rc»/-/r 'smut'; 

gr. (36ppopo(; 'slime, mud, smut, ordure, crap, muck'. Note: common lllyrian g"- > b-. 

References: WP. I 694. 
Page(s): 482 

Root / lemma: g^ou- 

Meaning: cattle 

Grammatical information: m. f. Nom. Sg. g^ous. Gen. 5'"&^5(and g''ouosn), Akk. g''dm, 

Lok. g''oui 

Material: Old Indie gauh m. f. 'cattle' (= Avestan gaus ds.), Gen. goh (= Avestan gaus), 

Dat. gave (= Avestan gave), Lok. gav/{= Latin Abl. boue), Akk. gam (also 2silb., as 

Avestan g^m); PI. Nom. gavah{= Avestan gave). Gen. gavam (= Avestan gav^m), Akk. 

gah{= Avestan ga, Indo Germanic *g"'ds, gr. Doric pwc;) ; therefrom ^o-pa-/? 'herdsman, 

shepherd', gopayati, gopayat/^huieV, etc.; 

Armenian /roi/'cow'; 

gr. Attic pou(; m. f. 'cattle, cow', Akk. pouv [both with fake ou in place of old *pouq (with 
real ou), Akk. *pajv], Doric pox;, Akk. pwv. Gen. po(F)6(;, etc.; also in pou-AOroc; m. ' time 
of unyoking oxen from the plough, evening', pou-Tupov m. ' butter' (out of it Latin butyrum. 
Modern High German ' butter'), actually ' cow's cheese ' (TOpoc; 'cheese'), further in 



strengthening prefix pou- from pou-AT|jO(; " ravenousness ', etc. (Scliwyzer Gr. Gr. I 434, 6; 
577 p); Note: common lllyrian g"- > b-. 

Latin bos, bovism. f. "cattle' (Oscan-Umbrian loanword for Latin *vds)\ derivatives of 
stem bov- ( *g"ou- before vowel) or bu- ( *g"ou- before consonance), bub- (redupl. 
formation): bovTIe^ cowshed ', bubf/e ds., bovTnus^ of or pertaining to oxen or cows: 
medulla ', bubu/us6s. (lautl. identical with gr. poupaAo(; ' gazelle ', that with Old Indie 
gava/a-b'wM Buffer is not to be immediately equated), Bubona' cattle goddess ', etc.; 
Umbrian bum^ bovem ' {*g"dm), bue^ bove ', Oscan in Buvaianud, Volscan bim^ bovem '; 

Old Irish boi. "cow' (from arch. *bau, Indo Germanic *g"dus). Gen. arch, bou, bau, later 
bao, bo, in Brit, replaced through the derivative acymr. buch, ncymr. buwch, acorn, buch, 
bret. buc'b^co\N' {*boukka); here the Proto Irish FIN Boouiv5a (= *Bovovinda), nowadays 
engl. Boyne, Old Irish B6(f)ind^ die Kuhweifle '; *g"ou-, Celtic *bou- in compounds 
gallorom. bo-tege {*g"ou-tegos) " cowshed ' (M.-L. 1229a), cymr. bugail {*g"ou-k"olios) " 
6ouk6Ao(; ', bret. bugenn^ cowhide ', (under the influence of common Celtic -A75-, -nt- > - 
nn-), next to which *bovo-tegos\v\ abret. boutig, cymr. beudy 'cowshed '; Middle Irish 
buasach "rich (in cows)' from buas " richness ' ( *g"ouo-uid-to-s "cow- knowledge '); 

Old High German chuo, SSachs. Old Swedish /ro(from dem Akk. *kdn, Indo Germanic 
*g"dm). Old English Old Frisian cu. Old Icelandic kyr'co\N' {*kuzkorr\ g^ous. Old English 
cJ could also be = Old High German kuo); 

Latvian guovs'cow', Demin. guotiija; 

Slavic *(g'c»K^o'c» "cattle'. Old Church Slavic ^i/-/77i>/7c» "threshing floor', i.e. " place where 
steers out the grain '; 

Tocharian A /rc»"cow', PI. kowi, B kau, PI. Obliq. kewan; A kayurs, B kaurse^buW < 
*g"ou-urso-, to Old Indie vrsan- "bull'. 

Maybe alb. {*k"o-) kau 'ox' : Rumanian Cg'^o-) bou'ox' common lllyrian - Celtic g"'- > b-. 



compare still yio-derivative Old Indie gavya-, gavya-, Avestan gavya-' bovinus ', hom. 
T£aaapapoiO(; " worth four steers ', Armenian kogi' butter' ( *g"ouio-), and the zero grade 
Old Indie sata-gu- " owning hundred cows ' = Old pers. &atagu- "name of a country ' 
(originally people, actually " owning hundred cows '), Old Indie nava-gva, dasa-gva-, 
Avestan aeta{*g)va- EN, i.e. " one who has gleaming steers '; gr. £KaT6|j-pr| ( *-g"u-3) "an 
offering of a hundred oxen; sacrifice'; against it is Latin bu-bulcus' one who ploughs with 
oxen, a ploughman, a herdsman ' after su-bulcus' a swine-herd ' shortened from 



*bubulcus, after Specht Indog. Dekl. 234 here Old Norse kvTgr^ bull calf, /ri//^e "young 
cow' (after Holthausen Wb. of old westn. in addition westfal. quTne, nid. kween6s.) and 
kussi, kurs/'caW, etc. 

To cattle name one places the gr. family of pooKw " graze, feed ', pooKn, ^6o\q " feed, 
pasture ', porov "cattle", poravn " pasture herb, feed ', porrip, pcbTwp "herdsman, 
shepherd', pwriavsipa " man-feeding, nurse of heroes, epith. of fruitful countries '; Note: 
common lllyrian g"'- > b-. 

Maybe alb. fpcbrajp) it'a/'/" herdsman, shepherd'. 

as well as Lithuanian ^5^ya"herd', guju, guiti^^nve, push', ^^0/55 "herd'; the oldest parts 
of these rows may have possibly been *g"6[u]-to-m " herd of cattle ' and *g"ouid " be cattle 
shepherd '? About gr. np£apu(; "old' see below per-3. 

numerous would become borrowings from sumer. ^^ (older *gud) "bull, cattle'. Against it 
Specht Indog. Dekl. 33. 

References: WP. 1696 f., WH. I 112, 118, Trautmann 94, Schwyzer Gr. Gr. I 577, 708. 
Page(s): 482-483 

Root / lemma: g^ou- g^u- 

Meaning: dung, dirt 

Note: in Germanic and esp. in Balto-Slavic with meaning -development from "repugnance, 

disgust, repulsion, loathing ' to "small, disgusting animal, reptile' and from " pollute, soil, 

defile, mutilate, deform' to "vilify, revile, rebuke'. 

Material: Old Indie gu-tha-h, -/r? "excrement', Avestan gu-^a-u. "smut, ordure' (only by 

Gramm. also guvati^ cacat ', gunam " cacatum '); 

Armenian kuav\6 koy'crap, muck' {*g"du-so\ ? see below); 

Latin bubinare^ soil with the menstruations ' could be transfigured from old *bovind {\N\Vr\ 
Oscan-Umbrian biox g'^, as bovTIeio bubTle; Note: common lllyrian g"- > b-. 

maked. yorav (leg. ^urav) uv Hes. (?); 

Slavic *(gc»i/b/7c» "ordure' in russ. -Church Slavic ^c»i//7c» etc., in ablaut Slavic *gavjg, *gaviti 
in russ. -Church Slavic ogavitT vexare ', serb. gaviti se^ be disgusted ' (and changing 
through ablaut guvf mi se " disgusts me, I must throw up ', guviti se), Czech o-haviti^ 
mutilate, deform', c»/75K/7y "hideous', russ. dial, gavedbt, "horror', kir. havedha^ plebs ', 



Czech haved'^ fowl, plebs ', poln. gawiedz^ small children and domestic animals; fowl, 
lice; rabble, mob '. 

d^-extension g''e[u](i!^-, g''6[u]6^-, g''CiA^-. 



Lithuanian geda\. " shame, disgracefulness', gedingas^ schandbar ', gedintr humiliate, 
revile ', Old Prussian gTdan/Wk. "shame'; 

Old Church Slavic gadh m. " reptile (*disgusting animal); harmful animal' {*g"d6!"-). 
Church Slavic gazdu, gaditi^ abhor, detest, rebuke', russ. gaditb "smudge, befoul, spoil', 
Serb, gad^ disgust, repulsion, loathing; snake, worms ', Czech haditi^vMy, rebuke' (etc., s. 
Berneker289); 

poln. zadacsiQ^ abominari ', zadny, zadliwy^uq\y, nasty ' {*g'^e(i!^-)\ russ. dial, gfdkij 
"disgusting', kir. hyd^ disgust, repulsion, loathing '; with formants -d(h)a\v\ Czech o-hyzda 
{*gyz-da) " disgust, repulsion, loathing, repugnance', /7yzo'///" rebuke, vilify, reject', poln. 
Dialectal gizd^ disgust, repulsion, loathing, smut, impure person' (with other meaning 
change serb. ^/zo'a "pride, elegance, jewellery, pleasantness, agreeableness ' , s. 
Berneker 374); 

Middle Low German quad^ dung, excrements, ordure, manure ', Old High German quat. 
Middle High German quat, kot, kat. Modern High German Kot, Tirol kot^ disgusting 
animal', PI. koter^ all kinds of vermin ', Middle Low German quad. Middle Dutch qwaet, 
holl. kwaad^xx\a6, wicked, evil, ugly, spoiled', md. ^^ao'"mad, wicked, evil, disgust, weak'; 

with Indo Germanic -9U-. 

cymr. /7i/o'/'" dirty, filthy', i^^o'/'o "smudge'. Middle Irish buadra/m 'c\ou6y, bewilder' 
(compare Pedersen KG. I 112); Note: common lllyrian g"- > b-. 

Old English cwead^or6ure\ Old Frisian quad^evW, bad'; 

with i/from *-ai/- Slovak. 0/7^^5 "monster', kIr. o^^o'a "reprimand'. Old Russian guditi^ 
slander, blaspheme, accuse, blame ' ; 

with -a-as zero grade from -^u] or Germanic ablaut neologism ndd. quadder^ dirty 
dampness, mucus' = Middle Low German koder^ mucus'. Modern High German dial. 
koder, Koder^ glutinous mucus, catarrh'; 

also ndd. quassen {* kwadson) " dribble (in humidity) ', quasken, quatsken. Modern High 
German quatschen, engl. quask, squash and perhaps the people's name Quadr, 



alb. zT{*gue&^[io-), fern, zeze {* gue^'^JS) "black, unlucky, bad ', z/T "mourning, grief, 
famine '. 

References: WP. I 694 ff., WH. I 118f., Trautmann 81. 
Page(s): 483-485 

Root / lemma: gTdo'^- 

Meaning: embryon, young 

Material: Gr. pp£(po(; n. " foetus, youngling ', Middle Irish brommach {*g"rorrb^akos)\ Note: 

common lllyrian g"- > b-. 

Old Church Slavic zrebg^ plenitude'. 

References: WP. I 689. 

Page(s): 485 

Root / lemma: gTeig- 

Meaning: to sleep, dream 

Material: Gr. ppi^u) fppiyju)) sppi^a "sleep, be inactive', appi^ Eypnyopwc; Hes.; Note: 

common lllyrian g"- > b-. 

russ. grezitb " talk in sleep, fantasize' (barely *grez-, rather *grbz-), greza "dream, 
maundering, silly discourse '. very doubtful; s. also Berneker 351 . 

References: WP. I 698. 
Page(s): 485 

Root / lemma: g'^rend!^- 

Meaning: to swell; breast 

Material: Gr. pp£v9o(; "pride', Pp£v9uo|jai " bear oneself haughtily, hold one's head high, 

swagger, plume oneself on '; Note: common lllyrian g"- > b-. 

Latin grandis^ Of things, full-grown, large, great, full, abundant: tumulus. Of persons, 
grown up, large, big, tall: Of style, great, lofty, dignified, noble ' (a= eor o); 

Old Church Slavic ^/po'ij" breast', Slovak. /7mo' "elevation', poln. old gr§dzi^bxeas\!, grqd 
' eijToht^tell^n^umDf^l^ns^ ' (etc.). 

References: WP. I 699, WH. I 617 f. 
Page(s): 485 



Root / lemma: gTetso- 

Meaning: thick, big 

Material: Latin grossus^\h\cV! one maintains to bring together with Middle Irish cymr. corn. 

bret. bras^b\Q, large, thick'. Middle Irish also "strong'. However, it makes the Celtic 

vocalism a problem, and Middle Irish Z^^es "already' is barely an additional obstruction. 

Note: common lllyrian g"- > b-. 

Whether bras rather as *g"'ra-sto-\.o Latin gravis, above S. 476? 

References: WP. I 698, WH. I 623. 

Page(s): 485 

Root / lemma: gTeugh-, gTugh- 

Meaning: to gnash the teeth; to bite 

Material: a) gr. ppuxw " crunch with the teeth, to eat with much noise, to eat greedily ' 

(besides through derailment from ppu^u), sppu^a ppuKw) "bite', ppuySriv "biting', ppuypoq " 

bruxism ', ppux£T6(; "cold fever' ("chattering of teeth'). 

b) Old Irish bron^ distress ', cymr. brwyn^ piercing, biting pain ' (proto Celtic *brugnos)\ 
Note: common lllyrian g"- > b-. 

Lithuanian grauziu, grauztT gnaw ', sugruzinti^ 6es\xoY; 

Old Church Slavic gryzQ, grysti^ gnaw ' (in other Slavic languages also from gnawing 
grief; here probably also sloven, gruze PI. f. " scabies '). 

To g/yzg probab\Y russ. grustb " distress ', sloven. grusV disgust, repulsion, loathing '. 

References: WP. I 697 f., Trautmann 100. 
Page(s): 485-486 

Root / lemma: ha ha! 

Meaning: interjection of laughter 

Material: Old Indie ha ha, gr. a a (ngr. xaxa inscribed), Latin {ha)hahae. Modern High
```


## [2026-09-06T15:08:15.278Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in 210 211; do echo \"########## HRN printed p.$p (leaf $((p+21))) ##########\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p+21+1))\"'' HRN.txt; done"
}
```


### [2026-09-06T15:08:16.742Z] TOOL RESULT

```
########## HRN printed p.210 (leaf 231) ##########
— 210 —
gör 'Grab*, dagegen, das Geiger neuerdings (Lautl.
des Bai. 53) mit ai. ghörd- grausig, furchtbar ver-
glichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein
semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
g*aur wohl nicht arab. kaßr (Hübschmann unter oss.
d. gaur, t. daur, S. 123), sondern vielmehr neupers.
gebr, gahr^) (vergl. Geiger, bei. LW. gaur, No. 81,
wo allerdings phlv. gabrä (semitisch!, nur *Mann
bedeutend) nicht als Grundform stehen durfte).
939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
vergl. bällden (No. 173).
ai. vi + {/^vardh- ^heranwachsen, gedeihen ; ist schon
im PehlevT verschwunden.
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
LW. afy. yva/a 'Fleisch'; kurd. güst; bei. gö$t, n.
göM (128); wa/. gust, minj. yös, sar. gü^t, siyn. goß,
^) Zuerst hat dies wohl Bückert, ZDMG. 10, 183 ausgesprochen.
«) Vergl. Fr. Müller, WZKM. 5, 263.
########## HRN printed p.211 (leaf 232) ##########
mmtmmmmmmm^mmmmi^^^m^^^
— 211 —
945. göSe 'Winkel, Ecke .
KäS. gm.
aw. *gaosaha-.
kurd. güi, güse 'Winkel*; bei. LW. gösak (127).
de Lagard e, Ges. Abb. stellt auch küsk *Kiosk'
hierher, das, im türkischen Munde zu kföik geworden,
als kuSk und kü§k zu den Persern zurückgewandert
sei ; arab. LW. jausäq, syr. LW. pK'i;! *Kiosk' sprechen
dafür, phlv.-päz. küSk bezw. köSk (PP61.) als späte
Form nicht dagegen.
^46. gün 'Farbe; Art und Weise*, güne,
ap. 'Podo]y(wvrj, 'AXojyovvrj; aw. goona- *Farbe'; phlv.
günak, gün, arm. LW. goin^),
afy. LW. yüna,
Vergl. ctln (No. 450), zeryün (No. 661); ebenso
äderyün, humäyün (d. i. Humä + gün) und loääfwe,
947. güh *Schmutz, Kot'.
aw. güd-a- in güSö.lvareta- *im Schmutz kriechend*,
matlgü&a-; phlv. güh in gühvart {\d. 14, 16); skr.
gütha- Exkremente*; arm. ku 'Mist' (H. No. 149); ksL
got>tno,
kurd. gü 'Exkremente'; afy. yul; bei. n. gtd^ (436);
wa/. g'w, jrf, kasm. gUs,
V
948. göher 'Edelstein ; Materie, Ursprung, Geschlecht (Sahn.
I, 149 Vers 366; 170 Vers 741)*2), arab. LW. jauhar
'Edelstein; Substanz'.
skr. jfö^m- 'Geschlecht, Ursprung*; phlv. göhr bezw.
göhar 'Materie, Substanz'.
Die Bedeutung 'Edelstein* ist erst sekundär; sie
findet sich noch nicht im Mittelpersischen ausser an
einigen späten Stellen.
*) Dass arm. ffofn persisohes LW. ist, beweist sicher goinagoin
'bunt* — np. gündgün.
*) äshn. II, 765 Vers 10 folgg. wird goher im Gegensatz zu
nizlid als die von Gott in den Menschen gelegte gute Natur definiert.
14*
```


## [2026-09-06T15:08:30.108Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in 236 237; do echo \"########## HRN p.$p ##########\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((p+22))\"'' HRN.txt; done\necho \"########## Horn No. 888 / gav ##########\"\ngrep -n \"888\\. \" HRN.txt | head"
}
```


### [2026-09-06T15:08:31.676Z] TOOL RESULT

```
########## HRN p.236 ##########
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
########## HRN p.237 ##########
— 237 —
*m + V^göp- "behüten, verwahren*, vergl. ai. X^göp- ;
plilv. n(i)huflan 'verbergen*.
kurd. nixiftifi *sich verbergen*, nix^ftin Causat.
^verbergen.
Bartholomae meint nach briefl. Mitteilung, dass
nihuften sein h von np. niMti (No. 1058) bezogen
habe; ai. i^^göp- sei vielleicht eine Nebenform von
[y^göh^ und die dazu gestellten Formen stammten
also nur zum Teil von göpä- 'Hirt*. Vergl. auch
Johansson, Indog. Forsch. IL 50, 51. Jedenfalls
wird es schwer, mhffffeti gänzlich von \ ^göh- zu
trennen.
1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
Testflöte* '), seh^näi ; nnlze.
g. nad.
ap. *nada' 'Schilf; phlv. nai bezw. nad (PPGl);
ai. nadd-, nadd- Schilfrohr (Pischel, ZDMG. :U),
717 folg., Ved. Studien I, 183 folg.); arm. net Pfeil*
(H. No. 219)?
Die Lautverhältnisse sind noch nicht richtig er-
kannt. Np. nei, g. nad setzen unbedingt eine Urform
*nada- voraus ; neben dieser gab es eine zweite Form
*narda-, auf welche ai. nadd- (gr. LW. vdodo^*, hebr.
LW. '^.IJ-)) und np. näf zurückgehen. Das jüngere
skr. näld- ist persisches Lehnwort. Wie häufig,
erscheint dann auch eine gedehnte Form, np. näl^
ai. nädt-, die nicht mehr 'Schilf, sondern ein 'Musik-
instrument aus Rohr, Flöte* bezeichnet. Skr. Hald-
wird jüngere Form für nadd- sein, wie Pischel an-
nimmt, nalada- ist sanskritisirtes vd^öoq,
1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
(No. 1066), niy[ayed,
ap. naiy 'nicht'; aw. nöit, na^ci-; päz. ne; ai. ncd.
oss. d. 7ie6i, t. ntci nichts' (201).
*) Kauk.-bergjüd. eürnai 'Schalmei*, russ. LW. zurna.
*) Die aus dorn Persiacbeii entlehnt sind.
########## Horn No. 888 / gav ##########
7717:888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
```


## [2026-09-06T15:08:40.455Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /888\\. / {print NR-1\": leaf\"; print}' HRN.txt | head -60"
}
```


### [2026-09-06T15:08:42.303Z] TOOL RESULT

```
219: leaf
- 198 —
886. ijästen Vendun, drehen' (8ähn. I, 368 Vers 8-1:9; 369
Vers 852), Praes. yär-em (unbelegt) ^) ; gesten, Praes.
gerd-em, gerdlden, gerdämden, vergl. berd packe dich*,
berdtden 'sich vom Wege entfernen, abwenden* (s.
No. 195).
g. västmün ; vergl. Käs. K. gelnoimün [l = rd, wäh-
rend in V. Z. r erscheint, Seite 180).
ai. [/^vart-, vdrtate *sich wenden, drehen'-); aw. vergl.
güd^ö.]varetanqm (vd. 14, 6) und varetata (ZPGL); phlv.
O'istan (PV.), gast (vd. 9 (84) GL, West), vartitan,
gartitan (Bund.), vart{i)sn, gart{i)sn (Bund.), vartänT-
tan (AV.).
kurd. geriyän 'spazieren, sich wenden; bei. LW.
gardag , n. garday umkehren , umwenden (70) ; sar.
yirs-am, yerd-ao etc.
887. (/am Schritt'.
aw. gäma- 'Schritt'; phlv. gäm.
888. f/äv llind', gö, gög 'Kalb' {^gavaka-)'''), göban 'Hirte'.
Kä§. V. K. Z. (/ö, Q. göb,
ap. vergl. Gau[brüva'j Fioß^vag; aw. gäv- Rind';
phlv. gö bezw. gav^ arm. LW. gavazan (echt hov *Kuh'
H. No. 148); ai. gdi^-,
kurd. gä 'Rind'; af/. yvä\ oss. d. yog, t. qiig 'Kuh'
(93); bei. gök, n. gö/ *Rind, Kuh, Ochse (123); wa/.
yäu, yü, sar. Jaw, siyn. /do, sangl. minj. ydo, yayn. gova;
vergl. sar. yubün, af/. yö6a 'Hirte*.
np. gävmes 'Büffel' : phlv. gavmes (Bund.), arm. LW.
gomesy syr. LW. IS?"»?!:!, oss. LW. kambec, kambec.
M Wahrscheinlich nur eine grammatische Bildung nach kärem
von kästen,
*) In F ick 's vierter Auflage des Vergl. Wörterbuches kehrt
Seite 316 auch aw. verente (Y. 43, 16; 51, 16) als *1. 8g. med. von
y rare.-* wieder , während es eine 3. 8g. von 1/ rrtr- (9. Klasse) ist
(Bartholemae, Ar. Forsch. II, 89; KZ. 29, 310).
^) Vielleicht auch jüd.-pers. n)} 'Motte' (Is. 51, 8), wie wir z. B.
gewisse Käfer ebenfalls *Kühchen* nennen?
```


## [2026-09-06T15:08:54.178Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== KLN cow =====\"; grep -n \"^cow, n\" KLN_1966.txt | head\necho \"===== KLN beef/butter/buffalo =====\"; grep -n \"^beef,\\|^buffalo,\\|^butter,\\|^bovine,\" KLN_1966.txt | head\necho \"===== AHD gwou =====\"; grep -n -i \"^g.ou-\\|gwou\\|g\\^wou\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:08:54.299Z] TOOL RESULT

```
===== KLN cow =====
===== KLN beef/butter/buffalo =====
===== AHD gwou =====
555:gvou-. Ox, bull, cow. Nominative singular form *gvéu-s. 1. Germanic *kéuz (> *kiiz) in Old English ci, cy, cye, cow: COW], (KINE); COWSLIP. 2. Latin bds (stem bov-), ox, bull, cow: BEEF, BOVINE, BUGLE!; OvIBos. 3. Greek bous, ox, bull, cow: BOUSTROPHEDON, BUCEPHALUS, BUCOLIC, BULIMIA, BUPRESTID, BUTTER, (BUTYRIC). 4. Sanskrit go-, gauh, cow: GAYAL. 5. Suffixed form *gv6u-ro- in Sanskrit gaurah, wild ox: GAUR. 6. Zero-grade form *guw-d- in Greek hekatombé, “sacrifice of a hundred oxen” (hekaton, hundred; see dekm): HECATOMB. [Pok. gtou- 482.]
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1317:BOUSTROPHEDON gWou-, streb(h)-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1557:GAST gheis- GASTRIC gras- GASTRO- gras- GASTRULA gras- GATHER ghedh- GAUCHE weng- GAUD gau- GAUDY! gau- GauDY? gau- GAUGE ghalgh- GAUNTLET? klou- GAUR gWou- GAVEL? ghabh- GAWK ghow-é- GAYAL gWou- _ GEANTICLINE gé GEAR garwian GEGENSCHEIN gagina, skeei- GELANDESPRUNG lendh-2, spergh- GELATIN gel-3 GELATION gel-3 GELD! ghel-3 GELD2 gheldh- GELDING ghel-3 GELID  gel-3 GELIGNITE egni- GELT! gheldh- GEM gembh- GEMINATE yem- GEMINI yem- GEMMA gembh- GEMMATE gembh- GEMMULE gembh- GEMOT mdéd- GEMSBOK bhugo- GEMUTLICH mé-1 GEMUTLICHKEIT mé-1 -GEN gene- GENDARME gene- GENDER gene- GENEALOGY genoe- GENERAL gene- GENERATE genoe- GENERATION geno- GENERIC gene- GENEROUS gene- GENESIS gene- -GENESIS gene- GENIAL! gene- GENIAL? genu-2 GENICULATE genu-1 GENITAL gene- GENITIVE gene- GENITOR gene- GENIUS gene- GENOCIDE gene- GENOTYPE gene- GENRE gene- GENS gene- GENT! gene- GENTEEL gene-
1716:KIND! gene- KIND? gene- KINDERGARTEN gene-, gher-1 KINDRED af-, gene- KINE gWou- KINEMATICS kei-3 KINESIOLOGY kei-3 -KINEsIS_ kei-3 KINESTHESIA kei-3 KINETIC kei-3 KING gene-
2017:OVIBOS gWou-, owi- OVINE owi-
```


## [2026-09-06T15:09:05.024Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== AHD dung =====\"; grep -n -i \"dung\" AHD_watkins1985.txt | head -20\necho \"===== KLN cow =====\"; grep -n \"cow, n\\.\" KLN_1966.txt | head; grep -n \"OE\\. cu\" KLN_1966.txt | head"
}
```


### [2026-09-06T15:09:05.107Z] TOOL RESULT

```
===== AHD dung =====
364:LOIN. 4. Possibly suffixed variant *dlo-gho- in Greek dolikhos, long: DOLICHOCEPHALIC, DOLICHOCRANIAL. [Pok. 5. del- 196.] del-2. To recount, count. 1. Germanic *taljan in Old English tellan, to count, recount: TELL. 2. Germanic *tal6é in: a. Old English talu, story: TALE; b. Middle Dutch dle, speech, language: TAAL. 3. Old English denominative talian, to tell, relate, probably akin to the source of Middle English talken, to talk: TALK. 4. Per- haps Greek dolos, ruse, snare: DOLERITE. [Pok. 1. del- 193.] del-3. To split, carve, cut. 1. Suffixed form *del-to- in Germanic *teldam, “thing spread out,” in Old English teld, awning, tent: TILT?. 2. Germanic extended form *telg- in Old English telgor, telgra, twig, branch: TILLER’. 3. Perhaps o-grade form *dol-é- in Latin dolére, to suffer (? < “to be beaten”): DOLE?, DOLOR; CONDOLE, INDO- LENT. 4. Suffixed o-grade form *dold-dhraé in Latin dolabra, a heavy chopping tool (< doldre, to chisel, hew): DOLABRIFORM. [Pok. 3. del- 194.] del-*. To drip. Perhaps suffixed (stative) o-grade form *dol- in Germanic *talgaz in Middle Low German falg, talch, tallow (< “dripping fat”), perhaps akin to the source of Middle English talow, tallow: TALLOw. [Pok. 4. del- 196.] deme-'. Also dem-. House, household. 1. Suffixed re- duced o-grade form *dom-o-, dom-u-, house, in: a. Latin domus, house: DOME, DOMESTIC, DOMICILE; MAJOR- DOMO; b. suffixed form *dom-o-no- in Latin dominus, master of a household (feminine domina > Old French dame, lady): DAME, DAN?, DANGER, DoM, DOMAIN, DOMI- NATE, DOMINICAL, DOMINIE, DOMINION, DOMINO}, (DOM- INO2), DUENNA, DUNGEON; (MADAM), MADAME, MADEMOISELLE, MADONNA, PREDOMINATE. 2. Com- pound *dems-pot-, “house-master” (*-pot-, powerful; see poti-), in Greek despotés, master, lord: DESPOT. 3. Root form *dem()-, to build (possibly a separate root), in: a. Germanic *timram in Old English timber, building material, lumber: TIMBER; b. Germanic *tumfté in Old Norse topt, homestead: Torr. [Pok. dem- 198.] deme-2. To constrain, force, especially to break in (horses). 1. Suffixed o-grade form *dom-o- in Germanic *tamaz in Old English tam, domesticated: TAME. 2. O-grade form *doma- in Latin domdre, to tame, sub- due: DAUNT; INDOMITABLE. 3. Zero-grade form *dmo- in Greek daman, to tame (> adamas, unconquerable): ADAMANT, DIAMOND. [Pok. (dema-), doma- 199.] denk-. To bite. 1. Germanic *tanhuz in Old English toh, tenacious, sticky (< “holding fast”): TOUGH. 2. Germanic *tanguz in Old English tang(e), tong(e), pincers, tongs: TONGS. 3. Germanic *tang- in Old Norse tangi, a point, sting, akin to the Scandinavian source of Middle English tonge, tange, point, tang: TANG!. 4, Germanic *teng- in Old High German zinko, spike, prong: z1Nc. [Pok. denk- 201.) dens-'. To use mental force. Reduplicated and suffixed zero-grade form *di-dns-sko- in Greek didaskein, to teach: pipactic. [Pok. 1. dens- 201.] dens-2. Dense, thick. 1. Suffixed form *dens-o- or *dns-o- in Latin dénsus, thick: DENSE; CONDENSE. 2. Suffixed zero-grade form *dns-u- in Greek dasus, hairy, shaggy: DASYURE. [Pok. 2. dens- 202.] dent-. Tooth. (Originally participle of ed- in the earlier meaning “to bite.”) 1. O-grade form *dont- in Germanic *tanthuz in Old English toth, tooth: TOOTH. 2. Zero-grade form *dné- perhaps in Germanic *tunth-sk- in Old English tisc, tix, canine tooth: TUSK. 3. Full-grade form *dent- in Latin déns (stem dent-), tooth: DENTAL, DENTATE, DENTI-, DENTICLE; (BIDEN- TATE), DANDELION, EDENTATE, INDENT!, (INDENTURE), TRIDENT. 4. O-grade variant form *(o)dont- in Greek odén, odous, tooth: -ODON, -ODONT, ODONTO-; CERATO- Dus. [In Pok. ed- 287.] deph-. To stamp. 1. Suffixed form *deph-s-ter- in Greek
601:kekw-. To excrete. Suffixed o-grade form *kok-ro- in Greek kopros, dung: copro-. [Pok. kek- 544.]
940:*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
1435:DRONE! dher-3 DRooP dhreu- DROP dhreu- DROPsY wed-1 DROSHKY dhragh- DRoss_ dher-1 DROUGHT dreug- DROVE? dhrelbh- DROWN dhreg- DROWSE dhreu- DRUID deru DRUPE deru, pekw- DRY dreug- DRYAD deru DUAD dwo- DUAL dwo- DuB! dheubh- DUB? dheubh- DUBIOUS dwo- DUCAL deuk- DucaT deuk- DUCHESS deuk- DUCHY deuk- Duct deuk- DUCTILE deuk- DUDEEN dheu-1 DUE ghabh- DUEL duellum DUENNA deme-1 DUET dwo- DUKE deuk- DukHoBoR_ bher-2, dheu-! DULCET dik-u- DULCIFY dik-u- DULL dheu-! Duma dhé-1 DUMB dheu-1 DUMP dub- pDuN2 dheu-? DUNDERHEAD (s)tene- DUNE dhino- DUNGEON deme-1 DUNK teng- DUO- dwo- DUODECIMAL dekm, dwo- DUOPSONY wes-1 DUPLE dwo- DUPLEX dwo- DUPLICATE dwo- DUPLICITY dwo- DURABLE deue- DURA MATER deru DURAMEN deru DURANCE deue- DURATION deue- DURBAR dhwer- DURESS deru DURING deue- DURST dhers- DURUM deru Dusk dheu-! Dust dheu-' DutTcH teuta- DUTY ghabh- DUUMVIR wi-ro- DUVETYN dheu-! DWELL dheu-! DWINDLE dheu-3 DYAD dwo- DYNAMIC deu-2 DYNAMITE deu-2 DYNAST deu-2 DYNASTY deu-2 Dys- dus- DYSENTERY en DYSLEXIA leg-1 DYSMENORRHEA mé-2 DYSPEPSIA pekw- DYSPLASIA pele-2 DYSPNEA pneu- DYSPROSIUM ei-1
===== KLN cow =====
9489:cowslip,  n.,  a  plant  with  yellow  flowers.  —  OE. cu-slyppe,  fr.  cu,  ‘cow’,  and  slyppe,  ‘slime’.  See cow  and  slip  and  cp.  oxlip.
10034:cutlet,  n.  —  F.  cotelette,  lit.  ‘a  little  rib’,  a  double dimin.  of  cote,  ‘rib’,  fr.  OF.  coste,  fr.  L.  costa, ‘rib,  side’.  See  coast  and  cp.  costal.  Cutlet  was prob.  influenced  in  form  by  cut. cuttlefish,  cuttle,  n.  —  ME.  cotul,  codul,  fr.  OE. cudele,  ‘cuttlefish’,  rel.  to  dial.  Norw.  kaule  (for *kodle),  lit.  ‘pouch  fish’,  and  to  OE.  codd,  ‘bag, shell,  husk’.  See  cod,  ‘a  small  bag’, cutty,  adj.,  short  (Scot,  and  dial.)  —  Formed  fr. cut  with  adj.  suff.  -y.
30131:presby-,  combining  form  meaning  ‘old’,  as  in presbyopia.  —  Gk.  repeerpu-,  fr.  replafkip,  ‘old, venerable’,  which  stands  for  “repsa-yu:;  (cp. Cretan  repstyu;,  Boeot.  reptoyuq),  and  lit. means  ‘he  that  goes  first’.  The  first  element  of this  compound  is  rel.  to  Gk.  reapoc,  ‘before, aforetime,  formerly’,  and  cogn.  with  L.  prae, ‘before’ ;  see  pre-.  The  second  element  is  a  deriv¬ ative  of  l.-E.  base  *gwu-,  ‘to  go’,  which  is  rel.  to base  *g"'em-,  of  s.m.,  whence  Gk.  fSxrveiv,  ‘to go’,  L.  venire,  ‘to  come’,  Goth,  qiman,  OE. cuman,  ‘to  come’ ;  see  come  and  cp.  base,  ‘bot¬ tom’.  Cp.  priest.
```


## [2026-09-06T15:09:10.184Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'g\\\"\\?ou-\\|gwou\\|g\"\"ou' KLN_1966.txt | head -20\necho \"--- cow n entry ---\"\ngrep -n \"^cow, \" KLN_1966.txt | head\ngrep -n \"cow,  n\" KLN_1966.txt | head"
}
```


### [2026-09-06T15:09:10.263Z] TOOL RESULT

```
8329:comely,  adj.  —  ME.  cumelich,  cumlich,  comeliche, comlich,  fr.  OE.  cymlie,  formed  with  suff.  -lie (see  like,  adj.),  fr.  cyme,  ‘fine,  beautiful,  splen¬ did’,  orig.  ‘frail,  delicate,  tender’,  which  is  rel. to  ME.  kime,  ‘weak,  delicate’,  OHG.  chumo, kiimd,  MHG.  kume,  ‘with  difficulty’,  OHG. chumig,  kumig,  ‘weak,  delicate’,  G.  kaum, ‘hardly,  scarcely’.  The  original  meaning  of  ME. kime  and  OHG.  chumig  was  ‘lamentable,  piti¬ able’;  cp.  OHG.  chuma,  ‘sorrow’,  OHG.  chu- mon,  ‘to  mourn’,  OS.  kumian,  ‘to  lament,  de¬ plore’.  All  these  words  are  derivatives  of  the I.-E.  imitative  base  *gou-,  *gow-,  ‘to  shout,  cry’ whence  also  OE.  ciegan  (for  orig.  *kaujan ),  ‘to call’,  cyta,  ‘kite’,  Ol.gavate,  ‘sounds,  resounds’, Gk.  yoav,  ‘to  wail,  groan,  weep’,  MLG.  kitten, ‘to  chatter,  babble,  prate’,  Lith.  gaudziii,  gausti, ‘to  howl’,  gaudas,  ‘lamentation’,  OSIav.  govoriti, ‘to  make  a  noise’,  Russ,  govorit',  Serb,  and Croat  ian^ovoWh,  Czech  hovoriti,  Slovak  hovorit’, ‘to  speak’,  OIr.  guth,  ‘voice’.  Cp.  kite.  The  word comely  was  influenced  in  meaning  by  an  as¬ sociation  with  come.
16485:govern,  tr.  and  intr.  v.  —  OF.  governer  (F.  gou- verner),  fr.  L.  gubernare,  ‘to  steer  or  pilot  a ship ;  to  govern’,  a  loan  word  introduced  through the  medium  of  the  Etruscans  fr.  Gk.  xo[3epvav, which  is  often  compared  with,  but  prob.  not related  to,  OI.  kiibaralf,  ‘pole,  beam,  tiller’,  Lith. kumbryti,  ‘to  govern’,  kumbras,  ‘tiller’.  Cp. gubernatorial.  Cp.  also  cybernetics.
16860:gum,  n.,  flesh  in  which  the  teeth  are  set.  —  ME. gome,  fr.  OE.  goma,  ‘palate’  (pi.  goman,  ‘jaws’), rel.  to  ON.  gomi,  ‘palate’,  gomr,  ‘gum’,  Swed. gom,  ‘palate’,  Dan.  gumme,  ‘gum’,  OHG.  gou- mo,  MHG.  goume,  G.  Gaumen,  ‘palate’,  and cogn.  with  Lith.  gomurys,  ‘palate’,  Lett,  ga¬ muts .  ‘windpipe,  trachea’,  fr.  I.-E.  base  *ghdu-, *gheu-,  *gheu-,  ‘to  gape’,  whence  also  Gk.  yctog (for  Vctfog),  ‘gulf,  chasm,  abyss,  the  rude  un¬ formed  mass’,  xotuvog,  ‘gaping’,  y  iay.a,  ‘chasm, gulf’.  The  above  base  is  rel.  to  base  *ghei-,  *ghi-, ‘to  gape,  yawn’.  See  yawn  and  words  there  re¬ ferred  to.
20734:kitchenette,  n.  —  A  hybrid  coined  fr.  kitchen with  -ette,  a  sulf.  of  French  origin, kitchen  midden,  refuse  marking  a  primitive  hu¬ man  settlement.  —  Dan.  kjokken  madding,  lit. ‘kitchen  midden’.  See  kitchen  and  midden, kichery,  n.  —  A  variant  of  kedgeree, kite,  n.  —  ME.  kite,  fr.  OE.  cyta,  ‘kite,  bittern’, rel.  to  ciegan  (for  orig.  *kaujan),  ‘to  call’,  MHG. ( stein-)kuze ,  G.  Kattz,  ‘screech  owl’,  MLG. kitten,  ‘to  chatter,  babble,  prate’,  LG.  kdter (whence  G.  Kdter),  ‘cur,  dog’,  fr.  I.-E,  base *gou-,  *gow-;  ‘to  shout,  cry’,  whence  also  OI. gavate,  ‘sounds,  resounds’,  Gk.  yoav,  ‘to  wail, groan,  weep’,  yooq,  ‘wailing,  groaning,  weeping’, OE.  cyme,  ‘fine,  beautiful,  splendid’,  orig.  ‘frail, delicate,  tender’.  See  comely, kith,  n.,  now  used  only  in  the  phrase  kith  and  kin. —  ME.  cuththe,  kith,  fr.  OE.  cydd(u)-,  ‘know¬ ledge,  acquaintance,  relationship;  native  coun¬ try’,  fr.  cud,  ‘known’,  pp.  of  cunnan,  ‘to  know’. See  can,  aux.  v.,  and  cp.  uncouth, kitling,  n.,  a  small  kitten.  — -  ME.,  fr.  ON.  ket- lingr,  ‘kitten;  young  of  other  animals’,  dimin. of  kdttr,  ‘cat’.  See  cat  and  dimin.  sufF.  -ling, kittel,  n.,  a  white  cotton  robe  which  pious  Jews wear  during  the  High  Holiday  services,  and  in which  they  are  buried.  —  Yiddish  kitel,  fr.  G. Kittel,  ‘frock,  coat’,  fr.  MHG.  kittel,  kitel,  ult. fr.  Arab.  qu(n,  ‘cotton’,  whence  also  G.  Kattun, ‘cotton’ ;  see  cotton.  For  the  ending  -el  in  kittel see  the  suffixes  -el  and  -le. kitten,  n.  —  ME.  kitoun,  a  blend  of  kitling  and ONF.  caton  (corresponding  to  OF.,  F.  chaton), ‘little  cat’,  dimin.  of  ONF.  cat  (corresponding to  OF.,  F.  chat),  ‘cat’.  See  cat  and  cp.  kittle,  ‘to bring  forth  kittens’,  kitty,  ‘kitten’.
--- cow n entry ---
9480:cow,  n.  —  ME,  ky,  kye,  fr.  OE.  cu,  rel.  to  OS.  ko, OFris.  ku,  MDu.  coe,  Du.  koe,  OHG.  chuo, kuo,  MHG.  kuo,  G.  Kuh,  Dan.  and  Swed.  ko, ON.  kyr,  Norw.  kyr,  ko,  ‘cow’,  and  cogn.  with OIr.  bo,  W.  buw,  ‘cow’,  L.  bos,  Gk.  (3o0q  (for *gwaus-),  ‘ox’,  Lett,  guovs,  ‘cow’,  OSlav.  *gov- gdo,  Czech  hovado,  Slovak  hovddo,  ‘ox’,  OI. gduh,  Avestic  gaush,  ‘ox,  bull,  cow*,  Toch.  A ko,  ki,  B  keu,  ‘cow’,  Arm.  kov,  ‘cow’,  kogi, ‘butter’.  AH  these  words  ult.  derive  fr.  Sumeric gu  (fr.  earlier  gud),  ‘bull,  ox’,  a  word  of  imi¬ tative  origin.  Chinese  ngo,  ngu,  ‘ox’,  is  a  Sumeric loan  word  (possibly  through  the  medium  of  an Indo-European  language).  Cp.  kine.  Cp.  also Bos,  boustrophedon,  bovine,  Bucentaur,  Buce¬ phalus,  Buceros,  bucolic,  buffalo,  bugle,  bugloss, Bupleurum,  Buprestis,  Busycon,  butter,  Gaek- war,  gaur,  Gautama,  gopura,  hecatomb,  nilgai, priest,  sang-de-boeuf.
9480:cow,  n.  —  ME,  ky,  kye,  fr.  OE.  cu,  rel.  to  OS.  ko, OFris.  ku,  MDu.  coe,  Du.  koe,  OHG.  chuo, kuo,  MHG.  kuo,  G.  Kuh,  Dan.  and  Swed.  ko, ON.  kyr,  Norw.  kyr,  ko,  ‘cow’,  and  cogn.  with OIr.  bo,  W.  buw,  ‘cow’,  L.  bos,  Gk.  (3o0q  (for *gwaus-),  ‘ox’,  Lett,  guovs,  ‘cow’,  OSlav.  *gov- gdo,  Czech  hovado,  Slovak  hovddo,  ‘ox’,  OI. gduh,  Avestic  gaush,  ‘ox,  bull,  cow*,  Toch.  A ko,  ki,  B  keu,  ‘cow’,  Arm.  kov,  ‘cow’,  kogi, ‘butter’.  AH  these  words  ult.  derive  fr.  Sumeric gu  (fr.  earlier  gud),  ‘bull,  ox’,  a  word  of  imi¬ tative  origin.  Chinese  ngo,  ngu,  ‘ox’,  is  a  Sumeric loan  word  (possibly  through  the  medium  of  an Indo-European  language).  Cp.  kine.  Cp.  also Bos,  boustrophedon,  bovine,  Bucentaur,  Buce¬ phalus,  Buceros,  bucolic,  buffalo,  bugle,  bugloss, Bupleurum,  Buprestis,  Busycon,  butter,  Gaek- war,  gaur,  Gautama,  gopura,  hecatomb,  nilgai, priest,  sang-de-boeuf.
34203:scow,  n.,  a  large,  flat-bottomed  lighter.  —  Du. schouw,  fr.  MDu.  scouwe,  related  to  MDu. scolde,  scoelde ,  scoude ,  of  s.m.,  and  to  OS. scaldan,  ‘to  push  a  boat  from  the  shore’.
```


## [2026-09-06T15:09:17.294Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=9480{n+=gsub(/\\f/,\"\")} END{print \"leaf(0-based)=\"n}' KLN_1966.txt\necho \"--- buffalo entry ---\"; grep -n \"^buffalo,  n\" KLN_1966.txt | head -3\necho \"--- butter ---\"; grep -n \"^butter,  n\" KLN_1966.txt | head -3\necho \"--- beef ---\"; grep -n \"^beef,  n\" KLN_1966.txt | head -3"
}
```


### [2026-09-06T15:09:19.688Z] TOOL RESULT

```
leaf(0-based)=202
--- buffalo entry ---
--- butter ---
--- beef ---
```


## [2026-09-06T15:09:27.036Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==203' KLN_1966.txt | head -8\necho \"...\"\nawk 'BEGIN{RS=\"\\f\"} NR==203' KLN_1966.txt | tail -4"
}
```


### [2026-09-06T15:09:29.125Z] TOOL RESULT

```
id  of  a  woman),  lit.  ‘covered  (i.e. protected)  by  her  husband’.  —  ME.,  fr.  OF. covert  (F.  couvert),  pp.  of  covrir.  See  cover  and cp.  overt.  Cp.  also  feme  covert  and  discovert. Derivatives:  covert,  n.,  covert-ly,  adv.,  covert¬ ness,  n.
coverture,  n.,  the  status  of  a  married  woman  (law). —  OF.  (F.  couverture),  fr.  covert,  pp.  of  covrir. See  prec.  word  and  -ure. covet,  tr.  and  intr.  v.  —  Fr.  OF.  coveitier,  fr.  VL. *cupidietdre,  fr.  *cupidietas,  altered  fr.  L.  cupi- ditds,  ‘desire’,  fr.  cupere,  ‘to  desire’ ;  see  Cupid. OF.  coveitier  soon  became  conveitier  (F.  con- voiter)  on  analogy  of  the  numerous  words  be¬ ginning  with  con-.
Derivatives:  covet-able,  adj.,  covet-er,  n.,  covet¬ ing,  adj.,  covet-ing-ly,  adv.,  covetise  (q.v.),  covet- ive-ness,  n.,  covetous  (q.v.) covetise,  n.,  covetousness  (obsol.)  —  OF.  coveitise (F.  convoitise),  fr.  VL.  *cupiditia,  fr.  L.  cupidus, ‘desirous’,  fr.  cupere,  ‘to  desire’.  See  covet  and -ise.
covetous,  adj.  —  OF.  coveitos  (F.  convoiteux), from  the  stem  of  coveitier,  ‘to  covet’.  See  covet and  -ous.
Derivatives:  covetous-ly,  adv.,  covetous-ness,  n. covey,  n.,  a  brood  of  partridges.  —  OF.  covee (F.  couvee),  prop.  fem.  pp.  of  cover  (F.  couver), ‘to  sit  on,  hatch’,  fr.  L.  eubare,  ‘to  lie  down’, which  is  cogn.  with  Gk.  xu(3oi;,  ‘hollow  above the  hip  of  cattle’.  See  cubicle, covid,  n.,  a  varying  measure  of  length.  —  Indo- Port.,  fr.  Port,  covado,  ‘ell,  cubit’,  fr.  L.  cubitum, cubitus,  ‘elbow,  ell,  cubit’,  whence  also  Sp.  codo, Catal.  colde,  colze,  Provenq.  coide,  F.  coude, Tosc.  govito,  Olt.  gombito.  It.  gomito,  Rum.  cot, ‘elbow’.  See  cubit, covil,  n.  —  A  var.  spelling  of  kovil. covin,  n.,  an  unlawful  agreement  (law).  —  OF. covin,  covine,  fit.  ‘a  coming  together’,  fr.  covenir. See  covenant  and  cp.  coven, covine,  n.  —  See  coven.
coving,  n.,  a  cove  or  series  of  coves  (archil.)  — Formed  fr.  cove,  ‘arch,’  with  subst.  suff.  -tag.
364
cow,  n.  —  ME,  ky,  kye,  fr.  OE.  cu,  rel.  to  OS.  ko, OFris.  ku,  MDu.  coe,  Du.  koe,  OHG.  chuo, kuo,  MHG.  kuo,  G.  Kuh,  Dan.  and  Swed.  ko, ON.  kyr,  Norw.  kyr,  ko,  ‘cow’,  and  cogn.  with OIr.  bo,  W.  buw,  ‘cow’,  L.  bos,  Gk.  (3o0q  (for *gwaus-),  ‘ox’,  Lett,  guovs,  ‘cow’,  OSlav.  *gov- gdo,  Czech  hovado,  Slovak  hovddo,  ‘ox’,  OI. gduh,  Avestic  gaush,  ‘ox,  bull,  cow*,  Toch.  A ko,  ki,  B  keu,  ‘cow’,  Arm.  kov,  ‘cow’,  kogi, ‘butter’.  AH  these  words  ult.  derive  fr.  Sumeric gu  (fr.  earlier  gud),  ‘bull,  ox’,  a  word  of  imi¬ tative  origin.  Chinese  ngo,  ngu,  ‘ox’,  is  a  Sumeric loan  word  (possibly  through  the  medium  of  an Indo-European  language).  Cp.  kine.  Cp.  also Bos,  boustrophedon,  bovine,  Bucentaur,  Buce¬ phalus,  Buceros,  bucolic,  buffalo,  bugle,  bugloss, Bupleurum,  Buprestis,  Busycon,  butter,  Gaek- war,  gaur,  Gautama,  gopura,  hecatomb,  nilgai, priest,  sang-de-boeuf.
...
cracknel,  n.,  a  kind  of  hard,  brittle  biscuit.  — Fr.  earlier  crakenel,  metathesis  of  F.  craquelin, ‘cracknel’,  fr.  MDu.  crakelinc  (Du.  krakeling), fr.  craken,  ‘to  crack’.  See  crack, cracovienne,  n.,  a  Polish  dance.  —  F.  (short  for danse  cracovienne,  fit.  ‘a  Cracow  danse’),  fem. of  cracovien,  ‘of  Cracow’,  fr.  Cracovie,  ‘Cracow’, fcracy,  combining  form  meaning  a  certain  type of  ‘rule’  or  ‘government’ ,  as  in  monocracy.  —  OF. -cracie  (F.  -cratie),  fr.  Gk.  -xpa-cia,  ‘rule’,  fr.
cradge
366
xpaxoi;,  ‘strength,  might,  power,  rule,  sway,  do¬ minion’  (whence  xpaxsxv,  ‘to  be  strong,  rule over’,  xpxxup,  ‘strong,  mighty’),  which  is  cogn. with  Goth,  hardus,  ‘hard’,  OE.  heard,  ‘hard, brave’.  See  hard  and
```


## [2026-09-06T15:09:36.514Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT gaospenta ===\"; grep -n -i \"spenta-\\s*, \\|gaospenta\\|gao.spenta\\|gaosp\" BRT.txt | head -10\necho \"=== BRT gaodana ===\"; grep -n -i \"gaodana\\|gao.dana\\|gaodayu\" BRT.txt | head -10\necho \"=== BRT gutha ===\"; grep -n -i \"guthavar\\|gu.a-\\|gutha\" BRT.txt | head -10\necho \"=== BRT gaetha ===\"; grep -n -i \"gaetha\\|gae.a-\" BRT.txt | head -10"
}
```


### [2026-09-06T15:09:36.619Z] TOOL RESULT

```
=== BRT gaospenta ===
2782:{upa  mit  Akic.);  para  n  *gaosp}nta  ...will,  cupiti  potens,  glücklich':  am^rstäiti baodasla  urvän^mca  */rai^ämahi  nazdista  '■  *asaonö  urvä  °sö  "in  Ewigkeit  (wird)  die upa  >war}sta  raoca  V.34.  [Seele    des  -4Aanhängers    glücklich    sein"
8245:•  J->  S->  P-  UP^  1)  Praea  i)  mit  Akk.; a)  räumlich,  a)  "hin  -  zu':  mi%r)m  yO  .  . fravazaiU  Aaea  karsvar»  yat  arjsaAi  'pa karsvar»  yat  ifaniraitm  Yt  lO.  67;  — "iräyS  °pa  naz'a.paötm  (sd.)  asatUi ..bar^is V.9,11;  Vd.J2;  —  ui'trö  .  .  yS  kapm aipi.spayeiti  spaeitit^m  upa  vayoan»ni Auxmao%re  (sd.)  .  .  YL/4.13;  — para  te gaosp^nta  .  .  hao^asca  . .  *fraisyämaAi  naz- dista  upa  . .  raocä  . .  P.  34.  ß)  'bei, an':  ipanS yöi  hislmte  a:^arö  °pa  ^^anntjm V.  13.28;  —  tqm  yazata  ..  °pa  zrayi^ vouruJcaam  Ytf.iiö;  33,  38,  54,  72,  76, /2.16,  /5. 19,  27,  31';  —  *"/a  *mailUn (sd.)  barfsatiham  ^.3.20;  —  at-a  tu  anya mays  äitt  (sd.)  JasOit  .  .  paoirim  °pa mayiin  ..  tanüm  pairi.yaozdai^ita'^ .<).^\; 31',  Ö.38,  5.54;  —  minum  bara^ ..  aridvl
10132:;  V.  ig.  41,  Yt  ig.  60';  —  n;imasj  « gaosp^nta^  tumas?  U *gaoAu}ia^^  ^>  V.  2A1, *V.34;  —  y!  . .  yazai  (sd.)  apa  . .  'iulcä västrät  acistsm  mantüm{sd.)  Y.^.  4;  — US  Sus  stuyl  täyäatcä  AazanAatcä  Y,  12. 2;  —  aipi.jatS {sd^  'am  Auhaf>A»m'>^  yai^a ra^aaiä  V.ij.^s; — yat .  .  Aainqm  ava- zSit  ..janyät*n»rSus  para  'am  asSitvar»- iqm  V.18.13;  F. 21;  —  xmmTm  'aus  yä canranhäxl  varaihlm  pantqm  azaite  Yt. 10.  38;  —  jvS  äp?m  jainli  Stram  fräva- yeiti  'am  *var)tqm  azaite  V.5.37;  —  al tsng  dngvä  ySng  alaAyä  vazdrfng  °ä  frU- ntffi/{sd.)  /JiiraAyä  .  .  Y.46.4;  —  nSii ..  karapanS  vSsträt  ar?ffi(sd.)  °avöi  äröis ä  *sfndä{sA.)..yi  Is' ilttgAs ..  Y.51.14;
13299:•  j.,  g.  dätar-  :  dahr-  m.j  j.  däJhri-  f. i)  'der,  die  gibt,  schenkt',  mit  Akk.  der Sache  und  a)  Dat  der  Person:  lumasp  te gaosp?nta  .  ,  'ärö  baxlim  (sd.)  . .  asaone V.  2J.  1  '>;  —  ava.jasa  aridvJ . .  avaahe  . . aridrai  yazimnäi  jaloyanfäi  '>ri/  (NSf.) äyapfym  VL5. 132;  19;  —  JravaSayB  .  . _>'S  °^rf/  (NPt)  v;irjimm  siayaite..  "^ris tiAmSi  voku  x^annS  yS  .  .  Yt  JJ.  24; 24'.  ß)  Gen,  der  Person:  asi (VSf.)  vohOm  i^annö  assqm  narqm Yt.  i-j.  6  *>.  2)  'der  schaffend  hervorbringt, Schöpfer'  von  jiAM.  und  den  AmSp. a)  mit  Gen.  des  Objekts:  aÄura  matda  .  , °tar>gat&anqin  astvaiiiftqm{Stw^iz.)asaum Yt  1. 1  usw.;  —  ahur)m  mazdqm  . .  °tärim vokunqm  dämanqm  Y.  16. 1 ;  —  azim  yö almrö  masdä  azim  yd  'la  vaithvqm  V. 22.  i;  — p»-3sal  zardhusträ  a/iur?m  maz- dqm: *°tar»*vaiikvqm^''  aAura  mazda  V. ig.iT,  verwendet Vyt. i'O ;  —  atmsä  spuita ..  vokunqm  VdrJ  Y.  65. 12;  Vr.  ;7, 12; aiimanam  spmlanqm  .  .  ysi  funti  Snhqm dämanqm  yal  ahurake  mazdä  'tarasca inanxslarasäi  .  .  Yt  ig.  18;  —  azSm  täii "iwä  fraxsnlisA)  auäml  masda  .  .  vispa- nqm  'tänm  Y.  44. 7 ;  —  'tä  artÄJus  andat .  .  hati^y5var?stqm  (sd.)  Y.  ^o.  1 1'*;  —  'tä xratSu^  .  .  räzSng  .  .  sähli  (sd.)  Y.  S'^- 6'*.  ß)  absolut,  von  AhM.:  taha  dim ahurS  mazda  avqn  (sd.)   'ta  Yt  8.  7
14460:idswyilHim  FrW.  2.  i ;  —  'naAe  ithwyanBif Vt./j.i3i,  *FrW.2.i,  3i  —  vm pu'^rff ähwyanSi!  vXsS  sarayä  'nö  Yt.5, 33,  17. 35;  —  vartnfm  yim  cahrugaospm  yakmäi tayata  'nB  Janta  aSsis  i/aAäiät  V. /.  17; —  'rur  yS  janal  aiim  äahäk^m  Y.g.jt; Yt.  j^  40,  lg.  9a ;  —  'ftSyat  äs  masyanqm ..  wrüravastimö  ..  Yt/9.36;  Az.2;  — päurvö  (sd.)  .  .  yal  dim  usca  usdvanayaj Vfrf%rajä  taxtnS  'ne  Vtj.  öi;  —  tl  ySi pü^ra  'nahe  F.4C
25637:—  s.  noch  Anhang.  b)  im  jAw.: 'uns  .  .  pasukanqm  .  .  äaiiikanqm  Yt  /J. 74;  —  aäahe  udraAe  .,  daAm?m  'vän^m V.y.  55;  —  neben  öaiKaA-''^:  para  a *gaosp)iita  baedoila  'värumäi  *fral^ämaAi P.34.  3}Anhang.  Die  Seele  des  Urrinds (s.  sgav-  m)  als  Gottheit",  im  gAw.  und jAw.:  atcä  gSus  'vä  raottä  (sd.)  Y.  2<).  9; I ;   —    ai  va  ustaniiW  (sd.)  aAva  sastai!
26985:—  aurvants  . .  'ta  vihvanhe  Y,  57.  3  7 ;  — 'ta  fradaxlta  nurr/a  Y,  ;o.  1 1 ;  —  mmasi ti  gaospmta"^  ..  *gaohi^ii"^  V,2/.i;  *P. j^'3)j  —  wertlos:  garB  *tühe  mmäne yat srlr»m  VyL  iS.
26986:KoDipA-i  Ableit  —  VgL  tpanyak;  sfiSniila-; ferne»  sfiSnai-'i>.  —  ksl.  svf/ü,  |[l.  in/tfilas 'heilig';  np.  vgl.  aspand  'Rtute'  (wozu  Hbu. AGr.  /.  Vji).  —  Pü.:  irmsümk,  Sü.:  mahalla- rai ,  mahallamah ,  gumlarak ,  auch  makän, ti^däkiki  s.  noch  No.  1-5,  S,  la  —  ')  Pü.: atozünlk  bavandak  mcniln  oder  spandaramal. —  i>  PQ.  I  sfieiiäk  (Sü. :  ma/iallarak)  meniiJi.  — 3)  Pü. :  ta  fa  ahräilh  awiäyenet  (Sä. :  fta- vardhayati).  —  4)  Pü.:  pa  an  i  ei  ewiäye- mtär  [Sä.:  firoT/arMayiat^)  marl,  —  S  PB,; pa  ,.  ojosäyFnÜH,  SQ.:  /j-tiiilatayä,  —  *)  Hds. ärPiaUilea  spiilasia.  —  7)  Hds.  spmlahcca ärmalSis.  —  *•)  Pu.i  amahraspand,  —  W  Hds. 'Om;  %,  vor-  nnd  nachher.  —  "*)  Pü.: mänsr  spand.  —  ")  Hds.  "/i.  —  ")  S.  S^'fl!/- No.  8.  —  '3)  Hds.  gaospinla.  —  'S  Die  Wörter setzen  eine  Basis  auf  (ar.)  -an  voraus.  Dass Gdn.  VSt.  3.  33,  SPreussAW.  ig.  433  und JN.  GlrPh.  3.  633  wegen  Pü.  aiiaiitiTi  sich neuestens  wieder  '.  dam  verstehen  konnten, ipjHia-  von  lit.  saifiUas,  ksl.  svftä  losiu- reissen,  ist  mir  nicht  begreiflich.  Wenn  dem awest.  spinia-  eine  andre  Bedeutung  als  'heilig' inkommen  sollte,  so  mijssie  es  eine  Bedeu- lungsverschiebung  oder  eine  Umdeutung  er- fahren haben;s.dazuBB. /;.6i,  IF.J.161N0.3. Das  ist  aber  nicht  der  Fall.  Ohne  die  Über- setzung annünii  würde  Niemand  auf  den  Ge- danken kommen,  spinta-  anders  als  mit  'heilig' wiederzugeben,  das  überall  vorzüglich  passt; sie  ist  wohl  insbesondere  durch  V.  51.  zi veranlasst  worden,  wo  wir  es  vielleicht  mit einem  Wortspiel  zu  tun  haben.  Die  Annahme, das  Wort  spjnta-  bedeute  eig.  'vorteil-,  gewinn-, heilbringend'  (Jn.  GlrPh.  2.  Ö35)  nimmt  doch auch  auf  dessen  Bildung  nicht  die  genügende Rücksicht.  Dass  awzünii,  np.  afsüdan  etymo- logisch mit  den  awestischen  Wörtern  nichts  zu schalTen  hat,  steht  fest,  trotz  Cdn.s  gegen- teiliger Meinung;  5.  sav-  No.  3. j.  spittlama  P.  44:  lies  spilama. •  j.  8pfliita.mamyav-  fem.  Adj.  'die Worte  sptntä  mainya  enthaltend,  damit  be- ginnend'; yufAäitisisd.y  Y.^jÜberschr.;
30287:n  gaospmta..*gaohula''^  (:y%.)Y.2i.i;Y.  .  j.  hu-pairi'tan- Adj. '(sich)  wohl  hcrum-
=== BRT gaodana ===
4006:—  Vgl.  gaodana-.  —  Pü.:  transski.  (als  EN.).
9788:•  j.gao-dana,  °jiana-  n.  1)  'Milchgeföss': frä  tl  Aasaanm  xam  aam  . .  frasnaymi ''.an?m  avi  hatUaiinh  ya^  asti  puirake >rims"^e  tausend  Quellen,  die  zum  Milch- gefiss  zusammenfliessen,  das  die  Nahrung des  Kindes  ist"  V.  21. 7  ".  s)  überh. 'Gcfäss,  Napf,  Schüssel'  (nur  Komp.,  s. N.  64).
14930:8^9  '*'paiti£a.gaodana-
14931:•  j.  *paitida.gaodana-''  Adj.  'verschiedene
15005:•  j.  pattina- Adj.  (fem.'nj-)  i) 'verschieden, gesondert':[°nam]"  hämcj^ariha  *pailiia.- gaodana  (sd.)  *nam  alte  *xläudrini  tao- '^ram  darsis  hamqm  päpthwqm  N.  64't 64'-  a)  ASf.  °nqm  als  Adv,  'diverse' (nur  Komp.).  2)  'einzeln' :_yjini^  ahmst yämanqm  'nqm  sairinqm  (sd.)  aSaval  .  . V.Ä8s;  — yavat  ahtnäi  'n
15007:•  j.  paitinqm.  gaodana-  Adj.  'verschiedene Schüsseln,  Näpfe  benützend,  aus  ver- schiedenen Schüsseln  trinkend':  paitinam.- i^ariia  (sd.)  'na  (ND.)  N.  64.
15009:•  j.  paitiniiin.x''ar99'a-  Adj,  'verschiedene Mahlzeiten  essend':  '^a  (ND.)  paitinqm.- gaodana  paitinqm  alte  *xsäudrim  tao^ram baräto paitinqm  päpi'iwqm  "(zwei  Männer) die  verschiedene  Mahlzeit  essen  und  aus verschiedenen  SchÜsseht  trinken,  sollen  . ." N.  64;  —  °&a  ksmsgaodana  N.64.
29860:•  j.  bämö.gaodana-'>  Adj.  'die  gleichen
29867:•  j.  hämö.x*ara9«-  Adj.  'die  gleiche Speise,  Mahlzeit  essend':  yä  nara  •>« (ND.)  ham5.gaodana  "zwei  Männer,  die  die gleiche  Mahlzeit  essen  und  aus  den  gleichen Schüssehi  trinken"  'a.64;  64.
=== BRT gutha ===
9871:•  j.  gaoz-,    p.  gaud-    V.     'verberget Praes.  4   gusa-,    24   gutaya-,    30  (Iter.) gauiiayot,
9880:•  j-,  g.  gaoS-  V.  'hören'.  Praes.  i  gus-, 3  gäid-,  30  (Kaus.)  güsaya-,  —  PPfP. 'guäa-.
10391:'  j  guSa-  m.  Name  einer  Abzweigung, ;ines  Seitenarmes  der  Ranhä:  Um  yazata .k3r?säsp5  upa  -Mm  apay:är>m  rankay^
21281:mit  Lok.  der  Sache:  f?rasaosträi  urvO- sistqm  (sd.)  aioAyä  da  sarSm  , .  maibyS^ yqm  (AS.)  vaishäu  "kiwahmX  3  xsä^rfft "dem  I-'r.  gewähre  .  .  und  mir  den  Ge- winn   des   Guthabens   in   deinem  Reich"
23340:—  I)  Pa  (für  z'-  u  o  d  in') :  vahuman.  —  ■)  Oder aach  in  D  b;  t.  Sp.  1396  m.  —  1)  Als  neulr. Sublt.;  vgL  Sp.  1398  o.  unter  OB.  —  t)  Fii.: S  a  I  viA  tan  ßSisn;  t.  iaf%-  No.  4.  Vgl. No.  7  f.  —  S>  Pü. !  3.  unter  'manaA-,  —  6)  Pü. : vaAuman.  —  7)  PS, :  virariln;  vgl.  No.  4,  8.  — ')  Pü  :  i^AU.  —  9)  Das  den  beiden  tingula- lischen  matk.  Substantiven  j'osna-  und  nahma- gemeinsame  Attiibut  steht  im  Dual  des  selben Geschlechts;  s.  No.  II  und  ta-  No.  5.  Gdn. in  der  NA.  zSt  will  den  Text  verballhornen.
24070:•  g,  vl-dätay-  f  'Verteilung  auf—,  Ein- weisung in  — '  (Lok.),  mit  LS.  vaaAäu 'Einweisung  auf  das  Guthaben'  (in  gutem und  üblem  Sinn),  wie  es  sich  beim  Ab- schluss  der  Buchungen  (dä'ira-)  ergibt''; nur  in  eschatologischem  Sinn:  ^wa  ä^rJ suxrä  mazda  vanhau  'data  (LS.)  ranayS (sd.)  "wenn  durch  dein  rotes  Feuer, o  M.,  das  Guthaben  der  beiden  Parteien verteilt  wird"  Y.JJ.  19;  —  tä  da  spfntä mainyü  mazdä  ahurä  ääirä  vanhSu  °däi- tlm  ränBibyä  (sd.)  "durch  diesen  heiligen Geist,  o  AhM.,  mittelst  des  Feuers  wirst du  die  Verteilung  des  Guthabens  für  die beiden  Parteien  vollziehen"  Y.  47. 6.  ]
26369:•  p.  suguda-,  j.  suj-Sa-  Adj.,  be- zeichnet ein  Volk,  'Sogdianer'  (nur Komp.).  a)  Sing,  (koll.)  für  Volk  imd Land:  Wimä  dahyava*  tyä  manä  pati- yäi/a'  . .  bllxtri¥  'da*  . .  "..  Sogdiane  . ." Bh.l.6;  D.5.  2,  7.3;  —  yahmya  apB  .  . %waxsfnte . .  gaomca  *sirfiim  '>  x^äiriz»m&i Yt  10. 14.
27940:yim  'rpm  nqma  ..yim  maiyäka  avi  duiva- ^avJtS zairimyaksm^&A.)  nqma  ao/ai/e"dcn Dasva  Z.  mit  Namen,  den  die  Übel- redenden Leute  Z,  nennen"  V.  13.  ö. Komp.;  zairimya-  +  *a/mra-  'des  Glieder  (oder Zehen)  in  einem  festen  Gehaus  stecken';  a  in der  KompFuge  statt  £  (bi.  i,  %  sgS.  ^),  %  36S. 3  b.  *aoura-  (statt  'angura-,  %  268. 47  c)  m. 'Glied'  oder  "Finget,  Zehe';  vgl.  ai.  anga- n.  'Glied',  aiigülof-  f.  'Füiger,  Zehe';  woss. ong  'Glied',  änguljä  'Finger*.  —  Vgl.  ioirim- yäia:  —  ai.  vgl.  harinu/a-  m.  'Schildkröle'.  — Pü, :  transskr.  [larimangur),  Npü. :  läi  fait.  — <)  Sa  nach  Npü.  nnd  Gü. ,  deren  Angaben von  der  Etymologie  nnterstätit  werde«.  GcR. OK.  160  denkt  vielmehr  an  den  Maulwurf. S.  noch  Sp.  Komm.  i.  297.
=== BRT gaetha ===
15573:*   y   mä    ht  bansma  pairiMsntsm  (sd.) pairlkgrantiS  ,  .  V.  ig.  ig:  — ?— . g.  pairigae*a-  n.  'Umfassung  des  An-
23470:•  j.  väiti-gaesa-  in.  Name  eines  Gebirgs*>: ; akmal  hala  garayS  fraexsyan  . .  dvadasS  j 'SS  Yt  ig.  2.
29410:zu  vispp.gaena-.
30163:P&. :  mSi  pa  kandämän  yui  kac  an  i  pa  sar ; vcrmullich  eine  Eiläulening  lu  'gaena-  im Gegens.  lU  var^sa-  (td.,  No.  2).
```


## [2026-09-06T15:09:50.250Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Unrat/Kot ===\"; grep -n \"Kot'\\|Unrat\\|'Kot\" BRT.txt | head -10\necho \"=== BRT gaetha- Besitz ===\"; grep -n \"gae\\.a-\\|ga%a-\\|gaeftä\\|Habe.*Vieh\\|lebende  Habe\" BRT.txt | head -10\necho \"=== CHEUNG gaub / nihuftan ===\"; grep -n -i \"nihuftan\\|nihumb\\|gaub\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T15:09:50.334Z] TOOL RESULT

```
=== BRT Unrat/Kot ===
3889:kackt',  sva.)  'er  "besudelt  mit  Kot':  yezi anhat  ..  aiwi.ir'  v3  ami.vatitim  {sd.)  vä
10392:;  •  j.  gül^a-  n.  'Schmutz,  Kot'.
19689:•  j.  matgü'ihi-  Adj.  'mit  Unrat^  Kot  be- haftet, unrein':  nasaum  '^am  V.J. 25.
20580:•  j.,  g.  mü'ÖTa-''  n.  'Exkremente,  faeces': '■%r3m  F.  11;  —  aitaKhani  astamca  .  . spämamca  (sd.)  '^ram^' {GV.)  'v.6.j; 29.  a)  sva.  'Unrat,  Unflat':  iadn  apn 'hrym  akyä  *madakya  (sd.)  ^.48. 10.
25476:•  j.  irimant-  Adj.  (fem.  'maiti-)  'mit Unrat  angefüllt':  bagvan  mayanqm  'maiti- nam  .  .  aipi.ianyat  V.  14.  6.
25477:'Durch  Haplol.  (S  jotf)»)  aus  *irimaimanl-; *irima.  (d.  L  irima-,  S  a68.  1)  m.  "Kot,  Unrat', »um  V.  ray-\  vgl.  np.  rim,  nbaL  rrm.  —  Pg.: may  /  rem.  —  ')  Vgl,  xstävant-.
=== BRT gaetha- Besitz ===
8342:—  kirPS3spas(a  . .  'ryS  yava  gaisus  ga%a- varö  Y.p.io.
=== CHEUNG gaub / nihuftan ===
575:etc.). Examples are *caxs ‘to drip, sip, eat’, *fšar! ‘to shame, be ashamed’, *gaub ‘to 
2019:*OLD PERSIAN: ? Gaubaruva <gubr"uv-> PN 'cattle-eater' = Kent: 182b 
8188:*gaub 113 
8221:*gaub ‘to say (positively/negatively)’ 
8223:*OLD PERSIAN: gaub- (med.) ‘to call oneself" = Kent: 182b 
8225:MED.; Pres. them.: IND. 3sg. gaubataiy <g-u-b-t-i-y> (БВ 2.21 |, DB 2.31, DB 2.51, etc.), impf. 35р. 
8226:agaubatä <a-g-[u]-[b]-[t]-a> (DB 1.84), <a-g-u-b-t-a> (DB 1.93, DB 3.35, DB 3.55), <a-g-u-b-t-a> (DB 
8227:2.66), <a-g-u-b-t-[a]> (DB 3.89), 3pl. agauba”tä <[a]-[g]-u-[b]-t-a> (DB 2.93), SUBJ. 3sg. gaubätaiy 
18197:by the other roots for ‘to speak’, *џаќ and *gaub respectively, in the other Iranian 
24034:*MIDDLE PERSIAN: (+ *ni-) MMP nhwmb-, BMP nhwmb- /nihumb-/ ‘to hide, 
24041:nhwptg, nhwpt, BMP nhwpt, caus. BMP nhwmbyt /nihumbid/; Caus.: pres. IND. 3sg. BMP nhwmbyt 
24042:/nihumbéd/ 
24048:*ni-) NP nihuftan ‘to hide, conceal, cover; to conceal oneself ...; to be beautiful (!)’ 
34051:gaub-, 113 
34052:Gaubaruva, 12 
35383:nhwmb- /nihumb-/, 368 
41203:nihuftan, 368 
55340:*gaub (s.v.), *ndz (s.v.), 
55471:*gaub (s.v.), *Hraz (s.v.), 
55503:*gaub (s.v.), *Hraz (s.v.),
```


## [2026-09-06T15:09:52.819Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24010,24075p' CHEUNG.txt"
}
```


### [2026-09-06T15:09:52.880Z] TOOL RESULT

```
Pres.: IND. 3sg. BSogd. swnpt, OPT. 3sg. MSogd. swmbyy; Fut.: IND. 3sg. MSogd. swmbtk’m; Partic.: 
perf. pass. BSogd. swBt, CSogd. "swbty ‘pierced’; Inf.: pret. MSogd. swBty 


*CHORESMIAN: snb- ‘to pierce’ > Samadi: 184 

*NWIR: NP suftan/sumb- ‘to pierce, bore’, Bal. supt, sumbit/sumb-, (EHB) 
subt'-/sub- ‘to pierce’ (< NP ?) 

*NEIR: Pash. suräy, Wa. sarv ‘hole, cavity’ (< *subra-), ? Sh. surv, Rosh. survak (f.) 
‘tick infesting cattle’, M. surv, Yi. surv ‘hole’ 

*SANSKRIT: ? Skt. svabhra- (n.) ‘gap, vault’? > EWAia II: 675 

© The root appears to be Ir. The connection to Skt. svabhra- is doubted in EWAia, 
l.c. An IE etymology for Ir. *su(m)p/b cannot be found. 


“PIE LIV: — | Pok.: 
*REFERENCES: Horn 1893: 163; EVP: 69 f.; IIFL II: 248a, 540; EVS: 75b; Steblin-Kamenskij 1999: 324; 
NEVP: 76; Shahbakhsh: s.v. sumb-; Korn 2005: 318, 382 f. 


*su(m)p/b? ? ‘to make up, "beautify"” 
*MIDDLE PERSIAN: (+ *ni-) MMP nhwmb-, BMP nhwmb- /nihumb-/ ‘to hide, 
conceal, cover up, guard’. > Cf. Henning 1933: 200: "Viell. sub, ap. *00Ь = ai. 


sumbhati ?" = DMMPP: 242a 

Pres.: SUBJ. 3pl. MMP nhwmb’nd, nhwm’nd, IMPV. 2sg. MMP nhwm; Partic.: perf. pass. MMP 
nhwptg, nhwpt, BMP nhwpt, caus. BMP nhwmbyt /nihumbid/; Caus.: pres. IND. 3sg. BMP nhwmbyt 
/nihumbéd/ 


*KHOTANESE: Khot. suraa- ‘pure’ 

*NWIR: ? NP sufrah ‘anything on or in which victuals are placed’, table-cloth’ || (+ 
*ni-) NP nihuftan ‘to hide, conceal, cover; to conceal oneself ...; to be beautiful (!)’ 
*MISC: Arm. (LW) surb ‘holy’ 

*SANSKRIT: Sobh ‘to be/make beautiful, make up, adorn’ (RV+) = EWAia II: 657 

© The root is Пг. only. Arm. sourb is probably a LW from (unattested) MIr. *subr, 
for which an ЕП. cognate, Khot. suraa-, can now be cited, on which see Emmerick, 
EVS Ш: 155. 


*PIE — — LIV: 330 | Pok.: 594 
*REFERENCES: DKS 1979: 427b f.; Werba 1997: 381 


*suah ‘to pant, wheeze’ 

*CHORESMIAN: ? s’s- ‘to pant? => Samadi: 178 f. 

*NEIR: Pash. sün ‘sniff, snort’, Sh. say(d), Bart. sawn name of a demon (*ѕи$па- = 
Skt. susna-) 


*suaH 369 


*SANSKRIT: Svas ‘to bluster, hiss, snort? (RV, AV+) = EWAia П: 677 

9 It is uncertain whether the Chor. form s’s- has other cognates: it may well have an
```


## [2026-09-06T15:10:12.036Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT gaitha ===\"; grep -n \"gaiθā\\|gaita\\|gai0a\\|gaithä\\|gai%ä\" KNT.txt | head -10\necho \"=== SOD gydh ===\"; grep -n \"gy8h\\|gyδh\\|gydh\\|ɣyδh\" SOD_pages.txt | head -10\necho \"=== SOD herd ===\"; grep -n -i \"herd,\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T15:10:12.121Z] TOOL RESULT

```
=== KNT gaitha ===
=== SOD gydh ===
=== SOD herd ===
```


## [2026-09-06T15:10:15.612Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT gai ===\"; grep -n \"^gai\\|gaiθ\\|gai8\\|gaiba-\\|estate\" KNT.txt | head -20\necho \"=== SOD file check ===\"; wc -l SOD_pages.txt SOD.txt; head -30 SOD_pages.txt\necho \"=== SOD grep herd ===\"; grep -n -i \"herd\" SOD.txt | head -20"
}
```


### [2026-09-06T15:10:15.690Z] TOOL RESULT

```
=== KNT gai ===
5340:gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
=== SOD file check ===
  45615 SOD_pages.txt
 111423 SOD.txt
 157038 total
 SOGDIAN
DICTIONARY
Sogdian - Persian - English




      B.Gharib




   FARHANGAN   PUBLICATIONS
Sogdian Dictionary (Sogdian-Persian-English)
by B. Gharib
editorial supervisor: A. Mansouri
editor: S. Fotouhi
© 1995, Farhangan Publications
2/52. Shahid-e Said Street, Tehran 15916, Iran.
Tel: 6460069. Fax: 670230

ISBN: 964-5558-06-9
4f*Jj*l{^ 0"J-^8 'Jy^**-             ^J>*4^ tfW : j' a>„J^ <f jljX-U^ -LUi^-L ^JjJ'j^ L» e jlf ijj-
                                                                • l^> o-^ jl ^^<o (j ^jb^b             j uij^- ^C*"
                  ;l_^0 jL-u jlS' 4$" (.5*^-*^' "^^   (H^- fJ




                                                                                                                   L?JJ J'
=== SOD grep herd ===
5240:potsherds  with  Sogdian  inscriptions  were  found  in 
21706:herdsman 
51710:pasture,  herd 
81129:shepherd 
90373:herd  6541 
90375:herdsman    2128 
93590:shepherd  10790
```


## [2026-09-06T15:10:21.095Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '51700,51720p' SOD.txt\necho \"--- context 6541 ---\"\ngrep -n \"6541\" SOD.txt | head -5"
}
```


### [2026-09-06T15:10:21.164Z] TOOL RESULT

```
from  sin) 
Sogdica.  3 

6540  p'tk'   B  =*  p>t»k     ' 

6541  pJtk3   B  cArt\&*^i(tjl:J^S)&  c>€\jTirjy> 

*   ?& 
pate 

pasture,  herd 
Frag.  18.2  apud.  S  W,  IIJ  1976,  63 

6542  p*tqwny   C  J^~j  ^ 
patak-une,  patakoni 
protection,  vigilance 
C2,  31R6,  10,  57V4  p72-3;  BSTii  892.6,  905.4 

6543  p'tp's   B 
patpas   ^p^p'y'k 
respected 
--- context 6541 ---
51705:6541  pJtk3   B  cArt\&*^i(tjl:J^S)&  c>€\jTirjy> 
90373:herd  6541 
92432:pasture     3250, 6541
```


## [2026-09-06T15:10:27.547Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD printed p.180 (leaf 246) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==247' SOD_pages.txt | head -60"
}
```


### [2026-09-06T15:10:30.028Z] TOOL RESULT

```
=== SOD printed p.180 (leaf 246) ===
  181

        Lett. 5.30; Yydfip, Hen. BBB p63.523; BSOAS                   TSP 2.494 etc.; STii 7.5, 8; BSTBL, Intox. 12, 20,
         1965, 246                                                      29; Hen. Tales. 475.14, 28; Yyr'k, SCE 394; pi.
 4525 yymr B                                       >V
                                                                        Yyr>t, SCE 260                            vyyr
      y/ximor ?                                                  4535 yyr'k »sk'r- B                o^«>*-^ ^Ixlo-*
      thin
                                                                      xere-oskar-
         TSP 6,87 n p204
                                                                      OcOmake a fool
 4526 yyn{>) B                                         O'^jj          SCE 251, 267
      y/xen ?
      conscience ?                                               4536 yyr'y =* yyr'k
      VJ 1030                                                    4537 yyrtr                                     j^cj^
                                                                      ye/irtar =>yyr
 4527 yyntwh B                               ^i~(<^>/-i0              later, afterwards
      xintu ? (xynt) ©MP xyndg                                        GMS 1285, 1667; Hen. Tales. 473.5, 486.14; BBB
      (a kind of)\\\ness *                                              c8 f 12, 32; TSP 12.65, 14.21; MDii; BSTi 71-7;
      TSP 2.35 n pl69                                                   Bcnv. Et. 1.302; MSP b- 134
4528 yyp6      B, S     j->)(^bj' jT jl «y JU <ju <->>- <o^     4538 yyrtrcyq     S                                */ j>*

        xep9  (xyp6)   ©<Av. xvae paidya ©pi. -f(y)                   ylrtarcik
                                                                      late
          =»xyp5
                                                                      C3 apud. Sund. MSP p46
        own, self, his
        EGSii 120; GMS 139; VJ; TSP; BSTBL; SCE; STii;          4539 yyry =» yyrJk
          Frag. Len.; Sogdica. 60.6; YypSh, MDii;               4540 yys'yph S =» yysp
          YypSwy Dhu. 276; Yypdt, GMS 1250, 139 n 1;            4541 yyscWk       B                    4,1.^ <c~J <Lr~J-
          Yyp5\ W-Li: Gropp. p39                                      yiscanc ? (yyscnk, yyscn*k) ©<*grsti; A v.
4529 yypa'w'nt B, S                             vGjl <jUjUi.          mean,  stingy
                                                                        gdrdda   (naka) ^yytcny'krKyh)
     xepOawand ^xypS^nd
     Lord, master                                                     TSP 8.194; SCE 46; GMS 382 n 2, 1021;
        TSP 7.102, 118; Hen. Tales. 468.33; MDii, -w                    Schwartz. BSOAS 34, 1971, 414; Yyscrikw,
4530 yyr B, S                                                           Frag. Len. 120, 6
                                            oIwOUj^^
     yi/er ? (yyr) =*yyrtr                                      4542 yyscn'k *» yysc'n'k
     late
                                                                4543 yyscnk M =* yyscWk
        EGSii 158; VJ 205; TSP 2.446, 1163, 12.40; Frag.        4544 yysp C                                     v^^j
          Len. 39.1; Yyrw, VJ 115; Yyyry GMS 1285;
                                                                      yisip, yesip (yysyp, yys}yph) =»yy5rp
                                                                      damage
          YyrK VJ 274; TSP 2.411 n pl74
4531 yyr- B, S                        j.b^^af^                        STi 14.15; Benv. Notesii 424; GMS 298; BBB 523,
     xer =»yrt-, yr-1, xyr-, y'yr-
     OeOgo, 0<?)pass, GcOcross, (ro)transfer                           706 b22; MSP b3; Yysypw, Hen. Tales. 480-30
                                                                                                              l y_^s
     SCE 540; VJ 1036; BSTBL, Vim. 4, Dhu. 49; Hen.             4545 yystrVy    B
       Tales. 475.15; W-Li: Gropp. p39                                xestrawe ? ^xwstry*
4532 yyr»k B -» yyr'k                                                 veneration
4533 yyr^kwn'y B                                                     TSP 6.70
     xerakune, xirakoni                              J^\y?
     foolishness                                                4546 yysyp M =» yysp, 'yws'yp-
        TSP 5.108; Hen. Texts. 731                              4547 yytcny'khCyh) B                        LT-i 'iJ^jJ
4534 yyr>k    b, S                                     i*j\ ■        yitsanyak(ya) ©f. n. ^yyscWk
                               (<j>>>~' >>)«y <
                                                                     meanness, stinginess
```


## [2026-09-06T15:10:36.379Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==246' SOD_pages.txt | head -70"
}
```


### [2026-09-06T15:10:38.658Z] TOOL RESULT

```
                                                                                                                   11



                                                                                                                   (J*


  ywys-
       east, sunrise                                         4512 ywy z*k(w) B           >^    j->)Ji-^ «U «j*r- «*=-W^
       TSP 17.4, 16, 20, 26, 31, 3.144; Hen. JRAS 1944,
          138.20; Frag. Len. 82 a 26                              xwezak(u), x5yze ? (ywzky ) ©adv.
                                                                  very, very much, extremely
  4503 ywys- B                          o>/is^'o>/3S
                                                                  GMS 234; Bcnv. Notcsi 36-7; BSTBL; VJ; TSP;
        xwes, xoys ©<Av. xvisa—, *xwisa\ MP xwyd
                                                                    SCE; STii 7.33; rwyz'w, VJ 1044; STii 7.30;
        OcOperspire, Go)sweat                                       BSTBL; TSP 6.40, 50, 62
        GMS 228, 539; TSP 2.295; Hen. Texts. 718;
          Bailey. Prolexis. 23; S W, MIS 1984, 206; AVS      4513 ywyz*y =* ywyz*y
          71                                                 4514 ywz- B,S                                      ^^
                                                                  xoz (ywz-) =^ywst-, xwj-, xwz-, ywyz-
  4504 ywyst    S(MD) ** ywycst
                                                                  (fo)demand, (f<?)wish
  4505 ywyst'k B, S              ^j^a i(jU* <*j&>J t^j            TSP 5.107, 13.13; BSTBL, Dhy. 40, 74, 145; Frag
       xoyste, xweste (ywystk) ©<Av, hvoista; Khot.
                                                                    Len.; MDii; trans, pret. VwStffir-, VJ 1077; l*L
         hva$ta\ Oss. xistan Munj. xusci =»xwsty(y),
                                                                    >Ywsty, Frag. Len. 93.36; AVS 138
         ywycst, xwystk
       chief, superior, teacher, honoured                    4515 ywz- =4 ywz-
      _ GMS 230; SCE 92; BSTBL, Dhy. 7, b9 etc.; Intox.      4516 ywzky B =$ ywy z*k(w)
                                                             4517 ywzn M                                          j^
          32; TSP 5.59, 8.200, 17.22; MDiii; Bailey.
          Prolexis. 435                                           yawazn ©<Av. gavasna ©ob. -yh -^wzn
                                                                  deer
  4506 ywystk ==» ywyst'k                                         GMS 375, 1230
  4507 ywystr B, S        (J>> y-t-x j->)j^jj* «>j;l>J t^j   4518 yy C                                             ^%$
       xoystar, xwestar ©<*xwa(y)ista-tara ©nom.
         ob. -y, -w, ->; pi. -t; ob. pi. -ty =*xwystr             and, also
       chief, superior, head                                      Yl/8?4.5, 10, 5, 21 & etc.; BSTi 61 etc.
                                                                  STii
       GMS 230, 1301; VJ; TSP; BSTBL; SCE; STii 7-40,
                                                             4519 yy- S                             cp/^^/^
         8.3; -/z, VJ 1506; -w, TSP 2.180; -y, SCE 128;
                                                                  xi, xai ©Oss. xai
         -\ SCE 478; TSP 5.74; Dhy. 15; -\ SCE 8, 9.8;
         MDii; Frag. Len.; S W, MIS 1984, 207; pi.                (to)divide, (fo)part ?
         Ywystrt(h), TSP 2.190, 632; Dhy. 163; ob. pi.            MDii p33.4; Gersh. Advice. 91
         Ywystrty, TSP 5.92, 7.172                           4520yy>ry>kh     B                              ^><J;
  4508 ywyz- B                    (oy>y^^)^j^                     xyaryak
                                                                  servitude, hired labour
       xwez, xoyz (ywyz-, ywy^-) ©<*xwdzaya
                                                                  SCE 41; Schwartz. BSOAS 34, 1971, 413
         ©inf. -Jj ^ywst-, xwst-, xwj-, ywz-, xwz-,
         xwyz                                                4521 yyS B, S              (u^^^^^.y
       demand, wish                                               xe§/9 ©<x+*y8 -*xy6, yy5h
                                                                  this, that same, then
       GMS 188; VJ; TSP; SCE; BSTBL; Frag. Len.;
         S W, MIS p207; Ywfz, MDii 2sg. impv.                     EGSii 122; GMS 1403, 1420; VJ; TSP; BSTBL*
         Ywfzym, lpl. pres. , Ywfzw, lsg. impf.                     STii; Frag. Len.

  4509 ywyz- =* ywyz-                                        4522 yygpp     S ^ yy5rp

  4510 ywyz1*? B                                             4523 yy5h B                                        ^Jf
                                                  ^j^U
       very ?, xoyze ? (ywyz^)
       xweze                                                      ye9 ? ©<OP gai0a; MP geh(ban); gih
                                                                  flock
                                                                  TSP 13ii, 14; S W\ IIJ 1976, 61
       TSP 5.93, 7.49; STii 8.7
```


## [2026-09-06T15:10:48.624Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS nihuftan ===\"; grep -n -i \"nihuft\\|nihuf\\|nhwpt\" SNS.txt SNS_pages.txt | head -10\necho \"=== Henning Sogdica p.57 ===\"; grep -n \"SOGDICA\" HENNING_selected_papers.txt | head -5\necho \"=== henning gwd / tuda ===\"; grep -n -i \"tuda\\|twdh\\|dung\" HENNING_selected_papers.txt | head -20"
}
```


### [2026-09-06T15:10:48.705Z] TOOL RESULT

```
=== SNS nihuftan ===
SNS.txt:14697:(ferfcum, 200, 7, 4) nhwpt , nhwmb- : jiU (p. 236. 
SNS.txt:14698:tnihuft Sstgd: *>i*ta VOCi.fVtfH nahunbat: {, 
SNS.txt:14704:•VtJ (^•A^],^^,«i |i! nihuftag ! S^*- 
SNS.txt:30113:nhwpt 262/12 
SNS.txt:31860:nihufSnd 286/3 
SNS.txt:31862:nihuft 262/10 
SNS.txt:31864:nihuftag 262/15 
SNS_pages.txt:10402:                                                 (tf*r.Man. II, 51)w*ng:j3i»                                         200, 7, 4) nhwpt , nhwmb-             jiU                236.
SNS_pages.txt:10406:            .^o-^-o^^                      :van 9 kardan:                     «i»tV*       ^'        tnihuft Sstgd: *>i*ta VOCi.fVtfH
SNS_pages.txt:10413:                                          .»jttSt*l£ r/toM            :vanldar:            A-v****   •VtJ      (^•A^],^^,«i|i! nihuftag                                   !        S^*-
=== Henning Sogdica p.57 ===
158:SOGDICA
898:18 SOGDICA
=== henning gwd / tuda ===
1350:“dung, manure", BBB., p. 102 (on f 8): this word still exists in Eastern Ir. dialects, e.g. Wakhi Sart manure, see Morgenstierne, IIFL,, ii, p. 521, and is attested also for Khwarezmian : irts—(2) Possibly “bridle”, from Av. aiwi.Sana- (Saka byana, Pashto mliina, te.), which, however, is By8'n (VJ., 1419), B8"nk (Dhuta, 166), in Sogdian, see Benveniste, J., 1933, i, p. 241. Or MPers. aiyanay NPers. biydnak “rushes” (‘a plant used for weaving bariys”, BQ.) ? —(8a) “Weeping.” Cf. ZIL., ix, p. 204%, "bgryy-—(38) “Flash, flame, lustre, brightness,” ete.—(4) “ Flashing, flaming," Sogd. is borrowed from Uiyur yalinéfy (yalin “flame ")—(5) Sogd. “ vehicle, chariot” (Skt. ydina).—(6) “ Unseizability, unprehensibility.”"—(6) lative of *”yrtyy, which is probably the same word as Buddh. 'ny’rtk, Vim. $1, 89 (ed. ’2y'rtk) = Chin. i tst (sce F, Weller on the passages), muddy, juicy, rich, fertile.”—(7) “ Inactively, inefficiently.” -y'- abstract of n’kt’rk (see below, 96), kt'rk Bahuvrihi compound, k(r)t- + 'rk “work, deed ”.—(9a) “ Or even.” "grye is MPers. "gr “if!” +c. suffix. The rendering " or (even) "” was probably taken from a passage similar to Mir. Man., ii, 207-4: ‘gr... 'gr... u'gr (= "grye) - ve. . . site” —(96) " Ineffective, inactive, powerless," see above, 7.—(10a) Sogd. ‘‘ damage, danger”. Hence, MPers. 'y = Av. aka- (or aya-), NPers. dk (for NP. -k, of. e.g. NP. trik from MPers. ryg)—(10b) Sogd. “ (even) if”. Hence, "gu = Parth. 'g "if" + the suffixed particle Parth. -1b, which stresses the first word of a sentence. Cf. ‘wh-b, Mir. Man., iti, and the following line from an unpublished fragment: mrd-acb mrd’n ‘frdwm 4h 'yy, ete. “Thou art the Man, the most exalted of men, the king,” ete. (M 274). Possibly -(w)b = Olt. -apit One might also compare Sogd. ‘cwty-p (ete.), if it could be established that this suffix were different from the enclitioal pronoun -f--—(Ia) MPers. “not seized”, or “ unseizable ", or, if grift here = “ crime ” (of. Air. W., 8.¥. @.goropta-), “free from crime.” Sogdian either "kiye (cf. Av. aka- “hook”, NPers. akag, akan grapnel'*2), or “xiye from *'zi- (cf. 8.7, ii, p. 515, 8.v 'nB'yidy) <*()ari- (BBB., pp. 54 sq.) “to pull" or “to draw near, attract” ?1—(114) Sogd. “‘at one time", Hence, ‘grye Parthian = Man. MPers. Agrye (NPers. hargis, ete.).—(12a) “ Arrival."—(126) MPers. “nice, splendid, magnificent,” ef. above, a 23.—(18) “ Acting in a nice, praiseworthy, decent manner” = “pious ”.—(14a) MPers. = (126). Sogd. «rat translates Syr. p'y' “‘pulcher, decorus”, seo
2358:against the rules, so that we cannot be sure whether kd is hol, If it is bud, of, NPers. kd (Arm. koit ; of. also the Pahl, transl. of Av. ydnhuya-) " stack, heap of com or dung”. For the explanation phers use NPers. tade “ heap”, which be tempting to identify with Sogd. fwéy). If it is knot =" pit, sink, dr Bartholomae once wrote & paper of seventeen pag Pahlavi words (Mir. Mund., i). But of all the vocable him only halak “foolish ” merits. consideration (for 1/r, MPers, rz, BSOS., ix, p. J. Sampson, p. 316) Other words are *harray (thus in Bal.) “saw”, *harg = Av. haroka:
2374:‘h8, beit' aheap of dung and refuse ", or" apitand refuse ". Turning
18498:‘Thanks to a singularly fortunate circumstance we can place BE@Nightae with certitude,* On his first visit to Paileali in 1911, Herafeld, after leavin Khaniqin, was compelled (by the turbulent state of the Turco-Persian frontier) to make & detour and ao travelled by way of Binhudrah, which he defined as las Gebiet der Mindung des Hulsin-flusses in die Diyilah? There can be no doubt that Binkudrak continues the ancient name, B2(@)-Nigatir.® The district lies on the direct line from Seleucia /Ctesiphon to Paikuli : the Sassanian road to
19121:dio Yashts so chorakteristischen Haufungen von sich en ein voreufgehendes Haupt- sinnwort anschlieGenden Relativsdtzen niemals vor, dad inmitten der Serie einem der Relativpronomina ein korrelatives Demonstrativ voranstinds, Ferner m@Bte die das doch ein Nominativ wire, wahrend des Satzgefge sinngemi nur einen Akkusativ zuliefe, grammatischer Nachlissigkeit zugeschrieben werden, Und schlieBlich ware a2m durchaus das falsche Pronomen; denn im awestischen (und cbonso im altpersischen) Sprachgebrauch entspricht dem Gegensatx xwisehen dem Himmel dort droben und der Erde hienieden eben der Gegensatx zwischen den Prono- minibus wa- und a&m/ima-, und gerade an dieser Stelle ist eine Verletzung des Usus um so weniger annehmbar, als die Gbliche Wendung: aom asmanam ..... mgm sqm ‘unmittelbar vorausgeht Man ist daher gozwungen, dio ursprdinglich von Geldner in Vorschlag? und spiter seiner Ausgabe in Anwendung gebrachte Abteilung der SAtze aufzugeben und aém mit den voranstebenden Wortern zusammenrulesen; also manayen ahe yada olf aém. Dies ist um so ndtiger als die tblichen Uhersetzungen keinen zufriedenstollenden Sinn ergeben. Bei den von Bartholomae im Altiranischen Worterbuch col. 1123 auf ozdhlten mit mgnayen che yas oder manayan ba yada cingol hrten Vergleichungen und Prd it wiederholt zu worden, vorausgeselzt, daB sio und dem Vergleichenden gemeinsam zugehdren; sonst aber ist ein Vergleich in allen seinen Gliedern vollstandig. Man mite daher bei unserer Stelle den Vergleichssatz auf folgende Weise aulfollen: mgnayan ahe yada vié (imam sam ata pairiéa bodve), das wire, xu! der Basis von Lommels Obersetzungt, ,gerade wie ‘cin Haus (bis 2u dieser Erde hin und um sie herum reicht)"; und das ist d°ch offen- sihtich nieht moglich Wonn wie jedoch aém in den Vergleichssatz einbezicbon, so erhalten wir damit ein rigliches Ersatswort {Or imqm zqm, 10 da der vervollstindigte Satz so lauton whrde: manayan ahe yaa vif aim (ida pairiga bodea), Hior wOrde also olf, gowil cin Nominativ, dem Himmel entsprochen, und adm, wahracheinlich ein Akkusativ, der Erde, Dio Bezichung im Bilde, zwischen elf und aém, maf der Beriehung ahneln, de statt hat und hier durch &&s pairida bodoa ausgedrtckt Warter kann nurim Hinblick auf das andre
19212:Dal ea sch hier um elie Inutgesetsliche KGrzung handelt,ateht mir sit langem ext (va ‘Trans, Phil. Soc, 1944, p. 50). Sie segt aieh 2B, bel den Endungen -oyl, -ayii der Stim, fir die 1. Kurylowles, Indoirania, pp. 10 agg. (= Comptes rendus de la Société des Sei 1 des Lettres de Wroclave, 111, 1968, Wroclaw 1951) eine komplisierto Reklirung gem der jedoch dio Ohereinatinmung der sanskritisehen und altpersschen Formea im Woge st
22590:nd Badisaf). Die Namen beider Hauptpersonen sind gliicklicherweise jo cinmal erhalten, als Bylwhr und Buys}. Eine Seite des Bruchstiicks enthilt das Ende der ersten Unterredung (= K. B. a B., Bombayer Druck 8. 69) und den Beginn der aweiten, welche mit Bédisafs Frage aber Bilauhars Lebensalter beginnt (= Bombayer Druck 8.
22591:Die Auffindung dieses von Manichiern Gberlieferten Epos sttitzt die meh fach gemachte Annahme einer auf indisch-buddhistisches Material gegriindeton manichdischen Urversion der Legende®; F.W.K.Moxian 2. B, schlug cin ymanichiisches Prototyp vielleicht in soghdischer Sprache" vor. Die Namens formen, besonders Buodys/, beweiten, daB der neue Text am Anfang der Uberlieferung steht Indisches Original: Baihisattea
24640:WH. W. Barry und O. Szewenévv1, vgl. Maynuoren 1.0. 328A. 6, wo ungenau behauptet wird, ich hatte ,,an eine Bildung von iran. Vdaie™ dacht, wihrend bei mir nur von dem Worte disé ,,Festung" die Rede war.
24668:Bei dieser Sachlage berahrt es merkwirdig, in Maynuorers Aufzih- Jung von Hosacus ,,Treffon das Folgende angeflhrt zu schen: Fir xapedpayyo .,kandrang" bietet Hoxmact, Manice fortfahrend, wohl die beasere Etymologie als Grnsaevrres und Hexwnso'* (S, 342); denn hier wird unsere Verbindung mit kandrang am Ende abgelchnt und am Anfang
24737:cinem altererbten Kompositum zu erwarten, aber nicht bei einer Zusam- menfiigung der lebenden Sprache; sogar bei Baryorupo, das schon lingst in ein Ganzes zusammengeschmolzen war, ist die Tenuis erhalten, Dazu kommt, daB sich eine Frau in einer Liste kuschanischer Wiirdentriiger wunderlich ausnihme, und endlich, daB die angeflhrte soghdische Vo- kabel gar nicht ,,Tochter“ heiBt. Denn, um eine von A. Manicg bei an. derer Gelegenheit gewahlte gute Formulicrung* anzuwenden, es ist dies cin Wort qui met plutdt Paccent sur la notion denfanco que sur celle de descendance, et qui ne précise pas le sexe. Wird doch im Soghdischen selbst das Wort von dem kleinen Seth, dem Sohne Adams, gebraucht, an einer Stelle, wo man am besten ,,Kindlein' dbersetzt; Anwendung verwandter Formen suf mannliche Kinder, bes. in pejorativem Sinne, ist hiwfig genug im Iranischen, vgl. etwa pers. king ,,Lustknabo' (ous *kanika-), welches auf jeder Seite von Ubaid-i Zakinis La(a?if zu finden ist;8.auch unten zu Kanishka. Wahrscheinlicher ist Aatiinyxvastyt cine Nisbe gewohnlicher Art, mit *-£i%, von einem Ortsnamen in -dn oder -giin (aus -kdn)®, dergleichen es Hunderte gibt™,
24753:Lchnwort, angepaBt durch Ersetzung von 5 durch 1, anzuschen wire. Ahnlich bogegnen wir ffir im Titel des Grofiviziers, oa%opxo qpouaxpo, dessen Herkunft aus dem seit der Griindung des sassanidischen Reiches bezougten, trotzdem vielleicht schon parthischen Vazurg-Framadar aber jeden Zweifel erhaben ist; er findet sich auf einem Siegel der Carter Col- lection, deren Verdffentlichung wir A, D. H. Brvan verdanken. Vor dem ‘Titel steht hier der Kigenname, ebenso bei einem Amethyst der Eremitage: Onpavpavo paveago , Varahrin der Satrap'®, mit der in Persien iibliche: urspringlich parthischen Form Zahrab, gegoniiber veraltetem kyatrapa, as in den indischen Grenzlanden weiterhin in Gebrauch bliel, Mégicher woise findet sich dakrab auch anf dem ebenfalls von A. D. H. Brvan ans Licht gezogenen Siegelabdruck des Ashmolean (auf den ich unten noch zuriickkomme), doch ist die Lesung ganz ungewiG; sicher ist wohl nur pxup-,, also dahr. , Macht/Machtbereich** oder eine Ableitung davon. Auf einom von Sraviskry zuginglich gemachten Stein? steht deutlich
24789:hat sich also nicht bewihrt 38 Numiem. Chron., 19 » Dio Abbildung bei C. W
24836:¥ Soino Transkription ist dagegen 2. T- veraltet; dio Regel fu schoidung von « und o in der Kursivschrift findet man in BSOAS 835,
```


## [2026-09-06T15:10:54.887Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2345,2380p' HENNING_selected_papers.txt"
}
```


### [2026-09-06T15:10:54.950Z] TOOL RESULT

```
ada * syrup”
 
   
s0 Arab., see Fraenkel, op. cit., p.
 
 
ant or
 
against the rules, so that we cannot be sure whether kd is hol, If it is bud, of, NPers. kd (Arm. koit ; of. also the Pahl, transl. of Av. ydnhuya-) " stack, heap of com or dung”. For the explanation phers use NPers. tade “ heap”, which be tempting to identify with Sogd. fwéy). If it is knot =" pit, sink, dr Bartholomae once wrote & paper of seventeen pag Pahlavi words (Mir. Mund., i). But of all the vocable him only halak “foolish ” merits. consideration (for 1/r, MPers, rz, BSOS., ix, p. J. Sampson, p. 316) Other words are *harray (thus in Bal.) “saw”, *harg = Av. haroka:
refuse” (NB. “ tax" is fr'g, not *hrg, see Orientalia, iv, p. 291) but ef. Niya doc. harga, Arm. hark, Burrow, BSOS., vii, p. 788). Of these wonds, harg “refuse "seems most suitable in connection with
 
of kad Persian lexicoga would
    
 
see BSOS,, ix, p. 84. As regards hy, it will be recalled that
 
on suitably spelt
mentioned by
 
 
f. eg. Man,
 
7, Welsh Gypsy ri
    
‘h8, beit' aheap of dung and refuse ", or" apitand refuse ". Turning
        
(58)
88 soGDICA
now to the Sogdian translation, we observe that the identical word sobyh, spelt tw8'k, occurs once in Diydna, 343, as a rendering of Chin, ME jin “shade”, etc., but corresponding to Skt. skandha (cf. Demiéville, JA., 1933, i, p. 209 n.). Tt would be wrong to arrive at the conclusion that Sogd. t8’k meant anything like “thade, shady, dark”, ete.; for the translator may well have been aware that Skt. skandha was intended, and therefore may have employed any of the other traditional renderings of skandka among which those meaning “aggregate, multitude, collection, heap” are most prominent (e.g. Chin. M jiin, Chin. #e tung, Uiyor yikmak), This would agree with the meaning of NPers.téde (see above). Thus we may assume that the Sogd. gloss means “‘refuse on a heap", but no corroboration is available for this translation of "my ; one can hardly compare Buddh. po "m'yk, DN, 10 = Chin. ff sien “fresh, clean”. —(29) Sopd. mryondyy is “lump, clod, ball", Baddh. mr’)wntk, SOB., 205, Prag. ii, 80 8qq. 78 either is an adjective (less likely on account of the lack of a vocalic ending), or forms a compound with mrytendyy. It could be the compound form of yr8'Kh “ throat” (SCE., 98, 125), and y- m- could mean “ throat-lump ” = "* Adam's apple.”” Although there are other possibilities (e.g. yr8-—= NBers. gil “clay”, or yr5- = Av. goroBé.{korsta-, hence gallstone ?”), this interpretation seems preferable on account of the identical compound Yidgha yurvo-huluza, Morgenstierne, IZPL., ii, p. 213, “ Adam's apple” (yurvo “ throat”, NPers. kuliiz “lump, clod of earth”*)—{30) MPers. “heart ".—(81) Parth. “pit, prison”, ef. BSOS., ix, p. 83. Restore f{nd-!—(33) MPers. “the coquettish one of ”.—(84) MPers. “ ears and e}
MP.-Sogd. " blood”. (37) MP.-Sogd." vein "—{38) Sogd. “ phlegm”. This word, apparently borrowed from a Prakrit form of Skt. dlesman, occurs frequently in Uiyur medical texts, see Rachmati, Heilk, Vig., fi, p. 443 (read lidp, litip in the place of lisp, lisip). Professor Bailey informed me that it is attested also for “ Tokharian", as letp- (Toch. Gramm., p. 229). Wakhi lip Morgenstierne, IJFL., ii, $28.
```


## [2026-09-06T15:11:09.344Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nls; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} NR==650' BQT_v3_pages.txt | head -40"
}
```


### [2026-09-06T15:11:11.997Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
---
[pdf page 650]
—N\aor—

کوزی (۱) مراد اين باشدکه با نیکان نیکی
و بایدان بدی - و بمعتی مقل هم آمده است
و بهترین ‎oT‏ مقل ازرق است ؛ و بسنی گویند
نبات مقل است یمنی علف مقل , و مقل صمفی
است که از ‎OF‏ بهم مبرسد - وبتر کی‌فصل پابیز
باشد .
وزاب ۱ - بنتح اول بروزن‌مهتاب.
آشیرا گویند که از کوشت و برنج و نخود
و گردکان پزند .

‎AIF‏ - بنم اول و سکون آخر که
زای نقطه‌دار ‎ath‏ , نام پرنده ات خوش آواز
شبیه به بلبل .

‎PTF‏ ۲ - بنتح اول و کاف
فارسی ۰ بروزن و معنی جوزاغند است که ممرب
‎oT‏ باشد , و ‎OT‏ شغتالوبی است خشك که درون
آترا از مخز گردکان پر کرده باشند .

‎POLI‏ - با انی مجهول و بای
‎aml‏ بر وزن بوستان » پاردم چاروا را گوبند .
وان چرم یا نواری ‎ath‏ که در زیر دم ستوران
گذارند ‎(x)‏ .

‏گوزبن ۴ © بفتح ‎Jol‏ و ضم پای‌ابجد.
درخت گردکان ‎an Sl,‏ ؛ و بضم اول هم درست
‎cal‏ +
‎Jal ho * IGF‏ بر وزن اوحد ,
بمعنی جمل باشد ‎OT,‏ جالوری است که س رکین

‏(۱) خم۱: کوز .
(4) چك » چش : میشود .
۱ - از :کوز ‎THF)‏

‏جوزاغند * جوزغند .

‏۴ - از :گوز (گردو) + بن ‎Gee)‏ .
```


## [2026-09-06T15:11:23.097Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 640 645 655 660 665; do echo \"== pdf $n ==\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v3_pages.txt | head -6; done"
}
```


### [2026-09-06T15:11:24.757Z] TOOL RESULT

```
== pdf 640 ==
[pdf page 640]
—N\ate—

کنکه

تولول ‎a Ke‏ وفارسیان ‎EP‏ .
== pdf 645 ==
[pdf page 645]
گوازه
‎ce - ot‏

کواز است ‎OT,‏ چوبی باشدکه ستوران را بدان
رانشد - و هاون چوبی را ‎Ay) a Se‏
== pdf 655 ==
[pdf page 655]
‎nh ply‏ معنی هم هست یمنی‌دگاهدار ومحافظت

‏گوش‌داشتن- بمعنی متوجه خدن
باشد ۱ - و کنایه از دیدن و نگاهداشتن (۱)
ونگاه گردن یز(۲) هست ۲ .
== pdf 660 ==
[pdf page 660]
lA

و جرم آسمان است - و کنابه از کوا کب هم
هست .

== pdf 665 ==
[pdf page 665]
‎AST‏ نمناك هدوت
‎ol”‏ فهناگ » بکر ها و فتح ‎oy‏ | باشد چه کیتی بمعنی جهان و نوردیدن بمعنی
بروزن ‎he‏ غمثاك » ‎coh‏ که آیرا خرفه | کردیدن است - و کنابه از آفتاب عالمتاب است-
‎le Bel 9 ge‏ و کنایه از اسکندر هم هست - و اسب را نیز
```


## [2026-09-06T15:11:31.715Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 651 652 653 656; do echo \"===== pdf $n =====\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v3_pages.txt; done"
}
```


### [2026-09-06T15:11:34.184Z] TOOL RESULT

```
===== pdf 651 =====
[pdf page 651]
کوزکند

گویند (۱) .
‎LPS‏ - با کاف فارسی بر وزن
نوشخند ۰ سخنان لاف ‎jy,‏ ودرو غ‌را گویند.
گود ‎CAP‏ - بنتح ال . بیخ کیاهی
است که در نظر چنان ‎UF Sauls‏ پنج شش
‎ast‏ کندم است که برهم چسییدماند و خوردن‌آن
منم آرزوی ‎Me‏ خوردن‌کند . گویند اگر يك
‎aL”‏ ازآن را با ده رطل عمل و ‎OT Shige‏
تيك درهم آمیز ند ودرظرفی-کرده سرآلرابگیر ند
در ساعت شراب رسيدة خوشگوار کردد و ‎OT‏
‏شراب فربهی آورد و قوت باء دهد و ‎NYT‏ معرب
کرده جوزجندم (۲) خوانشد .
گون ۱ - بنتح اول و انی و سکون
ه بفتح اول و انی و سکون
‎SM‏ ونون» ‎FF‏
‏ا زگاو کوهی باشد
وشاخهایاوبشاخهای
درخت خشك ‎att‏
‏مائد . کویندآب
کوشهای چشم او
ترباق‌زهرهاست_.

(۱) خم۱ : خوالند .

. ets ۱ ‏خم‎ (x)

)وا

گوده ۴ - با الی مجهول بروزن‌روزه.
‎GME‏ و غوزة خشخاش ‎May igs‏ ابربشم‌وامثال
‎faa SUT‏ و با زای فارسی هم آعده است .

گوذهر ۴ = بنتح اود و کس نانی
و قتح ‎elt‏ و سکون‌ها و رای فرشت ‎fade‏ ری
و ذنب راگوبند وآن دونقطة تقاطع فلك حامل
ومابل ‎pad‏ است و معرب‌آن جوزهر باشد .

گوده مح ‎Jol gee -f‏ ومیم‌وسکرن
خای نقطمدار , غلاف گل خرما راگویند.

گوز یه * ‎pie‏ اول بروزن‌لوزینه,
حلوائی ‎SaaS,‏ از مغ زکردکان پز ند .*

‎VOL‏ - مترون است کهبچة کاو
باشد - و بمعنی شتربچه و ‎SD‏ بچه و هر چیز
که‌آن کوچك و خورد سال ۷ ‎ath‏ هم‌هست چه
کوبمعنی‌خرد و کوچك‌نیز آمد» است۸ ؛ و کاهی
بطریق کنانه بجوانان بسمقل ‎Jol‏ عمرهم استعمال

‎(EUS OL gr‏ - کنابه از بیج
تور اس ت که برج دویم باشد از جملة دوازده‌برج

‏(۲) چش : - فلك ()

‏۱ - پپلوی 88722700 > اونوالا ۸۷ » ؛ ‎oF‏ معمولی جانوری است از ‎Bal gle‏ پر
شاخان از شخوار کنندکان ۰ که در جنگلپا زست کند . شاخهای ‎OT‏ هرسال می‌افتد و سالبسد

‎oh,‏ شاخ اضافی درمی‌آید . ركك : گوز.

‏۴ - غوزه (هم.) ‏ غوژه , ‎Ny‏ کوزغه .

‏۴ ۰( معرب ) جوزهر ‎Cpe)‏ در پندهش فصل 0 ‎ae‏ ۷ «گوزهر» و « موش پریك»

‏با سیارات مریوط ‎tb‏ شده ضد ماه و خورشید میباشند « پورداود | ‎Le‏ ج٩‏ ص ۱۹۵ ‎٩‏ .

‏۴ - از :گوژه (هم) مخ (خرما) (هم.) .

‏نبت). بهلوی ‎guctnak‏ > اونوالا ‎٩۳‏ >

‏۵ - از: کوز(کردو) (- بنه(یوند
۰ - از :کو )= کاو) +-ساله [ از : سال

‎Olay > gasile ‏[(آلء) . کردی‎ dbrlingskalb— ] JUS ‏سبت) دارای‎ aye) a+

‏۱ یز کردی 0۵8816 « ژابا س ۳4۹ > و رل : اسشق ۰۹4۱

‎. ‏خرد سل‎ - ٩

‏۸ - سحيح نیت . وکو | < گاو] («م.) ‎gine‏ مطلق‌جانوران اعلی است .

‏+ طوژ ‏ رك : کرژ.

===== pdf 652 =====
[pdf page 652]
و۱۸۵ کوشلسب

فلك ‎#.(y)‏ است که مو کل ‎col‏ برمهمات‌خلوعالم ۴ . ول

گوسپند کشان - بنم کان ,روز | دوز چهاردهمازهرماه شمسی باشد وفارسیان درین
‎we‏ قربارا گویند ۷ . روزجشن کنند وعدسازند وآن‌را سیرسو رکویند

گوست ه بر وزن ‎on‏ کوفتگی ودرین روزسیربرادر ‎Shy‏ خوراد و گوشت رابا گیاء
کوفه‌شدسرا کویند؟ - وبسسنی کوی‌هر وت ی | و علف پزند نه با چوب وهیزم ‏ و گویش این
‎Hl‏ بز رکه باشد ۴ . ‎cols‏ امان یافتن از مس ‎Lay‏ جن است وبدان
‎os‏ دوای ‎yal pl‏ کنند که منسوب بجن‌است» ودرین

گوش ‎te‏ نی روزليك است فرزند بمکتب دادن وپیشه آموختن
ات ‎ARE‏ | تسش رتست
و بسن کنج )0 ‎“ES,‏ - و ‎tee‏ حفظ و ‎chiles‏ هم هسته .
همآمدماست- ونام‌فرشته‌ای ‎GS‏ گوشاسب ۱ - بنم اول و تالك بالف
(۱) چش : فلکی . ‎(x)‏ چش :کج ()
۱ - رك : التفپیم پیرونی س ۲۵۲ . ؟ - اسح « کوست» (ه.م.) است .

۴- اوستا - 88052 « بارتولمه ‎۶۸٩‏ > پهلوی ‎ns > BOSH‏ رکه ص ۸۳ >»پارسی
پاستان - ‎gausha‏ , هندی ‎ghosha - ott‏ ( صدا ) , کردی 80 ‎ghvagh gust.‏ ,
| 8005 » 405 . بلوچی ‎gdsh‏ , وخی ‎ghish . ghiish‏ « اسعق ۰۹:۳ .

۴ - اوستا ‎goush‏ » پپلوی ‎gush‏ ( لفة بمعنی کاو [ه.م.]) ‎ee‏ فرشتة نگهبان
چپارپایانست . لگهبانی روز چهاردهم هرماء با اين فرشته است . بقول بیرولی در < گوش روز ©
ازدیماء جشنی بوده است موسوم به « شیرسور * که درین روز سیر وشراب میخوردند و برای‌دقع
‎cle je Oke vl‏ ویژه با گوشت می‌پختند. زرتشتیان ‎pl‏ نیزاین روزرا « کوش» نامند.بیرولی
‎TH‏ جوش > ( معرب گوش ) و در سفدی « غش * و در خوارزمي « غوشت * آورده :

کوش روز ای تکار مشکین خال ‎59S‏ بربط بگیر و ليك بمال .
منود ‎ane‏ . ص ‎٩٩۲‏ >
‎Hy‏ : روزشماری بقلم لگارنده ی ۹-۳۲ کوش داشتن . ‎OS bie‏ :
ای ‎Abe‏ العرش مرادش بده وزخطر چتم بدش دا کوش .

« حاظ شرازی مصحح قزوینیصس۲ 4۱۹

۲ - رك :کوشاسب » بوشاسب .

* گومپند » گوسفند - بتلفظ قدیم 0 , 8657874 . و بتلفظ کنونی
40 . اوستا - 8805۳6008 . پهلوی 805۳804 « استق ۹4۷ ۰۰ مرکب از : کو
(گاو « ‎saw‏ مطلق جانوران ‎lal‏ سودمند ؛ و بقر ) +-سیند
( اوستا 5۳61012 بمعتی مقدس ( لفة یمنی جانور ‎(hal)‏ پاك
در پهلوی ‎js‏ کوسیند اسم مطلق جانوران اهلی است ) . اسم
اصلی جانوری که امروزه کوسفند نامیده میشود ۰ میش ( هدم. )
است ) « قاب ۱ص ۸۰ ؛ جالوری است از ‎Bal sls‏ تهی شاخان
از تشخوار کنند گان ‎chlo.‏ شاخ مورب . حلقوی و پیچاپیچ .


===== pdf 653 =====
[pdf page 653]
کوش افتادن
کنیده و ببین بی‌قطه و بای فارسی زده؛بسعنی
خواب دیدن باشد که عربان ‎BSUS‏ سوبمعنی
احتلام و شیطالی شدن هم هست - وجوالیرا نیز
گویند که حنوز خطش ندمیده باشد .

گوش افقادن ‎ate‏ از کر شدن
و ناشنودن گوش باشد .

گوشان - با ‎gh‏ مجهول بر وزن
جوشان » عیر و فشردة انگور را گویند .

گوشانه ۱ بروزن روزانه ۰ ‎wise‏
‏کوشه و کمینگاه باشد .

گوش آوای ‎Ga)‏ واو بالف
کشیده بتحتالی زده . شخصی را گوبند که هرچیز
شنود خوب ‎Spd‏ وبا کیرد .

گوش در - بکر بای ابجد وفتع
دال و سکون رای بی‌نقطه (۲) » بمعت ی کوش بر
آواز است که منتظر واتظا رکش باشد .

گلوش برداستی = کنابه ازناامید
خدن و ‎abd‏ نظرکردن از ‎Meal‏ باشد ؛ و در
جای دیگریمعتیاتظار کشیدن بنظرآمده است؟.

گوش بر در داشتی - کنابه از

(۱) چك . چش : کو شآوایی .

(۷) چش : رای قرشت .

۱ و۸

اتظار کنیدن و منتظر‌بودن باشد .

‎sh Ke ft AF‏ ابجدوسکون
سین بی‌تقطه و فتح تای قرشت ۰ نام شخصی بوده
که چون اسکندرذوالقرلین متوجه شهربابل میشد
در اثنای راء بکوهی رسید بی ‎ple‏ و در دامن
آنکوه دریابی بود ‎HL Se‏ بشکار مشفول
شدند و مردیرا بافتند بزرکه جثه ودرشت اعضا
و پر موی و پهن کوش ۰ گویند پهنی کوش او
بمثابه‌ای ‎Soy‏ چرنْ خواییدی ‎FlyFF eh‏
و گوش دیگر را لحاف کردی ؛ تزد اسکندر
آوردند . تحقیق احوال او کرد و نام او رایرسید
کفت که : مرا « کوش بستر > نهادند نام ۳ .

‏گوش یچ = ‎gan‏ کوتمال است -
و پارچه‌ای را نیز گوبند که بجهت دفع سرما بر
دورس و کوش پیچند .

‏گوش پیچیده = ‎ab‏ از ‎2S‏
‏باشد - و کوش مال داده را نیز گویند .

‏گوشت ۴ - پفتح اول و ثانی وسکون
ثالث و فوقانی » نام یکی از شش ‎BT‏ موسیقی
است که (۳) ‎OT‏ نوروز و مابه وسلمك و گوشت
وشهناز و کردانیه باشد .

‎. ‏و‎ ote )۳(

‏۱ - قی ‎tS:‏ « اکر مراهزیمت دادند تراك ازسستان کیرم و بهمان کوشاله راضی
شرم .» «تاریخ سیستان ص4۱۲* . ؟ - ‎ol‏ معنی« وش بردر داشتن » است .
۴ - فردوسی‌طوسی دردلشکر کشیدن سکندر سوی‌بابل» آرد (شاهنامیخ ج۷ص۱۹۰5):

‏سکندر میه سوی ‎dik‏ کشید
پدید آمد از دور مردی ست رکه
تنش زیرموی ادرون همچو لیل
چودیدند کردان کسی زین شان
سکندر نگه کرد زو خیره ماد
«چدمردی؟» بد و گفت ونام‌توچیست؟*
پدو کفت : «شاها ! مرا بایومام

‏ز گرد ‎age‏ شد جهان ناپدید ...
پر از موی و با گوشهای بز رک
دو گوشش بپهنای دو کوش ‎Je‏
‎woe‏ پیش سکنتر . کشان
بروبر همی نام یزدان بخواند
‎oh an‏ وکام توچیست *
‎soy‏ نهادند لام ‎fa‏
‎AT: 5 “‏ گوشان .

‏۴ پارسی باستان ‎Ogaushta?‏ « هوبشمان ۹:4 > ‎BOsht ogy,‏ , اففانی ع

‏8 , کردی ‎gOsht‏ . بلوچی 80904 , 8۵220 . وخی ‎gusht‏ , منجی 80۵5 ,
سریکلی 8184 ‎wus.‏ 8011 « استق ‎cate‏ ماد رم وسرخ که استخوان بدن را می‌پوشاند
و پوشيده میشود از پوست بدن ۰ لحم .

===== pdf 656 =====
[pdf page 656]
SS

وا

است که ‎Wey‏ باشد 6 .

‎GE Le ۱ UP gh‏ فارسی بر وزن
مودار, نام جالوری است که س رگین را کلوله کند
و بگردانه وغلطان غلطان ‎Glogs‏ خود بردوآنر!
عربان خنفاء میگوبند .

‏وال ۷ (۱) روز نکویل,بسنی
‎IOS‏ است که م کین
‎bls‏ باشد و عربان
ختفاء گوبندش ‎Oy)‏ ۰

‎wo *۵ ‏گر‎ oF

‏کاف فارسی ‎Losey‏ ودال
بی‌نقطه» جوهریت که آلرا
کبرت‌هم ‎au Se‏ و آن
ک وکال چهار لوع میباشد : سفید

‎aS

‎LS‏ باغی ‎AF‏ - کنابه از
کوشه‌شینی وخلوت کزیدن باشد .

‎is‏ بالش = کتایه‌از کوشم وکنار
مسند باشد .

‎tle ay‏ شکیته ه کنابه از
ماء لو باشد که هلا لگوبند +

‏گوشیار ۱ - بر وزن هوشیار ‎ths‏
‏حکیمی بوده ازفاری وشیخ ابوعلی‌سینا شاگردی
‎are‏

‏گود ‎en‏ اول و سکون ثانی مجهول
وکاف فارسی » ‎Ob SEG gee‏ باشد و آنرا
کوی گریبان هم میگویند ۴ - ودانهای سختی
که در ‎Lael‏ بیم میرسد و درد نمیکند و عربان | وزرد وسرخ وسیاء؛ وبسضی گوبندچشمه‌ایست‌روان
تولول خوانتدش ۴ - و بممنی کوساله هم آمده ]| چون منجمد گردد کبربت شود ؛ و بست یکوشد

‏(۱) چش : کوکال . ‎)٩(‏ چك : میکوبند ؛ چش : - و عربان ...گوبندش .

‎FH ‏اصح همین صورت است یمنی با کاف پارسی » از :کوش ( نام فرشته ) («.م.)‎ - ٩
‏داده [ قس : بهمتیار , اسپندبار , هرمزدیار ) 4 ابوالنکیا‎ tee: * ‏داد‎ « Jae ‏پسوند‎ ( ob
‏چهارم‌هجری میزسته ومژلف‎ OF ‏دوم‎ bag ‏کوشیارین لبان باشهر یگیلالی منم بزرکه , وی‎
Bab ‏و «مجمح‌الاسول» است . رك : کوشیار گیلانی بقلم نگارنده در‎ UL ‏جامم » و «زیج‎ mS?
‏و ص۲۰8-۷۰۰. ۰ ۴ - ظ.با «بهمنیار» که شاکرد ابن‌سینا‎ BLL IIL ‏فرهنگه, چاپ مشهد‎
‏خلطشده» ولی او آنر باجالی است + وک شکل‌قديم :کوء گوی (هدم.),‎ (kn ‏بوده (نه‎

‏۴ < ک که («م.) © کو که (هم.) طبری 80 ‎(JLT)‏ « واژه نامه
‎dy > ۶‏ :کار ,کو . ۲ ص کوکال ‎(pn)‏ , قس : اوستا ‎vareta‏ 806۳8 .که درتفیی
‎Jalen) Soles OT Is) ose Favs f gOh _vartsse‏ وهای‌ملفوظ بمعنی سکین‌است) ‎ope‏
‏دوم همریشه وبععنی گردیدن وگرداندن‌است. لفة بمعنیس کین گردان(ه.م.) ورك ‎US FF‏
ورك : ح٩‏ ص۱۸۲ ۷ ک کار ‎pa)‏ ۸ - دراوراق مالوی‌بپپلوی ۳۵
«کو گرد . -ولفور» ,1 ‎(Henning, A list of Middle Persian..., 3505, XI,‏
‎p ۰3‏ )ک وکرد ‎Soufte)‏ فر) جنمی است بیط و جامد » برنگه زرد لیموبی » بی‌مزه وبی
بو . وزن‌مخضصوص‌آن ۵ است ودره ۱۱۶ درجه ذوب میشود ودر 440/۵ درجه بجوش‌میآید.
ک و کرد در طبیعت بوفور بصورت سولفورها با سولفانها , با صورت ‎gel‏ خویش درحوالی کوههای
آتشفشان یافت میشود .

‏» گوشه - بضم اول و کر سوم ( در لهجهٌ مرکزی ) و بقتح ‎OT‏ ( در تلفظ قدیم ) 4
اوستا - ‎ogaoshaka‏ . کردی 802 , 805۲6 . بلوچی ¢ 805۳086 ‎ys.‏ 805126
‎EO ۹40 gel?‏ کنج » زاوبه - خلوت . خلوتگاه ‎Se‏ کناره = دستهٌآوند - دکمه, کره.
```


## [2026-09-06T15:11:57.254Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 660 661; do echo \"===== pdf $n =====\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v3_pages.txt | tail -30; done"
}
```


### [2026-09-06T15:11:59.288Z] TOOL RESULT

```
===== pdf 660 =====
که همه کس نفهمد - و کنایه از کلامی‌است که
تمام قواعد و قوالین و صنایم و بدابع سخن در
‎OT‏ صرف شده ‎AN) ath‏

‏گوهری ۱ « بروزن جوهریجیزی
را کویند که از کوهر ساخته باشند - وخداوند
اصل و سبت را بيز کفته‌اند - و جواهر فروش
وجواهرشنای را هم کفته‌اند ۷ - و بمعنی ‎AS‏
‏هم هست که در مقابل عرشی است .

‏از: گوهر + خای(خاینده).

‎: ‏دولت‎ o,f
‏جهان بین که گوهر برو چون‌شکست.‎

‏نظامی کنجوی « رشیدی * .

‏6 - ز بهر ساعد شاخ ‎cel yl‏ کوهر کش
که قطره در خوشابست و سبزه شبه دوال .

‎. # ‏رشیدی‎ « QL

‏دفیع
‏- از ‎st oy:‏ ( پوند دبت ) ؛ پهلوی 8010716 ( اساسی ۰ اصلی ) « ‎he‏

‎٩ ۲ : ۶‏ .
« جواهری ۴ (معرب) کویند .

‎gohert toes -۲‏ ( جواهر فروشی ) « ژابا ص ۳۷۷ » . آمروزه

===== pdf 661 =====

‎ah,‏ - وبمعتی سراب همآهده است‌وآن شوره

‏زمینی است در صحراکه ازدور ‎OTE‏ میماند*۱-
و ‎tee‏ صحرا هم بنطرآمده است *۷.

‏گوی زر , گوی زدین )=

‏کنابه ازآفتاب ‎Wet‏

‏ای ‎cand‏ مشکین کله , ‎GUC,‏ کوی از انگله
می خور ز جام وبلبله , با ما خور و با ما نشین.
‎GL?‏ غزنوی ص ‎EVIE‏ .
۴ -کردی 80 ‎go.‏ ) گلوله‌های بازی .کرء ) « ژابا ص ‎COW‏ -کوی در التفهیم
بروئی ‎x)‏ ۵۷ ) بممتی فلك آمده . ۴ « کو ( مخفف ) ‎(pm)‏
‏۰ - از :کوی (گفتن )+۱( پسوند فاعلی و صفت مشبهه ) .
‎٩‏ - ( از دو درخت ) یکی ‎ok‏ و دیگری بر اوی
سخن کوی و با شاخ و با رنه و ‎Sy‏
‏چو روشن شود لر وبا شود .
« فردوسی طوسی. شاهنامةٌ بخ ج ۷ ص ۱۸۹۹.
۱ - از ‎GF:‏ (کفتن )۱-۲( تردید ) [ قس : مانا ] . گوبا در ‎cad‏ نامه ( ذیل :۲)
مخفف ‎CLAS?‏ آمده قس : پنداربا . امروزه غالباً بمعنی مذکور در متن استعمال شود .
۷ = کوانگله ‎Sag (pe)‏ : گوی , انگله ‏ ۸ - اثاره به « ‎AG,‏ النای
فی‌المهد و کهلا » ( سور ۳ [ آل عمران ‎٩ .) 4۱ ATL‏ - از: گوی + باز ( بازنده).
‎oh‏ ,5 : کویر .

‏پشب ماده کوبا و ‎big‏ شود

‏۱ رد : رشیدی .
```


## [2026-09-06T15:12:05.649Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"gutha\\|guh\\|gūh\\|gu.a\\b\" BQT_v3_pages.txt | head -20\necho \"--- pdf 659 tail ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==659' BQT_v3_pages.txt | tail -25"
}
```


### [2026-09-06T15:12:07.468Z] TOOL RESULT

```
46340:‏۴ - دراوستا 88780 (کلو) « پهلوی 8270 ؛ سانسکریت -8818 لاتینی ‎gula‏
--- pdf 659 tail ---
باشد - و ‎wip‏ آدم را نیز گونند - و خال را
هم کفته‌اند و عربان تراپ خوانند .

‏گوهر ]سمان - کنابه از ‎Jel‏

‏(۳) چش : است .

‏۴ رك :کون؛ ورك : ص ‎bradley)‏ کتاب.
۴ رك : « فرهنگ دساتیر

‎( Henning , A list of Middle Persian .., 1505, X, 1, ۵۰ 93(

‏۷ هت کپواره < گاهواره — کواره (هم.) .

‏۸ س کواره ‎(pa)‏

‎٩‏ - رل : کواه . - کوه ‎pin‏ اول و های ملفوظ بمعنی س رکین » اوستا 804102 [در

‏- ۷۵۲6/۵ ] 80400 بمعنی که کردان یعنی جمل . رك : کوکار ) ؛ پهلوی ‎BOB‏ ( در
6 اما که کردان ‎Jer‏ ( . ساتکریت - 80002 , ارمنی ‎ku‏ ( کود , ‎«(ads‏
‏کردی 80 ‎ghul ysl.‏ . بلوجی ‎gith‏ . وخی ‎gl. gil‏ , اشکاشمی 805 « استق ۹4۷ ».
*- پهلوی 8017 ( جوهر » ماده ) « ‎٩۱۹۱ USL‏ با 8010۴ معرب آن جوهر
« یی رکه ۸۷ » « منای ۲۷۵ : ۲ > . ورك : اسثق - هوبشمان ‎NEA‏ « پارسی ترصیم ‎PIS‏
‏برشته کردن بود ۰ » « ترجمان البلاغه . چاپ احمدآتش . بخش عکسی ص ‎۷۲۳٩‏ ب > .
```


## [2026-09-06T15:12:24.827Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor n in 657 658 659 662 663; do echo \"== pdf $n ==\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' BQT_v3_pages.txt | sed -n '2,4p'; done"
}
```


### [2026-09-06T15:12:26.336Z] TOOL RESULT

```
== pdf 657 ==
My

ممدیی است وآن بشاری باشد دخالی که بعضی
== pdf 658 ==
را

بازی کردن و خواه بز رکه باشد از برای توپ
== pdf 659 ==
کون ژده

‎OS"‏ ژ۵ه (۱) = ‎ce‏ زای‌فارسی‌ودال
== pdf 662 ==
—\ave—

‎pe AS‏ وزن فیس » ظرف
== pdf 663 ==
بیان هیجد هم

در ‎SE‏ فارسی ۳ ها ‎atts‏ بر پاتزده لغت و ‎cal‏
```


## [2026-09-06T15:12:32.033Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nd=json.load(open('BQT_v3_pagemap.json'))\nprint(type(d))\nif isinstance(d,dict):\n    ks=list(d)[:5]; print(ks); print({k:d[k] for k in ks})\n    for k in ['650','652','653','659','660','520','523']:\n        print(k, d.get(k))\n\""
}
```


### [2026-09-06T15:12:33.987Z] TOOL RESULT

```
<class 'dict'>
['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
{'pdf': 'data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'pdf_pages': 721, 'offset_mode': 1203, 'anchors': 34, 'map': {'1210': 1, '1211': 2, '1212': 3, '1213': 4, '1214': 5, '1215': 6, '1216': 7, '1217': 8, '1218': 9, '1219': 10, '1220': 11, '1221': 12, '1222': 13, '1223': 14, '1224': 15, '1225': 16, '1226': 17, '1227': 18, '1228': 19, '1229': 20, '1230': 21, '1231': 22, '1232': 23, '1233': 24, '1234': 25, '1235': 26, '1236': 27, '1237': 28, '1238': 29, '1239': 30, '1240': 31, '1241': 32, '1242': 33, '1243': 34, '1244': 35, '1245': 36, '1246': 37, '1247': 38, '1248': 39, '1249': 40, '1250': 41, '1251': 42, '1252': 43, '1253': 44, '1254': 45, '1255': 46, '1256': 47, '1257': 48, '1258': 49, '1259': 50, '1260': 51, '1261': 52, '1262': 53, '1263': 54, '1264': 55, '1265': 56, '1266': 57, '1267': 58, '1268': 59, '1269': 60, '1270': 61, '1271': 62, '1272': 63, '1273': 64, '1274': 65, '1275': 66, '1276': 67, '1277': 68, '1278': 69, '1279': 70, '1280': 71, '1281': 72, '1282': 73, '1283': 74, '1284': 75, '1285': 76, '1286': 77, '1287': 78, '1288': 79, '1289': 80, '1290': 81, '1291': 82, '1292': 83, '1293': 84, '1294': 85, '1295': 86, '1296': 87, '1297': 88, '1298': 89, '1299': 90, '1300': 91, '1301': 92, '1302': 93, '1303': 94, '1304': 95, '1305': 96, '1306': 97, '1307': 98, '1308': 99, '1309': 100, '1310': 101, '1311': 102, '1312': 103, '1313': 104, '1314': 105, '1315': 106, '1316': 107, '1317': 108, '1371': 164, '1372': 165, '1373': 166, '1374': 167, '1375': 168, '1376': 169, '1377': 170, '1378': 171, '1379': 172, '1380': 173, '1381': 174, '1382': 175, '1383': 176, '1384': 177, '1385': 178, '1386': 179, '1387': 180, '1388': 181, '1389': 182, '1390': 183, '1391': 184, '1392': 185, '1393': 186, '1394': 187, '1395': 188, '1396': 189, '1397': 190, '1398': 191, '1399': 192, '1400': 193, '1401': 194, '1402': 195, '1403': 196, '1404': 197, '1405': 198, '1406': 199, '1407': 200, '1408': 201, '1409': 202, '1410': 203, '1411': 204, '1412': 205, '1413': 206, '1414': 207, '1415': 208, '1416': 209, '1417': 210, '1418': 211, '1419': 212, '1420': 213, '1421': 214, '1422': 215, '1423': 216, '1424': 217, '1425': 218, '1426': 219, '1427': 220, '1428': 221, '1429': 222, '1430': 223, '1431': 224, '1432': 225, '1433': 226, '1434': 227, '1435': 228, '1436': 229, '1437': 230, '1438': 231, '1439': 232, '1440': 233, '1441': 234, '1442': 235, '1443': 236, '1444': 237, '1445': 238, '1446': 239, '1447': 240, '1448': 241, '1449': 242, '1450': 243, '1451': 244, '1452': 245, '1453': 246, '1454': 247, '1455': 248, '1456': 249, '1457': 250, '1458': 251, '1459': 252, '1460': 253, '1461': 254, '1462': 255, '1463': 256, '1464': 257, '1465': 258, '1466': 259, '1467': 260, '1468': 261, '1469': 262, '1470': 263, '1471': 264, '1472': 265, '1473': 266, '1474': 267, '1475': 268, '1476': 269, '1477': 270, '1478': 271, '1479': 272, '1480': 273, '1481': 274, '1482': 275, '1483': 276, '1484': 277, '1485': 278, '1486': 279, '1487': 280, '1488': 281, '1489': 282, '1490': 283, '1491': 284, '1492': 285, '1493': 286, '1494': 287, '1495': 288, '1496': 289, '1497': 290, '1498': 291, '1499': 292, '1500': 293, '1501': 294, '1502': 295, '1503': 296, '1504': 297, '1505': 298, '1506': 299, '1507': 300, '1508': 301, '1509': 302, '1510': 303, '1511': 304, '1512': 305, '1513': 306, '1514': 307, '1515': 308, '1516': 309, '1517': 310, '1518': 311, '1519': 312, '1520': 313, '1521': 314, '1522': 315, '1523': 316, '1524': 317, '1525': 318, '1526': 319, '1527': 320, '1528': 321, '1529': 322, '1530': 323, '1531': 324, '1532': 325, '1533': 326, '1534': 327, '1535': 328, '1536': 329, '1537': 330, '1538': 331, '1539': 332, '1540': 333, '1541': 334, '1542': 335, '1543': 336, '1544': 337, '1545': 338, '1546': 339, '1547': 340, '1548': 341, '1549': 342, '1550': 343, '1551': 344, '1552': 345, '1553': 346, '1554': 347, '1555': 348, '1556': 349, '1557': 350, '1558': 351, '1559': 352, '1560': 353, '1561': 354, '1562': 355, '1563': 356, '1564': 357, '1565': 358, '1566': 359, '1567': 360, '1568': 361, '1569': 362, '1570': 363, '1571': 364, '1572': 365, '1573': 366, '1574': 367, '1575': 368, '1576': 369, '1577': 370, '1578': 371, '1579': 372, '1580': 373, '1581': 374, '1582': 375, '1583': 376, '1584': 377, '1585': 378, '1586': 379, '1587': 380, '1588': 381, '1589': 382, '1590': 383, '1591': 384, '1592': 385, '1593': 386, '1594': 387, '1595': 388, '1596': 389, '1597': 390, '1598': 391, '1599': 392, '1600': 393, '1601': 394, '1602': 395, '1603': 396, '1604': 397, '1605': 398, '1606': 399, '1607': 400, '1608': 401, '1609': 402, '1610': 403, '1611': 404, '1612': 405, '1613': 406, '1614': 407, '1615': 408, '1616': 409, '1617': 410, '1618': 411, '1619': 412, '1620': 413, '1621': 414, '1622': 415, '1623': 416, '1624': 417, '1625': 418, '1626': 419, '1627': 420, '1628': 421, '1629': 422, '1630': 423, '1631': 424, '1632': 425, '1633': 426, '1634': 427, '1635': 428, '1636': 429, '1637': 430, '1638': 431, '1639': 432, '1640': 433, '1641': 434, '1642': 435, '1643': 436, '1644': 437, '1645': 438, '1646': 439, '1647': 440, '1648': 441, '1649': 442, '1650': 443, '1651': 444, '1652': 445, '1653': 446, '1654': 447, '1655': 448, '1656': 449, '1657': 450, '1658': 451, '1659': 452, '1660': 453, '1661': 454, '1662': 455, '1663': 456, '1664': 457, '1665': 458, '1666': 459, '1667': 460, '1668': 461, '1669': 462, '1670': 463, '1671': 464, '1672': 465, '1673': 466, '1674': 467, '1675': 468, '1676': 469, '1677': 470, '1678': 471, '1679': 472, '1680': 473, '1681': 474, '1682': 475, '1683': 476, '1684': 477, '1685': 478, '1686': 479, '1687': 480, '1688': 481, '1689': 482, '1690': 483, '1691': 484, '1692': 485, '1693': 486, '1694': 487, '1695': 488, '1696': 489, '1697': 490, '1698': 491, '1699': 492, '1700': 493, '1701': 494, '1702': 495, '1703': 496, '1704': 497, '1705': 498, '1706': 499, '1707': 500, '1708': 501, '1709': 502, '1710': 503, '1711': 504, '1712': 505, '1713': 506, '1714': 507, '1715': 508, '1716': 509, '1717': 510, '1718': 511, '1719': 512, '1720': 513, '1721': 514, '1722': 515, '1723': 516, '1724': 517, '1731': 528, '1732': 529, '1738': 531, '1739': 533, '1751': 548, '1752': 549, '1753': 550, '1754': 551, '1755': 552, '1756': 553, '1757': 554, '1758': 555, '1759': 556, '1760': 557, '1761': 558, '1762': 559, '1763': 560, '1764': 561, '1765': 562, '1766': 563, '1767': 564, '1768': 565, '1769': 566, '1770': 567, '1771': 568, '1772': 569, '1773': 570, '1774': 571, '1775': 572, '1776': 573, '1777': 574, '1778': 575, '1779': 576, '1780': 577, '1781': 578, '1782': 579, '1783': 580, '1784': 581, '1785': 582, '1786': 583, '1787': 584, '1788': 585, '1789': 586, '1790': 587, '1791': 588, '1792': 589, '1793': 590, '1797': 592, '1819': 616, '1820': 617, '1821': 618, '1822': 619, '1823': 620, '1824': 621, '1825': 622, '1826': 623, '1827': 624, '1828': 625, '1829': 626, '1830': 627, '1831': 628, '1832': 629, '1833': 630, '1834': 631, '1835': 632, '1836': 633, '1837': 634, '1838': 635, '1839': 636, '1840': 637, '1841': 638, '1842': 639, '1843': 640, '1844': 641, '1845': 642, '1846': 643, '1847': 644, '1848': 645, '1849': 646, '1850': 647, '1851': 648, '1875': 671, '1877': 674, '1878': 675, '1879': 676, '1880': 677, '1881': 678, '1882': 679, '1883': 680, '1884': 681, '1885': 682, '1886': 683, '1887': 684, '1888': 685, '1889': 686, '1890': 687, '1891': 688, '1892': 689, '1893': 690, '1894': 691, '1895': 692, '1896': 693, '1897': 694, '1898': 695, '1899': 696, '1900': 697, '1901': 698, '1902': 699, '1903': 700, '1904': 701, '1905': 702, '1906': 703, '1907': 704, '1908': 705, '1909': 706, '1910': 707, '1911': 708, '1912': 709, '1913': 710, '1914': 711, '1915': 712, '1916': 713, '1917': 714, '1918': 715, '1919': 716, '1920': 717, '1921': 718, '1922': 719, '1923': 720, '1924': 721}}
650 None
652 None
653 None
659 None
660 None
520 None
523 None
```


## [2026-09-06T15:12:49.428Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} NR==516' BQT_v3_pages.txt"
}
```


### [2026-09-06T15:12:51.443Z] TOOL RESULT

```
[pdf page 516]
۷۲۳

کوچ ‎BS‏ - ازمتزل بمنزلی ‎Ko‏
‎dB‏ و تحوبل کردن را گوبند - و کنابه از
گربختن - وغروب کردن هم‌هست .

کوچ و بلوچ ۱ - سم بای ‎aml‏
‏ولام » این لفت از توابع است. و نام طایفه ای
‎ach‏ ازسحرانشینان که در کوه‌های اطراف کرمان
توطن‌دارند و گویند ایتها ازعربان حجازهدرحرفت
‎ole!‏ جنک و خونریزی ودزدی وراهزلی باشد.
‎HSI‏ بیگانه‌ای ‎wats‏ یکدیگر را بکشند
ومال ‎Gad‏ را تاراج کنند و همچنین‌برادران
و خویشان وقرابنان و دوستان با هم‌جنگه کنند
و اين فعل را بسیار خوب دانند ؛ ویضی گنه

کوچه ۴ - بن اول وفتح جی‌فارسی,
راء کوچك و تک را ‎ae ag”‏ راه بز رکه
وفراخ راکو و کوی خوانند؛ وبعضی گویندیمعنی
برزن است که بمربی محله خوانند.

کوچه باستان ‎be‏ بای ابجد وسین
معقص . کنابه از دنیا وعالم است .

کوچه خر ‎Gis bo‏ شله دار

وطای بی‌تفطه ‎be Sines‏ باستان است کهعالم

کود

+ ‏باشد‎ Gay

کوچه فتادن - ‎HLS MS‏
غریب شدن و بغربت افتادن باشد ..

کوخ « بنم اول وسکون ثابی مجهول
وخای نقطه‌دار : خاله‌ای باشد که ‎VT‏ از چوب
و لی و علف سازند ۴ - و خانة بی روزن را لیز
کربند ۴ = و کیامی که ازآن حصر بافند و در
خراسان خریزه آونگ کنند 6 - و چرك کنج
و گوشهای چشم را هم میگویند - و بمعنی کرم
هم‌آمده است چنانکه گوبند « ‎grein‏ کوج
افتاده است © یعنی کرم افتاده است .

کو خاك - ‎pe‏ اول وفنح‌خای تقطه‌دار
پروزن کوچك » خوشة انگور را کوبند و جربی
خصله خوانند ‎٩‏ ؛ و باین ممنی بفتح آول ‎By‏
‏وسکون تاد وهی هم‌آمده است ۰

کوه - بغتح اول و شم ثالی و سکون
دال ابچد , مخفف کبود است و آن رنگی باشد
معروف ۴ - و جنم اول و الی مجپول بر وزن
‎rye‏ توده و خرمن غله را کویند۸ - وأباری که
برزمین زراعت ریزند تا زمین قوت گیردوزراعت
خوبآید ۸ - و ترجمةٌ مجموعههم هست که در

۱ - نام دوطايعةً مجاور هم ساکن مکران است : رك :کوج ( ح۳ ‎bate‏ قبل ) :

کرین کرد ازان نامداران سوار
‎shy ile‏ پاری» کوچ ‎coke‏

دلیران جنگی ده و دو هزار
زگیلان جنکی‌ودشت سروج ۰

فردوسی طوسی « شاهنامة بخ ج ۳ ص ‎OA‏

۴ - از :کو ( ۳ کوی )۲ چه ‎ys)‏ صفیر ) ‎OS!‏ 60026 , فریزندی ویرلی

8 نطنزی ۲008 2۰ . ۰ص ۰۲۹۰ , سمنالی 8 ,سنگری » سرخه‌بیولاسگردی
6 شهیرزادی 108 2۰. ۲ ص ۰۱۸۸ کردی خراسانی ( شرقی ) 6062۳ « ژابا
‎_?f‏ اسح بضم‌فاست مخفف «آفتادن»۰ ۴ -کردی ۲۵۲۱۲ ( کلبه. مصفر«کوج»)
«زابا ص۳۸۷ ؟ ‎ES eee‏ کازة ازنی وکلك ومانندآن بی‌روزن .کاخ مثله.» «منتهی‌الارب *:
‎Ss‏ دو روزه کاخ کوخی است

ص۳۸ .

در ‎ly‏ محمدی_ ‎eld‏ است .

Lis King? ‏شروایی‎ gi
‏مسعف > لوخ » (هم.) روخ (هم) . ۲ رل : السامی‌فی‌الاسامي در‎ -
80008 ‏کوت , اوستابی و ساد.کریت‎ A cay Se ‏:کبود‎ dy ۷...» ‏ممنی « خصلة‎
‏پلیدی آدمی و جانوران است که جهت‎ gar ‏پس لفة‎ (LIT) kot : ‏قی‎ , (Le) ‏(که‎
‎. ‏قوت بر زمین زراعتی ریزند . رگ : هرمزدنامه ص ۳۱۷-۳۱۹ . ره : ح ۱ صفحا بعد‎
```


## [2026-09-06T15:13:03.077Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN printed 202 (leaf 226) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==227' SYN.txt | head -50"
}
```


### [2026-09-06T15:13:05.072Z] TOOL RESULT

```
=== SYN printed 202 (leaf 226) ===
or the ‘hunt’ and ‘hunter’ are obvious cognates of the verbs.
1. Grk. é@npéw, Onpebw, fr. Onp ‘wild beast’ (3.11).
Grk. xuvnyeréw, xuynyew, fr. the earlier xuvn‘yerns (Hom.), xuvnyés ‘hunter’, cpds. of xbwy ‘dog’ and é&yw ‘drive’.
2, Lat. vénadrt (> Rum. vina), prob. (with grade *wén- beside *wen-) : Skt. van- ‘seek, desire’, OE winnan ‘strive, fight’, etc. Walde-P. 1.230. Ernout-M. 1085.
Lat. sectart ‘follow, pursue’ also used for ‘hunt’ animals, fr. *sectus, old pple. of sequi ‘follow’ (10.52).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Fr. chasser, Sp. cazar fr. for Lat. captare ‘try to
fee ize e’ (frequent. of capere ‘Selze,
monte ‘mountain,
idim (also ‘fish’), epd. of Pedersen 2.492. NIr. fadhachawm, fiadhuighim, fr. ie
, is fr. fiadh fiadhach ‘hunt oe ae ie fi cd iq”ld animal’, now Geer WW i the sbs., cf. also Ir. selg, NI. sealg, ) hunt? and NIr. sealgaire ‘hunter’, belonging with the following.
W. hela, Br. hemolc’hi (for holc’hi), with Ir. selg ‘hunt’ (sb.) : Skt. srj- ‘loose, emit, shoot’. Semantic de- yelopment in Celtic through loosing the hunting dogs (cf. Skt. srjatt. cgunas). Walde-P. 2.508. Pedersen 1.106.
Br. chaseal fr. Fr. chasser (above, 2).
4, ON veida, OE we&pan (with nouns for ‘the hunt’ ON veidr, OF wap), OHG weidon (also ‘pasture’, NHG wevden, 3.15), fr. an extension of *we7- in Lith. veju, vyti ‘pursue’, Skt. veti ‘seeks, fol- lows’, Av. vayeiti ‘pursues’, etc. Walde- P. 1.230. Falk-Torp 1361 f.
OE huntian (and hunta ‘hunter’), ME hunte, NE hunt : OE hentan ‘seize’,
*em-
ANIMALS
Digitized by Arya Samaj Foundation Chennai and eGangotri
191
Goth. fra-hinpan ‘capture’, Sw. hinna ‘reach’, wpphinna ‘overtake’ (10.54) fr. parallel root forms (*ken-d-, *ken-t-?), but outside connections dub. Walde-P. 1.460. Feist 161. NED s.v. hunt. OHG jagon, MHG, NHG jagen (> Dan. jage, Sw. jaga), Du. jagen, etym. dub., but perh.: Skt. yahu-, yahva- ‘restless, active, swift’, (pra-)yaks- ‘has- ten, press on’, Grk. txavdw ‘desire’, etc. Walde-P. 1.195f. Weigand-H. 1.940.
5. Lith. medzioti, Lett. medit, fr. Lith. medis ‘tree’, older sense ‘woods’, Lett. meés ‘woods’ (1.41). Mithl.-Endz. 2.590, 611. Cf. Sp. montear, above, 2.
6. ChSl. SCr., Boh. loviti, Pol. towié, polowaé, deriv. of ChSl. lovit ‘hunting, booty’ : Grk. deta ‘booty’, Lat. lucrum ‘gain’, Goth. laun, OHG lon ‘reward, pay’, etc. Walde-P. 2.379f. Berneker 7385 ff.
Russ. ochotit’sja refl. (with na ‘on’ when used transitively) fr. ochata ‘de- sire, will, hunt, chase, sport’ : chotét’, ChSI. chotéi ‘wish’ (16.61). For the change ‘desire’ > ‘hunt’, cf. Skt. lubdha- ‘greedy’, as sb. ‘hunter’. Berneker 398 f.
7. Skt. mrgaya-, fr. mrga- ‘wild ani- mal, game’ (8.11).
3.81 INSECT
Most of the European words for ‘in- ot (generic, but of somewhat chang- a Sometimes including worms, ultimately to Aristotle's naming of in-
their bodies. which either € accepted technical vabedyz, Boh. hmyz, Pol.
colloquial expressi ebug in
```


## [2026-09-06T15:13:10.179Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==238' SYN.txt | head -60"
}
```


### [2026-09-06T15:13:12.077Z] TOOL RESULT

```
itt, meso Be igtiags Sw. kétt SCr. meso Sp. carne OE Sl@sc Boh. maso Rims carne ME fleshe Pol. —_ mieso ae feoil, cua NE flesh Russ. mjaso Nir, feoil oe é ei Skt.  mdnsa-, mas- ‘cig, evs Av. av- (NPers. gust Br kig giaiad tS vleisch es be Most of th ee € words ‘ : ot all, are also ead a flesh’, though | semantic sources, where clear, are partly Meat (5,61), Words Ae Beshy as food, | ‘covering, surface’, referring to ‘flesh’ vs. Wed, ep. in. eco] ‘or ‘flesh’ are also | ‘bone’, but oftener ‘cut’, or ‘raw and €ccl. writings, for ‘body? : x ; : ale nversely some oeds f ody’, bloody’, or name of an animal, in all © used for ‘flesh’ or ‘body’ are | these cases referring to the flesh of an
Cf. 4.11. The
animal cut off for food or sacrifice.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
202 SELECTED INDO-EUROPEAN SYNONYMS
1. IE *mémso-, *més-, root connec- tion? Walde-P. 2.262. Feist 361.
Goth. mimz (once, here ‘meat’; also mammo prob. related); Lith. mésa, Lett. miesa, OPruss. mensa; ChSl. meso, etc., general Slavic: Skt. marisa-, mas-; Arm. mis; Alb. mish; Toch. B misa (pl. tan- tum); with other meanings, Grk. punpds ‘thigh’, Lat. membrum ‘part of the body’, Ir. mir ‘portion, morsel’, etc.
2. Grk. capt : Av. @wares- ‘cut’, with development as in Lat. card (below, 3). Walde-P. 1.751. Boisacq 854.
Grk. xpéas (but mostly ‘meat’) : Skt. kravis- ‘raw flesh, carrion’, krira- ‘bloody, raw’, Av. xri- ‘raw flesh’, Lat. cruor ‘blood from a wound’, OE hréaw ‘raw’, Lith. kraujas ‘blood’, etc. (4.14). Walde-P. 1.478 ff. Walde-H. 1.295.
3. Lat. card, gen. carnis (> It., Sp., Rum. carne, Fr. chair) : Umbr. karu ‘pars’ (but also karne, etc. ‘flesh’), Osc. carneis ‘partis’, Umbr. kartu ‘distributo’, Grk. xelpw ‘shear’, OE sceran ‘cut, shear’, etc., IE *(s)ker- ‘cut’. Develop- ment in Italic to ‘portion’ in general, then esp. ‘portion, cut of the flesh, flesh’. Walde-P. 2.575. Ernout-M. 156. Walde-H. 1.170.
4. Ir. féoil, etym.? Pedersen 1,139 compares W. gwanu ‘pierce’, OF wund ‘wound’, etc. (Walde-P. 1.212, Stokes 259, both without féoil).
Ir. cia (K. Meyer, Contrib. 540), etym.?
W. cig, Br. kig, OCorn. chic (Ir. cich ‘female breast’), outside connections? Pedersen 1.51. Walde-P. 1.334.
W. cnawd, prob. fr. *kné-to- : Grk. xvaw ‘scrape, scratch’, ultimately con-
nected with Ir. cness ‘skin’ (4.12) in both cases orig. ‘surface’. Vendryes, Wart. U. Sach. 12.248.
5. ON hold : OF hold ‘carcass’, Ty, colinn ‘body’, etc. (4.11).
ON horund ‘flesh, skin’ (for actual uses, cf. Fritzner, and Vigfusson) : Lat, cortum �
```


## [2026-09-06T15:13:19.480Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"نهفتن\" MON_part1.txt MON_part2.txt | head -10\necho \"--- FFD p.80 (pdf 85) ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==85' incoming/FFD/FFD_pages.txt | head -40"
}
```


### [2026-09-06T15:13:21.974Z] TOOL RESULT

```
MON_part1.txt:11426:شدن» روی نهفتن» در برده شدن. (نط.) 
MON_part1.txt:11903:گرفتن» ترس به دل نهفتن. به خود باز آمدن؛ 
MON_part1.txt:12755:اسرار: 5۳ [ع.] (مص م.) نهفتن» بوشیده 
MON_part1.txt:14020:اضمار: توص [ع. ۰] (مصم .) نهفتن» نهان 
MON_part1.txt:14021:داشتن» به دل نهفتن. ضمیر آوردن سرای 
MON_part1.txt:33437:کردن» پوشانیدن فرا گرفتن. نهفتن» مخفی 
MON_part1.txt:61075:دس: (025)5 [ع.] (سص‌م.) نهفتن» پنهان 
MON_part2.txt:74504:سرگوشی» زیرگوشی. (تص.) نهفتن آفات 
MON_part2.txt:81459:نهفتن» نهان کردن. (ص.) بوشیده؛ پنهان. به 
MON_part2.txt:81472:نهفتن: 
--- FFD p.80 (pdf 85) ---
[pdf page 85]
ار فعلهای فارسی دری
نوْشتن,» نوردیدن
نوشت « ایرانی باستان 21-۵7۶-1۵*. برای 1۵ > آراست. 8 پیشوند فعلی است.
: 4 صورت اصلی ۷87۶ است» 1 پیش از ۲ به 5 بدل شده است. ۷87۲ به معنی «گشتن»)
است و خود «گشتن» هم از این.ریشه آمده است. نوردید ماده ماضی جعلی است که از
مادةٌ مضارع با «ید» ساخته شده است.
نورد + ایرانی باستان ۴81-۷۵۲۲۵ برای 2-> آرای.
نهادن
نهاد « فارسی میانه 224 < ایرانی باستان 143-1۵:*. برای 1۵ > آراست. 7
پیشوند فعلی است. ريشهٌ 13 به معنی «گذاشتن» است.
نه « فارسی میانه 7 + ایرانی باستان 21-42-۵*. برای 2 -> آرای.
نهفت ۰
نهفت « فارسی میانه 218011 + فارسی باستان 00-1۵ -ط* + ایرانی باستان
2 برای 12 > آراست. 1 پیشوند فعلی است. 800 صورت اصلی ۶۶ است. 0
پیش از 1به ۶ بدل شده است. ريشهٌ ۶0 به معنی «آراستن» است.
نهنب < فارسی میانه 200000 < فارسی باستان 21-0020 < ایرانی باستان
۶21-۶ 2 پیش از 0 برای ساختن مادهٌ مضارع از ريشه آورده شده است.
(سفتن) هم از ريشهٌ 9 آمده است > سفتن.
نیوشیدن
نیوشید < فارسی میانه 5870قا:. 5576انه مادة ماضی جعلی است» از مادة مضارع
ساخته شده است.
نیوش « فارسی میانه 2105 « ایرانی باستان 21-82053-8*. برای 2 آرای. 1 پیشوند
فعلی است. ريشهٌ 8895 به معنی «گوش کردن» است. «گوش» هم از ريشةٌ 8203 آمده
است. صورت فارسی میانهٌ «گوش» 805 است. 58و از 825-8 * ایرانی باستان آمده است.
2 پسوند است.
```


## [2026-09-06T15:13:33.285Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n \"^gāw\\|^gāw \\|^gōspand\\|^gōšt\\|^gūh\\|^nihumb\\|^nihuft\\|^gēhān\\|^gāwān\\|^gōpān\" PHD.txt | head -20\necho \"-- alt --\"; grep -n \"gospand\\|gowspand\\|gwspnd\\|gwšt\\|nhwmb\" PHD.txt | head -20"
}
```


### [2026-09-06T15:13:33.385Z] TOOL RESULT

```
=== PHD ===
513:nihuftan 60 nizar
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
5564:gāwars dānistan appar-! appurdan! dānišnūmand dānišn jahūd yākand yākand
-- alt --
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
5440:gospandéihrag "Šā Ca» 10335 P
```


## [2026-09-06T15:13:40.325Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"gāw \\[[^]]*\\][^.]*\\.\" PHD.txt | head -5\ngrep -o \"gūh \\[[^]]*\\][^.]*\\.\" PHD.txt | head -5\ngrep -o \"gēhān[^.]*\\.\" PHD.txt | head -3\necho \"=== NYB ===\"; grep -n \"gōspand\\|gospand\\|gwspnd\" NYB_vol2_glossary.txt | head -5; grep -n \"nihumb\\|nhwmb\" NYB_vol2_glossary.txt | head -5; grep -n \"gēhān\\|gehan\" NYB_vol2_glossary.txt | head -5"
}
```


### [2026-09-06T15:13:40.514Z] TOOL RESULT

```
gēhān [gy)?>n! | = M, N gihān, jahān] world.
=== NYB ===
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
570:äp-eihrak [’p'-cyhlk'] containing the seed of the waters 87°; àp- u damik- u urvar- u gospand-cihrak containing the seed of the waters, the earth, the plants and the cattle 8711. — Av. (103 sq.) af$-cidra-; v. cihr and -cihrak.
1130:-cihrak [cyhlk'] = cihr used as the last element of an adj. compound, v. dp-~, damik-~, gospand-—, mart6m-~,urvar-~. Cihrāzātān [cyhl’c’t’n'] patron. 116". — From n. pr. C?hrāzāt, ci āzāt.
1698:göspand [gwspnd; KYN?] cattle in gen- eral, but esp. small cattle, sheep and goats, as distinguished from horses and cows, coll. 381%. 3916 ete., pl. cas. rect. 9417.20, 10416; pl. cas. obl. —-än 1” [KYN^-n'] 45%. 802. 861%, 893. 905-6, 943. 9724. 981, 1028; — apazär-göspand v. apazür. — Av. (506) gaospenta-; Paz. gospand, NP gospand, gosfand.
1699:gospand-cihrak [~-cyhlk'] containing the seed of cattle 879, — V. cihr, cihrak: cf ap-cihrak, gö-cihr.
2716:nihuftan [nhwptn'] nihumb- [nhwmb-] to conceal, to cover: api-$ apar varr nihuft he covered himself with his garment 56?’ ; apar ~ to conceal, to keep from the knowledge of 8011 = bē ~ 8014 (read ‘L menišn 1. 13); in both places restore the reading of the MSS: nhwmbt' = nihum- bet (not -byt' = -bēt). — MPrs nhwft nhwmb- or nhwm- = nihumm- with assi- milation (A-H II, BBB); Paz. nahuftan nahumb-; NP nihuftan nihumb-. Verbum 200; Bailey, ZP 83 (82 n. 5).
6052:nhwft, nhwmb- or nhwm-:
1655:gēhān [gyh’n'] pl. and coll., the world of creatures, men and animals, esp. the world of man: astömandän ~ 3913; han 4 mänisnömand (q.v.) göspandömand ~ 5714-15; herds of grazing animals 4913; — the material world in general: 21. 418 etc. passim. — < *gaidānām, gen. pl. of Av. (476 sqq.) gaēdā-; OP gai0à- “live-stock’; Aram. lw. (Targ, Talm) gyty ‘herds’; MPrth gyh (< gaia) ‘world’, pl. gyh?n ‘worlds’; Paz. geha; NP gehän, gihän, jihän. Cf gétah.
2524:mēnišn (mynšn'] thinking, thought, mind: together with gób?sn and kunišn v. göbisn ; Zartuxšt had ~ 4 fräröntar hac hamak gēhān a mind more righteous than (that of) all human beings 54%; ~ i fräröneh the way of thinking of honest people 6414; — ~ nihátan 6 to contemplate, to set one's mind on 5??*; 6 hän i ölsän ~ apar Sut hénd they inspired them 403-4; v. also apakandan, bastan, bastišn, nihä- tan, čpastan, viskaftan, vinäsitan; — pat ~ 4 Pourusäsp bim apakand 481911; pat ~ in my mind, through my inner senses 51%; hàn + či dētsr pat ~ his (spiritual) eye in his mind = his inner intuition 5226-27,
3270:rat [lt'] "genius", divinity or tutelary spirit presiding over one of the categories or classes into which all beings and things of the good creation are divided: ap?-Sün ~ Gēpet and their genius is G. 8674-25; Zartuxšt is ašūkān ~ the genius of (all) the Righteous 106!; he is in Avestan terminology the ahü and ratu of the world, hence the abstr. ahü-u-ratü-eh 4 gēhān 55%. — Av. (1498 sqq.) ?ratu-; NP rad ‘intelligent, learnd', ‘a high priest of the Magi'. As to the doctrine, v. Modi, Ceremonies 330—334.
3885:uzvühik ["wzw'hyk] brought out, spread abroad: yazdān ... andar gēhān ~ srav burt the message was announced to the world by the gods 55**, v. next w.
4891:gaidā-: gēhān
```


## [2026-09-06T15:13:46.733Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:13:46.760Z] TOOL RESULT

```


```


## [2026-09-06T15:13:51.052Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%E1%B9%93ws",
 "prompt": "Give the reconstruction, gloss, declension (nom/gen/acc), and the list of descendants (Indo-Iranian, Greek, Latin, Germanic). Also note any derived terms and the references cited."
}
```


## [2026-09-06T15:13:52.463Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%88",
 "prompt": "Give the Persian entry for گاو: etymology (Middle Persian, Proto-Iranian, PIE forms), meaning, and derived/related terms such as گوساله, گوسفند, گوشت."
}
```


### [2026-09-06T15:13:57.859Z] TOOL RESULT

```
# Proto-Indo-European *gʷṓws

**Reconstruction:** *gʷṓws (m or f)

**Gloss:** "cattle"

**Key Declension Forms:**
- Nominative singular: *gʷṓws
- Genitive singular: *gʷéws
- Accusative singular: *gʷṓm

**Major Descendants:**

*Indo-Iranian:* Proto-Indo-Iranian *gā́wš

*Greek:* Proto-Hellenic *gʷous

*Latin:* Proto-Italic *gʷōs

*Germanic:* Proto-Germanic *kōz

**Derived Terms:**
- *gʷow-kʷólh₁-o-s ("cowherd")
- *gʷów-yo-s
- *gʷow-wr̥sen- ("male cow, bull")
- *gʷow-dʰeh₁- ("cow-suckling")

**Notable Linguistic Issue:**
The reconstruction notes indicate "there is no trace of the e-grade" in this word, which is unusual. Some scholars propose analyzing it as a proterokinetic u-stem *gʷéh₃-u-s to connect it with *gʷeh₃- ("to graze").

**Key References:** Pokorny (1959), Ringe (2006), Wodtko et al. (2008)
```


### [2026-09-06T15:13:59.729Z] TOOL RESULT

```
# Persian Entry for گاو

## Etymology

The word traces back through multiple language stages. It derives from Middle Persian (TWRA /gāw/), Old Persian (*gāuš), Proto-Iranian (*gā́wš), Proto-Indo-Iranian (*gā́wš), and ultimately Proto-Indo-European (*gʷṓws).

The entry notes cognates including English "cow," Urdu گائے (gāe), Hindi गाय (gāy), Avestan 𐬔𐬀𐬊 (gao), Ancient Greek βοῦς (boûs), and Latin bōs.

## Meanings

The noun denotes:
1. "cow, bull, cattle" - the domesticated bovine animal
2. In astronomy, "the constellation Taurus"

## Derived and Related Terms

Selected compounds include:
- **آبله گاوی** (cowpox)
- **گاو دریایی** (manatee, literally "sea cow")
- **گاومیش** (buffalo)
- **گاوآهن** (plow)
- **گل گاوزبان** (Echium plant)
- **گمیز** (cow urine) - listed as a related term

Note: The requested terms گوساله (calf), گوسفند (sheep), and گوشت (meat) do not appear in this entry's derived/related terms sections.
```


## [2026-09-06T15:14:03.108Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B4%D8%AA",
 "prompt": "Persian گوشت: etymology (Middle Persian, Proto-Iranian, Avestan, PIE), meaning, cognates."
}
```


## [2026-09-06T15:14:04.403Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF",
 "prompt": "Persian گوسفند: etymology (Middle Persian gōspand, Avestan gaospəṇta-), meaning, and the components."
}
```


### [2026-09-06T15:14:09.791Z] TOOL RESULT

```
# گوشت (Meat) - Etymology and Linguistic Analysis

## Meaning
The word **گوشت** means "meat" across multiple languages including Persian, Urdu, Punjabi, and others.

## Etymology Chain

**Persian Origin:** According to Wiktionary, the Persian term was "inherited from Middle Persian" and traces back further to "Proto-Iranian *gawštaH."

**Historical Development:** The word followed this progression:
- Proto-Iranian (ancestor language)
- Middle Persian (classical form: gwšt')
- Modern Persian and descendant languages

## Cognates and Descendants

The term spread across numerous related languages:

- **Turkic languages:** Uzbek (goʻsht), Uyghur (gösh), Turkmen (göş)
- **Indic languages:** Hindi (गोश्त), Bengali (গোশত), Gujarati (ગોશ્ત)
- **Other Iranic:** Kyrgyz (гөш), Tajik (гӯшт)

Most borrowed the word directly "from Classical Persian," demonstrating Persian's linguistic influence across Central and South Asia.

The documented progression shows a stable root form persisting across millennia of linguistic evolution.
```


### [2026-09-06T15:14:11.990Z] TOOL RESULT

```
# گوسفند (Gosfand) - Word Summary

**گوسفند** is the Persian and Urdu word for "sheep."

## Etymology

The term has ancient roots tracing back through multiple languages. It derives from Middle Persian *gōspand*, which itself comes from Avestan *gao-spəṇta-*, meaning "beneficent cow." This Avestan compound combines two elements: *gao-* (cow) and *spəṇta* (holy).

## Linguistic Details

The word appears in both Persian and Urdu dictionaries. In Persian, it can be pluralized as *gōsfand-hā* or *gōsfandān*. The Urdu version is classified as feminine and was borrowed from Classical Persian.

## Related Terms

The Wiktionary entry also notes an alternative Persian form: *gōspand*, and references a related word *mīš* (another Persian term for sheep).

The word's presence across 23 language versions of Wiktionary reflects its importance in languages across Central Asia, South Asia, and beyond.
```


## [2026-09-06T15:14:18.312Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D9%87%D9%81%D8%AA%D9%86",
 "prompt": "Persian نهفتن: full etymology (Middle Persian, Proto-Iranian root, prefix), meaning, and any cited references (Cheung, Hasandust)."
}
```


## [2026-09-06T15:14:19.063Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%88%D8%AF%D9%87",
 "prompt": "Persian توده: etymology (Middle Persian, Proto-Iranian), meaning."
}
```


### [2026-09-06T15:14:24.055Z] TOOL RESULT

```
# Persian Verb نهفتن (nohoftan)

## Etymology
The word derives from **Middle Persian** nhwptn' (/⁠nihuftan⁠/), tracing back through Persian linguistic history. The entry notes it comes "From Middle Persian" but does not provide extended Proto-Iranian etymological details or citations to Cheung or Hasandust in the visible content.

## Meaning
The verb means "to hide; to conceal," with the synonym **پنهان کردن** (penhân kardan) noted in the dictionary entry.

## Conjugation Details
The word has two main stems:
- **Present stem:** نهنب (nohomb)
- **Past stem:** نهفت (nohoft)

Various dialectal pronunciations are documented, including Classical Persian, Dari, Iranian Persian, and Tajik variants, each with distinct IPA transcriptions reflecting regional phonological differences.

**Note:** The Wiktionary entry does not include the specific scholarly references you requested (Cheung, Hasandust) in its visible sections.
```


### [2026-09-06T15:14:25.438Z] TOOL RESULT

```
# توده (Tude) - Persian Etymology and Meaning

## Etymology

The Persian word **توده** derives from Proto-Iranian *taw(H)táH*, ultimately tracing back to Proto-Indo-European *tew(H)téh₂*, meaning "people, tribe, men-at-arms."

Cognates exist across Indo-European languages, including Latin *tōtus*, Lithuanian *tautà*, Irish *tuath*, and Gothic *þiuda*.

## Meanings

In Persian, توده has several definitions:

1. **Physical sense**: "heap, pile, mass"
2. **Social sense**: "people, folk, masses, nation, tribe, population"
3. **Accumulation**: "provision, accumulation, supply"
4. **Archaic cultural meaning**: "the language of people, popular culture and legends, folklore"

The word reflects its etymological root, with meanings oscillating between collective physical masses and groups of people or cultural traditions.
```


## [2026-09-06T15:14:31.630Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/buffalo",
 "prompt": "Give the full etymology of buffalo, including Greek boubalos and whether it is connected to bous 'ox'."
}
```


## [2026-09-06T15:14:32.286Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/butter",
 "prompt": "Give the full etymology of butter, including Greek boutyron, bous, tyros, and Latin butyrum."
}
```


### [2026-09-06T15:14:36.058Z] TOOL RESULT

```
# Buffalo Etymology

Based on the web page content provided, I can only offer limited information about buffalo's etymology:

The page indicates that "buffalo" derives from **"Medieval Latin bufalus, variant of Latin bubalus 'wild ox'"** according to the meta description.

Unfortunately, the page content does not include the full etymological details you're requesting. Specifically, it does not provide:

- Information about the Greek *boubalos* connection
- Discussion of whether it relates to *bous* (meaning "ox")
- The complete etymological chain beyond the Latin forms

To obtain the comprehensive etymology including Greek cognates and their relationships, you would need to access the full article content on etymonline.com, which does not appear to be included in the provided page data.
```


### [2026-09-06T15:14:39.363Z] TOOL RESULT

```
# Etymology of Butter

The word "butter" traces back through multiple languages and ancient roots:

**Latin Foundation:**
The term comes from Latin *butyrum*, which was borrowed into Old English as *butere*. This Latin word also influenced Romance languages like Italian *burro* and French *beurre*.

**Greek Origin:**
Latin *butyrum* derives from Greek *boutyron*, which scholars believe means "cow-cheese." As the source explains: "This is apparently 'cow-cheese,' from *bous* 'ox, cow'...+ *tyros* 'cheese'." Both components trace to Proto-Indo-European roots (*gwou-* for bovine animals and *teue-* meaning "to swell").

**Historical Usage:**
Interestingly, while butter was "used from an early date in India, Iran and northern Europe," it wasn't common in ancient Greece and Rome, despite the Greek name's origin. The historian Herodotus notably described it among Scythian oddities.

**Linguistic Note:**
The Greek etymology might represent folk etymology of a Scythian word, suggesting the product's origins in pastoral cultures rather than Mediterranean civilizations.
```


## [2026-09-06T15:14:45.862Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"BUFFALO [a-zA-Z()*-]*\" AHD_watkins1985.txt | head -5\ngrep -o \"BEEF [a-zA-Z()*-]*\" AHD_watkins1985.txt | head -5\necho \"--- IEC gwou ---\"; grep -n \"^g[^ ]*ou-\\|^gou-\\|^gwou\" IEC.txt | head -20"
}
```


### [2026-09-06T15:14:45.967Z] TOOL RESULT

```
BEEF gWou-
--- IEC gwou ---
4996:ghrou- — gh, ghru- (ghəru-)
5199:guou- (gu-) “ox; filth’. See guóu- and cpds. R- and z-gde forms in Skt. eu beside -gaváb, cpds.; OBr. bu- in bu-es ‘stable’; OW bu- in bu-al *drinking-horn'; ON kýr, as, ds kú; R cf. gumnó, Cz. humno *threshing-floor, barn’, fr. *guou- or *gueu-mn, lit. *ox-press' beside Cz. hov-ézí, adj. ‘beef, hov-ado ‘beast’; hov- no, R gov-no “dung”
5322:guou-, element of many cpds. in sense of ‘cow, cattle, beast; dung; lump’ etc. See the following entries, and guðus for the simplex
5323:guou- ‘tumour, ganglion, boil’. See follow- ing entries Skt. cf. gav-ininka, f. dual (queried: ‘groin’); Gk. cf. bou-bon ‘groin, tumour in groin’; Icel. kaun ‘boil’. An extn. appears in Pol. guz ‘boil, tumour, knot if not a R LW, cf. gonĝ-.
5362:guou-sthos, à, io (guouəst-, gust-) Skt. gosthah, -sthà *cowshed'; Per. güst ‘meat’; Rustic Lat. in It. busto “bust; Olr. buas “wealth in cattle’; OCS gusta ‘dross
5427:gur-nou- (analytical form of) gurnüs, à, gur- uoni, guernus, à, guernouos, etc. (cf. gurus ‘heavy’ and nàus, nous "boat from the shape of the nether stone of the handmill when worn down by an upper stone rolled upon it). Arm. erkan, a-st.; Oss. cf. kwrói, krói (for *gür-?) ‘mill’; Gk. cf. güris Tine flour”; Olr. bráu, Ir. bró; Cor. brow; OW breuan; MHG kürne; OCS Zrüny, gs Zrünüve beside Zrünü- vü, m.; Li. girna; Latv. dzirnas, f. pl. beside dzirnus & dzirnavas ‘handmill, millstone’. E- grade in Go. -qairnus; OHG quirn, quirna; MHG quirn-, kurne-stein; OS quern, u-st.; OFris. quern; OE cweorn; G Querne 'quern'; ON kvern, pl.-ir. f. WP I, 685
```


## [2026-09-06T15:14:55.599Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC guous ===\"; sed -n '5360,5375p' IEC.txt; grep -n \"^guóus\\|^guous\\|^guuthos\\|guthos\" IEC.txt | head\necho \"=== HUB gust/946 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==957' HUB.txt | head -40"
}
```


### [2026-09-06T15:14:59.272Z] TOOL RESULT

```
=== IEC guous ===
clude: Arm. ku ‘dung of deer": Vedic á-guh *cowless'; anu-guh 'droving'; Lat. bu- in bu- bulcus; It. (Umbrian) bi- in bi-folco ‘cow- herd); Slovene go-máz ‘reptile’
guðuså “mire, cowdung'. Cf. guoutos Fr. cf. bouse ‘mire’, boue *mud' (fr. a Celtic source); W baw ‘dung, filth’; Fris. kweaze ‘mire’. (Isophonic: MHG kuose ‘she-calf’)
guou-sthos, à, io (guouəst-, gust-) Skt. gosthah, -sthà *cowshed'; Per. güst ‘meat’; Rustic Lat. in It. busto “bust; Olr. buas “wealth in cattle’; OCS gusta ‘dross
guðutos, à, om, ios, io (guot-, güit-) (an asso- ciate of guüus, q. v.) | Skt. gota ‘cow’; güthab ‘dung’; Av. güo, Per. güh, id.; Arm. gu, o-st. (ambig.) ‘dung of wild animals’; Arc. bousós 'cattle-Crun' beside -pót&, -páte (in ois- “dung on sheep's rear); isophonic in Gk. boütes ‘herdsman’; bousé “female slave’ (used as cowgirl); Hes. bousía ‘a root resembling turnip’, MHG quot, quát, OE cwead, OFris. quad ‘dung’; adj. ‘bad’; LG (z-gde) küt ‘filth from entrails’; (Gmc. forms fr. *-dh- or *-tós, -tóm); Blg. cf. gutav ‘bad’; Li. gúotas “herd of small animals’; guotë, guo- Cià “orange-agaric”
guðutros, om (guutro-) (an association of COWS) Skt. gotrám 'cowshed'; LLat. cf. botrix *excre- ment’; W budr ‘filthy’
gur-, see gurus. A zero-gde element in Gk. br-iaros, br-ithüs, br-ómos; Lat. br-ütus; Latv. gr-üts
guràun, guràuon, guràán- ‘heavy stone, mill- stone'. WP I, 685. Cf. gurus Skt. gravan “heavy stone’; Per. garan, giran “heavy, dear; Arm. erkan ‘mill’; MIr. bráu, bró, gs. brón, id. beside Mir brón “burden, grief; W breuan ‘handmill’; Br. bréw ‘mill’. Cf. Lat. variant gravamen ‘grievance’
gurebhos, -es-, (gurebhmn, -ón) ‘foetus, in- fant, young animal’. WP I, 689 Gk. bréphos, n.; MHG krébe (?) ‘intestines’; OCS Zrébe beside Cz. hříbě *foal". (For Skt. gárbhah *womb, foetus, infant? see guolbh-)
gureio, gureio “be heavy’. Cf. gurus Skt. gure, mp. (lift beside güráyami, id.; Per. garayam ‘gravitate toward"; Arm. krem ‘bear,
371
carry’; Gk. baréo ‘weigh down’ beside Aeol. boréo, id.; Go. kaürjan, id.
guremó, gurem- ‘roar, rumble’. (Slav., Balt. and Alb. evidence ambig. Cf. guhrem-, and ghrem- (1) & (2). Cf. also WP II, 202 & 308) Av. gram-, v. ‘rage’; Gk. brémo; Ir. cf. breim, pl. breamanna, s. ‘rumbling of bowels’; W brefu “low, bleat’; R gremét ‘rumble, roar’; long-gde in Ukr. hrimaty, Cz. hfímat; also in Li. gremoju, oti *eat noisily', but cf. (? *guh- rém-) in Alb. gromé ‘belch’; Latv. grémens ‘heartburn’ beside Latv. gremot, v. ‘ruminate, chew over’. Variant in Latv. gremzt, v. (2) ‘toar’
gurost- (?) “heavy; weight, heavy substance. Cf. gurus Arm. erkat’, o-st. ‘iron’, OW W Br. Cor. bras ‘big’; Ir. bras “strong, big’; bras-, cpds. Celtic LW (?) in OE brzs ‘brass, bronze’
guriu- “heavy; weight’. Cf. gurus, etc. Hes. bri ‘heavy’; beside brimós ‘big, hard"; brízo “weigh down’; R grivna “gold dollar’; Cz. hřivna (talent weight)
guroghos, (n) (guroĝh-) ‘neck, craw’. Cf. gur- cpds. Gk. brókhos ‘noose, halter; MHG krage “neck, throat, ruff; Du. kraag “collar”; EME craw. (For a possible analysis of Gk. as *gur- and *sogh- “hold”, cf. EME hals-fang ‘pillory’, Lat. colli-strigium)
gurom- ‘bum, rumble, roar’. Cf. gurem-, ghrem- and guhrem- for ambiguities in Alb., S1., and Baltic. Gk. brómos ‘roar’: bronté (tthunder': Alb. grénzé ‘hornet’, fr. *guromta, -tio); OCS (am- big.) gromü ‘thunder’; Li. gramai, mpl. ‘phlegm’
=== HUB gust/946 ===
```


## [2026-09-06T15:15:09.377Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"گاو\" ARY_pages.txt | head -10\necho \"--- latin index GAV/GWOU ---\"\ngrep -n -i \"GWOU\\|GOU-\\|GAV\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-06T15:15:09.449Z] TOOL RESULT

```
294:«شخم» و «آهن) و «جوه و «گاوه و «بز» و «خوکک» نشان می‌دهد که این مردم به کشاورزی هم اشتغال"
302:همریشه» همگی دارای بک معنی نیستند. واژه‌های معدودی مانند «مادر» و دماه» و «گاو» در همه
938:همریشه‌ی مربوط به «اسب» و «گاوه و «گوسفندء و دسگ» و «خوکک؛). همریشگی واژه‌های متعدد
958:کشیشی و آئین‌های مذهبی بود. -تولوس هوستیلیوس (130571118 110178) که جنگاورخشن .|
964:(روحانیون) و «کشاتریاه ۸ (جنگاوران) و «ویسیاء ۷۸/8۸ |
967:۱-روحانیون زرتشتی ۲- جنگاوران ۳- دهگانان.
1023:پدر عروش يا ایل عروس «هدیه؛ (مثلاً چند رس گاو) می‌دادند. در مقابل پدر عروس موظف برد که
1077:‎٩‏ رزمجویی: ویژگی دیگر هند و اروپائیان جنگاوری بود..مردمی که طی چند سده از
1274:«مادر) یا «گاوه با «بوغ) معنی واژه‌های همریشه در زیانهای هند و اروپایی امروزی کاملدً یکی و
2479:۸ (حل نگهدار ی اسب‌ها) و 06۸۷0-57۸۷۸ (محل نگهداری گاوها) از یک ريشه است.
--- latin index GAV/GWOU ---
2431:wcesl Ag OS jT (Legh 5 j)gSi Jove) GAVO-STANA 4 (ml 6, 5 hygSs Jou) ASPO-STANA
7467:. POKORNY, —=~S*«~*~*~*S*« DO, DEDET, DARE LATIN) gaV
12337:KRAVA, GOVEDO GAV (OLD PERSIAN) sla gos),
13050:GAVITI SERBIAN) «gp (IM)BUBINARE = (.4Lt)}(GREEK) gb y
```


## [2026-09-06T15:15:11.972Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '12320,12345p' ARY_latin_index_pages.txt\necho \"=== 13040-13060 ===\"; sed -n '13040,13060p' ARY_latin_index_pages.txt"
}
```


### [2026-09-06T15:15:12.026Z] TOOL RESULT

```
KOMEN (DUTCH) «sacha KAM (TOKHRIAN B) Bs ins
oom! LITHUANIAN) gly} (SANSKRIT) 24 Suites
GATU LATVIAN) (3) gis GAYAM, -GAMAN, GATIS
GATRAM —(OLD IRISH) «Sg p! KAM > ARMENIAN) «g\
NGA ALBANIAN) UST BEMA, BAINEIN H(GREEK) gly
VENIR MATH) 3 4
RaERENCES GEE] cau ateiooring uf
‘POKORNY: 463-464 (OLD SCANDINAVIAN) 48 (64th)
BARNHART: (COME) 192 KOMA
DELAMARRE: (PAS) 84 CUMAN — (OLD SAXON) oS gi pS
MACKENZIE: (STEP) 134 KUMA HOLD FRISIAN) AS 52.3
1ve0 sebG ob, (OLD HIGH GERMAN) oyS glalt
QUEMAN, COMAN
[pdf page 423]
: sie
.
me (OLD CHURCH SLAVIC) ot Gl GAUSH, GAO- (AVESTAN) glios!
KRAVA, GOVEDO GAV (OLD PERSIAN) sla gos),
KROWA > (POLISH) ge) GAW (PAHLAVI) 5 344,
KOROVA, GOVIADO :(RUSSIAN) 53) QUG, YOG MOSSETIC) goss!
KRAVA (CZECH) Say GA (KURDISH) 52,
KRAVA SERBIAN) ype * GOK, GOX BALUCHD) gx sh
KRAVA (BOHEMIAN) go GHWA HAFGHAND) (344) gi) i
KRAVA (SLOVAK) | gel ko -(TORHARIAN A) A 5,55
KARVE (LITHUANIAN) ip) KAU (TOKHARIAN B)B 6
Gvovs (LATVIAN) (2) 9 GAGS, GO- (SANSKRIT) <4 Site
=== 13040-13060 ===

Big iy gles! 205 ol oF

KOT GERMAN) gist -GUTHA, GUTHO = (AVESTAN) (glu)
CWEAD — {OLD ENGLISH) op gdSi GUH, GUHVART §— PAHLAVI) ly,
OLD CHURCH SLAVIC) 345 (53% ct (KURDISH) 25
GOVNO GITH HBALUCHI) <g> sh
GOWNO (POLISH) rice GHUL s(AFGHANI) (3) git
GOVYNO (RUSSIAN) (y=) GUTHAH SANSKRIT) cy Sale
OHAVITI (CZECH) So KU, GUGH., KOY (ARMENIAN) (c+)!
GAVITI SERBIAN) «gp (IM)BUBINARE = (.4Lt)}(GREEK) gb y
OHUDA (SLOVAK) S| gh! QuaD OLD FRISIAN) oS S29
GEDA :(LITHUANIAN) gy) QUAT :(OLD HIGH GERMAN) of giST
[pdf page 448]
TAT phen
BUCK: 216 ‘REFERENCES beth
MALLORY & ADAMS: GwuH = POKORNY SSCS
Vary bu dby MACKENZIE: (EXCREMENT) 113
GAESA, GARSU —(AVESTAN) lesyl
REFERENCES bok, GEs PAHLAVI) 5 3h,
POKORNY, SSS GHESA, QIs MOSSETIC) bal
```


## [2026-09-06T15:15:18.479Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"GAUSH\\|GUTHO\\|GwuH\\|GWOU\" ARY_pages.txt | head -10"
}
```


### [2026-09-06T15:15:18.538Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:15:21.459Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n \"GAO\\|GUTHA\\|GUH\\|POKORNY\" ARY_pages.txt | head -20\necho \"--- headword گوه ---\"; grep -n \"^گوه\\|گوه \" ARY_pages.txt | head -10"
}
```


### [2026-09-06T15:15:21.537Z] TOOL RESULT

```
--- headword گوه ---
```


## [2026-09-06T15:15:34.489Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"Beef\" \"Butter\" \"Buffalo\" \"Cow\"; do echo \"=== $w ===\"; grep -n -m2 \"^$w, \" SKT.txt; grep -n -m2 \"$w, sb\\|$w (1)\\|^$w\\.\" SKT.txt | head -2; done\necho \"=== SKT generic ===\"; grep -n -m3 \"Beef\\b\" SKT.txt | head -5"
}
```


### [2026-09-06T15:15:36.218Z] TOOL RESULT

```
=== Beef ===
=== Butter ===
2535:Butter.  (L.-Gk.)  M.  K.  boUni  A.&
=== Buffalo ===
2399:Buffalo.  (Span.- U-Gk.)  Span.*«/&/o, buffalo,  orig.  a  kind  of  wild  ox.  —  L.  bujaltu, also  bubaius.  —  Gk.  ^ov^oXot.  a  buffalo, wild  ox,  anteloj^c.    (Not  a  true  (rk.  wonl.)
=== Cow ===
=== SKT generic ===
```


## [2026-09-06T15:15:39.148Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2535,2540p' SKT.txt\necho \"--- cow ---\"; grep -n \"Cow (i)\\|Cow.\\|COW\" SKT.txt | head -8\necho \"--- beef ---\"; grep -n \"Beef\" SKT.txt | head -5"
}
```


### [2026-09-06T15:15:39.239Z] TOOL RESULT

```
Butter.  (L.-Gk.)  M.  K.  boUni  A.&
CACK.
buttr^butera.  ^'L.bHiyrum.  — Gk.ilstfrf^ butter;  lit.  ox>cheese.  — Gk.  ^oim,  aa  v and  rvp^,  cheese.  ^  Really  Scythisa;  A Gk.  sense  is  a  forced  one.
butterfly.  (E.)  A.  &  butior-JU^.'Bk butter-fly.  So  called  from  its  exocsMi resembline  butter,  as  shewn  by  the  0.  Di boter-sthijttt  a  butterfly,  lit.  bnttervoidi (KiUan).    -|-   I^n-  b9Ur^ieg\    a  M(n
Buttery;  see  Bottle  (i).
Butto<^  Button ;  see  BeM^
--- cow ---
2387:Buck  (3).  to  steep  clothes  in  lye.  (C.) M.E.  ^ui^n.'Gaei.  buac^  dang  used  in bleaching,  lye  in  which  clothes  are  washed ; Irish  bua£,  lye.  Orig.  cow-dung ;  from Gael,  and  Irish  bo,  a  cow ;  see  Cow.
4227:COWER.
4243:Cow  VI ),  female  of  the  bull.  (E  )  A  S. ctii  pi.  cy,  whence  M.  E.  ky,  and  the double  pU  ky-fw^kifu.  ^  Du  Hm,  Ictl. kyn  Swed.  Dan.  ko,  G.  kuh,  Irish  and Gael.  &^,  L.  bos  i.Kcn.  t0nu\  Gk.  0oi*, Skt.  ^.    (VCU.)   Sec  Boef.- Buck  (:)).
4246:Cow  (j),  to  dishearten.  (Scand  )  Icel. kug^,  to  tyrannise  over ;  Dan.  km,  Io cfMrrce,  anbdue.
4247:Coward .  tee  OaudaL
4248:Cow«r.  (Scand.)    &L  E.  rmrrw. -Icel
4251:COWL.
4254:Cowry,  a  \m%\\  tibcll  useil  for  money. (Itttid.)      M!nil,     kauH,     a     smalt    shell (C^/'ifiJ  m*->mta)  used  as  coin  In  the  lower prnvirirc%  of  India;  Dcngali  /:(7/i  (Wilson). Cowftlip;  sec  Cow. Coxcomb;  tee  Oook  \i). CoXBwaln;  see  oook  (5),  under  Conoh. Coy:  »ee  Quiet. ^^m  CoBon ;  see  Couain. ^■Crnb<iy  a  shell  fish.  lE.)    AS.  mi^^. ^^^  Ucl  knUflfif  Swed.  JtraUa,  Dan.  h-abU, r        Du,    <('tti,    C.  ^nt^.      Cf.   Gk.  cdpa^of, I        prickly  crab,  beetle.  L.  scanxb^us,  beetle. I      iV^KAK.^
--- beef ---
```


## [2026-09-06T15:15:45.173Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"boeuf\\|bceuf\\|beef\" SKT.txt | head -8"
}
```


### [2026-09-06T15:15:45.221Z] TOOL RESULT

```
3729:CoUop,  a  slice  of  meat  (B.  7)  M.  & tthp/>e.  Cf.  Swed.  kdl9pt,  O.  Swed.  W«yl^_ slices  of  beef  stewed  ;  G.  khpps,  a  di*b  of meat  made  tender  by  beating.  From  iht verb  seen  in  E.  chp  «  clap,  to  make  a  noise; Dn.  klofptn^  G.  khpj'tH,  to  beaL  Allied to  Clap.
9456:Jerked  beef  (Peruvian.)  A  singular corruption  of  eharqui,  the  S.  Aineiican name  for  'jerked'  beef,  or  beef  dried in  a  particular  way.  It  appears  to  be  a Peruvian  word  ;  see  Picj^uU,  Conquest  of Peru.  c.  V.
22855:beef— cow.
```


## [2026-09-06T15:15:49.705Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"boeuf\\|buffalo,\\|butter,  n\\|beef,\" KLN_1966.txt | head -8"
}
```


### [2026-09-06T15:15:49.757Z] TOOL RESULT

```
4648:Derivatives:  beech,  beech-en,  beech-y,  adjs. beef,  n.  —  ME.  boef,  beef,  fr.  OF.  boef,  buef  (F. bceuf),  fr.  L.  bovem,  acc.  of  bos,  ‘ox’.  See  bovine and  cp.  next  word.  Cp.  also  biffin.
5804:buff,  n.,  a  blow;  tr.  and  intr.  v.,  to  strike.  — ME.  buffe,  fr.  OF.  buffe,  ‘blow’,  which  is  of imitative  origin.  Cp.  buffet,  puff, buff,  n.,  skin  of  the  buffalo.  —  From  earlier  buffe, ‘buffalo,  buff’,  fr.  F.  buff le,  ‘buffalo’.  To  account for  the  loss  of  the  ending  -le,  I  would  suggest that  it  was  mistaken  for  the  diminutive  suffix and  accordingly  dropped.
5805:Derivative:  buff,  tr.  v.,  to  polish  with  a  buff;  to make  as  smooth  as  buff  leather, buffalo,  n.  —  Port,  buffalo,  fr.  L.  bufalus,  a  col¬ lateral  form  of  bitbalus,  fr.  Gk.  poupaXo;,  ‘an African  antelope’,  later  ‘buffalo’,  which  is  prob. rel.  to  pou;,  ‘ox’.  See  bovine  and  cp.  prec.  word and  buffle.  Cp.  also  bubaline,  bubalis  and  the first  element  in  Buchloe.
5809:buffle,  n.  ( obsol .),  1)  buffalo;  2)  a  bufflehead  (ob- sol.)  —  F.,  ‘buffalo’,  fr.  Port,  buffalo.  See  buffalo, bufflehead,  n.,  a  small  North  American  duck.  — Compounded  of  buffle  and  bead, buffoon,  n.  —  F.  bouffon,  buffon,  fr.  It.  buffone, fr.  buff  a,  ‘joke,  jest,  pleasantry’,  which  is  rel.  to buffare,  ‘to  blow’;  of  imitative  origin.  Cp.  buff, ‘to  blow’.  For  the  ending  see  suff.  -oon. Derivatives:  buffoon ,  intr.  and  tr.  v.,  buffoon¬ ery,  n.
5969:butte,  n.,  an  isolated  hill  in  the  western  U.S.  — F.,  fr.  hut,  ‘goal,  target’.  See  butt,  ’aim,  goal’, butter,  n.  —  OE.  butere,  huttor-,  fr.  L.  butyrum (whence  also  OFris.,  OHG.  butera,  Du.  boter, MHG.  buter,  G.  Butler,  It.  burro,  OF.  burre, F.  beurre).  fr.  Gk.  [BoufOpov,  ‘butter’,  lit.  ‘cow cheese',  which  is  compounded  of  {Bone,  ‘ox, cow',  and  Tupo;,  ‘cheese’.  See  bovine  and  tyro-. Derivatives:  butter,  tr.  v.,  buttcr-y,  adj. butterfly,  n.  —  ME.  butter /lie,  fr.  OE.  buterfleoge. See  butter  and  fly.  Butterfly  prop,  means  ‘the flying  /wffercolored  thing’, butteris,  n.,  an  instrument  for  paring  the  hoofs of  horses.  —  A  variant  of  buttress,  from  which it  is  differentiated  in  meaning, buttery,  n.,  a  storeroom  for  liquor.  —  Lit.  ‘a  place where  butts  or  barrels  of  liquor  are  stored’,  fr. OF.  hoterie,  ‘place  for  keeping  bottles  or  butts’, fr.  bout.  See  butt,  ‘barrel',  and  -y  (representing OF.  -ie)  and  cp.  bottle,  ‘vessel-,  and  butler, buttock,  n.  —  Formed  fr.  butt,  ‘thick  end’,  with the  dimin.  suff.  -oek.
9480:cow,  n.  —  ME,  ky,  kye,  fr.  OE.  cu,  rel.  to  OS.  ko, OFris.  ku,  MDu.  coe,  Du.  koe,  OHG.  chuo, kuo,  MHG.  kuo,  G.  Kuh,  Dan.  and  Swed.  ko, ON.  kyr,  Norw.  kyr,  ko,  ‘cow’,  and  cogn.  with OIr.  bo,  W.  buw,  ‘cow’,  L.  bos,  Gk.  (3o0q  (for *gwaus-),  ‘ox’,  Lett,  guovs,  ‘cow’,  OSlav.  *gov- gdo,  Czech  hovado,  Slovak  hovddo,  ‘ox’,  OI. gduh,  Avestic  gaush,  ‘ox,  bull,  cow*,  Toch.  A ko,  ki,  B  keu,  ‘cow’,  Arm.  kov,  ‘cow’,  kogi, ‘butter’.  AH  these  words  ult.  derive  fr.  Sumeric gu  (fr.  earlier  gud),  ‘bull,  ox’,  a  word  of  imi¬ tative  origin.  Chinese  ngo,  ngu,  ‘ox’,  is  a  Sumeric loan  word  (possibly  through  the  medium  of  an Indo-European  language).  Cp.  kine.  Cp.  also Bos,  boustrophedon,  bovine,  Bucentaur,  Buce¬ phalus,  Buceros,  bucolic,  buffalo,  bugle,  bugloss, Bupleurum,  Buprestis,  Busycon,  butter,  Gaek- war,  gaur,  Gautama,  gopura,  hecatomb,  nilgai, priest,  sang-de-boeuf.
26059:ocular,  adj.,  pertaining  to  the  eye  or  sight.  —  L. ocularis,  ‘pertaining  to  the  eye’,  fr.  oculus,  ‘eye’, fr.  l.-E.  base  *oqw-,  ‘to  see’,  whence  also  Goth. augd,  OE.  cage,  ‘eye’.  See  eye  and  cp.  optic.  Cp. also  ocellus,  inoculate,  inveigle,  oeil-de-boeuf, oeillade,  and  the  second  element  in  monocle, monocular,  binocular,  antler.
26110:oeil-de-boeuf,  n.,  a  round  or  oval  window  ( archit .) —  F.  ail-de-bceuf  lit.  ‘eye  of  an  ox’,  fr.  aril  (fr. L.  oculus),  ‘eye’,  de,  ‘from,  of’  (fr.  L.  de,  ‘from, away  from’),  and  bauf  (fr.  L.  bovem,  acc.  of bos),  ‘ox’.  See  ocular,  de-  and  beef, oeillade,  n.,  an  amorous  glance.  —  F.  eeillade,  fr.
```


## [2026-09-06T15:16:01.555Z] TOOL CALL #58: Bash

```json
{
 "command": "ls site/pages/217.jpg 2>/dev/null; pdftoppm -f 217 -l 217 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg217 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:16:03.825Z] TOOL RESULT

```
site/pages/217.jpg
total 2152
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:16 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    462 Sep  6 11:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
```


## [2026-09-06T15:16:06.823Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg217.png"
}
```


### [2026-09-06T15:16:07.234Z] TOOL RESULT

```

```


## [2026-09-06T15:16:07.231Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:16:31.807Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 235\\|Page(s): 236\\|Page(s): 237\\|Page(s): 238\\|Page(s): 235-236\\|Page(s): 236-237\\|Page(s): 237-238\" POK_full.txt | head\necho \"---\"; grep -n \"gao-dana\\|gaodana\\|gao-di\\|gaodāyu\\|gao-day\" POK_full.txt | head"
}
```


### [2026-09-06T15:16:31.881Z] TOOL RESULT

```
19777:Page(s): 235 
22276:Page(s): 235 
22510:Page(s): 235-239 
---
```


## [2026-09-06T15:16:35.094Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22380,22420p' POK_full.txt\necho \"...\"; sed -n '22430,22512p' POK_full.txt | grep -n -i \"milch\\|dhē\\|Meaning\\|Root\\|av\\.\" | head -20"
}
```


### [2026-09-06T15:16:35.175Z] TOOL RESULT

```
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
...
```


## [2026-09-06T15:16:43.208Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3995,4010p' BRT.txt"
}
```


### [2026-09-06T15:16:43.267Z] TOOL RESULT

```
99
aiwyaohä-
afradsr^svant-
•  j.  aiwyaaha-  f.  'Lesen,  Studium'  uzw.  1  durch,  dass  ihm  (dem  Schüler)  kein  Be- der  heiligen  Texte:  ka  asti  ihy^a  »la/^!  scheid  wird?"  N.  ij; —  vtspagsu  "partnti saonB  {%A.)f  ..  aya  doEna  disyut  .  .  yB  .vlspaiiü  *'fi*i  ästryeiti  "jedes  Mal,  wenn %ritarymaEm  ratüm  'kam  nHit  aiwyästi  \  Einwendung  erhoben  und  kein  Bescheid Mit  gä'hs  srävaydti  "..  er  könnte  durch  gegeben  wird,  versündigt  er  sich"  N.7_J. seine  schlechte  Religion  (einen)  dazu  ver-  j  P"--  a/rälgda^Hnih.  —  ■>  s.  No.  3, 4.  —  i)  Ausg. leiten,  daas  er  wihrend  der  drei  (dafür!  l%^fZtl,^tl  ^- *)'m^^''Sr5ti~  ^'  "^ bestimmten)  Frühlinge'*  dem  Studium  (der  .""''  '',"^''  __  .  /'  ,™  '  .  ,  , ■    -       _       ,    .  ."    ,^..     •  ].  a-fra'oxiayant-  Adj.  (fem.  yan/i-)
heiligen  Texte)  nicht  obliegt,  (dass  er)  die G.  nicht  aufsagt"  V.iS.g'K Aus  ar.  *ai*jäsä-  (oder  auch  'asä-,   %  36S,  3, igS.']'}),  »om  V. 'a^-,  —  Pü.:  anvyähan  ahoyä- haninii;  s.  No,  2.  —  O  Vgl.  N.  II.  —  ")  Vgl. iSl  —   gegenüber  Pö.  und  Haug  SBayrAW. 1868.  2. 25,  DsT.  ZA.  2. 243 —Cld.  KZ.  jj.  459. j.  aiwyinli  N.  pj;  lies  amiySahayäiili. j.  aäoyslqm  N.  p5:  lies  aiuiyäsl°.
•  j.  awra-  n.  i)  'Regenwolke,  Wolke': yaha  'nm  vätsJsism  Y,(?.32;  —  'ra upapä  Yt  74.41;  —  'm  F.7.  2)  "Regeii, Regenschauer':  ma?ya  .  .  yähva  urväi/is (sd.)  'r&  Yt.Ä40.
KompE.   —    ai.  aikrä-   n.  'Wolke';    np,  abt •Wolke',  afy.  erif  'Wolke',  baJ.  haur  'Regen'.
—  Fii.:  awr,  {lu  F.  /):  m  dtrk, j.  awS'  (KonpA.):  s.  'avaA:
•  j.  aw2-däta-  Adj.  'ins  Wasser  gelegt, im  Wasser  ruhend':  vätasca  ys  darsU 'timca  ifaivnS  YtÄ  34.
•  j.  await-dina- Adj.  'einen  Wasserbehälter, ein  Wasserbecken  bildend':  vairfsla  °nht>hs (als  AP.)  Y.42.a.
*dina-  n.,  zum  V.  'i/J- ;  :ü.  'dhäiia-  n.,  np.  'dän.
—  Vgl.  gaodana-.  —  Pü.:  transski.  (als  EN.).
•  j.  awidänvan-  m.  Name  eines  Ge- wässers: ma  käu  apar^larS  h'ai  srayaKks vouru-kmake  äß  yJ  'nva  (NS.)  nqma  Yt jq.6a.
'  Eig.  'einen  Strom  von  Wasser  enthallend'f?),  | Ableit.  aus  'aatl-dänaz--  m. 11/V"  F.  J  h :  lies  a/r
'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
PPA.  zum  V.  'rari-.
```


## [2026-09-06T15:16:51.973Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%8B%E0%A4%AA",
 "prompt": "Sanskrit गोप (gopa): etymology (from गो + पा), meaning 'cowherd, protector', and relation to the root गुप् (gup)."
}
```


## [2026-09-06T15:16:53.459Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%81%E0%A4%AA%E0%A5%8D",
 "prompt": "Sanskrit root गुप् (gup): etymology - is it a denominative/back-formation from गोपा (gopā) 'cowherd'? meaning 'to protect'."
}
```


### [2026-09-06T15:16:58.142Z] TOOL RESULT

```
# गोप (Gopa) - Sanskrit Dictionary Entry

## Definition
The Sanskrit word **गोप** (gopa) is a masculine noun with two primary meanings:

1. **Cowherd/Herdsman**: "cowherd, herdsman, milkman" - a person who tends cattle
2. **Protector/Guardian**: One who guards or protects

## Etymology
The word combines two Sanskrit elements:
- **गो** (go) = cow; earth
- **-प** (-pa) = protector

This compound structure literally means "protector of cows."

## Linguistic Context
The term traces back through Proto-Indo-European origins and appears in ancient Sanskrit texts including the Rigveda (circa 1500-1000 BCE). The female equivalent is **गोपी** (gopī).

## Related Forms
A synonymous term is **गोपाल** (gopāla), also meaning cowherd. The word has influenced descendant languages including Pali, various Prakrit dialects, and modern Indo-Aryan languages like Odia, Dhivehi, and Sinhalese.
```


### [2026-09-06T15:16:59.498Z] TOOL RESULT

```
# Sanskrit Root गुप् (gup)

Based on the Wiktionary entry, गुप् is indeed derived through back-formation from गोपा (gopā́), meaning "protector of cows; protector, guardian."

**Etymology Summary:**
The entry shows that गुप् represents a "back-formation from गोपा (gopā́, 'protector of cows; protector, guardian'), whence also गोपायति (gopāyáti, 'to guard')."

**Meanings:**
The root carries multiple related senses:
- To guard, defend, protect, or preserve
- To hide or conceal
- In desiderative form: to shun or detest

**Linguistic Origin:**
The etymology traces back through Proto-Indo-European *peh₂- ('protect') via Sanskrit पा (pā), combined with the cow-related stem from गो (go, "cattle"). This demonstrates how the protective action becomes abstracted from its original context of cattle-guarding into a general verb meaning protection.
```


## [2026-09-06T15:17:06.108Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%87",
 "prompt": "Persian گوه: etymology (Middle Persian, Avestan gūθa-, Sanskrit gūtha-, PIE), meaning 'dung'."
}
```


## [2026-09-06T15:17:06.710Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF",
 "prompt": "Persian کود: etymology and meaning (manure, fertilizer). Any Middle Persian or Proto-Iranian form?"
}
```


### [2026-09-06T15:17:08.261Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:17:14.276Z] TOOL RESULT

```
# Persian کود: Etymology and Meaning

## Meanings
The word کود has two main etymologies in Persian:

**Etymology 1** (native origin): As a noun, it means "fertiliser" or "manure," and can also refer to "a stack or heap of corn."

## Etymology and Historical Forms

The entry states: "From Middle Persian [script needed] (kōδ)." Unfortunately, the **Middle Persian script form is not provided** in this Wiktionary entry—it only shows the transliteration "kōδ" without the actual script.

## Proto-Iranian Connection
The entry doesn't explicitly mention a Proto-Iranian form. However, it does establish the word's ancient roots through related languages: "Related to Sanskrit कूट (kūṭa, 'heap, multitude'), Romani kidao ('to heap'), Old Armenian կոյտ (koyt, 'heap, mass, pile')."

This linguistic network suggests an Indo-European origin related to concepts of heaping or gathering, though no specific Proto-Iranian reconstruction is cited in this source.
```


## [2026-09-06T15:17:29.184Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%E1%B9%93ws\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B4%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AA%D9%88%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%8B%E0%A4%AA\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%97%E0%A5%81%E0%A4%AA%E0%A5%8D\" \\\n \"https://www.etymonline.com/word/butter\" \\\n \"https://www.etymonline.com/word/buffalo\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 217, root Gwou: cow/dung branch verification\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:17:35.134Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1f0b99beb34b62b0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24897164dd4d6660.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae6e221828f6effe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e319a036534237ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0826040c20c04f56.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a4e351f0cf974ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a80851e89afc7e62.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c23adaa1be9409f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30654e30078411d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6d1babf97f0714da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/df5624c3e90e4059.txt
```


## [2026-09-06T15:18:08.147Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14690,14710p' SNS.txt\necho \"=== BRT columns for gutha/gaospenta ===\"\nawk 'BEGIN{RS=\"\\f\"} /j.  gül\\^a-/ {print \"leaf(0-based)=\"NR-1; print substr($0,1,300)}' BRT.txt"
}
```


### [2026-09-06T15:18:09.945Z] TOOL RESULT

```
•*\/\rJ {AiWb. 1832)vahu. xsa^ra-:^ 

(£W •&*»«&) *K^*>*j:vuhuxsatr-gah: -o-M_>\enj.»-ot« 

o-'a**'^**^*.^.^!^,.^,,^ :ni huft: ^v? 

C * p *' : ****<* /gop: ^rfa^^ni + /iop: jll j4 ^ 
(ferfcum, 200, 7, 4) nhwpt , nhwmb- : jiU (p. 236. 
tnihuft Sstgd: *>i*ta VOCi.fVtfH nahunbat: {, 

■ Y/M . J>1 « j*s w , ^ Aii 



•VtJ (^•A^],^^,«i |i! nihuftag ! S^*- 



.«-«*w:nax v ist: l* AJ *> 
nxwst :^. {Mir. Man. II, 61)nxwstyn, nxwst:^ 

=== BRT columns for gutha/gaospenta ===
leaf(0-based)=312
ata-  Adj.  'die  Galle  heraus- schneidend"':    kat    tä    tiara  yaozdayqn aiih>n  .  .  ya  rrasiuin  franuharat  sänS  i  "   ' para.iristahe  masyelu  väl  .  .  ayaozäayqn  ■ atihm  . .  lalJ'a  narS  'l^sca  (NPm.)  z^maö.- k?ntas^a  taica  tiarS  spiti.dsi'^ra  casmanal  * haca  it
```


## [2026-09-06T15:18:19.523Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=10392{n+=gsub(/\\f/,\"\")} END{print \"gutha leaf=\"n}' BRT.txt\nawk 'NR<=9788{n+=gsub(/\\f/,\"\")} END{print \"gaodana leaf=\"n}' BRT.txt\nawk 'BEGIN{RS=\"\\f\"} NR==538' BRT.txt | head -3\nawk 'BEGIN{RS=\"\\f\"} NR==511' BRT.txt | head -3"
}
```


### [2026-09-06T15:18:21.915Z] TOOL RESULT

```
gutha leaf=312
gaodana leaf=290
ä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68;  —  tal  i^aranS  b°  asti N.  30  ".  Ohne  Wert :  Vyt  5^,  Yt  2. 1 1 , Vd.  20.
Vgl.  iä  und  biihittm.  —  Et.  ?  Ob  in  ai. bä^hamt  S.  diw  WN,  AiOr.  /.  172  f.  —  Pü. (meist):  bSiIän,  (m  V.  iS):  purci{7)i),  (m  V. 3):  bälislänfi i  Sü.:  nilyam.  —  ')  Von  dem  es aber  durch  Enklitika  getrennt  sein  kann.  Ab- weichend ist  die  Stellung  Vt.  10.  S3  IT.  -  vgl. Yt  10.  53,  73  -.  N.  30.  —  =)  In  ungewöhn- licher Stellung,  s.  No.  1,  —  3)  S.  lu  bi.  — i}  S.  in  iäiiiibm.
•  j.  baiSiStsm  Adj.  'am  sichersten' '':  yatöU dim  b'  ava^anqn  (sd.)  sünöva..  V.o. 45.
aam  **o^  (statt  GP.)'*  vTrS.- vq%wanqm  Vr.  /.  5 ;  —  aat  ahmt  timäne zayänte  . .  tnürakäla  "oj  varih3ca'W.ii.6; —  gSuica  atvS.dätaya  (sd.)  gfusca  'oayä Yt.  7.  o;  —  gaom  alvöjiätahe  (sd.) . .  °%ake urvnO  fravasim  S,  2. 12.
Pü.:  piir  sarlak,  SQ.  (zu  Y.  lO):  sampürnajälß. —  >)  VgL  iharita-  No.  i.  NA.  Schreibt  /• und  v*  fälschlich  lusammen.
•  j.  pouru.spaxStay-  f.  'weithin  reichen- des Erspähen':  daya  .  .  °tim  tbi^antqm paiti./aitTm  dusmainyunqm  ha'i:rä.itiväitlm harmriianqm  "gib  . .,  dass  wir  die  Feinde auf  weit  hinaus  erspähen,  die  Gegner  ab- wehren, die  Widersacher  auf  einen  Schlag besiegen"  Y.57.  26;  —  Hi  rfflr^..  Ytp.  i.
```


## [2026-09-06T15:18:59.408Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg217.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/217.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-06T15:18:59.491Z] TOOL RESULT

```
total 8644
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:18 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-06T15:19:01.910Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:19:01.953Z] TOOL RESULT

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


## [2026-09-06T15:27:09.901Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk217.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPIE = W + \"Reconstruction:Proto-Indo-European/g%CA%B7%E1%B9%93ws\"\nGAV = W + \"%DA%AF%D8%A7%D9%88\"\nGOSHT = W + \"%DA%AF%D9%88%D8%B4%D8%AA\"\nGOSFAND = W + \"%DA%AF%D9%88%D8%B3%D9%81%D9%86%D8%AF\"\nNEHOFTAN = W + \"%D9%86%D9%87%D9%81%D8%AA%D9%86\"\nTUDEH = W + \"%D8%AA%D9%88%D8%AF%D9%87\"\nKUD = W + \"%DA%A9%D9%88%D8%AF\"\nGOPA = W + \"%E0%A4%97%E0%A5%8B%E0%A4%AA\"\nGUP = W + \"%E0%A4%97%E0%A5%81%E0%A4%AA%E0%A5%8D\"\nBUTTER = \"https://www.etymonline.com/word/butter\"\nBUFFALO = \"https://www.etymonline.com/word/buffalo\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(\n id=1, lang=\"Avestan\", words=\"gâuš, gave, ga 3, gâvô, gavâm, gao\",\n verdict=\"confirmed\",\n derivation=(\n  \"The forms are the paradigm of Avestan gav- 'cow, ox, bovine, domestic animal', the regular \"\n  \"Iranian continuation of PIE *gʷṓws: nom. sg. gāuš (< *gʷōws), dat. sg. gave (< *gʷewey), \"\n  \"acc. pl. gā (Nourai's 'ga 3' is his own homonym number for Av. gā, the accusative plural, \"\n  \"= Skt. gāḥ, Doric βῶς), nom. pl. gāvō, gen. pl. gavąm, and the compositional stem gao- \"\n  \"(gao-spənta-, gao-dāna-). Pokorny sets out exactly this paradigm ('Nom. Sg. gʷōus, Gen. gʷewos, \"\n  \"Akk. gʷōm, Lok. gʷowi'), equating Av. gāuš / gave / gavąm / gā with Old Indic gauḥ / gave / \"\n  \"gavām / gāḥ. The Iranian development is purely phonetic: PIE *gʷ > Indo-Iranian g before back \"\n  \"vowels, *ōw preserved as āu in the nominative, and the diphthong reduced to a- before a vowel \"\n  \"in the weak cases.\"),\n derivation_fa=(\n  \"صورت‌های آورده‌شده همان صرف واژهٔ اوستایی gav- «گاو، جانور اهلی» است: نهادی مفرد gāuš، برایی gave، \"\n  \"رایی جمع gā (شمارهٔ ۳ که نورایی افزوده نشانهٔ هم‌آوای سوم در فهرست خود اوست)، نهادی جمع gāvō، \"\n  \"اضافی جمع gavąm و ستاک ترکیبی gao-. این صورت‌ها بازماندهٔ مستقیم هندواروپایی آغازین *gʷṓws است؛ \"\n  \"*gʷ در هندوایرانی پیش از واکهٔ پسین به g بدل شده و دوواکهٔ *ōw در حالت نهادی به āu رسیده است. \"\n  \"پوکورنی (ص ۴۸۲–۴۸۳) و کلاین (ص ۳۶۴) همین برابری اوستایی و سنسکریت را می‌آورند. ادعای نورایی درست است.\"),\n sources=[PIE, GAV],\n ref_check=[{\"ref\": \"KLN:364\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 vol. I p.364 s.v. 'cow' (KLN_1966.txt line 9480, leaf 202, the printed '364' stands at the head of the column): '...OI. gáuh, Avestic gaush, ‘ox, bull, cow’, Toch. A ko, ki, B keu, ... Arm. kov'. Klein's added claim that all these ultimately derive from Sumerian gu is obsolete.\"}],\n consulted=[\n  {\"src\": \"POK\", \"where\": \"gʷou- 'cattle', pp. 482-483\", \"stance\": \"supports\",\n   \"note\": \"POK_full.txt: 'Root/lemma: gʷou-, Meaning: cattle, Grammatical information: m. f. Nom. Sg. gʷous, Gen. gʷewos, Akk. gʷōm, Lok. gʷowi ... Old Indie gauh m. f. ‘cattle’ (= Avestan gaus ds.), Gen. goh (= Avestan gaus), Dat. gave (= Avestan gave) ... Akk. gah (= Avestan ga)'.\"},\n  {\"src\": \"BRT\", \"where\": \"s.v. gav-, gāuš / gaodana- (BRT.txt line 9788)\", \"stance\": \"supports\",\n   \"note\": \"Bartholomae has the paradigm of gav- and the compositional stem gao- ('j. gao-dana-, °ðana- n. 1) ‘Milchgefäss’').\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷou-\", \"stance\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 555: 'gʷou-. Ox, bull, cow. Nominative singular form *gʷéu-s ... 4. Sanskrit go-, gauh, cow. [Pok. gʷou- 482.]'\"}])\n\nN(\n id=2, lang=\"Persian\", words=\"gâv «گاو»; gŭ-pân «گوپان»; gŭ-sâleh «گوساله»; gŭšt «گوشت»\",\n verdict=\"confirmed\",\n derivation=(\n  \"NP gāv 'cow' continues MP gāw (Book Pahlavi ideogram TWRA) < OIr. *gāuš, the same word as Av. gāuš; \"\n  \"Horn no. 888 lists 'gāv ‘Rind’, gō, gōg ‘Kalb’ (*gavaka-), gōbān ‘Hirte’' with 'aw. gāv- ‘Rind’; phlv. gō bzw. gav'. \"\n  \"gū-pān/gō(b)ān 'cowherd' is gav- + the agent suffix -pāna- 'protecting' (the same *pā- 'protect' as in Skt. gopā-), \"\n  \"cf. Sarikoli γubūn, Pashto γōba 'Hirte' cited by Horn; the -p-/-b- variation is the normal NP treatment of \"\n  \"intervocalic Iranian *p. gū-sāleh 'calf' is gō- 'cow' + -sāla 'yearling' (from *vatsa-ka- via the '-sāla' element, \"\n  \"Horn no. 941: 'Das ō in gōsāle stammt von gō ‘Kuh’ (No. 888)'); Mo'in analyses it as گو (=گاو) + ساله, Kurdish gāsāle. \"\n  \"gūšt 'meat' < MP gōšt [BSLYA] < Proto-Iranian *gawštaH, a -šta- derivative of *gaw- 'cow'; Horn no. 944 puts it \"\n  \"under 'aw. gāv, Nom. gāuš ‘Fleisch’', and Buck lists 'Av. gav- (NPers. gušt)' in his FLESH section.\"),\n derivation_fa=(\n  \"«گاو» از فارسی میانهٔ gāw و آن از ایرانی باستان *gāuš، هم‌ریشه با اوستایی gāuš و سنسکریت gauḥ. \"\n  \"«گوپان/گوبان» مرکب است از گو (=گاو) + پان/بان (از ریشهٔ *pā- «نگاهبانی کردن»؛ قس سنسکریت gopā-)؛ \"\n  \"پِ ایرانی در میان دو واکه در فارسی نو گاه به ب نرم شده، از این رو دو صورت گوپان و گوبان. \"\n  \"«گوساله» از گو (=گاو) + ساله؛ هرن (شمارهٔ ۹۴۱) می‌گوید که «او»ی گوساله از گو «گاو» آمده و بخش دوم با سنسکریت vatsá- «گوساله» مربوط است. \"\n  \"«گوشت» از فارسی میانهٔ gōšt و آن از ایرانی آغازین *gawštaH، مشتقی با پسوند -šta- از *gaw- «گاو»؛ هرن (شمارهٔ ۹۴۴) و باک (ص ۲۰۲) نیز گوشت را زیر gav- اوستایی آورده‌اند. \"\n  \"ادعای نورایی در هر چهار واژه درست است.\"),\n sources=[GAV, GOSHT],\n ref_check=[\n  {\"ref\": \"SYN:202\", \"status\": \"supports\",\n   \"note\": \"Buck 1949, §4.13 FLESH, printed p.202 (SYN.txt \\\\f-block 238): the comparative table lists 'Av. gav- (NPers. gušt)' beside Skt. māṃsa-, Grk. sarx, Lat. carō.\"},\n  {\"ref\": \"BQT:1856\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol. 3, scan pdf p.653 (= printed 1856), Mo'in's footnote 4 on گوشت: 'پارسی باستان gaushta? «هوبشمان ۹۴۶»، پهلوی gōsht، افغانی ..., کردی gōsht, بلوچی gōsht, وخی gusht ...'; گوساله with Mo'in's note 'از: گو (=گاو) + ساله' stands one page earlier (pdf 651 = p.1854).\"},\n  {\"ref\": \"HRN:210\", \"status\": \"supports\",\n   \"note\": \"Horn 1893 printed p.210 (HRN.txt leaf 231): no. 941 'gōsāle ‘Kalb’ ... Das ō in gōsāle stammt von gō ‘Kuh’ (No. 888)' and no. 944 'gōšt ‘Fleisch’. aw. gāv, Nom. gāuš ‘Fleisch’; phlv. gōšt'. gāv itself and gōbān 'Hirte' are Horn no. 888 on p.198.\"},\n  {\"ref\": \"MON:3430\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in's Farhang-e Farsi vol. 3 p.3430 (گوشت/گوساله area) is not paginated in the online vajehyab text and the local MON_part*.txt OCR carries no page markers.\"}],\n consulted=[\n  {\"src\": \"PHD\", \"where\": \"p. 76 s.v. gōšt, gōspand, gōstān\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie 1971: 'gōšt [BSLYA < A bsr’; gwšt | N ~] meat, flesh'; also 'gōstān [gwst’n] cattle-stall, cowshed', showing the gō- 'cow' compositional stem is alive in MP.\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷou-sthos\", \"stance\": \"partial\",\n   \"note\": \"Mann, IEC.txt: 'gʷou-sthos, ā, io (gʷouəst-, gust-) Skt. gosthah, -sthā ‘cowshed’; Per. gūst ‘meat’' — Mann too derives NP gūšt from a *gʷou- compound, though he analyses the second element as *sthā- rather than a -šta- suffix.\"},\n  {\"src\": \"SYN\", \"where\": \"§4.13 FLESH, p.202\", \"stance\": \"supports\",\n   \"note\": \"'Av. gav- (NPers. gušt)' in the word-table for 'flesh'.\"}])\n\nN(\n id=3, lang=\"Avestan\", words=\"gao-spenta; gao-di, gao-dana\",\n verdict=\"confirmed\",\n derivation=(\n  \"Both are Avestan compounds whose first member is the composition stem gao- of gav- 'cow, bovine'. \"\n  \"gao-spənta- 'the beneficent/holy cattle', i.e. small cattle, sheep (Vd. 21.1, P.34: 'para tē gaospəṇta ...'), \"\n  \"= gao- + spənta- 'holy, beneficent' (Nourai's cross-reference ☞Kwen is to PIE *ḱwen- 'holy'). \"\n  \"gao-δi- and gao-dāna- both mean 'milk vessel': the second member is the root noun of *dʰeh₁- 'to put, set' \"\n  \"(Pokorny's dhē- pp. 235-239 expressly cites 'Avestan gao-δi- ‘milk container’' among the root-noun compounds, \"\n  \"beside Skt. ni-dhi- 'container'), and gao-dāna- is the same root with the -ana- suffix \"\n  \"(Bartholomae: 'j. gao-dana-, °ðana- n. 1) ‘Milchgefäss’ ... 2) überh. ‘Gefäss, Napf, Schüssel’', Vd. 21.7). \"\n  \"So 'gao-di' is not a misprint but Nourai's rendering of Av. gaoδi-.\"),\n derivation_fa=(\n  \"هر دو واژه ترکیب‌های اوستایی‌اند که جزء نخستشان ستاک ترکیبی gao- از gav- «گاو» است. \"\n  \"gao-spənta- «چارپای مقدس/سودمند» (وندیداد ۲۱٫۱) از gao- + spənta- «مقدس» ساخته شده است. \"\n  \"gao-δi- و gao-dāna- هر دو «ظرف شیر» معنی می‌دهند؛ جزء دوم از ریشهٔ *dʰeh₁- «نهادن» است ــ \"\n  \"پوکورنی در مدخل dhē- (ص ۲۳۵–۲۳۹) صریحاً «اوستایی gao-δi- ‘ظرف شیر’» را در کنار سنسکریت ni-dhi- می‌آورد ــ \"\n  \"و بارتولمه نیز gao-dana-, °ðana- «ظرف شیر» را ثبت کرده است. پس «gao-di» غلط چاپی نیست بلکه همان gaoδi- اوستایی است. \"\n  \"ادعای نورایی درست است.\"),\n sources=[GOSFAND],\n ref_check=[\n  {\"ref\": \"BQT:1855\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol. 3, scan pdf p.652 (= printed 1855), Mo'in's starred footnote on گوسپند، گوسفند: 'اوستا - gaospenta، پهلوی gōspand «اسحق ۹۴۷»، مرکب از: گو (گاو ...) + سپند (اوستا spenta بمعنی مقدس)'.\"},\n  {\"ref\": \"POK:237\", \"status\": \"supports\",\n   \"note\": \"Pokorny's dhē- 'setzen, stellen, legen' (pp. 235-239) lists among the root-noun compounds: 'Avestan gao-δi- ‘milk container’' (POK_full.txt, block ending 'Page(s): 235-239'), exactly Nourai's 'gao-di'.\"}],\n consulted=[\n  {\"src\": \"BRT\", \"where\": \"s.v. gao-dana- (BRT.txt line 9788)\", \"stance\": \"supports\",\n   \"note\": \"'j. gao-dana, °ðana- n. 1) ‘Milchgefäss’ ... V.21.7; 2) überh. ‘Gefäss, Napf, Schüssel’'; gaospəṇta- is attested in the passages quoted s.v. upa and s.v. spənta- ('para te gaospəṇta ... P.34', 'nəmasə gaospəṇta ... V.21.1').\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 154 s.v. gōspand\", \"stance\": \"supports\",\n   \"note\": \"Nyberg: 'gōspand [gwspnd; KYN’] cattle in general, but esp. small cattle, sheep and goats ... — Av. (506) gaospenta-; Paz. gospand, NP gospand, gosfand.'\"}])\n\nN(\n id=4, lang=\"Persian\", words=\"gŭspand, gôsfand «گوسپند،گوسفند»\",\n verdict=\"confirmed\",\n derivation=(\n  \"Av. gao-spənta- > MP gōspand [gwspnd, ideogram KYN'] 'small cattle, sheep and goats' > NP gōspand, with the \"\n  \"later variant gōsfand in which the cluster -sp- was dissimilated/spirantised to -sf- (the same NP change as in \"\n  \"اسفند beside اسپند). Semantically the Avestan 'beneficent animal', a term for the whole class of useful herd \"\n  \"animals, narrowed in New Persian to 'sheep' specifically, میش being the older word for the animal (so Mo'in). \"\n  \"Horn no. 942 gives the chain flatly: 'gōspend, gōsfend ‘Kleinvieh, Schaf, Widder, Ziege’. aw. gaospenta- (vd. 21,1); phlv. gōspand'.\"),\n derivation_fa=(\n  \"«گوسپند/گوسفند» از فارسی میانهٔ gōspand و آن از اوستایی gao-spənta- «جانور سودمند و مقدس». \"\n  \"خوشهٔ -سپ- در فارسی نو به -سف- بدل شده (همانند اسپند > اسفند). از نظر معنایی، واژهٔ اوستایی نام عام چارپایان اهلی سودمند بوده \"\n  \"و در فارسی نو به «میش» محدود شده است؛ معین در حاشیهٔ برهان قاطع (ص ۱۸۵۵) همین را می‌گوید. \"\n  \"هرن (شمارهٔ ۹۴۲)، مکنزی و نیبرگ نیز همین زنجیره را می‌آورند. ادعای نورایی درست است.\"),\n sources=[GOSFAND],\n ref_check=[\n  {\"ref\": \"HRN:210\", \"status\": \"supports\",\n   \"note\": \"Horn 1893 p.210 (HRN.txt leaf 231) no. 942: 'gōspend, gōsfend ‘Kleinvieh, Schaaf, Widder, Ziege’. aw. gaospenta- (vd. 21, 1); phlv. gōspand.'\"}],\n consulted=[\n  {\"src\": \"PHD\", \"where\": \"p. 76 s.v. gōspand\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie: 'gōspand [KYN’ < A ‘n’ ?; gwspnd | N ~] (small) cattle, sheep.'\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. gōspand\", \"stance\": \"supports\",\n   \"note\": \"'— Av. (506) gaospenta-; Paz. gospand, NP gospand, gosfand.'\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 3, printed p.1855\", \"stance\": \"supports\",\n   \"note\": \"Mo'in's footnote: 'گوسپند، گوسفند ... اوستا - gaospenta، پهلوی gōspand ... اسم اصلی جانوری که امروزه گوسفند نامیده میشود، میش است.'\"}])\n\nN(\n id=5, lang=\"Sanskrit\", words=\"gâuh; gô-pâ-h, gôpâ\",\n verdict=\"confirmed\",\n derivation=(\n  \"Skt. gáuḥ 'cow, cattle' is the exact Indic counterpart of Av. gāuš, both < PIE *gʷṓws (Pokorny p.482). \"\n  \"gopā́- / gopā́ḥ 'cowherd, protector' is the transparent compound go- 'cow' + -pā́- 'protecting' \"\n  \"(root pā- < PIE *peh₂- 'to protect'; Nourai's ☞Pa refers to that root), attested from the Rigveda; \"\n  \"Pokorny lists it in the same entry ('therefrom go-pā-h ‘herdsman, shepherd’, gopāyati ...'). \"\n  \"From the compound the language back-formed a simplex verbal root gup- 'to guard, protect' and the \"\n  \"denominative gopāyati, so the 'protect' sense is genuinely a secondary offshoot of the word for 'cow'.\"),\n derivation_fa=(\n  \"سنسکریت gáuḥ «گاو» برابر دقیق gāuš اوستایی و بازماندهٔ *gʷṓws هندواروپایی است. \"\n  \"gopā́- «گاوبان، نگاهبان» ترکیبی است شفاف از go- «گاو» + -pā́- «نگاهبان» (از ریشهٔ *peh₂- «پاییدن، نگاه داشتن»)، \"\n  \"که از ریگ‌ودا به بعد گواهی شده است. از همین ترکیب، ریشهٔ سادهٔ gup- «نگاه داشتن» به شیوهٔ ساخت واپس‌گرد (back-formation) پدید آمده است. \"\n  \"پوکورنی (ص ۴۸۲) هر دو را در یک مدخل می‌آورد. ادعای نورایی درست است.\"),\n sources=[GOPA, GUP, PIE],\n ref_check=[\n  {\"ref\": \"POK:482\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt s.v. gʷou-, pp. 482-483: 'Old Indie gauh m. f. ‘cattle’ ... therefrom go-pa-h ‘herdsman, shepherd’, gopayati, gopayati ‘hütet’, etc.'\"}],\n consulted=[\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷou-, §4\", \"stance\": \"supports\",\n   \"note\": \"'4. Sanskrit go-, gauh, cow: GAYAL.'\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷōus / gʷou-\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'gʷou-, element of many cpds. in sense of ‘cow, cattle, beast; dung; lump’ etc.'; the cpd. entries include Skt. gosthaḥ 'cowshed', gotrám 'cowshed'.\"},\n  {\"src\": \"WLD\", \"where\": \"WP. I 696 f. (cited by Pokorny at the end of gʷou-)\", \"stance\": \"supports\",\n   \"note\": \"Pokorny's reference line for the entry is 'WP. I 696 f., WH. I 112, 118' — Walde-Pokorny treat the same material s.v. gʷou-.\"}])\n\nN(\n id=6, lang=\"Avestan / Sanskrit\", words=\"gôp, gôh\",\n verdict=\"disputed\",\n derivation=(\n  \"Half of this node is right and half is not. Sanskrit gup- (Horn's '√gōp-') really is a back-formation from \"\n  \"gopā́- 'protector of cows' — Wiktionary, following the standard handbooks, states 'back-formation from गोपा (gopā́), \"\n  \"whence also गोपायति (gopāyáti, to guard)' — so the arrow gopā́- → gup- 'to protect, preserve' is sound, and gup- \"\n  \"does also develop a sense 'to hide, conceal'. But (a) no Avestan root gaup-/gōp- 'to protect' is attested: \"\n  \"Bartholomae has no such entry, only gaoz-, guz- 'verbergen' (Praes. guza-, gūzaya-), so the language label \"\n  \"'Avestan' is unsupported; and (b) the second form 'gōh' is Skt. guh-/gūhati 'to hide', which belongs to \"\n  \"PIE *gʰewgʰ- (Av. gaoz-, guz-), a different root that has nothing to do with 'cow'. Horn himself flags this: \"\n  \"'Bartholomae meint ..., ai. √gōp- sei vielleicht eine Nebenform von √gōh-, und die dazu gestellten Formen \"\n  \"stammten also nur zum Teil von gopā- ‘Hirt’' — which is the discussion Nourai's NOTE points to. Modern \"\n  \"scholarship keeps gup- and guh- apart.\"),\n derivation_fa=(\n  \"این گره نیمه‌درست است. ریشهٔ سنسکریت gup- «نگاه داشتن، پاسداری کردن» به‌راستی ساخت واپس‌گردی از gopā́- «گاوبان، نگاهبان» است \"\n  \"و ویکی‌واژه نیز همین را می‌گوید؛ بنابراین پیکان gopā́- ← gup- درست است. اما دو اشکال هست: \"\n  \"نخست آنکه در اوستایی هیچ ریشهٔ gaup-/gōp- به معنی «نگاه داشتن» گواهی نشده و بارتولمه تنها gaoz-، guz- «پنهان کردن» را دارد، \"\n  \"پس برچسب «اوستایی» نادرست است؛ دوم آنکه صورت gōh همان سنسکریت guh-/gūhati «پنهان کردن» است که از ریشهٔ هندواروپایی *gʰewgʰ- می‌آید \"\n  \"(هم‌ریشه با gaoz- اوستایی) و ربطی به «گاو» ندارد. خود هرن (ص ۲۳۷) از قول بارتولمه همین تردید را بازگو می‌کند. \"\n  \"پژوهش امروزی این دو ریشه را از هم جدا می‌داند.\"),\n sources=[GUP, GOPA],\n ref_check=[\n  {\"ref\": \"HRN:237\", \"status\": \"partial\",\n   \"note\": \"Horn 1893 p.237 (HRN.txt leaf 258), under no. 1059: '*ni + √gōp- ‘behüten, verwahren’, vergl. ai. √gōp-'. But the same paragraph carries the caveat Nourai's NOTE alludes to: 'Bartholomae meint nach briefl. Mitteilung, dass nihuften sein h von np. nihān (No. 1058) bezogen habe; ai. √gōp- sei vielleicht eine Nebenform von √gōh-, und die dazu gestellten Formen stammten also nur zum Teil von gopā- ‘Hirt’.' So Horn supports the Sanskrit half but is himself uncertain, and he posits √gōp- for Iranian, he does not cite an attested Avestan verb.\"}],\n consulted=[\n  {\"src\": \"BRT\", \"where\": \"s.v. gaoz- (BRT.txt line 9871)\", \"stance\": \"contradicts\",\n   \"note\": \"'j. gaoz-, p. gaud- V. ‘verbergen’. Praes. guza-, gūzaya-, (Iter.) gaozayō' — Bartholomae's Avestan verb for 'hide' is gaoz-/guz-, and no gaup-/gōp- 'protect' is listed anywhere in the Altiranisches Wörterbuch.\"},\n  {\"src\": \"POK\", \"where\": \"gʷou- p.482\", \"stance\": \"partial\",\n   \"note\": \"Pokorny attaches only 'go-pā-h ‘herdsman’, gopāyati' to gʷou-; he does not derive Skt. guh- 'to hide' from it (that belongs to his gʰeugʰ- 'verbergen', p.450).\"},\n  {\"src\": \"CHEUNG\", \"where\": \"no entry *gaup 'to protect'\", \"stance\": \"silent\",\n   \"note\": \"Cheung 2007 has *gaub 'to say' and *gauz 'to hide' but no Iranian verbal root *gaup 'to protect' — grep of CHEUNG.txt for 'gaup' returns nothing.\"}])\n\nN(\n id=7, lang=\"Avestan\", words=\"ni-gôp\",\n verdict=\"disputed\",\n derivation=(\n  \"There is no attested Avestan verb ni-gaup-/ni-gōp- 'to hide, protect'. The form is Horn's 1893 reconstruction \"\n  \"(*ni + √gōp-) put forward to explain MP nihuftan, and Horn himself immediately reports Bartholomae's objection to it. \"\n  \"Bartholomae's Altiranisches Wörterbuch has no such entry; the Avestan verb for 'to hide' is gaoz-/guz- (Praes. guza-), \"\n  \"which would give MP *nigōz-/*niguxt, not nihumb-/nihuft. Modern Iranian etymology (Henning 1933, followed by \"\n  \"Abolqasemi and Cheung) explains MP nihumb-/nihuft from *ni-su(m)b- instead. The node is therefore an artefact of \"\n  \"the 19th-century literature rather than an Avestan datum.\"),\n derivation_fa=(\n  \"در اوستا هیچ فعلی به صورت ni-gaup-/ni-gōp- «پنهان کردن، نگاه داشتن» گواهی نشده است. این صورت بازسازی هرن (۱۸۹۳) است \"\n  \"برای توضیح فارسی میانهٔ nihuftan، و خود هرن بی‌درنگ ایراد بارتولمه را نقل می‌کند. در فرهنگ ایرانی باستان بارتولمه چنین مدخلی نیست؛ \"\n  \"فعل اوستایی «پنهان کردن» gaoz-/guz- است که در فارسی میانه *nigōz-/*niguxt می‌داد نه nihumb-/nihuft. \"\n  \"ریشه‌شناسی امروزی (هنینگ ۱۹۳۳، ابوالقاسمی، چونگ ۲۰۰۷) nihuft را از *ni-su(m)b- می‌گیرد. \"\n  \"پس این گره ساختهٔ ادبیات سدهٔ نوزدهم است و پژوهش امروزی آن را رد می‌کند.\"),\n sources=[NEHOFTAN],\n ref_check=[\n  {\"ref\": \"HRN:237\", \"status\": \"partial\",\n   \"note\": \"Horn p.237 does print '*ni + √gōp- ‘behüten, verwahren’ ... phlv. n(i)huftan ‘verbergen’', i.e. it supports Nourai's arrow — but as a starred reconstruction, and Horn adds Bartholomae's objection and Johansson IF II 50-51 in the same breath: 'Jedenfalls wird es schwer, nihuften gänzlich von √gōh- zu trennen.'\"}],\n consulted=[\n  {\"src\": \"BRT\", \"where\": \"no entry ni-gaup-/gaup-; s.v. gaoz- (line 9871)\", \"stance\": \"contradicts\",\n   \"note\": \"The Altiranisches Wörterbuch records no Avestan gaup-/gōp-; grep of BRT.txt finds only 'j. gaoz-, p. gaud- V. ‘verbergen’'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"*su(m)p/b, p. 368-369\", \"stance\": \"contradicts\",\n   \"note\": \"Cheung 2007: '*su(m)p/b ‘to make up, “beautify”’ ... MIDDLE PERSIAN: (+ *ni-) MMP nhwmb-, BMP nhwmb- /nihumb-/ ‘to hide, conceal, cover up, guard’. Cf. Henning 1933: 200: “Viell. sub, ap. *θub = ai. śumbhati?” ... NWIR: (+ *ni-) NP nihuftan.'\"},\n  {\"src\": \"PHD\", \"where\": \"p. 59 s.v. nihuftan\", \"stance\": \"silent\",\n   \"note\": \"MacKenzie gives only the MP forms ('nihuftan, nihumb- [nhwptn’, nhwmb-] cover, hide, conceal, clothe') without an Avestan etymon.\"}])\n\nN(\n id=8, lang=\"Pahlavi\", words=\"nihuftan\",\n verdict=\"disputed\",\n derivation=(\n  \"The Middle Persian verb is real and well attested: MacKenzie 'nihuftan, nihumb- [nhwptn', nhwmb-] cover, hide, \"\n  \"conceal, clothe', also nihumbīdan; Nyberg cites it from the Zoroastrian texts ('apaš abar warr nihuft ‘he covered \"\n  \"himself with his garment’'). What is disputed is the arrow drawn to it. The present stem nihumb- (Manichaean MP \"\n  \"nhwmb-, nhwm-) is the decisive evidence: a nasal-infixed *ni-su-m-b- with past participle *ni-suf-ta gives exactly \"\n  \"nihumb-/nihuft, whereas Horn's *ni-gōp- accounts for neither the nasal nor the h-. Henning (1933:200) proposed \"\n  \"'*sub, OP *θub = Skt. śumbhati', and this is now the standard view: Abolqasemi (FFD p.80, the very reference \"\n  \"Nourai's own note quotes) writes 'نهفت < فارسی میانه nihuft < فارسی باستان *ni-θuf-ta < ایرانی باستان *ni-suf-ta ... \"\n  \"ریشهٔ suf به معنی آراستن است', and Cheung 2007 files NP nihuftan under *su(m)p/b. So the book's own dissenting \"\n  \"footnote is the one modern scholarship follows.\"),\n derivation_fa=(\n  \"فعل فارسی میانه به‌خوبی گواهی شده است: مکنزی «nihuftan, nihumb- ‘پوشاندن، پنهان کردن’» و نیبرگ نیز شاهد متنی می‌آورد. \"\n  \"آنچه محل اختلاف است پیکانِ ریشه‌شناختی است. ستاک مضارع nihumb- (مانوی nhwmb-) نشان می‌دهد که اصل واژه *ni-su-m-b- با میان‌وند خیشومی است \"\n  \"و اسم مفعول *ni-suf-ta دقیقاً nihuft می‌دهد؛ حال آنکه *ni-gōp- هرن نه خیشومی را توضیح می‌دهد نه h را. \"\n  \"هنینگ (۱۹۳۳: ۲۰۰) صورت *sub / پارسی باستان *θub را پیشنهاد کرد و امروزه همین پذیرفته است: \"\n  \"ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» ص ۸۰ ــ همان مأخذی که خود نورایی در یادداشت آورده ــ می‌نویسد «نهفت < فارسی میانه nihuft < فارسی باستان *ni-θuf-ta < ایرانی باستان *ni-suf-ta»، \"\n  \"و چونگ (۲۰۰۷) نیز نهفتن را ذیل *su(m)p/b آورده است. خطای انتساب از آنِ کتاب است، نه اسکن.\"),\n sources=[NEHOFTAN],\n ref_check=[\n  {\"ref\": \"SNS:262\", \"status\": \"supports\",\n   \"note\": \"Tavoosi's Shayast ne Shayast glossary (SNS.txt lines 14697-14704) has the entry 'ni huft ... ni + √gop ... nhwpt, nhwmb-' with the text references 262/10, 262/12, 262/15 in the concordance — i.e. the glossary does give Nourai's derivation 'ni + √gop', following Horn. (The printed page numbering of the SNS scan could not be fixed; the reference is located by the transliteration.)\"}],\n consulted=[\n  {\"src\": \"PHD\", \"where\": \"p. 59 s.v. nihuftan\", \"stance\": \"supports\",\n   \"note\": \"'nihuftan, nihumb- [nhwptn’, nhwmb- | = M, N ~] cover, hide, conceal, clothe. nihumbīdan [nhwmbytn’] = nihuftan.' — confirms the MP word, no etymology given.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. nihuftan\", \"stance\": \"supports\",\n   \"note\": \"'nihuftan [nhwptn’] nihumb- [nhwmb-] to conceal, to cover ... MPrs nhwft nhwmb- or nhwm- = nihumm- with assimilation; Paz. nahuftan nahumb-; NP nihuftan nihumb-. Verbum 200; Bailey, ZP 83.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"*su(m)p/b, pp. 368-369\", \"stance\": \"contradicts\",\n   \"note\": \"Files MMP/BMP nhwmb- /nihumb-/ and NP nihuftan under *su(m)p/b, citing Henning 1933:200 '*sub, ap. *θub = ai. śumbhati'.\"},\n  {\"src\": \"FFD\", \"where\": \"p. 80 (scan pdf p.85), s.v. نهفت\", \"stance\": \"contradicts\",\n   \"note\": \"Abolqasemi: 'نهفت < فارسی میانه nihuft < فارسی باستان *ni-θuf-ta < ایرانی باستان *ni-suf-ta ... θuf صورت اصلی suf است. s پیش از u به θ بدل شده است. ریشهٔ suf به معنی آراستن است'; and 'نهنب < فارسی میانه nihumb < فارسی باستان *ni-θumba'.\"}])\n\nN(\n id=9, lang=\"Persian\", words=\"nehoftan «نهفتن»\",\n verdict=\"confirmed\",\n derivation=(\n  \"The step MP nihuftan → NP nihuftan/nehoftan is uncontroversial and purely phonetic: the Middle Persian infinitive \"\n  \"was taken over unchanged, with the usual New Persian lowering of short i to e in the modern standard pronunciation \"\n  \"(nihuftan > nehoftan) and u > o; the present stem نهنب nehomb continues MP nihumb-. Wiktionary: 'From Middle Persian \"\n  \"nhwptn’ (nihuftan)', past stem نهفت, present stem نهنب. The Saʿdi couplet Nourai quotes ('آن شنیدی که شاهدی به نهفت') \"\n  \"uses the noun نهفت 'concealment' from the same stem. Only the ultimate root of the word is in dispute (see node #8), \"\n  \"not this link.\"),\n derivation_fa=(\n  \"گذار از فارسی میانهٔ nihuftan به فارسی نوِ «نهفتن» بی‌هیچ اختلافی و صرفاً آوایی است: مصدر پهلوی بی‌تغییر به فارسی دری رسیده \"\n  \"و در تلفظ امروزی i کوتاه به e و u به o بدل شده است (nihuftan > nehoftan)؛ ستاک مضارع «نهنب» دنبالهٔ nihumb- پهلوی است. \"\n  \"ویکی‌واژه نیز همین را می‌آورد. بیت سعدی که نورایی نقل کرده اسم «نهفت» را از همین ستاک به کار برده است. \"\n  \"تنها ریشهٔ نهایی این واژه محل بحث است (بنگرید به گرهٔ ۸)، نه این حلقه.\"),\n sources=[NEHOFTAN],\n ref_check=[\n  {\"ref\": \"HRN:236\", \"status\": \"supports\",\n   \"note\": \"Horn 1893 p.236 (HRN.txt leaf 257), entry no. 1059: 'nihuften, nuhuften ‘verbergen’, Praes. nihuft-em, nihumbīden, nuhumbīden' — the entry heading that runs on to p.237.\"},\n  {\"ref\": \"MON:4870\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in's Farhang-e Farsi p.4870 (نهفتن) — the online vajehyab/abadis text of Mo'in carries no page numbers and the local MON OCR has no page markers, so the exact page could not be confirmed.\"}],\n consulted=[\n  {\"src\": \"PHD\", \"where\": \"p. 59 s.v. nihuftan\", \"stance\": \"supports\",\n   \"note\": \"MacKenzie's entry ends '| = M, N ~', i.e. the New Persian form is identical to the Middle Persian one.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. nihuftan\", \"stance\": \"supports\",\n   \"note\": \"'... Paz. nahuftan nahumb-; NP nihuftan nihumb-.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"*su(m)p/b p.369\", \"stance\": \"supports\",\n   \"note\": \"'(+ *ni-) NP nihuftan ‘to hide, conceal, cover; to conceal oneself’' listed as the direct NW-Iranian continuant of the MP verb.\"}])\n\nN(\n id=10, lang=\"Old Persian\", words=\"gaithâ\",\n verdict=\"disputed\",\n derivation=(\n  \"OP gaiθā- is a real word ('(living) personal property, cattle', DB 1.65 gaiθām-cā), and Av. gaēθā- likewise means \"\n  \"'living possessions, herd, the world of living beings'. But it does not come from *gʷou- 'cow'. Kent's lexicon says \"\n  \"explicitly: 'gaiθā- sb. ‘(living) personal property, cattle’: Av. gaēθā- ..., Phl. gēhān ‘world’ (from gen. pl.), \"\n  \"to root PIE *gʷei- seen in OP jīv-' — i.e. to *gʷeyh₃- 'to live' (Av. gaya- 'life', jī-, NP زیستن). Nyberg agrees: \"\n  \"gēhān '< *gaiθānām, gen. pl. of Av. gaēθā-; OP gaiθā- ‘live-stock’'. The semantic overlap with 'herd' is what has \"\n  \"misled the chart; formally *gʷou- could not yield gai-. Modern scholarship therefore places gaiθā- under the root \"\n  \"Nourai himself charts elsewhere as Gwei (živeh, giti, gihân).\"),\n derivation_fa=(\n  \"gaiθā- پارسی باستان واژه‌ای واقعی است («دارایی زنده، رمه»؛ کتیبهٔ بیستون ۱٫۶۵) و gaēθā- اوستایی نیز همین معنی را دارد، \"\n  \"اما از *gʷou- «گاو» نیامده است. کنت در واژه‌نامهٔ خود صریح می‌گوید که gaiθā- به ریشهٔ هندواروپایی *gʷei- «زیستن» بازمی‌گردد \"\n  \"(همان که در jīv- پارسی باستان و «زیستن» فارسی دیده می‌شود). نیبرگ نیز gēhān پهلوی را از *gaiθānām، اضافی جمع gaēθā-، می‌گیرد. \"\n  \"همانندی معنایی («رمه») سبب این خطا شده است؛ از نظر آوایی *gʷou- هرگز gai- نمی‌دهد. \"\n  \"پژوهش امروزی این واژه را زیر ریشهٔ Gwei (زیستن، گیتی، گیهان) می‌نهد، نه Gwou.\"),\n sources=[],\n ref_check=[\n  {\"ref\": \"SOD:180\", \"status\": \"partial\",\n   \"note\": \"Gharib, Sogdian Dictionary printed p.180 (SOD_pages.txt \\\\f-block 246), entry 4523: 'γyδh B — yeθ ? ©<OP gaiθa; MP gēh(bān); gih — flock. TSP 13ii, 14; S W, IIJ 1976, 61.' The page confirms OP gaiθa 'flock' and the Sogdian descendant, but says nothing about a connection to *gʷou-.\"}],\n consulted=[\n  {\"src\": \"KNT\", \"where\": \"Lexicon s.v. gaiθā- (KNT.txt line 5340)\", \"stance\": \"contradicts\",\n   \"note\": \"'gaiθā- sb. ‘(living) personal property, cattle’: Av. gaēθā- ‘individual living being, pl. world; household, property’, Phl. gēhān ‘world’ (from gen. pl.), to root PIE *gʷei- seen in OP jīv-. For varying interpretations, see Bthl. Lex. 85, with lit. — gaiθām-cā asf. DB 1.65.'\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. gēhān\", \"stance\": \"contradicts\",\n   \"note\": \"'gēhān [gyh’n] ... the world of creatures ... < *gaiθānām, gen. pl. of Av. (476 sqq.) gaēθā-; OP gaiθā- ‘live-stock’; Aram. lw. gyty ‘herds’; MPrth gyh (< gaiθa) ‘world’ ... NP gehān, gihān, jihān.'\"},\n  {\"src\": \"BRT\", \"where\": \"cols. 476 ff. s.v. gaēθā-\", \"stance\": \"contradicts\",\n   \"note\": \"Bartholomae treats gaēθā- 'lebendes Besitztum' at cols. 476 ff. (the column Nyberg cites), under the family of gay-/jī- 'leben', not under gav-.\"}])\n\nN(\n id=11, lang=\"Sogdian\", words=\"gydh\",\n verdict=\"confirmed\",\n derivation=(\n  \"Sogdian γyδh (read yeθ/γēδ) 'flock, herd' is the Sogdian reflex of the same Old Iranian *gaiθā- as OP gaiθā-: \"\n  \"intervocalic *-θ- is written -δ- in Buddhist Sogdian and the final -h is the orthographic marker of the feminine \"\n  \"ā-stem. Gharib's entry states the derivation in so many words, and gives the Middle Persian congeners gēh(bān), gih. \"\n  \"The word is attested in the Buddhist Sogdian text TSP 13ii,14 (Benveniste), discussed by Sims-Williams, IIJ 1976, 61. \"\n  \"The arrow OP gaiθā → Sogd. γyδh is really 'both continue Old Iranian *gaiθā-' rather than a borrowing from Old Persian, \"\n  \"Sogdian being a separate East Iranian branch — but that is Nourai's habitual shorthand and does not affect the substance.\"),\n derivation_fa=(\n  \"«γyδh» سغدی (خوانش yeθ/γēδ) به معنی «رمه، گله» بازماندهٔ همان *gaiθā- ایرانی باستان است که gaiθā- پارسی باستان نیز از آن آمده؛ \"\n  \"θ میان‌واکه‌ای در سغدی بودایی با δ نوشته می‌شود و h پایانی نشانهٔ املایی ستاک مؤنث ā است. \"\n  \"قریب (فرهنگ سغدی، ص ۱۸۰، مدخل ۴۵۲۳) خودِ این اشتقاق را می‌آورد و برابرهای فارسی میانهٔ gēh(bān) و gih را ذکر می‌کند. \"\n  \"تنها نکته آنکه سغدی شاخه‌ای مستقل از ایرانی شرقی است و واژه را از پارسی باستان وام نگرفته، بلکه هر دو از یک صورت ایرانی باستان‌اند؛ \"\n  \"این کوتاه‌نویسی همیشگی نورایی است و به اصل ادعا آسیبی نمی‌زند.\"),\n sources=[],\n ref_check=[\n  {\"ref\": \"SOD:180\", \"status\": \"supports\",\n   \"note\": \"Gharib printed p.180 (SOD_pages.txt \\\\f-block 246) entry 4523: 'γyδh B | yeθ ? ©<OP gaiθa; MP gēh(bān); gih | flock | TSP 13ii, 14; S W, IIJ 1976, 61.'\"}],\n consulted=[\n  {\"src\": \"SOD\", \"where\": \"p.180 entry 4523\", \"stance\": \"supports\",\n   \"note\": \"As quoted; the neighbouring entry 4521 γyδ 'this, that same' is a different word.\"},\n  {\"src\": \"NYB\", \"where\": \"Part II Glossary s.v. gēhān\", \"stance\": \"supports\",\n   \"note\": \"Nyberg gives the parallel Middle Persian/Parthian reflexes of *gaiθa- ('MPrth gyh (< gaiθa) ‘world’, pl. gyh’n'), the forms Gharib compares.\"},\n  {\"src\": \"SOG\", \"where\": \"Henning, Sogdica (Selected Papers II)\", \"stance\": \"silent\",\n   \"note\": \"grep of HENNING_selected_papers.txt for 'γyδ'/'gyδ' in the Sogdica glossary returns no discussion of this word.\"}])\n\nN(\n id=12, lang=\"Germanic\", words=\"koŭs\",\n verdict=\"transcription_suspect\",\n derivation=(\n  \"The derivation itself is right — PIE nom. sg. *gʷōws gives Proto-Germanic *kōz (acc. *kōm > *kūz), whence OE cū, \"\n  \"OS kō, OHG kuo, ON kýr — but the form printed in the book, 'koŭs', is not a possible Germanic shape: Germanic has \"\n  \"no final -s in this word (Verner's law and rhotacism give -z). Nourai's source, the 1976 AHD appendix, prints \"\n  \"'Germanic *kōuz'; the 1985 Watkins revision of the same list reads 'Germanic *kōuz (> *kūz) in Old English cū, cȳ, \"\n  \"cȳe, cow'. I checked the printed page (PDF p.217, book p.187, copy at data/verification/sources/refs/ocr/BOOK/217.png): \"\n  \"the book really does print 'koŭs', so the extraction is faithful and the slip is Nourai's.\"),\n derivation_fa=(\n  \"اصل اشتقاق درست است: نهادی مفرد هندواروپایی *gʷōws در ژرمنی آغازین *kōz (رایی *kōm > *kūz) می‌دهد که انگلیسی باستان cū، \"\n  \"ساکسونی باستان kō، آلمانی علیای باستان kuo و نورس باستان kýr از آن آمده‌اند. اما صورتی که کتاب چاپ کرده، «koŭs»، \"\n  \"در ژرمنی ممکن نیست؛ در این واژه s پایانی وجود ندارد و بر پایهٔ قانون ورنر و ابدال z>r باید *kōuz باشد. \"\n  \"مأخذ نورایی (پیوست ریشه‌های هندواروپایی AHD) صورت *kōuz را می‌آورد. تصویر صفحهٔ چاپی (ص ۱۸۷ کتاب) را دیدم: \"\n  \"کتاب همان «koŭs» را چاپ کرده است؛ پس خطا از خواندن اسکن نیست، بلکه خطای چاپی/نگارشی خود کتاب است.\"),\n error_in=\"book\",\n book_prints=\"koŭs\",\n correct_form=\"*kōuz (Proto-Germanic; Watkins/AHD)\",\n sources=[PIE],\n ref_check=[\n  {\"ref\": \"KLN\", \"status\": \"supports\",\n   \"note\": \"Klein p.364 s.v. 'cow': 'ME. ky, kye, fr. OE. cu, rel. to OS. ko, OFris. ku, MDu. coe, Du. koe, OHG. chuo, kuo, MHG. kuo, G. Kuh, Dan. and Swed. ko, ON. kyr' — no *kous.\"},\n  {\"ref\": \"AHD\", \"status\": \"partial\",\n   \"note\": \"Watkins 1985 s.v. gʷou-, §1: 'Germanic *kōuz (> *kūz) in Old English cū, cȳ, cȳe, cow: COW, (KINE); COWSLIP' — the reconstruction is *kōuz, not koŭs.\"},\n  {\"ref\": \"POK\", \"status\": \"supports\",\n   \"note\": \"Pokorny pp.482-483: 'Old High German chuo, ... Old English Old Frisian cu, Old Icelandic kyr ‘cow’ (*kūz : *kōr… gʷous)'.\"}],\n consulted=[\n  {\"src\": \"SKT\", \"where\": \"s.v. Cow (1) (SKT.txt line 4243)\", \"stance\": \"supports\",\n   \"note\": \"'Cow (1), female of the bull. (E.) A.S. cū, pl. cȳ, whence M.E. ky ... + Du. koe, Icel. kýr, Swed. Dan. ko, G. kuh, Irish and Gael. bó, L. bos, Gk. βοῦς, Skt. go.'\"},\n  {\"src\": \"KLN\", \"where\": \"vol. I p.364 s.v. cow\", \"stance\": \"supports\",\n   \"note\": \"As quoted above.\"}])\n\nN(\n id=13, lang=\"English\", words=\"cow\",\n verdict=\"confirmed\",\n derivation=(\n  \"PGmc. *kōz > OE cū (pl. cȳ) > ME cou/ky > NE cow; the Modern English plural kine is the old umlauted plural cȳ \"\n  \"with a second, weak plural ending added (cȳ-n). Klein and Skeat both give the chain, and Watkins files COW and KINE \"\n  \"under gʷou- §1. A wholly regular and uncontroversial Germanic inheritance.\"),\n derivation_fa=(\n  \"از ژرمنی آغازین *kōz به انگلیسی باستان cū (جمع cȳ)، سپس انگلیسی میانه cou/ky و انگلیسی نو cow. \"\n  \"جمع کهنِ kine همان cȳ است که پسوند جمع ضعیف -n دوباره بر آن افزوده شده. \"\n  \"کلاین، اسکیت و واتکینز (AHD) هر سه همین زنجیره را می‌آورند. زنجیره‌ای کاملاً بی‌اختلاف و ادعای نورایی درست است.\"),\n sources=[PIE],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book; checked against Klein, Skeat and Watkins instead.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"vol. I p.364 s.v. cow\", \"stance\": \"supports\",\n   \"note\": \"'cow, n. — ME. ky, kye, fr. OE. cu ... Cp. kine.'\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Cow (1)\", \"stance\": \"supports\",\n   \"note\": \"'A.S. cū, pl. cȳ, whence M.E. ky, and the double pl. ky-en = kine.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 gʷou- §1\", \"stance\": \"supports\",\n   \"note\": \"'Old English cū ... : COW, (KINE); COWSLIP.'\"}])\n\nN(\n id=14, lang=\"Latin\", words=\"bôs, bov-\",\n verdict=\"confirmed\",\n derivation=(\n  \"Latin bōs, gen. bovis 'ox, cow' shows b- for the expected native v- (*gʷōws should have given Latin *vōs); the b- \"\n  \"betrays borrowing from the Sabellic (Oscan-Umbrian) neighbours, where PIE *gʷ regularly became b (Umbrian bum \"\n  \"'bovem', bue 'bove', Oscan Buvaianud). Pokorny states this outright: 'Latin bos, bovis m. f. ‘cattle’ \"\n  \"(Oscan-Umbrian loanword for Latin *vōs)'. The stem alternation bov- (before a vowel) / bū- (before a consonant) \"\n  \"reflects *gʷow-/*gʷōu-.\"),\n derivation_fa=(\n  \"لاتینی bōs، اضافی bovis «گاو» به‌جای v آغازینِ انتظاری b دارد؛ چون *gʷ هندواروپایی در لاتین باید v می‌داد (*vōs). \"\n  \"این b نشان می‌دهد که واژه از زبان‌های همسایهٔ اسکو-اومبریایی وام گرفته شده که در آنها *gʷ به b بدل می‌شود \"\n  \"(اومبریایی bum «govem»، bue، اسکی Buvaianud). پوکورنی صریحاً می‌نویسد «bos, bovis وام‌واژه‌ای اسکو-اومبریایی به‌جای *vōs لاتینی». \"\n  \"دوگانگی ستاک bov- (پیش از واکه) و bū- (پیش از همخوان) بازتاب *gʷow-/*gʷōu- است. ادعای نورایی درست است.\"),\n sources=[PIE],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 gʷou- §2: 'Latin bōs (stem bov-), ox, bull, cow: BEEF, BOVINE, BUGLE1; OVIBOS.'\"}],\n consulted=[\n  {\"src\": \"POK\", \"where\": \"gʷou- pp.482-483\", \"stance\": \"supports\",\n   \"note\": \"'Latin bos, bovis m. f. ‘cattle’ (Oscan-Umbrian loanword for Latin *vōs); derivatives of stem bov- (*gʷou- before vowel) or bu- (*gʷou- before consonance) ... Umbrian bum ‘bovem’, bue ‘bove’, Oscan in Buvaianud.'\"},\n  {\"src\": \"KLN\", \"where\": \"vol. I p.364 s.v. cow / s.v. beef p.161\", \"stance\": \"supports\",\n   \"note\": \"s.v. beef: 'fr. L. bovem, acc. of bos, ‘ox’. See bovine'; s.v. cow: 'cogn. with ... L. bos, Gk. βοῦς'.\"}])\n\nN(\n id=15, lang=\"English\", words=\"beef\",\n verdict=\"confirmed\",\n derivation=(\n  \"Latin acc. bovem > Vulgar Latin *bovem > Old French boef, buef (Mod. Fr. bœuf) 'ox; beef' > Middle English boef, \"\n  \"beef (13th c., with the usual Anglo-Norman ue > ee), Modern English beef. The word entered English as the meat-name \"\n  \"of the Norman table beside the native animal-name cow — the classic pair noticed since Walter Scott. Klein: \"\n  \"'beef, n. — ME. boef, beef, fr. OF. boef, buef (F. bœuf), fr. L. bovem, acc. of bos, ‘ox’.'\"),\n derivation_fa=(\n  \"رایی لاتینی bovem از راه لاتین عامیانه به فرانسهٔ باستان boef/buef «گاو؛ گوشت گاو» رسید و از آنجا در سدهٔ سیزدهم میلادی \"\n  \"به انگلیسی میانه boef/beef و سپس انگلیسی نو beef راه یافت (ue فرانسویِ نورمان در انگلیسی به ee بدل شد). \"\n  \"این واژه نام گوشت در سفرهٔ نورمان‌ها بود در برابر نام جانورِ بومی cow. کلاین همین زنجیره را می‌آورد. ادعای نورایی درست است.\"),\n sources=[PIE],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference in the book for this node; checked against Klein and Watkins.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"vol. I p.161 s.v. beef (KLN_1966.txt line 4648)\", \"stance\": \"supports\",\n   \"note\": \"'beef, n. — ME. boef, beef, fr. OF. boef, buef (F. bœuf), fr. L. bovem, acc. of bos, ‘ox’. See bovine and cp. next word. Cp. also biffin.'\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 gʷou- §2 and the index\", \"stance\": \"supports\",\n   \"note\": \"index line 'BEEF gʷou-'; entry §2 'Latin bōs (stem bov-) ...: BEEF, BOVINE'.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Cow (1), cross-reference 'See Beef'\", \"stance\": \"supports\",\n   \"note\": \"Skeat cross-refers cow to beef; the Beef headword itself is badly OCRed in SKT.txt (only the cross-reference at line 22855 'beef—cow' is legible).\"}])\n\nN(\n id=16, lang=\"Greek\", words=\"bous\",\n verdict=\"confirmed\",\n derivation=(\n  \"Attic βοῦς (Doric βῶς), gen. βο(F)ός, 'ox, cow', from *gʷōws; the initial b- is the regular Greek treatment of PIE \"\n  \"*gʷ before a back vowel, and the Attic nominative has the 'spurious' ou of the contracted paradigm (Doric βῶς keeps \"\n  \"the inherited long ō). Pokorny: 'gr. Attic βοῦς m. f. ‘cattle, cow’, Akk. βοῦν (both with fake ou in place of old \"\n  \"*βωυς), Doric βως ... Gen. βο(F)ός'. It is the source of the compounds βου-κόλος 'cowherd', βού-τυρον 'butter' \"\n  \"and the prefix βου- 'huge'.\"),\n derivation_fa=(\n  \"یونانی آتیکی βοῦς (دُریک βῶς)، اضافی βο(ϝ)ός، «گاو»، از *gʷōws. b آغازین بازتاب عادی *gʷ هندواروپایی پیش از واکهٔ پسین در یونانی است، \"\n  \"و ou در نهادی آتیکی «ou دروغین» ناشی از هم‌آمیزی است، حال آنکه دُریک βῶς ōی موروثی را نگه داشته است. \"\n  \"پوکورنی همین را می‌گوید. این واژه پایهٔ ترکیب‌هایی چون βου-κόλος «گاوبان»، βού-τυρον «کره» و پیشوند تشدیدی βου- است. \"\n  \"ادعای نورایی درست است.\"),\n sources=[PIE],\n ref_check=[\n  {\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"Watkins 1985 gʷou- §3: 'Greek bous, ox, bull, cow: BOUSTROPHEDON, BUCEPHALUS, BUCOLIC, BULIMIA, BUPRESTID, BUTTER, (BUTYRIC).'\"}],\n consulted=[\n  {\"src\": \"POK\", \"where\": \"gʷou- pp.482-483\", \"stance\": \"supports\",\n   \"note\": \"'gr. Attic βοῦς m. f. ‘cattle, cow’, Akk. βοῦν (both with fake ou in place of old *βωυς) ..., Doric βως, Akk. βων, Gen. βο(F)ός, etc.; also in βου-λυτός ... βού-τυρον m. ‘butter’ (out of it Latin butyrum) ... actually ‘cow’s cheese’ (τυρός ‘cheese’).'\"},\n  {\"src\": \"KLN\", \"where\": \"vol. I p.364 s.v. cow\", \"stance\": \"supports\",\n   \"note\": \"'cogn. with ... Gk. βοῦς (for *gwaus-), ‘ox’ ... Cp. also Bos, boustrophedon, bovine, Bucentaur, Bucephalus, Buceros, bucolic, buffalo, bugle, bugloss, Bupleurum, Buprestis, Busycon, butter ... hecatomb.'\"}])\n\nN(\n id=17, lang=\"English\", words=\"buffalo, butter\",\n verdict=\"plausible\",\n derivation=(\n  \"BUTTER is fully confirmed: Gk. βούτυρον 'butter', literally 'cow-cheese' (βοῦς + τυρός 'cheese') > Lat. butyrum > \"\n  \"OE butere > NE butter (Etymonline; Klein s.v. butter; Watkins gʷou- §3). The only caveat, noted by Etymonline and \"\n  \"already by Skeat ('Really Scythian; the Greek sense is a forced one'), is that the Greek compound may itself be a \"\n  \"folk-etymological reshaping of a Scythian word, butter being a barbarian food for the Greeks. \"\n  \"BUFFALO is only indirectly and doubtfully connected: NE buffalo < Portuguese búfalo < Late Latin bufalus, variant of \"\n  \"Latin bubalus < Gk. βούβαλος, which meant 'African antelope' before it meant 'buffalo'. Klein says βούβαλος is \"\n  \"'prob. rel. to βοῦς'; Skeat flatly says '(Not a true Greek word)'; and Pokorny warns that Gk. βούβαλος 'gazelle' \"\n  \"'with Old Indic gavala- ‘wild buffalo’ is not to be immediately equated'. Watkins does not list BUFFALO under gʷou- \"\n  \"at all. So the butter arrow is certain, the buffalo arrow is a possibility only.\"),\n derivation_fa=(\n  \"دربارهٔ butter تردیدی نیست: یونانی βούτυρον «کره»، تحت‌اللفظ «پنیرِ گاو» (βοῦς + τυρός «پنیر») > لاتینی butyrum > \"\n  \"انگلیسی باستان butere > انگلیسی نو butter. تنها نکته آنکه اتیمانلاین و اسکیت احتمال می‌دهند خودِ ترکیب یونانی \"\n  \"ریشه‌شناسی عامیانه‌ای بر روی واژه‌ای سکایی باشد، چون کره خوراک یونانیان نبوده است. \"\n  \"اما buffalo پیوندی غیرمستقیم و مشکوک دارد: از پرتغالی búfalo، از لاتینی متأخر bufalus (گونهٔ bubalus)، از یونانی βούβαλος \"\n  \"که نخست «غزال آفریقایی» معنی می‌داده است. کلاین می‌گوید «احتمالاً مربوط به βοῦς»؛ اسکیت می‌گوید «واژهٔ یونانی اصیل نیست»؛ \"\n  \"و پوکورنی هشدار می‌دهد که نباید βούβαλος را بی‌درنگ با gavala- سنسکریت یکی گرفت. واتکینز نیز buffalo را ذیل gʷou- نیاورده است. \"\n  \"پس بخش نخست ادعا با احتیاط پذیرفتنی و بخش دوم قطعی است.\"),\n sources=[BUTTER, BUFFALO],\n ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference in the book for this node; checked against Klein, Skeat, Pokorny, Watkins and Etymonline.\"}],\n consulted=[\n  {\"src\": \"KLN\", \"where\": \"vol. I p.211 s.v. buffalo; p.222 s.v. butter\", \"stance\": \"partial\",\n   \"note\": \"'buffalo, n. — Port. buffalo, fr. L. bufalus, a collateral form of bubalus, fr. Gk. βούβαλος, ‘an African antelope’, later ‘buffalo’, which is prob. rel. to βοῦς'; 'butter, n. — OE. butere, buttor-, fr. L. butyrum ... fr. Gk. βούτυρον, ‘butter’, lit. ‘cow cheese’, which is compounded of βοῦς, ‘ox, cow’, and τυρός, ‘cheese’.'\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Buffalo (line 2399) and Butter (line 2535)\", \"stance\": \"partial\",\n   \"note\": \"'Buffalo. (Span.-L.-Gk.) Span. bufalo ... — L. bufalus, also bubalus. — Gk. βούβαλος, a buffalo, wild ox, antelope. (Not a true Gk. word.)'; 'Butter ... — Gk. βούτυρον, butter; lit. ox-cheese ... Really Scythian; the Gk. sense is a forced one.'\"},\n  {\"src\": \"POK\", \"where\": \"gʷou- p.483\", \"stance\": \"partial\",\n   \"note\": \"'bubulus ds. (lautlich identical with gr. βούβαλος ‘gazelle’, that with Old Indic gavala- ‘wild buffalo’ is not to be immediately equated)'.\"}])\n\nN(\n id=18, lang=\"Indo-European\", words=\"Gwôu\",\n verdict=\"plausible\",\n derivation=(\n  \"Pokorny does set up the root Nourai writes 'Gwôu': 'Root/lemma: gʷōu-, gʷū-, Meaning: dung, dirt' (pp. 483-485), \"\n  \"with Skt. gū-tha-ḥ 'excrement', Av. gū-θa- 'ordure', Arm. ku, Slavic *govьno, MHG quāt/G. Kot, OE cweād. \"\n  \"What is not established is the arrow Nourai draws, i.e. that this root is a branch of gʷou- 'cattle'. Pokorny \"\n  \"prints it as a separate lemma immediately after gʷou- and does not derive one from the other; Watkins/AHD has no \"\n  \"'dung' root at all (only one gʷou- entry, 'Ox, bull, cow'). On the other side, Mann's Indo-European Comparative \"\n  \"Dictionary does unify them — 'gʷou- (gu-) ‘ox; filth’ ... R. gov-no ‘dung’' and 'gʷōutos ... (an associate of \"\n  \"gʷōus)' — and the semantic bridge ('cow-dung' > 'dung') is the same one that produced Old Irish buach 'cow-dung, lye'. \"\n  \"So the connection is a defensible minority view, not a demonstrated one.\"),\n derivation_fa=(\n  \"پوکورنی ریشه‌ای را که نورایی «Gwôu» نوشته به‌راستی دارد: «gʷōu-، gʷū- به معنی سرگین، پلیدی» (ص ۴۸۳–۴۸۵)، \"\n  \"با سنسکریت gū-tha-, اوستایی gū-θa-, ارمنی ku، اسلاوی *govьno و آلمانی Kot. \"\n  \"آنچه اثبات‌نشده مانده پیکانی است که نورایی کشیده، یعنی اینکه این ریشه شاخه‌ای از gʷou- «گاو» باشد. \"\n  \"پوکورنی آن را مدخلی جداگانه بی‌درنگ پس از gʷou- می‌آورد و یکی را از دیگری نمی‌گیرد، و واتکینز (AHD) اصلاً چنین ریشه‌ای ندارد. \"\n  \"در برابر، مان در فرهنگ تطبیقی هندواروپایی هر دو را یکی می‌داند («gʷou- (gu-) ‘گاو؛ پلیدی’») و پل معنایی «سرگینِ گاو > سرگین» \"\n  \"همان است که در ایرلندی باستان buach «سرگین گاو» دیده می‌شود. پس این پیوند دیدگاهی اقلیتی و پذیرفتنی با احتیاط است، نه اثبات‌شده.\"),\n sources=[],\n ref_check=[\n  {\"ref\": \"AHD:1520\", \"status\": \"not_found\",\n   \"note\": \"the 1976 AHD appendix p.1520 is not available online; the 1985 Watkins revision of the same list (AHD_watkins1985.txt) has a single gʷou- entry, 'Ox, bull, cow ... [Pok. gʷou- 482]', and no root glossed 'dung' — grep for 'dung' in the whole file returns only kekʷ- and sker-4.\"},\n  {\"ref\": \"POK:483\", \"status\": \"supports\",\n   \"note\": \"POK_full.txt: 'Root/lemma: gʷōu-, gʷū-. Meaning: dung, dirt. ... Material: Old Indic gu-tha-h, -m ‘excrement’, Avestan gu-θa- n. ‘smut, ordure’ ... References: WP. I 694 ff., WH. I 118f., Trautmann 81. Page(s): 483-485.' The page number is right; but Pokorny lists it as a lemma of its own, not as a derivative of gʷou-.\"}],\n consulted=[\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷou- (gu-) and gʷōutos (IEC.txt lines 5199, 5322 ff.)\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'gʷou- (gu-) ‘ox; filth’ ... R. cf. gumnó ... beside Cz. hov-ězí adj. ‘beef’, hov-ado ‘beast’; hov-no, R. gov-no ‘dung’'; and 'gʷōutos ... (an associate of gʷōus, q.v.) Skt. gota ‘cow’; gūthaḥ ‘dung’; Av. gūθō, Per. gūh, id.'\"},\n  {\"src\": \"WLD\", \"where\": \"WP. I 694 ff.\", \"stance\": \"partial\",\n   \"note\": \"Pokorny's own reference line for the 'dung' lemma is 'WP. I 694 ff.' while that for 'cattle' is 'WP. I 696 f.' — Walde-Pokorny likewise treat them as adjacent but separate articles.\"},\n  {\"src\": \"ARY\", \"where\": \"Latin index, root گوه (scan pdf p.447)\", \"stance\": \"partial\",\n   \"note\": \"Aryanpur gives the dung word its own root heading ('GwuH', references POKORNY, BUCK 216, MALLORY & ADAMS, MACKENZIE (EXCREMENT) 113) separate from his گاو root (scan pdf p.423, GAUSH/GAO- Avestan, GAV Old Persian, GAW Pahlavi).\"}])\n\nN(\n id=19, lang=\"Avestan\", words=\"gutha\",\n verdict=\"confirmed\",\n derivation=(\n  \"Av. gūθa- n. 'dirt, dung', attested in the compounds gūθō.varəta- 'crawling in filth' and maiδyō-gūθa-, is the exact \"\n  \"match of Skt. gū-tha-ḥ 'excrement': both are *gū- + the -tha-/-θa- noun suffix of the Indo-Iranian type. Pokorny gives \"\n  \"them together under gʷōu-, gʷū- 'dung, dirt' ('Old Indic gu-tha-h ... Avestan gu-θa- n. ‘smut, ordure’'), and \"\n  \"Bartholomae records the word as a plain Younger Avestan noun.\"),\n derivation_fa=(\n  \"اوستایی gūθa- (خنثی) «چرک، سرگین» که در ترکیب‌های gūθō.varəta- «در پلیدی خزنده» و maiδyō-gūθa- گواهی شده، \"\n  \"برابر دقیق سنسکریت gū-tha- «فضله» است؛ هر دو از *gū- با پسوند اسم‌ساز هندوایرانی -tha-/-θa- ساخته شده‌اند. \"\n  \"پوکورنی هر دو را زیر gʷōu-، gʷū- «سرگین» می‌آورد و بارتولمه نیز آن را اسمی از اوستای متأخر ثبت کرده است. \"\n  \"ادعای نورایی درست است.\"),\n sources=[],\n ref_check=[\n  {\"ref\": \"POK:484\", \"status\": \"supports\",\n   \"note\": \"The lemma gʷōu-, gʷū- 'dung, dirt' runs pp.483-485 and reads: 'Old Indic gu-tha-h, -m ‘excrement’, Avestan gu-θa- n. ‘smut, ordure’ (only by Gramm. also guvati ‘cacat’, gunam ‘cacatum’); Armenian kuav ...'.\"}],\n consulted=[\n  {\"src\": \"BRT\", \"where\": \"s.v. gūθa- (BRT.txt line 10392)\", \"stance\": \"supports\",\n   \"note\": \"'j. gūθa- n. ‘Schmutz, Kot’'; cf. also 'j. maiδyō-gūθa- Adj. ‘mit Unrat, Kot behaftet, unrein’: nasaum ~am V.7.25' (line 19689).\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷōutos\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'Skt. gota ‘cow’; gūthaḥ ‘dung’; Av. gūθō, Per. gūh, id.; Arm. gu, o-st. ‘dung of wild animals’ ... MHG quot, quāt, OE cwead, OFris. quad ‘dung’.'\"},\n  {\"src\": \"HRN\", \"where\": \"p.211 no. 947\", \"stance\": \"supports\",\n   \"note\": \"'gūh ‘Schmutz, Kot’. aw. gūθa- in gūθō.varəta- ‘im Schmutz kriechend’, maiδyō-gūθa-; phlv. gūh in gūhvart (Vd. 14,16); skr. gūtha- ‘Exkremente’; arm. ku ‘Mist’; ksl. govьno.'\"}])\n\nN(\n id=20, lang=\"Persian\", words=\"goh «گوه»; cŭd «کود»; tŭdeh «توده»\",\n verdict=\"disputed\",\n derivation=(\n  \"Only the first of the three words belongs here. goh/gūh 'dung' is the regular reflex of Av. gūθa- through MP gūh \"\n  \"(attested in Vd. 14.16 gūhvart): Iranian intervocalic *θ > MP h, and the word survives across the Iranian \"\n  \"dialects (Kurdish gū, Pashto γul, Balochi gūh, Wakhi gū) — confirmed (Horn no. 947, Bartholomae, Mo'in). \"\n  \"کود kūd 'manure, heap of corn' is different: Wiktionary derives NP کود from MP kōδ and relates it to Skt. kūṭa- \"\n  \"'heap, multitude' and Arm. koyt 'heap, pile'; Henning (Sogdica, the SOG:57 Nourai cites) treats NPers. kōd as \"\n  \"'stack, heap of corn or dung' with Arm. koyt, i.e. a 'heap' word, not a 'dung' word. Mo'in's footnote at BQT:1723 \"\n  \"does connect it with gūtha, but the k- (not g-) and the primary sense 'heap' tell against it. توده tūda 'heap' is \"\n  \"certainly unrelated: Wiktionary derives it from Proto-Iranian *taw(H)táH < PIE *tewtéh₂ 'people, tribe' \"\n  \"(cf. Lat. tōtus, Lith. tautà, Goth. þiuda), and Henning at Sogdica p.57-58 equates it with Sogdian twδ’k \"\n  \"'heap/aggregate' — no dung element anywhere. Node verdict = the worst of the three.\"),\n derivation_fa=(\n  \"از این سه واژه تنها نخستین به این ریشه تعلق دارد. «گوه/گُه» بازماندهٔ قاعده‌مند gūθa- اوستایی است از راه فارسی میانهٔ gūh \"\n  \"(در وندیداد ۱۴٫۱۶ به صورت gūhvart)؛ θ ایرانی در میان دو واکه در فارسی میانه به h بدل شده و واژه در گویش‌های ایرانی زنده مانده است \"\n  \"(کردی gū، پشتو γul، بلوچی gūh، وخی gū) ــ این بخش تأیید می‌شود. \"\n  \"اما «کود» چیز دیگری است: ویکی‌واژه آن را از فارسی میانهٔ kōδ و هم‌ریشه با سنسکریت kūṭa- «توده» و ارمنی koyt «توده» می‌داند، \"\n  \"و هنینگ در «سغدیکا» (همان SOG:57 که نورایی آورده) kōd فارسی را «انبار یا تودهٔ غله» می‌گیرد و با koyt ارمنی می‌سنجد. \"\n  \"حاشیهٔ معین در برهان قاطع (ص ۱۷۲۳) آن را به gūtha می‌رساند، ولی کافِ آغازین (نه گاف) و معنی نخستینِ «توده» با این نظر نمی‌خواند. \"\n  \"«توده» بی‌گمان بی‌ارتباط است: از ایرانی آغازین *taw(H)táH و آن از هندواروپایی *tewtéh₂ «مردم، قبیله» (قس لاتینی tōtus، لیتوانیایی tautà، گوتی þiuda). \"\n  \"پس ادعای نورایی دربارهٔ «گوه» درست و دربارهٔ «کود» و «توده» پذیرفتنی نیست.\"),\n sources=[TUDEH, KUD],\n ref_check=[\n  {\"ref\": \"BQT:1723\", \"status\": \"supports\",\n   \"note\": \"Borhan-e Qate' vol. 3, scan pdf p.516 (= printed 1723), entry کود ('توده و خرمن غله را گویند؛ و آباری که برزمین زراعت ریزند تا زمین قوت گیرد'), Mo'in's footnote: 'کود ... اوستایی و سانسکریت gūtha (که)، قس: kot (تات) ... پس لغةً بمعنی پلیدی آدمی و جانوران است که جهت قوت بر زمین زراعتی ریزند. رک: هرمزدنامه ص ۳۱۷-۳۱۹.' — Mo'in does make Nourai's claim, but see 'consulted' for the modern objection.\"},\n  {\"ref\": \"BQT:1863\", \"status\": \"supports\",\n   \"note\": \"Same volume, scan pdf p.659 (= printed ~1862/1863), footnote on گوه: 'گوه، بضم اول و های ملفوظ، بمعنی سرگین، اوستا gūθa- [در gūθō.varəta-] ...؛ پهلوی gūh ...؛ سانسکریت gūtha-، ارمنی ku (کود، فضله)، کردی gū، افغانی ghul، بلوچی gūh، وخی gū، اشکاشمی gūš «اسحق ۹۴۷»'.\"},\n  {\"ref\": \"HRN:211\", \"status\": \"partial\",\n   \"note\": \"Horn 1893 p.211 (HRN.txt leaf 232) no. 947 covers گوه fully ('gūh ‘Schmutz, Kot’. aw. gūθa- ...; phlv. gūh; skr. gūtha-; arm. ku') but says nothing about کود or توده.\"},\n  {\"ref\": \"SOG:57\", \"status\": \"partial\",\n   \"note\": \"Henning, Sogdica pp.57-58 (HENNING_selected_papers.txt line 2358): 'NPers. kōd (Arm. koit; cf. also the Pahl. transl. of Av. ...) ‘stack, heap of corn or dung’ ... use NPers. tōda ‘heap’, which [it would] be tempting to identify with Sogd. twδ’k ... Thus we may assume that the Sogd. gloss means “refuse on a heap”'. The page really does discuss kōd and tōda together, as Nourai says, but Henning connects them with Arm. koyt 'heap' and Sogd. twδ’k, not with gūθa 'dung'.\"}],\n consulted=[\n  {\"src\": \"HRN\", \"where\": \"p.211 no. 947\", \"stance\": \"partial\", \"note\": \"supports گوه only; کود and توده are absent.\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷōutos\", \"stance\": \"partial\",\n   \"note\": \"Mann lists 'Per. gūh' under the dung root, but neither کود nor توده.\"},\n  {\"src\": \"BQT\", \"where\": \"vol. 3, printed pp.1723 and ~1863\", \"stance\": \"partial\",\n   \"note\": \"Mo'in supports both گوه and کود from gūtha; his کود etymology is contradicted by the k-/g- mismatch and by Wiktionary's MP kōδ : Skt. kūṭa- 'heap' : Arm. koyt.\"},\n  {\"src\": \"PHD\", \"where\": \"no MP entry *kōd or *tōdag traced to gūh\", \"stance\": \"silent\",\n   \"note\": \"MacKenzie has neither kōd nor tōdag under a dung root; grep of PHD.txt for 'gūh' finds no headword.\"}])\n\nentry = {\n \"entry\": 0,\n \"root\": \"Gwou\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gʷṓws (gen. *gʷéws, acc. *gʷṓm) 'cow, ox, head of cattle'\",\n \"note\": (\n  \"The root, the language label and the gloss are all correct: Pokorny's gʷou- 'cattle' (pp. 482-483) and \"\n  \"Watkins/AHD gʷou- 'Ox, bull, cow' are the same reconstruction now written *gʷṓws. It is one of the best-attested \"\n  \"PIE nouns, with a full root-noun paradigm continued almost intact in Indo-Iranian. Two things on this chart are \"\n  \"not equally secure. (a) The 'dung' branch (#18-#20): Pokorny prints gʷōu-, gʷū- 'dung, dirt' as a separate lemma \"\n  \"(pp. 483-485) and does not derive it from 'cattle'; only Mann unifies them. (b) Two whole sub-trees do not belong \"\n  \"under this root at all: OP gaiθā- 'herd' (#10-#11) is from *gʷeyh₃- 'to live' (Kent, Nyberg), the root Nourai \"\n  \"himself charts as Gwei on p.205; and the nihuftan chain (#6-#9) rests on Horn's 1893 *ni-gōp-, which Horn already \"\n  \"reports Bartholomae doubting and which Henning 1933, Abolqasemi (the FFD:80 dissent quoted in the book's own note) \"\n  \"and Cheung 2007 replace with *ni-su(m)b-. Nourai's references are unusually well chosen here: every one that could \"\n  \"be reached (KLN:364, POK:482/483/484, POK:237 for gao-δi-, SYN:202, BQT:1723/1855/1856/1863, HRN:210/211/236/237, \"\n  \"SOD:180, SOG:57, SNS:262) says what he says it says; the problem is that some of those sources are now superseded.\"),\n \"note_fa\": (\n  \"ریشه، برچسب زبانی و معنی هر سه درست است: gʷou- «گاو» در پوکورنی (ص ۴۸۲–۴۸۳) و gʷou- در واتکینز/AHD همان چیزی است \"\n  \"که امروز *gʷṓws نوشته می‌شود؛ یکی از استوارترین اسم‌های بازسازی‌شدهٔ هندواروپایی که صرف کامل آن در هندوایرانی تقریباً دست‌نخورده مانده است. \"\n  \"دو نکته در این نمودار به همان استواری نیست. نخست شاخهٔ «سرگین» (گره‌های ۱۸ تا ۲۰): پوکورنی gʷōu-، gʷū- «سرگین» را مدخلی جداگانه (ص ۴۸۳–۴۸۵) می‌آورد \"\n  \"و آن را از «گاو» نمی‌گیرد؛ تنها مان این دو را یکی می‌داند. دوم، دو زیرشاخهٔ کامل اصلاً به این ریشه تعلق ندارند: \"\n  \"gaiθā- پارسی باستان «رمه» (گره‌های ۱۰ و ۱۱) بنا بر کنت و نیبرگ از *gʷeyh₃- «زیستن» است، همان ریشه‌ای که خود نورایی در صفحهٔ ۲۰۵ زیر Gwei آورده؛ \"\n  \"و زنجیرهٔ «نهفتن» (گره‌های ۶ تا ۹) بر بازسازی *ni-gōp- هرن (۱۸۹۳) استوار است که خود هرن تردید بارتولمه را دربارهٔ آن نقل می‌کند \"\n  \"و هنینگ (۱۹۳۳)، ابوالقاسمی (همان FFD:80 که در یادداشت کتاب آمده) و چونگ (۲۰۰۷) به‌جای آن *ni-su(m)b- می‌گذارند. \"\n  \"ارجاع‌های نورایی در این صفحه به‌طرز چشمگیری دقیق‌اند: هر مأخذی که در دسترس بود همان را می‌گوید که او نسبت داده است؛ اشکال آنجاست که برخی از آن مآخذ امروز کهنه شده‌اند.\"),\n \"sources\": [PIE, GAV],\n \"ref_check\": [\n  {\"ref\": \"KLN:364\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 vol. I p.364 s.v. 'cow' (leaf 202 of KLN_1966.txt, the numeral '364' printed in the column): 'cogn. with OIr. bo, W. buw, ‘cow’, L. bos, Gk. βοῦς (for *gwaus-), ‘ox’, Lett. guovs, ... OI. gauh, Avestic gaush, ‘ox, bull, cow’, Toch. A ko, ki, B keu, ‘cow’, Arm. kov'.\"},\n  {\"ref\": \"POK:483\", \"status\": \"supports\",\n   \"note\": \"Pokorny's lemma gʷou- 'cattle' is printed on pp. 482-483 (POK_full.txt block 'Page(s): 482-483'), so the page reference is right; note that p.483 is also where the separate 'dung' lemma gʷōu-, gʷū- begins.\"}],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. gʷou-\", \"stance\": \"supports\",\n   \"note\": \"'gʷou-. Ox, bull, cow. Nominative singular form *gʷéu-s. 1. Germanic *kōuz (> *kūz) in Old English cū ... 2. Latin bōs (stem bov-) ... 3. Greek bous ... 4. Sanskrit go-, gauh, cow ... [Pok. gʷou- 482.]'\"},\n  {\"src\": \"WLD\", \"where\": \"WP. I 696 f.\", \"stance\": \"supports\",\n   \"note\": \"Pokorny closes the entry 'References: WP. I 696 f., WH. I 112, 118, Trautmann 94, Schwyzer Gr. Gr. I 577, 708' — Walde-Pokorny I 696 f. is the parent article.\"},\n  {\"src\": \"IEC\", \"where\": \"s.v. gʷou-, gʷōus (IEC.txt lines 5199, 5322)\", \"stance\": \"supports\",\n   \"note\": \"Mann: 'gʷou-, element of many cpds. in sense of ‘cow, cattle, beast; dung; lump’ etc. See the following entries, and gʷōus for the simplex.'\"},\n  {\"src\": \"SYN\", \"where\": \"§3.20/§4.13 (p.202)\", \"stance\": \"supports\",\n   \"note\": \"Buck's tables give the IE 'cow' word across the branches and list 'Av. gav- (NPers. gušt)' under FLESH.\"},\n  {\"src\": \"ARY\", \"where\": \"Latin index, root گاو (scan pdf p.423)\", \"stance\": \"supports\",\n   \"note\": \"Aryanpur's root page for گاو lists GAUSH, GAO- (Avestan), GAV (Old Persian), GAW (Pahlavi), QUG/YOG (Ossetic), GA (Kurdish), GOK/GOX (Balochi), GHWA (Pashto), KO/KAU (Tocharian), GAUS, GO- (Sanskrit), with Pokorny as reference.\"}],\n \"nodes\": nodes,\n}\n\ndoc = {\n \"pdf_page\": 217,\n \"book_page\": 187,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-217.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk217.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-217.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 217"
}
```


### [2026-09-06T15:27:13.151Z] TOOL RESULT

```
ok 20
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 12, 'disputed': 5, 'transcription_suspect': 1, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'not_checked': 5, 'partial': 6, 'not_found': 1}
books consulted: {'supports': 36, 'partial': 10, 'contradicts': 8, 'silent': 4} | by book: {'BRT': 6, 'PHD': 6, 'NYB': 6, 'KLN': 6, 'POK': 5, 'IEC': 5, 'AHD': 4, 'CHEUNG': 4, 'SKT': 4, 'BQT': 2, 'WLD': 2, 'HRN': 2, 'SYN': 1, 'FFD': 1, 'KNT': 1, 'SOD': 1, 'SOG': 1, 'ARY': 1}
```


## [2026-09-06T15:27:39.008Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-217.json` written, `verify_check.py 217` reports 20/20 nodes and **0 PROBLEM lines**.

**Page 217 (book p.187), root Gwou — 1 non-redirect entry, 20 nodes** (3 redirects skipped)
- Root verdict: confirmed (PIE *gʷṓws; POK 482-483, KLN 364, AHD gʷou-)
- Nodes: 12 confirmed · 2 plausible · 5 disputed · 1 transcription_suspect

Disputed / flagged:
- **#6 gôp, gôh (Av./Skt "to protect")** — Skt. *gup-* is a genuine back-formation from *gopā́-*, but no Avestan root gaup-/gōp- exists (Bartholomae has only *gaoz-* "hide"), and "gōh" = Skt. *guh-* < PIE *gʰewgʰ-, a different root. Horn p.237 itself quotes Bartholomae's doubt.
- **#7 Av. ni-gôp** — unattested; it is Horn's 1893 reconstruction only.
- **#8 Pahl. nihuftan** — MP verb real, derivation wrong: MP present stem *nihumb-* points to *ni-su(m)b-; Henning 1933, Abolqasemi (FFD:80, the book's own dissenting note) and Cheung 2007 all agree.
- **#10 OP gaithâ "herd"** — Kent and Nyberg derive gaiθā- from *gʷeyh₃- "to live" (the root Nourai charts as Gwei, p.205), not from *gʷou-.
- **#20 goh / cŭd / tŭdeh** — گوه confirmed; کود is a "heap" word (MP kōδ : Skt. kūṭa- : Arm. koyt, and Henning's own SOG:57 treats it so), توده is from PIr *taw(H)táH < PIE *tewtéh₂ "people" — unrelated.
- **#12 Germanic "koŭs"** — transcription_suspect, `error_in: book`. The printed page really shows *koŭs*; AHD/Watkins reads *kōuz*. Extraction is faithful; page image copied to `data/verification/sources/refs/ocr/BOOK/217.png`.

Plausible: #17 (butter certain, buffalo only doubtfully from βοῦς) and #18 (Pokorny keeps gʷōu- "dung" as a *separate* lemma; only Mann unifies it with "cattle"; AHD has no dung root, so AHD:1520 = not_found).

No extraction errors found — the JSON matches the printed page throughout, including the odd-looking "ga 3" (= Av. gā, acc. pl.) and "gao-di" (= Av. gaoδi- "milk container", which Pokorny p.237 confirms).
