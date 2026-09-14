# Verification process log — verify-page-447


## [2026-09-14T01:56:02.259Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 447 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-447.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-447.json. Write /home/sfmqrb/git/rishe/data/verification/page-447.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 447` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:03.317Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:04.180Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:04.197Z] TOOL RESULT

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


## [2026-09-14T01:56:04.690Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-447.txt"
}
```


### [2026-09-14T01:56:04.718Z] TOOL RESULT

```
1	=== PDF page 447 (book page 417) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Seu 1 : one's own self  (refs POK:882; AHD:1538)
4	#1 (parent #0) [Avestan] refs=POK:882; BQT:718; BRT:1862; | hva, hava, xva, xvâothra : self ; xvâjo-ayâo, xvadâya : alive from self, self destined, with eternal life ☞Aiw
5	  #2 (parent #1) [Pahlavi] refs=HUB:54; SNS:79 | xvat, xveš : self ; Xvatây : God
6	    #3 (parent #2) [Persian] refs=BQT:779; HRN:104 | xod «خود ١» : self ; Xodâ «خدا ، خدای» : "alive from self" | extra: خدیو ، خواجه ( خدایچه ) | NOTE: See "Ghu" for another possible root
7	  #4 (parent #1) [Avestan] refs=POK:842; SNS:267; IEC:1351 | xwa-tam, xwa-tô : the self, character, habit ; xvaĕ-pati, xvaĕ-paithya : one's own self ☞Pa | NOTE: "pati, paithya" means self or own in this combination
8	    #5 (parent #4) [Persian] refs=POK:842; SNS:267; IEC:1351 | xŭ «خو (بدخو ، خوشخو)» : character, habit ; xîš 1 «خویش ١» : self
9	#6 (parent #0) [Germanic] refs=AHD; KLN | 
10	  #7 (parent #6) [English] refs=AHD | so, such, also, self, sibling
11	#8 (parent #0) [Latin] refs=AHD | 
12	  #9 (parent #8) [English] refs=None | solo, sole, secret, secure, separate, seduce, ; select, sure, custom, suicide, segregate
13	#10 (parent #0) [Greek] refs=AHD | 
14	  #11 (parent #10) [English] refs=AHD | ethics, ethnic
15	#12 (parent #0) [Indo-European] refs=SYN 85,108 | Swe-sor : one's own female
16	  #13 (parent #12) [Avestan] refs=None | xvan-har : sister
17	    #14 (parent #13) [Persian] refs=None | xâhar «خواهر» : "one's own female relative"
18	  #15 (parent #12) [Germanic] refs=AHD | 
19	    #16 (parent #15) [English] refs=None | sister
20	  #17 (parent #12) [Latin] refs=None | 
21	    #18 (parent #17) [English] refs=None | sorority, cousin
22	
```


## [2026-09-14T01:56:07.404Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-447.json",
 "description": "Read source JSON for page 447"
}
```


### [2026-09-14T01:56:07.463Z] TOOL RESULT

```
{
  "pdf_page": 447,
  "book_page": 417,
  "entries": [
    {
      "root": {
        "name": "Seu 1",
        "lang": "Indo-European",
        "refs": "POK:882; AHD:1538",
        "gloss": "one's own self"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:882; BQT:718; BRT:1862;",
          "words": [
            {"translit": "hva, hava, xva, xvâothra", "gloss": "self", "script": null},
            {"translit": "xvâjo-ayâo, xvadâya", "gloss": "alive from self, self destined, with eternal life", "script": null, "see": ["Aiw"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HUB:54; SNS:79",
          "words": [
            {"translit": "xvat, xveš", "gloss": "self", "script": null},
            {"translit": "Xvatây", "gloss": "God", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:779; HRN:104",
          "words": [
            {"translit": "xod", "gloss": "self", "script": "خود ١"},
            {"translit": "Xodâ", "gloss": "\"alive from self\"", "script": "خدا ، خدای"}
          ],
          "script_extra": "خدیو ، خواجه ( خدایچه )",
          "note": "See \"Ghu\" for another possible root",
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:842; SNS:267; IEC:1351",
          "words": [
            {"translit": "xwa-tam, xwa-tô", "gloss": "the self, character, habit", "script": null},
            {"translit": "xvaĕ-pati, xvaĕ-paithya", "gloss": "one's own self", "script": null, "see": ["Pa"]}
          ],
          "note": "\"pati, paithya\" means self or own in this combination",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "POK:842; SNS:267; IEC:1351",
          "words": [
            {"translit": "xŭ", "gloss": "character, habit", "script": "خو (بدخو ، خوشخو)"},
            {"translit": "xîš 1", "gloss": "self", "script": "خویش ١"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "so, such, also, self, sibling", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "solo, sole, secret, secure, separate, seduce,", "gloss": null, "script": null},
            {"translit": "select, sure, custom, suicide, segregate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ethics, ethnic", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "SYN 85,108",
          "words": [
            {"translit": "Swe-sor", "gloss": "one's own female", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Avestan",
          "refs": null,
          "words": [
            {"translit": "xvan-har", "gloss": "sister", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "xâhar", "gloss": "\"one's own female relative\"", "script": "خواهر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 12,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sister", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 12,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "sorority, cousin", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:56:08.171Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:08.228Z] TOOL RESULT

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


## [2026-09-14T01:56:16.383Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','BQT','BRT','HUB','SNS','HRN','IEC','SYN','KLN','WLD','PHD','NYB','MON','ARY','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:700])\n    print()\n\""
}
```


### [2026-09-14T01:56:17.514Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/

CHEUNG null
```


## [2026-09-14T01:56:21.844Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==891' POK_01.txt | head -80"
}
```


## [2026-09-14T01:56:22.948Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"s(e)ue-\\|seue-\\|s(u̯)e-\\|su̯e-\" POK_full.txt | head -30"
}
```


### [2026-09-14T01:56:22.968Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-14T01:56:23.196Z] TOOL RESULT

```
73612:*s(e)ue-\.o, compare with aniaut su-: Old Church Slavic 5i/e/7e 'besides, without' and Latin 
74403:Note: and (after analogy from *t(e)ue) s(e)ue- 
74420:2. seue-, *sue-:0\d Indie Poss. sva- 'suus', Avestan hva-, x'a-, ap. huva-'e\gen, suus' 
83853:to reflexive possessive pronoun *se, seue-. 
84329:Indo Germanic *s(u)e-sor-\.o Reflexivstamme se-, seue-; to ending compare fem. Old
```


## [2026-09-14T01:56:25.383Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74330,74470p' POK_full.txt"
}
```


### [2026-09-14T01:56:25.443Z] TOOL RESULT

```
zusammendrehen, wind up, roll up ', ablaut. Church Slavic 5^/ra//"turn' (reshaped from 
*soukeJe-, compare russ. sucftb "zwirnen'); 

References: WP. II 470, Trautmann 291, Liden KZ 61, 7 f., Pedersen Hittite 134. 
See also: s. also seuio- " left ' and suei- "bend'. 



Page(s):914 



Root / lemma: seu-4, seu-t- 

Meaning: to boil, move vividly 

Material: Avestan havayqn^sxe schmoren', /7ai/aye///"erschmort' (3. Sg. Opt. huyaras- 

Old Indie *suyur\.o a present 7750/// after the Wurzelklasse); 

in addition Germanic *sau^- in Old Icelandic sjoda 'simmer, seethe, boil, cook'. Old 
English seoda/? (engl. seethe) ds.. Old High German siodan. Middle High German Modern 
High German sieden. Old Icelandic seyd'brausendes water', seyd/r'Kochfeuer'; Gothic 
saut^s^ sacrificial animal ', Old Icelandic sai/d^'sheep, also anderes small cattle'; Old 
Swedish 5a^A'/7"Sprudelquelle'; Germanic *sut=>a- in sodn. TIeischsuppe, broth'; 

Lithuanian siauciu siausti\ corn, grain) winnow, fan, die chaff of corn, grain segregate; 
play; dash, rage ', siuntu, siusti^XoW become'; besides also the meaning "hit' in zem. s/ut/s' 
shove ', Latvian sai/s/ 'geiftein'; compare also Lithuanian saubt/^age, clamor, dash', 
saJM'umhertoben', Old Lithuanian s/autit/" prank pull '; Latvian sau/fsm. 'gate'; 

maybe alb. (*5/-) 5/7^' "thresh, winnow'. 

russ. sucu, sutftb "spaften, joke', s^/(Gen. sut^ m. " merrymaker, buffoon ', slov. sutec 
■fool'. 

References: WP. II 471 f., Trautmann 260. 
Page(s): 914-915 

Root / lemma: seua- su- 

Meaning: to let, leave (?) 

Material: Gr. saw ' allow ' (*£Fa(ji)), spaaov saaov. lupaKouaioi, sua = la Hes., Put. saau), 

Aor. siaaa (to *£Ta); zero grade Old High German vir-sOmen, Modern High German 

saumen, ver-saumen {\nou\6 be denominative eines *sO-md-s' slackening, saumend'). 

References: WP. II 472, SchwyzerGr. Gr. 1, 682, 752. 

Page(s):915 

Root / lemma: seuio- 

Meaning: left 

Material: Old Indie savya-, Avestan haoya-^ left ', Old Church Slavic sujb, f. suja ds. 

References: WP. II 472, Trautmann 260; 



See also: perhaps as " writhed, crooked, humped ' to se^-J (compare Latin laevus above 

S. 652). 

Page(s):915 

Root / lemma: se- 

Meaning: reflexive pronoun 

Note: and (after analogy from *t(e)ue) s(e)ue- 

Material: 5e-and s^^e^J^e- Reflexivpronomen for alle Personen, Geschlechter uud Numeri; 

Gen. seue, Dat. seb^e/) enclitic Gen.-Dat. s(u)of, adjektivisches Possessiv s(e)uo-\ se-: se- 

ue- inflectional as te-: te-ue 'du'. 

/. se-;gr. acpg, acpiv etc., poss. acp6(;, derive from *a-(p£i, a-cpi(v), die as acp-£i, acp-i(v) 
aufgefafitwurden; 

Latin sibT, se, Paelignian sefei, Oscan s/7e/"sibi' {*s^^ei), s/om'se' (Umbrian seso'sibi' 
from se/-psd ^s\b\ ipsT?'), Gothic s/'k, Old High German s/h, Old Norse s//r "sich' {*se-ghe), 
Gothic sis. Old Icelandic se^Dat., Poss. Gothic seins. Old High German s/h etc. "sein' (auf 
dem Lok. *5e/beruhendes *sei-no-s); compare Messapici/e/>75/7"suam' from * suei-na-m; 
Old Prussian sebbeiDai.. s/enAkk., Old Church Slavic sebe Dat, s^Akk. "sibi, se'. 

2. seue-, *sue-:0\d Indie Poss. sva- 'suus', Avestan hva-, x'a-, ap. huva-'e\gen, suus' 
and zero grade Avestan hava-6s.; Avestan Dat. Abl. hvavdya'\.e. Iran. *buabya's\b\, se', x 
"^/'sibi'; 

Armenian in-k'n. Gen. in-k'ean, "selbsf (/r'from su), perhaps /ic/r'sui, sibi', {*seuero- 
ox*seuoro-); 

gr. £ (pamph. Fhs) "sich' from *sue, hom. ££ from *seue. Gen. hom. £0, do, £U, £U, Attic 
ou ( *suesjo), Dat. ol, oi, Lesbian Vo\{*suol) besides hom. £oT ( *seuoi), Poss. 6c„ Doric Voc, 
"sein' ( *suos) besides hom. £6c; ( *seuos), wherefore v\k\% ( *sua-li-k-) " of the same age, 
coeval, fellow '; 

alb. ve-te {* sue-th) "selbsf, u-Prou. refl. {*sue-), vaje'g'\r\' {*var/ato *suo-ro-' relative '), 
ve/a " brother ' (see above S. 685); 

Maybe Phrygian: ve/a-i. "family, relatives' (?) : alb. i/e//a "brother' 

Note: 

Wrong etymology of alb. vaje^gkV 



Maybe alb. Geg {*vargha) varza, tosk vaje "girl, virgin' : Latin virga^ thin branch, rod ' 
(from *uiz-ga), virgo^ girl, virgin '; 

Root / lemma: uer-3. E. uer-gh- {* suerg^h^: "to turn, press, strangle' < [common Latin 
Germanic -s- > -r-\ of Root / lemma: ueis-2\ "to turn, bend'. 

Old Latin sovos, from which in schwachtoniger position suos, Latin suus, Oscan suvefs 
"sui' (Gen.), suvad^sudi', Paelignian s^o/s "suis', marr. 5^5/77 "suam', next to which zero 
grade Umbrian sue-soLok. Sg. ^ sud; Latin sed, sepreposition "without', prefix "beiseite' 
basic meaning "forsich, without' (Abl. *s(u)ed), conjunction "but, however'; in addition gr. 
i5iO(; "privat, eigen', argiv. *Fh£5iogirovc\ Indo Germanic *sued-ios, 

Gothic si4/e5 "eigen', n. "property'. Old High German Old Saxon swas. Old English 
swses. Old Icelandic 5Kas5"dear, traut' (as *sue6'^-so-ox -to- root *sue6'^-, see below; 
Middle Dutch 5i4/ase///7c "father-in-law, son-in-law, brother-in-law'; to Old High German gi- 
swTo{see below) the VN S^/c»/7es by Tacitus, Old Icelandic SvTarxu. PI. "Schweden', svhdai 
"from selbst dead (not killed)', lengthened grade sve-vTss "stubborn ', Gothic swi-kunt^s 
"apparent, manifest, obvious'; 

Lithuanian sav$s, sei/^5"sui' (Gen.) etc., Ross, savas, zero grade Old Prussian swais = 
Old Church Slavic svojb "suus, eigen'; out of it swojak-b "affinis', etc. 

3. s(u)e-b^(o)-, st/o-b^o- "from eigener kind of: Old Indie sait'/?^ "congregation, meeting, 
Gemeindehaus' (less good above S. 105); Gothic sibja. Old High German sipp(e)ae\c. 
"family, Gesamtheit the particular Leute' {*sebjd}\ Germanic *sednd- and *sednan- lamWy' 
in Old Icelandic sjafn/m. "love', GN sjgfni., VN *Sednan-ez>Semnones^S\ppegenossen; 
in addition the VN Latin SabTnTas "die Sippenangehorigen', Sabelli {*safnolo-), Samnium = 
Oscan Safinim; Latin SamnTtes, perhaps ein from den in Italien wohnhaften lllyriern
```


## [2026-09-14T01:56:28.171Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '74470,74560p' POK_full.txt"
}
```


### [2026-09-14T01:56:28.234Z] TOOL RESULT

```
Oscan Safinim; Latin SamnTtes, perhaps ein from den in Italien wohnhaften lllyriern 
bezogener name with a from Indo Germanic o, compare Slavic sob-; in addition 
lengthened grade die Germanic Suebi, Old High German 5M/ai6'^"Schwaben' (Germanic 
*sweba-, Indo Germanic *sudo^o- "free, zum particular Volk belonging'); russ. (etc.) o-soba 
"person', 5C»i6'6"Eigenart, character'. Old Church Slavic sc»/?i.s/i/o"Eigenart, entity', and with 
su- Old Church Slavic 5KC»i6'c»o'a"Freiheit' (originally "state, status the Sippenangehorigen'); 
zero grade seems Old Prussian si/it's "selbsf; quite doubtful with e Slavic *sebrb in russ. 
pa-serbt "Stiefsohn' and (?) dem names the Serben and Sorberr, with still 
klarungsbediJrftiger nasalization *s§brb\n aserb. sebrtlree Baner', russ. syai6'/'"Nachbar, 
friend'; compare Vasmer2, 599, 611 f., 3, 61 f. 

4. sued^-:0\6 Indie si/ao'/7a"Eigenart, consuetude, custom, Heimstatte', (Avestan x 
'adata-' about sich selbst bestimmend, immortal ' is neuere composition); gr. £9o(; n. " 



consuetude, custom' (thematic psaov sGot; Hes., lakonisch), participle hom. sGwv " 
liabituai, customary ', Perf. £iu)9a, Lesbian £uu)0a "bin habitual, customary ' {*sesud6'^a), 
£0i^u) "gewohne', lengthened grade nGoq n. "custom, Gebrauch, Herkommen', PI. 
"domicile' (: Germanic *swesa-, if from *sue(i!^-s-o-, see above), nGsToq "trauf, sGvoq "bulk, 
mass, Volkerschaft' as "family'?; 

Latin sodalis{*sue6'^alis) "buddy, friend, Gespiele, fellow, Tischgenosse'; sc»/ed"bin 
habitual, customary ', with /for *6!^\ suesco^werde accustomed ' {*sue6'^-skd); 

but Gothic s/dus "custom'. Old High German s/'tu, Old English s/du, seodu. Old Icelandic 
sidr, Akk. PI. sidum. "custom' (previously Modern High German fem.) not here, da sie /in 
the root syllable have (Wissmann, MiJnchner Studien 6, 129, Anm. 28). 

5. t- derivatives: Avestan A'''ae-/^-"angehorig', A'''ae-/a/-"Angehorigkeit, affiliation' (due to 
eines Lok. *sue/-, suo/-); Old Church Slavic svatb "kinsman, relative, relative, Brautwerber', 
{*sud-to-s, compare serb. si/a/r" sister's husband ', Old Church Slavic svojak-b "affinis'); 
Lithuanian svecias, si/eZ/s "guest' (actually "foreigner, stranger'; because of svetimas^ 
strange ', Latvian svess' strange; guest', from *sue-t/oslor sich, alone stehend, hence 
out of stehend'; compare Latvian sevisks " separate, alone ' and gr. ZKac, (Hes. p£Ka(;), 
actually *F/7£-Kac; "for sich', compare av5pa-Kac; "man for man' and Old Indie dvisas "to 
zweien'; gr. £KaaTO(; (*£Kaa-aTO(; "for sich stehend') "ein jeder', thereafter £KaT£pO(;, delph. 
F£KaT£po(; "jeder from zweien'; hom. £Tr|<; (F£Tr|<;) "kinsman, relative, friend', el. Faac; 
"Privatmann'. 

With aniaut *se-(not *sud): Old Church Slavic *set-b "guest', pc»5e////"besuchen'; gr. 
ETopoq " fellow ', fem. *£Taipa, Eiaipa, wherefore as new m. sraipoq. 

6. other Zugehorigkeits- and Verwandtschaftsbezeichnungen (compare under particular 
Schlagworten *suelio[n]-, suesor-, suekuro-s, suekru-) are: 

Wavb^l^r^^yg^^g^rbrothei^*brotl^^ 

Old Icelandic sve/nn'\a6, young boy, herdsman, shepherd'. Old Saxon swen^ a swine- 
herd ' (Bedeutungsanschluft an sty/T? "swine'). Old English swan' a swine-herd, herdsman, 
shepherd', poet, "man, warrior'; Lithuanian svainis {* suoinjos) "of Weibes sister's husband 
', svaine'6\e sister the wife, woman', Latvian 51/5//7/5 "brother the wife, woman'; Old High 
German (ge)swTo'broVc\er-\v\-\a\N, sister's husband ', Middle High German geswTevn. f. 
"brother-in-law, Schwagerin', Old Icelandic sveiti. "Kriegerschar'; 



7. Auf a connection from *se-with dem Pron. Y<^y'/'C»-beruhendes *5e-/c»- seems (?) die 
base from Germanic *se/6'a-"selbst' (-b^^o-as above in *s(u)do'^o-), Gotliic silba. Old Norse 
sjalfr. Old English self. Old High German selb. Modern High German selb, -er, -s/in 
addition Venetic sselboi sselboi^s\b\ ipsi' (= Old High German selb selbo); compare also 
Germanic "se/o^a- "seldom', Gothic sllda-lelks 'wundersam' ("from rare, seltsamer Gestalt'), 
Old High German selt-sanr strange ', adv. se//a/7 "seldom' etc. ("seldom' from "for sich, 
alleinstehend, einzig'); daft Latin solus' alone, einzig, bare' a similar Indo Germanic 
connection *sd-/c»- entstammt, is possible; after Szemerenyi (Word 8, 50) from *sue-alo-. 

8. Vom reflexive in the meaning to divide is the stem 5£/e-in particles for "so' from which 
"as' and "if: 

Hom. coq (Fux;) postpositive "so' from *5^o-with suffixalem -5; but 6t(t)i, Attic otk; "was 
also always' {*Jod-k"id), hom. ottttoix;, Attic onux; "as' belong to */c»- above S. 283 
(Schwyzer Gr. Gr. 1, 617); Oscan svai, svae, Umbrian sve, sue'W, Old Latin suad 
(Festus) "sic'; Gothic swe'as' (relative), swa-swe'as'; Gothic swa, Old Norse sva, Old 
English swa, swse'so', Old Saxon Old High German nnd. so; in addition Gothic swa-leiks. 
Old Icelandic sITkr, Old English sweic, swilceic. Old High German solTh, sul/h etc. "solch'; 

Umbrian sc»-yO//'"siquis', Oscan svaepis, Volscan sep/s'siquis', surur, surer, surent, 
sururent "\tem' {*sud-sud)\ Old Latin sd-c'so' (could have evolved from *sud), Latin 5/~"if' 
(originally "so', sTdTs placet), sf-c'so'. 

References: WP. II 455 ff., WH. II 457 f., 506 f., 530 f., 552 f., 557, 626 f.; Trautmann 251 
f., 291 , 294 f., Schwyzer Gr. Gr. 1 , 226, 600 f., 606 f.; 2, 577; Mezger Word 4, 98 ff., 
Benveniste BSL 50, 36 ff.; 
See also: s. also sen/- and su-. 
Page(s): 882-884 

Root / lemma: seik-, sik- 
Meaning: to reach for, grab 

Material: Gr. Tku) ( *sTkd), Doric sTkoj ( *seikd) "come, gelange, erreiche', Ionian Attic Inf. Aor. 
iKEoOai {*s/k-), Praes. iKvsopai, hom. Ikovu) (*iKavFu)) ds., iKOvoc; "hinreichend, genijgend',
```


## [2026-09-14T01:56:37.801Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"suesor-\" POK_full.txt | head -20"
}
```


### [2026-09-14T01:56:37.864Z] TOOL RESULT

```
74514:Schlagworten *suelio[n]-, suesor-, suekuro-s, suekru-) are: 
84287:Root/ lemma: suesor-{*suestor) 
84293:Root/ lemma: suesor-{* suestoi): sister' derived from Root/ lemma: se-\ "reflexive
```


## [2026-09-14T01:56:39.367Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '84285,84360p' POK_full.txt"
}
```


### [2026-09-14T01:56:39.436Z] TOOL RESULT

```
Page(s): 1 050 

Root/ lemma: suesor-{*suestor) 

Meaning: sister 

Note: 

Root/ lemma: suesor-{* suestoi): sister' derived from Root/ lemma: se-\ "reflexive 

pronoun, *own' + common lllyrian -tar, -/o/'suffix; it was modelled after Root/ lemma: 

pate(r)Qer\. patr-es, -ds: father', Root/ lemma: mater-: mother'. Root/ lemma: b'^rater-: 

"brother' 

Material: Old Indie svasar-, Avestan x'arjhar-^ sister '; 

Armenian k'oirds. {*suesdr); Nom. PI. k'or-k' {* suesores). Gen. Sg. k'er{*suesros); gr. 

£op [Vok.] GuyaTrip, av£4Ji6(; Hes., io^zq, npoanKOVT£(;, auYY£V£T(; Hes.; Latin soror'a 

sister' (in addition sobnnus' a cousin by the mother's side, mother's sister's child ', from 

*suesr-Tnos = Old Church Slavic sestrinb " belonging to sister ', compare also East 

Lithuanian seserenas^ sister's son '); Old Irish siur^ sister' {*suesdr), Dat. Akk. sTeir, Gen. 

se/^a/" (analogy after mathir. Gen. mathai), cymr. chwaer, acorn, huir, mcorn. hoer, hor, 

bret. c'hoar, Gothic swistar{Qer\. swistrs, Dat. swistr); Old Icelandic syster, PI. systr{Pro\.o 

Norse swestariroru -er). Old High German swester{*-ei\). Old English sweostor, suster, 

vor dem /- insertion created anew are Old Saxon Old Swedish sw/zy'son of the mother's 
sister ', Old English swiria " sister's son, weather '; 

Old Prussian swestro(\r\ the a-Dekl. iJbergefuhrt) with m/ perhaps through Modern High 
German influence, for Lithuanian sesuo. Gen. sesersar\6 Old Church Slavic sestra(\r\ die 
a-Dekl. ubergefiJhrt) " sister ' (also FIN) place i/-loses *sesor- ahead; Tocharian A sar, B 
se/"" sister '. 



Indo Germanic *s(u)e-sor-\.o Reflexivstamme se-, seue-; to ending compare fem. Old 
Indie t/-srah'6re\', Old Irish teoir {* trisores) ds.; contains perhaps yet "so^'wife, woman'? 
Or from *su-esor{see 343) " of own blood, relative '? 

References: WP. II 533 f., WH. II 563, Trautmann 258, Benveniste, BSL 35, 104 f.; Pisani, 
Miscellanea G. Galbiati III, 1 951 , 7 f., M. Mayrhofer by Brandenstein Studien 32 ff. 
Page(s):1051 

Root / lemma: sueid- {* ksue/d- < g'^heid-) 

Meaning: milk 

Material: Old Indie ksvidyati, ksvedate {\}v\be\.) "wird humid, wet'; Avestan xsvTd-vc\. "milk', 

common Old Indie -g"h- > -ksu- : Avestan -g"h- > -xsu- 

perhaps to Lithuanian SK/es//"smear', Latvian svafdftds., Lithuanian si//es/as "butter', 

Latvian svie(k)st 6s. 

References: WP. II 521, WH. II 624; 

See also: s. also sueid- above S. 1042, Z. 5. 

Page(s): 1 043 

Root / lemma: sue(i)- 

Meaning: to bend, turn, swing 

Note: (see also se^-and sueng-^bex\6')
```


## [2026-09-14T01:57:23.620Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT grep hvadata ===\" && grep -n \"adāta\\|aδāta\\|hvadata\" BRT.txt | head -20; echo \"=== BRT col 1862 ===\"; grep -n \"^186[0-9]$\\|1862\" BRT.txt | head -20"
}
```


## [2026-09-14T01:57:24.574Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD s(w)e ===\"; grep -n \"s(w)e-\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-14T01:57:24.697Z] TOOL RESULT

```
=== BRT grep hvadata ===
=== BRT col 1862 ===
```


### [2026-09-14T01:57:24.745Z] TOOL RESULT

```
=== AHD s(w)e ===
155:Male blood relations were designated as bhrater- (BROTHER), which doubtless ex- tended beyond those with a common father or mother; the Greek cognate means “fellow member of a clan-like group.” The female counterpart was swesor- (SISTER), probably literally “the female member of the kin group,” with a feminine suffix *-sor- and the root s(w)e-, designating the self, one’s own group.
427:@gvh-. To drink. Suffixed form *égvh-r-yo- in: a. Latin ébrius, drunk: INEBRIATE; b. Latin compound sdbrius (sé-, without; see s(w)e-).
693:in: a. Old English -Jéosan, to lose: LORN, (LOSEL); b. Ger- manic *fer-leusan, *far-leusan (*fer-, *far-, prefix denot- ing rejection or exclusion; see per’) in (i) Old English forléosan, to forfeit, lose: FORLORN (ii) Dutch verliezen, to lose (past participle verloren): FORLORN HOPE. 2. Ger- manic */aww6 in Swedish lagg, barrel stave (< “split piece of wood”), akin to the probable source of LAG?. 3. Germanic *lausaz in: a. Old English léas, “loose,” free from, without, untrue, lacking: LEASING, -LESS; b. Old English los, loss: LOSE, (LOSS); CG. Old Norse Jauss, louss, loose: LOOSE; d. Swiss German lésch, loose: LOESS. 4. Zero-grade form *lu- in: a. Greek luein, to loosen, release, untie: LYSIS, LYSO-, -LYTE, -LYTIC; ANALYSIS, CATALYSIS, DIALYSIS, LYASE, PARALYSIS, TACHYLYTE; b. Latin lués, plague, pestilence (< “dissolution, putre- faction”): LUES; Cc. prefixed form *se-lu- (se-, apart; see s(w)e-) in Latin solvere, to loosen, untie: SOLUBLE, SOLUTE, SOLVE; ABSOLUTE, (ABSOLVE), ASSOIL, CONSO- LUTE, DISSOLVE, RESOLVE. [Pok. 2. Jeu- 681.] leu-2. Dirt; to make dirty. 1. Latin polluere, to pollute (< *por-luere; por- for pr6-, forth, forward; see per’): POLLUTE. 2. Suffixed zero-grade form */u-to- in Latin lutum, mud, mire, clay: LUTE?. [Pok. 1. leu- 681.] léu-1, Stone. Welsh Jlech, flat stone (from an uncertain preform): CROMLECH. [Pok. 2. léu- 683.] léu-2. Echoic root. 1. Extended form */eut- in Germanic *leuth- in Old High German liod (> German Lied), song: LIED; VOLKSLIED. 2. Extended variant form *laud- in Latin laus, praise, glory, fame: LAUD. [Pok. 3. éu- 683.] leubh-. To care, desire; love. I. Suffixed form *leubh-o- in Germanic *leubaz in Old English /éof, dear, beloved: LIEF; LEMAN, LIVELONG. II. O-grade form *loubh-. 1. Germanic */aubé in: a. Old English léaf, permission (< “pleasure, approval”): LEAVE?; b. Middle Dutch verlof, leave, permission (ver-, intensive prefix, from Germanic *fer-; see per'): FURLOUGH; Cc. Germanic *galaubd (*ga-, intensive prefix; see kom) in Old English geléafa, biléafa (bi-, about; see ambhi), belief, faith: BELIEF. 2. Ger- manic *galaubjan (*ga-, intensive prefix; see kom), “to hold dear,” esteem, trust, in Old English geléfan, beléfan (be-, about; see ambhi), to believe, trust: BELIEVE. III. Zero-grade form *lubh-. 1. Suffixed form *lubh-a- in Germanic */ubé in Old English Jufu, love: LovE. 2. Suf- fixed (stative) form *lubh-é- in Latin libére, to be dear, be pleasing: QUODLIBET. 3. Latin libid6, pleasure, desire: LIBIDO. [Pok. leubh- 683.] leud-. Small. Germanic */it- in: a. West Germanic *lutti- laz in Old English /ytel, little: LITTLE; b. Old English liitan, to bend down: LouT?; c. Old Norse lita, to bend down (< “to make small”): (LouT!); d. perhaps Middle Dutch loteren, to shake, totter (< “to make smaller”), perhaps akin to the source of Middle English Joitren, to idle away time: LOITER. [Pok. leud- 684.] leudh-'. To go. Zero-grade form *(e)ludh- in suffixed unextended form *elu-to- in Greek prosélutos, “one who comes to a place,” stranger (pros-, to; see per’): PROS- ELYTE. [In Pok. 6. e/- 306.] leudh-2. To mount up, grow. Suffixed form */eudh-ero- in Latin liber, free (the precise semantic development is obscure): LIBERAL, LIBERATE, LIBERTINE, LIBERTY, LIV- ERY; DELIVER. [Pok. 1. leudh- 684.] leu(e)-. To wash. 1. Suffixed form *lou-kd- in Germanic *laugo in Old English /éag, lye: LYE. 2. Suffixed form *lou-tro- in Old English /éathor, washing soda: LATHER. 3. Variant form *Jaw- in: a. Latin lavere, to wash, with its derivative -luere, to wash: LOTION; ABLUTION, ALLU- VION, COLLUVIUM, DELUGE, DILUTE, (ELUANT), ELUTE, ELUVIUM; b. form */aw-d- in Latin lavdre, to wash: LAVE, LOMENT; C. Latin lavatrina, ldtrina, a bath, privy: LATRINE. [Pok. Jou- 692.] leug-'. To bend, turn, wind. 1. Germanic *Jauk-, leek (semantic transition obscure), in Old English Jéac, leek: LEEK; GARLIC. 2. Zero-grade form *lug- in Germanic *luk- in: a. Old English loc, lock (perhaps < “a bending
1030:s(w)e-
1039:s(w)e-. Pronoun of the third person and reflexive (refer- ring back to the subject of the sentence); further appear- ing in various forms referring to the social group as an entity, “(we our-)selves.” 1. Suffixed extended form *sel-bho- in Germanic “selbaz, self, in Old English self, sylf, self, same: SELF. 2. Suffixed form *s(w)e-bh(o)- in Germanic *sibja-, “one’s own,” blood relation, relative, in Old English sibb, relative: s1B; Gossip. 3. Suffixed form *se-ge in Germanic “sik, self, in Old Norse sik, oneself (reflexive pronoun), whence -sk, reflexive suffix, as in biiask, to make oneself ready: BUSK?, (BUSTLE). 4. Suf- fixed form “swoi-no- in Germanic *swainaz, “one’s own (man),” attendant, servant, in Old Norse sveinn, herds- man, boy: SWAIN. 5. Suffixed form *s(u)w-o-, one’s own, in: a. Latin sui (genitive), of oneself: suICIDE; b. San- skrit sva- (< *swo-), one’s own, whence svdmin, “one’s own master,” owner, prince: SWAMI. 6. Extended form *sed in: a. Latin séd, sé, self, oneself (accusative): FELO- DE-SE, PER SE; b. Latin séd, sé, without, apart (< “on one’s Own”): SECEDE, SECERN, SECLUDE, SECRET, SE- CURE, SEDITION, SEDUCE, SEGREGATE, SELECT, SEPA- RATE, (SURE); Cc. Latin compound sdbrius, not drunk (ébrius, drunk; see egh-): SOBER. 7. Possibly suffixed lengthened o-grade form *sd-/o- in Latin sdlus, by oneself alone: SOLE2, SOLITARY, SOLITUDE, SOLO, SULLEN; DESO- LATE, SOLILOQUY, SOLIPSISM. 8. Extended root *swédh-, “that which is one’s own,” peculiarity, custom, in: a. Lat- in soddlis, companion (< “one’s own,” “relative”): so- DALITY; b. suffixed form *swédh-sko- in Latin suéscere, to get accustomed: (CONSUETUDE), CUSTOM, DESUETUDE, MANSUETUDE, MASTIFF; C. Greek éthos, custom, disposi- tion, trait: ETHIC, ETHOS; CACOETHES; d. suffixed form *swedh-no- in Greek ethnos, band of people living to- gether, nation, people (< “people of one’s own kind”): ETHNIC, ETHNO-. 9. Suffixed extended form *swet-aro- in Greek hetaros, later hetairos, comrade, companion: HETAERA. 10. Suffixed extended form *swed-yo- in Greek idios, personal, private (“particular to oneself”):
1057:swo-. Pronominal stem; so. Derivative of s(w)e-. 1. Ger- manic *swa- in: a. Old English swd, so: sol; b. Germanic compound *swa-lik-, “so like,” of the same kind (*/ik-, same; see lik-), in Old English swylc, such: sucH. 2. Ad- verbial form *swai in Latin si, if, in quasi (quam, as; see kWo- + si, if): NISI, QUASI. [In Pok. 2. seu- 882.] s(w)okwo-. Resin, juice. Variant form *sokvo- in Greek opos (< *hopos), juice: opruM. [Pok. s(wekvo-s 1044.] swombho-. Spongy. Germanic *swamba- in: a. Middle Low German sump, swamp: SUMP; b. Low German zwamp, swamp, akin to the Low German source of swamp. [Pok. suomb(hjo-s 1052.]
1154:wéro-. True. 1. Germanic *wéra- in Old English wér, faith, pledge: WARLOCK. 2. Latin vérus (> Old French voir, truth), true, with its derivative vérax, truth: VERA- CIOUS, VERISM, VERITY, VERY; AVER, VERDICT, VERIDI- CAL, VERIFY, VERISIMILAR, VOIR DIRE. 3. Latin sevérus, grave, serious; regarded by some as a compound of se-, sed, without (see s(w)e-), and vérus, true, but the semantic difficulties make this explanation improbable: SEVERE; ASSEVERATE, PERSEVERE. [Pok. 11. yer- 1165.]
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1420:DEODAR deiw-, deru DEONTOLOGY deu-1 DEPEND (s)pen- DEPICT peig-1 DEPILATE pilo- DEPLOY plek- DEPLUME pleus- DEPONE apo- DEPOPULATE populus DEPORT per-2 DEPOSIT apo- DEPRECATE prek- DEPRECIATE per-6 DEPREDATE ghend- DEPRESS per-5 DEPRIVE pert DEPTH dheub- DEPURATE peue- DEPUTE peu- DERACINATE wrad- DERANGE sker-3 DERELICT leikw- DERIVE rei-3 -DERM der-2 DERMA! der-2 DERMA? tera-1 -DERMA der-2 DERMATO- der-2 DEROGATE reg-! DERRIS der-2 DESCANT kan- DESCEND skand- DESCRIBE skribh- DESERTS = ser-3 DESERVE servus DESICCATE selkw- DESIGNATE sekw-1 DESIRE sweid-1 DESIST sta- DESMID dé- DESOLATE s(w)e- DESPAIR spé-1 DESPICABLE spek- DESPISE spek- DESPOIL spel-! DESPOND spend- DESPOT deme-! DESTINE sta- DESTITUTE sta- DESTRIER deks- DESTROY ster-2 DESUETUDE s(w)e- DESULTORY sel-4 DETAIN  ten- DETECT (s)teg- DETENT ten- DETER tres- DETERIORATE de- DETERMINE ter- DETEST trei- DETONATE (s)tene- DETOUR tera-1 DETRACT tragh- DETRIMENT tera-1 DETUMESCENCE teue- DEUCE! dwo- DEUTERAGONIST deu-? DEUTERIUM deu-!
1477:ERYTHEMA reudh-! ERYTHRO- reudh-1 ESCALADE skand- ESCAROLE ed- ESCHATOLOGY eghs ESCHEAT kad- ESCUDO skei- ESCULENT ed- ESCUTCHEON skei- ESOTERIC en ESPARTO sper-2 ESPECIAL spek- ESPERANCE spé-! ESPIONAGE spek- ESPOUSE spend- ESPY spek- ESQUIRE skei- ESSAY ag- ESSENCE es- ESSONITE sék- ESTABLISH sta- ESTANCIA sta- ESTER ak- EsTHER  ster-3 ESTRONE eis-1 ESTRUS eis-1 ESTUARY aidh- ESURIENT ed- ETCETERA eti, ko- ETCH ed- ETERNAL aiw- ETESIAN wet-2 ETHER aidh- ETHIC s(w)e- ETHMOID sé-3 ETHNIC s(w)e- ETHNO- s(w)e- ETHOS s(w)e- ETIOLOGY ai-! ETIQUETTE steig- EU- esu- EUCALYPTUS kel-2 EUCARYOTE kar-1 EUCHARIST gher-5 EUGLENA gel-2 EUMENIDES men-1 EUNUCH segh- EUONYMUS n6-men- EUPATRID peter- EUPEPTIC pekw- EUPHEMISM bha-2 EUPHONY bha-2 EUPHORIA bher-1 EUPHROSYNE gWhren- EUPNEA pneu- EUREKA were-2 EuRUS eus- EURY- were-1 EUuRYDICE deik-, were-1
1505:FEIGN dheigh- FEINT dheigh- FEIST pezd- FELDSPAR pele-2 FELICIFIC dhé(i)- FELICITATE dhé(i)- FELICITY dhé(i)- FELL! p(h)ol- FELL? pel-4 FELLATIO dhé(i)- FELLOW legh-, peku- FELO-DE-SE s(w)e- FELON2 ghel-2 FELT! pel-6 FEMALE dh@(i)- FEMININE dhé(i)- FEMTO- penkwe FEN pen-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1602:HETAERA s(w)e- HETERO- sem-! HETERODOX dek-! HETEROECIOUS weik-1 HETEROGENEOUS gene- HETERONYMOUS no-men- HEURISTIC wera-2 HEW kau-2
1669:IDIO- s(w)e- IDIOM s(w)e- IDIOMORPHIC s(w)e- IDIOPATHY s(w)e- IDIOSYNCRACY kere- IDIOSYNCRASY s(w)e- IDIOT s(w)e- IDOCRASE weid- IDOL weid- IDOLATER [é-1 IDYLL weid-
1813:MANIAC men-! MANICOTTI man-2 MANICURE cilra, man-2 MANIFEST dhers-, man-2 MANIKIN man-1 MANIPLE man-2 MANIPULATION man-2 MANNEQUIN man-! MANNER man-2 MANOMETER men-4 MANOR men-3 MANQUE man-2 MANSE men-3 MANSION men-3 MANSUETUDE man-?, s(w)e- MANTIC men-1 MANTICORE mer-2 MANTIS men-1 MANTRA men-1 MANUAL man-2 MANUBRIUM man-2 MANUFACTURE dhé-1, man-2 MANUMIT man-2 MANURE man-?, op-1 MANUS man-2 MANUSCRIPT man-2, skribh- MANY menegh-
1828:MASTER meg- MASTICATE mendh-2 MASTIFF man-2, s(w)e- MATADOR meg- MATCH! mag-
2081:PERQUISITE quaerere PERSE s(w)e- PERSECUTE sekw-1 PERSEVERE wéro- PERSIFLAGE swei-! PERSIST sta- PERSPECTIVE spek- PERSPIRE spirare PERSUADE swad- PERT wer-5 PERTAIN ten- PERTINACIOUS ten- PERTURB twer-1 PERVADE wadh-2 PERVERT wer-3 PERVIOUS wegh- PES ped-!
2230:sEccO seikw- SECEDE ked-, s(w)e- SECERN krel-, s(w)e- SECLUDE kleu-%, s(w)e- SECOND2 sekw.-1 SECONDO sekw-1 SECRET krel-, s(w)e- -SECT sek-, sekw-1 SECTILE sek- SECTION sek- SECTOR sek- SECUND sekw-1 SECUNDINES sekw-1 SECURE cilirra, s(w)e- SEDATE! sed-1 SEDENTARY sed-1 SEDERUNT sed-1 SEDGE sek- SEDILIA sed-1 SEDIMENT sed-1 SEDITION ei-1, s(w)e- SEDUCE deuk-, s(w)e- SEE] sekw.2
2236:SEETHE seut- SEGMENT sek- SEGNO  sekw-1 SEGREGATE ger-1, s(w)e- SEGUE sekw-1 SEGUIDILLA sekw-1 SEICENTO dekm, s(w)eks SEIGNIOR sen- SEISIN sag-
2239:SELECT leg-1, s(w)e- SELF s(w)e-
2244:SENARY s(w)eks SENATE sen-! SEND! sent- SENECTITUDE sen-1 SENESCENT sen-1 SENESCHAL sen-1 SENILE sen-1 SENIOR sen-1 SENITI dekm SENOPIA sen-! SENSE sent- SENSILLUM sent- SENTENCE  sent- SENTIENT sent- SENTIMENT sent- SENTINEL sent- SEPARATE pere-1, s(w)e- SEPTEMBER septm SEPTENNIAL at-, septm
2254:SHRED skreu- SHREW skreu- SHREWD skreu- SHRIKE ker-2 SHRIMP skerbh- SHRINK sker-3 SHRIVE skribh- SHROUD skreu- SHRUB! sker-1 SHTETL sta- SHTICK (s)teu- SHUDDER skut- SHUFFLE skeubh- SHUT skeud- SHUTTLE skeud- SIALADENITIS eng’- SIB s(w)e- SIBILATE swei-1 sic! so- SICCATIVE seikw- SICKLE _sek-
2261:SING sengh- SINGE senk- SINGLE sem-1 SINGSPIEL sengWh- SINISTRORSE wer-3 SINK seng¥- SINN FEIN s(w)e- SINTER sendhro- SIP seue-2
2273:SNIFF snu- SNIP snu- SNIVEL snu- SNOOP snu- SNORE sner- SNORKEL sner- SNORT sner- SNOT snu- SNOUT snu- SNOW sneig’h- SNUB snu- SNUFF! snu- SNUFFLE snu- SNUG! kes-1 sO swo- SOAK seua-2 sOAP_ seib- SOAVE swad- SOBER s(w)e- SOCIABLE sekw-1 SOCIAL sekw-1 SOCIETY sekw-1 SOCIO- sekw-1 SOCKET sU- SODALITY s(w)e- SODDEN seut- SOIL! sed-1 som? si- SOIREE sé@-2 SOJOURN deiw- SOKE sag- sol’ sawel-
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
2325:SUE sekw-1 SUFFER bher-1 SUFFICE dhé-1 SUFFICIENT dhé-1 SUFFIX dhig’- SUFFRAGAN bhreg- SUFFRAGE bhreg- SUFFUSE gheu- SUGGEST gerere SUICIDE s(w)e- SUINT sweid-2 SUITOR sekw-1 SULCATE selk- SULCUS selk- SULLEN s(w)e- SULTRY swel-2 SUM uper SUMMER! sem-2 SUMMIT uper
```


## [2026-09-14T01:57:31.629Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la BRT.txt && head -c 600 BRT.txt && echo && grep -c \"\" BRT.txt"
}
```


### [2026-09-14T01:57:31.713Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4803500 Sep  4 14:06 BRT.txt
Google
This  is  a  digital  copy  of  a  book  that  was  prcscrvod  for  gcncrations  on  library  shclvcs  bcforc  it  was  carcfully  scannod  by  Google  as  pari  of  a  projcct
to  make  the  world's  books  discoverablc  online.
It  has  survived  long  enough  for  the  Copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject
to  Copyright  or  whose  legal  Copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books
are  our  gateways  
30725
```


## [2026-09-14T01:57:35.487Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"adäta\\|adata\\|hvadä\" BRT.txt | head -20; echo \"---1862---\"; grep -n \"1862\" BRT.txt | head"
}
```


### [2026-09-14T01:57:35.624Z] TOOL RESULT

```
3352:(      sprechen;  s.  lu  ahuadätay-,  —  3)  Weil  a-iifä
6045:•  g.,  p-  azdi  Adv.  'kund,  gewiss' :  Ikärahya naiy  a'  abavaf'  tya'' . .  ". .  wurde  es  dem Volk  nicht  kund,  dass  .  ."  Bh.  1. 10;  — \adataiy  a°  bavätiy  D.  Ö.4';  —  k!  mSi pasSus  k!  mS  nä  ^ratd  vis/3  anyS  asät "^wa^cä  mazdä  ahurä  a'  zütä  vahisläatcä manaiahs  "von  wem  sonst  weiss  ich es  gewiss,  dass  er  auf  meinen  Ruf  meine Tiere,  dass  er  mich  beschirmt,  als  von A.  und  von  dir,  o  MAA.,  und  voaVM.}"
10655:•  g.  xrünarä-  f.  'blutige  Misshandlung, Blutbad':  Auxsa'i räis  ßiipram  (sd.)  'rqmäl ais  dadäta  ,  ,  trata  r/  ävaßö  (sd.)  Y. 55-8.
13139:—  raf^jrSm  . .  hyat  fryö  fryäi  (sd.)  daidit Y. 46.2;  43.\^;  —  kahmai  vananqm  dadä Y.  44.  15;  —  jitm-qm  (sd.)  .  .  rämqmcä äis  dadäta  (3S.)  vliibyö  Y.  55. 8;  —  y} virtzSnäi  vafiuhim  dät  frasastlm  "der  der Gemeinde  guten  Ruf  verschaffe"  Y.  4^.  7 ;
16748:gruenten praed.  Pron.  poss,  steht  der  Gen. des  Pron.  pers.:  fasava/'  dahyäus  manä abavc^  "drauf  wurde  die  Provinz  mein" Bh._j.2,  4,  12.11  b)  An  Stelle  des  praed. Nom.  steht  ein  Adv,:  axua  . .  bavaAi ya'ha  . .  "so  sollst  du  werden  wie  . ."  Az. 2;  —  i^m  . .  saohrä  bavainti  yas»  iava  . . "was  geschieht  mit  den  Z.,  wenn  .."  Yt. 5'94i  —  ftyat  fta%ra  (sd.)  wawi  bavat ya%rä  . .  Y.30.  9 ;  —  yäü  a  atthus  *paou- ruyU  bavat  'Vie  es  mit  dem  ersten  Leben werden  wird"  Y.  2<¥.  1 1 ;  —  I  adataiy  azdä (sd.)  bavatiy  D.6'.4'; — pasaved  draugc^ vasiy  (sd.)  abav<^  Bh.  i.io;  4-  lo»  16  {wo bly^);l\ —  a An  Aüwat (sd.)  abava/(AMgm.) Y. /p.  159',  c)  Statt  der  kongruenten Num.-Form  des  praed.  Adj.  steht  die  des Neutrums  im  Sing. :  ia'^a  aste  spana  3^ä.- xalmm  (sd.)  bavan  V.  15.  44;  43;  —  apirs- näyu  aAmi  (Sp.aj 6  u.)..yezi  baväm  p?r)- »^^»(sd.)  Yt/9.43(?); — yimS  ..jailyat avat..dazdi  ml ..yatbavani  s^annaiiuhas- ttmsm  tslanqm  Yt/5.  i6(?).  d)  Statt
19873:VgLgt./iiätA,  goL  wKBrföw,  k«l.  «([rfnii;  Bthl. 'BB.rj.So.—S.iniuaz^.~Pü.{znV.S3):meniIaAt ö  an  Aar  3  minän  daliihäh,  (zu  Y.  2S]:  ii ruvän  afidar  j^arötman  doAeL  —  *)  Das  Verbum ist  von  dem  bedeulungsgleichen  mqzdä-  und von  frou/ä- beeinfluist,  daher  iJdieZerreissnng in  m>n.,d'  (auch  im  Inr.)  und  2)  die  Formen dade,  datdüm.  —  Zum  ä  des  Inf.  *infndäiifyäi TgL  den  Inf.  *miadäta^/d.  —  ')  f»^  ist  nach dem  Metmm  ta  streichen, j.  mandäidySi  V.  it.  9:  lies  mind'.
19876:•  y,  g.  mainyav-,  manyav-  m.  'Geisf ; I)  'Geist' ab  Sitz  des  Denkens  und  Wollens, sva.  'manaA-;  I)  im  gAw.:  ta  t«^  *'iti- yJui  mahyä  . .  yüsmaibys  g>r>xl{ii,)  Y, 32.  9  ";  —  vTspSng  anySng  *'inyJus  spasyä (sd.)  dvadatahä  Y.  44. 1 1 ;  — fi-S  mä  slia (sd.)  %wahm3t  ^vaocai^kl  *'inyfui  hacä %ws  S>ä»ha  Y.2S.  ii'^i  —  *ärmaiti/  'iiryB *pfnsaitl ya'^ra  Ma^ä{s±)  Y.jj.  la;  — kvB  .  .  irixtim  ,  .  MrS  (sd.)  'inyü  Y.44. 3^;  —  mit  varthav  Adj,:  vanAsuS  *°m- yfus  syao'hananqm  javarB  (sd)  Y.  48. 8  *>.  a)  im  Gegensatz  zu  Sprechen  und YlaxiAth^:  y!  hSi  *inyO  ^aohanäis^a  urva'hS (sd.)  Y. 31.31;  —  mit  vanhav-  Adj.:  «ß zTi  (Sp.  1 54  u.)  zyadanstm  vatihsu!  *°m- yfu/ ^aohanaiyä  uxlaSyalä  Y,  4I5.  8^'j  — mit  sp3nta-,  spsidita- :  sf?nta  'inya  vaiWiä^a manatiha  haiä  aSät  (Sp.  a3im,)  lyadiia' nät'a  vacavAä/a  ahmai  dqn  . .  masdä  Y. 47-i;  —  oAyä^'iriy^ui' sp^iäaAya  vaM/fym . .  3»ana  . .  vtmyaiisA.)  Y.47.  a; —  aAya
25100:KompA. ;  E.  —  Ableit  ans  ^raiav-.  —  ü.  vgl. X-tviya-  Adj.  —  Pü.  (zu  V.,  F.,  Vr.  IK,  Y.>! frirö»  -  (lu  Y.  erl.):  j^^  -,  (zu  Vr.  7/): ralVtä;  Sü.  (lu  A.):  ladätarl.
26040:•  j.  savahi-  (n.)  Name  des  im  Osten  ge- legenen Erdteils  (iarfyar-,  sd.):  avi  ar>- zahi  ''<4i{AD,)  Yt. /o.  15;  133,  *V.  ip.  39''; —  upa  karhan  yat  'hi  YLJ2. 10;  — anzahibyS  (sd.)  'hibyS  fradata/suiiyS  .  . Vr.  10. 1.
28221:Pü. ;  zur  iai,  erL  1  pa  adätastän.
28541:susaili"''>  hactt  jafnavB  raonqtn  avi  bans-  i)  'sich  freuen',  absoL:  Auxsdhräis  Jm^ navS   gairinqm    V.  5.  2.  f)    a    und  rqm  (&±) . .  rämqmcä  äil  äadäta  syeitibyö
29420:•  p.  bamara-  m.  'Feind,  Gegner':  adataiy asdä  bavatiy  parsi^  marliyt^  *dürayapiy haia  parsir  'ram  patiyajatä  "und  es  wiiä dir  kund  werden:  der  persische  Mann hat  gar  fem  von  Pcrsien  den  Feind  be- kämpft" D.6. 4'».
---1862---
```


## [2026-09-14T01:57:41.741Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} {n++} END{print \"leaves:\",n}' BRT.txt; for i in 965 970 975; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BRT.txt | head -12; done"
}
```


### [2026-09-14T01:57:42.815Z] TOOL RESULT

```
leaves: 1041
=== leaf 965 ===
  selbe  Mutter hat':  bardiya^ . .  '13  hamapita  ka''bU}iyahyä Bh.  /.  10.
Komp.;  ^a* -!-«(•■)  oder  ^hama-\m'  (mit Haplol.)').  —  ■)  Vgl.  gr.  iiu;tT,Ticp  und  ander- seits ixarpti  (woiu  GMeyeR  GrGr.l  7a)  neben iliiiiaTptc,  tKvT{-  i/ii^vyn  (bei  Hesvch).
•  j.  hani-flraB'a-  m.  'Gegner,  Widersacher': vUämn  (sd.)  paskät  '%}m  Jantärim  pars dulmainyüm  Yt.iy.ii;  —  •'^»m  *paiii.- yBiliStS  (sd.)  Yt.  j^.  107;  r.^35;  —  ye^fie hasannm  vasyanqm  patti  °%ai  jasaiti Yt.iO.69;  —  y^  ^/rq/(sd.)  ia^  *^a\a.. sHja  mjainti  '%S  (AP.)  Yt  /o.  7 1 ;  13.  33; —  narqm  . .  *ia'^ravanan/qm  'S/  Ny. j.io;  —  Aa'hra.nivaitSm  •'^anam  aurvaha- namtbi^antqm  Y.57.b6;  YLy.133,  J5.1, V'yt/p;  —  ta  daiAkavö  ti  *'>ä^"  (NP.) YK.io.i.Z'^;-- yai!a..vanäma  vups  *-ä7 (AP.))'  Yt. /O.  34;  —  dämum  (sd.)  . . ^'%anamai  Yt2.  la.
Zum'V.  iflf  {ar.  *sani-j-lha-),  eig.  'der  ein (feindliches)  Zusammentreflen  hat',  1.  Aamara-, kamaraita:  —  ai.  vgL  nir-flhä-  m.  —  Pö.: kamimär  (wozu  WEST  SEE.  5.  300),  —  ')  Nach F I ;  pron.  flektirt.  —  >)  Wohl  Gloise.  —  3)  Hds. har>\}%  s.  Cid,  COA.  iSg;.  403.
•  j,  haniöistri-  £:  s.  unter  haMaistar-.
j.  Aami.gaad' :  liet  hämS^.
•  j.  haniö.gaona-  Adj.:  s.  unter  Mawia- gaona-.
dby  Google
1777
hamo.xäaOra-
hay- I A
177S
=== leaf 970 ===
2.  a)    mit    dariya-    'die  langdauemde
(ewige)  Seligkeit':  tanvaica  * kaosravanhtm urunaeca    darrf>tn    'vanh)m    F.^J  h;    — dätim  tl  tanuye  x"ann3  urunalca  darrjpm *vatih»m  Y\.i-].23;  —  vatihauca  sravahe urunag'a  danye  'vatihe  A.  i.  11;  —  aAeca aisliSus  dary/ai   Aaesrava^Asi    manahye- keca    aahlul  darrjai  'vatihäi  urune  asti vahistam  Vyt.js. KompA.  —    Ableit.  aus  *Av-aohav-  Adj.    — Pü. :  Auai^ik,  Sü. :  iiltamaAak,  Npii.  1  nli  andisT. —  ")  Zu  den  verschiedenen  Schreibungen  s, S  26:?.   17  fr.;  22.    —   »)  VgL/z-aabaa.  No.    I.
•  j.  havana-  m.  ('Auspresser,  Kelterer') Name  für  die  beiden  Teile  des  loi  Haoma- bereitung  verwendeten  Geräts,  spez.  beim ffaemamÖTsti  des  Trogs  und  Stössels*': fraiarfm{&A.)(it  tl  °»?m  . .  upa.staotni  . .  yö qsui * hanglurvayete  upanmat''  U  °n»m.. yahmi  niyne  nars  aojanha  "das  erstere (untere)  Stuck  deines  (des  Haoma-)bAÖt- sers  . .,  das  die  (.ff<zii/nii-)Zweige  aufnimmt, und  das  obere  , .,  womit  ich  hineinstampfe mit  Manneskraft"  Y.  lo.a; — ^d3ityö*ainyS havanS  *däityS  *ainyS  ya%a  *va  *däifys hita  "der  Vorschrift  entsprechend  sei  das eine  Stück  des  (Äiiowa-) Mörsers  und  der Vorschrifl  entsprechend  das  andre,  auf dass  beide  der  Vorschrift  entsprechen,  wenn sie  verbunden  sind"    N.  J07,  a)    Du,
'Mörser":  'na  däityBJarttaY  .14.%.  [N. lOj  aA.:  lies  hävanalibya;  —  N.47  aA.: lies  Aävanifiqm.]
*)  Abbildungen  des  heutzutage  üblichen  ans Kapfer  hergestellten  Mörsergerats  finden  sich allenthalben.  Früher  bestand  es  wobt  zumeist aus  Stein  und  der  Trog  war  demgemäss  wesent- lich flacher;  vgl.  H.  lOS,  wonach  der  kleinste zulässige  Morser  nur  drei  HaomaiMiex^t  fassen  tu kännen  brauchte.    Vgl.  auch  Aävaiia-  a.
KompE.  —  Zum  V.  'hav-.  —  ai.  vgl.  aähifä- vaifa-  Adj.  'lut  Somab ereil ung  dienend',  n. Du.  '  Somapressc'.  Vgl.  GON.  KZ,  tS-  526, Bthl.  IF.  5.  370.  —  Pü.j  kävan,  /riltum Aävan  -  aparlum'-'i  hävait  oder  afiar')  Aä^art (vgl.  PüErl.  zu  N.  /o/).  —  ■)  Vgl.  gr.  Ztipt; ■Mörserkeule'.
dby  Google
178?
havant-
•  j.ha'vant-Adj.'gleichgross, -viel, -wertig'; Plur.  'einander  gleichstehend':  ks  °vqs  datv5 "wer  ist  ein  (den  wirklichen)  gleichwertiger Z).?"  V.Ä  31;  32;  —  {tat  'vatqm  nana (sd.)  yahmi  .  .  N.ij;  *9'1;  —  _vaS<i  °va^ vag^at  N.  68{}).  a)  mit  Gen.:  yesi  .  . *'vanti(APa.)'^  ailahe  syao%nahe  v»r>syqn nsca  kainila  kanäca  "wenn  . .,  so  wirken gleichgrossen  Anteil  an  solchem  Tun  . ." V.J5.i3f.
KompA.  —  Eig.  'wie  er,  ihm  ähnlich'.  —  tnp. havanii.  —  Vi.:/ävatiil,  (lu  N.  6S):  ka  ilön  äiäs käl.  —  >f  Hds.  M/a  Iqm;  s.  aber  Pü.  —  ')  So Jpl,  Mfi;  Bthi-  IF.  13.  116.
•  j.  yS  nSit  aiwyasti  (Sp.  278  o.)  aiaya *anäusa  "havayaDhsm  *axtlm  N.  15.
=== leaf 975 ===
amm  vaa-  anietien,  s.  va- vana:  Zu  Y.  6i.  6  sind  die  WStter  in  NA. ^schlich  verbunden.  —  *)  Vgl.  iSt,  Mx.  /.  a8. —  M  So  nach  der  Var,  —  *)  Hds.  Jaiu}.  — ?)  Scheint  nur  eine  Variante  des  vorherg. Satzes  zu  sein.  Pü.  hat  freilich  für  xaxva grift,  für  M3w/  dagegen,  das  DsT.  ZA,  ^.  IJI für  einen  Aorist  sa-m-i  halt,  sirit.  —  ä)  VgL Y.  57.  12  unter  gam-  mit  paiS.
*  %■  (•  jO  ha-zao6a-  Adj.  'gleichen  Willens, gleichgewillt  mit  — '  (Instr.):  vahistfm  '^wä vahiitä   ySm    aiä    vahtstä    'Am    ahunm
".  .  dich,  o  bester,  den  mit  dem  besten A.  gleichgewillten  Ah."  Y.  21?.  8 ;  —  ahuri . .  ala  'SB  masdä  "AAM.,  der  mit  A.  gleich- gewillte"  V.2p.  7;  —  tat  vS  nS  'iäoha (VP.)  vUpänkB  daidyäi  savB  "diesen  euren Nutzen  sollt  ihr  uns  gewähren,  ihr  gleich- gewillten (Götter)  alle"  Y.5/.  20.
KompE.  —    aL  laj'ifa-  Adj.  —    Pü. :  fia  ikam
äBÜitilh.
•  j,  yim  vä  ainim  *Ad6B^al%a  (sd.) "hazaoäyä  paanha"  layqn  N.  /.
Pü. ;  undeutlich.  Vll. :  pa  dSHSn  -  pa  kämak  - i  ^eJ  u  S/räi  -  dastatoarih  -  1  öiän  i  haat- trätarän  i  apärllan  d.  i-  "auf  seinen  eignen Wunsch  (WUlen)  und  mit  Genehmigung  (Be> votlmächtigung)  der  andern  Genossen".  Da- nach vll.  kva  toBsa  uta  iänha'1  zu  lesen').  — ')  Ai.  Jäia-  m.,  vgl.  jämä-,  wofür  Npft. ämüxtuH  hat,  ebenso  wie  für  öfräs,  die  Ubier- setzung von  "paiaha  c=  sin/vi,  in  Mx.  — >)  Anders  HoKN  KZ.  34.  5S3.
•  j.  hazanra-  neutr.  Zw.  'tausend':  hist^nti .  .  yazalänhs  iattmla  'rtmca  YL  Ö,  i ;  — yä  .  .  paica  vazinti  xsvai  tatäü  •rtm'a Yt  5.  95.  a)  mit  Gen.:  ydi^a  'nrn narqm  "Htm  nartm  arwyaxiaySit  Yt  /.  1 9 ; Ä  55,  io.  69,  128-131*,  Y.65.  4';— _yaäa na  satimca  "tfmca  baivanca  *parsanqm ''ni/abmlsd.)  Ayät \t  13.  JI -,3.31,  63,  120, Ä4S-5-3.  10,  JO.82,  A.J.7-11*,  V.J.31, 37',  /A'.  70-73»,  74'',  2/.  7,  22.3-4,*,  Y. 6S.1S,  N.42',  H./.s,sVar.,  10;  —  'rai (ab  Gen.)  bar>sna  vlranqm  YL  5.  96; £49;  —  'r»m  (statt  Instr.)  ha<ia.cikanqm (sd.)  V.4-ioi  —  y^ /"""i  fl^q^t  daei-a- nqm  'rai  'rB  pairi  Yt_j.  10  •';  4.  2  ",  Vyt ig'K  a)  mit attrib. Einerzahlen:  ioiitfa- rasca  a^a  garayB  . .  ca'^aiargsatfm{sd.)/a
.dvaiea  satte  dvaica  =«  (ND.)  Yt/p.  7; '  —  nava^a  yaskS  navailisca  navaca  sata j  navaca  'ra  navas!s{sd.)ia  baivqn  V.  22.  3; !  Ytij-sg.  i)mAGK^\duyfrevpap€tnam j  V.  7tf.  73;  73%  Vd.  6  (-rohe).  b)  adjekt i  gebraucht:  ha'^ra  . .  yasata^byO  . .  panäx- \saiblica  laiaisca  'räiS^a  batvanbls^a  Vr. ,8.\;  —  'nm  vq%wh  bavatti  YLj<S'.5";5*'; I  —  'nmyanm  Vytf"; — 'raw^alsNom.) I  sünXs  strX.nSmanS  'räis  sunit  nairyS.- .itämanB  V.  y,  51;  14.1';  —  *rw«  (als I  Gen.)  narqm  .  .  taoxma  ,  .  xiva^  lata  . . tisrB  sata  (sd.)  V.  2. 30.
KompA.,  E.;  Ableit.  —  ai.  sahätra'  n.,  np. kiuär.  —  Pü. :  tOOO.  —  ')  Wo  'um  statt  duye •rt  lu  lesen.  Die  Abschreiber  haben  den Wechsel  von  V.  18.  73  auf  74  übertrafen.  — 1}  Werllose  Stellen.
dby  Google
1797
```


## [2026-09-14T01:57:51.051Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 1004 1005 1006 1007 1008; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BRT.txt | tail -6; done"
}
```


### [2026-09-14T01:57:52.152Z] TOOL RESULT

```
=== leaf 1004 ===
ai.  iHpuirä-  Adj.  (fem.  'rä-).    —    Pü.:  val  rA         J-  f^^-^ämya  Yt.  7a  143'  '«»  ^i«  '*  (^d-). dahihit  hupusik  (Sü.:  jv/üfraft-o™).  «  j.  hu-bsratay-  f.  i)  'gute  Darbringung*:
•  j.  hu-ptar-  Adj.  (fem.  'fshrl-')  'der  einen  \yd^a  . .  atmia  spmta  .  .paitisqn  ^'nitlmca guten  Vater,  gute  Eltern  hat,    von  ^Xct\*uHa.b)r)itlm^a  *van/a.b>r3itlmfa  Y.60.6;
dby  Google
1829  hub«r9tö  —  hufraya§tayae/a  1830
62. 1,  7,  P.^5;  —  'nfi  uita.b»r7H  vanta.-\  aufgesagt  wird"  Vr./ff.  o;  —  akunavaittm birifi  atars  Sfrlnämi  Y.68. 14.  a)  m\Xgä%qm  ..  'tarn  framar^mnqm  Vi.  14.1. Gen. desEmptingcTs: 'ntlsYa  u/ia.dmils"a  Zum  V. 'mar-.  —  Pa.  {ta'Vr.  74):  pa  xüp vanta.i^nscaya,aianqm}i.4^  .)'gute'  {r^fr:™ ™b^^! {"Ll^ ^J  '^\^'^.t: Pflege  :  IBm  13  datAkävd  ntpaht  ya  'r»/Im  ]  i„^t^  und  vgl.  Au/ram^uaya^/a.  Die  Wahl yatayäti  (sd.)   mi^rahe    Vt./0.78.  LS.       des  /^«-Ahsolutivs  war  hier  durch  dieNach-
-tS,   'ta,   Uam  als  Absol.   sbes.  barsehaft   (au
=== leaf 1005 ===
•  j.    aj«(    vahutäi    yat    "huf^rairwain    >  ,_
dastS.rat5  P.Jj.  !**-p/p   ,„„  v./ra.-  13.
Nach  Pü. :  viiarai  wäre  hup'  (s.  Äu^jin^a-)
lu   erwarlen;    aber   der  Text   ist  auch  sonst  .  •   p,  ''ufrätav-"  m.(?)  Name  eines  Flusses nicht  in  OrdnuDg.  .Eufrat:    zäxän^    näma'   vardanam    anuv
j.  hu/ArU:  i.  Auplar-.  '  'tauvä  (LS.)    Bh.  /.  I9.
•  i-  hu-fraW,tay-  _C  'gute  Darbringung-:  |  :;„?L%"„T^'TiSln'r^?ch^S^^^^^^^ äca  nU  jamyat  avamhe  aif.fräyasttca  %ao
=== leaf 1006 ===
gut  aufzusagen,  zu  reziliren':  /i/c/>- ..^a'i»  j-  hu-frä'yaätoy-  f.  'gutes  Opfern, hjtiti  haoma  Vr.t?.  3.  j Weihen':    äca  nS  jamyst  avaiMe  as.frä-
Zum   V.  »mar..    —    Vgl.  'mmtqm    yxnA  fta-^ yaitica  zaohranqm  •ticaXt.IO.T}.         DL, m^'ilay..   —  Pü.:/o  xüp  fräl  dlmurSnlh.  ^'iayaffca    ats  Inf."  sbes.
•  J.hu-fra'm«r9t«m'>.-m9r9t^'> Absol.!.   ■    hu-frS'yaStayae-Äi  In£  '(und)   gut 'mit  gutem  Aufsagen,  Rezitiren',  in  Vei>i^„     f        ^u weihen':  AuMy'  huframin- bmdnng    mit    dem   V.  '«ar-:  y<^m  .  .  ^  ^      g^,^    ^^  ^^  ^^^„^  Vr_p_3_ haptanhaitlm   ..   "Um  framanmmm     den       \^.  hu/riyaitay.    —    Pü.:   fa  *xüf /räl ya- YHapt,    wenn    er    mit    guter   Rezitation       silniA').  —  >)  anp*  statt  anpp*  getchr.
58'
dby  Google
iSji  hufräya^m  —  
=== leaf 1007 ===
gut  geführt,  geschwungen"':  iaritacit  aiiam\  frärm  kvnarih  rSl  yam  atl;  Si:  rvam  yai  te •ta    .  .   Yt  /0. 40.  "         '  ■  ■  *'"'"*  pravarlamänäÄ  ianü.
4i.  ™/raj.»*/a-  Adj.  -  .)  Vgl.  Yt  13.  1%.      ! ,   j     hunairySnk-  Adj.   'geschickt,  ge-
j.  hufräimi.d-  a.so:  lies  Aü /r".  'wandt":  mthnm  ..  'yinäm  raialstqm  Vt.
•  j.,  g.  hunav-  m.  'Sohn'  uzw.  i^aÄnschcr!  ^O-  '<";  —  «""^  kihrpa  .  .  yancö  Yl Wesen'*:  kvB  datnBil  drUjS  'nul  "der  ist  \  ^'-  •3-
ein  Sohn  aus  der  Schöpfuiw  der  .Dr."|  Komp.  mit  (Ableit.  ans)  •*,«fl/rr--(?)f..  sn. \.  51. 10 -j  —  'navO  {UV.)  i0uru.*ao>:ranqm\  '*    ''  ' -^  ^
(sd.)  Ytfo.  113;  —  nurvii  'H.it'J  j'aäti-]»  j.  hu-oi'vixta-  Adj.  'gut  hera,bge- kaya  (s
=== leaf 1008 ===
Saitnilan  (unter  ihav)  und  JusTi  PrJ.  88. 147, :  iiAi  5  kanCir  {i^it).   —    '»  Geschi.  an  o  mam
WEST  SBF_  4^.  40.  51,  39.  \,km,ixm-i)  sUtt  annd«;  B.  No.  2.  —  »)  G«chi.
•  j-,  g.  hunara-  m.  i)  -Können,  Kunst':'     «"""°>'  «""  »"dstda;  s.  No.  i. kyal     da     ^yaohana     mlidavqn    (sd.)    .  .  •  j.  huovana-  Adj.,  PPM.:  s.  'Aai-. %wä   'ra   ".  .  durch   dein   Können"   Y.  ,  j.  hunvant-  Adj.  (fem.  'vaintt-),  PPA.: 4^.5".         a)  'Kunstfertigkeit,  Geschick- js,  'hav.
lichkeit':    kva    asti    spä    vokunazgB  (sd)  1      .         ,  .  ,.  ,  ,     ,
daityBgätusl  .  .  ys  nfi^m  haiti  'ranam  '  "  >•  g- »»"-mata-  Adj.  gut  gedacht" ;  stets V.  13. 1 9-  3)  Tüchtigkeit,  persönlicher  ■  "«be-i  huxta-yx.^  hvarsia-  (Stverz.) :  nar^w.
Wert':  yS  .  .  upairi  'r>m  manS  barät  .  .  ■""»«""«  dat>rän?m  Hfmca  manB  hOx/fmca yat  hl  *man3  ^ahe  patti  bar
```


## [2026-09-14T01:57:58.389Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 1014 1018 1020 1022 1024; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BRT.txt | grep -n \"18[0-9][0-9]\" | head -4; done"
}
```


### [2026-09-14T01:57:59.491Z] TOOL RESULT

```
=== leaf 1014 ===
5:p.  *«i'flya.,  '•uvajiya-:  s.  Sp.   1846  f.
10:p.  ^laiä':  1.  unter  hv',  Sp.  1853  f.
=== leaf 1018 ===
=== leaf 1020 ===
=== leaf 1022 ===
=== leaf 1024 ===
```


## [2026-09-14T01:58:01.568Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in $(seq 1015 1030); do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BRT.txt | head -3; done"
}
```


### [2026-09-14T01:58:02.674Z] TOOL RESULT

```
=== leaf 1015 ===
  drvaspqm  ..  'lam  Vtp. 2.  b)  sonst:  ianüm  ya  mf  valnaüe 'f^ Y.  io.  14;  —  yetihä  (sd.)  k>Arj>s  •oayä  Yt
dbyGoot^Ie
'837
=== leaf 1016 ===
. £tlr.  2.  331,  —  3)  Worüber  zuletzt  EKüHN KZ.  SS-  3'3-  Stoffliche  Gleichheit  der  ai. sürä'  und  der  ür.  Aiirä-  anzunehmen,  ist  selbst- verständlich nicht  nötig.  —  4)  Der  Kumys der  Kirgisen  enthalt  je  nach  seinem  Alter  1,2 bis  2,0  Prozent  Alkohol;  5.  Ksuc,  Ersch. Grub  er  Enzykl.
•  j.  *hurä(h'a-''  Adj.  'mit  schönem  Wagen- zeug versehen':  hvaspS  aki  '%vS  Yl. 10. 76.
Statt  '■%iva-  geschr.,  %26S.  17  {daher  f,  nicht Kl,  S  ^^S.  38).  —  Ableit.  mit  va-'''i  aus  *hu- tä%ay  m.  (Ableit.  aus  ra%a-).  —  ')  NA.  hat Aurä%yö,  eine  kritisch  wertlose  Variante;  man erwartete  auch  Epenthese;  '%v^  bieten  F  1, jiousw.  31.  —  '1  Oder  ist  •Si'e  Vok.Sing. aus -iiiivi«;-?  Schwerlich.—  3)  Für  K  40  gibt Gdm.  zwei  verschiedene  Lesungen  anl
=== leaf 1017 ===
 havaiahäica .  .'nyäica yat  saolyantqm  Vr.5.  i.
Ableit.  aus  *Aa-rvan-\  -run-  Adj.;  eig.  'Zu- stand dessen,  des  Seele  gut  ist'.  —  PB.:  Au-
'•  j.hu-sasta-'*Adj.  (fem, '/J-) 'gut  bekannt
=== leaf 1018 ===
.  .  häirilli  pu&ri  vgrmvainti  .  .  *tB (NPf.)  srsuw«/!  Ytij.  15;  —  aiyävfm.. yS  . .  hairini  US  (APf.)  dalaiti  Y.  65.  a.
Ableit  «US  Auzämayi  %  i8i.  —  Pü.  {lu  Y.): ke  .  ,  husäyiltüA  dähil.
•  g.  hu-zäntav-  Adj.  'der  gute  Kunde hat  von  -,  wohlvertraut  ist  mit  -'  (Gea); yS  dalnqm  vehü  *jar>st3  (sd.)  mananhä armaüsÜ  kasht  asä  -tu!  ". .  weil  er  durch ASa  mit  dem  rechten  Deoken  wohlvertraut ist"  V.  4g.  5.  a)  absolut  'der  die  gute, rechte  Kunde  in  Glaubenssachen  hat, wissend"*:  andrS '^wavas {sA.)  °iusi  sf^nis matdä  Y.  4.^.  y,  —  yf--  dritä  ayantsm  \ urvätsi!  {%A.)  vä  Uui  .  .  Y.  4^.  5.  j
=== leaf 1019 ===
(näm!.  Ärm^  schenke uns  gutes  Wohnen,  sie  uns  Bestand  und Kraft  .  ."  Y.  48. 6.
Zum  V.  iiy-;  aus  ar.  *xhilman-  n.;  vgl.  ai. kllma-  m.  'Wohnsiti'  und  gr.  Xarr/iB  :  Xsi/ig(; I.  noch  '/raa%man-,  vä%man-,  väri%man-.  — Pü.:  ^ärih.
•  j.  hu-äit-  Adj.  'gutes  Wohnen  bietend, wo,  bei  dem  es  sich  gut  wohnen  lässt':
=== leaf 1020 ===
lsmanqm  aSavat  nafia- nqm  V.  7. 31;  —  vtlastiJrap  yat  (Sp. 1252  u.)  'kanqm  (als  Obj.)  ..  aitiha  s^mS nidaüyqn  "sie  sollen  in  der  Länge  einer V.  vom  trockenen  (Holz) , .  auf  der  Erde hier  niederlegen"  V,  7. 29;  3c,  33,  34;  — 'kanqm  yavanqm  V.  7.  35;  —  'hm  p>htn raicayat  Ytj.  78;  77;  —  aSavat  apat haca  nilbarayjn  °ke  z)me  nidathya»  "so- viel sollen  sie  aus  dem  Wasser  heraus-
I  holen  und  im  Trockenen,  auf  dem  Land ■  niederlegen"  V,  6.  »9;  31.  3)  n.  *Fesl- lland'":  yauna  (sd.)  tyaiy  'kahya  utä ^  tyaiy  *drayaAya  D.5.  2,  [V.Ä34:  lies '  kiiku.]
KompA,,  E.   —    Zum  V.  iaos-.  —   np.  xuit;
=== leaf 1021 ===
j. (fem.  •nä-)  i)  jAw."  'des  Tun  gut  ist': yvamm  humanaraA^m  (sd.,  auch  fdSt.) h%-alat»h>m  °%mm  hudaimm  Vr.^.  3;  — ySttB  . .  '"knaAe  H.  2.  1 8,  Vyt.  ij  \  —  yünat haca  .  .  °^nai  P.JSi  —  ^'""  •  ■  ''"^"^ H.  2.  II,  12;  —  kaxaye  .  .  '%nanhe  Yt, ^9-  95-  2)  gAw.  'wohlwirkend,  guttätig": at  köi  dtigidä  °^anä  ärmaiiis  "sbei  seine Tochter  ist  die  guttätige -fr»«."  ¥.45. 4.
Vgl.  'AuiyaiAaa-  EN.  —  Pü.:  Auiuniiti.  — >)  Stets  in  Verbindung  rait  /annanak-,  /aiamh- und  hiidaenä:
•  j.  "hu'syaoSna-  m.EN.  zweier  Gläubiger; i)  'nahe  a/aanff  Yt.  ij.  103.  2)  "nahe
=== leaf 1022 ===
.  2*3).  —  S.  das  folg. Wort  und  hqmJiar3lar.  vatj/wqm.  —  ')  Geringe Stelle;  offenbar  ReminUieni  an  V.  4-  44t-
•  j.  hus.ham.barvta-  Adj.  'wohl  zu- sammengebracht, erworben':  '^/(AblS.)'' ha€a  /aäät  {sd.)  Yt.1j.67.
Komp. :  Au'-^*kqm.b>rila;  %  3S7.  S.  das  vor- herg.  Wort.  —  ■>  Unthem.
=== leaf 1023 ===
�  *slatia  ahatiy avaiy  mä  dausta  Bh.  .^.  14.  2)  voraus- geht, uzw.  a)  hauv  (Sp.  I73r  u.):  hauv fravartis  'ya*  mädaiy  xsaya^iyt^  agaubats Bh.2.iz;  1.19,^.6,  9;  —  hauv  inartiyc^ 'yt^  avaAyä  karaAyä  ma'hiiii^  äAa*  Bh. J.  II.  b)  'ava-  (Sp.  16s  m.):  avam karam  'y</'  därayJ'vahaus  .  .  gaubaiaiy Bh.  _J.  9;  3,  14;  —  avam  tnartiyam  .. -ya/'säm  ma^t/ta''  äh<^  Bh.  2.  4;  /. 18.          Z)  ohne  demonstratives  Korrelat;
dby  Google
i«43
=== leaf 1024 ===
vum  ist  ohne
Bezugsmasse;     hacä     paruviyat<^      'ya  ^' amäxam    taumä    xsäydi:iyä    äh<^    "anti- quitus,  quae  (est) erat"    Bh.  /.  3
ASn.  Kii'hysr-para-  Adj.  'inde  ulterior',  Komp. mit  Abis.  (Adv.)  im  l.  Glied;  vgl.  Bthu  BB. 14.  146  (auch  gegen  Fov  KZ.  J/.  500J.
=== leaf 1025 ===
45  m.)  va vidamahya  Bh.2.6;  j.  18;  —  kärt^  'ye^  \angrB  yS  .  J  fyanhcü  (Sp.  277  o.)  h'i  nStt manä  Bh.2.7— ii',  14,^.3,  6,  7,  9,  lo;  ayJm  a ngrJ  (sd.)  *'mainyetll  \. 44.1a;  —
—  Aaru*  parsi^  'y(^  vihapatiy  Bh.  j.  $;^  kaUfa/amiurva'i  ff.  J  af  A'  kava  vTs'/ätpi..
—  iyam  dahyatts  pärs^  tyäm  mana^'^-.  das  ist  der  K.V.  . ."  Y.46.14;  —  im a^urä^masdä /räbara*  'ya  naiia    D.4.2;   Sinn  von  'talis,   einer  wie  der':   ärmaßi^
=== leaf 1026 ===
.,  DaL;  auf  die  s.Pers.  bezogen^zu  2):  vanhu h°  0ng  .  .  pai:mSng  .  .  *iarat  Y,  4O.  4;  iß  (Sp.  654  m.)  W  vanhaol  vanhS  buyät 5/.  10;  —  yS  asäuttl  vahiltö  :^attä  (sd.)  1  hvUvSya  yat  saoi:re  Y._5p,30.  b)  als vä  .  .,  at  A'  aiakyä  anhat..  i'Jf/r/Csd.)  Abi.;  auf  die  3.  Pers.  bezogen;  zu  i): Y-J5-3i  —  <^i  y<m!m  nUi  ,  .  SyHt  {%^.\yai  *his*hvavSya^  dasde  ratufrti*^ yai 150  0-),  dräjS  h'   dumqn  .  .  gät  (sd.)  Y. '  äat  hU  nStt  [Ai/]  hvävSya  datde  aratu-
46-  6;  —  p>nsä  aval  ya'hä  hvd  (zu  2  1  a) yi  hudänul . .  /rada^äi  (sd.)  asfifrvgatJ ^uiavas  (sd.)  , .  yada  h'  aahai  Y.  ?;. b)  adjektivisch,  nur  mit  na  (Sp.
)  /rif*''  "wenn  er  sie  von  sich  aus  gibt , ." N.55.         2)   Dat.  «"a/,   auf  die  3.  Pers. ,   bezogen;  zu  1):    afl-'am(Sp.  34 f.)AV  i'hra .  vä  asni  iira  vä  xsafite  mag'i:anaAe  x^ät"' 1051  o.):  y7  .,  sarahuilrtm  ..  xsnJus,  pairi^urvayeite    ".  .    pro    se    (ipso)    .  ," h-    nä   */rasraidyäi  (sd.)    ^fr^'hwS  Y.46.   V.  4.  1.  3)    Gen.    ^x^awAf",    auf  die
=== leaf 1027 ===
r  'Anhang".
—  A'  asava  zara'iiuitrll  urva'i^m  lira-  Ableit.  (fcö-,  j'Ji').  —  Vgl.  lat. //*i,  ksl,  w*/, tärim  is3it(STi  aSf)  Y  -I  11  a)  auf  "="■*  ^"''-  Kurze  VglCr.  409.  -  Pü.  ^»u  Y.): das  Pron.  rel.  ^a- (Sp.  laoa  u.)  als  dessen  ,  (zuV.)';w.H'^«;  s!  noch  Xo.^- ■)  Zu  belegen Korrelat;  a)  substanvisch:  A'  if  dngvä  ist  nur  die  Beziehung  auf  die  2.  und  3.  Sing.  — yS  dngVäiU  vahiitö  Y.  46.  6;  6;  —  '>  D.  i.  ir.  •hsfobia;  iSchr.  s.  S  ^S.  3.  — katärim  ä  angrS  vai  A'  vä  angrS  (sd.)  yT.  i",fpf:i;^Ä^-=i'%r^r.Ied  ai ma.M.44-^2\  —  k}h'y3mäandrS<dt'iat\  ^^^,^_  _  0,  Nomind  flektirl.  -  »  Hds. Y.46.9;  —  at  A'  matda  JsScH  äzBitis(sd.yä  \     avaaM  und  avaaha  (T>
yS  dainam  . .  *sär>sia  . .  kasät . .  Y.  -^.  5; ,  ,  -   ^^^  *„^^.  ^^^     ^  ^^^jer  hava-.
=== leaf 1028 ===
  . jamyät  yS  na  .  .  sUsit  Y.  43-  3-  [Y. '  "Ä?  H.  2.  11,  11;  —  haxayS  ..  'canhö  Yt 29.7:  lies  hvd.urulaäbys;  —   ^5^":   lies   z^.  95-
AvOiStaefva\  1      Slalt  hu-vaP  geschr.,  S  268.  H.  —  ai.  suvacas-
KompA.;  s.  ^aefatay-,  —  Sonst  nicht  nach-       Adj.  'tltri.i.  —  PQ.:  k^'maibi.  —  ■»  Stets  in weisbar;  vgl. 'A^j-,  mit  dem  es  wohl  irgend- 1      Verbindung   mit    kumanak-,    Aufy<,a%na-    und
=== leaf 1029 ===
  abava"  Bh. /.  16;  2.4. 1
Ableit.  aus  ^ujjaja-.  —  >)  NA.  bietet  ßlsch- lich  -yä,  NP.;  s.  'ava-,  Sp.  165  u.  '
•  j'i  g-  hv-apah-  i)  (im  gAw.)  n.  'gutes Werk,  Wirken':  ahyd  xsa'i'racä  maifitUca *'pa»hauca ''  tSm  at . .  yatamaidf  "wegen seiner  Herrschgcwalt  und  Grösse  und  seiner schönen  Werke  wollen  wir  ihn  . .  verehren" Y._57.  2.  a)  (im  jAw.)  Adj.  'gute,  schöne Werke  verrichtend,  wohlwirkend',  von AhM. :  azim  . .  dämanam  nipBta  ahmt  'pg (VS,,  nämL  ahura  mazäa)  Yt  70.54;  54;
=== leaf 1030 ===
hvar»  ..hau  mä..  ave  siärS  V.p.  41;  Yt ij. 1 6,  *FrBy. ;  —  upa  tairtm  (sd.)  haraihyä . .  yat  ml  aiwtts  urvtsMit  starasca  mäsca hvarica  Yti2.25;  V.2.40;  —  strSuSca manhimca  hvar?ca  Y.  2,  11,  77.  9,  Yt. 10. 145,  G.J.  6,  V, /J.  I,  3,  7.5a,  Vyt.4j;
—  haca  hvar»  (statt  Abi)  V.TJ.  10;  — kasna  x^^ngiQß).')  *str^mca  daX  advamm (sd.)  '^.44.  3;  —  fravasayS  .  .  yä  sirqm  ' mäi»hB  hürff  (GS.)  .  .  pa^ff  dalsaym  Yt. ^S-  57'!  Y.  7. 16;  —  hax?6r»mca  yat  asli  . .
hvara.äaeäinan-  184S
```


## [2026-09-14T01:58:08.908Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in $(seq 1031 1040); do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' BRT.txt | head -30; done"
}
```


### [2026-09-14T01:58:10.058Z] TOOL RESULT

```
=== leaf 1031 ===
xlaltai  YtJO.  143;
—  yS  yataite  hvar»  yat  am»hm  raim aurvat.asptm  Yt,  6,  4;  —  mi^r»m  ..yakmäi hvar»  aurvat,asp»m  dürät  tutnS  baohayäti Yt.io.go;  Az.^;  — paurva.natmat am»sahe hu  yat  aurvat.aspahe  Ytio.  13; — hva  r»Ja am»s}  sp»ntt  yatamaide  Vr.  ig.  2  (?),
KompA.  {hvar>.',  i'/ng.');  s,  noch.  Az-ar>xJaela- (auch  für  Y.  T.  11).  —  ai.  jfdr-  n.,  np.  xer (aus  it.'x^ar-,  Srfp);  gol.  vgl.iHma.  —  iFlei. S.  S  J9«  40s.  -  Pü-:  ^«rlft.  -  .)  Slven. unter  vaxsa-  und  frähnS.dätay-.  —  '>  Soll jedenfolU  eine  Form  zu  hvar-  vorstellen. Wertlos.  —  3)  NA.  hü.bämya.
•  j.  hvar«-xäaeta- "  n.  'der  leuchtende Sonnenball,  Sonne',  auch  als  Gottheit;  yas? tava  mazdä  k»r»naot  tacar»  ''nsit ..  *anlar».- ann»m{s<i.)  upairi  't»m  Ytj.go; — ya'^a avat  't»m..fraca  ätti  YtJO.  118;  —  °t»m *utyS.raili  Y.ig.iB; — uzayara  uslra  'ta aurvat.aspa  V.27.5;  —  yatcit  ahi..upa  ave stärd  .  .  upa  aom  maT»h»m  .  .  upa  'lfm aurzaj.rijp»m\t  12. 33—^4;  —  -/»m  am»i»m ralm  aurvat.asp»m  yasamaide  Yt 6.\\  6, jj.Si,  Y. /ö'.  4,  S.S.  11;  —  °tai  aurval- aspäi  Y.68.22;  —  'tahe  amtsahe  Yt,  6. o, Y.  22.  24;  Vd.20;  —  hvar»ca  xiaHahe'^ aurvaLaspahe  Y,  /.  1 1 .  a)  hvar»xsattaht (näml.  ayar»)  heisst  der  11.  Monatstag: 'tahe  amfsahe  ralvahe  aurvat.aspahe  S.  i. 11;  vgl.  2.  II,  Y.lö.  4.
mp.  (Pü.)  Statut,  np.  xarsid;  %  89.  —  ■)  Aus der  synffllt.  Fügung  hvan  xSaiOm  erwacbseo; vgl.  i^iirc^mazddh-  und  *hü  bämya  xsofläi'^X. /o.  143.  —  *)  Tmese  durch  ia\
•  j.  hvar«.caeäman-  m.  EN.  eines  der sechs  Genossen  des  Saosyani  bei  der  Auf-
dby  Google
1 849  hvar«.{SidTa-
erstehung,  Ratav  des  Karhar  S
=== leaf 1032 ===
avakV^: •manu  asaene  Yt.  13. 128,  121.
Eig.  'Sonnenlicht  bereitend  (?;'.  —  ')  Vgl.  Dd. jä.  4,    wo   der  Name   n-^arcaim  l&ulel   (sUtt
•  j.  hvara.ciSra-    m.   EN.  des   zweiten
Sohns  Zarakui'tras  (aus  zweiter  Ehe)*': °raAe  zaraius'trSis  aiaonS  Yt.  y.gS.
">  Er  heisst  im  Mp,  x'arair  oder  x'arsel  Hhr und  wird  aralislär  ipähpal  genannt,  Bd.  J2.  %. Eig.  'sonnen gesichtig'.
•  j.  hvar9.dar9sa-  Adj.  'der  den  Blick der  (sva.  wie  die)  Sonne  hat,  sonoengleich blickend':  yimf  . .  :^ar>na»uhast)m5  täta- nqm  'SO  masyänqm  Y.p.  4; — yat  baväni ,  .  •am  (stattNS'j  ma^anqm  Ytij.iö''.
>L  vgL  svard^s-  Adj.  —  Vgl.  *:^ing.darisa' und  tar>darisa-  (Sp.  451).  —  Pü.:  ^ariit «ikirihilum  hai  marlumän,  erl. ;  huraSmIum. S.  d»iu  Sg.  /,  561  ke  vi!p  däiti  i  vih  huias- miiä  nikiret,  iahn  i  öi  eaim  i  :^arsei  asl.  — I)  Geringe  Stelle.
•  j.  hvar^.dar^sä-  f.  '(solis  conspectus sva.)  Besonnung':  ifä.siairi! . .  raocä-aiwi.- var>na  (sd.)  Sya  (IS.)  hl  z»me  paitt  ni- daihlta  V.6'.  51 ;  —  cvant»n  dräjB  zrvanpm sairi  .  .  raoc3.aiwi.var2na  (sd.)  'sya  Q.^.) . .  bai-ainli  V.  7. 45.
Zum  V.  daris:  —Vgl.  dat^ia-,  —  Pü.:  -^ariel
•  j.  hvarv.darasya-  Adj.  '{so  dass  man von  der  Sonne  zu  sehen  ist  sva.)  der  Sonne ausgesetzt': ^<3i  nSil  aite  matdi^asna  aihm k9hrp?in  'sim  ksrmavqn  yänJrajS^''  "wenn die  ^f,  den  Körper  nicht  ein  Jahr  lang der  Sonne  aussetzen"  V.5. 14";  13'^
"daiisya-  Adj.,  PFP.  lum  V.  dam-,  si.  dMya- 'sehenswert',  vgl.  dfiya-  Adj.  'sichtbar'.  — P�
=== leaf 1033 ===
�.:  ^arstt  nikitUn.  —  O  Die  Interpunktion der  NA.  ist  danach  la  andern,  —  »)  Vgl.  V. 5.  51./.  4Sf-
•  j.  hvara'Sä(y)- :  'of-  f.  EN.  eines  gläu- , bigen  Mädchens:  ''jyh  asaimyäYti^.  141.
Eig.  'den  Blick  der  (wie  die)  Sonne  habend, ! sonnengleich  blickend';  vgl.  hvarLdarisa-,
•  j.  hva^^.ba^^zah•  Adj,  'die  Höhe  der  1 Sonne  habend,   so  hoch  wie  die  Sonne':
aiöis  baesaza  . .  g^mJra^avAa  (sd.)  äänu.- äräjanha  'zanka  (APn.)'>  Y.6'0.4.
Pii.;  x^ari/t  bäläk.   —  ■>  Them.
"  j.  'hvarez-  Adj.  'des  Wirken,  Tun  gut ist,  wohlwirkcnd':  vattkus  haomö ..kukanß
'vanS  i:i^%.yy  Y.^.16.
Komp.:  hw \-'va>-is-.  —  Vgl.  Uvariz-  EN.  — woss.  roarz  'gut'.  —  Pü,;  hitkämak ,  erL ;  kul
apäyist  i  frärön, —  i)  Könnte  nach  IF.p  löl auch  als  NS.  aus '^f^vs- genommen  werden; s.  aber  'kvarn:
•  j.  'hvaraz-  m.  EN.  eines  G^ubigcn, Bruders(?)  des  Ankasa:  •tä  (GD.)  ania- sayS  a/iioni  "des  JI.  und  des  A.,  der beiden  Gläubigen"  Yt. /j.  124.
Vgl.   'Miarn-.
•  j,  hvarazäna-  Adj.  (fem.  •na-)  'gute Gemeinden,  Bauernschaften  habend,  deren (bei  denen  die)  Gemeinden  gut  aufgehoben sind';  /rava/ayS . .  Aui^axmanU (sd.)  •zänä darrjd^bys  haxthroHbyS  upasitse  vahi^tä Yt./j,3o.  '
Komp.:  ka' -Yvamäna-.
•  j.,  g.  hvaräta-,  hvaraäta-''  Adj.  (fem. •tu-)  'gut  getan,  betätigt,  gehandelt": vXspaca  •ta  fyadhna  yasamaide  varStala vansyamnaca  Y.  57.  4 ;  —  arsuxöanqmca vacankqm  sravanAqmca  ..  °lanamca  fyao- hnanqm  Vi.  12. 2;  —  
=== leaf 1034 ===
wMa  ioa  ,.  'tpm syad^ram  vtr^zimnsm  Y. 3.0,2;  —  »M mqhrä  "die  gut  ausgeführten  Befehle"  Y.
_j. 4,  4.1,  Vi.iff.2'^;   im  Gegensatz
zu  duzvaHta-:  daityanqm  rahwyanqm 'lanqm  lyadhnanqm  var)zäi  pairi  . .  duz- variianqm  syaöknanqm  varjzäi  Vr.  7J. I,  a)  sonst  nur  neben  hüxta-  und humata- :  humataht paiti  manaahe  küxtahe paiii  vacatahs  °tahe  paiti  iyao%nahe  Yt 16.  6;  —  ästuyi  humatim  manO . .  küxUm vacö  .  .  •Um  syad^amm  Y.  J2.  8;  — fra- stuyl  kumaisibyascä  hüxtsibyascä  'tdibyascä mahwsibyascä  vax>hwSibyascä  varltvSi- byascä  Y.  //.  17;  —  nanm  alavamm dahrUfUm  kumatimca  manB  hüxümca  vac5 •Umca  syaohtum  Vr.  2.  5;  —  aa^. .  manya mananha  humahm  . .  hitsva  mrätoi  hUxttm .  .  sasiaiibya  var>za  't»m  syadhium  Aog. 25  ff.;  ^  *ar»m.maiti  *Aumata  mamne  (Sp. 1121  f)  *ar>m.uxti  *  hüxta  (vavaca)  anm.- varsti  °ia'^  (vavarfzd)F.2^; — yezi  kuma- tim  mainySt  kUxt^m  väcim  mrväl  'bm'^ v»nsyäl  syadhn»m  Gk-iöy;  —  narS  asa- vanö  humataü  mainimna  hüxtäU  ntrvats 'täis(3.\sOb}.)v>rpzyant3Y.jo.4;—AumiUa- nqm  hüxtanqm  •tanqm  iyadaca  anya- dacä  v»r>zyamnanqmcä  vävtmananqmca mahl  aibT.jaritärS  Y._J5,  aj  FrW.^,  i;  — "•"rfil^r* (sd,) ,  .paiti  nivaitis . .  humaialsuia haxtalsuca  •taisu^a^'*  ti.S4;  —  vTtpäi/ 'hwa   humatäii  .  .  huxtäis  .  .  'täis  pairi-
\jasämaidl  Y.36.  SJ  —  yS  hvqm  anhvqm
dby  Google
i85i
hvar§ta-  A
*hvaspa-
1853
yaozdäite  kumatäüca  küxtäUca  'täüca  V, 5.  2i;Ytj. 3;  —  haptavhatöii  humataca hüxtala  "tala  aiwig?r>%mahi
=== leaf 1035 ===
  Vr.  ly.  i ; Y.4'  1 1  H.  2. 1 4;  — yetihf  n^manhs  ciknm humahmüa  küxtimtä  °t»mcä  Y. $8.\',  — kais  hl  (näm!.  ahunahe  vairyehe)  afsman (sd.)?  humatim  hüxUm  °t3m  Y.  ig.  16;  19;
—  vSca  humata  hüxta  'la  äyesi  yeiti  Y.
J.  4;   im  Gegensatz  zu  duivarsta-  (und
duimüta-,  duiaxla-):  aibigairyä  (sd.)  dathi vispa  kumatäcä  hüxtäcä  't3cä  paitiricyä daikl  vlspä  dmmatacä  duiüxtäeä  dui- varlt3(a  Y. //.  17;  —  frastavattö  huma- taea  huxtala  °taca  niibanmnS  dusmalaca duiüxtaca  duävarstaca  H.  J.  7 ;  —  mä  hra- yqm  vaAUtanam  aiwi^yS  buyata  humata- lieca  mananhs  häxtaheca  vacaahB  'taheca fyad^nake;  "hrayqm  acUianqm  aiwt^yS buyata  dusmatake^a  matiatihs  duiüxtaheca vaianhs  duivarUah^a  syao\  nahe  V.  /A'.  1 7 ;
—  framtniti  humatanamca  häxtanqmca •tanqmca  paiHstätle  dusmatanqmca  duz- üxtanqmca  duzvarstanamla  Vr.  20.  a;  — vlspa  humata  . .  hlixta  . .  'la  bao63.varSta; vlspa  dusmata  . .  dtizOxta  . .  duivarsta  nöU baodd.varita  FrW.  3.  \\  —  nsit  malyö gae'^yS  sll  aojs  manyete  dusmatim  ya^a
mi^rasc'it  .  .    kumatim;    nSit  .  .  /"raoHirf^Q^^  *^^},i^^„^j,^  ..     al^  ^^^  ^^^     ' duiüxtfmya^a  mihrascij  . .  Auxt^m,  nStt  geschossener(Pfeik)"Y.57. i8.       hfasüm . .  Vfrfzyati  duwarstim  yaha  mi^rascil . .  |  ^k  Absol.  sbes.
'timYuo.io6;Gl.l63l;—  humatahe  ahmi\  pa.:  iBi'fl«(?)
=== leaf 1036 ===
,  Npü.:  «»/a  ra.-ffl'a«.  ~  ■>  WörtL duitnafaht  nSii  akmi  hüxtahe  ahmt  dui- 1  'als  ein  paar  (Preile),  die  ali  gut  geschossene Bxtahe  neii  ahni  'tahe  ahmt  dnivarstahe\  ffA"^.^""'"  '"den';  Pä.  fügt  erläuternd  tir nSit  aÄmiY.io.i6;  —  vlspa  humata. .hüxta  '■
*)    Die   man   durchschreiten  muis,   am   zum
ewigen  Licht  (anaira  ran/d)  zu  gelangen.
KompA.  —  Komp.;  Au' -\-varJta;  —  PiL:M/ari/ (Transskr.);  s.  noch  No.  3.  —  ')  So  (mit  •rflf) P.  i5,  N.  S4,  G5. 163.  —  ')  Pü. :  ^arset/ramÖH
•  j.  "^hvarStay-'^  f.  'gutes  Tun,  Handeln': mananhasca  ^humaiti  hizvasca  *hBxti tastayascä  'ti  *ra^wyg.varJN  (sd.)  Y.28.
Komp. :  hu'-\-varilay-.  —  Pü.  1  kvarll,  —  1)  Hdi.
•  j.  hvarStä-varaz-  Adj.  (fem.  'ti-)  'gute Werke  wirkend';  'r?zqm  alaonqm  .,  •mi- nqm  alaoninqm  Vr.  j/,  14.
Pü.:  hvarit  varzüär.
•  j.  hvars.hazaola-  Adj.  'mit  der  Sonne gleichgewilU':  amisä  spinta  vlspe  'sa  (NP.) Yt.  JO-  5 1 ,  'S- 9^;  —  n^rnS  vi  am?sa  spmtä vispe  •sä  (VP.J  Ny. /.  I.
Pü. ;  harvhp  fa  iant  iäaiU  itär[i),  Npü. :  tamäm yak  murad  äSrand»,  Sü. :  sarei  ciäbMIiiäk.
•  j.  hv-as6av-  Adj.  'des  Waden  schön sind':  hukf
=== leaf 1037 ===
TTtS  ahi  spttama  'tW  (NSm.)'> danyS-bizaus  Yt.  I/.22.
'}  Them. ;  auffaltige  Form,  die  einen  AS.  ir. *'iujfiim  voraussetzt.
•  j.  hv-asta-  Adj.  'gut  gevorfen,  ge- schössen':  i^a.vasma  (sd.)  .  ,  ya^cit  va- saite'tim  \l.  14.20;  —  äsyaaha{sd.)  'tayä
..•ta  vakist?m  *aah!im  ^afatii (Sp. 360  o.), Vlspa  dusmata. .dttzBxta.. duivarsta  aUslsm *anham  *asaiti  FrW.  j.  2.  A)  n.,  Sing. und  Plur,  Name  des  dritten  und  letzten der  drei  Vorräume  des  Paradieses*>:^i)iVrm gäma  frabarat y5  nars  alaonS  urva  humate paiti  nidähm  bilim  .  .  huxte  . .  'hritlm  .  . 'ie  . .  tBirlm  . .  anayralsva  raocBhva  nida- oäf  H.  2. 15;  ungeschickt  verwendet  Vyt. 54;  —  vTspfm  asai-an>ta  aya  ratu/rtta.. Jasmtun  paiti.barähi  humatäisca  hüxiäisca 'täilca  "jeden  Gläubigen  .  ,  nimm  auf  in Humata  und  Huxla  und  Hvarsta"  Y. ^5.4;  —  am>sanqm  spfitianqm  ..yalsqm ainyU  ainyehe  urvämm  aiwi.vaSnaiti  mtn- 'kw>ntfm{%i..)  humataSsu ..hüxtaisu ..'taisu .  .  *gar5   nmamm    Yt.  13.  84.  Wett-
los: näirikayai  .  .  hus.ham.sastayai  'tayäi Vyt  64.
j,  hv-ast«in  Absol,"'  'mit  gutem  Werfen', in  Verbindung  mit  dem  V.  'ah—,  apasi (sd.)  vasaite  arstil  yqm  *anhyeili  avi.- mihri/  .  .  yafS
=== leaf 1038 ===
t  hv  *aahyeiti  .  .  ".  .  die Lanze,  die  der  jl/iärafeind  wirft;  wenn  er auch  gut  werfend  wirft",  .  ."    YtJO.  aoC
Zum  V.  'ai-.  —  ■)  iBLld.  s.  asrul>m.  —  ")  Vgl. huMxiim  und  ZUBATY  IF,  3.  135.
•  j.  "hv-aspa-,  p.  "uv-aapa-  Adj.  (fem. 'Pä-)  'des  Ross(e)  gut,  tüchtig  ist  (sind)': 'ps  ahi  *hurähvS  Yt  i0.j6;  —  lä^wan.- satim  ayan.baranqm  (sd.) 
=== leaf 1039 ===
 'p3i  nai
=== leaf 1040 ===
re banmnSi
```


## [2026-09-14T01:58:31.520Z] TOOL CALL #21: Bash

```json
{
 "command": "ls tools/ && sed -n '1,40p' tools/ref_page.py"
}
```


### [2026-09-14T01:58:31.569Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
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
```


## [2026-09-14T01:58:35.487Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB leaf 64 (p.54) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==65' HUB.txt | head -60"
}
```


### [2026-09-14T01:58:36.855Z] TOOL RESULT

```
=== HUB leaf 64 (p.54) ===
— 54 —
Z. 2 stimmen, auch wenn es vorhanden ware, was
aber nicht der Fall ist: xcLvar-xudai = der Xavar-
herr Fird. I, 154, 465.
469. In den Nachtragen wird saxudan zerkratzen' (afgh.
LW. st^xudq 'scratched with the nails') hierher gestellt.
Aber 'kauen ist nicht zerkratzen' und xdyam nicht
Saxayam.
ill, NSldeke bezweifelt die Richtigkeit von Horn's
Etymologie: np. xuddi *Gott' = zd. *x^adaya- mit
voUem Recht, da ocudai = phi. x^atai (61. and. Ind.
p. 47, Bdh. Gl. 126, ZDMG. 31, p. 596, Nr. 34, etc.)
ein zd. *xwataya- oder auch *xwataia-^) voraussetzt,
die sich zur Not durch skr. svatas 4- ayu- Von selbst
lebend' oder skr. svatas + adi- Von selbst anfangend,
uranfanglich' (vgl. skr. svayambhu-) deuten liessen. Doch
sind diese Deutungen so unsicher wie die iibrigen. Vgl.
Fr. Muller, WZKM. 5, 65. Als Curiosum sei er-
wahnt, dass de Lagarde, Agathang. p. 159—160
deutsch Gott wieder (nach Burnouf) aus dem Per-
sischen {xodd = xudai) entlehnt sein lasst wie deutsch
gund (in Kunigunde etc.) aus pers. "^gund.
474. Vgl. ZDMG. 46, 234. Dazu arm. xarbzak 'Melone' (nur
bei Caxcax,)
475. Np. xarSang *Krebs' aus phi. karcang mit volksety-
mologischer Anlehnung an die Composita mit xar Esel
(vgl. Vullers s. v. xar 2), so dass nun das Wort
aus xar 'Esel' und cang *Kralle' zusammengesetzt er-
scheint.
476. Lies arm. xrat (fur xart),
477. Dazu kurd. vird, Mrs, hire 'Bar ZDMG. 38, 93.
478. Auf Grund der Pazendlesungen des Min. und Shk
setze ich x^arsand als Pehleviform an und lehne
die so wie so unsichere Etymologie Darmesteters
(= hu-rasant' gut-kommend' ab.)
*) Arsao. phi. *x^ataS, sp&ter phi. x^atai, paz. x^adai.
```


## [2026-09-14T01:58:54.879Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 125 (p.104) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==126' HRN.txt | head -70"
}
```


### [2026-09-14T01:58:55.953Z] TOOL RESULT

```
=== HRN leaf 125 (p.104) ===
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
itürk. /itnL'für. v.-ii:]. NOMtrkt: bei Uübschmann.
<>^at't. Elvi]]., r!^. l:'.:'.!. //tC'.ni, /i'Uc,
aw. vt-ri:l. x'^i^Ot*-: fthlv. /iff«ir id. i. ;frt<tef^) bezw.
/'td'iiw ai. Ytriji. >cj*iiid' Selbst I-Hrstininiung'.
LW. kiipi. ;f<^'r: af;. x'*'inii Oss. ;rwföi: bei. /*«*'*»
n. /»»(t*'!. /i '<»>'// i'..«oi.
Die Diirchsichtiirktrit Jt.-s Zusammenhanges mit l'^</*'
hat wohl Jas d i:eschützt : als Grundform ist etwa *?**
aw. /'adöffii' löder */»iit)'.*y'i-| anzusetzen. Nöldeic ^'
G^'A. l^SJ. .>. t«»:;i« bezweifelt die Richtigkeit 4^*^
EtvmoloKit' vielleicht nicht mit L'nreeht.
Fr. Müllers Erklärung jWZKM. 5. 6b) aus av^
*/ atö.ui/fio nach tiunem Willen sich bewegend*
schon an .>icii wenig Überzeugendes, ganz abgesehe
von der falschen awesti:?chen Xominativbildung.
47:i. yJrätnJden 'schreiten, ^ehen".
ai. l h'ntut'. knlwftfi. hrt'n/Uitr 'gehen, schreiten'.
In der Bedeutung angenehm, erfreuend* etc. ist,
wie schon Vullers gesehen hat. /jrüm ursprünglich
yu/rem. eine Ansicht, der auch Xöldeke beipflichtet
(mündliche Mitteilung».
47o. y/fi' 'Esel*, yj^ryö^ *Hase' (^^ *Eselsohr K /ercür, /«fr^^fAr«?
u. a. m.
aw. /ara- 'Esel : phlv. /ar: skr. khara- 'Esel'.
kurd. ier, liar (GuränT): SLfy./ar: oss. /ßräg, x^*'^9
(2i)7); bei. n. ffar, /ar, LW. har^) (192); wa/. ;rwr,
«ar. cer, üer, sangl. //tr, minj. xara.
*j Vcrgl. Ilorn, ZDMG. 44, 675, No. 134.
•; Vcrgl. Barthol oniao, ZDMG. 44, 550.
```


## [2026-09-14T01:59:09.795Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *47[0-9]\\. \\|^ *46[0-9]\\. \" HRN.txt | sed -n '1,40p'; echo \"=== search xud selbst ===\"; grep -n \"selbst'\" HRN.txt | head -20"
}
```


### [2026-09-14T01:59:09.864Z] TOOL RESULT

```
4207:460. {2)%ä 'Schulter .
4213:461. y^ar, x^^^ 'Fels; Dorn 2), x^*'^ (Häliz 16, 3), ;fä£?e?r
4217:462. '^Kitsten 'aufstehen*, Praes.;^e2-e/w (AM. 84 Zeile 2 v. u.),
4241:463. xäm *roh, ungekocht'.
4248:464. yritnös^) ^schweigend, still*, /ämösl.
4251:465. ^Jiän, yßne 'Haus , xänef/T.
4256:466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
4261:467. xäwer {/"äwer) 'Herr.
4264:468. ^äye 'Ei*.
4276:471. '/jtflfil. /u»*i «Tijit: HtiT. ;rM</4rfM</. /udäcendgür
4343:479. Y^urreni 'fröhlich, glücklich*, /iirirewT,
9930:469. Dazu se/üden zerkratzen' (Sahn. I, 222 Vers 1659,
9933:474. Vergl. Hübschmann, ZDMG. 46, 234 No. 17.
=== search xud selbst ===
4547:504. lud, ^eS (AM.) 'selbst'.
4549:ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
```


## [2026-09-14T01:59:12.088Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4540,4600p' HRN.txt; echo \"=== which leaf/page ===\"; awk 'BEGIN{RS=\"\\f\"} /504\\. lud/ {print NR-1}' HRN.txt"
}
```


### [2026-09-14T01:59:13.177Z] TOOL RESULT

```
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
Xüpih; ai. svdpas-'^),
504. lud, ^eS (AM.) 'selbst'.
Käs. x^d.
ap. vergl. wrö- ; aw. yyatö 'selbst'; phlv. ;^^a^, j^^'a/^Ä ;
ai. svdtas,
kurd. ;^i2 ; af/. ;t'/>'<^ ; oss. d. x'^^^^^9i t. /ädäg (298) ;
bei. i?a^, n. viixt^ vas; äiyn. ^w, sar. /w, wa;^. ;frti, gen.
505. x'*^* 'Sonne', hur, hör (reimt auf .<??^^ör; Sahn. 111,1105
Vers 693), Xurasan,
*) So korrigirt D armesteter, 6t. ir. I, 136.
') Yergl. Bartholomae ZDMG. 44, 552, Hübschmann ebenda
557, Geiger, Lautlehre d. Bei. § 15, 3. Uraprachliche Dialekt-
Verschiedenheit.
«) Ebenso Fr. Müller, WZKM. 5, r>7.- 112 —
aw. Iwar-; phlv. vergl. ;K?/r[pa;Y7// hez\^\ /var[varätt',
ai. svar.
kurd. /or, hilr[efaü; af;'. mar, nmar (Darmesteter>
Chants pop. XXXII); oss. d. yor, t. /Tir (306); si/n.
yer, yiv.
506. x^irsed 'Sonne'.
aw. hvare./sa^tem ^strahlende Sonne'; phlv. ;^"'arset
bezw. ;^?/r8rf, auch y^'arhsel (vergl. Hörn, Mitteilungen,
Heft IV, 34 No. 31).
507. y^itrden (FirdüsT, AM.: p^^'t'/v/ew ^)) essen, trinken',
/uräk, /^(lt\, /unl'i, /uris,
Kää. /ürfdri; /ürest,
ap. vergl. fxa()Tt\y6oa dy&Qomofdyog Ktesias; aw.
i/^X^'a)'-, yntraiti *essen'; phlv. /^'arfan, /^'ar(i)siij
yyartar, y^är etc., bezw. yurtan, arm. LW. yortlk
*Essen, Speise* (d. i. phlv. yurtik, AV.).
kurd. ymnn^ y^ärin essen ; af;'. yöral; oss. d. xvärun,
t. yärin (308); bei. varag, n. varay (404); si/n. minj.
ydr-am, sar. yör-am, sangl. y^är-afn.
Die l^y^m*' bedeutet sowohl essen' als auch 'trinken',
vergl. aw. äfs anaiui^.y^ared^a' (vd. 6, 31); ai. sürä-,
aw. hurä'^), lit. .wla (*Birkensaft') werden aber besser
zu i/^sav' 'auspressen' gestellt, woran Fick, Wörter-
buch^ noch zweifelt.
np. yurde, ynrd 'klein', phlv. yiirtak^ arm. LW. yortak
'zerbrochen, zerschlagen* kann nicht hierher gehören,
da es auf u reimt (Vis und RämTn S. 51, Vers 12,
V
Sahn. I, 179 Vers 905) und auch AM. u spricht; auch
mit aw. y^ara- 'W^unde* (de Lagarde) wird es schwer-
lich zusammengestellt werden können. Nöldeke
(mündliche Mitteilung), vergleicht lat. curttts 'kurz',
das zur [/^qert- 'schneiden' gehört. Die Aspiration im
Anlaut wäre dann neupersisch, wie öfter {yiramidev,
yerceng^ yired u. a. m.).
^) So auch immer in der Poesie.
*) EinmnI im Pehlevivondidäd, aber wohl nur umsohreibend, hur,
7d. 14 (72). - Zu aw. Inträ- vergl. Bartholomae, ZDMG. 37, 459.— 113 —
508. x^^> /ß^i ^^'^^ {^' i- X<^s, jüd.-pers.), (Sahn, /^^es^ daneben
äähn.O, AM.: ;kös) gut, schön, fröhlich* etc.").
Käs. x^Sj /öS.
=== which leaf/page ===
132
```


## [2026-09-14T01:59:20.165Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4500,4545p' HRN.txt"
}
```


### [2026-09-14T01:59:20.218Z] TOOL RESULT

```
LW. kurd. /(^r; afy. /'är; bei. vär (290).
Die Bedeutung 'niedrig, verächtlich' ist erst neu-
persisch.
497. i^äfiten 'wünschen, wollen, Praes. /"ähem, /"äliis,
/"äste 'Besitz'.
ai. l/^soad-, svädati 'sich schmecken lassen, Gefallen
finden*, svädate; gr. rjdoftat. Vergl. np. /iväi (No. 502).
phlv. yyastan 'wollen, wünschen', /^ah(i)§ff, x^stär,
y^astak 'Besitztum' etc.; kurd. /^dsthi , ;jfMSfni; bei.
vergl. västa 'für "(413).
498. x^äW/ 'Tischdecke; Tisch (gedeckter)'.
aw. /^'^aini' 'Teppich, Überzug, Decke',
kurd. LW. /an; af/. /^än; bei. n. vän 'Platte, Teller'
(289).
Geldner, Studien I, 17/8.
499. yiyänden Vufen, lesen etc.', /emden, /unlde, /unyä
'Musik, /unyäyer,
aw. l/";^^«;/- in /^anaf.ca/ra- ('klirrend'); phlv.
X'^äntan, /untt (GF.) ; ai. [/^svan-, sodnati 'tönen'.
kurd. y^ändin^ /ündin 'lesen; oss. d. /önim, i. xöJiin
'nennen , heissen , rufen , einladen' (305) ; bei. vänag,
n. vanay, vänganay 'lesen, recitiren, studiren' (412);
wa;f. ^an-am 'reden, sagen, sprechen'.
*) Sahn. I, 170 Vers 745 steht np. j^^är direkt im Gegensfttz zu
(hfsvär, wie im Awesta '^^äSra- zu (Inzä^ra-,— 111 —
500. ^fyalTden *f?chmeckon' , /^al 'Speise', /^älger, /^älf,
X^'ältger.
aw. x^arezista-; phlv. /^list (vd. 2 (77))'); arm.
l^alcr 'süss (sehr unsicher, H. No. 287).
501. polier \Sch wester, /ö/j.
g. yohr; Käs. /üh, yöh,
SiW. /^afihar- Schwester; phlv, /^'ühar, ytlk {PPGl.);
ai. svasar-; arm. ^^oir (H. No. 294).
kurd. xöh, ;c^A^» ^^^^ (H.-Sch.), af}'. yöt' ; oss. d. /ore,
t. ;ro; bei. gvahär, n. gvähar, göhär, gvär (131) 2); wa/.
;^m/, sar. ya;^, minj. yayvd, sangl. i/vd.
502. x^**^^*» /^^^^ 'Wohlgeschmack'.
skr. sräda- * Wohlgeschmack*.
kurd. x^ *Salz ; bei. väd, n. väd, vad\ vü:: (411)
'Salz.
In diesem Worte hat sich die ursprüngliche Be-
deutung der [/"svad- im Neupersischon allein noch
erhalten; vergl. /^'dfiten (No. 497).
503. y(nb gut, schön , /hIü.
Ka§. /ßh, /öb^ /eb.
aw. hväpah' 'wohltätig; phlv. /rap bezw. /üp,
```


## [2026-09-14T01:59:31.020Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Gewohnheit\\|Charakter\\|Natur, Gewohn\" HRN.txt | head -20"
}
```


### [2026-09-14T01:59:31.073Z] TOOL RESULT

```
984:phlv. ädlnak, ay\i\nak 'Sitte, Gewohnheit'.
4655:51G. ^j!lm 'Naturanlage, Charakter'-), vergl. hed^hn^ dns/lm,
8621:992. meniS, menisn (Wörterbücher) 'Sinn, Charakter,
10065:np. ener schlechter Charakter ist unbelegt (die laut-
```


## [2026-09-14T01:59:33.545Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4650,4680p' HRN.txt; echo \"--- leaf ---\"; awk 'BEGIN{RS=\"\\f\"} /51G\\. /{print NR-1}' HRN.txt"
}
```


### [2026-09-14T01:59:34.666Z] TOOL RESULT

```
denkt dagegen an ein ap. *kwäisiija' als Grundform;
zum Suffix 'ttja- vergl. ai. -tya-, Whitney, § 1245, b.
515. -^f^en (dialektisch yec) 'Pflug'.
aw. aem- (vd. 14, 10 (43)); phlv. /es(?).
Darmesteter, Et. ir. I, 77.
51G. ^j!lm 'Naturanlage, Charakter'-), vergl. hed^hn^ dns/lm,
duzyim {Vis und Ramm S. 32 V. 5 v. u.).
aw. vergl. haya-^ haem vd. 13 (124), pancö^\hya-
(Geldner, KZ. 30, 514 Note 1); phlv. /I?« bezw. /n;j
(vd. 13 (124), 5 (117) Gl.), huyjm (Gemme, ZDMG. 44,
068 No. 105), dus/wu
Anders und falsch Fr. Müller, WZKM. 5, 187; die
Bedeutung der aw. Worte steht jedenfalls fest.
517. x^?/'^» yJ^ 'Speichel', ylin (Gazophyhicium s. v.
saliva, Vullers s. v. ylm No. 3).
aw. gereöi.']yava'^ yt. 15, 47 (?); plilv. ;^ay?7Ä; (y. 38
(13) GL), yaya (Bund.).
Justi, Bund. s. v. yayü,
AM. gebraucht die Form yeön (208 Zeile 3 v. u., 209
*J Bedeutet auch bei Firdüsi 'fleissig, rechtschaffen* wie im
Pehlevi; ein np. ^^'es *Pflug' statt j^es (No. 515) giebt es nicht.
2) Reimt auf htm (Via und Rämln S. 51 Vers 9; 166 Vers 13),
dns sohon damals nicht mc»]ir bem gesprochoii wurde.- 115 —
Zeile 5, 232 Zeile 6, 7), vergl. ;^Mrfw (Vullers), /udn
(FR) ^). Die Zusammenstellung mit aw. geredi,]/(wa-
ist wohl falsch; das Nebeneinandervorkommen von d
(d) und y weist jedenfalls auf einen ursprünglichen
Dental hin, und so wird man auch im PehlevT besser
/adük, yadti lesen.
D.
518. dad 'Gerechtigkeit, Recht', dadistan,
--- leaf ---
135
```


## [2026-09-14T01:59:43.328Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xwad\\b\\|xwad \\|xwēš\\|xwadāy\\|xwah\\|xwāh\\|xōy\\|xēm\" PHD.txt | head -40; echo \"=== PHD_mackenzie ===\"; grep -n \"xwad\\|xwes\\|xwady\\|xwah\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-14T01:59:43.403Z] TOOL RESULT

```
124:~išn : [М tandis] ... add ёахгар |c hlk' | M cxr, № čarx] wheel, circle. čimīg ... add caused, justified, reasonable. dagrand-xwadāy ... delete eternal. dast-gir [dstgyl | N x]... delete: dst OHDWN, ...
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
665:xwarūfrān [hwl(’)wpl’n' | M xwrwpr'n) sunset, west. xwarrah [GDE < A gdh | (M prh, N farr)] fortune, glory, splendour. ~6mand [-’wmnd] fortunate, glorious. xwarséd, v. xwarxséd. xwartar [hw ltl] minor (sins). xwarwarān [hwlwPn!, -bPn'] = xwardfran. xwar(x)8éd [Azl(h)syt' | M xwrxšyd, № xuršēd] sun. xwāstag [NKSY A < A nksy’; hw'stk! | M xw’stg, N ~a] property, wealth. i ~õmand [-wmnd] wealthy. xwastan, !xwāh- [(Y)PLHWN-tn! < А V plh; hwstn!, hw'd- | J xwh-, N xwast] tread, trample; thresh. ~išn: trampling. xwāstan, *xwāh- [BOYHWN-stn! < A МУ Бу; hw'stn!', hwd- | M xw’stn, xt h-, N ~] seek, want, desire; attract, acquire. --j&n : desire, attraction. xwastüg [hwstwk!' | N xustū] confessing, believing. ~ih: confession, belief, faith. xwaš [BS YM < А bsym; hw | M xw, N ~] pleasant, sweet, nice. ~ih: pleasantness, pleasure. xwēd [Awyt! | M xwyd, N ~] moist, fresh. ~ih: moisture, freshness. xwédódah [hwytw(k)ds, -d^t! = Av. x"aetwada0a-] kin-marriage. xwēn-āhan [Ahw(y)n ?syn! = Av. x"aéna- (ayah-)] shining metal. xwēš [NP ŠE < А npf-h; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand [kwyš*wnd | N ~] relative, kinsman. xwēšēnīdan, xwēšēn- [/nwyfyn-ytn!] appropriate, make one’s own. xwēš-kār [леу dutiful. ~th: proper function. xwēš-tan [NPSE tn! | N ~] self. xwéy [hwyd | N xway] sweat, perspiration. xwistan [hwystn'] sweat, perspire. xwurd [hwlt' | N ~] small, little. xwurdag [hwltk' | N ~a] something small, particle; astr. lunar mansion; (horse's) pastern. ~ih: smallness.
703:absolute kāmag-xwadāy, kāmgār.
820:appropriate xwēšēnīdan.
891:attraction xwāhišn.
985:bent xwahl.
1443:crooked waxr, xwahl.
1570:desire (n.) árzóg, kam(ag), waran, xwāhišn.
1677:dominion šahryārīh; of long ~ dagrand-xwadāy.
1713:dutiful xwēškār.
1820:evil-natured dušxēm.
2063:function rāyēnišn; proper — xwēš- karih.
2330:householder kadagxwadāy.
2369:tll-natured wad-xēm.
2413:indeed xwad.
2415:independent kāmag-widār / -xwadāy kām-zīwišn.
2530:kinsman xwēšāwand.
2667:lord аху, bay, šahryār, xwadāy; ~ of the land dahibed.
2668:lordly xwadāywār.
2745:master awestād, rad, salar; ~ of the house kadagxwadāy, mānbed.
2825:misrule dušxwadāyīh; v. evil rule.
3023:own xwēš; make one’s ~ xwēšēnīdan,
3185:possessions grāmag, xwēšīh; v. pro- perty.
3371:relation, relative hamtohmag, xwēš- awand; bradarod.
3571:self grīw, xwad, xwēštan.
3572:selfhood xwadīh.
3573:self-indulgence xwad-dēšagīh.
3574:self-indulgent xwad-dēšag.
3673:sister xwah(ar).
4046:trampling xwāhišn.
4128:undutiful axwēškār.
4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
4984:kadagxwadāy kadagbünüg kadagig
5052:kimaghanjamih "age ” 425 kāmagxwadāy ^A pr 563 kāmgār > 56 8 1-2kāmag ($e 3 kāmagwidār ` 156 3 kāmrawāg 1 ө» e 4 kāmistan uerg s kastar `, Let 4 kástan 101635 4 kāč Q» 5 kābēn wars kāpūr N vays kādag Y4ve» 5 wast 25 A wasxwüstag 1341223920 эу "kay 24 drat “ys drodádwarih! >) мео 5 у kch SIE kahist 1825-65 4
5313:dastšūy dēwān dibīrīh dibīr dibīrestān 1%dabr, gabr Ixwāh-! xwastan! daftan daftar
5415:duSoxig dušox dušxwaršt dušhumat gūšūsrūd dušxwadāyīh dušāgāh dušāgāhīh dūšāram dušarz dušīh dujdānāg yojdahr yójdahrih yojdahrgar yējdahrgarīh dujdén dušgēwišn dujgand dujgandīh dujdēysšrīh dūšīzagīh dēšīzag dujdatt
5422:1*dēš-, duš- dušēwāzīh dušxēm dušxwār
5488:dagrand-xwadāy t pay KÉ
=== PHD_mackenzie ===
530:        dagrand-xwadiy .,. delete eternal.
640:       xwadiy ... read N xuday.
1360: a-xweskiir ['hwylk)l] undutiful.
1838:  ,...,-xwadiiy [-hwt'y] eternal, of long dominion.
2158: .......-xwadAyih [-hwt)yh] misrule.
3129:  ---xwaday [-hwt)y I P qdyxwd)y, N kadxudii] householder, master of
3166: ~-xwadiy [-hwt)y] independent, absolute.
5594:xwad [BNPSE < A b-,tlpi-h; hwt' I M xwd, N .......] self; indeed.
5596:xwaday [hwt>y I M xwd'y, N .......] lord.
5599:xwad-dOsag [hwtdwlk l ] self-indulgent.
5601:xwah [AIITE < A )~th I N -] sister.
5602:1, lIxwah., .......isn, v. xwastan, xwastan.
5604:xwahar [AHTEl, v. xwah; hw'hll (M xw'r), N xw4har] sister.
5605:xwahl [hw'hll (M xwhr), N .......] bent, crooked.
5619: ......ih: ease; v. also xwahrih.
5651:xwastan, lxwah- [(Y)PLHWN-tn l < A"; p[~; hwstn', h'llld- I J xwh-,
5666:xwes [NPSE < A nps-h; hwys 1M xwy(b)s, N .......] (one's) own.
5893:absolute kamag-xwaday, kamgar.               ebgat, petyiirag.
5936:alms ahlawdad.                            appropriate xwesenidan.
6014:attraction xwahisn.                      bat (anim.) sawag.
```


## [2026-09-14T01:59:51.905Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 132 (p.108) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==133' SYN.txt | head -50; echo; echo \"=== SYN leaf 109 (p.85) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==110' SYN.txt | head -30"
}
```


### [2026-09-14T01:59:53.129Z] TOOL RESULT

```
=== SYN leaf 132 (p.108) ===
 | Lat. coniugium, conutnin Dan. giftermaal, egte; bryl- Lett.  precéSands, lauliba; | tie ie ChSl. 6; rie 1 ) | : oe Sw. iftermdl, dkta; brél- .  brakit (maliizentstvo | een zoned, es SCr.  brak, Zenidba (2), Fr. see a oats 0: bodas OE weddung, sinscipe; udaja (b); svadba Bienes. cecil gifta, brgdhlop Boh. manielstvt, stiatek, Rum. Fe ranas ME  weddyng, wedlok, Zenitba (a), vdavky It. eh nak mariage (b); svatba a priodas; neithior NE marriage (wedlock); Pol. -malzenstvo, Slub; we- Br dimezi; eured wedding : sele : ; f Du. huwelijk, echt; brut- Russ. brak, supruzestvo, ze- loft nit'ba (a), zamu- OHG  hirat, éwa; britlouft Zestvo (b); svad’ba MHG hirdat, é(we); britlouft, Skt. vivaha-, patitva-, etc. hohzit Av. nairiéwana-
NHG heirat, ehe; hochzeit
Of the words entered, the majority, like NE marriage, cover both the state and the act of marriage (marriage as an institution, or the marriage took place). A few are used only for the married state, as Lat. matrimonium, NHG ehe. Many words are used only for the cere- mony, as NE wedding in its present usage. Such words are added, but separated by a semicolon.
In some cases there are distinct words for ‘taking a wife’ and ‘taking a husband’, corresponding to the dis- tinctive verbs (2.33). These are simi- larly indicated by a and b.
Most of the words for ‘marriage’ are obvious cognates (derivs. or in some cases the source) of the verbs for ‘mar- Ty’ and have been noted in the discus- Sion of the latter (2.33). Buta few, and many of the special words for the wed- ue ceremony, are of different origin. ae ee lit. OR ae (2.31), : . coniu(n)x ‘spouse en the usual legal term itehbecs ae , and nuptial ‘wedding’ ( >
= Seg see under nibere (2.33). : mmonium (>It., Sp. mat

=== SYN leaf 109 (p.85) ===
 man, OHG man, NHG mann, ete. (the most widespread Gme. word, with extension fr. ‘man’! to ‘man’); ChSl. madi (fr. *magjo- with a guttural suffix, as in Lith. Zmogus), SCr., Boh., Russ. muZ, Pol. maz (general Slay- ic word, with shift from ‘man’! to ‘man”); Skt. manu-, manus-, manusa-, manusa-. These point to an IE word for ‘man”!, but its root connection and so its ultimate semantic source are whol- ly uncertain. It has been derived from IE *men- ‘think’, or, since the designa-
tion ‘thinker’ seems too sophisticated, from *men- in an assumed earlier mean- ing ‘breath’ or the like; or by some con- nected with Lat. manus ‘hand’ (cf. NE all hands). Walde-P. 2.266. Falk-Torp 693. Feist 344 f.
In Germanic the prevailing meaning in the earlier period is ‘man’ (so Goth. manna reg. = avOpwros, only a few times = avyp). After the extension of use to include ‘man”, its place in the sense of ‘man’! was taken, except in English, by forms going back to a deriv. adj. like Goth. mannisks = avOphmivos. Hence OHG mannisco, mennisco, MHG, NHG, Du. mensch, Dan. menneske, Sw. men- niska. Falk-Torp 714. Weigand-H. 2.168.
In Slavic there was a complete shift from ‘man’! to ‘man’? and ‘husband’, and in part a later restriction to ‘hus- band’ with new derivatives in the sense of ‘man’, as SCr. muskarac, Russ. muzcina, ete.
3. Grk. aOpwros, etym. much dis- puted. But the old analysis av§p-wzos ‘man-faced, man-like’, fr. the stem of avip, avipds remains the most probable. Cf. Hesych. dpwp- dvOpwros, and for the semantic relation cf. OHG mannisco fr. man (above, 2). The change of avdp- to avOp- is due to a ‘in the second element (cf. répurmov fr. *Terp-rmov), which does not belong properly to the root é7- but may be due to the influence of dpaw. Kretschmer, Glotta 9.231 f., 27.246.
4. Ir. duine, W. dyn, Br. den, above, 1.
5. ChSl. Clovékti, ete., the general Slavic word for ‘man’! (SCr. covjek also ‘man”), whence Lett. cilveks (fr. Russ.), much disputed but best explained as epd. of a *éelo- (whence ChSI. éeljadi ‘household’) and *véki% : Lith. vaikas ‘child’, hence orig. ‘member of the house- hold’, with later extension to ‘man’!, Cf.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
. .
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 81
for ‘household’ but also d 141. Brug- eople. Berneker L Eee ‘ estgabe Kaegi 33. Briickner 79 (differently for second part of cpd.) G. Skt. (beside manu-, etc., above, 2) a-etym.? Uhlenbeck s.v. sere) magya- mostly ‘man”!, OPers.
SCr. éeljad coll.
martiya- ‘man’! and ‘man’?, NPers. mard ‘man’, Arm. mard ‘man’!, orig. ‘mortal’: Skt. mrta- ‘dead’, martya- ‘mortal, man’, Lat. mortuus ‘dead’, Grk. Bpords ‘a mortal’, fr. IE *mer- �
```


## [2026-09-14T01:59:58.219Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"2\\.45 SISTER\\|SISTER\" SYN.txt | head -10; echo \"---\"; grep -n \"swesor\\|\\*swesor\\|sve-sor\" SYN.txt | head"
}
```


### [2026-09-14T01:59:58.301Z] TOOL RESULT

```
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2908:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 2.44 2.45 BROTHER SISTER Grk. 4ded¢ds abehon NG abeAdeds, pop. Abephés 4deAH7, POP- d5epon s Lat. frdter soror It. fratello sorella Fr. frére se@ur Sp. hermano hermana Rum. frate sora Ir. brathir siur Nir.  dearbrathatr deirbhshiur W. brawd chwaer Br. breur c’hoar Goth. brépar swistar ON brddir systir Dan. _broder sdster Sw. broder syster (0) 0) brddor sweostor ME brother sister, suster NE brother sister Du. broeder zuster OHG  bruodar swestar MHG_bruoder swester NHG _ bruder schwester Lith.  brdlis sesuo Lett. bralis masa ChSl.  bratrii, brati sestra SCr. brat sesira Boh.  brair sestra Pol. brat siostra Russ. brat sestra Skt. bhratar- svasar- Av. bratar- x’ anhar-
3480:2.66 SISTER-IN-LAW
---
2641:4. Lat. -uzor ‘wife’: Arm. am-usin ‘spouse’, and to be analyzed as *uk-sor-, first part : Skt. uc- ‘be accustomed to, take pleasure in’, Lith. junkti ‘be accus- tomed’, ete. (Walde-P. 1.111), second part as in *swesor ‘sister’, etc. (2.45). Ernout-M. 1148.
2918:2.45. ‘Sister’. 1. IE *swesor-, prob. *swe-sor-, cpd. of the refl. *swe-, the sec- ond part related to the rare Grk. dap ‘wife’, Av. hairigt- ‘female’, Lat. uxor ‘wife’ (2.32), and the fem. numeral forms like Skt. tisras ‘three’. Walde-P. 2.583 f. Ernout-M. 958f. Wacker- nagel, Altind. Gram. 3.349. Benveniste, BSL 85.1.104 f.
```


## [2026-09-14T02:00:07.781Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"RELATIONSHIP 85\\| 85 2\\.\\|2\\.55\\|COUSIN\" SYN.txt | head -10"
}
```


### [2026-09-14T02:00:07.846Z] TOOL RESULT

```
1035:3. Gall. -magus in Arganto-magus, etc., Ir. mag, NIr. magh, W. maes, Br. maez, prob. as orig. ‘expanse’ : Lat. magnus, Skt. mah-, etc. ‘large, great’ (12.55), Skt. mahi- ‘earth’. Pedersen 1.96. Stokes 198f. Walde-P. 2.258 (ad- versely).
1519:ON skagr, Dan. skov, Sw. skog ‘woods’ : ON skaga ‘project’, skagt ‘promon- tory’, OE sceaga thicket’ (NE shaw), ChSl. skoditi, iter. skakati ‘jump’, etc., with development fr. ‘project, jut out’, (wooded) ‘promontory’. Walde-P. 2.557. Falk-Torp 1017. Hellquist 940.
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
2352:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 85
3207:Byz., NG dvefiss, dvefra (NG also avuiés, -4), with shift from earlier ‘cousin’ (2.55).
3208:3. Sp. sobrino, sobrina, fr. Lat. sobri- nus, -a ‘cousin’ (2.55). 4. NIr. garmhac
3227:2.55 COUSIN Father’s Brother’s Son (Daughter) d, Father’s Sister’s
3898:6. ChSl. skopiti (also skopict ‘ey- nuch’), SCr. skopiti (Boh. skopiti, Pol, skopté esp. of sheep, cf. skop ‘wether’), Russ. skopit’, fr. the root of Russ. SCepat’ ‘split’, Grk. oxérapyov ‘adze’, oxartw ‘dig’, Lat. caépd ‘capon’, ete, Walde-P. 2.559f. Walde-H. 1.161. Briickner 494.
5391:Goth. skuft (Jn. 11.2, etc. dat. sg. skufta coll. = 6prét ‘with her hair’), ON skopt (poet.), OHG scuft, MHG schopf, all coll. for ‘hair’ of the head (NHG ‘top of the head, tuft of hair’, etc.) : ON skauf ‘fox’s brush’, OE scéaf, OHG scoub, etc. ‘sheaf’, Walde-P. 2.555. Feist 435.
5422:4. ON skegg, Dan. skeg, Sw. skdgg : OE sceaga (once as gl. to Lat. coma), ME, NE shag ‘rough hair’ (whence the more common NE shaggy), ON skagz ‘promontory’ (with vb. skaga ‘project’), skdgr ‘woods’, etc. Walde-P. 2.557. Falk-Torp 1000. Hellquist 970.
```


## [2026-09-14T02:00:10.461Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2352,2380p' SYN.txt | cut -c1-1500"
}
```


### [2026-09-14T02:00:10.517Z] TOOL RESULT

```
MANKIND: SEX, AGE, FAMILY RELATIONSHIP 85
minino, feminale, etc. (but Mee mostly ‘feminine’ rather than ‘female );
1 orig. ‘giving suck’ : Grk. 6jo08at fuck’, Skt. dhayati ‘sucks’, etc. Walde- P, 1.829 ff. Ernout-M. 341, 343. Walde- H. 1.476.
3. Lat. mas ‘male’, also masculus (> It. maschio, maschile, Fr. méle, ME, NE male, Sp. macho), masculinus (> It. mascolino, Fr. masculin, NE masculine, now mostly of gender, attributes, etc.), etym.? Ernout-M. 594. Walde-H. 2.46 f.
4, OE wéepned ‘male’, also cpd. wepedman, wépman fr. wepen ‘weapon, penis’ (4.492, 20.21).
neo, fe
OE werlic, wifltc are used for ‘mascu- line, feminine’ gender (so Aelfric) but rarely, if at all, for ‘male, female’.
5. Skt. (beside adj. vrsan-) prefixed pums- or nara- (2.21) for ‘male’ human beings or animals. Similarly strz- (2.22) prefixed or added for ‘female’ human beings or animals.
Av. (beside adj. argan-) also adj. natrya- fr. nara- ‘man’ (2.21), for ‘male’ human beings or animals.
Av. hairisi- noun for ‘female’, applied to human beings and animals, perh. *har- : second part of IE *swe-sor- ‘sis- ter’ (2.45). Benveniste, BSL 35.1.104 f.
Av. x§a6r7- likewise noun for ‘female’, etym.? Barth. 547.
2.242 SEX Grk. —-yévos, gddov Goth. She Lith. gimtis, lytis NG dAov ON kyn Lett. dzimums Lat.  sexus Dan. kén ChSl. polit It. sesso Sw. kén SCr. spol Fr, sexe OE cyn(n) Boh. pohlavi Sp. sexo ME kynde, sexe Pol. pleé Rum. sex NE sex Russ. pol Ir, gné(?) Du. geslacht, kunne, sekse Skt. (linga-, jati-) Nir. — gné, cenéal, saghas ORG. Av. witeets W. thyw, ystlen MHG §gesleht(e) Br. rei NHG | geschlecht
The abstract notion of ‘sex’ is in many languages expressed only by words of broader scope, the special ref- erence to sex being shown by the context (as ‘male kind’ = ‘male sex’). But there are some distinctive words in which the Specialization to ‘sex’ is complete (so Lat. Setus, with derivs.) or nearly so.
e Semantic source is most com ‘sort, kind? (this often from ee Tace’), but in part ‘section’, ‘side’ ‘half?
» COmplexion’. he les ‘sex’ and grammatical ‘gen-
: ey expressed by ee » 48 In the case of Grk. But ihe ee gecynde, NHG geschlecht.
ay be differentiated, as in
Lat. serus vs. genus (with their Romance and English derivs.), NG ¢ddov vs. yévos, Russ. pol vs. rod (‘race, clan’ 19.23, ‘kind’, and ‘gender’).
1. Grk. -yévos ‘race, kin, clan’ (19.23), hence ‘class, kind’ and ‘sex’.
Grk. ¢i)ov ‘race, tribe’ (beside Puan, 19.23) and ‘sex’ (Aristoph., Xen.), lat- ter reg. NG.
2. Lat. serus (> It. sesso, Fr. sexe, Sp. sexo; Rum. sez neolog. fr. Fr.), be- side secus prob. : secare ‘cut’ (9.22), hence orig. ‘section’, but with prehistoric specialization to ‘sex’ (old etym. ques- tioned by Ernout-M. 935, but. still prob.).
3. Ir. gné ‘countenance, appearance,
ee In Public Domain. Gurukul Kangri Collection, Haridwar
see teepnatn eke oe oe
SLi hom
86
form, kind’ (: W. gne ‘color, hue, com- plexion’), also, at least in NIr., ‘sex’ in phrases with ‘male’, etc.
Ir. cenél ‘race, kin, kind’ (: cinim ‘spring from’), NIr. cenéal also ‘sex’ in phrases.
NI. saghas ‘sort, kind’ (etym.?), also for ‘sex’ in phrases ‘what kind is your child, boy or girl?’ (Dinneen, McKenna).
```


## [2026-09-14T02:00:15.859Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 689 690 691; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | head -25; done"
}
```


### [2026-09-14T02:00:16.881Z] TOOL RESULT

```
=== leaf 689 ===
��; OCS sokü, R. Srb. sok, m. “juice, sap’; Li. sakai, m. pl. ‘pitch, gum, resin’; OPr. sackis, id.
soquos, is, à (2) ‘utterance, declaration; ut- terer, denouncer'. WP II, 479. Cf. sequ- (2) and sequ- (2) Gk. ons gs: -idos, f. ‘vengeance’; Br. hop, pl. u, m. ‘cal’; OCS sokü, m. ‘accuser, plain- tiff; Srb. sók, m. 'denouncer'; Li. sakà, f. legend, tale’; cf. uZz-sakai, pl. “marriage banns'; (oxytonic prototype in) MHG sage, sf. ‘speech, rumour’; ON saga, f. ‘tale, saga"; E saw “tale”
soquos, à (3) “follower; following'. Cf. so- quios, soqu- (1) & sequ- (1) Alb. gjah, m. ‘prey’; OCz. sok, m. ‘rival’; Big. cf. po-soka, f. ‘direction’; Li. cf. sakùs, adj. *well-orientated'; péd-sakas, m. ‘track’
1249
soqusos “following, accompaniment, com-
panion, tracker, track, procedure”. Cf. sequ- (1), soqu- (1), etc. Skt. sakkah, sakkih, m. ‘companion’; Av. haxa, nom. sg. m., pl: haxaya, id.; Ober haxa-, cpds. id.; Gk. ópson, n. 'food eaten 'cum pane"; cf. opúō and opüio, v. “marry” beside a-Ossæð, v. ‘help’; Lat. cf. socius, m. 'com- panion, ally; OS seg, i-st., OE secg, ON seggr, pl. -ir, m. ‘man, warrior’ (fr. *soquís); OCz. cf. sok, m. ‘rival’. Here also Av. haxo, m. ‘sole of foot’; Arm. ak, Let, leg’; Phryg. (DW?) sükhos, m. “sandal; Lat. (LCW?) soccus, gs: A. m. ‘shoe, sandal’
_soqutos, is, cf. sequ- (1) & soqu- (1)
Olr. cf. sochuide, f. ‘crowd, mass’; (Ukr. cf. sokotyty, v. ‘watch’. Here?)
(sórb- ‘sup’, etc. Cf. srb-, surb- (surbh-) and WP II, 204. Var: srób-, sreb- in Li. All onomatopoeic. Thus in Alb. gjerb, v. id.; gjerbé, f. “leak, droplet’)
sorbhos "a fish? (?) “perch, bass, roach’ or sim. See Supt: S Gk. orphós, Attic: orphós, m. Cperch, bass? or sim.); Sw. sarv, m. ‘roach’
sorgh- (?)
Icel. sarga, v. (1) ‘hack’; Sw. sarga, v. ‘wound, graze, têar’; OCS sragü, adj. “awfuP. (Hitt. sarkus, adj. = ‘mighty, glorious’ or sim.) sorguhð ‘watch, observe, sleuth, pester’. (Evidence ambig.). Cf. WP II, 529 Hitt. sarkumi, v. ‘equip myself”; sarikuwas, s. (equipment? or “armed soldier”); Ir. suir- ghim, v. ‘woo’; (Go. sarwa, npl. ‘armour’; OE searu, searo, n. ‘craft, device’); Li. sargùs, adj. “watchfuP; Latv. sargs, m., sardze, f. ‘watch’; sargu, inf: sargāt (sic) ‘watch’. (Li. sarginti, inf. ‘make ill’ is factitive to type ser- guhō, q. v.). For Gmc. (ambig.) see soruos (1) sormos (sormonos, sormot-) ‘glum, gloomy, downcast, shamed'. Gk. ambig. cf. suorm- Cf. Gk. hormaíno, v. ‘sulk’ ?; Hes. hormanós, adj. ‘saturnine’?; OCS sramü, m. ‘shame’; sraméjo, čti, v. “be ashamed'; sramota, f. *shame'; Ukr. sorom, m. id.; Li. sarmatà, f. ‘shame’
soros (1) ‘filth; vermin’. Cf. sér- (3), seros.
For (2) see Supt:S. WP I, 410
soqusos — sotios
15
20
25
30
35
40
45
1250
Lat. cf. sor-des, s. ‘filth’; Ir. sor, pl. suir, m. *swine-louse'; W hor, s. pl. -od, id.; R sor, m. ‘dirt’; Cz. cf. seru, sráti, v. (cacare'; Li. sáru, inf: sárti, v. “get dirty
soruos, à (1) “protection, equipment, gear; protective’. Cf. seruó & sorguh-. (Gmc. ambig. but prob. here). WP II, 498 Av. hauro, adj. (2) ‘protective’; Gk. oúros, m. (guard). But to uer- for WH & Bois.); Lat. Cf. servo, äre, ob-servo, etc. (: Av. haurvai(mi), v. 'guard"); Go. sarwa, npl. equipment’, but cf. sorguh-); OHG saro, gs: sarawes, n. 'ar- mament'; MHG sar, sarwes, id.; OE searu (2), id. (1) = ‘craft, device?
=== leaf 690 ===
�there’; Gk. hó, hé, def. art. beside hos, hé, rel. pron.; OLat. sum ‘him’, sam ‘her’; SOS, sàs, pl. ‘them’; (Sard. su, sa, def. art. prob. fr. ipse); MIr. so ‘this; these’; cf. Ir. so-nn (‘here’, cf. Arm. ho-n ‘there’); Go. sa, sð, mf. ‘thi; ON sá, sú “that; the’. Extn. in Gk. hoíos, hoia, pn. ((such?. Ambig. cf. ios-); Av. hoyo *this'; Alb. ay, f: ajó “he, she’
sós- ‘flaccid, limp, tired; tire’. (also: *pen- dant" ?) Du. soes, m. ‘drowsiness’; soezen, v. *drowse'; Li. suosiu, suósti, v. tr. ‘tire, bore’; suosà, f. ‘trouble, nuisance’; suoslüs, adj. 'importu- nate’; cf. (?) Skt. sasna, f. ‘dewlap’; Srb. (?) sasa, f. ‘anemone’; cf. Cz. Pol. sasanka, id.
sotios “true, right’. Cf sntios, sontios, esnt-, snt-. (Indo-Iran. ambig.) Skt. satyáh, id.; Av. haigyo, id.; Ober hašiya-, id.; Gk. hósios, id.; cf. Olr. uisse, comparat: uissiu, adv. id. (phonol. uncertain); ON saór (2), id.; Lat. cf. (?) sos-, in sos-pes, -pitis, OLat. sis-pes (Fest.) ‘safe and sound’
1251
sough- (sougho; soughos, à, iə) ‘guard, watch, care’. Cf. WP IL, 472 Arm. hogam, v. id.; hog, o-st. id.; OCS cf. pro-sugü, m. “fitness, aptness'; pro-suZinü, adj. ‘suitable’; R cf. do-sug, m. ‘leisure’; Li. saugüs, adj. ^watchful; safe’; saugà, f. ‘safety, protection’; OLi. sáugmi, mod. sáugoju, oti, v. ‘save, protect’; Latv. saudze, f. ‘rescue; care’; saudzēju, ēt, v. ‘spare’
soutos, iə, us ‘surge, seethe; surging, boil- ing’. Cf. seuto, ið Skt. sótuh, m. ‘soma-pressing; soma-libation'; Go. saups, m. ‘sacrificial offering’; MHG sot; MHG sot gs: sodes, sm. & n. “boiling, brew'; OE (queried) seaóa, m. ‘heartburn’; cf. G Sod-brennen, id.; OE séap, m. ‘spring, sour- ce’; ON seyðir, m. pl. ‘cooking-fire’; Pol. suty, adj. 'abundant' ; Ukr. sutyj, id.; Latv. saute, f. 'fomentation, scalding, steeping’; Li. cf. siau- tis, gs: -Cio, m. ‘squall’ beside (z-gde) siütis, gs: -Cio, m. ‘rage’
spadha *lath, spatula, spade’. WP II, 653 Gk. spáthe, f. “blade, weaver's reed; MHG spate, OE spadu, f.; Du. spade, f.; ON spaói, m., G Spaten, wm., Sw. spade, wm. ‘spade’
spagó (sphago), ið “break out, erupt’ Gk. spházo & sphátto, v. ‘cut, slay’; MHG spachen, wv. tr. ‘crack, burst’; G cf. Spach, m. ‘chip’; spachern, v. ‘crack open, get chap- ped”. (Isophones: Arm. pakem, v. ‘shut, fas- ten’; pak, i, iv ‘closure’; ON spakr, spak- ‘gen- tle’: Sw. spácka, v. ‘cram’)
spaið (spanið) ‘stretch, force, cram’. Cf. spanos Arm. cf. hy-panam, aor: -paçi, v. ‘get crammed’ (if fr. *pul-9); Gk. spáð, v. ‘stretch; skin’; cf. spátos “skin” and spanós ‘rare’; Alb. fàj, v. tr. (cram', fr. *spanio); Lat. cf. spatium, n. (space, lit. stretch"); OE cf. (?) spanan, sv. 7. ‘lure’. (Isophonic: Av. spayei(mi) “fell; re- move'; spayo, m. “hiding, burial)
spanos (sphanos) “stretched, drawn, spun out, rarefied, thin). Cf. spaið Arm. cf. panak, panaki, adj. “puny, mean’, cpd. of ak ‘leg’?); Gk. spanós, adj. ‘rare’; MHG span, gs: spannes, sm. ‘stretch’; span- ne, swf. ‘span’. Kl. *-nn- expressive’; Du. span,
sough- (sougho; soughos, à, io) — speis (spé-)
10
20
25
30
35
40
45
1252
f. ‘span, lapse’; spanne, f. ‘period; mounting of a saw’; span n. ‘pair, team’; Icel. cf. spana. v. ‘egg on’; OE spanan, sv. 7 ‘lure (beside Icel. spenna, v. ‘clasp, buckle’); cf. also per- haps OS gi-spensti, 10-st. ‘enticement; Gmc. -nn- suggests a variant of type *spondh-; Cz. spona, f. ‘cramp, clasp’ (prob. here, despite HK: pnout)
spargos, à (spharg-) ‘point, prick, dot. Cf. sprg- (sphrg-) Av. sparoyo, m. ‘spike’; Lat, cf. spargo, Gre, v. ‘sprinkle’; Gk. spárge, f. ‘lust’; OE spearca, m. ‘spark’; MLG sparke, wm. id.
sparó, ið (sphar-) ‘seize’ (?) Arm. parem, parim, v. ‘cling; embrace; MHG sparen, wv. 'save, delay'; cf. ane spar, sunder spar ‘without delay”; Cz. spoti
=== leaf 691 ===
ti, inf. save’: G sparen); OE sparian, v. ‘spare, save, refrain’; ON spara, v. ‘spare, withhold, refrain’; sparr, adj. ‘sparing’. (Vowel ambig. cf. spor-) (4)
sparnos, is, jo ‘tip, point, pin, pinion’. Cf. sparg- and WP II, 21 & 602 Alb. ferrë, f. (briar, fr. *sparnio); Gaul. spar- nos ‘thorn’; Br. spern, m. id.; Cor. spern, coll. ‘briars, thicket’; Li. spařnas, m. ( ‘wing, pinion, fin’. Phon. ambig.); Latv. spārns, m. id. (The phonology of the Br. & Cor. terms is un- usual; the expected initial is *f-)
spartos, om ‘string, fibre’. WP II, 667 Tokh. A spartu, s. ‘knot of hair’; Gk. spárton, n. ‘rope’; (alleged) OLi. spartas, m. ‘bond, tie’
spatos, cf. spaið (spanið) and spendh-, spondh- ‘stretch’, etc. Gk. spátos, eos, n. ‘skin’; Lat. spatium, n. ‘space’
spēið ‘divine, soothsay, foresee’. (Distinct from sphēið, q.v.). See next, and cf. WP II, 660 & 680 Lat. cf. spero, are, denom. ‘hope’; Br. spía, inf. “hope, expect, observe’; ON spá, Sw. spå, v. ‘forecast’; Li. spéju, spéti, v. (1) ‘guess at, suspect, foresee’
speis (spé-) *foreseeing; foresight, forecast". Cf. speio. WP II, 660 & 680 Lat. spēs, gs: spei, f. ‘search, hope, joy’; Br. spi, m. ‘wait, hope, notice’; ON spá, f. pl: spar “prophecy”
1253
spek- (1) “look, see, observe’. WP II, 659 Skt. spas, m. ‘beholder’; (long-gde in) spåsa- yàmi, v. ‘show’: Av. spas, m. ‘spy’: spasya, 1sg. ‘wish to watch’; Gk. cf. (metath.) sképtomai, v, tr. ‘view, spy, consider’; Lat. specio, specére, v. ‘see, look at: OHG spéhon, MHG spëhen, wv. ‘spy, watch’; ON. Sw. speja, f. ‘spy’; (long- gde in) OHG, OS spáhi, MHG spzhe, adj. *wise, comely'; sf. *wisdom, comeliness'. Cf. also Lat. specium, n. ‘probe’; species, f. form, likeness, vision”
spek- (spekos, spokos, us) (2) ‘cave’ (?). (Arm. a LW from Lat. fossa via Gk.?)
Arm. pos, o-st. ‘ditch, hollow’; Lat. specus, gs: -üs, m. “cave
spektis, os, us (spoK-) “seeing, sight, view,
review, purview'. Cf. speK- (1) Skt. spastah, pp. & adj. ‘clear’; Av. spasta, obl: -tar, m. ‘watchman’; (LW from Iran. in) Arm. Spas, u, u, S. (service, cf. Per. sipás 'thanks- giving"), beside past, i-st. (? also an Iran. LW) “proof, reason, plea’; Tokh. cf. spaktàn, s. "ser. vice’; Gk. cf. (metath.) sképsis, f. 'considera- tion’; Lat. spectus, gs: -üs, s. ‘sight’: W ffes, m. ‘insight’, fr. *speKtis, cf. nos < *noktis or *nokts; ffesu, inf. ‘see through’; MDu. cf. spiede, spie, m. ‘spy’
(spel-, see sphel-)
spelé$hnos, à (speloghnos, à, splighén-)
‘spleen’. (Cons. and vowels anomalous. Prob. a cpd.) Skt. cf. plihan, m.; Av. sporozn; Per. supurz; Arm. pajcayn, gs: pajceyan; Gk. splén, gs: splénós, m. id. beside a-splenion *spleenwort'; splágkhnon, n. “bowel'; Lat. lien & lienis, gs. id. m. ‘spleen’; MIr. selg, Ir. sealg & seilg, f. id. beside seabhag, m. (sic), id.; Br. felch, m. id.; OCS slezena, f.; OCz. slezeň, m., R sele- zën-ka, f. id.
spelg- (sphelg-) (1) ‘faint’
Skt. phalgúh, adj. (2) ‘feeble’; Li. cf. spelgiù, "ti, v. ‘droop, wither spelg- (sphelg-) (2) ‘chip, splint’ Arm. peyk, Let ‘slat, flap, shutter’; Alb. cf. flegé, pl. a f. ((chip?, prob. fr. *splg-); Ir. spealg, speilg, f. (‘splinter, crag’, fr. *sph-); OE spelc, s. ‘splint, chip’; ON spelka, f. id.; Sw. cf. ben-spjalk ‘splint’. (Isophone: Latv.
speK- — sper- (spher-)
10
20
25
30
35
40
45
```


## [2026-09-14T02:00:23.254Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 739 740 741; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | head -40; done"
}
```


### [2026-09-14T02:00:24.331Z] TOOL RESULT

```
=== leaf 739 ===
 éthos, gs: -eos, n. ‘custom, habit'; cf. ethá- leos, &thaios, adj. “familiar”; cf. Lat. sob-, sub-
' jn soboles, suboles. f. ‘offspring
sueib- ‘fling, hurl, swing’. Cf. suib-, suibol-, suibros, etc. (O-gde: suoib-) MHG swifen, sich -, sv. 1. ‘rush’, cf. (o-gde) umbe-sweifen, wv. ‘fling round, wrap’; (z-gde in) swif, sm. “dash, fling'; OE swipian, v. ‘whip’; swipu, m. ‘scourge’; swipa, wm. A swipe, wf. id.; E swipe ‘bascule for raising water; to swipe ‘to lash’; LG swepen, v. ‘flog’; swep, f. ‘whip’; Latv. sveibinaju, v. ‘hurl, swing’. (For Gk. am-eíbo, see ueib- (uoib-))
sueibh- ‘blow, gush, sweep, gust’. Cf. suibh- Ir. siabaim, v. ‘wipe; blow, drift; (*-1- in) síobaim, v. id.; OE swifan, sv. 1. ‘turn, sweep’; ON svífa, sv. 1. ‘swish, whirl
sueidh- (1) (suïdh-) ‘dash, fling, hasten’. Cf. suidh- Gk. cf. eithar, adv. "at once? beside ithüs, adj. (1) ('straight, immediate" fr. *suidh-); z-gde in Lat. subitus, adj. ‘sudden’ and per. haps also in in-subidus, adj. (silly, fr. *nsuidh-. For subidus ‘filthy’, see süs ‘pig’, etc.); It. cf. séidim, v. (2) ‘incite’; Li. sviedinys, io, m. ‘missile’ beside svýdis, gs: svydZio, m. ‘fling’; Latv. sviežu, sviest, p. t. sviedu, v. ‘throw, fling’; sviesties, refl. ‘succeed’; (o-gde in) svaidu, inf: -it, v. (1) ‘fling’; ON cf. sviða, f. ‘cutlass’
sueidh- (2) (suidh-) ‘burn, itch, smart’. (For Gk. ídé: Li. svidùs, etc. cf. suid-) Lat. subo, ére, v. (“be in heat fr. *suidh-); OHG (Frankish: Otfr.) swidan, sv. 1. “burn, smart'; Sw. svida, sv. 1. id.; ON svíða, sv. 1. ‘singe, roast’; intr. ‘smart’; *suidh- in sviða, f. “burn, singed object’; sviði, n. ‘smart, burn’; (o-gde in) Cz. svědět, inf. (“itch, fr. *suoidh-)
sueig- (suoig-, sulg-) ‘turn, twist, spin’. Cf. suoig- as sep. entry W cf. chwi, pl. on m. (‘quick turn, spin’, fr. *suig-); MHG swich, sm. “going, passage of
1343
time’; be-swich, m. (1) ‘departure’; OE swican, sv. 1. (1) *wander, MLG (z-gde) swicken, v. ‘hop; wind, bind’; Du. zwikken, v. “get sprained, be wricked'; zwik, m. 'sprain'; E to switch, v. ‘to change"; Icel. cf. svikull, adj. 'elusive'; Cz. (initial variant) švih, m. ‘élan, dash” beside svižný, adj. ‘sprightly’; Li. cf. (o-gde) svaigüs ‘dizzy; intoxicating’. (For OE swican (1) (cheat; Sw. svika, v. id.; svek, n. ‘cunning’, fr. *suoi$- see suei$-)
sueig- (suig-) ‘delude, lure; wander, rave’. Cf. sui$no, ið Arm. cf. keni, gs: Kenvo, ab. s. Kcneav, adj. '*wheedling; Kcnim, v. ‘flatter, wheedle’; OHG, MHG swichan, swichen, v. ‘delude’; swiche, sf. ‘fraud’; OE swican, sv. 1. ‘deviate; delude, cheat; (*-i- in) swic, n. ‘delusion’; ON svíkja, sv. 1. as OHG; svik, npl. as OE; r. cf. seaghain, adj. ‘lovely’; seaghais, f. *pleasure' (ambig.)
sueió (sueiio) ‘make one's own, acquire, ac- custom'. Cf. sue-, seu-, etc. Skt. svàye, mp. ‘act on one's own: Lat. sueo, ere, v. ‘accustom’; Czech cf. u-svojit, inf. *ac- quire’. See next and cf. sutios. WP II, 455 & 470
sueios (genitive); suoios (possessive) ‘own’. (Strictly suei- "de moi’; suoi- (à moi’, etc.). Variant sulios, q. V. Skt. cf. svayám, invar. ‘self; svayüh, adj. “alone, isolated'; Kurd. xéw ‘owner; house- hold spirit; Oss. cf. jáxi, Dig. áxe Ceelt" fr. *io-sue-, or sim.); Gk. heós, é, ón, adj. own: Locr. wéos, id.; Myc. cf. wojo-, id.; OCS and com. Sl. svoj, a, o, adj. id. (from *suei- or *suoi-, cf. novü fr. *neuos). For Skt. svryåh, pl., sviya, & G dial. Ge-schweie, see suiios
suekrüs (suekrüs, KueKrüs) *mother-in-law'. Cf. sueKuros. WP II, 521 Skt. $vasrüh, id.; Per. xušū, id.; Arm. (variant) skesur & kesur, gs: skesri, ab. s. skesrav, id.; Gk. hekurá, id.; Alb. vjehërr, id.; Lat. socrus, gs. -üs, id.; W chwegr, Cor. wheger, pl. whegrow, id.; Go. swaihro, OHG swigar, MHG swiger, OE sweger, ON svzra, cf. Sw. svár-moder, id.; OCS svekry, pl. svekrüve, id. (variant consonantism); Li. cf. SeSiure, id.
(sueKs, sueKsti, variant
=== leaf 740 ===
 of type ksueKs,
suei?- (suig-) — suelo
10
20
25
30
35
40
45
1344
ksueKsti, q.v. ‘six. Cf. WP II, 522)
suekuros (suekuros) ‘father-in-law’. Cf. suekrüs. WP II, 521 (Skt. KueK-) Skt. svásurah, id.; Av. xwasuro, id.; Per. xusur, id.; Kurd. xezür, id.; Gk. hekurós 'father of husband’; Alb. vjehërr, m. 'father-in-law; Lat. socer, gs: soceri, id.; W cf. chwegrwn, d: Go. swaíhra, wm., OHG swéhur, MHG swé- her, OE sweor, id.; Li. (variant) SéSiuras, šēšu- ras & SéSeras, id.
(suel-, cf. suelo, suol-; suél-, see suelo)
sueld- “perish, decay; ruin, destruction’. Cf. suold-, suld- and suelo Go. swiltan, sv. 3., OE sweltan, ON svelta, sv. 3. id.; Sw. svälta, p. t. svalt, pp: svult, v. ‘starve’, intr.; cf. (type *sulds in) Oss. xälc (2) ruin, decay’; Arm. Kayc, gs & ab. s. Kaycu, s. ‘hunger’; Go. swulta-, cpds. ‘death’; ON sultr, m. ‘famine’; Norw. sult, s. “hunger” beside ON soltinn, OE swolten, pp. ‘perished’. (ISophonic in MHG swélzen, sv. 3. ‘burn’; E to swelter & sultry, prob. here also)
suelko (possible variant of type *selquó cf. sulquos) (?). Cf. WP II, 507 Gk. cf. hélko, fut. hélkuso, aor. heílkusa, v. “drag, téar' beside aphelküo, v. ‘drag off; Alb. helq, heq, hjek, aor: holqa, hoqa, v. ‘draw, pull’; Mir cf. (?) selc, selca, f. ‘hunt’; (W hel, hela, inf. ‘drive, round up, bunt represents a type *selg(h)-)
sueló (1) “burn, smoulder, blaze’. WP IL, 531 Skt. svárami, v. (2) ‘shine’; svar, n. ‘sunlight’; Av. Xxwar-, v. ‘shine’; hvaro, n. ((sun': Skt. svar, svaruh 'sunshine?)); Per. (ambig.) xuval, s. (lampblack', but cf. suord-); Gk. belle & héle, f. “heat of sun: also hélé, f. id. cf. eláne, f. lamp, torch'; dial. weléna, f. beside heléne, f. ‘goddess of light’; Lat. cf. sul-phur, z-gde (sulphur, w. semantics of OE cwic-fyr *'sulphur); OE swelan, intr. ‘burn, be burned? beside swaelan, tr. ‘burn’; G schwelen, v. 'smoulder'; ON svaela, wv. ‘choke’; f. ‘dense smoke’; Li. cf. svelmē, f. ‘smoke’; Latv. svelme, f. ‘glow’; (z-gde in) Li. svýlu, svilti, v. 'smoulder'; Latv. svilstu, svilt, v. ‘glow’; Fris. svilja, v. (dry, fr. *suelið); a possible cpd. in deíle, f. “twilight. The initial (su-) is explicit in Hes. (Lacon.) wélan, acc. ‘glow’
1345
beside (dial.) béla, id. Extn. (of type *sueld-) in MHG swélzen, sv. 3. fsmoulder'; cf. E swelter, & sultry (z-gde)
suelo, ið (2) “turn, bring” Lat. cf. soll- in soll-emnis (*'annual', hence ‘ritual’; soll-ers, -ertis, (/clever, lit. *turn-skill, semantics of G ge-wandt, R oborótlivyj, Cz. obratný clever); cf. also con-sulo, ére, v. (“bring together”, fr. *kom-suel-) (variant con- solo); Olr. cf. sel, m. “turn, time, space; Ir. seal, pl. -ta, m. (id. and *course"); cf. sealán, m. ‘withe for faggots, rope’; W chwel, pl. -ion, f. ‘turn, course’; chwelyd, inf. ‘turn over’; dy-chwelyd, inf. ‘return’; Cor. whël, f. as W; de-wheles, inf. ‘return’; Du. zwelen, tr. ‘turn — hay’; Sw. söla, v. (Ctarry', phon. of Norw. sómme ‘swim’); Latv. svelties, rett, *hurtle'
suelo (3) ‘surge, swell. (Common Gmc. swëll- from *sueln-: FK. DEW: schwellen) Per. cf. ab-xvar, -xvard, s. ‘source, spring’; Gk. cf. hális, adv. Cen masse, surging’, fr. *suluit or sim.); Lat. cf. in-solesco, Gre, v. (1) ‘swell beside solidus, adj. (“firm?, prob. fr. *suelid-, not as WH to sollus); MHG swéllen, sv. 3 ‘swell; faint with hunger
suelo "waste, consume’. Cf. suelo (1) Oss. cf. xwali, soht s. (corpse; Arm. cf. n-Koyem, v. (famish; faint w. hunger”, fr. *ni-suel-); EME sweal, v. ‘melt’; E dial. sweel away ‘die off" (isophonic in OE swælan, tr. ‘burn’); Icel. cf. sólunda, v. w. dat. tr. (^waste, consume’. Vocalism of sópa, v. sweep"); Lat. solo, are, v. (1) "lay waste’; (isophonic: Sw. svål, m. “horny skin, sward’; MHG swéllen, sv. 3. (2) *faint w. hunger?)
suelos, ios “close relative'. WP II, 533 Per. (?) xalü, s. “maternal uncle’; Oss. cf. (?) án-suvar, 
=== leaf 741 ===
üfsímàr (“brother? fr. *en-, *epi-^?); Hes. cf. aélioi, mpl. ‘men married to sisters in the same family'; Gk. cf. eilíones, pl. id.; Alb. cf. vlla, gs: vllau, pi. vllazën, T vë- llezér, m. (^brother', a synth. cpd.); Lat. cf. solus, adj. (alone; cf. sólor, àri, v. ‘cheer beside sodalis ‘comrade’; soleo, Gre, v. "be wont (Lat. forms fr. *suel- & *syel- 9); ON svili, pl. svilar, m. (brother-in-law^; pl. ‘men married to sisters of the same family")
suen- (suén-, suenmn-) (1) ‘sound, echo,
sueló, ið — suenĝð, ið
10
15
20
25
30
33
40
45
1346
‘ting’. WP II, 524
Skt. svanáh “sound, roar, tone, song'; svanáh ‘noise’; svanámi, v. ‘resound, echo’; Av. xwan-, v. id.; Per. xan-, cpds. ‘reading, singing’; xanam, v. (read, sing, all: Oss. xonín, v. ‘call’; Lat. sonus, i, m. ‘sound’; sono, äre, pf. sonul, v. ‘ring, sound’; MIr. & Ir. seinm, gs: seanma, s. ‘playing of music, singing’; (denom. vb. in) seinnim, vbl. root seinm ‘play — music’; OE swinn, m., swin, n. ‘me- lody’. (Uncertainly Gk. apos, n. ‘speech, tale, praise’; ainë, f. “praise, fame’, if fr. *sunio-, io)
suen- (suén-, suenmn-) (2) “think, suppose; thought, care, attention? LLat. sonium, n. (care*: Fr. soin, It. sogno); sonior, åri, v. ‘care’; LG swänen, v. ‘suppose’; G (fr. LG) mir schwant ‘ʻI have a feeling"; ON cf. svinnr, adj. (2) ‘wise’; svinnr, m., svinna, f. “sense, wisdom. (For Blg. svén, m. *shyness', see suoin- and cf. suln- (2))
suendho (suondh-) ‘wane, vanish, faint, pine’. Cf. sundh-. WP II, 526 OHG swintan, MHG swinden, sv. 3. id.; OE swindan, sv. 3. id.; OCS cf. pri-svedajo, -Svedati, v. ‘faint’; pri-sveno, -noti, v. (1) ‘wither’; (o-gde in) Arm. Kandem, v. facti- tive: ‘destroy’; MHG swenden, v. ‘abolish, clear — forest? (ambiguously z-gde in Gk. ánthrax, m. “carbuncle, cattle disease")
suengh- (1) ‘brandish; sword, surge, swing’ (For Gk. égkhos, n. ‘sword, lance, arrow’; Myc. e(n)kea, pl. ‘swords’, see sengh-); OHG swinga, f., MHG swinge, wf. “bat; sword'; OE swing, n. ‘surge’, cf. swingel, f. “whip, lash, blow'; E cf. swingle-tree (of cart); Du. cf. zwingel, m. 'flax-beater' beside (o-gde) zwengel, m. “handle, arm’
suengh- (suongh-) (2) (?) ‘thin’. See next. (Irish ambig.) Olr. seng, Ir. seang, adj. ‘thin, slim, lean’; ON svangr (0o-gde), id.
suenĝð, ið ‘squeeze, constrain, torture; toil, falter, waver’. Cf. WP II, 526 Skt. svañje, sváje, mp. ‘clasp, embrace’; MIr. & Ir. seangaim, v. ‘press, squeeze; reduce’; intr. (‘waste away’. 2 wds? cf. suengh- (2)); OE swincan, sv. 1. ‘toil, languish’; swinc, n.
 
1347
‘hardship’; Sw. svinka, v. ‘falter, waver’
suens- extn. of type suen- (1) q. v. Olr. séis, f. (“music”), perh. fr. *suns-); OE swinsian, v. “sound, ring”
suent- ‘dash, rush,  swish, (Onomat.). (Irish variant: sunt-) Gk. (ambig.) éntos, usu. pl. éntea, n. *fighting- gear”; Lat. cf. sonticus, adj. (harmful; epilep- tic, cf. G Schwind-sucht); Go. swinps ‘strong’; MHG swint, swinde, adj. (strong, quick, violent, sharp, evil, dangerous; OE swip “strong, severe, violent; right-hand’; swidan, sv. 1. “strengthen; attack’; Mir séitim, sétim, v. ‘blow; flow, gush’; ON svinnr 'swift; shrewd'; (mod. also 'stingy")
suepnið ‘dream’. See next, and cf. suepó, supnos Lat. somnio, are, denom. id.; OE swefnian, v. id.
suepnos, om 'sleep, dream. Cf. supnos and next. WP II, 523 Skt. svápnah, id.; Av. xwafno, wd: adj. "dor, mant; Per. xwab, as Skt.; Lat. somnus, 1, m. ‘sleep’; somnium, n. ‘dream’; MHG swép, gs: swébes, sm., OE swefn, n. ‘sleep’; ON cf. sofa, p. t. svaf, v. ‘sleep’; sofna, v. ‘fall asleep’; Sw. somna, v. “sleep”
suepo, ið (1) “be drowsy, sleep’; suopeio ‘tull’. WP II, 523 Skt. svápami, svápimi, v. ‘sleep’; Av. xwap-, v. id.; Per. xuftan, inf. beside xabam, xabidan, v. id.; (variant in) Per. xuspidan, Av. xwafs-, Oss. xüssin, inf. id. (fr. *sueps-
```


## [2026-09-14T02:00:30.243Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 742 743 744; do echo \"=== leaf $i ===\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n+1' IEC.txt | head -60; done"
}
```


### [2026-09-14T02:00:31.273Z] TOOL RESULT

```
=== leaf 742 ===
or *suepsK-); Lat. sopiO, Ire, v. Cu fr. *suep-); OE swefan, sv. 5. “sleep; cease’; ON sofa, p. t. svaf, id.; Sw. sova, id.; cf. (o-gde) OHG swebjan, swebben, v. lul; ON (e-gde) svæfa, inf. id.
suepó, io (2) ‘sway, hover’. WP II, 524 Lat. cf. sopio, onis, m. ‘penis’; OHG swébon, MHG swében, wv. ‘dangle, sway, hover’; MHG swébe, sf. ‘suspense’; OCS svepljo se, svepiti se, as OHG
suer- (1) *weigh down, hang'. (Long-gde: suér-). WP 1,264 Oss. cf. xársun, Iron. xássín, v. ((1) ‘carry’, fr. *suersKO); Gk. cf. a-eiro, v. ‘raise’ (fr. n-^); Alb. vjerr, aor: vora beside m-vjerr, m-vora, v. id. A “lever up; weigh; hang’; Go. (long-gde)
hurtle'.
suens- — suer-, on, -en (suor-, sur-)
10
20
25
30
35
40
45
1348
sweran, wv. ((respect', lit. ‘weigh, consider’, fr. swérs ‘honoured’, lit. weighty"); Li. sveriù, sveiti, aor: sveriau, v. ‘raise, lever up’; Latv. sveru, svert, tr. & intr. ‘weigh’. (Long-gde in) Av. xwairis, f. ‘blame’; Per. xwar, adj. “indi- gent; Go. swērs, adj. 'honoured', lit. ‘weighty’; MHG swaàr, swaere “painful, glum, heavy’; OE sw&r ‘heavy, dull, sad, sluggish, weak’; n. ‘heaviness’, etc.; Scots sweer, adj. “lazy, reluctant’; ON svárr, adj. “heavy, grave’. Cf. type *suermn- in Gk. hérma, n. ‘pivot; earring, necklace’ beside (o-gde) hórmos, m. ‘necklace’, lit. ‘pendant’; Alb. vjerré, f. "ver, sification’; beside i vjerré, adj. ‘sloping’; Li. svermuó, gs: -ens, m. “weight — on a scale’; (o-gde in) Alb. i várun, T i várur, adj. (hanging, fr. *suor-)
suer- (2) (suor-) “call, declare, state, speak, utter’. WP II 527 Skt. svaràmi, v. ‘sound; sing’; Gk. érō, éromai, v. ‘ask’; eíro, v. (2) “say, speak, tell’; cf. eirén, gs: -énos, m. “youth of speaking-age in Spar- tan parliament; MHG swéren, sv. 6. ‘swear’; OE swerian, sv. 6. id.; (o-gde in) Cz. ne- svor-ny, adj. ‘quarrelsome’; (long o-gde. in) OCS, Cz. svarü, svár, m. *quarrel' beside OCS svara, f., svarjo, -iti se, id.; ON sverja, v. ‘swear’ (p. t. sór & svór beside svaróa, pp: svarinn) (*-e-; *-0-; *-o-), (long o-gde in) MHG swuor, sm. (oath, curse: OCS svarü). Am- biguously *-e-/ *-o- in Skt. svárah, m. ‘sound, voice’. Ambiguous initial in Gk. éris, f. ‘strife’, and ambig. vocalism in Sw. sorl, n. ‘din’; sorla, v. (*syerol-?)
suer- (3) “harm, hurt, corrupt. See next Skt. svaràmi, v. (1) ‘blame’; Av. xwar-, v. “blame, injure’; xwairis, s. “abuse, blame"; Per. xware, s. ‘corruption, gangrene’; cf. xire, adj. ‘malignant’; MHG swérn, sv. “hurt; suppurate’
suer-, -on, -en (suor-, sur-) (4) 'swelling, suppuration, gangrene, ulcer. Cf. suer- (3) above. Av. xwaro, m. *wound'; Per. xware, s. 'gan- grene; leprosy?’ beside re, adj. ‘malignant’; Oss. cf. xàlmag, xwálmag, s. ‘scab, wound’; W cf. chwaren, f. (“gland”, fr. *suoren-); chwa- rel, m. (“breast tumour’, fr. *suorel-); OHG swéro, wm., MHG swér(e), s. & wm. ‘ulcer’;
1349
(Z-gde in) G Geschwür, id.
suer- (5) “post, pole, pillar, stump’. Cf. suir-. (Lat. ambig.) Skt. sváruh, m. id.; Gk. cf. hermís, gs: hermí- nos, f. id.; Lat. (ambig.) surus (“bough, stake, palisade’, fr. *suer- as in vocalism of vulva: Gk. eiláo or fr. type *guelbh-, oe: vult ^wishes', fr. *uel-, cf. (alleged) OLi. pa-velt, id.; or fr. *suir- as in vocalism of subitus, see suidh-, pudeo, fr. *po- or *pod-, and *uid-, q.V.) (for sul-phur cf. suel-, pür-, and for mulgeo cf. melg-)
suér- (1) “heavy, hanging”, etc. See suer- (1)
suér- (2) ‘tasty, piquant' in Tokh. swar, B sware, adj. (sweet, pleasant; Li. svere, f. ‘winter cress’: Latv. cf. (?) përkoni svere(s) *ground-ivy'
suerbh- (suorbh-) (1) ‘twist; thong, rope". WP II, 529 and squerbh-. (Gmc. ambig.) Arm. karb, i, iv, s. “asp, basilisk’; Tokh. A svarp, sparp, s. ‘rope’; W cf. chwerfu, v. ‘spin, roll": chwarf, pl. au f. ‘whirl; rocke
=== leaf 743 ===
t’, fr. *suorbh-; OFris. swerva, MHG swérben, sv. 3. ‘swerve’; ME swerven, id.; Du. zwerven, v. ‘roam’; Norw. sverve, v. ‘spin’
suerbh- (2) ‘wipe, smooth, lay out. (var. suorbh-). Cf. squerbh- Go. af-swairban, sv. 3. ‘wipe off; OE sweor- fan, sv. 3. ‘wipe; polish, file, scour’; ON sverfa, sv. 3. file’; cf. Swiss schwarben, v. ‘lay in swaths and E dial. swarf, s. “black grease from machinery'
suerbh- (3) 'skin, slough' Oss. xürv, s. “scale, slough, veil’; Gk. érphos (beside stérphos), gs. -eos, n. 'skin'. (OE sweorf, n. = ‘metal turnings’, cf. suerbh- Ou
suergos (suorg-) ‘sky, doud WP II, 531 Skt. svargáh, m. ‘heaven’; MHG swérc, gs: swérkes, sm. "dark doud: (o-gde in) swarc, adj. t'overcast; OS cf. swarkan, sv. 3. ‘grow dark": OE sweorc, m. 'thundercloud'; Du. zwerk, n. ‘sky, clouds’
(sueró, sueros, suér-, see suer- (1-4))
sueruos (qusueruos) ‘bitter, sour, tart". Onomat. (Variants) Per. Sür, adj. “salt-, brackish’; Olr. serb, Ir. searbh ‘bitter, sour; W chwerw, adj. ‘bitter’; Br. chwerð, id.; Cor. wherow, id. (and *harsh");
we
suer- — suesriios, io (suesrios, io)
10
20
25
30
35
40
45
1350
OHG cf. swéro, m. (fpain, sickness’, but see suer- (4); LG cf. sarw ‘tart, sour, harsh’; (variant in) OCS srüxükü, adj. *'rough'. Cf. Kauros, süros, quser-
(sués, see suls, ius, iusuis. Valid only for W. Br. chwi ‘yow’). WP I, 210
suesios “apart, alone; own, private’. Cf. suetios, suesue, seue, suelos, etc. WP II, 455. See next. (Variants in Iran.) Per. xwi$ “own; self; kinsman, son-in-law'; xwisan ‘kinsfolk’; xi3i, s. ‘kinship’; Kurd, xó$ ‘kinsman’; Oss. sáxi “they, themselves; their”; pn. (self; wäx ‘quality, nature’; xion, Dig. xewon, adj. “own, akin’; Hom. Gk. heós, adj. "own": Gk. eia, npl. (1) ‘provisions’; Umbr. swesu-, adj. own: Lat. cf. suere, inf. "ae custom’; cf. sé-par ‘unequal; Ir. seise, m. ‘comrade’; Go. swes, adj. own: n. ‘property’; OHG swas, adj. as Go. MHG swas, sm. or n. ‘closet, privy’; swàs-, cpds. ‘private’; OS cf. swēslīk, adj. own: OE sw&s, adj. ‘own, inti- mate"; Icel. svás ‘beloved’; OCz. cf. (?) svést, f. ‘mother-in-law’; Latv. svešs, adj. “foreign
(sueslos, possible variant of suelos, q.v. in Lat. solus, adj. ‘sole’. Uncertainly in Gk. hélor; helein; hélon ‘seizure; seize; seized" of booty)
suesór, suesor ‘sister’. Cf. sue- and extns., sər- and suesrios. (Z-gde in some Gmc. forms). WP II, 533 Skt. svasr & svasa, id.; Av. xwáha, acc: xwá- harom, id.; Per. xàhar, id.; Ossetic xwärä, cpds. xárá-, id.; cf. also án-suvár (“brother”, if for *som-suesr-, cf. G Ge-schwister); Tokh. A sar, B ser ‘sister’; Arm. Eur, gs: Ker, ab. sing. kerb, id.; Hes. éor, pl. éores ‘sister, daughter’; Lat. soror, gs: -oris, f. ‘sister’; Olr. siur, Ir. siür, gs: seather, id.; W chwaer, pl. chwiorydd, Br. choar, pl choarézed, Cor. whor, pl. wheryth, id.; OHG swéster, MHG id. and suster, süster, id.; Go. swistar OE sweostor, pl. -tra, -tru, Du. zuster, ON systir, pl. systr, id.; Finn. LW sisar, id.; OCS (and com. Sl.) sestra, id.; Li. sesē, gs: sesés beside sesuó, gs: seseřs. (NB. Gk. óar, gs: óaros ap- pears to represent an o-grade variant (resul- tant aspect) of the same root)
suesriios, io (suesrios, io) 'kinsman on
1351
female side’. See suesõr, and next Skt. svasriyah 'sister's son’; svasrīyā 'sister's daughter; Per. Sü, Sauhar, s. Chusband", Phonol. of šūr ‘salty’, see sueruo-); Arm. keri, -vo, -vov, s. “maternal uncle; cf. Ker- ay£ik ‘niece’; Lat. cf. sobrinus, a, adj. & s. *(of) cousin on mother's side’; OS swiri, m. ‘cousin’; OFris. swire, s. fcousinhood'; Ger- manic forms of obscure definition, cf. OE sweor, m. (2) ‘father-in-law’; cousin; G Schwáher ‘father-in-law; brother-in-law'. Cf. OCS Suri, m. (wife's brother’. Phonol. obs- cure. See next)
suesrinos 'sister's' Lat. sobrinus, a, mf. *maternal cousin'; Osc. cf. sverrunei (?) ‘to a (certain) kinsman’; OC
=== leaf 744 ===
S sestríni, Cz. sestřin, adj. ‘sisters’; R cf. Sürin, m. (*wife's brother’; fr. *sue-suesrino- ?). Cf. suesrios, above)
suesue (suosue), suésu, sus- 'so, thus, as; anyway' Kurd. xo ‘so, well: Umb. svesu ‘so, thus"; Mir feib, Ir. féibh as: Go. swa ‘so’; swaswe "as": OE swa, swaswa & swæ ‘so’; Norw. Sw. sá, Du. zoo, id. beside Du. zus, id.
suet- “alone, apart, by oneself; self; own, private, special, separate, outsider, new- comer’. Radical sue- (se-), w. extns. Skt. svatah, adj. & prn. “own; self; svata, f. ‘ownership’; Av. xwatom, n. ‘the self; xwato, adv. “of itself; Per. xü, s. ‘habit’; cf. (zero-gde) xud, prn. ‘self; Oss. xwüd-, xàd-, cpds. ‘self; xädäg, prn. id. (LW in Arm. katak, adj. 'si- milar’); Kurd. xas, adj. “special, favourite"; Arm. Kec ('separate', fr. *suets); Gk. étés, gs: étou, m. ‘kinsman; neighbour’; pl. étai *com- panions’; Elean wétas, s. “private citizen’; cf. hétaros, m. ‘comrade, attendant" and perh. het-airos ‘raised detachment’ (but cf. *iet-); here also prob. eteós, adj. “true, real’; cf. (variant) Lat. sed, cj. "but: sed-itio “going apart, sedition’; Li. svečias, adj. ‘foreign’: m. ‘guest’; Latv. svešs ‘foreign’; svets, m. ‘host, entertainer’. Cf. also Gk. etázō, v. (single out, fr. *syetajō). (Isophone: W chwed, m. ‘expression’; chwedi ‘after; then’)
(suən-, see suen-. Thus in ainos, aínē if for *suonio-, suonio, or *sun-)
suesrinos — suibh-, suibhlo
10
15
20
25
30
35
40
45
1352
suib- (sueib-, suoib-, suib-) ‘dash, whirl, swerve, sweep, jerk, whizz’. Cf. qusib-, etc. Onomat. Gk. cf. ibu, adv. ‘greatly’; Lat. subo, are & -ére, v. “be in heat’; sübulo, gs: -onis, m. ‘piper’; (for Lat. subitus see suidh-, but ambig.); Ir. síobaim, v. intr. ‘blow’; síob, f. ‘gust’ beside siubhal, m. “flight, dash’; Mir. cf. sibal, siubal, m. ‘stir; W chwyf, m. “stir” beside chwif, pl. iau, f. ‘whirl’; cf. chwyfan, f. ‘stirring, hesitancy’; MLG swippe, wm. & f. ‘whip’; Du. zweep, f. id. (secondary length, or fr. *suoib-); OE swipu, f. id.; ON svipr, m. ‘sweep, dash, flash’; svipan, f. (sweeping, swing: W chwyfan; chwyfio, inf. “dash, move"); OHG swipfen, id. beside MHG swi- fen, sv. 1. intr., id. (fr. *sueib-); ON svipa, v. id.; OE swipian, swippan, v. “flog? (secondary length in E swipe and prob. in Du. zwiepen (dialectal?) ‘swish, flog; totter, waver’). O-gde in OHG, MHG sweif, sm. ‘swinging gait; tail’; ON sveipr, m. (3) ‘stir, uproar’. Cf. also W chwi- in chwi-mwth, adj. ‘rapid’ beside mwth, adj. id. See next, and variant suibh- & suiu-, cf. also qusib-, etc.
suibəlos (qusib-) ‘dashing, passing, tran- sient, unstable’. Cf. suibros and suib- above. Variant suibh-. (Onomat.) Av. (ambig.) xáviwrom (hizvám) ‘fluency (of tongue)’; Olr. sibal, MIr. siubal, Ir. siubhal, m. “flight, dash, movement, stir’; ON svipull, adj. ‘unsteady; transient, fickle’. (An Oss. form xà- bål, adj. ‘flaccid’ represents a type *suebor- or sim. See next)
suibros ‘dashing, transient; cheating’. Va- riants: suibəlos and suebros Av. (ambig.) x&viwrom, n. ‘fluency’; Ir. (ambig. *-j- or *-e-) seabrach, adj. ‘lively’; seabhrán, m. ‘staggering gait’ beside (*-ei-) siabhair, adj. *elusive, illusory’; siabhraim, v. ‘cheat’; OHG (*-i- or *-e-) swépfar, adj. ‘sly’; OE swipor, adj. (2), id. (Type *suebros in W chwefr, adj. mf. ‘violent’; m. ‘violence’ and in Oss. xäbäl, xübal, adj. limp"). Cf. uib-, Kuib-
suibh- (suibhlo, etc.) variant of type suib-, suibolos, suibros, q. v. Av. xšviwi, adj. (swift,
```


## [2026-09-14T02:00:45.144Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s):8*4*2\\|Page(s): *84[0-9]\" POK_full.txt | head -20"
}
```


### [2026-09-14T02:00:45.197Z] TOOL RESULT

```
18214:Page(s):212 
18237:Page(s):212 
18321:Page(s):213 
19240:Page(s):217 
68622:Page(s): 840-841 
68656:Page(s): 841 
68696:Page(s): 841-842 
68740:Page(s): 842 
68758:Page(s): 842 
68772:Page(s): 843 
68908:Page(s): 842-843 
68966:Page(s): 844 
68986:Page(s): 843-844 
69012:Page(s): 845 
69038:Page(s): 845 
69057:Page(s): 845 
69079:Page(s): 846 
69104:Page(s): 845-846 
69121:Page(s): 846 
69135:Page(s): 846
```


## [2026-09-14T02:00:46.850Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68660,68775p' POK_full.txt"
}
```


### [2026-09-14T02:00:46.907Z] TOOL RESULT

```
Meaning: by, about, around, beside 

Note: probably *p+ os, Gen.-Abl. to Y^Jp-^ above S. 53 f. 

Material: Gr. in Arcadian-Cypriot and auf gr. Inschriften Phrygiens TToq, vor vowel also no-, 

geltungsgleich with rrpoc; (see *per'out - about', Nr. 8) and Doric rroTi; Lithuanian pas 

preposition "an, by'; probably also Old Church Slavic yoo in the meaning " behind, after'; 

compare das erhaltene 5- in Old Church Slavic poz-dbA6']. "late', poz-de Mn. "late', 

pozderije {paz-derije) "KaAapin, arunsTov'. To Lithuanian pas a\so pastaras'\he letzte, 

hinterste'. 



derivatives: 1. witli -//probably Armenian as/'after', Adverbal and preposition "after = 
secundum, gemaft'; in addition stor'the untere part'?; Latin post, Old Latin poste'aiter, 
behind ', ortlich and zeitlich, Adverbal and preposition m. Akk., Oscan pust, post, Umbrian 
post, pus'post' ortlich and zeitlich, preposition m. Abl., therefrom Latin posterns, Oscan 
pustrer\x\ postero', Umbrian postra, Latin postumus, Oscan pustmafsj 'postremae'; 
Umbrian postne, Latin poneirom *posti-ne, Oscan pustin, Umbrian pustin {irom *posti en) 
"je after' preposition m. Akk.; Umbrian pust-na/af' post\cas', purnaes ^post\c\s'; Latin 
/7c»s//c^s"hinten situated'. 

2. -ko-0\6 Indie /75sca(lnstr.) Adv. "behind, westlich, later' = Avestan pasca preposition 
" behind, after', ortlich and zeitlich. Old Indie pasca/ (Abl.) preposition " behind, after, 
westlich', Avestan paskatAdv. "vonhinten her, hinterdrein' spacial and zeitlich; Lithuanian 
paskul pasku/ (Dat) Adv. "afterwards, nachher', preposition "after'. 

3. In ending still controversial is ap. pasa ^aiter', preposition ortlich and zeitlich; alb. pas, 
Geg /77i6'as preposition " behind, after' (Indo Germanic *pos+ Demonstr. s/). 

References: WP. II 78 f., WH. II 347 ff., Trautmann 207, Schwyzer Gr. Gr. 2, 508. 
Page(s): 841-842 

Root / lemma: pot/s 

Meaning: owner, host, master, husband 

Material: Old \nd'\c pat/-, Avestan pa///- "master, mister, lord, master, consort, partner'; Old 

Indie /Oa//7/"" mistress, wife', Avestan paz?/?/- 'mistress'; Old \nd\c patyate^\r\errsc\nt, is 

teilhaftig' (: Latin potior); 

Avestan x'ae-pati- "er selbst'; 

gr. hogk; ' husband ', nowia "mistress (of Hauses), wife'; 5£a-noiva 'mistress of 
Hauses' (*5£a-novia, from *5£a-noTvia), 5£a-n6Tr|<;, -ou "master, mister of Hauses' (see 
above S. 198); alb. pata^had', y05s/7e"gehabt' {*pot-to-) (to a present as Latin potior. Old 
Indie yoa/ya/e); 

Latin potis {potior, potissimus) "wealthy, mighty', possum. Old Latin also potis sum 
"kann', potui, potensirom an e-denominative as Oscan putiad ^possW, putians 'poss\nt', 
Latin potestas^ power', potior, -TrT{potrtur and potTtui) "sich bemaehtigen'; com-pos 
"teilhaftig' (*"Mitherr'), tiospes, -itis' guest's friend ', pael. iiospus {*gtiosti-pots^ Qasihexx'); 
ein unflektiertes *poti 'selbst' placed in utpote^as natijrlich, da namlich, namely', actually 



*ut *pote{esf) "as es possible is = naturiicli', furtlierwitli syncope in m/hr-, meo-, suapte 
etc.; 

Gotliic bru^-fa^s^ bridegroom ', /7£//70'a-/&A'5"Befelilsliaber about 100 Mann'; engl. fad 
"strong, valiant, big, large'; 

Lithuanian pa/s "husband' and "selbsf (old patis), Latvian pats^ householder ' and 
"selbsf, Lithuanian K/espa/s "master, mister' (old viespatis). Old Prussian pattiniskun f\Vk. f. 
" matrimony '; f. Old Lithuanian viespatnr, *patn/'under influence of *yOa//- transfigured to 
*patr\n Old Prussian waispattin f\Vk. "wife, woman', Lithuanian pat/^\N\ie', Latvian pat/ 
"Wirtin'; indekl. particle Lithuanian pat, Latvian yC>a/"selbst, even, straight'; about Old 
Church Slavic gospodb "master, mister', see above S. 453; 

Hittite -yC»s/"eben(so), also, rather'; Tocharian A pa/s "husband'. 

References: WP. II 77 f., WH. I 660 f., II 350 f., 379 f., Trautmann 208, Benveniste 
Origines 1, 63 f., Pedersen Hittite 77 f., Endzelin Latvian Gr. 396 f. 
Page(s): 842 

Root / lemma: po-ti 

Meaning: against 

Note: through das Adv.-forms -//(compare *proti- : *pro above S. 815 f.) from *po (see 

below *apo' ab') extended 

Material: Avestan pa/'t/, ap. /05//y proverb, and preposition "against, entgegen, to, auf, by'; 

"an; for, um'; "from - from'; "in - toward, in'; hom., Boeotian, lak. etc. nori "np6(;' proverb. 

and preposition "against - toward, against, compared with; an, to', "in - toward, from-'. 

References: WP. II 77, Schwyzer Gr. Gr. 2, 508 f. 

Page(s): 842 

Root / lemma: pougo- or pougho- 

Meaning: clear, sound 

Note: only Celtic and Slavic 

Material: Old Irish o^"jungfraulich', oge"Jungfraulichkeit'; Czech pouhy^ pure, bare, 

simple, just'. 

References: WP. II 77. 

Page(s): 843 

Root / lemma: p6(i)-1 : (pa/-?:) pT-
```


## [2026-09-14T02:00:55.264Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -5; grep -c \"\\[pdf page\" BQT_v2_pages.txt"
}
```


### [2026-09-14T02:00:55.369Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
0
```


## [2026-09-14T02:00:57.752Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nprint(len(t))\npages=t.split('\\f')\nprint('pages',len(pages))\n# find page numbers\nfor i,p in enumerate(pages[:6]):\n    print('---',i,repr(p[:120]))\n\""
}
```


### [2026-09-14T02:00:58.845Z] TOOL RESULT

```
2900526
pages 684
--- 0 ''
--- 1 '                                         \u202b\u202a7\u202c\u202c\n\n                          \u202bرن\u202a۳\u202c\u202c\n    \u202bنات\u202c\n      \u202bا م\u202c\n              \u202bل'
--- 2 '                   \u202bم\u202c \u202bو\u202c\n\u202bنآکو سخنیم بیاموزد مرا\u202c\n                       \u202bد\u202c \u202bد\u202c \u202bل\u202c \u202bج\u202c \u202bم\u202c \u202bة\u202c \u202bچ\u202c \u202bا\u202c \u202bی\u202c \u202bد\u202c\n\u202bعلى '
--- 3 '                                                     \u202b\u202aar\u202c\u202c\n                                     \u202bمااضحاذفی\u202a\u200e\u202c\u202c\n \u202bاست\u202a\u200e\u202c'
--- 4 '   \u202bو\u202c              \u202bفك اا \u202a .\u202cبخش\u200cاول (منطق)\u202c                           \u202b\u202a ۰\u202cای\u202c\n\n \u202bحصحح سیدمحمد\u202c        \u202b\u202a 8\u202cمصحح محمد'
--- 5 '\u202b\u202a . ۱\u202cفيه ما فيه \u202a .\u202cمولوی بلخی رومی \u202a ۰\u202cمسحح بدیم الزمان\u200cفروزانفر\u202a .\u202cاز\u202c\n                                             '
```


## [2026-09-14T02:01:03.913Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nimport re\nfor w in ['خدیو','خدای','خویش','خواهر']:\n    idx=[i for i,p in enumerate(pages) if w in p]\n    print(w, idx[:20])\n\""
}
```


### [2026-09-14T02:01:04.941Z] TOOL RESULT

```
خدیو [178]
خدای [76, 163, 176, 177, 178, 204, 268, 269, 270, 281, 304, 391, 433, 458, 463, 479, 480, 582, 602, 648]
خویش [47, 82, 128, 163, 238, 243, 252, 258, 259, 319, 329, 369, 386, 451, 459, 504, 586, 589, 597, 605]
خواهر [124, 153, 157, 242, 257, 260, 277, 352, 376, 444, 534, 536, 625, 656, 659]
```


## [2026-09-14T02:01:07.395Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (176,177,178,179):\n    print('==== leaf',i,'====')\n    print(pages[i][:2500])\n\""
}
```


### [2026-09-14T02:01:08.412Z] TOOL RESULT

```
==== leaf 176 ====
 ‫ضا‬
  ‫با سوختن و راه رفتن در دست وایعاو‬                            ‫خجنك = نماول وفتح ثانی سوکون‬
                                                              ‫نون ودال ابجد ‪ 0‬نام قصبه‌ایت درماوراءالنهر که‬
                                         ‫‪.‬‬   ‫بهم رسد‬
                                                          ‫‪۲‬‬                              ‫مولد کمال است ‪٩‬‏ ‪:‬‬
‫اول و انی بتحتانی‬
  ‫»|‬    ‫=‬    ‫‪۷۳1‬‬
                            ‫حجیر "‪۰‬یکر‬
                                  ‫‪۴‬‬          ‫‪2‬‬


                                                               ‫_ بن اول و ثالی» در نذه است‬        ‫خجی؟‬

                                                              ‫گویند‪.‬‬   ‫که لآرا چکاو کے خوانند و بعربی قبره‬
‫وجمیل وخوش صورت وصاحب حسن راگویند ؛‬
                          ‫ویضم اول هم آمده است ‪1‬‬              ‫خجو له بکر اول و فتح ثانی و لام‬
                                                              ‫وسکون واو »آبله گروانندکه ببب کارکردن‬


                                                   ‫بیان ششم‬
            ‫درخای نقطه دار ‪ ۳‬دال بی نقطه مشممل بر شانزده لغت و کنات‬

 ‫‪-‬دوای؟ جم اول ‪ ۰‬نام ذات | وصاحب ومالك را نگیوزبند ؛ وبا ذال نقطه‌دار‬
                                                                    ‫خداً خ‬
                                      ‫بارتمالی است همچو الهواله ‪ -‬و مخقف خود؟" | هم خوانده‌اند ‪.‬‬
                                                                                              ‫‪1‬‬




                                                   ‫(‪ )۷‬چك‪ .‬چش‪ :‬جوئی‪.‬‬               ‫(‪ )۱‬خم‪ -: ۱‬و‪.‬‬
  ‫روزه راه‬         ‫ده‬   ‫‪ ۰‬من آن و ‪-‬مرقند‬         ‫‪ - ۱‬شهری مشپور بماوراء النهر بر ساحل سبحون‬
  ‫در ‪ ۱4‬درجه و ‪ ۳۲‬دققهة‬               ‫ت‬
                                      ‫س)‬‫اوس‬
                                          ‫است « ممجم‌البلدان ‪ :‬خجندة » و اکنون در ترکستان (ر‬
      ‫‪ - ۴‬ظ‪ .‬مصحف«چفو»‬          ‫عرض شمالی و ‪۸٩‬‏ درجه و‪ ۲4‬دققة طول‌شرفیه ضمیمهةٌ معجم البلدان»‪.‬‬
  ‫بهلوی ‪rhic‬‏ ‪( uh -‬از ‪ :‬هو (خوب ) ‪٣‬‏ چهر(اصل نژاد ) ‪.‬‬                            ‫هرژ=ر‬
                                                                                      ‫هج‬          ‫(«‪.‬م ) ‪= ۴‬‬
   ‫اوستا_‪-»3601)1‬ل‪0‬ا«بارتولمه ‪۱۲۸۱٩‬‏ نبیر گے ‪»۹۰۱‬طبری ‪( ۲1[06‬خوش» خوب‪ .‬زیدا) «واژه‌نامه‬
  ‫‪ .‬دامفالی نیز ×‪٣[0‬‏ ‪ ,‬شهمیرزادی ‪7[1205‬؛ لفة نيك نژاد ‪ .‬خوب اصل و مجازاً بمعانی‬                            ‫‪۳‬‬
  ‫‪ ۴‬ب۔هلوی متأخر ‪: . ۷2۸۵۷۲‬هلوی
==== leaf 177 ====
 ‫خدرگه‬                                                                                                     ‫‪a Ah‬‬


‫اول‌بروزن مهره » خرده‬         ‫حدره =‬                         ‫زراق که بظاهر خود را بیارایند‪ -‬وآلهایی‌را فیز‬
‫رىز هرچیز را گویند رک وشرارة آتش‌را لز‬‫و‬                      ‫‌دشدادو لمرود؛‬      ‫عابنییکر‬‫یخد‬
                                                                                           ‫دی‌‬
                                                                                             ‫نوا‬
                                                                                               ‫گونن که دع‬
          ‫گفته‌اند ؛ وبفتح اول همآمده اش‬                         ‫وآنها راخدای فروشان هم میگوبند با دوتحتانی‬
‫خدك ‪ .‬بفتح اووئانی بروزن کجك‪.‬‬                                                                                    ‫ورف‬
‫مطلق پل را گوبند خواه باسنگف وخشت وکچ‬                        ‫تون‬     ‫حجد او ند ‪ ۱‬ب‌ بقتح واو وسکون‬

 ‫بر رودخانه بندند و خواه با چوب وخاکد‬                                 ‫‪۰‬‬   ‫را کوند‬    ‫انه‬    ‫ویز رگ‬        ‫صاحب‬   ‫‪1‬‬   ‫ودال‬

                                 ‫بر جوی (‪# . )۱‬‬
                                                             ‫مزر گد‬        ‫بادشاه‬       ‫‪ ۴‬س‬     ‫حدایگان‬
‫سمعنی‬
    ‫بر وزن عشرنی ‪۰‬‬           ‫‪°‬‬
                                                                                            ‫وخداوند گار اعظم باشد‪.‬‬

‫بروزن بپلنگه‪ ,‬نام درختی‬      ‫‪-‬‬        ‫‪۱‬‬
                                                                 ‫حدر نق » بفتح‌اول وئانی‌بروزن‌خورنق‬
‫است بیارسخت که از چوب آن‌نیزه وتبروژین‬                       ‫بلغت رومی و بعضی گوبند بونانی عنکبوت را‬
                                                            ‫گوبند ‪ ۴‬؛ وباین‌معنی بجای نون بای حطی حم‬
                                          ‫میکویند ‪. ۷‬‬                                                ‫بنظر آ مده اف‬

                                                                               ‫(‪)۱‬چك» چش‪ :‬جوئی‪.‬‬
                            ‫وند (یوند اصاف) بمعنی صاحب (مطلقا) ‪:‬‬                    ‫‪+‬‬       ‫ا‬‫د‪:‬‬
                                                                                              ‫از‬‫‪ ۱‬خ‬
  ‫‪۶‬لتان ‪. ۸۳‬‬
           ‫گ‬                        ‫درتهند‬      ‫ر‬   ‫دست‬   ‫کنان‬    ‫لماش‬         ‫جاه‬          ‫ویشند‬
                                                                                                ‫
==== leaf 178 ====
     ‫‪۵‬ف‬

 ‫‪۴‬‬      ‫باشد‬    ‫بزرگه و خداوند خانه‬        ‫و کدخدای‬       ‫بضم اول و الی و سکون‬       ‫خدو ‪- ۲‬‬
‫کودبانوی خاله را نکبفزته‌اند (‪)۱‬؛ وبفتح اول‬                ‫وأو » آب دهن راگونند که از آثر مزةٌ چیزی‬
                                                                                            ‫‏‪Ey‬‬
                                                          ‫ْم اول بروزن سلو کك»‬     ‫کّ خدو ك و‬
‫جدیو * ‪ -‬بکر اول و الیوسکون‬
 ‫تحتالی مجهول و واو پادشاه ‪ -‬و وزیر س‬                     ‫پراکنده و پریشان شدن طبیمت باشد از امور‬
                                                          ‫‪ -‬وفهروخشم‪-‬‬     ‫ناملام ‪ _۴‬ویمعنی رشك وحد‬
 ‫ونگانةً عصر باشد ِ‬     ‫وخداوند کار ‪ -‬و بزرگه ‪-‬‬
                                                          ‫وخجلت وشرماری نیز آهده است ‪ -‬و بمعنی‬
                                                                          ‫آزردگی وعصهٌ بیجاخوردن ه‬
‫اول وثالی وفتح رابع‬     ‫»‪ -‬بكر‬   ‫حد بور‬
                                                          ‫؛ وبفتح‌اول‬   ‫همت‬
‫یمعتی خدیو است که‬          ‫و سکون رای فرشت ‪۰‬‬                                              ‫نیز گفته‌اند ‪۲‬‬
 ‫پادشاه ‪ -‬ووزیر ‪ -‬و خداوند کار ‪ -‬وبزرگه ‪-‬‬                  ‫حد بر ه بفتح اول بروزن وزیر» بمعنی‬
                            ‫وبگانةً عصر باشد ‪٩‬‏ ‪۰‬‬
                                                           ‫حن امت که خوب ‪ -‬وخوبی ‪ -‬و خوشدلی ‪-‬‬
‫وتح‬
  ‫حد به = بکراول وسکون تانی ف‬                                                         ‫وخوش خلقی باشد‬
‫تحتالی ‪ ۰‬بمعنی مضاف است که در مقابل مطلق‬                   ‫خد یش ‪ -‬بضم‌اول کوسرثانی وسکون‬
                                               ‫باشد ‪. ۷‬‬    ‫تستالی مجمول و شین قرشت ‪ ۰‬بمعنی پادشاه‬



                                                                            ‫(‪ )۱‬چش ‪:‬گوند‪.‬‬

      ‫‪ = ١‬خو (ه‪.‬م‪« ).‬اسفاا‪ ۲ :‬ص ‪ = 64‬خذوك (بفتح اول ونيز طم آن ) ر‬
  ‫(ك‪: ‎‬‬
                          ‫ع‪ .1‬مانوی‪012۷۷ ‎‬‬
                                         ‫‪4 K1‬‬
                                            ‫لفت فرس اسدی ص‪ " ۹٥۲) ‎‬درسغدی‪W ‎‬‬
          ‫)‪(Henning, sogdian loan words , BSOS. X. 1 . 94.‬‬
   ‫؟‪ ‎‬درقرای اطراف فزو‪.‬ن ‪ ( 1002‬اضطراب وغم وحزن ) ( ازافادات‌علامه دهخدا)‪‎.‬‬
                                               ‫رکنف جوم‪‎‬‬
                                                       ‫خن ن‬
                                                          ‫‪ ۴‬اف سیف سد رات‬
                ‫ز آنکه خد
==== leaf 179 ====
                                       ‫بیان هفتم‬

    ‫خای نقطه دار با رای بینقطه مشتمل بر یکصد و شصت و پنج‬                             ‫در‬

                                    ‫لفت و کنات )‪(۱‬‬



‫وخر ک طنبور وعود وقيجك و امثال آنرا لیز‬        ‫بفتح اول وسکون ثانی ‪ ۰‬معروف‬     ‫خر =‬

 ‫گوبند ‪ ,‬وآن چوبکی باشد کهدر زیر تهارای‬                                   ‫است وبعربی حمار‬
‫سازهای مذ کور گذارند ‪ -‬وہر چىز را نیز گوبیند‬                              ‫اعلی گونند ‪- ۷‬‬
‫بز رگی‬   ‫تاهمواری د‬   ‫که در بای و زشتی و‬                                    ‫اگر کسی را‬
‫و اتراشید کی بنهایت رسیده باشد همچو خرای‬                                  ‫عفرب گزیده باشد‬
‫و خرامرود و خربط و خرپشته و خرپیواز (‪)۳‬‬                                   ‫بابد که بآواز‬
 ‫خاه‬
   ‫رگ‬‫وخرتوت وخرچالوخرچنکه وخرسنکه و‬                       ‫خر‬               ‫بلند بگوش خر‬
 ‫ورموش‬  ‫ورمگس خ‬  ‫و خرکمان و خرکوف خ‬             ‫بگوید که مرا عقرب کزبده است وواژگونه برو‬
‫وخرمپره وخر ای وامثالآن ‪ -‬ویضم اول] فتاب‬        ‫سوار شود درد زابل گردد وهمان جای خر بدرد‬
                                                ‫اهنت‬   ‫را گزنده‬   ‫اتک‬     ‫عقرب‬   ‫که‬       ‫آبد‬
‫عالمتاب است‪ -‬ویکسراول بزبان بپلوی ‪ ۰‬بمعنی‬
                     ‫خوشی وخوشحالی باشد ‪.‬‬
                                               ‫ند که‬
                                                   ‫دکی‬
                                                     ‫بکنود‬
                                                         ‫وار پوست پیشالی خر را بر‬
                                               ‫میترسد دیگر شرسد ‪ .‬وماصگرروع باخود‬
 ‫خراب ‪ = ۴‬بر وزن شراب » معروف‬                  ‫نگاهدارد شفابابد ‪ -‬وکنابه از شخص بی عقل‬
 ‫است که لقیضآباد باشد یمنی وبران ‪ -‬وهرچیز‬      ‫واحمق هم هت ‪ -‬ولای شراب )‪ (+‬وگل تبره‬
 ‫وابه‬
    ‫ضایم گردیده ونابود شدمرا یز گونند ‪ -‬ک‬       ‫وچبنده را نیز گوبند که در ته حوضها وجوبپا‬
                       ‫ازست لاسقل هم هست‪.‬‬        ‫میباشد" وباین معنی‌باتشدیدثانی هم گفهاند ‪۴‬‬


                       ‫(‪ )0۷‬چش ‪ :‬شراب را ‪.‬‬                     ‫(‪ )۱‬چك ‪ :‬کنانه ‪.‬‬

                                                       ‫(‪ )۳‬چك ‪ .‬چش ‪ :‬خربیواز ‪.‬‬
   ‫کردی‬
      ‫‪-‬پلوی ‪ » 725‬اوستا ‪ » 8721-‬ساس کرت ‪"« 2372016-‬اسفا! ‪ ۲:‬ص ‪٦٦‬‏ »‬
                                                                  ‫‪ ۱‬پ‬
   ‫‪ « ۲‬اسفا ‪ ۲ : ۱‬ص ‪ ۱۹۲‬سنگلیجی ‪ ×۲3‬بودغا ‪ « 01070‬اسفا ‪ ۲ : ۱‬ص‪ :* ۷۰۳‬زباکی‬
   ‫‪ » ۲‬وخ ‪ 70‬و‪۲‬لا‪ » 5‬منجی ‪ « 37181‬کربرسن
```


## [2026-09-14T02:01:15.329Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T02:01:16.498Z] TOOL RESULT

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


## [2026-09-14T02:01:27.282Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint('=== leaf 178 full (p.718) ===')\nprint(pages[178])\n\" | tail -40"
}
```


### [2026-09-14T02:01:28.520Z] TOOL RESULT

```
                            ‫وبگانةً عصر باشد ‪٩‬‏ ‪۰‬‬
                                                           ‫حن امت که خوب ‪ -‬وخوبی ‪ -‬و خوشدلی ‪-‬‬
‫وتح‬
  ‫حد به = بکراول وسکون تانی ف‬                                                         ‫وخوش خلقی باشد‬
‫تحتالی ‪ ۰‬بمعنی مضاف است که در مقابل مطلق‬                   ‫خد یش ‪ -‬بضم‌اول کوسرثانی وسکون‬
                                               ‫باشد ‪. ۷‬‬    ‫تستالی مجمول و شین قرشت ‪ ۰‬بمعنی پادشاه‬



                                                                            ‫(‪ )۱‬چش ‪:‬گوند‪.‬‬

      ‫‪ = ١‬خو (ه‪.‬م‪« ).‬اسفاا‪ ۲ :‬ص ‪ = 64‬خذوك (بفتح اول ونيز طم آن ) ر‬
  ‫(ك‪: ‎‬‬
                          ‫ع‪ .1‬مانوی‪012۷۷ ‎‬‬
                                         ‫‪4 K1‬‬
                                            ‫لفت فرس اسدی ص‪ " ۹٥۲) ‎‬درسغدی‪W ‎‬‬
          ‫)‪(Henning, sogdian loan words , BSOS. X. 1 . 94.‬‬
   ‫؟‪ ‎‬درقرای اطراف فزو‪.‬ن ‪ ( 1002‬اضطراب وغم وحزن ) ( ازافادات‌علامه دهخدا)‪‎.‬‬
                                               ‫رکنف جوم‪‎‬‬
                                                       ‫خن ن‬
                                                          ‫‪ ۴‬اف سیف سد رات‬
                ‫ز آنکه خدوك مشود خون مرا ازین مگس‪. ‎‬‬
   ‫مولوی بلخی‌رومی‪.‬‬
                                                                 ‫‪ ۴‬ظ » از ت خدا («‪.‬م‪: ).‬‬
               ‫مکن بد بکس کر نخواهی بخوش‪.‬‬                        ‫نک گفت مزدور باآن خدیش‬
   ‫‪.4‬‬          ‫رود کی سەر قندی‪« .‬لفبت فری‬

   ‫® ‪ -‬خدیو از ‪ .۵ ۷6/۵۳‬از ‪ ( 2۷۳212070-‬ق ‪« ) 121۵۷‬یبرك ‪ ۷۵۲‬درمادء‬
   ‫‪ 2‬رك ‪ :‬خدا ‪« .‬خدیو» خداوند بود ‪ .‬گویندکشور خدیو و گهان خدیو ‪ .‬فردوسی‬                             ‫‪0۱‬‬
                                                                                     ‫)وید ‪:‬‬
                                                                                          ‫(وسی گ‬
                                                                                               ‫ط‬
               ‫وماند الجمن بى خدیو‪.‬‬       ‫مت‬    ‫سه‬
                                                                  ‫سيامك بدست خود و رای دیو‬
     ‫«لفت فری‪۱۶ ۲‬؟‪.‬‬

   ‫معرب آن « خدبوی » بضم اول و فتح دوم بمعنی مالك و امیر وآقا و درترکی بمعذی‬
                            ‫خدیو ‪.‬‬    ‫‪:‬‬   ‫رك‬    ‫_‬    ‫‪۱‬‬      ‫رزیر آمده «نفن» ورك ‪ :‬دائرةالمعارف احلام ‪.‬‬
                                                          ‫‪ ۷‬از دساتیر «فرهنك دساتیر‪. ۳8۲‬‬
```


## [2026-09-14T02:01:40.400Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i in (238,239,240):\n    print('==== leaf',i,'(p.',i+540,') ====')\n    print(pages[i])\n\""
}
```


### [2026-09-14T02:01:41.597Z] TOOL RESULT

```
==== leaf 238 (p. 778 ) ====
   ‫کوپ‬                                                                             ‫خواجة اختران‬
‫خلیفة خواجه مودود وخواجه محمد ریکه‌روان‬            ‫اخة آن » کناب از تاره‬           ‫اوجه‬
                                                                                      ‫ح‬
‫خلیفة خواجه خان‌سعید درآن موضم باهم‌صحیت‬                      ‫عتری ماش ۔ وآفتاب را نیز گونند ‪۱‬‬
                                   ‫داشته اند ‪.‬‬
                                                   ‫خواجه بار ۔ با باابیمد بروزن‬
‫خواحة فلك ‪ -‬کنابه ازآتاب ‪-‬‬
                                                    ‫آشدنکرها بعربی‬
                                                                 ‫لاله زار؛ طعام بقدر حاجت با‬
                         ‫وستارة مشتری باشف ‪.‬‬

‫خواخة ماح ‪ -‬اشارءبحضرترساك‬
‫صلوات‌افعلیه است ‪ .‬مجسهاح بمعنی کثیر الخیر‬              ‫خواجه اش ؟ ‪ -‬باناوئین‌فرشت‬
                                                    ‫‪-‬‬     ‫ند؟‬
                                                            ‫یرا‬
                                                              ‫وقا‬
                                                                ‫کكآ‬
                                                                  ‫ران ب‬
                                                                      ‫علامان بصكاحب وكنو‬
                                    ‫باشد ‪. ۴‬‬
                                                         ‫وسصی خداو ند وصاحب خانه هم امه اس‬
‫خو ار = با انی ممدوله بورزن چار ‪,‬‬
‫در آخر کلمات گفته‬        ‫ب‬
                         ‫کنیتر‬
                             ‫بابنمعنی بدو‬          ‫خواچه چرخ اردق‪ -‬کناب از‬
‫امیشورهمچو شرابخوارو کباب خوار ‪ ۴‬وامثال‬
‫نلیل وبی اعتباررا لگیوزبند © ‪ -‬وبمعنی‬
                                    ‫آذ‬‫و‬                 ‫خواچه سه یاران۔ نام رسکیاهی‬
‫یض کج ناش شین ‪.‬واسان‬     ‫نتقکه‬
                             ‫راست ام‬                    ‫است در دامن کوه‌کابل ‪ ۲‬ووحه تماش انت‬
‫رکافتیهز‌اند ‪ - ۱‬و بمعنی اند و قلیل هم‬                  ‫که خواجه مودودچشتی و خواجه خان سعید‬

  ‫« دزی ج ‪ ۱‬ص ‪٩۰ ۶۱4‬‏‬          ‫داش‬
                                 ‫وشش “‬
                                     ‫خجدا‬
                                        ‫‪ = _ ۴‬خو‬                       ‫‪ - ۱‬رك ‪ :‬خوا ‪.‬‬
              ‫سلطانيم‬     ‫بنندده بارگاه‬                    ‫‪ - ۴‬من وتو هردو خواجه تاشالیم‬
   ‫«لتان ‪.۰۹‬‬
           ‫ک‬
                                          ‫‪ - ۴‬ویسی گوبند بمناسبت پیمودن آسمانها ‪:‬‬
            ‫آت شیرءاینت مبشرنلام ‪.‬‬                           ‫خواجة مساح ومسیحش غلام‬
    ‫نظامی گنجوی‪ 2 .‬گنجنه >‬

  ‫® _ یهلوی ‪( ۲۷3‬بيهودە‪ .‬تاچیز)‬                  ‫خوار (خوارنده) از مصدر خواردن ‪.‬‬      ‫‪۴‬‬
                                                                               ‫‪:‬‬     ‫‪ ۰‬او بوال ‪۵‬‬

        ‫که بنده درنظر خویش خوار میدارد ؛‬                  ‫چه جرم دید خداوند سابق الاسم‬
   ‫«کلتان ‪.۰4‬‬
  ‫هلوی ‪. 52۷5‬‬           ‫‪ - ۱‬اوستا ‪ ( 2۳01۵۷2‬رفاه‪ ,‬آسایش ) هخرده اوستا ‪ ۲۹۱‬ح ‪۱‬‬
   ‫کردی ‪ . 725‬اففانی ‪ ۰ ۲2۷1‬بلوچی ‪« 72۷‬اسنق ‪.٩٤۹٩‬طیر‏ ی‪( ×4 ۲‬خوب) «صاب‌طبری‪.*۱۱۳‬‬

                                                                                ‫بقه ازصفحهٌ ‪۹۷۷‬‬
  ‫‪ #‬خواب ‪-‬بروزن تاب ‪ .‬پهلوی ‪ 08۷1‬درنیکبه ‪» ۵۳۱2‬سانسکربت ‪ › 8۳۷5‬اوستا‬
  ‫‪: 2062‬س ‪٩۵‬‏ ‪ ۵۷ ۰ ۸۹,‬و ‪ ۸۹۲‬کردی ‪ , 81۷6۲ ۰ 0۷61‬اففانی ع ‪۰ ۵۲‬‬
   ‫بلوچی ‪« ۵۷‬استق‪ .»۵۹4‬گیلکی ‪ 0۵5۰‬فریزتدی ‪ ۷۷21‬برنی ‪W۷4‬‏ نطنزی ‪« 7101‬که‪۱ .‬ص‬
   ‫‪ , ۹‬سمنالی ‪ . 02113‬سنگری ‪» ۷05‬سرخه‌یی ‪ , ۷۷0‬لاسکردی ‪ ۰ ۷5۷‬شپم‌رزادی ‪05‬‬
   ‫د کت ‪۲ .‬ص ‪ ۷۸۱‬طبری ‪« 05‬صاب طبری ‪ ۰ ۲۲۳۰‬درارا که ولرستان نیز ‪ ( ۷01‬مکی‌تژاد)؛‬
  ‫حالتی که برائر ازکار باز ماندن حوای ظاهر درانان وحیوان یدید آمد و اعنای تن را راحت و‬
                                 ‫‪.‬ر زجامه مانند مخمل‪.‬‬
                                                    ‫آسایش بشند؛ لوم ‪ ۰‬ضد‪ :‬بیداری ‪ .‬غفلت پ‬

==== leaf 239 (p. 779 ) ====
 ‫خوازه‬                                                                                                                     ‫‪۷‬‬           ‫‪-‬‬


‫بمعنی خوردنی ورزق وروزی باشد ‪ -‬و جضم اول‬                    ‫‪ -‬ونام ولاسی‌است درحوالی ری‪٩‬‏ ‪ -‬وعم‬                                        ‫هت‬
‫بروژن شماره » بمعتی دستورباشد که رسم وقاعده‬                 ‫اول و ثانی بالف کشیده بر وزن شمار " بمعنی‬
‫وقانون است ‪ -‬و طعامی را نیز کوبند که مقوی‬                         ‫باشد "‪ ۳‬وبعربی | واز کاو را خوانند ‪۰‬‬                              ‫خوردنی‬


 ‫بدن شود ق‪-‬اولبی بائد کهبنایان طاق کونبد‬                    ‫خو ار بار » بائانی معدوله وبای ابجد‬
‫بربالای آن سازند‪٩‬‏ ‪ -‬و بمعنی چوب بندی هم‬                    ‫است که قوت‬                 ‫کارزار» یمعی خوراك ادك‬                        ‫روزن‬
                                       ‫‪9‬‬       ‫فەا‬           ‫باشد ‪ - ۲‬و مره ولذت را نز گوند ‪-‬‬                                       ‫لانموت‬
‫خواری خوار » بائانی معدوله بر‬                               ‫ازديك‬           ‫وخطه‌ای‬           ‫و تومئی است از توه‌نات ضارا‬

     ‫وزن ماهی خوار » دشنام شنونده کروابند ‪.‬‬                                                                                         ‫ری ‪. ۴‬‬
 ‫خواری گردن ‏ کنابه از دشنام‬                                 ‫جو ار رم » نام‌شهر ست‌معروف ومشپور‬

                 ‫دادن ‪ -‬وزبان‌کاری کردن باشد ‪.‬‬                                                            ‫ازتر کتان ‪۶. ۴‬‬

 ‫بفتح اول بر وزن بماز »‬          ‫خوار ‪-‬‬
 ‫چوبدستی که خر کواو وسایر ستوران را بدان‬                          ‫کارزار ‪ ۰‬ستمکار وخواری کننده راکوبند ® ‪.‬‬
                                               ‫رانند ‪5‬‬
                                                             ‫جو ار کاره = با انی معدوله بر وزن‬
 ‫بائالی ممدو له بروزن عازه »‬    ‫حور از و ‌‬                                       ‫‪۰‬‬    ‫گویند ‪۹‬‬   ‫را‬    ‫دهنده‬   ‫دشنام‬             ‫‪4‬‬    ‫چارباره‬



 ‫بمفعنریی|ن ‪ -‬وخواهش باشد‪-۱٩‬‏ ومطلق چوب‬                      ‫خوار کادی ‪ -‬بانانی مسوله بروزن‬
 ‫پندیرا دکیوزیند اعم اآزنکه بجهت آبین بندی‬                  ‫دشنام‬       ‫و‬    ‫‪-‬‬       ‫باشد ‪۷‬‬   ‫دشنام دهی‬       ‫‪ ۰‬نمعتی‬               ‫وارداری‬

 ‫بابنایی ونقاشی کردن عمارت یابجهت تاك انگور‬                                                       ‫‪۱‬‬   ‫را نز گوند ‪۸‬‬                    ‫دهنده‬
 ‫وامثال آن بندند کوشکی وقبه‌ای را گنفزتهاند‬
 ‫که بجهت عروسی وآبین بندی ازکل ورباحین‬                       ‫خوا ده = بانانی ممدوله بروزن چاره»‬

   ‫‪ .‬معرب آن‬      ‫‪۳۸‬‬    ‫و حدود المالم ص‬         ‫‪۵۵۳‬‬   ‫کیپان ص‬      ‫‪.‬‬     ‫رك ‪ :‬حفرافیای سیاسی‬                   ‫‪-‬‬           ‫‪۱‬‬

    ‫البارها پر کرد ‪...‬‬    ‫چون بوسف‬     ‫«‬   ‫_‬    ‫‪۳‬‬          ‫«خوار» سم اول وفتح دوم ‪ :‬رلك‪ :‬معدم البلدان ‪۰‬‬


 ‫بوسف و زلیتا ‪ .‬خڅ‬
                 ‫خابنربار های مصر بجهان بیفتاد ‪ .‬خلق روی بمصر نهادند بطلب خواربار ‪.«٩‬‏‬
   ‫"‪ 7‬همان خوار (ھ‪.‬م‪ (.‬است ‪.‬‬       ‫‪۴‬‬                       ‫ص‪ ۹۳‬‏‪ - ٩‬آمروز یزاین کاحه معنتی ارراق بکار رود‪.‬‬

               ‫مقلده‪.‬‬   ‫رکف‪:‬ص؛ ست‌ و دو‬         ‫حدودالمالم رمعم السلدان و‬                 ‫‪ 5 ۳۴‬رکف ‪ :‬فہرست‬


         ‫زشت است خوارکاری»خوبت بردباری ‪.‬‬                          ‫‪ . 6‬توخوارکارتر کی «من بردبار عاشق‬
    ‫«منوچپری د؛مفالی ‪.*۸۸‬‬
    ‫‪ - ۷‬از‪ :‬خوارکار ی ( مصدری ) رك‪ :‬خوارکار ‪.‬‬                                           ‫‪ :‬خوارکار ‪.‬‬     ‫رک‬         ‫۔‬       ‫‪1‬‬


    ‫_؛ مصحف «خوازه» (هم‪).‬‬  ‫‏‪ ٩‬ظ‬                           ‫‪ - ۸‬باين معنی *خوارکار »>صحیح است‬
    ‫‏‪27287۷۲ .1١‬‬     ‫»ور که ‪ :‬کواز ‪۰‬‬                ‫‪۶‬ت ظ ‪ ,‬مصحف «حوازه (ھ‪.‬م‪(.‬‬                                          ‫‪.‬‬       ‫‪ :‬خو‬     ‫ورك‬



    ‫خواستن آرزو کردن)‪ .‬کردی ‪( 01122۷1‬من‌میخواهم) ‪ ۰‬مازندرانی ‪( 22۷722011‬کین‌خواء)‬                                                        ‫‏(‬
                                                                             ‫‪۰‬‬       ‫«واژه امەس ‪۹۳۲‬‬           ‫«اسفا‪۲ :۱‬ص ‪۱۹‬‬
           ‫‪۰‬‬   ‫ودومقدمه‬   ‫بست‬    ‫" ر کت ‪ :‬ص‬         ‫زبان خوارزم‬        ‫بخوارزم‬         ‫خوارز می ‪ ۳‬منسوب‬                    ‫‪۶‬‬

   ‫‪ #‬خوار ی ‪ -‬بروزن کاری » در بهلوی ‪ +012‬بمعنی آسالی است (رکه‪ :‬خوار ) آما‬

                                 ‫در فارسی بمعنی پستی وزبولی وتوهین گرفته‌اند «بشت هااس ‪۳۲۳٩‬‏ ‪.‬‬

==== leaf 240 (p. 780 ) ====
 ‫‪“VAY‬‬                                                                                                      ‫خوای‬
‫هر گاه‬    ‫چنانکه‬   ‫ارادی باشد‬     ‫راستی » بمعنی‬         ‫سازند ‪ ۱‬؛ وبایتمعنی بقتح اول بروزن ملازه هم‬
‫کوبند «حر کت خواسی » ازآن حر کت ارادی‬                                                                ‫آمده است ‪.‬‬
                                        ‫خواهدد ‪.‬‬
                                                         ‫خو اس س بانانی معدوله بروزن طای‪.‬‬
‫حو اسه = بفتح اول بر وزن نواسه ‪۰‬‬                        ‫بمعنی خواستگار و طلبکار باشد ‪ -‬و بفتح اول‬
 ‫نند‬ ‫صورتی باشد که در فالیزها و زراعتهپا نکصب‬             ‫بروزن‌پلای» بمعنی تریس و بیم وهرای باشد ‪.‬‬
‫تا وحوش وطبور ازآن رمیده خان بکشت زار‬
                                        ‫فسرانند ‪.‬‬
                                                        ‫وجزیر؛ مبان دربا باشد؟ ہے‬            ‫فته شده ‪- ۴‬‬        ‫راه‬

 ‫اه بائانی معدوله وسکون کاف‬   ‫خو‬                         ‫و طلب چیزی از کی کردن را نیز گوبند ‪- ۴‬‬
‫فارسی * مرغ خانگی رگوابند ‪ -‬وتخم هرغ را‬                  ‫وبمعنی زر ومال وسامان هم‌هست_ و گاهی یمعتی‬
 ‫نکیفزته اند کوخیوناه (‪ )۱‬تخم مرغ بروغن‬                  ‫اراده گفته مشود چنالکه گویند « خواست خدا‬
                                ‫«ربان کرده باشد ‪.‬‬                         ‫‪.‬‬       ‫‪۵‬‬   ‫اراد خدا‬   ‫شی‬    ‫نود ‪٩‬‏‬   ‫رین‬

 ‫خو ال ‪ -‬با انی معدوله بروزن مال »‬                       ‫‏‪ me‬بائانی‌معدو له باس‌داز ‪۰‬‬       ‫خواستار"‬
 ‫دوده‌ای که بحهت ساختن سداهی ومر کب از دود‬
                                                         ‫لر وکواکار ور خواهتده و طلت هه را‬
‫چراغ کیرند؛ و صم اول بروزن جوال همأ مده‬                                              ‫کوند ‪#*.‬‬
           ‫است ‪ -‬وخوردئی را نگیوزبند *‪.۹‬‬
                                                         ‫خو استه ‪ = ۷‬بائانیمعدو له بروزن راسته»‬

                                                          ‫لءاه‬
                                                             ‫زر ومال واسباب وجمعدت ومامان وملك وا‬
          ‫وزن تاستان » دوات سیاهی رگاوبند ‪.‬‬               ‫وآ لچه دلخواه باشف ‪ 5 ۸‬وترجمه معنی همهت‬

 ‫خلوسته(‪)۳‬ا با انی مفدوله بر وزن‬
                               ‫ا‬                         ‫چنادکه‌درعربی گوبندباله‌منی فلان درفارسی گویند‬
 ‫دانسته» بمعنی‌خو الستان(‪ )۲‬است که دوات ساهی‬                                                      ‫بخواسته فلان ‪.‬‬
                                   ‫ومر کب باشد ‪.‬‬          ‫خو استی* = با ثانی ممدوله بر وزن‬

    ‫‪:‬وابته ‪1‬‬
           ‫م‪ ۱‬خ‬
              ‫(خ‪)۳‬‬                   ‫)‪ (+‬خم‪ : ۱‬خواستان !‬                      ‫‪.‬‬       ‫(خ‪)۱‬اچگشی‪:‬نه‬
   ‫» خواستند که خوازه‌ها‬   ‫رسف‬    ‫تزدىڭ شاور‬       ‫شنبدند که آمیر (مسعود)‬             ‫‪ 2‬اشان جون‬      ‫‪۱‬‬

   ‫؟ ‏ لغتی در «خوست؟ بمعنی‌مالیده‬                 ‫‪٩‬‏ ‪.‬‬
                                                      ‫حن‪۲‬و‬
                                                         ‫زنند وبسیار شادی کنند ‪« » .‬بیهفی ‪ 44‬مت‬
   ‫)‪۰٩1‬‏ ‪ « :‬باشومت آن‌باشد‬      ‫‪ .‬درلغت فری آمده ( ص‬              ‫‪ :‬آبشخوست و بای خوست‬              ‫و کوفته رگ‬
  ‫که بیای دگرفته (کوفته‪ ۰‬دهضدا)رآبخوست |آ[ن باشدکه به ‪ .‬دهشدا] آب درهم گرفته( کوفته‬
         ‫‪ . ۴‬مصدر مرخم «خواستن» ‪.‬‬              ‫‪1‬‬    ‫‪_ ۳‬مخفف آ خوحت («‪.‬م‪).‬‬                        ‫دهشدا) باشد ‪» .‬‬
   ‫اوست بلکه بخواست‬        ‫همی دانیم که حر کت هرسه قم ازان (جم) تبهذات‬                           ‫_‬     ‫®‬
   ‫از‪ :‬خواست ‪ ۳‬ار (یسوندفاعلی "مبالفه)‪.‬‬             ‫‪1‬‬          ‫‪.‬‬     ‫ی‪۱‬‬           ‫واهر است» « زادالمسافرەن ‪۷‬‬

    ‫پهلوی ‪( 8152۷2‬مال)« مینا ‪« » ۲ :۹۳۱‬اسشق ‪ . ۷۹42‬ارمنی ع ‪12150‬‬      ‫‪۲‬‬
                ‫در ‪( ۲20120501‬وارت) » پپلوی ‪( ۲2012052۷2‬وارث) «هوشمان ‪۷۹٩4۰‬‏ ‪.‬‬
         ‫آونکه را خواسته است‌داش کم‪.‬‬                        ‫‪ ۸‬حر کرا داش است خواسته لت‬
    ‫‪۱‬‏‬
     ‫>‪٤‬‬‫شهیدبلخی‪« .‬تاریخ‌ادیبات ‪ .‬ش‪.‬فق‬
   ‫‪ = ۶‬خوار («‪.‬م‪ , ).‬چنانکه درخوالگر‬                      ‫از ‪ :‬خواست ‪ +‬ی (نسبت)‪- ‎‬‬                     ‫‪٩‬‬
    ‫بقه در صفحةٌ ‪۳.۸۷‬‬
          ‫( برهان فاطع ‪)۳۰۱‬‬
```


## [2026-09-14T02:01:49.910Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nimport re\nfor i in range(236,265):\n    head=' '.join(pages[i].split()[:8])\n    print(i, i+540, head[:90])\n\""
}
```


### [2026-09-14T02:01:51.706Z] TOOL RESULT

```
236 776 ‫¬ ‪~A‬‬ ‫ن‬ ‫ز بر‬ ‫وول‬ ‫حنبور ‏‪
237 777 ‫خواجه‬ ‫ها‬ ‫آنچه بدان روز (‪ )۱‬بگذرانند‪ .‬یمنی
238 778 ‫کوپ‬ ‫خواجة اختران‬ ‫خلیفة خواجه مودود وخواجه محمد
239 779 ‫خوازه‬ ‫‪۷‬‬ ‫‪-‬‬ ‫بمعنی خوردنی ورزق وروزی باشد
240 780 ‫‪“VAY‬‬ ‫خوای‬ ‫هر گاه‬ ‫چنانکه‬ ‫ارادی باشد‬ ‫راستی
241 781 ‫خوان پابه‬ ‫یز پا‬ ‫خوالگر ‪ - ۱
242 782 ‫‪۷‬‬ ‫خوانچة زر‬ ‫خو) نجه‪ .‬ررو خوانجه‌دد لن‪-‬‬
243 783 ‫خود خروه‬ ‫”‪“YA‬‬ ‫دایر‪ - ۷‬ویمعنی‌ذات و لقیض‌غیرهم
244 784 ‫‪e Cs‬‬ ‫خجودرا رسن کردن‬ ‫ونایه از علف
245 785 ‫خورخجیون‬ ‫‪YAY‬‬ ‫جوی کوچکیاست که‌ازرودخانةٌ بزر گی‌جدا کرده‬
246 786 ‫خورد‬ ‫خورده زه با انی معدوله بر وزن‬
247 787 ‫خوره‬ ‫اس‬ ‫مودلد به دیر‪ ۴‬موسوم ساختند چه‌بزبان
248 788 ‫ات‬ ‫سپو‬ ‫خوره‬ ‫خورة استخر »‪.‬خورة داراب »
249 789 
250 790 
251 791 ‫خوزی‬ ‫‪۱۷۱‬‬ ‫بروزن‌شولتان ؛ نم‬ ‫خورستان ‪۱‬‬ ‫غله
252 792 ‫‪۳-۲‬‬ ‫خوزی خوار‬ ‫بو سه م‬ ‫و دمعمی‬
253 793 ‫خوشة سیهر‬ ‫‪-۷۹۳-‬‬ ‫وعم بروزن احمداگ ‪ .‬طعامی
254 794 ‫باس‬ ‫حو شی ه با نانی مجهول بوزن
255 795 ‫روانند که سپاهیان‬ ‫ویفتح اول‌قندیل و تیردان گ‬
256 796 ‫‪- ۷۹‬‬ ‫از شراب لملی‬ ‫خون بکطن_اب‬ ‫خون‌دل
257 797 ‫خوید‬ ‫‪۷۷‬‬ ‫ابلای‬ ‫تشدح‪۷‬ت‪-‬و‬ ‫با‬ ‫ن‬ ‫دنیهآب‬ ‫تحتالی
258 798 ‫‪۷ 6‬‬ ‫خوی درد‬ ‫‪-‬‬ ‫هم هت‬ ‫باشد
259 799 ‫یه‬ ‫وعربان خراطین میگوند (‪. )۲‬‬ ‫وحرف خیرمعاف
260 800 ‫—‬ ‫س‬ ‫خپله‬ ‫خهی ‪ - ۲‬بفتحاولبروزن زهی
261 801 ‫سب‬ ‫ست ‪۵ ۱‬‬ ‫خر د بکسراول بروزن
262 802 ‫= ‪.‬‬ ‫خیرو‬ ‫نغری ‪:‬کان ات‬ ‫تاوزن‬ ‫خیری‬
263 803 ‫کز عتارم‬ ‫‪ ۵ ۳‬بزح‬ ‫ازمردم همان‌دایره میگوید
264 804 ‫خیشفوج‬ ‫==‬ ‫میگویند نه مطلق خوی را؛ وبسضی
```


## [2026-09-14T02:02:10.859Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint('==== leaf 243 (p.783) ====')\nprint(pages[243])\n\""
}
```


### [2026-09-14T02:02:11.992Z] TOOL RESULT

```
==== leaf 243 (p.783) ====
 ‫خود خروه‬                                                                                ‫”‪“YA‬‬


 ‫دایر‪ - ۷‬ویمعنی‌ذات و لقیض‌غیرهم آمده‌انت ‪۷‬‬         ‫و لام الف »‬   ‫کلاا صیفتح کاف‬        ‫خوب‬

‫ونان‬
   ‫چ‬        ‫چدنریان‬
                  ‫چنالکه کوبند ف«لانی خو‬
‫میداند؟عنی ذات خود راله دمگریرا »ودر نع‬             ‫خوب کلان۔ بر وزن موی کشان ‪.‬‬
‫مضاف مضمری آید ‪ -‬و ضد پیگانه هم هست‬                 ‫تنگه باشد ‪.‬‬ ‫بهاترضم‬
                                                                      ‫بمعنی خوب کلا است ک‬
‫چنانکه کوبند «فلانی ازخوداست » معنی بیگاله‬
                                 ‫يت ‪. ۸‬‬
                                                    ‫بای قارسی‬   ‫خو بله ‪٣‬‏ ا انی ممدو لد و‬

‫خود بر ست د باانی معدوله و کر‬
                                                            ‫بروزن طبله » بمعنی ابله ونادان باشد ‪.‬‬
  ‫ستا‬
    ‫خجبوردو‬
          ‫بای فارسی ؛ مردم متکبر و مت‬               ‫حوج ‪ -‬بروزن کوچ کله سر وفرق‌سر‬
                                       ‫باشد ‪.‬‬       ‫مرغانرا گونند ‏ وکوشت پار سرخی باشدکه‬
 ‫خود یسور ‪٩‬‏ با‪-‬نالی مسوله کور‬                      ‫برسرخروی است؟ ‪ -‬ونامگلی‌است سرخ‌رنگه‬
‫بای ابجد (‪ )۱‬و سین بی لقطه (‪ )۲‬بواو رسیده‬            ‫که آنرا بستان افروز کوبند ‪ -‬کووسفندجنگی‬
‫ویزای قطه دار (‪ )۳‬زده ‪ ,‬آتشکده آنربابجان‬             ‫رانز گفته‌اند ‪ 1 ۴‬وترك کلاه‌خودهم‌هست ‪ -‬وتبزی‬
‫است*‪٩‬‏ و بجای بای ابجد بای حطی (‪ )4‬نیز‬              ‫طاق وایوان را نگیوزبند ‪ -‬و حربر سرخیکه‬
                                      ‫هست ‪.‬‬                                  ‫بکرلوگاه نیز نندند ‪.‬‬

‫خودخروج‪ -۱۱‬با جيم فارسی »‬                            ‫خو چه ‪ - °‬بانانی‌نجهول بروزنکوچه‪.‬‬
‫به‌عنی تاج‌خروس است وآن گوشت سرخی باشد‬              ‫نمعتی دوم خوچ است که گل‌ستان افروز‪ -‬وتاج‬

                      ‫که برسرخروس است ‪.‬‬                                           ‫ومغفر خروی باشد ‪.‬‬
 ‫خود خروه؟ د باهای هوز‪ .‬بروزن‬                       ‫با ثانی معروف بر وزن زود »‬         ‫جود‪.‬‬

 ‫ومعنی خود خروس است که تاج و مغفر خروس‬                ‫بمعنی تاج ومخفرباشد ‪ - ۷‬وبائانی معدوله‌بمعن‬
                  ‫و کل بتان‌افروز‪ ۳۱‬باشد ‪.‬‬          ‫او باشد چنانکه گویند د خود داند » سنی او‬

     ‫(‪ )۳‬چك‪ _:‬شطه دار ‪.‬‬             ‫(‪ )۷‬چك ‪- :‬بی لقطه ‪.‬‬               ‫(‪ )۱‬چك ‪ :‬و کسربا ‪.‬‬
                                                                          ‫(‪ )4‬چك‪ :‬با‪.‬‬

  ‫رك ‪ :‬لفت فری ‪ ۵۹۰‬ورك‪ :‬خروج و خوچه‪.‬‬            ‫‪۴‬‬    ‫مصحف «خو بله»‪.‬‬     ‫‪۳.‬‬    ‫رکه‪:‬خوب کلان‬       ‫‪۱‬‬

                                     ‫غوچه (تاج خروس)‪« :‬اسفا‪۲ :۱‬ص ‪۰۷6‬‬         ‫عه‬    ‫‪۵‬‬    ‫غوچ ‪.‬‬
   ‫» تاج خروی‬   ‫ورك ‪ :‬خوچ ‪ « :‬خوج‬

   ‫(ر‬
    ‫‪ - ۱‬پارسی باستان ‪ 801121‬د‬                   ‫بود و خوچه نکیوزبند ‪« ».‬لفت فری ‪۵٩‬‏ ح‪٩۱‬‏ ‪.‬‬
    ‫خود سر تیز) « اثپیگل ص ‪. ۱۲۲۰‬استی ‪ (005‬کلاه ناح) «ك ‪ .‬است‪۱٤۸‬‏ =‬                      ‫‪09‬‬     ‫‪8‬‬
   ‫‪ - ۲‬ضمیرافس" پهلوی )‪×4۷‬‬              ‫پارسی خوی «لغت فرس ‪۱۲٥۰‬‏ ممرب آن خوذة «نفی؟ ‪.‬‬
   ‫ربک ‪« ۹۳۱۰‬مینا ‪۲٥ :۹۳۱‬‏ «ناوادبا ‪ ۷۹۱۰‬قس‪:‬پارسی باستان ‪ )2۷(01 -‬او ‪6687۷5‬‬
                                                                          ‫‪ ۵‬نی‬
  ‫(خود» خویش)‪:‬اسفا ‪ ۰۲ ۱‬ص ‪ ۰۹۱۳۷۸۳ ۰۱6۲ ۰۹۱۱ ۸‬استی‪« 8680621‬کث‪ .‬است‪› ۹۳۱‬‬
  ‫باين معنی «خودی»است‌و مقپوم آن از جملهمذ کور‬          ‫‪۸‬‬          ‫ورک‪ :‬ص لد از دباچه موف ‪.‬‬
  ‫‪٩‬‏ رکه ‪ :‬خود سوز‪.‬خودی سوز (ظ‪ ,‬مصحف ‪:‬‬                          ‫در متن مستفاد میشود نه از «خود) ‪.‬‬
  ‫‪۶‬أخون ازقول نظامی است ‪ .‬رکه ‪:‬‬
                              ‫م‬                      ‫خودیوز در شعر نظامی ‪ ,.‬ک ‪ :‬خودسوز) ‪.‬‬
                ‫خودی سوز ‪.‬مهمترین آآتشذکرد؛بایجان آذ رکشنپ است ‪.‬رکه ‪:‬کآذشرسب ‪.‬‬
   ‫‪۹۸۷‬‬   ‫حرهٌ‬
            ‫فد‬‫صبه‬
                ‫بق‬
```


## [2026-09-14T02:02:20.593Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(pages[237][-1800:])\n\""
}
```


### [2026-09-14T02:02:21.756Z] TOOL RESULT

```
                   ‫‪8‬اجیکی‬
                           ‫‪0‬جة ت‬   ‫‪-۱‬‬
                               ‫‪1‬درله‬                  ‫رك ‪ :‬اسقا ‪۲: ۱‬ص ‪۰۲‬‬       ‫‪۵‬‬
   ‫» درهندوتر کیه ‪( 805 -‬درهندوستان ‪ -‬اصطلاحاً خوجه بییروان اسمعیلیه‬       ‫شمارة ‪ ۸‬ص ‪۹۱۱‬‬
 ‫اطلاق شود ) ‪ ,‬معرب آخنواجا « تفس» « دزی ج‪ ۱‬ص‪٤٠٩‬‏ ‪ ۰‬آفای پورداود این‌کمه رامر کب‬
  ‫از ‪ ۵۷2 = 2۷27 :‬اوستابی بمعنی خود ‪ 16) +‬که درآخرکلمات اوستابی درآبد بمعنی لل و‬
  ‫همچنین‪.‬جمعاًبمنی کسکه دارای‌خودییوشخصیت مستقل‌است‪,‬دانته‌اد‪ «.‬حافظ شبرین سخن ‪, ۲ ۳۷‬‬
  ‫صفیر = چه)دانسته‌اند تیه‌ای‌در‬   ‫وند‬
                                     ‫س‪+‬‬‫یای)‬
                                          ‫((خد‬
                                             ‫كلوی‬
                                                ‫چی به‬
                                                    ‫بعضی اصل] نرا«خواتای‌چث» از خواتا‬
  ‫نزدیکی درباچة زره (هامون ) سیستانست ‪.‬انرا هم « کوه خدا» گویند وهم «کوء خواجه » (اين‬
           ‫درباچه و کوه ترد زرتشتبان جنبةٌ تقدس دارد ) واين امرشاید موند فرضةٌ اخیرباشد ‪.‬‬
   ‫‪ - ۷‬بین این دومعنی خواجه درحقیقت هیچگونه اختلان طفظ ومعنی نست و خواخه‬
   ‫درهردو مورد بمعنی بزر که وسرور وصاحب است بااين تفاوت که درمورددوم درقدیم «خواجمسرا»‬
   ‫میگفتند یعنی بزر كك و سرور اندرون» و چون مردم نامحرم لمیتوانته است درحرم راه بايد در‬
  ‫دستگاههای استبدادی قدیم مردالی را که بابد برای خدحت تریدت شوند خصی مکردلد ‪.‬کم کم‬
   ‫مردم ‪,‬در استعمال » لفت « سرا » را از دبال خواجه انداخته و بهمان لفظ خواجه افتصار‬
   ‫کرده‌اند‪ .‬وزراصطلاح عامه خواجه بمعنی‌خصی شده «وآغا » همکه بخواجه سرابان خضی اطلاق‬
  ‫کرده‌اند درحقیفت ترجمةٌ ترکی همین خواجه است وهآغاباشی» معننی بز رکه خواجه سرابان وا‬
                ‫دارد « باد کارسال ‪ ۳‬شمارة ‪٩-۷‬‏ ص ‪ > ۰۳۱-۱۳۱‬ورك ‪ :‬دائرتالمعارف اسلام ‪.‬‬
         ‫هصهفدرحة ‪۰۸‬‬
```


## [2026-09-14T02:02:34.800Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:02:34.808Z] TOOL RESULT

```


```


## [2026-09-14T02:02:38.243Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7",
 "prompt": "Give the full Persian etymology section for خدا (xodâ) — Middle Persian form, Old Iranian reconstruction, and any cited scholars. Also any related terms like خدیو, خواجه."
}
```


## [2026-09-14T02:02:39.996Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4",
 "prompt": "Give the full Persian etymology for خویش (xiš/xwēš) — Middle Persian, Avestan, Proto-Iranian forms and cited sources."
}
```


### [2026-09-14T02:02:43.630Z] TOOL RESULT

```
# Persian Etymology of خدا (xodâ)

## Middle Persian Form
The term derives from Middle Persian **hwtʾy** (xwadāy), meaning "lord."

## Old Iranian Reconstruction
The etymology traces back to **Proto-Iranian *hwatā́wHā** ("lord, god"), establishing ancient Indo-Iranian roots for this term.

## Cited Scholar
**D. N. MacKenzie** (1971) documents this in "A concise Pahlavi dictionary," providing lexicographic support for the Middle Persian form.

## Related Terms
Connected Persian words include:
- **خود** (xod) — "self"
- **خدیو** (xadiv) — "lord, master"  
- **خاتون** (xâtun) — "lady, noblewoman"

## Cognates Across Languages
The root appears in Avestan, Bactrian (khoadēo), Kurdish (xwedê/خوا), and Sanskrit (svadhā́), demonstrating widespread Indo-European distribution of this lexeme for divine authority.
```


### [2026-09-14T02:02:45.401Z] TOOL RESULT

```
# Persian Etymology for خویش (xiš/xwēš)

**Middle Persian Origin:**
The word derives from Middle Persian *NPŠE* / *𐭭𐭯𐭱𐭤* (xwēš), which came from Old Persian *𐎢𐎺𐎠𐎡𐎱𐏁𐎡𐎹𐎶* (ʰuvāipašiyam).

**Proto-Iranian Roots:**
The term traces to Proto-Iranian *\*hwaypaθyah*, a compound formation. The first element connects to Old Persian huva, derived from Proto-Iranian *\*hwáh*.

**Proto-Indo-European Foundation:**
The ultimate ancestry extends to Proto-Indo-Iranian *\*swás* (reflexive pronoun) and Proto-Indo-European *\*swós*.

**Related Form:**
The word shares etymological kinship with Persian خود (xwad/xod, meaning "self").

**Note on Sources:**
The entry cites "Pokorny 992" as its reference for etymological documentation, indicating derivation from established comparative Indo-European lexicography.
```


## [2026-09-14T02:02:55.601Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88",
 "prompt": "Give the Persian etymology for خو (xu) \"habit, nature/character\" — Middle Persian and Old Iranian forms, cited sources."
}
```


## [2026-09-14T02:02:57.585Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87",
 "prompt": "Give the Persian etymology for خواجه (xāja) — what origin is proposed, Middle Persian form, and cited sources. Also mention if it's linked to xwadāy."
}
```


### [2026-09-14T02:03:00.480Z] TOOL RESULT

```
# Persian Etymology of خو (xu)

Based on the Wiktionary entry, the Persian word **خو** (xō/xu) meaning "temper, disposition" has the following etymology:

**Middle Persian origin:** The term derives from Middle Persian [Book Pahlavi needed] (hwk' /⁠xōg⁠/).

**Old Iranian parallel:** It shows comparison with Old Armenian **խոկ** (xok), indicating shared Indo-European roots.

**No modern cited sources provided:** The entry does not cite contemporary scholarly works. The only textual reference given is from Rumi's *Masnavi* (c. 1260s), translated by Reynold A. Nicholson, which demonstrates historical usage rather than etymological documentation.

The entry explicitly notes that "Book Pahlavi script for Middle Persian terms" is requested but not yet provided, indicating incomplete etymological documentation in the source material.
```


### [2026-09-14T02:03:03.608Z] TOOL RESULT

```
# Persian Etymology of خواجه (xāja)

## Proposed Origin
The word ultimately derives from **Sanskrit उपाध्याय (upādhyāya)**, meaning "teacher; preceptor; spiritual adviser," transmitted through **Middle Indo-Aryan reflexes** via Central Asian intermediaries.

## Key Details
According to the Wiktionary entry, various Middle Indo-Aryan forms are attested, including Maharastri Prakrit uvajjhāa. The Central Asian loaning source most closely resembles an unattested form **\*vājjhāa**, which parallels Sindhi vājho ("Hindu schoolteacher") and Tamil vāttiyār ("teacher").

## Cited Sources
1. **Asatrian, Garnik** (2011) - "Review: Iranian Loanwords in Syriac" in *Iran and the Caucasus*, volume 15, number 1/2, page 324

2. **Asatrian, Garnik** (2012) - "Marginal remarks on the history of some Persian words" in *Iran and the Caucasus*, volume 16, number 1, page 108

## Note on xwadāy
The entry does not establish a direct connection between خواجه and xwadāy in its etymology section.
```


## [2026-09-14T02:03:20.851Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS grep xvat/xves ===\"; grep -n \"xvat\\|xvēš\\|xves\\|xvatāy\\|xvatay\\|xwat\" SNS.txt | head -20; echo \"=== SNS pages leaf count ===\"; awk 'BEGIN{RS=\"\\f\"}{n++}END{print n}' SNS_pages.txt"
}
```


### [2026-09-14T02:03:21.906Z] TOOL RESULT

```
=== SNS grep xvat/xves ===
29729:xvato 106/13 
30795:xvestar 79/16 
=== SNS pages leaf count ===
242
```


## [2026-09-14T02:03:22.169Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB xwatāy ===\"; grep -n \"xvatāy\\|xvatay\\|xwatāy\\|xvat \\|xvēš\\|xvat,\\|xvēš,\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T02:03:22.227Z] TOOL RESULT

```
=== NYB xwatāy ===
554:apäyistan ['p'dstn'], apāyītan [’p’dytn'] apäy-, 3d p. sg. apāyēt [’p’dt', ^p'dyt'], 3d p. pl. apäyend ['p'dynd], pret. 3d p. sg. apāyist 1. to please a p. (pat) 83%; cigon mēnēyān apäyist as it had pleased (was predestinated by) the heavenly gods 405, v. below. — 2. impers. it is desirable: -m apāyēt 6 han ciš I desire, try to obtain, this 562%, — 3. to be needed 1211-2 also pat. kär. apāyet 14%. 375, andar apāyēnd 105%. — 4. to be proper, seemly 4015 (bē ~). — 5. impers. apäyet auxiliary vb.: must, ought to, shall, should, has to, is bound to, ete. with the p. as indir. obj. (virtual dat.), a) governing an inf., which is as a rule placed after: u api-t xvatāyēh i Ērān šahr vas sal apäyet kartan and thou shalt exercise dominion over Iran for many years 629-31; 918-19, ]014 ete.; in this case preverbs to the inf. are drawn to apäyet; bé — pursitan 1319; ba ~ hištan 1313; kār-ē i apar nē ~ kartan 104%; apārīk 6 [KN] ~ xtartan 94??; less often the inf. is placed before: ēzatan nē ~ 1017-19; pit u mat frazand i xueš rād En and kär u kirpak ... bē üámóxtan ~ the parents shall teach 6522-23; 6519-20; 9113; the inf. sometimes has to be supplied: -
835:reluctancy: atün hàn i kart (v. ?kartan) ~ dahét he will create unwillingness with regard to what you have instituted 45), with the following gl. explaining ~: kū šmāh xvēš rād ne tuvān zuästan, kas šmāh rād ne xvāhēt ‘~ means that you are incapable of an act of will for your own sake and nobody will be willing (to act) for your benefit’ (you will be diffident and inefficient, and nobody will work for you) 45*3; the gist of Yam's speech is expressed in the gl. 452, v. acārēnītam.
1435:enyä [’yny’] otherwise 1377; bē... ~ except: bē magvemart ... ~ ... hec mart pat xčinak i xvēš bē mà pāyēt except the Magians. .. no man shall remain at home 2035; bē pat parvānakēh + yazdān
2723:nikand [nknd] pt. = pret. 3d p. sg. 92%, uncertain: api-§ góhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, i. e. the heavenly light which forms the substance of the material world, cf BdA p. 11? Ohur- mazd hac han i xvēš xvatēh getäh rošneh uy hac getäh rošneh karp + dāmān i xue$ frac brihénit, where gētāh rošneh seems to be a synonym of göhr xtarrah; nikandan from ni + the root kan- ‘to throw’ which is found in apakandan (g.v.).
3004:44%; pat hamāk rēc 49°; asp 2... ke pat rče-E 70 frasang be čiyend-(h)E (v. āma- tan) 610-31; pat bavandakéh i 30 sal 561; pat hazārak sar 99° etc.; pat har za- màn 10472; pat har gah u zaman 71%; pat € bar at one time 328; pat hàn yavar* ka on the occasion when Pl:2; pat han afterwards; pat fratoméh, pat avdoméh, pat bundahisneh, pat frazam: v. below II. 9. — 3. instrumental: pat dast dästan; pat han + dašn pad frac škast 531-12; pat uzvan ...saxtan göbend 1069; pat zafar apāc jūtār bütan 48°; pat cašm dītan; pat hàn + 4 äyö- žišn rahy vāzēt 519-11; pat ap (4) zarr nipistak 107°; with abstract nouns: pat zór u hunar ...hecakhaccahul hixt 15%; personal 7129-21, - II. in a figurative sense: 1. to the benefit of, or to the detriment of: cé-§ pat man névakéh vas kart 351; pat fradandàn i man vizandkār bavend 143. — 2. causal: pat zor... i Šahpuhr kanicak avd sahist 158-9; <pat> patvand because of relationship 117°; api-t pat ruvän dusxtäreh eton bavēt cigón 45°; — as a reward for: har kasé pat han and kar u kirpak ... mizd pātdāšin dahénd 10324-25, — 3. concessive: in spite of, notwithstanding, e. g. dānākēh + Zartuxšt pat han 1 aparnäi dātēh 539. — 4. final: for, e.g. pat én kar frestit ku ... 139; pat kār-ē Sut estat 1417; pat pātdāšin 9519-13; pat han + hunuskän ken 50'-?; pat xvēšēh u āzātēh dātan 117°. — 5. pat nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 mart nān-ē ka xuarend sagr hend 86?1—?, — 8. in a great many ex- pressions and idioms in varying func- tions, e.g. in such idioms as refer to domination (over), struggle, fight eto. (with, against), accusation (3714), excuse
3029:patigriftan [ptglptn', MKBLWN-], pati- gruftan [ptglwptn'] pačir- [MKBLWN-, ptyl-], pt. = pret. pass. 3d p. sg. patigrift [ptglpt'; MKBLWN.t, MKBLWN-x, 2876, 299. 611; -x, 21, 18%] patigruft [ptglwpt'] 5811. 6015: to receive, to ac- cept, to take up, often with the prev. frac: 1. Bastvar (PLK”) pat dast fräc patigrift B. caught *the battle-axe (just swung by the attacking enemy) with his hand 2875-26; barak xvēš pat dast frac patirét he himself takes command of the steed (by grasping the reins) with his hand 299. — 2. en den i mäzdesnän hac Ohurmazd patigrift he received the Maz- dayasnian religion from O. 18%2?sq. 1919, ete.; hàn 4 Evak frāc patigrift u apārīk hac dastavar hist the one (doctrine) he accepted and the other he excluded from the canon 10954. — 3. to agree 215; to accept, to comply with 381; göbiön ~ to receive the (divine) command 5811, 6028. — 4. pat fradandeh ~ to adopt as one's son 275; pat zanēh ~ to espouse 161; pat nikühdareh ~ to take charge of 8213. — 5. kē hac šmāh hàn patirét marnjénitan ? who among you takes it upon himself to slay this man? 4217; oišan-ic . . . baxtan
3627:310 šāyīt [š?dyt'], cond. 3d p. sg. (nē) &ayit hat 711%, to be able, capable, 1. with a pers. subj.: kad šāyem griftan? when shall we be able to catch him? 75; 8?;-4 martömän šāyēnd ayāftan 887-9; Sūšāns apāk Kai-Xösröi kartan šāyēnd. 8820-22; 908; — 2. with a non-pers. subj.: amäh garān ziyän ... haciš šāyet butan serious harm must necessarily arise for us: from it 191-?; ctš-ē ke ziyān ne haciš Sayist bütan from which no harm could arise 411-12; kū ātaxš haciš nē šāyet vextan that is: the fire cannot break forth from it 95! (gl.); — 2. impers.: it is possible, in varying modal senses: it can, may, might (be), it is proper, suitable, fitting, permis- sible; ‘perhaps it will... .’; it is predestin- ed, necessary, must, ought to, should, passim; the difference between šāyet and tuvan may be illustrated by 719-3; hakar tài 3 rēc griftan ne šāyet, pas hac hin griftam ne tuvdn if he cannot be caught within three days it will be im- possible to catch him; sdéyet ku perhaps 81. 242; ma hakar-am ... nē brihénit estet ku Erän-sahr pat ēv-xvatāyēh be šāyēt vīnā- ristan it is perhaps not predestined for me that I should bring E. together into one kingdom 137-9; šāyet butan ka šāyet butan “it is predestinated to happen when it is predestinated to happen”, it must happen when it must, Fate will necessarily be accomplished 231-? (cf Skr yad bhavisyati tad bhavisyati); kū yam etön névak pat xuatäyeh šāyet kartan that is: so beautiful & bowl must be made for royal persons 6015 (gl.); ānēd x"arisn šāyet x"artan it is permitted to take food here 76%, v. s. v. frayist ; tài Emahčip x"artan ne šāyet during one whole month it was not possible to drink of the water 2017; — if the real subj. is a person the pret. šāytst has regularly impers. construction: asvārān ... hixtan nē šāyist the equestrians could not haul up 153-4 (cf 887-8, above sub 1); ke (indir. obj.) cim 4 han catrang vicārtan šāyist anyone who could solve the problem of this game of chess 11817-18; without
3818:tuvän [twb?n'] 1. adj. mighty, powerful, energetic 559. 6619; subst. what one is able to do, v. s. v. sämänihä. — 2. impers. vb.: it is possible, one can, is able to; the subj. is an encl. pron., or a subst. in the cas. obl., or a form felt as a cas. obl.; construed with an inf., which is generally placed before, less often after ~; pret. ~ būt; a) without a subj.: 6 x¥és kartan nem 9?" ; griftan ne" (ef s. v. Säyistan) ete.; — b) with a logical subj.: man zatan nē ~ I cannot slay him 99%; man zivistan ne ~ 1035-5; api-tan griftan ne ~ 7%; ete.; ka-tan ~ when it will be possible for you 911; šmah xvēš rād ne ~ x"astan 452-3, v. axtäyisneh; aš pād i man... apar daštan ne ~ büt he was not able to „.. 3318-19. 48-8 2-5 vicārtan nē ~ 11912; cand-šan ~ dätan as much as they pos- sibly can 79%; apäc daštan ke ~? 247; martömän ... ayaftan u dānistan ne ~ mankind cannot ... 804-5; 10926-??; duš- man pat dušman hin nē ~ kartani... 414-15, 619-20. Pēc kas vicārtan ne ~ būt 11921. — From Av. (638 sg.) tav-; MPrs twn; Ps. twb?n-; Paz. tuq, tva; NP tuvān, tavān; cf tāyītan and tahé-kar.
3899:Vadagān [wtk?n'] patron. or pl. cas. obl.: adak-it 1000 sāl xvatāyēh i gehän dahom cigon 6 ~ dahyupat Dahāk dāt then I will
4376:xYatayéh domination, dominion, reign 620, 727, 1311.19.21 ete. passim; v. also zēšt-xvatāyēh, duš-xuatayeh, ēv-xYatāyēh, ēvak-x".; KZŠPrth hwtwypy, Gr. v. šeo-
4385:xvēšāvand [hwys?wnd] belonging to one’s own family, pl. cas. obl. —-än members of one's own family 9°.
4444:yazet [Prs inscr. and Ps. yzdty, BP yzdt'], pl. cas. obl. yazatān [yzt’n] HajB: 2. 4, commonly yazdän [inser. yzd’n, BP yzd?n'] Prth yazatān [y?ztn] HajA:3.4. SPrth 5.7.12, god: Atur ~ 252; Gosurvan ~ 3476-27; Nerösang ~ 60°; Mihr ~ 961; hin ~ (se. Zartuxst) vànom 61°; ~ a god, or possibly already (as in the Ps.) God 11918; — ~ as pl. cas. rect.: hamak ~ 104* (together with pl. cas. obl. amah- raspandan and martomčin used as pl. cas. rect.); — pl. cas. obl. yazdan (ete.) a) gen., often placed before its subst.: pat yazdan hayyäreh 314-15, 121* (but pat hayyd- reh i y. 50%); yazdān xvēš hom 6219;
```


## [2026-09-14T02:03:30.304Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"xvat\\|x\\\"at\\|xva[st]\\|hvat\" SNS.txt | head -30; echo \"--- count lines ---\"; wc -l SNS.txt"
}
```


### [2026-09-14T02:03:30.363Z] TOOL RESULT

```
4334:oWLj^araavandlh xvastan: ww»i*i2> ^'^ , 
7175:.jii>*: xvastar: N V#*y 
7756:1— r/)\J .(^y^j xvastan iL(Mir.Man. II, 48) 
29729:xvato 106/13 
30740:x v 3his xvastan 58/9 
30745:xvastag 58/3 
30746:xvastan 111/8 
--- count lines ---
34173 SNS.txt
```


## [2026-09-14T02:03:36.169Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29700,29740p' SNS.txt; echo \"==== around 30790 ====\"; sed -n '30780,30800p' SNS.txt"
}
```


### [2026-09-14T02:03:36.256Z] TOOL RESULT

```
xara- 46/1 
xumba- 73/7 
xraosya- 44/21 
xratu- 40/17 
xrafstra- 40/10 
xsaera- 199/11 
xsagra. vairya- 199/7 
xsapan-/xsapar 197/13 
xslra-? 206/8 
xsudra- 203/6 
xsnSvayeiti 202/7 
xsn3sa-, xsna 202/4 
xsnuraaine- 203/18 
xsmaiby 37/4 
xlva^wa- 205/2 
xivas- 10/21 
xsvasti- 313/6 
xsvas. mahya- 37/9 



x v a-/hva-hava- 79/10 
x v aepai$ya- 267/5 
x v aSturaant- 78/7 



x v a5tvada0a 78/12 
x v aini 59/22 
xvato 106/13 
x v a-data- 62/22 
x v afta-xv a fsta 62/15 
x v araiti 70/9 
x v aranah- 127/3-187/2; 
xVar-xsaSta- 70/19 
x v astan5m 175/7 
x v 30ra- 59/6 
x v 3para- 56/12 

G 

==== around 30790 ====
x v ast 66/4-308/17 
x v as -101/2 
x v astar 101/4 
x v Sdflgdah 78/8 
x v 5dOgdat 78/14 
x v 5s 79/9-267/4 
x v 5slh 267/12 
x v 6sk3r 79/22 
x v 5sk3rlh 80/2-6 
x v eskarlha 30/4 



xvgs sahgah 79/15 
x v £stan 267/13 
xvestar 79/16 
x v etCu:raan 78/5 



ySkand 299/9
```


## [2026-09-14T02:03:51.367Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aepai\\|5epai\\|3epai\" SNS.txt SNS_pages.txt | head -10"
}
```


### [2026-09-14T02:03:51.435Z] TOOL RESULT

```
SNS.txt:29722:x v aepai$ya- 267/5 
SNS_pages.txt:15333:                                                              x v aepai$ya-    267/5   gar5. damana- 322/19
```


## [2026-09-14T02:03:56.871Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"sister, fem\" \"sibling\" \"ethnic,\" \"sorority\" \"sororal\"; do echo \"=== $w ===\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-14T02:03:57.877Z] TOOL RESULT

```
=== sister, fem ===
=== sibling ===
=== ethnic, ===
10016:custody,  n.  —  L.  custodia,  ‘watching,  guard,  care, protection’,  fr.  custos,  gen.  custodis,  ‘watch, guard,  preserver,  keeper,  overseer,  protector’, fr.  I.-E.  base  *(s)qeudh-,  ‘to  cover’,  whence  also L.  cudo ,  ‘helmet  made  of  skin’,  OI.  kuharam, ‘cave’,  kuhufr,  ‘new  moon’,  lit.  ‘that  which  is hidden’,  Gk.  xeijfleiv,  ‘to  cover,  hide,  conceal', W.  cudd,  ‘a  hiding’,  cuddio,  ‘to  hide’,  Mir.  codal, ‘skin’.  Cp.  custos.  For  derivatives  of  the  related base  *(s)qeut-  see  hide,  ‘skin’.  The  bases *(s)qeu-dh-  and  *(s)qeu-t-  are  dental  enlarge ments  of  base  *(s)qeu-,  ‘to  cover,  hide’.  See  sky and  cp.  words  there  referred  to. custom,  n.  —  ME.  custume,  custome,  fr.  OF.  cos¬ tume,  custume  (F.  coutume),  fr.  L.  consuetu- dinem,  acc.  of  consuetudo,  ‘custom,  habit,  use, usage’,  fr.  cdnsuetus,  pp.  of  consuescere,  ‘to  ac¬ custom’,  fr.  con-  and  suescere,  ‘to  become used  or  accustomed’,  fr.  I.-E.  base  *swedh-, whence  also  Gk.  eS>oc;,  Jj-fto?,  ‘custom,  usage’, £9vo?,  ‘race’.  Base  *swedh-  is  compounded  of *swe-,  ‘his,  her,  its,  one’s  own’,  and  *dhe-,  ‘to put,  place;  to  do,  make’,  hence  lit.  means  ‘to make  one’s  own’.  See  sui-  and  the  verb  do  and cp.  consuetude,  costume,  which  are  doublets  of custom.  Cp.  also  assuetude,  de  suetude,  man- suete,  mastiff,  sodality.  Cp.  also  ethical,  ethnic, hetaira.
13738:ethnic,  adj.,  related  to  a  race.  —  L.  ethnicus,  fr. Gk.  idhuxcip,  fr.  sffvoc,  ‘nation,  race’  (in  Eccles. Greek  the  plural  28-vv)  means  ‘the  heathens, gentiles’).  Gk.  eUvo?  prob.  stands  for  *oFe&vo? and  orig.  meant  ‘one’s  own’.  It  is  rel.  to  effo? (for  *erF£ffo?),  ‘custom,  usage’.  See  ethical  and cp.  ethnos.
13740:Gk.  eOvo?,  ‘nation,  race’.  See  ethnic, ethnography,  n.,  the  description  of  races.  —  Com¬ pounded  of  ethno-  and  Gk.  -ypaepia,  fr.  ypx9Ei,\i, 'to  write’.  Sec  -graphy.
=== sorority ===
35365:Derivative:  sissy-ish,  adj. sister,  n.  —  ME.  sister,  of  Scand.  origin;  cp.  ON. systir,  Swed.  sister,  Dan.  .tester,  which  are  rel. to  OE.  sweostor,  swustor,  OS.  swestar,  OFris. swester,  suster,  MDu.  suster,  Du.  zuster,  OHG., MHG.  swester,  G.  Schwester,  Goth,  swistar, from  I.-E.  base  *swesdr,  whence  also  OI.  svasar-, Avestic  xvatjhar-,  Toch.  A  sar,  B  ser,  Arm.  k'oir, L.  soror,  OSlav.  sestra,  OPruss.  swestro,  Lith. sesud,  OIr.  sittr,  W.  chwaer,  OCo.  huir,  ‘sister’, Gk.  lop  (in  the  vocative  Sop).  I.-E.  *swesor  is compounded  of  the  reflexive  base  *swe-,  ‘his, one’s  own’  (see  sui)  and  -sor,  ‘woman’,  fr.  I.-E. *ser-,  ‘woman’,  which  appears  also  in  the  OI. fern,  forms  tisrdh  (dissimil.  fr.  *tri-sor ),  ‘three’, and  catasra(i,  ‘four’.  Accordingly  sister  orig. meant  ‘the  woman  belonging  to  one’s  own kindred’.  Cp.  cousin,  cozen,  sorority. Derivatives:  sister,  tr.  v.,  sister-hood,  n.,  sister¬ ly,  adj.,  sister-li-ness,  n.
35972:Sorex,  n.,  the  genus  of  shrews  ( zool .)  —  L.  sorex, ‘a  shrew',  which  stands  for  *swor-ak-s,  and  is cogn.  with  Gk.  (lpa£  (for  *surak-s),  of  s.m., prop,  ‘the  squeaking  animal’,  from  the  I.-E. imitative  base  *swer-,  *surr-,  ‘to  buzz,  murmur, pipe’,  whence  also  OI.  svarati,  ‘sounds’,  OSlav. svirati,  ‘to  pipe’,  L.  susurrus ,  ‘hum,  whisper’.  See susurration  and  cp.  soricine.  Cp.  also  hyrax. sorghum,  n.,  a  genus  of  grasses.  —  ModL.,  fr.  It. sorgo,  ‘Indian  millet’,  fr.  ML.  surgum,  surcum, suricum,  fr.  L.  Syricum  ( gramerif  (grass)  of  Syria’, neut.  of  Syricus,  fr.  Syria,  ‘Syria’.  See  Syrian, soricine,  adj.,  pertaining  to  the  genus  of  the shrews.  —  L.  soricinus,  ‘belonging  to  the  shrew’, fr.  sorex,  gen.  soricis.  See  Sorex  and  adj.  suff. -ine  (representing  L.  -inus). sorites,  n.,  a  series  of  syllogisms  in  which  the  pred¬ icate  of  each  becomes  the  subject  of  the  next (logic).  —  L. ,  fr.  Gk.  noipcLT^c; ,  (reopen;?,  short  for ( vSXkoyKsij.be,  acopu-nr)<;,  ‘a  heap  of  syllogisms, a  sorites’,  fr.  ncop6;,  ‘a  heap’.  See  sorus. soritical,  also  soritic,  adj.,  pertaining  to  a  sorites. —  Gk.  aeoperixoc,  fr.  atopei-r/]?,  (Topitrii;.  See prec.  word,  resp.  also  adj.  suff.  -a!, soroptimist,  n.,  member  of  a  club  of  business women  and  women  executives.  —  Contraction of  sorority  and  optimist.
35973:sororate,  n.,  marriage  with  a  wife’s  sister.  —  Coin¬ ed  by  Sir  James  George  Frazer  (1854-1941)  on analogy  of  levitate  fr.  L.  soror,  ‘sister’.  See sorority  and  subst.  suff.  -ate. sororicide,  n.,  one  who  kills  his  sister.  —  L.  soro- ricida,  compounded  of  soror,  gen.  sororis,  ‘sister’ and  -cida,  ‘killer’,  fr.  caedere,  ‘to  kill’.  See sorority  and  -cide,  ‘killer’, sororicide,  n.,  the  killing  of  one’stown  sister.  — Late  L.  sororicidium,  fr.  L.  soror,  gen.  sororis, ‘sister’,  and  -cidium,  ‘killing’,  fr.  caedere,  ‘to kill’.  See  sorority  and  -cide,  ‘killing’, sorority,  n.,  a  society  of  women.  —  ML.  sorori- tas,  ‘sisterhood’,  fr.  L.  soror,  gen.  sororis,  ‘sister’. See  sister  and  -ity.
=== sororal ===
```


## [2026-09-14T02:04:03.489Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"cousin,  n\" \"sib,  n\" \"self,  adj\" \"sole,  adj\" \"suicide,  n\" \"sure,  adj\"; do echo \"=== $w ===\"; grep -n \"$w\" KLN_1966.txt | head -2 | cut -c1-1400; done"
}
```


### [2026-09-14T02:04:04.655Z] TOOL RESULT

```
=== cousin,  n ===
9463:pounded’,  which  is  rel.  to  Heb.  kiskes,  of  s.m. These  verbs  are  prop.  Pilpel  forms  of  Arab. kassa,  resp.  Heb.  kdsds,  ‘he  chewed’.  Cp.  Ak¬ kad.  kasasu,  ‘to  cut  small’,  Aram.-Syr.  kiss‘thd, Akkad,  kissatu,  ‘fodder’, cousin,  n.  —  F.  cousin,  rel.  to  OProveng.  cozin; fr.  L.  consobrinus,  ‘cousin-german’,  orig.  de¬ noting  only  ‘the  child  of  a  mother’s  sister’,  fr. con-  and  sobrinus,  ‘a  cousin  by  the  mother’s side',  contraction  of  sordrinus,  from  soror,  ‘sis¬ ter’  (hence  prop,  meaning  ‘sister’s  child’),  which is  cogn.  with  Goth,  swistar,  OE.  sweostor,  ‘sis¬ ter’.  See  sister  and  cp.  cozen.
25235:(for  *sm-neptiyos),  ‘cousin,  nephew'.  Cp.  Gk. veTtoSec  (Odyssey  4,  404;  said  of  seals),  which prob.  means  ‘children,  descendants’,  and  is  the plural  of  vettco?  (equivalent  to  L.  nepos),  but was  refashioned  according  to  the  declension  of ttoiji;,  gen.  710865,  ‘foot’.  Cp.  also  niece,  nepo¬ tism.
=== sib,  n ===
35110:Siamese  twins,  —  So  called  from  the  Siamese twins  Eng  and  Chang  (1811-74).  —  They  were united  at  the  waist  by  a  band  of  flesh, sib,  n.  and  adj.  —  ME.,  fr.  OE.  sibb,  rel.  to  OS. sibbia,  OFris.,  MDu.  sibbe,  OHG.  sippa,  MHG., G.  sippe,  Goth,  sibja,  ‘kin,  kindred’,  and  cogn. with  Russ,  sob,  ‘character,  individuality’,  OSlav, o-sob-a,  ‘person’,  sobistvo,  ‘character,  indivi¬ duality’,  OPruss.  subs,  ‘self’.  All  these  words derive  fr.  I.-E.  base  *s(w)e-bh~,  ‘of  the  same kind’,  which  is  a  -Mi-enlargement  of  the  reflex¬ ive  pron.  base  *se-,  ‘self’.  See  sui  and  cp. gossip.  Cp.  also  Sabine,  Samnite.
=== self,  adj ===
=== sole,  adj ===
35845:sole,  adj.,  alone.  —  ME.  sool,  soul,  sole,  fr.  OF. sol  (fem.  sole)  (F.  seul,  fern,  seule),  fr.  L.  solus, ‘alone,  single’,  which  is  of  uncertain  origin.  It. possibly  stands  tor  *swd-lo-s,  and  lit.  means ‘being  by  himself’,  fr.  I.-E.  base  *sw’<?-,  ‘his,  her, its,  one’s’.  See  sui  and  cp.  desolate,  solitary, solitude,  sullen,  the  first  element  in  solifidian  and in  soliloquy  and  the  second  word  in  feme  sole. Derivative:  sole-ly,  adv.
=== suicide,  n ===
37399:suicidal,  adj.  —  See  suicide,  n.,  and  adj.  suff.  -al.
37400:Derivative:  suicidal-ly ,  adv. suicide,  n.,  the  act  of  killing  oneself  intentionally. —  Lit.  ‘killing  of  oneself’,  compounded  of  L. sui,  ‘of’  oneself  (see  sui),  and  -cidium,  ‘killing’, fr.  -cidere,  ‘to  kill’.  See  -cide,  ‘killing’, suicide,  n.,  one  who  commits  suicide.  —  Lit. ‘killer  of  oneself’,  compounded  of  L.  sui,  ‘of oneself’,  and  -cida,  fr.  -cidere.  See  prec.  word and  -cide,  ‘killer’.
=== sure,  adj ===
37572:sure,  adj.  —  ME.  sur,  sure,  fr.  MF.  seiir,  sur  (F. sur),  fr.  OF.,  fr.  L.  securus,  ‘free  from  care,  free from  danger;  careless’.  See  secure,  adj.,  and  cp. assure,  ensure,  insure.
```


## [2026-09-14T02:04:10.320Z] TOOL CALL #61: Bash

```json
{
 "command": "ls site/pages/447.jpg 2>/dev/null; pdftoppm -f 447 -l 447 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447.png"
}
```


### [2026-09-14T02:04:12.646Z] TOOL RESULT

```
site/pages/447.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 69608 Sep 13 22:04 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447.png
```


## [2026-09-14T02:04:14.675Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447.png"
}
```


### [2026-09-14T02:04:15.460Z] TOOL RESULT

```

```


## [2026-09-14T02:04:15.457Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:04:23.765Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg447.png')\nprint(im.size)\nc=im.crop((560,560,1200,720)).resize((640*3,160*3))\nc.save('pg447-crop.png')\n\" 2>&1 | head"
}
```


### [2026-09-14T02:04:25.263Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T02:04:27.513Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447-crop.png"
}
```


### [2026-09-14T02:04:27.542Z] TOOL RESULT

```

```


## [2026-09-14T02:05:05.102Z] TOOL CALL #65: WebSearch

```json
{
 "query": "Middle Persian xwadāy etymology *hwa-tāwā \"self-powerful\" Avestan xᵛaδāta Nöldeke"
}
```


## [2026-09-14T02:05:06.969Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%87%D8%B1",
 "prompt": "Give the Persian etymology for خواهر (xâhar) \"sister\": Middle Persian, Avestan, Proto-Iranian, PIE forms and cited sources."
}
```


### [2026-09-14T02:05:13.174Z] TOOL RESULT

```
# Persian Etymology of خواهر (xâhar) "sister"

**Middle Persian Origin:**
The word derives from Middle Persian [script needed] (hwʾhl /⁠xwāhar⁠/).

**Proto-Iranian Stage:**
It evolved from Proto-Iranian *hwáhā, which represents an earlier phonetic form.

**Proto-Indo-Iranian:**
The ancestry traces to Proto-Indo-Iranian *swásā, showing the characteristic "s" that shifted in Iranian languages.

**Proto-Indo-European Root:**
The ultimate source is PIE *swésōr, the reconstructed term for "sister" in the ancestral language family.

**Ancient Language Connection:**
Cognate forms appear in Avestan as 𐬓𐬀𐬢𐬵𐬀𐬭 (xᵛaŋhar), demonstrating continuity across related Indo-European branches.

**Cited Source:**
Hayyim, Sulayman (1934) documented this entry in *New Persian–English dictionary* (Teheran: Librairie-imprimerie Béroukhim).
```


### [2026-09-14T02:05:13.381Z] TOOL RESULT

```
Web search results for query: "Middle Persian xwadāy etymology *hwa-tāwā "self-powerful" Avestan xᵛaδāta Nöldeke"

Links: [{"title":"خدا - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7"},{"title":"Khuda | Religion Wiki | Fandom","url":"https://religion.fandom.com/wiki/Khuda"},{"title":"NÖLDEKE, THEODOR - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/noldeke-theodor/"},{"title":"English God and Farsi Khuda | WordReference Forums","url":"https://forum.wordreference.com/threads/english-god-and-farsi-khuda.2370644/"},{"title":"How Do You Say 'God' In Persian? (Khoda)","url":"https://persianwithel.com/glossary/khoda/"},{"title":"Contents Etymology Zoroastrianism Islamic usage","url":"https://www.markfoster.net/dcf/Khuda.pdf"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/fr/concept/58205684"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/58205684"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/fr/concept/13674707"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/en/concept/12053944/concepts"}]

Based on the search results, I can provide you with information about the etymology of Middle Persian xwadāy and its relationship to the Avestan form and Nöldeke:

The Middle Persian xwadāy ultimately derives from Proto-Iranian *hwatā́wHā ("lord, god"), with the form rendered in Book Pahlavi as an Aramaic ideogram.

The term cognates with Avestan xᵛaδata ("self-determined") in the sense of "not dependent on anything/anyone". The Avestan cognate xᵛaδāta ("self-determined, self-existent") preserves the older sense, "the one who exists by himself."

Regarding the etymology with "*hwa-tāwā" meaning "self-powerful": an alternative Old Iranian etymology has been proposed as *xva-tāwan- "powerful (tawān) by itself", though this appears as one of several competing etymologies rather than the standard account.

As for Nöldeke, the search results show that he provided a substantial introduction addressing the history and origins of the Middle Persian Xwadāy-nāmag ("Book of Kings"), but the results don't contain specific details about Nöldeke's views on the etymology of xwadāy itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:05:21.589Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88",
 "prompt": "Give the Persian etymology of خدیو (xadiv) — Middle Persian / Old Iranian source, and its relation to خدا."
}
```


## [2026-09-14T02:05:23.928Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s(w)e-",
 "prompt": "Does this reconstruction page exist? What is the PIE reflexive/possessive root for \"self, one's own\" and its descendants? If redirected, say so."
}
```


### [2026-09-14T02:05:26.997Z] TOOL RESULT

```
# Persian Etymology of خدیو

## Middle Persian/Bactrian Origin

According to the Wiktionary entry, خدیو is "inherited from Middle Persian" and ultimately derives from Bactrian χοαδηο (khoadēo, "lord").

## Relation to خدا

The entry lists خدا (xodâ) under "Related terms," indicating a connection between the two words. However, the document does not explicitly explain their etymological relationship. Both words relate to concepts of divinity and rulership in Persian, but the source material does not detail how they are linguistically connected beyond noting they are related terms in the language.
```


### [2026-09-14T02:05:30.045Z] TOOL RESULT

```
# Proto-Indo-European *swé

Yes, this reconstruction page exists in Wiktionary. The PIE reflexive/possessive root is **\*swé**, meaning "self" as a reflexive pronoun.

## Key Information

**Etymology**: According to the article, "This stem (and its substantive pronoun) was originally a reflexive element referring to all persons and numbers (as in Sanskrit and in Balto-Slavic)."

**Declension** varies by scholar:
- Multiple reconstructions exist from Sihler, Ringe, Beekes, and de Vaan
- Forms include accusative \*swé ~ \*se, genitive \*séwe ~ \*soy, and dative \*sébʰyo

## Major Descendants

The root produced descendants across Indo-European languages:

- **Greek**: ἕ (hé) from Proto-Hellenic \*hwe
- **Latin**: sē, suī, sibi via Proto-Italic forms
- **Sanskrit**: स्वयम् (svayám)
- **Gothic/Germanic**: Various reflexes through Proto-Germanic
- **Slavic**: Proto-Slavic \*sę (accusative) and \*sebe (genitive)
- **Celtic**: Proto-Celtic \*swe

The reflexive pronoun spawned numerous derivatives including possessive adjectives and other grammatical formations across daughter languages.
```


## [2026-09-14T02:05:41.548Z] TOOL CALL #69: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خدا' --note 'page 447, root Seu 1, node 3 Xodâ: modern etymology MP xwadāy < PIr *hwatāwHā' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خویش' --note 'page 447, root Seu 1, node 5 xîš < MP xwēš < OP huvāipašiya / Av. x'aēpaiθya' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خو' --note 'page 447, node 5 xŭ habit < MP xōg' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خواجه' --note 'page 447, node 3 extra خواجه: modern view (Asatrian) from Skt upādhyāya, not xudāyča' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خواهر' --note 'page 447, node 14 xâhar < MP xwāhar < Av. x-aŋhar- < PIE *swésōr' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/خدیو' --note 'page 447, node 3 extra خدیو: Bactrian khoadēo' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s(w)e-' --note 'page 447, root Seu 1 = PIE *swé reflexive' 2>&1 | tail -3"
}
```


### [2026-09-14T02:05:42.490Z] TOOL RESULT

```
Exit code 1
(eval):1: unmatched '
```


## [2026-09-14T02:05:47.833Z] TOOL CALL #70: Bash

```json
{
 "command": "for u in \"خدا:node 3 Xoda modern etymology MP xwaday\" \"خویش:node 5 xis from MP xwes OP huvaipasiya\" \"خو:node 5 xu habit from MP xog\" \"خواجه:node 3 extra xwaja modern view Asatrian Skt upadhyaya\" \"خواهر:node 14 xahar MP xwahar Av x-anhar PIE swesor\" \"خدیو:node 3 extra xadiv Bactrian khoadeo\"; do w=\"${u%%:*}\"; n=\"${u#*:}\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 447, root Seu 1, $n\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T02:05:51.656Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0b7766949e361ef0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7952d43208ed162.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bacbef06b2af2d51.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eef1cdebe6502a64.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/363ec3ab8cf4fa63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d3c8c6a601f8c29d.txt
```


## [2026-09-14T02:05:55.457Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s(w)e-' --note 'page 447, root Seu 1 = PIE *swe reflexive (redirects to *swe)' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/ethnic' --note 'page 447, node 11: Greek ethnos < PIE *swedh-no-' 2>&1 | tail -2"
}
```


### [2026-09-14T02:05:57.442Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8290e3021e58305a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3a68f544fa77bc3.txt
```


## [2026-09-14T02:06:01.333Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 swesor ===\"; grep -n \"su̯esor\\|suesor\\|s\\[u\\]esor\\|swesor\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -8; echo \"=== WLD Bd2 se-, sue- reflexive ===\"; grep -n \"Reflexivstamm\\|Reflexivpronomen\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -8"
}
```


### [2026-09-14T02:06:01.424Z] TOOL RESULT

```
=== WLD Bd2 swesor ===
12500:DaB idg. bJtrdior fAkzent wie suesor- „Sch^vester“; zu bher- „tragen, 
29666:unter eigenen Schlagworten behandelten suesor-, suekuro-s, 
34554:sijelio(n)- — suesor- 
34598:suesor- „Schwester‘‘. 
34602:*5Wsor; n. pi. Uor-lc aus "^suesores., g. sg. Her aus ^suesros', Hiibschmann 
34609:sohn“) ; air. slur „Schwester‘‘ suesor).^ d. a. sitir.^ g. sethar (Analogic nach 
34631:IP. 29, 124 ahd. wasa „Base“ fur eine 5-lose Nebenform von ^suesor, 
=== WLD Bd2 se-, sue- reflexive ===
34637:Idg. *s{u)e-sor- zum Reflexivstamme se-, und im Ausgang wie fem.
```


## [2026-09-14T02:06:04.270Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34596,34645p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"=== page marker ===\"; grep -n \"^533\\|^534\\|^532\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head"
}
```


### [2026-09-14T02:06:04.374Z] TOOL RESULT

```
schlafern“, s'^fa ,.toten^‘) zu gewinnen. 

suesor- „Schwester‘‘. 

Ai. smsar-, av. x^awlmr- .,Schwe3ter“ ; arm. Uoir ds. (uber aus 

*5Wsor; n. pi. Uor-lc aus "^suesores., g. sg. Her aus ^suesros', Hiibschmann 
Arm. St. I 55, Arm. Gr. I 504, Meillet Esq. 18, 25, 28, 58); gr. eoq [Vok.] * 
3vydTf]Q. dvEiptog Hes. (kaum ganz heile Glosse, Brugmannll^ 1,333), 
eoQEg * 7ioooi]}covT£g^ ovyyeveTg Hes. (Formen eines psilotischen Dialekts, 
Sommer Gr. Ltstud. 41); lat. soror (dazu sobrinus teils als „Geschwister- 
kind‘*, teils als „Kachgeschwisterkind“ beschrieben, aus *s^esr-7wo5, ~ aksL 
sestrim ,,der Schwestei* gehorig“, vgl. auch ostlit. seserenas „Schwester- 
sohn“) ; air. slur „Schwester‘‘ suesor).^ d. a. sitir.^ g. sethar (Analogic nach 
dem Paradigma mdthir^ g. mathar\ cymr. clucaer, acorn, huir.^ ncorn. Aoer, 
^or, bret. choar (vgl. Pick II* 324, Pedersen KG. I 73 f., II 105 f.); got. 
sivistar (g. d. swistrs^ swistr; hier vollzog sich der ^-Einschub), anord. 
syster^ pi. systr (urnord. swestar^ zu lesen swest^r^ ist kein Zeuge fiir ur- 
germ. Bestand des Korn, auf -or; urgerm, wohl nur -er nach den andern 
Verwandtschaftsnamen), ahd. sweater (*-er!), ags. sweostor.^ suster. 

W a } il e , Etymologischcs W orterbuch. 11. 35 



534 


suT* — suomblio-s 


Noch Tor dem ^Einschub neugeschaffen sind as. siviri „Sohii der Mutter- 
scliwester“, ags. gestviria „Schwestersohn, Yetter“, asehw. swiri „Sohn 
der Mutterschwester‘‘ (vgL ags. „Yaters8chwester‘' yon feeder „YeLtev"‘; 
Pick III ^ 544, Falk-Torp u. sister), — Nicht iiberzeugend halt Sutterlin 
IP. 29, 124 ahd. wasa „Base“ fur eine 5-lose Nebenform von ^suesor, 

Apr. swestro (in die a-Dekl. ubergefiihrt) mit w vielleicht durch dt. Ein- 
fluB, denn lit. sestio^ gen. sesefs nnd aksl. sestra (in die a-Dekl. ubergefiihrt) 
„Schwe8ter“ setzen 'M-loses *sesor- voraus. 

Idg. *s{u)e-sor- zum Reflexivstamme se-, und im Ausgang wie fem. 

ai. ti-srah „drei‘' vermutlich zu Wz. ser- „aneinander reihen‘‘, s. d. Ygl. 
Saussure Mem. 218, Delbriick Yerwandtschaftsnamen 84 f., Johansson Beitr. 
140 f., IP. 3, 226, Solmsen Unt. 205, Brugmann II^ 1^ 333^ Leumann Zfdt- 
Wtf. 11, 60 f. 

sul- (Hochstufe suio-T) „8chwinden, nachlassen, schwach und schweigsam 
werden“. 
=== page marker ===
26296:534, III* 369, Yf. LE^Vb.2 u. llra^ Meillet aaO. (betont die ursprgl. bloB 
34489:532 
34557:533 
34621:534
```


## [2026-09-14T02:06:10.997Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '29600,29680p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T02:06:11.052Z] TOOL RESULT

```
,,Zusammen-sprechen” entstanden (Edgerton KZ. 46, 173). 

"^snedh- (wohl mitWz. *dhe als 2. Gliede, „sich zu eigen machen, ge- 
wohnt”) : ai. svadha ,,Eigenart, Gewohnheit, Sitte, Heimstatte” (av. x^a-data- 
„eigener Bestimmung unterstehend, iiber sich selbst bestimmend, unver- 
ganglich” ist neuere Zssetzung); gr. e&og n. „Gewohnheit, Sitte” (thema- 
tisch peoov' ed'og Hes., lakonisch, Meillet Msl. 15,264), Ptc. horn. Mo)v 
,,gewohnt”, Pf. eico'&a, lesb. evcod^a „bin gewohnt”, i^lCco „gew6hne”, dehn- 
stufig f]'dog n. ,, Sitte, Gebrauch, Herkommen, pi. Wohnort” (: germ, "^swesa-, 
wenn aus *suedh-s-o-, s. o.), fj^eiog „traut” (e'&vog „Menge, Yolkerschaft” 
hieher als „Sippe”? Persson IP. 2, 201 Anm. 1; nicht nach Pick BB. 28, 
106 als „Bande” zu uedJi- ,,binden“); 

lat. sodalis (^snedhdlis) „Kamerad, Gespiele, Gefahrte, Tisch genosse‘ 
(sehr fraglich dagegen soleo wegen I fiir s. Yf. LEWb.^ s. v.), viel- 
leicht auch suesco „werde gewohnt” (kann aus "^snedh-shd entstanden sein 
und die auBerpraes. Formen stievl^ suHurn, sowie sueo, smre des Lukrez 
nach sich gezogen haben ; doch ist auch "^sue-sko von einem Instr. sue „zu 
eigen” ansetzbar); 

w-los got. sidus „Sitte”, ahd. sitUy ags. sldu, seodu^ anord. sidr (a. pi. 
sidii) m. ,. Sitte” (erst nhd. fern.) (aber auch auf ein "^se-iu-s „Eigenart” 



se-, se^e-, s^e- 


457 


zuruckfiihrbar, Solmsen Unters. 197; verfehlt vereinigt sie Wood Min. 18, 
t3f. mit anord. sidr^ gr. „gerade“, cymr. Jiaeddu „porrigere, assequi“ 
nnter einem „strecken'‘). Curfcius251, Feist PBrB. 1 5, 548 f., Johans- 

son IP. 2, 8. 

^-Ableitungen : av. x'^alAu- „angehorig‘S x^ae-tat- „Angehorigkeit, Zuge- 
horigkeit“ (auf Grund eines Loc. *snei-y suoi -) ; aksl. svah „Verwandter, 
Angehoriger, Brant werber“, svatiti „fur sich oder einen andern werben“, 
svacha „Brautwerberin“ {*siid-to-s oder eher *sna-tos; in ahnlicher Bed. 
Serb, svah „Schwestemiann“, aksl. svojakz „affinis“; lit. svdtas „Hochzeits- 
gast, weitlaufiger Yerwandter“ stammt aus dem Slav., v. d. Osten-Sacken 
IF. 33, 259); lit. svec^ias, svetis „Gast“ (nach Schulze KZ. 40, 417 eigent- 
lich „Frenider‘^ wegen svetimas „fremd^‘, lett. siveschs „fremd“, daher trotz 
apsisvetmti „sich bekannt, vertraut machen^ wohl nicht von einem ^sue-ta 
in der Bed. „Zugeh6rigkeit zu einem selbst, Vertrautheit'^, Brugmann Grdr. 
11^2,416 wesentlich nach Solmsen Unters. 203 abgeleitet, wie gr. €n]g, 
s. u., sondern ^s?ie-^tios „fur sich, allein stehend, daher auBerhaib stehend'‘ 
mit derselben Bedeutungsfarbung wie lett. sewiscJiki „besonders, abge- 
sondert, allein'* und wie gr. exdg, bei Hes. ^syAg^ „fern" aus "^sne-kds^ 
Bildung wie dydgaydg „Mann fiir Mann", ai. vka-i]dh „einzeln“, wo von die 
Zsriickung mit rig eyao-rog, s. Wackernagel KZ. 29, 144f., und die Keu- 
bildung iyA-regog, gort. psxdrsgog „jeder von zweien"), horn, errjg (phrjg) 
„ Angehoriger, Yerwandter, Freund" (s. o.), el. phag „Privatmann". 

Mit Anl. (nicht aksl. '^sct^ „Gast", poseiiti, szsetiti „besuchen" 

(s. Solmsen Unters. 203), gr. kragog „Gefahrte“, fern, "^eraiga, haiga, wozu 
als neues ra. Uraigog (aber gegen Zurlickfiihrung von lat. satelles „be- 
schiitzender Begleiter eines Yornehmen, Trabant" auf ahnliches *sJro-lo-s 
oder "^s/grodos, Walter KZ. 10, 302, Solmsen aaO., s. Yf. LEWb.*^ s. v. — 
Nicht iiberzeugend vermutet Petersson Fran fil. foren. i Lund, Sprakl. upp- 
satser lY 120 in ai. ao. stn „Frau" das fern, Gegenstiick zu £rapoc). 

Andere Zugehorigkeits- und Yerwandtschaftsbezeichnungen (auBer den 
unter eigenen Schlagworten behandelten suesor-, suekuro-s, 

suekrU') sind; 

anord. sveinn „Knablein, Knabe, junger Mann, Knecht", as. swen 
„Schweinehirt" (diese Bed. aus „Angehoriger, Knabe, zunachst der eigenen 
Sippe" durch BedeutungsanschluB an swin „Schwein"), ags. swan „Schweine- 
hirt, Hirt", poet. „Mann, Krieger", lit. svamis „des Weibes Schwester- 
mann", svaine ,,die Schwester der Frau", lett. sivainis „Bruder der Frau"; 
abd. geswTo „Schwager, Schwestermann", rahd. geswie m. f. „Schwager, 
Schwagerin" (auch afris. sla „Nachkommenschaft"?) ; vielleicht anord. sveit,^h 
-ir f. „die einen Hauptling umgebende Kriegerschar" (ags. sveot ds. aus 
*svaiut-^. Pick III ^ 543 f. ; noch viel fraglicher ist, ob ahd. „Rinder- 

herde, deren Weideplatz, Yiehhof" und swaniir „Herde" auf den Begriflf
```


## [2026-09-14T02:06:25.825Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint('pages',len(pages))\nfor w in ['خواهر','خویش','خدا']:\n    idx=[i for i,p in enumerate(pages) if w in p]\n    print(w, idx[:12])\n\""
}
```


### [2026-09-14T02:06:26.920Z] TOOL RESULT

```
pages 545
خواهر [505]
خویش [1, 16, 19, 23, 25, 29, 30, 40, 42, 43, 45, 47]
خدا [11, 14, 24, 30, 34, 35, 37, 43, 48, 49, 53, 54]
```


## [2026-09-14T02:06:29.505Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(pages[505][:1800])\n\""
}
```


### [2026-09-14T02:06:30.702Z] TOOL RESULT

```
[pdf page 506]
لیتوانی (404] هنال 7 ام ند انا پسگشت‌ها انشش برد درد
ایرندی کهن (#لونق ا۵): ۰ ۱۷8 ,71۸5 4 ۶0000
ولزی (7ا 5 (): ‎٩۳1‏ بلغ۸ 0 (۸۳۴115۷۷) مه
بر تونی (/875670): الا ۵ (058) هام02
آلبانی (8۸/]41ظ.اهم): ال 6 (08۸0507) داماد ای
1 و115 لاه
7 (015۳) :0700/5
8 (0:8۳11) +57
133 هلا
برهان قاطع + ۳۱۱۷۸
یادداشت:
چم این واژه در زبان‌های غیر ایرانی در غیر سانسکریت: پسر برادر» پسر خواهر.
| مانگلیس سرواژوی ناش ۳۵8
اوستایی (۸۲887۸): 1۸۸ گونیکه (00777/0): زان
پارسی باستان (۳87۵ ۰:۵۵ 7۸۷۸۰ ایسلندی‌کهن (0۸71۸2/(م صا0۵).
پپلوی (/4۲ات(۸): ۰ ۳0 بقل۸ا۸ ,ات۸« ۸1
کردی (6080157): 13ظ۲۷ ,۸۸33 ,3 ,تزظ ساکسونی کهن (547:00 0ا0): 11017
افغانی (پشتو) (4۳0[72/1)+ ۷۲ ,۲3 فریزی کهن (/فا5ل7۸ صله): 101
تخاری ۸ (۸ 4۸ 70501۸): 1 آلمانی کهن ((/0872 21027 0۵): 7118
تخاری 8 (8 ۸ل/70707۸): 0 آلمانی (65724۸2). ۸0
سانسگریت (54(/862/7): ۷۸۷۸ ,۸8۷۸ انگلیسی کهن (بلدلا8:/0 صا0): ۰ 11088
دا متی (لا(۸۵45): 3 ,ا(1 انگلیسی (8(/01./5): نان
یرنانی 08880): 3002183۹ ,8۸08۸ دانمارکی (/0۸//5): ان
لاتین (7100ها): 01 سوئدی (5177:01577): 0
فرانسه (7ع/۴2: زادنا نر وژی (07/0149/): ۹ ال
اسپانیایی (0ل82۸(713): 0 هلندی (076/7). ندال(
ایتالپایی (7۸4۸۷): 58 ,۴00۷0 اسلاری گهن (10/آها5 تل#6ناتل طا0):
رومانی ((۸4لاتا#): 0 ات ندرا
پرتغالی (۳07870017855): 10۷ لهستانی (۳0(/57): زرد اند (1
```


## [2026-09-14T02:07:35.481Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg447.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/447.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/447.png"
}
```


### [2026-09-14T02:07:35.573Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 69608 Sep 13 22:07 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/447.png
```


## [2026-09-14T02:17:11.662Z] TOOL CALL #78: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-447.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot_sources = [\n    \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/s(w)e-\",\n]\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"hva, hava, xva, xvâothra; xvâjo-ayâo, xvadâya\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The first group is sound: Avestan has the reflexive/possessive stem xʼa- (written hva- in Bartholomae's transcription) 'own, suus', with the ablaut variant hava- and the Old Persian match huva- — Pokorny 883 s.v. se- lists exactly 'Old Indic Poss. sva- \\\"suus\\\", Avestan hva-, xʼa-, ap. huva- \\\"eigen, suus\\\" and zero grade Avestan hava-'. The other three forms are not what the sources know. (a) 'xvâothra' is Av. xʼāθra-, but that word means 'comfort, well-being, ease' (Bartholomae col. 1877; Pahlavi xwārīh) and is hu- 'good' + -āθra-, not a derivative of the reflexive stem; the gloss 'self' is wrong. (b) 'xvâjo-ayâo' is not an attested Avestan word at all: it is Nourai's rendering of the CONJECTURAL compound *xʼatō-āyu- 'living of itself', which Hübschmann (Persische Studien p. 54, no. 471) floats as one way of getting MP xwatāy out of Old Iranian ('skr. svatas + āyu- \\\"von selbst lebend\\\"'); the -j- looks like the book's own misprint for -t-, and the second element is the āyu- of Nourai's root 'Aiw', exactly as his ☞ cross-reference says. (c) 'xvadâya' is likewise unattested; the attested Avestan word is xʼaδāta- 'self-determined, subject to its own ordinance, imperishable' (Walde-Pokorny II 456; Pokorny 883, where it is expressly called 'neuere Zusammensetzung'), and *xʼaδāya- is Horn's reconstruction (Grundriss no. 471, p. 104: 'als Grundform ist etwa aw. *xʼaδōδāta- (oder *xʼaδāya-?) anzusetzen'). I checked the printed page (pdf 447 = book 417): it really does print 'hva, hava, xva, xvâothra' and 'xvâjo-ayâo, xvadâya', so the extraction is faithful and the odd forms belong to the book.\",\n \"derivation_fa\": \"ستاک بازتابی اوستایی xʼa- / hva- «خود، ازآنِ خود» و گونهٔ کوتاه‌واکهٔ hava- و همریشهٔ پارسی باستان huva- درست است و پوکورنی (ص ۸۸۳) همان را می‌آورد؛ امّا سه صورت دیگر درست نیستند. «xvâothra» همان xʼāθra- اوستایی است که به معنی «آسایش، خوشی» (فارسی میانه xwārīh) و از hu- «نیک» است، نه از ریشهٔ بازتابی. «xvâjo-ayâo» واژه‌ای در اوستا نیست، بلکه ترکیبی است فرضی (*xʼatō-āyu- «زنده از خود») که هوبشمان (ص ۵۴) پیشنهاد کرده است؛ پیداست که «j» خطای چاپی کتاب به جای «t» است. صورت درست واژهٔ سوم نیز xʼaδāta- «خوداد، به فرمانِ خود، بی‌مرگ» است و *xʼaδāya- بازسازیِ هرن است. تصویر صفحهٔ چاپی را دیدم: خطا از خودِ کتاب است نه از خوانشِ اسکن.\",\n \"error_in\": \"book\",\n \"book_prints\": \"hva, hava, xva, xvâothra : self ; xvâjo-ayâo, xvadâya : alive from self, self destined, with eternal life\",\n \"correct_form\": \"Av. hva- / xʼa-, hava- (Op. huva-) 'own, self'; xʼaδāta- 'self-determined, imperishable' (not *xvadâya); Hübschmann's conjectural *xʼatō-āyu- 'living of itself' (not *xvâjo-ayâo); xʼāθra- = 'comfort', not 'self'\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\"],\n \"ref_check\": [\n   {\"ref\": \"POK:882\", \"status\": \"supports\", \"note\": \"Pokorny, lemma 'se-' pp. 882-884 (POK_full.txt l.74420): '2. seu̵e-, *su̵e-: Old Indic Poss. sva- \\\"suus\\\", Avestan hva-, xʼa-, ap. huva- \\\"eigen, suus\\\" and zero grade Avestan hava- ds.; Avestan Dat. Abl. hvaβōya ... xʼāi \\\"sibi\\\"'. Covers hva/hava/xva; says nothing about xʼāθra- or the two compounds.\"},\n   {\"ref\": \"BQT:718\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' ed. Mo'in, vol. 2 leaf 178 = printed p. 718 (offset printed = leaf + 540, checked against the running heads ۷۹۳ at leaf 253 and ۷۹۶ at leaf 256). The page carries خدیو / خدو and Mo'in's footnote 'خدیو از ... رک: خدا. «خدیو» خداوند بود' with the Middle Persian antecedent; it documents the Persian words, not the Avestan forms of this node.\"},\n   {\"ref\": \"BRT:1862\", \"status\": \"not_checked\", \"note\": \"Bartholomae's Altiranisches Wörterbuch: the local OCR (BRT.txt, Google scan altiranischeswr00bartgoog, 1041 leaves) breaks off in the xʼa- section at about col. 1853 (leaf 1038, s.v. hv-aspa-), so col. 1862 is not in the file; leaves 1039-1040 are blank.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 456 (lemma se-, seu̵e-, su̵e-, pp. 455-457)\", \"stance\": \"supports\", \"note\": \"'*su̵edh- ... ai. svadhā \\\"Eigenart, Gewohnheit, Sitte\\\" (av. xʼa-data- \\\"eigener Bestimmung unterstehend, über sich selbst bestimmend, unvergänglich\\\" ist neuere Zssetzung)' — the attested Avestan form is xʼaδāta-, and Nourai's gloss 'self destined, with eternal life' matches 'unvergänglich' precisely.\"},\n   {\"src\": \"HUB\", \"where\": \"p. 54 (no. 471), leaf 64 of HUB.txt\", \"stance\": \"partial\", \"note\": \"'Nöldeke bezweifelt die Richtigkeit von Horn's Etymologie: np. xudāi \\\"Gott\\\" = zd. *xʼaδaya- mit vollem Recht ... die sich zur Not durch skr. svatas + āyu- \\\"von selbst lebend\\\" oder skr. svatas + ādi- ... deuten liessen. Doch sind diese Deutungen so unsicher wie die übrigen.' — the source of Nourai's 'alive from self' and of his *xvâ(t)o-ayâo, but Hübschmann treats it as an unproven guess.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 471, p. 104 (leaf 125)\", \"stance\": \"partial\", \"note\": \"'aw. vergl. xʼaδāta-; pahlv. xvatāī ... als Grundform ist etwa aw. *xʼaδōδāta- (oder *xʼaδāya-?) anzusetzen. Nöldeke ... bezweifelt die Richtigkeit der Etymologie vielleicht nicht mit Unrecht.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\",\n \"words\": \"xvat, xveš; Xvatây\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian xwad [BNPSE; hwt'] 'self; indeed', xwēš [NPŠE; hwyš] '(one's) own' and xwadāy [hwt'y] 'lord' are all in MacKenzie, Concise Pahlavi Dictionary p. 93-94. xwad continues Old Iranian *hwatah / Av. xʼatō (adverbial ablative 'of itself') with the regular loss of the final vowel; xwēš continues Old Persian huvāipašiya- = Av. xʼaēpaiθya- 'one's own', with *hwaipaθya- > *xwēθy- > xwēš (the -θy- cluster giving MP š). xwadāy is 'lord, master' in Pahlavi first and 'God' only by extension (it renders Greek δεσπότης in the trilingual inscriptions), so Nourai's gloss 'God' is the later, New Persian value. Its Old Iranian source is the contested point: the older view (Horn) took it from *xʼaδāya-, the modern one from Proto-Iranian *hwatāwHah- 'self-powerful, ruling by itself' (to tav- 'be able'), which explains the -āy directly.\",\n \"derivation_fa\": \"در فارسی میانه xwad «خود»، xwēš «ازآنِ خود» و xwadāy «سرور، خداوند» هر سه در فرهنگ مکنزی (ص ۹۳–۹۴) آمده‌اند. xwad دنبالهٔ xʼatō اوستایی است؛ xwēš از پارسی باستان huvāipašiya- (= اوستایی xʼaēpaiθya-) می‌آید و خوشهٔ -θy- در فارسی میانه به ش بدل شده است. xwadāy در پهلوی نخست «سرور» است و معنیِ «خداوندِ عالم» در فارسی نو بر آن نشسته است. ادعای نورایی درست است، جز آنکه خاستگاهِ ایرانیِ باستانِ xwadāy امروزه *hwatāwHah- «خودتوان، به نیروی خود» دانسته می‌شود.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\", \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"HUB:54\", \"status\": \"partial\", \"note\": \"Hübschmann, Persische Studien p. 54 no. 471 (HUB.txt leaf 64) has exactly this Pahlavi form — 'np. xudāi \\\"Gott\\\" ... xudāi = phl. xʼatāi ... ein zd. *xʼataya- oder auch *xʼatāia- voraussetzt' — but he rejects, with Nöldeke, the Avestan *xʼaδāya- that Nourai's parent node assumes. Footnote: 'Arsāc. phl. *xʼataδ, später phl. xʼatāi, paz. xʼaδāi.'\"},\n   {\"ref\": \"SNS:79\", \"status\": \"supports\", \"note\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast: the volume's own Avestan/Pahlavi index (SNS.txt ll. 29720-30795) gives 'xʼa-/hva-hava- 79/10', 'xʼēš 79/9-267/4', 'xʼēškār 79/22', 'xʼēstar 79/16' — i.e. p. 79 is precisely where xʼa-/hava- and xʼēš are treated, as Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"p. 93-94 s.vv. xwad, xwadāy, xwēš (PHD.txt l. 663-665)\", \"stance\": \"supports\", \"note\": \"\\\"xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. ~ih: selfhood, essence. xwaday [hwt'y | M xwd'y, N ~] lord. ~ih: lordship, sovereignty\\\"; \\\"xwēš [NPŠE < A npš-h; hwyš | M xwy(b)s, N ~] (one's) own\\\"; also xwēš-tan 'self'. Note MacKenzie glosses xwadāy 'lord', not 'God'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.vv. xvatāyēh, xvēš, xvēšāvand\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt l. 4376: 'xʼatayēh domination, dominion, reign ... KZŠPrth hwtwypy, Gr. δεσπο-'; l. 4385 'xvēšāvand belonging to one's own family'; passim xvēš 'own'. The Greek gloss δεσπότης shows 'lord', not 'God'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\",\n \"words\": \"xod «خود ۱»; Xodâ «خدا ، خدای» (+ خدیو ، خواجه (خدایچه))\",\n \"verdict\": \"plausible\",\n \"derivation\": \"خود xod is the straightforward continuation of MP xwad (Mo'in's footnote in Borhan, vol. 2 p. 783 n. 2, labels it 'ضمیر انعکاسی: پهلوی xvat'), with the regular MP xw- > NP xʷ/x-. خدا xodā is MP xwadāy with loss of the final -y and shortening in the unstressed first syllable, the older written form خدای surviving beside it; Horn no. 471 (p. 104) sets out the same chain and notes that 'خداوند' and 'خداوندگار' are built on it. What is only PLAUSIBLE is the gloss: Nourai's '\\\"alive from self\\\"' is Horn's/Hübschmann's 19th-c. conjecture (*xʼaδāya- or svatas+āyu-), already doubted by Nöldeke; the current reconstruction is Proto-Iranian *hwatāwHah- 'self-powerful, self-ruling' (xʼa- + tav- 'be able'), which is why Bactrian has χοαδηο and Sogdian xwt'w. Of the two extra words, خدیو xadīv is indeed the same word (MP/Bactrian χοαδηο 'lord' > NP خدیو), but خواجه < *خدایچه is rejected by modern scholarship: Asatrian (2011, 2012) derives خواجه from Sanskrit upādhyāya- 'teacher' through a Middle Indo-Aryan *vājjhāa taken over in Central Asia. Mo'in prints the خدایچه idea as one of several ('بعضی اصل آن را خواتای‌چه ... دانسته‌اند'), beside Purdāvud's xʼa- + -ča.\",\n \"derivation_fa\": \"«خود» از فارسی میانهٔ xwad است (حاشیهٔ معین بر برهان قاطع، ج۲ ص ۷۸۳: «ضمیر انعکاسی، پهلوی xvat») و «خدا/خدای» از xwadāy پهلوی، با افتادن پایانهٔ -y. امّا معنی‌ای که نورایی می‌دهد («زنده از خود») همان حدسِ هرن و هوبشمان است که نولدکه ردّش کرده؛ ریشه‌شناسی امروزی آن را از ایرانی آغازین *hwatāwHah- «خودتوان، خودسالار» می‌گیرد (قس: بلخی χοαδηο، سغدی xwtʼw). «خدیو» همان واژه است، ولی «خواجه» از «خدایچه» را پژوهش امروزی (آساتریان) رد می‌کند و آن را وام‌واژه‌ای از سنسکریت upādhyāya- «آموزگار» از راه زبان‌های هندی میانه می‌داند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%D8%A7\", \"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D8%AC%D9%87\", \"https://en.wiktionary.org/wiki/%D8%AE%D8%AF%DB%8C%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:779\", \"status\": \"partial\", \"note\": \"Off by a few pages in this printing: with the verified offset (printed = leaf + 540 in BQT_v2_pages.txt) p. 779 = leaf 239 and carries خوار/خوازه/خوارزم, not خود. The words of this node are on the neighbouring pages: خدا at p. 716 (leaf 176), خدیو at p. 718, خواجه at p. 777-778 (leaf 237-238, where Mo'in's footnote gives 'بعضی اصل آن را «خواتای‌چه» از خواتا (خدای) پهلوی + چه (یای تصغیر) دانسته‌اند' — exactly Nourai's 'خواجه (خدایچه)'), and خود at p. 783 (leaf 243, footnote 2 'ضمیر انعکاسی: پهلوی xvat ... قس: پارسی باستان uva-'). So the content is there, the page number is two to four pages out.\"},\n   {\"ref\": \"HRN:104\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 471 = p. 104 (HRN.txt leaf 125): 'xudā, xudāī \\\"Gott\\\"; xudāvand, xudāvandgār ... aw. vergl. xʼaδāta-; phlv. xvatāī; ai. vergl. svadhā \\\"Selbstbestimmung\\\". LW kurd. xudē; afgh. xʼādāi; oss. xucau'. Exactly Nourai's arrow. (خود itself is Horn no. 504, p. 111: 'xud, xēš \\\"selbst\\\"; aw. xʼatō; phlv. xvat, xvatīh; ai. svatas'.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol. 2 p. 777 (leaf 237), Mo'in's footnote on خواجه\", \"stance\": \"partial\", \"note\": \"'آقای پورداود این کلمه را مرکب از xʼa = خود اوستایی + -ča ... دانسته‌اند ... بعضی اصل آن را «خواتای‌چه» از خواتا (خدای) پهلوی + چه دانسته‌اند' — Mo'in reports both as opinions, not as established fact.\"},\n   {\"src\": \"HUB\", \"where\": \"p. 54 no. 471\", \"stance\": \"contradicts\", \"note\": \"Hübschmann endorses Nöldeke's rejection of the Avestan *xʼaδāya- etymology 'mit vollem Recht'; he also dismisses as a 'Curiosum' de Lagarde's idea that German Gott was borrowed from Persian xodā — relevant to the chart's own NOTE 'See \\\"Ghu\\\" for another possible root'.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 93 s.v. xwadāy\", \"stance\": \"partial\", \"note\": \"'xwaday [hwt'y] lord' — supports the Persian descent but not the 'God' gloss at the Pahlavi stage.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\",\n \"words\": \"xwa-tam, xwa-tô; xvaĕ-pati, xvaĕ-paithya\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan xʼatəm (neuter) 'the self, one's own nature' and xʼatō (adverbial ablative) 'of itself, by oneself' are t-extensions of the reflexive stem xʼa-, formally the exact match of Old Indic svatáḥ; Mann's Indo-European Comparative Dictionary p. 1351 sets them under the lemma 'suet-' together with Skt. svatah and Per. xū 'habit', xud 'self'. xʼaē-pati- 'he himself' and xʼaēpaiiθya-/xʼaēpaiθya- 'one's own' are compounds of the locative-based *xʼai- with pati- 'master, self' — Pokorny p. 842 lists 'Avestan xʼae-pati- \\\"er selbst\\\"' inside the lemma potis, which is exactly what Nourai's NOTE and his ☞ Pa cross-reference say. The semantic slide 'one's own' > 'what is proper to one' > 'character, habit' is already Avestan/Old Indic (svadhā 'Eigenart, Gewohnheit').\",\n \"derivation_fa\": \"xʼatəm «خود، ذات» و xʼatō «از خود، به خودیِ خود» ساختهٔ پسوندیِ -t- از ستاک بازتابی xʼa- است و دقیقاً برابرِ svatah سنسکریت است؛ مان (ص ۱۳۵۱) همین دو را زیر ریشهٔ suet- می‌آورد. xʼaē-pati- «خودِ او» و xʼaē-paiθya- «ازآنِ خود» مرکّب‌اند از *xʼai- و pati- «سرور، خود»؛ پوکورنی در ص ۸۴۲ ذیل potis دقیقاً می‌نویسد: «Avestan xʼae-pati- „er selbst“». پس یادداشتِ نورایی دربارهٔ pati/paiθya درست است. تحول معنایی «ازآنِ خود» به «خوی و عادت» از همان دورهٔ هندوایرانی دیده می‌شود (قس: svadhā).\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"POK:842\", \"status\": \"supports\", \"note\": \"Pokorny p. 842, lemma 'potis' (POK_full.txt l. 68696-68740): '... Avestan xʼae-pati- \\\"er selbst\\\" ...' — precisely the element Nourai's NOTE explains.\"},\n   {\"ref\": \"SNS:267\", \"status\": \"supports\", \"note\": \"Tavoosi's Shayast ne Shayast glossary index (SNS.txt l. 29722, 30785): 'xʼaepaiθya- 267/5', 'xʼēš 79/9-267/4', 'xʼēšīh 267/12', 'xʼēstan 267/13' — p. 267 is where xʼaēpaiθya- and its Pahlavi continuation xwēš are dealt with, as cited.\"},\n   {\"ref\": \"IEC:1351\", \"status\": \"supports\", \"note\": \"Mann, IEC p. 1351, lemma 'suet- \\\"alone, apart, by oneself; self; own, private...\\\"' (IEC.txt leaf 744): 'Skt. svatah ...; Av. xwatəm, n. \\\"the self\\\"; xwatō, adv. \\\"of itself\\\"; Per. xū, s. \\\"habit\\\"; cf. (zero-gde) xud, prn. \\\"self\\\"' — word for word Nourai's nodes 4 and 5.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 457 (lemma se-, seu̵e-, su̵e-)\", \"stance\": \"supports\", \"note\": \"'t-Ableitungen: av. xʼaiṭu- \\\"angehörig\\\", xʼae-tat- \\\"Angehörigkeit, Zugehörigkeit\\\" (auf Grund eines Loc. *su̵ei-, su̵oi-)' — the same locative base *xʼai- that underlies xʼaē-paiθya-.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 504, p. 111\", \"stance\": \"supports\", \"note\": \"'xud, xēš (AM.) \\\"selbst\\\". ap. vergl. uva-; aw. xʼatō \\\"selbst\\\"; phlv. xvat, xvatīh; ai. svatas' — Horn's Avestan xʼatō is Nourai's 'xwa-tô'.\"},\n   {\"src\": \"AHD\", \"where\": \"s.v. s(w)e- (AHD_watkins1985.txt l. 1039)\", \"stance\": \"supports\", \"note\": \"'5. Suffixed form *s(u)w-o-, one's own, in ... Sanskrit sva- (< *swo-), one's own'; the t-extension is treated under the same root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"xŭ «خو (بدخو ، خوشخو)»; xîš 1 «خویش ۱»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"خویش xīš/xwēš is certain and uncontroversial: Old Persian huvāipašiya- = Avestan xʼaēpaiθya- 'one's own' > Middle Persian xwēš (the sequence *-paθya- yielding -š, with compensatory ē) > New Persian خویش, colloquially xīš; the compounds خویشتن and خویشاوند continue MP xwēš-tan and xwēšāwand. خو xū 'nature, habit' (بدخو، خوشخو) is the less secure half: Mann (IEC 1351) puts 'Per. xū, s. \\\"habit\\\"' straight under *suet- beside Av. xʼatəm/xʼatō, which is Nourai's arrow, but the Middle Persian antecedent is recorded as xōg (hwk'), which points rather to a *hwa-ka- formation — still inside the same reflexive root, but not through the t-stem. Persian خیم 'disposition' (Horn no. 516) is a different word (Av. *hya-, MP xēm). So the node is right about the root and about خویش, and approximately right about خو.\",\n \"derivation_fa\": \"«خویش» بی‌گفتگو از پارسی باستان huvāipašiya- (اوستایی xʼaēpaiθya-) «ازآنِ خود» می‌آید؛ در فارسی میانه xwēš و در فارسی نو «خویش» (و در گفتار xīš)؛ خوشهٔ -θy- به ش بدل شده و مصوّت کشیده شده است. امّا «خو» (در بدخو، خوشخو) برابر مان (ص۱۳۵۱) همان دنبالهٔ xʼatō/xʼatəm است، ولی صورت فارسی میانهٔ آن xōg ثبت شده که به ساختِ *hwa-ka- اشاره دارد؛ پس ریشه یکی است ولی راهِ میانی شاید یکی نباشد. به هر روی «خیم» واژه‌ای دیگر است (هرن، شمارهٔ ۵۱۶). ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%DB%8C%D8%B4\", \"https://en.wiktionary.org/wiki/%D8%AE%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:1351\", \"status\": \"supports\", \"note\": \"Mann p. 1351 s.v. suet-: '... Per. xū, s. \\\"habit\\\"; cf. (zero-gde) xud, prn. \\\"self\\\"' — Mann explicitly places Persian xū under this stem, which is the only reference of the three that actually asserts Nourai's arrow for خو.\"},\n   {\"ref\": \"SNS:267\", \"status\": \"supports\", \"note\": \"SNS index: 'xʼēš 79/9-267/4', 'xʼēšīh 267/12' beside 'xʼaepaiθya- 267/5' — p. 267 documents the xʼaēpaiθya- > xwēš link for خویش.\"},\n   {\"ref\": \"POK:842\", \"status\": \"partial\", \"note\": \"Pokorny p. 842 (lemma potis) gives Av. xʼae-pati- but no New Persian reflex; it supports the parent node, not the Persian words themselves.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 504, p. 111\", \"stance\": \"supports\", \"note\": \"'xud, xēš \\\"selbst\\\" ... phlv. xvat, xvatīh; ai. svatas; kurd. xō; oss. xwædæg' — Horn groups خود and خویش under the same reflexive stem.\"},\n   {\"src\": \"PHD\", \"where\": \"p. 94 s.v. xwēš\", \"stance\": \"supports\", \"note\": \"'xwēš [NPŠE; hwyš | M xwy(b)s, N ~] (one's) own. ~ih: possession. ~awand: relative, kinsman. xwēš-tan: self'. MacKenzie has no xōg 'habit' (his 'character, disposition' word is xēm, dušxēm).\"},\n   {\"src\": \"HRN\", \"where\": \"no. 516, p. 114-115\", \"stance\": \"partial\", \"note\": \"'xīm \\\"Naturanlage, Charakter\\\"; aw. vergl. haya-, haēm; phlv. xēm, huxīm, dušxīm' — shows that the Persian 'character' word Horn recognises is خیم, from a different stem, so خو has to be argued separately.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node for Proto-Germanic. The reflexive root shows up in Germanic as *selbaz 'self' (< suffixed *sel-bho-), *sibja- 'kin, one's own' (< *s(w)e-bh(o)-), *sik 'oneself' (< *se-ge), *swa 'so' (< *swo-) and *swainaz 'attendant, one's own man' — all set out in AHD s.v. s(w)e-, items 1-4, and in Klein s.v. sib.\",\n \"derivation_fa\": \"گرهٔ واسطه برای ژرمنیِ آغازین. ریشهٔ بازتابی در ژرمنی به صورت *selbaz «خود»، *sibja- «خویشاوند»، *sik «خود را»، *swa «چنین» و *swainaz دیده می‌شود؛ واتکینز (پیوست ریشه‌های هندواروپایی) و کلاین هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l. 1039 s.v. s(w)e-: '1. Suffixed extended form *sel-bho- in Germanic *selbaz ... 2. Suffixed form *s(w)e-bh(o)- in Germanic *sibja- ... 3. Suffixed form *se-ge in Germanic *sik ... 4. Suffixed form *swoi-no- in Germanic *swainaz'.\"},\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein s.v. 'sib' (KLN_1966.txt l. 35110): 'OE. sibb, rel. to OS. sibbia, ... Goth. sibja, \\\"kin, kindred\\\" ... All these words derive fr. I.-E. base *s(w)e-bh-, \\\"of the same kind\\\", which is a -bh-enlargement of the reflexive pron. base *se-, \\\"self\\\".'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 882-884 s.v. se-\", \"stance\": \"supports\", \"note\": \"Items 3, 7, 8: 'Gothic sibja, Old High German sippa ... Germanic *selba- \\\"selbst\\\", Gothic silba ... Gothic swe \\\"as\\\", swa-swe, Gothic swa, Old English swā'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 455-458\", \"stance\": \"supports\", \"note\": \"Same material in the parent work of Pokorny's entry (WP. II 455 ff.).\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"English\",\n \"words\": \"so, such, also, self, sibling\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are Germanic inheritances of *swe-. 'so' is OE swā < Gmc *swa < PIE *swo-, a pronominal stem AHD explicitly derives from s(w)e-; 'such' is OE swylc < Gmc *swa-lik- 'so-like'; 'also' is OE eall swā 'all so', i.e. the same *swo- with 'all' prefixed; 'self' is OE self/sylf < Gmc *selbaz < *sel-bho-; 'sibling' is OE sibling 'kinsman' from sibb 'kinship' < Gmc *sibja- < *s(w)e-bh(o)-, revived in its modern sense by geneticists in 1903. Klein, Skeat and Watkins all place them here.\",\n \"derivation_fa\": \"هر پنج واژه میراثِ ژرمنیِ همین ریشه‌اند: so از swāی انگلیسی کهن (< *swo-)، such از swylc = «چنین‌مانند»، also از eall swā «همه چنین»، self از *selbaz و sibling از sibb «خویشاوندی» (< *s(w)e-bh(o)-) که در ۱۹۰۳ زیست‌شناسان آن را دوباره زنده کردند. کلاین، اسکیت و واتکینز همه همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index (AHD_watkins1985.txt ll. 2239, 2254, 2273): 'SELF s(w)e-', 'SIB s(w)e-', 'SO swo-', 'SUCH lik-/swo-'; and s.v. swo-: 'Derivative of s(w)e-. 1. Germanic *swa- in: a. Old English swā, so: SO; b. Germanic compound *swa-lik-, \\\"so like\\\" ... Old English swylc, such: SUCH.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. sib, self, so, such\", \"stance\": \"supports\", \"note\": \"s.v. sib: 'derive fr. I.-E. base *s(w)e-bh-, \\\"of the same kind\\\", ... enlargement of the reflexive pron. base *se-, \\\"self\\\". See sui and cp. gossip.'\"},\n   {\"src\": \"POK\", \"where\": \"pp. 883-884 s.v. se-, items 3, 7, 8\", \"stance\": \"supports\", \"note\": \"'Gothic swa, Old Norse svá, Old English swā, swæ \\\"so\\\"; in addition Gothic swa-leiks, ... Old English swelc, swilc, Old High German solīh \\\"solch\\\"'; and 'Germanic *selba- \\\"selbst\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node for Latin. The root gives Latin suus 'his/her/its own' (< *sowos < *swo-), the genitive suī 'of oneself', the preposition/prefix sēd, sē 'apart, without' (an extended *sed), sōlus 'alone' (possibly *swē-lo-), and suēscere 'to grow accustomed' from the extended root *swēdh- 'that which is one's own'.\",\n \"derivation_fa\": \"گرهٔ واسطه برای لاتین. از همین ریشه در لاتین suus «ازآنِ خود»، suī، پیشوند sē-/sēd «جدا، بی‌»، sōlus «تنها» و suēscere «خو گرفتن» (از گسترشِ *swēdh-) پدید آمده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. s(w)e-: '5a. Latin suī (genitive), of oneself: SUICIDE; 6. Extended form *sed in: a. Latin sēd, sē, self ...; b. Latin sēd, sē, without, apart (< \\\"on one's own\\\") ...; 7. Possibly suffixed lengthened o-grade form *sō-lo- in Latin sōlus, by oneself alone; 8. Extended root *swēdh- ... b. Latin suēscere, to get accustomed.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp. 883-884 s.v. se-\", \"stance\": \"supports\", \"note\": \"'Old Latin sovos, from which ... suos, Latin suus ...; Latin sēd, sē preposition \\\"without\\\", prefix \\\"beiseite\\\" ... Latin sodālis (*suēdhālis) \\\"buddy, friend\\\" ... suesco \\\"werde accustomed\\\" (*suēdh-skō)'.\"},\n   {\"src\": \"LEW\", \"where\": \"Walde, Lat. etym. Wörterbuch s.vv. suus, sēd, sōlus\", \"stance\": \"supports\", \"note\": \"Same derivation; Walde is Pokorny's cited authority (WH. II 457 f., 506 f., 530 f., 552 f., 557, 626 f.).\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"English\",\n \"words\": \"solo, sole, secret, secure, separate, seduce,; select, sure, custom, suicide, segregate\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every one of these reaches English through Latin from *s(w)e-. solo (It. solo) and sole (OF sol < L. sōlus) are the 'alone' word; secret (sē-cernēre), secure (sē-cūra 'without care', whence also sure through Old French seûr), separate (sē-parāre), seduce (sē-dūcere 'lead apart'), select (sē-legere) and segregate (sē-gregāre 'set apart from the flock') all contain the separative prefix sē-/sēd 'apart, on one's own'; suicide is suī 'of oneself' + -cīdium; custom is OF costume < L. consuētūdinem, from consuēscere, to *swēdh- 'to make one's own'. AHD lists each of them under s(w)e- in its index, and Klein spells out the same chains.\",\n \"derivation_fa\": \"همهٔ این واژه‌ها از راه لاتین به انگلیسی رسیده‌اند: solo/sole از sōlus؛ secret، secure، separate، seduce، select و segregate همه پیشوندِ جداسازِ sē-/sēd «جدا، به خود» دارند؛ sure همان securus است که از راه فرانسهٔ کهن seûr آمده؛ suicide از suī + -cīdium «خودکشی»؛ و custom از consuētūdinem از ستاکِ *swēdh- «آنچه ازآنِ خود کنی». ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; it inherits AHD from its Latin parent. Checked against AHD and Klein anyway (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"index entries, AHD_watkins1985.txt ll. 2230, 2236, 2239, 2244, 2276, 2325, 1406\", \"stance\": \"supports\", \"note\": \"'SECRET krei-, s(w)e-', 'SECURE cūra, s(w)e-', 'SEDUCE deuk-, s(w)e-', 'SEGREGATE ger-, s(w)e-', 'SELECT leg-, s(w)e-', 'SEPARATE perə-, s(w)e-', 'SOLE² s(w)e-', 'SOLO s(w)e-', 'SUICIDE s(w)e-', 'CUSTOM s(w)e-'; 'SURE' appears in the s(w)e- entry itself under 6b.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. custom, sole, sure, suicide (KLN_1966.txt ll. 10016, 35845, 37572, 37400)\", \"stance\": \"supports\", \"note\": \"s.v. custom: 'fr. L. consuētūdinem ... fr. I.-E. base *swedh-, whence also Gk. ἔθος, ἦθος ... Base *swedh- is compounded of *swe-, \\\"his, her, its, one's own\\\", and *dhe-'; s.v. sole: 'fr. L. sōlus ... possibly stands for *swō-lo-s, and lit. means \\\"being by himself\\\", fr. I.-E. base *swe-'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. secret, secure, sure\", \"stance\": \"supports\", \"note\": \"Skeat derives all the se-/sed- compounds from Latin sed, se 'apart', the same particle.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node for Greek. From the extended root *swedh- 'one's own way' Greek has ἔθος 'custom, disposition' and ἦθος 'custom, haunt', from *swet- ἑταῖρος 'companion', and from *swed-yo- ἴδιος 'private, one's own'; ἔθνος 'band of people living together, nation' is taken by Watkins and Klein as *swedh-no- 'people of one's own kind'.\",\n \"derivation_fa\": \"گرهٔ واسطه برای یونانی. از گسترشِ *swedh- در یونانی «ἔθος» «خوی، عادت» و «ἦθος»، از *swet- «ἑταῖρος» «یار» و از *swed-yo- «ἴδιος» «شخصی» پدید آمده است؛ «ἔθνος» نیز به گمانِ واتکینز و کلاین *swedh-no- «مردمانِ خودی» است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/ethnic\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. s(w)e-, item 8: 'Extended root *swēdh-, \\\"that which is one's own\\\", peculiarity, custom, in: ... c. Greek ēthos, custom, disposition, trait: ETHIC, ETHOS; CACOETHES; d. suffixed form *swedh-no- in Greek ethnos, band of people living together, nation, people (< \\\"people of one's own kind\\\"): ETHNIC, ETHNO-.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 883 s.v. se-, item 4\", \"stance\": \"supports\", \"note\": \"'4. suēdh-: Old Indic svadhā ... gr. ἔθος n. \\\"consuetude, custom\\\" ... lengthened grade ἦθος n. \\\"custom, Gebrauch, Herkommen\\\" ... ἔθνος \\\"bulk, mass, Volkerschaft\\\" as \\\"family\\\"?' — Pokorny already marks ἔθνος with a query.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 456\", \"stance\": \"partial\", \"note\": \"'(ἔθνος \\\"Menge, Völkerschaft\\\" hieher als \\\"Sippe\\\"? Persson IF. 2, 201 Anm. 1)' — the connection of ἔθνος is attributed, with a question mark, to Persson; modern Greek etymologists (Beekes) call it uncertain.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"English\",\n \"words\": \"ethics, ethnic\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"ethic(s) is Latin ethica < Greek ἠθική (τέχνη) from ἦθος 'moral character, custom', via Old French éthique into Middle English (14th c.). ethnic is Late Latin ethnicus 'heathen' < Greek ἐθνικός from ἔθνος; its early English sense (15th c.) was 'gentile, heathen', from the Septuagint/Vulgate use of ἔθνη for the non-Jewish nations, and only in the 19th c. did it become 'pertaining to a race or people'. Both go back to *swedh- via Greek; the one caveat is that the connection of ἔθνος with ἔθος is probable rather than certain (Pokorny and Walde-Pokorny both add a question mark, Beekes leaves it open).\",\n \"derivation_fa\": \"ethic از لاتین ethica و آن از یونانی ἠθική (از ἦθος «خوی، منش») است و در سدهٔ ۱۴م میلادی از راه فرانسه وارد انگلیسی شده؛ ethnic از ἐθνικός از ἔθνος «قوم» است که نخست به معنی «غیری، کافر» به کار می‌رفت (به پیروی از کاربردِ ἔθνη در سبعینیه و وولگاتا) و معنی «قومی» از سدهٔ ۱۹م رواج یافته است. هر دو به *swedh- بازمی‌گردند؛ تنها نکته آنکه پیوندِ ἔθνος با ἔθος احتمالی است نه قطعی.\",\n \"sources\": [\"https://www.etymonline.com/word/ethnic\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index l. 1477: 'ETHIC s(w)e-', 'ETHNIC s(w)e-', 'ETHNO- s(w)e-', 'ETHOS s(w)e-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. ethnic (KLN_1966.txt l. 13738)\", \"stance\": \"supports\", \"note\": \"'L. ethnicus, fr. Gk. ἐθνικός, fr. ἔθνος \\\"nation, race\\\" (in Eccles. Greek the plural ἔθνη means \\\"the heathens, gentiles\\\"). Gk. ἔθνος prob. stands for *sweđhnos and orig. meant \\\"one's own\\\". It is rel. to ἔθος ... \\\"custom, usage\\\".'\"},\n   {\"src\": \"POK\", \"where\": \"p. 883 item 4\", \"stance\": \"partial\", \"note\": \"Pokorny writes 'ἔθνος ... as \\\"family\\\"?' — a query, so the ethnic half is 'probable', not certain.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Indo-European\",\n \"words\": \"Swe-sor\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"PIE *swésōr 'sister' (Pokorny 1051) is transparently *s(w)e- 'one's own' + *-sor 'woman', the feminine element that also appears in the archaic numerals Skt. ti-sráḥ 'three (fem.)', cátasraḥ 'four (fem.)', in Old Irish tḗoir, and in Latin uxor 'wife' (*uk-sor-). Avestan hairišī- 'female' is generally taken as the free-standing reflex of that *-sor-. So the literal sense 'one's own female (of the kin group)' that Nourai gives is exactly the standard analysis, and it is what Buck, Pokorny, Walde-Pokorny, Klein and Watkins all print.\",\n \"derivation_fa\": \"صورت بازساختهٔ *swésōr «خواهر» (پوکورنی ص ۱۰۵۱) از *s(w)e- «ازآنِ خود» و *-sor «زن» ساخته شده است؛ همان *-sor در شمارهٔ مؤنّثِ سنسکریت ti-sráḥ «سه» و در لاتین uxor «همسر» دیده می‌شود، و اوستایی hairišī- «ماده، زن» را بازتابِ مستقلِ آن می‌دانند. پس معنی‌ای که نورایی می‌دهد («مادهٔ خودی») همان تحلیلِ معیار است؛ ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SYN 85\", \"status\": \"supports\", \"note\": \"Buck p. 85 (§2.24 'Female'): 'Av. hairiši- noun for \\\"female\\\", applied to human beings and animals, perh. *har- : second part of IE *swe-sor- \\\"sister\\\" (2.45). Benveniste, BSL 35.1.104 f.'\"},\n   {\"ref\": \"SYN 108\", \"status\": \"supports\", \"note\": \"Buck §2.45 'Sister' (p. 108; SYN.txt l. 2918): '1. IE *swesor-, prob. *swe-sor-, cpd. of the refl. *swe-, the second part related to the rare Grk. ἔορ \\\"wife\\\", Av. hairiši- \\\"female\\\", Lat. uxor \\\"wife\\\" (2.32), and the fem. numeral forms like Skt. tisras \\\"three\\\". Walde-P. 2.583 f.' — word for word Nourai's 'Swe-sor: one's own female'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 1051 s.v. su̵esor-\", \"stance\": \"supports\", \"note\": \"'Indo Germanic *s(u̵)e-sor- to Reflexivstamme se-, seu̵e-; to ending compare fem. Old Indic ti-srah \\\"drei\\\", Old Irish teoir (*tri-sores); contains perhaps yet *sor \\\"wife, woman\\\"? Or from *su-esor \\\"of own blood, relative\\\"?'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 533-534 s.v. su̵esor-\", \"stance\": \"supports\", \"note\": \"'Idg. *s(u̵)e-sor- zum Reflexivstamme se-, und im Ausgang wie fem. ai. ti-sraḥ \\\"drei\\\" vermutlich zu Wz. ser- \\\"aneinander reihen\\\".'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 1350 s.v. suesór\", \"stance\": \"supports\", \"note\": \"'suesór, suesor \\\"sister\\\". Cf. sue- and extns., sər- and suesrios ... Av. xwáha, acc: xwáharom, id.; Per. xàhar, id.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Avestan\",\n \"words\": \"xvan-har\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan xʼaŋhar- 'sister' (nom. sg. xʼaha, acc. xʼahārəm) is the regular Iranian outcome of *swesōr: PIE *s- before a vowel becomes Iranian h-, the *-w- is written with the raised v of xʼ-, and intervocalic *-s- becomes -h- (with the nasal of the -ŋh- spelling), so *swesōr > Proto-Iranian *hwahar- > Av. xʼaŋhar-. Nourai's transliteration 'xvan-har' is his way of writing the ŋh digraph; the form and meaning are correct.\",\n \"derivation_fa\": \"اوستایی xʼaŋhar- «خواهر» (نهادی xʼaha، رایی xʼahārəm) دنبالهٔ منظمِ *swesōr است: s آغازینِ هندواروپایی در ایرانی به h بدل می‌شود، -w- در نوشتار با xʼ نمایانده می‌شود و s میان‌واکه‌ای نیز h می‌گردد؛ پس *swesōr > *hwahar- > xʼaŋhar-. آوانویسیِ «xvan-har» در کتاب همان دونگارهٔ ŋh است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The chart gives no reference for this node; verified against Pokorny, Walde-Pokorny, Buck, Klein and Horn (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 1051 s.v. su̵esor-\", \"stance\": \"supports\", \"note\": \"'Old Indic svasar-, Avestan xʼaŋhar- \\\"sister\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 533\", \"stance\": \"supports\", \"note\": \"'Ai. svasar-, av. xʼaŋhar- \\\"Schwester\\\"; arm. kʼoir ds.'\"},\n   {\"src\": \"SYN\", \"where\": \"§2.45, p. 107 table\", \"stance\": \"supports\", \"note\": \"Buck's comparative table prints 'Av. xʼaŋhar-' opposite Skt. svasar-, Lat. soror, Goth. swistar.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"Persian\",\n \"words\": \"xâhar «خواهر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian خواهر xāhar continues Middle Persian xwāhar [hw'hl] 'sister' (MacKenzie p. 93), itself from Old Iranian *hwáhar- / *hwahār- (the Avestan xʼaŋhar- of the parent node); intervocalic -h- is kept in the written language while the -ʼ- of xw- survives only in the spelling خوا-, giving modern xāhar. Manichaean Middle Persian has xwār, and the modern dialects show the same word (Kurdish xwāšk, Balochi gwahar, Ossetic xwæræ). Horn no. 501 (p. 111) prints exactly this chain. Nourai's gloss '\\\"one's own female relative\\\"' is the etymological, not the current, sense — which is the point of the box.\",\n \"derivation_fa\": \"«خواهر» از فارسی میانهٔ xwāhar (مانوی: xwār) و آن از ایرانی باستان *hwahar- (اوستایی xʼaŋhar-) است؛ هرن (شمارهٔ ۵۰۱، ص ۱۱۱) همین زنجیره را می‌آورد و همریشه‌های کردی xwāšk، بلوچی gwahar و اسی xwæræ را برمی‌شمارد. معنی‌ای که نورایی می‌دهد («خویشاوندِ مادهٔ خودی») معنیِ ریشه‌شناختی است نه معنیِ امروزی. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%88%D8%A7%D9%87%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given on the node; checked against Horn, MacKenzie and Mann (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"no. 501, p. 111 (HRN.txt leaf 132)\", \"stance\": \"supports\", \"note\": \"'xʼāhar \\\"Schwester\\\", xʼāh. aw. xʼaŋhar- \\\"Schwester\\\"; phlv. xʼāhar, xʼāk (PPGl.); ai. svasar-; arm. kʼoir. kurd. xʼōh, xʼāšk; afg. xʼor; oss. d. xʼore, i. xʼo; bal. gvahār, gvāhar.'\"},\n   {\"src\": \"PHD\", \"where\": \"p. 93 s.v. xwāhar (PHD.txt l. 663)\", \"stance\": \"supports\", \"note\": \"'xwahar [AHTEl, v. xwah; hw'hl | (M xw'r), N xwāhar] sister'; also 'xwah [AHTE < A ʾhšh | N ~] sister'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 1350\", \"stance\": \"supports\", \"note\": \"'Per. xàhar, id.' listed among the reflexes of suesór.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"Germanic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node for Proto-Germanic *swestr- < *swesr-, with the well-known epenthetic -t- that Germanic inserts between s and r (Gothic swistar, ON systir, OHG swester, OE sweostor). Walde-Pokorny notes that the -t- had not yet appeared in the older derivatives (OS swiri, OE geswiria 'sister's son'), which shows the insertion is Germanic-internal.\",\n \"derivation_fa\": \"گرهٔ واسطه برای ژرمنیِ آغازین *swestr- از *swesr-؛ در ژرمنی میانِ s و r واجِ میانجی t افزوده می‌شود (گوتی swistar، نورسی کهن systir، آلمانی کهن swester، انگلیسی کهن sweostor). والده–پوکورنی می‌نویسد که این t در مشتقّاتِ کهن‌تر هنوز نیست؛ پس پدیده‌ای درون‌ژرمنی است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. swesōr- (l. 155): 'The female counterpart was swesor- (SISTER), probably literally \\\"the female member of the kin group\\\", with a feminine suffix *-sor- and the root s(w)e-, designating the self, one's own group.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 533-534\", \"stance\": \"supports\", \"note\": \"'got. swistar (g. d. swistrs, swistr; hier vollzog sich der t-Einschub), anord. syster ... ahd. swester, ags. sweostor, suster. Noch vor dem t-Einschub neugeschaffen sind as. swiri \\\"Sohn der Mutterschwester\\\", ags. geswīria \\\"Schwestersohn\\\".'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. sister\", \"stance\": \"supports\", \"note\": \"'OE. sweostor, swustor, OS. swestar, OFris. swester, suster, MDu. suster, Du. zuster, OHG., MHG. swester, G. Schwester, Goth. swistar, from I.-E. base *swesōr'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"English\",\n \"words\": \"sister\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern English sister is Middle English sister, taken from Old Norse systir (Danelaw contact, 12th-13th c.), which displaced the native Old English sweostor/swuster; the s-form won out precisely because the Norse word was closer to the northern English forms. Ultimately Gmc *swestr- < PIE *swésōr. Klein: 'ME. sister, of Scand. origin; cp. ON. systir'.\",\n \"derivation_fa\": \"sister انگلیسی از انگلیسی میانه sister است که وام‌واژه‌ای است از نورسیِ کهن systir (از راه تماس با وایکینگ‌ها در سدهٔ ۱۲–۱۳ میلادی) و جایِ sweostor انگلیسی کهن را گرفته است؛ سرانجام از *swesōr هندواروپایی. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; checked against Klein and AHD (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. sister (KLN_1966.txt l. 35365)\", \"stance\": \"supports\", \"note\": \"'ME. sister, of Scand. origin; cp. ON. systir, Swed. syster, Dan. søster, which are rel. to OE. sweostor ... I.-E. *swesor is compounded of the reflexive base *swe-, \\\"his, one's own\\\" (see sui) and -sor, \\\"woman\\\" ... Accordingly sister orig. meant \\\"the woman belonging to one's own kindred\\\".'\"},\n   {\"src\": \"AHD\", \"where\": \"s.v. swesōr-\", \"stance\": \"supports\", \"note\": \"'swesor- (SISTER), probably literally \\\"the female member of the kin group\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Latin\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through node for Latin soror 'sister' < *swesōr with the regular Latin rhotacism of intervocalic -s- (*swesor > *sozor > soror) and *sw- > s-. Its derivative sōbrīnus 'cousin on the mother's side' stands for *swesr-īnos, matching Old Church Slavonic sestrinŭ.\",\n \"derivation_fa\": \"گرهٔ واسطه برای لاتین soror «خواهر» از *swesōr؛ s میان‌واکه‌ای در لاتین به r بدل می‌شود (روتاسیسم) و *sw- به s-. مشتقِّ آن sōbrīnus «پسرخاله/دخترخاله» از *swesr-īnos است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; checked against Pokorny, Walde-Pokorny and Klein (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 1051\", \"stance\": \"supports\", \"note\": \"'Latin soror \\\"a sister\\\" (in addition sobrīnus \\\"a cousin by the mother's side, mother's sister's child\\\", from *swesr-īnos = Old Church Slavic sestrinŭ \\\"belonging to sister\\\")'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 533\", \"stance\": \"supports\", \"note\": \"'lat. soror (dazu sobrinus ... aus *su̵esr-īnos, ~ aksl. sestrinŭ \\\"der Schwester gehörig\\\")'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\",\n \"words\": \"sorority, cousin\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"sorority is Medieval Latin sorōritās 'sisterhood', from soror, adopted in English in 1530s and applied to American college women's societies from 1887. cousin is Old French cosin/cousin from Latin consōbrīnus 'mother's sister's child', con- + sōbrīnus < *swesr-īnos 'of the sister', so it too rests on *swe-sor-; Middle English borrowed it in the 13th c. already widened to 'any collateral relative'. Klein spells out both.\",\n \"derivation_fa\": \"sorority از لاتینِ میانه sorōritās «خواهری» (از soror) است که در سدهٔ ۱۶م وارد انگلیسی شد و از ۱۸۸۷ برای انجمن‌های دانشجویی به کار رفت؛ cousin از فرانسهٔ کهن cosin از لاتین consōbrīnus (con- + sōbrīnus < *swesr-īnos) «فرزندِ خاله» است، پس آن نیز بر *swe-sor- استوار است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; checked against Klein (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. cousin, sorority (KLN_1966.txt ll. 9463, 35972)\", \"stance\": \"supports\", \"note\": \"s.v. cousin: 'F. cousin ... fr. L. consōbrīnus, \\\"cousin-german\\\", orig. denoting only \\\"the child of a mother's sister\\\", fr. con- and sobrīnus ... contraction of sorōrīnus, from soror, \\\"sister\\\" ... See sister and cp. cozen.' s.v. sorority: 'ML. sorōritās, \\\"sisterhood\\\", fr. L. soror ... See sister and -ity.'\"},\n   {\"src\": \"SYN\", \"where\": \"§2.55 'Cousin', p. 119 f.\", \"stance\": \"supports\", \"note\": \"Buck treats Lat. consōbrīnus / sobrīnus under 'cousin' as a derivative of soror.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Seu 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *s(w)e- / *swé (also written *seu̵e-, *su̵e-) 'self, one's own; reflexive pronoun'\",\n \"note\": \"Pokorny's lemma is headed 'se-' (pp. 882-884) with the note 'und (nach Analogie von *t(e)u̵e) s(e)u̵e-', and section 2 of that lemma is 'seu̵e-, *su̵e-' — exactly Nourai's 'Seu 1'. Watkins prints it as s(w)e- 'Pronoun of the third person and reflexive ... further appearing in various forms referring to the social group as an entity, \\\"(we our-)selves\\\"'. Language label ('Indo-European') and gloss ('one's own self') are both right. The chart's page-level NOTE on the Persian box, 'See \\\"Ghu\\\" for another possible root', concerns the English word God (PIE *ǵʰau- 'to call, invoke'), not خدا: the old idea (de Lagarde, after Burnouf) that German Gott was borrowed from Persian xodā is dismissed by Hübschmann (p. 54) as a 'Curiosum', and modern scholarship keeps the two words entirely apart. One page-level caveat about the references: Nourai's BQT page numbers for the Persian box are two to four pages out in Mo'in's edition (see node 3), and BRT:1862 could not be checked because the local Bartholomae OCR stops short of that column.\",\n \"note_fa\": \"ریشهٔ هندواروپاییِ آغازین *s(w)e- / *swé «خود، ازآنِ خود» (ضمیر بازتابی) را پوکورنی در صفحات ۸۸۲–۸۸۴ ذیل se- آورده و بخش دومِ همان مادّه «seu̵e-، su̵e-» است؛ پس عنوان، زبان و معنایی که نورایی می‌دهد هر سه درست است. واتکینز نیز همین را s(w)e- می‌نویسد. یادداشتِ خودِ نمودار («به ریشهٔ Ghu نگاه کنید») به واژهٔ انگلیسی God بازمی‌گردد نه به «خدا»؛ پنداشتِ کهنِ دولاگارد که Gott آلمانی را وام‌گرفته از «خدا»ی فارسی می‌دانست، هوبشمان (ص ۵۴) آن را «طرفه» خوانده و پژوهش امروزی آن دو را یکسره جدا می‌داند. در این صفحه دو کاستی هست: شمارهٔ صفحاتِ برهان قاطع دو تا چهار صفحه لغزش دارد، و صورت‌های اوستاییِ جعبهٔ نخست درست نیستند (نگاه کنید به گرهٔ ۱).\",\n \"sources\": root_sources,\n \"ref_check\": [\n   {\"ref\": \"POK:882\", \"status\": \"supports\", \"note\": \"Pokorny IEW pp. 882-884, 'Root / lemma: se-. Meaning: reflexive pronoun. Note: und (nach Analogie von *t(e)u̵e) s(e)u̵e-' with section '2. seu̵e-, *su̵e-'. Page 882 is the first page of the lemma, exactly as cited (POK_full.txt ll. 74403-74477).\"},\n   {\"ref\": \"AHD:1538\", \"status\": \"supports\", \"note\": \"The 1975 New College Edition's IE appendix runs pp. 1505-1550 and is alphabetical, so s(w)e- falls in the 1530s. The same entry in the standalone Watkins 1985 (AHD_watkins1985.txt l. 1039) reads: 's(w)e-. Pronoun of the third person and reflexive (referring back to the subject of the sentence); further appearing in various forms referring to the social group as an entity, \\\"(we our-)selves\\\".' [Pok. se- 882.]\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 455-458, lemma 'se-, seu̵e-, su̵e-'\", \"stance\": \"supports\", \"note\": \"Pokorny's source (WP. II 455 ff.); contains the Avestan, Greek, Latin and Germanic material of the whole chart, including the *su̵edh- and t-extensions.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt l. 1039 s.v. s(w)e-; l. 1057 s.v. swo-\", \"stance\": \"supports\", \"note\": \"Lists SELF, SIB, SO, SUCH, SOLE², SOLO, SECRET, SECURE, SEPARATE, SEDUCE, SELECT, SEGREGATE, SURE, CUSTOM, SUICIDE, ETHIC, ETHNIC under this root — i.e. every English word on this page except the sister group, which is under swesōr-.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann pp. 1349-1351, lemmas suesios, suesór, suet-, suesue\", \"stance\": \"supports\", \"note\": \"Mann's family of 'sue-' lemmas covers the Iranian and Persian reflexes explicitly (Per. xwiš, xū, xud, xàhar).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §2.45 p. 108 and §2.24 p. 85\", \"stance\": \"supports\", \"note\": \"'IE *swesor-, prob. *swe-sor-, cpd. of the refl. *swe-'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. sui, sib, sister, custom, ethnic\", \"stance\": \"supports\", \"note\": \"Klein routes all the English reflexes back to 'the reflexive pron. base *se-/*swe-, \\\"self\\\"'.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 447,\n \"book_page\": 417,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-447.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-447.py"
}
```


### [2026-09-14T02:17:13.024Z] TOOL RESULT

```
ok 18
```


## [2026-09-14T02:17:17.760Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-447.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 447"
}
```


### [2026-09-14T02:17:19.017Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'transcription_suspect': 1, 'confirmed': 15, 'plausible': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 4, 'not_checked': 7}
books consulted: {'supports': 36, 'partial': 7, 'contradicts': 1} | by book: {'WLD': 8, 'POK': 8, 'KLN': 6, 'HRN': 5, 'PHD': 4, 'AHD': 3, 'HUB': 2, 'IEC': 2, 'SYN': 2, 'NYB': 1, 'BQT': 1, 'LEW': 1, 'SKT': 1}
```


## [2026-09-14T02:17:39.071Z] AGENT

Verification of PDF page 447 (book p. 417) complete — `/home/sfmqrb/git/rishe/data/verification/page-447.json`, `verify_check.py 447` shows 0 PROBLEM lines.

**Counts (1 entry, root Seu 1 = PIE \*s(w)e- "one's own self")**
- Root: confirmed (POK 882–884 `se-`/`seu̯e-`; Watkins `s(w)e-`)
- Nodes 18/18: confirmed 15, plausible 2, transcription_suspect 1
- ref checks: supports 17, partial 4, not_checked 7; books consulted: 44 entries across POK, WLD, AHD, IEC, SYN, KLN, SKT, LEW, HRN, HUB, PHD, NYB, BQT

**transcription_suspect**
- Node 1 (Avestan): `xvâothra` and `xvâjo-ayâo` are not forms any source knows. Verified against the page image (copied to `data/verification/sources/refs/ocr/BOOK/447.png`) — the book really prints them, so `error_in: book`, not an extraction fault. Correct forms: Av. `xʼāθra-` means "comfort", not "self"; `xvâjo-ayâo` renders Hübschmann's conjectural *`xʼatō-āyu-` "living of itself" (the -j- is a misprint for -t-); the attested word is `xʼaδāta-`, `*xʼaδāya-` being Horn's reconstruction.

**plausible (two disputed sub-claims worth flagging)**
- Node 3 (خدا): the gloss "alive from self" is Horn's/Hübschmann's 19th-c. guess, which Nöldeke rejected and Hübschmann (HUB p. 54, the book's own citation) endorses rejecting; the current reconstruction is PIr. \*hwatāwHah- "self-powerful". Also خواجه < خدایچه is rejected by modern scholarship (Asatrian 2011/2012: from Skt. *upādhyāya-* via MIA \*vājjhāa); Mo'in prints it only as one opinion among several.
- Node 5 (خو): Mann IEC 1351 does place Per. *xū* "habit" under \*swet-, but the recorded MP antecedent is *xōg*, pointing to \*hwa-ka- rather than the t-stem.

**Reference problems the owner may want to note (not extraction errors)**
- `BQT:779` (node 3) is 2–4 pages out in Mo'in's edition: خدا is p. 716, خدیو p. 718, خواجه pp. 777–778, خود p. 783 (offset printed = leaf + 540 in `BQT_v2_pages.txt`, verified against running heads).
- `BRT:1862` could not be checked: the local Bartholomae OCR (`BRT.txt`) breaks off around col. 1853, before the xʼā- entries. Worth re-fetching that scan if column-level BRT checks matter on other خ pages.
- Nice hits: `SNS:79` and `SNS:267` are exactly right (confirmed via the volume's own Avestan index), and `IEC:1351` matches nodes 4–5 word for word.

No extraction errors found — the JSON is faithful to the printed page throughout.
