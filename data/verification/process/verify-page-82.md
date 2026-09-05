# Verification process log — verify-page-82


## [2026-09-05T06:10:22.882Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 82 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-82.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-82.json. Write /home/sfmqrb/git/rishe/data/verification/page-82.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 82` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:10:24.113Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:10:24.842Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:10:24.859Z] TOOL RESULT

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


## [2026-09-05T06:10:25.382Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-82.txt"
}
```


### [2026-09-05T06:10:25.400Z] TOOL RESULT

```
1	=== PDF page 82 (book page 52) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhag : to share out, to enjoy  (refs POK:107; IEC:61)  PART 2
4	#1 (parent #0) [Avestan] refs=HRN:39; AEF:224 | bâga : share, property, garden
5	#2 (parent #0) [Sogdian] refs=SOD:37,100 | bxš : to share out ; bğ : God
6	#3 (parent #0) [Sanskrit] refs=AHD; HJB:49; KLN:140 | bhağa : good fortune ; bhağavant-gita : sound of sublime ☞Gěi ; bhaga-dhara : holder of happiness, brave ☞Dher 1 | NOTE: "bhaga-dhara" may be from Persian "faghpoor" (HJB:49)
7	#4 (parent #0) [Indo-European] refs=IEC:61 | Bhag-los, Bhag-mos : enjoyment, feasting
8	  #5 (parent #1) [Persian] refs=HRN:39; AEF:224 | bâğ «باغ» : garden | NOTE: HUB:23 does not agree with this derivation.
9	  #6 (parent #3) [Mongolian] refs=HJB:49 | 
10	    #7 (parent #6) [Persian] refs=BQT; MON | bahâdor «بهادر» : hero
11	  #8 (parent #3) [English] refs=HJB; AID | Bhagavad-Gita ; bahadur
12	  #9 (parent #4) [Pahlavi] refs=MON:523 | bazm : feast
13	    #10 (parent #9) [Persian] refs=MON:523; IEC:61 | bazm «بزم» : feast | extra: بزم آرا
14	  #11 (parent #4) [Persian] refs=IEC:61; MON:489 | bazleh «بذله» : jest, joke | NOTE: MON derives this from Arabic
15	  #12 (parent #4) [Greek] refs=IEC:61 | phagein : to eat
16	    #13 (parent #12) [English] refs=AHD; IEC:62 | -phagos ; -phagy ; phagocyte ; phagomania ; phagophobia ; esophagus
17	--- entry 1 ---
18	ROOT [Indo-European] Bhâghu : elbow, arm  (refs POK:108)
19	#1 (parent #0) [Avestan] refs=POK:108; KLN:190 | bâzu, bâzâu : arm
20	  #2 (parent #1) [Persian] refs=BQT:220 | bâzŭ «بازو» : arm
21	#3 (parent #0) [Germanic] refs=AHD | boog : bow of a ship
22	  #4 (parent #3) [English] refs=None | bow : front section of a ship
23	--- entry 2 ---
24	ROOT Bhag-los -> redirect to Bhag
25	--- entry 3 ---
26	ROOT Bhag-mos -> redirect to Bhag
27	
```


## [2026-09-05T06:10:28.811Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-82.json",
 "description": "Read source JSON for page 82"
}
```


### [2026-09-05T06:10:28.851Z] TOOL RESULT

```
{
  "pdf_page": 82,
  "book_page": 52,
  "entries": [
    {
      "root": {
        "name": "Bhag",
        "lang": "Indo-European",
        "refs": "POK:107; IEC:61",
        "gloss": "to share out, to enjoy"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:39; AEF:224",
          "words": [
            {"translit": "bâga", "gloss": "share, property, garden", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:37,100",
          "words": [
            {"translit": "bxš", "gloss": "to share out", "script": null},
            {"translit": "bğ", "gloss": "God", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD; HJB:49; KLN:140",
          "words": [
            {"translit": "bhağa", "gloss": "good fortune", "script": null},
            {"translit": "bhağavant-gita", "gloss": "sound of sublime", "script": null, "see": ["Gěi"]},
            {"translit": "bhaga-dhara", "gloss": "holder of happiness, brave", "script": null, "see": ["Dher 1"]}
          ],
          "note": "\"bhaga-dhara\" may be from Persian \"faghpoor\" (HJB:49)",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "IEC:61",
          "words": [
            {"translit": "Bhag-los, Bhag-mos", "gloss": "enjoyment, feasting", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:39; AEF:224",
          "words": [
            {"translit": "bâğ", "gloss": "garden", "script": "باغ"}
          ],
          "note": "HUB:23 does not agree with this derivation.",
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "Mongolian",
          "refs": "HJB:49",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT; MON",
          "words": [
            {"translit": "bahâdor", "gloss": "hero", "script": "بهادر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 3,
          "lang": "English",
          "refs": "HJB; AID",
          "words": [
            {"translit": "Bhagavad-Gita", "gloss": null, "script": null},
            {"translit": "bahadur", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 4,
          "lang": "Pahlavi",
          "refs": "MON:523",
          "words": [
            {"translit": "bazm", "gloss": "feast", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:523; IEC:61",
          "words": [
            {"translit": "bazm", "gloss": "feast", "script": "بزم"}
          ],
          "script_extra": "بزم آرا",
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 4,
          "lang": "Persian",
          "refs": "IEC:61; MON:489",
          "words": [
            {"translit": "bazleh", "gloss": "jest, joke", "script": "بذله"}
          ],
          "note": "MON derives this from Arabic",
          "quote": null
        },
        {
          "id": 12,
          "parent": 4,
          "lang": "Greek",
          "refs": "IEC:61",
          "words": [
            {"translit": "phagein", "gloss": "to eat", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD; IEC:62",
          "words": [
            {"translit": "-phagos", "gloss": null, "script": null},
            {"translit": "-phagy", "gloss": null, "script": null},
            {"translit": "phagocyte", "gloss": null, "script": null},
            {"translit": "phagomania", "gloss": null, "script": null},
            {"translit": "phagophobia", "gloss": null, "script": null},
            {"translit": "esophagus", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bhâghu",
        "lang": "Indo-European",
        "refs": "POK:108",
        "gloss": "elbow, arm"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:108; KLN:190",
          "words": [
            {"translit": "bâzu, bâzâu", "gloss": "arm", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:220",
          "words": [
            {"translit": "bâzŭ", "gloss": "arm", "script": "بازو"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "boog", "gloss": "bow of a ship", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bow", "gloss": "front section of a ship", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Bhag-los", "redirect": "Bhag"},
      "nodes": []
    },
    {
      "root": {"name": "Bhag-mos", "redirect": "Bhag"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T06:10:29.765Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ && head -60 data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-05T06:10:29.812Z] TOOL RESULT

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
page-76.json
page-77.json
process
sources
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


## [2026-09-05T06:10:50.202Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '1,80p' data/verification/page-77.json",
 "description": "Look at prior verification file format"
}
```


### [2026-09-05T06:10:50.243Z] TOOL RESULT

```
{
  "pdf_page": 77,
  "book_page": 47,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Batiaxě",
      "verdict": "transcription_suspect",
      "modern_form": "Greek βατιάκη / βατιάκιον (batiákē) 'Persian drinking cup' (Athenaeus XI); beside it Old Persian *bātah 'wine' > MP bādag; the family is ultimately Akkadian baṭû 'bowl for liquids, wine jar' (< baṭium 'vessel, basin')",
      "note": "Horn's no. 155 (p. 36) is exactly Nourai's source: 'bādye \"Weingefäss\", vergl. bāde \"Wein\". ap. βατιάκη (φιάλη Athen. XI, 27) (de Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.).' Nourai's root box therefore reproduces Horn faithfully in substance — including the caveat, which he renders as 'The source of the Old Persian form is not clear' (Horn's 'unsicher'). Two things are nevertheless wrong with the box as printed. (1) The FORM: the word Horn cites is the Greek βατιάκη, i.e. batiākē with kappa; the book prints 'Batiaxě' with an x, which is not the attested form in any source (LSJ, Athenaeus, Ernout-Meillet, Wiktionary all have κ). Checked against the printed page (pdf p. 77, copy at data/verification/sources/refs/ocr/BOOK/77.png): the book itself prints 'Batiaxě', so this is Nourai's own misrendering, not a scan error. (2) The LANGUAGE LABEL: βατιάκη is a Greek word that Athenaeus reports as Persian; it is not an attested Old Persian form. The Old Persian antecedent modern sources reconstruct is *bātah 'wine' (whence MP bādag), and Latin batioca/batiola (Plautus, 2nd c. BCE) shows the cup-word already circulating in the Mediterranean. The ultimate source is Semitic (Akkadian baṭû), so 'the source of the Old Persian form is not clear' is over-cautious by 1999 standards rather than wrong.",
      "note_fa": "ریشهٔ این خانواده در کتاب «Batiaxě» و «پارسی باستان» خوانده شده است. آنچه هرن (ص ۳۶، شمارهٔ ۱۵۵) آورده در واقع واژهٔ یونانی βατιάκη (batiākē) «جام شراب پارسی» است که آتنایوس آن را پارسی می‌خواند؛ پس نه «x» درست است و نه دقیقاً «پارسی باستان». صورت ایرانی بازسازی‌شدهٔ امروزی *bātah در پارسی باستان است که در فارسی میانه bādag شده است، و خاستگاه نهایی این واژه اکدی baṭû «کاسه و خم شراب» دانسته می‌شود؛ لاتینی batioca نزد پلاؤتوس (سدهٔ دوم پ.م.) نشان می‌دهد که واژه از دیرباز در مدیترانه رواج داشته. تصویر صفحهٔ چاپی بررسی شد: خطا از خودِ کتاب است، نه از خوانش اسکن. جمله‌ای که نورایی افزوده («خاستگاه صورت پارسی باستان روشن نیست») همان «unsicher» هرن است.",
      "error_in": "book",
      "book_prints": "Batiaxě",
      "correct_form": "Batiākē (Gk. βατιάκη); the Old Iranian antecedent is OP *bātah",
      "sources": [
        "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87",
        "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9"
      ],
      "ref_check": [
        {"ref": "HRN:36", "status": "supports", "note": "Horn, Grundriss no. 155 (printed p. 36; HRN.txt line 1752, the OCR reads 'hädye *Weingefäss', vergl. bade 'Wein . ap. ßandarj' üsgaiiitj (ptdXrj Athen. XI, 27 (de Lagarde, Ges. Abh. 211), unsicher; phl. batak (PPGl.)' = 'bādye Weingefäss, vergl. bāde Wein. ap. βατιάκη (φιάλη Athen. XI, 27) …, unsicher; phl. batak'). The page carries the whole box: the Greek/'ap.' cup-word, the Pahlavi batak, the Persian bāde/bādye, and the caveat 'unsicher'."}
      ],
      "consulted": [
        {"src": "LAT", "where": "Ernout-Meillet s.v. batioca (LAT.txt line 7032)", "stance": "supports", "note": "'batioca, -ae f.: coupe à vin. Emprunt à une forme dialectale (Tarente, Héraclée) correspondant à ion.-att. βατιάκη. Un ex. de Pl. et un d'Arn. On trouve aussi batiola, de même sens (Pl. Colax frg. 1).' Attests the Greek form with κ and dates the cup-word to Plautus."},
        {"src": "KNT", "where": "Kent, Old Persian lexicon", "stance": "silent", "note": "grep 'batiak|batiac' in KNT.txt (and TLM.txt, SPG_keilinschriften1881.txt): no hits — the word is not in the attested Old Persian corpus, which is why 'Old Persian' can only mean 'reported as Persian by a Greek author'."},
        {"src": "BRT", "where": "Altiranisches Wörterbuch", "stance": "silent", "note": "no Avestan cognate of the cup-word; grep gave nothing."}
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Pahlavi",
          "words": "bâtak",
          "verdict": "confirmed",
          "derivation": "The Pahlavi word is written ⟨bʾtk'⟩ and read bādag 'wine, must'; Nourai's 'bâtak' is the older graphic transliteration (t for the Book-Pahlavi letter that stands for /d/ after a long vowel), the same form Horn quotes as 'phl. batak (PPGl.)' from the Pahlavi-Pazand glossaries. MacKenzie, Concise Pahlavi Dictionary p. 16 has 'bādag [bʾtk' | N bāda] wine, must', and his English index 'wine bādag, may'. The suffix is the Middle Persian -ag (< OIr. -aka-) added to the base *bāt-, so the chain root → MP bādag is the standard one; Khotanese bātaa 'wine, must' is the sister form.",
          "derivation_fa": "صورت پهلوی به خط کتابی ⟨bʾtk'⟩ نوشته می‌شود و bādag «می، شیرهٔ انگور» خوانده می‌شود؛ آنچه نورایی «bâtak» آورده، آوانگاری حرف‌به‌حرف کهن است (t در پهلوی پس از واکهٔ بلند برابر /d/ فارسی نو است) و همان صورتی است که هرن از واژه‌نامه‌های پهلوی نقل می‌کند. مکنزی در «فرهنگ کوچک پهلوی» ص ۱۶ آورده: bādag [bʾtk'] «می، شیره». پسوند ‑ag همان ‑aka- ایرانی باستان است. صورت خواستهٔ ختنی bātaa نیز هم‌ریشه است. ادعای نورایی در این گره درست است.",
          "sources": ["https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87"],
          "ref_check": [
            {"ref": "AEF:207", "status": "not_checked", "note": "Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi is not online (refs_online.json: 'catalogue/purchase only'); it is the Persian translation of Horn, so the equivalent passage is Horn no. 155, checked above, which does read 'phl. batak (PPGl.)'."}
          ],
          "consulted": [
            {"src": "PHD", "where": "MacKenzie p. 16 s.v. bādag (PHD.txt line 233); index 'wine' line 4315", "stance": "supports", "note": "'bādaģ [?{А! | N a] wine, must' (OCR of 'bādag [bʾtk' | N bāda]'); English index: 'wine badag, may.'"},
            {"src": "NYB", "where": "Nyberg, Manual of Pahlavi II (glossary)", "stance": "silent", "note": "grep 'bātak|bādag|bʾtk' gave no hit; Nyberg's glossary covers only the texts he edits, and 'wine' there is mad / has (line 1947)."},
            {"src": "HRN", "where": "no. 155, p. 36", "stance": "supports", "note": "'phl. batak (PPGl.)' — Horn takes the Pahlavi form from the Pahlavi-Pazand glossaries, exactly Nourai's arrow."}
          ]
        },
        {
          "id": 2,
          "lang": "Persian",
          "words": "bâdeh; bâdîyeh; pâtîleh",
          "verdict": "plausible",
          "derivation": "باده bāde 'wine' is the regular New Persian continuation of MP bādag: final -ag > -a/-e in New Persian (bandag > banda, bādag > bāde), so this word is confirmed. بادیه bādiye 'wine-bowl' is the same etymon but reached Persian by a detour: the Aramaic/Syriac bāṭīṯā and Arabic باطیة bāṭiya 'earthen wine vessel' (attested 7th c. CE, Sunan an-Nasāʾī) belong to the same Akkadian-based family, and Mo'in's own dictionary marks باطیه as '[ع. ← باطیة، ف. بادیه]', i.e. the Arabic shape of Persian بادیه — the doublet spelling باديه ( باطيه ) that the chart itself prints is the trace of this Arabic round trip. Nourai's arrow (straight from Pahlavi bātak) is therefore a simplification but not an error of family. پاتیله / پاتیل pātile 'large copper pot' is the weak link: Dehkhoda and Mo'in give only the meaning ('ظرف بزرگ مسین… پاتیله. تیان'; Mo'in 'دیگ بزرگ مسی'), with no etymology, and no source consulted connects it with bādag/bādiye; the p-/b- alternation Nourai relies on (as in piring/biring below) is possible but unattested here, so this word is unverified. The chart's own NOTE, that VFO:18 links these to English 'pot', has no support: 'pot' is Late Latin pottus / Old English pott of obscure origin, unrelated to the batiākē family, and VFO is not even in the project's reference key.",
          "derivation_fa": "«باده» دنبالهٔ منظم فارسی میانهٔ bādag است؛ پسوند ‑ag فارسی میانه در فارسی نو به ‑ه بدل شده (bandag > بنده، bādag > باده)، پس این واژه بی‌گمان درست است. «بادیه» به معنی «کاسهٔ می» از همین خانواده است اما از راهی دیگر رسیده: صورت آرامی/سریانی bāṭīṯā و عربی «باطیة» (گواه سدهٔ نخست هجری در سنن نسائی) هم‌ریشه‌اند و معین خودْ ذیل «باطیه» می‌نویسد «[ع. ← باطیة، ف. بادیه]»؛ یعنی همان دوگانهٔ «بادیه (باطیه)» که در نمودار آمده، نشانِ همین رفت‌وبرگشت از راه عربی است. اما «پاتیله/پاتیل» بندِ سست این گره است: دهخدا و معین تنها معنا («ظرف بزرگ مسین»، «دیگ بزرگ مسی») می‌دهند و هیچ ریشه‌شناسی نمی‌آورند و هیچ منبعی آن را به bādag نمی‌پیوندد؛ ابدال پ/ب که نورایی بر آن تکیه دارد ممکن است ولی در اینجا گواهی ندارد. یادداشتِ نمودار دربارهٔ پیوند این واژه‌ها با pot انگلیسی نیز پذیرفتنی نیست: pot از لاتینی متأخر pottus است و ربطی به این خانواده ندارد.",
          "sources": [
            "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%AF%D9%87",
            "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B7%D9%8A%D8%A9",
            "https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/"
          ],
          "ref_check": [
            {"ref": "AEF:207", "status": "not_checked", "note": "not online (see node 1); the German original Horn no. 155 (p. 36) carries the bāde/bādye pair — 'bādye Weingefäss, vergl. bāde Wein' — but has no پاتیله."}
          ],
          "consulted": [
            {"src": "BQT", "where": "Borhan-e Qate' vol. 1, s.v. باده (BQT_v1_pages.txt line 16477)", "stance": "supports", "note": "'باده _ بفتح [اول] … : شراب ، در پهلوی … (اونوال ۳۹۲) ، معرب آن باذق' — Mo'in's footnote gives the Pahlavi antecedent and the Arabicized form باذق, i.e. the same chain Nourai draws."},
            {"src": "MON", "where": "Farhang-e Farsi s.v. باده (MON_part1.txt line 20025) and s.v. باطیه (line 20671)", "stance": "partial", "note": "'باده: bāda (اِ.) نوشابه‌ای که مستی آورد' — no etymology; but s.v. باطیه: '[ع. ← باطیة، ف. بادیه] ظرف سفالینی که در آن شراب نگاه دارند' explicitly makes Arabic باطیة the counterpart of Persian بادیه. Mo'in's only بادیه headword (line 20048) is the unrelated Arabic بادیة 'desert'."},
            {"src": "PHD", "where": "MacKenzie p. 16 s.v. bādag", "stance": "supports", "note": "'bādag [bʾtk' | N bāda] wine, must' — MacKenzie himself gives New Persian bāda as the descendant."},
            {"src": "ARY", "where": "Aryanpur, Farhang-e rishe-ha", "stance": "silent", "note": "grep 'باده' in incoming/ARY/ARY_pages.txt: no hit (the book covers IE roots; a Semitic loan is out of its scope)."}
          ]
        }
      ]
    },
    {
      "entry": 1,
      "root": "Bazda",
      "verdict": "plausible",
      "modern_form": "Avestan bazda- 'afflicted, diseased' (past participle of ban- 'to afflict, make ill'), taken by Gharib as the source of Sogdian ʾβž 'bad, evil'",
      "note": "The form and the language label are right: Avestan bazda- is real, attested in the Nērangestān (N 56), and Bartholomae s.v. glosses it 'erkrankt, krank, siech' — the past participle of ban- 'to fall/make ill' (Cheung, root *ban 'to afflict, be afflicted', with Khotanese basdaa-). What is not Avestan is the GLOSS: 'bad, sin' is the Sogdian meaning, projected back onto the Avestan etymon. Nourai is however faithfully following his cited source: Gharib's Sogdian dictionary, entry 464 (printed p. 18), writes the etymology of ʾβj- as '© < Av. bazda'. So the root box is a correct transcript of a real scholarly proposal whose semantic step ('afflicted, sick' → 'bad, foul, sinful') is Gharib's, not something modern handbooks state independently; Cheung lists no Sogdian reflex under *ban. Hence 'plausible' rather than 'confirmed'.",
      "note_fa": "صورت و برچسب زبانی درست است: bazda- اوستایی واقعاً هست (نیرنگستان ۵۶) و بارتولومه آن را «erkrankt, krank, siech» (بیمار، رنجور) معنی می‌کند؛ اسم مفعولِ ban- «بیمار کردن، رنجاندن» است و چونگ نیز آن را زیر ریشهٔ *ban «رنجاندن» با ختنی basdaa- می‌آورد. آنچه اوستایی نیست، معناست: «بد، گناه» معنای سغدی است که به صورت اوستایی بازتابانده شده. با این همه نورایی امانت‌دار منبع خویش است: قریب در «فرهنگ سغدی»، مدخل ۴۶۴ (ص ۱۸ چاپی)، ریشه‌شناسی ʾβj- را چنین می‌نویسد: «< Av. bazda». پس این جعبهٔ ریشه نقلِ درستِ یک پیشنهاد علمی است که گام معناییِ آن («بیمار» ← «بد، پلید، گناه‌آلود») از آنِ قریب است و در فرهنگ‌های امروزی به‌صورت مستقل تأیید نشده؛ از این رو «با احتیاط پذیرفتنی».",
      "sources": [],
      "ref_check": [
        {"ref": "SOD:18", "status": "supports", "note": "Gharib, Sogdian Dictionary, entry 464 'ʾβj- M … ©<Av. bazda … bad, evil, pain' (SOD.txt line 10522). The page numerals in the OCR put entry 464 between the markers '18' (line 10448) and '19' (line 10596), so entry 464 stands on printed p. 18 — Nourai's SOD:18 is a page citation and it is exact."}
```


## [2026-09-05T06:10:52.047Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','HRN','AEF','SOD','AHD','HJB','KLN','BQT','MON','AID','HUB','ARY','PHD','NYB','BRT','WLD','SYN']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Print refs_online entries"
}
```


### [2026-09-05T06:10:53.795Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
```


## [2026-09-05T06:10:58.903Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==116' POK_01.txt | head -80\necho \"=====108=====\"\nawk 'BEGIN{RS=\"\\f\"} NR==117' POK_01.txt | head -60",
 "description": "Print Pokorny pages 107-108"
}
```


### [2026-09-05T06:11:00.509Z] TOOL RESULT

```
n',  w( von  ahd.  barij  PI.  banna  , Gebot  unter  Strafandrohung*  (nhd.  Bann,  Bawdi tcald),  ags.  gebann,  aisl.  bann  n.  »Verbot,  Bann*.
Toch.  A  pä-j  pä-g-  , betteln'  (Van  Windekens   Lexique  87  f.).
Nach  Kuiper  (AO.  XII  262)  hierher  (*bhd-s-)  ai.  bhisdkti  ,heilt',  bhiSdfi jArzt',  jav.  -bis-  , heilend*;    über   av.  bisazjät   vgl.  Kuiper  Nasalpräs.  44 fj
WP.  II  123 f.,  WH.  I  437  f.,  450,  458  f.,  525 f.,  Schwjzer  Gr.  Gr.  I  674r
bhabhä  und  anklingende  Worte  für  , Bohne*,  u.  zw.  , Saubohne',  vgl.  zuml Sachlichen  Hoops  Waldb.  350,  400  f.,  464  f.,  Helm  Kltpfl.«  221,  570,1 Schrader  RL.^  159  f.  |
Lat.  faba  (fäl.  haba)  , Bohne'  (dazu  die  PN  Fabius,  Fabidius  usw.  und die  Insel  Fabäria),  russ.  usw.  bob^,  apr.  babo  ds.  Wohl  redupliziertes Lallwort  und  als  , aufgeblasene  Schote,  Schwellung'  mit  gr.  g)a-KÖg  m. , Linse' :  alb.  bathe  f.  , Saubohne*  (*bhakä)  verwandt.  Auch  aisl.  baun,  ags. bean,  ahd.  bona  , Bohne'  (Baunonia  friesische  Insel  bei  Plinius)  sind  wohl durch  Dissimil.  von  *bab7iä  zu  *baunä  entstanden. WP.  II  131,  WH.  I  436.
bhMd'  .gut*.
Ai.  bhadrd-h  , erfreulich,  glücklich,  gut',  n.  , Glück,  Heil',  sii-bhadra-h ,herrlich' =  av.  hu-badra-  »glücklich';
got.  batiza  ,besser',  batista  , bester',  aisl.  betre,  betstr,  ags.  bet{e)ra,  betst, ahd.  bezzir(o),  bezzist,  nhd.  besser,  best]  dazu  das  Adv.  des  Kompar.  aisl. betr,  ags.  bet  (*batiz),  ahd.  baz  (*bataz,  erstarrtes  Neutr.  .Nutzen');  aisl. batim.  ,Verbesserung,  Heil*,  afries.  bata  m.  , Vorteil*,  mhd.  bazze  ds.;  got. gabatnan  ,Nutzen  erlangen*,  aisl.  batna  , besser  werden*,  ags.  batian,  ahd. bazzen  ds.;  mit  Ablaut  got.  böta  f.  ,Nutzen*,  aisl.  ags.  bot  , Besserung,  Er- satz*, ahd.  buoz(a)  f.  ,Besserung,  Buße'.
WP.  II  151  f..  Feist  83,  103,  174,  J.  Weisweiler  Buße  (1930).
107
hhaZ'  zuteilen;  als  Anteil  bestimmen  oder  (ursprüngl.  medial?)  als  An- '  teil,  als  Portion  erhalten'.
Ai  bhajati  , teilt  zu'  =  av,  bag-  (bazat)  ,als  Anteil  bestimmt  sein',  ai. hhaaa-h  ,Gut,  Glück*,  av.  baga-,  baya-  n.  , Anteil,  Los,  bes.  günstiges';  ai. bhaaa-h  , Zuteiler,  Herr,  Beiname  des  Savitar  und  eine
=====108=====
s  andern  Aditya'  = baya-  ,Herr,  Gott',  npers.  bay  ,Gott'  (formell  auch  =  gr. -ya/og) ;  ur- ind.  (Mitanni)  ON  Bagarriti  (=  Hhaga-rlti-  , Segensstrom'),  GN  Bagbartu (=  *bhaga-bhrt-  , Segenspenderin'),  kleinas.  VN  Bayadd(J^)ov£g  (=  ^bhaga- da-non-  , Reichtum  spendend'),  Kretschmer  KZ.  55^,  95,  Gl.  18,  232;  ai. hhaktd-m  , Mahlzeit*  =  av.  baxta-  Partiz.  ,als  Anteil  zugewiesen*,  n.  ,be- stimmter  Anteil,  Schicksalsbestimmung,  bes.  Mißgeschick*;  ai.  bhaksati o-onießt,  verzehrt^  =  av.  baxsaiti  ,hat  oder  gibt  Anteil',  Desid.  ai.  bhik-, Säte  ,erbittet';
phryg.  Bayalog'  Zevg  0Qvyiog  Hes.  (vielleicht  iranischen  Ursprungs); oder  ob  zu  gr.  q)r]y6g  , Eiche'?     S.  unter  bhägö-s]
OT.  (paysTy  , essen*,  aizo-qtdyog  , Getreide  essend',  usw.;  wegen  gr.  cpayo- yeg'  aiayöreg,  yväd-OL  ;Hes.  vielleicht  hierher  (Much  Zfdt  Wtf.  2,  283)  as. Ucinni-)  bako,  nhd.  Backe]
slav.  *bog^  , Anteil'  in  aksl.  ubog-b,  nebog^  ,arm',  bogah  , reich*,  aksl.  bog^ ,Gott'  (urverw.  oder  iran.  Lw.);  GN  Dazdi-bog^  , Reichtum  spendend';
toch.  A  jpäkj  B  pake  ,Teil*,  A  pagim  , Schatz*.
WP.  II  127  f.,  W.  Schulze  KZ.  60,  138  =  Kl.  Sehr.  469.
2»  hhag'  , scharf,  auch  vom  Geschmack'??
Kret.  cpdygog  , Wetzstein,   dxövr]^,   q)0^6g  ,spitzköpfig'   (aus    '^q)a^6g  nach Xo^og  , schief  ?)    wird   von    Liden  Arm. -St.  57  ff.  mit  arm.  bark  (könnte  = (pdyqog  sein)  ,herb,  bitter,  scharf  von  Geschmack;  heftig,  zornig*  verglichen, doch  kann  bark  auch  zu  idg.  *bhorguo-s  gehören. WP.  II   128.
bhägö-s  f.  ,Buche*.
Gr.  q)rjy6gy  dor.  g)ay6g  f.  ,Eiche*  (vgl.  Specht  KZ.  66,  59);  lat.  fdgus  f. ,Buche*;  gall.  bägos  in  ON  J5ä^äco?i,  Bägono-]  ahd.  buohha  , Buche*  (bököh-y vgl.  Silva  Bäcenis  ,Harz*  bei  Caesar  und  mlat.  Böcönia  ,Rhön'),  aisl.  bök  f., ags.  böc,  bece  (bökjön-),  dazu  got.  böka  f.  ,Buchstabe',  aisl.  bök,  ags.  5öc, ahd.  buoh  f.  n.  ,Buch*,  ahd.  buohstap  , Buchstabe',  eigentlich  , Buchenstab zum  Einritzen*.
Nisl.  beyki  n. , Buchenwald*  ist  (wegen  bceki  ds.)  Schreib  Variante  von  *b0kij einem  späten  Kollektivum  zu  bök]  ebenso  ist  vielleLcht  nisl.  beykir  , Küfer* zu  erklären.  Unklar  ist  mir  aisl.  budkr,  baudkr  , Medizinkasten',  das  nach Cleasby-Vigfusson  85b  ein  Lw.  aus   mlat.
```


## [2026-09-05T06:11:07.732Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bh.gh.-\\?s.*Ellenbogen\\|Ellenbogen\" POK_01.txt | head -20\necho \"-----\"\nawk 'BEGIN{RS=\"\\f\"} NR==117' POK_01.txt | tail -25\necho \"=====leaf118=====\"\nawk 'BEGIN{RS=\"\\f\"} NR==118' POK_01.txt | head -40",
 "description": "Find Pokorny bhaghu- elbow"
}
```


### [2026-09-05T06:11:09.589Z] TOOL RESULT

```
623:gr.  dyy.(bv  ^Bug,  Ellenbogen^  (D.Pl.  dymoi  zu  dyAri  =  dyy.dlri),  iTt-rjy^isv-Ldsg .die  an  den  dyKÖvsg  (Rippen?)  des  Schiffes  befestigten  Bohlen^  (Döderlein, Bechtel   Lexil.   129),   IcyytOLva   ,alles   Gekrümmte^,   UyY.iorQOv  .Angelhaken';
786:Ai.  irmd-h  ,Arm,  Vorderbug'  (ursprüngl.  ,Achselgelenk',  vgl.  Ixq&qov, lat.  artus)  =  av.  ardma-  ,Arm',  osset.  arm  ,hohle  Hand',  älm-ärin,  ärm-äiin , Ellenbogen',  lat,  armus  .der  oberste  Teil  des  Oberarms,  Schulterblatt,  bei Tieren  der  Vorderbug'  (aus  *ar(d)mos),  gall.  aramö  , Gabelung',  *aramones ,Scherenarme  der  Deichsel'  (Wartburg  I  119,  Jud  bei  Howald-Mejer  Rom. Schweiz  374ff.),  apr.  irmo  f.  ,Arm',  lit.  irmede  (,Armfraß',  d.  i.:)  , Gicht  in den  Gelenken',  irm-liga  , Gicht'  (s.  Trautmann  Apr.  347);  hochstufig  lit. zem.  PL  tant.  armai  ,Vorderarm  am  Wagen'  (ibd.),  aksl.  ramo,  rame, serb.  räme  ,Schulter',  got.  arms,  ahd.  usw.  arm  ,Arm',  arm.  armukii  ,Ellen- bogen'  (Hübschmann  Arm.  Stud.  I  21).
3500:bsl.  *dilbö  .grabe  ein.  höhle  aus':  in  lit.  delba  und  dälba  f.  .Brech- stange', lett.  düba  f..  dilbis  m.  .Röhrenknochen.  Schienbein',  delbs  .Ober- arm. Ellenbogen',  dalbs  m..  dalba  f.  .Fischerstange.  Heugabel';  vielleicht lit.  nu-dilbinti  .die  Augen  niederschlagen';  *
4494:I.  el;  elei-y  lei-  , biegen';  olinä  , Ellenbogen*.
4495:A.  Hierher  stellen  sich  zunächst  Bezeichnungen  für  , Ellenbogen'  und ,Elle':
4496:Gr.  wXsvT]  , Ellenbogen',  wA-^v,  -svog  ds.;  (hXeyigavov  (aus  d)Xevo-y.Qavov durch  Ferndissimilation,  vgl.  Brugmann  Ber.  d.  sächs.  Ges.  d.  W.  1901, 31  ff.)  , Ellenbogenkopf';  (hllov  tt^v  tov  ßgccxlovog  xa/fTn^v  Hes.;
4497:lat.  ulna  (aus  *olina)  , Ellenbogenknochen,  der  ganze  Arm*;
4498:air.  uilenn  , Winkel',  mir.  uillind  , Ellenbogen,  Winkel*  {-II-  aus  -In-  der synkopierten  Kasus,  vgl.  Pedersen  KG.  II  59),  cymr.  eliiij  acorn.  elin, Hret.  Hin  , Ellenbogen'  {*olina)]
4503:einfache  Wurzel  *üU-  in  ai.  aratni-Tj.  m.  ^Ellenbogen',  av.  arddna-  ds.  yVg rä^ni-  ,Elle',  apers.  arasnis  ds. ;
4504:in  alb.  ZeVe  geg.  laus  ,Arm  vom  Ellenbogen  bis  zur  Hand'  {*len^. doch  vgl.  Pedersen  KZ.  33,  544)  fehlt  der  anlaut.  Vokal.  *
4512:1.  In   Bezeichnungen    für   Ellenbogen,  Arm,   gelegentlich   auch   andere^ Körperteile:
4516:apr.  woaltis,  icoltis  ^EÜe,  Unterarm^  {*ölkt-)]  lit.  alküne,  elküne  f.,  apri^ alkunis  , Ellenbogen^,  lett.  Uks  n.  elkuons  ds.,  abg.  lak^thJ  russ.  lökotb  ,Elle', {^olk^-th)]  russ.  dial.  ahiiik(?)  ,talus^
-----
s  andern  Aditya'  = baya-  ,Herr,  Gott',  npers.  bay  ,Gott'  (formell  auch  =  gr. -ya/og) ;  ur- ind.  (Mitanni)  ON  Bagarriti  (=  Hhaga-rlti-  , Segensstrom'),  GN  Bagbartu (=  *bhaga-bhrt-  , Segenspenderin'),  kleinas.  VN  Bayadd(J^)ov£g  (=  ^bhaga- da-non-  , Reichtum  spendend'),  Kretschmer  KZ.  55^,  95,  Gl.  18,  232;  ai. hhaktd-m  , Mahlzeit*  =  av.  baxta-  Partiz.  ,als  Anteil  zugewiesen*,  n.  ,be- stimmter  Anteil,  Schicksalsbestimmung,  bes.  Mißgeschick*;  ai.  bhaksati o-onießt,  verzehrt^  =  av.  baxsaiti  ,hat  oder  gibt  Anteil',  Desid.  ai.  bhik-, Säte  ,erbittet';
phryg.  Bayalog'  Zevg  0Qvyiog  Hes.  (vielleicht  iranischen  Ursprungs); oder  ob  zu  gr.  q)r]y6g  , Eiche'?     S.  unter  bhägö-s]
OT.  (paysTy  , essen*,  aizo-qtdyog  , Getreide  essend',  usw.;  wegen  gr.  cpayo- yeg'  aiayöreg,  yväd-OL  ;Hes.  vielleicht  hierher  (Much  Zfdt  Wtf.  2,  283)  as. Ucinni-)  bako,  nhd.  Backe]
slav.  *bog^  , Anteil'  in  aksl.  ubog-b,  nebog^  ,arm',  bogah  , reich*,  aksl.  bog^ ,Gott'  (urverw.  oder  iran.  Lw.);  GN  Dazdi-bog^  , Reichtum  spendend';
toch.  A  jpäkj  B  pake  ,Teil*,  A  pagim  , Schatz*.
WP.  II  127  f.,  W.  Schulze  KZ.  60,  138  =  Kl.  Sehr.  469.
2»  hhag'  , scharf,  auch  vom  Geschmack'??
Kret.  cpdygog  , Wetzstein,   dxövr]^,   q)0^6g  ,spitzköpfig'   (aus    '^q)a^6g  nach Xo^og  , schief  ?)    wird   von    Liden  Arm. -St.  57  ff.  mit  arm.  bark  (könnte  = (pdyqog  sein)  ,herb,  bitter,  scharf  von  Geschmack;  heftig,  zornig*  verglichen, doch  kann  bark  auch  zu  idg.  *bhorguo-s  gehören. WP.  II   128.
bhägö-s  f.  ,Buche*.
Gr.  q)rjy6gy  dor.  g)ay6g  f.  ,Eiche*  (vgl.  Specht  KZ.  66,  59);  lat.  fdgus  f. ,Buche*;  gall.  bägos  in  ON  J5ä^äco?i,  Bägono-]  ahd.  buohha  , Buche*  (bököh-y vgl.  Silva  Bäcenis  ,Harz*  bei  Caesar  und  mlat.  Böcönia  ,Rhön'),  aisl.  bök  f., ags.  böc,  bece  (bökjön-),  dazu  got.  böka  f.  ,Buchstabe',  aisl.  bök,  ags.  5öc, ahd.  buoh  f.  n.  ,Buch*,  ahd.  buohstap  , Buchstabe',  eigentlich  , Buchenstab zum  Einritzen*.
Nisl.  beyki  n. , Buchenwald*  ist  (wegen  bceki  ds.)  Schreib  Variante  von  *b0kij einem  späten  Kollektivum  zu  bök]  ebenso  ist  vielleLcht  nisl.  beykir  , Küfer* zu  erklären.  Unklar  ist  mir  aisl.  budkr,  baudkr  , Medizinkasten',  das  nach Cleasby-Vigfusson  85b  ein  Lw.  aus   mlat. 
=====leaf118=====
 apotheka  , Behälter*  sein  soll?
108  •
Slav.  Huza-  :  H^z^-  .Holunder^  in  russ.  buz  m.  :  slov.  bez,  russ.  dial.  Jo^ bleiben  wohl  fern;  ebenso  kurd.  büz  ,eine  Art  Ulme^  das  auf  älteres  vik (aus  idg.  *uigös)  zurückgeht.  Mhd.  büche^  biuche  ^Lauge^  biuchen,  buchen ,m  Lauge  kochen  oder  waschen'  gehört  eher  zur  Wz.  bheug{h)-  .reinigen,
fegend
Ein  idg.  Nebeneinander  von  bhäug-  (:  bhdvg-  :  bhug-)  und  bhäg-  ist  äußerst unwahrscheinlich;  vgl.  W.  Schulze  KZ.  27,  428  =  Kl.  Sehr.  55.
Vielleicht  nach  E.  Leumann  (KZ.  bl,  190)  zu  av.  baga-  .Anteil,  Los^, also  , Losbaum',  da  in  dessen  Reiser  Zeichen  eingeritzt  wurden.
WP.  II  128  f..  WH.  I  445  f..  863  f..  E.  Passler  in  ,Frühgesch.  u.  Sprachw.' (Wien  1948).
bhMgh-  .Schlamm.  Sumpf,  s.  bhogh-.
bhäghü'S  .Ellbogen  und  Unterarm'.
Ai.  bähü-h  m.  .Arm.  bes.  Unterarm;  bei  Tieren  Vorderfuß',  av.  bäzävrl .Arm'.  Gen.  bäzvö  (arm.  bazuk  aus  dem  Iran.);
gr.  nrjXVQj  äol.-dor.  nä^vg  .Ellbogen.  Unterarm',  aisl.  bögr,  Akk.  PL  bögii^ .Arm.  Schulter',  ags.  bog  .Schulter.  Arm;  Zweig',  ahd.  buog  (nhd.  Bugl .Schulter.  Hüfte.  Bug  des  Tieres';
toch.  A  B  ipoke,  B  pauke  .Arm'.
WP.  II  130.
hhar-  :  bhor-  :  bhr-  .Hervorstehendes.  Borste.  Spitze.  Borstenähre.  Grannen- korn'.
Mit  vokal.  Formantien:
got.  batra-bagms  .Maulbeerbaum',  engl,  black  bear-berry  .uva  ursi'.  norw. bjerneber  .rubus  caesius'  sind  nach  dem  Bärennamen  umgedeutetes  *bara^^ .Strauch'  =  .Dornstrauch';
aus    urslav.  '^b^r^  [*bhor-)    stammen   russ.  dial.  bor^,  klr.  bor.   Gen.  brti .Art  Hirse',  skr.  bar  ds.
Weitergebildet  mit  g  sind:
air.  bairgen   f.   .Brot'    (^barigenä    oder    *barigona)y    cymr.  usw.  bara  m.  3 ds.  (*barag-j  vgl.  lat.  farrägö  .Mengfutter').
Mit  Formans  -ko-:
mir.  bare  ^Speerschaft'.  cymr.  barch  f.  .Speer',  slav.  bhrk^  in  skr.  brk .Spitze.  Keim.  Schnurrbart',  cech.  bi-k  .Kiel.  Schwungfeder',  auch  wohl russ.  berce,  berco  .Schienbein',  dial.  .Pfahl'   (Berneker  119).
Vielleicht  hierher  (mit  Konsonantenverschärfung)  Hrokko-  .Dachs',  mir. brocc,  cymr.  mbr.  broch  ds..  falls  ursprüngl.  .spitzschnauzig.  spitzig'  zu lat.    (kelt.)   broccus   .mit   hervorstehenden   Zähnen',   gall.  *broc
```


## [2026-09-05T06:11:21.891Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bhagl\\|bhagm\\|bhāgl\\|bhāgm\" IEC.txt | head -20\necho \"---bhag entries---\"\ngrep -n \"^bhag\\|bhagō\\|bhago\" IEC.txt | head -30",
 "description": "Grep Mann IEC for bhag-los/bhag-mos"
}
```


### [2026-09-05T06:11:21.954Z] TOOL RESULT

```
1069:61 bhaglos — bhaksó, ið
1071:bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia “feast”
---bhag entries---
1062:bhag-, bhāg- ‘enjoy; enjoyment’. WP II, 127 (à) Skt. bhajami “award; experience; enjoy; possess; bhagah “possession, luck’; bhágah “lord of the gods’; Av. bagom ‘share’, bayo ‘god’; Iran. LW in Arm. bag (i-st. share);
1067:bhagh- (bhaghino-) (?) ‘mud, marsh’ OLat. cf. fa-mix (Fest.: ‘marsh’, fr. *bhagh- + *mig-?) beside faedus, foedus (“filthy”, fr. *bhaghido-?); Walloon fagne *peat-moor' be- side Fr. fange, It. fango ‘mud’; Cz. bahno, Pol. bagno “mud? beside Cz. baZina ‘marsh’
1071:bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia “feast”
1075:bhaghulos, see bhaghus Skt. bahuláh, bahaláh ‘dense, abundant’; Gk. pakhulós *thickish"
1076:bhaghus ‘dense, thick, plentiful’. WP II, 151. Skt. bahüh; Beluchi baz ‘dense’; Kurd. bez ‘fat; Arm. cf. bazum (inflected Iran. LW? ‘much, many); Myc. & Gk. pakhús; cf. phák- elos (cpd. *bundle); Li. cf. bázmas ‘mass, crowd'.
```


## [2026-09-05T06:11:24.299Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1060,1090p' IEC.txt",
 "description": "Print Mann IEC around bhag"
}
```


### [2026-09-05T06:11:24.362Z] TOOL RESULT

```
35
40
bhag-, bhāg- ‘enjoy; enjoyment’. WP II, 127 (à) Skt. bhajami “award; experience; enjoy; possess; bhagah “possession, luck’; bhágah “lord of the gods’; Av. bagom ‘share’, bayo ‘god’; Iran. LW in Arm. bag (i-st. share);
. Phryg. cf. bagaios ‘Zeus’; Gk. éphagon (aor.
İsg. ʻate’; -phagos (cpds.; LW in Arm. bagin, bagni, -av ‘idol’ is apparently isophonic with Lat. faenum (‘usury’, fr. *bhaginom?); OCS (and comm. SL.) bogü “god”, beside bog-atü ‘rich’; Cz. also ne-bohý, u-bohy ‘poor’; Srb. cf. z-bog, adverb "Tor the sake of: Latv. na- bags ‘poor’. Cf. -baig- in Olr. su-baig-idir (3s. dep. ‘he rejoices’). See next, and cf. bhag-
bhāg- (1) (variant of bhag-, q.v.). WP II, 127 Skt. bhagáh (Cshare'. Vedic: luck); Av. baya ‘part’; OPer. bàji- ‘tribute’; Per. bat id.; Tokh. A pàk, B pàke “part'; Olr. bág “sake, benefit’; MIr. bá (loss of -g as in brí, tí, rí); Slovene, cf. božati (“fondle”, from bhag-, q. v.); Ukr. po-baZzaty ‘felicitate’; baZaty, bahnuty ‘desire’; Cz. baZziti ‘crave’, na-ba£Ziti ‘satisfy’. Cf. Skt. bhajitah "shared
bhāg- (2) “strike, struggle’ Oss. ?cf. bogal ((champion'; prob. fr. Turko- Mongolian boy-gal *ox-bull, accdg. to Abaev) (IE* a normally: Oss. a); MIr. bágh “battle, fight , exploit’; Du. beuken “flog”; Li. boginti ‘tug, heave, struggle?
bhagh- (bhaghino-) (?) ‘mud, marsh’ OLat. cf. fa-mix (Fest.: ‘marsh’, fr. *bhagh- + *mig-?) beside faedus, foedus (“filthy”, fr. *bhaghido-?); Walloon fagne *peat-moor' be- side Fr. fange, It. fango ‘mud’; Cz. bahno, Pol. bagno “mud? beside Cz. baZina ‘marsh’
bhaéinos "of a mast-bearing tree’. See bha- ĝos Gk. phéginos; Lat. Genus: MHG buochin, büechīn “beechen?
61 bhaglos — bhaksó, ið
bhaélos (?) ‘enjoyment’. (Variant of bhag- (1), q. v.). See next Per. bazla jesť’; Gk. phágilos “eatable?
bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia “feast”
bhaào, ið (?) “force, thrust, rant Olr. bágaim ‘boast, assert, vow’; Du. (ambig.) beuken ‘flog’. cf. bhag- (2)); Latv. bāžu, bāzt, and bazit (*thrust, bung’, refl. ‘obtrude one- self)
bhāĝos (1) ‘beech-mast, acorn; mast-bear- ing tree, beech, oak’. WP II, 128 Gk. phégós (Dor. -à-) ‘beech, oak’; Lat. fagus; MHG buoche; Du. beuk; OE bëce; ON bók ‘beech’. Cf. W. baedd, Cor. bath (“boar”, fr. *bhag-ed- *mast-eater")
bhà$os (2) “part, share’. Variant of bhag- (1), q.v. WP II, 128 Skt. bhaj; OPer. baji-; Per. ba: Tokh. pak, pake; MIr. cf. dím-bág ‘sorrow’, air-bág ‘glory’
bhaghulos, see bhaghus Skt. bahuláh, bahaláh ‘dense, abundant’; Gk. pakhulós *thickish"
bhaghus ‘dense, thick, plentiful’. WP II, 151. Skt. bahüh; Beluchi baz ‘dense’; Kurd. bez ‘fat; Arm. cf. bazum (inflected Iran. LW? ‘much, many); Myc. & Gk. pakhús; cf. phák- elos (cpd. *bundle); Li. cf. bázmas ‘mass, crowd'.
bhāĝhus “arm, forearm, upper arm, shoul- der". WP II, 130 Skt. bahüh; Av. bazus; Arm. dim. bazuk ‘forearm’; Oss. dim. bazug, bazig 'shoulder- blade’; Tokh. A poke, B pauke am": OHG buoc, buac, -ges ‘bend’; MHG buoc, -ges ‘upper arm’; OE bog “arm, shoulder, bough’; ON bógr; Du. cf. dim. beugel ‘ring’
bhai-, bhəi- (bhai-, bhəi) (fem. element, perh. aphetic, of ambhō, q. v.) MHG cf. bei-de (and comm. W Gmc.); Sw. begga; OCS o-bě (and comm. Sl.)
bháio, bhami ‘utter, declare, make plain, make bright'. WP II, 122 Skt. bhami; Tokh. pà-; OArm. bam, bas, baj (1, 2, 3s. ‘say’, to introduce indirect speech); Gk. pháo, ph&mí “speak? beside di-pháo, cpd. *discover'; Lat. for, fari; OE bogian, boian
10
20
25
30
35
40
45
62
‘boast’; OCz. baju, báti ‘tell; cf. also Cz. bájet “tell? R bàjat “say, speak’; Li. (?) boju, boti ‘notice, watch, heed?
bhaius (?) “brother” Hindi bhài; Blg. baj, baje, pl. bajeve “elder brother
bhak-, bhakolos ‘compact; lump’. Cf. bhakos, bhaK-, bhaks- Gk. cf. óm-phax, -phakos “bunch of sour grapes’, phákelos ‘bunch’; Alb. bake *pot- belly’, bákull ‘tubby’; Lat. (fr. Celt.?) bacci- num: basin (see Dauzat: bassin); Ir. baicle, baclach ‘crowd’; Br. bagol ‘hale, hearty’; W cf. bagad “cluster, crowd", bagwy ‘clump’; Srb. cf. bokast ‘humped’?
```


## [2026-09-05T06:11:40.489Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1090,1110p' IEC.txt",
 "description": "Print IEC page 62 content"
}
```


### [2026-09-05T06:11:40.550Z] TOOL RESULT

```
bhak-, bhakolos ‘compact; lump’. Cf. bhakos, bhaK-, bhaks- Gk. cf. óm-phax, -phakos “bunch of sour grapes’, phákelos ‘bunch’; Alb. bake *pot- belly’, bákull ‘tubby’; Lat. (fr. Celt.?) bacci- num: basin (see Dauzat: bassin); Ir. baicle, baclach ‘crowd’; Br. bagol ‘hale, hearty’; W cf. bagad “cluster, crowd", bagwy ‘clump’; Srb. cf. bokast ‘humped’?
bhakor (bhakk-) (?) Gaulish baccar “hazelwort'; Srb. bokor ‘shrub, bunch’
bhakos (bhokos?) ‘side, flank’ Arm. bak (‘limb’. Semantics of Go. fera ‘side; limb); OCS bokü (and comm. SI.) ‘flank’; cf. Srb. bokonj ‘side of ship’
bhaks- “swelling; bundle, bunch'. Cf. bhak- Lat. fascis; W baich ‘load’; Br. beach, id.; cf. Gallo-Lat. bacco E baccinum (fberry; pot, basin); LG cf. baksig ‘mighty’. (Cz. boch ‘ham’, bochen ‘loaf’, Pol. bochen "large loaf, lump of iron’, and Cz. bošec ‘rump of goose’ probably belong here, but Cz. boch has been influenced by MHG bache ‘ham, flitch’))
bhakso, io (bhask-) (1) ‘strike dumb; be dumbstruck. Arm. baxuk ‘mad’; Gk. (fr. Thrac. or Maced.) baskaíno ‘charm’: Gk. phaskaíno, id. beside báskanos ‘malicious; sorcerer’; Lat. fascinum ‘charm’; Alb. cf. beh ‘surprise’; MIr. cf. bas- call, baisceall “mad; lunatic; Sw. baksna ‘surprise’; Slovene (?) bo&iti ‘gape, stare’ (infl. by Tk. bos ‘empty’)
bhakso, io (2) “beat, ram, thrust Arm. baxem (redup. babaxem) (fbeat'. But a form bayxem also occurs, fr. *bhalks-?); LG baxen “beat down, ram; box’ (origin of E bash & box uncertain); Li. baksu, e ‘pierce’: Skt. bhaksami “sting”
bhaksó, ið (3) (bhask-) “bawl, bark? (Gk. phásko “say, assert though isophonic, is a form of bha-, see bhaio, bhàmi). Du.
63 bhakos, à — bhand- 64
bassen ‘bark’; Li. băkšyti ‘scold’. A parallel form occurs in Skt. bhasami “bark; scold’
bhakos, å ‘leguminous seed, bean, lentil’. WP II, 131 Av. cf. baxto ‘leguminous’; Gk. phakós ‘lentil’, a-pháke ‘vetch’ beside pháselos, phasiolos (*-Ki-) ‘bean’; Alb. bathé “broad bean’
bhal- (1) “white, pale; white-spotted; pallor, blaze on forehead" ` Skt. bhalah (epithet of sun), bharuh ‘gold’; Arm. bal (i-st. *pallor) Gk. Phalís ‘priestess of Juno', phálos *white, bright'; phálios, id.; Gk. (fr. Phryg. bálios ‘eyeless’; Alb. bal (^white-haired; blazed animal); Gaul. balio- (‘white blaze > Fr: baille, id.); Dacian sub- strate in Rum. bál ‘white blaze’; Br. bai" id. (and “white blazed', adj.): W bal, adj. id. be- side bali ‘blaze’; Go. bala- epithet of horse, LW in LLat. bala, gs balanis ‘white horse’; EME ball ‘white blazed; blaze on animal; Blg. bol ‘smallpox, pockmark’; Li. balas ‘snowdrop’, balai, pl. ʻanemone’; balù, bálti “turn pale’; Latv. bāls (tonal *-a- or long *-a-) ‘pale’. See bhal-. Cf. further Li. bálnas *whit- ish, of cattle’
bhal- (2) ‘forehead; prominence’. WP II, 175 Skt. cf. (a)bhalam (1) ‘forehead’; Gk. cf. pháios ‘forepiece on helmet? a component also of phál-agx ‘wedge-shaped frontal formation’, phalaris ‘coot; Alb. ballë ‘forehead, front of a formation’; Lat. fala *battering-ram', beside in-fula ‘headgear, garland on animal fore- head; W bâl, pl. baloedd (*bhalos, -es-) ‘peak, prominence’; ON bali 'grass-bank' ; OPr. ballo ‘forehead’. Cf. also the Gk. cpd. phal- akrós ‘bald’. Cf. bhàal- (2). The form re- presented in Lat. balaena seems to represent a non-Greek form of phálaina (‘whale’, lit. ‘hostile forehead’, cf. nuino- ‘hostile’ in Gk. ainós: Olr. anfine, s. ‘enemy’: OE unwine, id.). For OHG belihha ‘coot’, see FK: Belche
bhal- (1) (variant of bhal- (1), q.v. Skt. bhàlam 'spendour'; Latv. bāls ‘pale, light"; Li. cf. boluoti ‘shimmer’; Icel. bóla ‘foom up’?
bhāl- (2) ‘ump, boss, ball’. Cf. bhal- (2). WP II, 175 Skt. bhālam ((1) ‘forehead’ here, or to bhal- Ou: Oss. bal, Dig. bali (“sour cherry’. LW in
10
20
25
30
35
40
45
```


## [2026-09-05T06:11:50.984Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==61' HRN.txt | head -60",
 "description": "Print Horn page 39"
}
```


## [2026-09-05T06:11:52.030Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bāġ\\|bag \\|bāg\\b\\|Garten\" HUB.txt | head -40",
 "description": "Grep Hübschmann for bag/Garten"
}
```


### [2026-09-05T06:11:52.826Z] TOOL RESULT

```
- ^^9 —
aw. uhdaena- 'gewebt*; skr. vergl. ürna^vdbhi^
'Spinne* ^).
aty. üdal, ödal 'weben ; oss. vafpi (75) ; bei. gvapag,
n. ^vafay (134); wa;^. vufam, sar. väfam.
Arische (bezw. indogermanische) Doppelformen vaph-
und vahh-, vergl. Bartholomae, ZDMG. 44, 552,
Hübschmann, ib. 557.
' 169. bäy *6arten*.
Wohl aw. bäga- Xoos' (y. 51, 1); ai. hhägd- 'Teil,
Eigentum*; phlv. häg (PPGl.).
de Lagarde's Bemerkung bezüglich Nathans aus
Rom (Semitica I, 52) vermag ich nicht zu kontroliren.
170. häk 'Furcht*.
ar. '^bhäyaka-, von V^hhay' 'erschrecken, sich fürchten'
(aw. Jay-, ai. hhay-),
171. hälä *hoch\
aw. haresiah' 'Höhe'; phlv. bälä^ baldig bal(i)st (aw.
harezista-, z. B. vd. 2 (75)).
bei. baläd, n. bäläd 'Höhe ; empor, auf* (81) ; kurd.
LW. bälä. /
172. bäliS, bälist 'Kissen, bälfn,
g. bälist; Kä§. böUsm, böliSt
aw. barezis' 'Decke, Matte*; phlv. bäl(i)sn (bälln be-
deutet im Phlv. nur 'Höhe, Gipfel', es steht für
aw. bareSnU'j; ai. barhis- 'Opferstreu'; arm. barj
ngooxfcpdXaiop (H. No. 53).
LW. kurd. bäliät, bälisne^ böl%w^ bälge (H.-Sch.);
oss. t. baz 'Kissen* (50); wa/. baleß^ sar. baldjc.
173. hallden 'wachsen, zunehmen* (Sahn. I, S. 3 Vers 49),
bäliä 'Wachstum*-'); vergl. guvöllden (No. 939).
*) Die indogermanische Wurzel vehh'^ veph', vtra'rtü. wthen^ zuerst
Aufrecht KZ. 4, 282, fehlt auch in der neuesten Auflage von Fick*8
indogermanischem Wörterbuch, erster Theil.
') FR citirt als Beleg einen wortspielreichen Vers Senäl's
(Metr. Xeflf):
tä kl hhisesf /^äjS der bcUis
hälei ämed zt näz^ der hälis
```


### [2026-09-05T06:11:52.868Z] TOOL RESULT

```
742:169. Np. bay 'Garten' stimmt zu skr. bhaga- 'Teil, Anteil'
2675:bal. sumbag 'bohren', nb. sumbay *Seitenstechen das,
4284:polnz 'Garten = hebr. pardes (Hohelied), arm. partBz^ zd.
4610:vl^vared ; pal&: *Garten , arm. partSz, hebr. pardBs, zd. pairi-
4775:vor einfachen Eonsonanten : pdlez *Garten' = zd. pairidaeza-
4996:stand'; bustdn = bdstan 'Garten'; tuxm 'Same' = paz. tuxm^
7896:(yi) H. 213; barOz 'Schmuck' [g^) H. 193; pmz ^Garten
7918:'Garten', Varaz (in Namen) 'Eber' u. s. w. ; rz, das auch zu rj
8847:bag Antheil, Erbe' ^= zd. baya-, paz. bag 'Theil, Antheil'
8967:*Garten' = drast; taxtak 'Tafel' = tastdk. Doch geht duxt
9205:pr. sunbam 'durchbohre*, bal. sumbag 'bohren (oben p. 76);
9308:vared; guvCLlldan Vachsen , zd. m-vared; pflfe^r /Garten',
9831:eine Gartenpflanze mit zweiellenlangem Stengel,
```


## [2026-09-05T06:12:00.215Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '735,760p' HUB.txt\necho \"===== which leaf =====\"\nawk 'BEGIN{RS=\"\\f\"} /169. Np. bay .Garten./{print NR; exit}' HUB.txt",
 "description": "Read Hübschmann on bāγ"
}
```


### [2026-09-05T06:12:01.762Z] TOOL RESULT

```
sanisch-kurd. bahU *Unter-und Oberarm' (ZDMG. 38, 52)
gehort. Ob auch afgh. bau, bahu (pi. baUgdn^ bahugan)
'Armband, Schmuck fiirs Handgelenk' und armenisch
bahuand 'ein Frauenschmuck mit Edelsteinen (wohl aus
*bahuband) ?
167—168. Fiige ein: bdSdma, vdSdma 'Kopfhiille der
Frauen, arm. varsamak 'Schweisstuch'.
169. Np. bay 'Garten' stimmt zu skr. bhaga- 'Teil, Anteil'
etc. in der Bedeutung durchaus nicht.
171. Bal. balad 'H6he* scheint, wie auch Geiger, Laut-
lehre p. 19 (wegen I aus rd = rz) annimmt, altes
Lehnwort zu sein. Doch ist das Suffix aS, ad echt
balu5i, vgl. drazad Lange' (neben drazt) von drag lang- 24 —
(Dames, Grammar p. 14). Np. ftai^a *hoch, H5he* ist
wohl mit Suffix a aus ok (= phi. *bardak) gebildet
wie garma etc. (Darmesteter, Etud. iran. I, 267).
173. Np. bdltdan Vachsen' zu phi. caus. voimttan Phi.
Vend. 9, Z. 6 (vahn) ^) = zd. varedaya- Vachsen machen ,
Mann- Andreas, ZDMG. 47, 702.
174. Zu ham Morgen =paz. ham Aogemad. 114, vgl. phi.
hosbam 'daybreak' Gl. and Ind. p. 52, Min. Gl. 104,
Aogemad. 129, paz. bomdaS *dawn* Min. Gl. 40, bal.
gvarbOm *Dammerung' (Geiger Nr. 138). Afgh. bam
*Dach des Hauses* gehort zur folgenden Nummer. Zd.
bdmya- (im Metrum dreisilbig : botniya-) heisst trotz
Geldner nie sublimis*, sondern glanzend, strahlend,
===== which leaf =====
34
```


## [2026-09-05T06:12:13.148Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | head -60\necho \"===\"\ngrep -n \"βxš\\|Bxs\\|bxs-\\|bxš\" SOD*.txt 2>/dev/null | head -20",
 "description": "List refs dir and grep SOD"
}
```


### [2026-09-05T06:12:13.208Z] TOOL RESULT

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
===
SOD.txt:55124:7053  prbys-   C  ->  prbxs- 
SOD.txt:55127:parPayt-   ©pt.  st.;  pres.  prbYs-   =»prbxs-, 
SOD.txt:55230:parPaxste  ©pp.  =»prbxs-,  prbyty,  prP*ytk 
SOD_pages.txt:23965:7053 prbys-           C -> prbxs-                                               prbxsty
SOD_pages.txt:23968:      parPayt- ©pt. st.; pres. prbYs-           =»prbxs-,                     GMS 666; C2, 94V24 & p67; STi 6.3; Sund. AoFi
SOD_pages.txt:23985:7057 prPr- B                        o^^Cn* <u*boli;                           parPaxste ©pp. =»prbxs-, prbyty, prP*ytk
```


## [2026-09-05T06:12:19.663Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^[0-9]* *Px\\|Px5\\|PxS\\|Pxs\" SOD_pages.txt | head -30\necho \"=== BY god ===\"\ngrep -n \"god, lord\\|'god'\\|god, deity\" SOD_pages.txt | head -30",
 "description": "Grep Gharib Sogdian for bxs and bg"
}
```


### [2026-09-05T06:12:19.744Z] TOOL RESULT

```
6405:     anPaydc     =^npxs-                                                anpaxs, ambaxs         'np^t'k, >nPxs-
11208:     GMS 1964; BBB; Gersh. Sogd. Cpds. 138 n 2, 146              Paxs ©Shag-, baxsa =*Pxs-
13744:       8paxstc     ©f. pp. =»5Pxsty(y), 5p>yz-, Sp'yst-                 KG pl83; MSP bl31; GMS 515, 936; STi 39.5;
18917:                                                                            5335 mnPxs- M
33683:      wi8Paxs (wySPxs, wy8pys-) ©Khwar. bSfixs              10363 wy8wc cync M =* wyd}wc}ync
=== BY god ===
```


## [2026-09-05T06:12:23.718Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page 103\\]\\|\\[pdf page 104\\]\\|\\[pdf page 166\\]\\|\\[pdf page 167\\]\" SOD_pages.txt | head",
 "description": "Find pdf page tags in SOD"
}
```


### [2026-09-05T06:12:23.768Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:12:26.622Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SOD_pages.txt | head -5\necho \"---\"\nawk 'BEGIN{RS=\"\\f\"} NR==104' SOD_pages.txt | head -30",
 "description": "Inspect SOD page structure"
}
```


### [2026-09-05T06:12:29.522Z] TOOL RESULT

```
---
                                                                                                                       38

 Wyscy


      TSP 3.158 n pi 96; -Wf TSP 3.155; KG 486, 525,          GMS 396, 1004
        529, 632
                                                          978 'ndwxs M                                    J& iJ&J'
 965 WPyscy B                                ?^«>             anduxs ©ob. -yy ^ntwys
     refusal, rejection ?                                     effort, pursuit
     Lentz. STii 10,37; Hen. BBB 573; CMS 1008                Hen. Tales. 470.54; KG 2374
 966 >n6py- B                      j^b^yo^                979 'ndwxs-1 M                                          oxj^/
     andPay,
       *Sp'y- an0way ®<*ham-9waya-  -^nSpyt,                  anduxs   Ontwxs-, >ndwxs-:)      ^ntHvys

     0o)develop                                               0<9)strive
                                                              BBB 710; GMS 539; AVS 73
     CMS 293; TSP 2.361; Hen. Texts. 734, AVS 94
                                                         980 >ndwxs-2 B => Wwys-, todwxs-1
 967 ,n5pyt B                                    <»jj          Jn5'ykM,
                                                         981 >n8yk    (h)S                  cl^,jJuixJ^
     andPit ©pp. =>>n5Py-                                    andik, an8ik ? ©<*ham-dais~ ©ob. -v ^dyq,
     developed
     GMS431
                                                              nature, function, custom
 968 ,n6m,k ** 'nSm'y                                         BBB f91; GMS 1151; Hen. BSOAS 11.69, 29; MSP
 969 'nfim'y B, S                                               b64, 65; C2, p75; Bcnv. Et. 2.125
                                               y&^xS
     andame OnSmy, 'nSmyy, 'nSnVk)                       982 »n8ysn M, S                            (^x/)jU;oL;
       ®<*ham-ddman ©pi. -t -^dmy                            andesn, an5es(a)n ? Ondysn)
```


## [2026-09-05T06:12:38.036Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==166' SOD_pages.txt | head -40\necho \"########## leaf 103 (p.37)\"\nawk 'BEGIN{RS=\"\\f\"} NR==103' SOD_pages.txt | head -20",
 "description": "Print SOD printed pages 100 and 37"
}
```


### [2026-09-05T06:12:39.726Z] TOOL RESULT

```
                                                                                                       mmmmm^^^mt



 P'z'kh                                                                                                                100


            p204; Hen. Texts. 732; KG 373                         2540 pS'yz- B                         u^liji Oju^-
                                                                       Ps8ez ©<*abi-darzaya~; Parth. abdarz; Yaghn.
 2526 p>z>kh      B => p>z>
                                                                       * bidez- =»p5ystk, p5>yz>k
 2527 pVyt -» fl'z*                                                    (ro)cover, (fo)wrap
 2528 b'zyd- C =* P'zy5-                                               BSTBL, Dhu. 22, 286
 2529 P'zyS-      S                                    Oj^jIj-   2541 p5,yz,k B                              t>j^^ijJ,y_
          pazya5 (b'zyd-) ©impf. =>PzyS-
                                                                       Po6eze,
                                                                       coating, PiSezak
                                                                                covering =»p5>yz-
          (to)mount
          VJ 855; TSP 13.27; BSTii 880.5; C2, 77R5                     TSP 3.180, 196 n pl97

 2530 p>zy B                                         0=^-'-?'    2542 p5ystk B                           •j^^«ju*=i
      Pazay ©impf. ^Pz'y-                                             PoSiste ? ©<*abi-drsta; fdarz-, Yaghn. bidizta
      OcOincrease
                                                                       wrapped
      TSP 2.187                                                          ©pp. ^p5}yz-
                                                                       SCE 341; BSTBL, Dhu. 285; GMS 149A
 2531 b'zynt
      pazant ®3pL impf. =»p-                                     2543 Py- B, M, S          (oy^»* jj)vU^«Li*JJ-r^Jj^.
      GMS 801; AVS 229; b>znt% C2, 60 R29                             paY (bY-) ©<baga ©nom. ob. -y(yh ace. -w;
2532 -pc S                                    (ojby jl^y                voc. inst. abl. ->; pi. firyn, fiYh)yst =>PY*yst
                                                                      God, Lord, king, sir, excellency
     fac =»-p                                                         GMS 1168, 1177; Hen. BSOAS 1965, 245; fix,
     (from)you, (of)you                                                 STii 10.21
     Anc. Lett. 3.5, 4.3; GMS 1358
                                                                 2544 bY-   C -* Py-
2533 pdnpSCS)        B, M                                o^r
      f(o)canpa6 (pcnpS) ©ob. -y -^Pc'npSCS),                    2545 PYwn B, M, S                            (JU,)uIIj^
        fc»np5, >fcmb5(8)                                             PaYan (PYJn(h)) ©<bagandm        ©gen. pi.
      world
########## leaf 103 (p.37)
                36
                                                                                   Iju
                       37                                                                                                                     >n5)yk(h)

                       942 topr'kw B                                                     952 'nc'nh     B «* >nc}n
        oy>** i jUjI       anParaku ?                                                    953 WtCy)       C                            jfu^ijT^^
                           continuously
                                                                                              ancat(e) ©<*ham-cyata-           -»Jnc*y-
                           BSTBL, Padm. 27.45; Mack, n plOj S W, C2
                                                                                              appeased, rested, resided
                                                                      ^T1
                                                                                              BSTi 174; C2, 12V1
                              p76. 21
                       943 >nprytk B                            g=fcl<J>*                954 Wy-        S, M, C =» >nc»y-                        ^njmn,
>brty, Jn(3r-,             anPrayde, ambrayde (nP'rytk, 'nPryty) =^bryty                 955 5ncmn      M, C
                           paralysed, crippled
                                                                                              ancaman, anjaman ©ob. -y; ob. pi. ~ty =^
                           SCE 93, 117
                                                                                                'ngm'n
                       944 »npryty =» 'nPrytk                                                 assembly, reunion, church
```


## [2026-09-05T06:12:47.254Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"distribute\\|(to)divide\\|share, portion\\|apportion\" SOD_pages.txt | head -30",
 "description": "Grep Gharib for distribute/divide"
}
```


### [2026-09-05T06:12:47.306Z] TOOL RESULT

```
16604:         MDii; Frag. Len.; S W, MIS 1984, 207; pi.                (to)divide, (fo)part ?
```


## [2026-09-05T06:12:52.841Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 167 168; do echo \"#### leaf $L\"; awk -v l=$L 'BEGIN{RS=\"\\f\"} NR==l' SOD_pages.txt | head -50; done",
 "description": "Print SOD pages 101-102"
}
```


### [2026-09-05T06:12:54.261Z] TOOL RESULT

```
#### leaf 167
 101

 2550 py'n'nywn M                jUj^ju;U<4^^U^<jIj^U^                  312; Sund. AoFi 1974, 226; Hen. BSOAS Pyk^yc
                                                                                                               1965,
                                                                        247
      Payan-anyon
        god like                                                 2563 py'ny pskVk S          j*J'l^<jjJ'jUh tj^-d^M*
        GMS 1113;BBBf62                          jlU>- jj^                                           (-r-d iSf~# lT^    X*i
                                                                      Payane-piskate ^by'npsqty
 2551 py'n 'xsyya M
                                                                      god's tiding, wedding
      Payan-axsa6 (Py^ysyS)
                                                                      STi 39.14; Hen. Tales. 486 n 1; Hen. BSOAS
      lord of the gods           »Py'n MLK>
      GMS 1189; H?n. Tales. 485; W-Li                                    1965, 247 "baga-union making"
                                                                 2564 by'nyspqty C                     ^^^^
 2552 py'n'yk' Bt S    (jj> >^ ^)j'j^ v^^-,J^                         Payanespkote ? ^PyWysp
      Payanik (by'nyq, py'n'ykh) ©Parth. baganig                      feast, marriage feast
        ©ace. -w ^Py'nyk0'                                            BSTii 884.18; C2, 48V21; Benv. JA 1955, 312
      divine
      GMS 997, 1042; VJ 15, 92; TSP 7.9, 5.102, 103,            2565 py>nyyk M => Py>nyk(,)
        10.4; SCE 501, 558; KG 512, 533; Frag. Len.             2566 py'ptyc M                          J**<^<>*-
        57.13,71.13                                                  Pay(a)patic (Pyyptyc) ©*baga- pati ?
                                                                     divine
2553 py'n'ykh -» Py,n>yk>                                             BBB b71; Gcrsh. Sogd. Cpds. 141; Hen. Talcs.
2554 py'n'ysp S(M)            £l>>ji^Ui~ ju^<^iu x^                     476.19
     payanysp ? =»byJnyps
                                                                2567 PY'ystMn B, S             ji=_jJ *jUjl>- J^ <c~i#
     god's tiding, marriage
     Hen. Tales. 486.7 n 1; Hen. BSOAS 1965, 242                     Paycstan (Pyyyst'n) ©loc. -yh ^pyyst'n,
                                                                       byyst'n, PyyWn
2555 py'nysya     B -» Py>n Jxsyy5                                   god's place, paradise
2556 pY}n(h) => Py'n                                                 GMS 122, 1118; TSP 2597, 1022, 1138; 0: 18, 33;
2557 py>n MLK>       B                                                 Frag. Len. p94
                                                  OlfjLs- eU*
       Payan-xutaw =»pyJn 'xsyy6                                2568 py'yst B                                          jUj^
       king of the gods                                              Payist ©pi. =^Py-, Pyyst, Pyyct
       Frag. 4.3; BSTBL, Dhy. 173
                                                                     SCE 4; VJ 907, 1005, 1112; TSP 5, 6, 68; STii
2558 by>npsqty C                    ^^                                 1045; BSTBL, Intox. 4, Padm. 51; Frag. Len. ob.
     payan-pis-kote ^Py'ny pskt>k
                                                                      gods
     marriage, wedding                                                 flrysty;
                                                                       10.45    VJ 98; TSP 2.395; fix'ysu STii 8.6,
     STi 39.4; Hen. BSOAS 1965, 242-7                   cb>J    2569 pySVk      B                     ( j5U-)ju^«1^-.>t
2559 pY»n(y) pytm        B => py»n Pytm
                                                                     Pay-5ane
                                                                     temple      ©<*baga-ddna ©ace. -u>
2560 by'nyq     C => Py'nyk^
2561 PY>nykw B, M            (^)^0I^U^                               cxwS/ir&ny, Hen. BSOAS 1956, 367 n3,
#### leaf 168
 Pymyc                                                                                                              102
         MDii; MDiii A10.9                                         TSP 7.29, 34
 2574 pymyc     M                                           2584 pypsyh =¥ Pypsyy
                                    ( Jj^)JjkS]j^- '^J-^    2585 Pypsyt M                                        Ij^ j^
      Paymec
      divine, (of) god                                           Pay-poset (Pyspsyt) ©pi. fiYpsyt
      GMS 1103
                                                                   god's sons 476.9 i
                                                                   Hen. Tales.
 2575 pyn- M                               x^^€^^^
      payn, Payan ©<*bagina ©nom. -yy; ace. -w%             2586 Pypsyy       M                            <^>Jj^^
        abl. -J; loc. -y                                           Pay-pase     (Pypsyh) ©pi. -i ^pyp'wr
      temple
      GMS 165, 509, 1183; BBB; Hen. Tales. 473, 42;                god's son
                                                                   Tales. 476, 9 n 1; GMS 1067, 1666; Hen. BSOAS
        C2, 25R23, 25V n p62; Sund. AI 28, 1988, 180                  12;Cosm. 312, 80; BBB 579

2576 pynJk B                              c^Jm^,            2587 pypwr        M, S =» pypNvr
     Payne ©*bagna-ka~y Khwar. ^/w'jk; Oss.                 2588 pypwr'yc       M   jV)^        j0^    ((^x,)ii^ >j
       bdxndg =*byny
     naked                                                        Paypuric, Paypurec (Pypwryc)         =»pwryc
     SCE 385; Prolexis. 256                                       god's daughter, Divine Virgin
                                                                  GMS 1276; BBB 579
2577 pynpt'nch B                          o*lT<oj JV=r
     Payn-patanc                                            2589 pypwr'yst M           ^ui, ^^li^**** o& j^*y
     sorceress                                                   pay- purist (Pypwryst) ©pi. ^Pypwr'yc
                                                                 Divine Virgins
      SCE 250, 252
                                                                  BBB 579; GMS 26, 1276-, KG 605
2578 pynpt(w) B, S                  (oU-^jaIT «/^U
     payn-pat(u)                                            2590 pypwr stny B                  &~*jy>&ijy&(jj^' )*>&=?
     sorcerer, priest
     Anc. Lett. 1.10; SCE 255; Hen. BSOAS 28.250;                 paypur-stane
                                                                  China, {country <?/)Faghfur
       MDii pl70.5                                                TSP 8; Hen. Texts. 763
                                                            2591 pypwryc =* Pypwryc
2579 pynwy(y) M                             (>^-^)>*U
     Pay-nawe ©abl. -nw)      =^pyynwy(y)                   2592 pypwryst =* Pypwryst
     new moon
                                                            2593 pys- B, S                    o^J'jj^ <j.>b io<>~*>
     GMS 1964; BBB; Gersh. Sogd. Cpds. 138 n 2, 146              Paxs ©Shag-, baxsa =*Pxs-
2580 byny     C                                      <ca^        (ro)offer, 0o)give
                                                                 VJ; TSP 2.588, 3.206; BSTBL; MDii; GMS 551;
     Payne     (Pyny) ©pi. -t =»Pyn'k
     naked                                                          Hen. AION 1959, 35; 3sg. impf. fi'xl Frag.
                                                                    Len. 48.1
     Sogdica. 39.22; STi 27.12, 18; Sund. AI 28, 1988,
       180                                                  2594 pyspsyt =» Pypsyt
2581 pyny     M ** byny                                     2595 pyt—    B                         ^^ij^y <o^ ioXJ^v
2582 pyp>wr     B, M, S        j/>p)j>u9 ^IjIji^ ««jljAli         Payd/t ©pt. st. =»prbyt-
```


## [2026-09-05T06:13:14.786Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB bahadur ===\"\ngrep -n -i \"bahadur\\|BAHAUDUR\\|bhagadhara\\|bhaga-dhara\" HJB.txt | head -20",
 "description": "Grep Hobson-Jobson for bahadur"
}
```


### [2026-09-05T06:13:14.838Z] TOOL RESULT

```
=== HJB bahadur ===
2489:BAHAUDUR
2504:BAHAUDUR,  s.  H.  Bahadur,  'a hero,  or  champion.'  It  is  a  title  affixed commonly  to  the  names  of  European officers  in  Indian  documents,  or  when spoken  of  ceremoniously  by  natives {e.g.  "Jones  Sahib  Bahddur"\  in  which use  it  may  *be  compared  with  "the gallant  officer"  of  Parliamentary courtesy,  or  the  lUtutrissimo  Signare  of the  Italians.  It  was  conferr^  as  a title  of  honour  by  the  Great  Mogul and  by  other  native  princes  [while in  Persia  it  was  often  applied  to  slaves (Burton,  Ar.  Nights,  iii.  114)].  Thus it  was  particularly  a^ffected  to  the  end of  his  life  by  Hyder  Ali,  to  whom  it had  been  given  by  the  Raja  of  Mysore (see  quotation  from  John  Lind«iy below  [and  Wilks,  Mygoor,  Madras reprint,  i.  2801).  Bahddur  and  Sirddr Bahddur  are  also  the  official  titles  of members  of  the  2nd  and  1st  classes respectively  of  the  Order  of  British Inaia,  established  for  native  officers of  the  army  in  1837.  [The  title  of Rdi  Bahddur  is  also  conferred  upon Hindu  civil  officers.]
2507:BAHAUDUR.
2508:BAHAUDUR,
2510:Bahddur  is  one  of  the  tenas  which the  hosts  of  Chlngiz  Khan  brought with  them  from  the  Mon^l  Steppes. In  the  Monffol  cenealpgies  we  hnd Yesugai  Bahadur^  Uie  father  of  Chineiz, and  many  more.  Subutai  BahMur, one  of  the  great  soldiers  of  the  Mongol host,  twice  led  it  to  the  conquest  of Southern  Russia,  twice  to  that  of Northern  China.  In  Sanang  Setzen's ]X)etical  annals  of  the  MoiLgols,  as rendered  by  I.  J.  Schmidt,  the  word is  written  BaghaJtuTy  whence  in  Russian Boffoiir  still  survives  as  a  memento probably  of  the  Tartar  domination, meaning  *^  hero  or  champion.'  It occurs  often  in  the  old  Russian  epic fiallads  in  this  sense ;  and  is  also  ap- plied to  Samson  of  the  Bible.  It occurs  in  a  Russian  chronicler  as  early as  1240,  but  in  application  to  Mongol leaders.  In  Polish  it  is  found  as  Bo- hatyr^  and  in  Hungarian  as  Bdtor, — this last  beinjg  in  fact  the  popular  Mongol pronunciation  of  Baghaiur.  In  Turki also  this  elision  of  the  guttural  extends to  the  spelling,  and  the  word  becomes Bdtur,  as  we  find  it  in  the  Diets,  of VamWry  and  Pavet  de  Courteille. In  Manchu  also  the  word  takes  the form  of  BatuTUy  expressed  in  Chinese characters  as  Pa-tu-lu ;  f  the  Kirghiz has  it  as  Baiyr;  the  Altai-Tataric  as PcuUtyTy  and  the  other  dialects  even as  Magaihyr.  But  the  singular  history of  the  word  is  not  vet  entirely  told. Benfey  has  suggestecl  that  the  word originated  in  Skt.  bhaga-dhara  (*  happi- ness-possessing'). J  But  the  late lamented  Prof.  A.  Schiefner,  who favoured  us  with  a  note  on  the subject,  was  strongly  of  opinion  that the  word  was  rather  a  corruption ^Hhrough  dissimulation  of  the  conso- nant," of  the  Zend  bagha-puthra  *  Son of  GJod,'  and  thus  but  another  form of  the  famous  term  Fagbfor,  by  which the  old  Persians  rendered  the  Chinese Tien-tsz  (*Son  of  Heaven  *),  applying  it to  the  Emperor  of  China.
2521:1404.— "E  elles  le  dixeron  q  aquel  era uno  de  los  valiStes  e  Bahadures  q'en  e) linage  del  Sefior  am&"—Clavij0f  §  Ixxxix.
2523:1407.— "The  Prince  mounted,  escorted  by a  troop  of  Bahadurs,  who  were  always about  his  peTaon."—Abdurrazak't  Hist,  in Not.  et  Ext.  xiv.  126.
2528:We  have  said  that  the  title  Behauder {Bahadur)  was  one  by  which  Hyder Ali  of  Mysore  was  commonly  known in  his  day.  Thus  in  the  two  next quotations :
2537:1872.—".  .  .  the  word  'BahAdnr'  .  .  . (at  the  Mogul's  Court)  .  .  .  was  only  used as  an  epithet.  Ahmed  Shah  used  it  as  a title  and  ordered  his  name  to  be  read  in  the Friday  prayer  as  'Mujahid  ud  dfn  Mu- hammad AbtE  na^r  Ahmad  Sh^  Bahddur. Hence  also  *  Kamjaani  Bahadur,'  the  name by  which  the  £.  1.  Com^ny  is  still  known in  India.  The  modem  *  Khan  Bahddur '  is, in  Bengal,  by  permission  assumed  by  Mu- hammedan  Deputy  Magistrates,  whilst  Hindu Deputy  Magistrates  assume  *  R^  BalULdur ' ; it  stands,  of  course^  for  ^  KhjCn-i-Bahddur, ' 'the  courageous  Kh^n.'  The  compound, however,  is  a  modem  abnormal  one;  for *Khin'  was  conferred  by  the  Dihli  Em- perors, and  so  also  *  Bah^ur '  and  *  Bah^ur KMn,'  but  not  *Kh^  Bah^ur.'"— Pro/. Blochmann,  in  Ind,  AfUifptary,  i.  261.
3229:*  The  "  Bahadur"  ooold  hardly  have  read  Don Quixote  I  But  what  a  cuiiooa  parallel  presentH itself!  When  Sancho  Is  bracing  of  his  aau^ter to  the  "  Squire  of  the  Wood,  and  takes  umbrage at  the  ftee  epithet  which  the  said  8qnira  spiles to  her  (s  IsMmUkA  and  more) ;  the  latter  reminds him  of  the  like  term  of  apparent  abuse  (hardly reprodnoeable  here)  with  which  the  mob  were .wont  to  greet  a  champion  in  the  bull-ring  after  a deft  spear>thiust,  meaning  only  ths  highest  fbnd* nass  and  applause  I— Ffert  ii.  eh.  IIL
4583:1711.— "To  his  Excellency  Zulfikar  Khan Bahadur,  Nurzerat  Sing  {Narrat-Jang  i) Backshee  of  the  whole  Empire." — Address of  a  Letter  J/roia  President  wnd  Council  of Port  St,  George,  in  Wheeler,  ii.  160.
8861:DIU,  n.p.  A  port  at  the  south  end of  Peninsular  Guzerat.  The  town stands  on  an  island,  whence  its  name, from  Skt.  dvipa.  The  Portuguese were  allowed  to  build  a  fort  here  by treaty  with  Bahfidur  Shah  of  Quzeratj in  1535.  It  was  once  very  famous  for the  sieges  which  the  Portuguese  suc- cessfully withstood  (1538  and  1545) against  the  successors  of  Bahadur  Shah [see  the  account  in  Linsdkotm^  Hak. Soc.  i.  37  aeq,l  It  still  belongs to  Portugal,  but  is  in  great  decay. [Tavemier  (ed.  BaU,  ii.  36)  dweUs on  the  advantages  of  its  position.]
12082:S)utch)  Government  (see  H.  0,  Forbes, cUuralid's  Wanderings,  1885,  p.  204). [DohM  Oompany  Bahadur  ik  is  still a  common  form  of  native  appeal  for justice,  and  Company  Bdgh  is  the usual  phrase  for  the  public  garden  of a  station.  It  has  been  suggested,  but apparently  without  real  reason,  that tne  phrase  is  a  corruption  of  Company Jah&n,  '*  which  has  a  fine  sounding smack  about  it,  recalling  Shah  Jehan and  Jehangir,  and  the  ffolden  age  of the  Moguls"  (6r.  A,  Saia,  quot^  in Nates  and  Queries,  8  ser.  ii.  37).  And Sir  Q.  Birdwood  writes  :  "  The  earliest coins  minted  by  the  English  in  India were  of  copper,  stamped  with  a  figure of  an  irradiated  lin^am,  the  phallic *  Roi  Soleil.'  The  mintage  of  this  coin is  unknown  ^?  Madras),  but  without doubt  it  must  nave  served  to  ingratiate us  with  the  natives  of  the  country, and  may  have  ffiven  origin  to  their personification  of  the  Company  under the  potent  title  of  Kmnpani  Jehan, whicn,  in  English  mouths,  became *John  Company'"  (fieport  on  Old Records^  222,  note).]
20305:[c.  1803. — In  a  collection  of  native  letters, the  titles  of  Lord  Lake  are  given  as  follows : *'A$h:fa-vl'Mulk  Khdn  Dmtrim,  General Gerard  Lake  Bahadur,  8ipahialar-i-kishwar- i-Hind,"  **  Valiant  of  the  Kingdom,  Lord  of the  Cycle,  Commander-in-chief  of  the  Terri- tories of  Hindustan."- Aor<A  Imdian.  Sotes and  Queriety  iv.  17.]
22111:the  tiger  stood,  and  I  stood,  and  we  looked at  each  other.  I  had  no  weapon  but  my kukri  (KooIot)  .  .  .  and  the  Grovemment letters.  So  I  said,  *  My  lord  Tiger,  here are  the  Grovemment  letters,  the  Tetters  of the  Honourable  Kumpany  Bahadur  .  .  . and  it  is  necessary  for  me  to  go  on  with them.'  The  tiger  never  ceased  looking  at me,  and  when  I  had  done  speaking  he growled,  but  he  never  offered  to  get  out  of the  way.  On  this  I  was  much  more  afraid, so  I  kneeled  down  and  made  obeisance  to him ;  but  he  did  not  take  any  more  notice of  that  either,  so  at  last  I  told  him  I  should report  the  matter  to  the  Sahib,  and  I  threw down  the  letters  in  front  of  him,  and  came here  as  fast  as  I  was  able.  Sahib,  I  now  ask for  your  justice  against  that  tiger.'" — Lt.- Col,  T,  Lemn,  A  Fly  on  the  Wheel,  p.  444.
23748:Bab^ur,    Bahadurc,
```


## [2026-09-05T06:13:16.657Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AID bahadur ===\"; grep -n -i \"bahadur\" AID.txt | head -10\necho \"=== KLN bazu/brachium ===\"; grep -n -i \"OI. bāhú\\|bāhú\\|bahu-\\|Bhagavad\" KLN_1966.txt | head -20",
 "description": "Grep AID and Klein"
}
```


### [2026-09-05T06:13:16.737Z] TOOL RESULT

```
=== AID bahadur ===
5758:RAm  RAA.  The  denomination  of  Sikhs who  adhered  to  RAm  RAi,  the  son  of Har  RAi  the  seventh  guru,  when  the succession  passed,  not  to  him,  but  to his  great-uncle  Tegh  BahAdur.
=== KLN bazu/brachium ===
4302:baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
4885:Bhagavad-Gita,  the  celebrated  dialogue  between Krishna  and  Arjuna  inserted  in  the  Maha- bharata.  —  OI.  Bhdgavadgita,  ‘the  song  of  the Sublime  One’,  compounded  of  Bhaga,  suff. -vant  (corresponding  to  Gk.  -Fevr-,  -evt-)  and gi-td,  ‘song’,  prop.  fern.  pp.  of  gdyale,  ‘sings, calls',  from  the  I.-E.  imitative  base  *ga-,  *gi-, whence  also  Avestic  ga&a,  Pers.  gah,  ‘song’, Lith.  giedoti,  'to  sing’,  giesme,  ‘song’,  Lett. diesma,  ‘song’.
28431:-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning
```


## [2026-09-05T06:13:28.221Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^bahadur\\|bahadur,  n\\|^Bhaga,\" KLN_1966.txt | head\necho \"=== bough ===\"\ngrep -n \"bough,  n\\|^bough\" KLN_1966.txt | head\necho \"=== bow ship ===\"\ngrep -n \"bow,  n\\.,  the  fore\\|bow.*fore  part of a ship\\|forepart  of  a  ship\" KLN_1966.txt | head",
 "description": "Grep Klein for bahadur, Bhaga, bough, bow"
}
```


### [2026-09-05T06:13:28.302Z] TOOL RESULT

```
4884:Bhaga,  n.,  a  god  of  wealth  (Vedic  mythol.)  — OI.  Bhagah,  lit.  ‘allotter,  distributer,  master, lord’,  fr.  bhdjati,  ‘assigns,  allots,  apportions,  en¬ joys,  loves’,  rel.  to  Avestic  haya,  OPers.  baga, ‘master,  lord,  god’.  See  baksheesh  and  cp.  next word.  Cp.  also  pagoda.
=== bough ===
5426:Bougainvillaea,  n.,  a  small  genus  of  woody  vines. —  Named  after  the  French  navigator  Louis Bougainville  (1729-1811). bough,  n.  —  ME.  bogh,  fr.  OE.  bog,  boh,  ‘arm, shoulder,  bough’,  rel.  to  ON.  bogr,  ‘shoulder; bow  of  a  ship’,  OHG.  buog,  MHG.  buoc,  G.  Bug, ‘shoulder,  hock,  joint’,  fr.  I.-E.  *bhdghus-,  ‘el¬ bow,  arm’,  whence  also  OI.  bahuh,  Avestic  bazu, Arm.  bazuk,  ‘arm’,  Gk.  7rijxuS>  Dor- ‘elbow’,  Toch.  A  poke,  B  pauke,  ‘arm’.  Cp.  bow, ‘the  fore  part  of  a  ship’.
5427:bought,  past  tense  and  pp.  of  buy.  —  ME. boht(e),  fr.  OE.  bohte,  resp.  (ge)boht.  See  buy. bougie,  n.,  1)  a  wax  candle;  2)  a  surgical  instru¬ ment  used  to  dilate  a  body  canal.  —  F.,  ‘wax candle’,  fr.  Bougie,  Bugia,  a  town  of  Algeria. The  orig.  meaning  was  ‘fine  wax  candles brought  from  Bugia’,  and  only  at  a  relatively later  period  did  the  sense  of  the  word  develop into  ‘candles  brought  from  Algeria’,  and  ‘can¬ dles’  in  general.
18142:bough,  n„  the  hock  ( chiefly  Scot.)  —  The  orig. spelling  of  hock,  ‘joint  in  the  hind  leg  of  the horse’.
18143:boughite,  n.,  a  variety  of  hydrotalcite  (mineral.)
=== bow ship ===
5468:bow,  n.,  the  fore  part  of  a  ship.  —  Of  Scand. origin.  Cp.  ON.  bogr,  Dan.  bov,  Swed.  bog, ‘shoulder;  bow  of  a  ship’.  See  bough, bowdlerize,  tr.  v.,  to  expurgate.  —  Formed  with suff.  -ize  from  the  name  of  Thomas  Bowdler, who  in  1818  published  The  Family  Shakespeare, expurgating  from  it,  according  to  his  own words,  ‘whatever  is  unfit  to  be  read  by  a  gentle¬ man  in  a  company  of  ladies’.
```


## [2026-09-05T06:13:40.322Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"leaves\",len(leaves))\nfor i,l in enumerate(leaves):\n    if 'bough,  n.  —  ME.  bogh' in l:\n        print(\"bough leaf\",i); print(repr(l[:300])); print(\"...\")\n    if 'Bhaga,  n.,  a  god  of  wealth' in l:\n        print(\"Bhaga leaf\",i); print(repr(l[:300]))\n    if \"bow,  n.,  the  fore  part\" in l:\n        print(\"bow leaf\", i); print(repr(l[:200]))\nEOF",
 "description": "Locate Klein leaves for bough/Bhaga"
}
```


### [2026-09-05T06:13:42.171Z] TOOL RESULT

```
leaves 903
Bhaga leaf 100
'��,  fr.  beurre,  ‘butter’. See  prec.  word.\nbevel,  n.,  inclination  of  a  surface.  —  OF.  "baivel (whence  F.  beveau,  biveau),  ‘bevel  rule’,  fr.  OF. baif,  ‘with  an  open  mouth’,  fr.  baer,  beer,  ‘to gape’.  See  bay,  ‘part  in  the  wall’,  and  cp.  words there  referred  to.\nD'
bough leaf 111
' ambi-,  amphi-.\nbother,  tr.  and  intr.  v.  —  Of  uncertain  origin. Derivatives:  bother,  n.,  botheration  (q.v.), bothe r-er,  n.\nbotheration,  n.,  bother  (colloq.)  —  A  hybrid coined  from  the  verb  bother  and  -ation,  a  suff. of  Latin  origin.\nbothrio-,  combining  form  for  bot'
...
bow leaf 112
'  broth,  and  fervent,  phreatic.\nbourn,  bourne,  n.,  a  limit.  —  F.  borne,  fr.  earlier bodne.  See  bound,  ‘limit’, bourree,  n.,  an  old  lively  French  dance.  —  F., prop.  fem.  pp.  o'
```


## [2026-09-05T06:13:49.903Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in [99,100,101,110,111,112]:\n    nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', leaves[i])\n    print(i, nums[:10], repr(leaves[i][-200:]))\nEOF",
 "description": "Find page numbers on Klein leaves"
}
```


### [2026-09-05T06:13:51.519Z] TOOL RESULT

```
99 ['166', '167'] 'n.,  butter.  —  F.,  ‘butter’,  fr.  earlier  burre, fr.  L.  butyrum,  fr.  Gk.  pouxupov.  See  butter.\nbeurre,  n.,  any  kind  of  pear  with  soft  flesh.  —  F., pp.  of  beurrer,  ‘to  butter�'
100 ['166', '169'] 'ic-al, adjs.,  bibliograph-ic-al-ly,  adv. bibliolater,  n.,  a  worshiper  of  books.  —  See  next word  and  -later.\nDerivative:  bibliolatr-ous,  adj. biblioiatry,  n.,  worship  of  books;  worsh'
101 ['170', '171'] ' origin;  so  called  from  its  color. Big  Ben,  name  of  the  bell  attached  to  the  clock at  Westminster.  —  Named  after  Sir  Benjamin Fiall,  first  commissioner  of  works,  under  whose '
110 [] ' ‘both’,  Toch.  A  am-pi,  am-pe,  B  ant-api, Gk.  ‘both’,  apt-pi,  ‘round  about’,  L.\nam-bo,  ‘both’,  am-bi-,  ‘around’,  OSlav,  o-ba, Lith.  a-bu,  Lett,  a-bi,  OPruss.  ab-bai,  ‘both’.  Cp.'
111 [] "well,  spring’. Arm.  albeur  (gen.  aiber),  ‘source’,  Russ,  brujd, ‘current’,  bruit',  ‘to  stream  with  force’.  For more  cognates  see  barm,  brand,  bread,  brew, broil  (in  both  senses),"
112 ['193'] 'gut,  bowel’, fr.  L.  botellus,  ‘a  little  sausage’,  dim.  of  botulus. See  bowel  and  cp.  botulism, boycott,  tr.  v.,  to  combine  in  refusing  to  deal with.  —  Fr.  Captain  Charles  Boy'
```


## [2026-09-05T06:13:59.848Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'baksheesh,  n.,  a  gratuity' in l or 'bahadur' in l.lower():\n        nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$', l)\n        print(i, nums[:6], [x for x in l.split('\\n') if 'bahadur' in x.lower()][:3][:1])\nEOF",
 "description": "Find Klein leaf/page for baksheesh and bahadur"
}
```


### [2026-09-05T06:14:01.526Z] TOOL RESULT

```
85 ['140', '141'] ['baguette,  n.,  a  small  molding.  —  F.,  prop,  ‘a small  rod’,  fr.  It.  bacchetta,  dimin.  of  bacchio, ‘rod’,  fr.  L.  baculum.  See  bacillus, bahadur’n.,  a  title  given  to  European  officers  in India.  —  Hind,  bahddur,  ‘hero’,  which  accord¬ ing  to  Benfey  (in  Orient  und  Occident  1  137, quoted  in  Hobson-Jobson  49a)  derives  fr.  OI. bhaga-dhara-,  ‘happiness-possessing’.  The  first']
86 ['142', '143'] ["baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur."]
624 ['1169', '1170', '1171'] ['-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning']
```


## [2026-09-05T06:14:14.814Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f in ['BQT_v1_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'بازو', t):\n        s=max(0,m.start()-200); print(f, m.start(), repr(t[s:m.start()+300]).replace('\\\\n','\\n')[:520]); print('---')\n        if m.start()>400000: break\nEOF",
 "description": "Grep Borhan v1 for بازو"
}
```


### [2026-09-05T06:14:16.513Z] TOOL RESULT

```
BQT_v1_pages.txt 31511 'نی\u200cسر زمین
ختن وفق\u200cدهند تر کیب حروف بوضی\u200cدیگر لازمآمد . یکی\u200cازْ آنپایکاربردن
حرف «<شی> بودبرای ببان تلفظ حرف« » که\u200cدرختنی ما نند دیکرزبانپای\u200cایرانی
بسیاراست\u200cودر سا نسکر بت\u200cهیچ وجودندارد؛ و باین\u200cطریق «بازو» را «بای\u200cسو»
ژبان\u200cختنی را امتبازاتی مخصوص میباشد و درنوشتن آن حروف عله
همه کاملادر جز و کلمات نو شته\u200cمیشود و این\u200cبخلاف دیگر السنه\u200cابرانی ازقییل\u200cسندی
۱-رك:بالیز (متن وحاشیه). ۲- ازلپجةٌ وخی مد یاد خواهیم کرد .\x0cمقدیه شانزده
تست بت یت سس
ن
---
BQT_v1_pages.txt 162867 '| گر بچة اول پرستوك رابگیر ند در
وقتی که ماه در فزونی بود وشکم اورا مشکافند دوسنگ ریزه درشکم او
بر آید یکی بك رنگ و دیگری الوان چون در پوس تگوساله یابز کوهی
پیچند پیش\u200cاز آنکه گرد وخاك\u200cبراو نشیند و بر بازوی مصروع بندند یا بر-
گردنش آویز ند صرع\u200cاو زائل گردد. و گویند | گردو پرستو بگیر ند یکی نر
ویکی\u200cماده وسرهای آنهارا باتش بسوزانند ودرشراب بریز ند هر کس از\x0c"مقدنمه ۰ نود شش
آن\u200cشر اب خورد مست نگردد... ۹6\u200f
این\u200cبود نمو نه ومثالی چندازاتواع اغلاط وسپوها که صاحب برهانر |
روی\u200cداده 
---
BQT_v1_pages.txt 222572 'یش »آستانه » آستین » آسودن؛ [سیابان»
آش ۰ آشامیدن» آشیز ۰ آشتی» آشکارا » آشفتن » آفرید کار آهستگی»
آهنگر » ابرو » اردك » اردو ۰ اره » انگشتری » انگور » باداس >
بادام » باده » باران » باریدن *"بازار » بازو » باغبان » بسامداد »بخشش »
برف » بستن » بسیار» بلیل » بنده» بنیاد وغیره.
ما اینگونه لغات\u200cرا درحاشیه نقل کرده\u200cایمو بغشی از لفات\u200cرا که امروز
جزو زبان مامحوب میشود نیز در حاشیه افزوده\u200cایم» ازین قبیل ا-ت:
آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
انگشتانه» بادنجان باروت؛ بورانی
---
BQT_v1_pages.txt 355096 'باشد - و رسم و عادت وآیین را نیز
کویند - و نام نوابی است از موسیقی .
] ر اش خور شید - نام لسن اول
ست از سی لحن باربد و خطی که بي عارض
7 3
آرت . بقتح ثالث و سکون فوفانی .
آرنج را گوشد که\u200cبند گاه ساعد وبازوست وبعریی
مرفق خوانند ۴ .
دج - ختح. ناك
فآ ات کم باشد ۷ - ونامپر ندم\u200cای
آرد. بتح نله و ال ان
؟ \u200f رك : 1
آرت ۰ رد : : آرن
۰ رك : آرمیدن
۹ - رك:آران ۰
کردن » مهیا سلختن .
۳ هاده
کردن » آسودن . ساکن شدن .\x0cت برایو بی اه آرامی
رة حواشی صفحة .۳
۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب ف'
---
BQT_v1_pages.txt 361846 'ت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج\u200cاست که مرفی\u200cداشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم\u200cآعده است - وونج و'
---
BQT_v1_pages.txt 361918 'گر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج\u200cاست که مرفی\u200cداشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم\u200cآعده است - وونج ومجنت\u200cرا عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و 
---
BQT_v1_pages.txt 361958 '. 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج\u200cاست که مرفی\u200cداشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم\u200cآعده است - وونج ومجنت\u200cرا عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و طرز حم گفته\u200cاند چنانکه گویند :
«بدی
---
BQT_v1_pages.txt 499295 'شین
نقط 4 دار » مقداری باشد همین ٩\u200f ۰ و آن از سح
انگشت میانن دست\u200cراست است تاسرانگشت\u200cمیاتن
دست چپ , چون دستها را از هم کشاده دارند ؛
و بضی گویند از سر انگشت میادن دست )٩(\u200f
باشد امرفق که بند گاه ساعد و بازوست و این
اسح است - و نام شهرست از ولادت شیروان -
و بفتح اول و کسر ثانی بمعنی عاقل و زبرك و :
هوشیار باشد - و بمعنی انجمن هم بنظر آعده
است مت و سکون تانی از حرادگنتان اعد عا
آرنج - و انجمن و مجمم و جمعیت مردم راهم
گفته اند - و در عربی دیت و جريمهٌ جراحت
کردن باشد - و بدی افکندن میان مردم و بر
ان
---
```


## [2026-09-05T06:14:21.147Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v1_pages.txt | head -3\necho \"---count leaves---\"\npython3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(t.split(chr(12))))\"",
 "description": "Check BQT v1 page structure"
}
```


### [2026-09-05T06:14:22.905Z] TOOL RESULT

```
---count leaves---
777
```


## [2026-09-05T06:14:26.130Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:220 2>&1 | head -60",
 "description": "Fetch Borhan page 220"
}
```


### [2026-09-05T06:14:27.846Z] TOOL RESULT

```
no scan of BQT covers printed page 220 (see 'scans' in refs_online.json)
```


## [2026-09-05T06:14:30.188Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Show BQT ref config"
}
```


### [2026-09-05T06:14:31.827Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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


## [2026-09-05T06:14:35.959Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(436,444):\n    print('#### leaf',i)\n    print(t[i][:1400])\nEOF",
 "description": "Print Borhan v1 leaves around p.220"
}
```


### [2026-09-05T06:14:37.704Z] TOOL RESULT

```
#### leaf 436
با
خوانند و آنراکبوتر بیار دوست دارد . 9
پاار لك - بکر تاكث و سکون کاف ؛
مشفف باريك است که در مقاب لکنده باشد .
بار گاه - بروزن‌چار گاء.خیم‌پادشاهان
و سلاطن را ااگو, بند وجای رخصت واجازت‌باشد
و شکم حیوانات ماده را هم گویند .
باد گی » ختح ثاك بر وزن خانگی .
نوعی از اسب باشد » و بعضی اسب بالانی‌بار کس
,اگفته‌اند ٩‏ - ویمعنی قدرت ونوانایی هم هت
و روسییی و قععبگی را ايز گویند .
اد گیر - با رابم بتحتالی‌رسده وبراق
فرشت‌زده ۰ اسب و شنر وامثال آن باشد ازبرای
بار تردن و سواری و ارت مکی دادن ۴ -
و هودج و عماربرا هم کقنه‌اند - وماد#هرحیوانی
را نیز گویند .
بار گین » بکر رابم وسکون تحتانی
و اون » آبگر و تالابی را کوبند که در عبان
شهر و ادرون ده باشن - و جابی را نز گفتهاند
که زیر آب حملم ر مطخ و امثال آن در آن
جمح شود ۴ .
بار مان - بر وزن آرمان » نلم‌یکی از
بپلوانان ئوران است .
تجمل و حشمت و بزرگی باشد - و حنت نهادن
بر کسی - و پروانه وفرمان ورضا و رخصت‌دادن
باشد بدخول خانةٌ سلاطین - و بمعنی نازش
و مباهات - و لقب‌نيك وتفاخر + غرورهم‌هست
و بمعتی مدح و نعت هم بنظر آمده است.
بار نهادن - کنابه از زادن باشد .
بارو عه بر وژن جارو » حصار و قلمه را
گونتد . #۶
بارو د بادال » بر وزن و ععنی‌باروت
باشد که داروی تفنگه است: و بلخت سر بانی‌شوره
را گوبندکه جزو اعظم باروت باشد و آنرا نمك
چینی هم گونند ۴
بارود نه - بتح نات و زای هوز
و ون و سکون رابع » نلم فواٍبیست از موسیقی .
باروده » با زای حوز بر وزن پالوده.
خوراك و فوت‌هرروزه باشد- و ضروری‌وها:<تاح
هر روزه رانیز گویند از جامه و زبرجامه وامث
آن - و جامةٌ که
#### leaf 437
۲۱۷
طرز و روش ٩‏ -و قاعده وفانون باشد وعشرویی
را یز کنته‌اند مست کننده که آنرا از آرد برنج
وارزن و امثال آن سازند وحریی‌ابین خوانند ۲-
وهر چیز زشت را یز گویند- و بعنی زلف هم
هبت- و گله و رمة کاو و گوسفند واسب وامثال
آن باشد. و اسپ را یز گوبند که بعربی فری
خواند ؟ .
بارخ فهم - کنابه از فكك نهم‌است که
فكك‌الافلاك باشده و آترا بعربی عرش‌خوانند.
بادی ه بر وزن جاری ۰ نامیست از
نامهای خدابمالی جل‌جلاله ۴ و کاهی بر ملوه
و سلاطین. یز اطلاق کنند - و نام قصبه‌ایست در
حندوستان - و دیوار فلعه و حصار شپرباشد ۵ .
و از برای تقلبل و انحصار هم هست همچو التصه
همچو: یکباری ودو سه باری - و بمعنی گاهی
وایامی هم آهده ابت - و کمبتین قلب را نیز
گویند و هر چیزیکهپربار وسنگین‌باشد ٩‏ ۶
باد ون -بکس اكب و سکون‌نستانی
- ازاینباره گفتاربسیار گشت. قردوسی‌طوسی.
و فاف بواو رسیده و بنون زده ۰ بيونالي‌دوایست
که نرا شو کران‌خوانند» وآن نخم بینروهیست»
و از تفت که از ولایت بزد است آورند و آنرا
دوري تقتی کویند .
پا » بر وزن از , پرنده‌ایست مشهور
و »مروف که سلاطین و اکابر شکار فرمابند ۷ -
و کتادکی میان هر دو دست را نیز گومند چون
از هم بکثایند و آنرا نیز بترکی قلاح خوانند
و بحربی ماع کوبند ۸ و باین معنی با زای
فارسی‌هم آ مدهاست - و شبر و وجب رانیز کفته‌اند
و آن مقداری باشد از دست صاین ح انگشت
کوچك وانکشت‌شمت و دوش و بازو ؛ و مك‌بند
انگشت را یز گویند- وبمعنی تکرار و معاودث
و دیگرهم هست ٩‏ چنانکه کوشد: «بازیگو»
بعنیمکرربگو و«بازچه میگوید؟» ,عنی‌دنگرچه
میگوید؟ - و بازنده و بازی کننده را ی زگویند
همحو: قمارباز و رسمان‌باز
#### leaf 438
با ۱ - ۷۱۸ -
و باع و قلاح راکوند . وآن مقداری باشد از
سرانگشت میانین دست راست ناسر انگشت‌میافین
دست چپ وقترکهرستهاراازهم بگشایند ۴ - وجمعنی
دوشو بازوویك‌بندانگشت‌هم‌همت ۴ -وخاموشيی
باشد که فان در وفت بدن شستن وچیزی‌خوردن
بعد از زمزمه آختبار کنند ۴ ونام فربه ابست
از قرای طوی ومعرب آن فاز است . گویند تولد
۱ حکیم فردوسی از ] تجاست .
پاد اه با زای بالف کشیده . نود استیی
باشدبموجب‌قرارداد زراشت‌بهرام ۵, وهراسنیری
چهارمتفال است -٩‏ وبممنی دیگر ییا هم هست
یمنی بازیا . *#
باز آزردن. کابه از فابدث خاط
خواه کردن باشد ۷ . ۱
باز ار خاك - بکررای‌بی‌هطه وخای
قض فراز باشد - وبازماندن و واماندن بمعنی
طرمیدن هم هست- و بمعنی تمیز کردن وغرقه
لمودن میان درچیز باشد - و پمعتی جداه‌عت
_که بربی فصل کوبند - و بمعنی عکس و قلب
نیزآمده است - وشراب راهم میگوبند که‌بعریی
خمر خواشد - و سوی و طرف و جالب را یز
کنته اند - و پیعتی گذر کاه سل هم آمده
است - وباج وخراج‌را لیز کویند, و باینمعنی
بازای فارسی هم‌درست ات
باز س بنزای فارسی » بروزن و «حنی‌باج
و خراج باشد. و آن زرست که زبر دستان از
زبردسان گپررند بمنی پادشاهان یزركك ازیادشاهان
کوچك‌سنانند ؟ ؛ومالیکه حکام از رعابا وراهدار
از سودااگر گرند - و جزبه را نز گفته اید»
وآن زری باشد که ملمانان ازکافران‌یگ ود -
ن‌ بازار - در پهلوی و [در: هوحتان واچار ‌ سوق‌الاحواز ۰ رك 0 خوزستان ]
( یز 02227 .م ) » فریزندی ویریی 2286 , نطنزی 9202۲ «ه . ۱ص ۲۹۰ > , ممنانی
۲ منگری ۷۵28۲ , سرخه ؛ لاسگردی و شهمیرزادی 08226 « د . ۲ ص ۱۸۸
استی 08226 ده . استی 6۱۱4 ؛ محل خرید و فروش‌کالا وخ
#### leaf 439
نشطه‌دار بالف کشیده و یکاف زده » کتابه ازقالب
آدمیست - وعظمت بشریت رالیز کویتس وکنابه
از رونق اور دنبوی و اخروی باشد .
بار ار گان ۱ - ب کاف فارسی بالف
کشیده و بنون زده » سودا کررا کویند .
باز اکن بافا و کاف بر وزن‌مادرزن,
ژنده وینه‌ای باشد که فقیران ودرویشان برجامه
و خرقه دوزند - و مداخل مانندیرا نیز کویشد
که بضی از سپاهیان‌بریشت گربان جامه‌ینبهدار
و چارقب دوزند چنانکه سر مداخل بر میان هر
دوشانه افتد .
باژ بان ۳ - بازای فارسی و بای ابجد
پروزن کاروان » شخصی که باج و خراج از مردم
و ۳7 و اورابازداره میگویشد وطا نقه‌ای باشند
از ترکان .
باد پیج بروزن‌مارییج.مهرچندست
که بر ربسمان بندند و از بالای گهوارة اطفال
آویزند تا اشان بدان بازی کنند» و آترا بعربی
داداة کوند ؛ ویضی کفتهاند چهارچوب است
و بر آن تخته باجامه‌ای وصل کنند که بمنرلة
کهواره باشد اطفال را - و رسمانی را نی زکویند
۰ بازدار
که در ایام جشن و عید از جایی آویز هد و زنان
ر دختران بر آن نشته در هوا آیند: وروند .
ربامن‌معنی بجای بای‌فارسی بون‌هم آمدماست؟ .
یار خشیی . بکر اك و قح خای
نقطه دار و شین فرشت بتحتانی رسیده و بنون
زده » نوم از بازباشد که پشت‌آن سیاه و ثیره
ريك و چشمهایش سرخ بود.ه و این قس باز ا
نرکان قزل قوش خوانند ۴ ۰
پاز خمید ‏ بکس میم وسکون‌نحنالی
و دال , کیکه بسوان طعنه صدارت کی کند
و یکنابه مشن شخصی را یاز نماید کوبند « باز
خمید » یمنی بطمنه سخن او را کفت و صدارت
او کرد .
باردار - بر وزن رازدار ۰ برزیگر
و زراعت کننده را گوبند - و میرشکار و صیاد
ونگاه دارندث باز را عم کقته‌اند ٩‏ - وشخصی را
نیز کوب دکه مردمرا از کاری
#### leaf 440
برداعتن
مردم میگیرد .
باز داشتی - کنابه از :ان کردن
ومنم نمودن باشد ۷ .
بان - بای نرسی و دال یبد بر
وزن پاسبان » ظرفی‌را کوبند که زر باج ی که از
مردم میگیرند در آن ریزند .
پاز ر گان - بتح‌اك. مخنفبازارگان
است که سوداگر باشف ۲۳
اد فك » بر وزن باربند » سینه بند
طفلان و پتان‌بند زانرا گوبند .
باژر نگ - با کلف‌فارسی» بر رزنومعنی
باشد .
باز سفید در . کنابه از آفتاب عالمتاب
است . ۱
دار بالف کشیده » فوت ممیزه انسالی را گونند :
باژ گو نه - بازای فارسی . بر وزن
و معنی وا گونه است که بمربی عکس و قلب
کویند - و نصی و امبارك را نیز گفته‌اند »
وبازای هوزهم درست است .
باز گیر - بازای حوز بروزن بلدگیر »
مردم تلریخدان و تارسخی و مورخ را گوبند .
باز مان » بروزن آسمان » بمعنی‌توقف
باشد - و آمر بدینممنی هم هست معنی موفوف
دارو توقف کن
ل
ان - بختح زای‌فلرسی وسکون نون »
۷۷0 ات
کوسفند با بزبراکوبندکه پیش پیش کله براه
رود و بمربی کراز خوانند ۴ .
باز نیچ ۴ - با زای حوز و نون بروزن
بازپیج » رسمانی باشد که در الم عید و جشن
از جابی آویزند و زنان و دختران بر آن شته
در هوا آیند و روند ۵ .۴
باز و دادن » کنابه ازداری‌دادن ومدد
کاری کردن‌باشد .
بار و درار مردم دراژ دست باشد -
وکنابه از الب ء مسئولی شدن و دراز دستی
باژ و د - بروزن کافور , نلم جادو گری
بوده از توران که بسحر و جلدو لشکر ابرانرا
شکست داد و عاقبت بر دست رهام بن کودرز
که کد .
باه - بنتح ناك » مقدار کشاد کی‌میان
هر دو دست را گونند چورن دست ها را از حم
بکشابندوآنرا بعربی‌باع وبتر کی‌قلاجخوانشد ۷ -
و فاسلٌ میان دودیوار و دوکوه را نیز گوین دکه
عبارت از ک
#### leaf 441
اک
بار یجه‌رو م ود نگ - سخرتروز
و شب را کونند - و کنابه از دیا و روز کار هم
حست باعتبار شب و روز .3۶
با د ثر ۵ - باتحتالی‌مجمول بروژن‌کاجیر»»
خصه و یرای از شب باشدچنانکه اگر کویند :
«بازبرة اول وبازبر؛ آخر» » مراد از آن پاره‌ای
از اول شب و باره‌ای از آخر شب مود .
بار توش سِ باکاف فارسی‌بو او رسیده
و شین نقطه دار زده م, کنانه از شوخ و که
باشد .
باس - بروزن طاسی » بمعنی قدیم ناش
گویند ؟ - و بمعنی قوت و قدرت » عریست
پاسیو س ۰ با بای ابجد بروزن آبنوی:
توعی از ربحان باشد که آنرا مرزنگوش خوانند
و بمربی آذان‌الفار گوبند .
باستار و یستار - از الفظ متتاسه
است همحو فلان و همان 4 و استعمالش در اوصاف
را جدا جدا استعمال میکنند باستار و بستار را
نیز جدا جدا مذ کور میه‌ازند ۳ .
باستان ت‌ِ مروزن‌داستان . گیندو کته
و قدیيم و دیرنه را کوبند ۴ و کنابه از دبا
و عالم و دهر و گردون هم هست - و بزبان‌دری
باشامه .
تاریخ را کویند که احوال پیتینیان باشد 9 -
و بمعتی مجرد هم‌بنظر ؛مده که از ترك وتجرید
باشه ۷ .
پاستان‌نامه پانون بالف کشیيده‌وميم
مفتوح . نام کتابیست از تاریخ فارسیان ۷ .
باستی بروزن‌راستی ؛ بمعتی‌افتاد کی
و فروتنی باشد .
باسر ۸ - بفتح رای‌قرشت وسکون‌يم »
زمینی را کون دکه بجهت کشت و زراعت کردن
آماده و مهیا کرده باشند - و کشت زار را نیز
کوشد ۸
پاسر ه ‌ بفتح‌ثالث وربع ء کشت‌وزراعت
را کوند » و بسکون اكك و کر الث هم بنظر
آمده ات ٩‏
پاساث - بضم تال وسکون‌کاف ,خمازء
و دهان دره باشد . و سبب آن خواب با خمار
باسگ بحوال‌دفتی -کنایه از
همخانه شدن با مردم بدخو و ممارض شدن با
هرزه کو باشد .
پاشام - بروزن آ
#### leaf 442
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
؟ ‏ همرة باز [ رك : با
#### leaf 443
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
اوسی میب وعمت ددگن عون ۵ ۰
با کسی دز بان‌داشتی « کنابه از
آنت که خود را بآانکس از آنکس وانمایث .
با گل- بنتح کاف فارسی و سکون لام ء
آب نم گرم را گوند
پا نك بروزن یازند ؛ با فوت‌را گوند
و آن جوهربت معروف ٩‏ ,وبا بای فارسی عم
عنی آخرین:
. #سنی : بعاقیت .
دارای کلها
```


## [2026-09-05T06:15:05.320Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad 2>/dev/null || mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -sL -o bqt440.jpg \"https://archive.org/download/borhan-ghate-v1/page/n440_w1400.jpg\" -w \"%{http_code} %{size_download}\\n\"\nls -la bqt440.jpg; file bqt440.jpg",
 "description": "Download Borhan v1 leaf 440 image"
}
```


### [2026-09-05T06:15:09.368Z] TOOL RESULT

```
200 513902
-rw-rw-r-- 1 sfmqrb sfmqrb 513902 Sep  5 02:15 bqt440.jpg
bqt440.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-09-05T06:15:13.623Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('bqt440.jpg')\nw,h=im.size\nim.crop((0,int(h*0.72),w,h)).resize((int(w*0.7),int(h*0.28*0.7))).save('bqt440_bottom.png')\nprint(im.size)\n\" 2>&1 | tail -2; ls -la bqt440_bottom.png",
 "description": "Crop footnote area of Borhan page"
}
```


### [2026-09-05T06:15:15.634Z] TOOL RESULT

```
(2479, 3508)
-rw-rw-r-- 1 sfmqrb sfmqrb 189420 Sep  5 02:15 bqt440_bottom.png
```


## [2026-09-05T06:15:17.779Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt440_bottom.png"
}
```


### [2026-09-05T06:15:17.800Z] TOOL RESULT

```

```


## [2026-09-05T06:15:34.258Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bazm ===\"; grep -n -i \"bazm\\|banquet\\|feast\" PHD.txt | head -20\necho \"=== NYB bazm ===\"; grep -n -i \"bazm\" NYB_vol2_glossary.txt | head -10\necho \"=== BRT bazu ===\"; grep -n \"bāzu\\|bazu-\\|bāzāv\\|Arm.*bazuk\" BRT.txt | head -20",
 "description": "Grep MacKenzie/Nyberg/Bartholomae"
}
```


### [2026-09-05T06:15:34.324Z] TOOL RESULT

```
=== PHD bazm ===
256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
572:stün(ag) [stwn(k)!' | M 'stwn, N sutūn] column, pillar, mast. stir [sżwl] trustee, curator, guardian. ~ЛЬ : trusteeship. sturģ [stwlg | N suturg] fierce, contentious; gross, coarse. süd [swt! | M send, N ~] use, profit, advantage. sudab [st?*5 | N ~] rue. sūd-abģār [swt?fk'/] profitable. sūdaģ [swtk!] negligent, indolent. ~ih: negligence, indolence. sidan, sāy- [swtn', s'd- | N ~] rub. sūd(ö)mand [swt(?w)mnd | N sūdmand] useful. suft [swpt' | N ~] shoulder. suftan, sumb- [swptn!, swmb- | N ~] pierce, bore. sumb [swmb* | N ~] hoof. isūr [sw] | M swr, N ~] meal, feast, banquet. *sür [sel] strong. sūrāg [swl(?)k'] hole, burrow. ~ig [-yk'] burrowing (animal). ««Omand (-'wmnd] holed. sūrāx [swPh | N ~] hole. sust [swst! | = M, N —] slack, lazy. ~ih: slackness, laziness. Iguš [swš | (N šus)] lung. *suš [stw$] degree (of arc). suxr [swhl | N surx] red. suy [swd | M swy-] hunger. *swahistan, swah- [swh-stn' | P swh-] sigh. sya [syd? | (P syw, N styah)] black. ~hag [-hk' | N -a] pupil (of eye).
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
1147:canapé bazmawurd.
1904:feast bazm, sir.
2736:marriage zanīh; — feast wayēdagān.
2755:meal bazm, čāšt, mézd, sir; evening ~ $am.
=== NYB bazm ===
=== BRT bazu ===
```


## [2026-09-05T06:15:41.720Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"bazu\\|bäzu\\|bâzu\\|bazav\\|bäzav\\|Arm\\b.*bazuk\\|bazuk\" BRT.txt | head -20\necho \"=== 956 ===\"\ngrep -n \"^956\\|Vorderarm\\|Oberarm\" BRT.txt | head -20",
 "description": "Grep Bartholomae for bāzu"
}
```


### [2026-09-05T06:15:41.775Z] TOOL RESULT

```
5388:auniäa.bäzav-
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
6617:daHtaya  .  .   urukwan  V.J. 30;  Vt.j.if.',  bäzava  Ytj.?;  —  ydhaca  .  .  ßtäna  .  .
7945:mä:uiayasmm  frapinaeiti  V.  ^,  3 1 ;  —  urva- "iamlit  ziayemi  avt  •mai  varS  Yl  12. 3 (vgl.  12.4,  wo  avat);^  °mal  iimltum  yaol- diiiätu  .  .  'map'>  ätram  .  .  "mat^  apim . ,  °mat^^  zqttt  ,  .  °maO^  gqm  .  .  *maj^' un-arqm  .  .  'mat>^  nartm  asava/um  .  . 'mal^  näiriiqm  V.  ij.4— 7 ;  —  'm^rn  hao- m?m  .  .  äyese  yesti  'mqmca  gqm  .  .  °mä zaoira  .  .  °tnq  asmqsca  baoioTmfa  Y.  22. 1-3;  >.  3.  2.'i*.  ^.4,  4-i\  3.  ^ö-i.  GS. 14.  7^-23;  —  {ävaihayama/it)  'mq  kaomq 'ma  haomya  'ma  stania  "ma  myazäa  "ma asma  .  .  'ma  (AD.)  asmana  Aävana  .  , 'ma  ayaahama  Mvana  .  .  °mqm  Sp)m  .  . 'inat  barasma  .  .  °ma  kihrpasca  DvTslsca 'mH  ..  :ao^ra  "mrm  haomim  Vr. //.  at; —  paiti  ti  trarrfa  .  .  'mä  srvä  va^a- yemi  .  .  °mäs>  tE  srvä  m»yya  .  .  kyHr? arstayasca  Y.ij.g;  9;  —  'iru>m  U  nanm nisrinaomi  V.  /i".  5 1 ;  5 1 ;  —  D  °mam  psrsam ksram  psdiy  yadiy  karJ'  parstr  pst<^ ahatiy ..\i.$.y,—<^urJ'mttzäSmaiy  upasläm abarc/'  yätä  °mt^  xio^j^am  adäry  voinil (^uri^masdah!^  °«ni*  xia%''am  dilrayämiy Bh. /.  9;ll —  nSit  °mal  vTsp>m  düivarstsm .  .  mObrS  vaenaiti  Yt  ro.  10g.  a)  sub- stantivisch: D  draug^dif  hami'h''iyä  aku- nat^ ty(^  'maiy  karam  adurujiyasti'"..yie^ die  hier  (näml-  die  abgebildeten  Empörer) das  Volk  belogen  haben"  Bh.^.  4 ;  —  'me  nö ..aspapara.-nay enteist.)  'me  nS..*bäzava sHndayänii  (sd.)  Yt. /0.4z.  a)  mit  einem erläuternden  oder  ergänzenden  Relativ; a)  adjektivisch:  -mat  karhara  yät  ifani- ra>>m  Y. 57.31,  Yt  70.15,  133,  JB.15, H.  /.  14;  —  alis  .  .  rämyat  im  upa  'mal nmänsm  yat  äküiri  Y.  10.  i ;  —  ima  asäsca sOdrasca  . .  'msm  sBdrahe  paüim  ytm ahunm  Y.  2.16;  —  °mqm  dasriqm  yqm sAäirfm  YtÄgg;  —  'mqm  .  .  tqm  . .  yä nS  baraitt  Y.jS.i;  y.i;  —  vTspä  'mä 3ps  ys  amä  patti  /rataSnii  Y.  (»5. 3 ;  — 'mqm  tanüm  yä  ml  vaSnaite  huraoha  Y. /o.  14,  ß)  substantivisch:  vispgm  'mal
8118:•  j.  Ujra.bäzav-  Adj.  'starkarmig':  {iiit^r?) ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]
8376:•  j.,  p.  upa-stä-  f.  "Beistand,  Hilfe':  vtsta- spähe  . .  yd  bäzusca  °taca  vuata  ..  dalnaya Yt. /J.  99;  —  \  t^urt^masdamaiy  °tam <^ar<^  Bh./.g,  13,  18,  19,  2.6— la',  14, ^  .  3,  6,  7,  9,  10,  14,4.12,  0.7.5;  Bh. .^.13;  —  1  mann  </'ur<^mazda  'täm  barattn' fiadä  .  .  bagaibii  D.  ^.  3 ;  —  nRnm  me bara  'tarn  YL5.63;  —  ya'i^a  ml  barm 'tarn  .  .  fravasayS  Yt.  y,  i ;  — yd'A  2I  mS nsit  daiüft  'tarn  Yt/3.  la;  —  vT'iärayäti 'tqm  m^rr/ahe  pannB  Yt,  74.36;  —  th  .. °lqm  hittti  dähista  (sd.)  Yt.  13. 1 7.
8661:•  j.  uz-bäzav-  Adj.  (auch  masfc.)  'die Ajme  emporhebend';  °zäus  (NS.)  fiaiii attunxllm  (sd.) /ravazai/e  mi^rS  Yt,/o.ia4.
10461:mit  frä  i)  'ergreifen':  mürpin  .  .  y?>ihe ..bäzava  fragrnvmti^''''  (stattDu.)  "»nürg.- aojattAs  (sd.)  Yt.  10. 104.  3)  'annehmen, entgegennehmen':  ßra  atnisH  spmts  gJ^ii giurväin ' sl  Y. 2S.0.      fragSun-ayat Vd.  13.
10464:x^anns  kaiigpr^fsäiie  Yt./p.47,  51  (wo grif"');  —  t?Miil  mi'irS  hangr»fs)mnS *pairi.apaya  (sd.)  bäzuwe  Yt.  lo.  105; —  aom  :^armS  hangSurvayala  Yt.  i(). 35.  a)    mit    den   Sinnen:   yat    '^wä
11373:—  daryyaäi"'>  bäzava  Yt  70,104;  — pourucil  ü^aAe  N.  6^;  —  *vanaite  akimat man3  Yt.  ig.  g6;  —  aspaat  ysi  mi%rö.- drujqm  .  .  Yl  10.  20;  Aog.  4^;  —  karsas- Ht  frakaraysis  Y.g.  10;  zit  *Y.y,  — autark  *kä%rwtHi  N.  /09;  —  tarS  p>rp- tümcit  Y.ig.6;  —  Aandarpzaat  /landar?- zaym  V.(?.  49;  —  urvähqmät  zbayant avi  . .  Yl  12.  3;  —  ianvasAf  :^ahya  uita- n?m  Y.  jj.  14;  verwendet  Y.  1/.18,  /j.4;
12246:spähe  kihrpa  aurusake  .  .  äal  paiti avaiti  .  .  avi  zrayS  vourukasttn  .  .  ä  äim paüi.yq^  nisdvaraili  daevS  yS  apaoiö aspahe  kfhrpa  iümahe .  .  kam  läcit  bäzus barats  . .  'ryaica  . .  -vasca .  .'täyüitya%ö  . . a    rapi^winfm    srvämm    ä    Mm    bavatli
12894:')  Ein  Schönheitsieichen;  vgl.  Artaxerxts  L Beiwort  Longimaiios,     S.  in  dar>-fö,bäzav-.
12906:darttgö.bazav-
12909:•  g.  darsgö.bäzav-,  j.  dar^ö.bäzav- Adj.  (auch  fem.)  langannig':  hukmlB  ahi
17111:hangnwnäiti  .  .  *As  *'mya  xsagtäi  "den  •  j.   bäzu.jata-  n.    Tenn.  techn.  fiir  die
17125:•  j,  bäzav-  m.  i)  'Ann'  der  Menschen  und       '  5'  '*     ..  ..r,    _  .   i-n^    ,  *j:  -.^  « i-M^         i-,   -r  ,/TL'      .    Tc-v.i   j   <■      ■         Komp.  mit  ND.  im  l,  Glied;  s.  ituan-  A. Gotter:  ÄJtJv« '«i'jfLb.  als  IS.)'' j(jn«aiv)        .     /_      ■      v  ^      .  j-     (^    .     -       j ./aÄ«.-«.ä*te.«,*5,"milde,»li,JimAnn  •   !■   bs^-s-aolah-   Ad,.    Oak    m    den «.d  dem  «cht«,  mit  de«,  rechten  Ar»  m,d  '^f  "»  *^'  "^'  '""• '  -»ß-»«. . . deoh»kei."V.j.>5i-j...,yü!j»,,;7™i,  V»«"!'"  '?*''/'/?;  \t.,o.,y,-«-a^,aAr
17667:frabäzu.dräjah-
17674:•  j.  fra'bäzu.dr^ab-  n.  'Länge  eines FrabStav*^ :  frära%m.dräj5  yat  naptanqm °/s  yat  kuikanqm  (nänü.  aismanam)  "in der  Idnge  eines  Fmr.  von  feuchten,  in der  Länge  einer  Frad.  von  trockenen (Hölzera)"  V.  7. 33,  34;  30.
18268:•  j.  frl'riflmdräjah-  n.  'I.änge  eines  Fr. (Elle)'*':  °Js yai  hulkanqm  frabazu.dmjö yat  naptanqm  "in  der  Länge  eines  Fr. von  trockenem,  eines  Frab.  von  feuchtem Holz"  V.  7. 30,  33 ;  29,  5.  4  PiiZ.3;  —  *"> N.  10  j  ".
=== 956 ===
12558:•  j.  daoä-  m.  'Oberarm,   Schulter":    "Ä
12559:(ND,)F.  _3g;  —  cvat  na  *mt?>na  alsmahe (sd.)  paitiiarS  ratufriii  yaha  vansnahe kihrpahe  äSus  (NS,)  ".  •  (so  gross)  als  der Oberarm  eines  Mannesleibes"  N.  S06;  F. 14"-
12560:ai.    ddf-   in.,   n.  'Vorderarm';    mp.  (Fa.),   np.
```


## [2026-09-05T06:15:50.734Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls MON*; echo \"---\"; grep -n \"بزم\" MON_part1.txt | head -10; echo \"=== بذله ===\"; grep -n \"بذله\" MON_part1.txt | head -10; echo \"=== بهادر ===\"; grep -n \"بهادر\" MON_part1.txt | head -10",
 "description": "Grep Mo'in for bazm, bazleh, bahador"
}
```


### [2026-09-05T06:15:50.819Z] TOOL RESULT

```
MON_part1.txt
MON_part2.txt
---
2569:بزم...) شاد کردن» مسرور کردن: دل شاه 
5223:آب آورد» ناد آورد؛ بزم آورد» راه آورده 
7765:بزم کردن. 
9293:شروع می‌گردد. اراد آهنین: عزم جبزم و 
23136:بزم: ۳:۲0 (!) مسجلس شراب و طرب و 
23138:انس. خیمه و سراپرده. بزم سنگین: بزمی که 
23141:بزم‌ارای: 027201-۷ [ - بزم آراینده] (افا.) 
23143:می‌کند» بزم آرا. 
23145:بزمان: ,02 ,0220050 (ا.) میل و خواهش. 
23149:بزماورد: 02701-310 (.) گوشت بخته و 
=== بذله ===
58177:نیکو طبیعت. بذله گو» شیرین زبان. خوش 
87048:خوش طبیعت» بذله گو. 
93721:طبع» نکته‌سنج. بذله گوی. زیباه خوشگل) 
=== بهادر ===
23179:سزن‌بهادر: ۷-۲ آف. تسر.] 
26301:بهادر: ۲ اآتر.] (رص.) و دلاور» 
62736:دلیر: -0۱ (ص.) دلاور» شجاع» بهادر. 
83545:(امر.) سوار دلاور. بهادر» پهلوان جنگجو.
```


## [2026-09-05T06:15:54.086Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23130,23160p' MON_part1.txt\necho \"===== bahador =====\"\nsed -n '26295,26310p' MON_part1.txt\necho \"===== bazleh headword search =====\"\ngrep -n \"بذلة\\|بذله:\" MON_part1.txt | head",
 "description": "Read Mo'in entries"
}
```


### [2026-09-05T06:15:54.180Z] TOOL RESULT

```
چلیاسه» وزغه» مارمولک. 

بزک: مهد (.) زینت و آرایش عموماً و 
آرایش زنان خصوصا توالت. 

بزک: ۱07-6 (ا.مصف.) بز کو چکک؛ بز یچه. 
بزم: ۳:۲0 (!) مسجلس شراب و طرب و 
مهمانی و ضیافت. محفل و انجمن و مجلس 
انس. خیمه و سراپرده. بزم سنگین: بزمی که 
در آن مردم بسیار جمع باشند. 

بزم‌ارای: 027201-۷ [ - بزم آراینده] (افا.) 
آنکه مجلس عیش و مهمانی را آرایش 
می‌کند» بزم آرا. 

بزمان: ,02 ,0220050 (ا.) میل و خواهش. 
(ص.) مست و انسدوهگین» مسخمور و 
بی‌دماع. 

بزماورد: 02701-310 (.) گوشت بخته و 
سبزی و تخم‌مرغ پخته است که در نان 
بیچند و با کارد قطعه قطعه کرده و خورند. 
گوشت پخته و تره و خاگینه باشد که در نان 
تنگ پیچند و مانند نواله سازند و با کارد 
باره باره کنند و خورند: لقمه القاضی» 
قاضی» ساندو یچ. 

رمحه. (0-)2 ۱۵2۵0211 [- بژمژه] (ا.) 
(جان.) سو سمار. 


===== bahador =====

ب‌هاء: 8 (ع. ف. بها] (.) روشنی» 
درخشندگی» رونق. زیبایی» نیکویی. زینت» 


آرایش. عظمت؛ کمال. فر» شکوه فره. 
بهادر: ۲ اآتر.] (رص.) و دلاور» 
شجاع. 
بهار: ۰ (.) اولین فصل سال» ربیع. 
شکوفة گل هر درخت. (گیا.) گیاهی از تیه 
مرکبان که چهار گونه از آن شناخته شده, 
گل‌هاش زرد رنگ و در کوهستان‌های 
اروپای مرکزی و جنوبی و آسیای غربی و 
مرکزی می‌روید و به عنوان گل زینتی نیز در 
باغ‌ها کاشته می‌شود؛ گل گاو چشم اقحوان 
اصفر. (مس.) یکی از دستگاه‌ها و ادوار 
===== bazleh headword search =====
```


## [2026-09-05T06:16:04.234Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"بذل\" MON_part1.txt | head -20; echo \"=== part2 ===\"; grep -n \"بذل\" MON_part2.txt | head -10",
 "description": "Grep Mo'in for بذل"
}
```


### [2026-09-05T06:16:04.312Z] TOOL RESULT

```
20051:بادل: اعتةه [ع.] (افا. بذل) بذل کننده 
21789:بذال: اقتتهه [ع.] (ص.) سیار بذل کننده» 
58177:نیکو طبیعت. بذله گو» شیرین زبان. خوش 
87048:خوش طبیعت» بذله گو. 
93721:طبع» نکته‌سنج. بذله گوی. زیباه خوشگل) 
=== part2 ===
39479:رفتاری؛ نیکویی» نیک وکاری. کرم؛ بذل» 
39499:معاشر ت» بذله گو. 
39503:باریک و نیکو نکته. بذله. شوخی. نکتة 
41502:لیم: ((ص.) شوخ و ظریف و بذله گو. 
42345:بذله گو. 
44689:بذل کند چون اختلاف دو طرفی است. ثانبا 
59033:سخنان خنده آور؛ لطفه‌هاء بذله‌ها. 
63343:کور بذلیون آفریقاء گلگل. (گیا.) صمغ 
65152:دهد. مسخره» بذله گوی» مقلد.
```


## [2026-09-05T06:16:18.160Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T06:16:18.165Z] TOOL RESULT

```


```


## [2026-09-05T06:16:21.897Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%BA",
 "prompt": "Give the full Persian etymology section for باغ (bāġ) 'garden': Middle Persian form, Proto-Iranian/Old Iranian reconstruction, cognates, and any cited authors (Hasandust, Cheung, MacKenzie)."
}
```


## [2026-09-05T06:16:23.375Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B2%D9%85",
 "prompt": "Give the Persian etymology of بزم (bazm) 'feast, banquet': Middle Persian form, Old Iranian reconstruction, cognates and cited sources."
}
```


### [2026-09-05T06:16:28.496Z] TOOL RESULT

```
# Persian Etymology of باغ (bāġ)

Based on the Wiktionary entry, here is the Persian etymology:

**Middle Persian Form:** bʾg (transliterated form from Pahlavi script)

**Proto-Iranian/Old Iranian Reconstruction:** The word derives from Proto-Iranian *bāgáh, which came from Old Persian *bāgah

**Further Origin:** This traces back to Proto-Indo-Iranian *bʰāgás, ultimately from Proto-Indo-European *bʰeh₂g- ("to divide, distribute, allot") plus the nominal suffix *-ós

**Cited Authority:** D. N. MacKenzie is referenced in the Further Reading section for his 1971 work "A concise Pahlavi dictionary" (Oxford University Press), where he documents "bāɣ" as the entry.

The entry notes this is an "inherited" term in Persian, tracing a continuous lineage from Middle Persian through Old Persian back to ancient Indo-Iranian roots, rather than a later borrowing.
```


### [2026-09-05T06:16:32.705Z] TOOL RESULT

```
# Persian Etymology of بزم (bazm)

Based on the Wiktionary entry provided, the etymology section states:

"Akin to Old Armenian բազմիմ (bazmim), an Iranian borrowing."

The article does not provide:
- A Middle Persian etymological form
- An Old Iranian reconstruction
- Additional cognates beyond the Old Armenian reference
- Specific cited sources for the etymology (the Persian section lacks reference citations)

The entry suggests the word has Iranian origins, as evidenced by its borrowing into Old Armenian, but stops short of reconstructing earlier forms or providing comprehensive cognate evidence. For more detailed etymological information, consulting specialized historical linguistics sources would be necessary.
```


## [2026-09-05T06:16:40.262Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Persian bazm etymology Middle Persian bazm feast Armenian bazmim Iranian *bazma-"
}
```


## [2026-09-05T06:16:42.163Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1",
 "prompt": "Give the etymology of Persian بهادر (bahādor) 'hero, brave' — source language (Mongolian/Turkic baghatur), and any discussion of alternative origins."
}
```


### [2026-09-05T06:16:46.678Z] TOOL RESULT

```
Web search results for query: "Persian bazm etymology Middle Persian bazm feast Armenian bazmim Iranian *bazma-"

Links: [{"title":"ARMENIA AND IRAN iv. Iranian influences in Armenian Language - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/armenia-iv/"},{"title":"Iranian-Armenian language contact in and before the 5ᵗʰ century CE","url":"https://ora.ox.ac.uk/objects/uuid:38e2dcfa-4051-4e5f-a761-844526cc6449/download_file?file_format=pdf&safe_filename=Meyer_DPhil_thesis_deposit.pdf&type_of_work=Thesis"},{"title":"Bahmanag%C4%81n","url":"https://en.wikipedia.org/wiki/Bahmanag%C4%81n"},{"title":"Bazm and Razm: Feast and Fight in Persian Art - The Metropolitan Museum of Art","url":"https://www.metmuseum.org/press/exhibitions/2015/bazm-and-razm"},{"title":"Bazm and Razm: Feast and Fight in Persian Art","url":"https://www.metmuseum.org/exhibitions/listings/2015/bazm-and-razm"},{"title":"باز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2"},{"title":"Meaning of bazm | Rekhta","url":"https://www.rekhta.org/urdudictionary?keyword=bazm"},{"title":"Bazm","url":"https://en.wikipedia.org/wiki/Bazm"},{"title":"بزم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%A8%D8%B2%D9%85"},{"title":"Bazm u Razm","url":"https://en.wikipedia.org/wiki/Bazm_u_Razm"}]

Based on the search results, here's what I found regarding the etymology of Persian "bazm":

Armenian "bazmim" ("I sit down to dinner") derives from Parthian and Middle Persian "bazm" meaning "meal, feast." This illustrates how the word entered Armenian through contact with Iranian languages.

In Persian culture, "bazm" (feast) is an ancient concept with roots in pre-Islamic Iran, reflecting its deep historical significance in Persian civilization.

The search results show that this etymological connection between Persian, Middle Persian, Armenian, and other Iranian languages demonstrates significant language contact between the Armenian and Iranian linguistic spheres, particularly in vocabulary related to social and cultural practices like feasting and dining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-05T06:16:47.422Z] TOOL RESULT

```
# Etymology of Persian بهادر (bahādor)

The word originates from **Middle Mongol** *ᠪᠠᠭ᠋ᠠᠲᠤᠷ* (baɣatur). According to the Wiktionary entry, it was "borrowed from Middle Mongol," with attestation appearing "after the Mongol conquest in the 1200s."

The document does not discuss alternative origins or compare Mongolian versus Turkic sources. The etymological information provided focuses solely on the Middle Mongol root, establishing the word's introduction into Persian following the 13th-century Mongol invasions.
```


## [2026-09-05T06:17:24.593Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG baj ===\"; grep -n \"\\*baj\\|baj-\\|\\*bag\\b\" CHEUNG.txt | head -20\necho \"=== ARY باغ/بزم/بازو ===\"; grep -n \"بزم\\|بازو\\|^باغ\\|باغ:\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Cheung and Aryanpur"
}
```


### [2026-09-05T06:17:24.657Z] TOOL RESULT

```
=== CHEUNG baj ===
532:*-so, e.g. *рах ‘to divide, apportion’ (cf. *baj ‘to divide’), *Hraxs ‘to protect, 
1415:*baj ‘to bestow, divide, have a share; to give, apportion’ 
1443:*NEIR: Yzgh. veZ ‘partner (in hunting, sharing the bag made)’ (< *bajia-), Wanji wej 
1447:stierne, Le, but rather from the root *baj, on which see ESIJa II: 57. In addition, the 
1485:*baj 3 
1534:*baj ‘to break’ 
2522:formation *b"(e)H>g-s’/,- ‘to wish to divide’ of *b'ag"- ‘to get a share’ (*baj). The 
11830:2001-2002: 36: *iaya-baja- ‘barley breaker’ (see *baj). The reconstruction would be 
20921:forms for instance is shared with notably *baj and *braj. = LIV: 415 f. | Pok.: 686 
55205:*baj, *baxs 
55762:*baj, *baxs, *nau (s.v.) 
55794:*baid (s.v.), *baj, 
56327:*baj (s.v.) 
56350:*baj, *baxs, *daH° 
56634:*baj (s.v.) 
56732:*baj, *daH' , *HraH, *parH° 
56791:*baj, *baxs 
56898:*baj (s.v.), *dar', *dra(n)j, 
57094:*baj (s.v.) 
57219:*baj (s.v.), *dars’ (s.v.), *hau 
=== ARY باغ/بزم/بازو ===
1108:خط نویسی» افسانه‌ها و تاریخ مردم خود را در حافظه‌ی خود جا داده و در بزم‌ها یا مراسم رسمی با
1115:(110178۸0078) شعر عشقی يا رزمی می‌سرودند و در بزم‌ها با صدای آهنگین می‌خواندند..
6682:۲ چم این واژه در اوستی: بازو,
7487:چم این واژه در زبان آلمانی: بزم برپاکردن.
8492:چم این واژه در برخی زبان‌های هند و اروپایی: بازو» ساغد.
10633:آلمانی میانه (02744 بزم/ز صام): 7 را ۶00/000
12448:لاتین (4707ما): 0۸5 ,قاتا ماتا0 آلمانی کهن ((مانمعه بزماط ام
13473:چم این واژه در زبان لاتین؛ بازو
15223:چم اين واژه در زبان‌های ژرمنی: خوراکد» بزم
```


## [2026-09-05T06:17:28.253Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1415,1450p' CHEUNG.txt\necho \"==== ARY 6682 context ====\"\nsed -n '6670,6695p' incoming/ARY/ARY_pages.txt",
 "description": "Read Cheung *baj and Aryanpur bāzu context"
}
```


### [2026-09-05T06:17:28.309Z] TOOL RESULT

```
*baj ‘to bestow, divide, have a share; to give, apportion’ 
*AVESTAN: baZ- (baxs-) ‘to bestow, divide, give a share’ (cf. Martinez 1999: 128 ff.) 
|| (+ *4-) ‘to apportion, portion out’ = Liste: 37 


2 *baid 


Pres. ja (?): INJ. 3sg. YAv. baZat (Yt 19.8); Aor. s-: INJ. med. 3sg. OAv. baxsta (Y 31.10), SUBJ. 3sg. 
OAv. baxsaiti(Y 47.5, Y 50.3, ? Y 18.6), IMPV. med. 2sg. OAv. abaxsohuua (Y 33.10) 


«OLD PERSIAN: big- ‘to bestow’. Ф The interpretation of OP °bigna- is supported by 
MSogd. prbyn, a synonym of BSogd. pr-b’ytk, and Chor. Bynyk ‘good fortune’, cf. 
Morgenstierne 1971: 326. = Kent: 199a 

Partic.: perf. pass. °bigna- < °-b-i-g-n-> (DB 4.84) 

*KHOTANESE: buss- ‘to give, distribute’ || (+ *nis-) LKh. nasphaj- ‘to be obtained’ || 
(+ *ham-) ? LKh. hamphaj- ‘to hold’ = SGS: 103, 51, 141 f. 

*SOGDIAN: BSogd. by- ‘to give, bestow’, SSogd. Bxt° ‘luck, fortune’, MSogd. 
pr-byn ‘gift’ 

Pret.: tr. IND. Isg. BSogd. Bytw ö’r’m, 3sg. BSogd. Byttw ó rt, Inf.: pret. BSogd. Byty 

*CHORESMIAN: Bynyk ‘good fortune’ 

*NEIR: Yzgh. veZ ‘partner (in hunting, sharing the bag made)’ (< *bajia-), Wanji wej 
‘part, portion’ || (+ *ham-) Sh. amböj ‘for, instead of, in exchange for’, Rosh. imboj 
‘id.; substitute, substitution’. 0 Sh. amboj, etc. are probably not from *ham-paka-, 
Skt. sam-paka- ‘ripening thoroughly, maturing’, as cautiously suggested by Morgen- 
stierne, Le, but rather from the root *baj, on which see ESIJa II: 57. In addition, the 
meanings assigned by Morgenstierne have been corrected in ESIJa II: ‘3a, вместо, 
взамен” and “за, вместо, взамен; замена, замещение” respectively. 

==== ARY 6682 context ====
۸ | _چه چي (به چم "چه چیزی)
پسگشت‌ها دشر داد 7 (11006) :01025
۳ 17
0 (1300) 8۸82/0 برهان قاطع زا 9 : ۶۶۴
10 84 او

یادداشت: 1

۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»

چنگال مرغان و جانوران دیگر (برهان قاطع :: ۹3۴)

۲ چم این واژه در اوستی: بازو,

چم این واژه در کردی: دست.

چم این واژه در ایسلندی کهن: خانه,

چم این واژه در اکثر زبان‌های ژرمنی: قلاب, ۱

1

| جمانگلیس سرواژهی را ی ۵5
اوستایی ((4874): 37 ,۲17 نروژی (08۷۴01۵۷/): 11۷۸ ,3۷1 ,11۷1
پارسی باستان (۶88814۷ 010): لهستانی (۳0[5): اد
```


## [2026-09-05T06:17:35.429Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN bazm ===\"; grep -n \"bazm\\|Gastmahl\\|Gelage\" HRN.txt | head -10\necho \"=== HUB bazm ===\"; grep -n \"bazm\" HUB.txt | head -10\necho \"=== NYB bzm ===\"; grep -n \"bzm\\|bazm\" NYB_vol2_glossary.txt NYB_vol1.txt | head -10\necho \"=== ARY bagh ===\"; grep -n \"باغ\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Horn/Hübschmann/Nyberg/Aryanpur"
}
```


### [2026-09-05T06:17:35.516Z] TOOL RESULT

```
=== HRN bazm ===
3938:422. JeSn 'Fest, Gelage* »).
6566:753. sür *Fest, Gelage'. •
6571:'Gelage, Hochzeitsfest* (die Bedeutung ist hier noch
8769:1007. meyezd *Gelage\
=== HUB bazm ===
951:23, 13), afgh. LW. bazm *an assembly, a company, a
953:(WZKM. 7, 368), das arm. LW. bazmel sich zu Tische
954:setzen , dvanXivai Marc. 6, 39 etc., bazmakan *der zu
955:Tische sitzt, Gast' etc. Dazu np. bazmgah 'Ort des
956:Gelages', bazma 'angulus in loco compotationis'. Frag-
6384:bazm Test' H. 215; baza *Siinde' H. 216; bastan 'binden
7975:= zd. sm = ap. np. zmi bazm 'Gastmahl', arm. bazmakan
10331:bazm 29.
=== NYB bzm ===
=== ARY bagh ===
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
11041:۳ چم این واژه در یونانی: کج بیل» بیل باغبانی. :
11961:چم این واژه در زبان‌های غیرایرانی و غیرهندی: غرید» غدغد کردن» صدای قورباغه ایجاد کردن. :
```


## [2026-09-05T06:17:39.317Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '940,965p' HUB.txt\necho \"=== which page ===\"\npython3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i,l in enumerate(t):\n    if 'bazm' in l and 'afgh' in l:\n        print('leaf',i)\n\"\necho \"=== 7975 ctx ===\"\nsed -n '7970,7980p' HUB.txt",
 "description": "Read Hübschmann on bazm"
}
```


### [2026-09-05T06:17:41.230Z] TOOL RESULT

```
bdzina 'Maroquin . — Auflfallig sind die dialektischen
(semn. wa;j.) Formen mit c, in denen wohl ein Suffix
steckt.
214. Im Altpersischen ist vazrka- gross' zu lesen mit r-
Vokal (KZ. 27, 111), im Phi. vazrk^) (HajtabSd-Inschrift
Z. 6), spater vazurg Gl. and Ind. 236, paz. guzurg
Min. 61. 95, np. hu»urg» Horn's Bemerkungen gegen
den r-Vokal im Persischen (KZ. 32, 572 flg.) sind ver-
fehlt. — Dazu auch afgh. LW. buzarg *a saint, an elder,
an ancestor, 2) great, venerable'.
215. Zu ba^m *Gesellschaft, Gastmahl, Gelage' (Fird. I,
23, 13), afgh. LW. bazm *an assembly, a company, a
banquet' geh5rt, wie Fr. Miiller schon bemerkt hat
(WZKM. 7, 368), das arm. LW. bazmel sich zu Tische
setzen , dvanXivai Marc. 6, 39 etc., bazmakan *der zu
Tische sitzt, Gast' etc. Dazu np. bazmgah 'Ort des
Gelages', bazma 'angulus in loco compotationis'. Frag-
lich. bleibt, ob das Wort mit skr. bhaj verwandt ist.
Ware die urspriingliche Bedeutung *Versanimlung' ge-
wesen, liesse es sich zu lit. bdzmas *Menge, Masse'
(von Menschen etc.), echt arm. bazum Viel' etc. stellen.
217. Np. bisydr Viel' -= ap. ^vasi-dara- Viel haltend'
(so schon Darmesteter, ahnlich Fr. Miiller, WZKM.
6, 357).
*) Geschrieben ist allerdings v(a)crk^ gesprochen aber wurde nie-
mals c sondern z^ vgl. arm. vzurk^ vzruk (Eli§g 20, 5). Das Wort zeigt
=== which page ===
leaf 39
=== 7975 ctx ===
(Strabo), ap, ^Artavazdah-; np. nazd 'nahe* = zd. nazda-;
phi. arm. azd *Nachricht, Kunde' =■ ap. azda *Kunde'; np.
miyazd *Gelage' (Parsenwort) = zd. myazda-, Np. mayz
'Gehirn' = zd. mazga-, ksl. mozgu, idg. mazg'^ho^.
b)tlran. zm (= idg. ^^ g^h + w, auch][dA -f s + w?)
= zd. sm = ap. np. zmi bazm 'Gastmahl', arm. bazmakan
*Gast*, siehe oben p. 29 ; razm *Schlacht, Kampf , arm. razm
und paterazni, phi. razm u patrazm Yatk. i. Zar. 66, zd.
rasman-, Wrzl. reg'^, siehe oben p. 66; hSzum 'Brennholz'
= zd. a^sma-, aus *aidhsmO'?, vgl. gr. ai&w; Gurazm bei
Firdusi (fur *Karazm) = zd. kavarasmo (gen. sg.), Dar-
```


## [2026-09-05T06:17:59.179Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds', t.count(chr(12)))\nimport re\nprint(re.findall(r'(?m)^\\s*\\d{2,4}\\s*$', t)[:20])\nprint(len(t.split(chr(10))))\n\"\ngrep -n \"pdf page\\|\\[page\" MON_part1.txt | head -3",
 "description": "Check Mo'in file page structure"
}
```


### [2026-09-05T06:18:01.009Z] TOOL RESULT

```
formfeeds 0
['11 \n\n', '۱۳۲۷ \n', '۱۳۳۳ \n', '\n\n۱۰۳ ', '\n\n۱۰۷ \n\n', '\n\n۱۰۹ ', '\n\n۱۱۰ \n', '\n\n۱۲۱۱ ', '\n\n۱۱۴ ', '\n\n۱۵ \n\n', '\n\n۱۷ ', '\n\n۱۲۱۸ \n\n', '\n\n۱۹ ', '\n\n۱۲۱ ', '\n\n۱۳ ', '\n\n۱۳۵ \n\n', '\n\n۱۳۸ \n\n', '۳9 \n', '\n\n۱۳۹ ', '\n\n۳۳۷ ']
99340
```


## [2026-09-05T06:18:09.033Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%B0%D9%84%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for بذله exactly, including any bracketed origin tag such as [ع.], and also the دهخدا entry's origin marking."
}
```


## [2026-09-05T06:18:10.496Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for بهادر exactly, including any bracketed origin tag (e.g. [تر.] or [مغ.]), and the دهخدا entry's stated origin."
}
```


### [2026-09-05T06:18:14.949Z] TOOL RESULT

```
# Dictionary Entries for بذله

**From Farhang-e Mo'in (Mo'in Dictionary):**
"(بَ لِ ) ( اِ. ) شوخی ، لطیفه ."
[Translates to: wit, humor, pleasantry]

**From Dehkhoda Dictionary Origin Marking:**
The Dehkhoda entry indicates the word's Arabic origin with "( ع اِ )" notation, classifying it as an Arabic loanword in Persian. The entry documents two primary meanings: everyday clothing and witty discourse, with the latter sense including pleasantries and jests.
```


### [2026-09-05T06:18:17.001Z] TOOL RESULT

```
# بهادر Dictionary Entries

## Farhangi Mo'in (فرهنگ معین)
The entry states: "(بَ دُ ) \[ تر. \] (ص . ) دلیر، دلاور، شجاع ."

The bracketed tag \[تر.\] indicates a Turkish origin.

## Dehkhoda (لغت نامه دهخدا)
The Dehkhoda entry begins with: "بهادر. \[ ب َ دُ \] ( ص ) شجاع و دلیر بکمال. ( برهان )"

This entry does not explicitly state an origin source in its opening, though it cites various classical Persian lexicographical authorities (برهان, آنندراج, etc.) for definitions meaning "courageous and brave."
```


## [2026-09-05T06:18:24.270Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/esophagus",
 "prompt": "Give the full etymology of esophagus, including the Greek elements and whether -phagos 'to eat' from phagein is involved, and any note that the first element is uncertain."
}
```


## [2026-09-05T06:18:25.899Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bow",
 "prompt": "Give the etymology of 'bow' meaning the front of a ship (bow n.2 or n.3): which language it was borrowed from (Old Norse bogr, Middle Low German boog, Dutch boeg), the date, and the connection to 'bough' and PIE *bhagu- 'arm'."
}
```


### [2026-09-05T06:18:29.134Z] TOOL RESULT

```
# Etymology of Esophagus

The word derives from Greek *oisophagos*, literally meaning "what carries and eats." The term combines two Greek elements:

1. **First element**: *oisein* (future infinitive of *pherein*), meaning "to carry," which traces back to the Proto-Indo-European root *bher- meaning "to carry."

2. **Second element**: *-phagos*, derived from *phagein* meaning "to eat," stemming from the PIE root *bhag- meaning "to share out, apportion; to get a share."

The word entered English in the late 14th century. The first element's uncertain status isn't explicitly noted in the source, though the future infinitive construction (*oisein*) suggests some complexity in the Greek formation. The "-phagos" component is clearly identified as coming from *phagein*, and this eating-related root does appear in the etymology.
```


### [2026-09-05T06:18:35.369Z] TOOL RESULT

```
# Etymology of "Bow" (Front of a Ship)

**Origin and Date:**
The nautical term "bow" dates to the mid-14th century. It comes from sources including "Old Norse _bogr_, Middle Low German _boog_, Middle Dutch _boech_" referring to a ship's bow.

**Connection to PIE Root:**
All these forms trace back to "Proto-Germanic _\*bugon-_, from PIE root _\*bheug-_ 'to bend,' with derivatives referring to bent, pliable, or curved objects."

**Note on "Bough":**
The document does not mention any connection between the nautical "bow" and the word "bough" (tree branch), nor does it reference PIE *bhagu-. The "bow" (ship's front) and "bough" (tree part) appear to be separate etymological lines, though both relate to the *bheug- root meaning "to bend."
```


## [2026-09-05T06:18:48.107Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82%C7%B5us",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Indo-Iranian, Avestan, Persian, Greek, Germanic including Middle Low German/Dutch and English bough/bow, Tocharian, Armenian)."
}
```


## [2026-09-05T06:18:49.072Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88",
 "prompt": "Give the Persian etymology of بازو (bāzu) 'arm': Middle Persian form, Old Iranian/Avestan antecedent, Proto-Indo-European root, and cognates."
}
```


### [2026-09-05T06:18:50.722Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:18:57.295Z] TOOL RESULT

```
# Persian Etymology of بازو (bāzu)

**Old Persian Form:** The word derives from Old Persian **𐎲𐎠𐏀𐎢** (bāzu).

**Proto-Indo-Iranian Antecedent:** It comes from Proto-Indo-Iranian **\*bʰaHȷ́ʰúš**.

**Proto-Indo-European Root:** The ultimate source is Proto-Indo-European **\*bʰeh₂ǵʰús**, meaning "arm."

**Cognates:** Related words appear across ancient and modern languages, including Avestan 𐬠𐬁𐬰𐬬𐬋 (bāzvō), Sanskrit बाहु (bāhu), Ancient Greek πῆχυς (pêkhus, "forearm"), and Old Armenian բազուկ (bazuk), which itself was borrowed from Iranian.

This etymological path demonstrates the word's deep Indo-European heritage, with the term remaining relatively stable across millennia of linguistic development.
```


## [2026-09-05T06:19:05.690Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT bough/bow ===\"; grep -n \"^BOUGH\\|BOUGH,\\|BOW (3)\\|BOW,  the fore\\|Bough\" SKT.txt | head -10\necho \"=== SKT oesophagus/anthropophagi ===\"; grep -n -i \"phagous\\|oesophag\\|esophag\\|sarcophagus\" SKT.txt | head -10\necho \"=== FSD phagocyte ===\"; grep -n -i \"phagocyte\" FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt 2>/dev/null | head -5",
 "description": "Grep Skeat and Funk-Wagnalls"
}
```


### [2026-09-05T06:19:05.782Z] TOOL RESULT

```
=== SKT bough/bow ===
=== SKT oesophagus/anthropophagi ===
5994:Esophagus,  gulitt,  tL.-Gk.l  Late  U rf/c/Z/a^T/r.  —  Gk.  olao^^ot,  the  gTillet,  lit. cuiivejer  of  food.  — Gk  otaai.  I  shall  carry, from  a  base  ot-.  lo  carry  (Skt.  vi^  to  drirc) ; tpay-,  base  of  ^a7ftV,  to  eaU
16490:sarcophagus.  ;U  -  Ck,y    L.  m phagut,  a  ^tone  tomb;  nude  of stone  which  was  suppoaed  to corpse   (Pliny^.  —  Gk.  «e ouusumuig ,  beoo:  Umr-atnnc-  *  Uk.  ^V
=== FSD phagocyte ===
FSD_vol3.txt:37017:' mi'ero-phage, n i/utol A small phagocyte ml'ero-
FSD_vol3.txt:98065:upon tbe Ingestion of pathogenic bacteria by phagocytes
FSD_vol3.txt:143405:— pliag'o-ry''Cal, o Of or pcrtatnli^ to a phagocyte.
FSD_vol3.txt:143407:or quality of a phagocyte — pmm''o-cy'i«»-blast, n A
FSD_vol3.txt:143408:phagocyte In embryo - phag*o-ey-|ol'y^sls, n The dl»>
```


## [2026-09-05T06:19:11.910Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"bough\" SKT.txt | head -5\necho \"=== FSD bough/bow ===\"; grep -n -i \"\\[<AS\\. bog\\|bogr.*shoulder\\|shoulder.*bogr\" FSD_vol1.txt | head -5\necho \"=== WEB ===\"; ls | grep -i \"WEB\"",
 "description": "Grep Skeat/FSD for bough"
}
```


### [2026-09-05T06:19:12.025Z] TOOL RESULT

```
10439:limber  u),  part  of  a consisting  of  two  wheels  and (Scand,>  Krom  prov.  E.  UmAoTt thilii  or  shalts,  the  b  being Further,  Umm-fr-t  \%  a  lionhU  plural ;. appears  by  the  dcrivaiJua.»loeL  Am| boughs,  branches  (hcoce.  shafts'!,  pL lim,  foliage,  closely  related  toAjNr.  alui Xilmb  (3),  the  edge  or  bonlei scKlJnl,  &c  (L.)  L.  Umlm4^ edging.  e<Igc.
11202:Maat  (i),  a  pole,  to  hold  the  sails  of  a ship.  (E.)  M.  E.  mast.  A.  S.  mtrst.  stem of  a  tree,  bough,  mast.  4-  ^^^  ffMs^, Swcd.  and  Dan.  mtu/,  G.  mast.
15553:y.  (K  —  L.)  F.  ramijitr,  to  put Achca  (hence,  to  branch  oflT).— !«. a  branch,  bough ;  -^tart, lake.
19241:tow  (3)»  coarse  part  of  hemp.  (E.) M.  E.  tffw.  A.S.  tow,  occuring  in  tffit'-Nc weore,  material  for  spinning,  lit.  'low-like stufl,*  and  in  ttrw-hth,  a  tow'housc,  hou«>e for  spinning.  Orig.  the  operation,  not  the material;  cf.  A.  o.  getawa^  implements. Allied  to  A.S,  tatuian,  to  prepare,  work  ; see  Tawr  (above).  +  O.  Du.  touw.  tow, toutoen,  to  tan  leather,  touwe,  a  weaver's implement;  IceL  ti,  a  tuft  of  wool  for spiKning. Tawdry,  showy,  gaudy.  (E.J  Formerly uscil  in  the  pliraitc  laivdry  late,  which  mean! lace  bought  at  St.  Awdrys  fair,  held  in  the Isle  of  Ely  (and  elsewhere)  on  St.  Awdry'i day,  Oct.  17.  Tawdry  is  a  familiar  con- traciiou  of  St.Awdry.  p.  Again  Axvdry iit  a  popular  form  of  Eihefdrida,  the  La< tinised  form  of  the  A.  S.  female  name y^^ldryfi  or  y£)v/J'rytJ.  It  means  'noble strength;'  from  A.S.  tfffW  or  <r]tf/.  noble, and  \ryfi  or  ^ry^u,  strength.  CI.  Icel. ynlf^rf  the  name  of  a  goddess;  and  the suffix  in  Cer-trudt^  a  name  of  O4 origm.
20739:W^erHufHt  A  common  Hiying.  *  L./re, isblicly;   yrrAum.  a  word. Verbena.  (,L.)  L.  u^rbtna,  orig.  a  sacred bough;    afiei wards,    Tcrvain.      Allied    to tt^rdfr,  Iw'g.  shoot,  rod.
=== FSD bough/bow ===
=== WEB ===
WEB_vol1.txt
```


## [2026-09-05T06:19:16.299Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"boog\\|boeg\\|bogr\" WEB_vol1.txt FSD_vol1.txt SKT.txt 2>/dev/null | head -12",
 "description": "Grep for boog/boeg/bogr in English dictionaries"
}
```


### [2026-09-05T06:19:16.361Z] TOOL RESULT

```
SKT.txt:11286:Maze.  (Scand.)  M.  E.  mate find  M.E.  Mtiuen.  to  confiiste. origin;  cf.  Norwe;j.  miua  it  \ reflexive),  to  lose  one's  scn-rts  a: dream,  masa^  to  pore  over  a  thing prate,  chatter :  Icel  ma^a.  to  prate,  chi| Swed.  dial,  masa,  to  bask  in  the  son,  B laiy.  lounj^e  about.  Cf  E.  in  a ft  dreamy  pcTpIcxity.  Tlie  orig. to  have  lein  '  to  Iw  lost  in  tboogfaC or  pore  over  a  thing,  whence  ue  i '  perplexity '  for  the  sb.
WEB_vol1.txt:22476:e shoulder, arm; Ice. bogr; Sw. bog; O.H.G buog; Gr. pechys; Sans. bahu, the arm.)
WEB_vol1.txt:22625:5. to express (agreement, thanks, etc.) by bowing. bow, v.i. 1. to bend; to curve; to bend, in token of respect; often with down, as, money is the idol to which the world bows down. 2. to stoop; to fall upon the knees. [Dial.] 3. to bend the head or body forward as a č mark of assent or salutation. 4. to yield or submit, as to authority. bow, n. an inclination of the head, or a bending of the body, in token of respect, civility, or submission. bow, 7. [16th-c., from LG. or Seand.; cf, LG. biz, D. boeg, Sw. bog, shoulder, bows.] 1. the front part of a ship, boat, or airship; the prow. ` 2. the oarsman nearest the bow. bows on; head first. bows under; making difficult progress; over- whelmed. bow, a. of or near the bow; fore: opposed to stern. bow, n. (ME. bowe, boge; AS. boga, from bugan, to bend.] 1. a curve; a bend. : 2. a device for shooting arrows: it is a
WEB_vol1.txt:22696:of a ship's square sails, by s ; called bridles, and used 40 eon nnate Parts edge of the sail tight forward on ne Weather is panog into the wind. £ en the ship on a bowline; close-hauled: wi ; as to go as nearly against a3 oan eal bow’line bri/dle, in nautical us which the bowline is attached Ones pail Gwiline knot (not), a knot used to tie of a bōwl’ing, n. 1.a game in i is bowled along a Poden eh a hea ball in an attempt to knock over ten wont alley) set upright at the far end; tenpins oden pins 2. the game of bowls. A _ 3. the playing of either of the bowl’ing, a. of or for bowling. bowl’ing al/ley, 1. a long, narrow wooden lane used in bowling: the pla: a ball down it so as to knock down rA rolls placed upright at the far end. © pins _ 2, [often pL] a building for bowling bowl’ing green, a smooth, level lawn fo: ea the game of ip pie x Owls, n. 1. an old game played lawn (bowling green) with & weighted wood ball (bowl) which is rolled in an attem = te Tae) it stop near another, stationary bah 2. ninepins or tenpins. 3. skittles. bow’man, n.; pl. bOw’men, an archer. bow’min, 7.; pl. bow’men, the oarsma nearest to the bow of the boat; the bow oaks bown, bowne, v.t. and v.i. to boun, 5 bow net, 1. a trap of wickerwork, etec., for catching lobsters and crawfish. X 2. a kind of bird net. bow Oar, the foremost oar used in a boat except in a whaleboat, where it is sometimes the second oar; also, the person who pulls it. bow pen, a metallic ruling pen having the part which holds the ink bowed out toward the middle; also, a bow compass carrying such a pen. bow pen’cil, a bow compass, on one leg of which there is a pencil. bow pin, the pin which secures the bows of an ox yoke. bow’pot, n. a boughpot. bow saw, a saw with a narrow blade set in a strong frame resembling a bow. béwse (or bouz), n., V-t., and v.i.; bowsed, $t., pp.; bowsing, ppr. bouse (drink). bow’shot, 2. the distance marked by the flight of an arrow. 5 bow’sprit (or bd/sprit), n. [ME. bowsprit; D boegspriet; boeg, bow of a ship, and spriel, a sprit.] a large, tapered pole or plank extend- ing forward from the bow of a sailing vessel: the foremost stays are fastened to it.
WEB_vol1.txt:106806:Gen. Sir William Boog Leishman (1865-1926), adormite a E LA wreath: [
FSD_vol1.txt:45681:boeg,  1   bll;  2   bQ,  a.  [S.-Afr.  D.]  Weary;  tired.
FSD_vol1.txt:46745:boose,  1   bQz;  2   boog,  n.  [Prov.  Eng.]  A   cow-stall  or  -shed;
```


## [2026-09-05T06:19:27.723Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"bhag-\\|bhagus\\|bhaghu\\|bhāghu\" AHD_watkins1985.txt | head -20",
 "description": "Grep Watkins AHD for bhag/bhaghu"
}
```


### [2026-09-05T06:19:27.829Z] TOOL RESULT

```
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2120:PORGY bhag-2 PORK porko- PORNOGRAPHY per-§ POROMERIC per-2 PORPOISE peisk-, porko- PORT! per-2
```


## [2026-09-05T06:19:40.446Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"baga-\\s*n\\.\\|baya-\\|Anteil,  Los\\|Anteil, Los\" BRT.txt | head -20",
 "description": "Grep Bartholomae for baga-"
}
```


### [2026-09-05T06:19:40.494Z] TOOL RESULT

```
6186:■  /.,  g.  aäay-  f  'was  einem  auf  Grund seiner  Leistung  —  in  gutem  und  schlimmem Sinn  —  zukommt;  Anteil,  Los,  Verdienst, Lohn,  Belohnung*,  bes.  beim  letzten  Ge- richt": kä  ahmäi  °sis  ?r3nävi  Y.g.y,  4 —  yaia  ad  masis/äsca  . .  asayö  »nnavanU Y.52.3;  —  'itm  fyao^anäis  vohü  äaiält mofuiMhii  "(je)  nach  den  Taten  (die  einer getan  hat)  soll  VM.  das  Los  zuweisen" Y..^j.i6";  —  ia  zasta  yä  tä  haßt  (sd.) az<i  yä  da  -Sil dr^äin asäunaka  ". .  jene Lose,  die  du  dem  Drug-  und  dem  Afa- anhänger  zuweisen  wirst  .  ."  Y.4y-4;  — ail  .  .  ya  vi  'Itf  *ranöibya  savSi  (sd.) ndoyai  Y.43.12;  —  vTdyai  (sd.)  saoi);_ jdiä  hsi  '/is  anhat  Y.  4^.  9 ;  —  yada  'sifis maAjä  VOSS  xsayä  (sd)  Y,50.9;  -^.S; iiSit..asahe  nSi£  '/ayä{GS.y^/räi'fnti{sA.) P.44;  —  >r>kyä  amatai^yä  °Ms..aslöis Vr.^.4;  —  däidl  aiä  tarn  'sim  vanhsus Syafta  manar^hs  Y.  28. 7 ;  — yS  mHi  nä  va gMa  (sd.)  va  .  .  dayät  ■  ■  vahista  'slm  asäi vehü  xiair»m  mananha  "wer  . .,  als  Lohn für  seine  Gerechtigkeit  das  Reich  durch VM.  (verldhe  ihm)"  Y.4ö.io*>;
10436:•  j-,  g.,  p.  'grab-  V.  'greifen'.  Praes. i  grab-,  11%  g^rminä'^,  15  girißa-*'"'^ , 23  garb.tya-,  gSun'aya-'^,  24  gSurvaya-'^, <)-^  24 ^3r?mbaya-'^,2T g)r3bya-,gpr)uya-^'>; Perf  I  jagaurv-*^,  jayaurv-^^,  ftgaurv-^^, 2  jag»r»b-.  —  PPf P.  g^r^ta-'');  Inf.  gfnbqm.
12671:•  j.,g.'dab-V, 'betrügen'.  Praes.2  dava-^'', lob  dibmav-'^,  iddiivia-^'"^^  24davaya-''>, 26  (Pass.)  iytf(yii-'>,  30  (Iter.)  däbaya-.  —
16638:"   g.   baga-,  j.  "baya-  n.  'Anteil,   Los':
16728:•  j-,  g.  bay- V.  'erschrecken'.  Praes.  2  !  J/^"'"  ■■  "^''i  ^ß'"*'  ^'^^'^  vanhaot  mana- baya-,\  bya-;  Perf.  i  btwt-.  1«"*«-'   ■  ■    "■  ■  "E^^^oref    iK    .  ."    Vr.  //.
17061:•  g.  bäga-  n.  'Anteil,  Los':  vo?ta  xia'knm vairim  'g»m  aibT.bairist3m  *vrdls;mn3i  (Sp. 722  u.)  .  .  asä  antan.caraitl  Y.jt.  i.
19209:*nizbaya-
19244:•  j,  *m-zbaya-  m.  'Anrufung':  mal  °yeke
26459:•  j.  skamb-  'stemmen',  nur  mit  Praev. Praes.  9+24  sambaya-^^.  —  Inf.  'scapta- yalca;  Absol.  'skamhm.
27716:•  j.  zamb-  V.,  nur  mit  harn  'zermal- men'.    Piaes.  30  (Iter.)  zimbaya-.
30323:anäar  Im  rawäi  i^ät;    im  GrB.  scheint    lu  '  1-  hu-baya-   Adj.  (fem.  •Ja-)    'gutes  EhC;
```


## [2026-09-05T06:19:53.865Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-",
 "prompt": "Give the reconstruction, meaning, and descendants of this PIE root (Indo-Iranian, Avestan, Old Persian, Greek phagein, Slavic bogŭ, Tocharian)."
}
```


### [2026-09-05T06:19:59.609Z] TOOL RESULT

```
# Proto-Indo-European Root *bʰeh₂g-

**Reconstruction:** *bʰeh₂g- (with alternative form *bʰag-)

**Meaning:** "to divide, distribute, allot"

**Key Descendants:**

- **Indo-Iranian:** *bʰāgás ("portion; share"), Sanskrit भज॑ति (bhájati)
- **Avestan:** 𐬠𐬀𐬲 (baž)
- **Old Persian:** 𐎲𐎠𐎪𐎶 (bājim)
- **Greek:** ἔφᾰγον (éphăgon, "to eat" from "to receive a share")
- **Slavic:** Proto-Slavic *bogъ ("share, god")
- **Tocharian:** pāk/pāke ("part, portion, share, piece")
- **Germanic:** Proto-Germanic *bōks ("book" from "identifying marks")

The root shows semantic development from concrete notions of distribution and apportionment to abstract concepts like "share," "portion," and "deity" across Indo-European languages.
```


## [2026-09-05T06:20:04.776Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%BA' --note 'page 82, root Bhag, node 5: Persian باغ bāġ etymology (MP bāg < PIr *bāgáh < PIE *bʰeh₂g-)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%B2%D9%85' --note 'page 82, root Bhag, nodes 9-10: Persian بزم bazm, Armenian bazmim as Iranian loan' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1' --note 'page 82, root Bhag, nodes 6-8: Persian بهادر bahādor < Middle Mongol baɣatur' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88' --note 'page 82, root Bhâghu, node 2: Persian بازو bāzu < OP bāzu < PIE *bʰeh₂ǵʰus' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/esophagus' --note 'page 82, root Bhag, node 13: esophagus < Gk oisophagos, -phagos from phagein' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/bow' --note 'page 82, root Bhâghu, nodes 3-4: English bow (of a ship) < ON bogr / MLG boog / MDu boech' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D8%B0%D9%84%D9%87/' --note 'page 82, root Bhag, node 11: بذله in Moin and Dehkhoda, marked Arabic (ع اِ)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/' --note 'page 82, root Bhag, node 7: بهادر in Moin, tagged [تر.] Turkish' 2>&1 | tail -3",
 "description": "Archive web sources used"
}
```


### [2026-09-05T06:20:11.454Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d0254a8577498e21.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81d228e4afe38829.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b893df06703e275.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7321751ed099d444.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d756bf4f08c07c0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5d91f486af1fa6c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e9c9893bacdc33bd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd38d7677df2c130.txt
```


## [2026-09-05T06:20:26.207Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-' --note 'page 82, entry 0 root box: PIE *bʰeh₂g- to divide, distribute, allot' 2>&1 | tail -2\nmkdir -p data/verification/sources/refs/ocr/BQT\ncat > data/verification/sources/refs/ocr/BQT/220.vision.txt <<'EOF'\n# Borhan-e Qate' (ed. Mo'in), printed page 220 = BQT_v1_pages.txt leaf 440\n# = archive.org borhan-ghate-v1 leaf n440 (image read directly, OCR of the footnote band was illegible)\n# Footnotes at the foot of the page (read from the image, Persian print):\n\n۱ - در پهلوی âpâc dâshtan «منع کردن، مناس ۲۶۶».\n۲ - رك: بازارگان. در زباکی bâzargân «کرمرسن ۷۵».\n۳ - رك: بازن.   ۴ - مصحف بازپیج (= باذبیج) رك: بازپیج.\n۵ - رك: بازپیج.   ۶ - رك: باز.   ۷ - مرکب از: باز (مرغ شکاری) + یار (مبدل: دار؛ چنانکه اسفندیار مبدل اسفنددات است) لغة یعنی دارندهٔ باز.\n\n۸ بازو - در اوستا bâzu ، سانسکریت bâhu «بارتولمه ۹۵۶»، گیلکی bâzû ، برنی\nو نطنزی bâzu «ک. ۱ ص ۲۸۸»، دزفولی و شوشتری bôly ؛ و آن قسمتی است از دست که از\nدوش تا آرنج را شامل است.\n\n۹ بازی - لعب - قمار - فریب.\nEOF\necho saved",
 "description": "Archive PIE root page and save Borhan vision reading"
}
```


### [2026-09-05T06:20:27.918Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d7c6f8d1a1f64c02.txt
saved
```


## [2026-09-05T06:20:37.583Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 82 -l 82 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg82 && ls -la pg82.png\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg82.png'); print(im.size)\nw,h=im.size\nim.crop((0,0,w,int(h*0.55))).save('pg82_top.png')\nim.crop((0,int(h*0.45),w,h)).save('pg82_bot.png')\n\"",
 "description": "Render PDF page 82"
}
```


### [2026-09-05T06:20:40.254Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74477 Sep  5 02:20 pg82.png
(1700, 2200)
```


## [2026-09-05T06:20:42.528Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg82_top.png"
}
```


### [2026-09-05T06:20:42.551Z] TOOL RESULT

```

```


## [2026-09-05T06:20:50.214Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg82_bot.png"
}
```


### [2026-09-05T06:20:50.235Z] TOOL RESULT

```

```


## [2026-09-05T06:21:10.598Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'npxs' in l or 'nPxs' in l or 'anpaxs' in l or 'ambaxs' in l:\n        print('leaf',i,'printed p.',i-66)\n        import re\n        for ln in l.split('\\n'):\n            if 'pxs' in ln.lower() or 'baxs' in ln.lower():\n                print('   ',ln.strip()[:200])\nEOF",
 "description": "Locate Sogdian anbaxs- entry page"
}
```


### [2026-09-05T06:21:12.354Z] TOOL RESULT

```
leaf 101 printed p. 35
    anPaydc     =^npxs-                                                anpaxs, ambaxs         'np^t'k, >nPxs-
leaf 102 printed p. 36
    947 'npxs- M                    o^J'r^'io^J'j^y
    anPaxs, arhbaxs ©<*ham-baxsa; MP hambaxs                          quiet
leaf 278 printed p. 212
    5335 mnPxs- M
    man Paxs ©impf. ^npxs-
leaf 298 printed p. 232
    5801 n* npxst C                            ^^Uw^^j
leaf 307 printed p. 241
    writing (npxsty) ©<*nipixsta ©pp.
    6012 nnSp'mbn M                          {**H fi)J2j>        6023 npxsty -* np^stk
    •020 nny M, S                             (^/ rb)J2                 npxsty, np}YStk, npYStk
    Hen. Sogdica. p7; BSOAS 28, 1965, 252 n 67                     np}xstw\ Frye 21, npxsty
    pcrf. st. ^np^s-, npxst-, np'xst-Cy)                        Pahl. nibdy-, nibdstan =*nyp8-, np»st-
leaf 308 printed p. 242
    nipes =4npxst-, np'ys-
    6041 npxst- M, C
    6043 npxsty C                                           <^.
    nipaxste (np'ysty) ©pi. npxstyt
    STi 57.16, 56.11; STii 1, 81, 89; n. nt. npxstw,
```


## [2026-09-05T06:21:27.470Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nf='incoming/WLD/WLD_Bd2_pages.txt'\nt=open(f,encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('leaves',len(leaves))\nfor i,l in enumerate(leaves):\n    if re.search(r'bhag|bh[aā]gh[uū]', l) and ('zuteilen' in l or 'Anteil' in l or 'Ellbogen' in l or 'Ellenbogen' in l):\n        print('leaf',i, l[:400].replace('\\n',' | '))\n        print('...')\nEOF",
 "description": "Grep Walde-Pokorny Bd2 for bhag/bhaghu"
}
```


### [2026-09-05T06:21:29.180Z] TOOL RESULT

```
leaves 725
leaf 131                                                      bhaud- bhud- |                                                             :         — bhag-                                   127 |  | (ia EN) „Kampf‘ (vgl. Lofctner KZ. 7, ISO, Fick II^ 159, Zup. Gr- 24, Peder- | sen KGr. 134, 63, Palk-Torp u. hadlL, wo weiteres Zubehor aus neuern | germ. Sprachen, z. B. dt. Blutbad), Die genaue Bed.-Obereinstimmung | zwi
...
leaf 132  128                                         bhag-   — bhagO'S |   stiminter Anteil,         Schicksalsbestiininiiiig,      bes.       Mi6geschick‘‘;     ai.    lihal^mii |  jjgeniefit, yerzehrt“      — av. laxsaiti „hat oder gibt Anteil^; Desid. ai. IhiMate |                                                                  vHva „genie6t |  „erbittet''; slav. *hog^ ,.Anteib' vielleicht in slov, zlega boga
...
leaf 133                                         bhag      bbago-s                     129 |  | s.Berneker 99 f. m. Lit, Bruckner KZ. 46, 195). YgL Curtius 188 (iiber | den phryg. BayaTog, nicht ,,q)r]ya)va7og'^ s. u. bhag- „zuteilen“). |   Aus dem Germ, hieher (Osthoff aaO.) nisi, beylci n. „Buchenwald; Buche^', | bmiJcr „Buclise‘‘ (ursprgl. aus „Buchenholz“), beyJcir „Kufer, Bottcher^^ (,,Y er- | fertiger Yon buchen
...
leaf 134  130                              bh%h-?, bhegli-         :   bbugli- ?   — b}iad(h) |       [Den germ, ati- und si. tf-Formen nicht geniigend setzt Wood Mod. Phil. | 11, 325        fiir    fcfgus   usw. bh(u)ag- statt IMtig-                 als Gdf. an.] |  |  | bhagh-? Oder bhegh- bhogh- ? „streiten'^ |                                      : |  |  |  |  |       Gall,    bagaudae „Guerillas eines Bauernkrieges        
...
leaf 149                                                                                                          ; |  |  |  |  |                                         bheug(li)   — bheug-, bbeugb-                                 145 |  | 2. bheiig(h)            „weghm, sich entledigen; ausfegen**. |    Av. baog- „losen, retten“ {bunjainti „sie befreien, retten“, bUjayamno | „ablegend“, bunjayat „er rette“), bUjim acc. .,
...
leaf 152                          ;                             ;                       :                      a |  |  |  | 148                                      bheg-   — | bauslis „Gebot“,  lit. pasibaudyti „sicli erheben, aufbrechen" baicdmti „auf- | muntern, Lust zu etwas erwecken‘‘, apr. eibaudints „auferweckt'^ |    Abg. bljudq^ bljusti „wahren, hiiten, achtgeben“, russ. bljudu, bljtisH | „beobachten, wahrnehmen^
...
```


## [2026-09-05T06:21:36.615Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in [131,132,134,135]:\n    print('#### leaf',i)\n    print(t[i][:1800])\nEOF",
 "description": "Print Walde-Pokorny leaves 131-135"
}
```


### [2026-09-05T06:21:38.467Z] TOOL RESULT

```
#### leaf 131
                                                     bhaud- bhud-
                                                            :         — bhag-                                   127

(ia EN) „Kampf‘ (vgl. Lofctner KZ. 7, ISO, Fick II^ 159, Zup. Gr- 24, Peder-
sen KGr. 134, 63, Palk-Torp u. hadlL, wo weiteres Zubehor aus neuern
germ. Sprachen, z. B. dt. Blutbad), Die genaue Bed.-Obereinstimmung
zwischen Kelfc. und Germ, widerrat isolierende Zuruckfiihrung von germ.
*badiia auf *bha(:ud, oder die Yon kelt. *bodtio^ auf ^bJiachjo- mit der
Media von %haud- „schlagen“. Beziehung zu ai. badh- „drangen“ (Fick
III^256 zw.; iiber das isolierte ai. Wort auch u. bheidh- „zureden“) be-
steht        wohl nicht.

bhaud-       bhiid- „schlagen, stoBen^^ (Hochstufe
                  ;                                                             kaum   als *bhoitd~    za       be-
        stimmen).
     AisL bauta {-add) „schlagen, sto6en‘‘, ags. beatan                                {beat),   ahd. bb‘^(^)an
{bie^   Oder schw, V.) „schlagen, stoBen''
     mhd. bo^, bo^, buj m. „Schlag“, nhi. Ambo/i; ags.                                    „Hammer% mnd.
hotel ds.,            mbd. boe^el „Schlagel“,               aisl.   boytiU   „Zeugang 3 glied des Pferdes^'
(Bed. wie ir. hot s. u., vgl. auch lat. fuUto u. bhatd-); aisl. biitr „kurzes
Stuck eines Baumstammes“, buta „einen Baurastamm zerlegen"*, mit tt nd.
butt „stumpf, piump^‘ (dazu auch der Fischname Butte), mhd. biifze „abge-
schnittenes Stuck, Klumpen^^ (s. aber ahnliche Worte anderer Gdbed. u.
hii-j bhu- „aufbiasen“), ags. buttuc „Ende, Stiick Land'*, norw.
                                                                 mdartl. butt
„Stumpf, Klotz“ (auch „Krug, Holzkufe^, vgl. ags. hytt „a bottle, but, ton“,
auch „Schlauch“; s. zu d
#### leaf 132
 128                                         bhag-   — bhagO'S
  stiminter Anteil,         Schicksalsbestiininiiiig,      bes.       Mi6geschick‘‘;     ai.    lihal^mii
 jjgeniefit, yerzehrt“      — av. laxsaiti „hat oder gibt Anteil^; Desid. ai. IhiMate
                                                                 vHva „genie6t
 „erbittet''; slav. *hog^ ,.Anteib' vielleicht in slov, zlega boga
 ein boses Geschick“ (?), sicher in aksl. nbogz, n< bogz ^aim^ bogaf^ „reich";
 aksl. bog'h „Gott“ (nrverw, oder von den iranischen Skythen nbemommen;
 8. znm Slav. Berneker 66 f. m. Lit.);

    phryg. Bayaiog' Zevg ^Qvyiog Hes. (nach Solmsen KZ. 34,49 ebenfalls
  vielleicht iranischen Ursprnngs, doch s, auch Solmsen Beitr. 139 A 1 uber die
  Moglichkeit, dafi BaXalog zu lesen sei; gegen Yerb. m. (frjyog s. Wiede-
  mann BB. 28, 13); gr. cfayeiv ,jessen“, lokr. TzaiuLaTocfayelaxai „niit Kon-
 fiskation betroffen werden"'.
      Cnrtius 297, Fick       P 87, 284, 487, IP P6 (\vo, wie zw. auch bei Peder-
sen KG. II 460 f. nicht exist, ir. dcbegim „verlaDge“ u. dgl. angereiht wird
 unter Yerweis auf das ai. Desiderativ Ihi'ksate „erbittet“, hhiksd „das
 Betteln“; diese und die kelt. \Yorte aber auch nicht nach Yf. KZ. 34, 480
 unter einer Wz. bhiegh-, bhigli- zu vereinen). Trotz gr. (payoveg’ oiayoreg,
yvd'doi Hes. kaum hieher (Much Zfdt^V^tf. 2, 283) as. (kinni-) baho, dt.
 Backe (s. vielmehr u. bhag- „biegen‘‘). Die Zuruckfuhrung von bhag- auf
bhvag- behufs Yereinigung mit ai. bJnindkti, bhoga-h (s. u. bhevgh-^ „weg-
tun'‘) durch Hirt Abl. 139 ist gekiinstelt (s. auch Wiedemann BB. 28, 12f.),

   Dafi nach Zimmer KZ. 36, 447ff. mit ai. bhcfga-k „der Anteil am Opfer,
der den Gottern zugeteilt wird'^ ein kelt. *bago- „der Ehrenanteil des
grofiten Helden am Festeber^ als Grundlage
#### leaf 134
 130                              bh%h-?, bhegli-         :   bbugli- ?   — b}iad(h)
      [Den germ, ati- und si. tf-Formen nicht geniigend setzt Wood Mod. Phil.
11, 325        fiir    fcfgus   usw. bh(u)ag- statt IMtig-                 als Gdf. an.]


bhagh-? Oder bhegh- bhogh- ? „streiten'^
                                     :




      Gall,    bagaudae „Guerillas eines Bauernkrieges                            in Gallien“;             gehort zu
air. bagahn „ich kampfe, riihme, prahle, drohe“ (der Bedeutungsumfang
von dem Wortkampfe, der den Tatlichkeiten vorangeht, s. Zimmer KZ. 36,
447 ff.), hcig f. „Kampf'', cvmr. (Zimmer aaO.) beio ,,tadeln‘*, bai ,,Pehler‘^;
ahd. bagan, bdgen „zanken, streiten“, aisl. baga, bcsgja „adversari, resistere“,
ahd. baga „Zank, Streif', as. bag m. „Prahlerei‘', mhd.         -ges m. „lautes
Schreien, Zank, Streit“,                  aisl.    bagr, bagi ,,adversarius“, hagr „schwierig, ver-
drieBlich, hinderlich'', z. B.                    Pick
                                      494, II* 160, 111* 257. Das von Prell-
witz^ 368,  Uhlenbeck Ai. Wb. 189, Falk-Torp u. h^ag, in Rechnung ge-
zogene ai. bahate „drangt, driickt'' ist wegen der abweichenden Bed. und
bes. wegen der Unsicherheit seiner eigentlichen Lautform (s. Uhlenbeck
aaO.) schwerlich zu vergleichen.
   Nach Zimmer aaO. ist Entlehnung der germ. Sippe aus der kelt. (die
idg. b\h\ag\h] oder          fortsetzen konnte) sehr erwagenswert anderm                                   ;


falls bestiinde Ablaut germ. E    kelt. o (z. B. Pedersen EG. I 101).
                                                    :



   Die von Pauli KZ. 14, 100, Prellwitz aaO. (zw.) angenommene Yer-
wandtschaft mit ^bhdglms „Ellbogen und Unterarm^* ware lautlich nur bei
kelt. Ursprung der germ. Worte halt
#### leaf 135
                                    bhabha — bhares-, bhores-                                             131


lich“       usw. (s. hlioidlio-) unter einer Wz. "^bholiyVi- „schmutzig, garstig'^
(\.    d.   Osten-Sacken IF. 23, 378, s. auch 33, 207) ist eine ganz fragwiirdige
Konstruktion.


bhabha und anklingende Worte fur „Bohne‘‘, u. zw. „Saubohne“, vgl. zum
    Sachlichen Hoops Waldb. 350, 400f., 464 f., Hehn Kltpfl. ® 221, 570,
        Schrader RL.^ 159f.
   Lat. faba      (dial. „Bohne“, mss. usw. bob^, apr. babo ds.
                           Jiaba)                                   Wenn                         —
das     Wort (gegen Kretschmer Einl. 146 f.) eine Red.-Bildung und nach
Persson Beitr. 253a 1, Wood Mod. Phil. 11, 324, als „aufgeblasene Schote,
Schwellung“ mit germ. Worten wie mhd. biiobe „Knabe‘', pi. auch ,,die
weiblichen Bruste“ unter einer Lautvorstellung ^blia (von den aufgeblahten
Backen) verwandt sein sollte, konnte auch gr. cpaxog „Linse‘' alb. ba'&e                     :




,,Saubohne'*' {^bhakti,  G. Meyer Alb. Wb, 22, Pedersen KZ. 36, 332) als in-
folge der (deminutiven) -Z’o-Ableitung nicht der Reduplikation bediirftige
Schwesterbildung gelten (iiber das in der Bildung gleichartig aussehende
gr. d^axog s. u. '^ereg'^Qijo- und "^arvko-), Auch da6 aisl. baun, ags. ahd.
bona „Bohne“ {Baunonia friesische Insel bei Plinius) durch Hiss, von
^habna zu ^tanna entstanden sei, ist, obgleich unsicher, doch wahrschein-
licher, als da6 es eine mit got. nfbauljan „anschwellen machen, aufblasen'*
ablautgleiche Bildung von "^bheti „schwellen‘' (oder blieu- „wachsen, wer-
den“j sei (E. Schroeder ZfdA. 42, 71, Petersson IF. 23, 390, Holthausen
AfdA. 20, 233j.
   lAt. pupa, lett. pupa „Bohne^' stammen                  durch finn. Vermittlung (liv. pupa,
fin
```


## [2026-09-05T06:21:43.347Z] TOOL CALL #71: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:21:43.387Z] TOOL RESULT

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


## [2026-09-05T06:22:01.892Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg82.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/82.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/82.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T06:22:01.969Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74477 Sep  5 02:22 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/82.png
```


## [2026-09-05T06:23:07.007Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82a.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_BAG  = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%BA\"\nW_BAZM = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B2%D9%85\"\nW_BAH  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\"\nW_BAZU = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88\"\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-\"\nE_ESO  = \"https://www.etymonline.com/word/esophagus\"\nE_BOW  = \"https://www.etymonline.com/word/bow\"\nA_BAZL = \"https://abadis.ir/fatofa/%D8%A8%D8%B0%D9%84%D9%87/\"\nA_BAH  = \"https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/\"\n\nentry0 = {\n  \"entry\": 0,\n  \"root\": \"Bhag\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *bʰeh₂g- / *bʰag- 'to divide, distribute, allot; to get a share' (Pokorny 1. bhag- 107; Watkins bhag-¹)\",\n  \"note\": \"The root box is exactly right. Pokorny p.107 heads the entry 'bhag- ‘zuteilen; als Anteil bestimmen oder (ursprüngl. medial?) als Anteil, als Portion erhalten’' — i.e. Nourai's 'to share out, to enjoy', the second gloss being the medial sense Pokorny himself flags. Watkins (AHD appendix) gives 'bhag-¹. To share out, apportion, also to get a share', and Mann (IEC 61, p.60) 'bhag-, bhāg- ‘enjoy; enjoyment’'. Modern laryngeal notation writes the root *bʰeh₂g- (Wiktionary), which is the same root with *a analysed as *eh₂. The language label 'Indo-European' and the page numbers POK:107 and IEC:61 are both correct. What is worth flagging at root level is Nourai's PART-2 chart itself: it hangs on this one root three quite different kinds of claim — the inherited Iranian/Greek reflexes (bāga-, βγ, phagein), which are secure; Mann's private reconstructions *bhaglos/*bhagmos, which no other handbook accepts; and the Sanskrit→Mongolian→Persian route for bahādor, which modern scholarship rejects outright.\",\n  \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۱۰۷ ریشهٔ bhag- را «بخش کردن، بهره معیّن کردن یا بهره گرفتن» معنی کرده و همین دو معناست که نورایی آورده است؛ واتکینز (پیوست AHD) و من (IEC ۶۱) نیز همین را دارند. در نگارش امروزی این ریشه را *bʰeh₂g- می‌نویسند که همان ریشه است با تحلیل a به eh₂. نکتهٔ مهم آن است که نورایی سه دسته ادّعای ناهمسان را زیر یک ریشه آورده است: بازمانده‌های اصیل ایرانی و یونانی (bāga-، βγ، phagein) که پذیرفته‌اند؛ بازسازی‌های شخصی من (*bhaglos، *bhagmos) که هیچ فرهنگ دیگری نپذیرفته؛ و راه سانسکریت ← مغولی ← فارسی برای «بهادر» که پژوهش امروزی آن را رد می‌کند.\",\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"POK:107\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.107 (POK_01.txt, \\\\f-leaf 116, the page marker '107' stands mid-leaf): 'hhaZ- [= bhag-] zuteilen; als Anteil bestimmen oder (ursprüngl. medial?) als Anteil, als Portion erhalten'. The entry runs on to p.108 with ai. bhajati, av. bag-/baxsaiti, ai. bhaga-, av. baga-/baγa-, npers. baγ 'Gott', gr. φαγεῖν 'essen', slav. bogŭ. Page number and gloss both exact.\"},\n    {\"ref\": \"IEC:61\", \"status\": \"supports\", \"note\": \"Mann, IEC.txt line 1062 (printed p.60) 'bhag-, bhāg- ‘enjoy; enjoyment’. WP II, 127', and on printed p.61 (running head '61 bhaglos — bhaksó, ið') the two derived entries Nourai copies. The 'to enjoy' half of his gloss is Mann's word.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 127-128 (incoming/WLD/WLD_Bd2_pages.txt leaves 131-132)\", \"stance\": \"supports\", \"note\": \"the running heads read '— bhag- 127' and '128 bhag- — bhago-s'; the article has 'ai. bhakṣati „genießt, verzehrt“ — av. baxsaiti „hat oder gibt Anteil“ … slav. *bogŭ „Anteil“ … gr. φαγεῖν „essen“'. This is the source Pokorny and Mann both cite (WP II 127).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhag-¹ (AHD_watkins1985.txt line 323)\", \"stance\": \"supports\", \"note\": \"'bhag-¹. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH. [Pok. 1. bhag- 107.]'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 p.142 s.v. baksheesh (KLN_1966.txt leaf 86)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *bhag-, ‘to distribute, share out’, whence also OI. bhājati … bhagaḥ ‘allotter, distributor, master, lord’, Gk. φαγεῖν ‘to eat’. See -phagous and cp. Bhaga … and in bahadur.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1949\", \"stance\": \"silent\", \"note\": \"grep 'bhag' in SYN.txt returned nothing usable; Buck treats 'eat' (§5.11) from *ed- and does not discuss this root.\"}\n  ],\n  \"nodes\": []\n}\njson.dump(entry0, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.json','w'), ensure_ascii=False)\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82a.py",
 "description": "Build entry 0 root section"
}
```


### [2026-09-05T06:23:08.781Z] TOOL RESULT

```
ok
```


## [2026-09-05T06:29:28.263Z] TOOL CALL #74: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\nSP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\ne0=json.load(open(SP+'e0.json'))\n\nW_BAG  = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%BA\"\nW_BAZM = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B2%D9%85\"\nW_BAH  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1\"\nW_BAZU = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88\"\nW_PIE  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-\"\nE_ESO  = \"https://www.etymonline.com/word/esophagus\"\nE_BOW  = \"https://www.etymonline.com/word/bow\"\nA_BAZL = \"https://abadis.ir/fatofa/%D8%A8%D8%B0%D9%84%D9%87/\"\nA_BAH  = \"https://abadis.ir/fatofa/%D8%A8%D9%87%D8%A7%D8%AF%D8%B1/\"\n\nN=[]\n\nN.append({\n \"id\":1,\"lang\":\"Avestan\",\"words\":\"bâga\",\"verdict\":\"plausible\",\n \"derivation\":\"Avestan bāga- is real: Bartholomae, Altiranisches Wörterbuch, has both 'g. baga-, j. baγa- n. ‘Anteil, Los’' and a separate Gathic 'bāga- n. ‘Anteil, Los’' cited from Yasna 51.1 — the long-vowel stem *bʰeh₂g-o- beside the short-vowel one, exactly the *bʰāgás of Proto-Indo-Iranian (Skt. bhāgá- 'portion'). Nourai's form and language label are therefore right, and so is the first gloss 'share'. 'Property' is a stretch of Skt. bhāgá- 'Teil, Eigentum' (Horn's own wording), and 'garden' is not an Avestan meaning at all: it is the New Persian sense of bāγ read back into the Avestan etymon so that the arrow to node #5 looks self-evident. The real semantic step ('allotted share' → 'allotted plot of land' → 'garden') happens inside Iranian, most probably already in Middle Persian.\",\n \"derivation_fa\":\"صورت اوستایی bāga- واقعی است: بارتولومه در «فرهنگ ایرانی باستان» هم baga-/baγa- «بهره، بخت» را دارد و هم bāga- گاهانی «بهره، قسمت» را با شاهد یسنا ۵۱٫۱؛ این همان ستاک با واکهٔ بلند است که در هندوایرانی آغازین *bʰāgás و در سنسکریت bhāgá- «بهره، دارایی» بازتاب یافته. پس صورت و برچسب زبانی درست است و معنای نخست («بهره») نیز. امّا «دارایی» بازخوانی آزادِ عبارت هرن است و «باغ» اصلاً معنای اوستایی نیست؛ نورایی معنای فارسی نو را به ریشهٔ اوستایی بازتابانده تا پیوند با گرهٔ ۵ بدیهی بنماید. تحوّل معنایی («بهرهٔ بخش‌شده» ← «قطعه‌زمین بخش‌شده» ← «باغ») درون خودِ ایرانی و به احتمال زیاد در فارسی میانه رخ داده است. داوری: با احتیاط پذیرفتنی.\",\n \"sources\":[W_BAG,W_PIE],\n \"ref_check\":[\n  {\"ref\":\"HRN:39\",\"status\":\"supports\",\"note\":\"Horn, Grundriss no. 169, printed p.39 (HRN.txt \\\\f-leaf 61): '169. bāγ ‘Garten’. Wohl aw. bāga- ‘Loos’ (Y. 51,1); ai. bhāgá- ‘Teil, Eigentum’; phlv. bāg (PPGl.).' — this single line is the source of Nourai's whole Avestan box, gloss 'property' included (Horn's 'Eigentum'), and of the arrow to node #5. Note Horn's hedge 'Wohl' (= probably).\"},\n  {\"ref\":\"AEF:224\",\"status\":\"not_checked\",\"note\":\"Khaleqi Motlaq's Asās-e Ešteqāq-e Fārsi is the Persian translation of Horn and is not online (refs_online.json: catalogue only). Its no. 169 is the passage checked above; p.224 is consistent with the Persian edition's numbering.\"}\n ],\n \"consulted\":[\n  {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW (BRT.txt lines 16638 and 17061)\",\"stance\":\"partial\",\"note\":\"'g. baga-, j. baγa- n. ‘Anteil, Los’' and 'g. bāga- n. ‘Anteil, Los’: … Y.51.1'. Bartholomae confirms the form and 'share/lot' but gives no 'property' and certainly no 'garden'.\"},\n  {\"src\":\"KNT\",\"where\":\"Kent, Old Persian lexicon\",\"stance\":\"partial\",\"note\":\"grep 'baga' in KNT.txt: Old Persian has baga- 'god' (Ahuramazdā bagānām baga) and bāji- 'tribute', i.e. the same root in the sister language, but no *bāga- 'garden'.\"},\n  {\"src\":\"POK\",\"where\":\"IEW p.107-108\",\"stance\":\"supports\",\"note\":\"'av. baga-, baγa- n. ‘Anteil, Los, bes. günstiges’ … npers. baγ ‘Gott’' — Pokorny lists the Avestan noun under this root, but among his Iranian reflexes there is no word for 'garden'.\"}\n ]})\n\nN.append({\n \"id\":2,\"lang\":\"Sogdian\",\"words\":\"bxš; bğ\",\"verdict\":\"confirmed\",\n \"derivation\":\"Both Sogdian words are genuine reflexes of the root. (a) βxš- (Gharib no. 2593, printed p.102) '(to) offer, (to) give', with the note '< *bag-, baxša-' and the cross-reference to the prefixed ʾnβxš- (no. 947, p.36) anβaxš/ambaxš '< *ham-baxša-, MP hambaxš' — the *-s- present of the root, i.e. the same formation as Avestan baxšaiti 'has or gives a share' and Persian baxšīdan. (b) βγ- (Gharib no. 2543, printed p.100) 'God, Lord, king, sir, excellency', explicitly '< baga', the ordinary Iranian development 'apportioner' → 'lord, god' seen also in Old Persian baga-, Parthian bg, and the Slavic loan/cognate bogŭ. Nourai's transliterations bxš and bğ reproduce Gharib's βxš / βγ with β written b and γ written ğ.\",\n \"derivation_fa\":\"هر دو واژهٔ سغدی بازماندهٔ راستین همین ریشه‌اند. نخست βxš- (قریب، مدخل ۲۵۹۳، ص ۱۰۲ چاپی) «بخشیدن، دادن» با ریشه‌شناسی «< *bag-, baxša-» و ارجاع به ʾnβxš- (مدخل ۹۴۷، ص ۳۶) anβaxš «آمرزیدن» از *ham-baxša- که در فارسی میانه hambaxš است؛ این همان ستاکِ -s- ریشه است که در اوستایی baxšaiti «بهره می‌دهد» و فارسی «بخشیدن» دیده می‌شود. دوم βγ- (مدخل ۲۵۴۳، ص ۱۰۰) «خدا، خداوند، سرور» با تصریح «< baga»؛ همان تحوّل معنایی همیشگی ایرانی «بخش‌کننده» ← «خداوند» که در پارسی باستان baga- و پارتی bg نیز هست. آوانگاری نورایی (bxš، bğ) همان βxš و βγ قریب است. ادعای نورایی درست است.\",\n \"sources\":[W_PIE],\n \"ref_check\":[\n  {\"ref\":\"SOD:100\",\"status\":\"supports\",\"note\":\"Gharib, Sogdian Dictionary, entry 2543 on printed p.100 (SOD_pages.txt \\\\f-leaf 166, running head '100'): 'βγ- (bγ-) B, M, S … ©<baga ©nom. ob. -y(y)h; acc. -w; voc. inst. abl. -ʾ; pl. βγyn, βγʾyst … God, Lord, king, sir, excellency'. Exactly Nourai's 'bğ : God'.\"},\n  {\"ref\":\"SOD:37\",\"status\":\"partial\",\"note\":\"Printed p.37 (SOD_pages.txt leaf 103) carries entries 942-955 (ʾnβrʾkw, ʾnβrytk, ʾncʾnh, ʾncmn …), i.e. the immediate neighbourhood of no. 947 ʾnβxš- 'anβaxš, ambaxš ©<*ham-baxša; MP hambaxš', whose page marker is '36' (leaf 102). The simplex βxš- itself is entry 2593 on printed p.102 (leaf 168): 'βxš- B, S … βaxš ©<bag-, baxša … (to)offer, (to)give'. So the citation lands on the prefixed compound of the same verb, one or two pages off the simplex — the material is there but the number is imprecise.\"}\n ],\n \"consulted\":[\n  {\"src\":\"SOD\",\"where\":\"Gharib nos. 947 (p.36), 2543 (p.100), 2593 (p.102)\",\"stance\":\"supports\",\"note\":\"see the quotations in ref_check; Gharib's own etymological brackets give '<*ham-baxša' and '<baga', i.e. the root of this chart.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"Cheung, Etym. Dict. of the Iranian Verb, root *baj (CHEUNG.txt line 1415 ff.)\",\"stance\":\"supports\",\"note\":\"'*baj ‘to bestow, divide, have a share; to give, apportion’ … SOGDIAN: BSogd. βγ- ‘to give, bestow’, SSogd. βxt° ‘luck, fortune’, MSogd. pr-βyn ‘gift’ … AVESTAN: baž- (baxš-) ‘to bestow, divide, give a share’ … OLD PERSIAN: bāj- ‘to bestow’.' Cheung's Sogdian entry is the same material.\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien\",\"stance\":\"silent\",\"note\":\"Persische Studien treats New Persian only; no Sogdian entry (grep 'sogd' round the bag- material gives nothing relevant).\"}\n ]})\n\nN.append({\n \"id\":3,\"lang\":\"Sanskrit\",\"words\":\"bhağa; bhağavant-gita; bhaga-dhara\",\"verdict\":\"disputed\",\n \"derivation\":\"Three words of very unequal standing. (a) bhaga- 'good fortune, prosperity; the apportioner, a god of wealth' is a textbook reflex of the root — Pokorny p.107 'ai. bhaga-ḥ ‘Gut, Glück’ … ‘Zuteiler, Herr, Beiname des Savitar’', Klein p.169 s.v. Bhaga. Confirmed. (b) The Gītā's title is Bhagavad-gītā, 'the song sung by the Blessed One', bhagavat- (bhaga- + suffix -vant-) in its sandhi form bhagavad- plus gītā, f. pp. of gā́yati 'sings' (PIE *gʷeh₂- / Nourai's root Gěi). The book prints the stem-form 'bhağavant-gita' — which is Klein's analysis ('compounded of Bhaga, suff. -vant … and gītá'), not an attested compound — and glosses it 'sound of sublime', a misprint for Klein's 'the song of the Sublime One'. I checked the printed page (pdf p.82, copy at data/verification/sources/refs/ocr/BOOK/82.png): the book itself has 'bhağavant-gita : sound of sublime', so the extraction is faithful and the fault is the author's. (c) bhaga-dhara- 'happiness-possessing' is not a real Sanskrit lexeme used of a hero; it is Theodor Benfey's 1862 conjecture (Orient und Occident I 137) about the origin of bahādur, reported — and immediately contested — by Hobson-Jobson and copied from there by Klein. Modern Turkology and Mongolistics reject it: baγatur is an Inner-Asian title attested centuries before any Indian contact, and Wiktionary derives Persian bahādor from Middle Mongol baɣatur. Hence 'disputed' for the node.\",\n \"derivation_fa\":\"سه واژه با اعتبارِ بسیار نابرابر. نخست bhaga- «بخت نیک، کامیابی؛ بخش‌کننده، نام ایزدی» که بازماندهٔ کلاسیک همین ریشه است (پوکورنی ص ۱۰۷: «ai. bhaga-ḥ ‘Gut, Glück’ … ‘Zuteiler, Herr’»، کلاین ص ۱۶۹). دوم نام «بهگودگیتا» که صورت درست آن Bhagavad-gītā است، یعنی bhagavat- (از bhaga- + پسوند -vant-) در صورت سندهیِ bhagavad- به‌علاوهٔ gītā «سرود» از ریشهٔ gā́yati «سرودن». کتاب ستاکِ «bhağavant-gita» را چاپ کرده — که تحلیل کلاین است نه ترکیبِ گواهی‌شده — و آن را «sound of sublime» معنی کرده، حال آنکه کلاین «the song of the Sublime One» (سرودِ آن بزرگوار) دارد. تصویر صفحهٔ چاپی بررسی شد: خطا از خودِ کتاب است، نه از خوانش اسکن. سوم bhaga-dhara- «دارندهٔ بخت» که اصلاً واژه‌ای سانسکریت به معنی «دلاور» نیست، بلکه حدسِ بنفای (۱۸۶۲) دربارهٔ خاستگاه «بهادر» است که هابسن‌جابسن آن را نقل و همان‌جا رد کرده است. پژوهش امروزی این را نمی‌پذیرد: baγatur عنوانی درون‌آسیایی است که قرن‌ها پیش از هرگونه تماس هندی گواهی دارد. داوری: پژوهش امروزی این گره را رد می‌کند.\",\n \"error_in\":\"book\",\n \"book_prints\":\"bhağavant-gita : sound of sublime\",\n \"correct_form\":\"Bhagavad-gītā 'the song of the Blessed/Sublime One'\",\n \"sources\":[W_BAH,W_PIE],\n \"ref_check\":[\n  {\"ref\":\"KLN:140\",\"status\":\"supports\",\"note\":\"Klein 1966, printed p.140 (KLN_1966.txt \\\\f-leaf 85, page markers '140','141'): 'bahadur, n., a title given to European officers in India. — Hind. bahādur, ‘hero’, which according to Benfey (in Orient und Occident 1 137, quoted in Hobson-Jobson 49a) derives fr. OI. bhaga-dhara-, ‘happiness-possessing’.' The page is exact and it is indeed where Nourai's 'bhaga-dhara' comes from — but Klein reports it as Benfey's opinion, not as fact.\"},\n  {\"ref\":\"HJB:49\",\"status\":\"partial\",\"note\":\"Hobson-Jobson s.v. BAHAUDUR (HJB.txt lines 2504-2510, printed p.49): 'Bahādur is one of the terms which the hosts of Chingiz Khan brought with them from the Mongol Steppes… In Sanang Setzen's poetical annals of the Mongols… the word is written Baghatur… Benfey has suggested that the word originated in Skt. bhaga-dhara (‘happiness-possessing’). But the late lamented Prof. A. Schiefner… was strongly of opinion that the word was rather a corruption… of the Zend bagha-puthra ‘Son of God’, and thus but another form of the famous term Faghfur.' The page supports Nourai's NOTE verbatim, but it presents bhaga-dhara as one rejected conjecture among several, and its own main statement is that the word is Mongol.\"},\n  {\"ref\":\"AHD\",\"status\":\"contradicts\",\"note\":\"Watkins 1985 s.v. bhag-¹ (AHD_watkins1985.txt line 323) lists only Greek phagein and Avestan bakhš-/Persian bakhšīdan under this root; neither bahadur nor Bhagavad-Gita is derived from it in the appendix, and 'bhaga-dhara' does not occur.\"}\n ],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"IEW pp.107-108\",\"stance\":\"partial\",\"note\":\"'ai. bhaga-ḥ ‘Gut, Glück’; av. baga-, baγa- n. ‘Anteil, Los’ … ai. bhaga-ḥ ‘Zuteiler, Herr, Beiname des Savitar’'. Confirms bhaga-, says nothing of a compound bhaga-dhara-.\"},\n  {\"src\":\"KLN\",\"where\":\"Klein p.169 s.v. Bhaga and Bhagavad-Gita (leaf 100)\",\"stance\":\"partial\",\"note\":\"'Bhaga, n., a god of wealth (Vedic mythol.) — OI. Bhagaḥ, lit. ‘allotter, distributer, master, lord’, fr. bhajati…' and 'Bhagavad-Gita … OI. Bhágavadgītā, ‘the song of the Sublime One’, compounded of Bhaga, suff. -vant … and gītá, ‘song’, prop. fem. pp. of gāyate, ‘sings’'. Klein's headword is Bhagavad-Gita (with -vad-), and his gloss is 'song', not 'sound' — the book's misprint is visible against this.\"},\n  {\"src\":\"AID\",\"where\":\"Whitworth, Anglo-Indian Dictionary\",\"stance\":\"silent\",\"note\":\"grep 'bahadur' in AID.txt finds only the proper name 'Tegh Bahādur' (line 5758); Whitworth has no etymological article on the word, so Nourai's 'AID' citation on node #8 has no substance for the Sanskrit claim either.\"}\n ]})\n\nN.append({\n \"id\":4,\"lang\":\"Indo-European\",\"words\":\"Bhag-los, Bhag-mos\",\"verdict\":\"plausible\",\n \"derivation\":\"These two reconstructions are taken verbatim from Mann and exist nowhere else. On IEC printed p.61 Mann has 'bhaĝlos (?) ‘enjoyment’. (Variant of bhag- (1), q.v.) … Per. bazla ‘jest’; Gk. cf. phágilos ‘eatable’' and 'bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia ‘feast’'. Both are back-formations from the very Persian words Nourai then hangs beneath them, supported only by loosely comparable Greek nouns; Mann himself marks the first with a question mark. Morphologically *bʰag-mo- and *bʰag-lo- are unobjectionable PIE noun types (thematic *-mo-/-lo- abstracts), and *bʰaǰ-ma- would in fact give Iranian *bazma- regularly, so the shapes are not impossible; but neither Pokorny nor Walde-Pokorny nor Watkins reconstructs them, and 'enjoyment, feasting' is Mann's gloss for both. Plausible as a proposal, not established.\",\n \"derivation_fa\":\"این دو بازسازی عیناً از فرهنگ منِ (Mann) گرفته شده و در هیچ فرهنگ دیگری نیست. من در صفحهٔ ۶۱ می‌نویسد: «bhaĝlos (?) ‘enjoyment’ … Per. bazla ‘jest’؛ Gk. phágilos» و «bhagmos ‘enjoyment, feasting’ … Per. bazm ‘feast’؛ Gk. phágema, phagésia». هر دو در واقع بازسازی وارونه از همان واژه‌های فارسی‌اند که نورایی زیرشان می‌آورد و تنها تکیه‌گاهشان چند اسم یونانی نه‌چندان دقیق است؛ خودِ من نخستین را با علامت پرسش آورده. از دید ساختواژی *bʰag-mo- و *bʰag-lo- الگوهای پذیرفتهٔ هندواروپایی‌اند (اسم‌های مجرد با پسوند ‑mo-/‑lo-) و *baǰ-ma- ایرانی به‌قاعده bazm می‌دهد؛ امّا نه پوکورنی، نه والده‑پوکورنی و نه واتکینز چنین صورت‌هایی نساخته‌اند. داوری: با احتیاط پذیرفتنی، نه اثبات‌شده.\",\n \"sources\":[],\n \"ref_check\":[\n  {\"ref\":\"IEC:61\",\"status\":\"supports\",\"note\":\"IEC.txt lines 1069-1071, on the leaf whose running head reads '61 bhaglos — bhaksó, ið': 'bhaĝlos (?) ‘enjoyment’. (Variant of bhag- (1), q. v.). See next Per. bazla ‘jest’; Gk. phágilos ‘eatable’' / 'bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia “feast”'. Nourai's box, gloss included, is a direct copy of these two lines.\"}\n ],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"IEW pp.107-108\",\"stance\":\"silent\",\"note\":\"Pokorny's bhag- article lists no *bhag-lo- or *bhag-mo- and no Persian bazm/bazla; his only New Persian item is baγ 'Gott'.\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 127-128\",\"stance\":\"silent\",\"note\":\"the article (leaves 131-132 of WLD_Bd2_pages.txt) has no -mo-/-lo- derivatives and no Persian nouns.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. bhag-¹\",\"stance\":\"silent\",\"note\":\"only *bhags- is given as an extended form; no *bhag-mo-/*bhag-lo-.\"}\n ]})\n\nN.append({\n \"id\":5,\"lang\":\"Persian\",\"words\":\"bâğ\",\"verdict\":\"confirmed\",\n \"derivation\":\"باغ bāγ 'garden' continues Middle Persian bāg ⟨bʾg⟩ (MacKenzie 'bāγ garden'), from Old Iranian/Proto-Iranian *bāgáh 'share, allotted portion' — the same *bʰeh₂g-o-s as Avestan bāga- and Sanskrit bhāgá-; Old Persian would give *bāga-. Phonetically nothing happens beyond the Middle Persian lenition of intervocalic/final -g and its New Persian realisation as ġ; the whole work is semantic: 'allotted share' → 'allotted plot of ground' → 'orchard, garden' (compare Persian بخش 'share' and بهر 'portion' from the same root, and the parallel Slavic *bogъ 'share > god'). Wiktionary states the chain as MP bʾg < PIr. *bāgáh < PII *bʰāgás < PIE *bʰeh₂g- + *-ós, i.e. exactly Horn's and Nourai's derivation. The chart's own NOTE is historically accurate — Hübschmann, Persische Studien p.23 ad Horn no. 169 writes 'Np. baγ ‘Garten’ stimmt zu skr. bhaga- ‘Teil, Anteil’ etc. in der Bedeutung durchaus nicht' — but modern Iranistics has come down on Horn's side, so the objection is now a historical footnote rather than a live dispute.\",\n \"derivation_fa\":\"«باغ» دنبالهٔ فارسی میانهٔ bāg ⟨bʾg⟩ است (مکنزی: «bāγ باغ») و آن از ایرانی باستان *bāgáh «بهره، قطعهٔ بخش‌شده»، همان *bʰeh₂g-o-s که در اوستایی bāga- و سنسکریت bhāgá- دیده می‌شود. از نظر آوایی جز نرم‌شدن g پایانی فارسی میانه و تلفّظ آن به‌صورت غ در فارسی نو چیزی رخ نداده؛ همهٔ کار بر دوش تحوّل معنایی است: «بهرهٔ بخش‌شده» ← «قطعه‌زمین واگذارشده» ← «بوستان، باغ» (سنجیدنی با «بخش» و «بهر» از همین ریشه، و با *bogъ اسلاوی «بهره ← خدا»). ویکی‌واژه همین زنجیره را می‌آورد و پس ادعای هرن و نورایی درست است. یادداشت نمودار نیز راست است: هوبشمان در «پژوهش‌های فارسی» ص ۲۳ نوشته «باغِ فارسی نو از نظر معنایی هیچ با bhaga- سنسکریت جور درنمی‌آید»؛ امّا ایران‌شناسی امروز جانب هرن را گرفته و ایراد هوبشمان اکنون تنها یادداشتی تاریخی است.\",\n \"sources\":[W_BAG],\n \"ref_check\":[\n  {\"ref\":\"HRN:39\",\"status\":\"supports\",\"note\":\"Horn no. 169, printed p.39: 'bāγ ‘Garten’. Wohl aw. bāga- ‘Loos’ (Y. 51,1); ai. bhāgá- ‘Teil, Eigentum’; phlv. bāg (PPGl.).' Nourai's arrow Avestan bāga- → Persian bāγ is Horn's, with Horn's hedge dropped.\"},\n  {\"ref\":\"AEF:224\",\"status\":\"not_checked\",\"note\":\"Persian translation of Horn, not online; the corresponding passage is Horn no. 169, quoted above.\"}\n ],\n \"consulted\":[\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien p.23, note on Horn no. 169 (HUB.txt line 742, \\\\f-leaf 34 which ends with the page marker '— 24 —')\",\"stance\":\"contradicts\",\"note\":\"'169. Np. baγ ‘Garten’ stimmt zu skr. bhaga- ‘Teil, Anteil’ etc. in der Bedeutung durchaus nicht.' Nourai's HUB:23 citation is exact, and Hübschmann's objection is purely semantic.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary, s.v. bāγ\",\"stance\":\"supports\",\"note\":\"Wiktionary's Further Reading cites MacKenzie 1971 for 'bāɣ' garden; the Pahlavi word ⟨bʾg⟩ is the link Horn already had from the Pahlavi-Pazand glossaries ('phlv. bāg (PPGl.)').\"},\n  {\"src\":\"BRT\",\"where\":\"AiW s.v. bāga- (BRT.txt line 17061)\",\"stance\":\"partial\",\"note\":\"'g. bāga- n. ‘Anteil, Los’ … Y.51.1' — the etymon exists with the meaning 'share', which is what the derivation needs; the 'garden' sense is Persian only.\"},\n  {\"src\":\"ARY\",\"where\":\"Aryanpur, Farhang-e rishe-hā\",\"stance\":\"silent\",\"note\":\"grep 'باغ' in incoming/ARY/ARY_pages.txt returns only پالیز/فالیز/باغبانی contexts, no headword باغ with an IE root.\"}\n ]})\n\nN.append({\n \"id\":6,\"lang\":\"Mongolian\",\"words\":\"\",\"verdict\":\"disputed\",\n \"derivation\":\"An empty pass-through box whose only content is the arrow: Sanskrit bhaga-dhara- → Mongolian (baγatur) → Persian bahādor. The Mongol word is real — Middle Mongol baγatur 'hero, valiant', Sanang Setzen's Baghatur, Yesügei Ba'atur the father of Chingiz — but the Sanskrit source is Benfey's 1862 guess, and Hobson-Jobson, the very page Nourai cites, already prints Schiefner's rejection of it in favour of Avestan baγa-puθra 'son of God' (= faghfūr), the alternative Nourai's own NOTE on node #3 records. Neither survives modern scrutiny: baγatur/bagatur is attested as a steppe title long before Indian or Sasanian contact could deliver either etymon (Danube-Bulgar and Türk usage, Greek Βαγατούρ in the 6th c.), and the standard handbooks (Doerfer, TMEN; Wiktionary) treat it as a native Inner-Asian (Turkic-Mongolic) word of uncertain further origin. The arrow into this box is therefore rejected; only the arrow out of it (node #7) stands.\",\n \"derivation_fa\":\"این جعبه واژه‌ای ندارد و تنها حاملِ پیکان است: سانسکریت bhaga-dhara- ← مغولی (baγatur) ← فارسی «بهادر». خودِ واژهٔ مغولی راست است — مغولی میانه baγatur «دلاور»، «باگاتور» در تاریخ سنانگ ستسن، و «یسوگای باگاتور» پدر چنگیز — امّا خاستگاه سانسکریت آن حدسِ بنفای (۱۸۶۲) است و هابسن‑جابسن در همان صفحه‌ای که نورایی ارجاع می‌دهد ردّیهٔ شیفنر را نیز آورده که به‌جای آن baγa-puθra اوستایی «پسر خدا» (= فغفور) را پیشنهاد می‌کند؛ همان که در یادداشت گرهٔ ۳ آمده است. هیچ‌یک از این دو امروز پذیرفته نیست: baγatur عنوانی استپی است که قرن‌ها پیش از هرگونه تماس هندی یا ساسانی گواهی دارد (نزد بلغارهای دانوب و ترکان، و به یونانی Βαγατούρ در سدهٔ ششم میلادی)، و دورفر و ویکی‌واژه آن را واژه‌ای بومیِ ترکی‑مغولی با خاستگاه نامعلوم می‌دانند. پس پیکانِ ورودی به این گره رد می‌شود و تنها پیکان خروجی (گرهٔ ۷) برجا می‌ماند.\",\n \"sources\":[W_BAH],\n \"ref_check\":[\n  {\"ref\":\"HJB:49\",\"status\":\"partial\",\"note\":\"Hobson-Jobson p.49 s.v. BAHAUDUR gives the Mongol history in detail ('Bahādur is one of the terms which the hosts of Chingiz Khan brought with them from the Mongol Steppes… written Baghatur… In Turki… Bātur… In Manchu… Baturu… the Kirghiz has it as Baṭyr'), so it fully supports 'Mongolian' as the immediate source of the Persian word; but on the Sanskrit link it records Benfey's suggestion only to set Schiefner's rebuttal against it, i.e. it does not support the arrow Sanskrit → Mongolian.\"}\n ],\n \"consulted\":[\n  {\"src\":\"HJB\",\"where\":\"Hobson-Jobson p.49 (HJB.txt line 2510)\",\"stance\":\"partial\",\"note\":\"see ref_check; the article's own conclusion is that the word came from the Mongol steppes, not from India.\"},\n  {\"src\":\"KLN\",\"where\":\"Klein p.140 s.v. bahadur\",\"stance\":\"partial\",\"note\":\"Klein gives 'Hind. bahādur ‘hero’' and only reports Benfey's Sanskrit derivation at second hand ('quoted in Hobson-Jobson 49a'); he does not endorse it.\"},\n  {\"src\":\"LKT\",\"where\":\"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs\",\"stance\":\"silent\",\"note\":\"grep 'bahadur|bagatur|baghatur' in LKT.txt: no entry — Lokotsch covers the word only if it entered a European language, which it did not (outside Russian bogatyr', which he files elsewhere).\"}\n ]})\n\nN.append({\n \"id\":7,\"lang\":\"Persian\",\"words\":\"bahâdor\",\"verdict\":\"confirmed\",\n \"derivation\":\"بهادر bahādor 'hero, valiant' is a Mongol loan of the Ilkhanid period: Middle Mongol baγatur was taken into Persian in the 13th century, when the Mongol military titulature (noyan, yasa, tümen, bahādor) entered Persian historiography with Juwaynī and Rashīd al-Dīn; Wiktionary dates the borrowing 'after the Mongol conquest in the 1200s'. Phonetically Mongol -γ- between vowels is rendered by Persian -h- (baγatur → bahādur), a substitution well attested in Turco-Mongol loans, and the -tur ending is fitted to the Persian -dor shape. From Persian it passed to Indo-Persian chancery usage and thence to Urdu/Hindi bahādur and English bahadur. Nourai's Mongolian → Persian arrow is right; only the Sanskrit ancestor above it is not.\",\n \"derivation_fa\":\"«بهادر» وام‌واژه‌ای مغولی از روزگار ایلخانان است: baγatur مغولی میانه در سدهٔ هفتم هجری/سیزدهم میلادی، همراه دیگر اصطلاحات لشکری مغول (نویان، یاسا، تومان، بهادر) و از راه تاریخ‌نویسانی چون جوینی و رشیدالدین به فارسی درآمد؛ ویکی‌واژه نیز وام‌گیری را «پس از فتح مغول در دههٔ ۱۲۰۰ میلادی» می‌داند. از نظر آوایی، غِ میان‌واکه‌ایِ مغولی در فارسی به «ه» بدل شده (baγatur ← بهادر) که در وام‌واژه‌های ترکی‑مغولی نمونه دارد، و پایانهٔ ‑tur به قالب فارسی ‑در درآمده. از فارسی به دیوان‌سالاری هند و از آنجا به اردو/هندی bahādur و انگلیسی bahadur رفته است. پس پیکان مغولی ← فارسی درست است؛ تنها نیای سانسکریتِ بالای آن نادرست است.\",\n \"sources\":[W_BAH,A_BAH],\n \"ref_check\":[\n  {\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"Mo'in, Farhang-e Fārsi s.v. بهادر: '(بَ دُ) [تر.] (ص.) دلیر، دلاور، شجاع' (abadis.ir فرهنگ معین section; the local MON_part1.txt line 26301 shows the same entry with the origin bracket OCRed as 'اآتر.]'). Mo'in marks the word a loan — from Turkish rather than Mongolian, but a steppe loan either way, which supports the arrow into this node and contradicts the Sanskrit ancestry.\"},\n  {\"ref\":\"BQT\",\"status\":\"supports\",\"note\":\"Dehkhoda s.v. بهادر opens 'بهادر. [ب َ دُ] (ص) شجاع و دلیر بکمال. (برهان)' — i.e. Borhan-e Qāṭeʿ is the authority for the meaning 'hero', exactly the gloss Nourai gives; Borhan offers no Indian etymology.\"}\n ],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in s.v. بهادر (via abadis.ir)\",\"stance\":\"supports\",\"note\":\"'[تر.] (ص.) دلیر، دلاور، شجاع' — a Turkic/steppe loanword adjective, no Sanskrit.\"},\n  {\"src\":\"BQT\",\"where\":\"Borhan-e Qāṭeʿ as quoted by Dehkhoda s.v. بهادر\",\"stance\":\"supports\",\"note\":\"'شجاع و دلیر بکمال. (برهان)'.\"},\n  {\"src\":\"HJB\",\"where\":\"Hobson-Jobson p.49\",\"stance\":\"supports\",\"note\":\"'In Persia it was often applied to slaves (Burton, Ar. Nights, iii. 114)… Bahādur is one of the terms which the hosts of Chingiz Khan brought with them from the Mongol Steppes' — the Mongol→Persian route stated outright.\"},\n  {\"src\":\"TTS\",\"where\":\"Vámbéry, Ćagataische Sprachstudien\",\"stance\":\"partial\",\"note\":\"Hobson-Jobson itself reports the form from Vámbéry: 'In Turki also this elision of the guttural extends to the spelling, and the word becomes Bātur, as we find it in the Dicts. of Vámbéry and Pavet de Courteille' — i.e. the word is at home in Turkic as well as Mongol.\"}\n ]})\n\nN.append({\n \"id\":8,\"lang\":\"English\",\"words\":\"Bhagavad-Gita; bahadur\",\"verdict\":\"disputed\",\n \"derivation\":\"The two English words do not share the route the chart draws for them. Bhagavad-Gita is a straightforward learned borrowing of the Sanskrit title (English from the later 18th century, after Charles Wilkins's 1785 translation), so for that word the Sanskrit parent node is correct. bahadur, however, is not a Sanskrit word in English: Klein's own entry (p.140) says 'Hind. bahādur, ‘hero’', i.e. English took it in British India from Urdu/Hindi, which had it from Persian, which had it from Mongol — the chain that runs through nodes #6 and #7, not through node #3. Hobson-Jobson (p.49) documents exactly this: the title conferred by the Great Mogul, 'Jones Sahib Bahādur', Rāi Bahādur, Khān Bahādur, 'Kumpanī Bahādur' for the East India Company. So the node's second word is misfiled under Sanskrit.\",\n \"derivation_fa\":\"این دو واژهٔ انگلیسی از یک راه نیامده‌اند. «Bhagavad-Gita» وام‌واژه‌ای کتابی و مستقیم از سانسکریت است (در انگلیسی از اواخر سدهٔ هجدهم، پس از ترجمهٔ چارلز ویلکینز در ۱۷۸۵) و برای این واژه گرهٔ سانسکریت درست است. امّا «bahadur» در انگلیسی از سانسکریت نیامده: خودِ کلاین در ص ۱۴۰ می‌نویسد «Hind. bahādur ‘hero’»، یعنی انگلیسی آن را در هند بریتانیا از اردو/هندی گرفته، اردو از فارسی، و فارسی از مغولی — همان زنجیره‌ای که از گره‌های ۶ و ۷ می‌گذرد، نه از گرهٔ ۳. هابسن‑جابسن (ص ۴۹) همین را مستند می‌کند: لقبی که پادشاهان مغولِ هند می‌دادند، «جونز صاحب بهادر»، «رای بهادر»، «خان بهادر» و «کمپانی بهادر». پس واژهٔ دوم این گره زیر سرشاخهٔ نادرست نشسته است.\",\n \"sources\":[W_BAH],\n \"ref_check\":[\n  {\"ref\":\"HJB\",\"status\":\"contradicts\",\"note\":\"Hobson-Jobson p.49 s.v. BAHAUDUR: 'H. Bahādur, ‘a hero, or champion.’ It is a title affixed commonly to the names of European officers in Indian documents… It was conferred as a title of honour by the Great Mogul' — 'H.' = Hindustani, and the article's history section derives the word from the Mongol steppes, not from Sanskrit.\"},\n  {\"ref\":\"AID\",\"status\":\"not_found\",\"note\":\"grep 'bahadur' in AID.txt (Whitworth, An Anglo-Indian Dictionary, 1885): the only hit is the personal name 'Tegh Bahādur' (line 5758); Whitworth has no headword bahadur, so this citation cannot be checked as given.\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1966 pp.140 and 169\",\"stance\":\"contradicts\",\"note\":\"'bahadur … — Hind. bahādur, ‘hero’' (p.140) versus 'Bhagavad-Gita … — OI. Bhágavadgītā' (p.169): Klein routes the two English words differently, exactly as objected here.\"},\n  {\"src\":\"HJB\",\"where\":\"Hobson-Jobson p.49\",\"stance\":\"contradicts\",\"note\":\"see ref_check.\"},\n  {\"src\":\"WEB\",\"where\":\"Webster (WEB_vol1.txt)\",\"stance\":\"silent\",\"note\":\"grep 'bahadur' in WEB_vol1.txt: no headword; the word is an Anglo-Indian regionalism rather than general English vocabulary.\"}\n ]})\n\nN.append({\n \"id\":9,\"lang\":\"Pahlavi\",\"words\":\"bazm\",\"verdict\":\"plausible\",\n \"derivation\":\"Middle Persian bazm 'meal, feast' is well attested — MacKenzie, Concise Pahlavi Dictionary p.19: 'bazm [bzm] meal, feast. ~-awurd [-ʾwlt] a sort of canapé', and his English index has 'feast bazm, sūr' and 'meal bazm, čāšt, mēzd, sūr'. Parthian/Middle Persian bazm is also the source of Old Armenian bazmim 'to recline at table, sit down to a meal' and bazmakan 'guest' (an Iranian loan already in the 5th-century Gospel translation, Mark 6:39). What is not established is the arrow: deriving it from Mann's *bhagmos. Formally the step is defensible — the palatalised root allomorph *bʰaǰ- (Skt. bhaj-, Av. baž-) plus *-ma- gives Old Iranian *baǰma- > *bazma- > bazm, and Hübschmann's own phonology section (p.75) files bazm among the words with Iranian zm — but Hübschmann, Persische Studien no. 215 (p.29), writes that it 'remains questionable whether the word is related to Skt. bhaj', and offers instead a link to Lithuanian bazmas 'crowd, mass' and native Armenian bazum 'much' (i.e. to the 'thick, abundant' root, Mann's bhaghus), if the original sense was 'assembly'. So a real alternative etymology stands beside Nourai's.\",\n \"derivation_fa\":\"«بزم» در فارسی میانه گواهی روشن دارد: مکنزی در «فرهنگ کوچک پهلوی» ص ۱۹ آورده «bazm [bzm] خوراک، بزم» و ترکیب «bazm-āwurd» (نوعی لقمه)، و در نمایهٔ انگلیسی «feast bazm, sūr» و «meal bazm, čāšt, mēzd, sūr». همین واژهٔ فارسی میانه/پارتی سرچشمهٔ ارمنیِ کهنِ bazmim «بر سفره نشستن» و bazmakan «مهمان» است که وام‌واژه‌ای ایرانی در ترجمهٔ انجیل سدهٔ پنجم میلادی (مرقس ۶:۳۹) است. آنچه اثبات‌نشده مانده پیکان است، یعنی بازگرداندن آن به *bhagmos منِ. از دید آوایی گام درست‌شدنی است: گونهٔ کامی‌شدهٔ ریشه (*bʰaǰ-، سنسکریت bhaj-، اوستایی baž-) با پسوند ‑ma- در ایرانی باستان *baǰma- > *bazma- > bazm می‌دهد، و خودِ هوبشمان در بخش آواشناسی (ص ۷۵) «بزم» را در شمار واژه‌های دارای zm ایرانی آورده. امّا هوبشمان در «پژوهش‌های فارسی» شمارهٔ ۲۱۵ (ص ۲۹) می‌نویسد پیوند این واژه با bhaj سانسکریت «مشکوک می‌ماند» و اگر معنای نخستین «انجمن» بوده، آن را به bazmas لیتوانیایی «انبوه» و bazum ارمنی «بسیار» می‌پیوندد. پس ریشه‌شناسی رقیبی در کنار ادعای نورایی هست. داوری: با احتیاط پذیرفتنی.\",\n \"sources\":[W_BAZM],\n \"ref_check\":[\n  {\"ref\":\"MON:523\",\"status\":\"not_checked\",\"note\":\"The print edition of Mo'in's Farhang-e Fārsi carries the Pahlavi/Avestan forms in Latin script that Nourai is citing, but the digital text available here (MON_part1.txt) has no page numbering and reproduces only 'بزم: (اِ.) مجلس شراب و طرب و مهمانی و ضیافت…' without an etymological bracket, so vol.1 p.523 could not be confirmed. The Pahlavi form itself is independently verified from MacKenzie (see consulted).\"}\n ],\n \"consulted\":[\n  {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary, s.v. bazm (PHD.txt line 256); English index lines 1904, 2755\",\"stance\":\"supports\",\"note\":\"'bazm [bzm] meal, feast. ~-awurd [-ʾwlt | N ~] a sort of canapé'; index 'feast bazm, sūr' and 'meal bazm, čāšt, mēzd, sūr'. The Pahlavi word and its meaning are exactly as Nourai has them.\"},\n  {\"src\":\"NYB\",\"where\":\"Nyberg, Manual of Pahlavi II (glossary)\",\"stance\":\"silent\",\"note\":\"grep 'bazm|bzm' in NYB_vol2_glossary.txt: no hit; Nyberg's glossary covers only the texts he edits.\"},\n  {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien no. 215, p.29 (HUB.txt lines 951-957) and the phonology section p.75 (line 7975)\",\"stance\":\"partial\",\"note\":\"'215. Zu bazm ‘Gesellschaft, Gastmahl, Gelage’ (Fird. I, 23,13), afgh. LW. bazm … gehört … das arm. LW. bazmel ‘sich zu Tische setzen’ … bazmakan ‘der zu Tische sitzt, Gast’ … Fraglich bleibt, ob das Wort mit skr. bhaj verwandt ist. Wäre die ursprüngliche Bedeutung ‘Versammlung’ gewesen, liesse es sich zu lit. bazmas ‘Menge, Masse’, echt arm. bazum ‘viel’ etc. stellen.' And p.75: 'ūriran. zm … = ap. np. zmi, bazm ‘Gastmahl’, arm. bazmakan ‘Gast’, siehe oben p.29; razm ‘Schlacht’…'\"},\n  {\"src\":\"CHEUNG\",\"where\":\"Cheung, root *baj (CHEUNG.txt line 1415 ff.)\",\"stance\":\"silent\",\"note\":\"Cheung lists Avestan baž-/baxš-, OP bāj-, Khotanese buss-, Sogdian βγ-, but no nominal *bazma- and no Middle Persian bazm under this root.\"}\n ]})\n\nN.append({\n \"id\":10,\"lang\":\"Persian\",\"words\":\"bazm\",\"verdict\":\"confirmed\",\n \"derivation\":\"New Persian بزم bazm 'feast, banquet, convivial assembly' is the direct continuation of the Middle Persian word of node #9, unchanged in form (a monosyllabic stem ending in a consonant cluster passes from Pahlavi to New Persian untouched: bazm, razm, xašm). It is the standard Shahnameh word for the courtly drinking-party paired with razm 'battle' — Hübschmann cites Firdausi I 23,13 — and the chart's 'extra' بزم‌آرا bazm-ārā 'feast-adorner' is the regular Persian agent compound with the present stem ārā- of آراستن. Mo'in glosses it 'مجلس شراب و طرب و مهمانی و ضیافت' and lists بزم‌آرای in his next entry, so the box (including the parenthesised compound) matches the dictionary. Only the ancestry above the Pahlavi node is open (see #9).\",\n \"derivation_fa\":\"«بزم» فارسی نو دنبالهٔ بی‌واسطهٔ همان واژهٔ فارسی میانهٔ گرهٔ ۹ است و صورت آن هیچ دگرگونی نیافته؛ ستاک‌های تک‌هجایی که به خوشهٔ همخوانی ختم می‌شوند از پهلوی به فارسی نو دست‌نخورده می‌رسند (بزم، رزم، خشم). این واژه در شاهنامه همواره در برابر «رزم» می‌نشیند و هوبشمان شاهد فردوسی (دفتر یکم، ۲۳/۱۳) را می‌آورد. «بزم‌آرا» که در نمودار در کنار آن آمده، ترکیب فاعلی به‌قاعده با ستاک حال «آرا» از «آراستن» است. معین نیز «بزم» را «مجلس شراب و طرب و مهمانی و ضیافت» معنی کرده و بلافاصله «بزم‌آرای» را مدخل ساخته است؛ پس محتوای جعبه با فرهنگ‌ها می‌خواند. تنها نیای بالادستِ گرهٔ پهلوی جای گفت‌وگو دارد (نگاه کنید به گرهٔ ۹). ادعای نورایی در این گره درست است.\",\n \"sources\":[W_BAZM],\n \"ref_check\":[\n  {\"ref\":\"MON:523\",\"status\":\"partial\",\"note\":\"The entry is in Mo'in (MON_part1.txt line 23136): 'بزم: (اِ.) مجلس شراب و طرب و مهمانی و ضیافت. محفل و انجمن و مجلس انس… بزم سنگین: بزمی که در آن مردم بسیار جمع باشند', immediately followed by 'بزم‌آرای: [= بزم آراینده] (افا.) آنکه مجلس عیش و مهمانی را آرایش می‌کند، بزم آرا' — i.e. both the headword and the chart's extra بزم آرا are Mo'in's. The volume/page (vol.1 p.523) could not be verified: the local digital text has no pagination.\"},\n  {\"ref\":\"IEC:61\",\"status\":\"supports\",\"note\":\"Mann's entry 'bhagmos ‘enjoyment, feasting’ … Per. bazm ‘feast’' (IEC.txt line 1071) is exactly the Persian word and gloss Nourai puts in this box.\"}\n ],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in s.v. بزم and بزم‌آرای\",\"stance\":\"supports\",\"note\":\"see ref_check; no origin bracket is given, i.e. Mo'in treats it as inherited Persian (he brackets loans, e.g. '[ع.]', '[تر.]').\"},\n  {\"src\":\"HUB\",\"where\":\"Persische Studien no. 215, p.29\",\"stance\":\"supports\",\"note\":\"'bazm ‘Gesellschaft, Gastmahl, Gelage’ (Fird. I, 23,13)… Dazu np. bazmgāh ‘Ort des Gelages’, bazma ‘angulus in loco compotationis’' — the New Persian word and its derivatives.\"},\n  {\"src\":\"PHD\",\"where\":\"MacKenzie s.v. bazm\",\"stance\":\"supports\",\"note\":\"'bazm [bzm] meal, feast' — the Pahlavi antecedent, unchanged in New Persian.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss\",\"stance\":\"silent\",\"note\":\"grep 'bazm|Gastmahl|Gelage' in HRN.txt: Horn has jašn (no. 422), sūr (no. 753) and mēyazd (no. 1007) for 'Fest, Gelage' but no article on bazm.\"}\n ]})\n\nN.append({\n \"id\":11,\"lang\":\"Persian\",\"words\":\"bazleh\",\"verdict\":\"disputed\",\n \"derivation\":\"بذله bazle 'jest, witticism' is an Arabic loan, not an Indo-European inheritance. The spelling is decisive: the second radical is ذ (dhāl), a letter used in Persian orthography essentially only in Arabic loans, and the word belongs to the Arabic root b-dh-l بذل 'to give freely, expend, lavish' (verbal noun بَذْل, nomen vicis/speciei بَذْلَة). Dehkhoda marks the headword '(ع اِ)' = Arabic noun and gives both Arabic senses, 'everyday clothing' and 'freely-given (witty) speech'; Mo'in glosses it '(بَ لِ) (اِ.) شوخی، لطیفه' and tags cognate بذال as '[ع.]'. The 'jest' sense is the literary Persian and Arabic development of 'something given away freely' (a witticism lavished on the company). Nourai takes it from Mann, IEC p.61, who prints under his private reconstruction 'bhaĝlos (?) ‘enjoyment’ … Per. bazla ‘jest’' — Mann evidently read the Persian word as containing z and matched it to Greek phágilos; the ذ shows the analysis cannot stand. The chart's own NOTE ('MON derives this from Arabic') is correct, and modern scholarship is with MON.\",\n \"derivation_fa\":\"«بذله» وام‌واژه‌ای عربی است، نه میراث هندواروپایی. املا خود گواه است: همخوان دوم «ذ» است و این حرف در املای فارسی جز در واژه‌های عربی به‌کار نمی‌رود؛ واژه از ریشهٔ عربی ب‑ذ‑ل «بخشیدن، ارزانی داشتن» است (مصدر «بَذْل»، صورت «بَذْلَة»). دهخدا مدخل را «(ع اِ)» یعنی اسم عربی نشانه‌گذاری کرده و هر دو معنای عربی («جامهٔ روزمرّه» و «سخن ارزانی‌شده، لطیفه») را می‌آورد؛ معین آن را «(بَ لِ) (اِ.) شوخی، لطیفه» معنی می‌کند و «بذّال» هم‌ریشه را «[ع.]» می‌نشانَد. معنای «لطیفه» تحوّل ادبیِ «آنچه به رایگان بخشیده شود» است. نورایی این را از منِ (IEC ص ۶۱) گرفته که زیر بازسازی شخصی خود «bhaĝlos (?) ‘enjoyment’ … Per. bazla ‘jest’» آورده است؛ پیداست من واژه را با «ز» خوانده و با phágilos یونانی سنجیده، حال آنکه «ذ» این تحلیل را باطل می‌کند. یادداشت خودِ نمودار («معین آن را عربی می‌داند») درست است و پژوهش امروزی جانب معین را می‌گیرد. داوری: پژوهش امروزی این ادعا را رد می‌کند.\",\n \"sources\":[A_BAZL],\n \"ref_check\":[\n  {\"ref\":\"IEC:61\",\"status\":\"supports\",\"note\":\"IEC.txt line 1069-1070: 'bhaĝlos (?) ‘enjoyment’. (Variant of bhag- (1), q. v.). See next Per. bazla ‘jest’; Gk. phágilos ‘eatable’'. Nourai reports Mann accurately — the page is exact and the claim is Mann's — but Mann's question mark and the Arabic spelling both undercut it.\"},\n  {\"ref\":\"MON:489\",\"status\":\"partial\",\"note\":\"Mo'in's بذله is not in the digital text available here (the headword is missing from MON_part1.txt, which has only بذّال '[ع.] (ص.) بسیار بذل کننده' at line 21789); via abadis.ir the فرهنگ معین entry reads '(بَ لِ) (اِ.) شوخی، لطیفه'. Mo'in's Arabic tagging of the b-dh-l family, and Dehkhoda's explicit '(ع اِ)' on بذله itself, confirm the NOTE that MON makes it Arabic; the page number vol.1 p.489 could not be checked (no pagination in the local text).\"}\n ],\n \"consulted\":[\n  {\"src\":\"MON\",\"where\":\"Farhang-e Mo'in s.v. بذله (via abadis.ir) and s.v. بذّال (MON_part1.txt line 21789)\",\"stance\":\"contradicts\",\"note\":\"'بذله: (بَ لِ) (اِ.) شوخی، لطیفه'; 'بذال: [ع.] (ص.) بسیار بذل کننده' — the family is marked Arabic.\"},\n  {\"src\":\"BQT\",\"where\":\"Dehkhoda (which reproduces Borhan and Mo'in's notes) s.v. بذله, via abadis.ir\",\"stance\":\"contradicts\",\"note\":\"the entry opens '(ع اِ)' = Arabic noun, with the two senses 'everyday clothing' and 'witty discourse'.\"},\n  {\"src\":\"HRN\",\"where\":\"Horn, Grundriss\",\"stance\":\"silent\",\"note\":\"grep 'bazl|bazle' in HRN.txt: no entry — Horn's Grundriss deliberately excludes Arabic loans, which is itself an argument.\"},\n  {\"src\":\"POK\",\"where\":\"IEW pp.107-108\",\"stance\":\"silent\",\"note\":\"no Persian noun of this shape under bhag-.\"}\n ]})\n\nN.append({\n \"id\":12,\"lang\":\"Greek\",\"words\":\"phagein\",\"verdict\":\"confirmed\",\n \"derivation\":\"Greek φαγεῖν phageîn 'to eat' is the classic and uncontested reflex of this root: it is a suppletive aorist infinitive (aor. ἔφαγον éphagon) serving ἐσθίω 'I eat', and its semantics — 'to have got one's share (of food)' → 'to eat' — is the reason Pokorny, Walde-Pokorny, Watkins and Klein all put it here. Pokorny p.108: 'gr. φαγεῖν ‘essen’, σιτο-φάγος ‘Getreide essend’'; Watkins: 'Greek phagein, to eat (< “to have a share of food”)'. In Greek the root shows no *-s- extension (contrast Avestan baxšaiti, Sanskrit bhakṣati); the plain thematic aorist stem phag- is what all the English combining forms are built on.\",\n \"derivation_fa\":\"یونانی φαγεῖν (phageîn) «خوردن» بازماندهٔ کلاسیک و بی‌چون‌وچرای این ریشه است: مصدر ماضی سادهٔ مکمِّلِ ἐσθίω «می‌خورم» است (ماضی ἔφαγον) و همین تحوّل معنایی — «بهرهٔ خود از خوراک را گرفتن» ← «خوردن» — سبب شده پوکورنی، والده‑پوکورنی، واتکینز و کلاین همگی آن را ذیل همین ریشه بیاورند. پوکورنی ص ۱۰۸: «gr. φαγεῖν ‘essen’، σιτο-φάγος ‘غله‌خوار’»؛ واتکینز: «Greek phagein, to eat (< ‘to have a share of food’)». در یونانی برخلاف اوستایی baxšaiti و سنسکریت bhakṣati پسوند ‑s‑ نیامده و همین ستاک سادهٔ phag- پایهٔ همهٔ ترکیب‌های انگلیسی است. ادعای نورایی درست است.\",\n \"sources\":[W_PIE,E_ESO],\n \"ref_check\":[\n  {\"ref\":\"IEC:61\",\"status\":\"partial\",\"note\":\"Mann's Greek material for this root is on printed p.60 in the main entry ('Gk. éphagon (aor. 1sg. ‘ate’); -phagos (cpds.)') and on p.61 only in the derived entries ('Gk. phágilos ‘eatable’', 'Gk. cf. phágema ‘food’, phagésia “feast”'). So IEC:61 does carry Greek phag- words, but the plain infinitive phageîn is Mann's p.60 item.\"}\n ],\n \"consulted\":[\n  {\"src\":\"POK\",\"where\":\"IEW p.108 (POK_01.txt leaf 117)\",\"stance\":\"supports\",\"note\":\"'gr. φαγεῖν ‘essen’, σιτο-φάγος ‘Getreide essend’, usw.'\"},\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 128 (WLD_Bd2_pages.txt leaf 132)\",\"stance\":\"supports\",\"note\":\"'gr. φαγεῖν „essen“, lokr. παμπασιοφαγεῖσθαι „mit Konfiskation betroffen werden“.'\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. bhag-¹\",\"stance\":\"supports\",\"note\":\"'1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS.'\"},\n  {\"src\":\"KLN\",\"where\":\"Klein 1966 s.v. -phagous (KLN_1966.txt leaf 624, p.1169)\",\"stance\":\"supports\",\"note\":\"'Gk. -φάγος, ‘eater of’, from the stem of φαγεῖν, ‘to eat’, which is cogn. with OI. bhajati … Avestic baγa-, OPers. baga-, ‘master, god’, lit. ‘distributor’… All these words derive fr. I.-E. base *bhag-, ‘to distribute, share out’.'\"}\n ]})\n\nN.append({\n \"id\":13,\"lang\":\"English\",\"words\":\"-phagos; -phagy; phagocyte; phagomania; phagophobia; esophagus\",\"verdict\":\"confirmed\",\n \"derivation\":\"All six are learned Greek-based formations on the stem of φαγεῖν and thus genuinely belong under node #12. -phagous/-phage render Greek -φάγος 'eater of'; -phagy/-phagia render -φαγία; phago- is the combining form. phagocyte was coined by Élie Metchnikoff in 1884 (Greek phago- + kytos 'hollow vessel, cell') for the 'eating cells' of the immune system, and phagomania (compulsive eating) and phagophobia (morbid fear of eating/swallowing) are 19th-20th-century medical Greek of the same kind. esophagus is older and slightly different: Greek οἰσοφάγος oisophágos, literally 'what carries and eats', from οἴσω oísō (future of φέρω 'carry', PIE *bher-) + the phag- stem; it entered English in the late 14th century through Late Latin oesophagus. So the second element only is from this root — Watkins accordingly lists ESOPHAGUS under *bher-¹ as well.\",\n \"derivation_fa\":\"هر شش صورت ساخته‌های عالمانه بر پایهٔ ستاک یونانی φαγεῖν‌اند و به‌درستی زیر گرهٔ ۱۲ می‌نشینند. ‑phagous/‑phage برابر ‑φάγος «خورندهٔ …»، ‑phagy/‑phagia برابر ‑φαγία، و phago‑ صورت ترکیبی آن است. «phagocyte» را الی مچنیکوف در ۱۸۸۴ ساخت (phago- + kytos «یاخته») برای یاخته‌های بیگانه‌خوار دستگاه ایمنی؛ «phagomania» و «phagophobia» نیز از همین گونهٔ یونانیِ پزشکیِ سده‌های نوزدهم و بیستم‌اند. «esophagus» کهن‌تر و اندکی متفاوت است: یونانی οἰσοφάγος «آنچه می‌بَرد و می‌خورد» از οἴσω (مضارع آیندهٔ φέρω «بردن»، از ریشهٔ *bher-) و ستاک phag-؛ از راه لاتینی متأخر oesophagus در اواخر سدهٔ چهاردهم به انگلیسی رسیده. پس در این واژه تنها جزء دوم از ریشهٔ حاضر است و واتکینز آن را ذیل *bher-¹ نیز فهرست می‌کند. ادعای نورایی درست است.\",\n \"sources\":[E_ESO],\n \"ref_check\":[\n  {\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. bhag-¹: '-PHAGE, -PHAGIA, PHAGO-, -PHAGOUS'; the AHD word index (AHD_watkins1985.txt line 2084) lists '-PHAGE bhag-1  -PHAGIA bhag-!  PHAGO- bhag-1  -PHAGOUS bhag-!'. Exactly Nourai's list of combining forms.\"},\n  {\"ref\":\"IEC:62\",\"status\":\"not_found\",\"note\":\"Printed p.62 of Mann (IEC.txt lines 1090-1096, between the running heads '61 bhaglos — bhaksó, ið' and '63 bhakos, ā — bhand- 64') runs bhaius, bhak-/bhakolos, bhakor, bhakos, bhaks-, bhakso — none of it about Greek phag- or its English derivatives. Mann's -phagos material is on p.60 in the bhag- article. The citation does not lead to the claim.\"}\n ],\n \"consulted\":[\n  {\"src\":\"KLN\",\"where\":\"Klein 1966 p.1169 s.v. -phagous, -phagy\",\"stance\":\"supports\",\"note\":\"'-phagous, combining form meaning ‘eating, feeding on’, as in creophagous, xylophagous. — Gk. -φάγος … Cp. the second element in esophagus. Cp. also bahadur, baksheesh, Bhaga, Bhagavad-Gita.' — Klein even groups the same set of words Nourai's chart does.\"},\n  {\"src\":\"SKT\",\"where\":\"Skeat s.v. Esophagus (SKT.txt line 5994)\",\"stance\":\"supports\",\"note\":\"'Esophagus, gullet, [L.-Gk.] Late L. œsophagus. — Gk. οἰσοφάγος, the gullet, lit. conveyer of food. — Gk. οἴσω, I shall carry, from a base oi-, to carry; φαγ-, base of φαγεῖν, to eat.'\"},\n  {\"src\":\"FSD\",\"where\":\"Funk & Wagnalls, Standard Dictionary (FSD_vol3.txt lines 143405-143408, 98065)\",\"stance\":\"supports\",\"note\":\"the phagocyte family is entered in full ('phag'o-cy''tal, a. Of or pertaining to a phagocyte', 'phagocytoblast', 'phagocytolysis', and the definition 'upon the ingestion of pathogenic bacteria by phagocytes'), confirming the English words are real technical vocabulary.\"}\n ]})\n\ne0[\"nodes\"]=N\njson.dump(e0, open(SP+'e0full.json','w'), ensure_ascii=False)\nprint(\"nodes\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82b.py",
 "description": "Build entry 0 nodes"
}
```


### [2026-09-05T06:29:30.587Z] TOOL RESULT

```
nodes 13
```


## [2026-09-05T06:31:52.339Z] TOOL CALL #75: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82c.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nSP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\ne0=json.load(open(SP+'e0full.json'))\n\nW_BAZU = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88\"\nE_BOW  = \"https://www.etymonline.com/word/bow\"\n\ne1={\n \"entry\":1,\n \"root\":\"Bhâghu\",\n \"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *bʰeh₂ǵʰu- / *bʰāǵʰu-s 'arm, forearm, elbow' (Pokorny bhāghū-s 108; Watkins bhaghu-)\",\n \"note\":\"Root, language label, gloss and page citation are all correct. Pokorny p.108 heads the article 'bhāghū-s ‘Ellbogen und Unterarm’' — literally Nourai's 'elbow, arm' — and lists ai. bāhú-ḥ, av. bāzāuš/bāzvō, gr. πῆχυς (Aeol.-Dor. πᾶχυς), aisl. bōgr, ags. bōg, ahd. buog, toch. A/B poke, B pauke. Mann has the same set at IEC p.61 ('bhāĝhus ‘arm, forearm, upper arm, shoulder’. WP II, 130') and Watkins abbreviates it to 'bhaghu-. Arm. Germanic *bōguz in Old English bōg, boh, bough: BOUGH. [Pok. bhāghū-s 108.]'. In modern laryngeal notation the reconstruction is *bʰeh₂ǵʰus (Wiktionary), with a palatal *ǵʰ (whence Indo-Iranian *ȷ́ʰ, Skt. h, Iranian z) — which is why the Iranian reflex has -z- while Greek and Germanic show plain velars. This root is unrelated to the Bhag root of entry 0 despite the similar look; the chart keeps them properly apart.\",\n \"note_fa\":\"صورت ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست است. پوکورنی در ص ۱۰۸ می‌نویسد «bhāghū-s ‘Ellbogen und Unterarm’» یعنی همان «آرنج، بازو»ی نورایی، و این‌ها را برمی‌شمارد: سنسکریت bāhú-، اوستایی bāzāuš/bāzvō، یونانی πῆχυς، نروژی کهن bōgr، انگلیسی کهن bōg، آلمانی علیای کهن buog، تخاری poke/pauke. من نیز در IEC ص ۶۱ همین را دارد و واتکینز به‌کوتاهی «bhaghu-. Arm.» می‌آورد. در نگارش امروزی این ریشه *bʰeh₂ǵʰus است با *ǵʰِ کامی که در هندوایرانی به *ȷ́ʰ و در ایرانی به z بدل می‌شود؛ به همین سبب است که صورت ایرانی «ز» دارد ولی یونانی و ژرمنی همخوان نرم‌کامی نشان می‌دهند. این ریشه با ریشهٔ Bhag در مدخل پیشین هیچ نسبتی ندارد و نمودار نیز آن دو را جدا نگاه داشته است.\",\n \"sources\":[W_BAZU],\n \"ref_check\":[\n  {\"ref\":\"POK:108\",\"status\":\"supports\",\"note\":\"Pokorny IEW p.108 (POK_01.txt \\\\f-leaf 118, right after the page marker '108'): 'bhāghū-s ‘Ellbogen und Unterarm’. Ai. bāhú-ḥ m. ‘Arm, bes. Unterarm; bei Tieren Vorderfuß’, av. bāzāuš ‘Arm’, Gen. bāzvō (arm. bazuk aus dem Iran.); gr. πῆχυς, äol.-dor. πᾶχυς ‘Ellbogen, Unterarm’, aisl. bōgr, Akk. Pl. bōgu ‘Arm, Schulter’, ags. bōg ‘Schulter, Arm; Zweig’, ahd. buog (nhd. Bug) ‘Schulter, Hüfte, Bug des Tieres’; toch. A B poke, B pauke ‘Arm’. WP. II 130.' Page and gloss exact.\"}\n ],\n \"consulted\":[\n  {\"src\":\"WLD\",\"where\":\"Walde-Pokorny II 130 (incoming/WLD/WLD_Bd2_pages.txt leaf 134, running head '130')\",\"stance\":\"supports\",\"note\":\"the page refers to '*bhāghus ‘Ellbogen und Unterarm’' when discussing whether the Germanic bag-/bāg- 'streiten' family could belong with it — confirming that WP II 130 is where this root stands, exactly as Pokorny's back-reference says.\"},\n  {\"src\":\"IEC\",\"where\":\"Mann, IEC printed p.61 (IEC.txt line 1077)\",\"stance\":\"supports\",\"note\":\"'bhāĝhus ‘arm, forearm, upper arm, shoulder’. WP II, 130 Skt. bāhúḥ; Av. bāzuš; Arm. dim. bazuk ‘forearm’; Oss. dim. bazug, bazig ‘shoulder-blade’; Tokh. A poke, B pauke ‘arm’; OHG buoc, buac ‘bend’; MHG buoc ‘upper arm’; OE bōg ‘arm, shoulder, bough’; ON bōgr…'\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. bhaghu- (AHD_watkins1985.txt line 323)\",\"stance\":\"supports\",\"note\":\"'bhaghu-. Arm. Germanic *bōguz in Old English bōg, boh, bough: BOUGH. [Pok. bhāghū-s 108.]'\"}\n ],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Avestan\",\"words\":\"bâzu, bâzâu\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Avestan bāzu- 'arm' is a u-stem; Bartholomae's headword is 'j. bāzav- m. 1) ‘Arm’ der Menschen und Götter' (the -av- citation form of a u-stem), with the attested nom. sg. bāzāuš and gen. sg. bāzvō, and compounds such as darəgō.bāzav- 'long-armed' (Artaxerxes' epithet Longimanus), uzbāzav- 'raising the arms', uγra.bāzav- 'strong-armed' and the technical term bāzu.jata- (a degree of sin). Nourai's two forms are therefore the same word twice: bâzu = the stem bāzu-, bâzâu = Bartholomae's bāzav-/the nominative bāzāuš. Both are correct; the root is *bʰeh₂ǵʰu-, with palatal *ǵʰ > Indo-Iranian *ȷ́ʰ > Avestan z (Sanskrit bāhú- shows h from the same source).\",\n   \"derivation_fa\":\"اوستایی bāzu- «بازو» ستاکی است با پایانهٔ u؛ سرمدخل بارتولومه «bāzav- (مذکر) ‘بازوی مردمان و ایزدان’» است (صورت ارجاعی ستاک‌های u)، با صورت‌های گواهی‌شدهٔ فاعلی bāzāuš و اضافی bāzvō و ترکیب‌هایی چون darəgō.bāzav- «دراز‌بازو» (لقب اردشیر درازدست)، uzbāzav- «بازو برافرازنده» و uγra.bāzav- «نیرومندبازو». پس دو صورتی که نورایی آورده یک واژه‌اند: bâzu همان ستاک bāzu- و bâzâu همان bāzav-/bāzāuš بارتولومه. ریشه *bʰeh₂ǵʰu- است و *ǵʰِ کامی آن در هندوایرانی به *ȷ́ʰ و در ایرانی به z بدل شده (در سنسکریت bāhú- همان آوا به h رسیده). ادعای نورایی درست است.\",\n   \"sources\":[W_BAZU],\n   \"ref_check\":[\n    {\"ref\":\"POK:108\",\"status\":\"supports\",\"note\":\"'av. bāzāuš ‘Arm’, Gen. bāzvō' — Pokorny gives precisely the two shapes Nourai prints (stem and nominative/av- form).\"},\n    {\"ref\":\"KLN:190\",\"status\":\"supports\",\"note\":\"Klein 1966, printed p.190 (KLN_1966.txt \\\\f-leaf 111, whose neighbours carry the page markers 191/193): 'bough, n. — ME. bogh, fr. OE. bōg, bōh, ‘arm, shoulder, bough’, rel. to ON. bogr, ‘shoulder; bow of a ship’, OHG. buog, MHG. buoc, G. Bug, ‘shoulder, hock, joint’, fr. I.-E. *bhāghus-, ‘elbow, arm’, whence also OI. bāhuḥ, Avestic bāzu, Arm. bazuk, ‘arm’, Gk. πῆχυς, Dor. πᾶχυς ‘elbow’, Toch. A poke, B pauke, ‘arm’. Cp. bow, ‘the fore part of a ship’.' The page is exact and it covers both this node and nodes #3-#4.\"}\n   ],\n   \"consulted\":[\n    {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW s.v. bāzav- (BRT.txt line 17125; compounds at lines 8118, 8661, 12909, 17111)\",\"stance\":\"supports\",\"note\":\"'j. bāzav- m. 1) ‘Arm’ der Menschen und Götter'; 'j. uγra.bāzav- Adj. ‘starkarmig’'; 'j. uz-bāzav- Adj. ‘die Arme emporhebend’'; 'g. darəgō.bāzav-, j. darəšō.bāzav- Adj. ‘langarmig’'; 'j. bāzu.jata- n. Term. techn.' Mo'in's footnote to Borhan cites this material as 'بارتولمه ۹۵۶'.\"},\n    {\"src\":\"KNT\",\"where\":\"Kent, Old Persian\",\"stance\":\"silent\",\"note\":\"grep 'bazu|bāzu' in KNT.txt gives no Old Persian attestation of the noun in the inscriptions; Wiktionary nevertheless posits OP bāzu (𐎲𐎠𐏀𐎢) as the immediate Persian antecedent, i.e. reconstructed rather than attested.\"},\n    {\"src\":\"IEC\",\"where\":\"Mann p.61 s.v. bhāĝhus\",\"stance\":\"supports\",\"note\":\"'Av. bāzuš; Arm. dim. bazuk ‘forearm’; Oss. dim. bazug, bazig ‘shoulder-blade’.'\"}\n   ]},\n  {\"id\":2,\"lang\":\"Persian\",\"words\":\"bâzŭ\",\"verdict\":\"confirmed\",\n   \"derivation\":\"بازو bāzu 'upper arm' continues Old Iranian *bāzu- unchanged in its consonants; Middle Persian has bāzā ⟨bʾcʾy⟩ (MacKenzie: 'bāzā [bʾcʾy | (N bāzū)] arm', with bāzā-banag 'arm-guard, brassard'), and the New Persian shape bāzū is the u-stem restored/generalised. Mo'in's own etymological footnote in Borhan-e Qāṭeʿ p.220 gives the chain explicitly: 'بازو ـ در اوستا bāzu، سانسکریت bāhu «بارتولمه ۹۵۶»، گیلکی bāzū، برنی و نطنزی bāzu، دزفولی و شوشتری bōly؛ و آن قسمتی است از دست که از دوش تا آرنج را شامل است' — Avestan bāzu, Sanskrit bāhu (with the Bartholomae column number), the dialect forms, and the anatomical definition 'the part of the arm from the shoulder to the elbow', which is exactly Nourai's gloss 'arm'. Wiktionary derives it from Old Persian bāzu < PII *bʰaHȷ́ʰúš < PIE *bʰeh₂ǵʰús. Armenian bazuk is the Iranian loan of the same word.\",\n   \"derivation_fa\":\"«بازو» دنبالهٔ ایرانی باستان *bāzu- است و همخوان‌های آن دست‌نخورده مانده؛ در فارسی میانه bāzā ⟨bʾcʾy⟩ است (مکنزی: «bāzā [bʾcʾy | فارسی نو bāzū] بازو» با ترکیب bāzā-banag «بازوبند») و صورت فارسی نو bāzū همان ستاک u است که دوباره عمومیت یافته. حاشیهٔ ریشه‌شناختی معین بر «برهان قاطع» ص ۲۲۰ زنجیره را روشن می‌آورد: «بازو ـ در اوستا bāzu، سانسکریت bāhu «بارتولمه ۹۵۶»، گیلکی bāzū، برنی و نطنزی bāzu، دزفولی و شوشتری bōly؛ و آن قسمتی است از دست که از دوش تا آرنج را شامل است» — یعنی همان معنایی که نورایی داده است. ویکی‌واژه نیز آن را از پارسی باستان bāzu و در نهایت از *bʰeh₂ǵʰús می‌گیرد. «بازوک» ارمنی وام‌واژهٔ همین کلمه از ایرانی است. ادعای نورایی درست است.\",\n   \"sources\":[W_BAZU],\n   \"ref_check\":[\n    {\"ref\":\"BQT:220\",\"status\":\"supports\",\"note\":\"Borhan-e Qāṭeʿ ed. Mo'in, printed p.220 = BQT_v1_pages.txt \\\\f-leaf 440 (the leaves round it carry the running numerals 217 and 218), the page with بازو دادن / بازو دراز / بازود. The OCR of the footnote band is unreadable, so the archive.org leaf image (borhan-ghate-v1, n440) was read directly; footnote 8 reads: 'بازو ـ در اوستا bāzu، سانسکریت bāhu «بارتولمه ۹۵۶»، گیلکی bāzū، برنی و نطنزی bāzu «ک. ۱ ص ۲۸۸»، دزفولی و شوشتری bōly؛ و آن قسمتی است از دست که از دوش تا آرنج را شامل است.' Saved verbatim to data/verification/sources/refs/ocr/BQT/220.vision.txt. The citation is exact and it carries precisely the Avestan→Persian derivation Nourai draws.\"}\n   ],\n   \"consulted\":[\n    {\"src\":\"PHD\",\"where\":\"MacKenzie, Concise Pahlavi Dictionary s.v. bāzā (PHD.txt line 256)\",\"stance\":\"supports\",\"note\":\"'bāzā [bʾcʾy | (N bāzū)] arm. ~banag [-pʾnk] arm-guard, brassard' — MacKenzie himself gives New Persian bāzū as the descendant, and the Pahlavi link Nourai's chart skips.\"},\n    {\"src\":\"HRN\",\"where\":\"Horn, Grundriss\",\"stance\":\"silent\",\"note\":\"grep 'bāzū|bazu' in HRN.txt gives no numbered entry for the word; Horn's neighbours in Hübschmann's notes (nos. 166-167) discuss Kurdish bahū 'fore- and upper arm' and Afghan bāzū-band, which is the same family.\"},\n    {\"src\":\"HUB\",\"where\":\"Hübschmann, Persische Studien, note to Horn nos. 166-167, p.23 (HUB.txt line 735)\",\"stance\":\"supports\",\"note\":\"'…sanisch-kurd. bahū ‘Unter- und Oberarm’ (ZDMG. 38, 52) gehört. Ob auch afgh. bāzū, bahū (pl. bāzūgān, bahugān) ‘Armband, Schmuck fürs Handgelenk’ und armenisch bazuband ‘ein Frauenschmuck mit Edelsteinen’ (wohl aus *bāzūband)?' — the same etymon in the neighbouring Iranian languages.\"},\n    {\"src\":\"MON\",\"where\":\"Mo'in, Farhang-e Fārsi\",\"stance\":\"silent\",\"note\":\"the digital text of Mo'in available here has no etymological bracket on بازو; his Latin-script forms are in the print edition, and the same author's Borhan footnote (above) gives them.\"}\n   ]},\n  {\"id\":3,\"lang\":\"Germanic\",\"words\":\"boog\",\"verdict\":\"plausible\",\n   \"derivation\":\"The Germanic reflex is Proto-Germanic *bōguz 'shoulder, upper arm' > OE bōg/bōh (> bough), ON bōgr, OHG buog (NHG Bug), MDu. boech, MLG bōch/boog, Du. boeg. The nautical sense 'shoulder of a ship, bow' developed in the Hanseatic/Low German and Scandinavian seafaring vocabulary and is the form English borrowed. Nourai's 'boog' is defensible as the Middle Low German spelling — Etymonline cites 'Middle Low German boog' beside Old Norse bogr and Middle Dutch boech — but it is not the modern Dutch word for a ship's bow (that is boeg; Dutch boog means 'arch, bow-weapon' and belongs to the unrelated *beug- 'bend'), and the label 'Germanic' with the gloss 'bow of a ship' attaches a specifically Low German/Norse nautical sense to a Proto-Germanic body-part noun. Nourai's own reference, AHD, does not support the ship sense: Watkins gives only 'Germanic *bōguz in Old English bōg, boh, bough: BOUGH'. Hence plausible rather than confirmed.\",\n   \"derivation_fa\":\"بازماندهٔ ژرمنی این ریشه *bōguz ژرمنی آغازین «شانه، بازو» است: انگلیسی کهن bōg/bōh (که bough امروزی از آن است)، نروژی کهن bōgr، آلمانی علیای کهن buog (آلمانی امروز Bug)، هلندی میانه boech، آلمانی سفلای میانه bōch/boog و هلندی boeg. معنای دریایی «شانهٔ کشتی، سینهٔ کشتی» در واژگان دریانوردی آلمانی سفلی و اسکاندیناوی پدید آمد و انگلیسی همان را وام گرفت. «boog» که نورایی آورده به‌عنوان املای آلمانی سفلای میانه پذیرفتنی است (اتیمانلاین نیز «Middle Low German boog» را در کنار bogr و boech می‌آورد)، امّا واژهٔ هلندیِ امروزیِ سینهٔ کشتی نیست (آن boeg است؛ hollandsche boog یعنی «کمان، طاق» و از ریشهٔ بی‌ربطِ *beug- «خمیدن» است). افزون بر این، برچسب «ژرمنی» با معنای «سینهٔ کشتی» معنایی به‌کلّی محلی را به اسمی همگانی و اندام‌واژه می‌چسباند، و خودِ مرجعِ نورایی یعنی AHD این معنا را نمی‌دهد و تنها می‌نویسد «Germanic *bōguz in Old English bōg, boh, bough». داوری: با احتیاط پذیرفتنی.\",\n   \"sources\":[E_BOW],\n   \"ref_check\":[\n    {\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. bhaghu- (AHD_watkins1985.txt line 323): 'bhaghu-. Arm. Germanic *bōguz in Old English bōg, boh, bough: BOUGH. [Pok. bhāghū-s 108.]', and the word index (line 1314) has 'BOUGH bhaghu-' but no BOW. So AHD supports a Germanic *bōguz under this root but does not give the form 'boog' nor the sense 'bow of a ship'.\"}\n   ],\n   \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 p.190 s.v. bough and p.192 s.v. bow\",\"stance\":\"supports\",\"note\":\"'bough … OE. bōg, bōh, ‘arm, shoulder, bough’, rel. to ON. bogr, ‘shoulder; bow of a ship’, OHG. buog … fr. I.-E. *bhāghus-, ‘elbow, arm’' and 'bow, n., the fore part of a ship. — Of Scand. origin. Cp. ON. bogr, Dan. bov, Swed. bog, ‘shoulder; bow of a ship’. See bough.' Klein connects the nautical word to this root, but through Scandinavian rather than a form 'boog'.\"},\n    {\"src\":\"WEB\",\"where\":\"Webster (WEB_vol1.txt lines 22476, 22625, 22696)\",\"stance\":\"partial\",\"note\":\"s.v. bough: '…AS. bōg, bōh, the shoulder, arm; Ice. bogr; Sw. bog; O.H.G buog; Gr. pechys; Sans. bahu, the arm.' s.v. bow: '[16th-c., from LG. or Scand.; cf. LG. bug, D. boeg, Sw. bog, shoulder, bows.] the front part of a ship'; and s.v. bowsprit: '[D. boegspriet; boeg, bow of a ship, and spriet, a sprit]'. Webster's Low German/Dutch forms are bug and boeg, not boog.\"},\n    {\"src\":\"POK\",\"where\":\"IEW p.108\",\"stance\":\"partial\",\"note\":\"'aisl. bōgr, Akk. Pl. bōgu ‘Arm, Schulter’, ags. bōg ‘Schulter, Arm; Zweig’, ahd. buog (nhd. Bug) ‘Schulter, Hüfte, Bug des Tieres’' — the Germanic forms are given with body-part meanings; the ship sense is not mentioned.\"}\n   ]},\n  {\"id\":4,\"lang\":\"English\",\"words\":\"bow\",\"verdict\":\"confirmed\",\n   \"derivation\":\"English bow 'front section of a ship' is first recorded in the mid-14th century and is a nautical borrowing, not an inherited word: Etymonline gives 'Old Norse bogr, Middle Low German boog, Middle Dutch boech' as its sources, Klein 'Of Scand. origin. Cp. ON. bogr, Dan. bov, Swed. bog, ‘shoulder; bow of a ship’. See bough', and Webster '[16th-c., from LG. or Scand.]'. The English inherited cognate of the same Germanic etymon is bough (OE bōg 'arm, shoulder, bough'), which is why the two words are doublets: 'shoulder' → (of a ship) 'the shouldering forward part', and 'shoulder/arm' → (of a tree) 'branch'. The chart's Germanic → English arrow is thus correct as a borrowing arrow; the gloss 'front section of a ship' is exact.\",\n   \"derivation_fa\":\"واژهٔ انگلیسی bow «سینه/پیشانی کشتی» نخستین‌بار در میانهٔ سدهٔ چهاردهم میلادی ثبت شده و وام‌واژه‌ای دریایی است نه میراث درون‌زبانی: اتیمانلاین خاستگاه آن را «نروژی کهن bogr، آلمانی سفلای میانه boog، هلندی میانه boech» می‌داند، کلاین «از اسکاندیناوی؛ سنجیدنی با ON bogr، دانمارکی bov، سوئدی bog ‘شانه؛ سینهٔ کشتی’» و وبستر «[سدهٔ شانزدهم، از آلمانی سفلی یا اسکاندیناوی]». هم‌ریشهٔ اصیلِ انگلیسیِ همین ستاک ژرمنی واژهٔ bough «شاخه» است (انگلیسی کهن bōg «بازو، شانه، شاخه»)، و از همین رو این دو واژه دوگانه‌اند: «شانه» ← «بخش پیش‌آمدهٔ کشتی» و «شانه/بازو» ← «شاخهٔ درخت». پس پیکان ژرمنی ← انگلیسی به‌عنوان پیکان وام‌گیری درست است و معنایی که داده شده دقیق است. ادعای نورایی درست است.\",\n   \"sources\":[E_BOW],\n   \"ref_check\":[\n    {\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the node carries no reference in the book (refs=None); the claim was checked against Klein, Webster and Etymonline instead — all three agree.\"}\n   ],\n   \"consulted\":[\n    {\"src\":\"KLN\",\"where\":\"Klein 1966 p.192 s.v. bow (KLN_1966.txt leaf 112, page marker 193)\",\"stance\":\"supports\",\"note\":\"'bow, n., the fore part of a ship. — Of Scand. origin. Cp. ON. bogr, Dan. bov, Swed. bog, ‘shoulder; bow of a ship’. See bough.'\"},\n    {\"src\":\"WEB\",\"where\":\"Webster (WEB_vol1.txt line 22625)\",\"stance\":\"supports\",\"note\":\"'bow, n. [16th-c., from LG. or Scand.; cf. LG. bug, D. boeg, Sw. bog, shoulder, bows.] 1. the front part of a ship, boat, or airship; the prow.'\"},\n    {\"src\":\"SKT\",\"where\":\"Skeat\",\"stance\":\"silent\",\"note\":\"grep 'bough|bow, the fore' in SKT.txt returns no headword (the OCR of Skeat's B section is badly damaged); nothing could be read either way.\"}\n   ]}\n ]\n}\n\nout={\"pdf_page\":82,\"book_page\":52,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-05\",\"entries\":[e0,e1]}\nwith open('/home/sfmqrb/git/rishe/data/verification/page-82.json','w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build82c.py\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-82.json > /dev/null && echo \"valid JSON\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 82",
 "description": "Write page-82.json and run verify_check"
}
```


### [2026-09-05T06:31:54.462Z] TOOL RESULT

```
written
valid JSON
nodes verified: 17/17
node verdicts: {'plausible': 4, 'confirmed': 9, 'disputed': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'not_checked': 4, 'partial': 7, 'contradicts': 2, 'not_found': 2}
books consulted: {'partial': 11, 'supports': 25, 'silent': 17, 'contradicts': 5} | by book: {'KLN': 7, 'POK': 6, 'HUB': 5, 'PHD': 4, 'MON': 4, 'BRT': 3, 'HJB': 3, 'WEB': 3, 'HRN': 3, 'KNT': 2, 'CHEUNG': 2, 'WLD': 2, 'AHD': 2, 'BQT': 2, 'SKT': 2, 'SOD': 1, 'AID': 1, 'ARY': 1, 'LKT': 1, 'TTS': 1, 'NYB': 1, 'FSD': 1, 'IEC': 1}
```


## [2026-09-05T06:32:18.203Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-82.json` written; `verify_check.py 82` reports **17/17 nodes, 0 PROBLEM lines**.

**Page 82 (book p. 52) — verdicts**
- Roots: 2 confirmed (Bhag = POK 107 *bʰeh₂g-; Bhâghu = POK 108 *bʰeh₂ǵʰu-, both page citations exact)
- Nodes: 9 confirmed, 4 plausible, 4 disputed

**Disputed**
- Bhag #3 Sanskrit `bhaga-dhara` — not a real Sanskrit lexeme; Benfey's 1862 guess for *bahādur*, which Hobson-Jobson p.49 (Nourai's own ref) prints only to rebut.
- Bhag #6 Mongolian (empty box) — the Sanskrit→Mongol arrow fails; *baγatur* is an Inner-Asian title attested long before Indian contact (Doerfer; Wiktionary).
- Bhag #8 English `bahadur` — Klein p.140 routes it "Hind. bahādur", i.e. via Urdu ← Persian ← Mongol, not from Sanskrit (*Bhagavad-Gita* alone is fine here).
- Bhag #11 Persian `bazleh` بذله — Arabic root b-dh-l; the ذ rules out Mann's *bhaĝlos. Dehkhoda marks it (ع اِ); the chart's own NOTE is right.

**Plausible (with reasons)**
- #1 Avestan `bâga` — Bartholomae has only 'Anteil, Los'; "garden" is the Persian sense read back.
- #4 IE `Bhag-los, Bhag-mos` — copied verbatim from Mann IEC p.61, in no other handbook (Mann himself marks one "?").
- #9 Pahlavi `bazm` — real (MacKenzie p.19), but Hübschmann PS §215 p.29 says the link to Skt. *bhaj* "bleibt fraglich" and offers Lith. *bazmas* / Arm. *bazum* instead.
- Bhâghu #3 Germanic `boog` — defensible as MLG *boog*, but AHD (the cited ref) gives only *bōguz* → OE *bōg* → bough, no ship sense; Dutch *boog* is a different word.

**Extraction errors: none.** The printed page (pdf 82, image saved to `data/verification/sources/refs/ocr/BOOK/82.png`) matches the JSON exactly, including `bhağavant-gita : sound of sublime` — that is the book's own misprint for Klein's "the song of the Sublime One" (recorded as `error_in: book` on node #3).

**Reference-citation notes for the owner:** `SOD:37` lands on the prefixed ʾnβxš- (p.36) rather than the simplex βxš- (p.102); `SOD:100` is exact. `IEC:62` (node #13) contains nothing about phag-; Mann's material is on p.60. `AID` has no *bahadur* headword. `MON:523`/`MON:489` could not be page-verified (local Mo'in text is unpaginated). `BQT:220` verified by reading the archive.org leaf image — Mo'in's footnote 8 gives "در اوستا bāzu، سانسکریت bāhu «بارتولمه ۹۵۶»", saved to `data/verification/sources/refs/ocr/BQT/220.vision.txt`. Nine web pages archived via `fetch_source.py`.
