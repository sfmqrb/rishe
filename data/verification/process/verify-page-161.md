# Verification process log — verify-page-161


## [2026-09-05T20:30:44.559Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 161 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-161.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-161.json. Write /home/sfmqrb/git/rishe/data/verification/page-161.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 161` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:30:46.106Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:30:46.807Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:30:46.837Z] TOOL RESULT

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


## [2026-09-05T20:30:47.010Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-161.txt"
}
```


### [2026-09-05T20:30:47.025Z] TOOL RESULT

```
1	=== PDF page 161 (book page 131) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Eres 2 : to pierce  (refs POK:335)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:335; KNT:172; TZF:31 | aršti, aštrâ 2 : a short spear ; aršti-bara : spear man (carrier) ☞Bher 1 ; u-ârštika : good spear man ☞Su 1
5	  #2 (parent #1) [Persian] refs=BQT:751, TZF:31 | xešt 2 «خِشت ۲» : a short spear
6	--- entry 1 ---
7	ROOT Ergh -> redirect to Er 1
8	--- entry 2 ---
9	ROOT Ers -> redirect to Eres 1
10	--- entry 3 ---
11	ROOT Ersen -> redirect to Eres 1
12	--- entry 4 ---
13	ROOT Es 1 -> redirect to Aidh
14	--- entry 5 ---
15	ROOT [Indo-European] Es 2, Es-ti : to be  (refs POK:340,341,342; IEC:254)
16	#1 (parent #0) [Avestan] refs=POK:340; KNT:214; IEC:254 | ahmi : I am ; asti : it is ; hant, hat : true, real ; haithya : true
17	  #2 (parent #1) [Persian] refs=IEC:250,254; MON:260,345 | astan «استن» : to be ; ast 1 «است ۱» : is ; -am «-آم» : (I) am
18	#3 (parent #0) [Old Persian] refs=POK:340,341; KNT:214 | amiy : I am ; hašiya : true
19	#4 (parent #0) [Germanic] refs=AHD | izmi : am ; isti : is ; sijai : may it be so, yes
20	  #5 (parent #4) [English] refs=AHD | am ; is ; yes
21	#6 (parent #0) [Latin] refs=AHD | esse : to be
22	  #7 (parent #6) [French] refs=AHD | 
23	    #8 (parent #7) [Persian] refs=VOP:43 | esâns «اسانس» : essence
24	    #9 (parent #7) [English] refs=AHD | essence
25	  #10 (parent #6) [English] refs=AHD | absent, interest, present, entity, proud
26	#11 (parent #0) [Sanskrit] refs=IEC:254, AHD:1298 | asti : is ; su-asti, svasti : well being, good luck ☞Su 1
27	  #12 (parent #11) [English] refs=AHD:1298 | swastica, swastika : an ancient religious symbol adopted in 1935 as an emblem of Nazi Germany
28	--- entry 6 ---
29	ROOT Es-ti -> redirect to Es 2
30	
```


## [2026-09-05T20:30:50.289Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-161.json",
 "description": "Read source JSON page 161"
}
```


### [2026-09-05T20:30:50.323Z] TOOL RESULT

```
{
  "pdf_page": 161,
  "book_page": 131,
  "entries": [
    {
      "root": {
        "name": "Eres 2",
        "lang": "Indo-European",
        "refs": "POK:335",
        "gloss": "to pierce"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:335; KNT:172; TZF:31",
          "words": [
            {"translit": "aršti, aštrâ 2", "gloss": "a short spear", "script": null},
            {"translit": "aršti-bara", "gloss": "spear man (carrier)", "script": null, "see": ["Bher 1"]},
            {"translit": "u-ârštika", "gloss": "good spear man", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:751, TZF:31",
          "words": [
            {"translit": "xešt 2", "gloss": "a short spear", "script": "خِشت ۲"}
          ],
          "note": null,
          "quote": {
            "text": "چو شیر نر بر آن خوک درژم تاخت - سیه پر خشت پیچان را بیانداخت",
            "poet": "Vîs-o-Râmîn"
          }
        }
      ]
    },
    {
      "root": {"name": "Ergh", "redirect": "Er 1"},
      "nodes": []
    },
    {
      "root": {"name": "Ers", "redirect": "Eres 1"},
      "nodes": []
    },
    {
      "root": {"name": "Ersen", "redirect": "Eres 1"},
      "nodes": []
    },
    {
      "root": {"name": "Es 1", "redirect": "Aidh"},
      "nodes": []
    },
    {
      "root": {
        "name": "Es 2, Es-ti",
        "lang": "Indo-European",
        "refs": "POK:340,341,342; IEC:254",
        "gloss": "to be"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:340; KNT:214; IEC:254",
          "words": [
            {"translit": "ahmi", "gloss": "I am", "script": null},
            {"translit": "asti", "gloss": "it is", "script": null},
            {"translit": "hant, hat", "gloss": "true, real", "script": null},
            {"translit": "haithya", "gloss": "true", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "IEC:250,254; MON:260,345",
          "words": [
            {"translit": "astan", "gloss": "to be", "script": "استن"},
            {"translit": "ast 1", "gloss": "is", "script": "است ۱"},
            {"translit": "-am", "gloss": "(I) am", "script": "-آم"}
          ],
          "note": null,
          "quote": {
            "text": "امروز که در دست توام مرحمتی کن - فردا که شوم خاک چه سود اشک ندامت",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:340,341; KNT:214",
          "words": [
            {"translit": "amiy", "gloss": "I am", "script": null},
            {"translit": "hašiya", "gloss": "true", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "izmi", "gloss": "am", "script": null},
            {"translit": "isti", "gloss": "is", "script": null},
            {"translit": "sijai", "gloss": "may it be so, yes", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "am", "gloss": null, "script": null},
            {"translit": "is", "gloss": null, "script": null},
            {"translit": "yes", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "esse", "gloss": "to be", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "VOP:43",
          "words": [
            {"translit": "esâns", "gloss": "essence", "script": "اسانس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "essence", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "absent, interest, present, entity, proud", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:254, AHD:1298",
          "words": [
            {"translit": "asti", "gloss": "is", "script": null},
            {"translit": "su-asti, svasti", "gloss": "well being, good luck", "script": null, "see": ["Su 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD:1298",
          "words": [
            {"translit": "swastica, swastika", "gloss": "an ancient religious symbol adopted in 1935 as an emblem of Nazi Germany", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Es-ti", "redirect": "Es 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:30:50.654Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:30:50.692Z] TOOL RESULT

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
```


## [2026-09-05T20:30:56.184Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','TZF','BQT','IEC','MON','AHD','VOP','BRT','HRN','HUB','PHD','NYB','WLD','SYN','KLN','SKT','ARY','CHEUNG','FFD','IRN','LEW','LAT','FSD','WEB','TLM','AVG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-09-05T20:30:58.325Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadab

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/v

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

TLM {"title": "H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Series, 1908", "edition_found": "1908", "kind": "archive_djvu", "url": "https://archive.org/details/ancientpersianle00tolm_0", "identifier": "ancientpersianle00tolm_0 (also in.ernet.dli.2015.90691, ancientpersianl00tolmgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/TLM.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 24 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

AVG {"title": "A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892", "edition_found": "1892", "kind": "archive_djvu", "url": "https://archive.org/details/pt1avestagrammar00jackuoft", "identifier": "pt1avestagrammar00jackuoft (also an-avesta-grammar-in-comparison-with-sanskrit, in.ernet.dli.2015.47742)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AVG.txt", "page_offset": "leaf = printed + 54 (e.g. leaf 61 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/det
```


## [2026-09-05T20:31:04.273Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 343 344; do echo \"=== POK_01 leaf $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_01.txt | head -80; done"
}
```


## [2026-09-05T20:31:04.286Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-05T20:31:06.117Z] TOOL RESULT

```
=== POK_01 leaf 343 ===
erativ  a-ar-as-ld-it  (arsJcit)  ,gelangte  wiederholt'  (vgl.  oben  ai. rcchdti) ;
5.  Kausativ  (vgl.  oben  S.  61)  ar-nu-uz-zi  (^arnuzi)  ,bringt  wohin,  setzt in  Bewegung'  (j-nu-]  vgl.  oben  ai.  rnöti)\  Imper.  2.  Sg.  ar-nu-ut  (arnut) =  gr.  oovv-d-i,  Verbaln.  a-ar-nu-mar  (arnumar) ;
inwieweit  toch.  A  ar-,  B  er-  ,hervor bringen,  verursachen',  mit  sÄ-Kaus. ars-,  ers-  ds.,  nach  Meillet  (MSL.  19,  159)  hierher  gehören,  ist  unsicher ; sicher  fern  bleiben  AB  ar-,  är-  ,aufhören',  mit  s/:-Kaus.  ars-,  ärs-  .verlassen' (ungenau  Van  Windekens  Lexique  6,  22).
h.  Erweiterung  er-ed-  (c?-Präsens ?) :  s.  ered-  .zerfließen',  ai.  drdati, rddti    ,fließt   usw.',  auch    ,beunruhigt' ;    mit   dem   Kaus.    arddyati    ,macht
330  ^
fließen;    bedrängt,    quält,   tötet'    wäre  aisl.  erta  {*artjan)  ^aufstacheln^  an reizen,  necken'   gleichsetzbar,    doch   ist  Verknüpfung   mit   *ardi-   ,Spit2A Stachel'  (oben   S.  63)  mindestens  gleichwertig;    eine   zweisilbige  Form  i' ägaC^ovai'  ige^i^ovaiv  Hes.,  IxQaöog  , Erregung';
weiter   hierher   oder   zu   5.  er-   ai.   rddati   ,kratzt,    ritzt,   gräbt,   hackt^ vi-radati  , zertrennt,  eröffnet';
vielleicht  auch  apr.  redo  ,Furche'  (Persson  Beitr.  667).
c.  Erweiterung  er-edh-:  s.  oben  S.  327  ige-d-cj  usw.   u.  unten  S.  339
d,  Basis  erei-]  und  reis- :ri-}-rolo-s,  ri-ti-  ,Fließen'. Ai.  irya-  s.  oben  S.  327 ; ai.  rinätiy  rinvati  (drinvan)   ,läßt  fließen,  entlaufen,  entläßt',  rlyate    o-q.
rät  ins  Fließen,  löst  sich  auf,  rina-  ,in  Fluß  geraten,  fließend',  rlti-  ,Strom Lauf,  Strich;  Lauf  der  Dinge,  Art,  Weise'  (letztere  Bed.  auch  in  mir. rlan  ,wa7,  manner'),  rit-  ,entrinnend',  raya-  m.  ,Strömung,  Strom,  Lauf Eile,  Heftigkeit',  retas-  n.  ,Guß,  Strom,  Same',  renn-  m.  ,Staub'  (:  aruss, renh  ,Sandbank');  zum  w-Suffix  vgl.  unten  \a.t.  ilvus;
arm.  ari  ,stehe  auf!'  (Persson  Beitr.  769)  Zu  y-afnem,  S.  327;  ^^^^
gr.  lesb.  dgtvcüj  (*dQl-viüj)  ,setze  in  Bewegung,  errege,  reize  zum  Zorn'1* egig,    -löog  ,Streit'    (vielleicht   im   i   zu    unserer   Wurzelform,   falls  nicht i- besser  nach  Schwyzer  Gl.  12,  17  zu  igstdo)  , stütze,  stemme,  stoße,  drängeO^r* ark.   igivvsiv  ,zürnen'  aus  ^Egivvg  eig.  ,die  den  Mörder  verfolgende,  ztiivj nende  Seele  des  Ermordeten'  (??) ;  ''**S'
alb.    geg.   rite    , feucht,    naß',    eig.   ,*fließend'    (*ri
=== POK_01 leaf 344 ===
nete  :  ai.    rindti,  8\&y,'h rinoti) ;  "^
lat.   oriorj    ongo   s.  oben;   rlvus   (*rei-uo-s)   ,Bach';    in    dem   abg.  rtvhUh ,Nebenbuhler'     entsprechender     Bedeutungswendung    rlvlnus    und    rivälU ,Nebenbuhler    in    der    Liebe'    (letztere   Form    Umbildung    nach    aequalis,' södälis),  eigentlich  ,Bachnachbar' ;
wahrscheinlich  hierher  irrltäre  ,erregen,  aufbringen,  erbittern',  jpron^flr«  n^^ ,hervorreizen,  durch  Reiz  hervorbringen,  anreizen,  anlocken',  (wohl  Intensiva zu  einem  *ir-ri-re) ;  '  -
ir.   rlan   ,Meer'   und    (vgl.  ai.  r'iti-)    ,Art,  Weise',   gall.    Renos   (*reinos)^4 ,Rhein'  (ob  auch  nach  Stokes  KZ.  37,  260  ir.  riasc  ,a  marsb',  rzm  ,schlechte8  j^ Wetter'??),  cymr.  rhidio  ,coire'  (:  ags.  rld^  ai.  riti-h),  air.  riathorj  cymr rhaiadr,  acymr.  reatir  ,Wasserfall'  {*riia-tro-)]
ags.  rid  m.  f.,  ride  f.  , Strom,  Bach',  as.  rxth  m.  ,torrens',  mnd.  ride  Vm_ ,Bach,  Wasserlauf',  nhd.  -reid{e)  in  Ortsnamen;  Dimin.  (^rtpulön)  ndd rille  ,Furche  nach  Regen wasser,  Rinne';  weiters  ags.  ä-rceman  ,erheben,  sich erheben',  mengl.  r^men^  engl,  roam  ,umherstreifen',  aisl.  reimudr  ,Umher- streifen',  reimir  ,Schlange',  par  er  reimt  ,da  ist  es  nicht  geheuer,  spukt, reima  ,infestare'  (Bed.  wie  abg.  rijati  ,stoßen').    Über  rinnan  s.  oben.
331
as.
Mit  germ.  s-Erweiterung:  got.  urreisan  ,auf stehen',  aisl.  risa^  ao-s. rtsan  ;Sich  erheben',  ahd.  risan,  mhd.  rlsen  ^steigen,  fallen';  ahd.  reisa ^Aufbruch,  Zug,  Kriegszug,  Reise',  ^ot^urraisjan  ,aufstehen  machen,  auf- richten, erwecken',  aisl.  reisa  ds.,  ags.  rceran  ,erheben,  aufrichten,  er- richten', ahd.  reren  ,fallen  machen,  herablaufen  machen,  vergießen';  ndd. reren  ,fallen',  mhd.  riselen  ,tropfen,  regnen',  nhd.  rieseln^  mhd.  risel  m. ^Regen',  aisl.  blöd-risa,  mhd.  bluotvise  ,blutbespritzt',  afries.  blödrisne  ,blutende Wunde';  aus  , fallen'  wird  ,gefallen'  in  ags.  (ge)rlsan  ,ziemen',  ahd.  garlsan ^zukommen,  geziemen'  (vgl.  die  s-Erw.  abg.  ristati),  mhd.  rkch,  hurtig, schnell'  (vgl.  abg.  riskanije)\
lit.  ry-tas  ,Morgen'  (,*Sonnenaufgang',  vgl.  got.  urreisan),  lett.  rietu, -6Ju,  -et  ,hervorbrechen,  aufgehen  (z.  B.  vom  Tag),  hervorströmen',  riete ,Milch  in  der  Mutterbrust'  (vgl.  formal  ai.  reta-)]
slav.  "^raia-  m.  ,Strömung'  ( :  oben  ai.  raya-h  m.  ,Strom,  Lauf)  in  abg. izrojh  ,Samenerguß',  s^rojh  ,Zusammenfluß',  naroj  , Andrang',  roj  ,Bienen- schwarm'  (*roto-s);  dazu  reka  (*roi-ka)  ,Fluß';  slav.  *reiö  ,stoße'  in  aksl. rejqj  rejati  ,fließen'  (nslav.)  und  ,stoßen,  drängen'  (wie  dgirco  ,bewege'); dazu  ablautendes  aksl.  vy
```


### [2026-09-05T20:31:06.150Z] TOOL RESULT

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


## [2026-09-05T20:31:16.063Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arsti\\|aršti\\|arstay\\|Speer\" POK_01.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:31:16.150Z] TOOL RESULT

```
208:Gl-,  alaxog  n.  , Schande'  (aus  *aig'^h-s-kos,  /v-Ableitung  von  einem  s-St. *aig'ihes-,  wie:)  got.  aiioiski  n.  , Schande,  Beschämung';  vgl.  weiter  aiaxvvri , Scham,  Ehrgefühl,  Schande',  «iö'xui'w  , entehre,  schände,  entstelle',  med. , scheue  mich,  schäme  mich',  alaxQog  , schimpflich,  schmachvoll;  garstig*; got.  unaiivisks  , schandlos',  aiwiskön  , schändlich  handeln',  ags.  Icwiscie)  n. , Schande,  Vergehen',  Adj.  , schamlos*,  mnd.  eisch  , häßlich,  abscheulich', nnd.  eisk^  aisch  , ekelhaft,  garstig^
840:Arm.  ardn  , Lanze,  Speer'  :  lit.  ardas  m.  , Stangengerüst  zum  Flachs- trocknen', alt  ardamas  ,die  in  der  Diagonale  des  Segels  stehende  Spreiz- stange' (s.  zur  Bed.  Bezzenberger  GGA.  1885,  920)'?  Petersson  KZ.  47, 245  (die  lit.  Wörter  nicht  besser  nach  Leskien  Abi.  329  zu  ardyti  ,spal- ten,  trennen',  s.  unten   er-  ,locker').
1467:mir.  bare  ^Speerschaft'.  cymr.  barch  f.  .Speer',  slav.  bhrk^  in  skr.  brk .Spitze.  Keim.  Schnurrbart',  cech.  bi-k  .Kiel.  Schwungfeder',  auch  wohl russ.  berce,  berco  .Schienbein',  dial.  .Pfahl'   (Berneker  119).
1476:Lat.  fastigium  (Hharsti-)  ,Spitze,  Gipfel,  Abdachung^,  hierher  vielleicht fastus,  -üs  m.  ,Hochmut,  Stolz^  (^w-Stamm),  dazu  fastldium  ,Ekel,  Über- druß, Stolz^  (aus  *fasti-tidium^  zu  taedium)\  s.  auch  Pisani  Rc.  R.  Ist. Lomb.  76,  2,  17  f.';
1641:WP.  II  137  f.,  WH.  I  503  f.,  506,  Trautmann  33,  Liden  KZ.  61,  12: Karstien  KZ.  65,  154  f.
3078:Gr.  SÖQv  , Baumstamm,  Holz,  Speer'  (Gen.  honi.  Sovgög,  trag.  doQÖg  aus *doQf6g,  öovgarog,  att.  dögazog  aus  *SoQj^nTog^  dessen  n  mit  ai.  drünah vergleichbar  ist);
3080:sizil.  äa%edo}qog  ,Eber'  (nach  Kretschmer  KZ.  36,  267  f.  '^dv-a%s-doQj^og oder  -dwgJ^og  ,dem  Speere  standhaltend'),  ark.  dor.  JwQL-y.X^gj  dor.  böot. Ja}Qi-f,iaxog  u.  dgl.,  JcoQisvg  ,Dorer'  (von  Jcogig  ,Waldland');  dgvg,  dgvög , Eiche,  Baum'  (aus  dem  n.  *c??nt  oder  *dervj  *doru  g.  "^druuös  nach  andern Baumnamen  zum  Fem.  geworden;  infolge  der  Einsilbigkeit  Nominativ- dehnung), dycgö-dgva  , Fruchtbäume',  dgv-iöfiog  , Holzhacker',  dgvLvog  ,von der  Eiche,  von  Eichenholz',  Jgvag  ,Baumnymphe',  ysgdvögvov  ,alter  Baum- stamm', ädgva '  Ttlola  ^ovö^vXa '  KvngLoi  Hes.  (*6'^-,  Lit.  bei  Boisacq  s.  v.), evögvov  xagöia  divögov  Hes.
3580:hierher  wohl  lit.  dergia  (dergti)  .es  ist  schlechtes  Wetter',  ddrganaj ddrga  .quatschiges,  schlechtes  Wetter'  (Stoßton,  vgl.  die  gr.  Wurzelformen und  lit.  dregnas,  dregnüs  .feucht');  dazu  aruss.  padoroga  wohl  .Unwetter', sloven.  sy-dragaj  -drag,  -drga  .kleinkörniger  Hagel;  gefrorene  Schnee- klümpchen.  Graupeln';  lit.  dargüs  .garstig,  schmutzig';  alit.  dergesis .unflätiger  Mensch',  alit.  dergeti  .hassen',  lett.  derdzeties  .zanken,  streiten' (Mühlenbach-Endzelin  I  456  m.  Lit.),  apr.  de^-gt  ,sie  hassen';  lit.  dergti .schmutzig  werden,  beschmutzen',  dargti  ,beschimpfen',  ddrga  f.  , regne- risches Wetter,  Besudelung,  Beschimpfung';
3584:c.  dherk-  in:   lit.  derkti  ,garstig  machen,  besudeln',  darkyti  ^schmähej schimpfen,  entstellen',  darkus  ,garstig',  apr.  erder kts  ,vergiftet',  lett.  därl därci   (*darkis)    ,Schecke''  Mühlenbach-Endzelin   I  448    (s.  die    Sippe Leskien  Abi.  361);    oder  zu  mhd.  zurch  ,Kot',  zürchen  ,cacare'?   Zupitz^ Gutt.  170  unter  Betonung  des  Intonationsunterschiedes  von  derkti  gegen» über   dergesis  usw.;
4687:^oö'TjVsy-rjg  ;bis  zu  den  Füßen  herabreichend^,  dovQ-r]vsyirjg  ,einen  Speerwurf ^yeit^  ==  ;S0  weit  man  mit  einem  geschleuderten  Speere  reicht'  oder  pass. vom  Speer  erreicht',  wie  y.evTQ-7]v8yirjg  ,vom  Stachel  (erreicht  =)  angetrieben'; Pass.  Aor.  '^vsx^rjv  ,wurde  getragen',  Perf.  xar-rjvoyia  Hes.,  h-rjvoxa  (iv- ist  darin  wohl  Reduplikation;  ebenso  im  Med.  iv-rjvsy(.iaL,  zu  dem  sich als   3.  Sg.  iv-rjveyycTai   statt  Hv-rjvs'/iTai  gesellte,   nach   dem  Aor.  iveyy,eTv)]
5014:Ai.  rsdti  ,stößt,  sticht',  rHk  ,Speer',  av.  arUi-  ds. ; lit.  ersketis  , Dornpflanze',  vgl.  oben  S.  67 ; sloven.  r^sdk  ,Gänsedistel'. Persson  Beitr.  84.   Verschieden  davon  ist:
```


## [2026-09-05T20:31:17.185Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /es-, sein|es- +,sein|esmi|,sein\\x27/ {print NR\": \"substr($0,1,300)\"\\n---\"}' POK_01.txt | head -40"
}
```


### [2026-09-05T20:31:21.619Z] TOOL RESULT

```
156:   Abgrund^).
Wie  lit.  burnä,  arm.  beran  ,Mund^  (eigentl.  ,Offnung^)  zu  bher-  ,schneiden^ unter  einer  Anschauung  ,Kluft  ==  Schlund^
WP.  II  171,  WH.  I  482,  551  f.,  866,  Liden  Mel.  Pedersen  92,  Specht Dekl.  162.
X.  bbes-  ,abreiben,  zerreiben,  ausstreuen^.
Ai.  bdbhasti
---
157: nd  bJiüvat,  Perf.  .  babhuva,  Partiz.  Perf.  Akt.  babhüvän,  f.  babhüvusl (:  gr.  7t6q)V(bg,  Ttecpvvla,  lit.  büvo,3iks\.  byvati),  Inf.  bhdvitum,  Absol.  bhütvä (vgl.  lit.  büty,  Supinum  ,zu  sein',  apr.  büton  Inf.);
a.i.  bhütd-h,  av.  büta-  ,ge worden,  seiend,  ai
---
158: a  ,kleines  Nest'  aus  *bitlja.
Als  2.  Kompos.-glied  in  vftsgcpvi^g,  vTC€Q-g)[*f]iaXog.    Über  q)Trv  s.  unten.
Illyr.  VN  Buni,  ON  Bovvvog  (:  iilb.  bune).
Messap.  ßvQLov  6Lxr][.i(Xj  ßavqla'  ohia  Hes.  (:ahd.  bür);
10*
148
alb.  hujj  hüj  (*bunjö)  ,wohne,  übernachte
---
159:   Formen  von  es-  und  bheu-,  z.  B.  hat  die 1.  Sg.  Präs.  Konj.  air.  beu  (*bh-esö)  den  Anlaut  von  bheu-  bezogen;
air.  -biu  ,ich  pflege  zu  sein',  mcymr.  bydaf  corn.  bethaf  mbret.  bezaff ds.  {Hhuij,ö  =  lat.  fiö,  daneben  *bhui-  in  air.  blth,  mcymr.  bit  ,estö'
---
202: ek-)  ^reißen,  zerreißen,  zerfasernd ^*  \[  dasä  ;die  am  Ende  eines  Gewebes  hervorragenden  Zettelfäden, r-ansen^;  ir.  dual  ,Locke^  {*doklo-)\  got.  tagl  n.  ,einzelnes  Haar^,  anord. titql  u.  ,die  Haare  im  Pferdeschwanz*^,  ags.  tcegl  (engl,  tau)  m.  _,Sch\vanz^,. alid.
---
203: �ltere    Erklärungen    bei   WH.  I  327  f.  und   Feist  If S.  aucb  unten  unter  centuria  u.  Kluge ^^  unter  Becker.
Ablautendes  (d)ktpt'  (Dual),  {d)komt'  (Plur.)  in  den  Zebnerzablen  (^^ die  Bildungen  bis  50  sind  als  idg.  nacbweisbar),  z.  B.  ai.  trimsät  ,30', d-risq
---
294: nn  Dem.  32 ff.,  BSGW.  60,  41  ff.,  Grundr.  IP  2,  324 ff., Pedersen  Pron.  dem.  311  ff.
A.  Kasuell  verwendete  Formen:
ai.  aydm  ,er'  =  gthav.  ai/9w,  jav.  aem  (nach  ahdm  ,ich'  erweitertes  ar. *ai  =  idg.  *ei;  idg.  *ei  vom  St.  e-,  wie  *quo-i  vom  St.  kuo-^  nicht  H
---
295: rde  und  eam  usw.  nach  sich  zog;  tarn  bei  Varro  1.  1.  5,  166 und  8,  44  wohl  Schreibfehler  für  eam.  —  Aus  dem  Lat.  hierher  ipse  aus *ls-pse  (wegen  alat.  fem.  eapse),  is-te  (aber  ille  erst  danach  umgebildetes  - olhts),  vgl.  umbr.  estu  ,istumj  ista';
air.  e 
---
354: Marstrander  ZceltPh.  7,  360;  vgl.  oben  S.  65.
ers-  :  orsos  , Hinterer,  Schwanz*.
Arm.  or  ,  Hinterer'  (meist  PI.  or-k,  i-St.);
gr.  bggog  m.  , Hinterer'  (dazu  oigd  f.  , Schweif  aus  *ors{a)  =  ^|;*
ahd.  a?'s,  ags.  ears  m.,  aisl.  ars,  rass  ,  Arsch'  =  '  ^
hitt.  a-
---
```


## [2026-09-05T20:31:28.405Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nimport re\ni=t.find(\"rHk  ,Speer'\")\nprint(\"charpos\",i)\nprint(\"leaf\", t.count('\\f',0,i)+1)\nprint(t[i-2500:i+600])\nEOF"
}
```


### [2026-09-05T20:31:30.127Z] TOOL RESULT

```
charpos 947831
leaf 349
  Rednitz  (Bayern)  aus  *Rodantia.
WP.  I  148,   Pokorny  Mel.  Boisacq  II  193  ff.
335
eregai.h)0',  erog^{h)o'  ,Erbse,  Hülsenfrucht^
Gr.  b'goßog  m.  (aus  ^eooßog  nach  dem  Gen.  usw.  doößov);  vgl.  aber ^V.  Schulze  Kl.  Sehr.  81),  egeßLvd-og  m.  (das  kleinasiat.  Suffix  erweist nicht  gerade  solche  Herkunft,  da  in  Pflanzennamen  auch  sonst  vorkommend, so  in  Ußivd-oi'  iqsßivd^oi  Hes.)  ,Kichererbse^ ;
lat.  ervum  n.  ,eine  Hülsenfrucht^  (aus  *eroiwm,  '^eregu(h)om  oder *erogi^{h)om)]
ahd.  araweiz,  ariciz,  nhd.  Erhse,  as.  er(iw)it,  rand.  erwete,  ndd.  erwten PL,  anord.  ertr  f.  PL  (Dat.  ertrum)  ds.  (-ait  wohl  bloßes  Suffix);
aber  mir.  orbaind  ,grains^  steht  für  ^ärbainn,  älter  arbanna  (oben  S.  63).
Wahrscheinlich  Entlehnungen  aus  einer  gemeinsamen,  wohl  ostmedi- terranen Quelle,  aus  der  auch  ai.  aravindam  , Lotosblume'  stammt.
WP.  I  145,  WH.  I  41 9 f.,. 863.
j.  erek'  (er[e]g-i2-)  ,Laus,  Milbe^  oft  tabuierend  entstellt.
Ai.  lik^ä  ,Nisse,  Lausei'  (wohl  aus  *laksd  durch  Einfluß  von  likhdti ,ritzt') ;
lat.  ricinus  1.  ,ein  sich  in  die  Haut  von  Schafen,  Hunden  oder  Rind- vieh einbohrendes  Ungeziefer,  Zecke'  (unsicher  ist  die  Zugehörigkeit  von 2.  ,eine  Strauchart,  Ricinus  communis')  kann  auf  älteres  *recinos  zurück- gehen und  mit  lit.  erke  , Zecke,  Schaflaus'  (*erkia),  lett.  erce  , Kuhmilbe, böse  Person'  unter  idg.  *erek-  zusammengehören.  Weiterhin  ist  zu  ver- gleichen arm.  o{r)jil  ,Nisse,  Lausei'  (hier  scheint  eine  Wurzelvariante er{e)gh-  vorzuliegen,  wie  auch  in  der  folgenden  alb.  Form)  und  orJciun ,ringworm,  itching,  erysipelas'  (aus  *orqiiöno-  (?)  mit  einem  -rzo-Suffix  wie im  Lat.  nach  Petersson  KZ.  47,  263  f.),  alb.  ergjiz  ,kleine  Laus'  (s.  ü.  Meyer Alb.  Wb.  96;  Zweifel  bei  Hermann  KZ.  41,  48;  doch  kann  der  abweichende Guttural  im  Armen,   und  Alban.   auf   tabuierender   Entstellung    beruhen).
WP.  I  145,  n  344.
2.  er(e)k',  rek-,  rok-  ,auf reißen,  spalten,  schinden'.
Ai.  rknd-h  ,geschunden,  kahlgerieben',  r^sdh  ,kahl',  rksara-h  ,Spitze, Dorn';
lit.  j-erkä,  pra-j-erkä  ,Schlitz';  (über  lett.  ercis  ,Wacholder'  usw.  s.  oben S.  67  f.) ;  mit  anderer  Ablautstufe  lit.  ranküj  räkti  ,aufstochern',  rakUis , Splitter,  Dorn',  usw.
Persson  Beitr.  839.   Dazu  .gehört  auch :
I.  eres-  , stechen'.
Ai.  rsdti  ,stößt,  sticht',  rHk  ,Speer',  av.  arUi-  ds. ; lit.  ersketis  , Dornpflanze',  vgl.  oben  S.  67 ; sloven.  r^sdk  ,Gänsedistel'. Persson  Beitr.  84.   Verschieden  davon  ist:
336
f
2,  ere-S'  (ers-,  ^s-,  e^es-),  und  r€s-,  rös-  ,fließen ;  rosa  ^Feuchtigkeit Tau';  von  lebhafter  Bewegung  überhaupt,  auch  ^umherirren'  und  ,auf- geb rächt,  aufgeregt  sein';  e^esiä  ,Übel wollen'  (S.  337).
1.  Ai.  rdsa-h  _,Saft,  Flüssigkeit',  o^asä  , Feuchtigkeit,  Naß',  auch  mythischer Flußname  gleich  av.  Ranhä  (d.  i.  Eahä),  daraus  der  Name  der  Wolga  ^pg.
lat.  rös,  röris  ,Tau'  (kon
```


## [2026-09-05T20:31:51.737Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT arsti ===\"; grep -n -i \"aršti\\|arsti\\|ạršti\" KNT.txt | head -30; echo; echo \"=== BRT arsti ===\"; grep -n \"aršti\\|arsti\" BRT.txt | head -30"
}
```


### [2026-09-05T20:31:51.795Z] TOOL RESULT

```
=== KNT arsti ===
1438:Saka-, Sug(u)da-, Nisdya-, si*kabru-, and the 3 dubious siyamam. 3 5117. рів. f from pIE s after certain sounds 1 (8115) remained unchanged in OP: у ОР тав: Ма- ‘greatest’, Av. masisla-, Gk. шікито 5 "longest". : OP fràisayam ‘I sent’, Skt. ejayat? ‘he brings’, OP uška- ‘dry’, Av. huska-, Lith. satisa-s. OP gausa- ‘ear’, Skt. ghóga- ‘noise’. 4 OP adarínaus ‘he dared’, Skt. dhysnéti ‘he dares’. 4 OP aría- ‘male’ in ArSama- ‘Arsames’, Skt. 4 rsa-bhd- ‘bull’. 4 pIE *sed-as- in ОР Лай ‘seat’, cf. СК. &os (from -$ pIE *sedos). 4 pIE *e-st-sfe-to, OP ачЧаіа ‘he stood’, cf. Gk. : israrat ‘he stands’ (from *sestatat). 4 pIE *rsti-, OP nom. arštiš, Skt. rstf-s (cf. $115). 4 OP nom. tani ‘body’, Skt. tani-s. 4 For ks and other clusters giving zš, see $102; 4 for kn and gn giving initial тп and medial im, 4 $06; for -Sc- as a sandhi product, $105; for pAr. 4 & giving OP Sy, $104; for pAr. t giving OP y 4 $80; for pAr. én giving OP $n, $82. 1 The verbal prefix ni- affects an initial s of the 4 verbal root; thus ni-$d- from ni- + stä- and 4
1524:*bher- ‘bear’ in bara*tiy ‘they bear’; *bhor- in aršti-bara ‘spear-bearer’; *bhr- in u-bar-tam ‘well uplifted’; *bhór- in asa-büra- ‘horse-borne’, uSa-büri- ‘camel-borne’.
1785:Agents: baga- ‘dispenser, god’; drauga- ‘deceiver, the Lie’; arSti-bara- ‘spear-bearer’; züra-kara- ‘evil-doer’; dáraniya-kara- ‘gold-worker, gold- smith’,
1895:arSti-bara- 'spear-bearer'; vaga-bara- ‘bow-bearer’ ; taka-bara- ‘petasos-wearing’.
2145:III. It is not always possible to determine whether the feminine common nouns are -f- stems or -2- stems; etymological comparison is necessary The short vowel seems assured in aršti-, Skt. rstí- ‘spear’; palim, Skt. stem pathi- in some case-forms;
2887:Ратѕаћуй martiyahyd düraty arsti$ paragmata ‘the E |
4179:2 yavahaus : xSayafiyahya : arStibara рма 1 Аѕрасапё : vagabara : Darayavahaus :
4187:Nores то DN, MINOR INSCRIPTIONS: DNo: *'arstibara, engraved &r¢sti*2bh+r?; the original draft was miswritten ато5чіа ота, and the $, intended to replace the s*, was by error inserted in the place of the a. (But the first en- graved character is read by Cameron from photographs not as 5%, but ав Ле; for а miswritten йе І can offer no explanation).
5084:аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
5086:arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
5158:^u- insep. prefix ‘good, well’ (uv- before vow- els): Av. hu-, Skt. su-, Gk. 0-уиѕ ‘having good life, healthy’, pIE *su- (§140.IV): in uxSnav-, ukàra-, ucüra-, Utüna-, ulava-, ubanwaniya-, ufrasta- ufrasta-, ubarta-, umartiya-, иғада-, uradana-, Uvaxstra-, &Uvürazmi-, warstika-, uvdsabdra-, waspa-, dinara-, uwkhamaranakara-.

=== BRT arsti ===
3675:•  j.  apänk-  :  apak-  Adj.  (fem.  apacl-)  'nach hinten,  rückwärts  gewendet':  "^//(NSf)" vazaili  arstiS  yqm  . .  "rückwärts  fliegt  die Lanze,  die  . ."  Yt.  10.  ao.  a)  NSm. als  Adv.'>:  °Pq^  ^avS  damayäti  "nach hinten  (auf  den  Rücken)  fesselt  er  ihre Hände"  Vt.70. 48.  b)  IS.  als  Adv. 'zurück': *'pasa^'>  vi  *zamar?  ana  duye*  {%A.)\i.i. 2g;  —  uzg?r>pt3mHt  saa'^pm  -pasa  apa.- j^anvainti  (sd^  Yt  14.46.
3846:•  j.  aiwi.druxtäe  Inf.  'zu  belügen,  be- trügen' :  nBit  imat  j'Ispim  äuwarU^m  nöil vispsm  üiiiii-df  (n'äml.  varstim)  mi^rö vasnaili  ". .  nicht  alles,  was  zum  Trug (getan  ist)  . ."  Yt.  jo.  io5(?).
5359:•  j.  *ar»m.uxtay  ■'  f.  'rechtes,  angemesse- nesSprechen':  *ar7m.maiH  *kumata  mamne (sd.)    "uxti    küxta     anm.varsti     kvarasta
5664:•  j.  paiti.b?r>tim  "arstiätim  N.  2. VtrniBlt  SuperL;  s.  vorher.  —  Pü. :  fehlt.
6722:1)  'werfen  (eine  Waffe),  schiessen':  arstii yqm  *an/iyeili'^  avi.>tiiiris  Yt  10.  ao;  *2i; —  tiyris" .  ,  yi'm  an/iaf  »rsxsö  (sd.)  Yt  8. 6;  —  äsyatjka  Avastayn  {sA.)  *arikima- nayäi^  (GD.)  Y.57.  28;  —  yalat  hvasttm (sd.)  *a»Ayeiti''>  Yt/0. 21;  —  asia  F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^'>  "der Feind  wurde  ins  Wasser  gedräng "" /.  19.
9805:•  p.  *gau'bruva-'>  m,  EN.  eines  Persers, Genosse  Darios  I.  bei  der  Magophonie, Gobryas:  'v<^  pätil^uvarU däraya  vakaus xsäyä^iyahyä  arstibara''  "G.,  der  Patt' scAorier,  des  Königs  Z>.  Speerträger"  D. 8;  —  °J'o*  nämt^  mardutiiyaAyä  J>u^''a!' pärsa''  Bh.4. 18;  5.1'.
10054:—  11  pärsahya  martiyakyä  *dliraiy  arstis /«rJ^OTtf/a(NSf.)  "des  persischen  Mannes' I.anze  ist  weit  in  die  Ferne  gekommen" D.  /;.  4.
13835:duh-arstimca  V.J.  20;  42,  Y.  77.  8,  7,  Yt /0. 106'';  —  hüxtahe  ahmt  'tahe  iiHi ahmt  Y.  /o.  16;  7/.  7;  —  nizbarimnB  .  . °l(ua  H.J.  7;  Fr\V._y.  I,  2;  —  aibigaityä äaßil  vJspä  . .  hüxta'ä  ,.pairirifyä  dai%t vlspH  . .  °tälä  Y.ii.iT,  —  yai  fraoirilaiti fairi  ..  -taiifyasc'a  H.  i.  ij;— paili//,U^ .  .  'tanqmca  Vr.  20.  2.
14991:•  j.  paiti-bsrstay-  f,  'Darbringung':  ä 'rntlm  ^»ntnistim  N.3; — 'ritim  ^arstistim
15963:•  p.  pätiä''uvaray-  Adj.  'aus  Patis''uvara stammend, /'arfjf^örer'"':  ^gaubruvc^  'ris darayc^vahaus  .  .  arstibarj^  D.  8.
16043:•  p,  pärsa-  Adj.,  bezeichnet  ein  Volk 'persisch;  Perser':  naiy  ahi^  martiyj'  naiy "frf*  naiy  msdi^  Bh.  /.  13;  —  'sahyä  marti' yafyä  . .  arstii  D.  £.  4;  4;  —  imam  karam 'tarn  pädiy  (sd.)  yadiy  kär<^  °faf*  /ato* akatiy  D.5.  3;  Bh.^.  i,  5,  6;  —  karam °sam  Uta  mädam  Bh, j,  6,  3, 14;  6;  —  Aadä anä  °sS  iäräD.5.2;  —  adam  däray<^vt^us . ,  'f rf*  "saltya  puVa'  D,  6".  j ;  —  adam  'ja* amiy  D.  17. 3;  —  dädarsis  nänui'  °si^ manä  ba'dakt^  Bh._3,3;  6,  9,  3.6,  la,  4.x\ iS,\  5. 1.         a)  Sing.  (koUekt.)  für  Volk;
16806:tarn  arstim  barai/iYt.  10.21.  5) '(davon- 1  nanbyB  .  .  V.  77.  4;  —  ydka  ..  am?r7xtim tragen  sva.)  gewinnen;  empfangen':  yänä  avaiaräni  ..  Uta  az?m  apaiaräni  ..  sk- (sd.)  baraiti  astavB  va  .  .  m^nyahe  Yt.  o^m'a  tars/amca  haca  maata  dämaiyS  Yt 14.3^.  a)  mit  refl.  Dat:  paourva  ?ü  g.^i-;  10*; — ya  haca  daevayasnai^yü . . fumS  baraiti  "zuerst  gewinnt  er  sich  .  ."  apa.bara{^S2ih.)'^^  aya  ratit/H/"w3sinajk Yt  14.36.  b)  mit  Abi.:  iahmät  .  .  1  den  D.  ..weggenommen  hat,  damit  wird Aar»hr?m  barUi  "von  wem . .  soll  sie  Pflege  man  r."  N.  ^4;  —  mt^ram  . .  yS  nar^m  apa empfangen?"  V. y,  17;  16.  6)  'halten,!  qxanhai  baraiti  ". ,  aus  der  Not  (fortträgt pflegen,  behandehi  ab -';  die  Bestimmung '  sva.)  befreit"  YtJo.az;  aaf.*.  b)  mit erfolgt  a)  durch  praed.  Akk,:  \avam'G^vi.:  yS  daii^hSus  . .  apa  v^n%rajtum **uiaratam  abaram  "den  hab  ich  gut  ge- .  iaz-fl///  Yt  70.27;  —  «/«*  aeiqm  bärvä halten  (behandelt)"  Bh.  /.  8,  4-  13;  — ^aojd  .  .  barahi  Yt/0,a3.  c)  mitDat: in  pass.  Wendung:  *driyümca  drJvJmca'kahmäi  xiäimm  .  .  paiti.da'häni  ..  koA- ara%wyS.b?r3te  (sd.)  barimne  (ADf.) "' !  mä/  xi^dinm  .  .  apaiaräni  Yt  10.  109— P.26.  b)  durch  ein  Absolutiv  (sd.)  zuliii.  d)  mit  enkl.  Gen.-Dat  desPron.: ^bar-.  ys  vohu.b3r»tqm  baraite  milir?m  Yt  \apa  hl  vastra  baraym  V.5. 49;  —  ku%a 13. 18;  —  yS  nS  hub?r3tqtn  barst  Yt  1$. '  te  aam  *apavaräni''''>  navaca  yaskS . .  V. 40;  —  yö  nä  his  kubfnta  *barat  Yt  22,6.  a)  'Jemanden  bringen  um  — ', y-  >8;  —  ya'ha  duibirmts  *barailt'**  (in  mit  dopp,  Akk.'**:  jvö  . .  drvä  .  .  nar^m pass.  Sinn)  Yt/0. 48;  —  ya^a  Aub^ntS  asavarum  hanhus  }fan'i:ahaa  .  .  apa.- *baraite"^  (in  pass.  Sinn,  näml.  mthrö)'  baraiti  "..bringt  (er)  den  Gläubigen  um Yt/0,  112.  7)    mit   AS.    vääirt    'die  j  die  Nutzniessung  . ."  V.5.  38.         2)  'ab-
17611:•  j,  fradaxStanä-')  f.  'Schleuderstein':  isüm vä  arstim  vä  'nizm  vS  P.  27.
17886:mit^an  i)  'Jemanden  zu  Rate  ziehen': S.  Absol.  hqm.parstim  und  Inf.  hSmfar- iidif.        2)  'sich  beraten  mit  — ,  beraten
19033:duhiarstim   n'   vTspsm   aiwidruxiSe  mtirrS
19793:yaUa  *hvarfti  P.  28;  —  äat  .  .  manya 'nanka  humahm  .  .  hixva  mrüSii  hüxt^m .  .  tastaeibya  varfza  kvarstim  Aog.  25?.;
20047:'y<^  naiy  pärsi^  naiy  mad^  naiy  amaxam taumaya  kalciy  hytr  . .  Bh.  /.  1 3 ;  —  /  °y^ /rOätr  namtf  margavi^  Bh.^.  3;  5,  13, 1. 11,  16',  2.3,  4,  14,  5.  i'j  —  parsaAya •yakyä  *daraiy  (sd.)  arstis  paragmatä  . . parsc^  'y<^  *dUrayapiy  haca  pärs^  ka- maram  (sd.)  paitiyajatä  D.  if.  4;  —  hauv •jw*  hyi^  avakya  karahya  mt^iitJ^  ahJ' Bh._5. 11;  9;  —  via  tyaii'aiy  /ratama  'ya anusiya  ahi^ta  Bh.  /.  13;  —  avam  vaAyaz- datam  Uta  'ya  tyaisaiy  fratama  anustyä Sh^ta   i^arl>ay<£'  Bh.^.  7;  8,  11,  2.  i3;i|
20648:vacS  sara%usira  FrW.  /,  a;  Vt._j.  a,  V.  2.  5 PiiZ.;  —  yezi  humatsm  mainyät  kOxtim vääm  mrvUt  kvarstim  virizyät  ^aöhi Gs. /ö^;  — yüi  narS . .  humatais  mainit. Aaxfäis  (statt  AP.)  mrvai3l,NP.)  hvarsfüiS vimyantd  V.  70. 4 ; — manya . .  htzva  hUxtym mrSiti  Aog.  2(*fF.;  —  nsit  ma^ö ..  mraoiti duiuxhm  ya%a  mihrasat  mraoiti  hüxtim Yt  10. 106;  —  mazds  data  mraei  gayekyä (sd.)  syao^anais  vahyBY.  ^1.  19.  a)  mit Dat.  dcrPersoa:  sä:^}nl . .  kainibyB  mraomX ^-  53-  5  i  —  ^'*  '^'  "^'f  y^  ^^^i  S^'*^  '^■f'* (sd.)  mraot  Y.  46.  9;  —  aHbyS  mazdä  aka (sd.)    mraot  ysi  .  .  Y.  _J2.  12.  4)    mit
20866:sich  auf  die  i.  oder  2.  Person,  die  in  der Verbalform  des  übergeordneten  Satzes  ent- halten ist;  erste  Person:  y)  ('der  ich') *uruan3m  m}n  gairi  (sd.)  . .  dadl .  .yavat isäi  (sd.)  .  .  avat  xsai  ..  Y.2S.4;  —  yf . .  yaxai  (sd)  apa  . .  yastl^'^  . .  araohm ziaya  .  .  yJ  .  .  kaya  (sd.)  .  .  tot  *tsya  . . darsti>is{sd.)ca  ..  ^.33. 4— 6; —  anat/ va nSii  . .  yanaU  saranaimä  (sd.)  ySi  ('die wir  sva.  indem  wir")  v5  ySth>ma  (sd.)  Y. 3Ä9;  —  zweite  Person:  daidl  möt  y7 ('der  du')  gqm  tass  Y.  5/.  7;  —  nu  sraota yae('6xfi  ihr'Va  asnat  yalia  dürat  (sd.) isa%a    Y.  4j.  i;  4A'.  7  (yBi).  b)    das
20945:•  j.  yao-kars-  den.  Praes.  32  'Getreide säen,  bauen':  kat  asti  damaya  . .  uru>wan (sd.)  i . .  yal  ttyr^m  paiti  yaokarsti  {3SPA.) ". .  wenn  man  tüchtig  Getreide  baut"  V.
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
21257:•  j.  yat  paiti "  adv.-artige  Verb. ;  sie  leitet überall  einen  Satz  ein,  der  auf  eine  Frage antwortet;  i)  'wo,  ubi':  kva..z)mö  säist)in1 ■  •  yl  ^''  p^iti  fraistim  kärayeiti  .  . yavanqtttca  västranqm{sd.)ca  V.  J.  4;  i, 2.  5i  6,  8—13*,  32.  2) 'wenn,  wofern': kaf  asti  damaya  uruhwan  {sd)i  ..  ya^ w/rim  paiti  yaokarsti  (sd.)  V.  _j.  30;  — kö  .  .  tarn  . .  x^nUvayeitil  ..yat  bä  paiti .  ,  naire  aSaone  vtnzyät  asaya  daoäiti  V.
25104:•  j.*raSTwyö.varstay-'*  f.  'angemessenes Handeln, Tun':  mananhaica*humaiH  Mt- vasca  huxti  zastayasca  *kvarsti  °ti  natdys (sd.)  aAmi  . .  "bei  gutem  Denken  des Sinns,  gutem  Reden  der  Zunge,  gutem, angemessenem  Handeln  der  Hände  bin ich  . ."  P.  28.
29131:haslAäHalayä  -,    harn  dm  n  n  1)  -   Sü. :    saia- väiiHah.    —    ')  Ad«  ar.  *]admai;    %  403.   — «)  Vgl,  iSt  Y.  30.  10,  53.  3.  -  3)  S.  nmäna- No.  7. •    j,    haäa.m^^ra-    i)    Adj.    'mit    dem Mq^ra  zusammenseiend,  mit  ihm  eins'": zara^ultrim  °nm  Vr.  13.  i.         2)  m.  '(Mit- mq'^ra''',    d.  i.)     Ergänzungs/naSra,    Er- gänzung, Nachtrag  zur  Glaubenslehre'*': 'rtm  zainiparlUm,  °räi  zairti.parstili,  'rahe <zaini.parsiahe,  'ra  (VS.)  saini.parsta  Extr. \i-4.
30089:—  hariuhanne  *mai  *=3i;j3>  "die  beiden Backen  sammt  der  Zunge"  Y.  J/.4;  — /taomB.anhar^toAe  i^A.)  'evS^^  A.4.5;  — •zvffii  danhanha  "mit  Zungenfertigkeit"  Ny. 1. 1 6 ;  —  'sva  mrsSii  hüxttm  . ,  zastalibya vansa  hvarstint  Aog.söf.;  —  tai  ttS  .  . vldvanni  vao'a  'zvä  ^wahya  anhS  ". .  mit der  Zunge  deines  Mundes"  Y._J/.  3;  — mananhasca  *humaiti  'vaüa^  *hüxti  zasta- yasca  ''hvarsti'S.28; — kva  'w«  V.3,sPüZ., VdsjP.^j;  — ■  na^a.cit  mihs.aojSn!^ (sd.)   alSqm   a^aipai'iya  •sjiS''''   Yt  Z^.  95;
30650:•  j.  hv-aiwyästa-  Adj.  (fem.  '/ü-)  'gut' geworfen,  geschossen':  arstis  Ha  Yt. ;_;.  7z.
30695:zu  duzvaHta-:  daityanqm  rahwyanqm 'lanqm  lyadhnanqm  var)zäi  pairi  . .  duz- variianqm  syaöknanqm  varjzäi  Vr.  7J. I,  a)  sonst  nur  neben  hüxta-  und humata- :  humataht paiti  manaahe  küxtahe paiii  vacatahs  °tahe  paiti  iyao%nahe  Yt 16.  6;  —  ästuyi  humatim  manO . .  küxUm vacö  .  .  •Um  syad^amm  Y.  J2.  8;  — fra- stuyl  kumaisibyascä  hüxtsibyascä  'tdibyascä mahwsibyascä  vax>hwSibyascä  varltvSi- byascä  Y.  //.  17;  —  nanm  alavamm dahrUfUm  kumatimca  manB  hüxümca  vac5 •Umca  syaohtum  Vr.  2.  5;  —  aa^. .  manya mananha  humahm  . .  hitsva  mrätoi  hUxttm .  .  sasiaiibya  var>za  't»m  syadhium  Aog. 25  ff.;  ^  *ar»m.maiti  *Aumata  mamne  (Sp. 1121  f)  *ar>m.uxti  *  hüxta  (vavaca)  anm.- varsti  °ia'^  (vavarfzd)F.2^; — yezi  kuma- tim  mainySt  kUxt^m  väcim  mrväl  'bm'^ v»nsyäl  syadhn»m  Gk-iöy;  —  narS  asa- vanö  humataü  mainimna  hüxtäU  ntrvats 'täis(3.\sOb}.)v>rpzyant3Y.jo.4;—AumiUa- nqm  hüxtanqm  •tanqm  iyadaca  anya- dacä  v»r>zyamnanqmcä  vävtmananqmca mahl  aibT.jaritärS  Y._J5,  aj  FrW.^,  i;  — "•"rfil^r* (sd,) ,  .paiti  nivaitis . .  humaialsuia haxtalsuca  •taisu^a^'*  ti.S4;  —  vTtpäi/ 'hwa   humatäii  .  .  huxtäis  .  .  'täis  pairi-
30707:mi^rasc'it  .  .    kumatim;    nSit  .  .  /"raoHirf^Q^^  *^^},i^^„^j,^  ..     al^  ^^^  ^^^     ' duiüxtfmya^a  mihrascij  . .  Auxt^m,  nStt  geschossener(Pfeik)"Y.57. i8.       hfasüm . .  Vfrfzyati  duwarstim  yaha  mi^rascil . .  |  ^k  Absol.  sbes.
30723:j,  hv-ast«in  Absol,"'  'mit  gutem  Werfen', in  Verbindung  mit  dem  V.  'ah—,  apasi (sd.)  vasaite  arstil  yqm  *anhyeili  avi.- mihri/  .  .  yafSt  hv  *aahyeiti  .  .  ".  .  die Lanze,  die  der  jl/iärafeind  wirft;  wenn  er auch  gut  werfend  wirft",  .  ."    YtJO.  aoC
```


## [2026-09-05T20:31:52.447Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (352,353,354,355,356):\n    print(\"==== leaf\",n,\"====\")\n    print(leaves[n-1][:3500])\nEOF"
}
```


### [2026-09-05T20:31:54.043Z] TOOL RESULT

```
==== leaf 352 ====
1.  ero-,  re-,  er(e)-  , rudern;  Ruder';  ero-ter-  , Ruderer'.
Ai.  ari-tra-  m.  , treibend;  Ruder',  n.  (auch  a?'i7ra-)  , Steuerruder',  aritdr ,Ruderer';
gr.    igs-TTjg    ^Ruderer',    Ersatz    für    *iQSTrjQ   (=  ai.    aritdr-)    wozu   fem 'EgevQicc  ON  erhalten,  egiaaci),  att.  iosTToj  , rudere'  (*€gsT-i(x),  Denominativ)  ,J.- iosTfiög,  PL   igsTf-id    (statt   *6Qfji.iog  =  lat.    remus,    nach    igsTrjg,    Schwyzer  '^ Gr.  Gr.  I  493 2)  , Ruder',   hom.  elgsalrj   (sl-  metr.  Dehnung)  ,das  Rudern'  >''"<' UTTTj^srjyg  , Ruderknecht,  Matrose';   übertragen:  , schwer  arbeitender  Diener' Tievrrjgrjg  ,Fünfdecker';    slyiöa-ogogf   Tgiay-öw-ogogy    ion.   Tgirj-aörT-egog   usw. (die  -o^og-Formen  durch  gr.  Assimihation  von  o  aus  £?);  äh-rjgrjg  ,das  Meer durchrudernd',  dixcp-T^grjg  ,doppelruderig',  Tgirjgrjg  ,Dreidecker';
lat.  remus  , Ruder',  triresmom,  septeresmom  Columna  rostrata  (Gruudf. eher  *re-smo-  als  *ret-smo-) '^
air.  o'ä-  , rudern',  imb-rä-  »rudern,  zu  Schiffe  fahren'  (z.  B.  Impf,  -raad, Perf.  imm-rerae  ,profectus  est',  Verbn.  imram  ,das  Rudern'),  räme  , Ruder';
anord.  röa,  ags.  röivan,  mhd.  rilejen  , rudern';  ahd.  ruodar^  ags.  rödor  n. ,Ruder',  anord.  röpr  (w-St.  *röpru-)  ,das  Rudern';
lit.  iriiXy  irti  , rudern',  irklas  , Ruder',  ablaut.  apr.  arttoes  f.  PL  ,Schiffsreise'.
WP.  I  143  f.,  Trautmann  105.
2.  era-,  re-  , ruhen*;  re-uä,  rö-uä  ,Ruhe'.
Av.  airime  adv.  , still,  ruhig'  {^et^-mo-),  armae-iad,  -Uä  , ruhig  sitzend,  !| still  stehend'  (*e?--mo-  oder  *e7'a-mo-;  bloß  graphisches  -i-  sieht  in  airime  % Meillet  Dial.  indoeur.  Q^) ;  ^^  '
gr.  ^gtori  (7tol€[.iOLo)  »(Kampfes) ruhe',  egwiw  , lasse  ab'  =  anord.  ?'ö,  ags. röw,  ahd.  ruoica^  nhd.  Ruhe  (*röwö),  ablautend  mit  ahd.  räwa  ds. ;  dgd-fisvai' j)avxd^€Lv  Hes.  (?) ;
cymr.  araf  , ruhig,  mild,  langsam'  {*er9-mo-) ;
nach  Rozwadowski  R.  Sl.  6,  58  f.  angeblich  hierher  der  Name  der  Wolga Pä  als  , ruhiges,  stehendes  Wasser'  aus  *Rava  (mordvin.  Ravo)  zu  lit. rova  (=  germ.  *röuö  ,Ruhe'),  lett.  räwa  , stehendes  Wasser',  lit.  FlN Rova  =  slav.  Ravu]  besser  oben  S.  336.
Anreihung  von  gr.  egcjg  , Liebe',  sga^ac  , liebe'  (vgl.  ai.  rdmate  ,ruht, steht  still,   läßt  sich   genügen,  findet  Gefallen,  pflegt  der  Liebe')  ist  eine
339
höchstens  ganz  schwache  Möglichkeit  (s.  Boisacq  m.  Lit.,  Persson  Beitr. 667).
Eine  s-Erw.  *r-e-s-,  r-o-s-  in  got.  rasta  ,Meile'  (,Rast'),  anord.  r^s^  f. ^Wegstrecke',  ahd.  rasta  L  ,Ruhe,  Rast,  Wegstrecke,  Zeitraum',  as.  rasta und  resta  (*rastja)  ,Ruhe,  Lager',  ags.  rcest  und  rest  ,Ruhe,  Ruhelager, Grab';  ablautend  m
==== leaf 353 ====
nd.  o-uste,  roste  ,Ruhe,  Wegstrecke',  spätmhd.  o-ust ,Ruhe';  got.  razn  n.  ,Haus',  anord.  rann  ds.^  ags.  cern,  ren  n.  ,Haus'  (mit merkwürdiger  Bed.  o^cßsn  n.  ,Planke,  Zimmerdecke'),  afries.  ern  in  ßä-ern ,Vieh-haus';  unsicher  ags.  reord  {^rezdo)  f.,  gereord  n.  , Mahlzeit,  Fest, Futter',  anord.  greddir  , Fütterer,  Sättiger'  {^garazdlz),  grenna  , füttern' {*ga-raznian).
Vgl.  rem-,  das  wie  res-  mit  (e)rd-  zusammengestellt  wird.
WP.  I  144  f.
er(9)d-  {,r{d)d-\  er{9)dh-  ,hoch;  wachsen'.
Av.  drddva-  ,hoch';
lat.  arduus  ,hüch,  steil' ;
gall.  Arduenna  silva,  air.  ard  (*fduo-)  ,hoch,  groß';  cjmr.  hardd  , schön';
aisl.  grdugr  , steil'  setzt  (wie  allenfalls  auch  drddva-)  eine  Parallelform auf  dh-  fort,  indem  verschiedene  Erweiterungen  von  er-  ,(in  Bewegung setzen)   hochbringen'  durch   dh   (vgl.  ÖQodvvcj  ,treibe  an'  usw.)  vorliegen.
Sicher  mit  dh  lat.  ai-hor  ^^-^n^'»  wozu  kurd.  är-  aus  *ard-  ,Baum'  in ärzang  ,die  durch  Wind  und  Wetter  verursachte  dunkle  Färbung  auf  den Bäumen*,  eig.  ,Baumrost' ;
alb.  rit  , wachse',  aus  fd-  oder  fdh-'^
slav.  *orstg,  abg.  rastg,  russ.  rastü,  cech.  rostu  usw.  , wachse*  (*ord-, ordh-to) ;
toch.  A  orto  , empor'.
WP.  I  148  f.,  II  289  f.,  WH.  I  64  f.
ergh'  , schütteln,  erregen,  beben'  od.  dgl.,  wohl  Erweiterung  von  er-  ,in Bewegung  setzen'.
Ai.  2'^Ä^y«^i  »bebt,  tost,  stürmt';
gr.  ÖQXEO)   ,7tall(x),  %Lve(x)\   meist  ÖQxaonai   ,tanze,   hüpfe,  springe,   bebe'.
Wegen  der  in  3.  er-  ebenfalls  vorliegenden  Bed.  ,1'^fg'  u.  dgl.  können  dazu in  Beziehung  stehen:
av.  drdyant-  ,arg,  abscheulich*;
ahd.  ar{a)g  ,feig,  träge,  böse,  arg',  ags.  earg  ds.,  aisl.  argr  und  mit Metathese  ragr  ,unmännlich,  wollüstig,  schlecht' ;
lit.  ariüs  ,lüstern,  sinnlich*.
WP.  I  147  f.
22*
340  9
erk"'  , strahlen;  hell  klingen,  lobpreisen'.
Ai.  drcati  , strahlt;  lobsingt,  begrüßt,  ehrt',  arkd-  m.  ,Strahl,  BlitzstraL)      1 Sonne,    Feuer;   Lied,   Sänger'   (=  arm.  erg),    rc-,    Nom.  Sg.  fÄ  f.  ,GlaiuI Gedicht;  Vers',  j-kvan-  ,lobpreisend,  jubelnd';  *
arm.  erg  ,Lied' ;  . .
air.  erc  , Himmel*,  mir.  suairc  , angenehm,  schön,  strahlend'  (*su-erhiU)* toch.  A  yärk,  B  yarke  »Verehrung'  (Pedersen  REtlE.  3,  18);  V'
hitt.  ar-ku-ua-nu-un  ,ich  betete'  (arkuannn) ;  anders  Hendrikseu  45 und  74.
WP.  I  147,  
==== leaf 354 ====
Marstrander  ZceltPh.  7,  360;  vgl.  oben  S.  65.
ers-  :  orsos  , Hinterer,  Schwanz*.
Arm.  or  ,  Hinterer'  (meist  PI.  or-k,  i-St.);
gr.  bggog  m.  , Hinterer'  (dazu  oigd  f.  , Schweif  aus  *ors{a)  =  ^|;*
ahd.  a?'s,  ags.  ears  m.,  aisl.  ars,  rass  ,  Arsch'  =  '  ^
hitt.  a-ar-ra-d§  (arras),  Dat.  ar-ri-i§-äi  (arrisi)]  das  -si  enklit.  Pronomen* e-stufig    air.  err    (*ersa)    f.  , Schwanz,    Ende*    (auch    des    Streitwagens)
davon  eirr  , Wagenkämpfer'  (*ers-et-s),  Gen.  erred]
wird   vielfach   als    »Erhebung,  vorstehender  Körperteil'  zu   3.  er-  (oben
S.  326)  gestellt.  'flf
WP.  I  138,   Couvreur  H  98,  Pedersen  KG.  II  101.  '  '""^^^  -
es-  jSein*,  Kopula  und  Verbum  Substantivum ;  bildet  ursprünglich  nur  ein duratives  Präsens  wird  daher  einzelsprachlich  vielfach  durch  die Wurzel  bheud- :  bhü-  suppliert.
1.  Ai.  dsmi,  dsi,  dsti,  smds,  sthd,  sdnti,  av.  ahmi,  3.  Sg.  asti,  3.  PI.  h9nti, apers.  amiy]
arm.  em,  es,  e;
gr.  hom.  att.  bliil  (=  emi,  äol.  I'^ujut,  dor.  ^^t),  el  (=  ei  aus  *esi,  nur att.,  hom.  dg,  idai),  iati,  Biy,sv  (wie  et^i;  att.  ia^iev  wie  ^are]  dor.  ii^eg), iaze,  aioi  (dor.  ivTi),  Dual  iatöv]
venet.  est,
alb.  jam  (*esmi) ;
lat.  sum  (durch  Einfluß  der  1.  PI.),  es(s),  est  (Inchoat.  escit,  wie  gr. Iffx«),  sumus,  estis,  sunt  (Inchoat.  escu7it)]  osk.  süm,  est  (ist)]  umbr.  est]
air.  (nur  als  Kopula)  am  (*esmi),  a-t,  is,  ammi  (*esmesi),  adi-h,  it  {*sentl, acymr.  hint) ;
got.  im,  IS,  ist,  3.  PI.  sind  {*senti)]  aisl.  ew,  est  (ert),  es  (er)]  ags.  eom (nach  beom),  northumbr.  am  (*os-7n),  eart  (Endung  des  Präteritopräs.);  is] 3.  PI.  northumbr.  aron  (*os-nt),  usw. ;
341
alit.  esml,  (heute  esü,  dial.  esmü)  esl,  esti,  Dual  alt  und  dial.  esvä,  estaü und  estä-,  lett.  esmu  (dial.  esit),  esi  usw.;  apr.  asmai,  assai  (essei),  est  (ast);
aksl.  jesm7>,  jesi,  jesh  {*esti),  jesrm,  jeste,  sqH  {==  lat.  sunt) ;  Dual  jesvl jesta,  jeste,  usw.;
toch.  Präs.  B  3.  Sg.  ste,  star-  (mit  Enklitikon),  3.  PI.  skente,  stare, skentar-  Imperf.  A  1.  Sg.  sem,  2.  Sg.  set  usw.,  B  sai{-),  mit  Optativformans idg.  -Ol-  (nach  Pedersen  Tochar.  161  soll  auch  B  nes-,  A  nas-  ,sein'  die AVurzel  es-  enthalten,  das  Präverb  n-  sei  mit  der  Postposition  B  ne  iden- tisch??);
hitt.  e-es-mi  (esmi),  3.  Sg.  e-es-zi  (eszi),  3.  PI.  a-§a-an-zi  (asanzi ;  das  as durch  Vokalharmonie  aus  *es-?).
2.  Wichtige  Übereinstimmungen:
Imperf.  ai.  äsam^  äs,  äs,  bzw.  Perf.  äsa,  äsitha,  dsa,  PI.  äsma,  ästa, äsan,  Dual,  �
==== leaf 355 ====
�stam,  ästäm  :  gr.  hom.  1.  Sg.  ^cc,  2.  Sg.  hom.  att.  ^a&a,  3.  Sg. dor.  usw.  ^g,  PL  hom.  ^[xav,  ^vs,  ^aav,  3.  Dual  hom.  }jaT7]v',  mit  ^(Tt^a  vgl. hitt.  e-e§-ta  (esta)  ,war,  warst^;  themat.  1.  Sg.  3.  PI.  äol.  eov  (*e-s-om,  bzw. *e-s-on^) :  augmentlos  3.  PI.  ai.  san,  av.  hdn  (*sent  oder  *5on^).
Neubildungen  scheinen  lat.  erat  {*es-ä-t)  =  cjmr.  oedd  ,war^
Gr.  Imperf.  eoy,ov,  eois  :  alat.  escit  (die  Futurbedeutung  erinnert  an arm.  i-cem  ,daß  ich  sei^  aus  prothet.  *i  + s-\- {s)ke-,  Meillet  Esquisse  121);
Konjunkt.  ved.  2.  Sg.  dsas{i),  3.  Sg.  dsat(i):  lat.  Fut.  em,  m^;
Optat.  ved.  s{i)yäm]  gr.  fli^j/  (das  e  von  *iafiL):  lat.  Konj.  siem,  sies,  sze/, umbr.  sir,  sei  ,sis^,  si,  sei  ,sit^,  sins  _,sint':  ahd.  3.  Sg.  sl;
Imper.  2.  Sg.  gath.-av.  zdi  :  gr.  att.  üad-i  (*es-dhi) ;  3.  Sg.  gr.  hom.  att. saTO) :  lat.  estö{d)  :  osk.  eshtf? ;
3.  Partizipium  senU,  sont-,  snt-  ,seiend',  z.  T.  mit  Entwicklung  zu  ,wahr, tatsächlich*,  und  weiter  teils  zu  ,gut',  teils  zu  ,der  wirkliche  Täter,  der Schuldige'  :
Ai.  sdnt-  sdt-  m.,  n.  (f.  sat-i)  , seiend,  gut,  wahr*,  av.  hant-,  hat-  ds.;
gr.  iövx-,  oW-,  dor.  ivr-  ,seiend*  (Schwyzer  Gr.  Gr.  I  473,  525^,  567, 678),  Nom.  PI.  rd  ^vxa  , Gegenwart,  Wahrheit,  Besitz*,  abgeleitet  ovala, dor.  iaala,  (bala  f.  , Eigentum,  Natur,  Wirklichkeit',  usw.;
lat.  in  praesens,  -sentis  , gegenwärtig*,  osk.  praesentid  ,praesente*,  ab-sens , abwesend' ;  söns.  Gen.  sontis  ,schuldig,  schädlich'  (vgl.  sonticus  morbus »Epilepsie'?);
urgerm.  *sanpa-  ,wahr*  in  anord.  sannr^  sadr,  ahd.  sandj  as.  söd  ,wahr, und  , wessen  Schuld  ohne  Zweifel  steht',  ags.  söd  ,wahr' ;  daneben  tief- stufig germ.  *sun{d)jd-z,  got.  *sunjis  ,wahr'  {sunja  , Wahrheit');  die  eigent- liche Bed.  noch  in  bisunjane  , ringsum*,  ursprüngl.  Gen.  PL  ,der  ringsum seienden' =  ai.  satyd-  ,wahr,  recht*  {*sntio-),  n.  , Wahrheit*,  av.  haid^ya- ,wahr,  echt*,  apers.  hasiya-  ds. ;
342  •
mit  erhaltenem  oder  assim.  d  ahd.  suntea,  as.  sundea,  afries.  sende,  aisl  #' synd,  synd  <  mnd.  sünde,  ags.  synn  f.  ,Sünde,  Verbrechen'  (urgerm.  *sundi  "v* *sun(d)jäz),   weiter  zu  as.   ahd.   sunnea   ,Hinderung,   Not',   aisl.   syn   , Ab- leugnung' ;
apr.  Nom.  Sg.
==== leaf 356 ====
  sins,   Dat.  Sg.  sentismu,  alit.  Akk.  Sg.  m.  santj,  lit.  s««    ' saficio  (jünger  esqs,  esqs  m.,  esanti  f.),  lett.  eswo^s  , seiend' ;  Gerundium  Ht
aksl.  sy  ( :  ai.  sdn),  Gen.  Sg.  m.  sgUa ;
hitt.  as-sa-an-za  (assanz)  , seiend';  ~  ^;
fo-Partiz.  *s-e-t6',  s-o-tö-  in  gr.  hd'  dXrjdfj.  äyad-a  Hes.,   hdt^w   ,prüfe',  f ■ ^Tfdg,  irv^ög  ,wahr,  wirklich'  und  Saiog  ,recht,  erlaubt,  fromm';
<i-Abstrakta:  ai.  ahhi-sti-  f.  ,Hilfe'  {abhi-sti-  m.  ,Helfer'),  av.  aiwiUi-  f, , Studium';  ai.  üpa-sti-  m.  ,Untergebener'  (ai.  sv-asti-  f.  , Wohlsein'  wohl ^ ar.  Neubildung);  vgl.  gr.  iartb  ,oiala^f  äneffTO),  drcEOtvg  Hes.  , Abwesenheit' ^ u.  dgl. ;  M
über  das  vielleicht  hierher  gehörige  gr.  icr-d-lög  ,tüchtig,  gut,  glücklich*,  '^ dor.  iaXög,  arkad.  iaXög  vgl.  Schwyzer  Gr.  Gr.  I  5335,  Specht  Dekl.  256.  |
WP.  I  160 f.,  Schwyzer  Gr.  Gr.  I  676ff.,  Trautmanu  71,  usw.  «
Zum  obigen  vielleicht: esu-s  (:  SU-)  ,gut,  tüchtig'.
Gr.  ivg,  '^vg  ,tüchtig,  gut',  Adverb  e-5   (Akk.  n.),  Präfix  ed-  gehört  zu
hitt.  a-a§-§u-u§  (assus)  ,gut';  zum  a-  s.  Pedersen  Hitt.  167  u.  Anm.; vielleicht  als  Schwundstufe  dazu  (Friedrich  IF.  41,  370  f.)  das  Präfix  sm-, s.  dort;
hierzu  vielleicht  lat.  erus  ,Herr',  fem.  era,  alat.  esa  , Herrin* ;
doch  ist  hitt.  i§-ha-a-a§  (ishas)  ,Herr'  fernzuhalten,  da  dies  zu  arm. isxan  ,Herr',  isxal  , herrschen*  gehört  (?),  das  selbst  nichtidg.  Herkunft  ist (Couvreur  5  9);
fern  bleiben  gall.  GN  Esus  (mit  e-),  wohl  wegen  der  Namen  mit  Äes-, Ais-  am  ehesten  zu  1.  ais-  oder  2.  ais-  (oben  S.  16),  weniger  wahrscheinlich zu  2.  eis-  (oben  S.  299);  ebenso  der  air.  PN  Eogan  (*ivogenos)  und  der cymr.  PN  Oicein  (älter  Yiceiii,  Eugein,  Ougen)  =  air.  PN  Ügaine  (*ouo- geTiios),  vgl.  dazu  Bergin  Eriu  12,  224 f.
WP.  I  161,  WH.  I  419,  863.  Ein  ;etymol.  Versuch  bei  Kretschmer, Objekt.  Konjugation  16  ff.
es-  (nur  medial)  , sitzen'.
Ai.  äste,  av.  äste  ,er  sitzt'
```


## [2026-09-05T20:32:07.488Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor pat in [\"аг$Е- sb. ‘spear’\",\"arslibara- sb.\",\"^u- insep. prefix\"]:\n    i=t.find(pat)\n    print(pat,\"-> leaf\",t.count('\\f',0,i)+1)\n# print leaf around\ndef show(n,k=2500):\n    print(\"==== leaf\",n,\"====\")\n    print(leaves[n-1][:k])\nEOF"
}
```


## [2026-09-05T20:32:07.850Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hašiya\\|hasiya\\|haSiya\\|amiy\\b\" KNT.txt | head -20"
}
```


### [2026-09-05T20:32:09.237Z] TOOL RESULT

```
аг$Е- sb. ‘spear’ -> leaf 195
arslibara- sb. -> leaf 195
^u- insep. prefix -> leaf 198
```


### [2026-09-05T20:32:09.275Z] TOOL RESULT

```
1107:OP hasiyam ‘true’, Skt. satyám.
1456:OP amiy ‘I am’, LAv. ahmi, Skt. dsmi, from pIE *esm:.
1530:*g¥em- ‘come’ in -jamiy ‘may it come’, *g*m- in pardgmata ‘gone forth’ (see $244).
1634:(2) pAr. palatalization of velars before palatal vowels, giving an alternation in OP k/c, g/j ($78.11): Maka Maciyà, kunautiy kartam car- lanaiy, kašciy cisci, drauga draujana adurujiya, pard-gmala ha"gmalà à-jamiyü.
2430:pIE *ueid-ne-/-no- in OP vainamiy Ч see’, 3d sg. vainatiy, mid. vainataiy; Skt. véndm? ‘I desire’, vénati, vénate. $211. Tug PnEsENT-TENSE SYSTEM OF TYPE
2561:I. The primary ending -mi is attached directly to non-thematic stems, as in pIE *es-mz, Skt. dsmz, Av. ahmi, ОР amiy. The ending of thematic stems was the lengthening of the thematic vowel o, as in Lat. ferd, Gk. феро; but to this -б there was added in Aryan the ending -mz, as in Skt. bhdra-mt, Av. barümi, ОР pari-barümiy. Other OP examples: parsimiy, Skt. prechámi; dárayamiy, Skt. dhard- ydmi; vatndmty, jadiyämiy.
2613:The old neuter in pAr. -а{ survives in the first element of the compounds Déraya‘-va‘u- ‘Darius’. Vi”da'-farna*- ‘Intaphernes’, Vdya'-spdra- (5162); and in the derivative haSiya- ‘true’, = Skt. satyá-, pIE *snt-go-, where (Skt.) sát is nt. pte. to root as- ‘be’.
2714:C. Alone, to denote means: DB 1.11f vafnà Auramazdéha aham хауада amiy ‘by the favor of Ahuramazda I am king".
2715:D. Alone, to express specification: DNb 40f yãumainiš amiy ша daslaibuyü ша pādaibiyā ‘trained am I both as to hands and as to feet’. So also with numerals: DB 2.56 Andmakahya mahyd XV raucabi$ 6akatà aha ‘of the month Anamaka, 15 by days were past’; Wa 1 IT karšā ‘2 (units) by weight’; cf. Lg. 19.227-9.
2769:may be used as predicate to any subject:! DB 2.18f кага Parsa шй Майа hya ира mam аһа haw kamnam dha ‘the Persian and Median army which was with me—this was a small thing’; во also DB 1.47 uvaipa saam (referring to Parsam utà Madam ша aniyà dahyàva), DNa 39 ctyakaram aha ava dahyava, DNb 6f avakaram amiy, ОХЬ 27f avā- karam-ca-maiy usiy wa framand, DNb 50 ciyükaram amiy ciyükaram-ca-maiy tonaré. A neu- ter subject may have a masculine substantive as predicate: DNb 11f tya rdstam ava тат kama ‘what is right, that is my desire’.
2899:DNb 26 z£nula amiy, cf. the adj. in the parallel clause uxsnaus атту, in line 27.
2934:(b) Prayers: biyé DB 4.56, 56, 58, 74f, 75, 78f; negative with md, biyà DB 4.59, 79°, äjamiyä DPd 19.
3045:positions are found, for stylistic reasons: 34 hama- ranakara атту uShamaranakara ‘as battle-fighter I am a good battle-fighter’, 41f asabára wdsabéra amiy ‘as horseman a good horseman am I’, 42f danwamya woanwaniya amiy ‘as bowman a good bowman am I’, 44 ārštika amiy uvārštika ‘as spearman Ї am a good spearman'.
3149:0816. Sryzistic Omissions occur in OP, es- pecially of the copula when there is a predicate adjective or phrase; cf. §275, §276. Examples: DB Lf Cišpäãiš pita (sc. cha) Hazàmanis; 1.9 VIII mand іаитӣуӣ (ве. dha") tyaty . . .; 1.10 adam (sc. amiy) navama; 1.13 ima (se. ha*tiy) dahydva tyaty ‚..} 1.15 tyaty drayahyá (ве. ha*tiy; or possibly daraya"tiy, сї. XPh 23f); 1.27 ima (sc. astiy) tya mand kartam (se. astty).
3151:Another type of stylistic omission is found when a clause is repeated, and one or more words of the prior clause are not repeated in the second, but are to be understood from the prior clause. Thus DNb 35-7 yaciy vaindmiy hamiciyam yaciy пату vainamiy (sc. hamiciyam) ‘whatever I see (to be) rebellious, whatever I see (to be) not (rebellious)’; and similarly in DNb 38-40.
3431:3 : Cispais : xšãyaðiyahyā : риса ; HaxdmaniSah 4 ув : парӣ : Вапу : Áriyáramna : xšāyaðiya 5 :iyam : dahyau§ : Parsa : tya : adam : dárayá 6 miy : hya : uvaspà : umartiyü : mana : baga 7 : vazraka : Auramazda ; frábara : vašnā : Au 8 ramazdàáha : adam : xXàyafiya : iyam : da 9 hyauS : amiy : 80у : Anyaramna
3471:12 dha : adam : хддёуайуа : amiy : Auramazdā :xšaçam : mana: frabara : 6
3489:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 39 : adurujiya : adam : Bardiya : amiy : һуа : Kürau$ : puça : Kabijiyahya : br
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
```


## [2026-09-05T20:32:17.432Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (194,195,198):\n    print(\"==== leaf\",n,\"====\")\n    print(leaves[n-1][:1800])\n    print(\"...\")\nEOF"
}
```


### [2026-09-05T20:32:19.366Z] TOOL RESULT

```
==== leaf 194 ====
t’).
-
LEXICON
ч.
Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zšaça- de- rives from aría-); imitation of Xšayāršā, acc. -üm, explains the long vowel of the ultima in the nom. and acc. ($78, §161.[b; decl, §172, $187). Artazšaçã nsm. А:Ра 9°, 17°; АЧ; D'Sb 3°; A’Sa 1; A’5b; A*8c 1°; А4 1, 2; А? На 1; A*Hb; Ае 7, 156; A*Pa 5 (as acc., 52476), 8, 12 (as gen., $313.IT), 13 (as gen.), 14f (as gen.), 15f (as gen.), 21, 231; AVsb-d. — Ardaxcasca ($49; or -Sda) AVsa. Arlax áagüm asm. АІРА 51°; А%8а 4; A?He 5; S£ 2-4. ArtaxSacahyé gsm. D'Sb 2°; Artaxíafrahyà (Tm. Lex. 54) A?Ha 2f, 3; Arlazíagühya ($53) A’Sa 2 bis; A?He 101, (аз nom., 5313.1) 11.
ariàvan- adj. ‘righteous, blessed’, denoting the blissful state of the true religionists after death: identical with Av. asavan- ‘characterized by Arta or Asha, righteous’, Skt. rldvan- ‘true to sacred Jaw’ (cf. Hz. Ар! 289-93); from *ria-, OP arta-, with lengthened final vowel, + ad]. suffix -van- ($30, $155.IV). атара nsm. (8124.5, $187) XPh 48, 55.
Artavardiya- sb. ‘Artavardiya’, one of Darius’s generals: Flam. ?r-du-mar-ti-ja, АКК. ar- ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. suffix ($80, §31, §144.1V, S160.Ia): ‘Doer of Jus- tice’ (not from vard- ‘to increase’, Skt. vardh-, be- cause of -z- in АКК. and in Aram. "rívrzy, аз Bv. BSLP 31.2.66-7 shows). Artavardiya пет. DB 3.30f, 33. Artavardiyam asm. DB 3.36, 43.
Ardaxcasca (or -Sda), probably miswritten for Arlax&acü, q.v.
ardata- sb. ‘silver’: Av. arazata-, Skt. rajatá-, cf. Gk. &pyvpos, Lt. argentum. (S30, §88, $145); Yezdi ait ‘silver’ has Ir
...
==== leaf 195 ====
пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (as gen.; §313.1[). Aršämahyā gsm. DB 1.3, 5; DBa 4, 6.
arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200.
avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt 2°; рле, 1; DE 3; XPa 2; XPb 3; XPe 2; XPd 2; XPf 2, 28; XPh 2, 37; XE 4; XV 3; А?Ра 2f^; A’H 3; A*Pa 2f. avamsam DB 2.20, 821; 3.31, 85; 5.8. auahya gsm. DB 1.29; 3.70; 4.48f. алапа absm. DSf 81. араш npm. DB 5.15, 31°; DSf 48, 50°, 51, 53, 54. avaiy apm. DB 2.77; 4.69. avaišām gpm. DB 4.51.
avém 
...
==== leaf 198 ====
�; 4.33; DPe 7; DNa 16; DSe 15; DSm 5°; XPh 14. ima apf. DB 1.21; D$g 3°.
ima nsn. DB 1.27, 72; 2.01; 3.10, 20, 58, 76; 4.1, 9, 40, 49, 59; 5.2; DPh 4; ОМ 32; DSf 22; DH 3. ima asn. DB 1.25 bis, 26, 68; 444; DNb If; DSf 10; DS} 2°, 5°; ХРе 10f; XPd 16; XSa 1; Х8е 3°; XV 20; А:Ра 19°; D'Sb3?, 4°. imá apn. DB 432. imaibiš ipn. DNb 48.
Imaniš- sb. ‘Imanish’, name assumed by the Elamite rebel Martiya (§163.V): Elam. um-man- nu-$, АКК. tm-nia-ni-e-Su. — Imani$ пә. (8185.11) DB 2.10; 4.16f; DBF 4.
уат demonst. adj. and pron. ‘this’ ($11, $260.I1I, $265): from * nsf. (perhaps also from *? suffixless пзш.) -+ pronominal -am (q.v.). Decl., $199. Seealso?dà,/ma-. тат pron. пет. DBb 1; DBe 1; DBd 1; DBe 1; РЫ 1; DBg 1; DBh 1; DBi 1; рву 1; DBk1; DN i-v, xv, xvi", xvii, xxix; А?Р 1-4, 8°, 9-21, 22 (written imy*, $51), 23-8, 29°, 30. туат adj. nsf. AmH 5,8 (as Isf., §56.V);
DPd 6; DZe 10; iya (§52.V) DB 4.90; т |
DB 4.91 (written тё, $52. VI).
isuvd- sb. ‘battle-ax’ (Junge, Klio 33.223; Kent, JNES 4.233): etymology unknown (stem- formation $143.IV). Not ‘bowcase’, for ?$uvd-, to Av. ifu- ‘arrow’, Skt. fsu- (ef. for variant views Wb. Grab 41-8). _ iswām asf. DNd 2.
LEXICON
as- vb., see atš-,
isti- sb. ‘sun-dried brick’ (5152.11, 5179.11): Av. tštya-, NPers. 110, Skt. istaka-, Medieval Skt. isttka- (König, Burgbau 51-2; Wb. AfOF 7.41; Hz. AMI 3.57-8; W. N. Brown, Lg. 8.13). 2328 nsf. DSf 29.
ета or lismar\uy asn., of uncertain mean- ing, possibly ‘(gold) inlay’ (Cameron, Persepolis Treasury Tablets 129-30), DSf 51; supplied by Hz. AMI 3.74-5, as a borrowing from Elam. 25- ma-lu (@%ma-lu ‘wood’ Hinz, Orientalia 1950, shortly to appear), or from the lost Akk. original of both; сЁ JAOS 53.21, 56.220. But read rather Idàr|uv with Hinz, see Lex. s.v.
Izalàü- sb. 'Izala', a district in Assy
...
```


## [2026-09-05T20:32:44.236Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN xist/hist ===\"; grep -n -i \"chi[sš]t\\|xist\\|hišt\\|Wurfspieß\\|Spieß\" HRN.txt | head -20; echo; echo \"=== HUB ===\"; grep -n -i \"Wurfspieß\\|Spieß\\|chist\" HUB.txt | head -20; echo \"=== PHD ===\"; grep -n -i \"xišt\\|hyšt\\|xist\" PHD.txt PHD_mackenzie.txt | head; echo \"=== BRT astra ===\"; grep -n \"aštrā\\|astra-\\|aštra\" BRT.txt | head -20"
}
```


### [2026-09-05T20:32:44.324Z] TOOL RESULT

```
=== HRN xist/hist ===
7983:brechen' auf iranischem Boden existirt haben müsse.
9457:)94. hest 'er ist, existirt', hestl *Sein, Existenz'.
9462:des Existirens erhielt. Von der dritten Person bildete
9810:für agrütu bezeugt, beweist dann die Existenz einer
10045:ahü' im PehlevT zu existiren.
10091:nicht beibehalten werden ; np. engösTden existirt nicht.
10504:Fehle vT vielleicht noch existirt, wenn es auch sonst
10555:existiren wohl nur in den Wörterbüchern.
11043:188. stfirtan statt v(l)startan existirt schon im PehlevT
19846:Ixista 488.

=== HUB ===
=== PHD ===
PHD.txt:24:ALMOST every published list of Pahlavi words contains a number of entries of doubtful nature, the uncertainty lying either in their form, their meaning, or even, occasionally, their very existence. The purpose of this dictionary is to provide the student with a representative vocabulary of Pahlavi in which such uncertain words have been reduced to a minimum and marked. It differs from its predecessors in that the Pahlavi words are given in a phonemic transcription representing, as far as it is deducible from the evidence, the pronunciation they would have had in the third century of our era, the period of the rise of the Sasanian empire. The reasons for this departure from the 'archaistic' tradi- tion of Pahlavi studies I have given elsewhere.! If one reason stands out it is that of practicality, as most corroborative evidence comes from this period.
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:193:---rēšn(ih) [-Iwsn!, -lwsnyh] Infinite Light. anāhīd р/у | N ndhid] immaculate; a goddess; astr. Venus. an-àáhóg P7 kwok!] undefiled. an-ālūd [?77/wt'] undefiled. a-nāmčištīg m mcftyk!] unspecified. an-ámurzid [?rmwlcyt! | M ?n’mwrz‘yd] merciless. an-āmurzišn [*7”mwicšn!] mercilessness. anār [71 | N ~] pomegranate. anārģēl [777/gy/ | N nārgēl) coconut. an-arzünig [?77/c”nyk!] undeserving, unworthy. an-ast [^n 4 Y T'] non-existent.
PHD.txt:194:~ih : non-existence. ānāst [?n’st'] spoilt, destroyed.
PHD.txt:219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
PHD.txt:512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
=== BRT astra ===
4290:•  j.  an-aiwLvastra-  Adj.  'unbekleidet':! <Äa  nara  . .  mayna  . .  'ra  (ND.)  V.  Ä  10.
8330:•  j.  ratu/ris  canmanqmca  pasu.vastra- nqmca  "upajaeäaätnÜä '* "  fraoiritarst n'almät  N-i«?'*.
9604:•  j.  kastra-  n.  'Spaten':  °r^m  paiü/.hjtyzim
11941:•  j.,  g.  tanü-  f.,  m.'*,  g.  tanuS-'*  n.  Xeib' 1)  der  Menschen  (und  menschenähnlich gedachten  Götter);  auch  sva.  'Person', wobei  die  obliquen  Ka^us  auch  im  Sinn von  ihn'  usw.,  sowie  -  mit  oder  ohne  Ava-, hava-  —  in  reflexiver  Bedeutung^*  im  Sinn von  'sich,  mich'  usw.  gebraucht  werden: ya  anrS  mainyui  frak?rfntat  avi  imqm 'nüm  yam  masyänqm  V.  20.3;  5;  s.  noch lu  aj  —  ks , .  a%r3  tafitus  äärayat  'naot haca  maiyehe  V.  20. 1 ;  —  yasca  .  .  dax- manam  avavantim  mazS  vXkänayat  yaha hl  'nui  anhal  V.  7. 5 1 ;  —  {yai)  *may'iain 'nUm**  aiwyästam  (sd.)  "irlris  .  .  N.  p5; *95^>  —  '*'"'  panna  (sd)  °nBm  aiwi.- si/ais  YX.  14. ^5 i  —  yaf  kl  'nus  hiskvi Aiynvi  (sd.)  pqsnu  bavai  V.5.31;  —  &«.- ayarpm..  'nüm  frasnayayania  Yt/0.  laz; 133;  —  US  'nüm  snayaita  us  *vasirä  V. J.  54;  —  "^ris  frasnaiti  •nunqm  . .  vastra- nam  V. /2.  a;  —  hakmt  aps  hvqm  'nüm pairi yaozdai^ita  V.  (),3i;  31",  ä  36,  37, 39,  Vd./5,  ig*,  20; —  Ja/  vlspam  kvam 'nüm  ayaozdata  k>r>naoiti  V,  ■¥.40;  — yal fU  zasta  nöie  frasnäta  aai  vJspam  hvqm 'nüm  ayaozdata  ik?n>»aoiti  Y.S.40; — yffi Aqm.nasüm  paitiäristfm  °nüm  yaozdai%yqn V.g.i;  —  iia  iristahe  'nüm  avaMsta  .. isaaa  (sd.)  ml  yaoldaitim  V,  Ä  100;   —
14505:zananqm  upäzSit  V.4.11;  11,  2.30;  — ■yff  zpmS  lis'rö  karsA /rakarayeiti  H.  lOi; 7o;(?),  loo'i?).  [Vgl.  noch  SnYNo.  i, zu  %ri^.Aastra-  \md  "hh'^x^is/s.]
14708:•  j.  ^SriS-hastra-'*  n.  'Versammlung  von dreien':  yä  bii.hastrim  sravayeiä  . .  *rsm
15871:*pasu.vastra-
15876:•  j.  'pasu.vastra-  n.  TCleid  aus  Tier-, /spez.i  Schaffell':  carimanam  'ranamca N.  >8;  8v,  —  'rahe  F.^b.
15878:•  j.  'pasu.vastra-  n.  "Viehstall';  az3m  . .
23152:•  j.  'vastra-  n.  'Kleid,  Gewand,  Kleidungs- stück': bawraitti  'rä  vatahüta  arydvT  Yt 5.  129;  —  spaSa  'rä  var^hatti  spaita Yljo.  136;  —  ?rf%ahm  zaranim  . . 'rSsca ktSh  bämanivä  Yt  i"],  14;  zit.  F.  5  (wo vüHrät  vaca  k°)\  —  'nm  . .  ubdanum V3  Izaimm  vä  V.  <?.  23;  —  sr%nm  'nm st»hrpa^aah»m  Vd.  20;20;  —  yänhuya- nam  ..  °ranam  Vd.2;  *I2;  —  hanhus :far^aheca  -rahe-a  V.  5, 38;  —  aSä :^ar»hi  ofaratu  a^ä  'rä  varahatu  V. 3.  19;  —  avalm  3?ar3h>mca  'rpmcij  Y. 5S-3i  z;  — yii0  x^arpia  jrOiS  'raV.^.S^i S7i  58,  Vyt45;  —  i^an^aliiyB  ..'ralibyS .  ,  astayanta  V,  J.  j8;  —  gave  x^arsham gave  'rtm'^  Y.  10.20;  —  mä  gSui  mS °rahe  hatS  aoäitlm  (sd.)   vag^sii  V.  4.46;
23156:•  j.  »vastra-  n.  'Fresse,  Maul,  Rachen': azSis  vilapahe  'r?m  N.  48.
24312:•  j.  virö.vastra-  n.  'Männerkleid':  avaval aipi  ya%a  Byum  'nm  ", .  (als  ein  Männer- kleid sva.)  als  das  Gewand  eines  Mannes" V.  8. 35.
29673:enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
```


## [2026-09-05T20:32:52.110Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT Peitsche ===\"; grep -n \"Peitsche\" BRT.txt | head -10; echo; echo \"=== BQT v2 خشت ===\"; grep -n \"خشت\" BQT_v2_pages.txt | head -20; echo; echo \"=== count pages tags ===\"; grep -c \"pdf page\" BQT_v2_pages.txt"
}
```


### [2026-09-05T20:32:52.196Z] TOOL RESULT

```
=== BRT Peitsche ===
4888:•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
5959:G.  anslässt"',  wird  er  ur,"  N.joj.  j  der  Peitsche"  P.p.         b)  kat  aaahe  paiti
6488:•  j.  aätra-Dhäd-  Adj.  'mit  der  Peitsche lenkend':  mi^rnn  .  .  °»Aäojm  amavanUm .  .  ra>aestq//i  Ytio.  112.
6492:•  j.  alträ-    f.    'Geisel,    Peitsche,    Knute':  narü  xsa^ra  xsaymU  "va  ni'jäiu.pifu  VL yat  b>r3z»m   barat   'ra  väam  "wenn  laut  1/7.  7;  5.130.
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
6504:'Stocic,  £ub'  und  ahd.  i-^öAi  'Peitsche'  usw.  j-  '^''''  (Nerbalf.):  s.  qs-.
9608:von  der  Peitsche:  yat  btrizam  barä£ aitra  väcim  aspanqmca  srifa  xsu/sqn aitra  kahvqn  Yt.  iO.  113.
10188:•  j.  gav-äza-  m.  'Gerät  zum  Antreiben des  Viehs',  Du.  'die  beiden  Geräte  z.  A, d.  V.',  d.  i,  'Stachel  und  Peitsche':  yalsqm
10191:•  j.  gav-äzista-'*  Adj.  'der  das  Vieh  am besten  antreibt,  womit  man  das  Vieh  am besten  antreiben  kann':  'zistaQiD.)  ffava:;J (sd.)  "Stachel  und  Peitsche,  womit  man das  Vieh  am  besten  antreibt"  V.  ;4. 10.    1
10955:•  j.  x^vaewayataäträ-  Adj.  (mask.  *ra-) 'der  die  Peitsche  kreisen  lässt,  schwingt': xsähra  . .  'ra  (APn.)  "Reiche,  wo  man die  Peitsche  schwingt"  Yt.5. 130.

=== BQT v2 خشت ===
3597:‫هردو زاج سوخته وبوزن زاج خشت بخته‌وبوزن‬
3741:                    ‫که در آن خشت و‬                 ‫آورند ‪ -‬ومتسوب بناجا را چاچی گوبند عموما‬
4537:‫حیلاگه = بكر اول بروزن خشتك ‪.‬‬
5072:‫چرخشت ‪ ۲‬باشیننقطه دار ‪ ۰‬بر‬                                                    ‫اول باشد که فلك قمراست‬
5076:      ‫‪:‬رخشت و — ‪naidgoS,gninneH‬‏‬
5100:                      ‫شکل غلط کلمة چرخشت‬       ‫‪۹‬‬
5102:                      ‫باکلمة پپلوی‬   ‫و شاید چرخشت‬     ‫‪thswxrc‬‏‬       ‫مفدی‬          ‫‪=°‬‬              ‫(ه‪.‬م‪. ).‬‬
5103:                      ‫(‪ )1501172:‬خواند بمعذی‌چرخشت‬                 ‫که بقول تب رکه‌میتوان آلر| ‪5‬‬
5174:    ‫بجرخشت‪ .‬‏‬             ‫دست‬
8386:                ‫مروز گارحزبران کندت خشت پزی‪.‬‬                           ‫برو زکار زمستان کندت گی‬
10297:‫مطلق پل را گوبند خواه باسنگف وخشت وکچ‬                        ‫تون‬     ‫حجد او ند ‪ ۱‬ب‌ بقتح واو وسکون‬
10815:                          ‫(‪ )3‬چش ‪:‬خرخشته ‪.‬‬                                   ‫‏)‪ (e‬خم‪ : ۱‬دقداق ‪.‬‬
10897:    ‫(‪۰‬م‪. ).‬‬      ‫«چرخشت»‬          ‫^ _ مسحضف‬      ‫رك ‪ :‬خرخشه‪.‬‬         ‫‪۵‬‬     ‫‪ - ۷‬باین معنی اسم صوت ‪.‬‬
11608:‫اول مخفف خیرو است و آکنلی باشدکهآ نرا‬               ‫زای قطه دار همآمده _وخشتکاری اطراف باعحه‬
11894:           ‫‪ ۳‬ینداری که ازبهر آغاز چرخشت اءت و فعردن انگور‪« ».‬التفهیم ‪ .‬بیرونی ‪۸٩٩. -۷5۷‬‏‬
12243:         ‫‪9‬‬   ‫رك‪ :‬خشتامن» خش‬                     ‫‪.‬‬    ‫‪..‬خشتامن‬    ‫‪ ۳‬مقاءل«خر»(د‪.‬م ‪).‬ره خشامن‬
12288:                                                    ‫خشت تابه ه بافوقالی بالف کشد‪.‬‬
12289:‫خشت رر د خشت ر رین کنابه‬                            ‫فوتح بای ابجد ‪ .‬کوره و داش خشت یزی را‬
12291:‫جفتلث = مصغر خشت است ‪ -‬وبارچة‬                        ‫خشتامی ‪ -‬بفتح اول بروزن تردامن »‬
12296:‫کابه از آقاب‬              ‫خشتك رر‬                    ‫حشتچه » بکر اول وفتح جیم‌فارسی‪.‬‬

=== count pages tags ===
0
```


## [2026-09-05T20:32:56.755Z] TOOL CALL #18: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:751 2>&1 | head -60"
}
```


### [2026-09-05T20:32:58.513Z] TOOL RESULT

```
no scan of BQT covers printed page 751 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:33:00.834Z] TOOL CALL #19: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:33:02.887Z] TOOL RESULT

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


## [2026-09-05T20:33:10.677Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"nleaves\",len(leaves))\nfor n in (208,209,210,211,212,213):\n    print(\"==== leaf\",n,\" printed ~\",n+540,\"====\")\n    print(leaves[n][:2000])\nEOF"
}
```


### [2026-09-05T20:33:12.511Z] TOOL RESULT

```
nleaves 684
==== leaf 208  printed ~ 748 ====
 ‫‪Yg‬‬     ‫~‪m‬‬                                                                                      ‫‪‎‬هرو‬


‫بمعنی‬   ‫‪ -‬بر وزن رسیدن »‬         ‫خسدن‬                      ‫خسوره ه بم اول وفتح رای قرشت؛‬
‫استت که در زیر «ندان ترم کردن‬           ‫خایدن‬              ‫یمضی خور استت که پدر شوحو و پدر زن‬
                                                                                                    ‫يلد‪٩ ‎‬‬




                                                    ‫بیان دهم‬
             ‫در خای نقطه دار باشن نقطه دار مشتمل بر هفتاد و هفت‬

                                               ‫لغت و کنات‬

‫خشاوه » بکر اول بر وزن کلاوه ‪.‬‬                            ‫هس سم اول و سکون ثالی هً‬            ‫‪ ۱‬حش‬
‫ياكکردن باغ و زمینو کشت‌زار وزراعت‌باشد از‬                 ‫بمعتی ملدرزن ومادر شوهر باشد ‪ ۴‬؛ وبفتح اول‬
‫ویمعنی‌بیراستن‬   ‫>‬   ‫وخاشاك وعلفهای خودرو‬           ‫خی‬      ‫هم باینمه‌نی وهم بمعنی تند وتیز دوبدن آمده‬
 ‫هم هت که بریدن شاخهای زبادنی درخت‬                        ‫ات ‪ -‬و بيخ بغل را نیزکوبند و بعربی ابط‬
‫بسای وأو رای یی نقطه همآمده‬      ‫باشد؛ ویاشمعنی‬
                                                                                                   ‫خوانند ‪.‬‬   ‫‪je‬‬

                                           ‫‪.‬‬        ‫است‬     ‫خثاهی ‪ -‬بقتح اول و میم بر وزن‬
                                                            ‫زن‬      ‫مادر‬     ‫‪EER‬‏‬              ‫‪۰‬‬     ‫فلاخن‬
‫ضم اول بروزن‌همای بمعنی (‪)۱‬‬       ‫ه‬   ‫خثای‬
               ‫باشد ‪:‬‬   ‫نله‬   ‫کننده و ‪1‬‬        ‫خوش‬
                                                            ‫ومادر شوحراست » وبایئمعنی بضم اول هم آعده‬
                                                                                               ‫لت ‪. ۴‬‬
                                                            ‫خثا نیدن؟ ت بروزن رسانیدن‪ ,‬بدندان‬
‫‪۰‬آجر‬    ‫رشت‬    ‫هس بکراول‌بروزن‬        ‫حت‬



‫خام وپخته راگوبند ‪١‬‏ ‪-‬ونوعی از سلاح جنگه‬                              
==== leaf 209  printed ~ 749 ====
                                                                                                ‫یوا‬


‫‪٩‬‏ ‪-‬‬    ‫ند‬
         ‫زبان‬
            ‫دانوتن‬
                 ‫که در زیربغل جامه و می‬              ‫باشد ‏‪٩‬وآن‌یز؛ کوچکی‌استکه در میان‌آن‬
             ‫ویمعنیآینه زالو هم‌آمده امتا ‪۰‬‬          ‫بافته بسته باشند‬       ‫شم‬
                                                                             ‫رنیبا‬
                                                                                 ‫بسما‬
                                                                                    ‫ا ری‬
                                                                                       ‫حلقه‌ای از‬
‫ت بکسر دوخای تقطمدار‬     ‫حشت‬       ‫حشت‬
                                                    ‫وانگشت سبابة رادرآن حلقه کرده بجانب خسم‬
                                                     ‫انداز ند‪ - ۴‬ونام نك دوازدهم است از جمله‬
‫وسکون دوشین و تای قرشت » صدای ورق‌کاغذ‬
                                                      ‫و سك کتاب‪ .‬زند پوازند (ی‪۱‬ع)نی‬‫يتك‬ ‫بيس‬
‫ر جامه که نو پوشیده باشند‪.‬‬‫زمهیو‬
                              ‫وصدای جا‬
  ‫شیت‬
    ‫قتحررا‬
         ‫اول وف‬          ‫کهسدر‬
                             ‫بتر‬
                               ‫خش‬                    ‫بك قىم ازجملابیست وبك‌فم‪,‬چه نك بمعنی‬
                                                    ‫قم باشد ‪ - ۴‬و نوعی از حلوا هم هت که‬
                                                     ‫در مشکها و جاها ریزند نابك پارچه وقرص‬
‫پارچة چهار كوشة زبر بغل جامه و زبر جامه‬                                                               ‫دود‬

                             ‫وشلوار باشد ‪. ۸‬‬
                                                    ‫خشت تابه ه بافوقالی بالف کشد‪.‬‬
‫خشت رر د خشت ر رین کنابه‬                            ‫فوتح بای ابجد ‪ .‬کوره و داش خشت یزی را‬
                                                                                                  ‫‪۳۱‬‬
‫جفتلث = مصغر خش
==== leaf 210  printed ~ 750 ====
           ‫‪۷‬ی‬‫‪۲‬‬



                                                                      ‫خشتنشار ‪ = ۱‬بفتح اول وشین نقطه‌دار‬
 ‫کنابه از زر بر ه‬          ‫‪-‬‬   ‫کردن‬          ‫خشخاش‬                   ‫بالفکشیده بر وزن بهمنبار ‪ .‬مرغابی بزر گی‬
                                             ‫ریزه کردن باشد ‪.‬‬        ‫است تیره رنگ و میان‌سراوسفیدمیباشدوبتر کی‬
                                                                                                ‫قعقلداق خواند ‪.‬‬

‫وسکون دوشین وبك نای قرشت * بمعنی خشت‬
 ‫شد‬        ‫خای‬   ‫دو‬    ‫نکش‬       ‫‌‬   ‫‪5‬‬   ‫خشت‬        ‫حش‬

                                                                      ‫مفلوك ‪» .‬‬        ‫خشتو ك =(‪ )۱‬بر وزن‬
                                                                       ‫حرامزاده رااگویند ؛ ویض اول هم آمده است‪.‬‬
 ‫خشت‌است که صدای‌ورق‌کاغن وجامه وازاروشلوار‬
                                             ‫نو پوشیده باشد ‪.‬‬         ‫حشته = بفتح اول و فوقانی و سکون‬
 ‫‏‪ =m‬بققح اول وثانی وسکون‌کاف‪.‬‬                   ‫حك‬                    ‫انی ‪ ,‬مردم مفلس وبی برگك ونوا گروابند ‪.‬‬
 ‫وهی است وبعریی جبل خوانند ‪ -‬وبضم اول‬
                                    ‫نکام‬                              ‫خشحان ‪ ۲‬ه باجم بر وزن افشان ‪.‬‬
 ‫و سکون انی وکاف معروف است که دز مقابل‬                                ‫عناصر اربعه کروایند کهآب و خاك وهوا وآتش‬
  ‫ترباشد ‪٩‬‏ ‪ -‬وبمعنی محض و بحت (‪ )۲‬وصرف‬                                                                                 ‫باشد ‪.‬‬
‫ممسك را هم‬             ‫و‬       ‫و نحل‬          ‫انت‬     ‫امد‬   ‫لو‬        ‫خشخاش ‪ -‬مروف است ‪ ۰ ۴‬و آن‬
                                                 ‫میگویند ‪. ۷‬‬           ‫چند قم باشد ‪ :‬اببض واسود وزبدی ومقرن‪. ۴‬‬
                                                                       ‫خشخاش اییض بوستانی امت وآن سرد وترباشد‬
                               ‫مانم ومنم کننده را گوشد ‪۰‬‬               ‫و بعضی گویند خشك امت ‪ .‬خوردن آن باعسل‬
     ‫‪ .‬بضم اول
==== leaf 211  printed ~ 751 ====
  ‫دهان‬    ‫خك‬                                                                                                     ‫‪۳‬و‪۷‬‬
 ‫مازه ‪ ,‬شاخهای خشکی را کوبند که از درخت‬
      ‫‪-‬ت دگرخفتتهر‌ااند ‪.‬‬ ‫ودس‬‫پاشن‬
                                ‫وده ب‬
                                    ‫برب‬                          ‫وزن‌دزد(‪ )۱‬افثار » نخود و ماش و عدس و باقلا‬
‫حشت لسشجتالورست که اوراسنگه‬                                                               ‫ناد ‪.‬‬   ‫نتر‬
                                                                                                    ‫و]‬ ‫گثال‬
                                                                                                          ‫وام‬
                                                                  ‫خثشك امار ‪ -‬بتممزء رس‬
‫= بفتح بای فارسی وسکون‬              ‫ی‬     ‫خلت‬                   ‫"رضی است که‬
                                                                          ‫بالف کشیده وبرای قرشت زده م‬
‫مارزدم شوم قدم و نامبار که‬                ‫به‬
                                           ‫نیا»‬
                                              ‫کتان‬
                                                 ‫نح‬               ‫آابعربی استسقا گوبند ؛ وبابنمعنی بجای میم»‬
                                                                                                           ‫نر‬
                                                      ‫باشد ‪۰‬‬                                   ‫نون هم بنظرآمُده است ‪.‬‬
 ‫جان‪ -‬با جيم بروزن مرغدان‬                  ‫خشك‬                    ‫خشکا مار ‪ -‬بنماور وثالك مویم‌هر‬
                                                                  ‫دو بالف کشده وبرای فرشت زده › ممعنی‌خشك‬
  ‫یده‬
    ‫ششق‬
      ‫نتج ع‬
          ‫و شخصی را نیز گوبند که اذ‬                               ‫امار است که مرض استسفا باشد؟ ‪ -‬وبمعنی‌هبم‬
  ‫ناث ‪.‬‬   ‫محروم‬        ‫نکرده واز باد دوست‬       ‫و ءاشقی‬           ‫واستقصا ونفحص وتجسی واءتفساروحاب‌واستیفا‬
‫حشلت جنیان ‪ -‬کی را گونند که‬ 
==== leaf 212  printed ~ 752 ====
    ‫‪4‬‬


                                                                ‫خشثك دیش د بکر رای بقیطه‬
                                            ‫‪.‬‬   ‫خممر فزق‬       ‫و سکون تحتالی و شين نقطه دار ‪ .‬بمعنی مکر‬
‫خشاث مغز = بمعنی‌خنك سراست که‬                                   ‫وحله‌وفاق وفریفتن وبازی‌دادن وبهانه کردن(‪)۱‬‬
                                                               ‫وخشکیی رایزگونند که بر‬          ‫_‪)۲‬‬
                                                                                                 ‫دن(‬
                                                                                                   ‫شرد‬
                                                                                                     ‫اآو‬
                                                                                                       ‫بذر‬
                                                                                                         ‫وع‬
              ‫بی‌ته ودیوانه‌وش وتند خوی باشد ‪٩‬‏‬
                                                                                      ‫روی زخم بسته شود ‪٩‬‏ ‪.‬‬
‫خشکنانه ‪ = ۲‬بانون‌بر وزن موربانه‪.‬‬
      ‫نانیراگوبند که آنرا بی‌نان خورش خورند ‪.‬‬                  ‫خثك ر بشه » بنتح تن فرتت ‪۱‬‬
                                                               ‫بمعنی بهانه کردن و عذر آوردن باشد چنانکه‬
‫خشکنای « با ون بالف کشد‬                                        ‫اکر گوند خنك رشه میکند مرادن ‪,‬اشد‬
‫زده » نای کلورا گویند ‪ ۰‬و بعربی حلقوم‬
                                      ‫بتحتانی‬
                                                               ‫که بهانه میکند ‪ -‬وخشکی روی زخم را نیز‬
                                                    ‫خوانند ‪.‬‬                                            ‫کو‬
‫خشکو اھ » باواو ‪.‬بر وزن و ععنی‬
                                                               ‫خشکسار؟ ‪ -‬باسینبی قطهبروزن‬
      ‫خشکفاست که نانخمیر برتیامده وفطیرباشد‪.‬‬                   ‫بردبار » زمی
==== leaf 213  printed ~ 753 ====
                                                                                                                ‫‪۷۲‬‬


 ‫بزر کهتیرء رن میانسرسفید باشد و ترکان‬                            ‫خشی ه بنتح اول بروزن چمن گ‪.‬یاهی‬
‫قثقلداق میگوبند ‪ ۰‬وبضم اول نیز درست است "‬                         ‫باشد کهاز آن جامه بافند و فقیران ودروشان‬
‫و بشاین نقطه دار همآمده است چه در فارسی‬                           ‫پوشند ‪ -‬وبکر اول مخفف خشین است» ‪ ۰‬آن‬
 ‫سین وشین هردو بهم تبدیل می‌بابند ؛ و بجای‬                         ‫بازبی باشد نه‌سقید وله سباء ‪ -‬ودرعربی هرچیز‬
 ‫لون بای حطی هکمفته اند کهبر وزن بدیدار‬                                                             ‫درشت را گوشد ‪۳‬‬
                                                   ‫باشد ‪.‬‬         ‫خشنان ‪ -‬ب باضمول بر وزن برهان ‪۰‬‬
‫‪ -‬بر وزن بلنگ ‪ ,‬زاغ سر‬                    ‫حشنگ‬                                       ‫فرخنده وخجسته ومبارك راگوبند ‪.‬‬
‫وسر کجل و کجلی را کوبند ‪ -‬و مردم کچل را‬                           ‫ک=نابه ازمنافق‌بودن‬            ‫دن‬
                                                                                                  ‫شیلو‬
                                                                                                     ‫ش‬ ‫خ‬
                                           ‫تگبفزته‌اند‪.‬‬                                             ‫وطاق کردن باشد ‪.‬‬
         ‫‪۱‬‬       ‫‪۲‬‬     ‫معیم ‪. _ ۵‬‬
 ‫حشنو = بامول والك بروزن‌پر کو‪.‬‬                                   ‫خشی خاله = بروزن‌طر بخانه‪ .‬خانه‌ای‬
 ‫مخفف خشنود است که راضی وخوشحال باشد ‪۰‬‬
                                                                  ‫‪۰‬ویند که ازتی بوربا سازند ‪ -‬و خانه‌ای رانيز‬
                                                                                                            ‫گ‬
                    ‫ویفتح اول هم درست است ‪۴#.‬‬                      ‫گته‌اند که بر در ورنجرءآن خار شتری ندند‬
  ‫حشنی ‪ -‬بضم اول و کر الك بورزن‬                                    ‫و آب بر آن پاشند تا
```


## [2026-09-05T20:33:32.272Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (208,209):\n    print(\"==== leaf\",n,\"FULL ====\")\n    print(leaves[n])\nEOF"
}
```


### [2026-09-05T20:33:34.200Z] TOOL RESULT

```
==== leaf 208 FULL ====
 ‫‪Yg‬‬     ‫~‪m‬‬                                                                                      ‫‪‎‬هرو‬


‫بمعنی‬   ‫‪ -‬بر وزن رسیدن »‬         ‫خسدن‬                      ‫خسوره ه بم اول وفتح رای قرشت؛‬
‫استت که در زیر «ندان ترم کردن‬           ‫خایدن‬              ‫یمضی خور استت که پدر شوحو و پدر زن‬
                                                                                                    ‫يلد‪٩ ‎‬‬




                                                    ‫بیان دهم‬
             ‫در خای نقطه دار باشن نقطه دار مشتمل بر هفتاد و هفت‬

                                               ‫لغت و کنات‬

‫خشاوه » بکر اول بر وزن کلاوه ‪.‬‬                            ‫هس سم اول و سکون ثالی هً‬            ‫‪ ۱‬حش‬
‫ياكکردن باغ و زمینو کشت‌زار وزراعت‌باشد از‬                 ‫بمعتی ملدرزن ومادر شوهر باشد ‪ ۴‬؛ وبفتح اول‬
‫ویمعنی‌بیراستن‬   ‫>‬   ‫وخاشاك وعلفهای خودرو‬           ‫خی‬      ‫هم باینمه‌نی وهم بمعنی تند وتیز دوبدن آمده‬
 ‫هم هت که بریدن شاخهای زبادنی درخت‬                        ‫ات ‪ -‬و بيخ بغل را نیزکوبند و بعربی ابط‬
‫بسای وأو رای یی نقطه همآمده‬      ‫باشد؛ ویاشمعنی‬
                                                                                                   ‫خوانند ‪.‬‬   ‫‪je‬‬

                                           ‫‪.‬‬        ‫است‬     ‫خثاهی ‪ -‬بقتح اول و میم بر وزن‬
                                                            ‫زن‬      ‫مادر‬     ‫‪EER‬‏‬              ‫‪۰‬‬     ‫فلاخن‬
‫ضم اول بروزن‌همای بمعنی (‪)۱‬‬       ‫ه‬   ‫خثای‬
               ‫باشد ‪:‬‬   ‫نله‬   ‫کننده و ‪1‬‬        ‫خوش‬
                                                            ‫ومادر شوحراست » وبایئمعنی بضم اول هم آعده‬
                                                                                               ‫لت ‪. ۴‬‬
                                                            ‫خثا نیدن؟ ت بروزن رسانیدن‪ ,‬بدندان‬
‫‪۰‬آجر‬    ‫رشت‬    ‫هس بکراول‌بروزن‬        ‫حت‬



‫خام وپخته راگوبند ‪١‬‏ ‪-‬ونوعی از سلاح جنگه‬                                             ‫رش کردن باشد ‪.‬‬


      ‫نیز‪ 311501‬بپمن معالی کےنواد) رك خ‪:‬سر‪ ,‬خسوره‬                           ‫( ‪5‬‬      ‫اك‬
                                                                                      ‫اردر‬
                                                                                         ‫‏‪٩‬‬
         ‫‪9‬‬   ‫رك‪ :‬خشتامن» خش‬                     ‫‪.‬‬    ‫‪..‬خشتامن‬    ‫‪ ۳‬مقاءل«خر»(د‪.‬م ‪).‬ره خشامن‬


             ‫‪O‬‬                         ‫‪ - ۴‬اسدی کوبد ( لفت فری ‪TR‬‏‬
                                                                                   ‫) کوید ‪:‬‬   ‫(سمرقندى‬

                                   ‫بی شك ( بثك ‪ .‬دهخدا) لهنگ‌دارد دل را همی خشاید‬
              ‫ترسم که ناکوارد کایدون ته خرد خاید ‪» .‬‬
  ‫بیداست که خشانید» فعل ماضی استاز « ختایدن» ؛ دربن صورت مضارع آن «خشاند»‬
  ‫اشد ( ماتتد رساند از رسالیدن ) ته خشاید که باید ازمسدر خشودن (همجون کشاید از کشودن )‬
   ‫‪.‬هراً مصدرفمل بموزر‬
                     ‫یاخشابیدن(هموپایدازپابیدن) باشد‪,‬وخشودن بمعنی دیگریآمده («‪.‬م‪ ).‬ظا‬
                     ‫‪ = ۵6‬خوش آی (خوش آننده) ‪.‬‬                             ‫خشاسن است ‪ .‬رك ‪ :‬خایدن‪.‬‬
   ‫‪ ۱‬پهلوی ‪ , 6051‬اوستا ‪ 800151 -‬ساسکرت ‪« 2612005 -‬اسفا ‪ ۲ :۱‬ص ‪۷٩‬‏‬
                                           ‫و ‪ . ۷۸۰‬افنانی شاناک‪« ]2‬هوبشمان ‪»۸۸4‬‬
  ‫زیرهای قاطع)»)‬

==== leaf 209 FULL ====
                                                                                                ‫یوا‬


‫‪٩‬‏ ‪-‬‬    ‫ند‬
         ‫زبان‬
            ‫دانوتن‬
                 ‫که در زیربغل جامه و می‬              ‫باشد ‏‪٩‬وآن‌یز؛ کوچکی‌استکه در میان‌آن‬
             ‫ویمعنیآینه زالو هم‌آمده امتا ‪۰‬‬          ‫بافته بسته باشند‬       ‫شم‬
                                                                             ‫رنیبا‬
                                                                                 ‫بسما‬
                                                                                    ‫ا ری‬
                                                                                       ‫حلقه‌ای از‬
‫ت بکسر دوخای تقطمدار‬     ‫حشت‬       ‫حشت‬
                                                    ‫وانگشت سبابة رادرآن حلقه کرده بجانب خسم‬
                                                     ‫انداز ند‪ - ۴‬ونام نك دوازدهم است از جمله‬
‫وسکون دوشین و تای قرشت » صدای ورق‌کاغذ‬
                                                      ‫و سك کتاب‪ .‬زند پوازند (ی‪۱‬ع)نی‬‫يتك‬ ‫بيس‬
‫ر جامه که نو پوشیده باشند‪.‬‬‫زمهیو‬
                              ‫وصدای جا‬
  ‫شیت‬
    ‫قتحررا‬
         ‫اول وف‬          ‫کهسدر‬
                             ‫بتر‬
                               ‫خش‬                    ‫بك قىم ازجملابیست وبك‌فم‪,‬چه نك بمعنی‬
                                                    ‫قم باشد ‪ - ۴‬و نوعی از حلوا هم هت که‬
                                                     ‫در مشکها و جاها ریزند نابك پارچه وقرص‬
‫پارچة چهار كوشة زبر بغل جامه و زبر جامه‬                                                               ‫دود‬

                             ‫وشلوار باشد ‪. ۸‬‬
                                                    ‫خشت تابه ه بافوقالی بالف کشد‪.‬‬
‫خشت رر د خشت ر رین کنابه‬                            ‫فوتح بای ابجد ‪ .‬کوره و داش خشت یزی را‬
                                                                                                  ‫‪۳۱‬‬
‫جفتلث = مصغر خشت است ‪ -‬وبارچة‬                        ‫خشتامی ‪ -‬بفتح اول بروزن تردامن »‬
‫مربع زیر بغل جامه ومیان تنبان وشلوار را لیز‬           ‫و سم اول نیز درست‬         ‫مادر زن رگاونند‬
       ‫عنته‌اسه‬
              ‫کون وآیینه (‪ )۲‬زائو را مک‬                                                         ‫ات ‪. ۴‬‬

‫کابه از آقاب‬              ‫خشتك رر‬                    ‫حشتچه » بکر اول وفتح جیم‌فارسی‪.‬‬
                               ‫‪۰‬‬   ‫عالمتاب ست‬        ‫ه باشد‬    ‫شر‬ ‫و‌چها‬
                                                                      ‫گه‌ای‬
                                                                          ‫خشتك رگاونند ؛وآن پارچ‬

                               ‫(‪)۲‬اچك‪ .‬چش‪ :‬مئه ‪۰‬‬                 ‫(‪ )۱‬چك ‪ :‬ژند ویاژند ‪.‬‬
  ‫‪ - ۱‬هندی باستانی ‪( 1۵5۲‬یزه) » قی‪ :‬اوستا ‪ -‬ئ‪ » 5۲3‬بارسی‌باستان یز لاتا‪.578‬‬
                                         ‫ص ‪۷٩‬‏ *‪.‬‬        ‫سنا‬      ‫بهلوی] ‪٠ 015۳2‬‏ ارمنی ع ‪yaeth‬‏‬
                                         ‫‪ - ۴‬وقت محر که کلنك تسبه ای ساخته است‬
             ‫هند تا خزران تاخثه است‬       ‫یای‬
                                            ‫ودزرل‬
           ‫است‪...‬‬
                ‫‌شت‬
                  ‫تسته»خ‬
                       ‫خ‌ا‬
                         ‫افته‬
                            ‫نردو کو‬
                                  ‫بل‌ف‬
                                     ‫طم‬                  ‫می سیه‌برففاش تيغ برون‌آخته امت‬
  ‫«منوچهری داحقاتی ‪.*۷4۱‬‬
  ‫ی مزدسنا‬    ‫است‬   ‫یا ‪dãdartiC‬‏‬   ‫‪tãûdartiC‬‏‬   ‫دات‬    ‫دوازدهم اوستا چىىرە‬    ‫نام سك‬   ‫ك‬   ‫‪۳‬‬


 ‫باشد‬    ‫وىك شت‬     ‫دوازدهم ازست‬   ‫شت‬    ‫رشن ‪٩‬‏ ‪)unhsar(ue‬‬      ‫‪ ۰‬وشایف خشت مصحف‬           ‫‪۵‬‬    ‫برآبر ص‬

  ‫‪ _ ۵‬رك‪ :‬خشتره » خشنت‪«.‬خشتحه‪.‬‬              ‫رك ‪ :‬خشامن » خش ‪.‬‬           ‫‪۴‬‬         ‫رک‪ :‬شت ‪ ۱‬ص‪۹۱‬‬

  ‫زربکش جامه و پوتیدنی باشد وخشتك نیز گوبند ومردم‌عوام‌سوژه گوبند ‪ .‬همارهم(مروزی) کوبد‪:‬‬
           ‫حم‌ایچ کم نشود یوی گنده‌از خلت‪».‬‬            ‫بجای خشتجه کرشت افه بردوزی‬
  ‫«لفت فرس ‪.۸ ۲۲‬‬
 ‫خشت («‪.‬م‪).‬‬     ‫خش ( بکسر دوخاء ( "‪ ۳‬خش‬         ‫خش‬    ‫‪ - ۷‬اسم‌صوت =‬     ‫‪:‬‬    ‫رك‪:‬خفتك‬       ‫‏‪٩‬‬

       ‫کی‬
        ‫ن‪.‬‬‫شصلا‬
             ‫خا‬‫‪ _ ۹‬رك‪ :‬خشنحه ‪۰ ۰‬‬                ‫‪۰‬‬    ‫خعتك‬   ‫رك‪:‬خشتجه(متن‌وحاشیه)»‬          ‫‪۸‬‬

                                                            ‫(رك‪ :‬خشتك) کهزر دوزی شده باشد ‪:‬‬
             ‫خدتك زرسوزء(سوزء) بیراهنش‪.‬‬                       ‫پرزر و درگشته ز تدوامن‬
  ‫ظامیکنجوی‪ « .‬کنجینه‪۲‬ه*‪.‬‬
```


## [2026-09-05T20:34:24.325Z] TOOL CALL #22: Bash

```json
{
 "command": "pdftoppm -f 161 -l 161 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg161 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:34:24.936Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins es- ===\"; grep -n \"^es-\\|es- *To be\\|swastika\\|proud\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:34:26.694Z] TOOL RESULT

```
total 16064
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:34 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:34:26.757Z] TOOL RESULT

```
=== AHD watkins es- ===
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
460:es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
1087:teue-. Also teu-. To swell. 1. Extended form *teuk- in Germanic *theuham, “the swollen or fat part of the leg,” thigh, in Old English théoh, thigh: THIGH. 2. Extended form *tis- in Germanic compound *thiis-hundi-, “swollen hundred,” thousand (*hundi-, hundred; see dekm), in Old English thisend, thousand: THOUSAND. 3. Suffixed zero-grade form *tu-l- probably in Germanic *thul- in Old English thol(l), oar pin, oarlock (< “a swelling”): THOLE PIN. 4. Extended zero-grade form *tiim- in: a. Germanic *thimoén- in Old English thima, thumb (< “the thick finger”): THIMBLE, THUMB; b. suffixed (stative) form *tum-é- in Latin tumére, to swell, be swollen, be proud: TUMESCENT, TUMID, TUMOR; DETUMESCENCE, INTU- MESCE, TUMEFACIENT, TUMEFY; C. suffixed form *tum- olo- in Latin tumulus, raised heap of earth, mound: TUMULUS. 5. Extended lengthened zero-grade form *tibh- in Latin tiber, lump, swelling: TRUFFLE, TUBER; PROTUBERATE. 6. Suffixed zero-grade form *tu-r-yo- in Greek turos, cheese (< ‘“‘a swelling,” “coagulating”’): BUTTER, TYROSINE, TYROTHRICIN. 7. Suffixed variant form *tw6-ro- in Greek sdros, heap, pile: SORITES, SORUS. 8. Suffixed variant form *twd-mn, in Greek sdma, body (< “a swelling,” “stocky form”): SOMA, SOMATO-, -SOME?; PROSOMA. 9. Suffixed zero-grade form *twa-wo- in Greek saos, sds, safe, healthy (< “swollen,” “strong”), with derivative verb sdzein, to save, rescue: CREOSOTE, SOTE- RIOLOGY. 10. Perhaps nasalized extended form *tu-m-b(h)- (or extended zero-grade form *tum-) in Greek tumbos, barrow, tomb: TOMB. [Pok. téu- 1080.]
```


## [2026-09-05T20:34:34.921Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg161.png"
}
```


### [2026-09-05T20:34:35.301Z] TOOL RESULT

```

```


## [2026-09-05T20:34:35.294Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:34:52.886Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 161 -l 161 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg161_600 && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg161_600.png')\nprint(im.size)\nw,h=im.size\n# empty box next to Old Persian: approx x 0.52-0.78, y 0.44-0.50 of page\nim.crop((int(0.50*w),int(0.435*h),int(0.80*w),int(0.50*h))).save('crop_empty.png')\n# -am persian script area\nim.crop((int(0.50*w),int(0.355*h),int(0.80*w),int(0.405*h))).save('crop_am.png')\nEOF\nls -la crop_*.png"
}
```


### [2026-09-05T20:34:57.617Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb  4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb  4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb  7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb 16978 Sep  5 16:34 crop_morocco.png
```


## [2026-09-05T20:34:59.941Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_am.png"
}
```


### [2026-09-05T20:34:59.954Z] TOOL RESULT

```

```


## [2026-09-05T20:35:00.676Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_empty.png"
}
```


### [2026-09-05T20:35:00.689Z] TOOL RESULT

```

```


## [2026-09-05T20:35:12.792Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg161_600.png'); w,h=im.size\nim.crop((int(0.50*w),int(0.480*h),int(0.80*w),int(0.545*h))).resize((1300,int(1300*(0.065*h)/(0.30*w)))).save('c_empty2.png')\nim.crop((int(0.68*w),int(0.428*h),int(0.79*w),int(0.452*h))).resize((1200,int(1200*(0.024*h)/(0.11*w)))).save('c_am2.png')\nEOF\necho done"
}
```


### [2026-09-05T20:35:14.917Z] TOOL RESULT

```
done
```


## [2026-09-05T20:35:17.766Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_am2.png"
}
```


### [2026-09-05T20:35:17.781Z] TOOL RESULT

```

```


## [2026-09-05T20:35:18.108Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_empty2.png"
}
```


### [2026-09-05T20:35:18.173Z] TOOL RESULT

```

```


## [2026-09-05T20:35:30.749Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg161_600.png'); w,h=im.size\nc=im.crop((int(0.700*w),int(0.425*h),int(0.790*w),int(0.450*h)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS)\nc.save('c_am3.png'); print(c.size)\nEOF"
}
```


### [2026-09-05T20:35:33.277Z] TOOL RESULT

```
(1377, 495)
```


## [2026-09-05T20:35:35.707Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_am3.png"
}
```


### [2026-09-05T20:35:35.739Z] TOOL RESULT

```

```


## [2026-09-05T20:36:11.499Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK astra Stachel ===\"; grep -n \"asträ\\|aṣṭrā\\|astra  ,Stachel\\|,Stachel'\" POK_01.txt | head -10; echo; echo \"--- POK ag- treiben context ---\"; python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"ag'-\")\nimport re\nfor m in re.finditer(r\"Stachelstock|Treibstecken|Stachel'\", t[:200000]):\n    print(m.start(), t[max(0,m.start()-300):m.start()+120].replace('\\n',' '))\n    print('---')\nEOF"
}
```


## [2026-09-05T20:36:12.039Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6485,6520p' BRT.txt"
}
```


### [2026-09-05T20:36:14.079Z] TOOL RESULT

```
=== POK astra Stachel ===
61:Als  idg.  Instrumentalnomen  auf  -trä  hierher  ai.  asträ  ,Stachel  zum Viehantreiben^,  av.  asträ  ,Peitsche,  Geißel'.

--- POK ag- treiben context ---
49994 r  ag's.  eher  ,Alire'  s.  unter  s-Formantien. 3.  u-St.: Gr.  icxvQOv  , Spreu'  s.  unter  s-Formantien ;  lat.  acus^  -üs  L  , Nadel;  Fiscli- name',  acuere  , schärfen',  acümen  , Spitze',  acia  (f^acu-iä)  , Faden  zum Nähen',  aquifolium  (neben  äcrifoUum)  , Stechpalme',  aculeus  , Stachel', accipiter  ,Habicht,  Falke'  (*acu-peter  ,schnellfliegendQ ;  gall.  acaunum (^akounon)  , Felsen';  ill.  O
---
126212 f-arn ,Klaue^)  aus  "^cmkato-  =  aksl.  gkoth  ^Haken'^; gallorom.  ancoi'ago,  ancora(y)iLS  aus  ^miko-räkos  ^Rheinsalm,  Hakenlachs' schwd.  Anke  ^Bodenseeforelle'  (g"^^l-  *cinko-  ^gekrümmt'  und  *7'äko-  ,vorne^ aus  *prökO',  cymr.  o^hag  ;Yor^); ahd.  angoj    angul   ^Fischhaken^    Stachel'^    aisl.  angi^    ags.   onga   ^Spitze] Stachel'  i^aidkön-]    über   got.  halsagga  ^Halshiegung,   Nack
---
126265 en'^; gallorom.  ancoi'ago,  ancora(y)iLS  aus  ^miko-räkos  ^Rheinsalm,  Hakenlachs' schwd.  Anke  ^Bodenseeforelle'  (g"^^l-  *cinko-  ^gekrümmt'  und  *7'äko-  ,vorne^ aus  *prökO',  cymr.  o^hag  ;Yor^); ahd.  angoj    angul   ^Fischhaken^    Stachel'^    aisl.  angi^    ags.   onga   ^Spitze] Stachel'  i^aidkön-]    über   got.  halsagga  ^Halshiegung,   Nacken'   s.  vielmehi angh-);  "^-angra  (bis  aufs  Ges
---
176545 e  in  der  Diagonale  des  Segels  stehende  Spreiz- stange' (s.  zur  Bed.  Bezzenberger  GGA.  1885,  920)'?  Petersson  KZ.  47, 245  (die  lit.  Wörter  nicht  besser  nach  Leskien  Abi.  329  zu  ardyti  ,spal- ten,  trennen',  s.  unten   er-  ,locker'). WP.  I  84. ardi-,  rdi-  , Spitze,  Stachel'. Ai.  ali  , Biene,  Skorpion'  (aus  *a^i,  idg.  *i'di)  =  gr.  Uqdig  , Pfeilspitze, Stächet;  air.  aird  
---
```


### [2026-09-05T20:36:14.119Z] TOOL RESULT

```
Eig.  Bed.?  — O  NA.  asti  ga/yö,  aberFla/Ki'; vgl.  zu  *iüvß^a/ya-.
•  j.  aäti.masah-  Adj.  'von  der  Grösse einer  A.':  äat  pitSus  ydi:a  cdijiciärS  'sS N.  (7^(?);  —  taltim  dauru  . . nyäzaym  (sd.) +°jj')  xraoidvaAe  bti'  altavatö  var>dvahe "ein  .  .  Stück  Holz  .  .  von  der  Grösse" einer  Ä.  aus  hartem,  doppelt  so  gross'' aus  weichem"  V.  13. 30.
Pü.:  aiink  masäk,  (lu  N.):  fighi  4  Ai7/(?)  aitak masäk.  —  I)  NA.  iilim';  s.  Var.  —  =)  Es handelt  sich  um  die  Dicke  de»  HohknebeU. Ihn  verschieden  lang  zu  nehmen  je  nach  der Holiarl,  wäre  sinnlos.
•  j.  aätra-Dhäd-  Adj.  'mit  der  Peitsche lenkend':  mi^rnn  .  .  °»Aäojm  amavanUm .  .  ra>aestq//i  Ytio.  112.
VgL  aL  aiträ  . .  paJiiiad&am  KV.  6.  53.  9  und
dby  Google
a63  aäträ-  —  aÄya-  264
•  j.  alträ-    f.    'Geisel,    Peitsche,    Knute':  narü  xsa^ra  xsaymU  "va  ni'jäiu.pifu  VL yat  b>r3z»m   barat   'ra  väam  "wenn  laut  1/7.  7;  5.130.
die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
?/aAl%asA:  yaaam  zavanam  aiauntru'ra   it^ae\  vt  rs  »i
V.;4.8;  -  -r««   ;««>?«  (sd.)  käsayäti  ^',TV  ,  ÄJ';  ..  t-  «/«^.-^...  No.  >. V.  i8. 4:  —  tüiryeAe  *>rl  vä  axaiä  (sd.)  v  ,    „  -,..,-.       ^
sracsöJaranaya    'mva   V.f,.        «)   meist  VJ-   as.fralwnrtay-   f.   'reichliche   Dar- mit  ospaA,  'Pferdegeisel':  irisal^  upäza-   )"^''$'-  '''"^"^  ""'^r<""J"'  hu/rab?mt,ca
n  (Stverz.)  upüzoit  (sd.)  aspake  'raya
(sd.)  Yt  10.  77.
>riiat^  sraoislaranaya  V.4.19;  usw.     '"  j.  as.fra'y^tay-  £ 'reichliches  Opfern,
KompA-,  E.  —  Zum  V.  az-;  eig.  'Vorrichtung  Weihen':     °tica    zaoiranam     Au/räyastica
zum  Antreiben  der  Tiere' ^J.    —    ai.  dilt-i-  f.  "mit  reichlicher  und  guter  Weihe  von  Z."
•Stach el stock' I um  ViehmtieibeD 'l,  mp.  (Pu.)  y^  ,„   _,,)
^/,(J«,A.PJ1  010.^,631  -  »AI.  Hoh,i...  'V°e(/.S,.  V.  «X,. zeichen,  5.  Dnler  iitxera-.  —    ')  VgL  an.  geul  ^  '
'Stocic,  £ub'  und  ahd.  i-^öAi  'Peitsche'  usw.  j-  '^''''  (Nerbalf.):  s.  qs-.
•  j.  as.dSnav-  Adj.  'mit  starken,  grossen  •  P-  aSna-  m.  'Marschiren',  mit  astty  'er (Samen-)Körnem':  us  apam  aoavS  .  .  befindet  sich  auf  dem  Marsch  nach  — ' jasänti  -nunqmca  yavanq'm  kasuJätm-  («^V  »"'*  Akk.):  *adaiiy  adam  ^naiy^^ natnca  västra'nam  "die  wässerbäche  wer-  •'^'"»  "^'y  ''uv'^jam  pasäv<^  kacämi/' den.,  hervorbrechen  hin  zum  Getreide  atars<^^y^  uz-aßyä  "damals  war  ich mit  den  grossen  und  zum  Gras  mit  den  ^  d^™  Marsch  nach  Susa;  drauf  bc- kleinen  Körnern"  YtÄig".  kamen  die  Suser  Furcht  vor  mir"  Bh.2.4.
Vgl.    Bd.    24.    29:    sla-i'rdänak    ÖirtakSn.    —  '       Zum  V.  ai-.  —  Vgl.  '<i4-  I  S;  BTIUL  BB.  15.
1)  iSynL  s.  Hbm.  ZC  176.  34,    ZDMG.  43-  666,   IF.  10.  190.    Fov  KZ.
V      o__  ,^  .....         „       '      35-  37,  69,  ZUMG.  53.  567.  —    'i  Allenfalls
.  ].  asa-*wo.zgatama-  Ad,,  'der  aUer-      ^Xr/:  d^n  ain^y-Ai.  ILm  =  j.  a>n^:  aL drängendste,  allereifrigste':  °mq  gavästrya-       äsmana).  —  jj  Vgl.  %rah-  No.  3. varlt>niq  narqm  asäunqm  Y.  13.  2.  '         j.  ainäat^a,  ainJ:  s.  unter  aiaa-.
SuperU'    aus    *ai>-%wö^^'ä-  Adj.    'der    starken  j,  asnSMmäi  N.  70:  lies  daiinSJimäi.
Drang,  Efer  hat'.  —  *ä:imj!f  J-  f.  (statt  %-jiaz;',
S  aß-j'.  57),   lum  V.  ia;^s-;  »erhält  sich  zu  •  j.  as.manah- Adj. 'mit  Starker  Begierde,
^'.^qzj-aiti  wie   ai.  iccAa-   zu  ahd.  eisi-öii.  —   Brunst*:    ustra»h5  .  .    sainiMaofa    'nanha
Pü.:  vai  raf,jnr..!iS;lum.  Sü.:  bakukUiaharsa-    (fjpm.)    Vt.  77    11 tamak.    —     ')    Mit   dem    Ideogramm    für    röe  '  /       J
geschr.,  s.  Mills  SBE.J/.  251  (wo  eine  gren-  •    j.    as.inizda-    Adj.    (fem.  'di-)    'reich- hche  Etymologie).  .liehen    Lohn    bringend,    eintragend':    /v
•  j.  aS.paourva-  Adj.  'der  weitaus  vor-  (näml.  gs>a)  n5  buyqn  Aumiida  (sd.)  -ds anstehende,  erste':  aisam  nmäna . .  hisimte  Y.55.  a.
-va  darrjS.upastSe  (sd.)  Vt  77.  8.  Pu.:  vat  mizd.
•  j.  aä.padina-  Adj.  'wo  man  viel  kocht':  •  j.  asya-  Adj.  'der  es  mit  dem  heiligen xsä^ra..  siai.iaxxra  (sd.)  °na  Vt.5. 130.   Recht,   mit  Asa  hält'  sva.  'fromm,  recht-
■Kochen',    znmV. /a.*-;    '  nach  !  schaffen',     nur    von    Sraosa:
S  2g8.  4.  -
```


## [2026-09-05T20:36:27.800Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"asträ  ,Stachel  zum\")\nprint(\"leaf\",t.count('\\f',0,i)+1)\nprint(t[max(0,i-2500):i+500])\nEOF"
}
```


### [2026-09-05T20:36:29.468Z] TOOL RESULT

```
leaf 12
 ,bis'. WH.  [  12,  Devoto  Mel.  Pedersen  224.
ades-,  ados'  n.  , Getreideart,  Spelt'.
r^at.  ador,  -(fi'ü  n.  ,eine  Art  Getreide,  Spelt',  vielleicht  zu  got.  atish (*ade8-lco-)  , Saatfeld',  wohl  m.  wie  ahd.  ezzisca  PI.  ,Saat',  mhd.  dial.  Esch, Schweiz,  dial.  Aesch,  , Feldflur  eines  Dorfes';  toch.  AB  äti  , Gräser'  (anders Pedersen  Toch.  64^).    Über  gv.  ä^rjQ  s.  unter  andh-.
WP.  I  45,  Feist  61a,  anders  WH.  I   14.
ad(u)-,  ad-TO-   ,Wasserlau£'.
Avest.  aöu  , Wasserlauf,  Bach,  Kanal',  ven.-ill.  FIN  Ad(cl)ua  (zum  Po), *Adulia':>Attel  (zur  Donau  in  Bayern),  Mons  Adulas  ,St.  Gottbard^  (wohl nach  den  dort  entspringenden  Flüssen  benannt),  der  oberösterr.  FIN  *Adra -^Attersee,  Attergau,  FIN  Adrana>  Eder  (Hessen),  vielleicht  auch  der ON  Adria  in  Venetien  (danach  das  mare  Adriaticum),  der  sizil.  FIN  ^Adgavög und  der  ven.-ill.  Name  der  Oder  OvL-adovag]  ferner  der  lett.  FIN  Adula. Vasmer  ZslPh.  8,  114  f.,  Pokorny  Urill.  4,  70,  93,  109,  124.
ag-  jtreiben'  (eigentlich  wohl  ,mit  geschwungenen  Armen  treiben'),  , schwingen', in  Bewegung  setzen,  führend  Ursprünglich  auf  den  Präsensstamm  be- schränkt.
agö:  ai.  djati  ,treibt',  av.  azaiti  ^treibt,  führt  weg*,  arm.  acem  , führe, bringe^;  gr.  Uyuj  ,führe^  (Aor.  }}yayov,  ^^^a  [sind  jung),  lat.  agö  ^treibe^  führe, verhandle^  (Pf.  egl  mit  Ablautneuerung),  osk.  Imper.  actud  =  umbr.  aitu ,agito',  osk.  acum  ^agere^,  air.  ad-aig  {*aget)  ,adigit',  acymr.  agit,  hegit, jünger  eyt  {*agiti),  daneben  die  starke  Flexion  in  cymr.  corn.  bret.  a  (*aget) ,geht^;  ^Prät.  air.  ro-da-acht  ,trleb  sie  forf^,  cymr.  aeth  (*ag-t)  ,iit^  usw., s.  Pedersen  KG.  II  451  ff.,  air.  äin  ^Treiben,  Spiel^  (aus  *agms),  gallo-rom. *and-agnis  ,großer  Schritt^,  frz.  andain  , Schwade,  Sensenhieb',  afrz.  ,Weit- schritt^,  anord.  aka  , fahren*"  (Prät.  ök  wie  ai.  Gramm,  äja)]  ags.  ac  ,aber, sondern'  (wörtl.  ,geh!^  wie  lat.  age)]   toch.  B  ak-,  AB  äk-  , reisen,  führend
fo-Partiz.:  ä/,T6g,  lat.  actus,  kelt.  *amb{i)-aktos  eigentlich  , herumge- sandter (:  air.  imm-aig)  Bote,  Diener'  in  gall.  (-lat.)  amhactus  , Dienstmann, Höriger^,  cymr.  amaeth  ,servus  arans'  (aus  dem  Kelt.  stammt  got.  andhalits, ahd.  ambaht  , Diener^,  woraus  die  Sippe  von  nhd.  Amt).
Als  idg.  Instrumentalnomen  auf  -trä  hierher  ai.  asträ  ,Stachel  zum Viehantreiben^,  av.  asträ  ,Peitsche,  Geißel'.
Dehnstufenbildungen:  ai.  äji-h  m.  f.  ,Wettlauf,  Kampf,  mir:  äg  (Gen. äga,  w-St.)  ,Kampf^,  äga,  aige  ,Führer'  (vgl.  auch  gall.  PN  Ago-märus =  air.  dgmar  , kriegerisch'';  Com-ägius),  lat.  nur  in  Kompositis:  amhägeSj -um  ,Umgang,  Umlauf;  Irrgang;  Winkelzüge'  (kons.  St.  wie  ai.  dj-E  ,zu treiben'  =  lat.  agi  Inf.  Pass.,  und  wie  ai.  aj-  in  prtanäj-  ,in  den  Kampf ziehend',  jedoch
```


## [2026-09-05T20:36:38.710Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN chist/xist ===\"; grep -n -i \"hi[sš]t\\b\\|Ziegel\\|Speer\" HRN.txt | head -25; echo; echo \"=== HUB ===\"; grep -n -i \"Ziegel\\|isti\\b\" HUB.txt | head -15; echo; echo \"=== FSF خشت ===\"; grep -n \"خشت\" FSF_pages.txt | head -10; echo; echo \"=== CHEUNG ars ===\"; grep -n \"aršti\\|\\*Hars\\|ṛṣṭi\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T20:36:38.799Z] TOOL RESULT

```
=== HRN chist/xist ===
2518:246. bihiSt^ behist ^Paradies'.
2519:(äw, mhista- 'bester; phlv. vahist; ai. väsistha-.
2520:LW. kurd. behist.
2521:Die Aussprache behist ist die ursprüngliche ; in bihist
4431:488. x^Ht 'Ziegel, Backstein'.
4432:aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
5197:phlv. döc *Speer (Dat. d. 21, 8), phlv. pjiz. dö/tav,
5712:zehistän 'Fehlgeburt, Placenta' (AM.), jüd.-pers. TIM
6044:686. MobTti, zöpm-), zöpin 'kurzer Speer (in Gelän bezw.
7197:aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
8687:999. mih gross*, mehist ^), mihtnj mihter.
8692:mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
10118:23. arst 'Speer, Lanze (vd. 14 (34)).
10119:ap. aw. arsti' 'Speer, Lanze*; ai. f^i- *Speer.
10246:Hekim Nizäri QuhistänT.
14941:paHistäna- 158.

=== HUB ===
1938:488. Lies afgh. LW. xa^ta 'Ziegel*.
9512:aresa-, skr. rksa-; xist 'Ziegel', phi. oHst = zd.istya-; xism,

=== FSF خشت ===
3943:                                                ‫سر انجام خشتست بالین تو‬
6200:  ‫‪۶۲۲۳۰۷۸۱‬‬                                          ‫نه خشت و نه آب و نه دیوار گر‪.‬‬
8359:                                                    ‫خشت زیر سر و برتارک هفت اختر پای‬
10400:‫خشت و کتاب» (رشیدی)‪« ,‬پهلوی هم‬                      ‫به خرسندی اگزرد خود بشکریم‬
10460:                           ‫خشت (بازیر اول)‬                      ‫چو خستو نیاید میانش به از‬
10472:‫به آورد خشت افگند بردو میل‬                        ‫اگر کشته گر خحستةً تير بود‬
12735:                                                           ‫ونه آ‬‫یو‬‫دخشت‬‫نه‬
14450:  ‫گلش مشک‌سارابد و زر خشت‬                       ‫نظایر آن به‌هیچو جه در زبان فارسی سابقه‬
17517:           ‫شکاف تراک (لغت فصرحس»‬                   ‫گچ و خشت و سنگ گران آورید‬
17590: ‫سبک خشت را کالبد ساختند‬                                                     ‫(مسعود ‪:)۸۱۱‬‬

=== CHEUNG ars ===
55458:*Hars
```


## [2026-09-05T20:36:40.385Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"nleaves\",len(leaves))\nfor p in (250,254):\n    n=p//2+15\n    print(\"==== printed p\",p,\"-> leaf\",n,\"====\")\n    print(leaves[n][:2500])\nEOF"
}
```


### [2026-09-05T20:36:42.353Z] TOOL RESULT

```
nleaves 858
==== printed p 250 -> leaf 140 ====
ng (dhuriə, a zero-formula to dhuer-, dhuor-, dhur- ‘door’. etc.) WP I, 870 Gk. thairós singularized: ‘hinge of door
‘place free from snow’; er-aebern ‘to thaw’; Upper G āper, āber ‘free from snow’ ed- (ëdå, om, io, iom, is) ‘food, bait’. Cf.
` edmi. WP I, 118
Skt. adyam; Oss. ad, adä; Hitt. écan ‘food’; Lat. -edia in inedia “lack of food'; OE æt; MHG às; ON át, cpds: -æti; OCS. jadi, jaZda; R jéda; Li. édis, gs ēdžio; cf. also edZios, pl. ‘manger’; Latv. éda. Cf. edrà, etc. Extns. in Lat. edax ‘voracious’; Ukr. idkyj ‘caustic’; cf. W iddas ‘pungent’
edolis, os, om “edible; food". WP I, 118. Cf. éd-, edmi, etc. Lat. edulis; OE etol; ON etall; Blg. jàlo, jàdalo ‘food’; Cz. jedlý “edible”; jídlo ‘food’; Li. ēda- las ‘pigfood, swill’
(edior ‘food’. See éd-, ëdra, etc. Gk. eidar “food?
edmi, (edó), 3s esti *eat. WP I, 118 Skt. ádmi; Av. ad-; Hitt. écmi; Hom. édo; Lat. edo, 3s ést; Osc. edum, mi Ir. cf. íd-ighim ('consume', fr. *éd-a8-); Go. itan; OE etan;
231
OHG e33an, ezan; G essen, beside aassen 'de- vour’; OCS jami, inf. jasti; R jém, jësti; OLi. edmi, Li. ēdu, inf. ēsti; Latv. edu, est
édmn-, édn- “food; tooth, set of teeth’. Cf. WP I, 118 and see édmi Skt. ádman 'food'; Arm. atamn, gs atman ‘tooth’; Hitt. cf. ecan ‘food’; Gk. edanós "eat: able’; Lat. (?) cf. cena (*meal', if for *ko-eds- nā); MIr. edam ‘eating; MHG ézzen “food, meal; ON átan, id. Li. edmens, usu. pl. ēd- menys “set of teeth’; Latv. cf. esma “bait
ednt-, edont- (odont-) 'eating-; tooth’. Cf. ed-, etc. and edonts below Skt. adat, pres. pt.; cf. a-dantah ‘toothless; leech’; Gk. odoüs; gs odóntos; Ion. odón; Lat. dens; Go. tunpus, -tundi (*dnt-) beside OHG zand, OE top, ON tonn, etc.; Olr. dét *tooth; food"; Li. &dantis, adj. “eating; corrosive’ be- side dantis, m. “tooth?
edó(n) «devourer, consumer’. Cf. éd-, etc. Lat. edo ‘glutton’; Li. eduonis, gs -ies 'bone- caries’; ON cf. aeta ‘eater’
edonts (edont, edon), act. pt. ‘eating’. See ednt- Skt. adan, adanti, adát; Hitt. adanc, neut. adan; Gk. (sole instance) édontes, pl.; Lat. edens; Go. itand-s, -1, -0; OHG ëzzanti; OCz. jéda, jédüci, jéda; Li. édas, édanti, Eda (adver- bial: édant)
édó(n) (édon-, édios) ‘eater’. Cf. édmi, etc. Gk. cf. anth-édón, -édónos (“bee”, lit. flower- eater"); Go. uz-eta, wm. ‘crib’; OE -æta in self- ? *cannibal; ON aeta; æti; (R cf. jédkij *mor- dant'; Li. edikas ‘big eater); Li. eduonis, gs i&s, m. beside edéjas “big eater; OCS cf. medv- GO (bear, lit. 'honey-eater)
edra, is “food? Hitt. ēdri; Li. edrà, id.
eds-, 
==== printed p 254 -> leaf 142 ====
mb. eikvas-atis (in phr. ahtis-per.. . ‘for de- parted souls'?); Li. cf. eikvoti ‘squander’ be- side eiklüs ‘nimble’. (Isophonic are Lat. 1co, ere; OLat. eic- "strike
eila, io ‘going, gait;, gang, troop; file, line’. Cf. ei-mi. Cf. WP I, 70, 104 Skt. ela “sport beside Irah, -am ‘wind’; ilā 'flow"; ir-te, mp. ‘go’ (ei-: i-); Gk. ale ile “gang, troop; W wyl “flow, gush’; OHG ia ‘haste’; Du. ijl, id.; Sw. il ‘gust’; Li. eilé line, row? be- side eilà, eilià, id. and (o-gde) ailà "row. rank’; Latv. iela ‘street beside (o-gde) aile ‘row, path, opening”. (Isophonic forms are Lat. ilia, -ium ‘waistline’; Ir. alle gs éille ‘thong’; Latv. iela (2) “peg, prop, stick’. Lit. dine" ?)
eilus, os (11-?) “mud, clay” Oss. ilà, id.; Gk. eilús, (os id.; cf. arg-ilos ‘white clay; Cz. jíl, gs -u ‘clay’; R il ‘mud’
eimi (eio) ‘go’. WP I, 102. (Plural forms: i-) Skt. émi, 1 pl. imáh; Av. aei(mi); OPer. ay-; Hitt. cf. ca-imi, cpd.; Myc. ijon, pr. pt. “going; Hom. eimi, pl. men: pr. subj. eið, íð; EMAlb. íhem (-h- due to hiatus, or fr. *-sK-); Lat. eo, īre; Pael. cf. eite! *go!; Umb. etu, 3s. jussive; W âf “shall go? beside awyf “may I go’; Br. an, 1s. pr.; inn, 1sg. fut.; EMLi. eimi; Latv. eimu, iemu, eju, id. Cf. Latv. eja ‘path’ & Li. eimé! let's go!
(eimos 'going'. Cf. oimos and see eismn- be- low) Skt. (ambig.) éman ‘path, course’; Ir. éimh ‘swift; ON ima, f. ‘strife
-einå ‘product of . . ?. Cf. -inā Lat. porc-ina ‘pork’; Cz. kon-ina, etc. (“horse- meat”, etc.); Slovene, cf. prasét-ina ‘pork’; Li. parš-iena, id.
eiså, io (ois-) ‘go, dash, impetus, outburst’. Cf. eismn-, oisá, eimi Skt. (ambig.) éSa ‘search; desire’; Lat. (ambig.) ira ‘anger’; Icel. cf. írafár *overhaste'; Li. cf. eislùs ‘going’; eisena ‘gait’
235
eisio ‘shall go’. Cf. eimi Skt. esyàmi; Gk. eið (pres. subj.); Li. eisu, ei- siu; Latv. iešu (The Li. form eisu is that of the Bible translation)
eisios (eiso-, eito-) (a cpd. pronoun) Skt. cf. esab, -a, neut. etat ‘this’; Osc. eíseís “his; etus’; eise (loc. sg. ‘in him, her, it"); Umb. erer, m., erar, f. “his, her
eisk- (eisK-) ‘request, demand, search". WP I, 12. Cf. aisK- Umb. cf. eiscurent “they shall demand": W wysg (adj. ‘proceeding’; s. ‘procedure, trend"); OSC isto, iskati & isko, ati zeck: Li. ieškau, ieškoti, id.
eismn- (eimn-) “going, movement. Cf. ei-mi and cpds., oi-m- Skt. cf. éman “path, course Ir. éimh, adj. ‘swift; ON ima ‘conflict, strife’; Li. eismas ‘going, traffic, movement; (o-gde in Hom. oima 'dash"). Variants: Li. eisena ‘gait’; W wys (‘mobilit
```


## [2026-09-05T20:36:55.790Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10112,10130p' HRN.txt; echo \"-----488-----\"; sed -n '4425,4445p' HRN.txt; echo \"--- leaf of 23 ---\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"23. arst 'Speer\",\"488. x^Ht 'Ziegel\"]:\n    i=t.find(pat); print(pat,\"leaf\",t.count('\\f',0,i)+1, \"printed p ~\", t.count('\\f',0,i)+1-21)\nEOF"
}
```


## [2026-09-05T20:36:56.761Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (150,151,152,153):\n    print(\"==== leaf\",n,\"====\")\n    print(leaves[n][:2200])\nEOF"
}
```


### [2026-09-05T20:36:57.497Z] TOOL RESULT

```
47), Geldner, KZ. 30, 520 No. 14.
21. äpus 'schwanger, vergl. unter np. äbisten (oben
No. 5).
22. armest 'abgeschlossen, hilflos' (West, Sacr. B. of the
East, Vol. XXIV, 42 Note 2).
aw. armaesta^ (vom Wasser).
23. arst 'Speer, Lanze (vd. 14 (34)).
ap. aw. arsti' 'Speer, Lanze*; ai. f^i- *Speer.
24. artestär 'Krieger, artestärän salär (Karnäm. S. 67
Note 3), adQaöxadaoavoahiVTjq (Proc. Pers. 1, 6, 11).
aw. rai^aestar- 'Krieger ; ai. rathesthär-.
Np. ert^dar (statt erdesdär) wird im FR und FJ
einmal aus dem pärsischen Dichter Behräm Zerätust
belegt.
25. arü8 'weiss, päz. alös (Bund., Men., AV.).
aw. aurvsa- 'weiss' ') ; ai. arusd- 'weiss, glänzend',
oss. d. orSj vors, t. Urs 'weiss' (255) ist unsicher.
26. arvand 'stark, schnell' in Arvandasp, vergl. arvand
'Vorzug' (Bund.).
-----488-----
Käs. /asrii',
ai. <;DarrU' 'Schwiegermutter'; arm. akesnr (H. No. 253) ;
lat. socru-s; ksl. soekry.
kuvd. /ost, /esü, yasrü 'Schwiegermutter; af/. ;K''ö4fa ;
bei. V((8sö, vasl, vase (406) ; wa;^. /as, si/n. /as, sar. /,e/.
Vergl. ytisur (No. 486).
488. x^Ht 'Ziegel, Backstein'.
aw. istya- 'Ziegel, Backstein' ; phlv. /ist ; skr. isfakOr-
'Backstein'.
afy. LW. /ßta; bei. ist (168).
489. ^usk 'trocken', /ös« ') 'Ähre', yös, yöslden, yösdniden
(AM. 236 Zeile 3 v. u.), /mkUm,
Kä§. tisk (jendn, husküdSn.
ap. Msia- trocken'; aw. huskd- 'trocken*, aflluiosemnu'
'nicht vertrocknend'; phlv. /<*^Ä;, /usklh^ /ösTnUän
(Bund.)-); ;rösaA; 'Ähre' (Bund.); ai. güska-, güsyati,
skr. gösa-.
kurd. LW. hüsk; afy. vud; oss. /tisk, ba/ussin (311
und Seite 141); bei. husay 'trocknen, austrocknen (160)
(LW?); wa/. vesk,
np, /uskar {/usk ärd, Vullers, 756, vergl. dial. ör,
--- leaf of 23 ---
23. arst 'Speer leaf 288 printed p ~ 267
488. x^Ht 'Ziegel leaf 130 printed p ~ 109
```


### [2026-09-05T20:37:35.096Z] TOOL RESULT

```
==== leaf 150 ====
ig. For VW: LEDT yärk is: Arm. erg ‘song’. Blg. lacks the usual me- tathesis)
erm-, ermen- (ormen-) ‘enormous, swollen’. Cf. ormn- Sk. arman, armana, n. armas, m. ‘swelling of the eyes’; Hitt. armas, armannis (queried: ‘full moon); armaniya(mi) ‘swell; be pre- gnant; Arm. armanam "be astonished’; Ger- manic proper n. Ermeni-ricus: OE Eormenric; OE eormen-, cpds. ‘huge’; ON jormun.-, id.; W (ambig.) erf ‘dashing; dash’; (o-gde in) Gk. órmenos ‘high’, and in OCS ramínü *dash- ing, violent; Cz. cf. ná-ramny *wonderful; Li. efmas, m. ‘monster’; Latv. erms, id.
249
ersKó ‘go to, reach’. Cf. erso (1) Skt. cf. réchami ‘go’; Per. rasam, 1dan “arrive? (LW in Romani: aresav reach": Hitt. arski(mi) *reach'
ersð (1) ‘go, glide, wander, creep, dawdle’. WP I, 150 Skt. arsami; Arm. (ambig.) eram (OO) ‘crawl’. Cf. serp-); Hitt. arsa(mi) “flow; Gk. érro ‘trudge, wander, limp, flag; Lat. erro, åre ‘wander, err; MHG irren, MLG érren 'con- fuse; err’; Blg. (ambig.) réxam se ‘wander’
ersó (2) ‘rave, rage’. Cf. irs- Skt. (ambig.) irasyàmi; Arm. (?) eram ‘boi; eřantn ‘zeal’. Cf. ieso; Go. cf. aírzeis “angry”; OS irri; OE iersian ‘rage’ beside ierre ‘angry’; Li. cf. erzu, eti ‘growl’; érzinti “irritate? (con- sonantism unusual) Extns. in Alb. jermé *dazed' and ON jarmr ‘scream’
es- (radical "bel See following entries
es- (variant of root: es-) Skt. ase “sit, rest, remain’; Gk. h&mai "ert": Hitt. cf. às(mi), v. remain’. Vocalism?)
-es- alternating with n.a.sg. -os, pl. -eso, a neuter type of "universal" aspect: see menos, 2enos, nebhos, quelos, ieuos, etc.
esános (sanos) “good, due, right, proper, Cf. sános, esnt-; esont-, snt-, sont- (all with radical: *es-, s- "be Hitt. cf. asanc, neut. asan 'true'; Lat. sanus (* good; sound"), cf. san-cio, -cire (*establish, enact’. Cf. cio, cire ‘cal’ and sense of G gut-heissen); cf. also sanates (‘reinstated rebels’, fr. san- *good" — Fest.); W iawn (just, right, proper’, fr. esàn-); Br. écen, d: OHG suona “judgment; reconciliation; suonen ‘judge’; cf. G Sübne and ver-sóhnen; OS sonian, id.; OCS sanü ‘dignity’ beside sanitü (holy: OS gi-sonid). (For OE sona *forth- with’: W hawn ‘brisk’ see són-)
ésom (ésiom), imperf. lsg. of root es-, q.v. Cf. WP 
==== leaf 151 ====
); Lat. esca; Li. eskà ‘appetite’; esküs ‘gluttonous’
esKo (es-sKo) (inceptive-progressive) “be, become’. Cf. es-, etc. Pali aččhāmi '/remain'; Romani achav, id.; Hitt. éskami, id.; (Arm. icem 'shall, may be is more prob. fr. *esiem, see SEM: AHG, p. 48); Hom. cf. éskon ‘I became’; OLat. escit, 3s. *will be'. Fest.). Cf. the inchoatives in Gk. -sko, Lat. -escoó, Alb. -h; Li. at. and in OCS rosto (CI grow’, fr. *ordhsKo)
esmei (with variants: esmu, esmou, etc.), dat. sg. of pers. pron. ‘to him, it Skt. asmai, asmai; Umbr. esmei; Go. cf. imma; OHG cf. emu, emo; OCS jemu; Li. jam. Cf. is
esmi (es-si, es-ti) am, etc. WP I, 160 & Cf. esti as sep. entry Skt. ásmi; Av. ahmi; OPer. amiy; Per. am; Hitt. esmi; Arm. em; Gk. eimí; Dor. Aeol. emm: Alb. jam; Lat. sum; Osc. súm; MIr. isam; W wyf; Br un; Go. im; OE eom; ON em; OSw. æm; OCS jesmi; OCz. jsem; OLI. esmi; Latv. esmu
esmi (eso'i, ésoi) “sil. Cf. esmi. WP II, 486 Skt. ase; Av. ah-; Hitt. esmi, àsmi ‘sit, remain’; cf. estari, 2s.: esari, 3s. esa ‘sit; HHitt. cf.
251
3s. (queried) asta ‘sits’; Gk. inf. hesmai, hémai beside káth-emai (‘to sit. Infl. of Seed. ?); Alb. jehem ‘remain’;
esmn- (esmen, esmis, io, esn-) “being; sub- stance'. (Formative suffix also in Gk. & Lat.) Arm. (ambig.) iran, rant (body, trunk’. Cf. étür, etor-); Hom., Gk. -émen, emp (inf. suf- fix); Boeot. eimen, inf. ‘to be’; Lat. cf. -ena, in cat-, hab-, ar- (has-), -ena; Norw. emne, Sw. ämne, wn (element, subject, matter, sub- stance’. Linked semantically w. ON efni, id. but cf. OE stemn, stefn); Icel. cf. ess ('ele- ment in phr. i essinu sínu “in his element); OCS sémí ‘person’ beside Blg. esè, n. ('in- heritence', fr. *esn); Li. esmé “being, essence’ beside asmuó, -efis ‘person’; Latv. esme "be ing, essence’. (The same root may be embed- ded in OHG ernust-, OE eornoste 'earnest, cf. R estestvennyj. For OE eormen-, ON jormun-, see erm-, ermen-)
esmn- (ésmà, ésen-, eso(n)) ‘eating; pasture’. Cf. ésio, eskà i OE sen, æsa, wm. 'titbit; pasture’ (-ēsn- in ef-esn, id.), cf. also essian ‘glut, sate’? and G Asung; Li. ésena ‘gluttony’; Latv. esma "bat",
esmnos (esimnos, esniu-) “fine, thin”. Variant of emnos (?), q. v. (A Skt. form of type *asanáh, Prakrit
==== leaf 152 ====
ynde, "DC
esnt- (esont-) (2) ‘guilty; guilt, sin’. Exten- sion of (1) (?) Lat. sons; OHG suntea; OS sundja; OE synn; ON synd
eent (senti, snti, esonti, sonti), 3pl. "are, Cf. es- "bei Skt. santi; Av. həñtī; Per. and; Gk. eisí, éāsi, Dor. entí; Mycenaean ee(n)si; Arm. en; Alb. jané; Hitt. asanci; Lat. sunt; Osc. Umb. sent; OBr. hint, int; Br. int; W ynt, yd-ynt (*id- senti); Go. sind; OHG sint; OCS sotí; OCz. jsú
esntos, -esə essential, substance’; pl. “tackle”, etc. Cf. esnt- (1) Gk. éntea, npl.; Lat. cf. essentia; Ir. éide, éideadh ‘armour, equipment'; Blg. esè, pl. esëta ‘inheritance’
esó (potential) ‘may, shall be’. See es-, etc. Skt. ásam; Gk. éð; Lat. ero
esont-, see esnt- (1)
ésos HHitt. asas "seat": Hitt. asas-, v. ‘set, seat'; Skt. asáh, s.
és-romos (eromos) 'resting-place, refuge’. See és-, ràmos Av. airimom ‘solitude’; Gk. éremía "rest, eréma ‘quietly’. (A variant form occurs in Skt. a$ramah, -am ^hermitage")
esros “good, fine, noble, grand'. Cf. es-mi, esulos, esus Lat. *ebrus (in in-ebrae aves 'inauspicious birds”); Ir. earr ‘noble, grand"
essi (esi) "art. 2sg. of es-mi, q.v. WP I, 160 Skt. asi; Av. ahi; Per. 1; Arm. es; Hom. E Dor. essí; Alb. je; OLat. ess; Lat. es; Go. is; ON er-t; OCS jesi; OLi. esi; Latv. esi
est- (1) (stis, estus) ‘being; creature’. Cf. es-, etc. ` Skt. cf. astam “home; setting’; astu-vid ‘aware’; Av. stis ‘creature’, astus ‘body’; Oss. 1s, D. jes “property”; Lat. cf. -stia (in be-stia, if for *guer-stiio); cf. Skt. sv-astih ‘wellbeing’ (*su-
253
est-)
est- (2) (theme of *ed- + *-t-, see ed-mi) “eat, consume” Lat. (Plaut.) essi ‘I ate’; estur “is eaten’; OW yssu ‘to consume’; Blg. jàstije “food, dish’ (*-ē-)
est- (3) in a redup. formula *estest- (ístëst-) “true, right, alike’. Cf. 1st-; esəst-, etc. and radical: es- *be' W eisoes, eiswys, eisys "likewise; OCS estistvije “nature? beside istü ‘true, the same, chief, natural; Latv. 1sts ‘true, genuine”
esti ‘is’, 3sg of es-mi, q.v. WP I, 160 Skt. ásti; Av. asti; Per. ast; Oss. 1s, jes beside is ‘there is; Tokh. B ste; Arm. e (archaic: iK); Hitt. esci; HHitt. asta; Gk. esti; Alb. asht, është; Lat. Umb. Osc. est (Osc. also íst); Sic. esti; Olr. is; OBr. iss, is; OW iss; W ys; Cor. es
==== leaf 153 ====

15
20
25
30
35
40
45
254
so-, px. id.; Gaul. cf. Essui, pl. (a Celtic tribe of Brittany); OBr. eu- (in eu-les "good. voice); W hy- px; OCS omg ‘desirous’; OCz. cf. ochevny ‘wanton’
esus (esos, esi-) (2) “animal, breath, being”. Cf. es-mi, etc. Skt. ásuh (Ð “breath, life; Av. àhus (2) ‘world, place’; cf. áha ‘mind’; áhva “self, being’; Per. ahü deer": Arm. cf. ir, -i, -av, a-st. ‘thing, fact’; irav ‘rightly’; iravi, adj. ‘true’ from a type *esiiə)
esus (és-) (3) “god, demon’. Cf. esulos, etc. Skt. ásuh, id.; Av. áhus ‘lord’; Hitt. hassus ‘king’ beside eshas (‘master’. The u-st. with umlaut is functional; the a-st., IE o-st. is non- functional); Lat. erus, herus ‘master’; era, OLat. esa ‘mistress’; Gaul. Esus ‘God’; ON ass, i-st. “heathen god'
eteros basic form of a cpd. pron. w. the comparative extn. -teros. Cf. an-teros, iotero-, (ieter-), Kitero-, quetero-, etc. WP I, 99 Myc. cf. atero-weto (‘next year’. Ambig. ? *antero-); Gk. háteros, beside héteros; Alb. dial. jetër, jatér “other”; Umb. etram, f. sg. id.; OCH jeterü “a certain; some, any”
etesé (sentence particle) *so, well, but, then”, etc. Cf. iot-se, et-se
eti, eto, et “and, but, yet’. Cf. ati, atand WP I, 43. See et-se Gk. éti; cf. also ex-éti (cj. 'since"); Phryg. eti- (px); Alb. e; Lat. Umb. Pael. Fal. et; Olr. eti, eti-c; Mär eta ‘so; OW cf. etaw, eton; W eto ‘yet; Go. ib; OHG ith; ON eða, eðr; Blg.Srb. eto ‘since, as’; Li. ét, ét "but
etmn- ‘breath’. WP I, 118. See next Skt. atman, atmanah; OHG àdum (cf. atam, id.); OS athum; OFris. éthma; MHG àtem, MLG adem: Du. adem; OE &pm, id. (see FK: EWDS 17: Atem, Odem). (Consonantism obscure in Gmc.)
etór (etrom, Str) “internal organ’. WP I, 117 (Arm. irank “body, trunk’ is ambig.); Gk. étor “heart”; étron ‘belly’; OHG adara ('vein'; pl. tintestines); MHG àder (as OHG, also = ‘sinew, nerve); OE ædre ‘veim’; pl. ‘kidneys’; ON cf. æðr, as. & ds æði ‘vein’. (OCS jadro “bosom? indicates a variant consonant, cf.
255
Cz. ňadra ‘bosom’, fr. a type *en-endhro-)
et-se (et-sié-, eti-siet, e-te-siet) (particle or conj.) ‘so, be-it'. Cf. eti, siem (siet) Vedic átha; Skt. átha; Av. áo, a Arm. ete, te; Lat. etsi; cf. also Gk. éti, cj. ‘yet
eugh- (ügh-) (rage, curse, swear
```


## [2026-09-05T20:37:53.012Z] TOOL CALL #40: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T20:37:53.018Z] TOOL RESULT

```


```


## [2026-09-05T20:37:57.188Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D8%AA",
 "prompt": "Give the full Persian entry: all etymologies and senses for خشت (xešt), especially any sense 'javelin/short spear' and its etymology (Middle Persian, Avestan, Proto-Iranian forms), and the 'brick' etymology. Quote the etymology sections verbatim."
}
```


## [2026-09-05T20:37:59.073Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁es-",
 "prompt": "Summarize the reconstruction page for the PIE root 'to be': the exact form, meaning, and the descendant forms in Avestan, Old Persian, Sanskrit, Latin, Proto-Germanic. Quote the key lines."
}
```


### [2026-09-05T20:38:04.834Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁es- ("to be")

## Reconstruction Details

**Exact Form:** *h₁es- (imperfective)

**Meaning:** "to be"

**Etymology Note:** The page indicates this root is "Probably related to *h₁eh₁s- ('to sit')" and notes that the root may have originally meant "to sit" before acquiring the meaning "to be."

## Key Quote on Semantic Development

"the root *h₁es- may have originally meant 'to sit' before eventually coming to mean 'to be.'"

## Documented Descendants

The page explicitly lists only one language family:

**Proto-Indo-Iranian:** *Has-

## Notable Limitation

Unfortunately, the Wiktionary page does not provide specific descendant forms in Avestan, Old Persian, Sanskrit, Latin, or Proto-Germanic. It references these languages indirectly (Proto-Indo-Iranian descendants would eventually develop into Avestan and Old Persian forms), but the actual attested reflexes in those individual languages are not documented on this particular reconstruction page.
```


### [2026-09-05T20:38:25.855Z] TOOL RESULT

```
# Persian Entry for خشت (xešt)

## Etymology 1 (Brick)

"From Middle Persian [script needed] (hšt' /⁠xišt⁠/, "brick"), from Old Persian 𐎡𐏁𐎫𐎡 (i-š-t-i /⁠išti-⁠/, "sun-dried brick")"

This etymology traces the word back through Middle Persian to Old Persian, with cognates in Avestan (ištiia, išti, zəmōištuua), Sanskrit (iṣṭakā), and other Indo-European languages.

### Senses under Etymology 1:
1. Adobe, sun-dried brick
2. Tile; slab
3. A loaf baked for the soul of a deceased person (uncommon)
4. In Zoroastrianism, the twelfth chapter of the Zend

## Etymology 2 (Javelin/Weapon)

"See Old Armenian ašteay"

This brief etymology references Old Armenian sources without providing detailed Middle Persian or Avestan reconstructions.

### Sense under Etymology 2:
1. Javelin, dart, spear, halberd, or poleaxe (archaic)

The document provides rich etymological detail only for the "brick" sense, leaving the weapon sense's deeper linguistic history less developed.
```


## [2026-09-05T20:38:52.987Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D5%A1%D5%B7%D5%BF%D5%A5%D5%A1%D5%B5",
 "prompt": "Quote the Old Armenian entry ašteay: its meaning, etymology (Iranian source, Avestan aršti-, Old Persian), and any mention of Persian خشت (xešt)."
}
```


## [2026-09-05T20:38:53.756Z] TOOL CALL #44: WebSearch

```json
{
 "query": "Persian خشت \"javelin\" etymology Avestan aršti- Hasandust ریشه‌شناسی خشت نیزه"
}
```


### [2026-09-05T20:38:59.000Z] TOOL RESULT

```
# Old Armenian ašteay Entry

**Meaning:** The word refers to a "short javelin for throwing from a distance, a dart."

**Etymology:** The entry states it is "an Iranian borrowing" with comparisons to Old Persian *a-r-š-t-i-š* ("spear"), Avestan *aršti* ("spear, lance"), and Sanskrit *ṛṣṭí* ("spear, lance"). 

**Persian خشت (xešt):** The dictionary notes this Persian term means "javelin, dart, spear" as a more distant cognate within the same etymological family.

The entry demonstrates how this Armenian weapon term derives from ancient Indo-Iranian language roots, with the semantic field consistently involving projectile weapons across multiple language families.
```


### [2026-09-05T20:39:04.078Z] TOOL RESULT

```
Web search results for query: "Persian خشت "javelin" etymology Avestan aršti- Hasandust ریشه‌شناسی خشت نیزه"

Links: [{"title":"աշտեայ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D5%A1%D5%B7%D5%BF%D5%A5%D5%A1%D5%B5"},{"title":"SPEAR - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/spear-eastern-iran/"},{"title":"Explore - Encyclopaedia Iranica","url":"https://iranicaonline.org/explore/?wpv_paged=547&wpv_view_count=903"},{"title":"Arshtat","url":"https://en.wikipedia.org/wiki/Arshtat"},{"title":"Persian-Etymology-Charts.pdf","url":"https://parsianjoman.org/wp-content/uploads/2022/12/Persian-Etymology-Charts.pdf"},{"title":"𐎠𐎼𐏁𐎫𐎡𐎣 - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%81%F0%90%8E%AB%F0%90%8E%A1%F0%90%8E%A3"},{"title":"PERSONAL NAMES, IRANIAN ii. AVESTAN NAMES - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/personal-names-iranian-ii-avestan/"},{"title":"Arshavir","url":"https://en.wikipedia.org/wiki/Arshavir"},{"title":"Ashtad Yasht","url":"https://en.wikipedia.org/wiki/Ashtad_Yasht"},{"title":"Avestan alphabet","url":"https://en.wikipedia.org/wiki/Avestan_alphabet"}]

Based on the search results, I found relevant information about the etymology of Persian خشت (xešt, meaning "javelin" or "dart"):

The Persian word خشت (xešt, "javelin, dart, spear") is compared with Old Persian 𐎠𐎼𐏁𐎫𐎡𐏁 (a-r-š-t-i-š, "spear"), Avestan 𐬀𐬭𐬱𐬙𐬌 (aršti, "spear, lance"), and Sanskrit ऋष्टि (ṛṣṭí, "spear, lance"). 

The Old Persian used the same word aršti- for denoting both a spear and a javelin. This word derives from Proto-Indo-Iranian *Hr̥štikás, from *Hr̥štíš ("spear"), from Proto-Indo-European *h₁r̥stís.

The search results confirm the relationship between the Persian خشت and Avestan aršti-, supporting their common Indo-European etymological origin related to spear-like weapons. However, I could not find specific information about "Hasandust ریشه‌شناسی" in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:39:11.036Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%81%F0%90%8E%AB%F0%90%8E%A1%F0%90%8E%A3",
 "prompt": "Quote the Old Persian entry āršṭika-: meaning, etymology (from aršti- 'spear' + -ka-, Proto-Indo-Iranian, PIE form), attestation (DNb), and any mention of uvāršṭika-."
}
```


## [2026-09-05T20:39:12.055Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/essence",
 "prompt": "Quote the etymology of 'essence', and also anything on 'proud', 'entity', 'interest', 'absent', 'present' if present on the page. Focus on essence: Old French, Latin essentia, esse."
}
```


### [2026-09-05T20:39:15.837Z] TOOL RESULT

```
# Old Persian Entry: āršṭika-

**Meaning:** "spearman"

**Etymology:** Derived from Proto-Indo-Iranian *Hr̥štikás, which comes from *Hr̥štíš ("spear"), ultimately from Proto-Indo-European *h₁r̥stís. The formation involves the root aršti- plus the diminutive or agent suffix -ka-.

**Attestation:** The term appears in inscription DNb, line 44, where it occurs in the phrase: "As a spearman, I am a good spearman, on horseback."

**Related term:** The derived form uvāršṭika- (u-v-a-r-š-t-i-k) means "good spearman," attested in the same inscription.
```


### [2026-09-05T20:39:19.503Z] TOOL RESULT

```
# Etymology of "Essence"

**Main Entry:**
The word "essence" entered English in the late 14c. from Latin *essentia*, meaning "being, essence." This Latin term was formed as an abstract noun from *essent-*, the present participle stem of *esse* ("to be"), which traces back to the PIE root *\*es-* meaning "to be."

**Key Quote:**
"in philosophy, 'true being, substance,' as distinguished from accidental qualities or appearances, from Latin *essentia*"

**Semantic Evolution:**
Initially applied to theological concepts regarding the Trinity's substance, the word broadened by the 1650s to mean "basic element of anything." By around 1600, it acquired the sense of "ingredient which gives something its particular character," especially regarding distilled plant oils, eventually yielding the modern meaning of fragrance or perfume.

---

## Related Terms (from page)

The page mentions these words derive from the same *\*es-* root but provides minimal detail beyond listing them: **proud**, **entity**, **interest**, **absent**, and **present**. No substantial etymological information for these terms appears in the provided content.
```


## [2026-09-05T20:39:27.188Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && head -c 800 MON_part1.txt && echo \"---- pagecount ----\" && python3 -c \"\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('leaves',t.count(chr(12))+1)\nt2=open('MON_part2.txt',encoding='utf-8',errors='replace').read()\nprint('leaves2',t2.count(chr(12))+1)\n\""
}
```


## [2026-09-05T20:39:28.064Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"استن\\b\" MON_part1.txt | head -10; echo \"=== اسانس ===\"; grep -n \"اسانس\" MON_part1.txt | head -5"
}
```


### [2026-09-05T20:39:29.171Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نامه مدش نامع 

مه مر وه ود 

3 ور 133131313 


هم مشب جج جب بیج چم مدوجو 
چم وم 
جر 


درل ولو ونر نو تلا رت 
11 


مج جرج جر یی میج 6و یوج هو هجوج وی یویر جر دم مور و 555 
و ده ها وی مزا موی ماما میو و موه ومد موه اش اما موم م میا شا ولمم 


معین, محمد» ۱۳۵۰۰۱۲۹۱ 
فرهنگ معین / محمد معین. -- تهران: آدنا: کتا�---- pagecount ----
leaves 1
leaves2 1
```


### [2026-09-05T20:39:29.238Z] TOOL RESULT

```
697:راستن» | -رهیدن» آ -وردن؛ ۲ -شسودن. 
1313:و دهان بکار برند. وضوء دست‌نماز. استنجا 
2550:است در مقابل «یبراستن» چنانکه بزک کردن 
2559:جهره «آراستن» است و زدن شاخه‌ها و 
2560:برگ‌های زبادی درخت «بیراستن». نطم 
2570:کیتی بباراستند (فردوسی). 
2572:اراسته: (6-)318512 (امق. آراستن) مرین» 
2632:آراییدن: «دل]- 273 [- آراستن ] (مصم.) 
2634:آراینده» آراییده) آراستن. 
3499:کردن» پبراستن چرم» دیاغت. 
=== اسانس ===
3090:اسانسور: 0 دستگاهی که به 
3093:به زمین فرود آیند؛ بالارو» اسانسر. 
10896:اسانس: دعقم (.) جوهر گل‌ها و گٌیاهان 
25629:معمولی (اسانس نفت) اشتباه کرد. این بنزین 
25643:مانند اسانس نفت بسیار آتشگیر ولی مانند
```


## [2026-09-05T20:39:36.154Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10890,10900p' MON_part1.txt; echo \"=== استن headword ===\"; grep -n \"^استن\\|استن:\\|هستن\" MON_part1.txt | head -10; echo \"=== است ۱ ===\"; grep -n \"است: \\|است ۱\" MON_part1.txt | head -10"
}
```


### [2026-09-05T20:39:36.255Z] TOOL RESULT

```
فروتران و برتران. سرین‌های مردم» کفل‌ها. 
اسافل اعضا: اندام‌های زیرین» اعضای 
فرودین» عضوهای پایینی بدن» عضوهای 
بدن از سرین به پایین. اسافل بدن: عضوهای 
زبرین ندن» اندام‌های پایینی تن. 

اسانس: دعقم (.) جوهر گل‌ها و گٌیاهان 
که بصورت عطر استخراج شو د. 

اسپ: ند [- اسپ] (.) (جاذ.) بستانداری 
از راستهٌ فردسمان جزو تبره سم‌داران که 
=== استن headword ===
4388:۳ ازت‌داری هستند که در نساتات و 
7480:است. (شیم.) تر کیباتی هستند که بدن گیاهان 
7495:نمی‌کند و بطور کلی حاجب ماوراء هستند. 
7523:مستنیر (مستنیره) (فز.): اجسامی هستند که از 
7947:بدنی که مقدمات آن هستند» مقارن و همراه 
8933:دلیل تباهی هستند؛ مقّ. اقبال. 
9447:مخالف تغییر و انقلاب و ترای هستند. 
9654:خود را از کسی خواستن: توقع بیجا از کسی 
10504:هستند. بعضی‌بیرنگ یا سفید و برخی 
11049:نزدیک کوکناریان هستند و اکثراً آن را جزو 
=== است ۱ ===
375:مجلد خواهد بود که بعض آنها به شرح زیر است: 
378:دارا است: 
1430:عبر آب؛ محجرای است: تا ) کذز کاة 
1531:نهانی از کسی گرفته بودن. شب آستن است: 
4245:به قولی بر چهار قسم است: ۱ - حلوق 
5519:آن است: 
5930:آنها از اين قرار است: آب ت ث ج ح خ د ذ 
6256:شمال ابران موجوداست: کل ابر یشم. ( کبا.) 
6884:ستختگو است نس خر عرر کسده.است: 
8202:مامانی» خوب. اخ است: (در زبان کودکان)
```


## [2026-09-05T20:39:42.274Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and لغت‌نامه دهخدا sections for the headword استن — its meaning(s), especially any verb meaning 'to be' (بودن) and the origin tag (e.g. [په.])."
}
```


### [2026-09-05T20:39:49.367Z] TOOL RESULT

```
# استن — Verb Meaning and Etymology

## فرهنگ معین (Mo'in Dictionary)

The entry lists استن with the pronunciation **(اَ س ِ تُ)** and provides two distinct definitions:

1. A chemical meaning: "a colorless, volatile, flammable liquid with an ethereal odor"
2. A structural meaning: "column; pillar"

## لغت‌نامه دهخدا (Dehkhoda Dictionary)

Under the entry **استن [اَ ت َ]**, the dictionary identifies it as **(مص) هستن** — a "hypothetical infinitive" form of the verb "to be," with conjugations: استم، استی، است، استیم، استید، استند

The origin tag **(ع اِ)** indicates this entry carries an "Arabic origin" classification.

The dictionary also notes that alternative forms include: ام، ای، است، ایم، اید، اند, with the past participle appearing as: ستم
```


## [2026-09-05T20:40:05.463Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN essence ===\"; grep -o \"essence, n\\..\\{0,400\\}\" KLN_1966.txt | head -3; echo; echo \"=== KLN swastika ===\"; grep -o \"swastika.\\{0,400\\}\" KLN_1966.txt | head -3; echo; echo \"=== KLN yes ===\"; grep -o \"yes, adv\\..\\{0,350\\}\" KLN_1966.txt | head -3; echo; echo \"=== SKT essence/yes/am ===\"; grep -o \"ESSENCE.\\{0,300\\}\\|YES\\..\\{0,300\\}\\|AM\\..\\{0,300\\}\" SKT.txt | head -6"
}
```


## [2026-09-05T20:40:06.879Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN be ===\"; grep -n \"9\\.91\\|To Be\\|9\\.9 \" SYN.txt | head -10; echo \"=== SYN spear ===\"; grep -n \"20\\.26\\|SPEAR\" SYN.txt | head -10"
}
```


### [2026-09-05T20:40:07.705Z] TOOL RESULT

```
=== KLN essence ===

=== KLN swastika ===
swastika, essence,  n.  —  F.,  fr.  L.  essentia,  ‘being  or  essence of  a  thing’,  fr.  essent-,  pres.  part,  stem  of  esse, ‘to  be’;  prop,  loan  translation  of  Gk.  ouctES, ‘essence’.  See  esse  and  cp.  words  there  referred to.  For  the  ending  sec  suff.  -ence.
swastika.  —  Prob.  for  fill  -  foot  and orig.  denoting  the  device  that  fills  the  foot  of a  painted  window.
swastika;  used  as  the  emblem  of Nazism.  —  G.  Hakenkreuz,  lit.  ‘hook-cross’.  See hook  and  cross,  n.

=== KLN yes ===

=== SKT essence/yes/am ===
AM.)
AM.
AM.)
AM.) U.  £.  ^niM.  ->  W.  Uu».  Irish IftA.     So  alio  F.  ^rm ;  izuxa na.
AM.)
AM.
```


### [2026-09-05T20:40:07.761Z] TOOL RESULT

```
=== SYN be ===
867:OHG melm (Tat. 49.9 = Mk. 10.14) : Goth. malma ‘sand’, etc., fr. the same root as Goth. mulda ‘dust’ (above).
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
8368:Walde-H, 1.210. Us ‘foo ae oe fatten! ‘ood, fodder” penéli "feed "+ Walde-P, 9.9 nes ee - 2.25. Ernout-M.
11514:ChSl. prébyvati ‘remain’, SCr. prebi- vati ‘dwell’, Boh. objvati ‘dwell’, Russ. prebyvati ‘sojourn, reside’, cpds. of ChSl. byvati iter. of byti ‘be’ (9.91); Boh. bydleti, denom. of bydlo ‘dwelling’, fr. the same root.
14928:Du. bouwen, MHG biwen, NHG bauen ‘cultivate, build’: OHG baan ‘dwell, inhabit, till’, Goth. bauan, OF buan ‘dwell, inhabit’, ON bia ‘dwell, ar- range, prepare’, also (late) byggja, Dan. bygge, Sw. bygga ‘settle, found, build’; with *-plo suffix OE botl ‘dwelling’ (whence OF bytlian), with metathesis bold (whence ME bylde, bulde, NE build), fr. IE *bheu- ‘be’ (9.91). Walde- P. 2.142. Falk-Torp 88, 121.
15985:9.91 BE 1, etc. Goth. wisan, ist, was Lith. biti, esu, yra tu eas etc. ON vera, er, var Lett. but, esmu, tr N SC, reat fui, etc. Dan. va@re, er, var ChSl. byli, Jeslit i Bice é fui, stato Sw. vara, Gr, var SCr. biti, jest qh a e 1 jus, aé OE wesan, béon, béo(m), Boh. —byli, Je(st) | Sp, _ser, estar, es, ful, sido, is, wes Pol. _byé, jest B estado ME _be(n), 2s, was Russ. byt’, est’ Rum. fi, teste, ful NE be, zs, was Skt. as-, bha- Ir. tau, biuu, buith Du. zujn, ben, zs, was Av. ah-, bi- Nir. taim, bim, beith OHG_ wesan, bim, ist, was W. bod, ys, yw MHG wesen, bin, ist, was Br. _beza, bez NHG sein, bin, ist, war
16023:As already stated in 9.91, one of the two IE roots for ‘be’ denoted primarily ‘come into being, become’, this sense prevailing or frequent in some of the TE languages.
16038:t. fier’ Be, atc. (9.91):
16054:6. ChSl. byti ‘be’ (9.91), also ‘be- come’. So sometimes in modern Slavic, esp. SCr. biti, Russ. byt’.
16057:7. Skt. bhi-, Av., OPers. bi- ‘be’ (9.91), but esp. ‘become’.
=== SYN spear ===
6677:‘Pointed object’. Dan. pik, Sw. pick (Hellquist 760); NE prick (NED Prick, sb. 17); W., Corn. cal, Br. kale’h (: W. col ‘sting’, Ir. colg ‘sword’, Pedersen 1.105); W. Zlost (‘sting, dart, penis’) ; Ir, gae ‘spear’ (20.26) and ‘penis’ (Laws, Gloss. 438) ; OF pintel (NE pintle ‘a kind of pin or bolt’), MLG pint, pitte, Sw. dial. pitt (Falk-Torp 861); OHG zumpfo, MHG zumpfe (prob. : MLG timpe, Du. dial. tump ‘tip, point’, nasalized form of that in NE tip); Russ. chuj perh. : chvoj ‘pine needle’ (Berneker 408); Skt. ¢epa-, gepas- (: Lat. cippus ‘stake, post’, etc., Walde-H. 1.219); Sp. carajo (prob. fr. VLat. *caracium, Grk. Xapaxtoy, dim. of xapak ‘pointed stake’ (REW 1862) ; perh. here W. pidyn, Br. pidenn (Henry 223).
34330:| CHAPTER 20 i WARFARE 20.11 Freur (vb.) 20.28 Gun; CANNoNn 20.12 BatrxE (sb.) 20.29 GuNPOWDER 20.13 War 20.31 Anmor (Defensive) : 20.132 Enemy 20.32 BreasTPLaTr, Corsier hea ies 20.338 HetMer ne aes 20.34 Snreip 20, Renton 20.35 Fortress 20.18 GENERAL 2030 = LOWnE 20.19 Ap 20.41 Victory 20.21 Wearons, ARMS 20.42 Derzat (sb.) 20.22 Crus 20.43 Arrack (sb.) 20.222 BATTLE-Ax 20.44 DEFENSE 20.23 Sune 20.45 RETREAT (sb.) 20.24 Bow 20.46 SuRRENDER (vb.) 20.25 Arrow 20.47 Captivr, PRISONER : 20.26 SpPEar 20.48 Boory, Srors : 20.27 Sworp 20.49 AxpusH (sb.) 20.11 FIGHT (vb.) ee péxopal, qroenewo one meu Lith. kovott, kautis, muStis TONELO erjask, vega Lett. kauti Lat.  pugndare, proeliari Dan. tee bare ChSl. mtrdli 46, bratt It. combattere, pugnare Sw. kampa, fikta, sldss SCr. _boriti se (biti se) : Be. Fee en OE feohtan, wigan, win- eer oS Sia se) - , nan ol.  walezyd, bid sie : sa Pa ME Ee kempe Russ. eee Nee bit'sja, . chim, cai rie rat'sja | a ON al troidim ne Ae vechten Skt.  yudh- : ym ehtan Av. parat-, yud- Br. en em ganna MHG vehten, wigen
34630:Av. zaéna-, and zaya-, with zayan- ‘armed’ : Skt. heti- ‘missile’, hi- ‘urge, hurl’, prob. also Ir. gae, OE gar, ete. ‘spear’ (20.26). Walde-P. 1.546. Barth. 1650, 1666. Walde-H. 1.576.
34741:Late ON pila, Dan., Sw. pil, Du. pijl, OHG, MHG pfil, NHG pfeil (OE pil ‘dart’, NE pile), fr. Lat. pilum theavy javelin’ (20.26). Falk-Torp 825. Weigand-H. 2.407.
34761:20.26 SPEAR
35340:1. Grk. aixpddwros, lit. ‘taken by the spear’, epd. of atxuy ‘spear’ (20.26) and vbl. adj. of aXicxouar, aor. #Awy ‘be tak- en, seized’.
```


## [2026-09-05T20:40:15.024Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34761,34790p' SYN.txt; echo \"===== 9.91 detail =====\"; sed -n '15985,16010p' SYN.txt | head -30; echo \"=== KLN swastika full ===\"; grep -o \".\\{300\\}Swastika.\\{0,400\\}\\|.\\{200\\}svastika.\\{0,400\\}\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T20:40:30.015Z] TOOL RESULT

```
20.26 SPEAR
Grk. — dépu, ASyx7, alxu7 ON spjol, geirr, spjor Lith. elis, zeSmas (rago- NG Sépu, Kovrépe Dan.  spyd, lanse tiné) Lat. hasta, lancea Sw. spjut, lans Lett. 5k’éps It. lancia, asta OE spere, gar ChSl. koptje, sulica Fy. lance, épiew ME _spere, launce SCr.  koplje, sulica Sp. lanza, asta NE spear, lance Boh. _o8tép, kopt, sudlice Rum. lance, suli{dé Du. speer, spie(t)s, lans Pol. wlécznia, kopja Tr. gae, -sleg OHG sper, spioz Russ. kop’e Nir.  sleagh MHG sper, spiez, lanze Skt. rsti- ¥ ae guwaywffon NHG speer, spiess, lanze Av., OPers. ar Sti-
r. goa,
Besides the most generic words for ‘spear’, as a weapon of thrusting or throwing, there are numerous terms for special types (NE lance, pike, javelin, ete.), most of which are left unnoticed.
The words are partly based upon such notions as ‘throw, thrust’ or the like, ‘sharp, pointed’, and (orig. denoting the shaft) ‘wood, spar’. But several are of obscure origin.
1. Grk. dépv ‘tree-trunk, beam’, etc., whence ‘spear-shaft’ and eventually ‘spear’ (the most common word in
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Hom.) : Skt. da@ru- ‘piece of wood, stake’, Av. daru- ‘tree-trunk, piece of wood, club’, Grk. dpis ‘tree, oak’, ChSl. drtiva ‘wood’, Goth. triu ‘tree, wood’, etc. (1.42). Walde-P. 1.804. Boisacq 197.
Grk. \6yxn (Hdt., not in Hom.), prob. fr. the same (Celtic) source as Lat. lancea. Boisacq 586. Walde-H. 1.757 f. Ernout-M. 521.
Grk. alyuy, prob. fr. *alk-oua- : Lat. icere ‘strike’, Cypr. lxyapévos ‘wounded’. Walde-P. 1.7f. Walde-H. 1.670. Boi- sacq 31.
Grk. éyxos (freq. in Hom. as ‘spear’;
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE 1391
Jater for other weapons), etym.? Walde- P. 1.608, 2.327. Boisacq 214.
Grk. dxwy ‘javelin’ (Hom.+) : dxawa ‘spike, goad’, axis ‘pointed object’, axpos ‘topmost’, Lat. dcer ‘sharp’, etc. Walde-P. 1.20. Boisacq 32.
NG xovrap., fr. late Grk. kovrdpror, dim. of xovrés ‘(boat-)pole, pike, crutch, goad’ (> Lat. contus ‘pole’ and ‘pike’ as weapon) : xevréw ‘sting, prick’, W. cethr ‘nail’, Br. kentr ‘spur’, ete. Walde- P. 1.402. Boisacq 484.
2. Lat. hasta (> It., Sp. asta), Umbr. hostatu ‘hastatos’ : Ir. gat ‘withe’, Goth. gazds ‘prick, sting’, ON gaddr ‘prick, point’, OHG gart ‘stimulus’. Walde-P. 1.541. Ernout-M. 445. Walde-H. 1.636.
Lat. lancea (> It. lancia [> Hung. lancsa > Rum. lance], Fr. lance, Sp. lanza), see under Grk. \éyxn, above, 1.
Lat. pilwm, the heavy javelin of the Roman infantry, orig. and earliest form much disputed. Thought by some to be the same word as pilum ‘pestle’ and first applied to a more primitive club- like weapon. Kropatchek, Jahrb. d. deutsch. arch. Inst. 1908 86 f. Couissin, op. cit. 22 f.
OFr. espieu, Fr. épiew (now heavy spear for hunting boars, etc.), fr. a Frank. *speut = OHG spioz (below, 4).
Rum. sulijd, fr. Slavic, cf. ChSl. sulica (below, 6).
3. Ir. gae (gai), W. gwaew, guayw and (cpd. with ffon ‘stick’) gwaywffon, Br. goaf, Gall.-Lat. gaesum, Gallo-Grk. yat- gov: ON geirr, OE gar ‘spear’, Grk. xatos ‘shepherd’s staff’, prob. fr. the same root as Skt. heti- ‘missile’, Av. zaéna- ‘weapon’, Skt. hi- ‘urge, hurl’. Walde-P. 1.528, 546. Pedersen 1.96. Walde-H. 1.575 f.
Ir. sleg, NIr. sleagh, perh. : Skt. srj- release, shoot, pour’, MHG_ selken ‘drip, sink’. Ir. selg ‘hunt (fr. the releas-
ing of the hunting dogs). Walde-P. 2.508. Pederson 1.100.
Other Ir. ‘spear’-names (Bauersfeld, op. cit.) crdisech (etym.?), laigen (= W. llain ‘blade, sword’, Pedersen 1.97, Walde-P. 2.381), manais (etym.?).
4. ON spjot, Dan. spyd, Sw. spjut, MLG spé&, OHG spioz, MHG spiez, NHG spiess (> Du. spies, spiets), etym. dub., perh.: Lith. spaudziu, spausti ‘press’, Grk. omebiw ‘hasten, urge’. Persson, Beitr. 415. Falk-Torp 1553 (with refs.; vs. 1138 and Walde-P. 2.119).
ON geirr, OE gar (OHG gér rare ex- cept in proper names like Gérhart, etc.) : Ir. gae, etc. (above, 3).
ON spjor (poet.), OH, ME spere, NE spear, OHG, MHG sper, NHG, Du. speer : ON sparri ‘spar, timber’, sperra ‘rafter’, OHG sparro ‘beam, rafter, pole’, Lat. sparus, sparum ‘hunting spear’. Walde-P. 2.665. Falk-Torp 1140.
ME launce, NE lance, Du. lans, MHG, NHG lanze (> Dan. lanse, Sw. lans), fr. Fr. lance (above, 2).
5. Lith. zetis (quotable from 16th cent.; Buga, Kalba ir Senové 166; still usual word, Senn) : ezti ‘go’.
===== 9.91 detail =====
9.91 BE 1, etc. Goth. wisan, ist, was Lith. biti, esu, yra tu eas etc. ON vera, er, var Lett. but, esmu, tr N SC, reat fui, etc. Dan. va@re, er, var ChSl. byli, Jeslit i Bice é fui, stato Sw. vara, Gr, var SCr. biti, jest qh a e 1 jus, aé OE wesan, béon, béo(m), Boh. —byli, Je(st) | Sp, _ser, estar, es, ful, sido, is, wes Pol. _byé, jest B estado ME _be(n), 2s, was Russ. byt’, est’ Rum. fi, teste, ful NE be, zs, was Skt. as-, bha- Ir. tau, biuu, buith Du. zujn, ben, zs, was Av. ah-, bi- Nir. taim, bim, beith OHG_ wesan, bim, ist, was W. bod, ys, yw MHG wesen, bin, ist, was Br. _beza, bez NHG sein, bin, ist, war
Words for ‘be’, denoting existence and serving as the copula, are mostly derived from two IE roots, of which
one (*es-) was the most colorless, while the other (*bheu-, *bhi-) evidently had
the primary sense of ‘come into being, become’,
Nearly every- | where tivo or more of these roots supple- ment each other in the complete verb.
“nd irrelevant to
tic of our general purpose,
Pedersen 2.418 ff., and cae €rmanic in general
i) ¥, i ty es-, Weak gi
tade *s_. = MoUt-M. 1091, Walde-P,
Grk. elut, Aeol. gupe (*esmi), 38g. éazi, NG eya (mid. starting fr. forms like imperf. juny NT), 3sg., pl. evar (fr. a = &eort; vowels after efuat); Lat. esse, sum, est, etc., with Romance pres. forms; infin. esse > VLat. *essere after legere, etc., hence It. essere, Fr. étre, Sp. ser; Celt. 3sg. (as copula) Ir. is, W. ys, yw, Br. es, etc. (Pedersen 2.422 ff.); Gme. 3sg. Goth., OHG-NHG ist, OE-NE is, ON, Dan. er, Sw. dr; OLith. 1sg. esmi (now esu), Lett. esmu, OPruss. asmai, 3sg. OLith. esti (now yra, as Lett. ir), OPruss. ast; ChSl. Isg. jesmt, 8sg. jestii, SCr jest, Boh. je(st), Pol. jest, Russ. est’; Skt. as-, 1sg. asmi, 3sg. asit, Av. ah-, Isg. ahmt, 3sg. asti; Hitt. es- (3sg. eszi, 3 pl. asanzi).
2. IE *bheu-, *bhi-, primarily ‘come into being, become’, this sense prevail- ing, on the whole, in Indo-Iranian, fre- quent also in early (and partly modern) Slavic, and wholly dominant in Grk., as
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
636
bona, aor. é6iv ‘come into being’, esp. ‘grow’ (¢iw ‘bring forth, beget’), dbors ‘nature’, duréy ‘plant’, etc., and in a Lat. differentiated form (fier, ft0). Walde-P. 2.140f. Ernout-M. 1001. Walde-H. 1.557 f.
Lat. perf. fui, etc. (early Lat. also infin. fore, imperf. subj. forem, Osc. fustd ‘esset’), It., Sp. fui, Fr. fus, Rum. fui, Rum. infin. fi, ete.; Ir. biwu, NIr. bim (consuetud. pres.), infin. Ir. buzth, NI. beith, W. bod, Br. beza (MBr. bout), Br. 3sg. bez, etc. (Pedersen 2.437 ff.); OF infin. béon, ME be(n), NE be, Isg. OE béo(m), NE be (subj. and dial. in- dic.), OHG bim, MHG, NHG bin, Du. ben; Lith. buti, Lett. but, pret. Lith. buvau, Lett. biju; ChSl. byti, SCr. bitz, Boh. byt, Pol. byé, Russ. byt’, pret. ChSI. bychu, pple. pret. ChSl. bylz, Russ. byl, etc.; Skt. bhi-, Av., OPers. bu- (8sg. Skt. bhavati, Av. bavait, OPers. 3sg. pret. abava, etc.) ‘become’ and simply ‘be’. (NPers. biidan ‘be’).
3. IE *wes-, primary notion ‘remain, abide, dwell’, as in Skt. vas-, Av. vah- (7.11). Walde-P. 1.306f. Feist 567.
9.92 BECOME
Digitized by Arya Samaj Foundation Chennai and eGangotri ; ——
SELECTED INDO-EUROPEAN SYNONYMS
Infin. Goth. wisan, ON vera, Dan vere, Sw. vara, OF, OHG wesan, MHG wesen; pret. Goth, OHG, MHG was (NHG war), ON, Dan., Sw. var, Or wes, ME, NE was, etc.
4, IE *sia- ‘stand’.
From Lat. stdre, pple. It. stato, Fr été, Sp. estado, also Sp. estar with pres, forms, etc.; Ir. -tdu-, NIr. taim fr. alaim (Pedersen 2.431. Thurneysen, Gram. 477 f.).
Cf. derivs. of the same root for the stronger ‘exist’, sometimes hardly more than ‘be’, as Lat. ex-istere (> Er. exister, NE exist, etc.), NHG bestehen (also entstehen ‘come into being, arise’), and for ‘become’ (9.92). j
5. Forms of Lat. sedére ‘sit’ are mixed with those of esse in the inflection of Sp. ser. Hanssen, Sp. Gram. p. 76.
6. Lith. 3sg., pl. yra, Lett. ir (old ira) is prob. an old noun meaning ‘existence’, ' but etym. unknown (OF 2sg. eart, pl. aron, NE art, are, prob. fr. *es-, cf.
=== KLN swastika full ===
```


## [2026-09-05T20:40:40.351Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN rsti para ===\"; grep -n \"rsti-\\|r$ti\" SYN.txt | head; echo; echo \"=== FSF khesht ===\"; sed -n '10455,10480p' FSF_pages.txt; echo; echo \"=== ARY khesht ===\"; grep -n \"خشت\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T20:40:41.876Z] TOOL RESULT

```
=== SYN rsti para ===
6:fiorspe tate 2 Sa : 2 baretehaheaisss Sateen Pete
8:pink i ; : mae 2 © mks f ; oF - piigheely teres Sinan he
9:wih ~ te eee, ¢ poalea te se eigaeaeteanees . ea E . : f ; vee tt sett tctetas, aaa | Swe eater desc sti'e heh thats boree getter ted oPetncnbatgragey | ; Aa stich?)
10:ot aren
12:Re Beer me
18:Wiel Obrtetetcteiaten,
20:ae 1 OT Wa THT aT famfrat STAT ae , ate asaa wee fer 8 afac aaa § Ae TS ATA! ie ‘ é ; és ; |
21:This beck furesented
24:ae as an expression of 48 . @ | Friendship, and Gooduill
30:i Digitized by Arya Samaj Foundation Chennai and eGangotri I Bh .

=== FSF khesht ===

     ‫ز آن نپسسریمان بل را نوات‬                                                   ‫خستو آمدن‬

 ‫ز بهرش بسی خسروی هدیه ساخت‬                                                    ‫افرار کردن‪:‬‬

                           ‫خشت (بازیر اول)‬                      ‫چو خستو نیاید میانش به از‬
‫نیز؛کوتاهکهدر میان آن حلقه‌ای از ابریشم‬           ‫ببرید و ایندانم آیین و فر‬
‫رییاسمان تافته ببندند اونگشت سبابه را‬              ‫(‪)۳-۱۳-۸۳۴‬‬

                                                                                        ‫خسته‬
‫در آن حلقه کرده‪ ,‬دست راتاب داده نیزه‬
‫کوتاه را بزور دست بسوی دشمن اندازند‪:‬‬                                  ‫‪-۱‬زخمی‪ ,‬آسیب‌دیده‪:‬‬

        ‫بهبالای سرو و به نیروی پیل‬                         ‫ویر بود‬
                                                                 ‫وری منرغخچ‬
                                                                          ‫سی ه‬
                                                                             ‫تل‬
‫به آورد خشت افگند بردو میل‬                        ‫اگر کشته گر خحستةً تير بود‬
 ‫(‪)۱-۷۳۲-۹۸۴۱‬‬                                      ‫(‪:)۲-۸۵۱-۸۸۴‬‬
                        ‫(ویس ‪:)۹۹۴-۲۳‬‬                ‫یشب‪:‬‬ ‫سری‬ ‫آم‪.‬‬
                                                                ‫‪-۲‬به معنی خستگی‪ ,‬زخ‬
     ‫چو شیرنربرآن خوک دژم تاخت‬                     ‫رسستم در نسخستین نبرد ابسافندیار‬
 ‫را بینداخت‬      ‫ان‬
                  ‫چشت‬
                    ‫یر خ‬
                       ‫په پ‬

=== ARY khesht ===
596:هند و اروپایی راکامل‌ترکرده‌اند. هنوز کار خواندن هزاران لوح وخشت هنت به پایان نرسیده است
611:حدود ۲۵ هزار لوحه و خشت مکتوب (بّرنوشته) در دست است. این خشت‌ها و لوحه‌ها به حروف
614:شده‌اند. خواندن این لوحه‌ها و خشت‌ها هنوز ادامه دارد. از لووبان‌ها و پالائیکك‌ها و لیسپان‌ها مدارکك
736:چندین دهه قبل» کاوشگران حدود سه هزار خشت سفالی دارای نوشتار در جزیره‌ی کرت و :
737:جنوب آبخست سان‌ی ونان پیدا کردند؛ شماری از این خشت‌هاکه قدیمی‌ترند (بنام ۸ 003۸13 ٍ
739:دیگری از ان خشت‌ها (8 ج1.13773۸) که قدمت آنها به حدود ۱۲۰۰ سال پیش از میلاد می‌رسد به ۱
1127:ا,گهن. دانش ما درباره‌ی:پارسی کهن محدود است به شمار کمی سنگك نوشته و خشت سفالی که به
1152:سلوکی (به خط میخی) و در تعدادی خشت‌های سفالی یافت می‌شود. در برخی متون مردمان
```


## [2026-09-05T20:40:54.588Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/swastika",
 "prompt": "Quote the etymology of 'swastika': Sanskrit svastika, su- 'well' + asti 'being', and the date when it was adopted as the Nazi emblem."
}
```


## [2026-09-05T20:40:55.496Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B3%D8%A7%D9%86%D8%B3",
 "prompt": "Quote the Persian entry اسانس: etymology (borrowed from French essence?) and meaning."
}
```


### [2026-09-05T20:40:58.106Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:40:59.335Z] TOOL RESULT

```
# Etymology of Swastika

**Etymology:**
"Sanskrit _svastika-s_, literally 'being fortunate,' from _svasti-s_ 'well-being, luck,' from _su-_ 'well'...+ _as-_, root of _asti_ '(he) is.'"

**Nazi Adoption:**
The term entered English usage referring to the Nazi emblem by 1932. The German designation was _Hakenkreuz_, meaning "hook-cross."

It's worth noting that the symbol itself originated as an ancient cosmic or religious symbol intended to bring good fortune, long before its association with Nazi Germany.
```


## [2026-09-05T20:41:06.050Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%A7%D9%86%D8%B3/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for اسانس: its origin tag (e.g. [فر.] = French) and meaning."
}
```


### [2026-09-05T20:41:11.718Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for اسانس

**Origin tag:** [فر.] (French)

**Meaning:** "جوهر و عصارة گل ها و گیاهان ، عطر مایه"

In concise terms, the Mo'in dictionary identifies اسانس as a fragrant substance derived from flowers and plants, with French origin, defined as "the essence and extract of flowers and plants, aromatic oil."
```


## [2026-09-05T20:41:20.387Z] TOOL CALL #58: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D8%B4%D8%AA' \\\n 'https://en.wiktionary.org/wiki/%D5%A1%D5%B7%D5%BF%D5%A5%D5%A1%D5%B5' \\\n 'https://en.wiktionary.org/wiki/%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%81%F0%90%8E%AB%F0%90%8E%A1%F0%90%8E%A3' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81es-' \\\n 'https://www.etymonline.com/word/essence' \\\n 'https://www.etymonline.com/word/swastika' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/' \\\n 'https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%A7%D9%86%D8%B3/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 161 (book p.131): roots Eres 2 (xešt/aršti) and Es 2 Es-ti (to be); verification of Nourai charts' 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:41:25.344Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/362b528ffe88f70e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f633a2d8dbe3196a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05960b93fb571f49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2c74dd4d20e459fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/12ca58cc8b64bdcb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b650c66cc7deea31.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/71391c242f0b58e3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0f13270b182cac58.txt
```


## [2026-09-05T20:41:30.312Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg161.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/161.png && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_am3.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/161_am_detail.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T20:41:30.389Z] TOOL RESULT

```
total 5160
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 16:41 .
drwxrwxr-x 10 sfmqrb sfmqrb   4096 Sep  5 16:21 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T20:41:44.785Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY latin index ===\"; grep -n -i \"ARSTI\\|RSTI\\|\\bES-\\b\\|ESMI\" incoming/ARY/ARY_latin_index_pages.txt | head -12; echo \"=== NYB ast ===\"; grep -n \"^ast \\|hast\\b\\|astīh\" NYB_vol2_glossary.txt | head -8; echo \"=== PHD hast/ast ===\"; grep -o \"last \\[AY T.\\{0,120\\}\" PHD.txt | head -3"
}
```


### [2026-09-05T20:41:46.438Z] TOOL RESULT

```
=== ARY latin index ===
1131:5 Ghaw ASLe) das y thos yo Lab} ou) 5 sp (SARMATIAN) «sll. (CHORESMIAN)
5655:THORSTI TISHNAK, (PAHLAVD 5 Sa
5657:THORSTI, THYRSTA TESHNI, TESHNITI <(KURDISH) 52,5
5663:‘THURST, THURSTIG TARSHAMIM, TAIRAMIM
6791:SKURSTU, SKURDAU, SKURSTI
8458:DESMITAIS — (LATVIAN) (3) ix DIXIEME APRENCH) Wild
9072:a ete nS As A RESMIDAN SH53!y olay GAG 92 “1 |
11534:KERTU, KIRSTI :(LITHUANIAN) gl)» KARETA, KARQTISH
12765:VARTYTI, VERSTI, VERCHIU WART H{TOKHARIAN A) A 5 iat
13601:ror Sopa Ka MITH-, MARZ-, MARSTI
15407:ESMI, ESHZI HITTITE) casa ESSERE LUTALIAN) .g\to\
=== NYB ast ===
431:an-aryan [’n’ry’n] (Prth) non-Aryans HajA: 2. ŠPrth: 5.11, = Prs anörän. anäst ['n'st'] nothingness, that which is vain, worthless: dróv u ~ 83%. 8427. — Paz. anäst, Skr. v. nästikya (Mx), nästika (SGV); anahast ‘non existent’, Skr. v. asat, nāsti; anahasti ‘unreality, extinction’ (SGV, Aog.). From the neg. pref. and (v.s.v. anāvinast) + *hast; anāst < ana- hast with contraction seems to be the older form, anahast to be a recent for- mation.
439:and [’nd] so much, so many: én ~ this much 64°; all this, all these 351. 623. 6572.24; hac én ~ sal apāc since so many years 1674; han ~ dušman all these ene- mies (sg. as with numerals) 249; 10426, 11923; — ~ cand as much (big, large, high, etc.) as: 3119-15, 935. (935 without ~); ~ cand yašt-ē (as much as =) at least some ceremonies 659; — hän <... cand as much (many, long, ete.) as 92°. 997. 10027, 10324-25; 2 ~ dranäi pahnāi cand han i nn hast twice the length (and) breadth of it as it is now 10024-25; 7000 han ~ cand
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
672:= Dūrēsrav bé 6 Zartušt guft ku: cigēn-at fratom ham (cf 209 ete.) bahr u rocik be apakand hom, an tč an (v. lan and ?an) har 2 aš apar barom api-t bē marnjēnēm "D. said to Z.: because thou hast deprived me, as the first, of both munistry and food, we both, thou and I, shall be enraptured in an ecstatic vision, and then I shall annihilate thee’.
706:ast ['st' the bones 50!. 10012; +ast- dahišnan corporeal creatures 5571. — Av. (211 sq.) ast-; MPrs ?st, stg. V. astómand.
950:subst. ‘he who will be’ = the future, coming man: har hastän butan bavētān all those who are, who have been, and who will be 5518, — Cf the use of Jv as a subst. in Apocal. 1:4.8 ó àv x«i 6 Av xal ó čpy0- uevoc.
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1065:| dragon 818; 3511, 3615-16, 411-18, 5110, 921. 1089; hast $ mat but 110? (but of course always but éstat); — the pres. of
=== PHD hast/ast ===
last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ
```


## [2026-09-05T20:41:54.268Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=15407 && /\\[pdf page [0-9]+\\]/{p=$0} END{}' incoming/ARY/ARY_latin_index_pages.txt >/dev/null; python3 - <<'EOF'\nimport re\nlines=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\np=None\nfor i,l in enumerate(lines[:15420],1):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: p=m.group(1)\n    if i in (15407,5655):\n        print(i,\"pdf page\",p,\"|\",l[:200])\nEOF"
}
```


### [2026-09-05T20:41:56.287Z] TOOL RESULT

```
5655 pdf page 196 | THORSTI TISHNAK, (PAHLAVD 5 Sa
15407 pdf page 527 | ESMI, ESHZI HITTITE) casa ESSERE LUTALIAN) .g\to\
```


## [2026-09-05T20:42:11.099Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD ers ===\"; grep -o \"ers-[^.]\\{0,200\\}\" AHD_watkins1985.txt | head -5; echo \"=== WLD Bd1 eres stechen ===\"; grep -n \"eres-\\|ereŝ-\\|1. eres\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== WLD Bd1 Speer rsti ===\"; grep -n \"rsti-\\|f-sti\\|ṛṣṭí\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -6"
}
```


### [2026-09-05T20:42:12.790Z] TOOL RESULT

```
=== AHD ers ===
ers-, “to dry
ers-
ers-
ers-ti-), to hasten: FESTINATE
ers-
=== WLD Bd1 eres stechen ===
9778:‘) rout, rasa, ros, kaum mit Anlaut gr- zu *neres- „ua£‘, s. \ T f. LEWb.' 2 65b. 
9804:Persson Beitr. 636 f.). Neben diesen Gruppen, die auf einem s-St. *eres- 
34568:mit m : aisl. gUna f. ,.Offnung“, schweiz. gim ds. ; aisl. geimi ...Meeres- 
39210:der darum yaXtjvt] aus *yeXdva assimiliert sein lafit?) „Heiterkeit, Meeres- 
46547:KZ. 30,210 aus *ters(o-) herleitbar ist, erwog man als Gdf. *teros-, *teres- 
46549:umgebildetes Heres-tris , -nos sein ; was zur wenig ansprechenden Folgerung 
47945:tres-, ters- (** teres-) „zittern". 
=== WLD Bd1 Speer rsti ===
43442:junges", ar. grsti-li ,.Farse, junge Kuh", gatji-h ,.junger Stier", worfiber aber 
48096:Charpentier KZ. 40, 474 f. aus idg. trsti-). Unsicher, da Binse und Schilf 
50876:upa-drg- f. ,,Anblick“, drsti- f. „Anblick“, av. aibldardsti- ds. (Inf. hoch-
```


## [2026-09-05T20:42:19.723Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9795,9820p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"==========\"; grep -n \"Stachel zum Viehantreiben\\|asträ ,Stachel\\|astra ,Stachel\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-05T20:42:19.790Z] TOOL RESULT

```
*eros, vgl. aucli sgeo/qAew „Neckerei treiben", Boisacq m. Lit.j, hom. ao« 
(Yok.j „ft/.ajiuxe“ (in r Ageg dosg; Schulze Qu. ep. 456, s. auch Proehde 
BB. 20, 380, Boisacq 76; “.igqg „Gott der Gewalttiitigkeit“ scheint nach 
Bechtel Lexil. 59 nicht urspriinglich cs-St. gewesen zu sein, sondern Per- 
sonifizierung des wzvenvandten Subst. agq „Yerderben, Gewalttat“ (s. auch 
Kretschmer Gl. 4, 347), woven ug^uevog „betroffen, versehrt, gequalt“); 
arm. her „Zorn, Neid, Hader“ (Liden aaO., m. Lit.); sehr zweifelhaft ist 
Zugehorigkeit von. russ. dial, jeresb „hitziger, zankischer Mensch“, jnrsitbsja 
,,sich widersetzen, zanken“ (*jbrs- : ai. 7 rsycL) (v. d. Osten-Sacken IP. 23, 380, 
Persson Beitr. 636 f.). Neben diesen Gruppen, die auf einem s-St. *eres- 
(: ers, e res, rs), *eros- ( e rdS-) beruhen tBrugmann Grdr. II 2 l, 192, wonach 
vielleicht auch lat. error nach errare mit rr ausgestattetes alteres *erds ist), 
stehn mit vergleichbarer Bed.: gr. dor], dgt]f.ievo g (s. o.). ai. irin- „gewaltig, 
gewaltsam“, gr. rot;, igedco, fraglich ob dazu russ. dial, jeretitbsja „sich 
argern, zanken“ u. dgl., s. Wz. *er-, *or~. 

1. el- in Baumnamen fur ,,Erle“ und „Ulme“. 

1. „Erle, Eller“. 

Lat. ohms „Erle, Eller“ (wohl aus *alsnos und nicht, wie friiher Peder- 
sen IF. 5, 40 wollte, mit altem Bindevokal aus *alisnos herzuleiten, vgl. 
dazu Johansson, Beitr. z. gr. Sprachk. 106 und Vf. LE\Vb. 2 2S; das an- 
lautende al geht auf alteres J- zuriick). — Fiir das got. ist nach Aus- 
weis des span, aliso „Erle“, frz. alize „Elsbeere“ ein "alisa „Erle“ an- 
zusetzen; ahd. elira und mit Metathese erila, nhd. Eller, Erie, mndd. 
==========
```


## [2026-09-05T20:42:30.144Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC rsti ===\"; grep -n \"rsti\\|ersti\" IEC.txt | head -8; echo \"=== SYN 8. Skt rsti ===\"; grep -n \"rsti-.*aršti\\|aršti-.*rsti\\|Skt. rsti\" SYN.txt | head -5; grep -o \"8\\. Skt\\..\\{0,300\\}\" SYN.txt | head -5"
}
```


### [2026-09-05T20:42:31.930Z] TOOL RESULT

```
=== IEC rsti ===
680:ardis ‘pont, tip, peak’. WP I, 83. Cf. rtis, arstis, ardus Arm. ardn (‘dart, lance’. Consonantism ob- scure. If a LW, cf. arstis); Gk. árdis; MIr.Ir. aird, áird ‘point, peak’; ON cf. erta ‘to taunt’ (:Gk. árdis. Boisacq)
734:arstis (rstis) ‘spear, shaft’. Cf. ardis, rtis Skt. rstíh; Av. Ober arstis; Oss. arc, pl. är- cita; (Iran.LW in Arm. aste); Picenian (Eastern Italic) cf. arsta, arstio ‘obelisk’. For OCz. rat- iSté ‘spear’, see ort-.
1822:bhrsos, ios, à, is ‘shag, tuft, bristles, fur. Cf. bhrstis Av. cf. boro$o ‘backbone’; Arm. bars (i-st. ‘horsehair, mane"); Gk. phársos (2) ‘cluster’; Phryg.? (LW in Gk.?) bürsa ‘rawhide, skin bag’; Lat. (LW or Gallo-Lat?) burra ‘shaggy garment’; re-burrus, adj. ‘bristly’, cf. also LLat. borr-àágo (“borage”, lit. *bristly plant"); variant (*bhors-) in Olr. barr *tree-foliage, spray’; Cor. bar (1) “bunch, tufted branch? beside Oir. barrán “head of hair; ME burre ‘burr’; Norw. Sw. borre, id. (Sw. also 'thistle- head, sea-urchin’); Cf. OCS brí$-ljanü *spindle- Dee beside Cz. brs-len, id.; cf. also Cz. brs- ina ‘grassy slope’. See bhors-
1823:bhrstis, os (bhurst-, bhrust-) ‘spike, shoot, twig, bristle’. WP II, 131 Sk. bhrstíb; Oss. barc ‘mane’; Hitt. parsdus ‘sprout; Lat. (ambig. füstis ((stick', fr. *bhurst-? cf. bhrustos (2)); Ir. bruis *brush- wood", ambig. cf. bhrust-); Br. cf. bréSen ‘twig; OHG burst, OE byrst; ON burst ‘bristle’; Sw. borst, id.; cf. Mod. Icel. byrstur, adj. ‘harsh’; Blg. brüst ‘green twigs’; Cz. bršť, Pol. barszcz 'hogweed' Srb. bfst *shoot'. (The Slav. forms are ambig. cf. bhrust-)
1824:bhrstið ‘break out, shoot, burst. Cf. WP IL, 206 and bhrstis above W brysio ‘hasten’, brys ‘haste’; Br. brésia ‘scamper’; OS brustian ‘break out; Slovene brstiti ‘sprout’; Icel. cf. byrstur, adj. ‘harsh, gruff; OE cf. byrst ‘loss’
2533:drktis “seeing, sight, brightness? Cf. derk-, dork-, drk- & WP I, 806 Skt. drstih; Av. (o-gde) darstis; Alb. dritë ‘light’; MIr. cf. drithle ‘flash’; OBr. cf. -drichet- ‘scope’; OHG zorcht, zoraht, adj. ‘bright; OS torht, id. OE torht (id. & *brightness")
3187:dhrêhtós ‘held; strong, firm, sold See dhrgh- (1) Skt. drdhah, drhitah, pp. and adj. id.; Av. dorosta, pp. id.; OLat. (prob.) forctus; Li. dirZtas ‘solidified; solid". Cf. Skt. dhrstih *tongs'
3191:dhrstis ‘boldness’. See dhrs- and next Per. durust “harsh, severe'; OE ge-dyrst, OHG gi-turst ‘boldness’; O-gde in Av. daršis ‘harsh’; Ir. dorrdha, id. (semantic link w. OE dyrst *tribulation")
=== SYN 8. Skt rsti ===
34803:7. Skt. rsti-, Av., OPers. argti- : Skt. rs- ‘push, thrust, stab, kill’. Uhlen- beck 35.
8. Skt. upatyaka-, fr. upa-tya- ‘be- neath’, hence ‘land at the foot of a mountain’,
8. Skt. urmi-, Av. varami-, above, 1.
8. Skt. wisa- ‘spring’ : udan- ‘water’. Walde-P. 1.252.
8. Skt. vrksa- ‘tree’, Av. varasa- ‘tree’ or ‘woods’ (? cf. Barth. IF 9.273, ftn.), etym.? Walde-P. 1.286, 289.
8. Skt. bhartar- ‘husband’, bharyd- ‘wife’, lit. ‘the sustainer’ and ‘the one sustained’, fr. bhr- ‘bear, carry’ : Grk. épw ‘bear’, etc.
```


## [2026-09-05T20:42:41.307Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"arstis (rstis) ‘spear, shaft’\")\nleaf=t.count('\\f',0,i)+1\nprint(\"leaf\",leaf)\n# find nearest page marker in that leaf\nseg=t.split('\\f')[leaf-1]\nimport re\nprint([m for m in re.findall(r'\\n(\\d{2,4})\\n',seg)])\nprint(seg[:200])\nEOF"
}
```


### [2026-09-05T20:42:43.183Z] TOOL RESULT

```
leaf 35
['10', '20', '30', '40']
arcus, gs. üs (also OL gs arqui *bow); arquus ‘rainbow’; cf. arqui-tenens “holding a bow’; OE earh, earwe ‘arrow’; ON or, pl. orvar, id.; Go. cf. arhvazna ‘arrow’; OCz. cf. roky-ta, Srb. rakita ‘sallo
```


## [2026-09-05T20:43:21.496Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor n in (236,237,238):\n    print(\"==== leaf\",n,\"(printed ~\",n-23,\") ====\")\n    print(leaves[n-1][:1500])\nEOF"
}
```


### [2026-09-05T20:43:23.269Z] TOOL RESULT

```
Exit code 1
==== leaf 236 (printed ~ 213 ) ====
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
IndexError: list index out of range
```


## [2026-09-05T20:43:26.944Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"n leaves\",len(leaves))\nfor n in (len(leaves)-4,len(leaves)-3,len(leaves)-2):\n    print(\"==== leaf\",n,\"====\")\n    print(leaves[n-1][:1200])\nEOF\necho \"=== grep ah- 'to be' ===\"; grep -n \"ah- vb\\|^ah-\\|'to be'\" KNT.txt | head -10"
}
```


### [2026-09-05T20:43:28.593Z] TOOL RESULT

```
n leaves 232
==== leaf 228 ====
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne -
LEXICON 203
‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5242.11), ef. ~o- extension in Av. masya-, Skt. mártya- ($144.IV). See also wmartiya-, *Martiya-.
martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ 16, 19, 21, 24; XPh 51. martiyà узш. "Ма 56. martiyam asm. DB 3.57; DNa 3; DNb 12, 22; DSe 3; DSf 2, 16f; DSs 2; DSt 3°; рле 2; DE 4f; XPa 2; XPb 4f; XPe 21; XPd 3f; XPf 3; XPh 3; XE 5; XV 4; A'Pa 3P; А°Не 3f; A?Pa 3f. martiyahyé gsm. DNa 4, 44; ОМ 3; DSe 4f; DSf
. 8; D8s 5^; DSt 4^; DZe 2f; DE 6; XPa 3; ХРЬ 6;
ХРе 3; XPd 4f; ХРі 4f; XPh 4; XE 7; XV 5; AlPa 5°; A?He 4f; martthya A3Pa 4f (852.VI; hardly phonetie, as taken by Morgenstierne, Ácta Or. 1.253). martiyá npm. DB 1.571; 4.80, 82; DSf 47, 49, 51, 52, 54. татітуй apm. DB 2.77; 3.48, 50, 74, 90, 91. татйуйтат gpm. DB 4.87. martiyaibiš ip
==== leaf 229 ====
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V).
(1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà npm. DSf 50f, 52, 55.
(2) ‘Egyptians’, as province: Mudräyā npm. DPe 11f.
(3) ‘Egypt’: Mudráya nsm. DB 1.15, 27°; DNa 27; DSe 26°; DSm 7^; XPh 28. Mudrüyam asm. DB 1.32, 33; DZe 8. Mudrayé absm. DSf 41; DZe 11. Mudrüyaty lsm. DZe 9.
ya- rel. pron. ‘who, which’, generalized by enel. -ciy (ef. Hz. ApI 355-6): Av. Skt. ya-, Gk. ds, pIE %0-. See also уйй, уада, yada-, yadry, yaniy, уйй.  ya-ciý nan~ ($105, $130, $197) РМ 57. ya-ciy asn. DNb 35, 86
204
Yautiyd- sb. ‘Yautiya’, a district in Persia: Elam. 4a-t-t-1a-18, АКК. 1-0-0-ја. Yautiya nsf. DB 3.23.
yaud- vb. ‘be in commotion’, present stem yauda-: Av. yaoz- ‘boil up’ (§88), pres. yaoza- (Hz. AMI 8.67, ApI 362-5); not to Av. yaod- ‘fight’, Skt. yudh-, because of the difference in the present stem (Av. yüióyeiti, Skt. yüdhyati; JAOS 58.116).  ayauda imf. (5213) XPh 31f (not dyauda пзш. ‘rebellion’, as taken by Henning, BSOS 10.505, which is refuted by Akk. version). ayauda" 3d pl. imf. (5232.П) DSe 33°. yau[da*- tim] asf. pres. pte. act. ($190.1, $240) DNa 32.
==== leaf 230 ====
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39.
lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $296; cf. yaa tya ХР 29); yadàyà XPh 39 (perhaps error in writing, §55.1; but ef. Hz. AMI 8.66, ApI 358, Nyberg Rel. 477-8).
*Yadd- sb. ‘Yada’, probably ‘Anshan’ (as shown by the Elam. translation 3.3 an-za-an.mar, read by Cameron; cf. §166.n2): not an abstract yadà- ‘loyalty’ to root yad- (q.v.), as commonly taken (wrongly also Foy; KZ 35.43; Hüsing, ОГЛ
Ы
LEXICON | 205
8.513-6; Hz. ApI 244-9; Nyberg, Rel. 477-8). Yadayd absf. ($141, $175) DB 3.26.
yadiy conj. ^if, when’: Av. yetéi, Skt. yddi: per- haps pAr. nt. rel. *iad + deietic 4. Syntax $297. (1) Sf, with subj.: DB 4.38f, 54, 57, 721, 77; DPe 19, 22; DNa 38 (yadi-patiy), DNb 29 (yadi- và; cf. Hz. ApI 359); XPh 47 (yadi-maniyáty; 841, $92. VI); with opt., DNb 20f; with pres. ind., ОХЬ 25 (yadi-và). (2) ‘when’, with imf. ind., DB 1.38, DS
=== grep ah- 'to be' ===
5127:tah- vb. ‘be’: Av. ah- Skt. as-, Gk. tert, Lt.
5140:tah- vb. ‘throw’: Av. *ah-, Skt. as-, pres. dsyatt. dlhlyatlé imf. mid. as pass. (§214, §274d) DB 1.95 (restoration of Kern, ZDMG 23.239).
```


## [2026-09-05T20:43:42.610Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [\"tah- vb. ‘be’\",\"LEXICON 203\"]:\n    i=t.find(pat); print(repr(pat),\"leaf\",t.count('\\f',0,i)+1)\ni=t.find(\"tah- vb. ‘be’\")\nprint(t[i-200:i+900])\nEOF\necho \"=== hasiya adj ===\"; grep -o \"hasiya- adj.\\{0,300\\}\\|hašiya- adj.\\{0,300\\}\\|haSiya- adj.\\{0,300\\}\" KNT.txt | head -3"
}
```


### [2026-09-05T20:43:44.663Z] TOOL RESULT

```
'tah- vb. ‘be’' leaf 197
'LEXICON 203' leaf 228
ess’ are related ideas. asnaty DB 2.11f; [aSnajiy DB 5.23.
агай adv. “known ОСА: azdà "thus", Phi. ага,
174
Skt. addhá ‘surely’, from pAr. *adzdhà (885); cf. MB Gr. §118. DB 1.32; DNa 43, 45; DNb 50.
tah- vb. ‘be’: Av. ah- Skt. as-, Gk. tert, Lt.
esl, Gt. ist, pIE *es-. See also hafya-, А@їуй- bau$na-. Conj., $208.
amiy ist sg., Av. ahmi, Skt. dsmz, Gk. Lesb. tume, Att. eui, NEng. am (5118.11, $226.1): AmH 9; DB 1.12, 39, 53, 75, 79; 2.10, 15, 80; 3.25, 81; 49, 11, 14°, 17, 19, 22, 25, 27, 30; DBb 5, 7; DBe 8f; DBd 4f, 7; DBe 6, 9; DBE 4f; DBg 7f; DBh 5f, 9; Рві 6, 10; DB} 5; DNa 35; DNb 6f, 7, 8, 1f, 13, 15, 26, 27, 34, 40, 42, 43, 44, 51; Die Т; A? He 18.
азу, Ау. asti, NPers. dst, Skt. ásti (5116, 5228.1): DB 4.46, 51; DNb 54f, 56; DSe 37; XPh 30.
a'mahy, Av. mahi, Skt. smds-1, Gk. Dor. dues 8118.11, §230.1): DB 1.7f, 11; DBa 12, 18.
ha"tiy 3d pl, Av. honti, Skt. sánti, Gk. Dor. iy i, Ове. sent ($89, §122, §232.1): DB 4.61, 63°.
Gham ist sg. imf., Skt. ham, Gk. Hom. ўа (867.II, §122, 6226.1): DB 1.14; 2.6, 12; 377; 4.63 bis, 64. алат XPh 15f ($53, $131; hardly with Hz. AMI 8.65, A
=== hasiya adj ===
```


## [2026-09-05T20:44:00.031Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(\"last leaf tail:\",leaves[-1][-600:])\ni=t.find(\"the derivative haSiya- ‘true’\")\nprint(\"hasiya grammar leaf\",t.count('\\f',0,i)+1)\ni2=t.find(\"OP hasiyam ‘true’\")\nprint(\"hasiyam leaf\",t.count('\\f',0,i2)+1)\nEOF"
}
```


### [2026-09-05T20:44:01.862Z] TOOL RESULT

```
last leaf tail: ubj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
hasiya grammar leaf 95
hasiyam leaf 47
```


## [2026-09-05T20:44:09.880Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"es- ,,sein\\|es- „sein\\|esmi\\b\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-05T20:44:09.926Z] TOOL RESULT

```
10418:es- „sein“. 
28518:umbr. esmi-k „huic“, lat. ecce (wohl aus *ed-ke , s. *e Pron. -St.), osk. um 
43716:ges'mti „loschen“, gesmi „kleines, cben noch glimmendes Feuer"; lett. el: lest u
```


## [2026-09-05T20:44:12.316Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10418,10450p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-05T20:44:12.364Z] TOOL RESULT

```
es- „sein“. 

Ai. usmi , asti „bin, ist*‘, av. ahmi, asfi , ap. amiy, arm. em „bin“, gr. 
£((<(, tori, alb. jam „bin“, lat. sum , cst altlat. escit, eseunt, obescet wie gr. 
tay.t), o. sum, est. 1st, u. cst, air. am, is, got. im , ist, lit. esm't, csl(i), apr. 
(tsmai. ast cst, aksl. jesnib, jcslz usw, s. die Grammatiken und vgl. Wb. 
m. Lit. 

Ptc. *scnt , sent „seiemP, z. T. m. Entw. zu „wahr, tatsachlich“ und 
weiter teils zu ,,gut“, teils zu „der wirkliche Tater, Schuldige 11 : ai. sant- 
„seiend, gut“, gr. dir, tdtv, dor. pi. tvreg usw., lat. pmesens, absens, sons 
(s. u. *snta „straffiillig, schadlich“ ( morbus sontinis, s. Yf. LEWb. 2 725) 
= ags. sod „wahr“, anord. sannr „wahr“ und „wessen Schuld aufier Zweifel 



es-en, os-en,-er- 


161 


steht 11 , woneben tiefstufig germ. *sun(d')jd-, got. sunjis ,,wahr u ( sunja 
„Wahrheit“; die eigentliche Bed. noch in bisunjunc ,.ringsum u , ursprgl. 
g. pi. „der ringsum seienden“ = ai. satyd- „wahr, recht“, n. „Wahrheit“, 
av. hcith/a- ,. wirklich 11 , ap. hakiya- ds. ; lit. esas m., esanti f.. abg. sg, snsta 
„seiend“. 

^o-Pte. *s-e-ta -, s-o-fb- (s. Curtius 3 207. Brugmann II 2 1, 401) in gr. ha’ 
dhgfHj. dyad a Hes., hd£a> „priife“. heog, hv/uog „wahr, wirklich 11 und ooiog 
„recht, erlaubt 11 (kaum Umfarbung eines *anog = sntios *nach siehe 

auch Boisacq s. v.).
```


## [2026-09-05T20:44:52.950Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT ahmi/haithya ===\"; grep -o \"haiθya-.\\{0,150\\}\\|hai%ya-.\\{0,150\\}\\|haiihya.\\{0,120\\}\" BRT.txt | head -5; grep -o \"•  g\\.,  j\\.  ah-.\\{0,250\\}\\|j\\.,  g\\.  ah-.\\{0,250\\}\" BRT.txt | head -3; echo \"=== TLM amiy ===\"; grep -o \"amiy.\\{0,180\\}\" TLM.txt | head -3; echo \"=== LEW esse ===\"; grep -o \"sum, esse.\\{0,250\\}\\|esse .\\{0,200\\}\" LEW_1910.txt | head -3; echo \"=== LAT esse ===\"; grep -o \"sum, es, est.\\{0,250\\}\" LAT.txt | head -2"
}
```


### [2026-09-05T20:44:54.782Z] TOOL RESULT

```
=== BRT ahmi/haithya ===
=== TLM amiy ===
amiy
amiy  hya  Kuraus  pu0ra  Kanbuji-
amiy  hya  Kuraus  pu0ra  kasciy naiy  adarsnaus  cisciy  0astana-54)iy  pariy  Gaumatam  tyam magum  yfita  adam  arasam  pasava  adam  Aura-55  )maz[d]am  pati- yavahyaiy3  Auramazda
=== LEW esse ===
esse I 639 vingeon, vigeon II 796 viste II 583 votle II 746 zeste, ziste II 583/4
esse (air.) I 392 esslu- IT 327 essomutn (air.) [423 estar (air.) I 392 é (air.) 17 597 étan (air.) I 53 eter, etur, etar (air,)
esse (air.) IT 85 methos II 80 mi (air.) ,,Monat* 71 mi- (air.) ,,miB-“ IT 137 miad (air.) IT 95 mian (air.) IT 60 mid- (air.) ,medius’ IT 57 mid (air.) ,,Met* IT 59 mide (mir.) IT 357 midiur (air.) IT 56 
=== LAT esse ===
```


## [2026-09-05T20:45:01.725Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT hai_ya wirklich ===\"; grep -n \"wirklich, wahr\\|'wirklich'\\|,wirklich\" BRT.txt | head -8; echo \"=== BRT ahmi ===\"; grep -n \"ahmi\" BRT.txt | head -5; echo \"=== LEW sum ===\"; grep -n \"^sum,\\|sum, ,ich bin\\|sum  ,ich\" LEW_1910.txt | head -5"
}
```


### [2026-09-05T20:45:01.804Z] TOOL RESULT

```
=== BRT hai_ya wirklich ===
=== BRT ahmi ===
2454:—  vlstäspo  Snhqm  daJiyunqm  ssu.asfö.- Umö  *bval  Yt.  5.98;  —  humaya  nö  büvata .  .  ahmt  nmiirte  aiiiAe  visi  ahmi  %antvö aiiihe    daiühvS   aAmnktmca    .  .   Vr.  12.5;
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2472:dalvil  . .  atibyö  kam  Y.44.20;  46.12;  — li  narS..aeiqm  nmäna  Yt.i~.yC;  g— 14.^, J0.39f.s,  33,Y./j.3,j7.37,Vr.//.i9,V.2, 43-J.i4,Ä4i,  12.1, 13.50,  i5.22,FrV/. 10. 40,  N.<S'5; — g3ui..ya  dar>nlhu  mi^rS.- drujqm  ..frazarsta  (sd.)  aglqm  rai'iya  .. hiit»nte  Yt. /o.  38;  —  vTspanqmca  , .  asae- nqm  aiaoninqmca  .,  vUpanqmca  allqm  za- ra'iuStnm  ..  *susruma ikatsim  Yt.Jj.148; —  a^qm  anyS  N.  61,  62;  —  aifam  aOiai»- kam  .  .  adqmcH  S  ahmt  .  .  vicC^ei  (sd.) aipT\.32.i;  30.1,  8,55.9;  —  haxays .. astvat.gr3take  .  .  assu  paro  fräntmlite aismü  Ytiff.g$;  — gä^a  . .  yezi  argAqm *Syutnpe  väUm  framaraiti  N.  42;  —  xi paiti  apqm  .  .  a^ra  atthqm  V.  y.  5 1 ,  Y. 6Ä7;  Yl/j.68;  —  duzvarmanhS  .  .  rä- mqmcä  J//'"'  dadätu  V.  ^3.  8 ;  —  yaia  ta r  ,  ,  minghäeä  .  .  yH  vohü  .  ,  a'iä  %WJ Si/'"'  yazamaide  Y.  j(?.4;  —  karapsAsaJ (sd.)  kfvitäsca  . .  töi  abyH  (AbL)  bairyänts (sd.)  .,  Y.52. 15; — spuda..kuir3  ayä.. Y.44-I5;  30.6,  3t.io;  —  /J  mainyn  .  . ascä  (GD.)  .  .  Y.30.3;  —  Gen.  in  Ver- bindung mit  hava-i  zasta  hl . .  frasniöa- v paityesii  V.22.7  — 13;  /.z;- — \y"t  aSahe  yat  apirmäyükahe  ahe  hava- aiwySr3hafi?m,.äat  aiijhi  ahi  aiwyästö  Y.  _v(7«  tütroö  "die  Hände  ..  des  Kindes  an ij.zb;  — ahur>m  ..  ahyä  x!a~i:räc3  ..  *hva- 1  dessen  Leib"  V.itf,  7  (?)  "';  —  dgL,  zugleich paphsiica  (sd.)  lim  .  .  yasämaidi  Y.  J7.  vorausweisend:  astvatjr3iö  ..  kB  ..  aiike if.;  —  sraosim  ..yazamaide  ahe  raya  . .  j  haxayB  /räyente  astvat.iritahe  Yt.  ip.  95: aiÄke  ama  ,.  ahe  yasna  ..  t?m  yai3i  "den '  - —  dalnqm  .  .  yao:dai%xSa  ai:a  sT  aiAka Sr.  .  .;  ob  seiner  Pracht  .  ."  Y.  57.3;  Yt.  yaoidaitii  ..  havaya  .  .  dainayä  Y.io. J-i^i  5i  9  (statt  fem.!);  —  noii  kl  anyö\i9.  a)  spez.  auf  das  Subjekt  des  gleichen urva  kaum  urvämm  paiti  irista  (sd.)  ^a-|Satzes,  Reflexivum:  ka%S  .  .  gqm  Ha- zaiti  xraosyü(a{%t^voyaca*a>»he^^.*at3hr^^  sSil  y}  kirn  ahmai  ..  stsi  usyaj  (sd.) Y.  13.9;  —  fravasayS  . .  ankam  raya  . .  Yt  ".  .  qui  eam  sibj  .  .  esse  cupiat"  Y.  ^o.  2 ; 13.2, 14—18"';  — gunäayäi  ..  za/an  ta/-  ^  —  nsit  sp>ntqm  d3r?st  (sd).  akmai  stöi San  (sd)  aya^'*  masJY.3.32;  —  vac?  ..\armaitlm  Y.4^.2;  —  hvJ  tat  n3  ..  ak- yii  . ,  akmai  straohm  dqn  Y.  45. 5 ;  —  |  mai  "'  dazdl  (sd.)  Y.  5/.  1 9 ;  —  aada  (sd.) ustä  ahmst  yahmai  .  .  kakmaicTt  . .  atca  \  vinzyötüca  It  akmai  fracä  vatöyBtü  (sd) <ihmai  Y.  43. 1  f ;  —  gavöi  . .  ha  %X  to\lt  alibyB  yöi  .  .  "..  sibi  (ipse)  . ."  Y.  J5.  6; huisii»m3  .  .  dal  .  .  at  ahyäi  .  .  masda  \- —  at  hT . .  /ravanll  (sd.)  vasirim  ahyai orvara  vaxsat  Y.4S-6;  31-9;  —  raya  ..\fntyant3m  Y.jj.  10;  —  nSit  ta  Im  x^3ui koya  aiiiAä  raiavö  Y.iff.iS;  *YyX.  50; — {vaipyö  .,  zara'iuhrtm  ..  Ayat  akml'^ paoiryö  gairis  . .  akmat  haca  garayO  tu- 1  urüraost  astö  hyat  , .  v3z3  (sd,)  Y.  31. uxiyqHYt.ig.\i.;  34,80;  —  hö  nBit..*/r3-\  12.  aa)  Der  Gen,  vertritt  dann  die  ent- nJmaite  ,.  /rä  ahmst  parö  ..  «jÄion/i;  j  sprechendeFormdeslat  suus:  airj  *i'jiri»i Y. 57-18,  ungeschickt  benutzt  Ytp.4;  lo.  baraiti  mi>akvac3  vä  irvivaca  (sd.)  vä.. 117;- —  *haltuma  . .  kacaiti  dim  . .  astica  akyl  zaridaca  manat»kac3  ", .  ex  suo  (uter- ahmi  avavat;^arin6  yäi:a  yat..Yx.ig.(>Z;\c^^)  corde  et  animo"  Y.ji.ti; —  akya —  :^aitu/  . .  vtrizifum  mat  airyamnä  . .  \xrata  frö  ma  sastB  (sd.)  vakistä  Y.  45. 6  ;
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
=== LEW sum ===
```


## [2026-09-05T20:55:11.569Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build161.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 161,\n \"book_page\": 131,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Eres 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁ers- 'to pierce, thrust' (Pokorny 335 '1. eres- stechen'); the ti-abstract *h₁ŗstí- 'spear'\",\n   \"note\": \"Pokorny p.335 carries exactly this root: '1. eres- ,stechen‘. Ai. ṛṣáti ,stößt, sticht‘, ṛṣṭí- ,Speer‘, av. aršti- ds.; lit. erškėtis ,Dornpflanze‘; sloven. resak ,Gänsedistel‘.' Language label (Indo-European) and gloss ('to pierce') are both right, and Nourai's numbering matches Pokorny's own: Pokorny's '2. ere-s- ,fließen‘' begins on p.336 and is Nourai's Eres 1 (hence the redirects 'Ers' and 'Ersen' on this page). The root is small and poorly attested outside Indo-Iranian — Pokorny's only authority is Persson, Beiträge 84; Walde-Pokorny has no separate entry for it and Watkins/AHD omits it (no English reflex). Modern practice reconstructs the noun as PIE *h₁ŗstís > PIIr. *Hŗštíš, and Buck (20.26) derives Skt. ṛṣṭi-/Av. aršti- from Skt. ṛṣ- 'push, thrust, stab', i.e. the same 'pierce' semantics. The one real problem on this chart is not the root but the word aštrā- attached to node #1 (see there).\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁ers- «سوراخ کردن، فرو بردن، زدن» در پوکورنی صفحهٔ ۳۳۵ زیر عنوان «1. eres- stechen» آمده و همان نمونه‌هایی را دارد که نورایی آورده است: سنسکریت ṛṣáti «می‌زند، فرو می‌برد» و ṛṣṭí- «نیزه»، اوستایی aršti-. شماره‌گذاری نورایی نیز با پوکورنی هم‌خوان است، زیرا ریشهٔ دوم پوکورنی (ص ۳۳۶، «جاری شدن») همان Eres 1 اوست. امروز این ریشه را *h₁ers- و نام ابزار را *h₁ŗstís بازسازی می‌کنند. ادعای نورایی دربارهٔ خود ریشه درست است؛ اشکال در واژهٔ aštrā- است که در گره شمارهٔ ۱ زیر این ریشه نشانده شده است.\",\n   \"sources\": [\n    W + \"%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%81%F0%90%8E%AB%F0%90%8E%A1%F0%90%8E%A3\",\n    W + \"%D5%A1%D5%B7%D5%BF%D5%A5%D5%A1%D5%B5\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:335\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 349 (the leaf carrying the running numbers 335–336), last entry before the '336' catch-number: '1. eres- ,stechen‘. Ai. ṛṣáti ,stößt, sticht‘, ṛṣṭí- ,Speer‘, av. aršti- ds.; lit. erškėtis ,Dornpflanze‘, vgl. oben S. 67; sloven. resak ,Gänsedistel‘. Persson Beitr. 84. Verschieden davon ist: [336] 2. ere-s- ... ,fließen‘.' Exactly the root, label and gloss the chart prints.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.150 f. (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt l.9804)\", \"stance\": \"silent\",\n     \"note\": \"Walde-Pokorny I discusses an s-stem *eres-/*eros- only in the 'anger, rush, wander' sense ('Neben diesen Gruppen, die auf einem s-St. *eres- ... beruhen'); there is no separate 'stechen' root, which is why Pokorny cites Persson Beitr. 84 and no WP number for it.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt (grep 'ers-')\", \"stance\": \"silent\",\n     \"note\": \"Watkins has only 'ers-, to be wet' and '*ers-ti- to hasten' (FESTINATE); no root 'to pierce' and no *ŗsti- 'spear' — expected, since the family left no English descendant.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 20.26 SPEAR, §7 (SYN.txt l.34803)\", \"stance\": \"supports\",\n     \"note\": \"'7. Skt. ṛṣṭi-, Av., OPers. aršti- : Skt. ṛṣ- ‚push, thrust, stab, kill‘. Uhlenbeck 35.' — the same root meaning Nourai gives.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann p. ~20 s.v. arstis (IEC.txt leaf 35)\", \"stance\": \"supports\",\n     \"note\": \"'arstis (rstis) ‚spear, shaft‘. Cf. ardis, rtis. Skt. ṛṣtíh; Av., OPer. arštis; Oss. arc, pl. ärcitä; (Iran. LW in Arm. ašte); Picenian cf. arsta, arstio ‚obelisk‘.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan / Old Persian\",\n     \"words\": \"aršti, aštrâ 2; aršti-bara; u-ârštika\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Three of the four forms are exactly right, one is wrong. (a) Av. aršti-, OP aršti- f. 'spear' (OP nom. arštiš, DNa 44 'the spear of the Persian man has gone forth far') continues PIIr. *Hŗštíš < PIE *h₁ŗstís, a ti-abstract of *h₁ers- 'thrust, pierce'; the syllabic *ŗ regularly yields Old Iranian ar- before the cluster -šti- (Kent §152.III, §179.III), so *ŗs-ti- > aršti-, beside Skt. ṛṣṭí-. (b) OP aršti-bara- 'spear-bearer' = aršti- + bara- 'bearer' (PIE *bher-, Nourai's Bher 1); it is the caption of Gobryas the Patischorian on Darius's tomb at Naqš-e Rostam (DNc 2), where the mason's slip in the spelling is discussed by Kent. (c) OP āršṭika- 'spearman' is aršti- with vṛddhi of the first syllable plus -ka-, and uv-āršṭika- 'good spearman' prefixes u-/uv- 'good' (Av. hu-, Skt. su-, Nourai's Su 1); both stand in DNb 44, 'āršṭika amiy uvāršṭika' — 'as a spearman I am a good spearman'. Nourai's 'u-ârštika' is Kent's uvāršṭika- with the pre-vocalic -v- dropped; the form and gloss are otherwise correct. (d) aštrā- does NOT belong here and is not 'a short spear': Bartholomae (AiW col. 263 f.) glosses Av. aštrā- f. as 'Geisel, Peitsche, Knute' (whip, scourge) and derives it 'zum V. az-, eig. ‚Vorrichtung zum Antreiben der Tiere‘', comparing Skt. aṣṭrā- 'Stachelstock zum Viehantreiben' (ox-goad); Pokorny himself lists 'ai. aṣṭrā ,Stachel zum Viehantreiben‘, av. aštrā ,Peitsche, Geißel‘' as the -trā- instrument noun of the root aǣ5- 'treiben' on p.4, i.e. from PIE *h₂eǣ5- 'to drive', not from *h₁ers-. So the arrow is right for aršti-/aršti-bara-/uvāršṭika- and wrong for aštrā-, which also carries a wrong gloss; the node therefore takes the worst verdict.\",\n     \"derivation_fa\": \"از چهار صورت این جعبه، سه تا درست است و یکی نادرست. اوستایی و پارسی باستان aršti- «نیزه» (صورت فاعلی مفرد arštiš در سنگ‌نبشتهٔ داریوش در نقش رستم) از ایرانی‌هندی آغازین *Hŗštíš و آن از هندواروپایی *h₁ŗstís است؛ روال آوایی آن است که *ŗ هجایی در ایرانی باستان پیش از خوشهٔ -šti- به ar- بدل می‌شود. aršti-bara- «نیزه‌بر» مرکب است از همین واژه و ستاک bara- «برنده»، و uvāršṭika- «نیزه‌ور خوب» از پیشوند uv- «خوب» با صورت وردھی از aršti- به‌علاوهٔ پسوند -ka- (هر دو در DNb ۴۴: «نیزه‌ورم، نیزه‌وری خوب»). امّا aštrā- در این‌جا جای ندارد و معنایش «نیزهٔ کوتاه» نیست: بارتولومه (ستون ۲۶۳) آن را «تازیانه، شلاق» معنی کرده و از ستاک az- «راندن» گرفته است، و خود پوکورنی هم در صفحهٔ ۴ آن را زیر ریشهٔ aǣ5- «راندن» آورده است. پس این پیکان برای سه واژهٔ نخست درست و برای aštrā- رد می‌شود.\",\n     \"sources\": [\n      W + \"%F0%90%8E%A0%F0%90%8E%BC%F0%90%8F%81%F0%90%8E%AB%F0%90%8E%A1%F0%90%8E%A3\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"POK:335\", \"status\": \"partial\",\n       \"note\": \"Pokorny p.335 has 'av. aršti- ds. [= Speer]' and so supports aršti-, but it says nothing about aštrā-, aršti-bara- or uvāršṭika-; and the same book puts 'av. aštrā ,Peitsche, Geißel‘' on p.4 under aǣ5- 'treiben' — i.e. Nourai's own first reference contradicts his placing of aštrā- here.\"},\n      {\"ref\": \"KNT:172\", \"status\": \"supports\",\n       \"note\": \"Kent, Old Persian, Lexicon p.172 (KNT.txt leaf 195, the leaf that carries the running number 172): 'aršti- sb. ‚spear‘ (§30): Av. aršti-, Skt. ṛṣtí-, pIE *ṛs-ti- (§152.III, §179.III), to root in Skt. ṛṣáti ‚rush, push‘. See also āršṭika-, aršti-bara-. arštiš nsf. DNa 44.' — immediately followed by 'āršṭika- sb. ‚spearman‘: from aršti- ‚spear‘ with vṛddhi ... + suffix -ka-' and 'arštibara- sb. ‚spear-bearer‘: aršti- ‚spear‘ + bara- ‚bearer‘ ... DNc 2'. Exactly the page Nourai cites and exactly what his arrows claim (minus aštrā-).\"},\n      {\"ref\": \"TZF:31\", \"status\": \"not_checked\",\n       \"note\": \"Abolghasemi, Tārix-e Moxtaṣar-e Zabān-e Fārsi — refs_online.json records no scan or copy anywhere online (kind 'website', local_file null).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 263 f. s.v. aštrā- (BRT.txt ll.6488–6504)\", \"stance\": \"contradicts\",\n       \"note\": \"'j. aštrā- f. ‚Geisel, Peitsche, Knute‘' with Yt.10.113 'wenn laut die Peitsche knallt'; footnote: 'Zum V. az-; eig. ‚Vorrichtung zum Antreiben der Tiere‘ ... ai. aṣṭrā- f. ‚Stachelstock (zum Viehantreiben)‘'. Also col. 263 aštra-ḏhāū- 'mit der Peitsche lenkend'. No 'short spear' sense anywhere; the word belongs to az- 'drive', not to *eres- 'pierce'.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p.4, root aǣ5- 'treiben' (POK_01.txt leaf 12)\", \"stance\": \"contradicts\",\n       \"note\": \"'Als idg. Instrumentalnomen auf -trā hierher ai. aṣṭrā ,Stachel zum Viehantreiben‘, av. aštrā ,Peitsche, Geißel‘.' — aštrā- is Pokorny's, and everyone's, derivative of 'drive', not of 'pierce'.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent pp.172, 180 (KNT.txt leaves 195, 198) and §143.V\", \"stance\": \"supports\",\n       \"note\": \"p.180 s.v. u- 'good, well': the list of compounds includes 'uvārštika-'; §§ in the grammar quote DNb 44 'āršṭika amiy uvāršṭika ‚as battle-spearman I am a good spearman‘' and DNc 'arštibara' as Gobryas' title.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 20.26 SPEAR (SYN.txt l.34761 ff.)\", \"stance\": \"supports\",\n       \"note\": \"In the head table for 'spear': 'Skt. ṛṣti-; Av., OPers. aršti-'; §7 derives them from Skt. ṛṣ- 'push, thrust, stab, kill'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann p. ~20 s.v. arstis (IEC.txt leaf 35)\", \"stance\": \"supports\",\n       \"note\": \"'arstis (rstis) ‚spear, shaft‘ ... Skt. ṛṣtíh; Av., OPer. arštis; Oss. arc ...; (Iran. LW in Arm. ašte)' — confirms the Avestan/Old Persian pair but knows no aštrā- in this family.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"xešt 2 «خِشت ۲»\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP خشت xešt 'javelin, short throwing-spear' — Borhān-e Qāteʿ defines it as 'a small spear in the middle of which a loop of woven silk cord is tied; one puts the forefinger through the loop and hurls it at the enemy', and Nourai's Vis-o-Rāmin couplet ('چو شیر نر بر آن خوک دژم تاخت / سیه پر خشت پیچان را بینداخت') is quoted for exactly that sense by Nušin's Farhang-e Šāhnāme too. Moʿin's etymological footnote to that very Borhān entry — the reference Nourai cites — derives it from Old Indic ṛṣṭi 'spear', comparing Av. aršti- and OP aršti-, i.e. precisely Nourai's arrow; Wiktionary's Old Armenian ašteay ('short javelin', an Iranian loan from *aršti-) likewise lists Persian خشت 'javelin, dart, spear' as a member of the family. The reason for only 'plausible' is the initial x-: the regular New Persian outcome of OIr. aršti- is the arst that Horn (Grundriss no. 23) records from the Vendīdād Pahlavi ('arst ‚Speer, Lanze‘; ap. aw. aršti-'), and MacKenzie's Pahlavi dictionary knows xišt only as 'brick' (< OP išti-, Av. ištiia-, Horn no.488). The javelin word has therefore been remodelled on, or has fallen together with, the homophonous xešt 'brick' — a step no source spells out. The chart's own transliteration and Persian script are correct, and Nourai's '2' correctly separates it from xešt 1 'brick'.\",\n     \"derivation_fa\": \"«خِشت» در معنای نیزهٔ کوتاهِ پرتابی: معین در حاشیهٔ برهان قاطع همین ریشه‌شناسی را می‌آورد: «هندی باستانی ṛṣṭi (نیزه)، قس: اوستا aršti-، پارسی باستان aršti-». ویکی‌واژه نیز در مدخل ارمنی کهن ašteay «زوپین» (وام‌واژه‌ای ایرانی از *aršti-) «خشت» فارسی را هم‌خانواده می‌شمارد. با این حال «خ» آغازین تحول منظم نیست: بازتاب قاعده‌مندِ aršti- در فارسی همان arst است که هرن (شمارهٔ ۲۳) از وندیداد می‌آورد، و مکنزی در فرهنگ پهلوی تنها xišt «آجر» را دارد (از پارسی باستان išti-). پس به دیدهٔ احتیاط پذیرفتنی است: ریشه درست است ولی پیدایش «خ» آغازین را باید به همگونی با «خشت» هم‌آوای به معنای آجر نسبت داد.\",\n     \"sources\": [\n      W + \"%D8%AE%D8%B4%D8%AA\",\n      W + \"%D5%A1%D5%B7%D5%BF%D5%A5%D5%A1%D5%B5\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:751\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 208–209 (printed p. 748–749 by the file's +540 offset, 751–752 by the earlier +540±3 estimate — Nourai's 751 falls inside that band and lands on this very entry). Text: 'خشت ... بمعنی آجر خام و پخته را گویند ۱ - و نوعی از سلاح جنگ باشد و آن نیزهٔ کوچکی است که در میان آن حلقه‌ای از ریسمان ابریشم بافته بسته باشند و انگشت سبابه را در آن حلقه کرده بجانب خصم اندازند'; Moʿin's footnote 1 on that page reads (OCR, partly damaged) '۱ - هندی باستانی ṛṣṭi (نیزه)، قس: اوستا aršti-، پارسی باستان ...، پهلوی ...، ارمنی ...' — exactly the arrow Nourai draws. (The preceding page's footnote gives the separate brick etymology: 'پهلوی xišt، اوستا ištya-، سانسکریت iṣṭakā-'.)\"},\n      {\"ref\": \"TZF:31\", \"status\": \"not_checked\", \"note\": \"no copy of Abolghasemi's Tārix-e Moxtaṣar available (see refs_online.json).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FSF\", \"where\": \"Nušin, Farhang-e Šāhnāme s.v. خشت (با زیر اول) (FSF_pages.txt l.10460 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'نیزهٔ کوتاه که در میان آن حلقه‌ای از ابریشم یا ریسمان تافته ببندند و انگشت سبابه را در آن حلقه کرده، دست را تاب داده نیزهٔ کوتاه را بزور دست بسوی دشمن اندازند' — and it quotes the same Vis-o-Rāmin line Nourai prints ('چو شیر نر بر آن خوک دژم تاخت ...', marked ویس ۲۳-۴۹۹). Confirms the sense and the citation; gives no etymology.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 23 (p. ~2; HRN.txt l.10118)\", \"stance\": \"partial\",\n       \"note\": \"'23. arst ‚Speer, Lanze‘ (Vd. 14 (34)). ap. aw. aršti- ‚Speer, Lanze‘; ai. ṛṣṭi- ‚Speer‘.' Horn takes the Iranian spear word into Persian as arst, not as xešt — the same etymon, a different Persian shape.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt ll.1938, 9512)\", \"stance\": \"partial\",\n       \"note\": \"'xišt ‚Ziegel‘, phl. xišt = zd. ištya-' and 'Lies afgh. LW. xašta ‚Ziegel‘' — Hübschmann knows Persian خشت only in the 'brick' sense (< *ištya-); he does not treat the javelin homonym.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.94 s.v. xišt (PHD.txt)\", \"stance\": \"partial\",\n       \"note\": \"'xišt [hšt' | (P hyštyg), N ~] brick.' MacKenzie's Pahlavi lexicon has no xišt 'javelin', so the Middle Persian link in Nourai's chain is not documented there.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian and Latin indexes (incoming/ARY)\", \"stance\": \"silent\",\n       \"note\": \"grep 'خشت' in ARY_pages.txt returns only running-text mentions of clay tablets in the introduction; there is no headword entry for خشت.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 5,\n   \"root\": \"Es 2, Es-ti\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁es- 'to be' (1sg *h₁ésmi, 3sg *h₁ésti); participle *h₁s-ónt- 'being, true'\",\n   \"note\": \"Pokorny pp.340–342 s.v. 'es- ,sein‘, Kopula und Verbum Substantivum' is precisely the entry Nourai cites, and its three pages match his three page numbers: p.340–341 the paradigms (ai. ásmi, asti; av. ahmi, asti, həṅti; apers. amiy; lat. sum, est; got. im, ist), p.341–342 the participle 'senṭ-, sont-, sṅt- ,seiend‘, z. T. mit Entwicklung zu ,wahr, tatsächlich‘' (ai. sánt-, av. hant-, hat-; ai. satyá-, av. haiθya-, apers. hašiya-; lat. praesens, absens, sons) and, p.342, the ti-abstracts including 'ai. sv-asti- f. ,Wohlsein‘'. The chart's second head-form 'Es-ti' is Pokorny's own 3sg *esti, so the redirect 'Es-ti → Es 2' is correct. Nourai's root gloss, language label and the whole set of daughter forms are standard; his branch structure follows Watkins/AHD s.v. es- almost item for item.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *h₁es- «بودن» (در پوکورنی صفحات ۳۴۰–۳۴۲ زیر es- ,sein‘) که هم فعل اسنادی است و هم فعل وجودی. همان سه صفحه‌ای که نورایی ارجاع داده به ترتیب صرف فعل (اوستایی ahmi، asti، həṅti؛ پارسی باستان amiy)، اسم فاعل *sent-/*sont- و تحول معنایی آن به «راست، واقعی» (اوستایی hant-/hat- و haiθya-، پارسی باستان hašiya-، لاتین praesens/absens/sons) و سرانجام مصدرهای -ti مانند سنسکریت sv-asti- را در بر می‌گیرد. صورت دوم عنوان (Es-ti) همان سوم‌شخص مفرد *esti است. ادعای نورایی دربارهٔ ریشه پذیرفتنی و مطابق با پوکورنی، والده–پوکورنی، واتکینز و باک است.\",\n   \"sources\": [\n    W + \"Reconstruction:Proto-Indo-European/h%E2%82%81es-\",\n    \"https://www.etymonline.com/word/essence\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"POK:340,341,342\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaves 354–356 carry the running numbers 341 and 342 and hold the entry that begins 'es- ,sein‘, Kopula und Verbum Substantivum; bildet ursprünglich nur ein duratives Präsens ...' immediately under the '340' catch-number on leaf 353. All three cited pages are the one article, and its content is what the chart draws.\"},\n    {\"ref\": \"IEC:254\", \"status\": \"partial\",\n     \"note\": \"Mann's *es- articles run over IEC pp.249–255 (IEC.txt leaves 150–153): 'es- (radical ‚be‘) See following entries' on p.249, 'esmi (es-si, es-ti) ‚am‘ ... Skt. ásmi; Av. ahmi; OPer. amiy; Per. am' on p.251, 'esti ‚is‘ ... Skt. ásti; Av. asti; Per. ast' and 'est- (1) ... cf. Skt. sv-astih ‚wellbeing‘ (*su-est-)' on p.253, and esus (2)/(3) on pp.254–255. The material is all there but is spread over pp.249–255 rather than sitting on p.254 alone.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 160 f. s.v. es- „sein“ (incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt l.10418 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'es- „sein“. Ai. asmi, asti „bin, ist“, av. ahmi, asti, ap. amiy, arm. em ... got. im, ist ... Ptc. *sent-, sont- „seiend“, z. T. m. Entw. zu „wahr, tatsächlich“ ... ai. satya- „wahr, recht“, av. haiθya- „wirklich“, ap. hašiya- ds.' — every Iranian form on Nourai's chart.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. es- (AHD_watkins1985.txt l.460)\", \"stance\": \"supports\",\n     \"note\": \"'es-. To be. 1. ... *es-mi in Germanic *izm(i) in Old English eam, eom, am: AM. 2. ... *es-ti in: a. Germanic *ist(i) ... is; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie ... yes: YES. ... 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, INTEREST, PRESENT, PROUD ... [Pok. es- 340.]' — Nourai's Germanic, English and Latin boxes are a transcript of this entry.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 9.91 BE (SYN.txt l.15985 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'1. IE *es-, weak grade *s- ... Skt. as-, 1sg. asmi, 3sg. asti, Av. ah-, 1sg. ahmi, 3sg. asti; Hitt. es- ...' with the Latin, Germanic, Baltic and Slavic paradigms.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Avestan\",\n     \"words\": \"ahmi; asti; hant, hat; haithya\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Av. ahmi 'I am' < PIIr. *asmi < PIE *h₁és-mi, with the regular Iranian change of intervocalic/pre-nasal *-sm- to -hm- (Skt. ásmi keeps the sibilant); Av. asti 'is' = PIE *h₁és-ti unchanged (Skt. ásti, Gk. ἐστί, Lat. est). hant-/hat- is the present participle *h₁s-ónt-/*h₁s-ṇt- 'being' (Skt. sánt-/sat-, Gk. ἐόντ-, Lat. -sent- in praesens): initial *s- before a vowel becomes h- in Iranian, and the zero-grade oblique stem gives hat-. Its semantic drift 'being > real > true' is the same one Pokorny documents for Germanic *sanþa- (OE sōð 'true') and Latin sons 'guilty'. Av. haiθya- 'true' is the -ya- adjective *h₁s-ṇt-yó- (Skt. satyá-, OP hašiya-), Iranian *-ty- > Av. -θy-. So all four forms and the arrow from the root are correct; Nourai's 'haithya' is the usual ASCII rendering of haiθya-.\",\n     \"derivation_fa\": \"اوستایی ahmi «هستم» از هندوایرانی *asmi و آن از *h₁és-mi است؛ در ایرانی خوشهٔ -sm- به -hm- بدل شده (سنسکریت آن را نگاه داشته: ásmi). asti «هست» عیناً همان *h₁és-ti است. hant-/hat- اسم فاعل حال (*h₁s-ónt-) است که س‌ آغازین در ایرانی به ه‌ بدل شده و معنای «بودنده» > «راست، واقعی» گرفته است. haiθya- «راست» صفتی است با پسوند -ya- (سنسکریت satyá-، پارسی باستان hašiya-) که -ty- ایرانی در اوستایی به -θy- بدل می‌شود. هر چهار صورت درست است و ادعای نورایی پذیرفته می‌شود.\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81es-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:340\", \"status\": \"supports\",\n       \"note\": \"Pokorny p.340: 'Ai. ásmi, ási, ásti, smás, sthá, sánti, av. ahmi, 3. Sg. asti, 3. Pl. həṅti, apers. amiy'; p.341: 'Ai. sánt- sát- ... ,seiend, gut, wahr‘, av. hant-, hat- ds.'; p.341 f.: 'ai. satyá- ,wahr, recht‘ ..., av. haiθya- ,wahr, echt‘, apers. hašiya- ds.'\"},\n      {\"ref\": \"KNT:214\", \"status\": \"partial\",\n       \"note\": \"The local Kent OCR (KNT.txt, 232 leaves) breaks off in the lexicon at 'vaj- vb.' ≈ p.208, so the cited p.214 (the h- letter, where hašiya- stands) cannot be read. What is readable fully supports the claim: Kent p.174 's.v. ah- vb. ‚be‘: Av. ah-, Skt. as-, Gk. ἐστί, Lt. est, Gt. ist, pIE *es-. See also hašiya-, Hašiyā-baušna-' with 'amiy 1st sg., Av. ahmi', 'astiy, Av. asti, NPers. āst', 'haṅtiy 3d pl., Av. hənti'; and §162 (p. ~72) 'the derivative hašiya- ‚true‘, = Skt. satyá-, pIE *sṇt-yo-, where (Skt.) sát is nt. pte. to root as- ‚be‘'.\"},\n      {\"ref\": \"IEC:254\", \"status\": \"partial\",\n       \"note\": \"Mann has 'esmi ... Av. ahmi', 'esti ‚is‘ ... Av. asti' and 'eənt (senti ...) ‚are‘ ... Av. həñtī' on pp.251–253, one to three pages before the cited 254.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. ah- / haiθya- (BRT.txt, grepped 'ahmi', 'wirklich', 'haiθya')\", \"stance\": \"not_found\",\n       \"note\": \"The scan's OCR is too corrupt in the h- and a- verb columns to isolate the headwords: 'ahmi' returns only running quotation text (ll.2454–2476) and no grep spelling of haiθya- matches. Bartholomae was readable for aštrā- (col. 263) but not here.\"},\n      {\"src\": \"WLD\", \"where\": \"WP I 160 f.\", \"stance\": \"supports\",\n       \"note\": \"'av. ahmi, asti ... av. hant-, hat- ... av. haiθya- „wirklich“' — the same four forms.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 9.91 (SYN.txt l.16000)\", \"stance\": \"supports\",\n       \"note\": \"'Av. ah-, 1sg. ahmi, 3sg. asti'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"astan «استن»; ast 1 «است ۱»; -am «-آم»\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The etymology is right and the Persian script of the third word is wrong. NP است ast 'is' continues MP ast (MacKenzie: 'ast [AYT' < Aram. ʾyty | M ʾst, N ~] is, exists'), from OP astiy = Av. asti < PIE *h₁ésti; Kent notes the New Persian outcome under his OP astiy. The enclitic first person -am 'I am' continues MP -ēm/-am < OIr. *ahmi (Av. ahmi, OP amiy) with loss of the final vowel and reduction of the unstressed syllable; Mann prints it simply as 'Per. am' beside Av. ahmi. استن astan is a lexicographers' back-formed infinitive to that copula: Dehxodā s.v. استن has '(مص) هستن ... استم، استی، است، استیم، استید، استند', explicitly a hypothetical infinitive, with the reduced series 'ام، ای، است، ایم، اید، اند' — so the form exists in the dictionaries but is a grammarians' citation form, not a classical infinitive. THE FLAG: the book prints the Persian script of the third word as «ـ آم», with an alef-madda; the Persian enclitic is «ـَم», written «ام» only after a vowel-final word (تشنه‌ام), never «آم» (which would be read ām). I rendered pdf page 161 at 600 dpi and read the box: the madda is unmistakably there, so the JSON is a faithful copy and the misprint is Nourai's own. Verdict for the node is the worst of its words.\",\n     \"derivation_fa\": \"ریشه‌شناسی درست است ولی املای فارسی واژهٔ سوم غلط است. «است» از فارسی میانهٔ ast، از پارسی باستان astiy و اوستایی asti است (مکنزی: ast «هست، وجود دارد»). شناسهٔ «ـَم» دنبالهٔ *ahmi ایرانی باستان است (من پایانی افتاده و هجای بی‌تکیه کوتاه شده). «استن» مصدری است که فرهنگ‌نویسان از روی صرف فعل ربطی ساخته‌اند؛ دهخدا آن را «(مص) هستن» می‌نامد و صرف «استم، استی، است...» را می‌آورد. امّا کتاب شناسهٔ اول‌شخص را «ـ آم» با الف ممدود چاپ کرده که نادرست است؛ صورت درست «ـَم» (و پس از واکه «ام») است. تصویر صفحهٔ ۱۶۱ با دقت ۶۰۰ دی‌پی‌آی خوانده شد و مدّ روی الف آشکار است؛ پس خطای چاپی کتاب است، نه خطای خوانش اسکن.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"ـ آم\",\n     \"correct_form\": \"ـَم (after a vowel: ام)\",\n     \"sources\": [\n      \"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%AA%D9%86/\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"IEC:250,254\", \"status\": \"partial\",\n       \"note\": \"Mann p.251 s.v. esmi: 'Skt. ásmi; Av. ahmi; OPer. amiy; Per. am; Hitt. esmi ...' — exactly Nourai's '-am'; p.253 s.v. esti: 'Skt. ásti; Av. asti; Per. ast' — exactly his 'ast 1'. The pages are 251 and 253, one page off each of the two cited numbers; Mann has no Persian infinitive astan.\"},\n      {\"ref\": \"MON:260,345\", \"status\": \"partial\",\n       \"note\": \"Moʿin's lexicon, checked via abadis (فرهنگ معین s.v. استن), gives استن only as 'ستون' (pillar) and as the chemical acetone — not as the copula. The copula infinitive is Dehxodā's: 'استن [اَ تَ] (مص) هستن ... استم، استی، است، استیم، استید، استند' with the reduced set 'ام، ای، است، ایم، اید، اند'. The cited Moʿin pages (vol. 1, pp. 260/345) are in the ا range and plausibly hold است/استن, but the print volumes are not online, so the exact pages could not be read.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.12 s.v. ast (PHD.txt)\", \"stance\": \"supports\",\n       \"note\": \"'ast [AYT! < A ʾyty | M ʾst, N ~] is, exists. ~ih: existence.' — Middle Persian ast continued unchanged as NP ast, the link Nourai's arrow needs.\"},\n      {\"src\": \"KNT\", \"where\": \"Kent p.174 s.v. ah- 'be'\", \"stance\": \"supports\",\n       \"note\": \"'astiy, Av. asti, NPers. āst, Skt. ásti' — Kent himself carries the chain down to New Persian.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II s.v. hast/ast (NYB_vol2_glossary.txt)\", \"stance\": \"partial\",\n       \"note\": \"The glossary's entries turn on būdan/hast; 'ast' appears as 'ast [ʾst'] the bones ... Av. ast-' (a homonym, 'bone'), and *hast is cited only inside the discussion of anāst 'nothingness ... from the neg. pref. + *hast'. It attests MP hast/ast as the copula but has no separate headword for it.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Latin index p.528 (ARY_latin_index_pages.txt l.15407)\", \"stance\": \"partial\",\n       \"note\": \"The index lists 'ESMI, ESHZI (HITTITE)' pointing into the Persian entry for this family, so Aryanpur treats *es- with Persian reflexes, but the Persian headword page was not fetched.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Old Persian\",\n     \"words\": \"amiy; hašiya\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OP amiy 'I am' (written a-mi-y) < *ahmi < PIE *h₁ésmi: Old Persian regularly loses the h of the cluster *-hm-, so Avestan ahmi : OP amiy (Kent §118.II, §226.I); it is the commonest word in the royal inscriptions ('adam Dārayavaʳuš xšāyaθiya amiy'). OP hašiya- 'true' is *h₁s-ṇt-yó-, the -ya- adjective to the participle, Skt. satyá-, Av. haiθya-; Old Persian *θy > šiy (§104), whence hašiya, e.g. DB 4 'this is true, not false'. Both forms and the direct arrow from the root are correct; the empty box drawn to the right of this node on the printed page carries no language, no reference and no word, and is a layout filler, not a derivation.\",\n     \"derivation_fa\": \"پارسی باستان amiy «هستم» از *ahmi و آن از *h₁ésmi است؛ در پارسی باستان ه‌ در خوشهٔ -hm- می‌افتد پس اوستایی ahmi برابر amiy است (کنت §۱۱۸). hašiya- «راست» همان *h₁s-ṇt-yó- است (سنسکریت satyá-، اوستایی haiθya-) که در پارسی باستان *θy به شی‌ بدل می‌شود. هر دو صورت درست است. (جعبهٔ خالی روبه‌روی این گره در چاپ کتاب نه زبان دارد نه واژه؛ تنها آرایهٔ صفحه‌آرایی است.)\",\n     \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%81es-\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:340,341\", \"status\": \"supports\",\n       \"note\": \"p.340 'apers. amiy'; p.341 f. 'apers. hašiya- ds. [= wahr, echt]'.\"},\n      {\"ref\": \"KNT:214\", \"status\": \"partial\",\n       \"note\": \"p.214 (the h- section, holding hašiya-) is past the end of the local OCR, but Kent p.174 s.v. ah- lists 'amiy 1st sg., Av. ahmi, Skt. ásmi ... AmH 9; DB 1.12 ...' and 'See also hašiya-', and §162 states 'the derivative hašiya- ‚true‘, = Skt. satyá-, pIE *sṇt-yo-'. §115/§117 also give 'OP hasiyam ‚true‘, Skt. satyám'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Kent §115 and p.174 (KNT.txt ll.1107, 1456, 5127 ff.)\", \"stance\": \"supports\",\n       \"note\": \"'OP amiy ‚I am‘, LAv. ahmi, Skt. ásmi, from pIE *esmi' and 'OP hasiyam ‚true‘, Skt. satyám'.\"},\n      {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon (TLM.txt, grep 'amiy')\", \"stance\": \"supports\",\n       \"note\": \"The text volume prints the Behistun passages with amiy ('adam ... amiy hya Kuraus puθra Kanbujiya...'), attesting the form Nourai gives.\"},\n      {\"src\": \"WLD\", \"where\": \"WP I 160 f.\", \"stance\": \"supports\",\n       \"note\": \"'ap. amiy' in the paradigm list, and 'ap. hašiya- ds.' beside av. haiθya-.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Germanic\",\n     \"words\": \"izmi; isti; sijai\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"These are Watkins's Proto-Germanic reconstructions, copied from the AHD appendix: *izm(i) 'am' from athematic *h₁es-mi with Verner-voicing of *s > *z before the resonant, *ist(i) 'is' from *h₁és-ti, and the optative stem *sijē/ai- from PIE *h₁s-ih₁- (the *si- optative of Pokorny's 'Optat. ved. s(i)yām, gr. εἴην, lat. siem, sies, siet ... ahd. 3. Sg. sī'). Nourai's glosses ('am', 'is', 'may it be so, yes') are Watkins's own. The one loose point is that 'yes' is glossed at the Germanic node although the yes-form itself is West Germanic (OE gēse/gīese = gēa 'yea' + sī(e) 'may it be'), which the chart in fact handles by putting 'yes' in the English box below.\",\n     \"derivation_fa\": \"این سه صورت، بازسازی‌های ژرمنی آغازین‌اند که عیناً از پیوست ریشه‌های واتکینز (AHD) گرفته شده: *izm(i) از *h₁es-mi با واک‌شدن s > z بنا به قانون ورنر، *ist(i) از *h₁és-ti، و ستاک التزامی *sijai- از *h₁s-ih₁- (هم‌ریشه با لاتین siem و یونانی εἴην). معناهایی که نورایی می‌دهد همان معناهای واتکینز است. ادعا درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. es-: '1. Athematic first person singular form *es-mi in Germanic *izm(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Germanic *ist(i) in Old English is, is: IS ... 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gēse (gēa, yea; see i- + sie), yes: YES.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p.340–341\", \"stance\": \"supports\",\n       \"note\": \"'got. im, is, ist, 3. Pl. sind (*senti); aisl. em, est (ert), es (er); ags. eom ..., northumbr. am (*os-m)' and 'Optat. ... ahd. 3. Sg. sī'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 9.91\", \"stance\": \"supports\",\n       \"note\": \"'Gmc. 3sg. Goth., OHG-NHG ist, OE-NE is, ON, Dan. er, Sw. är'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"am; is; yes\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"OE eam/eom (Anglian am) > ModE am; OE is > is; OE gēse/gīese > ME yis/yes > yes. The last is a compound, not a simple reflex: gēa 'yea' + the optative sī(e) 'may it be (so)', literally 'yea, may it be so' — which is why Nourai glosses the Germanic optative *sijai as 'may it be so, yes'. AHD puts all three under es- exactly as the chart does; the strong-verb suppletion of English 'be' (be/was from *bheu- and *wes-) is not at issue because only the *es- members are listed here.\",\n     \"derivation_fa\": \"am از انگلیسی کهن eom/eam، is از is و yes از gēse/gīese می‌آید. واژهٔ اخیر مرکّب است: gēa «آری» + sī(e) «باد، باشد»، یعنی «آری، چنین باد»؛ پس معنایی که نورایی برای sijai آورده («may it be so, yes») دقیق است. ادعا درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. es-: 'Old English eam, eom, am: AM'; 'Old English is, is: IS'; 'Old English sie, may it be (so) in gēse (gēa, yea; see i- + sie), yes: YES'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SYN\", \"where\": \"Buck 9.91 (SYN.txt l.15985)\", \"stance\": \"supports\",\n       \"note\": \"The paradigm table gives 'OE wesan, bēon, bēo(m), is, wes / ME be(n), is, was / NE be, is, was' — English is belongs to *es-.\"},\n      {\"src\": \"POK\", \"where\": \"Pokorny p.341\", \"stance\": \"supports\",\n       \"note\": \"'ags. eom (nach bēom), northumbr. am (*os-m), eart ...; is; 3. Pl. northumbr. aron (*os-nt)'.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Latin\",\n     \"words\": \"esse\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin esse 'to be' is the athematic infinitive of *h₁es-: 2sg es(s), 3sg est = PIE *h₁ésti; the 1sg sum is analogical on the 1pl sumus (Pokorny: 'lat. sum (durch Einfluß der 1. Pl.), es(s), est'), and the inchoative escit matches Greek ἔσκω. The infinitive esse was later remade in Vulgar Latin as *essere on the model of legere, which is why the Romance infinitives are It. essere, Fr. être, Sp. ser (Buck 9.91). Watkins lists esse as the source of the English words in nodes #9 and #10.\",\n     \"derivation_fa\": \"مصدر لاتین esse «بودن» صورت بی‌میانجی ریشهٔ *h₁es- است؛ est دقیقاً همان *h₁ésti است و sum به قیاس از sumus ساخته شده (پوکورنی ص ۳۴۰). در لاتین عامیانه مصدر به *essere دگرگون شد که منشأ مصدرهای رومانیایی (ایتالیایی essere، فرانسوی être) است. ادعا درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. es-: '5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT¹, (PRESENT²), PROUD, (QUINTESSENCE), (REPRESENT).'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p.340\", \"stance\": \"supports\",\n       \"note\": \"'lat. sum (durch Einfluß der 1. Pl.), es(s), est (Inchoat. escit, wie gr. ἔσκω), sumus, estis, sunt'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 9.91\", \"stance\": \"supports\",\n       \"note\": \"'Lat. esse, sum, est, etc., with Romance pres. forms; infin. esse > VLat. *essere after legere, etc., hence It. essere, Fr. être, Sp. ser'.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box: Nourai routes the two words below (Persian esâns, English essence) through French rather than straight from Latin, and rightly so. The French link is Old French essence (12th c.), a learned borrowing of Latin essentia; the modern French noun essence carries both the philosophical sense and, from the 17th–18th c. perfumers' and chemists' usage, 'volatile extract, distilled oil', and it is that later sense that both descendants below inherit. No word is printed in the box and none is needed.\",\n     \"derivation_fa\": \"این جعبه تهی است و تنها نقش واسطه دارد: نورایی دو واژهٔ پایین («اسانس» فارسی و essence انگلیسی) را از راه فرانسه می‌برد که درست است: فرانسوی کهن essence (سدهٔ ۱۲م) وام‌واژه‌ای عالمانه از لاتین essentia است و معنای «عصارهٔ فرّار» در سده‌های ۱۷–۱۸ میلادی بر آن افزوده شده است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"Watkins lists ESSENCE under Latin esse without naming the French stage; the French intermediary is supplied by Klein and Etymonline (see 'consulted' on node #9).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. essence (KLN_1966.txt)\", \"stance\": \"supports\",\n       \"note\": \"'essence, n. — F., fr. L. essentia, ‚being or essence of a thing‘' — Klein routes it through French exactly as the chart does.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Persian\",\n     \"words\": \"esâns «اسانس»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP اسانس esāns 'essence, essential oil, perfume base' is a 19th–20th-century loan from French essence [esɑ̃s], taken in through the chemistry/perfumery vocabulary that entered Persian with the Dār al-Fonūn and the pharmaceutical trade; the Persian spelling اسانس renders the French nasal vowel with -ان- and the final -s of the French spelling is pronounced, as usual in such loans. Moʿin's dictionary tags it [فر.] '(French)' and defines it 'جوهر و عصارهٔ گل‌ها و گیاهان، عطرمایه' — the borrowed sense being the later French 'volatile extract', not the philosophical 'essence'. Nourai's arrow (French → Persian) and gloss are right.\",\n     \"derivation_fa\": \"«اسانس» وام‌واژه‌ای نو از فرانسوی essence است که از راه زبان شیمی و عطرسازی در دورهٔ قاجار وارد فارسی شده است؛ واکهٔ خیشومی فرانسه در فارسی با «ان» نوشته می‌شود. معین آن را با نشانهٔ [فر.] می‌آورد و «جوهر و عصارهٔ گل‌ها و گیاهان، عطرمایه» معنی می‌کند. پس ادعای نورایی درست است، هرچند معنای وام‌گرفته همان معنای متأخر فرانسوی (عصارهٔ فرّار) است نه معنای فلسفی آن.\",\n     \"sources\": [\"https://abadis.ir/fatofa/%D8%A7%D8%B3%D8%A7%D9%86%D8%B3/\"],\n     \"ref_check\": [\n      {\"ref\": \"VOP:43\", \"status\": \"not_checked\",\n       \"note\": \"Moširi, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (Alborz 1371) — refs_online.json records 'kind: none': no scan, no ebook, no catalogue record with a copy; re-searched 2026-09 with nothing found.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.v. اسانس (via abadis.ir)\", \"stance\": \"supports\",\n       \"note\": \"'[فر.] جوهر و عصارهٔ گل ها و گیاهان، عطرمایه' — Moʿin's own origin tag is French. The local OCR (MON_part1.txt l.10896) shows the same entry, 'اسانس: [فر.] جوهر گل‌ها و گیاهان که بصورت عطر استخراج شود', with the tag damaged by OCR.\"},\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. essence\", \"stance\": \"supports\",\n       \"note\": \"'essence, n. — F., fr. L. essentia' — confirms that the immediate donor of the modern international word is French.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"essence\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English essence is attested from the late 14th c., borrowed from Old French essence, itself from Latin essentia 'being, essence' — an abstract noun in -ia built on essent-, the (artificial) present participle stem of esse, coined as a calque of Greek οὐσία (Klein: 'prop. loan translation of Gk. oὐσία'). It first meant 'true being, substance' in Trinitarian theology, broadened to 'basic element of anything' by the 1650s, and from c.1600 acquired the perfumers' sense 'ingredient which gives something its character', hence 'distilled plant oil'. Nourai's Latin → French → English route is the standard one.\",\n     \"derivation_fa\": \"essence انگلیسی از پایان سدهٔ ۱۴م میلادی از فرانسوی کهن essence وام گرفته شده و آن از لاتین essentia است؛ essentia اسم معنایی از ستاک essent- (اسم فاعل ساختگیِ esse) است که به تقلید از یونانی οὐσία ساخته شد. معنای نخستین آن کلامی بود، سپس به «عنصر اصلی» و سرانجام به «عصارهٔ معطر» گسترش یافت. مسیری که نورایی رسم کرده همان مسیر معیار است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. es-, §5: 'Latin esse, to be: ENTITY, ESSENCE ...'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein, CEDEL s.v. essence (KLN_1966.txt)\", \"stance\": \"supports\",\n       \"note\": \"'essence, n. — F., fr. L. essentia, ‚being or essence of a thing‘, fr. essent-, pres. part. stem of esse, ‚to be‘; prop. loan translation of Gk. oὐσία, ‚essence‘. See esse ...'\"},\n      {\"src\": \"WEB/etymonline\", \"where\": \"etymonline.com/word/essence\", \"stance\": \"supports\",\n       \"note\": \"'late 14c., from Latin essentia ‚being, essence‘, abstract noun from essent-, present participle stem of esse ‚to be‘, from PIE root *es- ‚to be‘'; the perfumery sense c.1600.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"English\",\n     \"words\": \"absent, interest, present, entity, proud\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All five are Latin *es- words, and Watkins lists precisely this set under the root. absent ← Lat. absent-, participle of abesse 'to be away' (ab- + esse); present ← praesent-, participle of praeesse 'to be before'; interest ← Lat. interest 'it makes a difference, it concerns', 3sg of interesse (inter- + esse), taken into English through Anglo-French interesse as a legal term for a stake in property; entity ← Late Lat. entitas, built on ens/entis, an artificial present participle of esse coined by medieval philosophers to translate Greek τὸ ὄν. proud is the least obvious and the most interesting: OE prūd/prūt is an early borrowing of Old French prud, the oblique of prouz 'brave, valiant', from Late Latin *prodis, extracted from Latin prod-est 'is useful' — so the *es- root sits in the second element (cf. proud/prowess/prude). Pokorny p.341 independently gives 'lat. in praesens, -sentis ,gegenwärtig‘ ... ab-sens ,abwesend‘' from the participle *sont-.\",\n     \"derivation_fa\": \"هر پنج واژه از راه لاتین به انگلیسی رسیده‌اند: absent از absent- (اسم فاعل abesse)، present از praesent-، interest از فعل interest (سوم‌شخص interesse) که از راه فرانسهٔ آنگلونورمن و به‌عنوان اصطلاح حقوقی وارد شد، entity از entitas لاتین متأخر (بر پایهٔ ens/entis که فیلسوفان قرون وسطا برای برگردان τὸ ὄν ساختند)، و proud که از همه دورتر می‌نماید: انگلیسی کهن prūd وام‌واژه‌ای است از فرانسوی کهن prud از *prodis لاتینی که خود از prod-est «سودمند است» جدا شده؛ پس ریشهٔ *es- در جزء دوم آن است. فهرست نورایی عیناً همان فهرست واتکینز است و درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/essence\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"Watkins s.v. es-, §5: 'Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT¹, (PRESENT²), PROUD, (QUINTESSENCE), (REPRESENT)' — Nourai's five words are a subset of this list, in Watkins's own order.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p.341\", \"stance\": \"supports\",\n       \"note\": \"Under the participle *sent-/sont-: 'lat. in praesens, -sentis ,gegenwärtig‘, osk. praesentid ,praesente‘, ab-sens ,abwesend‘; sōns, Gen. sontis ,schuldig‘.'\"},\n      {\"src\": \"WEB/etymonline\", \"where\": \"etymonline.com/word/essence (root cross-references)\", \"stance\": \"supports\",\n       \"note\": \"The page lists proud, entity, interest, absent and present among the words from PIE *es-.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"asti; su-asti, svasti\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Skt. ásti 'is' is PIE *h₁ésti with no change at all (Av. asti, Gk. ἐστί, Lat. est). sv-asti- f. 'well-being, good fortune' is su- 'good, well' (PIE *h₁su-, Av. hu-, OP u-/uv-, Nourai's Su 1) + -asti-, a ti-abstract to the same root, literally 'good being'; Pokorny notes at p.342 that this ti-abstract is 'wohl ar. Neubildung' — i.e. formed inside Indo-Iranian rather than inherited whole, which does not affect the derivation from *h₁es-. The sandhi form svasti- with the glide is the one used in the Vedic benediction svàsti (RV), whence the adjective/derivative svāstika-. Nourai's two words, gloss and cross-reference to Su 1 are all correct.\",\n     \"derivation_fa\": \"سنسکریت ásti «هست» دقیقاً همان *h₁ésti است. sv-asti- «بهزیستی، نیک‌بختی» مرکّب است از su- «خوب» (همان که در اوستایی hu- و پارسی باستان u-/uv- دیدیم) و -asti- که اسم معنایی با پسوند -ti- از همین ریشه است؛ پوکورنی (ص ۳۴۲) یادآور می‌شود که این ساخت احتمالاً نو‌ساختهٔ هندوایرانی است، و این از درستی انتساب آن به ریشهٔ *h₁es- نمی‌کاهد. ادعای نورایی درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/swastika\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:254\", \"status\": \"partial\",\n       \"note\": \"Mann p.253 s.v. est- (1): 'cf. Skt. sv-astih ‚wellbeing‘ (*su-est-)'; p.253 s.v. esti: 'Skt. ásti'. Both are on 253, one page before the cited 254.\"},\n      {\"ref\": \"AHD:1298\", \"status\": \"not_checked\",\n       \"note\": \"AHD:1298 is a page of the main dictionary text of the 1975/76 New College Edition (the IE appendix is pp.1505–1550); the local copy is Watkins's 1985 standalone Roots volume, which has no such pagination. What is checkable — Watkins s.v. es-, '2b. Sanskrit asti, is: SWASTIKA' — supports the chart.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"Pokorny p.342\", \"stance\": \"supports\",\n       \"note\": \"Among the ti-abstracts: 'ai. abhi-sti- f. ,Hilfe‘ ...; ai. úpa-sti- m. ,Untergebener‘ (ai. sv-asti- f. ,Wohlsein‘ wohl ar. Neubildung)'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 9.91\", \"stance\": \"supports\",\n       \"note\": \"'Skt. as-, 1sg. asmi, 3sg. asti' — the Sanskrit copula belongs to *es-.\"}\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"swastica, swastika\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English swastika (also spelt swastica in 19th-c. archaeological writing) is a direct borrowing of Sanskrit svāstika-/svastika- 'a thing conducive to well-being, an auspicious mark', from svasti- 'well-being' (su- + asti-, node #11); it entered English through Indological and archaeological usage in the 1870s–80s (Schliemann's Troy reports popularised it) and by 1932 was the ordinary English name of the National Socialist emblem, which German itself calls Hakenkreuz 'hook-cross' (so Klein). Nourai's gloss is broadly right but the date needs qualifying: the NSDAP adopted the symbol on its party flag in 1920, and 1935 is the year of the Reich Flag Law that made the swastika banner the national flag of Germany — which is presumably what Nourai means by 'adopted in 1935 as an emblem of Nazi Germany'.\",\n     \"derivation_fa\": \"swastika انگلیسی وام‌واژه‌ای مستقیم از سنسکریت svastika- «نشان خجسته» است که خود از svasti- «بهزیستی» ساخته شده و در دههٔ ۱۸۷۰ میلادی از راه هندشناسی و باستان‌شناسی به انگلیسی راه یافته است. دربارهٔ تاریخی که نورایی می‌آورد باید دقیق شد: حزب نازی این نشان را در ۱۹۲۰ بر پرچم حزبی نهاد و سال ۱۹۳۵ سالی است که قانون پرچم رایش آن را پرچم رسمی آلمان کرد. جز این نکته، ادعا درست است.\",\n     \"sources\": [\"https://www.etymonline.com/word/swastika\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1298\", \"status\": \"partial\",\n       \"note\": \"The cited page belongs to the 1975/76 New College Edition's main text (its dictionary entry for 'swastika'), which is not in the local library. Watkins's appendix, which is, says 'Sanskrit asti, is: SWASTIKA' under es- — the same claim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"Klein s.v. swastika (KLN_1966.txt)\", \"stance\": \"supports\",\n       \"note\": \"Klein has 'swastika; used as the emblem of Nazism. — G. Hakenkreuz, lit. ‚hook-cross‘' in the German cross-reference, confirming the Nazi-emblem use and the German name.\"},\n      {\"src\": \"WEB/etymonline\", \"where\": \"etymonline.com/word/swastika\", \"stance\": \"supports\",\n       \"note\": \"'Sanskrit svastika-s, literally ‚being fortunate‘, from svasti-s ‚well-being, luck‘, from su- ‚well‘ ... + as-, root of asti ‚(he) is‘'; the Nazi-emblem sense 'by 1932'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nimport io, os\np = \"/home/sfmqrb/git/rishe/data/verification/page-161.json\"\nwith io.open(p, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", p, os.path.getsize(p))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build161.py"
}
```


### [2026-09-05T20:55:15.080Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-161.json 58731
```


## [2026-09-05T20:55:19.657Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-161.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 161"
}
```


### [2026-09-05T20:55:21.645Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'disputed': 1, 'plausible': 1, 'confirmed': 11, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 9, 'supports': 9, 'not_checked': 4}
books consulted: {'contradicts': 2, 'supports': 28, 'partial': 5, 'silent': 1, 'not_found': 1} | by book: {'POK': 6, 'SYN': 6, 'KLN': 4, 'KNT': 3, 'WEB/etymonline': 3, 'BRT': 2, 'PHD': 2, 'ARY': 2, 'WLD': 2, 'IEC': 1, 'FSF': 1, 'HRN': 1, 'HUB': 1, 'NYB': 1, 'TLM': 1, 'MON': 1}
```


## [2026-09-05T20:55:27.639Z] TOOL CALL #76: Bash

```json
{
 "command": "grep -o \"aǣ5-\" data/verification/page-161.json | wc -l && python3 - <<'EOF'\nimport io\np=\"/home/sfmqrb/git/rishe/data/verification/page-161.json\"\ns=io.open(p,encoding=\"utf-8\").read()\ns=s.replace(\"*h₂eǣ5-\",\"*h₂eǵ-\").replace(\"aǣ5-\",\"aǵ-\")\nio.open(p,\"w\",encoding=\"utf-8\").write(s)\nEOF\ngrep -o \"aǵ-\" data/verification/page-161.json | head; python3 -m json.tool data/verification/page-161.json >/dev/null && echo OK && python3 tools/verify_check.py 161 | head -3"
}
```


### [2026-09-05T20:55:29.973Z] TOOL RESULT

```
4
aǵ-
aǵ-
aǵ-
aǵ-
OK
nodes verified: 14/14
node verdicts: {'disputed': 1, 'plausible': 1, 'confirmed': 11, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
```


## [2026-09-05T20:55:47.764Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-161.json` written, valid JSON, `verify_check.py 161` shows **0 PROBLEM lines** (14/14 nodes, 2 roots).

**Page 161 (book p.131) — verdicts**
- Roots: 2 confirmed (Eres 2 = Pokorny 335 "1. eres- stechen"; Es 2/Es-ti = Pokorny 340–342 "es- sein"). 5 redirects skipped.
- Nodes: 11 confirmed, 1 plausible, 1 disputed, 1 transcription_suspect.
- Ref checks: 9 supports, 9 partial, 4 not_checked (TZF and VOP have no copy anywhere; KNT:214 and AHD:1298 fall outside the local scans).

**Flagged items**
- `disputed` — Eres 2 #1, Avestan/OP **aštrâ 2** "a short spear": Bartholomae col. 263 glosses Av. aštrā- 'whip, scourge', from the verb az- 'drive' ("Vorrichtung zum Antreiben der Tiere"), and Pokorny himself puts av. aštrā / skt. aṣṭrā under aǵ- 'treiben' on p.4 — not under eres- 'pierce' on p.335. aršti-, aršti-bara- and uvāršṭika- in the same box are fully confirmed by Kent p.172/p.180 (DNa 44, DNc 2, DNb 44).
- `transcription_suspect` — Es 2 #2, Persian **-am**: the book prints the script as «ـ آم» with an alef-madda; correct is «ـَم» (after a vowel «ام»), as Dehxodā's استن entry shows. `error_in: "book"` — I rendered pdf p.161 at 600 dpi and the madda is unmistakable, so **the extraction is faithful and no data fix is needed**. Page image saved to `data/verification/sources/refs/ocr/BOOK/161.png` plus a zoom `161_am_detail.png`.
- `plausible` — Eres 2 #2, Persian **خشت** 'javelin': Moʿin's footnote in Borhān (the cited BQT page, found at BQT_v2 leaf 208–209) does derive it from OInd. ṛṣṭi / Av. aršti-, and Wiktionary's Old Armenian ašteay entry lists it as a cognate; but the initial x- is irregular — Horn no. 23 gives arst as the regular NP reflex and MacKenzie knows xišt only as 'brick'.

**No extraction errors found.** One note for the owner: the printed page has an empty, unlabelled box to the right of the Old Persian node (no language, no refs, no words) — a layout filler that the extraction correctly omitted.
