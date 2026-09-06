# Verification process log — verify-page-221


## [2026-09-06T15:12:31.754Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 221 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-221.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-221.json. Write /home/sfmqrb/git/rishe/data/verification/page-221.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 221` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:12:33.438Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:12:34.227Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T15:12:34.236Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-221.txt"
}
```


### [2026-09-06T15:12:34.246Z] TOOL RESULT

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


### [2026-09-06T15:12:34.254Z] TOOL RESULT

```
1	=== PDF page 221 (book page 191) ===
2	--- entry 0 ---
3	ROOT [Semitic] H.n.n : to have grace and kindness  (refs KLN:701)
4	#1 (parent #0) [Arabic] refs=KLN:701 | H.n.n : to have grace ; Hannâneh : gracious, kind, also sad and sorry (possibly due to the hard crying of "Hannâneh" after the prophet Mohammad passed away).
5	  #2 (parent #1) [Persian] refs=MON; FVA:115 | hanân «حنان» : kindness ; hannân «حنّان ، حنّانه» : kind, gracious, one who cries ; hanîn «حنین» : sorrow, kindness
6	#3 (parent #0) [Hebrew] refs=KLN:701 | hânan : was gracious ; hannah : kindness, Anna ; Yô-hânan : 'The Lord is gracious', John
7	  #4 (parent #3) [Persian] refs=MON6:2343; AKM:36 | Yŭhannâ «یوحنّا» : Saint John ; Yahyâ «یحیی» : "God is gracious, a male name"
8	  #5 (parent #3) [Old Persian] refs=SOD:443 | yâna : grace
9	    #6 (parent #5) [Sogdian] refs=SOD:443 | y`n : grace
10	  #7 (parent #3) [Greek] refs=KLN | Anna : gracious ; Iwannos : gracious
11	    #8 (parent #7) [Latin] refs=None | 
12	      #9 (parent #8) [English] refs=KLN:78,831 | Anne, Ann, Anna ; John, Jane, Jean, Joanne
13	    #10 (parent #7) [Greek] refs=KLN:813; OEW:xi | Ion 1 : Hellenic people who settled in the Mediterranean islands in 1100 BC. | NOTE: The link between the tribe names "Iwnios, Iwn, Iwnos and Iawn" and "Iwannos: gracious", which is the root of many names, is not quite clear
14	      #11 (parent #10) [Old Persian] refs=KLN:813; KNT:204 | yauna : Greek
15	        #12 (parent #11) [Persian] refs=BQT:2549 | yŭnân «یونان» : Greece
16	    #13 (parent #7) [Latin] refs=KLN:813 | Iônius : Ionian
17	      #14 (parent #13) [English] refs=None | Ionian, Ionic
18	    #15 (parent #7) [Russian] refs=KLN:821 | 
19	      #16 (parent #15) [English] refs=KLN:821 | Ivan
20	
```


## [2026-09-06T15:12:37.544Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-221.json | head -200",
 "description": "Read source JSON for page 221"
}
```


### [2026-09-06T15:12:37.583Z] TOOL RESULT

```
{
  "pdf_page": 221,
  "book_page": 191,
  "entries": [
    {
      "root": {
        "name": "H.n.n",
        "lang": "Semitic",
        "refs": "KLN:701",
        "gloss": "to have grace and kindness"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:701",
          "words": [
            {"translit": "H.n.n", "gloss": "to have grace", "script": null},
            {"translit": "Hannâneh", "gloss": "gracious, kind, also sad and sorry (possibly due to the hard crying of \"Hannâneh\" after the prophet Mohammad passed away).", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON; FVA:115",
          "words": [
            {"translit": "hanân", "gloss": "kindness", "script": "حنان"},
            {"translit": "hannân", "gloss": "kind, gracious, one who cries", "script": "حنّان ، حنّانه"},
            {"translit": "hanîn", "gloss": "sorrow, kindness", "script": "حنین"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "شاها ز خدمت تو هرگه که دور مانم - حنّانه وار ازدل هردم کشم حنین را",
            "poet": "Qâ'ânî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:701",
          "words": [
            {"translit": "hânan", "gloss": "was gracious", "script": null},
            {"translit": "hannah", "gloss": "kindness, Anna", "script": null},
            {"translit": "Yô-hânan", "gloss": "'The Lord is gracious', John", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON6:2343; AKM:36",
          "words": [
            {"translit": "Yŭhannâ", "gloss": "Saint John", "script": "یوحنّا"},
            {"translit": "Yahyâ", "gloss": "\"God is gracious, a male name\"", "script": "یحیی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "ولی خط مرا افزون ، کرم کن تاکنم موزون - کلامی همچو انگلیون، به لحنی همچو یوحنّا",
            "poet": "Sohbat Lârî"
          }
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "SOD:443",
          "words": [
            {"translit": "yâna", "gloss": "grace", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:443",
          "words": [
            {"translit": "y`n", "gloss": "grace", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Greek",
          "refs": "KLN",
          "words": [
            {"translit": "Anna", "gloss": "gracious", "script": null},
            {"translit": "Iwannos", "gloss": "gracious", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:78,831",
          "words": [
            {"translit": "Anne, Ann, Anna", "gloss": null, "script": null},
            {"translit": "John, Jane, Jean, Joanne", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "Greek",
          "refs": "KLN:813; OEW:xi",
          "words": [
            {"translit": "Ion 1", "gloss": "Hellenic people who settled in the Mediterranean islands in 1100 BC.", "script": null}
          ],
          "script_extra": null,
          "note": "The link between the tribe names \"Iwnios, Iwn, Iwnos and Iawn\" and \"Iwannos: gracious\", which is the root of many names, is not quite clear",
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Old Persian",
          "refs": "KLN:813; KNT:204",
          "words": [
            {"translit": "yauna", "gloss": "Greek", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "BQT:2549",
          "words": [
            {"translit": "yŭnân", "gloss": "Greece", "script": "یونان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 7,
          "lang": "Latin",
          "refs": "KLN:813",
          "words": [
            {"translit": "Iônius", "gloss": "Ionian", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Ionian, Ionic", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 7,
          "lang": "Russian",
          "refs": "KLN:821",
          "words": [],
          "script_extra": null,
          "note": null,
```


## [2026-09-06T15:12:38.965Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','FVA','AKM','SOD','KNT','BQT','OEW']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


### [2026-09-06T15:12:40.773Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with N
AKM {"title": "Amir J. A'lam, Farhang-e A'lam-e Ketab-e Moqaddas (Dictionary of Proper Names in the Bible, English–Persian), Iran University Press 1988", "kind": "purchase", "url": "in print (Niloofar 1388); gisoom/iketab", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are
```


## [2026-09-06T15:12:44.084Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 200,260p data/extracted/batch/page-221.json; echo ---; ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-06T15:12:44.136Z] TOOL RESULT

```
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": "KLN:821",
          "words": [
            {"translit": "Ivan", "gloss": null, "script": null}
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
```


## [2026-09-06T15:12:44.139Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-06T15:12:44.184Z] TOOL RESULT

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
```


## [2026-09-06T15:12:58.450Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['KLN','SOD','KNT','MON','BQT','OEW','FVA','AKM']:\n    v=d.get(k) or {}\n    print('==',k, '| local:',v.get('local_file'),'| offset:',v.get('page_offset'),'| hint:',str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-06T15:12:59.215Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kerub\\|ḥanan\\|hanan\\b\" KLN_1966.txt | head -20; echo \"=== grace base\"; grep -n \"grace\" KLN_1966.txt | head -40"
}
```


### [2026-09-06T15:13:00.047Z] TOOL RESULT

```
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SOD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== OEW | local: None | offset: None | hint: Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>
== FVA | local: None | offset: None | hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== AKM | local: None | offset: None | hint: Not found.
```


### [2026-09-06T15:13:00.115Z] TOOL RESULT

```
2837:Ann,  Anna,  Anne,  fern.  PN.  —  L.  Anna,  fr.  Gk. "Awa,  fr.  Heb.  Hann6h,  lit.  ‘grace’,  from  the base  of  hanan,  ‘he  was  gracious,  showed  favor’. See  Hannah.
20240:jerkin,  n.,  a  jacket.  —  Of  uncertain  origin. Jeroboam,  name  of  two  kings  in  Israel  (Bible)  — Heb.  Yarobh'dm,  lit.  meaning  ‘let  the  people  in¬ crease’,  fr.  yarSbh,  3rd  person  sing,  imperf.  of base  r-b-b,  ‘to  become  many,  to  increase’,  and 'am,  ‘people’.  For  the  first  element  see  rabbi, for  the  second  see  Amhaarez.  See  Martin  Noth, Die  israelitischen  Personennamen  im  Rahmen der  gemeinsemitischen  Namengebung,  206,  and G.  Buchanan  Gray,  Studies  in  Hebrew  Proper Names,  59.
21330:Leah,  1)  fem.  PN. ;  2)  in  the  Bible,  the  elder  daugh¬ ter  of  Laban  and  wife  of  Jacob.  —  Lit.  ‘wild- cow’;  cp.  Arab,  laan,  ‘wildcow’.  See  Friedrich Delitzsch,  Prolegomena  einesneuenhebr.-aram. Worterbuchs  zum  Alten  Testament  p.  80,  G. Buchanan,  Studies  in  Hebrew  Proper  Names, p.  96,  and  Martin  Noth,  Die  israelitischen  Per- sonennamen  im  Rahmen  der  gemeinsemitischen Namengebung,  p.  10.
34979:Derivative :  shin,  tr.  and  intr.  v. ,  to  climb  (a  pole or  rope),  prop,  ‘to  use  the  shins  for  climbing’, shin,  n.,  name  of  the  21st  letter  of  the  Heb.  al¬ phabet.  —  Heb.  shin,  for  shen,  ‘tooth’  (which derives  from  the  stem  of  shanan,  ‘sharpened’, and  is  rel.  to  Aram,  shinna,  Syr.  shennd,  Arab. sinn,  Ethiop.  senn,  Akkad,  shitmu,  ‘tooth’);  so called  in  allusion  to  the  ancient  Hebrew  form  of this  letter.  Cp.  san,  ‘name  of  letter’, shine,  intr.  and  tr.  v.  —  ME.  schinen,  shinen,  fr. OE.  scinan,  rel.  to  OS.,  OHG.  skirtan,  ON., OFris.  skina,  Dan.  skinne ,  Swed.  skina,  Du. sehijnen,  MHG.  schinen,  G.  scheinen,  Goth. skeinan,  ‘to  shine,  appear' ;  formed  with  -n-for- mative  element  of  the  present  tense,  from  I.-E. base  *ski-,  *ska{i)-,  *sksi-,  ‘to  shine,  flicker, glimmer’,  whence  also  OSlav.  sinqti,  ’to  flash up,  shine’,  OI.  chaya,  Gk.  oxia,  ‘shade’.  See scene  and  cp.  sheer,  ‘bright’,  shimmer,  Gegen- schein.  Cp.  also  chaya,  Sciaenidae,  sciara,  scin¬ tilla,  scio-,  Scirophorian.  skiagraphy,
=== grace base
1235:Abrus,  n.,  a  genus  of  plants  of  the  pea  family (bot  )  —  ModL.,  for  •Habrus,  fr.  Gk.  dpp<k, ‘graceful,  delicate’.  See  habru-.
2150:Aleochara,  n.,  a  genus  of  rove  beetles  ( entomol .) —  ModL.,  compounded  of  Gk.  aXso;,  a  col¬ lateral  form  of  rjXeiSi;,  ‘wandering  in  mind,  dis¬ traught,  foolish’,  and  yaps.,  ‘joy’.  The  first  ele¬ ment  is  rel.  to  aXaoSai,  ‘to  wander,  roam’;  see hallucinate  and  cp.  Alastor,  aleatory.  The  second element  is  rel.  to  yaipew,  ‘to  rejoice’,  yapiq, ‘grace,  kindness’;  see  Charis. aleph,  n.,  name  of  the  1st  letter  of  the  Heb.  al¬ phabet.  —  Heb.  aleph,  pausal  form  of  eleph,  ‘ox’ ; so  called  in  allusion  to  the  ancient  Hebrew  form of  this  letter,  representing  the  head  of  an  ox.  Cp. alpha.  For  the  form  cp.  daleth,  lamedh,  samekh. alepidote,  adj.,  without  scales  ( zool .)  —  Gk. aXeTuSwxo?,  fr.  a-  (see  priv.  pref.  a-)  and XetuSwtoc,  ‘covered  with  scales’,  fr.  Xerct?,  gen. XetuSo?,  ‘scale’.  See  lepido-,  leper.
2837:Ann,  Anna,  Anne,  fern.  PN.  —  L.  Anna,  fr.  Gk. "Awa,  fr.  Heb.  Hann6h,  lit.  ‘grace’,  from  the base  of  hanan,  ‘he  was  gracious,  showed  favor’. See  Hannah.
3200:Derivatives:  appli-able,  adj.,  appliable-ness,  n., appli-abl-y,  adv.,  appli-ance,  n.,  appli-ant,  adj. appoggiatura,  n.,  a  grace  note  (music).  —  It.,  lit. ‘a  support’,  fr.  appoggiare,  ‘to  lean,  rest,  sup¬ port’,  fr.  VL.  *appodiare,  ‘to  support’,  fr.  ad- and  L.  podium,  ‘elevated  place,  balcony  .  See podium  and  cp.  appui.
4761:bensh,  tr.  and  intr.  v.,  to  bless;  to  say  grace.  — Yiddish  benshen,  fr.  dial.  OF.  *bencheir  (OF. beneir ,  F.  benir),  fr.  L.  henedicere.  See  benediction, bent,  adj.,  curved.  —  Pp.  of  bend, bent,  n.,  inclination.  —  Fr.  prec.  word, bent  grass,  also  bent,  n.  —  OE.  beonot-  (in  place names),  rel.  to  OS.  binut ,  OHG.  binuy,  MHG. hin(e)3,  bin3,  ‘rush’.  G.  Binse  developed  fr.  early MHG.  bintz(e),  pi.  of  MHG.  bin(e)3 . Benthamism,  n.,  utilitarianism,  as  taught  by Bentham  (philos.)  —  Named  after  Jeremy  Bent- ham  (1748-1832),  founder  of  the  English  Util¬ itarian  School  of  Philosophy.  For  the  ending see  suff.  -ism.
6198:tics  tending  to  promote  grace  and  health;  2)  (con¬ strued  as  a  singular)  the  art  of  such  gymnastics. —  Compounded  of  Gk.  xaXXoi;,  ‘beauty’,  and abevo;,  ‘strength’.  Gk.  xa Xkoc,  derives  fr.  xotXoc, ‘beautiful’;  see  calo-.  For  the  second  element see  sthenic  and  cp.  asthenia,  neurasthenia.  For the  ending  of  calisthenics  see  suff.  -ics. calk,  caulk,  tr.  v.,  to  stop  up  the  seams  of  a  ship with  oakum.  —  The  original  meaning  was  ‘to tread’,  fr.  ME.  cauken,  fr.  ONF.  cauquier,  corre¬ sponding  to  OF.  cauchier,  chauchier  (F.  cocher), ‘to  tread’,  fr.  L.  calcare,  ‘to  tread’,  fr.  calx,  gen. calcis,  ‘heel’.  See  Calceolaria  and  cp.  words there  referred  to.
7219:Charis,  n.,  Grace,  one  of  the  three  attendants  of Aphrodite  =  Venus  (Greek  and  Roman  mythol.) —  Gk.  Xdptq,  fr.  yapic.,  ‘grace’,  rel.  to  yptipeiv, (for  *xAp-iew),  ‘to  rejoice’,  fr.  I.-E.  base  *gher-, ‘to  desire’,  whence  also  OE.  georn,  ‘desirous’. See  yearn  and  cp.  charism  and  the  second  ele¬ ment  in  Eleocharis,  Eucharist,  Hydrocharis.  Cp. also  Charon.
7220:charism,  n.,  a  divine  favor  or  gift.  —  Gk.  xapi<t(j.a, ‘grace,  favor,  gift’,  fr.  xap(?ecr^at>  ‘to  show favor’,  fr.  x«PlC-  See  prec.  word  and  -ism. Charissa,  fern.  PN.  —  MGk.,  fr.  Gk.  ydpLp, ‘grace’.  See  Charis.
7349:chervil,  n.,  an  aromatic  plant.  —  OE.  cerfille,  fr. L.  chaerephyllum,  fr.  Gk.  xocipstpuXXov,  which  is compounded  of  xcdpeiv,  ‘to  rejoice’,  and  <puX- Xov,  ‘leaf’.  The  first  element  is  rel.  to  yapu;, ‘grace’;  see  Charis.  For  the  second  element  see phyllo-.
7869:-cle,  dimin.  subst.  suff".  « —  Fr.  L.  -cuius  (masc.), -cula  (fem.),  or  -culum  (neut.),  either  directly or  through  the  medium  of  F.  -de.  See  -cule. clean,  adj.  —  ME.  cleric,  fr.  OE.  cline,  ‘clear, clean,  pure’,  rel.  to  OS.  kleni,  ‘dainty,  graceful’, OHG.  kle  ini,  ‘shining,  neat,  elegant"  (whence MHG.  kleine,  ‘nice,  graceful,  small’,  G.  Mein, ‘small’;  in  G.  Kleinod,  ‘jewel,  gem’,  prop, ‘something  neat  or  fine’,  the  orig.  meaning  of klein  survives),  and  prob.  cogn.  with  Gk.  yXxivov (Hesychius),  ‘star-shaped  ornaments’,  -(zhxv, ‘to  laugh’.  See  geloto-  and  cp.  the  first  clement in  kleeneboc.  Derivatives :  dean,  adv.  (c\.v.), clean¬ er,  n.,  clean-ing,  n.,  clean-ly,  adv. clean,  adv.  —  OE.  dine,  "entirely’,  fr.  dine ‘clear,  clean,  pure’.  See  clean,  adj. cleanly,  adj.  —  ME.  clenly,  fr.  OE.  clinlic,  fr. cline.  See  clean,  adj.,  and  adj.  suff.  -ly. Derivatives:  clean-li-ly,  adv.,  clean-li-ness,  n. cleanness,  n.  —  ME.  clennesse,  fr.  OE.  dinnes, fr.  dine.  See  dean,  adj.,  and  -ness, cleanse,  tr.  v.  —  ME.  clensien,  clensen,  fr.  OE. dinsian,  fr.  dine.  See  dean,  adj.
8726:congratulate,  tr.  v.  —  Fr.  L.  congratulate,  pp.  of congratulari ,  ‘to  wish  joy  warmly,  congratulate’, fr.  con-  and  gratulari,  ‘to  wish  joy’,  fr.  gratus, ‘pleasing’.  See  grace,  n.,  and  cp.  grateful. Derivatives:  congratulation  (q.v.),  congratulat- or,  n.,  congratulat-ory,  adj. congratulation,  n.  —  F.,  fr.  L.  congratulalionem, acc.  of  congratuladd,  fr.  congratulatus,  pp.  of congratulari.  See  prec.  word  and  -ion. congregant,  n.,  a  member  of  a  congregation.  — L.  congregdns,  gen.  -antis,  pres.  part,  of  congre- gdre.  See  next  word  and  -ant. congregate,  adj.,  assembled.  —  L.  congregdtus, ‘flocking  together’,  pp.  of  congregate,  ‘to  flock together’,  fr.  con-  and  gregare,  ‘to  gather  into a  flock’,  from  grex,  gen.  gregis,  ‘flock’.  See  gre¬ garious  and  adj.  suff.  -ate. congregate,  tr.  and  intr.  v.,  to  gather  into  a  crowd ; to  assemble.  —  L.  congregdtus ,  pp,  of  congre- gdre.  See  prec.  word.
8931:contempt,  n.,  1)  scorn;  2)  disgrace;  3)  disrespect of  court.  —  L.  contemptus,  ‘a  despising,  con¬ tempt,  scorn’,  fr.  contemptus,  pp.  of  contemnere. See  contemn.
9024:contumely,  n.,  contemptuous  insolence.  —  OF. contumelie,  fr.  L.  con  umelia,  ‘insult,  affront, disgrace,  ignominy',  from  the  adj.  *contumelis, ‘haughty,  insolent’,  which  is  rel.  to  contumax, ‘haughty,  insolent’.  See  contumacy, contund,  tr.  v.,  to  contuse.  —  L.  contundere,  ‘to beat,  bruise’.  See  next  word, contuse,  tr.  v.,  to  bruise.  —  L.  contusus,  pp.  of contundere,  ‘to  beat,  bruise’,  fr.  con-  and  tundere, ‘to  beat,  strike,  stump’.  See  fund, contusion,  n.,  a  bruise.  —  F.,  fr.  L.  contusidnem, acc.  of  contusio,  'a  crushing,  bruising’,  fr.  con-
10492:decennium,  n.,  a  period  of  ten  years.  —  L.,  ‘a period  of  ten  years’,  fr.  decennis,  ‘of  ten  years’, fr.  decern,  ‘ten’,  and  annus,  ‘year’.  See  decem- and  annual  and  cp.  decennary,  decenniad.  For the  change  of  Latin  a  (in  dnnus)  to  e  (in  dec¬ ennis,  dec-ennium)  see  accent  and  cp.  biennial. decent,  adj.  —  L.  decens,  gen.  -entis,  becoming, seemly,  fitting,  proper,  decent’,  pres.  part,  of decet,  decere,  ‘to  be  seemly  or  fitting’,  rel.  to decus,  gen.  decoris,  ‘ornament,  grace,  splendor, glory,  honor,  dignity’,  dignus  (for  *dec-nos), ‘suitable,  becoming,  proper’  (lit.  ‘decorated, splendid’),  dexter  (for  *dexi-teros),  ‘on  the  right side’  (lit.  ‘on  the  becoming  or  fitting  side’),  do-
10550:decorate,  tr.  v.  —  L.  decordtus,  pp.  of  decorare, ‘to  decorate,  adom,  embellish;  to  honor,  dis¬ tinguish’,  fr.  decus,  gen.  decoris,  ‘ornament, grace,  splendor’.  See  decent  and  verbal  suff. -ate.
10649:deft,  adj.,  dexterous.  —  ME.,  fr.  OE.  (ge)dtefte, ‘mild,  gentle’,  rel.  to  gedafen,  gedefe,  ‘suitable’, Goth,  gadaban,  ‘to  be  fit’,  ON.  dafna,  ‘to  grow strong’,  Du.  deftig,  ‘important,  relevant’,  fr. I.-E.  base  * dhabh -,  ‘to  become,  be  suitable’, whence  also  L.  faber,  ‘forger,  smith’,  OSlav. dobru,  ‘fine,  good’,  doba,  ‘opportunity’,  podoba, ‘ornament’,  Lith.  dabinti,  ‘to  adorn’,  dabnits, ‘graceful’.  Cp.  daft.  Cp.  also  fabric,  forge. Derivatives:  deft-ly,  adv.,  deft-ness,  n. defunct,  adj.,  dead.  —  L.  defunctus,  pp.  of  de- fungor,  defungi,  ‘to  finish,  have  done  with,  per¬ form,  depart,  die’,  fr.  de-  and  fungi  (pp.  functus), ‘to  be  engaged  in,  discharge,  perform,  execute, do’.  See  function.
11687:OF.  desgorger  (F.  degorger),  fr.  des-  (fr.  L.  dis-) and  gorge,  ‘throat’.  See  dis-  and  gorge, disgrace,  n.  —  F.  disgrace,  fr.  It.  disgrazia,  fr. dis-  (fr.  L.  dis-)  and  grazia,  ‘grace’,  fr.  L.  gratia, ‘favor,  kindness,  charm’.  See  dis-  and  grace,  v. Derivatives:  disgrace-ful,  adj.,  disgrace-ful-ly , adv.,  disgrace-fui-ness,  n. disgrace,  tr.  v.  — -  F.  disgracier,  fr.  disgrace.  See disgrace,  n.
12633:Edda,  n„  orig.  name  of  the  book  written  by Snorri  Sturluson  (died  in  1241);  later  used  to  de¬ note  ancient  Icelandic  poems  in  general.  —  ON., fr.  odr,  ‘spirit,  mind;  passion,  song,  poetry’,  rel. to  OE.  wop,  ‘sound,  melody,  song’,  and  cogn. with  OIr.  faith,  ‘poet’,  W.  gwawd,  ‘poem’,  L. vates,  soothsayer,  prophet,  seer’.  See  vates  and cp.  words  there  referred  to. eddy,  n.,  whirlpool;  current  of  air.  —  ME.  ydy, prob.  fr.  ON.  ida,  ‘whirlpool’,  lit.  meaning  ‘that which  rebounds  or  flows  back’,  fr.  ON.  pref. id-,  ‘again’,  which  is  rel.  to  OE.,  OS.  ed-,  OHG. et-,  it-,  Goth,  ip,  ‘and,  but,  however’,  and  cogn. with  L.  et,  ‘and’.  See  et.  Derivative:  eddy,  intr.  v. ede-,  form  of  edea-  before  a  vowel, edea,  n.  pi.,  the  external  genitals.  —  Fr.  Gk. aiSoia,  ‘privy  parts,  pudenda’,  prop.  neut.  pi. of  txlSoiog,  ‘bashful,  shamefaced’,  lit.  ‘having a  claim  to  regard’,  fr.  aiScog,  ‘shame,  bash¬ fulness,  reverence’,  fr.  the  stem  of  atSeaffai, ‘to  be  ashamed,  fear,  show  a  sense  of  regard, respect’,  which  prob.  stands  for  ‘afoSeaffai,  fr. I.-E.  *aiz-d-,  whence  also  OI.  idi  (for  *izdi),  ‘I honor’,  Goth,  aistan,  ‘to  fear’.  I.-E.  *aiz-d-  is a  -d-enlargement  of  base  *ais-,  ‘to  honor,  respect’, whence  OHG.  era ,  MHG.  ere,  G.  Ehre ,  ‘honor  , ON.  eir,  ‘grace’,  OE.  dr,  ‘honor, dignity,  benefice, prosperity,  help,  kindness,  mercy’.  Cp.  the  first element  in  Eric.
12804:elemi,  corresponding  to  Arab,  al-lamt. elenchus,  n.,  a  refutation.  —  L.,  fr.  Gk.  IXsyxoi; (masc.),  ‘disproof,  argument  by  refutation’, which  is  rel.  to  iXzyx°i  (neut.),  ‘blame,  disgrace’, IXly/civ,  ‘to  disprove ;  to  disgrace’,  and  possibly cogn.  with  Lett,  langat,  ‘to  disgrace,  abuse’.  Cp. next  word.
12806:Eleocharis,  n.,  a  genus  of  plants,  the  spike  rush (bot.)  —  ModL.,  lit.  ‘delight  of  the  marsh’, compounded  of  Gk.  eXo?,  ‘marsh’,  and  yapi?, ‘grace,  delight’.  The  first  element  is  cogn.  with OI.  sdras-,  ‘pond’.  For  the  second  element  see Charis.
13766:Eucharis,  n.,  a  genus  of  the  plants  of  the  amar¬ yllis  family  (bot.)  —  ModL.,  fr.  Gk.  e6xaP1?. ‘pleasant,  agreeable’,  fr.  e5,  ‘well’,  and  X“P‘S> ‘favor,  grace’.  See  next  word.
13768:ptoxia,  ‘thankfulness,  gratitude’,  fr.  EuyaptaToc, ‘pleasant,  agreeable’,  fr.  suxapt^siv,  ‘to  render thanks’,  fr.  eu  (see  eu-)  and  ya. pip,  ‘favor,  grace’. See  Charis  and  cp.  words  there  referred  to. Derivatives:  eucharist-ic ,  eucharist-ic-al,  adjs., eucharist-ic-al-ly,  adv.
14154:exprobrate,  tr.  v.,  to  censure.  —  L.  exprobrdtus, pp.  of  exprobrare,  ‘to  make  a  matter  of  reproach, accuse  of  something  disgraceful,  upbraid’,  fr. ist  ex-  and  probrum,  ‘a  shameful  act'.  See  op¬ probrium.
14258:fabric,  n.  —  F.  fabrique,  fr.  L.  fabrica,  ‘workshop of  an  artisan,  building,  fabric’,  fr.  faber,  gen. fabri,  ‘workman,  artisan,  artificer,  forger, smith’,  from  L.  base  *fab-,  corresponding  to I.-E.  base  *dhabh-,  ‘to  become  or  be  suitable', whence  Arm.  darbin,  ‘smith’,  OSlav.  dobrii, ‘fine,  good’,  doba,  ‘opportunity’,  Lith.  dabinti, ‘to  adorn’,  dabnits,  ‘graceful’.  Cp.  daft,  deft, forge.
14836:flaggy,  adj.,  pertaining  to  flagstone.  —  Formed with  adj.  suff.  -y  fr.  flag,  ‘flagstone’, flagitious,  adj.,  extremely  wicked;  scandalous.  — L.  flagitiosus,  ‘shameful,  disgraceful’,  fr.  fldgi- tium,  ‘shameful  deed,  shame’,  fr.  ft agitare,  ‘to whip,  decry;  to  demand  passionately’,  freq.  of *fldgere,  ‘to  whip’  (a  verb  of  which  flagrum, ‘whip’,  is  a  derivative).  The  verb  flagitare  stands to  *fldgere  as  agitare,  ‘to  put  in  constant  mo¬ tion’,  stands  to  agere,  ‘to  move’.  See  flagellum and  -ous.
15666:Derivatives:  gain-ful,  gain-less,  adjs. gainly,  adj.,  shapely;  comely.  —  Formed  with adj.  suff.  -lyfr.  obsol.  E .gain,  ‘graceful,  suitable, kindly’,  fr.  ME.  gayn,  geyn,  ‘direct,  ready,  con¬ venient’,  fr.  ON.  gegn,  of  s.m,  See  again, gainsay,  tr.  v.,  to  contradict.  —  ME.  geinseien, lit.  ‘to  say  against’,  fr.  ON.  gegn,  ‘against’ (which  is  rel.  to  OE.  gegn-,  gean-,  ‘against’),  and ME.  seggen,  seien,  ‘to  say’.  See  again  and  say,  v. gainst,  prep.  —  Aphetic  for  against, gait,  n.,  manner  of  walking.  —  ME.  gate,  ‘a  way’. See  gate,  ‘passage’.
15789:garage,  n.  — F„  orig.  meaning  ‘a  place  for  storing something’,  fr.  garer ,  ‘to  make  safe,  protect , fr.  Frankish  *wardn,  ‘to  guard’,  which  is  rel.  to OHG.  biwaron,  of  s.m.  See  ware,  ‘alert’,  and  -age. Derivative:  garage ,  tr.  v. garb,  n.,  costume,  style.  —  MF.  garbe  (F.  galbe), 'graceful  curb;  graceful  outline’,  fr.  It.  garbo, ‘grace’,  which  is  of  Teut.  origin.  Cp.  OHG. gar(a)wi,  ‘dress,  equipment,  preparation’,  and see  gear.
15988:gentility, n„  1)  gentle  birth;  2)  politeness.  —  OF. gentilite  (F.  gentilite),  fr.  L.  gentilitatem,  acc.  of gentilitas,  ‘relationship  of  those  who  belong  to a  gens’,  fr.  gentilis.  See  gentile  and  -ity. gentle,  adj.,  1)  well-born;  2)  honorable;  3)  res¬ pectable.  —  OF.  gentil,  ‘of  good  family,  noble’ (whence  F.  gentil,  ‘nice,  graceful,  pleasing,  fine, pretty’),  fr.  L.  gentilis,  ‘belonging  to  the  same gens’.  See  gentile  and  cp.  genteel.
16503:Derivatives:  grabbl-er,  n.,  grabbl-ing,  n. grace,  n.  —  ME.,  fr.  MF.  (=  F.)  grace,  fr.  OF. grace,  fr.  L.  gratia,  ‘favor  shown  to  another, kindness,  loveliness,  charm;  thanks,  thankful¬ ness,  gratitude’,  fr.  grants,  ‘beloved,  pleasing, dear,  agreeable;  grateful’,  fr.  I.-E.  base  *gwer-, ‘to  praise,  welcome’,  whence  also  OI.  gfndli, gfniti,  ‘sings,  praises,  announces’,  gtr,  girdh, ‘praise,  song’,  gurtifr,  of  s.m.,  gurtah,  ‘welcome’, Avestiv  gar-,  ‘to  praise’,  Lith.  giriit,  girti,  ‘to praise,  celebrate’,  Lett,  dzifties,  ‘to  boast’, OPruss.  girtwei,  ‘to  praise’,  girsnan,  ‘praise, reputation’.  Cp.  gracious,  grateful,  gratify, gratis,  gratuitous,  gratulate,  agree,  congratu¬ late,  disgrace,  ingrate,  ingratiate,  mauger. Derivatives:  grace,  v.  (q.v.),  grace-ful,  adj., grace-ful-ly ,  adv.,  grace-ful-ness,  n.,  grace-less, adj.,  grace-less-ly,  adv.,  grace-Iess-ness,  n. grace,  tr.  v.  —  OF.  grader,  fr.  grace.  See  grace,n. Grace,  fern.  PN.  —  Lit.  ‘favor,  grace’,  fr.  L. gratia.  See  grace,  n.
16504:Gracilaria,  n„  a  genus  of  algae  (hot.)  —  ModL., fr.  L.  gracilis,  ‘slender’.  See  gracile. gracile,  adj.,  i)  slender;  2)  gracefully  slender.  — L.  gracilis,  ‘slender,  thin,  slight,  meager’,  dis¬ simulated  fr.  *cracitis,  rel.  to  cracens,  ‘slender’, and  prob.  cogn.  with  OI.  kfsdh,  ‘thin,  weak’, Avestic  klr*sa-,  ‘lean,  meager’,  Lith.  karitu, karSti,  ‘to  be  very  old,  to  age’,  Lett,  karst,  karst, ‘to  grow  old,  ripen’.  Cp.  Gracilaria.  For  the  end¬ ing  of  grac-ilis  cp.  habilis ,  ‘handy,  supple,  suit¬ able’,  fr.  habere,  ‘to  have,  hold’  (see  able).
16507:L.  gratiosus,  ‘enjoying  favor,  agreable,  obliging’, fr.  gratia.  See  grace,  n.,  and  suff.  -ous. Derivatives:  gracious-ly,  adv.,  gracious-ness,  n. grackle,  n.,  any  of  various  birds  of  the  starling family.  —  L.  graculus,  ‘the  jackdaw’,  of  imi¬ tative  origin;  cp.  croak,  v.,  and  words  there referred  to.
16601:Derivative:  grate,  tr.  v.,  to  furnish  with  a  grate, grateful,  adj.  —  Formed  with  suff.  -ful  from  ob- sol.  grate,  ‘agreable,  thankful’,  fr.  L.  grdtus, ‘agreable,  grateful’,  whence  gratia,  ‘kindness, loveliness’.  See  grace,  n.,  and  cp.  words  there referred  to.
16602:Derivatives:  grateful-ly,  adv. graticule,  n.,  a  design  divided  into  squares.  —  F., fr.  ML.  graticula,  ‘gridiron’,  dimin.  of  grata. See  grate,  ‘frame  of  metal  bars’,  and  -cule. gratification,  n.  —  L.  gratificdtio,  gen.  -onis, ‘obligingness,  complaisance’,  fr.  gratificatus, pp.  of  gratificari.  See  next  word  and  -ation. gratify,  tr,  v.,  to  please.  —  F.  gratifier,  fr.  L.  gra- tificdre,  a  collateral  form  of  gratificari,  ‘to  do favor  to,  to  oblige,  gratify’,  formed  fr.  grdtus, ‘agreeable,  grateful’,  and  -ficare,  fr.  facere,  ‘to make,  do’.  See  grace,  n.,  and  -fy.
16605:Gratiola,  n.,  a  genus  of  plants,  the  hedge  hyssop (bot.)  —  ML.,  dimin.  formed  fr.  L.  gratia, ‘kindness,  loveliness’  (see  grace,  n.,  and  -ole); so  called  in  allusion  to  its  supposed  medicinal properties.
16606:gratis,  adv.,  for  nothing;  freely.  —  L.  gratis,  con¬ traction  of  gratiis,  ‘out  of  favor;  without  re¬ ward,  for  nothing,  gratuitously’,  abl.  pi.  of gratia,  ‘favor,  kindness’.  See  grace,  n. Derivative:  gratis,  adj.
16607:gratitude,  n.  —  F.,  fr.  Late  L.  gratitudo,  ‘thank¬ fulness,  gratitude’,  fr.  grdtus,  ‘beloved,  pleasing, dear,  thankful’.  See  grace,  n.,  and  -tude. gratuitous,  adj.,  given  for  nothing;  free.  —  L. grdtuitus,  ‘that  which  is  done  without  pay,  spon¬ taneous,  gratuitous’,  formed  —  on  analogy  of fortuitus,  ‘casual’  —  fr.  grdtus,  ‘pleasing,  agree¬ able’.  See  grace,  n.  For  the  ending  see  fortu¬ itous.
16612:tuitatem,  acc.  of  gratuitas,  ‘free  gift’,  fr.  L. grdtuitus.  See  prec.  word  and  -ity. gratulate,  tr.  v.,  to  congratulate.  —  L.  gratulatus, pp.  of  gratuldri,'  to  manifest  joy,  congratulate’, contracted  fr.  *grati-tulari,  ‘to  bring  something agreeable’,  compounded  of  grdtus,  ‘pleasing, agreeable’,  and  tulo  =  fero,  ‘I  bring’.  See  grace, n.,  and  tolerate  and  cp.  congratulate.  Cp.  also L.  opitulor,  ‘I  help,  aid,  assist’,  lit.  ‘I  bring  help’, fr.  ops,  gen.  opis,  ‘help,  assistance’,  and  tulo  — fero,  ‘I  bring’.  —  For  the  contraction  of  *grati- tulor  into  grdtulor  see  haplology. gratulation,  n.,  congratulation.  —  L.  gratulatio, gen.  -onis,  ‘manifestation  of  joy,  congratula¬ tion’.  fr.  gratulatus,  pp.  of  grdtulari.  See  prec. word  and  -ion.
16636:Derivative:  graze,  n.,  pasturage, graze,  tr.  v.,  to  touch  slightly.  —  Formed  from prec.  word  and  orig.  used  in  the  sense  ‘to  touch the  (grassy)  ground’  (said  of  bullets  that  touched the  ground  and  rebounded).  Cp.  G.  grasen,  ‘to feed  on  grass’  (fr.  Gras,  ‘grass’),  which  is  used also  in  the  above  mentioned  military  sense. Derivative:  graze,  n.,  a  slight  contact, grazier,  n.,  one  who  grazes  cattle.  —  Formed  fr, graze,  ‘to  feed’,  with  agential  suff.  -ier. grazioso,  adj.,  graceful  (musical  direction).  —  It., fr.  L.  grdtidsus.  See  gracious, grease,  n.  —  ME.  gresse,  grese,  fr.  OF.  gresse, graisse  (F.  graisse),  fr.  VL.  *  crass  ia,  ‘thickness, fatness',  fr.  L.  crasstts,  ‘thick,  fat’,  Cp.  Olt. grascia,  OProveny.  graissa,  Catal.  graxa.  Port, grai.xa ,  ‘fat’.  It.  grasce  (pi.),  ‘victuals’  [Sp.^raso, ‘fat’,  n.,  is  formed  fr.  graso,  ‘fat’,  adj.,  a  col¬ lateral  form  of  craso,  fr.  L.  crassus],  and  see crass.  Cp.  also  degras.
16983:Derivative:  habituat-ion,  n. habitude,  n.,  custom,  habit.  —  F.,  fr.  L.  habi- tudinem,  acc.  of  habitudd,  ‘condition,  habit’,  fr. habitus.  See  habit,  n.,  and  -ude. habitue,  n.,  one  who  habitually  visits  a  place.  — F.,  pp.  of  habituer,  ‘to  habituate’.  See  habituate, habro-,  combining  form  meaning  ‘graceful’.  — Gk.  a(3po-,  fr.  a|3p6<;,  ‘graceful,  delicate,  pretty’; rel.  to  i£(3pa,  ‘a  favorite  slave’,  which  is  bor¬ rowed  fr.  Aram,  habhrd,  ‘companion;  female companion’,  from  the  stem  of  ftabber,  ‘he  joined’, which  is  rel.  to  Heb.  hahhar,  ‘he  joined,  was joined;  he  charmed’,  habher,  ‘companion’, hebher,  hebhrd,  ‘company’,  Ethiop.  habara,  ‘he bound’,  Akkad,  ebru,  ‘companion’,  ubburu.  To bind,  ban’.  See  H.  Lewy,  Die  semitischen  Fremd- worter  im  Griechischen,  p.68,  and  Muss  Ar- nolt,  Semitic  Words  in  Greek  and  Latin,  in Transactions  of  the  American  Philological  As¬ sociation,  Vol.  XXIII,  p. 65. hachure,  n.,  a  short  line  used  in  shading.  —  F.,  fr. hacher.  To  cut’.  See  hatch,  To  engrave’,  and  -ure. Derivative:  hachure,  tr.  v. hacienda,  n.,  a  large  estate,  ranch.  —  Sp.,  ‘landed estate’,  fr.  earlier  facienda,  fr.  L.  faeienda. Things  to  be  done’,  neut.  pi.  gerundive  of facere. To  do’.  See  fact.  For  other  words  traceable  to Latin  gerundives  cp.  agenda  and  words  there referred  to.
17169:Derivatives:  hanker,  n.,  hanker-er,  n.,  hanker¬ ing,  verbal  n.,  hanker-ing-ly,  adv. hanky-panky,  n.,  jugglery,  hocus-pocus.  — Coined  on  analogy  of  hokey-pokey  (q.v.) Hannah,  1)  fern.  PN. ;  2)  in  the  Bible,  the  mother of  the  prophet  Samuel.  —  Heb.  ffanndh,  lit. ‘graciousness’,  from  the  stem  of  hdnan,  ‘he  was gracious,  showed  favor’,  whence  also  (ten, ‘favor,  grace’,  hinndm,  ‘for  nothing,  gratuitous¬ ly’,  hanndn,  ‘gracious’,  tehinndh,  tahandn,  ‘sup¬ plication  for  favor’;  rel.  to  Aram.  1. idndn ,  Syr. han,  Arab,  hanna,  ‘was  favorable,  merciful’, Akkad,  jihnanuni,  ‘he  has  mercy  on  me’,  jenni- nunu,  ‘he  has  mercy  on  us’.  Cp.  the  first  ele¬ ment  in  the  Punic  PN.  Hannibha'al,  ‘Hannibal’, lit.  ‘my  favor  is  with  Baal’.  Cp.  also  Ann,  Jane, Jenny,  Joanna,  John.
```


## [2026-09-06T15:13:07.173Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\ndef find(pat, maxn=6):\n    out=[]\n    for i,l in enumerate(leaves):\n        for m in re.finditer(pat,l):\n            out.append((i, l[max(0,m.start()-100):m.start()+800].replace('\\n',' ')))\n            if len(out)>=maxn: return out\n    return out\nfor pat in [r'Hannah,\\s+1\\)', r'^John,', r'Ionia', r'Ivan', r'Joanna', r'Jane,']:\n    print('======',pat)\n    for i,s in find(pat,3):\n        print('LEAF',i,'~printed p.',(i-12)*2,'-',(i-12)*2+1)\n        print(s[:900])\n        print('---')\nEOF"
}
```


### [2026-09-06T15:13:08.935Z] TOOL RESULT

```
====== Hannah,\s+1\)
LEAF 378 ~printed p. 732 - 733
y,  adv. hanky-panky,  n.,  jugglery,  hocus-pocus.  — Coined  on  analogy  of  hokey-pokey  (q.v.) Hannah,  1)  fern.  PN. ;  2)  in  the  Bible,  the  mother of  the  prophet  Samuel.  —  Heb.  ffanndh,  lit. ‘graciousness’,  from  the  stem  of  hdnan,  ‘he  was gracious,  showed  favor’,  whence  also  (ten, ‘favor,  grace’,  hinndm,  ‘for  nothing,  gratuitous¬ ly’,  hanndn,  ‘gracious’,  tehinndh,  tahandn,  ‘sup¬ plication  for  favor’;  rel.  to  Aram.  1. idndn ,  Syr. han,  Arab,  hanna,  ‘was  favorable,  merciful’, Akkad,  jihnanuni,  ‘he  has  mercy  on  me’,  jenni- nunu,  ‘he  has  mercy  on  us’.  Cp.  the  first  ele¬ ment  in  the  Punic  PN.  Hannibha'al,  ‘Hannibal’, lit.  ‘my  favor  is  with  Baal’.  Cp.  also  Ann,  Jane, Jenny,  Joanna,  John. Hansard,  n.,  official  reports  of  the  Parliament  at Westminster.  —  So  called  fr.  Luke  Hansard (1752-1828)  and
---
====== ^John,
====== Ionia
LEAF 47 ~printed p. 70 - 71
us,  fr.  Anacreon,  fr.  Gk. ’  Avaxpecov,  a  celebrated  Greek  lyrical  poet  bom at  Teos  in  Ionia  (560-478  B.C.E.). anacrusis,  n.,  unstressed  syllable  before  a  stressed syllable  at  the  beginning  of  a  verse.  —  Gk. dvdxpoump,  ‘a  pushing  back’,  fr.  dvaxpoueiv, ‘to  push  back’,  fr.  dvd,  ‘back’  (see  ana-),  and xpouciv  (for  *xpouast.v),  ‘to  knock,  strike, push’,  which  is  rel.  to  Homeric  xpoalvstv  (prob. for  *xpouadv-teiv),  ‘to  stamp,  strike  with  the hoof’,  and  cogn.  with  OSlav.  su-krusg,  su-kru - Siti,  Russ.  krusit\  Lith.  krusu,  kruSti,  ‘to  smash, shatter’,  OSlav.  kruchu,  ‘piece,  bit  of  food’, anadem,  n.,  a  wreath,  garland.  —  L.  anadema,  fr. Gk.  dvd8/)pa,  ‘band,  headband’,  fr.  dvaSetv, ‘to  bind  up’,  fr.  dvd  (see  ana-)  and  8eTv,  ‘to bind’.  See  diadem. anadiplosis,  n.,  repetition  of  an  initial  
---
LEAF 437 ~printed p. 850 - 851
 -ionis  (either directly  or  through  the  medium  of  OF.  and  F. -ion).  Cp.  -ation,  -ition. Ionian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Ionius,  fr.  Gk.’Idmoi;,  ‘Ionian’,  fr.’Tcav  (gen. Tcovoe),  contraction  of  Titov  (gen.  Taovo^), ‘Ionian’,  fr.  orig.  *TiFtov,  whence  Heb.  Yawdn, Akkad.  Iamanu,  Idvanu,  Egypt.  Yfvana,  Y*- vanna,  ‘Greek’.  Cp.  also  OI.  Yavanah,  OPers. Yauna,  ‘Greek’,  OI.  yavanika,  ‘Greek  woman’; ‘curtain  (in  the  theater)’,  lit.  ‘Greek  (partition)’. Ionic,  adj.  —  L.  lonicus,  fr.  Gk.  Ttov.xic,  ‘Ionic’, fr.  Tov.  See  prec.  word  and  -ic. ionium,  n.,  a  radioactive  element  pertaining  to the  uranium  group  (chem)  —  ModL.,  formed fr.  ion  with  suff.  -ium;  so  called  in  allusion  to its  ionizing  power. ionize,  tr.  v.,  to  separate  into  ions.  —  Formed  fr. ion  with  suff.  -ize. ionosp
---
LEAF 437 ~printed p. 850 - 851
,  -ition. Ionian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Ionius,  fr.  Gk.’Idmoi;,  ‘Ionian’,  fr.’Tcav  (gen. Tcovoe),  contraction  of  Titov  (gen.  Taovo^), ‘Ionian’,  fr.  orig.  *TiFtov,  whence  Heb.  Yawdn, Akkad.  Iamanu,  Idvanu,  Egypt.  Yfvana,  Y*- vanna,  ‘Greek’.  Cp.  also  OI.  Yavanah,  OPers. Yauna,  ‘Greek’,  OI.  yavanika,  ‘Greek  woman’; ‘curtain  (in  the  theater)’,  lit.  ‘Greek  (partition)’. Ionic,  adj.  —  L.  lonicus,  fr.  Gk.  Ttov.xic,  ‘Ionic’, fr.  Tov.  See  prec.  word  and  -ic. ionium,  n.,  a  radioactive  element  pertaining  to the  uranium  group  (chem)  —  ModL.,  formed fr.  ion  with  suff.  -ium;  so  called  in  allusion  to its  ionizing  power. ionize,  tr.  v.,  to  separate  into  ions.  —  Formed  fr. ion  with  suff.  -ize. ionosphere,  n.,  that  part  of  the  earth’s  atmosphere which  extends  from  the  stratosph
---
====== Ivan
LEAF 145 ~printed p. 266 - 267
 which  was  first used  by  Walter  Scott  (‘Cedric  the  Saxon’  is  one of  the  characters  in  Ivanhoe)  prob.  stands  for OE.  Cerdic  and  owes  its  form  to  a  mistake  of Scott's. Cedrus,  n.,  a  genus  of  trees  of  the  pine  family (bot.)  —  L.,  ‘cedar’.  See  cedar, cedula,  n.,  in  Spanish  countries;  order,  certi¬ ficate,  security.  —  Sp.  cedula,  fr.  L.  schedula. See  schedule. ceil,  tr.  v.,  to  overlay,  cover.  —  F.  del,  ‘sky, canopy’,  fr.  L.  caelum,  ‘sky’.  See  celestial. Derivatives:  ceil-er,  n.,  ceil-ing,  n. celadon,  n.,  pale  green  color.  —  F.  celadon,  fr. Celadon,  Astrce’s  lover  in  Honore  d’Urfe’s novel  Astree.  Honore  d’Urfe  formed  this  name from  the  Latin  PN.  Celadon  occurring  in  Ovid’s Metamorphoses. celadonite,  n.,  a  green  silicate  of  iron,  magnesium and  potassium  (mineral.)  —  Formed  with  subst.
---
LEAF 444 ~printed p. 864 - 865
elder  (bot) —  ModL.,  fr.  Gaulish  ivos,  whence  also  F.  if, ‘yew’.  See  yew  and  cp.  uva. Ivan,  masc.  PN.  —  Russ.,  fr.  Gk  'Itna.wrfi.  See John. -ive,  suff.  meaning  ‘tending  to;  of  the  quality  of’. —  L.  -ivus  (mostly  through  the  medium  of  F. -if,  fern.  -ive). ivory,  n.  —  ME.  ivorie,  fr.  OF.  ivurie  (F.  ivoire), fr.  L.  eboreus,  ‘of  ivory’,  fr.  ebur,  ‘ivory’,  bor¬ rowed  fr.  Egyptian  ab,  abu,  ‘elephant,  ivory’, prob.  through  the  medium  of  the  Phoenicians. The  same  word  appears  in  the  second  element of  Heb.  shen-habbtm,  ‘ivory’  (lit.  ‘tooth  of  the elephant’),  whence  Yebu  (=  Heb.  Yebh),  ori¬ ginal  name  of  the  island  Elephantine;  cp.  also OI.  ibhah,  ‘elephant’,  and  the  second  element in  Gk.  £X-s<pa<;,  ‘elephant’.  Cp.  ebumine, elephant ivy,  n.  —  ME.  ivi,  fr.  OE.  ifig,  rel.  to  MLG.  if-
---
LEAF 448 ~printed p. 872 - 873
ferred  to.  The  second element  derives  fr.  handn,  ‘he  was  gracious’.  See Hannah  and  cp.  Ivan,  Jane,  Jean,  masc.  and fem.  PN.,  jenneting,  Jenny,  Joan,  Joanna, Johnny. John  Bull,  the  English  nation  personified.  —  Fr. John  Bull,  a  character  representing  the  English nation  in  Arbuthnot’s  satire  The  History  of John  Bull  (1712). Johnny,  masc.  PN.  —  Formed  fr.  John  with dimin,  suff.  -y. Johnsonese,  n.,  a  pompous,  inflated  style.  • — Prop,  the  style  of  Dr.  Samuel  Johnson  ( 1 709-84). For  the  ending  see  suff.  -ese. Johnsonian,  adj.,  pertaining  to,  or  resembling. Dr.  Samuel  Johnson  or  his  style.  —  See  prec. word  and  -ian. Derivative :  Johnsonian-ism,  n. johnstrupite,  n.,  a  complex  silicate  of  cerium and  other  metals  (mineral.)  —  G.  Johnstrupit, named  after  Professor  Frederik  Johnstrup  of Copenhag
---
====== Joanna
LEAF 378 ~printed p. 732 - 733
  PN.  Hannibha'al,  ‘Hannibal’, lit.  ‘my  favor  is  with  Baal’.  Cp.  also  Ann,  Jane, Jenny,  Joanna,  John. Hansard,  n.,  official  reports  of  the  Parliament  at Westminster.  —  So  called  fr.  Luke  Hansard (1752-1828)  and  his  descendants,  printers  of these  reports. Derivative:  Hansard-ize,  tr.  v.,  to  confront  (a member  of  Parliament)  with  his  former  state¬ ments  as  recorded  in  Hansard. Hansa,  n.,  medieval  guild  of  merchants.  —  MF. hanse,  fr.  MLG.  hanse,  ‘merchants’  guild’,  fr. OHG.  hansa,  ‘troop  of  warriors’,  which  is  rel. to  Goth,  hansa,  ‘troop,  company,  multitude’, OE.  hos,  ‘attendants,  retinue’.  Finn,  kansa, ‘people,  society’,  Russ.-Karelian  kanza,  ‘syna¬ gogue’  are  Teut.  loan  words. Hanseatic,  adj.,  pertaining  to  the  Hansa.  —  ML. Hanseaticus.  See  prec.  word  and  -atic. hansom,  n.,  also  hansom  ca
---
LEAF 445 ~printed p. 866 - 867
an,  fr. jSp,  ‘a  cover’. Jane,  fern.  PN.  —  F.  Jeanne,  fr.  OF.  Jehane,  fr. ML.  Johanna,  Joanna.  See  Joan  and  cp.  Jean, fern.  PN.  Cp.  also  demijohn,  jenny. Jane,  n.,  a  small  Genoese  coin.  —  OF.  Jane,  fr. ML.  Janua,  ‘Genoa’.  Cp.  L.  Genua,  whence  It. Genova,  F.  Genes. Janet,  fem.  PN.  —  A  dimin.  of  Jane  (q.v.) jangada,  n.,  a  kind  of  catamaran.  —  Port.,  fr. Malayalam  cahhdtam,  fr.  OI.  sarpghatah,  a joining  together  of  timber,  union’, jangar,  n.,  a  raft.  —  Port,  jangada.  See  prec.  word, jangle,  intr.  and  tr.  v.  —  ME .janglen,  ‘to  chatter, quarrel’,  fr.  OF.  jangler,  ‘to  chatter’,  which  is of  Teut.  origin.  Cp.  MDu.  jangelen,  Du.  jen- gelen,  ‘to  whine’,  dial.  G.  jangeln,  ‘to  speak  in a  whining  manner', 'which  are  prob.  imitative. Cp.  jingle. Derivatives:  jangl-er,  n.,  jangl-ing,  n. ja
---
LEAF 448 ~printed p. 872 - 873
Joel, John,  Jonathan,  Joshua,  for  the  second  see Aboth  and  cp.  words  there  referred  to. Joanna,  fem.  PN.  —  ML.  Johanna,  Joanna,  fem. form  of  ML.  Johannes,  Joannes.  See  John  and cp.  Jean,  fem.  PN.,  Johanna, job,  n.,  piece  of  work.  —  Of  uncertain  origin. Derivatives:  job,  intr.  v.,  to  do  odd  jobs, etc; tr.  v.,  to  hire  or  to  let  out  for  hire  (a  horse  or carriage),  jobb-er,  n.,  jobb-ery,  n.,  jobb-ing,  adj. job,  tr.  v.,  to  stab,  to  prod.  —  ME.  jobben,  ap¬ parently  of  imitative  origin.  Cp.  jab. Job,  1)  masc.  PN. ;  2)  in  the  Bible:  a)  a  man  who endured  much  suffering  with  faith  and  patience; b)  the  Book  of  Job.  —  Late  L.  Job,  Jobus,  fr.  Gk. ’Icifl,  fr.  Heb.  lyydbh,  which — according  to several  scholars — lit.  means  ‘treated  as  an enemy,  hated,  persecuted’,  fr.  ayyabh,  ‘he  wa
---
====== Jane,
LEAF 378 ~printed p. 732 - 733
in  the  Punic  PN.  Hannibha'al,  ‘Hannibal’, lit.  ‘my  favor  is  with  Baal’.  Cp.  also  Ann,  Jane, Jenny,  Joanna,  John. Hansard,  n.,  official  reports  of  the  Parliament  at Westminster.  —  So  called  fr.  Luke  Hansard (1752-1828)  and  his  descendants,  printers  of these  reports. Derivative:  Hansard-ize,  tr.  v.,  to  confront  (a member  of  Parliament)  with  his  former  state¬ ments  as  recorded  in  Hansard. Hansa,  n.,  medieval  guild  of  merchants.  —  MF. hanse,  fr.  MLG.  hanse,  ‘merchants’  guild’,  fr. OHG.  hansa,  ‘troop  of  warriors’,  which  is  rel. to  Goth,  hansa,  ‘troop,  company,  multitude’, OE.  hos,  ‘attendants,  retinue’.  Finn,  kansa, ‘people,  society’,  Russ.-Karelian  kanza,  ‘syna¬ gogue’  are  Teut.  loan  words. Hanseatic,  adj.,  pertaining  to  the  Hansa.  —  ML. Hanseaticus.  See  prec.  word  and  -atic. hansom,  n.,  al
---
LEAF 445 ~printed p. 866 - 867
 kind  of  sedan  (India). —  Bengali  jhapdn,  fr.  Hind,  japan,  jhappan,  fr. jSp,  ‘a  cover’. Jane,  fern.  PN.  —  F.  Jeanne,  fr.  OF.  Jehane,  fr. ML.  Johanna,  Joanna.  See  Joan  and  cp.  Jean, fern.  PN.  Cp.  also  demijohn,  jenny. Jane,  n.,  a  small  Genoese  coin.  —  OF.  Jane,  fr. ML.  Janua,  ‘Genoa’.  Cp.  L.  Genua,  whence  It. Genova,  F.  Genes. Janet,  fem.  PN.  —  A  dimin.  of  Jane  (q.v.) jangada,  n.,  a  kind  of  catamaran.  —  Port.,  fr. Malayalam  cahhdtam,  fr.  OI.  sarpghatah,  a joining  together  of  timber,  union’, jangar,  n.,  a  raft.  —  Port,  jangada.  See  prec.  word, jangle,  intr.  and  tr.  v.  —  ME .janglen,  ‘to  chatter, quarrel’,  fr.  OF.  jangler,  ‘to  chatter’,  which  is of  Teut.  origin.  Cp.  MDu.  jangelen,  Du.  jen- gelen,  ‘to  whine’,  dial.  G.  jangeln,  ‘to  speak  in a  whining  manner', 'which  are  prob.
---
LEAF 445 ~printed p. 866 - 867
e,  fr. ML.  Johanna,  Joanna.  See  Joan  and  cp.  Jean, fern.  PN.  Cp.  also  demijohn,  jenny. Jane,  n.,  a  small  Genoese  coin.  —  OF.  Jane,  fr. ML.  Janua,  ‘Genoa’.  Cp.  L.  Genua,  whence  It. Genova,  F.  Genes. Janet,  fem.  PN.  —  A  dimin.  of  Jane  (q.v.) jangada,  n.,  a  kind  of  catamaran.  —  Port.,  fr. Malayalam  cahhdtam,  fr.  OI.  sarpghatah,  a joining  together  of  timber,  union’, jangar,  n.,  a  raft.  —  Port,  jangada.  See  prec.  word, jangle,  intr.  and  tr.  v.  —  ME .janglen,  ‘to  chatter, quarrel’,  fr.  OF.  jangler,  ‘to  chatter’,  which  is of  Teut.  origin.  Cp.  MDu.  jangelen,  Du.  jen- gelen,  ‘to  whine’,  dial.  G.  jangeln,  ‘to  speak  in a  whining  manner', 'which  are  prob.  imitative. Cp.  jingle. Derivatives:  jangl-er,  n.,  jangl-ing,  n. jangle,  n.  —  ME.,  fr.  OF.  jangle,  fr.  jangler.  See jangle,  v. Janissa
---
```


## [2026-09-06T15:13:20.320Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nfor pat in [r'Hannah,', r'Ionian,', r'Ivan,', r'Ann,\\s+Anna', r'John,\\s+masc']:\n    for i,l in enumerate(leaves):\n        m=re.search(pat,l)\n        if m:\n            print('===',pat,'LEAF',i)\n            print(l[max(0,m.start()-200):m.start()+700].replace('\\n',' ')[:900])\n            break\nEOF"
}
```


### [2026-09-06T15:13:22.001Z] TOOL RESULT

```
leaves 1
=== Hannah, LEAF 0
n, ‘to  hang*. See hang.   Derivatives: hanker, n., hanker-er, n., hanker-  ing, verbal n., hanker-ing-ly , adv.   hanky-panky, n., jugglery, hocus-pocus. —  Coined on analogy of hokey-pokey (q.v.)   Hannah, 1) fem. PN.; 2) in the Bible, the mother  of the prophet Samuel. — Heb. Hannd h , lit.  ‘graciousness’, from the stem of hdnan , ‘he was  gracious, showed favor’, whence also ben,  ‘favor, grace’, hinndm, ‘for nothing, gratuitous-  ly’, hannQn, ‘gracious’, t i binnd h , tahdnhn , ‘sup-  plication for favor’; rel. to Aram, bdnan, Syr.  ban, Arab, hdnna, ‘was favorable, merciful’,  Akkad, jihnanuni , ‘he has mercy on me’, jenni-  nunu , ‘he has mercy on us’. Cp. the first ele-  ment in the Punic PN. Hannibha'al , ‘Hannibal’,  lit. ‘my favor is with Baal’. Cp. also Ann, Jane,  Jenny, Joanna, John.   Hansard, n., official reports of the Parliament at  Westminster. — So called fr. Luke Ha
=== Ionian, LEAF 0
67); cp. anion, cation.   -ion, suff. forming nouns denoting state , con-  dition or action. — L. -id, gen. -ion is (either  directly or through the medium of OF. and F.  -ion). Cp. -ation, -ition.   Ionian, adj. and n. — Formed with suff. -an fr.  L. lonius, fr. Gk.’Idmoq, ‘Ionian’, fr. "Iuv (gen.  Iwvoq), contraction of Tlwv (gen. ’Movoq),  ‘Ionian’, fr. orig. *T£fo>v, whence Heb. Ydwdn,  Akkad. lamanu , lavanu, Egypt. Y e v a na, Y e -  v a nna, ‘Greek’. Cp. also OI. Yavanah , OPers.  Yauna, ‘Greek’, OI. yavanikd, ‘Greek woman’ ;  ‘curtain (in the theater)’, lit. ‘Greek (partition)’.   Ionic, adj. — L. lonicus, fr. Gk. Tamxoq, ‘Ionic’,  fr. v Igiv. See prec. word and -ic.   Ionium, n., a radioactive element pertaining to  the uranium group {chem.) — ModL., formed  fr.-ion with suff. -ium; so called in allusion to  its ionizing power.   ionize, tr. v., to separate into ions. — Formed f
=== Ivan, LEAF 0
c  elements (chem.) — See prec. word and cp. e.g.  radium , sodium,   Iva, n., a genus of plants, the marsh elder (bot.)   — ModL., fr. Gaulish ivos, whence also F. if,  ‘yew*. See yew and cp. uva.   Ivan, masc. PN. — Russ., fr. Gk ’Icodlvv^q. See   John.   -ive, suff. meaning ‘tending to; of the quality of’.   L. -ivus (mostly through the medium of F.  -if, fern. -ive).   ivory, n. — ME. ivorie , fr. OF. ivurie (F. ivo/re),  fr. L. eboreus , ‘of ivory’, fr. ebur, ‘ivory’, bor-  rowed fr.- Egyptian db, abu , ‘elephant, ivory’,  prob. through the medium of the Phoenicians.  The same word appears in the second element  of Heb. shen-habbtm, ‘ivory’ (lit. ‘tooth of the  elephant’), whence Yebu (= Heb. Yebh), ori-  ginal name of the island Elephantine; cp. also  OI. ibhah, ‘elephant’, and the second element  in Gk. iX-i^oLQ, ‘elephant’. Cp. eburnine,  elephant.   ivy, n. — ME. ivi, fr. OE. If
=== Ann,\s+Anna LEAF 0
al sound. — G. Anlaut , fr. an, ‘on,  at’, and Laut, ‘sound, tone’, G. an is rel. to E.  on (q.v.) G. Laut , ‘sound, tone’, derives fr. laut,  ‘loud’; see loud. Cp. ablaut, auslaut, inlaut,  umlaut   Ann, Anna, Anne, fem. PN. — L. Anna, fr. Gk.  "Awa, fr. Heb. Hannd h , lit. ‘grace’, from the  base of hdnan, ‘he was gracious, showed favor’.  See Hannah.   anna, n., an Indian penny. — Hind. and.  Annabel, Annabella, fem. PN. — The name is  usually interpreted as a compound of Anna and  Bella. It is more probable, however, that it arose  from a misreading of the name Amabel for Ana-  bel. Cp. Arabel, Arabella,  annabergite, n., a hydrous nickel arsenate (min-  eral.) — Named after Annaberg in Saxony. For  the ending see subst. suff. -ite.     annalist, n., a writer of annals. — F. annaliste, fr.  unnales, ‘annals’, fr. L. annales. See next word  and -ist.   annals, n. pi. — L. annales (sdl
=== John,\s+masc LEAF 0
uff. -er.   johannite, n., a hydrous uranium copper sulfate  {mineral.) — G. Johannit, named after Arch-  duke Johann of Austria (1782-1859). The enc ng  - it goes back to Gk. see subst, suff, -ite.  John, masc. PN. — ML. Johannes , fr. Late L.  Joannes , fr. Gk. *Io>avvr)<;, fr. Heb. Yohandn, lit.  ‘the Lord is gracious’. For the first element see  Joab and cp. words there referred to. The second  element derives fr. hdnan, ‘he was gracious’. See  Hannah and cp. Ivan, Jane, Jean, masc. and  fern. PN., jenneting, Jenny, Joan, Joanna,  Johnny.   John Bull, the English nation personified. — Fr.  John Bull , a character representing the English  nation in Arbuthnot’s satire The History of  John Bull (1712).   Johnny, masc. PN. — Formed fr. John with  dimin. suff. -y.   Johnsonese, n., a pompous, inflated style. —  Prop, the style of Dr. Samuel Johnson ( 1 709-84).  For the ending see suff.
```


## [2026-09-06T15:13:41.693Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SOD y'n / grace\"; grep -n \"443\" SOD_pages.txt | head -5; python3 - <<'EOF'\nimport re\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('SOD leaves',len(leaves))\nhits=[(i,m.group(0),l[max(0,m.start()-150):m.start()+300].replace('\\n',' ')) for i,l in enumerate(leaves) for m in re.finditer(r\"y'?[`‘]?n\\b.{0,40}grace|grace\",l)]\nprint(len(hits))\nfor h in hits[:15]: print(h[0],'|',h[2][:300]); print('--')\nEOF"
}
```


## [2026-09-06T15:13:42.668Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT yauna\"; grep -n \"^yauna\\|yauna-\\|^yāna\\|yana-\" KNT.txt | head -20"
}
```


### [2026-09-06T15:13:43.524Z] TOOL RESULT

```
== SOD y'n / grace
5016:          KG pl77; Hen. BSOAS 12, 606 n9; Mittclir. 94        443 »zyr-' M, B                  O^jl jT < jpjjT
7930:1443 'rSyp' «> 'rS'yp*
8512:        BSTBL, Dhy.; >sprYm>kw, VJ 340, 443, 962;    *<J      perfect, complete, completely
10803:                                                 ^                    2443 V* B                                            ofc.u
11073:                                                                       VJ 1469, 1443; Hen. ZDMG 1936, 197; fiT'nw,
SOD leaves 645
12
228 | C2 gloss. 4104 Yft- =* YPt-                                                Yamyak                                                                  disgrace 4105 Tfty C                                                      STii 6.7; S W, C2 pl67, 27-8                                      jj*j<(SXJ)<^ 
--
228 |   BSTii 894.20; C2, 54R20                                      Yamyawe                                                                   humbling, disgrace  4106 Yh B,S                                                       C2, AR26                                               W'J'jJ      xa ©pron. 
--
392 |                                                     patl/eO (ptytyO ©ob. -y 8070 ptyrnyy M =* ptyrny                                               disgraceful, contemptible 8071 ptyrwS- M                                         0^.3 j          BSTii 906.5, 843.30, 57: C2, 40V 5, 68R30 V26 n      pat
--
392 |                                    patiGya (ptytyO =»pty5y\ pt}y52                                                                       contempt, disgrace                                                         J'ojl 8073 ptyrys- M                                                        STi 45.9; ST
--
447 |  adj. Syr>kh, VJ; TSP 13.5, 2.12;          Dhy. 229                                                                1981, 21V5 "goodness, beneficence, grace" C2                                                                                  gloss, pi 32, 61R23; S W, AO 1981, 17 9409 syrV     B      
--
448 | zy(y)) ©pi. -/; ob.               sirsktya (syrqty*) =»syr*kty\ syry*kty*        pi. -ty =»syrywzc, syrxwzy(y)                             good deed, grace       friend, well-wisher                                        BBB f38; STii 1.10, 3.47; C2 n pi 32, 133; Gersh.       TSP 2.151, 255, 9.116; 
--
510 | , S                                     yjjxjj           yan ©<OP yana            ya ©<wy* ©pron. art. nom. f. & loc.                          mercy, grace, favour, wish            that, in that                                                GMS 181; VJ 1215, 1220; SCE 257; TSP 2.587,               
--
511 | ^m     <c~^»j ^        yan-8Parakya ©ob. -/; pi. -yt                                  BSTii 873.4, 906.7; C2, 23R 10, 24 n p24, 40V7,        {gift o/)grace, favour, blessing                                 66V7, 66R4; S W, AO 42, 1981, 19, yatukani                                                    
--
550 |       dew    5989,5994,6015                     discussion   9944 GcOdeprive         7116, 7144          Dewashtich      3805                      disgrace    4116,4117,8084 deprived       7110,7131, 11608        diadem     3739                           disgraceful    8082 depth      5844          
--
550 | ashtich      3805                      disgrace    4116,4117,8084 deprived       7110,7131, 11608        diadem     3739                           disgraceful    8082 depth      5844                        diadem-bearing      3740                  disgust 8117,8118 deputy      7479                  
--
556 | 33,         2046, 9737, 9793, 9824, 9900           governor 3904, 5727   9540, 9542                          gods     2545, 2548, 2568, 2606, 2612,   grace 9441, 10898, 10904                                          11123 GcOgive a judgement      6395                                                 
--
641 | Slave...", typewritten text >dycopied for the xLi/L               4   Fray. act.              Frag. act.                                    author by grace, independently of its publicationt in Japanese xxxix/R             11                                                                        by 
--
```


### [2026-09-06T15:13:43.573Z] TOOL RESULT

```
=== KNT yauna
5655:pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
5657:pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
5839:yaniy соп]. ‘where, whereon’: lsn. *ya^mi (= Skt. ydsmi-n, Av. yahmy-a ‘where’) to relative stem ya-, with -n- after isn. *yand, cf. isn. lyand to tya- (hardly yanazy, loc. formed on stem yana- extracted from isn. *yand, as taken by Bthl. Ат 1262; not miswritten for tyanaty, as taken by Müller, WZKM 7.112; other theories in Tm. Lex. 120 s.v.). Syntax $296. XV 22.
```


## [2026-09-06T15:13:50.354Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"yauna\" KNT.txt | head -20; echo \"=== ionia/greek\"; grep -n -i \"Ionian\\|Ionia\" KNT.txt | head -10"
}
```


### [2026-09-06T15:13:50.411Z] TOOL RESULT

```
830:A?P 26 iyam : Yauna : takabarü ‘this is the
1766:drüya-, Yauna-, Labanüna-, Sug(u)da-, Sku"za-,
1991:Katpatuka ‘Cappadocia’; Karka ‘the Cariang’; Yauna ‘Ionia’ or Yaund ‘the Ionians'; Sparda ‘Sardis, Lydia’; Skudra ‘Thrace and Mace- donia'.
2010:57 Same as Fem. as Derivative Pl. Ethnic Masc. as Province Ethnic Province Ethnic as Province Province Babirus X Babiruviya Maka Maciya* Мастӣ Майа X Mudraya X Mudraya Yauna X Yauna Saka X Saká Saka Sug(u)da Skudra x* Sparda Spardtya Zraka x* Натайа Harawats§ Harauvatiya* Hiduš Hiduya*
2027:Nom. Sg. martiya, х$йуабтуа, Ката, baga, drauga, hamiciya, атиќа; man’s name, Kabijiya; place names and ethnics Раза, Майа, Sugda Suguda, Saka, Sparda, Mudréya, Uja боја, Yauna, Parðava, Armina, Arminiya, Asagaria, Gadāra, Márgava, Uyjiya.
2040:Nom. Pl. martiyd, z$ayatiyà, hamiciyd, anuštyā, takabard, tigrazaudà, haumavargà, paruva, Mada, Вока, Mudrüyà, Yauna, Uvjiya; with double
3474:15 Qura : Arabaya : Mudraya : tyaiy : drayahya : Sparda : Yauna : Mada : Armina : Kat 16 patuka : Parfava : Zraka : Haraiva : Uvárazmiy : Bāxtriš : Suguda : Gadara : Sa
3550:$ Ariyãram- KT, both occurrences; not -rdm-, with RI. 1 [ота KT, cf. ота DBa 11 KT; not adaià with Andreas and Hüsing KZ 38.255. *VITI : manā : taumaya: ef, Hist. App. I. © duvilàparanam, sce Lex. “ On list of provinces, see Kent, JNES 2.302-6. 5 Yauna Bv. Gr. 6348; not ушпа] = Уат], with KT, cf. Ri.’s ашпа]. 1 [Sugluda. KT. © јот" RI., KT; instead of the expected fersherueme, ? agr"H--] KT, ef. Ri.’s аё; ортеу“ Cameron; see Lex. s.v. agriya-. ? tyanā : mand : dálà of RI. and KT is correct; not dittography for tyà : mand, cf. the idiom in XPh 49 and 51-2. 2 араттуйуа, from pari- + ay-; for wrong interpretations, see Lex. u-s Auramazda | miaiy :| ima KT. ** habnalddrayat{y] KT. ?hauvam KT. *avajata RL, KT; not to be emended to avdjate, with Gray, Bthl. # On Gaumata-Bardiya, sce Hist. App. П. * On the OP calendar, see Hist. App. IV.
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4330:7 Üja : BabiruS : Авита : Arabya : Mudrüya : Sparda : 8 Yauna : Майа: Armina : Katpatuka : Parbava : Zraka : 9 Haraiva : Uvürazmi$ : Báxtri& : Suguda : Gadára : 10 8atagut : Harawvati$ : Hidus : Skudra : Yound : taka
4733:: Yauna :
4735:: Yauna : takabará : : Putàya :
5808:| Yauna- adj. 'Ionian'; pl., also a province of
5810:(1) ‘Ionian’: Yauna nsm. A?P 26. Yaund npm. DSf 33f, 48; as nam. (556.1) А?Р 23.
5812:(3) ‘Tonia’: Yauna nsm. DB 1.15; DNa 28; DSm 8°. Yaund absm. DSf 42.
=== ionia/greek
828:А?Р 15 йат : Saka : tigraralud|a (as above). А?Р 23 iyam : Yaund ‘this is the Ionians'. A?P 24 бат : ака : paradratya ‘this is the
831:Ionian (sg.), petasos-wearers (pl.)".
1991:Katpatuka ‘Cappadocia’; Karka ‘the Cariang’; Yauna ‘Ionia’ or Yaund ‘the Ionians'; Sparda ‘Sardis, Lydia’; Skudra ‘Thrace and Mace- donia'.
3564:$6. 1.12-7. Saith Darius the King: These are the countries which eame unto me; by the favor of Ahuramazda I was king of them: Persia, Flam, Babylonia, Assyria, Arabia, Egypt, (those) who are beside the sea, Sardis, Ionia, Media, Armenia, Cappadocia, Parthia, Drangiana, Aria, Choras- mia, Bactria, Sogdiana, Gandara, Scythia, Satta- gydia, Arachosia, Maka: in all, ХХИ provinces.
4089:§2. 5-18. Saith Darius the King: By the favor * 1 of Ahuramazda these are the countries which Ie got into my possession along with this Persian folk, which felt fear of me (and) bore me tribute: Elam, Media, Babylonia, Arabia, Assyria, Egypt, Armenia, Cappadocia, Sardis, Ionians who are of the mainland and (those) who are by the sea, and countries which are across the sea; Sagartia, Parthia, Drangiana, Aria, Bactria, Sogdiana, Chorasmia, Sattagydia, Arachosia, Sind, Gandara, Scythians, Maka. |
4230:.. (= DNa 24-8), Ionians, (those) who are by
4282:83 ‘Babylonians’ here seems to denote 'Ionians resi- dent in Babylonia’, ef. Kónig, Burgbau 25; confirmed by the reading of Akk. frag. Y line 9 of obverse (АКК. 21 = OP 30), given by Scheil 24.107. 55 Between the text of 55 and that of 56, Scheil's fragment 0 indicates the presence of vašnā Auramazdaha (JAOS 51.196) ; but there is no space for it in tablet a. There is also no room for aita tya, inserted here by Hz. AMI 3.38, 3.77. € {aha} Вга. WZKM 39.36; probably better than abava, Kent, JAOS 52.223.
4294:Sg. 30-5. The cedar timber, this—a mountain by name Lebanon—from there was brought. The Assyrian people, it brought tt to Babylon; from Babylon the Carians and the Ionians brought it to Susa. The yakd-timber was brought from Gan- dara and from Carmania.
4296:{81. 40-5. The silver and the ebony were brought from Egypt. The ornamentation with which the wall was adorned, that from Ionia was brought. The ivory whieh was wrought here, was brought from Ethiopia and from Sind and from Arachosia.
4299:wrought the stone, those were Ionians and
```


## [2026-09-06T15:13:51.134Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in (509,510,511):\n    print('==== LEAF',i)\n    print(leaves[i][:2600])\nEOF"
}
```


### [2026-09-06T15:13:53.374Z] TOOL RESULT

```
==== LEAF 509
                                                                                                                      442
 xwystr

 10852 xwystr      M                      j£ J ^Ujj i^j              C2, 102V30
          xoystar, [x<5star], xwestar ®<*xwd(y)ist-tara;
            <*xweste-tar ©ob. pi. ~ty =^xwstr, ywystr,        10862 xy' S
                                                                    xe ©3sg. opt. =>Y*y, y*t
            xwynstr                                                 MSP bl39
          chief, superior, Presbyter
          S W, RL 207; GMS 230, 1248, 1301; BBB b45,          10863 xyJ C -» xy5
            611                                               10864 xyd C =» xy5

10853 xwyz                                           j^\y>~   10865 xy8 M, S                (u>> jll* j>)\&\ <jT ^J
                                                                    xe8/9, x!9 (xyd, xy55) ©demons, pron. & adj.,
      xwez, xoyz, [x5z] ©*xwdzaya-         =»xwz-,
                                                                      nom. sg. & pi. =»wy8, yy5
                   -
                yzsh
          (to)ywwi                                                   that, this, these
          S W R 207; GMS 232; KG 550, 572, 3sg. impf.
              ,    L                                                 GMS 1109, 1403, 1420-3; BBB 545, 555 bl9;
                                                                       Anc. Lett. 2.46, 48; MSP p55; STi 21.16, 33.14,
10854 xwz- C                       o^J'^tjpy idij'j^^                   19 etc.; STii p584; BSTi 136; C2 gloss. p235;
      xoz ©Arm. xoyz
      (^examine, (/o)test                                              xySywn "instantly" GMS 1109; xydqy, C2
      S W, C2 p85.15, 3sg. pres. xwzt, 102R18, 19; xw
                                                                      p84 n 59; xyd n>x, C2 p85.21 Mle voici"
        zU BSTii 829, 18.19; 3pl. subj. xwznU 40V 15:         10866 xyS8 M =* xy5
        BSTii 907.15                                          10867 xySywn M                               ^U^pJjy
                                                                    xe9-yon ?
10855 xwz- C, S                  ja^^ t&J'j jjT 'j^lj*-
      xoz, xwaz, xwez ©xdiz <*xwazaya ©pt. xwst                     instantly, on the spot
        ^xwj-, ywyz-, Ywz~i xwyz                                    GMS 1109
      OcOrequest, (/o)wish, (/<?)ask                          10868 xynt =* yyntwh
      GMS 232, 595; STi 73.15, 75.4; STii 3.6, 6.5, 30,
                                               
==== LEAF 510
     443


           xyp&wnty, STi 8.14, 37.14; BSTi 335; BSTii                    C2 gloss. p233; Benv. Eti; JA 1955, 320; Hen.
             842.12, 897.76; C2 gloss. p235;voc. xyp&wnt\                  Tales. 481.49; GMS 1466 A
             ST137.21; pi. xpp&wntt, C2, 12R11; voc. pi.          10884 y>b     C =» y>p-
            xyp&wnty, C2, 12R26                                   10885 y}p-      B, M      o$£ J*** ^jJio^f jum*^ < <J-^ 0'^,
     10874 xyr- M, C                   o-^jj* io*^cS j>- ij&j
                                                                         yap (y>b) ©Khwar. y'JJ
           xer ? xi/ar ? ©3sg. impf. =*xrt-, y'yr-, Yyr~                 (fo)wander, (ro)rove, (to)travel
           (to)go, (to)go out, (ro)go away                               GMS 900, 1002; Vim. 85, BSTBL; C2, 83 V6;
                                                                           AVS 109
                                                                                                                                    y}n
           GMS 611; BSTii 890.57; C2, 60R25, 60V25 p77,
             30; Sund. AI 28.186; CII 1990 E7; Yyr% Tales
                                                                  10886 y>p>k =» y'pch
             475.15, 478.9
                                                                  10887 y>b»qc C                                        jkf^
     10875 xyz- M                                     <>_>-
                                                                         yapakc ©ob. -y
           xi/ez ? ©Shiz-, tezza-; *hahiza-; MP >/zyz,                   erring, wandering
             w/iyz ^yxyzyy
                                                                         BSTii 893.14: C2, 13V 14; GMS 1002
            (ro)creep
                                                                  10888 y>p»y =* y>pk
            BBB 512; Gersh. BSOAS 14, 493
                                                                  10889 y>pch
                                                                        roving B                           J^f^^jj*'^.^
     10876 xjzyy =» z'yyyz'k, z'yxyzyy
                                                                        yaPc (y>P>k) ©f. n.
     10877 xz^ M                                      (j->r)0'>
           xazan ©ob. -y
                                                                         VJ 1413 n p98; AVS 109
           fall, autumn
            Sund. Man. Lett. 306.31                               10890 y>pk
                                                              
==== LEAF 511
                                                                                                                      444



  yV                                                                                                           *y l&^£
          3.206, 211; Padm. 23, 34, BSTBL; STii 3.25,           10910 y^kmync       B
                                                                                                        ync
          6.36, C2, 68R15; Frag. Len. 6R7                             yate-menc (y^kmync)          >y}tm

 10899 y,n> C
                                                                      G?/)flesh
                                                                      SCE 376, 252; GMS 1103
       yana(k) (yWkh) ©pi. y>nt, fntt; demons.
          pron^ nom. sg. f. «*y-, }yny(y)                       10911 y't'yn'k B
       this
                                                                      yatene =»y*tny
       GMS 1402, 1497; VJ 1032, 1245; STii 7.8, 6.23;
                                                      csJ             TSP  2.509
         C2, 12 VI 1, 68R17: BSTii 842.17; S W, TPS                   (o/)flesh
         1994, 48                                                                                                  -*
                                                               10912 y'tyw'r =» y'tywVk                          J* /
                                                 «J>.
 10900 yWkh     B, M => y)n>                                   10913 y'tywVk B
 10901 y'nd   M =» y>nt                                               yat-xwar(e) (y'tyw'r) ^y't'k yw^y jy-£~*t
 10902 y'nh S                                                         carnivore, flesh-eater
       yan ©<Skt. yana                              Lr lA^J           TSP 2.960; y>trw>r% TSP 2.510, 512, 643, 733,
       chariot                                                          796, 909, 21iii 5; SCE 297
       Frag. Len. 93.8, ynnh
                                                               10914 y'tk => y>t>k
10903 y»nt C                                                   10915 y>tk kr'wny B
                                      ^y*!!*, y-, }yny(y)
      yand (y>ntt) ©pron. art. pi                                     yate-karune -^y^k
      these, those                                                    meat production
      EGSii 13a GMS 1498; STi 18.6, 26.3, 36.8; STii                  TSP 2269; Hen. Texts. 734
        7.8, 6.23; C2, 94V20, 69V25, 66 V6, 61V25; VJ
```


## [2026-09-06T15:14:01.042Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i in (510,511):\n    l=leaves[i]\n    for m in re.finditer(r\"yan\\b|y\\)n|y\\}n\", l):\n        print('LEAF',i, repr(l[max(0,m.start()-500):m.start()+500]))\n        print('~~~~')\nEOF"
}
```


### [2026-09-06T15:14:02.869Z] TOOL RESULT

```
LEAF 510 "                                         yap (y>b) ©Khwar. y'JJ\n           xer ? xi/ar ? ©3sg. impf. =*xrt-, y'yr-, Yyr~                 (fo)wander, (ro)rove, (to)travel\n           (to)go, (to)go out, (ro)go away                               GMS 900, 1002; Vim. 85, BSTBL; C2, 83 V6;\n                                                                           AVS 109\n                                                                                                                                    y}n\n           GMS 611; BSTii 890.57; C2, 60R25, 60V25 p77,\n             30; Sund. AI 28.186; CII 1990 E7; Yyr% Tales\n                                                                  10886 y>p>k =» y'pch\n             475.15, 478.9\n                                                                  10887 y>b»qc C                                        jkf^\n     10875 xyz- M                                     <>_>-\n                                                                         yapakc ©ob"
~~~~
LEAF 510 "   yat ©<*wpa- yata-t *upa- yama                                flashing\n                                                                        yalinciy ©<Uigh.\n           safe, healthy\n           MDii, Nov. 4R17, 19 p22.17 n p43.7; Gersh.                   Sogdica. 29.4a\n             Advice. 93\n                                                                  10898 y'n B, M, C                        jjjT <*jia u=^ «,j»laJ\n     10883 y> C, S                                     yjjxjj           yan ©<OP yana\n           ya ©<wy* ©pron. art. nom. f. & loc.                          mercy, grace, favour, wish\n           that, in that                                                GMS 181; VJ 1215, 1220; SCE 257; TSP 2.587,\n\n\n\n\n                                         T^ppapsr\n"
~~~~
LEAF 511 "2, 1245; STii 7.8, 6.23;\n                                                      csJ             TSP  2.509\n         C2, 12 VI 1, 68R17: BSTii 842.17; S W, TPS                   (o/)flesh\n         1994, 48                                                                                                  -*\n                                                               10912 y'tyw'r =» y'tywVk                          J* /\n                                                 «J>.\n 10900 yWkh     B, M => y)n>                                   10913 y'tywVk B\n 10901 y'nd   M =» y>nt                                               yat-xwar(e) (y'tyw'r) ^y't'k yw^y jy-£~*t\n 10902 y'nh S                                                         carnivore, flesh-eater\n       yan ©<Skt. yana                              Lr lA^J           TSP 2.960; y>trw>r% TSP 2.510, 512, 643, 733,\n       chariot                                                          796, 909, 21iii 5; SCE 297\n       Frag. Len. 93.8, y"
~~~~
LEAF 511 "                                  -*\n                                                               10912 y'tyw'r =» y'tywVk                          J* /\n                                                 «J>.\n 10900 yWkh     B, M => y)n>                                   10913 y'tywVk B\n 10901 y'nd   M =» y>nt                                               yat-xwar(e) (y'tyw'r) ^y't'k yw^y jy-£~*t\n 10902 y'nh S                                                         carnivore, flesh-eater\n       yan ©<Skt. yana                              Lr lA^J           TSP 2.960; y>trw>r% TSP 2.510, 512, 643, 733,\n       chariot                                                          796, 909, 21iii 5; SCE 297\n       Frag. Len. 93.8, ynnh\n                                                               10914 y'tk => y>t>k\n10903 y»nt C                                                   10915 y>tk kr'wny B\n                                      ^y*!!*, y-, }yny(y)\n      yand (y>ntt) ©pron. art. pi      "
~~~~
LEAF 511 "61V25; VJ\n                                                               10916 y'tkmync ==> y^kmync                  tf«5*»\n         1245; Hen. JRAS 1944, 138.42; S W, TPS\n                                                               10917 y'tqwny C\n        1994, 48                                                     sorcery\n                                                                     yatkoni/e ©<*yatu-ka+ ana+ya -»y}twknyh\n10904 y'n-Bbrtiy1    C    cS^ ^Ua*l<o~j ^m     <c~^»j ^\n       yan-8Parakya ©ob. -/; pi. -yt                                  BSTii 873.4, 906.7; C2, 23R 10, 24 n p24, 40V7,\n       {gift o/)grace, favour, blessing                                 66V7, 66R4; S W, AO 42, 1981, 19, yatukani\n                                                                                                                   J*°r\n       C2, 31V3, 25, 54V22, 57V9 n p75; Benv. JA\n          1959, 132; BSTii 893.3, 25, 895.52, 905.7; cf.       10918 y'tmwnt       B                     "
~~~~
```


## [2026-09-06T15:14:15.330Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT yana\"; grep -n \"yāna\\|yana-\" BRT.txt | head -30"
}
```


### [2026-09-06T15:14:15.381Z] TOOL RESULT

```
=== BRT yana
3909:•  j.  aiwi.zilzuyana-  Adj.,  PPM.:  %.zav:
3922:•  j,  aiwi-sayana-  n,  'Bewohaen':  yaha . .  *aiwUayama  darr/a  -na  . .  b>nymyS.- siabm  (sd.)  H\.to.^^.
4871:•  j.  ayana-  n.  'Gang,  iter";  ^vat  *ana dbHsl»m  'fum  parankaSäiti  "quantum  p!u- rimum  iter  .  ,"  N.^;  —  yme  paittsi^A!) garS  nm3nim  Yl_J.  4,
5545:•  j.  airyana-  Adj.  'arisch':  "m/w  :^ar3nS Yt.  J<?.  1,  5,  7,  8,  S.  2.  9*>;  —  sonst  von vasjah-  (sd,,  auch  fdSt):  °n»m  vagjö,  'yeiie val/aAi.
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
8315:IComp.i  upa\-*ayiatä-  l^lSS.  1),  zum  V.  'cy--, eig.  'da*  Herzugehen'.  —  aL  vgl.  upäyana-  n. 'Herbeikommen'.  —  Pü. :  dtr  (oder  dar^  apar rawunik,    Sü.i   iiparipraifltii    mit   der    Erl.r
9316:Itehrter  Reihenfolge):  adari^ä  airotäraJca.^^  ,  ^^  karsnayana-  patr.   Adj.  'von  Karsna
9813:gaorayana-
9859:Bed.  ?  —  Vgl.  gaerayana-.
9860:•  j.  gaorayana-  m.  EN.  eines  Gläubigen: 'nahe  asoonü  Yt  13. 1 1 8.
10102:•  j,  gaya^stayana-  patr.  Adj.  'von  Gaya- '  iistay  stammend,  dessen  Nachkomme': asa.^ad>:nahe  'nahe  asaotis  YU13. 114.
10175:•  j.  gav-a'äayana-  Adj.  'die  Wohnstätte [  der  Rinder  bildend,  von  Rindern  bewohnt':
10354:j.  gävayana-  i)  Adj.  'fiirs  Rind  be- stimmt': nmJmm  'mm  "einen  Rinderstall" V.7.^.14.  2)    n.    'Rinderstall;     Stall':
10541:•  j.  xayana-  Adj.  (fem.  -na-)  'fontanus': apfm  °nqm  . .  apim  zrayanqm  "das  Quell- wasser .  ."  Yt,().2.
10542:Ableit.  am  xan-  (vgl.  xqnya^*\  —  FQ. :  äp  i xänlk,  äp  pa  x3ti.  —  ")  Wie  ist  die  Bildung zu  Stande  gekommen?  Wohl  einfach  durch Reimen  auf  das  (folgende)  irayana-i  s.  lu gaimai-anl-.
11676:•  j.  Jistayana-"  patr.  Adj.  Von  Jlltay stammend,  dessen  Nachkomme :  asähurahe (sd.)  "nahe  asaonS  \t.  ij.  113.
13334:Komp.:  *däi(yi.iipa'sayana- Adj.-'t-iat^ ;  S  z6j, —  ^upa-sayana-  n.,  znm  V.  liy-l  ii.  itiyaiia-. n.  —  V&.:däiaa/>aiihi{i)iavc;  Npä.:  6a  ulirüA pusß  bid,  mit  der  Etl.  1  ka  fas  az  vaki  1  afriix- lan  läaim  nihatid  an  puiS  ('Uoterslüliung').
13387:•  j.  dinayana-  patr.  Adj.  'von  Dänay abstammend,  dessen  Nachkomme''':  kir^ süspd  .  .  yS  janal  zaranyS.pus?m  hifäspsm vansaotnca  'imn  Yt/p.  41.
13388:Ableit  aus  'dänay-  m.  EN".  —  ■>  Denkbar wäre  auch,  dass  dänayana- za 'dSnav- gehöit; vgl.  lu  märgaya..
13812:*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
13813:*sayana-Ti.,  lum  V.  jiiy- ;  ai,  inj'««.!- n. 'Lager'
16126:•  j.  par«9ii.vae8ayana- Adj. 'auf  breiter  '^■)-  ii' ■ .  patkärinä').  —  i)  j  2/2  aE.  — Warte bcfindhch':  tni>>nm..  'ramYLiO.T.       ''  ^-  ^^ ^'"'i'  Sp.  869  o.,  m.
16489:•  j.  baevar3.vaeSayana-  Adj.  'mit  zehn- tausend Warten':  nmämm  . .  bagvan.misUm 'tarn  V.  18.  aS;  zit  Vyt  4$.
16737:•  j.  bayana-  m.  Name  eines  Bergs  oder Gebirgs :  ahmal  haca  garayS  fraoxgran  . .
17759:•  j.  frayana-  n.  'Weg,  Bahn':  äiiri  mi- %rahe  'nä  .  .pähanä  jafrä  gaoyaotse  "klar sind  M.%  Wege  . .  weit  und  tief  zur  Weide" Ytio.  112.
17760:Komp. :  */ra-\-ayana-\  %  268.  3  b.  —  ai.  fitS- yatia-  n.  'Eingang,  Anfang'.
18277:•  j.  fräSaoStrayana-  patr.  Adj.  'von  Fra- ^aoslra  stammend,  dessen  Nachkomme': husyao'^nahe  -nahe  Yty.  104;  —  s^ä- dalnahe  'naht  Yt.  13. 104.
18364:•  j.  fryana-  m.  EN". :  s.  unter  fryana-,
18366:•  j-  'fryana-  Adj.,  PPM.:  s.fräy:
18368:"  i-t  g-  'fryana-,  j,  fryana-  m.  Name  einer gläubigen  /arischen  Familie":  naptyaSsa naßucä  türahyS  .  .  °yJnahyä  aojyaisä  Y. 46.  \2;  —  ysistö  yd  'yanariqm  "K  (aus der  Familie)  der  Fry''  Yt  5. 81 ;  —ydUtahe 'yJnanam  YtJJ.  120.
```


## [2026-09-06T15:14:17.049Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB/HRN yunan\"; grep -n \"Yūnān\\|Junan\\|jūnān\\|Ionier\" HUB.txt HRN.txt | head -20; echo \"=== PHD\"; grep -n -i \"yōnān\\|hrōm\\|yavan\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-06T15:14:17.124Z] TOOL RESULT

```
=== HUB/HRN yunan
=== PHD
```


## [2026-09-06T15:14:23.160Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yäna-\\|yana-  n\\.\\|'Gunst\\|Gunst,  Gnade\\|yä-  \" BRT.txt | head -30; echo \"=== search yā root\"; grep -n \"^•  *[gj]\\.\\s*yäna\\|j\\.  yäna\" BRT.txt | head"
}
```


### [2026-09-06T15:14:23.244Z] TOOL RESULT

```
3046:•  g.  aköyä-  f.  'Androhung  von  Bösem' '' : at  zT  töi  vaxsyä  .  .  hyal  °yä  (NS-)  dng- väiti  ustä  yi  abm  dädri  "von  den  bei- den . .,  von  dem  Bösen,  das  dem  Drug- anhänger  angedroht  ist'',  und  von  dem Glück  dessen,  der  am  A.  festhält"  Y.5/,8.
3092:•  g-  ag»nyä-  f.  'melke  Kuh,  Milchkuh': apas&l  vä  agt}c3  vä  mätprqicä  vä  'jrä *drfguäayanh6  vTspBpaitli  avaoÜ'amS  "und euch,  Wasser,  rufen  wir  an  als  die  träch- tigen und  die  Mutter-  und  die  melken Kühe,  die  fiir  den  Armen  sorgen,  die  all- tränkenden"   ^.38.$.
3093:«L  äghnyä-  1.  "Kuh'  (auch  von  Wulken  and Flütseu);  Bthl  AF.  3.  39'  —  Vü.-.  agjnjiä (in  Av.-Buchst)  mit  der  Erl.:  xön  'Blut';  vgl. zn  ma^ioHt:
3113:KotnpA.  i  Ableit.  —  AbleiL  aus  ajra-.  —  ü. agriyä-  Adj,,  mp.  airyai.  —  PB.!  a^ryat.  — 1  Hd$.  srairim,  d.  i.  mp.  j-iir,  womit  die  vor- ausgehenden  Wörter  trjra,  a-ftim  bbersetit werden  (vgl.  asar  für  anaira-\  und  atriin.  ~- *)  Pü.  erl.  ayryai  afiar  soüin  mit  loi  i  sar "Waschen  des  Kopfes";  vgl.  West  SEE. /A 456.
3457:•  j.  at-tävaxiyä-  fem.  Adj.  'die  Worte  a/ tJ  vaxsyä  enthaltend,  damit  beginnend': 'yqm  Aäitim (sd.)'^  yazamaide  Y.jo.  la;  — ••ya  häitis'''  Y.30  Überschr.
3461:•  j.  at.fravax5yä-  fem.  Adj.  'die  Worte atfravaxlyä  enthaltend,  damit  beginnend': -yqm    kaittm  (sd.)'*  yazamaide  V.4^5. 12;
4130:ai.  asafyä-  Adj.  —  Pü. ;  anäikärän,  erL :  nasäk i  nikän,    dazu  die  Bern.:    asi  ie  aHarianlkän
4187:•  j.  anbuyä-  f.  'Erwerb  des  Anspruchs  auf das  (andre)  Leben':  imnm  "yamia  *a!a- yamca  ra%wamca  rafufriiimca  äyese  yeHi
4254:•  j.  anaiSyä-  f.  'Bann,  Interdikt':  cvanl>m drajS  zrviln^m  aitiha  z^mS  (%t~,  3  b)  'ya (NS.)^a/  ahmt  .  .  V.6.1;  i.
4725:ai.  vgl.  anyb'nyä-  Adj.  —  Pü.:  !and  ä«  maf  paiüünlfm  'mähe. .  "krimaht . .  baaazyehi
4855:.  j.  a-yaozdä-  f.  'Verunreinigung  Ver- . .  -  ayaBhö.Jyä-  Adj.  (mask.  -ya-)  'mit seuchung':  vT^pm  a  ahmat  'i^"  f 'dya\  ^^^^^^  (eisernen)  Sehnen':  vLlzah...
4871:•  j.  ayana-  n.  'Gang,  iter";  ^vat  *ana dbHsl»m  'fum  parankaSäiti  "quantum  p!u- rimum  iter  .  ,"  N.^;  —  yme  paittsi^A!) garS  nm3nim  Yl_J.  4,
4913:•  j.  a-yä-  Adj.  (auch  fem.)  'hin  gehend,
4926:■  j.  a-yesnya-  Adj.:  s.  unter  ayatnya-. •  j.  ayehyä-  f.  Bezeichnung  einer  Klasse weiblicher  Wesen  der^o^^ischenSchöpfiing: paxnüta  Al  kaxuit  (sd.)  .  .  'ye  (VS.)  .  . yüimaiH  JaJii  V.  21.17.
5167:•  j.  a-vahmya-  Adj.  (fem.  'yä-  'unwürdig
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
5796:l^'^  /■  57'>.  —  I'Ö-!  '""<  (»uY.  46,49)%  «/"«; i.  noch  So.  1. —  ')  Pö. ;  ähitciiit;  unklar. — »I  Näml.  des  ärigvanl:  —  i)  Eig.  'fiic  das Haus'.  —  *)  Geselle,  eig.  Saalgenosse,  Hau^ eenosse;  das  ist  der  Gast  ebenfalls. —  Eine falsche  Et  bei  Gdn.  Cama  Mem.  Vol.  140; Tj;l.  tu  'aitaj!-.  Die  Et.  vonBradkes,  der ZDMG.  40.  349  got.  ansis  'Gunst'  vergleicht, halte  ich  mindeat  für  weniger  wabtscbcinlich.
6216:a$ayä-  3
7815:•  }.  a^iSyä-  f.  'Pfosten':  mi^nm  .  .  yj .  . stawra  yä  kirtnaotti  Yt. /O.  a8.
8038:(näml.  äps)  yazamaide  täU  */ryqnmahl  lais iitmahyamahi  täÜ  ilüidyämahl  H.^S.i,. Ableit.  aus  ihiil-  (sd.).  —  al  ifutihyä-  Praes. —  iBed.  {und  ?Et.)  vgl.  PiscHEL  VSt.  i.  191, Gdn.  KZ.  jo.  5 16,  Ludwig  ABoehmGW.  iSijn. 63,  Bthl.  Stud.  /.  133,  Leuuahn  EtWb.  36, Uhlenbeck  WAiSpr.  as,  DsT.ZA.zdSt.,  JusTi TrJ.  ÄJ.  85.  —  Pu.!  dfiämenieaii,Sä.:  pjayilum  % PQErl.:  ku{ni)  äpäm  pa  tö  baväl,  Sü.:  tila  tut j-nam  tvayä  ihüyäl.  —  O  Nur  Yllipt
8064:S.  ä.airyiniä.iSyä.  —  PFl'.  lum  V.  ^a/!-.  — ai.  vgL  ffyä-  Adj.  —  Pü.  (lu  ^.48):  x''äl,un, (zu  Y.  Sl)-.  pa  iPäliiSn,  (zu  Y.  54  1.  St.  und zu    2  a  o):    xvähiinth,     (sonst) :    x^äslär.    —
8315:IComp.i  upa\-*ayiatä-  l^lSS.  1),  zum  V.  'cy--, eig.  'da*  Herzugehen'.  —  aL  vgl.  upäyana-  n. 'Herbeikommen'.  —  Pü. :  dtr  (oder  dar^  apar rawunik,    Sü.i   iiparipraifltii    mit   der    Erl.r
9044:»II.  *ki/'bü'-^''jiyä-  'mit  Sehnen  aus  -?  -';  s.  ■
9769:•  j.  gaed'o.mvr^ndyäna-  patr.  Adj.  'von  ,  pn.:  gitwar,  (lu  V.):  ges,  Npü.  (tu  Yi.):  dar 'cya  abstammend' :  paitUt3tie  . .  aratöisca  •"  r^'i')-  —  ')  S  ^^2  No.  2.  —  >>  So,  mit  S, 'noÄe  Yt  J^.  137.                                             ^  "  ^^-  '"''  *"'^-'°-
9855:Ableit.  aus  igav-,  —  ai.  gäz-ya-,  gavyä-  Adj.  — PS.  (lu  V.):  fnSlaii  gäv  pim.  —  D  iSchr. ävaya  (vor  A)  statt  a^ya  s.  S  26e.    13  c.
10753:•  j.  xäaSrB.kämyä-  f.  'Sorge,  Besorgtheit
10755:Ableit.  aus  iäma-.    —    ai.  kimyä-  f.  —   Pü.:
11582:Zum  \.  jyä-  (aus  der  volleren  Form;  s.  dazu HlBT  Ablaut  97).  —  Pü-!  *afashtisn')  kämak pa  yin.  —  i)  S.  zu  saed-  No,  2.  So  ist  lU lesen,  gegen  Haug  Essays'  366;  vgl  Pu.  zu
11800:mit  nt  '(ein  Gewand)  fallen  lassen,'  aus- ziehen' :  y3  aiwyärshayäite  kantssla  .  . pas^a  *aiwyäst»m  nitaosayäti  .  .  N.  197. Vgl,  afy.  lai  'leer',  PDw.  läiam  'ich  leere  aus'; ai.  tucckyä-  Adj.  'leer',  sbal.  tusag  'verlassen weiden',  np.  lik  'leer';  s.  dazu  Bthl.  IF.  8. 252,  Gor.  GIrPh.  i  b.  299.  —  Pü.  (zu  V.  f: tukik  bvtan,  (mV. /;>):  afar  löshüUm,  (zoN.): *nitdiimlan  (zT.  in  Aw.-Bnchsl.li  (zu  N.  Sj) erL. :  hai  Jröt  griflan,  —  ')  Hds.  taosy',  — ')  NA.  •yeinli;  s.  Var.
12354:•  j.  *tüirya-  m.,  tüiryä-  f.  'Vatersbnider, -Schwester':  yat  •ye..ya  va  para.iriäyei/i V.  72.  15,  [tairya'  V.  72.  19:  s,  unter duymiri;  —  V.  72. 17:  lies  täiryS.pu%rS, tBiTyaJuyha^
=== search yā root
21619:•  j.  yänavas'tsma-  Adj.  'der  am  meisten Gunst(beweise)  gevrährt';  yana  ahmt  °mS Yt.  14.  3.
```


## [2026-09-06T15:14:25.512Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON part1/2 حنان\"; grep -n \"حنان\\|حنین\\|حنّان\" MON_part1.txt MON_part2.txt | head -20; echo \"== MON یوحنا\"; grep -n \"یوحنا\" MON_part1.txt MON_part2.txt | head -10"
}
```


### [2026-09-06T15:14:25.723Z] TOOL RESULT

```
== MON part1/2 حنان
MON_part2.txt:43369:ونصان» حنین؛ ری اصم؛ عادل» فاتق» 
MON_part2.txt:65326:امتحان کننده؛ ج. ممتحنین. 
MON_part1.txt:54346:حنان: [ع.] (امص.) رحمت.؛ 
MON_part1.txt:54350:حنان؛ مقدددد [ع.] (ص.) بخشاینده. سیار 
MON_part1.txt:54354:حنانه: (6-)2م2هدد۱ [ع. حنانه ] (اص.) سیار 
MON_part1.txt:54355:ناله کننده نوحه کننده: ستون حنانه. 
MON_part1.txt:54398:حنین: ۱20 [ع.] (مص‌ل.) بانگ کردن از 
== MON یوحنا
```


## [2026-09-06T15:14:34.004Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21600,21650p' BRT.txt"
}
```


### [2026-09-06T15:14:34.076Z] TOOL RESULT

```
S.  unter  "hii.i'islä.
•  j.  fa/  (Sp.  630)  upazbaya  yät  paiayas- (sd.)Äi . .  Vyt  4?.  Wertlos.  {N.  6t,  62 : lies  yat.]
g.  yäl  V.  32.  4:  lies  yäal;  ~-  Y.  jfi.  6;  s. Sp.  1205  m.;  Tl^yäai;  aber  man  ver- langte NSn.
•  p.  a/Ctf*  adam  yä-a**m  jaäiyämiy  t^ur^- mazdäm  "das  erbitte  ich  mir  als  Gunst von  AhM."  D.^.3.
Vgl.  yäita-,  yänya-,  —  Zuteilt  iSt.  FOY  KZ, jj.  49,  der  die  Lesung  yürnyam  belÜnrortet. Es  geht  aber  doch  nicht  an,  einem  aaaj'äni- abgeleiteten  yäniya-  die  selbe  Bedeutung  wie dem  Grundwort  zuzuweisen.
•  j.,  g.  yäna-,  j.  yi^na-''  m.  'Gunst,  Gunst- gewährung, Gunstbeweis'  (seitens  der  Gott- heiten gegenüber  den  Menschen):  imitn %wqm  .  .  "tum  kaema  fa^yenii  Y.  9,  19;
—  apo  'mm  vS  yäsämi  . .  tarn  im  däyafa Y.  Ö5. 1 1 ;  —  datta  nS  t)m  °n>m  Y.6S.  2 1 ; Vyt.  8;  —  vindai  'fum  yaka  vindat . .  V. ig.  6;  —   vindät  t>m.   'tum  ..  Yt/7, 26;
—  °nh  (als  AP.)  baraiti  astavS  "Gunst- beweise (der  Götter)  trägt  davon  . ."  Yt. ^4-  3Ö;  —  annis  vh  nöit. .  °näis  sarana^nä (sd.)  "um  dieser  Gunstbeweise  willen . ."  Y. 2Ä9; — ye2i  sl'ttäoa  davai/i{Sp.g20ta.)  .. "wenn  er  (der  Mann)  um  seiner  (Mi^ras) Gunst  willen  .."  Yt/0. 137;  — yamyaeata Sarai uitrS . .  avaheia  paiti  yqnahe  ". .  und
um  jene  Gunst  (zu  erlangen)"  Yt,i6.6; —  °na  ahmi  yänavastitnB  Yt  i4-  3-
KompE. ;  Ableit.  —  VgL^öwitifoijiyönelnf.  —
Zura  V.j'ajB-»);  Bthl  BB.  70. 279.  —  mp._fö»3).
—  Tu.  {iMY.s,38,6a):  yän  -  Sä.:  ialyäifam,
hibham  -,  [zu  Y.  ff/.  V.  /p):  HHoaUA;    NpB.
(zu  Yt.  r4):    mii,yäri,    —    D  Zu   %'3s6.  3;
NA.  nur  zu  Yt.  !6.  (,;   aber  Fi  »uch  zu  Yt.
10.   137. —  »>  Vgl.  zBed.  »i.  yäntam  sumnäm
RV.  j.  67.  a  (U.W.),  zF.  (a)  n.ydmiün,ii  (usw.);
B.  noch  'yä/a-.  —  J)  Falsch   vergleicht   Gge.
GIrPh.    /b.  ao8  afy.  yün  'Gang'.
•  j.  yänavas'tsma-  Adj.  'der  am  meisten Gunst(beweise)  gevrährt';  yana  ahmt  °mS Yt.  14.  3.
SuperL  aus  *yäna'vttnl:  —  Npü.:  üjyar  ruiira- sandatar.
•  j.  yänya-  Adj.  'Gunst  erweisend,  Gunst (der  Götter)  erwirkend';  'nJm  manö  'nlm vacö  'nlm  ryaohn^m  .  .  zarahuüraie  Y. sS.o.
Ableit.  aus  yäna-.  —  Pü. :  yan,  SD.  1  ioihanaA,
•  j.  yämö.paiika-  Adj.,  mit  xumba-  'Vor- richtung zum  Glasbiennen,  Glasbrennofen': xumbal  kala  'kat  V.S.8$.
np.  Jäm  'Glas,  Becher'.  Wgh  yama-.  —  Pü. : xumbai  ape  yämii  palin,  erl. ;  däsht  (?)  karän  \ vgl.  Darabs  Bemerkung  dazu.
•  p.  yävä  Adv.  'so  lang  als',  mit  Konj.: yadiy  imäm  dipim  vainaky  .  .  ulSmaiy  y' taumä  ahatiy  pankarahidis  ",  .  so  Sang die  Kraft  dazu  vorhanden  ist . ."  Bh.  .^  16; 1 7.        a)  mit  dem  Korr.  ^ävä:  y  *taum3
•  ahatiy ''  *ävä  avaiy  parikarä   Bh.  4.1$.
Vgl.  fti.  yavani-  Adj.;  S  4i6^  No.  4.  —  0  So richtig  gegen  NA.  For  KZ.  jj.  47.  Doch s.  zu  toHtnan-  No.  I.
•  j.  yi-varana-"  Adj.  (fem.  °«5-)  'welchen Glauben  habend,  wes  Glaubens':  °«a" ups  °nä''>  urvarä  'na  g3uf  .  .  'nS  ahurS mazda  .  .  °nS  at  tara^tdtrs  'nS  kavS vlUäspg  'n<J  (NDm.)  faraiaosirä  jämaipa 'nB  kascU  saofyantam  . .  tä  varynä{sA.y3  . . Y.  12.  7.
Pü. :  i-a«  iämai  ät,  i  äp  (usw.).  —  ')  NA.  hat die  drei  ersten  Male  ya.var',  s.  aber  Var.  — »)  Man  erwartet  'n3  (NPf.).
•  j.  y^varvna-  n.  'Stössel'  (des  Mörsers): yai^qm  zayanqm  vastrytke  fsityantU  . .  °mm zgfTfsnö.va-fiarum  ". .  ein  StÖssel  mit  rund- lichem Kop&tUck"  V. /4. 10.
Man  erwartete  *yavärina;  all  Komp.  au«  yma- +*ar3iia-  n.,  eig.  Instrament  zum  Mahlen des  Getreides';  ■.  zn1izJa-undGIrFh./.3ti[. — np. yävar, yär.  — Pfi. :  iur/öt  1  ör/'gemahlenei Getreide'i    erLi    äiyäi  i  fa  datt  '«ine  Hand*
db,Google
isS;  yär-  —  yäs-  mit  a  1188
•  j.  (,  P->  yäi-  n.  'Jahr"':  tai^a  ayar>  Gottheiten  der  sechs  Jahreszeiten  und  der mait^UJiU yai  'n  'Sind  die  halten  für  eben  jeweils  am  Ende  gefeierten  fünMgigen Tag,  was  ein  Jahr  (ist)"  V.  2.41;  —  •«  Jahresfeste*':  'ya  (AP.)  aiavana  aiahe aar/ J^3Mff^raJU(sd.)  tj'atll'V.S.46V}iZ.;  ratavS  Y,  2.  9;   17,  Vr.  2.  2;  —   'yaültyS
—  tar8  'n  V.j.jö,  Ä33;  —  ramats  o/aAe mäifyffY.  1.^,^1. 1.2;  —  rahnam.. (sd.)  tarS  */7  V.p,46;  —  na^iuM  'n  "ein   'yanqmca  sar^nqmia  Y./.17.
halbes  Jahr  lang"  N,45'  *44''  ^^z"  *4[3'''        **  ''^'"   Nsunen    finden   nch   i.  B.  Vr.  /.  3,
„,'  n  11  .  .  .  ••e-"      •--  liehe)  Feste,  wie  FnihUiiE»-,  Mittsommer-,  Enile-
das    erste   Halbjahr    oder    das   zwate  f^,,,  werden  rie  ipiter  dem  Andenken  u  die
N.44;  — ._>rii  *yä  (als  GS.!)^  "dreimal  einielnen   Abschnitte   der   Schöpfong   geweihL
des  Jahis"  IN.^;  —  hatannm  'nmCf)  VgL  Bd.  25.  iE;  Roth  ZDMG.  54.698,  G«, Yyf  ^                                                                         '  OK.  320,  DsT.  ZA.  A  36,  j.  iSo  nnd  ontei  den
Vr^      iLL.j  .11  einzelnen   Nunen;    ferner  Vdllexs  Fiaemenlc
*)   Dm  J«hT  bestand  ans- 13  Monaten  in  30  ,,     ^b   fn.^.   ,  r-    ,,«    v   -  ,    7n\ir
nud  reste  s.  unter  j-aj^ra-,  Zn  den  Namen  der        .  -,   ,       .>-^    -  -  i-      ^ Monate  %.  nnter  mÄ*-;   die  der  Tage  e^eben       ""^'  <"  *'=  gaitntar.
"t<^^;E;  AbldL  -  goLyV^.  -Txu:  .äK- ■'  >•  &  S^»*  ^-  '^^"^  °^  "■  verfangen'.
1)  Hds.  yi,  —   »  Hds.  jra;  aber  Fa.:  ji/.  —    P'aes.  2  j^dJ«-.
9  Wie  iD  lesen?    Fö.:  j  tir  imdar  säl  i)  'etwas  verlangen,  wonach  Verlangen
.  j.  ylp..£ar»i-  Adj.  'amun.  liahens,  ein  "^"^  '^'T"  ™  ""^K»  sl^«:  bfetn Jalii  hin-,  m  Ende  bringend,  dem  ^i.  I  ""-■,  mit  Akt  der  Sache:  Om  v^^m Jahr  zn  Ende  gehf:  «Ä?»  . .  «V«  -H,  >'"'"''•  "■"»fl'  i«e»>  gnten  Lohn  nag (GS.)  «.««rf.»..  ^r,!:rM>m  'Uifl,.sMi.'f^  Verlangen    Y.j;  21;  -  m«/^J<..
(wieder)  i
ZornV.  I:  ,  
im  Ablaut  mit  (./ä«Ä)«ari- (mit  idg./-).  Es  Vum    urvästtnä  {fA.)   V.^2.l;  —  ahjS  yStä  .
```


## [2026-09-06T15:14:47.830Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r\"Yauna- adj\",l):\n        print('LEAF',i,'printed ~',i-15)\n        m=re.search(r\"Yauna- adj\",l)\n        print(l[max(0,m.start()-300):m.start()+900])\n        break\n# also yāna\nfor i,l in enumerate(leaves):\n    for m in re.finditer(r\"y[aā]na-? *sb|yānam|yana- sb\", l):\n        print('=== yana LEAF',i,'printed ~',i-15)\n        print(l[max(0,m.start()-300):m.start()+600])\nEOF"
}
```


### [2026-09-06T15:14:49.454Z] TOOL RESULT

```
LEAF 228 printed ~ 213
ifference in the present stem (Av. yüióyeiti, Skt. yüdhyati; JAOS 58.116).  ayauda imf. (5213) XPh 31f (not dyauda пзш. ‘rebellion’, as taken by Henning, BSOS 10.505, which is refuted by Akk. version). ayauda" 3d pl. imf. (5232.П) DSe 33°. yau[da*- tim] asf. pres. pte. act. ($190.1, $240) DNa 32.
| Yauna- adj. 'Ionian'; pl., also a province of
the Persian Empire; mase. sg. as sb., ‘Ionia’, а province: Elam. (2)-a-u-na, Akk. ja-ma-nu, Gk. Tovia.
(1) ‘Ionian’: Yauna nsm. A?P 26. Yaund npm. DSf 33f, 48; as nam. (556.1) А?Р 23.
(2) ‘Ionians’, as province: Yauná npm. DPe 12{; DNa 29; DSe 271°; DSm 10°; XPh 23.
(3) ‘Tonia’: Yauna nsm. DB 1.15; DNa 28; DSm 8°. Yaund absm. DSf 42.
yaumant- adj. ‘trained, skilled’: adj. to *yauman-, with vriddhi (5126, $152.T, ў}155.Ш), from root seen in Skt. уйин ‘harnesses, fastens’, ef. Hz. ApI 365-6 (not with Sen 249, ‘agile’, from *yduman-aina-, fem. -2). See also ayáu- mani-.  yüumainii пзш. (with epenthesis, $127; Lg. 15.173) DNb 40.
уашлуй- sb. ‘canal’ (§48): NPers. Joi ^water- course, canal’, cf. perhaps Skt. (Vedic) yavyd isf. ‘stream, river’; perhaps deriv. (§144.V) of root ay-/i-/yà- ‘go’ (JAOS 62.271). yauviyd nsf. DZe 10. yaunydm asf. Оле 8f, 
=== yana LEAF 219 printed ~ 204
 See also dumlaparanam. — paranam asn. as adv. ‘formerly’ DB 1.51, D'Sb 3.
pariy prep. and prefix ‘around, about’: Av. pairi, Skt. pári, Gk. тері, Lt. per ‘through’, pIE *peri ($64, §75.1, $113, §140.1). Prep. with aec. ‘about’ DB 1.54. Prefix-with ay-, bar-; ef. also pariyana-.
196 OLD PERSIAN
pariyana- sb. ‘superiority’: deriv. ($147.IT) of pariy, in meaning seen in Ау. pairi ‘vorne, über ... hin’, Skt. pári as prefix ‘much, excessively’, cf. Gk. meptoads ‘excessive’ (otherwise Hz. ApI 273, Sen 250). pariyanam nsn. DNb 52.
paru- adj. ‘much, many’: Av. pouru-, Skt. purú-, Gk. modts, Gt. filu, pIE *palu- (§63.1, $107). See also paruzana-. рати) nsm. ($114, $127, $140.I) DB 449; DSf 56 bis. pariindm gpm. DSi 4, 5; DE 9, 10; XPa 5 bis; XPb 9, 10; XPc 4f, 5; XPd 6f, 7f; XPf 6, 7; XPh 5, 6; XE 9f, 11; XV 7,8; А:Ра 7°, 8°; А°Нс 6 bis. parünàm gpf. DPe 4. parüenüm ($28.П) gpm. DNa 6, 7; DSe 6,
```


## [2026-09-06T15:14:57.230Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(224,231):\n    hdrs=re.findall(r\"\\n?\\s*(\\d{3})\\s+OLD PERSIAN|OLD PERSIAN\\s+(\\d{3})|LEXICON\\s+(\\d{3})|(\\d{3})\\s+LEXICON\", leaves[i])\n    print(i, hdrs, leaves[i][:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:14:58.692Z] TOOL RESULT

```
224 [] 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54
225 [('202', '', '', '')] BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2
226 [] 24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] 
227 [('', '', '203', '')] ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1
228 [] so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a provi
229 [] d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; 
230 [] am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71
```


## [2026-09-06T15:15:07.819Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && for f in BQT_v4_pages.txt BQT_v5_pages.txt; do echo \"=== $f\"; grep -n \"یونان\" $f | head -10; done"
}
```


### [2026-09-06T15:15:09.478Z] TOOL RESULT

```
=== BQT_v4_pages.txt
870:در هم آمیخته را کوبند ؛ و باین معنی با سین | بنفش رنه دارد و بآخرنخم کرد وآنرا ییونانی
1093:‎٩‏ - یونانی 336185 ( سیاء ) « اختینگای ». ۰ رد : مالیخولیا +
3121:۵ مروارید - بنم اول پپلوی 130۳۷2۴14 «تاوادیا۱۹۴* ۰ ازیونانی 228780251185
3142:و منصب لو یافتن و ترقی دز احوال بهم رسیدن | حطی . لغتی است.یونانی بممتی مرزنگوش وآن
3224:۴ - از یونانی ۸]۵۳1۵00۱1100 > عاازباه۴ - 6اه (فر) « دزی ج؟ ۹۸۹ >
3614:رد0٩‏ < ع17صعه 6ل 62و02 ( از یونانی ۳۵۵18 ) < ۷۵۲۲۵ عل 500008 ( فر )
4247:نقطةٌ زده » بلفت رومی و بحی کونند بیونانی | اسبر ازآن بهم میرسد واصبر دوائیت معروف.
4264:تصرف یونان » بو کوسلاوی و بلغاری است . - مصحف « فیلفوی > . رك : فیلقوی .
4267:و اسم ذلك النبات بالمربية المقر » و بالیونانی الوی .» «* عقار ۳۱۸ * ۰ بونانی 2[08 * 5غ810
4549:۱ - همین صورت‌اخی رسحیح بنظرمیآ ید - ملغم وملفمه عربی‌ظاهرا ازیونانی 13281287708
=== BQT_v5_pages.txt
1609:قدری اصل کلمه باختلاف : یونانی درن‌پویم ( دئیس » قاضی ) » عیلامی
2064:صفحلا ‎٩۶‏ , ستون ۱ سطر ۲۲ » آرامونی ت اظ ۰ مصحف‌دا نامونی»یونانی
2120:موْمن) » آزیونانی 8۳8011:08 * فر- 8۳86010 +
2399:صفح۱۳۲۹, ستون۲ سطر ۰۱ اسقور دیون-معرب‌لاتینی 8007100 آزیونانی
2402:سطر ۰۸ اسقورون- معرب یونانی 916718 (کاهش » کسر » نقص) قس.
2557:سطر ۲۴ .انالیقی - محرف«اکالیفی»یونانی 8۳81010 (فرهنگ ا نگلیسی
2636:سطر ۷۵ » اورمالی - معرب یونانی 618107011 ( جزو اول درمنعاة +
2639:دوغن‌و جزو دوم ۰۳:61 عسل ) ( فرهنگه انگلیسی - یونانی وودهوز ) ؛
3743:از یونانی هطع؟ 07ج .
6331:مینوان پكلمةٌ یونانی 10961086408 ترجمه کرد د« نولدکه . حماسة" ملی
```


## [2026-09-06T15:15:10.338Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN/HUB yunan\"; grep -n -i \"junan\\|jûnân\\|Ионан\\|Yūnān\" HRN.txt HUB.txt | head; echo \"== FVQ (Jeffery) yunan/hanan\"; grep -n -i \"Yūnān\\|Yaḥyā\\|Yahya\\|Yuhanna\" FVQ.txt | head -20"
}
```


### [2026-09-06T15:15:10.405Z] TOOL RESULT

```
== HRN/HUB yunan
== FVQ (Jeffery) yunan/hanan
9612:but there seems reason to believe that this form, like Yahya for 
9627:else, but its elose connection there with the name Yahya would seem to indicate that
```


## [2026-09-06T15:15:21.062Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('v4 leaves',len(leaves))\nimport re\nfor i in range(len(leaves)-12,len(leaves)):\n    print('---LEAF',i, leaves[i][:200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:15:22.815Z] TOOL RESULT

```
v4 leaves 553
---LEAF 541 [pdf page 542] متنها بویان وولاخ « بالام بر وزن سوراخ , مان | ولون را هم‌گفته اند هنچو آتریون که پسمتی سراب وبیآب ودور از آپادانی را گویند. آذ رگون است بمنی آش‌رنگه؟۴ . وت « بنم اول وسکون ثانی و نون »
---LEAF 542 [pdf page 543] بودن در دهان ماهی شدن - 4۹ ونام‌پدرلنطی‌هم هست که بوتان منسوب‌باوست ۱ کنابه ازرفتن روز وآمدن شب باشد؟۴ .+  بونی دردهان ماهی‌شدن- ۱  بیان نوزدهم در بای حطی با های هوز مشتمل برسه لغت  فها
---LEAF 543 [pdf page 544] از کناب برهان قاطع در لغات متفرقه محتری بر فتاد و بيِك لفت و کنایت آذاراقی۱ - بفتح اول وذال نقطه‌دار | تحمل کردن وگذرانیدن حرف پهلودار باشد از و رای بی‌قطه هردو بالف کشیده وقاف بتحتانی 
---LEAF 544 [pdf page 545] 3 << که عولم تاتوله خوانند . خوردن قدری از آن | وآن برج سیم است ازجملةٌ دوازده برج فلك . متی‌آرد" . چچ" - بنتح جیم فارسی وسکون جیم ام - بفتح اول و سکون میم . معروف ۱ ابجد: طبقی‌باشد که 
---LEAF 545 [pdf page 546] -۳)- زوم وکا هردو فارسی, خلریشت را گوبند . رضو ان گده «کنابه ازبپدت عنبر حشرما! - بنتم‌حای‌بی‌ضله ونای‌منلله | سرشت است . وسکون رای بی‌نقطه ومیم بالف کشیده. نوی از رعنای صاحب بر بط «کنا
---LEAF 546 [pdf page 547] وک - 4۹4 نک کت آن درخت است. ومعنی تبیدن باشد که حر کت کردن و برجستن  وال" - با زا وعاف هردوفارسی, بر | است مراعضای آدمی وحیوانات دیگررا بونکام وزن وممثی ژفال است که انگشت باشد . کفتن . 
---LEAF 547 [pdf page 548] و1 تم ۰ بر ابو خینپند بر که آن است. که برزبانها ومیان‌مردم افتاده باشد لیکن‌بمنوان پا" - بنتح غین ضطهرار وبای‌فارسی | سرکوشی وخفیه بهمکوبند . وسکونکاف, گیاهی است که ازآن حسیر وبوریا فحل
---LEAF 548 [pdf page 549] قیل و۹4۹ ومیم» پنبه را گوبند وعربان قطن خوانند . رطوبت که بردست می‌پیچد (۱) ومیوء آن گرد قعبل! - بنتح قاف وسکون‌عینی‌نقطه الا فتحکاف وغین نقطه دار دبای ابید مقتوح بل زدد + کیاطیاست ددان
---LEAF 549 [pdf page 550] دنه سم لهت! « بفتح لام بروزن مست. بمعنی | کردن یعنی پراکنده وپریشان مکن . خوب ولیکو باشد - وهرچیزقویرا نی زگویند . نچات؟ - بفتح‌نون وجیم فارسی‌وسکون لصف؟ < بفتح لام وصادبی نقطه‌وسکون کا
---LEAF 550 [pdf page 551] ساره م۲1۹۸  نقطه وفای بتحتانی کشیده » نوعی ازبیالةٌ شراب نظار گبی* - بنتم نون وظای نقطه‌دار باشد۱ - واسطرلاب سفی‌را هم میگویند « آن | معدد بالف کشیده و رای بی‌قطه مفتوح و کاق اسطرلایی ب
---LEAF 551 [pdf page 552] تسمشنها قوب وغرچند آنوشیروان ازاوخواست که بقیمت (۱) | وعلم برپای کردن وراست سودن‌را دز گفته‌اتد ؛ اعلی بخزد او لفروخت. هرگاه چیزبرا برزمین بیفکنی وآن چیز راست وفنو رد۱ - بفتح واو وسکون‌
---LEAF 552 [pdf page 553] ما۵۵ ۵ -9طع جومعم‌زا #حصسم ۸ 2 046 3 پچ ۳ 6 ع. 80۴۲۸۵۸۲ ۳۴۲۹۸۸۷۶ ۸۸۵۷۶ ها ۵۶ ۵۵7/۵۸۸۸۸۲۶ ) 9 6عل عع۵۷ عف از ۵۱ وف 3 .۲00۵ 6۱۲6601 8۵000 ۸ ۲ ۸۷۵۳۰ سقتج 0۶ ۱۷۲۶ ۸ ۲۵۲۵:۳ ۷۷0۲۰4:۹۷ 71۴71 ۱
```


## [2026-09-06T15:15:35.757Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nimport re\nfor i,l in enumerate(leaves):\n    if i<520: continue\n    for m in re.finditer('یونان', l):\n        print('LEAF',i, l[max(0,m.start()-250):m.start()+250].replace('\\n',' '))\n        print('--')\nEOF"
}
```


### [2026-09-06T15:15:37.383Z] TOOL RESULT

```
LEAF 541 وران » دم بمعنی‌فلس وفلوی‌باشد۱ - ونمدوتمد زین‌را نیز | ولاتی است که اکثر حکما ازآن ولابت بودماند کوبند۳ - ونام رودخانه‌ای‌هم هست؟* - ورنکه | وسکندر آب درآن انداخت و خراب کرد - << ۳<۳ ی - جهانگیری برای این معتی دو بیت ذیل را شاهد آورده : فلسفی‌فلسی ویونانی همه پولی ارزد نفی‌این‌مذهب بوتان بخراسان پایم- (خاقانی شرْوانی . دیوان س۳۰۰). با اس حدیت و نظم اقرآن پولی نرزد حدیت پونان . (خاقانی. تحفقالعراقین چاپ قریب سه٩).‏ درشر ح خافانی بون بمعنی «دانگه» آمده «فرهنکه نظام» رشیدی گوبد: «یون, نمد زین (ر3 
--
LEAF 541  ) مبنامند و آن ناحیتی است در آسیای صفیر» بین ملطیه وف وکیه یمنی بین‌خلیج ازمیر کنونی درشمال ومتدلیه «رجنوب. چون ایرانیان تین بار بلاین طایفه ازهلن‌ها رویروشدند ومدت درازی/بونیه متعمرءٌ ایران بشمارمیرفت (درزمان هغامتشیان) آزینرو همه تواحی هلن‌ها را «یونان» نامیدندء چنانکه پونادٍان نيزهمةٌ نواحی ایران را بمناسبت نام قوم پاری, ۳6۳818خواندند. پونان را یونانیان - ۳361188. فراسوبان31806) وانگلیسیان 6 وآلمانیان 0716010681280 مینامند. یودان یکی‌از ممالك شبه جزیرة بالکان لست که ازجهت مشرق‌بدربای اژه با 
--
LEAF 541 «رجنوب. چون ایرانیان تین بار بلاین طایفه ازهلن‌ها رویروشدند ومدت درازی/بونیه متعمرءٌ ایران بشمارمیرفت (درزمان هغامتشیان) آزینرو همه تواحی هلن‌ها را «یونان» نامیدندء چنانکه پونادٍان نيزهمةٌ نواحی ایران را بمناسبت نام قوم پاری, ۳6۳818خواندند. پونان را یونانیان - ۳361188. فراسوبان31806) وانگلیسیان 6 وآلمانیان 0716010681280 مینامند. یودان یکی‌از ممالك شبه جزیرة بالکان لست که ازجهت مشرق‌بدربای اژه با مجمع‌الجزابر؛ ازجنوب یبحرالروم (مدترانه) » ازمقرب‌پدربای ایونی وازشمال ببلفارستان» بو کوسلاوی وآلبانی
--
LEAF 548 * - بنم لام و سکون حای گوبند . ی ۱ بی‌نقطه» بروزن و جعنی لعبتان است که صورت گصنیئون ‌- بفتح کاف وسکون‌صاد بازيچهة دخترکان باش د که از پارچه سازید. بی‌نقطه ونون‌مفتوح بتحتانی‌زده وئای‌مثلئه‌مضموم لذروه - بنتس‌لام وسکون دالبی نقطه وواوونون؛ هردوسا کن بیونانی‌بادنجان صحرائیرا وضم رای قرشت وواو مفتوح, نام قلعه ایست در کوبند. ساق آن‌باريك میباشد وبمرتبةٌ صاحب | هندوستان۹ . سس گ_-_-_-_-_-_-_-<--<-<<<<<م<<<<<<<<<<م ‏ مه ی  () خم۱: می‌چسید. () چك, چش: شکفت .  ۱ - «قعبل تزدیتی ازاقسام فطر است. ونزد بسنی 
--
```


## [2026-09-06T15:15:50.370Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\ntxt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=txt.split('\\f')\nl=leaves[541]\ni=l.find('مبنامند و آن ناحیتی')\nprint(l[max(0,i-1500):i+300])\nEOF"
}
```


### [2026-09-06T15:15:52.223Z] TOOL RESULT

```
» با نون بر وزن نوران » دم
بمعنی‌فلس وفلوی‌باشد۱ - ونمدوتمد زین‌را نیز | ولاتی است که اکثر حکما ازآن ولابت بودماند
کوبند۳ - ونام رودخانه‌ای‌هم هست؟* - ورنکه | وسکندر آب درآن انداخت و خراب کرد -
<< ۳<۳ ی
- جهانگیری برای این معتی دو بیت ذیل را شاهد آورده :
فلسفی‌فلسی ویونانی همه پولی ارزد نفی‌این‌مذهب بوتان بخراسان پایم-
(خاقانی شرْوانی . دیوان س۳۰۰).
با اس حدیت و نظم اقرآن پولی نرزد حدیت پونان .
(خاقانی. تحفقالعراقین چاپ قریب سه٩).‏
درشر ح خافانی بون بمعنی «دانگه» آمده «فرهنکه نظام» رشیدی گوبد: «یون, نمد زین (ر3 :
ممنی دوم) وکاهی بممنی مطلق پشم نیز کوبند. قطران (تیریزی) کوید :
چو پربالای میمون‌او. برزم آندرنپد بون او بود فرخ فربدون او » عدو شحاك شوم‌اختر.
وخاقانی گوید: با نص وحدیث...؟ درون‌سورت درهردو شعرخافالی معنی پشم درست است نه فلس
«فرهتگه نظام» ر4: حاشية بعد . ۴ - «یون غاشیه بود. مجلدی (کی‌کانی) کوید :
رکب غزو ورا,کسوه ملّی زیید زین پردة خان خطا زین ورا زیید بون >
«لغت فری س4*۳ -
*بون, لمدزین باشد. عنصری (بلخی) کوید :
از فتح و اظفن بینم بر لیزم نو عقد وز فر وهذی بینم بر دیزة لو ون -
هم عنصری کوید :
هیون چو جنگه برآورد وبون فکند براو بگوش جنگ نماید همی خیال دوال .>
«لفت قرس س۴4*۳ ۰
درصحاح‌الفری (نسخة طاعتی) آمده: یون: نمدزین باشد.» وبیت «ازفتح وظفر...۶ را بنام عماره
شاهد آورده است . ۴ - «کازرون بنزديك دریای بوست» «حدودالعالم ص۴۷۸ ۰

۴ کون (م.م.) . قسی: آذریون, همایون . * - از: بون ۲ آن (پموسکان
با جمع) . بون 108 (پارسی باستان 98088) یکی از طواب بز رکه هلن, که نام خود را از
8 » پر 0۳61386 و۸001108 گرفته. منوب بدان 18865 «مرچنت» ومسکن این قوم
را 10812 ۱ مرچنت » ( 10816 فر ) مبنامند و آن ناحیتی است در آسیای صفیر» بین ملطیه
وف وکیه یمنی بین‌خلیج ازمیر کنونی درشمال ومتدلیه «رجنوب. چون ایرانیان تین بار بلاین
طایفه ازهلن‌ها رویروشدند ومدت درازی/بونیه متعمرءٌ ایران بشمارمیرفت (درزمان هغامتشیان)
آزینرو همه تواحی هلن‌ها را «یونان» نامیدندء چنانکه پونادٍان نيزهمةٌ نواحی ایران ر
```


## [2026-09-06T15:16:05.328Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:16:05.337Z] TOOL RESULT

```


```


## [2026-09-06T15:16:07.701Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON یحیی\"; grep -n \"یحیی\" MON_part1.txt MON_part2.txt | head -5; echo \"== ARY\"; grep -n \"یونان\\|حنان\" incoming/ARY/ARY_pages.txt | head -8; echo \"== FVQ hanan/Yahya ctx\"; sed -n '9605,9635p' FVQ.txt"
}
```


### [2026-09-06T15:16:07.777Z] TOOL RESULT

```
== MON یحیی
MON_part1.txt:597:دانشنامه ‏ دانشنامه علائی قریب (عبدالعظیم و دکتر یحیی) 
== ARY
28:شترکك» واژه‌های همريشه در زبان‌های سانسکریت و ارمنی و یونانی ولاتین و آلمانی و انگلیسی و
205:هندی» اسلاوی» بالتیکه) و زبانهای سنتم 4 (ژرمنی» لاتین» یونانی» سلنیک). در زبانهای
217:به‌جلگه‌ی تارم (باختر چین) کوج کردند و علت شباهت زبان آنها با یونانی و سلتی همین است؛ آیا به
517:است: از یونانی کامل‌تر و از لاتین پرواژه‌تر و از هر دو به طور چشم‌گیری پالوده‌تر
544:باید به طور علمی و سامانمند بررسی و اثبات گردد. مثلاً آوای یونانی 2۳3 برابر است با آوای ژرمنی
545:8 چون واژه‌ی «بردن؛ در بونانی ۳۳180 و در انگلیسی 81۸14 است. واژه‌ی «برادر» در یونانی
547:نتیجه گرفت که طبق این اصل (یونانی 217 < ژرمنی 8). واژه‌ی یونانی ۳18005 (به معنی درخت
560:واژه‌ی بنیادین را احیاکرد. مثلاً پس از تعبین برابرهای واژه‌ی «زمین» (سانسکریت: 4۵7۸8 یونانی؛ . ,
== FVQ hanan/Yahya ctx
course on Protevanyelion, viii, 4. ^ ^ ^ 

There are variant spellings of the word, . u j j ; u j j and ( j j 

(Tab. on iii, 32), and the early authorities recognized the name as 
foreign, al-Jawallqi, Mu'arrab, 77. 5 The probabilities seem to be that 
it came into Ar. from Syr. Vp1. 6 We find fcOISKT in Mandaean, 7 
but there seems reason to believe that this form, like Yahya for 
Yohanna, has been influenced by Arabic (Brandt, JiRM, viii, 380). 
The name apparently does not occur in the early literature, 8 though 
it must have been well known to Arabian Christians in pre-Islamic 
times. 

1 Vullers, Lex, li, 168, 169. 

2 Addai Slier, 77, also argues for a Persian origin, but he wants to derive it from 

->ljJ meaning yellow water. 

3 80 Kraenkrf, op. eit. 

4 It is remotely possible that in the list of Prophets in vi, 85, it refers to someone 
else, but its elose connection there with the name Yahya would seem to indicate that 
the same Zachariah is meant as is mentioned in the other passages. 

8 So al-KhafajT, 99. 

Rhodokanakis, WZKM, xvii, 285; Horovitz, KU, 113; Mingatm, Kyriac, 
Influence, 82. 

7 As in the Liber Adami (ed. Norbcrg), and Qinzn (tr. Lidzbarski), 51, 213, 219.
```


## [2026-09-06T15:16:11.345Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Yahya\" FVQ.txt | head -20"
}
```


### [2026-09-06T15:16:11.395Z] TOOL RESULT

```
9612:but there seems reason to believe that this form, like Yahya for 
9627:else, but its elose connection there with the name Yahya would seem to indicate that
```


## [2026-09-06T15:16:16.424Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"yohanan\\|johanan\\|Yuhanna\\|Yohanna\\|Iohannes\" FVQ.txt | head -20; echo \"=== KLN Joab\"; python3 -c \"\nimport re\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'Joab,',t); print(t[m.start()-100:m.start()+700])\""
}
```


### [2026-09-06T15:16:18.438Z] TOOL RESULT

```
9613:Yohanna, has been influenced by Arabic (Brandt, JiRM, viii, 380). 
=== KLN Joab
or father. 
Cp. the first element in Abraham, Abner, Absa- 
lom, Abigail, and the second element in Joab, 
Moab, Barabbas. Cp. also abbot and words 
there referred to. Cp. also borage, 
abound, intr. v. — ME. abounden , fr. OF. (— F.) 
abonder , fr. L. abundare, ‘to overflow; to a- 
bound’, fr. ab- and unda, ‘wave’. See undate and 
cp. redound, surround. Derivatives: abound-er, 
n., abound- ing , adj., abound-ing-ly, adv. 
about, adv. — ME. abuten, abouten , aboute , fr. 
OE. abutan, onbutan, ‘on the outside of’, formed 
fr. a-, ‘on’, and butan, ‘outside’, which itself is 
formed fr. be, ‘by’, and utan, ‘outside’, fr. ut, 
‘out’. See by and out and cp. but. 

Derivative: about . oren. 

above, adv. — ME. aboven ; fr. OE. abufan , form- 
ed fr. a-, ‘on’, and bufan, ‘above’, which itself 
is
```


## [2026-09-06T15:16:28.407Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D9%86%D9%86",
 "prompt": "Give the Arabic root ح ن ن entry: the root meaning, derived terms (حنان، حنّان، حنين، حنانة), and any note on Semitic cognates (Hebrew חנן)."
}
```


## [2026-09-06T15:16:30.270Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82",
 "prompt": "Give the full etymology of Ancient/Koine Greek Ἰωάννης — from Hebrew יוֹחָנָן, meaning, and descendants (Latin Iohannes etc.)."
}
```


### [2026-09-06T15:16:30.343Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:16:36.477Z] TOOL RESULT

```
# Etymology of Ἰωάννης (Iōánnēs)

**Origin:** The name derives from Biblical Hebrew יוֹחָנָן (Yōḥānān), meaning "God is gracious" or "Yahweh is gracious."

**Path:** According to the Wiktionary source, it entered Greek as "a learned borrowing from Koine Greek," becoming Ἰωάννης. The modern Greek form Ιωάννης maintains this classical lineage.

**Latin and Romance Descendants:** The name passed into Latin as **Iohannes**, which subsequently generated numerous European forms:
- English: John, Ian, Iain
- Romance languages: Jean (French), Juan (Spanish), Giovanni (Italian), João (Portuguese)
- Germanic languages: Johann, Johan, Hans
- Slavic languages: Ivan, Jan

**Modern Greek Variants:** The page notes that Ιωάννης has an informal doublet, Γιάννης (Giánnis), and a feminine form, Ιωάννα (Ioánna).

The name remains significant in Christian tradition, associated with biblical figures like John the Apostle and John the Baptist, and celebrates saints in the Greek Orthodox tradition on January 7.
```


## [2026-09-06T15:16:39.440Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D9%86%D8%A7%D9%86",
 "prompt": "Give the Arabic and Persian entries for حنان: etymology (root ح ن ن), meaning, and whether Persian حنان is marked as an Arabic borrowing."
}
```


## [2026-09-06T15:16:41.101Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D9%88%D9%86%D8%A7%D9%86",
 "prompt": "Give the Persian entry یونان: etymology (Old Persian Yauna, Greek Ionia), meaning Greece, and any Arabic يونان entry."
}
```


### [2026-09-06T15:16:44.918Z] TOOL RESULT

```
# حنان (Ḥanān) - Arabic Entry

**Root:** ح ن ن (ḥ n n)

**Meanings:**
1. Verbal noun of ḥanna (Form I)
2. "mercy, kindness, affection"
3. "tenderness"
4. "compassion"

**Pronunciation:** /ħa.naːn/

**Grammar:** Masculine noun, triptote declension

---

# Persian Entry Status

The webpage indicates that "حنان" has entries across 6 languages including Persian (فارسی), with a link to the Persian Wiktionary version. However, **the provided content does not include the actual Persian entry details or specify whether it is marked as an Arabic borrowing.** The page only shows the English Wiktionary's Arabic section.

To answer your question about Persian etymology marking, you would need to access the Persian Wiktionary directly via the provided link.
```


### [2026-09-06T15:16:45.135Z] TOOL RESULT

```
# Persian Entry: یونان

**Etymology:** The word derives from Old Persian _𐎹𐎢𐎴_ (Yauna), which itself comes from Ancient Greek _Ἰωνία_ (Iōnía), meaning "Ionia."

**Meaning:** یونان refers to Greece, a country located in Southeastern Europe.

**Arabic Entry:** The page references an Arabic descendant: اليونان (al-yūnān), which is the Arabic form of the same word meaning Greece.
```


## [2026-09-06T15:16:51.068Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%8A%D8%AD%D9%8A%D9%89",
 "prompt": "Give the Arabic entry يحيى: etymology (relation to Hebrew יוֹחָנָן / Syriac ܝܘܚܢܢ, John the Baptist), and any competing derivation from Arabic حيي \"to live\"."
}
```


## [2026-09-06T15:16:53.052Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%B8%CF%89%CE%BD%CE%AF%CE%B1",
 "prompt": "Give the etymology of Ancient Greek Ἰωνία and Ἴων (Ion) — origin of the tribal name, Hebrew Yāwān, Old Persian Yauna, and whether it is connected to Ἰωάννης."
}
```


### [2026-09-06T15:16:57.919Z] TOOL RESULT

```
# Etymology of يحيى (Yahya)

## Primary Etymology
The origin of يحيى remains uncertain. It diverges notably from the Hebrew יוֹחָנָן (Yōḥānān, "Yahweh is gracious") and Syriac Yuḥannā, despite all three referring to John the Baptist.

## Traditional Islamic Explanation
Muslim scholars traditionally connect يَحْيَى to the Arabic root حيي, relating it to "to live" or "he is alive," suggesting a meaning tied to vitality rather than divine graciousness.

## Alternative Scholarly Theory
Some scholars propose a scribal misreading explanation. In early unvocalized Arabic script (rasm), the forms Yuḥannā and Yaḥyā would look identical visually: "the _nūn_ and the _yāʾ_ letters look identical in their rasm medial forms." This suggests inadvertent substitution during transcription.

## Epigraphic Evidence
A 306 CE inscription from al-Ula contains Yḥya in Nabataean script, indicating the name existed in pre-Islamic Arabia. Scholars debate whether this supports either the phono-semantic matching theory (equating existing Arabic names with foreign ones based on sound similarity) or demonstrates independent Arabic origins.
```


### [2026-09-06T15:16:59.829Z] TOOL RESULT

```
# Etymology of Ἰωνία and Ἴων

Based on the Wiktionary entry provided, here's what can be established:

## Direct Etymology

The article states: "From _Ἴων_ (Íōn, 'Ionian') +‎ _-ῐ́ᾱ_ (-ĭ́ā)." This shows that Ionia is formed by combining the root referring to Ionians with a feminine territorial suffix.

## Connection to Other Languages

The entry notes a comparative form: "Compare Egyptian _ywnj-ꜥꜣ_ ('Great Ionia')" with hieroglyphic transcription, suggesting the term was recognized and borrowed by Egyptian speakers.

The **Descendants section** shows how the Greek term spread to other languages, including Latin (Iōnia), Persian (yunân), and Turkish (İyonya).

## Limitations of Source Material

The provided Wiktionary page does **not address**:
- The ultimate origin of the tribal name Ἴων itself
- Connections to Hebrew Yāwān or Old Persian Yauna
- Any relationship to Ἰωάννης (John)

To answer these questions comprehensively would require additional scholarly sources beyond this dictionary entry.
```


## [2026-09-06T15:17:04.658Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%B8%CF%89%CE%BD",
 "prompt": "Etymology of Ancient Greek Ἴων (Ion, Ionian) — pre-Greek origin? Mycenaean iawone? relation to Hebrew יָוָן Yāwān, Old Persian Yauna, Sanskrit Yavana."
}
```


## [2026-09-06T15:17:05.669Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/John",
 "prompt": "Give the etymology of the name John (Medieval Latin Johannes, Late Latin Joannes, Greek Ioannes, Hebrew Yohanan) and any note on Jane/Joan/Ivan."
}
```


### [2026-09-06T15:17:06.949Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:17:13.316Z] TOOL RESULT

```
# Etymology of John

**Etymology Chain:**
The name John traces back through multiple languages: Medieval Latin *Johannes* → Late Latin *Joannes* → Greek *Ioannes* → Hebrew *Yohanan* (longer form *y'hohanan*).

**Original Meaning:**
According to the source, the Hebrew root is "said to mean literally 'Jehovah has favored' or 'Jah is gracious,' from *hanan* 'he was gracious.'"

**Related Forms:**
- **Jane/Joan:** These are feminine variants derived from the same Latin root
- **Ivan:** The Russian form of John, which also stems from the Latin *Johannes*

**Historical Note:**
The Greek adaptation modified the Hebrew ending to conform to Greek conventions. English speakers later inserted the "-h-" in imitation of the Medieval Latin form. The name became extremely popular in Christian cultures due to John the Baptist and John the Evangelist, eventually becoming used generically and as an appellative in phrases like "John Bull" and "John Barleycorn."
```


## [2026-09-06T15:17:17.206Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BC%B8%CE%AC%CF%89%CE%BD",
 "prompt": "Etymology of Ancient Greek Ἰάων / Ἴων (Ionian): Mycenaean, Proto-Hellenic *Iāwōn, pre-Greek, descendants including Hebrew יָוָן, Old Persian Yauna, Sanskrit Yavana, Akkadian."
}
```


## [2026-09-06T15:17:19.149Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%AC%99%F0%90%AC%8C%F0%90%AC%99%F0%90%AC%8C",
 "prompt": "Does this Old Persian page exist? If not say so. I am looking for Old Persian 𐎹𐎢𐎴 (Yauna)."
}
```


### [2026-09-06T15:17:21.173Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:17:23.910Z] TOOL RESULT

```
# Ἰάων (Ionian) - Ancient Greek Term

Based on the Wiktionary entry, **Ἰάων** (transliterated as *Ĭā́ōn*) is an Ancient Greek masculine noun meaning "an Ionian."

## Key Details

**Grammar:** The word follows third declension patterns in Attic Greek, with the genitive form **Ῐ̓ᾱ́ονος** (*Ĭā́onos*).

**Pronunciation:** The term evolved across periods—in 5th BCE Attic it was pronounced /i.ǎː.ɔːn/, shifting to /iˈa.on/ by the 1st century CE.

**Related Terms:** Connected words include Ἰάς (*Ĭás*), Ἰωνία (*Ĭōnĭ́ā* - Ionia), and Ἰωνικός (*Ĭōnĭkós* - Ionic).

**Modern Descendant:** The term survives in Modern Greek as Ιάων (*Iáon*).

The entry also references the Wikipedia article on Ionians for broader historical context about this ancient Greek people and their cultural significance.
```


## [2026-09-06T15:17:29.481Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8E%B9%F0%90%8E%A2%F0%90%8E%B4",
 "prompt": "Old Persian 𐎹𐎢𐎴 (Yauna): etymology (borrowed from Ancient Greek Ἰάων/Ἰωνία), meaning, descendants (Persian یونان, Sanskrit Yavana, Sogdian)."
}
```


## [2026-09-06T15:17:30.444Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Ionian",
 "prompt": "Etymology of Ionian / Ionia — Greek Ionia, Ion, Hebrew Yawan, and any statement about origin of the tribal name."
}
```


### [2026-09-06T15:17:35.680Z] TOOL RESULT

```
# Old Persian 𐎹𐎢𐎴 (Yauna)

This Wiktionary entry documents an Old Persian term meaning "Ionian" or "Greek," referring to the region of Ionia and its inhabitants.

## Key Information

**Forms and Meanings:**
- As an adjective: "Ionian" or "Greek"
- As a proper noun: "Ionia"

**Etymology:**
The term appears in ancient Persian inscriptions, notably in cuneiform relief depicting "Ionian tribute bearers" from 5th century BCE Persepolis.

**Linguistic Descendants:**

The word traveled across languages and continents:
- **Persian branch:** Middle Persian *yōnān* → modern Persian یونان (yunân), influencing Arabic, Bengali, Hindi, and Turkish variants
- **Indian branch:** Ashokan Prakrit 𑀬𑁄𑀦 (yona) → Sanskrit यवन (yavana), spreading to Tamil, Thai, and Burmese
- **Cuneiform:** Also attested in Achaemenid Elamite texts

This demonstrates how a single ancient term for Greek peoples propagated through multiple language families across Asia, the Middle East, and beyond.
```


### [2026-09-06T15:17:37.378Z] TOOL RESULT

```
# Etymology of Ionian

Based on the provided content, here's what we know about the origin:

**Primary Etymology:**
The term "Ionian" (adj., from 1590s) derives from "Ionia," referring to ancient Greek districts inhabited by the Ionians—one of the three or four major divisions of ancient Greek peoples.

**Mythological Attribution:**
According to Herodotus, the name traces to an ancestral figure named Ion, described as "son of Apollo and Creusa."

**Linguistic Origins:**
The source suggests the name is likely pre-Greek in origin. A possible connection exists to Sanskrit *yoni* meaning "womb, vulva," potentially referencing "a goddess-worshipping people."

**Geographic Scope:**
Ionia encompassed Attica, Euboea, and the Peloponnesus's north coast, but particularly the coastal Asia Minor strip including Samos and Chios islands.

**Note on Hebrew Yawan:**
The provided content does not discuss Hebrew *Yawan* or make direct connections between it and the Greek tribal name, so I cannot address that aspect based on this source alone.
```


## [2026-09-06T15:17:46.104Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%97%D7%A0%D7%9F",
 "prompt": "Hebrew חנן (ḥanan): meaning \"to be gracious, show favor\", root, and derived names (חַנָּה Hannah, יוֹחָנָן Yohanan). Also note Semitic cognates (Arabic حنّ)."
}
```


## [2026-09-06T15:17:48.067Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%86%CE%BD%CE%BD%CE%B1",
 "prompt": "Ancient/Koine Greek Ἄννα: etymology from Hebrew חַנָּה (Ḥannāh) 'grace', descendants Latin Anna, English Ann/Anne/Anna."
}
```


### [2026-09-06T15:17:52.180Z] TOOL RESULT

```
# חנן (Hanan)

This Wiktionary entry documents a Hebrew and Aramaic word with multiple related meanings.

**Hebrew Verb**: The term חָנַן (khanán) functions as a verb meaning "to pardon, grant amnesty" or "to pity, have mercy, deal kindly." It follows the pa'al construction pattern.

**Proper Noun**: As a name, חָנָן (khanán) serves as a masculine given name, transliterated in English as both Hanan and Chanan.

**Aramaic Usage**: In Aramaic, the same characters represent a verb meaning "to be merciful" and a proper noun referring to the biblical figure Annas, or functioning as a male given name.

**Etymology**: The word derives from the Semitic root ח־נ־ן (kh-n-n), with cognates in Arabic (ح ن ن). The entry includes biblical citations from the Tanach demonstrating usage, such as in Numbers 6:25 where the term conveys divine grace.
```


### [2026-09-06T15:17:53.504Z] TOOL RESULT

```
# Άnnα - Greek Name Entry

This Wiktionary page documents **Άnnα** (Ánna), a Greek feminine proper noun and given name.

## Key Information

**Etymology:** The name "Inherited from Ancient Greek _Ἄnnα_ (Ánna), from Biblical Hebrew _חַנָּה_ (Ḥannā)."

**Meanings:** 
1. References the biblical figure Hannah
2. Serves as a contemporary female given name, comparable to English equivalents like Ann, Anne, or Hannah

**Pronunciation:** /ˈa.na/ with syllable division: Άn‧na

**Grammatical Details:** The entry provides a declension table showing singular and plural forms across nominative, genitive, accusative, and vocative cases.

**Related Term:** Αnnούλa (Annoúla) appears as a diminutive derivative.

The page notes that this name belongs to "Greek nouns declining like 'γαλοπούλa'" and lacks a genitive plural form in standard usage.
```


## [2026-09-06T15:17:57.456Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/y%C4%81nam",
 "prompt": "Does this page exist? If so give the reconstruction, meaning 'favour, grace', and descendants (Avestan yāna-, Old Persian yāna-, Middle Persian, Sogdian y'n)."
}
```


## [2026-09-06T15:17:58.705Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D9%86%D9%8A%D9%86",
 "prompt": "Arabic حنين: etymology (root ح ن ن), meaning 'yearning, longing, moaning'; also any Persian entry حنین."
}
```


### [2026-09-06T15:17:59.317Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:18:04.281Z] TOOL RESULT

```
# حنين (Hanin) - Arabic Word

According to the Wiktionary entry, **حنين** (ḥanīn) is an Arabic noun with these primary meanings:

1. **Strong craving or desire** - The word denotes intense emotional yearning
2. **Nostalgia** - A longing for the past or absent things

## Linguistic Details

The term functions as a "verbal noun of حَنَّ (ḥanna)" and belongs to the Semitic root ح ن ن (ḥ n n). 

Pronunciation is rendered as /ħa.niːn/ in IPA notation, following the rhyme pattern of "-iːn" words in Arabic.

The entry also notes that this masculine noun follows standard Arabic declension patterns as a triptote noun, meaning it takes case endings in both indefinite and definite forms.
```


## [2026-09-06T15:18:18.913Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt FSD_vol2.txt FSD_vol3.txt WEB.txt LEW_1910.txt LAT.txt LKT.txt AFM.txt PLA.txt AFA.txt; do [ -f \"$f\" ] && { echo \"=== $f\"; grep -n -i \"Ionian\\|Ionia\\b\" \"$f\" | head -3; }; done 2>/dev/null; ls | grep -i \"^WEB\\|^PLA\\|^SKT\\|^FSD\""
}
```


### [2026-09-06T15:18:20.784Z] TOOL RESULT

```
=== SKT.txt
13928:aymphony.  (F.  —  L  — Gk.)  F.  sym- phonic,  Cx>L  —  L.  symplionia,  —  Gk.  tfv/i- ^wfla^music  (Lukexv.  jg).  — Gk.  ffvp^«yrof, harmonious.  —  Gk.  (rv/i-,  for  (nJr,  together; ^•K^,  sound. Phosphorus.  (U  -  Gk.)  l^^koipMona.  —
=== FSD_vol2.txt
10014:E-phefsian,  1   i-fi'sen;  2   e-fe'zhan,  o.  Relating  to  or characteristic  of  Ephe.sus,  an  ancient  Ionian  city  of  Asia Minor,  famous  for  its  temple  of  Artemis  (Diana), and  later  also  as  a   center  ot  Christian  worship.- Ephe- sian Artemis,  same  as  Diana  of  the  Ephesians.— E.  Council,  any  one  of  several  councils  of  the  church held  at  Ephesus,  especially  that  which  condemned  Nes- torius  (A.  D.  431)  .-E.  liturgies,  a   group  of  ancient
10036:Epli'c-s«s,  1   ef'i-sus;  3   gf'e-sus,  n.  luh.  An  ancient  Ionian  c-pib'a-tus,  1   i-pib'o-tna;  2   e-pib'a-tfts. commercial  city  of  we.stcrn  Asia  Minor;  capUal  of  the  a.  Marked  by  double
11930:An  ancient  Ionian  common  name  for  any  plant  of  ais  genra  is  dog’ s,toQth  E8"ca-lan'te,  1   6s'ka-lQn't6;  2   e8”eii-lan'te,  ».  1,  Jfuan s   slbvl  Herophlle.—  «inifi  nr  ndde.r  s.tonnur..  2.  ffi-1  Chem.  Vanadium:  for-  -1519),  S   Spanish  soldier;  With  Cortez  in  Mexico.
=== FSD_vol3.txt
3202:city of Ionia Magnesia od Mmindrumt. 2. A coast
19726:- Ionian
24966:g , barile Ionian Islands ■> 10 21 g.; barrU Cuba (honey)
=== LEW_1910.txt
=== LAT.txt
18191:(Pulg.); cf. aussi «819 *ebrionia.
28205:(Tac .), histrionicus (b.lat.); histrionia ( sc. ars), Piante; histrio,
31658:labrae, -arum ( acc.pl. labras, tab.deuotionia, cf.Ernout Rec. textes
=== LKT.txt
=== AFM.txt
=== AFA.txt
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
SKT.txt
WEB_vol1.txt
```


## [2026-09-06T15:18:28.894Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT John/Anna/Ivan\"; grep -n -i \"Johannes\\|Yohanan\\|Hannah\" SKT.txt | head -5; echo \"== FSD Ionian adj\"; grep -n \"I-o'ni-an\\|Io'ni-an\\|I.o'ni.an\" FSD_vol2.txt FSD_vol3.txt | head -5; echo \"== FSD John\"; grep -n \"^John\\|John, \" FSD_vol2.txt | head -5; echo \"== WEB\"; grep -n -i \"Ionian\\|Johannes\" WEB_vol1.txt | head -5"
}
```


### [2026-09-06T15:18:29.061Z] TOOL RESULT

```
== SKT John/Anna/Ivan
== FSD Ionian adj
== FSD John
256:John  Homio  Boutflao  act.  i,  »c.  1.
801:John  Lubbock  Preellistoric  Times  p.  129.  Iw.  a   n.  1872.]
3741:Bums  Sco'tus,  1   dunz  skO'tim;  2   dflns  sco'tfls.  1.  John, "the  Subtle  Doctor”  (1265?-130S?),  a   Franciscan  monk and  scholastic  philosopher.  See  Scotism  and  Dunce.  3. A   nickname  of  Sir  Waiter  Scott:  from  his  knowledge  of  old Scottish  chronicles.  [or  semolina,
5149:mitted  to  William  I.;  thenceforth  an  adventurer.  4.  Sir  Edge'hill,  1   ej'hU;  2   cdidbU,  ti.  A   ridge  mxir  the  .soutlimi. John,  pen.nanie  of  Sir  Richard  Steele.  5.  In  Shakespeare'a  bonier  of  Warwiek.shlre,  England;  first  battle  of  the  Civil AfBg  hear,  a   noble  young  man,  son  of  Gloucester,  who  at-  War,  Sunday,  Oct.  23,  1612.
5289:Johnson  county,  Ind.  2.  A   village  in  Christian  county,  III.  et'mdnt,  2   6t'munt:  It.  Ed-moa'do,  1   ed-m3r
== WEB
36096:Coc- cë’iăn (-yin), n. {Latinized form of Koch.) an adherent of the theology of the covenants founded by Johannes Koch or Cocceius (1603- 1669), professor of theology at Leyden.
42787:Cor’fi-6te, Cor’fiite, n. a native or inhabitant of Corfu, one of the Ionian islands.
65448:E-phé’siin, (-zhin), a. of or relating to the an- cient Ionian city, Ephesus, in Asia Minor, or its people,
85663:(b) impudence; presumptuousness; effron- tery; (c) force; power; effectiveness. [Slang.] gut, v.t.; gutted, pt., pp.; gutting, ppr. 1. to take out the intestines of; to eviscerate. E 2. to destroy the interior of, as by fire. E< Gu’ten-bérg Břble, a Latin Bible produced at Mainz, Germany, sometime before 1456, re- utedly printed by Johannes Gutenberg 13082-1408). It is generally regarded as the
97169:res and the warmer parts of America, and č Ionian K in-dis-cérp/i-ble-ness, n.
```


## [2026-09-06T15:18:31.522Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT yunan/Ion\"; grep -n -i \"Jonien\\|Junan\\|Ionien\" LKT.txt | head -5; echo \"== PLA?\"; ls | grep -i pla; echo \"== AFM hanan\"; grep -n \"حنان\\|حنین\" AFM.txt AFM_pages.txt 2>/dev/null | head -5; echo \"== ARY latin index yauna\"; grep -n -i \"yauna\\|yana\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-06T15:18:31.612Z] TOOL RESULT

```
== LKT yunan/Ion
== PLA?
== AFM hanan
== ARY latin index yauna
1050:Ala Gg pp IL) (ASTYANAX (S'ULzal Sts) lege
1638:ia) Lggee Saad AZMOYANA, — :(AFGHANI) (4), gli!
8353:DUYANALLI HITTITE) <9 wAT (TOKHARIAN A) A. )\5s
9632:BIAO (GREEK) gi ZYANA, ZYANI-—:(AVESTAN) (pln)
9639:AMINDAROV: (DAMAGE) 208 JAYATI, SYANA, JYA-
```


## [2026-09-06T15:18:48.587Z] TOOL CALL #51: Bash

```json
{
 "command": "ls site/pages/221.jpg 2>/dev/null; pdftoppm -f 221 -l 221 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg221 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:18:50.862Z] TOOL RESULT

```
site/pages/221.jpg
total 3096
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:18 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    462 Sep  6 11:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
```


## [2026-09-06T15:18:53.935Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg221.png"
}
```


### [2026-09-06T15:18:54.320Z] TOOL RESULT

```

```


## [2026-09-06T15:18:54.316Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:19:50.761Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT jadiya/yana\"; grep -n \"jadiya\\|yānam\\|yanam\" KNT.txt | head -10; echo \"== PHD yan\"; grep -n \"^yān\\|^yōnān\\|yōn\\b\\|^yān \" PHD.txt PHD_mackenzie.txt | head -10; echo \"== NYB\"; grep -n \"yān \\|yōnān\\|Yavan\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-06T15:19:50.845Z] TOOL RESULT

```
== KNT jadiya/yana
2663:D. As double object, one of the person and the other of the thing: DB 1.44f айа xšaçam tya Gaumdta hya magus айта Kabügiyam ‘this king- ship which Gaumata the Magian took away from Cambyses’ or ‘of which Gaumata deprived Cam- byses’; so also 1.46f, 59, 65f, and its passive in 1.49f hya атат Gaumàlam Шат magum тёасат ditam салтта ‘who might make that Gaumata the Me- dian deprived of the kingship’, DB 4.65 лау Skaurim (= skaubim) пай tunwatam züra akuna- vam ‘neither to the weak nor to the powerful did І do wrong’. DPd 20-2 айа adam yànam jadiya-
4056:20 iyàram : mà : drauga : aita : adam : 21 yünam : jadiyamiy : Auramazd
4058:28 Матау : yanam : Auramazda : dadàt 24 uv : hadd : vitatbis : bagaibis :
4059:Nores то DPd: 9 Фи$їуйтй Jn. (not бча»). 18 abiy Stolze (not an*iys)). 19-20 duSiydram Jn. (not d'a¥-), ^ j yarem? ; тоа with divider and all characters visible, and a gap between i and у", aec. to Cameron. ?! узт" тэ, with separation caused by a defect in the stone (so Stolze’s photograph). * The insertion of yanam is re- quired for the filling of the gap, in which some slight traces of the characters are still visible; so Cameron, from photo.
4148:52 meamaiy : pariyanam : mataly : duruztam :
4204:DSc = DaniUs, Susa C. adam : Darayavaus XS : vazraka XS XSyanam : ViStaspahya : риса TRANSLATION OF DSc: I am...(= DPa 1-3, 4-5). DSd = Danrus, Susa р.
4241:6 yavauš : XS : vazraka : XŠ : XSyanam : XŠ : DHnam : XŠ
4385:1 adam : Dürayavaus XS : vazraka XŠ ASyanam 2 XS DHyünàm XS : ahyàyà BUya : Vi 3 Staspahya : риса : Haxàmanisiya Nore vo DSy: Text read from a carbon rubbing, which assures the omission of the word-dividera; but the space in the lost part of line 3 requires its presence. The defective copy has slightly different line division.
4401:5 XS : vazraka : XŠ : XSyanam : XŠ : dahyünám : vispazanünàm : XŠ : ahyay 6 à : bümiy& : vazrakáyà : düraiy : apiy : Vistáspahyá : puça : Ha
4462:14 dyatiyanam : хёйуаб
== PHD yan
== NYB
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
773:Aiviyàn Ptwbyw'n'] = Āspiyān (g. v.) 11627. — Paz. Á0wyànq (Aog.). As to the spelling -yw?- for -4yā- cf s. v. āyiyān.
845:*āyiyān [’dyw’n'], *āyiyānak [Pdyw'nk'] a bird’s nest 409-16-25, — Reading hypo- thetical; I identify the w. with MPrth ’hy’ng = ähiyänag ‘nest’ (A-H III) < "a0iyan-, borrowed in SW and subjected there to the usual alternation -h- : -y-. The genuine SW form is found in NP 4é- yanah < "čdOyčna-, with -0y- in contact- ual position > -sy-. As to the spelling -yw- for -iy- cf apiyuat, giyäk, niyandar.
909:band [bnd] tie, band, bond; fetters 919. 34! (81? probably mistaken for bry<n> = brin, cf Mx ch. 279; Paz. is wanting); ~ + zēndān imprisonment, captivity 9°; ~ the snare of Death 6514-18; ca rād ka menčyan u gētīkān dänisn u kār-ākāhēh har 2 band 6 tč [i.e. xrat] patvast why are knowledge and skill of both the heavenly and the earthly beings (so) closely tied up with (dependent on) thee [the Wisdom]? 8811-12; the Skr. v. joins band with the preceding har 2: dvdvapi bandhau, but this is contradicted by 12017-18; cigön martömäan i andar gété band 6 mēnēyān patvast estet as men in this world are closely tied up with the heavenly beings. — Av. (926 sq.) banda- ; MPrth. bnd; bndys?n ‘prison’ (MHC); MPrs bnd (A-H II), bn = bann (S, A-H I), bnyst’n = bannistän < band- (A-H I); Paz. NP band. V. bastan.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1342:dräyän-jöyisneh [dPd?n ywdšnyh] the act of chewing performed by one who is chattering: ~ kartan to chew when chat- tering (we would prefer to say: to chatter when chewing) 691°. — drāyān pt. of the next w.; joyišneh det. v. n. of jütan (g. v.). Paz. dräeq jčišni. Skr. v. mauna- madhye jalpa ‘chatter in the midst of silence’, i.e. where silence ought to prevail.
1918:hangösitak [hngwšytk'] resemblance; re- presentation; reflection (of light) 1117-21, 112*; a symbol 12021-22; — in comparisons, together with homänäk: pūt ~ homänäk (food) resembling putrid matters 7612-18; damik andar miyān i asmän ~ etön homänäk cigón ... the resemblance of the earth in the centre of the heaven is like... = the position of the earth... resembles 86°. — From ham + goš, of NP gošah ‘angle, corner, edge’: ‘having the same angle or edge’, ‘bordering on’. MPrs ’ngwsydg; Paz. angošidaa (SGV), Skr. v. drstänta ‘pattern, model’, upa- māna ‘comparison’, nidarsana, pratirūpa ‘example’. A good illustration of its ‘use and purport SGV V, 15-16.
1926:han-tai [ZK D] until, on to: ~ 6 mtyān van to the middle of the tree 415; ~ hàn i veh Dāitī 564; peš hac ~ ka-män ... jöyät before he devours us 98%’ (as to man, v.s. v. man). — Olr *anu-tävat 'to- wards as far (as), cf Skr tāvat ‘so long, so far’ (yāvat ‘as’), v. tāt; hence Milr *(h)an-tàv, SW han-tai, later *(k)andāt, Paz. anda. Prth han < anu, KZŠPrth 1.2 hn prhš L = han fraxé 6, Gr fog čurpoo0ev, also han 6 ibd. and l. 19 = Prs l. 24 D = tai, Gr ac. Not found in MPrthPrs — Av. (127) anu, OP anuv.
```


## [2026-09-06T15:20:06.100Z] TOOL CALL #54: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Ἰωάννης\" \\\n \"https://en.wiktionary.org/wiki/حنان\" \\\n \"https://en.wiktionary.org/wiki/یونان\" \\\n \"https://en.wiktionary.org/wiki/يحيى\" \\\n \"https://en.wiktionary.org/wiki/Ἰωνία\" \\\n \"https://en.wiktionary.org/wiki/Ἰάων\" \\\n \"https://www.etymonline.com/word/John\" \\\n \"https://www.etymonline.com/word/Ionian\" \\\n \"https://en.wiktionary.org/wiki/𐎹𐎢𐎴\" \\\n \"https://en.wiktionary.org/wiki/חנן\" \\\n \"https://en.wiktionary.org/wiki/Άννα\" \\\n \"https://en.wiktionary.org/wiki/حنين\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 221, root Semitic H.n.n (Hannah/John/Ionia): verification of nodes 1-16\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:20:13.068Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/95eacaffbf956bdd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d533e0fe0129ebfe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/61ccb4358261b7aa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68898918d6e87d8b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf05d3f57362b2be.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9dd9d628ca601f5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b762de56cf47d8ea.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f3e607ed1996853.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70f7e520686047f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a7db1a6ee99059d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05d62223c521cf41.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ad9b4ba4ba3e5680.txt
```


## [2026-09-06T15:20:17.287Z] TOOL CALL #55: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg221.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/221.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/221.png; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:20:17.366Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 71497 Sep  6 11:20 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/221.png
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
```


## [2026-09-06T15:20:20.365Z] TOOL CALL #56: Bash

```json
{
 "command": "sed -n '60,130p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T15:20:20.406Z] TOOL RESULT

```
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


## [2026-09-06T15:22:07.891Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"-- BQT v2 حنان\"; grep -c \"حنانه\" BQT_v2_pages.txt; grep -n \"حنانه\" BQT_v2_pages.txt | head -3; echo \"-- LAT/LEW Iohannes\"; grep -c -i \"iohannes\\|ionius\" LAT.txt LEW_1910.txt; echo \"-- LKT Ivan\"; grep -c -i \"iwan\\|ivan\" LKT.txt; echo \"-- WEB Ivan\"; grep -n \"^I'van\\|Ivan,\" WEB_vol1.txt | head -3; echo \"-- SKT hannah/johannes\"; grep -c -i \"johannes\\|hannah\\|ionius\" SKT.txt; echo \"-- FSD Anne PN\"; grep -c -i \"Iohannes\\|Yohanan\" FSD_vol1.txt FSD_vol2.txt"
}
```


### [2026-09-06T15:22:08.053Z] TOOL RESULT

```
-- BQT v2 حنان
0
-- LAT/LEW Iohannes
LEW_1910.txt:0
LAT.txt:2
-- LKT Ivan
13
-- WEB Ivan
-- SKT hannah/johannes
0
-- FSD Anne PN
FSD_vol1.txt:0
FSD_vol2.txt:0
```


## [2026-09-06T15:22:10.613Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ionius\\|iohannes\" LAT.txt | head -3; echo \"-- LKT iwan ctx\"; grep -n -i \"iwan\\|ivan\" LKT.txt | head -5"
}
```


### [2026-09-06T15:22:10.686Z] TOOL RESULT

```
39578:cus et mUlionius ; mularis,-e: m. herba', mulicurius; mulomedicus,-cina
56319:Ddr. lat.: scorpionius, scorpiacum. De scorpionem pravient gat. skaurpjo.
-- LKT iwan ctx
74:De  Sacy  ChrAr  =  A.  J.  Silvestre  de  Sacy,  Chrestomathie  arabe  ou  extraits  de divers  ecrivains  arabes,  tant  en  prose  qu'en  vers,  ä  l'usage  des  6l6ves  de l'ecole  speciale  des  langues  orientnles  Vivantes.    3  Bde.    Paris  1806.
1321:'Dämon,  Teufel'  [Horn  NpEt  S.  133, Nr.  598],  ebenso  tk.  diiv  'böser  Geist'; hieraus  bulg.  serb.  diw  'Riese',  poln. diiv  'Dämon'.  —  Aus  dem  zugehörigen Adj.  devänä  'verrückt'  [Horn  a.  a.  0.] wird  zunächst  tk.  diwane  und  dann  bulg. divane  'Verrückter',  serb.  diivanija  'hal- ber Narr'.    [Bern  SlEtWb  202.
1354:[Letzten  Endes  von  ^evs.dibir  'Schreiber' Horn  NpEtS.  119,  Nr.  540]  'Amtszimmer, Rat,  Tribunal',  hieraus  wurde  der  Sitz des  Beamten,  ein  bequemer  Sitz,  ein Ruhelager,  andererseits  aber  auch  Samm- lung von  Gedichten  eines  oder  mehrerer Dichter,  jedoch  nur  auf  den  Orient  be- züglich. Im  einzelnen  hat  man :  sp.  pg. aduana  'Zollhaus',  prov.  doana,  frz. douane,  it.  doana,  dogana  [mit  Konta- mination von  *ducana  aus  dux  >  doge] 'dass.'.  Frz.  divan  'Ruhebett',  it.  divano, rum.  divan,  russ.  bulg.  diivan,  öech.  dy- van,  dtsch.  Diwan,  engl,  divan,  angloind. dewaun  'Ruhebett,  Gedichtsammlung'. —  Aus  tat.  duwan  [Wechsel  zwischen u  und  i  im  Tk.  häufig,  vgl.  z.  B.  osm. diwar  und  duwar  'Wand'],  duwan  etmek 'richten'  kommt  russ.  duwan  'Teilung eines  Gewinns',  duwanit'  'eine  Beute, Gewinn  teilen'.  [DE  47.  Eguilaz  61. Devic  DEt  104.  ML  2707.  Gorjajew  91 u.  98.  Hobson-Jobson  309/311.
2551:'KameP  [eigentlich  'Schnelligkeit  ha- bend'], hieraus  wahrscheinlich  pers. kärwän  oder  käricän  'Kamelzug,  Reise- gesellschaft', in  alle  europäischen  Spra- chen übergegangen:  rum.  caravanä, chervanä,  it.  caravana,  carovana,  pg. sp.  caravana,  frz.  caravane;  engl,  cctra- van,  ndl.  karavaan;  dtsch.  Karawane, schwed.  fcßj'afrtn;  vxxss.  karawan,  bulg. kerwan,  serb.  karawan,  öech.  karavana, poln.  karaivana.  Mit  pers.  säräi  'Palast' [Horn  NpEt  S.  161,  Nr.  727]  ergibt  sich die  Bezeichnung  für  die  Herbergen  der Karawanen :  känvänsäräl.  Hieraus  rum. cherväsärie  'Lagerhaus,  Stapelplatz',  it. caravanserraglio,  frz.  caravanserail,  pg. caraicansarä ;  dtsch.  A'^rrtwanserai;  russ. karatvanseraj  [vgl.  Karl  Müller,  Die Karawanserai  im  Vorderen  Orient.  Ber- hn  1920].  [Klutre  227/228.  FR.  MÜL- LER in  WZKM  V,  354.
3093:'Weihrauch'  [hebr.  le^önä,  woraus  gr. Xißavoq];  hieraus  mit  ar.  Art.  mlat.  oli- bamim,  frz.  oliban,  olibane,  it.  sp.  pg. olibano,  pharmazeutischer  Ausdruck  für 'Weihrauch'.  Ferner  russ.  bulg.  serb. liwan  'dass.'.  Nach  FAUSTO  LASINIO, Di  alcune  voci  italiane  credute  di  ori- gine  Orientale.  In  GSAI  III,  145/6 diiekt  aus  dem  gr.  6  Xißavoq,  für  die slavischen  Formen  freilich  das  Wahr- scheinlichste. [Devic  DEt  179.  Lammens Rem  185/186.  Eguilaz  466.  Gorjajew 186.
```


## [2026-09-06T15:27:47.569Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nW = [\"https://en.wiktionary.org/wiki/%D7%97%D7%A0%D7%9F\",\n     \"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D8%A7%D9%86\"]\n\ndata = {\n \"pdf_page\": 221,\n \"book_page\": 191,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"H.n.n\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Common Semitic root *ḥ-n-n 'to be gracious, show favour, have mercy'\",\n   \"note\": \"The root is real and the language label 'Semitic' and the gloss are both right: Heb. חָנַן ḥānan 'he was gracious, showed favor', ḥēn 'favor, grace', ḥannūn 'gracious'; Aram. ḥănan, Syr. ḥan, Arab. ḥanna, Akkad. iḥnananni 'he has mercy on me'. Klein (s.v. Hannah) gives exactly this family. NOTE ON THE CITATIONS: Nourai's KLN page numbers on this page (701, 78, 813, 821, 831) are those of the 1971 one-volume 'unabridged' Klein, not of the 1966 two-volume set, where Hannah stands on p.732, Ann on p.~81, Ionian on p.850, Ivan on p.864 and John on p.872 (leaves 378, 51, 437, 444, 448 of the archive.org scan). All five entries were located and read; only the page numbers belong to the other edition. The page as a whole is a single tree that mixes two entirely unrelated Greek words — Ἰωάννης (a Hebrew loan) and Ἴων (a pre-Greek tribal name) — and hangs Old Persian yāna- 'favour' off the Hebrew verb; those three arrows are the page's real errors (nodes #5, #10, and by inheritance #13).\",\n   \"note_fa\": \"ریشهٔ سامی ح‌ن‌ن «بخشایندگی و مهربانی داشتن» ریشه‌ای است واقعی و شناخته‌شده: عبری ḥānan «بخشود، مهر ورزید»، آرامی و سریانی ḥan، عربی حَنَّ، اکدی. کلاین در مدخل Hannah همین خانواده را می‌آورد، پس ادعای نورایی در بارهٔ خودِ ریشه درست است. تنها نکته آن است که شماره‌های صفحهٔ کلاین در این صفحه (۷۰۱، ۷۸، ۸۱۳، ۸۲۱، ۸۳۱) از چاپ یک‌جلدی ۱۹۷۱ است نه چاپ دوجلدی ۱۹۶۶. مشکل اصلی این نمودار در جای دیگری است: نورایی «یانَ»ی پارسی باستان و نام قوم «ایون» یونانی را نیز زیر همین ریشهٔ سامی آورده که هیچ‌یک درست نیست.\",\n   \"sources\": [\"https://en.wiktionary.org/wiki/%D7%97%D7%A0%D7%9F\",\n               \"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D8%A7%D9%86\"],\n   \"ref_check\": [\n     {\"ref\": \"KLN:701\", \"status\": \"supports\",\n      \"note\": \"Klein 1971 ed. s.v. Hannah (= p.701 of that edition; 1966 ed. leaf 378 = p.732): 'Heb. Ḥannāh, lit. \\\"graciousness\\\", from the stem of ḥānan, \\\"he was gracious, showed favor\\\", whence also ḥēn, \\\"favor, grace\\\", ḥinnām, \\\"for nothing, gratuitously\\\", ḥannūn, \\\"gracious\\\", tᵉḥinnāh, taḥănūn, \\\"supplication for favor\\\"; rel. to Aram. ḥănan, Syr. ḥan, Arab. ḥanna, \\\"was favorable, merciful\\\", Akkad. iḥnananni, \\\"he has mercy on me\\\"… Cp. also Ann, Jane, Jenny, Joanna, John.' Exactly Nourai's root box.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"KLN\", \"where\": \"1966 ed. leaf 378 (printed p.732) s.v. Hannah; 1971 ed. p.701\", \"stance\": \"supports\",\n      \"note\": \"grep -n 'Hannah,' KLN_1966.txt / KLN_1971.txt; both editions carry the identical article quoted above.\"},\n     {\"src\": \"FVQ\", \"where\": \"FVQ.txt lines 9605-9630 (Jeffery, in the discussion of the Qurʾānic names)\", \"stance\": \"partial\",\n      \"note\": \"Jeffery touches the family only obliquely: 'there seems reason to believe that this form, like Yahya for Yohanna, has been influenced by Arabic (Brandt, JiRM, viii, 380)'. He does not treat the root ḥ-n-n itself.\"},\n     {\"src\": \"AFM\", \"where\": \"grep 'حنان' AFM.txt AFM_pages.txt\", \"stance\": \"silent\",\n      \"note\": \"no hit; Addi Shir's book covers Persian words in Arabic, and a native Arabic root is by definition outside it.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Arabic\", \"words\": \"H.n.n; Hannâneh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic ḥanna (root ح ن ن) 'to yearn, feel tenderness, be compassionate', with the verbal nouns ḥanān 'affection, mercy' and ḥanīn 'yearning, the moaning of a she-camel for her young'; the intensive adjective ḥannān 'most merciful' is a divine epithet (al-Ḥannān), fem. ḥannāna. This is the direct Arabic continuation of the Common Semitic root of the root box — Klein lists Arab. ḥanna beside Heb. ḥānan, Aram. ḥănan, Syr. ḥan and Akkad. iḥnananni. The 'sad, sorry, wailing' side of the gloss is genuine but comes from ḥanīn 'moaning', not from a grief tradition: Nourai's aside refers to ustūn-e ḥannāna, 'the moaning pillar', the palm-trunk in the Medina mosque that the Prophet used to lean on and which, in a much-quoted hadith, moaned when he moved to the new minbar — during his lifetime, not after his death, so that detail of the note is inaccurate.\",\n     \"derivation_fa\": \"عربی «حَنَّ» از ریشهٔ ح‌ن‌ن، با مصدرهای «حَنان» (مهر، رحمت) و «حَنین» (اشتیاق، نالهٔ شتر برای بچه‌اش)، و صفت مبالغهٔ «حنّان» (بسیار بخشاینده؛ از اسماء الهی) و مؤنث آن «حنّانه». این دنبالهٔ مستقیم همان ریشهٔ سامی است و کلاین صورت عربی را در کنار عبری و آرامی و سریانی و اکدی می‌آورد، پس ادعای نورایی درست است. تنها توضیح جانبی او دقیق نیست: «ستون حنّانه» ستون خرمابُنی مسجد مدینه است که بنا بر حدیثی مشهور هنگام روی‌آوردن پیامبر به منبر تازه نالید، یعنی در زمان حیات ایشان نه پس از وفات؛ معنای «اندوه و ناله» هم از «حنین» می‌آید نه از آن روایت.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D8%A7%D9%86\",\n                 \"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D9%8A%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:701\", \"status\": \"supports\",\n        \"note\": \"Klein s.v. Hannah (1971 p.701): '…rel. to Aram. ḥănan, Syr. ḥan, Arab. ḥanna, \\\"was favorable, merciful\\\"' — the Semitic-root→Arabic arrow exactly as drawn.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 leaf 378 (p.732) / 1971 p.701 s.v. Hannah\", \"stance\": \"supports\",\n        \"note\": \"'Arab. ḥanna, \\\"was favorable, merciful\\\"' listed as cognate of Heb. ḥānan.\"},\n       {\"src\": \"AFM\", \"where\": \"grep 'حنان|حنین' AFM.txt AFM_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"},\n       {\"src\": \"FVQ\", \"where\": \"grep 'hanan|Yohanna' FVQ.txt\", \"stance\": \"silent\",\n        \"note\": \"Jeffery has no entry for ḥ-n-n; the root is native Arabic, not a foreign vocabulary item.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\", \"words\": \"hanân «حنان»; hannân «حنّان ، حنّانه»; hanîn «حنین»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are unassimilated Arabic loans of the literary/Islamic layer of New Persian (from the 9th c. onward), taken over with the Qurʾānic and Arabic-lexicographical vocabulary and with no change beyond the Persian pronunciation of ح as /h/ and of the ʿAyn-less short vowels. Mo'in tags every one of them as Arabic: «حنان: [ع.] (امص.) رحمت» — abstract noun 'mercy'; «حنّان: [ع.] (ص.) بخشاینده» 'gracious'; «حنانه: [ع.] (اِص.) ناله‌کننده، نوحه‌کننده: ستون حنانه» 'wailing, lamenting: the moaning pillar'; «حنین: [ع.] (مص‌ل.) بانگ کردن» 'to cry out'. Qāʾānī's line quoted in the chart («حنّانه‌وار از دل هر دم کشم حنین را») plays on exactly the ustūn-e ḥannāna image, which is why Nourai's gloss for ḥannān includes 'one who cries'.\",\n     \"derivation_fa\": \"هر سه واژه وام‌واژهٔ عربی‌اند و در لایهٔ ادبی فارسی نو (از سدهٔ سوم هجری به بعد) همراه با واژگان قرآنی و عربی وارد شده‌اند؛ هیچ دگرگونی آوایی چشمگیری رخ نداده جز تلفظ فارسیِ «ح». معین هر سه را با نشان [ع.] می‌آورد: «حنان: [ع.] (امص.) رحمت»، «حنّان: [ع.] (ص.) بخشاینده»، «حنانه: [ع.] (اِص.) ناله‌کننده، نوحه‌کننده: ستون حنانه»، «حنین: [ع.] (مص‌ل.) بانگ کردن». بیت قاآنی که نورایی شاهد آورده نیز بر همان تصویر «ستون حنّانه» تکیه دارد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D8%A7%D9%86\",\n                 \"https://en.wiktionary.org/wiki/%D8%AD%D9%86%D9%8A%D9%86\"],\n     \"ref_check\": [\n       {\"ref\": \"MON\", \"status\": \"supports\",\n        \"note\": \"MON_part1.txt lines 54346-54398 (grep 'حنان' MON_part1.txt): «حنان: [ع.] (امص.) رحمت» / «حنان [ع.] (ص.) بخشاینده» / «حنانه: [ع. حنانه] (اِص.) ناله کننده نوحه کننده: ستون حنانه» / «حنین: [ع.] (مص‌ل.) بانگ کردن از…». All tagged Arabic, with the three glosses Nourai gives.\"},\n       {\"ref\": \"FVA:115\", \"status\": \"not_checked\",\n        \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368): refs_online.json records that no digital copy exists on any permitted platform, and there is no local file.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"MON\", \"where\": \"MON_part1.txt ll. 54346, 54350, 54354-55, 54398\", \"stance\": \"supports\",\n        \"note\": \"quoted above; the [ع.] tag is Mo'in's own marker for an Arabic borrowing.\"},\n       {\"src\": \"BQT\", \"where\": \"grep 'حنانه' BQT_v2_pages.txt (the ح volume)\", \"stance\": \"silent\",\n        \"note\": \"0 hits — Borhan-e Qateʿ is a dictionary of Persian words and excludes plain Arabic borrowings of this kind.\"},\n       {\"src\": \"ARY\", \"where\": \"grep 'حنان' incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n        \"note\": \"no hit; Aryanpur's dictionary covers Indo-European roots only.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Hebrew\", \"words\": \"hânan; hannah; Yô-hânan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Biblical Hebrew חָנַן ḥānan (qal) 'he was gracious, showed favour, had mercy' (Num. 6:25 'the Lord … be gracious unto thee'); חַנָּה Ḥannāh, lit. 'graciousness', the mother of Samuel (1 Sam. 1); and יוֹחָנָן Yōḥānān, a theophoric compound of Yō- (the shortened Yahweh element, the same as in Joab, Joel, Jonathan) + ḥānan, 'Yahweh is gracious' — the priestly and later Christian name behind John. Hebrew is the direct continuation of the Semitic root of the root box, so the arrow is trivially right; Klein and Etymonline both spell out the compound in these terms.\",\n     \"derivation_fa\": \"عبری کتاب مقدس חָנַן (ḥānan) «بخشود، مهر ورزید» (اعداد ۶:۲۵)؛ חַנָּה (Ḥannāh) «بخشایندگی»، نام مادر سموئیل؛ و יוֹחָנָן (Yōḥānān) که ترکیبی خدانام است از Yō- (کوتاه‌شدهٔ یهوه، همان جزء نخست یوآب و یوئیل) و ḥānan، یعنی «یهوه بخشاینده است». عبری دنبالهٔ مستقیم همان ریشهٔ سامی است، پس این پیوند بی‌چون‌وچرا درست است؛ کلاین و اتیمآنلاین هر دو همین ترکیب را می‌آورند.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D7%97%D7%A0%D7%9F\",\n                 \"https://www.etymonline.com/word/John\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:701\", \"status\": \"supports\",\n        \"note\": \"Klein s.v. Hannah (1971 p.701) as quoted for the root; and s.v. John (1971 p.831): 'ML. Johannes, fr. Late L. Joannes, fr. Gk. Ἰωάννης, fr. Heb. Yōḥānān, lit. \\\"the Lord is gracious\\\". For the first element see Joab … The second element derives fr. ḥānan, \\\"he was gracious\\\". See Hannah.'\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 leaves 378 and 448 (pp.732, 872) s.v. Hannah, John\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"FVQ\", \"where\": \"FVQ.txt l. 9612\", \"stance\": \"partial\",\n        \"note\": \"Jeffery mentions Yōḥannā only as the Syriac/Christian form behind Qurʾānic Yaḥyā.\"},\n       {\"src\": \"AFA\", \"where\": \"grep 'hanan' AFA.txt (Fraenkel, Aramäische Fremdwörter)\", \"stance\": \"silent\", \"note\": \"no relevant hit.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Persian\", \"words\": \"Yŭhannâ «یوحنّا»; Yahyâ «یحیی»\", \"verdict\": \"plausible\",\n     \"derivation\": \"یوحنّا did not come to Persian from Hebrew directly: the transmitting form is the Syriac church name ܝܘܚܢܢ Yōḥannān (the doubled -nn- and the final long -ā are Syriac/Arabic, not Hebrew), which entered Arabic as يوحنّا Yūḥannā, the standard Arabic-Christian name of St John, and thence Persian — so an extra Syriac→Arabic link is missing from the chart. یحیی is genuinely disputed. Muslim philology reads it as an Arabic imperfect of ح‑ي‑ي 'to live' ('he lives'); Western scholarship (Jeffery; and the rasm argument) sees it as a reshaping of Yūḥannā, since medial nūn and yāʾ are indistinguishable in unpointed early Arabic script, so that YWḤNN could be read YḤYY. Against a purely Qurʾānic origin stands a Nabataean inscription of 306 CE from al-ʿUlā with yḥyʾ, i.e. the shape existed in pre-Islamic Arabia. Either way the gloss 'God is gracious' belongs to Yōḥānān and reaches Yaḥyā only through that identification, not through an Arabic etymology.\",\n     \"derivation_fa\": \"«یوحنّا» مستقیماً از عبری نیامده است: صورت واسطه، نام کلیسایی سریانی Yōḥannān است (تشدید ن و الف پایانی از سریانی/عربی است نه عبری) که در عربی «یوحنّا» شد و از عربی به فارسی رسید؛ پس یک حلقهٔ سریانی–عربی در نمودار افتاده است. دربارهٔ «یحیی» اختلاف هست: صرف‌نویسان مسلمان آن را فعل مضارع از ریشهٔ ح‑ي‑ي «زیستن» می‌دانند، اما خاورشناسان (جفری و دیگران) آن را دگرگون‌شدهٔ «یوحنّا» می‌شمارند، زیرا در خط بی‌نقطهٔ کهن «ن» و «ی» میانی یکسان نوشته می‌شد. از سوی دیگر کتیبه‌ای نبطی از سال ۳۰۶ میلادی در العُلا صورت yḥyʾ را دارد، یعنی این نام پیش از اسلام هم در عربستان بوده. بنابراین معنای «خدا بخشاینده است» از آنِ «یوحانان» است و تنها از راه همین یکی‌انگاری به «یحیی» رسیده؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%8A%D8%AD%D9%8A%D9%89\",\n                 \"https://en.wiktionary.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82\"],\n     \"ref_check\": [\n       {\"ref\": \"MON6:2343\", \"status\": \"not_checked\",\n        \"note\": \"Mo'in vols 5-6 (the aʿlām/proper-name volumes) are not among the local scans, and vajehyab/abadis carry only the lexicon volumes 1-3, so the page could not be opened.\"},\n       {\"ref\": \"AKM:36\", \"status\": \"not_checked\",\n        \"note\": \"A'lam, Farhang-e A'lam-e Ketab-e Moqaddas: refs_online.json records 'purchase only', no digital copy.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"FVQ\", \"where\": \"FVQ.txt ll. 9605-9630 (Jeffery, Foreign Vocabulary of the Qurʾān)\", \"stance\": \"partial\",\n        \"note\": \"'The probabilities seem to be that it came into Ar. from Syr. …' and 'this form, like Yahya for Yohanna, has been influenced by Arabic' — Jeffery routes the name through Syriac, not straight from Hebrew.\"},\n       {\"src\": \"MON\", \"where\": \"grep 'یوحنا' MON_part1.txt MON_part2.txt\", \"stance\": \"silent\",\n        \"note\": \"0 hits: the local Mo'in scan covers the lexicon only, not the aʿlām volumes Nourai cites.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org s.v. يحيى (archived)\", \"stance\": \"partial\",\n        \"note\": \"'The origin of يحيى remains uncertain… diverges notably from the Hebrew יוֹחָנָן'; gives both the ح ي ي derivation and the rasm-misreading theory, plus the 306 CE Nabataean yḥyʾ.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"yâna\", \"verdict\": \"disputed\",\n     \"derivation\": \"The word itself is real and correctly labelled: Old Persian yāna- 'favour, grace', attested in Darius' Persepolis inscription DPd 20-22, aita adam yānam jadiyāmiy Auramazdām 'this I ask as a favour of Ahuramazda' (Kent, Old Persian, text DPd and §284; Bartholomae quotes the same passage). But its parentage in the chart is wrong. Bartholomae (AiWb, s.v.): 'j., g. yāna-, j. yąna- m. \\\"Gunst, Gunstgewährung, Gunstbeweis\\\" (seitens der Gottheiten gegenüber den Menschen) … Zum V. yā-; mp. yān', i.e. a -na- abstract of the Indo-Iranian verb yā- 'to ask, implore, pray for' (Skt. yā-ca- 'beg', RV yāntam sumnám), from PIE *yeh₂-. There is no phonetic road from Hebrew ḥānan to yāna-: Iranian has no source for the initial y-, and a Semitic ḥ- would have been rendered, not deleted, in Old Iranian. Modern scholarship treats OP/Av. yāna- as inherited Iranian and unrelated to Semitic ḥ-n-n; the resemblance is accidental.\",\n     \"derivation_fa\": \"خودِ واژه واقعی است و برچسب زبانی‌اش هم درست: پارسی باستان yāna- «بخشش، لطف»، در کتیبهٔ داریوش (DPd، سطر ۲۰–۲۲): aita adam yānam jadiyāmiy Auramazdām «این را همچون لطفی از اهورامزدا می‌خواهم» (کنت؛ و بارتولومه همین شاهد را می‌آورد). اما نسب‌نامه‌ای که نورایی برایش کشیده نادرست است. بارتولومه در فرهنگ ایرانی باستان می‌نویسد: yāna- «لطف، عطای ایزدی… از ریشهٔ فعلی yā-؛ فارسی میانه yān»، یعنی اسمی با پسوند -na از ریشهٔ هندوایرانی yā- «خواستن، طلبیدن» (سنسکریت yāc-)، از هندواروپایی آغازین *yeh₂-. راه آوایی از «حَنَنَ» عبری به yāna- وجود ندارد: نه y آغازین توجیه‌پذیر است و نه حذف ح سامی. پژوهش امروزی این واژه را ایرانیِ موروثی می‌داند و پیوند آن با ریشهٔ سامی ح‌ن‌ن را رد می‌کند؛ شباهت تصادفی است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%F0%90%8E%B9%F0%90%8E%A2%F0%90%8E%B4\"],\n     \"ref_check\": [\n       {\"ref\": \"SOD:443\", \"status\": \"partial\",\n        \"note\": \"Gharib, Sogdian Dictionary, printed p.443 (SOD_pages.txt leaf 510) no. 10898: \\\"y'n B, M, C — yan ©<OP yana — mercy, grace, favour, wish\\\". Gharib does give Old Persian yāna as the source of the Sogdian word, i.e. she supports the #5→#6 arrow, but she says nothing whatever about Hebrew or a Semitic origin, which is the arrow Nourai actually draws here.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch, s.v. yāna- (BRT.txt ll. 21607-21615)\", \"stance\": \"contradicts\",\n        \"note\": \"'j., g. yāna-, j. yąna- m. \\\"Gunst, Gunstgewährung, Gunstbeweis\\\" (seitens der Gottheiten gegenüber den Menschen) … Zum V. yā-; mp. yān' — derived from the Iranian verb yā- 'ask, implore', with Vedic yāntam sumnám compared; no Semitic connection anywhere in the article.\"},\n       {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, DPd 20-22 (KNT.txt ll. 2663, 4056) \", \"stance\": \"partial\",\n        \"note\": \"'DPd 20-2 aita adam yānam jadiya[miy]…' and the text 'adam yānam jadiyamiy Auramazd[ām]' — the word is attested as Nourai says, but Kent gives it no Semitic source.\"},\n       {\"src\": \"SOD\", \"where\": \"p.443 no. 10898\", \"stance\": \"partial\", \"note\": \"as quoted in ref_check.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Sogdian\", \"words\": \"y`n\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib no. 10898 (printed p.443) y'n, attested in Buddhist, Manichaean and Christian Sogdian, read yān 'mercy, grace, favour, wish', with the explicit note '<OP yana'; the neighbouring entry 10904 y'n-βr'kya '(gift of) grace, favour, blessing' is built on it. Sogdian, the Eastern Middle Iranian language of Samarkand and Panjikent (4th-10th c. CE), continues Old Iranian *yāna- directly — Gharib's '<OP' is the usual shorthand for the Old Iranian antecedent rather than a claim of borrowing from Achaemenid Persian. The #5→#6 arrow as drawn is therefore right; what it inherits from above (the Hebrew parent) is not.\",\n     \"derivation_fa\": \"غریب در فرهنگ سغدی، شمارهٔ ۱۰۸۹۸ (صفحهٔ ۴۴۳)، صورت y'n را در سغدی بودایی و مانوی و مسیحی ثبت کرده، با خوانش yān «رحمت، لطف، بخشش، خواست» و یادداشت صریح «<OP yana»؛ مدخل مجاور (۱۰۹۰۴) y'n-βr'kya «(بخشش) لطف و برکت» نیز بر همین ساخته شده. سغدی، از زبان‌های ایرانی میانهٔ شرقی، این واژه را از ایرانی باستان *yāna- به ارث برده است و «<OP» نزد غریب اشاره به همان صورت ایرانی باستان است نه وام‌گیری از پارسی هخامنشی. پس پیوند «پارسی باستان ← سغدی» درست است؛ آنچه نادرست است پیوند بالاتر (عبری) است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%F0%90%8E%B9%F0%90%8E%A2%F0%90%8E%B4\"],\n     \"ref_check\": [\n       {\"ref\": \"SOD:443\", \"status\": \"supports\",\n        \"note\": \"SOD_pages.txt leaf 510 = printed p.443 (offset printed ≈ leaf − 67 here), entry '10898 y'n B, M, C | yan ©<OP yana | mercy, grace, favour, wish | GMS 181; VJ 1215, 1220; SCE 257; TSP 2.587…'. Nourai's page number and gloss are exact.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"SOD\", \"where\": \"p.443 nos. 10898, 10904\", \"stance\": \"supports\", \"note\": \"as quoted; cf. '10904 y'n-βr'kya … (gift of) grace, favour, blessing'.\"},\n       {\"src\": \"BRT\", \"where\": \"AiWb s.v. yāna- (BRT.txt l. 21607ff.)\", \"stance\": \"supports\",\n        \"note\": \"gives the Old/Middle Iranian background ('mp. yān') that the Sogdian form continues.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Greek\", \"words\": \"Anna; Iwannos\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The derivation is right, the Greek form is not. Ἄννα is the Septuagint/New Testament rendering of Heb. Ḥannāh: Greek had no ḥēth, so the initial consonant was simply dropped and the geminate -νν- kept (Klein: 'Ann, Anna, Anne … L. Anna, fr. Gk. Ἄννα, fr. Heb. Ḥannāh, lit. \\\"grace\\\", from the base of ḥānan'). Ἰωάννης renders Heb. Yōḥānān the same way, with the Greek first-declension masculine ending -ης substituted for the Hebrew ending (Klein s.v. John). Both came into Greek through Jewish-Greek scripture between the 3rd c. BCE and the 1st c. CE. But the chart prints the Greek name as 'Iwannos': in Nourai's own transliteration w = ω, so the intended shape is Iōannos — a nominative that never existed in Greek. The printed page (pdf p.221, book p.191) shows 'Iwannos', so the extraction is faithful and the error is the book's; the same misspelling is repeated inside the chart's NOTE at node #10.\",\n     \"derivation_fa\": \"خودِ اشتقاق درست است، اما صورت یونانی نادرست ثبت شده. «Ἄννα» صورت یونانیِ عبری Ḥannāh در ترجمهٔ سبعینی و عهد جدید است: یونانی «ح» نداشت و آن را حذف کرد و تشدید ن را نگه داشت (کلاین: Anna از یونانی Ἄννα از عبری Ḥannāh). «Ἰωάννης» نیز به همین شیوه برابرِ عبری Yōḥānān است، با پایانهٔ -ης صرف نخست یونانی. هر دو میان سدهٔ سوم پیش از میلاد و سدهٔ یکم میلادی از راه متون یهودی–یونانی وارد یونانی شدند. اما کتاب صورت «Iwannos» را چاپ کرده که با قرارداد خود نورایی (w = ω) می‌شود Iōannos، و چنین صورتی در یونانی وجود ندارد؛ درست آن Iōannēs است. تصویر صفحهٔ چاپی نشان می‌دهد که خطا از خودِ کتاب است نه از خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"Iwannos\",\n     \"correct_form\": \"Iōannēs (Ἰωάννης)\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82\",\n                 \"https://en.wiktionary.org/wiki/%CE%86%CE%BD%CE%BD%CE%B1\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN\", \"status\": \"supports\",\n        \"note\": \"Klein 1971 p.78 s.v. Ann: 'L. Anna, fr. Gk. Ἄννα, fr. Heb. Ḥannāh, lit. \\\"grace\\\", from the base of ḥānan, \\\"he was gracious, showed favor\\\". See Hannah.' And p.831 s.v. John: '…fr. Gk. Ἰωάννης, fr. Heb. Yōḥānān'. Klein's Greek is Ἰωάννης, never *Ἰώαννος.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 leaves 51 and 448 / 1971 pp.78, 831\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"SKT\", \"where\": \"grep -i 'Johannes|Hannah|Ionius' SKT.txt\", \"stance\": \"silent\",\n        \"note\": \"0 hits — Skeat's Concise excludes personal names.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"s.v. Ἰωάννης and Ἄννα (archived)\", \"stance\": \"supports\",\n        \"note\": \"'From Biblical Hebrew יוֹחָנָן (Yōḥānān), \\\"God is gracious\\\"'; 'Ἄννα … from Biblical Hebrew חַנָּה (Ḥannā)'. Nominative is Ἰωάννης.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box: the Latin stage between Greek and English is Late Latin Ioannes / Medieval Latin Iohannes (with the fem. Iohanna/Joanna) and Latin Anna, all of them Vulgate and church forms rather than classical borrowings. Klein s.v. John: 'ML. Johannes, fr. Late L. Joannes, fr. Gk. Ἰωάννης'; s.v. Ann: 'L. Anna, fr. Gk. Ἄννα'. The -h- of Johannes is a medieval Latin re-spelling that misread the Hebrew initial yod-he, and it is that spelling that gave English its silent h.\",\n     \"derivation_fa\": \"این جعبهٔ خالی حلقهٔ لاتینی میان یونانی و انگلیسی است: لاتینی متأخر Ioannes و لاتینی میانه Iohannes (مؤنث Iohanna/Joanna) و نیز Anna؛ همگی صورت‌های کلیسایی و ولگاتی‌اند نه وام‌گیری کلاسیک. کلاین می‌نویسد: John از لاتینی میانه Johannes، از لاتینی متأخر Joannes، از یونانی Ἰωάννης. حرف «h» در Johannes املای دوبارهٔ سده‌های میانه است و همان است که «h» بی‌صدای انگلیسی را پدید آورده.\",\n     \"sources\": [\"https://www.etymonline.com/word/John\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"the box carries no reference in the book; the claim was checked against Klein s.v. John and Ann instead (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1966 leaf 448 (p.872) s.v. John; leaf 51 s.v. Ann\", \"stance\": \"supports\",\n        \"note\": \"'John, masc. PN. — ML. Johannes, fr. Late L. Joannes, fr. Gk. Ἰωάννης, fr. Heb. Yōḥānān'.\"},\n       {\"src\": \"LAT\", \"where\": \"grep -i 'Iohannes|Ionius' LAT.txt (Ernout-Meillet)\", \"stance\": \"silent\",\n        \"note\": \"no entry — Ernout-Meillet does not cover Christian onomastics.\"},\n       {\"src\": \"LEW\", \"where\": \"grep -i 'Iohannes' LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"0 hits.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"Anne, Ann, Anna; John, Jane, Jean, Joanne\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Ann/Anne/Anna come straight from Latin Anna (Klein p.78). John entered Middle English as Jon/Johan from Old French Jehan/Jean < Latin Johannes, and the silent -h- was restored in the 16th c. in imitation of Medieval Latin Johannes (Etymonline). Jane is French Jeanne < Old French Jehane < ML Johanna (Klein s.v. Jane); Jean is the Scots feminine of the same Johanna; Joanne/Joanna is ML Joanna direct (Klein s.v. Joanna: 'ML. Johanna, Joanna, fem. form of ML. Johannes, Joannes'). All are ultimately the Hebrew name of node #3.\",\n     \"derivation_fa\": \"Ann/Anne/Anna یکراست از لاتینی Anna آمده‌اند (کلاین ص ۷۸). John در انگلیسی میانه به صورت Jon/Johan از فرانسهٔ کهن Jehan/Jean و آن از لاتینی Johannes گرفته شد و حرف «h» بی‌صدا در سدهٔ شانزدهم به تقلید از املای لاتینی سده‌های میانه بازگردانده شد. Jane از فرانسوی Jeanne < فرانسهٔ کهن Jehane < لاتینی میانه Johanna است؛ Jean صورت مؤنث اسکاتلندی همان؛ و Joanne/Joanna مستقیماً از Johanna لاتینی. همگی سرانجام به همان نام عبری بازمی‌گردند. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/John\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:78,831\", \"status\": \"supports\",\n        \"note\": \"1971 ed. p.78 s.v. 'Ann, Anna, Anne, fem. PN. — L. Anna, fr. Gk. Ἄννα…' and p.831 s.v. 'John, masc. PN. — ML. Johannes… Cp. Ivan, Jane, Jean, masc. and fem. PN., jenneting, Jenny, Joan, Joanna, Johnny.' Both of Nourai's page numbers are correct for the one-volume edition; in the 1966 set the same articles are on leaves 51 and 448.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 pp.78, 831; also s.v. Jane (1966 leaf 445) and Joanna (leaf 448)\", \"stance\": \"supports\",\n        \"note\": \"'Jane, fem. PN. — F. Jeanne, fr. OF. Jehane, fr. ML. Johanna, Joanna'; 'Joanna, fem. PN. — ML. Johanna, Joanna, fem. form of ML. Johannes, Joannes.'\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/John (archived)\", \"stance\": \"supports\",\n        \"note\": \"'Medieval Latin Johannes → Late Latin Joannes → Greek Ioannes → Hebrew Yohanan… \\\"Jah is gracious\\\", from hanan \\\"he was gracious\\\"'; notes Jane/Joan as feminine variants and the restored -h-.\"},\n       {\"src\": \"FSD\", \"where\": \"grep -i 'Iohannes|Yohanan' FSD_vol1.txt FSD_vol2.txt\", \"stance\": \"silent\",\n        \"note\": \"0 hits; Funk & Wagnalls gives no etymology for the personal name.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Greek\", \"words\": \"Ion 1\", \"verdict\": \"disputed\",\n     \"derivation\": \"The people are real and the date is roughly right: Ἴων (Homeric/Ionic Ἰάων, pl. Ἰάονες, from *Ἰάϝων) is the eponym and tribal name of the Ionians, whose migration to the central west coast of Asia Minor and the offshore islands (Chios, Samos) is conventionally put at c. 1050-1000 BCE — though 'Mediterranean islands' is loose for what was the Aegean seaboard. The derivation drawn is what fails. Ἰάων is not from Ἰωάννης: it is attested in Homer and in Near Eastern records (Heb. יָוָן Yāwān, Akkad. Ia-ma-nu / Ia-va-nu, Egyptian Ywnj) from the 8th-6th c. BCE, centuries before Ἰωάννης was ever coined — the Greek name only came into being when the Septuagint transliterated Yōḥānān in the 3rd-2nd c. BCE. Etymonline states the tribal name 'probably is pre-Greek'; Beekes likewise treats Ἰάων as Pre-Greek substrate. Nourai's own NOTE concedes the link 'is not quite clear'; modern scholarship says there is no link at all, and this is the page's second bad arrow.\",\n     \"derivation_fa\": \"خودِ قوم واقعی است و تاریخ هم تقریباً درست: Ἴων (در هومر و ایونی Ἰάων، جمع Ἰάονες، از *Ἰάϝων) نام نیای اساطیری و نام قوم ایونیان است و کوچ آنان به کرانهٔ باختری آسیای صغیر و جزیره‌های نزدیک (خیوس، ساموس) را معمولاً حدود ۱۰۵۰–۱۰۰۰ پیش از میلاد می‌دانند. اما پیوندی که نورایی کشیده نادرست است: Ἰάων از Ἰωάννης نیامده. این نام در هومر و در اسناد خاور نزدیک (عبری יָוָן، اکدی Iamanu/Iavanu، مصری Ywnj) از سدهٔ هشتم تا ششم پیش از میلاد گواهی شده، یعنی سده‌ها پیش از آنکه نام Ἰωάννης در ترجمهٔ سبعینی از عبری ساخته شود. اتیمآنلاین این نام قومی را «احتمالاً پیش‌یونانی» می‌داند و بیکس نیز آن را از لایهٔ زیرین پیش‌یونانی می‌شمارد. خودِ نورایی در یادداشتش می‌پذیرد که این پیوند «چندان روشن نیست»؛ پژوهش امروزی می‌گوید اصلاً پیوندی در کار نیست.\",\n     \"sources\": [\"https://www.etymonline.com/word/Ionian\",\n                 \"https://en.wiktionary.org/wiki/%E1%BC%B8%CF%89%CE%BD%CE%AF%CE%B1\",\n                 \"https://en.wiktionary.org/wiki/%E1%BC%B8%CE%AC%CF%89%CE%BD\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:813\", \"status\": \"contradicts\",\n        \"note\": \"Klein 1971 p.813 s.v. Ionian (1966 leaf 437, p.850): 'Formed with suff. -an fr. L. Ionius, fr. Gk. Ἰώνιος, \\\"Ionian\\\", fr. Ἴων (gen. Ἴωνος), contraction of Ἰάων (gen. Ἰάονος), \\\"Ionian\\\", fr. orig. *Ἰάϝων, whence Heb. Yāwān, Akkad. Iamanu, Iavanu, Egypt. Yᵉvana, \\\"Greek\\\". Cp. also OI. Yavanaḥ, OPers. Yauna, \\\"Greek\\\".' Klein derives Ἴων from *Ἰάϝων and never connects it with Ἰωάννης, which he treats at p.831 as a separate Hebrew loan — so the page Nourai cites in fact refutes his arrow.\"},\n       {\"ref\": \"OEW:xi\", \"status\": \"not_checked\",\n        \"note\": \"Shipley, Origins of English Words (1984), is lending-only on archive.org (djvu.txt returns 403); p.xi is front matter, not an entry.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 p.813 / 1966 leaf 437 (p.850) s.v. Ionian\", \"stance\": \"contradicts\", \"note\": \"as quoted.\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Ionian (archived)\", \"stance\": \"contradicts\",\n        \"note\": \"'the name probably is pre-Greek'; derives Ionian from Ionia, the districts of the Ionians, with Herodotus' eponym Ion son of Apollo — no Semitic name behind it.\"},\n       {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ, Mo'in's footnote to «یون», vol. 4 printed p.2459\", \"stance\": \"partial\",\n        \"note\": \"«یون Ion (پارسی باستان Yauna) یکی از طوایف بزرگ هلن، که نام خود را از … Ἴων … گرفته» — Mo'in gives the Ion→Ionia→Yauna line but nothing about Ἰωάννης.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"Old Persian\", \"words\": \"yauna\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian Yauna- 𐎹𐎢𐎴 'Ionian; Ionia', one of the satrapy names in the province lists of Darius I and Xerxes (DB 1.15, DNa 28-29, DPe 12, DSf 33/42/48, DSm 8/10, XPh 23, A?P 23/26), with Elamite (I)a-u-na and Akkadian Ia-ma-nu beside it (Kent, Lexicon s.v.). It is a borrowing of Greek Ἰάων/*Ἰάϝων made when the Achaemenids annexed the Ionian cities of Asia Minor after Cyrus' conquest of Lydia in 546 BCE; the Greek digamma of *Ἰάϝων is rendered by the OP diphthong -au-, and the name was extended from the Ionians proper to Greeks in general (the yaunā takabarā, 'petasos-wearing Ionians', are the Macedonians). The arrow #10→#11 is exactly right; only #10's own parentage is not.\",\n     \"derivation_fa\": \"پارسی باستان Yauna- «ایونی؛ ایونیه»، یکی از نام‌های ساتراپی‌ها در فهرست کشورهای داریوش و خشایارشا (بیستون ۱:۱۵، نقش رستم ۲۸–۲۹، DPe، DSf، خشایارشا XPh) که در متن‌های عیلامی (I)a-u-na و اکدی Ia-ma-nu همراهی‌اش می‌کنند (کنت، واژه‌نامه). این وام‌واژه‌ای است از یونانی Ἰάων/*Ἰάϝων که پس از فتح لیدیه به دست کوروش (۵۴۶ پیش از میلاد) و پیوستن شهرهای ایونی به شاهنشاهی هخامنشی وارد پارسی باستان شد؛ «واو» یونانی (دیگاما) به‌صورت مصوت مرکب au بازتاب یافته و معنای آن از «ایونی» به «یونانی» به‌طور کلی گسترده شده است. این پیوند درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%F0%90%8E%B9%F0%90%8E%A2%F0%90%8E%B4\",\n                 \"https://en.wiktionary.org/wiki/%E1%BC%B8%CE%AC%CF%89%CE%BD\"],\n     \"ref_check\": [\n       {\"ref\": \"KNT:204\", \"status\": \"supports\",\n        \"note\": \"Kent, Old Persian, Lexicon (KNT.txt leaf 228; running heads put the leaf at pp.204-205): 'Yauna- adj. \\\"Ionian\\\"; pl., also a province of the Persian Empire; masc. sg. as sb., \\\"Ionia\\\", a province: Elam. (I)a-u-na, Akk. Ia-ma-nu, Gk. Ἰωνία.' Nourai's page number lands on the entry.\"},\n       {\"ref\": \"KLN:813\", \"status\": \"supports\",\n        \"note\": \"Klein s.v. Ionian: '…fr. orig. *Ἰάϝων, whence Heb. Yāwān, Akkad. Iamanu, Iavanu … Cp. also OI. Yavanaḥ, OPers. Yauna, \\\"Greek\\\"' — the Greek→Old Persian arrow explicitly.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KNT\", \"where\": \"Lexicon s.v. Yauna- (leaf 228, pp.204-205)\", \"stance\": \"supports\", \"note\": \"as quoted; cf. also KNT.txt l. 1991 'Yauna \\\"Ionia\\\" or Yaunā \\\"the Ionians\\\"'.\"},\n       {\"src\": \"KLN\", \"where\": \"1971 p.813 / 1966 leaf 437\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"BQT\", \"where\": \"Mo'in's footnote to «یون», vol. 4 p.2459\", \"stance\": \"supports\",\n        \"note\": \"«یون Ion (پارسی باستان Yauna)» — Mo'in equates the Greek tribal name with OP Yauna.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Persian\", \"words\": \"yŭnân «یونان»\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP یونان continues Middle Persian yōnān, a collective/plural in -ān built on Yauna- ('the land of the Yauna'), exactly as tāzī → tāziyān; the Old Persian diphthong au regularly became MP ō and then NP ū (cf. OP Bauda- → NP bud), so Yaun-ān > yōnān > yūnān. Mo'in's own footnote in Borhan-e Qateʿ s.v. یون sets it out: «یون Ion (پارسی باستان Yauna) یکی از طوایف بزرگ هلن … مسکن این قوم را Ionia مینامند … چون ایرانیان نخستین بار با این طایفه از هلن‌ها روبرو شدند و مدت درازی ایونیه مستعمرهٔ ایران بشمار میرفت (در زمان هخامنشیان) از این رو همه نواحی هلن‌ها را «یونان» نامیدند» — the part-for-whole shift from Ionia to all of Greece is precisely the Achaemenid contact. Arabic اليونان is in turn a loan from Persian, and Sanskrit यवन yavana / Ashokan Prakrit yona come from the same Old Iranian source.\",\n     \"derivation_fa\": \"«یونان» فارسی دنبالهٔ فارسی میانهٔ yōnān است، جمع/اسم جمعِ -ān بر پایهٔ Yauna- («سرزمین یَئونه‌ها»)، درست مانند تازی ← تازیان؛ مصوت مرکب au در پارسی باستان به‌قاعده در فارسی میانه ō و سپس در فارسی نو ū شده است: Yaun-ān > yōnān > yūnān. حاشیهٔ خودِ معین در برهان قاطع ذیل «یون» همین را می‌گوید: «یون Ion (پارسی باستان Yauna) یکی از طوایف بزرگ هلن … چون ایرانیان نخستین بار با این طایفه از هلن‌ها روبرو شدند و مدت درازی ایونیه مستعمرهٔ ایران بشمار میرفت (در زمان هخامنشیان) از این رو همه نواحی هلن‌ها را «یونان» نامیدند» — یعنی همان تحول معنایی جزء به کل. «الیونان» عربی نیز از فارسی وام گرفته شده و «یَوَنَ» سنسکریت از همان خاستگاه ایرانی باستان است. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%DB%8C%D9%88%D9%86%D8%A7%D9%86\",\n                 \"https://en.wiktionary.org/wiki/%F0%90%8E%B9%F0%90%8E%A2%F0%90%8E%B4\"],\n     \"ref_check\": [\n       {\"ref\": \"BQT:2549\", \"status\": \"partial\",\n        \"note\": \"The content is there but the page number is a digit transposition: the entry «یون» with Mo'in's Ionia footnote stands on printed p.2459 (vol. 4 of the Mo'in edition, PDF leaf 542 of incoming/BQT/BQT_v4_pages.txt; printed = pdf + 1917). The main text of that edition ends around p.2468, so 'BQT:2549' cannot exist. Read 2459.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"BQT\", \"where\": \"vol. 4 printed p.2459 (pdf leaf 542), footnotes to «یون»\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n       {\"src\": \"HRN\", \"where\": \"grep -i 'Junan|Yūnān' HRN.txt\", \"stance\": \"silent\",\n        \"note\": \"0 hits — Horn's Grundriss treats appellatives, not country names.\"},\n       {\"src\": \"HUB\", \"where\": \"grep -i 'Junan|Ionier' HUB.txt\", \"stance\": \"silent\", \"note\": \"0 hits.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"s.v. یونان and 𐎹𐎢𐎴 (archived)\", \"stance\": \"supports\",\n        \"note\": \"'From Old Persian 𐎹𐎢𐎴 (Yauna), from Ancient Greek Ἰωνία'; the OP entry gives the chain 'Middle Persian yōnān → Persian یونان', with Arabic, Turkish, Hindi and Bengali borrowings from it.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"Latin\", \"words\": \"Iônius\", \"verdict\": \"plausible\",\n     \"derivation\": \"Latin Iōnius 'Ionian' (mare Iōnium, the Ionian Sea) is a straight borrowing of Greek Ἰώνιος, the adjective of Ἴων, and Klein's cited page says so: 'Ionian … fr. L. Ionius, fr. Gk. Ἰώνιος, \\\"Ionian\\\", fr. Ἴων'. What is only 'plausible' is the arrow as the book draws it: node #13 hangs from the Greek Anna/Iōannēs box (#7), not from the Ion box (#10) two rows above it, so the chart formally derives the Ionian Sea from the name John. Read as descending from Ion (#10), the link is fully confirmed; read literally, it repeats the error of #10.\",\n     \"derivation_fa\": \"لاتینی Iōnius «ایونی» (mare Iōnium «دریای ایونی») وام‌گیری مستقیم از یونانی Ἰώνιος، صفت Ἴων، است و همان صفحه‌ای که نورایی ارجاع داده همین را می‌گوید: «Ionian … از لاتینی Ionius، از یونانی Ἰώνιος، از Ἴων». آنچه تنها «با احتیاط پذیرفتنی» است شیوهٔ رسم پیکان است: این جعبه در نمودار از جعبهٔ یونانیِ Anna/Iōannēs آویخته شده نه از جعبهٔ «Ion»، و بدین‌سان کتاب عملاً نام دریای ایونی را از نام یوحنا می‌گیرد. اگر آن را زیر «Ion» بخوانیم پیوند کاملاً درست است؛ اگر لفظ‌به‌لفظ بخوانیم همان خطای بند پیشین تکرار شده است.\",\n     \"sources\": [\"https://www.etymonline.com/word/Ionian\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:813\", \"status\": \"supports\",\n        \"note\": \"Klein 1971 p.813 (1966 leaf 437): 'Ionian, adj. and n. — Formed with suff. -an fr. L. Ionius, fr. Gk. Ἰώνιος, \\\"Ionian\\\", fr. Ἴων (gen. Ἴωνος), contraction of Ἰάων…' — Latin Iōnius from Greek Ἰώνιος confirmed; but Klein's Greek source is Ἴων, not Ἰωάννης.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 p.813 / 1966 leaf 437 s.v. Ionian, Ionic\", \"stance\": \"partial\",\n        \"note\": \"supports the Greek→Latin step, contradicts the parent box the chart attaches it to.\"},\n       {\"src\": \"LAT\", \"where\": \"grep -i 'Ionius' LAT.txt (Ernout-Meillet)\", \"stance\": \"silent\",\n        \"note\": \"the only hits are unrelated strings (mulionius, scorpionius); no entry for the ethnic adjective.\"},\n       {\"src\": \"LEW\", \"where\": \"grep -i 'Ionius' LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"0 hits.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"English\", \"words\": \"Ionian, Ionic\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Ionian (adj., 1590s) is Latin Iōnius plus the English suffix -an; Ionic is Latin Iōnicus < Greek Ἰωνικός (Klein: 'Ionic, adj. — L. Ionicus, fr. Gk. Ἰωνικός, \\\"Ionic\\\", fr. Ἴων'). Both are learned Renaissance formations, used first of the Greek dialect and the region and then of the architectural order (the Ionic capital with its volutes) and of the Ionian Sea. Straightforward Latin→English chain, uncontroversial.\",\n     \"derivation_fa\": \"انگلیسی Ionian (صفت، دههٔ ۱۵۹۰) از لاتینی Iōnius با پسوند انگلیسی -an ساخته شده، و Ionic از لاتینی Iōnicus و آن از یونانی Ἰωνικός (کلاین). هر دو ساخت‌های عالمانهٔ دورهٔ رنسانس‌اند که نخست دربارهٔ گویش و سرزمین ایونی و سپس دربارهٔ سبک معماری (سرستون ایونی با پیچک‌هایش) و دریای ایونی به کار رفته‌اند. این زنجیرهٔ لاتینی–انگلیسی بی‌مناقشه است.\",\n     \"sources\": [\"https://www.etymonline.com/word/Ionian\"],\n     \"ref_check\": [\n       {\"ref\": \"None\", \"status\": \"not_checked\",\n        \"note\": \"the box carries no reference in the book; checked against Klein p.813 and Etymonline instead (see consulted).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 p.813 / 1966 leaf 437 s.v. Ionian, Ionic\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/Ionian (archived)\", \"stance\": \"supports\",\n        \"note\": \"'Ionian (adj., from 1590s) derives from Ionia, referring to ancient Greek districts inhabited by the Ionians'.\"},\n       {\"src\": \"WEB\", \"where\": \"grep -i 'Ionian' WEB_vol1.txt\", \"stance\": \"partial\",\n        \"note\": \"Webster has the word only in glosses ('one of the Ionian islands', 'the ancient Ionian city, Ephesus'); no etymological article in the volume on disk.\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"Russian\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The empty box is Russian Иван Ivan, which reached Slavic with Byzantine Christianity: Greek Ἰωάννης was taken into Old Church Slavonic as Иоаннъ Ioannŭ after the conversion of Rus' in 988, and the vernacular reduced the unstressed initial sequence to give Иван. Klein states the route in one line at the page Nourai cites.\",\n     \"derivation_fa\": \"این جعبهٔ خالی همان «ایوان» روسی (Иван) است که همراه با مسیحیت بیزانسی به زبان‌های اسلاوی رسید: یونانی Ἰωάννης در اسلاوی کلیسایی کهن به‌صورت Иоаннъ وام گرفته شد (پس از گرویدن روس در سال ۹۸۸ میلادی) و در گویش مردمی، هجای آغازینِ بی‌تکیه کاهش یافت و Иван پدید آمد. کلاین در همان صفحه‌ای که نورایی ارجاع داده این مسیر را می‌آورد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:821\", \"status\": \"supports\",\n        \"note\": \"Klein 1971 p.821 (1966 leaf 444, p.864): 'Ivan, masc. PN. — Russ., fr. Gk Ἰωάννης. See John.' Exactly the Greek→Russian arrow.\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 p.821 / 1966 leaf 444\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"Wiktionary\", \"where\": \"s.v. Ἰωάννης, Descendants (archived)\", \"stance\": \"supports\",\n        \"note\": \"lists 'Slavic languages: Ivan, Jan' among the descendants of Ἰωάννης through Latin/Church Slavonic.\"},\n       {\"src\": \"LKT\", \"where\": \"grep -i 'Iwan|Ivan' LKT.txt\", \"stance\": \"silent\",\n        \"note\": \"13 hits, all inside unrelated words (kārwān, dīwān, liwan); Lokotsch covers Oriental loanwords and has no entry for the name.\"}\n     ]\n    },\n    {\n     \"id\": 16, \"lang\": \"English\", \"words\": \"Ivan\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English Ivan is a direct borrowing of Russian Иван, used first of Russian bearers of the name (Ivan the Terrible, r. 1547-84, familiar in English from the 16th c. onward) and then, from the 19th-20th c., as a generic personification of the Russian soldier or the Russian people, on the model of John Bull. Klein's entry at the page Nourai cites gives the Russian source and refers back to John.\",\n     \"derivation_fa\": \"«Ivan» در انگلیسی وام‌گیری مستقیم از روسی Иван است؛ نخست برای نامیدن روس‌ها (ایوان مخوف، پادشاهی ۱۵۴۷–۱۵۸۴، که از سدهٔ شانزدهم در انگلیسی شناخته بود) و سپس از سدهٔ نوزدهم و بیستم همچون نمادِ عام سرباز یا مردم روس، بر قیاس John Bull. کلاین در همان صفحه‌ای که نورایی ارجاع داده خاستگاه روسی آن را می‌آورد و به مدخل John ارجاع می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B7%CF%82\"],\n     \"ref_check\": [\n       {\"ref\": \"KLN:821\", \"status\": \"supports\",\n        \"note\": \"'Ivan, masc. PN. — Russ., fr. Gk Ἰωάννης. See John.' (1971 p.821 = 1966 leaf 444).\"}\n     ],\n     \"consulted\": [\n       {\"src\": \"KLN\", \"where\": \"1971 p.821 / 1966 leaf 444\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n       {\"src\": \"SKT\", \"where\": \"grep -i 'Ivan' SKT.txt\", \"stance\": \"silent\", \"note\": \"no entry; Skeat excludes personal names.\"},\n       {\"src\": \"WEB\", \"where\": \"grep -n \\\"^I'van|Ivan,\\\" WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"0 hits in the volume on disk.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('data/verification/page-221.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-221.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 221"
}
```


### [2026-09-06T15:27:50.108Z] TOOL RESULT

```
written
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 11, 'plausible': 2, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 11, 'not_checked': 6, 'partial': 2, 'contradicts': 1}
books consulted: {'supports': 20, 'silent': 17, 'partial': 8, 'contradicts': 3} | by book: {'KLN': 11, 'BQT': 4, 'Wiktionary': 4, 'FVQ': 3, 'Etymonline': 3, 'MON': 2, 'BRT': 2, 'KNT': 2, 'SOD': 2, 'SKT': 2, 'LAT': 2, 'LEW': 2, 'WEB': 2, 'AFM': 1, 'ARY': 1, 'AFA': 1, 'FSD': 1, 'HRN': 1, 'HUB': 1, 'LKT': 1}
```


## [2026-09-06T15:28:11.334Z] AGENT

Page 221 (book p.191) verified — `data/verification/page-221.json` written, `verify_check.py 221` reports **0 PROBLEM lines** (16/16 nodes).

**Counts** — root: 1 confirmed. Nodes: 11 confirmed, 2 plausible, 2 disputed, 1 transcription_suspect.
Ref checks: 11 supports, 2 partial, 1 contradicts, 6 not_checked (FVA:115, MON6:2343, AKM:36, OEW:xi, plus the 2 boxes with no refs).

**Disputed**
- `H.n.n` #5 Old Persian *yāna* "grace" ← Hebrew *ḥānan*: the word is real (DPd 20-22 `adam yānam jadiyāmiy Auramazdām`), but Bartholomae s.v. *yāna-* derives it from the Iranian verb *yā-* "ask, implore" (PIE *\*yeh₂-*, MP *yān*). No phonetic route from Semitic ḥ-n-n; inherited Iranian, unrelated.
- `H.n.n` #10 Greek *Ion* ← Greek *Iōannēs*: Ἰάων/Ἴων is attested in Homer and in Hebrew *Yāwān* / Akkadian *Iamanu* centuries before Ἰωάννης existed (LXX, 3rd–2nd c. BCE). Etymonline and Beekes call it pre-Greek. Klein p.813 — the page Nourai cites — in fact derives Ἴων from \*Ἰάϝων and never links it to Ἰωάννης, so his own reference contradicts the arrow. His NOTE already hedges; modern view: no link at all.

**Transcription suspect**
- #7 Greek: the book prints **"Iwannos"** (= Iōannos, an impossible nominative); correct is Ἰωάννης / Iōannēs. `error_in: book` — page image checked and copied to `data/verification/sources/refs/ocr/BOOK/221.png`; the extraction is faithful. The same misspelling recurs inside #10's NOTE.

**Plausible**: #4 (یوحنّا comes via Syriac Yōḥannān → Arabic يوحنّا, a link missing from the chart; یحیی's origin is genuinely contested — Arabic ḥ-y-y vs. rasm-misreading of Yūḥannā, with a 306 CE Nabataean *yḥyʾ*). #13 (Latin *Iōnius* ← Gk Ἰώνιος is right, but the box hangs from the Anna/Iōannēs node instead of from *Ion*).

**No extraction errors** — the JSON matches the printed page throughout.

**Two citation notes for the owner (book-side, not data-side)**
- Nourai's KLN page numbers on this page (701, 78, 813, 821, 831) are the **1971 one-volume** Klein; in the 1966 two-volume set the same articles are on pp. 732, ~81, 850, 864, 872. All were located and read.
- `BQT:2549` does not exist (the Mo'in edition's main text ends ~p.2468). The یون entry with Mo'in's Ionia/Yauna footnote is on **p.2459** — a digit transposition.
