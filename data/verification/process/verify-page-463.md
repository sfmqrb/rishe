# Verification process log — verify-page-463


## [2026-09-14T02:27:39.903Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 463 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-463.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-463.json. Write /home/sfmqrb/git/rishe/data/verification/page-463.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 463` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T02:27:40.881Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T02:27:41.734Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T02:27:41.750Z] TOOL RESULT

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


## [2026-09-14T02:27:42.164Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-463.txt"
}
```


### [2026-09-14T02:27:42.195Z] TOOL RESULT

```
1	=== PDF page 463 (book page 433) ===
2	--- entry 0 ---
3	ROOT [Indo-European] So, To : this, that  (refs POK:979)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:979; ZFS:51 | hâ 2, hô, hâu 2, hauv, hya : it, that, the ; ava-hya, awa, awam : he, she ; šim, šâm : him, her
5	  #2 (parent #1) [Pahlavi] refs=BQT:197 | kĕ : that ; avâ : he, she ; avâ-šâm : plural form used as a sign of respect for he/she
6	    #3 (parent #2) [Persian] refs=BQT:1230; HRN:31,170 | Keh «که» : that ; oŭ «او» : he, she ; îšân «ایشان» : he/she, him/her | extra: اینکه ، آنکه
7	#4 (parent #0) [Avestan] refs=AHD:1541 | ha-mazan : the warrior ☞Magh 2
8	  #5 (parent #4) [Latin] refs=None | 
9	    #6 (parent #5) [French] refs=None | 
10	      #7 (parent #6) [Persian] refs=MON5:58 |  «آمازن ۱» : woman warrior (obsolete) ;  «آمازن ۲» : name of a river
11	    #8 (parent #5) [English] refs=AHD:40,1541 | Amazon 1 : woman warrior ; Amazon 2 : name of a river
12	#9 (parent #0) [Germanic] refs=None | 
13	  #10 (parent #9) [English] refs=AHD | the, this, they, there, than, then, that, them, she
14	--- entry 1 ---
15	ROOT [Arabic] Soffeh : seat, saddle, varendah  (refs KLN:1468)
16	#1 (parent #0) [Persian] refs=MON:2156 | soffeh «صُفّه» : seat, saddle, varendah
17	#2 (parent #0) [Turkish] refs=KLN:1468 | sofa
18	  #3 (parent #2) [English] refs=AHD:1227; KLN:1468 | sofa
19	#4 (parent #0) [French] refs=KLN:1468 | sofa
20	--- entry 2 ---
21	ROOT Soito -> redirect to Sě 1
22	
```


## [2026-09-14T02:27:45.067Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-463.json",
 "description": "Read source JSON for page 463"
}
```


### [2026-09-14T02:27:45.141Z] TOOL RESULT

```
{
  "pdf_page": 463,
  "book_page": 433,
  "entries": [
    {
      "root": {
        "name": "So, To",
        "lang": "Indo-European",
        "refs": "POK:979",
        "gloss": "this, that"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:979; ZFS:51",
          "words": [
            {"translit": "hâ 2, hô, hâu 2, hauv, hya", "gloss": "it, that, the", "script": null},
            {"translit": "ava-hya, awa, awam", "gloss": "he, she", "script": null},
            {"translit": "šim, šâm", "gloss": "him, her", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:197",
          "words": [
            {"translit": "kĕ", "gloss": "that", "script": null},
            {"translit": "avâ", "gloss": "he, she", "script": null},
            {"translit": "avâ-šâm", "gloss": "plural form used as a sign of respect for he/she", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1230; HRN:31,170",
          "words": [
            {"translit": "Keh", "gloss": "that", "script": "که"},
            {"translit": "oŭ", "gloss": "he, she", "script": "او"},
            {"translit": "îšân", "gloss": "he/she, him/her", "script": "ایشان"}
          ],
          "script_extra": "اینکه ، آنکه",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "AHD:1541",
          "words": [
            {"translit": "ha-mazan", "gloss": "the warrior", "script": null, "see": ["Magh 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON5:58",
          "words": [
            {"translit": null, "gloss": "woman warrior (obsolete)", "script": "آمازن ۱"},
            {"translit": null, "gloss": "name of a river", "script": "آمازن ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD:40,1541",
          "words": [
            {"translit": "Amazon 1", "gloss": "woman warrior", "script": null},
            {"translit": "Amazon 2", "gloss": "name of a river", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "the, this, they, there, than, then, that, them, she", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Soffeh",
        "lang": "Arabic",
        "refs": "KLN:1468",
        "gloss": "seat, saddle, varendah"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2156",
          "words": [
            {"translit": "soffeh", "gloss": "seat, saddle, varendah", "script": "صُفّه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "در دل خویش طاهرا گشت و ندید جز ترا - صفه به صفه لابه لا پرده به پرده تو به تو",
            "poet": "Tâhereh Ghazvînî"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Turkish",
          "refs": "KLN:1468",
          "words": [
            {"translit": "sofa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:1227; KLN:1468",
          "words": [
            {"translit": "sofa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "French",
          "refs": "KLN:1468",
          "words": [
            {"translit": "sofa", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Soito",
        "redirect": "Sě 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T02:27:47.958Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','ZFS','BQT','HRN','AHD','MON','KLN','MON5','PHD','NYB','BRT','KNT','WLD','IEC','SYN','HUB','FVQ','AFM','PLA','SKT','WEB','FSD','LKT','TTS','ARY','DOZ','LAM','DEV','PHN','AFA']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:600])\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-14T02:27:49.073Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
ZFS {"title": "Mohsen Abolghasemi, Zaban-e Farsi va Sargozasht-e An, Hirmand 1375/1996", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand. Other Abolghasemi titles are open on archive.org and parsianjoman, not this one."}
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
MON5 MISSING
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed 
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start wit
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
```


## [2026-09-14T02:28:31.013Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,140p' SOURCE_MATRIX.md; echo ===; ls refs/ | head -60"
}
```


### [2026-09-14T02:28:31.126Z] TOOL RESULT

```
Exit code 1
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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
- **SOD** — Badr al-Za

... [1662 characters truncated] ...

3 lexicon, vol 4 foreign compounds, vols
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
(eval):1: == not found
```


## [2026-09-14T02:28:32.405Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | head; echo ===; python3 -c \"\nimport json,glob\nf=sorted(glob.glob('page-4*.json'))[-3:]\nprint(f)\nd=json.load(open(f[-1]))\nprint(json.dumps(d,ensure_ascii=False)[:3000])\n\""
}
```


### [2026-09-14T02:28:33.931Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-14T02:28:37.945Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 -c \"\nimport json\nd=json.load(open('page-462.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\" 2>/dev/null || ls /home/sfmqrb/git/rishe/data/verification/page-46*.json"
}
```


### [2026-09-14T02:28:39.154Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/page-46.json
```


## [2026-09-14T02:28:41.815Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls page-4*.json | tail -20; python3 -c \"\nimport json\nd=json.load(open('page-385.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T02:28:42.944Z] TOOL RESULT

```
page-445.json
page-446.json
page-447.json
page-448.json
page-449.json
page-44.json
page-450.json
page-451.json
page-452.json
page-453.json
page-454.json
page-455.json
page-456.json
page-457.json
page-458.json
page-45.json
page-46.json
page-47.json
page-48.json
page-49.json
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "where": "Mann, alphabetical",
   "stance": "silent",
   "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
  }
 ]
}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance": "partial",
   "note": "lists ai. pajasyá- 'Bauchgegend, Weichen' beside the pakṣa- family; gloss 'flank'."
  }
 ]
}
```


## [2026-09-14T02:28:48.943Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json; d=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\nprint('---KLN---'); print(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('---BQT---'); print(d['BQT']['page_offset']); print(d['BQT'].get('lookup_hint')); print(d['BQT'].get('local_file')); print(d['BQT'].get('scans'))\nprint('---HRN---'); print(d['HRN'].get('lookup_hint'))\nprint('---MON---'); print(d['MON'].get('page_offset')); print(d['MON'].get('local_file'))\n\""
}
```


### [2026-09-14T02:28:49.915Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
---KLN---
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
---BQT---
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
---HRN---
Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
---MON---
None
['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
```


## [2026-09-14T02:28:54.171Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 214 215 216 217; do echo \"### POK_03 leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print substr($0,1,1500)}' POK_03.txt; done"
}
```


## [2026-09-14T02:28:54.835Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 97[5-9]\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:28:55.280Z] TOOL RESULT

```
### POK_03 leaf 214
 vfj  ,spinnt'  (*avi^isL',  evvr]  ,nebat',  ivvvriTog  ,gut  gesponnen'  erweisen Anl.  sn-),  Fut.  vrjCTio ;  vrjd^ü)  ,spinne',  vfjf,ia  , Gespinst,  Faden'  (=  lat.  nemen)^ vfjffig  ,das  Spinnen'  (:  ahd.  nät  ,Naht'),  vfiTQOv  , Rocken';  vcj^svogj  vwvra Gramm,  wohl  aus  *v7j-önevog,   ^yrjovTa',
lat.  neöf  nere  {*sne-iö)   ,spinnen',   nemen  , Gespinst,   Gewebe',   netus  ds. ;
mir.  smid  , dreht;  bindet,  quält,  müht  sich  ab';  cymr.  nyddu  ,nere',  corn. nethe,  mbret.  nezaff  ds.  {*sn(i){ö);  mir.  snim  m.  ,das  Spinnen,  Drehen;  Kum- mer'; Abtönung  snö-  in  air.  snäth{e)  , Faden',  bret.  neud  ds. ;  (aber  cymr. ysnoden  ,lace,  band',  corn.  snod  ,vitta'  aus  engl,  snood  ,Haarband');  air. snäthat  ,Nadel',  cymr.  nodwydd  ,acus,  acicula',  acorn.  notuid,  mbret.  na- doez  ,Nadel*;
ahd.  näu  ,nähe*  (=  lat.  neö,  gr.  vfj,  ai.  snäyati^  doch  ohne  s-),  nät  jNahV ; got.  neplttj  aisl.  näl,  ahd.  nädala,  ags.  nädl  f.  ,Nadel'  (aisl.  snälda  , Hand- spindel', wohl  umgestellt  aus  *snäd[i]la)]  *snö'  in  agutn.  snöp,  nschwed. snod{d)  , Schnur',  ags.  snöd  f.  , Kopf  binde'  (:  air.  snäthj  lett.  snäte)-^
lett.  snäjuj  snät  ,locker  zusammendrehen,  spinnen',  snäte,  snäne,  snät{e)ne f.  ,leinene  Decke';  s-los;  ndtns  ,leinen,  zwirnen*,  nät{e)ne  =  snät{e)ne]  *m- als  Schwundstufe  zu  *7iei-  (s.  o.  ai.  nlvi-)  in  lit.  nytis  ,Hevelte  oder  Weber- ka
### POK_03 leaf 215
, schneien*,  pamir §ugni  ^9nij  , Schnee*,  (*snaiga-)'j  gr.  yicpa  Akk.  ,Schnee*,  hom.  äydwKpo^ ,sehr  beschneit*^  vslq)eL  (ytcpsi)  ,es  schneit',  viq)dg  , Schneeflocke*  (nyertÖ , Schneegestöber*),  lat.  nix,  nivis  jSchnee*,  nivit  ,es  schneit'  (wohl  i);  Nasal- präs, ninguit  (ninxit)  ds.;
ir.  snigid  ,es  tropft,  regnet*,  snige  n.  ,Tropfen,  Fließen*,  snecht(a)e  , Schnee* (zum  ^Formans  vgl.  vicpSTÖg)]  cymr.  nyf  , Schnee',  nyfio  ,schneien';
ahd.  ags.  sniwan  , schneien*  (st.  V.,  Fartiz.  gi-snigan,  vgl.  noch  nhd.  bair, Partiz.  geschniwen ;  sonst  nhd.  schw.  V.),  aisl.  snyr  ,es  schneit'  (Partiz.  snißnn jverschneit') ;  got.  snaiws  , Schnee'  =  ags.  snäw,  ahd.   sneo  (Gen.   snewes)*
lit.  sniegas,  lett.  sniegs  (Vokal  vom  Verb  übernommen)  , Schnee*,  snaXgala ^Schneeflocke',  sniega  ,es  schneit',  Inf.  smgtij  apr.  snaygis  , Schnee',  aksl» sn4g^  , Schnee*.
V^P.  II  695,  WH.  II 169  f.,  Trautmann  272f.,  Vasmer  2,  680,  R.  L.  Turner BSOAS  18,  449 f.;  vgl.  ai.  snihyati  ,wird  feucht,  heftet  sich*,  sneha-  m.  ,Kle- brigkeit,  Öl,  Fett*.
sneit-  jSchneiden*;  snoito-  , Abgeschnittenes*.
Got.  sneipan,  aisl.  snida  , schneiden,  ernten*,  ags.  snldaTi  jSchneiden,  hauen*, as.  snithan,  ahd.  snldan  »schneiden';  aisl.  sneid  ,abgeschnittenes  Stück*, mhd.  sneite  , durch  den  Wald  gelegter  Durchhau*  u.  dgl. ;  ahd.  snit  ,der Schnitt*,  mhd.  snlde  , Schneid
### POK_03 leaf 216
g ;  övvQi^saL '  ödvqsr  au  Hes. ; Uihd.  snarren  , schnarren^  schwatzen',  snerren  ^schwatzen',  snurren  ,rauschen, sausen",  snurrcere,  srmrrinc  , Spaßmacher,  Narr',  nhd.  schnarren,  schnurren, Schnurre,  engl,  snarl  ^knurren',  mengl.  snorin,  nengl.  snore  ,schnarchen', mengl.  sneren,  nengl.  sneer  ^verächtlich  lachen';  mengl.  nurnen  /hersagen', ßchwed.  dial.  norna,  nyrna  ,zuflüstern',  aisl.  norn  , Schicksalsgöttin',  mhd. ^arreUj  nerren  ,knurren',  ahd.  narro  ,Narr*;
lit.  niürniuj  niurneti  ,brummen,  knurren';  lett.  nura  ,ein  weinerlicher Mensch',  nurdt  ,brummen,  spinnen  wie  eine  Katze^
Auf  -d\  mengl.  snurtin  ,schnarchen^  mhd.  snarz  , Schnarre,  Wachtel- könig'; lett.  nurdet  , murren,  brummen,  knurren'.
Auf  -g:  norw.  schwed.  snerka  ,prusten,  schnarchen',  schwed.  snurka ,rÖcheln',  mnd.  snorken,  snarken  , schnarchen,  schnauben',  mhd.  snarchen ds.,  nhd.  schnarchen'^  norw.  nurka  ,knarren,  knurren',  ndl.  nurken  ,brum- men,  nörgeln';  lit.  snarglys  , Nasenschleim',  lett.  snurgalas  ds.  (,*rasselnd, röchelnd');  snirguot  , schluchzen;  fauchen  wie  die  Gänse';  lett.  nir^guoties jhöhnisch  lachen',  nui^gt  ,die  Zähne  zeigen';  auch  wohl  lit.  narglyti  ,etwas langsam  tun'  (Bed.  ähnlich  wie  in  Schweiz,  norggen  ,ohne  Erfolg  arbeiten').
Auf  -k:  aisl.  sngrgla  (*snargulön)  , röcheln',  nhd.  nörgeln,  nergeln  ,un- deutlich  sprechen,  mit  verdrießliche
### POK_03 leaf 217
sa,  fibulatura',  nhd.  2Vai^ dial.    auch   ,Klammer,   Krampen   an   Türen*    wie   norw.   norve   , Klamme' Krampe'  (und  lett.  närs,  näre  , Klammer');  *
nhd.  bair.  der-narren  , starr  werden,  besonders  vor  Frost'  (,*sich  zusammÄ»*' ziehen,  -krampfen'),  narr  , mißratene  verschrumpfte  Frucht*,  narr  (schweii^ ,krampfartige   Spannung',   narrennagel  ,unförmig  ausgewachsener  KagSj^ schwundstufig  (mit  s-)  nhd.  schnurren,  ein- schnurren,  -schnorren  »zusamiuto^v schrumpfen',  isl.  snurda , Knoten  an  einem  Faden,  bildlich  vom  Nasenrümpfea^  ^
dehnstufig  aisl.  näri , Weichen^  (,Einschnürung  des  Leibes'),  mhd.  nSrUdk , knapp,  genau,  jung*  und  mit  Abtönung  aisl.  Nöri  , Zwergname',  nör  n.  ,enrft Bucht,  Sund',  dän.  schwed.  nör  ,Knirps,  ganz  kleines  Kind' ;  '*
wahrscheinlich  ahd.  snuor  , Schnur,  Band,  Seil',  dän.-schwed.  snör^^ got.  snörjö  ,geflochtener  Korb*,  ags.  sner  (*snör{ö)  ,  Saite  einer  Harfe',  aiiL sneri  n.  , gedrehtes  Seil';
lit.  neriüj  nerti  , untertauchen,  einschlüpfen,  einfädeln',  nyrH,  Prät.  ni mrti  ,sich  schlängeln,  ranken',  ismrtij   ,sich  verrenken',   näras  ,Tauchei narys  , Schlinge;  Gelenk,  Glied';  lett.  närs,  näre  ,Klammer*;
russ.  neret,  neretö  ,Art  Fischreuse';
hierher  gehört  3.  ner-,  oben  S.  766.
Erweiterungen :
sner-b-  mit  germ.  p:  norw.   dial.   snerpa   st.  V.   ^einschrumpfen,  sie zusammenziehen',  ahd.
```


### [2026-09-14T02:28:55.346Z] TOOL RESULT

```
78967:Page(s): 977 
79008:Page(s): 975 
79083:Page(s): 975-977 
79111:Page(s): 977-978 
79129:Page(s): 978 
79153:Page(s): 978 
79159:Page(s): 977 
79225:Page(s): 977 
79310:Page(s): 978 
79315:Page(s): 979 
79361:Page(s): 979-980 
79410:Page(s): 978-979
```


## [2026-09-14T02:28:58.803Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79290,79420p' POK_full.txt"
}
```


### [2026-09-14T02:28:58.897Z] TOOL RESULT

```
Old English snoru. Old Icelandic snor, sn0r. Modern High German Schnur^ daughter-in- 



law ' (after the a-stem), Crimean Gothic schnos {Hs. schuos); s. -Church Slavic snhcha ds.; 

perhaps also alb. nuse, nusja'bnde' {*snus/e). 

Note: 

Amazingly gr. vuo^, Armenian nu, nurus, alb. nuse obey the same phonetic laws of alb. sn- 

> n- or the drop of initial s- 

References: WP. II 701 f., WH. II 190, Trautmann 273, Vasmer2, 682 f.; after Specht Indo 

Germanic Dekl. 90 f. to Old Indie sanotT acquires, wins ', above S. 906; s. though above 

sneUci^-. 

Page(s): 978 

Root / lemma: soi-to- 
Meaning: sorcery' 
See also: see above S. 891 {se-). 
Page(s): 979 

Root / lemma: solo-, sol(e)uo- 

Meaning: whole, integrate 

Note: 

Root/ lemma: solo-, sol(e)uo-\ "whole, integrate' derived from Root/ lemma: sal-\ "salt; 

salty water'. 

Material: Old Indie sarva-^ unbroken, unmarred, unscathed, undamaged, whole, all, each, 

every ', Avestan haurva-, ap. haruva- " unbroken, unmarred, unscathed, undamaged, 

whole' (= gr. oKoc,, ouKoq, alb. gja/e, compare also Latin salvus). Old Indie sarvatat(i)-^ 

intactness, completeness, entireness, wholeness, welfare, salvation', Avestan haurvatat- 

"Ganzheit, Vollkommenheit, welfare ' (= gr. 6A6Tr|<;); Armenian olj{*solio-) "fit, healthy, 

whole, complete '; gr. Attic oKoc,, Ionian ouAo(; (*6AFo(;) " complete, whole', Vok. ouAs (: 

Latin sa/i/efrom *salve) through reinterpretation to an Imperativ); 

besides with vollerer Formansstufe oKobc, (from *6A£F6(;), oAosTtqi uyiaivsi Hes.; alb. 
gjale, ^/Me "strong, fat, alert, awake, smart', ngjal, ngjairbe\ebe, heal, fatten' {*soluo-); 
zero grade: Latin salvus^beW, fit, healthy, gerettet', salve {see above), Umbrian sal(u)uom 
"salvum', Oscan sa/ai/s "salvus', Paelignian SalauaturPH "Salvator' from * salvo- {*saluuo- 
or *salouo-= gr. oKobc^, Latin salus, -//s"Unverletztheit, haleness, healthiness, 
Wohlergehen', salu-bris "the haleness, healthiness zutraglich', Sallustius (with lengthened 
-/A); besides *solos\x\ soli-dus, soldus ^ dense = gediegen, massiv' and "tight, firm, 
complete, whole', so/dv "dense, filzig', solidare^ to make firm or solid ', Paelignian solois 
"omnibus'; 



Italian *sollos {*sol-no-) in Old Latin sollus '\.o\\is et solidus', Latin sellers, sollemnlsetc, 
Oscan sullus 'omnes'; but cymr. bret. holl, oil, corn. oZ/'whole, all', belong to Old Irish oil 
(above S. 24); Tocharian A salu' complete ', B 5C»/-/77e 'whole'. 

References: WP. II 510 ff., WH. II 471 ff., 555 ff.; 

See also: perhaps in ablaut to sel-, above sel-6S. 900. 

Page(s): 979-980 

Root / lemma: so{sJ, sa 

Meaning: demonstrative stem; he, she 

Grammatical information: originally only Nom. Sg. m. f., die other case of stem to-, fem. 

also sT 

Material: Old Indie saand sah{*sos), f. sa, Avestan ha and ho, f. /7a (also in Old Indie e- 

sa, Avestan ae-sa'this'; with particle -^Old Indie a-sau, Avestan hau, ap. hauvm. f. 'this, 

diese', compare gr. ou[ioc;]); 

gr. 6, n (Doric a:) article (Attic etc. also PI. oi, ai compared with alterem Doric Toi, rai); 
substantivisch 6q (Kai 6c;, r\b'6q) from *sos (or slos), wherefore sich n. 6, Akk. 6v, pv etc. 
gesellte; further das with den ro-forms as the relative gebrauchte 6c; by Herodotus; *so-u-, 
sa-u'\r\ ou[to(;], au[Tr|]; 6-5£ 'this'; 

alb. *so, *sa\n k-u'th\s', /reyid 'diese' {*ke-o) and a-u' that, that yonder, that one; 
emphatically, that well-known; in contrast with hie, the former, (sometimes the latter)', a-Jo 
'ilia'; Old Latin sa-psa "\psa' , sum, sam, sos, sas'eum, eam, eos, eas'; *so-in Oscan exo- 
'hic' (e.g. Abl. f. exac) from *e-ke-so- (to front part s. ko- 'this'); 

gall, so-sin, so-sloAkk. Sg. n.. Old Irish {s)a n- Neutr. of article, and Relativpronomen, s 
prefixedes Pron. the 3. Sg. f. and 3. PI. (//77yC>i/'circum eos' lmb+ si/from *sdns) etc.; Old 
Irish demonstrative -so{*sos) 'this, -e, -es'; bret. /70/7'unser', ho-z' your '; 

Gothic sa, so. Old Icelandic sa, sCr, Old English sem.; 

Tocharian A m. sa-m, f. sa-m, n. ta-m; Tocharian B m. se ( *so), f. sa, n. te; 

to anaphorischen 50 belongs also Gatha-Avestan hoi, jav. he, se, ap. saly, gr. oi 'ihm'; 

besides ein erweit stem sOJio-, sO'lia- Old Indie syah and (after sa) syam. syai., ap. 
hya^xr\., hyai.; perhaps Old Irish se'this' from *slod, and -se, -saparticula augens the 1. 
Sg.; very doubtful is ZuriJekfuhrung from Old Icelandic s/a'this' on previous *slo. 



Fern. *5/ gr. "sie' (Soph.), Old Irish 5/~"sie', Gothic s/, Old High German s/~ s/"sie'; in 
addition after Rosenfeld, Forsch. under Fortschr. 29, 176 schwachtonig 5/in Proto Norse 
s/-a/naR 'that', sa-s/'th\s', su-s/'6\ese', f^at-s/" this '; genus-indifferent are Akk. Old Indie 
s/777, Avestan h/m, ap. s/m. 

References: WP. II 509, Wackernagel-Debrunner III 536 ff., Schwyzer Gr. Gr. 1, 610 f., 
Pedersen Tocharian 1 1 1 3 f. 
Page(s): 978-979 

Root / lemma: sofujra : sora 

Meaning: calf (of leg) 

Material: Gr. aojpoi tt65£(; (m 89) 'Beine ohne Waden'?; Ionian (bpr\ Teil eines Opfertieres, 

calf?; 

Latin sura "calf, if with -ur- from -or, or -u- in ablaut to -du-7
```


## [2026-09-14T02:29:16.760Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ watkins Amazon\"; grep -n -i \"amazon\" AHD_watkins1985.txt | head -20; echo \"@@@ watkins so- to-\"; grep -n \"^so-\\|^to-\\|^sem-1\\|^i-\\|^ko-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:29:16.835Z] TOOL RESULT

```
@@@ watkins Amazon
712:“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
@@@ watkins so- to-
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
1654:sem-1
```


## [2026-09-14T02:29:17.532Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: to-\\|lemma: to,\\|Root / lemma: to\" POK_full.txt | head"
}
```


### [2026-09-14T02:29:17.592Z] TOOL RESULT

```
86858:Root / lemma: to-1, ta-, tio- 
86952:Root / lemma: to-2 
86960:Root / lemma: tolk"- 
86973:Root / lemma: tong-1{ *teng^ 
87009:Root / lemma: tong-2 
87015:Root / lemma: top- 
87038:Root / lemma: tor-, toro-s
```


## [2026-09-14T02:29:27.050Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '705,716p' AHD_watkins1985.txt; echo \"@@@ sem-1 entry\"; grep -n \"^sem-1\\|^sem-!\\|sem-1\\. One\" AHD_watkins1985.txt | head; echo \"@@@ so-\"; grep -n \"Pronominal stem\\|demonstrative\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T02:29:27.131Z] TOOL RESULT

```
ma-. Mother. An imitative root derived from the child’s cry for the breast (a linguistic near-universal found in many of the world’s languages, often in reduplicated form). 1. Latin mamma, breast: MAMMA2, MAMMALIA, MAMMILLA. 2. Probably Greek Maia, “good mother” (respectful form of address to old women), also nurse: MaAIA, MAIEUTIC. (3. More recently formed in the same way is English MAMA.) [Pok. 3. md- 694.]
ma-3, Damp. 1. Suffixed form *md-ro- in Germanic *mora- in Old English mér, marsh, wilderness: MOOR?2. 2. Suffixed form *mé-no- in Latin mdndre, to flow, trickle: EMANATE. [Pok. md-no- 699.]
[macula. A spot, blemish; also a hole in a net, mesh. Latin noun of unknown origin. MACKLE, MACLE, MACULA, MACULATE, MACULE, MAIL?, MAILLOT, MAQUIS; IMMACU- LATE, TRAMMEL.]
mad-. Moist, wet; also refers to various qualities of food. 1. Sanskrit madati, “it gladdens, it bubbles,” hence madana-, delightful, joyful, hence madanah, a myna bird: MYNA. 2. Suffixed form *mad-i- in Germanic *mati- in: a. Old English mete, food: MEAT; b. Middle Low German (ge)mate (ge-, together, from Germanic *ga-; see kom), “he with whom one shares one’s food,” compan- ion: MATE}, 3. Suffixed form *mad-sto-, becoming *mazdo-, in Germanic *masta- in Old English mest, fodder: MasT?. [Pok. mad- 694.]
mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
magh-'. To be able, have power. 1. Germanic *snag- in: a. Old English magan, to be able: May; b. Old French esmaier, to frighten: DISMAY. 2. Germanic suffixed form *mah-ti-, power, in Old English miht, power: MIGHT!. 3. Germanic suffixed form *mag-inam, power, in Old English mzgen, power: MAIN}. 4. Suffixed length- ened-grade form *magh-and-, “that which enables,” in Greek (Attic) mékhané, (Doric) madkhand, device: MA- CHINE, MECHANIC, (MECHANISM), (MECHANO-). 5. Possi- bly suffixed form *magh-u- in Old Persian magus, member of a priestly caste (< “mighty one”): (MAGI), (MAGIC), MAGUS; ARCHIMAGE. [Pok. magh- 695.]
magh-. To fight. Hypothetical Old Iranian *ha-maz-an-,
“warrior” (*ha-, with < *sm-; see sem-'), possibly borrowed into Greek as Amazén, Amazon: AMAZON. [Pok. magh- 697.]
maghu-. Young person of either sex. Suffixed form *magho-ti- in Germanic *magadi-, with diminutive *ma- gadin-, in Old English mezgden, virgin: MAID, MAIDEN. [Pok. maghos 696.]
mai-'. To cut. 1. Suffixed form *mai-d- in Germanic *mait- in: a. Germanic *é-mait-jon, “the biter” (prefix *6., meaning uncertain, from Indo-European @, 6; see Pok. é, 6 280), a small biting insect, in Old English #mette, ant: ANT, EMMET; b. Germanic *mitén-, “the
mas
biter,” a small biting insect, in (i) Old English mite, mite: MITE! (ii) Middle Dutch mite, insect, small object, small coin: MITE?; c. possibly Old French mahaigner, to maim (> Anglo-Norman mangler, to hack): MAIM, MANGLE!, MAYHEM. 2. Suffixed form *mai-lo- in Old Irish méel, shorn, bald, hornless, akin to the source of MULEY. [Pok. 1. mai- 697.]
@@@ sem-1 entry
1654:sem-1
@@@ so-
125:The cognate languages give evidence for demonstrative and interrogative pronouns. Both have also developed into relative pro- nouns in different languages. The most per- sistent and widespread pronominal stems are to- and k“o-, which are preserved in the English demonstrative and interrogative- relative pronouns and adverbs beginning with th- (THIS, THEN) and wh- (WHO, WHICH, WHEN).
559:i-. Pronominal stem. 1. Germanic *is-lik-, same (*lik-, like; see lik-), in Old English ilca, same: ILK. 2. Germanic *jaino-, *jeno-, in Old English geon, that: Yon. 3. Ger- manic *jend- in Old English geond, as far as, yonder: YOND, (YONDER). 4. Extended forms *ydm, *ydi, in Ger- manic */d, *jai, in Old English géa, affirmative particle, and gése, yes (see es-): YEA, YES. 5. Old English giet, gieta (preform uncertain), still: yET. 6. Old English gif (preform uncertain), if: 1F. 7. Basic form *i-, with neuter *id-em, in Latin is, he (neuter id), and idem, same: 1D, IDEM, (IDENTICAL), IDENTITY; (IDENTIFY). 8. Suffixed form *i-tero- in Latin iterum, again: ITERATE; (REITER- ATE). 9. Suffixed and extended form ‘*iéa)-em in Latin item, thus, also: ITEM. 10. Suffixed variant form *e-tero- (see ko-). [Pok. 3. e- 281.]
642:h. Anglo-Norman aloper, to run away from one’s hus- band with a lover: ELOPE. kneigwh-. To lean on. 1. Latin cdnivére (< *con-niguére; com-, together; see kom), “to lean together” (said of eyelids), to close the eyes, be indulgent: CONNIVE. 2. Suf- fixed zero-grade form *knigvh-to- in Latin nictdre, to move the eyelids, wink: NICTITATE. 3. Uncertain preform in Latin niti, to lean forward, strive: NISUS; RENITENT. [Pok. knei-geh- 608.] knid-. Egg of a louse. Suffixed form *knid-d in Germanic *hnito in Old English hnitu, egg of a louse: NIT. [Pok. knid- 608.] ko-. Stem of demonstrative pronoun meaning “this.” I. Variant form *ki-. 1. Germanic *hi- in: a. Old English he, he: HE!; b. Old English him, him: HIM; c. Old English his, his: 1s; d. Old English hire, her: HER; e. Old English Ait, it: 1r. f. Old English hér, here: HERE; g. Old English heonane, heonon, from here: HENCE. 2. Suffixed form “ki-tro- in Germanic *hi-thra- in Old English hider, hither: HITHER. 3. Suffixed form *ki-s in Latin cis, on this side of: cis-. II. Variant form *ke-. 1. Preposed in *ke-etero- (*e-tero-, a second time, again; see i-) in Latin céterus (neuter plural cétera), the other part, that which remains: ET CETERA. 2. Latin -ce (see nu-). III. Attrib- uted by some to this root (but more likely of obscure origin) is Germanic root *hind-, behind. 1. Old English bihindan, in the rear, behind (bi, at; see ambhi): BE- HIND, HIND!. 2. Old High German hintar (> German hinter-), behind: HINTERLAND. 3. Germanic derivative verb *hindron, to keep back, in Old English hindrian, to check, hinder: HINDER}. [Pok. ko- 609.] k6-. To sharpen, whet. Contracted from *koo-. 1. Suffixed extended form “kooi-no- in Germanic *haind in Old English hdn, stone: HONE!. 2. Perhaps Greek kénos, cone, conical object (< “a sharp-pointed object”): CONE. [Pok. Aéi- 541.] kob-. To suit, fit, succeed. Germanic *hap- in Old Norse happ, chance, good luck: HAP, (HAPPEN), (HAPPY); (HAP- LEss), (MISHAP). [Pok. kob- 610.] [kokkos. Kermes berry, pit, grain. Greek noun of un- known origin: COCCID, COCCUS, COCHINEAL; MONO- COQUE.] koksa. Body part. Latin coxa, hip: Coxa, CUISSE, CUSH- ION. [Pok. koksd 611.] kolem-. Grass, reed. Suffixed form *kolsm-o-. 1. Ger- manic “*halmaz in Old English healm, halm, straw: HAULM. 2. Latin cudmus, stalk: CULM!. 3. Zero-grade form “kibpm-o- in Greek kalamos, a reed, straw: CALA- MITE, CALAMUS, CALUMET, CARAMEL, SHAWM. [Pok. kolomo-s 612.] koli-. Glue. Suffixed variant form *koly-a in Greek kolla, glue: COLLAGE, COLLO-, COLLODION; PROTOCOL. [Pok. Rolfeji- 612.] kom. Beside, near, by, with. 1. Germanic *ga-, together, with (collective and intensive prefix and marker of the past participle), in Old English ge-, with, also participial, collective, and intensive prefix: ENOUGH, HANDIWORK, YCLEPT. 2. Latin cum, co-, with: CUM; CONQUIAN. 3. Old Latin com, with (collective and intensive prefix): co-, com-. 4, Suffixed form *kom-trd in Latin contra, against, opposite: (CON!), CONTRA-, CONTRARY, (COUNTER!), COUNTER-, COUNTRY; ENCOUNTER. 5. Suffixed form *kom-yo- in Greek koinos, common, shared: COENO-; CENOBITE, EPICENE, KOINE. 6. Reduced form *ko- (see gher-', mei-', smei-). [Pok. kom 612.] konemo-. Shinbone, bone, Reduced form *kemmo- per- haps in Germanic *hamma in Old English hamm, ham, thigh: HAM. [Pok. konamo- 613.] konk-. To hang. 1. Germanic *hanhan in: a. Old English hon, to hang: HANG; b. Dutch (dialectal) hankeren, to long for; HANKER; ¢C. possibly Middle English he(e)ng, hinge, hinge (ultimately from the base of Old English hangian, to hang): HINGE. 2. Suffixed form *konk-t-d- in
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
```


## [2026-09-14T02:29:42.754Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"to-. Demonstrative\\|to-\\. Pronominal\\|THEN, THENCE\\|so-\\. \" AHD_watkins1985.txt | head; echo \"@@@\"; grep -no \"sem-1\\. One[^.]*\\..\\{0,900\\}\" AHD_watkins1985.txt | head -3"
}
```


## [2026-09-14T02:29:43.704Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '86858,86880p' POK_full.txt; echo \"@@@ magh 697\"; grep -n \"lemma: magh\" POK_full.txt | head"
}
```


### [2026-09-14T02:29:43.787Z] TOOL RESULT

```
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
507:ghaiso-. A stick, spear. 1. Germanic *gaizaz in: a. Old English gar, spear: GORE}; (GARFISH), GARLIC; b. com- pound *nabé-gaizaz, tool for piercing wheel hubs (*nabd, hub; see nobh-); c. Old Norse geirr, spear (in geirfalki, gyrfalcon, akin to the source of Old French girfaut): GYRFALCON. 2. Germanic *gaizé in Old English gdra, corner, point of land: GORE?. [Pok. ghaiso- 410.]
802:omeso-. Also omso-. Shoulder. 1. Form *omso- in Ger- manic *amsa- in Old Norse dss, a (mountain) ridge: os*. 2. Form *omeso- in Latin humerus, shoulder: HUMERUS. 3. Lengthened-grade form *dmso- in Greek 6mos, shoul- der: ACROMION. [Pok. om(e)so-s 778.]
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
977:sneud(h)-. To be sleepy. Expressive root. Compare snu-. Zero-grade form *snud-to- giving *nusto- in Greek nusta- zein, to be sleepy: NYSTAGMOUS. [Pok. 1. sneud(h)- 978.] snu-. Imitative beginning of Germanic words connected with the nose. 1. Germanic *snit-, *snut- in: a. Old English gesnot(t), nasal mucus (ge-, collective prefix; see kom): SNOT; b. Middle Dutch snut(e), snout, akin to the probable source of Middle English snute, snout: SNOUT; c. German Schnauze, snout: SCHNAUZER, SCHNOZZLE. 2. Germanic *snuf- in: a. Low German or Dutch snuffe- len, to sniff at: SNUFFLE; b. Middle Dutch snuffen, to snuffle: SNUFF!; c. Old English *snyflan (> Middle English snyvelen), to run at the nose: SNIVEL; d. Middle English sniffen, to sniff: sNirF. 3. Germanic *snup- in Dutch snoepen, to eat on the sly, pry: SNoop. 4. Ger- manic *snip- in Low German and Dutch snippen, to snap at: snip. 5. Germanic *snap- in Middle Low German and Middle Dutch snappen, to snap at: SNAP. 6. Germanic *snub- in Old Norse snubba, “to snub, turn up one’s nose at,” scold, rebuke: SNUB. 7. Germanic *snak- in Middle Dutch snakken, to snap at, akin to the Low German source of Middle English snacchen, to snatch: SNATCH. [In Pok. snd- 971.] so-. This, that (nominative). For other cases see to-. 1. Greek ho (nominative plural Aoi), the: HOI POLLOI. 2. Feminine form “syd in Germanic *sjé in Old English séo, sie, she: SHE. 3. Compound variant form *sei-ke (*-ke, “that”; see ko-) in Latin sic, thus, so, in that manner: sic}. [Pok. so(s), sd, si 978.] sol-. Also sole-. Whole. I. Basic form *sol-. 1. Suffixed form *sol-ido- in Latin solidus, solid: SOLID; CONSOLI- DATE. 2. Suffixed form *sol-wo- in Greek holos, whole: HOLO-; CATHOLIC. 3. Dialectal geminated form *soll-o-
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1123:walso-. A post. 1. Latin vallus, post, stake, whence vallum, a palisade, wall: VALLATION, WALL; INTERVAL. 2. Greek hélos (< *hdlos < *walsos), stud, nail, wart: MYCELIUM. [In Pok. 7. yel- 1140.]
1130:weg-'. To weave a web. Related to wokso-. Suffixed
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
@@@
```


### [2026-09-14T02:29:43.859Z] TOOL RESULT

```
Root / lemma: to-1, ta-, tio- 

Meaning: that, he (demonstr. base) 

Grammatical information: Nom. Akk. Sg. n. tod, Akk. Sg. m. torn, f. tarn. Gen. Sg. m. tosio, 

f. tesias 

Note: (Nom. Sg. m. f. so, sa, see there) 

Material: Old Indie tad {tat) "das', Avestan taj, Akk. Sg. Old Indie tamm., tami., Avestan 

tdmm., tamt, tain., etc.; Armenian -o'(e.g. ter-d^t\r\e master, mister da, du the master, 

mister', ay-d'\he da'), da^th\s', doin^ihe same', etc.; 

gr. TO, Akk. Sg. tov, rpv (Doric tqv), to etc.; to-vuv "nun' = alb. ta-nf, 

alb. ke-ta^Vr\\s, these' {*tod, out of it in proclitic:) /e(Ablat. *tdd) "where'; 

Maybe alb. {a-te) a/e"that'. 

Latin istum, -tarn, -tud etc., Umbrian e's/^"istum'; Latin tam'so' (old also temporal 
@@@ magh 697
```


## [2026-09-14T02:30:06.387Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ BRT hauv/hāu\"; grep -n \"hauv\\|hāu\\b\" BRT.txt | head -20; echo \"@@@ BRT hya\"; grep -n \"^hya\\|hya-\\b\" BRT.txt | head -20; echo \"@@@ BRT šim\"; grep -n \"šim\\|sim,\" BRT.txt | head -10"
}
```


### [2026-09-14T02:30:06.475Z] TOOL RESULT

```
@@@ BRT hauv/hāu
3138:•  p,  a-xäata-  Adj.  (fem.  °/3-)  'unverletzt, ungestört':  Ayi^  duvaislam  ÜyätW  'tl hauvciy  . .  nirasitliy  (sd.)  , .  "Wohlbehagen, auf  sehr  lange  Zeit  hinaus  ungestört,  es wird  sich  . .  einstellen  . ."  D,  5. 3.
4965:aJs dessen  Konelat:  avam  käram..  °vaAya ksrahyä  .  .  tyam  z-ohyazdaiJ*  /räilayi^ Bh.5.  lof.;  —  nadi'tahaire^  .  .  udafiatata .  .  fasäve^  adam  .  .  asiyavam  abiy  "vam nadi'tabairam  kyi^  nabitkadrai'ari^  agau- batä  Bh. /. i6- 1 8;_j.  3, g,  14, 2. 4. 1  b) sub- stantivisch, auch  im  Sinn  unsres  schwach- tonigen  'er':  t3m  lafmeii . .  yatata  ahurö maxda , ,  aom  Jai'iyat  Yt  ^5. 1  —  3 ;  —  I  gau- mat^  . .  hauv  udapaiata  . .  pasäv<^  ATru* aHy..'vam  asiyav^  Bh.;.ii;  —  *utilmaiy amyaiiiy  vasiy  astiy  kartam  °v<^  .  .  naiy nifistam  Bh.  4.8;  —  tuvam  ks  hyc^ imäm  dipim  vainahy  .  .  imatvä  patikarä . .  yävä  (sd.)  *taumä  *ahatiy  *äva  °vaiy pariiarä  Bh.4-i5;  — ya'^a  «J  snaihi^. paiti.vaiaMt  'vat  paiti.päpayamnS  "..eine Waffe  .  ^  sich  dagegen  zu  decken  suchend' P.  2/;  —  afavatum  mahrka'^ni  aon äinrnta  strmca(sd.)\t ip.12.  a)l'insbes. ein  Nomen,  das  —  zum  selben  Satz  gc- höiig  —  sammt  Zubehör  unmittelbar Toraosgeht:  kSram  tyam  hamii'iyam  kyeT
4970:aväjanam  |  *startä   akatiy  "vaiy  (als  AP.)  mä  dauitH 'vaiy  .  .  parsä  Bh.4'i4i  —  hauv  karam fräiSaytr  .  .  vivana^  nilwa"  pärs^  mann 6a!'dakaf'    karj'uvatiyä    xsa>''apJVt1    abty Bli.j.9;  —  kärJ"  kyi^  hamth^iy^ manä  naiy  gaubataiy  °vam  /adiy'Eh.2.'},io; martiyä  tyaisaty  ..anuHyä  äka'tS 'vaiy {3\sAF.)../rdÄ^/am  Bh.  2. 13.-,        i)  II  auf ein  Relativum  als  dessen  Korrelat:  tya* parsbartam    ä/Sa*    °^a*    adam  pattpadam akunavam    Bh.  t.  14;   —   tyJ'iam    adam aiakam  "vJ^  akunav^tä  D.d.  4 ;  3,  Bh.  l.  7, 4.16,    17,  X.r.  3,  2.3;  —  Uta   ty<^maiy pi^''a^  iatiam  -valciy  (ASn.)  t^urJ'mazdtl patuv    X.7.4;  J.3;    —   kyci'    aparam  .  . Patiparsatiy  °vaky3  . .  Bh.  4-  8;  —  tyaisaiy fi-atamä  anuiiyä  ähc^til  'vaiy  (als  AP.). . frahcTJam  Bh.  3. 1 3 ;  —  tyaiy  panevä  xsäya- hiyä  . .  'vaisäm  naiy  astiy  kartam . .  Bh.  4- 9.11       3)  auf  einen  Satz(inhalt) :  y3  nanm kasyatfke  (sd.)  satthii  da^tti  vfavi  'i'Ot paraiti  (sÄ)  V. /j.  2;  —  ya^a  nSii  .  . kar>tS. .  avasySt  vismteisd.)  °val .  ./rava- lays  Yty.72f.         a)  in  Verbindung  mit ta-  'hie  ille':  ya'isa  azim  häätyene  pu'^rgm daliai  ahmäi  tat  "vat  syapt?m  artdvi.. Ytj.i8f.;(j.S,J5.4,äi,  Vyt.45.        2)vor. ausweisend;  1)  auf  direkte  Rede,  sub- stantivisch: tamatfkil . .  °vat  stuyi:  nSit., xäa  Y.  J2. 3 ;  —  °vat  manawka  maiiiimna : nqm  stavap  Yt5.7;  123,  y.49,  '9- 50;   —  *viövä    'vai   hava    xra'hwa: ml  hiu  nä  .  .  P.  21.         2)  auf  eine erläuternde  oder  ergänzende  nominale  Bei- fügung, a)  adjektivisch,  auch  im  Sinn  unsres Artikels  (des  schwachtonigen 'der'): /a^i- kayäi  yil  aom  puiinm   baraiti  anyahmai arsanai  varsl»m  Yt.  17.58;  —  aat .  .  aom miryjim  /rayrarayati  .  .  parSJars  nqma \.i8.2y,  —  'vä  /ba^sä  .  .  daevaniim  mal- yänqmca  ". .  die  Anfeindungen  der  D.  und Menschen"  Yt. /.  10;  — yasi  tat  paiti  'vä gaiiiä  tayus  .  .  para.baraiti  dasa  ".  ,  was jenes,  das  Anwesen  anlangt.."  V. y.  10; II.         o)    mit   relativischem   Anschluss: *'vau  (NSf.)  pairika  yS   dulyäirya  Yt  8. 54;  —  'vqm  kikrpmt  . ,  yqm  sämake  Yt. y.6i  ;   62,    Y.2O.2,    y.19.14;    —  /la^a *'vadhat  vlsat  yat  tnäsdayamöit  V.  '9- 1 2 ; —  haca  "vaahät  tamia^  yat  datvö.Jatayh V.ig.20\    —    'va   (APn.)  "baEiaza  ..  ya kumäydte  Vr.  9.  3.  b)  substantivisch:
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
5048:Schlacht  gehefert"  Bh.  j.3;  usw.  c)  be- gründend 'aus  den  angegebenen  Grün- den, folglich,  in  Folge  dessen'**:  paurvB yat  ditn  usca  usdvanayat  .  .  %raitaonö  .  . hS  °%a  vazata  %ri.ayar3m  ", .  der  schwebte in  Folge  dessen  .."  Ytj.öiC;  —  ai-a •  ].,  p.  ava'^a  Adv.  I)  'de,  ita';  1)  ver-  ait)m  nmä/am  baraytn  °%a  iriststn  hirt- gleichend  'so,  ebenso';  ein  Nebensatz  mit  zayin  "so  sollen  sie  die  Behausung  weg- y<^a  'wie'  geht  voraus  oder  folgt:  l_>'a;ia-  tragen  (und)  folglich  den  Toten  dalassen" sam  ..  ahaAya^  '^ä  *aiunavaya"i3  Bh.  V.  Ä  3;  a;  —  vTspe  fyrisfnti  pinnine 1. 8;  —  yd^a  .  .  hvanxhStm  .  .  fraca .  »&«  mOvayacit  .  .  tinsttUu  (sd.)  YL  14. aiti  ahvica  vazaite  ..  °^a  az»mHf  ..  a/a-.^Z.  4)  'desgleichen,  item';  pagtryäi säniYtio.iiS; — }ydh3 paruvamay  °%ä' mdarftayfn{sA)  af^nitäyukim  °>a  ätrpm Bh./,i4';  4.4,5.2;  —  \- iyam  yuviyS  {sA.)  V.J5.48;  —  mairyS  drva  bizangrB  "äa akäniy  *°^<J  *ya'iä  adam  niyastäyam  D.  ahmaoys  V. 5.35;  — JvS  nanm  ..  Jainli i-/.y,  — yimö  °'^a  kmnaot  yaia  dim  nsit  ''ha  m^nts  V.J. 37;  38;  —  ä'hrö *iiasaf  ahurö  V.  2.32;  i8.-t,t,  35,  38,  ir).  ahurake  . .  °^a  näirikayäi  V.  15.45  Gl.; 33.  a)  vorausweisend 'folgendennassen,  Vd.  2.  11) 'in  einem  solchen  Fall,  unter alio'-.lhauv  karahy3 'hä  adurußyt^  adam  solchen  Umständen':  yat  ..  spä  ahqm.- hardiyc^  amiy  Bh./.ii;  16,  2.3,  5,  ^.x'^}  baöhimtöS  vä  bavaf..°'ha  Al baeidz^m(sd.) 1.16,  2,14,^.5;  —  y-UOT  (sd.)  ..  aduru-  .'.  upi^isayffi  Y. IJ.35;  15.48.  in)'dort's'; jiya*  -hiJ  a%ah<^  adam..  amiy  Bh.  b— j';^,fs  'ha  dasiam..vlbarai  aHaisva  var>ßva 4.29;  —  '^äidiy  a>aAam  paraidiy  "so .  "wer  hat  dort  die  Rehgion  verbreitet..?" befahl  ich  ihm;  'Zieh  aus  . .'"  Bh.j.3;  V.  2.42;  39.  [Vytj^:  lies  'S«".] 9,  14,  2.6,  7,  10,  14;  —yadiy  '%a  *mam-  Ableit.  —  Eig.  'auf  jene  Weise'.  —  wo*s. yüAay  hacä  aniyanä  mä  tanam  D.5.3;Bh.  |  "^ä.  —  Pü.:  ää«,  (mV.  3.  42):  fiar^ 4-l'A — "''^  °^^  marthanS:  ..  Yt.lp.47;  — AS'':ba  vyaxmanyala:..  Yt/p.43-  a)  mit folgendem  _j'fläa  oder^ai  'insofern . .  als
5265:I  mit  nt,  niy  i)  'herab(zur  Erde)kommeB, I -sinken':  vTsp>m  a  ahmltyataim  (tiyris) \paili.apayal  vazamnö  sl'amantpm  avi gat- Wlm  ^fanvaia  paiti  nirat'''  "bis  dass  er (der  Pfeil)  dahinschiessend  zum  Berg  X^. gelangte;  auf  dem  ?C.  kam  er  zur  Erde" Yt<?.38;  —  5.  noch  «r«  Inf.  2)  'herab- kommend sich  einstellen  in  — ',  mit  abiy und  Akk.;  siy.itis..  hauvciy  t^urä  nirasätiy abiy  imäm  vi^am  "Wohlbehagen  ■ .  (es) wird  sich  durch  Ah.  einstellen  in  diesem Haus"  D.  5.3.
5288:arminiye^  hülditahya  pui:''^  hauv babirauv  Bh.j,i3;  4.t,  Bh.i; .  abiy  avam  °xam  aUyavJ'  Bh,
5703:Sagartien . ."  D.5.  2;  —  hauv  °lam  haini- '^''iyam  akunauS  Eh.  4-2;  —  adam xSayäHy<^  amty  -laiy  Bh.  2.  14,  4-  2,  Bh-g.
6567:sva.  da  sein,  vorhanden  sein,  extstiien ;  es  hat  am  ku'-äst»iram  Yt.  /j.  i  s  * ;  153';  — gibt..".  A)  II  im  Ap.:  /  gaumätc^dafväis . .  Aatam  dracjistais  \.12.^;  ^', ttämt^  »lagul  ahJ'  hauv  . .  Bh.^.z;  — !2i?.3;  —  kahmäiclt  hätqm  jiß'qm  .  .ädä t/'urJ'ma^ä  .  .  ulä  antya  ba^äkJ'  (yay'  (sd.V'JcdemderSeienden.."  Y.jj.S;/^.!!, h(ftiy  "AHM. . .  und  die  andern  Götter,  \  12.  4,  27. 15,  A. J.  7;  —  tqtn  daenqm  yn die  es  gibt"  Bh.^^.  13;  12;  —  negirt:  naiy  kätam  vahista  "die  Religion,  die  für  die J>io*  martiyt^  naiy  pirsa^  naty  . .  hyJ' . . '  Seienden  die  beste  ist"  V.  44. 10;  —  ya'ia "es  war  kein  Mensch  da,  weder  ein  Perser  haribis  jijisam  (sd.)  .,  Y.2/.1;  —  ysi noch  . .,  der . ."  Bh.  M  3.  B)  im  Avf.:'A»nti    (APn.)    aiüha    z>mS   kan^nii    (sd.)
7962:•  p.  imaima-')  m.  EN.  eines  Susiers,  der sich  gegen  Darius /.  empörte:  »*dahyaus hauv  haciim<^'  hami^t'iyä  abavJ'  1  mar- tiyc^'  "Ma*  nilmt^  **m<ajiy^  avam  mä^t- itam  akuiiav^  Bh.5,  i".
8195:vor  dem  ersten  Glied;  'ta  buyä  afrasaiiitil 'ta  äSu^.sravä  AacimnS  Y.  /;.  i ;  —  E  gau- mülJ'  .  .  adlru^  k^bajiyam  °tä  psrsam 'tä  mudam  'ta  aniyil  daAyav^^h.i.ii'i*; loJ*',  iii*>,  2.13*,  14';  — fras'a  upa.- Siiiidayäti  tni^rS . .  'ta  nmänjui  °ta  vXs?m 'ta  . .  Yt.  /o.  i89.  b)  beim  letzten  Glied zusammen  mit  a)  td,  ß)  /i^  (s.  auch  II  2  a) 'und  auch';  a)  barat  i^amiS  , .  baSsas>m 'ta  anumca  Vt/^.2.  ß)  yat  upanhacat taelyantqm  vprpiräjanfin  'ta  anySsat'"' haxayS  Yt.  /().  89;  87;  —  Aazar^nm Vij^wA  bavaiti  'ta  äsmmcit  frazaintm Yl  /<V.  5.  II)  zur  Verbindung  von  Sätzen; i)  bei  gleichem  Subjekt:  \  hauv  käram fraisayi^  ..  'tJsiJm  i  martiyam  maiistam aiunaus  Bh.j.^;  l.iS,  2.4,  13',  14',  16, 3.7,  II,  4-2,  16,  I70-I'.  D-4.3,  X.7.3; —  babirum  asiyavam  vasna  a'urtrmaz- dähJ'  °/(7**  babirum  agarbäyam  'tä  avam .  .  agarbJyam  "ich  zog  nach  Babylon und  nahm  nach  dem  Willen  AhM&. Babylon  ein  und  nahm  jenen  .  .  ge- fangen" Bh.2.1-,11  — ya'^a  az?m  banäa- ytni  .  .  fraiirasyätam  'ta  .  ,  vdaayeni  'ta .  .  upanayeni  YL5.18;  9^,  31*,  5.34,  82, ;;.2,  Y./0.4,  F.p»  FrB.  a)  Das  Sub- jekt ist  wiederholt:  'ta  drvh  asp>m  *viste\ 't.i  drva  .  .  yavanhim  *viste  Aog.  ^2;  —  | da'iäni  li  .  .  'ta  tl  az?m  afrlnäni  V,  22. 5.  a)    bei   verschiedenen   Subjekten:
8196:(^uri^matdil  ^uväitt  dausta  biyil*  'tstaiy fauml  rasiy  bty^  'ta  dargani  jXva  Bh.4- 10;  II,  i6^  17',  1. 18,  ^.  7;  —  il  J  mar- tiyJ'  a'ii''ina^  .  .  hauv  udapatatH  .  .  'ta 1  martiyc^  babinanya!'  . .  hauv  udapatata Bh./.  16;  —  ul'ta  bä  yim  halaht  'ta  mqm upaviaiaM  Yt.  ly.  J ;  iS. 6J,  Az. 2.  a) llzu- sammen  mit  ay  (s.lb  ß)>>:  i'aAiä  t^ura'^- masdähJ'     *'tamaiy^>  ■*     aniyasny     vasty
8273:•  p,  upa'darma-  m.  £N.  eines  Mannes: /  martiy^  ah''ind'  nämd'  'makyä pU^^'J' hauv  udapatats  ''uvajaiy  Bh. /.  16.
8974:77,3;  —  im(^  slänamCsd.}  hauv  niyastäyJ' ka-  X.7.3.
9161:II  utä  pitrsam  .  ,  util  aniyl  dakyäv^ I  hauv  ^äyasatä  " uväipasiyam  (sd,)  akufä l(3SPrM.)    Bh.y.ii.  a)   mit  Adv,    statt
9515:aha*  Bh.  2. 6;  5, J.  5.         2)  'Volk'  in  poli- 1     ^'^■- ^  ^-^"^  '""''■  -  ''  ^^-  S  JSJ- tischem   Sinn;   'die  Leute':    pasava"    -ra")         S-  '"^""'  ^-  5'-  ''■  '■  '^''^''-^- >iffnOT'a*  "amt^^iye^  a6av<^ . .  uH  pärsa^  •  j-  kirft-  Adj.  'versans  circa  -,  sich  ab- utn   madä*  ata  anml  dahyävc^  ßh./.  11;  gebend,  zu  tun  machend  mit -,  tätig  bei -'. 13,  16,  ?.I3,  r.  10;  —  hauv  -rahyä  am^ä       f^^P^-  "  ^"""  ^-  *'"'-■  "  ■^ß'"    '^'^''-  >""*
9848:-        '  magui  .  .  'iJ'  näma'  hauv    udapatatä  .  .
9849:hauv    kärahyä    ava%ä    adurujiy<^    adam
10438:obern; gefangen  nehmen',  Akt  und  Med.: xsiii-^atn  lycr  bäbirauv  hauv  agarbJyatS Bh.J.16;  11";  —  imil  dahyavJ^  tyä  adam agarbiiyam  D.tf.3;  ij-y,^-  *vi"da''/am3 bilbirum  agarbSya''  Bh.y.  14;  2.  i;  — bäbirum  hauv  agarbilyatä'&i.^.iy,  —  utä g  xsaya'iiyä  agarbSyam  Bh.  4. 2;  3;  — avam  vahyazdätam  agarbsy^  utä  martiyä tyaisaiy  fratamä  anusiya  äh^tä  agarbaya"
10711:j.,  g.  xäaSra-,  p.  xSsO-'a-  n.  'imperium, regnum,  Herrschaft,  Reich';  uzw.  im  Sinn von  1)  "Herrschgewalt,  Obergewalt,  Herr- schermacht'"; i)  I  im  Ap.:  c^ur^mazdä h'am  mann  fmbara''  Bh./.s,i3;  9,  'D.4. 1,17. 1 ;  —  °^^am  iyt^  bäbirauv  hauv  agar- blyaiiJ  Bh.7.  16;  11';  —  vasnä  a^urO^- mazdäA^  imJ'  °h''am  därayämiy  Bh.  /. 9;  9;  —  °'ii''amiim  adam  adlnant  Bh./. 13;  i3i  —  "''"*  "ä'^'»'«  fy<^  gaumätc^ ty^  maguS  üdin^  ia''bBßyam  aitJ'  ''i'aiii ha'ä  paruviyata''  amäxam  taumäya  aha Bh./.i2;  —  '^'am  tyJ" ..paräbarfam  aha^ .  .patipadam  akunavam  Bh.  /.  1 4.  ||  2)  im jAw.T  uparäi  amäi  .  .  v»r?'hrSi  ..  °%räi A.  /.  8;  —  '%rakela  paiti  bäiiumais  dan- yayasca  paiti  darr^S.jXtSiS  Yt  y.  135; —  ''%r)mca  paiti.astlmca  darrfö.xsa^rfin "'hrahe  darr^5.j.ttJm  ustanahe  A.  /.  8;  — yim3  asti  hr.?>e(s6.}  '^rayä  (GD,)  V.  2. -  ^ahmi  '>re  Vr. /^_2(P);  P.  2^; — yimahe  °&re  nSit  aotftn  SnHa  .  .  yavata xsaySit  (sd.)  . ,  "unter  Ks  Herrschaft  .  ," Y.^.j;  V.2.S; — yim?m  . .  ye/'jhe  ''^rula .  .  nöit  aottm  fff»ha  . .  para  ahmSl  yat . . Yt.  IQ.  33 ;  —  yimS  . .  yat  kirmaot  aiähe '"ifräha  *amarsanta  pasu  vira  Y.g.  4;  Yt 15. 16; — Auxsa'hrS.ttmaiät  al  ""kmin  äfyai A.J.6;  —  zard^ustrim  ..ya^  as  ..*%rfm huxsa^rJ.ümS  (sd.)  \t  1^.79;  A.^.4,  Vs. 5^_j; —  'ir.lt  xsayamiia  VytJ5;  — yal^a anyhsBt  ""^räl  xlayamnä  hatnö-xiahrS.- xiayamnS  Yt.  J5.  54;  —  As  araHwya  '"^ra nsit  xiayeti  Vyt  47;  —  us  nü  atühäi  vJse jamyäl  asimea  "'hrsmca  savasca  .  .  Y.  60. 2;  —  zaraiiultrahe  ,  ,  paoiryai  hanhanuse gqrnifa  ahmla  .  .  uxüahyäca  (sd.)  i
@@@ BRT hya
5172:•  p.  avahya-rädiy  adv.-artige  Verb. 'aus diesem  Grund,  deshalb':  äspiU pit-ii  haxä- manil  .  .  av  haxamanisiyä  'itahyümahy Bh.  /.  3;  —  tyt^  manä  kartam  avaiii (sd.)  *aiava^  av  mä  apagaudaya'^  Bh. 4-10.  a)  mit  folg.  yai^a  'weil':  av <^urJ^mazdä  upaitSm  abar^  .  .  ya>il naiy  ar'tkt^  abavam  Bh.  4.13.  b)  mit folg.  («(7)  tyt^  'damit  (nicht)':  av  naiy nipislam  (sd.)  mütyt^  .  .  aj'ahyä  paruv *>adayä^  (sd.)  Bh.  4.8;  —  av  hlram avdjaniy^'  matyJ'mäm  xsnasätty  (sd.) (fffl*  ..  "deshalb  möchte  er  die  Leute  töten, damit  sie  nicht  .  ,'">  Bh,  j.  13.
25333:•  p.  *r^d-  f.  'ratio,  causa':  avahya-rädix {LS.)  sbes.
26296:•  j.,  g.  sah'*,  p.  ö-ah-*'  V.  'pronuntiare'. Praes,  i  saA-^'^  :  sai-*\  3  sSngAa-,  sar»ha-, ^aka-  (=  Sj-)»,  7  iqsah-^\  27  (Pass.) %ahya-T>.  —  PPfP.  'sas'ta-;  Inf.  %aslanaiy, °sastayai-ca;  Absol.  'saahim.
27896:hyak-  Sp.  1703- j,  zar^vahe  Vd.  13:  gemeint  ist  trlüakf.
28476:hyat  da  °Sb«J  (sd.)  mlzdavqn  yaca    ux'üä  nasuspacya  V. /.  16;    —    narsni    °ina   A.
@@@ BRT šim
19432:PPA,  einer  Basis  ir.  *maii-  'hervorquellen'; vgl.  np.  niaiTt/an,  mazidan  'saugen,  schmecken', sbaLmi<-Vsaueen'(usw.,  beiHBM.  PSL  137)'). —  Pü.:  transskt.  und  erl.  :/a  umar  eslel{aiso Fflanzensaft).  —  >)  Wegen  der  Bedeutungs- diflerenz  verweise  ich  auf  ahd.  iwrüait  'her- vorquellen'und  j;EiAi'sapor'DEW.,woznGsTllOFF rBtB.  8.  279  auch   ahd.  sim,g^  '»äugen'  «teilt.
```


## [2026-09-14T02:30:08.041Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ KNT hauv\"; grep -n \"hauv\" KNT_full.txt | head -15; echo \"@@@ KNT avahya\"; grep -n \"avahya\\|ava-hya\\|hya\" KNT_full.txt | head -20; echo \"@@@ KNT sim/sam\"; grep -n \"^šim\\|^šām\\|šim\\b\" KNT_full.txt | head -10"
}
```


### [2026-09-14T02:30:08.133Z] TOOL RESULT

```
@@@ KNT hauv
6473:haus, hauvam, haumavarga-, Vahauka-, but was 
7340:also hauv-maty hauv-taiy hauv-ciy. 
10206:written either hau- or hauv- (5137). The form hau- 
10210:ate hauv. 
12621:$263. Тнк DEMONSTRATIVE haww (once hauvam, 
16499:8 m : akunaus : hauv : dahy&um : P 
16509:14 adam : dárayámiy : hauv : patuy 
16626:29 à : hauvam : 1dà : xšāyaðiya : dha : avahyà : Kabüfiyahya : bra 
16636:36 sdva : І martiya : magus : dha : Gaumáta : пата : hauv : udapatatà : hacd : Рай 
16639:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 
16643:4] aSiyava : uta : Parsa : ша : Mada : uta : aniyà : dahyáva : xfagam : hauv 
16654:47 : Madam : uta : атуда : dahy&va : hauv : àyasatà : uvaipasiyam : акша : hau 
16751:74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 
16753:76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya 
16761:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 
@@@ KNT avahya
505:6165. Names of Months.................. 55 $198. The OP Relative and Article hya hyà 
532:$180. The Case-Endings of -й- Stems in pIE ndhyatt, йтїшаң)................ 72 
2051:hya : imam : lacaram : 
2502:[Uvára]zm'ya А?Р 8; Vahyav'Sdapaya Sd. 
2613:dahyau. _ 
2653:hya and hyd (Skt. syds syd), in which an 1 could 
2656:thus nom. masc. hya, fem. hyd, nt. tya; асс, 
2672:hita-; d'hyau% = dahydus, Skt. ddsyu-; hey 
2673:= hya, Skt. syds; рге ау" = part-barahy, 
2696:ату = abahiya XPh 18; elsewhere afahya. 
2707:copies of ХР]; elsewhere X Syahya. 
2890:атат; garma- in Garmapadahya, Skt. gharmá-; 
3021:Skt. ca; ттш уга = martiyahya, Skt. -asya. 
3033:dbharan; Му = hya for hyat, Skt. syds; ty? = 
3063:short passage (DB 3.38-51): Vahyazddtahyd 
3122:scription, when desirable: thus hyat, Гуа“, abara', 
3177:= XSyà XShya XSahya; but XS-chtya А1 2 Ж 
3530:güfavà DB 1.62f, ete.; dahyawā DB 1.34. 
3728:ahyá(yà) A*Sde 1 = ahyayà A’Sdb 1. 
3788:Artazšaçāhyā A'Sa 2 bis, for ArtaxSacahya (or 4 
@@@ KNT sim/sam
3141:singles: брт DB 1.95 = äpiš-šim, laumanisaiy 
6406:-Saiy -šim -Sém - 404 is generalized in the form 1 
7297:uld-taiy, uld-Saty, utā-šim, wlü-Süm, шщй-йї$. 
7469:-šim -šīm -&$, see S117. 
10144:I. Ace. -šim is the acc. of pIE *sf-, in the pAr. 
10154:person Av. bwat, Skt. 001; but in DB 1.50 -šim 
10156:gen. -šām were formed by analogy, though -šim 
12362:П. The enchties -šim and -dim and their forms 
12375:ence to kära 3.45. DNa 36f -&m refers back to -šim 
12377:bümim32. DB 4.5f -šim has the meaning ‘foe(s)’
```


## [2026-09-14T02:30:14.868Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10140,10160p' KNT_full.txt; echo \"@@@ 2650\"; sed -n '2650,2660p' KNT_full.txt; echo \"@@@ 12360\"; sed -n '12360,12380p' KNT_full.txt; echo \"@@@ 12621\"; sed -n '12618,12640p' KNT_full.txt"
}
```


### [2026-09-14T02:30:14.961Z] TOOL RESULT

```
$195. Tug Enciitic Pronouns оғ тне THIRD 
PERSON. 

I. Ace. -šim is the acc. of pIE *sf-, in the pAr. 
sandhi-form with š after final -¢ and -u (§117); Skt. 
sim has the long vowel; Av. him has pAr. h which 
is regular initial antevocalic, but the long vowel 
is not significant because ї is in Av. often written 
long before final -m. To -sim, the gen.-dat. -šaty 
was formed by analogy to Ist person -maty, 2d 
person -taty. The abl. -$a* was used only аз a 
suffix to ablatival adverbs; in form it is analogical 
to 1st person -ma', Av. mat, Skt. mát, and to 2d 
person Av. bwat, Skt. 001; but in DB 1.50 -šim 
functions as ablative. Pl. асе. -% (Av. М8) and 
gen. -šām were formed by analogy, though -šim 
was used also to refer to a plural antecedent. 

П. Ace. -dim (Av. dim), not differentiated in 
function from -5im, seems to have originated by 
@@@ 2650
pronoun and article tya-, always written ty- 
= fya-, and never #0" = tiya-. The reason for 
this is that the nom. sg. masc. and fem. were 
hya and hyd (Skt. syds syd), in which an 1 could 
not be written (§27); and the other forms, using 
the stem (ya-, followed their model in this point: 
thus nom. masc. hya, fem. hyd, nt. tya; асс, 
tyam lyam tya; etc. 

$26. PosTCONSONANTAL v was written -uv-: 
thus Логи» = harwa, Skt. sérvas; Puram = 
@@@ 12360
which may not call itself mine—that do ye smite’. 

П. The enchties -šim and -dim and their forms 
may have antecedents of any gender, and the 
singular forms may refer {0 antecedents of any 
number; for details, see Lex. s.vv. -Sa- and -di-. 

III. Plural pronouns are often used where the 
antecedent is ‘men’ implied in a preceding kara 
‘people, army’ or dahydus ‘province’ or the like: 
thus DB 1.65 -diš goes back to 64 kärahyä; DB 
2.19-21 -šīm in two occurrences and the two 
plural imperatives go back to kéram; DB 3.11f 
akunava"tà is plural by the meaning of dahydué, 
as are agarbdya” 3.48 and agarbaya” 3.49 by refer- 
ence to kära 3.45. DNa 36f -&m refers back to -šim 
36, denoting ‘men’ (cf. II, above) implied from 
bümim32. DB 4.5f -šim has the meaning ‘foe(s)’ 
by reference to hamaraná ‘battles’ (see JAOS 
85.844—50, 41.74-5). 

@@@ 12621
III. The generic article is discussed in §261.V. 


$263. Тнк DEMONSTRATIVE haww (once hauvam, 
DB 1.29) is either a pronoun referring to a pre- 
viously mentioned substantive, or an adjective im- 
mediately followed by its substantive, which is 
then sometimes explained by a relative clause (DB 
1.92; 2.66; 3.35, 54, 70). 

§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- 
larly either pronoun or adjective; it commonly 
refers to something already mentioned, but some- 
times has a forward reference, as in naimd ava 
ката tya tunuvd skaubars radiy miła kariyars ‘that 
is not my desire, that the mighty should have 
wrong done to him by the weak’ (DNb 10f; also 
DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, 
DSe 34, XPh 49, 51f). It has also the meaning 
‘yonder’ as applied to the sky: Auramazdà hya 
imam bümim ada hya атат asmdénam айй ‘Ahura- 
mazda, who created this earth, who created yonder 
sky’ (DNa 1-3, eto.).
```


## [2026-09-14T02:30:15.921Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ HRN leaf52 (p.31)\"; awk 'BEGIN{RS=\"\\f\"} NR==53{print}' HRN.txt | head -60"
}
```


### [2026-09-14T02:30:17.040Z] TOOL RESULT

```
@@@ HRN leaf52 (p.31)
— 31 —
Darmesteter's Erklärung (Et. ir. I, 75) aus
*apama' d. i. apa 4- ama- = lat. abemptum ist aus zwei
Gründen unmöglich: erstens weil die Grundbedeutung
von emö nicht ^kaufen*, sondern nehmen* ist (vergl.
lit. imü, ifriti nehmen', air. ein 'nehmen*, ksl. imq,
jpM 'nehmen'); zweitens weil lat. emö auch zu got.
tnman gehört, also seine Urform *^rwö lautet.
132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
(Jer. 51, 44).
ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
V. u.); Thron*.
ap. *avaranga- oder wohl besser '^abiranga- (vergl.
skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
134. euJzen (geschrieben evzen) 'tödtend*, in ser]ewzen
(Sahn. I, 100 Vers 714, 450 Vers 288), hezber\ewzen
(Sahn. I, 356 Vers 659).
aw. aiwi + l/^aw- 'tödten' ; phlv. afzatan (PPGL),
päz. awazadan.
Np. evzendlden der Wörterbücher ist nur eine gram-
matische gelehrte Bildung ; über die Emendation ewzen
vergl. Salemann-Shukovski, Neup. Grammatik, § 7
(dieselbe verbietet die Ableitung von ava-),
135. östUm, ustam 'treu, ergeben' (Vis und Rämin, Seite 78
Vers 12 1).
ap. ^avastaman- 'zuverlässig*, vergl. skr. ava-r
i/^sthä' 'bleiben, verharren*, avasthita- (von Personen)
'standhaft, zuverlässig*; phlv. östam bezw. tistäm
'Helfer (Men., vergl. awastäm, West ib.).
136. öi 'er, jener, vei,
ap. ava' + hya-; päz. öi.
*j Hier scheint es aber ^schwach* zu bedeuten.
```


## [2026-09-14T02:30:23.672Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ HRN leaf191 (p.170)\"; awk 'BEGIN{RS=\"\\f\"} NR==192{print}' HRN.txt | head -60; echo \"@@@ grep isan\"; grep -n \"ïsân\\|isän\\|īšān\\|isan 'sie'\\|awesän\\|avêsân\" HRN.txt | head -10"
}
```


### [2026-09-14T02:30:24.744Z] TOOL RESULT

```
@@@ HRN leaf191 (p.170)
— 170 -
Die Ableitung von np. Mm aus aw. ysäfniya-
(üarniesteter, Et. ir. I, 82, II, 161) ist sehr an-
sprechend, wennschon mir eine Grundform ^/sampHya-
nicht wahrscheinlich ist. Bei einer so starken Con-
traction konnte auch schliesslich der auslautende Nasal
noch in Mitleidenschaft gezogen werden, vergl. np.
Behräm gegenüber Varahrän; g. cum bei Beresine,
II, 24, VIII, 1 ist gewiss erst sekundär wie cübän
statt sübän (No. 776).
769. San 'ihr (Enclit.).
ap. sam (Enclit.) ; phlv. -^dn,
770. sdnzdeh sechzehn'.
aw. /svasjlasa 'sechzehnter ; phlv. säncdahiim ^).
af/. späras ; kurd. LW. säfizdeh,
np. sänzdeh ist durch das ihm vorhergehende pämdeh
beeinflusst.
771. smie 'Kamm'.
Käs. K. yö\sen (?).
phlv. sänak 'Kamm' (AV.); gr. xrf4', icrivinv (Hesych),
indog. he-n (Hübschmann, ZDMG. 44, 560).
bei. sak *Kamm' (445), dagegen LW. sänug 'Pferde-
strieger (866).
772. sah 'König, Herrscher, sähäne, sälü, sähin 'Falke'-).
ap. /ßäyadiya- 'Herrscher; päz. sah (PPGL), ^syäv
aaa, Ksoiiavöad (Agathias 261, 5, 264, 1).
Allgemein entlehnt (meist mit der speciellen Be-
deutung 'Perserkönig), wie auch säht (z. B. oss. d. sai
'Fünfkopekenstück', bei. säht 'Zweiannastück' (256);
dagegen in der Bedeutung *Landstrasse' in skr. säht,
Weber, Monatsber. BAW. 1879, 812).
778. sähensfih 'König der Könige'.
ap. yßäyad iyänäm ysäyadiya *der Könige König',
Vergl. Seite 128 Note 6.
^) * Sähen ^ vorgl. arm. LW. .^aJien.
@@@ grep isan
5759:g. izvFin (Käs. Q. ilzün ist natürlich arab. lisän).
7470:kurd. kisän ziehen'; af>'. k/dl; bei. kasay, n. /i'asay
7639:Dames: kisän, kisäin, kisänak).
8946:1032. niSästen 'sich setzen lassen', Praos. uisän-em,
8947:nisänden.
12294:Jisänden 102.
13152:nisänden 1032.
20501:kisänak 877.
```


## [2026-09-14T02:30:32.319Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ PHD ke\"; grep -n \"^kē \\|^kē$\\|kē \\[\" PHD.txt PHD_mackenzie.txt | head -20; echo \"@@@ PHD oy\"; grep -n \"^ōy\\|ōy \\[\\|awēšān\\|awē\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T02:30:33.369Z] TOOL RESULT

```
@@@ PHD ke
@@@ PHD oy
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:530:бу [OLE < A “l-h | M >zoy, N ~] he, she, that; (pl. awēšān).
PHD.txt:1574:desolate awérag, awērān.
PHD.txt:2481:invisible abaydāg, awēnišnīg.
PHD.txt:3390:report srawēnīdan.
PHD.txt:3487:ruined awērag, awērān, tabāh; be ~ tabāhīhistan.
PHD.txt:3974:they awēšān.
PHD.txt:3990:those awēšān.
PHD.txt:4555:jaw! Jawēnī šēwan frēst-Ī frēstādan? hil-t hilišnī hištanī šagr, šīr šīrēnīh šīrēn šēb šēb- šēbāg šēbišn šīšag šēdā šēd uzwānī šnāxtan šnāy- šnās- šnāyēn- šnāyēnīdan
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
```


## [2026-09-14T02:30:33.732Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ NYB oy\"; grep -n \"ōi\\b\\|ōy\\b\\|avēšān\\|awēšān\" NYB_vol2_glossary.txt | head -20; echo \"@@@ NYB ke\"; grep -n \"^kē\\|kē '\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T02:30:33.817Z] TOOL RESULT

```
@@@ NYB oy
@@@ NYB ke
```


## [2026-09-14T02:30:48.597Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ PHD MNW\"; grep -no \"MNW[^|]\\{0,80\\}\" PHD.txt | head -6; echo \"@@@ NYB MNW\"; grep -no \"MNW[^\\n]\\{0,120\\}\" NYB_vol2_glossary.txt | head -6; echo \"@@@ NYB OLE\"; grep -no \"OLE[^\\n]\\{0,120\\}\" NYB_vol2_glossary.txt | head -6"
}
```


### [2026-09-14T02:30:49.768Z] TOOL RESULT

```
@@@ PHD MNW
426:MNW < A mn-w 
@@@ NYB MNW
121:MNW<N>: (MN) haf‘el HAYMEN to believe
170:MNW: MANNU who?
671:MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. ž
787:MNW BNY-t (to one who built =) that it should be built. — KZSPrth 1. 16. 19 ’wpds$t, pres. *wpdys- ; MPrth *bdyst, ’bdys- ‘
1848:MNW hm mwd). — V. mod.
2126:MNW-8?n' ynšn' MN-#’n' = kē-šān janišn hac-isän is ambiguous: ‘those from whom slaughter had arisen’? (but haci$ would have
@@@ NYB OLE
```


## [2026-09-14T02:30:50.954Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 463 -l 463 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg463-v && ls -la pg463-v.png"
}
```


### [2026-09-14T02:30:52.615Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 62814 Sep 13 22:30 pg463-v.png
```


## [2026-09-14T02:30:55.385Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '424,430p' PHD.txt | cut -c1-600; echo \"@@@ NYB 2120-2130\"; sed -n '2124,2128p' NYB_vol2_glossary.txt | cut -c1-500; echo \"@@@ NYB ke entries\"; grep -n \"kē \" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-14T02:30:55.465Z] TOOL RESULT

```
kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd
kardan 5o kehtar
kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] ac
kem 51 k6Sk
kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] bod
kū(x)šīdan 52 laSkar
kē(x)šīdan, kū(x)š- [kz(4)$-ytn! | M htos-ydn, N kēšīdan) strive, struggle, endeavour. ~iSn: strife, combat. ~iSnig : energetic. Кбу [kwd | N ~] street, lane. ki [AYK < A’yk | M kw, N kū, hi] where; that; than, ~ Буар [N лија] where. ~ tā: so that. kūč(ak) [Awe(k!) | N kūčak] small. kak [kwk'] small, short. kulāčag [kwľck' | N kulīča] small, round bun. kulāf [kwl”5 | N kuláh] cap, bonnet. ~ak [-k!] | N ~hak] little cap; calyx. kulang [Ring | N ~] crane. kullag [kwlk'] locust. kumig [Awmyk'] stomach. kun-, -išn, v. kardan, kunišn. кар [STE < A *st-h; kwn
@@@ NYB 2120-2130
but we are here in a part of Iran where Greeks reigned for about 200 years after Alexander (v. Tarn, The Greeks in Bactria & India, 1951). There is every reason to believe that their kings and magnates erected monumental buildings over their tombs, with which the Yvy1 of the de- ceased was in some way connected. The Greek Yvx1 could, however, only be ren- dered in Iranian by jän, as the ruvān belonged to a quite different sphere. Prob- ably these seven jdnakdns were built in the seven cities w
jān-apispār [y?n! ’psp’l] v. s. v. jan.
janišn [ynšn'] the act of slaying 1018 (correct initial g- to y- with one dot be- low). — The NW form of zantšn, v. zatan. The passage is not quite clear. The text of the MSS: MNW-8?n' ynšn' MN-#’n' = kē-šān janišn hac-isän is ambiguous: ‘those from whom slaughter had arisen’? (but haci$ would have been the correct construction), ‘those of them (hac-ısän partitive, seems rather superfluous) by whom slaughter is done’ ? My emendation MRK*-n' = MLK?-’n' = $ähän: ‘those
kart ēstēt, cigön Dahäk u Frāsyāp u Väman [thus Cod. DH; TD w’tn', Paz. vätan, perhaps for Väöarjä the father of Vaman, Tab. I, 530 init.] u apārīk hac én āivēnak marg-aržānān, pātifrās [+ Paz. vama, probably a misspelt Vaman] 10 ātvēnak-ic vitārēnd ‘those who have in- stituted their own *laws for mankind, as D. and F. and V. and other death deserving men of that kind, will undergo ten sorts of punishment’. For the whole passage cf Phl Vd ad 75? (p. 279).
jànómand [y’n’wmnd] endowed with physical life 34%.
@@@ NYB ke entries
267:m-ic 5525-26; han katärcihe ke hac den ākāh, ~ 6716; har martom kē ..., ~-is 909; 5 kē.. up the thread of a narrative after a lengthy gualification: pas hac matani... —-išan 4018-19; 807-5; 871-2, — OP adakiy;
335:akah [’k’s] aware, knowing 39%, 574. 108?; ~ kartan to inform 10%, 11%; kē hac dén ~ he who is enlightened by Religion 6716; subst. pl. cas. obl. kam ~-Gn the ignorant, the witless 11077. — MPrs .g?
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
799:a-vinn [?wbyn'; ’wbn. PT 1664] not gaining, not winning: 1. of a p.: defeated 4215; ~ kartan to do away with 48°; — 2. of things: fruitless, wasted, lost 6814-20, 6922.27; — [kē (for ka) x"àstak xYart i pitar kart u handoat, i dütakän yāft, avinn (*wbn) būt šut ... when the fortune has been consumed that his father made and
895:bahr [b’hl] lot, share, portion 692°. 9019.11; (the part played by the priest in the service =) ministry 5319-1? (v.s. v. arzä- nikénitan), a synonym of yazisn (q. v.); this sense is confirmed by Zsprm XII, 6: Pourusäsp bahr o öi hilāi ke-š patiš aržānīkēh ‘P. shall leave the bahr to the one who has the qualification for it’, corresponding to (Pourusäsp...) yazišn 6 yastärän *hārēfūt (v. hareftan), with the gl. kū 6 yazāt kē apāyet yaštan 5314-15; — happiness, prosperity: tan ~ bodily beauty 22%, — Av. (923) baxadra-; Ps bhly; MPrth bhr ’*ate’; MPrs bhr (A-H I), h’mbhr "having the same share’ (A-H II); Paz. bahar, Skr. v. vibhäga and samrddhi; NP barx. [It would be tempt- ing to connect (čan) bahr with Skr bhadra- ‘beautiful, happy’; phonetically there is no difficulty, cf Skr mudrā: muhr ‘seal’ ; Av. baóra- is attested in hu-baóra- (1828) ‘happy’; thus Bailey in A. M., N.S. IT: 1, 1952, 32].
1074:ham-ic ham-ic 4271 (illogical co- ordination), kē . . . ké-c 5924 both... and (ké-c ... u kē-c 3918); -c . api-: pat-ic
1188:~ kē that 397?; with obj.: passim; with inf. to know how to, to manage to 5026.27, 511-2, — Av. (1659) zan-, OP dan-; MPrth z’n’dn z’n-; MPrs d'nystn d’n-; Paz. dä- nastan, dänestan dan-, NP dänistan. danišn [d'nšn'] knowledge 661, 803-5; ~ u kār-ākāhēh 881.23; m <u> xrat 4 martömän 10414; akahéh u ~ 1095, ~ u ākāhēh 111’. — MPrs d’nysn; NP dans. dānišnēh det. v. n.: uspurrikiha (q. v.) ~ 10615-16.
1294:1ditan [dytn'; HZYTN-tn', inscr. and Ps. HZYTN-] vén-, 2nd p. sg. HZYTN-yd = vënë 7164. HZYTN-h = venah 31°; subju. lst p. sg. HZYTN-n = vēnān P2: 10: to see, to regard, to catch sight of, to contemplate, to discern, to experience: ayāftan u ~ u dänistan 88°; dänäkıhä ~ 51; pat venisn ~ 5013-1; pat (xves) cašm ~ 7479, 80%; — with ki that 115. 127 ete., with ka that 40%; — with a pt. as its complement: -m murtak dit han tahm spähpat I saw this valiant general slain 2719-11; 2 zan nisastak dit 6"; with an adj. P2:10. 2719. 5776 sq. (purr com- ` plement); — with an indir. interrog. clause: ~ kū . . . cigēn to see how 2518-19; ka-t dīt kū kas kē ... kart 137-9 a contam- ination between ka-t dit ku kas
```


## [2026-09-14T02:31:00.781Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \".\\{200\\}MNW < A mn-w.\\{300\\}\" PHD.txt"
}
```


### [2026-09-14T02:31:00.835Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:31:02.833Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '426p' PHD.txt | cut -c1-1200"
}
```


### [2026-09-14T02:31:02.886Z] TOOL RESULT

```
kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] d
```


## [2026-09-14T02:31:06.137Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \".\\{120\\}who, which.\\{160\\}\" PHD.txt | head -5; echo \"@@@ PHD_mackenzie\"; grep -no \".\\{80\\}who, which.\\{120\\}\" PHD_mackenzie.txt | head -5"
}
```


### [2026-09-14T02:31:07.178Z] TOOL RESULT

```
422: householder, master of the house. kadām [ktm | M kd?m, N кийат) which, what. c--iz-é(w) [-c-H D] whichever. kadar [kt] who, which. 7-iz-é(w) [-c-H D] whoever. kaf [kp | N —] foam, slime. kaf-, v. kaftan. kafč [kpc | N ~] ladle, skimmer. ~ag [-А! | N ~a] spoon. kafš, ~ag [kps, -k! | N Аар]
426:of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), y
@@@ PHD_mackenzie
```


## [2026-09-14T02:31:14.915Z] TOOL CALL #31: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:31:14.922Z] TOOL RESULT

```


```


## [2026-09-14T02:31:18.324Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%87",
 "prompt": "Give the Persian entry for که (ke) — the conjunction/relative pronoun \"that, who\". Quote its etymology section verbatim, including Middle Persian form and Proto-Iranian / Proto-Indo-European reconstruction."
}
```


## [2026-09-14T02:31:19.806Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%88",
 "prompt": "Give the Persian entry for او (u/ow) \"he, she\". Quote the etymology verbatim (Middle Persian, Old Iranian, Proto-Iranian forms)."
}
```


### [2026-09-14T02:31:24.916Z] TOOL RESULT

```
# Persian Etymology of که (ke)

**Etymology Section Quote:**

"Merger of Middle Persian 𐭠𐭩𐭪 (AYK /⁠kū⁠/, "that", used for subordination to a main clause) with [Inscriptional Pahlavi needed]"

The entry indicates that که derives from multiple Middle Persian sources merged together. The documented source shows the AYK form meaning "that" used for subordinating clauses. However, the full etymological details for the other merged components are marked as requiring Inscriptional Pahlavi script notation, so complete Proto-Iranian or Proto-Indo-European reconstructions beyond what's shown are not fully provided in the visible text.

The page does note cognation with English "what" and references Proto-Indo-European *kʷís, *kʷós, but the specific Proto-Iranian intermediate forms are not explicitly stated in the etymology section.
```


### [2026-09-14T02:31:26.520Z] TOOL RESULT

```
# Persian Entry for او (u/ow)

## Etymology

According to the Wiktionary entry, the etymology is presented as follows:

"From Middle Persian [Book Pahlavi needed] (OLE), 𐭥𐭫𐭤 (ʿlh), 𐫀𐫇𐫏 (ʾwy /⁠ōy⁠/, 'he; she; that')."

The entry indicates a derivation from Middle Persian forms, though the Book Pahlavi script representation is noted as missing. The Proto-Iranian ancestry is referenced in related entries for cognate terms across other Iranian languages.
```


## [2026-09-14T02:31:32.299Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B4%D8%A7%D9%86",
 "prompt": "Persian entry ایشان (išān) \"they, he/she (polite)\": quote the etymology verbatim — Middle Persian awēšān, its analysis, Old Iranian/Proto-Iranian antecedent."
}
```


## [2026-09-14T02:31:33.330Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sofa",
 "prompt": "Quote the full etymology entry for \"sofa\" verbatim (Turkish, Arabic suffah, the root, and dates)."
}
```


### [2026-09-14T02:31:36.431Z] TOOL RESULT

```
# Etymology of "Sofa"

According to the Online Etymology Dictionary, the word "sofa" originates from Turkish _sofa_, which derives from Arabic _suffah_ meaning "bench of stone or wood; a couch." The term first appeared in English in the 1620s referring to "raised section of a floor, covered with carpets and cushions" as an Eastern interior feature. By 1717, it came to mean "long stuffed seat for reclining."
```


### [2026-09-14T02:31:37.901Z] TOOL RESULT

```
# Etymology of Persian ایشان (išān)

According to the Wiktionary entry, the word derives from **"Middle Persian 𐭥𐭫𐭤𐭱𐭠𐭭 (awēšān, 'they')"**.

The entry traces this Middle Persian form back to earlier Iranian languages, though it does not explicitly specify the Proto-Iranian reconstruction. The documented lineage shows the term evolved from Middle Persian through to modern Persian, where it functions as both a third-person plural pronoun meaning "they" and as a formal/polite singular form equivalent to "he" or "she."

This etymological path demonstrates typical sound changes in Persian phonology, with the Middle Persian *awēšān* developing into the contemporary form *išān*.
```


## [2026-09-14T02:31:40.577Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Amazon",
 "prompt": "Quote the full etymology entry for \"Amazon\" verbatim — the Greek word, the folk etymology \"breastless\", the Iranian *ha-mazan- proposal, and the river name."
}
```


## [2026-09-14T02:31:42.240Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Amazon",
 "prompt": "Quote the etymology section for English/Ancient Greek Amazon (Ἀμαζών) verbatim: all proposed origins including Iranian *ha-mazan-, Beekes' Pre-Greek view, and the origin of the river name Amazon."
}
```


### [2026-09-14T02:31:45.047Z] TOOL RESULT

```
# Etymology of Amazon

According to the Online Etymology Dictionary, the word "Amazon" comes from Greek *Amazonēs*, likely from "an unknown non-Indo-European word, or possibly from an Iranian compound *\*ha-maz-an-* '(one) fighting together.'"

The folk etymology derives it from "*a-* 'without' + *mazos*, variant of *mastos* 'breast,'" leading to the legend that Amazons "cut or burned off one breast so they could draw bowstrings more efficiently."

Regarding the river name, it was "rechristened with this name by Francisco de Orellana, 1541, after an encounter with female warriors." Alternatively, "the river name is a corruption of a native word in Tupi or Guarani meaning 'wave.'"
```


### [2026-09-14T02:31:50.154Z] TOOL RESULT

```
# Amazon Etymology - Ancient Greek Origins

Based on the Wiktionary entry, here is the etymology section for the Ancient Greek Amazon (Ἀμαζών):

**From the source document:**

"From Middle English, from Latin, from Ancient Greek Ἀμαζών (Amazṓn); perhaps Ionian Greek pronunciation of Old Persian *hamazan- ("warrior"), as the Amazon women were known warriors."

The entry also notes a folk etymology: the word may derive from "ἀ- (a-, 'not') + μαζός (mazós, 'breast')", referencing the belief that Amazons removed their right breast to improve archery and spear-throwing abilities.

**Regarding the river name:** The document does not provide a separate etymological account for why the Amazon River received this name. It only mentions that Spanish explorer Francisco de Orellana named it after the mythological Amazons following a battle with indigenous peoples where women fought alongside men.

The entry contains a note requesting source verification for the Iranian etymology, indicating scholarly uncertainty about this proposed origin.
```


## [2026-09-14T02:31:59.582Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ KLN sofa\"; grep -n \"^sofa,\\|sofa, n\" KLN_1966.txt KLN_1971.txt | head; echo \"@@@ ctx\"; grep -no \".\\{0,60\\}sofa, n.\\{0,700\\}\" KLN_1966.txt | head -3"
}
```


## [2026-09-14T02:32:01.575Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ SKT\"; grep -no \".\\{0,40\\}SOFA.\\{0,400\\}\" SKT.txt | head -3; echo \"@@@ LKT\"; grep -no \".\\{0,80\\}[Ss]ofa.\\{0,400\\}\" LKT.txt | head -5; echo \"@@@ DEV\"; grep -no \".\\{0,60\\}SOFA.\\{0,500\\}\" DEV.txt | head -3; echo \"@@@ PHN\"; grep -no \".\\{0,60\\}SOFA.\\{0,500\\}\" PHN.txt | head -3"
}
```


### [2026-09-14T02:32:03.563Z] TOOL RESULT

```
@@@ KLN sofa
KLN_1971.txt:225652:sofa, n. — Turk, sofa , fr. Arab. ?iijfa h , whence 
KLN_1966.txt:35804:sofa,  n.  —  Turk,  sofa,  fr.  Arab.  stiffah,  whence also  It.  sofa,  F.  sofa.
@@@ ctx
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,700}
                        \___exceeds complexity limits
```


### [2026-09-14T02:32:14.638Z] TOOL RESULT

```
@@@ SKT
ugrep: error: error at position 81
][\x80-\xbf]*){0,400}
                     \___exceeds complexity limits


@@@ LKT
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,400}
                        \___exceeds complexity limits


@@@ DEV
ugrep: error: error at position 81
][\x80-\xbf]*){0,500}
                     \___exceeds complexity limits


@@@ PHN
ugrep: error: error at position 81
][\x80-\xbf]*){0,500}
                     \___exceeds complexity limits
```


## [2026-09-14T02:32:17.878Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '35802,35808p' KLN_1966.txt; echo \"@@@ leaf number\"; python3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=p.find('sofa,  n.')\nprint('leaf', p[:i].count('\\f'))\nprint(repr(p[i-200:i+300]))\nEOF"
}
```


## [2026-09-14T02:32:18.892Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in SKT.txt LKT.txt DEV.txt PHN.txt LAM.txt DOZ.txt; do echo \"@@@ $f\"; grep -n -i \"sofa\" $f | head -4; done"
}
```


### [2026-09-14T02:32:19.140Z] TOOL RESULT

```
sodomy,  n.,  unnatural  copulation;  bestiality.  — ME.,  fr.  OF.  (=  F.)  sodomie,  fr.  Sodome,  fr. Late  L.  Sodoma,  fr.  Gk.  SoSojjta.  See  prec. word  and  -y  (representing  OF.  -ie).
soever,  adverbial  suff.  —  Compounded  of  so  and ever.
sofa,  n.  —  Turk,  sofa,  fr.  Arab.  stiffah,  whence also  It.  sofa,  F.  sofa.
soffione,  n.,  a  jet  of  steam.  —  It.,  fr.  soffiare,  ‘to blow’,  fr.  L.  sufflare,  ‘to  blow  forth  from  below’, fr.  sub-  and  flare,  ‘to  blow’.  See  flatus.
soffit,  n.,  a  term  of  architecture.  —  F.  sofflte,  fr. It.  soffltto,  fr.  VL.  *sujflctus,  corresponding  to L.  suffixus,  pp.  of  sitffigere,  ‘to  fasten  below’, used  as  a  noun.  See  suffix.
soft,  adj.  • —  ME.  so  fie,  adj.  and  adv.,  fr.  OE. softe,  orig.  an  adv.  standing  in  gradational  rela¬ tionship  to  the  adj.  sefte,  ‘easy,  mild,  comfort¬ able,  gentle’;  rel.  to  OS.  sdfti  (adj.),  safto  (adv.), OHG.  semfti  (adj.),  samfto  (adv.),  MHG. senfte  (adj.),  sanfte  (adv.),  G.  sanft  (adj.  and adv.),  MDu.  sachte,  Du.  zacht  (adj.  and  adv.), G.  sacht  (adj.  and  adv.)  and  prob.  also  to  Goth. samjan,  ‘to  please’,  ON.  semja,  ‘to  shape,  com¬ pose,  arrange;  to  settle,  make  peace’. Derivatives:  soft,  adv.,  n.  and  interj.,  soft-en,  tr. and  intr.  v.,  soft-en-er,  n,,  soft-en-ing ,  n.,  soft- ish,  adj.,  soft-ling,  n.  and  adj.,  soft-ly,  adv.,  soft¬ ness,  n.
softa,  n.,  a  Muslim  theological  student.  —  Turk. Sofia,  fr.  Pers.  sukhtah,  lit.  ‘lighted,  burning', pp.  of  sukhtan,  ‘to  light,  burn’,  here  used  in  the sense  ‘to  glow  with  enthusiasm  for  the  truth  of religion’.
@@@ leaf number
leaf 779
' fr.  OF.  (=  F.)  sodomie,  fr.  Sodome,  fr. Late  L.  Sodoma,  fr.  Gk.  SoSojjta.  See  prec. word  and  -y  (representing  OF.  -ie).\nsoever,  adverbial  suff.  —  Compounded  of  so  and ever.\nsofa,  n.  —  Turk,  sofa,  fr.  Arab.  stiffah,  whence also  It.  sofa,  F.  sofa.\nsoffione,  n.,  a  jet  of  steam.  —  It.,  fr.  soffiare,  ‘to blow’,  fr.  L.  sufflare,  ‘to  blow  forth  from  below’, fr.  sub-  and  flare,  ‘to  blow’.  See  flatus.\nsoffit,  n.,  a  term  of  architecture.'
```


### [2026-09-14T02:32:20.286Z] TOOL RESULT

```
@@@ SKT.txt
6376:fast  (3),  to  abstain  from  food.  (£.)  A.  5. fiTf/dH,  orig.  to  moke  fast,  observe,  be strict :  from  fast  (above).  -4-  Du.  vastiH. Van./aj/t,  Swed.and  \cc\.fasta,  O.fasttn. ^^^^  (3)>  quick.  (Scasd.)  A  peculiar use  of /ai/  (i)  above;  this  use  is  Scnnd. Cf.  Iccl.  drtkita  fast,  to  drink  hard,  sofa fast,  to  be  fast  aalecp,^^/r  /  vrrkum^  harti
12912:a  low  fluffed  seat.  (F.-Turk.) u,  ait  olloman.  sofa.  — F.   0/fo- rkivh.     So  named  from  Othman founHrr  of  the  Turkish  empire. 'TTouch,  the  socket  of  a  precious lament.  (K.  — O.  H.  G.>     Usually I,  yet  ncuiK  it  the  tnie  form.     M.  K. H^«0.  y.   nemhtt    ncsche,  nuscht,    a ^^bup.  bracelet  (Bur^y);  Lx)W  L. ^Hl.  H.  G.  nmkt,  O.  H.  G.  nauriz, IBw,  clasp,  brooch kCbt  (1).  pt,  t.  of  Owe.  q.  t. \%h%  (a).  ;!--•'---     ^rcOne. Uioe  (t\  :  of  :i  pound.  (F.
17672:SOFA.
24027:Syas,  11  nestling.  (F.— L.^  For  nias  \ due  to  pyiuing  OM  rynj  (or  a  uias.^V.  Hiais^ anesiUng:  Cot.  He al50give5«ian/,  whence fauUon  ntarti,  *  a  nias  falcon.'  Cp.  Ital. nUiace,  or  nidasofaUont^ '  an  eya£e-hawk, a  young  hawk  taken  out  of  her  nest ;'  Tnr- riano.  Forroefl  as  if  from  Low  Lat.  nida- tcm*,  ace  of  nidax*,  adj.  from  L.  nidus,  a
@@@ LKT.txt
3175:'Ort,  wo  man  sich  setzt'  [vom  Vb, ka'ada  'sich  setzen,  niederkauern'  und Präfix  ma-  des  Ortes],  ebenso  tk.  niakad 'Ort,  wo  man  sich  niederlegt;  Stoff, der  das  Sofa  bedeckt';  hieraus  rum. tnacat  'Steppdecke,  Betlbehang'.  [Sain 54.    Löbel  EITAP  59.
3381:1464a.  Tk.  minder: [Kelekian  Kämüs  1231]  'Sofakissen, Strohsack,  Matratze',  eigentlich  im  tk. Hause  eine  hölzerne,  niedrige,  an  der Wand  befestigte,  also  unbewegliche,  mit Teppichen  belegte  Bank,  die  ringsum im  Zimmer  die  AVände  entlang  läuft. In  reichen  Häusern  ist  der  minder  oft mit  kostbaren  Seidenkissen  gepolstert; auf  ihm  wird  auch,  und  zwar  ganz
4370:'Ruhebank'  [vom  Vb.  saffa  'in  eine  Reihe stellen'];  hieraus  zur  Bezeichnung  eines gepolsterten  Sitzes  lür  mehrere  Personen it.  sofä,  frz.  sofa,  sopha,  sp.  pg.  sofd, rum.  sofa;  engl.  ndl.  sofa,  dtsch.  Sofa; russ.  sofa.  [DE  340.  Devic  DEt  210. Eguilaz  494.    ML  2025.
4802:N.  pr.,  Name  des  dritten  Kalifen  und  des Begründers  der  türkischen  Dynastie  [Os- man  I.  1259—1326];  nach  dem  letzteren ist  das  Volk  der  Osmanen,  fi  z.  Ottomans, benannt;  nach  ihnen  heißt  ein  niedriges, breites  Sofa  ohne  Füße  und  Lehne  frz. Ottomane,  dtsclj.  Ottomane,  engl.  Otto- man.
@@@ DEV.txt
1305:Fagarier.  Genre  de  plantes  de  la  famille  des  xanthoxy- lées,  qui  tire  son  nom  du  fagar  a.  Le  fa  gara,  dans  Avi- cenne  [hMà  fâg-hara),  est  un  fruit  qui  ressemble  au  pois chiche  et  au  mahalep,  et  qu'on  apporte,  dit-il,  de  Sofala (aJLuJ!  ^-o  JctJrr)\  c'est-a-dire  de  quelque  endroit  de  la mer  des  Indes.  Le  voyageur  Linschot^  dit  que  ce  mol  dé- signe à  Java  le  fagarier  du  Japon.  La  lettre /n'existant  pas en  javanais  non  plus  qu'en  nmlais ,  fagara  ne  peut  être  un terme  de  ces  langues,  où  l'on  trouve  seulement  j^Li  pâgar, haie,  qui  paraît  être  étymologiquement  le  même  mot.
2134:Sofa  ou  Sopha.  Portug.  sofa.  De  l'arabe  iiÀ^  ^f^ff'h même  sens,  dans  Bocthor  et  dans  Gberbonneau,  scamnuni (Uscubitorium  dans  Freytag,  et  aussi  h  siêf^e  de  la  selle.
4331:Sofa.
4339:Sopha  ,  voy.  Sofa.
@@@ PHN.txt
9227:SOFA, ou mieux SOFFAT, s. m. (a.)
9232:et autres objets. — En France, sofa ne s'entend que d'un lit
9235:du mot sofa n'en est pas moins exacte. (Voyez le Journal des
9237:mère.) — Voltaire écrivait wpha, et sofa est l'orthographe que
@@@ LAM.txt
593:muphti, sofa, caphar, alphard, chérif, récif. Le fâ devient
820:conseil de l'empii-e, d'un sofa et d'un salon (Belot). De là, les divers sens
1078:en français. Il est souvent omis; ex. : sofa, cavas, chébec,
6749:passage à %joater aux exemples cités dans Dozj. Suppléni, s. ^j^ .224 SOFA
@@@ DOZ.txt
1117:Divan in den zin van sofa heeft Freytag ook niet,
1119:teekenis; zie Bocthor en Berggren onder sofa. Ham-
1962:en sofa (Barbarie); men vindt het ook als matelas bg
1985:mince et petit pour lessofas,^arraAa;Humbert, Guide y
```


## [2026-09-14T02:32:32.678Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (744,746,748,750,777,779,781):\n    print('=== leaf',i, repr(p[i][:150]))\nEOF"
}
```


### [2026-09-14T02:32:33.814Z] TOOL RESULT

```
=== leaf 744 ' n.  —  It.  scopo,  ‘mark,  target,  thing  aimed at,  aim",  goal,  object’,  fr.  Gk.  avoitoq,  mark  to shoot  at,  watcher,  examiner,  spy,  sc'
=== leaf 746 '  referred  to. scriptorium,  n.,  a  writing  room  esp.  that  of  a  mon¬ astery.  —  Late  L.,  prop.  neut.  of  L.  scriptorius , ‘pertaining  t'
=== leaf 748 'ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu.\nseaward\nsecure\ngesaete,  ‘seat’,  OHG.  gisdyi,  MHG.  gesiige, ‘seat;  siege;  situ'
=== leaf 750 "hol,  n.,  name  of  the  Heb. -Aram,  vowel  sign  ’.' —  Aram.  s(ghbl,  lit.  ‘cluster  of  grapes' ;  so  call¬ ed  from  its  form.\nsegholate,  a"
=== leaf 777 'e  *snab-,  ‘beak;  to  snatch  with  the  beak,  to snap’,  whence  also  Lith.  srtdpas,  ‘beak,  bill’.  Cp. neb  and  words  there  referred  to.\n'
=== leaf 779 'sociology,  n.  —  F.  sociologie,  a  hybrid  coined  by the  French  philosopher  Isidore  Auguste  Comte (1798-1857)  fr.  L.  socius,  ‘companion’'
=== leaf 781 '2)  single;  3)  lonely.  — ME.,  fr.  L.  solitarius,  ‘alone,  lonely,  solitary’ (whence  also  F.  solitaire),  fr.  solitas,  ‘loneliness’, fr.  '
```


## [2026-09-14T02:32:52.214Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in (748,779):\n    t=p[i]\n    print('=== leaf',i,'len',len(t))\n    print('HEAD:',repr(t[:60]))\n    print('NUMS:',re.findall(r'\\b1[0-9]{3}\\b',t)[:20])\nEOF"
}
```


### [2026-09-14T02:32:53.378Z] TOOL RESULT

```
=== leaf 748 len 12017
HEAD: 'ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze, '
NUMS: ['1583', '1408', '1409', '1866', '1924', '1866', '1927']
=== leaf 779 len 12027
HEAD: 'sociology,  n.  —  F.  sociologie,  a  hybrid  coined  by th'
NUMS: ['1798', '1857', '1468', '1469', '1778', '1829', '1736']
```


## [2026-09-14T02:33:05.571Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nt=p[779]\nfor n in ('1468','1469'):\n    i=t.find(n); print(n,'at',i,repr(t[max(0,i-120):i+60]))\ni=t.find('sofa,  n.'); print('sofa at',i)\nprint('len',len(t))\nEOF"
}
```


### [2026-09-14T02:33:06.749Z] TOOL RESULT

```
1468 at 1244 ". OIr.  socc,  W.  swch,  ‘plowshare’,  prop,  ‘snout’, which  are  cogn.  with  L.  sits,  Gk.  Cq,  oos.\nsocle\nsolder\n1468'\n1469\n‘swine’.  See  sow,  ‘female  pig’,  and  cp.  wo"
1469 at 1250 "  socc,  W.  swch,  ‘plowshare’,  prop,  ‘snout’, which  are  cogn.  with  L.  sits,  Gk.  Cq,  oos.\nsocle\nsolder\n1468'\n1469\n‘swine’.  See  sow,  ‘female  pig’,  and  cp.  words th"
sofa at 4522
len 12027
```


## [2026-09-14T02:33:06.950Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ KLN Amazon\"; grep -n \"^Amazon,\\|Amazon,  n\" KLN_1966.txt | head -3; echo \"@@@ WEB Amazon\"; grep -n -i \"Amazon\" WEB_vol1.txt 2>/dev/null | head -5; ls | grep -i \"^WEB\""
}
```


### [2026-09-14T02:33:07.037Z] TOOL RESULT

```
@@@ KLN Amazon
2409:Amazon,  n.,  a  member  of  a  race  of  female  war¬ riors  in  Scythia  ( Greek  mythol.)  —  L.,  fr.  Gk. ’A|za£d>v,  which  prob.  derives  fr.  Heb.  ammftz, ‘strong’.  The  form  of  the  word  ’Apatov  was prob.  influenced  by  the  folk  etymology  accord¬ ing  to  which  ’Apia^tov  lit.  means  ‘without breast’,  fr.  A-  (see  priv.  pref.  a-)  and  pa£6 ?, ‘breast’  (the  Amazons  are  said  to  have  cut  off their  right  breasts  in  order  to  use  the  bow  with more  ease).
2411:Amazon,  n.,  name  of  the  largest  river  in  the  world in  volume.  —  Sp.  Amazonas,  from  prec.  word; so  called  by  Francisco  Orellana  after  his  battle with  the  Tapuyas  (in  1541),  in  allusion  to  the circumstance  that  the  women  of  the  tribe helped  the  men  in  their  fight.  Cp.  next  word, amazonite,  n.,  a  green  variety  of  microline  (min¬ eral.)  —  Formed  with  subst.  suff.  -ite  from  the name  of  the  Amazon  River,  near  which  it  occurs, ambages,  n.  pi.,  a  roundabout  way.  —  L.  am¬ bages,  ‘a  roundabout  way’,  lit.  ‘a  going  round’, compounded  of  ambi-,  ‘about’,  and  ag-,  length¬ ened  form  of  the  stem  of  agere,  ‘to  move,  drive’. See  ambi-  and  agent,  adj.,  and  cp.  ambiguous. Cp.  also  amt,  ambassador,  embassy.  For  ag-, lengthened  form  of  the  stem  of  agere,  cp.  L.  in- dag  are,  ‘to  trace  out,  investigate’,  which  is  form¬ ed  fr.  ind(u)-,  ‘in’,  and  ag-,  lengthened  form  of the  stem  of  agere  (see  indagate).
@@@ WEB Amazon
6335:Am/a-z6n, n. (L., from Gr. Amaz6én; a priv., and mazos, breast. Derived by Greek folk etym. from the legend that the Amazons cut off the right breast to facilitate the use of the bow and javelin.]
6341:6. an Amazon ant.
6343:Am.-4a-z0/ni-an, a. 1. pertaining to or resem- bling an Amazon; hence, of masculine man- ners; warlike: applied to females.
6344:2. belonging to the River Amazon in South America, or to the country around it. am/a:zon-ite, n. Amazon stone.
6345:Am/a:z6n stone, a bright green variety of microlite, used as a gem, found on the banks of the Amazon River and elsewhere.
WEB_vol1.txt
```


## [2026-09-14T02:33:21.941Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ LKT 4370 ctx\"; sed -n '4360,4375p' LKT.txt; echo \"@@@ PLA suffa\"; grep -n \"ṣuffa\\|suffa\\|صفه\\|صفة\" incoming/PLA/PLA_pages.txt | head -5; echo \"@@@ AFM\"; grep -n \"الصفة\\|صفة\" AFM_pages.txt | head -5"
}
```


### [2026-09-14T02:33:22.044Z] TOOL RESULT

```
@@@ LKT 4370 ctx
'Ingwer,  Zingiber  olficinarum  Roscoe' [eigentlich  'horiiarlig' ;  so  sind  die  Wur- zeln des  braunen  oder  gemeinen  Ing- wers tatsächlich  beschaffen];  mit  Schwin- den des  vokalischen  r  wurde  ar.  zen- §ehll,  tk.  zingifre  sowie  gr.  Zi-fYißepn;, lat.  zingiber  und  hieraus:  iL  zenzovcro, zenzero,  gengioi-o,  aprov.  gingebre,  frz. gingembre,  kat.  gingebre,  sp.  gengibre, agengibre,  pg.  gengibre,  gengivre,  rum. ghimber,  zingifil,  zinzifil ;  ndl.  gemher, engl,  ginger,  dtsch.  Ingtver  [mit  Abwurf des  Anlautes  wie  bei  den  folgenden Formen];  russ.  imbir,  inbir,  klruss.  im- bir,  poln.  imbier,  jembier,  cech.  zätcor, serb.  dzendzefil,  dumbir  [über  ung. gyönibir'].  [Dozy  Oost  40/41.  Kluge 215/216.    Bern  SlEtWb  259.
1931.  Tk.  Staiubul:
N.  pr.,  Name  der  europäischen  Haupt- stadt der  Türkei,  auch  Istambul  [aus gr.  eiq  xäv  -nöXiv];  hieraus  serb.  stambol, russ.  stambulka ,  dtsch.  Stutnbulina 'schwarzer  tk.  Gehrock'.  [Gorjajew  342. Mikl  SlEtWb  320  a.
1932.  Ar.  snbät  :
'Schlaf,  Ruhe,  Lethargie'  [vom  Vb.  sa- bata  'ruhen',  gleicher  Wurzel  wie  Sabbat, s,  hier  Nr.  1742],  ebenso  tk  ;  hieraus poln.  (alt)  subet  'Zuflucht;  Lethargie'. [JVIikl  SlEtWb  328  b.    Karlowicz  422.
1933.  Ar.  siidd:
'Schleuse,  Wehr  an  einem  Flusse'  [vom Vb.  sadda  'versperren'];  hieraus  mit ar.  Art.  kat.  assut,  sp.  azud  'dass.' ;  aus dem  Einheitsnomen  sudda  wurde  sp. azuda,  pg.  aguda  'Wasseriad,  Noria'. [DE  229.    Eguilaz  32ö.
1934.  Ar.  süf: 'Baumwollstoff',  ebenso  tk.  sof;  hieraus rum.  zof,  sof  'Barchent'.  —  Das  ar.  Adj. süft,  also  'der  in  Baumwollkutte  Ge- kleidete' bezeichnete  den  Anhänger  des sog.  Sufismus,  einer  Geistesrichtung  im Islam,  die  das  Lebensziel  des  Menschen in  dem  Streben  nach  mystischer  Ver- einigung mit  Gott  auf  dem  Wege  der
Ekstase  erblickt  und  besonders  von  den Derwischorden  gepflegt  wird :  frz.  soufi, was  wir  heutzutage  etwa  'Theosoph' nennen  [Einwirkung  von  gr.aoqpöq 'weise' braucht  nicht  ausgeschlossen  zu  sein, wenn  es  auch  nicht  Grundwort  ist]; engl.  sofi.
1935.  Ar.  snffa:
'Ruhebank'  [vom  Vb.  saffa  'in  eine  Reihe stellen'];  hieraus  zur  Bezeichnung  eines gepolsterten  Sitzes  lür  mehrere  Personen it.  sofä,  frz.  sofa,  sopha,  sp.  pg.  sofd, rum.  sofa;  engl.  ndl.  sofa,  dtsch.  Sofa; russ.  sofa.  [DE  340.  Devic  DEt  210. Eguilaz  494.    ML  2025.
1936.  Ar.  sufr:
'Messing'  [von  asfar  'gelb';  über  die Form  des  ar.  Wortes  vgl.  FLEISCHER u.  DOZY  in  BSAW  XX,  285];  hieraus [oder  aus  einer  westarabischen  Form sufar,  die  in  Spanien  gebräuchlich  war] mit  ar.  Art.  sp.  azofar,  pg.  agofar  'dass.'. [DE  227.    Eguilaz  323.
1937.  Ar.  sufra :
'Niedriger  Speisetisch',  ebenso  tk.  sofra 'dass.',  eine  manchnial  ziemlich  große, runde  Platte,  die  auf  einen  Schemel, kürsi  [s.  hier  Nr.  1 1 90],  oder  ein  ent- sprechendes einfaches  Gestell  gelegt, erst  unmittelbar  vor  dem  Gebrauche  in das  Zimmer  gebracht  wird  und  im  orien- talischen Haushalt  als  Eßtisch  dient; hiei  aus  rum.  sofra  'dass.',  sofragiü  'Ta- feldecker,  -diener',  sofrageiie  'Speise- zimiiier'.
1938.  Tk.  sug-iik:
@@@ PLA suffa
@@@ AFM
2757:الفروق :« وعلدىي 0 الكقر ܥܰܪ ܨ الرومي 21 وهو صفة علد الروم لا ܐܕܒ الل ( ܚܝ
```


## [2026-09-14T02:33:23.770Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ MON soffe\"; grep -n \"صفه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5; echo \"@@@ BQT v2 صفه\"; grep -n \"صفه\" BQT_v2_pages.txt | head -5; echo \"@@@ FSD vol4 sofa\"; grep -n -i \"sofa\" FSD_vol4.txt 2>/dev/null | head -5; ls | grep FSD"
}
```


### [2026-09-14T02:33:23.898Z] TOOL RESULT

```
@@@ MON soffe
MON_part2.txt:21258:اصبهانی (اصفهانی): (پز.) سولفورانتیمون را 
MON_part2.txt:32261:اصفهان. گز علفی: ( کْیا.) شک رک درخت 
MON_part2.txt:32280:انواع دارد. کز اصفهانی: نوعی شیرینی که 
MON_part2.txt:32344:معادل ۲ بهر است. گز شاه اصفهانبه: واحد 
MON_part2.txt:32360:اصفهانمه (تاریخ قم. ۵ ترکیات فعلی: 
@@@ BQT v2 صفه
42:         ‫عضو وزارت فرهنگ ( لغات اصفهانی )‪.‬‬        ‫نی)‪.‬‬
1497:     ‫دوم‬   ‫دوم ول مسجم البلدان قربهاست از اصفهان " ولف در فهر ست خود جز ( که‌گاه سشدید‬
3572:   ‫ترجمه محاسن اصفهان باحتمام عبای‌اقبال ص‪ ۵۱‬سمد؛ ورك ‪ :‬فهرست همان کتاب ومعجم‌البلدان‬
7084:                                                                  ‫در لهج اصفهان هنوز معمول است‬
9384:   ‫است ولعاب بسیاردارد د کل کلاب»‪« »۰۲‬خا کشی‌بلت اصفهان» اسم خبه است» ‪#‬تحفةحكيممۇمن›‬
@@@ FSD vol4 sofa
377:dle.w,7(0)-s  ‘plllng.n  Asaddle-plk  Sccpile-s  .pin,  s^d'  free",  1   sad'-trl',  2   eSd'-tre  ,   n   Same  as  moht-jas- n   ApUot-plnconnectlngthosaddlastothesprlngsofaloco-  ,   «   Isvndiv^I
5440:3.  A   covering,  as  of  tapestry  or  leather,  for  the  back  of  an  compound  (CnHisOO  contained  m   various  oils  as  castor-oil, article  of  furniture  as  a   sofa  or  a   chair  2   A   frame  form-  It  Is  obtained  by  distillation  with  a   caustic
5443:ter  s   *clarf  —   s   -fastener,  n   A   screw-clamp  for  fast- ening a   scat  of  n   V   ehlcle  to  the  body  —   s   Oockey,  n   An upper  flap  on  a   saddle  —   s.dock,  n   The  lock  of  a   rev  erslble car-seat  — s   *mongcrIng,  n   Trading  in  parliamentary scats  —   s.  of  war,  the  district  where  war  Is  being  carried on— s.irall,  n   A   crosspiece  between  the  legs  and  Im- mediately' below  the  seat,  as  of  a   chair  or  sofa  —   s.fstand,  n A   wooden  or  metal  frame  supporting  that  end  of  a   car-seat which  Is  next  to  the  aisle  —   s.«stonc,  n   Same  ns  a   vmster
5448:anas  —   to  hold  or  Keep  one’s  s   ,   to  remain  seated,  also to  keep  one  a   position  aa  a   member  of  Parliament  —   to take  a   back  s.  (Colloq  ],  to  occupy  a   subordinate  position —   to  take  one’s  seat,  to  take  tbe  sitting-place  assigned  to one  also,  to  assume  an  ofllclal  position,  as  in  Congress ficat'ago,  1   sit'd,  2   sCt'ag,  n   IRarc)  Seating  capacity ficat'er,  l   sit'ar,  2   sCt'cr,  n   Iltare]  1.  An  usher  2.  A vehicle  with  a   certain  number  of  scats  used  only  la  com- bination, as  a   two-,  three-  or  four-irafer seath,  1   sifh.  2   sCth  n   Thecoalflsh  sethett  sUhet. scat'jng,  1   slt'iJ),  2   set'ing,  n   1.  Tbe  act  of  placing  on or  providing  with  a   seat  or  seats  2.  Any  fabric,  as haircloth  or  plush,  for  upholstering  seats,  as  of  chairs  or sofas  3.  Mach  A   fitted  support  or  base,  as  a   cast- iron  bed,  a   scat  4.  That  part  of  a   ahip^s  frame  which rests  on  the  keel
7904:ormerly,  a   seat  at  the  end  of  a   long  sofa  separated from  the  mam  body  by  an  arm  or  projection,  as,  a   sofa w   ith  tw  o   [Var  of  settle,  n   ] —   set-tee'*bcd",  n   A
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
```


## [2026-09-14T02:33:35.426Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg463-v.png"
}
```


### [2026-09-14T02:33:36.036Z] TOOL RESULT

```

```


## [2026-09-14T02:33:36.017Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:33:54.147Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v1_pages.txt; echo \"@@@ tags\"; grep -c \"pdf page\" BQT_v1_pages.txt; echo \"@@@ search او entry v1\"; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in range(405,422):\n    s=t[i][:300].replace('\\n',' | ')\n    print(i, s[:260])\nEOF"
}
```


### [2026-09-14T02:33:55.411Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
@@@ tags
0
@@@ search او entry v1
777
405 کردن باشد و آلرا بعربی جارت خوانند که | کتاخی باشد ؟ . | اوستاك » بر وزن نوشباد ۰ داننده | و آموزانند علمی وعملی‌بود ازامورکلی‌وجزئی ۴ . | اوستام - بانانی مجهرل و سکون‌ميم؛ | پراق زین و لجام اسب را کویند - و مردم | معتمد واعتمادی را ند کنته انه ۴ - و بمعنی | آ
406 ی | وساحران‌را بجهت سول مفاسد. خود ورلم کردن | جانوران - و حیله و تروبر را یز کفته‌اند . | اور سه شم اول بروزت بوسه ۰ بمعنی | دبودن و دبایش و ربایندکی باشد.» و باینمعنی | بفتح اول حم کفتهاند . | اوسیموی « بح اول و سکون تانی | بلفت بوفانی دوابی است که آنرا تودر
407 ٩ لب‎ | است که در مقابل حنیش باشد ءو اوج معوّب | آدت . | او کاد (۱) ۰ بروزن و ممنی اقدر(0) | است که جراحت بشت چاروا بلشد - و زمین گیر | و اماننه و آزرده را نز گویند ؛ و بابددانت | که در لت فارسی چنانکه بای ابجد بواو تبدیل | می‌بابد فای سعفض یز تبدیل مییابد چنا
408 اومالی | بالف کشیده و لام رسنه ۰ ۳ | انت که دهن‌السل تافو .۱۱ عل داود هم | کونند . گرم و تراست در چهارم . | او مان » بر وزن چوکان » قربهاٍست | ازفرای همدان » ومولدائیرالدین آتجاست ۱ 4 | او فك - بفتح اول و ثانی بروزن سمند» | ظرف وانا را کوبند ۴ - ویکوثانی جمعنی
409 ٩۸4 - | احریمه | اه - ختح اود و سکون انی : بسحنی آء | باشد و آن کلبه ات" که دود وفت اضوی | وحسرت گویشد. | اهاد ‏ بروزن هار : پالومه ای که بر | کاغذ و شوربای ی که بر جامه ماللد ٩‏ .* | اهر - بروزن بهر ۴ ان موضی است | از آ ذربایجان که رودخانٌ عظیمی دارد ۴ - ونام
410 اهزون | اهز ون - ختح اول بر وذن محزون » | بازاینده و متروترا گوبند وحربی عقیمه‌خوانند . | اهلث « بروزن مك . آحك را گویشه | و حربی کلس و نوره خواشد . | انامه - بر وزن شهنامه . بمعنی کر | وفر وخودآرابی و خودنمابی - و دولتسوعشق- | و رسوابی باشد - و عرچیزیرا نیز گ
411 ۱ اهور * - بنتع اول و ثالث و سکون | ثانی و زای نقطمدار ۰ نلم تیرآندازی بوده بفایت | قادرانداز در زمان انوشیروان » کوبند باسیف ذو | بزن (۱) همراه شده بود . بادشاه حبشهرابيك‌تبر | بر روی نخت کشت و ملکش راگرفت . | اهون - بفتح اول وثانی بواو رسیده | و ون زده ۰ مخف
412 ابا | جه 0 ده | ایا - بختح اول و ثالیبالف کشیده .بمعنی | و کاهی‌درمقام حسرت‌وافوی هم استعمال مشود . | ایاد - بروزن بهار . نام ماه سیم بهار | است ازمامرومیان » وبودن آفتاب در برججوزا- | و ترجه حساب هم هست چه ابار گیر محاسب | و حماب گیرنده را گونند ۲ | ایارده ۴ 
413 ۱۳ات ایدغ | ایاره گیر ۱ -بر وزن کنار هگیر ». | محاسب و نوبسنده را گویند . | ایاد ۴ ه بر وزن نماز , دام غلام تراد | سلطان محمود غز نوی بوده - | ابادي - بررزن لمازی » برقع سیاعی | ست که زنان بریشت چشم بندند ۴ . | " ایا ؟ « بروزن ممای » بمعنی ایاز | است که نام غل
414 ایا - بروزن وممنی زبرا و ازبرای‌آن | و از ایشجهت باشد . | ایر اف ۴ - بکر اود و سکون ثانی | و ثالث بالف کشده ویفای زده ۰ نام عدر اردااست | که پارسیان‌اورا پیعمبر | میدانتها ند و | ابسر آن ٩‏ - | بر وزن ببران . نام | هوشنگ ین سيامك | باشد - و ولاسته عرای | | بد‌
415 وه آبرسا | اول نیشاپور است ۷ . از پادشاهان بابل هم بوده است | ار ج ‏ بکسراول و سکون ثانی‌مجهول الیرسا « بکس اول و سکون انیوثاك | و #الك مقتوح بجیم زده ؛ نام پس فربدون است | و سین بی‌فقطٌبالف کشیده » بیونانی ۴ قوس‌رفزح | توا فلك آفتاب را یز کویند؟ . - وناییکی ر
416 و چون کل آن زرد و سفیدو کبود میباشدبنایر | آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح است . | بیوایی ٩‏ طلق و زر ورق دا کوبند و بثیرازی | برقك خوانند . | ایر قان - با قاف بروزن میهمان .بلغت | روغی حنا را کوبتد و آن ب رکه درختی باشد که | " یکوبند و خمی رکنند و بردست 
417 ایقفه ه با فا بررزن و معلی ابفده‌است | که بهوده گو و سبکار باشد که حرزه چانه | ۱9۳۳ | اون بکر او وسکون انی وفاف | بواو وسیده و بنون زده ؛ بلفت رومي کلی است | بغات بدیوی و کنده و بعربی‌وردالمنتن‌خوانند . | رنگ آن برنگ گل سرخ ماند . | ابگ ب بکسراول وسکون ثانی و 
418 ابلا | ومردمان و جماعت را نیز گویند - وهیل را هم | مبگوبند که له صفارباشد - و بکر اولوفتح | انی مشدد گا و کوهی باشد . گوشد چون سمار | شود بیتی خود را برسوراخ مارنهد و بنفم. مار | را بجاب خود کشد چنانکه مقناطیس آهن را , | چون مار را بخورد شفا بابد » و بعربی‌بقر
419 دنق | و نام ییت النفدس هم‌هست - وبسینی کوبند تام | عبت ان رت رادم کر از | فتحهایعبرخطاب. ومعنی آن‌سدیق اکبرباشد. | ایم « بروزن جیم » مردی را گوبند که | زنش مرده باشد ۱ . | ) ثمد ‌ِ بروژن‌ایسد .کاوآهن‌را گوبنده | و آن اعنی است که زمین را بدان شدبار کنند | و بمت
420 ایولز | ایو اد « بانانی مجهول بر وزن شیرازه | بمعتی آراسته و بیراسته باشه ۱ . | بسعنی ابواز است که آراسته و پیراسته باشد ۳ . | الوان ه بروز نکوان . صقه و طاق را | بند ۴ ,: | ابوانس بفتح‌اول وسکون ثانی‌وثالث | بالف کشیده و نون مکسود بین بی‌نقطةٌ ده .نام | شهری 
421 و شش لت و نات | بیان اول | با - , دمعم مع است که‌بجهت عصاحت | باشد - ویمعنی به بفتح بای ابجد - و مضاف به | اسامی آشها مانند ماست باوزیره با و کدوباوامثال | آن ۱ - و مخفف باد و باشد» هم هست . | بااوش « با حمزء بواو رسیده بر وزن | پاپوش » خیار بزرکی باش دکه بجهت
```


## [2026-09-14T02:34:06.455Z] TOOL CALL #50: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-14T02:34:06.505Z] TOOL RESULT

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


## [2026-09-14T02:34:14.825Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(395,415):\n    body=t[i]\n    hits=[w for w in ('پهلو','ضمیر','اوستا','غایب','اوی') if w in body]\n    if hits: print(i,hits)\n# print leaf 402-404 fully-ish\nfor i in (400,401,402,403,404):\n    print('==== leaf',i)\n    print(t[i][:1200])\nEOF"
}
```


### [2026-09-14T02:34:16.088Z] TOOL RESULT

```
397 ['پهلو', 'اوستا']
398 ['پهلو']
399 ['اوی']
400 ['پهلو']
402 ['پهلو']
404 ['اوستا']
405 ['اوستا']
406 ['اوی']
407 ['پهلو']
408 ['پهلو', 'اوستا', 'اوی']
410 ['پهلو', 'اوستا', 'اوی']
411 ['پهلو', 'اوستا']
412 ['پهلو', 'اوستا']
413 ['اوستا']
414 ['اوستا']
==== leaf 400
واجب و بفستا وا گیبتد و جر هی اهنت »
و آن‌قدارست ازسرانگشت ,کوچك ۷ مرانگشت
بزر که دست آدمی ۰
اوذست » بروژن بدست » بمعنی‌آودی
اس ت که وجب و بدست وشبر باشد .
و مدشه‌ایست .
ذاز شلمدار وسکون رای بی‌شطه ؛ بات بونانی ۷
آب را گویشد و مربی ماء خوائند .
آور » پم اول‌بروزن مور . بمعنی‌مشت
باشد عمواً و عشتی را گویند که بر دهن شخصی
زنند خصوساً - و بادام و پسته وکردکان وامثال
آ ها را یز گونندکه مغزشان نایم و یز شده
باشد . ۱
آودا - بختح اود و سکون تالی و ثالث
مالف کشده , حصار و قلمه راکوشد .
فراز وبالا و بلندی باشد ۴ .
آوداشتی - بر وزن و ععنی برداشتن
و بلند ساختن و افراختن باشد ۴ .
اوداهي » بن اول و فتم میبوسکون
تون بومی از خوانندکی و کونندکی باش دکه
آن خاسهةٌ فارسیان است و شعر آن بزبان‌پهلوی
باشد - و نام دهی‌است از مضافات وئوابم‌جونقان
مشهور باورامه رچوناین ضم کونند کیرا خخصی
)۱( ۳ : وادو 3
٩‏ ّ سونانی 0001 «اشتیشگاس».
۴ رد 1 آوردیدن ۰
ی نل ‌-
از خنیاکران آن ده وضم کرده بود بنابر‌آن‌به :
آورامن شهرت یافت ۰ ۱
اور امه با میم‌پروزن روزانه »بمعنی
اورامن است که نومی از کویند کی فارسیان‌باشد.
و للم دهی است از وابع جوشقان .
اوردیدن ۰ بح اول و نانی بر وزن
توردبدن» جنگه کردن‌وحمله نمودثرا کویند ؟.
اوردس بختح اول و کر ثانی وسکون
را و سین پی‌قطه » درخت سر وکوهی را کویند
و جربی عرعر خوانند ٩‏ .
اور شلیم ۱ 
==== leaf 401
ای ۸ اه
نیز خواشد ره ۳
اورمز ۱ نم اول و میم و سکون
وین ثالث و زای قطمدار . دام متارة
ی باشد - و فام روز اول است از هر صله
نيك است در این روز نو پوشیدن‌وسفر
کردن" و مهر بر کاغذ نهادن » و بد است قرض
و وام دادن - و نام فرشته ایست که تدییر لمور
اسفندیار هم هستِ که بسر بهمن باشد .
اودهز ۵ ۱ » پروزن روز دزد » بمعنی
اورمز است که نام روز اول از حرمله شمسی -
و نم ستار؟ مشتری -.و لام فرشته ای که موکل
ات تلم بسرزاده اسفندبار
اورمك « پروزن اوزيك , کلاموطاقی
پهمین‌را گویند,وسنی‌این‌لفت ران رکی‌میدانند ۴ .
آود نج - تال وثالك و سکون‌نالی
و نون و جیم » سکه الگور را کویشد و آرا
و جم ال و سکون انی مجهول » چوب خوشة
انگور باش که انگور آرا خورده بلشند ؛ وباین
معانی بچای حرف ثالث لام هم بنظرآمده است .
آورنگن
آود فحین - بر وزن فروروین » بمعنی
اورنجن امت و آن میلی باشد از طلا ونقره که
زنان بر (۱) دست و با یکنند .
اود فك ۲ ۰ بر وزن سوکند » مکر
وقریب و دفا وخدعه باشد - و + وی
حست که تخت پادشاهان است - و بممنی شأن
و شوکت و فر و شکوه و عظمت و ژیبایی وبها
لیز آمده است- و هم یکی از پسرا نکی‌پشین‌بن
و طالم و زیدگانی را هم گفتها ند - و رودخانةً
عظیم و بر رکه را یز کویندمطلقاً همچو رودئیل
ودجلةٌ بفداد واثالآ نپا ۵ - وبمعنی درباهم‌پشظار
آمده اس تکه بعربی جحر خوانند - و سیاهی‌را
یز کن‌ماند که در مقابل سفیدست .
اور ف
==== leaf 402
آوروختن
آود و ختن ه بروزن و معنی افروخئن
است. که روشن کردن: آنشس و چراغ باشد ۷ .:
آوده » بفتح اول و ثاكك وسکون‌انی »
بمعنی ابره است که روی فبا و کلاه و امثال ان
باشد, چه درفارسی با و واو بهم نبد بل‌می با بند ‌-
اور یا ۴ ه بر وزن بوربا» نام شخصی
است که داود علیه‌السلام او را بجنك فرستاد واو
۳ جنک کته شد و داود زن او را خواست
سلیتان عله‌الملام از ان زن بهم دسید ؛ ویسنی
گوند جد مادری سلیمان است و جمعی گویند
برادز داود عله‌السلام بود .
۱ اور لت هن اول و خفای نانی و کسر
الث و سکون تحتانی و بای ابجد» آنست که در
عربی محرف و بت رکی قیقاح گویند . *
"او رف هت یک ثات و سکون واو ؛
بروزن و معنی اوربباست که‌بتر کی‌قیقاج‌وبعربی
ایو < بانندید ثانی بر وزن هوزء نوعی
از مرغایی بزر که باشد - و مفتح اول و کمرثانی
و بکسر اول و انی هم آعده است؛ گوشد عربی
ی 9
اورار بروزن و ممنی افزار است که
بادبان کشتی - و دست افزارپيشه وران - و کفش
و با افر ار سوداروی کرم‌باشد مثل فلفل‌ودارچینی
. رك :افروختن . ۴ رد : اپره‎ ٩
یت
و زیره و غیره که در ذیگه طمام ریز تر6 ۰
اورایش بررزن ومعنی افزایش‌است
ععنی زباده شدن .
اون ك با زای فارسی بروژندوزن»
بمعنی انداز باشد که از انداختن و افکندن‌است.
و بمعنی فاعل حم صت که اندازنده وافکننده
باشدب وامرباین معنی‌هم آعده است یعنی بینداز
و بیقکن و قتل و کثش را نیز کونند که از
کشگن ماشد .
م
==== leaf 403
ی و ای
ع ‏ به ۷ ج جم حممي یه ۶" چا + ف ( ۲[ ج هو مه
۳ 2
۳
۱۲
۳ 5
۴ اه
۵اه
کدی نع
1 پدیم‌ر(ید._ | هرز | ع۴غطع | اصونل خدا ۳
۲ تس( ]ار ۱ 3
ری رکراه) رسد ایدا 2۶ | اعا ۹
ری و 4 پلاس ۳ -72] ]| جزه, فره ۹
او ص دویسم ای اوسعَة ید | اشم.خم ب
او رگشبه) وود اه | جرف ۳ 1
| زد رس طکه 6 یر فا ول دس ت نمسندا سین .حانه 9 اد
! دگرنای )ان (رش 8۱۳24 راست ,دست له 0۶ ) 5
یه 66 ند جرد جر نت اصعبعوق | رانا رورشد (ممدا) ع
ز وراه ورتم دملد او ارو 29۳۵ تعارز 0
ز (اراه ویر ات 4
آ و رکشده) [ید<6 ره وت و (وساة
او نهد (س تراد مهم | دم »بر _
ان ترسیری مس () نتم وحصگ» اند + صأنه
] (دیچن) ری زد خن ۱ ی 6
۹ 5 مند 6 مب کاعٌه هت ۳ ,کامه ۷
5 اعد اغق اماب | ج
خر ج ند ۵۵ ازیه خزفنه 9 ۷ چا
گر سید اه | ]۳۰۲ , 8
3 1 عو سع‌ندت ,یت )
ٍآ تسوا یسدنه اه هی ]| رایس | عم 5
۳ و 9 5 کر
م‌ ۲سدیج چش یم پسیدده 4
ح نسم لام نزو | ررف. گس ّ
۱ ۵۰ اد ۹
زد اک أوب؟ 4 ۰
رُ نل(د رنر 3 راو ۱
۱ یا (نید جد ت۳۳( سراه‌سگه قلة ره یام ](۸۵ه)1
==== leaf 404
اوستا
یه اثقبای اوستالی
7 ۳۹ فش کر 22۰
۷ ن نکددیین | زخش | ۵۷2۰۶
۳۸ ۲ ۱ وه | ٩۶2/42‏
و دهد اولام یمد ادن
|٩۹‏ :)| دیوید ابرخده | دک«دم
۳۰ 1 دا ز نت ۵ زرد اصه 3۶2
۳اه تب ۶۸ < 2 3:۳9
۳ ت‌ یه «دندیید روت | نووبد»!
۳ی| ب ارنود ایخه | رده
این و یمن رد | ۲۵۷دو
6۵ م نم(مد میت | 03۲۵۲۵
۰۹ ‌زری مود یره | دامجدلا
۰۷ د | , یه ده« |ردردم._ ندیه | دیدده
کلم ) 0
۳۸ 4 رِ (یری د دار ۷ را
٩یا‏ وزئی )| فاد ۵ نم ادف | ۷2۲2
۰ زد ۳ وا رک ره با ررید () ار 20۷2۲۵ط
1 م_
۱و | سس | وومهد .| ستو ۹
۲ | ش در | فاستد امه 1342
۴۳ دود ش رم زد ند( وپرمد هررشت4| ۱۷۵۴۶۰۵
۷ سم ۳ ترم سر ددبه ژد | صا رکه | ۱5۷992
س
شا رخا .
رهش
ضم
اف . او
بل
فروهر: مریرد
فك ۳ حدا
مر ۰ ‌
رن
مرو
۱ زد
--ٍ
ترس
برف
سر ژوهمزار)
سنورف
اد
کردارل
هلوت
چم و وه دج مان ک و هی مه من مب اب نم مها ما عح
```


## [2026-09-14T02:34:25.021Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,b in enumerate(t):\n    if 'ضمیر' in b and 380<i<430:\n        j=b.find('ضمیر')\n        print(i, repr(b[max(0,j-300):j+300]))\nEOF"
}
```


### [2026-09-14T02:34:26.109Z] TOOL RESULT

```
417 '» وین زای فارسی\u200cهم بنظر\nآمده است\nایژ لك - با نانی مجهول و زای فارسی\nبروزن مك » شرارء آتش راگوشد .\nایس - یکر اول و سکون ثانی و سين\nبی\u200cنقطه بالف کشیده . نام پیغمبریست ازییفمبران\nبنی\u200cاسرائیل ۱ و نام صحف ابراهیم علیه\u200cالسلام\nهم همست - و بمعنی این زمان و این دم والحال \u200f\nهم باشد ۴ 3\nایشان » بروزن خوبهان . ضمیر ات\nنسبت بذوی المفول حاضر بطریق تعظیم و جمم .\nند استسمال کنند ۴ . ۱\nابش » بر وزن و معنی بيشه و جتگل ا\nباشد - و جاسوی و چاپلوس رانیز کفتهاند ۴ .\nای\u200cشهر یار - نم درز سیام است از\nماهپای مذکی:- و خطاب بکلاشر وشهربار عم\nسصت\nمر 0\nوصف زنان است همچو بیبی و ب یبکه و ییکم .\nایقده - بکر اول و شم غین نقطه\u200cد'
```


## [2026-09-14T02:34:34.307Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[417])\nEOF"
}
```


### [2026-09-14T02:34:35.449Z] TOOL RESULT

```
ایقفه ه با فا بررزن و معلی ابفده‌است
که بهوده گو و سبکار باشد که حرزه چانه
۱9۳۳
اون بکر او وسکون انی وفاف
بواو وسیده و بنون زده ؛ بلفت رومي کلی است
بغات بدیوی و کنده و بعربی‌وردالمنتن‌خوانند .
رنگ آن برنگ گل سرخ ماند .
ابگ ب بکسراول وسکون ثانی و کاف
فارسی » ولاتی است است از ولابات فارسی 6
ایگ بادن هایگ معلوم. و بای ایجد
پالف کشیده و واو مفتوح بنون زده » نام کتابی
است در مذحب فان و ار ان درتتانن موباین
معنی‌بجای بای ایجد میم وبجای واو دال هم‌بنظر
آمده است وافاعلم 9
ایگر - بفتح اول و سکون انی و کاف
فارسی مغنوح بر‌ای فرشت‌زده ۰ درامی‌است که به
اکر شپرت دارد و عربی وج و بیونانی افارون
خوانند . سقید و سطبر و کرمدار می‌باشد .
ایل « بکر اوز و سکون نانی مجهول
و لام ؛ بلغت سربانی یکی از نامهای خدایتمالی
است جل جلاله ۷ و بزبان تر کی بمعنی‌دوست
و موافق و رام باشدکه نقیض وحنی است ۸ -
زده » جوال را گویند» وین زای فارسی‌هم بنظر
آمده است
ایژ لك - با نانی مجهول و زای فارسی
بروزن مك » شرارء آتش راگوشد .
ایس - یکر اول و سکون ثانی و سين
بی‌نقطه بالف کشیده . نام پیغمبریست ازییفمبران
بنی‌اسرائیل ۱ و نام صحف ابراهیم علیه‌السلام
هم همست - و بمعنی این زمان و این دم والحال ‏
هم باشد ۴ 3
ایشان » بروزن خوبهان . ضمیر ات
نسبت بذوی المفول حاضر بطریق تعظیم و جمم .
ند استسمال کنند ۴ . ۱
ابش » بر وزن و معنی بيشه و جتگل ا
باشد - و جاسوی و چاپلوس رانیز کفتهاند ۴ .
ای‌شهر یار - نم درز سیام است از
ماهپای مذکی:- و خطاب بکلاشر وشهربار عم
سصت
مر 0
وصف زنان است همچو بیبی و ب یبکه و ییکم .
ایقده - بکر اول و شم غین نقطه‌دار
بروزن سهده : بمعتی سیکسارو سهوده کوی‌باشد»
و باین‌معنی بفتح اول هم آمده است
۱ - ظاهراً مراد الیسع الیشع (عبری : خداوند نجات میدهد یامی‌بیند) واوشا کرد وجانشین
ابلیای نبی‌بود. رك: فاموی مقدس .۹۸‏ ۴ -کیلکی 292 (اکنون). ۳ - بهلری2۷65020
جمم 2۷6 (او, اوی) دنب رکهه۲» [رك : او]. ره : ص ,به ازديباچة مژلف. ۴ - رك : آبشه.
۵ - ۳ ایج(دارابگرد)«معجم»مولدندالدین ایچی.  ٩‏ -ظ مسخف «( که مادج» دراوستاائ و کمه-
د ثجا ۸086102026802 که رساله‌اییست دارای ۲٩‏ بند اوستابی و مجموعاً ۲۸۰کلمه . و ۱4۵۰
کلم بازند درآن آعده . رك : خرده‌اوستا ۸-۱۷4 ۱۷. ۷ - ابلمدش‌دلالت برقوموافتدار,
باسماء و کلمات عبری ملحق مشود » و استعمال آن‌مخصوص لفظ ای لت بلکه درمورد خدابان
مت‌برستان نیز ایشعمال یشود. «قاموس عقدس ۰۱:۲ ات 9 1 ابل بمعنی دست »
حردم ۰ ملت » گروه , سال ؛ «طیم وتابم است «جغثابی۱۲» و ابلات جسم معمول این کمه‌است .
۵ ایستادن - بنتم ششم . پهلوی 0ها 650 «تاوادبا ۲۱۹۶ «عنای ۲۲۷۳ ۰ ایرآنی‌باستان
2 - 2۷1 جزو اول بشوند وجزو دوم‌مشتن از )5 (500 لهج جنوب غربی) *نبر 45۵5 ۷»
در اوستا 562 (استادن) «بارنولمه ۲۱۹۰ » بمعنی برپا شدن , قیام کردن ؛ بر خاستن - متوفف
بقبه درصنحةٌ ۹۹۸
```


## [2026-09-14T02:34:55.977Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1230 2>&1 | head -60"
}
```


### [2026-09-14T02:35:04.245Z] TOOL RESULT

```
REF: BQT:1230  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 21  OCR-lang: fas

شاند -۱۳۰-
ایشان هم هت که شمیر جمع غایب باشد ‎٩‏ - شاه ۱ - بروزن چانه . معررفت‌وآن
ودر عربی ؟ بمعنی قدر ومرتبه وشوکت‌وعظمت | چیزی باشد که از چوب
- وحال وقکر واندیشه و کاروبار باشد - ۵ ۳ | وغیره سازند و بدان‌رش 9 اج
داشتن از چیزی دا هم کوبند کامي بجای وزلف و گیو راپردازدهند ۱11 7
لفظ حق هم‌گفته میشود چنانکه میگویند « این افزاری‌است جولاهگانر| "
آیه در شأن او دازل شده است» بعنی در حق او ۱ <-وافزاری‌است جوا هذالر
آمده اس که تارهای‌رسمان رااز آن شانه(سه‌قم)

وی نرانند بعنوانیکه در وقت بافتن دوتار یکجا
شاد * - بر وزن داند . بمنی زلت 1 را دا بان ۲2۵0
انس و پهلوی هم واقع شود - ریدم
وکا کل را شانهکند . و بمعنی شان عصل وخان ۳۵
شاندن « بر وزن ماندن » بمعنی شانه زنبور هم‌هست ۷ - وجست هم
کردن باشد ۴ - ومخفف ساندن و شالیدن هم | وخیز اسب راز کونند- سیر
هی 6 واستخوان کتف‌راهم‌میگویند. دی شم
شاناک - بر رزن نار4 , سنکه دان شاه سره حنعد شانه سر
وچینه دان مرغانر | گوبند . را گویند.» وآن پرنده است معروف ۸ .

۱- پهلوی هم 5028 - پارسی‌باستان 58217 «اسشق ۷۹۹. درفارسی «شان*م رکب
است از :ش 510 - ۳ پوند جمع‌آن 0 (نظیر : مان تان) «هوبشمان ۷۹۹ . رك: ص«4؛ از
دییاچهٌ موْلف . ۴ - (عر) «خان بالفتح » کاروحال . شئون‌وشان جمع ... وجت وجوی
وجستن ودربافتن وپرواً کردن ... و کردن کاری‌را که موجب خوبی‌ورولق حال وکار باشد وخبردادن»
« منتهی الارب» . درفارسی بجای شأن . 51128 تلفظ کنند. خاقانی‌شروانی درقصیدة شینیه پس از
پیت مذ کور درح ۰ صفحةٌ قبل کوید «دیوان خاقانی ۲۱۸ :

و کرچه‌نحل وقتی‌نوش بارد نیش‌هم دارد ‏ توآن منکر که اوحی ربك آمد وحی درشاش.

۳ - ر : شاندن.

۰ ۴ - جهان بآب‌وفاروی عدل میشوید فلك بدست ظفر جمد ملك میشاند .
آبوری آیوردی ۰ «فرهنگه نظام» ۰

ی بدسگال تو راحه دارد جان شانده در دل ز غ بپال از تو,

۰ سوزنی‌سمرقندی. «فرهنك نظام».

- پهلوی 512821 (غانه) . هند وژرمانی ( هندو اروپایی) 186-8 ۰ بلوچی 828
بلوچی ع 518808 (فعوی اسب) « امشق ۷۷۱ ۰ اورامانی 5128 ( دوش»شیب کوه ) 0
اورامان ۰۴۱۲۹ ۰ ۷ << شان(۶م.) . ۷ - پرنده‌ای از نوع كنجدك دارای منقار
باريك و دراز باندلم مارسیاه ودارای بکدسته در (بشکل تاج) برصر .۰

شانرده - بفتح دال » اوستا 4282 . 2511۷258 ,پهلوی 018 کردی 2

065 . (ن) در شانزده بقیای «پانزده» پدیدآمده «اسشق ۷۷۰ پازد 5202422 ,
بلوچی‌ع نیز 5132820128 هو بشمان ۰ کیلکی511082436 ؛عددی دو بر ابر هشت ,ده بملاوشش.

( برهان قاطع ۱۵۹ )
```


## [2026-09-14T02:35:29.232Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B5%D9%81%D9%87/",
 "prompt": "Quote the entries for صفه — especially the فرهنگ معین (Mo'in) section and the دهخدا section: meanings (سکو، ایوان، پیشگاه، زین) and any origin tag such as [ع.]."
}
```


## [2026-09-14T02:35:32.062Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%A9",
 "prompt": "Arabic entry صفة: distinguish ṣuffa (صُفّة) \"raised seat, bench, portico, saddle-seat\" from ṣifa \"attribute\". Quote etymology: root ص ف ف (ṣ-f-f), relation to ṣaffa \"to arrange in a row\", and any note about borrowing into Turkish/European languages."
}
```


### [2026-09-14T02:35:33.937Z] TOOL RESULT

```
# صفه Dictionary Entry

## Farhang-e Mo'in (معین)
According to this reference: "(صُ فَّ ) [ ع . صفة ] (اِ. ) خانه تابستانی سقف دار" — a roofed summer residence, with the etymology marked as Arabic (ع.).

## Dehkhoda Section
This dictionary provides multiple meanings for صفه:

- **سکو** (platform/dais)
- **ایوان** (portico/vault)
- **پیشگاه** (vestibule/forecourt)
- **زین** (saddle — referring to a rider's seat)

The entry also notes صفه refers to "an elevated platform within a room or mosque for seating," characteristic architecture in traditional Persian dwellings where the raised floor created a distinguished gathering space.
```


### [2026-09-14T02:35:39.410Z] TOOL RESULT

```
# صفة (Sifa/Suffa) - Arabic Etymology

The Wiktionary entry distinguishes two Arabic etymologies:

## Etymology 1: ṣifa (صِفَة)
Derives from root **و ص ف** (w-ṣ-f), related to "وَصَفَ" (waṣafa, meaning "to describe, to characterize"). This yields meanings including:
- Quality, feature, characteristic
- Grammatical adjective
- Word or phrase modifying a noun

## Etymology 2: ṣuffa (صُفَّة)
Borrowed from Aramaic **צִפָּא/צִיפָּא** (ṣippā), possibly from Akkadian roots meaning "mat" or "doorsill." Definitions include:
- "Bench, stone bench"
- "Sofa, sill, shelf, console"
- "Vestibule, anteroom, portico"
- Notably: "أَهْلُ الصُّفَّةِ" (the companions of Prophet Mohammed)

## Language Descendants
The second form particularly influenced Turkish and European languages—"صفه" evolved into Ottoman Turkish "صفه" (suffa, sofa), spawning English "sofa" and related terms in French and other languages.
```


## [2026-09-14T02:35:50.032Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/sofa",
 "prompt": "Quote the Turkish etymology entry for \"sofa\": Arabic ṣuffa, first attestation date in Turkish, and any note on the European loan."
}
```


## [2026-09-14T02:35:51.905Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A2%D9%85%D8%A7%D8%B2%D9%88%D9%86/",
 "prompt": "Is there an entry for آمازون (Amazon)? Quote any Mo'in (معین) or Dehkhoda text about the woman warriors and the river."
}
```


### [2026-09-14T02:35:53.277Z] TOOL RESULT

```
I cannot provide the requested etymology entry for "sofa" because the web page content provided only shows the header, navigation, and footer of the Nişanyan Sözlük website—it does not include the actual dictionary entry for the word "sofa" itself. 

To obtain the Turkish etymology information you're seeking (the Arabic origin ṣuffa, first attestation date, and European loan notes), you would need to access the full entry on the Nişanyan Sözlük website directly.
```


### [2026-09-14T02:35:54.165Z] TOOL RESULT

```
The server returned HTTP 400 Bad Request.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T02:36:04.246Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ HUB 769/šān\"; grep -n \"769\\|šān\\|san 'ihr'\" HUB.txt | head -15"
}
```


### [2026-09-14T02:36:04.300Z] TOOL RESULT

```
@@@ HUB 769/šān
2781:769. Np. 'Sdn aus -s + Pluralsuflf. an gebildet wie -wi5w,
```


## [2026-09-14T02:36:05.308Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ KLN they\"; grep -n \"^they,\\|^she,\\|^the,  definite\\|^that,  pron\" KLN_1966.txt | head"
}
```


### [2026-09-14T02:36:05.365Z] TOOL RESULT

```
@@@ KLN they
34910:she,  nom.  sing,  of  the  3rd  person  fern.  pron.  — ME.  scheo,  scho,  sche,  she,  fr.  OE.  seo,  sio,  fem. of  se,  used  as  definite  article,  orig.  a  demon¬ strative  pron.  meaning  ‘that’ ;  rel.  to  OS.  siu,  ON. sii  (fem.  of  sa),  sja,  ‘this’,  Du.  zij,  OHG.  siu,  si, MHG.  sie,  si,  G.  sie,  ‘she’,  Goth,  so  (fem.  of  sa), orig.  demonstr.  pron.  used  as  def.  art.  Outside Teut.  cp.  OI.  sa,  ‘she’  (fem.  of  sas,  ‘he’),  sya (fem.  of  sya),  ‘this’,  Gk.  I  (in  Sophocles),  ‘she’, )),  fem.  of  the  art.  6,  OIr.  si,  ‘she’,  OI.  sim  (acc.), ‘her’.
```


## [2026-09-14T02:36:10.584Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2775,2795p' HUB.txt"
}
```


### [2026-09-14T02:36:10.642Z] TOOL RESULT

```
gehalten werden. Ein *Kummet' ist ganz etwas anderes.
Bei uns scheinen diese 'Jochholzer nicht gebrauchlich
zu seln.
768. Afgh. Suma *nuit* finde ich nur bei Darmesteter,
Chants populaires p. XL. als altes LW. aus dem
Persischen.
769. Np. 'Sdn aus -s + Pluralsuflf. an gebildet wie -wi5w,
-tan. Vgl. WZKM. 7, 280.
770. Dazu paz. Sdnzdah Min. 61. 186, bal. LW. sanzdah,
Afgh. lies sparas.
774. Lat. queo ist noch etym. dunkel.
776. Lies arm. spet Np. iuban (Fird. I, 444, 178) oder
dopan (kaS. iepAn u. s. w.) ist doch von suban zu
trennen.
777. Aus *aiwiStap' ware np. ^afstap, arm. *austap geworden.
Das arm. LW. stap kann nur auf ein phi. §tap, istap
oder ustap zuriickgehen. Der von Horn angefiihrte
pehl. Infinitiv kann ostaftan oder ttstaftan gelesen
werden, da anlaut. D und u gleich geschrieben werden.
782. Nach F r. M ii 1 1 e r , WZKM. 8, 96 zu skr. ksud 'schlagen,
stampfen*. Aber die Bedeutung von np. Sustan ist
```


## [2026-09-14T02:36:22.960Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ HRN ke\"; grep -n \"ke 'dass'\\|ki 'dass'\\|^[0-9]\\{3,4\\}\\. ke\\b\\|ke,  'dass\" HRN.txt | head; echo \"@@@ WLD Bd2 509\"; python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,b in enumerate(t):\n    if re.search(r'\\bso\\(s\\)|sos\\b.{0,40}sā|Demonstrativstamm', b[:4000]):\n        print('leaf',i, b[:200].replace('\\n',' '))\n        if i>250: break\nEOF"
}
```


### [2026-09-14T02:36:24.192Z] TOOL RESULT

```
@@@ HRN ke
@@@ WLD Bd2 509
leaves 725
leaf 458 454                                  salo-    se-, sene-, sue>          lat.   saliva „Speichel“ (daraus entlehnt mir. saile, cymr.            Jialitv,   bret. halo ds., Fick II^ 291, Pedersen KGr. I
```


## [2026-09-14T02:36:27.727Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (512,513,514):\n    print('==== leaf',i)\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-14T02:36:28.820Z] TOOL RESULT

```
==== leaf 512
                                                                          ;




 508                                           selg     singho


^suelk- noch            in    ahd. swelahan,     sivelgan „schwelgen‘‘ (ware ,,einen guten
Zug haben,              einzieben“;       Zupitza Gutt. 161 zw. Uhlenbeck PBrB. 26, 308)
anzuerkennen, s. Falk-Torp u. svelge, Daher auch lat. sulcus nicht etwa
aus ^suelJcos, *sicolkos iind gr. xeXoov „Grenzfiirche‘‘ nicht nach Medermann
IP. 26, 45 aus '^siielkom umgestellten quelsom,


selg- „loslassen, entsenden, werfen, ausgie6en“,
      Ai. srjdti, sdrjati „entlaBt, schieBt, gieBt*', Ptc. srstd-Ji, vlsdrjana-m „Aus-
gieBung*^            {sdrga-h    „das Entlassen,      SchieBen,     GieBen“ mit g durch Ent-
gleisung; nicht zu sloYen. sraga „Tropfen“, Schmidt                               KZ. 25,115)      av. lidvd-
zaiti^        Jiarozalti     „entlaBt, sendet aus,     schickt aus“, Ptc. liardsta-, liardzUna-
n. „das Lassen, Verlassen; Durchlassen, Piltrieren*^
            f. „Jagd'' (vom Loslassen der Hunde, ai. srjdti cunaJj),
      air. selg                                                            acymr.
inhelcJia „Yenando*', helgha-ti ,.jage!‘' ncymr. hel, Jiela, helg ,,Yenari, aucu-
pari,        vestigare'',     corn,   helhia    „Jagen'',   bret.   hemolc'Tii       ds.   (Zup.    KZ. 35,
270 f.), ear. sleg (j^-slga) „Speer'^ (Pick II                  KG. I 100);
                                                             307, Pedersen
      mhd. selJcen st. Y. „tropfend niederfallen, sich senken, Yon Wolken“ (Ygl.
die ind. Bed. „ausgieBen“), ags. *a-scolcan „trage sein oder werden“, nur
im Ptc. d-solcen^ solcen „trage, faul“, engl. sulhg (Zup. G. 199, Pick III ^ 436).
   Der Yergleich der ar. Worte mit arm. zercanim ,,rette mich, entrinne,
fliehe^^ (Yorausgesetzt, daB z- Praefix sei, s. Hiibschmann Arm. Gr. I 440,
Pedersen KZ. 36, 289) und mit alb. derh sjgiefie              (Pedersen BB. 20,
238 a 2, doch KZ. 36, 289 aufgegeben) ist nicht Yorzuziehen.


selp- „Pett (Butter, Schmalz)'^
      Ai. sarpis- n. „Schmelzbutter, Sehmalz“, srprd- „geolt, glatt, blank‘d; gr.
I'htog (n.)      •
                     eXatov, orsaQ Hes.      und (mit (p nach dXei(pa         :   Xijtogl fragt Boisacq)
eXipog* povxvQov. Kvjrptoi Hes., oXtii], oXmg,                      „01flasche“; alb. Ts. G. Meyer
BB. 8, 192, Alb. AYb. 137, Pedersen KZ. 33, 549;                        36, 284) fjcdpe „ButteP';
ahd. salba,           as.   sa
==== leaf 513
                                                                                                                             -    ,




                                                                sindh(u-)       — soito-s                                                            509

sindh(u-) ,,FIuB*‘??
      Ai. sindlm-h                m. f. jjStrom, FluB                      ;
                                                                               Indus,           Indusland'*; av. ap.                       Hindu- m.
.,Indusiand, Indien“; kaum hierlier air. Sinainn, a. sg., Sinnae g. sg. .,der Shan-
Tion“. Fick II ^ 303*                  Ob von einem -> r?/i-Praesens zu2                                              si- „tropfeln, rinnen“?


so,     sa         ,,(5,          urspriinglicli                    nur nom.           sg.       m.   f.,   die            andern Kasus             vom
         Stamme to-,
      Ai. sd         und sdh^           f.    sa, av.           ha und ho,                f.   ha (auch in ai.                    c-ic?,    av.    ae-m
„dieseF*; mit Partikel                          -ti       ai.   a-sdu, av. hdu. ap. hativ                             ni.   f.    .,dieser,       diese‘\
vgl.     gr, oi’[Tog]);                gr.     d,     7
                                                       )
                                                              Artikel          (att.      usw.        auch           pi.    ol,       at   gegeniiber
alterem             dor. to/,          ral )   ;
                                                    substantivisch                   6g        {nal   oc,        7)6^ og)         aus      ^sos    (oder
      wozu sich n. d, acc. 6V,
^s'los)^                         usw. gesellte; ferner das zs. mit den
ro-Formen als Relativum gebrauchte dg bei Herodot; '^so-u-, sCi-u /s. 0 .)
in o?[Tog], av\rr}\\                   d-de „dieser*^;
      alb.    *50,         *5«
                           h-ii „dieser“. Jcejo „diese’‘ (^ke-o) und a-d .jille^^, a-jd
                                  in
,,illa‘‘ (s.    Pedersen KZ. 34, 28S; 36. 103, 282, 3l0ff.. Pron. dem. 13f.); alat.
>ia-psa       „ipsa'‘. sum^ sam^ sos, sas „eum, earn, eos, eas''; '"^so- in osk. exo-

„hic“        (z.    B. abl.
                   f. exac) aus H-ke-so- (zum Vorderglied s. u. ko „dieser“);
gall. .so-5m  noneton „hoc sacellum'\ air. (s)a n- neutr. des Artikels, und
Relativpronomen, s infigiertes pron. des 3. sg. f.
==== leaf 514
510                             songli(o-, -a),       sonqo-   —   solo-, sol(e)uo-



vergleicht OsthofF BB. 24, 158fiF. (wo                         ausfiihrliche Lit.)    ansprechend auch
gr. oifXYj „Lied, Gesang, Gedicht, Sage, Erzahlung^, oTfiog in der Bed. „Lied-
weise, Melodie‘‘ (auch           ohne die jon. Psilose iiberliefert), jiagotjuia
„Sprichwort“, nQooifxiov, att. q)Qoiixiov (^aus ngo-ol'iAiov^ „Liedanfang, Einlei-
tung“, aoijuov aQQtjTov Hes., mit zweifelhafterem Eechte auch ai. saman- n.
                   *




„gesungenes Lied, Gesang‘^ als ^so\i]men oder se[^]-mew- (ware entwederDehn-
stufenbildung, oder setzte schweren Wzvokalismus               voraus, so daS
europ. *soitos aus *5o#os); denn siXman- kann als „Zu8amnienfugung, com-
positio‘‘ zu samara „zs.“ gehoren (s. *sem- ,,eins‘' und vgl. dort zur Dehn>
stufe auch ai. saman- m. n. „gute, beschwichtigende Worte, Milde, freund-
liches Eatgegenkommen“ usw., mit deren spezieller Anwendung auf das
freundliche Beisammensein freilich saman „Lied“ nichts zu tun hat Uhlen-                         ;


beck Ai. Wb. 333).

SOiigh(o-, -a) Odersonqo- „Ahrenbuschel, Strohbuschel“.
  Arm. ung (gen. ongoy) „kleine Strohstiickchen; Bund Stroh mit einzelnen
in den Ahren zuriickgebliebenen K6rnern“; ahd. sanga „Ahrenbu8chel,
manipulus“, nhd. Sange^ Sangel „Ahrenbuschel“, engl. dial, sangle ds. Peters-
son KZ. 47, 267 fiir die Gdf. songho- sprache gr. a^vgov „Spreu“, wenn
                        ;


als     sngh- hieher,        doch       ist   dies    von seiten der Bed. nicht zwingend und
scheint a^vgov eher mit ax(og „Schorf, Grind“ auf eine Gdbed. „absplitternd,
spreuartig sich abschuppend“ zu weisen (iiber ayvrj „Spreu; Flaum, Schaum^'
s.   u. ak- „spitz'‘;       gegen Anreihung von ofjopa^ s. u. enebh- „Nabel“).

sora „Wade“?
   Bechtel 99 a. 1887, 69, GDI. 5497, KZ. 46, 161                            =
                                                       LexiL 80 iibersetzt gr.
aoygoi nodeg  fji 89 als „Beine ohne ^aden‘‘, da jon. wgg {^grj) nach dem
Scholion von Aristarch mit TccoXfj gleichgesetzt wird; aber in der milesi-
schen Inschrift GAI. 5497 wird die ojoj] der xcolij als verschiedener Kdrper-
teil („Yorderbug? Schulterblatt?'*) gegeniibergestellt, so da6 die Bed. nicht

feststeht;
     lat.               wenn mit -fir- aus -dr — s. Yf. LEWb.^ 757; dialek-
            sura „Wade‘‘,
tisch?        Sommer Hdb.^ 68                 —
                                  so — Sg7]: sonst wird Abl
```


## [2026-09-14T02:37:11.124Z] TOOL CALL #64: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T02:37:11.175Z] TOOL RESULT

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


## [2026-09-14T02:37:19.948Z] TOOL CALL #65: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%88' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B4%D8%A7%D9%86' \\\n 'https://www.etymonline.com/word/sofa' \\\n 'https://www.etymonline.com/word/Amazon' \\\n 'https://en.wiktionary.org/wiki/Amazon' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%A9' ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note 'page 463 (So/To; Soffeh) verification' 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:37:23.724Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c6ea997d74004944.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/614bd339191d4550.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a8c62b3aab2cfa7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8307f3689dfbd37.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4c27d25b1fb19db8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1e8ba26195a2e16.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5da9e7650db90f8a.txt
```


## [2026-09-14T02:37:28.862Z] TOOL CALL #66: Bash

```json
{
 "command": "timeout 120 python3 /home/sfmqrb/git/rishe/tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%B5%D9%81%D9%87/' --note 'page 463, Persian soffeh صفه, Mo'\"'\"'in + Dehkhoda entries' 2>&1 | tail -2; mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg463-v.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/463.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/463.png"
}
```


### [2026-09-14T02:37:31.184Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/52837ac4bab0ccd8.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 62814 Sep 13 22:37 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/463.png
```


## [2026-09-14T02:37:45.085Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ IEC\"; grep -n \"^so, sā\\|^so(s)\\|^sos,\\|^to-, tā\\|^tod\\b\" IEC.txt | head; echo \"@@@ IEC2\"; grep -n \"sos \" IEC.txt | head -5; echo \"@@@ SYN demonstr\"; grep -n \"Demonstrative Pronouns\\|13\\.1 \" SYN.txt | head -5"
}
```


### [2026-09-14T02:37:45.173Z] TOOL RESULT

```
@@@ IEC
16746:sos, f: sa ‘this; he, she’. Cf. so (sio-), ios. Extn. sosios, å. WP II, 509 Skt. sah, sā; Av. ho, hà; Hitt. cf. -as ‘he’; -an ‘him’, -at ‘it’; Tokh. A sas, B su, sà; Hitt. cf. sas “he; he who’; Arm. cf. ho-s ‘here’; ho-n ��there’; Gk. hó, hé, def. art. beside hos, hé, rel. pron.; OLat. sum ‘him’, sam ‘her’; SOS, sàs, pl. ‘them’; (Sard. su, sa, def. art. prob. fr. ipse); MIr. so ‘this; these’; cf. Ir. so-nn (‘here’, cf. Arm. ho-n ‘there’); Go. sa, sð, mf. ‘thi; ON sá, sú “that; the’. Extn. in Gk. hoíos, hoia, pn. ((such?. Ambig. cf. ios-); Av. hoyo *this'; Alb. ay, f: ajó “he, she’
18693:tod, neut. sg. of type tos, q.v. in Skt. tad; Tokh B te beside Tokh. A tám, tan; Hitt. tat; Go. cf. pata, otherwise *bat in Gmc.; ON cf. pat-ki, for *pat-gi (‘that not Cf. ghi); Li. tad, adv. ‘then’; cj. ‘that’; OAIb. cf. ké-tá, a-tá (with singular vb.): "(hat (Buzuk). Cf. WP I, 742
18695:todé, todo, todo, tod ‘then’. Cf. to- (tos, tod, tom) & dé, dó Skt. tadá, tad, id.; Av. taóa, id.; Gk. tóde, emph. prn. ‘this’; ON cf. þaðan, adv. ‘thence’; OCz. cf. tda ‘there’; tdy ‘then’; Ukr. cf. todi ‘then’; Li. tadà, id.; Latv. tad, id. WP I, 743 & 711
@@@ IEC2
389:āKsos (? oKsos) ‘keen, sharp, clear; keen- ness, etc? W awch ‘edge, keenness’; Cz. jas ‘clarity’; cf. the synthetic OCS cpd. jastrebü ‘hawk’, with part of the semantics of Lat. accipiter, id. The Lat. form ascia and It. azza indicate a short vowel. `
453:alkos, à, is, ios 'shrine, temple, grove. WP I, 90. Cf. aleks- Gk. álsos (grove, fr. *alkios), cf. also *alx, ds. alkí beside alké 'strength, safeguard, de- fence’; Go. alhs ‘temple’; OHG alah, OE eath, id.; Li. alkas *hallowed grove', alka *barrow, mound. Cf. Latv. elks (idol. Vocalism ob- scure)
1429:bhluksos ‘white, blank’. Variant of bhluskos, q. v. Cf. bhluk- Br. bluch ‘hairless’; Cor. blogh, id.; OCz. biščieti sé “flash”; Icel. blossa, v. ‘blaze’; blossi, m. Norw. blusse, id. (& “blush?); bluss ‘torch’
1822:bhrsos, ios, à, is ‘shag, tuft, bristles, fur. Cf. bhrstis Av. cf. boro$o ‘backbone’; Arm. bars (i-st. ‘horsehair, mane"); Gk. phársos (2) ‘cluster’; Phryg.? (LW in Gk.?) bürsa ‘rawhide, skin bag’; Lat. (LW or Gallo-Lat?) burra ‘shaggy garment’; re-burrus, adj. ‘bristly’, cf. also LLat. borr-àágo (“borage”, lit. *bristly plant"); variant (*bhors-) in Olr. barr *tree-foliage, spray’; Cor. bar (1) “bunch, tufted branch? beside Oir. barrán “head of hair; ME burre ‘burr’; Norw. Sw. borre, id. (Sw. also 'thistle- head, sea-urchin’); Cf. OCS brí$-ljanü *spindle- Dee beside Cz. brs-len, id.; cf. also Cz. brs- ina ‘grassy slope’. See bhors-
2204:dé-siqusos ‘dried up’. See dë, siqusos Lat. *desiccus (in desiccare); Ir. díosc “dried up, barren’
@@@ SYN demonstr
```


## [2026-09-14T02:38:26.545Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"@@@ PHN\"; sed -n '9225,9245p' PHN.txt; echo \"@@@ DEV 2134\"; sed -n '2132,2137p' DEV.txt; echo \"@@@ FSD4 sofa headword\"; grep -n \"so'fa\\|sofa,  n\\|so.fa,\" FSD_vol4.txt | head -5"
}
```


### [2026-09-14T02:38:26.634Z] TOOL RESULT

```
@@@ PHN
— Soda est un terme de pathologie dont on ne fait plus guère
usage aujourd'hui.
SOFA, ou mieux SOFFAT, s. m. (a.)
ajL4 [s'ouffat] estrade en planches, élevée d'un pied environ,
couverte d'un tapis et placée vers le fond d'un salon, chez les
Orientaux. Le même terme arabe désigne aussi une espèce de
tablette en marbre ou en pierre sur laquelle on place des vases
et autres objets. — En France, sofa ne s'entend que d'un lit
de repos à dosiner, d'un canapé, et cette signification est, sans
doute, un peu détournée du sens primitif; mais l'origine arabe
du mot sofa n'en est pas moins exacte. (Voyez le Journal des
Savants, cahier de janvier i848, p. 46, article de M. Quatre-
mère.) — Voltaire écrivait wpha, et sofa est l'orthographe que
l'on suit aujourd'hui; cependant la transcription soffat serait
plus régulière, puisque la deuxième radicale du mot oriental
est doublée , et que sa dernière lettre est un b t.
SOFI,s. m. (a.)
i^âQ l^'oûfy] vêtu de laine, adjectif dérivé de <jy^ [s'oûf] laine.
Ëpithète donnée à des religieux orientaux qui font profession
d'une grande austérité et ne portent que des vêtements de laine.Atlarb<^ à la vfp ronleroplative ei rejetant loole pratiqae ei-
U^rîeare de ruile, les $o/ls oo fw/C» consîdmnt Fanéantisse-
@@@ DEV 2134
210  DICTIONNAIRE  ÉTYMOLOGIQUE
Soda.  Ancien  ternie  de  médecine,  violent  mal  de  tête. De  l'arabe  ^î*Xo  sodâ\  même  sens,  qui  se  rattache  à  ^*>wo sacla,  fendre  en  deux.
Sofa  ou  Sopha.  Portug.  sofa.  De  l'arabe  iiÀ^  ^f^ff'h même  sens,  dans  Bocthor  et  dans  Gberbonneau,  scamnuni (Uscubitorium  dans  Freytag,  et  aussi  h  siêf^e  de  la  selle.
Solive.  Ce  terme  de  charpenterie,  dont  l'origine  ne  pa- raît se  rattacher  ni  au  latin  ni  aux  langues  du  même groupe,  offre  une  grande  analogie  de  son  et  de  sens  avec l'arabe  l^J^  salah,  salih ,  arbre  d'une  longueur  notable, et  <-^AkM  sahb ,  arbre  dépouillé  de  branches.  Est-ce  une pure  coïncidence?  Rappelons  que  l'art  du  charpentier  a emprunté  un  certain  nombre  de  mots  à  la  langue  arabe.
SoPHi.  ^^Le  nom  de  sopin  donné  aux  souverains  de  la Perse,  pendant  les  xvf  et  xvii'  siècles,  dit  M.  De^rémery^ doit  son  origine  à  ^^yu^  sefewi,  adjectif  relatif  ou  patrony- mique, dérivé  du  nom  du  cheikh  Séfi,  sixième  ancêtre  du chah  Ismaïl,  fondateur  de  la  dynastie  des  Séjis  ou  mieux Séfévis.  55  On  a  dit  soplu  sans  doute  par  confusion  avec  le terme  soufi,  ci-après.
SouFi.  Transcription  de  l'arabe  ^^ao  soiifi,  sage,  reli- gieux, qu'on  veut  tirer  de  Oy^  souf,  laine,  les  soufis  étant tenus  de  porter  des  vêtements  de  hiine  et  non  de  soie; d'autres  disent  du  grec  cTo(p6s,  sage.
@@@ FSD4 sofa headword
14366:No  power  how  creat  soever  can  force  men  to  chanee  theic opinions  Fuasklxn  Autobioa  voi  a   pt  it  p   606  [l  1874  J sof,  1   sof.  2   35f,  n   A   plain  fabric  made  of  Angora  goats'  hair so'fa,  i   sO'iu,  2   ao'ia,  n   K   \ong  Bent,  propuriy  -op- holstcrcd  and  havnng  a   back  and  raised  ends,  or  some- times pillows  f<Turk  soffa,<saffa  put  In  line  ]   —   so'fa* bed",  n   A   sofa  that  can  be  transformed  Into  a   bed.  usually
```


## [2026-09-14T02:44:17.008Z] TOOL CALL #69: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-463.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\ndef N(i, lang, words, verdict, der, der_fa, sources, refs, cons, **extra):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": der, \"derivation_fa\": der_fa, \"sources\": sources,\n         \"ref_check\": refs, \"consulted\": cons}\n    d.update(extra)\n    return d\n\ne0_nodes = [\n N(1, \"Avestan / Old Persian\",\n   \"hâ 2, hô, hâu 2, hauv, hya; ava-hya, awa, awam; šim, šâm\",\n   \"plausible\",\n   \"Av. hā (f. nom. sg.) and hō (m. nom. sg.) continue PIE *séh2 / *só; the paradigm is suppletive, the oblique cases coming from *to- (Av. tәm, tā-). Av. hāu and OP hauv 'that (one), yonder' are *so- plus the deictic particle *-u (cf. Skt. asau, Gk. hou[tos]); Kent §263 calls hauv (once hauvam, DB 1.29) 'the demonstrative'. OP hya / hyā (Skt. syáḥ, syā́) is the relative-article built on the extended stem *syo-, *syā-, which Pokorny files under this very headword; Kent §26/§198 notes it is always written hy- because the nom. sg. m./f. were hya, hyā. The enclitics OP -šim (acc.) and -šām (gen. pl.) go back to PIE *sim (Skt. sīm, Av. hīm), Old Persian š- being the regular pAr. sandhi form after final -i/-u (Kent §195), -šām being analogical. The one word that does not belong to this root is awa/awam: OP ava-, Av. auua- 'that' is a separate deictic stem (Pokorny 73f. au-, aue- 'jener'), so only the compound ava-hya (ava- + hya-) contains a *so-/*to- element. Hence 'plausible' rather than 'confirmed'.\",\n   \"صورت‌های اوستایی hā (نهادی مادینه) و hō (نهادی نرینه) دنبالهٔ *séh2/*só هندواروپایی آغازین‌اند و ستاک آن‌ها در حالت‌های دیگر از *to- گرفته می‌شود (پارادایم مکمل/suppletive). hāu اوستایی و hauv پارسی باستان «آن، آن دورتر» از *so- به‌علاوهٔ ادات اشارهٔ *-u ساخته شده‌اند (قس. asau سنسکریت) و کنت (بند ۲۶۳) آن را «ضمیر اشاره» می‌نامد. hya/hyā پارسی باستان (برابرِ syáḥ/syā́ سنسکریت) موصول‌ـ‌حرف تعریف است و از ستاک گستردهٔ *syo-, *syā- می‌آید که پوکورنی زیر همین سرواژه آورده است. پی‌بست‌های -šim (رایی) و -šām (اضافی جمع) به *sim هندواروپایی (hīm اوستایی، sīm سنسکریت) بازمی‌گردند و š آغازین صورت سندی ایرانی‌ـ‌هندی پس از -i/-u است (کنت بند ۱۹۵). تنها awa/awam به این ریشه تعلق ندارد: ava- پارسی باستان و auua- اوستایی ستاک اشارهٔ جداگانه‌ای است (پوکورنی ص ۷۳)، و فقط ترکیب ava-hya عنصر *so-/*to- را در خود دارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n   [],\n   [{\"ref\": \"POK:979\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW 978-979 'so(s), sā' (POK_full.txt, block ending 'Page(s): 978-979'): 'Old Indic sa and sah (*sos), f. sā, Avestan ha and hō, f. hā ... with particle -u Old Indic a-sau, Avestan hāu, ap. hauv m. f. \\\"this\\\" ... besides an extended stem syo-, syā- Old Indic syáḥ ... ap. hya m., hyā f. ... genus-indifferent are Akk. Old Indic sīm, Avestan hīm, ap. sim.' Every form of this node except awa/awam stands on that page.\"},\n    {\"ref\": \"ZFS:51\", \"status\": \"not_checked\",\n     \"note\": \"Abolghasemi, Zaban-e Farsi va Sargozasht-e An — refs_online.json records that no digitised copy exists on any permitted platform (re-searched 2026-09); not on disk.\"}],\n   [{\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §195, §263 (KNT_full.txt lines 10144ff., 12621ff.)\", \"stance\": \"supports\",\n     \"note\": \"'Acc. -šim is the acc. of pIE *si-, in the pAr. sandhi-form with š after final -i and -u (§117); Skt. sīm has the long vowel; Av. hīm has pAr. h ... Pl. acc. -šiš (Av. hīš) and gen. -šām were formed by analogy'; and '§263. The demonstrative hauv (once hauvam, DB 1.29) is either a pronoun referring to a previously mentioned substantive, or an adjective...'. §264 treats ava- 'that' as a SEPARATE demonstrative.\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, s.v. ava-, hauv (BRT.txt lines 4965-5048, 5172)\", \"stance\": \"partial\",\n     \"note\": \"Bartholomae's article on ava- cites 'hauv udapatatā' etc. and lists 'p. avahya-rādiy ... \\\"aus diesem Grund, deshalb\\\"' under ava-; i.e. he files hauv/ava- under the deictic ava-, not under hā/hō, which supports the analysis that awa- is a distinct stem.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 509 (WLD_Bd2_pages.txt leaf 513)\", \"stance\": \"supports\",\n     \"note\": \"'so, sā ... ursprünglich nur nom. sg. m. f., die andern Kasus vom Stamme to-. Ai. sá und sáḥ, f. sā, av. ha und hō, f. hā ... mit Partikel -u ai. a-sāu, av. hāu, ap. hauv m. f. \\\"dieser, diese\\\".'\"}]),\n\n N(2, \"Pahlavi\", \"kĕ; avâ; avâ-šâm\", \"transcription_suspect\",\n   \"Two of the three forms are not Middle Persian as written. MacKenzie p.50 does have kē [MNW < A mn-w | M kȳ, N ki] 'who, which', but it continues Old Iranian *ka- / *kahya (PIE *kʷo-, *kʷis), the interrogative-relative stem, not *so-/*to-; New Persian ke is the merger of that kē with MP kū 'that' (AYK). For 'he, she' Middle Persian has ōy [OLE, Manichaean ʾwy] with the plural awēšān [ʾwyšʾn] (MacKenzie pp. 5, 61) — no *avā and no *avā-šām are attested. The printed page (book p. 433) does read 'avâ' and 'avâ-šâm', so the extraction is faithful and the odd forms are the book's own: they are Nourai's rendering of Mo'in's footnote to Borhan-e Qate' p. 197, which writes 'پهلوی avēšān جمع avē (او، اوی)' — i.e. avē / avēšān with ē; 'avâ-šâm' additionally looks re-spelled after the Avestan šām of the parent box. The gloss 'plural form used as a sign of respect for he/she' is lifted verbatim from Borhan's Persian entry ایشان on that same page, which is a New Persian, not a Pahlavi, entry.\",\n   \"از سه صورت این جعبه دو صورت به شکل نوشته‌شده در فارسی میانه گواهی نشده است. مکنزی (ص ۵۰) kē را با نویسهٔ هُزوارشی MNW «که، کی» ثبت کرده، اما این واژه دنبالهٔ *ka-/*kahya ایرانی باستان (از *kʷo- هندواروپایی) است، یعنی ستاک پرسشی‌ـ‌موصولی، نه ستاک اشارهٔ *so-/*to-؛ «که» فارسی نو نیز حاصل آمیزش همین kē با kū «که، تا» ی پهلوی است. برای «او» فارسی میانه ōy دارد و جمع آن awēšān (مکنزی صص ۵ و ۶۱)؛ صورت‌های avâ و avâ-šâm در هیچ متن پهلوی نیامده‌اند. تصویر صفحهٔ چاپی (ص ۴۳۳) نشان می‌دهد که همین صورت‌ها در کتاب چاپ شده‌اند، پس خطای خوانش اسکن در کار نیست و خطا از خودِ کتاب است: نورایی حاشیهٔ معین بر برهان قاطع ص ۱۹۷ («پهلوی avēšān جمع avē») را با â به‌جای ē بازنویسی کرده و šām اوستایی جعبهٔ بالا را در آن گنجانده است. معنای «صورت جمع برای احترام» نیز عیناً تعریف مدخل فارسیِ «ایشان» در همان صفحهٔ برهان است.\",\n   [],\n   [{\"ref\": \"BQT:197\", \"status\": \"partial\",\n     \"note\": \"Borhan-e Qate' (ed. Mo'in) p. 197 = BQT_v1_pages.txt leaf 417: entry 'ایشان ـ بر وزن خویشان. ضمیر است نسبت بذوی العقول حاضر بطریق تعظیم و جمع ... استعمال کنند ۳.' with Mo'in's footnote 3 at the foot of the page: 'پهلوی avēšān جمع avē (او، اوی) ... [رک: او]'. The page thus supports a Pahlavi avēšān/avē — spelled with ē — but it is an entry on New Persian ایشان, and it says nothing about kē.\"}],\n   [{\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 5, 50, 61 (PHD.txt lines 223, 426, 530)\", \"stance\": \"contradicts\",\n     \"note\": \"'ōy [OLE < A ʾl-h | M ʾwy, N ~] he, she, that; (pl. awēšān)'; 'awēšān [OLEʾn, v. ōy | M ʾwyšʾn, N ēšān] they, those'; 'kē [MNW < A mn-w | M kȳ, N ki] who, which'. No avā / avā-šām.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt lines 671, 2126)\", \"stance\": \"partial\",\n     \"note\": \"Nyberg reads the ideogram MNW as kē throughout ('MNW ... = kē tō man', 'MNW-šān janišn ... = kē-šān janišn hac-išān') and writes the 3rd-person plural as išān, never avā-šām.\"}],\n   error_in=\"book\",\n   book_prints=\"kĕ : that ; avâ : he, she ; avâ-šâm : plural form used as a sign of respect for he/she\",\n   correct_form=\"MP kē 'who, which'; ōy / awē 'he, she'; pl. awēšān\"),\n\n N(3, \"Persian\", \"Keh «که»; oŭ «او»; îšân «ایشان»\", \"plausible\",\n   \"او: Horn no. 136 (p. 31) gives exactly the chart's route — 'ōi \\\"er, jener\\\"; ap. ava- + hya-; pāz. ōi' — i.e. Old Iranian *awa-hya > MP ōy > early NP ō/ōi > modern ū/ow «او»; the -hya element is the *so-/*syo- of the root, the ava- element is not. ایشان < MP awēšān, the plural of ōy, with regular loss of initial a-w- > ī- in New Persian (MP awēšān > NP ēšān/īšān); its -šān is the old third-person enclitic, Horn no. 769 (p. 170): 'šān \\\"ihr (Enclit.)\\\"; ap. šām; phlv. -šān', which is precisely the chart's šām > -šān link, and Mo'in repeats it in the footnote to Borhan p. 1230 ('پهلوی šān، پارسی باستان šām، هوبشمان'). که 'that' is the weak link: it is the merger of MP kū 'that' (ideogram AYK) with MP kē 'who, which' (MNW), from the PIE interrogative-relative stem *kʷo-/*kʷis (cognate with English who, what), not from *so-/*to-. The parenthetical اینکه، آنکه are simply compounds of این/آن with that same که.\",\n   \"«او» از فارسی میانهٔ ōy و آن از *awa-hya ایرانی باستان است؛ هرن (شمارهٔ ۱۳۶، ص ۳۱) دقیقاً همین را می‌گوید: «ōi = ava- + hya-, پازند ōi». پس جزء -hya همان عنصر *so-/*syo- ریشه است، ولی جزء ava- به ستاک اشارهٔ دیگری تعلق دارد. «ایشان» از awēšān فارسی میانه (جمع ōy) است؛ awē- آغازین در فارسی نو به ای- بدل شده و -šān همان پی‌بست کهن سوم‌شخص است: هرن (شمارهٔ ۷۶۹، ص ۱۷۰) می‌نویسد «šān، پارسی باستان šām، پهلوی -šān» و معین نیز در حاشیهٔ برهان قاطع ص ۱۲۳۰ همین را از هوبشمان نقل می‌کند (هرچند خودِ هوبشمان در «مطالعات ایرانی» شمارهٔ ۷۶۹ -šān را ترکیب š + پسوند جمع -ان می‌داند). اما «که» به این ریشه بستگی ندارد: آمیزهٔ kū و kē فارسی میانه است و به ستاک پرسشی‌ـ‌موصولی *kʷo-/*kʷis هندواروپایی بازمی‌گردد (هم‌ریشه با who/what انگلیسی). پس دو واژه درست و یکی ردشدنی است.\",\n   [\"https://en.wiktionary.org/wiki/%DA%A9%D9%87\",\n    \"https://en.wiktionary.org/wiki/%D8%A7%D9%88\",\n    \"https://en.wiktionary.org/wiki/%D8%A7%DB%8C%D8%B4%D8%A7%D9%86\"],\n   [{\"ref\": \"HRN:31,170\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss, p. 31 no. 136 (HRN.txt leaf 52): 'ōi \\\"er, jener\\\". ap. ava- + hya-; pāz. ōi.' — and p. 170 no. 769 (leaf 191): '769. šān \\\"ihr (Enclit.)\\\". ap. šām (Enclit.); phlv. -šān.' Both arrows of the chart are on exactly the cited pages.\"},\n    {\"ref\": \"BQT:1230\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' p. 1230 (fetched with tools/ref_page.py BQT:1230, pdf page 21 of vol. 3; the printed numeral ۱۲۳۰ is visible at the head): the entry شان ends '... و ایشان هم هست که ضمیر جمع غایب باشد' and Mo'in's footnote 1 reads 'پهلوی šān ـ پارسی باستان šām «هوبشمان». در فارسی «شان» مرکب است از: ش š + ان (پیوند جمع)'.\"}],\n   [{\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp. 5, 61\", \"stance\": \"supports\",\n     \"note\": \"'awēšān ... | M ʾwyšʾn, N ēšān] they, those' and 'ōy ... | M ʾwy, N ~] he, she' — the MP→NP steps او and ایشان are given explicitly.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, no. 769 (HUB.txt line 2781)\", \"stance\": \"partial\",\n     \"note\": \"'769. Np. -šān aus -š + Pluralsuff. -ān gebildet wie -mān, -tān. Vgl. WZKM. 7, 280.' Hübschmann makes NP -šān an inner-Persian formation (enclitic -š + plural -ān) rather than a direct continuation of OP -šām.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir (فرهنگ معین, s.v. او/ایشان region)\", \"stance\": \"silent\",\n     \"note\": \"The online Mo'in text carries the bracketed origin tags but not the Latin-script Pahlavi forms of the print edition, so it adds nothing beyond Borhan's footnotes for these three words.\"}]),\n\n N(4, \"Avestan\", \"ha-mazan\", \"disputed\",\n   \"There is no Avestan word ha-mazan-. The form is a modern conjecture, and Nourai's own source says so: Watkins (AHD appendix, s.v. magh-2 'to fight') writes 'Hypothetical Old Iranian *ha-maz-an-, \\\"warrior\\\" (*ha-, with < *sm̥-; see sem-1), possibly borrowed into Greek as Amazōn'. Two things follow. (1) The language label should be 'Old Iranian (hypothetical)', not 'Avestan'. (2) The word does not belong under So/To at all: the *ha- of *ha-mazan- is the zero grade *sm̥- of *sem- 'one, together' (hence 'fighting together'), and the second element is *magh- 'to fight' — which is why Nourai's own cross-reference points to Magh 2. Modern scholarship is more sceptical still: Beekes and Wiktionary treat Gk. Ἀμαζών as Pre-Greek / of unknown origin, Etymonline calls the Iranian compound only a possibility beside 'an unknown non-Indo-European word', and Klein derives it instead from Hebrew ʿammīṣ 'strong'. The ancient 'breastless' explanation (a- + mazos) is universally regarded as folk etymology.\",\n   \"واژه‌ای به صورت ha-mazan- در اوستا گواهی نشده است؛ این صورت یک بازسازی فرضی است و خودِ مأخذ نورایی همین را می‌گوید: واتکینز در پیوست ریشه‌های هندواروپایی AHD ذیل magh-2 «جنگیدن» می‌نویسد: «Old Iranian *ha-maz-an- فرضی، «جنگاور» (جزء *ha- از *sm̥- «با هم»، نک. sem-1)، شاید به یونانی وام داده شده به صورت Amazōn». پس نخست، برچسب زبانی باید «ایرانی باستانِ فرضی» باشد نه «اوستایی»؛ دوم، این واژه اصلاً به ریشهٔ So/To تعلق ندارد، چون *ha- درجهٔ صفر *sem- «یک، با هم» است و جزء دوم *magh- «جنگیدن» (که ارجاع خود نورایی به Magh 2 نیز همین را نشان می‌دهد). پژوهش امروزی محتاط‌تر است: بیکس و ویکی‌واژه Ἀμαζών را واژه‌ای پیش‌یونانی و بی‌ریشهٔ روشن می‌دانند، اتیمانلاین ریشهٔ ایرانی را تنها «شاید» می‌شمارد و کلاین آن را از ʿammīṣ عبری «نیرومند» می‌گیرد. توضیح باستانی «بی‌پستان» (a- + mazos) ریشه‌شناسی عامیانه است. بنابراین پژوهش امروزی این پیکان را رد می‌کند.\",\n   [\"https://www.etymonline.com/word/Amazon\", \"https://en.wiktionary.org/wiki/Amazon\"],\n   [{\"ref\": \"AHD:1541\", \"status\": \"partial\",\n     \"note\": \"Watkins 1985 (the standalone edition of the same appendix), s.v. magh-2: 'magh-2. To fight. Hypothetical Old Iranian *ha-maz-an-, \\\"warrior\\\" (*ha-, with < *sm̥-; see sem-1), possibly borrowed into Greek as Amazōn, Amazon: AMAZON. [Pok. magh- 697.]' The reference does carry the compound, but files it under magh- with *ha- from *sem-, i.e. NOT under the demonstrative *so-, and marks it hypothetical.\"}],\n   [{\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Amazon (KLN_1966.txt line 2409)\", \"stance\": \"contradicts\",\n     \"note\": \"'Amazon, n., a member of a race of female warriors in Scythia (Greek mythol.) — L., fr. Gk. Ἀμαζών, which prob. derives fr. Heb. ʿammīṣ, \\\"strong\\\". The form of the word ... prob. influenced by the folk etymology according to which Ἀμαζών lit. means \\\"without breast\\\".'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1, s.v. Amazon (WEB_vol1.txt line 6335)\", \"stance\": \"contradicts\",\n     \"note\": \"'[L., from Gr. Amazōn; a priv., and mazos, breast. Derived by Greek folk etym. from the legend that the Amazons cut off the right breast...]' — no Iranian source at all.\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch\", \"stance\": \"silent\",\n     \"note\": \"grep of BRT.txt for 'mazan', 'hamazan', 'ha-mazan' returns no headword; the compound is unattested in Avestan.\"}]),\n\n N(5, \"Latin\", \"(no word given)\", \"plausible\",\n   \"A pass-through box for Latin Amazōn, Amazonis f., the Latin form of the ethnonym. The chart makes it depend directly on the (hypothetical) Iranian word, which skips the only stage that is actually attested: Greek Ἀμαζών (Homer Il. 3.189, Herodotus 4.110ff.), whence Latin took the name with the usual -ōn, -onis declension in the classical period; Latin then supplies Old French and English. So the box itself is right, but one link of the chain (Greek) is missing from the drawing.\",\n   \"این جعبه تنها گذرگاهی است برای Amazōn, Amazonis لاتین. نمودار آن را مستقیماً از واژهٔ فرضی ایرانی می‌گیرد و بدین‌سان تنها حلقهٔ گواهی‌شدهٔ زنجیره را حذف می‌کند: یونانی Ἀμαζών (ایلیاد ۳٫۱۸۹، هرودوت ۴٫۱۱۰ به بعد) که لاتین آن را در دورهٔ کلاسیک با صرف -ōn/-onis وام گرفته و سپس به فرانسهٔ کهن و انگلیسی رسانده است. پس خودِ جعبه درست است، اما یک حلقه (یونانی) در نمودار جا افتاده است.\",\n   [\"https://en.wiktionary.org/wiki/Amazon\"],\n   [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own; checked instead against the references of the neighbouring boxes (AHD:1541, AHD:40).\"}],\n   [{\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Amazon\", \"stance\": \"supports\",\n     \"note\": \"'— L., fr. Gk. Ἀμαζών' — Latin from Greek, the stage the chart omits.\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's, vol. 1, s.v. Amazon\", \"stance\": \"supports\",\n     \"note\": \"'[L., from Gr. Amazōn ...]'.\"}]),\n\n N(6, \"French\", \"(no word given)\", \"confirmed\",\n   \"Pass-through box for French Amazone (attested from the 14th c., learned borrowing from Latin Amazōn(em) with the -e of the feminine); in French it also acquired the sense 'horsewoman, lady riding side-saddle' (monter en amazone), which is the sense that later travelled east. Latin > French is regular and uncontroversial.\",\n   \"جعبهٔ گذرگاهیِ فرانسوی Amazone (از سدهٔ چهاردهم، وام‌گیری عالمانه از Amazōn(em) لاتین با -e مادینه). در فرانسه معنای «زن سوارکار» (monter en amazone) نیز پیدا کرده که همان معنایی است که بعدها به شرق رفته است. مسیر لاتین ← فرانسوی قاعده‌مند و بی‌مناقشه است.\",\n   [\"https://www.etymonline.com/word/Amazon\"],\n   [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"box carries no reference; the Latin > French step is covered by Klein and Etymonline s.v. Amazon.\"}],\n   [{\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Amazon / amazonite\", \"stance\": \"supports\",\n     \"note\": \"Klein's chain L. < Gk. with the Romance forms following the Latin; French Amazone is the regular learned reflex.\"},\n    {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\",\n     \"note\": \"grep of DEV.txt for 'Amazone' finds no entry — Devic treats only orientalisms, i.e. he does not regard Amazone as an Oriental loan in French.\"}]),\n\n N(7, \"Persian\", \"«آمازن ۱»; «آمازن ۲»\", \"plausible\",\n   \"Persian آمازن/آمازون (āmāzon) 'woman warrior' and 'the Amazon river' is a modern European loan, and the French route the chart draws is the likeliest one: Qajar-period Persian took most classical and geographical names through French (Amazone), which explains the vowel -on and the stress; the two numbered senses are Mo'in's own two a'lām entries (vol. 5, proper names). The word is book-learned and never had a Persian inflectional life, hence Nourai's label 'obsolete' for sense 1. The chain is plausible but the mediation cannot be proved from the sources on disk, and the form usually printed in Persian is آمازون; the book's آمازُن is a legitimate transliteration of French Amazone rather than an error.\",\n   \"«آمازن/آمازون» در فارسی وام‌واژه‌ای اروپایی و نو است و مسیری که نمودار می‌کشد (فرانسوی ← فارسی) محتمل‌ترین مسیر است: بیشتر نام‌های کلاسیک و جغرافیایی در دورهٔ قاجار از راه فرانسه به فارسی آمده‌اند (Amazone) و همین واکهٔ پایانی -on را توضیح می‌دهد. دو معنای شماره‌دار همان دو مدخل اعلام معین (جلد ۵) است. واژه کتابی است و در فارسی صرف نشده، ازاین‌رو نورایی معنای نخست را «متروک» خوانده است. زنجیره پذیرفتنی است، اما واسطهٔ فرانسوی را با منابع در دسترس نمی‌توان اثبات کرد؛ املای رایج فارسی «آمازون» است و «آمازُن» کتاب آوانگاری درستِ Amazone فرانسوی است، نه غلط چاپی.\",\n   [\"https://en.wiktionary.org/wiki/Amazon\"],\n   [{\"ref\": \"MON5:58\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in vol. 5 (اعلام) is not digitised: refs_online.json lists only the lexicon volumes for MON, vajehyab/abadis serve the lexicon text (a query for آمازون on abadis returned HTTP 400), and the local MON_part1/2 files are the 2-vol Adena lexicon reprint, which has no proper-name section.\"}],\n   [{\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir/vajehyab\", \"stance\": \"silent\",\n     \"note\": \"no آمازون entry retrievable online (the a'lām volumes are not served); grep of MON_part1/MON_part2 for آمازون likewise finds nothing.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Amazon (river)\", \"stance\": \"supports\",\n     \"note\": \"'Amazon, n., name of the largest river in the world in volume. — Sp. Amazonas, from prec. word; so called by Francisco Orellana after his battle with the Tapuyas (in 1541)' — the same two senses that Mo'in numbers 1 and 2 in Persian.\"}]),\n\n N(8, \"English\", \"Amazon 1; Amazon 2\", \"confirmed\",\n   \"English Amazon is first the mythological female warrior (Middle English, from Latin Amazōn, from Greek Ἀμαζών), and secondarily the river: Francisco de Orellana renamed the Rio Marañón in 1541 after a fight in which native women bore arms, Spanish Amazonas, whence English. Both senses are exactly as the chart gives them, and AHD:40 is the dictionary page where the two senses stand. The only disputed part of this branch is the ultimate origin claimed in box #4, not the Latin > English transmission.\",\n   \"Amazon انگلیسی نخست به معنای زن جنگاور اساطیری است (انگلیسی میانه، از Amazōn لاتین، از Ἀμαζών یونانی) و سپس نام رود: فرانسیسکو دِ اورهانا در ۱۵۴۱ پس از نبردی که در آن زنان بومی نیز جنگیدند، رود مارانیون را Amazonas نامید و از اسپانیایی به انگلیسی رسید. هر دو معنا دقیقاً همان است که نمودار آورده و صفحهٔ AHD:40 نیز همین دو معنا را دارد. تنها بخش مورد مناقشهٔ این شاخه ریشهٔ نهایی در جعبهٔ #۴ است، نه انتقال لاتین ← انگلیسی.\",\n   [\"https://www.etymonline.com/word/Amazon\"],\n   [{\"ref\": \"AHD:40,1541\", \"status\": \"partial\",\n     \"note\": \"AHD:1541 = the IE-roots appendix entry checked above (Watkins s.v. magh-2, 'hypothetical ... possibly borrowed into Greek'); AHD:40 is the New College dictionary page with the Amazon entries, which is not in the local corpus (only the Watkins appendix is). Klein and Webster confirm the two senses and the Greek>Latin>English route.\"},\n    {\"ref\": \"KLN:1468\", \"status\": \"not_checked\", \"note\": \"not cited on this node.\"}],\n   [{\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Amazon (2 entries, line 2409-2411)\", \"stance\": \"supports\",\n     \"note\": \"the mythological word ('a member of a race of female warriors in Scythia') and 'name of the largest river in the world in volume ... so called by Francisco Orellana ... (in 1541)'.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, s.v. Amazon\", \"stance\": \"supports\",\n     \"note\": \"the dictionary carries both the mythological and the river sense with the same Greek>Latin derivation.\"}]),\n\n N(9, \"Germanic\", \"(no word given)\", \"confirmed\",\n   \"Pass-through box for Proto-Germanic, where the PIE suppletive demonstrative survives as *sa (m.), *sō (f.), *þat (n.) — Gothic sa, sō, þata, Old Norse sá, sú, þat, Old English sē, sēo, þæt. The s-forms of the nominative and the þ- forms of the rest are the direct continuation of *so- beside *to- (Germanic *þ- from PIE *t- by Grimm's law); the later levelling of þ- into the nominative (OE þē > the) happened within English.\",\n   \"جعبهٔ گذرگاهیِ ژرمانی آغازین، که در آن پارادایم مکمل هندواروپایی به صورت *sa (نرینه)، *sō (مادینه)، *þat (خنثی) بازمانده است: گوتیک sa, sō, þata؛ نورس کهن sá, sú, þat؛ انگلیسی کهن sē, sēo, þæt. صورت‌های s- در حالت نهادی و صورت‌های þ- در بقیهٔ حالت‌ها دنبالهٔ مستقیم *so- در کنار *to- هستند (þ ژرمانی از *t هندواروپایی بر پایهٔ قانون گریم). یکسان‌سازی þ- در حالت نهادی (þē > the) بعدها درون انگلیسی رخ داده است.\",\n   [],\n   [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"box carries no reference; checked against the root's own POK:979 and against Watkins s.v. so-/to-.\"}],\n   [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. so-, to- (AHD_watkins1985.txt lines 977, 1094)\", \"stance\": \"supports\",\n     \"note\": \"'so-. This, that (nominative). For other cases see to-. ... 2. Feminine form *syā in Germanic *sjō in Old English sēo, sīe, she: SHE'; 'to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *þē- ...'.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 978-979\", \"stance\": \"supports\",\n     \"note\": \"'Gothic sa, sō, Old Icelandic sá, sú, Old English sē m.' listed among the reflexes of so(s), sā.\"}]),\n\n N(10, \"English\", \"the, this, they, there, than, then, that, them, she\", \"confirmed\",\n   \"All nine words are reflexes of this root, and Watkins' appendix distributes them exactly as the chart does: under to- 'the (OE þē), this (Gmc *þasi-), than/then (*þana-), there (*þēr), that (*tod > OE þæt), they (Gmc nom. pl. *þai, borrowed into English from Old Norse þeir in the 12th-13th c.), them (dat. pl. *þaimiz, likewise via Norse þeim)'; and under so- 'Feminine form *syā in Germanic *sjō in Old English sēo, sīe: SHE'. The only refinement to add is that they/them/their are Norse-mediated rather than inherited directly through Old English, and that she's development (OE sēo > ME scho, sche) involves a shift of stress in the diphthong.\",\n   \"هر نُه واژه بازماندهٔ همین ریشه‌اند و پیوست واتکینز دقیقاً همان تقسیم‌بندی نمودار را دارد: ذیل to- واژه‌های the (انگلیسی کهن þē)، this (ژرمانی *þasi-)، than/then (*þana-)، there (*þēr)، that (*tod > þæt)، they (جمع نهادی ژرمانی *þai) و them (برایی جمع *þaimiz) آمده‌اند و ذیل so- واژهٔ she («صورت مادینهٔ *syā در ژرمانی *sjō، انگلیسی کهن sēo, sīe»). تنها نکتهٔ تکمیلی این است که they/them/their از راه نورس کهن (þeir, þeim) در سدهٔ دوازدهم‌ـ‌سیزدهم وارد انگلیسی شده‌اند نه از راه میراث مستقیم انگلیسی کهن، و در she دگرگونی مصوت مرکبِ sēo (> scho, sche) در کار است. ادعای نورایی درست است.\",\n   [],\n   [{\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. to-: '1. Germanic *þē- in Old English þē ... THE; ... 3. Germanic *þasi- in Old English þes, this: THIS. 4. Germanic *þana- in Old English þanne ... THAN, THEN. ... 6. Germanic *þēr in Old English þēr, there: THERE. ... 8. Germanic nominative plural *þai in Old English þā and Old Norse þeir: THEY. ... 10. Germanic dative plural *þaimiz in Old Norse þeim and Old English þǣm: THEM. 11. Extended neuter form *tod- ... in Old English þæt: THAT'; and s.v. so-: '... Old English sēo, sīe, she: SHE.'\"}],\n   [{\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. she (KLN_1966.txt line 34910)\", \"stance\": \"supports\",\n     \"note\": \"'she ... fr. OE. sēo, sio, fem. of se, used as definite article, orig. a demonstrative pron. meaning \\\"that\\\" ... Outside Teut. cp. OI. sā \\\"she\\\" ... Gk. hē, fem. of the art. ho, OIr. sí \\\"she\\\", OI. sīm (acc.) \\\"her\\\".' — the same Indo-European set as boxes #1 and #10.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 978-979 and 1086\", \"stance\": \"supports\",\n     \"note\": \"Germanic sa/sō/þat listed under so(s), sā, with the oblique forms referred to the stem to- (IEW 1086 'to-1, tā-, tyo-: that, he (demonstr. base)').\"}]),\n]\n\ne0 = {\n \"entry\": 0,\n \"root\": \"So, To\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *só (m.), *séh2 (f.) — nominative only — with the suppletive oblique stem *to- (*tód n.) 'this, that'\",\n \"note\": \"Pokorny prints the headword as 'so(s), sā' with the gloss 'demonstrative stem; he, she' and the explicit grammatical note 'originally only Nom. Sg. m. f., the other cases of stem to-, fem. also sī' (IEW 978-979), and treats 'to-1, tā-, tyo- \\\"that, he (demonstr. base)\\\"' as its companion at IEW 1086. Nourai's double headword 'So, To' therefore renders the standard reconstruction correctly, the language label 'Indo-European' is right, and the gloss 'this, that' is right. Cross-cutting problems on this chart: (a) box #4 (ha-mazan > Amazon) does not belong to this root at all — its *ha- is *sm̥- 'together' (root *sem-), as Nourai's own AHD reference states; (b) the Persian/Pahlavi word ke/kē belongs to the interrogative stem *kʷo-; (c) awa/awam in box #1 belongs to the deictic stem *awo- (IEW 73). The Persian material that does belong here is او (< *awa-hya) and the -šān of ایشان (< *šām).\",\n \"note_fa\": \"پوکورنی این ریشه را با سرواژهٔ «so(s), sā» و معنای «ستاک اشاره؛ او» آورده و صریحاً یادآور شده که «در اصل تنها در حالت نهادی نرینه و مادینه به کار می‌رفته و حالت‌های دیگر از ستاک to- ساخته می‌شده» (فرهنگ ریشه‌شناسی هندواروپایی، صص ۹۷۸–۹۷۹)، و ستاک to- را نیز در ص ۱۰۸۶ آورده است. بنابراین سرواژهٔ دوگانهٔ «So, To» بازسازی معیار را درست نشان می‌دهد، برچسب «هندواروپایی» درست است و معنای «این، آن» نیز درست است. اما سه اشکال سراسری در این نمودار هست: نخست، جعبهٔ #۴ (ha-mazan ← Amazon) اصلاً به این ریشه تعلق ندارد و جزء *ha- آن درجهٔ صفر *sem- «با هم» است — همان چیزی که مأخذ خودِ نورایی (AHD) می‌گوید؛ دوم، «که» فارسی و kē پهلوی به ستاک پرسشی *kʷo- بازمی‌گردند؛ سوم، awa/awam در جعبهٔ #۱ از ستاک اشارهٔ دیگری (*awo-، پوکورنی ص ۷۳) است. آنچه به‌راستی از این ریشه در فارسی مانده «او» (از *awa-hya) و جزء -شان در «ایشان» (از *šām) است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"POK:979\", \"status\": \"supports\",\n   \"note\": \"IEW 978-979, 'Root / lemma: so(s), sā; Meaning: demonstrative stem; he, she; Grammatical information: originally only Nom. Sg. m. f., die other case of stem to-, fem. also sī' (POK_full.txt, block ending 'Page(s): 978-979'). Page 979 is the second page of that article, so the citation is exact.\"}],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 509 (WLD_Bd2_pages.txt leaf 513, running head 'sindh(u-) — soito-s 509')\", \"stance\": \"supports\",\n    \"note\": \"'so, sā \\\"ὁ, ἡ\\\", ursprünglich nur nom. sg. m. f., die andern Kasus vom Stamme to-.' — the source Pokorny himself refers to ('WP. II 509').\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. so-, to- (AHD_watkins1985.txt lines 977, 1094)\", \"stance\": \"supports\",\n    \"note\": \"'so-. This, that (nominative). For other cases see to-. ... [Pok. so(s), sā, sī 978.]' and 'to-. Demonstrative pronoun. For the nominative singular see so-. ... [Pok. 1. to- 1086.]' — the two headwords Nourai combines into 'So, To'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. s.v. sos (IEC.txt line 16746)\", \"stance\": \"supports\",\n    \"note\": \"'sos, f: sā \\\"this; he, she\\\". ... WP II, 509  Skt. sah, sā; Av. hō, hā; ... Gk. hó, hē, def. art. ...; Go. sa, sō ...; ON sá, sú \\\"that; the\\\".'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms\", \"stance\": \"silent\",\n    \"note\": \"Buck's chapters are organised by notion (the demonstrative pronouns are not among his headings); a grep of SYN.txt for 'demonstrative' turns up no entry for this root.\"}],\n \"nodes\": e0_nodes,\n}\n\ne1_nodes = [\n N(1, \"Persian\", \"soffeh «صُفّه»\", \"confirmed\",\n   \"Persian صُفّه (ṣoffe) is an Arabic loanword, taken over with the Arabic form and meaning: 'raised platform, stone bench, roofed portico, the raised seat of a saddle'. Mo'in's dictionary tags it explicitly '[ع. صفة]' (= Arabic) and defines it 'خانهٔ تابستانی سقف‌دار'; Dehkhoda glosses it سکو، ایوان، پیشگاه، زین — the last of which ('saddle') is precisely the second sense in Nourai's root box. In Persian architecture the word is the standard term for the raised, vaulted bay of a mosque or house (صفّهٔ عمر at Persepolis, etc.). The direction of the loan is Arabic > Persian, as the chart draws it; the word is not among the Persian loans in Arabic listed by Asbaghi or Addi Shir.\",\n   \"«صُفّه» در فارسی وام‌واژه‌ای عربی است و با همان صورت و معنا گرفته شده: «سکو، ایوان سرپوشیده، پیشگاه، نشیمنگاه زین». معین آن را صریحاً با نشانهٔ «[ع. صفة]» آورده و «خانهٔ تابستانی سقف‌دار» معنی کرده است، و دهخدا معناهای سکو، ایوان، پیشگاه و زین را می‌دهد — که معنای اخیر همان «saddle» جعبهٔ ریشه در کتاب است. در معماری ایرانی «صفه» اصطلاح جاافتاده برای ایوان بلند و طاق‌دار مسجد و خانه است. جهت وام‌گیری، چنان‌که نمودار می‌کشد، عربی ← فارسی است؛ این واژه در فهرست وام‌واژه‌های فارسی در عربی (اصباغی، ادی شیر) نیامده است. ادعای نورایی درست است.\",\n   [\"https://abadis.ir/fatofa/%D8%B5%D9%81%D9%87/\", \"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%A9\"],\n   [{\"ref\": \"MON:2156\", \"status\": \"supports\",\n     \"note\": \"Mo'in's entry, read through abadis.ir (the site serves the فرهنگ معین text): '(صُ فَّ) [ع. صفة] (اِ.) خانه تابستانی سقف دار' — the bracketed [ع.] is Mo'in's Arabic-origin tag, exactly the arrow the chart draws. The print page number 2156 could not be verified because only the lexicon text, not the pagination, is online.\"}],\n   [{\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n     \"note\": \"grep of PLA_pages.txt for صفه / ṣuffa finds nothing — Asbaghi does not claim the word for Persian, which is consistent with Arabic > Persian.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba\", \"stance\": \"silent\",\n     \"note\": \"grep of AFM_pages.txt for صفة yields only an unrelated occurrence of the word صفة 'attribute'; no headword claiming صفّه as an arabicised Persian word.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 p. 1468 s.v. sofa\", \"stance\": \"supports\",\n     \"note\": \"'Turk. sofa, fr. Arab. ṣuffah' — the word is Arabic, so a Persian ṣoffe can only be a loan from it.\"}]),\n\n N(2, \"Turkish\", \"sofa\", \"confirmed\",\n   \"Ottoman Turkish صوفا/صفه sofa 'the raised, carpeted hall or dais of a house' is a straightforward borrowing of Arabic ṣuffa, with the regular Turkish treatment of the Arabic feminine ending -a(h) as -a and loss of the gemination. It is this Turkish word — the domestic architectural feature seen by European travellers in the 16th-17th c. — and not the Arabic one directly that Klein makes the source of the European words; Funk & Wagnalls agrees ('< Turk. soffa, < saffa put in line').\",\n   \"«صوفا/صفه» در ترکی عثمانی به معنای تالار یا سکوی فرش‌شدهٔ خانه، وام‌گیری مستقیم از «صُفّة» عربی است؛ پایان مادینهٔ -a(h) عربی در ترکی به -a بدل می‌شود و تشدید از میان می‌رود. کلاین همین واژهٔ ترکی را — که سیاحان اروپایی در سده‌های شانزدهم و هفدهم در خانه‌های عثمانی دیدند — خاستگاه واژه‌های اروپایی می‌داند، نه واژهٔ عربی را به‌طور مستقیم؛ فرهنگ فانک و واگنالز نیز همین را می‌گوید: «< Turk. soffa, < saffa put in line».\",\n   [\"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%A9\"],\n   [{\"ref\": \"KLN:1468\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p. 1468 (KLN_1966.txt leaf 779, which carries the printed numerals 1468/1469): 'sofa, n. — Turk. sofa, fr. Arab. ṣuffah, whence also It. sofa, F. sofa.'\"}],\n   [{\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs, no. 1935 (LKT.txt)\", \"stance\": \"partial\",\n     \"note\": \"'1935. Ar. ṣuffa: \\\"Ruhebank\\\" [vom Vb. ṣaffa \\\"in eine Reihe stellen\\\"]; hieraus ... it. sofà, frz. sofa, sopha, sp. pg. sofá, rum. sofa; engl. ndl. sofa, dtsch. Sofa; russ. sofa.' Lokotsch derives the European words straight from Arabic and does not mention Turkish mediation.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, s.v. sofa (FSD_vol4.txt line 14366)\", \"stance\": \"supports\",\n     \"note\": \"\\\"so'fa, n. A long seat, properly upholstered and having a back and raised ends ... [< Turk. soffa, < saffa put in line]\\\".\"}]),\n\n N(3, \"English\", \"sofa\", \"confirmed\",\n   \"English sofa is first recorded in the 1620s in the Oriental sense 'raised part of a floor covered with carpets and cushions' — i.e. the Turkish sofa as described by travellers — and only by 1717 does it mean the piece of furniture, 'a long stuffed seat'. The Turkish > English route of the chart is Klein's and Etymonline's; the modern furniture sense in fact spread from French/Italian usage, so the English word has a double life, but the etymon is the same Turkish sofa < Arabic ṣuffa.\",\n   \"واژهٔ sofa در انگلیسی نخستین‌بار در دههٔ ۱۶۲۰ در معنای شرقی آن ثبت شده است — «بخش برآمدهٔ کف اتاق، پوشیده از فرش و بالش»، یعنی همان «سوفا»ی ترکی که سیاحان وصف کرده‌اند — و تنها از ۱۷۱۷ به معنای مبل و نیمکت درازِ پشتی‌دار به کار رفته است. مسیر ترکی ← انگلیسیِ نمودار همان مسیر کلاین و اتیمانلاین است؛ هرچند معنای امروزینِ مبل از راه کاربرد فرانسوی و ایتالیایی گسترش یافته، ریشهٔ واژه همان sofa ترکی از «صُفّة» عربی است. ادعای نورایی درست است.\",\n   [\"https://www.etymonline.com/word/sofa\"],\n   [{\"ref\": \"KLN:1468\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p. 1468: 'sofa, n. — Turk. sofa, fr. Arab. ṣuffah, whence also It. sofa, F. sofa.'\"},\n    {\"ref\": \"AHD:1227\", \"status\": \"not_checked\",\n     \"note\": \"the New College AHD page 1227 (dictionary entry 'sofa') is not in the local corpus — only the Watkins IE-roots appendix of that edition is; the same etymology is confirmed by Klein, Funk & Wagnalls and Etymonline.\"}],\n   [{\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt, index line 17672 'SOFA')\", \"stance\": \"partial\",\n     \"note\": \"the headword appears in Skeat's word-list but the OCR of the entry body on that leaf is unreadable; no contradiction, no usable quotation.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, s.v. sofa\", \"stance\": \"supports\",\n     \"note\": \"\\\"[< Turk. soffa, < saffa put in line]\\\" — Turkish intermediary and the Arabic verbal root, as in Klein.\"}]),\n\n N(4, \"French\", \"sofa\", \"confirmed\",\n   \"French sofa (Voltaire still wrote sopha) is attested from the 17th c. and is, in Klein's words, taken from the same Arabic word: 'Arab. ṣuffah, whence also It. sofa, F. sofa'. Devic (p. 210) says the same — 'Sofa ou Sopha ... De l'arabe ṣuffah, même sens ... et aussi le siège de la selle' — and his mention of the saddle-seat is the very sense Nourai puts in the root box; Pihan (p. ~430, s.v. SOFA, ou mieux SOFFAT) insists 'l'origine arabe du mot sofa n'en est pas moins exacte' and notes that the more regular transcription would be soffat because the second radical is doubled. Some modern French dictionaries route the word through Turkish as well; the chart's direct Arabic > French arrow follows Klein, Devic, Pihan and Lokotsch.\",\n   \"«sofa» فرانسوی (ولتر هنوز sopha می‌نوشت) از سدهٔ هفدهم گواهی شده و به گفتهٔ کلاین از همان واژهٔ عربی گرفته شده است: «Arab. ṣuffah, whence also It. sofa, F. sofa». دِویک (ص ۲۱۰) نیز همین را می‌گوید: «Sofa ou Sopha ... از عربی ṣuffah، به همان معنا ... و نیز نشیمنگاه زین» — و همین «نشیمنگاه زین» همان معنایی است که نورایی در جعبهٔ ریشه آورده است. پیان نیز تأکید می‌کند که «ریشهٔ عربی واژهٔ sofa کم‌تردید است» و می‌افزاید آوانگاری دقیق‌تر soffat است چون همخوان دوم مشدد است. برخی فرهنگ‌های امروزی فرانسه واسطهٔ ترکی را نیز می‌آورند؛ پیکان مستقیمِ عربی ← فرانسویِ نمودار پیرو کلاین، دِویک، پیان و لوکوچ است.\",\n   [],\n   [{\"ref\": \"KLN:1468\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 p. 1468 s.v. sofa: '... fr. Arab. ṣuffah, whence also It. sofa, F. sofa.' — French straight from Arabic, exactly the arrow drawn.\"}],\n   [{\"src\": \"DEV\", \"where\": \"Devic p. 210 (DEV.txt line 2134)\", \"stance\": \"supports\",\n     \"note\": \"'Sofa ou Sopha. Portug. sofa. De l'arabe ṣuffah, même sens, dans Bocthor et dans Cherbonneau, scamnum discubitorium dans Freytag, et aussi le siège de la selle.'\"},\n    {\"src\": \"PHN\", \"where\": \"Pihan, s.v. SOFA (PHN.txt line 9227ff.)\", \"stance\": \"supports\",\n     \"note\": \"'SOFA, ou mieux SOFFAT, s. m. (a.) [ṣ'ouffat] estrade en planches, élevée d'un pied environ, couverte d'un tapis ... l'origine arabe du mot sofa n'en est pas moins exacte ... la transcription soffat serait plus régulière, puisque la deuxième radicale du mot oriental est doublée.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1935\", \"stance\": \"supports\",\n     \"note\": \"'hieraus ... frz. sofa, sopha' — French among the words derived directly from Arabic ṣuffa.\"}]),\n]\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Soffeh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Arabic صُفَّة (ṣuffa) 'stone bench, raised platform, covered portico; the seat of a saddle'\",\n \"note\": \"The root box is right as far as it goes: the immediate source of Persian صفّه, Turkish sofa and the European sofa is Arabic ṣuffa, a real word of the ṣ-f-f family, and the three glosses Nourai gives ('seat, saddle, varendah' = veranda) are all attested — 'saddle-seat' is in Devic and in Dehkhoda's Persian entry, 'veranda/portico' is the architectural sense. Two caveats. (1) Naming the box simply 'Arabic' hides a dispute about the word's own origin: Klein and Lokotsch connect it with the verb ṣaffa 'to arrange in a row' (so the traditional Arab lexicographers), whereas Wiktionary, following the Semitists, makes ṣuffa a borrowing from Aramaic ṣippā (ultimately perhaps Akkadian), i.e. a Wanderwort rather than an Arabic denominal. (2) The transcription 'Soffeh' is the Persian pronunciation of the word, not the Arabic one (ṣuffa); the box is labelled Arabic but vocalised in Persian.\",\n \"note_fa\": \"جعبهٔ ریشه تا همین‌جا درست است: خاستگاه بی‌واسطهٔ «صفّه» فارسی، «sofa» ترکی و «sofa» اروپایی واژهٔ عربی «صُفّة» است، واژه‌ای واقعی از خانوادهٔ ص‌ف‌ف، و هر سه معنایی که نورایی داده («سکو، زین، ایوان») گواهی شده‌اند؛ معنای «نشیمنگاه زین» در دِویک و در مدخل دهخدا آمده و معنای «ایوان» همان کاربرد معماری است. دو نکته: نخست، برچسب سادهٔ «عربی» اختلافی را پنهان می‌کند: کلاین و لوکوچ (به پیروی از لغویان عرب) آن را از فعل «صفّ» «به صف کردن» می‌گیرند، اما ویکی‌واژه به پیروی از سامی‌شناسان «صُفّة» را وام‌واژه‌ای آرامی (ṣippā، شاید در نهایت اکدی) می‌داند، یعنی واژه‌ای سرگردان نه مشتق عربی. دوم، آوانگاری «Soffeh» تلفظ فارسی واژه است نه عربی (ṣuffa)؛ جعبه «عربی» برچسب خورده ولی با واکه‌های فارسی خوانده شده است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B5%D9%81%D8%A9\", \"https://abadis.ir/fatofa/%D8%B5%D9%81%D9%87/\"],\n \"ref_check\": [{\"ref\": \"KLN:1468\", \"status\": \"supports\",\n   \"note\": \"Klein 1966 p. 1468 (KLN_1966.txt leaf 779, whose OCR carries the printed page numerals '1468 1469'): 'sofa, n. — Turk. sofa, fr. Arab. ṣuffah, whence also It. sofa, F. sofa.' The Arabic headword and all three descendant boxes of the chart stand on that one line.\"}],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1935 (LKT.txt)\", \"stance\": \"supports\",\n    \"note\": \"'1935. Ar. ṣuffa: \\\"Ruhebank\\\" [vom Vb. ṣaffa \\\"in eine Reihe stellen\\\"]' — Arabic, with the ṣ-f-f etymology.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n    \"note\": \"grep of FVQ_pages.txt for ṣuffa finds no entry — Jeffery does not treat the word as a foreign element of Qur'anic Arabic (it is not a Qur'anic word; ahl al-ṣuffa is a ḥadīth term).\"},\n   {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen\", \"stance\": \"silent\",\n    \"note\": \"grep of AFA.txt for ṣuffa/صفة produces no entry, so the Aramaic derivation now given by Wiktionary is not Fraenkel's.\"}],\n \"nodes\": e1_nodes,\n}\n\ndoc = {\"pdf_page\": 463, \"book_page\": 433, \"verified_by\": \"claude-opus-5\",\n       \"verified_on\": \"2026-09-13\", \"entries\": [e0, e1]}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-463.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-463.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-463.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 463"
}
```


### [2026-09-14T02:44:18.475Z] TOOL RESULT

```
written
JSON_OK
nodes verified: 14/14
node verdicts: {'plausible': 4, 'transcription_suspect': 1, 'disputed': 1, 'confirmed': 8}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 7, 'partial': 3}
books consulted: {'supports': 19, 'partial': 5, 'contradicts': 3, 'silent': 6} | by book: {'KLN': 7, 'FSD': 3, 'BRT': 2, 'PHD': 2, 'MON': 2, 'WEB': 2, 'DEV': 2, 'POK': 2, 'LKT': 2, 'KNT': 1, 'WLD': 1, 'NYB': 1, 'HUB': 1, 'AHD': 1, 'PLA': 1, 'AFM': 1, 'SKT': 1, 'PHN': 1}
```


## [2026-09-14T02:44:23.693Z] TOOL CALL #70: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\np='data/verification/page-463.json'\nd=json.load(open(p,encoding='utf-8'))\nn=[x for x in d['entries'][0]['nodes'] if x['id']==8][0]\nn['ref_check']=[r for r in n['ref_check'] if r['ref']!='KLN:1468']\njson.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 tools/verify_check.py 463"
}
```


### [2026-09-14T02:44:24.878Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'plausible': 4, 'transcription_suspect': 1, 'disputed': 1, 'confirmed': 8}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_checked': 6, 'partial': 3}
books consulted: {'supports': 19, 'partial': 5, 'contradicts': 3, 'silent': 6} | by book: {'KLN': 7, 'FSD': 3, 'BRT': 2, 'PHD': 2, 'MON': 2, 'WEB': 2, 'DEV': 2, 'POK': 2, 'LKT': 2, 'KNT': 1, 'WLD': 1, 'NYB': 1, 'HUB': 1, 'AHD': 1, 'PLA': 1, 'AFM': 1, 'SKT': 1, 'PHN': 1}
```


## [2026-09-14T02:44:43.701Z] AGENT

Page 463 verified; `verify_check.py 463` shows 0 PROBLEM lines.

**Counts** (2 entries, 14 nodes; the 3rd entry `Soito` is a redirect, skipped)
- Roots: confirmed 2 (So/To; Arabic Soffeh)
- Nodes: confirmed 8, plausible 4, disputed 1, transcription_suspect 1
- Ref checks: 8 supports, 3 partial, 6 not_checked · 33 `consulted` entries across 18 books

**Flagged items**
- **disputed** — So/To #4 Avestan `ha-mazan` "the warrior" → Amazon: no such Avestan word exists. Nourai's own source (Watkins/AHD:1541) prints "Hypothetical Old Iranian *ha-maz-an-… (*ha-, with < *sm̥-; see sem-1)… possibly borrowed into Greek", i.e. it belongs under *magh- 'to fight' + *sem- 'together', **not** under the demonstrative *so-/*to-. Klein derives Gk. Ἀμαζών from Heb. ʿammīṣ, Webster from a- + mazos, Beekes/Wiktionary call it Pre-Greek.
- **transcription_suspect** — So/To #2 Pahlavi `avâ`, `avâ-šâm`: not attested MP forms (MacKenzie has ōy, pl. awēšān). The printed page 433 does read "avâ / avâ-šâm", so the extraction is faithful — `error_in: book`. They are Nourai's re-spelling of Mo'in's footnote in Borhan p.197 ("پهلوی avēšān جمع avē"), with â for ē and the Avestan šām grafted on. The same node's `kĕ` is real MP kē but belongs to *kʷo-, not this root.
- Also noted inside `derivation` (not flagged): Persian که in #3 is from MP kū/kē < PIE *kʷo- (Wiktionary), so one of that box's three words does not belong; `awa/awam` in #1 belongs to the deictic *awo- (Pok. 73); the Latin box #5 skips the Greek stage.

**No extraction errors** — the JSON matches the printed page everywhere (checked against a 200 dpi render, copied to `data/verification/sources/refs/ocr/BOOK/463.png`).

Strong confirmations: POK 978-979 + WP II 509 + Mann s.v. *sos* for the root; Horn no. 136 p.31 ("ōi… ap. ava- + hya-") and no. 769 p.170 ("šān… ap. šām; phlv. -šān") for او/ایشان — both exactly the cited pages; Borhan p.1230 (fetched via ref_page.py) carries Mo'in's "پهلوی šān ـ پارسی باستان šām" footnote; Klein p.1468 (leaf whose OCR shows the printed numerals 1468/1469) reads "sofa, n. — Turk. sofa, fr. Arab. ṣuffah, whence also It. sofa, F. sofa", which alone supports the whole Soffeh chart. 8 web pages archived via fetch_source.py.
